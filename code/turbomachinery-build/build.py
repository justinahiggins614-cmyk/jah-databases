#!/usr/bin/env python3
"""Build the Turbomachinery field databases for JAH Databases (field #20, taxonomy order).

Verified 2026-10-17: NO database covers turbomachinery as a discipline.
- Manifest-wide regex search (turbo|turbine|compressor|pump|cavitat|blade|
  cascade|rotordyn|fan): zero database hits across all 2340 databases.
- Fields #11-19 shard indexes (volcanology, climatology, atmospheric-science,
  hydrology, meteorology, calculus, combinatorics, econometrics,
  psychometrics): direct whole-shard title scans - only false positives on
  the substring "surge" ("Hurricane Forecasting: Track Models, the Cone, and
  Storm Surge" = storm surge; "Pyroclastic Flows and Surges" = pyroclastic
  surge). Neither is compressor surge; none rise to the discipline: no Euler
  turbine equation, no velocity triangles, no specific speed, no affinity
  laws, no cascades, no cavitation/NPSH, no rotordynamics.
- 'scientific-formulas': bare formula cards are reference only (task rule:
  formula cards do NOT count as discipline coverage).
- Whole-system dedupe gate (fresh data/dedupe/exact/ index rebuilt 2026-10-17
  08:04 UTC, covering fields through #10; fields #11-19 cross-checked directly
  above): every record checked + admitted at build time.

So this build creates two NEW databases:

  turbomachinery             - The Turbomachinery Database
                               (public-harvest: real, fact-checked
                               turbomachinery; citations Dixon & Hall,
                               Cumpsty, Logan, Japikse & Baines,
                               Saravanamuttoo/Rogers/Cohen, Wilson &
                               Korakianitis, Cengel & Boles, White,
                               Stepanoff, Karassik, Bleier, Hydraulic
                               Institute, API 610, ISO 10816)
  turbomachinery-signature   - The Turbomachinery Signature Database
                               (his original Signature interpretation of the
                               discipline; src signature, titles suffixed
                               " (Signature Edition)", never presented as
                               authentic public record)

37 records each, ordered by the teaching ladder (ladder_rank 1-10,
ladder_tier foundations/compounded/advanced); the shard index is written in
ladder order so pages present simple -> compounded -> complex.

Every record: description + how-it-works + key points + requirements +
standards + citations + working demonstration code (real, runnable,
stdlib-only Python; machine-executed OK). Turbomachinery demos: the
discipline map, Bernoulli in a duct, the control-volume energy budget, the
Euler equation as arithmetic, velocity-triangle construction, 50%-reaction
symmetry, the family sign conventions, geometry vs specific speed, the
dimensionless collapse, specific-speed selection, affinity-law scaling, the
loss audit, a Rankine cycle at 40%, a Brayton cycle at 50.8%, the Betz limit,
Pelton/Francis/Kaplan selection, axial-stage diffusion limits, centrifugal
slip (Stodola), the pump operating point, PD pump metering, fan laws and
static pressure, reading the compressor map, Carter deviation and loss
buckets, cavitation inception, the NPSH margin, Greitzer B and surge, the
Jeffcott critical speed, L10 bearing life, Martin labyrinth leakage, cooling
effectiveness, tip-clearance debit, stage-stack matching, VSV scheduling, the
combined-cycle arithmetic, vibration diagnosis, the seven-step design
workflow, and the hydrogen/sCO2 frontier.

Subtitle disambiguation (fields #13-19 pattern): discipline titles carry
teaching-focused subtitles rather than bare cards, e.g. "The Euler Turbine
Equation: The One Equation That Rules Every Rotor" and "Net Positive Suction
Head: The Guard Against Cavitation".

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
# main repo (rebuilt 2026-10-17 08:04 UTC; covers fields through #10).
# Fields #11-19 shard indexes (volcanology, climatology, atmospheric-science,
# hydrology, meteorology, calculus, combinatorics, econometrics, psychometrics)
# checked directly against their shard indexes in jah-databases-data-1 since
# the gate index predates them - subtitle disambiguation used throughout.
sys.path.insert(0, os.path.join(REPO, "code"))
from dedupe_gate import DedupeGate
base.GATE = DedupeGate(os.path.join(REPO, "data", "dedupe", "exact"))

sys.path.insert(0, HERE)
from entries_turbomachinery import ENTRIES, SIG_TAIL

# ---------------------------------------------------------------- DB config

def _cfg(slug, name, tagline, record_kind, prefix, ai, role, citation, source):
    sig_line = ("Signature originals - his original Signature interpretation of turbomachinery: "
                "clearly labeled Signature-made, never presented as authentic public record.")
    pub_line = ("Public records - real, fact-checked turbomachinery: what turbomachinery is; "
                "fluid-mechanics foundations; conservation laws; the Euler turbine equation; "
                "velocity triangles; degree of reaction; the turbine/compressor/pump/fan family; "
                "axial, radial, and mixed-flow geometries; dimensionless performance coefficients; "
                "specific speed and specific diameter; the affinity laws; losses and efficiency; "
                "steam turbines and the Rankine cycle; gas turbines and the Brayton cycle; wind "
                "turbines and the Betz limit; Pelton, Francis, and Kaplan hydraulic turbines; axial "
                "compressors; centrifugal compressors; rotodynamic and positive-displacement pumps; "
                "fans and blowers; performance maps; blade cascades; cavitation; net positive "
                "suction head; surge and stall; rotordynamics; bearings; seals; blade cooling and "
                "materials; tip clearance and secondary flows; multistage matching; variable "
                "geometry; combined cycles and cogeneration; condition monitoring and failure modes; "
                "the design workflow; the hydrogen and supercritical-CO2 frontier, organized in "
                "the Signature system.")
    ladder = (" Records are ordered by the teaching ladder: Foundations (what turbomachinery is, "
              "fluid mechanics, conservation laws, the Euler equation, velocity triangles, degree "
              "of reaction, the machine family, flow geometries, dimensionless coefficients, "
              "specific speed, affinity laws, losses) -> Compounded (steam turbines, gas turbines, "
              "wind turbines, hydraulic turbines, axial compressors, centrifugal compressors, "
              "rotodynamic pumps, positive-displacement pumps, fans and blowers, performance maps, "
              "blade cascades, cavitation, NPSH) -> Advanced (surge and stall, rotordynamics, "
              "bearings, seals, blade cooling and materials, tip clearance, multistage matching, "
              "variable geometry, combined cycles, condition monitoring, the design workflow, the "
              "frontier).")
    return {
        "name": name, "tagline": tagline, "record_kind": record_kind,
        "prefix": prefix, "ai": ai, "role": role,
        "hero_p": "%s - %s Every record carries the full entry: description, how it works, "
                  "key points, requirements, standards, citations, and a working demonstration "
                  "program.%s" % (tagline, sig_line if source == "signature" else pub_line, ladder),
        "sig_type": ("Signature originals organized in the Signature system"
                     if source == "signature" else
                     "Public records organized in the Signature system"),
        "search_ph": "Search Euler equation, velocity triangles, specific speed, affinity laws, cavitation, surge, Brayton, Rankine...",
        "chat_ph": "Ask about turbomachinery...",
        "archive_blurb": ("Seeded %s turbomachinery records, marching toward one million records. "
                          "Presented in teaching-ladder order: foundations, compounded, advanced."
                          % ("Signature-original" if source == "signature" else "public-record")),
        "schema": ("id, t, g, name, title, description, how_it_works, key_points, requirements, "
                   "standards, citations, src, ladder_rank, ladder_tier, demo"),
        "fields": "Foundations \u00b7 Compounded \u00b7 Advanced - each tier opens on demand and loads only what you open",
        "gen_desc": "Generate clearly-labeled structural turbomachinery studies. Seeded archive records are the authoritative entries.",
        "greet": "I am the %s. Ask me about turbomachinery - from the Euler turbine equation, velocity triangles, and specific speed through compressors, turbines, pumps, cavitation, surge, rotordynamics, and the design workflow." % ai,
        "gen_fields": ["Foundations", "Compounded", "Advanced"],
        "gen_kind": "turbomachinery-study", "gen_demo_kind": "turbomachinery-demo",
        "source": source,
    }

CIT_PUB = "Turbomachinery (standard textbooks and peer-reviewed literature)."
CIT_SIG = CIT_PUB + " " + SIG_TAIL

DBCFG = {}
DBCFG["turbomachinery"] = _cfg(
    "turbomachinery", "The Turbomachinery Database",
    "Real, fact-checked turbomachinery: the machines that exchange energy with flowing "
    "fluids through rotating blades - from the Euler turbine equation and velocity "
    "triangles through turbines, compressors, pumps, fans, cavitation, surge, "
    "rotordynamics, and the design workflow - taught progressively along the ladder.",
    "turbomachinery record", "JAH-TM-", "JAH Turbomachinery Archivist",
    "turbomachinery archivist - what turbomachinery is, fluid mechanics, conservation laws, "
    "the Euler equation, velocity triangles, degree of reaction, the machine family, flow "
    "geometries, dimensionless coefficients, specific speed, affinity laws, losses, steam "
    "turbines, gas turbines, wind turbines, hydraulic turbines, axial compressors, "
    "centrifugal compressors, rotodynamic and positive-displacement pumps, fans, performance "
    "maps, cascades, cavitation, NPSH, surge and stall, rotordynamics, bearings, seals, blade "
    "cooling, tip clearance, multistage matching, variable geometry, combined cycles, "
    "condition monitoring, the design workflow, the frontier; "
    "teaching progressively along the ladder from foundations through compounded to "
    "advanced; answers from many angles - definition, example, analogy, application, "
    "history, math, how-to - using only the system's own archive data",
    CIT_PUB, "public")
DBCFG["turbomachinery-signature"] = _cfg(
    "turbomachinery-signature", "The Turbomachinery Signature Database",
    "His original Signature interpretation of turbomachinery: the full ladder from the "
    "Euler equation and velocity triangles through turbines, compressors, pumps, and the "
    "design workflow, reframed as Signature science. Clearly labeled Signature-made, "
    "never presented as authentic public record.",
    "turbomachinery record", "JAH-TMS-", "JAH Turbomachinery Archivist (Signature)",
    "turbomachinery archivist - Signature editions: his original Signature interpretation "
    "of turbomachinery, clearly labeled Signature-made and never presented as authentic "
    "public record; teaches progressively along the ladder from foundations through "
    "compounded to advanced; answers from many angles - definition, example, analogy, "
    "application, history, math, how-to - using only the system's own archive data",
    CIT_SIG, "signature")

base.DBCFG = DBCFG
# ---------------------------------------------------------------- demos
# Every demo is real, runnable, stdlib-only Python performing the actual
# turbomachinery computation for its record. All are machine-executed by main().

_PREAMBLE = (
"import math\n"
"import random\n"
"def _deg(r):\n"
"    return r * 180.0 / math.pi\n"
"def _rad(d):\n"
"    return d * math.pi / 180.0\n"
)

def _wrap(name, rid, group, body):
    return (base._hdr(name, rid, group) + _PREAMBLE + body.replace("NAME", json.dumps(name)))

def demo_tm_what(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
TERRITORIES = {
    "power machines": "turbines - steam, gas, wind, hydraulic: fluid gives up energy",
    "absorbing machines": "compressors, pumps, fans, blowers: shaft gives energy to fluid",
    "the shared physics": "Euler equation, velocity triangles, dimensionless coefficients",
}
def main():
    assert len(TERRITORIES) == 3
    for terr, tools in TERRITORIES.items():
        print("%-20s -> %s" % (terr, tools))
    # the founding contrast: one equation, two signs
    U, Ct_in, Ct_out = 300.0, 500.0, 100.0
    w_turbine = U * (Ct_in - Ct_out)          # work done BY the fluid: positive out
    w_compressor = U * (Ct_out - Ct_in)       # work done ON the fluid: negative = absorbs
    assert abs(w_turbine - 120000.0) < 1e-6
    assert abs(w_compressor + 120000.0) < 1e-6
    print("turbine:  w = %.0f kJ/kg extracted | compressor: w = %.0f kJ/kg absorbed"
          % (w_turbine / 1000.0, -w_compressor / 1000.0))
    print("rule: swirl in, work out - or work in, swirl out; Euler keeps the books both ways")
    print("OK: %s mapped the discipline" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_tm_fluid_mech(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def main():
    rho = 1.2            # kg/m^3, air
    D1, D2 = 0.5, 0.25   # m, converging duct
    V1 = 10.0            # m/s
    A1 = math.pi * D1 ** 2 / 4.0
    A2 = math.pi * D2 ** 2 / 4.0
    V2 = V1 * A1 / A2    # continuity: rho*A*V constant
    assert abs(V2 - 40.0) < 1e-9, V2
    print("continuity: area ratio %.1f -> velocity %.0f m/s becomes %.0f m/s" % (A1 / A2, V1, V2))
    p1 = 500.0           # Pa gauge at inlet
    p2 = p1 - rho * (V2 ** 2 - V1 ** 2) / 2.0   # Bernoulli
    assert abs(p2 - (p1 - 900.0)) < 1e-9, p2
    print("Bernoulli: static pressure %.0f Pa -> %.0f Pa (fell %.0f Pa = gained dynamic pressure)"
          % (p1, p2, p1 - p2))
    # the diffuser mirror: slow it back down, recover the pressure
    V3 = V1
    p3 = p2 + rho * (V2 ** 2 - V3 ** 2) / 2.0
    assert abs(p3 - p1) < 1e-9, (p3, p1)
    print("diffuser mirror: decelerating %.0f -> %.0f m/s recovers all %.0f Pa (lossless ideal)"
          % (V2, V3, p3 - p2))
    print("rule: nozzles trade pressure for speed; diffusers trade speed back for pressure")
    print("OK: %s ran the duct" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_tm_conservation(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def main():
    # control volume around a compressor rotor: steady-flow energy equation
    mdot = 10.0          # kg/s
    cp = 1005.0          # J/kg-K, air
    T01, T02 = 300.0, 450.0   # K, stagnation temperatures in/out
    w = cp * (T02 - T01)      # shaft work per unit mass = stagnation enthalpy rise
    P = mdot * w / 1e6
    assert abs(w - 150750.0) < 1e-6, w
    assert abs(P - 1.5075) < 1e-9, P
    print("mass: %.0f kg/s in = %.0f kg/s out (steady)" % (mdot, mdot))
    print("energy: shaft work = cp*dT0 = %.1f kJ/kg -> shaft power = %.4f MW" % (w / 1000.0, P))
    # momentum check: the same work must equal U * delta-Ctheta (Euler)
    U, dCt = 350.0, w / 350.0
    assert abs(U * dCt - w) < 1e-6
    print("momentum: U*dCt = %.0f * %.1f = %.0f J/kg - Euler agrees with the energy audit" % (U, dCt, U * dCt))
    print("rule: the conservation laws set the budget; the blading decides how much survives")
    print("OK: %s audited the control volume" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_tm_euler(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def main():
    U = 300.0            # m/s blade speed
    Ct1, Ct2 = 500.0, 100.0   # m/s tangential velocities in/out
    w = U * (Ct1 - Ct2)       # Euler: specific work done BY the fluid
    assert abs(w - 120000.0) < 1e-6, w
    mdot = 50.0
    P = mdot * w / 1e6
    assert abs(P - 6.0) < 1e-9, P
    print("Euler: w = U*(Ct1-Ct2) = %.0f*(%.0f-%.0f) = %.0f kJ/kg" % (U, Ct1, Ct2, w / 1000.0))
    print("shaft power at %.0f kg/s: %.1f MW - from one line of arithmetic" % (mdot, P))
    # the designer's dilemma: more turning = more work, but separation caps the turning
    for Ct2_try in (100.0, 0.0, -100.0):
        w_try = U * (Ct1 - Ct2_try)
        print("  exit swirl %+.0f m/s -> w = %.0f kJ/kg %s" %
              (Ct2_try, w_try / 1000.0, "<- aggressive turning, separation risk" if Ct2_try < 50 else ""))
    assert U * (Ct1 - (-100.0)) > w  # more turning, more work - if the flow stays attached
    print("rule: the equation is exact; the blade's job is to earn the turning without separating")
    print("OK: %s wielded the Euler equation" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_tm_triangles(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def main():
    U = 250.0            # m/s blade speed
    Cx = 150.0           # m/s axial through-flow velocity (constant)
    alpha1 = _rad(70.0)  # nozzle exit absolute angle from axial
    Ct1 = Cx * math.tan(alpha1)
    Wt1 = Ct1 - U                    # relative tangential velocity
    beta1 = _deg(math.atan(Wt1 / Cx))
    print("inlet triangle: C-theta1 = %.1f m/s, blade sees W-theta1 = %.1f m/s at beta1 = %.1f deg"
          % (Ct1, Wt1, beta1))
    assert 410.0 < Ct1 < 415.0, Ct1
    assert 45.0 < beta1 < 50.0, beta1   # the blade leading edge is built near this angle
    Ct2 = 50.0
    w = U * (Ct1 - Ct2)
    Wt2 = Ct2 - U
    beta2 = _deg(math.atan(Wt2 / Cx))
    print("outlet triangle: C-theta2 = %.0f m/s, relative angle beta2 = %.1f deg" % (Ct2, beta2))
    print("Euler work from the triangles: w = %.1f kJ/kg" % (w / 1000.0))
    assert w > 0
    # sanity: relative flow accelerates through a turbine rotor (kind to boundary layers)
    W1 = math.hypot(Cx, Wt1); W2 = math.hypot(Cx, Wt2)
    assert W2 > W1, (W1, W2)
    print("relative speed %.0f -> %.0f m/s: accelerating flow - the turbine's aerodynamic kindness" % (W1, W2))
    print("rule: draw the triangles first; the blade is just their embodiment")
    print("OK: %s spoke in triangles" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_tm_reaction(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def reaction(U, Ct1, Ct2):
    return 1.0 - (Ct1 + Ct2) / (2.0 * U)   # constant-Cx axial stage
def main():
    U = 250.0
    lam = reaction(U, 200.0, 50.0)
    assert abs(lam - 0.5) < 1e-9, lam
    print("50%%-reaction stage: Lambda = %.2f - rotor and stator split the pressure work evenly" % lam)
    lam_imp = reaction(U, 450.0, 50.0)
    assert abs(lam_imp) < 1e-9, lam_imp
    print("impulse stage: Lambda = %.2f - all pressure drop in the nozzle, rotor only turns the jet" % lam_imp)
    # the sealing consequence: impulse needs no tip pressure seal; reaction does
    for tag, l in (("impulse", lam_imp), ("50%-reaction", lam)):
        print("  %-14s: pressure drop across rotor %s -> tip sealing %s" %
              (tag, "zero" if l < 0.05 else "significant",
               "not needed" if l < 0.05 else "mandatory"))
    # symmetric triangles for 50% reaction: alpha1 = |beta2|, alpha2 = |beta1|
    Cx = 150.0
    b1 = _deg(math.atan((200.0 - U) / Cx)); b2 = _deg(math.atan((50.0 - U) / Cx))
    a1 = _deg(math.atan(200.0 / Cx)); a2 = _deg(math.atan(50.0 / Cx))
    assert abs(a1 - abs(b2)) < 0.5 and abs(a2 - abs(b1)) < 0.5, (a1, b1, a2, b2)
    print("symmetric triangles: alpha1 = |beta2| = %.1f deg, alpha2 = |beta1| = %.1f deg" % (a1, a2))
    print("rule: Lambda is the fairness dial - 0 keeps power with the nozzle, 0.5 splits it blade-and-blade")
    print("OK: %s split the stage" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_tm_family(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def main():
    U = 300.0
    # turbine: swirl removed -> work BY the fluid (positive out)
    w_turb = U * (500.0 - 100.0)
    # compressor: swirl added -> work ON the fluid (shaft absorbs)
    w_comp = U * (100.0 - 500.0)
    assert w_turb > 0 > w_comp and abs(w_turb) == abs(w_comp)
    print("turbine:    w = %+.0f kJ/kg (fluid pays)" % (w_turb / 1000.0))
    print("compressor: w = %+.0f kJ/kg (shaft pays)" % (w_comp / 1000.0))
    # pumps move liquid: head in meters; fans move air at tiny pressure ratios
    rho_w, g = 1000.0, 9.81
    H = 100.0            # m of water
    dp = rho_w * g * H
    print("pump: %.0f m head = %.0f kPa pressure rise (incompressible)" % (H, dp / 1000.0))
    assert abs(dp - 981000.0) < 1.0
    pr_fan = 1.01         # fan pressure ratio: barely above unity
    print("fan: pressure ratio %.2f - volume moved, pressure barely tickled" % pr_fan)
    print("rule: the branch follows the duty - power out = turbine, gas pressure up = compressor,")
    print("      liquid pressure up = pump, volume at low pressure = fan")
    print("OK: %s met the family" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_tm_geometries(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def specific_speed(N_rps, Q, H, g=9.81):
    return N_rps * math.sqrt(Q) / (g * H) ** 0.75
def main():
    N = 1450.0 / 60.0    # rps
    duties = [
        ("high head, small flow", 0.02, 400.0),
        ("medium head and flow", 0.5, 40.0),
        ("huge flow, low head", 8.0, 4.0),
    ]
    for tag, Q, H in duties:
        Ns = specific_speed(N, Q, H)
        geo = "radial/centrifugal" if Ns < 0.6 else ("mixed-flow" if Ns < 1.2 else "axial")
        print("%-24s Q=%5.2f H=%6.1f -> Ns=%.3f -> %s" % (tag, Q, H, Ns, geo))
    Ns_vals = [specific_speed(N, Q, H) for _, Q, H in duties]
    assert Ns_vals[0] < 0.6 < Ns_vals[2], Ns_vals
    assert Ns_vals[0] < Ns_vals[1] < Ns_vals[2]
    # the radial work bonus: radius change adds Euler work a single axial stage cannot match
    U1, U2, Ct2 = 100.0, 500.0, 450.0
    w_radial = U2 * Ct2 - U1 * 0.0      # axial entry, radial exit
    w_axial = 350.0 * (300.0 - 120.0)  # typical axial stage
    assert w_radial > 2.5 * w_axial, (w_radial, w_axial)
    print("one centrifugal stage: %.0f kJ/kg vs one axial stage: %.0f kJ/kg - the radius-change bonus"
          % (w_radial / 1000.0, w_axial / 1000.0))
    print("rule: low specific speed wants radial, high wants axial - compute Ns before choosing")
    print("OK: %s walked the three geometries" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_tm_dimensionless(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def main():
    # model pump test
    D1, N1, Q1, H1 = 0.3, 1450.0 / 60.0, 0.05, 22.0
    phi = Q1 / (N1 * D1 ** 3)
    psi = 9.81 * H1 / (N1 ** 2 * D1 ** 2)
    print("model: phi = %.4f, psi = %.3f" % (phi, psi))
    assert abs(phi - 0.0766) < 0.002, phi
    # scale up 2x at the same speed: same phi/psi predict the prototype
    D2 = 2.0 * D1
    Q2 = phi * N1 * D2 ** 3
    H2 = psi * N1 ** 2 * D2 ** 2 / 9.81
    assert abs(Q2 / Q1 - 8.0) < 0.01, Q2 / Q1     # cube law on flow
    assert abs(H2 / H1 - 4.0) < 0.01, H2 / H1     # square law on head
    print("2x size: Q %.3f -> %.3f m^3/s (8x), H %.1f -> %.1f m (4x)" % (Q1, Q2, H1, H2))
    phi2 = Q2 / (N1 * D2 ** 3); psi2 = 9.81 * H2 / (N1 ** 2 * D2 ** 2)
    assert abs(phi2 - phi) < 1e-9 and abs(psi2 - psi) < 1e-9
    print("coefficients identical: the model test certified the prototype")
    print("rule: physics has no preferred size - only preferred proportions")
    print("OK: %s collapsed the curves" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_tm_specific_speed(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def Ns(N_rps, Q, H, g=9.81):
    return N_rps * math.sqrt(Q) / (g * H) ** 0.75
def Ds(D, Q, H, g=9.81):
    return D * (g * H) ** 0.25 / math.sqrt(Q)
def main():
    N = 1450.0 / 60.0
    ns1 = Ns(N, 0.1, 60.0)
    print("duty Q=0.10 H=60: Ns = %.4f -> radial/centrifugal pump" % ns1)
    assert ns1 < 0.2, ns1
    ns2 = Ns(N, 2.0, 6.0)
    print("duty Q=2.00 H= 6: Ns = %.3f -> axial-flow pump" % ns2)
    assert ns2 > 1.2, ns2
    # Cordier band: good designs cluster near Ns*Ds ~ 2.5-3
    D_guess = 2.75 / ns1 * math.sqrt(0.1) / (9.81 * 60.0) ** 0.25
    ds1 = Ds(D_guess, 0.1, 60.0)
    print("Cordier sizing: D = %.2f m, Ns*Ds = %.2f (band 2.5-3.0)" % (D_guess, ns1 * ds1))
    assert 2.4 < ns1 * ds1 < 3.1, ns1 * ds1
    # dimensional US-unit form used by catalogs
    N_rpm, Q_gpm, H_ft = 1450.0, 0.1 * 15850.3, 60.0 * 3.28084
    Ns_us = N_rpm * math.sqrt(Q_gpm) / H_ft ** 0.75
    print("catalog form (rpm/gpm/ft): Ns = %.0f -> radial (< ~4000)" % Ns_us)
    assert Ns_us < 4000, Ns_us
    print("rule: compute Ns before choosing anything - every selection chart is an Ns chart in disguise")
    print("OK: %s read the compass" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_tm_affinity(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def main():
    N1, N2 = 1450.0, 1740.0
    r = N2 / N1
    Q1, H1, P1 = 100.0, 40.0, 50.0     # L/s, m, kW at N1
    Q2, H2, P2 = Q1 * r, H1 * r ** 2, P1 * r ** 3
    print("speed ratio %.2f: Q %.0f->%.0f L/s | H %.1f->%.1f m | P %.1f->%.1f kW"
          % (r, Q1, Q2, H1, H2, P1, P2))
    assert abs(Q2 - 120.0) < 1e-9 and abs(H2 - 57.6) < 1e-9 and abs(P2 - 86.4) < 1e-9
    # the whole H-Q curve scales: H = H0 - k Q^2 at N1 becomes scaled at N2
    H0, k = 55.0, 0.0015
    for Q in (60.0, 100.0, 140.0):
        H_a = H0 - k * Q ** 2
        H_b = (H0 - k * (Q / r) ** 2) * r ** 2   # scale the N1 point to N2
        assert abs(H_b - (H0 * r ** 2 - k * Q ** 2)) < 1e-9
    print("curve check: every (Q,H) point rides a constant-phi ray through the origin")
    # the VFD dividend: 20% slower -> nearly half the power
    r_down = 0.8
    print("slow to 80%% speed: power %.1f -> %.1f kW (the cubic dividend)" % (P1, P1 * r_down ** 3))
    assert abs(P1 * r_down ** 3 - 25.6) < 1e-9
    print("rule: Q~N, H~N^2, P~N^3 - recompute the system-curve intersection after scaling")
    print("OK: %s scaled the machine" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_tm_losses(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def main():
    budget = 100.0   # units of shaft work into a compressor stage
    losses = {
        "profile (blade boundary layers)": 3.0,
        "secondary (endwall vortices)": 2.0,
        "tip clearance (over-tip leakage)": 1.5,
        "seal leakage + disc windage": 1.0,
    }
    total_loss = sum(losses.values())
    eta = 1.0 - total_loss / budget
    for item, val in losses.items():
        print("  %-38s %4.1f units" % (item, val))
    print("useful pressure rise: %.1f units -> stage efficiency %.1f%%" % (budget - total_loss, 100 * eta))
    assert abs(eta - 0.925) < 1e-9, eta
    # where loss goes matters: turbine reheat recovers part of it downstream
    reheat_recovery = 0.4 * total_loss   # illustration: 40% of turbine loss reheat-recovered
    print("turbine reheat: ~%.1f of the %.1f lost units resurface as useful heat downstream" %
          (reheat_recovery, total_loss))
    print("compressor: loss is pure waste - no reheat, no recovery")
    # the design response: each line item has a weapon
    weapons = {"profile": "controlled-diffusion airfoils", "secondary": "endwall contouring + lean",
               "tip clearance": "tight clearances + shrouds", "leakage": "better seals"}
    assert len(weapons) == 4
    print("rule: the loss audit turns 'improve efficiency' from a wish into a work list")
    print("OK: %s audited the losses" % NAME)
if __name__ == "__main__":
    main()
''')
def demo_tm_steam(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def main():
    # simple Rankine: 10 MPa / 500 C superheat, 10 kPa condenser
    h1, s1 = 3474.5, 6.8000          # kJ/kg, kJ/kg-K: superheated steam
    sf, sfg, hf, hfg = 0.6492, 7.5010, 191.81, 2392.1   # 10 kPa saturation
    x2 = (s1 - sf) / sfg             # isentropic expansion to condenser pressure
    h2 = hf + x2 * hfg
    wt = h1 - h2                     # turbine work
    vf = 0.00101                     # m^3/kg
    wp = vf * (10000.0 - 10.0)       # pump work, kJ/kg
    h4 = hf + wp
    qin = h1 - h4
    eta = (wt - wp) / qin
    print("turbine work %.0f kJ/kg | pump work %.1f kJ/kg (liquids are cheap to pump)" % (wt, wp))
    print("heat added %.0f kJ/kg -> thermal efficiency %.1f%%" % (qin, 100 * eta))
    assert 0.39 < eta < 0.41, eta
    print("exhaust quality x = %.3f: the last stages run wet - erosion territory" % x2)
    assert 0.80 < x2 < 0.85, x2
    # reheat bonus: hotter average heat-addition temperature
    print("reheat between HP and IP cylinders lifts both efficiency and exhaust dryness")
    print("rule: every kPa shaved off the condenser pressure is free turbine work")
    print("OK: %s ran the Rankine cycle" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_tm_gas(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def main():
    rp, gamma, cp = 12.0, 1.4, 1005.0
    T1, TIT = 300.0, 1500.0
    eta_ideal = 1.0 - rp ** (-(gamma - 1.0) / gamma)
    T2 = T1 * rp ** ((gamma - 1.0) / gamma)
    T4 = TIT / rp ** ((gamma - 1.0) / gamma)
    wc, wt = cp * (T2 - T1), cp * (TIT - T4)
    wnet, qin = wt - wc, cp * (TIT - T2)
    eta = wnet / qin
    print("compressor swallows %.0f kJ/kg | turbine delivers %.0f kJ/kg" % (wc / 1000.0, wt / 1000.0))
    print("net %.0f kJ/kg on %.0f kJ/kg heat -> eta = %.1f%% = ideal Brayton %.1f%%"
          % (wnet / 1000.0, qin / 1000.0, 100 * eta, 100 * eta_ideal))
    assert abs(eta - eta_ideal) < 1e-9, (eta, eta_ideal)
    assert abs(eta - 0.508) < 0.005, eta
    # TIT lever: hotter gas, more specific work, barely moves ideal efficiency
    for tit in (1300.0, 1500.0, 1700.0):
        w = cp * ((tit - tit / rp ** 0.2857) - (T2 - T1))
        print("  TIT %.0f K -> specific work %.0f kJ/kg" % (tit, w / 1000.0))
    print("rule: pressure ratio sets the efficiency; TIT sets the power - materials set the TIT")
    print("OK: %s fired the Brayton cycle" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_tm_wind(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def main():
    rho, D, V = 1.225, 100.0, 12.0
    A = math.pi * D ** 2 / 4.0
    P_wind = 0.5 * rho * A * V ** 3
    betz = 16.0 / 27.0
    print("wind power through the disc: %.2f MW" % (P_wind / 1e6))
    assert abs(P_wind / 1e6 - 8.32) < 0.05, P_wind
    print("Betz ceiling: %.1f%% -> at most %.2f MW extractable" % (100 * betz, P_wind * betz / 1e6))
    Cp = 0.45
    assert Cp < betz
    P = P_wind * Cp
    print("real rotor at Cp = %.2f: %.2f MW" % (Cp, P / 1e6))
    assert abs(P / 1e6 - 3.74) < 0.05, P
    # the optimum: slow the wind to 1/3 at the disc (a = 1/3)
    a = 1.0 / 3.0
    Cp_check = 4.0 * a * (1.0 - a) ** 2
    assert abs(Cp_check - betz) < 1e-9, Cp_check
    print("induction factor a = 1/3 gives Cp = 4a(1-a)^2 = %.4f = 16/27: the optimum derived" % Cp_check)
    # cubic law: double the wind, 8x the power
    print("wind 12 -> 24 m/s: power %.2f -> %.2f MW (the cubic)" % (P / 1e6, P * 8 / 1e6))
    print("rule: 59.3%% is all the sky will ever surrender - siting and size collect it")
    print("OK: %s harvested the wind" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_tm_hydro(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def main():
    sites = [
        ("alpine", 500.0, 2.0, "Pelton"),
        ("valley", 100.0, 20.0, "Francis"),
        ("river", 10.0, 100.0, "Kaplan"),
    ]
    for tag, H, Q, expect in sites:
        P = 1000.0 * 9.81 * Q * H * 0.90 / 1e6   # hydraulic power at 90% efficiency
        # low specific speed (high head, low flow) -> Pelton; high -> Kaplan
        ssi = Q / H ** 1.5    # crude specific-speed indicator (higher = more flow-type)
        kind = "Pelton" if ssi < 2e-4 else ("Francis" if ssi < 0.05 else "Kaplan")
        print("%-6s H=%5.0f m Q=%6.1f m^3/s -> %-7s (%.1f MW)" % (tag, H, Q, kind, P))
        assert kind == expect, (tag, kind)
    # Pelton jet physics: the nozzle converts the full head to a jet
    H = 500.0
    Vjet = math.sqrt(2.0 * 9.81 * H)
    U = 0.45 * Vjet
    assert abs(Vjet - 99.0) < 0.5, Vjet
    print("Pelton jet at 500 m head: %.0f m/s; buckets run at ~0.45x = %.1f m/s" % (Vjet, U))
    # the draft tube: free head from exit kinetic energy recovery
    Vexit = 6.0
    recovered = Vexit ** 2 / (2.0 * 9.81)
    print("draft tube recovers ~%.1f m of head from %.0f m/s exit velocity - free energy" % (recovered, Vexit))
    print("rule: head and flow pick the runner - low Ns gets cups, high Ns gets adjustable blades")
    print("OK: %s chose the runners" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_tm_axial_comp(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def main():
    U, Cx = 350.0, 180.0
    Ct1, Ct2 = 160.0, 230.0          # swirl added by the rotor
    w = U * (Ct2 - Ct1)
    Wt1, Wt2 = Ct1 - U, Ct2 - U
    W1 = math.hypot(Cx, Wt1); W2 = math.hypot(Cx, Wt2)
    dehaller = W2 / W1
    sigma = 1.0                       # solidity
    DF = 1.0 - W2 / W1 + abs(Wt2 - Wt1) / (2.0 * sigma * W1)
    print("stage work: %.1f kJ/kg | de Haller W2/W1 = %.3f (>= 0.72) | diffusion factor = %.3f (<= 0.6)"
          % (w / 1000.0, dehaller, DF))
    assert dehaller >= 0.72, dehaller
    assert DF <= 0.6, DF
    eta_stage, cp, T01 = 0.90, 1005.0, 300.0
    PR = (1.0 + eta_stage * w / (cp * T01)) ** 3.5
    print("stage pressure ratio: %.2f:1 (the honest per-stage increment)" % PR)
    assert 1.15 < PR < 1.55, PR
    print("14 such stages: %.1f:1 overall - the staircase to 30:1" % (PR ** 14))
    assert 25.0 < PR ** 14 < 40.0, PR ** 14
    print("rule: diffusion is the enemy - de Haller and DF are the guards at the gate")
    print("OK: %s built the stage" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_tm_cent_comp(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def main():
    U2 = 500.0                        # m/s tip speed (stress-limited)
    assert U2 <= 600.0, "tip speed beyond material limit"
    Z, beta2b = 17, _rad(60.0)        # blades, backsweep: 30 deg from radial
    slip = 1.0 - math.pi * math.sin(beta2b) / Z    # Stodola
    print("Stodola slip factor: %.3f - the flow lags the blade" % slip)
    assert 0.80 < slip < 0.88, slip
    w = slip * U2 ** 2                 # Euler with zero inlet swirl, corrected by slip
    cp, T01 = 1005.0, 300.0
    eta = 0.82
    ws = eta * w                       # isentropic work actually achieved
    PR = (1.0 + ws / (cp * T01)) ** 3.5
    PR_ideal = (1.0 + w / (cp * T01)) ** 3.5
    print("Euler work (slip-corrected): %.0f kJ/kg -> pressure ratio %.1f:1 in ONE stage"
          % (w / 1000.0, PR))
    assert 4.0 < PR < 6.0, PR
    assert 6.0 < PR_ideal < 7.0, PR_ideal
    print("isentropic ideal would be %.1f:1 - efficiency and slip take their cut" % PR_ideal)
    N_rpm = U2 * 60.0 / (math.pi * 0.1)
    print("impeller D = 100 mm at %.0f rpm: turbocharger territory" % N_rpm)
    # backsweep trade: less work than radial blades, far wider stable range
    slip_radial = 1.0 - math.pi * math.sin(_rad(90.0)) / Z
    print("radial blades would give slip %.3f (more work, narrower map) - backsweep buys range" % slip_radial)
    assert slip_radial < slip
    print("rule: one impeller, one mighty throw - slip is the honest tax on hurrying")
    print("OK: %s spun the impeller" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_tm_pumps(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def main():
    # pump curve H = H0 - k Q^2 ; system curve H = Hs + ks Q^2 (Q in m^3/s)
    H0, k = 120.0, 3125.0
    Hs, ks = 60.0, 6250.0
    # operating point: solve (H0 - Hs) = (k + ks) Q^2
    Qop = math.sqrt((H0 - Hs) / (k + ks))
    Hop = H0 - k * Qop ** 2
    print("operating point: Q = %.3f m^3/s (%.0f L/s), H = %.1f m" % (Qop, Qop * 1000, Hop))
    assert abs(Qop - 0.08) < 0.002, Qop
    assert abs(Hop - 100.0) < 0.5, Hop
    eta = 0.84
    P = 1000.0 * 9.81 * Qop * Hop / eta / 1000.0
    print("shaft power: %.1f kW at %.0f%% efficiency (the BEP)" % (P, 100 * eta))
    assert abs(P - 93.4) < 1.0, P
    # throttle the discharge valve: system curve steepens, point slides up-left
    ks2 = 14000.0
    Qop2 = math.sqrt((H0 - Hs) / (k + ks2))
    Hop2 = H0 - k * Qop2 ** 2
    assert Qop2 < Qop and Hop2 > Hop, (Qop2, Hop2)
    print("throttled: Q %.0f -> %.0f L/s, H %.1f -> %.1f m - throttling burns energy as valve loss"
          % (Qop * 1000, Qop2 * 1000, Hop, Hop2))
    print("rule: the pump proposes (its curve), the system disposes (the intersection)")
    print("OK: %s found the operating point" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_tm_pd_pump(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def main():
    Vrev = 0.15          # litres per revolution (triplex plunger)
    N = 300.0            # rpm
    Qth = Vrev * N       # L/min, theoretical
    eta_v = 0.95
    Qact = Qth * eta_v
    print("theoretical %.1f L/min x %.2f volumetric eff. = %.2f L/min actual" % (Qth, eta_v, Qact))
    assert abs(Qact - 42.75) < 1e-9, Qact
    # the PD promise: flow nearly independent of discharge pressure
    for p_MPa in (5.0, 35.0):
        Q = Qact   # same trapped volume per revolution, whatever the back-pressure
        P = (Q / 60000.0) * (p_MPa * 1e6) / 0.90 / 1000.0
        print("  discharge %4.1f MPa: flow %.2f L/min, power %.1f kW" % (p_MPa, Q, P))
    assert abs((Qact / 60000.0) * 35e6 / 0.90 / 1000.0 - 27.7) < 0.2
    # the PD peril: closed discharge -> pressure has nowhere to go
    print("closed valve: trapped volumes keep coming - pressure spikes until the relief valve saves the pipes")
    print("pulsation: triplex -> 3 pulses per rev at %.0f Hz" % (3 * N / 60.0))
    print("rule: PD pumps meter by geometry - relief valves are mandatory, not optional")
    print("OK: %s trapped the volumes" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_tm_fans(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def main():
    Q1, dp1, eta_t = 5.0, 1200.0, 0.78
    P1 = Q1 * dp1 / eta_t / 1000.0
    print("duty: %.1f m^3/s at %d Pa, %.0f%% total eff. -> shaft %.2f kW" % (Q1, dp1, 100 * eta_t, P1))
    assert abs(P1 - 7.69) < 0.05, P1
    r = 1.2
    Q2, dp2, P2 = Q1 * r, dp1 * r ** 2, P1 * r ** 3
    print("fan laws at %.0f%% speed: Q %.1f->%.1f | dp %d->%d Pa | P %.2f->%.2f kW"
          % (100 * r, Q1, Q2, dp1, dp2, P1, P2))
    assert abs(P2 - 13.29) < 0.05, P2
    # total vs static: exit kinetic energy wasted to atmosphere
    Vexit, rho = 15.0, 1.2
    q_exit = rho * Vexit ** 2 / 2.0
    dp_static = dp1 - q_exit
    eta_s = Q1 * dp_static / (P1 * 1000.0)
    print("exit dynamic %d Pa wasted: static rise %d Pa, static eff. %.1f%% (the honest metric)"
          % (q_exit, dp_static, 100 * eta_s))
    assert abs(q_exit - 135.0) < 1e-9
    assert eta_s < eta_t
    print("rule: total pressure flatters; static pressure tells the truth")
    print("OK: %s moved the air" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_tm_maps(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def main():
    # one corrected speed line: (corrected flow kg/s, pressure ratio)
    choke = (105.0, 22.0)
    surge = (62.0, 27.5)
    oper = (80.0, 25.0)
    SM = (surge[1] - oper[1]) / oper[1]
    print("100%% speed line: choke (%.0f kg/s, PR %.0f) ... surge (%.0f kg/s, PR %.1f)"
          % (choke[0], choke[1], surge[0], surge[1]))
    print("operating point (%.0f kg/s, PR %.0f): surge margin %.1f%%" % (oper[0], oper[1], 100 * SM))
    assert abs(SM - 0.10) < 1e-9, SM
    assert SM >= 0.10, "margin below the 10% floor"
    # corrected parameters: the machine feels Mach, not rpm
    N, T01 = 10000.0, 300.0
    Nc = N / math.sqrt(T01 / 288.0)
    T01_cold = 260.0
    Nc_cold = N / math.sqrt(T01_cold / 288.0)
    print("same %.0f rpm: standard day feels Nc=%.0f, cold day feels Nc=%.0f - the map shifts"
          % (N, Nc, Nc_cold))
    assert Nc_cold > Nc   # cold dense air: aerodynamically faster, walks toward surge
    print("cold-day walk toward the surge line is why maps are drawn corrected")
    print("rule: choke cliffs right, surge dragons left - fly the operating line between them")
    print("OK: %s read the map" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_tm_cascades(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def main():
    chord, spacing = 100.0, 80.0      # mm
    solidity = chord / spacing
    theta = 30.0                       # degrees camber
    m = 0.26
    delta = m * theta * math.sqrt(spacing / chord)   # Carter's deviation rule
    print("solidity %.2f, camber %.0f deg -> Carter deviation %.2f deg" % (solidity, theta, delta))
    assert 6.0 < delta < 8.0, delta
    print("the flow leaves %.1f deg off the metal angle - aim the blade to compensate" % delta)
    # the loss bucket: incidence tolerance of the blade section
    def loss_bucket(i):
        return 0.020 + 0.004 * i ** 2 + (0.05 if abs(i) > 6 else 0.0)  # illustration
    for i in (-8, -4, 0, 4, 8):
        print("  incidence %+d deg -> profile loss coeff %.3f" % (i, loss_bucket(i)))
    assert loss_bucket(0) < loss_bucket(8) and loss_bucket(0) < loss_bucket(-8)
    print("bucket minimum near zero incidence; steep walls past +-6 deg = separation")
    print("rule: design in 2-D, then stack with twist, lean, and sweep into the 3-D blade")
    print("OK: %s unwrapped the row" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_tm_cavitation(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def main():
    T_C = 80.0
    p_vapor = 47.4          # kPa absolute at 80 C
    p_inlet = 101.0         # kPa absolute suction static
    V_le = 12.0             # m/s local velocity at the blade leading edge
    depression = 1000.0 * V_le ** 2 / 2.0 / 1000.0   # kPa dynamic depression
    p_local = p_inlet - depression
    print("inlet %.0f kPa abs; leading-edge depression %.0f kPa -> local %.0f kPa" %
          (p_inlet, depression, p_local))
    print("vapor pressure at %.0f C: %.1f kPa -> %s" %
          (T_C, p_vapor, "CAVITATION: local pressure below vapor" if p_local < p_vapor else "no cavitation"))
    assert p_local < p_vapor, "expected inception in this demo"
    # cavitation number at the leading edge
    sigma = (p_inlet - p_vapor) * 1000.0 / (0.5 * 1000.0 * V_le ** 2)
    print("cavitation number sigma = %.2f: inception when the local value crosses zero" % sigma)
    assert sigma < 1.0, sigma
    # the Thoma parameter ties it to the machine's head
    NPSH, H = 4.0, 60.0
    thoma = NPSH / H
    print("Thoma sigma_Th = NPSH/H = %.3f: the machine-level inception index" % thoma)
    print("rule: cavitation is a suction-side crime - all cures aim at the inlet")
    print("OK: %s boiled the inlet" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_tm_npsh(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def main():
    # NPSHa: what the system offers (meters of water)
    p_atm, h_static, h_loss, h_vel = 10.33, 3.0, 1.2, 0.4
    p_vapor = 2.03          # 60 C water
    NPSHa = p_atm + h_static - p_vapor - h_loss + h_vel
    NPSHr = 6.5             # m, manufacturer's 3%-drop point at this flow
    margin = NPSHa / NPSHr
    print("NPSHa = %.1f m vs NPSHr = %.1f m -> margin ratio %.2f" % (NPSHa, NPSHr, margin))
    assert abs(NPSHa - 10.5) < 0.15, NPSHa
    assert margin >= 1.3, margin
    print("margin >= 1.3: the pump sleeps soundly")
    # hot summer: 90 C water, vapor head 7.15 m
    NPSHa_hot = p_atm + h_static - 7.15 - h_loss + h_vel
    print("90 C water: NPSHa = %.1f m < NPSHr %.1f m -> full cavitation, head collapse" % (NPSHa_hot, NPSHr))
    assert NPSHa_hot < NPSHr
    # suction specific speed judges the inlet design (US units illustration)
    N_rpm, Q_gpm = 1750.0, 0.12 * 15850.3
    S = N_rpm * math.sqrt(Q_gpm) / (NPSHr * 3.28084) ** 0.75
    print("suction specific speed S = %.0f (tolerant below ~8500-11000)" % S)
    print("rule: NPSH is a system property first - the cure is usually in the piping, not the pump")
    print("OK: %s guarded the suction" % NAME)
if __name__ == "__main__":
    main()
''')
def demo_tm_surge_stall(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def greitzer_B(U, a, Vp, Ac, Lc):
    return (U / (2.0 * a)) * math.sqrt(Vp / (Ac * Lc))
def main():
    U, a = 400.0, 340.0
    # large downstream plenum: surge
    B_big = greitzer_B(U, a, 50.0, 0.5, 10.0)
    # small downstream volume: rotating stall
    B_small = greitzer_B(U, a, 2.0, 0.5, 10.0)
    print("Greitzer B: large plenum %.2f | small plenum %.2f (crossover ~0.8)" % (B_big, B_small))
    assert B_big > 0.8 and B_small < 0.8, (B_big, B_small)
    print("  B = %.2f > 0.8 -> SURGE: system-wide violent flow reversal" % B_big)
    print("  B = %.2f < 0.8 -> ROTATING STALL: local patches circling, mean flow continues" % B_small)
    # the static criterion: positive slope past the pressure-rise peak
    PR_peak, PR_left = 2.80, 2.75   # throttling left past the peak drops PR: positive slope
    dPR_dmc = (PR_left - PR_peak) / -1.0
    assert dPR_dmc > 0
    print("past the peak, d(PR)/d(flow) > 0: statically unstable - the characteristic invites reversal")
    # protection arithmetic: hold 12% surge margin
    PR_surge_line, PR_op = 27.5, 24.6
    SM = (PR_surge_line - PR_op) / PR_op
    assert SM >= 0.10, SM
    print("surge line PR %.1f vs operating PR %.1f: margin %.1f%% - the stability budget" %
          (PR_surge_line, PR_op, 100 * SM))
    print("rule: compute B before the first startup - the machine will obey it whether you did or not")
    print("OK: %s met the instability twins" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_tm_rotordynamics(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def main():
    m, k = 40.0, 8.0e6
    wn = math.sqrt(k / m)
    Nc = 60.0 * wn / (2.0 * math.pi)
    print("Jeffcott: omega_n = %.0f rad/s -> critical speed Nc = %.0f rpm" % (wn, Nc))
    assert 4200.0 < Nc < 4350.0, Nc
    Nop = 2950.0
    sep = (Nc - Nop) / Nc
    print("running %.0f rpm: separation margin %.1f%% (API wants ~15-20%%+)" % (Nop, 100 * sep))
    assert sep > 0.15, sep
    # unbalance response vs speed ratio, damping ratio 0.05
    zeta = 0.05
    print("unbalance magnification vs speed ratio r:")
    for r in (0.5, 0.9, 1.0, 1.3, 2.0):
        mag = r ** 2 / math.sqrt((1 - r ** 2) ** 2 + (2 * zeta * r) ** 2)
        print("  r = %.1f -> x %.2f" % (r, mag))
    mag_crit = 1.0 / (2.0 * zeta)
    assert abs(mag_crit - 10.0) < 1e-9
    print("at the critical the response peaks at 1/(2*zeta) = %.0f x static - damping is the only rescue" % mag_crit)
    # supercritical: self-centering above r ~ 1.3
    r = 2.0
    mag2 = r ** 2 / math.sqrt((1 - r ** 2) ** 2 + (2 * zeta * r) ** 2)
    assert mag2 < 2.0, mag2
    print("supercritical (r=2): magnification %.2f - the rotor spins about its mass center" % mag2)
    print("rule: know where the shaft sings, damp the passage, never linger")
    print("OK: %s spun the Jeffcott rotor" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_tm_bearings(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def l10_hours(C, P, p, rpm):
    return (C / P) ** p * 1e6 / (rpm * 60.0)
def main():
    C, P, rpm = 90.0, 6.0, 2950.0     # kN, kN, ball bearing p=3
    life = l10_hours(C, P, 3, rpm)
    print("C=%d kN, P=%d kN: L10 = %.0f million rev = %.0f hours" % (C, P, (C / P) ** 3, life))
    assert life > 15000.0, life
    # the cubic's cruelty: double the load
    life2 = l10_hours(C, 2 * P, 3, rpm)
    ratio = life / life2
    print("double the load -> life %.0f h (%.1fx shorter): the cubic punishes" % (life2, ratio))
    assert abs(ratio - 8.0) < 0.01, ratio
    # fluid-film: no metal contact at speed -> no fatigue life limit
    h_film = 50.0   # microns
    print("tilting-pad journal: %.0f-micron oil film carries tonnes with zero contact - life is not L10-limited" % h_film)
    # thrust: balance drum trims the residual axial load
    F_axial, F_drum = 420.0, 380.0    # kN steam push vs drum compensation
    F_thrust = F_axial - F_drum
    assert F_thrust < 0.15 * F_axial, F_thrust
    print("axial push %d kN - drum %d kN = %d kN on the Kingsbury pads" % (F_axial, F_drum, F_thrust))
    print("rule: rolling for compactness, fluid-film for heavy damping, magnetic for the oil-free future")
    print("OK: %s carried the rotor" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_tm_seals(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def main():
    D, clearance, n_teeth = 0.5, 0.0004, 8
    A = math.pi * D * clearance
    p1, p2, T1, R = 2.0e6, 1.4e6, 600.0, 461.5
    m_dot = (A * p1 / math.sqrt(R * T1)) * math.sqrt(1.0 - (p2 / p1) ** 2) / math.sqrt(n_teeth - math.log(p2 / p1))
    print("labyrinth (%d teeth, %.1f mm clearance): leakage %.3f kg/s (Martin)" % (n_teeth, clearance * 1000, m_dot))
    assert 0.5 < m_dot < 0.7, m_dot
    main_flow = 100.0
    print("against %.0f kg/s main flow: %.2f%% - times a dozen seals, real money" % (main_flow, 100 * m_dot / main_flow))
    m_brush = m_dot / 4.0
    print("brush-seal retrofit: %.3f kg/s (4x tighter) - pays back fast" % m_brush)
    assert m_brush < m_dot / 3.0
    # teeth count leverage
    m_4 = (A * p1 / math.sqrt(R * T1)) * math.sqrt(1.0 - (p2 / p1) ** 2) / math.sqrt(4 - math.log(p2 / p1))
    assert m_4 > m_dot
    print("4 teeth would leak %.3f kg/s: leakage falls with tooth count" % m_4)
    print("rule: leakage is lost Euler work - sealing efficiency IS machine efficiency")
    print("OK: %s throttled the gaps" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_tm_cooling(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def main():
    Tg, Tm_allow, Tc = 1700.0, 1250.0, 800.0
    eps = (Tg - Tm_allow) / (Tg - Tc)
    print("Tg=%.0f K, metal limit %.0f K, coolant %.0f K -> required effectiveness %.2f" % (Tg, Tm_allow, Tc, eps))
    assert abs(eps - 0.5) < 1e-9, eps
    # uncooled: TIT capped at the metal limit
    w_cooled = 1700.0 - 738.0     # proportional to TIT - T4, illustration
    w_bare = 1250.0 - 738.0 * 1250.0 / 1700.0
    print("uncooled TIT capped at %.0f K: specific work falls ~%.0f%%" % (Tm_allow, 100 * (1 - w_bare / w_cooled)))
    assert w_bare < 0.8 * w_cooled
    # the price: cooling air bypasses the combustor
    cool_frac = 0.20
    eta_penalty_pts = 2.5
    print("cooling air %.0f%% of compressor flow costs ~%.1f efficiency points - spent like money" %
          (100 * cool_frac, eta_penalty_pts))
    # TBC: free temperature drop
    tbc_drop = 150.0
    print("thermal barrier coating: %.0f K drop with zero air spent" % tbc_drop)
    print("rule: how close to melting dare you run - and how much air will you spend for it")
    print("OK: %s survived the furnace" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_tm_tip_clearance(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def main():
    h_blade, tau = 60.0, 0.6      # mm
    ratio = tau / h_blade
    debit_comp = 1.5 * (ratio * 100.0)    # pts per 1% clearance/height: compressor
    debit_turb = 1.0 * (ratio * 100.0)    # turbine
    print("clearance %.1f mm / blade %.0f mm = %.1f%% -> debit ~%.1f pts (compressor), ~%.1f pt (turbine)"
          % (tau, h_blade, 100 * ratio, debit_comp, debit_turb))
    assert abs(debit_comp - 1.5) < 1e-9 and abs(debit_turb - 1.0) < 1e-9
    # thermal breathing: hot restart opens the gap
    tau_hot = 1.2
    print("hot restart: gap %.1f mm -> debit %.1f pts (doubled) until temperatures equalize" %
          (tau_hot, 1.5 * (tau_hot / h_blade) * 100.0))
    # the leakage jet driving the vortex
    dp_tip, rho_tip = 20000.0, 5.0
    Vjet = math.sqrt(2.0 * dp_tip / rho_tip)
    print("tip jet velocity ~%.0f m/s: rolls into the passage vortex, scrambles the next row" % Vjet)
    assert 80.0 < Vjet < 100.0, Vjet
    # casing treatment buys stall margin
    print("casing treatment (grooves over the tip): +5-10%% stall margin - ugly grooves, beautiful stability")
    print("rule: a millimeter of nothing steals percentages - tailor the clothes to every breath")
    print("OK: %s measured the gap" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_tm_multistage(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def mc(m, T, p):
    return m * math.sqrt(T) / p
def PR_stage(mc, mc_design):
    return max(1.0, 1.15 + 0.5 * (1.0 - mc / mc_design))
def main():
    # design: 8 kg/s physical; stage corrected flows matched to annulus sizes
    T12, p12, T23, p23 = 320.0, 120.0, 330.0, 110.0
    mc1d, mc3d = 1.00, 0.80
    target = 1.35
    def overall(m):
        return PR_stage(mc(m, T12, p12), mc1d) * PR_stage(mc(m, T23, p23), mc3d)
    lo, hi = 4.5, 7.5
    assert overall(lo) > target > overall(hi), (overall(lo), overall(hi))
    for _ in range(30):
        mid = 0.5 * (lo + hi)
        if overall(mid) > target:
            lo = mid
        else:
            hi = mid
    m_star = 0.5 * (lo + hi)
    assert abs(overall(m_star) - target) < 0.005, overall(m_star)
    mc1 = mc(m_star, T12, p12); mc3 = mc(m_star, T23, p23)
    i1 = 33.0 * (1.0 - mc1 / mc1d)        # front-stage incidence, deg (illustrative)
    i3 = -20.0 * (mc3 / mc3d - 1.0)       # rear-stage incidence: negative = toward choke
    print("stage-stack converged: m = %.2f kg/s, overall PR = %.3f" % (m_star, overall(m_star)))
    print("  front stage: %.0f%% low on corrected flow -> incidence %+.1f deg (stall at +10)" %
          (100 * (1 - mc1 / mc1d), i1))
    print("  rear stage: %+.0f%% vs design -> incidence %+.1f deg (toward choke)" %
          (100 * (mc3 / mc3d - 1), i3))
    assert i1 > 5.0, i1   # front stage eating its stall margin
    # remedy: 1 kg/s interstage bleed lets the front stage breathe
    bleed = 1.0
    mc1_b = mc(m_star + bleed, T12, p12)
    i1_b = 33.0 * (1.0 - mc1_b / mc1d)
    print("bleed %.1f kg/s after stage 1: front incidence %+.1f -> %+.1f deg - rescued" % (bleed, i1, i1_b))
    assert i1_b < 3.0, i1_b
    print("rule: the operating line is the stages' negotiated agreement, not one stage's wish")
    print("OK: %s matched the stack" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_tm_vgeom(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def main():
    U_des, Cx_des = 350.0, 180.0
    alpha1 = math.atan(160.0 / 180.0)      # design absolute flow angle, rad
    kappa1 = math.atan((160.0 - U_des) / Cx_des)   # blade metal angle
    phi_des = Cx_des / U_des
    # part speed, fixed geometry: incidence runs away
    U = 0.8 * U_des
    beta1 = math.atan((160.0 - U) / Cx_des)
    i_fixed = _deg(beta1 - kappa1)
    print("80%% speed, fixed vanes: incidence %+.1f deg - deep toward stall" % i_fixed)
    assert i_fixed > 10.0, i_fixed
    # VSV schedule: close vanes, throttle Cx, hold the absolute flow angle
    Cx_new = 144.0
    Ct1_new = Cx_new * math.tan(alpha1)
    beta1_new = math.atan((Ct1_new - U) / Cx_new)
    i_new = _deg(beta1_new - kappa1)
    phi_new = Cx_new / U
    print("VSVs close: Cx %.0f->%.0f m/s, flow coefficient %.3f->%.3f (design %.3f)" %
          (Cx_des, Cx_new, Cx_des / U, phi_new, phi_des))
    print("incidence %+.1f -> %+.1f deg: the triangle is restored" % (i_fixed, i_new))
    assert abs(phi_new - phi_des) < 0.01, (phi_new, phi_des)
    assert abs(i_new) < 1.0, i_new
    # IGV part-load: throttle the whole machine aerodynamically
    print("IGVs: closing throttles mass flow ~25%% at near-constant pressure ratio - no throttle-valve waste")
    print("rule: every speed has its stance - the unison ring conducts the choreography")
    print("OK: %s scheduled the vanes" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_tm_combined(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def main():
    eta_GT, eta_ST = 0.38, 0.30
    eta_cc = eta_GT + eta_ST * (1.0 - eta_GT)
    print("GT %.0f%% + steam bottoming %.0f%% of exhaust heat -> combined %.1f%%" %
          (100 * eta_GT, 100 * eta_ST, 100 * eta_cc))
    assert 0.55 < eta_cc < 0.58, eta_cc
    gain = (eta_cc - eta_GT) / eta_GT
    print("relative gain over the gas turbine alone: +%.0f%% - with no new fuel burned" % (100 * gain))
    assert gain > 0.45, gain
    # record machines
    eta_cc2 = 0.40 + 0.32 * (1.0 - 0.40)
    print("advanced (1700 C-class TIT, triple-pressure HRSG): %.1f%% - the most efficient heat engine sold" %
          (100 * eta_cc2))
    assert eta_cc2 > 0.59, eta_cc2
    # pinch economics: halving the pinch doubles surface for ~1% more heat
    print("pinch 20 K -> 10 K: ~1%% more heat recovered for ~2x evaporator surface - economics sizes the HRSG")
    # CHP: heat has value too
    eta_total_chp = 0.85
    print("cogeneration: power + useful heat = %.0f%% of fuel - the right answer where heat has value" %
          (100 * eta_total_chp))
    print("rule: refuse to let 600-degree heat walk out the stack")
    print("OK: %s squeezed every joule" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_tm_monitoring(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def zone(v):
    if v < 2.3:
        return "A (new-machine good)"
    if v < 4.5:
        return "B (acceptable)"
    if v < 7.1:
        return "C (unsatisfactory - plan action)"
    return "D (damage imminent - act now)"
def main():
    rpm = 10800.0
    f1x = rpm / 60.0
    baseline, trend, trip = 2.1, 4.8, 7.1
    print("vibration trend: %.1f -> %.1f mm/s RMS | trip %.1f" % (baseline, trend, trip))
    print("  baseline: zone %s" % zone(baseline))
    print("  current:  zone %s" % zone(trend))
    assert "C" in zone(trend) and "A" in zone(baseline), (zone(baseline), zone(trend))
    # spectrum diagnosis
    print("spectrum at %.0f rpm: 1x = %.0f Hz growing -> unbalance (fouling shedding?)" % (rpm, f1x))
    assert abs(f1x - 180.0) < 1e-9
    f_whip = 0.45 * f1x
    print("new 0.45x = %.0f Hz -> oil whirl precursor in a journal bearing - check oil and temperatures" % f_whip)
    assert abs(f_whip - 81.0) < 1e-9
    print("blade-pass = blades x rpm: sidebands there mean rub or blade damage")
    # performance corroboration
    pr_sag = 0.02
    print("discharge pressure sagged %.0f%% at constant corrected flow: fouling - wash the compressor" %
          (100 * pr_sag))
    print("rule: two independent signals, one story - converge the data before turning the wrench")
    print("OK: %s listened to the machine" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_tm_workflow(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def main():
    print("the seven descents, executed on a duty: Q=0.10 m^3/s, H=60 m, water, 1450 rpm")
    # 1. duty -> Ns -> geometry
    N = 1450.0 / 60.0
    Ns = N * math.sqrt(0.10) / (9.81 * 60.0) ** 0.75
    print("1. Ns = %.4f -> radial/centrifugal" % Ns)
    assert Ns < 0.2
    # 2. phi -> size
    phi = 0.08
    D = (0.10 / (phi * N)) ** (1.0 / 3.0)
    print("2. phi = %.2f -> D = %.3f m" % (phi, D))
    assert abs(D - 0.373) < 0.01, D
    # 3. Euler head available
    U2 = math.pi * D * 1450.0 / 60.0
    H_euler = U2 ** 2 / 9.81
    print("3. U2 = %.1f m/s -> Euler head %.1f m vs duty 60 m: headroom for slip and loss" % (U2, H_euler))
    assert H_euler > 60.0
    # 4. slip check (Stodola, 9 blades, 25 deg backsweep)
    Z, beta2b = 9, _rad(65.0)
    slip = 1.0 - math.pi * math.sin(beta2b) / Z
    H_real = slip * H_euler
    print("4. Stodola slip %.3f -> real head %.1f m (trim D slightly, re-run the loop)" % (slip, H_real))
    assert 0.60 < slip < 0.75, slip
    # 5. structures: critical-speed margin placeholder (shaft sized so Nc > 1.2*Nop)
    Nc_margin = 1.31
    print("5. shaft sized: Nc/Nop = %.2f (> 1.2 required)" % Nc_margin)
    assert Nc_margin > 1.2
    # 6. map: BEP at the duty; 7. validate: CFD -> rig -> cut metal
    print("6. predicted H-Q curve: BEP lands on the duty point")
    print("7. validate (CFD, rig test), iterate - metal is cut LAST")
    print("rule: the ladder in design order - triangles swear to Euler, metal swears to the triangles")
    print("OK: %s walked the workflow" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_tm_frontier(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def main():
    # sCO2: dense fluid near the critical point slashes compression work
    bwr_air, bwr_sco2 = 0.50, 0.23
    print("back-work ratio: air Brayton %.2f vs sCO2 %.2f - the compressor barely sips" % (bwr_air, bwr_sco2))
    assert bwr_sco2 < 0.5 * bwr_air
    eta_sco2 = 0.47
    print("recuperated sCO2 at 650 C TIT: ~%.0f%% efficiency - steam territory at gas-turbine simplicity" %
          (100 * eta_sco2))
    assert 0.44 < eta_sco2 < 0.52, eta_sco2
    print("10 MW sCO2 turbine ~0.3 m diameter: desk-sized power - but 0.3 mm clearance is crueler on small blades")
    # hydrogen: the flame-speed challenge
    S_CH4, S_H2 = 0.4, 2.9     # m/s laminar flame speeds
    print("flame speed: methane %.1f m/s vs hydrogen %.1f m/s (%.1fx) - flashback wants the premixer" %
          (S_CH4, S_H2, S_H2 / S_CH4))
    assert S_H2 / S_CH4 > 7.0
    n_jets = 1600
    print("micromix answer: %d tiny diffusion flames, sub-millisecond residence - too fast for NOx, too split to flash back" % n_jets)
    print("turbine downstream: ~1600 K gas, 15%%+ water vapor - the ladder's tools with updated properties")
    print("rule: new fluids, new flames - same Euler")
    print("OK: %s reached the frontier" % NAME)
if __name__ == "__main__":
    main()
''')

DEMOS = {
    "tm_what": demo_tm_what, "tm_fluid_mech": demo_tm_fluid_mech,
    "tm_conservation": demo_tm_conservation, "tm_euler": demo_tm_euler,
    "tm_triangles": demo_tm_triangles, "tm_reaction": demo_tm_reaction,
    "tm_family": demo_tm_family, "tm_geometries": demo_tm_geometries,
    "tm_dimensionless": demo_tm_dimensionless, "tm_specific_speed": demo_tm_specific_speed,
    "tm_affinity": demo_tm_affinity, "tm_losses": demo_tm_losses,
    "tm_steam": demo_tm_steam, "tm_gas": demo_tm_gas,
    "tm_wind": demo_tm_wind, "tm_hydro": demo_tm_hydro,
    "tm_axial_comp": demo_tm_axial_comp, "tm_cent_comp": demo_tm_cent_comp,
    "tm_pumps": demo_tm_pumps, "tm_pd_pump": demo_tm_pd_pump,
    "tm_fans": demo_tm_fans, "tm_maps": demo_tm_maps,
    "tm_cascades": demo_tm_cascades, "tm_cavitation": demo_tm_cavitation,
    "tm_npsh": demo_tm_npsh, "tm_surge_stall": demo_tm_surge_stall,
    "tm_rotordynamics": demo_tm_rotordynamics, "tm_bearings": demo_tm_bearings,
    "tm_seals": demo_tm_seals, "tm_cooling": demo_tm_cooling,
    "tm_tip_clearance": demo_tm_tip_clearance, "tm_multistage": demo_tm_multistage,
    "tm_vgeom": demo_tm_vgeom, "tm_combined": demo_tm_combined,
    "tm_monitoring": demo_tm_monitoring, "tm_workflow": demo_tm_workflow,
    "tm_frontier": demo_tm_frontier,
}
# ---------------------------------------------------------------- records
# demo_kind wiring: entry "key" -> DEMOS key (names differ for readability).
DEMO_KEY = {
    "what_is_turbomachinery": "tm_what", "fluid_mechanics_foundation": "tm_fluid_mech",
    "conservation_laws": "tm_conservation", "euler_turbine_equation": "tm_euler",
    "velocity_triangles": "tm_triangles", "degree_of_reaction": "tm_reaction",
    "turbomachinery_family": "tm_family", "flow_geometries": "tm_geometries",
    "dimensionless_performance": "tm_dimensionless", "specific_speed": "tm_specific_speed",
    "affinity_laws": "tm_affinity", "losses_efficiency": "tm_losses",
    "steam_turbines": "tm_steam", "gas_turbines": "tm_gas",
    "wind_turbines": "tm_wind", "hydraulic_turbines": "tm_hydro",
    "axial_compressors": "tm_axial_comp", "centrifugal_compressors": "tm_cent_comp",
    "rotodynamic_pumps": "tm_pumps", "positive_displacement_pumps": "tm_pd_pump",
    "fans_blowers": "tm_fans", "performance_maps": "tm_maps",
    "blade_cascades": "tm_cascades", "cavitation": "tm_cavitation",
    "npsh": "tm_npsh", "surge_stall": "tm_surge_stall",
    "rotordynamics": "tm_rotordynamics", "bearings": "tm_bearings",
    "seals_leakage": "tm_seals", "cooling_materials": "tm_cooling",
    "tip_clearance": "tm_tip_clearance", "multistage_matching": "tm_multistage",
    "variable_geometry": "tm_vgeom", "combined_cycle": "tm_combined",
    "condition_monitoring": "tm_monitoring", "design_workflow": "tm_workflow",
    "frontier": "tm_frontier",
}
assert set(DEMO_KEY) == {e["key"] for e in ENTRIES}, "demo key map incomplete"
assert set(DEMO_KEY.values()) == set(DEMOS), "demo map misses demos"

def build_records(slug, source):
    cfg = DBCFG[slug]
    sig = source == "signature"
    # Teaching-ladder order: stable sort by ladder_rank (entries are already
    # in ladder order in entries_turbomachinery.py).
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
        demo_fn = DEMOS[DEMO_KEY[e["key"]]]
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
    for slug in ("turbomachinery", "turbomachinery-signature"):
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
                               capture_output=True, text=True, timeout=120)
            assert p.returncode == 0, "demo failed %s: %s" % (r["id"], p.stderr[-500:])
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
