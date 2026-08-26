"""64-bit SimHash and variant grouping (plan AD-07, §6.4 step 3).

This is the highest-value component in the retrieval stack for this corpus.
Measured: `components-guide-7` and `-8` share 99 of 99 slugs; `studio-guide-8`
and `-9` share 115 of 117. Without collapse, a top-5 can be one paragraph
repeated four times — the context budget is spent without the context widening.

SimHash over token shingles rather than exact hashing, because versions differ
in trivial ways (a renamed menu item, a changed screenshot path) that must
still collapse. Hamming distance <= 3 on 64 bits is the operating point.
"""

from __future__ import annotations

import hashlib
import re
from collections import defaultdict

_TOKEN = re.compile(r"[a-z0-9]+")
_MASK = (1 << 64) - 1


def _shingles(text: str, k: int = 3) -> list[str]:
    toks = _TOKEN.findall(text.lower())
    if len(toks) < k:
        return toks or [""]
    return [" ".join(toks[i : i + k]) for i in range(len(toks) - k + 1)]


def simhash64(text: str, k: int = 3) -> int:
    """Charikar SimHash. Returns an unsigned 64-bit int."""
    v = [0] * 64
    for sh in _shingles(text, k):
        h = int.from_bytes(hashlib.blake2b(sh.encode("utf-8"), digest_size=8).digest(), "big")
        for b in range(64):
            v[b] += 1 if (h >> b) & 1 else -1
    out = 0
    for b in range(64):
        if v[b] > 0:
            out |= 1 << b
    return out


def hamming(a: int, b: int) -> int:
    return ((a ^ b) & _MASK).bit_count()


def to_signed(u: int) -> int:
    """SQLite INTEGER is signed 64-bit; store the bit pattern, not the value."""
    return u - (1 << 64) if u >= (1 << 63) else u


def to_unsigned(s: int) -> int:
    return s + (1 << 64) if s < 0 else s


def group_variants(
    items: list[tuple[int, str, int]], max_distance: int = 8
) -> dict[str, list[int]]:
    """Cluster cross-version duplicates.

    `items` is (chunk_id, group_key, simhash_unsigned). The key is an EXACT
    identity for "the same section of the same topic" — in this corpus that is
    `family|slug|heading_path`, which is ground truth and needs no fuzzy match.

    Measured on all 7,586 true cross-version pairs in the full index
    (2026-08-26 build, `regroup --report`):

        distance 0 ....... 18.3% (byte-identical)
        distance <= 3 .... 21.7%
        distance <= 8 .... 30.5%
        distance <= 16 ... 38.8%
        distance <= 24 ... 49.1%
        distance <= 32 ... 84.3%
        median ........... 25

    The shape matters more than any single number. It is bimodal: a mass of
    identical-to-near-identical pairs below ~8, a long flat valley from 8 to
    24, then a spike approaching 32 — which on 64 bits is what two unrelated
    documents score. So the corpus contains both "reprinted verbatim across
    releases" and "rewritten between releases", with relatively little in
    between, and the valley is where a threshold belongs.

    Two consequences. First, "same topic across versions" does NOT imply "same
    content" — most of these pages were genuinely rewritten. Second, using
    SimHash to FIND the pairs was the wrong job for it: it discards an exact
    key that is already ground truth and recovers barely a fifth of them.

    The right division of labour, and what this function now does:
      * the exact key decides WHICH chunks are candidates to collapse
      * SimHash decides WHETHER they may be collapsed

    That guard is what protects version correctness. If Studio 8 and Studio 9
    say the same thing, collapsing to one hit plus `also_in_versions` is a win.
    If they diverged, collapsing would hide the version-specific answer — so
    they stay separate and both remain retrievable.

    The threshold is set at 8, the low edge of the valley, because the two
    error directions are not symmetric. Failing to collapse a duplicate costs
    context budget and the user still sees the answer; collapsing a diverged
    pair hides a version-specific answer, which is the R1 failure this whole
    subsystem exists to prevent. Raising it to 16 collapses only 4.3pp more
    chunks (21.3% -> 25.6%) and buys that entirely out of the ambiguous middle.

    Returns {group_key#n: [chunk_id, ...]} for clusters of size >= 2.
    """
    by_key: dict[str, list[tuple[int, int]]] = defaultdict(list)
    for cid, key, h in items:
        by_key[key].append((cid, h))

    out: dict[str, list[int]] = {}
    for key, members in by_key.items():
        if len(members) < 2:
            continue
        parent = {cid: cid for cid, _ in members}

        def find(x: int) -> int:
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        for i in range(len(members)):
            for j in range(i + 1, len(members)):
                (a, ha), (b, hb) = members[i], members[j]
                if find(a) != find(b) and hamming(ha, hb) <= max_distance:
                    parent[find(b)] = find(a)

        clusters: dict[int, list[int]] = defaultdict(list)
        for cid, _ in members:
            clusters[find(cid)].append(cid)
        for n, (_root, group) in enumerate(sorted(clusters.items())):
            if len(group) >= 2:
                out[f"{key}#{n}"] = sorted(group)
    return out
