"""Keyword-based intent classifier — UK-specific rules (v0.2 BSB AI Guidance).

PROVENANCE: CITED:01-court-hierarchy.md, 10-bar-rule-publicity-solicitation.md,
    13-citation-format-primary.md, 04-statute-data-protection.md,
    BSB AI Guidance May 2026
"""

from ailawfirm_uk.brain.intents import Intent

_RULES: list[tuple[list[str], Intent]] = [
    (
        ["add to calendar", "schedule for", "remind me", "block out"],
        Intent.CALENDAR_ADD,
    ),
    (
        ["calendar", "schedule", "diary", "next week", "show today", "what's on"],
        Intent.CALENDAR_QUERY,
    ),
    (
        [
            "citation",
            "oscola",
            " ewca ",
            " ewhc ",
            " uksc ",
            " ac ",
            "cite",
            "cited",
            "verify citation",
            "check citation",
        ],
        Intent.CITATION_LOOKUP,
    ),
    (
        [
            "court",
            "jurisdiction",
            "high court",
            "crown court",
            "magistrates",
            "county court",
            "court of session",
            "court of appeal",
            "supreme court",
            "ukca",
            "uksc",
        ],
        Intent.COURT_QUERY,
    ),
    (
        [
            "draft",
            "drafting",
            "particulars of claim",
            "defence",
            "witness statement",
            "skeleton argument",
        ],
        Intent.DRAFTING_NEED,
    ),
    (
        [
            "deadline",
            "limitation",
            "time limit",
            "directions",
            "case management",
            "service deadline",
        ],
        Intent.DEADLINE_CHECK,
    ),
    (
        ["client said", "client called", "client wants"],
        Intent.CLIENT_COMM,
    ),
    (
        [
            "sra",
            "bsb",
            "rule 8",
            "rc8",
            "publicity",
            "solicit",
            "advertis",
            "ico",
            "uk gdpr",
            "dpa 2018",
            "aml",
            "poca",
            "mlr 2017",
            "accounts rules",
            "ai compliance",
            "ai guidance",
            "rc86",
            "rc89",
            "rc9",
            "rc15",
            "rc19",
            "rc20",
        ],
        Intent.COMPLIANCE_FLAG,
    ),
    (
        ["public access", "direct access", "lay client", "rc123"],
        Intent.DIRECT_ACCESS_CHECK,
    ),
    (
        ["risk", "risk assessment", "bsb risk", "classify risk", "risk level"],
        Intent.RISK_ASSESSMENT,
    ),
    (
        ["audit log", "audit trail", "show logs", "retention", "audit query"],
        Intent.AUDIT_QUERY,
    ),
    (
        [
            "transparency",
            "disclose ai",
            "client informed",
            "rc19 disclosure",
            "inform client",
        ],
        Intent.TRANSPARENCY_GATE,
    ),
    (
        ["matter", "hearing", "filed", "order received", "argued"],
        Intent.MATTER_UPDATE,
    ),
]


def classify(payload: str) -> Intent:
    """Classify a user utterance into one of 14 intent classes."""
    p = payload.lower()
    for keywords, intent in _RULES:
        for kw in keywords:
            if kw in p:
                return intent
    return Intent.UNKNOWN
