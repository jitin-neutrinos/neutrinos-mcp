"""Phase 3.5: Entity and Relationship Extraction (Agentic GraphRAG).

Reads chunks.jsonl, extracts thematic entities and semantic relationships,
and writes them to entities.jsonl and relations.jsonl for index.py to load.
"""

from __future__ import annotations

import json
import logging
from pathlib import Path
from typing import Any, Iterable

from neutrinos_mcp.config import ROOT

log = logging.getLogger(__name__)

# Mock extraction function (In a production environment, this would hit 
# a local SLM via ONNX or a nimble hosted model to perform Named Entity Recognition)
def _extract_from_text(text: str, chunk_id: int) -> tuple[list[dict], list[dict]]:
    """Return a tuple of (entities, relations) found in the text."""
    entities: list[dict] = []
    relations: list[dict] = []
    
    # Placeholder Logic: A true extraction would use LLM structural output here.
    # For now, this serves as the schema-compliant extraction scaffold.
    if "Studio" in text and "Data Binding" in text:
        entities.extend([
            {"id": f"ent_{chunk_id}_1", "name": "Studio", "category": "Product", "description": "Visual builder"},
            {"id": f"ent_{chunk_id}_2", "name": "Data Binding", "category": "Feature", "description": "UI to data mapping"}
        ])
        relations.append({
            "src": f"ent_{chunk_id}_2", 
            "rel": "CONFIGURED_VIA", 
            "dst": f"ent_{chunk_id}_1",
            "chunk_id": chunk_id
        })
        
    return entities, relations

def build(chunks_path: Path, entities_out: Path, relations_out: Path) -> None:
    """Read chunks and produce extracted entities and relationships."""
    
    entities_seen = set()
    global_entities = []
    global_relations = []
    
    log.info("extracting entities from chunks...")
    
    with chunks_path.open("r", encoding="utf-8") as f:
        for i, line in enumerate(f):
            if not line.strip():
                continue
            chunk = json.loads(line)
            chunk_id = i + 1  # Simulated chunk ID alignment
            
            extracted_ents, extracted_rels = _extract_from_text(chunk["text"], chunk_id)
            
            for ent in extracted_ents:
                if ent["name"] not in entities_seen:
                    entities_seen.add(ent["name"])
                    global_entities.append(ent)
            
            global_relations.extend(extracted_rels)

    with entities_out.open("w", encoding="utf-8") as f:
        for ent in global_entities:
            f.write(json.dumps(ent) + "\n")
            
    with relations_out.open("w", encoding="utf-8") as f:
        for rel in global_relations:
            f.write(json.dumps(rel) + "\n")
            
    log.info(f"extracted {len(global_entities)} entities and {len(global_relations)} relations")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
    data_dir = ROOT / "data"
    build(
        data_dir / "chunks.jsonl",
        data_dir / "entities.jsonl",
        data_dir / "relations.jsonl"
    )
