# core/calendar/ — ICS calendar sync (ADR-002)

Primary: ICS feed generation (`.ics` files), importable into Calendar.app, Outlook, Google Calendar.
Timezone: UTC base, Europe/London with BST summer handling.

Files:
- `ics_writer.py` — Generates valid ICS from CalendarEvent dataclass
- `publishers.py` — Filesystem and stdout publishers

v0.2+: macOS EventKit direct integration.
No Google API — local-first, offline-capable.
