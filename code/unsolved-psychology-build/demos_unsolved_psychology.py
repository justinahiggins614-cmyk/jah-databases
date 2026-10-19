#!/usr/bin/env python3
"""Solution-explorer walkthrough demos for the Unsolved Psychology
databases (Manon 2026-10-17 16:15 Unsolved Problems Solved series,
batch 1 — Psychology).

Each record ships a solution-explorer walkthrough: a real, runnable,
stdlib-only Python program that walks the user through the Signature
proposed solution approach in five steps, with adjustable assumption
weights (override on the command line, e.g. --a1=0.5 --c2=0.4), a
CONFIRM panel, a REFUTE panel, and a computed verdict.

Scoring model (deterministic, hand-set weights per entry):
  C  = sum of confirm-line weights
  R  = sum of refute-line weights
  net = (C - R) / (C + R)            -> in (-1, 1), the evidence balance
  A  = mean of assumption weights    -> adjustable confidence, default 1.0
  explored = net * A                  -> the reported explorer score

The demo prints its real computed values, asserts tight bounds (never
float exact-equality), keeps the honesty rule in its verdict text
(proposed, unconfirmed — never established science), and ends with the
OK marker. The build machine-executes all 68 demos before any files
are written.
"""
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from entries_unsolved_psychology import ENTRIES


def _prog(entry, title, rid, group):
    problem = repr(entry["problem"])
    assumptions = repr(entry["assumptions"])
    confirm = repr(entry["confirm"])
    refute = repr(entry["refute"])
    exp = repr(round((sum(w for _, _, w in entry["confirm"]) -
                      sum(w for _, _, w in entry["refute"])) /
                     (sum(w for _, _, w in entry["confirm"]) +
                      sum(w for _, _, w in entry["refute"])), 6))
    key = repr(entry["key"])
    head = ('#!/usr/bin/env python3\n"""' + title.replace('"', "'") +
            ' — solution-explorer walkthrough.\nRecord ' + rid + ' [' +
            group + ']. Property of Justin Addam Higgins (JAH).\n'
            'Adjustable: --a1=.. --a2=.. --a3=.. --c1=.. --c2=.. --c3=..'
            ' --r1=.. --r2=.. --r3=..\n"""\n')
    body = '''
import sys

PROBLEM = __PROBLEM__
ASSUMPTIONS = __ASSUMPTIONS__
CONFIRM = __CONFIRM__
REFUTE = __REFUTE__
EXPECTED_NET = __EXPECTED_NET__
KEY = __KEY__

def overrides(argv):
    ov = {}
    for a in argv[1:]:
        if a.startswith("--") and "=" in a[2:]:
            k, v = a[2:].split("=", 1)
            if k in ("a1", "a2", "a3", "c1", "c2", "c3", "r1", "r2", "r3"):
                try:
                    ov[k] = float(v)
                except ValueError:
                    pass
    return ov

def main():
    ov = overrides(sys.argv)
    a = [ov.get("a%d" % (i + 1), 1.0) for i in range(3)]
    cw = [ov.get("c%d" % (i + 1), w) for i, (_, _, w) in enumerate(CONFIRM)]
    rw = [ov.get("r%d" % (i + 1), w) for i, (_, _, w) in enumerate(REFUTE)]
    assert len(ASSUMPTIONS) == 3 and len(CONFIRM) == 3 and len(REFUTE) == 3
    assert all(0.0 < w <= 1.0 for w in cw), "confirm weight out of (0,1]"
    assert all(0.0 < w <= 1.0 for w in rw), "refute weight out of (0,1]"
    assert all(0.0 < w <= 2.0 for w in a), "assumption weight out of (0,2]"
    C = sum(cw)
    R = sum(rw)
    net = (C - R) / (C + R)
    assert -1.0 < net < 1.0, "net out of (-1,1)"
    touched = any(k in ov for k in ("c1", "c2", "c3", "r1", "r2", "r3"))
    if not touched:
        assert abs(net - EXPECTED_NET) < 0.02, "net drifted from authored expectation"
    conf = sum(a) / 3.0
    explored = net * conf
    assert -2.0 < explored < 2.0, "explorer score out of (-2,2)"
    print("=== Solution Explorer ===")
    print("Record: " + KEY)
    print("Step 1/5 — The open problem:")
    print("  " + PROBLEM)
    print("Step 2/5 — Adjustable assumptions (confidence weights):")
    for i, s in enumerate(ASSUMPTIONS):
        print("  [A%d weight=%.2f] %s" % (i + 1, a[i], s))
    print("  Assumption confidence: %.3f" % conf)
    print("Step 3/5 — CONFIRM panel (what would support the proposal):")
    for i, (label, text, _w) in enumerate(CONFIRM):
        print("  [C%d weight=%.2f] %s: %s" % (i + 1, cw[i], label, text))
    print("Step 4/5 — REFUTE panel (what would kill the proposal):")
    for i, (label, text, _w) in enumerate(REFUTE):
        print("  [R%d weight=%.2f] %s: %s" % (i + 1, rw[i], label, text))
    print("Step 5/5 — Explorer score:")
    print("  confirm=%.3f refute=%.3f net=%+.3f explored=%+.3f" % (
        C / (C + R), R / (C + R), net, explored))
    if explored > 0.15:
        verdict = "leans promising"
    elif explored < -0.15:
        verdict = "refute lines dominate — approach likely needs revision"
    else:
        verdict = "balanced — needs discriminating evidence"
    print("  Verdict: " + verdict)
    print("  Honesty: Signature-generated proposed solution — not established")
    print("  science. Never proof, never peer acceptance, never settled.")
    print("OK: " + KEY)

if __name__ == "__main__":
    main()
'''
    for tok, val in (("__PROBLEM__", problem), ("__ASSUMPTIONS__", assumptions),
                     ("__CONFIRM__", confirm), ("__REFUTE__", refute),
                     ("__EXPECTED_NET__", exp), ("__KEY__", key)):
        body = body.replace(tok, val)
    return head + body


def make_demo(entry):
    def demo(hdr, title, rid, group):
        return hdr(title, rid, group) + _prog(entry, title, rid, group)
    return demo


DEMOS = {e["key"]: make_demo(e) for e in ENTRIES}
assert len(DEMOS) == 34 and len(ENTRIES) == 34
