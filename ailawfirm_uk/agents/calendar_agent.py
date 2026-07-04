"""Calendar agent — wraps uk_calendar_sync MCP tool (ICS generation).

PROVENANCE: CITED:_RESEARCH_SUMMARY.md (ADR-002 pattern)
"""


def handle(payload: str) -> dict:
    return {
        "agent": "calendar_agent",
        "status": "v0.1 — wraps uk_calendar_sync",
        "action": "delegated to MCP tool",
        "payload": payload,
    }
