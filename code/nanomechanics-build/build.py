#!/usr/bin/env python3
"""Build the Nanomechanics field databases for JAH Databases (field #31, taxonomy order).

Verified 2026-10-17 (see entries_nanomechanics.py docstring): NO database
covers the nanomechanics discipline. Manifest search (2362 databases): zero
nanomechan* slugs/names; nearest neighbors are 'nanotech' (10,001 general
nanotechnology records), 'nanophotonics' (field #30: light-matter
interaction, not mechanics), 'nanosystems-engineers' and
'nanotechnology-engineering-technologists-and-technicians' (people/career
records), 'submicroscopic-phenomena-databases' (general phenomena),
materials-science and mechanical-engineering families (bulk/macroscale).
Whole-system title sweep over all 762 shard indexes (1,134,585 records):
nanomechanics discipline terms hit exactly 2 records - two general
tribology lubricant records in submicroscopic-phenomena-databases. ZERO
full-record discipline coverage anywhere.

So this build creates two NEW databases, 34 ladder-ordered records each,
covering ONLY what the system left uncovered (mechanical behavior at the
nanoscale):

  nanomechanics              - The Nanomechanics Database
                               (public-harvest: real, fact-checked
                               nanomechanics; standard references Bhushan
                               'Nanotribology and Nanomechanics', Cleland
                               'Foundations of Nanomechanics', Gerberich &
                               Michler 'Micro and Nanomechanical Testing',
                               Oliver & Pharr, JKR/DMT contact theory)
  nanomechanics-signature    - The Nanomechanics Signature Database
                               (his original Signature interpretation;
                               src signature, titles suffixed
                               " (Signature Edition)", never presented as
                               authentic public record)

34 records each, ordered by the teaching ladder (ladder_rank 1-10,
ladder_tier foundations/compounded/advanced); the shard index is written in
ladder order so pages present simple -> compounded -> complex.

Every record: description + how-it-works + key points + requirements +
standards + citations + working demonstration code (real, runnable,
stdlib-only Python; machine-executed OK). Nanomechanics demos: scale
ladder; surface-to-volume scaling; nanowire tension; continuum boundary;
Laplace pressure; van der Waals vs capillary; cantilever beam; Oliver-Pharr
pipeline; reduced modulus; WLC DNA stretching; Hall-Petch curve; nanotube
spring/resonance/breaking; graphene membrane inversion; friction loop +
Prandtl-Tomlinson; Hertz/JKR/DMT/Tabor; adhesion vs gravity; NEMS mass
responsivity; GHz nanotube resonator; Basquin S-N; Griffith fracture +
flaw tolerance; Lennard-Jones stiffness + Verlet energy check; in-situ TEM
strain rate; dislocation census + Frenkel ceiling; superelastic actuator
sizing; Gibson-Ashby nanolattice; Kelvin-Voigt creep + Deborah; Euler
buckling + wrinkling; Zener thermoelastic damping; piezoelectric charge +
flexoelectricity; Q vs pressure + immersion; zero-point motion + ground
state; full design-rule spec sheet; cell indentation.

Subtitle disambiguation (fields #13-30 pattern): specialty titles carry
teaching-focused subtitles rather than bare cards, e.g. "Nanoindentation:
Reading Hardness from a Force Curve".

Dedupe: whole-system gate (data/dedupe/exact/, covers through field #10)
PLUS a direct normalized-title cross-check against the shard indexes of
fields #11-30 (volcanology, climatology, atmospheric-science, hydrology,
meteorology, calculus, combinatorics, econometrics, psychometrics,
turbomachinery, electromagnetics, petroleum-refining, aerodynamics,
hypersonic-aerodynamics, aeroelasticity, petrophysics, tunneling,
microrobotics, actuators-sensors, nanophotonics + signatures), whose titles
postdate the gate index.

Never the words "bat belt" anywhere. No website references. No Facebook.
"""
import gzip
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
# main repo (covers through field #10). Fields #11-30 are cross-checked
# directly against their shard indexes (GAP_TITLES below).
sys.path.insert(0, os.path.join(REPO, "code"))
from dedupe_gate import DedupeGate
from build_global_dedupe import norm_title
base.GATE = DedupeGate(os.path.join(REPO, "data", "dedupe", "exact"))

sys.path.insert(0, HERE)
from entries_nanomechanics import ENTRIES, SIG_TAIL

# ---------------------------------------------------------------- gap titles
# Normalized titles from fields #11-30 shard indexes (postdate the gate).
GAP_SLUGS = [
    "volcanology", "volcanology-signature",
    "climatology", "climatology-signature",
    "atmospheric-science", "atmospheric-science-signature",
    "hydrology", "hydrology-signature",
    "meteorology", "meteorology-signature",
    "calculus", "calculus-signature",
    "combinatorics", "combinatorics-signature",
    "econometrics", "econometrics-signature",
    "psychometrics", "psychometrics-signature",
    "turbomachinery", "turbomachinery-signature",
    "electromagnetics", "electromagnetics-signature",
    "petroleum-refining", "petroleum-refining-signature",
    "aerodynamics", "aerodynamics-signature",
    "hypersonic-aerodynamics", "hypersonic-aerodynamics-signature",
    "aeroelasticity", "aeroelasticity-signature",
    "petrophysics", "petrophysics-signature",
    "tunneling", "tunneling-signature",
    "microrobotics", "microrobotics-signature",
    "actuators-sensors", "actuators-sensors-signature",
    "nanophotonics", "nanophotonics-signature",
]

def _load_gap_titles():
    titles = {}
    for slug in GAP_SLUGS:
        p = os.path.join(SHARD, "data", slug, "index.jsonl.gz")
        if not os.path.exists(p):
            print("  WARNING: gap index missing for %s" % slug, flush=True)
            continue
        with gzip.open(p, "rt", encoding="utf-8", errors="replace") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    r = json.loads(line)
                except ValueError:
                    continue
                t = r.get("t") or r.get("title") or ""
                nt = norm_title(t)
                if nt:
                    titles.setdefault(nt, []).append((slug, r.get("id")))
    return titles

GAP_TITLES = _load_gap_titles()
print("gap cross-check: %d normalized titles from %d field #11-30 databases"
      % (len(GAP_TITLES), len(GAP_SLUGS)), flush=True)

def _dedupe_refused(slug, title):
    if [h for h in base.GATE.check(slug, title) if h[0] != slug]:
        return "gate"
    if norm_title(title) in GAP_TITLES:
        return "gap"
    return None

# ---------------------------------------------------------------- DB config

def _cfg(slug, name, tagline, record_kind, prefix, ai, role, citation, source):
    sig_line = ("Signature originals - his original Signature interpretation of nanomechanics: "
                "clearly labeled Signature-made, never presented as authentic "
                "public record.")
    pub_line = ("Public records - real, fact-checked nanomechanics: what nanomechanics is; "
                "size effects; stress, strain, and modulus; the continuum boundary; surface "
                "energy and surface stress; van der Waals, capillary, and electrostatic "
                "forces; elastic nanobeams; nanoindentation; the Oliver-Pharr method; AFM "
                "force spectroscopy; nanowire tension; Hall-Petch and its breakdown; carbon "
                "nanotube mechanics; graphene mechanics; nanotribology; nanoscale contact "
                "mechanics (Hertz, JKR, DMT); adhesion and stiction; NEMS resonators; "
                "nanotube/nanowire GHz resonators; nanoscale fatigue; nanoscale fracture; "
                "molecular dynamics for mechanics; in-situ TEM testing; dislocation "
                "starvation plasticity; nanoscale superelasticity; nanolattices and "
                "mechanical metamaterials; nanoscale viscoelasticity; buckling and "
                "wrinkling; thermoelastic damping; electromechanical coupling; fluid "
                "damping; quantum limits of motion; nanomechanical design rules; "
                "nanobiomechanics, organized in the Signature system.")
    ladder = (" Records are ordered by the teaching ladder: Foundations (what nanomechanics "
              "is, size effects, stress/strain/modulus, the continuum boundary, surface "
              "energy, surface forces, elastic beams) -> Compounded (nanoindentation, "
              "Oliver-Pharr, AFM force spectroscopy, nanowire tension, Hall-Petch, "
              "nanotubes, graphene, nanotribology, contact mechanics, adhesion, NEMS) -> "
              "Advanced (GHz resonators, fatigue, fracture, molecular dynamics, in-situ "
              "TEM, dislocation-starved plasticity, superelasticity, nanolattices, "
              "viscoelasticity, buckling, thermoelastic damping, electromechanics, fluid "
              "damping, quantum limits, design rules, nanobiomechanics).")
    return {
        "name": name, "tagline": tagline, "record_kind": record_kind,
        "prefix": prefix, "ai": ai, "role": role,
        "hero_p": "%s - %s Every record carries the full entry: description, how it works, "
                  "key points, requirements, standards, citations, and a working demonstration "
                  "program.%s" % (tagline, sig_line if source == "signature" else pub_line, ladder),
        "sig_type": ("Signature originals organized in the Signature system"
                     if source == "signature" else
                     "Public records organized in the Signature system"),
        "search_ph": "Search nanoindentation, Hall-Petch, NEMS, nanotribology, JKR, resonators...",
        "chat_ph": "Ask about nanomechanics...",
        "archive_blurb": ("Seeded %s nanomechanics records, marching toward one million records. "
                          "Presented in teaching-ladder order: foundations, compounded, advanced."
                          % ("Signature-original" if source == "signature" else "public-record")),
        "schema": ("id, t, g, name, title, description, how_it_works, key_points, requirements, "
                   "standards, citations, src, ladder_rank, ladder_tier, demo"),
        "fields": "Foundations \u00b7 Compounded \u00b7 Advanced - each tier opens on demand and loads only what you open",
        "gen_desc": "Generate clearly-labeled nanomechanics studies. Seeded archive records are the authoritative entries.",
        "greet": "I am the %s. Ask me about nanomechanics - from what it is through size effects, stress and strain, the continuum boundary, surface energy and forces, elastic beams, nanoindentation, the Oliver-Pharr method, AFM force spectroscopy, nanowire tension, Hall-Petch, nanotubes, graphene, nanotribology, contact mechanics, adhesion, NEMS resonators, GHz resonators, fatigue, fracture, molecular dynamics, in-situ TEM, dislocation-starved plasticity, superelasticity, nanolattices, viscoelasticity, buckling, thermoelastic damping, electromechanics, fluid damping, quantum limits, design rules, and nanobiomechanics." % ai,
        "gen_fields": ["Foundations", "Compounded", "Advanced"],
        "gen_kind": "nanomechanics-study", "gen_demo_kind": "nanomechanics-demo",
        "source": source,
    }

CIT_PUB = ("Nanomechanics (standard texts: Bhushan 'Nanotribology and Nanomechanics: An "
           "Introduction' 4th ed. 2017; Cleland 'Foundations of Nanomechanics' 2003; "
           "Gerberich & Michler (eds.) 'Micro and Nanomechanical Testing of Materials "
           "and Devices' 2008; Bhushan (ed.) 'Springer Handbook of Nanotechnology' 4th "
           "ed. 2017; Oliver & Pharr, J. Mater. Res. 7, 1564-1583 (1992) and 19, 3-20 "
           "(2004); Johnson, Kendall & Roberts, Proc. R. Soc. A 324, 301-313 (1971); "
           "Derjaguin, Muller & Toporov, J. Colloid Interface Sci. 53, 314-326 (1975); "
           "Hertz, J. reine angew. Math. 92, 156-171 (1882); Griffith, Phil. Trans. "
           "R. Soc. A 221, 163-198 (1921); Hall, Proc. Phys. Soc. B 64, 747-753 "
           "(1951); Petch, J. Iron Steel Inst. 174, 25-28 (1953); Israelachvili "
           "'Intermolecular and Surface Forces' 3rd ed. 2011; Landau & Lifshitz "
           "'Theory of Elasticity' 3rd ed. 1986; Ekinci & Roukes, Rev. Sci. Instrum. "
           "76, 061101 (2005); Schmid, Villanueva & Roukes 'Fundamentals of "
           "Nanomechanical Resonators' 2016).")
CIT_SIG = CIT_PUB + " " + SIG_TAIL

DBCFG = {}
DBCFG["nanomechanics"] = _cfg(
    "nanomechanics", "The Nanomechanics Database",
    "Real, fact-checked nanomechanics: from what nanomechanics is through size effects, "
    "stress and strain, the continuum boundary, surface energy and surface forces, and "
    "elastic nanobeams, through nanoindentation, the Oliver-Pharr method, AFM force "
    "spectroscopy, nanowire tension, Hall-Petch and its breakdown, nanotubes, graphene, "
    "nanotribology, contact mechanics, adhesion, and NEMS resonators, to GHz resonators, "
    "fatigue, fracture, molecular dynamics, in-situ TEM, dislocation-starved plasticity, "
    "superelasticity, nanolattices, viscoelasticity, buckling, thermoelastic damping, "
    "electromechanics, fluid damping, quantum limits, design rules, and nanobiomechanics "
    "- taught progressively along the ladder.",
    "nanomechanics record", "JAH-NMH-", "JAH Nanomechanics Archivist",
    "nanomechanics archivist - mechanical behavior at the nanoscale: size effects, "
    "stress/strain/modulus, continuum boundary, surface energy and forces, elastic "
    "beams, nanoindentation, Oliver-Pharr, AFM force spectroscopy, nanowire tension, "
    "Hall-Petch, nanotubes, graphene, nanotribology, Hertz/JKR/DMT contact, adhesion, "
    "NEMS, GHz resonators, fatigue, fracture, molecular dynamics, in-situ TEM, "
    "dislocation-starved plasticity, superelasticity, nanolattices, viscoelasticity, "
    "buckling, thermoelastic damping, electromechanics, fluid damping, quantum limits, "
    "design rules, nanobiomechanics; teaching progressively along the ladder from "
    "foundations through compounded to advanced; answers from many angles - definition, "
    "example, analogy, application, history, math, how-to - using only the system's "
    "own archive data",
    CIT_PUB, "public")
DBCFG["nanomechanics-signature"] = _cfg(
    "nanomechanics-signature", "The Nanomechanics Signature Database",
    "His original Signature interpretation of nanomechanics: the full ladder from what "
    "nanomechanics is through size effects, stress, surfaces, beams, indentation, wires, "
    "tubes, friction, contact, resonators, fracture, simulation, plasticity, lattices, "
    "damping, quantum limits, and design, reframed as Signature science. Clearly "
    "labeled Signature-made, never presented as authentic public record.",
    "nanomechanics record", "JAH-NMS-", "JAH Nanomechanics Archivist (Signature)",
    "nanomechanics archivist - Signature editions: his original Signature "
    "interpretation of nanomechanics, clearly labeled Signature-made and "
    "never presented as authentic public record; teaches progressively along the "
    "ladder from foundations through compounded to advanced; answers from many "
    "angles - definition, example, analogy, application, history, math, how-to - "
    "using only the system's own archive data",
    CIT_SIG, "signature")

base.DBCFG = DBCFG

# ---------------------------------------------------------------- demos
# Every demo is real, runnable, stdlib-only Python performing the actual
# nanomechanics computation for its record. All are machine-executed by main().

_PREAMBLE = (
"import math\n"
)

def _wrap(name, rid, group, body):
    return (base._hdr(name, rid, group) + _PREAMBLE + body.replace("NAME", json.dumps(name)))

def demo_nm_what_is(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # the scale ladder: atoms across a feature, surface share of a cube
    atom_d = 0.25                       # nm, typical atomic diameter
    feature = 100.0                     # nm
    atoms_across = feature / atom_d
    def sav(L):
        return 6.0 / L                 # surface-to-volume of a cube, 1/m
    sv_cm = sav(0.01)
    sv_10nm = sav(10e-9)
    # fraction of atoms within one atomic layer of the surface (10 nm cube)
    L_nm, shell = 10.0, atom_d
    surf_frac = (L_nm**3 - (L_nm - 2.0 * shell) ** 3) / L_nm**3
    print("a 100 nm feature spans %.0f atoms" % atoms_across)
    print("surface-to-volume: 1 cm cube %.0f /m; 10 nm cube %.1e /m" % (sv_cm, sv_10nm))
    print("ratio: %.0e - the surface takes over" % (sv_10nm / sv_cm))
    print("atoms within one layer of the surface (10 nm cube): %.1f%%" % (surf_frac * 100))
    assert atoms_across == 400.0
    assert sv_cm == 600.0 and abs(sv_10nm - 6e8) < 1.0
    assert sv_10nm / sv_cm == 1e6
    assert 0.13 < surf_frac < 0.16, surf_frac
    print("rule: shrink the object and the surface becomes the object")
    print("OK: %s walked the scale ladder" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_nm_scale_effects(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # surface-to-volume and surface-atom fraction down the size ladder
    a = 0.25                            # nm, atomic diameter
    print("   L        SA/V (1/m)   ~surface-atom fraction")
    for L_nm in (1e9, 1e6, 1e3, 100.0, 10.0, 1.0):
        L = L_nm * 1e-9
        sv = 6.0 / L
        frac = min(6.0 * a / L_nm, 1.0)
        print("   %-8g %-12.3g %s" % (L_nm, sv,
              "essentially every atom" if frac >= 1.0 else "%.2f" % frac))
    assert 6.0 / 1e-3 == 6000.0
    assert 6.0 / 10e-9 == 6e8
    # strength scaling: nanopillars sigma ~ d^-0.6 anchored at 100 MPa @ 10 um
    def sigma(d):
        return 100.0 * (d / 10e-6) ** -0.6     # MPa
    s100nm = sigma(100e-9)
    print("Au pillar strength model: 10 um -> 100 MPa; 100 nm -> %.0f MPa" % s100nm)
    assert 1400.0 < s100nm < 1600.0, s100nm
    print("rule: the surface fraction is the size effect you can compute on a napkin")
    print("OK: %s scaled the world down" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_nm_stress_strain(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # pull a steel nanowire: stress, strain, elongation, and the unit mnemonic
    d, L, F = 100e-9, 10e-6, 1e-6      # m, m, N
    E = 200e9                            # Pa, steel
    A = math.pi * (d / 2.0) ** 2
    sigma = F / A
    eps = sigma / E
    elong = eps * L
    print("area: %.3e m^2" % A)
    print("stress: %.1f MPa" % (sigma / 1e6))
    print("strain: %.3e" % eps)
    print("elongation of 10 um wire: %.2f nm" % (elong * 1e9))
    print("mnemonic check: 1 nN on 1 nm^2 = %.0f GPa" % (1e-9 / 1e-18 / 1e9))
    assert abs(sigma / 1e6 - 127.32) < 0.1, sigma
    assert abs(elong * 1e9 - 6.37) < 0.05, elong
    assert 1e-9 / 1e-18 == 1e9
    print("rule: modulus is the bonds'; strength is the flaws' - know which you measure")
    print("OK: %s pulled the wire" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_nm_continuum_breakdown(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # atoms across a feature; surface fraction; the 10 nm boundary
    a = 0.25
    for feat in (100.0, 10.0, 5.0, 2.0, 1.0):
        n = feat / a
        inner = max(feat - 2.0 * a, 0.0)
        frac = (feat**3 - inner**3) / feat**3 if feat else 1.0
        verdict = "continuum OK" if feat >= 10.0 else ("bridge zone" if feat >= 5.0 else "ATOMISTIC ONLY")
        print("%6.1f nm: %5.0f atoms across, surface fraction %.2f -> %s" % (feat, n, frac, verdict))
    assert 100.0 / a == 400.0 and 10.0 / a == 40.0 and 1.0 / a == 4.0
    frac10 = (10.0**3 - 9.5**3) / 10.0**3
    assert abs(frac10 - 0.1426) < 0.002, frac10
    print("rule: forty atoms across is a continuum; four atoms across is a molecule")
    print("OK: %s found the boundary" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_nm_surface_energy(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # Laplace pressure 2*gamma/R: the self-squeeze of small things
    def laplace(gamma, R):
        return 2.0 * gamma / R
    p_au10 = laplace(1.5, 10e-9)
    p_au5 = laplace(1.5, 5e-9)
    p_water = laplace(0.072, 100e-9)
    print("Au particle R=10 nm: %.0f MPa of self-pressure" % (p_au10 / 1e6))
    print("Au particle R=5 nm:  %.0f MPa" % (p_au5 / 1e6))
    print("water droplet R=100 nm: %.2f MPa" % (p_water / 1e6))
    assert abs(p_au10 - 3e8) < 1e6, p_au10
    assert abs(p_au5 - 6e8) < 1e6, p_au5
    assert abs(p_water - 1.44e6) < 1e4, p_water
    print("rule: 1/R is a tyrant - halve the radius, double the squeeze")
    print("OK: %s felt the squeeze" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_nm_surface_forces(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # van der Waals vs capillary for a 10 nm tip: the humidity verdict
    A_ham, R, D = 6.5e-20, 10e-9, 0.5e-9
    F_vdw = A_ham * R / (6.0 * D ** 2)        # sphere-plate
    gamma = 0.072
    F_cap = 4.0 * math.pi * R * gamma          # water meniscus
    print("van der Waals pull: %.0f pN" % (F_vdw * 1e12))
    print("capillary pull:     %.2f nN" % (F_cap * 1e9))
    print("capillary wins by %.1fx - dry the air or lose" % (F_cap / F_vdw))
    assert 430.0 < F_vdw * 1e12 < 437.0, F_vdw
    assert 9.0 < F_cap * 1e9 < 9.1, F_cap
    assert 20.0 < F_cap / F_vdw < 22.0
    # electrostatic: 1 V across a 10 nm gap, plate 1 um^2
    V, gap, area = 1.0, 10e-9, 1e-12
    F_el = 8.854e-12 * area * V ** 2 / (2.0 * gap ** 2)
    print("electrostatic (1 V, 10 nm gap, 1 um^2): %.1f nN - the long-range actor" % (F_el * 1e9))
    assert 43.0 < F_el * 1e9 < 46.0, F_el
    print("rule: at the nanoscale the 'empty' gap is the most crowded place")
    print("OK: %s weighed the invisible hands" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_nm_elastic_beams(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # the reference silicon cantilever: 10 x 1 x 0.1 um
    E, rho = 169e9, 2330.0
    L, w, t = 10e-6, 1e-6, 100e-9
    I = w * t ** 3 / 12.0
    k = 3.0 * E * I / L ** 3
    m = rho * L * w * t
    m_eff = 0.24 * m
    f = (1.0 / (2.0 * math.pi)) * math.sqrt(k / m_eff)
    delta = 1e-9 / k                        # 1 nN load
    print("stiffness k = %.4f N/m" % k)
    print("resonance f = %.2f MHz" % (f / 1e6))
    print("1 nN bends the tip %.1f nm" % (delta * 1e9))
    assert abs(k - 0.04225) < 0.0005, k
    assert 1.35 < f / 1e6 < 1.42, f
    assert abs(delta * 1e9 - 23.7) < 0.3, delta
    # scaling check: halve the length -> 8x stiffness
    k2 = 3.0 * E * I / (L / 2.0) ** 3
    assert abs(k2 / k - 8.0) < 1e-9
    print("halve the length: stiffness x%.0f - the 1/L^3 law" % (k2 / k))
    print("rule: the cantilever is the finger; calibrate the finger")
    print("OK: %s bent the beam" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_nm_nanoindentation(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # Oliver-Pharr pipeline on a synthetic 500 uN curve
    P_max = 500e-6
    h_max = 100e-9
    S = 150e-6 / 1e-9                    # 150 uN/nm -> N/m
    eps, beta = 0.75, 1.034
    h_c = h_max - eps * P_max / S
    A = 24.5 * h_c ** 2                  # ideal Berkovich, m^2
    H = P_max / A
    E_r = (math.sqrt(math.pi) / (2.0 * beta)) * S / math.sqrt(A)
    print("contact depth h_c = %.1f nm" % (h_c * 1e9))
    print("hardness H = %.2f GPa" % (H / 1e9))
    print("reduced modulus E_r = %.0f GPa" % (E_r / 1e9))
    assert abs(h_c * 1e9 - 97.5) < 0.05, h_c
    assert abs(H / 1e9 - 2.15) < 0.03, H
    assert abs(E_r / 1e9 - 266.0) < 2.0, E_r
    print("rule: the unloading slope is pure elasticity - trust the retreat")
    print("OK: %s reduced the curve" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_nm_oliver_pharr(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # worked example: S = 200 uN/nm, h_c = 80 nm -> E_r -> E
    S = 200e-6 / 1e-9
    h_c = 80e-9
    beta = 1.034
    A = 24.5 * h_c ** 2
    E_r = math.sqrt(math.pi) * S / (2.0 * beta * math.sqrt(A))
    nu = 0.3
    E_i, nu_i = 1141e9, 0.07               # diamond indenter
    inv_E = 1.0 / E_r - (1.0 - nu_i ** 2) / E_i
    E = (1.0 - nu ** 2) / inv_E
    print("E_r = %.1f GPa" % (E_r / 1e9))
    print("E (nu=0.3) = %.0f GPa" % (E / 1e9))
    assert abs(E_r / 1e9 - 432.9) < 1.0, E_r
    assert abs(E / 1e9 - 633.0) < 3.0, E
    # sensitivity: 5% in h_c -> ~10% in modulus (area ~ h_c^2)
    A2 = 24.5 * (h_c * 1.05) ** 2
    E_r2 = math.sqrt(math.pi) * S / (2.0 * beta * math.sqrt(A2))
    print("5%% deeper contact -> E_r drops %.1f%%: depth calibration is king" % ((1 - E_r2 / E_r) * 100))
    assert 4.5 < (1 - E_r2 / E_r) * 100 < 5.0
    print("rule: fit the top of the unload, calibrate the depth, state the nu")
    print("OK: %s ran the standard" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_nm_afm_mechanics(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # worm-like-chain stretching of DNA: Lp = 50 nm, L = 1000 nm
    kT = 4.114                              # pN*nm at 298 K
    Lp, L = 50.0, 1000.0                    # nm
    def F_wlc(x_over_L):
        x = x_over_L
        return (kT / Lp) * (1.0 / (4.0 * (1.0 - x) ** 2) - 0.25 + x)
    F90 = F_wlc(0.90)
    F99 = F_wlc(0.99)
    print("DNA at 90%% extension: %.2f pN" % F90)
    print("DNA at 99%% extension: %.1f pN" % F99)
    print("stiffening factor: %.0fx over the last 9%% of stretch" % (F99 / F90))
    assert abs(F90 - 2.11) < 0.03, F90
    assert abs(F99 - 205.8) < 1.0, F99
    assert F99 / F90 > 90.0
    print("rule: entropy is a spring that hardens as it straightens")
    print("OK: %s stretched the molecule" % NAME)
if __name__ == "__main__":
    main()
''')
def demo_nm_nanowires(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # gold nanowire in tension: d = 100 nm, L = 2 um, breaks at 1.5 GPa
    d, L = 100e-9, 2e-6
    E = 79e9
    sigma_break = 1.5e9
    A = math.pi * (d / 2.0) ** 2
    F_break = sigma_break * A
    eps_break = sigma_break / E
    elong = eps_break * L
    bulk = 120e6
    print("breaking force: %.2f uN" % (F_break * 1e6))
    print("breaking strain: %.2f%%" % (eps_break * 100))
    print("elongation: %.1f nm" % (elong * 1e9))
    print("stronger than bulk gold by %.1fx" % (sigma_break / bulk))
    assert abs(F_break * 1e6 - 11.78) < 0.05, F_break
    assert abs(elong * 1e9 - 38.0) < 0.3, elong
    assert abs(sigma_break / bulk - 12.5) < 0.05
    print("ideal ceiling E/10 = %.1f GPa: this wire reached %.0f%% of it"
          % (E / 10.0 / 1e9, sigma_break / (E / 10.0) * 100))
    print("rule: remove the flaws, meet the bonds")
    print("OK: %s broke the wire" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_nm_hall_petch(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # Hall-Petch for copper + the breakdown below ~15 nm
    sigma0, k = 25.0, 0.14               # MPa, MPa*m^0.5
    def hp(d):
        return sigma0 + k / math.sqrt(d)
    pts = ((10e-6, 69.3), (1e-6, 165.0), (100e-9, 467.7), (10e-9, 1425.0))
    print(" grain size -> Hall-Petch strength")
    for d, expect in pts:
        s = hp(d)
        flag = " <- BREAKDOWN ZONE (real metal softens here)" if d <= 15e-9 else ""
        print(" %8s -> %7.1f MPa%s" % ("%.0f nm" % (d * 1e9) if d < 1e-6 else "%.0f um" % (d * 1e6), s, flag))
        assert abs(s - expect) < 2.0, (d, s)
    print("peak strength sits near 10-15 nm grains: nanocrystalline is an optimum")
    print("rule: every strengthening law has a scale where it inverts")
    print("OK: %s mapped the peak" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_nm_nanotubes(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # single-wall tube d = 1.4 nm, t = 0.34 nm, E = 1 TPa, L = 1 um
    E = 1e12
    d, t, L = 1.4e-9, 0.34e-9, 1e-6
    r = d / 2.0
    A = math.pi * d * t
    I = math.pi * r ** 3 * t
    k_axial = E * A / L
    rho = 1350.0
    f_cant = (1.875 ** 2 / (2.0 * math.pi * L ** 2)) * math.sqrt(E * I / (rho * A))
    F_break = 100e9 * A                    # 100 GPa tensile strength
    print("cross-section: %.3e m^2 (a million times thinner than hair)" % A)
    print("axial stiffness: %.2f N/m - a soft spring of the stiffest stuff" % k_axial)
    print("cantilever resonance: %.2f MHz" % (f_cant / 1e6))
    print("breaking force at 100 GPa: %.0f nN" % (F_break * 1e9))
    assert abs(k_axial - 1.50) < 0.03, k_axial
    assert 7.4 < f_cant / 1e6 < 7.7, f_cant
    assert abs(F_break * 1e9 - 149.5) < 1.0, F_break
    print("rule: 1 TPa material, 1.5 N/m spring - geometry is destiny")
    print("OK: %s loaded the tube" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_nm_graphene(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # invert Lee et al.'s membrane indentation: cubic coefficient -> E_2D -> E_3D
    C = 1.44e15                            # N/m^3, measured cubic coefficient
    a = 500e-9
    q = 1.02
    E_2D = C * a ** 2 / q ** 3
    t_graphene = 0.335e-9
    E_3D = E_2D / t_graphene
    print("E_2D = %.0f N/m" % E_2D)
    print("E_3D = %.2f TPa (via 0.335 nm thickness)" % (E_3D / 1e12))
    assert 336.0 < E_2D < 343.0, E_2D
    assert 1.0 < E_3D / 1e12 < 1.03, E_3D
    # breaking: 42 N/m line force
    sigma_2D_break = 42.0
    print("intrinsic strength 42 N/m = %.0f GPa in 3D units" % (sigma_2D_break / t_graphene / 1e9))
    assert abs(sigma_2D_break / t_graphene / 1e9 - 125.4) < 1.0
    print("rule: for one atom, N/m is the honest unit")
    print("OK: %s pressed the membrane" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_nm_nanotribology(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # friction loop reduction + Prandtl-Tomlinson slip force
    F_fwd, F_rev = 60e-9, -58e-9
    load = 100e-9
    F_f = (F_fwd - F_rev) / 2.0
    mu = F_f / load
    print("friction force: %.0f nN at %.0f nN load -> mu = %.2f" % (F_f * 1e9, load * 1e9, mu))
    assert abs(F_f * 1e9 - 59.0) < 0.5, F_f
    assert abs(mu - 0.59) < 0.01, mu
    # atomic stick-slip: barrier 0.1 eV, lattice 0.25 nm
    U0 = 0.1 * 1.602176634e-19
    a = 0.25e-9
    F_max = 2.0 * math.pi * U0 / a
    print("Prandtl-Tomlinson slip force: %.2f nN per atomic snap" % (F_max * 1e9))
    assert 0.39 < F_max * 1e9 < 0.42, F_max
    print("~%.0e stick-slip events per second at a 1 um/s scan" % (1e-6 / a))
    print("rule: friction is a negotiation, conducted one atomic snap at a time")
    print("OK: %s slid the tip" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_nm_contact_mechanics(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # Si tip R = 50 nm on Si at P = 100 nN: Hertz, pull-offs, Tabor map
    E, nu = 169e9, 0.22
    E_star = 1.0 / (2.0 * (1.0 - nu ** 2) / E)
    R, P = 50e-9, 100e-9
    a = (3.0 * P * R / (4.0 * E_star)) ** (1.0 / 3.0)
    p_mean = P / (math.pi * a ** 2)
    w = 0.1
    F_jkr = 1.5 * math.pi * w * R
    F_dmt = 2.0 * math.pi * w * R
    print("Hertz radius a = %.2f nm, mean pressure %.2f GPa" % (a * 1e9, p_mean / 1e9))
    print("JKR pull-off %.1f nN vs DMT pull-off %.1f nN" % (F_jkr * 1e9, F_dmt * 1e9))
    assert abs(a * 1e9 - 3.48) < 0.05, a
    assert abs(p_mean / 1e9 - 2.63) < 0.05, p_mean
    assert abs(F_jkr * 1e9 - 23.6) < 0.2 and abs(F_dmt * 1e9 - 31.4) < 0.2
    # Tabor parameter: which theory judges?
    z0 = 0.3e-9
    w2 = 0.05
    def tabor(Rt):
        return (Rt * w2 ** 2 / (E_star ** 2 * z0 ** 3)) ** (1.0 / 3.0)
    mu_small, mu_big = tabor(10e-9), tabor(100e-6)
    print("Tabor: R=10 nm -> %.3f (DMT territory); R=100 um -> %.2f (JKR territory)"
          % (mu_small, mu_big))
    assert 0.045 < mu_small < 0.055, mu_small
    assert 1.0 < mu_big < 1.12, mu_big
    print("rule: pick the referee before arguing the contact")
    print("OK: %s touched down" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_nm_adhesion(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # JKR pull-off vs radius; adhesion-to-weight ratio; the crossover
    w = 0.1
    rho, g = 2500.0, 9.81
    print(" radius      pull-off      adhesion/weight")
    for R in (10e-9, 50e-9, 1e-6, 100e-6):
        F = 1.5 * math.pi * w * R
        W = (4.0 / 3.0) * math.pi * R ** 3 * rho * g
        unit = "nN" if F < 1e-6 else "uN"
        val = F * 1e9 if F < 1e-6 else F * 1e6
        print(" %-10s  %7.2f %-2s   %.2g" % ("%.0f nm" % (R * 1e9) if R < 1e-6 else "%.0f um" % (R * 1e6),
                                             val, unit, F / W))
    assert abs(1.5 * math.pi * w * 50e-9 * 1e9 - 23.6) < 0.2
    R_cross = math.sqrt(9.0 * w / (8.0 * rho * g))     # adhesion = weight, ideal smooth
    print("ideal-smooth crossover (adhesion = weight): %.1f mm" % (R_cross * 1e3))
    print("roughness drags the real crossover to tens of microns: dust sticks")
    assert 2.0 < R_cross * 1e3 < 2.3, R_cross
    print("rule: below the crossover, nothing falls - everything sticks")
    print("OK: %s paid the surface debt" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_nm_nems(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # NEMS mass balance: 5 x 0.5 x 0.1 um Si beam at 10 MHz
    rho = 2330.0
    L, w, t = 5e-6, 0.5e-6, 100e-9
    f0 = 10e6
    m = rho * L * w * t
    m_eff = 0.396 * m                        # doubly-clamped
    R = f0 / (2.0 * m_eff)                   # Hz/kg responsivity
    dalton = 1.6605390666e-27
    m_protein = 100e3 * dalton
    df = R * m_protein
    m_min = 1.0 / R                          # 1 Hz noise floor
    print("beam mass: %.2e kg" % m)
    print("responsivity R = %.2e Hz/kg" % R)
    print("100 kDa protein shifts f by %.2f Hz" % df)
    print("mass floor at 1 Hz noise: %.2e kg (%.0f kDa)" % (m_min, m_min / (1e3 * dalton)))
    assert abs(R - 2.17e22) / 2.17e22 < 0.02, R
    assert abs(df - 3.60) < 0.05, df
    assert abs(m_min - 4.61e-23) / 4.61e-23 < 0.02, m_min
    print("rule: the beam sings flat when a ghost lands - read the hertz")
    print("OK: %s weighed the ghost" % NAME)
if __name__ == "__main__":
    main()
''')
def demo_nm_nanotube_resonance(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # doubly-clamped SWCNT, L = 200 nm: gigahertz tuning fork
    E = 1e12
    d, t = 1.4e-9, 0.34e-9
    r = d / 2.0
    A = math.pi * d * t
    I = math.pi * r ** 3 * t
    rho = 1350.0
    L = 200e-9
    beta = 4.7300408
    f0 = (beta ** 2 / (2.0 * math.pi * L ** 2)) * math.sqrt(E * I / (rho * A))
    print("first-mode resonance: %.2f GHz" % (f0 / 1e9))
    assert 1.19 < f0 / 1e9 < 1.21, f0
    # gate-voltage tension tuning: the guitar-string effect
    print(" tension -> frequency (gate tuning)")
    for T in (0.0, 0.3e-9, 1e-9, 3e-9):
        f = f0 * math.sqrt(1.0 + T * L ** 2 / (math.pi ** 2 * E * I))
        print(" %5.1f nN -> %.2f GHz" % (T * 1e9, f / 1e9))
    f_1nN = f0 * math.sqrt(1.0 + 1e-9 * L ** 2 / (math.pi ** 2 * E * I))
    assert 4.1 < f_1nN / 1e9 < 4.25, f_1nN
    print("rule: tension is the tuning peg of the nanoworld")
    print("OK: %s rang the tube" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_nm_fatigue_nano(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # Basquin S-N for a gold nanowire: sigma_f' = 2 GPa, b = -0.1
    sig_f, b = 2000.0, -0.1               # MPa
    def S_N(N):
        return sig_f * (2.0 * N) ** b
    print(" cycles -> allowable stress amplitude")
    for N in (1e3, 1e6, 1e9, 1e12):
        print(" %8.0e -> %6.0f MPa" % (N, S_N(N)))
    assert abs(S_N(1e6) - 468.8) < 1.0, S_N(1e6)
    assert abs(S_N(1e9) - 234.8) < 1.0, S_N(1e9)
    # invert: life at 300 MPa
    N_life = 0.5 * (300.0 / sig_f) ** (1.0 / b)
    print("at 300 MPa: %.2e cycles to failure" % N_life)
    print("  = %.1f minutes at 70 MHz; %.1f days at 1 kHz" % (N_life / 70e6 / 60.0, N_life / 1e3 / 86400.0))
    assert 8.5e7 < N_life < 8.8e7, N_life
    print("rule: static strength is a boast; the S-N curve is the biography")
    print("OK: %s cycled to failure" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_nm_fracture_nano(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # Griffith curve for glass + the flaw-tolerance threshold
    E, gamma = 70e9, 1.0
    sigma_th = E / 10.0
    def griffith(a):
        return math.sqrt(2.0 * E * gamma / (math.pi * a))
    print(" flaw size -> Griffith strength")
    for a, expect in ((1e-6, 211.1), (100e-9, 667.5), (10e-9, 2111.0), (1e-9, 6675.0)):
        s = griffith(a)
        capped = min(s, sigma_th)
        print(" %7s -> %8.0f MPa%s" % ("%g nm" % (a * 1e9), capped / 1e6,
                                       " (capped at theoretical)" if s > sigma_th else ""))
        assert abs(s / 1e6 - expect) < 3.0, (a, s)
    a_c = 2.0 * E * gamma / (math.pi * sigma_th ** 2)
    print("flaw-tolerance threshold a_c = %.2f nm: smaller flaws cannot weaken it" % (a_c * 1e9))
    assert abs(a_c * 1e9 - 0.909) < 0.01, a_c
    print("rule: read Griffith backwards - small flaws retire")
    print("OK: %s broke it honestly" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_nm_md_mechanics(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # Lennard-Jones argon: bond stiffness -> modulus estimate; Verlet honesty check
    eps = 119.8 * 1.380649e-23            # J
    sigma = 3.405e-10                     # m
    k = 57.1 * eps / sigma ** 2           # d2U/dr2 at minimum, N/m
    r0 = 2.0 ** (1.0 / 6.0) * sigma
    E_est = k / r0
    m_ar = 39.948 * 1.6605390666e-27
    omega = math.sqrt(k / m_ar)
    f_vib = omega / (2.0 * math.pi)
    print("bond stiffness k = %.3f N/m" % k)
    print("modulus estimate k/r0 = %.2f GPa (measured solid Ar: 2-3 GPa)" % (E_est / 1e9))
    print("bond vibration: %.3f THz" % (f_vib / 1e12))
    assert abs(k - 0.815) < 0.005, k
    assert abs(E_est / 1e9 - 2.13) < 0.05, E_est
    assert abs(f_vib / 1e12 - 0.558) < 0.005, f_vib
    # velocity-Verlet on a harmonic oscillator: energy must not drift
    dt, n = 1e-15, 2000
    x, v, m, kk = 1e-11, 0.0, m_ar, k
    a = -kk * x / m
    E0 = 0.5 * m * v ** 2 + 0.5 * kk * x ** 2
    Emax_dev = 0.0
    for _ in range(n):
        x += v * dt + 0.5 * a * dt ** 2
        a_new = -kk * x / m
        v += 0.5 * (a + a_new) * dt
        a = a_new
        E = 0.5 * m * v ** 2 + 0.5 * kk * x ** 2
        Emax_dev = max(Emax_dev, abs(E - E0) / E0)
    print("Verlet energy drift over %d steps: %.2e (relative)" % (n, Emax_dev))
    assert Emax_dev < 1e-4, Emax_dev
    print("rule: the potential is the physics; energy conservation is the receipt")
    print("OK: %s integrated the atoms" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_nm_insitu_tem(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # reduce a synthetic 5-frame in-situ tensile test
    d = 100e-9
    A = math.pi * (d / 2.0) ** 2
    L0 = 2e-6
    frames = [                            # (time_s, load_uN, elongation_nm)
        (0.0, 0.0, 0.0),
        (15.0, 3.0, 9.7),
        (30.0, 6.0, 19.4),
        (45.0, 9.0, 29.0),
        (60.0, 11.78, 38.0),
    ]
    print("  t(s)  load(uN)  stress(GPa)  strain(%%)")
    stresses = []
    for t, FuN, dnm in frames:
        sig = FuN * 1e-6 / A
        eps = dnm * 1e-9 / L0
        stresses.append(sig)
        print(" %5.0f  %7.2f    %6.2f      %.2f" % (t, FuN, sig / 1e9, eps * 100))
    rate = ((38.0e-9 / L0) - 0.0) / 60.0
    E_fit = (stresses[-1] - stresses[1]) / ((38.0e-9 - 9.7e-9) / L0)
    print("strain rate: %.2e /s" % rate)
    print("modulus from frames 2-5: %.0f GPa" % (E_fit / 1e9))
    assert abs(rate - 3.17e-4) < 0.05e-4, rate
    assert abs(stresses[-1] / 1e9 - 1.50) < 0.02, stresses[-1]
    assert 70.0 < E_fit / 1e9 < 90.0, E_fit
    print("rule: every stress point gets a microstructure photograph")
    print("OK: %s filmed the pull" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_nm_plasticity(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # dislocation census: 200 nm Au pillar vs 1 mm^3 bulk
    rho_d = 1e12                            # dislocation line length per volume, 1/m^2
    d, h = 200e-9, 400e-9
    A_cross = math.pi * (d / 2.0) ** 2
    N_pillar = rho_d * A_cross               # dislocation lines threading the cross-section
    N_bulk = rho_d * 1e-6                    # threading a 1 mm^2 bulk face
    G = 27e9
    tau_frenkel = G / (2.0 * math.pi)
    print("dislocations threading the pillar: %.3f -> STARVATION" % N_pillar)
    print("dislocations threading 1 mm^2 of bulk: %.0f -> forest" % N_bulk)
    print("Frenkel ideal shear strength: %.2f GPa" % (tau_frenkel / 1e9))
    assert abs(N_pillar - 0.0314) < 0.001, N_pillar
    assert N_bulk == 1e6
    assert abs(tau_frenkel / 1e9 - 4.30) < 0.02, tau_frenkel
    # size scaling of source stress: tau ~ G*b/lambda, lambda ~ d
    b = 0.288e-9
    for dd in (1000e-9, 200e-9, 50e-9):
        tau_src = G * b / dd / 1e9
        print("  source stress at d=%4.0f nm: %.2f GPa" % (dd * 1e9, tau_src))
    print("rule: N << 1 dislocations means nucleation writes the rules")
    print("OK: %s counted the defects" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_nm_superelasticity(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # NiTi nanowire actuator sizing: plateau, stroke, damping
    d, L = 100e-9, 2e-6
    sigma_p = 500e6
    loop_width = 200e6
    eps_tr = 0.06
    A = math.pi * (d / 2.0) ** 2
    V = A * L
    stroke = eps_tr * L
    F_act = sigma_p * A
    W_cycle = loop_width * eps_tr            # J/m^3 per cycle
    E_diss = W_cycle * V
    print("recoverable stroke: %.0f nm on a 2 um wire (%.0f%%)" % (stroke * 1e9, eps_tr * 100))
    print("actuation force: %.2f uN" % (F_act * 1e6))
    print("energy dissipated per cycle: %.1e J/m^3 (%.1e J in this wire)" % (W_cycle, E_diss))
    assert abs(stroke * 1e9 - 120.0) < 0.5, stroke
    assert abs(F_act * 1e6 - 3.93) < 0.05, F_act
    assert abs(W_cycle - 1.2e7) < 1e4, W_cycle
    assert abs(E_diss - 1.885e-13) / 1.885e-13 < 0.02, E_diss
    print("rule: the hysteresis loop is the product when you need damping")
    print("OK: %s sized the actuator" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_nm_nanolattices(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # Gibson-Ashby: octet (stretch) vs foam (bend) at 1% relative density
    E_s, sig_s, rho_s = 200e9, 1e9, 8000.0
    for rho_bar in (0.1, 0.01, 0.001):
        E_oct = 0.3 * E_s * rho_bar
        s_oct = 0.3 * sig_s * rho_bar
        E_foam = E_s * rho_bar ** 2
        s_foam = 0.3 * sig_s * rho_bar ** 1.5
        rho = rho_bar * rho_s
        print("density %5.1f%% (%6.1f kg/m^3): octet E=%7.1f MPa | foam E=%6.2f MPa  (%.0fx)"
              % (rho_bar * 100, rho, E_oct / 1e6, E_foam / 1e6, E_oct / E_foam))
    assert abs(0.3 * E_s * 0.01 - 6e8) < 1e6
    assert abs(0.3 * sig_s * 0.01 - 3e6) < 1e4
    spec = 6e8 / 80.0
    print("octet at 1%%: specific stiffness %.2e m^2/s^2 - aluminum territory at 1%% weight"
          % spec)
    assert abs(spec - 7.5e6) < 1e4, spec
    print("rule: spend material only where the load paths run")
    print("OK: %s built empty space" % NAME)
if __name__ == "__main__":
    main()
''')
def demo_nm_viscoelastic(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # Kelvin-Voigt creep of a polymer nanofiber + the Deborah verdict
    E, eta = 2e9, 1e6
    tau = eta / E
    sigma0 = 100e6
    eps_inf = sigma0 / E
    eps_tau = eps_inf * (1.0 - math.exp(-1.0))
    print("retardation time tau = %.1f ms" % (tau * 1e3))
    print("creep: eps(inf) = %.3f; eps(tau) = %.4f (63%%)" % (eps_inf, eps_tau))
    assert abs(tau - 5e-4) < 1e-9, tau
    assert abs(eps_tau - 0.0316) < 0.0005, eps_tau
    print(" process time -> Deborah number -> verdict")
    for tp, verdict in ((1e-6, "glassy solid"), (1e-3, "FULL VISCOELASTIC DRAMA"), (1.0, "flowing liquid")):
        De = tau / tp
        print(" %8s -> De = %8.1f: %s" % ("%g s" % tp, De, verdict))
    assert abs(tau / 1e-3 - 0.5) < 1e-9
    assert abs(tau / 1e-6 - 500.0) < 1e-6
    print("rule: ask the time question before fitting any modulus")
    print("OK: %s watched it creep" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_nm_buckling(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # Euler buckling of a Au nanopillar + wrinkle metrology
    E = 79e9
    d, L, K = 100e-9, 1e-6, 0.7
    I = math.pi * d ** 4 / 64.0
    P_cr = math.pi ** 2 * E * I / (K * L) ** 2
    A = math.pi * (d / 2.0) ** 2
    sig_cr = P_cr / A
    sig_yield_nano = 1.5e9
    print("Euler load P_cr = %.2f uN -> %.0f MPa" % (P_cr * 1e6, sig_cr / 1e6))
    print("nanoscale yield ~%.0f MPa: %s wins" % (sig_yield_nano / 1e6,
          "BUCKLING" if sig_cr < sig_yield_nano else "yielding"))
    assert abs(P_cr * 1e6 - 7.81) < 0.05, P_cr
    assert abs(sig_cr / 1e6 - 994.0) < 5.0, sig_cr
    assert sig_cr < sig_yield_nano
    # wrinkling: 50 nm film on 2 MPa substrate
    h, Ef, Es = 50e-9, 70e9, 2e6
    lam = 2.0 * math.pi * h * (Ef / (3.0 * Es)) ** (1.0 / 3.0)
    print("wrinkle wavelength: %.2f um - a modulus ruler" % (lam * 1e6))
    assert abs(lam * 1e6 - 7.12) < 0.05, lam
    print("rule: know whether you tested the material or the structure")
    print("OK: %s buckled honestly" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_nm_thermal_effects(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # Zener thermoelastic damping for a 100 nm Si beam
    E, alpha, T = 169e9, 2.6e-6, 300.0
    rho, Cp, kappa = 2330.0, 700.0, 150.0
    h = 100e-9
    tau = h ** 2 * rho * Cp / (math.pi ** 2 * kappa)
    f_peak = 1.0 / (2.0 * math.pi * tau)
    Delta = E * alpha ** 2 * T / (rho * Cp)
    Q_ted = 2.0 / Delta
    print("thermal time tau = %.1f ps; damping peaks at %.1f GHz" % (tau * 1e12, f_peak / 1e9))
    print("relaxation strength Delta = %.2e -> TED-limited Q = %.0f" % (Delta, Q_ted))
    assert abs(tau * 1e12 - 11.0) < 0.3, tau
    assert abs(f_peak / 1e9 - 14.4) < 0.3, f_peak
    assert 9500.0 < Q_ted < 9540.0, Q_ted
    # thermalization scaling L^2
    t_cm = (1e-2) ** 2 / (kappa / (rho * Cp))
    t_nm = (100e-9) ** 2 / (kappa / (rho * Cp))
    print("thermalize 1 cm: %.1e s; 100 nm: %.1e s (%.0e x faster)"
          % (t_cm, t_nm, t_cm / t_nm))
    assert abs(t_cm / t_nm - 1e10) < 1e8
    print("rule: every vibration pays the heat tax - price it first")
    print("OK: %s taxed the vibration" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_nm_electromechanical(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # ZnO nanowire nanogenerator + flexoelectric crossover
    d33 = 12.4e-12
    d, L = 100e-9, 10e-6
    A = math.pi * (d / 2.0) ** 2
    F = 1e-6
    sigma = F / A
    Q = d33 * F
    I_1kHz = Q * 1000.0
    print("axial press 1 uN -> stress %.0f MPa" % (sigma / 1e6))
    print("charge per press: %.2e C; current at 1 kHz: %.1f fA" % (Q, I_1kHz * 1e15))
    assert abs(sigma / 1e6 - 127.3) < 0.5, sigma
    assert abs(Q - 1.24e-17) / 1.24e-17 < 0.02, Q
    assert abs(I_1kHz * 1e15 - 12.4) < 0.3, I_1kHz
    # flexoelectricity: strain gradient ~ curvature
    mu = 1e-9
    delta, Lc = 100e-9, 1e-6
    kappa = 3.0 * delta / Lc ** 2
    P_flexo = mu * kappa
    print("bent cantilever: strain gradient %.1e /m -> P_flexo = %.1e C/m^2" % (kappa, P_flexo))
    assert abs(kappa - 3e5) < 1.0, kappa
    assert abs(P_flexo - 3e-4) / 3e-4 < 1e-9, P_flexo
    print("shrink 10x: gradient (and P_flexo) grow 10x, piezo stays flat")
    print("rule: bend it sharply enough and every insulator joins in")
    print("OK: %s harvested the volts" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_nm_fluid_structure(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # Q vs pressure ladder + water immersion for a NEMS beam
    Q0, p0 = 1e4, 0.133322                  # at 1 mTorr
    print(" pressure -> Q (molecular regime, Q ~ 1/p)")
    for p, label in ((0.133322, "1 mTorr"), (1.0, "1 Pa"), (100.0, "100 Pa"), (101325.0, "1 atm")):
        Q = Q0 * p0 / p
        print(" %7s -> Q = %.3g%s" % (label, Q, "  (resonance drowned)" if Q < 1 else ""))
    assert abs(Q0 * p0 / 1.0 - 1333.2) < 0.5
    assert abs(Q0 * p0 / 101325.0 - 0.01316) < 0.0005
    p_Q100 = Q0 * p0 / 100.0
    print("vacuum spec for Q=100: %.1f Pa" % p_Q100)
    assert abs(p_Q100 - 13.33) < 0.05, p_Q100
    # immersion: added mass drops the frequency
    rho_f, w = 1000.0, 1e-6
    m_add = math.pi * rho_f * w ** 2 / 4.0
    m_beam = 2330.0 * w * 100e-9
    ratio = math.sqrt(1.0 + m_add / m_beam)
    print("water immersion: frequency drops %.2fx (added mass %.1fx beam)"
          % (ratio, m_add / m_beam))
    assert abs(m_add / m_beam - 3.37) < 0.03
    assert abs(ratio - 2.09) < 0.02, ratio
    print("rule: vacuum for frequency, fluid for force")
    print("OK: %s drained the chamber" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_nm_quantum_limits(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # zero-point motion and the ground-state ladder
    hbar, kB = 1.0545718e-34, 1.380649e-23
    m, f = 1e-15, 1e6
    omega = 2.0 * math.pi * f
    x_zp = math.sqrt(hbar / (2.0 * m * omega))
    T_gs = hbar * omega / kB
    print("zero-point motion x_zp = %.1f fm" % (x_zp * 1e15))
    print("ground state needs T < %.0f uK" % (T_gs * 1e6))
    assert abs(x_zp * 1e15 - 91.6) < 0.5, x_zp
    assert abs(T_gs * 1e6 - 48.0) < 1.0, T_gs
    print(" thermal phonons in the 1 MHz mode:")
    for T in (0.01, 1.0, 300.0):
        n = kB * T / (hbar * omega)
        print(" %6s K -> %.3g phonons" % (T, n))
    assert abs(kB * 0.01 / (hbar * omega) - 208.4) / 208.4 < 0.01
    assert abs(kB * 300.0 / (hbar * omega) - 6.251e6) / 6.251e6 < 0.01
    print("rule: cool past the thermal lies to the quantum floor")
    print("OK: %s heard the ground state" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_nm_design_rules(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # end-to-end spec sheet: 10 MHz Si cantilever
    E, rho = 169e9, 2330.0
    f_target = 10e6
    w, t = 1e-6, 200e-9
    const = 0.5596 * math.sqrt(E / (12.0 * rho))     # f = const * t / L^2
    L = math.sqrt(const * t / f_target)
    I = w * t ** 3 / 12.0
    k = 3.0 * E * I / L ** 3
    g0 = 500e-9
    A_el = w * L
    V_pi = math.sqrt(8.0 * k * g0 ** 3 / (27.0 * 8.854e-12 * A_el))
    print("=== nanomechanical spec sheet ===")
    print("geometry: L=%.2f um, w=1 um, t=200 nm" % (L * 1e6))
    print("frequency: %.1f MHz (target 10)" % (const * t / L ** 2 / 1e6))
    print("stiffness k = %.2f N/m" % k)
    print("pull-in V_pi = %.1f V -> drive below %.0f V" % (V_pi, 0.7 * V_pi))
    print("damping: TED peak at 14.4 GHz >> 10 MHz (negligible); budget gas + clamping")
    print("linearity: keep amplitude below %.0f nm (t/10)" % (t * 1e9 / 10.0))
    assert abs(L * 1e6 - 5.25) < 0.05, L
    assert abs(k - 2.34) < 0.05, k
    assert abs(V_pi - 43.2) < 0.5, V_pi
    print("rule: write the whole promise before etching anything")
    print("OK: %s signed the spec sheet" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_nm_bio_mechanics(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # AFM cell indentation: Hertz sphere-on-soft-flat
    E_cell, nu = 1000.0, 0.5
    E_star = E_cell / (1.0 - nu ** 2)
    R, delta = 5e-6, 500e-9
    F = (4.0 / 3.0) * E_star * math.sqrt(R) * delta ** 1.5
    print("cell E=1 kPa, 5 um probe, 500 nm deep -> F = %.2f nN" % (F * 1e9))
    assert abs(F * 1e9 - 1.41) < 0.03, F
    # thickness rule of thumb: keep delta < 10% of cell height
    h_cell = 5e-6
    print("delta/h_cell = %.0f%% %s" % (delta / h_cell * 100,
          "(OK: thin-film correction small)" if delta / h_cell < 0.1 else "(CORRECT for substrate!)"))
    assert abs(delta / h_cell - 0.1) < 1e-9
    # stiffness contrast: healthy vs cancerous cell
    for E, label in ((2000.0, "healthy"), (500.0, "cancerous (softer)")):
        Es = E / (1.0 - nu ** 2)
        print("  %s cell: F = %.2f nN at the same depth" % (label, (4.0 / 3.0) * Es * math.sqrt(R) * delta ** 1.5 * 1e9))
    print("rule: the cell is listening with its whole cytoskeleton - poke gently")
    print("OK: %s poked the cell" % NAME)
if __name__ == "__main__":
    main()
''')

DEMOS = {
    "what_is": demo_nm_what_is, "scale_effects": demo_nm_scale_effects,
    "stress_strain": demo_nm_stress_strain,
    "continuum_breakdown": demo_nm_continuum_breakdown,
    "surface_energy": demo_nm_surface_energy,
    "surface_forces": demo_nm_surface_forces,
    "elastic_beams": demo_nm_elastic_beams,
    "nanoindentation": demo_nm_nanoindentation,
    "oliver_pharr": demo_nm_oliver_pharr,
    "afm_mechanics": demo_nm_afm_mechanics,
    "nanowires": demo_nm_nanowires, "hall_petch": demo_nm_hall_petch,
    "nanotubes": demo_nm_nanotubes, "graphene": demo_nm_graphene,
    "nanotribology": demo_nm_nanotribology,
    "contact_mechanics": demo_nm_contact_mechanics,
    "adhesion": demo_nm_adhesion, "nems": demo_nm_nems,
    "nanotube_resonance": demo_nm_nanotube_resonance,
    "fatigue_nano": demo_nm_fatigue_nano,
    "fracture_nano": demo_nm_fracture_nano,
    "md_mechanics": demo_nm_md_mechanics,
    "insitu_tem": demo_nm_insitu_tem, "plasticity": demo_nm_plasticity,
    "superelasticity": demo_nm_superelasticity,
    "nanolattices": demo_nm_nanolattices,
    "viscoelastic": demo_nm_viscoelastic, "buckling": demo_nm_buckling,
    "thermal_effects": demo_nm_thermal_effects,
    "electromechanical": demo_nm_electromechanical,
    "fluid_structure": demo_nm_fluid_structure,
    "quantum_limits": demo_nm_quantum_limits,
    "design_rules": demo_nm_design_rules,
    "bio_mechanics": demo_nm_bio_mechanics,
}
assert set(DEMOS) == {e["key"] for e in ENTRIES}, "demo map misses entries"


def build_records(slug, source):
    cfg = DBCFG[slug]
    sig = source == "signature"
    # Teaching-ladder order: stable sort by ladder_rank (entries are already
    # in ladder order in entries_nanomechanics.py).
    ordered = sorted(enumerate(ENTRIES), key=lambda p: (p[1]["ladder_rank"], p[0]))
    recs = []
    for _, e in ordered:
        name = e["name"]
        title = name + " (Signature Edition)" if sig else name
        # Whole-system dedupe: gate (through field #10) + direct gap
        # cross-check against field #11-30 shard titles. Never a sample.
        why = _dedupe_refused(slug, title)
        if why:
            print("  dedupe refused (%s): %s" % (why, title), flush=True)
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
    for slug in ("nanomechanics", "nanomechanics-signature"):
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
