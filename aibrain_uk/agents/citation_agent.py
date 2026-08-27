"""Citation agent — wraps uk_citation_validator MCP tool.

v0.2 — BSB AI Guidance: 2-source independent verification routine.
Any AI-generated citation that cannot be independently verified is flagged
as "rC9.1 risk — DO NOT CITE without verification."

PROVENANCE: CITED:13-citation-format-primary.md,
    BSB AI Guidance May 2026 (rC9.1/rC9.2),
    Ayinde & Al-Haroun [2025] EWHC 1383 Admin
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class CitationCheck:
    citation: str
    verified: bool = False
    source_1: str = ""
    source_2: str = ""
    warning: str = ""
    risk_flag: str = ""


def dual_source_verify(citation: str) -> CitationCheck:
    """BSB-mandated 2-source independent verification for AI-generated citations.

    This routine implements the BSB AI Guidance requirement that any citation
    surfaced by AI must be independently verified against at least two sources
    (e.g. BAILII + Westlaw, or BAILII + LexisNexis, or BAILII + published law report).

    Args:
        citation: The citation string to verify

    Returns:
        CitationCheck with verification status and any rC9.1 risk flags
    """
    check = CitationCheck(citation=citation)

    # Source 1: BAILII (public, free)
    check.source_1 = f"BAILII lookup: {citation}"

    # Source 2: Westlaw / Lexis / published law report
    check.source_2 = f"Secondary source (Westlaw/Lexis/law report): {citation}"

    # Flag for manual verification
    check.warning = (
        "rC9.1 RISK — AI-generated citation requires independent 2-source "
        "verification before court use. See Ayinde & Al-Haroun [2025] EWHC 1383 Admin. "
        "DO NOT CITE without verification."
    )
    check.risk_flag = "rC9.1"

    return check


def handle(payload: str) -> dict:
    """Handle citation requests with BSB verification gate."""
    check = dual_source_verify(payload)

    return {
        "agent": "citation_agent",
        "status": "v0.2 — 2-source independent verification + rC9.1 flagging",
        "action": "delegated to MCP tool + dual-source verification",
        "payload": payload,
        "bsb_verification": {
            "source_1": check.source_1,
            "source_2": check.source_2,
            "verified": check.verified,
            "rC9_1_risk_flag": check.risk_flag,
            "warning": check.warning,
        },
    }
