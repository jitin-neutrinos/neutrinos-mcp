# Product Requirements Document (PRD): Neutrinos Advanced GraphRAG MCP

## 1. Meta Information
* **Product Name**: Neutrinos Advanced GraphRAG MCP Server
* **Target Consumer**: Discourse RAG Responder AI Agent
* **Document Status**: Draft / Approved for Implementation
* **Primary Objective**: Provide a standardized, highly accurate, and context-aware Retrieval-Augmented Generation (RAG) interface over the Neutrinos documentation using the Model Context Protocol (MCP).

---

## 2. Background & Motivation
The Neutrinos documentation is comprehensive, highly technical, and deeply interconnected via hyperlinks. A standard keyword search or a naive Vector RAG implementation will struggle with this dataset because:
1. **Vocabulary Mismatch**: Users on Discourse may use different terms than the official documentation.
2. **Context Loss**: Technical concepts often span multiple linked pages (e.g., configuring a feature on page A requires understanding a prerequisite on page B).
3. **Hallucination Risks**: LLMs answering forum questions must be grounded in exact, highly relevant snippets to avoid generating misleading technical advice.

**The Solution:** An **Advanced GraphRAG** architecture exposed via an **MCP Server**. 
By combining Semantic Vector Search, Cross-Encoder Re-ranking, and Knowledge Graph traversal, the Discourse Responder can dynamically explore the documentation, retrieving exact answers and walking the graph of related concepts when necessary.

---

## 3. Architecture & Tech Stack

The architecture is designed to run locally, ensuring fast latency and avoiding external API costs, while delivering state-of-the-art retrieval performance.

### 3.1. Infrastructure
* **MCP Server Framework**: `FastMCP` (Python) - A lightweight, robust wrapper for the official Anthropic MCP SDK.
* **Vector Database**: `ChromaDB` - Local, embeddable, and highly optimized for semantic search.
* **Graph & Relational Storage**: `SQLite` - Stores the raw document text and the edge relationships (hyperlinks) between documents.

### 3.2. AI & ML Models (Local)
* **Embedding Model**: `BAAI/bge-small-en-v1.5` 
  * *Rationale*: Consistently ranks at the top of the MTEB (Massive Text Embedding Benchmark) for retrieval tasks in its size class.
* **Re-ranking Model**: `cross-encoder/ms-marco-MiniLM-L-6-v2`
  * *Rationale*: Bi-encoders (standard vector search) are fast but less precise. A Cross-Encoder evaluates the exact relationship between the query and the retrieved chunk, significantly boosting top-K accuracy and minimizing hallucinations.
* **Chunking Strategy**: `LangChain RecursiveCharacterTextSplitter` 
  * *Strategy*: 512 tokens with a 50-token overlap, respecting markdown boundaries (headers, code blocks).

---

## 4. Data Model

The data exists in two complementary stores:

### 4.1. The Knowledge Graph (SQLite)
* **Table: `documents`** (The Nodes)
  * `url` (TEXT, Primary Key)
  * `title` (TEXT)
  * `content` (TEXT) - Full markdown content.
* **Table: `edges`** (The Relationships)
  * `source_url` (TEXT)
  * `target_url` (TEXT)
  * *Primary Key*: (source_url, target_url)

### 4.2. The Semantic Index (ChromaDB)
* **Collection: `neutrinos_chunks`**
  * `id`: Hash of the chunk.
  * `embedding`: Dense vector (384 dimensions for bge-small).
  * `document`: The chunk text.
  * `metadata`: `{ "url": "...", "title": "...", "chunk_index": int }`

---

## 5. MCP Tool Definitions (The API)

The MCP server will expose the following tools to the Discourse RAG Responder. The tool count is intentionally kept minimal to prevent LLM prompt bloat and decision paralysis.

### 1. `advanced_hybrid_search(query: str, top_k: int = 5)`
* **Description**: The primary entry point. Performs a semantic search for the query, retrieves the top 20 chunks from ChromaDB, and passes them through the Cross-Encoder. Returns the top `k` re-ranked chunks.
* **Returns**: List of highly accurate text chunks, accompanied by their source URLs and confidence scores.

### 2. `read_full_context(url: str)`
* **Description**: Used when the responder LLM determines that a returned chunk is relevant but lacks surrounding context (e.g., a chunk containing the middle of a large code block). 
* **Returns**: The complete, un-chunked document text from the SQLite `documents` table.

### 3. `traverse_knowledge_graph(url: str)`
* **Description**: Exposes the structural layout of the documentation. Given a URL, queries the SQLite `edges` table.
* **Returns**: 
  * `outgoing_links`: Articles that this page references.
  * `incoming_links`: Articles that reference this page.
* **Use Case**: Allows the agent to conceptually "click around" the documentation if it realizes a prerequisite or related concept is needed to formulate the answer.

---

## 6. Implementation Phases

### Phase 1: Data Acquisition (In Progress)
* **Status**: Currently executing.
* **Tasks**: Playwright crawler navigates `documentation.neutrinos.com`, bypassing SPA rendering issues, and populates `neutrinos_docs.db` with raw text and hyperlink edges.

### Phase 2: Ingestion & Vectorization Pipeline
* **Tasks**: 
  1. Develop `ingest.py` to read `neutrinos_docs.db`.
  2. Implement Langchain text splitters to chunk the markdown.
  3. Generate embeddings using `bge-small-en-v1.5`.
  4. Upsert vectors and metadata into a local ChromaDB instance within the `neutrinos-mcp` directory.

### Phase 3: MCP Server Development
* **Tasks**:
  1. Initialize a `FastMCP` server.
  2. Implement the `advanced_hybrid_search` function, integrating ChromaDB querying and Cross-Encoder re-ranking.
  3. Implement `read_full_context` and `traverse_knowledge_graph` as SQLite wrappers.
  4. Expose the server via `stdio` transport for easy integration with the Discourse bot.

### Phase 4: Integration & Evaluation
* **Tasks**:
  1. Connect the Discourse RAG Responder to the MCP server.
  2. **Evaluation**: Test against 50 historical Discourse questions.
  3. **Metrics**: Aim for an MRR@5 (Mean Reciprocal Rank) > 0.85 and a Hallucination Rate < 2%.

---

## 7. Security & Governance
* The MCP server operates in a read-only capacity against the SQLite and Chroma databases.
* GraphRAG endpoints do not execute dynamic code; they only return structural data and string content.
* All processing happens locally, ensuring no proprietary documentation data is leaked to third-party embedding APIs.
