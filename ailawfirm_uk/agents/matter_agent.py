"""Matter agent — v0.1 stub. Full tracking in v0.2+."""


def handle(payload: str) -> dict:
    return {
        "agent": "matter_agent",
        "status": "v0.1 — stub",
        "action": "logged",
        "payload_preview": payload[:200],
    }
