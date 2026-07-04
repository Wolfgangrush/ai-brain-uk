from ailawfirm_uk.mcp_tools.citation_validator import validate


class TestCitationValidator:
    def test_neutral_uksc(self):
        result = validate("[2023] UKSC 42")
        assert result["format"] == "OSCOLA_NEUTRAL"
        assert result["year"] == 2023
        assert result["reporter_or_court"] == "UKSC"
        assert result["volume_or_serial"] == 42
        assert result["valid"] is True

    def test_neutral_ewca_civ(self):
        result = validate("[2023] EWCA Civ 123")
        assert result["format"] == "OSCOLA_NEUTRAL"
        assert result["reporter_or_court"] == "EWCA Civ"
        assert result["volume_or_serial"] == 123
        assert result["valid"] is True

    def test_neutral_ewhc(self):
        result = validate("[2024] EWHC 567 (KB)")
        assert result["format"] == "OSCOLA_NEUTRAL"
        assert result["reporter_or_court"] == "EWHC"
        assert result["year"] == 2024
        assert result["valid"] is True

    def test_neutral_ewca_crim(self):
        result = validate("[2025] EWCA Crim 89")
        assert result["format"] == "OSCOLA_NEUTRAL"
        assert result["reporter_or_court"] == "EWCA Crim"
        assert result["valid"] is True

    def test_traditional_donoghue(self):
        result = validate("Donoghue v Stevenson [1932] AC 562 (HL)")
        assert result["format"] == "OSCOLA_CASE"
        assert result["year"] == 1932
        assert result["reporter_or_court"] == "AC"
        assert result["page_or_serial"] == 562
        assert result["valid"] is True

    def test_traditional_wlr(self):
        result = validate("Caparo Industries plc v Dickman [1990] WLR 358")
        assert result["format"] == "OSCOLA_CASE"
        assert result["reporter_or_court"] == "WLR"
        assert result["valid"] is True

    def test_statute(self):
        result = validate("Companies Act 2006, s 172")
        assert result["format"] == "OSCOLA_STATUTE"
        assert result["valid"] is True

    def test_statute_with_subsection(self):
        result = validate("Equality Act 2010, s 149(1)")
        assert result["format"] == "OSCOLA_STATUTE"
        assert result["valid"] is True

    def test_invalid_gibberish(self):
        result = validate("gibberish nonsense")
        assert result["format"] == "UNKNOWN"
        assert result["valid"] is False

    def test_invalid_wrong_court(self):
        result = validate("[2023] XYZ 123")
        assert result["format"] == "UNKNOWN"
        assert result["valid"] is False
