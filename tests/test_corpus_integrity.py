"""Invariants the built index must satisfy (plan §10.5, §11.3).

These run against the real artifact, so they are skipped when it is absent —
a fresh clone should not fail its test suite for want of a 26-minute build.

What they exist to catch is a class of failure that unit tests structurally
cannot: the index builds without error, every query returns something, and the
answers are quietly wrong because a join dropped rows, the FTS table drifted
out of sync with `chunk`, or the vector count silently diverged.
"""

from __future__ import annotations

import json
import sqlite3
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from neutrinos_mcp.config import publications, settings  # noqa: E402

DB = ROOT / settings()["paths.db"]
pytestmark = pytest.mark.skipif(
    not DB.exists(), reason=f"no index at {DB}; run python -m neutrinos_mcp.ingest.index")


@pytest.fixture(scope="module")
def conn():
    from neutrinos_mcp.vectorstore import SqliteVecStore

    c = sqlite3.connect(f"file:{DB}?mode=ro", uri=True)
    SqliteVecStore.load_extension(c)
    yield c
    c.close()


@pytest.fixture(scope="module")
def manifest(conn):
    rows = dict(conn.execute("SELECT key, value FROM build_manifest").fetchall())
    return rows


def one(conn, sql, *a):
    return conn.execute(sql, a).fetchone()[0]


# ------------------------------------------------------------------ counts


def test_census_totals_match_the_index(conn):
    """The index must contain the corpus we measured, not a partial crawl."""
    census = json.loads((ROOT / "data" / "census.json").read_text(encoding="utf-8"))
    assert one(conn, "SELECT COUNT(*) FROM publication") == census["totals"]["publications"]
    assert one(conn, "SELECT COUNT(*) FROM topic") == census["totals"]["topics"]


def test_every_chunk_has_a_vector(conn):
    """A missing vector is invisible: the chunk is BM25-reachable but never
    dense-reachable, so it drops out of exactly the queries dense retrieval
    exists to serve."""
    assert one(conn, "SELECT COUNT(*) FROM vec_chunks") == one(conn, "SELECT COUNT(*) FROM chunk")


def test_fts_is_in_sync_with_chunk(conn):
    """External-content FTS5 does not self-maintain — a forgotten rebuild leaves
    a stale shadow table that still answers queries.

    Row counts are necessary but not sufficient: a rebuild against shifted
    rowids keeps the count and corrupts every mapping. So a match is also
    followed back to `chunk` to confirm the rowid actually addresses the row
    whose text was indexed. The `integrity-check` pragma is not used here — it
    needs a writable handle, and the test must not be able to mutate the
    shipped index.
    """
    assert one(conn, "SELECT COUNT(*) FROM chunk_fts") == one(conn, "SELECT COUNT(*) FROM chunk")
    row = conn.execute(
        """SELECT f.rowid, c.text FROM chunk_fts f JOIN chunk c ON c.id = f.rowid
           WHERE chunk_fts MATCH 'component' LIMIT 1""").fetchone()
    assert row, "FTS returned no hit for a term that certainly occurs"
    assert "component" in row[1].lower() or "component" in one(
        conn, "SELECT heading_path || ' ' || context_prefix FROM chunk WHERE id=?",
        row[0]).lower()


def test_topic_fts_is_in_sync(conn):
    assert one(conn, "SELECT COUNT(*) FROM topic_fts") == one(conn, "SELECT COUNT(*) FROM topic")


# ------------------------------------------------------- referential health


def test_no_orphan_chunks(conn):
    assert one(conn, "SELECT COUNT(*) FROM chunk c "
                     "LEFT JOIN topic t ON t.id=c.topic_id WHERE t.id IS NULL") == 0


def test_foreign_keys_hold(conn):
    assert conn.execute("PRAGMA foreign_key_check").fetchall() == []


def test_resolved_edges_point_somewhere(conn):
    """`resolved=1` with a null destination would make graph expansion silently
    traverse nothing — the CHECK constraint should make this impossible."""
    assert one(conn, "SELECT COUNT(*) FROM edge WHERE resolved=1 AND dst_id IS NULL") == 0


def test_unresolved_edge_share_is_within_tolerance(conn):
    """Measured 2,024 of 6,675 links unresolved (30%) — mostly cross-publication
    and external. A sharp rise means the slug normaliser broke."""
    total = one(conn, "SELECT COUNT(*) FROM edge")
    unresolved = one(conn, "SELECT COUNT(*) FROM edge WHERE resolved=0")
    assert total > 0
    assert unresolved / total < 0.45, f"{unresolved}/{total} unresolved"


# ------------------------------------------------------------- versioning


def test_every_publication_is_classified(conn):
    reg = publications()
    pubs = [r[0] for r in conn.execute("SELECT id FROM publication")]
    assert [p for p in pubs if p not in reg] == []


def test_exactly_one_current_publication_per_family(conn):
    reg = publications()
    for fam, pubs in reg.products().items():
        assert sum(1 for p in pubs if p.is_current) == 1, fam


def test_variant_groups_never_span_two_families(conn):
    """A group spanning families would collapse Studio content into a Components
    answer — a wrong-product hit that looks perfectly confident."""
    bad = conn.execute(
        """SELECT c.variant_group_id, COUNT(DISTINCT p.product)
           FROM chunk c JOIN publication p ON p.id = c.pub
           WHERE c.variant_group_id IS NOT NULL
           GROUP BY c.variant_group_id HAVING COUNT(DISTINCT p.product) > 1""").fetchall()
    assert bad == [], f"cross-family groups: {bad[:5]}"


def test_variant_group_canonical_is_a_member(conn):
    bad = conn.execute(
        """SELECT g.id FROM variant_group g
           LEFT JOIN chunk c ON c.id = g.canonical_chunk_id AND c.variant_group_id = g.id
           WHERE c.id IS NULL""").fetchall()
    assert bad == [], f"canonical not in group: {bad[:5]}"


# ---------------------------------------------------------------- content


def test_no_boilerplate_leaked_into_chunk_text(conn):
    """`div class="footer"` once leaked copyright text into 1,077 of 3,117
    topics. Five remain, all genuine prose mentions."""
    n = one(conn, "SELECT COUNT(*) FROM chunk WHERE text LIKE '%All Rights Reserved%'"
                  " OR text LIKE '%Was this helpful%'")
    assert n <= 20, f"{n} chunks contain footer boilerplate"


def test_chunks_carry_the_contextual_prefix(conn):
    """AD-06: the prefix is what makes a bare chunk answerable. If it is empty
    the dense arm loses its product/version signal entirely."""
    assert one(conn, "SELECT COUNT(*) FROM chunk WHERE context_prefix IS NULL "
                     "OR context_prefix = ''") == 0


def test_no_empty_chunks(conn):
    assert one(conn, "SELECT COUNT(*) FROM chunk WHERE TRIM(text) = ''") == 0


def test_manifest_records_the_embedding_model(manifest):
    """The query side must use the model the index was built with; a mismatch
    produces plausible-looking nonsense rather than an error."""
    cfg = settings()
    assert manifest["embedding_model"] == cfg["embedding.model"]
    assert int(manifest["embedding_dim"]) == cfg["embedding.dim"]


def test_manifest_query_prefix_matches_settings(manifest):
    """BGE is asymmetric: the instruction goes on the query side only. If the
    index was built under a different prefix than the server applies, nothing
    errors — every result just gets quietly worse."""
    assert manifest.get("embedding_query_prefix") == settings()["embedding.query_prefix"]
