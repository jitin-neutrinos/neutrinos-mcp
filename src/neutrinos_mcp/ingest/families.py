"""Seed config/publications.yaml from the measured census (plan §6.5).

Naming gets you part of the way and provably no further: `app-builder-s-user-guide`
and `studio-guide-7` share 0.991 of their slugs while sharing no name. So family
membership is derived by union-find over the census Jaccard matrix, then the
name parser supplies product labels and version numbers on top.

The output is a REVIEW ARTIFACT. Every entry the clustering inferred rather than
read off a name is flagged `review: true` with the evidence attached, so the
human reviewing it knows exactly which claims need product-history sign-off.

    python -m neutrinos_mcp.ingest.families --seed
"""

from __future__ import annotations

import argparse
import json
import re
from collections import defaultdict
from pathlib import Path

from ..config import ROOT, settings

# Publications whose slug-overlap is high because they are *siblings* (a tutorial
# and the guide it accompanies), not versions of one another. Union-find would
# otherwise fuse them. Keeping this list short and explicit is the point.
NEVER_MERGE: set[frozenset[str]] = set()

# Trailing version markers seen in the 53 real publication ids.
_VERSION_PATTERNS = [
    (re.compile(r"^(?P<stem>.+?)-for-release-(?P<v>\d+)$"), "release"),
    (re.compile(r"^(?P<stem>.+?)-(?P<v>\d+)$"), "suffix"),
]

_STRIP_SUFFIXES = ("-publication", "-guide", "-s-user-guide", "-user-s-guide")

# Trailing words that are documentation-furniture, not part of the product name.
# Without this, `app-builder-s-user-guide` labels as "App Builder User", and a
# community member typing "App Builder" fails to resolve.
_TRAILING_NOISE = {"user", "guide", "s", "reference", "docs", "doc"}

# Products whose names are acronyms; title-casing mangles them.
_ACRONYMS = {
    "ai": "AI", "sdk": "SDK", "api": "API", "srm": "SRM",
    "psd": "PSD", "pwa": "PWA", "art": "ART", "faqs": "FAQs",
}


def parse_name(pub_id: str) -> tuple[str, str | None]:
    """(stem, version) from a publication id. Version is None when unversioned."""
    for pat, _kind in _VERSION_PATTERNS:
        m = pat.match(pub_id)
        if m:
            return m.group("stem"), m.group("v")
    return pub_id, None


def titleise(stem: str) -> str:
    s = stem
    for suf in _STRIP_SUFFIXES:
        if s.endswith(suf):
            s = s[: -len(suf)]
            break
    s = s.replace("neutrinos-", "").replace("project-", "").replace("-", " ").strip()
    words = s.split()
    # Strip documentation-furniture words from the tail only; "User Guide" is
    # furniture, but a leading word never is.
    while len(words) > 1 and words[-1].lower() in _TRAILING_NOISE:
        words.pop()
    out = [_ACRONYMS.get(w.lower(), w.capitalize()) for w in words]
    return " ".join(out) or stem


class UnionFind:
    def __init__(self, items):
        self.parent = {i: i for i in items}

    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra != rb:
            self.parent[rb] = ra


def seed(threshold: float = 0.70) -> dict:
    census = json.loads((ROOT / "data" / "census.json").read_text(encoding="utf-8"))
    pub_ids = [p["publication"] for p in census["publications"]]
    counts = {p["publication"]: p["topics"] for p in census["publications"]}
    newest = {p["publication"]: p["lastmod_max"] for p in census["publications"]}
    pairs = census["near_duplicate_pairs_jaccard_ge_0_5"]

    uf = UnionFind(pub_ids)

    # 1. Merge on name stem — the easy, unambiguous half.
    by_stem: dict[str, list[str]] = defaultdict(list)
    for pid in pub_ids:
        stem, _ = parse_name(pid)
        by_stem[stem].append(pid)
    name_merges = set()
    for stem, group in by_stem.items():
        for other in group[1:]:
            uf.union(group[0], other)
            name_merges.add(frozenset((group[0], other)))

    # 2. Merge on measured slug overlap — this is what catches the renames.
    evidence: dict[frozenset[str], float] = {}
    for pr in pairs:
        a, b, j = pr["a"], pr["b"], pr["jaccard"]
        if j < threshold or frozenset((a, b)) in NEVER_MERGE:
            continue
        uf.union(a, b)
        evidence[frozenset((a, b))] = j

    # 3. Build families.
    clusters: dict[str, list[str]] = defaultdict(list)
    for pid in pub_ids:
        clusters[uf.find(pid)].append(pid)

    # 3b. Two distinct clusters can derive the SAME family id — `change-log` and
    # `change-log-publication` both titleise to "Change Log", and their slug
    # overlap is below threshold so neither merge rule joined them. Left alone
    # that yields two "current" versions in one family, which breaks scoping.
    # Same name => same product => merge.
    def family_id_of(members: list[str]) -> str:
        anchor = max(members, key=lambda p: (counts[p], parse_name(p)[1] is not None))
        product = titleise(parse_name(anchor)[0])
        return re.sub(r"[^a-z0-9]+", "-", product.lower()).strip("-")

    by_family: dict[str, list[str]] = defaultdict(list)
    for members in clusters.values():
        by_family[family_id_of(members)] += members
    clusters = {k: v for k, v in by_family.items()}

    out_pubs, aliases = {}, {}
    for members in clusters.values():
        # Family id + product label come from the member with the most topics,
        # preferring one that carries an explicit version.
        members.sort(key=lambda p: (-counts[p], p))
        stems = {parse_name(p)[0] for p in members}
        anchor = max(members, key=lambda p: (counts[p], parse_name(p)[1] is not None))
        product = titleise(parse_name(anchor)[0])
        family = re.sub(r"[^a-z0-9]+", "-", product.lower()).strip("-")

        versioned = [(p, parse_name(p)[1]) for p in members]
        # rank: explicit numeric version ascending; unversioned members sort oldest
        def rank_key(item):
            _p, v = item
            return (1, int(v)) if v is not None else (0, 0)

        ordered = sorted(versioned, key=rank_key)
        newest_lastmod = max((newest[p] or "") for p in members)

        for rank, (pid, ver) in enumerate(ordered, start=1):
            is_current = rank == len(ordered)
            inferred = len(stems) > 1  # family spans >1 name stem => a rename
            ev = [
                f"{'/'.join(sorted(k))} J={v}"
                for k, v in evidence.items()
                if pid in k
            ]
            out_pubs[pid] = {
                "title": titleise(parse_name(pid)[0]) + (f" {ver}" if ver else ""),
                "product": product,
                "version": ver,
                "version_rank": rank,
                "family": family,
                "is_current": is_current,
                "lifecycle": "current" if is_current else "superseded",
                "topic_count": counts[pid],
                "newest_lastmod": newest[pid],
                **({"review": True, "evidence": ev} if inferred and ev else {}),
            }
            other = titleise(parse_name(pid)[0])
            if other.lower() != product.lower():
                aliases[other] = family

    return {
        "_generated_by": "neutrinos_mcp.ingest.families --seed",
        "_source": "data/census.json (measured 2026-08-26)",
        "_review_note": (
            "Entries marked `review: true` were grouped by measured slug overlap, "
            "not by name — they imply a product rename. Confirm each against "
            "product history before this file is frozen (plan §14 Q2b). A wrong "
            "family assignment produces confidently version-wrong answers (R1)."
        ),
        "aliases": aliases,
        "publications": out_pubs,
    }


def _dump(doc: dict) -> str:
    """Hand-rolled YAML so ordering and comments stay reviewer-friendly."""
    L: list[str] = [
        "# config/publications.yaml — the reviewed product/version map (plan §6.5)",
        f"# generated: {doc['_generated_by']}",
        f"# source:    {doc['_source']}",
        "#",
    ]
    for line in doc["_review_note"].split(". "):
        if line.strip():
            L.append(f"# {line.strip().rstrip('.')}.")
    L += ["", "aliases:"]
    for k, v in sorted(doc["aliases"].items()):
        L.append(f'  "{k}": {v}')
    L += ["", "publications:"]
    for pid, e in sorted(
        doc["publications"].items(), key=lambda kv: (kv[1]["family"], kv[1]["version_rank"])
    ):
        L.append(f"  {pid}:")
        if e.get("review"):
            L.append("    # REVIEW: grouped by measured overlap, not by name — confirm the rename.")
            for ev in e["evidence"]:
                L.append(f"    #   evidence: {ev}")
        L.append(f'    title: "{e["title"]}"')
        L.append(f'    product: "{e["product"]}"')
        L.append(f'    version: {e["version"] if e["version"] is not None else "null"}')
        L.append(f"    version_rank: {e['version_rank']}")
        L.append(f"    family: {e['family']}")
        L.append(f"    is_current: {str(e['is_current']).lower()}")
        L.append(f"    lifecycle: {e['lifecycle']}")
        L.append(f"    topic_count: {e['topic_count']}")
        L.append(f"    newest_lastmod: \"{e['newest_lastmod']}\"")
        if e.get("review"):
            L.append("    review: true")
    return "\n".join(L) + "\n"


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--seed", action="store_true", help="write config/publications.yaml")
    ap.add_argument("--threshold", type=float, default=0.70)
    ap.add_argument("--force", action="store_true", help="overwrite an existing file")
    args = ap.parse_args()

    doc = seed(args.threshold)
    fams = {e["family"] for e in doc["publications"].values()}
    needs_review = [p for p, e in doc["publications"].items() if e.get("review")]

    print(f"publications classified : {len(doc['publications'])}")
    print(f"families derived        : {len(fams)}")
    print(f"aliases (renames)       : {len(doc['aliases'])}")
    print(f"entries needing review  : {len(needs_review)}")
    for p in needs_review:
        print(f"    - {p}")

    if args.seed:
        out: Path = settings().path("publications")
        if out.exists() and not args.force:
            print(f"\n{out} exists; pass --force to overwrite.")
            return
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(_dump(doc), encoding="utf-8")
        print(f"\nwrote {out}")


if __name__ == "__main__":
    main()
