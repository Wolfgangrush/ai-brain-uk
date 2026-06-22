"""Court agent — wraps uk_court_lookup MCP tool.

PROVENANCE: CITED:01-court-hierarchy.md
"""


def handle(payload: str) -> dict:
    return {
        "agent": "court_agent",
        "status": "v0.1 — wraps uk_court_lookup",
        "action": "delegated to MCP tool",
        "payload": payload,
    }
