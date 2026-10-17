#!/usr/bin/env python3
"""Demo programs for the Asset and Equipment Registry databases.

Every demo is real, runnable, stdlib-only Python performing the actual
asset-registry computation for its record. All are machine-executed by
build.py: each prints its real computed values, asserts tight bounds (never
float exact-equality), and ends with the OK marker.
"""

_PREAMBLE = "import math\n"


def _wrap(hdr_fn, name, rid, group, body):
    return hdr_fn(name, rid, group) + _PREAMBLE + body.replace("NAME", __import__("json").dumps(name))


def demo_aer_what_is_asset(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the three gates: threshold, useful life, standalone unit
    threshold = 2500.0
    items = [
        ("laptop", 1800.0, 4, True),
        ("air compressor", 3200.0, 10, True),
        ("wrench", 40.0, 8, True),
        ("warehouse building", 250000.0, 39, True),
        ("box of filters", 320.0, 0, False),
    ]
    capitalized, tracked_only, expensed = [], [], []
    for label, cost, life, standalone in items:
        if cost >= threshold and life > 1 and standalone:
            capitalized.append((label, cost))
        elif standalone and life > 1:
            tracked_only.append((label, cost))
        else:
            expensed.append((label, cost))
    cap_total = sum(c for _, c in capitalized)
    print("capitalized: %s" % capitalized)
    print("tracked but expensed: %s" % tracked_only)
    print("expensed supplies: %s" % expensed)
    print("capitalized total: $%.2f" % cap_total)
    assert len(capitalized) == 2
    assert len(tracked_only) == 2
    assert len(expensed) == 1
    assert 253199.99 < cap_total < 253200.01
    print("rule: threshold, life, standalone - three gates, one decision")
    print("OK: %s classified the fleet" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_aer_register_anatomy(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # six families; completeness = filled required fields over required fields
    families = {
        "identity": ["tag", "serial", "manufacturer", "model", "asset_name", "acquired"],
        "classification": ["category", "subcategory", "class", "depr_method", "depr_life"],
        "location": ["site", "building", "room", "custodian"],
        "condition": ["condition_rating", "condition_date", "inspector"],
        "financials": ["cost_basis", "in_service_date", "book_value", "funding_source"],
        "history": ["warranty_expiry", "work_orders", "custody_chain", "calibration_due"],
    }
    record = {f: True for fam in families.values() for f in fam}
    record["calibration_due"] = False  # not yet scheduled
    record["funding_source"] = False   # missing
    required = sum(len(v) for v in families.values())
    filled = sum(1 for v in record.values() if v)
    completeness = filled / required * 100.0
    print("field families: %d" % len(families))
    print("required fields: %d, filled: %d" % (required, filled))
    print("completeness: %.2f %%" % completeness)
    per_family = {k: sum(1 for f in v if record[f]) / len(v) * 100.0 for k, v in families.items()}
    for k, v in per_family.items():
        print("  %-15s %5.1f %%" % (k, v))
    assert required == 26
    assert filled == 24
    assert 92.30 < completeness < 92.32
    assert 74.9 < per_family["history"] < 75.1
    assert 99.9 < per_family["identity"] < 100.1
    print("rule: six families, one truth - identity, class, location, condition, financials, history")
    print("OK: %s measured the record" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_aer_asset_tags(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # tag check digit (mod-10) over the numeric core 202600417
    core = "202600417"
    total = sum(int(d) for d in core)
    check = (10 - total % 10) % 10
    tag = "AREG-" + core[:4] + "-" + core[4:] + str(check)
    print("numeric core: %s digit sum %d" % (core, total))
    print("check digit: %d" % check)
    print("full tag: %s" % tag)
    assert total == 22
    assert check == 8
    assert tag == "AREG-2026-004178"
    # verify: recompute from a presented tag
    presented = "AREG-2026-004178"
    digits = "".join(c for c in presented if c.isdigit())
    vtotal = sum(int(d) for d in digits[:-1])
    vcheck = (10 - vtotal % 10) % 10
    ok = (vcheck == int(digits[-1]))
    print("presented tag verifies: %s" % ok)
    assert ok
    # a mistyped tag fails
    bad = "AREG-2026-004188"
    bdigits = "".join(c for c in bad if c.isdigit())
    btotal = sum(int(d) for d in bdigits[:-1])
    assert (10 - btotal % 10) % 10 != int(bdigits[-1])
    print("mistyped tag correctly rejected")
    print("rule: the number is the identity - the check digit guards it")
    print("OK: %s named the asset" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_aer_categories(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # class defaults inherit: depreciation life and PM template per class
    classes = {
        "IT-LAPTOP": {"life": 4, "assets": 412, "avg_cost": 1400.0},
        "FAC-HVAC": {"life": 15, "assets": 86, "avg_cost": 18500.0},
        "VEH-PICKUP": {"life": 7, "assets": 64, "avg_cost": 42000.0},
        "TOOL-POWER": {"life": 8, "assets": 930, "avg_cost": 320.0},
    }
    total_assets = sum(c["assets"] for c in classes.values())
    # straight-line annual depreciation across the classified fleet
    annual_depr = sum(c["assets"] * c["avg_cost"] / c["life"] for c in classes.values())
    print("classified assets: %d" % total_assets)
    for k, c in classes.items():
        print("  %-10s life %2dy  %4d assets  class depr $%10.2f/yr" %
              (k, c["life"], c["assets"], c["assets"] * c["avg_cost"] / c["life"]))
    print("fleet annual depreciation: $%.2f" % annual_depr)
    assert total_assets == 1492
    assert 671466.66 < annual_depr < 671466.68
    print("rule: rules written once per shelf, inherited by every asset on it")
    print("OK: %s shelved the fleet" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_aer_naming_taxonomy(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # SITE-SYSTEM-SEQUENCE construction from controlled vocabularies
    sites = {"HQ": "Headquarters", "DEN": "Denver Plant", "AUS": "Austin Depot"}
    systems = {"HVAC": "Heating/Ventilation/AC", "ELEC": "Electrical", "PLMB": "Plumbing"}
    counters = {}
    def make_name(site, system):
        assert site in sites and system in systems, "vocabulary violation"
        key = (site, system)
        counters[key] = counters.get(key, 0) + 1
        return "%s-%s-%03d" % (site, system, counters[key])
    names = [make_name("HQ", "HVAC") for _ in range(3)] + [make_name("DEN", "ELEC")]
    print("constructed: %s" % names)
    assert names == ["HQ-HVAC-001", "HQ-HVAC-002", "HQ-HVAC-003", "DEN-ELEC-001"]
    # parse back: the name decomposes without a lookup
    def parse(nm):
        parts = nm.split("-")
        assert len(parts) == 3
        return {"site": parts[0], "system": parts[1], "seq": int(parts[2]),
                "site_name": sites[parts[0]], "system_name": systems[parts[1]]}
    p = parse("HQ-HVAC-014")
    print("parsed HQ-HVAC-014 -> %s" % p)
    assert p["site"] == "HQ" and p["system"] == "HVAC" and p["seq"] == 14
    # alias table: old names resolve to the official name
    aliases = {"Compressor #3": "HQ-HVAC-003", "AC-3": "HQ-HVAC-003"}
    assert aliases["AC-3"] == "HQ-HVAC-003"
    print("alias AC-3 resolves to HQ-HVAC-003")
    print("rule: one name, spelled one way, everywhere")
    print("OK: %s spoke the language" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_aer_acquisition_cap(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # capitalized cost = price + freight + installation + setup labor
    price, freight, install, setup = 45000.0, 1200.0, 3800.0, 0.0
    basis = price + freight + install + setup
    threshold, life, standalone = 2500.0, 10, True
    capitalize = basis >= threshold and life > 1 and standalone
    annual_sl = basis / life
    print("capitalized cost basis: $%.2f" % basis)
    print("gates: cost>=threshold %s, life>1 %s, standalone %s" %
          (basis >= threshold, life > 1, standalone))
    print("capitalize: %s" % capitalize)
    print("straight-line annual: $%.2f" % annual_sl)
    assert 49999.99 < basis < 50000.01
    assert capitalize
    assert 4999.99 < annual_sl < 50000.01 / 10 + 0.01
    assert 4999.99 < annual_sl < 5000.01
    # in-service date starts the clock, not delivery
    from datetime import date
    delivered, commissioned = date(2025, 12, 18), date(2026, 2, 4)
    in_service = commissioned
    first_year_months = 13 - in_service.month
    print("delivered %s, in service %s - depreciation starts %s" % (delivered, in_service, in_service))
    print("first-year months in service: %d" % first_year_months)
    assert in_service == date(2026, 2, 4)
    assert first_year_months == 11
    print("rule: the clock starts when the asset is ready for use")
    print("OK: %s welcomed the asset" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_aer_assignment_custody(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # chain of custody: every link named, dated, signed
    chain = [
        ("2024-01-05", "2024-06-10", "Alvarez"),
        ("2024-06-10", "2024-09-02", "Denver Site"),
        ("2024-09-02", None, "Tool Pool"),
    ]
    def find_gaps(links):
        gaps = []
        for (s1, e1, _), (s2, e2, _) in zip(links, links[1:]):
            if e1 != s2:
                gaps.append((e1, s2))
        unassigned = [l for l in links if l[2] is None]
        return gaps, unassigned
    gaps, unassigned = find_gaps(chain)
    print("custody links: %d, gaps: %d, unassigned: %d" % (len(chain), len(gaps), len(unassigned)))
    assert len(gaps) == 0 and len(unassigned) == 0
    # a broken chain is detected
    broken = [
        ("2024-01-05", "2024-06-10", "Alvarez"),
        ("2024-07-01", None, "Denver Site"),  # 21-day gap, no signatures
    ]
    bgaps, _ = find_gaps(broken)
    print("broken chain gaps detected: %s" % bgaps)
    assert len(bgaps) == 1
    # exit clearance: zero assigned assets before HR clears
    assigned_to_departing = [l for l in chain if l[2] == "Alvarez" and l[1] is None]
    clear = len(assigned_to_departing) == 0
    print("departing custodian clear: %s" % clear)
    assert clear
    print("rule: every asset, exactly one custodian, every link signed")
    print("OK: %s kept the chain" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_aer_condition_ratings(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # 1-5 scale; overall follows the worst significant element
    elements = {"casing": 2, "seals": 4, "bearings": 2, "motor_amps": 3, "alignment": 2}
    overall = max(elements.values())
    history = [2, 2, 3, 3, 4]
    avg = sum(history) / len(history)
    print("element scores: %s" % elements)
    print("overall rating (worst element): %d" % overall)
    print("rating history %s average %.2f" % (history, avg))
    assert overall == 4
    assert 2.79 < avg < 2.81
    # fleet roll-up: the backlog quantified
    fleet = [1]*40 + [2]*120 + [3]*60 + [4]*22 + [5]*8
    backlog = sum(1 for r in fleet if r >= 4)
    backlog_pct = backlog / len(fleet) * 100.0
    fleet_avg = sum(fleet) / len(fleet)
    print("fleet: %d assets, condition 4-5 backlog: %d (%.1f %%), average %.2f" %
          (len(fleet), backlog, backlog_pct, fleet_avg))
    assert len(fleet) == 250
    assert backlog == 30
    assert 11.99 < backlog_pct < 12.01
    assert 2.35 < fleet_avg < 2.37
    print("rule: the worst element defines the asset; the distribution defines the plan")
    print("OK: %s heard the testimony" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_aer_location_tracking(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    from datetime import date
    # controlled hierarchy + move log; current location is the last move
    moves = [
        (date(2023, 3, 1), "DEN", "Bldg B", "Production Floor", "Line 3"),
        (date(2024, 8, 15), "DEN", "Bldg B", "Production Floor", "Line 5"),
        (date(2025, 11, 2), "AUS", "Bldg A", "Assembly", "Cell 2"),
    ]
    today = date(2026, 10, 17)
    current = moves[-1]
    days_there = (today - current[0]).days
    print("moves on record: %d" % len(moves))
    print("current: %s / %s / %s / %s since %s (%d days)" %
          (current[1], current[2], current[3], current[4], current[0], days_there))
    assert len(moves) == 3
    assert current[1] == "AUS" and current[4] == "Cell 2"
    assert days_there == 349
    # auditor walk: register -> room -> tag
    expected = ("AUS", "Bldg A", "Assembly", "Cell 2")
    found = ("AUS", "Bldg A", "Assembly", "Cell 2")
    walk_ok = expected == found
    print("auditor walk (register->room->tag): %s" % walk_ok)
    assert walk_ok
    print("rule: the register and the room must agree")
    print("OK: %s knew where it stood" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_aer_lifecycle_states(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # guarded state machine: retirement is a one-way door
    transitions = {
        "Planned": ["Ordered", "Retired"],
        "Ordered": ["In Service", "Retired"],
        "In Service": ["In Maintenance", "In Storage", "Transferred", "Retired"],
        "In Maintenance": ["In Service", "Retired"],
        "In Storage": ["In Service", "Transferred", "Retired"],
        "Transferred": ["In Service", "In Storage", "Retired"],
        "Retired": ["Disposed"],
        "Disposed": [],
    }
    def move(state, nxt):
        assert nxt in transitions[state], "illegal transition %s -> %s" % (state, nxt)
        return nxt
    s = "Planned"
    for nxt in ["Ordered", "In Service", "In Maintenance", "In Service", "Retired", "Disposed"]:
        s = move(s, nxt)
    print("walked lifecycle: Planned -> ... -> %s" % s)
    assert s == "Disposed"
    # illegal jumps rejected
    for bad_from, bad_to in [("Retired", "In Service"), ("Ordered", "Disposed"), ("Disposed", "In Service")]:
        try:
            move(bad_from, bad_to)
            raise SystemExit("guard failed for %s -> %s" % (bad_from, bad_to))
        except AssertionError as ex:
            assert "illegal transition" in str(ex)
    print("illegal transitions rejected: Retired->In Service, Ordered->Disposed, Disposed->In Service")
    # state-keyed rules: work orders only against serviceable states
    workable = {"In Service", "In Maintenance"}
    assert "Retired" not in workable and "In Service" in workable
    print("rule: the road has guards; retirement is a one-way door")
    print("OK: %s walked the road" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_aer_tag_technologies(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # economics for 5,000 assets: label cost + audit labor
    n = 5000
    techs = {
        "barcode": {"tag_cost": 0.05, "infra": 400.0, "sec_per_scan": 30.0},
        "qr": {"tag_cost": 0.06, "infra": 0.0, "sec_per_scan": 12.0},
        "rfid": {"tag_cost": 0.35, "infra": 2500.0, "sec_per_scan": 2.0},
    }
    labor_hr = 28.0
    print("fleet: %d assets" % n)
    for k, t in techs.items():
        tag_total = n * t["tag_cost"] + t["infra"]
        audit_hours = n * t["sec_per_scan"] / 3600.0
        audit_cost = audit_hours * labor_hr
        print("  %-7s tags+infra $%8.2f  full audit %6.1f h ($%8.2f)" %
              (k, tag_total, audit_hours, audit_cost))
    bc = techs["barcode"]
    rf = techs["rfid"]
    bc_audit_h = n * bc["sec_per_scan"] / 3600.0
    rf_audit_h = n * rf["sec_per_scan"] / 3600.0
    print("barcode audit %.1f h vs rfid audit %.1f h" % (bc_audit_h, rf_audit_h))
    assert 41.6 < bc_audit_h < 41.8
    assert 2.77 < rf_audit_h < 2.79
    rf_total = n * rf["tag_cost"] + rf["infra"]
    assert 4249.99 < rf_total < 4250.01
    print("rule: match the voice to the keeping - quiet tags for quiet assets, chorus where counting is the work")
    print("OK: %s chose the voice" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_aer_depreciation(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    cost, salvage, life = 50000.0, 5000.0, 10
    # straight-line
    sl_annual = (cost - salvage) / life
    sl_book3 = cost - sl_annual * 3
    print("straight-line annual: $%.2f, book after 3y: $%.2f" % (sl_annual, sl_book3))
    assert 4499.99 < sl_annual < 4500.01
    assert 36499.99 < sl_book3 < 36500.01
    # double-declining balance with crossover to straight-line, landing on salvage
    rate = 2.0 / life
    book, sched = cost, []
    for yr in range(1, life + 1):
        ddb = book * rate
        sl_rem = (book - salvage) / (life - yr + 1)
        dep = max(ddb, sl_rem)
        dep = min(dep, book - salvage)
        book -= dep
        sched.append((yr, dep, book))
    print("DDB year 1: $%.2f, year 10: $%.2f, final book: $%.2f" % (sched[0][1], sched[-1][1], book))
    assert 9999.99 < sched[0][1] < 10000.01
    assert 4999.99 < book < 5000.01
    total_dep = sum(d for _, d, _ in sched)
    assert 44999.99 < total_dep < 45000.01
    # units of production: 120,000 lifetime hours, 11,400 this year
    uop_rate = (cost - salvage) / 120000.0
    uop_exp = uop_rate * 11400.0
    print("units-of-production this year (11,400 h): $%.2f" % uop_exp)
    assert 4274.99 < uop_exp < 4275.01
    print("rule: the schedule is a promise kept year after year")
    print("OK: %s kept the promise" % NAME)
if __name__ == "__main__":
    main()
''')


DEMOS = {
    "what_is_asset": demo_aer_what_is_asset,
    "register_anatomy": demo_aer_register_anatomy,
    "asset_tags": demo_aer_asset_tags,
    "categories": demo_aer_categories,
    "naming_taxonomy": demo_aer_naming_taxonomy,
    "acquisition_cap": demo_aer_acquisition_cap,
    "assignment_custody": demo_aer_assignment_custody,
    "condition_ratings": demo_aer_condition_ratings,
    "location_tracking": demo_aer_location_tracking,
    "lifecycle_states": demo_aer_lifecycle_states,
    "tag_technologies": demo_aer_tag_technologies,
    "depreciation": demo_aer_depreciation,
}


def demo_aer_cmdb_records(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # CI web: impact analysis walks downstream from the core switch
    rels = [
        ("SW-CORE-01", "depends-on", "UPS-02"),
        ("SRV-APP-03", "runs-on", "SRV-VMH-01"),
        ("SRV-VMH-01", "depends-on", "SW-CORE-01"),
        ("APP-ERP", "runs-on", "SRV-APP-03"),
        ("PRN-04", "connects-to", "SW-CORE-01"),
        ("SRV-DB-02", "depends-on", "SW-CORE-01"),
        ("APP-ERP", "depends-on", "SRV-DB-02"),
    ]
    down = {}
    for a, rel, b in rels:
        down.setdefault(b, []).append(a)
    def blast(ci):
        seen, stack = set(), [ci]
        while stack:
            cur = stack.pop()
            for dep in down.get(cur, []):
                if dep not in seen:
                    seen.add(dep)
                    stack.append(dep)
        return seen
    impacted = blast("SW-CORE-01")
    print("outage at SW-CORE-01 impacts %d CIs: %s" % (len(impacted), sorted(impacted)))
    assert len(impacted) == 5
    assert "APP-ERP" in impacted and "PRN-04" in impacted
    # upstream root-cause walk for APP-ERP
    up = {}
    for a, rel, b in rels:
        up.setdefault(a, []).append(b)
    def roots(ci):
        seen, stack = set(), [ci]
        while stack:
            cur = stack.pop()
            for dep in up.get(cur, []):
                if dep not in seen:
                    seen.add(dep)
                    stack.append(dep)
        return seen
    deps = roots("APP-ERP")
    print("APP-ERP depends upstream on %d CIs" % len(deps))
    assert len(deps) == 5
    print("rule: the web is the payoff - impact downstream, cause upstream")
    print("OK: %s charted the fellowship" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_aer_work_orders(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # failure history -> MTBF, bad actors, cost of care
    orders = [
        ("2024-02-11", "bearing seized - lubrication starvation", 6.0, 420.0),
        ("2024-05-03", "seal leak - worn faces", 3.0, 180.0),
        ("2024-09-19", "bearing seized - contamination ingress", 8.0, 510.0),
        ("2025-01-22", "coupling misalignment - thermal growth", 4.0, 260.0),
    ]
    op_hours, n_fail = 8000.0, len(orders)
    down = sum(h for _, _, h, _ in orders)
    cost = sum(c for _, _, _, c in orders)
    mtbf = op_hours / n_fail
    mttr = down / n_fail
    print("failures: %d in %.0f h, downtime %.1f h, parts+labor $%.2f" % (n_fail, op_hours, down, cost))
    print("MTBF %.0f h, MTTR %.1f h" % (mtbf, mttr))
    assert n_fail == 4
    assert 1999.9 < mtbf < 2000.1
    assert 5.24 < mttr < 5.26
    assert 1369.99 < cost < 1370.01
    # failure-mode roll-up: the repeat offender
    from collections import Counter
    modes = Counter(m.split(" - ")[0] for _, m, _, _ in orders)
    print("failure modes: %s" % dict(modes))
    assert modes["bearing seized"] == 2
    # as-found specificity check: vague notes rejected
    vague = [m for _, m, _, _ in orders if len(m.split()) < 3]
    print("vague work-order notes: %d" % len(vague))
    assert len(vague) == 0
    print("rule: specific notes teach; 'fixed pump' teaches nothing")
    print("OK: %s wrote the medical file" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_aer_pm_scheduling(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    from datetime import date, timedelta
    today = date(2026, 10, 17)
    # PM master: last completion + interval -> next due; overdue flagged
    pms = [
        ("P-101", "lubrication", date(2026, 9, 20), 30),
        ("P-101", "vibration route", date(2026, 9, 1), 60),
        ("AHU-04", "filter change", date(2026, 7, 10), 90),
        ("AHU-04", "belt inspection", date(2026, 10, 1), 30),
    ]
    due, overdue = [], []
    for asset, task, last, interval in pms:
        nxt = last + timedelta(days=interval)
        (overdue if nxt < today else due).append((asset, task, nxt))
    print("PMs due: %d, overdue: %d" % (len(due), len(overdue)))
    for asset, task, nxt in overdue:
        print("  OVERDUE %s %s was due %s" % (asset, task, nxt))
    assert len(overdue) == 1
    assert len(due) == 3
    # compliance = completed on time over due
    completed_on_time, total_due = 46, 50
    compliance = completed_on_time / total_due * 100.0
    print("PM compliance: %d/%d = %.1f %%" % (completed_on_time, total_due, compliance))
    assert 91.9 < compliance < 92.1
    assert compliance >= 90.0, "program is theater below 90%"
    # interval tuning: a PM that never finds anything earns extension
    findings_3y, current_interval = 0, 30
    new_interval = 60 if findings_3y == 0 else current_interval
    print("lubrication findings in 3y: %d -> interval %d -> %d days" %
          (findings_3y, current_interval, new_interval))
    assert new_interval == 60
    print("rule: the schedule is a promise kept in public, measured monthly")
    print("OK: %s kept the calendar" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_aer_warranty(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    from datetime import date
    today = date(2026, 10, 17)
    # coverage record: start trigger is in-service, not purchase
    in_service, duration_years = date(2024, 3, 15), 3
    expiry = date(in_service.year + duration_years, in_service.month, in_service.day)
    remaining = (expiry - today).days
    print("warranty: %s to %s, %d days remaining" % (in_service, expiry, remaining))
    assert expiry == date(2027, 3, 15)
    assert remaining == 149
    # claim eligibility on a failure inside coverage
    failure_date = date(2026, 9, 30)
    eligible = in_service <= failure_date <= expiry
    print("failure %s claim eligible: %s" % (failure_date, eligible))
    assert eligible
    # pre-expiry inspection at 90 days out
    inspect_on = date(expiry.year, expiry.month, expiry.day)
    from datetime import timedelta
    inspect_on = expiry - timedelta(days=90)
    print("pre-expiry inspection due: %s" % inspect_on)
    assert inspect_on == date(2026, 12, 15)
    # recovery ledger drives the renewal decision
    claims = [("2024-11-02", 1840.0), ("2026-09-30", 2310.0)]
    recovered = sum(c for _, c in claims)
    contract_price = 1500.0
    print("lifetime recovery $%.2f vs contract $%.2f -> renew: %s" %
          (recovered, contract_price, recovered > contract_price))
    assert 4149.99 < recovered < 4150.01
    assert recovered > contract_price
    print("rule: a promise unclaimed is a gift refused")
    print("OK: %s watched the horizon" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_aer_calibration(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    from datetime import date, timedelta
    today = date(2026, 10, 17)
    # recall: due dates from last calibration + interval
    instruments = [
        ("TQW-014", "torque wrench", date(2026, 2, 10), 365, 150.0, 0.04),
        ("DMM-207", "multimeter", date(2025, 12, 1), 365, None, 0.001),
        ("PG-033", "pressure gauge", date(2026, 9, 25), 180, 100.0, 0.01),
    ]
    for tag, kind, last, interval, nominal, tol in instruments:
        due = last + timedelta(days=interval)
        status = "OVERDUE" if due < today else "due %s" % due
        print("  %s %-14s last %s interval %dd -> %s" % (tag, kind, last, interval, status))
    overdue = [t for t, _, last, iv, _, _ in instruments if last + timedelta(days=iv) < today]
    print("overdue instruments: %d" % len(overdue))
    assert len(overdue) == 0  # DMM-207 due 2026-12-01, still current
    # as-found out-of-tolerance -> impact reckoning
    as_found, as_left = 103.2, 100.1
    in_tol = abs(as_found - nominal) <= nominal * tol if nominal else True
    print("PG-033 as-found %.1f vs nominal %.0f +/-%.0f%%: in tolerance %s" %
          (103.2, 100.0, 1.0, in_tol))
    assert not in_tol  # 3.2% error exceeds 1% tolerance
    measurements_since = 47
    print("measurements since last good calibration now suspect: %d" % measurements_since)
    assert measurements_since == 47
    # traceability chain depth
    chain = ["PG-033", "LAB-STD-07", "NMI-REF-02", "SI"]
    print("traceability chain depth: %d links" % (len(chain) - 1))
    assert len(chain) - 1 == 3
    print("rule: truth in measurement is truth in stewardship")
    print("OK: %s kept true measure" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_aer_audits(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # wall-to-wall: 250 on the list, plus the orphan hunt
    listed = 250
    matched, found_wrong, not_found = 241, 7, 2
    orphans = 3  # found tagged, no register row
    assert matched + found_wrong + not_found == listed
    match_rate = matched / listed * 100.0
    print("listed %d: matched %d, found-with-errors %d, ghosts %d" %
          (listed, matched, found_wrong, not_found))
    print("orphans (found, unrecorded): %d" % orphans)
    print("match rate: %.1f %%" % match_rate)
    assert 96.39 < match_rate < 96.41
    assert match_rate >= 90.0, "register untrustworthy below 90%"
    # cycle counting: rotating monthly sample covers the register yearly
    monthly_sample, months = 220, 12
    annual_coverage = monthly_sample * months
    print("cycle count coverage per year: %d asset-checks" % annual_coverage)
    assert annual_coverage == 2640
    # ghost investigation outcomes
    ghost_findings = {"transferred without paperwork": 1, "scrapped without form": 1}
    assert sum(ghost_findings.values()) == not_found
    print("ghost dispositions: %s" % ghost_findings)
    print("rule: the ledger laid beside the world - and the two asked to agree")
    print("OK: %s held the reckoning" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_aer_utilization(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # operating hours over available hours (planned downtime excluded)
    op_hours, avail_hours = 1320.0, 1760.0
    util = op_hours / avail_hours * 100.0
    print("utilization: %.0f / %.0f h = %.1f %%" % (op_hours, avail_hours, util))
    assert 74.99 < util < 75.01
    # band assignment
    def band(u):
        if u < 30: return "challenge"
        if u > 85: return "capacity warning"
        return "healthy"
    print("band: %s" % band(util))
    assert band(util) == "healthy"
    assert band(22.0) == "challenge" and band(94.0) == "capacity warning"
    # cost per operating hour: the value question
    annual_cost = 237600.0  # depreciation + maintenance + energy + insurance
    cpoh = annual_cost / op_hours
    print("annual cost $%.2f / %.0f h = $%.2f per operating hour" % (annual_cost, op_hours, cpoh))
    assert 179.99 < cpoh < 180.01
    # trend: climbing utilization warns of capacity pain
    trend = [61.0, 66.0, 71.0, 75.0]
    rising = all(b > a for a, b in zip(trend, trend[1:]))
    print("4-quarter trend %s rising: %s" % (trend, rising))
    assert rising
    print("rule: count the days honestly - challenge the idle, relieve the overburdened")
    print("OK: %s counted the days" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_aer_spare_parts(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # reorder point = daily usage * lead time + safety stock
    annual_usage, lead_days = 4.0, 30.0
    daily = annual_usage / 365.0
    safety = 1.0  # one unit of variability cover
    rop = daily * lead_days + safety
    print("seal kit: %.1f/yr, lead %d d -> reorder point %.2f" % (annual_usage, lead_days, rop))
    assert 1.32 < rop < 1.34
    # carrying vs stockout: the balance
    unit_cost, on_hand = 185.0, 3
    carrying_rate = 0.25
    carrying = unit_cost * on_hand * carrying_rate
    downtime_hr, stockout_prob = 5200.0, 0.15
    expected_stockout = downtime_hr * 8.0 * stockout_prob  # 8 h wait for emergency part
    print("carrying cost $%.2f/yr vs expected stockout cost $%.2f/yr" % (carrying, expected_stockout))
    assert 138.74 < carrying < 138.76
    assert 6239.99 < expected_stockout < 6240.01
    assert expected_stockout > carrying, "stocking is rational here"
    # criticality override: insurance spare stocked regardless of usage
    insurance_spare = {"usage_per_year": 0.1, "lead_weeks": 26, "critical": True}
    stock = 1 if insurance_spare["critical"] and insurance_spare["lead_weeks"] > 12 else 0
    print("turbine insurance spare stocked: %d (critical, 26-week lead)" % stock)
    assert stock == 1
    print("rule: providence on the shelf - the repair bought before the breaking")
    print("OK: %s stocked the mercy" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_aer_criticality(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # weighted consequence scoring, safety heaviest
    weights = {"safety": 0.35, "environment": 0.15, "production": 0.25, "cost": 0.15, "redundancy": 0.10}
    assets = {
        "BOILER-01": {"safety": 5, "environment": 4, "production": 5, "cost": 4, "redundancy": 5},
        "PUMP-114": {"safety": 2, "environment": 2, "production": 3, "cost": 2, "redundancy": 2},
        "FAN-022": {"safety": 1, "environment": 1, "production": 1, "cost": 1, "redundancy": 1},
    }
    def score(f):
        return sum(f[k] * weights[k] for k in weights)
    def rank(s):
        return "A" if s >= 4.0 else ("B" if s >= 2.5 else "C")
    ranked = {a: (score(f), rank(score(f))) for a, f in assets.items()}
    for a, (s, r) in ranked.items():
        print("  %-9s score %.2f rank %s" % (a, s, r))
    assert ranked["BOILER-01"][1] == "A"
    assert ranked["PUMP-114"][1] == "C"
    assert ranked["FAN-022"][1] == "C"
    assert 4.69 < ranked["BOILER-01"][0] < 4.71
    assert 2.24 < ranked["PUMP-114"][0] < 2.26
    # risk = criticality x likelihood per failure mode
    likelihood, controls = 3, "relief valve tested annually"
    risk = ranked["BOILER-01"][0] * likelihood
    print("BOILER-01 overpressure risk: %.2f x likelihood %d = %.2f (%s)" %
          (ranked["BOILER-01"][0], likelihood, risk, controls))
    assert 14.09 < risk < 14.11
    print("rule: weigh without flinching, keep according to the weight")
    print("OK: %s weighed the trusts" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_aer_baselines(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # baseline snapshot vs live state: the drift hunt
    baseline = {"firmware": "4.1.0", "setpoint_psi": 120, "program_rev": "C",
                "io_config": "16DI/8DO", "motor_amps_trip": 28.5}
    live = {"firmware": "4.2.1", "setpoint_psi": 120, "program_rev": "C",
            "io_config": "16DI/8DO", "motor_amps_trip": 31.0}
    authorized = {"firmware": "4.2.1"}  # approved change CHG-2091
    drift = {k: (baseline[k], live[k]) for k in baseline if baseline[k] != live[k]}
    print("drifted fields: %d" % len(drift))
    unauthorized = {k: v for k, v in drift.items() if k not in authorized}
    print("unauthorized: %s" % unauthorized)
    assert len(drift) == 2
    assert list(unauthorized.keys()) == ["motor_amps_trip"]
    # disposition: remediate the unauthorized back to baseline
    remediated = dict(live)
    remediated["motor_amps_trip"] = baseline["motor_amps_trip"]
    assert remediated["motor_amps_trip"] == 28.5
    print("remediated motor_amps_trip to baseline 28.5 A")
    # change history: the 2 a.m. read
    history = [("2025-06-02", "commissioned", "baseline A"),
               ("2026-04-18", "CHG-2091", "firmware 4.1.0 -> 4.2.1")]
    print("change history entries: %d" % len(history))
    assert len(history) == 2
    print("rule: what changed, and was the changing authorized")
    print("OK: %s remembered the face" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_aer_reliability(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # class-level, rolling 12 months: honest definitions
    op_hours, failures, repair_down = 40000.0, 20, 180.0
    mtbf = op_hours / failures
    mttr = repair_down / failures
    avail = mtbf / (mtbf + mttr) * 100.0
    print("MTBF %.0f h, MTTR %.1f h, availability %.3f %%" % (mtbf, mttr, avail))
    assert 1999.9 < mtbf < 2000.1
    assert 8.99 < mttr < 9.01
    assert 99.551 < avail < 99.553
    # target per criticality: A assets at 99.5%
    target = 99.5
    print("A-critical target %.1f %%: %s" % (target, "MET" if avail >= target else "MISSED"))
    assert avail >= target
    # fleet sizing from MTBF: 50 pumps, 8000 h/yr each
    fleet_failures = 50 * 8000.0 / mtbf
    seal_kits = fleet_failures * 1.0
    print("expected fleet failures/yr: %.0f -> seal kits to stock: %.0f" % (fleet_failures, seal_kits))
    assert 199.9 < fleet_failures < 200.1
    print("rule: count without flattery - fewer falls, swifter risings")
    print("OK: %s read the pulse" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_aer_tco(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # 10-year TCO: the iceberg under the purchase price
    r = 0.06
    price = 100000.0
    annual = {"energy": 8000.0, "maintenance": 5000.0, "downtime_risk": 3000.0}
    residual = 8000.0
    pv = price
    for yr in range(1, 11):
        pv += sum(annual.values()) / ((1 + r) ** yr)
    pv -= residual / ((1 + r) ** 10)
    undiscounted = price + sum(annual.values()) * 10 - residual
    print("10-yr TCO undiscounted: $%.2f" % undiscounted)
    print("10-yr TCO present value @6%%: $%.2f" % pv)
    print("purchase price share of undiscounted: %.1f %%" % (price / undiscounted * 100))
    assert 251999.99 < undiscounted < 252000.01
    assert 213293.0 < pv < 213296.0
    assert 39.6 < price / undiscounted * 100 < 39.8
    # keep vs replace: old asset's rising curve vs new machine
    old_next5 = [14000.0, 16500.0, 19500.0, 23000.0, 27000.0]
    new_annual_equiv = 18500.0
    keep_pv = sum(c / ((1 + r) ** (i + 1)) for i, c in enumerate(old_next5))
    new_pv = sum(new_annual_equiv / ((1 + r) ** (i + 1)) for i in range(5))
    print("keep 5-yr PV $%.2f vs replace 5-yr PV $%.2f -> %s" %
          (keep_pv, new_pv, "REPLACE" if new_pv < keep_pv else "KEEP"))
    assert 82658.0 < keep_pv < 82661.0
    assert 77927.0 < new_pv < 77930.0
    assert new_pv < keep_pv
    print("rule: count the whole weight, honestly summed and discounted")
    print("OK: %s weighed the iceberg" % NAME)
if __name__ == "__main__":
    main()
''')


DEMOS.update({
    "cmdb_records": demo_aer_cmdb_records,
    "work_orders": demo_aer_work_orders,
    "pm_scheduling": demo_aer_pm_scheduling,
    "warranty": demo_aer_warranty,
    "calibration": demo_aer_calibration,
    "audits": demo_aer_audits,
    "utilization": demo_aer_utilization,
    "spare_parts": demo_aer_spare_parts,
    "criticality": demo_aer_criticality,
    "baselines": demo_aer_baselines,
    "reliability": demo_aer_reliability,
    "tco": demo_aer_tco,
})


def demo_aer_iso55000(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # maturity self-assessment 0-5 per ISO 55001 clause, evidence-backed
    clauses = {
        "4 Context": 3, "5 Leadership": 4, "6 Planning": 3,
        "7 Support": 3, "8 Operation": 4, "9 Performance evaluation": 2,
        "10 Improvement": 2,
    }
    avg = sum(clauses.values()) / len(clauses)
    gaps = [k for k, v in clauses.items() if v < 3]
    print("clauses assessed: %d, maturity average: %.2f" % (len(clauses), avg))
    for k, v in clauses.items():
        print("  %-24s %d/5" % (k, v))
    print("gap clauses (<3): %s" % gaps)
    assert len(clauses) == 7
    assert 2.99 < avg < 3.01
    assert len(gaps) == 2
    # line of sight: objectives -> policy -> SAMP -> plans
    los = ["organizational objectives", "asset management policy",
           "strategic asset management plan", "per-class asset plans"]
    print("line of sight links: %d" % len(los))
    assert len(los) == 4
    print("rule: cost, risk, and performance in balance across the whole life")
    print("OK: %s walked the line of sight" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_aer_lease_vs_buy(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    r = 0.07
    # BUY: 120k now, 4k/yr maintenance, 25k residual at year 6
    buy_pv = 120000.0 + sum(4000.0 / ((1 + r) ** y) for y in range(1, 7)) \\
        - 25000.0 / ((1 + r) ** 6)
    # LEASE: 24500/yr payments, maintenance included, 3k return fee at end
    lease_pv = sum(24500.0 / ((1 + r) ** y) for y in range(1, 7)) \\
        + 3000.0 / ((1 + r) ** 6)
    print("buy  NPV @7%%: $%.2f" % buy_pv)
    print("lease NPV @7%%: $%.2f" % lease_pv)
    winner = "LEASE" if lease_pv < buy_pv else "BUY"
    print("winner: %s (saves $%.2f)" % (winner, abs(buy_pv - lease_pv)))
    assert 122406.0 < buy_pv < 122409.0
    assert 118000.0 < lease_pv < 119500.0
    assert lease_pv < buy_pv
    # end-of-term decision raised 12 months out
    from datetime import date
    lease_end = date(2029, 6, 30)
    decision_due = date(lease_end.year - 1, lease_end.month, lease_end.day)
    print("lease ends %s -> end-of-term decision due %s" % (lease_end, decision_due))
    assert decision_due == date(2028, 6, 30)
    print("rule: decide on economics - the off-balance-sheet motive is gone")
    print("OK: %s ran the duel" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_aer_health_scoring(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # weighted 0-100 health score, every weight declared
    weights = {"condition": 0.30, "failures": 0.25, "age": 0.20,
               "criticality": 0.15, "parts_risk": 0.10}
    assert abs(sum(weights.values()) - 1.0) < 1e-9
    assets = {
        "P-101": {"condition": 55, "failures": 40, "age": 30, "criticality": 90, "parts_risk": 70},
        "AHU-04": {"condition": 85, "failures": 90, "age": 75, "criticality": 50, "parts_risk": 90},
    }
    def score(f):
        return sum(f[k] * weights[k] for k in weights)
    def band(s):
        if s >= 80: return "healthy"
        if s >= 60: return "watch"
        if s >= 40: return "at risk - fund renewal"
        return "replace now"
    ranked = sorted(((a, score(f), band(score(f))) for a, f in assets.items()),
                    key=lambda x: x[1])
    for a, s, b in ranked:
        print("  %-6s score %5.1f -> %s" % (a, s, b))
    p101 = score(assets["P-101"])
    ahu = score(assets["AHU-04"])
    assert 52.9 < p101 < 53.1
    assert 79.4 < ahu < 79.6
    assert ranked[0][0] == "P-101" and ranked[0][2] == "at risk - fund renewal"
    # economic-life crossing: keeping cost vs replacement annuity
    keep_next_year, replace_annuity = 14200.0, 11800.0
    print("keep next year $%.2f vs replacement annuity $%.2f -> %s" %
          (keep_next_year, replace_annuity,
           "REPLACE" if keep_next_year > replace_annuity else "KEEP"))
    assert keep_next_year > replace_annuity
    print("rule: replace at the crossing - without sentimentality, without delay")
    print("OK: %s read the prognosis" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_aer_disposal(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # net recovery = proceeds - selling costs - sanitization - decommissioning
    proceeds, selling, sanit, decom = 12000.0, 800.0, 450.0, 1250.0
    net = proceeds - selling - sanit - decom
    print("resale $%.2f - selling $%.2f - sanitization $%.2f - decommission $%.2f" %
          (proceeds, selling, sanit, decom))
    print("net recovery: $%.2f" % net)
    assert 9499.99 < net < 9500.01
    # sanitization level matched to data classification (NIST SP 800-88)
    def sanitize_level(classification):
        return {"public": "clear", "internal": "purge",
                "confidential": "purge", "restricted": "destroy"}[classification]
    for cls, expect in [("public", "clear"), ("internal", "purge"), ("restricted", "destroy")]:
        assert sanitize_level(cls) == expect
    print("sanitization: public->clear, internal->purge, restricted->destroy")
    # disposal certificate: every thread closed
    cert = {"method": "resale", "date": "2026-10-02", "net": net,
            "sanitization_evidence": "CERT-8841", "manifests": ["HW-2210"],
            "authorized_by": "R. Okafor"}
    required = ["method", "date", "net", "sanitization_evidence", "manifests", "authorized_by"]
    complete = all(k in cert for k in required)
    print("disposal certificate complete: %s" % complete)
    assert complete
    # tag number retires forever
    retired_tags = {"AREG-2026-004178"}
    assert "AREG-2026-004178" in retired_tags
    print("rule: discharged with honor - certificate filed, name retired")
    print("OK: %s closed the book" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_aer_federation_discovery(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # reconciliation: staged discovery findings vs the CMDB web
    cmdb = {"SRV-01", "SRV-02", "LAP-101", "LAP-102", "SW-01"}
    discovered = {"SRV-01", "SRV-02", "SRV-03", "LAP-101", "SW-01", "PRN-09"}
    matched = cmdb & discovered
    new = discovered - cmdb        # unauthorized or forgotten
    missing = cmdb - discovered    # lost, off-network, or retired silently
    conflict = {"LAP-102"}          # attribute disagreement -> manual queue
    print("matched %d, new %d %s, missing %d %s, conflicts %d" %
          (len(matched), len(new), sorted(new), len(missing), sorted(missing), len(conflict)))
    assert len(matched) == 4
    assert new == {"SRV-03", "PRN-09"}
    assert missing == {"LAP-102"}
    truth = len(matched) / len(cmdb) * 100.0
    print("CMDB truth score: %.1f %%" % truth)
    assert 79.9 < truth < 80.1
    # identity resolution: serial -> tag -> finance id
    idmap = {"SN-88412": ("AREG-2026-004178", "FIN-55201")}
    resolved = idmap.get("SN-88412")
    print("SN-88412 resolves to tag %s / finance %s" % resolved)
    assert resolved == ("AREG-2026-004178", "FIN-55201")
    # every finding becomes a task
    tasks = len(new) + len(missing) + len(conflict)
    print("reconciliation tasks opened: %d" % tasks)
    assert tasks == 4
    print("rule: the council of witnesses, every disagreement worked")
    print("OK: %s weighed the testimonies" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_aer_insurance(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # schedule of values at replacement cost, rebuilt yearly
    schedule = [("Bldg A", 4200000.0), ("HVAC fleet", 1586000.0),
                ("vehicle fleet", 2688000.0), ("IT assets", 1912000.0)]
    total_insured = sum(v for _, v in schedule)
    rate_per_1000, deductible = 2.80, 25000.0
    premium = total_insured / 1000.0 * rate_per_1000
    print("schedule of values: $%.2f" % total_insured)
    print("premium @ $%.2f/1000: $%.2f, deductible $%.2f" % (rate_per_1000, premium, deductible))
    assert 10385999.99 < total_insured < 10386000.01
    assert 29080.79 < premium < 29080.81
    # expected loss vs premium: the rationality check
    loss_history = [("2023", 12000.0), ("2024", 0.0), ("2025", 31000.0)]
    avg_loss = sum(v for _, v in loss_history) / len(loss_history)
    print("3-yr average loss $%.2f vs premium $%.2f" % (avg_loss, premium))
    assert 14333.32 < avg_loss < 14333.34
    # underinsurance check: book value vs replacement cost
    book_value = 6100000.0
    coinsurance_pct = book_value / total_insured * 100.0
    print("book value is %.1f %% of replacement - coinsurance %s" %
          (coinsurance_pct, "AT RISK" if coinsurance_pct < 80 else "OK"))
    assert 58.7 < coinsurance_pct < 58.8
    # claim proof pack from the register
    proof = ["existence (register + audit 96.4%)", "value (schedule)",
             "care (maintenance history)", "photos before/after"]
    print("claim proof pack: %d items" % len(proof))
    assert len(proof) == 4
    print("rule: the backstop only holds if it was honestly built")
    print("OK: %s built the backstop" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_aer_data_quality(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # five dimensions, measured monthly per site
    n = 2500
    dims = {
        "completeness": 2410 / n * 100.0,   # required fields filled
        "accuracy": 96.4,                    # audit-verified true rate
        "uniqueness": (n - 6) / n * 100.0,   # 6 duplicate tag rows found
        "consistency": 2435 / n * 100.0,     # cross-field rules passing
        "timeliness": 2280 / n * 100.0,     # moves recorded same-day
    }
    for k, v in dims.items():
        print("  %-12s %5.1f %%" % (k, v))
    overall = sum(dims.values()) / len(dims)
    print("overall data quality: %.2f %%" % overall)
    assert 96.39 < dims["completeness"] < 96.41
    assert 99.75 < dims["uniqueness"] < 99.77
    assert 96.22 < overall < 96.24
    # duplicate detection on serial numbers
    serials = ["SN-1", "SN-2", "SN-1", "SN-3", "SN-2", "SN-4"]
    seen, dupes = set(), set()
    for s in serials:
        if s in seen:
            dupes.add(s)
        seen.add(s)
    print("duplicate serials detected: %s" % sorted(dupes))
    assert dupes == {"SN-1", "SN-2"}
    # scorecard behavior change: laggard site identified
    sites = {"DEN": 97.2, "AUS": 94.1, "HQ": 88.3}
    laggard = min(sites, key=sites.get)
    print("laggard site: %s at %.1f %%" % (laggard, sites[laggard]))
    assert laggard == "HQ"
    print("rule: measure what you claim - quality compounds like interest")
    print("OK: %s graded the ledger" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_aer_analytics_kpi(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the twelve dials, each with definition, target, trend, owner
    kpis = [
        ("asset count", 2480, 2500, "up"),
        ("replacement value $M", 10.39, 10.5, "up"),
        ("PM compliance %", 92.0, 90.0, "up"),
        ("reactive work %", 18.0, 20.0, "down"),
        ("maint cost % of repl value", 3.1, 4.0, "flat"),
        ("audit match %", 96.4, 95.0, "up"),
        ("A-critical with current condition %", 98.0, 100.0, "up"),
        ("warranty recovery $k", 41.5, 30.0, "up"),
    ]
    red = [k for k, v, t, tr in kpis
           if (v < t if k not in ("reactive work %", "maint cost % of repl value") else v > t)]
    print("KPIs on dashboard: %d, red dials: %d %s" % (len(kpis), len(red), red))
    assert len(red) == 3  # asset count, replacement value, A-critical condition
    # reactive ratio: emergency hours over total
    reactive = 18.0
    assert reactive <= 20.0
    # maintenance cost benchmark 2-4% of replacement value
    maint_pct = 3.1
    assert 2.0 <= maint_pct <= 4.0
    # lineage: every number traces to source rows
    lineage = {"PM compliance %": ["work_orders:50 due", "work_orders:46 on-time"]}
    assert len(lineage["PM compliance %"]) == 2
    print("lineage example: PM compliance 92%% <- 46/50 work orders")
    # monthly review: every red dial gets a named action with a date
    actions = {k: ("owner assigned", "2026-11-15") for k in red}
    print("red-dial actions assigned: %d" % len(actions))
    assert len(actions) == 3
    print("rule: definition, target, trend, owner - or it is trivia")
    print("OK: %s manned the watchtower" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_aer_fleet(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # one fleet view: utilization + cost per site, then the reallocation harvest
    fleet = [
        ("Site A loader L-07", 22.0, 18400.0),
        ("Site B loader L-12", 91.0, 17900.0),
        ("Site B rental spend", None, 14600.0),
    ]
    # move L-07 to Site B: kills the rental, utilization rebalances
    combined_op = 22.0 + 91.0  # percent-points of two loaders' capacity
    new_util_each = combined_op / 2
    saving = 14600.0  # rental eliminated
    print("reallocate L-07 A->B: each loader at %.1f %%, rental $%.2f/yr eliminated" %
          (new_util_each, saving))
    assert 56.4 < new_util_each < 56.6
    assert 14599.99 < saving < 14600.01
    # lifecycle conveyor: replacement trigger per class
    policy = {"sedan": (120000, 7), "pickup": (150000, 8), "forklift": (12000, 10)}
    vehicle = ("sedan", 118500, 6.8)
    trigger = policy[vehicle[0]]
    due = vehicle[1] >= trigger[0] or vehicle[2] >= trigger[1]
    print("sedan at %d mi / %.1f yr vs trigger %d mi / %d yr -> replacement %s" %
          (vehicle[1], vehicle[2], trigger[0], trigger[1], "DUE" if due else "not yet"))
    assert not due  # 118,500 < 120,000 and 6.8 < 7
    # chargeback: full monthly cost posted to the holding site
    monthly = (18400.0 + 17900.0) / 12
    print("monthly chargeback for the two loaders: $%.2f" % monthly)
    assert 3024.99 < monthly < 3025.01
    print("rule: many roofs, one ledger, one standard of care")
    print("OK: %s mustered the fleet" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_aer_registry_program(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    from datetime import date
    # phased build with gates: foundation -> pilot -> rollout -> operation
    phases = [
        ("foundation", date(2026, 11, 1), date(2027, 1, 31), "standards + charter"),
        ("pilot", date(2027, 2, 1), date(2027, 4, 30), "500 assets, 95% match gate"),
        ("rollout", date(2027, 5, 1), date(2027, 10, 31), "waves with audits"),
        ("operation", date(2027, 11, 1), date(2028, 10, 31), "PM/warranty/analytics live"),
    ]
    total_days = sum((e - s).days + 1 for _, s, e, _ in phases)
    print("program phases: %d, total calendar days: %d" % (len(phases), total_days))
    assert len(phases) == 4
    assert total_days == 731
    # pilot gate: match rate must clear 95%
    pilot_match = 96.4
    gate_pass = pilot_match >= 95.0
    print("pilot match %.1f %% -> gate: %s" % (pilot_match, "PASS" if gate_pass else "FIX FIRST"))
    assert gate_pass
    # record ramp: waves add assets, operation never re-enters bad data
    ramp = [0, 500, 2500, 2480 + 500]
    print("record ramp by phase end: %s" % ramp)
    assert ramp[-1] == 2980
    # victory condition: capital plan built from register data
    charter_metrics = ["audit match rate", "PM compliance", "maintenance cost trend",
                       "capital decisions from register"]
    print("charter metrics: %d" % len(charter_metrics))
    assert len(charter_metrics) == 4
    print("rule: prove each phase before the next - the ledger becomes an institution")
    print("OK: %s founded the keeping" % NAME)
if __name__ == "__main__":
    main()
''')


DEMOS.update({
    "iso55000": demo_aer_iso55000,
    "lease_vs_buy": demo_aer_lease_vs_buy,
    "health_scoring": demo_aer_health_scoring,
    "disposal": demo_aer_disposal,
    "federation_discovery": demo_aer_federation_discovery,
    "insurance": demo_aer_insurance,
    "data_quality": demo_aer_data_quality,
    "analytics_kpi": demo_aer_analytics_kpi,
    "fleet": demo_aer_fleet,
    "registry_program": demo_aer_registry_program,
})
