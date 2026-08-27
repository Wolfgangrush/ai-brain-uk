"""
Acceptance tests (TDD) — UK (England & Wales) jurisdiction-native agents.

Opus-owned CONTRACT. RED against the v0.1 stubs; the fleet implements to GREEN.
Axes: (1) shape, (2) UK-native law (Limitation Act 1980 + CPR), (3) NO foreign
residue — neither India (1963/CrPC/writ/SLP/482/indian-*) NOR Singapore
(Limitation Act 1959/ROC 2021/SGHC/ailawfirm_singapore).
"""

import inspect
import re


from aibrain_uk.agents import deadline_agent, drafting_agent, matter_agent

FOREIGN_RESIDUE = re.compile(
    r"\b1963\b|CrPC|BNSS|\b482\b|\b528\b|NI Act|Order VIII|anticipatory\s+bail|"
    r"indian-hc-drafting|supreme-court-drafting|indian-rent-control|indian-tax|"
    r"personaldraftingstack|ailawfirm[-_]india|Limitation Act 1963|"
    r"Limitation Act 1959|ROC 2021|originating claim|\bSGHC\b|\bSGCA\b|ailawfirm[_-]singapore",
    re.I,
)


def _flat(d: dict) -> str:
    return " ".join(str(v) for v in d.values())


class TestDeadlineUK:
    def test_contract_six_years_s5(self):
        r = deadline_agent.handle("limitation for a breach of contract claim")
        b = _flat(r)
        assert "6 year" in b.lower()
        assert "Limitation Act 1980" in b
        assert re.search(r"\bs\.?\s*5\b|section\s*5", b, re.I)

    def test_tort_six_years_s2(self):
        r = deadline_agent.handle("tort negligence claim for property damage")
        b = _flat(r)
        assert "6 year" in b.lower()
        assert re.search(r"\bs\.?\s*2\b|section\s*2", b, re.I)

    def test_personal_injury_three_years_s11(self):
        r = deadline_agent.handle("personal injury claim after an accident")
        b = _flat(r)
        assert "3 year" in b.lower()
        assert re.search(r"\bs\.?\s*11\b|section\s*11", b, re.I)

    def test_recovery_of_land_twelve_years_s15(self):
        r = deadline_agent.handle("action to recover land")
        b = _flat(r)
        assert "12 year" in b.lower()
        assert re.search(r"\bs\.?\s*15\b|section\s*15", b, re.I)

    def test_computes_deadline_when_date_present(self):
        r = deadline_agent.handle("breach of contract on 12 January 2020")
        assert r.get("deadline")
        assert r.get("days_remaining") is not None

    def test_shape_keys(self):
        r = deadline_agent.handle("contract claim")
        for k in ("agent", "category", "article", "period"):
            assert k in r

    def test_no_foreign_residue(self):
        for q in ["contract claim", "recover land", "personal injury", "enforce judgment"]:
            assert not FOREIGN_RESIDUE.search(_flat(deadline_agent.handle(q))), q


class TestDraftingUK:
    def test_claim_form_recognised(self):
        r = drafting_agent.handle("draft a claim form under CPR Part 7")
        assert "claim form" in r.get("doc_type", "").lower()
        assert "draft-with-docx" in _flat(r).lower()

    def test_particulars_of_claim_recognised(self):
        r = drafting_agent.handle("draft the particulars of claim")
        assert "particulars" in r.get("doc_type", "").lower()

    def test_defence_recognised(self):
        r = drafting_agent.handle("draft a defence and counterclaim")
        assert "defence" in r.get("doc_type", "").lower()

    def test_shape_keys(self):
        r = drafting_agent.handle("draft a witness statement")
        assert "doc_type" in r and "suggested_skill" in r

    def test_no_foreign_residue(self):
        for q in [
            "draft a claim form",
            "draft a writ",
            "draft an SLP",
            "draft an originating claim",
        ]:
            assert not FOREIGN_RESIDUE.search(_flat(drafting_agent.handle(q))), q


class TestMatterUK:
    def test_store_path_is_uk(self):
        src = inspect.getsource(matter_agent)
        assert ".aibrain_uk" in src
        assert ".ailawfirm-india" not in src and ".ailawfirm_singapore" not in src

    def test_add_then_list_roundtrip(self, tmp_path, monkeypatch):
        store = tmp_path / "matters.json"
        monkeypatch.setattr(matter_agent, "_STORE_PATH", store, raising=False)
        matter_agent.handle("add matter Regina v Smith Holdings Ltd")
        listed = matter_agent.handle("list matters")
        assert "Smith Holdings" in _flat(listed)

    def test_shape_keys(self):
        r = matter_agent.handle("list matters")
        assert r.get("agent") == "matter_agent"

    def test_no_foreign_residue(self):
        for q in ["add matter ABC", "list matters", "status of XYZ"]:
            assert not FOREIGN_RESIDUE.search(_flat(matter_agent.handle(q))), q
