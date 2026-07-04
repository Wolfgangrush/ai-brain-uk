"""BSB AI Guidance risk-based approach — 3x3 matrix (effective 18 May 2026).

Implements the BSB's three-axis risk classification:
  - Application axis: admin (low) / general client (medium) / court submissions +
    vulnerable + protected characteristics (high)
  - Use axis: spelling-grammar (low) / legal research (medium) / text generation +
    drafting + automated/agentic (high)
  - Technology axis: spelling tools (low) / legal-specific AI in secure env (medium) /
    agentic + general-purpose without data protections (high)

Each session is auto-classified, logged to audit trail, and the user is warned
on high-risk combinations.

PROVENANCE: BSB Artificial Intelligence Guidance May 2026, Part B (Risk-Based Approach)
"""

from __future__ import annotations

import json
import time
from dataclasses import dataclass, field
from enum import Enum
from pathlib import Path
from typing import Optional


class RiskLevel(Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"


class ApplicationAxis(Enum):
    """BSB Application axis — what the AI is being used for."""

    ADMIN = ("admin", RiskLevel.LOW)
    GENERAL_CLIENT = ("general_client", RiskLevel.MEDIUM)
    COURT_SUBMISSIONS = ("court_submissions", RiskLevel.HIGH)
    VULNERABLE = ("vulnerable", RiskLevel.HIGH)
    PROTECTED_CHARACTERISTICS = ("protected_characteristics", RiskLevel.HIGH)

    def __init__(self, label: str, risk: RiskLevel):
        self.label = label
        self.risk = risk


class UseAxis(Enum):
    """BSB Use axis — how the AI is being used."""

    SPELLING_GRAMMAR = ("spelling_grammar", RiskLevel.LOW)
    LEGAL_RESEARCH = ("legal_research", RiskLevel.MEDIUM)
    TEXT_GENERATION = ("text_generation", RiskLevel.HIGH)
    DRAFTING = ("drafting", RiskLevel.HIGH)
    AUTOMATED_AGENTIC = ("automated_agentic", RiskLevel.HIGH)

    def __init__(self, label: str, risk: RiskLevel):
        self.label = label
        self.risk = risk


class TechnologyAxis(Enum):
    """BSB Technology axis — what tool is being used."""

    SPELLING_TOOLS = ("spelling_tools", RiskLevel.LOW)
    LEGAL_SPECIFIC_AI_SECURE = ("legal_specific_ai_secure", RiskLevel.MEDIUM)
    AGENTIC_GENERAL_PURPOSE_NO_PROTECTION = (
        "agentic_general_purpose_no_protection",
        RiskLevel.HIGH,
    )

    def __init__(self, label: str, risk: RiskLevel):
        self.label = label
        self.risk = risk


# Keyword classifiers for each axis
_APPLICATION_KEYWORDS: list[tuple[list[str], ApplicationAxis]] = [
    (["admin", "calendar", "schedule", "diary", "filing", "time recording"], ApplicationAxis.ADMIN),
    (
        ["client", "advice", "opinion", "letter", "correspondence", "conference"],
        ApplicationAxis.GENERAL_CLIENT,
    ),
    (
        [
            "court",
            "submission",
            "skeleton",
            "pleading",
            "particulars of claim",
            "defence",
            "witness statement",
            "hearing",
            "bundle",
            "trial",
        ],
        ApplicationAxis.COURT_SUBMISSIONS,
    ),
    (
        ["vulnerable", "child", "protected party", "litigation friend", "mental capacity"],
        ApplicationAxis.VULNERABLE,
    ),
    (
        [
            "discrimination",
            "equality act",
            "protected characteristic",
            "disability",
            "race",
            "religion",
            "sex",
            "sexual orientation",
            "age",
            "gender reassignment",
            "marriage",
            "pregnancy",
            "maternity",
        ],
        ApplicationAxis.PROTECTED_CHARACTERISTICS,
    ),
]

_USE_KEYWORDS: list[tuple[list[str]], UseAxis] = [
    (["spell", "grammar", "proofread", "typo", "format"], UseAxis.SPELLING_GRAMMAR),
    (
        ["research", "search", "find case", "look up", "statute", "legislation"],
        UseAxis.LEGAL_RESEARCH,
    ),
    (
        ["draft", "write", "generate", "compose", "text", "paragraph"],
        UseAxis.TEXT_GENERATION,
    ),
    (
        ["drafting", "pleading", "particulars", "skeleton argument", "opinion"],
        UseAxis.DRAFTING,
    ),
    (
        ["auto", "agent", "bulk", "batch", "autonomous", "agentic"],
        UseAxis.AUTOMATED_AGENTIC,
    ),
]

_TECHNOLOGY_KEYWORDS: list[tuple[list[str], TechnologyAxis]] = [
    (["spell check", "grammarly", "spelling tool"], TechnologyAxis.SPELLING_TOOLS),
    (
        ["local", "ollama", "qwen", "offline", "air-gapped", "ailawfirm"],
        TechnologyAxis.LEGAL_SPECIFIC_AI_SECURE,
    ),
    (
        [
            "chatgpt",
            "claude.ai",
            "gemini",
            "copilot",
            "bard",
            "deepseek",
            "cloud",
            "openai",
            "anthropic",
            "google ai",
        ],
        TechnologyAxis.AGENTIC_GENERAL_PURPOSE_NO_PROTECTION,
    ),
]


@dataclass
class RiskClassification:
    """Result of classifying a session across all three BSB axes."""

    application: ApplicationAxis = ApplicationAxis.ADMIN
    use: UseAxis = UseAxis.SPELLING_GRAMMAR
    technology: TechnologyAxis = TechnologyAxis.LEGAL_SPECIFIC_AI_SECURE
    overall_risk: RiskLevel = RiskLevel.LOW
    warnings: list[str] = field(default_factory=list)
    timestamp: str = field(default_factory=lambda: time.strftime("%Y-%m-%dT%H:%M:%S"))

    def to_dict(self) -> dict:
        return {
            "application": self.application.label,
            "application_risk": self.application.risk.value,
            "use": self.use.label,
            "use_risk": self.use.risk.value,
            "technology": self.technology.label,
            "technology_risk": self.technology.risk.value,
            "overall_risk": self.overall_risk.value,
            "warnings": self.warnings,
            "timestamp": self.timestamp,
        }


def _classify_axis(payload: str, keyword_map: list[tuple[list[str], any]]) -> any:
    """Match payload against keyword lists; return the highest-risk match."""
    p = payload.lower()
    best = None
    best_risk = RiskLevel.LOW
    for keywords, axis_val in keyword_map:
        for kw in keywords:
            if kw in p:
                if axis_val.risk.value == "high" or (
                    best_risk == RiskLevel.LOW and axis_val.risk.value == "medium"
                ):
                    best = axis_val
                    best_risk = axis_val.risk
    return best


def _compute_overall(app_risk: RiskLevel, use_risk: RiskLevel, tech_risk: RiskLevel) -> RiskLevel:
    """BSB overall risk: highest of the three axes wins."""
    risks = [app_risk, use_risk, tech_risk]
    if RiskLevel.HIGH in risks:
        return RiskLevel.HIGH
    if RiskLevel.MEDIUM in risks:
        return RiskLevel.MEDIUM
    return RiskLevel.LOW


def _generate_warnings(
    app: ApplicationAxis, use: UseAxis, tech: TechnologyAxis, overall: RiskLevel
) -> list[str]:
    warnings: list[str] = []
    if overall == RiskLevel.HIGH:
        warnings.append(
            "BSB HIGH RISK: rC86 outsourcing conditions may not be met. "
            "Ensure rC20 personal responsibility — AI output must be independently verified. "
            "Consider whether rC19 transparency disclosure to client is required."
        )
    if app == ApplicationAxis.COURT_SUBMISSIONS:
        warnings.append(
            "COURT SUBMISSION: rC9.1 / rC9.2 — AI-generated content in court documents "
            "carries heightened risk of misleading the court. Verify ALL citations, "
            "authorities, and factual assertions independently. See Ayinde & Al-Haroun "
            "[2025] EWHC 1383 Admin."
        )
    if app == ApplicationAxis.VULNERABLE:
        warnings.append(
            "VULNERABLE CLIENT/PARTY: Heightened rC15 confidentiality and rC19 "
            "transparency obligations apply. Confirm AI disclosure to client/litigation friend."
        )
    if app == ApplicationAxis.PROTECTED_CHARACTERISTICS:
        warnings.append(
            "PROTECTED CHARACTERISTICS: AI bias risk elevated. Verify output does not "
            "introduce or amplify discrimination contrary to Equality Act 2010."
        )
    if use == UseAxis.AUTOMATED_AGENTIC:
        warnings.append(
            "AGENTIC/AUTOMATED USE: rC20 — personal responsibility CANNOT be delegated to AI. "
            "Human-in-the-loop confirmation required before any output is relied upon. "
            "See Ayinde & Al-Haroun [2025] EWHC 1383 Admin."
        )
    if tech == TechnologyAxis.AGENTIC_GENERAL_PURPOSE_NO_PROTECTION:
        warnings.append(
            "UNPROTECTED TECHNOLOGY: BSB guidance states it is 'unlikely that "
            "free-of-charge, publicly available AI systems fulfil' rC86-89 conditions. "
            "Client data must not be entered into general-purpose cloud AI tools. "
            "See rC15 (confidentiality) and Munir [2026] UKUT 81 (IAC) on LPP preservation."
        )
    return warnings


def classify_session(
    payload: str,
    audit_log_dir: Optional[str] = None,
) -> RiskClassification:
    """Classify a user session across all three BSB axes and log to audit trail.

    Args:
        payload: The user's input/prompt text
        audit_log_dir: Directory for audit log output (default: ~/.ailawfirm_uk/audit_logs/)

    Returns:
        RiskClassification with overall risk level and warnings
    """
    app = _classify_axis(payload, _APPLICATION_KEYWORDS) or ApplicationAxis.ADMIN
    use = _classify_axis(payload, _USE_KEYWORDS) or UseAxis.SPELLING_GRAMMAR
    tech = _classify_axis(payload, _TECHNOLOGY_KEYWORDS) or TechnologyAxis.LEGAL_SPECIFIC_AI_SECURE

    overall = _compute_overall(app.risk, use.risk, tech.risk)
    warnings = _generate_warnings(app, use, tech, overall)

    classification = RiskClassification(
        application=app,
        use=use,
        technology=tech,
        overall_risk=overall,
        warnings=warnings,
    )

    # Log to audit trail
    _log_risk_classification(classification, audit_log_dir)

    return classification


def _log_risk_classification(
    classification: RiskClassification,
    audit_log_dir: Optional[str] = None,
) -> None:
    """Write risk classification to audit log."""
    log_dir = Path(audit_log_dir or "~/.ailawfirm_uk/audit_logs/").expanduser()
    log_dir.mkdir(parents=True, exist_ok=True)

    log_entry = {
        "type": "risk_classification",
        **classification.to_dict(),
    }

    date_str = time.strftime("%Y-%m-%d")
    log_file = log_dir / f"risk_log_{date_str}.jsonl"

    with open(log_file, "a") as f:
        f.write(json.dumps(log_entry, default=str) + "\n")
