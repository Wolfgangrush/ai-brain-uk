"""Routes classified intents to specialist agents — v0.2 BSB AI Guidance."""

from ailawfirm_uk.brain.intents import Intent


def route(intent: Intent) -> str:
    """Return the agent module name for a given intent."""
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
        Intent.RISK_ASSESSMENT: "risk_assessment",
        Intent.TRANSPARENCY_GATE: "transparency_gate",
        Intent.DIRECT_ACCESS_CHECK: "direct_access_check",
        Intent.AUDIT_QUERY: "audit_log",
        Intent.UNKNOWN: "matter_agent",
    }
    return _ROUTE_MAP.get(intent, "matter_agent")
