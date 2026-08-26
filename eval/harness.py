"""Run the golden set through the real query path (plan §10.1).

The harness calls `KnowledgeBase.search` — the same entry point `server.py`
uses — rather than reaching into `Pipeline`. If the harness had its own wiring,
it would measure a stack that no user ever runs.

    python -m eval.harness                          # full stack
    python -m eval.harness --rung 0                 # BM25 only
    python -m eval.harness --tag before --out-dir eval/runs
"""

from __future__ import annotations

import argparse
import json
import platform
import statistics
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from neutrinos_mcp.config import ROOT  # noqa: E402
from neutrinos_mcp.kb import KnowledgeBase  # noqa: E402
from neutrinos_mcp.retrieval.pipeline import Stages  # noqa: E402

from . import metrics as M  # noqa: E402


def load_golden(path: Path, reviewed_only: bool = False) -> list[dict]:
    if not path.exists():
        raise SystemExit(
            f"No golden set at {path}. Generate a seed with "
            f"`python -m eval.generate --n 200` and review it (plan §10.2).")
    items = []
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        it = json.loads(line)
        if reviewed_only and not it.get("reviewed"):
            continue
        items.append(it)
    if not items:
        raise SystemExit("Golden set is empty (did --reviewed-only filter everything?).")
    return items


def score_one(kb: KnowledgeBase, item: dict, top_k: int, stages: Stages) -> dict:
    t0 = time.perf_counter()
    err = None
    try:
        res = kb.search(item["question"], top_k=top_k, stages=stages)
        hits = res.hits
    except Exception as exc:                      # a raised error is a score of 0
        hits, res, err = [], None, f"{type(exc).__name__}: {exc}"
    latency_ms = (time.perf_counter() - t0) * 1000

    refs = [h["ref"] for h in hits]
    rel = item.get("relevant_refs") or []
    row = {
        "id": item["id"],
        "kind": item.get("kind"),
        "family": item.get("family"),
        "recall@5": M.recall_at_k(refs, rel, 5),
        "recall@10": M.recall_at_k(refs, rel, 10),
        "mrr@10": M.mrr_at_k(refs, rel, 10),
        "ndcg@10": M.ndcg_at_k(refs, rel, 10),
        "precision@5": M.precision_at_k(refs, rel, 5),
        "duplicate_rate@5": M.duplicate_rate_at_k(hits, 5),
        "cross_version_dupe@5": M.cross_version_dupe_rate_at_k(hits, 5),
        "latency_ms": round(latency_ms, 1),
        "n_hits": len(hits),
    }
    vc = M.version_correct_at_1(hits, item.get("expected_version"),
                               item.get("expected_product"))
    if vc is not None:
        row["version_correct@1"] = vc
    if res is not None:
        row["confidence"] = res.confidence
        row["sufficient_evidence"] = 1.0 if res.sufficient_evidence else 0.0
        row["abstained"] = 0.0 if res.sufficient_evidence else 1.0
    if err:
        row["error"] = err
    return row


def run(kb: KnowledgeBase, items: list[dict], top_k: int, stages: Stages,
        verbose: bool = False) -> dict:
    rows = []
    for i, item in enumerate(items, 1):
        rows.append(score_one(kb, item, top_k, stages))
        if verbose and i % 25 == 0:
            print(f"  {i}/{len(items)}", file=sys.stderr, flush=True)

    agg = M.aggregate(rows)
    lat = sorted(r["latency_ms"] for r in rows)
    agg["latency_p50_ms"] = round(statistics.median(lat), 1)
    agg["latency_p95_ms"] = round(lat[min(int(0.95 * len(lat)), len(lat) - 1)], 1)
    agg.pop("latency_ms", None)
    agg["errors"] = sum(1 for r in rows if "error" in r)

    # Wilson bounds on the headline rate: with n=200 the half-width is ~7pp, so
    # a 3pp "improvement" between two runs is noise. Reporting the interval
    # alongside the point estimate is what stops that being read as a win.
    lo, hi = M.wilson_interval(agg.get("recall@5", 0.0), len(rows))
    agg["recall@5_ci95"] = [round(lo, 4), round(hi, 4)]

    return {"summary": agg, "rows": rows}


def by_slice(rows: list[dict], key: str) -> dict:
    out: dict[str, dict] = {}
    groups: dict[str, list[dict]] = {}
    for r in rows:
        groups.setdefault(str(r.get(key)), []).append(r)
    for k, g in sorted(groups.items()):
        a = M.aggregate(g)
        out[k] = {m: a[m] for m in ("n", "recall@5", "mrr@10", "duplicate_rate@5")
                  if m in a}
    return out


def main() -> None:
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--golden", default=str(ROOT / "eval" / "golden" / "seed.jsonl"))
    ap.add_argument("--db", default=None)
    ap.add_argument("--top-k", type=int, default=10)
    ap.add_argument("--rung", type=int, default=None,
                    help="ablation rung 0-7 (§10.4); default = full stack")
    ap.add_argument("--reviewed-only", action="store_true")
    ap.add_argument("--tag", default="run")
    ap.add_argument("--out-dir", default=str(ROOT / "eval" / "runs"))
    ap.add_argument("--limit", type=int, default=0)
    args = ap.parse_args()

    items = load_golden(Path(args.golden), args.reviewed_only)
    if args.limit:
        items = items[: args.limit]
    stages = Stages.rung(args.rung) if args.rung is not None else Stages()

    kb = KnowledgeBase(args.db)
    t0 = time.perf_counter()
    result = run(kb, items, args.top_k, stages, verbose=True)
    wall = time.perf_counter() - t0

    result["meta"] = {
        "tag": args.tag,
        "rung": args.rung,
        "stages": vars(stages),
        "golden": args.golden,
        "n_items": len(items),
        "reviewed_only": args.reviewed_only,
        "top_k": args.top_k,
        "db": str(kb.db_path),
        "manifest": kb.stats().get("build", {}),
        "wall_seconds": round(wall, 1),
        "python": platform.python_version(),
        "machine": platform.machine(),
    }
    result["by_kind"] = by_slice(result["rows"], "kind")
    result["by_family"] = by_slice(result["rows"], "family")
    kb.close()

    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    name = f"{args.tag}" + (f"-rung{args.rung}" if args.rung is not None else "") + ".json"
    (out_dir / name).write_text(json.dumps(result, indent=2), encoding="utf-8")

    print(json.dumps(result["summary"], indent=2))
    print(f"\nwrote {out_dir / name}")


if __name__ == "__main__":
    main()
