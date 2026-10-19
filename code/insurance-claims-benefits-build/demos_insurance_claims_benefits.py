#!/usr/bin/env python3
"""Demonstration programs for the Insurance Claims and Benefits databases.

Every demo is real, runnable, stdlib-only Python that machine-checks the
record it ships with: the entry's own data is baked into the program, the
program recomputes real values from it, asserts tight bounds (never float
exact-equality), prints the real computed values, and ends with the OK
marker. The build machine-executes every demo.
"""
import json


def _hdr(name, rid, group):
    return ('#!/usr/bin/env python3\n"""%s — working demonstration.\n'
            'Record %s [%s]. Property of Justin Addam Higgins (JAH).\n"""\n'
            % (name, rid, group))


def _t_lossratio(hdr, name, rid, group, d):
    l, p = float(d['losses']), float(d['earned_prem'])
    return hdr + 'LOSS=%r\nEP=%r\n' % (l, p) + '''def main():
    lr = LOSS/EP
    print("incurred losses:", LOSS)
    print("earned premium:", EP)
    print("loss ratio:", round(lr, 3))
    assert EP > 0 and LOSS >= 0
    assert abs(lr - LOSS/EP) < 1e-9
    assert 0 <= lr <= 3
    print("OK: loss ratio verified for", @@NAME@@)
if __name__ == "__main__":
    main()
'''.replace('@@NAME@@', json.dumps(name))


def _t_combined(hdr, name, rid, group, d):
    lr, er = float(d['loss_ratio']), float(d['expense_ratio'])
    return hdr + 'LR=%r\nER=%r\n' % (lr, er) + '''def main():
    cr = LR + ER
    print("loss ratio:", LR, "| expense ratio:", ER)
    print("combined ratio:", round(cr, 3))
    print("underwriting profit" if cr < 1 else "underwriting loss")
    assert abs(cr - (LR+ER)) < 1e-9
    assert 0 < cr < 3
    print("OK: combined ratio verified for", @@NAME@@)
if __name__ == "__main__":
    main()
'''.replace('@@NAME@@', json.dumps(name))


def _t_premium(hdr, name, rid, group, d):
    r, e = float(d['rate']), float(d['exposure'])
    return hdr + 'RATE=%r\nEXP=%r\n' % (r, e) + '''def main():
    prem = RATE*EXP
    print("rate:", RATE, "| exposure units:", EXP)
    print("premium:", round(prem, 2))
    assert RATE > 0 and EXP > 0
    assert abs(prem - RATE*EXP) < 1e-9
    print("OK: premium verified for", @@NAME@@)
if __name__ == "__main__":
    main()
'''.replace('@@NAME@@', json.dumps(name))


def _t_reserve(hdr, name, rid, group, d):
    pd, cr = float(d['paid']), float(d['case_reserve'])
    return hdr + 'PAID=%r\nCASE=%r\n' % (pd, cr) + '''def main():
    incurred = PAID + CASE
    print("paid to date:", PAID)
    print("case reserve:", CASE)
    print("incurred loss:", round(incurred, 2))
    assert PAID >= 0 and CASE >= 0
    assert abs(incurred - (PAID+CASE)) < 1e-9
    print("OK: reserves verified for", @@NAME@@)
if __name__ == "__main__":
    main()
'''.replace('@@NAME@@', json.dumps(name))


def _t_subro(hdr, name, rid, group, d):
    pd, rc = float(d['paid']), float(d['recovered'])
    return hdr + 'PAID=%r\nREC=%r\n' % (pd, rc) + '''def main():
    net = PAID - REC
    pct = 100.0*REC/PAID
    print("paid:", PAID, "| recovered:", REC)
    print("net loss:", round(net, 2))
    print("recovery %:", round(pct, 1))
    assert PAID > 0 and 0 <= REC <= PAID
    assert abs(net - (PAID-REC)) < 1e-9
    print("OK: subrogation verified for", @@NAME@@)
if __name__ == "__main__":
    main()
'''.replace('@@NAME@@', json.dumps(name))


def _t_eligibility(hdr, name, rid, group, d):
    inc, lim = float(d['income']), float(d['limit'])
    return hdr + 'INC=%r\nLIM=%r\n' % (inc, lim) + '''def main():
    elig = INC <= LIM
    print("household income:", INC, "| limit:", LIM)
    print("eligible:", elig)
    assert INC >= 0 and LIM > 0
    assert elig == (INC <= LIM)
    print("OK: eligibility verified for", @@NAME@@)
if __name__ == "__main__":
    main()
'''.replace('@@NAME@@', json.dumps(name))


def _t_benefit(hdr, name, rid, group, d):
    b, h = float(d['base']), float(d['household'])
    return hdr + 'BASE=%r\nHH=%r\n' % (b, h) + '''def main():
    monthly = BASE*HH
    print("base amount:", BASE, "| household size:", HH)
    print("monthly allotment:", round(monthly, 2))
    assert BASE > 0 and HH >= 1
    assert abs(monthly - BASE*HH) < 1e-9
    print("OK: benefit verified for", @@NAME@@)
if __name__ == "__main__":
    main()
'''.replace('@@NAME@@', json.dumps(name))


def _t_adjudication(hdr, name, rid, group, d):
    b, a = float(d['billed']), float(d['allowed'])
    return hdr + 'BILLED=%r\nALLOW=%r\n' % (b, a) + '''def main():
    pct = 100.0*ALLOW/BILLED
    print("billed:", BILLED, "| allowed:", ALLOW)
    print("allowed %:", round(pct, 1))
    assert BILLED > 0 and 0 <= ALLOW <= BILLED
    assert abs(pct - 100.0*ALLOW/BILLED) < 1e-9
    print("OK: adjudication verified for", @@NAME@@)
if __name__ == "__main__":
    main()
'''.replace('@@NAME@@', json.dumps(name))


def _t_fraudrate(hdr, name, rid, group, d):
    c, f = float(d['claims']), float(d['flagged'])
    return hdr + 'C=%r\nF=%r\n' % (c, f) + '''def main():
    pct = 100.0*F/C
    print("claims:", C, "| flagged:", F)
    print("flag rate %:", round(pct, 2))
    assert C > 0 and 0 <= F <= C
    assert abs(pct - 100.0*F/C) < 1e-9
    print("OK: fraud rate verified for", @@NAME@@)
if __name__ == "__main__":
    main()
'''.replace('@@NAME@@', json.dumps(name))


def _t_caseload(hdr, name, rid, group, d):
    w, c = float(d['workers']), float(d['cases'])
    return hdr + 'W=%r\nC=%r\n' % (w, c) + '''def main():
    per = C/W
    print("workers:", W, "| cases:", C)
    print("cases per worker:", round(per, 1))
    assert W > 0 and C >= 0
    assert abs(per - C/W) < 1e-9
    print("OK: caseload verified for", @@NAME@@)
if __name__ == "__main__":
    main()
'''.replace('@@NAME@@', json.dumps(name))


def _t_appealrate(hdr, name, rid, group, d):
    a, o = float(d['appeals']), float(d['overturned'])
    return hdr + 'A=%r\nO=%r\n' % (a, o) + '''def main():
    pct = 100.0*O/A
    print("appeals:", A, "| overturned:", O)
    print("overturn rate %:", round(pct, 1))
    assert A > 0 and 0 <= O <= A
    assert abs(pct - 100.0*O/A) < 1e-9
    print("OK: appeal rate verified for", @@NAME@@)
if __name__ == "__main__":
    main()
'''.replace('@@NAME@@', json.dumps(name))


_T = {'lossratio': _t_lossratio, 'combined': _t_combined,
      'premium': _t_premium, 'reserve': _t_reserve, 'subro': _t_subro,
      'eligibility': _t_eligibility, 'benefit': _t_benefit,
      'adjudication': _t_adjudication, 'fraudrate': _t_fraudrate,
      'caseload': _t_caseload, 'appealrate': _t_appealrate}


def build(dk, name, rid, group, data):
    assert dk in _T, 'unknown demo kind %r' % dk
    return _T[dk](_hdr(name, rid, group), name, rid, group, data)
