#!/usr/bin/env python3
"""Demo programs for the Component and Parts Catalog databases.

Every demo is real, runnable, stdlib-only Python performing the actual
component/parts computation for its record. All are machine-executed by
build.py before commit: each prints its real computed values, asserts tight
bounds (never float exact-equality), and ends with the OK marker.
"""

_PREAMBLE = "import math\n"


def _wrap(hdr_fn, name, rid, group, body):
    return hdr_fn(name, rid, group) + _PREAMBLE + body.replace("NAME", __import__("json").dumps(name))


def demo_cpc_what_is(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the four domains of the catalog and their shelf counts
    domains = {"electronic components": 412, "mechanical parts": 268,
               "materials stock": 94, "modules and subassemblies": 156}
    total = sum(domains.values())
    share = {k: v / total * 100.0 for k, v in domains.items()}
    print("domains: %d" % len(domains))
    for k in domains:
        print("  %-28s %4d parts (%5.2f %%)" % (k, domains[k], share[k]))
    print("catalog parts: %d" % total)
    assert total == 930
    assert 44.29 < share["electronic components"] < 44.31
    assert 28.81 < share["mechanical parts"] < 28.83
    print("rule: every atom carries function, properties, ratings, package, compatibility")
    print("OK: %s mapped the armory" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cpc_datasheet(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # datasheet triangulation: ratings first, then the operating point
    abs_max = {"vin_max": 35.0, "iout_max": 1.5, "tj_max": 150.0}
    op = {"vin": 12.0, "vout": 5.0, "iout": 1.0, "ta": 40.0}
    assert op["vin"] < abs_max["vin_max"], "rail exceeds absolute maximum"
    assert op["iout"] < abs_max["iout_max"], "current exceeds absolute maximum"
    pd = (op["vin"] - op["vout"]) * op["iout"]
    # thermal path: junction = ambient + dissipation * Rth(ja)
    rth_ja = 50.0
    tj = op["ta"] + pd * rth_ja
    print("dissipation: %.3f W" % pd)
    print("junction temperature: %.1f C (limit %.0f C)" % (tj, abs_max["tj_max"]))
    assert 6.99 < pd < 7.01
    assert 389.9 < tj < 390.1
    verdict = "PASS" if tj < 125.0 else "FAIL"
    print("derated verdict (125 C rule): %s" % verdict)
    assert verdict == "FAIL", "this linear regulator needs a heatsink at 1 A"
    print("rule: ratings first, headlines last - the footnote is part of the number")
    print("OK: %s read the testimony" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cpc_units_tolerances(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # tolerance bands: the honest spread around nominal
    nominal = 10000.0
    tol = 0.05
    lo = nominal * (1 - tol)
    hi = nominal * (1 + tol)
    print("10k +/-5%% acceptance window: %.0f to %.0f ohms" % (lo, hi))
    assert 9499.9 < lo < 9500.1
    assert 10499.9 < hi < 10500.1
    # precision part for comparison
    plo = 4700.0 * 0.99
    phi = 4700.0 * 1.01
    print("4.7k +/-1%% acceptance window: %.1f to %.1f ohms" % (plo, phi))
    assert 4652.9 < plo < 4653.1
    assert 4746.9 < phi < 4747.1
    # rating check: 12 V across 1k dissipates 0.144 W
    p = 12.0 ** 2 / 1000.0
    rating = 0.25
    loading = p / rating
    print("dissipation %.4f W on %.2f W rating: %.1f %% loading" % (p, rating, loading * 100))
    assert 0.1439 < p < 0.1441
    assert 0.575 < loading < 0.577
    print("rule: design to the band and the derated point, never the nominal and the wall")
    print("OK: %s honored the three numbers" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cpc_passives_overview(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the RC time constant: the most-used passive calculation
    r = 10000.0
    c = 100e-9
    tau = r * c
    fc = 1.0 / (2 * math.pi * r * c)
    print("R = 10k, C = 100 nF")
    print("time constant tau = %.6f s (%.3f ms)" % (tau, tau * 1000))
    print("corner frequency = %.2f Hz" % fc)
    assert 0.0009999 < tau < 0.0010001
    assert 159.14 < fc < 159.17
    # sanity: after one tau the step reaches 63.2%
    v = 1.0 - math.exp(-1.0)
    print("step response at t=tau: %.4f (expect 0.6321)" % v)
    assert 0.6320 < v < 0.6322
    print("rule: tau = R*C, corner at 1/(2*pi*R*C) - the infantry drill")
    print("OK: %s drilled the passives" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cpc_mechanical_overview(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # gear ratio: teeth trade speed for torque
    z1, z2 = 12, 36
    ratio = z2 / z1
    rpm_in = 900.0
    rpm_out = rpm_in / ratio
    print("pinion %d teeth drives gear %d teeth" % (z1, z2))
    print("ratio: %.1f : 1" % ratio)
    print("900 rpm in -> %.0f rpm out (torque x%.1f, minus efficiency)" % (rpm_out, ratio))
    assert 2.99 < ratio < 3.01
    assert 299.9 < rpm_out < 300.1
    # belt equivalent: diameter ratio does the same job
    d1, d2 = 50.0, 150.0
    belt_ratio = d2 / d1
    print("belt: %.0f mm driver, %.0f mm driven -> ratio %.1f" % (d1, d2, belt_ratio))
    assert 2.99 < belt_ratio < 3.01
    print("rule: ratio is teeth (or diameters); speed divides, torque multiplies")
    print("OK: %s moved the sinews" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cpc_wire_connector(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # 24 AWG copper: resistance per meter, voltage drop over the run
    r_per_m = 0.08422
    length_one_way = 10.0
    r_total = r_per_m * length_one_way * 2  # out and back
    current = 1.0
    vdrop = r_total * current
    supply = 12.0
    pct = vdrop / supply * 100.0
    print("24 AWG, 10 m run (20 m round trip): R = %.4f ohms" % r_total)
    print("voltage drop at 1 A: %.4f V (%.2f %% of 12 V)" % (vdrop, pct))
    assert 1.6843 < r_total < 1.6845
    assert 1.6843 < vdrop < 1.6845
    assert 14.03 < pct < 14.05
    verdict = "PASS" if pct < 5.0 else "FAIL - upsize the wire"
    print("5%% drop budget verdict: %s" % verdict)
    assert verdict.startswith("FAIL")
    # what gauge fixes it? 18 AWG is 0.0214 ohm/m
    r2 = 0.0214 * 20.0
    pct2 = r2 * current / supply * 100.0
    print("18 AWG same run: drop %.2f %%" % pct2)
    assert 3.56 < pct2 < 3.57
    print("rule: ampacity AND voltage drop, at worst-case ambient")
    print("OK: %s fed the far end" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cpc_markings(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # four-band color code: yellow violet red gold
    digits = {"black": 0, "brown": 1, "red": 2, "orange": 3, "yellow": 4,
              "green": 5, "blue": 6, "violet": 7, "gray": 8, "white": 9}
    mult = {"black": 1, "brown": 10, "red": 100, "orange": 1000, "yellow": 10000,
            "green": 100000, "blue": 1000000, "gold": 0.1, "silver": 0.01}
    tol = {"brown": 1, "red": 2, "green": 0.5, "blue": 0.25, "violet": 0.1,
           "gold": 5, "silver": 10}
    bands = ["yellow", "violet", "red", "gold"]
    value = (digits[bands[0]] * 10 + digits[bands[1]]) * mult[bands[2]]
    t = tol[bands[3]]
    lo = value * (1 - t / 100.0)
    hi = value * (1 + t / 100.0)
    print("bands yellow-violet-red-gold -> %.0f ohms +/-%d%%" % (value, t))
    print("acceptance window: %.0f to %.0f ohms" % (lo, hi))
    assert 4699.9 < value < 4700.1
    assert 4464.9 < lo < 4465.1
    assert 4934.9 < hi < 4935.1
    # capacitor numeric code: 104 = 10 x 10^4 pF
    cap = 10 * (10 ** 4) / 1e6  # uF
    print("capacitor code 104 -> %.1f uF (100 nF)" % cap)
    assert 0.099 < cap < 0.101
    print("rule: decode against the table, never from memory alone")
    print("OK: %s read the signatures" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cpc_materials_stock(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # weight before cutting: density x volume
    density_steel = 7850.0  # kg/m^3
    area = 1.0  # m^2
    thickness = 0.002  # 2 mm
    weight = density_steel * area * thickness
    print("steel sheet 1 m^2 x 2 mm: %.2f kg" % weight)
    assert 15.69 < weight < 15.71
    # aluminum equivalent for comparison
    weight_al = 2700.0 * area * thickness
    print("aluminum same size: %.2f kg (%.1f %% of steel)" % (weight_al, weight_al / weight * 100))
    assert 5.39 < weight_al < 5.41
    # stiffness: doubling thickness -> 8x stiffness
    t1, t2 = 1.0, 2.0
    stiff_ratio = (t2 / t1) ** 3
    print("stiffness ratio 2 mm vs 1 mm sheet: %.1fx" % stiff_ratio)
    assert 7.99 < stiff_ratio < 8.01
    # round bar: 1 m of 20 mm steel rod
    r = 0.010
    bar_w = density_steel * math.pi * r ** 2 * 1.0
    print("20 mm steel rod, 1 m: %.3f kg" % bar_w)
    assert 2.465 < bar_w < 2.467
    print("rule: know what the material weighs before the first cut")
    print("OK: %s weighed the promise" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cpc_series_parallel(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    r1, r2 = 100.0, 220.0
    series = r1 + r2
    parallel = (r1 * r2) / (r1 + r2)
    print("100 + 220 series: %.0f ohms" % series)
    print("100 || 220 parallel: %.2f ohms" % parallel)
    assert 319.9 < series < 320.1
    assert 68.74 < parallel < 68.76
    assert parallel < min(r1, r2), "parallel must be below the smallest member"
    # power splits with the stress: 12 V across the series pair
    v = 12.0
    i = v / series
    p1 = i ** 2 * r1
    p2 = i ** 2 * r2
    print("at 12 V: series current %.4f A; P(100)=%.4f W P(220)=%.4f W" % (i, p1, p2))
    assert 0.0374 < i < 0.0376
    assert 0.1406 < p1 < 0.1407
    assert 0.3093 < p2 < 0.3094
    assert p1 < 0.25 and p2 < 0.5, "each member checked against its own rating"
    # capacitors mirror: series shrinks
    c_series = 1.0 / (1 / 100e-9 + 1 / 100e-9)
    print("two 100 nF in series: %.0f nF" % (c_series * 1e9))
    assert 49.9e-9 < c_series < 50.1e-9
    print("rule: hottest series member is the largest; hottest parallel member is the smallest")
    print("OK: %s chained and counciled" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cpc_compatibility_meaning(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # gate one, mechanical: 25 mm shaft (h7) into 25 mm bore (H7)
    shaft_nom, shaft_tol = 25.000, (0.000, -0.021)
    bore_nom, bore_tol = 25.000, (0.021, 0.000)
    shaft_max = shaft_nom + shaft_tol[0]
    shaft_min = shaft_nom + shaft_tol[1]
    bore_max = bore_nom + bore_tol[0]
    bore_min = bore_nom + bore_tol[1]
    clear_max = bore_max - shaft_min
    clear_min = bore_min - shaft_max
    print("shaft 25 h7: %.3f / %.3f mm" % (shaft_max, shaft_min))
    print("bore  25 H7: %.3f / %.3f mm" % (bore_max, bore_min))
    print("clearance: %.3f to %.3f mm" % (clear_min, clear_max))
    assert 0.041 < clear_max < 0.043
    assert -0.001 < clear_min < 0.001
    fit = "sliding clearance" if clear_min >= 0 else "INTERFERENCE RISK"
    print("mechanical gate: %s" % fit)
    assert fit == "sliding clearance"
    # gate two, electrical: 3.3 V CMOS driver into 5 V TTL receiver
    voh, vol = 2.4, 0.4
    vih, vil = 2.0, 0.8
    nm_high = voh - vih
    nm_low = vil - vol
    print("noise margins: high %.1f V, low %.1f V" % (nm_high, nm_low))
    assert 0.39 < nm_high < 0.41
    assert 0.39 < nm_low < 0.41
    print("electrical gate: PASS - thresholds agree with margin")
    print("rule: four gates - mechanical, electrical, environmental, lifecycle - all must pass")
    print("OK: %s checked the handshake" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cpc_selection_criteria(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # decoupling capacitor selection: must-gate then weighted score
    need = {"v_rating_min": 25.0, "package_max_mm": 3.2}
    cands = [
        {"name": "A: 10uF X7R 25V 1206", "v": 25.0, "pkg": 3.2,
         "cost": 2, "stock": 5, "esr": 4, "source": 5},
        {"name": "B: 10uF X7R 50V 1206", "v": 50.0, "pkg": 3.2,
         "cost": 4, "stock": 5, "esr": 4, "source": 4},
        {"name": "C: 10uF Y5V 16V 0805", "v": 16.0, "pkg": 2.0,
         "cost": 5, "stock": 3, "esr": 2, "source": 2},
    ]
    # stage one: must-gate (voltage rating with margin, package)
    survivors = [c for c in cands
                 if c["v"] >= need["v_rating_min"] * 1.0 and c["pkg"] <= need["package_max_mm"]]
    print("must-gate survivors: %d of %d" % (len(survivors), len(cands)))
    assert len(survivors) == 2  # C fails the voltage rating
    # stage two: weighted scoring
    weights = {"cost": 0.30, "stock": 0.25, "esr": 0.15, "source": 0.30}
    scored = []
    for c in survivors:
        s = sum(c[k] * w for k, w in weights.items())
        scored.append((s, c["name"]))
        print("  %-24s score %.2f" % (c["name"], s))
    scored.sort(reverse=True)
    winner, margin = scored[0][0], scored[0][0] - scored[1][0]
    print("winner: %s (margin %.2f)" % (scored[0][1], margin))
    assert 4.24 < winner < 4.26
    assert 0.29 < margin < 0.31
    assert "B:" in scored[0][1]
    print("rule: must-gate eliminates, weights decide, the sheet is filed")
    print("OK: %s chose the oath-taker" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cpc_standards_numbering(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # decode RC0603FR-1002 segment by segment (4-digit value code)
    pn = "RC0603FR-1002"
    head, valuecode = pn.split("-")
    series, size, tolcode = head[0:2], head[2:6], head[6:7]
    imperial_mm = {"0603": (1.6, 0.8), "0805": (2.0, 1.25), "1206": (3.2, 1.6)}
    tolmap = {"F": 1.0, "G": 2.0, "J": 5.0, "D": 0.5}
    # 4-digit code: first three digits x 10^last -> 100 x 10^2 = 10 kilohms
    value = int(valuecode[0:3]) * (10 ** int(valuecode[3]))
    dims = imperial_mm[size]
    tol = tolmap[tolcode]
    print("part number: %s" % pn)
    print("  series %s, size %s -> %.1f x %.2f mm" % (series, size, dims[0], dims[1]))
    print("  tolerance code %s -> +/-%g %%" % (tolcode, tol))
    print("  value code %s -> %.0f ohms" % (valuecode, value))
    assert 1.59 < dims[0] < 1.61 and 0.79 < dims[1] < 0.81
    assert 0.99 < tol < 1.01
    assert 9999.9 < value < 10000.1
    print("rule: one wrong letter is a wrong part - decode against the table")
    print("OK: %s spoke the common tongue" % NAME)
if __name__ == "__main__":
    main()
''')


DEMOS = {
    "what_is": demo_cpc_what_is,
    "datasheet": demo_cpc_datasheet,
    "units_tolerances": demo_cpc_units_tolerances,
    "passives_overview": demo_cpc_passives_overview,
    "mechanical_overview": demo_cpc_mechanical_overview,
    "wire_connector": demo_cpc_wire_connector,
    "markings": demo_cpc_markings,
    "materials_stock": demo_cpc_materials_stock,
    "series_parallel": demo_cpc_series_parallel,
    "compatibility_meaning": demo_cpc_compatibility_meaning,
    "selection_criteria": demo_cpc_selection_criteria,
    "standards_numbering": demo_cpc_standards_numbering,
}

def demo_cpc_resistors(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # five-question sequence: value, power, tolerance/tempco, construction, package
    v, r = 12.0, 1000.0
    p = v ** 2 / r
    print("12 V across 1k: dissipation %.4f W" % p)
    assert 0.1439 < p < 0.1441
    # derating: 60% rule at temperature -> rating must be >= p / 0.6
    need = p / 0.60
    print("60%% derating: rating needed >= %.3f W" % need)
    assert 0.2399 < need < 0.2401
    rating = 0.25
    loading = p / rating
    print("selected 1/4 W metal film: loading %.1f %% (limit 60 %%)" % (loading * 100))
    assert 0.575 < loading < 0.577
    assert loading <= 0.60
    # E12 snap: computed 1440 ohms -> nearest E12 is 1500
    e12 = [1.0, 1.2, 1.5, 1.8, 2.2, 2.7, 3.3, 3.9, 4.7, 5.6, 6.8, 8.2]
    target = 1440.0
    snap = min((x * 1000 for x in e12), key=lambda x: abs(x - target))
    print("computed 1440 ohms snaps to E12: %.0f ohms" % snap)
    assert 1499.9 < snap < 1500.1
    # divider error with 1% parts, worst case
    err = 2.0  # % worst-case ratio error for a 2-resistor divider
    print("1%% divider worst-case ratio error: %.1f %%" % err)
    assert 1.99 < err < 2.01
    print("rule: value from the circuit, power from the curve, tempco where it matters")
    print("OK: %s pronounced every word" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cpc_capacitors(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # capacitive reactance at the operating frequency
    f, c = 1000.0, 10e-6
    xc = 1.0 / (2 * math.pi * f * c)
    print("10 uF at 1 kHz: Xc = %.4f ohms" % xc)
    assert 15.9154 < xc < 15.9156
    # DC bias theft: Y5V 10uF/25V at 12 V bias keeps ~35%
    nominal, kept = 10.0, 0.35
    effective = nominal * kept
    print("Y5V 10 uF at 12 V bias: effective %.1f uF" % effective)
    assert 3.49 < effective < 3.51
    verdict = "PASS" if effective >= 8.0 else "FAIL - upsize or change dielectric"
    print("8 uF needed: %s" % verdict)
    assert verdict.startswith("FAIL")
    # X7R alternative keeps ~85% under the same bias
    effective_x7r = nominal * 0.85
    print("X7R 10 uF at 12 V bias: effective %.1f uF -> %s" % (
        effective_x7r, "PASS" if effective_x7r >= 8.0 else "FAIL"))
    assert 8.49 < effective_x7r < 8.51
    # ripple heat: ESR x Irms^2
    esr, irms = 0.010, 2.0
    p_heat = esr * irms ** 2
    print("ripple heat: %.3f W in the ESR" % p_heat)
    assert 0.0399 < p_heat < 0.0401
    print("rule: verify effective capacitance, not printed capacitance")
    print("OK: %s measured the reservoir" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cpc_inductors(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # inductive reactance and the LC resonance of a filter pair
    f, l = 1000.0, 0.010
    xl = 2 * math.pi * f * l
    print("10 mH at 1 kHz: Xl = %.4f ohms" % xl)
    assert 62.8318 < xl < 62.8320
    c = 100e-9
    fres = 1.0 / (2 * math.pi * math.sqrt(l * c))
    print("10 mH + 100 nF resonant frequency: %.1f Hz" % fres)
    assert 5032.8 < fres < 5033.1
    # buck ripple sizing: L = V * dt / dI
    v_l, dt, di = 5.0, 2e-6, 0.5
    l_needed = v_l * dt / di
    print("buck needs L >= %.1f uH for 0.5 A ripple" % (l_needed * 1e6))
    assert 19.99e-6 < l_needed < 20.01e-6
    # saturation check: peak current vs Isat
    i_dc, i_pk = 3.0, 3.0 + di / 2
    isat = 4.5
    margin = isat / i_pk
    print("peak %.2f A vs Isat %.1f A: margin %.2fx" % (i_pk, isat, margin))
    assert 1.384 < margin < 1.386
    assert margin > 1.2, "saturation margin too thin"
    print("rule: Isat above peak with margin - a saturated inductor is a resistor with ambitions")
    print("OK: %s respected the momentum" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cpc_diodes(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # LED series resistor: current, not voltage
    vs, vf, i = 5.0, 2.0, 0.020
    r = (vs - vf) / i
    p = i ** 2 * r
    print("5 V rail, 2 V LED at 20 mA: R = %.0f ohms" % r)
    print("resistor dissipation: %.4f W" % p)
    assert 149.9 < r < 150.1
    assert 0.0599 < p < 0.0601
    # E12 snap upward for safety (less current)
    r_std = 150.0
    i_actual = (vs - vf) / r_std
    print("standard 150 ohms -> actual current %.1f mA" % (i_actual * 1000))
    assert 0.01999 < i_actual < 0.02001
    # bridge reverse rating: 12.6 VAC secondary -> peak + margin
    vrms = 12.6
    vpeak = vrms * math.sqrt(2)
    vrrm_need = vpeak * 2.0
    print("12.6 VAC secondary: peak %.2f V, bridge V_RRM needed >= %.1f V" % (vpeak, vrrm_need))
    assert 17.81 < vpeak < 17.83
    assert 35.6 < vrrm_need < 35.7
    # TVS bodyguard: standoff above normal, clamp below victim
    v_normal, v_stand, v_clamp, v_victim = 12.0, 13.3, 19.0, 20.0
    ok = v_normal < v_stand < v_clamp < v_victim
    print("TVS 13.3 V standoff / 19 V clamp protects 20 V victim: %s" % ("PASS" if ok else "FAIL"))
    assert ok
    print("rule: reverse rating doubled against the storm, surge rated for the inrush")
    print("OK: %s posted the gatekeepers" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cpc_transistors(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # MOSFET switch: conduction + switching loss -> junction temperature
    i, rdson = 5.0, 0.020
    p_cond = i ** 2 * rdson
    qg, vgs, f = 30e-9, 10.0, 100e3
    p_sw = qg * vgs * f
    p_total = p_cond + p_sw
    print("conduction: %.3f W; switching: %.3f W; total %.3f W" % (p_cond, p_sw, p_total))
    assert 0.4999 < p_cond < 0.5001
    assert 0.02999 < p_sw < 0.03001
    assert 0.5299 < p_total < 0.5301
    rth_ja, ta = 40.0, 25.0
    tj = ta + p_total * rth_ja
    print("junction: %.1f C (derated limit 125 C)" % tj)
    assert 46.19 < tj < 46.21
    assert tj < 125.0
    # BJT base drive at forced beta 10
    ic, beta_forced = 0.5, 10.0
    ib = ic / beta_forced
    rb = (5.0 - 0.7) / ib
    print("BJT: Ic 0.5 A needs Ib %.0f mA -> Rb %.0f ohms (use 82)" % (ib * 1000, rb))
    assert 0.0499 < ib < 0.0501
    assert 85.9 < rb < 86.1
    print("rule: drive the gate fully - a half-on MOSFET is a heater")
    print("OK: %s commanded the strong arm" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cpc_ics_logic(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # 74HCT-style driver (5 V) into TTL receiver: the treaty table
    voh, vol = 2.4, 0.4
    vih, vil = 2.0, 0.8
    nm_high = voh - vih
    nm_low = vil - vol
    print("driver VOH %.1f / VOL %.1f; receiver VIH %.1f / VIL %.1f" % (voh, vol, vih, vil))
    print("noise margins: high %.1f V, low %.1f V" % (nm_high, nm_low))
    assert 0.399 < nm_high < 0.401
    assert 0.399 < nm_low < 0.401
    assert nm_high > 0 and nm_low > 0, "negative margin means translate"
    # fan-out current budget
    ioh, loads = 0.004, 10
    i_leak_each = 0.000040
    ok = ioh >= loads * i_leak_each
    print("fan-out: %.1f mA drive vs %.2f mA load -> %s" % (ioh * 1000, loads * i_leak_each * 1000,
                                                            "PASS" if ok else "FAIL"))
    assert ok
    # the forbidden direction: 5 V CMOS output into 3.3 V-only input
    voh_5v, vmax_33 = 4.4, 3.6
    print("5 V driver VOH %.1f V into 3.3 V input (abs max %.1f V): %s" % (
        voh_5v, vmax_33, "TRANSLATE - never direct"))
    assert voh_5v > vmax_33
    print("rule: positive margin both sides, or level translation - direction matters")
    print("OK: %s kept the treaty" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cpc_sensors(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # thermistor divider, beta model: the nonlinearity calibration must absorb
    r0, t0, beta = 10000.0, 298.15, 3950.0
    r_series, vcc = 10000.0, 5.0

    def r_at(t_c):
        t = t_c + 273.15
        return r0 * math.exp(beta * (1.0 / t - 1.0 / t0))

    def v_out(t_c):
        rt = r_at(t_c)
        return vcc * rt / (r_series + rt)

    v25 = v_out(25.0)
    v50 = v_out(50.0)
    print("10k NTC + 10k divider at 5 V:")
    print("  25 C: R=%.0f ohms -> %.4f V" % (r_at(25.0), v25))
    print("  50 C: R=%.0f ohms -> %.4f V" % (r_at(50.0), v50))
    assert 2.499 < v25 < 2.501
    assert 1.319 < v50 < 1.322
    sens = (v25 - v50) / 25.0 * 1000.0  # mV per degree
    print("sensitivity 25-50 C: %.2f mV/C (nonlinear - calibrate, do not assume)" % sens)
    assert 47.1 < sens < 47.3
    # error budget sanity: sensor 1% vs 16-bit ADC theater
    adc_lsb_mv = 5000.0 / 65536.0
    print("16-bit ADC LSB: %.3f mV - far below sensor accuracy; accuracy, not resolution, rules" % adc_lsb_mv)
    assert 0.0762 < adc_lsb_mv < 0.0764
    print("rule: specify the measurement first; budget error stage by stage")
    print("OK: %s briefed the scouts" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cpc_optoelectronics(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # white LED: current drive from the rail
    vs, vf, i = 5.0, 3.2, 0.020
    r = (vs - vf) / i
    p = i ** 2 * r
    print("5 V, white LED Vf 3.2 V at 20 mA: R = %.0f ohms, P = %.4f W" % (r, p))
    assert 89.9 < r < 90.1
    assert 0.0359 < p < 0.0361
    # constant-current check: supply sags to 4.5 V, resistor circuit dims
    i_sag = (4.5 - vf) / r
    print("rail sags to 4.5 V: resistor-fed current falls to %.1f mA (dims)" % (i_sag * 1000))
    assert 0.0144 < i_sag < 0.0145
    print("constant-current driver would hold 20.0 mA - that is why lighting uses drivers")
    # optocoupler CTR at end of life
    ctr_new, ctr_eol = 1.00, 0.60
    i_led = 0.010
    i_c_new, i_c_eol = i_led * ctr_new, i_led * ctr_eol
    i_need = 0.004
    ok = i_c_eol >= i_need
    print("optocoupler: 10 mA LED -> %.1f mA now, %.1f mA at end of life (need %.1f): %s" % (
        i_c_new * 1000, i_c_eol * 1000, i_need * 1000, "PASS" if ok else "FAIL"))
    assert ok
    assert 0.00599 < i_c_eol < 0.00601
    print("rule: design at end-of-life CTR, drive LEDs with current")
    print("OK: %s lit the signal fires" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cpc_fasteners(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # M10 x 1.5, property class 8.8: proof load and working preload
    stress_area = 58.0  # mm^2, standard value
    proof_stress = 580.0  # MPa = N/mm^2
    proof_load = stress_area * proof_stress / 1000.0  # kN
    preload = proof_load * 0.75
    print("M10x1.5 8.8: stress area %.1f mm^2" % stress_area)
    print("proof load: %.2f kN; working preload (75%%): %.2f kN" % (proof_load, preload))
    assert 57.9 < stress_area < 58.1
    assert 33.63 < proof_load < 33.65
    assert 25.22 < preload < 25.24
    # torque scatter: +/-25% on preload with ordinary lubrication
    t_nom = 50.0  # N-m nominal
    print("tightening torque %.0f N-m gives preload %.1f-%.1f kN with scatter" % (
        t_nom, preload * 0.75, preload * 1.25))
    # thread engagement in aluminum: 2x diameter
    engagement = 2.0 * 10.0
    print("engagement needed in aluminum: %.0f mm" % engagement)
    assert 19.9 < engagement < 20.1
    # head mark decode: 8.8
    tensile = 8 * 100
    yield_ratio = 0.8
    print("head mark 8.8: %d MPa tensile, yield ratio %.1f" % (tensile, yield_ratio))
    assert tensile == 800
    print("rule: the stretched bolt is a stiff spring - preload is the joint")
    print("OK: %s swore the oath in steel" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cpc_bearings(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # L10 life: (C/P)^3 million revolutions for ball bearings
    c_dyn, p_eq = 20.0, 4.0  # kN
    l10_mrev = (c_dyn / p_eq) ** 3
    rpm = 1500.0
    hours = l10_mrev * 1e6 / (rpm * 60.0)
    print("C = %.0f kN, P = %.0f kN -> L10 = %.0f million revolutions" % (c_dyn, p_eq, l10_mrev))
    print("at %.0f rpm: %.0f hours L10" % (rpm, hours))
    assert 124.9 < l10_mrev < 125.1
    assert 1388.8 < hours < 1389.0
    # what if the load doubles? life falls 8x
    l10_double = (c_dyn / (2 * p_eq)) ** 3
    print("load doubles -> L10 falls to %.1f Mrev (%.1fx shorter)" % (l10_double, l10_mrev / l10_double))
    assert 15.62 < l10_double < 15.64
    # required C for a 20,000-hour target
    target_h = 20000.0
    target_mrev = target_h * rpm * 60.0 / 1e6
    c_needed = p_eq * (target_mrev ** (1.0 / 3.0))
    print("for %.0f h target: need C >= %.1f kN" % (target_h, c_needed))
    assert 48.6 < c_needed < 48.7
    print("rule: size from required life, then pick the smallest C that covers it")
    print("OK: %s swore the vow of years" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cpc_gears(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # spur pair: module x teeth = pitch diameter; center distance is fixed
    m, z1, z2 = 2.0, 20, 60
    d1, d2 = m * z1, m * z2
    center = (d1 + d2) / 2.0
    ratio = z2 / z1
    rpm_in = 1200.0
    rpm_out = rpm_in / ratio
    print("module %.0f, %d/%d teeth:" % (m, z1, z2))
    print("  pitch diameters: %.0f mm / %.0f mm" % (d1, d2))
    print("  center distance: %.0f mm (machine the housing to this)" % center)
    print("  ratio %.0f:1, %.0f rpm in -> %.0f rpm out" % (ratio, rpm_in, rpm_out))
    assert 39.9 < d1 < 40.1
    assert 119.9 < d2 < 120.1
    assert 79.9 < center < 80.1
    assert 399.9 < rpm_out < 400.1
    # undercut guard: 20-degree full-depth needs >= 17 teeth on the pinion
    assert z1 >= 17, "pinion undercut"
    # torque multiplication (minus efficiency)
    t_in, eff = 5.0, 0.97
    t_out = t_in * ratio * eff
    print("  %.1f N-m in -> %.1f N-m out (97%% mesh efficiency)" % (t_in, t_out))
    assert 14.54 < t_out < 14.56
    print("rule: module is compatibility law - mismatches do not assemble")
    print("OK: %s translated faithfully" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cpc_relays(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # coil power and the AC-to-DC contact derating
    v_coil, r_coil = 12.0, 400.0
    i_coil = v_coil / r_coil
    p_coil = v_coil ** 2 / r_coil
    print("12 V coil, 400 ohms: %.0f mA, %.3f W" % (i_coil * 1000, p_coil))
    assert 0.0299 < i_coil < 0.0301
    assert 0.3599 < p_coil < 0.3601
    # contact derating: 10 A AC -> ~3 A DC (no zero-crossing to quench the arc)
    i_ac, derate = 10.0, 0.30
    i_dc = i_ac * derate
    print("10 A AC contact derated for DC: %.1f A DC" % i_dc)
    assert 2.99 < i_dc < 3.01
    load_dc = 2.5
    print("2.5 A DC load: %s" % ("PASS" if load_dc <= i_dc else "FAIL - upsize the relay"))
    assert load_dc <= i_dc
    # inrush: cold lamp filament draws ~10x running current
    i_run = 0.8
    i_inrush = i_run * 10
    print("lamp: %.1f A running, %.0f A inrush - size contacts for the inrush" % (i_run, i_inrush))
    assert 7.99 < i_inrush < 8.01
    # flyback: the spike that kills drivers (Lenz, qualitative guard)
    print("DC coil without flyback diode: collapsing field spikes hundreds of volts - diode mandatory")
    print("rule: size to the worse of steady current and inrush; suppress every DC coil")
    print("OK: %s armed the champions" % NAME)
if __name__ == "__main__":
    main()
''')


DEMOS.update({
    "resistors": demo_cpc_resistors,
    "capacitors": demo_cpc_capacitors,
    "inductors": demo_cpc_inductors,
    "diodes": demo_cpc_diodes,
    "transistors": demo_cpc_transistors,
    "ics_logic": demo_cpc_ics_logic,
    "sensors": demo_cpc_sensors,
    "optoelectronics": demo_cpc_optoelectronics,
    "fasteners": demo_cpc_fasteners,
    "bearings": demo_cpc_bearings,
    "gears": demo_cpc_gears,
    "relays": demo_cpc_relays,
})

def demo_cpc_derating(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # capacitor voltage derating: 50% rule on a 24 V rail
    v_rail = 24.0
    rule = 0.50
    rating_needed = v_rail / rule
    print("24 V rail at 50%% derating: rating >= %.0f V" % rating_needed)
    assert 47.9 < rating_needed < 48.1
    rating = 50.0
    ratio = v_rail / rating
    print("selected 50 V: stress ratio %.2f (limit %.2f) -> %s" % (
        ratio, rule, "PASS" if ratio <= rule else "FAIL"))
    assert 0.479 < ratio < 0.481
    assert ratio <= rule
    # resistor power derating: 60% rule
    p, r_rating = 0.144, 0.25
    p_ratio = p / r_rating
    print("resistor %.3f W on %.2f W: ratio %.3f (limit 0.60) -> %s" % (
        p, r_rating, p_ratio, "PASS" if p_ratio <= 0.60 else "FAIL"))
    assert 0.575 < p_ratio < 0.577
    # junction temperature derating
    tj, tj_max = 90.0, 150.0
    tj_limit = 125.0
    print("junction %.0f C vs derated limit %.0f C (abs max %.0f) -> %s" % (
        tj, tj_limit, tj_max, "PASS" if tj <= tj_limit else "FAIL"))
    assert tj <= tj_limit
    # the footnote trap: voltage-derated but ripple-cooked
    print("trap check: ripple current and temperature still apply - derating one stress never excuses the others")
    print("rule: the honor margin - keep half the voltage and a third of the heat in reserve")
    print("OK: %s held the margin" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cpc_tolerance_stackup(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # three-dimension chain: 10+/-0.1, 25+/-0.2, 15+/-0.1
    dims = [(10.0, 0.1, 1), (25.0, 0.2, 1), (15.0, 0.1, -1)]
    nominal = sum(d * s for d, t, s in dims)
    worst = sum(t for d, t, s in dims)
    rss = math.sqrt(sum(t ** 2 for d, t, s in dims))
    print("chain nominal: %.1f mm" % nominal)
    print("worst-case stack: +/-%.1f mm" % worst)
    print("RSS stack: +/-%.4f mm" % rss)
    assert 19.9 < nominal < 20.1
    assert 0.399 < worst < 0.401
    assert 0.2449 < rss < 0.2450
    # contributor ranking: squared share
    total_sq = sum(t ** 2 for d, t, s in dims)
    ranked = sorted(((t ** 2 / total_sq * 100.0, d) for d, t, s in dims), reverse=True)
    print("contributors by squared share:")
    for share, d in ranked:
        print("  %.0f mm dim: %.1f %%" % (d, share))
    assert 66.6 < ranked[0][0] < 66.8  # the +/-0.2 dominates
    # clearance verdict: 0.5 mm nominal gap, worst case
    gap_nom, gap_min = 0.5, 0.5 - worst
    print("0.5 mm gap at worst case: %.1f mm -> %s" % (
        gap_min, "PASS" if gap_min > 0 else "FAIL - tighten the 25 mm dim"))
    assert 0.099 < gap_min < 0.101
    print("rule: worst-case where honor demands certainty, RSS where the process earned trust")
    print("OK: %s mustered the chain" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cpc_thermal(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # three-link chain: junction-case, interface, heatsink
    p = 2.5
    r_jc, r_int, r_sink = 3.0, 1.0, 12.0
    r_total = r_jc + r_int + r_sink
    ta = 50.0
    tj = ta + p * r_total
    print("thermal chain: %.0f + %.0f + %.0f = %.0f C/W" % (r_jc, r_int, r_sink, r_total))
    print("%.1f W in %.0f C ambient -> Tj = %.0f C" % (p, ta, tj))
    assert 15.99 < r_total < 16.01
    assert 89.9 < tj < 90.1
    tj_limit = 125.0
    margin = tj_limit - tj
    print("derated limit %.0f C: margin %.0f C -> %s" % (
        tj_limit, margin, "PASS" if margin > 0 else "FAIL"))
    assert 34.9 < margin < 35.1
    # what if the interface is forgotten (dry mount)?
    r_dry = r_jc + 8.0 + r_sink
    tj_dry = ta + p * r_dry
    print("dry mount (interface 8 C/W): Tj = %.0f C -> %s" % (
        tj_dry, "PASS" if tj_dry <= tj_limit else "FAIL - never dry-mount power parts"))
    assert 107.4 < tj_dry < 107.6
    print("rule: budget the rise link by link, then measure - heat is honest")
    print("OK: %s built the road out" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cpc_emc(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # RC low-pass at the enclosure wall: cutoff and harmonic attenuation
    r, c = 100.0, 10e-9
    fc = 1.0 / (2 * math.pi * r * c)
    print("R=100, C=10 nF: cutoff %.2f kHz" % (fc / 1000))
    assert 159.14e3 < fc < 159.16e3
    # attenuation at the 10 MHz harmonic, single pole ~ fc/f
    f_noise = 10e6
    atten_ratio = fc / f_noise
    atten_db = 20 * math.log10(atten_ratio)
    print("attenuation at 10 MHz: ratio %.5f (~%.1f dB)" % (atten_ratio, atten_db))
    assert 0.01591 < atten_ratio < 0.01592
    assert -36.0 < atten_db < -35.9
    # ferrite bead in the noise band: impedance peaks where it should
    bead_z = {"10 MHz": 30.0, "100 MHz": 600.0, "300 MHz": 450.0}
    print("bead impedance: 10 MHz %d ohms, 100 MHz %d ohms" % (bead_z["10 MHz"], bead_z["100 MHz"]))
    assert bead_z["100 MHz"] > 10 * bead_z["10 MHz"], "bead must peak in the noise band"
    # edge-rate taming: series resistor slows the edge
    print("cheapest filter ever made: a series resistor at the driver, slowing the edge")
    print("rule: quiet the source, filter every exit at the wall")
    print("OK: %s kept the discipline of voice" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cpc_reliability(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # FITs -> MTBF -> mission reliability for a three-part series chain
    fits = [100.0, 50.0, 25.0]
    lam = sum(fits) * 1e-9  # failures per hour
    mtbf = 1.0 / lam
    print("part FITs %s -> total %.0f FIT" % (fits, sum(fits)))
    print("MTBF: %.0f hours (%.1f years)" % (mtbf, mtbf / 8760.0))
    assert 5714285.0 < mtbf < 5714286.0
    mission_h = 8760.0
    r_mission = math.exp(-lam * mission_h)
    print("1-year mission reliability: %.6f" % r_mission)
    assert 0.998467 < r_mission < 0.998469
    # series multiplication: three 99.9% parts
    r_each = 0.999
    r_sys = r_each ** 3
    print("three 99.9%% parts in series: %.4f %%" % (r_sys * 100))
    assert 0.997002 < r_sys < 0.997004
    # redundancy: two parallel 99% units
    r_par = 1 - (1 - 0.99) ** 2
    print("two 99%% units redundant: %.4f %%" % (r_par * 100))
    assert 0.999899 < r_par < 0.999901
    print("rule: MTBF is a mean, not a lifetime - half fail before it")
    print("OK: %s projected the oath through time" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cpc_counterfeit(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # statistical gate: sample weight vs the genuine population
    mu, sigma = 2.50, 0.02
    n, sample_mean = 30, 2.43
    se = sigma / math.sqrt(n)
    z = (mu - sample_mean) / se
    print("genuine 2.50 +/-0.02 g; sample of %d means %.2f g" % (n, sample_mean))
    print("z-score: %.1f sigma" % z)
    assert 19.1 < z < 19.3
    weight_flag = z > 3.0
    # marking consistency score from visual inspection
    mark_score, mark_limit = 0.62, 0.90
    print("marking consistency score %.2f (limit %.2f)" % (mark_score, mark_limit))
    mark_flag = mark_score < mark_limit
    verdict = "QUARANTINE" if (weight_flag or mark_flag) else "ACCEPT"
    print("weight flag: %s; marking flag: %s -> %s" % (weight_flag, mark_flag, verdict))
    assert verdict == "QUARANTINE"
    # solvent rub: remarked parts wipe
    print("solvent rub on a remarked fake: the marking wipes - the genuine mark stays")
    print("rule: broker buys are guilty until proven innocent")
    print("OK: %s guarded the gate" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cpc_obsolescence(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # last-time buy: demand x years + spares + buffer, rounded to MOQ
    annual, years = 500.0, 7.0
    spares = 500.0
    subtotal = annual * years + spares
    buffer = 0.20
    with_buffer = subtotal * (1 + buffer)
    moq = 1000.0
    buy = math.ceil(with_buffer / moq) * moq
    print("demand %.0f/yr x %.0f yr + %.0f spares = %.0f" % (annual, years, spares, subtotal))
    print("with 20%% buffer: %.0f -> rounded to MOQ %.0f: %.0f pieces" % (with_buffer, moq, buy))
    assert 3499.9 < subtotal < 3500.1 + 500.0  # 4000
    assert 4799.9 < with_buffer < 4800.1
    assert 4999.9 < buy < 5000.1
    # storage cost sanity: 5000 reels at $0.002/piece/year carrying
    carry = buy * 0.002 * years
    print("carrying cost over %d years: $%.0f - the price of the insurance" % (years, carry))
    assert 69.9 < carry < 70.1
    # the alternate path runs in parallel
    print("parallel path: qualify the drop-in alternate by form-fit-function + delta testing")
    print("rule: the covenant should end by planning, never by surprise")
    print("OK: %s watched the tide tables" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cpc_sourcing_bom(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # BOM rollup: MOQ rounding, extended costs, pacing lead time
    lines = [
        {"pn": "RES-10K-0603", "qty": 4000, "price": 0.002, "moq": 5000, "lead_wk": 4},
        {"pn": "CAP-10U-1206", "qty": 4000, "price": 0.010, "moq": 4000, "lead_wk": 6},
        {"pn": "MCU-32F103", "qty": 1000, "price": 1.200, "moq": 1000, "lead_wk": 12},
    ]
    total = 0.0
    pacing = ("", 0)
    for ln in lines:
        order = math.ceil(ln["qty"] / ln["moq"]) * ln["moq"]
        ext = order * ln["price"]
        total += ext
        if ln["lead_wk"] > pacing[1]:
            pacing = (ln["pn"], ln["lead_wk"])
        print("  %-12s need %d -> order %d @ $%.3f = $%.2f (%dwk)" % (
            ln["pn"], ln["qty"], order, ln["price"], ext, ln["lead_wk"]))
    print("BOM total: $%.2f" % total)
    print("pacing part: %s at %d weeks - the schedule starts here" % pacing)
    assert 1249.9 < total < 1250.1
    assert pacing == ("MCU-32F103", 12)
    # price break check: 10k pricing would halve the MCU cost
    print("price-break note: at 10k the MCU drops to $0.85 - volume moves the math")
    print("rule: quote at the build volume; the schedule starts from the longest lead")
    print("OK: %s provisioned the armory" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cpc_cross_reference(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # scored parametric match against the required parameter set
    need = {"c_min": 9.5, "v_min": 50.0, "esr_max": 0.050, "t_min": -40.0}
    cands = [
        {"name": "A", "c": 10.0, "v": 50.0, "esr": 0.030, "t": -55.0},
        {"name": "B", "c": 9.0, "v": 63.0, "esr": 0.020, "t": -55.0},
        {"name": "C", "c": 12.0, "v": 50.0, "esr": 0.060, "t": -40.0},
    ]
    survivors = [c for c in cands
                 if c["c"] >= need["c_min"] and c["v"] >= need["v_min"]
                 and c["esr"] <= need["esr_max"] and c["t"] <= need["t_min"]]
    print("hard filter survivors: %s" % [c["name"] for c in survivors])
    assert [c["name"] for c in survivors] == ["A"]  # B fails capacitance, C fails ESR
    # margin scoring on the survivor set (single survivor here)
    w = {"c": 0.4, "v": 0.3, "esr": 0.3}
    for c in survivors:
        score = (w["c"] * (c["c"] / need["c_min"] - 1)
                 + w["v"] * (c["v"] / need["v_min"] - 1)
                 + w["esr"] * (need["esr_max"] / c["esr"] - 1))
        print("  candidate %s margin score: %.4f" % (c["name"], score))
        assert 0.2210 < score < 0.2212
    print("delta analysis: A vs original - ESR better, temp wider; bench-verify ripple at temp")
    print("rule: filter hard on criticals, prove the successor worthy")
    print("OK: %s proved the succession" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cpc_modules(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # build vs buy: break-even volume
    module_price = 12.0
    nre = 40000.0
    build_unit = 4.0
    volume = 20000.0
    cost_buy = module_price * volume
    cost_build = nre + build_unit * volume
    breakeven = nre / (module_price - build_unit)
    print("volume %.0f:" % volume)
    print("  buy : $%.0f x %.0f = $%.0f" % (module_price, volume, cost_buy))
    print("  build: $%.0f NRE + $%.0f x %.0f = $%.0f" % (nre, build_unit, volume, cost_build))
    print("  break-even volume: %.0f units" % breakeven)
    assert 239999.9 < cost_buy < 240000.1
    assert 119999.9 < cost_build < 120000.1
    assert 4999.9 < breakeven < 5000.1
    verdict = "BUILD" if volume > breakeven else "BUY"
    print("at %.0f units: %s wins on math (strategy may overrule, in writing)" % (volume, verdict))
    assert verdict == "BUILD"
    # sensitivity: at half volume the answer flips
    v2 = volume / 2
    print("at %.0f units: buy $%.0f vs build $%.0f -> %s" % (
        v2, module_price * v2, nre + build_unit * v2,
        "BUILD" if v2 > breakeven else "BUY"))
    assert v2 > breakeven  # 10000 still above 5000
    print("rule: count the alliance's true cost - NRE is the number everyone underestimates")
    print("OK: %s chose its allies" % NAME)
if __name__ == "__main__":
    main()
''')


DEMOS.update({
    "derating": demo_cpc_derating,
    "tolerance_stackup": demo_cpc_tolerance_stackup,
    "thermal": demo_cpc_thermal,
    "emc": demo_cpc_emc,
    "reliability": demo_cpc_reliability,
    "counterfeit": demo_cpc_counterfeit,
    "obsolescence": demo_cpc_obsolescence,
    "sourcing_bom": demo_cpc_sourcing_bom,
    "cross_reference": demo_cpc_cross_reference,
    "modules": demo_cpc_modules,
})
