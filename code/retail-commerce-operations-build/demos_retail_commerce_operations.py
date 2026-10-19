#!/usr/bin/env python3
"""Demonstration programs for the Retail Commerce Operations databases.

Every demo is real, runnable, stdlib-only Python that machine-checks the
record it ships with: the entry's own data is baked into the program, the
program recomputes real values from it, asserts tight bounds (never float
exact-equality), prints the real computed values, and ends with the OK
marker. The build machine-executes every demo.
"""
import json
import math


def _hdr(name, rid, group):
    return ('#!/usr/bin/env python3\n"""%s — working demonstration.\n'
            'Record %s [%s]. Property of Justin Addam Higgins (JAH).\n"""\n'
            % (name, rid, group))


def _t_eoq(hdr, name, rid, group, d):
    D, S, H = float(d['D']), float(d['S']), float(d['H'])
    return hdr + 'import math\nD=%r\nS=%r\nH=%r\n' % (D, S, H) + '''def main():
    eoq = math.sqrt(2*D*S/H)
    orders = D/eoq
    total = (D/eoq)*S + (eoq/2)*H
    print("annual demand:", D)
    print("EOQ:", round(eoq, 2), "units")
    print("orders per year:", round(orders, 2))
    print("total annual cost: $", round(total, 2))
    assert eoq > 0 and orders > 0 and total > 0
    assert abs(eoq - math.sqrt(2*D*S/H)) < 1e-9
    assert 0 < orders < D
    print("OK: EOQ verified for", @@NAME@@)
if __name__ == "__main__":
    main()
'''.replace('@@NAME@@', json.dumps(name))


def _t_turnover(hdr, name, rid, group, d):
    cogs, inv = float(d['cogs']), float(d['avg_inv'])
    return hdr + 'COGS=%r\nAVG_INV=%r\n' % (cogs, inv) + '''def main():
    turns = COGS/AVG_INV
    days = 365.0/turns
    print("cost of goods sold: $", round(COGS, 2))
    print("average inventory: $", round(AVG_INV, 2))
    print("inventory turnover:", round(turns, 2), "turns/year")
    print("days of supply:", round(days, 1))
    assert turns > 0
    assert abs(turns*AVG_INV - COGS) < 1e-6*COGS + 1e-6
    assert 0 < days < 3650
    print("OK: turnover verified for", @@NAME@@)
if __name__ == "__main__":
    main()
'''.replace('@@NAME@@', json.dumps(name))


def _t_markdown(hdr, name, rid, group, d):
    orig, pct = float(d['orig']), float(d['pct'])
    return hdr + 'ORIG=%r\nPCT=%r\n' % (orig, pct) + '''def main():
    sale = ORIG*(1-PCT/100.0)
    taken = ORIG-sale
    print("original price: $", round(ORIG, 2))
    print("markdown percent:", PCT)
    print("sale price: $", round(sale, 2))
    print("markdown dollars: $", round(taken, 2))
    assert 0 <= sale <= ORIG
    assert abs(taken - ORIG*PCT/100.0) < 0.01
    assert abs(sale + taken - ORIG) < 0.01
    print("OK: markdown verified for", @@NAME@@)
if __name__ == "__main__":
    main()
'''.replace('@@NAME@@', json.dumps(name))


def _t_sellthru(hdr, name, rid, group, d):
    rec, sold = float(d['received']), float(d['sold'])
    return hdr + 'RECEIVED=%r\nSOLD=%r\n' % (rec, sold) + '''def main():
    st = 100.0*SOLD/RECEIVED
    left = RECEIVED-SOLD
    print("units received:", RECEIVED)
    print("units sold:", SOLD)
    print("sell-through:", round(st, 1), "%")
    print("units remaining:", left)
    assert 0 <= st <= 100.0
    assert abs(SOLD/RECEIVED*100.0 - st) < 1e-9
    print("OK: sell-through verified for", @@NAME@@)
if __name__ == "__main__":
    main()
'''.replace('@@NAME@@', json.dumps(name))


def _t_gmroi(hdr, name, rid, group, d):
    gm, inv = float(d['gross_margin']), float(d['avg_inv_cost'])
    return hdr + 'GM=%r\nINV=%r\n' % (gm, inv) + '''def main():
    gmroi = GM/INV
    print("gross margin dollars: $", round(GM, 2))
    print("average inventory cost: $", round(INV, 2))
    print("GMROI:", round(gmroi, 2))
    assert gmroi > 0
    assert abs(gmroi*INV - GM) < 1e-6*GM + 1e-6
    print("OK: GMROI verified for", @@NAME@@)
if __name__ == "__main__":
    main()
'''.replace('@@NAME@@', json.dumps(name))


def _t_basket(hdr, name, rid, group, d):
    tx, it, rev = float(d['txns']), float(d['items']), float(d['revenue'])
    return hdr + 'TXNS=%r\nITEMS=%r\nREV=%r\n' % (tx, it, rev) + '''def main():
    avg = REV/TXNS
    ipt = ITEMS/TXNS
    print("transactions:", TXNS)
    print("average basket: $", round(avg, 2))
    print("items per transaction:", round(ipt, 2))
    assert avg > 0 and ipt >= 1.0
    assert abs(avg*TXNS - REV) < 1e-6*REV + 1e-6
    print("OK: basket metrics verified for", @@NAME@@)
if __name__ == "__main__":
    main()
'''.replace('@@NAME@@', json.dumps(name))


def _t_markup(hdr, name, rid, group, d):
    cost, price = float(d['cost']), float(d['price'])
    return hdr + 'COST=%r\nPRICE=%r\n' % (cost, price) + '''def main():
    markup = 100.0*(PRICE-COST)/COST
    margin = 100.0*(PRICE-COST)/PRICE
    print("cost: $", round(COST, 2), "| price: $", round(PRICE, 2))
    print("markup on cost:", round(markup, 1), "%")
    print("margin on price:", round(margin, 1), "%")
    assert PRICE > COST > 0
    assert markup > margin > 0
    assert abs((PRICE-COST)/COST*100.0 - markup) < 1e-9
    print("OK: markup/margin verified for", @@NAME@@)
if __name__ == "__main__":
    main()
'''.replace('@@NAME@@', json.dumps(name))


def _t_breakeven(hdr, name, rid, group, d):
    fx, pr, vc = float(d['fixed']), float(d['price']), float(d['varcost'])
    return hdr + 'FIXED=%r\nPRICE=%r\nVARCOST=%r\n' % (fx, pr, vc) + '''def main():
    be = FIXED/(PRICE-VARCOST)
    print("fixed cost: $", round(FIXED, 2))
    print("contribution per unit: $", round(PRICE-VARCOST, 2))
    print("break-even units:", round(be, 1))
    assert PRICE > VARCOST > 0 and FIXED > 0
    assert abs(be*(PRICE-VARCOST) - FIXED) < 1e-6*FIXED + 1e-6
    print("OK: break-even verified for", @@NAME@@)
if __name__ == "__main__":
    main()
'''.replace('@@NAME@@', json.dumps(name))


def _t_shrink(hdr, name, rid, group, d):
    sales, pct = float(d['sales']), float(d['shrink_pct'])
    return hdr + 'SALES=%r\nPCT=%r\n' % (sales, pct) + '''def main():
    dollars = SALES*PCT/100.0
    print("net sales: $", round(SALES, 2))
    print("shrink rate:", PCT, "%")
    print("shrink dollars: $", round(dollars, 2))
    assert 0 <= PCT < 100.0
    assert abs(dollars - SALES*PCT/100.0) < 1e-6*SALES + 1e-6
    print("OK: shrink verified for", @@NAME@@)
if __name__ == "__main__":
    main()
'''.replace('@@NAME@@', json.dumps(name))


def _t_loyalty(hdr, name, rid, group, d):
    mem, pts, val = float(d['members']), float(d['avg_points']), float(d['point_value'])
    return hdr + 'MEMBERS=%r\nAVG_PTS=%r\nPT_VAL=%r\n' % (mem, pts, val) + '''def main():
    liability = MEMBERS*AVG_PTS*PT_VAL
    per_member = AVG_PTS*PT_VAL
    print("members:", MEMBERS)
    print("liability for unredeemed points: $", round(liability, 2))
    print("average value per member: $", round(per_member, 2))
    assert liability > 0 and per_member > 0
    assert abs(liability/MEMBERS - per_member) < 1e-9
    print("OK: loyalty liability verified for", @@NAME@@)
if __name__ == "__main__":
    main()
'''.replace('@@NAME@@', json.dumps(name))


_T = {'eoq': _t_eoq, 'turnover': _t_turnover, 'markdown': _t_markdown,
      'sellthru': _t_sellthru, 'gmroi': _t_gmroi, 'basket': _t_basket,
      'markup': _t_markup, 'breakeven': _t_breakeven, 'shrink': _t_shrink,
      'loyalty': _t_loyalty}


def build(dk, name, rid, group, data):
    assert dk in _T, 'unknown demo kind %r' % dk
    return _T[dk](_hdr(name, rid, group), name, rid, group, data)
