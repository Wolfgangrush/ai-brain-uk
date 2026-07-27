"""UK Limitation Act 1980 deadline classifier (England & Wales). Pure stdlib."""

import re
from datetime import date, timedelta

_MONTHS = {
    "january": 1,
    "february": 2,
    "march": 3,
    "april": 4,
    "may": 5,
    "june": 6,
    "july": 7,
    "august": 8,
    "september": 9,
    "october": 10,
    "november": 11,
    "december": 12,
    "jan": 1,
    "feb": 2,
    "mar": 3,
    "apr": 4,
    "jun": 6,
    "jul": 7,
    "aug": 8,
    "sep": 9,
    "sept": 9,
    "oct": 10,
    "nov": 11,
    "dec": 12,
}

_AGENT = "deadline_agent"
_NOTE = (
    "AI-generated period. Deliberate concealment/fraud/disability can extend "
    "time (Part II, s 32). Verify against the Limitation Act 1980 before relying."
)


def _find_date(text):
    """Return a date.date if a recognised date is present in text, else None."""
    if not text:
        return None
    # DD-MM-YYYY or DD/MM/YYYY
    m = re.search(r"\b(\d{1,2})[-/](\d{1,2})[-/](\d{4})\b", text)
    if m:
        try:
            return date(int(m.group(3)), int(m.group(2)), int(m.group(1)))
        except ValueError:
            pass
    # YYYY-MM-DD
    m = re.search(r"\b(\d{4})-(\d{1,2})-(\d{1,2})\b", text)
    if m:
        try:
            return date(int(m.group(1)), int(m.group(2)), int(m.group(3)))
        except ValueError:
            pass
    # "12 January 2020"
    m = re.search(r"\b(\d{1,2})\s+([A-Za-z]+)\s+(\d{4})\b", text)
    if m:
        mo = _MONTHS.get(m.group(2).lower())
        if mo:
            try:
                return date(int(m.group(3)), mo, int(m.group(1)))
            except ValueError:
                pass
    # "January 12 2020"
    m = re.search(r"\b([A-Za-z]+)\s+(\d{1,2})\s+(\d{4})\b", text)
    if m:
        mo = _MONTHS.get(m.group(1).lower())
        if mo:
            try:
                return date(int(m.group(3)), mo, int(m.group(2)))
            except ValueError:
                pass
    return None


def _classify(text):
    """First-match-wins keyword classification under the Limitation Act 1980."""
    lower = (text or "").lower()
    # 1. Recovery of land
    if re.search(
        r"\brecover(?:ing|ed|s)?\s+land\b|\bland\b|\bimmovable\b|\bpossession\b|\bmortgage\b",
        lower,
    ):
        return ("Recovery of land", 12, "s 15 Limitation Act 1980")
    # 2. Specialty (deed)
    if re.search(r"\bdeed\b|\bspecialty\b|\bunder seal\b", lower):
        return ("Specialty (deed)", 12, "s 8 Limitation Act 1980")
    # 3. Defamation
    if re.search(r"\bdefamation\b|\blibel\b|\bslander\b|\bmalicious falsehood\b", lower):
        return ("Defamation", 1, "s 4A Limitation Act 1980")
    # 4. Enforcement of judgment
    if re.search(
        r"\benforc\w+\s+(?:a\s+)?judgment\b|\bjudgment\s+debt\b|\bexecution\b",
        lower,
    ):
        return ("Enforcement of judgment", 6, "s 24 Limitation Act 1980")
    # 5. Personal injury
    if re.search(r"\bpersonal\s+injur", lower):
        return ("Personal injury", 3, "s 11 Limitation Act 1980")
    if re.search(r"\bnegligence\b", lower) and re.search(r"\binjur", lower):
        return ("Personal injury", 3, "s 11 Limitation Act 1980")
    if re.search(r"\baccident\b", lower):
        return ("Personal injury", 3, "s 11 Limitation Act 1980")
    # 6. Contract
    if re.search(r"\bcontract\b|\bbreach\b|\bdebt\b|\bloan\b", lower):
        return ("Contract", 6, "s 5 Limitation Act 1980")
    # 7. Tort
    if re.search(r"\btort\b|\bnegligence\b|\bnuisance\b|\btrespass\b|\bdamage\b", lower):
        return ("Tort", 6, "s 2 Limitation Act 1980")
    # 8. Default
    return ("General / residuary", 6, "s 5 Limitation Act 1980")


def handle(payload: str) -> dict:
    text = payload or ""
    category, years, article = _classify(text)
    start_date = _find_date(text)
    period_days = years * 365
    if start_date is not None:
        deadline = start_date + timedelta(days=period_days)
        days_remaining = (deadline - date.today()).days
        start_iso = start_date.isoformat()
        deadline_iso = deadline.isoformat()
    else:
        days_remaining = None
        start_iso = None
        deadline_iso = None
    period_str = "1 year" if years == 1 else f"{years} years"
    return {
        "agent": _AGENT,
        "status": "ok",
        "category": category,
        "article": article,
        "period": period_str,
        "start_date": start_iso,
        "deadline": deadline_iso,
        "days_remaining": days_remaining,
        "note": _NOTE,
    }
