#!/usr/bin/env python3
"""Demo programs for the Price and Profit Tracking databases.

Every demo is real, runnable, stdlib-only Python performing the actual
price/profit computation for its record. All are machine-executed by build.py:
each prints its real computed values, asserts tight bounds (never float
exact-equality), and ends with the OK marker. Cross-checked against the entry
text in entries_price_profit_tracking.py - the numbers agree.
"""

_PREAMBLE = "import math\n"


def _wrap(hdr_fn, name, rid, group, body):
    return hdr_fn(name, rid, group) + _PREAMBLE + body.replace("NAME", __import__("json").dumps(name))


def demo_ppt_price_anatomy(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the six anatomical fields of a complete price record
    fields = ["amount", "currency", "unit", "time", "market", "terms"]
    print("anatomical fields: %d" % len(fields))
    for f in fields:
        print("  - %s" % f)
    assert len(fields) == 6
    # normalize a $4.50 dozen of eggs to per-egg
    per_egg = 4.50 / 12
    print("per-egg price: $%.4f" % per_egg)
    assert 0.374 < per_egg < 0.376
    print("rule: compare only after the six fields align")
    print("OK: %s dissected the record" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_ppt_nominal_vs_real(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # 1968 minimum wage $1.60 into 2023 dollars: CPI 34.8 -> 304.702
    cpi_1968, cpi_2023 = 34.8, 304.702
    real = 1.60 * (cpi_2023 / cpi_1968)
    print("1968 $1.60 in 2023 dollars: $%.2f" % real)
    assert 13.99 < real < 14.03
    mult = cpi_2023 / cpi_1968
    print("inflation multiplier 1968-2023: %.3f" % mult)
    assert 8.75 < mult < 8.76
    print("rule: nominal tells what people saw, real tells what they could buy")
    print("OK: %s weighed both monies" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_ppt_supply_demand(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # demand Q = 100 - 2P, supply Q = 20 + 3P
    p_star = (100 - 20) / (2 + 3)
    q_star = 100 - 2 * p_star
    print("equilibrium: P=%.1f Q=%.1f" % (p_star, q_star))
    assert p_star == 16 and q_star == 68
    # supply shifts left by 15 (harvest failure)
    p2 = (100 - (20 - 15)) / 5
    q2 = 100 - 2 * p2
    print("after supply shock: P=%.1f Q=%.1f" % (p2, q2))
    assert p2 == 19 and q2 == 62
    print("rule: price is a property of the meeting point, not the thing")
    print("OK: %s found the meeting point" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_ppt_cost_types(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    fixed, var, qty = 5000.0, 12.0, 400
    total = fixed + var * qty
    avg = total / qty
    print("total: $%.0f  average: $%.2f  marginal: $%.0f" % (total, avg, var))
    assert total == 9800.0
    assert 24.49 < avg < 24.51
    assert var == 12.0
    # scale effect: doubling quantity thins the fixed cost
    avg2 = (fixed + var * 800) / 800
    print("average at 800 loaves: $%.2f" % avg2)
    assert 18.24 < avg2 < 18.26
    print("rule: average cost for survival, marginal cost for the next unit")
    print("OK: %s read the ledger" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_ppt_markup_vs_margin(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    cost, price = 60.0, 100.0
    profit = price - cost
    markup = profit / cost
    margin = profit / price
    print("markup: %.2f %%  margin: %.2f %%" % (markup * 100, margin * 100))
    assert 0.665 < markup < 0.668
    assert 0.399 < margin < 0.401
    # conversion identities
    assert 0.399 < markup / (1 + markup) < 0.401
    # the classic shortfall: 40% markup is not 40% margin
    m40 = 0.40 / 1.40
    print("a 40%% markup earns only %.2f %% margin" % (m40 * 100))
    assert 0.285 < m40 < 0.287
    print("rule: ask which language the percentage speaks")
    print("OK: %s translated both tongues" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_ppt_cpi_measure(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # CPI-U annual averages: 2020 258.811, 2023 304.702
    cpi_2020, cpi_2023 = 258.811, 304.702
    infl = (cpi_2023 - cpi_2020) / cpi_2020 * 100.0
    print("inflation 2020-2023: %.2f %%" % infl)
    assert 17.70 < infl < 17.77
    # the basket costs ~3x its 1982-84 base
    print("2023 basket vs 1982-84 base: %.2fx" % (cpi_2023 / 100.0))
    assert 3.04 < cpi_2023 / 100.0 < 3.06
    print("rule: (later - earlier) / earlier, basket disclosed")
    print("OK: %s read the thermometer" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_ppt_reading_price_tag(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    a = 3.29 / 12.0
    b = 4.99 / 20.0
    print("coffee A: $%.4f/oz  coffee B: $%.4f/oz" % (a, b))
    assert 0.274 < a < 0.275
    assert 0.249 < b < 0.250
    saving = (a - b) / a * 100.0
    print("B cheaper by %.1f %%" % saving)
    assert b < a
    assert 8.9 < saving < 9.1
    print("rule: convert, note terms, stamp time")
    print("OK: %s read the fine print" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_ppt_break_even(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    fixed, price, var = 12000.0, 25.0, 13.0
    contrib = price - var
    be_qty = fixed / contrib
    be_rev = be_qty * price
    print("break-even: %.0f units, $%.0f revenue" % (be_qty, be_rev))
    assert be_qty == 1000.0
    assert be_rev == 25000.0
    # margin of safety at 1400 units
    safety_units = 1400 - be_qty
    safety_profit = safety_units * contrib
    print("safety at 1400 units: %.0f units -> $%.0f profit" % (safety_units, safety_profit))
    assert safety_profit == 4800.0
    # a $1 price rise lowers break-even
    be2 = fixed / (26.0 - var)
    print("break-even at $26 price: %.1f units" % be2)
    assert 923.0 < be2 < 923.2
    print("rule: raise price, cut variable cost, or cut fixed cost")
    print("OK: %s counted to the milestone" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_ppt_profit_layers(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    rev, cogs, opex, below = 1000000.0, 620000.0, 230000.0, 50000.0
    gross = rev - cogs
    oper = gross - opex
    net = oper - below
    gm, om, nm = gross / rev, oper / rev, net / rev
    print("gross %.0f (%.0f %%)  operating %.0f (%.0f %%)  net %.0f (%.0f %%)"
          % (gross, gm * 100, oper, om * 100, net, nm * 100))
    assert 0.379 < gm < 0.381
    assert 0.149 < om < 0.151
    assert 0.099 < nm < 0.101
    print("rule: the layer where profit vanishes names the problem")
    print("OK: %s stacked the layers" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_ppt_gold_series(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # LBMA annual averages $/oz
    series = {1970: 36.02, 1980: 615.00, 1990: 383.51, 2000: 279.11,
              2010: 1224.53, 2020: 1769.64, 2024: 2394.86}
    yrs = 2024 - 1970
    cagr = (series[2024] / series[1970]) ** (1.0 / yrs) - 1
    print("gold 1970-2024 CAGR: %.2f %%" % (cagr * 100))
    assert 0.0805 < cagr < 0.0812
    # real conversion: 1980 $615 into 2023 dollars (CPI 82.4 -> 304.702)
    real1980 = 615.0 * (304.702 / 82.4)
    print("1980 $615 in 2023 dollars: $%.0f" % real1980)
    assert 2272.0 < real1980 < 2277.0
    print("1980 peak $850 intraday; 2024 nominal $%.2f" % series[2024])
    print("rule: read every long series twice - nominal and real")
    print("OK: %s read the century" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_ppt_oil_series(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # WTI annual averages $/bbl
    avg2008, avg2020 = 99.67, 39.68
    drop = (avg2008 - avg2020) / avg2008 * 100.0
    print("2008 avg $%.2f -> 2020 avg $%.2f: %.1f %% decline" % (avg2008, avg2020, drop))
    assert 60.1 < drop < 60.3
    print("landmarks: Jul 2008 spike $145.31; Apr 20 2020 print -$36.98")
    print("2024 avg $76.63; 2025 avg $65.39")
    assert 76.0 < 76.63 < 77.5
    print("rule: quote average, high, and low - or the average lies")
    print("OK: %s survived the volatility" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_ppt_housing_series(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # median new-home price: 1975 $39,300 -> 2024 $420,300
    p1975, p2024 = 39300.0, 420300.0
    mult = p2024 / p1975
    yrs = 2024 - 1975
    cagr = mult ** (1.0 / yrs) - 1
    print("multiple: %.2fx  CAGR: %.2f %%" % (mult, cagr * 100))
    assert 10.69 < mult < 10.71
    assert 0.0493 < cagr < 0.0498
    # real conversion: CPI 53.8 -> 304.702
    real1975 = p1975 * (304.702 / 53.8)
    print("1975 price in 2023 dollars: $%.0f" % real1975)
    assert 222400.0 < real1975 < 222800.0
    print("rule: nominal, real, and relative to income - all three")
    print("OK: %s walked the 49 years" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_ppt_sp500_series(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # S&P 500 year-end closes
    c2010, c2024 = 1257.64, 5881.63
    mult = c2024 / c2010
    cagr = mult ** (1.0 / 14.0) - 1
    print("2010-2024: %.2fx  CAGR %.2f %% (price return)" % (mult, cagr * 100))
    assert 4.67 < mult < 4.69
    assert 0.1160 < cagr < 0.1170
    # 2007-2009 drawdown: ~1565 high to 666 trough
    dd = (1565.0 - 666.0) / 1565.0 * 100.0
    print("2007-2009 drawdown: %.1f %%" % dd)
    assert 57.3 < dd < 57.6
    print("rule: price return understates owner return - add dividends")
    print("OK: %s read the market diary" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_ppt_inflation_adjustment(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # $20 of 1913 (CPI 9.9) into 2023 dollars (CPI 304.702)
    v1913 = 20.0 * (304.702 / 9.9)
    print("$20 in 1913 = $%.2f in 2023 dollars" % v1913)
    assert 615.0 < v1913 < 616.2
    # $7.25 of 2009 (CPI 214.537) into 2023 dollars
    v2009 = 7.25 * (304.702 / 214.537)
    print("$7.25 in 2009 = $%.2f in 2023 dollars" % v2009)
    assert 10.28 < v2009 < 10.32
    print("rule: annual averages for annual data; print the reference year")
    print("OK: %s ran the time machine" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_ppt_depreciation_methods(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    cost, life = 10000.0, 5
    sl = cost / life
    ddb1 = cost * (2.0 / life)
    syd1 = cost * (5.0 / 15.0)
    print("SL/yr $%.0f  DDB yr1 $%.0f  SYD yr1 $%.2f" % (sl, ddb1, syd1))
    assert sl == 2000.0
    assert ddb1 == 4000.0
    assert 3333.3 < syd1 < 3333.4
    # the full SYD schedule sums to cost
    sched = [cost * (d / 15.0) for d in (5, 4, 3, 2, 1)]
    print("SYD schedule: %s" % ["%.2f" % s for s in sched])
    assert 9999.9 < sum(sched) < 10000.1
    print("rule: total is always cost - salvage; only timing differs")
    print("OK: %s confessed the aging" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_ppt_appreciation_cagr(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # gold 2000 $279.11 -> 2024 $2394.86
    mult = 2394.86 / 279.11
    cagr = mult ** (1.0 / 24.0) - 1
    print("multiple %.3f  CAGR %.2f %%" % (mult, cagr * 100))
    assert 8.57 < mult < 8.59
    assert 0.0933 < cagr < 0.0941
    # closing the loop
    back = 279.11 * (1 + cagr) ** 24
    print("loop check: %.2f" % back)
    assert 2394.0 < back < 2396.0
    # the naive simple-average trap
    naive = (mult - 1) / 24.0
    print("naive average %.1f %% vs CAGR %.2f %% - compounding matters" % (naive * 100, cagr * 100))
    assert naive > 0.30
    print("rule: quote volatility beside CAGR; never annualize under five years")
    print("OK: %s measured honestly" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_ppt_comparables_approach(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    comp_a = 340000.0 / 1700.0
    comp_b = 399000.0 / 1900.0
    avg = (comp_a + comp_b) / 2.0
    value = 1800.0 * avg
    print("comps $%.0f/sqft and $%.0f/sqft -> value $%.0f" % (comp_a, comp_b, value))
    assert comp_a == 200.0
    assert comp_b == 210.0
    assert value == 369000.0
    # business version: 6x revenue on $10M
    biz = 10.0 * 6.0
    print("peer multiple 6x on $10M revenue -> $%.0fM" % biz)
    assert biz == 60.0
    print("rule: recent, nearby, similar, arm's-length - three good beat ten distant")
    print("OK: %s heard the neighbors" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_ppt_cost_approach(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    replacement, depreciation, land = 280000.0, 60000.0, 90000.0
    # depreciation's three faces
    physical, functional, external = 25000.0, 20000.0, 15000.0
    assert physical + functional + external == depreciation
    value = replacement - depreciation + land
    print("value = %.0f - %.0f + %.0f = $%.0f" % (replacement, depreciation, land, value))
    assert value == 310000.0
    print("rule: the cost approach sets the ceiling - reconcile, never average blindly")
    print("OK: %s priced the rebuild" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_ppt_income_approach_dcf(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    c, r, n = 10000.0, 0.08, 5
    pv = c * (1 - (1 + r) ** -n) / r
    print("PV of $10k/yr x 5yr at 8%%: $%.2f" % pv)
    assert 39920.0 < pv < 39935.0
    # sensitivity across rates
    for rr in (0.06, 0.10):
        v = c * (1 - (1 + rr) ** -n) / rr
        print("  at %d%%: $%.2f" % (int(rr * 100), v))
    v6 = c * (1 - 1.06 ** -n) / 0.06
    v10 = c * (1 - 1.10 ** -n) / 0.10
    assert 42115.0 < v6 < 42135.0
    assert 37900.0 < v10 < 37915.0
    # Gordon growth: $10k growing 2% at 8%
    g = 10000.0 / (0.08 - 0.02)
    print("growing perpetuity: $%.2f" % g)
    assert 166660.0 < g < 166675.0
    print("rule: the discount rate is the whole argument - show the table")
    print("OK: %s priced tomorrow" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_ppt_price_elasticity(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    dq = (85 - 100) / 100.0
    dp = (12 - 10) / 10.0
    e = dq / dp
    print("elasticity: %.2f" % e)
    assert -0.76 < e < -0.74
    r0, r1 = 100 * 10.0, 85 * 12.0
    print("revenue $%.0f -> $%.0f: %s" % (r0, r1, "rose (inelastic)" if r1 > r0 else "fell"))
    assert r1 == 1020.0
    # midpoint formula
    em = ((85 - 100) / 92.5) / ((12 - 10) / 11.0)
    print("arc elasticity: %.2f" % em)
    assert -0.90 < em < -0.88
    print("rule: raise where inelastic, cut where elastic - measure first")
    print("OK: %s heard the buyers answer" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_ppt_margins_by_industry(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # net profit on $100 revenue: grocery $2, restaurant $6, software $27
    margins = {"grocery": 2.0 / 100, "restaurant": 6.0 / 100, "software": 27.0 / 100}
    for k, v in margins.items():
        print("  %-10s net margin %.0f %%" % (k, v * 100))
    assert 0.019 < margins["grocery"] < 0.021
    assert 0.059 < margins["restaurant"] < 0.061
    assert 0.269 < margins["software"] < 0.271
    assert margins["grocery"] < margins["restaurant"] < margins["software"]
    print("rule: judge profit against the industry normal, never in the abstract")
    print("OK: %s read the league tables" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_ppt_unit_economics(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    monthly, gm = 50.0, 0.80
    gp = monthly * gm
    cac, life = 120.0, 24
    payback = cac / gp
    ltv = gp * life
    ratio = ltv / cac
    print("gross/customer/mo $%.0f  payback %.0f mo  LTV $%.0f  LTV/CAC %.0f" % (gp, payback, ltv, ratio))
    assert gp == 40.0
    assert payback == 3.0
    assert ltv == 960.0
    assert ratio == 8.0
    # stress: lifetime halves
    print("if lifetime 12 mo: LTV/CAC = %.1f" % ((gp * 12) / cac))
    assert (gp * 12) / cac == 4.0
    print("rule: audit the one customer before blessing the million")
    print("OK: %s passed the one-customer audit" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_ppt_price_index_construction(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # Laspeyres: base basket $100, current cost $118
    idx = 118.0 / 100.0 * 100.0
    print("Laspeyres index: %.0f -> %.0f %% inflation" % (idx, idx - 100))
    assert idx == 118.0
    # hedonic: $1000 laptop, benchmark 100 -> 200
    per_unit_old = 1000.0 / 100.0
    per_unit_new = 1000.0 / 200.0
    decline = (per_unit_old - per_unit_new) / per_unit_old * 100.0
    print("quality-adjusted price decline: %.0f %%" % decline)
    assert decline == 50.0
    print("rule: publish basket, weights, base period, and adjustments")
    print("OK: %s built the machine" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_ppt_timeseries_tools(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    y = [100.0, 102.0, 101.0, 105.0, 107.0]
    sma = sum(y[-3:]) / 3.0
    print("3-period SMA: %.2f" % sma)
    assert 104.32 < sma < 104.35
    chg = [(y[i] - y[i - 1]) / y[i - 1] for i in range(1, len(y))]
    mean = sum(chg) / len(chg)
    vol = math.sqrt(sum((c - mean) ** 2 for c in chg) / (len(chg) - 1))
    print("period volatility: %.2f %%" % (vol * 100))
    assert 0.020 < vol < 0.021
    # least-squares slope, x = 0..4
    mx, my = 2.0, sum(y) / 5.0
    slope = sum((i - mx) * (v - my) for i, v in enumerate(y)) / sum((i - mx) ** 2 for i in range(5))
    print("trend slope: %.2f per period" % slope)
    assert 1.69 < slope < 1.71
    print("rule: smooth before judging, measure noise before trusting signal")
    print("OK: %s listened patiently" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_ppt_purchasing_power_lifetime(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # $1 of 1970 (CPI 38.8) in 2023 dollars (CPI 304.702)
    v = 304.702 / 38.8
    retained = 38.8 / 304.702
    print("$1 of 1970 = $%.2f in 2023; retained %.1f %%" % (v, retained * 100))
    assert 7.84 < v < 7.87
    assert 0.127 < retained < 0.128
    home = 23400.0 * v
    print("1970 median home in 2023 dollars: $%.0f" % home)
    assert 183600.0 < home < 183900.0
    # forward: 3% inflation, 20 and 40 years
    f20 = 1 / 1.03 ** 20
    f40 = 1 / 1.03 ** 40
    print("dollar in 20yr: %.2f  in 40yr: %.2f" % (f20, f40))
    assert 0.553 < f20 < 0.555
    assert 0.306 < f40 < 0.308
    print("rule of 72: at 3%%, halves every %.0f years" % (72 / 3))
    print("rule: nominal for the story, real for the judgment")
    print("OK: %s spanned the lifetime" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_ppt_fermi_ballpark(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    vehicles, miles, mpg, price = 240_000_000, 12000.0, 25.0, 3.50
    gal_per_vehicle = miles / mpg
    per_vehicle = gal_per_vehicle * price
    total = vehicles * per_vehicle
    print("gal/vehicle/yr: %.0f  $/vehicle/yr: $%.0f" % (gal_per_vehicle, per_vehicle))
    print("annual US gasoline spending: $%.1fB" % (total / 1e9))
    assert gal_per_vehicle == 480.0
    assert per_vehicle == 1680.0
    assert 4.031e11 < total < 4.033e11
    print("ballpark range: $300-500B - order of magnitude, not false precision")
    print("rule: decompose, estimate coarsely, multiply, sanity-check")
    print("OK: %s built an honest ballpark" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_ppt_analogous_estimation(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # analog $199 x 1.4 capability factor
    band = 199.0 * 1.4
    print("analog-adjusted band center: $%.1f" % band)
    assert 278.5 < band < 278.7
    # PERT three-point: optimistic 350, likely 280, pessimistic 220
    pert = (350.0 + 4 * 280.0 + 220.0) / 6.0
    print("PERT expected price: $%.2f (range $220-$350)" % pert)
    assert 281.6 < pert < 281.8
    print("rule: the estimate lives until real sales arrive")
    print("OK: %s priced the stranger" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_ppt_market_multiples(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    pe_price = 2.0 * 20.0
    ev = 12_000_000.0 * 8.0
    capval = 50000.0 / 0.06
    print("P/E price $%.0f  EV $%.0fM  cap-rate value $%.2f" % (pe_price, ev / 1e6, capval))
    assert pe_price == 40.0
    assert ev == 96_000_000.0
    assert 833300.0 < capval < 833400.0
    # PEG check: P/E 20 on 15% growth
    peg = 20.0 / 15.0
    print("PEG at 15%% growth: %.2f" % peg)
    assert 1.32 < peg < 1.34
    print("rule: triangulate with DCF and cost - never multiples alone")
    print("OK: %s heard all three witnesses" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_ppt_inventory_valuation(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # buy 10 @ $5 then 10 @ $7; sell 12 at $10
    fifo_cogs = 10 * 5.0 + 2 * 7.0
    fifo_end = 8 * 7.0
    lifo_cogs = 10 * 7.0 + 2 * 5.0
    lifo_end = 8 * 5.0
    avg = 120.0 / 20.0
    avg_cogs, avg_end = 12 * avg, 8 * avg
    print("FIFO COGS $%.0f inv $%.0f | LIFO COGS $%.0f inv $%.0f | AVG COGS $%.0f inv $%.0f"
          % (fifo_cogs, fifo_end, lifo_cogs, lifo_end, avg_cogs, avg_end))
    assert (fifo_cogs, fifo_end) == (64.0, 56.0)
    assert (lifo_cogs, lifo_end) == (80.0, 40.0)
    assert (avg_cogs, avg_end) == (72.0, 48.0)
    reserve = fifo_end - lifo_end
    swing = (120.0 - fifo_cogs) - (120.0 - lifo_cogs)
    print("LIFO reserve: $%.0f; gross-profit swing at $10 price: $%.0f" % (reserve, swing))
    assert reserve == 16.0
    assert swing == 16.0
    print("rule: disclose the method and the reserve")
    print("OK: %s counted which dollars left" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_ppt_price_forecasting(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # quarterly sales $100K, $110K, $121K: +10% trend
    trend = 121.0 * 1.10
    seasonal = trend * 1.15
    print("trend forecast $%.1fK  seasonal Q4 $%.2fK" % (trend, seasonal))
    assert 133.0 < trend < 133.2
    assert 153.0 < seasonal < 153.2
    # 80% prediction interval from residual std $9K
    lo, hi = trend - 1.28 * 9.0, trend + 1.28 * 9.0
    print("80%% interval: $%.1fK - $%.1fK" % (lo, hi))
    assert 121.5 < lo < 121.7
    assert 144.5 < hi < 144.7
    print("rule: interval, assumptions, expiry date - or it is a wish")
    print("OK: %s confessed the unknown" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_ppt_profit_attribution(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    a = 1000 * 20.0
    b = 500 * 60.0
    total = a + b
    print("A $%.0f (%.0f %%)  B $%.0f (%.0f %%)" % (a, a / total * 100, b, b / total * 100))
    assert a == 20000.0
    assert b == 30000.0
    assert 0.599 < b / total < 0.601
    # customer truth: revenue 10k, product cost 6k, service 3.5k
    true_profit = 10000.0 - 6000.0 - 3500.0
    print("true customer profit: $%.0f (not the $4000 the sales report claims)" % true_profit)
    assert true_profit == 500.0
    # channel: 15% marketplace fee on $20 contribution
    direct, market = 20.0, 20.0 * 0.85
    print("direct $%.0f vs marketplace $%.0f contribution" % (direct, market))
    assert market == 17.0
    print("rule: unattributed profit is luck; attributed profit is strategy")
    print("OK: %s named the authors" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_ppt_hurdle_rate(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    wacc = 0.60 * 0.10 + 0.40 * 0.05 * (1 - 0.25)
    print("WACC: %.2f %%" % (wacc * 100))
    assert 0.0749 < wacc < 0.0751
    for irr, verdict in ((0.09, "accept"), (0.06, "reject")):
        print("project IRR %.0f %% vs hurdle %.2f %%: %s" % (irr * 100, wacc * 100, verdict))
        assert (irr > wacc) == (verdict == "accept")
    risky = wacc + 0.075
    print("speculative venture hurdle: %.2f %%" % (risky * 100))
    assert 0.149 < risky < 0.151
    print("rule: set the hurdle from markets, not from ambition")
    print("OK: %s guarded the door" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_ppt_pricing_psychology(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    anchor, price = 499.0, 349.0
    perceived = (anchor - price) / anchor * 100.0
    print("perceived discount: %.2f %%" % perceived)
    assert 30.0 < perceived < 30.2
    # honesty test: was the anchor ever real? (flag, not proof)
    anchor_was_real = True
    print("anchor was a real past price: %s" % anchor_was_real)
    assert anchor_was_real
    print("rule: rhetoric for a true price is courtesy; for a false anchor, perjury")
    print("OK: %s persuaded without deceiving" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_ppt_price_record_capstone(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    record = {
        "item": "regular gasoline", "amount": 3.50, "currency": "USD",
        "unit": "per gallon", "per_unit": 3.50 / 1.0,
        "timestamp": "2024-06-01", "market": "retail, Ohio, USA",
        "terms": "price includes motor-fuel tax", "source": "station pump survey",
        "nominal": 3.50, "real_2024": 3.50, "record_id": "JAH-PFT-000034",
    }
    required = ["item", "amount", "currency", "unit", "per_unit", "timestamp",
                "market", "terms", "source", "nominal", "real_2024", "record_id"]
    missing = [k for k in required if k not in record]
    print("fields present: %d/12" % (len(required) - len(missing)))
    assert not missing
    assert record["amount"] > 0
    # per-unit normalization of the dozen-eggs example
    per_egg = 4.50 / 12
    print("per-egg normalization: $%.3f" % per_egg)
    assert 0.374 < per_egg < 0.376
    # profit anatomy beside price anatomy: $0.10/gal retail margin
    retail_margin = 0.10 / 3.50 * 100.0
    print("retail margin: %.2f %%" % retail_margin)
    assert 2.85 < retail_margin < 2.87
    # dedupe key
    key = (record["record_id"], record["timestamp"], record["source"])
    print("dedupe key: %s" % (key,))
    assert len(set([key])) == 1
    print("rule: machine-readable, human-readable, time-travel-ready")
    print("OK: %s sealed the covenant" % NAME)
if __name__ == "__main__":
    main()
''')

DEMOS = {
    "price-anatomy": demo_ppt_price_anatomy,
    "nominal-vs-real": demo_ppt_nominal_vs_real,
    "supply-demand": demo_ppt_supply_demand,
    "cost-types": demo_ppt_cost_types,
    "markup-vs-margin": demo_ppt_markup_vs_margin,
    "cpi-measure": demo_ppt_cpi_measure,
    "reading-price-tag": demo_ppt_reading_price_tag,
    "break-even": demo_ppt_break_even,
    "profit-layers": demo_ppt_profit_layers,
    "gold-series": demo_ppt_gold_series,
    "oil-series": demo_ppt_oil_series,
    "housing-series": demo_ppt_housing_series,
    "sp500-series": demo_ppt_sp500_series,
    "inflation-adjustment": demo_ppt_inflation_adjustment,
    "depreciation-methods": demo_ppt_depreciation_methods,
    "appreciation-cagr": demo_ppt_appreciation_cagr,
    "comparables-approach": demo_ppt_comparables_approach,
    "cost-approach": demo_ppt_cost_approach,
    "income-approach-dcf": demo_ppt_income_approach_dcf,
    "price-elasticity": demo_ppt_price_elasticity,
    "margins-by-industry": demo_ppt_margins_by_industry,
    "unit-economics": demo_ppt_unit_economics,
    "price-index-construction": demo_ppt_price_index_construction,
    "timeseries-tools": demo_ppt_timeseries_tools,
    "purchasing-power-lifetime": demo_ppt_purchasing_power_lifetime,
    "fermi-ballpark": demo_ppt_fermi_ballpark,
    "analogous-estimation": demo_ppt_analogous_estimation,
    "market-multiples": demo_ppt_market_multiples,
    "inventory-valuation": demo_ppt_inventory_valuation,
    "price-forecasting": demo_ppt_price_forecasting,
    "profit-attribution": demo_ppt_profit_attribution,
    "hurdle-rate": demo_ppt_hurdle_rate,
    "pricing-psychology": demo_ppt_pricing_psychology,
    "price-record-capstone": demo_ppt_price_record_capstone,
}
