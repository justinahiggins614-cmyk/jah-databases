#!/usr/bin/env python3
"""Solution-explorer walkthrough demos for The Unsolved Climate Science
Database (34 records) and its Signature edition.

Every demo is a working program that walks the user through the Signature
solution approach: interactive steps, adjustable assumptions, real computed
values, tight-bounds asserts (never float exact-equality), and a clear
confirm/refute panel. All demos are real, runnable, stdlib-only Python.

Calc archetypes (chosen per entry in entries_unsolved_climate_science.py):
  gain     - warming = planck_C / (1 - (f_base + a0))   (feedback-gain explorer)
  sum      - value = a0 + a1 + ...                       (ledger sums)
  sum1     - value = 1 + a0 + a1 + ...                   (amplification factors)
  min      - value = min(a0, a1, ...)                    (weakest-link ledgers)
  heat     - ZJ = a0(W/m2) * a1(years) * 16.0965         (Earth heat inventory)
  carbon   - ppm = a0(GtCO2) * a1(airborne) / 7.81       (carbon-cycle ledger)
  sealevel - cm = (a0(mm/yr)*a1(years) + 0.5*a2*a1^2)/10 (sea-level ledger)
  expr     - value = <python expression in a0..aN>       (entry-specific model)

Never the words "bat belt" anywhere. No website references. No Facebook.
"""

SIG_LABEL = "Signature-generated proposed solution - not established science."


def _py_str(s):
    """Render a Python string literal safely."""
    return repr(s)


def demo_explorer(hdr_fn, name, rid, group, points, req, spec):
    """Build a solution-explorer walkthrough program for one entry."""
    calc = spec["calc"]
    qty = spec["quantity"]
    unit = spec["unit"]
    assumptions = spec["assumptions"]
    formula = spec["formula"]
    checks = spec["checks"]
    steps = spec["steps"]
    confirm = spec["confirm"]
    refute = spec["refute"]
    note = spec["note"]

    n = len(assumptions)
    arg_names = ", ".join("a%d" % i for i in range(n))

    if calc == "gain":
        planck = spec["planck"]
        f_base = spec.get("f_base", 0.0)
        body = "    return %r / (1.0 - (%r + a0))" % (planck, f_base)
    elif calc == "sum":
        body = "    return " + " + ".join("a%d" % i for i in range(n))
    elif calc == "sum1":
        body = "    return 1.0 + " + " + ".join("a%d" % i for i in range(n))
    elif calc == "min":
        body = "    return min(" + ", ".join("a%d" % i for i in range(n)) + ")"
    elif calc == "heat":
        body = "    return a0 * a1 * 16.0965"
    elif calc == "carbon":
        body = "    return a0 * a1 / 7.81"
    elif calc == "sealevel":
        body = "    return (a0 * a1 + 0.5 * a2 * a1 * a1) / 10.0"
    elif calc == "expr":
        body = "    return " + spec["expr"]
    else:
        raise ValueError("unknown calc %r" % calc)

    defaults = [a[1] for a in assumptions]

    lines = []
    lines.append(hdr_fn(name, rid, group))
    lines.append('"""Solution-explorer walkthrough.')
    lines.append('')
    lines.append('Walks through the Signature proposed solution approach for')
    lines.append('this unsolved problem: interactive steps, adjustable')
    lines.append('assumptions with real computed values, and a confirm/refute')
    lines.append('panel stating what evidence would support or kill the approach.')
    lines.append('')
    lines.append(SIG_LABEL)
    lines.append('"""')
    lines.append("import math")
    lines.append("")
    lines.append("LABEL = " + _py_str(SIG_LABEL))
    lines.append("QUANTITY = " + _py_str(qty))
    lines.append("UNIT = " + _py_str(unit))
    lines.append("FORMULA = " + _py_str(formula))
    lines.append("")
    lines.append("STEPS = [")
    for s in steps:
        lines.append("    " + _py_str(s) + ",")
    lines.append("]")
    lines.append("ASSUMPTIONS = [")
    for label, default, values in assumptions:
        lines.append("    (%s, %r, %r)," % (_py_str(label), default, list(values)))
    lines.append("]")
    lines.append("CONFIRM = [")
    for c in confirm:
        lines.append("    " + _py_str(c) + ",")
    lines.append("]")
    lines.append("REFUTE = [")
    for r in refute:
        lines.append("    " + _py_str(r) + ",")
    lines.append("]")
    lines.append("")
    lines.append("def model(%s):" % arg_names)
    lines.append(body)
    lines.append("")
    lines.append("def main():")
    lines.append("    print('=' * 64)")
    lines.append("    print(" + _py_str(name) + ")")
    lines.append("    print('Record ' + " + _py_str(rid) + " + ' [' + " + _py_str(group) + " + ']')")
    lines.append("    print(LABEL)")
    lines.append("    print('=' * 64)")
    lines.append("    print()")
    lines.append("    print('Walkthrough steps:')")
    lines.append("    for i, s in enumerate(STEPS, 1):")
    lines.append("        print('  %d. %s' % (i, s))")
    lines.append("    print()")
    lines.append("    print('Adjustable assumptions:')")
    lines.append("    for label, default, values in ASSUMPTIONS:")
    lines.append("        print('  %-42s default=%s explored=%s' % (label, default, values))")
    lines.append("    print()")
    lines.append("    print('Model: %s = %s [%s]' % (QUANTITY, FORMULA, UNIT))")
    lines.append("    base = model(%s)" % ", ".join(repr(d) for d in defaults))
    lines.append("    print('  baseline (defaults): %.4g %s' % (base, UNIT))")
    lines.append("    print()")
    lines.append("    print('Verification checks (tight bounds, real computed values):')")
    for vals, expected, tol in checks:
        vlist = ", ".join(repr(v) for v in vals)
        lines.append("    v = model(%s)" % vlist)
        lines.append("    print('  model(%s) = %%.4g (expected %%.4g)' %% (v, %r))" % (vlist, expected))
        lines.append("    assert abs(v - %r) <= %r, 'check failed: %%r vs %%r' %% (v, %r)" % (expected, tol, expected))
    lines.append("    print('  all %d checks passed within tolerance')" % len(checks))
    lines.append("    print()")
    lines.append("    print('What would CONFIRM this approach:')")
    lines.append("    for c in CONFIRM:")
    lines.append("        print('  + ' + c)")
    lines.append("    print('What would REFUTE this approach:')")
    lines.append("    for r in REFUTE:")
    lines.append("        print('  - ' + r)")
    lines.append("    print()")
    lines.append("    print('OK: solution-explorer walkthrough completed for ' + " + _py_str(name) + ")")
    lines.append("")
    lines.append("if __name__ == '__main__':")
    lines.append("    main()")
    lines.append("")
    return "\n".join(lines) + "\n"


DEMOS = {"explorer": demo_explorer}
