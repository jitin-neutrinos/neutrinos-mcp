"""The query contract (plan §4.2, §5.3).

Every query, every validation rule and every error lives here. `server.py` and
`cli.py` translate arguments in and format results out and contain no SQL, so
the MCP path and the evaluation path exercise identical code — which is the
only reason offline metrics predict online behaviour.

Read-only by construction: connections open with `mode=ro` and `query_only`,
and no method builds SQL by string interpolation of user input.
"""

from __future__ import annotations

import re
import sqlite3
from pathlib import Path
from typing import Any

import numpy as np

from .config import ROOT, publications, settings
from .errors import KBError, invalid, not_found, unavailable
from .retrieval.graph import typed_neighbourhood
from .retrieval.pipeline import Pipeline, Result, Stages
from .retrieval.rerank import Reranker
from .vectorstore import SqliteVecStore, open_store

_REF = re.compile(r"^(?P<pub>[a-z0-9][a-z0-9-]*)/(?P<slug>[a-z0-9][a-z0-9._-]*)(?:#(?P<anchor>[A-Za-z0-9_-]+))?$")


def parse_ref(ref: str) -> tuple[str, str, str | None]:
    m = _REF.match((ref or "").strip())
    if not m:
        raise invalid(
            f"'{ref}' is not a valid ref. Expected '<publication>/<slug>' with an "
            f"optional '#<anchor>', e.g. 'studio-guide-9/data-binding#h3_1689083776'. "
            f"Copy it verbatim from a search_docs result.")
    return m.group("pub"), m.group("slug"), m.group("anchor")


def _reranker(cfg) -> Reranker:
    """One construction site for the re-ranker, so the pipeline and the server
    cannot disagree about its budget knobs."""
    return Reranker(
        cfg["reranker.model"],
        cfg.get("reranker.preferred"),
        cfg["reranker.enabled"],
        max_chars=cfg.get("reranker.max_chars", 0),
        threads=cfg.get("reranker.threads"),
        batch_size=cfg.get("reranker.batch_size", 64),
    )


class QueryEmbedder:
    """Query-side embedding. Applies the model's required asymmetric prefix.

    BGE models expect the instruction on the QUERY side only. Omitting it does
    not error — it silently degrades every result — so it is applied here, once,
    from the value recorded in the build manifest rather than a literal.
    """

    def __init__(self, model: str, threads: int | None = None):
        from fastembed import TextEmbedding

        kw = {"threads": threads} if threads else {}
        self._m = TextEmbedding(model_name=model, **kw)

    def __call__(self, text: str) -> np.ndarray:
        v = next(iter(self._m.embed([text])))
        v = np.asarray(v, dtype=np.float32)
        n = float(np.linalg.norm(v))
        return v / (n if n > 1e-9 else 1.0)


class KnowledgeBase:
    MAX_LIMIT = 200

    def __init__(self, db_path: str | Path | None = None, lazy_models: bool = True):
        self.cfg = settings()
        self.reg = publications()
        # NB: the attribute is `db_path`, not `path` — `path` would shadow a
        # query method on any future traversal API.
        self.db_path = Path(db_path) if db_path else (ROOT / self.cfg["paths.db"])
        if not self.db_path.exists():
            raise unavailable(
                f"No index at {self.db_path}. Build it with "
                f"`python -m neutrinos_mcp.ingest.index`.")
        self.conn = sqlite3.connect(f"file:{self.db_path}?mode=ro", uri=True,
                                    check_same_thread=False)
        self.conn.execute("PRAGMA query_only = ON")
        self.conn.execute("PRAGMA mmap_size = 268435456")
        SqliteVecStore.load_extension(self.conn)

        self.manifest = dict(self.conn.execute("SELECT key, value FROM build_manifest"))
        self._verify_manifest()

        backend = self.manifest.get("vector_backend", self.cfg["vector_store.backend"])
        self.store = open_store(backend, conn=self.conn,
                                chroma_path=ROOT / self.cfg["paths.chroma"])
        self._embedder: QueryEmbedder | None = None
        self._pipeline: Pipeline | None = None
        if not lazy_models:
            self._ensure_models()

    # ------------------------------------------------------------ lifecycle

    def _verify_manifest(self) -> None:
        """AD-12. Serving vectors built by another model is silent and total."""
        want_model = self.cfg["embedding.model"]
        got_model = self.manifest.get("embedding_model")
        if got_model and got_model != want_model:
            raise unavailable(
                f"Index was built with embedding model '{got_model}' but settings.toml "
                f"says '{want_model}'. Queries would be embedded into a different space "
                f"than the index. Rebuild the index or restore the setting.")
        want_dim = str(self.cfg["embedding.dim"])
        got_dim = self.manifest.get("embedding_dim")
        if got_dim and got_dim != want_dim:
            raise unavailable(f"Index dim {got_dim} != configured {want_dim}.")

    def _ensure_models(self) -> None:
        if self._pipeline is None:
            self._embedder = QueryEmbedder(self.cfg["embedding.model"],
                                           self.cfg.get("embedding.threads"))
            self._pipeline = Pipeline(
                self.conn, self.store, self.reg, self.cfg,
                embed_query=self._embedder,
                reranker=_reranker(self.cfg))

    def close(self) -> None:
        try:
            self.conn.close()
        except Exception:
            pass

    # --------------------------------------------------------------- search

    def search(self, query: str, product: str | None = None, version: str | None = None,
               include_superseded: bool = False, top_k: int = 6,
               stages: Stages | None = None) -> Result:
        if not query or len(query.strip()) < 2:
            raise invalid("`query` must be at least 2 characters.")
        top_k = self._clamp_top_k(top_k)
        self._ensure_models()
        try:
            return self._pipeline.search(  # type: ignore[union-attr]
                query, product, version, include_superseded, top_k, stages)
        except ValueError as exc:  # unknown product/version from scope.resolve
            raise invalid(str(exc), self._product_suggestions()) from None

    def _clamp_top_k(self, k: int) -> int:
        mx = self.cfg["retrieval.max_top_k"]
        if not isinstance(k, int) or k < 1:
            raise invalid(f"`top_k` must be an integer >= 1 (got {k!r}).")
        return min(k, mx)

    def _product_suggestions(self, limit: int = 12) -> list[dict]:
        rows = self.conn.execute(
            "SELECT DISTINCT product FROM publication ORDER BY topic_count DESC LIMIT ?",
            (limit,)).fetchall()
        return [{"value": r[0], "field": "product"} for r in rows]

    # ------------------------------------------------------------- document

    def topic_row(self, pub: str, slug: str) -> sqlite3.Row | tuple:
        row = self.conn.execute(
            """SELECT t.id, t.pub, t.slug, t.title, t.breadcrumb, t.url, t.lastmod,
                      t.word_count, t.body_md, p.product, p.version, p.is_current
               FROM topic t JOIN publication p ON p.id = t.pub
               WHERE t.pub = ? AND t.slug = ?""", (pub, slug)).fetchone()
        if row:
            return row
        alts = self.conn.execute(
            "SELECT pub, slug, title FROM topic WHERE slug = ? LIMIT 5", (slug,)).fetchall()
        sugg = [{"value": f"{a[0]}/{a[1]}", "label": a[2], "field": "ref"} for a in alts]
        if not sugg:
            near = self.conn.execute(
                "SELECT pub, slug, title FROM topic WHERE slug LIKE ? LIMIT 5",
                (f"%{slug[:20]}%",)).fetchall()
            sugg = [{"value": f"{n[0]}/{n[1]}", "label": n[2], "field": "ref"} for n in near]
        raise not_found("topic", f"No topic '{pub}/{slug}'.", sugg)

    def sections_of(self, topic_id: int) -> list[dict]:
        rows = self.conn.execute(
            """SELECT anchor, heading_path, token_count, text, ordinal
               FROM chunk WHERE topic_id = ? ORDER BY ordinal""", (topic_id,)).fetchall()
        return [{"anchor": r[0], "heading_path": r[1], "token_count": r[2],
                 "text": r[3], "ordinal": r[4]} for r in rows]

    def code_samples_of(self, topic_id: int) -> list[dict]:
        rows = self.conn.execute(
            "SELECT lang, code FROM code_sample WHERE topic_id = ?", (topic_id,)).fetchall()
        return [{"lang": r[0], "code": r[1]} for r in rows]

    def other_versions_of(self, pub: str, slug: str) -> list[str]:
        fam = self.reg.get(pub).family
        rows = self.conn.execute(
            """SELECT p.version FROM topic t JOIN publication p ON p.id = t.pub
               WHERE t.slug = ? AND p.family = ? AND t.pub != ?""", (slug, fam, pub)).fetchall()
        return sorted({r[0] for r in rows if r[0]})

    # ---------------------------------------------------------------- graph

    def related(self, pub: str, slug: str, limit_per_relation: int = 10) -> dict:
        row = self.topic_row(pub, slug)
        return typed_neighbourhood(self.conn, int(row[0]), limit_per_relation)

    # ------------------------------------------------------------- versions

    def compare_versions(self, slug: str, product: str | None = None,
                         versions: list[str] | None = None) -> dict:
        fam = None
        if product:
            fam = self.reg.resolve_product(product)
            if not fam:
                raise invalid(f"Unknown product '{product}'.", self._product_suggestions())
        rows = self.conn.execute(
            """SELECT t.pub, t.slug, t.title, t.url, t.lastmod, t.content_hash,
                      p.product, p.version, p.is_current, p.family, p.version_rank
               FROM topic t JOIN publication p ON p.id = t.pub
               WHERE t.slug = ?""", (slug,)).fetchall()
        if fam:
            rows = [r for r in rows if r[9] == fam]
        if not rows:
            near = self.conn.execute(
                "SELECT DISTINCT slug FROM topic WHERE slug LIKE ? LIMIT 5",
                (f"%{slug[:20]}%",)).fetchall()
            raise not_found("topic", f"No topic with slug '{slug}'"
                            + (f" in product '{product}'." if product else "."),
                            [{"value": n[0], "field": "slug"} for n in near])
        fams = {r[9] for r in rows}
        if len(fams) > 1 and not fam:
            raise invalid(
                f"Slug '{slug}' exists in several products ({', '.join(sorted(fams))}). "
                f"Pass `product` to disambiguate.",
                [{"value": f, "field": "product"} for f in sorted(fams)])
        rows.sort(key=lambda r: r[10])
        if versions:
            rows = [r for r in rows if (r[7] or "") in {str(v) for v in versions}]
        return {"rows": rows, "family": next(iter(fams))}

    def section_hashes(self, pub: str, slug: str) -> dict[str, int]:
        rows = self.conn.execute(
            """SELECT c.heading_path, c.simhash FROM chunk c
               WHERE c.pub = ? AND c.slug = ?""", (pub, slug)).fetchall()
        return {r[0]: int(r[1]) for r in rows}

    # -------------------------------------------------------------- catalog

    def products(self, include_archived: bool = False,
                 name_contains: str | None = None) -> list[dict]:
        out: list[dict] = []
        for fam, pubs in self.reg.products().items():
            keep = [p for p in pubs if include_archived or p.lifecycle != "archived"]
            if not keep:
                continue
            name = keep[0].product
            if name_contains and name_contains.lower() not in name.lower():
                continue
            counts = dict(self.conn.execute(
                "SELECT id, topic_count FROM publication").fetchall())
            newest = dict(self.conn.execute(
                "SELECT id, newest_lastmod FROM publication").fetchall())
            aliases = [k for k, v in self.reg._aliases.items() if v == fam]  # noqa: SLF001
            out.append({
                "product": name,
                "aliases": sorted({a.title() for a in aliases}),
                "versions": [{
                    "version": p.version, "publication": p.id,
                    "is_current": p.is_current, "lifecycle": p.lifecycle,
                    "topic_count": counts.get(p.id, 0),
                    "newest_lastmod": newest.get(p.id),
                } for p in keep],
            })
        return sorted(out, key=lambda d: d["product"])

    def stats(self) -> dict:
        g = lambda q: self.conn.execute(q).fetchone()[0]  # noqa: E731
        return {
            "publications": g("SELECT count(*) FROM publication"),
            "topics": g("SELECT count(*) FROM topic"),
            "chunks": g("SELECT count(*) FROM chunk"),
            "edges": g("SELECT count(*) FROM edge"),
            "variant_groups": g("SELECT count(*) FROM variant_group"),
            "code_samples": g("SELECT count(*) FROM code_sample"),
            "vectors": self.store.count(),
            "manifest": self.manifest,
        }
