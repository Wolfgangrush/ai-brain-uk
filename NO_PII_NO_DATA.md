# NO_PII_NO_DATA — Zero-Collection Architecture (UK)

**This document explains, in detail, why AI Brain — UK collects no personal data from you, and what that means under UK GDPR and the Data Protection Act 2018.**

## The short version

The publisher (wolfgang_rush) operates **zero infrastructure** that touches your data. There is no server. There is no telemetry. There is no analytics. There is no "anonymous usage improvement data." The tool runs entirely on your laptop.

## The architectural guarantee

AI Brain — UK is **local-first** software. Specifically:

**(1) The codebase contains zero telemetry.** Verify with `grep -ri "telemetry\|analytics\|tracking\|requests.post\|urlopen" ailawfirm_uk/` — should return only legitimate cloud-AI calls (user-initiated, routed direct to your chosen vendor).

**(2) The publisher operates no server.** No AI Brain UK API. No cloud service. No database. The publisher's only infrastructure is the GitHub repository.

**(3) Storage is on your laptop.** Your matter data, citation cache, calendar entries, and configuration live under `~/.ailawfirm-uk/`. The publisher has no access to this folder.

**(4) Network calls are limited to:**
- Package installation (PyPI during `pip install`)
- User-initiated AI cloud calls (if you opt into cloud mode — direct to vendor, not through publisher)
- Optional update checks (v0.2+ if added — will be opt-in and check GitHub releases only)

## Cloud-mode (when you opt in)

If you choose to use cloud AI processing, your queries route **directly from your laptop to the AI vendor**. The publisher is not in the data path. The contract for cloud-mode usage is between **you** and the **AI vendor** under their terms of service.

For client-confidential work, do NOT use cloud mode. Use the local-only mode. See [MODEL_SETUP.md](MODEL_SETUP.md).

## UK GDPR implications

Under UK GDPR (the UK's post-Brexit equivalent of EU GDPR) and the Data Protection Act 2018:

**The publisher is NOT a controller.** A controller "determines the purposes and means of the processing of personal data" (Article 4(7)). The publisher determines neither — the user determines what to process; the user chooses where it gets processed.

**The publisher is NOT a processor.** A processor "processes personal data on behalf of the controller" (Article 4(8)). The publisher processes no data on anyone's behalf.

**The publisher is a software publisher.** Publishing open-source software is not a "processing" activity under UK GDPR Article 4(2). It is a publication activity governed by intellectual property law (CDPA 1988), not data-protection law.

If you use the tool to process personal data of your clients, **you** are the controller for that processing. Your UK GDPR obligations apply:
- Lawful basis (Article 6 / Article 9 for special categories)
- Transparency (Articles 12-14)
- Data minimisation (Article 5(1)(c))
- Security (Article 32)
- DSAR handling (Article 15)
- Breach notification to ICO within 72 hours (Article 33)
- ICO registration (DPA 2018 §137)

## International transfers (Schedule 21 DPA 2018 / UK GDPR Chapter V)

If you opt into cloud mode and the cloud vendor processes data outside the UK, the international transfer is YOUR action. Your obligations under Chapter V of UK GDPR (adequacy decisions · UK IDTA · UK Addendum to EU SCCs · binding corporate rules · derogations) apply. The publisher provides the tool; you decide whether and how to engage cloud processors.

## Verification path

You can independently verify zero-collection:

1. `grep -ri "telemetry\|analytics\|posthog\|mixpanel\|segment\|amplitude\|google-analytics\|datadog\|sentry" ailawfirm_uk/` — should return zero results.
2. `cat requirements.txt` — no analytics or telemetry libraries.
3. Run the tool offline — should work fully (cloud-AI calls will fail, which is expected and visible).
4. Inspect network traffic with `nettop` (macOS) / `nethogs` (Linux) — should show traffic only to user-initiated cloud-AI endpoints if cloud mode is on.

## If this changes

If a future version adds telemetry, opt-in update checks, or any cloud touchpoint involving the publisher's infrastructure, that change will be:
- Announced in CHANGELOG
- Default OFF · user-opt-in only
- Documented in this file with the change date and specific data category

This file always represents the current state. If it differs from the code, the code is the truth — file an issue.

---

*This document references LEGAL_EXPOSURE_PLAYBOOK §2(b) (Zero Data Collection pillar), §3.V4 (Data Protection — UK GDPR specific), §3.V9 (Conduct-Rule Inducement — SRA §6.3 / BSB rC15). Playbook version: v0.1.*
