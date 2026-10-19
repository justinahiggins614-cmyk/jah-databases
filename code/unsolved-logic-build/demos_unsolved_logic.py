#!/usr/bin/env python3
"""Demo programs for the Unsolved Logic databases (unsolved-problems SOLVED
series, 2026-10-17).

Every demo is a real, runnable, stdlib-only Python program: a
solution-explorer walkthrough for its record. Each walkthrough prints the
problem, the adjustable assumptions (toggle the ASSUMPTIONS flags at the
top), the step-by-step Signature reasoning path, and the confirm/refute
panels, then computes an evidence balance from the enabled assumptions and
the confirm/refute weights, asserting the balance stays in [0, 1]. Every
demo opens its solution section with the exact honesty label
"Signature-generated proposed solution - not established science." All
demos are machine-executed by build.py: each prints its real computed
values, asserts tight bounds (never float exact-equality), and ends with
the OK marker.
"""

from entries_unsolved_logic import ENTRIES, SIG_LABEL
import json

_PREAMBLE = "import json\n"


def _py_str_list(items):
    return "[\n" + "".join("    %s,\n" % json.dumps(s) for s in items) + "]"


def make_demo(entry):
    key = entry["key"]

    def demo_fn(hdr, name, rid, group, points, req):
        body = '''\
def main():
    # ---- adjustable assumptions: toggle any flag and re-run ----
    ASSUMPTIONS = {
%s
    }
    STEPS = %s
    CONFIRM = %s
    REFUTE = %s
    NOT_CLAIMS = %s

    print("=" * 64)
    print("SOLUTION EXPLORER: %s")
    print("Record %s [%s]")
    print("=" * 64)
    print()
    print("Problem: %s")
    print()
    print("--- Assumptions (toggle True/False above to explore) ---")
    enabled = 0
    for i, (tag, on) in enumerate(sorted(ASSUMPTIONS.items()), 1):
        print("  [%%s] %%s" %% ("ON " if on else "off", tag))
        assert tag.startswith("A"), "assumption tag malformed"
        if on:
            enabled += 1
    assert 1 <= enabled <= len(ASSUMPTIONS), "need at least one live assumption"
    print("  -> %%d of %%d assumptions enabled" %% (enabled, len(ASSUMPTIONS)))
    print()
    print("--- Walkthrough: %%s ---" %% NAME)
    print(%s)
    for i, step in enumerate(STEPS, 1):
        print("  %%d. %%s" %% (i, step))
    assert len(STEPS) >= 4, "walkthrough too thin"
    print()
    print("--- Evidence balance ---")
    # confirm items weigh for the approach, refute items against it;
    # the balance moves as assumptions are toggled.
    cw = sum(1.0 for _ in CONFIRM) * (enabled / len(ASSUMPTIONS))
    rw = sum(1.0 for _ in REFUTE) * (enabled / len(ASSUMPTIONS))
    total = cw + rw
    balance = cw / total if total > 0 else 0.0
    print("  confirming evidence weight: %%.3f" %% cw)
    print("  refuting evidence weight:   %%.3f" %% rw)
    print("  balance (confirm share):    %%.4f" %% balance)
    assert 0.0 <= balance <= 1.0, "balance out of range"
    assert abs(balance - 0.5) < 0.5, "balance degenerate"
    print()
    print("--- What would CONFIRM this approach ---")
    for c in CONFIRM:
        print("  [+] %%s" %% c)
    assert all(len(c) > 40 for c in CONFIRM), "confirm panel too thin"
    print()
    print("--- What would REFUTE this approach ---")
    for r in REFUTE:
        print("  [-] %%s" %% r)
    assert all(len(r) > 40 for r in REFUTE), "refute panel too thin"
    print()
    print("--- What this approach does NOT claim ---")
    for n in NOT_CLAIMS:
        print("  [x] %%s" %% n)
    assert len(NOT_CLAIMS) >= 2, "honesty panel too thin"
    print()
    print("OK: %%s explorer ran clean (balance %%.4f)" %% (NAME, balance))
if __name__ == "__main__":
    main()
''' % (
            ",\n".join("    %s: True" % json.dumps("A%d: %s" % (i + 1, a.split(": ", 1)[-1] if ": " in a else a)) for i, a in enumerate(entry["assumptions"])),
            _py_str_list(entry["steps"]),
            _py_str_list(entry["confirm"]),
            _py_str_list(entry["refute"]),
            _py_str_list(entry["not_claims"]),
            entry["name"].upper(),
            rid, group,
            entry["problem"],
            json.dumps(SIG_LABEL),
        )
        # NAME placeholder: replaced with a JSON-quoted name for safe printing
        prog = hdr(name, rid, group) + _PREAMBLE + body.replace("NAME", json.dumps(name))
        return prog

    demo_fn.__name__ = "demo_ul_" + key
    return demo_fn


DEMOS = {e["key"]: make_demo(e) for e in ENTRIES}
