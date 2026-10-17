#!/usr/bin/env python3
"""Build the Microrobotics field databases for JAH Databases (field #28, taxonomy order).

Verified 2026-10-17 (see entries_microrobotics.py docstring): NO database
covers microrobotics as a specialty discipline. Manifest search (2356
databases): no 'microrobot' database. Nearest neighbors: 'robots' (37,000
macro-robot records), 'robotics-autonomous-physical-systems' (32 macro
records), 'microsystems-engineers' (people records), 'Microfabrication
Labs/Facilities' (cleanroom facility records). Whole-system title sweep
over all 758 shard indexes + full-text sweep over all 1,129,379 records
('microrobot', 'micro-robot', 'nanorobot', 'microbot', 'microgripper',
'microactuator', 'microassembly', 'microswimmer', 'micro-locomotion',
'comb drive', 'thermal microactuator', 'piezoelectric microactuator',
'electrostatic microactuator', 'microfluidic robot', 'microfabrication',
'scaling law'): ZERO full-record discipline coverage anywhere (only
incidental mentions: cleanroom facility records, management 'scaling laws
for teams', passing mentions in hypersonics/petrophysics).

So this build creates two NEW databases, 32 ladder-ordered records each,
covering ONLY what the system left uncovered:

  microrobotics             - The Microrobotics Database (public-harvest:
                             real, fact-checked micro/nano-scale robotics;
                             citations Madou 2011, Maluf & Williams 2004,
                             Senturia 2001, Kovacs 1998, Gad-el-Hak 2006,
                             Sitti 2017, Nelson/Kaliakatsos/Abbott 2010,
                             Purcell 1977, Feynman 1959, Judy 2001,
                             Diller & Sitti 2013, Howell 2001, Pister 1992,
                             Ma et al. 2013, Whitesides & Grzybowski 2002,
                             Rubenstein et al. 2014, Kummer et al. 2010)
  microrobotics-signature  - The Microrobotics Signature Database (his
                             original Signature interpretation; src
                             signature, titles suffixed
                             " (Signature Edition)", never presented as
                             authentic public record)

32 records each, ordered by the teaching ladder (ladder_rank 1-10,
ladder_tier foundations/compounded/advanced); the shard index is written in
ladder order so pages present simple -> compounded -> complex.

Every record: description + how-it-works + key points + requirements +
standards + citations + working demonstration code (real, runnable,
stdlib-only Python; machine-executed OK). Microrobotics demos: silicon-cube
scaling; Reynolds numbers across rungs; capillary length and Brownian
wander; MEMS cantilever stiffness/frequency/sag; wafer die yield, DRIE
time, lithography resolution; Al-on-Si thermal stress; comb-drive force and
pull-in voltage; piezo bimorph deflection; chevron amplification; magnetic
torque/force vs weight; capacitive accelerometer signal chain; battery vs
capacitor endurance; inductive resonance; walker speed and Stokes drag;
microchannel flow and Re; adhesion vs grip; assembly throughput; vision
frame jumps; swarm coverage and messaging scaling; flexure stress;
Janus swimmer range; bacterial thrust vs drag; optical trap force and
intensity; drug-dose arithmetic; tremor filtering and motion scaling;
RoboBee lift; pipeline inspection coverage; self-assembly yield binomial;
stiction vs restore and Weibull failures; diffraction limit; endurance
crossover; learning-curve economics.

Subtitle disambiguation (fields #13-27 pattern): specialty titles carry
teaching-focused subtitles rather than bare cards, e.g. "Scaling Laws at
Small Sizes: Why Surface Beats Volume".

Never the words "bat belt" anywhere. No website references. No Facebook.
"""
import importlib.util
import json
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = "/home/hatch/workspace/jah-databases"
SHARD = "/home/hatch/workspace/jah-databases-data-1"
SHARD_BASE = "https://justinahiggins614-cmyk.github.io/jah-databases-data-1"
TEMPLATE = os.path.join(REPO, "db", "public-synthetic-intelligence", "index.html")

sys.path.insert(0, os.path.join(REPO, "code", "phone-compound-build"))
import build as base
# Whole-system dedupe gate against the FRESH data/dedupe/exact/ index in the
# main repo (per task). Fields past the gate index were cross-checked
# directly (see docstring) - subtitle disambiguation used throughout.
sys.path.insert(0, os.path.join(REPO, "code"))
from dedupe_gate import DedupeGate
base.GATE = DedupeGate(os.path.join(REPO, "data", "dedupe", "exact"))

sys.path.insert(0, HERE)
from entries_microrobotics import ENTRIES, SIG_TAIL

# ---------------------------------------------------------------- DB config

def _cfg(slug, name, tagline, record_kind, prefix, ai, role, citation, source):
    sig_line = ("Signature originals - his original Signature interpretation of microrobotics "
                "engineering: clearly labeled Signature-made, never presented as authentic "
                "public record.")
    pub_line = ("Public records - real, fact-checked micro/nano-scale robotics: what "
                "microrobotics is; the micro-scale map and Reynolds regimes; scaling laws; "
                "MEMS bodies; microfabrication; micro-scale materials; electrostatic, "
                "piezoelectric, thermal, and magnetic actuation; micro-sensors; powering "
                "and the energy problem; wireless power and communication; micro-locomotion "
                "and low-Reynolds swimming; microfluidic integration; micro-grippers; "
                "micro-assembly; micro-scale control; swarm microrobots; compliant "
                "mechanisms; chemical propulsion; biohybrid robots; optical control; "
                "medical microrobots; microsurgery tools; insect-scale flight; inspection "
                "microrobots; self-assembly and micro-origami; reliability, stiction, and "
                "packaging; testing and characterization; energy scaling limits; economics "
                "and roadmap, organized in the Signature system.")
    ladder = (" Records are ordered by the teaching ladder: Foundations (what microrobotics "
              "is, the scale map, scaling laws, MEMS bodies, microfabrication, materials) -> "
              "Compounded (electrostatic, piezoelectric, thermal, magnetic actuation; "
              "micro-sensors; powering; wireless power; locomotion; microfluidics; grippers; "
              "micro-assembly; control; swarms) -> Advanced (compliant mechanisms; chemical "
              "propulsion; biohybrids; optical control; medical microrobots; microsurgery; "
              "insect flight; inspection; self-assembly; reliability; testing; energy "
              "limits; economics and roadmap).")
    return {
        "name": name, "tagline": tagline, "record_kind": record_kind,
        "prefix": prefix, "ai": ai, "role": role,
        "hero_p": "%s - %s Every record carries the full entry: description, how it works, "
                  "key points, requirements, standards, citations, and a working demonstration "
                  "program.%s" % (tagline, sig_line if source == "signature" else pub_line, ladder),
        "sig_type": ("Signature originals organized in the Signature system"
                     if source == "signature" else
                     "Public records organized in the Signature system"),
        "search_ph": "Search comb drive, MEMS, piezoelectric, scaling laws, microrobot, swarm, drug delivery...",
        "chat_ph": "Ask about microrobotics...",
        "archive_blurb": ("Seeded %s microrobotics records, marching toward one million records. "
                          "Presented in teaching-ladder order: foundations, compounded, advanced."
                          % ("Signature-original" if source == "signature" else "public-record")),
        "schema": ("id, t, g, name, title, description, how_it_works, key_points, requirements, "
                   "standards, citations, src, ladder_rank, ladder_tier, demo"),
        "fields": "Foundations \u00b7 Compounded \u00b7 Advanced - each tier opens on demand and loads only what you open",
        "gen_desc": "Generate clearly-labeled microrobotics studies. Seeded archive records are the authoritative entries.",
        "greet": "I am the %s. Ask me about microrobotics - from scaling laws, MEMS, and microfabrication through electrostatic, piezoelectric, thermal, and magnetic actuation, micro-sensors, powering, locomotion, control, swarms, medical microrobots, microsurgery, insect-scale flight, self-assembly, reliability, and the economics roadmap." % ai,
        "gen_fields": ["Foundations", "Compounded", "Advanced"],
        "gen_kind": "microrobotics-study", "gen_demo_kind": "microrobotics-demo",
        "source": source,
    }

CIT_PUB = ("Microrobotics (standard texts: Madou 'Fundamentals of Microfabrication and "
           "Nanotechnology' 3rd ed. 2011; Maluf & Williams 'An Introduction to "
           "Microelectromechanical Systems Engineering' 2nd ed. 2004; Senturia "
           "'Microsystem Design' 2001; Kovacs 'Micromachined Transducers Sourcebook' 1998; "
           "Gad-el-Hak (ed.) 'The MEMS Handbook' 2nd ed. 2006; Sitti 'Mobile Microrobotics' "
           "2017; Nelson, Kaliakatsos & Abbott 2010; Purcell 'Life at Low Reynolds Number' "
           "1977; Feynman 'There's Plenty of Room at the Bottom' 1959; Judy 2001; "
           "Diller & Sitti 2013; Howell 'Compliant Mechanisms' 2001; Pister et al. 1992; "
           "Ma et al. 2013; Whitesides & Grzybowski 2002; Rubenstein et al. 2014; "
           "Kummer et al. 2010).")
CIT_SIG = CIT_PUB + " " + SIG_TAIL

DBCFG = {}
DBCFG["microrobotics"] = _cfg(
    "microrobotics", "The Microrobotics Database",
    "Real, fact-checked micro/nano-scale robotics: from the scale map, scaling laws, MEMS "
    "bodies, and microfabrication through electrostatic, piezoelectric, thermal, and magnetic "
    "actuation, micro-sensors, powering, wireless power, locomotion, microfluidics, grippers, "
    "micro-assembly, control, and swarms to compliant mechanisms, chemical and biohybrid "
    "propulsion, optical control, medical microrobots, microsurgery, insect-scale flight, "
    "inspection, self-assembly, reliability, testing, energy limits, and the economics "
    "roadmap - taught progressively along the ladder.",
    "microrobotics record", "JAH-MRO-", "JAH Microrobotics Archivist",
    "microrobotics archivist - scaling laws, MEMS, microfabrication, micro-actuation "
    "(electrostatic, piezoelectric, thermal, magnetic), micro-sensors, powering, wireless "
    "power, micro-locomotion, microfluidics, micro-grippers, micro-assembly, control, "
    "swarms, compliant mechanisms, chemical propulsion, biohybrids, optical control, "
    "medical microrobots, microsurgery, insect-scale flight, inspection, self-assembly, "
    "reliability, testing, energy limits, economics; teaching progressively along the ladder "
    "from foundations through compounded to advanced; answers from many angles - definition, "
    "example, analogy, application, history, math, how-to - using only the system's own "
    "archive data",
    CIT_PUB, "public")
DBCFG["microrobotics-signature"] = _cfg(
    "microrobotics-signature", "The Microrobotics Signature Database",
    "His original Signature interpretation of microrobotics: the full ladder from what "
    "microrobotics is through scaling laws, MEMS, actuation, sensing, power, locomotion, "
    "control, swarms, medical microrobots, self-assembly, reliability, and the economics "
    "roadmap, reframed as Signature science. Clearly labeled Signature-made, never presented "
    "as authentic public record.",
    "microrobotics record", "JAH-MRS-", "JAH Microrobotics Archivist (Signature)",
    "microrobotics archivist - Signature editions: his original Signature "
    "interpretation of microrobotics, clearly labeled Signature-made and "
    "never presented as authentic public record; teaches progressively along the "
    "ladder from foundations through compounded to advanced; answers from many "
    "angles - definition, example, analogy, application, history, math, how-to - "
    "using only the system's own archive data",
    CIT_SIG, "signature")

base.DBCFG = DBCFG

# ---------------------------------------------------------------- demos
# Every demo is real, runnable, stdlib-only Python performing the actual
# microrobotics computation for its record. All are machine-executed by main().

_PREAMBLE = (
"import math\n"
)

def _wrap(name, rid, group, body):
    return (base._hdr(name, rid, group) + _PREAMBLE + body.replace("NAME", json.dumps(name)))

def demo_mr_what(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # the first microrobotics calculation: what does small weigh, and what rules it
    rho_si = 2330.0            # kg/m3, silicon
    L = 1e-3                  # m: 1 mm cube
    V = L ** 3
    m = rho_si * V
    W = m * 9.81
    s_v = 6.0 / L             # surface-to-volume ratio, 1/m
    s_v_big = 6.0 / 1.0       # the same cube at 1 m
    print("1 mm silicon cube: mass = %.2f mg, weight = %.1f uN" % (m * 1e6, W * 1e6))
    print("surface/volume = %.0f /m  (vs %.0f /m for a 1 m cube: %dx)" % (s_v, s_v_big, s_v / s_v_big))
    assert abs(m - 2.33e-6) < 1e-8, m
    assert abs(W - 2.286e-5) < 1e-7, W
    assert abs(s_v - 6000.0) < 1e-9
    print("gravity pulls with ~23 micronewtons; surface forces pull far harder")
    print("rule: at the micro-scale, design for surfaces first and weight last")
    print("OK: %s weighed the small" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_mr_scale(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # Reynolds number: which rung of the ladder, which physics
    rho, mu = 1000.0, 1e-3    # water
    def Re(v, L):
        return rho * v * L / mu
    cases = [
        ("1 mm robot at 1 mm/s", 1e-3, 1e-3),
        ("10 um swimmer at 10 um/s", 1e-5, 1e-5),
        ("human swimmer, 2 m at 1 m/s", 1.0, 2.0),
    ]
    for label, v, L in cases:
        print("%-30s Re = %.4g" % (label, Re(v, L)))
    assert abs(Re(1e-3, 1e-3) - 1.0) < 1e-9
    assert abs(Re(1e-5, 1e-5) - 1e-4) < 1e-12
    assert abs(Re(1.0, 2.0) - 2e6) < 1.0
    print("ten orders of magnitude separate the micro-swimmer from the human")
    print("rule: read the Reynolds number before choosing how to move")
    print("OK: %s mapped the rungs" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_mr_scaling(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # crossovers: where surface tension beats gravity, where diffusion beats swimming
    gamma, rho, g = 0.072, 1000.0, 9.81
    lam = math.sqrt(gamma / (rho * g))      # capillary length, m
    kT = 1.380649e-23 * 298.0
    mu, a = 1e-3, 1e-6                      # water, 1 um particle radius
    D = kT / (6.0 * math.pi * mu * a)       # Stokes-Einstein, m2/s
    rms_1s = math.sqrt(2.0 * D * 1.0)       # Brownian wander in 1 s, m
    print("capillary length of water = %.2f mm" % (lam * 1e3))
    print("below ~mm: surface tension beats gravity")
    print("1 um particle: D = %.3g m2/s, wanders %.2f um in 1 s" % (D, rms_1s * 1e6))
    assert abs(lam - 2.709e-3) < 1e-5, lam
    assert abs(rms_1s - 6.608e-7) < 1e-8, rms_1s
    print("the wander is comparable to the particle itself: budget for randomness")
    print("rule: find the crossover length first - it tells you which physics is boss")
    print("OK: %s found the crossovers" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_mr_mems(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # the MEMS workhorse: silicon cantilever stiffness, ring frequency, self-sag
    E, rho = 169e9, 2330.0
    L, w, t = 500e-6, 50e-6, 2e-6
    I = w * t ** 3 / 12.0
    k = 3.0 * E * I / L ** 3
    m = rho * L * w * t
    f0 = (1.0 / (2.0 * math.pi)) * math.sqrt(k / m)
    sag = m * 9.81 / k
    print("cantilever 500x50x2 um: k = %.3f N/m" % k)
    print("mass = %.3g kg; f0 = %.0f Hz; sags %.1f nm under its own weight" % (m, f0, sag * 1e9))
    assert abs(k - 0.1352) < 0.002, k
    assert abs(f0 - 5422.0) < 20.0, f0
    assert abs(sag - 8.45e-9) < 2e-10, sag
    print("soft as thread, fast as a whistle, light as nothing: the MEMS signature")
    print("rule: stiffness goes as 1/L^3 - halve the length, stiffen eightfold")
    print("OK: %s bent the beam" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_mr_fab(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # batch economics: dies per wafer, etch time, lithography resolution
    wafer_d, die = 150.0, 5.0 * 5.0          # mm, mm2
    dies = int(math.pi * (wafer_d / 2.0) ** 2 / die)
    drie_rate = 10.0                          # um/min
    etch_min = 500.0 / drie_rate              # through a 500 um wafer
    lam, NA = 365e-9, 0.5
    res = 0.61 * lam / NA                     # Rayleigh, m
    print("150 mm wafer, 5x5 mm dice -> ~%d robots per wafer" % dies)
    print("DRIE at 10 um/min: 500 um through-etch = %.0f min" % etch_min)
    print("365 nm lithography at NA 0.5 resolves %.2f um" % (res * 1e6))
    assert dies == 706, dies
    assert abs(etch_min - 50.0) < 1e-9
    assert abs(res - 4.453e-7) < 1e-9, res
    print("a thousand robots per etch run: batch is the business model")
    print("rule: count the dice before counting the cost")
    print("OK: %s ran the fab" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_mr_mat(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # the price of stacking films: thermal-expansion mismatch stress
    E_al = 70e9
    d_alpha = (23.0 - 2.6) * 1e-6            # Al vs Si, /K
    dT = 100.0
    sigma = E_al * d_alpha * dT
    si_specific = 7e9 / 2330.0                # strength/density, N m/kg
    steel_specific = 400e6 / 7800.0
    print("Al film on Si, heated 100 K: thermal stress = %.0f MPa" % (sigma / 1e6))
    print("silicon specific strength vs steel: %.1fx" % (si_specific / steel_specific))
    assert abs(sigma - 1.428e8) < 1e6, sigma
    print("enough to curl a beam like a potato chip: manage the mismatch")
    print("rule: every film interface is a potential failure - choose stresses you can live with")
    print("OK: %s stressed the stack" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_mr_elec(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # comb-drive muscle and the pull-in cliff
    eps0 = 8.854e-12
    N, h, g, V = 100, 10e-6, 2e-6, 50.0
    F = N * eps0 * h * V ** 2 / g
    A, g0, k = 1e-6, 5e-6, 10.0
    Vpi = math.sqrt(8.0 * k * g0 ** 3 / (27.0 * eps0 * A))
    print("comb drive (100 fingers, 50 V): F = %.2f uN" % (F * 1e6))
    print("parallel plate (1 mm2, 5 um gap, 10 N/m): pull-in at %.2f V" % Vpi)
    assert abs(F - 1.10675e-5) < 1e-8, F
    assert abs(Vpi - 6.468) < 0.01, Vpi
    print("past one-third of the gap the plates cannot resist each other: stay below, or use the snap")
    print("rule: voltage is cheap, gaps are precious - shrink the gap, not the ambition")
    print("OK: %s charged the combs" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_mr_piezo(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # bimorph: a whisper of crystal strain amplified into a shout of motion
    d31 = 180e-12                            # m/V, PZT magnitude
    L, t = 2e-3, 0.2e-3
    per_volt = 1.5 * d31 * (L / t) ** 2      # m/V
    V = 50.0
    delta = per_volt * V
    print("PZT bimorph 2 mm x 0.2 mm: %.1f nm/V" % (per_volt * 1e9))
    print("at 50 V the tip moves %.2f um" % (delta * 1e6))
    assert abs(per_volt - 2.7e-8) < 1e-10, per_volt
    assert abs(delta - 1.35e-6) < 1e-8, delta
    print("long and thin wins: deflection grows as (L/t)^2")
    print("rule: never bend the crystal brutishly - leverage it")
    print("OK: %s flexed the crystal" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_mr_thermal(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # chevron: heat expands, geometry amplifies
    alpha, L, dT = 2.6e-6, 500e-6, 300.0
    dL = alpha * L * dT
    theta = math.radians(5.0)
    amp = 1.0 / math.tan(theta)
    apex = dL * amp
    P = 5.0 ** 2 / 200.0                     # V^2/R heater power
    print("thermal expansion: %.2f um -> chevron apex: %.2f um (x%.1f)" % (dL * 1e6, apex * 1e6, amp))
    print("heater power: %.3f W; force class: millinewtons" % P)
    assert abs(dL - 3.9e-7) < 1e-9, dL
    assert abs(apex - 4.458e-6) < 5e-8, apex
    assert abs(P - 0.125) < 1e-9
    print("strong, simple, slow, hot: the strongman bargain")
    print("rule: pulse it like a heartbeat and keep it away from anything that fears warmth")
    print("OK: %s fired the chevron" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_mr_mag(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # telekinesis math: torque and pull on a micro-magnet
    V = (100e-6) ** 3
    m = 1e6 * V                              # magnetic moment, A m2
    B, gradB = 0.01, 1.0
    torque = m * B
    force = m * gradB
    weight = 7500.0 * V * 9.81               # NdFeB-ish density
    print("100 um magnet: torque in 10 mT = %.1g N m" % torque)
    print("pull in 1 T/m gradient = %.1f uN = %.1fx its own weight" % (force * 1e6, force / weight))
    assert abs(torque - 1e-8) < 1e-11, torque
    assert abs(force - 1e-6) < 1e-9, force
    assert abs(force / weight - 13.59) < 0.05
    print("the field lifts fourteen magnets' worth: wireless muscle")
    print("rule: uniform field aims it, gradient moves it, rotating field swims it")
    print("OK: %s aimed the field" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_mr_sens(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # capacitive accelerometer: nanometres in, femtofarads out
    eps0 = 8.854e-12
    A, g = 1e-6, 2e-6
    C0 = eps0 * A / g
    m, k = 1e-9, 1.0
    x_1g = m * 9.81 / k
    dC = C0 * x_1g / g
    f0 = (1.0 / (2.0 * math.pi)) * math.sqrt(k / m)
    print("C0 = %.2f pF; 1 g moves the mass %.1f nm -> dC = %.1f fF" % (C0 * 1e12, x_1g * 1e9, dC * 1e15))
    print("resonance f0 = %.0f Hz (far above the motion it measures)" % f0)
    assert abs(C0 - 4.427e-12) < 1e-14, C0
    assert abs(dC - 2.171e-14) < 1e-16, dC
    assert abs(f0 - 5033.0) < 5.0, f0
    print("Brownian battering sets the floor: quiet the room (vacuum) to hear the whisper")
    print("rule: every sensor is a chain - physical to mechanical to electrical - and every link adds noise")
    print("OK: %s felt the nanometres" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_mr_power(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # the cruelest budget: joules you can carry vs watts you must spend
    Vb = 1e-9                                  # 1 mm3 battery, m3
    E_bat = 3000.0 * Vb * 100.0 * 3600.0  # 3 mg at 100 Wh/kg -> J
    draw = 1e-3
    t_bat = E_bat / draw
    E_cap = 0.5 * 1e-3 * 3.0 ** 2              # 1 mF at 3 V
    t_cap = E_cap / draw
    print("1 mm3 battery: %.2f J -> 1 mW robot runs %.0f s (%.0f min)" % (E_bat, t_bat, t_bat / 60.0))
    print("1 mF capacitor at 3 V: %.1f mJ -> %.1f s at 1 mW" % (E_cap * 1e3, t_cap))
    assert abs(E_bat - 1.08) < 0.02, E_bat
    assert abs(t_bat - 1080.0) < 2.0
    assert abs(E_cap - 4.5e-3) < 1e-9
    print("capacitors are sprint reservoirs, not fuel tanks")
    print("rule: sleep at nanowatts, burst at milliwatts - the average is what the battery feels")
    print("OK: %s balanced the budget" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_mr_wireless(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # resonance is the whole trick: tune the guest to the room's note
    f = 13.56e6
    L = 1e-6
    C = 1.0 / ((2.0 * math.pi * f) ** 2 * L)
    lam = 3e8 / f
    f_check = 1.0 / (2.0 * math.pi * math.sqrt(L * C))
    print("1 uH coil resonates at 13.56 MHz with %.1f pF" % (C * 1e12))
    print("wavelength = %.1f m: every microrobot is deeply near-field" % lam)
    assert abs(C - 1.3775e-10) < 1e-12, C
    assert abs(lam - 22.12) < 0.05, lam
    assert abs(f_check - f) / f < 1e-9
    print("far-field radio is the wrong tool; near-field induction is the right one")
    print("rule: high Q rescues weak coupling - wind for Q, trim for resonance")
    print("OK: %s tuned the link" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_mr_loco(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # legs for the big small, corkscrews for the small small
    stride, freq = 100e-6, 100.0
    v = stride * freq
    bl_s = v / 1e-3
    mu, a = 1e-3, 0.5e-3
    F_drag = 6.0 * math.pi * mu * a * 1e-3    # 1 mm sphere at 1 mm/s
    print("1 mm walker: 100 um strides at 100 Hz -> %.0f mm/s = %.0f body lengths/s" % (v * 1e3, bl_s))
    print("Stokes drag on 1 mm sphere at 1 mm/s: %.2f nN" % (F_drag * 1e9))
    assert abs(v - 0.01) < 1e-12
    assert abs(F_drag - 9.4248e-9) < 1e-11, F_drag
    print("the scallop opens and closes and goes nowhere: swim non-reciprocally or walk")
    print("rule: below Re~1 there is no coasting - stop pushing, stop instantly")
    print("OK: %s learned to move" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_mr_fluid(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # the robot's aquarium: laminar channel flow
    w, h, Lc = 100e-6, 50e-6, 0.01
    mu, dP = 1e-3, 1000.0
    R = 12.0 * mu * Lc / (w * h ** 3)
    Q = dP / R
    v = Q / (w * h)
    Dh = 2.0 * w * h / (w + h)
    Re = 1000.0 * v * Dh / mu
    print("100x50 um channel, 1 cm, 1 kPa: Q = %.3f uL/s, v = %.1f mm/s, Re = %.2f" % (Q * 1e9, v * 1e3, Re))
    assert abs(Q - 1.0417e-10) < 1e-13, Q
    assert abs(Re - 1.389) < 0.01, Re
    print("Re 1.4: streams layer without mixing - gradients stay put")
    print("rule: halve the height, multiply resistance sixteenfold - respect h^3")
    print("OK: %s plumbed the chip" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_mr_grip(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # the inverted problem: grasping is easy, releasing is hard
    A_H, R, Dd = 1e-19, 5e-6, 0.4e-9
    F_vdw = A_H * R / (6.0 * Dd ** 2)
    F_cap = 2.0 * math.pi * R * 0.072
    grip = 10e-6
    print("10 um sphere: van der Waals %.2f uN, capillary %.2f uN vs %d uN grip" % (
        F_vdw * 1e6, F_cap * 1e6, int(grip * 1e6)))
    assert abs(F_vdw - 5.208e-7) < 1e-9, F_vdw
    assert abs(F_cap - 2.2619e-6) < 1e-8, F_cap
    print("let go and the part stays glued to the jaw: design the release, not just the grasp")
    print("rule: peel, puff, jerk, or submerge - never just open the jaws and hope")
    print("OK: %s learned to let go" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_mr_assem(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # serial patience vs parallel dreams
    t_part = 10.0
    rate = 3600.0 / t_part
    t_1000 = 1000.0 / rate
    tol = 1e-6 / 10e-3
    print("pick-place at 10 s/part: %.0f parts/hour; 1000 parts = %.1f hours" % (rate, t_1000))
    print("+-1 um over 10 mm travel demands %.0e relative precision per axis" % tol)
    assert abs(rate - 360.0) < 1e-9
    assert abs(t_1000 - 2.7778) < 0.01, t_1000
    assert abs(tol - 1e-4) < 1e-12
    print("a footstep is an earthquake here: isolate, cool, humidify, automate")
    print("rule: parallelism wins - arrays, wafer transfer, self-assembly")
    print("OK: %s built by hand" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_mr_ctrl(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # piloting in fog: what the camera sees between frames
    fps, v = 30.0, 1e-3
    jump = v / fps
    latency, overshoot = 1e-3, 1e-3 * 1e-3
    diffr = 0.61 * 550e-9 / 0.9
    print("30 fps camera, 1 mm/s robot: jumps %.1f um between frames" % (jump * 1e6))
    print("1 ms latency at 1 mm/s = %.1f um overshoot; diffraction limit %.2f um" % (overshoot * 1e6, diffr * 1e6))
    assert abs(jump - 33.333e-6) < 1e-7, jump
    assert abs(diffr - 3.728e-7) < 1e-9, diffr
    print("33x the precision target per frame: slow near the target, model the rest")
    print("rule: when sensing falls short, redesign the task - funnels, traps, docks")
    print("OK: %s steered the fog" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_mr_swarm(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # many tiny, one big: coverage, messaging, and free fault tolerance
    coverage = int(1.0 / 0.01 ** 2)            # 1 m2 on a 10 mm grid
    n = 1000
    local_msgs = n * 6
    all_to_all = n * (n - 1)
    survivors = int(10000 * 0.9)
    print("1 m2 inspection needs %d robots on a 10 mm grid" % coverage)
    print("1000 robots: local messages %d vs all-to-all %d" % (local_msgs, all_to_all))
    print("lose 10%% of 10,000: %d still working - fault tolerance is free" % survivors)
    assert coverage == 10000
    assert local_msgs == 6000 and all_to_all == 999000
    print("talk to neighbours, signal through the world, never address individuals")
    print("rule: program the rule and the environment - the behaviour emerges")
    print("OK: %s raised the swarm" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_mr_compl(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # the hinge that was never assembled: silicon flexure
    E = 169e9
    L, w, t = 200e-6, 20e-6, 5e-6
    I = w * t ** 3 / 12.0
    k = 3.0 * E * I / L ** 3
    d = 10e-6
    F = k * d
    sigma = 6.0 * F * L / (w * t ** 2)
    margin = 7e9 / sigma
    print("Si flexure 200x20x5 um: k = %.1f N/m; 10 um -> %.0f uN at %.0f MPa" % (k, F * 1e6, sigma / 1e6))
    print("margin to silicon's 7 GPa limit: %.0fx - flex it a million times" % margin)
    assert abs(k - 13.203) < 0.05, k
    assert abs(sigma - 3.169e8) < 1e7, sigma
    print("no pins, no wear, no lube: the motion was always in the material")
    print("rule: fillet every corner - a sharp corner is a crack waiting to happen")
    print("OK: %s bent without breaking" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_mr_chem(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # drink the sea: Janus swimmer speed and voyage length
    v = 10e-6                                   # m/s in peroxide
    size = 2e-6
    bl_s = v / size
    t_run = 600.0
    voyage = v * t_run
    print("2 um Janus particle: %.0f um/s = %.0f body lengths/s" % (v * 1e6, bl_s))
    print("10-minute run covers %.1f mm" % (voyage * 1e3))
    assert abs(voyage - 6e-3) < 1e-9
    print("asymmetry is the engine: catalyst on one side only")
    print("rule: it swims until chemistry says stop - give it a voyage worth completing")
    print("OK: %s drank the fuel" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_mr_bio(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # hire the cell: bacterial thrust vs Stokes drag, balanced exactly
    thrust = 10 * 0.5e-12                       # 10 E. coli, N
    mu, a = 1e-3, 5e-6                          # water, 10 um cargo radius
    v = thrust / (6.0 * math.pi * mu * a)
    print("10 bacteria x 0.5 pN = %.1f pN thrust -> cargo speed %.0f um/s" % (thrust * 1e12, v * 1e6))
    assert abs(v - 5.305e-5) < 1e-7, v
    print("the cells self-fuel, self-repair, and steer themselves up gradients")
    print("rule: keep the living half fed and unthreatened - diplomacy between kingdoms")
    print("OK: %s hired the crew" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_mr_opt(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # a finger of focused starlight
    k_trap = 10e-12 / 1e-6                      # 10 pN/um -> N/m
    F = k_trap * 1e-6
    P, r = 0.1, 0.5e-6
    I = P / (math.pi * r ** 2)
    print("optical trap: 1 um displacement -> %.0f pN restoring force" % (F * 1e12))
    print("100 mW in a 1 um spot: intensity %.2g W/m2" % I)
    assert abs(F - 1e-11) < 1e-14, F
    assert abs(I - 1.2732e11) < 1e9, I
    print("gentle enough for a cell, precise enough for a chromosome")
    print("rule: light needs line of sight - deep tissue needs a fibre, not a wish")
    print("OK: %s trapped the light" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_mr_med(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # targeted delivery arithmetic: flood vs courier
    n, cargo = 1e9, 1e-12                        # robots, litres each
    total = n * cargo
    local = total * 0.01                         # 1% reach the target
    print("%.0e robots x 1 pL = %.1f mL total dose" % (n, total * 1e3))
    print("1%% targeting -> %.0f uL delivered exactly where needed" % (local * 1e6))
    assert abs(total - 1e-3) < 1e-12
    assert abs(local - 1e-5) < 1e-14
    print("microlitres at the disease vs millilitres through healthy tissue")
    print("rule: first do no harm - then dissolve without a trace")
    print("OK: %s dosed the target" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_mr_surg(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # steadier than human: tremor filtered, motion divided
    tremor, scale = 100e-6, 100.0
    tool_motion = tremor / scale
    vessel, tool = 100e-6, 30e-6
    print("hand tremor %.0f um / %dx motion scaling -> tool moves %.1f um" % (tremor * 1e6, scale, tool_motion * 1e6))
    print("100 um vessel: %.0f um tool leaves %.0f um of wall clearance" % (tool * 1e6, (vessel - tool) * 1e6))
    assert abs(tool_motion - 1e-6) < 1e-12
    print("virtual fixtures: software walls the tool cannot cross")
    print("rule: remove the noise, never the judgment - the surgeon still decides")
    print("OK: %s steadied the hand" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_mr_fly(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # the final exam: 80 milligrams that refuses to fall
    m = 80e-6
    W = m * 9.81
    f = 120.0
    print("RoboBee-class: mass %.0f mg, weight %.0f uN of lift required" % (m * 1e6, W * 1e6))
    print("wingbeat %.0f Hz on piezo muscles; frequency scales ~1/size" % f)
    assert abs(W - 7.848e-4) < 1e-6, W
    print("resonant wings beat almost for free; power is still tethered")
    print("rule: free flight awaits better power density, not better aerodynamics")
    print("OK: %s earned its wings" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_mr_insp(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # coverage arithmetic: the watchman's schedule
    L, v = 1000.0, 0.01
    t1 = L / v / 3600.0
    t10 = t1 / 10.0
    print("1 km of 10 cm pipe at 10 mm/s: one crawler %.1f h, ten crawlers %.1f h" % (t1, t10))
    assert abs(t1 - 27.778) < 0.05, t1
    assert abs(t10 - 2.778) < 0.05, t10
    print("no disassembly, no shutdown, no scaffolding: the business case")
    print("rule: no radio inside steel - record everything, dump it at the dock")
    print("OK: %s walked the pipe" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_mr_self(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # origami yield: the binomial judges every hinge
    hinges = 50
    y_good, y_need = 0.99, 0.999
    y1 = y_good ** hinges
    y2 = y_need ** hinges
    print("50 hinges at 99%% each: %.1f%% fold correctly" % (y1 * 100.0))
    print("at 99.9%% each: %.1f%% - the production threshold" % (y2 * 100.0))
    assert abs(y1 - 0.6050) < 0.002, y1
    assert abs(y2 - 0.9512) < 0.002, y2
    print("minimize hinge count, self-correct every fold, test statistically")
    print("rule: one trigger turns a wafer of flat patterns into a wafer of robots")
    print("OK: %s folded itself" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_mr_rel(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # the invisible enemies: a meniscus and a statistic
    F_stick = 2.0 * 0.072 * 4.0 * 100e-6      # water meniscus under 100 um plate
    F_restore = 10e-6
    beta, eta, t = 2.0, 1e7, 1e6
    F_fail = 1.0 - math.exp(-((t / eta) ** beta))
    print("stiction: %.1f uN meniscus vs %.0f uN restore -> %s" % (
        F_stick * 1e6, F_restore * 1e6, "STUCK" if F_stick > F_restore else "free"))
    print("Weibull(beta=2, eta=1e7): %.2f%% fail by 1e6 cycles" % (F_fail * 100.0))
    assert abs(F_stick - 5.76e-5) < 1e-9, F_stick
    assert abs(F_fail - 0.00995) < 2e-4, F_fail
    print("coat everything, seal everything, fillet everything")
    print("rule: reliability is designed in, not inspected in")
    print("OK: %s survived the small" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_mr_test(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # knowing the invisible: the diffraction wall
    diffr = 0.61 * 550e-9 / 0.9
    print("optical microscope limit (550 nm, NA 0.9): %.2f um" % (diffr * 1e6))
    print("below it: SEM (vacuum), interferometry (~1 nm heights), laser vibrometry (no touch)")
    assert abs(diffr - 3.728e-7) < 1e-9, diffr
    print("measure what the equation predicts - disagreement indicts model or process")
    print("rule: report uncertainty honestly; every instrument has limits")
    print("OK: %s measured the invisible" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_mr_energy(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # the theorem: below ~1 mm3, the tank loses and the feed wins
    E_mm3, P = 1.08, 1e-3
    t_big = E_mm3 / P
    t_small = (E_mm3 * 1e-3) / P                # 100 um cube: 1e-3 the volume
    print("1 mm3 battery at 1 mW: %.0f s (%.0f min)" % (t_big, t_big / 60.0))
    print("100 um robot's share at 1 mW: %.2f s - a firework, not a machine" % t_small)
    print("wireless 1 mW continuous inside the workspace: infinite endurance")
    assert abs(t_big - 1080.0) < 2.0
    assert abs(t_small - 1.08) < 0.05, t_small
    print("millibots carry fuel and roam; microrobots take power as a utility")
    print("rule: design the system around the feed, not the tank")
    print("OK: %s proved the theorem" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_mr_econ(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # from bench to industry: the learning curve and the mask set
    c0, v0, v1, lr = 100.0, 1e4, 1e7, 0.8
    doublings = math.log2(v1 / v0)
    c1 = c0 * (lr ** doublings)
    mask = 50000.0
    print("$100 at 10k units -> $%.2f at 10M units (80%% learning curve)" % c1)
    print("$50k mask set: $%.2f/unit at 1k units, $%.2f at 1M" % (mask / 1e3, mask / 1e6))
    assert abs(c1 - 10.82) < 0.05, c1
    assert abs(mask / 1e3 - 50.0) < 1e-9 and abs(mask / 1e6 - 0.05) < 1e-9
    print("gates: untethered power, microscope-free control, reliability at scale")
    print("rule: never promise the ten-thousandth robot before the first hundred earn their keep")
    print("OK: %s priced the future" % NAME)
if __name__ == "__main__":
    main()
''')

DEMOS = {
    "what_is_microrobotics": demo_mr_what, "scale_map": demo_mr_scale,
    "scaling_laws": demo_mr_scaling, "mems_body": demo_mr_mems,
    "microfabrication": demo_mr_fab, "micro_materials": demo_mr_mat,
    "electrostatic_actuation": demo_mr_elec, "piezoelectric_actuation": demo_mr_piezo,
    "thermal_actuation": demo_mr_thermal, "magnetic_actuation": demo_mr_mag,
    "micro_sensors": demo_mr_sens, "micro_power": demo_mr_power,
    "wireless_power": demo_mr_wireless, "micro_locomotion": demo_mr_loco,
    "microfluidics": demo_mr_fluid, "micro_grippers": demo_mr_grip,
    "micro_assembly": demo_mr_assem, "micro_control": demo_mr_ctrl,
    "swarm_micro": demo_mr_swarm, "compliant_mech": demo_mr_compl,
    "chemical_propulsion": demo_mr_chem, "biohybrid": demo_mr_bio,
    "optical_control": demo_mr_opt, "medical_microbots": demo_mr_med,
    "microsurgery": demo_mr_surg, "micro_flight": demo_mr_fly,
    "inspection_env": demo_mr_insp, "self_assembly": demo_mr_self,
    "reliability": demo_mr_rel, "testing": demo_mr_test,
    "energy_limits": demo_mr_energy, "economics_roadmap": demo_mr_econ,
}
assert set(DEMOS) == {e["key"] for e in ENTRIES}, "demo map misses entries"


def build_records(slug, source):
    cfg = DBCFG[slug]
    sig = source == "signature"
    # Teaching-ladder order: stable sort by ladder_rank (entries are already
    # in ladder order in entries_microrobotics.py).
    ordered = sorted(enumerate(ENTRIES), key=lambda p: (p[1]["ladder_rank"], p[0]))
    recs = []
    for _, e in ordered:
        name = e["name"]
        title = name + " (Signature Edition)" if sig else name
        # Whole-system dedupe gate (his standing rule: every record, never a sample).
        if [h for h in base.GATE.check(slug, title) if h[0] != slug]:
            print("  gate refused (cross-db dupe): %s" % title, flush=True)
            continue
        rid = "%s%06d" % (cfg["prefix"], len(recs) + 1)
        if sig:
            description = ("Signature original interpretation. " + e["sig_lens"] + " "
                           + e["description"])
            how = e["sig_lens"] + " " + e["how_it_works"]
            citations = list(e["citations"]) + [SIG_TAIL]
        else:
            description = e["description"]
            how = e["how_it_works"]
            citations = list(e["citations"])
        rec = {
            "id": rid, "t": title, "g": e["group"], "name": name, "title": title,
            "description": description,
            "how_it_works": how,
            "key_points": list(e["key_points"]),
            "requirements": list(e["requirements"]),
            "standards": list(e["standards"]),
            "citations": citations,
            "src": "signature" if sig else "public-harvest",
            "ladder_rank": e["ladder_rank"],
            "ladder_tier": e["ladder_tier"],
        }
        demo_fn = DEMOS[e["key"]]
        program = demo_fn(name if not sig else title, rid, e["group"],
                          e["key_points"], "; ".join(e["requirements"]))
        rec["demo"] = {"kind": "python", "language": "python",
                       "program": program,
                       "note": "Working demonstration program (real, runnable Python)."}
        base.GATE.admit(slug, title, rid)
        recs.append(rec)
    # Ladder order guarantee: ids were assigned in ladder order; re-verify.
    ranks = [r["ladder_rank"] for r in recs]
    assert ranks == sorted(ranks), "records not in ladder order for %s" % slug
    return recs


def main():
    sys.path.insert(0, os.path.join(REPO, "code", "numbering-build"))
    spec = importlib.util.spec_from_file_location(
        "nb_build", os.path.join(REPO, "code", "numbering-build", "build.py"))
    nb = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(nb)
    nb.DBCFG = DBCFG

    sweep_path = "/home/hatch/workspace/goals/database-quality-audit/hidden_files/patches/sweep-db-pages.py"
    sspec = importlib.util.spec_from_file_location("sweep", sweep_path)
    sweep = importlib.util.module_from_spec(sspec)
    sspec.loader.exec_module(sweep)

    built = {}
    for slug in ("microrobotics", "microrobotics-signature"):
        source = "signature" if slug.endswith("-signature") else "public"
        built[slug] = build_records(slug, source)

    # sanity: ids unique + prefix + required keys + ALL demo programs compile
    # + banned-content scan + ladder fields present
    total = 0
    for slug, recs in built.items():
        cfg = DBCFG[slug]
        ids = [r["id"] for r in recs]
        assert len(ids) == len(set(ids)), "dup ids in %s" % slug
        assert all(i.startswith(cfg["prefix"]) for i in ids), "prefix drift in %s" % slug
        assert len(recs) >= 30, "fewer than 30 records in %s" % slug
        for r in recs:
            for k in ("id", "t", "g", "name", "title", "description", "how_it_works",
                      "key_points", "requirements", "standards", "citations",
                      "src", "ladder_rank", "ladder_tier", "demo"):
                assert k in r, "missing %s in %s" % (k, r["id"])
            prog = r["demo"].get("program")
            assert prog and len(r["description"]) > 200, "stub in %s" % r["id"]
            assert 1 <= r["ladder_rank"] <= 10, "ladder_rank out of range in %s" % r["id"]
            assert r["ladder_tier"] in ("foundations", "compounded", "advanced"), \
                "bad ladder_tier in %s" % r["id"]
            compile(prog, r["id"], "exec")
            blob = json.dumps(r).lower()
            assert "facebook" not in blob, "facebook ref in %s" % r["id"]
            assert "bat belt" not in blob, "banned phrase in %s" % r["id"]
            if slug.endswith("-signature"):
                assert "(signature edition)" in r["title"].lower(), "sig title missing suffix"
                assert r["src"] == "signature"
            else:
                assert r["src"] == "public-harvest"
        total += len(recs)
        n = base.write_shard_db(slug, recs)
        print("shard: %-38s %d records" % (slug, n), flush=True)

    # machine-execute EVERY demo (canon: runnable demo, machine-executed OK)
    for slug, recs in built.items():
        for r in recs:
            prog = r["demo"]["program"]
            p = subprocess.run([sys.executable, "-c", prog],
                               capture_output=True, text=True, timeout=180)
            assert p.returncode == 0, "demo failed %s: %s" % (r["id"], p.stderr[-800:])
            assert "OK:" in p.stdout, "demo no OK marker %s" % r["id"]
    print("demo execution: all %d demos ran OK" % total, flush=True)

    with open(TEMPLATE, "r", encoding="utf-8") as f:
        template = f.read()
    for slug, recs in built.items():
        page = nb.build_page(slug, template)
        page = page.replace(
            "Generate structural synthetic intelligence studies. Seeded archive records are the authoritative entries.",
            DBCFG[slug]["gen_desc"])
        assert 'id="stCount"' in page and "var SLUG='%s';" % slug in page
        assert "minmax(120px,1fr)" in page and "pre.codeblock" in page
        assert "pill-ex" in page and "qmerge" in page, "Exhaustive pill / merger button missing"
        assert "dataset.p" in page, "tab-handler guard missing"
        assert "facebook" not in page.lower()
        assert "synthetic intelligence" not in page.lower(), "template leftover in %s" % slug
        assert "bat belt" not in page.lower(), "banned phrase in page %s" % slug
        ddir = os.path.join(REPO, "db", slug)
        os.makedirs(ddir, exist_ok=True)
        ppath = os.path.join(ddir, "index.html")
        with open(ppath, "w", encoding="utf-8") as f:
            f.write(page)
        changed, notes = sweep.process_page(ppath)
        topics = {}
        for r in recs:
            topics.setdefault(r["g"], []).append("%s - %s" % (r["t"], r["g"]))
        gen_js = nb.build_gen_js(slug, topics, DBCFG[slug])
        assert "facebook" not in gen_js.lower() and "bat belt" not in gen_js.lower()
        with open(os.path.join(ddir, "gen-%s.js" % slug), "w", encoding="utf-8") as f:
            f.write(gen_js)
        print("page:  db/%s/index.html + gen-%s.js [%s]" % (slug, slug, ", ".join(notes)), flush=True)

    entries_m = [base.manifest_entry(s, len(built[s])) for s in built]
    base.update_json_list(os.path.join(REPO, "data", "manifest.json"), entries_m)
    entries_a = [base.api_entry(s, len(built[s])) for s in built]
    base.update_json_list(os.path.join(REPO, "api.json"), entries_a)
    print("manifest + api.json: appended %d databases, %d records" % (len(built), total))
    print("NEXT: run python3 code/restamp_counts.py, then commit + push.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
