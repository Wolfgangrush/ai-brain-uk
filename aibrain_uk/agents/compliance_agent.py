"""BSB AI Guidance Compliance Officer — expanded rule set (effective 18 May 2026).

Covers:
  - Original SRA Code §8 / BSB rC8 publicity firewall
  - Original UK GDPR + DPA 2018 + POCA flags
  - NEW: BSB AI Guidance rules — rC86 (outsourcing), rC86.3 (AI conditions),
    rC87/rC89 (practice management), rC9.1/rC9.2 (reckless misleading),
    rC15 (confidentiality), rC19 (transparency), rC20 (personal responsibility),
    rC123 (Public Access AI-reliance check)
  - NEW: All Core Duties CD1-CD10
  - NEW: Hamid jurisdiction case-law: Ayinde & Al-Haroun [2025] EWHC 1383 Admin,
    Munir [2026] UKUT 81 (IAC), Oakley v Information Commissioner [2024] UKFTT 315 (GRC)

PROVENANCE: BSB Artificial Intelligence Guidance May 2026, BSB Handbook,
    10-bar-rule-publicity-solicitation.md, 04-statute-data-protection.md,
    27-anti-money-laundering-obligations.md, 36-bar-rules-public-access.md
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional


# ── Core Duties (CD1-CD10) ────────────────────────────────────────────────
CORE_DUTIES: dict[str, str] = {
    "CD1": "You must observe your duty to the court in the administration of justice.",
    "CD2": "You must act in the best interests of each client.",
    "CD3": "You must act with honesty and integrity.",
    "CD4": "You must maintain your independence.",
    "CD5": "You must not behave in a way which is likely to diminish the trust and "
    "confidence which the public places in you or in the profession.",
    "CD6": "You must keep the affairs of each client confidential.",
    "CD7": "You must provide a competent standard of work and service to each client.",
    "CD8": "You must not discriminate unlawfully against any person.",
    "CD9": "You must be open and co-operative with your regulators.",
    "CD10": "You must take reasonable steps to manage your practice, or carry out "
    "your role within your practice, competently and in compliance with "
    "your legal and regulatory obligations.",
}

# ── AI-specific BSB rule references ───────────────────────────────────────
AI_RULES: dict[str, str] = {
    "rC86": "Outsourcing — barristers remain responsible for all outsourced activities. "
    "AI use MAY constitute outsourcing. Due diligence required.",
    "rC86.3": "Conditions for outsourcing — including AI: (a) no compromise of CD duties; "
    "(b) client consent where required; (c) adequate safeguards for "
    "confidentiality and data protection; (d) ability to override/monitor.",
    "rC87": "Practice management — chambers/practices must have effective systems "
    "including for AI use. Record-keeping of AI-assisted work.",
    "rC89": "Practice management — competence obligation extends to understanding "
    "and managing the technology you deploy.",
    "rC9.1": "You must not knowingly or recklessly mislead the court. AI-generated "
    "citations, authorities, or factual assertions must be independently verified.",
    "rC9.2": "You must not construct facts supporting your case knowing them to be "
    "untrue. AI hallucination is NOT a defence to rC9.2.",
    "rC15": "Client confidentiality — data entered into third-party AI tools may "
    "constitute disclosure. Local-first architecture preserves rC15. "
    "See Munir [2026] UKUT 81 (IAC).",
    "rC19": "Transparency — clients must be informed where AI materially impacts "
    "the delivery of services. Document disclosure in engagement letters.",
    "rC20": "Personal responsibility — you CANNOT delegate professional judgment "
    "to AI. Every AI-assisted output must be independently reviewed. "
    "See Ayinde & Al-Haroun [2025] EWHC 1383 Admin.",
    "rC123": "Public Access / Direct Access — lay clients may not understand AI "
    "limitations. Additional rC19 disclosure and rC20 verification "
    "obligations apply.",
}

# ── Case-law references (Hamid jurisdiction) ──────────────────────────────
AI_CASE_LAW: dict[str, str] = {
    "Ayinde & Al-Haroun [2025] EWHC 1383 Admin": (
        "Hamid jurisdiction — AI-generated authorities and submissions. Court "
        "emphasised rC20 personal responsibility: counsel MUST independently "
        "verify all AI output before submission. AI cannot be the 'author' of "
        "legal submissions."
    ),
    "Munir [2026] UKUT 81 (IAC)": (
        "Legal Professional Privilege (LPP) preserved by local-first AI "
        "architecture. Cloud AI tools that transmit data to third-party servers "
        "risk LPP waiver. Local-only deployment maintains privilege."
    ),
    "Oakley v Information Commissioner [2024] UKFTT 315 (GRC)": (
        "UK GDPR implications of AI data processing. Transparency obligations "
        "under Article 5(1)(a) UK GDPR apply to AI-assisted decision-making. "
        "Data subjects must be informed of AI processing of their personal data."
    ),
}

# ── BSB AI Guidance direct quotes ─────────────────────────────────────────
BSB_QUOTES: dict[str, str] = {
    "unlikely_public_ai": (
        "It is unlikely that free-of-charge, publicly available AI systems "
        "fulfil these conditions [rC86-89] for use with client-confidential or "
        "court-facing legal work."
    ),
    "risk_based_approach": (
        "The BSB expects barristers and chambers to adopt a risk-based approach "
        "to AI use, considering: the application (what it's used for), "
        "the nature of use (how it's used), and the technology (what tool)."
    ),
    "local_first_lpp": (
        "Where AI tools process data locally without transmission to third "
        "parties, the rC15 confidentiality and Legal Professional Privilege "
        "concerns are substantially mitigated."
    ),
}


@dataclass
class ComplianceFlags:
    """Result of compliance scan."""

    agent: str = "compliance_agent"
    status: str = "v0.2 — BSB AI Guidance expanded rule set"
    flags: list[dict] = field(default_factory=list)
    core_duties_implicated: list[str] = field(default_factory=list)
    case_law_relevant: list[str] = field(default_factory=list)
    direct_quote: Optional[str] = None


def handle(payload: str, context: Optional[dict] = None) -> dict:
    """Scan for BSB compliance flags including AI-specific rules.

    Args:
        payload: User input / prompt text
        context: Optional dict with keys like 'is_public_access', 'is_court_submission',
                 'ai_tool_type', 'contains_citations'

    Returns:
        ComplianceFlags as dict
    """
    p = payload.lower()
    ctx = context or {}
    flags: list[dict] = []
    duties: list[str] = []
    case_law: list[str] = []
    quote: Optional[str] = None

    # ── Original publicity / solicitation checks ──────────────────────────
    if any(k in p for k in ["solicit", "advertis", "promot", "publicity"]):
        flags.append(
            {
                "rule": "SRA Code of Conduct §8 / BSB rC8 — publicity restrictions",
                "research_ref": "10-bar-rule-publicity-solicitation.md",
                "severity": "medium",
            }
        )
        duties.append("CD5")

    # ── Original UK GDPR / data protection ────────────────────────────────
    if any(k in p for k in ["uk gdpr", "dpa 2018", "personal data", "data breach", "ico"]):
        flags.append(
            {
                "rule": "UK GDPR + DPA 2018 — note 72-hour ICO breach notification",
                "research_ref": "04-statute-data-protection.md",
                "severity": "high",
            }
        )
        duties.extend(["CD6", "CD9", "CD10"])

    if any(k in p for k in ["data use", "data access act", "duaa"]):
        flags.append(
            {
                "rule": "Data (Use and Access) Act 2025 — CURRENCY check vs prior DPA 2018",
                "research_ref": "04-statute-data-protection.md",
                "severity": "medium",
            }
        )

    # ── Original AML / POCA ────────────────────────────────────────────────
    if any(k in p for k in ["aml", "poca", "money laundering", "mlr 2017", "kyc"]):
        flags.append(
            {
                "rule": "POCA 2002 + MLR 2017 + ECCTA 2023 phase-in",
                "research_ref": "27-anti-money-laundering-obligations.md",
                "severity": "high",
            }
        )
        duties.append("CD3")

    if any(k in p for k in ["client money", "accounts rules", "client account"]):
        flags.append(
            {
                "rule": "SRA Accounts Rules — client money compliance gate",
                "research_ref": "44-bar-rule-client-money.md",
                "severity": "high",
            }
        )

    # ── NEW: AI-specific checks ───────────────────────────────────────────
    # AI outsourcing (rC86 / rC86.3)
    if any(
        k in p
        for k in [
            "ai",
            "artificial intelligence",
            "language model",
            "llm",
            "gpt",
            "claude",
            "chatgpt",
            "copilot",
            "gemini",
            "deepseek",
            "ollama",
            "qwen",
        ]
    ):
        flags.append(
            {
                "rule": "rC86 + rC86.3 — AI use may constitute outsourcing. "
                "Due diligence + client consent + confidentiality safeguards required.",
                "research_ref": "BSB AI Guidance May 2026, Part B",
                "severity": "high",
            }
        )
        duties.extend(["CD6", "CD7", "CD10"])
        quote = BSB_QUOTES["unlikely_public_ai"]

    # Cloud AI / data exfiltration risk (rC15)
    if any(
        k in p
        for k in [
            "cloud",
            "api",
            "openai",
            "anthropic",
            "google",
            "deepseek api",
            "chatgpt",
            "claude.ai",
            "copilot",
        ]
    ):
        flags.append(
            {
                "rule": "rC15 — Cloud AI services may constitute unauthorised disclosure. "
                "Client-confidential data must not be transmitted to third-party "
                "AI providers without adequate safeguards. See Munir [2026] UKUT 81 (IAC).",
                "research_ref": "BSB AI Guidance May 2026, rC15 + Munir",
                "severity": "critical",
            }
        )
        duties.append("CD6")
        case_law.append("Munir [2026] UKUT 81 (IAC)")

    # AI-generated content / rC9.1, rC9.2
    if any(
        k in p
        for k in ["ai-generat", "ai generat", "ai wrote", "ai draft", "auto-generat", "hallucinat"]
    ):
        flags.append(
            {
                "rule": "rC9.1 + rC9.2 — AI-generated content must be independently verified. "
                "Hallucinated citations/authorities = reckless misleading of the court. "
                "See Ayinde & Al-Haroun [2025] EWHC 1383 Admin.",
                "research_ref": "BSB AI Guidance May 2026, rC9.1-9.2 + Ayinde/Al-Haroun",
                "severity": "critical",
            }
        )
        duties.extend(["CD1", "CD3", "CD7"])
        case_law.append("Ayinde & Al-Haroun [2025] EWHC 1383 Admin")

    # Public Access + AI (rC123)
    if ctx.get("is_public_access") or any(
        k in p for k in ["public access", "direct access", "lay client"]
    ):
        flags.append(
            {
                "rule": "rC123 — Public Access lay clients require additional AI disclosure. "
                "Confirm client understands AI involvement and limitations.",
                "research_ref": "BSB AI Guidance May 2026, rC123 + 36-bar-rules-public-access.md",
                "severity": "high",
            }
        )
        duties.extend(["CD2", "CD7", "CD10"])

    # Court submissions + AI (rC9.1/rC9.2 + Hamid)
    if ctx.get("is_court_submission") or any(
        k in p
        for k in [
            "skeleton",
            "pleading",
            "submission",
            "court",
            "hearing",
            "trial",
            "witness statement",
            "particulars of claim",
        ]
    ):
        flags.append(
            {
                "rule": "rC9.1 + rC9.2 + Hamid jurisdiction — Court submissions involving AI "
                "trigger heightened verification obligations. Counsel must certify "
                "personal review of all AI-assisted content.",
                "research_ref": "Ayinde & Al-Haroun [2025] EWHC 1383 Admin",
                "severity": "critical",
            }
        )
        duties.extend(["CD1", "CD3"])
        case_law.append("Ayinde & Al-Haroun [2025] EWHC 1383 Admin")

    # Transparency (rC19)
    if ctx.get("is_client_facing") or any(
        k in p for k in ["client", "advice", "opinion", "deliverable", "engagement letter"]
    ):
        flags.append(
            {
                "rule": "rC19 — Client must be informed where AI materially impacts "
                "service delivery. Document in engagement letter / client care letter.",
                "research_ref": "BSB AI Guidance May 2026, rC19",
                "severity": "medium",
            }
        )
        duties.append("CD2")

    # Personal responsibility (rC20) — always flagged when AI is in use
    if any(k in p for k in ["ai", "auto", "agent", "draft", "generat"]):
        flags.append(
            {
                "rule": "rC20 — Personal responsibility CANNOT be delegated to AI. "
                "Every AI-assisted output must be independently reviewed by counsel.",
                "research_ref": "BSB AI Guidance May 2026, rC20",
                "severity": "high",
            }
        )

    # Oakley — UK GDPR + AI
    if any(
        k in p
        for k in [
            "data subject",
            "subject access",
            "sar",
            "dsar",
            "ico complaint",
            "information commissioner",
        ]
    ):
        case_law.append("Oakley v Information Commissioner [2024] UKFTT 315 (GRC)")

    # LPP concerns
    if any(
        k in p
        for k in [
            "privilege",
            "lpp",
            "legal professional privilege",
            "without prejudice",
            "confidential",
        ]
    ):
        flags.append(
            {
                "rule": "rC15 + LPP — Legal Professional Privilege preserved ONLY by "
                "local-first architecture. Cloud AI tools risk waiver. "
                "See Munir [2026] UKUT 81 (IAC).",
                "research_ref": "Munir [2026] UKUT 81 (IAC)",
                "severity": "critical",
            }
        )
        duties.append("CD6")
        case_law.append("Munir [2026] UKUT 81 (IAC)")

    # Deduplicate
    duties = list(dict.fromkeys(duties))
    case_law = list(dict.fromkeys(case_law))

    return {
        "agent": "compliance_agent",
        "status": "v0.2 — BSB AI Guidance May 2026 expanded rule set",
        "flags": flags,
        "core_duties_implicated": duties,
        "case_law_relevant": case_law,
        "direct_quote": quote,
    }


def get_rules_summary() -> dict:
    """Return a structured summary of all AI-relevant BSB rules."""
    return {
        "core_duties": CORE_DUTIES,
        "ai_rules": AI_RULES,
        "case_law": AI_CASE_LAW,
        "bsb_quotes": BSB_QUOTES,
        "effective_date": "2026-05-18",
        "guidance_title": "BSB Artificial Intelligence Guidance May 2026",
    }
