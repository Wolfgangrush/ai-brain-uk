# Getting Started — AI Brain UK · Solo Edition · v0.1

**Authoritative English guide.** For Welsh, Scottish Gaelic, or Irish, see the language picker in [README.md](README.md).

---

## What is AI Brain UK?

AI Brain UK is a local-first practice OS for UK solo solicitors and barristers. It automates repetitive legal-administrative tasks — court lookups, OSCOLA citation validation, calendar sync, and regulatory compliance checks — using an on-device AI brain.

It is **not a robot lawyer**. It does not file documents, correspond with clients, or replace your professional judgment. It is a practice tool, like your case management system or your diary — but smarter.

## Who this is for

- **Sole solicitors** regulated by the SRA, running a high-street or virtual practice
- **Self-employed barristers** regulated by the BSB, practicing from chambers
- **In-house counsel** transitioning to solo practice
- **Cross-border specialists** needing UK-specific compliance checks alongside international work

## System Requirements

- Python 3.9 or later
- macOS, Windows, or Linux
- 2 GB free disk space (for ChromaDB embeddings)
- No API key required for core functionality (local mode)

---

## Quick Install (macOS)

```bash
# 1. Clone the repo
git clone https://github.com/Wolfgangrush/ai-law-firm-uk.git
cd ai-law-firm-uk

# 2. Create virtual environment
python3 -m venv .venv
source .venv/bin/activate

# 3. Install
pip install -e .

# 4. Initialize
ailawfirm-uk init

# 5. Verify
ailawfirm-uk status
```

See [MAC_INSTALL.md](MAC_INSTALL.md) for detailed macOS instructions including Homebrew prerequisites.

## Quick Install (Windows)

```powershell
git clone https://github.com/Wolfgangrush/ai-law-firm-uk.git
cd ai-law-firm-uk
python -m venv .venv
.venv\Scripts\activate
pip install -e .
ailawfirm-uk init
ailawfirm-uk status
```

See [WINDOWS_INSTALL.md](WINDOWS_INSTALL.md) for detailed Windows instructions.

## Quick Install (Linux)

```bash
git clone https://github.com/Wolfgangrush/ai-law-firm-uk.git
cd ai-law-firm-uk
python3 -m venv .venv && source .venv/bin/activate
pip install -e .
ailawfirm-uk init
ailawfirm-uk status
```

---

## What you get (v0.1)

### 3 MCP Tools
| Tool | What it does |
|---|---|
| `uk_court_lookup` | Fuzzy-search UK courts by name → returns tier, jurisdiction, location, procedural code |
| `uk_citation_validator` | Validates OSCOLA 4th ed. citations — neutral, traditional, and statute formats |
| `uk_calendar_sync` | Generates `.ics` calendar files for import into Calendar.app, Outlook, Google Calendar |

### 7 Specialist Agents
| Agent | Status |
|---|---|
| `compliance_agent` | Live — SRA §8, BSB rC8, UK GDPR, POCA keyword firewall |
| `court_agent` | Live — wraps uk_court_lookup |
| `citation_agent` | Live — wraps uk_citation_validator |
| `calendar_agent` | Live — wraps uk_calendar_sync |
| `matter_agent` | Stub (v0.2+) |
| `drafting_agent` | Stub (v0.2+) |
| `deadline_agent` | Stub (v0.2+) |

### MCP Client Setup (Claude Code)

Add to your MCP configuration:

```json
{
  "mcpServers": {
    "ailawfirm-uk": {
      "command": "python3",
      "args": ["-m", "ailawfirm_uk.mcp_server"]
    }
  }
}
```

---

## Configuring an LLM Provider

The brain's classifier runs locally on keyword matching. For advanced intent classification and drafting (v0.2+), you can connect an external LLM. See [MODEL_SETUP.md](MODEL_SETUP.md) for provider configuration (Claude, GPT, Gemini).

**Privacy note:** Any content you send to an external LLM provider leaves your machine. Use entity aliasing for client-identifying information.

---

## Calendar Setup

The `uk_calendar_sync` tool generates `.ics` files in `~/.ailawfirm-uk/calendar.ics`. Open this file in:

- **macOS Calendar.app:** File → Import → select `calendar.ics`
- **Outlook (macOS/Windows):** File → Import → select `calendar.ics`
- **Google Calendar:** Settings → Import & Export → upload `calendar.ics`

The calendar auto-refreshes on each sync. Timezone defaults to Europe/London with BST summer handling.

---

## Regulatory Coverage (v0.1)

| Regime | Coverage |
|---|---|
| **SRA Code of Conduct** | §8 publicity restrictions — keyword flagging |
| **BSB Handbook** | rC8 publicity rules for self-employed barristers |
| **UK GDPR + DPA 2018** | ICO breach notification (72-hour) keyword flagging |
| **Data (Use and Access) Act 2025** | CURRENCY flag — recent legislation |
| **POCA 2002 + MLR 2017** | AML/KYC keyword flagging |
| **SRA Accounts Rules** | Client money compliance gate |
| **ECCTA 2023** | Identity verification phase-in through 2026 |

**IMPORTANT:** v0.1 compliance_agent is a keyword firewall — it flags potential issues but does not provide legal advice. You remain responsible for regulatory compliance.

---

## Directory Structure

```
ai-law-firm-uk/
├── ailawfirm_uk/
│   ├── core/           # Shared legal domain (courts, citations, statutes, ontology)
│   │   └── calendar/   # ICS sync
│   ├── solo/           # Solo practitioner modules (v0.2+)
│   ├── firm/           # Multi-advocate modules (v0.3+)
│   ├── brain/          # Intent classifier + router
│   ├── agents/         # 7 specialist agents
│   ├── mcp_tools/      # 3 MCP tools
│   └── i18n/           # 4-language support
├── tests/              # Test suite
├── _research/          # Domain research (READ-ONLY)
├── GETTING_STARTED*.md # Onboarding guides (4 languages)
├── SCOPE.md            # v0.1 scope document
├── KNOWLEDGE_PROVENANCE.md  # Domain claim → research citation ledger
└── README.md           # Project README
```

---

## Current Limitations (v0.1)

- **Drafting assistance** (particulars of claim, defence, skeleton argument, witness statement) ships in v0.2
- **Deadline tracking** (limitation clock, case-management directions) ships in v0.2
- **Firm mode** (multi-user, billing, conflict-of-interest) ships in v0.3
- **Full UI translations** (Welsh, Scottish Gaelic, Irish) ship in v0.2
- **macOS EventKit** direct calendar integration ships in v0.2

---

## Privacy & Data

- Everything runs locally. No telemetry. No analytics. No cloud.
- Your client data stays in `~/.ailawfirm-uk/palace/` (ChromaDB).
- Calendar data stays in local `.ics` files.
- entity aliasing substitutes real names in calendar summaries for lock-screen safety.

See [MODEL_SETUP.md](MODEL_SETUP.md) for the LLM boundary discussion.

---

## Getting Help

- Read [SCOPE.md](SCOPE.md) to understand what's in v0.1 and what's coming
- Read [KNOWLEDGE_PROVENANCE.md](KNOWLEDGE_PROVENANCE.md) to see the research sources behind every domain claim
- File issues at [github.com/Wolfgangrush/ai-law-firm-uk/issues](https://github.com/Wolfgangrush/ai-law-firm-uk/issues)
- For Welsh/Scottish Gaelic/Irish speakers: [TRANSLATION_HELP_WANTED.md](TRANSLATION_HELP_WANTED.md)

---

## License

MIT — see [LICENSE](LICENSE). Built on MemPalace memory architecture (also MIT).

---

*Welcome, solicitor / barrister. Let's reduce the admin burden.*
