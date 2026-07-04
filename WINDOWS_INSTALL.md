# WINDOWS_INSTALL.md — Windows Installation Guide

## Prerequisites

- Windows 10 (build 19041+) or Windows 11
- [Git for Windows](https://git-scm.com/download/win)
- [Python 3.9+](https://www.python.org/downloads/windows/)

**Important:** During Python installation, check "Add Python to PATH."

## Step-by-Step

### 1. Verify Python

Open PowerShell or Command Prompt:
```powershell
python --version  # expect 3.9 or higher
git --version
```

### 2. Clone the Repo

```powershell
git clone https://github.com/Wolfgangrush/ai-law-firm-uk.git
cd ai-law-firm-uk
```

### 3. Create Virtual Environment

```powershell
python -m venv .venv
.venv\Scripts\activate
```

### 4. Install

```powershell
pip install -e .
```

### 5. Initialize

```powershell
ailawfirm-uk init
```

This creates `%USERPROFILE%\.ailawfirm-uk\` with default config.

### 6. Verify

```powershell
ailawfirm-uk status
```

## Outlook Calendar Integration

The calendar sync tool generates `.ics` files. To import into Outlook:

1. Open **Outlook**
2. **File → Open & Export → Import/Export**
3. Select **Import an iCalendar (.ics) file**
4. Browse to `%USERPROFILE%\.ailawfirm-uk\calendar.ics`
5. Choose **Open as New** or **Import**

## MCP Setup with Claude Code

Add to your MCP configuration:
```json
{
  "mcpServers": {
    "ailawfirm-uk": {
      "command": "python",
      "args": ["-m", "ailawfirm_uk.mcp_server"]
    }
  }
}
```

## Troubleshooting

### "Python was not found"

Ensure Python is in your PATH. Re-run the Python installer and check "Add Python to PATH," or add it manually in System Environment Variables.

### "Microsoft Visual C++ 14.0 is required"

Some dependencies may require the Visual C++ build tools:
1. Download [Visual Studio Build Tools](https://visualstudio.microsoft.com/downloads/#build-tools-for-visual-studio-2022)
2. Install with "Desktop development with C++" workload

### ChromaDB issues

ChromaDB works on Windows. If you encounter errors:
```powershell
pip install --upgrade chromadb
```

### Running in WSL2

AI Brain UK works in WSL2 (Windows Subsystem for Linux). Follow the Linux install instructions inside your WSL distribution.
