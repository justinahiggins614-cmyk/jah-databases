#!/usr/bin/env python3
"""PHASE D — Everything subject databases: real, runnable, stdlib-only demo
programs, one family per subject. Every demo is genuine computation over the
subject's own concepts and prints an "OK:" marker. Property of Justin Addam
Higgins (JAH).
"""
import json
import math


def _hdr(name, rid, group):
    return ('#!/usr/bin/env python3\n"""%s — working demonstration.\n'
            'Record %s [%s]. Property of Justin Addam Higgins (JAH).\n"""\n'
            % (name, rid, group))


def demo_math(name, rid, group, points, req):
    return _hdr(name, rid, group) + '''\
import math
def solve_quadratic(a, b, c):
    disc = b * b - 4 * a * c
    if disc < 0:
        return ()
    s = math.sqrt(disc)
    return ((-b + s) / (2 * a), (-b - s) / (2 * a))
def sieve(n):
    is_p = [True] * (n + 1)
    is_p[0] = is_p[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if is_p[i]:
            is_p[i*i:n+1:i] = [False] * len(range(i*i, n+1, i))
    return [i for i, p in enumerate(is_p) if p]
def main():
    roots = solve_quadratic(1, -5, 6)
    print("x^2 - 5x + 6 = 0 -> roots", roots)
    assert roots == (3.0, 2.0)
    primes = sieve(50)
    print("primes <= 50:", primes)
    assert primes == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
    print("OK: %s solved a quadratic and sieved primes" % ''' + json.dumps(name) + ''')
if __name__ == "__main__":
    main()
'''


def demo_physics(name, rid, group, points, req):
    return _hdr(name, rid, group) + '''\
import math
G = 9.80665
def projectile_range(v0, angle_deg):
    th = math.radians(angle_deg)
    return v0 * v0 * math.sin(2 * th) / G
def kinetic_energy(m, v):
    return 0.5 * m * v * v
def main():
    r = projectile_range(25.0, 45.0)
    print("v0=25 m/s @45deg -> range %.2f m" % r)
    assert abs(r - 63.73) < 0.1
    ke = kinetic_energy(2.0, 25.0)
    print("KE of 2 kg @25 m/s = %.1f J" % ke)
    assert abs(ke - 625.0) < 1e-9
    print("OK: %s computed real projectile and energy physics" % ''' + json.dumps(name) + ''')
if __name__ == "__main__":
    main()
'''


def demo_chem(name, rid, group, points, req):
    return _hdr(name, rid, group) + '''\
MASSES = {"H": 1.008, "C": 12.011, "N": 14.007, "O": 15.999, "Na": 22.990,
          "Cl": 35.45, "S": 32.06, "Ca": 40.078}
import re
def molar_mass(formula):
    total = 0.0
    for el, n in re.findall(r"([A-Z][a-z]?)(\\d*)", formula):
        total += MASSES[el] * (int(n) if n else 1)
    return total
def main():
    mm = molar_mass("H2SO4")
    print("molar mass H2SO4 = %.3f g/mol" % mm)
    assert abs(mm - 98.079) < 0.01
    mm2 = molar_mass("CaCl2")
    print("molar mass CaCl2 = %.3f g/mol" % mm2)
    assert abs(mm2 - 110.978) < 0.01
    print("OK: %s computed real molar masses" % ''' + json.dumps(name) + ''')
if __name__ == "__main__":
    main()
'''


def demo_bio(name, rid, group, points, req):
    return _hdr(name, rid, group) + '''\
"""SYNTHETIC SAMPLE SEQUENCE — real sequence statistics over a fabricated
sequence. Never real genetic data."""
import random
from collections import Counter
def gc_content(seq):
    c = Counter(seq)
    return (c["G"] + c["C"]) / len(seq)
def population_growth(n0, rate, generations):
    n = n0
    for _ in range(generations):
        n *= (1 + rate)
    return n
def main():
    rnd = random.Random(20261015)
    seq = "".join(rnd.choice("ACGT") for _ in range(5000))
    gc = gc_content(seq)
    print("length=%d GC=%.3f" % (len(seq), gc))
    assert abs(gc - 0.5) < 0.05
    pop = population_growth(100, 0.1, 10)
    print("100 organisms @10%%/gen for 10 gens -> %.1f" % pop)
    assert abs(pop - 259.37) < 0.1
    print("NOTE: synthetic sequence — real genomics needs reference alignment.")
    print("OK: %s ran real sequence and population math" % ''' + json.dumps(name) + ''')
if __name__ == "__main__":
    main()
'''


def demo_cs(name, rid, group, points, req):
    return _hdr(name, rid, group) + '''\
import random, time
def quicksort(a):
    if len(a) <= 1:
        return a
    p = a[len(a) // 2]
    return quicksort([x for x in a if x < p]) + [x for x in a if x == p] + quicksort([x for x in a if x > p])
def binary_search(a, x):
    lo, hi = 0, len(a) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if a[mid] == x:
            return mid
        lo, hi = (mid + 1, hi) if a[mid] < x else (lo, mid - 1)
    return -1
def main():
    rnd = random.Random(42)
    data = [rnd.randint(0, 100000) for _ in range(20000)]
    t0 = time.perf_counter()
    s = quicksort(data)
    dt = time.perf_counter() - t0
    assert s == sorted(data)
    print("quicksort 20,000 ints: %.3f s, verified sorted" % dt)
    idx = binary_search(s, s[12345])
    assert idx >= 0 and s[idx] == s[12345]
    assert binary_search(s, -1) == -1
    print("binary search: found index %d, miss -> -1" % idx)
    print("OK: %s ran real sorting and searching" % ''' + json.dumps(name) + ''')
if __name__ == "__main__":
    main()
'''


def demo_eng(name, rid, group, points, req):
    return _hdr(name, rid, group) + '''\
def cantilever_deflection(P, L, E, I):
    """Max deflection of a cantilever beam under tip load P (SI units)."""
    return P * L ** 3 / (3 * E * I)
def bending_stress(M, c, I):
    return M * c / I
def main():
    # steel beam: 2 m span, 10 kN tip load, E=200 GPa, I=8.33e-6 m^4
    d = cantilever_deflection(10000.0, 2.0, 200e9, 8.33e-6)
    print("cantilever deflection: %.4f m (%.1f mm)" % (d, d * 1000))
    assert abs(d - 0.016) < 0.002
    sig = bending_stress(20000.0, 0.1, 8.33e-6)
    print("bending stress: %.1f MPa" % (sig / 1e6))
    assert abs(sig / 1e6 - 240.1) < 1.0
    print("OK: %s computed real beam mechanics" % ''' + json.dumps(name) + ''')
if __name__ == "__main__":
    main()
'''


def demo_med(name, rid, group, points, req):
    return _hdr(name, rid, group) + '''\
"""EDUCATIONAL REFERENCE ONLY — not medical advice. Demonstrates standard
health-metric formulas used in wellness references."""
def bmi(weight_kg, height_m):
    return weight_kg / height_m ** 2
def bmi_class(v):
    if v < 18.5: return "Underweight"
    if v < 25.0: return "Healthy weight"
    if v < 30.0: return "Overweight"
    return "Obesity"
def target_hr_zone(age):
    hr_max = 220 - age
    return (0.5 * hr_max, 0.85 * hr_max)
def main():
    b = bmi(70.0, 1.75)
    print("BMI 70kg/1.75m = %.1f (%s)" % (b, bmi_class(b)))
    assert abs(b - 22.86) < 0.01 and bmi_class(b) == "Healthy weight"
    lo, hi = target_hr_zone(40)
    print("age 40 target HR zone: %.0f-%.0f bpm" % (lo, hi))
    assert (lo, hi) == (90.0, 153.0)
    print("NOTE: educational reference — consult a clinician for health decisions.")
    print("OK: %s computed real health metrics" % ''' + json.dumps(name) + ''')
if __name__ == "__main__":
    main()
'''


def demo_earth(name, rid, group, points, req):
    return _hdr(name, rid, group) + '''\
import math
def haversine_km(lat1, lon1, lat2, lon2):
    r = 6371.0
    p1, p2 = math.radians(lat1), math.radians(lat2)
    dp, dl = math.radians(lat2 - lat1), math.radians(lon2 - lon1)
    a = math.sin(dp/2)**2 + math.cos(p1)*math.cos(p2)*math.sin(dl/2)**2
    return 2 * r * math.asin(math.sqrt(a))
def richter_energy(magnitude):
    # Gutenberg-Richter energy estimate, joules
    return 10 ** (1.5 * magnitude + 4.8)
def main():
    d = haversine_km(40.7128, -74.0060, 51.5074, -0.1278)
    print("New York -> London: %.0f km" % d)
    assert 5500 < d < 5650
    e = richter_energy(6.0)
    print("M6.0 quake energy: %.2e J" % e)
    assert abs(e - 6.31e13) / 6.31e13 < 0.01
    print("OK: %s computed real earth-science quantities" % ''' + json.dumps(name) + ''')
if __name__ == "__main__":
    main()
'''


def demo_astro(name, rid, group, points, req):
    return _hdr(name, rid, group) + '''\
import math
MU_SUN = 1.32712440018e20  # m^3/s^2
AU = 1.495978707e11        # m
C = 299792458.0            # m/s
def orbital_period_days(semi_major_axis_m):
    return 2 * math.pi * math.sqrt(semi_major_axis_m ** 3 / MU_SUN) / 86400.0
def light_minutes(distance_m):
    return distance_m / C / 60.0
def main():
    t = orbital_period_days(AU)
    print("Earth orbital period from Kepler's 3rd law: %.2f days" % t)
    assert abs(t - 365.25) < 0.5
    mars_t = orbital_period_days(1.524 * AU)
    print("Mars orbital period: %.1f days" % mars_t)
    assert abs(mars_t - 687.0) < 2.0
    lm = light_minutes(AU)
    print("light travel time Sun->Earth: %.1f minutes" % lm)
    assert abs(lm - 8.3) < 0.1
    print("OK: %s computed real orbital mechanics" % ''' + json.dumps(name) + ''')
if __name__ == "__main__":
    main()
'''


def demo_econ(name, rid, group, points, req):
    return _hdr(name, rid, group) + '''\
def compound(principal, annual_rate, years, compounds_per_year=12):
    return principal * (1 + annual_rate / compounds_per_year) ** (compounds_per_year * years)
def loan_payment(principal, annual_rate, years):
    r = annual_rate / 12
    n = years * 12
    return principal * r / (1 - (1 + r) ** -n)
def main():
    v = compound(10000.0, 0.07, 10)
    print("$10,000 @7%% for 10y compounded monthly -> $%.2f" % v)
    assert abs(v - 20096.61) < 1.0
    pmt = loan_payment(300000.0, 0.06, 30)
    print("$300k mortgage @6%% 30y -> $%.2f/mo" % pmt)
    assert abs(pmt - 1798.65) < 0.5
    print("OK: %s computed real finance math" % ''' + json.dumps(name) + ''')
if __name__ == "__main__":
    main()
'''


def demo_psych(name, rid, group, points, req):
    return _hdr(name, rid, group) + '''\
"""SYNTHETIC SAMPLE DATA — real descriptive statistics over fabricated
research-style sample scores. No real participants."""
import random, statistics
def main():
    rnd = random.Random(20261015)
    group_a = [rnd.gauss(100.0, 15.0) for _ in range(200)]
    group_b = [rnd.gauss(108.0, 15.0) for _ in range(200)]
    ma, mb = statistics.mean(group_a), statistics.mean(group_b)
    sda, sdb = statistics.stdev(group_a), statistics.stdev(group_b)
    pooled = ((sda**2 + sdb**2) / 2) ** 0.5
    cohens_d = (mb - ma) / pooled
    print("A: n=200 mean=%.1f sd=%.1f" % (ma, sda))
    print("B: n=200 mean=%.1f sd=%.1f" % (mb, sdb))
    print("Cohen's d = %.2f" % cohens_d)
    assert abs(ma - 100) < 3 and abs(mb - 108) < 3
    assert 0.3 < cohens_d < 0.8
    print("NOTE: synthetic samples — real studies need preregistered methods.")
    print("OK: %s ran real descriptive statistics" % ''' + json.dumps(name) + ''')
if __name__ == "__main__":
    main()
'''


def demo_hist(name, rid, group, points, req):
    return _hdr(name, rid, group) + '''\
EVENTS = [
    ("Writing in Mesopotamia", -3200), ("Pyramids of Giza", -2560),
    ("Athens democracy", -508), ("Fall of Rome", 476),
    ("Printing press", 1440), ("Moon landing", 1969),
]
def span_years(a, b):
    return abs(b - a)
def main():
    ordered = sorted(EVENTS, key=lambda e: e[1])
    print("chronological order:")
    for label, yr in ordered:
        print("  %5d  %s" % (yr, label))
    assert ordered[0][1] == -3200 and ordered[-1][1] == 1969
    s = span_years(-3200, 1969)
    print("writing -> moon landing: %d years" % s)
    assert s == 5169
    print("OK: %s ordered and measured real historical spans" % ''' + json.dumps(name) + ''')
if __name__ == "__main__":
    main()
'''


def demo_geo(name, rid, group, points, req):
    return _hdr(name, rid, group) + '''\
import math
def population_density(pop, area_km2):
    return pop / area_km2
def haversine_km(lat1, lon1, lat2, lon2):
    r = 6371.0
    p1, p2 = math.radians(lat1), math.radians(lat2)
    dp, dl = math.radians(lat2 - lat1), math.radians(lon2 - lon1)
    a = math.sin(dp/2)**2 + math.cos(p1)*math.cos(p2)*math.sin(dl/2)**2
    return 2 * r * math.asin(math.sqrt(a))
def main():
    d = population_density(8_335_000, 783.8)
    print("NYC density: %.0f people/km^2" % d)
    assert 10000 < d < 11200
    dist = haversine_km(35.6762, 139.6503, -33.8688, 151.2093)
    print("Tokyo -> Sydney: %.0f km" % dist)
    assert 7750 < dist < 7900
    print("OK: %s computed real geographic quantities" % ''' + json.dumps(name) + ''')
if __name__ == "__main__":
    main()
'''


def demo_law(name, rid, group, points, req):
    return _hdr(name, rid, group) + '''\
"""EDUCATIONAL REFERENCE ONLY — demonstrates deadline arithmetic used in
legal practice. Not legal advice; rules vary by jurisdiction."""
import datetime
def add_calendar_days(start, days):
    return start + datetime.timedelta(days=days)
def add_business_days(start, days):
    d, added = start, 0
    while added < days:
        d += datetime.timedelta(days=1)
        if d.weekday() < 5:
            added += 1
    return d
def main():
    filing = datetime.date(2026, 10, 15)
    resp = add_calendar_days(filing, 30)
    print("30-day response deadline from 2026-10-15 -> %s" % resp)
    assert resp == datetime.date(2026, 11, 14)
    biz = add_business_days(filing, 10)
    print("10 business days from 2026-10-15 -> %s" % biz)
    assert biz == datetime.date(2026, 10, 29)
    print("NOTE: educational reference — deadlines depend on court rules.")
    print("OK: %s computed real deadline arithmetic" % ''' + json.dumps(name) + ''')
if __name__ == "__main__":
    main()
'''


def demo_phil(name, rid, group, points, req):
    return _hdr(name, rid, group) + '''\
def entails(premises, conclusion):
    """Brute-force propositional entailment over P, Q, R."""
    atoms = sorted({a for f in premises + [conclusion] for a in f if a.isupper()})
    def ev(f, val):
        stack = []
        for tok in f:
            if tok.isupper():
                stack.append(val[tok])
            elif tok == "~":
                stack.append(not stack.pop())
            else:
                b, a = stack.pop(), stack.pop()
                stack.append((a and b) if tok == "&" else ((not a) or b))
        return stack[0]
    for mask in range(2 ** len(atoms)):
        val = {a: bool(mask & (1 << i)) for i, a in enumerate(atoms)}
        if all(ev(p, val) for p in premises) and not ev(conclusion, val):
            return False, val
    return True, None
def main():
    # Modus ponens: P->Q, P |= Q   (tokens: P Q > means P implies Q)
    ok, ce = entails([["P", "Q", ">"], ["P"]], ["Q"])
    print("modus ponens valid:", ok)
    assert ok
    # Affirming the consequent is invalid: P->Q, Q |/= P
    ok2, ce2 = entails([["P", "Q", ">"], ["Q"]], ["P"])
    print("affirming the consequent valid:", ok2, "| counterexample:", ce2)
    assert not ok2
    print("OK: %s checked real argument validity" % ''' + json.dumps(name) + ''')
if __name__ == "__main__":
    main()
'''


def demo_ling(name, rid, group, points, req):
    return _hdr(name, rid, group) + '''\
import re
from collections import Counter
SAMPLE = ("Language carries meaning through sound and structure. "
          "Speakers learn patterns; patterns shape language. "
          "Every language organizes sound, word, and sentence.")
def flesch_kincaid_grade(text):
    words = re.findall(r"[a-zA-Z']+", text)
    sents = [s for s in re.split(r"[.!?]+", text) if s.strip()]
    syll = sum(max(1, len(re.findall(r"[aeiouy]+", w.lower()))) for w in words)
    return 0.39 * len(words) / len(sents) + 11.8 * syll / len(words) - 15.59
def main():
    words = re.findall(r"[a-z]+", SAMPLE.lower())
    freq = Counter(words)
    print("tokens=%d types=%d" % (len(words), len(freq)))
    for w, c in freq.most_common(4):
        print("  %-10s %d" % (w, c))
    assert freq["language"] == 3
    g = flesch_kincaid_grade(SAMPLE)
    print("Flesch-Kincaid grade: %.1f" % g)
    assert 0 < g < 20
    print("OK: %s ran real linguistic text analysis" % ''' + json.dumps(name) + ''')
if __name__ == "__main__":
    main()
'''


def demo_artmusic(name, rid, group, points, req):
    return _hdr(name, rid, group) + '''\
NOTES = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
MAJOR_STEPS = [2, 2, 1, 2, 2, 2, 1]
def major_scale(root):
    idx = NOTES.index(root)
    scale, pos = [root], idx
    for step in MAJOR_STEPS:
        pos = (pos + step) % 12
        scale.append(NOTES[pos])
    return scale
def complement(hexcolor):
    r = 255 - int(hexcolor[1:3], 16)
    g = 255 - int(hexcolor[3:5], 16)
    b = 255 - int(hexcolor[5:7], 16)
    return "#%02X%02X%02X" % (r, g, b)
def main():
    sc = major_scale("G")
    print("G major:", sc)
    assert sc == ["G", "A", "B", "C", "D", "E", "F#", "G"]
    comp = complement("#1E5AA8")
    print("complement of #1E5AA8 ->", comp)
    assert comp == "#E1A557"
    print("OK: %s built a real scale and color complement" % ''' + json.dumps(name) + ''')
if __name__ == "__main__":
    main()
'''


def demo_edu(name, rid, group, points, req):
    return _hdr(name, rid, group) + '''\
def weighted_grade(items):
    """items: list of (score, weight); weights sum to 1."""
    return sum(s * w for s, w in items)
def letter(g):
    for cut, L in ((90, "A"), (80, "B"), (70, "C"), (60, "D")):
        if g >= cut:
            return L
    return "F"
def spaced_repetition_intervals(n=5):
    iv, out = 1, []
    for _ in range(n):
        out.append(iv)
        iv = int(iv * 2.5) or iv + 1
    return out
def main():
    g = weighted_grade([(92, 0.4), (85, 0.3), (78, 0.2), (95, 0.1)])
    print("weighted grade: %.1f (%s)" % (g, letter(g)))
    assert abs(g - 87.4) < 0.01 and letter(g) == "B"
    iv = spaced_repetition_intervals(5)
    print("review intervals (days):", iv)
    assert iv[0] == 1 and all(b > a for a, b in zip(iv, iv[1:]))
    print("OK: %s computed real education metrics" % ''' + json.dumps(name) + ''')
if __name__ == "__main__":
    main()
'''


def demo_agri(name, rid, group, points, req):
    return _hdr(name, rid, group) + '''\
def yield_estimate(plants_per_ha, ears_per_plant, kernels_per_ear, kernel_g):
    kernels = plants_per_ha * ears_per_plant * kernels_per_ear
    return kernels * kernel_g / 1e6  # tonnes per hectare
def irrigation_mm(area_ha, depth_mm):
    # 1 mm over 1 ha = 10 m^3
    return area_ha * depth_mm * 10.0
def main():
    y = yield_estimate(75000, 1.0, 500, 0.30)
    print("maize yield estimate: %.2f t/ha" % y)
    assert abs(y - 11.25) < 0.01
    w = irrigation_mm(40.0, 25.0)
    print("40 ha @25 mm -> %.0f m^3 water" % w)
    assert w == 10000.0
    print("OK: %s computed real agronomy estimates" % ''' + json.dumps(name) + ''')
if __name__ == "__main__":
    main()
'''


def demo_energy(name, rid, group, points, req):
    return _hdr(name, rid, group) + '''\
def electricity_cost(kwh, rate_per_kwh):
    return kwh * rate_per_kwh
def solar_daily_kwh(panel_kw, sun_hours, efficiency=0.85):
    return panel_kw * sun_hours * efficiency
def co2_avoided_kg(kwh, grid_factor=0.4):
    return kwh * grid_factor
def main():
    cost = electricity_cost(900.0, 0.17)
    print("900 kWh @ $0.17/kWh -> $%.2f" % cost)
    assert abs(cost - 153.0) < 1e-9
    gen = solar_daily_kwh(8.0, 5.2)
    print("8 kW array, 5.2 sun-hours -> %.1f kWh/day" % gen)
    assert abs(gen - 35.36) < 0.01
    co2 = co2_avoided_kg(gen * 365)
    print("annual CO2 avoided: %.0f kg" % co2)
    assert co2 > 5000
    print("OK: %s computed real energy quantities" % ''' + json.dumps(name) + ''')
if __name__ == "__main__":
    main()
'''


DEMOS = {
    "math": demo_math, "physics": demo_physics, "chem": demo_chem,
    "bio": demo_bio, "cs": demo_cs, "eng": demo_eng, "med": demo_med,
    "earth": demo_earth, "astro": demo_astro, "econ": demo_econ,
    "psych": demo_psych, "hist": demo_hist, "geo": demo_geo,
    "law": demo_law, "phil": demo_phil, "ling": demo_ling,
    "artmusic": demo_artmusic, "edu": demo_edu, "agri": demo_agri,
    "energy": demo_energy,
}
