"""Stage 1 — crawl (plan §6.1).

AD-01: the ClickHelp portal serves complete, server-rendered HTML at
`/article/<pub>/<slug>`. The hash-routed reader URL is for humans. So this is
plain HTTP with a bounded async pool — no browser, no fixed waits, minutes not
hours — and unlike a headless crawl it leaves behind `raw/` as provenance, so
extraction can be re-run and re-tested without re-fetching.

Coverage is sitemap-driven, not link-following: BFS from a seed page reaches
whatever the SPA nav happens to expose, which measurably missed 42 of 53
publications. The sitemap index enumerates all 3,117 topics by construction.

    python -m neutrinos_mcp.ingest.crawl              # delta crawl
    python -m neutrinos_mcp.ingest.crawl --full       # ignore cache
    python -m neutrinos_mcp.ingest.crawl --pubs studio-guide-9,ai-hub
"""

from __future__ import annotations

import argparse
import asyncio
import hashlib
import json
import re
import time
from dataclasses import dataclass, field
from pathlib import Path
from xml.etree import ElementTree as ET

import httpx

from ..config import ROOT, settings

_NS = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
_SAFE = re.compile(r"[^A-Za-z0-9._-]")


@dataclass
class Topic:
    pub: str
    slug: str
    lastmod: str | None

    @property
    def key(self) -> str:
        return f"{self.pub}/{self.slug}"


@dataclass
class Report:
    started: str = ""
    finished: str = ""
    duration_s: float = 0.0
    publications: int = 0
    discovered: int = 0
    fetched: int = 0
    cached: int = 0
    failed: int = 0
    bytes: int = 0
    per_publication: dict = field(default_factory=dict)
    failures: list = field(default_factory=list)


def raw_path(pub: str, slug: str) -> Path:
    return settings().path("raw") / _SAFE.sub("_", pub) / (_SAFE.sub("_", slug) + ".html")


async def _get(client: httpx.AsyncClient, url: str, retries: int) -> httpx.Response:
    last: Exception | None = None
    for attempt in range(retries):
        try:
            r = await client.get(url)
            if r.status_code < 500:
                return r
            last = httpx.HTTPStatusError(f"HTTP {r.status_code}", request=r.request, response=r)
        except Exception as exc:  # network flake, timeout, reset
            last = exc
        await asyncio.sleep(1.0 * (attempt + 1))  # linear backoff
    raise last  # type: ignore[misc]


async def discover(client: httpx.AsyncClient, only: set[str] | None = None) -> list[Topic]:
    """Sitemap index -> every (publication, slug, lastmod) in the portal."""
    cfg = settings()
    idx = await _get(client, cfg["source.sitemap_index"], cfg["source.retries"])
    idx.raise_for_status()
    sitemaps = [
        loc.text
        for loc in ET.fromstring(idx.content).findall(".//sm:loc", _NS)
        if loc.text and "sitemap_publication_" in loc.text
    ]

    async def one(sm_url: str) -> list[Topic]:
        pub = sm_url.rsplit("sitemap_publication_", 1)[1].removesuffix(".xml")
        if only and pub not in only:
            return []
        r = await _get(client, sm_url, cfg["source.retries"])
        root = ET.fromstring(r.content)
        out = []
        for url_el in root.findall(".//sm:url", _NS):
            loc = url_el.findtext("sm:loc", namespaces=_NS) or ""
            lastmod = url_el.findtext("sm:lastmod", namespaces=_NS)
            slug = loc.rstrip("/").rsplit("/", 1)[-1]
            if slug:
                out.append(Topic(pub, slug, (lastmod or "")[:10] or None))
        return out

    groups = await asyncio.gather(*(one(s) for s in sitemaps))
    return [t for g in groups for t in g]


async def crawl(full: bool = False, only: set[str] | None = None) -> Report:
    cfg = settings()
    rep = Report(started=time.strftime("%Y-%m-%dT%H:%M:%S"))
    t0 = time.time()

    limits = httpx.Limits(max_connections=cfg["source.concurrency"] * 2,
                          max_keepalive_connections=cfg["source.concurrency"])
    headers = {"User-Agent": cfg["source.user_agent"], "Accept": "text/html"}

    async with httpx.AsyncClient(
        headers=headers, limits=limits, timeout=cfg["source.timeout_s"],
        follow_redirects=True, http2=False,
    ) as client:
        topics = await discover(client, only)
        rep.discovered = len(topics)
        rep.publications = len({t.pub for t in topics})
        print(f"discovered {rep.discovered} topics across {rep.publications} publications")

        sem = asyncio.Semaphore(cfg["source.concurrency"])
        done = 0

        async def fetch(t: Topic) -> None:
            nonlocal done
            dest = raw_path(t.pub, t.slug)
            if not full and dest.exists() and dest.stat().st_size > 0:
                rep.cached += 1
                rep.per_publication.setdefault(t.pub, {"fetched": 0, "cached": 0, "failed": 0})["cached"] += 1
                return
            url = cfg["source.article_url"].format(pub=t.pub, slug=t.slug)
            async with sem:
                try:
                    r = await _get(client, url, cfg["source.retries"])
                    if r.status_code != 200 or not r.content:
                        raise RuntimeError(f"HTTP {r.status_code}, {len(r.content)} bytes")
                    dest.parent.mkdir(parents=True, exist_ok=True)
                    dest.write_bytes(r.content)
                    rep.fetched += 1
                    rep.bytes += len(r.content)
                    rep.per_publication.setdefault(t.pub, {"fetched": 0, "cached": 0, "failed": 0})["fetched"] += 1
                except Exception as exc:
                    rep.failed += 1
                    rep.per_publication.setdefault(t.pub, {"fetched": 0, "cached": 0, "failed": 0})["failed"] += 1
                    rep.failures.append({"pub": t.pub, "slug": t.slug, "url": url, "error": str(exc)[:200]})
                finally:
                    done += 1
                    if done % 250 == 0:
                        el = time.time() - t0
                        print(f"  {done}/{len(topics)}  ({done/el:.1f}/s, {rep.failed} failed)")

        await asyncio.gather(*(fetch(t) for t in topics))

    # index of what we have, so extract.py needs no network at all
    manifest = [
        {"pub": t.pub, "slug": t.slug, "lastmod": t.lastmod,
         "url": cfg["source.reader_url"].format(pub=t.pub, slug=t.slug),
         "raw": str(raw_path(t.pub, t.slug).relative_to(ROOT)).replace("\\", "/")}
        for t in topics if raw_path(t.pub, t.slug).exists()
    ]
    (ROOT / "data" / "topics_manifest.json").write_text(
        json.dumps(manifest, indent=1), encoding="utf-8")

    rep.duration_s = round(time.time() - t0, 1)
    rep.finished = time.strftime("%Y-%m-%dT%H:%M:%S")
    (ROOT / "data" / "crawl_report.json").write_text(
        json.dumps(rep.__dict__, indent=2), encoding="utf-8")
    return rep


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--full", action="store_true", help="re-fetch even if cached in raw/")
    ap.add_argument("--pubs", type=str, default=None, help="comma-separated publication ids")
    args = ap.parse_args()
    only = {p.strip() for p in args.pubs.split(",")} if args.pubs else None

    rep = asyncio.run(crawl(full=args.full, only=only))
    print(
        f"\ndiscovered={rep.discovered}  fetched={rep.fetched}  cached={rep.cached}  "
        f"failed={rep.failed}  {rep.bytes/1e6:.1f} MB  in {rep.duration_s}s"
    )
    if rep.failures:
        print(f"\nfirst failures ({len(rep.failures)} total):")
        for f in rep.failures[:10]:
            print(f"  {f['pub']}/{f['slug']}: {f['error']}")


if __name__ == "__main__":
    main()
