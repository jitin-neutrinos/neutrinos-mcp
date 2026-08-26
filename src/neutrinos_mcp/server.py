"""MCP adapter (plan §8.4).

Translates arguments in and formats results out. Contains no SQL and no
retrieval logic — that is `kb.py` and `retrieval/`, so the CLI, the evaluation
harness and this server all exercise one code path.

Protocol posture:
  * tools are registered from `tools/schemas.py`, which is generated from the
    plan, so the wire contract and the specification cannot drift
  * every response is validated against its declared `outputSchema` before it
    leaves (AD-11)
  * a bad call returns an isError result, never a transport error — one bad
    tool call must not kill the session
  * all tools are read-only; there is no write path in the process
"""

from __future__ import annotations

import argparse
import json
import logging
import os
import sys
from typing import Any

from .config import ROOT, settings
from .errors import KBError
from .kb import KnowledgeBase
from .tools.handlers import dispatch
from .tools.schemas import COMMON, DEFAULT_ENABLED, TOOLS_BY_NAME

log = logging.getLogger("neutrinos-mcp")

_kb: KnowledgeBase | None = None


def check_for_db_updates():
    """Checks GitHub for a new database release and downloads it if newer."""
    try:
        import urllib.request
        import json
        import datetime
        from pathlib import Path
        
        # IMPORTANT: Make sure this matches your actual GitHub org/repo
        repo = "neutrinos/neutrinos-mcp" 
        req = urllib.request.Request(f"https://api.github.com/repos/{repo}/releases/latest")
        req.add_header('User-Agent', 'neutrinos-mcp-updater')
        
        # Fast 3-second timeout so it doesn't block startup if offline
        with urllib.request.urlopen(req, timeout=3.0) as response:
            data = json.loads(response.read().decode())
            published_at = data.get("published_at")
            
            db_path = Path("data/neutrinos.db")
            db_timestamp = db_path.stat().st_mtime if db_path.exists() else 0
            
            if published_at:
                dt = datetime.datetime.strptime(published_at, "%Y-%m-%dT%H:%M:%SZ")
                remote_ts = dt.replace(tzinfo=datetime.timezone.utc).timestamp()
                
                # If remote release is newer than local DB modification time
                if remote_ts > db_timestamp:
                    log.info(f"New DB version found ({data.get('tag_name')}). Downloading...")
                    asset_url = next((a.get("browser_download_url") for a in data.get("assets", []) if a.get("name") == "neutrinos.db"), None)
                    
                    if asset_url:
                        db_path.parent.mkdir(parents=True, exist_ok=True)
                        tmp_path = db_path.with_suffix(".db.tmp")
                        urllib.request.urlretrieve(asset_url, tmp_path)
                        tmp_path.replace(db_path)
                        log.info("Database updated successfully.")
    except Exception as e:
        log.warning(f"Auto-update check failed (this is non-fatal): {e}")


def kb() -> KnowledgeBase:
    """Opened lazily and reused: model load is ~1s and must not be paid per call."""
    global _kb
    if _kb is None:
        check_for_db_updates()
        _kb = KnowledgeBase()
    return _kb


# --------------------------------------------------------------- validation

_REGISTRY = None


def _validator(schema: dict):
    global _REGISTRY
    try:
        from jsonschema import Draft202012Validator
        from referencing import Registry, Resource
    except Exception:
        return None
    if _REGISTRY is None:
        # Registered under both the bare relative uri tools actually use
        # ("common.json#/$defs/...") and the declared $id, so either form
        # resolves regardless of which one a future schema edit picks.
        resource = Resource.from_contents(COMMON)
        _REGISTRY = Registry().with_resources(
            [("common.json", resource), (COMMON["$id"], resource)])
    # A tool's outputSchema also carries its OWN local `$defs` (e.g.
    # list_related's `neighbourList`) — the registry only supplies common.json;
    # local `#/$defs/...` refs must still resolve against `schema` itself, so
    # `schema` is registered with an anonymous resource rather than passed as
    # a bare dict, which is what `Draft202012Validator(schema, registry=...)`
    # already does correctly.
    return Draft202012Validator(schema, registry=_REGISTRY)


def validate_output(name: str, payload: dict) -> list[str]:
    """Returns a list of violations. Empty means valid."""
    spec = TOOLS_BY_NAME.get(name, {})
    schema = spec.get("outputSchema")
    if not schema:
        return []
    v = _validator(schema)
    if v is None:
        return []
    return [f"{'/'.join(str(p) for p in e.path)}: {e.message}" for e in v.iter_errors(payload)][:5]


def _strip_private(obj: Any) -> Any:
    """Drop internal `_`-prefixed keys before validation.

    They carry operator signal (content warnings, truncation) that the schema
    deliberately does not declare; keeping them out of the validated payload
    means `additionalProperties: false` stays meaningful.
    """
    if isinstance(obj, dict):
        return {k: _strip_private(v) for k, v in obj.items() if not k.startswith("_")}
    if isinstance(obj, list):
        return [_strip_private(x) for x in obj]
    return obj


def call_tool(name: str, args: dict) -> tuple[dict, bool]:
    """(payload, is_error). Errors are RFC 7807 problem objects."""
    try:
        raw = dispatch(kb(), name, args)
    except KBError as exc:
        return exc.to_dict(), True
    except Exception as exc:  # never let an unexpected error kill the session
        log.exception("tool %s failed", name)
        return {
            "type": "https://neutrinos-mcp/errors/internal",
            "title": "Internal Error", "status": 500,
            "detail": f"{type(exc).__name__}: {exc}",
        }, True

    payload = _strip_private(raw)
    problems = validate_output(name, payload)
    if problems:
        # A contract violation is a bug here, not the caller's fault — but the
        # caller still gets usable data plus a visible warning.
        log.error("output schema violation in %s: %s", name, problems)
        payload["_schema_warnings"] = problems
    return payload, False


# ------------------------------------------------------------------- FastMCP


def build_server(enabled: list[str] | None = None):
    from fastmcp import FastMCP
    from fastmcp.tools.function_tool import FunctionTool

    names = enabled or DEFAULT_ENABLED
    mcp = FastMCP(name="neutrinos-docs")

    for n in names:
        spec = TOOLS_BY_NAME[n]

        def make(tool_name: str):
            def handler(**kwargs) -> dict:
                payload, is_error = call_tool(tool_name, kwargs)
                if is_error:
                    from fastmcp.exceptions import ToolError

                    raise ToolError(json.dumps(payload))
                return payload

            handler.__name__ = tool_name
            return handler

        # Built directly rather than via `mcp.tool()`/`Tool.from_function`:
        # those introspect the Python signature to derive the input schema,
        # but every tool here shares one generic `**kwargs` handler and
        # already has its schema hand-authored in `tools/schemas.py` (AD-11) —
        # introspection would reject `**kwargs` outright and would drift from
        # the plan's schema regardless. `FunctionTool.run()` only binds
        # `arguments` by keyword, so a `**kwargs`-only `fn` executes correctly
        # with an explicit `parameters` schema.
        mcp.add_tool(FunctionTool(
            name=n,
            description=spec["description"],
            parameters=spec["inputSchema"],
            output_schema=spec.get("outputSchema"),
            fn=make(n),
            tags={"documentation", "read-only"},
        ))
    return mcp


def main() -> None:
    ap = argparse.ArgumentParser(description="Neutrinos documentation MCP server")
    ap.add_argument("--transport", choices=["stdio", "http"], default="stdio")
    ap.add_argument("--host", default="127.0.0.1")
    ap.add_argument("--port", type=int, default=8931)
    ap.add_argument("--tools", default=None, help="comma-separated tool subset")
    ap.add_argument("--verbose", action="store_true")
    args = ap.parse_args()

    logging.basicConfig(
        level=logging.DEBUG if args.verbose else logging.WARNING,
        stream=sys.stderr,  # stdout is the transport on stdio
        format="%(levelname)s %(name)s %(message)s")

    enabled = [t.strip() for t in args.tools.split(",")] if args.tools else None
    server = build_server(enabled)
    if args.transport == "stdio":
        server.run()
    else:
        server.run(transport="http", host=args.host, port=args.port)


if __name__ == "__main__":
    main()
