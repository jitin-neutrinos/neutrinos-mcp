"""The ranking stack — stages 0..8 (plan §7).

    scope -> (BM25 || dense) -> RRF -> rerank -> variant collapse -> MMR
          -> confidence gate -> [graph expansion] -> assemble

Every stage is separately switchable via `Stages`, because §10.4's ablation
ladder has to be able to turn each one off and measure the delta. A component
that cannot be ablated cannot be shown to earn its place.
"""

from __future__ import annotations

import math
import sqlite3
import time
from dataclasses import dataclass, field
from datetime import date, datetime

import numpy as np

from ..config import PublicationRegistry, Settings
from ..vectorstore import VectorStore
from . import graph as G
from . import lexical
from .fusion import collapse_variants, mmr, normalise, rrf
from .rerank import Reranker, sigmoid
from .scope import ResolvedScope, resolve, version_ambiguous


@dataclass
class Stages:
    """Ablation switches (§10.4). All on = the full stack."""

    bm25: bool = True
    dense: bool = True
    rerank: bool = True
    collapse: bool = True
    mmr: bool = True
    expand: bool = True

    @classmethod
    def rung(cls, n: int) -> "Stages":
        """The ladder in §10.4, rungs 0-7."""
        return {
            0: cls(True, False, False, False, False, False),   # BM25 only
            1: cls(False, True, False, False, False, False),   # dense only
            2: cls(True, True, False, False, False, False),    # + RRF
            3: cls(True, True, False, False, False, False),    # + ctx prefix (index-side)
            4: cls(True, True, True, False, False, False),     # + rerank
            5: cls(True, True, True, True, False, False),      # + collapse
            6: cls(True, True, True, True, True, False),       # + MMR
            7: cls(True, True, True, True, True, True),        # + graph
        }[n]


@dataclass
class Result:
    hits: list[dict] = field(default_factory=list)
    scope: ResolvedScope | None = None
    match_expression: str = ""
    confidence: float = 0.0
    sufficient_evidence: bool = False
    version_ambiguous: bool = False
    timings: dict = field(default_factory=dict)
    diagnostics: dict = field(default_factory=dict)


def _staleness(lastmod: str | None, fresh_m: int, aging_m: int) -> str:
    if not lastmod:
        return "stale"
    try:
        d = datetime.strptime(lastmod[:10], "%Y-%m-%d").date()
    except ValueError:
        return "stale"
    months = (date.today() - d).days / 30.44
    return "fresh" if months < fresh_m else ("aging" if months < aging_m else "stale")


class Pipeline:
    def __init__(self, conn: sqlite3.Connection, store: VectorStore,
                 reg: PublicationRegistry, cfg: Settings,
                 embed_query=None, reranker: Reranker | None = None):
        self.conn = conn
        self.store = store
        self.reg = reg
        self.cfg = cfg
        self._embed = embed_query
        self.reranker = reranker or Reranker(
            cfg["reranker.model"], cfg.get("reranker.preferred"), cfg["reranker.enabled"],
            max_chars=cfg.get("reranker.max_chars", 0),
            threads=cfg.get("reranker.threads"),
            batch_size=cfg.get("reranker.batch_size", 64))

    # ---------------------------------------------------------------- hydrate

    def _hydrate(self, chunk_ids: list[int]) -> dict[int, dict]:
        if not chunk_ids:
            return {}
        q = ",".join("?" * len(chunk_ids))
        rows = self.conn.execute(
            f"""SELECT c.id, c.pub, c.slug, c.anchor, c.heading_path, c.text,
                       c.token_count, c.variant_group_id, c.topic_id,
                       t.title, t.lastmod,
                       p.product, p.version, p.is_current, p.title
                FROM chunk c
                JOIN topic t ON t.id = c.topic_id
                JOIN publication p ON p.id = c.pub
                WHERE c.id IN ({q})""", chunk_ids).fetchall()
        fresh_m, aging_m = self.cfg["staleness.fresh_months"], self.cfg["staleness.aging_months"]
        anchor_tpl = self.cfg["source.anchor_url"]
        reader_tpl = self.cfg["source.reader_url"]
        out = {}
        for (cid, pub, slug, anchor, heading, text, tok, vg, tid,
             title, lastmod, product, version, is_current, pub_title) in rows:
            ref = f"{pub}/{slug}" + (f"#{anchor}" if anchor else "")
            url = (anchor_tpl.format(pub=pub, slug=slug, anchor=anchor) if anchor
                   else reader_tpl.format(pub=pub, slug=slug))
            out[cid] = {
                "chunk_id": cid, "topic_id": tid, "ref": ref, "url": url,
                "title": title, "heading_path": heading or title,
                "product": product, "version": version,
                "is_current": bool(is_current), "publication": pub,
                "last_updated": lastmod,
                "staleness": _staleness(lastmod, fresh_m, aging_m),
                "text": text, "token_count": tok, "_vg": vg,
            }
        return out

    # ---------------------------------------------------------------- search

    def search(self, query: str, product: str | None = None, version: str | None = None,
               include_superseded: bool = False, top_k: int = 6,
               stages: Stages | None = None) -> Result:
        st = stages or Stages()
        cfg = self.cfg
        T: dict[str, int] = {}
        diag: dict = {}

        def tick(name, t0):
            T[name] = int((time.perf_counter() - t0) * 1000)

        # -- 0. scope ------------------------------------------------------
        t0 = time.perf_counter()
        scope = resolve(self.reg, query, product, version, include_superseded)
        tick("scope", t0)

        arms, labels = [], []

        # -- 1a. BM25 ------------------------------------------------------
        match_expr = ""
        if st.bm25:
            t0 = time.perf_counter()
            lex, match_expr = lexical.search(
                self.conn, query, cfg["retrieval.bm25_candidates"], scope.pubs or None)
            tick("bm25", t0)
            diag["bm25_hits"] = len(lex)
            if lex:
                arms.append(lex)
                labels.append("bm25")

        # -- 1b. dense -----------------------------------------------------
        if st.dense and self._embed is not None:
            t0 = time.perf_counter()
            qv = self._embed(cfg["embedding.query_prefix"] + query)
            dense = [(cid, 1.0 - dist) for cid, dist in
                     self.store.query(qv, cfg["retrieval.dense_candidates"],
                                      scope.to_store_scope())]
            tick("dense", t0)
            diag["dense_hits"] = len(dense)
            if dense:
                arms.append(dense)
                labels.append("dense")

        if not arms:
            return Result(scope=scope, match_expression=match_expr,
                          sufficient_evidence=False, timings=T, diagnostics=diag)

        # -- 2. RRF --------------------------------------------------------
        t0 = time.perf_counter()
        fused = rrf(arms, k=cfg["retrieval.rrf_k"], labels=labels)
        tick("rrf", t0)
        provenance = {cid: arms_found for cid, _s, arms_found in fused}
        ranked: list[tuple[int, float]] = [(cid, s) for cid, s, _ in fused][: cfg["retrieval.rerank_input"]]

        # -- 3. rerank -----------------------------------------------------
        rerank_meta = {"status": "disabled"}
        if st.rerank and ranked:
            hyd = self._hydrate([c for c, _ in ranked])
            passages = [f"{hyd[c]['heading_path']}\n{hyd[c]['text']}" for c, _ in ranked if c in hyd]
            ids = [c for c, _ in ranked if c in hyd]
            scores, rerank_meta = self.reranker.score(query, passages)
            # Rerank is 90%+ of query latency on CPU; leaving it out of
            # `timings` made the stage invisible in exactly the traces meant to
            # explain a slow query.
            T["rerank"] = rerank_meta.get("ms", 0)
            if scores:
                ranked = sorted(zip(ids, (sigmoid(s) for s in scores)),
                                key=lambda t: -t[1])
        diag["rerank"] = rerank_meta

        # -- 4. variant collapse ------------------------------------------
        hyd = self._hydrate([c for c, _ in ranked])
        also: dict[int, list[str]] = {}
        if st.collapse:
            t0 = time.perf_counter()
            group_of = {c: hyd[c]["_vg"] for c in hyd}
            version_of = {c: hyd[c]["version"] for c in hyd}
            before = len(ranked)
            ranked, also = collapse_variants(ranked, group_of, version_of)
            tick("collapse", t0)
            diag["collapsed"] = before - len(ranked)

        # -- 5. MMR --------------------------------------------------------
        if st.mmr and len(ranked) > top_k:
            t0 = time.perf_counter()
            scores = dict(ranked)
            norm = dict(zip(scores.keys(), normalise(scores.values())))
            vecs = self.store.vectors_for(list(scores.keys()))
            order = mmr(list(scores.keys()), norm, vecs, top_k, cfg["retrieval.mmr_lambda"])
            ranked = [(c, scores[c]) for c in order]
            tick("mmr", t0)
        else:
            ranked = ranked[:top_k]

        # -- 6/7. confidence gate + graph expansion ------------------------
        top_score = max((s for _, s in ranked), default=0.0)
        expanded, why = (False, "")
        if st.expand and ranked:
            do, why = G.should_expand(query, top_score, cfg["retrieval.low_confidence"])
            if do:
                t0 = time.perf_counter()
                seeds = [hyd[c]["topic_id"] for c, _ in ranked[:3] if c in hyd]
                nbrs = G.neighbours(self.conn, seeds)
                extra_ids = G.chunks_of(self.conn, nbrs, scope.pubs or None)
                extra_ids = [c for c in extra_ids if c not in dict(ranked)]
                if extra_ids and self._embed is not None:
                    ehyd = self._hydrate(extra_ids)
                    passages = [f"{ehyd[c]['heading_path']}\n{ehyd[c]['text']}"
                                for c in extra_ids if c in ehyd]
                    eids = [c for c in extra_ids if c in ehyd]
                    escores, _m = self.reranker.score(query, passages)
                    if escores:
                        scored = sorted(zip(eids, (sigmoid(s) for s in escores)),
                                        key=lambda t: -t[1])
                        keep = [(c, s) for c, s in scored if s >= top_score * 0.6][:3]
                        if keep:
                            hyd.update(self._hydrate([c for c, _ in keep]))
                            for c, _ in keep:
                                provenance.setdefault(c, []).append("graph")
                            ranked = sorted(ranked + keep, key=lambda t: -t[1])[:top_k]
                            expanded = True
                tick("expand", t0)
        diag["expanded"] = expanded
        diag["expand_reason"] = why

        # -- 8. assemble ---------------------------------------------------
        hits = []
        raw = [s for _, s in ranked]
        disp = normalise(raw) if (rerank_meta.get("status") != "ok") else raw
        for (cid, _s), shown in zip(ranked, disp):
            h = hyd.get(cid)
            if not h:
                continue
            out = {k: v for k, v in h.items() if not k.startswith("_")}
            out["score"] = round(float(shown), 4)
            out["retrieved_by"] = provenance.get(cid, [])
            if also.get(cid):
                out["also_in_versions"] = also[cid]
            hits.append(out)

        conf = round(float(hits[0]["score"]) if hits else 0.0, 4)
        sufficient = bool(hits) and conf >= cfg["retrieval.low_confidence"]
        return Result(
            hits=hits, scope=scope, match_expression=match_expr,
            confidence=conf, sufficient_evidence=sufficient,
            version_ambiguous=version_ambiguous(hits, scope),
            timings=T, diagnostics=diag,
        )
