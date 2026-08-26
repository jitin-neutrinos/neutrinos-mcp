"""RFC 7807 problem payloads (plan §8.1, §8.5.1).

Errors are instructions. A tool error that says only "not found" costs the
agent a turn; one that names the values that WOULD have matched lets it retry
correctly. Every not-found here carries `suggestions`.
"""

from __future__ import annotations

BASE = "https://neutrinos-mcp/errors"


class KBError(Exception):
    """Carries an RFC 7807 payload. Surfaced as an isError tool result, never
    as a transport error — one bad call must not kill the session (§8.4)."""

    def __init__(self, kind: str, title: str, status: int, detail: str,
                 suggestions: list[dict] | None = None):
        super().__init__(detail)
        self.kind = kind
        self.title = title
        self.status = status
        self.detail = detail
        self.suggestions = suggestions or []

    def to_dict(self) -> dict:
        out = {"type": f"{BASE}/{self.kind}", "title": self.title,
               "status": self.status, "detail": self.detail}
        if self.suggestions:
            out["suggestions"] = self.suggestions
        return out


def not_found(what: str, detail: str, suggestions: list[dict] | None = None) -> KBError:
    return KBError(f"{what}-not-found", f"{what.replace('-', ' ').title()} Not Found",
                   404, detail, suggestions)


def invalid(detail: str, suggestions: list[dict] | None = None) -> KBError:
    return KBError("invalid-argument", "Invalid Argument", 422, detail, suggestions)


def unavailable(detail: str) -> KBError:
    return KBError("index-unavailable", "Index Unavailable", 503, detail)
