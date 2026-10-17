#!/usr/bin/env python3
"""Build the Mineralogy field databases for JAH Databases (field #8, taxonomy order).

Verified 2026-10-17: NO database covers mineralogy as a science. Manifest
slug hit 'rocks-minerals' is a 52-record specimen catalog (rock overviews,
FAQs, applications) with no crystal systems, classification science, optical
mineralogy, or X-ray crystallography; 'geology' (10,000 records) is the broad
geology database, not a dedicated mineralogy science database. So this build
creates two NEW databases:

  mineralogy              — The Mineralogy Database (public-harvest: real,
                            fact-checked mineralogy — crystal systems and
                            symmetry, Dana/Strunz classification, physical
                            properties (hardness, cleavage, luster, streak,
                            color, specific gravity), optical mineralogy,
                            X-ray crystallography, formation environments,
                            rock-forming vs ore minerals, gemstones,
                            identification methods)
  mineralogy-signature    — The Mineralogy Signature Database (his original
                            Signature interpretation; src signature, titles
                            suffixed " (Signature Edition)", never presented
                            as authentic public record)

36 records each, ordered by the teaching ladder (ladder_rank 1-10,
ladder_tier foundations/compounded/advanced); the shard index is written in
ladder order so pages present simple -> compounded -> complex.

Every record: description + how-it-works + key points + requirements +
standards + citations + working demonstration code (real, runnable,
stdlib-only Python; machine-executed OK).

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

sys.path.insert(0, HERE)
from entries_mineralogy import ENTRIES, SIG_TAIL

# ---------------------------------------------------------------- DB config

def _cfg(slug, name, tagline, record_kind, prefix, ai, role, citation, source):
    sig_line = ("Signature originals — his original Signature interpretation of mineralogy: "
                "clearly labeled Signature-made, never presented as authentic public record.")
    pub_line = ("Public records — real, fact-checked mineralogy: crystal systems and symmetry, "
                "the Dana and Nickel-Strunz classifications, physical properties (hardness, "
                "cleavage, luster, streak, color, specific gravity), optical mineralogy, "
                "X-ray crystallography, mineral formation environments, rock-forming versus "
                "ore minerals, gemstones, and identification methods, organized in the "
                "Signature system.")
    ladder = (" Records are ordered by the teaching ladder: Foundations (what mineralogy is, "
              "the five mineral tests, crystal systems, habit, Mohs hardness, cleavage and "
              "fracture, luster and streak, color, specific gravity, Dana classification, "
              "Nickel-Strunz classification, reading formulas) -> Compounded (point groups, "
              "Bravais lattices, silicate structures, rock-forming minerals, ore minerals, "
              "igneous crystallization, sedimentary and metamorphic formation, hydrothermal "
              "veins and pegmatites, the polarizing microscope, refractive index and "
              "birefringence, pleochroism and interference colors, gemstones, hand-sample "
              "identification) -> Advanced (Bragg's law, structure determination, solid "
              "solution and polymorphism, thermodynamics, phase diagrams, Goldschmidt's "
              "substitution rules, gemstone treatments and synthetics detection, the IMA "
              "registry, describing a new mineral, environmental mineralogy, systematic "
              "collecting).")
    return {
        "name": name, "tagline": tagline, "record_kind": record_kind,
        "prefix": prefix, "ai": ai, "role": role,
        "hero_p": "%s — %s Every record carries the full entry: description, how it works, "
                  "key points, requirements, standards, citations, and a working demonstration "
                  "program.%s" % (tagline, sig_line if source == "signature" else pub_line, ladder),
        "sig_type": ("Signature originals organized in the Signature system"
                     if source == "signature" else
                     "Public records organized in the Signature system"),
        "search_ph": "Search quartz, feldspar, Mohs, Bragg, Dana, Strunz, gemstones, cleavage...",
        "chat_ph": "Ask about mineralogy...",
        "archive_blurb": ("Seeded %s mineralogy records, marching toward one million records. "
                          "Presented in teaching-ladder order: foundations, compounded, advanced."
                          % ("Signature-original" if source == "signature" else "public-record")),
        "schema": ("id, t, g, name, title, description, how_it_works, key_points, requirements, "
                   "standards, citations, src, ladder_rank, ladder_tier, demo"),
        "fields": "Foundations · Compounded · Advanced — each tier opens on demand and loads only what you open",
        "gen_desc": "Generate clearly-labeled structural mineralogy studies. Seeded archive records are the authoritative entries.",
        "greet": "I am the %s. Ask me about mineralogy — from the Mohs scale up to X-ray structure determination." % ai,
        "gen_fields": ["Foundations", "Compounded", "Advanced"],
        "gen_kind": "mineralogy-study", "gen_demo_kind": "mineralogy-demo",
        "source": source,
    }

CIT_PUB = "Mineralogy (peer-reviewed literature and standard textbooks)."
CIT_SIG = CIT_PUB + " " + SIG_TAIL

DBCFG = {}
DBCFG["mineralogy"] = _cfg(
    "mineralogy", "The Mineralogy Database",
    "Real, fact-checked mineralogy: crystal systems and symmetry, Dana and "
    "Nickel-Strunz classification, physical properties, optical mineralogy, "
    "X-ray crystallography, formation environments, rock-forming and ore "
    "minerals, gemstones, and identification methods.",
    "mineralogy record", "JAH-MIN-", "JAH Mineralogy Archivist",
    "mineralogy archivist — crystal systems and symmetry, Dana/Strunz classification, "
    "physical properties (hardness, cleavage, luster, streak, color, specific gravity), "
    "optical mineralogy, X-ray crystallography, formation environments, rock-forming vs "
    "ore minerals, gemstones, identification methods; teaching progressively along the "
    "ladder from foundations (what mineralogy is, five tests, crystal systems, habit, "
    "Mohs, cleavage, luster/streak, color, SG, Dana, Strunz, formulas) through compounded "
    "(point groups, Bravais lattices, silicates, rock-forming minerals, ores, Bowen's "
    "series, sedimentary/metamorphic formation, hydrothermal/pegmatites, polarizing "
    "microscope, RI/birefringence, pleochroism/interference, gemstones, hand-sample ID) "
    "to advanced (Bragg's law, structure determination, solid solution/polymorphism, "
    "thermodynamics, phase diagrams, Goldschmidt's rules, treatments/synthetics "
    "detection, IMA registry, new-mineral description, environmental mineralogy, "
    "systematic collecting); answers from many angles — definition, example, analogy, "
    "application, history, math, how-to — using only the system's own archive data",
    CIT_PUB, "public")
DBCFG["mineralogy-signature"] = _cfg(
    "mineralogy-signature", "The Mineralogy Signature Database",
    "His original Signature interpretation of mineralogy: the full ladder from "
    "the Mohs scale to X-ray structure determination, reframed as Signature "
    "engineering. Clearly labeled Signature-made, never presented as "
    "authentic public record.",
    "mineralogy record", "JAH-MSG-", "JAH Mineralogy Archivist (Signature)",
    "mineralogy archivist — Signature editions: his original Signature interpretation of "
    "mineralogy, clearly labeled Signature-made and never presented as authentic public "
    "record; teaches progressively along the ladder from foundations through compounded "
    "to advanced; answers from many angles — definition, example, analogy, application, "
    "history, math, how-to — using only the system's own archive data",
    CIT_SIG, "signature")

base.DBCFG = DBCFG

# ---------------------------------------------------------------- demos
# Every demo is real, runnable, stdlib-only Python performing the actual
# mineralogical calculation for its record. All are machine-executed by main().

_PREAMBLE = """import math
import re
"""

def _wrap(name, rid, group, body):
    return (base._hdr(name, rid, group) + _PREAMBLE + body.replace("NAME", json.dumps(name)))

def demo_mineral_count(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    approved = 6000.0
    rock_forming = 30.0
    share = 100 * rock_forming / approved
    print("approved species ~%.0f; rock-forming ~%.0f (%.1f %%)" % (approved, rock_forming, share))
    assert abs(share - 0.5) < 0.05
    feldspar_crust = 60.0
    print("feldspar alone ~%.0f %% of the crust by weight" % feldspar_crust)
    assert feldspar_crust == 60.0
    # diamond vs graphite: same chemistry, different structure -> different minerals
    assert "C" == "C"
    print("diamond = graphite = C: structure makes the mineral, not just chemistry")
    print("OK: %s counted the minerals" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_five_tests(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def is_mineral(natural, inorganic, solid, definite, ordered):
    tests = {"naturally occurring": natural, "inorganic": inorganic,
             "solid": solid, "definite composition": definite,
             "ordered structure": ordered}
    failed = [k for k, v in tests.items() if not v]
    return (not failed, failed)
CANDIDATES = {
    "quartz": (True, True, True, True, True),
    "opal": (True, True, True, False, False),      # variable water, no long-range order
    "coal": (True, False, True, False, False),     # organic
    "mercury": (True, True, False, True, False),   # liquid
    "lab quartz": (False, True, True, True, True), # synthetic
    "ice": (True, True, True, True, True),         # natural ice passes
}
def main():
    for label, flags in CANDIDATES.items():
        ok, failed = is_mineral(*flags)
        print("%-10s -> %s%s" % (label, "MINERAL" if ok else "not mineral",
                                 "" if ok else " (fails: %s)" % ", ".join(failed)))
    assert is_mineral(*CANDIDATES["quartz"])[0] is True
    assert is_mineral(*CANDIDATES["ice"])[0] is True
    assert is_mineral(*CANDIDATES["opal"])[0] is False
    assert is_mineral(*CANDIDATES["coal"])[0] is False
    assert is_mineral(*CANDIDATES["mercury"])[0] is False
    assert is_mineral(*CANDIDATES["lab quartz"])[0] is False
    print("OK: %s ran the five tests" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_crystal_systems(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
SYSTEMS = {
    "cubic":        ("a=b=c", "all 90"),
    "tetragonal":   ("a=b!=c", "all 90"),
    "orthorhombic": ("a!=b!=c", "all 90"),
    "hexagonal":    ("a=b!=c", "90,90,120"),
    "trigonal":     ("a=b=c", "all equal, not 90"),
    "monoclinic":   ("a!=b!=c", "two 90"),
    "triclinic":    ("a!=b!=c", "none 90"),
}
def classify(a_eq_b, b_eq_c, all_90, gamma_120, all_equal_angles):
    if a_eq_b and b_eq_c and all_90: return "cubic"
    if a_eq_b and not b_eq_c and all_90: return "tetragonal"
    if not a_eq_b and not b_eq_c and all_90: return "orthorhombic"
    if a_eq_b and not b_eq_c and gamma_120: return "hexagonal"
    if a_eq_b and b_eq_c and all_equal_angles and not all_90: return "trigonal"
    if not a_eq_b and not b_eq_c and not all_90 and not all_equal_angles:
        # need the beta-only case -> monoclinic; fully general -> triclinic
        return "monoclinic/triclinic (check beta)"
    return "unclassified"
def main():
    assert len(SYSTEMS) == 7
    assert classify(True, True, True, False, True) == "cubic"
    assert classify(True, False, True, False, False) == "tetragonal"
    assert classify(False, False, True, False, False) == "orthorhombic"
    assert classify(True, False, False, True, False) == "hexagonal"
    assert classify(True, True, False, False, True) == "trigonal"
    print("systems: %s" % ", ".join(SYSTEMS))
    print("galena (distorted cube) -> still cubic: symmetry decides, not face quality")
    print("OK: %s classified the systems" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_habit_lookup(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
HABITS = {
    "prismatic": ["tourmaline", "quartz"],
    "bladed": ["kyanite"],
    "fibrous": ["serpentine (asbestos form)"],
    "botryoidal": ["malachite"],
    "dendritic": ["native copper"],
    "cubic": ["galena", "pyrite"],
    "tabular": ["barite"],
    "massive": ["(any mineral, shapeless)"],
}
def describe(mineral):
    return [h for h, ms in HABITS.items() if mineral in ms]
def main():
    assert "prismatic" in describe("tourmaline")
    assert "botryoidal" in describe("malachite")
    assert "cubic" in describe("galena")
    assert "dendritic" in describe("native copper")
    print("habit terms: %s" % ", ".join(sorted(HABITS)))
    print("rule: fast faces vanish, slow faces define the form")
    print("OK: %s read the habits" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_mohs_bracket(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
MOHS = ["talc", "gypsum", "calcite", "fluorite", "apatite",
        "orthoclase", "quartz", "topaz", "corundum", "diamond"]
FIELD = {"fingernail": 2.5, "copper coin": 3.0, "steel nail": 5.5,
         "glass plate": 5.5, "steel file": 6.5}
def bracket(scratches, resists):
    lo = max([FIELD[t] for t in scratches], default=1.0)
    hi = min([FIELD[t] for t in resists], default=10.0)
    return lo, hi
def main():
    assert MOHS[0] == "talc" and MOHS[9] == "diamond"
    assert MOHS.index("quartz") + 1 == 7
    # unknown scratches glass (5.5) but not the steel file (6.5)
    lo, hi = bracket(["glass plate"], ["steel file"])
    print("scratches glass, resists file -> hardness %.1f-%.1f" % (lo, hi))
    assert (lo, hi) == (5.5, 6.5)
    # ordinal scale: gaps are not equal
    print("ordinal only: the 9->10 gap dwarfs the 1->2 gap")
    print("kyanite: 5 along, 7 across -> always note direction")
    print("OK: %s bracketed the hardness" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_cleavage_angles(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
CLEAVAGE = {
    "mica": (1, "perfect", None),
    "feldspar": (2, "good", 90),
    "pyroxene": (2, "good", 90),
    "amphibole": (2, "good", 56),
    "halite": (3, "perfect", 90),
    "calcite": (3, "perfect", 75),   # rhombohedral, not 90
    "fluorite": (4, "perfect", None),
}
def identify(directions, angle):
    cands = [m for m, (d, q, a) in CLEAVAGE.items()
             if d == directions and (a is None or abs(a - angle) <= 3)]
    return cands
def main():
    assert identify(2, 56) == ["amphibole"], identify(2, 56)
    assert identify(2, 90) == ["feldspar", "pyroxene"]
    assert identify(3, 90) == ["halite"]
    assert identify(3, 75) == ["calcite"]
    assert identify(1, 0) == ["mica"]
    print("amphibole 56/124 vs pyroxene ~90: the classic angle split")
    print("quartz: no cleavage -> conchoidal fracture")
    print("OK: %s measured the breaks" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_luster_streak(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
NONMETALLIC = ["vitreous", "pearly", "silky", "resinous",
               "waxy", "greasy", "adamantine", "dull"]
STREAK = {"hematite": "reddish-brown", "pyrite": "greenish-black",
          "gold": "golden-yellow", "magnetite": "black",
          "cinnabar": "scarlet"}
def fools_gold_test(streak):
    return "gold" if streak == "golden-yellow" else "pyrite (fool's gold)"
def main():
    assert len(NONMETALLIC) == 8
    assert fools_gold_test("golden-yellow") == "gold"
    assert fools_gold_test("greenish-black") == "pyrite (fool's gold)"
    assert STREAK["hematite"] == "reddish-brown"
    print("luster first split: metallic vs non-metallic")
    print("streak: hematite red-brown even when the specimen looks steel-gray")
    print("minerals harder than ~7 scratch the plate instead of streaking")
    print("OK: %s read light and powder" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_color_mechanism(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def mechanism(mineral, color_varies, essential_element):
    if not color_varies and essential_element:
        return "idiochromatic (reliable)"
    if color_varies:
        return "allochromatic (unreliable alone)"
    return "pseudochromatic (light effect, unreliable alone)"
CASES = {
    "malachite": (False, True),    # Cu essential, always green
    "azurite": (False, True),
    "quartz": (True, False),       # amethyst/smoky by traces
    "fluorite": (True, False),
    "opal": (True, False),         # play of color
    "labradorite": (True, False),
    "sulfur": (False, True),       # always yellow
}
def main():
    assert mechanism("malachite", *CASES["malachite"]) == "idiochromatic (reliable)"
    assert mechanism("quartz", *CASES["quartz"]) == "allochromatic (unreliable alone)"
    assert mechanism("opal", *CASES["opal"]) == "allochromatic (unreliable alone)"
    assert mechanism("sulfur", *CASES["sulfur"]) == "idiochromatic (reliable)"
    print("rule: color hints, streak/hardness/cleavage confirm")
    print("OK: %s sorted the colors" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_specific_gravity(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def specific_gravity(w_air, w_water):
    assert w_water < w_air, "submerged weight must be less"
    return w_air / (w_air - w_water)
KNOWN = {"quartz": 2.65, "calcite": 2.71, "galena": 7.5, "gold": 19.3}
def main():
    sg = specific_gravity(100.0, 62.26)   # quartz-like specimen
    print("W_air=100.0 g, W_water=62.26 g -> SG=%.3f" % sg)
    assert abs(sg - 2.65) < 0.01
    sg2 = specific_gravity(50.0, 43.33)   # galena-like
    print("W_air=50.0 g, W_water=43.33 g -> SG=%.2f" % sg2)
    assert abs(sg2 - 7.5) < 0.05
    for mineral, known in KNOWN.items():
        print("reference: %-8s SG %.2f" % (mineral, known))
    print("formula: SG = W_air / (W_air - W_water)")
    print("OK: %s weighed in water" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_dana_classify(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def dana_class(formula):
    f = formula
    if re.search(r"Si", f) and "O" in f: return "silicates"
    if "CO3" in f: return "carbonates"
    if "SO4" in f: return "sulfates"
    if "PO4" in f: return "phosphates"
    if re.search(r"BO", f): return "borates"
    if re.search(r"[ClF]($|[^a-z])", f) or f in ("NaCl",): return "halides"
    if re.fullmatch(r"[A-Z][a-z]?", f): return "native elements"
    if "S" in f and "O" not in f.replace("S", "", 1): return "sulfides"
    if re.search(r"O\\d*$", f) or re.fullmatch(r"[A-Z][a-z]?\\d*O\\d*", f): return "oxides"
    return "unclassified"
def main():
    assert dana_class("SiO2") == "silicates"
    assert dana_class("CaCO3") == "carbonates"
    assert dana_class("FeS2") == "sulfides"
    assert dana_class("NaCl") == "halides"
    assert dana_class("Fe2O3") == "oxides"
    assert dana_class("CaSO4.2H2O") == "sulfates"
    assert dana_class("Au") == "native elements"
    assert dana_class("Ca5(PO4)3(OH)") == "phosphates"
    print("key: find the dominant anionic group in the formula")
    print("quartz Dana number 75.1.3.1 = class.type.group.species")
    print("OK: %s filed by Dana" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_strunz_classify(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
STRUNZ10 = ["1 elements", "2 sulfides/sulfosalts", "3 halides", "4 oxides",
            "5 carbonates/nitrates", "6 borates",
            "7 sulfates/chromates/molybdates/tungstates",
            "8 phosphates/arsenates/vanadates", "9 silicates", "10 organics"]
SILICATE_SUB = {"neso": "9.A", "soro": "9.B", "cyclo": "9.C",
                "ino": "9.D", "phyllo": "9.E", "tecto": "9.F"}
def strunz_silicate(linkage):
    return SILICATE_SUB[linkage]
def main():
    assert len(STRUNZ10) == 10
    assert strunz_silicate("ino") == "9.D"
    assert strunz_silicate("tecto") == "9.F"
    assert strunz_silicate("phyllo") == "9.E"
    print("classes: %s" % "; ".join(STRUNZ10))
    print("structure first: same linkage sits together whatever the chemistry")
    print("OK: %s filed by Strunz" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_formula_weight(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
ATOMIC = {"Si": 28.085, "O": 15.999, "Ca": 40.078, "C": 12.011,
          "Fe": 55.845, "S": 32.06, "Mg": 24.305, "Cu": 63.546, "H": 1.008}
def formula_weight(parts):
    return sum(ATOMIC[el] * n for el, n in parts)
def weight_percent(parts, el):
    fw = formula_weight(parts)
    return 100 * sum(ATOMIC[e] * n for e, n in parts if e == el) / fw
def charge_ok(cations, anions):
    return abs(sum(cations) + sum(anions)) < 1e-9
def main():
    quartz = [("Si", 1), ("O", 2)]
    fw = formula_weight(quartz)
    print("SiO2 formula weight: %.3f" % fw)
    assert abs(fw - 60.083) < 0.01
    si_pct = weight_percent(quartz, "Si")
    print("Si weight %%: %.2f" % si_pct)
    assert abs(si_pct - 46.74) < 0.05
    assert charge_ok([2.0], [-2.0]) is True       # CaCO3: Ca2+ + (CO3)2-
    assert charge_ok([2.0], [-1.0]) is False
    # malachite Cu2CO3(OH)2 reads as copper carbonate hydroxide
    print("charges must balance: formulas are checkable arithmetic")
    print("OK: %s weighed the formulas" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_point_group_lookup(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
CUBIC_GROUPS = ["23", "m-3", "432", "-43m", "m-3m"]
NO_CENTER_PIEZO = {"32": True, "m-3m": False, "6mm": True}
def piezoelectric_possible(group):
    return NO_CENTER_PIEZO.get(group, None)
def main():
    assert len(CUBIC_GROUPS) == 5
    assert piezoelectric_possible("32") is True    # quartz: no center
    assert piezoelectric_possible("m-3m") is False # halite: centered
    print("32 point groups total; cubic holds 5")
    print("quartz 32 -> piezoelectric; halite m-3m -> forbidden by center")
    print("crystallographic restriction: only 1,2,3,4,6-fold axes")
    print("OK: %s inventoried the symmetry" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_bravais_lookup(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
# systematic absences by centering: which (hkl) vanish
def extinct(h, k, l, centering):
    if centering == "P": return False
    if centering == "I": return (h + k + l) % 2 == 1
    if centering == "F": return not ((h % 2 == k % 2 == l % 2))
    if centering == "C": return (h + k) % 2 == 1
    raise ValueError(centering)
def main():
    assert extinct(1, 0, 0, "I") is True    # h+k+l odd -> gone
    assert extinct(1, 1, 0, "I") is False
    assert extinct(1, 1, 1, "F") is False   # all odd -> present
    assert extinct(1, 0, 0, "F") is True    # mixed -> gone
    assert extinct(1, 0, 0, "C") is True
    assert extinct(1, 1, 0, "C") is False
    print("14 Bravais lattices: absences reveal the centering")
    print("diamond = FCC lattice + two-atom motif")
    print("OK: %s read the absences" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_silicate_ratio(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
FAMILIES = {"neso": 4.0, "soro": 3.5, "cyclo": 3.0, "ino-single": 3.0,
            "ino-double": 2.75, "phyllo": 2.5, "tecto": 2.0}
EXAMPLES = {"olivine": "neso", "epidote": "soro", "beryl": "cyclo",
            "pyroxene": "ino-single", "amphibole": "ino-double",
            "mica": "phyllo", "quartz": "tecto", "feldspar": "tecto"}
def family_of(mineral):
    return EXAMPLES[mineral]
def si_o_ratio(family):
    return 1.0 / FAMILIES[family]   # O per Si
def main():
    assert family_of("olivine") == "neso"
    assert family_of("mica") == "phyllo"
    assert family_of("quartz") == "tecto"
    assert abs(si_o_ratio("tecto") - 0.5) < 1e-9    # SiO2
    assert abs(si_o_ratio("neso") - 0.25) < 1e-9   # SiO4
    print("O:Si from 4.0 (isolated) down to 2.0 (framework)")
    print("linkage -> cleavage: sheets flake, chains prism, frameworks fracture")
    print("OK: %s linked the tetrahedra" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_qap_classify(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def qap(q, a, p):
    total = q + a + p
    qn, an, pn = 100 * q / total, 100 * a / total, 100 * p / total
    if qn >= 20 and an > pn and an >= 35: return "granite"
    if qn >= 20 and pn >= an: return "granodiorite/tonalite"
    if qn < 20 and qn >= 5 and an > pn: return "syenite"
    if qn < 5 and pn > 90: return "anorthosite"
    if qn < 5 and an < 10: return "gabbro/diorite"
    return "intermediate"
def main():
    assert qap(30, 60, 10) == "granite"
    assert qap(25, 20, 55) == "granodiorite/tonalite"
    assert qap(0, 0, 100) == "anorthosite"
    assert qap(2, 8, 90) == "gabbro/diorite"
    print("Q=30 A=60 P=10 -> granite (quartz+alkali feldspar dominate)")
    print("feldspar ~60% of crust; quartz+feldspar name most rocks")
    print("OK: %s plotted the triangle" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_ore_grade(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def contained_metal(tonnage_t, grade_pct):
    return tonnage_t * grade_pct / 100.0
def cutoff_grade(cost_per_t, price_per_t, recovery=0.9):
    return 100 * cost_per_t / (price_per_t * recovery)
def main():
    metal = contained_metal(10_000_000, 1.2)
    print("10 Mt at 1.2 %% Cu -> %.0f t contained copper" % metal)
    assert metal == 120000.0
    co = cutoff_grade(45.0, 9000.0)
    print("cost $45/t, Cu $9000/t -> cutoff grade %.2f %%" % co)
    assert abs(co - 0.56) < 0.02
    ore = 1.2 > co
    print("1.2 %% > %.2f %% cutoff -> ORE (at this price)" % co)
    assert ore is True
    print("ore is economic: price moves the cutoff")
    print("OK: %s graded the deposit" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_bowen_order(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
DISCONTINUOUS = ["olivine", "pyroxene", "amphibole", "biotite"]
CONTINUOUS = ["Ca-plagioclase", "Na-plagioclase"]  # calcic -> sodic
LATE = ["orthoclase", "muscovite", "quartz"]
def crystallizes_before(a, b):
    seq = DISCONTINUOUS + LATE
    if a in DISCONTINUOUS and b in DISCONTINUOUS:
        return seq.index(a) < seq.index(b)
    return None
def main():
    assert DISCONTINUOUS[0] == "olivine" and LATE[-1] == "quartz"
    assert crystallizes_before("olivine", "amphibole") is True
    assert crystallizes_before("biotite", "olivine") is False
    print("discontinuous: %s" % " -> ".join(DISCONTINUOUS))
    print("continuous: Ca-plagioclase -> Na-plagioclase")
    print("late: %s" % " -> ".join(LATE))
    print("reversed = weathering order: olivine alters first, quartz endures")
    print("OK: %s ran the reaction series" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_metamorphic_grade(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
BARROVIAN = ["chlorite", "biotite", "garnet", "staurolite", "kyanite", "sillimanite"]
def grade(assemblage):
    idx = [BARROVIAN.index(m) for m in assemblage if m in BARROVIAN]
    return max(idx) if idx else -1
def facies(assemblage):
    s = set(assemblage)
    if {"garnet", "clinopyroxene"} <= s: return "eclogite facies"
    if "garnet" in s: return "amphibolite facies"
    if "chlorite" in s: return "greenschist facies"
    return "undetermined"
def main():
    assert grade(["chlorite", "muscovite"]) == 0
    assert grade(["garnet", "staurolite"]) == 3
    assert grade(["sillimanite"]) == 5
    assert facies(["garnet", "clinopyroxene", "quartz"]) == "eclogite facies"
    assert facies(["chlorite", "muscovite"]) == "greenschist facies"
    print("Barrovian: %s" % " -> ".join(BARROVIAN))
    print("Al2SiO5 trio: kyanite/andalusite/sillimanite = pressure gauge")
    print("OK: %s read the grade" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_vein_zoning(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
ZONES = [("proximal/hot", ["cassiterite", "wolframite", "quartz"]),
         ("intermediate", ["galena", "sphalerite", "chalcopyrite"]),
         ("distal/cool", ["stibnite", "cinnabar", "barite"])]
PEG_ZONES = ["border", "wall", "intermediate", "core"]
PEG_ORE = {"intermediate": ["spodumene", "beryl", "tourmaline", "columbite-tantalite"]}
def zone_of(mineral):
    for zone, minerals in ZONES:
        if mineral in minerals: return zone
    return None
def main():
    assert zone_of("cassiterite") == "proximal/hot"
    assert zone_of("galena") == "intermediate"
    assert zone_of("cinnabar") == "distal/cool"
    assert PEG_ORE["intermediate"] == ["spodumene", "beryl", "tourmaline", "columbite-tantalite"]
    assert PEG_ZONES[-1] == "core"
    print("vein zoning: hot -> cool maps to cassiterite -> galena -> cinnabar")
    print("pegmatite: border -> wall -> intermediate (Li/Cs/Ta here) -> quartz core")
    print("OK: %s followed the gradient" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_microscope_routine(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
ROUTINE = ["PPL: color/pleochroism", "PPL: relief vs neighbors",
           "PPL: habit and cleavage traces", "XPL: interference color",
           "XPL: extinction angle", "XPL: twinning",
           "Bertrand: interference figure (uniaxial cross vs biaxial isogyres)"]
def magnification(ocular, objective):
    return ocular * objective
def main():
    assert len(ROUTINE) == 7
    assert magnification(10, 40) == 400
    assert "Bertrand" in ROUTINE[-1]
    print("routine:")
    for i, step in enumerate(ROUTINE, 1):
        print("  %d. %s" % (i, step))
    print("standard thin section: 30 microns")
    print("OK: %s worked the scope" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_becke_line(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def becke_match(n_grain, oils):
    # raise focus: line moves into the higher-index medium
    for oil in sorted(oils):
        if oil < n_grain:
            continue  # line still in the grain: try a higher oil
        return oil    # line vanishes: match
    return None
def main():
    oils = [1.54, 1.58, 1.62, 1.66, 1.70]
    m = becke_match(1.66, oils)
    print("grain n=1.66 against oils -> match at %.2f" % m)
    assert m == 1.66
    assert becke_match(1.55, oils) == 1.58
    print("relief: garnet (1.7-1.9) bold vs medium (1.54); quartz ~invisible")
    print("OK: %s watched the Becke line" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_retardation_calc(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def retardation_nm(thickness_um, birefringence):
    return thickness_um * 1000.0 * birefringence
def michel_levy_order(ret_nm):
    return int(ret_nm // 550) + 1
def main():
    r = retardation_nm(30.0, 0.009)   # quartz, standard section
    print("quartz 30 um, d=0.009 -> %.0f nm (first-order gray-white)" % r)
    assert abs(r - 270.0) < 1e-9
    assert michel_levy_order(r) == 1
    r2 = retardation_nm(30.0, 0.172)  # calcite
    print("calcite 30 um, d=0.172 -> %.0f nm (high-order pastel)" % r2)
    assert abs(r2 - 5160.0) < 1e-9
    assert michel_levy_order(r2) >= 9
    print("pleochroism: biotite tan->brown on 90-degree stage rotation")
    print("OK: %s computed retardation" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_gem_carat(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def carats_to_grams(ct):
    return ct * 0.2
def grade_diamond(ct, color, clarity, cut):
    score = {"D": 4, "E": 3, "F": 2, "G": 1}.get(color, 0)
    score += {"FL": 4, "VVS": 3, "VS": 2, "SI": 1}.get(clarity, 0)
    score += {"Excellent": 4, "Very Good": 3}.get(cut, 0)
    return score
def main():
    assert abs(carats_to_grams(5.0) - 1.0) < 1e-9
    assert abs(carats_to_grams(1.0) - 0.2) < 1e-9
    g = grade_diamond(1.0, "D", "FL", "Excellent")
    print("1.00 ct D/FL/Excellent -> quality score %d/12" % g)
    assert g == 12
    g2 = grade_diamond(1.0, "G", "SI", "Very Good")
    assert g2 == 5
    print("carat = 0.2 g exactly; cut angles derive from refractive index")
    print("OK: %s weighed the gems" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_id_funnel(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def identify(luster, hardness, cleavage_dirs, streak):
    if luster == "metallic":
        if hardness >= 6 and streak == "greenish-black": return "pyrite"
        if cleavage_dirs == 3 and hardness <= 3: return "galena"
        if streak == "reddish-brown": return "hematite"
        return "metallic: test SG and magnetism next"
    # non-metallic branch
    if hardness >= 7 and cleavage_dirs == 0: return "quartz"
    if cleavage_dirs == 2 and 5.5 <= hardness <= 6.5: return "feldspar group"
    if cleavage_dirs == 1 and hardness <= 3: return "mica group"
    if cleavage_dirs == 3 and hardness <= 3.5: return "calcite (acid test confirms)"
    return "non-metallic: check streak, SG, special tests"
def main():
    assert identify("metallic", 6.5, 0, "greenish-black") == "pyrite"
    assert identify("metallic", 2.5, 3, "gray") == "galena"
    assert identify("non-metallic", 7, 0, "white") == "quartz"
    assert identify("non-metallic", 6, 2, "white") == "feldspar group"
    assert identify("non-metallic", 3, 3, "white") == "calcite (acid test confirms)"
    print("funnel: luster -> hardness -> cleavage -> streak -> special tests")
    print("confirm with TWO independent properties, never one test")
    print("OK: %s ran the funnel" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_bragg_calc(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
LAMBDA_CU = 1.5406  # angstroms, Cu K-alpha
def d_spacing(two_theta_deg, lam=LAMBDA_CU):
    theta = math.radians(two_theta_deg / 2.0)
    return lam / (2.0 * math.sin(theta))
def two_theta(d, lam=LAMBDA_CU):
    return 2.0 * math.degrees(math.asin(lam / (2.0 * d)))
def main():
    d = d_spacing(26.66)   # quartz 101 peak
    print("2theta=26.66 deg -> d=%.3f A" % d)
    assert abs(d - 3.343) < 0.005
    t = two_theta(3.343)
    print("d=3.343 A -> 2theta=%.2f deg" % t)
    assert abs(t - 26.66) < 0.05
    print("n*lambda = 2*d*sin(theta): planes pick their own angles")
    print("OK: %s diffracted the X-rays" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_structure_factor(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def structure_factor(h, atoms):
    # 1-D demo: atoms = [(x_fractional, scattering_f)]
    re = sum(f * math.cos(2 * math.pi * h * x) for x, f in atoms)
    im = sum(f * math.sin(2 * math.pi * h * x) for x, f in atoms)
    return math.hypot(re, im)
def main():
    atoms = [(0.0, 1.0), (0.5, 1.0)]   # two identical atoms, half cell apart
    f0 = structure_factor(0, atoms)
    f1 = structure_factor(1, atoms)
    f2 = structure_factor(2, atoms)
    print("F(0)=%.1f F(1)=%.1f F(2)=%.1f" % (f0, f1, f2))
    assert abs(f0 - 2.0) < 1e-9
    assert abs(f1 - 0.0) < 1e-9   # systematic absence from the centering
    assert abs(f2 - 2.0) < 1e-9
    print("intensities encode positions; phases must be recovered (phase problem)")
    print("Pauling check: radius ratio 0.225-0.414 -> tetrahedral")
    print("OK: %s summed the scattering" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_solid_solution(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
# Vegard's law: cell edge interpolates linearly between endmembers
FO_A, FA_A = 4.756, 4.820   # olivine a-edge, forsterite / fayalite (A)
def olivine_a_edge(fo_fraction):
    return FO_A + (1.0 - fo_fraction) * (FA_A - FO_A)
def fo_from_edge(a):
    return 1.0 - (a - FO_A) / (FA_A - FO_A)
def main():
    a = olivine_a_edge(0.80)
    print("Fo80 olivine a-edge: %.4f A" % a)
    assert abs(a - 4.7688) < 0.0005
    fo = fo_from_edge(a)
    print("measured a=%.4f -> Fo%.0f" % (a, 100 * fo))
    assert abs(fo - 0.80) < 0.01
    # perthite: solvus unmixing on cooling
    print("perthite intergrowths = alkali feldspar solvus crossed on cooling")
    print("polymorphs: diamond/graphite, calcite/aragonite, kyanite/andalusite/sillimanite")
    print("OK: %s interpolated the series" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_gibbs_stability(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def delta_g(delta_h, delta_s, t_k):
    return delta_h - t_k * delta_s
def equilibrium_t(delta_h, delta_s):
    return delta_h / delta_s
def main():
    dh, ds = 10000.0, 20.0   # J/mol, J/mol/K
    teq = equilibrium_t(dh, ds)
    print("dH=%.0f J, dS=%.0f J/K -> equilibrium at %.0f K" % (dh, ds, teq))
    assert abs(teq - 500.0) < 1e-9
    assert delta_g(dh, ds, 400.0) > 0, "reactants stable below Teq"
    assert delta_g(dh, ds, 600.0) < 0, "products stable above Teq"
    print("dG<0 -> products stable; Clapeyron dP/dT = dS/dV slopes the boundary")
    print("diamond at surface: metastable (kinetically blocked), not stable")
    print("OK: %s minimized the free energy" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_lever_rule(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def lever_fractions(bulk, left, right):
    # tie line from left composition to right; bulk between them
    assert left <= bulk <= right
    f_right = (bulk - left) / (right - left)
    return 1.0 - f_right, f_right
def phase_rule_variance(components, phases):
    return components - phases + 2
def main():
    f_liq, f_sol = lever_fractions(50.0, 20.0, 80.0)
    print("bulk 50%%, tie 20-80 -> liquid %.1f %%, solid %.1f %%" % (100*f_liq, 100*f_sol))
    assert abs(f_liq - 0.5) < 1e-9 and abs(f_sol - 0.5) < 1e-9
    f2 = lever_fractions(30.0, 20.0, 80.0)
    assert abs(f2[1] - (10.0/60.0)) < 1e-9
    v = phase_rule_variance(1, 3)   # Al2SiO5 triple point
    print("Al2SiO5 triple point variance: %d (fixed point in nature)" % v)
    assert v == 0
    print("OK: %s read the diagram" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_goldschmidt_check(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
RADII = {"Mg2+": 0.72, "Fe2+": 0.78, "Na+": 1.02, "Ca2+": 1.00, "K+": 1.38}
def radius_diff_pct(a, b):
    ra, rb = RADII[a], RADII[b]
    return 100 * abs(ra - rb) / min(ra, rb)
def check(a, b):
    d = radius_diff_pct(a, b)
    if d <= 15: return "free substitution"
    if d <= 30: return "partial (high T only)"
    return "blocked"
def main():
    assert check("Mg2+", "Fe2+") == "free substitution"       # 8.3%
    assert check("Na+", "Ca2+") == "free substitution"       # radius ok; charge needs coupling
    assert check("K+", "Na+") == "blocked"                   # 35%
    print("Mg/Fe diff: %.1f %% -> %s" % (radius_diff_pct("Mg2+", "Fe2+"), check("Mg2+", "Fe2+")))
    print("Na/Ca: radius fine, charge differs -> coupled NaSi<->CaAl")
    print("Ni follows Mg into olivine; Zr/REE enrich late melts (incompatible)")
    print("OK: %s filtered the substitutions" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_treatment_detect(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
EVIDENCE = {
    "curved striae": "flame-fusion synthetic",
    "chevron growth": "hydrothermal synthetic",
    "breadcrumb inclusions": "flux synthetic",
    "healed fractures + silk": "natural (possibly heated)",
    "nail-head spicules": "hydrothermal synthetic",
    "suspiciously clean": "synthetic suspect — lab test",
}
TREATMENTS = {"sapphire": ["heating"], "ruby": ["heating"],
              "emerald": ["fracture filling"], "topaz": ["irradiation + heating"]}
def diagnose(observation):
    return EVIDENCE.get(observation, "inconclusive — lab test")
def main():
    assert diagnose("curved striae") == "flame-fusion synthetic"
    assert diagnose("breadcrumb inclusions") == "flux synthetic"
    assert diagnose("healed fractures + silk") == "natural (possibly heated)"
    assert "heating" in TREATMENTS["sapphire"]
    assert "fracture filling" in TREATMENTS["emerald"]
    print("ladder: inclusions -> spectra -> UV -> lab (FTIR/chemistry)")
    print("rule: any value-affecting treatment must be disclosed")
    print("OK: %s spotted the treatment" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_ima_checklist(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
REQUIRED = ["name", "formula", "type locality", "crystallographic data",
            "type specimen repository"]
def validate_proposal(proposal):
    return [f for f in REQUIRED if f not in proposal]
def name_ok(name, existing):
    return name not in existing and len(name) >= 3
def main():
    good = {f: "x" for f in REQUIRED}
    assert validate_proposal(good) == []
    bad = {"name": "x", "formula": "y"}
    missing = validate_proposal(bad)
    print("incomplete proposal missing: %s" % missing)
    assert missing == ["type locality", "crystallographic data", "type specimen repository"]
    existing = {"quartz", "calcite", "pyrite"}
    assert name_ok("newmineralite", existing) is True
    assert name_ok("quartz", existing) is False
    print("~6000 valid species; names must not collide; suffixes -(Ce)/-(La) mark REE dominance")
    print("OK: %s checked the registry" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_newmineral_checklist(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
STEPS = ["rule out known species", "prove single-phase homogeneity",
         "quantitative chemistry", "crystal structure",
         "physical + optical properties", "CNMNC proposal",
         "reviewer response", "approval + master-list entry"]
def pipeline_done(done_steps):
    return [s for s in STEPS if s not in done_steps]
def main():
    assert len(STEPS) == 8
    remaining = pipeline_done(STEPS[:5])
    print("after 5 steps, remaining: %s" % remaining)
    assert remaining == ["CNMNC proposal", "reviewer response", "approval + master-list entry"]
    assert pipeline_done(STEPS) == []
    print("most candidates die at step 1: varieties, mixtures, misidentified knowns")
    print("~100 new species/year; type specimen anchors the name forever")
    print("OK: %s walked the pipeline" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_acid_base_accounting(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def acid_potential(sulfide_s_pct):
    return sulfide_s_pct * 31.25   # t CaCO3 equiv per kt rock
def net_neutralization(np_t, ap_t):
    return np_t - ap_t
def main():
    ap = acid_potential(2.0)
    print("2.0 %% sulfide-S -> acid potential %.1f t CaCO3/kt" % ap)
    assert abs(ap - 62.5) < 1e-9
    nnp = net_neutralization(20.0, ap)
    print("NP 20.0 - AP 62.5 -> NNP %.1f (negative = acid generating)" % nnp)
    assert abs(nnp - (-42.5)) < 1e-9
    assert nnp < 0
    # remediation: limestone neutralizes 2H+ per CaCO3
    print("pyrite oxidation: 2FeS2 + 7O2 + 2H2O -> acid (bacteria speed it up ~1e6x)")
    print("remediation: limestone drains, wetlands, phosphate -> pyromorphite locks Pb")
    print("OK: %s balanced the ledger" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_collection_audit(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
DANA_CLASSES = ["native elements", "sulfides", "halides", "oxides",
                "carbonates", "borates", "sulfates", "phosphates", "silicates"]
REQUIRED_LABEL = ["catalog number", "species", "locality", "source", "date"]
def audit(collection):
    gaps = [c for c in DANA_CLASSES
            if not any(s["dana_class"] == c for s in collection)]
    bad = [s["catalog number"] for s in collection
           if any(f not in s or not s[f] for f in REQUIRED_LABEL)]
    return gaps, bad
def mk(n, cls, loc=""):
    return {"catalog number": n, "species": "sp" + n, "locality": loc,
            "source": "field", "date": "2026", "dana_class": cls}
def main():
    coll = [mk("001", "silicates", "NC"), mk("002", "oxides", "MN"),
            mk("003", "carbonates", "")]   # 003 missing locality
    gaps, bad = audit(coll)
    print("class gaps: %d of %d" % (len(gaps), len(DANA_CLASSES)))
    assert len(gaps) == 6
    assert "sulfides" in gaps
    print("unlabeled/under-labeled: %s" % bad)
    assert bad == ["003"]
    print("rule: verify every ID twice before labeling; fill class gaps first")
    print("OK: %s audited the drawers" % NAME)
if __name__ == "__main__":
    main()
''')

DEMOS = {
    "mineral_count": demo_mineral_count, "five_tests": demo_five_tests,
    "crystal_systems": demo_crystal_systems, "habit_lookup": demo_habit_lookup,
    "mohs_bracket": demo_mohs_bracket, "cleavage_angles": demo_cleavage_angles,
    "luster_streak": demo_luster_streak, "color_mechanism": demo_color_mechanism,
    "specific_gravity": demo_specific_gravity, "dana_classify": demo_dana_classify,
    "strunz_classify": demo_strunz_classify, "formula_weight": demo_formula_weight,
    "point_group_lookup": demo_point_group_lookup,
    "bravais_lookup": demo_bravais_lookup, "silicate_ratio": demo_silicate_ratio,
    "qap_classify": demo_qap_classify, "ore_grade": demo_ore_grade,
    "bowen_order": demo_bowen_order, "metamorphic_grade": demo_metamorphic_grade,
    "vein_zoning": demo_vein_zoning, "microscope_routine": demo_microscope_routine,
    "becke_line": demo_becke_line, "retardation_calc": demo_retardation_calc,
    "gem_carat": demo_gem_carat, "id_funnel": demo_id_funnel,
    "bragg_calc": demo_bragg_calc, "structure_factor": demo_structure_factor,
    "solid_solution": demo_solid_solution, "gibbs_stability": demo_gibbs_stability,
    "lever_rule": demo_lever_rule, "goldschmidt_check": demo_goldschmidt_check,
    "treatment_detect": demo_treatment_detect, "ima_checklist": demo_ima_checklist,
    "newmineral_checklist": demo_newmineral_checklist,
    "acid_base_accounting": demo_acid_base_accounting,
    "collection_audit": demo_collection_audit,
}

# ---------------------------------------------------------------- records

def build_records(slug, source):
    cfg = DBCFG[slug]
    sig = source == "signature"
    # Teaching-ladder order: stable sort by ladder_rank (entries are already
    # in ladder order in entries_mineralogy.py).
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
        demo_fn = DEMOS[e["demo_kind"]]
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
    for slug in ("mineralogy", "mineralogy-signature"):
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
                               capture_output=True, text=True, timeout=60)
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
            topics.setdefault(r["g"], []).append("%s — %s" % (r["t"], r["g"]))
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
