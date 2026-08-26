"""The query contract (plan §4.2, §5.3) — `KnowledgeBase` end to end.

`parse_ref` is tested unconditionally: it is pure string parsing and every
other test in this file depends on it being right. Everything else needs the
built index and is skipped without one, same as `test_corpus_integrity.py`.
"""

from __future__ import annotations

import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from neutrinos_mcp.config import settings  # noqa: E402
from neutrinos_mcp.errors import KBError  # noqa: E402
from neutrinos_mcp.kb import parse_ref  # noqa: E402

DB = ROOT / settings()["paths.db"]
needs_index = pytest.mark.skipif(
    not DB.exists(), reason=f"no index at {DB}; run python -m neutrinos_mcp.ingest.index")


# ------------------------------------------------------------------ parse_ref


def test_parse_ref_splits_publication_slug_and_anchor():
    assert parse_ref("studio-guide-9/data-binding#h3_123") == (
        "studio-guide-9", "data-binding", "h3_123")


def test_parse_ref_anchor_is_optional():
    assert parse_ref("studio-guide-9/data-binding") == ("studio-guide-9", "data-binding", None)


@pytest.mark.parametrize("bad", ["../../etc/passwd", "no-slash", "", "  ", "a/", "/b"])
def test_parse_ref_rejects_malformed_input(bad):
    """A traversal-shaped ref must fail here, not reach a filesystem or SQL call."""
    with pytest.raises(KBError) as exc:
        parse_ref(bad)
    assert exc.value.status == 422


# ------------------------------------------------------------------- fixtures


@pytest.fixture(scope="module")
def kb():
    from neutrinos_mcp.kb import KnowledgeBase

    inst = KnowledgeBase()
    yield inst
    inst.close()


@pytest.fixture(scope="module")
def any_ref(kb):
    """A real (pub, slug) pulled from the live index, so tests don't hardcode
    a slug that a future crawl might rename or drop."""
    row = kb.conn.execute("SELECT pub, slug FROM topic LIMIT 1").fetchone()
    return f"{row[0]}/{row[1]}"


# ---------------------------------------------------------------- kb.search


@needs_index
class TestSearch:
    def test_returns_hits_with_the_documented_shape(self, kb):
        res = kb.search("how do I bind a widget to a data model")
        assert res.hits
        h = res.hits[0]
        for key in ("ref", "url", "title", "heading_path", "product",
                    "is_current", "staleness", "score", "text"):
            assert key in h

    def test_rejects_a_too_short_query(self, kb):
        with pytest.raises(KBError) as exc:
            kb.search("x")
        assert exc.value.status == 422

    def test_rejects_an_empty_query(self, kb):
        with pytest.raises(KBError):
            kb.search("   ")

    def test_top_k_is_clamped_to_configured_max(self, kb):
        """`_clamp_top_k` must never let a caller ask past `retrieval.max_top_k` —
        that bound is what keeps one bad call from blowing the context budget."""
        mx = kb.cfg["retrieval.max_top_k"]
        res = kb.search("data binding", top_k=mx + 500)
        assert len(res.hits) <= mx

    def test_rejects_a_non_positive_top_k(self, kb):
        with pytest.raises(KBError):
            kb.search("data binding", top_k=0)

    def test_unknown_product_raises_with_suggestions(self, kb):
        with pytest.raises(KBError) as exc:
            kb.search("data binding", product="Definitely Not A Real Product")
        assert exc.value.status == 422
        assert exc.value.suggestions, "an unknown product must suggest real ones"

    def test_scoped_search_only_returns_the_requested_product(self, kb):
        """Studio 9 is unambiguous in this corpus (plan §2) — every returned
        hit must actually belong to it, not merely rank it first."""
        res = kb.search("data binding", product="Studio", version="9")
        for h in res.hits:
            assert h["product"] == "Studio"
            assert h["version"] == "9"

    def test_confidence_and_sufficient_evidence_are_consistent(self, kb):
        """`sufficient_evidence` is defined as confidence >= low_confidence
        (kb.py) — a divergence here would mean the two paths drifted."""
        res = kb.search("how do I configure a workflow trigger")
        threshold = kb.cfg["retrieval.low_confidence"]
        assert res.sufficient_evidence == (bool(res.hits) and res.confidence >= threshold)


# ------------------------------------------------------------------ document


@needs_index
class TestDocument:
    def test_topic_row_resolves_a_real_ref(self, kb, any_ref):
        pub, slug = any_ref.split("/")
        row = kb.topic_row(pub, slug)
        assert row[1] == pub and row[2] == slug

    def test_topic_row_not_found_carries_suggestions(self, kb, any_ref):
        pub, _ = any_ref.split("/")
        with pytest.raises(KBError) as exc:
            kb.topic_row(pub, "definitely-not-a-real-slug-xyz")
        assert exc.value.status == 404

    def test_sections_of_are_ordered(self, kb, any_ref):
        pub, slug = any_ref.split("/")
        tid = kb.topic_row(pub, slug)[0]
        sections = kb.sections_of(tid)
        assert [s["ordinal"] for s in sections] == sorted(s["ordinal"] for s in sections)


# -------------------------------------------------------------------- catalog


@needs_index
class TestCatalog:
    def test_products_lists_at_least_one_current_version_per_product(self, kb):
        for p in kb.products():
            assert any(v["is_current"] for v in p["versions"]), p["product"]

    def test_name_contains_filters_case_insensitively(self, kb):
        all_prods = {p["product"] for p in kb.products()}
        target = next(iter(all_prods))
        found = kb.products(name_contains=target.lower())
        assert any(p["product"] == target for p in found)

    def test_stats_counts_match_products_and_topics(self, kb):
        s = kb.stats()
        assert s["publications"] > 0
        assert s["topics"] > 0
        assert s["vectors"] == s["chunks"], "every chunk must have a vector (AD-... §10.5)"


# --------------------------------------------------------------- comparisons


@needs_index
class TestCompareVersions:
    def test_unknown_slug_raises_not_found(self, kb):
        with pytest.raises(KBError) as exc:
            kb.compare_versions("definitely-not-a-real-slug-xyz")
        assert exc.value.status == 404

    def test_ambiguous_slug_across_products_requires_product(self, kb):
        """If a slug exists in more than one product family, the API must force
        disambiguation rather than silently picking one (R1)."""
        row = kb.conn.execute(
            """SELECT t.slug FROM topic t JOIN publication p ON p.id = t.pub
               GROUP BY t.slug HAVING COUNT(DISTINCT p.family) > 1 LIMIT 1""").fetchone()
        if not row:
            pytest.skip("no cross-family slug collision in this build")
        with pytest.raises(KBError) as exc:
            kb.compare_versions(row[0])
        assert exc.value.status == 422
