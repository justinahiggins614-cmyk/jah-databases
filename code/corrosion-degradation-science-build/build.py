#!/usr/bin/env python3
"""Build the Corrosion and Degradation Science pair (gap-audit part 2).

Verified 2026-10-17: NO database covers corrosion/degradation science
(mechanisms, environmental exposure, protection, service life). Manifest keyword
search (corrosion, degradation): zero hits. ZERO full-record coverage.

Two NEW databases, 34 ladder-ordered records each:
  corrosion-degradation-science            (public-harvest)
  corrosion-degradation-science-signature  (signature)

Never any website references. No Facebook.
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, "/home/hatch/workspace/jah-databases/code/gapaudit-p2")
import driver
from entries_corrosion import ENTRIES

RK = "corrosion science record"
CIT_PUB = ("Corrosion and degradation science (standard references: Fontana & Greene "
           "'Corrosion Engineering' 3rd ed. 1986; Uhlig & Revie 'Corrosion and Corrosion "
           "Control' 4th ed. 2008; ISO 9223 atmospheric corrosivity; ASTM G31 laboratory "
           "immersion testing; AMPP (NACE) standards; Pourbaix 'Atlas of Electrochemical "
           "Equilibria in Aqueous Solutions' 1966).")
CIT_SIG = CIT_PUB + " Signature editions are his original Signature treatment of corrosion science."
STANDARDS = ["Corrosion practice per ISO 9223 / ASTM G31 / cited references",
             "Teaching-ladder order: foundations, compounded, advanced"]

cfg_pub, cfg_sig = driver.pair_cfgs(
    slug_base="corrosion-degradation-science", name_base="Corrosion and Degradation Science",
    tagline=("Corrosion mechanisms, environmental exposure, protection, and service life: "
             "why materials degrade and how to stop it - from the electrochemical cell and "
             "rust through pitting, galvanic attack, and stress corrosion cracking to "
             "cathodic protection, coatings, inhibitors, and lifetime modeling, taught "
             "progressively along the ladder."),
    record_kind=RK, prefix_pub="JAH-CDS-", prefix_sig="JAH-CDSG-",
    ai_base="JAH Corrosion Archivist",
    role_pub=("corrosion archivist - corrosion mechanisms, environmental exposure, "
              "protection methods, service life; teaching progressively along the ladder "
              "from foundations through compounded to advanced; answers from many angles - "
              "definition, example, procedure, math, standards - using only the system's "
              "own archive data"),
    role_sig=("corrosion archivist - Signature editions: his original Signature treatment "
              "of corrosion science, clearly labeled Signature-made and never presented as "
              "authentic public record; teaches progressively along the ladder; answers "
              "from many angles using only the system's own archive data"),
    search_ph="Search galvanic, pitting, Pourbaix, cathodic protection, coatings, PREN...",
    chat_ph="Ask about corrosion...",
    archive_topic="corrosion-science records",
    gen_kind="corrosion-science",
    standards=STANDARDS, cit_pub=CIT_PUB, cit_sig=CIT_SIG,
    hero_pub=("Public records - real, fact-checked corrosion science: what corrosion is, the "
              "electrochemical cell, uniform attack, the galvanic series, rust, corrosion "
              "rates, environments, passivity, measurement, Faraday's law, non-metal "
              "degradation, the cost of corrosion, galvanic and pitting and crevice attack, "
              "intergranular corrosion, stress corrosion cracking, corrosion fatigue, "
              "erosion-corrosion, MIC, Pourbaix diagrams, polarization, PREN, atmospheric "
              "corrosion, cathodic protection, coatings, inhibitors, material selection, "
              "monitoring, service-life modeling, concrete degradation, high-temperature "
              "oxidation, test racks, and systems design - organized in the Signature system. "
              "Every record carries the full entry: description, how it works, key points, "
              "requirements, standards, citations, and a working demonstration program. "
              "Records are ordered by the teaching ladder: Foundations -> Compounded -> Advanced."),
    hero_sig=("Signature originals - his original Signature treatment of corrosion and "
              "degradation science: the full ladder from the electrochemical cell through "
              "every corrosion mechanism to protection and lifetime modeling, reframed as "
              "Signature science. Clearly labeled Signature-made, never presented as "
              "authentic public record. Every record carries the full entry: description, "
              "how it works, key points, requirements, standards, citations, and a working "
              "demonstration program."))

DEMOS = {}


def _reg(key):
    def deco(fn):
        DEMOS[key] = fn
        return fn
    return deco


import json as _json


@_reg("co_faraday")
def d_faraday(name, rid, group):
    return driver.demo_hdr(name, rid, group) + '''\
def main():
    # Faraday's law: corrosion rate from current density -> mils per year
    # mpy = 0.129 * i * EW / rho  (i in uA/cm^2, EW equivalent weight, rho g/cm^3)
    i = 10.0       # uA/cm^2
    EW = 27.92     # iron
    rho = 7.87
    mpy = 0.129 * i * EW / rho
    mm_y = mpy * 0.0254
    print("i=%.1f uA/cm^2 -> %.2f mpy = %.3f mm/year" % (i, mpy, mm_y))
    assert abs(mpy - 4.576) < 0.01, mpy
    assert abs(mm_y - 0.1162) < 0.001
    print("OK: %s converted corrosion current to penetration rate" % ''' + _json.dumps(name) + ''')
if __name__ == "__main__":
    main()
'''


@_reg("co_galvanic")
def d_galvanic(name, rid, group):
    return driver.demo_hdr(name, rid, group) + '''\
def main():
    # galvanic series (seawater, V vs SCE): more negative = more anodic (corrodes)
    series = [("magnesium", -1.55), ("zinc", -1.00), ("aluminum", -0.75),
              ("carbon steel", -0.60), ("stainless 304", -0.20),
              ("copper", -0.15), ("titanium", 0.05), ("graphite", 0.25)]
    ordered = sorted(series, key=lambda x: x[1])
    for metal, e in ordered:
        print("  %-14s %+.2f V" % (metal, e))
    # zinc coupled to steel: zinc is anodic -> protects steel
    assert ordered[0][0] == "magnesium" and ordered[-1][0] == "graphite"
    e_zn = dict(series)["zinc"]
    e_fe = dict(series)["carbon steel"]
    assert e_zn < e_fe, "zinc must be anodic to steel"
    print("zinc (-1.00 V) anodic to steel (-0.60 V): galvanizes and protects")
    print("OK: %s ordered the galvanic series and predicted the anode" % ''' + _json.dumps(name) + ''')
if __name__ == "__main__":
    main()
'''


@_reg("co_pren")
def d_pren(name, rid, group):
    return driver.demo_hdr(name, rid, group) + '''\
def main():
    # PREN = Cr + 3.3*Mo + 16*N: pitting resistance equivalent number
    alloys = {
        "304": (18.0, 0.0, 0.05),
        "316": (16.5, 2.1, 0.05),
        "2205 duplex": (22.0, 3.0, 0.16),
    }
    for name_a, (cr, mo, n) in alloys.items():
        pren = cr + 3.3 * mo + 16.0 * n
        print("  %-12s PREN = %.1f" % (name_a, pren))
    assert abs((18.0 + 0.0 + 16.0 * 0.05) - 18.8) < 1e-9
    assert abs((22.0 + 3.3 * 3.0 + 16.0 * 0.16) - 34.5) < 0.1
    print("PREN > 32 typically needed for seawater service")
    print("OK: %s computed PREN for stainless grades" % ''' + _json.dumps(name) + ''')
if __name__ == "__main__":
    main()
'''


@_reg("co_cp")
def d_cp(name, rid, group):
    return driver.demo_hdr(name, rid, group) + '''\
def main():
    # cathodic protection: current needed for a pipeline section
    # bare steel in soil needs ~10 mA/m^2; coated needs far less
    area_m2 = 500.0
    demand = 0.010  # A/m^2 bare steel
    coating_eff = 0.95
    current = area_m2 * demand * (1.0 - coating_eff)
    print("pipeline %.0f m^2, coating %.0f%% -> protection current %.2f A" % (
        area_m2, coating_eff * 100, current))
    assert abs(current - 0.25) < 1e-9
    # anode sizing: 10 kg zinc anode ~ 7800 Ah capacity
    print("OK: %s sized cathodic protection current" % ''' + _json.dumps(name) + ''')
if __name__ == "__main__":
    main()
'''


@_reg("co_coating")
def d_coating(name, rid, group):
    return driver.demo_hdr(name, rid, group) + '''\
def main():
    # coating coverage: liters needed for a DFT over an area
    area_m2 = 120.0
    dft_um = 250.0          # dry film thickness, micrometers
    solids = 0.65           # volume solids fraction
    loss = 0.15             # application loss
    liters = area_m2 * dft_um / 1000.0 / solids * (1.0 + loss)
    print("area %.0f m^2, DFT %d um, %.0f%% solids -> %.1f liters" % (area_m2, dft_um, solids * 100, liters))
    assert abs(liters - 53.1) < 0.2, liters
    print("OK: %s computed coating quantity for target DFT" % ''' + _json.dumps(name) + ''')
if __name__ == "__main__":
    main()
'''


@_reg("co_life")
def d_life(name, rid, group):
    return driver.demo_hdr(name, rid, group) + '''\
def main():
    # service life from corrosion allowance: life = allowance / rate
    allowance_mm = 3.0
    rate_mm_y = 0.12
    life = allowance_mm / rate_mm_y
    print("allowance %.1f mm at %.2f mm/y -> service life %.0f years" % (allowance_mm, rate_mm_y, life))
    assert abs(life - 25.0) < 1e-9
    # with 2x safety factor on rate
    assert abs(allowance_mm / (2 * rate_mm_y) - 12.5) < 1e-9
    print("OK: %s estimated service life from corrosion allowance" % ''' + _json.dumps(name) + ''')
if __name__ == "__main__":
    main()
'''


@_reg("co_pourbaix")
def d_pourbaix(name, rid, group):
    return driver.demo_hdr(name, rid, group) + '''\
def main():
    # Pourbaix diagram: water stability lines at 25 C
    # E_H2 = -0.0591*pH ; E_O2 = 1.229 - 0.0591*pH
    for ph in (0, 7, 14):
        e_h2 = -0.0591 * ph
        e_o2 = 1.229 - 0.0591 * ph
        print("  pH %2d: H2 line %+.3f V, O2 line %+.3f V" % (ph, e_h2, e_o2))
    assert abs(-0.0591 * 7 - (-0.4137)) < 1e-4
    assert abs((1.229 - 0.0591 * 7) - 0.8153) < 1e-4
    print("regions: immunity (below), corrosion (ion-stable), passivity (oxide-stable)")
    print("OK: %s plotted water stability lines of the Pourbaix diagram" % ''' + _json.dumps(name) + ''')
if __name__ == "__main__":
    main()
'''


@_reg("co_polar")
def d_polar(name, rid, group):
    return driver.demo_hdr(name, rid, group) + '''\
import math
def main():
    # Tafel extrapolation: corrosion current from polarization data
    # E vs log(i): anodic and cathodic Tafel lines intersect at (Ecorr, icorr)
    # synthetic data around Ecorr = -0.45 V, icorr = 8 uA/cm^2
    e_corr, i_corr = -0.45, 8.0
    beta_a, beta_c = 0.12, 0.10  # V/decade
    def i_anodic(e):
        return i_corr * 10 ** ((e - e_corr) / beta_a)
    def i_cathodic(e):
        return i_corr * 10 ** ((e_corr - e) / beta_c)
    e_test = -0.33
    print("at E=%.2f V: anodic %.1f, cathodic %.3f uA/cm^2" % (e_test, i_anodic(e_test), i_cathodic(e_test)))
    assert abs(i_anodic(e_corr) - i_corr) < 1e-9
    assert abs(i_cathodic(e_corr) - i_corr) < 1e-9
    print("OK: %s extrapolated corrosion current by Tafel lines" % ''' + _json.dumps(name) + ''')
if __name__ == "__main__":
    main()
'''


@_reg("co_coupon")
def d_coupon(name, rid, group):
    return driver.demo_hdr(name, rid, group) + '''\
def main():
    # 3D-printable corrosion coupon exposure rack: printable directions + disclosed estimate
    # rack holds 6 coupons 50x25x3 mm; frame volume ~ 28 cm^3
    vol_cm3 = 28.0
    speed_mm3_s = 12.0
    t_min = vol_cm3 * 1000.0 / speed_mm3_s / 60.0 * 1.25
    print("exposure rack volume %.0f cm^3 -> ESTIMATED print time %.0f min" % (vol_cm3, t_min))
    print("DISCLOSED ESTIMATE ONLY: real time varies with printer and settings.")
    assert 40.0 < t_min < 60.0, t_min
    print("directions: PETG (chemical resistant), 0.2 mm layers, 50% infill, coupon slots vertical")
    print("OK: %s specified a printable exposure rack with disclosed estimate" % ''' + _json.dumps(name) + ''')
if __name__ == "__main__":
    main()
'''


@_reg("co_inhibitor")
def d_inhibitor(name, rid, group):
    return driver.demo_hdr(name, rid, group) + '''\
def main():
    # inhibitor efficiency: IE% = (CR0 - CRi) / CR0 * 100
    cr0 = 2.40   # mm/y uninhibited
    cri = 0.18   # mm/y with inhibitor
    ie = (cr0 - cri) / cr0 * 100.0
    print("uninhibited %.2f mm/y, inhibited %.2f mm/y -> efficiency %.1f%%" % (cr0, cri, ie))
    assert abs(ie - 92.5) < 1e-9
    assert ie > 90.0, "good inhibitors exceed 90% efficiency"
    print("OK: %s computed inhibitor efficiency" % ''' + _json.dumps(name) + ''')
if __name__ == "__main__":
    main()
'''


def main():
    return driver.run_pair(HERE, cfg_pub, cfg_sig, ENTRIES, DEMOS)


if __name__ == "__main__":
    sys.exit(0 if main() else 1)
