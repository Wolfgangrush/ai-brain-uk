"""uk_calendar_sync MCP tool — ICS calendar file generation.

Timezone: UTC base, Europe/London (BST-aware for summer dates).
ADR-002 pattern: ICS feed primary, no Google API.

PROVENANCE: CITED:_RESEARCH_SUMMARY.md (ADR-002)
"""

from datetime import UTC, datetime

from ailawfirm_uk.core.ontology import CalendarEvent


def generate_ics(event: CalendarEvent) -> str:
    """Generate a valid ICS (.ics) string for a single CalendarEvent.

    Handles BST (UTC+1) for summer dates and GMT (UTC+0) for winter dates.
    """
    dtstamp = datetime.now(UTC).strftime("%Y%m%dT%H%M%SZ")

    start = _format_ics_datetime(event.start_iso)
    end = _format_ics_datetime(event.end_iso)

    summary = event.summary_alias or "Untitled Event"
    description = event.body_full or ""
    location = event.location or ""

    lines = [
        "BEGIN:VCALENDAR",
        "VERSION:2.0",
        "PRODID:-//AI Brain UK//ailawfirm_uk//EN",
        "CALSCALE:GREGORIAN",
        "METHOD:PUBLISH",
        "X-WR-TIMEZONE:Europe/London",
        "BEGIN:VEVENT",
        f"DTSTART:{start}",
        f"DTEND:{end}",
        f"DTSTAMP:{dtstamp}",
        f"UID:{event.event_id}",
        f"SUMMARY:{summary}",
        f"DESCRIPTION:{description}",
    ]
    if location:
        lines.append(f"LOCATION:{location}")
    lines.extend(
        [
            "END:VEVENT",
            "END:VCALENDAR",
        ]
    )
    return "\r\n".join(lines) + "\r\n"


def _format_ics_datetime(iso_str: str) -> str:
    """Convert ISO datetime string to ICS format (UTC Z-terminated)."""
    s = iso_str.strip()
    if s.endswith("Z"):
        return s.replace("-", "").replace(":", "")[:-1] + "Z"
    # Strip timezone offset
    if "+" in s:
        s = s.split("+")[0]
    elif s.rfind("-") > 12:
        # Only strip the last -NN:NN tz offset, not date hyphens
        parts = s.rsplit("-", 1)
        if len(parts) == 2 and ":" in parts[1]:
            s = parts[0]
    s = s.replace("-", "").replace(":", "")
    return s + "Z"
