"""
UK legal ontology — enums and dataclasses for courts, statutes, citations, bar rules, matters.

PROVENANCE: CITED:01-court-hierarchy.md, 04-statute-data-protection.md,
    10-bar-rule-publicity-solicitation.md, 13-citation-format-primary.md,
    27-anti-money-laundering-obligations.md, _RESEARCH_SUMMARY.md
"""

from dataclasses import dataclass, field
from enum import Enum
from typing import Optional


class MatterType(Enum):
    CIVIL_CLAIM = "Civil Claim (CPR Part 7)"
    PART_8_CLAIM = "Part 8 Claim (alternative procedure)"
    JR = "Judicial Review (CPR 54)"
    CRIM_CASE = "Criminal Case"
    APPEAL_CIVIL = "Civil Appeal"
    APPEAL_CRIMINAL = "Criminal Appeal"
    FAMILY = "Family Proceedings"
    DIVORCE = "Divorce / Dissolution"
    PROBATE = "Probate / Estate Administration"
    TRIBUNAL_EMPLOYMENT = "Employment Tribunal claim"
    TRIBUNAL_TAX = "First-tier Tribunal (Tax)"
    OTHER = "Other (specify)"


class UKCourt(Enum):
    UKSC = "Supreme Court of the United Kingdom"
    EWCA_CIVIL = "Court of Appeal — Civil Division (England & Wales)"
    EWCA_CRIM = "Court of Appeal — Criminal Division (England & Wales)"
    EWHC_KBD = "High Court — King's Bench Division"
    EWHC_CHANCERY = "High Court — Chancery Division"
    EWHC_FAMILY = "High Court — Family Division"
    CROWN = "Crown Court"
    MAGISTRATES = "Magistrates' Court"
    COUNTY = "County Court"
    SCOTLAND_SESSION = "Court of Session (Scotland)"
    SCOTLAND_JUSTICIARY = "High Court of Justiciary (Scotland)"
    SCOTLAND_SHERIFF = "Sheriff Court (Scotland)"
    NI_JUDICATURE = "Court of Judicature (Northern Ireland)"
    OTHER = "Other (specify)"


class UKStatute(Enum):
    COMPANIES_ACT_2006 = "Companies Act 2006"
    EQUALITY_ACT_2010 = "Equality Act 2010"
    UK_GDPR = "UK General Data Protection Regulation (post-Brexit retained)"
    DPA_2018 = "Data Protection Act 2018"
    DATA_USE_ACCESS_ACT_2025 = "Data (Use and Access) Act 2025 — RECENT"
    SOLICITORS_ACT_1974 = "Solicitors Act 1974"
    BRIBERY_ACT_2010 = "Bribery Act 2010"
    POCA_2002 = "Proceeds of Crime Act 2002"
    ECCTA_2023 = "Economic Crime and Corporate Transparency Act 2023 — PHASE-IN"
    LIMITATION_ACT_1980 = "Limitation Act 1980"
    CONSUMER_RIGHTS_ACT_2015 = "Consumer Rights Act 2015"
    CPR = "Civil Procedure Rules 1998 (as amended through 2026)"
    CRIMPR = "Criminal Procedure Rules"
    FPR = "Family Procedure Rules 2010"


class UKBarRule(Enum):
    SRA_CODE_PUBLICITY = "SRA Code of Conduct §8 — publicity restrictions"
    BSB_HANDBOOK_RC8 = "BSB Handbook rC8 — publicity for self-employed barristers"
    SRA_ACCOUNTS_RULES = "SRA Accounts Rules — client money handling"
    SRA_AML_OBLIGATIONS = "SRA AML obligations (POCA + MLR 2017)"


@dataclass
class Matter:
    matter_id: str
    matter_type: MatterType
    court: UKCourt
    short_title: str
    parties_claimant: list[str] = field(default_factory=list)
    parties_defendant: list[str] = field(default_factory=list)
    statutes_invoked: list[UKStatute] = field(default_factory=list)
    filed_date: Optional[str] = None
    next_hearing_date: Optional[str] = None
    next_hearing_location: Optional[str] = None
    status_note: Optional[str] = None


@dataclass
class Citation:
    raw: str
    format: str  # 'OSCOLA_CASE' | 'OSCOLA_NEUTRAL' | 'OSCOLA_STATUTE' | 'UNKNOWN'
    year: Optional[int] = None
    reporter_or_court: Optional[str] = None
    volume_or_serial: Optional[int] = None
    page_or_serial: Optional[int] = None
    valid: bool = False
    parse_notes: Optional[str] = None


@dataclass
class CalendarEvent:
    event_id: str
    matter_id: Optional[str] = None
    summary_alias: str = ""
    body_full: str = ""
    start_iso: str = ""  # YYYY-MM-DDTHH:MM:SS+00:00 (UTC default · BST applies summer)
    end_iso: str = ""
    location: Optional[str] = None
    event_type: str = "hearing"
