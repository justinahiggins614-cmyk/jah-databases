#!/usr/bin/env python3
"""Solution-explorer walkthrough demo builders for the Unsolved Earth Science
databases (Unsolved Problems Solved series, batch 1).

Each record ships a solution-explorer demo: a working program that walks the
user through the Signature solution approach - interactive steps, adjustable
assumptions, and a clear what-would-confirm/refute panel. Demos compute real
values at runtime from the adjustable assumptions, assert tight bounds (never
float exact-equality), and end with the OK marker.
"""

import json

LABEL = "Signature-generated proposed solution \u2014 not established science."


def _fmt_src(x):
    return json.dumps(x)


def explorer_demo(entry, title, rid, group):
    """Build the full demo program source for one entry."""
    ex = entry["explorer"]
    L = []
    L.append("#!/usr/bin/env python3")
    L.append('"""%s - solution-explorer walkthrough.' % title.replace('"', "'"))
    L.append("Record %s [%s]. Property of Justin Addam Higgins (JAH)." % (rid, group))
    L.append('The Signature approach shown here is a labeled proposal, not established science.')
    L.append('"""')
    L.append("import math")
    L.append("import json")
    L.append("")
    L.append("LABEL = %s" % _fmt_src(LABEL))
    L.append("TITLE = %s" % _fmt_src(title))
    L.append("RID = %s" % _fmt_src(rid))
    L.append("")
    L.append("# ---- adjustable assumptions (edit A and re-run) ----")
    L.append("A = %s" % repr(ex["assumptions"]))
    L.append("")
    L.append("# ---- model: the Signature approach as a computable sketch ----")
    L.append(ex["model_src"])
    L.append("")
    L.append("BLURB = %s" % _fmt_src(ex["blurb"]))
    L.append("STEPS = %s" % repr(ex["steps"]))
    L.append("CONFIRM = %s" % _fmt_src(ex["confirm"]))
    L.append("REFUTE = %s" % _fmt_src(ex["refute"]))
    L.append("CHECKS = %s" % repr(ex["checks"]))
    L.append("HONESTY = %s" % _fmt_src(ex["honesty"]))
    L.append("")
    L.append("def fmt(x):")
    L.append("    if isinstance(x, bool):")
    L.append("        return str(x)")
    L.append("    if isinstance(x, float):")
    L.append("        if x == 0.0:")
    L.append("            return '0'")
    L.append("        a = abs(x)")
    L.append("        if a >= 100000.0 or a < 0.001:")
    L.append("            return '%.4g' % x")
    L.append("        return '%.6g' % x")
    L.append("    return str(x)")
    L.append("")
    L.append("def main():")
    L.append("    print('=' * 70)")
    L.append("    print('SOLUTION EXPLORER')")
    L.append("    print(TITLE)")
    L.append("    print('=' * 70)")
    L.append("    print('')")
    L.append("    print('[1] ' + LABEL)")
    L.append("    print(BLURB)")
    L.append("    print('')")
    L.append("    print('[2] Adjustable assumptions (edit A and re-run):')")
    L.append("    for k in sorted(A.keys(), key=str):")
    L.append("        v = A[k]")
    L.append("        print('      %s = %s' % (k, fmt(v) if isinstance(v, (int, float)) else json.dumps(v)))")
    L.append("    print('')")
    L.append("    print('[3] Walkthrough - the model step by step:')")
    L.append("    R = run(A)")
    L.append("    for label, key, unit in STEPS:")
    L.append("        u = (' ' + unit) if unit else ''")
    L.append("        print('      - %s: %s%s' % (label, fmt(R[key]), u))")
    L.append("    print('')")
    L.append("    print('[4] What would CONFIRM this proposed approach:')")
    L.append("    for c in CONFIRM:")
    L.append("        print('      + ' + c)")
    L.append("    print('')")
    L.append("    print('[5] What would REFUTE this proposed approach:')")
    L.append("    for r in REFUTE:")
    L.append("        print('      - ' + r)")
    L.append("    print('')")
    L.append("    print('[6] Tight-bounds checks (never exact float equality):')")
    L.append("    for key, lo, hi in CHECKS:")
    L.append("        v = R[key]")
    L.append("        assert lo < v < hi, 'bounds violated for %s' % key")
    L.append("        print('      check %s = %s inside (%s, %s): PASS' % (key, fmt(v), fmt(lo), fmt(hi)))")
    L.append("    print('')")
    L.append("    print('[7] Honesty note: ' + HONESTY)")
    L.append("    print('')")
    L.append("    print('OK: solution-explorer walkthrough completed for %s' % RID)")
    L.append("")
    L.append("if __name__ == '__main__':")
    L.append("    main()")
    L.append("")
    return "\n".join(L)


def demos_for(entries):
    """Map entry key -> demo builder bound to that entry."""
    out = {}
    for e in entries:
        out[e["key"]] = (lambda e: (lambda title, rid, group: explorer_demo(e, title, rid, group)))(e)
    return out
