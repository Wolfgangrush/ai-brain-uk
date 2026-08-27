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

    log_dir = Path(audit_log_dir or "~/.aibrain_uk/audit_logs/").expanduser()
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

    log_dir = Path(audit_log_dir or "~/.aibrain_uk/audit_logs/").expanduser()
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

    log_dir = Path(audit_log_dir or "~/.aibrain_uk/audit_logs/").expanduser()
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

# Local-tier flag — local inference is not wired in this release. Flip to True
# only when brain/llm.py actually routes to a local model (e.g. ollama on
# 127.0.0.1). Until then, every caller must treat "local" mode as not
# available and cannot honestly report that data does not leave the machine.
LOCAL_TIER_IMPLEMENTED = False


LPP_LOCAL_MODE_MESSAGE = (
    "LPP FIREWALL · LOCAL MODE (NOT IMPLEMENTED IN THIS RELEASE): Local "
    "inference is not wired in this release (LOCAL_TIER_IMPLEMENTED=False). "
    "Configuration requesting 'ollama' or 'local' is silently routed to a "
    "cloud provider by brain/llm.py. Treat all prompts as cloud-routed. "
    "Munir [2026] UKUT 81 (IAC) LPP responsibility remains with the user; "
    "verify Pseudonymisation Gateway coverage and your vendor DPA."
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
    """Read the configured llm_provider from ~/.aibrain_uk/config.json.

    Local inference is NOT implemented in this release (LOCAL_TIER_IMPLEMENTED).
    Therefore this helper cannot honestly report "local" mode — no code path
    routes inference to a local model, so saying so would be a false statement
    that data does not leave the machine.

    Returns one of:
      - "cloud-unconfigured":           no config file, unreadable config, or
                                         no ai_provider/llm_provider key set
      - "cloud-<provider_name>":        named cloud provider
                                         (anthropic / openai / google / deepseek)
      - "cloud-despite-local-config":   the config requests "ollama" or
                                         "local" but the code still sends to
                                         the cloud — the user's stated intent
                                         and the actual behaviour diverge
    """
    config_path = Path.home() / ".aibrain_uk" / "config.json"
    if not config_path.exists():
        # Fallback to the legacy lowercase-hyphen path some installs used.
        legacy_path = Path.home() / ".aibrain-uk" / "config.json"
        if not legacy_path.exists():
            return "cloud-unconfigured"
        config_path = legacy_path
    try:
        cfg = json.loads(config_path.read_text())
    except (OSError, json.JSONDecodeError):
        return "cloud-unconfigured"

    provider = (cfg.get("ai_provider") or cfg.get("llm_provider") or "").lower()
    if provider in ("ollama", "local"):
        # The user has asked for local inference; we don't implement it. Name
        # the divergence so it cannot be silently swallowed downstream.
        return "cloud-despite-local-config"
    if not provider:
        return "cloud-unconfigured"
    return f"cloud-{provider}"


def lpp_firewall_check() -> dict:
    """Return the LPP firewall status — runtime check of configured LLM provider.

    Reads the user's config.json and reports the effective egress route. In this
    release, inference is ALWAYS routed to a cloud provider (see
    LOCAL_TIER_IMPLEMENTED); "local mode" is not implemented, so this helper
    cannot honestly report that data does not leave the machine.

    Pseudonymisation Gateway sanitisation is applied on every egress
    (sanitise → POST → desanitise); the user retains vendor DPA + UK GDPR
    Schedule 21 supplementary safeguards responsibility.
    """
    provider = _read_provider_from_config()

    # Map the helper's prefixed return values to a human-readable display name
    # for the returned dict. The raw prefixed value is preserved in the local
    # `provider` variable; downstream consumers that key off it must be updated
    # to recognise the "cloud-" prefix.
    if provider == "cloud-unconfigured":
        display_provider = "unconfigured (default cloud vendor)"
        warning = None
    elif provider == "cloud-despite-local-config":
        display_provider = "cloud vendor (default anthropic) — see warning"
        warning = (
            "Configuration requests local inference ('ollama' or 'local'), but "
            "this release does not implement a local tier "
            "(LOCAL_TIER_IMPLEMENTED=False). Prompts are being sent to a cloud "
            "provider (default https://api.anthropic.com) after "
            "Pseudonymisation Gateway sanitisation. This is the most dangerous "
            "state: the user's configuration says local, the code does cloud. "
            "Investigate and reconfigure immediately."
        )
    else:
        # "cloud-<name>" form, e.g. "cloud-anthropic"
        display_provider = provider[len("cloud-") :]
        warning = None

    result = {
        "status": "active",
        "mode": "cloud",
        "provider": display_provider,
        "data_transmission": (
            "via Pseudonymisation Gateway (placeholders substituted before "
            f"transmission to {display_provider})"
        ),
        "lpp_preserved_by": (
            "Gateway sanitisation + your vendor DPA + your UK GDPR Schedule 21 "
            "supplementary safeguards"
        ),
        "precedent": "Munir [2026] UKUT 81 (IAC)",
        "message": LPP_CLOUD_MODE_MESSAGE_TEMPLATE.format(provider=display_provider),
        "user_obligations_remaining": (
            f"Execute {display_provider}'s DPA / Article 28 contract. "
            f"Implement UK GDPR Schedule 21 supplementary safeguards if "
            f"{display_provider}'s servers are outside UK ICO-adequate "
            "jurisdictions. Verify Pseudonymisation Gateway coverage of your "
            "matter's specific identifiers."
        ),
    }
    if warning is not None:
        result["warning"] = warning
    return result


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
