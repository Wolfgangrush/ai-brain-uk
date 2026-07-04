from ailawfirm_uk.brain.intents import Intent
from ailawfirm_uk.brain.classifier import classify
from ailawfirm_uk.brain.router import route


class TestClassifier:
    def test_calendar_query(self):
        assert classify("what's on my calendar next week") == Intent.CALENDAR_QUERY

    def test_citation_lookup(self):
        assert classify("check this citation [2023] EWCA Civ 123") == Intent.CITATION_LOOKUP

    def test_court_query(self):
        assert classify("which court has jurisdiction for this") == Intent.COURT_QUERY

    def test_compliance_flag_sra(self):
        assert classify("is this publicity allowed under SRA rules") == Intent.COMPLIANCE_FLAG

    def test_compliance_flag_aml(self):
        assert classify("do I need KYC and AML checks for this") == Intent.COMPLIANCE_FLAG

    def test_compliance_flag_uk_gdpr(self):
        assert classify("does UK GDPR apply to this data breach") == Intent.COMPLIANCE_FLAG

    def test_deadline_check(self):
        assert classify("what's the limitation deadline for this") == Intent.DEADLINE_CHECK

    def test_drafting_need(self):
        assert classify("help me draft a skeleton argument") == Intent.DRAFTING_NEED

    def test_matter_update(self):
        assert classify("the matter was filed today") == Intent.MATTER_UPDATE

    def test_calendar_add(self):
        assert classify("add to calendar for next Friday") == Intent.CALENDAR_ADD

    def test_unknown(self):
        assert classify("banana smoothie recipe") == Intent.UNKNOWN


class TestRouter:
    def test_routes_calendar_query_to_calendar_agent(self):
        assert route(Intent.CALENDAR_QUERY) == "calendar_agent"

    def test_routes_citation_to_citation_agent(self):
        assert route(Intent.CITATION_LOOKUP) == "citation_agent"

    def test_routes_court_to_court_agent(self):
        assert route(Intent.COURT_QUERY) == "court_agent"

    def test_routes_compliance_to_compliance_agent(self):
        assert route(Intent.COMPLIANCE_FLAG) == "compliance_agent"

    def test_routes_drafting_to_drafting_agent(self):
        assert route(Intent.DRAFTING_NEED) == "drafting_agent"

    def test_routes_unknown_to_matter_agent(self):
        assert route(Intent.UNKNOWN) == "matter_agent"
