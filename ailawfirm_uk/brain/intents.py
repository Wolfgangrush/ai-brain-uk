"""Intent classes for the UK Solo brain classifier (v0.2 — 14 classes)."""

from enum import Enum


class Intent(Enum):
    MATTER_UPDATE = "matter_update"
    CITATION_LOOKUP = "citation_lookup"
    COURT_QUERY = "court_query"
    DRAFTING_NEED = "drafting_need"
    DEADLINE_CHECK = "deadline_check"
    CLIENT_COMM = "client_comm"
    COMPLIANCE_FLAG = "compliance_flag"
    CALENDAR_QUERY = "calendar_query"
    CALENDAR_ADD = "calendar_add"
    RISK_ASSESSMENT = "risk_assessment"
    TRANSPARENCY_GATE = "transparency_gate"
    DIRECT_ACCESS_CHECK = "direct_access_check"
    AUDIT_QUERY = "audit_query"
    UNKNOWN = "unknown"
