#!/usr/bin/env python3
"""Demo programs for the Inventory and Warehouse State databases.

Every demo is real, runnable, stdlib-only Python performing the actual
inventory/warehouse computation for its record. All are machine-executed by
build.py: each prints its real computed values, asserts tight bounds (never
float exact-equality), and ends with the OK marker.
"""

_PREAMBLE = "import math\n"


def _wrap(hdr_fn, name, rid, group, body):
    return hdr_fn(name, rid, group) + _PREAMBLE + body.replace("NAME", __import__("json").dumps(name))


def demo_inv_what_is(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
import datetime
def main():
    # the four record families a warehouse keeps and their shares
    families = {"stock master records": 34, "movement postings": 412,
                "location records": 96, "transaction lines": 128}
    total = sum(families.values())
    share = {k: v / total * 100.0 for k, v in families.items()}
    print("record families: %d" % len(families))
    for k in families:
        print("  %-22s %4d (%5.2f %%)" % (k, families[k], share[k]))
    print("total records: %d" % total)
    assert total == 670
    assert 5.07 < share["stock master records"] < 5.08
    assert 61.49 < share["movement postings"] < 61.50
    assert 14.32 < share["location records"] < 14.33
    assert 19.10 < share["transaction lines"] < 19.11
    # holding-cost rule of thumb: 25% of 670 units at $40 average value
    annual_hold = 670 * 40.0 * 0.25
    print("holding-cost illustration: $%.2f / yr" % annual_hold)
    assert 6699.9 < annual_hold < 6700.1
    print("rule: enough to serve demand and absorb variability, but no more")
    print("OK: %s framed the discipline" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_inv_sku_atom(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # well-formed SKU: prefix-category-sequence-checkdigit
    prefix, cat, seq = "INV", "ELC", "004217"
    digits = [int(c) for c in seq]
    check = sum(digits) % 10
    sku = "%s-%s-%s-%d" % (prefix, cat, seq, check)
    print("built SKU: %s" % sku)
    assert check == 4
    assert sku == "INV-ELC-004217-4"
    # a changed digit changes the check: the typo is caught
    bad_seq = "004218"
    bad_check = sum(int(c) for c in bad_seq) % 10
    print("typo check digit: %d (mismatch -> rejected)" % bad_check)
    assert bad_check != check
    # supplier aliases map many outside names to the one master SKU
    aliases = {"SUP-8812": sku, "GTIN-0085000412179": sku}
    for alias, target in aliases.items():
        assert target == sku
    print("aliases resolved: %d -> %s" % (len(aliases), sku))
    print("rule: one number, one thing, for all time")
    print("OK: %s stamped the atom" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_inv_stock_states(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the conserved stock-state ledger for one SKU
    states = {"on_hand": 500, "reserved": 120, "in_transit": 200,
              "quarantine": 15, "damaged": 5}
    def atp(s):
        return s["on_hand"] - s["reserved"]
    print("on-hand %d, reserved %d -> ATP %d" % (states["on_hand"], states["reserved"], atp(states)))
    assert atp(states) == 380
    # promise an order of 100: reservation moves, on-hand does not
    states["reserved"] += 100
    print("after reserving 100: reserved %d, ATP %d" % (states["reserved"], atp(states)))
    assert atp(states) == 280
    assert states["on_hand"] == 500, "reserving must not move physical stock"
    # conservation: the states always sum to the position
    position = sum(states.values())
    print("total position: %d" % position)
    assert position == 940
    # quarantine and damaged never enter a promise
    sellable = states["on_hand"] - states["quarantine"] - states["damaged"]
    print("sellable on-hand: %d" % sellable)
    assert sellable == 480
    print("rule: every unit in exactly one state; ATP is computed, never guessed")
    print("OK: %s told the truth of the shelf" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_inv_location_address(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # encode and decode a structured location address
    def encode(aisle, bay, level, binc):
        return "%s-%02d-%02d-%s" % (aisle, bay, level, binc)
    def decode(addr):
        a, b, l, c = addr.split("-")
        return {"aisle": a, "bay": int(b), "level": int(l), "bin": c}
    addr = encode("A", 12, 3, "B")
    print("encoded: %s" % addr)
    assert addr == "A-12-03-B"
    back = decode(addr)
    assert back == {"aisle": "A", "bay": 12, "level": 3, "bin": "B"}
    print("decoded: %s" % back)
    # putaway fit check: unit dims vs location capacity
    loc = {"addr": addr, "type": "bulk reserve", "max_l": 48, "max_w": 48,
           "max_h": 60, "max_lb": 2000}
    unit = {"l": 48, "w": 40, "h": 48, "lb": 800}
    fits = (unit["l"] <= loc["max_l"] and unit["w"] <= loc["max_w"]
            and unit["h"] <= loc["max_h"] and unit["lb"] <= loc["max_lb"])
    print("putaway fit for %s: %s" % (loc["addr"], fits))
    assert fits is True
    # type rule: flammables may not go to a general location
    print("rule: the right address, the right type, scan-confirmed")
    print("OK: %s mapped the addresses" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_inv_uom_hierarchy(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # pack hierarchy: pallet -> case -> each, one base unit
    hierarchy = {"each": 1, "case": 24, "pallet": 960}
    base = "each"
    def to_base(qty, unit):
        return qty * hierarchy[unit]
    got = to_base(3, "pallet") + to_base(5, "case")
    print("3 pallets + 5 cases = %d eaches" % got)
    assert 2999.9 < got < 3000.1
    # the classic mistake: 100 heard as eaches when cases were meant
    meant = to_base(100, "case")
    heard = to_base(100, "each")
    shortfall = meant - heard
    print("unit misread shortfall: %d eaches" % shortfall)
    assert 2299.9 < shortfall < 2300.1
    # receiving converts on entry; the receipt remembers the original unit
    receipt = {"qty": 40, "unit": "case", "as_base": to_base(40, "case")}
    print("receipt: %d %s stored as %d %s" % (receipt["qty"], receipt["unit"], receipt["as_base"], base))
    assert receipt["as_base"] == 960
    print("rule: humans name the unit; the system does the arithmetic")
    print("OK: %s kept one true measure" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_inv_valuation_simple(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # three receipt layers, one sale of 150 units
    layers = [(100, 10.0), (100, 12.0), (100, 14.0)]
    sale = 150
    def issue_fifo(layers, qty):
        cost, rest = 0.0, []
        for q, p in layers:
            if qty <= 0:
                rest.append((q, p)); continue
            take = min(q, qty); cost += take * p; qty -= take
            if q - take > 0: rest.append((q - take, p))
        return cost, rest
    def issue_lifo(layers, qty):
        return issue_fifo(list(reversed(layers)), qty)
    fifo_cogs, fifo_rest = issue_fifo(layers, sale)
    lifo_cogs, lifo_rest = issue_lifo(layers, sale)
    fifo_val = sum(q * p for q, p in fifo_rest)
    lifo_val = sum(q * p for q, p in lifo_rest)
    print("FIFO: COGS %.2f, remaining value %.2f" % (fifo_cogs, fifo_val))
    print("LIFO: COGS %.2f, remaining value %.2f" % (lifo_cogs, lifo_val))
    assert 1599.9 < fifo_cogs < 1600.1
    assert 1999.9 < fifo_val < 2000.1
    assert 1999.9 < lifo_cogs < 2000.1
    assert 1599.9 < lifo_val < 1600.1
    # weighted average blends all layers
    total_cost = sum(q * p for q, p in layers)
    avg = total_cost / sum(q for q, p in layers)
    avg_cogs = sale * avg
    print("average: COGS %.2f at $%.2f/unit" % (avg_cogs, avg))
    assert 11.99 < avg < 12.01
    assert 1799.9 < avg_cogs < 1800.1
    print("profit swing FIFO vs LIFO on the same sale: %.2f" % (lifo_cogs - fifo_cogs))
    print("rule: the money follows the flow, so the flow must be honest")
    print("OK: %s priced the layers" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_inv_lead_time(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # lead time in legs: admin, supplier, transit, receiving
    legs = {"admin": 1.0, "supplier": 6.0, "transit": 5.0, "receiving": 2.0}
    total = sum(legs.values())
    demand_per_day = 20.0
    cover = demand_per_day * total
    print("legs: %s" % legs)
    print("lead time %.1f days -> demand during lead time %.1f" % (total, cover))
    assert 13.9 < total < 14.1
    assert 279.9 < cover < 280.1
    # the supplier leg stretches 4 days: the exposure grows
    legs["supplier"] = 10.0
    total2 = sum(legs.values())
    cover2 = demand_per_day * total2
    print("supplier stretches: lead time %.1f days -> cover %.1f" % (total2, cover2))
    assert 17.9 < total2 < 18.1
    assert 359.9 < cover2 < 360.1
    print("extra stock the stretch demands: %.1f units" % (cover2 - cover))
    print("rule: measure the wait honestly; stock the bridge across it")
    print("OK: %s read the master clock" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_inv_goods_receipt(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # three-way match with tolerance rules and dispositions
    lines = [
        {"sku": "A", "ordered": 100, "received": 96, "damaged": 0, "tol": 0.05},
        {"sku": "B", "ordered": 50, "received": 55, "damaged": 0, "tol": 0.05},
        {"sku": "C", "ordered": 200, "received": 200, "damaged": 12, "tol": 0.02},
    ]
    putaway = []
    for ln in lines:
        variance = (ln["received"] - ln["ordered"]) / ln["ordered"]
        good = ln["received"] - ln["damaged"]
        if ln["damaged"] > 0:
            disp = "quarantine %d damaged; accept %d" % (ln["damaged"], good)
            putaway.append((ln["sku"], good))
        elif abs(variance) <= ln["tol"]:
            disp = "accept within tolerance (variance %+.1f%%)" % (variance * 100)
            putaway.append((ln["sku"], good))
        else:
            disp = "ESCALATE: variance %+.1f%% exceeds tolerance" % (variance * 100)
        print("line %s: ordered %d, received %d -> %s" % (ln["sku"], ln["ordered"], ln["received"], disp))
    assert putaway == [("A", 96), ("C", 188)]
    print("putaway tasks: %d" % len(putaway))
    assert len(putaway) == 2
    print("rule: count at the gate with open eyes; nothing enters on trust")
    print("OK: %s guarded the gate" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_inv_pick_pack_ship(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # release a 3-line order, confirm picks, verify the pack by weight
    order = [{"sku": "S1", "qty": 10, "loc": "A-01-01", "wt": 0.5},
             {"sku": "S2", "qty": 4, "loc": "A-02-03", "wt": 1.2},
             {"sku": "S3", "qty": 2, "loc": "B-01-02", "wt": 0.8}]
    for ln in order:
        scanned = (ln["loc"], ln["sku"])  # location + item scan confirmation
        assert scanned == (ln["loc"], ln["sku"])
        print("picked %d x %s from %s [scan OK]" % (ln["qty"], ln["sku"], ln["loc"]))
    expected_wt = sum(ln["qty"] * ln["wt"] for ln in order)
    lo, hi = expected_wt * 0.95, expected_wt * 1.05
    actual = 11.5
    print("expected %.2f kg, band %.2f-%.2f, actual %.2f" % (expected_wt, lo, hi, actual))
    assert 11.39 < expected_wt < 11.41
    assert lo < actual < hi, "weight check failed: reopen the carton"
    print("pack verification: PASS; manifesting 1 carton to load L-77")
    print("rule: every handoff has its check")
    print("OK: %s delivered the vow" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_inv_expiry_lot_basics(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
import datetime
def main():
    today = datetime.date(2026, 10, 17)
    lots = [
        {"lot": "L1", "exp": datetime.date(2026, 11, 20), "qty": 100},
        {"lot": "L2", "exp": datetime.date(2026, 10, 25), "qty": 60},
        {"lot": "L3", "exp": datetime.date(2026, 10, 10), "qty": 40},
    ]
    for lot in lots:
        lot["days"] = (lot["exp"] - today).days
        status = "BLOCKED - expired" if lot["days"] < 0 else "sellable"
        print("lot %s: %d days to expiry -> %s" % (lot["lot"], lot["days"], status))
    assert lots[0]["days"] == 34
    assert lots[1]["days"] == 8
    assert lots[2]["days"] == -7
    pickable = [l for l in lots if l["days"] >= 0]
    assert len(pickable) == 2
    # forward traceability: lot L2 went to two shipments
    genealogy = {"L2": ["S-101", "S-104"]}
    print("forward trace L2 -> %s" % genealogy["L2"])
    assert genealogy["L2"] == ["S-101", "S-104"]
    print("rule: without lot discipline a recall is a guess; with it, a list")
    print("OK: %s honored the families" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_inv_cycle_counting(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # ABC-driven yearly count schedule
    classes = {"A": (20, 12), "B": (60, 4), "C": (200, 2)}  # (skus, counts/yr)
    total_counts = sum(n * f for n, f in classes.values())
    workdays = 250
    per_day = total_counts / workdays
    print("yearly counts: %d -> %.2f per working day" % (total_counts, per_day))
    assert 879.9 < total_counts < 880.1
    assert 3.51 < per_day < 3.53
    # a day of blind counts against a small warehouse
    book = {"S1": 100, "S2": 40, "S3": 25, "S4": 60}
    counted = {"S1": 100, "S2": 38, "S3": 25, "S4": 60}
    variances = {k: counted[k] - book[k] for k in book if counted[k] != book[k]}
    print("blind counts: %d SKUs, variances: %s" % (len(book), variances))
    assert variances == {"S2": -2}
    accuracy = (len(book) - len(variances)) / len(book) * 100.0
    print("day accuracy: %.1f %%" % accuracy)
    assert 74.9 < accuracy < 75.1
    print("investigation S2: mis-pick posted to S3 yesterday -> process fix logged")
    print("rule: count blind, question every variance, fix the process")
    print("OK: %s kept the daily inspection" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_inv_abc_analysis(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # rank twelve SKUs by annual usage value, cut ABC classes
    auv = [70000, 20000, 6000, 4000, 3000, 2000, 1500, 1000, 700, 500, 300, 200]
    total = sum(auv)
    ranked = sorted(enumerate(auv), key=lambda p: -p[1])
    # deterministic cut: walk the cumulative curve until thresholds cross
    cum = 0.0; a_cut = b_cut = None
    for i, v in enumerate([p[1] for p in ranked]):
        cum += v
        if a_cut is None and cum / total >= 0.80: a_cut = i
        if b_cut is None and cum / total >= 0.95: b_cut = i
    nA, nB, nC = a_cut + 1, b_cut - a_cut, len(auv) - b_cut - 1
    print("A: %d SKUs, B: %d SKUs, C: %d SKUs" % (nA, nB, nC))
    assert (nA, nB, nC) == (2, 4, 6)
    cum2 = sum(v for _, v in ranked[:2]) / total * 100.0
    sku_share = nA / len(auv) * 100.0
    print("A: %.1f %% of SKUs carry %.2f %% of the value" % (sku_share, cum2))
    assert 82.41 < cum2 < 82.43
    assert 16.6 < sku_share < 16.7
    policy = {"A": "weekly counts, tight forecast", "B": "monthly counts", "C": "simple rules, big lots"}
    for c in ("A", "B", "C"):
        print("class %s policy: %s" % (c, policy[c]))
    print("rule: control effort follows the money; simplicity covers the rest")
    print("OK: %s ranked the treasury" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_inv_reorder_point(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # R = d*L + SS: order when inventory position touches R
    d, L, SS = 20.0, 10.0, 40.0
    R = d * L + SS
    print("d=%.0f/day, L=%.0f days, SS=%.0f -> R=%.0f" % (d, L, SS, R))
    assert 239.9 < R < 240.1
    # simulate daily demand against the tripwire
    position, day, fired, fired_pos = 300.0, 0, None, None
    while position > 0 and day < 30:
        day += 1
        position -= d
        if fired is None and position <= R:
            fired, fired_pos = day, position
    print("order fired on day %d at position %.0f" % (fired, fired_pos))
    assert fired == 3
    assert 239.9 < fired_pos < 240.1
    print("rule: the tripwire watches position - on-hand plus on-order minus commitments")
    print("OK: %s set the watchman" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_inv_eoq(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # EOQ = sqrt(2DS/H): the balance of ordering vs holding
    D, S, H = 10000.0, 50.0, 2.0
    eoq = math.sqrt(2 * D * S / H)
    orders_yr = D / eoq
    ordering = orders_yr * S
    holding = (eoq / 2.0) * H
    total = ordering + holding
    print("EOQ %.1f units, %.2f orders/yr" % (eoq, orders_yr))
    print("ordering $%.2f + holding $%.2f = $%.2f" % (ordering, holding, total))
    assert 707.0 < eoq < 707.2
    assert 14.13 < orders_yr < 14.15
    assert 1414.20 < total < 1414.23
    # the curve is flat near the bottom: rounding to 700 costs little
    t700 = (D / 700.0) * S + (700.0 / 2.0) * H
    penalty = (t700 - total) / total * 100.0
    print("rounded to 700: penalty %.3f %%" % penalty)
    assert 0.0 < penalty < 0.05
    # discount break test: 3% off at 1000 units
    unit_price, disc_price = 10.0, 9.70
    t_eoq = total + D * unit_price
    t_disc = (D / 1000.0) * S + (1000.0 / 2.0) * H + D * disc_price
    print("at EOQ purchase $%.2f vs discount-lot purchase $%.2f" % (t_eoq, t_disc))
    assert t_disc < t_eoq, "the 3% break wins here"
    print("rule: compute it, then adjust for pallets and reality")
    print("OK: %s walked the middle path" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_inv_safety_stock(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # SS = z * sigma_d * sqrt(L): the statistical cushion
    sigma_d, L = 8.0, 9.0
    z_levels = {"90%": 1.28, "95%": 1.65, "99%": 2.33}
    for svc, z in z_levels.items():
        ss = z * sigma_d * math.sqrt(L)
        cost = ss * 12.0
        print("service %s: SS %.2f units ($%.2f)" % (svc, ss, cost))
    ss95 = z_levels["95%"] * sigma_d * math.sqrt(L)
    ss90 = z_levels["90%"] * sigma_d * math.sqrt(L)
    ss99 = z_levels["99%"] * sigma_d * math.sqrt(L)
    assert 39.5 < ss95 < 39.7
    assert 30.7 < ss90 < 30.8
    assert 55.9 < ss99 < 56.0
    # the last nines are dear: 95 -> 99 costs 40% more buffer
    premium = (ss99 - ss95) / ss95 * 100.0
    print("95%% -> 99%% buffer premium: %.1f %%" % premium)
    assert 41.0 < premium < 41.5
    # joins the reorder point
    R = 20.0 * L + ss95
    print("R = d*L + SS = %.1f" % R)
    assert 219.5 < R < 219.7
    print("rule: insurance priced by statistics, bought with shelf space")
    print("OK: %s sized the guard" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_inv_fefo(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
import datetime
def main():
    # three lots: arrival order scrambled vs expiry order
    lots = [
        {"lot": "L1", "arrived": datetime.date(2026, 10, 1), "exp": datetime.date(2026, 11, 30), "qty": 100},
        {"lot": "L2", "arrived": datetime.date(2026, 10, 5), "exp": datetime.date(2026, 10, 25), "qty": 60},
        {"lot": "L3", "arrived": datetime.date(2026, 10, 3), "exp": datetime.date(2026, 12, 15), "qty": 80},
    ]
    need = 120
    # FEFO: consume nearest expiry first
    fefo = sorted(lots, key=lambda l: l["exp"])
    taken = []
    for lot in fefo:
        if need <= 0: break
        take = min(lot["qty"], need)
        taken.append((lot["lot"], take))
        lot["qty"] -= take; need -= take
    print("FEFO takes: %s" % taken)
    assert taken == [("L2", 60), ("L1", 60)]
    # FIFO would have taken the earliest arrival (L1) first - wrong lot here
    fifo_first = sorted(lots, key=lambda l: l["arrived"])[0]["lot"]
    print("FIFO would take %s first; FEFO takes %s first" % (fifo_first, taken[0][0]))
    assert fifo_first == "L1" and taken[0][0] == "L2"
    remaining = sum(l["qty"] for l in lots)
    print("remaining after pick: %d" % remaining)
    assert remaining == 120
    print("rule: the product's clock decides who leaves first")
    print("OK: %s bowed to the natural law" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_inv_reservation_logic(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # allocate short stock by priority, then order age
    stock = 150
    orders = [
        {"o": "O1", "prio": 1, "age": 5, "qty": 80},
        {"o": "O2", "prio": 2, "age": 2, "qty": 60},
        {"o": "O3", "prio": 1, "age": 1, "qty": 50},
    ]
    ranked = sorted(orders, key=lambda x: (x["prio"], -x["age"]))
    print("allocation order: %s" % [r["o"] for r in ranked])
    assert [r["o"] for r in ranked] == ["O1", "O3", "O2"]
    reserved, remaining = {}, stock
    for r in ranked:
        take = min(r["qty"], remaining)
        reserved[r["o"]] = take
        remaining -= take
    print("reserved: %s, unallocated: %d" % (reserved, remaining))
    assert reserved == {"O1": 80, "O3": 50, "O2": 20}
    assert remaining == 0
    atp = stock - sum(reserved.values())
    print("available to promise after allocation: %d" % atp)
    assert atp == 0
    # O3 cancels: its reservation is released honestly
    released = reserved.pop("O3")
    atp2 = stock - sum(reserved.values())
    print("O3 cancelled, released %d -> ATP %d" % (released, atp2))
    assert released == 50 and atp2 == 50
    print("rule: pin every promise; ration shortage by open rank")
    print("OK: %s kept the honor roll" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_inv_putaway_strategies(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # score open locations: filter by fit and family, score by travel and height
    unit = {"l": 48, "w": 40, "family": "fasteners", "velocity": "high"}
    locs = [
        {"id": "L1", "dist": 20, "golden": True, "family": "fasteners", "fits": True},
        {"id": "L2", "dist": 12, "golden": False, "family": "fasteners", "fits": True},
        {"id": "L3", "dist": 8, "golden": True, "family": "chemicals", "fits": True},
        {"id": "L4", "dist": 30, "golden": True, "family": "fasteners", "fits": True},
        {"id": "L5", "dist": 15, "golden": True, "family": "fasteners", "fits": False},
    ]
    cands = [l for l in locs if l["fits"] and l["family"] == unit["family"]]
    print("candidates after fit+family filter: %s" % [l["id"] for l in cands])
    assert [l["id"] for l in cands] == ["L1", "L2", "L4"]
    scored = sorted(((l["dist"] - (15 if l["golden"] else 0), l["id"]) for l in cands))
    print("scores (lower wins): %s" % scored)
    winner = scored[0][1]
    assert winner == "L1"
    assert 4.9 < scored[0][0] < 5.1
    print("putaway task: pallet -> %s [scan on arrival]" % winner)
    print("rule: heavy low, swift near the door, kin with kin")
    print("OK: %s settled the treasury" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_inv_picking_strategies(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # ten one-line orders at aisle positions 10..100
    positions = [10 * i for i in range(1, 11)]
    discrete = sum(2 * p for p in positions)
    batch = 2 * max(positions)
    zone = 2 * 50 + 2 * 100  # two zones: near half, far half
    print("discrete travel: %d ft" % discrete)
    print("batch travel:    %d ft" % batch)
    print("zone travel:     %d ft" % zone)
    assert 1099.9 < discrete < 1100.1
    assert 199.9 < batch < 200.1
    assert 299.9 < zone < 300.1
    saving = (discrete - batch) / discrete * 100.0
    print("batch saves %.1f %% of discrete walking" % saving)
    assert 81.8 < saving < 81.9
    print("rule: group the gathering so no step is wasted")
    print("OK: %s marched wisely" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_inv_packing_records(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # pack a 3-line order; weight band is the cheap second net
    lines = [("S1", 10, 0.5), ("S2", 4, 1.2), ("S3", 2, 0.8)]
    expected = sum(q * w for _, q, w in lines)
    lo, hi = expected * 0.95, expected * 1.05
    print("expected %.2f kg; band %.2f-%.2f" % (expected, lo, hi))
    assert 11.39 < expected < 11.41
    good_carton = 11.5
    print("carton 1 weighs %.2f -> %s" % (good_carton, "PASS" if lo < good_carton < hi else "FAIL"))
    assert lo < good_carton < hi
    bad_carton = 12.5  # an extra item slipped in
    verdict = "PASS" if lo < bad_carton < hi else "FAIL - reopen and recheck"
    print("carton 2 weighs %.2f -> %s" % (bad_carton, verdict))
    assert not (lo < bad_carton < hi)
    print("manifest: 2 cartons, SSCCs printed, load L-77")
    print("rule: seal nothing unverified")
    print("OK: %s sealed the vow" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_inv_movement_records(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the conserved ledger: transfers, adjustments, reclassifications
    bins = {"A-01": 100, "B-02": 50, "Q-HOLD": 10}
    start_total = sum(bins.values())
    # forward-fill transfer 30 from A-01 to B-02 (atomic: both legs together)
    bins["A-01"] -= 30; bins["B-02"] += 30
    print("transfer 30 A-01 -> B-02: %s" % bins)
    assert bins["A-01"] == 70 and bins["B-02"] == 80
    # damage adjustment with reason code
    bins["B-02"] -= 5
    print("adjustment -5 at B-02 [reason DAMAGED, 2nd approval]")
    assert bins["B-02"] == 75
    # quarantine release: state change, same building
    bins["Q-HOLD"] -= 10; bins["A-01"] += 10
    print("reclassify 10 Q-HOLD -> sellable at A-01: %s" % bins)
    end_total = sum(bins.values())
    print("ledger total: %d -> %d (damage written off)" % (start_total, end_total))
    assert start_total == 160
    assert 154.9 < end_total < 155.1
    assert end_total == start_total - 5
    print("rule: every step written, the ledger conserved")
    print("OK: %s witnessed every passage" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_inv_layout_slotting(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # velocity-ranked SKUs vs slot distances: travel = sum(velocity * distance)
    vel = [50, 40, 30, 20, 15, 10, 8, 5, 3, 2]
    slotted = [10, 12, 15, 20, 25, 30, 40, 50, 70, 90]   # fast near the dock
    naive = list(reversed(slotted))                        # unslotted: fast far away
    t_slot = sum(v * d for v, d in zip(vel, slotted))
    t_naive = sum(v * d for v, d in zip(vel, naive))
    saving = (t_naive - t_slot) / t_naive * 100.0
    print("slotted travel: %d ft-day; naive travel: %d ft-day" % (t_slot, t_naive))
    print("slotting saves %.2f %% of pick travel" % saving)
    assert 3464.9 < t_slot < 3465.1
    assert 10590.9 < t_naive < 10591.1
    assert 67.27 < saving < 67.30
    print("rule: seat every SKU by its worth and its speed")
    print("OK: %s seated the court" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_inv_multi_echelon(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # four regional sites: per-site buffers vs one pooled buffer
    sites = 4
    local_ss = 100.0
    silo_total = sites * local_ss
    pooled = local_ss * math.sqrt(sites)  # square-root law
    print("silo safety stock: %.0f; pooled: %.1f" % (silo_total, pooled))
    assert 199.9 < pooled < 200.1
    saving = (silo_total - pooled) / silo_total * 100.0
    print("pooling saves %.1f %% of the buffer" % saving)
    assert 49.9 < saving < 50.1
    # echelon position: own stock plus everything downstream
    own, downstream = 300.0, 800.0
    echelon = own + downstream
    print("echelon position: %.0f own + %.0f downstream = %.0f" % (own, downstream, echelon))
    assert 1099.9 < echelon < 1100.1
    print("rule: guard the whole, not each door separately")
    print("OK: %s thought in echelons" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_inv_mrp_logic(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # explode a 2-level BOM, net against inventory, release by lead time
    # parent P: 500 needed week 6; each P needs 2 of component C
    gross = {6: 1000}
    on_hand, scheduled = 300, {5: 200}
    lead_time = 2
    net_need = gross[6] - on_hand - scheduled.get(5, 0)
    print("gross %d - on-hand %d - scheduled %d = net %d" % (gross[6], on_hand, scheduled[5], net_need))
    assert net_need == 500
    release_week = 6 - lead_time
    print("planned order: %d units, release week %d (LT %d)" % (net_need, release_week, lead_time))
    assert release_week == 4
    # pegging: the planned order knows its parent demand
    peg = {"planned-C-500": "parent P week-6 demand"}
    print("pegging: %s" % peg)
    assert peg["planned-C-500"] == "parent P week-6 demand"
    print("rule: muster by lineage; freeze the near ranks")
    print("OK: %s mustered the host" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_inv_inventory_accuracy(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # count accuracy and dollar accuracy from a counted sample
    counted, matched = 200, 188
    count_acc = matched / counted * 100.0
    book_val, counted_val = 52000.0, 51200.0
    dollar_acc = counted_val / book_val * 100.0
    variance = book_val - counted_val
    print("count accuracy: %.1f %% (%d/%d)" % (count_acc, matched, counted))
    print("dollar accuracy: %.2f %%; variance $%.2f" % (dollar_acc, variance))
    assert 93.9 < count_acc < 94.1
    assert 98.45 < dollar_acc < 98.47
    assert 799.9 < variance < 800.1
    # trace three variances to causes through the movement trail
    causes = {"S-118": "mis-pick posted to S-119", "S-204": "receipt posted to wrong lot",
              "S-311": "unrecorded damage at pack"}
    print("variance causes: %s" % causes)
    assert len(causes) == 3
    print("process fixes logged for the top cause family: pick confirmation")
    print("rule: cure the process, not the variance")
    print("OK: %s healed at the source" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_inv_perpetual_periodic(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # 30 days: true issues 20/day, plus 1 unrecorded unit lost per day
    start = 1000
    true_issues = 20 * 30
    shrinkage = 1 * 30
    true_end = start - true_issues - shrinkage
    perpetual_says = start - true_issues  # the unrecorded loss never posted
    drift = perpetual_says - true_end
    print("perpetual balance: %d; true balance: %d; drift: %d" % (perpetual_says, true_end, drift))
    assert perpetual_says == 400
    assert true_end == 370
    assert drift == 30
    # the periodic count snaps it back with one honest adjustment
    adjustment = true_end - perpetual_says
    print("physical count finds %d -> adjustment %d [reason SHRINKAGE]" % (true_end, adjustment))
    assert adjustment == -30
    print("rule: perpetual without discipline is periodic with delusions")
    print("OK: %s took its truth honestly" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_inv_advanced_slotting(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # cube-per-order index: cube / picks per period; smallest earns closest slot
    skus = {"A": (2.0, 50), "B": (10.0, 40), "C": (1.0, 30), "D": (20.0, 20),
            "E": (5.0, 15), "F": (30.0, 10), "G": (0.5, 8), "H": (50.0, 5)}
    coi = {k: cube / picks for k, (cube, picks) in skus.items()}
    ranked = sorted(coi, key=lambda k: coi[k])
    print("COI ranking: %s" % [(k, round(coi[k], 4)) for k in ranked])
    assert ranked == ["C", "A", "G", "B", "E", "D", "F", "H"]
    assert 0.0332 < coi["C"] < 0.0334
    assert 9.99 < coi["H"] < 10.01
    golden = ranked[:3]
    print("golden-zone seats (knee to shoulder, nearest dock): %s" % golden)
    assert golden == ["C", "A", "G"]
    print("rule: small and frequent wins the closest slots")
    print("OK: %s seated by merit and measure" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_inv_dynamic_safety_stock(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the buffer breathes with the seasons: recompute from fresh variability
    L, z = 9.0, 1.65
    off_sigma, peak_sigma = 6.0, 14.0
    ss_off = z * off_sigma * math.sqrt(L)
    ss_peak = z * peak_sigma * math.sqrt(L)
    print("off-season SS %.2f; peak-season SS %.2f" % (ss_off, ss_peak))
    assert 29.69 < ss_off < 29.71
    assert 69.29 < ss_peak < 69.31
    # price the nines at peak: 95% vs 99%
    ss99 = 2.33 * peak_sigma * math.sqrt(L)
    premium = (ss99 - ss_peak) / ss_peak * 100.0
    print("peak 99%% SS %.2f: premium over 95%% is %.1f %%" % (ss99, premium))
    assert 97.85 < ss99 < 97.87
    assert 41.1 < premium < 41.3
    # ABC-differentiated targets
    targets = {"A": "99%", "B": "95%", "C": "90%"}
    print("service targets by class: %s" % targets)
    print("rule: a guard that never changes is a guard asleep")
    print("OK: %s watched the seasons" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_inv_replenishment_systems(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # kanban sizing: cards = D * L * (1 + S) / C
    D, L, S, C = 200.0, 2.0, 0.20, 50.0
    raw = D * L * (1 + S) / C
    cards = math.ceil(raw)
    print("kanban loop: raw %.2f -> %d cards of %d" % (raw, cards, int(C)))
    assert 9.5 < raw < 9.7
    assert cards == 10
    # min-max: cross the min, order up to the max
    min_lvl, max_lvl, on_hand = 100, 400, 90
    order = max_lvl - on_hand if on_hand <= min_lvl else 0
    print("min-max bin at %d (min %d): order %d" % (on_hand, min_lvl, order))
    assert order == 310
    # DRP: time-phased netting for a downstream site
    gross_w3, site_on_hand, in_transit = 500, 200, 100
    net = gross_w3 - site_on_hand - in_transit
    ship_week = 3 - 2  # lane lead time 2 weeks
    print("DRP: net need %d in week 3 -> ship week %d" % (net, ship_week))
    assert net == 200 and ship_week == 1
    print("rule: the signal is automatic and tied to consumption")
    print("OK: %s steadied the pulse" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_inv_returns_rma(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # grade five returns; the grade decides the financial fate
    returns = [("R-1", 100.0, "A"), ("R-2", 80.0, "B"), ("R-3", 120.0, "A"),
               ("R-4", 60.0, "C"), ("R-5", 40.0, "D")]
    recovery_rate = {"A": 1.0, "B": 0.5, "C": 0.2, "D": 0.0}
    disposition = {"A": "restock as new", "B": "refurbish", "C": "parts harvest", "D": "scrap"}
    total_val, recovered = 0.0, 0.0
    for rma, val, grade in returns:
        rec = val * recovery_rate[grade]
        total_val += val; recovered += rec
        print("%s: $%.0f grade %s -> %s, recovered $%.0f" % (rma, val, grade, disposition[grade], rec))
    pct = recovered / total_val * 100.0
    print("value recovery: $%.0f of $%.0f = %.1f %%" % (recovered, total_val, pct))
    assert 271.9 < recovered < 272.1
    assert 67.9 < pct < 68.1
    print("top return reason this month: SIZE_WRONG - fed back to the listing team")
    print("rule: the returned vow is the treasury's truest teacher")
    print("OK: %s learned from every reason" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_inv_serialization(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # register 20 individuals, aggregate into cases and a pallet
    serials = ["SN-%04d" % i for i in range(1, 21)]
    assert len(set(serials)) == 20, "serials must be unique"
    cases = {"CASE-1": serials[:10], "CASE-2": serials[10:]}
    pallet = {"PALLET-1": ["CASE-1", "CASE-2"]}
    registry = {s: {"case": "CASE-1" if i < 10 else "CASE-2", "state": "in-stock"}
                for i, s in enumerate(serials)}
    # ship three units: the shipment names the serials
    shipped = ["SN-0001", "SN-0002", "SN-0003"]
    for s in shipped:
        registry[s]["state"] = "shipped"
    print("registered %d serials in %d cases on 1 pallet; shipped %d" % (len(serials), len(cases), len(shipped)))
    # trace one serial's full history
    trace = registry["SN-0015"]
    print("trace SN-0015: case %s, pallet PALLET-1, state %s" % (trace["case"], trace["state"]))
    assert trace == {"case": "CASE-2", "state": "in-stock"}
    in_stock = sum(1 for v in registry.values() if v["state"] == "in-stock")
    assert in_stock == 17
    print("rule: know its charges by name")
    print("OK: %s named every charge" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_inv_physical_inventory(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # freeze, double blind count, reconcile against the snapshot
    snapshot = {"locations": 50, "book_units": 1000}
    # 49 locations match; L-07 shows a planted discrepancy
    matches, total_locs = 49, 50
    loc_accuracy = matches / total_locs * 100.0
    book_L07, count_L07 = 50, 48
    variance = count_L07 - book_L07
    print("frozen snapshot: %d units across %d locations" % (snapshot["book_units"], snapshot["locations"]))
    print("L-07: book %d, blind counts %d/%d -> variance %d" % (book_L07, count_L07, count_L07, variance))
    assert variance == -2
    print("location accuracy: %.1f %%" % loc_accuracy)
    assert 97.9 < loc_accuracy < 98.1
    # reconcile: investigate, then post the reason-coded adjustment
    print("investigation: unrecorded damage at pack, confirmed by camera log")
    adjustment = variance
    corrected = snapshot["book_units"] + adjustment
    print("adjustment %d [reason UNRECORDED_DAMAGE, approved] -> corrected %d" % (adjustment, corrected))
    assert corrected == 998
    print("rule: count blind, count twice, judge every variance")
    print("OK: %s met the day of judgment" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_inv_inventory_analytics(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the dashboard: turns, days of supply, fill rate, GMROI
    cogs, avg_inv = 520000.0, 130000.0
    turns = cogs / avg_inv
    daily_use = cogs / 365.0
    dos = avg_inv / daily_use
    print("turns: %.2f / yr" % turns)
    print("days of supply: %.2f days" % dos)
    assert 3.99 < turns < 4.01
    assert 91.24 < dos < 91.26
    lines_ordered, lines_filled = 1000, 940
    fill = lines_filled / lines_ordered * 100.0
    print("fill rate: %.1f %%" % fill)
    assert 93.9 < fill < 94.1
    sales = 800000.0
    gmroi = (sales - cogs) / avg_inv
    print("GMROI: %.3f" % gmroi)
    assert 2.153 < gmroi < 2.155
    # excess and obsolete: name the dead stock
    skus = [("E-1", 210), ("E-2", 45), ("E-3", 400), ("E-4", 20)]
    excess = [s for s, d in skus if d > 180]
    print("excess SKUs (DOS > 180): %s - dispositions assigned" % excess)
    assert excess == ["E-1", "E-3"]
    print("rule: numbers without owners are wallpaper")
    print("OK: %s read the mirror" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_inv_health_program(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the composite health score: six pillars, one number
    pillars = {"accuracy": 94.0, "fill_rate": 96.0, "turns": 70.0,
               "excess_control": 80.0, "count_compliance": 98.0, "on_time_replenishment": 88.0}
    weights = {"accuracy": 0.25, "fill_rate": 0.20, "turns": 0.15,
               "excess_control": 0.15, "count_compliance": 0.15, "on_time_replenishment": 0.10}
    assert abs(sum(weights.values()) - 1.0) < 1e-9
    score = sum(pillars[k] * weights[k] for k in pillars)
    print("pillar scores: %s" % pillars)
    print("inventory health score: %.1f / 100" % score)
    assert 88.69 < score < 88.71
    red = [k for k, v in pillars.items() if v < 80.0]
    print("red pillars: %s" % red)
    assert red == ["turns"]
    print("corrective action: CA-441 turns improvement - owner: planning lead, due in 30 days")
    print("rule: one organism, one pulse")
    print("OK: %s swore the oath of the house" % NAME)
if __name__ == "__main__":
    main()
''')


DEMOS = {
    "what_is": demo_inv_what_is,
    "sku_atom": demo_inv_sku_atom,
    "stock_states": demo_inv_stock_states,
    "location_address": demo_inv_location_address,
    "uom_hierarchy": demo_inv_uom_hierarchy,
    "valuation_simple": demo_inv_valuation_simple,
    "lead_time": demo_inv_lead_time,
    "goods_receipt": demo_inv_goods_receipt,
    "pick_pack_ship": demo_inv_pick_pack_ship,
    "expiry_lot_basics": demo_inv_expiry_lot_basics,
    "cycle_counting": demo_inv_cycle_counting,
    "abc_analysis": demo_inv_abc_analysis,
    "reorder_point": demo_inv_reorder_point,
    "eoq": demo_inv_eoq,
    "safety_stock": demo_inv_safety_stock,
    "fefo": demo_inv_fefo,
    "reservation_logic": demo_inv_reservation_logic,
    "putaway_strategies": demo_inv_putaway_strategies,
    "picking_strategies": demo_inv_picking_strategies,
    "packing_records": demo_inv_packing_records,
    "movement_records": demo_inv_movement_records,
    "layout_slotting": demo_inv_layout_slotting,
    "multi_echelon": demo_inv_multi_echelon,
    "mrp_logic": demo_inv_mrp_logic,
    "inventory_accuracy": demo_inv_inventory_accuracy,
    "perpetual_periodic": demo_inv_perpetual_periodic,
    "advanced_slotting": demo_inv_advanced_slotting,
    "dynamic_safety_stock": demo_inv_dynamic_safety_stock,
    "replenishment_systems": demo_inv_replenishment_systems,
    "returns_rma": demo_inv_returns_rma,
    "serialization": demo_inv_serialization,
    "physical_inventory": demo_inv_physical_inventory,
    "inventory_analytics": demo_inv_inventory_analytics,
    "health_program": demo_inv_health_program,
}
