"""Stage 2 — extract (plan §6.2).

ClickHelp article pages are a flat sequence of body children: a `div.sidebar`
of navigation furniture, then h2/h3 headings interleaved with p/ol/ul/table,
then a `footer` carrying prev/next. Headings carry their anchor id directly
(`<h3 id="h3_1689083776">`), which is what makes section-level deep-link
citations possible.

Two rules this module exists to enforce:

1. **Sidebar navigation is separated, not discarded.** `div.sidebar` and
   `footer` are excluded from prose — otherwise the same nav text is indexed
   on all 3,117 pages and pollutes both BM25 and the embeddings — but they are
   captured as structured `mini_toc` / `prev` / `next` fields.

2. **Inline elements are wrapped before descent.** Rendering an `<a>`/`<b>`/
   `<img>` by walking its *children* silently drops the element's own markup,
   which loses every cross-reference link in the corpus. `_inline_of()` wraps
   the element in a holder first. `tests/test_extract.py` pins this.

    python -m neutrinos_mcp.ingest.extract
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import unicodedata
from dataclasses import asdict, dataclass, field
from pathlib import Path

from lxml import html as LH

from ..config import ROOT, settings

# ---------------------------------------------------------------- sanitising

# §9.1.2 — Unicode TAG block (E0000-E007F) is a documented payload-concealment
# vector in MCP tooling; zero-width chars hide text from a human reviewer while
# remaining visible to the model. Strip both at the source.
_INVISIBLE = re.compile(
    "[​-‏‪-‮⁠-⁤﻿]|[\U000e0000-\U000e007f]"
)
_WS = re.compile(r"[ \t   ]+")


def clean_text(s: str) -> str:
    if not s:
        return ""
    s = unicodedata.normalize("NFC", s)
    s = _INVISIBLE.sub("", s)
    s = s.replace(chr(160), chr(32)).replace(chr(13)+chr(10), chr(10)).replace(chr(13), chr(10))
    return _WS.sub(" ", s)


# ---------------------------------------------------------------- data model


@dataclass
class Section:
    heading: str
    level: int
    anchor: str | None
    heading_path: str
    md: str
    has_code: bool = False


@dataclass
class Link:
    href: str
    text: str
    target_pub: str | None
    target_slug: str | None
    resolved: bool


@dataclass
class CodeSample:
    lang: str | None
    code: str
    anchor: str | None


@dataclass
class Topic:
    pub: str
    slug: str
    title: str
    url: str
    lastmod: str | None
    breadcrumb: str = ""
    body_md: str = ""
    word_count: int = 0
    content_hash: str = ""
    sections: list[Section] = field(default_factory=list)
    code_samples: list[CodeSample] = field(default_factory=list)
    links: list[Link] = field(default_factory=list)
    mini_toc: list[str] = field(default_factory=list)
    see_also: list[Link] = field(default_factory=list)
    prev: str | None = None
    next: str | None = None


# ---------------------------------------------------------------- inline pass

_INLINE_SKIP = {"script", "style"}


def _inline(el, out: list[str], skip: tuple[str, ...] = ()) -> None:
    """Render an element's CHILDREN. Never call this on the element you want rendered.

    `skip` suppresses descent into given tags WITHOUT removing them from the
    tree. Detaching nodes to control rendering is how the /smart/ cross-links in
    nested <ol> vanished from link harvesting: the DOM is read more than once,
    so no pass may mutate it.
    """
    if el.text:
        out.append(clean_text(el.text))
    for ch in el:
        if not isinstance(ch.tag, str):
            if ch.tail:
                out.append(clean_text(ch.tail))
            continue
        if ch.tag.lower() not in skip:
            _inline_node(ch, out, skip)
        if ch.tail:
            out.append(clean_text(ch.tail))


def _inline_node(el, out: list[str], skip: tuple[str, ...] = ()) -> None:
    """Render an element INCLUDING its own markup.

    This wrapper is the whole point: `_inline` walks children, so calling it
    directly on an <a> emits the link text and drops the link.
    """
    tag = el.tag.lower()
    if tag in _INLINE_SKIP:
        return
    if tag == "br":
        out.append("\n")
        return
    if tag == "img":
        src = (el.get("src") or "").strip()
        alt = clean_text(el.get("alt") or "").strip()
        if src:
            out.append(f"![{alt}]({src})")
        return

    inner: list[str] = []
    _inline(el, inner, skip)
    text = "".join(inner)

    if tag == "a":
        href = (el.get("href") or "").strip()
        label = text.strip() or clean_text(el.text_content()).strip()
        if href and not href.startswith("javascript:") and label:
            out.append(f"[{label}]({href})")
        else:
            out.append(text)
    elif tag in ("b", "strong"):
        out.append(f"**{text}**" if text.strip() else text)
    elif tag in ("i", "em"):
        out.append(f"*{text}*" if text.strip() else text)
    elif tag in ("code", "tt", "kbd"):
        out.append(f"`{text}`" if text.strip() else text)
    else:
        out.append(text)


def inline_md(el, skip: tuple[str, ...] = ()) -> str:
    out: list[str] = []
    _inline(el, out, skip)
    return re.sub(r"[ \t]+\n", "\n", "".join(out)).strip()


# ---------------------------------------------------------------- block pass


def _is_code_table(el) -> bool:
    return "CHCodeSample" in (el.get("class") or "")


def _code_from_table(el) -> CodeSample:
    lang_el = el.xpath('.//*[contains(@class,"CHCodeSample_langName")]')
    code_el = el.xpath('.//*[contains(@class,"CHCodeSample_code")]')
    lang = clean_text(lang_el[0].text_content()).strip() if lang_el else None
    node = code_el[0] if code_el else el
    # <pre> inside preserves newlines; text_content() on the cell flattens them,
    # so prefer the pre when present.
    pre = node.xpath(".//pre")
    raw = (pre[0] if pre else node).text_content()
    code = unicodedata.normalize("NFC", _INVISIBLE.sub("", raw)).replace(" ", " ")
    return CodeSample(lang=lang or None, code=code.strip("\n"), anchor=None)


def _list_md(el, depth: int = 0) -> str:
    ordered = el.tag.lower() == "ol"
    lines: list[str] = []
    n = 1
    for li in el.findall("li"):
        # Read-only: find nested lists to recurse into, but never detach them.
        sub = [c for c in li if isinstance(c.tag, str) and c.tag.lower() in ("ul", "ol")]
        body = inline_md(li, skip=("ul", "ol"))
        marker = f"{n}." if ordered else "-"
        pad = "  " * depth
        first, *rest = (body or "").split("\n")
        lines.append(f"{pad}{marker} {first}".rstrip())
        lines += [f"{pad}   {r}".rstrip() for r in rest if r.strip()]
        for s in sub:
            lines.append(_list_md(s, depth + 1))
        n += 1
    return "\n".join(x for x in lines if x.strip())


def _table_md(el) -> str:
    rows = []
    for tr in el.xpath(".//tr"):
        cells = [inline_md(td).replace("\n", " ").replace("|", "\\|")
                 for td in tr.xpath("./th|./td")]
        if cells:
            rows.append(cells)
    if not rows:
        return ""
    width = max(len(r) for r in rows)
    rows = [r + [""] * (width - len(r)) for r in rows]
    head, *body = rows
    out = ["| " + " | ".join(head) + " |",
           "|" + "|".join([" --- "] * width) + "|"]
    out += ["| " + " | ".join(r) + " |" for r in body]
    return "\n".join(out)


def _block_md(el) -> tuple[str, CodeSample | None]:
    tag = el.tag.lower()
    if tag == "table":
        if _is_code_table(el):
            cs = _code_from_table(el)
            fence = f"```{cs.lang.lower()}" if cs.lang else "```"
            return f"{fence}\n{cs.code}\n```", cs
        return _table_md(el), None
    if tag in ("ul", "ol"):
        return _list_md(el), None
    if tag == "pre":
        return f"```\n{el.text_content().strip()}\n```", CodeSample(None, el.text_content().strip(), None)
    if tag == "blockquote":
        inner = inline_md(el)
        return "\n".join(f"> {l}" for l in inner.split("\n")), None
    if tag == "hr":
        return "---", None
    return inline_md(el), None


# ---------------------------------------------------------------- link mapping

_ART = re.compile(r"^/articles?/(?:#!)?(?P<pub>[^/#?]+)/(?P<slug>[^/#?]+)")
_SMART = re.compile(r"^/smart/(?P<pub>[^/#?]+)/(?P<slug>[^/#?]+)")


def map_link(href: str, known_pubs: set[str]) -> tuple[str | None, str | None, bool]:
    """href -> (publication, slug, resolved). Unresolved targets are kept, not dropped."""
    if not href or href.startswith(("javascript:", "mailto:", "#")):
        return None, None, False
    h = href
    for pre in ("https://documentation.neutrinos.com", "http://documentation.neutrinos.com"):
        if h.startswith(pre):
            h = h[len(pre):]
    if not h.startswith("/"):
        return None, None, False
    if "/a/" in h:  # section anchor on a topic page
        h = h.split("/a/")[0]
    m = _ART.match(h) or _SMART.match(h)
    if not m:
        return None, None, False
    pub, slug = m.group("pub"), m.group("slug")
    return pub, slug, pub in known_pubs


# ---------------------------------------------------------------- topic parse

# Class-based furniture. NOTE `footer`: ClickHelp emits <div class="footer">,
# not <footer>, so a tag-only check leaks its copyright/feedback boilerplate
# into the prose of every page that has one (measured: 1,077 of 3,117).
_SKIP_CLASS = ("sidebar", "CHSeeAlso", "CHMiniToc", "nonPrintable",
               "footer", "CHBreadcrumb", "headerBreadcumb")


def parse_topic(raw_html: bytes, pub: str, slug: str, url: str,
                lastmod: str | None, known_pubs: set[str]) -> Topic:
    doc = LH.fromstring(raw_html)
    body = doc.xpath("//body")
    root = body[0] if body else doc

    t = Topic(pub=pub, slug=slug, title="", url=url, lastmod=lastmod)

    # --- furniture, captured then excluded -------------------------------
    for el in root.xpath('.//*[contains(@class,"CHMiniToc_heading2") or contains(@class,"CHMiniToc_heading3")]'):
        txt = clean_text(el.text_content()).strip()
        if txt:
            t.mini_toc.append(txt)
    for a in root.xpath('.//*[contains(@class,"CHSeeAlso")]//a'):
        p, s, ok = map_link(a.get("href") or "", known_pubs)
        if p:
            t.see_also.append(Link(a.get("href") or "", clean_text(a.text_content()).strip(), p, s, ok))
    bc = root.xpath('.//*[contains(@class,"CHBreadcrumb")]')
    if bc:
        t.breadcrumb = clean_text(bc[0].text_content()).strip()

    for cls, attr in (("CHNavLinkPrevious", "prev"), ("CHNavLinkNext", "next")):
        el = root.xpath(f'.//a[contains(@class,"{cls}")]')
        if el:
            p, s, ok = map_link(el[0].get("href") or "", known_pubs)
            if p and s:
                setattr(t, attr, f"{p}/{s}")

    drop = set()
    for el in root.xpath(".//div|.//footer|.//script|.//style|.//nav"):
        cls = el.get("class") or ""
        if el.tag in ("script", "style", "footer", "nav") or any(k in cls for k in _SKIP_CLASS):
            drop.add(el)

    # --- prose walk -------------------------------------------------------
    sections: list[Section] = []
    cur: Section | None = None
    stack: dict[int, str] = {}
    parts: list[str] = []

    def flush() -> None:
        nonlocal cur
        if cur is not None:
            cur.md = "\n\n".join(x for x in cur.md.split("\n\n") if x.strip()).strip()
            sections.append(cur)
            cur = None

    def emit_text(txt: str | None) -> None:
        """Bare text directly under <body>.

        Some stub topics have no heading and no block element at all — their
        entire prose is the `.tail` of a preceding node (often the sidebar).
        Iterating only child *elements* silently drops those pages to empty.
        Tails are collected even after skipped elements, because the sidebar's
        tail is exactly where that prose sits.
        """
        nonlocal cur
        t2 = clean_text(txt or "").strip()
        if not t2:
            return
        parts.append(t2)
        if cur is None:
            cur = Section(heading="", level=2, anchor=None, heading_path="", md="")
        cur.md = (cur.md + "\n\n" + t2).strip()

    emit_text(root.text)

    for el in root.iterchildren():
        if not isinstance(el.tag, str):
            continue
        tag = el.tag.lower()
        cls = el.get("class") or ""
        skipped = (
            el in drop
            or tag in ("script", "style", "footer", "nav")
            or any(k in cls for k in _SKIP_CLASS)
        )
        if skipped:
            emit_text(el.tail)
            continue

        if tag in ("h1", "h2", "h3", "h4", "h5", "h6"):
            flush()
            lvl = int(tag[1])
            heading = clean_text(el.text_content()).strip()
            stack[lvl] = heading
            for deeper in [k for k in stack if k > lvl]:
                stack.pop(deeper, None)
            path = " > ".join(stack[k] for k in sorted(stack))
            cur = Section(heading=heading, level=lvl, anchor=el.get("id") or None,
                          heading_path=path, md="")
            if not t.title:
                t.title = heading
            parts.append(("#" * min(lvl, 6)) + " " + heading)
            emit_text(el.tail)
            continue

        md, cs = _block_md(el)
        if cs and cs.code.strip():
            cs.anchor = cur.anchor if cur else None
            t.code_samples.append(cs)
        if md.strip():
            parts.append(md)
            if cur is None:
                cur = Section(heading="", level=2, anchor=None, heading_path="", md="")
            cur.md = (cur.md + "\n\n" + md).strip()
            if cs:
                cur.has_code = True

        for a in el.xpath(".//a"):
            lp, ls, ok = map_link(a.get("href") or "", known_pubs)
            if lp and ls:
                t.links.append(Link(a.get("href") or "", clean_text(a.text_content()).strip(), lp, ls, ok))

        emit_text(el.tail)
    flush()

    if not t.title:
        title_el = doc.xpath("//title/text()")
        t.title = clean_text(title_el[0]).strip() if title_el else slug.replace("-", " ").title()

    t.sections = sections
    t.body_md = "\n\n".join(parts).strip()
    t.word_count = len(t.body_md.split())
    t.content_hash = hashlib.sha256(t.body_md.encode("utf-8")).hexdigest()
    if not t.breadcrumb:
        t.breadcrumb = t.title
    return t


# ---------------------------------------------------------------- driver


def run(limit: int | None = None, write_docs: bool = True) -> dict:
    cfg = settings()
    manifest = json.loads((ROOT / "data" / "topics_manifest.json").read_text(encoding="utf-8"))
    if limit:
        manifest = manifest[:limit]
    known_pubs = {m["pub"] for m in manifest}

    out_path = ROOT / "data" / "topics.jsonl"
    docs_dir = ROOT / "docs"
    stats = {"topics": 0, "sections": 0, "code_samples": 0, "links": 0,
             "unresolved_links": 0, "empty_body": 0, "no_anchor_sections": 0, "words": 0}

    with out_path.open("w", encoding="utf-8") as fh:
        for i, m in enumerate(manifest, 1):
            raw = (ROOT / m["raw"]).read_bytes()
            t = parse_topic(raw, m["pub"], m["slug"], m["url"], m.get("lastmod"), known_pubs)
            stats["topics"] += 1
            stats["sections"] += len(t.sections)
            stats["code_samples"] += len(t.code_samples)
            stats["links"] += len(t.links)
            stats["unresolved_links"] += sum(1 for l in t.links if not l.resolved)
            stats["no_anchor_sections"] += sum(1 for s in t.sections if not s.anchor)
            stats["words"] += t.word_count
            if not t.body_md.strip():
                stats["empty_body"] += 1
            fh.write(json.dumps(asdict(t), ensure_ascii=False) + "\n")

            if write_docs:
                p = docs_dir / m["pub"] / f"{m['slug']}.md"
                p.parent.mkdir(parents=True, exist_ok=True)
                p.write_text(f"# {t.title}\n\n<{t.url}>\n\n{t.body_md}\n", encoding="utf-8")
            if i % 500 == 0:
                print(f"  extracted {i}/{len(manifest)}")

    (ROOT / "data" / "extract_report.json").write_text(json.dumps(stats, indent=2), encoding="utf-8")
    return stats


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--limit", type=int, default=None)
    ap.add_argument("--no-docs", action="store_true")
    args = ap.parse_args()
    s = run(limit=args.limit, write_docs=not args.no_docs)
    print(json.dumps(s, indent=2))


if __name__ == "__main__":
    main()
