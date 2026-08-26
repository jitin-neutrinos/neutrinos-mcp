"""Stage 2 — Reciprocal Rank Fusion, plus MMR and variant collapse helpers.

RRF (Cormack, Clarke & Buettcher, SIGIR 2009): score(d) = sum 1/(k + rank_i(d)).

It operates on RANKS, not scores, which is exactly why it suits this pipeline:
BM25 returns unbounded negative-log-odds and cosine returns [0,2]. Any
score-level combination needs per-corpus calibration that drifts the moment the
corpus or the model changes. RRF needs none, and k=60 is the published default.
"""

from __future__ import annotations

from collections import defaultdict
from typing import Iterable, Sequence

import numpy as np


def rrf(
    ranked_lists: Sequence[Sequence[tuple[int, float]]],
    k: int = 60,
    weights: Sequence[float] | None = None,
    labels: Sequence[str] | None = None,
) -> list[tuple[int, float, list[str]]]:
    """Fuse ranked lists. Returns [(id, fused_score, which_arms_found_it)]."""
    w = list(weights) if weights else [1.0] * len(ranked_lists)
    lbl = list(labels) if labels else [f"arm{i}" for i in range(len(ranked_lists))]
    scores: dict[int, float] = defaultdict(float)
    provenance: dict[int, list[str]] = defaultdict(list)
    for arm, lst in enumerate(ranked_lists):
        for rank, (doc_id, _s) in enumerate(lst, start=1):
            scores[doc_id] += w[arm] / (k + rank)
            provenance[doc_id].append(lbl[arm])
    return sorted(
        ((d, s, provenance[d]) for d, s in scores.items()),
        key=lambda t: -t[1],
    )


def normalise(scores: Iterable[float]) -> list[float]:
    """Min-max to [0,1] for display. Never used for ranking decisions."""
    xs = list(scores)
    if not xs:
        return []
    lo, hi = min(xs), max(xs)
    if hi - lo < 1e-9:
        return [1.0 if hi > 0 else 0.0] * len(xs)
    return [(x - lo) / (hi - lo) for x in xs]


def mmr(
    candidates: Sequence[int],
    scores: dict[int, float],
    vectors: dict[int, np.ndarray],
    top_k: int,
    lam: float = 0.7,
) -> list[int]:
    """Maximal Marginal Relevance (Carbonell & Goldstein).

    Stops three sections of one page from consuming the whole budget when the
    answer needs two different pages. Candidates without a vector are never
    dropped — they fall through on relevance alone.
    """
    if top_k <= 0 or not candidates:
        return []
    pool = [c for c in candidates]
    selected: list[int] = []
    while pool and len(selected) < top_k:
        best, best_val = None, -1e18
        for c in pool:
            rel = scores.get(c, 0.0)
            if not selected or c not in vectors:
                val = lam * rel
            else:
                vc = vectors[c]
                sims = [
                    float(np.dot(vc, vectors[s]))
                    for s in selected
                    if s in vectors
                ]
                val = lam * rel - (1.0 - lam) * (max(sims) if sims else 0.0)
            if val > best_val:
                best, best_val = c, val
        selected.append(best)  # type: ignore[arg-type]
        pool.remove(best)      # type: ignore[arg-type]
    return selected


def collapse_variants(
    ranked: Sequence[tuple[int, float]],
    group_of: dict[int, int | None],
    version_of: dict[int, str | None],
) -> tuple[list[tuple[int, float]], dict[int, list[str]]]:
    """Stage 4 — cross-version near-duplicate collapse (AD-07).

    Keeps the highest-ranked member of each variant group and records which
    other product versions carry the same content. On this corpus that is worth
    more top-k slots than any model swap: components-guide-7 and -8 share 99 of
    99 slugs, so an uncollapsed top-5 can be one paragraph four times.

    The dropped versions are not lost — they become `also_in_versions`, which
    turns the corpus's redundancy from a liability into a signal that the answer
    is version-independent.
    """
    seen: dict[int, int] = {}
    out: list[tuple[int, float]] = []
    also: dict[int, list[str]] = {}
    for cid, score in ranked:
        gid = group_of.get(cid)
        if gid is None:
            out.append((cid, score))
            continue
        if gid not in seen:
            seen[gid] = cid
            out.append((cid, score))
            also[cid] = []
        else:
            keeper = seen[gid]
            v = version_of.get(cid)
            if v and v not in also.setdefault(keeper, []):
                also[keeper].append(v)
    for cid in also:
        also[cid] = sorted(set(also[cid]), key=lambda x: (len(x), x))
    return out, also
