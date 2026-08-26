"""Stage 0 — version scope resolution (plan §7.0).

The single highest-risk failure for this corpus is answering a Studio 9
question from the Studio 7 page: fluent, cited, and wrong. Scope resolution is
what prevents it, and it must run BEFORE scoring — filtering afterwards lets 50
candidate slots fill with superseded near-duplicates before scoping ever runs.

Precedence:
  1. explicit `product` / `version` tool arguments
  2. version tokens detected in the query ("Studio 9", "v8", "release 6")
  3. default: current versions only
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field

from ..config import PublicationRegistry
from ..vectorstore import Scope

# A version token: "9", "v9", "version 9", "release 6", "8.x".
# The product NAME is resolved separately, as a suffix of the preceding words
# (see detect_versions) rather than by one greedy regex group.
_VER_NUM = re.compile(r"\b(?P<ver>\d{1,2})(?:\.[0-9x]+)?\b")


@dataclass
class ResolvedScope:
    families: list[str] = field(default_factory=list)
    pubs: list[str] = field(default_factory=list)
    versions: list[str] = field(default_factory=list)
    products: list[str] = field(default_factory=list)
    include_superseded: bool = False
    inferred: bool = True
    inferred_from: str = "default_current"
    ambiguous_products: list[str] = field(default_factory=list)

    def to_store_scope(self) -> Scope:
        return Scope(
            families=self.families or None,
            pubs=self.pubs or None,
            current_only=(not self.include_superseded and not self.pubs),
        )

    def as_dict(self) -> dict:
        return {
            "products": self.products,
            "versions": self.versions,
            "include_superseded": self.include_superseded,
            "inferred": self.inferred,
            "inferred_from": self.inferred_from,
        }


def detect_versions(query: str, reg: PublicationRegistry) -> list[tuple[str, str]]:
    """(family, version) pairs named in the query. Product name must resolve.

    Works backwards from each version token over the 1-4 words preceding it,
    longest first. A single non-greedy regex group swallows the whole clause
    ("how do I do this in Studio" for "...in Studio 8"), which never resolves
    to a product — the name has to be tried as a *suffix* of what precedes the
    number, not as everything before it.
    """
    found: list[tuple[str, str]] = []
    for m in _VER_NUM.finditer(query or ""):
        ver = m.group("ver")
        before = (query[: m.start()]).strip()
        before = re.sub(r"\b(?:v|version|release|r)\s*$", "", before, flags=re.I).strip()
        words = re.findall(r"[A-Za-z][A-Za-z.\-]*", before)
        for n in range(min(4, len(words)), 0, -1):
            fam = reg.resolve_product(" ".join(words[-n:]))
            if fam:
                found.append((fam, ver))
                break
    return found


def resolve(
    reg: PublicationRegistry,
    query: str = "",
    product: str | None = None,
    version: str | None = None,
    include_superseded: bool = False,
) -> ResolvedScope:
    rs = ResolvedScope(include_superseded=include_superseded)

    # 1 — explicit arguments win outright
    if product:
        fam = reg.resolve_product(product)
        if fam is None:
            raise ValueError(
                f"Unknown product '{product}'. Call list_products for valid values."
            )
        rs.families = [fam]
        rs.products = [reg.family(fam)[0].product]
        rs.inferred = False
        rs.inferred_from = "explicit_argument"
        if version:
            match = [p for p in reg.family(fam) if (p.version or "") == str(version)]
            if not match:
                avail = [p.version for p in reg.family(fam) if p.version]
                raise ValueError(
                    f"Product '{rs.products[0]}' has no version '{version}'. "
                    f"Available: {', '.join(avail) or 'unversioned'}."
                )
            rs.pubs = [p.id for p in match]
            rs.versions = [str(version)]
        else:
            fam_pubs = reg.family(fam)
            keep = fam_pubs if include_superseded else [p for p in fam_pubs if p.is_current]
            rs.pubs = [p.id for p in keep]
            rs.versions = [p.version for p in keep if p.version]
        return rs

    # 2 — version tokens in the query text
    detected = detect_versions(query, reg)
    if detected:
        pubs, vers, prods = [], [], []
        for fam, ver in detected:
            match = [p for p in reg.family(fam) if (p.version or "") == ver]
            if match:
                pubs += [p.id for p in match]
                vers.append(ver)
                prods.append(match[0].product)
        if pubs:
            rs.pubs = sorted(set(pubs))
            rs.versions = sorted(set(vers))
            rs.products = sorted(set(prods))
            rs.families = sorted({reg.get(p).family for p in rs.pubs})
            rs.inferred = True
            rs.inferred_from = "query_tokens"
            return rs

    # 3 — default: current versions only, all products
    rs.include_superseded = include_superseded
    rs.inferred = True
    rs.inferred_from = "default_current"
    if not include_superseded:
        rs.pubs = [p.id for p in reg if p.is_current]
    rs.products = []
    rs.versions = []
    return rs


def version_ambiguous(hits: list[dict], scope: ResolvedScope) -> bool:
    """True when strong hits span multiple versions and the user named none.

    The correct move then is to ask, not to guess — which is why this is a
    typed field on the tool response rather than a hope about model behaviour.
    """
    if not scope.inferred or scope.versions:
        return False
    strong = [h for h in hits[:5] if h.get("score", 0) >= 0.5]
    fams = {(h.get("product"), h.get("version")) for h in strong if h.get("version")}
    by_product: dict[str, set] = {}
    for prod, ver in fams:
        by_product.setdefault(prod, set()).add(ver)
    return any(len(v) > 1 for v in by_product.values())
