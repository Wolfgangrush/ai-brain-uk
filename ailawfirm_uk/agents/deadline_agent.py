"""Deadline agent — v0.1 stub. Limitation clock + directions tracking in v0.2+."""


def handle(payload: str) -> dict:
    return {
        "agent": "deadline_agent",
        "status": "v0.1 — stub",
        "action": "acknowledged",
        "note": "Deadline tracking ships in v0.2",
        "payload_preview": payload[:200],
    }
