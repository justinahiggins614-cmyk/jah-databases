#!/usr/bin/env python3
"""Build the Fire Science and Fire Protection pair (gap-audit part 2).

Verified 2026-10-17: NO database covers fire science/fire protection
(combustion, detection, suppression, compartmentation, evacuation). Manifest
keyword search (fire science, fire protection): zero hits. ZERO full-record
coverage.

Two NEW databases, 34 ladder-ordered records each:
  fire-science-fire-protection            (public-harvest)
  fire-science-fire-protection-signature  (signature)

Never any website references. No Facebook.
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, "/home/hatch/workspace/jah-databases/code/gapaudit-p2")
import driver
from entries_fire import ENTRIES

RK = "fire protection record"
CIT_PUB = ("Fire science and protection (standard references: NFPA 13 (sprinklers), NFPA 72 "
           "(fire alarms), NFPA 101 (Life Safety Code); SFPE Handbook of Fire Protection "
           "Engineering 5th ed.; Drysdale 'An Introduction to Fire Dynamics' 3rd ed. 2011; "
           "Karlsson & Quintiere 'Enclosure Fire Dynamics' 1999).")
CIT_SIG = CIT_PUB + " Signature editions are his original Signature treatment of fire science."
STANDARDS = ["Fire practice per NFPA / SFPE Handbook as cited",
             "Teaching-ladder order: foundations, compounded, advanced"]

cfg_pub, cfg_sig = driver.pair_cfgs(
    slug_base="fire-science-fire-protection", name_base="Fire Science and Fire Protection",
    tagline=("Combustion, detection, suppression, compartmentation, and evacuation: how fires "
             "behave and how buildings defeat them - from the fire tetrahedron and heat "
             "release rate through detectors, sprinklers, and compartmentation to smoke "
             "modeling, special suppression, and performance-based design, taught "
             "progressively along the ladder."),
    record_kind=RK, prefix_pub="JAH-FSP-", prefix_sig="JAH-FSPS-",
    ai_base="JAH Fire Archivist",
    role_pub=("fire protection archivist - combustion, detection, suppression, "
              "compartmentation, evacuation; teaching progressively along the ladder from "
              "foundations through compounded to advanced; answers from many angles - "
              "definition, example, procedure, math, standards - using only the system's "
              "own archive data"),
    role_sig=("fire protection archivist - Signature editions: his original Signature "
              "treatment of fire science, clearly labeled Signature-made and never "
              "presented as authentic public record; teaches progressively along the ladder; "
              "answers from many angles using only the system's own archive data"),
    search_ph="Search HRR, flashover, sprinklers, detectors, egress, compartmentation...",
    chat_ph="Ask about fire protection...",
    archive_topic="fire-protection records",
    gen_kind="fire-protection",
    standards=STANDARDS, cit_pub=CIT_PUB, cit_sig=CIT_SIG,
    hero_pub=("Public records - real, fact-checked fire science: what fire science is, the "
              "fire tetrahedron, heat release rate, t-squared growth, smoke, combustion "
              "products, ignition, fire spread, flashover, time-temperature curves, human "
              "behavior, fire statistics, smoke and heat detectors, alarm systems, "
              "sprinklers, K-factors, system types, standpipes, extinguishers, "
              "compartmentation, fire-rated assemblies, egress, smoke management, zone "
              "models and FDS, flashover prediction, detector siting, hydraulic "
              "calculations, special suppression, warehouse fires, performance-based design, "
              "fire investigation, printable training models, and the engineer's role - "
              "organized in the Signature system. Every record carries the full entry: "
              "description, how it works, key points, requirements, standards, citations, "
              "and a working demonstration program. Records are ordered by the teaching "
              "ladder: Foundations -> Compounded -> Advanced."),
    hero_sig=("Signature originals - his original Signature treatment of fire science and "
              "fire protection: the full ladder from combustion through detection and "
              "suppression to performance-based design, reframed as Signature science. "
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


@_reg("fs_hrr")
def d_hrr(name, rid, group):
    return driver.demo_hdr(name, rid, group) + '''\
def main():
    # t-squared fire growth: Q = alpha * t^2 ; medium growth alpha = 0.0117 kW/s^2
    alpha = 0.0117  # kW/s^2 (medium)
    for t in (60, 120, 300):
        Q = alpha * t ** 2
        print("  t=%3d s: HRR = %6.0f kW" % (t, Q))
    assert abs(alpha * 120 ** 2 - 168.5) < 0.5
    # time to 1 MW
    import math
    t_1mw = math.sqrt(1000.0 / alpha)
    print("medium fire reaches 1 MW at ~%d s" % t_1mw)
    assert 285 < t_1mw < 300, t_1mw
    print("OK: %s modeled t-squared fire growth" % ''' + _json.dumps(name) + ''')
if __name__ == "__main__":
    main()
'''


@_reg("fs_sprinkler")
def d_sprinkler(name, rid, group):
    return driver.demo_hdr(name, rid, group) + '''\
import math
def main():
    # sprinkler discharge: Q = K * sqrt(P)
    K = 80.0    # L/min/bar^0.5 (standard spray sprinkler)
    P = 1.0     # bar
    Q = K * math.sqrt(P)
    print("K=%d at %.1f bar -> %.0f L/min per sprinkler" % (K, P, Q))
    assert abs(Q - 80.0) < 1e-9
    # 12 sprinklers operating
    print("12 heads flowing: %.0f L/min total demand" % (12 * Q))
    assert abs(12 * Q - 960.0) < 1e-9
    print("OK: %s computed sprinkler discharge from K-factor" % ''' + _json.dumps(name) + ''')
if __name__ == "__main__":
    main()
'''


@_reg("fs_egress")
def d_egress(name, rid, group):
    return driver.demo_hdr(name, rid, group) + '''\
def main():
    # egress time: occupants / (door capacity) ; RSET vs ASET
    occupants = 300
    doors = 3
    cap_per_door = 1.33  # persons/second per unit width (approx)
    width_m = 1.0
    flow = doors * width_m * cap_per_door * 60.0  # persons/minute
    t_move = occupants / flow
    t_pre = 1.5   # pre-movement, min
    RSET = t_pre + t_move
    ASET = 8.0    # available safe egress time, min
    print("occupants %d, flow %.0f/min -> movement %.1f min, RSET %.1f min vs ASET %.0f min" % (
        occupants, flow, t_move, RSET, ASET))
    assert abs(t_move - 1.253) < 0.01, t_move
    assert RSET < ASET, "RSET must be less than ASET"
    print("OK: %s checked RSET against ASET for egress" % ''' + _json.dumps(name) + ''')
if __name__ == "__main__":
    main()
'''


@_reg("fs_smoke")
def d_smoke(name, rid, group):
    return driver.demo_hdr(name, rid, group) + '''\
def main():
    # smoke filling (simplified zone model): layer descent in a compartment
    # dz/dt from plume entrainment; use simple filling estimate
    A = 100.0     # m^2 floor area
    H = 4.0       # m ceiling height
    Q_kw = 500.0  # kW fire
    # plume volume flow (Heskestad approx, m^3/s)
    import math
    z = 2.0       # m plume height
    m_dot = 0.071 * Q_kw ** (1.0 / 3.0) * z ** (5.0 / 3.0)
    print("500 kW fire: plume entrains ~%.2f m^3/s at %.0f m" % (m_dot, z))
    assert 0.5 < m_dot < 2.0, m_dot
    # time to fill upper 2 m of 100 m^2 room
    t_fill = (A * 2.0) / m_dot
    print("upper 2 m layer fills in ~%.0f s without venting" % t_fill)
    print("OK: %s estimated smoke filling with a plume correlation" % ''' + _json.dumps(name) + ''')
if __name__ == "__main__":
    main()
'''


@_reg("fs_detector")
def d_detector(name, rid, group):
    return driver.demo_hdr(name, rid, group) + '''\
import math
def main():
    # detector spacing: NFPA 72 smooth-ceiling spacing 9.1 m (30 ft) for smoke
    spacing = 9.1  # m
    area = 800.0   # m^2
    n = math.ceil(area / (spacing ** 2))
    print("area %.0f m^2 at %.1f m spacing -> %d smoke detectors" % (area, spacing, n))
    assert n == 10, n
    print("reduce spacing for beams, high ceilings, high airflow")
    print("OK: %s laid out detector coverage" % ''' + _json.dumps(name) + ''')
if __name__ == "__main__":
    main()
'''


@_reg("fs_compartment")
def d_compartment(name, rid, group):
    return driver.demo_hdr(name, rid, group) + '''\
def main():
    # MQH flashover correlation (simplified): dT = 6.85 * (Q^2 / (Av*sqrt(Hv)*hk*AT))^(1/3)
    Q = 1500.0     # kW
    Av = 2.0       # m^2 vent area
    Hv = 2.0       # m vent height
    hk = 0.02      # kW/m^2/K effective heat transfer
    AT = 120.0     # m^2 total internal surface
    dT = 6.85 * (Q ** 2 / (Av * Hv ** 0.5 * hk * AT)) ** (1.0 / 3.0)
    print("upper layer rise dT = %.0f C for %.0f kW fire" % (dT, Q))
    print("flashover likely when upper layer ~500-600 C")
    assert 400.0 < dT < 700.0, dT
    print("OK: %s estimated flashover with the MQH correlation" % ''' + _json.dumps(name) + ''')
if __name__ == "__main__":
    main()
'''


@_reg("fs_extinguish")
def d_extinguish(name, rid, group):
    return driver.demo_hdr(name, rid, group) + '''\
def main():
    # extinguisher coverage: light hazard, one 2-A extinguisher per 280 m^2 (NFPA 10 approx)
    area = 1400.0  # m^2
    per = 280.0
    import math
    n = math.ceil(area / per)
    travel_max = 23.0  # m max travel distance (light hazard)
    print("area %.0f m^2 -> %d extinguishers (max travel %.0f m)" % (area, n, travel_max))
    assert n == 5
    print("classes: A (ordinary), B (flammable liquid), C (electrical), K (kitchen)")
    print("OK: %s sized extinguisher coverage per NFPA 10" % ''' + _json.dumps(name) + ''')
if __name__ == "__main__":
    main()
'''


@_reg("fs_alarm")
def d_alarm(name, rid, group):
    return driver.demo_hdr(name, rid, group) + '''\
def main():
    # alarm audibility: 15 dB above ambient (NFPA 72), sound drops 6 dB per doubling
    ambient = 55.0  # dBA office
    required = ambient + 15.0
    # sounder rated 85 dBA at 3 m; level at 12 m:
    import math
    level_12m = 85.0 - 20.0 * math.log10(12.0 / 3.0)
    print("ambient %d dBA -> required %d dBA; sounder gives %.1f dBA at 12 m" % (
        ambient, required, level_12m))
    assert abs(level_12m - 72.96) < 0.05, level_12m
    assert level_12m >= required
    print("OK: %s verified alarm audibility with distance attenuation" % ''' + _json.dumps(name) + ''')
if __name__ == "__main__":
    main()
'''


@_reg("fs_hydrant")
def d_hydrant(name, rid, group):
    return driver.demo_hdr(name, rid, group) + '''\
def main():
    # hydrant flow test: available flow at residual pressure (Hazen-Williams on main)
    # simplified: static 6 bar, residual 4.5 bar at 60 L/s test flow
    static, residual, q_test = 6.0, 4.5, 60.0  # bar, bar, L/s
    # project to 1.4 bar residual (20 psi) using Q2 = Q1 * ((Ps-Pr1)/(Ps-Pr2))^0.54
    Q_avail = q_test * ((static - 1.4) / (static - residual)) ** 0.54
    print("static %.1f bar, residual %.1f at %d L/s -> available %.0f L/s at 1.4 bar" % (
        static, residual, q_test, Q_avail))
    assert 90.0 < Q_avail < 130.0, Q_avail
    print("OK: %s projected hydrant flow to residual pressure" % ''' + _json.dumps(name) + ''')
if __name__ == "__main__":
    main()
'''


@_reg("fs_model")
def d_model(name, rid, group):
    return driver.demo_hdr(name, rid, group) + '''\
def main():
    # 3D-printable fire training model: compartment cutaway for training
    # dollhouse-style room 150 mm cube section, ~30 cm^3
    vol_cm3 = 30.0
    speed_mm3_s = 12.0
    t_min = vol_cm3 * 1000.0 / speed_mm3_s / 60.0 * 1.25
    print("training compartment volume %.0f cm^3 -> ESTIMATED print time %.0f min" % (vol_cm3, t_min))
    print("DISCLOSED ESTIMATE ONLY: real time varies with printer and settings.")
    assert 45.0 < t_min < 60.0, t_min
    print("directions: PLA, 0.2 mm layers, 20% infill; TRAINING MODEL ONLY - never near real fire")
    print("OK: %s specified a printable training model with disclosed estimate" % ''' + _json.dumps(name) + ''')
if __name__ == "__main__":
    main()
'''


def main():
    return driver.run_pair(HERE, cfg_pub, cfg_sig, ENTRIES, DEMOS)


if __name__ == "__main__":
    sys.exit(0 if main() else 1)
