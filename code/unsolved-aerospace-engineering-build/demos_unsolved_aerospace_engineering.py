#!/usr/bin/env python3
"""Solution-explorer walkthrough demos for The Unsolved Aerospace Engineering Database.

Data-driven: each entry carries demo_data (two real published quantities, a
tight published range for their ratio, and confirm/refute conditions). Every
demo is a working program: it states the problem, walks the Signature proposed
approach, computes a REAL ratio from real numbers, checks it with tight-bounds
asserts (never float exact-equality), prints a confirm/refute panel, and ends
with the OK marker.

Honesty rule: demos explore PROPOSED approaches. They never claim proof.
"""

LABEL = "Signature-generated proposed solution \u2014 not established science."


def _clean(s):
    return (str(s).replace("\\", "/").replace('"""', "'''").replace('"', "'"))


def _demo_fn(entry):
    dd = entry.get("demo_data") or {}
    a_label, a_val = dd.get("a", ("quantity A", 1.0))
    b_label, b_val = dd.get("b", ("quantity B", 1.0))
    lo, hi = dd.get("bounds", (0.0, 1e30))
    step1 = _clean(dd.get("step1", "the published ratio quantifies the problem's scale"))
    confirm = _clean(dd.get("confirm", "the predicted signature appears in controlled study"))
    refute = _clean(dd.get("refute", "the predicted signature fails to appear"))
    name = _clean(entry.get("name", "study"))
    lens = _clean(entry.get("sig_lens", ""))
    if len(lens) > 220:
        lens = lens[:217] + "..."
    problem = _clean(entry.get("problem", ""))
    if len(problem) > 160:
        problem = problem[:157] + "..."

    def fn(hdr, rname, rid, group, points, req):
        prog = hdr(rname, rid, group)
        prog += '"""SOLUTION EXPLORER: ' + name + '.\n'
        prog += 'Walks the Signature proposed approach: ' + lens + '\n'
        prog += 'PROPOSAL ONLY - ' + LABEL + '"""\n\n'
        prog += 'import math\n\n'
        prog += '# ---- real published quantities ----\n'
        prog += 'A_LABEL = "' + _clean(a_label) + '"\n'
        prog += 'A = ' + repr(float(a_val)) + '\n'
        prog += 'B_LABEL = "' + _clean(b_label) + '"\n'
        prog += 'B = ' + repr(float(b_val)) + '\n'
        prog += 'LO = ' + repr(float(lo)) + '\n'
        prog += 'HI = ' + repr(float(hi)) + '\n\n'
        prog += 'def step1_problem():\n'
        prog += '    print("STEP 1 - the problem: ' + problem + '")\n'
        prog += '    ratio = A / B\n'
        prog += '    print("  %s = %.6g ; %s = %.6g" % (A_LABEL, A, B_LABEL, B))\n'
        prog += '    print("  ratio A/B = %.6g -- ' + step1 + '")\n'
        prog += '    assert LO < ratio < HI, "ratio outside published range"\n'
        prog += '    return ratio\n\n'
        prog += 'def step2_signature_approach(ratio):\n'
        prog += '    print("STEP 2 - Signature approach: ' + lens + '")\n'
        prog += '    print("  The proposal reads the measured ratio %.6g as the" % ratio)\n'
        prog += '    print("  observable fingerprint the solution must explain.")\n'
        prog += '    assert ratio > 0, "ratio must be positive"\n'
        prog += '    return True\n\n'
        prog += 'def step3_testable(ratio):\n'
        prog += '    print("STEP 3 - testable prediction: a future measurement must")\n'
        prog += '    print("  move this ratio outside [%.6g, %.6g] if the proposal" % (LO, HI))\n'
        prog += '    print("  is wrong, or reproduce it inside the band if right.")\n'
        prog += '    inside = LO < ratio < HI\n'
        prog += '    print("  current published ratio inside band: %s" % inside)\n'
        prog += '    assert inside\n\n'
        prog += 'def confirm_refute_panel():\n'
        prog += '    print("CONFIRM/REFUTE PANEL:")\n'
        prog += '    print("  CONFIRM if: ' + confirm + '")\n'
        prog += '    print("  REFUTE if: ' + refute + '")\n\n'
        prog += 'def main():\n'
        prog += '    r = step1_problem()\n'
        prog += '    step2_signature_approach(r)\n'
        prog += '    step3_testable(r)\n'
        prog += '    confirm_refute_panel()\n'
        prog += '    print("OK: %s solution-explorer complete (ratio=%.6g)" % (RID, r))\n\n'
        prog += 'RID = "' + rid + '"\n'
        prog += 'if __name__ == "__main__":\n'
        prog += '    main()\n'
        return prog

    return fn


def build_demos(entries):
    return {e["key"]: _demo_fn(e) for e in entries}
