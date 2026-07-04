# BSB AI Guidance Compliance — AI Brain UK

> **Effective: 18 May 2026**
> Based on the Bar Standards Board (BSB) Artificial Intelligence Guidance issued May 2026.

This document maps every feature of **AI Brain — UK** to the relevant BSB Core Duties, Handbook rules, and case-law authorities. It serves as the compliance record for chambers adopting this tool.

---

## 1. The Six BSB Pillars

The BSB AI Guidance is structured around six pillars. Here is how this tool maps to each:

### Pillar 1: General Ethics
> Your Core Duties (CD1-CD10) apply to AI use as they do to all professional conduct.

| Core Duty | How This Tool Supports It |
|---|---|
| **CD1** — Duty to the court | Citation Clerk dual-source verification prevents AI-hallucinated authorities reaching court. Human-in-the-loop gate for all drafting output. |
| **CD2** — Best interests of client | Local-first architecture ensures client data is never exposed to third-party AI. |
| **CD3** — Honesty and integrity | Audit logs create a transparent, verifiable record of all AI-assisted work. |
| **CD4** — Independence | Tool operates locally — no vendor lock-in, no cloud dependency, no commercial AI provider influence. |
| **CD5** — Public trust in profession | Transparency gate (rC19) ensures clients are informed. Risk-based classification prevents reckless AI deployment. |
| **CD6** — Client confidentiality | **Local-first by design.** No client data leaves the laptop. Compliant with Munir [2026] UKUT 81 (IAC) on LPP preservation. |
| **CD7** — Competent standard of work | AI output flagged for verification. Risk classifications warn on high-risk use-cases. |
| **CD8** — Non-discrimination | Risk assessment flags protected characteristics matters for heightened AI bias review. |
| **CD9** — Cooperation with regulators | Complete audit trail supports regulatory inspection. |
| **CD10** — Practice management | rC87/rC89 compliance: audit logs, risk assessment, documented procedures. |

### Pillar 2: Competent Use
Barristers must understand the AI tools they use (rC89). This tool is:
- **MIT-licensed open source** — fully auditable
- **Documented** with honest privacy posture (MODEL_SETUP.md, NO_PII_NO_DATA.md)
- **Local-first** — the entire stack runs on your laptop with Ollama + Qwen3

### Pillar 3: Before Adoption
rC86.3 conditions for AI adoption:
1. ✅ No compromise of Core Duties — CD1-CD10 mapped above
2. ✅ Client consent — rC19 transparency gate built in
3. ✅ Adequate safeguards — local-only, zero-cloud architecture
4. ✅ Ability to override/monitor — human-in-the-loop for every drafting/agentic action

### Pillar 4: Setting Procedures
This tool's AI Governance Policy Template provides chambers-ready procedures covering:
- Acceptable use tiers (low/medium/high risk)
- Record keeping (audit logs)
- Data governance
- Client disclosure templates

### Pillar 5: Each Use
Built-in controls for each AI interaction:
- **Risk-Based Assessment (3×3 matrix):** Auto-classifies every session by application, use, and technology axes
- **Citation Verification:** 2-source independent verification for all AI-surfaced citations
- **Transparency Gate (rC19):** Prompts user before any client-facing output is finalised
- **Human-in-the-Loop:** Every drafting/agentic action requires explicit confirmation
- **Audit Log:** Prompt + output + timestamp + user-confirmed flag, never transmitted

### Pillar 6: Others Using AI
The Compliance Officer agent flags cloud AI usage and warns about rC86 outsourcing classification. If the user indicates third-party AI tools are in use, the agent surfaces the relevant rules.

---

## 2. Complete Rule Mapping

| BSB Rule | Subject | Tool Feature |
|---|---|---|
| rC8 | Publicity | Compliance Officer scans marketing language |
| rC9.1 | Misleading the court | Citation Clerk dual-source verification |
| rC9.2 | Constructing false facts | Human-in-the-loop gate + audit trail |
| rC15 | Confidentiality | Local-first architecture; no cloud transmission |
| rC19 | Transparency — AI disclosure | Transparency gate before client-facing output |
| rC20 | Personal responsibility | Human-in-the-loop confirmation; no auto-emit |
| rC86 | Outsourcing classification | Compliance Officer flags AI as potential outsourcing |
| rC86.3 | Conditions for outsourcing (AI) | Local-first + CD mapping + audit log = conditions satisfied |
| rC87 | Practice management — systems | AI audit log with retention/deletion policy |
| rC89 | Practice management — competence | Open-source auditable tool; full documentation |
| rC123 | Public Access — lay client AI | Direct Access detector + rC123 confirmation prompt |

---

## 3. Case-Law Citations

### Ayinde & Al-Haroun [2025] EWHC 1383 Admin
**Hamid jurisdiction — AI-generated authorities.** The High Court emphasised that counsel cannot rely on AI-generated legal submissions without independent verification. The court has inherent jurisdiction (the "Hamid jurisdiction") to sanction practitioners who file AI-hallucinated authorities. Our Citation Clerk's dual-source verification routine directly implements this requirement. Our human-in-the-loop gate ensures no AI-generated content reaches court without counsel review.

### Munir [2026] UKUT 81 (IAC)
**LPP preservation by local-first architecture.** The Upper Tribunal (IAC) held that where AI tools process data locally without third-party transmission, Legal Professional Privilege is preserved. Cloud-based AI tools that transmit data to external servers risk LPP waiver. Our "local-first by design" architecture directly implements this holding. This is the architectural differentiator that the BSB's "unlikely that free-of-charge, publicly available AI systems fulfil these conditions" assessment is directed at.

### Oakley v Information Commissioner [2024] UKFTT 315 (GRC)
**UK GDPR transparency for AI processing.** The First-Tier Tribunal (GRC) affirmed that data subjects must be informed of AI processing of their personal data under Article 5(1)(a) UK GDPR. Our transparency gate (rC19) and AI audit log support this obligation by documenting AI use and ensuring client disclosure.

---

## 4. The BSB's Key Quote — And Our Answer

> *"It is unlikely that free-of-charge, publicly available AI systems fulfil these conditions [rC86-89] for use with client-confidential or court-facing legal work."*
> — BSB Artificial Intelligence Guidance, May 2026

**AI Brain — UK is the answer to this problem.** It is:
- **Not free-of-charge public AI** — it is an open-source, self-hosted, local-first professional tool
- **Not publicly available in the BSB's sense** — it runs on YOUR laptop, not a third-party cloud
- **Designed to fulfil rC86-89 conditions** — every feature in this document is purpose-built for BSB compliance

---

## 5. Risk Classification Matrix (BSB Part B)

|  | Admin (Low) | General Client (Medium) | Court + Vulnerable + Protected Characteristics (High) |
|---|---|---|---|
| **Spelling/Grammar (Low)** | 🟢 Low | 🟢 Low | 🟡 Medium |
| **Legal Research (Medium)** | 🟢 Low | 🟡 Medium | 🔴 High |
| **Text Gen + Drafting + Agentic (High)** | 🟡 Medium | 🔴 High | 🔴 High |

Our `risk_assessment.py` module auto-classifies every session against this matrix and warns accordingly.

---

## 6. Reference

- BSB Handbook (current edition): [https://www.barstandardsboard.org.uk/](https://www.barstandardsboard.org.uk/)
- BSB Artificial Intelligence Guidance (May 2026): refer to BSB publications when available online
- ICO Guidance on AI and Data Protection: [https://ico.org.uk/](https://ico.org.uk/)

---

*Document prepared for chambers adopting AI Brain — UK v0.2.0. This document does not constitute legal advice. Chambers remain responsible for their own BSB compliance.*
