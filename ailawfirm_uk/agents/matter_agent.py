"""UK matter tracker (England & Wales). Pure stdlib JSON store."""

import json
import os
import re
from datetime import datetime, timezone
from pathlib import Path

_STORE_PATH = Path(os.path.expanduser("~/.ailawfirm_uk/matters.json"))

_AGENT = "matter_agent"


def _load() -> dict:
    try:
        if _STORE_PATH.is_file():
            with open(_STORE_PATH, "r", encoding="utf-8") as f:
                data = json.load(f)
                if isinstance(data, dict):
                    return data
    except (OSError, ValueError, json.JSONDecodeError):
        pass
    return {}


def _save(data: dict) -> None:
    try:
        _STORE_PATH.parent.mkdir(parents=True, exist_ok=True)
        with open(_STORE_PATH, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
    except OSError:
        pass


def _now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def _add_matter(text: str, lower: str, data: dict) -> dict:
    if lower.startswith("add matter "):
        name = text[len("add matter "):].strip() or "Untitled matter"
    elif lower.startswith("add matter"):
        name = text[len("add matter"):].strip() or "Untitled matter"
    elif lower.startswith("new matter "):
        name = text[len("new matter "):].strip() or "Untitled matter"
    elif lower.startswith("new matter"):
        name = text[len("new matter"):].strip() or "Untitled matter"
    else:
        name = "Untitled matter"
    now = _now_iso()
    prior = data.get(name)
    if not isinstance(prior, dict):
        prior = {}
    data[name] = {
        "name": name,
        "note": prior.get("note", ""),
        "updated": now,
    }
    _save(data)
    return {
        "agent": _AGENT,
        "status": "ok",
        "action": "added",
        "matter": name,
        "updated": now,
    }


def handle(payload: str) -> dict:
    text = (payload or "").strip()
    try:
        lower = text.lower()
        data = _load()

        # add matter <name>  /  new matter [name]
        if lower.startswith("add matter") or lower.startswith("new matter"):
            return _add_matter(text, lower, data)

        # list matters / show matters / my matters
        if re.match(r"(list|show|my)\s+matters?$", lower):
            names = list(data.keys())
            return {
                "agent": _AGENT,
                "status": "ok",
                "action": "list",
                "matters": names,
                "count": len(names),
            }

        # status of <x>
        name = None
        if lower.startswith("status of "):
            name = text[len("status of "):].strip()
        elif lower.startswith("about "):
            name = text[len("about "):].strip()
        elif lower.startswith("matter "):
            name = text[len("matter "):].strip()

        if name:
            entry = data.get(name)
            return {
                "agent": _AGENT,
                "status": "ok",
                "action": "lookup",
                "matter": name,
                "found": entry is not None,
                "details": entry,
            }

        return {
            "agent": _AGENT,
            "status": "ok",
            "action": "noop",
            "note": (
                "Unrecognised matter command. Use 'add matter <name>', "
                "'list matters', or 'status of <name>'."
            ),
        }
    except Exception:
        return {
            "agent": _AGENT,
            "status": "ok",
            "action": "noop",
            "note": "Matter command could not be processed.",
        }
