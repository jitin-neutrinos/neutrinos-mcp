"""Phase 3.5: Entity and Relationship Extraction (Local SLM).

Reads chunks.jsonl, extracts thematic entities and semantic relationships using a LOCAL Ollama model,
and writes them to entities.jsonl and relations.jsonl for index.py to load.

Requirements:
- Ollama installed and running (http://localhost:11434)
- Model pulled: `ollama run phi3:mini` or `ollama run llama3.1:8b`
"""

from __future__ import annotations

import json
import logging
import asyncio
from pathlib import Path
from openai import AsyncOpenAI
from neutrinos_mcp.config import ROOT

log = logging.getLogger(__name__)

# Point to Local Ollama Server instead of NVIDIA NIM
API_KEY = "ollama"
BASE_URL = "http://localhost:11434/v1"

# We recommend phi3:mini for extremely fast CPU extraction, or llama3.1:8b if you have 16GB RAM.
MODEL = "phi3:mini" 

PROMPT_SYS = """You are a documentation knowledge graph extractor. 
Extract technical entities (Product, Feature, API, Concept) and relationships (DEPENDS_ON, CONFIGURES, IMPLEMENTS, DEPRECATES, RELATED_TO) from the text.
Output ONLY valid JSON matching this schema exactly. Do not include markdown formatting or extra text.
{
  "entities": [
    {"id": "ent_1", "name": "string", "category": "Product|Feature|API|Concept", "description": "short description"}
  ],
  "relations": [
    {"src": "ent_1", "rel": "DEPENDS_ON", "dst": "ent_2"}
  ]
}
"""

async def process_chunk(client: AsyncOpenAI, chunk: dict, sem: asyncio.Semaphore) -> tuple[list[dict], list[dict]]:
    async with sem:
        try:
            resp = await client.chat.completions.create(
                model=MODEL,
                messages=[
                    {"role": "system", "content": PROMPT_SYS},
                    {"role": "user", "content": chunk["text"]}
                ],
                temperature=0.0,
                max_tokens=1024,
                # Note: Not all local SLMs support strict json_object, but we enforce it in prompt
                response_format={"type": "json_object"} 
            )
            raw = resp.choices[0].message.content.strip()
            if raw.startswith("```json"):
                raw = raw[7:]
            if raw.startswith("```"):
                raw = raw[3:]
            if raw.endswith("```"):
                raw = raw[:-3]
            data = json.loads(raw.strip())
            entities = data.get("entities", [])
            relations = data.get("relations", [])
            
            id_to_name = {e["id"]: e["name"] for e in entities if "id" in e and "name" in e}
            
            clean_entities = []
            for e in entities:
                if "name" in e and "category" in e:
                    clean_entities.append({
                        "name": e["name"],
                        "category": e["category"],
                        "description": e.get("description", "")
                    })
                    
            clean_relations = []
            for r in relations:
                src_name = id_to_name.get(r.get("src"))
                dst_name = id_to_name.get(r.get("dst"))
                if src_name and dst_name and "rel" in r:
                    clean_relations.append({
                        "src": src_name,
                        "rel": r["rel"],
                        "dst": dst_name,
                        "chunk_id": chunk["id"]
                    })
            log.info(f"Chunk {chunk['id']} complete: {len(clean_entities)} entities.")
            return clean_entities, clean_relations
        except Exception as e:
            log.warning(f"Failed to process chunk {chunk.get('id')}: {e}")
            return [], []

async def build_async(chunks_path: Path, entities_out: Path, relations_out: Path) -> None:
    client = AsyncOpenAI(api_key=API_KEY, base_url=BASE_URL)
    
    # Running locally on CPU: Keep concurrency lower so it doesn't crash your system
    sem = asyncio.Semaphore(4)
    
    chunks = []
    log.info("Reading chunks...")
    with chunks_path.open("r", encoding="utf-8") as f:
        for i, line in enumerate(f):
            if not line.strip(): continue
            c = json.loads(line)
            c["id"] = i + 1
            chunks.append(c)
            # REMOVED THE LIMIT: It will now process all 10,000+ chunks.
                
    log.info(f"Processing {len(chunks)} chunks via Local Ollama ({MODEL})...")
    log.info("This will take a significant amount of time on CPU. You can monitor the logs below.")
    
    tasks = [process_chunk(client, chunk, sem) for chunk in chunks]
    results = await asyncio.gather(*tasks)
    
    entities_seen = set()
    global_entities = []
    global_relations = []
    
    for (ents, rels) in results:
        for ent in ents:
            if ent["name"] not in entities_seen:
                entities_seen.add(ent["name"])
                ent["id"] = ent["name"]
                global_entities.append(ent)
        global_relations.extend(rels)

    with entities_out.open("w", encoding="utf-8") as f:
        for ent in global_entities:
            f.write(json.dumps(ent) + "\n")
            
    with relations_out.open("w", encoding="utf-8") as f:
        for rel in global_relations:
            f.write(json.dumps(rel) + "\n")
            
    log.info(f"DONE! Extracted {len(global_entities)} entities and {len(global_relations)} relations.")

def build(chunks_path: Path, entities_out: Path, relations_out: Path) -> None:
    asyncio.run(build_async(chunks_path, entities_out, relations_out))

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
    data_dir = ROOT / "data"
    build(
        data_dir / "chunks.jsonl",
        data_dir / "entities.jsonl",
        data_dir / "relations.jsonl"
    )
