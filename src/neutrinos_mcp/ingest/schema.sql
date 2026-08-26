-- =====================================================================
-- neutrinos.db — Neutrinos Documentation Retrieval MCP
-- Applied verbatim by ingest/index.py against a new file. Never migrated.
-- =====================================================================

PRAGMA journal_mode = WAL;
PRAGMA foreign_keys = ON;

-- ---------------------------------------------------------------------
-- publication — 53 rows. Version family metadata from config/publications.yaml (§6.5)
-- ---------------------------------------------------------------------
CREATE TABLE publication (
    id             TEXT    PRIMARY KEY,           -- 'studio-guide-9'
    title          TEXT    NOT NULL,              -- 'Studio Guide 9'
    product        TEXT    NOT NULL,              -- 'Studio'
    version        TEXT,                          -- '9'; NULL for unversioned
    version_rank   INTEGER NOT NULL DEFAULT 0,    -- higher = newer within family
    family         TEXT    NOT NULL,              -- 'studio'  (spans renames!)
    is_current     INTEGER NOT NULL DEFAULT 0     CHECK (is_current IN (0,1)),
    lifecycle      TEXT    NOT NULL DEFAULT 'current'
                   CHECK (lifecycle IN ('current','superseded','archived')),
    topic_count    INTEGER NOT NULL DEFAULT 0,
    newest_lastmod TEXT                           -- ISO date, max over its topics
) WITHOUT ROWID;

CREATE INDEX idx_pub_family  ON publication(family, version_rank DESC);
CREATE INDEX idx_pub_current ON publication(is_current) WHERE is_current = 1;

-- ---------------------------------------------------------------------
-- topic — 3,117 rows.
-- Surrogate INTEGER id because FTS5 external-content tables require a rowid;
-- (pub, slug) remains the logical key per AD-03 and is enforced UNIQUE.
-- ---------------------------------------------------------------------
CREATE TABLE topic (
    id           INTEGER PRIMARY KEY,
    pub          TEXT    NOT NULL REFERENCES publication(id),
    slug         TEXT    NOT NULL,
    title        TEXT    NOT NULL,
    breadcrumb   TEXT    NOT NULL DEFAULT '',
    url          TEXT    NOT NULL,                -- /articles/#!<pub>/<slug>
    lastmod      TEXT,                            -- ISO date from sitemap
    word_count   INTEGER NOT NULL DEFAULT 0,
    content_hash TEXT    NOT NULL,                -- sha256(body_md); drives delta crawl
    body_md      TEXT    NOT NULL,
    UNIQUE (pub, slug)
);

CREATE INDEX idx_topic_pub  ON topic(pub);
CREATE INDEX idx_topic_slug ON topic(slug);        -- cross-version slug lookup (§8.2 #4)

-- ---------------------------------------------------------------------
-- variant_group — cross-version near-duplicate clusters (AD-07)
-- ---------------------------------------------------------------------
CREATE TABLE variant_group (
    id                 INTEGER PRIMARY KEY,
    family             TEXT    NOT NULL,          -- groups never span families
    canonical_chunk_id INTEGER NOT NULL,          -- FK added after chunk load; see note
    member_count       INTEGER NOT NULL,
    versions_json      TEXT    NOT NULL           -- '["7","8","9"]'
);

CREATE INDEX idx_vg_family ON variant_group(family);

-- ---------------------------------------------------------------------
-- chunk — the retrieval unit. ~15k–35k rows.
-- Vectors live ONLY in vec_chunks; storing them twice would waste ~45 MB.
-- pub/slug are denormalised so filtering and ref-building need no join.
-- ---------------------------------------------------------------------
CREATE TABLE chunk (
    id               INTEGER PRIMARY KEY,
    topic_id         INTEGER NOT NULL REFERENCES topic(id),
    pub              TEXT    NOT NULL,
    slug             TEXT    NOT NULL,
    ordinal          INTEGER NOT NULL,            -- 0-based within topic
    heading_path     TEXT    NOT NULL,            -- 'Using Studio > Widgets > Binding'
    anchor           TEXT,                        -- 'h3_1689083776'; NULL if none
    level            INTEGER NOT NULL DEFAULT 2,  -- 2 = h2, 3 = h3
    text             TEXT    NOT NULL,            -- chunk body, prefix NOT included
    context_prefix   TEXT    NOT NULL,            -- §6.3 deterministic header
    token_count      INTEGER NOT NULL,
    has_code         INTEGER NOT NULL DEFAULT 0   CHECK (has_code IN (0,1)),
    simhash          INTEGER NOT NULL,            -- 64-bit, stored as signed bit pattern
    variant_group_id INTEGER          REFERENCES variant_group(id),
    UNIQUE (topic_id, ordinal)
);

CREATE INDEX idx_chunk_topic   ON chunk(topic_id);
CREATE INDEX idx_chunk_pub     ON chunk(pub);
CREATE INDEX idx_chunk_variant ON chunk(variant_group_id)
                                 WHERE variant_group_id IS NOT NULL;

-- ---------------------------------------------------------------------
-- edge — typed adjacency list (§5.1).
-- dst_pub/dst_slug are always recorded; dst_id is NULL for unresolved
-- targets (the known-broken /smart/project-… links) so gaps are surfaced.
-- ---------------------------------------------------------------------
CREATE TABLE edge (
    src_id   INTEGER NOT NULL REFERENCES topic(id),
    rel      TEXT    NOT NULL
             CHECK (rel IN ('PARENT_OF','NEXT','PREV','SEE_ALSO','LINKS_TO',
                            'SAME_TOPIC_OTHER_VERSION','SUPERSEDED_BY')),
    dst_pub  TEXT    NOT NULL,
    dst_slug TEXT    NOT NULL,
    dst_id   INTEGER          REFERENCES topic(id),
    resolved INTEGER NOT NULL DEFAULT 1 CHECK (resolved IN (0,1)),
    PRIMARY KEY (src_id, rel, dst_pub, dst_slug),
    CHECK (resolved = 0 OR dst_id IS NOT NULL)
) WITHOUT ROWID;

CREATE INDEX idx_edge_dst ON edge(dst_id, rel) WHERE dst_id IS NOT NULL;
CREATE INDEX idx_edge_rel ON edge(rel);

-- ---------------------------------------------------------------------
-- code_sample — 'how do I write this' queries hit these directly
-- ---------------------------------------------------------------------
CREATE TABLE code_sample (
    id       INTEGER PRIMARY KEY,
    topic_id INTEGER NOT NULL REFERENCES topic(id),
    chunk_id INTEGER          REFERENCES chunk(id),
    lang     TEXT,                                -- from CHCodeSample_langName
    code     TEXT    NOT NULL
);

CREATE INDEX idx_code_topic ON code_sample(topic_id);

-- ---------------------------------------------------------------------
-- build_manifest (AD-12) — verified at server start; mismatch = refuse to serve
-- ---------------------------------------------------------------------
CREATE TABLE build_manifest (
    key   TEXT PRIMARY KEY,
    value TEXT NOT NULL
) WITHOUT ROWID;
-- keys: schema_version, embedding_model, embedding_revision, embedding_dim,
--       reranker_model, reranker_revision, chunker_version, corpus_hash,
--       built_at, topic_count, chunk_count, publications_yaml_hash

-- =====================================================================
-- Full-text indexes (FTS5, external content — prose indexed, not duplicated)
-- Column WEIGHTS are applied at QUERY time via bm25(), not declared here.
-- =====================================================================

CREATE VIRTUAL TABLE chunk_fts USING fts5(
    context_prefix,
    heading_path,
    text,
    content      = 'chunk',
    content_rowid= 'id',
    tokenize     = 'porter unicode61 remove_diacritics 2'
);
-- query:  SELECT rowid, bm25(chunk_fts, 3.0, 4.0, 1.0) AS score
--         FROM chunk_fts WHERE chunk_fts MATCH ? ORDER BY score LIMIT 50;

CREATE VIRTUAL TABLE topic_fts USING fts5(
    title,
    breadcrumb,
    body_md,
    content      = 'topic',
    content_rowid= 'id',
    tokenize     = 'porter unicode61 remove_diacritics 2'
);
-- query:  bm25(topic_fts, 8.0, 3.0, 1.0)

-- No sync triggers: the DB is rebuilt from scratch each run, so index.py
-- issues INSERT INTO <fts>(<fts>) VALUES('rebuild') once, after bulk load.

-- =====================================================================
-- Vector index (sqlite-vec vec0). Loaded via sqlite_vec.load(conn).
-- Plain columns are METADATA columns: filterable in WHERE *before* distance
-- is computed, which is what makes version scoping cheap (§7.0).
-- Brute-force KNN — correct at this scale; ANN unnecessary until ~10x (AD-02).
-- =====================================================================

CREATE VIRTUAL TABLE vec_chunks USING vec0(
    chunk_id     INTEGER PRIMARY KEY,
    embedding    FLOAT[384],
    pub          TEXT,
    family       TEXT,
    version_rank INTEGER,
    is_current   INTEGER,
    +heading_path TEXT          -- auxiliary: returned, never filtered on
);
-- query:  SELECT chunk_id, distance FROM vec_chunks
--         WHERE embedding MATCH :q AND k = 50
--           AND family IN (...) AND is_current = 1;
