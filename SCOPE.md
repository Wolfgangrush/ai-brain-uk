# SCOPE.md — UK v0.1

## In Scope (THIS BUILD)

### Core Architecture
- [x] Fork from brain-3.0.0 (MIT)
- [x] Package rename → `ailawfirm_uk`
- [x] Env-var isolation (AILAWFIRM_UK_PALACE_PATH)
- [x] Default paths → `~/.ailawfirm-uk/`
- [x] ChromaDB collection → `ailawfirm_uk_drawers`

### Legal Domain Modules
- [x] Ontology enums — UK courts, statutes, bar rules, Matter/Citation/CalendarEvent dataclasses
- [x] Court hierarchy — UKSC → County Court + Scottish + NI
- [x] OSCOLA 4th ed. citations — neutral + traditional + statute patterns
- [x] Statute enum — Companies Act 2006 through Data (Use and Access) Act 2025
- [x] SRA Code §8 + BSB rC8 + UK GDPR + POCA compliance keywords

### Brain + Agents
- [x] 10 intent classes (MATTER_UPDATE through UNKNOWN)
- [x] 7 specialist agents (3 live wrapped, 3 stub, 1 keyword firewall)
- [x] UK-specific classifier keywords

### MCP Tools
- [x] `uk_court_lookup` — 6 court stubs with fuzzy matching
- [x] `uk_citation_validator` — OSCOLA parsing (3 patterns)
- [x] `uk_calendar_sync` — ICS generation (UTC + BST)

### Multi-Language Onboarding ⭐
- [x] English (authoritative, ~250 lines)
- [x] Cymraeg (Welsh, AI-assisted)
- [x] Gàidhlig (Scottish Gaelic, AI-assisted)
- [x] Gaeilge (Irish, AI-assisted)
- [x] CLI welcome banner — all 4 languages
- [x] TRANSLATION_HELP_WANTED.md

### Quality Gates
- [x] 38+ tests, all passing
- [x] Ruff check: All checks passed
- [x] Ruff format: all files already formatted
- [x] No git push (local only until Opus verifies)

## Out of Scope (v0.2+)

### Legal Domain
- Full court procedural rules (CPR/CrimPR/FPR — only enum entries in v0.1)
- Sentencing guidelines
- Precedent search
- Cause-list scraping
- E-filing integration
- Legal aid eligibility checker

### Agents (stubs in v0.1)
- Drafting agent (particulars of claim, defence, witness statement, skeleton argument)
- Deadline agent (limitation clock, case-management directions)
- Matter agent (full tracking, document management)

### Firm Mode (v0.3+)
- Multi-user auth
- Billing and time recording
- Conflict-of-interest checking
- Supervisory dashboards
- SRA Accounts Rules automation

### i18n
- Full UI string translation (v0.1 = onboarding guides only)
- Scottish Gaelic / Irish UI (v0.2+)

### Calendar
- macOS EventKit direct integration (v0.2+)
- Google Calendar / Outlook sync
- Court-listing auto-import (CaTH/CourtServe)

## Currency-Aware Stubs

The following domain items are explicitly flagged as recent/phase-in and will need updates:

| Item | Status | Monitor |
|---|---|---|
| Data (Use and Access) Act 2025 | RECENT — in ontology | UK GDPR adequacy with EU |
| ECCT 2023 identity verification | PHASE-IN through 2026 | Companies House guidance |
| SRA Fee Hike 2026 (~29%) | PROPOSED | SRA consultation outcome |
| Making Tax Digital (MTD) | MANDATORY April 2026 for >£50k | HMRC enforcement timeline |

## Explicitly NOT in Scope (any version)

- Legal advice generation (this is a practice OS, not a robot lawyer)
- Court filing (human-in-the-loop always)
- Client-facing AI (internal tool only)
- Replacing professional indemnity insurance
- Replacing qualified legal judgment
