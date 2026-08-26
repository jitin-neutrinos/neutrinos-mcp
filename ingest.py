import sqlite3
import os
import chromadb
from chromadb.utils import embedding_functions
from langchain_text_splitters import RecursiveCharacterTextSplitter
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

DB_PATH = "neutrinos_docs.db"
CHROMA_PATH = os.path.join("neutrinos-mcp", "chroma_db")
EMBEDDING_MODEL = "BAAI/bge-small-en-v1.5"

def setup_sqlite():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    # Table to track which documents have already been ingested into the vector DB
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS ingested_docs (
            url TEXT PRIMARY KEY,
            ingested_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    return conn

def main():
    logging.info("Initializing ChromaDB and Embedding Model...")
    
    # Initialize ChromaDB client
    chroma_client = chromadb.PersistentClient(path=CHROMA_PATH)
    
    # Use SentenceTransformers embedding function
    sentence_transformer_ef = embedding_functions.SentenceTransformerEmbeddingFunction(model_name=EMBEDDING_MODEL)
    
    # Create or get the collection
    collection = chroma_client.get_or_create_collection(
        name="neutrinos_chunks",
        embedding_function=sentence_transformer_ef,
        metadata={"hnsw:space": "cosine"} # Cosine similarity is best for bge models
    )
    
    # Initialize text splitter (512 tokens max, 50 overlap)
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000, # Approx 250-300 tokens
        chunk_overlap=150,
        length_function=len,
        separators=["\n\n", "\n", " ", ""]
    )
    
    conn = setup_sqlite()
    cursor = conn.cursor()
    
    # Get all documents that haven't been ingested yet
    cursor.execute("""
        SELECT d.url, d.title, d.content 
        FROM documents d
        LEFT JOIN ingested_docs i ON d.url = i.url
        WHERE i.url IS NULL
    """)
    unprocessed_docs = cursor.fetchall()
    
    if not unprocessed_docs:
        logging.info("No new documents to ingest.")
        return

    logging.info(f"Found {len(unprocessed_docs)} new documents to ingest.")
    
    for url, title, content in unprocessed_docs:
        if not content or len(content.strip()) < 50:
            logging.warning(f"Skipping empty or very short document: {url}")
            cursor.execute("INSERT INTO ingested_docs (url) VALUES (?)", (url,))
            conn.commit()
            continue
            
        logging.info(f"Chunking and embedding: {url}")
        
        # Split text into chunks
        chunks = text_splitter.split_text(content)
        
        # Prepare data for ChromaDB
        ids = []
        documents = []
        metadatas = []
        
        for i, chunk in enumerate(chunks):
            chunk_id = f"{url}#chunk_{i}"
            ids.append(chunk_id)
            documents.append(chunk)
            metadatas.append({
                "url": url,
                "title": title if title else "Untitled",
                "chunk_index": i
            })
        
        # Insert into ChromaDB
        try:
            collection.add(
                documents=documents,
                metadatas=metadatas,
                ids=ids
            )
            
            # Mark as ingested in SQLite
            cursor.execute("INSERT INTO ingested_docs (url) VALUES (?)", (url,))
            conn.commit()
        except Exception as e:
            logging.error(f"Failed to ingest chunks for {url}: {e}")

    conn.close()
    logging.info(f"Successfully ingested all pending documents into ChromaDB at {CHROMA_PATH}")

if __name__ == "__main__":
    main()
