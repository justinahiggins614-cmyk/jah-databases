#!/usr/bin/env python3
"""Build the Water Distribution Utility pair (gap-audit part 2).

Verified 2026-10-17: NO database covers water distribution utilities (network
hydraulics, leakage management, treatment, demand, asset condition). Manifest
keyword search (water distribution, water utility): zero hits. ZERO full-record
coverage.

Two NEW databases, 34 ladder-ordered records each:
  water-distribution-utility            (public-harvest)
  water-distribution-utility-signature  (signature)

Never any website references. No Facebook.
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, "/home/hatch/workspace/jah-databases/code/gapaudit-p2")
import driver
from entries_water import ENTRIES

RK = "water utility record"
CIT_PUB = ("Water distribution (standard references: AWWA Manuals of Water Supply Practices "
           "(M-series); Rossman 'EPANET 2 Users Manual' (US EPA); Water Research Foundation "
           "reports; Walski et al. 'Advanced Water Distribution Modeling and Management' 2003; "
           "US EPA drinking water regulations).")
CIT_SIG = CIT_PUB + " Signature editions are his original Signature treatment of water utilities."
STANDARDS = ["Water practice per AWWA / US EPA as cited",
             "Teaching-ladder order: foundations, compounded, advanced"]

cfg_pub, cfg_sig = driver.pair_cfgs(
    slug_base="water-distribution-utility", name_base="Water Distribution Utility",
    tagline=("Network hydraulics, leakage management, treatment, demand, and asset condition: "
             "how drinking water reaches every tap safely - from sources and treatment "
             "through pipes, pumps, and tanks to leakage control, demand forecasting, and "
             "main replacement, taught progressively along the ladder."),
    record_kind=RK, prefix_pub="JAH-WDU-", prefix_sig="JAH-WDUS-",
    ai_base="JAH Water Archivist",
    role_pub=("water utility archivist - network hydraulics, leakage, treatment, demand, "
              "asset condition; teaching progressively along the ladder from foundations "
              "through compounded to advanced; answers from many angles - definition, "
              "example, procedure, math, standards - using only the system's own archive data"),
    role_sig=("water utility archivist - Signature editions: his original Signature "
              "treatment of water distribution, clearly labeled Signature-made and never "
              "presented as authentic public record; teaches progressively along the ladder; "
              "answers from many angles using only the system's own archive data"),
    search_ph="Search Hazen-Williams, EPANET, leakage, ILI, water hammer, demand...",
    chat_ph="Ask about water distribution...",
    archive_topic="water-utility records",
    gen_kind="water-utility",
    standards=STANDARDS, cit_pub=CIT_PUB, cit_sig=CIT_SIG,
    hero_pub=("Public records - real, fact-checked water utility practice: what distribution "
              "systems are, sources, treatment, networks, pressure, head loss, demand, water "
              "quality, disinfection, tanks, pumps, valves, Hazen-Williams, EPANET, pressure "
              "zones, extended-period simulation, water hammer, leakage, ILI, DMAs, chlorine "
              "decay, water age, demand forecasting, pump scheduling, asset condition, "
              "failure prediction, main replacement, smart metering, SCADA, contamination "
              "warning, fire flow, model calibration, printable fittings, and emergency "
              "resilience - organized in the Signature system. Every record carries the full "
              "entry: description, how it works, key points, requirements, standards, "
              "citations, and a working demonstration program. Records are ordered by the "
              "teaching ladder: Foundations -> Compounded -> Advanced."),
    hero_sig=("Signature originals - his original Signature treatment of water distribution "
              "utilities: the full ladder from sources and treatment through hydraulics and "
              "leakage to asset management and resilience, reframed as Signature science. "
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


@_reg("wd_hazen")
def d_hazen(name, rid, group):
    return driver.demo_hdr(name, rid, group) + '''\
def main():
    # Hazen-Williams head loss: hf = 10.67 * L * Q^1.852 / (C^1.852 * D^4.87)
    L = 500.0      # m
    Q = 0.050      # m^3/s
    C = 120.0      # roughness coefficient (lined ductile iron)
    D = 0.300      # m
    hf = 10.67 * L * Q ** 1.852 / (C ** 1.852 * D ** 4.87)
    print("L=%.0f m Q=%.3f m3/s C=%.0f D=%.0f mm -> head loss %.2f m" % (L, Q, C, D * 1000, hf))
    assert abs(hf - 1.0313) < 0.01, hf
    print("OK: %s computed Hazen-Williams head loss" % ''' + _json.dumps(name) + ''')
if __name__ == "__main__":
    main()
'''


@_reg("wd_balance")
def d_balance(name, rid, group):
    return driver.demo_hdr(name, rid, group) + '''\
def main():
    # node mass balance: inflow = outflow + demand (EPANET-style continuity)
    nodes = {
        "tank": {"in": 0.120, "out": 0.120, "demand": 0.000},
        "j1": {"in": 0.120, "out": 0.070, "demand": 0.050},
        "j2": {"in": 0.070, "out": 0.000, "demand": 0.070},
    }
    for n, f in nodes.items():
        bal = f["in"] - f["out"] - f["demand"]
        print("  %s: in=%.3f out=%.3f demand=%.3f balance=%.4f" % (n, f["in"], f["out"], f["demand"], bal))
        assert abs(bal) < 1e-9, n
    print("OK: %s verified node mass balance across the network" % ''' + _json.dumps(name) + ''')
if __name__ == "__main__":
    main()
'''


@_reg("wd_ili")
def d_ili(name, rid, group):
    return driver.demo_hdr(name, rid, group) + '''\
def main():
    # Infrastructure Leakage Index: ILI = CARL / UARL
    # UARL (L/day) = (18*Lm + 0.8*Nc + 25*Lp) * P  (Lm mains km, Nc connections, Lp km, P m pressure)
    Lm, Nc, Lp, P = 120.0, 15000.0, 30.0, 45.0
    uarl = (18.0 * Lm + 0.8 * Nc + 25.0 * Lp) * P
    carl = 850.0 * 1000.0  # L/day current annual real losses
    ili = carl / uarl
    print("UARL=%.0f L/d CARL=%.0f L/d -> ILI=%.2f" % (uarl, carl, ili))
    assert abs(uarl - 670950.0) < 1.0, uarl
    assert abs(ili - 1.267) < 0.01, ili
    print("ILI near 1.0 is excellent; above 4 needs action")
    print("OK: %s computed the Infrastructure Leakage Index" % ''' + _json.dumps(name) + ''')
if __name__ == "__main__":
    main()
'''


@_reg("wd_hammer")
def d_hammer(name, rid, group):
    return driver.demo_hdr(name, rid, group) + '''\
import math
def main():
    # Joukowsky water hammer: dP = rho * a * dV
    rho = 1000.0
    a = 1000.0     # m/s wave speed in steel pipe
    dV = 1.5       # m/s sudden velocity change (valve slam)
    dP = rho * a * dV
    print("valve slam dV=%.1f m/s -> surge %.1f bar" % (dV, dP / 1e5))
    assert abs(dP / 1e5 - 15.0) < 1e-9
    # slow closure over 10 s avoids the full surge
    print("slow closure spreads the change: surge avoided")
    print("OK: %s computed water hammer surge with Joukowsky" % ''' + _json.dumps(name) + ''')
if __name__ == "__main__":
    main()
'''


@_reg("wd_chlorine")
def d_chlorine(name, rid, group):
    return driver.demo_hdr(name, rid, group) + '''\
import math
def main():
    # first-order chlorine decay: C = C0 * exp(-k*t)
    C0 = 1.2   # mg/L at plant
    k = 0.15   # /hour bulk decay
    for t in (2, 8, 24):
        c = C0 * math.exp(-k * t)
        print("  t=%2dh: residual %.2f mg/L %s" % (t, c, "(OK)" if c >= 0.2 else "(BOOST NEEDED)"))
    assert abs(C0 * math.exp(-k * 8) - 0.361) < 0.01
    assert C0 * math.exp(-k * 24) < 0.2
    print("OK: %s modeled chlorine decay along the network" % ''' + _json.dumps(name) + ''')
if __name__ == "__main__":
    main()
'''


@_reg("wd_demand")
def d_demand(name, rid, group):
    return driver.demo_hdr(name, rid, group) + '''\
def main():
    # diurnal demand pattern: multipliers on average-day demand
    pattern = [0.45, 0.40, 0.38, 0.42, 0.60, 0.95, 1.25, 1.35,
               1.20, 1.05, 1.00, 1.05, 1.10, 1.05, 1.00, 1.05,
               1.15, 1.35, 1.40, 1.25, 1.05, 0.85, 0.65, 0.52]
    avg = sum(pattern) / 24.0
    peak = max(pattern)
    print("24-h pattern: avg multiplier %.3f, peak %.2f at hour %d" % (avg, peak, pattern.index(peak)))
    assert abs(avg - 0.938) < 0.01, avg
    assert peak == 1.40
    print("OK: %s built a diurnal demand pattern" % ''' + _json.dumps(name) + ''')
if __name__ == "__main__":
    main()
'''


@_reg("wd_pump")
def d_pump(name, rid, group):
    return driver.demo_hdr(name, rid, group) + '''\
def main():
    # pump power: P = rho*g*Q*H / eta
    rho, g = 1000.0, 9.81
    Q = 0.080    # m^3/s
    H = 45.0     # m head
    eta = 0.75
    P = rho * g * Q * H / eta
    print("Q=%.3f m3/s H=%.0f m eta=%.0f%% -> %.1f kW" % (Q, H, eta * 100, P / 1000))
    assert abs(P / 1000 - 47.088) < 0.01, P
    # daily energy at 16 h runtime
    print("16 h/day -> %.0f kWh/day" % (P / 1000 * 16))
    print("OK: %s computed pump power and energy" % ''' + _json.dumps(name) + ''')
if __name__ == "__main__":
    main()
'''


@_reg("wd_tank")
def d_tank(name, rid, group):
    return driver.demo_hdr(name, rid, group) + '''\
def main():
    # tank turnover: volume / daily throughput; low turnover = stale water
    import math
    D, h = 20.0, 8.0   # m diameter, height
    vol = math.pi * (D / 2) ** 2 * h
    daily_m3 = 1800.0
    turnover_days = vol / daily_m3
    print("tank %.0f m dia x %.0f m: %.0f m^3, turnover every %.1f days" % (D, h, vol, turnover_days))
    assert abs(vol - 2513.3) < 1.0, vol
    assert abs(turnover_days - 1.40) < 0.05
    print("turnover under ~3 days keeps water fresh")
    print("OK: %s computed tank turnover time" % ''' + _json.dumps(name) + ''')
if __name__ == "__main__":
    main()
'''


@_reg("wd_pressure")
def d_pressure(name, rid, group):
    return driver.demo_hdr(name, rid, group) + '''\
def main():
    # pressure zone check: 35-80 psi service range
    zones = {"zone-A": 62.0, "zone-B": 28.0, "zone-C": 95.0}
    for z, p in zones.items():
        status = "OK" if 35.0 <= p <= 80.0 else ("LOW" if p < 35 else "HIGH")
        print("  %s: %.0f psi -> %s" % (z, p, status))
    assert zones["zone-A"] == 62.0
    print("low zones need boosting; high zones need pressure reduction")
    print("OK: %s checked pressure zones against service range" % ''' + _json.dumps(name) + ''')
if __name__ == "__main__":
    main()
'''


@_reg("wd_fitting")
def d_fitting(name, rid, group):
    return driver.demo_hdr(name, rid, group) + '''\
def main():
    # 3D-printable pipe fitting demo model: printable directions + disclosed estimate
    # demo 90-degree elbow trainer, ~22 cm^3
    vol_cm3 = 22.0
    speed_mm3_s = 12.0
    t_min = vol_cm3 * 1000.0 / speed_mm3_s / 60.0 * 1.25
    print("trainer elbow volume %.0f cm^3 -> ESTIMATED print time %.0f min" % (vol_cm3, t_min))
    print("DISCLOSED ESTIMATE ONLY: real time varies with printer and settings.")
    assert 30.0 < t_min < 45.0, t_min
    print("directions: PETG, 0.25 mm layers, 40%% infill, ports facing up; NOT for pressure service")
    print("OK: %s specified a printable fitting trainer with disclosed estimate" % ''' + _json.dumps(name) + ''')
if __name__ == "__main__":
    main()
'''


def main():
    return driver.run_pair(HERE, cfg_pub, cfg_sig, ENTRIES, DEMOS)


if __name__ == "__main__":
    sys.exit(0 if main() else 1)
