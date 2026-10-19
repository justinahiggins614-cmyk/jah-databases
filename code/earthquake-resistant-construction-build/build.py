#!/usr/bin/env python3
"""Build the Earthquake-Resistant Construction pair (gap-audit part 2).

Verified 2026-10-17: NO database covers earthquake-resistant construction
(seismic design, ground motion, structural response, retrofit methods). Manifest:
'earthquake-prediction' is a Signature FUN/FUTURES database (prediction
entertainment, 85 records) - different discipline entirely. ZERO full-record
coverage of seismic design/construction.

Two NEW databases, 34 ladder-ordered records each:
  earthquake-resistant-construction            (public-harvest)
  earthquake-resistant-construction-signature  (signature)

Never any website references. No Facebook.
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, "/home/hatch/workspace/jah-databases/code/gapaudit-p2")
import driver
from entries_earthquake import ENTRIES

RK = "seismic construction record"
CIT_PUB = ("Earthquake-resistant construction (standard references: ASCE/SEI 7-22 'Minimum "
           "Design Loads and Associated Criteria for Buildings'; ACI 318 building code; "
           "FEMA P-58 seismic performance assessment; Chopra 'Dynamics of Structures' 5th ed. "
           "2020; Kramer 'Geotechnical Earthquake Engineering' 1996; IBC International "
           "Building Code).")
CIT_SIG = CIT_PUB + " Signature editions are his original Signature treatment of seismic construction."
STANDARDS = ["Seismic practice per ASCE 7 / ACI 318 as cited",
             "Teaching-ladder order: foundations, compounded, advanced"]

cfg_pub, cfg_sig = driver.pair_cfgs(
    slug_base="earthquake-resistant-construction", name_base="Earthquake-Resistant Construction",
    tagline=("Seismic design, ground motion, structural response, and retrofit methods: how "
             "buildings survive earthquakes - from plate tectonics and response spectra "
             "through moment frames, shear walls, and ductile detailing to base isolation, "
             "dampers, and retrofit, taught progressively along the ladder."),
    record_kind=RK, prefix_pub="JAH-EQR-", prefix_sig="JAH-EQRS-",
    ai_base="JAH Seismic Archivist",
    role_pub=("seismic construction archivist - seismic design, ground motion, structural "
              "response, retrofit methods; teaching progressively along the ladder from "
              "foundations through compounded to advanced; answers from many angles - "
              "definition, example, procedure, math, standards - using only the system's "
              "own archive data"),
    role_sig=("seismic construction archivist - Signature editions: his original Signature "
              "treatment of earthquake-resistant construction, clearly labeled "
              "Signature-made and never presented as authentic public record; teaches "
              "progressively along the ladder; answers from many angles using only the "
              "system's own archive data"),
    search_ph="Search base shear, response spectrum, drift, isolation, retrofit, liquefaction...",
    chat_ph="Ask about earthquake-resistant construction...",
    archive_topic="seismic-construction records",
    gen_kind="seismic-construction",
    standards=STANDARDS, cit_pub=CIT_PUB, cit_sig=CIT_SIG,
    hero_pub=("Public records - real, fact-checked seismic construction: what "
              "earthquake-resistant construction is, plate tectonics, seismic waves, "
              "magnitude and intensity, SDOF response, resonance, inertia forces, ductility, "
              "response spectra, site effects, liquefaction, nonstructural risk, equivalent "
              "lateral force, base shear, drift limits, load paths, moment frames, shear "
              "walls, braced frames, diaphragms, foundations, detailing, seismic design "
              "categories, ASCE 7, response spectrum analysis, base isolation, dampers, "
              "soil-structure interaction, liquefaction mitigation, concrete jacketing, FRP "
              "wrapping, steel bracing retrofit, printable structural models, and "
              "performance-based design - organized in the Signature system. Every record "
              "carries the full entry: description, how it works, key points, requirements, "
              "standards, citations, and a working demonstration program. Records are ordered "
              "by the teaching ladder: Foundations -> Compounded -> Advanced."),
    hero_sig=("Signature originals - his original Signature treatment of "
              "earthquake-resistant construction: the full ladder from ground motion through "
              "structural systems to isolation and retrofit, reframed as Signature science. "
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


@_reg("eq_sdof")
def d_sdof(name, rid, group):
    return driver.demo_hdr(name, rid, group) + '''\
import math
def main():
    # SDOF: natural period from mass and stiffness; T = 2*pi*sqrt(m/k)
    m = 50000.0    # kg (one floor)
    k = 2.0e7      # N/m lateral stiffness
    T = 2.0 * math.pi * math.sqrt(m / k)
    f = 1.0 / T
    print("floor mass %.0f kg, stiffness %.1e N/m -> T=%.3f s (f=%.2f Hz)" % (m, k, T, f))
    assert abs(T - 0.314) < 0.005, T
    # stiffer -> shorter period
    T2 = 2.0 * math.pi * math.sqrt(m / (4.0 * k))
    assert abs(T2 - T / 2.0) < 1e-9
    print("OK: %s computed SDOF natural period" % ''' + _json.dumps(name) + ''')
if __name__ == "__main__":
    main()
'''


@_reg("eq_baseshear")
def d_baseshear(name, rid, group):
    return driver.demo_hdr(name, rid, group) + '''\
def main():
    # equivalent lateral force: V = Cs * W
    W = 12000.0    # kN seismic weight
    SDS = 1.0      # design spectral acceleration
    R = 8.0        # response modification (special moment frame)
    Ie = 1.0
    Cs = SDS / (R / Ie)
    # Cs need not exceed SDS/(R/Ie); cap and floor per ASCE 7 (simplified)
    V = Cs * W
    print("W=%.0f kN SDS=%.2f R=%.0f -> Cs=%.4f V=%.0f kN" % (W, SDS, R, Cs, V))
    assert abs(Cs - 0.125) < 1e-9
    assert abs(V - 1500.0) < 1e-9
    print("OK: %s computed seismic base shear" % ''' + _json.dumps(name) + ''')
if __name__ == "__main__":
    main()
'''


@_reg("eq_drift")
def d_drift(name, rid, group):
    return driver.demo_hdr(name, rid, group) + '''\
def main():
    # story drift check: drift ratio <= 0.02 for most occupancies (ASCE 7)
    story_h = 4.0  # m
    disp_top, disp_bot = 0.055, 0.015  # m elastic displacements
    Cd = 5.5       # deflection amplification
    Ie = 1.0
    drift = (disp_top - disp_bot) * Cd / Ie
    ratio = drift / story_h
    print("story drift %.3f m over %.1f m -> ratio %.4f (limit 0.020)" % (drift, story_h, ratio))
    print("  -> %s" % ("PASS" if ratio <= 0.020 else "FAIL"))
    assert abs(ratio - 0.055) < 1e-9, ratio
    assert abs(drift - 0.22) < 1e-9, drift
    assert ratio > 0.020  # this example fails -> stiffen the frame
    print("OK: %s checked story drift against ASCE 7 limits" % ''' + _json.dumps(name) + ''')
if __name__ == "__main__":
    main()
'''


@_reg("eq_liquefaction")
def d_liquefaction(name, rid, group):
    return driver.demo_hdr(name, rid, group) + '''\
def main():
    # simplified liquefaction screening: factor of safety = CRR / CSR
    # CSR ~ 0.65 * (amax/g) * (sv/sv') * rd ; CRR from SPT-based curve (simplified)
    amax_g = 0.30
    sv, svp = 120.0, 70.0   # kPa total / effective stress
    rd = 0.95
    CSR = 0.65 * amax_g * (sv / svp) * rd
    CRR = 0.18              # from corrected SPT blow count (simplified)
    FS = CRR / CSR
    print("CSR=%.3f CRR=%.2f -> FS=%.2f (%s)" % (CSR, CRR, FS, "LIQUEFACTION RISK" if FS < 1.0 else "OK"))
    assert abs(CSR - 0.318) < 0.01, CSR
    assert FS < 1.0  # this layer is at risk -> mitigate
    print("OK: %s screened liquefaction with factor of safety" % ''' + _json.dumps(name) + ''')
if __name__ == "__main__":
    main()
'''


@_reg("eq_isolation")
def d_isolation(name, rid, group):
    return driver.demo_hdr(name, rid, group) + '''\
import math
def main():
    # base isolation: lengthen period to cut spectral acceleration
    # T_isolated = 2.5 s vs T_fixed = 0.5 s; Sa roughly proportional to 1/T in velocity region
    T_fixed, T_iso = 0.5, 2.5
    Sa_fixed = 1.0   # g
    Sa_iso = Sa_fixed * (T_fixed / T_iso)
    print("fixed T=%.1f s Sa=%.2fg -> isolated T=%.1f s Sa=%.2fg (%.0f%% cut)" % (
        T_fixed, Sa_fixed, T_iso, Sa_iso, (1 - Sa_iso / Sa_fixed) * 100))
    assert abs(Sa_iso - 0.20) < 1e-9
    # isolator displacement demand
    g = 9.81
    D = Sa_iso * g * T_iso ** 2 / (4 * math.pi ** 2)
    print("isolator displacement demand ~%.2f m" % D)
    assert 0.2 < D < 0.5, D
    print("OK: %s showed isolation cutting spectral demand" % ''' + _json.dumps(name) + ''')
if __name__ == "__main__":
    main()
'''


@_reg("eq_spectrum")
def d_spectrum(name, rid, group):
    return driver.demo_hdr(name, rid, group) + '''\
def main():
    # ASCE 7 design spectrum (simplified): Sa = SDS for T <= Ts, = SD1/T beyond
    SDS, SD1 = 1.0, 0.6
    Ts = SD1 / SDS
    def Sa(T):
        if T <= Ts:
            return SDS
        return SD1 / T
    for T in (0.2, 0.6, 1.0, 2.0):
        print("  T=%.1f s -> Sa=%.3f g" % (T, Sa(T)))
    assert abs(Sa(0.2) - 1.0) < 1e-9
    assert abs(Sa(2.0) - 0.3) < 1e-9
    print("OK: %s built a design response spectrum" % ''' + _json.dumps(name) + ''')
if __name__ == "__main__":
    main()
'''


@_reg("eq_ductility")
def d_ductility(name, rid, group):
    return driver.demo_hdr(name, rid, group) + '''\
def main():
    # R factor: design for V_elastic / R, relying on ductility
    V_elastic = 6000.0  # kN if fully elastic
    systems = {"ordinary moment frame": 3.5, "intermediate moment frame": 4.5,
               "special moment frame": 8.0, "special shear wall": 6.0}
    for name_s, R in systems.items():
        print("  %-24s R=%.1f -> design V=%.0f kN" % (name_s, R, V_elastic / R))
    assert abs(V_elastic / 8.0 - 750.0) < 1e-9
    print("higher R needs stricter ductile detailing - the trade is explicit")
    print("OK: %s applied response modification factors" % ''' + _json.dumps(name) + ''')
if __name__ == "__main__":
    main()
'''


@_reg("eq_retrofit")
def d_retrofit(name, rid, group):
    return driver.demo_hdr(name, rid, group) + '''\
def main():
    # column jacketing: capacity gain from added concrete and ties
    cap_before = 400.0   # kN shear capacity
    # jacket adds 100 mm each face; shear capacity scales with area and confinement
    gain_factor = 1.8
    cap_after = cap_before * gain_factor
    demand = 650.0
    print("capacity %.0f -> %.0f kN vs demand %.0f kN: %s" % (
        cap_before, cap_after, demand, "ADEQUATE" if cap_after >= demand else "STILL SHORT"))
    assert abs(cap_after - 720.0) < 1e-9
    assert cap_after >= demand
    print("OK: %s sized a jacketing retrofit to meet demand" % ''' + _json.dumps(name) + ''')
if __name__ == "__main__":
    main()
'''


@_reg("eq_soil")
def d_soil(name, rid, group):
    return driver.demo_hdr(name, rid, group) + '''\
def main():
    # site class from Vs30 (m/s): ASCE 7 simplified boundaries
    def site_class(vs30):
        if vs30 > 760: return "B (rock)"
        if vs30 > 360: return "C (very dense soil/soft rock)"
        if vs30 > 180: return "D (stiff soil)"
        return "E (soft clay)"
    for vs in (900, 500, 250, 120):
        print("  Vs30=%d m/s -> site class %s" % (vs, site_class(vs)))
    assert site_class(250) == "D (stiff soil)"
    assert site_class(120) == "E (soft clay)"
    print("softer sites amplify shaking: site factors scale the spectrum")
    print("OK: %s classified sites by Vs30" % ''' + _json.dumps(name) + ''')
if __name__ == "__main__":
    main()
'''


@_reg("eq_model")
def d_model(name, rid, group):
    return driver.demo_hdr(name, rid, group) + '''\
def main():
    # 3D-printable moment-frame teaching model: printable directions + disclosed estimate
    # 2-story single-bay frame, ~35 cm^3 of members
    vol_cm3 = 35.0
    speed_mm3_s = 12.0
    t_min = vol_cm3 * 1000.0 / speed_mm3_s / 60.0 * 1.25
    print("frame model volume %.0f cm^3 -> ESTIMATED print time %.0f min" % (vol_cm3, t_min))
    print("DISCLOSED ESTIMATE ONLY: real time varies with printer and settings.")
    assert 55.0 < t_min < 70.0, t_min
    print("directions: PLA, 0.2 mm layers, 30% infill, print upright; shake-table demo model only")
    print("OK: %s specified a printable frame model with disclosed estimate" % ''' + _json.dumps(name) + ''')
if __name__ == "__main__":
    main()
'''


def main():
    return driver.run_pair(HERE, cfg_pub, cfg_sig, ENTRIES, DEMOS)


if __name__ == "__main__":
    sys.exit(0 if main() else 1)
