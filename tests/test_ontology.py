from ailawfirm_uk.core.ontology import (
    CalendarEvent,
    Citation,
    Matter,
    MatterType,
    UKBarRule,
    UKCourt,
    UKStatute,
)


class TestMatterType:
    def test_all_matter_types_present(self):
        assert len(MatterType) >= 10

    def test_civil_claim(self):
        assert MatterType.CIVIL_CLAIM.value == "Civil Claim (CPR Part 7)"

    def test_judicial_review(self):
        assert MatterType.JR.value == "Judicial Review (CPR 54)"

    def test_criminal_case(self):
        assert MatterType.CRIM_CASE.value == "Criminal Case"

    def test_family_proceedings(self):
        assert MatterType.FAMILY.value == "Family Proceedings"

    def test_tribunal(self):
        assert "Employment Tribunal" in MatterType.TRIBUNAL_EMPLOYMENT.value


class TestUKCourt:
    def test_all_courts_present(self):
        assert len(UKCourt) >= 12

    def test_supreme_court(self):
        assert "Supreme Court" in UKCourt.UKSC.value

    def test_appeal_court_civil(self):
        assert "Civil Division" in UKCourt.EWCA_CIVIL.value

    def test_high_court_kbd(self):
        assert "King's Bench" in UKCourt.EWHC_KBD.value

    def test_scotland_courts(self):
        assert "Session" in UKCourt.SCOTLAND_SESSION.value
        assert "Justiciary" in UKCourt.SCOTLAND_JUSTICIARY.value

    def test_ni_court(self):
        assert "Judicature" in UKCourt.NI_JUDICATURE.value


class TestUKStatute:
    def test_all_statutes_present(self):
        assert len(UKStatute) >= 12

    def test_companies_act(self):
        assert UKStatute.COMPANIES_ACT_2006.value == "Companies Act 2006"

    def test_uk_gdpr(self):
        assert "General Data Protection Regulation" in UKStatute.UK_GDPR.value

    def test_data_use_access_act_recent(self):
        assert "RECENT" in UKStatute.DATA_USE_ACCESS_ACT_2025.value

    def test_eccta_phase_in(self):
        assert "PHASE-IN" in UKStatute.ECCTA_2023.value

    def test_dpa_2018(self):
        assert "Data Protection Act 2018" in UKStatute.DPA_2018.value


class TestUKBarRule:
    def test_all_bar_rules_present(self):
        assert len(UKBarRule) >= 4

    def test_sra_code_publicity(self):
        assert "§8" in UKBarRule.SRA_CODE_PUBLICITY.value

    def test_bsb_handbook_rc8(self):
        assert "rC8" in UKBarRule.BSB_HANDBOOK_RC8.value

    def test_sra_accounts_rules(self):
        assert "client money" in UKBarRule.SRA_ACCOUNTS_RULES.value

    def test_sra_aml(self):
        assert "AML" in UKBarRule.SRA_AML_OBLIGATIONS.value


class TestMatterDataclass:
    def test_create_matter(self):
        m = Matter(
            matter_id="M001",
            matter_type=MatterType.CIVIL_CLAIM,
            court=UKCourt.EWHC_KBD,
            short_title="Smith v Jones",
        )
        assert m.matter_id == "M001"
        assert m.matter_type == MatterType.CIVIL_CLAIM
        assert m.court == UKCourt.EWHC_KBD
        assert m.parties_claimant == []
        assert m.statutes_invoked == []

    def test_matter_with_parties_and_statutes(self):
        m = Matter(
            matter_id="M002",
            matter_type=MatterType.JR,
            court=UKCourt.EWCA_CIVIL,
            short_title="R (on the application of X) v Secretary of State",
            parties_claimant=["X"],
            parties_defendant=["Secretary of State for the Home Department"],
            statutes_invoked=[UKStatute.UK_GDPR, UKStatute.DPA_2018],
        )
        assert len(m.parties_claimant) == 1
        assert len(m.parties_defendant) == 1
        assert len(m.statutes_invoked) == 2

    def test_matter_optional_dates(self):
        m = Matter(
            matter_id="M003",
            matter_type=MatterType.CRIM_CASE,
            court=UKCourt.CROWN,
            short_title="R v Accused",
            filed_date="2026-05-01",
            next_hearing_date="2026-06-15",
            next_hearing_location="Courtroom 3, Snaresbrook Crown Court",
        )
        assert m.filed_date == "2026-05-01"
        assert m.next_hearing_date == "2026-06-15"
        assert "Snaresbrook" in m.next_hearing_location


class TestCitationDataclass:
    def test_oscola_neutral_citation(self):
        c = Citation(
            raw="[2023] EWCA Civ 123",
            format="OSCOLA_NEUTRAL",
            year=2023,
            reporter_or_court="EWCA Civ",
            volume_or_serial=123,
            valid=True,
        )
        assert c.year == 2023
        assert c.reporter_or_court == "EWCA Civ"
        assert c.valid is True

    def test_oscola_traditional_citation(self):
        c = Citation(
            raw="Donoghue v Stevenson [1932] AC 562 (HL)",
            format="OSCOLA_CASE",
            year=1932,
            reporter_or_court="AC",
            page_or_serial=562,
            valid=True,
        )
        assert c.year == 1932
        assert c.reporter_or_court == "AC"

    def test_invalid_citation(self):
        c = Citation(raw="gibberish", format="UNKNOWN", valid=False)
        assert c.valid is False


class TestCalendarEventDataclass:
    def test_calendar_event_hearing(self):
        e = CalendarEvent(
            event_id="EVT001",
            matter_id="M001",
            summary_alias="CLIENT_A hearing",
            start_iso="2026-07-15T10:00:00+01:00",
            end_iso="2026-07-15T13:00:00+01:00",
            location="Royal Courts of Justice, London",
        )
        assert e.event_id == "EVT001"
        assert e.event_type == "hearing"
        assert "+01:00" in e.start_iso  # BST

    def test_calendar_event_winter_utc(self):
        e = CalendarEvent(
            event_id="EVT002",
            matter_id="M002",
            summary_alias="CLIENT_B conference",
            start_iso="2026-12-15T10:00:00+00:00",
            end_iso="2026-12-15T11:00:00+00:00",
        )
        assert "+00:00" in e.start_iso  # GMT
