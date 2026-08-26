"""The tool contract (plan §8.5).

These schemas are the API. An agent never reads the plan — it reads `inputSchema`
and the description string, and every ambiguity there becomes a malformed call
at runtime. So the contract is tested as strictly as the code.

The schemas are generated from the plan's §8.5 JSON blocks, which is what keeps
the document and the server from drifting; these tests are what keep the
generated payload honest once it has been generated.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from neutrinos_mcp.tools.schemas import COMMON, DEFAULT_ENABLED, TOOLS, TOOLS_BY_NAME  # noqa: E402

jsonschema = pytest.importorskip("jsonschema", reason="pip install jsonschema")
referencing = pytest.importorskip("referencing", reason="pip install referencing")

# `common.json#/$defs/...` is a real cross-file reference (§8.5), not a typo —
# `test_common_definitions_are_referenced_not_duplicated` requires the $ref
# indirection rather than inlined copies. A bare Draft202012Validator cannot
# resolve it, so every validator built here shares one registry that maps the
# retrieval-uri tools actually use ("common.json") to the COMMON document.
_REGISTRY = referencing.Registry().with_resource(
    "common.json", referencing.Resource.from_contents(COMMON))


def _validator(schema):
    return jsonschema.Draft202012Validator(schema, registry=_REGISTRY)


EXPECTED = {"search_docs", "fetch_document", "list_related",
            "compare_versions", "list_products", "answer_pack"}


def test_the_expected_tools_are_defined():
    assert set(TOOLS_BY_NAME) == EXPECTED


def test_answer_pack_is_defined_but_not_enabled():
    """Phase 5, gated on evaluation (§8.2 #6) — defined so the contract is
    complete, unregistered so it cannot be called before it is earned."""
    assert "answer_pack" in TOOLS_BY_NAME
    assert "answer_pack" not in DEFAULT_ENABLED
    assert set(DEFAULT_ENABLED) == EXPECTED - {"answer_pack"}


@pytest.mark.parametrize("tool", TOOLS, ids=lambda t: t["name"])
def test_schema_is_valid_json_schema(tool):
    jsonschema.Draft202012Validator.check_schema(tool["inputSchema"])


@pytest.mark.parametrize("tool", TOOLS, ids=lambda t: t["name"])
def test_no_additional_properties(tool):
    """Open schemas let a typo'd argument pass silently and change nothing —
    the agent then retries the same wrong call because nothing objected."""
    assert tool["inputSchema"].get("additionalProperties") is False


@pytest.mark.parametrize("tool", TOOLS, ids=lambda t: t["name"])
def test_every_property_is_described(tool):
    """The description is the only documentation the model gets."""
    missing = [k for k, v in tool["inputSchema"].get("properties", {}).items()
               if not (v.get("description") or "").strip()]
    assert not missing, f"{tool['name']}: undescribed {missing}"


@pytest.mark.parametrize("tool", TOOLS, ids=lambda t: t["name"])
def test_tool_description_states_when_to_use_it(tool):
    """Anthropic's tool-design guidance: a name is not enough to disambiguate
    five overlapping retrieval tools. Each must say what it is *for*."""
    d = tool.get("description", "")
    assert len(d) >= 120, f"{tool['name']}: description too thin ({len(d)} chars)"


@pytest.mark.parametrize("tool", TOOLS, ids=lambda t: t["name"])
def test_bounded_arguments_have_limits(tool):
    """Any integer an agent can pass must be bounded, or one bad call can ask
    for the whole corpus and blow the context budget."""
    for name, spec in tool["inputSchema"].get("properties", {}).items():
        if spec.get("type") == "integer":
            assert "minimum" in spec and "maximum" in spec, f"{tool['name']}.{name}"
        if spec.get("type") == "string" and name in ("query", "ref", "slug"):
            assert "minLength" in spec, f"{tool['name']}.{name}"


@pytest.mark.parametrize("tool", TOOLS, ids=lambda t: t["name"])
def test_response_format_enum_where_offered(tool):
    """`response_format` must be a closed enum — a free string means the server
    silently falls back to a default the agent did not ask for."""
    spec = tool["inputSchema"].get("properties", {}).get("response_format")
    if spec is not None:
        assert spec.get("enum"), f"{tool['name']}: response_format must be an enum"
        assert "default" in spec


def _resolve_ref_spec(spec: dict) -> dict:
    """`ref` properties are `{"$ref": ...}` or `{"allOf": [{"$ref": ...}]}`
    pointing at `common.json#/$defs/ref` — resolve through the same registry
    the validators use rather than requiring the pattern to be inlined, which
    would defeat the $ref indirection `test_common_definitions_are_referenced_
    not_duplicated` requires."""
    ref = spec.get("$ref") or next(
        (s["$ref"] for s in spec.get("allOf", []) if "$ref" in s), None)
    if not ref:
        return spec
    resolver = _REGISTRY.resolver()
    return resolver.lookup(ref).contents


def test_ref_pattern_is_anchored_and_shared():
    """A `ref` is the join between every tool. If two tools disagree on its
    shape, an agent can copy a value out of one and have it rejected by the
    next — the single worst failure mode in a multi-tool loop."""
    pats = {}
    for t in TOOLS:
        spec = t["inputSchema"].get("properties", {}).get("ref")
        if not spec:
            continue
        resolved = _resolve_ref_spec(spec)
        if "pattern" in resolved:
            pats[t["name"]] = resolved["pattern"]
    assert pats, "no tool constrains `ref`"
    assert len(set(pats.values())) == 1, f"divergent ref patterns: {pats}"
    pat = next(iter(pats.values()))
    assert pat.startswith("^") and pat.endswith("$")
    rx = re.compile(pat)
    assert rx.match("studio-guide-9/data-binding")
    assert rx.match("studio-guide-9/data-binding#h3_1689083776")
    assert not rx.match("../etc/passwd")
    assert not rx.match("studio-guide-9")


def test_examples_validate_against_their_own_schema():
    """An example that does not validate teaches the model a malformed call."""
    for t in TOOLS:
        v = _validator(t["inputSchema"])
        for ex in t.get("examples", []):
            errs = sorted(v.iter_errors(ex.get("arguments", ex)), key=str)
            assert not errs, f"{t['name']} example invalid: {[e.message for e in errs]}"


# ------------------------------------------------------- negative validation


def _v(name):
    return _validator(TOOLS_BY_NAME[name]["inputSchema"])


def test_search_docs_rejects_an_unknown_argument():
    """`top_k` is a real property — this must fail on the typo, not on that."""
    assert not _v("search_docs").is_valid(
        {"query": "how do I bind a widget", "bogus_argument": 5})


def test_search_docs_rejects_top_k_above_maximum():
    """Uses a valid-length query so the failure is attributable to `top_k`
    alone — an earlier version of this test passed only because `minLength`
    fired first on a one-character query."""
    assert not _v("search_docs").is_valid(
        {"query": "how do I bind a widget", "top_k": 9999})


def test_search_docs_rejects_a_too_short_query():
    assert not _v("search_docs").is_valid({"query": "x"})


def test_search_docs_accepts_a_minimal_call():
    assert _v("search_docs").is_valid({"query": "how do I bind a widget"})


def test_fetch_document_rejects_a_traversal_ref():
    assert not _v("fetch_document").is_valid({"ref": "../../etc/passwd"})


def test_common_definitions_are_referenced_not_duplicated():
    """`$defs` exist so the shared shapes have one definition; a schema that
    inlines its own copy is the drift this indirection prevents."""
    assert COMMON, "no shared definitions"
    blob = json.dumps(TOOLS)
    assert "$ref" in blob
