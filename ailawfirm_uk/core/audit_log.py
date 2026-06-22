"""AI Audit Log — always-on audit trail for BSB rC86-89 compliance.

Logs every AI prompt + output + timestamp + user-confirmed-output flag.
Configurable retention (90-day default). Deletion policy enforced.
Stored at ~/.ailawfirm_uk/audit_logs/ — never transmitted.

PROVENANCE: BSB Artificial Intelligence Guidance May 2026, rC87.2 (practice management),
    rC86.3 (outsourcing conditions — record-keeping requirement)
"""

from __future__ import annotations

import json
import os
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Optional


DEFAULT_RETENTION_DAYS = 90
DEFAULT_LOG_DIR = "~/.ailawfirm_uk/audit_logs"


class AuditLogger:
    """Always-on audit log for AI interactions.

    Usage:
        logger = AuditLogger()
        logger.log(prompt="...", output="...", agent="citation_agent")
        logger.log(prompt="...", output="...", user_confirmed=True)
    """

    def __init__(
        self,
        log_dir: Optional[str] = None,
        retention_days: int = DEFAULT_RETENTION_DAYS,
    ):
        self._log_dir = Path(log_dir or os.path.expanduser(DEFAULT_LOG_DIR))
        self._retention_days = retention_days
        self._log_dir.mkdir(parents=True, exist_ok=True)
        self._enforce_retention()

    def log(
        self,
        prompt: str,
        output: str = "",
        agent: str = "unknown",
        user_confirmed: bool = False,
        risk_level: str = "",
        session_id: str = "",
        metadata: Optional[dict] = None,
    ) -> dict:
        """Write an entry to the audit log.

        Args:
            prompt: The user's input or AI prompt
            output: The AI-generated output
            agent: Which specialist agent handled this
            user_confirmed: Whether the user explicitly confirmed the output
            risk_level: BSB risk classification (low/medium/high)
            session_id: Session identifier for grouping
            metadata: Arbitrary additional context

        Returns:
            The log entry dict that was written
        """
        timestamp = datetime.now(timezone.utc).isoformat()
        entry = {
            "timestamp": timestamp,
            "prompt": prompt,
            "output": output,
            "agent": agent,
            "user_confirmed": user_confirmed,
            "risk_level": risk_level,
            "session_id": session_id,
            "metadata": metadata or {},
        }

        date_str = datetime.now(timezone.utc).strftime("%Y-%m-%d")
        log_file = self._log_dir / f"audit_{date_str}.jsonl"

        with open(log_file, "a") as f:
            f.write(json.dumps(entry, default=str) + "\n")

        return entry

    def query(
        self,
        start_date: Optional[str] = None,
        end_date: Optional[str] = None,
        agent: Optional[str] = None,
        risk_level: Optional[str] = None,
    ) -> list[dict]:
        """Query audit logs with optional filters.

        Args:
            start_date: ISO date string (YYYY-MM-DD)
            end_date: ISO date string (YYYY-MM-DD)
            agent: Filter by agent name
            risk_level: Filter by risk level

        Returns:
            List of matching log entries
        """
        results: list[dict] = []
        for log_file in sorted(self._log_dir.glob("audit_*.jsonl")):
            file_date = log_file.stem.replace("audit_", "")
            if start_date and file_date < start_date:
                continue
            if end_date and file_date > end_date:
                continue
            try:
                with open(log_file, "r") as f:
                    for line in f:
                        line = line.strip()
                        if not line:
                            continue
                        entry = json.loads(line)
                        if agent and entry.get("agent") != agent:
                            continue
                        if risk_level and entry.get("risk_level") != risk_level:
                            continue
                        results.append(entry)
            except (json.JSONDecodeError, OSError):
                continue
        return results

    def _enforce_retention(self) -> int:
        """Delete log files older than retention_days. Returns count of deleted files."""
        cutoff = datetime.now(timezone.utc) - timedelta(days=self._retention_days)
        deleted = 0
        for log_file in self._log_dir.glob("audit_*.jsonl"):
            try:
                file_date_str = log_file.stem.replace("audit_", "")
                file_date = datetime.strptime(file_date_str, "%Y-%m-%d").replace(
                    tzinfo=timezone.utc
                )
                if file_date < cutoff:
                    log_file.unlink()
                    deleted += 1
            except (ValueError, OSError):
                continue

        # Also clean risk logs
        for risk_file in self._log_dir.glob("risk_log_*.jsonl"):
            try:
                file_date_str = risk_file.stem.replace("risk_log_", "")
                file_date = datetime.strptime(file_date_str, "%Y-%m-%d").replace(
                    tzinfo=timezone.utc
                )
                if file_date < cutoff:
                    risk_file.unlink()
                    deleted += 1
            except (ValueError, OSError):
                continue

        return deleted

    def retention_status(self) -> dict:
        """Return current retention configuration and log count."""
        entries = self.query()
        return {
            "retention_days": self._retention_days,
            "log_dir": str(self._log_dir),
            "total_entries": len(entries),
            "oldest_entry": entries[0]["timestamp"] if entries else None,
            "newest_entry": entries[-1]["timestamp"] if entries else None,
        }

    def delete_all_logs(self) -> int:
        """Emergency purge — delete all audit logs. Returns count of deleted files."""
        deleted = 0
        for pattern in ["audit_*.jsonl", "risk_log_*.jsonl", "transparency_*.jsonl"]:
            for f in self._log_dir.glob(pattern):
                f.unlink()
                deleted += 1
        return deleted


# Singleton convenience
_audit_logger: Optional[AuditLogger] = None


def get_audit_logger() -> AuditLogger:
    global _audit_logger
    if _audit_logger is None:
        _audit_logger = AuditLogger()
    return _audit_logger
