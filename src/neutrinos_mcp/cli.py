"""Terminal adapter (plan §4.2).

Same contract as the MCP server, different formatting. `--json` on any command
emits the exact envelope the MCP tool would return, which is what makes the
evaluation harness and the agent path provably identical.

Windows consoles default to cp1252 and this corpus contains curly quotes and
em dashes, so stdout/stderr are reconfigured to UTF-8 on import.
"""

from __future__ import annotations

import argparse
import json
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

from .errors import KBError
from .kb import KnowledgeBase
from .tools.handlers import dispatch

DIM, BOLD, RESET = "\033[2m", "\033[1m", "\033[0m"


def _hr(s: str) -> str:
    return f"{DIM}{'─' * 76}{RESET}\n{BOLD}{s}{RESET}"


def render_search(p: dict) -> str:
    out = [_hr(f"{len(p['results'])} passages  ·  confidence {p['confidence']}"
               f"  ·  {'SUFFICIENT' if p['sufficient_evidence'] else 'WEAK EVIDENCE'}")]
    sc = p.get("scope_applied", {})
    out.append(f"{DIM}scope: products={sc.get('products') or 'all'} "
               f"versions={sc.get('versions') or 'current'} "
               f"({sc.get('inferred_from')}){RESET}")
    if p.get("version_ambiguous"):
        out.append(f"{BOLD}! version ambiguous — ask the user which version{RESET}")
    for i, h in enumerate(p["results"], 1):
        stale = "" if h["staleness"] == "fresh" else f"  [{h['staleness']}]"
        also = f"  also in v{','.join(h['also_in_versions'])}" if h.get("also_in_versions") else ""
        out.append(f"\n{BOLD}{i}. {h['title']} — {h['heading_path']}{RESET}")
        out.append(f"   {DIM}{h['product']} {h.get('version') or ''}"
                   f"  score={h['score']}  via {'+'.join(h.get('retrieved_by', []))}"
                   f"{stale}{also}{RESET}")
        out.append(f"   {h['ref']}")
        body = h["text"].strip().replace("\n", "\n   ")
        out.append("   " + body[:600] + ("…" if len(body) > 600 else ""))
    if p.get("notice"):
        out.append(f"\n{DIM}note: {p['notice']}{RESET}")
    return "\n".join(out)


def render_products(p: dict) -> str:
    out = [_hr(f"{len(p['products'])} products  ·  {p['total_topics']} topics  "
               f"·  built {p['index_built_at']}")]
    for prod in p["products"]:
        alias = f"  {DIM}(aka {', '.join(prod['aliases'])}){RESET}" if prod.get("aliases") else ""
        out.append(f"\n{BOLD}{prod['product']}{RESET}{alias}")
        for v in prod["versions"]:
            mark = "*" if v["is_current"] else " "
            out.append(f"  {mark} v{v['version'] or '-':<6} {v['publication']:<44} "
                       f"{v['topic_count']:>4} topics  {v['staleness']}")
    return "\n".join(out)


def render_related(p: dict) -> str:
    out = [_hr(f"related to {p['ref']}")]
    for rel, items in p["relations"].items():
        if not items:
            continue
        out.append(f"\n{BOLD}{rel}{RESET}")
        for it in items:
            cur = "" if it.get("is_current", True) else f" {DIM}(superseded){RESET}"
            out.append(f"  {it['ref']:<58} {it['title'][:34]}{cur}")
    if p.get("unresolved_links"):
        out.append(f"\n{DIM}unresolved upstream links: "
                   f"{', '.join(u['target'] for u in p['unresolved_links'][:6])}{RESET}")
    return "\n".join(out)


def render_compare(p: dict) -> str:
    out = [_hr(f"{p['slug']} across {p['product']} — verdict: {BOLD}{p['verdict']}{RESET}")]
    if p.get("rename_note"):
        out.append(f"{DIM}{p['rename_note']}{RESET}")
    for v in p["versions"]:
        cur = " *" if v["is_current"] else "  "
        out.append(f"\n{cur}v{v['version']:<4} sim={v['similarity_to_newest']:<6} "
                   f"{v['ref']}")
        for label, key in (("+", "sections_added"), ("-", "sections_removed"),
                           ("~", "sections_changed")):
            if v.get(key):
                out.append(f"      {label} {', '.join(v[key][:4])}"
                           + (" …" if len(v[key]) > 4 else ""))
    return "\n".join(out)


def render_fetch(p: dict) -> str:
    out = [_hr(f"{p['title']}  ({p['product']} {p.get('version') or ''}, {p['staleness']})")]
    out.append(f"{DIM}{p['url']}{RESET}\n")
    out.append(p["content"])
    if p.get("truncated"):
        out.append(f"\n{DIM}truncated — continue_from={p.get('continue_from')}{RESET}")
    return "\n".join(out)


RENDER = {"search": render_search, "products": render_products,
          "related": render_related, "compare": render_compare, "fetch": render_fetch}
TOOL = {"search": "search_docs", "products": "list_products", "related": "list_related",
        "compare": "compare_versions", "fetch": "fetch_document"}


def main() -> None:
    ap = argparse.ArgumentParser(prog="neutrinos-cli", description=__doc__)
    ap.add_argument("--json", action="store_true", help="emit the raw MCP envelope")
    sub = ap.add_subparsers(dest="cmd", required=True)

    s = sub.add_parser("search")
    s.add_argument("query")
    s.add_argument("--product"); s.add_argument("--version")
    s.add_argument("--top-k", type=int, default=6)
    s.add_argument("--include-superseded", action="store_true")
    s.add_argument("--detailed", action="store_true")

    f = sub.add_parser("fetch"); f.add_argument("ref")
    f.add_argument("--section"); f.add_argument("--max-tokens", type=int, default=4000)

    r = sub.add_parser("related"); r.add_argument("ref")

    c = sub.add_parser("compare"); c.add_argument("slug")
    c.add_argument("--product")

    p = sub.add_parser("products"); p.add_argument("--contains")

    sub.add_parser("stats")

    a = ap.parse_args()
    try:
        kb = KnowledgeBase()
        if a.cmd == "stats":
            print(json.dumps(kb.stats(), indent=2))
            return
        args = {
            "search": lambda: {"query": a.query, "product": a.product, "version": a.version,
                               "top_k": a.top_k, "include_superseded": a.include_superseded,
                               "response_format": "detailed" if a.detailed else "concise"},
            "fetch": lambda: {"ref": a.ref, "section": a.section, "max_tokens": a.max_tokens},
            "related": lambda: {"ref": a.ref},
            "compare": lambda: {"slug": a.slug, "product": a.product},
            "products": lambda: {"name_contains": a.contains},
        }[a.cmd]()
        args = {k: v for k, v in args.items() if v is not None}
        payload = dispatch(kb, TOOL[a.cmd], args)
        clean = {k: v for k, v in payload.items() if not k.startswith("_")}
        print(json.dumps(clean, indent=2, ensure_ascii=False) if a.json
              else RENDER[a.cmd](payload))
    except KBError as exc:
        print(json.dumps(exc.to_dict(), indent=2), file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
