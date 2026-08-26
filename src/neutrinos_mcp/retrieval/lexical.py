"""Stage 1a — BM25 over chunk_fts, with a relaxation ladder (plan §7.1).

Two things this module is responsible for:

* **Never letting user input reach FTS5 as syntax.** A question containing
  `AND`, `OR`, `NEAR`, `*` or an unbalanced quote is a query, not an
  expression. Every term is tokenised and re-quoted before it reaches MATCH.

* **Relaxing predictably, and saying so.** "How do I bind a widget?" should not
  return zero results because "how" and "do" are absent from the corpus. The
  ladder goes AND -> AND-minus-stopwords -> OR-minus-stopwords -> OR, and the
  winning expression is reported back so the caller can weigh a loose match
  differently from a strict one.
"""

from __future__ import annotations

import re
import sqlite3

_TOKEN = re.compile(r"[A-Za-z0-9_][A-Za-z0-9_.\-]*")

# Deliberately small: this corpus is full of short technical tokens, and an
# aggressive stoplist would eat real terms ("on", "is" appear in API names).
STOPWORDS = {
    "a", "an", "and", "are", "as", "at", "be", "but", "by", "can", "do", "does",
    "for", "from", "how", "i", "if", "in", "into", "is", "it", "its", "me", "my",
    "of", "on", "or", "our", "so", "that", "the", "their", "then", "there",
    "these", "they", "this", "to", "was", "we", "were", "what", "when", "where",
    "which", "why", "will", "with", "you", "your",
}


def terms(query: str) -> list[str]:
    """Safe FTS5 terms. Anything that could be an operator becomes a literal."""
    return [t for t in _TOKEN.findall(query or "") if len(t) > 1 or t.isdigit()]


def _quote(t: str) -> str:
    return '"' + t.replace('"', '""') + '"'


def relaxations(query: str) -> list[tuple[str, str]]:
    """[(label, match_expression)] from strictest to loosest."""
    ts = terms(query)
    if not ts:
        return []
    keep = [t for t in ts if t.lower() not in STOPWORDS] or ts
    q = [_quote(t) for t in ts]
    k = [_quote(t) for t in keep]
    out = [("AND", " AND ".join(q))]
    if keep != ts:
        out.append(("AND-nostop", " AND ".join(k)))
    if len(k) > 1:
        out.append(("OR-nostop", " OR ".join(k)))
    if len(q) > 1 and keep != ts:
        out.append(("OR", " OR ".join(q)))
    seen, uniq = set(), []
    for label, expr in out:
        if expr not in seen:
            seen.add(expr)
            uniq.append((label, expr))
    return uniq


def search(
    conn: sqlite3.Connection,
    query: str,
    limit: int = 50,
    pubs: list[str] | None = None,
) -> tuple[list[tuple[int, float]], str]:
    """Returns ([(chunk_id, bm25_score)], winning_match_expression).

    bm25() returns a negative number where more negative is better; it is
    flipped here so callers everywhere treat "higher is better".
    """
    scope_sql, scope_args = "", []
    if pubs:
        scope_sql = f" AND c.pub IN ({','.join('?' * len(pubs))})"
        scope_args = list(pubs)

    for _label, expr in relaxations(query):
        sql = f"""
            SELECT c.id, -bm25(chunk_fts, 3.0, 4.0, 1.0) AS score
            FROM chunk_fts
            JOIN chunk c ON c.id = chunk_fts.rowid
            WHERE chunk_fts MATCH ?{scope_sql}
            ORDER BY score DESC
            LIMIT ?
        """
        try:
            rows = conn.execute(sql, [expr, *scope_args, limit]).fetchall()
        except sqlite3.OperationalError:
            continue  # a malformed expression must never surface as an error
        if rows:
            return [(int(r[0]), float(r[1])) for r in rows], expr
    return [], ""


def search_topics(
    conn: sqlite3.Connection, query: str, limit: int = 20, pubs: list[str] | None = None
) -> list[tuple[int, float]]:
    scope_sql, scope_args = "", []
    if pubs:
        scope_sql = f" AND t.pub IN ({','.join('?' * len(pubs))})"
        scope_args = list(pubs)
    for _label, expr in relaxations(query):
        sql = f"""
            SELECT t.id, -bm25(topic_fts, 8.0, 3.0, 1.0) AS score
            FROM topic_fts JOIN topic t ON t.id = topic_fts.rowid
            WHERE topic_fts MATCH ?{scope_sql}
            ORDER BY score DESC LIMIT ?
        """
        try:
            rows = conn.execute(sql, [expr, *scope_args, limit]).fetchall()
        except sqlite3.OperationalError:
            continue
        if rows:
            return [(int(r[0]), float(r[1])) for r in rows]
    return []
