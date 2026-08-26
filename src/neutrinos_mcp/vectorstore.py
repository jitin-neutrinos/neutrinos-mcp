"""Vector store behind an interface (plan AD-02, R5).

Two working backends:

* **sqlite-vec** (default) — vectors live in the same file as content, FTS and
  graph, so the index is one artifact that snapshots, ships and rolls back
  atomically. Brute-force KNN over ~8k x 384 is a few milliseconds; ANN would
  be premature. Metadata columns filter BEFORE distance is computed, which is
  what makes version scoping cheap rather than a post-filter that wastes the
  candidate pool.

* **chroma** — a fully wired alternate. Selected with one line in
  settings.toml. It is the escape hatch R5 asks for (sqlite-vec is pre-v1), and
  the reason the rest of the codebase never imports either library directly.

Both implement the same contract, and `tests/test_vectorstore.py` runs the same
suite against whichever backends are installed.
"""

from __future__ import annotations

import sqlite3
import struct
from pathlib import Path
from typing import Iterable, Protocol, Sequence

import numpy as np


def pack(vec: Sequence[float]) -> bytes:
    return struct.pack(f"{len(vec)}f", *vec)


def unpack(blob: bytes) -> np.ndarray:
    return np.frombuffer(blob, dtype=np.float32)


class Scope:
    """A resolved version scope (plan §7.0), shared by both backends."""

    __slots__ = ("families", "pubs", "current_only")

    def __init__(self, families: Iterable[str] | None = None,
                 pubs: Iterable[str] | None = None,
                 current_only: bool = False):
        self.families = sorted(set(families)) if families else None
        self.pubs = sorted(set(pubs)) if pubs else None
        self.current_only = current_only

    def __repr__(self) -> str:
        return f"Scope(families={self.families}, pubs={self.pubs}, current_only={self.current_only})"


class VectorStore(Protocol):
    def create(self, dim: int) -> None: ...
    def add(self, rows: Sequence[dict]) -> None: ...
    def query(self, vec: np.ndarray, k: int, scope: Scope | None = None) -> list[tuple[int, float]]: ...
    def vectors_for(self, chunk_ids: Sequence[int]) -> dict[int, np.ndarray]: ...
    def count(self) -> int: ...


# ------------------------------------------------------------------ sqlite-vec


class SqliteVecStore:
    """Vectors inside neutrinos.db. Keeps the single-artifact property."""

    name = "sqlite-vec"

    def __init__(self, conn: sqlite3.Connection):
        self.conn = conn

    @staticmethod
    def load_extension(conn: sqlite3.Connection) -> None:
        import sqlite_vec

        conn.enable_load_extension(True)
        sqlite_vec.load(conn)
        conn.enable_load_extension(False)

    def create(self, dim: int) -> None:
        self.conn.execute(
            f"""CREATE VIRTUAL TABLE IF NOT EXISTS vec_chunks USING vec0(
                   chunk_id INTEGER PRIMARY KEY,
                   embedding FLOAT[{dim}],
                   pub TEXT, family TEXT,
                   version_rank INTEGER, is_current INTEGER,
                   +heading_path TEXT)"""
        )

    def add(self, rows: Sequence[dict]) -> None:
        self.conn.executemany(
            """INSERT INTO vec_chunks
               (chunk_id, embedding, pub, family, version_rank, is_current, heading_path)
               VALUES (?,?,?,?,?,?,?)""",
            [(r["chunk_id"], pack(r["vector"]), r["pub"], r["family"],
              r["version_rank"], r["is_current"], r["heading_path"]) for r in rows],
        )

    def _where(self, scope: Scope | None) -> tuple[str, list]:
        if scope is None:
            return "", []
        parts, args = [], []
        if scope.families:
            parts.append(f"family IN ({','.join('?' * len(scope.families))})")
            args += scope.families
        if scope.pubs:
            parts.append(f"pub IN ({','.join('?' * len(scope.pubs))})")
            args += scope.pubs
        if scope.current_only:
            parts.append("is_current = 1")
        return ((" AND " + " AND ".join(parts)) if parts else ""), args

    def query(self, vec: np.ndarray, k: int, scope: Scope | None = None) -> list[tuple[int, float]]:
        where, args = self._where(scope)
        sql = f"SELECT chunk_id, distance FROM vec_chunks WHERE embedding MATCH ? AND k = ?{where}"
        return [(int(r[0]), float(r[1]))
                for r in self.conn.execute(sql, [pack(vec.tolist()), k, *args])]

    def vectors_for(self, chunk_ids: Sequence[int]) -> dict[int, np.ndarray]:
        if not chunk_ids:
            return {}
        q = ",".join("?" * len(chunk_ids))
        rows = self.conn.execute(
            f"SELECT chunk_id, embedding FROM vec_chunks WHERE chunk_id IN ({q})",
            list(chunk_ids)).fetchall()
        return {int(r[0]): unpack(r[1]) for r in rows}

    def count(self) -> int:
        return int(self.conn.execute("SELECT count(*) FROM vec_chunks").fetchone()[0])


# ---------------------------------------------------------------------- chroma


class ChromaStore:
    """ChromaDB alternate backend (R5 escape hatch).

    Kept behaviourally identical to SqliteVecStore: same Scope semantics, same
    return shape, cosine distance in both cases.
    """

    name = "chroma"
    COLLECTION = "neutrinos_chunks"

    def __init__(self, path: str | Path):
        import chromadb

        self.path = str(path)
        self._client = chromadb.PersistentClient(path=self.path)
        self._col = None

    def create(self, dim: int) -> None:
        import chromadb  # noqa: F401

        try:
            self._client.delete_collection(self.COLLECTION)
        except Exception:
            pass
        # Embeddings are supplied explicitly — never let Chroma download and run
        # its own default model, or the index would silently disagree with the
        # manifest (AD-12).
        self._col = self._client.create_collection(
            name=self.COLLECTION,
            metadata={"hnsw:space": "cosine", "dim": dim},
            embedding_function=None,
        )

    @property
    def col(self):
        if self._col is None:
            self._col = self._client.get_collection(self.COLLECTION, embedding_function=None)
        return self._col

    def add(self, rows: Sequence[dict]) -> None:
        self.col.add(
            ids=[str(r["chunk_id"]) for r in rows],
            embeddings=[list(map(float, r["vector"])) for r in rows],
            metadatas=[{"pub": r["pub"], "family": r["family"],
                        "version_rank": int(r["version_rank"]),
                        "is_current": int(r["is_current"]),
                        "heading_path": r["heading_path"]} for r in rows],
        )

    @staticmethod
    def _filter(scope: Scope | None):
        if scope is None:
            return None
        clauses = []
        if scope.families:
            clauses.append({"family": {"$in": scope.families}})
        if scope.pubs:
            clauses.append({"pub": {"$in": scope.pubs}})
        if scope.current_only:
            clauses.append({"is_current": {"$eq": 1}})
        if not clauses:
            return None
        return clauses[0] if len(clauses) == 1 else {"$and": clauses}

    def query(self, vec: np.ndarray, k: int, scope: Scope | None = None) -> list[tuple[int, float]]:
        res = self.col.query(
            query_embeddings=[list(map(float, vec))],
            n_results=k,
            where=self._filter(scope),
            include=["distances"],
        )
        ids = res.get("ids", [[]])[0]
        dists = res.get("distances", [[]])[0]
        return [(int(i), float(d)) for i, d in zip(ids, dists)]

    def vectors_for(self, chunk_ids: Sequence[int]) -> dict[int, np.ndarray]:
        if not chunk_ids:
            return {}
        res = self.col.get(ids=[str(c) for c in chunk_ids], include=["embeddings"])
        out = {}
        for i, emb in zip(res.get("ids", []), res.get("embeddings", [])):
            out[int(i)] = np.asarray(emb, dtype=np.float32)
        return out

    def count(self) -> int:
        return int(self.col.count())


# ---------------------------------------------------------------------- factory


def open_store(backend: str, conn: sqlite3.Connection | None = None,
               chroma_path: str | Path | None = None) -> VectorStore:
    if backend == "sqlite-vec":
        if conn is None:
            raise ValueError("sqlite-vec backend needs the sqlite connection")
        return SqliteVecStore(conn)
    if backend == "chroma":
        if chroma_path is None:
            raise ValueError("chroma backend needs a path")
        return ChromaStore(chroma_path)
    raise ValueError(f"unknown vector_store.backend '{backend}' (expected sqlite-vec | chroma)")
