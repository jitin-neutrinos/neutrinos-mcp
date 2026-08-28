# CLAUDE.md

@AGENTS.md

Everything in `AGENTS.md` applies. **Read it first** — it holds the project context, architectural constraints, and tool definitions. This file adds only what is specific to Claude Code workflows in the `neutrinos-mcp` repo.

## Claude-Specific Workflow

- **No Auto-Generation:** Do not auto-generate generic project documentation or overwrite `AGENTS.md`. The instruction budgets are carefully curated (under 150 lines).
- **Background Tasks:** Long-running commands like `python -m neutrinos_mcp.ingest.index` or local LLM extraction (`entity_extract_local.py`) must be executed as background tasks so the session is not blocked.
- **Reporting:** If a test or build fails due to a missing environment dependency (like `sqlite-vec` on Windows bare-metal), report it honestly to the user rather than faking success.

## Skills Mandate
- **Mandate:** Always use the `caveman` and `ponytail` skills while working on these projects.
