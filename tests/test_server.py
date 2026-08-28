"""The MCP adapter (plan §8.4) — `call_tool` and `build_server`.

Every enabled tool is exercised through `call_tool`, the same function
`build_server` wires to FastMCP, and its response is checked against the
declared `outputSchema` — the one guarantee AD-11 makes: what leaves the
server matches what the schema promises, or the violation is surfaced
in-band rather than shipped silently.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from neutrinos_mcp.config import settings  # noqa: E402
from neutrinos_mcp.tools.schemas import DEFAULT_ENABLED, TOOLS_BY_NAME  # noqa: E402

DB = ROOT / settings()["paths.db"]
needs_index = pytest.mark.skipif(
    not DB.exists(), reason=f"no index at {DB}; run python -m neutrinos_mcp.ingest.index")

if DB.exists():
    import neutrinos_mcp.server as server


@pytest.fixture(scope="module")
def any_ref():
    kb = server.kb()
    row = kb.conn.execute("SELECT pub, slug FROM topic LIMIT 1").fetchone()
    return f"{row[0]}/{row[1]}"


@needs_index
class TestCallTool:
    ARGS = {
        "search_docs": {"query": "how do I bind a widget to a data model"},
        "list_products": {},
    }

    @pytest.mark.parametrize("name", sorted(DEFAULT_ENABLED))
    def test_default_enabled_tool_returns_a_schema_valid_payload(self, name, any_ref):
        args = dict(self.ARGS.get(name, {}))
        if name in ("fetch_document", "list_related"):
            args["ref"] = any_ref
        if name == "compare_versions":
            args["slug"] = any_ref.split("/")[1]
        payload, is_error = server.call_tool(name, args)
        assert not is_error, payload
        assert "_schema_warnings" not in payload, payload.get("_schema_warnings")

    def test_unknown_tool_is_an_error_not_an_exception(self):
        payload, is_error = server.call_tool("not_a_real_tool", {})
        assert is_error
        assert payload["status"] == 422

    def test_bad_ref_is_an_error_payload_not_a_crash(self):
        payload, is_error = server.call_tool("fetch_document", {"ref": "../../etc/passwd"})
        assert is_error
        assert payload["status"] in (400, 422)

    def test_index_built_at_is_strict_rfc3339(self):
        """`jsonschema`'s own format check for `date-time` is lenient enough to
        accept a bare local-time string with no offset at all (confirmed by
        testing it directly) -- so schema validation passing here proves
        nothing. This is the check that actually caught the real bug: Claude
        Desktop's MCP client enforces the stricter RFC 3339 rule that a
        date-time value MUST carry a "Z" or a numeric offset."""
        payload, is_error = server.call_tool("list_products", {})
        assert not is_error
        ts = payload["index_built_at"]
        assert re.match(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(\.\d+)?(Z|[+-]\d{2}:\d{2})$", ts), \
            f"index_built_at {ts!r} has no RFC 3339 time-offset"

    def test_output_never_leaks_private_underscore_keys(self, any_ref):
        payload, _ = server.call_tool("search_docs", {"query": "data binding"})

        def _walk(obj):
            if isinstance(obj, dict):
                assert not any(k.startswith("_") for k in obj), obj
                for v in obj.values():
                    _walk(v)
            elif isinstance(obj, list):
                for v in obj:
                    _walk(v)

        _walk(payload)


@needs_index
def test_build_server_registers_exactly_the_default_enabled_tools():
    import asyncio

    mcp = server.build_server()
    # FastMCP's registered-tool names are the contract surface (plan §8.4) —
    # this must match DEFAULT_ENABLED exactly, not a superset or subset.
    names = {t.name for t in asyncio.run(mcp.list_tools())}
    assert names == set(DEFAULT_ENABLED)


def test_answer_pack_is_wired_to_a_handler():
    """Phase 5's gate (plan §8.2 #6) is lifted by explicit decision, once a
    real downstream consumer existed whose own architecture already needed
    exactly this (a Discourse-question-answering bot treating
    `recommended_action` as binding) — see `handlers.answer_pack`'s
    docstring. `DEFAULT_ENABLED` is untouched: still opt-in via `--tools`,
    not on by default."""
    from neutrinos_mcp.tools.handlers import HANDLERS

    assert "answer_pack" in TOOLS_BY_NAME
    assert "answer_pack" in HANDLERS
    assert "answer_pack" not in DEFAULT_ENABLED


@needs_index
class TestAnswerPack:
    def test_returns_schema_valid_payload_for_a_well_covered_question(self):
        payload, is_error = server.call_tool(
            "answer_pack", {"question": "how do I bind a widget to a data model"})
        assert not is_error, payload
        assert "_schema_warnings" not in payload, payload.get("_schema_warnings")
        assert payload["recommended_action"] in (
            "answer", "answer_with_caveat", "ask_for_version", "escalate")
        assert 0 <= payload["confidence"] <= 1

    def test_escalates_on_a_question_the_docs_do_not_cover(self):
        payload, is_error = server.call_tool(
            "answer_pack",
            {"question": "what is the capital of France and how many people live there"})
        assert not is_error, payload
        assert payload["recommended_action"] == "escalate"
        assert payload["evidence"] == [] or payload["confidence"] < 1
        assert payload["coverage_notes"]

    def test_citations_are_deduplicated_by_url(self):
        payload, is_error = server.call_tool(
            "answer_pack", {"question": "how do I bind a widget to a data model"})
        assert not is_error, payload
        urls = [c["url"] for c in payload["citations"]]
        assert len(urls) == len(set(urls))

    def test_respects_a_small_token_budget(self):
        payload, is_error = server.call_tool(
            "answer_pack",
            {"question": "how do I bind a widget to a data model", "token_budget": 1000})
        assert not is_error, payload
        assert payload["tokens_used"] <= 1000 or len(payload["evidence"]) <= 1

    def test_caveat_is_null_unless_action_is_answer_with_caveat(self):
        payload, is_error = server.call_tool(
            "answer_pack", {"question": "how do I bind a widget to a data model"})
        assert not is_error, payload
        if payload["recommended_action"] != "answer_with_caveat":
            assert payload["caveat"] is None
