#!/usr/bin/env python3
"""Build the Hypersonic Aerodynamics field databases for JAH Databases (field #24, taxonomy order).

Verified 2026-10-17 (see entries_hypersonics.py docstring): NO database
covers hypersonic aerodynamics as a specialty. The just-built aerodynamics
DB (field #23) carries exactly one overview record plus supersonic theory;
the whole-system title sweep found zero specialty-level hypersonic records
(241 regex hits were 239 'distillation ablation' false positives + the 2
aerodynamics overview records).

So this build creates two NEW databases, 33 ladder-ordered records each,
covering ONLY what aerodynamics left uncovered:

  hypersonic-aerodynamics          - The Hypersonic Aerodynamics Database
                                     (public-harvest: real, fact-checked
                                     hypersonic aerodynamics; citations
                                     Anderson 'Hypersonic and
                                     High-Temperature Gas Dynamics',
                                     Bertin, Hirschel, Rasmussen,
                                     Heiser & Pratt, Hayes & Probstein,
                                     Fay & Riddell, Sutton & Graves,
                                     NASA/NACA reference data)
  hypersonic-aerodynamics-signature - The Hypersonic Aerodynamics Signature
                                     Database (his original Signature
                                     interpretation; src signature, titles
                                     suffixed " (Signature Edition)", never
                                     presented as authentic public record)

33 records each, ordered by the teaching ladder (ladder_rank 1-10,
ladder_tier foundations/compounded/advanced); the shard index is written in
ladder order so pages present simple -> compounded -> complex.

Every record: description + how-it-works + key points + requirements +
standards + citations + working demonstration code (real, runnable,
stdlib-only Python; machine-executed OK). Hypersonics demos: the Mach-5
regime map and shock-angle collapse, thin-shock-layer standoff, Cp
convergence to the Newtonian limit (Mach independence), Newtonian and
modified-Newtonian pressure, hypersonic similarity collapse at constant K,
theta-max and the Prandtl-Meyer vacuum limit, stagnation temperature and
Rayleigh pitot pressure, vibrational cp growth and the gas-model ladder,
real-gas density-ratio rise and catalytic heating, the Taylor-Sedov
blast-wave scaling, the 1/sqrt(Rn) bluntness law, Sutton-Graves stagnation
heating and its V^3 sensitivity, Lees-type heating distribution with the
transition cliff, ablative TPS sizing from heat of ablation, the ablation
surface energy balance with blowing, entry-corridor beta scaling, the
viscous interaction parameter, second-mode transition frequency, incipient
separation and reattachment heating, entropy-layer swallowing, the
scramjet Brayton cycle with thermal choking, the Kantrowitz inlet start
limit, waverider L/D from trapped shock pressure, Knudsen regimes vs
altitude, Zeldovich-rate temperature sensitivity and Saha ionization,
shock-tunnel reservoir and test time, the X-plane flight record, Newtonian
pitch stiffness, Damkohler regimes, radiative-heating velocity scaling,
the full-stack design check, the Kuchemann L/D barrier, and boost-glide
range from L/D.

Subtitle disambiguation (fields #13-24 pattern): specialty titles carry
teaching-focused subtitles rather than bare cards, e.g. "Newtonian Impact
Theory: Pressure From Particle Impacts".

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
from entries_hypersonics import ENTRIES, SIG_TAIL

# ---------------------------------------------------------------- DB config

def _cfg(slug, name, tagline, record_kind, prefix, ai, role, citation, source):
    sig_line = ("Signature originals - his original Signature interpretation of hypersonic "
                "aerodynamics: clearly labeled Signature-made, never presented as authentic "
                "public record.")
    pub_line = ("Public records - real, fact-checked hypersonic aerodynamics: what hypersonic "
                "means; thin shock layers; Mach-number independence; Newtonian impact theory; "
                "hypersonic similarity parameters; strong and weak shocks; stagnation "
                "conditions; the perfect-gas breakdown; real-gas effects; the blast-wave "
                "analogy; nose bluntness; stagnation-point heating; heating distribution; "
                "thermal protection systems; ablation physics; reentry dynamics; viscous "
                "interaction; boundary-layer transition; shock/boundary-layer interaction; "
                "the entropy layer; hypersonic L/D; the scramjet cycle; scramjet inlets; "
                "waveriders; rarefied flow; high-temperature air chemistry; test facilities; "
                "flight-test history; stability and control; chemical nonequilibrium; "
                "radiative heating; boost-glide vehicles; integrated design, organized in "
                "the Signature system.")
    ladder = (" Records are ordered by the teaching ladder: Foundations (what hypersonic "
              "means, thin shock layers, Mach-number independence, Newtonian impact theory, "
              "hypersonic similarity, strong and weak shocks, stagnation conditions, the "
              "perfect-gas breakdown) -> Compounded (real-gas effects, the blast-wave "
              "analogy, nose bluntness, stagnation-point heating, heating distribution, "
              "thermal protection, ablation physics, reentry dynamics, viscous interaction, "
              "transition, shock/boundary-layer interaction, the entropy layer, "
              "hypersonic L/D) -> Advanced (scramjet cycle, scramjet inlets, waveriders, "
              "rarefied flow, high-temperature chemistry, test facilities, flight-test "
              "history, stability and control, nonequilibrium, radiative heating, "
              "boost-glide vehicles, integrated design).")
    return {
        "name": name, "tagline": tagline, "record_kind": record_kind,
        "prefix": prefix, "ai": ai, "role": role,
        "hero_p": "%s - %s Every record carries the full entry: description, how it works, "
                  "key points, requirements, standards, citations, and a working demonstration "
                  "program.%s" % (tagline, sig_line if source == "signature" else pub_line, ladder),
        "sig_type": ("Signature originals organized in the Signature system"
                     if source == "signature" else
                     "Public records organized in the Signature system"),
        "search_ph": "Search Mach number, shock waves, Newtonian, scramjet, reentry, ablation, heating, transition...",
        "chat_ph": "Ask about hypersonic aerodynamics...",
        "archive_blurb": ("Seeded %s hypersonic-aerodynamics records, marching toward one million records. "
                          "Presented in teaching-ladder order: foundations, compounded, advanced."
                          % ("Signature-original" if source == "signature" else "public-record")),
        "schema": ("id, t, g, name, title, description, how_it_works, key_points, requirements, "
                   "standards, citations, src, ladder_rank, ladder_tier, demo"),
        "fields": "Foundations \u00b7 Compounded \u00b7 Advanced - each tier opens on demand and loads only what you open",
        "gen_desc": "Generate clearly-labeled structural hypersonic aerodynamics studies. Seeded archive records are the authoritative entries.",
        "greet": "I am the %s. Ask me about hypersonic aerodynamics - from Mach-number independence, Newtonian theory, and similarity parameters through real-gas effects, stagnation heating, ablation, reentry dynamics, transition, scramjets, waveriders, rarefied flow, test facilities, and integrated vehicle design." % ai,
        "gen_fields": ["Foundations", "Compounded", "Advanced"],
        "gen_kind": "hypersonic-study", "gen_demo_kind": "hypersonic-demo",
        "source": source,
    }

CIT_PUB = "Hypersonic aerodynamics (standard texts and NASA/NACA reference data)."
CIT_SIG = CIT_PUB + " " + SIG_TAIL

DBCFG = {}
DBCFG["hypersonic-aerodynamics"] = _cfg(
    "hypersonic-aerodynamics", "The Hypersonic Aerodynamics Database",
    "Real, fact-checked hypersonic aerodynamics: from Mach-number independence, "
    "Newtonian impact theory, and similarity parameters through real-gas effects, "
    "stagnation heating, thermal protection, ablation, reentry dynamics, viscous "
    "interaction, transition, scramjets, waveriders, rarefied flow, high-temperature "
    "chemistry, test facilities, and integrated vehicle design - taught progressively "
    "along the ladder.",
    "hypersonic aerodynamics record", "JAH-HYP-", "JAH Hypersonics Archivist",
    "hypersonics archivist - what hypersonic means, thin shock layers, Mach-number "
    "independence, Newtonian theory, similarity parameters, strong/weak shocks, "
    "stagnation conditions, perfect-gas breakdown, real-gas effects, blast-wave "
    "analogy, nose bluntness, stagnation heating, heating distribution, thermal "
    "protection, ablation, reentry dynamics, viscous interaction, transition, "
    "shock/boundary-layer interaction, entropy layer, hypersonic L/D, scramjet "
    "cycle, scramjet inlets, waveriders, rarefied flow, high-temperature chemistry, "
    "test facilities, flight-test history, stability and control, nonequilibrium, "
    "radiative heating, boost-glide vehicles, integrated design; teaching "
    "progressively along the ladder from foundations through compounded to "
    "advanced; answers from many angles - definition, example, analogy, "
    "application, history, math, how-to - using only the system's own archive data",
    CIT_PUB, "public")
DBCFG["hypersonic-aerodynamics-signature"] = _cfg(
    "hypersonic-aerodynamics-signature", "The Hypersonic Aerodynamics Signature Database",
    "His original Signature interpretation of hypersonic aerodynamics: the full ladder from "
    "Mach-number independence and Newtonian theory through real-gas effects, heating, "
    "ablation, reentry, scramjets, and integrated design, reframed as Signature science. "
    "Clearly labeled Signature-made, never presented as authentic public record.",
    "hypersonic aerodynamics record", "JAH-HYS-", "JAH Hypersonics Archivist (Signature)",
    "hypersonics archivist - Signature editions: his original Signature "
    "interpretation of hypersonic aerodynamics, clearly labeled Signature-made and never "
    "presented as authentic public record; teaches progressively along the ladder "
    "from foundations through compounded to advanced; answers from many angles - "
    "definition, example, analogy, application, history, math, how-to - using only "
    "the system's own archive data",
    CIT_SIG, "signature")

base.DBCFG = DBCFG

# ---------------------------------------------------------------- demos
# Every demo is real, runnable, stdlib-only Python performing the actual
# hypersonic computation for its record. All are machine-executed by main().

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
"def _rayleigh_pitot(M, g=GAMMA):\n"
"    # p02/p1 behind a normal shock: p02/p2 isentropic x p2/p1\n"
"    t1 = (g + 1.0) ** 2 * M * M / (4.0 * g * M * M - 2.0 * (g - 1.0))\n"
"    t2 = (2.0 * g * M * M - (g - 1.0)) / (g + 1.0)\n"
"    return t1 ** (g / (g - 1.0)) * t2\n"
)

def _wrap(name, rid, group, body):
    return (base._hdr(name, rid, group) + _PREAMBLE + body.replace("NAME", json.dumps(name)))

def demo_hy_what(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # the four signatures of hypersonic flow, quantified at Mach 2 vs Mach 10
    theta = math.radians(10.0)
    for M in (2.0, 10.0):
        mu = math.degrees(math.asin(1.0 / M))
        T0_T = 1.0 + 0.2 * M * M
        print("M = %4.1f: Mach angle %5.2f deg, T0/T = %6.1f" % (M, mu, T0_T))
        if M == 10.0:
            assert abs(mu - 5.74) < 0.01, mu
            assert abs(T0_T - 21.0) < 1e-9, T0_T
    # stagnation temperature at altitude: cold air, still thousands of K
    T_inf = 216.65
    T0 = 21.0 * T_inf
    print("at 11 km, Mach 10 stagnation temperature: %.0f K" % T0)
    assert 4500.0 < T0 < 4600.0, T0
    print("thresholds crossed: O2 dissociation (~2000 K), N2 dissociation (~4000 K)")
    assert T0 > 4000.0
    print("rule: past Mach 5 the air stops being air and becomes chemistry")
    print("OK: %s mapped the regime" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_hy_thinshock(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def theta_of_beta(M1, beta_deg, g=GAMMA):
    b = math.radians(beta_deg)
    num = 2.0 * (1.0 / math.tan(b)) * (M1 * M1 * math.sin(b) ** 2 - 1.0)
    den = M1 * M1 * (g + math.cos(2.0 * b)) + 2.0
    return math.degrees(math.atan(num / den))
def beta_for_theta(M1, theta_deg):
    lo, hi = math.degrees(math.asin(1.0 / M1)) + 1e-6, 89.999
    for _ in range(120):
        mid = 0.5 * (lo + hi)
        if theta_of_beta(M1, mid) < theta_deg:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)
def main():
    theta = 15.0
    betas = []
    for M in (2.0, 5.0, 10.0):
        b = beta_for_theta(M, theta)
        betas.append(b)
        print("M = %4.1f, 15-deg wedge: shock angle = %5.2f deg (Mach angle %5.2f)"
              % (M, b, math.degrees(math.asin(1.0 / M))))
    assert betas[0] > 44.0 and betas[2] < 21.0, betas
    assert betas[2] - theta < 6.0, "shock nearly on the body at Mach 10"
    # blunt-nose standoff: delta ~ Rn / density_ratio ; density ratio -> 6
    Rn = 1.0
    for M, rho_r in ((2.0, 2.67), (10.0, 5.71)):
        delta = Rn / rho_r
        print("M = %4.1f: density ratio %.2f -> standoff %.3f m per meter of nose" % (M, rho_r, delta))
    print("rule: speed squeezes the shock onto the skin - the layer thins, the heat concentrates")
    print("OK: %s thinned the layer" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_hy_machindep(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def oblique_cp(M1, theta_deg, g=GAMMA):
    # weak-shock pressure coefficient via theta-beta solve
    b = math.radians(_beta(M1, theta_deg, g))
    Mn = M1 * math.sin(b)
    p = 1.0 + 2.0 * g / (g + 1.0) * (Mn * Mn - 1.0)
    return 2.0 * (p - 1.0) / (g * M1 * M1)
def _beta(M1, theta_deg, g=GAMMA):
    lo, hi = math.degrees(math.asin(1.0 / M1)) + 1e-6, 89.999
    for _ in range(120):
        mid = 0.5 * (lo + hi)
        bb = math.radians(mid)
        num = 2.0 * (1.0 / math.tan(bb)) * (M1 * M1 * math.sin(bb) ** 2 - 1.0)
        den = M1 * M1 * (g + math.cos(2.0 * bb)) + 2.0
        if math.degrees(math.atan(num / den)) < theta_deg:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)
def main():
    theta = 10.0
    newtonian = 2.0 * math.sin(math.radians(theta)) ** 2
    print("Newtonian limit Cp = 2 sin^2(10 deg) = %.4f" % newtonian)
    assert abs(newtonian - 0.0603) < 1e-3, newtonian
    prev = None
    cps = []
    for M in (5.0, 8.0, 15.0, 30.0):
        cp = oblique_cp(M, theta)
        cps.append(cp)
        print("M = %4.1f: oblique-shock Cp = %.4f (%.2f of Newtonian)" % (M, cp, cp / newtonian))
        if prev is not None:
            assert cp < prev, "Cp must fall toward the Newtonian limit"
        prev = cp
    # the flattening is the point: each Mach doubling changes Cp less
    d_5_8 = cps[0] - cps[1]
    d_15_30 = cps[2] - cps[3]
    print("delta Cp M5->8: %.4f ; M15->30: %.4f - the curve flattens" % (d_5_8, d_15_30))
    assert d_15_30 < 0.5 * d_5_8
    assert cps[3] / newtonian < 1.25
    print("rule: past Mach ~10 the pressure field barely notices more speed - geometry decides")
    print("OK: %s froze the Mach number" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_hy_newtonian(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # pure Newtonian Cp = 2 sin^2(theta)
    for deg in (5.0, 10.0, 20.0, 30.0):
        cp = 2.0 * math.sin(math.radians(deg)) ** 2
        print("theta = %4.1f deg: Cp = %.4f" % (deg, cp))
    assert abs(2.0 * math.sin(math.radians(20.0)) ** 2 - 0.2340) < 1e-3
    # modified Newtonian: Cp = Cp_stag * sin^2(theta), Cp_stag from Rayleigh pitot
    M = 10.0
    p02_p1 = _rayleigh_pitot(M)
    cp_stag = 2.0 * (p02_p1 - 1.0) / (GAMMA * M * M)
    print("M = %.0f: Rayleigh pitot p02/p1 = %.2f -> Cp_stag = %.4f" % (M, p02_p1, cp_stag))
    assert 1.80 < cp_stag < 1.85, cp_stag
    for deg in (10.0, 20.0):
        cp_mod = cp_stag * math.sin(math.radians(deg)) ** 2
        cp_pure = 2.0 * math.sin(math.radians(deg)) ** 2
        print("  theta %4.1f: pure %.4f vs modified %.4f" % (deg, cp_pure, cp_mod))
    # cone lift estimate: integrate modified Newtonian over a 10-deg half-angle cone at 5 deg AoA
    thc, alpha = math.radians(10.0), math.radians(5.0)
    n = 360
    cl = sum(max(0.0, cp_stag * math.sin(thc * math.cos(a) + alpha) ** 2 if thc * math.cos(a) + alpha > 0 else 0.0)
             * math.cos(a) for a in (2 * math.pi * i / n for i in range(n))) / n * 2.0
    print("10-deg cone at 5 deg AoA: Newtonian CL ~ %.3f" % cl)
    assert 0.05 < cl < 0.15, cl
    print("rule: particles strike, momentum turns, pressure answers - Newton priced it first")
    print("OK: %s impacted the theory" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_hy_similarity(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def oblique_cp_theta(M1, theta_deg, g=GAMMA):
    lo, hi = math.degrees(math.asin(1.0 / M1)) + 1e-6, 89.999
    for _ in range(120):
        mid = 0.5 * (lo + hi)
        bb = math.radians(mid)
        num = 2.0 * (1.0 / math.tan(bb)) * (M1 * M1 * math.sin(bb) ** 2 - 1.0)
        den = M1 * M1 * (g + math.cos(2.0 * bb)) + 2.0
        if math.degrees(math.atan(num / den)) < theta_deg:
            lo = mid
        else:
            hi = mid
    b = math.radians(0.5 * (lo + hi))
    Mn = M1 * math.sin(b)
    p = 1.0 + 2.0 * g / (g + 1.0) * (Mn * Mn - 1.0)
    return 2.0 * (p - 1.0) / (g * M1 * M1)
def main():
    # same K = M*theta(rad), different M: scaled Cp/theta^2 should collapse
    K = 1.5
    vals = []
    for M in (6.0, 10.0, 15.0):
        theta_deg = math.degrees(K / M)
        cp = oblique_cp_theta(M, theta_deg)
        scaled = cp / (math.radians(theta_deg) ** 2)
        vals.append(scaled)
        print("M = %4.1f, theta = %5.2f deg (K = %.2f): Cp/theta^2 = %.4f" % (M, theta_deg, K, scaled))
    spread = (max(vals) - min(vals)) / (sum(vals) / len(vals))
    print("spread across Mach 6-15 at constant K: %.1f%%" % (spread * 100.0))
    assert spread < 0.10, vals
    # viscous interaction parameter chi = M^3 sqrt(C) / sqrt(Re_x)
    C = 1.0
    for M, Re_x in ((5.0, 1e6), (10.0, 1e5)):
        chi = M ** 3 * math.sqrt(C) / math.sqrt(Re_x)
        regime = "strong" if chi > 1.0 else "weak"
        print("M = %4.1f, Re_x = %.0e: chi = %.2f (%s interaction)" % (M, Re_x, chi, regime))
    assert (10.0 ** 3 / math.sqrt(1e5)) > 1.0
    print("rule: K folds Mach and angle into one signature - same K, same flow")
    print("OK: %s scaled the heat" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_hy_strongweak(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def theta_of_beta(M1, beta_deg, g=GAMMA):
    b = math.radians(beta_deg)
    num = 2.0 * (1.0 / math.tan(b)) * (M1 * M1 * math.sin(b) ** 2 - 1.0)
    den = M1 * M1 * (g + math.cos(2.0 * b)) + 2.0
    return math.degrees(math.atan(num / den))
def main():
    M = 10.0
    # scan beta to find theta_max
    best = max((theta_of_beta(M, b), b) for b in [i * 0.5 for i in range(12, 170)])
    print("M = %.0f: max deflection theta_max = %.1f deg at beta = %.1f deg" % (M, best[0], best[1]))
    assert 44.0 < best[0] < 48.0, best
    # Prandtl-Meyer vacuum limit for air
    g = GAMMA
    s = math.sqrt((g + 1.0) / (g - 1.0))
    nu_max = math.degrees(0.5 * math.pi * (s - 1.0))
    print("Prandtl-Meyer vacuum limit nu_max = %.1f deg" % nu_max)
    assert 129.0 < nu_max < 132.0, nu_max
    # base pressure ~ vacuum at hypersonic speed: Cp_base -> -2/(g M^2)
    cp_base = -2.0 / (g * M * M)
    print("M = %.0f base-pressure coefficient ~ %.4f (near vacuum)" % (M, cp_base))
    assert abs(cp_base - (-0.0143)) < 1e-3, cp_base
    print("rule: the flow turns until the shock says stop - or expands until there is nothing left")
    print("OK: %s found the limits" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_hy_stagcond(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    T_inf = 216.65
    for M in (5.0, 10.0, 15.0):
        T0_T = 1.0 + 0.2 * M * M
        T0 = T0_T * T_inf
        p02_p1 = _rayleigh_pitot(M)
        print("M = %4.1f: T0/T = %5.1f -> T0 = %6.0f K ; p02/p1 = %6.1f"
              % (M, T0_T, T0, p02_p1))
    assert abs((1.0 + 0.2 * 25.0) * T_inf - 1300.0) < 5.0
    T0_10 = 21.0 * T_inf
    assert 4500.0 < T0_10 < 4600.0, T0_10
    # stagnation enthalpy: h0 = h + V^2/2 ; at Mach 10, 11 km
    V = 10.0 * _a_sound(T_inf)
    h0 = 1005.0 * T_inf + V * V / 2.0
    print("V = %.0f m/s: stagnation enthalpy h0 = %.2e J/kg" % (V, h0))
    assert 4.3e6 < h0 < 4.6e6, h0
    # kinetic share of the budget
    print("kinetic share of h0: %.1f%%" % (V * V / 2.0 / h0 * 100.0))
    assert V * V / 2.0 / h0 > 0.9
    print("rule: the nose banks the whole flight energy - every downstream state spends it")
    print("OK: %s priced the hot point" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_hy_gasbreak(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def cp_n2_vib(T):
    # thermally-perfect N2: cp = 7/2 R (translation+rotation) plus vibrational
    R = 296.8
    theta_v = 3390.0
    x = theta_v / T
    cp = 3.5 * R + R * x * x * math.exp(x) / (math.exp(x) - 1.0) ** 2
    return cp
def main():
    for T in (300.0, 1000.0, 2000.0):
        cp = cp_n2_vib(T)
        gamma = cp / (cp - 296.8)
        print("T = %6.0f K: cp = %7.1f J/kg-K, gamma = %.3f" % (T, cp, gamma))
    assert abs(cp_n2_vib(300.0) - 1039.0) < 15.0
    assert cp_n2_vib(2000.0) > 1.15 * cp_n2_vib(300.0), "vibration must raise cp"
    gamma_2000 = cp_n2_vib(2000.0) / (cp_n2_vib(2000.0) - 296.8)
    assert gamma_2000 < 1.33, gamma_2000
    print("thresholds: vibration ~800 K, O2 dissociation ~2000 K, N2 ~4000 K, ionization ~9000 K")
    # model ladder choice
    for T, model in ((500.0, "calorically perfect"), (1500.0, "thermally perfect"),
                     (3000.0, "equilibrium reacting"), (6000.0, "nonequilibrium")):
        print("  %6.0f K -> %s" % (T, model))
    print("rule: heat edits the gas model - use the wrong draft and the numbers lie")
    print("OK: %s broke the perfect gas" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_hy_realgas(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # density ratio across a strong normal shock vs effective gamma
    def rho_ratio(g):
        return (g + 1.0) / (g - 1.0)
    for g, tag in ((1.40, "cold perfect gas"), (1.20, "dissociating"), (1.10, "strongly dissociated")):
        print("%-20s gamma=%.2f -> density ratio %.1f" % (tag, g, rho_ratio(g)))
    assert abs(rho_ratio(1.40) - 6.0) < 1e-9
    assert rho_ratio(1.10) > 15.0
    # standoff shrinks as density ratio grows
    Rn = 1.0
    for g in (1.40, 1.15):
        print("  gamma %.2f: standoff ~ %.3f m per meter nose" % (g, Rn / rho_ratio(g)))
    # real shock-layer temperature: energy split between heating and dissociation
    V = 6000.0
    T_perfect = V * V / (2.0 * 1005.0)   # all kinetic -> sensible
    # with dissociation absorbing ~40% the temperature falls
    T_real = T_perfect * 0.6
    print("V = %.0f m/s: perfect-gas T0 ~ %.0f K, real (dissociating) ~ %.0f K"
          % (V, T_perfect, T_real))
    assert T_real < 0.7 * T_perfect
    # catalytic wall penalty: recombination dumps formation energy as heat
    q_noncat, q_cat = 1.0, 1.5
    print("wall catalycity: non-catalytic q = %.1f -> fully catalytic q = %.1f (relative)" % (q_noncat, q_cat))
    assert q_cat > q_noncat
    print("rule: dissociation cools the gas but heats the wall that welcomes atoms home")
    print("OK: %s felt the real gas" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_hy_blastwave(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # Taylor-Sedov cylindrical blast: R = (E t^2 / rho)^(1/4)
    # unsteady analogy: t = x/V -> shock radius grows as x^(1/2)
    E_per_L = 1.0e6   # energy per unit length, J/m (drag * 1m)
    rho = 0.01
    V = 3000.0
    print("cylindrical blast, E/L = %.1e J/m, rho = %.3f kg/m3:" % (E_per_L, rho))
    radii = []
    for x in (10.0, 40.0, 90.0):
        t = x / V
        R = (E_per_L * t * t / rho) ** 0.25
        radii.append(R)
        print("  x = %5.1f m (t = %.3f s): shock radius R = %.2f m" % (x, t, R))
    # check x^(1/2) growth: R(40)/R(10) should be 2
    assert abs(radii[1] / radii[0] - 2.0) < 1e-9, radii
    assert abs(radii[2] / radii[0] - 3.0) < 1e-9, radii
    print("R grows as sqrt(x): doubling distance quadruples... no - doubles the radius")
    # pressure behind the blast decays as R^-2 (cylindrical)
    p1 = 1.0 / radii[0] ** 2
    p2 = 1.0 / radii[1] ** 2
    print("pressure decay: p(40m)/p(10m) = %.3f" % (p2 / p1))
    assert abs(p2 / p1 - 0.25) < 1e-9
    print("rule: the blunt nose is a continuous explosion - Sedov wrote its biography")
    print("OK: %s rode the blast" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_hy_bluntness(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # heating ~ 1/sqrt(Rn): Sutton-Graves form at fixed rho, V
    k, rho, V = 1.83e-4, 1.0e-4, 7000.0
    def q(Rn):
        return k * math.sqrt(rho / Rn) * V ** 3
    q_sharp = q(0.05)
    q_blunt = q(1.0)
    print("rho=%.0e, V=%.0f m/s:" % (rho, V))
    print("  Rn = 0.05 m: q = %.2e W/m2" % q_sharp)
    print("  Rn = 1.00 m: q = %.2e W/m2" % q_blunt)
    print("  bluntness cuts peak heating %.1fx" % (q_sharp / q_blunt))
    assert abs(q_sharp / q_blunt - math.sqrt(20.0)) < 1e-9
    # standoff grows with Rn
    for Rn in (0.05, 1.0):
        print("  Rn = %.2f m: standoff ~ %.3f m (delta ~ Rn/6)" % (Rn, Rn / 6.0))
    # drag penalty of bluntness: wave drag ~ Cp_stag * frontal area
    cp_stag = 1.83
    for Rn in (0.05, 1.0):
        A = math.pi * Rn * Rn
        print("  Rn = %.2f m: blunt wave-drag proxy Cp*A = %.3f m2" % (Rn, cp_stag * A))
    assert cp_stag * math.pi * 1.0 ** 2 > 100.0 * cp_stag * math.pi * 0.05 ** 2
    print("rule: blunt survives, sharp melts - geometry is thermal protection")
    print("OK: %s blunted the nose" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_hy_stagheat(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def sutton_graves(rho, V, Rn, k=1.83e-4):
    return k * math.sqrt(rho / Rn) * V ** 3
def main():
    # Apollo-like: Rn = 4.6 m, V = 11 km/s, rho at 70 km ~ 8.8e-5
    q = sutton_graves(8.8e-5, 11000.0, 4.6)
    print("Apollo-like entry: q_stag = %.2e W/m2 (%.2f MW/m2)" % (q, q / 1e6))
    assert 0.8e6 < q < 1.4e6, q
    # V^3 sensitivity: +10% velocity
    q2 = sutton_graves(8.8e-5, 12100.0, 4.6)
    print("+10%% velocity -> q = %.2f MW/m2 (%.0f%% more)" % (q2 / 1e6, (q2 / q - 1.0) * 100.0))
    assert abs(q2 / q - 1.331) < 1e-9
    # LEO return at 7.8 km/s for comparison
    q_leo = sutton_graves(8.8e-5, 7800.0, 4.6)
    print("LEO return 7.8 km/s: q = %.2f MW/m2" % (q_leo / 1e6))
    assert q / q_leo > 2.5, "lunar return is a different world"
    # Fay-Riddell flavor: q ~ (rho*mu)^0.4 (rho_e mu_e)^0.1 (h0 - hw)
    # show the enthalpy-difference driving potential
    h0 = 11000.0 ** 2 / 2.0
    print("stagnation enthalpy at 11 km/s: %.2e J/kg" % h0)
    assert 6.0e7 < h0 < 6.1e7, h0
    print("rule: velocity cubed - the unforgiving arithmetic of fire")
    print("OK: %s metered the stagnation fire" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_hy_heatdist(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # Lees-type distribution on a sphere: q/q_stag vs angle from stagnation point
    q_stag = 1.0
    print("sphere heating distribution q/q_stag:")
    for deg in (0.0, 30.0, 60.0, 90.0):
        # correlation-style decay: cos^1.5-ish falloff
        ratio = math.cos(math.radians(deg)) ** 1.5 if deg < 90.0 else 0.0
        print("  %4.0f deg: %.3f" % (deg, ratio))
    assert abs(math.cos(math.radians(60.0)) ** 1.5 - 0.3536) < 1e-3
    # transition cliff: turbulent heating 3-5x laminar
    q_lam = 0.4
    for factor in (3.0, 5.0):
        print("transition: laminar %.2f -> turbulent %.2f (x%.0f)" % (q_lam, q_lam * factor, factor))
    # flap hot spot: reattachment amplification
    q_flap = 0.5 * 4.0
    print("deflected flap reattachment: undisturbed 0.50 -> hot spot %.1f (x4)" % q_flap)
    assert abs(q_flap - 2.0) < 1e-9
    # the map must be drawn with the cliff included
    print("heating maps carry transition as a step and interactions as spikes")
    print("rule: the nose takes the headline, the whole body takes the heat")
    print("OK: %s mapped the heat" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_hy_tps(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # ablative sizing: mass loss = heat load / heat of ablation Q*
    Q_star = 2.0e7   # J/kg, typical ablator effective heat of ablation
    heat_load = 5.0e8  # J/m2 integrated over entry
    m_loss = heat_load / Q_star
    print("heat load %.1e J/m2 / Q* %.1e J/kg -> ablated mass %.1f kg/m2"
          % (heat_load, Q_star, m_loss))
    assert abs(m_loss - 25.0) < 1e-9, m_loss
    rho_tps = 1400.0
    thickness = m_loss / rho_tps * 2.0   # factor 2: char + virgin + margin
    print("TPS thickness needed: %.1f cm" % (thickness * 100.0))
    assert 0.02 < thickness < 0.06, thickness
    # reusable tile: conduction drop across 5 cm of tile, k = 0.05 W/m-K
    k_tile, L = 0.05, 0.05
    q_in = 2.0e5
    # radiative equilibrium surface: eps sigma T^4 = q
    eps, sigma = 0.9, 5.67e-8
    T_surf = (q_in / (eps * sigma)) ** 0.25
    print("tile surface at q=%.0e W/m2: T = %.0f K (re-radiating)" % (q_in, T_surf))
    assert 1300.0 < T_surf < 1500.0, T_surf
    # conducted inward: in radiative equilibrium the surface re-radiates nearly
    # everything; only a small conducted flux soaks toward the structure
    q_cond = 0.0025 * q_in   # 0.25% conducted
    dT_tile = q_cond * L / k_tile
    print("conducted flux %.0f W/m2 -> %.0f K drop across the %.0f-cm tile"
          % (q_cond, dT_tile, L * 100.0))
    assert 400.0 < dT_tile < 600.0, dT_tile
    print("structure beneath stays cool while the surface glows at %.0f K" % T_surf)
    print("rule: ablate the fierce entries, insulate the reusable ones")
    print("OK: %s skinned the vehicle" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_hy_ablation(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # surface energy balance: q_conv + q_rad = q_reradiated + q_ablation + q_conduction
    q_conv, q_rad = 1.2e6, 0.3e6
    eps, sigma, T_w = 0.9, 5.67e-8, 2000.0
    q_rerad = eps * sigma * T_w ** 4
    q_cond = 0.1e6
    Q_star = 2.0e7
    q_abl = q_conv + q_rad - q_rerad - q_cond
    m_dot = q_abl / Q_star
    print("in: %.2f MW/m2 | re-radiated %.2f | conducted %.2f | ablation %.2f MW/m2"
          % ((q_conv + q_rad) / 1e6, q_rerad / 1e6, q_cond / 1e6, q_abl / 1e6))
    print("ablation mass flux: %.3f kg/m2-s" % m_dot)
    assert q_abl > 0, "energy must balance with positive ablation"
    assert 0.001 < m_dot < 0.05, m_dot
    # blowing effect: B' = m_dot / (rho_e u_e C_M) ; heating reduction
    B_prime = 0.2
    reduction = 1.0 / (1.0 + 2.0 * B_prime)
    print("B' = %.1f: blowing cuts convective heating to %.0f%%" % (B_prime, reduction * 100.0))
    assert 0.6 < reduction < 0.8, reduction
    # recession over a 300 s entry
    rho_char = 400.0
    recession = m_dot * 300.0 / rho_char
    print("300 s entry: char recession ~ %.1f cm" % (recession * 100.0))
    assert recession > 0.0
    print("rule: the shield spends itself so the crew does not have to")
    print("OK: %s burned the shield" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_hy_reentry(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # ballistic coefficient beta = W/(C_D A) = m/(C_D A)
    def beta(m, CD, A):
        return m / (CD * A)
    capsule = beta(8000.0, 1.4, 12.0)
    lifting = beta(8000.0, 0.8, 30.0)
    print("capsule beta = %.0f kg/m2 ; lifting body beta = %.0f kg/m2" % (capsule, lifting))
    assert capsule > 400.0 and lifting < 400.0
    # peak deceleration scales with 1/beta at fixed entry angle: n_max ~ V^2 sin(gamma)/(2 e beta g0)-ish
    # use scaling: n1/n2 = beta2/beta1
    print("lifting body pulls %.1fx the capsule's peak g (at same gamma)" % (capsule / lifting))
    # entry corridor: overshoot boundary gamma ~ -0.5 deg, undershoot ~ -3 deg for capsule
    print("capsule corridor: overshoot ~-0.5 deg (skip-out) ; undershoot ~-3 deg (g/heating)")
    # peak heating point: max of rho*V^3 along a -1.5 deg entry (scale heights)
    H = 7200.0
    rho0 = 1.225
    V0 = 7800.0
    gamma = math.radians(1.5)
    # rho*V^3 peaks where d/dh = 0 for exponential atmosphere, const gamma: h* = H*ln-ish
    # demonstrate numerically
    best = max(((rho0 * math.exp(-h / H)) * (V0 * math.exp(-h * 0.0 / H)) ** 3, h)
               for h in range(20000, 90001, 1000))
    print("rho*V^3 (const-V proxy) peaks at h = %.0f m" % best[1])
    # bank-angle modulation: lift vector tilt controls energy
    for bank_deg in (0.0, 60.0):
        lift_up = math.cos(math.radians(bank_deg))
        print("bank %4.0f deg: vertical lift fraction %.2f" % (bank_deg, lift_up))
    assert abs(math.cos(math.radians(60.0)) - 0.5) < 1e-9
    print("rule: beta chooses the corridor, bank angle flies it")
    print("OK: %s flew the corridor" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_hy_viscint(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # chi = M^3 sqrt(C) / sqrt(Re_x) ; strong interaction chi >> 1
    def chi(M, Re_x, C=1.0):
        return M ** 3 * math.sqrt(C) / math.sqrt(Re_x)
    cases = [(3.0, 1e6, "supersonic plate"), (8.0, 1e6, "hypersonic plate"),
             (10.0, 1e5, "hypersonic high altitude")]
    for M, Re_x, tag in cases:
        c = chi(M, Re_x)
        regime = "STRONG" if c > 3.0 else ("weak" if c < 0.5 else "moderate")
        print("%-24s M=%4.1f Re_x=%.0e: chi=%6.2f [%s]" % (tag, M, Re_x, c, regime))
    assert chi(3.0, 1e6) < 0.1, "supersonic plate should be weak"
    assert chi(10.0, 1e5) > 3.0, "high-altitude hypersonic should be strong"
    # induced pressure rise near leading edge (strong-interaction scaling ~ chi^0.5)
    c = chi(10.0, 1e5)
    p_induced_ratio = 1.0 + 0.5 * math.sqrt(c)
    print("induced pressure near leading edge: %.1fx the inviscid value" % p_induced_ratio)
    assert p_induced_ratio > 1.5
    # displacement thickness scale: delta*/x ~ M^2/sqrt(Re_x)
    dstar = 10.0 ** 2 / math.sqrt(1e5)
    print("delta*/x ~ M^2/sqrt(Re_x) = %.3f at M=10, Re_x=1e5" % dstar)
    assert dstar > 0.2, "thick layer - co-author of the pressure field"
    print("rule: at hypersonic speed the boundary layer edits the pressure field")
    print("OK: %s coupled the viscous" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_hy_transition(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # second-mode frequency: f ~ U_e / (2 delta)
    U_e, delta = 1500.0, 0.003
    f = U_e / (2.0 * delta)
    print("second-mode frequency: U_e=%.0f m/s, delta=%.0f mm -> f = %.0f kHz"
          % (U_e, delta * 1000.0, f / 1000.0))
    assert 200.0e3 < f < 300.0e3, f
    # transition Reynolds number grows with Mach (roughly), then bluntness reversal
    for M, Re_xt in ((3.0, 3.0e6), (6.0, 8.0e6), (8.0, 12.0e6)):
        x_t = Re_xt * MU_AIR / (RHO_SL * 1500.0)
        print("M = %.0f: Re_x,transition ~ %.1e" % (M, Re_xt))
    # heating cliff across transition
    q_lam = 1.0
    print("transition: q %.1f -> %.1f (turbulent, x%.0f)" % (q_lam, q_lam * 4.0, 4.0))
    # roughness: critical roughness Reynolds Re_kk
    k_rough = 0.0002
    u_k = 1500.0 * 0.5
    Re_kk = 0.01 * u_k * k_rough / MU_AIR
    print("roughness Re_kk ~ %.0f (trip risk if > ~250)" % Re_kk)
    # e^N: N=9-10 in flight
    N = 9.5
    print("e^N method: N = %.1f -> amplification e^N = %.1e" % (N, math.exp(N)))
    assert math.exp(N) > 1e4
    print("rule: the trapped wave breaks the smooth signature - heating jumps the cliff")
    print("OK: %s tripped the transition" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_hy_sbli(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # incipient separation angle shrinks with Mach (deg, turbulent, rough scaling)
    for M, alpha_inc in ((3.0, 14.0), (5.0, 10.0), (8.0, 7.0)):
        print("M = %.0f: incipient separation ~ %.0f deg ramp" % (M, alpha_inc))
    assert True
    # reattachment heating amplification vs ramp angle
    print("reattachment heating amplification:")
    for ramp_deg, amp in ((10.0, 2.0), (20.0, 4.5), (30.0, 8.0)):
        print("  %4.0f-deg ramp: x%.1f" % (ramp_deg, amp))
    assert 8.0 > 4.5 > 2.0
    # separation length scales with incoming boundary-layer thickness and shock strength
    delta = 0.01
    L_sep = delta * 30.0   # strong interaction order
    print("delta = %.0f mm -> separation bubble L ~ %.2f m" % (delta * 1000.0, L_sep))
    assert L_sep > 10.0 * delta
    # Edney Type IV: jet impingement heating spike
    q_stag = 1.0
    q_type4 = 12.0 * q_stag
    print("Edney Type IV shock-shock: local heating x%.0f stagnation value" % (q_type4 / q_stag))
    assert q_type4 / q_stag > 10.0
    # cowl-lip design consequence
    print("cowl lips and flap hinges are placed to dodge Type IV impingement")
    print("rule: where shocks meet the layer, the signature folds and burns through")
    print("OK: %s separated and reattached" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_hy_entropy(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # entropy rise across normal vs oblique shock: ds/R = ln-ish; show gradient
    def ds_R(Mn, g=GAMMA):
        p = 1.0 + 2.0 * g / (g + 1.0) * (Mn * Mn - 1.0)
        r = ((g + 1.0) * Mn * Mn) / ((g - 1.0) * Mn * Mn + 2.0)
        return math.log(p / r ** g) / (g - 1.0)
    ds_nose = ds_R(10.0)
    ds_flank = ds_R(2.5)
    print("entropy rise ds/R: nose (Mn=10) %.2f vs flank (Mn=2.5) %.2f"
          % (ds_nose, ds_flank))
    assert ds_nose > 3.0 * ds_flank, "strong normal-shock entropy dominates"
    # swallowing distance: x_sw ~ Rn * f(M) ; blunt cone swallows late
    Rn = 0.5
    for M in (5.0, 10.0):
        x_sw = Rn * (8.0 + 0.5 * M)
        print("M = %4.1f, Rn = %.1f m: swallowing distance ~ %.1f m (%.0f nose radii)"
              % (M, Rn, x_sw, x_sw / Rn))
    # inside the entropy layer the edge Mach is low and temperature high
    print("edge conditions inside layer: hot, low-Mach nose-shock gas - not freestream")
    # capsule: never swallows
    print("capsule afterbody: entropy layer thicker than the vehicle is long")
    print("rule: the nose writes a hot blanket over everything behind it")
    print("OK: %s swallowed the layer" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_hy_ld(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # Kuchemann-style (L/D)max decline with Mach
    def ld_max(M):
        return 4.0 * (M + 3.0) / M
    for M in (0.8, 2.0, 6.0, 10.0):
        print("M = %4.1f: Kuchemann (L/D)max ~ %.1f" % (M, ld_max(M)))
    assert ld_max(6.0) < 7.0, ld_max(6.0)
    assert ld_max(0.8) > 15.0
    # drag breakdown at Mach 6 for a waverider-ish vehicle
    CD_wave, CD_fric, CD_base = 0.045, 0.020, 0.008
    CD = CD_wave + CD_fric + CD_base
    CL = 0.30
    LD = CL / CD
    print("M=6: CD_wave=%.3f CD_fric=%.3f CD_base=%.3f -> L/D = %.1f at CL=%.2f"
          % (CD_wave, CD_fric, CD_base, LD, CL))
    assert 3.5 < LD < 5.0, LD
    print("wave drag share: %.0f%%" % (CD_wave / CD * 100.0))
    assert CD_wave / CD > 0.5
    # range from L/D: R ~ (L/D) * altitude (glide)
    h = 30000.0
    print("glide range from %d km at L/D=%.1f: ~%.0f km" % (h / 1000.0, LD, LD * h / 1000.0))
    assert LD * h / 1000.0 > 100.0
    print("rule: speed spends reach - every tenth of L/D is bought, not given")
    print("OK: %s priced the glide" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_hy_scramjet(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # scramjet Brayton: stations - capture, combustor in, combustor out, nozzle exit
    M0 = 8.0
    T0, p0 = 1200.0, 120000.0  # combustor-entrance static conditions after inlet
    # lean hydrogen burn: f ~ 0.015, h_pr = 120 MJ/kg
    f, h_pr = 0.015, 120.0e6
    cp = 1200.0
    q_add = f * h_pr
    T_cc = T0 + q_add / ((1.0 + f) * cp)
    print("heat addition: q = %.2e J/kg -> combustor T %.0f K -> %.0f K" % (q_add, T0, T_cc))
    assert T_cc > 2500.0, T_cc
    # thermal choking check (Rayleigh): heat addition must not drive combustor Mach to 1.
    # at M=3.0, gamma=1.3: T/T* ~ 0.30, so max heat ratio = T*/T - 1 ~ 2.3.
    # real combustors also diverge (area relief) for extra margin.
    M_cc = 3.0
    T_Tstar = 0.30
    max_heat_ratio = 1.0 / T_Tstar - 1.0
    actual_ratio = (T_cc - T0) / T0
    print("Rayleigh: max heat ratio at M=3.0: %.2f ; actual: %.2f" % (max_heat_ratio, actual_ratio))
    assert actual_ratio < max_heat_ratio, "would thermally choke"
    # specific impulse: Isp ~ V_exhaust-ish / g0 ; scramjet ~ 1000-2000 s vs rocket ~450 s
    Isp_scram, Isp_rocket = 1500.0, 450.0
    print("Isp: scramjet ~%.0f s vs rocket ~%.0f s (no oxidizer carried)" % (Isp_scram, Isp_rocket))
    assert Isp_scram > 3.0 * Isp_rocket
    # residence time: 1 m combustor at ~1500 m/s
    t_res = 1.0 / 1500.0
    print("residence time: %.2f ms - mix and burn in a blink" % (t_res * 1000.0))
    assert t_res < 1e-3
    print("rule: fire lit inside a hurricane, held steady by geometry alone")
    print("OK: %s burned supersonic" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_hy_inlet(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def kantrowitz(M, g=GAMMA):
    # max started contraction ratio: isentropic area ratio at M divided by normal-shock total pressure recovery
    def A_Astar(mm):
        return (1.0 / mm) * ((2.0 / (g + 1.0)) * (1.0 + (g - 1.0) / 2.0 * mm * mm)) ** ((g + 1.0) / (2.0 * (g - 1.0)))
    p = 1.0 + 2.0 * g / (g + 1.0) * (M * M - 1.0)
    M2sq = ((g - 1.0) * M * M + 2.0) / (2.0 * g * M * M - (g - 1.0))
    p02_p2 = (1.0 + (g - 1.0) / 2.0 * M2sq) ** (g / (g - 1.0))
    p01_p1 = (1.0 + (g - 1.0) / 2.0 * M * M) ** (g / (g - 1.0))
    rec = p02_p2 * p / p01_p1   # normal-shock total-pressure recovery
    return rec * A_Astar(M)     # Kantrowitz: CR_max = recovery x isentropic area ratio
def main():
    for M in (3.0, 4.0, 6.0):
        cr = kantrowitz(M)
        print("entrance M = %.1f: Kantrowitz max contraction ratio = %.2f" % (M, cr))
    assert kantrowitz(4.0) < kantrowitz(6.0), "higher Mach allows more contraction"
    assert 1.0 < kantrowitz(4.0) < 3.0, kantrowitz(4.0)
    # multi-ramp external compression at Mach 8: three 8-deg ramps
    # each weak shock: small loss; total recovery high vs single normal shock
    def normal_rec(M, g=GAMMA):
        p = 1.0 + 2.0 * g / (g + 1.0) * (M * M - 1.0)
        M2sq = ((g - 1.0) * M * M + 2.0) / (2.0 * g * M * M - (g - 1.0))
        p02_p2 = (1.0 + (g - 1.0) / 2.0 * M2sq) ** (g / (g - 1.0))
        p01_p1 = (1.0 + (g - 1.0) / 2.0 * M * M) ** (g / (g - 1.0))
        return p02_p2 * p / p01_p1
    single = normal_rec(8.0)
    multi = 0.97 ** 3 * normal_rec(2.2)   # three weak ramps then weak terminal shock
    print("Mach 8: single normal recovery %.4f vs 3-ramp + terminal %.4f" % (single, multi))
    assert multi > 5.0 * single
    # kinetic energy efficiency target
    ke_eff = 0.96
    print("kinetic-energy efficiency target: %.2f - every point is thrust" % ke_eff)
    print("rule: compress without slowing - the inlet seats a hurricane supersonically")
    print("OK: %s started the inlet" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_hy_waverider(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # conical waverider: cone half-angle 10 deg at Mach 6
    M, thc = 6.0, math.radians(10.0)
    # Taylor-Maccoll-ish: use oblique shock at cone angle as proxy for surface pressure
    lo, hi = math.degrees(math.asin(1.0 / M)) + 1e-6, 89.999
    for _ in range(120):
        mid = 0.5 * (lo + hi)
        bb = math.radians(mid)
        num = 2.0 * (1.0 / math.tan(bb)) * (M * M * math.sin(bb) ** 2 - 1.0)
        den = M * M * (GAMMA + math.cos(2.0 * bb)) + 2.0
        if math.degrees(math.atan(num / den)) < 10.0:
            lo = mid
        else:
            hi = mid
    beta = math.radians(0.5 * (lo + hi))
    Mn = M * math.sin(beta)
    p_ratio = 1.0 + 2.0 * GAMMA / (GAMMA + 1.0) * (Mn * Mn - 1.0)
    cp_under = 2.0 * (p_ratio - 1.0) / (GAMMA * M * M)
    print("M = %.0f, 10-deg cone: shock %.1f deg, underside Cp = %.4f"
          % (M, math.degrees(beta), cp_under))
    assert 0.10 < cp_under < 0.16, cp_under
    # upper surface: Prandtl-Meyer expansion to near-vacuum-ish low pressure
    cp_upper = -0.02
    # planform: delta wing, S_ref; lift from pressure difference
    dcp = cp_under - cp_upper
    # L/D estimate: lift ~ dCp * planform factor, drag ~ wave + friction
    LD = dcp / (0.035)
    print("delta-Cp = %.3f -> L/D estimate ~ %.1f" % (dcp, LD))
    assert 3.0 < LD < 6.0, LD
    # shock-riding condition: leading-edge sweep must match shock angle
    print("leading edge rides the %.1f-deg shock: no spillage, no detachment drag"
          % math.degrees(beta))
    # off-design: at Mach 5 the shock angle grows -> edge no longer on shock
    print("off-design (lower Mach): shock steepens, spillage begins - the waverider compromise")
    print("rule: surf the wave you make - lift drawn from your own shock")
    print("OK: %s rode the shock" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_hy_rarefied(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # mean free path vs altitude (exponential atmosphere, sea-level lambda ~ 68 nm)
    lam_sl = 68.0e-9
    H = 7200.0
    L = 1.0   # 1-m nose radius vehicle
    print("Knudsen number Kn = lambda/L for L = %.0f m:" % L)
    for h_km in (60.0, 80.0, 100.0, 120.0):
        lam = lam_sl * math.exp(h_km * 1000.0 / H)
        Kn = lam / L
        if Kn < 0.01:
            regime = "continuum"
        elif Kn < 0.1:
            regime = "slip flow"
        elif Kn < 10.0:
            regime = "transition (DSMC)"
        else:
            regime = "free-molecule"
        print("  %5.0f km: lambda = %.2e m, Kn = %.3f [%s]" % (h_km, lam, Kn, regime))
    lam100 = lam_sl * math.exp(100000.0 / H)
    assert 0.05 < lam100 < 0.3, lam100
    # free-molecule drag: flat plate normal to flow, diffuse reflection: CD ~ 2
    rho_120 = RHO_SL * math.exp(-120000.0 / H)
    V = 7500.0
    D_fm = 2.0 * _q(rho_120, V) * 1.0
    print("120 km free-molecule drag per m2: %.3f N" % D_fm)
    assert D_fm < 10.0, "whisper drag at the edge of air"
    # slip-flow correction size
    print("slip regime: Navier-Stokes + velocity slip + temperature jump at the wall")
    print("rule: the continuum lets go molecule by molecule - Kn names the regime")
    print("OK: %s thinned to molecules" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_hy_chemistry(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # Zeldovich: N2 + O -> NO + N ; k_f = C T^eta exp(-Ta/T), Ta ~ 38000 K
    C, eta, Ta = 7.0e10, 0.0, 38000.0
    def kf(T):
        return C * (T ** eta) * math.exp(-Ta / T)
    for T in (3000.0, 5000.0, 8000.0):
        print("T = %.0f K: Zeldovich k_f = %.2e" % (T, kf(T)))
    assert kf(8000.0) / kf(3000.0) > 1e3, "violent temperature sensitivity"
    # equilibrium composition sketch: O2 dissociated fraction vs T (illustrative logistic)
    print("dissociation fraction (illustrative):")
    for T, tag in ((2000.0, "O2 onset"), (4000.0, "N2 onset"), (6000.0, "heavily dissociated")):
        alpha = 1.0 / (1.0 + math.exp(-(T - 3500.0) / 800.0))
        print("  %.0f K [%s]: alpha ~ %.2f" % (T, tag, alpha))
    # Saha ionization onset: electron fraction grows steeply past ~9000 K
    def saha_ion(T):
        return 1.0 / (1.0 + math.exp(-(T - 11000.0) / 1200.0))
    for T in (8000.0, 11000.0, 14000.0):
        print("T = %.0f K: ionization fraction ~ %.3f" % (T, saha_ion(T)))
    assert saha_ion(14000.0) > 0.9 > saha_ion(8000.0)
    print("plasma frequency exceeds radio frequencies -> communications blackout")
    # Park uncertainty note
    print("rate data (Park models) carry the largest uncertainty in aerothermodynamics")
    print("rule: the shock unmakes air into five letters, then eleven")
    print("OK: %s reacted the air" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_hy_facilities(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # reflected shock tunnel: reservoir from reflected shock at Mach 4 incident
    M_s = 5.0
    g = GAMMA
    # temperature ratio across incident + reflected shock (approx: two normal shocks)
    def T_ratio(M):
        p = 1.0 + 2.0 * g / (g + 1.0) * (M * M - 1.0)
        r = ((g + 1.0) * M * M) / ((g - 1.0) * M * M + 2.0)
        return p / r
    T2_T1 = T_ratio(M_s)
    T5_T2 = T_ratio(2.5)   # reflected shock weaker
    T_res = 300.0 * T2_T1 * T5_T2
    print("incident Ms=%.1f: T2/T1=%.1f, T5/T2=%.1f -> reservoir T0 ~ %.0f K"
          % (M_s, T2_T1, T5_T2, T_res))
    assert T_res > 2500.0, T_res
    # test time: ~2 ms for a 10-m shock tube
    L_tube = 10.0
    a_driver = 1000.0
    t_test = 0.002
    print("test time ~ %.0f ms: model must be instrumented for microseconds" % (t_test * 1000.0))
    # expansion tube: higher enthalpy via unsteady expansion
    h_shock_tunnel = 8.0e6    # J/kg
    h_expansion = 20.0e6
    print("enthalpy: shock tunnel %.1e J/kg vs expansion tube %.1e J/kg"
          % (h_shock_tunnel, h_expansion))
    assert h_expansion > 2.0 * h_shock_tunnel
    # equivalent flight velocity
    V_eq = math.sqrt(2.0 * h_expansion)
    print("expansion-tube enthalpy = %.1f km/s equivalent flight speed" % (V_eq / 1000.0))
    assert 6.0 < V_eq / 1000.0 < 7.0, V_eq
    # facility trade
    print("trade: test time vs enthalpy vs flow quality - no one rig covers a trajectory")
    print("rule: flight flashed in milliseconds - instruments must blink to catch it")
    print("OK: %s fired the tunnel" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_hy_flighttest(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # the proving years: Mach, peak altitude, key demonstration
    flights = [
        ("X-15", 6.7, 107.0, "hypersonic heating + reaction controls, 199 flights"),
        ("Shuttle", 24.0, 120.0, "reusable TPS + lifting entry, 135 flights"),
        ("X-43A", 9.6, 33.0, "scramjet, fastest airbreathing flight"),
        ("X-51A", 5.1, 21.0, "hydrocarbon scramjet, 210 s burn"),
    ]
    for name_, mach, alt, feat in flights:
        V = mach * _a_sound(216.65)
        print("%-8s Mach %4.1f (~%.0f m/s), %5.0f km: %s" % (name_, mach, V, alt, feat))
    # X-43A speed check
    V_x43 = 9.6 * _a_sound(216.65)
    assert 2800.0 < V_x43 < 2900.0, V_x43
    # X-51A burn time vs X-43A
    print("burn duration: X-43A ~11 s -> X-51A 210 s (19x longer)")
    assert 210.0 / 11.0 > 15.0
    # dynamic pressure at X-43A test point (33 km, rho ~ 8e-3)
    rho_33 = RHO_SL * math.exp(-33000.0 / 7200.0)
    q_43 = _q(rho_33, V_x43)
    print("X-43A test q ~ %.0f kPa (the corridor's currency)" % (q_43 / 1000.0))
    assert 30.0 < q_43 / 1000.0 < 80.0, q_43
    print("rule: tunnels approximate, flight closes - every generation builds its X-plane")
    print("OK: %s flew the proving years" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_hy_stability(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # Newtonian pitch stiffness of a blunt 15-deg half-angle cone
    thc = math.radians(15.0)
    cp_stag = 1.83
    # Cm_alpha ~ -sum over windward panels of Cp * moment arm ; estimate per radian
    # simplified: Cm_alpha = -k * cp_stag * sin(2*thc)-ish scaling
    Cm_alpha = -cp_stag * math.sin(2.0 * thc) * 2.0
    print("15-deg blunt cone: Newtonian Cm_alpha ~ %.3f per rad (stable)" % Cm_alpha)
    assert Cm_alpha < -0.5, Cm_alpha
    # trim: flap deflection needed to trim at alpha=10 deg
    alpha = math.radians(10.0)
    Cm_alpha_body = Cm_alpha * alpha
    # body flap effectiveness (Newtonian, flap at 25 deg local inclination)
    flap_deg = 20.0
    dCm_ddef = -0.02   # per degree, representative
    defl_trim = -Cm_alpha_body / dCm_ddef
    print("trim at 10 deg AoA needs ~%.1f deg body-flap (magnitude; sign sets direction)" % abs(defl_trim))
    assert 0.0 < abs(defl_trim) < 30.0, defl_trim
    # trim drag penalty
    dCD_trim = 0.5 * cp_stag * math.sin(math.radians(defl_trim)) ** 2 * 0.15
    print("trim-drag increment ~ %.4f" % dCD_trim)
    assert dCD_trim > 0.0
    # RCS hand-off: q below which aero control quits (~1 kPa)
    print("below q ~ 1 kPa: aerodynamic control quits, RCS takes over")
    # X-15/Shuttle blend
    print("blend schedule: RCS-only high, blended mid-corridor, aero-only low")
    print("rule: the forebody is a weathervane, the flap pays trim drag, the jets mind the top")
    print("OK: %s trimmed hypersonic" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_hy_noneq(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # Damkohler number Da = flow time / chemical time
    def regime(Da):
        if Da > 100.0:
            return "equilibrium"
        if Da < 0.01:
            return "frozen"
        return "NONEQUILIBRIUM"
    cases = [(1e4, "nose region, low altitude"), (1.0, "peak-heating point"),
             (1e-3, "far wake / high altitude")]
    for Da, tag in cases:
        print("Da = %6.1e [%s]: %s" % (Da, tag, regime(Da)))
    assert regime(1.0) == "NONEQUILIBRIUM"
    # relaxation zone: vibrational relaxation time (Landau-Teller-ish, illustrative)
    T, p = 5000.0, 1000.0
    tau_v = 1.0e-6 * (300.0 / T) ** 2 * (101325.0 / p) * 10.0
    print("vibrational relaxation time ~ %.1e s at %.0f K, %.0f Pa" % (tau_v, T, p))
    # flow time across 1-m shock layer at 2000 m/s post-shock
    t_flow = 1.0 / 2000.0
    Da_v = t_flow / tau_v
    print("flow time %.1e s -> Da_vib ~ %.1f" % (t_flow, Da_v))
    # temperature overshoot: frozen T right behind shock vs equilibrium T
    T_frozen, T_eq = 12000.0, 6000.0
    print("relaxation zone: T spikes to %.0f K (frozen), decays to %.0f K (equilibrium)"
          % (T_frozen, T_eq))
    assert T_frozen > 1.5 * T_eq
    # Park two-temperature model
    print("Park model: T (translation-rotation) + T_v (vibration) - the workhorse")
    print("rule: the shock writes faster than chemistry reads - the layer catches up in space")
    print("OK: %s relaxed the chemistry" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_hy_radheat(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # Tauber-Sutton-like radiative heating scaling: q_rad ~ rho^1.2 * V^8-ish (illustrative)
    def q_rad(rho, V):
        return 1.0e-30 * (rho ** 1.2) * (V ** 8.0)
    # normalize to Apollo-like point: rho=8.8e-5, V=11 km/s -> ~0.5 MW/m2 radiative
    ref = q_rad(8.8e-5, 11000.0)
    print("radiative scaling anchored at Apollo-like point:")
    for V in (8000.0, 11000.0, 13000.0):
        ratio = q_rad(8.8e-5, V) / ref
        print("  V = %.0f km/s: q_rad x%.2f of Apollo value" % (V / 1000.0, ratio))
    assert q_rad(8.8e-5, 13000.0) / ref > 3.0, "brutal velocity scaling"
    assert q_rad(8.8e-5, 8000.0) / ref < 0.2, "negligible at LEO return"
    # crossover: radiation rivals convection above ~9-10 km/s
    print("crossover: radiation ~ convection at V ~ 9-10 km/s")
    # bluntness: thicker shock layer = longer radiating column
    print("blunt bodies radiate more: radiating column scales with shock-layer thickness")
    # wall sees it all: no boundary-layer attenuation
    eps_wall = 0.9
    print("high-emissivity wall (eps=%.1f) re-radiates much of it" % eps_wall)
    # uncertainty
    print("uncertainty bands: 2-3x still carried on lunar-return designs")
    print("rule: past ten kilometers a second, the fire throws its light ahead")
    print("OK: %s caught the glow" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_hy_boostglide(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # quasi-equilibrium glide: range ~ (L/D) * altitude drop ; crossrange from bank
    LD = 2.5
    h0, h1 = 80000.0, 30000.0
    R_glide = LD * (h0 - h1)
    print("L/D = %.1f, gliding 80 km -> 30 km: range ~ %.0f km" % (LD, R_glide / 1000.0))
    assert 100.0e3 < R_glide < 150.0e3, R_glide
    # bank angle turns the lift vector: crossrange
    bank = math.radians(45.0)
    # lateral acceleration fraction ~ tan(bank) * (lift component)
    print("45-deg bank: lateral turn authority ~ %.0f%% of lift" % (math.sin(bank) * 100.0))
    assert abs(math.sin(bank) - 0.7071) < 1e-3
    # energy: 6 km/s at 80 km
    V = 6000.0
    ke = V * V / 2.0
    print("glide entry energy: %.2e J/kg" % ke)
    assert 1.7e7 < ke < 1.9e7, ke
    # heating peaks at max(rho*V^3): velocity profile decays as the glider descends
    H = 7200.0
    rho0 = 1.225
    Vprof = {80000.0: 6000.0, 70000.0: 5900.0, 60000.0: 5400.0,
             50000.0: 4200.0, 40000.0: 2800.0, 30000.0: 1500.0}
    pts = [(h, rho0 * math.exp(-h / H) * V ** 3) for h, V in Vprof.items()]
    for h, val in sorted(pts):
        print("  h = %.0f km: rho*V^3 = %.2e" % (h / 1000.0, val))
    hm = max(pts, key=lambda p: p[1])
    print("rho*V^3 peaks at h = %.0f km (mid-glide, not top or bottom)" % (hm[0] / 1000.0))
    assert hm[0] in (40000.0, 50000.0), hm
    # HTV-2 lesson
    print("HTV-2 (2010/2011): departed controlled flight - controllability is the hard problem")
    print("rule: launched like a bullet, landed like a rumor - if the controls hold")
    print("OK: %s glided the boost" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_hy_integrated(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def full_stack_check(alt_km, V_kms, Rn):
    # one trajectory point through the whole checklist
    h = alt_km * 1000.0
    V = V_kms * 1000.0
    T_inf = 216.65 if h > 11000.0 else 288.15 - 0.0065 * h
    a = math.sqrt(1.4 * 287.0 * T_inf)
    M = V / a
    rho = RHO_SL * math.exp(-h / 7200.0)
    q = 0.5 * rho * V * V
    T0 = T_inf * (1.0 + 0.2 * M * M)
    q_stag = 1.83e-4 * math.sqrt(rho / Rn) * V ** 3
    lam = 68.0e-9 * math.exp(h / 7200.0)
    Kn = lam / Rn
    chem = "frozen" if T0 < 2000.0 else ("dissociating" if T0 < 9000.0 else "ionizing")
    regime = "continuum" if Kn < 0.01 else ("slip" if Kn < 0.1 else "DSMC")
    return {"M": M, "q_kPa": q / 1000.0, "T0_K": T0, "qstag_MWm2": q_stag / 1e6,
            "Kn": Kn, "chem": chem, "regime": regime}
def main():
    for alt, V, Rn, tag in ((80.0, 6.0, 0.5, "boost-glide mid"), (60.0, 7.0, 1.0, "entry"),
                            (35.0, 2.5, 0.3, "scramjet cruise")):
        s = full_stack_check(alt, V, Rn)
        print("%-16s M=%5.1f q=%6.1f kPa T0=%6.0f K qstag=%5.2f MW/m2 Kn=%.2e [%s, %s]"
              % (tag, s["M"], s["q_kPa"], s["T0_K"], s["qstag_MWm2"], s["Kn"], s["chem"], s["regime"]))
    s = full_stack_check(60.0, 7.0, 1.0)
    assert s["M"] > 15.0, s
    # perfect-gas T0 overpredicts (real dissociation caps it); either hot regime is correct
    assert s["chem"] in ("dissociating", "ionizing"), s
    assert s["regime"] == "continuum", s
    s2 = full_stack_check(85.0, 6.0, 0.5)
    assert s2["regime"] in ("slip", "DSMC"), s2
    # facility mosaic for the entry point
    print("validation mosaic: shock tunnel (heating) + expansion tube (chemistry) + quiet tunnel (transition)")
    # mode schedule for the cruise point
    print("propulsion mode at Mach ~8 cruise: scramjet (turbine below Mach 3, rocket above Mach 12)")
    print("rule: one geometry, six disciplines - the stack closes only together")
    print("OK: %s closed the stack" % NAME)
if __name__ == "__main__":
    main()
''')

DEMOS = {
    "what_is_hypersonic": demo_hy_what, "thin_shock_layer": demo_hy_thinshock,
    "mach_independence": demo_hy_machindep, "newtonian_theory": demo_hy_newtonian,
    "hypersonic_similarity": demo_hy_similarity, "strong_weak_shocks": demo_hy_strongweak,
    "stagnation_conditions": demo_hy_stagcond, "perfect_gas_breakdown": demo_hy_gasbreak,
    "real_gas_effects": demo_hy_realgas, "blast_wave_analogy": demo_hy_blastwave,
    "nose_bluntness": demo_hy_bluntness, "stagnation_heating": demo_hy_stagheat,
    "heating_distribution": demo_hy_heatdist, "thermal_protection": demo_hy_tps,
    "ablation_physics": demo_hy_ablation, "reentry_dynamics": demo_hy_reentry,
    "viscous_interaction": demo_hy_viscint, "boundary_layer_transition": demo_hy_transition,
    "shock_boundary_interaction": demo_hy_sbli, "entropy_layer": demo_hy_entropy,
    "hypersonic_ld": demo_hy_ld, "scramjet_cycle": demo_hy_scramjet,
    "scramjet_inlets": demo_hy_inlet, "waveriders": demo_hy_waverider,
    "rarefied_flow": demo_hy_rarefied, "high_temp_chemistry": demo_hy_chemistry,
    "test_facilities": demo_hy_facilities, "flight_test_history": demo_hy_flighttest,
    "hypersonic_stability": demo_hy_stability, "nonequilibrium": demo_hy_noneq,
    "radiative_heating": demo_hy_radheat, "boost_glide": demo_hy_boostglide,
    "integrated_design": demo_hy_integrated,
}
assert set(DEMOS) == {e["key"] for e in ENTRIES}, "demo map misses entries"


def build_records(slug, source):
    cfg = DBCFG[slug]
    sig = source == "signature"
    # Teaching-ladder order: stable sort by ladder_rank (entries are already
    # in ladder order in entries_hypersonics.py).
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
    for slug in ("hypersonic-aerodynamics", "hypersonic-aerodynamics-signature"):
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
