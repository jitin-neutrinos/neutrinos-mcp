"""Seed the golden set from the corpus (plan §10.2).

The honest framing: this produces *silver* data, not gold. Each item is derived
from a real heading in a real topic, so the relevance label is grounded — the
question is machine-written, so the phrasing is not how a community member
would actually ask. Every item carries `reviewed: false` until a human edits it.

That distinction matters because a set generated from headings and scored by a
retriever that indexes those same headings measures self-consistency, not
usefulness. It is a regression harness first, a quality bar second.

Sampling is deliberately stratified rather than random (§10.2):

  * by product family, so a metric cannot be carried by Studio alone
  * over version-divergent topics, which is where R1 actually bites
  * over topics with code samples, which is where extraction is most fragile
  * over plain prose, so the ordinary case is represented

    python -m eval.generate --n 200 --out eval/golden/seed.jsonl
"""

from __future__ import annotations

import argparse
import json
import random
import re
import sqlite3
import sys
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from neutrinos_mcp.config import ROOT, publications, settings  # noqa: E402

# Headings that name no concept — a question built from them is unanswerable.
_JUNK = re.compile(
    r"^(overview|introduction|summary|notes?|see also|prerequisites?|"
    r"related (topics?|articles?)|conclusion|references?|index|contents?|"
    r"steps?|procedure|examples?|table of contents)$", re.I)

_HOWTO = ("how do I {h} in {p}?",
          "what are the steps to {h} in {p}?",
          "{h} in {p}")
_WHATIS = ("what is {h} in {p}?",
           "explain {h} in {p}",
           "{p} {h}")
_CODE = ("show me a code sample for {h} in {p}",
         "example of {h} in {p}")
_VERSION = ("how do I {h} in {p} {v}?",
            "did {h} change in {p} {v}?")


def _leaf(heading_path: str) -> str:
    return (heading_path or "").split(">")[-1].strip()


def _phrase(h: str) -> str:
    """Lower-case the leaf heading unless it is an identifier or acronym."""
    if h.isupper() or re.search(r"[A-Z]{2,}|[a-z][A-Z]|[_(){}]", h):
        return h
    return h[0].lower() + h[1:] if h else h


def _question(rng: random.Random, kind: str, h: str, product: str, version) -> str:
    tpl = {"howto": _HOWTO, "whatis": _WHATIS, "code": _CODE, "version": _VERSION}[kind]
    return rng.choice(tpl).format(h=_phrase(h), p=product, v=version or "")


def candidates(conn: sqlite3.Connection) -> list[dict]:
    reg = publications()
    rows = conn.execute(
        """SELECT c.id, c.pub, c.slug, c.anchor, c.heading_path, c.token_count,
                  c.variant_group_id, t.title,
                  p.product, p.version, p.is_current,
                  (SELECT COUNT(*) FROM code_sample s WHERE s.topic_id = c.topic_id)
           FROM chunk c
           JOIN topic t ON t.id = c.topic_id
           JOIN publication p ON p.id = c.pub
           WHERE p.is_current = 1 AND c.token_count >= 80""").fetchall()
    out = []
    for (cid, pub, slug, anchor, hp, tok, vg, title,
         product, version, _cur, ncode) in rows:
        leaf = _leaf(hp) or title
        if not leaf or _JUNK.match(leaf) or len(leaf) < 4:
            continue
        out.append({
            "chunk_id": cid, "pub": pub, "slug": slug, "anchor": anchor,
            "heading": leaf, "heading_path": hp, "title": title,
            "product": product, "version": version,
            "family": reg.get(pub).family, "tokens": tok,
            "has_code": ncode > 0, "variant_group_id": vg,
        })
    return out


def stratify(rng: random.Random, cands: list[dict], n: int) -> list[dict]:
    """Round-robin over families, then over strata within each family.

    Round-robin rather than proportional allocation on purpose: proportional
    sampling would give Studio (117 topics) many times the weight of a small
    publication, and the small publications are exactly where retrieval is
    weakest and least observed.
    """
    by_family: dict[str, list[dict]] = defaultdict(list)
    for c in cands:
        by_family[c["family"]].append(c)

    strata = {}
    for fam, items in by_family.items():
        buckets = {
            "version": [c for c in items if c["variant_group_id"]],
            "code": [c for c in items if c["has_code"]],
            "plain": [c for c in items if not c["has_code"] and not c["variant_group_id"]],
        }
        for b in buckets.values():
            rng.shuffle(b)
        strata[fam] = buckets

    picked: list[dict] = []
    seen: set[tuple] = set()
    families = sorted(strata)
    order = ["plain", "code", "version"]
    i = 0
    while len(picked) < n:
        progressed = False
        for fam in families:
            bucket = strata[fam][order[i % len(order)]]
            while bucket:
                c = bucket.pop()
                key = (c["family"], c["slug"], c["heading"])
                if key in seen:
                    continue
                seen.add(key)
                picked.append(c)
                progressed = True
                break
            if len(picked) >= n:
                break
        i += 1
        if not progressed:
            break   # every bucket in every family exhausted
    return picked[:n]


def to_item(rng: random.Random, c: dict, idx: int) -> dict:
    if c["variant_group_id"] and rng.random() < 0.5:
        kind = "version"
    elif c["has_code"] and rng.random() < 0.4:
        kind = "code"
    else:
        kind = rng.choice(["howto", "whatis"])
    ref = f"{c['pub']}/{c['slug']}"
    if c["anchor"]:
        ref = ref + "#" + c["anchor"]
    return {
        "id": f"g{idx:04d}",
        "question": _question(rng, kind, c["heading"], c["product"], c["version"]),
        "kind": kind,
        "relevant_refs": [ref],
        "expected_product": c["product"],
        "expected_version": c["version"] if kind == "version" else None,
        "family": c["family"],
        "source_chunk_id": c["chunk_id"],
        "reviewed": False,
        "notes": "",
    }


def main() -> None:
    cfg = settings()
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--db", default=str(ROOT / cfg["paths.db"]))
    ap.add_argument("--n", type=int, default=200)
    ap.add_argument("--seed", type=int, default=20260826)
    ap.add_argument("--out", default=str(ROOT / "eval" / "golden" / "seed.jsonl"))
    args = ap.parse_args()

    rng = random.Random(args.seed)
    conn = sqlite3.connect(f"file:{args.db}?mode=ro", uri=True)
    cands = candidates(conn)
    picked = stratify(rng, cands, args.n)
    items = [to_item(rng, c, i + 1) for i, c in enumerate(picked)]
    conn.close()

    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("w", encoding="utf-8") as fh:
        for it in items:
            fh.write(json.dumps(it, ensure_ascii=False) + "\n")

    fams: dict[str, int] = defaultdict(int)
    kinds: dict[str, int] = defaultdict(int)
    for it in items:
        fams[it["family"]] += 1
        kinds[it["kind"]] += 1
    print(json.dumps({
        "candidates": len(cands), "written": len(items), "out": str(out),
        "families_covered": len(fams), "by_kind": dict(kinds),
        "min_per_family": min(fams.values()) if fams else 0,
        "max_per_family": max(fams.values()) if fams else 0,
        "reviewed": 0,
        "WARNING": "machine-generated silver data; set reviewed=true after human edit",
    }, indent=2))


if __name__ == "__main__":
    main()
