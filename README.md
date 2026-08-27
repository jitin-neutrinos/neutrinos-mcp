# neutrinos-mcp

A retrieval MCP server over the Neutrinos documentation corpus (53 publications, 3,117 topics,
7,810 indexed chunks). Hybrid BM25 + dense retrieval, RRF fusion, cross-encoder reranking,
cross-version near-duplicate collapse, and conditional link-graph expansion — built to answer
"is this true for the version the user is actually on", which a naive semantic-search-over-docs
setup gets wrong on this corpus more than half the time. See `implementation_plan.md` for the
full design rationale (architecture decisions, data model, evaluation methodology).

## Quick start

`neutrinos-mcp` is a **public** repo, so no authentication is needed to clone it, fetch a release,
or run either one-liner below — just `git` and (optionally) `gh` for pulling the pre-built database
faster (see Distribution below; without `gh` the server fetches it automatically on first use
instead, just not during install).

**macOS/Linux — one line:**

```bash
curl -fsSL https://raw.githubusercontent.com/jitin-neutrinos/neutrinos-mcp/master/install.sh | bash
```

**Windows (PowerShell) — one line:**

```powershell
iex (irm https://raw.githubusercontent.com/jitin-neutrinos/neutrinos-mcp/master/install.ps1)
```

Each fetches the installer script itself (not the whole repo) and runs it directly — earlier
versions of this README had the one-liner do its own `git clone` first and then invoke the
script from inside it, which duplicated the script's own clone step and, on a machine with a
stale `~/.neutrinos-mcp` left by an interrupted previous run, failed at that outer clone before
the script ever got a chance to detect and clean up the mess (`git clone` refuses to run at all
against a non-empty target). Fetching just the script and letting it manage the target
directory itself avoids that class of bug entirely.

Each script: checks whether an install already exists there and is genuinely complete (a
`.install_complete` marker written only at the end of a prior successful run) — if so it updates
in place (`git pull`); if a directory exists but isn't marked complete (wreckage from an
interrupted run, exactly what caused the bug above), it's removed before cloning fresh. It then
creates a venv, installs the package (`python -m pip install -e .` — never a bare `pip`/`pip.exe`,
since that executable specifically gets blocked by execution policy on some locked-down corporate
machines while `python.exe` itself is still allowed), fetches the latest pre-built
`data/neutrinos.db` from the newest GitHub release via `gh release download` if `gh` is installed
(otherwise the running server fetches it on first use instead — see Distribution below), registers
`neutrinos-docs` with Claude Code at **user scope** (every project, not just this one), and merges
an entry into Claude Desktop's `claude_desktop_config.json` (macOS/Linux/Windows paths handled;
merged with a small Python script, not overwritten, since that file commonly already has other MCP
servers in it). **This also covers Cowork** — the agentic-work tab in the Claude Desktop app isn't
a separate app and has no config of its own; Desktop's own SDK layer bridges servers registered in
its config into Cowork's sandboxed VM automatically. A server added directly inside a Cowork
session, by contrast, can't connect at all (the VM is isolated from the host), which is why the
registration target is Desktop's config file specifically. **If anything up through the package
install fails, everything the run created is removed before it exits** — a failed attempt never
leaves wreckage behind to break the next one; a failure in the DB fetch or either registration step
does not, since a working local install that just hasn't fetched its DB yet, or still needs manual
registration, isn't "failed." **Restart Claude Code / Claude Desktop afterward** — a server
registered while a session is already running isn't picked up until the client reconnects.

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
