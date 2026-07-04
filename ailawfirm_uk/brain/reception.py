"""One-shot boot report for the AI Law Brain Front Desk (UK edition).

Prints a greeting banner, runs a systems check across the specialists and
the router, reports the retrospective-memory count, and prints the
last-session recap. Does not enter an interactive loop.
"""

import importlib

from ailawfirm_uk.brain import memory


# Specialist modules present in ailawfirm_uk/agents/. Kept in sync with
# the actual files in that directory — every name here MUST resolve to an
# importable module exposing a callable handle().
AGENTS = (
    "matter_agent",
    "citation_agent",
    "court_agent",
    "drafting_agent",
    "deadline_agent",
    "compliance_agent",
    "calendar_agent",
)


def run_reception() -> int:
    """Boot the front desk: print banner, run systems check, recap.

    Returns 0 if every specialist and the router are online, otherwise
    returns 1. Always prints the full report before returning.
    """
    # 1. Greeting banner
    print("======================================================")
    print("  AI LAW BRAIN  ·  Front Desk")
    print("  Good day, Solicitor. Booting your brain...")
    print("======================================================")
    print()
    print("  SYSTEMS CHECK")
    print("  -------------")

    # 2. Per-agent import + handle() presence check
    online = 0
    for name in AGENTS:
        try:
            mod = importlib.import_module(f"ailawfirm_uk.agents.{name}")
            if not callable(getattr(mod, "handle", None)):
                raise RuntimeError("handle() is not callable")
            online += 1
            print(f"  ✅ {name}")
        except Exception as exc:
            print(f"  ❌ {name} (offline: {exc})")

    # 3. Router check
    router_ok = False
    try:
        router = importlib.import_module("ailawfirm_uk.brain.router")
        if not callable(getattr(router, "think", None)):
            raise RuntimeError("think() is not callable")
        router_ok = True
        print("  ✅ router")
    except Exception as exc:
        print(f"  ❌ router (offline: {exc})")

    # 4. Summary line
    router_state = "ON" if router_ok else "OFF"
    print(
        f"  brain: ON  ·  specialists: {online}/{len(AGENTS)} online  ·  "
        f"router: {router_state}"
    )
    print()

    # 5. Retrospective memory count
    n = memory.count()
    suffix = "s" if n != 1 else ""
    print(
        f"  retrospective memory: ON  ·  {n} past interaction{suffix} on file"
    )
    print()

    # 6. Recap — covers both "prints internally" and "returns a string".
    recap = memory.recap(3)
    if recap:
        print(recap)

    # 7. Closing line
    print()
    print("  How may I help you today, Solicitor?")
    print()

    # 8. Return code
    return 0 if (online == len(AGENTS) and router_ok) else 1
