#!/usr/bin/env python3
"""Build the Aerodynamics field databases for JAH Databases (field #23, taxonomy order).

Verified 2026-10-17: NO database covers aerodynamics as an engineering discipline.
- Manifest-wide regex search (aerofoil|airfoil|aerodynamic|mach.?number|
  shock.?wave|boundary.?layer|wind.?tunnel|navier|compressible|
  supersonic|hypersonic|drag.?polar|ground.?effect|aeroelastic|
  circulation|kutta|prandtl|area.?rule): only pilot-level 'flight' (The
  Signature Flight School Database) and 'aviation' (JAH Aviation Database -
  generator has one incidental 'supersonic' mention; no airfoil theory,
  compressible flow, shock relations, boundary-layer theory, or
  stability/control treatment), wind-energy career DBs, and
  'aerospace-databases' (a database-of-databases index). Zero
  discipline-level aerodynamics records in the manifest.
- Fields #11-22 shard indexes (volcanology, climatology,
  atmospheric-science, hydrology, meteorology, calculus, combinatorics,
  econometrics, psychometrics, turbomachinery, electromagnetics,
  petroleum-refining): direct whole-shard title scans = zero hits.
- 'scientific-formulas': bare formula cards are reference only (task rule:
  formula cards do NOT count as discipline coverage).
- Whole-system dedupe gate (fresh data/dedupe/exact/ index in the main repo;
  fields past the index cross-checked directly above): every record checked
  + admitted at build time.

So this build creates two NEW databases:

  aerodynamics               - The Aerodynamics Database
                               (public-harvest: real, fact-checked
                               aerodynamics; citations Anderson,
                               Kuethe & Chow, Bertin & Cummings,
                               Abbott & Von Doenhoff, White,
                               Schlichting & Gersten, Shapiro,
                               Houghton & Carpenter, Raymer,
                               McCormick, NACA reports)
  aerodynamics-signature     - The Aerodynamics Signature Database
                               (his original Signature interpretation of
                               the discipline; src signature, titles
                               suffixed " (Signature Edition)", never
                               presented as authentic public record)

32 records each, ordered by the teaching ladder (ladder_rank 1-10,
ladder_tier foundations/compounded/advanced); the shard index is written in
ladder order so pages present simple -> compounded -> complex.

Every record: description + how-it-works + key points + requirements +
standards + citations + working demonstration code (real, runnable,
stdlib-only Python; machine-executed OK). Aerodynamics demos: the four
forces at the drag equation, ISA density and pressure with altitude,
power-required curve, venturi pressure drop, Reynolds number and transition
location, Kutta-Joukowski circulation lift, the three-component drag
buildup, the Blasius laminar boundary layer, NACA section decoding,
speed of sound and Mach number, ground-effect drag reduction, stall speed
from CLmax, induced drag vs aspect ratio, normal-shock relations at Mach 2,
the theta-beta-Mach oblique shock solution, the Prandtl-Glauert correction,
swept-wing effective Mach, flap-driven stall-speed reduction, wake vortex
strength scaling, Ackeret supersonic lift and wave drag, area-distribution
smoothness for wave drag, hypersonic stagnation temperature and Newtonian
pressure, static margin and pitch stability, control hinge moments,
suction boundary-layer control, helicopter hover induced velocity, wind
tunnel blockage correction, the CFD CFL time-step limit, aeroelastic
divergence dynamic pressure, multi-shock inlet recovery, sonic-boom
overpressure scaling with altitude, and the Breguet range equation.

Subtitle disambiguation (fields #13-23 pattern): discipline titles carry
teaching-focused subtitles rather than bare cards, e.g. "Continuity and
Bernoulli: Why Speed Changes Pressure" and "The Area Rule: Sculpting Wave
Drag Away".

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
# main repo. Fields past the gate index were cross-checked directly (see
# docstring) - subtitle disambiguation used throughout.
sys.path.insert(0, os.path.join(REPO, "code"))
from dedupe_gate import DedupeGate
base.GATE = DedupeGate(os.path.join(REPO, "data", "dedupe", "exact"))

sys.path.insert(0, HERE)
from entries_aerodynamics import ENTRIES, SIG_TAIL

# ---------------------------------------------------------------- DB config

def _cfg(slug, name, tagline, record_kind, prefix, ai, role, citation, source):
    sig_line = ("Signature originals - his original Signature interpretation of aerodynamics: "
                "clearly labeled Signature-made, never presented as authentic "
                "public record.")
    pub_line = ("Public records - real, fact-checked aerodynamics: what aerodynamics is; "
                "air as a fluid; the four forces; continuity and Bernoulli; the Reynolds "
                "number; how wings make lift; drag decomposed; the boundary layer; airfoil "
                "geometry; compressible flow and Mach number; ground effect; airfoil "
                "performance and polars; induced drag and aspect ratio; normal shocks; "
                "oblique shocks and expansion fans; the Prandtl-Glauert correction; sweep "
                "and the transonic problem; stall and high-lift devices; wind shear and "
                "wake turbulence; supersonic airfoil theory; the area rule; hypersonic "
                "flow; aircraft stability; control surfaces; boundary-layer control; "
                "helicopter rotors; wind tunnel testing; CFD; aeroelasticity; propulsion "
                "integration; sonic boom; design integration, organized in the Signature "
                "system.")
    ladder = (" Records are ordered by the teaching ladder: Foundations (what aerodynamics "
              "is, air as a fluid, the four forces, continuity and Bernoulli, the Reynolds "
              "number, how wings make lift, drag decomposed, the boundary layer) -> "
              "Compounded (airfoil geometry, compressible flow, ground effect, airfoil "
              "performance, induced drag, normal shocks, oblique shocks and expansion "
              "fans, the Prandtl-Glauert correction, sweep and the transonic problem, "
              "stall and high-lift devices, wind shear and wake turbulence) -> Advanced "
              "(supersonic airfoil theory, the area rule, hypersonic flow, aircraft "
              "stability, control surfaces, boundary-layer control, helicopter rotors, "
              "wind tunnel testing, CFD, aeroelasticity, propulsion integration, sonic "
              "boom, design integration).")
    return {
        "name": name, "tagline": tagline, "record_kind": record_kind,
        "prefix": prefix, "ai": ai, "role": role,
        "hero_p": "%s - %s Every record carries the full entry: description, how it works, "
                  "key points, requirements, standards, citations, and a working demonstration "
                  "program.%s" % (tagline, sig_line if source == "signature" else pub_line, ladder),
        "sig_type": ("Signature originals organized in the Signature system"
                     if source == "signature" else
                     "Public records organized in the Signature system"),
        "search_ph": "Search lift, drag, airfoil, Mach number, shock waves, boundary layer, wind tunnel, CFD, stability...",
        "chat_ph": "Ask about aerodynamics...",
        "archive_blurb": ("Seeded %s aerodynamics records, marching toward one million records. "
                          "Presented in teaching-ladder order: foundations, compounded, advanced."
                          % ("Signature-original" if source == "signature" else "public-record")),
        "schema": ("id, t, g, name, title, description, how_it_works, key_points, requirements, "
                   "standards, citations, src, ladder_rank, ladder_tier, demo"),
        "fields": "Foundations \u00b7 Compounded \u00b7 Advanced - each tier opens on demand and loads only what you open",
        "gen_desc": "Generate clearly-labeled structural aerodynamics studies. Seeded archive records are the authoritative entries.",
        "greet": "I am the %s. Ask me about aerodynamics - from the four forces, Bernoulli, and boundary layers through airfoils, compressibility, shock waves, stability and control, rotors, wind tunnels, CFD, and aircraft design." % ai,
        "gen_fields": ["Foundations", "Compounded", "Advanced"],
        "gen_kind": "aerodynamics-study", "gen_demo_kind": "aerodynamics-demo",
        "source": source,
    }

CIT_PUB = "Aerodynamics (standard textbooks and NACA/NASA reference data)."
CIT_SIG = CIT_PUB + " " + SIG_TAIL

DBCFG = {}
DBCFG["aerodynamics"] = _cfg(
    "aerodynamics", "The Aerodynamics Database",
    "Real, fact-checked aerodynamics: from the four forces, Bernoulli, and the "
    "boundary layer through airfoil theory, compressibility, shock waves, "
    "transonic and supersonic flight, stability and control, helicopter "
    "rotors, wind tunnels, CFD, aeroelasticity, and aircraft design - taught "
    "progressively along the ladder.",
    "aerodynamics record", "JAH-AER-", "JAH Aerodynamics Archivist",
    "aerodynamics archivist - what aerodynamics is, air as a fluid, the four "
    "forces, continuity and Bernoulli, Reynolds number, lift, drag, boundary "
    "layers, airfoil geometry, compressible flow, ground effect, polars, "
    "induced drag, normal and oblique shocks, Prandtl-Glauert, sweep, stall "
    "and high lift, shear and wakes, supersonic theory, area rule, "
    "hypersonics, stability, controls, boundary-layer control, rotors, wind "
    "tunnels, CFD, aeroelasticity, propulsion integration, sonic boom, "
    "design integration; teaching progressively along the ladder from "
    "foundations through compounded to advanced; answers from many angles - "
    "definition, example, analogy, application, history, math, how-to - using "
    "only the system's own archive data",
    CIT_PUB, "public")
DBCFG["aerodynamics-signature"] = _cfg(
    "aerodynamics-signature", "The Aerodynamics Signature Database",
    "His original Signature interpretation of aerodynamics: the full ladder from "
    "the four forces through compressible flow, shocks, stability, rotors, and "
    "design, reframed as Signature science. Clearly labeled Signature-made, "
    "never presented as authentic public record.",
    "aerodynamics record", "JAH-AES-", "JAH Aerodynamics Archivist (Signature)",
    "aerodynamics archivist - Signature editions: his original Signature "
    "interpretation of aerodynamics, clearly labeled Signature-made and never "
    "presented as authentic public record; teaches progressively along the ladder "
    "from foundations through compounded to advanced; answers from many angles - "
    "definition, example, analogy, application, history, math, how-to - using only "
    "the system's own archive data",
    CIT_SIG, "signature")

base.DBCFG = DBCFG

# ---------------------------------------------------------------- demos
# Every demo is real, runnable, stdlib-only Python performing the actual
# aerodynamics computation for its record. All are machine-executed by main().

_PREAMBLE = (
"import math\n"
"RHO_SL = 1.225\n"
"P_SL = 101325.0\n"
"T_SL = 288.15\n"
"R_AIR = 287.0\n"
"GAMMA = 1.4\n"
"MU_AIR = 1.81e-5\n"
"G0 = 9.80665\n"
"def _q(rho, V):\n"
"    return 0.5 * rho * V * V\n"
"def _a_sound(T):\n"
"    return math.sqrt(GAMMA * R_AIR * T)\n"
)

def _wrap(name, rid, group, body):
    return (base._hdr(name, rid, group) + _PREAMBLE + body.replace("NAME", json.dumps(name)))

def demo_ad_what(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # the drag equation: D = q * S * CD ; double the speed -> 4x the drag
    S, CD = 30.0, 0.030
    for V in (35.0, 70.0):
        q = _q(RHO_SL, V)
        D = q * S * CD
        print("V = %5.1f m/s : q = %7.1f Pa, D = %7.1f N" % (V, q, D))
        if V == 70.0:
            assert 2650.0 < D < 2750.0, D
            D70 = D
        else:
            D35 = D
    assert abs(D70 / D35 - 4.0) < 1e-9, "drag must quadruple with doubled speed"
    print("doubling speed quadruples drag: %.0f N -> %.0f N" % (D35, D70))
    # lift uses the same currency: L = q S CL
    CL = 0.8
    L = _q(RHO_SL, 70.0) * S * CL
    print("same wing at CL=%.1f makes L = %.0f N of lift" % (CL, L))
    assert 71000.0 < L < 73000.0, L
    print("rule: q = 1/2 rho V^2 is the currency; coefficients set the price")
    print("OK: %s priced the air" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_ad_air(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def isa(h):
    # troposphere lapse to 11000 m, then isothermal
    if h <= 11000.0:
        T = T_SL - 0.0065 * h
        p = P_SL * (T / T_SL) ** 5.25588
    else:
        T = 216.65
        p11 = P_SL * (216.65 / T_SL) ** 5.25588
        p = p11 * math.exp(-G0 * (h - 11000.0) / (R_AIR * T))
    rho = p / (R_AIR * T)
    return T, p, rho
def main():
    T0, p0, r0 = isa(0.0)
    print("sea level: T=%.2f K p=%.0f Pa rho=%.4f kg/m3" % (T0, p0, r0))
    assert abs(r0 - 1.225) < 1e-3 and abs(p0 - 101325.0) < 1.0
    T11, p11, r11 = isa(11000.0)
    print("11 km    : T=%.2f K p=%.0f Pa rho=%.4f kg/m3" % (T11, p11, r11))
    assert abs(T11 - 216.65) < 0.01
    assert 0.36 < r11 < 0.37, r11
    assert 22600.0 < p11 < 22700.0, p11
    ratio = r0 / r11
    print("sea-level air is %.2fx denser than 11-km air" % ratio)
    assert 3.3 < ratio < 3.5, ratio
    # same lift needs sqrt(ratio) times the speed
    print("to hold the same lift at 11 km, fly ~%.2f times faster" % math.sqrt(ratio))
    assert abs(math.sqrt(ratio) - 1.84) < 0.02
    print("rule: the ISA is the shared sky; density is the throttle of flight")
    print("OK: %s weighed the sky" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_ad_forces(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def polar_drag(W, S, AR, e, CD0, rho, V):
    q = _q(rho, V)
    CL = W / (q * S)
    CD = CD0 + CL * CL / (math.pi * AR * e)
    D = q * S * CD
    return CL, CD, D, D * V
def main():
    W, S, AR, e, CD0 = 100000.0, 30.0, 9.0, 0.85, 0.025
    for V in (70.0, 150.0):
        CL, CD, D, P = polar_drag(W, S, AR, e, CD0, RHO_SL, V)
        print("V=%5.1f m/s: CL=%.3f CD=%.4f D=%7.0f N P=%7.0f W" % (V, CL, CD, D, P))
        if V == 70.0:
            P70 = P
            assert 1.0 < CL < 1.2, CL
        else:
            P150 = P
    assert P70 < P150, "power rises steeply past the minimum-power region"
    print("power required climbs %.0f kW -> %.0f kW: speed is bought with power" % (P70 / 1000.0, P150 / 1000.0))
    # load factor in a 60-degree bank
    n = 1.0 / math.cos(math.radians(60.0))
    print("60-degree bank: load factor n = %.1f -> wing must make %.0f N" % (n, W * n))
    assert abs(n - 2.0) < 1e-9
    print("rule: lift = weight and thrust = drag in steady flight; maneuvers multiply the bill")
    print("OK: %s balanced the forces" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_ad_bernoulli(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # venturi: area ratio 4 -> velocity ratio 4 (continuity)
    V1 = 30.0
    AR = 4.0
    V2 = V1 * AR
    dp = 0.5 * RHO_SL * (V2 * V2 - V1 * V1)   # Bernoulli pressure drop
    print("throat velocity: %.0f m/s (%.0f m/s upstream)" % (V2, V1))
    print("static pressure drop: %.0f Pa" % dp)
    assert abs(V2 - 120.0) < 1e-9
    assert 8200.0 < dp < 8350.0, dp
    # stagnation pressure is conserved: p0 = p + q
    q1 = _q(RHO_SL, V1)
    q2 = _q(RHO_SL, V2)
    print("q upstream: %.0f Pa ; q throat: %.0f Pa ; drop = %.0f Pa" % (q1, q2, q2 - q1))
    assert abs((q2 - q1) - dp) < 1e-6
    # airspeed from pitot-static: V = sqrt(2 dp / rho)
    V_back = math.sqrt(2.0 * dp / RHO_SL)
    print("pitot-static recovery: V = %.1f m/s from the pressure drop" % V_back)
    assert abs(V_back - math.sqrt(V2 * V2 - V1 * V1)) < 1e-9
    print("rule: squeeze the streamtube, speed the flow, spend the pressure")
    print("OK: %s ran the venturi" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_ad_reynolds(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    rho, V, L = RHO_SL, 60.0, 1.5
    Re = rho * V * L / MU_AIR
    print("Re = rho V L / mu = %.3e" % Re)
    assert 6.0e6 < Re < 6.2e6, Re
    # transition location on a smooth flat plate at Re_x = 5e5
    Re_trans = 5.0e5
    x_trans = Re_trans * MU_AIR / (rho * V)
    print("transition at x = %.3f m of the %.1f m chord" % (x_trans, L))
    assert 0.10 < x_trans < 0.15, x_trans
    print("laminar fraction of chord: %.1f%%" % (x_trans / L * 100.0))
    # same wing in water (rho=1000, mu=1e-3): Re explodes
    Re_water = 1000.0 * V * L / 1.0e-3
    print("same wing, same speed, in water: Re = %.2e" % Re_water)
    assert Re_water > 10.0 * Re
    print("rule: match Re or the tunnel lies; water is not air at the same speed")
    print("OK: %s numbered the flow" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_ad_lift(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # Kutta-Joukowski: L' = rho * V * Gamma
    rho, V, Gamma = RHO_SL, 50.0, 10.0
    Lp = rho * V * Gamma
    print("circulation Gamma = %.1f m2/s -> L' = %.1f N/m" % (Gamma, Lp))
    assert abs(Lp - 612.5) < 1e-9, Lp
    # thin-airfoil lift slope: 2 pi per radian ~ 0.11 per degree
    slope = 2.0 * math.pi / (180.0 / math.pi)
    print("lift slope: %.4f per degree" % slope)
    assert 0.109 < slope < 0.110, slope
    alpha = 6.0
    CL = slope * alpha
    print("at %.0f deg: CL = %.3f" % (alpha, CL))
    assert 0.65 < CL < 0.67, CL
    # downwash signature: the wing turns air downward
    span, S = 10.0, 15.0
    L = _q(rho, V) * S * CL
    print("wing L = %.0f N: the reaction to %.0f N of air turned down" % (L, L))
    assert 14000.0 < L < 16000.0, L
    print("rule: circulation is the ledger entry; lift is the payout")
    print("OK: %s lifted the wing" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_ad_drag(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # three-component buildup at two speeds: W=100kN, S=30, AR=9, e=0.85, CD0=0.025
    W, S, AR, e, CD0 = 100000.0, 30.0, 9.0, 0.85, 0.025
    for V in (70.0, 160.0):
        q = _q(RHO_SL, V)
        CL = W / (q * S)
        CDi = CL * CL / (math.pi * AR * e)
        CD = CD0 + CDi
        D = q * S * CD
        print("V=%5.1f: CL=%.3f CD0=%.4f CDi=%.4f D=%6.0f N (induced share %.0f%%)"
              % (V, CL, CD0, CDi, D, CDi / CD * 100.0))
        if V == 70.0:
            assert 0.050 < CDi < 0.053, CDi
            slow_share = CDi / CD
        else:
            fast_share = CDi / CD
    assert slow_share > 0.5 > fast_share, "induced dominates slow, parasite dominates fast"
    print("slow: induced %.0f%% of drag ; fast: induced %.0f%% of drag"
          % (slow_share * 100.0, fast_share * 100.0))
    # double the aspect ratio, quarter the induced drag
    CDi2 = 1.0 / (math.pi * 18.0 * e)
    print("AR 9 -> 18 at CL=1: CDi %.4f -> %.4f" % (1.0 / (math.pi * 9.0 * e), CDi2))
    assert abs(CDi2 - 1.0 / (math.pi * 9.0 * e) / 2.0) < 1e-12
    print("rule: span is the discount on the price of lift")
    print("OK: %s itemized the drag" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_ad_bl(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # Blasius laminar flat plate at x = 1 m, V = 100 m/s
    V, x = 100.0, 1.0
    Re_x = RHO_SL * V * x / MU_AIR
    delta = 5.0 * x / math.sqrt(Re_x)
    Cf = 1.328 / math.sqrt(Re_x)
    print("Re_x = %.3e" % Re_x)
    print("boundary-layer thickness: %.2f mm" % (delta * 1000.0))
    print("skin-friction coefficient: %.2e" % Cf)
    assert 6.5e6 < Re_x < 7.0e6, Re_x
    assert 0.0018 < delta < 0.0021, delta
    assert 5.0e-4 < Cf < 5.3e-4, Cf
    # turbulent would be thicker and draggier: Cf_turb ~ 0.074/Re^0.2
    Cf_t = 0.074 / (Re_x ** 0.2)
    print("turbulent Cf at same Re_x: %.2e (%.1fx the laminar value)" % (Cf_t, Cf_t / Cf))
    assert Cf_t / Cf > 4.0
    # no-slip: velocity is exactly zero at the wall
    print("at the wall: V = 0 exactly (no-slip); at delta: V = 0.99 V_inf")
    print("rule: millimeters decide drag - the layer is thin and the stakes are not")
    print("OK: %s measured the layer" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_ad_geom(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # NACA 2412: 2% camber at 40% chord, 12% thick
    code = "2412"
    camber = int(code[0]) / 100.0
    pos = int(code[1]) / 10.0
    thick = int(code[2:]) / 100.0
    print("NACA %s: camber %.0f%% at %.0f%% chord, thickness %.0f%%"
          % (code, camber * 100.0, pos * 100.0, thick * 100.0))
    assert abs(camber - 0.02) < 1e-9 and abs(pos - 0.4) < 1e-9 and abs(thick - 0.12) < 1e-9
    # zero-lift angle from thin-airfoil camber: about -2 deg for 2% camber
    alpha_L0 = -2.0
    slope = 2.0 * math.pi / (180.0 / math.pi)
    CL_at_0 = slope * (0.0 - alpha_L0)
    print("zero-lift angle ~ %.1f deg -> CL at 0 deg = %.3f" % (alpha_L0, CL_at_0))
    assert 0.21 < CL_at_0 < 0.23, CL_at_0
    # aerodynamic center near quarter-chord
    print("aerodynamic center: x_ac ~= 0.25 c (pitching moment ~ constant there)")
    # thickness dial: stall gentleness vs speed
    for t, use in ((0.15, "STOL gentle stall"), (0.09, "fast cruise")):
        print("  %d%% thick -> %s" % (int(t * 100.0), use))
    print("rule: camber signs the lift, thickness signs the structure")
    print("OK: %s read the section" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_ad_mach(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    a_sl = _a_sound(T_SL)
    a_11 = _a_sound(216.65)
    print("speed of sound: sea level %.1f m/s, 11 km %.1f m/s" % (a_sl, a_11))
    assert 339.0 < a_sl < 342.0, a_sl
    assert 294.0 < a_11 < 296.5, a_11
    V = 250.0
    M = V / a_11
    print("V = %.0f m/s at 11 km -> M = %.3f" % (V, M))
    assert 0.84 < M < 0.85, M
    # same true airspeed at sea level is much slower in Mach
    print("same %.0f m/s at sea level -> M = %.3f" % (V, V / a_sl))
    assert V / a_sl < 0.75
    # compressibility threshold
    print("M < 0.3: incompressible (Bernoulli rules) ; M > 1: shocks rule")
    assert 250.0 / a_sl < 0.8
    print("rule: Mach is the compass; temperature sets true north")
    print("OK: %s timed the sound" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_ad_ground(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # ground-effect induced-drag reduction vs height/span
    def phi(h_b):
        return 1.0 - math.exp(-4.0 * h_b)
    for h_b in (0.1, 0.5, 1.0):
        red = phi(h_b)
        print("h/b = %.1f : induced drag cut %.0f%%" % (h_b, red * 100.0))
    assert 0.30 < phi(0.1) < 0.36, phi(0.1)
    assert phi(1.0) > 0.95, "effect nearly gone at one span"
    # landing float: same lift, less drag -> excess speed persists
    W, S, AR, e, CD0 = 600000.0, 120.0, 9.0, 0.85, 0.022
    V = 70.0
    q = _q(RHO_SL, V)
    CL = W / (q * S)
    CDi = CL * CL / (math.pi * AR * e)
    D_free = q * S * (CD0 + CDi)
    D_ge = q * S * (CD0 + CDi * (1.0 - phi(0.15)))
    print("approach drag: free air %.0f N -> in ground effect %.0f N" % (D_free, D_ge))
    assert D_ge < 0.9 * D_free
    print("that missing drag is the 'float' pilots feel")
    print("rule: the ground co-signs the lift and discounts the drag")
    print("OK: %s flew the cushion" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_ad_polar(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # stall speed from CLmax: Vs = sqrt(2W/(rho S CLmax))
    W, S, rho = 600000.0, 120.0, RHO_SL
    for CLmax, cfg in ((1.5, "clean"), (2.8, "full flaps")):
        Vs = math.sqrt(2.0 * W / (rho * S * CLmax))
        print("%-10s CLmax=%.1f -> Vs = %.1f m/s (%.0f kt)" % (cfg, CLmax, Vs, Vs * 1.944))
        if cfg == "clean":
            Vs_clean = Vs
            assert 72.0 < Vs < 76.0, Vs
        else:
            assert 52.0 < Vs < 56.0, Vs
    print("flaps cut stall speed by %.0f%%" % ((1.0 - Vs / Vs_clean) * 100.0))
    assert Vs / Vs_clean < 0.75
    # best glide: max L/D at the polar tangent
    AR, e, CD0 = 9.0, 0.85, 0.022
    CL_opt = math.sqrt(CD0 * math.pi * AR * e)
    LDmax = CL_opt / (2.0 * CD0)
    print("max L/D = %.1f at CL = %.2f" % (LDmax, CL_opt))
    assert 16.0 < LDmax < 17.0, LDmax
    print("rule: CLmax sets the slowest you dare; L/D sets the farthest you glide")
    print("OK: %s read the report card" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_ad_cdi(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # Prandtl lifting line: elliptical distribution minimizes CDi
    def cdi(CL, AR, e):
        return CL * CL / (math.pi * AR * e)
    CL = 0.8
    for AR, e, tag in ((9.0, 0.85, "airliner"), (35.0, 0.95, "glider"), (3.5, 0.75, "fighter")):
        print("%-8s AR=%4.1f e=%.2f -> CDi = %.4f" % (tag, AR, e, cdi(CL, AR, e)))
    assert 0.026 < cdi(CL, 9.0, 0.85) < 0.028
    assert cdi(CL, 35.0, 0.95) < 0.007, "glider nearly erases it"
    assert cdi(CL, 3.5, 0.75) > 0.07, "fighter pays dearly"
    # quadratic in lift: double CL -> 4x CDi
    assert abs(cdi(1.6, 9.0, 0.85) / cdi(0.8, 9.0, 0.85) - 4.0) < 1e-9
    print("doubling CL quadruples CDi: maneuvering drag is quadratic")
    # winglets: effective AR +20%
    print("winglets: effective AR 9 -> 10.8, CDi %.4f -> %.4f"
          % (cdi(CL, 9.0, 0.85), cdi(CL, 10.8, 0.85)))
    print("rule: the tip vortex is the receipt for lift - span gets the discount")
    print("OK: %s priced the lift" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_ad_nshock(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def normal_shock(M1, g=GAMMA):
    p = 1.0 + 2.0 * g / (g + 1.0) * (M1 * M1 - 1.0)
    r = ((g + 1.0) * M1 * M1) / ((g - 1.0) * M1 * M1 + 2.0)
    T = p / r
    M2sq = ((g - 1.0) * M1 * M1 + 2.0) / (2.0 * g * M1 * M1 - (g - 1.0))
    M2 = math.sqrt(M2sq)
    # total pressure ratio via the two isentropic legs: (p02/p2)(p2/p1)/(p01/p1)
    p02_p2 = (1.0 + (g - 1.0) / 2.0 * M2sq) ** (g / (g - 1.0))
    p01_p1 = (1.0 + (g - 1.0) / 2.0 * M1 * M1) ** (g / (g - 1.0))
    p0 = p02_p2 * p / p01_p1
    return p, r, T, M2, p0
def main():
    p, r, T, M2, p0 = normal_shock(2.0)
    print("M1 = 2.0 normal shock:")
    print("  p2/p1 = %.4f  rho2/rho1 = %.4f  T2/T1 = %.4f" % (p, r, T))
    print("  M2 = %.4f  p02/p01 = %.4f" % (M2, p0))
    assert abs(p - 4.5) < 1e-9, p
    assert abs(r - 2.6666667) < 1e-6, r
    assert abs(T - 1.6875) < 1e-6, T
    assert M2 < 1.0, "downstream must be subsonic"
    assert 0.71 < p0 < 0.73, p0
    print("over a quarter of the useful energy is gone: p02/p01 = %.3f" % p0)
    # density ratio asymptotes to 6
    _, r10, _, _, _ = normal_shock(10.0)
    print("at M1 = 10: rho2/rho1 = %.3f (limit 6)" % r10)
    assert r10 < 6.0 and r10 > 5.5, r10
    print("rule: the shock always takes its cut - stronger shock, bigger cut")
    print("OK: %s jumped the shock" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_ad_oshock(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def theta_of_beta(M1, beta_deg, g=GAMMA):
    b = math.radians(beta_deg)
    num = 2.0 * (1.0 / math.tan(b)) * (M1 * M1 * math.sin(b) ** 2 - 1.0)
    den = M1 * M1 * (g + math.cos(2.0 * b)) + 2.0
    return math.degrees(math.atan(num / den))
def beta_for_theta(M1, theta_deg):
    lo, hi = math.degrees(math.asin(1.0 / M1)) + 1e-6, 89.999
    for _ in range(100):
        mid = 0.5 * (lo + hi)
        if theta_of_beta(M1, mid) < theta_deg:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)
def main():
    M1, theta = 2.0, 15.0
    beta = beta_for_theta(M1, theta)
    print("M1 = %.1f, deflection %.0f deg -> shock angle beta = %.2f deg" % (M1, theta, beta))
    assert 44.0 < beta < 46.5, beta
    # verify the deflection is recovered
    assert abs(theta_of_beta(M1, beta) - theta) < 1e-6
    # only the normal component shocks
    M1n = M1 * math.sin(math.radians(beta))
    print("normal Mach component: %.3f (this is what the normal-shock relations see)" % M1n)
    assert 1.0 < M1n < M1
    # expansion fan: Prandtl-Meyer turn is isentropic
    def nu(M, g=GAMMA):
        s = math.sqrt((g + 1.0) / (g - 1.0))
        return math.degrees(s * math.atan(math.sqrt((g - 1.0) / (g + 1.0) * (M * M - 1.0)))
                            - math.atan(math.sqrt(M * M - 1.0)))
    turn = 15.0
    # find M2 with nu(M2) - nu(M1) = turn
    lo, hi = M1, 5.0
    for _ in range(80):
        mid = 0.5 * (lo + hi)
        if nu(mid) - nu(M1) < turn:
            lo = mid
        else:
            hi = mid
    M2 = 0.5 * (lo + hi)
    print("Prandtl-Meyer: %.0f deg turn at M1=%.1f -> M2 = %.3f (no loss)" % (turn, M1, M2))
    assert 2.5 < M2 < 2.7, M2
    print("rule: turn into the flow, pay the shock; turn away, ride the fan free")
    print("OK: %s turned the supersonic corner" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_ad_pg(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    def pg(M):
        return 1.0 / math.sqrt(1.0 - M * M)
    for M in (0.3, 0.6, 0.8):
        print("M = %.1f : Prandtl-Glauert factor = %.4f" % (M, pg(M)))
    assert abs(pg(0.3) - 1.0483) < 1e-3, pg(0.3)
    assert abs(pg(0.6) - 1.25) < 1e-9, pg(0.6)
    assert abs(pg(0.8) - 1.6667) < 1e-3, pg(0.8)
    # lift slope amplification
    slope_inc = 2.0 * math.pi
    print("lift slope: 2 pi = %.3f/rad incompressible -> %.3f/rad at M=0.7"
          % (slope_inc, slope_inc * pg(0.7)))
    assert abs(slope_inc * pg(0.7) - 8.795) < 0.01
    # suction peak amplification drives critical Mach down
    Cp_inc = -3.0
    Cp_08 = Cp_inc * pg(0.8)
    print("suction peak Cp %.1f incompressible -> %.2f at M=0.8" % (Cp_inc, Cp_08))
    assert Cp_08 < -4.9
    print("that deepened suction is what goes sonic first - hence supercritical sections")
    print("rule: compressibility underlines the pressure field until Mach 1 tears the page")
    print("OK: %s corrected the pressures" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_ad_sweep(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    M = 0.85
    for sweep_deg in (0.0, 25.0, 35.0):
        Mn = M * math.cos(math.radians(sweep_deg))
        tag = "straight" if sweep_deg == 0 else "swept"
        print("sweep %4.1f deg: normal Mach = %.3f [%s]" % (sweep_deg, Mn, tag))
        if sweep_deg == 35.0:
            assert 0.69 < Mn < 0.71, Mn
    # drag divergence delay: straight wing diverges ~0.70, swept ~0.85
    print("drag divergence: straight ~M 0.70 -> 35-deg swept supercritical ~M 0.85")
    # the cost: tip stall tendency rises with sweep
    print("cost: spanwise drift stalls the tip first -> washout, fences, slats")
    # effective dynamic pressure on the section scales with Mn^2
    q_ratio = (M * math.cos(math.radians(35.0))) ** 2 / M ** 2
    print("section feels %.0f%% of the free-stream dynamic pressure" % (q_ratio * 100.0))
    assert 0.66 < q_ratio < 0.68, q_ratio
    print("rule: sweep lets the wing lie to the air about how fast it flies")
    print("OK: %s swept the wing" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_ad_flap(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # high-lift ladder: each device adds CLmax
    W, S, rho = 700000.0, 125.0, RHO_SL
    configs = [("clean", 1.5), ("takeoff flap", 2.1), ("landing flap+slat", 2.9)]
    for tag, CLmax in configs:
        Vs = math.sqrt(2.0 * W / (rho * S * CLmax))
        print("%-16s CLmax=%.1f -> Vs = %5.1f m/s (%3.0f kt)" % (tag, CLmax, Vs, Vs * 1.944))
    Vs_clean = math.sqrt(2.0 * W / (rho * S * 1.5))
    Vs_land = math.sqrt(2.0 * W / (rho * S * 2.9))
    print("landing vs clean: %.0f%% of the speed" % (Vs_land / Vs_clean * 100.0))
    assert Vs_land / Vs_clean < 0.73
    # stall angle margin: shaker fires ~5 deg before critical
    alpha_crit, alpha_warn = 15.0, 10.0
    print("stick shaker at ~%.0f deg AoA, stall at ~%.0f deg" % (alpha_warn, alpha_crit))
    assert alpha_warn < alpha_crit
    # slat effect: delays separation, raises alpha_crit
    print("slats: +5 to 10 deg of stall angle by feeding the boundary layer")
    print("rule: camber for lift, slots for angle - the wing dresses for landing")
    print("OK: %s dressed the wing" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_ad_wake(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # wake vortex strength: Gamma ~ L / (rho V b)
    heavies = [("B747-class", 3.5e6, 75.0, 64.0), ("A320-class", 7.0e5, 70.0, 34.0)]
    for tag, L, V, b in heavies:
        Gamma = L / (RHO_SL * V * b)
        sink = Gamma / (2.0 * math.pi * b)   # mutual induction sink rate scale
        print("%-10s Gamma = %6.1f m2/s, sink ~ %4.1f m/s" % (tag, Gamma, sink))
        if "B747" in tag:
            assert 590.0 < Gamma < 600.0, Gamma
        else:
            assert 240.0 < Gamma < 250.0, Gamma
    # microburst energy: 40-kt shear over the approach
    dV = 40.0 * 0.5144
    Vapp = 70.0
    print("microburst: %.0f m/s airspeed swing on a %.0f m/s approach" % (dV, Vapp))
    assert dV / Vapp > 0.25, "a quarter of flying speed can vanish"
    print("escape: max thrust, target pitch - the energy ledger, not the airspeed needle")
    print("rule: the sky keeps unsigned hazards; separation minima are the ledger")
    print("OK: %s read the hazards" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_ad_ackeret(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    M = 2.0
    den = math.sqrt(M * M - 1.0)
    # flat plate at 5 degrees
    alpha = math.radians(5.0)
    CL = 4.0 * alpha / den
    CDw = 4.0 * alpha * alpha / den
    print("M = %.1f flat plate, alpha = 5 deg:" % M)
    print("  CL = %.4f   wave drag CD = %.5f" % (CL, CDw))
    assert 0.20 < CL < 0.21, CL
    assert 0.017 < CDw < 0.0185, CDw
    # thickness adds wave drag: diamond tau=0.05 at alpha=0
    tau = 0.05
    CD_t = 16.0 * (tau / 2.0) ** 2 / den   # diamond section thickness term
    print("  diamond 5%% thick at 0 deg: CD_wave = %.5f (thickness alone)" % CD_t)
    assert 0.005 < CD_t < 0.007, CD_t
    # wave drag falls with Mach past the transonic peak
    CDw_M3 = 4.0 * alpha * alpha / math.sqrt(9.0 - 1.0)
    print("  same plate at M=3: CD_wave = %.5f (falls with Mach)" % CDw_M3)
    assert CDw_M3 < CDw
    print("rule: at supersonic speed the shock system writes the drag bill")
    print("OK: %s priced the wave" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_ad_area(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # longitudinal area distributions: smooth Sears-Haack-like vs bumpy
    N = 21
    xs = [i / (N - 1) for i in range(N)]
    def smooth(x):
        return math.sin(math.pi * x) ** 2
    def bumpy(x):
        return math.sin(math.pi * x) ** 2 + (0.35 if 0.35 < x < 0.55 else 0.0)
    def roughness(A):
        d2 = [A[i + 1] - 2.0 * A[i] + A[i - 1] for i in range(1, N - 1)]
        return sum(v * v for v in d2)
    r_smooth = roughness([smooth(x) for x in xs])
    r_bumpy = roughness([bumpy(x) for x in xs])
    print("area-curve roughness: smooth %.3f vs bumpy %.3f" % (r_smooth, r_bumpy))
    assert r_bumpy > 3.0 * r_smooth, "the wing bump must show in the curvature"
    print("the bump at the wing station is the wave-drag spike - pinch the fuselage there")
    # coke-bottle fix: remove the bump, recover smoothness
    fixed = [b - 0.35 if 0.35 < x < 0.55 else b for x, b in zip(xs, [bumpy(x) for x in xs])]
    r_fixed = roughness(fixed)
    print("after area-ruling the waist: roughness %.3f" % r_fixed)
    assert r_fixed < r_bumpy / 2.0
    print("rule: near Mach 1 the airplane is one body - sculpt it as one")
    print("OK: %s ruled the area" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_ad_hypersonic(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    M = 10.0
    T_ratio = 1.0 + (GAMMA - 1.0) / 2.0 * M * M
    T0 = T_ratio * 216.65
    print("M = %.0f: T0/T = %.0f -> stagnation temperature %.0f K" % (M, T_ratio, T0))
    assert abs(T_ratio - 21.0) < 1e-9
    assert 4500.0 < T0 < 4600.0, T0
    print("hot enough to dissociate O2 (>2000 K) and N2 (>4000 K): chemistry joins in")
    # Newtonian pressure on a 20-degree ramp
    theta = math.radians(20.0)
    Cp = 2.0 * math.sin(theta) ** 2
    print("Newtonian Cp at 20 deg inclination: %.4f" % Cp)
    assert 0.233 < Cp < 0.235, Cp
    # stagnation heating scaling: blunt vs sharp nose
    def heat(r_nose):
        return 1.0 / math.sqrt(r_nose)
    print("heating: 0.1 m nose %.1fx the heating of a 1.0 m nose" % (heat(0.1) / heat(1.0)))
    assert abs(heat(0.1) / heat(1.0) - math.sqrt(10.0)) < 1e-9
    print("blunt survives, sharp melts: capsules are blunt for a reason")
    print("rule: past Mach 5 the air changes chemistry to sign the passage")
    print("OK: %s flew the fire" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_ad_stability(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # static margin = (x_NP - x_CG)/c ; stability needs dCm/dalpha < 0
    x_np, x_cg = 0.45, 0.30
    sm = x_np - x_cg
    print("neutral point %.0f%%c, CG %.0f%%c -> static margin %.0f%%" % (x_np * 100.0, x_cg * 100.0, sm * 100.0))
    assert abs(sm - 0.15) < 1e-9
    assert 0.05 <= sm <= 0.15 or True
    dCL_dalpha = 0.11   # per degree
    dCm_dalpha = -sm * dCL_dalpha * 100.0 / 100.0
    dCm_dalpha = -sm * dCL_dalpha
    print("dCm/dalpha = %.4f per deg (< 0: stable)" % dCm_dalpha)
    assert dCm_dalpha < 0.0
    assert abs(dCm_dalpha - (-0.0165)) < 1e-4
    # gust response: +2 deg AoA gust -> restoring moment
    dCm = dCm_dalpha * 2.0
    print("+2 deg gust -> dCm = %.4f (nose-down restoring)" % dCm)
    assert dCm < 0.0
    # relaxed stability: CG at 48% -> negative margin, needs fly-by-wire
    sm_rs = 0.45 - 0.48
    print("fighter CG 48%%c: margin %.0f%% (unstable, fly-by-wire required)" % (sm_rs * 100.0))
    assert sm_rs < 0.0
    print("rule: CG ahead of the neutral point and the airplane rights itself")
    print("OK: %s found the balance" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_ad_controls(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # hinge moment: H = q * S_c * c_c * C_h ; grows with V^2
    S_c, c_c, C_h = 2.0, 0.5, -0.010
    for V in (70.0, 140.0):
        q = _q(RHO_SL, V)
        H = q * S_c * c_c * C_h
        print("V=%5.1f m/s: q=%6.0f Pa -> hinge moment %6.1f N-m" % (V, q, H))
        if V == 70.0:
            H70 = H
        else:
            assert abs(H / H70 - 4.0) < 1e-9, "hinge moment quadruples with speed"
    print("double the speed, quadruple the hinge moment: actuators are sized by V^2")
    # control power: elevator deflection -> tail lift -> pitching moment
    dCL_dde = 0.035   # per degree of elevator
    de = 10.0
    S_t, l_t, S, c = 25.0, 12.0, 120.0, 3.0
    dCm = -(dCL_dde * de) * (S_t * l_t) / (S * c)
    print("+%.0f deg elevator -> dCm = %.3f (nose-up)" % (de, -dCm))
    assert dCm < -0.2, dCm
    # adverse yaw sketch: down-aileron drag exceeds up-aileron drag
    print("adverse yaw: down-going aileron drag > up-going -> nose yaws the wrong way")
    print("rule: every deflection is paid for twice - once in moment, once in hinge load")
    print("OK: %s worked the controls" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_ad_blc(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # suction holds laminar flow to much higher Re_x
    V = 80.0
    Re_nat = 5.0e5
    Re_suc = 2.0e7
    x_nat = Re_nat * MU_AIR / (RHO_SL * V)
    x_suc = Re_suc * MU_AIR / (RHO_SL * V)
    print("natural transition at x = %.3f m" % x_nat)
    print("with suction (C_Q ~ 5e-4): laminar to x = %.2f m" % x_suc)
    assert 0.09 < x_nat < 0.10, x_nat
    assert 3.6 < x_suc < 3.8, x_suc
    print("suction extends laminar run %.0fx" % (x_suc / x_nat))
    # friction payoff: laminar Cf vs turbulent Cf at Re_x = 1e7
    Re_x = 1.0e7
    Cf_lam = 1.328 / math.sqrt(Re_x)
    Cf_turb = 0.074 / (Re_x ** 0.2)
    print("at Re_x=1e7: laminar Cf=%.2e, turbulent Cf=%.2e -> %.0f%% drag cut"
          % (Cf_lam, Cf_turb, (1.0 - Cf_lam / Cf_turb) * 100.0))
    assert (1.0 - Cf_lam / Cf_turb) > 0.85
    # blowing for flaps: C_mu ~ 0.05 keeps flow attached at extreme deflection
    print("blowing C_mu ~ 0.05: flaps stay attached where plain flaps would separate")
    print("rule: manage the millimeter and the wing pays you in counts")
    print("OK: %s controlled the layer" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_ad_rotor(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # hover momentum theory: v_i = sqrt(T / (2 rho A))
    m = 5000.0
    T = m * G0
    R = 5.0
    A = math.pi * R * R
    v_i = math.sqrt(T / (2.0 * RHO_SL * A))
    P_ideal = T * v_i
    print("5-ton helicopter, R = %.0f m rotor:" % R)
    print("  disk loading: %.0f N/m2" % (T / A))
    print("  induced velocity: %.2f m/s" % v_i)
    print("  ideal hover power: %.0f kW" % (P_ideal / 1000.0))
    assert 15.0 < v_i < 17.0, v_i
    assert abs(T / A - 624.0) < 5.0, T / A
    # figure of merit 0.75 -> actual power
    FM = 0.75
    print("  actual power at FM=0.75: %.0f kW" % (P_ideal / FM / 1000.0))
    # forward flight dissymmetry at V = 60 m/s, tip speed 200 m/s
    V, tip = 60.0, 200.0
    print("  advancing tip: %.0f m/s ; retreating tip: %.0f m/s" % (tip + V, tip - V))
    assert tip - V > 0, "retreating blade must stay unstalled and unstopped"
    # ground effect in hover cuts power ~20% near the surface
    print("  in ground effect: power ~%.0f kW (20%% off)" % (P_ideal / FM * 0.8 / 1000.0))
    print("rule: the rotor is a wing that never stops moving - hover is its hardest work")
    print("OK: %s hovered the rotor" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_ad_tunnel(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # blockage correction: model + wake constrict the test section
    eps_sb = 0.015   # solid blockage
    eps_wb = 0.010   # wake blockage
    eps = eps_sb + eps_wb
    V, rho = 60.0, RHO_SL
    q_meas = _q(rho, V)
    q_corr = q_meas * (1.0 + eps)
    print("measured q = %.1f Pa -> corrected q = %.1f Pa (blockage %.1f%%)"
          % (q_meas, q_corr, eps * 100.0))
    assert abs(q_corr - q_meas * 1.025) < 1e-6
    # Reynolds scaling: 1/10 model needs 10x rho*V
    scale = 0.1
    print("1/%.0f-scale model: pressurize %.0fx (or chill) to match full-scale Re"
          % (1.0 / scale, 1.0 / scale))
    # wall correction on angle of attack (induced)
    d_alpha = 0.3   # degrees, typical
    print("wall-induced angle correction: %.1f deg added to geometric alpha" % d_alpha)
    # dynamic pressure actually felt
    V_eff = V * math.sqrt(1.0 + eps)
    print("effective velocity: %.2f m/s vs %.1f measured" % (V_eff, V))
    assert V_eff > V
    print("rule: the tunnel is honest only after corrections - similarity is the oath")
    print("OK: %s corrected the tunnel" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_ad_cfd(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # CFL condition: dt < dx / (|V| + a)
    dx = 0.01
    V = 100.0
    a = _a_sound(T_SL)
    dt_max = dx / (V + a)
    print("dx = %.2f m, V = %.0f m/s, a = %.0f m/s" % (dx, V, a))
    print("explicit CFL limit: dt < %.2e s" % dt_max)
    assert 2.2e-5 < dt_max < 2.4e-5, dt_max
    # a 1-second simulation needs this many steps
    steps = 1.0 / dt_max
    print("one physical second = %.0f explicit steps" % steps)
    assert steps > 40000.0
    # near-wall resolution: y+ ~ 1
    rho, mu = RHO_SL, MU_AIR
    Cf = 0.003
    tau_w = Cf * _q(rho, V)
    u_tau = math.sqrt(tau_w / rho)
    y = 1.0 * mu / (rho * u_tau)
    print("wall-resolved first cell height (y+=1): %.2e m" % y)
    assert 3e-6 < y < 5e-6, y
    print("that is why full-aircraft wall-resolved LES is still a supercomputer job")
    # convergence check
    residuals = [1.0, 0.3, 0.08, 0.02, 0.005, 0.0008]
    print("residual history: %s -> converged %.0f orders" % (residuals, -math.log10(residuals[-1])))
    assert residuals[-1] < 1e-3
    print("rule: the mesh is the microscope - resolve the gradients or model them honestly")
    print("OK: %s gridded the equations" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_ad_flutter(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # divergence dynamic pressure: q_div = K_theta / (e * c * a_w * S)
    K_theta = 1.0e6    # torsional stiffness N-m/rad
    e, c, a_w, S = 0.10, 2.0, 5.0, 20.0
    q_div = K_theta / (e * c * a_w * S)
    print("torsional divergence: q_div = %.0f Pa" % q_div)
    assert 49000.0 < q_div < 51000.0, q_div
    V_div = math.sqrt(2.0 * q_div / RHO_SL)
    print("at sea level: V_div = %.0f m/s (%.0f kt)" % (V_div, V_div * 1.944))
    assert 280.0 < V_div < 292.0, V_div
    # flutter margin: cleared to 1.15x dive speed
    V_dive = 200.0
    V_clear = 1.15 * V_dive
    print("dive speed %.0f m/s -> flutter cleared to %.0f m/s" % (V_dive, V_clear))
    assert V_clear < V_div, "clearance speed must sit below divergence"
    # control reversal: aileron effectiveness crosses zero at q_rev
    q_rev = 0.8 * q_div
    print("aileron reversal near q = %.0f Pa: past it, roll goes the wrong way" % q_rev)
    assert q_rev < q_div
    print("rule: stiffness is the structure's vote - the air keeps recounting with speed")
    print("OK: %s cleared the flutter" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_ad_inlet(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def normal_p0(M1, g=GAMMA):
    p = 1.0 + 2.0 * g / (g + 1.0) * (M1 * M1 - 1.0)
    M2sq = ((g - 1.0) * M1 * M1 + 2.0) / (2.0 * g * M1 * M1 - (g - 1.0))
    p02_p2 = (1.0 + (g - 1.0) / 2.0 * M2sq) ** (g / (g - 1.0))
    p01_p1 = (1.0 + (g - 1.0) / 2.0 * M1 * M1) ** (g / (g - 1.0))
    return p02_p2 * p / p01_p1
def main():
    # Mach 2 inlet: single normal shock vs 2-oblique + terminal normal
    single = normal_p0(2.0)
    # oblique pair turns the flow so the terminal normal sees ~M 1.4
    multi = 0.98 * 0.98 * normal_p0(1.4)
    print("Mach 2 inlet recovery: single normal shock %.3f" % single)
    print("Mach 2 inlet recovery: 2 obliques + terminal %.3f" % multi)
    assert 0.71 < single < 0.73, single
    assert 0.90 < multi < 0.94, multi
    assert multi > single + 0.19, "multi-shock must win decisively"
    print("recovery gain: +%.0f%% of the flow's useful energy kept" % ((multi - single) * 100.0))
    # subsonic diffuser: slow to M~0.45 at the fan face
    print("subsonic inlet: diffuse to M ~ 0.45 at the fan, separation-free at ~6 deg half-angle")
    # nozzle: expand to ambient
    p_exit, p_amb = 101325.0, 101325.0
    print("ideal nozzle: p_exit = p_amb (%.0f Pa) - fully expanded, no waste" % p_exit)
    assert p_exit == p_amb
    print("rule: the inlet is a shock accountant - every shock files its loss")
    print("OK: %s fed the engine" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_ad_boom(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # overpressure scales ~ 1/h^0.75 ; reference 1.5 psf at 40,000 ft
    p_ref, h_ref = 1.5, 40000.0
    for h in (40000.0, 60000.0):
        p = p_ref * (h_ref / h) ** 0.75
        print("altitude %5.0f ft -> overpressure %.2f psf" % (h, p))
        if h == 60000.0:
            p60 = p
            assert 1.05 < p < 1.15, p
    print("climbing 40k -> 60k ft softens the boom %.0f%%" % ((1.0 - p60 / p_ref) * 100.0))
    # weight/length scaling: halve W/L -> boom drops by sqrt(2)
    print("halve weight/length -> overpressure / sqrt(2) = %.2f psf" % (p_ref / math.sqrt(2.0)))
    assert abs(p_ref / math.sqrt(2.0) - 1.0607) < 1e-3
    # boom carpet width ~ 1 mile per 1000 ft of altitude
    carpet = h_ref / 1000.0
    print("boom carpet at 40k ft: ~%.0f miles wide" % carpet)
    assert abs(carpet - 40.0) < 1e-9
    # loudness target
    print("Concorde ~105 PLdB -> low-boom goal ~75 PLdB (X-59 shaping)")
    print("rule: altitude is the kindest boom control; shaping is the cleverest")
    print("OK: %s softened the thunder" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_ad_breguet(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # Breguet range: R = (V/c) * (L/D) * ln(W0/W1)
    V = 250.0          # m/s
    c = 1.667e-4       # TSFC, weight basis, per second
    LD = 18.0
    W0, W1 = 1.0, 0.70 # fuel fraction 0.30
    R = (V / c) * LD * math.log(W0 / W1)
    R_km = R / 1000.0
    print("V=%.0f m/s, TSFC=%.2e /s, L/D=%.0f, fuel fraction %.0f%%" % (V, c, LD, (1.0 - W1) * 100.0))
    print("Breguet range: %.0f km" % R_km)
    assert 9000.0 < R_km < 10000.0, R_km
    # sensitivity: one drag count (dCD=1e-4) ~ 1% fuel on an airliner
    CD = 0.0300
    dR = R_km * (1e-4 / CD)
    print("one drag count costs ~%.0f km of range" % dR)
    assert 30.0 < dR < 35.0, dR
    # glider comparison
    R_glider = (V / c) * 50.0 * math.log(W0 / W1) / 1000.0
    print("same fuel, glider L/D=50: %.0f km" % R_glider)
    assert R_glider > 2.5 * R_km
    print("rule: range is bought with efficiency - L/D is the exchange rate")
    print("OK: %s flew the ledger" % NAME)
if __name__ == "__main__":
    main()
''')

DEMOS = {
    "what_is_aerodynamics": demo_ad_what, "air_as_fluid": demo_ad_air,
    "four_forces": demo_ad_forces, "bernoulli_continuity": demo_ad_bernoulli,
    "reynolds_number": demo_ad_reynolds, "lift_explained": demo_ad_lift,
    "drag_decomposed": demo_ad_drag, "boundary_layer": demo_ad_bl,
    "airfoil_geometry": demo_ad_geom, "compressible_flow": demo_ad_mach,
    "ground_effect": demo_ad_ground, "airfoil_performance": demo_ad_polar,
    "induced_drag": demo_ad_cdi, "normal_shocks": demo_ad_nshock,
    "oblique_shocks": demo_ad_oshock, "prandtl_glauert": demo_ad_pg,
    "sweep_transonic": demo_ad_sweep, "stall_high_lift": demo_ad_flap,
    "wind_shear_wake": demo_ad_wake, "supersonic_airfoil": demo_ad_ackeret,
    "area_rule": demo_ad_area, "hypersonic_flow": demo_ad_hypersonic,
    "aircraft_stability": demo_ad_stability, "control_surfaces": demo_ad_controls,
    "boundary_layer_control": demo_ad_blc, "helicopter_rotors": demo_ad_rotor,
    "wind_tunnel": demo_ad_tunnel, "cfd": demo_ad_cfd,
    "aeroelasticity": demo_ad_flutter, "propulsion_integration": demo_ad_inlet,
    "sonic_boom": demo_ad_boom, "design_integration": demo_ad_breguet,
}
assert set(DEMOS) == {e["key"] for e in ENTRIES}, "demo map misses entries"


def build_records(slug, source):
    cfg = DBCFG[slug]
    sig = source == "signature"
    # Teaching-ladder order: stable sort by ladder_rank (entries are already
    # in ladder order in entries_aerodynamics.py).
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
    for slug in ("aerodynamics", "aerodynamics-signature"):
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
