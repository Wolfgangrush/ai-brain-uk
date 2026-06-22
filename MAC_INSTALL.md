# MAC_INSTALL.md — macOS Installation Guide

## Prerequisites

- macOS 12 (Monterey) or later
- Xcode Command Line Tools: `xcode-select --install`
- Homebrew (optional but recommended): [brew.sh](https://brew.sh)

## Step-by-Step

### 1. Install Python 3.9+

```bash
brew install python@3.12
```

Or download from [python.org](https://www.python.org/downloads/).

Verify:
```bash
python3 --version  # expect 3.9 or higher
```

### 2. Clone the Repo

```bash
git clone https://github.com/Wolfgangrush/ai-law-firm-uk.git
cd ai-law-firm-uk
```

### 3. Create Virtual Environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 4. Install

```bash
pip install -e .
```

### 5. Initialize

```bash
ailawfirm-uk init
```

This creates `~/.ailawfirm-uk/` with default config.

### 6. Verify

```bash
ailawfirm-uk status
```

## Calendar.app Integration

The calendar sync tool generates `.ics` files at `~/.ailawfirm-uk/calendar.ics`. To import into macOS Calendar:

1. Open **Calendar.app**
2. **File → Import...**
3. Select `~/.ailawfirm-uk/calendar.ics`
4. Choose the calendar to add events to

The `.ics` file auto-refreshes on each sync. Re-import to update.

## MCP Setup with Claude Code

Add to `~/.claude/claude_desktop_config.json` or your project's `.mcp.json`:

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

## Troubleshooting

### "externally managed environment" error

```bash
python3 -m pip install --break-system-packages -e .
```

### "No module named ailawfirm_uk"

Ensure you're in the virtual environment and have run `pip install -e .`.

### ChromaDB issues on Apple Silicon

ChromaDB works natively on Apple Silicon. If you encounter issues:
```bash
pip install --upgrade chromadb
```
