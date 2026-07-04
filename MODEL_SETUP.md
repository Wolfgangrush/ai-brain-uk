# MODEL_SETUP.md — LLM Provider Configuration

AI Brain UK runs locally by default. For advanced intent classification and drafting assistance (v0.2+), you can connect an external LLM provider.

## Local Mode (default, v0.1)

No API key required. The brain classifier uses keyword matching. MCP tools run entirely on-device.

## External LLM Providers

### Anthropic (Claude) — Recommended

```bash
export ANTHROPIC_API_KEY="sk-ant-..."
```

Configure in `~/.ailawfirm-uk/config.json`:
```json
{
  "llm_provider": "anthropic",
  "llm_model": "claude-sonnet-4-6"
}
```

### OpenAI (GPT)

```bash
export OPENAI_API_KEY="sk-..."
```

```json
{
  "llm_provider": "openai",
  "llm_model": "gpt-4o"
}
```

### Google (Gemini)

```bash
export GOOGLE_API_KEY="..."
```

```json
{
  "llm_provider": "google",
  "llm_model": "gemini-2.5-pro"
}
```

### Local (Ollama)

No API key. Install [Ollama](https://ollama.com) and pull a model:
```bash
ollama pull llama3.2
```

```json
{
  "llm_provider": "ollama",
  "llm_model": "llama3.2"
}
```

## Privacy Boundary

**When you configure an external LLM provider, prompts containing matter summaries, citations, and compliance queries go to that provider's servers.**

Mitigations:
1. **entity aliasing** — The system uses aliased entity names in all external prompts. Client names, case references, and party names are substituted before leaving your machine.
2. **Local-first by default** — No provider is configured unless you explicitly set one.
3. **Provider data policies vary** — Anthropic, OpenAI, and Google have different data retention policies. Check your provider's terms.

## UK-Specific Considerations

- **SRA confidentiality obligations** (SRA Code §6.3): You remain responsible for client confidentiality regardless of tooling.
- **BSB Core Duty 6** (confidentiality): Same obligation applies to barristers.
- **ICO guidance on AI and data protection**: If processing personal data through an LLM provider, this constitutes processing under UK GDPR. Ensure your provider's DPA covers this.
- **Legal professional privilege**: Be cautious about sending privileged material to LLM providers. Use entity aliasing for privileged content.

## Recommended Setup for UK Solo Practitioners

1. Use **local mode** for day-to-day court lookups, citation validation, and calendar sync (no data leaves your machine)
2. Configure an **external LLM** only for drafting assistance (v0.2+)
3. Always use **entity aliasing** when external LLM is configured
4. Review your **professional indemnity insurance** — some policies now address AI tooling
---

## ⚠️ Third-party CLI tools and IDEs — user assumes all risk

If you integrate this Software with **any third-party AI service, CLI tool, or AI-assisted IDE** — including but not limited to: **Anthropic Claude API · Claude CLI · Claude Code · OpenAI API · Codex CLI · Google Gemini API · Gemini CLI · DeepSeek API · OpenCode · Cursor · GitHub Copilot · JetBrains AI · Mistral · Cohere · HuggingFace inference · Groq · Together AI · Qwen API · or any other model provider, CLI, IDE, or AI-assisted tool** — you do so **at your own risk** and under the terms of service of that third-party tool.

The publisher (wolfgang_rush · Rushikesh R. Mahajan):

- Does **NOT** recommend any specific third-party tool
- Does **NOT** receive any compensation, referral fee, or benefit from any third-party tool's adoption
- Does **NOT** verify any third-party tool's privacy posture, security, or compliance with your jurisdiction's law
- Accepts **NO** responsibility for your choice of third-party tooling
- Accepts **NO** responsibility for any data leakage, confidentiality breach, professional-conduct violation, regulatory non-compliance, or any other harm resulting from your use of third-party tools alongside this Software
- Makes **NO** warranty that any third-party tool is suitable for legal-professional use in any jurisdiction

**You are solely responsible** for:

- Reading the privacy policy and terms of service of each third-party tool before connecting it
- Ensuring compliance with all confidentiality rules, data-protection laws, sectoral regulations, and bar conduct rules that apply to your practice
- Obtaining client consent where required before routing client data through any third-party tool
- Verifying that the third-party tool does not retain, train on, or share your queries in ways that breach your professional obligations
- Managing API keys, access tokens, and credentials securely (do not commit them to version control; use environment variables or a password manager)
- Independently verifying any output produced by a third-party tool before client-facing use

**This warning applies regardless of which third-party tool you choose, and regardless of any privacy claim that tool makes.** The responsibility to verify and the liability for use rest entirely with you.

---

