# neutrinos-mcp

A retrieval MCP server over the Neutrinos documentation corpus (53 publications, 3,117 topics,
7,810 indexed chunks). Hybrid BM25 + dense retrieval, RRF fusion, cross-encoder reranking,
cross-version near-duplicate collapse, and conditional link-graph expansion — built to answer
"is this true for the version the user is actually on", which a naive semantic-search-over-docs
setup gets wrong on this corpus more than half the time. See `implementation_plan.md` for the
full design rationale (architecture decisions, data model, evaluation methodology).

## Quick start

```bash
pip install -e ".[dev]"

# Build the index (crawls documentation.neutrinos.com, ~25 min)
python -m neutrinos_mcp.ingest.index

# Query it
neutrinos-cli search "how do I bind a widget to a data model"
neutrinos-cli search "accessing data models" --product Studio --version 9
neutrinos-cli fetch studio-guide-9/data-binding --json
neutrinos-cli products

# Run the MCP server
neutrinos-mcp
```

## Layout

```
config/          settings.toml (runtime config), publications.yaml (product/version registry)
src/neutrinos_mcp/
  ingest/        crawl -> extract -> chunk -> embed -> build (data/neutrinos.db)
  retrieval/     the ranking pipeline: scope -> BM25/dense -> RRF -> rerank -> collapse -> MMR -> expand
  tools/         MCP tool JSON schemas + handlers (the contract; see plan §8.5)
  kb.py          the query API — server.py and cli.py both call this and nothing else touches SQL
  server.py      FastMCP entry point
  cli.py         terminal adapter over the same contract
eval/            golden-set generation, harness, ablation ladder, two-run regression report
tests/           schema contract tests, corpus-integrity tests (skip without a built index), unit tests
data/            neutrinos.db (built artifact), chroma_db (optional mirror), census.json
```

## Testing

```bash
pytest                                    # unit + schema tests; integrity tests skip without an index
python -m eval.harness --tag baseline     # full-stack retrieval quality on the golden set
python -m eval.ablate                     # §10.4 rung-by-rung ablation
python -m eval.report before.json after.json --gate   # regression gate, exits 1 on a real regression
```

## Configuration

Everything tunable lives in `config/settings.toml`, not in code — retrieval candidate counts,
the RRF constant, MMR lambda, reranker truncation/threading, staleness windows, token budgets.
Model weights are pinned by name and verified against the build manifest at server startup
(AD-12): serving an index built with a different embedding model fails loudly rather than
returning silently-degraded results.

## What this is not

Not a general web-search or code-execution surface, not an LLM-extracted entity graph, not a
writer — the server returns evidence with stable citations (`ref` tokens); composing the reply
is the calling agent's job. See plan §1.4.
