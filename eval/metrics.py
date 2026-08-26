"""Retrieval metrics (plan §10.3).

Two of these are corpus-specific and exist because the standard set hides the
failures that actually matter here:

  version_correctness@1 — is the top hit from the right product version? MRR
      cannot see this: retrieving the Studio 7 page for a Studio 9 question
      scores a perfect 1.0 if the slug matches.

  duplicate_rate@k — what fraction of returned chunks near-duplicate a
      higher-ranked one? With ~98% cross-version slug overlap an uncollapsed
      top-5 can be one paragraph four times and still score well on nDCG.
"""

from __future__ import annotations

import math
from collections import defaultdict
from typing import Iterable, Sequence


def _norm(ref: str) -> str:
    """Compare at page level: an anchor is a finer-grained hit on the same page."""
    return (ref or "").split("#")[0].strip().lower()


def recall_at_k(retrieved: Sequence[str], relevant: Iterable[str], k: int) -> float:
    rel = {_norm(r) for r in relevant}
    if not rel:
        return 0.0
    got = {_norm(r) for r in retrieved[:k]}
    return len(got & rel) / len(rel)


def precision_at_k(retrieved: Sequence[str], relevant: Iterable[str], k: int) -> float:
    rel = {_norm(r) for r in relevant}
    if not k:
        return 0.0
    hits = sum(1 for r in retrieved[:k] if _norm(r) in rel)
    return hits / min(k, max(len(retrieved), 1))


def mrr_at_k(retrieved: Sequence[str], relevant: Iterable[str], k: int) -> float:
    rel = {_norm(r) for r in relevant}
    for i, r in enumerate(retrieved[:k], start=1):
        if _norm(r) in rel:
            return 1.0 / i
    return 0.0


def ndcg_at_k(retrieved: Sequence[str], relevant: Iterable[str], k: int) -> float:
    rel = {_norm(r) for r in relevant}
    dcg = sum(1.0 / math.log2(i + 1)
              for i, r in enumerate(retrieved[:k], start=1) if _norm(r) in rel)
    ideal = sum(1.0 / math.log2(i + 1) for i in range(1, min(len(rel), k) + 1))
    return dcg / ideal if ideal else 0.0


def version_correct_at_1(hits: Sequence[dict], expected_version: str | None,
                         expected_product: str | None = None) -> float | None:
    """None when the item does not pin a version (excluded from the average)."""
    if not expected_version:
        return None
    if not hits:
        return 0.0
    top = hits[0]
    if expected_product and (top.get("product") or "").lower() != expected_product.lower():
        return 0.0
    return 1.0 if str(top.get("version") or "") == str(expected_version) else 0.0


def duplicate_rate_at_k(hits: Sequence[dict], k: int = 5) -> float:
    """Fraction of returned chunks that repeat a higher-ranked (topic, section)."""
    seen: set[tuple] = set()
    dupes = 0
    window = hits[:k]
    for h in window:
        key = (_norm(h.get("ref", "")), (h.get("heading_path") or "").lower())
        if key in seen:
            dupes += 1
        seen.add(key)
    return dupes / max(len(window), 1)


def cross_version_dupe_rate_at_k(hits: Sequence[dict], k: int = 5) -> float:
    """Same section of the same topic returned for two different versions.

    This is the specific failure AD-07 exists to prevent, so it is measured
    separately from generic duplication.
    """
    seen: dict[tuple, str] = {}
    dupes = 0
    for h in hits[:k]:
        slug = _norm(h.get("ref", "")).split("/")[-1]
        key = (h.get("product"), slug, (h.get("heading_path") or "").lower())
        if key in seen and seen[key] != h.get("version"):
            dupes += 1
        seen[key] = h.get("version")
    return dupes / max(len(hits[:k]), 1)


def citation_validity(hits: Sequence[dict], resolver) -> float:
    """Fraction of refs that resolve to a live topic/anchor."""
    if not hits:
        return 1.0
    ok = sum(1 for h in hits if resolver(h.get("ref", "")))
    return ok / len(hits)


def aggregate(rows: list[dict]) -> dict:
    """Mean each metric, skipping None (metric not applicable to that item)."""
    acc: dict[str, list[float]] = defaultdict(list)
    for r in rows:
        for k, v in r.items():
            if isinstance(v, (int, float)) and v is not None:
                acc[k].append(float(v))
    out = {k: round(sum(v) / len(v), 4) for k, v in acc.items() if v}
    out["n"] = len(rows)
    return out


def wilson_interval(p: float, n: int, z: float = 1.96) -> tuple[float, float]:
    """95% CI for a proportion.

    Reported alongside every rate because v1's n=50 gave roughly +/-14pp — wide
    enough that a real regression would pass unnoticed.
    """
    if n == 0:
        return (0.0, 1.0)
    d = 1 + z * z / n
    c = p + z * z / (2 * n)
    m = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n))
    return (max(0.0, (c - m) / d), min(1.0, (c + m) / d))
