# Changelog

## [0.1.1] — 2026-06-05 · Dual-mode disclosure refinement

### Changed
- **README.md** — refined headline tagline, BSB-compliance table, "BSB's Key Concern — And This Firm's Answer" paragraph, "Why this exists" closing line, "Privacy & Data Handling — what stays where" section, and "Why this differs from ChatGPT / Claude.ai" comparison table to honestly disclose the dual-mode architecture (local-default · cloud-optional) and the role of the internalised Pseudonymisation Gateway as the structural privacy primitive when cloud mode is invoked.

  Prior wording overstated by treating local-only as architectural fact across all tiers; the architecture is in fact **local-default with cloud-optional + Gateway-sanitised cloud transmission**. The deep architecture docs ([MODEL_SETUP.md](MODEL_SETUP.md), [NO_PII_NO_DATA.md](NO_PII_NO_DATA.md), [pseudonymisation.py](ailawfirm_uk/pseudonymisation.py) source) were already honest about this; the headline-level wording has now been brought into line with them.

- **`ailawfirm_uk/core/gates.py`** — `lpp_firewall_check()` converted from a compile-time architectural assertion into a runtime config-reading check:
  - Reads `~/.ailawfirm_uk/config.json` (or legacy `.ailawfirm-uk/config.json`) at call time.
  - In local mode (`ai_provider="ollama"` / `"local"` / unset) → returns the architectural-guarantee shape (data does not leave the machine; Munir [2026] UKUT 81 (IAC) LPP considerations satisfied by absence of transmission).
  - In cloud mode (`ai_provider="anthropic"` / `"openai"` / `"google"` / `"deepseek"`) → returns honest cloud-mode shape (Pseudonymisation Gateway sanitises before transmission; user retains LPP responsibility + must execute vendor DPA + Article 28 + UK GDPR Schedule 21 supplementary safeguards).
  - The static `LPP_FIREWALL_MESSAGE` constant is preserved (now points to the local-mode message) for backwards compatibility with any existing consumer.

- **`ailawfirm_uk/core/gates.py`** — `SESSION_BANNER` split into two templates (`SESSION_BANNER_LOCAL` + `SESSION_BANNER_CLOUD_TEMPLATE`) with a new `session_banner()` function that selects the right banner based on the configured provider. The cloud-mode banner discloses the Pseudonymisation Gateway sanitisation step + the user's remaining LPP / DPA / Schedule 21 obligations. The static `SESSION_BANNER` constant is preserved (now points to the local-mode banner) for backwards compatibility.

### Why this matters
A UK solo solicitor relying on the prior *"LPP preserved by local-only architecture"* or *"Data never leaves your machine. Compliant by architecture."* lines who then configured a cloud-LLM provider would have been misled. The Gateway sanitisation does reduce LPP exposure structurally, but cloud-mode users retain professional-responsibility obligations the prior wording did not surface. The refinement is honest disclosure; the Gateway as a privacy primitive is materially stronger than what most cloud-AI legal tools offer; the wedge for choosing this tool over commodity cloud AI is preserved.

### Unchanged
- All other code, agents, skills, drafting templates, statute corpus, tests, and getting-started guides are unchanged. This is a documentation + privacy-disclosure-honesty refinement, not a behavioural change in any specialist agent or in the Pseudonymisation Gateway itself.

### Verification
- `grep -rinE "LPP preserved by local-only architecture|Data never leaves your machine\\. Compliant by architecture|local-first is not a feature, it.s the foundation" .` — should return zero hits after this commit
- `python -c "from ailawfirm_uk.core.gates import lpp_firewall_check; import json; print(json.dumps(lpp_firewall_check(), indent=2))"` — should report `mode: local` or `mode: cloud` based on the user's actual config.json
