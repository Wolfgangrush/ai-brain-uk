from ailawfirm_uk.core.ontology import CalendarEvent
from ailawfirm_uk.mcp_tools.calendar_sync import generate_ics


class TestCalendarSync:
    def test_generates_valid_ics(self):
        event = CalendarEvent(
            event_id="evt-001@ailawfirm-uk",
            matter_id="M001",
            summary_alias="CLIENT_A hearing",
            body_full="Case management conference in CLIENT_A matter",
            start_iso="2026-06-15T10:00:00+01:00",
            end_iso="2026-06-15T13:00:00+01:00",
            location="Royal Courts of Justice, London",
        )
        ics = generate_ics(event)
        assert "BEGIN:VCALENDAR" in ics
        assert "BEGIN:VEVENT" in ics
        assert "END:VEVENT" in ics
        assert "END:VCALENDAR" in ics
        assert "SUMMARY:CLIENT_A hearing" in ics
        assert "LOCATION:Royal Courts of Justice, London" in ics
        assert "X-WR-TIMEZONE:Europe/London" in ics

    def test_bst_summer_date(self):
        event = CalendarEvent(
            event_id="evt-bst@ailawfirm-uk",
            matter_id="M002",
            summary_alias="BST_TEST hearing",
            start_iso="2026-07-15T10:00:00+01:00",
            end_iso="2026-07-15T13:00:00+01:00",
        )
        ics = generate_ics(event)
        assert "DTSTART:" in ics
        assert "DTEND:" in ics
        lines = [e for e in ics.split("\r\n") if e.startswith("DTSTART:")]
        line = lines[0]
        assert "20260715T" in line
        assert line.endswith("Z") or "Z\r" in line

    def test_gmt_winter_date(self):
        event = CalendarEvent(
            event_id="evt-gmt@ailawfirm-uk",
            matter_id="M003",
            summary_alias="WINTER_TEST conference",
            start_iso="2026-12-15T10:00:00+00:00",
            end_iso="2026-12-15T11:00:00+00:00",
        )
        ics = generate_ics(event)
        assert "SUMMARY:WINTER_TEST conference" in ics
        lines = [e for e in ics.split("\r\n") if e.startswith("DTSTART:")]
        line = lines[0]
        assert "20261215T" in line

    def test_minimal_event(self):
        event = CalendarEvent(
            event_id="evt-min@ailawfirm-uk",
            summary_alias="Quick check-in",
            start_iso="2026-05-20T09:00:00+00:00",
            end_iso="2026-05-20T09:30:00+00:00",
        )
        ics = generate_ics(event)
        assert "BEGIN:VCALENDAR" in ics
        assert "SUMMARY:Quick check-in" in ics
