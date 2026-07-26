"""UK CPR document-type router (England & Wales). Pure stdlib."""

import re

_AGENT = "drafting_agent"
_SKILL = "draft-with-docx"
_NEXT_STEP = (
    "Invoke draft-with-docx with the case folder; verify the current CPR "
    "Practice Direction and prescribed form."
)
_NOTE = (
    "AI classification — confirm the document type and the current CPR form "
    "before filing."
)


def _classify(text: str) -> str:
    """Map a drafting request to a CPR document type."""
    lower = (text or "").lower()
    if re.search(r"\bclaim\s+form\b|\bpart\s+7\b|\bpart\s+8\b", lower):
        return "Claim Form (CPR Part 7/8)"
    if re.search(r"\bparticulars\s+of\s+claim\b", lower):
        return "Particulars of Claim"
    if re.search(r"\bdefence\b|\bcounterclaim\b|\bpart\s+20\b", lower):
        return "Defence / Counterclaim"
    if re.search(r"\breply\b", lower):
        return "Reply"
    if re.search(r"\bapplication\s+notice\b|\bn244\b", lower):
        return "Application Notice (Form N244)"
    if re.search(r"\bwitness\s+statement\b", lower):
        return "Witness Statement"
    if re.search(r"\bskeleton\s+argument\b", lower):
        return "Skeleton Argument"
    return "General statement of case (confirm doc type)"


def handle(payload: str) -> dict:
    text = payload or ""
    return {
        "agent": _AGENT,
        "status": "ok",
        "doc_type": _classify(text),
        "suggested_skill": _SKILL,
        "next_step": _NEXT_STEP,
        "note": _NOTE,
    }
