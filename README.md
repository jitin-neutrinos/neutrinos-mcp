# neutrinos-mcp

A retrieval MCP server over the Neutrinos documentation corpus (53 publications, 3,117 topics,
7,810 indexed chunks). Hybrid BM25 + dense retrieval, RRF fusion, cross-encoder reranking,
cross-version near-duplicate collapse, and conditional link-graph expansion — built to answer
"is this true for the version the user is actually on", which a naive semantic-search-over-docs
setup gets wrong on this corpus more than half the time. See `implementation_plan.md` for the
full design rationale (architecture decisions, data model, evaluation methodology).

## Quick start

`neutrinos-mcp` is a **private** repo, so every option below needs a machine that's already
authenticated to it — `git` configured with a credential that can clone it (credential
manager / PAT / SSH key), or `gh auth login` already run. Without that, cloning just fails
with a 404, not a permissions error, which is easy to misread as "the repo doesn't exist."

**macOS/Linux — one line:**

```bash
git clone https://github.com/jitin-neutrinos/neutrinos-mcp.git ~/.neutrinos-mcp; bash ~/.neutrinos-mcp/install.sh
```

**Windows (PowerShell) — one line:**

```powershell
git clone https://github.com/jitin-neutrinos/neutrinos-mcp.git $HOME\.neutrinos-mcp; & "$HOME\.neutrinos-mcp\install.ps1"
```

Both are `git clone` followed by the platform installer, chained with `;` rather than `&&`/`&&`
equivalents so a rerun still proceeds even though the clone step then fails harmlessly ("already
exists") — `install.sh`/`install.ps1` each do their own `git pull` in that case, so reruns are
safe. Either script: creates a venv, installs the package (`python -m pip install -e .` — never
a bare `pip`/`pip.exe`, since that executable specifically gets blocked by execution policy on
some locked-down corporate machines while `python.exe` itself is still allowed), fetches the
latest pre-built `data/neutrinos.db` from the newest GitHub release via `gh release download` if
`gh` is installed (otherwise the running server fetches it on first use instead — see
Distribution below), and registers `neutrinos-docs` with Claude Code at **user scope** (every
project, not just this one). **Start a new Claude Code session afterward** — a server registered
mid-session isn't picked up until the client reconnects.

To build from source instead of using the pre-built release DB:

```bash
pip install -e ".[dev]"

# Build the index (four stages, run in order; full run crawls
# documentation.neutrinos.com and takes ~25 min)
python -m neutrinos_mcp.ingest.crawl      # stage 1 -> raw/*.html (delta by default; --full to re-fetch everything)
python -m neutrinos_mcp.ingest.extract    # stage 2 -> data/topics.jsonl
python -m neutrinos_mcp.ingest.chunk      # stage 3 -> data/chunks.jsonl
python -m neutrinos_mcp.ingest.index      # stage 4 -> data/neutrinos.db

# Query it
neutrinos-cli search "how do I bind a widget to a data model"
neutrinos-cli search "accessing data models" --product Studio --version 9
neutrinos-cli fetch studio-guide-9/data-binding --json
neutrinos-cli products

# Run the MCP server
neutrinos-mcp
```

**On a locked-down Windows machine**, two separate things can block a plain `pip install -e .`
setup, and they need different workarounds:

- `pip.exe` itself refused to run (`Access is denied`) — use `python.exe -m pip install -e .`
  instead of a bare `pip install`. The block is on that specific wrapper executable; the
  interpreter is unaffected.
- **Even after a successful install**, the `.exe` launchers pip generates for `neutrinos-mcp`,
  `neutrinos-cli` and `neutrinos-build` (in `.venv\Scripts\`) can hit the *identical*
  `Access is denied` when actually run — confirmed on this project's own dev machine. Whatever
  policy blocks `pip.exe` evidently blocks freshly-generated console-script launchers in
  general, not `pip.exe` by name specifically. The fix is the same in both cases: never invoke
  the `.exe`, always go through the interpreter — `python.exe -m neutrinos_mcp.cli ...` instead
  of `neutrinos-cli ...`, and for the server:

  ```powershell
  claude mcp add neutrinos-docs --scope user `
    -- "<repo>\.venv\Scripts\python.exe" -m neutrinos_mcp.server
  ```

  This works whether or not `pip install -e .` succeeded — `config.py` resolves every path
  against the source checkout, not site-packages, so if the install step failed entirely, add
  `-e PYTHONPATH="<repo>\src"` to the command above and it behaves identically. `install.ps1`
  already does this (see below), so this only matters if you're registering by hand.

## Distribution and auto-update

`.github/workflows/build-db.yml` runs the four ingest stages daily against the live site and
publishes `data/neutrinos.db` as a GitHub release asset (`raw/` is cached between runs so this
is actually incremental, not a full re-crawl every day — see the workflow's comments).
`install.sh` clones the repo and pulls the latest release DB via `gh release download`; if `gh`
isn't available, `neutrinos_mcp.server._check_for_db_updates_once` fetches it the first time the
server starts instead. That check runs once per process, in a background thread, and never on
the request path — see its docstring for why that distinction matters (a synchronous version of
it once tore down a live MCP connection on a slow corporate network).

## Layout

```
.github/workflows/build-db.yml   daily ingest + GitHub release publish (see Distribution above)
install.sh       macOS/Linux installer: clone, venv, pip install -e ., fetch release DB, register
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
