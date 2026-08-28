"""Tool handlers: arguments in, schema-valid envelope out (plan §8).

No SQL here — everything goes through `KnowledgeBase`. Each handler is
responsible for three things the schemas alone cannot enforce:

  * token budgets, applied server-side with a truncation notice that tells the
    agent how to narrow rather than leaving it to guess (§8.1)
  * the untrusted-content boundary on every passage (§9.1)
  * turning a `KBError` into an isError payload, never a transport error (§8.4)
"""

from __future__ import annotations

from datetime import datetime, timezone
from typing import Any, Callable

from ..config import settings
from ..errors import KBError, invalid
from ..kb import KnowledgeBase, parse_ref
from ..sanitize import clean_passage
from .schemas import TOOLS_BY_NAME

# ------------------------------------------------------------------ budgeting


def est_tokens(text: str) -> int:
    """Cheap character-based estimate; exact counting is not worth a tokenizer
    load on the serve path, and the cap only needs to be approximately right."""
    return max(1, int(len(text) / 3.6))


def _rfc3339(ts: str) -> str:
    """Coerce a manifest timestamp into RFC 3339 for `list_products.index_built_at`.

    RFC 3339 requires a time-offset ("Z" or +HH:MM); Python's own
    `datetime.fromisoformat` does not, so a bare local-time string parses fine
    here and still fails a strict client-side validator (confirmed: this was
    accepted internally but rejected by Claude Desktop's MCP client).
    `ingest.index` writes a correct value going forward, but this also has to
    cover every index built before that fix without requiring a rebuild —
    an already-shipped manifest is exactly the kind of stored value this
    handler cannot assume matches the current code's expectations. The
    original offset cannot be recovered after the fact, so a bare value is
    treated as UTC rather than left invalid.
    """
    if not ts:
        return ts
    try:
        dt = datetime.fromisoformat(ts)
    except ValueError:
        return ts
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    return dt.isoformat()


def _trim_passage(text: str, max_tokens: int) -> tuple[str, bool]:
    if est_tokens(text) <= max_tokens:
        return text, False
    keep = int(max_tokens * 3.6)
    cut = text[:keep]
    nl = cut.rfind("\n\n")
    return (cut[:nl] if nl > keep * 0.5 else cut).rstrip() + "\n…", True


def _hit_payload(h: dict, detailed: bool, per_passage_tokens: int) -> dict:
    text, flags = clean_passage(h["text"])
    text, truncated = _trim_passage(text, per_passage_tokens if not detailed
                                    else per_passage_tokens * 4)
    out = {
        "ref": h["ref"], "url": h["url"], "title": h["title"],
        "heading_path": h["heading_path"], "product": h["product"],
        "version": h.get("version"), "is_current": h["is_current"],
        "last_updated": h.get("last_updated"), "staleness": h["staleness"],
        "score": h["score"], "retrieved_by": h.get("retrieved_by", []),
        "text": text,
    }
    if h.get("also_in_versions"):
        out["also_in_versions"] = h["also_in_versions"]
    if flags:
        # Surfaced, not silently scrubbed: the operator needs to see it.
        out["_content_warning"] = flags
    if truncated:
        out["_truncated"] = True
    return out


# ------------------------------------------------------------------- handlers


def search_docs(kb: KnowledgeBase, args: dict) -> dict:
    cfg = settings()
    fmt = args.get("response_format", "concise")
    top_k = int(args.get("top_k", cfg["retrieval.default_top_k"]))
    res = kb.search(
        query=args["query"],
        product=args.get("product"),
        version=args.get("version"),
        include_superseded=bool(args.get("include_superseded", False)),
        top_k=top_k,
    )
    per_passage = 400 if fmt == "concise" else 1600
    hits = [_hit_payload(h, fmt == "detailed", per_passage) for h in res.hits]

    out: dict[str, Any] = {
        "results": hits,
        "scope_applied": res.scope.as_dict() if res.scope else {},
        "confidence": res.confidence,
        "sufficient_evidence": res.sufficient_evidence,
    }
    if res.match_expression:
        out["match_expression"] = res.match_expression
    if res.version_ambiguous:
        out["version_ambiguous"] = True
    notices = []
    if not res.hits:
        notices.append(
            "No passages matched. Try fewer or more specific terms, or call "
            "list_products and pass `product` explicitly.")
    if not res.sufficient_evidence and res.hits:
        notices.append(
            "Evidence is weak. Say the documentation does not clearly cover this "
            "rather than composing an answer from these passages.")
    if res.version_ambiguous:
        notices.append(
            "Strong matches exist in more than one product version and the user "
            "named none. Ask which version they are on before answering.")
    if any(h.get("_truncated") for h in hits) and fmt == "concise":
        notices.append("Passages were trimmed. Use fetch_document for the full section.")
    if notices:
        out["notice"] = " ".join(notices)
        out["truncated"] = any(h.get("_truncated") for h in hits)
    return out


def _evidence_item(h: dict, text: str) -> dict:
    """One `common.json#/$defs/hit` entry for `answer_pack`. Deliberately not
    `_hit_payload` (used by `search_docs`): that one adds `_content_warning`/
    `_truncated`, which are fine under `search_docs`'s own looser output
    schema but are not declared fields on the shared `hit` $def, so including
    them here would fail `answer_pack`'s `additionalProperties: false`
    validation (`server.validate_output`)."""
    out = {
        "ref": h["ref"], "url": h["url"], "title": h["title"],
        "heading_path": h["heading_path"], "product": h["product"],
        "version": h.get("version"), "is_current": h["is_current"],
        "last_updated": h.get("last_updated"), "staleness": h["staleness"],
        "score": h["score"], "text": text,
    }
    if h.get("retrieved_by"):
        out["retrieved_by"] = h["retrieved_by"]
    if h.get("also_in_versions"):
        out["also_in_versions"] = h["also_in_versions"]
    return out


def answer_pack(kb: KnowledgeBase, args: dict) -> dict:
    """Phase 5 (plan §8.2 #6, §8.5.7). One call assembling a citation-ready,
    token-budgeted evidence bundle plus a binding `recommended_action`, for a
    caller that composes one reply per question rather than chaining
    `search_docs` -> `fetch_document` -> `list_related` itself.

    Built once a real downstream consumer existed to earn it against (a
    Discourse-question-answering bot, whose own retrieval design already
    treats `recommended_action` as binding) — the plan's own gating
    condition ("only if transcript analysis shows the Responder making
    repetitive search_docs -> fetch_document -> list_related sequences") is
    satisfied by that consumer's architecture directly, not by transcript
    mining after the fact.

    Reuses `kb.search()` exactly like `search_docs` — same scope resolution,
    same hybrid retrieval + rerank + confidence gate — so the two tools never
    disagree about what counts as good evidence for the same question. This
    handler's own job is strictly the parts `search_docs` does not do:
    token-budgeted selection (vs. a fixed `top_k`), a deduplicated citation
    table, and the `recommended_action`/`caveat`/`coverage_notes` decision.
    """
    cfg = settings()
    token_budget = int(args.get("token_budget", 6000))
    res = kb.search(
        query=args["question"],
        product=args.get("product"),
        version=args.get("version"),
        include_superseded=False,
        top_k=cfg["retrieval.max_top_k"],
    )

    evidence: list[dict] = []
    citations: dict[str, dict] = {}  # keyed by url; insertion order == rank order
    used = 0
    for h in res.hits:
        text, _flags = clean_passage(h["text"])
        text, _truncated = _trim_passage(text, 500)
        t = est_tokens(text)
        if evidence and used + t > token_budget:
            break
        used += t
        evidence.append(_evidence_item(h, text))
        citations.setdefault(h["url"], {"ref": h["ref"], "url": h["url"], "title": h["title"]})

    if not res.hits or not res.sufficient_evidence:
        action = "escalate"
    elif res.version_ambiguous:
        action = "ask_for_version"
    else:
        action = "answer"

    caveat = None
    if action == "answer" and evidence and evidence[0]["staleness"] == "stale":
        action = "answer_with_caveat"
        caveat = ("This information may be out of date — the top matching page has not "
                  "been updated recently.")

    coverage_notes: list[str] = []
    if action == "ask_for_version":
        coverage_notes.append(
            "Strong matches exist in more than one product version; ask which version "
            "the user is on rather than guessing.")
    elif action == "escalate":
        coverage_notes.append(
            "No passages matched this question in the indexed documentation."
            if not res.hits else
            "Evidence relevance is below the confidence threshold for a direct answer.")

    scope_dict = (res.scope.as_dict() if res.scope else
                  {"products": [], "versions": [], "include_superseded": False, "inferred": True})

    return {
        "recommended_action": action,
        "caveat": caveat,
        "evidence": evidence,
        "citations": list(citations.values()),
        "coverage_notes": coverage_notes,
        "confidence": res.confidence,
        "scope_applied": scope_dict,
        "tokens_used": used,
    }


def fetch_document(kb: KnowledgeBase, args: dict) -> dict:
    cfg = settings()
    pub, slug, anchor = parse_ref(args["ref"])
    section = args.get("section") or anchor
    max_tokens = min(int(args.get("max_tokens", cfg["budgets.fetch_default"])),
                     cfg["budgets.fetch_max"])

    row = kb.topic_row(pub, slug)
    (tid, _pub, _slug, title, breadcrumb, url, lastmod,
     _wc, body_md, product, version, is_current) = row

    sections = kb.sections_of(tid)
    if section:
        match = [s for s in sections
                 if s["anchor"] == section or s["heading_path"] == section]
        if not match:
            raise KBError(
                "section-not-found", "Section Not Found", 404,
                f"No section '{section}' in {pub}/{slug}.",
                [{"value": s["anchor"] or s["heading_path"],
                  "label": s["heading_path"], "field": "section"}
                 for s in sections[:8]])
        chosen = match
    else:
        chosen = sections

    parts, included, used, cont = [], set(), 0, None
    for s in chosen:
        t = est_tokens(s["text"])
        if used and used + t > max_tokens:
            cont = s["anchor"] or s["heading_path"]
            break
        parts.append(s["text"])
        included.add(s["ordinal"])
        used += t

    content = "\n\n".join(parts) if parts else body_md
    content, flags = clean_passage(content)
    content, hard_trunc = _trim_passage(content, max_tokens)

    from ..retrieval.pipeline import _staleness

    out: dict[str, Any] = {
        "ref": f"{pub}/{slug}" + (f"#{anchor}" if anchor else ""),
        "url": url, "title": title, "breadcrumb": breadcrumb,
        "product": product, "version": version, "is_current": bool(is_current),
        "last_updated": lastmod,
        "staleness": _staleness(lastmod, cfg["staleness.fresh_months"],
                                cfg["staleness.aging_months"]),
        "content": content,
        "sections": [{"anchor": s["anchor"], "heading_path": s["heading_path"],
                      "token_count": s["token_count"],
                      "included": s["ordinal"] in included} for s in sections],
        "truncated": bool(cont) or hard_trunc,
        "continue_from": cont,
    }
    if args.get("include_code_samples", True):
        out["code_samples"] = kb.code_samples_of(tid)
    ov = kb.other_versions_of(pub, slug)
    if ov:
        out["also_in_versions"] = ov
    if flags:
        out["_content_warning"] = flags
    return out


def list_related(kb: KnowledgeBase, args: dict) -> dict:
    pub, slug, _ = parse_ref(args["ref"])
    lpr = int(args.get("limit_per_relation", 10))
    data = kb.related(pub, slug, lpr)
    wanted = args.get("relations")
    rels = data["relations"]
    if wanted:
        allowed = set(wanted)
        rels = {k: v for k, v in rels.items() if k in allowed}
    out = {"ref": f"{pub}/{slug}", "relations": rels}
    if data["unresolved_links"]:
        out["unresolved_links"] = data["unresolved_links"][:lpr]
    return out


def compare_versions(kb: KnowledgeBase, args: dict) -> dict:
    slug = args["slug"]
    data = kb.compare_versions(slug, args.get("product"), args.get("versions"))
    rows = data["rows"]
    newest = rows[-1]
    newest_hashes = kb.section_hashes(newest[0], newest[1])

    def hamming(a: int, b: int) -> int:
        return ((a ^ b) & ((1 << 64) - 1)).bit_count()

    versions, sims = [], []
    for (rpub, rslug, title, url, lastmod, chash,
         product, version, is_current, _fam, _rank) in rows:
        h = kb.section_hashes(rpub, rslug)
        added = sorted(set(h) - set(newest_hashes))
        removed = sorted(set(newest_hashes) - set(h))
        changed = sorted(k for k in (set(h) & set(newest_hashes))
                         if hamming(h[k], newest_hashes[k]) > 3)
        total = max(len(set(h) | set(newest_hashes)), 1)
        sim = 1.0 - (len(added) + len(removed) + len(changed)) / total
        sims.append(sim)
        entry = {
            "version": version or "-", "publication": rpub,
            "ref": f"{rpub}/{rslug}", "url": url, "present": True,
            "is_current": bool(is_current), "last_updated": lastmod,
            "similarity_to_newest": round(sim, 3),
            "sections_added": added, "sections_removed": removed,
            "sections_changed": changed,
        }
        if args.get("include_text"):
            entry["text"] = kb.topic_row(rpub, rslug)[8]
        versions.append(entry)

    others = [s for s in sims[:-1]] or [1.0]
    worst = min(others)
    verdict = ("identical" if worst >= 0.999 else
               "minor_wording" if worst >= 0.9 else "substantive_change")
    if len(versions) == 1:
        verdict = "identical"

    pubs = {v["publication"] for v in versions}
    prods = {kb.reg.get(p).product for p in pubs}
    names = {kb.reg.get(p).title.rsplit(" ", 1)[0] for p in pubs}
    out = {
        "slug": slug, "product": sorted(prods)[0],
        "verdict": verdict, "versions": versions,
    }
    if len(names) > 1:
        out["rename_note"] = (
            f"This family spans a product rename: {', '.join(sorted(names))}. "
            f"Versions are matched by family and slug, not by name.")
    return out


def list_products(kb: KnowledgeBase, args: dict) -> dict:
    from ..retrieval.pipeline import _staleness

    cfg = settings()
    prods = kb.products(bool(args.get("include_archived", False)),
                        args.get("name_contains"))
    for p in prods:
        for v in p["versions"]:
            v["staleness"] = _staleness(v.get("newest_lastmod"),
                                        cfg["staleness.fresh_months"],
                                        cfg["staleness.aging_months"])
    return {
        "products": prods,
        "index_built_at": _rfc3339(kb.manifest.get("built_at", "")),
        "total_topics": int(kb.manifest.get("topic_count", 0)),
    }


def traverse_knowledge_graph(kb: KnowledgeBase, args: dict) -> dict:
    return kb.traverse_knowledge_graph(args["entity_name"], int(args.get("max_depth", 2)))


HANDLERS: dict[str, Callable[[KnowledgeBase, dict], dict]] = {
    "search_docs": search_docs,
    "fetch_document": fetch_document,
    "list_related": list_related,
    "compare_versions": compare_versions,
    "list_products": list_products,
    "answer_pack": answer_pack,
    "traverse_knowledge_graph": traverse_knowledge_graph,
}


def dispatch(kb: KnowledgeBase, name: str, args: dict) -> dict:
    fn = HANDLERS.get(name)
    if fn is None:
        raise invalid(
            f"Unknown tool '{name}'.",
            [{"value": n, "field": "tool"} for n in sorted(HANDLERS)])
    if name not in TOOLS_BY_NAME:
        raise invalid(f"Tool '{name}' has no schema.")
    return fn(kb, args or {})
