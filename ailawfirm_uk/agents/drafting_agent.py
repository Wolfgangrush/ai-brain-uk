"""Drafting agent — v0.1 stub. Drafting assistance in v0.2+."""


def handle(payload: str) -> dict:
    return {
        "agent": "drafting_agent",
        "status": "v0.1 — stub",
        "action": "acknowledged",
        "note": "Drafting assistance ships in v0.2",
        "payload_preview": payload[:200],
    }
