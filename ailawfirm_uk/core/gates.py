"""BSB AI Guidance gates — transparency, human-in-the-loop, direct access, LPP firewall.

Implements the mandatory control gates required by BSB AI Guidance (effective 18 May 2026):
  - rC19 Transparency Gate: client disclosure before any client-facing artifact
  - rC20 Human-in-the-Loop: confirmation required for all drafting/agentic actions
  - rC123 Direct Access: lay-client AI reliance check
  - LPP Firewall: architectural confirmation that data stays local

PROVENANCE: BSB AI Guidance May 2026,
    Ayinde & Al-Haroun [2025] EWHC 1383 Admin,
    Munir [2026] UKUT 81 (IAC)
"""

from __future__ import annotations

import json
from dataclasses import dataclass, field
from datetime import datetime, timezone
from enum import Enum
from pathlib import Path
from typing import Optional


# ── Transparency Gate (rC19) ──────────────────────────────────────────────

TRANSPARENCY_PROMPT = (
    "Has the client been informed of AI use per rC19? [y/N] "
    "(BSB rC19: clients must be informed where AI materially impacts "
    "the delivery of services. Document in engagement letter.)"
)


class TransparencyResponse(Enum):
    CONFIRMED = "confirmed"
    DENIED = "denied"
    PENDING = "pending"


@dataclass
class TransparencyGateResult:
    response: TransparencyResponse = TransparencyResponse.PENDING
    timestamp: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())
    artifact_description: str = ""
    user_response: str = ""


def transparency_gate(artifact_description: str = "") -> TransparencyGateResult:
    """rC19 gate: prompt user to confirm client has been informed of AI use.

    This gate fires before any client-facing artifact (draft, opinion, advice document)
    is finalised. The response is logged to the audit trail.

    Args:
        artifact_description: Description of the client-facing artifact

    Returns:
        TransparencyGateResult for logging
    """
    return TransparencyGateResult(
        response=TransparencyResponse.PENDING,
        artifact_description=artifact_description,
    )


def log_transparency_response(
    result: TransparencyGateResult,
    user_response: str,
    audit_log_dir: Optional[str] = None,
) -> dict:
    """Log the user's transparency gate response to audit trail."""
    confirmed = user_response.strip().lower() in ("y", "yes")
    result.user_response = user_response
    result.response = TransparencyResponse.CONFIRMED if confirmed else TransparencyResponse.DENIED

    log_dir = Path(audit_log_dir or "~/.ailawfirm_uk/audit_logs/").expanduser()
    log_dir.mkdir(parents=True, exist_ok=True)

    entry = {
        "type": "transparency_gate",
        "timestamp": result.timestamp,
        "artifact_description": result.artifact_description,
        "response": result.response.value,
        "rule": "rC19",
    }

    date_str = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    log_file = log_dir / f"transparency_{date_str}.jsonl"

    with open(log_file, "a") as f:
        f.write(json.dumps(entry, default=str) + "\n")

    return entry


# ── Human-in-the-Loop Gate (rC20) ─────────────────────────────────────────

HITL_PROMPT = (
    "HUMAN-IN-THE-LOOP CHECK (rC20): Confirm you have independently reviewed "
    "this AI output before reliance. This is a professional obligation — you "
    "cannot delegate judgment to AI. See Ayinde & Al-Haroun [2025] EWHC 1383 Admin. "
    "Confirm review? [y/N]"
)


@dataclass
class HITLResult:
    confirmed: bool = False
    timestamp: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())
    action_type: str = ""
    user_response: str = ""


def human_in_the_loop_gate(action_type: str) -> HITLResult:
    """rC20 gate: every drafting/agentic action requires explicit user confirmation.

    No bulk-execute. No auto-emit. Reference: Ayinde & Al-Haroun [2025] EWHC 1383 Admin.

    Args:
        action_type: Description of the action requiring confirmation

    Returns:
        HITLResult for logging
    """
    return HITLResult(action_type=action_type)


def log_hitl_response(
    result: HITLResult,
    user_response: str,
    audit_log_dir: Optional[str] = None,
) -> dict:
    """Log the human-in-the-loop response."""
    result.confirmed = user_response.strip().lower() in ("y", "yes")
    result.user_response = user_response

    log_dir = Path(audit_log_dir or "~/.ailawfirm_uk/audit_logs/").expanduser()
    log_dir.mkdir(parents=True, exist_ok=True)

    entry = {
        "type": "human_in_the_loop",
        "timestamp": result.timestamp,
        "action_type": result.action_type,
        "confirmed": result.confirmed,
        "rule": "rC20",
        "precedent": "Ayinde & Al-Haroun [2025] EWHC 1383 Admin",
    }

    date_str = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    log_file = log_dir / f"audit_{date_str}.jsonl"

    with open(log_file, "a") as f:
        f.write(json.dumps(entry, default=str) + "\n")

    return entry


# ── Direct Access Detector (rC123) ────────────────────────────────────────

R123_PROMPT = (
    "PUBLIC ACCESS / DIRECT ACCESS DETECTED (rC123): Lay clients may not "
    "understand AI limitations. Confirm the client has been informed of AI "
    "involvement in their matter and understands AI's role and limitations. "
    "Has this disclosure been made? [y/N]"
)


@dataclass
class DirectAccessResult:
    confirmed: bool = False
    timestamp: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())
    matter_id: str = ""


def direct_access_check(matter_id: str = "") -> DirectAccessResult:
    """rC123 routine: if matter is marked as Public Access/Direct Access,
    trigger confirmation that client understands AI involvement.

    Args:
        matter_id: Matter reference

    Returns:
        DirectAccessResult for logging
    """
    return DirectAccessResult(matter_id=matter_id)


def log_direct_access_response(
    result: DirectAccessResult,
    user_response: str,
    audit_log_dir: Optional[str] = None,
) -> dict:
    """Log the direct access AI disclosure confirmation."""
    result.confirmed = user_response.strip().lower() in ("y", "yes")

    log_dir = Path(audit_log_dir or "~/.ailawfirm_uk/audit_logs/").expanduser()
    log_dir.mkdir(parents=True, exist_ok=True)

    entry = {
        "type": "direct_access_check",
        "timestamp": result.timestamp,
        "matter_id": result.matter_id,
        "confirmed": result.confirmed,
        "rule": "rC123",
    }

    date_str = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    log_file = log_dir / f"audit_{date_str}.jsonl"

    with open(log_file, "a") as f:
        f.write(json.dumps(entry, default=str) + "\n")

    return entry


# ── LPP Firewall ──────────────────────────────────────────────────────────

LPP_LOCAL_MODE_MESSAGE = (
    "LPP FIREWALL · LOCAL MODE: Confidential client data does not leave the "
    "local environment in this configuration. Ollama + Qwen3 run on this laptop. "
    "Munir [2026] UKUT 81 (IAC) LPP-preservation considerations are satisfied "
    "by absence of cross-vendor transmission. Free/public cloud AI tools cannot "
    "make this claim."
)

LPP_CLOUD_MODE_MESSAGE_TEMPLATE = (
    "LPP FIREWALL · CLOUD MODE ({provider}): Prompts will be transmitted to "
    "{provider} after Pseudonymisation Gateway sanitisation (party names, "
    "government IDs, case references substituted with deterministic placeholders "
    "before transmission). Cloud vendor sees only abstract matter structure. "
    "You retain Munir [2026] UKUT 81 (IAC) LPP responsibility — verify your "
    "vendor DPA, Article 28 obligations, and any UK GDPR Schedule 21 "
    "supplementary safeguards are in place before invoking cloud mode for "
    "privileged work."
)

# Kept for backwards compatibility with any consumer that imports this constant.
LPP_FIREWALL_MESSAGE = LPP_LOCAL_MODE_MESSAGE


def _read_provider_from_config() -> str:
    """Read the configured llm_provider from ~/.ailawfirm_uk/config.json.

    Returns 'local' (default) if no config exists, or if ai_provider/llm_provider
    is 'ollama' / 'local' / unset. Returns the provider name
    (anthropic/openai/google/deepseek) if a cloud provider is configured.
    """
    config_path = Path.home() / ".ailawfirm_uk" / "config.json"
    if not config_path.exists():
        # Fallback to the legacy lowercase-hyphen path some installs used.
        legacy_path = Path.home() / ".ailawfirm-uk" / "config.json"
        if not legacy_path.exists():
            return "local"
        config_path = legacy_path
    try:
        cfg = json.loads(config_path.read_text())
        provider = (cfg.get("ai_provider") or cfg.get("llm_provider") or "local").lower()
        if provider in ("ollama", "local", ""):
            return "local"
        return provider
    except (OSError, json.JSONDecodeError):
        return "local"


def lpp_firewall_check() -> dict:
    """Return the LPP firewall status — runtime check of configured LLM provider.

    Reads the user's config.json and reports honestly whether the tool is in
    local mode (data does not leave the machine) or cloud mode (PII is sanitised
    via Pseudonymisation Gateway before transmission; user retains LPP
    responsibility).

    NOT an architectural guarantee in cloud mode — the Gateway sanitisation is
    structural, but the user remains responsible for vendor DPA + UK GDPR
    Schedule 21 supplementary safeguards.
    """
    provider = _read_provider_from_config()
    if provider == "local":
        return {
            "status": "active",
            "mode": "local",
            "provider": "ollama (or v0.1 keyword-matching brain · no LLM)",
            "data_transmission": "none",
            "lpp_preserved_by": "architecture (absence of cross-vendor transmission)",
            "precedent": "Munir [2026] UKUT 81 (IAC)",
            "message": LPP_LOCAL_MODE_MESSAGE,
            "user_obligations_remaining": (
                "Standard SRA Rule 6.3 / BSB rC15 client-confidentiality "
                "obligations in your conduct of the matter."
            ),
        }
    return {
        "status": "active",
        "mode": "cloud",
        "provider": provider,
        "data_transmission": (
            "via Pseudonymisation Gateway (placeholders substituted before "
            "transmission to "
            f"{provider})"
        ),
        "lpp_preserved_by": (
            "Gateway sanitisation + your vendor DPA + your UK GDPR Schedule 21 "
            "supplementary safeguards"
        ),
        "precedent": "Munir [2026] UKUT 81 (IAC)",
        "message": LPP_CLOUD_MODE_MESSAGE_TEMPLATE.format(provider=provider),
        "user_obligations_remaining": (
            f"Execute {provider}'s DPA / Article 28 contract. Implement UK GDPR "
            f"Schedule 21 supplementary safeguards if {provider}'s servers are "
            "outside UK ICO-adequate jurisdictions. Verify Pseudonymisation "
            "Gateway coverage of your matter's specific identifiers."
        ),
    }


# ── Session Startup Compliance Banner ──────────────────────────────────────

SESSION_BANNER_LOCAL = """
╔══════════════════════════════════════════════════════════════╗
║  BSB AI GUIDANCE (effective 18 May 2026) — ACTIVE           ║
║                                                            ║
║  LPP FIREWALL · LOCAL MODE                                  ║
║  Confidential client data does not leave this laptop in     ║
║  this configuration. Munir [2026] UKUT 81 (IAC) LPP        ║
║  considerations satisfied by absence of transmission.       ║
║                                                            ║
║  rC20: Personal responsibility — AI output MUST be          ║
║  independently verified before reliance.                    ║
║  See Ayinde & Al-Haroun [2025] EWHC 1383 Admin.            ║
║                                                            ║
║  Risk-based assessment: ACTIVE                             ║
║  AI audit log: ACTIVE (90-day retention)                    ║
║  Citation 2-source verification: ACTIVE                     ║
╚══════════════════════════════════════════════════════════════╝
"""

SESSION_BANNER_CLOUD_TEMPLATE = """
╔══════════════════════════════════════════════════════════════╗
║  BSB AI GUIDANCE (effective 18 May 2026) — ACTIVE           ║
║                                                            ║
║  LPP FIREWALL · CLOUD MODE ({provider:<20})        ║
║  Prompts will be transmitted to {provider:<24}      ║
║  AFTER Pseudonymisation Gateway sanitisation                ║
║  (party names · government IDs · case refs → placeholders). ║
║  You retain Munir [2026] UKUT 81 (IAC) LPP responsibility   ║
║  + vendor DPA + UK GDPR Schedule 21 supplementary safeguard.║
║                                                            ║
║  rC20: Personal responsibility — AI output MUST be          ║
║  independently verified before reliance.                    ║
║  See Ayinde & Al-Haroun [2025] EWHC 1383 Admin.            ║
║                                                            ║
║  Risk-based assessment: ACTIVE                             ║
║  AI audit log: ACTIVE (90-day retention)                    ║
║  Citation 2-source verification: ACTIVE                     ║
╚══════════════════════════════════════════════════════════════╝
"""


def session_banner() -> str:
    """Return the right session banner for the configured LLM provider."""
    provider = _read_provider_from_config()
    if provider == "local":
        return SESSION_BANNER_LOCAL
    return SESSION_BANNER_CLOUD_TEMPLATE.format(provider=provider)


# Kept for backwards compatibility — callers using SESSION_BANNER as a constant
# get the local-mode banner. New callers should call session_banner() to get the
# runtime-correct version.
SESSION_BANNER = SESSION_BANNER_LOCAL
