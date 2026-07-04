"""Routes classified intents to specialist agents — v0.2 BSB AI Guidance."""

from __future__ import annotations

import importlib
from typing import Any, Dict

from ailawfirm_uk.brain.intents import Intent


# ---------------------------------------------------------------------------
# Routing map
# ---------------------------------------------------------------------------
# Each Intent value maps to the module name in ailawfirm_uk/agents/ that
# should handle it. Kept in sync with the actual agent modules on disk.

_ROUTE_MAP: dict[Intent, str] = {
    Intent.MATTER_UPDATE: "matter_agent",
    Intent.CITATION_LOOKUP: "citation_agent",
    Intent.COURT_QUERY: "court_agent",
    Intent.DRAFTING_NEED: "drafting_agent",
    Intent.DEADLINE_CHECK: "deadline_agent",
    Intent.CLIENT_COMM: "matter_agent",
    Intent.COMPLIANCE_FLAG: "compliance_agent",
    Intent.CALENDAR_QUERY: "calendar_agent",
    Intent.CALENDAR_ADD: "calendar_agent",
    Intent.RISK_ASSESSMENT: "matter_agent",
    Intent.TRANSPARENCY_GATE: "matter_agent",
    Intent.DIRECT_ACCESS_CHECK: "matter_agent",
    Intent.AUDIT_QUERY: "matter_agent",
    Intent.UNKNOWN: "matter_agent",
}


def route(intent: Intent) -> str:
    """Return the agent module name for a given intent."""
    return _ROUTE_MAP.get(intent, "matter_agent")


def _call_agent(agent_module_name: str, payload: str) -> Dict[str, Any]:
    """Import the agent module and invoke its handle() function.

    Returns a structured dict the brain can serialise. Never raises — any
    failure becomes a clean ok=False response so the front-end can keep
    running.
    """
    full_module = f"ailawfirm_uk.agents.{agent_module_name}"
    try:
        mod = importlib.import_module(full_module)
        handler = getattr(mod, "handle", None)
        if handler is None:
            return {
                "ok": False,
                "intent": None,
                "agent": agent_module_name,
                "error": f"agent module {full_module} has no handle() function",
            }
        result = handler(payload)
        return {
            "ok": True,
            "intent": None,
            "agent": agent_module_name,
            "result": result,
        }
    except ImportError as exc:
        return {
            "ok": False,
            "intent": None,
            "agent": agent_module_name,
            "error": f"agent module import failed: {exc}",
        }


def think(text: str) -> Dict[str, Any]:
    """Classify, route, and (when a host LLM is available) answer.

    The user-facing brain entry point. Mirrors the India reference's
    pattern: classify -> dispatch to the matched agent's handle() ->
    enrich with the specialist prompt's AI answer when ANTHROPIC_*
    env vars are present.

    Offline-safe: when no LLM host is configured, specialists.answer()
    returns None and the structured engine result is returned unchanged.
    """
    # Local import keeps the import-time graph small and avoids any
    # circular-import risk between classifier / router / specialists.
    from ailawfirm_uk.brain.classifier import classify
    from ailawfirm_uk.brain import specialists

    intent = classify(text)
    response = _call_agent(route(intent), text)
    response["intent"] = intent.value

    # AI-backed specialist answer — only attached when the host LLM is
    # actually reachable. Wrapped in try/except so an LLM transport
    # failure never breaks the deterministic structured response.
    try:
        grounding = response.get("result", {}) if isinstance(response, dict) else {}
        ai = specialists.answer(intent.value, text, grounding)
        if ai:
            response["answer"] = ai
    except Exception:
        # Offline fallback already in place — nothing to do.
        pass

    return response
