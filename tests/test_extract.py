"""Extraction invariants (plan §6.2).

Each test here pins a bug that was actually hit during the build, because each
one silently degrades the whole corpus rather than raising.
"""

from __future__ import annotations

import sys
from pathlib import Path

import pytest
from lxml import html as LH

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from neutrinos_mcp.ingest.extract import (  # noqa: E402
    clean_text, inline_md, map_link, parse_topic,
)

FIX = Path(__file__).parent / "fixtures"
PUBS = {"components-guide-8", "ai-hub", "how-to-articles-8", "studio-guide-9"}


def _topic(name: str, pub: str, slug: str):
    return parse_topic((FIX / name).read_bytes(), pub, slug, "http://x", None, PUBS)


# --------------------------------------------------------------- inline pass


def test_inline_node_keeps_the_elements_own_markup():
    """Walking an <a>'s CHILDREN emits the text and drops the link.

    This cost every cross-reference in the corpus the first time.
    """
    el = LH.fromstring('<p>see <a href="/articles/x/y">the guide</a> now</p>')
    md = inline_md(el)
    assert "[the guide](/articles/x/y)" in md, md


def test_bold_and_code_survive_nesting():
    el = LH.fromstring("<p>Use <b>Save</b> then <code>flush()</code></p>")
    md = inline_md(el)
    assert "**Save**" in md and "`flush()`" in md


def test_list_walker_does_not_mutate_the_dom():
    """Rendering must never detach nodes: the DOM is read again for links.

    Detaching nested <ol> is how the /smart/ cross-links vanished.
    """
    doc = LH.fromstring(
        '<div><ol><li>outer'
        '<ol><li>inner <a href="/articles/p/q">link</a></li></ol>'
        "</li></ol></div>")
    before = len(doc.xpath(".//a"))
    from neutrinos_mcp.ingest.extract import _block_md

    _block_md(doc.xpath(".//ol")[0])
    assert len(doc.xpath(".//a")) == before, "renderer mutated the tree"


def test_nested_list_link_is_harvested():
    t = _topic("button.html", "components-guide-8", "button")
    targets = {(l.target_pub, l.target_slug) for l in t.links}
    assert ("project-sample-how-to-guide", "bind-page-flows-to-components") in targets


# ------------------------------------------------------------- furniture


def test_sidebar_is_separated_not_discarded():
    t = _topic("button.html", "components-guide-8", "button")
    assert t.mini_toc, "mini-TOC should be captured"
    for entry in t.mini_toc:
        # captured as structure, absent from prose
        assert f"\n{entry}\n" not in t.body_md or entry in [s.heading for s in t.sections]


def test_footer_boilerplate_never_reaches_prose():
    """<div class="footer"> — a tag-only check misses it and leaked copyright
    text into 1,077 of 3,117 topics."""
    t = _topic("retrain-model.html", "ai-hub", "retrain-model")
    low = t.body_md.lower()
    assert "all rights reserved" not in low
    assert "send feedback" not in low
    assert "clickhelp.co" not in low


def test_prev_next_captured_as_structure():
    t = _topic("button.html", "components-guide-8", "button")
    assert t.prev == "components-guide-8/checkbox"
    assert t.next == "components-guide-8/slider"


# ------------------------------------------------------------- structure


def test_every_named_heading_has_an_anchor():
    """Anchors are what make section-level citations possible."""
    t = _topic("button.html", "components-guide-8", "button")
    named = [s for s in t.sections if s.heading]
    assert named
    assert all(s.anchor for s in named), [s.heading for s in named if not s.anchor]


def test_heading_paths_are_hierarchical():
    t = _topic("button.html", "components-guide-8", "button")
    paths = [s.heading_path for s in t.sections if s.heading]
    assert "Button > Overview" in paths


def test_code_sample_keeps_language_and_anchor():
    t = _topic("button.html", "components-guide-8", "button")
    assert t.code_samples
    cs = t.code_samples[0]
    assert cs.lang == "CSS"
    assert cs.anchor, "code sample should be attributed to its section"


def test_bare_tail_text_is_not_dropped():
    """Stub topics carry their whole body as the .tail of a preceding node.
    Iterating only child elements silently reported them as empty."""
    t = _topic("troubleshootings.html", "how-to-articles-8", "troubleshootings")
    assert t.word_count > 0
    assert "troubleshooting" in t.body_md.lower()


# ------------------------------------------------------------- sanitising


def test_clean_text_normalises_nbsp_and_cr():
    assert clean_text("a b") == "a b"
    assert clean_text("x\r\ny") == "x\ny"


def test_concealment_characters_are_stripped():
    assert clean_text("safe​text") == "safetext"
    assert clean_text("tag\U000e0041payload") == "tagpayload"


# ------------------------------------------------------------- link mapping


@pytest.mark.parametrize(
    "href,expect",
    [
        ("/articles/components-guide-8/button", ("components-guide-8", "button", True)),
        ("/articles/#!ai-hub/overview", ("ai-hub", "overview", True)),
        ("/articles/components-guide-8/button/a/h2_1", ("components-guide-8", "button", True)),
        ("/smart/project-x/topic-y", ("project-x", "topic-y", False)),
        ("javascript:void(0)", (None, None, False)),
        ("mailto:a@b.c", (None, None, False)),
    ],
)
def test_map_link(href, expect):
    assert map_link(href, PUBS) == expect
