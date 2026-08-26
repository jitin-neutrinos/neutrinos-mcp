"""Settings and publication-family configuration.

Two config sources:
  config/settings.toml     — runtime knobs, model pins, budgets
  config/publications.yaml — the reviewed product/version map (plan §6.5)

`publications.yaml` is load-bearing: naming alone cannot derive version families
because products were renamed (App Builder -> Studio at Jaccard 0.991). An
unclassified publication is a build failure, never a warning.
"""

from __future__ import annotations

import tomllib
from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path
from typing import Any

import yaml

ROOT = Path(__file__).resolve().parents[2]


def _deep_get(d: dict, dotted: str, default: Any = None) -> Any:
    cur: Any = d
    for part in dotted.split("."):
        if not isinstance(cur, dict) or part not in cur:
            return default
        cur = cur[part]
    return cur


class Settings:
    """Thin typed accessor over settings.toml. Paths resolve against repo root."""

    def __init__(self, raw: dict):
        self._raw = raw

    def __getitem__(self, dotted: str) -> Any:
        val = _deep_get(self._raw, dotted)
        if val is None:
            raise KeyError(f"settings.toml has no key '{dotted}'")
        return val

    def get(self, dotted: str, default: Any = None) -> Any:
        return _deep_get(self._raw, dotted, default)

    def path(self, dotted: str) -> Path:
        return ROOT / str(self[f"paths.{dotted}"])


@lru_cache(maxsize=1)
def settings() -> Settings:
    with open(ROOT / "config" / "settings.toml", "rb") as fh:
        return Settings(tomllib.load(fh))


@dataclass(frozen=True, slots=True)
class Publication:
    """One of the 53 publications, with its resolved family membership."""

    id: str
    title: str
    product: str
    version: str | None
    version_rank: int
    family: str
    is_current: bool
    lifecycle: str  # current | superseded | archived

    @property
    def label(self) -> str:
        return f"{self.product} {self.version}" if self.version else self.product


class PublicationRegistry:
    """The reviewed family map. Every lookup that misses is an error, by design."""

    def __init__(self, pubs: dict[str, Publication], aliases: dict[str, str]):
        self._pubs = pubs
        self._aliases = {k.lower(): v for k, v in aliases.items()}

    def __len__(self) -> int:
        return len(self._pubs)

    def __contains__(self, pub_id: str) -> bool:
        return pub_id in self._pubs

    def __iter__(self):
        return iter(self._pubs.values())

    def get(self, pub_id: str) -> Publication:
        try:
            return self._pubs[pub_id]
        except KeyError:
            raise KeyError(
                f"Publication '{pub_id}' is not classified in config/publications.yaml. "
                f"Add it (plan §6.5) — an unclassified publication silently escapes "
                f"version scoping."
            ) from None

    def family(self, name: str) -> list[Publication]:
        """All publications in a family, newest first."""
        return sorted(
            (p for p in self._pubs.values() if p.family == name),
            key=lambda p: -p.version_rank,
        )

    # Words users append that are documentation furniture, not product names.
    # "Components Guide" must resolve even though the product is "Components".
    _NOISE = ("guide", "guides", "docs", "doc", "documentation",
              "user guide", "user's guide", "reference", "manual")

    def _candidates(self, text: str):
        key = " ".join(text.strip().lower().split())
        yield key
        for n in self._NOISE:
            if key.endswith(" " + n):
                yield key[: -(len(n) + 1)].strip()
        yield key.replace(" ", "-")

    def resolve_product(self, text: str) -> str | None:
        """Map a user-supplied product name (or a former name) to a family id.

        Tolerant of trailing documentation words and of the publication id
        itself, because a community member types what they see on the page.
        """
        if not text:
            return None
        for key in self._candidates(text):
            if not key:
                continue
            if key in self._aliases:
                return self._aliases[key]
            if key in self._pubs:
                return self._pubs[key].family
            for p in self._pubs.values():
                if p.product.lower() == key or p.family == key:
                    return p.family
        return None

    def current_of(self, family: str) -> Publication | None:
        fam = self.family(family)
        for p in fam:
            if p.is_current:
                return p
        return fam[0] if fam else None

    def products(self) -> dict[str, list[Publication]]:
        out: dict[str, list[Publication]] = {}
        for p in self._pubs.values():
            out.setdefault(p.family, []).append(p)
        for v in out.values():
            v.sort(key=lambda p: -p.version_rank)
        return out


@lru_cache(maxsize=1)
def publications() -> PublicationRegistry:
    path = settings().path("publications")
    if not path.exists():
        raise FileNotFoundError(
            f"{path} is missing. Run `python -m neutrinos_mcp.ingest.families --seed` "
            f"to generate it from data/census.json, then have it reviewed (plan §6.5)."
        )
    doc = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    pubs: dict[str, Publication] = {}
    for pid, e in (doc.get("publications") or {}).items():
        pubs[pid] = Publication(
            id=pid,
            title=e.get("title", pid),
            product=e["product"],
            version=(str(e["version"]) if e.get("version") is not None else None),
            version_rank=int(e.get("version_rank", 0)),
            family=e["family"],
            is_current=bool(e.get("is_current", False)),
            lifecycle=e.get("lifecycle", "current"),
        )
    return PublicationRegistry(pubs, doc.get("aliases") or {})
