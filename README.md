# 🇬🇧 AI Brain for UK Lawyers

> **Free practice OS for every UK solo solicitor, barrister, advocate (Scotland), CILEx-regulated practitioner, and in-house counsel. Terminal-native. Local-first by default (Ollama + Qwen3 — nothing leaves your laptop). Cloud-LLM optional with the [Pseudonymisation Gateway](https://github.com/Wolfgangrush/pseudonymisation-gateway) sanitising PII before any prompt leaves the machine.**

**For qualified legal professionals only.** Intended for solicitors regulated by the SRA, barristers regulated by the BSB, advocates regulated by the Faculty of Advocates (Scotland), solicitors regulated by the Law Society of Scotland or the Law Society of Northern Ireland, CILEx-regulated practitioners, in-house counsel of UK entities, and paralegals working under their supervision. **If you are not a qualified legal professional, do not use this tool to produce client-facing legal work.** Read [DISCLAIMER.md](DISCLAIMER.md) before installation.

**Version:** 0.1.1 · **License:** MIT · **Publisher:** [wolfgang_rush](https://github.com/Wolfgangrush) — an Indian advocate (High Courts of India, India). NOT admitted in any UK jurisdiction. This is a software publication for UK-admitted practitioners. · **Engine:** Built on a local memory architecture

> ⚠️ **AI can make mistakes. Always verify the output.**
>
> This software generates assistive drafts and suggestions only. Every legal claim, citation, statute reference, procedural step, deadline calculation, and ground of relief must be independently verified by a qualified human practitioner before filing, advising a client, or relying on the output. The publisher accepts no liability for outputs used without verification.

> 🛡️ **Privacy primitive: PII pseudonymisation** via [pseudonymisation-gateway](https://github.com/Wolfgangrush/pseudonymisation-gateway) (wolfgang_rush · MIT). This firm uses the `uk` jurisdiction module + Indian-diaspora overlay for cross-jurisdiction PII coverage. Open-source · zero runtime deps · session-scoped · in-memory only · never writes PII to disk.


> 🛡️ **Pseudonymisation coverage (v0.1.1):** The privacy gateway pseudonymises PII before any cloud-API call; any residue the scanner can't fully resolve is surfaced to you and audit-logged — you retain the final call (v0.3 honest-disclosure). Covers UK-native identifiers (National Insurance Number · NHS Number · UTR · UK VAT · UK phone · GBP amounts · UK IBAN · EWHC/EWCA/UKSC case numbers) and Indian-diaspora identifiers (Aadhaar · PAN · GSTIN · IFSC · Indian phone — UK has substantial South Asian diaspora). Generic patterns (email · names with honorifics · dates · case numbers) work cross-jurisdiction.

> **🧠 AI Brain that LEARNS.** Every session makes the next one smarter. Two built-in Claude Code skills power this: `/retrospective` saves what the firm learned at session end — every jurisdiction, statute, argument pattern, and procedural rule you touched is logged so the firm's knowledge compounds. `/wake` loads that accumulated context the next time you start, so you never begin from zero. The firm is your second brain, and it gets sharper with every case.

> 🆕 **Updated 2026-05-19 — BSB AI Guidance compliance integrated.** This release implements the Bar Standards Board's *Guidance on the use of Artificial Intelligence and Other Technologies* (BSB Handbook · Current Guidance · effective 18 May 2026). The tool now enforces: 3×3 risk-based approach matrix · AI audit logs (rC87.2) · rC86 outsourcing classification · rC19 transparency gate · rC20 human-in-the-loop · plus Hamid-jurisdiction case-law awareness (Ayinde · Al-Haroun [2025] EWHC 1383 Admin · Munir [2026] UKUT 81 IAC · Oakley [2024] UKFTT 315 GRC). See the full mapping below.

---

## 🛡️ BSB AI Guidance Compliance

> **Effective 18 May 2026** — The Bar Standards Board has issued *Guidance on the use of Artificial Intelligence and Other Technologies* (BSB Handbook · Current Guidance), binding on all barristers and chambers in England & Wales. This tool was designed for compliance at the architecture layer. The protocols below are not adopted optionally — they are wired into the firm's brain, agents, and skills so every session honours them by default.

### The Six BSB Pillars — How This Tool Maps

| BSB Pillar | What It Requires | How This Tool Delivers |
|---|---|---|
| **1. General Ethics** | CD1-CD10 apply to AI use as to all professional conduct | All 10 Core Duties mapped in [BSB_GUIDANCE_COMPLIANCE.md](docs/BSB_GUIDANCE_COMPLIANCE.md) |
| **2. Competent Use** | Barristers must understand the tools they deploy (rC89) | MIT-licensed open source — fully auditable. Dual-mode architecture: local-default (Ollama) or cloud-LLM with internalised Pseudonymisation Gateway sanitisation. Verifiable in source. |
| **3. Before Adoption** | Due diligence against rC86.3 conditions | **Local mode**: confidentiality safeguards met by absence of transmission. **Cloud mode**: Pseudonymisation Gateway substitutes party names + government IDs + case references with placeholders before any prompt leaves your machine. CD mapping documented. Client consent gate built in (rC19). Override/monitor via human-in-the-loop. You retain rC86.3 responsibility — verify Gateway coverage for your matter's specific identifiers and execute vendor DPA before invoking cloud mode for client-confidential work. |
| **4. Setting Procedures** | Chambers must have documented AI procedures (rC87) | [AI Governance Policy Template](examples/AI_GOVERNANCE_POLICY_TEMPLATE.md) — chambers-customisable, covering acceptable uses, record keeping, data governance, ICO LOCS alignment. |
| **5. Each Use** | Risk assessment, verification, audit trail for every AI interaction | 3×3 risk matrix auto-classification · 2-source citation verification · AI audit log (90-day retention) · Transparency gate (rC19) · Human-in-the-loop gate (rC20) · No bulk-execute, no auto-emit |
| **6. Others Using AI** | Supervise pupils, juniors, and external AI use | Compliance Officer flags cloud AI risks. rC86 outsourcing classification warns on third-party AI tools. |

### The BSB's Key Concern — And This Firm's Answer

The BSB AI Guidance states:

> *"It is unlikely that free-of-charge, publicly available AI systems fulfil these conditions [rC86-89] for use with client-confidential or court-facing legal work."*

**AI Brain — UK is the answer.** It is not a free-of-charge, publicly available cloud AI. It is a professional tool with a **dual-mode architecture**: local-default (the `connect-local` command configures Ollama + Qwen3 to run the language model on your laptop — nothing leaves the machine) and cloud-optional (Claude / Gemini / DeepSeek for users who choose them for quality reasons, with the internalised Pseudonymisation Gateway sanitising party names + government IDs + case references before any prompt leaves your machine). Every feature — from audit logs to citation verification to the transparency gate to the Gateway sanitisation in cloud mode — is purpose-built for BSB compliance.

See [docs/BSB_GUIDANCE_COMPLIANCE.md](docs/BSB_GUIDANCE_COMPLIANCE.md) for the full rule-by-rule mapping, including Core Duties CD1-CD10, rC86-rC123, and Hamid-jurisdiction case-law (Ayinde & Al-Haroun [2025] EWHC 1383 Admin, Munir [2026] UKUT 81 (IAC), Oakley v Information Commissioner [2024] UKFTT 315 (GRC)).

---

## 🌐 Choose your language

| Script | Language | Region | Guide |
|---|---|---|---|
| 🇬🇧 | **English** | All UK jurisdictions · Default | [GETTING_STARTED.md](GETTING_STARTED.md) |
| 🏴󠁧󠁢󠁷󠁬󠁳󠁿 | **Cymraeg (Welsh)** | Wales | [GETTING_STARTED_WELSH.md](GETTING_STARTED_WELSH.md) |
| 🏴󠁧󠁢󠁳󠁣󠁴󠁿 | **Gàidhlig (Scottish Gaelic)** | Scotland | [GETTING_STARTED_SCOTTISH_GAELIC.md](GETTING_STARTED_SCOTTISH_GAELIC.md) |
| 🇮🇪 | **Gaeilge (Irish)** | Northern Ireland · cross-border | [GETTING_STARTED_IRISH.md](GETTING_STARTED_IRISH.md) |

> 🙏 **Honest note:** Welsh, Scottish Gaelic, and Irish guides were AI-assisted. **Native-speaker PRs warmly welcome** via [TRANSLATION_HELP_WANTED.md](TRANSLATION_HELP_WANTED.md). Your dialect is your dignity; help us get it right.

---

## 💛 Why this exists

> The UK solo legal market faces multiple compounding pressures:
> - **2026 SRA fee hike (~29%)** + Making Tax Digital mandate (April 2026 for earners >£50k)
> - **Post-Brexit retained EU law turbulence** — REUL Act 2023 sunsetting · UK GDPR divergence · Data (Use and Access) Bill
> - **~45% of working day** estimated on non-billable admin (citations · court diary · compliance · deadlines)
> - **SRA Code of Conduct technological competence** obligation means lawyers must understand the tools they use

Magic Circle firms have legal-engineering teams. Solo solicitors don't. We built this so a UK solo practitioner — whether SRA-regulated solicitor in Cardiff or BSB-regulated barrister in Inner Temple chambers — can have a second brain that costs **£0 forever**, runs locally by default (Ollama + Qwen3), and supports SRA Rule 6.3 / BSB rC15 confidentiality at the architecture layer — either by absence of transmission (local mode) or by Pseudonymisation Gateway sanitisation (cloud mode).

---

## 🧠 What's inside — specialists who live in your terminal

| # | Specialist | What they do for you |
|---|---|---|
| 🧠 | **The Receptionist (brain)** | Listens to what you say. Figures out who you need. Calls the right specialist. You never memorize commands. |
| 📂 | **The Matter Manager** | Holds every active matter — parties, prayers, hearings, orders, draft state. Walk into court · context comes back instantly. |
| 📜 | **The Citation Clerk** | Parses UK citations — OSCOLA 4th ed. format (neutral citations · law reports · case names). **v0.2 BSB AI Guidance:** 2-source independent verification routine. Flags any AI-generated citation that cannot be independently verified as "rC9.1 risk — DO NOT CITE without verification." See Ayinde & Al-Haroun [2025] EWHC 1383 Admin. |
| 🏛️ | **The Court Registrar** | Knows the UK court hierarchy: UK Supreme Court · Court of Appeal · High Court divisions · Crown Court · County Court · Magistrates' Court · Tribunals · plus Scottish Court of Session · High Court of Justiciary · Sheriff Courts · plus NI court structure. |
| ✍️ | **The Drafting Assistant** | Ships with **107 UK drafting templates** in [`_drafting_data/`](_drafting_data/) covering: contracts (sale of goods · services · employment · NDA · tenancy · commercial lease · shareholders · loan · settlement) · pleadings (N1 · particulars · defence + counterclaim · reply · witness statement) · motions (N244 · summary judgment · strike-out) · evidence (statement of truth · ET1) · pre-action + settlement (letter before claim · consent · Tomlin · Part 36) · costs (Form Precedent H · bill of costs · retainer) · insolvency (statutory demand · winding-up · administration · IVA · individual bankruptcy) · style guides (drafting · OSCOLA citation · formatting per PD 5A) **plus 62 litigation-backbone templates** covering all 13 categories: appeals (N161 · grounds · skeleton · permission · SC) · injunctions (without-notice · freezing · search · undertaking · interim skeleton) · disclosure (DRD PD 57AD · N265 · privilege log · redaction · models A-E) · expert evidence (CPR Part 35 instruction · report · joint statement · SJE · cross-exam) · default judgment (N225/N227 · set aside) · enforcement (HCEO · charging order · TPDO · attachment of earnings · writ of control) · skeleton arguments (trial · CMC · directions · interim · summary judgment) · counsel briefing (brief · merits · evidence · settle pleadings · conference) · judicial review (N461 · grounds · AoS N462 · permission skeleton · summary grounds of resistance) · trial documentation (bundle · authorities · chronology · cast list · reading list · opening · closing · PD 57AC compliance) · ADR (mediation position · agreement · settlement deed · WP protocols) · insolvency-beyond-statutory-demand · specialist tribunals (FTT Tax · UT Tax · Immigration · Property Chamber). **Plus 10 Tier-1 statute digests** in [`_statute_corpus/`](_statute_corpus/) covering Companies Act 2006 · DPA 2018 + UK GDPR · Consumer Rights Act 2015 · Employment Rights Act 1996 · Equality Act 2010 · CPR 1998 · Solicitors Regulation + LSA 2007 · Data (Use and Access) Act 2025. **Plus 6 procedural-anchor index files** (CPR PDs · CrimPR PDs · FPR PDs · Pre-Action Protocols · Court Guides · Costs CPR 44-47). |
| 🛡️ | **The Compliance Officer** | BSB AI Guidance (May 2026) expanded rule set. Covers rC86 (AI outsourcing), rC86.3 (conditions), rC87/rC89 (practice management), rC9.1/rC9.2 (court misleading), rC15 (confidentiality), rC19 (transparency), rC20 (personal responsibility — cannot delegate to AI), rC123 (Public Access AI-reliance). All 10 Core Duties mapped. Hamid jurisdiction case-law: Ayinde & Al-Haroun [2025] EWHC 1383 Admin, Munir [2026] UKUT 81 (IAC), Oakley v Information Commissioner [2024] UKFTT 315 (GRC). |
| ⚖️ | **The Risk Assessor** | BSB 3×3 risk matrix — auto-classifies every session by application (admin / general client / court+vulnerable+protected characteristics), use (spelling / research / drafting+agentic), and technology (spelling tools / legal-specific AI / agentic cloud). Warns on high-risk combinations. Logs to audit trail. |
| 📋 | **The Audit Clerk** | Always-on AI audit log — prompt + output + timestamp + user-confirmed flag. 90-day default retention with enforced deletion policy. Stored at `~/.ailawfirm_uk/audit_logs/`, never transmitted. rC87.2 practice management compliance. |
| 🔐 | **The Transparency Gate** | rC19 gate: before any client-facing artifact is finalised, prompts "Has the client been informed of AI use per rC19? [y/N]" — logs response. rC20 human-in-the-loop gate: every drafting/agentic action requires explicit confirmation. No bulk-execute. No auto-emit. |
| 👥 | **The Direct Access Detector** | If matter is marked "Public Access scheme / Direct Access," triggers rC123 routine: confirms client understands AI involvement before proceeding. |
| 📅 | **The Calendar Sync** | ICS feed sync to iPhone Calendar / Google Calendar / Outlook — no third-party API, no data processor. code-aliased summary line (lock-screen safe) · full matter detail in event body. Timezone Europe/London (BST-aware). |

---

## 🚀 Install in 30 minutes

### Step 1 — Pick your operating system

| OS | Guide |
|---|---|
| 🍎 **Mac** | [MAC_INSTALL.md](MAC_INSTALL.md) — Terminal, common gotchas |
| 🪟 **Windows** | PowerShell · standard pip install |
| 🐧 **Linux** | Same commands as Mac |

### Step 2 — Install Python (one-time) + the tool

```bash
pip install git+https://github.com/Wolfgangrush/ai-law-firm-uk.git
```

### Step 3 — Connect an AI brain (ONE COMMAND)

```bash
ailawfirm-uk connect-local
```

This single command:
1. Detects if Ollama is installed; if not, prints platform-specific install instructions
2. Detects your laptop's RAM
3. Recommends and downloads the right Qwen3 model (14b for 16GB+ · 7b for 8GB · 1.7b for older laptops)
4. Writes config so all subsequent calls route to local Ollama
5. Runs a smoke test to confirm local connectivity

After this, **no queries leave your laptop**.

Three honest model options — see [MODEL_SETUP.md](MODEL_SETUP.md):

| Choice | Cost | Privacy | Best for |
|---|---|---|---|
| 🥇 **Local Ollama + Qwen3** | £0 forever | 🟢 Perfect — nothing leaves your laptop | **Client matters · SRA Rule 6.3 / BSB rC15 confidentiality · UK GDPR-sensitive work** |
| 🥈 **DeepSeek API** | ~£2-5/mo | ⚠️ Acceptable IF opt-out — but China is NOT on UK ICO adequacy list; UK GDPR Chapter V applies | Non-client work · public-law research · templates |
| 🥉 **Claude / Gemini API** | ~£25-70/mo | 🟢 Strong (enterprise privacy default-ON) | Heavy daily users with executed Article 28 DPA + Schrems-II supplementary measures |

### Step 4 — Run

```bash
ailawfirm-uk
```

Sample commands:

```
> tell me about the Court of Session Outer House jurisdiction
> validate [2023] UKSC 42
> check this advert: "Best contentious-probate solicitor in London"
> what's the limitation for breach of contract under the Limitation Act 1980?
> add hearing MAT-2026-014 Inner London Crown Court 2026-06-09 10:00 BST
> sync calendar
```

---

## 🔒 Privacy & Data Handling — what stays where

**Architecture — three pieces decide your privacy posture:**

**(1) Local-only state.** Your matters, drafts, audit logs, calendar entries, and configuration live in `~/.ailawfirm_uk/`. Never uploaded by the tool. Never synced to a third-party cloud by the tool. No telemetry. No "anonymous usage statistics." The publisher operates zero infrastructure and cannot access this folder. Verifiable via `grep -ri "telemetry\|analytics\|requests.post\|urlopen" ailawfirm_uk/` — should return only user-initiated cloud-LLM calls.

**(2) LLM backend — you choose.** The default `connect-local` command configures Ollama + Qwen3 to run the language model on your laptop (truly nothing leaves). If you opt into a cloud-LLM tier (DeepSeek / Claude / Gemini) for quality reasons, see the tier table above for cost + privacy trade-offs.

**(3) Pseudonymisation Gateway — always-on for cloud mode.** When you configure a cloud-LLM provider in `~/.ailawfirm_uk/config.json`, the internalised `PseudonymisationGateway` (source: `ailawfirm_uk/pseudonymisation.py` — 12 tests in `tests/test_pseudonymisation.py`) automatically substitutes real names, government IDs (NI Number · NHS Number · UTR · UK VAT · Aadhaar for Indian-diaspora matters), contact identifiers (phone · email), and case references (EWHC / EWCA / UKSC numbers) with deterministic placeholders BEFORE the prompt leaves your machine. The placeholder ↔ original map lives in memory only (never written to disk; destroyed when the gateway goes out of scope). Cloud vendors see only the abstract structure of the matter; the user sees real values restored in the response.

The wedge: every other cloud-AI legal tool sends raw client PII to the LLM by default. wolfgang_rush AI Brain — UK ships Ollama-first AND ships the Gateway as the privacy primitive that closes the gap when you choose cloud mode for quality reasons.

### What goes to the API provider during each query

Each time the firm reasons about a matter, the following are sent to your chosen API provider:
- Your prompt (the question or instruction)
- Relevant context the firm pulls from your local matter folder (current draft state, recent orders, citations being verified)

Your full matter history, audit logs, and unrelated cases are NOT sent. The firm sends the minimum context needed to answer the current question.

### What API providers contractually guarantee

| Provider | Trains on your data? | Retention | Source |
|---|---|---|---|
| **Claude API** (Anthropic) | ❌ No — Commercial Services data is not used for training | ~30 days for safety/abuse review (Zero Data Retention available on enterprise contract) | [Anthropic Privacy Policy](https://www.anthropic.com/legal/privacy) · [Commercial Terms](https://www.anthropic.com/legal/commercial-terms) |
| **OpenAI API** (GPT-4) | ❌ No — API data not used for training since March 2023 | ~30 days for abuse review (ZDR available) | [OpenAI API Data Usage Policies](https://openai.com/policies/api-data-usage-policies) |
| **Gemini API (paid via Vertex AI)** | ❌ No — paid-tier API data not used for training | Per Google Cloud contract | [Vertex AI data governance](https://cloud.google.com/vertex-ai/docs/general/data-governance) |
| **Gemini Free Tier** | ⚠️ **YES — Google AI uses free-tier prompts to improve products** | — | [Google AI Studio terms](https://ai.google.dev/gemini-api/terms) — **DO NOT use free-tier Gemini for confidential client matters.** |
| **DeepSeek V4 Pro API** | ❌ No — per DeepSeek API terms, inputs/outputs not used for model training | Retention policy less documented than OpenAI/Anthropic; verify for matter sensitivity | [DeepSeek API ToS](https://platform.deepseek.com/api-docs/legal) · **Note:** provider is China-based; consider jurisdictional data-residency requirements |

### What that does NOT mean — solicitor's residual risk

Even though API data is not used for training:

1. **Data IS in transit** during each query — it passes through the provider's infrastructure
2. **Brief logging retention** (typically 30 days) means the provider holds the data for that window
3. **Lawful access requests** — a subpoena, lawful intercept warrant, GDPR data-subject access request, or provider security incident could expose data during the retention window
4. **Provider-side breach risk** — however small, it exists

This is fundamentally different from local-LLM mode (where no data leaves your machine, ever, period). The `connect-local` command already configures Ollama + Qwen3 as the v0.1 default — solicitors handling confidential, privileged, or special-category data should stay in local-LLM mode for that work. The cloud-LLM tier exists for non-confidential research, public-law analysis, and template scaffolding where contractual no-training is a sufficient safeguard.

### Solicitor's decision

If your matter is:
- **General commercial / corporate / contract drafting** → Claude / OpenAI / paid Gemini API are appropriate. Contractual no-training protections are strong. Audit logs are local.
- **Legal-privileged client communication / privileged litigation strategy** → Evaluate against your jurisdiction's professional conduct rules. Most regulators permit reasoned use of cloud-AI with disclosure to the client. (See England & Wales (SRA / BSB) guidance.) Document the choice in your audit log.
- **GDPR special-category data / health / criminal record / political opinion** → Stay in `connect-local` (Ollama + Qwen3) mode. Do not opt into any cloud-LLM tier for these matters; do not use free-tier Gemini.
- **State secrets / classified material / under-seal court orders** → Stay in `connect-local` (Ollama + Qwen3) mode. For physically air-gapped networks where the pip-install / model-download / auto-update paths are also prohibited, await the v0.3+ signed offline-install bundle below.

The firm's audit log captures every API call (timestamp, agent, prompt-summary, output-summary) at `~/.ailawfirm_uk/audit_logs/`. Logs never leave your machine. They are your professional-conduct compliance trail.

### v0.3+ roadmap

> What v0.1 already ships: (a) local-LLM default via `connect-local` (Ollama + Qwen3 — nothing leaves your laptop in local mode), (b) configurable cloud-LLM tier covering Claude / OpenAI / paid Gemini / DeepSeek, (c) Pseudonymisation Gateway sanitising PII before any cloud-LLM call, and (d) no first-party telemetry. The items below extend the floor — they are not a future replacement for what is already shipped.

- **Signed offline-install bundle** — the `pip install` path currently touches PyPI and the Ollama model registry; v0.3+ ships a signed offline-installable archive with the Qwen3 model pre-bundled, removing the last network-touch point even at install time. For solicitors on physically air-gapped networks (under-seal court matter rooms, state-secret-clearance environments, prison-side advice).
- **In-firm LLM tenant adapter** — drop-in config for Azure OpenAI / private Vertex / on-prem vLLM endpoints. Distinct from the today-shipped public-API cloud-LLM tier; targets solicitors whose firm already provisions LLM infrastructure under its own DPA.
- **Expanded local-model surface** — Llama 3.3 70B / Qwen 2.5 72B / DeepSeek V4 Pro (open-weights via Ollama), for solicitors with larger laptops who want better-than-Qwen3-14b local reasoning.

Tracked at: [drafting-agents-core issues](https://github.com/Wolfgangrush/drafting-agents-core/issues).

---

**No agenda · no telemetry · no cloud-default · MIT licensed · £0 forever.**

**England & Wales (SRA / BSB) Rule compliance built into the tool's audit + transparency-gate architecture.** Solicitor remains professionally responsible for every output. The firm is a force-multiplier, not a substitute for judgment.

---

## ⚖️ Why this differs from ChatGPT / Claude.ai

The BSB AI Guidance (May 2026) states that **"it is unlikely that free-of-charge, publicly available AI systems fulfil these conditions [rC86-89]"** for use with client-confidential or court-facing legal work. Here's why:

| Concern | ChatGPT / Claude.ai (Free/Cloud) | AI Brain — UK (dual-mode) |
|---|---|---|
| **Data location** | Your prompts and client data are transmitted to third-party cloud servers (US-based) in the clear. | **Local mode**: everything runs on your laptop; zero data transmission. **Cloud mode**: only Pseudonymisation-Gateway-sanitised prompts (placeholders substituted for real PII) are transmitted, going direct to your chosen vendor — the publisher is not in the data path. |
| **LPP preservation** | Cloud transmission may waive Legal Professional Privilege. See Munir [2026] UKUT 81 (IAC). | **Local mode**: LPP preserved by architecture (absence of cross-vendor transmission). **Cloud mode**: Pseudonymisation Gateway substitutes party names + privileged identifiers with placeholders BEFORE any prompt leaves your machine; cloud vendor sees only abstract matter structure. You remain responsible for executing your vendor DPA + Article 28 + UK GDPR Schedule 21 supplementary safeguards before invoking cloud mode for privileged work — see Munir [2026] UKUT 81 (IAC). |
| **rC15 confidentiality** | Data entered = potential unauthorised disclosure. BSB specifically flags this as a compliance risk. | **Local mode**: data does not leave your machine. **Cloud mode**: PII is sanitised via Pseudonymisation Gateway before transmission. You retain rC15 responsibility — verify the Gateway's coverage of your matter's specific identifiers before relying on cloud mode for confidential work. |
| **rC86.3 due diligence** | You cannot audit the model, the infrastructure, or the data handling. | MIT-licensed open source. Fully auditable. You control the model (Ollama + Qwen3 in local mode; vendor-of-choice in cloud mode). Gateway sanitisation logic is in `ailawfirm_uk/pseudonymisation.py` with 12 tests. |
| **rC87 audit trail** | No built-in legal audit logging. Prompt history is outside your chambers' control. | Always-on AI audit log. 90-day retention. Stored locally at `~/.ailawfirm_uk/audit_logs/`. Never transmitted by the tool. |
| **rC19 transparency** | No built-in client disclosure mechanism. | Transparency gate prompts before every client-facing output. |
| **rC20 personal responsibility** | No guardrails against blind reliance on AI output. | Human-in-the-loop gate. Citation 2-source verification. No auto-emit. |
| **UK GDPR compliance** | US-based cloud providers require Schrems-II supplementary measures + Article 28 DPA — and your raw client PII transits in cleartext. | **Local mode**: UK GDPR international-transfer triggers do not fire. **Cloud mode**: the international transfer is YOUR action (the publisher is not a controller or processor — see [NO_PII_NO_DATA.md](NO_PII_NO_DATA.md)); Gateway sanitisation reduces but does not eliminate Schrems II exposure. You must execute Chapter V Article 46 supplementary safeguards + Article 28 DPA with your vendor. |
| **Cost** | Free tier monetises your data. Paid tiers cost £20-200+/mo. | £0 forever in local mode. ~£2-70/mo if you opt into a cloud tier. |

**The BSB designed the guidance to regulate tools like ChatGPT and Claude.ai.** This tool was designed to comply with that guidance. The difference is architectural — local-default with cloud-mode-via-Gateway is the foundation, and you choose which mode each session runs in.

---

## 📁 Where your data lives

```
~/.ailawfirm-uk/                     ← Mac/Linux
C:\Users\YourName\.ailawfirm-uk\     ← Windows
├── palace/                          ← all matter/client/citation memory (ChromaDB)
├── config.json                      ← your settings (AI provider · jurisdiction · prefs)
├── calendars/                       ← generated .ics feeds for iPhone/Outlook subscribe
└── people_map.json                  ← optional client alias system (lock-screen safety)
```

Copy this folder to a USB drive · OneDrive · iCloud Drive · Dropbox = complete backup of your practice in 5 seconds.

---

## 🔄 How to update your firm

When a new version of AI Brain — UK is published, you pull it in with **one command**. Your matter data + your project-root `CLAUDE.md` are **never touched** — only the firm's installed code, skills, and prompts refresh.

### Path 1 — Plain terminal

```
ailawfirm-uk update
```

Under the hood this runs `pip install --upgrade git+https://github.com/Wolfgangrush/ai-law-firm-uk.git`. After it finishes, restart any open `ailawfirm-uk` session so the new skills + prompts load.

### Path 2 — Inside Claude Code

Type:

```
/update
```

Claude runs the same command for you and reports the result.

### Path 3 — Inside Gemini CLI

Type:

```
/update
```

Same outcome — Gemini calls `ailawfirm-uk update` for you.

### When to update

- **The publisher tells you** a new version is out → update.
- **Monthly hygiene** → update once a month so you stay current on skills + bug fixes.
- **After hitting a bug** → first thing to try is updating, in case it is already fixed upstream.

### What does NOT update (by design)

- Your matter folders (`~/Desktop/<your-firm>/<matter>/...`)
- Your project-root `CLAUDE.md` (your customisations always win)
- Your `~/.ailawfirm-uk/` config + palace data
- Your chosen AI model setup (Ollama · DeepSeek · Claude · Gemini)

Only the firm's installed Python code, skills, and template files refresh. Your practice is unaffected.

### One catch — existing users + new template rules

If a new version updates the template `CLAUDE.md` (the firm's standing rules), your project-root `CLAUDE.md` is preserved because your customisations always win. To see what changed in the template after an update:

```
diff CLAUDE.md "$(python3 -c 'import ailawfirm_uk, os; print(os.path.join(os.path.dirname(ailawfirm_uk.__file__), "templates/CLAUDE.md"))')"
```

Review the diff and merge what you want into your own `CLAUDE.md`.

---

## 🛤️ Roadmap (honest)

> 🙏 **Honest note on timelines:** Solo-author OSS · ships as time permits · v0.2 / v0.3 / v0.4+ targets are indicative, not committed dates. Open an issue if a specific feature on a specific timeline matters to your work.



- **v0.1.0** *(shipped)* — bootstrap: architecture, brain layer with 10-intent classifier, 7 specialist agents (4 live · 3 stubs), 3 working MCP tools (court · citation · calendar), 4-language onboarding (English · Welsh · Scottish Gaelic · Irish), connect-local one-command CLI, LEGAL_EXPOSURE_PLAYBOOK v0.1 compliance
- **v0.2 — knowledge layer** *(shipped 2026-05-28)* — **107 drafting templates** in `_drafting_data/` covering: (a) Tier-1 + Tier-2 contracts and pleadings (9+19) — sale of goods · services · employment · NDA · tenancy · commercial lease · shareholders · loan · settlement · N1 · particulars · defence + counterclaim · reply · witness statement · N244 · summary judgment · strike-out · statement of truth · ET1 · letter before claim · consent · Tomlin · Part 36 · Form Precedent H · bill of costs · retainer · statutory demand · N434; (b) Tier-3 specialist (8) — Family Form A + C100 + statement-in-support · Criminal basis of plea + defence statement + bail · Land Registry TR1 + AP1; (c) full 13-category litigation backbone (62 templates) — appeals · injunctions · disclosure (PD 57AD) · expert evidence (CPR Part 35) · default judgment · enforcement (HCEO · charging order · TPDO · attachment of earnings · writ of control) · skeleton arguments · counsel briefing · judicial review (N461) · trial documentation (PD 57AC) · ADR · insolvency (winding-up · administration · IVA) · specialist tribunals (Tax FTT/UT · Immigration · Property Chamber); (d) 6 procedural-anchor index files (CPR PDs · CrimPR PDs · FPR PDs · Pre-Action Protocols · Court Guides · Costs CPR 44-47); (e) 3 style guides (drafting · OSCOLA citation · formatting per PD 5A — expanded with bundles + PD 57AC + electronic filing). **Plus 10 statute digests** in `_statute_corpus/` (Companies Act 2006 · DPA 2018 + UK GDPR · Consumer Rights Act 2015 · Employment Rights Act 1996 · Equality Act 2010 · CPR 1998 · Solicitors Regulation + LSA 2007 · Data (Use and Access) Act 2025).
- **v0.1.1 — Pseudonymisation Gateway** *(shipped 2026-05-29)* — internalised at `ailawfirm_uk/pseudonymisation.py`; sanitises PII before any cloud-LLM call. Standalone source at [pseudonymisation-gateway](https://github.com/Wolfgangrush/pseudonymisation-gateway).
- **v0.2 — frontend / UX layer** *(in progress)* — matter dashboard · section-by-section statute depth for Tier-2 statutes (Limitation Act · POCA · Bribery Act · ECCTA 2023) · SRA Code + BSB Handbook deep digests
- **v0.3** *(following milestone)* — **firm mode** for multi-solicitor practices · role/permission · matter assignment · conflict-check (SRA Rule 6.5) · client-account compliance (SRA Accounts Rules)
- **v0.4+** — BAILII / Westlaw-public / Lexis-public cross-reference · Apple EventKit native · CalDAV bidirectional sync · deeper Scottish + NI jurisdiction-specific modules · sectoral specialisms (construction · IP licensing · admiralty · medical-disciplinary)

Six sister jurisdictions on the same architecture: 🇮🇳 India · 🇸🇬 Singapore · 🇦🇺 Australia · 🇦🇪 Dubai-DIFC · 🇪🇺 EU · 🇺🇸 USA — each as its own MIT-licensed repo.

---

## 🌐 Family Status (honest · cross-firm)

The wolfgang_rush AI Brain family ships across 7 jurisdictions. Honest status of the v0.2 legal-knowledge layer (statute corpus + drafting data) per firm:

| Firm | Statute corpus | Drafting corpus | Shared agents | GitHub |
|------|---|---|---|---|
| 🇮🇳 **India** | Native knowledge base · maintainer-curated | wolfgang_rush plugins (14 Indian-litigation plugins · separate stack) | Not applicable — Indian-specific | ✅ LIVE |
| 🇪🇺 **EU** | ✅ 11 statutes · 8/8 Tier-1 | ✅ **56 templates** · litigation + commercial complete (v0.2 closed 2026-05-28) | ✅ Migrated | ✅ LIVE |
| 🇦🇺 **Australia** | ✅ 13 Tier-1 statute digests + 39 research files | ✅ **79 templates** · litigation + commercial + tribunal complete (v0.2 closed 2026-05-28) | ✅ Migrated | ✅ LIVE |
| 🇦🇪 **Dubai-DIFC** | ✅ 24 statute digests · dual-track (15 DIFC + 9 Mainland UAE Federal) · v0.2 closed 2026-05-29 | ✅ **81 templates** · dual-track DIFC + Mainland · litigation + commercial + tribunal complete (v0.2 closed 2026-05-28) | ✅ Migrated | ✅ LIVE |
| 🇸🇬 **Singapore** | ✅ 17 statute digests Tier-1 | ✅ **55 templates + 6 scaffolds** · litigation + commercial + regulatory complete (v0.2 closed 2026-05-28) | ✅ Migrated | ✅ LIVE |
| 🇬🇧 **UK** | ✅ 10 statute digests Tier-1 | ✅ **107 templates** · litigation + commercial + Tier-3 specialist + procedural anchors complete (v0.2 closed 2026-05-28) | ✅ Migrated | ✅ LIVE |
| 🇺🇸 **USA** | ✅ 23 federal-first Tier-1 statute digests | ✅ **89 templates** · all 13 litigation categories + commercial + corporate complete (v0.2 closed 2026-05-29) | ✅ Migrated | ✅ LIVE |

**Plus:**
- **AI Startup Firm — India v0.1** (legal-ops brain for founders)
- **GC In-House Brain** (multi-jurisdictional, 8 modules — 3 live · 5 shipping v0.2+)

Both share the same `drafting-agents-core` architecture pattern.

All firms migrated to the central [drafting-agents-core](https://github.com/Wolfgangrush/drafting-agents-core) agent library on 2026-05-20 (Path B-Lite) — single source of truth for the agent layer; jurisdictional knowledge stays per-firm.

---

## 📚 Documentation

| File | What it covers |
|---|---|
| [GETTING_STARTED.md](GETTING_STARTED.md) + 3 Celtic language variants | Layman-friendly 30-minute tour |
| [MAC_INSTALL.md](MAC_INSTALL.md) | Mac-specific install with common gotchas |
| [DISCLAIMER.md](DISCLAIMER.md) | Full legal disclaimer · SRA + BSB conduct rules · UK GDPR controller/processor analysis · UPL exclusion |
| [NO_PII_NO_DATA.md](NO_PII_NO_DATA.md) | Zero-collection architecture · UK GDPR + DPA 2018 + Chapter V analysis |
| [SECURITY.md](SECURITY.md) | Vulnerability reporting · coordinated disclosure · security hygiene |
| [MODEL_SETUP.md](MODEL_SETUP.md) | Honest privacy table · local vs cloud · third-party CLI tool warning |
| [SCOPE.md](SCOPE.md) | What's in v0.1, what's not |
| [KNOWLEDGE_PROVENANCE.md](KNOWLEDGE_PROVENANCE.md) | Every domain claim's source (CITED:<research-file>) |
| [TRANSLATION_HELP_WANTED.md](TRANSLATION_HELP_WANTED.md) | Community call for native-speaker translation PRs |
| [BSB_GUIDANCE_COMPLIANCE.md](docs/BSB_GUIDANCE_COMPLIANCE.md) | Full BSB AI Guidance compliance mapping — all Core Duties, rules (rC86-rC123), and Hamid case-law (Ayinde, Al-Haroun, Munir, Oakley) |
| [AI_GOVERNANCE_POLICY_TEMPLATE.md](examples/AI_GOVERNANCE_POLICY_TEMPLATE.md) | Chambers-customisable AI governance policy — acceptable uses, record keeping, data governance, ICO LOCS alignment |

---

## 🙏 Credits

- **Engine — all architectural credit:** a local memory architecture — the highest-scoring open-source AI memory system ever benchmarked. MIT licensed. We are a downstream fork specialized for UK solo practice.
- **Publisher:** [wolfgang_rush](https://github.com/Wolfgangrush) — an Indian advocate (High Courts of India, India). MIT-licensed legal-tech publisher.
- **Inspired by:** every UK solo solicitor who's worked Saturday morning on a fast-track listing in the County Court.

---

## ⚠️ Disclaimer

This tool helps you organize your practice. It does **NOT** give legal advice. It does **NOT** replace your professional judgment. It does **NOT** solicit work on your behalf. SRA Code §8 / BSB rC8 publicity firewall is built in but **YOU** remain responsible for compliance with all bar/society conduct rules, UK GDPR, POCA, and the Legal Services Act 2007.

The publisher is not admitted in any UK jurisdiction. The publisher does not offer legal services in the UK. This is a software publication under the MIT License.

Ships AS-IS without warranty. See [LICENSE](LICENSE).

---

## 📞 Support

- **Issues / bugs:** https://github.com/Wolfgangrush/ai-law-firm-uk/issues
- **Translation help:** [TRANSLATION_HELP_WANTED.md](TRANSLATION_HELP_WANTED.md) (Welsh · Scottish Gaelic · Irish PRs welcome)
- **Want to add a feature?** Open an issue with `[feature-request]` label

---

`Let's begin. Gadewch i ni ddechrau. Tòisichidh sinn. Tosaímid.` 🙏
