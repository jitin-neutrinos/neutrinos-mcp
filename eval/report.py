"""Compare two harness runs and gate a release (plan §10.6, §11.4).

Used two ways:

  * by hand, to see what a change did
  * in CI as a regression gate — `--gate` exits non-zero when a headline metric
    falls outside its confidence interval, which is the only defensible way to
    distinguish a real regression from a 200-item sampling wobble

    python -m eval.report eval/runs/before.json eval/runs/after.json
    python -m eval.report before.json after.json --gate
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from . import metrics as M  # noqa: E402

# Direction each metric should move. Duplicates and latency are the two where
# "up" is bad, and getting that backwards would silently invert the gate.
HIGHER_IS_BETTER = {
    "recall@5": True, "recall@10": True, "mrr@10": True, "ndcg@10": True,
    "precision@5": True, "version_correct@1": True, "sufficient_evidence": True,
    "duplicate_rate@5": False, "cross_version_dupe@5": False,
    "latency_p50_ms": False, "latency_p95_ms": False, "errors": False,
}

# Gate thresholds. Latency is absolute (ms); the rest are proportions.
GATE = {
    "recall@5": 0.03,
    "mrr@10": 0.03,
    "version_correct@1": 0.05,
    "duplicate_rate@5": 0.05,
    "latency_p95_ms": 400.0,
}


def load(p: str) -> dict:
    return json.loads(Path(p).read_text(encoding="utf-8"))


def main() -> None:
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("before")
    ap.add_argument("after")
    ap.add_argument("--gate", action="store_true",
                    help="exit 1 if any gated metric regressed beyond tolerance")
    args = ap.parse_args()

    a, b = load(args.before), load(args.after)
    sa, sb = a["summary"], b["summary"]
    n = min(sa.get("n", 0), sb.get("n", 0))

    keys = [k for k in HIGHER_IS_BETTER if k in sa or k in sb]
    w = max(len(k) for k in keys) + 2
    print(f"{'metric':<{w}}{'before':>12}{'after':>12}{'delta':>12}   verdict")
    print("-" * (w + 48))

    failures = []
    for k in keys:
        va, vb = sa.get(k), sb.get(k)
        if va is None or vb is None:
            continue
        d = vb - va
        better = (d > 0) == HIGHER_IS_BETTER[k]
        tol = GATE.get(k)

        if k.endswith("_ms"):
            verdict = "ok" if (d <= 0 or (tol and d <= tol)) else "SLOWER"
        elif abs(d) < 1e-9:
            verdict = "flat"
        elif better:
            verdict = "better"
        elif tol is not None and abs(d) > tol:
            verdict = "REGRESSION"
        else:
            verdict = "worse (within tolerance)"

        # A proportion whose CIs overlap has not moved in any measurable sense,
        # regardless of how the point estimates compare.
        if not k.endswith("_ms") and k != "errors" and n:
            la, ha = M.wilson_interval(va, n)
            lb, hb = M.wilson_interval(vb, n)
            if not (hb < la or lb > ha) and verdict in ("better", "REGRESSION"):
                verdict += " [CIs overlap: not significant]"

        if verdict.startswith("REGRESSION") or verdict == "SLOWER":
            failures.append((k, va, vb, d))

        fmt = "{:.0f}" if k.endswith("_ms") or k == "errors" else "{:.4f}"
        print(f"{k:<{w}}{fmt.format(va):>12}{fmt.format(vb):>12}"
              f"{('+' if d >= 0 else '') + fmt.format(d):>12}   {verdict}")

    for label, key in (("kind", "by_kind"), ("family", "by_family")):
        if key not in a or key not in b:
            continue
        rows = []
        for name in sorted(set(a[key]) | set(b[key])):
            ra, rb = a[key].get(name, {}), b[key].get(name, {})
            if "recall@5" in ra and "recall@5" in rb:
                d = rb["recall@5"] - ra["recall@5"]
                if abs(d) >= 0.05:
                    rows.append((name, ra["recall@5"], rb["recall@5"], d))
        if rows:
            print(f"\nlargest recall@5 moves by {label} (>= 5pp):")
            for name, x, y, d in sorted(rows, key=lambda r: r[3]):
                print(f"  {name:<32}{x:.3f} -> {y:.3f}  ({'+' if d >= 0 else ''}{d:.3f})")

    if args.gate:
        if failures:
            print(f"\nGATE FAILED: {len(failures)} metric(s) regressed beyond tolerance")
            for k, va, vb, d in failures:
                print(f"  {k}: {va} -> {vb} ({d:+.4f}, tolerance {GATE[k]})")
            raise SystemExit(1)
        print("\nGATE PASSED")


if __name__ == "__main__":
    main()
