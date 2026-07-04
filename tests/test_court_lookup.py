from ailawfirm_uk.mcp_tools.court_lookup import lookup


class TestCourtLookup:
    def test_exact_code_match_uksc(self):
        result = lookup("UKSC")
        assert result["status"] == "found"
        assert result["match_type"] == "exact_code"
        assert "Supreme Court" in result["court"]["name"]

    def test_fuzzy_supreme_court(self):
        result = lookup("Supreme Court")
        assert result["status"] == "found"
        assert "UKSC" in result["court"]["code"]

    def test_fuzzy_kings_bench(self):
        result = lookup("King's Bench")
        assert result["status"] == "found"
        assert result["court"]["code"] == "EWHC-KBD"

    def test_fuzzy_crown_court(self):
        result = lookup("Crown Court")
        assert result["status"] == "found"
        assert result["court"]["code"] == "Crown"

    def test_fuzzy_court_of_session(self):
        result = lookup("Court of Session")
        assert result["status"] == "found"
        assert result["court"]["code"] == "Scotland-Session"

    def test_fuzzy_magistrates(self):
        result = lookup("Magistrates Court")
        assert result["status"] == "found"
        assert result["court"]["code"] == "Magistrates"

    def test_not_found(self):
        result = lookup("Mars Tribunal")
        assert result["status"] == "not_found"
