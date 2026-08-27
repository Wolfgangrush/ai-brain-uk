"""uk_citation_validator MCP tool — OSCOLA 4th ed. citation parser.

PROVENANCE: CITED:13-citation-format-primary.md
"""

import re

# Neutral citation: [YYYY] Court Number  e.g. [2023] EWCA Civ 123
_NEUTRAL_PATTERN = re.compile(
    r"^\[(?P<year>\d{4})\]\s+(?P<court>UKSC|EWCA Civ|EWCA Crim|EWHC|UKHL)"
    r"\s+(?P<num>\d+)(\s+\(.+?\))?$"
)

# Traditional law-report: Name v Name [YEAR] REPORTER PAGE (COURT)
_TRADITIONAL_PATTERN = re.compile(
    r"^.+?\s+v\s+.+?\s+\[(?P<year>\d{4})\]\s+"
    r"(?P<reporter>AC|All ER|WLR|QB|KB|Ch|Fam|Lloyd's Rep)\s+"
    r"(?P<page>\d+)(\s+\(.+?\))?$"
)

# Statute: Act Name YYYY, s NN  e.g. Companies Act 2006, s 172
_STATUTE_PATTERN = re.compile(r"^.+?\s+\d{4},\s+s\s+\d+(\(\w+\))?$")

VALID_COURTS = {"UKSC", "EWCA Civ", "EWCA Crim", "EWHC", "UKHL"}
VALID_REPORTERS = {"AC", "All ER", "WLR", "QB", "KB", "Ch", "Fam", "Lloyd's Rep"}


def validate(citation: str) -> dict:
    """Parse and validate an OSCOLA citation.

    Returns format, parsed fields, and validity flag.
    """
    raw = citation.strip()

    m = _NEUTRAL_PATTERN.match(raw)
    if m:
        court = m.group("court")
        return {
            "raw": raw,
            "format": "OSCOLA_NEUTRAL",
            "year": int(m.group("year")),
            "reporter_or_court": court,
            "volume_or_serial": int(m.group("num")),
            "valid": court in VALID_COURTS,
            "parse_notes": None if court in VALID_COURTS else f"Unknown court code: {court}",
        }

    m = _TRADITIONAL_PATTERN.match(raw)
    if m:
        reporter = m.group("reporter")
        return {
            "raw": raw,
            "format": "OSCOLA_CASE",
            "year": int(m.group("year")),
            "reporter_or_court": reporter,
            "page_or_serial": int(m.group("page")),
            "valid": reporter in VALID_REPORTERS,
            "parse_notes": None if reporter in VALID_REPORTERS else f"Unknown reporter: {reporter}",
        }

    m = _STATUTE_PATTERN.match(raw)
    if m:
        return {
            "raw": raw,
            "format": "OSCOLA_STATUTE",
            "valid": True,
            "parse_notes": "Statute citation — structural check only",
        }

    return {
        "raw": raw,
        "format": "UNKNOWN",
        "valid": False,
        "parse_notes": "Could not parse as OSCOLA citation",
    }
