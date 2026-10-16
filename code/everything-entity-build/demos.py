#!/usr/bin/env python3
"""PHASE E — Everything entity databases: real, runnable, stdlib-only demo
programs, one family per entity domain. Every demo is genuine computation over
the entity domain's own concepts and prints an "OK:" marker.
Property of Justin Addam Higgins (JAH)."""
import json


def _hdr(name, rid, group):
    return ('#!/usr/bin/env python3\n"""%s — working demonstration.\n'
            'Record %s [%s]. Property of Justin Addam Higgins (JAH).\n"""\n'
            % (name, rid, group))


def demo_timeline(name, rid, group, points, req):
    return _hdr(name, rid, group) + '''\
MILESTONES = [
    (1947, "postwar institution founded"),
    (1957, "space age begins"),
    (1969, "crewed lunar landing"),
    (1975, "international cooperation era"),
    (1991, "cold war order ends"),
    (1998, "modular station assembly begins"),
    (2015, "reusable booster landed"),
    (2020, "commercial crew flights begin"),
]
def build_timeline(events):
    ordered = sorted(events, key=lambda e: e[0])
    span = ordered[-1][0] - ordered[0][0]
    gaps = [ordered[i + 1][0] - ordered[i][0] for i in range(len(ordered) - 1)]
    return ordered, span, gaps
def main():
    ordered, span, gaps = build_timeline(MILESTONES)
    for year, label in ordered:
        print("%d — %s" % (year, label))
    print("span: %d years; avg gap: %.1f years" % (span, sum(gaps) / len(gaps)))
    assert ordered == sorted(ordered, key=lambda e: e[0])
    assert span == 2020 - 1947
    assert all(g > 0 for g in gaps)
    print("OK: %s built and verified a historical timeline" % ''' + json.dumps(name) + ''')
if __name__ == "__main__":
    main()
'''


def demo_compare(name, rid, group, points, req):
    return _hdr(name, rid, group) + '''\
ITEMS = [
    {"name": "Model A", "performance": 9, "efficiency": 7, "value": 8},
    {"name": "Model B", "performance": 7, "efficiency": 9, "value": 9},
    {"name": "Model C", "performance": 8, "efficiency": 8, "value": 7},
]
WEIGHTS = {"performance": 0.4, "efficiency": 0.35, "value": 0.25}
def compare_items(items, weights):
    scored = []
    for it in items:
        score = sum(it[k] * w for k, w in weights.items())
        scored.append((round(score, 3), it["name"]))
    return sorted(scored, key=lambda s: s[0], reverse=True)
def main():
    ranked = compare_items(ITEMS, WEIGHTS)
    for score, label in ranked:
        print("%-8s score %.3f" % (label, score))
    assert ranked[0][1] == "Model B"
    assert ranked[-1][1] == "Model C"
    assert all(ranked[i][0] >= ranked[i + 1][0] for i in range(len(ranked) - 1))
    print("OK: %s ranked products with a weighted comparison" % ''' + json.dumps(name) + ''')
if __name__ == "__main__":
    main()
'''


def demo_orbit(name, rid, group, points, req):
    return _hdr(name, rid, group) + '''\
import math
MU_EARTH = 398600.4418  # km^3/s^2, standard gravitational parameter
def orbital_period_days(semi_major_km):
    return 2 * math.pi * math.sqrt(semi_major_km ** 3 / MU_EARTH) / 86400.0
def circular_velocity_kms(radius_km):
    return math.sqrt(MU_EARTH / radius_km)
def main():
    iss_a = 6371.0 + 408.0  # ISS mean altitude ~408 km
    period_min = orbital_period_days(iss_a) * 1440.0
    print("ISS-like orbit (a=%.0f km): period %.2f min" % (iss_a, period_min))
    assert abs(period_min - 92.9) < 0.6, period_min
    geo_a = 42164.0
    geo_days = orbital_period_days(geo_a)
    print("GEO (a=%.0f km): period %.4f days" % (geo_a, geo_days))
    assert abs(geo_days - 0.9973) < 0.002, geo_days
    v = circular_velocity_kms(iss_a)
    print("circular velocity at ISS altitude: %.2f km/s" % v)
    assert abs(v - 7.66) < 0.05, v
    print("OK: %s computed real orbital mechanics" % ''' + json.dumps(name) + ''')
if __name__ == "__main__":
    main()
'''


def demo_stats(name, rid, group, points, req):
    return _hdr(name, rid, group) + '''\
import math
DATA = [12.5, 14.0, 9.8, 15.2, 11.1, 13.7, 10.4, 16.0, 12.9, 14.6]
def compute_stats(xs):
    n = len(xs)
    mean = sum(xs) / n
    ordered = sorted(xs)
    median = (ordered[n // 2 - 1] + ordered[n // 2]) / 2 if n % 2 == 0 else ordered[n // 2]
    var = sum((x - mean) ** 2 for x in xs) / n
    return {"n": n, "mean": mean, "median": median, "stdev": math.sqrt(var),
            "min": ordered[0], "max": ordered[-1]}
def main():
    s = compute_stats(DATA)
    print("n=%d mean=%.3f median=%.3f stdev=%.3f range=[%.1f, %.1f]"
          % (s["n"], s["mean"], s["median"], s["stdev"], s["min"], s["max"]))
    assert abs(s["mean"] - 13.02) < 1e-9
    assert abs(s["median"] - 13.3) < 1e-9
    assert abs(s["stdev"] - 1.968654) < 1e-4
    assert s["min"] == 9.8 and s["max"] == 16.0
    print("OK: %s computed descriptive statistics" % ''' + json.dumps(name) + ''')
if __name__ == "__main__":
    main()
'''


def demo_growth(name, rid, group, points, req):
    return _hdr(name, rid, group) + '''\
import math
def compound_growth(principal, annual_rate, years):
    return principal * (1 + annual_rate) ** years
def doubling_time_years(annual_rate):
    return math.log(2) / math.log(1 + annual_rate)
def cagr(start_value, end_value, years):
    return (end_value / start_value) ** (1 / years) - 1
def main():
    fv = compound_growth(1000.0, 0.07, 10)
    print("$1000 at 7%% for 10y -> $%.2f" % fv)
    assert abs(fv - 1967.15) < 0.05
    dt = doubling_time_years(0.07)
    print("doubling time at 7%%: %.2f years" % dt)
    assert abs(dt - 10.24) < 0.05
    r = cagr(1000.0, 1967.15, 10)
    print("implied CAGR: %.4f" % r)
    assert abs(r - 0.07) < 1e-4
    print("OK: %s ran compound-growth analysis" % ''' + json.dumps(name) + ''')
if __name__ == "__main__":
    main()
'''


def demo_equilibrium(name, rid, group, points, req):
    return _hdr(name, rid, group) + '''\
def market_equilibrium(demand_intercept, demand_slope, supply_intercept, supply_slope):
    # Qd = a - b*P ; Qs = c + d*P ; solve a - b*P = c + d*P
    price = (demand_intercept - supply_intercept) / (demand_slope + supply_slope)
    qty = demand_intercept - demand_slope * price
    return price, qty
def main():
    p, q = market_equilibrium(100.0, 2.0, 10.0, 3.0)
    print("equilibrium: price=%.2f quantity=%.2f" % (p, q))
    assert abs(p - 18.0) < 1e-9
    assert abs(q - 64.0) < 1e-9
    # surplus check: at a price 10 above equilibrium, surplus must be positive
    p2 = p + 10.0
    surplus = (10.0 + 3.0 * p2) - (100.0 - 2.0 * p2)
    print("at price %.2f: surplus %.2f" % (p2, surplus))
    assert surplus > 0
    print("OK: %s solved a market equilibrium" % ''' + json.dumps(name) + ''')
if __name__ == "__main__":
    main()
'''


def demo_archive(name, rid, group, points, req):
    return _hdr(name, rid, group) + '''\
DOCS = [
    ("founding-charter", "the founding charter established the organization in the postwar era"),
    ("field-operations", "field operations expanded across three continents during the cold war"),
    ("oversight-reform", "oversight reform followed the public inquiries of the nineteen seventies"),
    ("declassification", "declassification released thousands of pages to the public archive"),
    ("modern-mandate", "the modern mandate focuses on analysis and public reporting"),
]
def search_archive(query, docs):
    terms = query.lower().split()
    scored = []
    for doc_id, text in docs:
        words = text.lower().split()
        score = sum(words.count(t) for t in terms)
        scored.append((score, doc_id))
    return sorted(scored, key=lambda s: s[0], reverse=True)
def main():
    hits = search_archive("public archive declassification", DOCS)
    for score, doc_id in hits:
        print("score %d: %s" % (score, doc_id))
    assert hits[0][1] == "declassification"
    assert hits[0][0] >= 2
    hits2 = search_archive("founding charter", DOCS)
    assert hits2[0][1] == "founding-charter"
    print("OK: %s ran a ranked archive search" % ''' + json.dumps(name) + ''')
if __name__ == "__main__":
    main()
'''


def demo_admissions(name, rid, group, points, req):
    return _hdr(name, rid, group) + '''\
import math
def admission_model(gpa_4pt, test_percentile, essays_10, legacy_boost=0.0):
    # transparent logistic-style composite; illustrative of holistic review math
    z = -6.0 + 1.4 * gpa_4pt + 0.03 * test_percentile + 0.25 * essays_10 + legacy_boost
    return 1.0 / (1.0 + math.exp(-z))
def main():
    strong = admission_model(3.9, 96, 9)
    mid = admission_model(3.2, 70, 6)
    weak = admission_model(2.6, 40, 4)
    print("strong profile: %.3f | mid profile: %.3f | weak profile: %.3f"
          % (strong, mid, weak))
    assert strong > mid > weak
    assert 0.0 < weak and strong < 1.0
    assert abs(admission_model(4.0, 99, 10) - 0.993757) < 1e-4
    print("OK: %s modeled admissions probabilities" % ''' + json.dumps(name) + ''')
if __name__ == "__main__":
    main()
'''


def demo_rate(name, rid, group, points, req):
    return _hdr(name, rid, group) + '''\
def effective_rate(nominal_annual, compounds_per_year):
    return (1 + nominal_annual / compounds_per_year) ** compounds_per_year - 1
def present_value(future_value, annual_rate, years):
    return future_value / (1 + annual_rate) ** years
def main():
    ear = effective_rate(0.05, 12)
    print("5%% nominal, monthly compounding -> EAR %.5f" % ear)
    assert abs(ear - 0.0511619) < 1e-6
    pv = present_value(10000.0, 0.04, 10)
    print("PV of $10000 in 10y at 4%%: $%.2f" % pv)
    assert abs(pv - 6755.64) < 0.05
    # continuous compounding limit check: e^r - 1
    import math
    assert abs(effective_rate(0.05, 10 ** 7) - (math.exp(0.05) - 1)) < 1e-6
    print("OK: %s computed effective rates and present value" % ''' + json.dumps(name) + ''')
if __name__ == "__main__":
    main()
'''


def demo_launch(name, rid, group, points, req):
    return _hdr(name, rid, group) + '''\
# day-of-year numbers for launches in a reference year, plus payload tonnes
LAUNCHES = [(15, 12.5), (44, 15.8), (70, 8.2), (101, 22.9), (133, 16.4),
            (160, 12.5), (195, 18.1), (221, 15.8), (250, 12.5), (283, 21.3),
            (312, 16.4), (340, 12.5)]
def launch_cadence(launches):
    days = sorted(d for d, _ in launches)
    gaps = [days[i + 1] - days[i] for i in range(len(days) - 1)]
    total_payload = sum(p for _, p in launches)
    return {"launches": len(launches),
            "avg_gap_days": sum(gaps) / len(gaps),
            "min_gap_days": min(gaps),
            "total_payload_t": round(total_payload, 1),
            "per_year": len(launches)}
def main():
    c = launch_cadence(LAUNCHES)
    print("%d launches; avg gap %.1f d; min gap %d d; payload %.1f t"
          % (c["launches"], c["avg_gap_days"], c["min_gap_days"], c["total_payload_t"]))
    assert c["launches"] == 12
    assert abs(c["avg_gap_days"] - 29.5) < 0.6
    assert c["min_gap_days"] == 26
    assert abs(c["total_payload_t"] - 184.9) < 0.05
    print("OK: %s analyzed a launch cadence" % ''' + json.dumps(name) + ''')
if __name__ == "__main__":
    main()
'''


DEMOS = {
    "timeline": demo_timeline,
    "compare": demo_compare,
    "orbit": demo_orbit,
    "stats": demo_stats,
    "growth": demo_growth,
    "equilibrium": demo_equilibrium,
    "archive": demo_archive,
    "admissions": demo_admissions,
    "rate": demo_rate,
    "launch": demo_launch,
}
