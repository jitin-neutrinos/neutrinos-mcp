"""Recompute variant groups in place (plan AD-07).

Grouping is cheap — no embedding, seconds not minutes — but it is the single
highest-value knob in the retrieval stack for this corpus, and its threshold
wants tuning against the golden set. Coupling a seconds-long, frequently-tuned
step to a 26-minute embedding run would mean it never gets tuned.

    python -m neutrinos_mcp.ingest.regroup --report        # measure only
    python -m neutrinos_mcp.ingest.regroup --apply         # rewrite groups
    python -m neutrinos_mcp.ingest.regroup --apply -d 12   # try a threshold
"""

from __future__ import annotations

import argparse
import collections
import json
import sqlite3

from ..config import ROOT, publications, settings
from .simhash import group_variants, hamming, to_unsigned


def load(conn: sqlite3.Connection):
    reg = publications()
    rows = conn.execute(
        """SELECT c.id, c.pub, c.slug, c.heading_path, c.simhash
           FROM chunk c ORDER BY c.id""").fetchall()
    keyed, meta = [], {}
    for cid, pub, slug, heading, sh in rows:
        fam = reg.get(pub).family
        keyed.append((cid, f"{fam}|{slug}|{heading}", to_unsigned(sh)))
        meta[cid] = (pub, fam, reg.get(pub).version, reg.get(pub).version_rank)
    return keyed, meta


def distance_profile(keyed) -> dict:
    """Hamming distribution over true same-topic cross-version pairs."""
    by = collections.defaultdict(list)
    for cid, key, h in keyed:
        by[key].append((cid, h))
    dists = []
    for members in by.values():
        for i in range(len(members)):
            for j in range(i + 1, len(members)):
                dists.append(hamming(members[i][1], members[j][1]))
    if not dists:
        return {"pairs": 0}
    dists.sort()
    hist = collections.Counter(dists)
    cum, recall = 0, {}
    for d in range(0, 33):
        cum += hist.get(d, 0)
        if d in (0, 1, 2, 3, 4, 6, 8, 12, 16, 24, 32):
            recall[f"<= {d}"] = round(100 * cum / len(dists), 1)
    return {"pairs": len(dists), "median": dists[len(dists) // 2],
            "p90": dists[int(0.9 * len(dists))], "cumulative_recall_pct": recall}


def regroup(conn: sqlite3.Connection, max_distance: int, apply: bool) -> dict:
    keyed, meta = load(conn)
    groups = group_variants(keyed, max_distance)

    covered = sum(len(v) for v in groups.values())
    spans = collections.Counter()
    for members in groups.values():
        spans[len({meta[c][2] for c in members})] += 1

    stats = {
        "max_distance": max_distance,
        "chunks": len(keyed),
        "groups": len(groups),
        "chunks_in_groups": covered,
        "pct_chunks_collapsed": round(100 * (covered - len(groups)) / max(len(keyed), 1), 1),
        "groups_by_version_span": dict(sorted(spans.items())),
    }

    if apply:
        conn.execute("DELETE FROM variant_group")
        conn.execute("UPDATE chunk SET variant_group_id = NULL")
        vg, upd = [], []
        for gid, (_key, members) in enumerate(sorted(groups.items()), start=1):
            canonical = max(members, key=lambda c: meta[c][3])
            versions = sorted({meta[c][2] or "-" for c in members})
            vg.append((gid, meta[canonical][1], canonical, len(members), json.dumps(versions)))
            upd += [(gid, c) for c in members]
        conn.executemany(
            "INSERT INTO variant_group (id,family,canonical_chunk_id,member_count,versions_json)"
            " VALUES (?,?,?,?,?)", vg)
        conn.executemany("UPDATE chunk SET variant_group_id=? WHERE id=?", upd)
        conn.commit()
        stats["applied"] = True
    return stats


def main() -> None:
    cfg = settings()
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--db", default=str(ROOT / cfg["paths.db"]))
    ap.add_argument("-d", "--max-distance", type=int, default=cfg["retrieval.simhash_hamming"])
    ap.add_argument("--apply", action="store_true", help="rewrite groups in the DB")
    ap.add_argument("--report", action="store_true", help="distance profile + sweep")
    args = ap.parse_args()

    conn = sqlite3.connect(args.db)
    if args.report:
        keyed, _ = load(conn)
        print(json.dumps(distance_profile(keyed), indent=2))
        print("\nthreshold sweep (no changes written):")
        for d in (0, 2, 3, 4, 6, 8, 12, 16):
            s = regroup(conn, d, apply=False)
            print(f"  d<={d:<3} groups={s['groups']:>5}  chunks_in_groups={s['chunks_in_groups']:>5}"
                  f"  collapsed={s['pct_chunks_collapsed']:>5}%")
    else:
        print(json.dumps(regroup(conn, args.max_distance, args.apply), indent=2))
    conn.close()


if __name__ == "__main__":
    main()
