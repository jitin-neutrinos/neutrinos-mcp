# AGENTS.md

Context for AI coding agents working in the `neutrinos-mcp` repository. This file serves as the canonical onboarding manual. Read this before modifying any code.

## What this is

The **Neutrinos MCP Server** is a Model Context Protocol server that handles document indexing, hybrid retrieval (BM25 + Dense Vectors via `sqlite-vec`), and Agentic GraphRAG (relational entity extraction) for the Neutrinos documentation corpus. It is consumed by the main Discourse RAG Bot over HTTP.

**`implementation_plan.md` is the source of truth.** It carries the full architecture and data model. Read it before proposing major architectural changes.

## Tech Stack & Architecture

- **Language:** Python 3.11+
- **Core Framework:** `fastmcp` (MCP 2026-07-28 support)
- **Database:** SQLite (with `sqlite-vec` extension for vector similarity search). 
- **Embeddings:** `fastembed` using `BAAI/bge-small-en` (Runs locally on CPU via ONNX, zero external API calls).
- **Graph Extraction:** Uses local SLMs (via Ollama/phi3) or NVIDIA NIM APIs for extraction, mapped into relational SQLite tables (`entity`, `entity_relation`).

## Critical Rules & Constraints

1. **Separation of Concerns:** This repository ONLY provides the data engine and tool definitions (e.g., `search_docs`, `traverse_knowledge_graph`). The actual Agent orchestrator logic (LangGraph, ReAct loops) lives in the separate `RAG-bot` repository. Do NOT add LLM orchestrator logic here.
2. **Single Artifact Portability:** Do not introduce networked databases (Postgres/Redis) to this repo. The entire knowledge base must remain a portable `.db` file (`neutrinos.db`).
3. **API Independence:** By default, ingestion and search must run locally without requiring external APIs (hence the use of `fastembed` and `sqlite-vec`). If introducing LLM extraction tasks, always provide a local-first fallback (e.g., `entity_extract_local.py`).
4. **Secrets Policy:** Never hardcode credentials. API keys (e.g., NVIDIA NIM) must be passed via `.env` or environment variables and never logged in shell histories.

## Critical Commands

- **Build Index:** `python -m neutrinos_mcp.ingest.index` (Requires `sqlite_vec`)
- **Run Graph Extraction (Local SLM):** `python -m neutrinos_mcp.ingest.entity_extract_local`
- **Run Server:** `python -m neutrinos_mcp.server --transport http --host 0.0.0.0 --port 8931`
- **Run Tests:** `python -m pytest`

## Skills Mandate
- **Mandate:** Always use the `caveman` and `ponytail` skills while working on these projects.
