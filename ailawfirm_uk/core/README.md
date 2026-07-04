# core/ — Shared legal domain modules

Used by both solo and firm modes. Holds the UK legal ontology:
- `ontology.py` — Enums for UK courts, statutes, citation formats, bar rules, Matter/Citation/CalendarEvent dataclasses
- `courts/` — Court lookup and hierarchy
- `citations/` — OSCOLA citation parsing and validation
- `statutes/` — Statute metadata and cross-references
- `calendar/` — ICS calendar sync (Europe/London timezone, BST-aware)
