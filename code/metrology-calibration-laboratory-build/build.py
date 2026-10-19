#!/usr/bin/env python3
"""Build the Metrology and Calibration Laboratory pair (gap-audit part 2).

Verified 2026-10-17: NO database covers the metrology/calibration laboratory
discipline (reference standards, traceability, calibration results, uncertainty).
Manifest: 'metrology-measurement-databases' is a 10-record META-CATALOG of
databases (not measurement practice); 'calibration-technologists-and-technicians'
covers the OCCUPATION (people records). ZERO full-record coverage of calibration
laboratory practice itself.

Two NEW databases, 34 ladder-ordered records each:
  metrology-calibration-laboratory            (public-harvest)
  metrology-calibration-laboratory-signature  (signature)

Never any website references. No Facebook.
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, "/home/hatch/workspace/jah-databases/code/gapaudit-p2")
import driver
from entries_metrology import ENTRIES

RK = "metrology record"
CIT_PUB = ("Metrology and calibration (standard references: JCGM 100:2008 (GUM) 'Guide to the "
           "expression of uncertainty in measurement'; JCGM 101:2008 (GUM Supplement 1, Monte "
           "Carlo); SI Brochure 9th ed. (BIPM); ISO/IEC 17025:2017 testing and calibration "
           "competence; NIST Handbook 150; OIML recommendations).")
CIT_SIG = CIT_PUB + " Signature editions are his original Signature treatment of metrology."
STANDARDS = ["Metrology practice per JCGM 100 (GUM) / ISO/IEC 17025 as cited",
             "Teaching-ladder order: foundations, compounded, advanced"]

cfg_pub, cfg_sig = driver.pair_cfgs(
    slug_base="metrology-calibration-laboratory", name_base="Metrology and Calibration Laboratory",
    tagline=("Reference standards, traceability, calibration results, and uncertainty: the "
             "science of getting measurements right - from the SI and traceability chains "
             "through gauge blocks, deadweight testers, and 17025 accreditation to "
             "uncertainty budgets, Monte Carlo evaluation, and quantum standards, taught "
             "progressively along the ladder."),
    record_kind=RK, prefix_pub="JAH-MCL-", prefix_sig="JAH-MCLS-",
    ai_base="JAH Metrology Archivist",
    role_pub=("metrology archivist - reference standards, traceability, calibration, "
              "uncertainty, accreditation; teaching progressively along the ladder from "
              "foundations through compounded to advanced; answers from many angles - "
              "definition, example, procedure, math, standards - using only the system's "
              "own archive data"),
    role_sig=("metrology archivist - Signature editions: his original Signature treatment "
              "of metrology, clearly labeled Signature-made and never presented as authentic "
              "public record; teaches progressively along the ladder; answers from many "
              "angles using only the system's own archive data"),
    search_ph="Search traceability, uncertainty, GUM, gauge blocks, 17025, deadweight...",
    chat_ph="Ask about metrology...",
    archive_topic="metrology records",
    gen_kind="metrology",
    standards=STANDARDS, cit_pub=CIT_PUB, cit_sig=CIT_SIG,
    hero_pub=("Public records - real, fact-checked metrology: what metrology is, the SI, "
              "traceability, calibration vs adjustment, uncertainty, Type A/B, the GUM, "
              "certificates, reference standards, units, rounding, the calibration lab, "
              "gauge blocks, temperature and pressure and electrical and mass calibration, "
              "intervals, as-found/as-left, measurement assurance, intercomparisons, ISO "
              "17025, CMC, environmental controls, uncertainty budgets, Monte Carlo, curve "
              "fitting, drift analysis, software validation, thermal effects, quantum "
              "standards, time/frequency, printable fixtures, and the national system - "
              "organized in the Signature system. Every record carries the full entry: "
              "description, how it works, key points, requirements, standards, citations, "
              "and a working demonstration program. Records are ordered by the teaching "
              "ladder: Foundations -> Compounded -> Advanced."),
    hero_sig=("Signature originals - his original Signature treatment of metrology and "
              "calibration: the full ladder from the SI and traceability through every "
              "calibration discipline to quantum standards, reframed as Signature science. "
              "Clearly labeled Signature-made, never presented as authentic public record. "
              "Every record carries the full entry: description, how it works, key points, "
              "requirements, standards, citations, and a working demonstration program."))

DEMOS = {}


def _reg(key):
    def deco(fn):
        DEMOS[key] = fn
        return fn
    return deco


import json as _json


@_reg("me_gum")
def d_gum(name, rid, group):
    return driver.demo_hdr(name, rid, group) + '''\
import math
def main():
    # GUM: combined standard uncertainty from components, then expanded k=2
    components = [
        ("repeatability (A)", 0.0042),
        ("calibration cert (B)", 0.0058),
        ("resolution (B)", 0.0029),
        ("temperature (B)", 0.0015),
    ]
    uc = math.sqrt(sum(u ** 2 for _, u in components))
    U = 2.0 * uc
    for label, u in components:
        print("  %-22s u = %.4f" % (label, u))
    print("combined uc = %.4f, expanded U(k=2) = %.4f" % (uc, U))
    assert abs(uc - 0.00787) < 1e-4, uc
    assert abs(U - 0.01574) < 1e-4
    print("OK: %s combined uncertainties per the GUM" % ''' + _json.dumps(name) + ''')
if __name__ == "__main__":
    main()
'''


@_reg("me_trace")
def d_trace(name, rid, group):
    return driver.demo_hdr(name, rid, group) + '''\
def main():
    # traceability chain: each link calibrated by the one above, uncertainties growing
    chain = [
        ("SI definition (BIPM)", 0.0),
        ("NMI primary standard", 0.5),
        ("accredited lab reference", 1.5),
        ("working standard", 4.0),
        ("shop floor instrument", 12.0),
    ]
    print("traceability chain (uncertainties in ppm):")
    for i, (link, u) in enumerate(chain):
        print("  %d. %-28s u=%s" % (i, link, u if u else "defined"))
    us = [u for _, u in chain[1:]]
    assert all(b >= a for a, b in zip(us, us[1:])), "uncertainty must grow down the chain"
    assert us[-1] == 12.0
    print("OK: %s verified an unbroken traceability chain" % ''' + _json.dumps(name) + ''')
if __name__ == "__main__":
    main()
'''


@_reg("me_gauge")
def d_gauge(name, rid, group):
    return driver.demo_hdr(name, rid, group) + '''\
def main():
    # gauge block stack: wring blocks to make 41.5 mm; stack uncertainty
    blocks = [40.0, 1.5]  # mm
    total = sum(blocks)
    u_each = 0.00015  # mm per block
    import math
    u_stack = math.sqrt(len(blocks) * u_each ** 2)
    print("stack %s = %.1f mm, u = %.5f mm" % (blocks, total, u_stack))
    assert abs(total - 41.5) < 1e-9
    assert abs(u_stack - 0.000212) < 1e-5, u_stack
    print("OK: %s stacked gauge blocks with uncertainty" % ''' + _json.dumps(name) + ''')
if __name__ == "__main__":
    main()
'''


@_reg("me_interval")
def d_interval(name, rid, group):
    return driver.demo_hdr(name, rid, group) + '''\
def main():
    # calibration interval from drift: interval = tolerance / drift_rate * safety
    drift_per_year = 0.004   # units/year
    tolerance = 0.02
    safety = 0.5
    interval_y = tolerance / drift_per_year * safety
    print("drift %.3f/y, tolerance %.2f -> interval %.1f years" % (drift_per_year, tolerance, interval_y))
    assert abs(interval_y - 2.5) < 1e-9
    print("OK: %s set a drift-based calibration interval" % ''' + _json.dumps(name) + ''')
if __name__ == "__main__":
    main()
'''


@_reg("me_en")
def d_en(name, rid, group):
    return driver.demo_hdr(name, rid, group) + '''\
import math
def main():
    # En value for interlaboratory comparison: |x1-x2| / sqrt(U1^2+U2^2) <= 1 passes
    x1, U1 = 10.002, 0.006
    x2, U2 = 9.998, 0.006
    en = abs(x1 - x2) / math.sqrt(U1 ** 2 + U2 ** 2)
    print("lab1 %.3f +/- %.3f, lab2 %.3f +/- %.3f -> En = %.2f (%s)" % (
        x1, U1, x2, U2, en, "PASS" if en <= 1 else "FAIL"))
    assert abs(en - 0.471) < 0.01, en
    assert en <= 1.0
    print("OK: %s scored an interlaboratory comparison with En" % ''' + _json.dumps(name) + ''')
if __name__ == "__main__":
    main()
'''


@_reg("me_calcurve")
def d_calcurve(name, rid, group):
    return driver.demo_hdr(name, rid, group) + '''\
def main():
    # calibration curve: linear fit of instrument reading vs standard
    std = [0.0, 5.0, 10.0, 15.0, 20.0]
    rdg = [0.02, 5.03, 10.01, 15.04, 20.02]
    n = len(std)
    mx, my = sum(std) / n, sum(rdg) / n
    b = sum((x - mx) * (y - my) for x, y in zip(std, rdg)) / sum((x - mx) ** 2 for x in std)
    a = my - b * mx
    print("correction: true = %.4f + %.5f * reading" % (a, b))
    # apply correction to a new reading
    new_rdg = 12.50
    corrected = a + b * new_rdg
    print("reading %.2f -> corrected %.3f" % (new_rdg, corrected))
    assert abs(b - 1.0) < 0.002, b
    assert abs(corrected - 12.5245) < 0.005, corrected
    print("OK: %s fitted and applied a calibration curve" % ''' + _json.dumps(name) + ''')
if __name__ == "__main__":
    main()
'''


@_reg("me_cmc")
def d_cmc(name, rid, group):
    return driver.demo_hdr(name, rid, group) + '''\
def main():
    # CMC: smallest uncertainty the lab can claim, vs customer requirement
    cmc = {"dc_voltage_10V": 2.5e-6, "resistance_1k": 8e-6, "mass_1kg": 0.5e-6}
    jobs = [("dc_voltage_10V", 5e-6), ("resistance_1k", 5e-6), ("mass_1kg", 1e-6)]
    for param, need in jobs:
        ok = cmc[param] <= need
        print("  %-16s CMC %.1e <= need %.1e -> %s" % (param, cmc[param], need, "ACCEPT" if ok else "DECLINE"))
    assert cmc["dc_voltage_10V"] <= 5e-6
    assert not (cmc["resistance_1k"] <= 5e-6)
    print("OK: %s checked jobs against CMC claims" % ''' + _json.dumps(name) + ''')
if __name__ == "__main__":
    main()
'''


@_reg("me_temp")
def d_temp(name, rid, group):
    return driver.demo_hdr(name, rid, group) + '''\
def main():
    # temperature correction: steel part measured at 24 C, report at 20 C
    # L20 = L_T / (1 + alpha*(T-20))
    L_T = 100.023   # mm measured at 24 C
    alpha = 11.5e-6 # /C for steel
    T = 24.0
    L20 = L_T / (1.0 + alpha * (T - 20.0))
    print("measured %.3f mm at %.0f C -> %.4f mm at 20 C" % (L_T, T, L20))
    assert abs(L20 - 100.0184) < 1e-3, L20
    print("OK: %s corrected a length to reference temperature" % ''' + _json.dumps(name) + ''')
if __name__ == "__main__":
    main()
'''


@_reg("me_pressure")
def d_pressure(name, rid, group):
    return driver.demo_hdr(name, rid, group) + '''\
def main():
    # deadweight tester: p = m*g / A
    m = 10.0        # kg
    g = 9.80665
    A = 1e-4        # m^2 piston area
    p = m * g / A   # Pa
    print("mass %.1f kg on %.0f mm^2 -> %.3f MPa" % (m, A * 1e6, p / 1e6))
    assert abs(p / 1e6 - 0.980665) < 1e-6
    print("OK: %s computed deadweight pressure from first principles" % ''' + _json.dumps(name) + ''')
if __name__ == "__main__":
    main()
'''


@_reg("me_round")
def d_round(name, rid, group):
    return driver.demo_hdr(name, rid, group) + '''\
def main():
    # report uncertainty with 2 significant figures; round value to match
    def fmt(value, u):
        import math
        digits = 2
        exp = math.floor(math.log10(u)) - digits + 1
        u_r = round(u / 10 ** exp) * 10 ** exp
        v_r = round(value / 10 ** exp) * 10 ** exp
        return v_r, u_r
    v, u = fmt(10.0234, 0.00804)
    print("reported: %.3f +/- %.5f" % (v, u))
    assert abs(u - 0.0080) < 1e-9, u
    assert abs(v - 10.0234) < 1e-9, v
    print("OK: %s rounded a result to its uncertainty" % ''' + _json.dumps(name) + ''')
if __name__ == "__main__":
    main()
'''


def main():
    return driver.run_pair(HERE, cfg_pub, cfg_sig, ENTRIES, DEMOS)


if __name__ == "__main__":
    sys.exit(0 if main() else 1)
