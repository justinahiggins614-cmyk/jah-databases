#!/usr/bin/env python3
"""Demo programs for the Manufacturing Cost databases.

Every demo is real, runnable, stdlib-only Python performing the actual cost
computation for its record. All are machine-executed by build.py: each prints
its real computed values, asserts tight bounds (never float exact-equality),
and ends with the OK marker.
"""

_PREAMBLE = "import math\n"


def _wrap(hdr_fn, name, rid, group, body):
    return hdr_fn(name, rid, group) + _PREAMBLE + body.replace("NAME", __import__("json").dumps(name))


def demo_mfg_what_is(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the three elements of manufacturing cost on the example device
    material, labor, overhead = 4.20, 2.80, 3.50
    unit_cost = material + labor + overhead
    prime = material + labor
    conversion = labor + overhead
    print("material: %.2f  labor: %.2f  overhead: %.2f" % (material, labor, overhead))
    print("prime cost: %.2f  conversion cost: %.2f" % (prime, conversion))
    print("unit manufacturing cost: %.2f" % unit_cost)
    assert 10.49 < unit_cost < 10.51
    assert 6.99 < prime < 7.01
    assert 6.29 < conversion < 6.31
    print("rule: material + labor + overhead, nothing else, is the cost of making")
    print("OK: %s stacked the three elements" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_mfg_bom(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # five-line BOM roll-up: qty-per times unit price, summed
    bom = [("housing", 1, 1.10), ("screws", 4, 0.04), ("circuit board", 1, 2.30),
           ("label", 1, 0.05), ("shipping box", 1, 0.35)]
    total = 0.0
    for part, qty, price in bom:
        ext = qty * price
        total += ext
        print("  %-14s %d x %5.2f = %5.2f" % (part, qty, price, ext))
    print("BOM material roll-up: %.2f" % total)
    assert 3.95 < total < 3.97
    print("rule: extended cost is quantity times price, and the sum is the truth")
    print("OK: %s rolled the recipe" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_mfg_material_cost(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # sheet-steel bracket: gross stock, scrap credit, net material cost
    gross_kg, price = 1.0, 2.50
    part_kg = 0.8
    scrap_kg, scrap_price = gross_kg - part_kg, 0.30
    gross_cost = gross_kg * price
    credit = scrap_kg * scrap_price
    net = gross_cost - credit
    utilization = part_kg / gross_kg * 100.0
    print("gross steel cost: %.2f" % gross_cost)
    print("scrap credit: %.2f" % credit)
    print("net material cost: %.2f" % net)
    print("utilization: %.1f %%" % utilization)
    assert 2.49 < gross_cost < 2.51
    assert 0.05 < credit < 0.07
    assert 2.43 < net < 2.45
    assert 79.9 < utilization < 80.1
    print("rule: price times gross stock, minus what the scrap man pays back")
    print("OK: %s priced the steel honestly" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_mfg_labor_cost(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # burdened labor rate: wage plus the BLS benefit load, then per-unit time
    wage, burden = 24.00, 0.31
    rate = wage * (1 + burden)
    minutes_per_unit = 6.0
    unit_labor = rate * minutes_per_unit / 60.0
    print("burdened rate: %.2f $/hr" % rate)
    print("labor cost per unit: %.2f" % unit_labor)
    assert 31.43 < rate < 31.45
    assert 3.13 < unit_labor < 3.15
    # the error of using the bare wage
    bare = wage * minutes_per_unit / 60.0
    under = (unit_labor - bare) / unit_labor * 100.0
    print("bare-wage error understates labor by %.1f %%" % under)
    assert 23.6 < under < 23.8
    print("rule: the wage is not the cost of an hour")
    print("OK: %s burdened the hour" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_mfg_overhead_intro(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # overhead allocation: pool over base gives the rate, usage absorbs it
    pool, base_hours = 1200000.0, 60000.0
    rate = pool / base_hours
    job_hours = 2.5
    absorbed = rate * job_hours
    print("overhead rate: %.2f $/DLH" % rate)
    print("job absorbs: %.2f" % absorbed)
    assert 19.99 < rate < 20.01
    assert 49.99 < absorbed < 50.01
    # the base-choice effect: same pool over machine hours instead
    mrate = pool / 40000.0
    print("same pool over 40,000 machine hours: %.2f $/MH" % mrate)
    assert 29.99 < mrate < 30.01
    print("rule: the base is the whole game - choose it like it matters")
    print("OK: %s divided the roof fairly" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_mfg_cost_stack(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the full ladder: elements -> prime/conversion -> COGM -> COGS
    dm, dl, oh = 4.20, 2.80, 3.50
    prime = dm + dl
    conversion = dl + oh
    mfg = dm + dl + oh
    begin_wip, end_wip = 1.00, 0.50
    cogm = mfg + begin_wip - end_wip
    begin_fg, end_fg = 2.00, 1.50
    cogs = cogm + begin_fg - end_fg
    print("prime: %.2f  conversion: %.2f  mfg cost: %.2f" % (prime, conversion, mfg))
    print("COGM: %.2f  COGS: %.2f" % (cogm, cogs))
    assert 6.99 < prime < 7.01
    assert 6.29 < conversion < 6.31
    assert 10.49 < mfg < 10.51
    assert 10.99 < cogm < 11.01
    assert 11.49 < cogs < 11.51
    print("rule: every rung answers one question - skip none")
    print("OK: %s climbed the stack" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_mfg_cogs_unit(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # unit cost from production, COGS from sales - siblings, not twins
    total_mfg, produced = 105000.0, 10000
    unit = total_mfg / produced
    sold = 9000
    cogs = sold * unit
    ending_fg = (produced - sold) * unit
    print("unit cost: %.2f" % unit)
    print("COGS on 9,000 sold: %.2f" % cogs)
    print("finished goods on shelf: %.2f" % ending_fg)
    assert 10.49 < unit < 10.51
    assert 94499 < cogs < 94501
    assert 10499 < ending_fg < 10501
    print("rule: cost follows units made; expense follows units sold")
    print("OK: %s separated the siblings" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_mfg_landed_cost(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # landed cost: the quote is a photograph, the dock is the real thing
    fob, freight, insurance = 10000.0, 1800.0, 150.0
    duty_rate = 0.12
    duty = fob * duty_rate
    units = 5000
    landed = fob + freight + insurance + duty
    per_unit = landed / units
    fob_unit = fob / units
    uplift = (per_unit - fob_unit) / fob_unit * 100.0
    print("duty: %.2f" % duty)
    print("landed total: %.2f" % landed)
    print("FOB unit: %.2f  landed unit: %.2f" % (fob_unit, per_unit))
    print("quote understated reality by %.1f %%" % uplift)
    assert 1199 < duty < 1201
    assert 13149 < landed < 13151
    assert 2.62 < per_unit < 2.64
    assert 31.4 < uplift < 31.6
    print("rule: compare domestic price to foreign LANDED cost, never to FOB")
    print("OK: %s landed the shipment" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_mfg_quotation(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # effective unit cost at YOUR volume: unit price plus amortized tooling
    unit_price, nre, moq = 2.40, 6000.0, 2000
    eff_moq = unit_price + nre / moq
    eff_vol = unit_price + nre / 10000.0
    print("effective at MOQ 2,000: %.2f" % eff_moq)
    print("effective at 10,000: %.2f" % eff_vol)
    assert 5.39 < eff_moq < 5.41
    assert 2.99 < eff_vol < 3.01
    print("rule: the quantity you buy decides which cost is real")
    print("OK: %s read the fine print" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_mfg_make_buy_intro(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # first-pass make vs buy: avoidable cost only, sunk cost stays out
    avoidable = 3.00 + 1.50 + 0.75
    buy_price = 5.80
    saving = buy_price - avoidable
    print("avoidable make cost: %.2f  buy price: %.2f" % (avoidable, buy_price))
    print("make saves per unit: %.2f" % saving)
    assert 5.24 < avoidable < 5.26
    assert 0.54 < saving < 0.56
    # the trap: counting allocated fixed overhead that never leaves
    fixed_alloc = 40000.0 / 10000.0
    trap_make = avoidable + fixed_alloc
    print("trap version (fixed alloc added): %.2f - would flip the answer" % trap_make)
    assert 9.24 < trap_make < 9.26
    print("rule: compare the buy price only to costs that actually vanish")
    print("OK: %s asked the first question" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_mfg_bom_rollup(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # bottom-up roll-up through the subassembly level
    sub_material = 2 * 1.10 + 4 * 0.04
    sub_labor = 0.40
    sub_cost = sub_material + sub_labor
    top = sub_cost + 2.30 + 0.35 + 0.05
    print("subassembly: material %.2f + labor %.2f = %.2f" % (sub_material, sub_labor, sub_cost))
    print("top-level material roll-up: %.2f" % top)
    assert 2.35 < sub_material < 2.37
    assert 2.75 < sub_cost < 2.77
    assert 5.45 < top < 5.47
    # scrap compounding across levels
    levels, rate = 3, 0.02
    compound = 1 - (1 - rate) ** levels
    print("2%% scrap at 3 levels compounds to %.2f %%" % (compound * 100))
    assert 0.058 < compound < 0.060
    print("rule: explode every level, and let scrap compound honestly")
    print("OK: %s climbed the tree" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_mfg_labor_standards(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # earned hours vs actual hours: the efficiency verdict
    standard = 0.10
    units = 480
    earned = units * standard
    actual = 52.0
    efficiency = earned / actual * 100.0
    gap = actual - earned
    print("earned hours: %.1f  actual: %.1f" % (earned, actual))
    print("efficiency: %.1f %%" % efficiency)
    print("hour gap: %.1f" % gap)
    assert 47.9 < earned < 48.1
    assert 92.2 < efficiency < 92.4
    assert 3.9 < gap < 4.1
    print("rule: one number prices the quote, paces the floor, and writes the variance")
    print("OK: %s timed the work" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_mfg_machine_hour_rate(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the machining center's annual hunger, divided by honest hours
    pool = 120000 + 45000 + 30000 + 95000 + 60000 + 130000
    hours = 2000.0
    rate = pool / hours
    job_time = 0.25
    job_cost = rate * job_time
    print("annual pool: %d" % pool)
    print("machine rate: %.2f $/hr" % rate)
    print("0.25-hr job absorbs: %.2f" % job_cost)
    assert pool == 480000
    assert 239.99 < rate < 240.01
    assert 59.99 < job_cost < 60.01
    print("rule: fantasy hours make fantasy rates - count productive time only")
    print("OK: %s rated the machine" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_mfg_tooling_nre(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # one tool, two forecasts: the denominator decides
    tool = 80000.0
    adder_hi = tool / 200000.0
    adder_lo = tool / 50000.0
    print("tooling per part at 200,000: %.2f" % adder_hi)
    print("tooling per part at 50,000: %.2f" % adder_lo)
    assert 0.39 < adder_hi < 0.41
    assert 1.59 < adder_lo < 1.61
    ratio = adder_lo / adder_hi
    print("low volume costs %.0fx per unit in tooling" % ratio)
    assert 3.99 < ratio < 4.01
    print("rule: amortize over volume you believe, not volume you wish")
    print("OK: %s harvested the tool" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_mfg_injection_molding(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # press rate over cycle math, plus resin by weight
    press_rate, cycle_s, cavities = 45.0, 24.0, 2
    parts_per_hour = cavities * 3600.0 / cycle_s
    machine_per_part = press_rate / parts_per_hour
    resin_kg, resin_price = 0.04, 3.20
    resin_per_part = resin_kg * resin_price
    part = machine_per_part + resin_per_part
    print("parts per hour: %.0f" % parts_per_hour)
    print("machine per part: %.3f  resin per part: %.3f" % (machine_per_part, resin_per_part))
    print("part cost before tooling: %.3f" % part)
    assert 299 < parts_per_hour < 301
    assert 0.149 < machine_per_part < 0.151
    assert 0.127 < resin_per_part < 0.129
    assert 0.277 < part < 0.279
    print("rule: cycle, cavities, weight, volume - four chambers, four levers")
    print("OK: %s shot the mold math" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_mfg_machining(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # setup spread over the batch plus cycle at the machine rate
    rate = 85.0
    setup_cost = 45.0 / 60.0 * rate
    batch = 200
    run_cost = batch * 3.2 / 60.0 * rate
    total = setup_cost + run_cost
    per_part = total / batch
    setup_share = setup_cost / total * 100.0
    print("setup: %.2f  run: %.2f  batch total: %.2f" % (setup_cost, run_cost, total))
    print("per part: %.2f (setup is %.1f %% of it)" % (per_part, setup_share))
    assert 63.74 < setup_cost < 63.76
    assert 906.66 < run_cost < 906.68
    assert 4.84 < per_part < 4.86
    assert 6.5 < setup_share < 6.6
    print("rule: batch size is the denominator that decides everything")
    print("OK: %s cut the chips" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_mfg_electronics_assembly(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # five layers of board cost before components
    bare = 1.80
    smt = 42 * 0.012
    pth = 6 * 0.08
    test = 0.35
    total = bare + smt + pth + test
    print("bare %.2f + SMT %.3f + PTH %.2f + test %.2f" % (bare, smt, pth, test))
    print("assembly stack: %.2f" % total)
    assert 0.503 < smt < 0.505
    assert 0.479 < pth < 0.481
    assert 3.12 < total < 3.15
    # yield inflates the cost per GOOD board
    fpy = 0.97
    effective = total / fpy
    print("at 97%% first-pass yield, effective: %.2f" % effective)
    assert 3.22 < effective < 3.24
    print("rule: count placements, joints, and test - then divide by yield")
    print("OK: %s populated the board" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_mfg_yield_scrap(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the process tax: input plus rework, divided by good units
    input_cost, fpy = 10.00, 0.96
    rework_rate, rework_cost = 0.03, 1.50
    effective = (input_cost + rework_rate * rework_cost) / fpy
    tax = (effective - input_cost) / input_cost * 100.0
    print("effective cost per good unit: %.2f" % effective)
    print("yield tax: %.1f %%" % tax)
    assert 10.45 < effective < 10.47
    assert 4.5 < tax < 4.7
    print("rule: late defects are the most expensive - catch them early")
    print("OK: %s priced the tax" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_mfg_scale(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # Wright's 80 percent learning curve across doublings
    first, rate = 10.0, 0.80
    units = [1, 2, 4, 8]
    times = [first * (u ** (math.log(rate) / math.log(2))) for u in units]
    for u, t in zip(units, times):
        print("unit %d: %.2f hours" % (u, t))
    assert 9.99 < times[0] < 10.01
    assert 7.99 < times[1] < 8.01
    assert 6.39 < times[2] < 6.41
    assert 5.11 < times[3] < 5.13
    print("rule: steepest early - prototypes are brutal, maturity is cheap")
    print("OK: %s rode the curve" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_mfg_abc(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # peanut-butter vs activity-based: who really pays for setups
    pool, total_dlh = 200000.0, 10000.0
    trad_rate = pool / total_dlh
    a_trad, b_trad = 8000 * trad_rate, 2000 * trad_rate
    setup_pool, setups = 80000.0, 100
    setup_rate = setup_pool / setups
    rest_pool, rest_rate = pool - setup_pool, (pool - setup_pool) / total_dlh
    a_abc = 20 * setup_rate + 8000 * rest_rate
    b_abc = 80 * setup_rate + 2000 * rest_rate
    print("traditional: A %.0f  B %.0f" % (a_trad, b_trad))
    print("ABC:         A %.0f  B %.0f" % (a_abc, b_abc))
    print("B was subsidized by %.0f" % (b_abc - b_trad))
    assert 159999 < a_trad < 160001
    assert 39999 < b_trad < 40001
    assert 111999 < a_abc < 112001
    assert 87999 < b_abc < 88001
    assert 47999 < (b_abc - b_trad) < 48001
    print("rule: activities cause cost - trace them, do not spread them")
    print("OK: %s unmasked the subsidy" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_mfg_should_cost(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # bracket should-cost from markets and standards vs the quote
    material = 0.5 * 3.00
    process = 0.5 / 60.0 * 90.0
    labor, overhead = 0.45, 0.60
    factory = material + process + labor + overhead
    should = factory * 1.12
    quote = 4.10
    gap = (quote - should) / quote * 100.0
    print("factory cost: %.2f  should-cost: %.2f  quote: %.2f" % (factory, should, quote))
    print("gap: %.1f %%" % gap)
    assert 3.29 < factory < 3.31
    assert 3.69 < should < 3.71
    assert 9.7 < gap < 9.9
    print("rule: build the price from physics and markets, then ask about the gap")
    print("OK: %s built the should" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_mfg_target_cost(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # backwards from the shelf: price minus margins equals the design budget
    retail = 49.99
    wholesale = retail * 0.50
    target = wholesale * (1 - 0.35)
    print("retail %.2f -> wholesale %.2f -> factory target %.2f" % (retail, wholesale, target))
    assert 24.99 < wholesale < 25.01
    assert 16.24 < target < 16.26
    # decompose to three subsystems by function weight
    weights = {"power": 0.40, "housing": 0.35, "electronics": 0.25}
    for k, w in weights.items():
        sub = target * w
        print("  %-11s target: %.2f" % (k, sub))
    assert 6.49 < target * 0.40 < 6.51
    print("rule: the market sets the price - design fits what is left")
    print("OK: %s aimed backwards" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_mfg_margin_math(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # markup vs margin on the factory -> wholesale -> retail chain
    cost, wholesale, retail = 10.50, 18.00, 36.00
    markup_w = (wholesale - cost) / cost * 100.0
    margin_w = (wholesale - cost) / wholesale * 100.0
    margin_r = (retail - wholesale) / retail * 100.0
    print("wholesale markup: %.1f %%  wholesale margin: %.1f %%" % (markup_w, margin_w))
    print("retail margin: %.1f %%" % margin_r)
    assert 71.3 < markup_w < 71.5
    assert 41.6 < margin_w < 41.8
    assert 49.9 < margin_r < 50.1
    # conversion check: 50 percent margin == 100 percent markup
    m = 0.50
    equiv_markup = m / (1 - m) * 100.0
    print("50%% margin converts to %.0f%% markup" % equiv_markup)
    assert 99.9 < equiv_markup < 100.1
    print("rule: markup over cost, margin over price - never mix the denominators")
    print("OK: %s walked the chain" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_mfg_breakeven(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # contribution margin aims at the fixed mountain
    price, variable = 25.00, 16.25
    cm = price - variable
    fixed = 87500.0
    be_units = fixed / cm
    be_revenue = fixed / (cm / price)
    print("contribution per unit: %.2f" % cm)
    print("break-even: %.0f units / %.0f dollars" % (be_units, be_revenue))
    assert 8.74 < cm < 8.76
    assert 9999 < be_units < 10001
    assert 249999 < be_revenue < 250001
    # the 10,001st unit
    profit_one_more = cm
    print("unit 10,001 profit: %.2f" % profit_one_more)
    assert 8.74 < profit_one_more < 8.76
    print("rule: fixed costs are the mountain - contribution is the shovel")
    print("OK: %s found the line" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_mfg_make_buy_tco(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # full owned cost of each option at 50,000 units
    vol = 50000
    make = 5.25 * vol + 40000.0
    buy = 5.80 * vol + 12500.0 + 5000.0 + 8000.0
    diff = buy - make
    print("make total: %.0f  buy total: %.0f" % (make, buy))
    print("making wins by %.0f" % diff)
    assert 302499 < make < 302501
    assert 315499 < buy < 315501
    assert 12999 < diff < 13001
    # crossover: at what buy price would the verdict flip
    flip_price = (make - 12500.0 - 5000.0 - 8000.0) / vol
    print("buy price that flips it: %.2f" % flip_price)
    assert 5.53 < flip_price < 5.55
    print("rule: the cheapest quote is rarely the cheapest decision")
    print("OK: %s owned the total" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_mfg_parametric(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # CER: cost = 120 * weight^0.8 fitted on enclosure history
    a, b = 120.0, 0.8
    w = 5.0
    est = a * (w ** b)
    print("5 kg enclosure estimates at %.2f" % est)
    assert 434.8 < est < 435.0
    # scale effect visible: doubling weight less than doubles cost
    est10 = a * (10.0 ** b)
    ratio = est10 / est
    print("10 kg estimates at %.2f (ratio %.3f, not 2.0)" % (est10, ratio))
    assert 1.740 < ratio < 1.742
    print("rule: a CER is a statistical promise - report the interval, respect the range")
    print("OK: %s fit the curve" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_mfg_quality_cost(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # Juran's four buckets on one plant's year
    prevention, appraisal = 20000.0, 35000.0
    internal, external = 60000.0, 120000.0
    copq = prevention + appraisal + internal + external
    sales = 4700000.0
    pct = copq / sales * 100.0
    failure_share = (internal + external) / copq * 100.0
    print("cost of poor quality: %.0f (%.1f %% of sales)" % (copq, pct))
    print("failure share of quality spend: %.1f %%" % failure_share)
    assert 234999 < copq < 235001
    assert 4.99 < pct < 5.01
    assert 76.5 < failure_share < 76.7
    print("rule: move dollars from failure to prevention - they return severalfold")
    print("OK: %s priced the pain" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_mfg_lifecycle(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the 85,000 machine and its ten-year appetite
    price = 85000.0
    annual = 6000.0 + 9000.0 + 40000.0
    years = 10
    disposal, salvage = 5000.0, 8000.0
    lcc = price + annual * years + disposal - salvage
    price_share = price / lcc * 100.0
    print("lifecycle cost: %.0f" % lcc)
    print("purchase price was %.1f %% of the real number" % price_share)
    assert 631999 < lcc < 632001
    assert 13.4 < price_share < 13.5
    print("rule: the price is the cover charge - cost the whole evening")
    print("OK: %s lived the decade" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_mfg_transfer_pricing(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # cost-plus transfer: where the profit appears is a choice
    cost, markup = 10.50, 0.15
    transfer = cost * (1 + markup)
    seller_profit = transfer - cost
    print("transfer price: %.2f  seller profit per unit: %.2f" % (transfer, seller_profit))
    assert 12.07 < transfer < 12.09
    assert 1.57 < seller_profit < 1.59
    # buyer perspective at 20,000 units
    buyer_material = transfer * 20000
    print("buyer books %.0f of material on 20,000 units" % buyer_material)
    assert 241499 < buyer_material < 241501
    print("rule: document it like a customer price - the auditors will read it")
    print("OK: %s moved the profit honestly" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_mfg_dfm_cost(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # part-count attack: insertion cost before and after integration
    insert = 0.35
    before, after = 24, 14
    cost_before, cost_after = before * insert, after * insert
    saved = cost_before - cost_after
    print("assembly cost: %.2f -> %.2f, saved %.2f per unit" % (cost_before, cost_after, saved))
    assert 8.39 < cost_before < 8.41
    assert 4.89 < cost_after < 4.91
    assert 3.49 < saved < 3.51
    # at 100,000 units a year
    annual = saved * 100000
    print("at 100,000 units: %.0f a year freed" % annual)
    assert 349999 < annual < 350001
    print("rule: cost is born at the drawing board - attack it there")
    print("OK: %s designed the cost out" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_mfg_disruption_cost(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # expected disruption loss vs the price of resilience
    prob, consequence = 0.08, 250000.0
    expected = prob * consequence
    resilience = 12000.0
    net = expected - resilience
    print("expected annual disruption cost: %.0f" % expected)
    print("dual-source resilience: %.0f  net benefit: %.0f" % (resilience, net))
    assert 19999 < expected < 20001
    assert 7999 < net < 8001
    print("rule: price the breakage, then buy resilience where it pays")
    print("OK: %s insured the chain" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_mfg_compliance_cost(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the regulation layer, per unit
    annual = 96000.0
    volume = 240000
    per_unit = annual / volume
    print("compliance per unit: %.2f" % per_unit)
    assert 0.39 < per_unit < 0.41
    # design lever: substance-free material deletes a 18,000 test program
    test_program = 18000.0
    new_per_unit = (annual - test_program) / volume
    print("after designing out the test program: %.3f" % new_per_unit)
    assert 0.324 < new_per_unit < 0.326
    print("rule: measure the layer, allocate by driver, design it down")
    print("OK: %s counted the rules" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_mfg_twenty_cent(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the 200-to-1 lesson: factory cost inside the selling price
    factory, price = 0.20, 40.00
    ratio = price / factory
    share = factory / price * 100.0
    print("price-to-cost ratio: %.0f to 1" % ratio)
    print("factory cost is %.2f %% of the price" % share)
    assert 199 < ratio < 201
    assert 0.49 < share < 0.51
    # scale power: two cents saved at a million units
    saving = 0.02 * 1000000
    print("0.02 saved at 1,000,000 units: %.0f" % saving)
    assert 19999 < saving < 20001
    # stack check: logistics slice of one example
    logistics = 1.80
    print("logistics slice: %.2f (%.1f %%)" % (logistics, logistics / price * 100))
    assert 4.4 < logistics / price * 100 < 4.6
    print("rule: know your 0.20, price your 40 - never confuse the two")
    print("OK: %s learned the lesson" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_mfg_cost_audit(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # teardown repricing vs the claimed material cost
    parts = [1.20, 0.85, 0.95, 0.60, 0.45, 0.38, 0.52, 0.30, 0.28, 0.35, 0.27, 0.25]
    assert len(parts) == 12
    teardown = sum(parts)
    claimed = 8.90
    variance = claimed - teardown
    pct = variance / claimed * 100.0
    print("teardown total: %.2f  claimed: %.2f" % (teardown, claimed))
    print("variance: %.2f (%.1f %%)" % (variance, pct))
    assert 6.39 < teardown < 6.41
    assert 2.49 < variance < 2.51
    assert 27.9 < pct < 28.1
    print("rule: verify from an independent source - unchecked costs drift")
    print("OK: %s made the number confess" % NAME)
if __name__ == "__main__":
    main()
''')


DEMOS = {
    "what_is": demo_mfg_what_is,
    "bom": demo_mfg_bom,
    "material_cost": demo_mfg_material_cost,
    "labor_cost": demo_mfg_labor_cost,
    "overhead_intro": demo_mfg_overhead_intro,
    "cost_stack": demo_mfg_cost_stack,
    "cogs_unit": demo_mfg_cogs_unit,
    "landed_cost": demo_mfg_landed_cost,
    "quotation": demo_mfg_quotation,
    "make_buy_intro": demo_mfg_make_buy_intro,
    "bom_rollup": demo_mfg_bom_rollup,
    "labor_standards": demo_mfg_labor_standards,
    "machine_hour_rate": demo_mfg_machine_hour_rate,
    "tooling_nre": demo_mfg_tooling_nre,
    "injection_molding": demo_mfg_injection_molding,
    "machining": demo_mfg_machining,
    "electronics_assembly": demo_mfg_electronics_assembly,
    "yield_scrap": demo_mfg_yield_scrap,
    "scale": demo_mfg_scale,
    "abc": demo_mfg_abc,
    "should_cost": demo_mfg_should_cost,
    "target_cost": demo_mfg_target_cost,
    "margin_math": demo_mfg_margin_math,
    "breakeven": demo_mfg_breakeven,
    "make_buy_tco": demo_mfg_make_buy_tco,
    "parametric": demo_mfg_parametric,
    "quality_cost": demo_mfg_quality_cost,
    "lifecycle": demo_mfg_lifecycle,
    "transfer_pricing": demo_mfg_transfer_pricing,
    "dfm_cost": demo_mfg_dfm_cost,
    "disruption_cost": demo_mfg_disruption_cost,
    "compliance_cost": demo_mfg_compliance_cost,
    "twenty_cent": demo_mfg_twenty_cent,
    "cost_audit": demo_mfg_cost_audit,
}
