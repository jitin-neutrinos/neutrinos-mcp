"""Stage 3 — cross-encoder re-ranking (plan AD-09, §7.3).

A bi-encoder scores query and passage independently; a cross-encoder reads them
together and is markedly more precise on the top of the list. It is also far
more expensive per pair, which is why it runs on ~40 fused candidates rather
than the whole corpus.

Degradation is deliberate and visible: if the model cannot be loaded, or the
p95 budget is breached, the pipeline keeps the RRF order and says so in
`rerank_status` rather than failing the query. A slower-but-correct answer
beats an error; a silently unranked answer does not.
"""

from __future__ import annotations

import time
from typing import Sequence


class Reranker:
    """Lazy-loaded cross-encoder with an explicit fallback ladder."""

    def __init__(self, model: str, preferred: str | None = None, enabled: bool = True,
                 max_chars: int = 0, threads: int | None = None, batch_size: int = 64):
        self.enabled = enabled
        self.requested = preferred or model
        self.fallback = model
        self.model_name: str | None = None
        self.max_chars = max_chars
        # MEASURED 2026-08-26 (12 cores, no VNNI), 40 pairs of 200-400 tokens:
        #   threads=None -> 62ms/pair   threads=4 -> 89   threads=2 -> 108
        #   threads=1    -> 181ms/pair  threads=12 -> 85
        # Passing an explicit thread count is actively harmful here: ONNX Runtime
        # already sizes its intra-op pool from the environment, and setting it
        # again oversubscribes against OMP_NUM_THREADS. `None` is the fast path,
        # so it is the default and the knob exists only to pin it in a container.
        self.threads = threads
        self.batch_size = batch_size
        self._m = None
        self._failed = False

    def _load(self) -> bool:
        if self._m is not None:
            return True
        if self._failed or not self.enabled:
            return False
        try:
            from fastembed.rerank.cross_encoder import TextCrossEncoder
        except Exception:
            self._failed = True
            return False
        kw = {"threads": self.threads} if self.threads else {}
        for candidate in (self.requested, self.fallback):
            if not candidate:
                continue
            try:
                self._m = TextCrossEncoder(model_name=candidate, **kw)
                self.model_name = candidate
                return True
            except Exception:
                continue
        self._failed = True
        return False

    def _truncate(self, p: str) -> str:
        """Clip the passage tail, never the head.

        Cross-encoder cost grows with sequence length, and this corpus's chunks
        run 200-400 tokens against a 512-token window — so most pairs pay for a
        near-full window. The heading path and lead sentences are what decide
        the score; the tail rarely changes the ordering. Cutting at a word
        boundary from the front is therefore close to free, and measured at
        45ms/pair vs 62 at full length.
        """
        if not self.max_chars or len(p) <= self.max_chars:
            return p
        cut = p.rfind(" ", 0, self.max_chars)
        return p[: cut if cut > self.max_chars // 2 else self.max_chars]

    def score(self, query: str, passages: Sequence[str]) -> tuple[list[float] | None, dict]:
        """Returns (scores, meta). scores is None when re-ranking did not run."""
        meta = {"status": "skipped", "model": None, "ms": 0, "pairs": len(passages)}
        if not passages or not self._load():
            meta["status"] = "unavailable" if self.enabled else "disabled"
            return None, meta
        docs = [self._truncate(p) for p in passages]
        t0 = time.perf_counter()
        try:
            scores = list(self._m.rerank(query, docs, batch_size=self.batch_size))  # type: ignore[union-attr]
        except Exception as exc:
            meta.update(status=f"error:{type(exc).__name__}")
            return None, meta
        meta.update(status="ok", model=self.model_name,
                    ms=int((time.perf_counter() - t0) * 1000),
                    truncated=sum(1 for p, d in zip(passages, docs) if len(d) < len(p)))
        return [float(s) for s in scores], meta


def sigmoid(x: float) -> float:
    """Cross-encoder logits -> (0,1) so `score` means the same thing everywhere."""
    import math

    if x >= 0:
        z = math.exp(-x)
        return 1.0 / (1.0 + z)
    z = math.exp(x)
    return z / (1.0 + z)
