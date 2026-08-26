"""The ablation ladder (plan §10.4).

Runs rungs 0..7 over one golden set and prints the marginal delta each stage
buys. The point is falsifiability: a component that does not move a metric here
is complexity the server is carrying for free, and should be cut. RRF, the
reranker, variant collapse and MMR all have a cost in latency or code, and this
is the only artefact that says whether they earn it.

    python -m eval.ablate
    python -m eval.ablate --rungs 0,2,4,5,7
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from neutrinos_mcp.config import ROOT  # noqa: E402
from neutrinos_mcp.kb import KnowledgeBase  # noqa: E402
from neutrinos_mcp.retrieval.pipeline import Stages  # noqa: E402

from .harness import load_golden, run  # noqa: E402

RUNGS = {
    0: "BM25 only",
    1: "dense only",
    2: "+ RRF fusion",
    3: "+ contextual prefix (index-side)",
    4: "+ cross-encoder rerank",
    5: "+ variant collapse",
    6: "+ MMR diversity",
    7: "+ graph expansion (full stack)",
}

HEADLINE = ["recall@5", "mrr@10", "ndcg@10", "duplicate_rate@5",
            "cross_version_dupe@5", "version_correct@1", "latency_p95_ms"]


def main() -> None:
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--golden", default=str(ROOT / "eval" / "golden" / "seed.jsonl"))
    ap.add_argument("--db", default=None)
    ap.add_argument("--top-k", type=int, default=10)
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--rungs", default="0,1,2,4,5,6,7")
    ap.add_argument("--out", default=str(ROOT / "eval" / "runs" / "ablation.json"))
    args = ap.parse_args()

    items = load_golden(Path(args.golden))
    if args.limit:
        items = items[: args.limit]
    rungs = [int(r) for r in args.rungs.split(",") if r.strip() != ""]

    kb = KnowledgeBase(args.db)
    results = {}
    for r in rungs:
        print(f"rung {r}: {RUNGS[r]}", file=sys.stderr, flush=True)
        results[r] = run(kb, items, args.top_k, Stages.rung(r))["summary"]
    kb.close()

    # ---- table -------------------------------------------------------------
    cols = [m for m in HEADLINE if any(m in s for s in results.values())]
    w = max(len(RUNGS[r]) for r in rungs) + 4
    print(f"\n{'rung':<{w}}" + "".join(f"{c:>22}" for c in cols))
    prev = None
    for r in rungs:
        s = results[r]
        line = f"{r} {RUNGS[r]:<{w - 2}}"
        for c in cols:
            v = s.get(c)
            if v is None:
                line += f"{'-':>22}"
                continue
            cell = f"{v:.3f}" if c != "latency_p95_ms" else f"{v:.0f}ms"
            if prev is not None and prev.get(c) is not None:
                d = v - prev[c]
                sign = "+" if d >= 0 else ""
                cell += f" ({sign}{d:.3f})" if c != "latency_p95_ms" else f" ({sign}{d:.0f})"
            line += f"{cell:>22}"
        print(line)
        prev = s

    print("\nnote: deltas are vs the rung above, not vs rung 0. A stage whose "
          "delta sits inside the recall@5 CI has not been shown to help.")

    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(
        {"n_items": len(items), "rungs": {str(k): v for k, v in results.items()},
         "labels": {str(k): RUNGS[k] for k in rungs}}, indent=2), encoding="utf-8")
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
