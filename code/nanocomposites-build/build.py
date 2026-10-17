#!/usr/bin/env python3
"""Build the Nanocomposites field databases for JAH Databases (field #32, taxonomy order).

Verified 2026-10-17 (see entries_nanocomposites.py docstring): NO database
covers the nanocomposites discipline. Manifest search (2364 databases):
zero 'nanocomposit*' slugs or names; nearest neighbors are 'nanotech'
(10,001 general-nanotechnology records), 'nanomechanics' (34 nanomechanics
records - the mechanics of nanoscale objects, a different discipline),
'nano-gel-bot', 'nanotechnology-future', and nanotechnology career records.
Whole-system title sweep over all 764 shard indexes (~1.14M records):
the word 'nanocomposite' hits exactly one database - 'dental-published'
(114 records, all "Level 2: ... nanocomposite longevity studies": dental
filling study-planning entries mentioning dental nanocomposite fillings) -
study-corpus items, not discipline coverage. ZERO full-record discipline
coverage anywhere.

So this build creates two NEW databases, 34 ladder-ordered records each,
covering ONLY what the system left uncovered (matrix + nanoscale filler
science: rule of mixtures, Halpin-Tsai, percolation, interface load
transfer, dispersion, tortuous-path barrier, char-layer flame retardancy,
and the full filler/matrix/processing/characterization ladder):

  nanocomposites              - The Nanocomposites Database
                               (public-harvest: real, fact-checked
                               nanocomposite science; standard references
                               Ajayan/Schadler/Braun 'Nanocomposite Science
                               and Technology', Hussain et al. (2006),
                               Thostenson/Li/Chou (2005), Coleman et al.
                               (2006), Ray/Okamoto (2003), Paul/Robeson
                               (2008))
  nanocomposites-signature    - The Nanocomposites Signature Database
                               (his original Signature interpretation;
                               src signature, titles suffixed
                               " (Signature Edition)", never presented as
                               authentic public record)

34 records each, ordered by the teaching ladder (ladder_rank 1-10,
ladder_tier foundations/compounded/advanced); the shard index is written in
ladder order so pages present simple -> compounded -> complex.

Every record: description + how-it-works + key points + requirements +
standards + citations + working demonstration code (real, runnable,
stdlib-only Python; machine-executed OK). Nanocomposites demos: interface
surface-to-volume; surface-atom fraction; filler specific surface area;
specific modulus; Voigt/Reuss bounds; wt%-to-vol% conversion; dispersion
penalty via Halpin-Tsai; Kelly-Tyson critical length; Halpin-Tsai
parallel/transverse/random; aspect-ratio sweep; percolation threshold and
power law; CNT strength; graphene mixture; Bragg clay d-spacing;
nanocellulose specific modulus; Orowan looping; flaw tolerance;
Krieger-Dougherty viscosity; Scherrer size; coating hardness; electrospun
mat modulus; fracture energy; Simon EMI shielding; Maxwell-Garnett
thermal; Nielsen barrier; cone flame numbers; printed anisotropy; bone
bounds + dental loading; healing efficiency; magnetic mixture + blocking
size; RVE census + MD time; recyclate retention; exposure vs NIOSH REL;
weighted decision matrix.

Subtitle disambiguation (fields #13-31 pattern): specialty titles carry
teaching-focused subtitles rather than bare cards, e.g. "The Rule of
Mixtures: Your First Property Estimate".

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
from entries_nanocomposites import ENTRIES, SIG_TAIL

# ---------------------------------------------------------------- DB config

def _cfg(slug, name, tagline, record_kind, prefix, ai, role, citation, source):
    sig_line = ("Signature originals - his original Signature interpretation of nanocomposites: "
                "clearly labeled Signature-made, never presented as authentic "
                "public record.")
    pub_line = ("Public records - real, fact-checked nanocomposites: what nanocomposites are; "
                "the nanoscale advantage; filler dimensions (0D/1D/2D); polymer, metal, and "
                "ceramic matrices; the rule of mixtures; weight vs volume fractions; "
                "dispersion; the interface; Halpin-Tsai; aspect ratio; percolation; carbon "
                "nanotubes; graphene; clay; nanocellulose; metal-matrix and ceramic-matrix "
                "nanocomposites; processing routes; characterization; coatings; electrospun "
                "mats; fracture toughness; EMI shielding; thermal conductivity; barrier "
                "properties; flame retardancy; 3D printing; biomedical uses; self-healing; "
                "magnetic nanocomposites; multiscale modeling; sustainability; safety; "
                "design rules, organized in the Signature system.")
    ladder = (" Records are ordered by the teaching ladder: Foundations (what nanocomposites "
              "are, the nanoscale advantage, filler dimensions, matrices, rule of mixtures, "
              "fractions, dispersion, interface) -> Compounded (Halpin-Tsai, aspect ratio, "
              "percolation, nanotubes, graphene, clay, nanocellulose, metal-matrix, "
              "ceramic-matrix, processing, characterization, coatings, electrospun mats) -> "
              "Advanced (toughness, EMI shielding, thermal, barrier, flame, 3D printing, "
              "biomedical, self-healing, magnetic, modeling, sustainability, safety, "
              "design rules).")
    return {
        "name": name, "tagline": tagline, "record_kind": record_kind,
        "prefix": prefix, "ai": ai, "role": role,
        "hero_p": "%s - %s Every record carries the full entry: description, how it works, "
                  "key points, requirements, standards, citations, and a working demonstration "
                  "program.%s" % (tagline, sig_line if source == "signature" else pub_line, ladder),
        "sig_type": ("Signature originals organized in the Signature system"
                     if source == "signature" else
                     "Public records organized in the Signature system"),
        "search_ph": "Search Halpin-Tsai, percolation, nanotubes, graphene, clay, barrier, EMI shielding...",
        "chat_ph": "Ask about nanocomposites...",
        "archive_blurb": ("Seeded %s nanocomposites records, marching toward one million records. "
                          "Presented in teaching-ladder order: foundations, compounded, advanced."
                          % ("Signature-original" if source == "signature" else "public-record")),
        "schema": ("id, t, g, name, title, description, how_it_works, key_points, requirements, "
                   "standards, citations, src, ladder_rank, ladder_tier, demo"),
        "fields": "Foundations \u00b7 Compounded \u00b7 Advanced - each tier opens on demand and loads only what you open",
        "gen_desc": "Generate clearly-labeled nanocomposites studies. Seeded archive records are the authoritative entries.",
        "greet": "I am the %s. Ask me about nanocomposites - from what they are through the nanoscale advantage, filler dimensions, matrices, the rule of mixtures, fractions, dispersion, and the interface, through Halpin-Tsai, aspect ratio, percolation, nanotubes, graphene, clay, nanocellulose, metal-matrix and ceramic-matrix systems, processing, characterization, coatings, and electrospun mats, to toughness, EMI shielding, thermal conductivity, barrier, flame retardancy, 3D printing, biomedical uses, self-healing, magnetic systems, modeling, sustainability, safety, and design rules." % ai,
        "gen_fields": ["Foundations", "Compounded", "Advanced"],
        "gen_kind": "nanocomposites-study", "gen_demo_kind": "nanocomposites-demo",
        "source": source,
    }

CIT_PUB = ("Nanocomposites (standard texts: Ajayan/Schadler/Braun 'Nanocomposite Science and "
           "Technology' 2003; Hussain et al. 'Polymer-matrix Nanocomposites' J. Composite "
           "Materials 2006; Thostenson/Li/Chou 'Nanocomposites in context' Composites Sci. "
           "Tech. 2005; Coleman et al. 'Small but strong' Carbon 2006; Ray/Okamoto "
           "'Polymer/layered silicate nanocomposites' Prog. Polymer Sci. 2003; Paul/Robeson "
           "'Polymer nanotechnology: Nanocomposites' Polymer 2008; Koo 'Polymer "
           "Nanocomposites' McGraw-Hill 2006; Halpin/Kardos 'The Halpin-Tsai equations' "
           "Polymer Eng. Sci. 1976; Nielsen 'Models for the Permeability of Filled Polymer "
           "Systems' 1967; Gilman 'Flammability studies of polymer layered-silicate "
           "nanocomposites' Applied Clay Sci. 1999; NIOSH CIB 65 'Occupational Exposure to "
           "Carbon Nanotubes and Nanofibers' 2013).")
CIT_SIG = CIT_PUB + " " + SIG_TAIL

DBCFG = {}
DBCFG["nanocomposites"] = _cfg(
    "nanocomposites", "The Nanocomposites Database",
    "Real, fact-checked nanocomposites: from what nanocomposites are through the nanoscale "
    "advantage, filler dimensions, matrices, the rule of mixtures, fractions, dispersion, "
    "and the interface, through Halpin-Tsai, aspect ratio, percolation, nanotubes, graphene, "
    "clay, nanocellulose, metal-matrix and ceramic-matrix systems, processing, "
    "characterization, coatings, and electrospun mats, to toughness, EMI shielding, thermal "
    "conductivity, barrier, flame retardancy, 3D printing, biomedical uses, self-healing, "
    "magnetic systems, modeling, sustainability, safety, and design rules - taught "
    "progressively along the ladder.",
    "nanocomposites record", "JAH-NCP-", "JAH Nanocomposites Archivist",
    "nanocomposites archivist - matrix + nanoscale filler science: rule of mixtures, "
    "Halpin-Tsai, percolation, interface load transfer, dispersion, filler dimensions "
    "(0D/1D/2D), polymer/metal/ceramic matrices, nanotubes, graphene, clay, nanocellulose, "
    "processing routes, characterization, coatings, toughness, EMI shielding, thermal "
    "conductivity, tortuous-path barrier, flame retardancy, 3D printing, biomedical uses, "
    "self-healing, magnetic systems, multiscale modeling, sustainability, safety, design "
    "rules; teaching progressively along the ladder from foundations through compounded "
    "to advanced; answers from many angles - definition, example, analogy, application, "
    "history, math, how-to - using only archive data from this system",
    CIT_PUB, "public")
DBCFG["nanocomposites-signature"] = _cfg(
    "nanocomposites-signature", "The Nanocomposites Signature Database",
    "His original Signature interpretation of nanocomposites: the full ladder from what "
    "nanocomposites are through scale, fillers, matrices, mixtures, interfaces, models, "
    "processing, and characterization to toughness, shielding, barrier, fire, printing, "
    "medicine, healing, magnetism, and design rules, reframed as Signature science. Clearly "
    "labeled Signature-made, never presented as authentic public record.",
    "nanocomposites record", "JAH-NCS-", "JAH Nanocomposites Archivist (Signature)",
    "nanocomposites archivist - Signature editions: his original Signature "
    "interpretation of nanocomposites, clearly labeled Signature-made and "
    "never presented as authentic public record; teaches progressively along the "
    "ladder from foundations through compounded to advanced; answers from many "
    "angles - definition, example, analogy, application, history, math, how-to - "
    "using only archive data from this system",
    CIT_SIG, "signature")

base.DBCFG = DBCFG

# ---------------------------------------------------------------- demos
# Every demo is real, runnable, stdlib-only Python performing the actual
# nanocomposites computation for its record. All are machine-executed by main().

_PREAMBLE = (
"import math\n"
)

def _wrap(name, rid, group, body):
    return (base._hdr(name, rid, group) + _PREAMBLE + body.replace("NAME", json.dumps(name)))

def demo_nc_what_is(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # surface-to-volume of a sphere: 3/r - the interface arithmetic
    sv_nano = 3.0 / 5e-9          # 5 nm sphere
    sv_grain = 3.0 / 5e-4         # 0.5 mm grain
    print("5 nm sphere surface-to-volume: %.1e /m" % sv_nano)
    print("0.5 mm grain surface-to-volume: %.1e /m" % sv_grain)
    print("ratio: %.0e - the interface takes over" % (sv_nano / sv_grain))
    assert 5.99e8 < sv_nano < 6.01e8
    assert sv_grain == 6000.0
    assert 0.99e5 < sv_nano / sv_grain < 1.01e5
    print("rule: shrink the filler and the surface becomes the material")
    print("OK: %s weighed the interface" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_nc_scale(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # fraction of atoms within one atomic layer (0.3 nm) of a cube's surface
    d = 0.3
    for L in (10.0, 1000.0):
        f = (L**3 - (L - 2.0*d)**3) / L**3
        print("cube %.0f nm: %.2f%% of atoms are surface atoms" % (L, f*100))
    f10 = (10.0**3 - 9.4**3) / 10.0**3
    f1000 = (1000.0**3 - 999.4**3) / 1000.0**3
    assert 0.169 < f10 < 0.170
    assert 0.00179 < f1000 < 0.00181
    print("rule: at 10 nm the surface is the material; at 1 um it is a rumor")
    print("OK: %s counted surface atoms" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_nc_filler_dimensions(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # specific surface area: sphere 3/(rho*r), tube 4/(rho*d), platelet 2/(rho*t)
    ssa_sphere = 3.0 / (2200.0 * 50e-9) / 1000.0      # 50 nm silica, m^2/g
    ssa_tube = 4.0 / (1300.0 * 10e-9) / 1000.0        # 10 nm CNT
    ssa_plate = 2.0 / (2600.0 * 1e-9) / 1000.0        # 1 nm clay
    print("50 nm silica spheres: %.1f m^2/g" % ssa_sphere)
    print("10 nm nanotubes: %.1f m^2/g" % ssa_tube)
    print("1 nm platelets: %.1f m^2/g" % ssa_plate)
    assert 27.2 < ssa_sphere < 27.4
    assert 307.6 < ssa_tube < 307.8
    assert 769.1 < ssa_plate < 769.4
    print("rule: the thinnest dimension sets the surface - platelets win per gram")
    print("OK: %s measured the filler zoo" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_nc_matrices(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # specific modulus E/rho: the fair way to compare material families
    for mat, E, rho in (("aluminum", 70e9, 2700.0), ("epoxy", 3e9, 1200.0),
                        ("alumina", 380e9, 3900.0)):
        print("%-9s specific modulus: %.1f MN m/kg" % (mat, E / rho / 1e6))
    assert abs(70e9/2700.0/1e6 - 25.9) < 0.1
    assert abs(3e9/1200.0/1e6 - 2.5) < 0.05
    assert abs(380e9/3900.0/1e6 - 97.4) < 0.1
    print("rule: divide stiffness by weight before you compare materials")
    print("OK: %s weighed the matrices" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_nc_rule_of_mixtures(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # Voigt (parallel, share strain) and Reuss (series, share stress) bounds
    Ef, Em, Vf = 72.0, 3.0, 0.5
    voigt = Vf*Ef + (1.0-Vf)*Em
    reuss = 1.0 / (Vf/Ef + (1.0-Vf)/Em)
    print("Voigt upper bound: %.2f GPa" % voigt)
    print("Reuss lower bound: %.2f GPa" % reuss)
    print("anisotropy between fences: %.1fx" % (voigt/reuss))
    assert voigt == 37.5
    assert abs(reuss - 5.76) < 0.01
    print("rule: reality grazes between the fences - outside them is wrong data")
    print("OK: %s walked the fence line" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_nc_fractions(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # weight fraction -> volume fraction; density cross-check catches voids
    wf, rhof, rhom = 0.30, 2500.0, 1200.0
    vf = (wf/rhof) / (wf/rhof + (1.0-wf)/rhom)
    print("30 wt%% glass in epoxy = %.1f vol%%" % (vf*100))
    assert 0.170 < vf < 0.172
    rho_c = vf*rhof + (1.0-vf)*rhom
    rho_from_mass = 1.0 / (wf/rhof + (1.0-wf)/rhom)
    print("composite density: %.0f kg/m^3 (both routes agree)" % rho_c)
    assert abs(rho_c - rho_from_mass) < 1e-6
    print("rule: weigh in wt%%, think in vol%%, verify by density")
    print("OK: %s balanced the books" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_nc_dispersion(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # Halpin-Tsai penalty for agglomeration: aspect 1000 -> effective 10
    def halpin_tsai(aspect, vf, ratio):
        xi = 2.0*aspect
        eta = (ratio - 1.0)/(ratio + xi)
        return (1.0 + xi*eta*vf)/(1.0 - eta*vf)
    good = halpin_tsai(1000.0, 0.01, 1000.0/3.0)
    bad = halpin_tsai(10.0, 0.01, 1000.0/3.0)
    print("isolated tubes (aspect 1000): E/Em = %.2f" % good)
    print("agglomerated (aspect 10): E/Em = %.2f" % bad)
    print("dispersion penalty: %.1fx of reinforcement lost" % (good/bad))
    assert 3.84 < good < 3.87
    assert 1.19 < bad < 1.21
    print("rule: one percent dispersed beats five percent clumped")
    print("OK: %s priced agglomeration" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_nc_interface(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # Kelly-Tyson critical length: lc = sigma_f * d / (2 * tau)
    sig_f, d, tau = 30e9, 10e-9, 50e6
    lc = sig_f*d/(2.0*tau)
    print("critical length: %.1f um" % (lc*1e6))
    for L_um in (1.0, 10.0):
        L = L_um*1e-6
        eff = L/(2.0*lc) if L < lc else 1.0 - lc/(2.0*L)
        print("%4.0f um tube: %.1f%% load-transfer efficiency" % (L_um, eff*100))
    assert abs(lc - 3e-6) < 1e-9
    assert abs(1e-6/(2.0*lc) - 1.0/6.0) < 1e-9
    assert abs((1.0 - lc/(2.0*10e-6)) - 0.85) < 1e-9
    print("rule: the handshake length decides how much strength arrives")
    print("OK: %s measured the handshake" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_nc_halpin_tsai(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # Halpin-Tsai for glass/epoxy: parallel, transverse, in-plane random
    Ef, Em, Vf, aspect = 72.0, 3.0, 0.1, 100.0
    r = Ef/Em
    eta_L = (r-1.0)/(r + 2.0*aspect)
    eta_T = (r-1.0)/(r + 2.0)
    EL = Em*(1.0 + 2.0*aspect*eta_L*Vf)/(1.0 - eta_L*Vf)
    ET = Em*(1.0 + 2.0*eta_T*Vf)/(1.0 - eta_T*Vf)
    Er = 0.375*EL + 0.625*ET
    print("parallel: %.2f GPa; transverse: %.2f GPa; in-plane random: %.2f GPa" % (EL, ET, Er))
    assert 9.24 < EL < 9.27
    assert 3.86 < ET < 3.89
    assert 5.87 < Er < 5.91
    print("rule: most fibres point the wrong way - average honestly")
    print("OK: %s ran Halpin-Tsai" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_nc_aspect_ratio(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # stiffness vs aspect ratio at 5 vol%, 24x contrast: diminishing returns
    def ht(aspect):
        xi = 2.0*aspect; r = 24.0; vf = 0.05
        eta = (r-1.0)/(r+xi)
        return (1.0+xi*eta*vf)/(1.0-eta*vf)
    vals = [(a, ht(float(a))) for a in (1, 10, 100, 1000)]
    for a, v in vals:
        print("aspect %4d: E/Em = %.2f" % (a, v))
    assert 1.13 < vals[0][1] < 1.15
    assert 1.55 < vals[1][1] < 1.57
    assert 2.03 < vals[2][1] < 2.05
    assert 2.13 < vals[3][1] < 2.15
    print("rule: almost everything is won by aspect 100 - the rest is vanity length")
    print("OK: %s swept the aspect ratios" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_nc_percolation(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # percolation threshold for rods ~ 0.7/aspect; power law above it
    aspect = 1000.0
    vc = 0.7/aspect
    vf = 0.01
    sigma = 1e4*(vf - vc)**2.0
    print("percolation threshold: %.4f vol%%" % (vc*100))
    print("at 1 vol%%: sigma = %.2f S/m vs matrix 1e-12 S/m" % sigma)
    assert abs(vc - 7e-4) < 1e-9
    assert 0.86 < sigma < 0.87
    print("rule: one more bridge and the islands become a continent")
    print("OK: %s found the threshold" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_nc_cnt_polymer(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # Kelly-Tyson strength: matrix share + efficiency-weighted filler share
    sig_m, sig_f, vf, eta = 80.0, 30000.0, 0.02, 0.85
    sig_c = sig_m*(1.0-vf) + eta*sig_f*vf
    print("2 vol%% CNT in 80 MPa epoxy -> %.0f MPa (%.1fx)" % (sig_c, sig_c/sig_m))
    assert 588.0 < sig_c < 589.0
    assert 7.3 < sig_c/sig_m < 7.4
    print("rule: spectacular, yet far below the mixture fantasy - reality discounts")
    print("OK: %s loaded the straws" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_nc_graphene(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # random 2D platelets: 3/8 orientation weight on the mixture
    E = 0.375*0.01*1000.0 + 3.0*0.99
    print("1 vol%% random graphene in epoxy: %.2f GPa vs 3.00 GPa neat" % E)
    assert abs(E - 6.72) < 0.01
    print("rule: platelets pay in-plane - orient them or average honestly")
    print("OK: %s laid the chain mail" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_nc_clay(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # Bragg d-spacing: the XRD diary of intercalation
    lam = 0.154                                   # nm, Cu K-alpha
    theta = math.radians(4.8/2.0)                 # 2theta = 4.8 deg
    d = lam/(2.0*math.sin(theta))
    print("d001 at 2theta=4.8 deg: %.2f nm (pristine 1.20 nm -> intercalated)" % d)
    assert 1.83 < d < 1.85
    print("rule: the peak shifts when polymer enters, vanishes when layers part")
    print("OK: %s read the clay diary" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_nc_nanocellulose(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # specific modulus: the tree vs the mill, per kilo
    cnf = 130e9/1500.0/1e6
    steel = 200e9/7800.0/1e6
    print("CNF specific modulus: %.1f MN m/kg; steel: %.1f" % (cnf, steel))
    print("the tree beats the mill by %.1fx per kilo" % (cnf/steel))
    assert 86.6 < cnf < 86.8
    assert 3.37 < cnf/steel < 3.39
    print("rule: sunlight and patience outrank blast furnaces per pound")
    print("OK: %s weighed the forest" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_nc_mmnc(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # Orowan looping: dislocations bow around particles, delta_sigma = G*b/L
    dsigma = 26e9*0.286e-9/100e-9
    print("Orowan strength gain: %.1f MPa from particles alone" % (dsigma/1e6))
    assert 74.0 < dsigma/1e6 < 75.0
    print("rule: salt the roads with boulders and the traffic slows")
    print("OK: %s jammed the dislocations" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_nc_cmnc(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # flaw tolerance: a_c = (K_IC/(Y*sigma))^2 / pi - toughness squared is forgiveness
    for K in (3.0e6, 5.0e6):
        ac = (K/500e6)**2/math.pi
        print("K_IC=%.0f MPa m^1/2: survivable flaw %.1f um" % (K/1e6, ac*1e6))
    assert 11.4 < (3.0e6/500e6)**2/math.pi*1e6 < 11.6
    assert 31.7 < (5.0e6/500e6)**2/math.pi*1e6 < 32.0
    print("rule: small toughness gains, tripled survivable flaws")
    print("OK: %s priced forgiveness" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_nc_processing(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # Krieger-Dougherty: the viscosity tax on loading
    vf, vm, intr = 0.20, 0.64, 2.5
    eta_r = (1.0 - vf/vm)**(-intr*vm)
    print("20 vol%% spheres: relative viscosity %.2f" % eta_r)
    assert 1.81 < eta_r < 1.83
    print("rule: viscosity is the tax collector - masterbatch pays it once")
    print("OK: %s paid the viscosity tax" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_nc_characterization(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # Scherrer equation: D = K*lambda/(beta*cos(theta)) - broad peaks, small crystals
    beta = math.radians(0.5)                      # peak broadening, rad
    theta = math.radians(25.0)                    # 2theta = 50 deg
    D = 0.9*0.154/(beta*math.cos(theta))
    print("Scherrer size: %.1f nm" % D)
    assert 17.4 < D < 17.7
    print("rule: broad peaks are small crystals - measure, don't admire")
    print("OK: %s sized the invisible" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_nc_coatings(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # nanocomposite hard coatings: nanostructure doubles the hardness
    h_tin, h_nc = 20.0, 45.0
    print("TiN: %.0f GPa -> nc-TiN/SiNx: %.0f GPa (%.2fx harder)" % (h_tin, h_nc, h_nc/h_tin))
    print("Archard: wear rate falls ~%.1fx at equal load" % (h_nc/h_tin))
    assert h_nc/h_tin == 2.25
    print("rule: 5 nm crystals, 2 nm tissue - no room for dislocations, no road for cracks")
    print("OK: %s hardened the surface" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_nc_electrospun(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # random fibre mat: Cox 3/8 orientation average on the fibre modulus
    E = 0.375*0.30*3.0                            # GPa
    print("random nylon mat (30 vol%% fibres): %.0f MPa" % (E*1000))
    assert abs(E*1000 - 337.5) < 0.1
    print("rule: spin the fibre, weave the mat, calender for strength")
    print("OK: %s wove the mat" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_nc_toughness(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # fracture energy G_c = K_IC^2/E: toughness is energy, and energy loves K squared
    E = 3e9
    for K in (0.6e6, 1.5e6):
        G = K**2/E
        print("K_IC=%.1f MPa m^1/2 -> G_c=%.0f J/m^2" % (K/1e6, G))
    assert abs((0.6e6)**2/E - 120.0) < 0.5
    assert abs((1.5e6)**2/E - 750.0) < 1.0
    print("rule: toughness is energy - and energy scales with K squared")
    print("OK: %s taxed the crack" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_nc_emi_shielding(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # Simon formalism: SE = 50 + 10*log10(sigma/f) + 1.7*t*sqrt(sigma*f)
    sigma, f, t = 100.0, 1000.0, 0.2              # S/cm, MHz, cm
    SE = 50.0 + 10.0*math.log10(sigma/f) + 1.7*t*math.sqrt(sigma*f)
    print("2 mm, 100 S/cm, 1 GHz: SE = %.1f dB" % SE)
    assert 147.4 < SE < 147.7
    print("rule: reflect the cowards, absorb the brave")
    print("OK: %s silenced the noise" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_nc_thermal(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # Maxwell-Garnett for spheres: the sobering arithmetic of heat paths
    kf, km, vf = 3000.0, 0.2, 0.05
    ratio = (kf + 2*km + 2*vf*(kf-km))/(kf + 2*km - vf*(kf-km))
    k = km*ratio
    print("5 vol%% spheres (k=3000) in 0.2 W/m K matrix -> %.3f W/m K" % k)
    print("only %.0f%% gain - spheres are rest stops, not highways" % ((ratio-1)*100))
    assert 0.231 < k < 0.233
    print("rule: connectivity beats loading, aspect beats spheres")
    print("OK: %s paved the heat maze" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_nc_barrier(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # Nielsen tortuous path: P/P0 = (1-Vf)/(1 + alpha*Vf/2)
    alpha, vf = 100.0, 0.03
    p = (1.0-vf)/(1.0 + alpha*vf/2.0)
    print("aspect-100 platelets at 3 vol%%: P/P0 = %.3f (%.0f%% cut)" % (p, (1-p)*100))
    assert abs(p - 0.388) < 0.001
    print("rule: tile the shingles, audit every tile")
    print("OK: %s built the labyrinth" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_nc_flame(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # cone calorimetry: the char skin starves the flame
    phrr0, phrr1 = 1000.0, 400.0
    char0, char1 = 5.0, 25.0
    print("PHRR: %.0f -> %.0f kW/m^2 (%.0f%% cut)" % (phrr0, phrr1, (1-phrr1/phrr0)*100))
    print("char: %.0f%% -> %.0f%% (%.0fx)" % (char0, char1, char1/char0))
    assert (1-phrr1/phrr0) == 0.6
    assert char1/char0 == 5.0
    print("rule: feed the beast stones, not fuel - wall it out and let it starve")
    print("OK: %s armored against fire" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_nc_additive(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # printed anisotropy: ply rotation, cos^4/sin^4 - the slicer draws the strength map
    EL, ET = 9.2557, 3.8734
    c45 = math.cos(math.radians(45.0))
    E45 = EL*c45**4 + ET*(math.sin(math.radians(45.0)))**4
    print("0-deg raster: %.2f GPa; 45-deg raster: %.2f GPa" % (EL, E45))
    assert 3.27 < E45 < 3.30
    print("rule: the slicer draws the strength map - plan the walk")
    print("OK: %s printed the anisotropy" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_nc_biomedical(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # bone bounds + dental loading: the mixture frames, architecture decides
    voigt = 0.5*100.0 + 0.5*1.0                  # HA/collagen, GPa
    reuss = 1.0/(0.5/100.0 + 0.5/1.0)
    print("50/50 HA/collagen: Voigt %.1f GPa, Reuss %.2f GPa - bone's 18 GPa is architecture" % (voigt, reuss))
    wf = 0.80
    vf = (wf/2200.0)/(wf/2200.0 + (1.0-wf)/1200.0)
    print("dental 80 wt%% silica = %.1f vol%%" % (vf*100))
    assert voigt == 50.5
    assert 1.97 < reuss < 1.99
    assert 68.5 < vf*100 < 68.7
    print("rule: copy the staggered brickwork - the body patented it first")
    print("OK: %s apprenticed to bone" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_nc_self_healing(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # healing efficiency: recovered fracture load over virgin
    virgin, healed = 100.0, 75.0
    eta = healed/virgin
    print("healing efficiency: %.0f%% (%.0f N of %.0f N recovered)" % (eta*100, healed, virgin))
    assert eta == 0.75
    print("rule: capsules heal once, networks refill, chemistry repeats - pick your forgiveness")
    print("OK: %s forgave the crack" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_nc_magnetic(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # mixture magnetization + superparamagnetic blocking size KV = 25kT
    M = 0.30*2.45                                # T, 30 vol% FeCo
    kB, T, K = 1.380649e-23, 300.0, 4e4
    V = 25.0*kB*T/K
    d = (6.0*V/math.pi)**(1.0/3.0)
    print("30 vol%% FeCo: %.3f T" % M)
    print("Fe blocking diameter at 300 K: %.1f nm" % (d*1e9))
    assert abs(M - 0.735) < 1e-9
    assert 16.9 < d*1e9 < 17.2
    print("rule: size the memory, pour the forgetfulness where healing is needed")
    print("OK: %s tuned the magnets" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_nc_modeling(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # RVE census + MD time: the relay's two hardest numbers
    N = 0.05*200.0**3/(math.pi*20.0**3/6.0)
    t = 1e6*1e-15
    print("RVE: %.0f particles in the 200 nm cube" % N)
    print("MD: 1e6 steps x 1 fs = %.0e s - a blink against processing minutes" % t)
    assert 95.0 < N < 96.0
    assert t == 1e-9
    print("rule: the relay runs laps - model predicts, experiment checks")
    print("OK: %s ran the relay" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_nc_sustainability(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # recyclate arithmetic: degraded matrix + shortened fibres in Halpin-Tsai
    def ht(Ef, Em, vf, aspect):
        r = Ef/Em; xi = 2.0*aspect
        eta = (r-1.0)/(r+xi)
        return Em*(1.0+xi*eta*vf)/(1.0-eta*vf)
    virgin = ht(72.0, 3.0, 0.30, 50.0)
    recyclate = ht(72.0, 2.5, 0.30, 20.0)
    print("virgin: %.1f GPa; recyclate: %.1f GPa (%.0f%% retained)" % (virgin, recyclate, recyclate/virgin*100))
    assert 20.8 < virgin < 21.0
    assert 16.5 < recyclate < 16.8
    print("rule: downcycling is honest recycling - price the ratchet")
    print("OK: %s priced the second life" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_nc_safety(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # exposure arithmetic vs the NIOSH limit
    handled_mg, airborne_frac, room_m3 = 10.0, 0.01, 100.0
    conc = handled_mg*1000.0*airborne_frac/room_m3   # ug/m^3
    REL = 1.0
    print("10 mg handled, 1%% airborne, 100 m^3 room -> %.1f ug/m^3" % conc)
    print("NIOSH REL: %.0f ug/m^3 -> %s" % (REL, "AT THE LIMIT - hood required" if conc >= REL else "under the limit"))
    assert conc == 1.0
    print("rule: bound filler is safe filler - hood the powder, verify the air")
    print("OK: %s checked the air" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_nc_design_rules(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # weighted decision matrix for an EV battery tray: the weights choose
    weights = [0.35, 0.25, 0.25, 0.15]           # stiffness, cost, process, safety
    cands = {
        "glass/epoxy baseline": [3, 5, 5, 5],
        "CNT hybrid": [5, 2, 3, 3],
        "nanocellulose system": [4, 4, 3, 5],
    }
    scores = dict((k, sum(s*w for s, w in zip(v, weights))) for k, v in cands.items())
    for k, v in sorted(scores.items(), key=lambda kv: -kv[1]):
        print("%-22s weighted score: %.2f" % (k, v))
    winner = max(scores, key=scores.get)
    assert abs(scores["glass/epoxy baseline"] - 4.30) < 1e-9
    assert abs(scores["CNT hybrid"] - 3.45) < 1e-9
    assert abs(scores["nanocellulose system"] - 3.90) < 1e-9
    assert winner == "glass/epoxy baseline"
    print("winner: %s - the weights chose, not the hype" % winner)
    print("rule: ten rules, checked honestly, beat ten percent more filler")
    print("OK: %s ran the checklist" % NAME)
if __name__ == "__main__":
    main()
''')

DEMOS = {
    "what_is": demo_nc_what_is, "scale": demo_nc_scale,
    "filler_dimensions": demo_nc_filler_dimensions,
    "matrices": demo_nc_matrices, "rule_of_mixtures": demo_nc_rule_of_mixtures,
    "fractions": demo_nc_fractions, "dispersion": demo_nc_dispersion,
    "interface": demo_nc_interface, "halpin_tsai": demo_nc_halpin_tsai,
    "aspect_ratio": demo_nc_aspect_ratio, "percolation": demo_nc_percolation,
    "cnt_polymer": demo_nc_cnt_polymer, "graphene": demo_nc_graphene,
    "clay": demo_nc_clay, "nanocellulose": demo_nc_nanocellulose,
    "mmnc": demo_nc_mmnc, "cmnc": demo_nc_cmnc,
    "processing": demo_nc_processing,
    "characterization": demo_nc_characterization, "coatings": demo_nc_coatings,
    "electrospun": demo_nc_electrospun, "toughness": demo_nc_toughness,
    "emi_shielding": demo_nc_emi_shielding, "thermal": demo_nc_thermal,
    "barrier": demo_nc_barrier, "flame": demo_nc_flame,
    "additive": demo_nc_additive, "biomedical": demo_nc_biomedical,
    "self_healing": demo_nc_self_healing, "magnetic": demo_nc_magnetic,
    "modeling": demo_nc_modeling, "sustainability": demo_nc_sustainability,
    "safety": demo_nc_safety, "design_rules": demo_nc_design_rules,
}
assert set(DEMOS) == {e["key"] for e in ENTRIES}, "demo map misses entries"



def build_records(slug, source):
    cfg = DBCFG[slug]
    sig = source == "signature"
    # Teaching-ladder order: stable sort by ladder_rank (entries are already
    # in ladder order in entries_nanocomposites.py).
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
    for slug in ("nanocomposites", "nanocomposites-signature"):
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
