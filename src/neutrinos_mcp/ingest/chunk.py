"""Stage 3 — chunk (plan §6.3).

Splits on the heading tree the extractor recovered, not on character offsets.
The structure is already in the source; blind recursive splitting severs code
samples and tables, and produces chunks whose provenance cannot be cited.

The contextual prefix (AD-06) is the cheap, deterministic form of Anthropic's
contextual retrieval: product, version, lifecycle and heading path are placed
INSIDE the text that gets embedded and lexically indexed, so a query naming
"Studio 9" gets lift from both retrieval arms. No LLM, one string concat.
"""

from __future__ import annotations

import argparse
import json
import re
from dataclasses import asdict, dataclass
from pathlib import Path

from ..config import ROOT, publications, settings
from .simhash import simhash64, to_signed

_FENCE = re.compile(r"^```", re.M)


# ---------------------------------------------------------------- tokenising


class TokenCounter:
    """Real BGE tokenizer when available; calibrated heuristic otherwise.

    Chunk budgets drive both retrieval quality and the server's token caps, so
    a wrong count is not cosmetic. The heuristic is only a fallback for offline
    rebuilds.
    """

    def __init__(self, model: str):
        self._tok = None
        try:
            from tokenizers import Tokenizer

            self._tok = Tokenizer.from_pretrained(model)
        except Exception:
            self._tok = None

    @property
    def exact(self) -> bool:
        return self._tok is not None

    def count(self, text: str) -> int:
        if self._tok is not None:
            return len(self._tok.encode(text, add_special_tokens=False).ids)
        return max(1, int(len(text) / 3.6))  # calibrated on this corpus


# ---------------------------------------------------------------- data model


@dataclass
class Chunk:
    pub: str
    slug: str
    ordinal: int
    heading_path: str
    anchor: str | None
    level: int
    text: str
    context_prefix: str
    token_count: int
    has_code: bool
    simhash: int          # signed 64-bit bit pattern, ready for SQLite
    family: str

    @property
    def embed_text(self) -> str:
        """What actually gets embedded and FTS-indexed (AD-06)."""
        return f"{self.context_prefix}\n---\n{self.text}"


def build_prefix(pub_title: str, product: str, version: str | None,
                 lifecycle: str, heading_path: str) -> str:
    ver = f" · {product} v{version}" if version else f" · {product}"
    return f"[{pub_title}{ver} · {lifecycle}]\n{heading_path or pub_title}"


# ---------------------------------------------------------------- splitting


def _split_blocks(md: str) -> list[str]:
    """Paragraph-level blocks, with fenced code kept atomic."""
    out: list[str] = []
    buf: list[str] = []
    in_code = False
    for line in md.split("\n"):
        if line.startswith("```"):
            in_code = not in_code
            buf.append(line)
            if not in_code:
                out.append("\n".join(buf))
                buf = []
            continue
        if in_code:
            buf.append(line)
            continue
        if not line.strip():
            if buf:
                out.append("\n".join(buf))
                buf = []
        else:
            buf.append(line)
    if buf:
        out.append("\n".join(buf))
    return [b for b in out if b.strip()]


def _pack(blocks: list[str], tc: TokenCounter, target_max: int,
          hard_max: int, overlap_ratio: float) -> list[str]:
    """Greedily fill to target_max. A single oversized block is never split."""
    parts: list[str] = []
    cur: list[str] = []
    cur_tok = 0
    for b in blocks:
        bt = tc.count(b)
        if bt >= hard_max and not cur:
            parts.append(b)          # atomic: an over-budget code block or table
            continue
        if cur and cur_tok + bt > target_max:
            parts.append("\n\n".join(cur))
            keep: list[str] = []
            budget = int(target_max * overlap_ratio)
            for prev in reversed(cur):
                if _FENCE.search(prev):
                    break            # never carry code into the overlap
                pt = tc.count(prev)
                if pt > budget:
                    break
                keep.insert(0, prev)
                budget -= pt
            cur = keep + [b]
            cur_tok = sum(tc.count(x) for x in cur)
        else:
            cur.append(b)
            cur_tok += bt
    if cur:
        parts.append("\n\n".join(cur))
    return parts


def chunk_topic(topic: dict, tc: TokenCounter, cfg) -> list[Chunk]:
    reg = publications()
    pub = reg.get(topic["pub"])
    lifecycle = pub.lifecycle
    tmin = cfg["chunking.target_min"]
    tmax = cfg["chunking.target_max"]
    merge_below = cfg["chunking.merge_below"]
    hard_max = cfg["chunking.hard_max"]
    overlap = cfg["chunking.overlap_ratio"]

    # 1. sections -> units, merging undersized ones forward into the next sibling
    units: list[dict] = []
    for s in topic["sections"]:
        md = (s["md"] or "").strip()
        if not md:
            continue
        u = {"heading_path": s["heading_path"] or topic["title"],
             "anchor": s["anchor"], "level": s["level"], "md": md,
             "tok": tc.count(md), "has_code": bool(s.get("has_code"))}
        if units and units[-1]["tok"] < merge_below:
            prev = units[-1]
            prev["md"] = prev["md"] + "\n\n" + md
            prev["tok"] = tc.count(prev["md"])
            prev["has_code"] = prev["has_code"] or u["has_code"]
            # keep the EARLIER anchor: it is where the merged text begins
            continue
        units.append(u)

    # a topic whose whole body is one short blob still deserves one chunk
    if not units and (topic["body_md"] or "").strip():
        body = topic["body_md"].strip()
        units = [{"heading_path": topic["title"], "anchor": None, "level": 2,
                  "md": body, "tok": tc.count(body), "has_code": "```" in body}]

    out: list[Chunk] = []
    ordinal = 0
    for u in units:
        pieces = ([u["md"]] if u["tok"] <= tmax
                  else _pack(_split_blocks(u["md"]), tc, tmax, hard_max, overlap))
        for piece in pieces:
            if not piece.strip():
                continue
            prefix = build_prefix(pub.title, pub.product, pub.version,
                                  lifecycle, u["heading_path"])
            text = piece.strip()
            out.append(Chunk(
                pub=topic["pub"], slug=topic["slug"], ordinal=ordinal,
                heading_path=u["heading_path"], anchor=u["anchor"], level=u["level"],
                text=text, context_prefix=prefix, token_count=tc.count(text),
                has_code=("```" in text) or u["has_code"],
                # SimHash over the PROSE only: including the prefix would make
                # every cross-version pair differ by exactly the version token
                # and defeat the whole point of grouping them.
                simhash=to_signed(simhash64(text)),
                family=pub.family,
            ))
            ordinal += 1
    return out


# ---------------------------------------------------------------- driver


def run(limit: int | None = None) -> dict:
    cfg = settings()
    tc = TokenCounter(cfg["embedding.model"])
    src = ROOT / "data" / "topics.jsonl"
    dst = ROOT / "data" / "chunks.jsonl"

    stats = {"tokenizer": "exact" if tc.exact else "heuristic",
             "topics": 0, "chunks": 0, "with_code": 0, "tokens": 0,
             "undersized": 0, "oversized": 0, "no_anchor": 0}
    hist: dict[str, int] = {}

    with src.open(encoding="utf-8") as fin, dst.open("w", encoding="utf-8") as fout:
        for i, line in enumerate(fin, 1):
            if limit and i > limit:
                break
            topic = json.loads(line)
            stats["topics"] += 1
            for ch in chunk_topic(topic, tc, cfg):
                stats["chunks"] += 1
                stats["tokens"] += ch.token_count
                stats["with_code"] += int(ch.has_code)
                stats["no_anchor"] += int(ch.anchor is None)
                if ch.token_count < cfg["chunking.target_min"]:
                    stats["undersized"] += 1
                if ch.token_count > cfg["chunking.hard_max"]:
                    stats["oversized"] += 1
                b = min(ch.token_count // 100 * 100, 1000)
                hist[f"{b}-{b+99}"] = hist.get(f"{b}-{b+99}", 0) + 1
                fout.write(json.dumps(asdict(ch), ensure_ascii=False) + "\n")
            if i % 500 == 0:
                print(f"  chunked {i} topics -> {stats['chunks']} chunks")

    stats["mean_tokens"] = round(stats["tokens"] / max(stats["chunks"], 1), 1)
    stats["histogram"] = dict(sorted(hist.items(), key=lambda kv: int(kv[0].split("-")[0])))
    (ROOT / "data" / "chunk_report.json").write_text(json.dumps(stats, indent=2), encoding="utf-8")
    return stats


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--limit", type=int, default=None)
    args = ap.parse_args()
    print(json.dumps(run(args.limit), indent=2))


if __name__ == "__main__":
    main()
