"""Stage 4 — index (plan §6.4).

Builds `data/neutrinos.db.new` from nothing, verifies it, then atomically
replaces the live file. The build is idempotent by construction: there is no
migration path because there is never an old file to migrate.

Order matters in two places:

* chunk <-> variant_group is a declared cycle, so chunks load with a NULL
  variant_group_id, groups are computed, then chunks are updated (§5.4 note 3).
* FTS5 external-content indexes are populated by a single 'rebuild' after bulk
  load, not by per-row triggers.

    python -m neutrinos_mcp.ingest.index
    python -m neutrinos_mcp.ingest.index --backend chroma
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import sqlite3
import sys
import time
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

import numpy as np

from ..config import ROOT, publications, settings
from ..vectorstore import SqliteVecStore, open_store
from .simhash import group_variants, to_unsigned

SCHEMA_VERSION = "2.0"


# ------------------------------------------------------------------ embeddings


class Embedder:
    """fastembed / ONNX. CPU-only, no torch (plan §4.4)."""

    def __init__(self, model: str, dim: int, batch_size: int = 32, threads: int | None = None):
        from fastembed import TextEmbedding

        self.model_name = model
        self.dim = dim
        self.batch_size = batch_size
        # Explicit thread count: leaving it to ORT's default measured 2.3x slower.
        kw = {"threads": threads} if threads else {}
        self._m = TextEmbedding(model_name=model, **kw)

    def encode(self, texts: list[str]) -> np.ndarray:
        out = np.asarray(list(self._m.embed(texts, batch_size=self.batch_size)), dtype=np.float32)
        if out.shape[1] != self.dim:
            raise RuntimeError(
                f"embedding dim {out.shape[1]} != configured {self.dim}; "
                f"settings.toml and the model disagree (AD-12)")
        # cosine space: normalise once here so distance == 1 - dot
        norms = np.linalg.norm(out, axis=1, keepdims=True)
        return out / np.clip(norms, 1e-9, None)


# ----------------------------------------------------------------------- build


def _connect(path: Path) -> sqlite3.Connection:
    conn = sqlite3.connect(path)
    conn.execute("PRAGMA foreign_keys = ON")
    conn.execute("PRAGMA synchronous = OFF")
    conn.execute("PRAGMA cache_size = -262144")
    conn.execute("PRAGMA temp_store = MEMORY")
    return conn


def build(backend: str | None = None, limit: int | None = None) -> dict:
    cfg = settings()
    reg = publications()
    t0 = time.time()
    backend = backend or cfg["vector_store.backend"]

    build_path = ROOT / cfg["paths.db_build"]
    build_path.parent.mkdir(parents=True, exist_ok=True)
    for stale in (build_path, Path(str(build_path) + "-wal"), Path(str(build_path) + "-shm")):
        stale.unlink(missing_ok=True)

    conn = _connect(build_path)
    SqliteVecStore.load_extension(conn)
    conn.executescript((Path(__file__).parent / "schema.sql").read_text(encoding="utf-8"))

    stats: dict = {"backend": backend, "schema_version": SCHEMA_VERSION}

    # -- publications ------------------------------------------------------
    conn.executemany(
        """INSERT INTO publication
           (id,title,product,version,version_rank,family,is_current,lifecycle,topic_count,newest_lastmod)
           VALUES (?,?,?,?,?,?,?,?,0,NULL)""",
        [(p.id, p.title, p.product, p.version, p.version_rank, p.family,
          int(p.is_current), p.lifecycle) for p in reg],
    )
    stats["publications"] = len(reg)

    # -- topics ------------------------------------------------------------
    topics: dict[tuple[str, str], int] = {}
    topic_rows, code_rows = [], []
    pending_edges: list[tuple[str, str, str, str, str]] = []  # src_pub,src_slug,rel,dst_pub,dst_slug
    tid = 0
    with (ROOT / "data" / "topics.jsonl").open(encoding="utf-8") as fh:
        for n, line in enumerate(fh, 1):
            if limit and n > limit:
                break
            t = json.loads(line)
            if t["pub"] not in reg:
                raise KeyError(f"publication '{t['pub']}' unclassified — see §6.5")
            tid += 1
            topics[(t["pub"], t["slug"])] = tid
            topic_rows.append((tid, t["pub"], t["slug"], t["title"], t.get("breadcrumb") or t["title"],
                               t["url"], t.get("lastmod"), t["word_count"], t["content_hash"], t["body_md"]))
            for cs in t.get("code_samples", []):
                code_rows.append((tid, cs.get("lang"), cs["code"]))
            for rel, val in (("NEXT", t.get("next")), ("PREV", t.get("prev"))):
                if val and "/" in val:
                    dp, ds = val.split("/", 1)
                    pending_edges.append((t["pub"], t["slug"], rel, dp, ds))
            for l in t.get("see_also", []):
                if l.get("target_pub") and l.get("target_slug"):
                    pending_edges.append((t["pub"], t["slug"], "SEE_ALSO", l["target_pub"], l["target_slug"]))
            for l in t.get("links", []):
                if l.get("target_pub") and l.get("target_slug"):
                    pending_edges.append((t["pub"], t["slug"], "LINKS_TO", l["target_pub"], l["target_slug"]))

    conn.executemany(
        """INSERT INTO topic (id,pub,slug,title,breadcrumb,url,lastmod,word_count,content_hash,body_md)
           VALUES (?,?,?,?,?,?,?,?,?,?)""", topic_rows)
    conn.executemany("INSERT INTO code_sample (topic_id,lang,code) VALUES (?,?,?)", code_rows)
    stats["topics"] = len(topic_rows)
    stats["code_samples"] = len(code_rows)

    conn.execute("""UPDATE publication SET
                      topic_count    = (SELECT count(*) FROM topic WHERE topic.pub = publication.id),
                      newest_lastmod = (SELECT max(lastmod) FROM topic WHERE topic.pub = publication.id)""")

    # -- chunks ------------------------------------------------------------
    chunk_rows, chunk_meta = [], []
    cid = 0
    with (ROOT / "data" / "chunks.jsonl").open(encoding="utf-8") as fh:
        for line in fh:
            c = json.loads(line)
            key = (c["pub"], c["slug"])
            if key not in topics:
                continue
            cid += 1
            chunk_rows.append((cid, topics[key], c["pub"], c["slug"], c["ordinal"],
                               c["heading_path"], c["anchor"], c["level"], c["text"],
                               c["context_prefix"], c["token_count"], int(c["has_code"]),
                               c["simhash"]))
            chunk_meta.append(c)
    conn.executemany(
        """INSERT INTO chunk (id,topic_id,pub,slug,ordinal,heading_path,anchor,level,
                              text,context_prefix,token_count,has_code,simhash)
           VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)""", chunk_rows)
    stats["chunks"] = len(chunk_rows)
    conn.commit()

    # -- Agentic GraphRAG Entities & Relations -----------------------------
    entities_path = ROOT / "data" / "entities.jsonl"
    relations_path = ROOT / "data" / "relations.jsonl"
    if entities_path.exists() and relations_path.exists():
        entity_rows = []
        eid_map = {}
        eid = 0
        with entities_path.open(encoding="utf-8") as fh:
            for line in fh:
                e = json.loads(line)
                eid += 1
                eid_map[e["id"]] = eid
                entity_rows.append((eid, e["name"], e["category"], e.get("description", "")))
        conn.executemany("INSERT INTO entity (id,name,category,description) VALUES (?,?,?,?)", entity_rows)
        
        relation_rows = []
        with relations_path.open(encoding="utf-8") as fh:
            for line in fh:
                r = json.loads(line)
                if r["src"] in eid_map and r["dst"] in eid_map:
                    relation_rows.append((eid_map[r["src"]], r["rel"], eid_map[r["dst"]], r["chunk_id"]))
        conn.executemany("INSERT OR IGNORE INTO entity_relation (src_id,rel_type,dst_id,chunk_id) VALUES (?,?,?,?)", relation_rows)
        conn.commit()
        stats["entities"] = len(entity_rows)
        stats["entity_relations"] = len(relation_rows)

    # -- edges -------------------------------------------------------------
    edges: set[tuple] = set()
    for sp, ss, rel, dp, ds in pending_edges:
        src = topics.get((sp, ss))
        if src is None:
            continue
        dst = topics.get((dp, ds))
        if src == dst:
            continue  # self-edge
        edges.add((src, rel, dp, ds, dst, 1 if dst else 0))

    # SAME_TOPIC_OTHER_VERSION — the edge that makes version disambiguation work.
    # Built from family + slug, NOT name similarity, so it spans the renames.
    by_family_slug: dict[tuple[str, str], list[tuple[str, str]]] = defaultdict(list)
    for (pub, slug) in topics:
        by_family_slug[(reg.get(pub).family, slug)].append((pub, slug))
    same_ver = 0
    for (_fam, _slug), members in by_family_slug.items():
        if len(members) < 2:
            continue
        for a in members:
            for b in members:
                if a == b:
                    continue
                edges.add((topics[a], "SAME_TOPIC_OTHER_VERSION", b[0], b[1], topics[b], 1))
                same_ver += 1

    # SUPERSEDED_BY — publication-level, projected onto topics with the same slug
    sup = 0
    for fam, pubs in reg.products().items():
        ordered = sorted(pubs, key=lambda p: p.version_rank)
        for older, newer in zip(ordered, ordered[1:]):
            for (pub, slug), t_id in topics.items():
                if pub != older.id:
                    continue
                tgt = topics.get((newer.id, slug))
                if tgt:
                    edges.add((t_id, "SUPERSEDED_BY", newer.id, slug, tgt, 1))
                    sup += 1

    conn.executemany(
        "INSERT OR IGNORE INTO edge (src_id,rel,dst_pub,dst_slug,dst_id,resolved) VALUES (?,?,?,?,?,?)",
        list(edges))
    stats["edges"] = conn.execute("SELECT count(*) FROM edge").fetchone()[0]
    stats["edges_by_rel"] = dict(conn.execute("SELECT rel, count(*) FROM edge GROUP BY rel").fetchall())
    stats["unresolved_edges"] = conn.execute("SELECT count(*) FROM edge WHERE resolved=0").fetchone()[0]
    conn.commit()

    # -- variant groups (AD-07) -------------------------------------------
    # Exact key = "same section of the same topic across versions"; SimHash is
    # then only a guard on whether the content is close enough to collapse.
    keyed: list[tuple[int, str, int]] = []
    for row, c in zip(chunk_rows, chunk_meta):
        key = f"{c['family']}|{c['slug']}|{c['heading_path']}"
        keyed.append((row[0], key, to_unsigned(c["simhash"])))

    rank_of = {p.id: p.version_rank for p in reg}
    fam_of = {row[0]: reg.get(row[2]).family for row in chunk_rows}
    pub_of = {row[0]: row[2] for row in chunk_rows}
    ver_of = {p.id: p.version for p in reg}
    gid = 0
    vg_rows, upd = [], []
    for _key, members in group_variants(keyed, cfg["retrieval.simhash_hamming"]).items():
        gid += 1
        canonical = max(members, key=lambda c: rank_of.get(pub_of[c], 0))
        versions = sorted({ver_of.get(pub_of[c]) or "-" for c in members})
        vg_rows.append((gid, fam_of[canonical], canonical, len(members), json.dumps(versions)))
        upd += [(gid, c) for c in members]
    conn.executemany(
        "INSERT INTO variant_group (id,family,canonical_chunk_id,member_count,versions_json) VALUES (?,?,?,?,?)",
        vg_rows)
    conn.executemany("UPDATE chunk SET variant_group_id=? WHERE id=?", upd)
    stats["variant_groups"] = len(vg_rows)
    stats["chunks_in_groups"] = len(upd)
    conn.commit()

    # -- FTS ---------------------------------------------------------------
    conn.execute("INSERT INTO chunk_fts(chunk_fts) VALUES('rebuild')")
    conn.execute("INSERT INTO topic_fts(topic_fts) VALUES('rebuild')")
    conn.commit()

    # -- embeddings --------------------------------------------------------
    emb = Embedder(cfg["embedding.model"], cfg["embedding.dim"],
                   cfg["embedding.batch_size"], cfg.get("embedding.threads"))
    store = open_store(backend, conn=conn, chroma_path=ROOT / cfg["paths.chroma"])
    store.create(cfg["embedding.dim"])

    texts = [f"{c['context_prefix']}\n---\n{c['text']}" for c in chunk_meta]
    B = 256
    print(f"  embedding {len(texts)} chunks with {cfg['embedding.model']} -> {backend}", flush=True)
    t_emb = time.time()
    for i in range(0, len(texts), B):
        vecs = emb.encode(texts[i : i + B])
        rows = []
        for j, v in enumerate(vecs):
            r = chunk_rows[i + j]
            p = reg.get(r[2])
            rows.append({"chunk_id": r[0], "vector": v, "pub": p.id, "family": p.family,
                         "version_rank": p.version_rank, "is_current": int(p.is_current),
                         "heading_path": r[5]})
        store.add(rows)
        # Commit per batch. Holding 7,810 vec0 inserts in one transaction cost
        # ~2.8 GB of RSS and made progress invisible to a read-only observer.
        conn.commit()
        done = min(i + B, len(texts))
        el = time.time() - t_emb
        print(f"    {done}/{len(texts)}  ({done/max(el,1e-9):.1f}/s, "
              f"eta {int((len(texts)-done)/max(done/max(el,1e-9),1e-9))}s)", flush=True)
    conn.commit()
    stats["vectors"] = store.count()

    # -- manifest (AD-12) --------------------------------------------------
    corpus_hash = hashlib.sha256(
        b"".join(r[8].encode() for r in topic_rows)).hexdigest()[:32]
    pub_hash = hashlib.sha256(
        (ROOT / cfg["paths.publications"]).read_bytes()).hexdigest()[:32]
    manifest = {
        "schema_version": SCHEMA_VERSION,
        "embedding_model": cfg["embedding.model"],
        "embedding_dim": str(cfg["embedding.dim"]),
        "embedding_query_prefix": cfg["embedding.query_prefix"],
        "reranker_model": cfg["reranker.model"],
        "chunker_version": cfg["chunking.chunker_version"],
        "vector_backend": backend,
        "corpus_hash": corpus_hash,
        "publications_yaml_hash": pub_hash,
        # RFC 3339 requires a time-offset ("Z" or +HH:MM) on a date-time value;
        # `time.strftime` produced neither (bare local time, no zone at all) --
        # valid enough for Python's own lenient `datetime.fromisoformat`, but
        # rejected by stricter RFC 3339 validators (confirmed: Claude Desktop's
        # MCP client rejected `index_built_at` built this way). `list_products`
        # additionally coerces older manifests built before this fix.
        "built_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "topic_count": str(len(topic_rows)),
        "chunk_count": str(len(chunk_rows)),
    }
    conn.executemany("INSERT INTO build_manifest (key,value) VALUES (?,?)", list(manifest.items()))

    conn.execute("PRAGMA optimize")
    conn.commit()
    integrity = conn.execute("PRAGMA integrity_check").fetchone()[0]
    if integrity != "ok":
        raise RuntimeError(f"integrity_check failed: {integrity}")
    fk = conn.execute("PRAGMA foreign_key_check").fetchall()
    if fk:
        raise RuntimeError(f"foreign_key_check failed: {fk[:3]}")
    conn.close()

    # VACUUM needs its own connection outside a transaction
    v = sqlite3.connect(build_path)
    v.execute("VACUUM")
    v.close()

    stats["duration_s"] = round(time.time() - t0, 1)
    stats["db_bytes"] = build_path.stat().st_size
    stats["manifest"] = manifest
    return stats


def mirror_to_chroma(db_path: Path) -> dict:
    """Copy vectors from the built DB into ChromaDB without re-embedding.

    Lets the Chroma backend be a live, swap-in alternate (R5) at the cost of a
    copy rather than a second embedding pass. Vectors are supplied explicitly,
    so Chroma never runs an embedding model of its own — the two stores are
    guaranteed to hold identical numbers.
    """
    cfg = settings()
    reg = publications()
    conn = sqlite3.connect(f"file:{db_path}?mode=ro", uri=True)
    SqliteVecStore.load_extension(conn)
    src = SqliteVecStore(conn)
    dst = open_store("chroma", chroma_path=ROOT / cfg["paths.chroma"])
    dst.create(cfg["embedding.dim"])

    ids = [int(r[0]) for r in conn.execute("SELECT id FROM chunk ORDER BY id")]
    meta = {int(r[0]): (r[1], r[2]) for r in conn.execute("SELECT id, pub, heading_path FROM chunk")}
    B = 500
    for i in range(0, len(ids), B):
        batch = ids[i : i + B]
        vecs = src.vectors_for(batch)
        rows = []
        for cid in batch:
            if cid not in vecs:
                continue
            pub_id, heading = meta[cid]
            p = reg.get(pub_id)
            rows.append({"chunk_id": cid, "vector": vecs[cid], "pub": p.id, "family": p.family,
                         "version_rank": p.version_rank, "is_current": int(p.is_current),
                         "heading_path": heading})
        if rows:
            dst.add(rows)
    n = dst.count()
    conn.close()
    return {"chroma_path": str(ROOT / cfg["paths.chroma"]), "chroma_vectors": n}


def publish() -> Path:
    """Atomic swap: keep the previous file for one-command rollback (§11)."""
    cfg = settings()
    live, new, prev = (ROOT / cfg["paths.db"], ROOT / cfg["paths.db_build"], ROOT / cfg["paths.db_prev"])
    if live.exists():
        prev.unlink(missing_ok=True)
        os.replace(live, prev)
    for suffix in ("-wal", "-shm"):
        Path(str(new) + suffix).unlink(missing_ok=True)
    os.replace(new, live)
    return live


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--backend", choices=["sqlite-vec", "chroma"], default=None)
    ap.add_argument("--limit", type=int, default=None)
    ap.add_argument("--no-publish", action="store_true")
    ap.add_argument("--also-chroma", action="store_true",
                    help="mirror vectors into ChromaDB after building (no re-embedding)")
    args = ap.parse_args()

    stats = build(backend=args.backend, limit=args.limit)
    if not args.no_publish:
        stats["published_to"] = str(publish())
    if args.also_chroma:
        target = ROOT / settings()["paths.db"] if not args.no_publish else ROOT / settings()["paths.db_build"]
        print("  mirroring vectors into ChromaDB ...")
        stats.update(mirror_to_chroma(target))
    (ROOT / "data" / "index_report.json").write_text(json.dumps(stats, indent=2), encoding="utf-8")
    print(json.dumps({k: v for k, v in stats.items() if k != "manifest"}, indent=2))


if __name__ == "__main__":
    main()
