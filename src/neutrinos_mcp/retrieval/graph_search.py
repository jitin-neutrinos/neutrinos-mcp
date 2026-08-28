"""Agentic GraphRAG Traversal (Feature 3).

Executes multi-hop recursive queries across the semantic entity_relation table
to allow the LLM agent to explore concept spaces deterministically.
"""

from __future__ import annotations

import sqlite3

def traverse_graph(conn: sqlite3.Connection, entity_name: str, max_depth: int = 2) -> dict:
    """Traverse the knowledge graph starting from a specific entity.

    Returns the neighborhood of entities up to `max_depth` hops away,
    including the chunk_ids (refs) that serve as evidence for each edge.
    """
    max_depth = max(1, min(max_depth, 3))  # Clamp depth to prevent massive fanout

    # Find the starting entity
    start = conn.execute(
        "SELECT id, name, category, description FROM entity WHERE name = ? COLLATE NOCASE",
        (entity_name,)
    ).fetchone()

    if not start:
        # Fallback: fuzzy search
        sugg = conn.execute(
            "SELECT name FROM entity WHERE name LIKE ? LIMIT 5",
            (f"%{entity_name}%",)
        ).fetchall()
        suggestions = [s[0] for s in sugg]
        return {
            "error": f"Entity '{entity_name}' not found.",
            "suggestions": suggestions
        }

    start_id, start_name, start_cat, start_desc = start

    # Recursive CTE to find paths up to max_depth
    # We collect edges: (src_name, rel_type, dst_name, chunk_id, depth)
    query = """
    WITH RECURSIVE
      search_graph(src_id, rel_type, dst_id, chunk_id, depth) AS (
        SELECT src_id, rel_type, dst_id, chunk_id, 1
        FROM entity_relation
        WHERE src_id = ? OR dst_id = ?
        
        UNION ALL
        
        SELECT er.src_id, er.rel_type, er.dst_id, er.chunk_id, sg.depth + 1
        FROM entity_relation er
        JOIN search_graph sg ON (er.src_id = sg.dst_id OR er.dst_id = sg.src_id)
        WHERE sg.depth < ?
      )
    SELECT DISTINCT
      e1.name AS src_name,
      sg.rel_type,
      e2.name AS dst_name,
      c.pub,
      c.slug,
      sg.depth
    FROM search_graph sg
    JOIN entity e1 ON sg.src_id = e1.id
    JOIN entity e2 ON sg.dst_id = e2.id
    JOIN chunk c ON sg.chunk_id = c.id
    ORDER BY sg.depth ASC
    LIMIT 100
    """
    
    rows = conn.execute(query, (start_id, start_id, max_depth)).fetchall()

    edges = []
    entities_seen = {start_name}
    for r in rows:
        src, rel, dst, pub, slug, depth = r
        edges.append({
            "source": src,
            "relation": rel,
            "target": dst,
            "evidence_ref": f"{pub}/{slug}",
            "depth": depth
        })
        entities_seen.add(src)
        entities_seen.add(dst)

    # Fetch metadata for all seen entities
    placeholders = ",".join("?" for _ in entities_seen)
    ent_rows = conn.execute(
        f"SELECT name, category, description FROM entity WHERE name IN ({placeholders})",
        tuple(entities_seen)
    ).fetchall()
    
    nodes = [{"name": e[0], "category": e[1], "description": e[2]} for e in ent_rows]

    return {
        "start_node": {
            "name": start_name,
            "category": start_cat,
            "description": start_desc
        },
        "nodes": nodes,
        "edges": edges
    }
