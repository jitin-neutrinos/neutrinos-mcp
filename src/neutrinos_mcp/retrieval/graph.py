"""Stages 6-7 — confidence gate and conditional graph expansion (plan AD-08).

The graph is an expansion signal, not a co-equal retrieval mode. Most support
questions are single-hop lookups; traversing on every query buys latency, not
accuracy. So expansion fires only when the evidence is weak or the question is
shaped like a prerequisite question.

Relations used, in the order they earn their place:
  PREV     — the authored "what comes before this", the best prerequisite signal
  SEE_ALSO — human-curated, high precision
  LINKS_TO — in-prose cross-references
"""

from __future__ import annotations

import re
import sqlite3
from typing import Sequence

# Questions whose answer usually lives one hop away from the best match.
_PREREQ = re.compile(
    r"\b(before|prerequisit\w*|require[sd]?|first|setup|set up|configure|"
    r"depend\w*|why (?:does|is|are|can't|cannot)|doesn'?t work|not working|"
    r"after|next step|instead of)\b",
    re.I,
)

EXPANSION_RELS = ("PREV", "SEE_ALSO", "LINKS_TO")


def should_expand(query: str, top_score: float, threshold: float) -> tuple[bool, str]:
    """(expand?, why). The reason is surfaced in telemetry so the gate is auditable."""
    if top_score < threshold:
        return True, f"low_confidence({top_score:.2f}<{threshold})"
    if _PREREQ.search(query or ""):
        return True, "prerequisite_language"
    return False, ""


def neighbours(
    conn: sqlite3.Connection,
    topic_ids: Sequence[int],
    rels: Sequence[str] = EXPANSION_RELS,
    limit: int = 12,
) -> list[int]:
    """Resolved 1-hop neighbours of the given topics, nearest relations first."""
    if not topic_ids:
        return []
    tq = ",".join("?" * len(topic_ids))
    rq = ",".join("?" * len(rels))
    rows = conn.execute(
        f"""SELECT dst_id, rel FROM edge
            WHERE src_id IN ({tq}) AND rel IN ({rq})
              AND resolved = 1 AND dst_id IS NOT NULL""",
        [*topic_ids, *rels],
    ).fetchall()
    order = {r: i for i, r in enumerate(rels)}
    seen: dict[int, int] = {}
    for dst, rel in rows:
        d = int(dst)
        if d in topic_ids:
            continue
        seen[d] = min(seen.get(d, 99), order.get(rel, 99))
    return [d for d, _ in sorted(seen.items(), key=lambda kv: kv[1])][:limit]


def chunks_of(conn: sqlite3.Connection, topic_ids: Sequence[int],
              pubs: Sequence[str] | None = None, per_topic: int = 2) -> list[int]:
    """Lead chunks for expanded topics — the opening sections carry the concept."""
    if not topic_ids:
        return []
    out: list[int] = []
    scope = ""
    args_extra: list = []
    if pubs:
        scope = f" AND pub IN ({','.join('?' * len(pubs))})"
        args_extra = list(pubs)
    for tid in topic_ids:
        rows = conn.execute(
            f"SELECT id FROM chunk WHERE topic_id = ?{scope} ORDER BY ordinal LIMIT ?",
            [tid, *args_extra, per_topic],
        ).fetchall()
        out += [int(r[0]) for r in rows]
    return out


def typed_neighbourhood(conn: sqlite3.Connection, topic_id: int,
                        limit_per_relation: int = 10) -> dict:
    """Full typed neighbourhood for the `list_related` tool (§8.5.4)."""
    out: dict[str, list] = {k: [] for k in
                            ("next", "prev", "see_also", "links_to",
                             "linked_from", "other_versions")}
    unresolved: list[dict] = []

    rows = conn.execute(
        """SELECT e.rel, e.dst_pub, e.dst_slug, e.dst_id, e.resolved,
                  t.title, p.product, p.version, p.is_current
           FROM edge e
           LEFT JOIN topic t ON t.id = e.dst_id
           LEFT JOIN publication p ON p.id = e.dst_pub
           WHERE e.src_id = ?""", (topic_id,)).fetchall()

    key = {"NEXT": "next", "PREV": "prev", "SEE_ALSO": "see_also",
           "LINKS_TO": "links_to", "SAME_TOPIC_OTHER_VERSION": "other_versions"}
    for rel, dpub, dslug, dst_id, resolved, title, product, version, is_current in rows:
        if not resolved or dst_id is None:
            unresolved.append({"target": f"{dpub}/{dslug}", "relation": rel})
            continue
        bucket = key.get(rel)
        if bucket is None:
            continue
        if len(out[bucket]) >= limit_per_relation:
            continue
        out[bucket].append({
            "ref": f"{dpub}/{dslug}", "title": title or dslug,
            "product": product, "version": version,
            "is_current": bool(is_current),
        })

    back = conn.execute(
        """SELECT t.pub, t.slug, t.title, p.product, p.version, p.is_current
           FROM edge e JOIN topic t ON t.id = e.src_id
           JOIN publication p ON p.id = t.pub
           WHERE e.dst_id = ? AND e.rel = 'LINKS_TO' LIMIT ?""",
        (topic_id, limit_per_relation)).fetchall()
    out["linked_from"] = [
        {"ref": f"{r[0]}/{r[1]}", "title": r[2], "product": r[3],
         "version": r[4], "is_current": bool(r[5])} for r in back]

    return {"relations": out, "unresolved_links": unresolved}
