#!/usr/bin/env python3
"""Build the Tribology and Lubrication pair (gap-audit part 2).

Verified 2026-10-17: NO database covers tribology as a discipline (friction,
wear, lubrication systems, surface interactions, lifetime). Manifest keyword
search (tribology, lubrication): zero hits. ZERO full-record coverage.

Two NEW databases, 34 ladder-ordered records each:
  tribology-lubrication            (public-harvest)
  tribology-lubrication-signature  (signature)

Never any website references. No Facebook.
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, "/home/hatch/workspace/jah-databases/code/gapaudit-p2")
import driver
from entries_tribology import ENTRIES

RK = "tribology record"
CIT_PUB = ("Tribology and lubrication (standard references: Bowden & Tabor 'The Friction and "
           "Lubrication of Solids' 1950; Stachowiak & Batchelor 'Engineering Tribology' 4th ed. "
           "2013; Hamrock, Schmid & Jacobson 'Fundamentals of Fluid Film Lubrication' 2004; "
           "ISO 281 rolling bearing life; ASTM D4172 four-ball wear; Czichos et al. "
           "'Tribology: A Systems Approach to the Science and Technology of Friction, "
           "Lubrication, and Wear' 2009).")
CIT_SIG = CIT_PUB + " Signature editions are his original Signature treatment of tribology."
STANDARDS = ["Tribology practice per ISO 281 / cited references",
             "Teaching-ladder order: foundations, compounded, advanced"]

cfg_pub, cfg_sig = driver.pair_cfgs(
    slug_base="tribology-lubrication", name_base="Tribology and Lubrication",
    tagline=("Friction, wear, lubrication systems, surface interactions, and lifetime: the "
             "science of surfaces in contact - from friction laws and the Stribeck curve "
             "through hydrodynamic and elastohydrodynamic lubrication, wear mechanisms, and "
             "bearings to film thickness, oil analysis, and lifetime prediction, taught "
             "progressively along the ladder."),
    record_kind=RK, prefix_pub="JAH-TRL-", prefix_sig="JAH-TRLS-",
    ai_base="JAH Tribology Archivist",
    role_pub=("tribology archivist - friction, wear, lubrication regimes, bearings, seals, "
              "surface engineering, lifetime prediction; teaching progressively along the "
              "ladder from foundations through compounded to advanced; answers from many "
              "angles - definition, example, procedure, math, standards - using only the "
              "system's own archive data"),
    role_sig=("tribology archivist - Signature editions: his original Signature treatment "
              "of tribology, clearly labeled Signature-made and never presented as authentic "
              "public record; teaches progressively along the ladder; answers from many "
              "angles using only the system's own archive data"),
    search_ph="Search friction, Stribeck, viscosity, wear, EHL, bearings, L10...",
    chat_ph="Ask about tribology...",
    archive_topic="tribology records",
    gen_kind="tribology",
    standards=STANDARDS, cit_pub=CIT_PUB, cit_sig=CIT_SIG,
    hero_pub=("Public records - real, fact-checked tribology: what tribology is, friction laws, "
              "static vs kinetic friction, wear, lubrication regimes, viscosity, surface "
              "roughness, contact mechanics, oils and greases, additives, the Stribeck curve, "
              "tribometers, hydrodynamic and elastohydrodynamic lubrication, boundary "
              "lubrication, viscosity-temperature, adhesive/abrasive/fatigue wear, Archard's "
              "law, journal and rolling bearings, L10 life, gears, seals, film thickness, oil "
              "analysis, grease practice, solid lubricants, surface engineering, fretting, "
              "oxidation, lifetime models, test specimens, and systems design - organized in "
              "the Signature system. Every record carries the full entry: description, how "
              "it works, key points, requirements, standards, citations, and a working "
              "demonstration program. Records are ordered by the teaching ladder: "
              "Foundations -> Compounded -> Advanced."),
    hero_sig=("Signature originals - his original Signature treatment of tribology and "
              "lubrication: the full ladder from friction laws through lubrication regimes "
              "and wear to lifetime prediction, reframed as Signature science. Clearly "
              "labeled Signature-made, never presented as authentic public record. Every "
              "record carries the full entry: description, how it works, key points, "
              "requirements, standards, citations, and a working demonstration program."))

DEMOS = {}


def _reg(key):
    def deco(fn):
        DEMOS[key] = fn
        return fn
    return deco


import json as _json


@_reg("tr_stribeck")
def d_stribeck(name, rid, group):
    return driver.demo_hdr(name, rid, group) + '''\
def main():
    # Hersey number -> lubrication regime on the Stribeck curve
    def regime(hersey):
        if hersey < 1e-7:
            return "boundary"
        if hersey < 1e-5:
            return "mixed"
        return "hydrodynamic"
    cases = [(2e-8, "boundary"), (1e-6, "mixed"), (5e-5, "hydrodynamic")]
    for h, exp in cases:
        got = regime(h)
        print("  Hersey %.0e -> %s" % (h, got))
        assert got == exp
    print("OK: %s classified lubrication regimes by Hersey number" % ''' + _json.dumps(name) + ''')
if __name__ == "__main__":
    main()
'''


@_reg("tr_visc")
def d_visc(name, rid, group):
    return driver.demo_hdr(name, rid, group) + '''\
import math
def main():
    # viscosity-temperature: Walther equation log-log form
    # log10(log10(nu + 0.7)) = A - B*log10(T); fit two points, predict third
    def walther_fit(nu1, T1, nu2, T2):
        import math
        y1 = math.log10(math.log10(nu1 + 0.7))
        y2 = math.log10(math.log10(nu2 + 0.7))
        x1, x2 = math.log10(T1), math.log10(T2)
        B = (y1 - y2) / (x2 - x1)
        A = y1 + B * x1
        return A, B
    def walther_pred(A, B, T):
        y = A - B * math.log10(T)
        return 10.0 ** (10.0 ** y) - 0.7
    # ISO VG 46: ~46 cSt at 40C, ~6.7 cSt at 100C
    A, B = walther_fit(46.0, 313.15, 6.7, 373.15)
    nu70 = walther_pred(A, B, 343.15)
    print("VG46: A=%.4f B=%.4f -> viscosity at 70C = %.1f cSt" % (A, B, nu70))
    assert 12.0 < nu70 < 20.0, nu70
    print("OK: %s predicted viscosity with the Walther equation" % ''' + _json.dumps(name) + ''')
if __name__ == "__main__":
    main()
'''


@_reg("tr_hertz")
def d_hertz(name, rid, group):
    return driver.demo_hdr(name, rid, group) + '''\
import math
def main():
    # Hertzian contact: steel ball on flat, max pressure p0
    F = 100.0          # N
    R = 0.010          # m ball radius
    E = 210e9          # Pa steel
    nu = 0.30
    Estar = E / (2.0 * (1.0 - nu ** 2))
    a = (3.0 * F * R / (4.0 * Estar)) ** (1.0 / 3.0)
    p0 = 3.0 * F / (2.0 * math.pi * a ** 2)
    print("contact radius a = %.3f mm, max pressure p0 = %.0f MPa" % (a * 1000, p0 / 1e6))
    assert abs(a * 1000 - 0.187) < 0.01, a
    assert 1300e6 < p0 < 1450e6, p0
    print("OK: %s computed Hertzian contact pressure" % ''' + _json.dumps(name) + ''')
if __name__ == "__main__":
    main()
'''


@_reg("tr_archard")
def d_archard(name, rid, group):
    return driver.demo_hdr(name, rid, group) + '''\
def main():
    # Archard wear law: V = K * F * s / H
    K = 1e-4           # wear coefficient (mild wear)
    F = 50.0           # N normal load
    s = 1000.0         # m sliding distance
    H = 2e9            # Pa hardness
    V = K * F * s / H  # m^3
    print("wear volume = %.3e m^3 = %.2f mm^3" % (V, V * 1e9))
    assert abs(V * 1e9 - 2.5) < 1e-9
    # double the load -> double the wear (Archard linearity)
    assert abs((K * 2 * F * s / H) - 2 * V) < 1e-18
    print("OK: %s applied the Archard wear law" % ''' + _json.dumps(name) + ''')
if __name__ == "__main__":
    main()
'''


@_reg("tr_l10")
def d_l10(name, rid, group):
    return driver.demo_hdr(name, rid, group) + '''\
def main():
    # bearing L10 life: L10 = (C/P)^p million revolutions (p=3 ball bearings)
    C = 19.0   # kN dynamic load rating
    P = 4.75   # kN equivalent load
    p = 3.0
    L10 = (C / P) ** p
    rpm = 1500.0
    hours = L10 * 1e6 / (60.0 * rpm)
    print("C=%.1f kN P=%.2f kN -> L10 = %.0f million rev = %.0f hours at %d rpm" % (C, P, L10, hours, rpm))
    assert abs(L10 - 64.0) < 1e-9
    assert abs(hours - 711.1) < 1.0, hours
    print("OK: %s computed bearing L10 life" % ''' + _json.dumps(name) + ''')
if __name__ == "__main__":
    main()
'''


@_reg("tr_friction")
def d_friction(name, rid, group):
    return driver.demo_hdr(name, rid, group) + '''\
def main():
    # friction power loss: P = mu * F * v
    mu = 0.08          # lubricated sliding
    F = 2000.0         # N
    v = 2.5            # m/s
    P = mu * F * v
    print("mu=%.2f F=%.0f N v=%.1f m/s -> friction power %.0f W" % (mu, F, v, P))
    assert abs(P - 400.0) < 1e-9
    # dry steel (mu~0.5) would waste 6x the power
    assert abs(0.5 * F * v - 2500.0) < 1e-9
    print("OK: %s computed friction power loss" % ''' + _json.dumps(name) + ''')
if __name__ == "__main__":
    main()
'''


@_reg("tr_film")
def d_film(name, rid, group):
    return driver.demo_hdr(name, rid, group) + '''\
def main():
    # lambda ratio: film thickness / composite roughness -> regime check
    h_min = 0.8        # micrometers, min film thickness
    ra1, ra2 = 0.4, 0.4
    import math
    sigma = math.sqrt(ra1 ** 2 + ra2 ** 2)
    lam = h_min / sigma
    regime = "full film" if lam > 3 else ("mixed" if lam > 1 else "boundary")
    print("h_min=%.1f um sigma=%.3f um lambda=%.2f -> %s" % (h_min, sigma, lam, regime))
    assert abs(lam - 1.414) < 0.01, lam
    assert regime == "mixed"
    print("OK: %s evaluated the lambda ratio" % ''' + _json.dumps(name) + ''')
if __name__ == "__main__":
    main()
'''


@_reg("tr_grease")
def d_grease(name, rid, group):
    return driver.demo_hdr(name, rid, group) + '''\
def main():
    # grease relubrication interval estimate (simplified bearing-factor method)
    # interval_hours = K / (rpm * bore_mm^0.5)-style estimate; use catalog-style factor
    rpm, bore = 1500.0, 60.0
    factor = 1.4e7  # empirical factor for ball bearings, hours*rpm*sqrt(mm)
    import math
    interval = factor / (rpm * math.sqrt(bore))
    print("bearing %d mm at %.0f rpm -> relubrication interval ~%.0f hours" % (bore, rpm, interval))
    assert 900.0 < interval < 1400.0, interval
    print("OK: %s estimated a grease relubrication interval" % ''' + _json.dumps(name) + ''')
if __name__ == "__main__":
    main()
'''


@_reg("tr_oil")
def d_oil(name, rid, group):
    return driver.demo_hdr(name, rid, group) + '''\
def main():
    # oil analysis trending: iron ppm rising -> investigate
    fe = [8, 9, 11, 10, 14, 18, 25, 34]  # ppm over 8 samples
    warn, crit = 20, 40
    status = "critical" if fe[-1] >= crit else ("watch" if fe[-1] >= warn else "normal")
    trend_up = fe[-1] > fe[0] and sum(1 for a, b in zip(fe, fe[1:]) if b > a) >= 5
    print("Fe trend %s -> %d ppm: %s (rising: %s)" % (fe, fe[-1], status.upper(), trend_up))
    assert status == "watch" and trend_up
    print("OK: %s trended wear metals toward a maintenance decision" % ''' + _json.dumps(name) + ''')
if __name__ == "__main__":
    main()
'''


@_reg("tr_rough")
def d_rough(name, rid, group):
    return driver.demo_hdr(name, rid, group) + '''\
import math
def main():
    # Ra from a surface profile: mean absolute deviation from mean line
    profile = [0.42, -0.31, 0.55, -0.48, 0.36, -0.29, 0.51, -0.44,
               0.38, -0.33, 0.47, -0.40]
    mean = sum(profile) / len(profile)
    ra = sum(abs(x - mean) for x in profile) / len(profile)
    print("profile n=%d mean=%.3f Ra=%.3f micrometers" % (len(profile), mean, ra))
    assert abs(ra - 0.410) < 0.01, ra
    print("OK: %s computed Ra from a surface profile" % ''' + _json.dumps(name) + ''')
if __name__ == "__main__":
    main()
'''


@_reg("tr_coupon")
def d_coupon(name, rid, group):
    return driver.demo_hdr(name, rid, group) + '''\
def main():
    # 3D-printable pin-on-disk wear test coupon: printable directions + disclosed estimate
    # coupon: 30 mm dia x 8 mm disk; volume = pi r^2 h
    import math
    r, h = 15.0, 8.0  # mm
    vol_mm3 = math.pi * r ** 2 * h
    speed_mm3_s = 12.0
    t_min = vol_mm3 / speed_mm3_s / 60.0 * 1.25  # +25% overhead
    print("coupon dia %.0f mm x %.0f mm: volume %.0f mm^3" % (2 * r, h, vol_mm3))
    print("ESTIMATED print time %.0f min (0.2 mm layers, PETG, 40%% infill)" % t_min)
    print("DISCLOSED ESTIMATE ONLY: real time varies with printer and settings.")
    assert 8.0 < t_min < 16.0, t_min
    print("directions: print flat, 0.2 mm layers, test face up, deburr before testing")
    print("OK: %s specified a printable wear coupon with disclosed estimate" % ''' + _json.dumps(name) + ''')
if __name__ == "__main__":
    main()
'''


def main():
    return driver.run_pair(HERE, cfg_pub, cfg_sig, ENTRIES, DEMOS)


if __name__ == "__main__":
    sys.exit(0 if main() else 1)
