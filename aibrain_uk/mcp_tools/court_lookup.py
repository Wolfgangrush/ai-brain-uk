"""uk_court_lookup MCP tool — fuzzy-match UK court by name.

PROVENANCE: CITED:01-court-hierarchy.md
"""

COURTS: list[dict] = [
    {
        "name": "Supreme Court of the United Kingdom",
        "code": "UKSC",
        "location": "Parliament Square, London",
        "tier": "Final appellate",
        "jurisdiction_class": "UK-wide",
        "procedural_code": "UKSC Rules",
        "research_ref": "01-court-hierarchy.md",
    },
    {
        "name": "Court of Appeal — Civil Division (England & Wales)",
        "code": "EWCA-Civil",
        "location": "Royal Courts of Justice, London",
        "tier": "Appellate",
        "jurisdiction_class": "England & Wales",
        "procedural_code": "CPR Part 52",
        "research_ref": "01-court-hierarchy.md",
    },
    {
        "name": "High Court — King's Bench Division",
        "code": "EWHC-KBD",
        "location": "Royal Courts of Justice, London",
        "tier": "First instance / appellate",
        "jurisdiction_class": "England & Wales",
        "procedural_code": "CPR Part 7 (multi-track) / Part 8",
        "research_ref": "01-court-hierarchy.md",
    },
    {
        "name": "Crown Court",
        "code": "Crown",
        "location": "Multiple locations across England & Wales",
        "tier": "First instance (criminal)",
        "jurisdiction_class": "England & Wales",
        "procedural_code": "CrimPR",
        "research_ref": "01-court-hierarchy.md",
    },
    {
        "name": "Magistrates' Court",
        "code": "Magistrates",
        "location": "Multiple locations across England & Wales",
        "tier": "First instance (summary)",
        "jurisdiction_class": "England & Wales",
        "procedural_code": "Magistrates' Courts Act 1980",
        "research_ref": "01-court-hierarchy.md",
    },
    {
        "name": "Court of Session (Scotland)",
        "code": "Scotland-Session",
        "location": "Parliament House, Edinburgh",
        "tier": "Appellate / first instance",
        "jurisdiction_class": "Scotland",
        "procedural_code": "Rules of the Court of Session",
        "research_ref": "01-court-hierarchy.md",
    },
]


def lookup(query: str) -> dict:
    """Fuzzy-match a court name query against known UK courts.

    Returns the best match or a not-found result.
    """
    q = query.lower().strip()
    best: dict | None = None
    best_score = 0

    for court in COURTS:
        name_lower = court["name"].lower()
        code_lower = court["code"].lower()

        if q == code_lower:
            return {"status": "found", "court": court, "match_type": "exact_code"}

        if q in name_lower or name_lower in q:
            score = len(q)
            if score > best_score:
                best_score = score
                best = court

        keywords = name_lower.replace("'", "").replace("-", " ").split()
        matched = sum(1 for kw in keywords if kw in q)
        if matched >= 2 and matched > best_score:
            best_score = matched
            best = court

    if best and best_score > 0:
        return {"status": "found", "court": best, "match_type": "fuzzy"}

    return {
        "status": "not_found",
        "query": query,
        "hint": "Try: Supreme Court, Court of Appeal, King's Bench, Crown Court, Magistrates, Court of Session",
    }
