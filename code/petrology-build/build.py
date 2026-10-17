#!/usr/bin/env python3
"""Build the Petrology field databases for JAH Databases (field #9, taxonomy order).

Verified 2026-10-17: NO database covers petrology as a science. Manifest
slug hit 'rocks-minerals' is a 52-record seed-generated specimen catalog
(rock overviews, FAQs, applications) with no igneous/metamorphic/sedimentary
petrology, no IUGS classification, no phase equilibria, no metamorphic
facies science, and no petrographic microscopy; 'geology' is the broad
generated geology database, not a dedicated petrology science database;
'petroleum-engineers' / 'public-petroleum-engineers' are oil-and-gas
industry databases, unrelated to petrology the science. So this build
creates two NEW databases:

  petrology              — The Petrology Database (public-harvest: real,
                           fact-checked petrology — igneous, sedimentary,
                           and metamorphic petrology; magma genesis;
                           Bowen's reaction series; IUGS, QAP, and TAS
                           classification; textures and structures;
                           sedimentary provenance and diagenesis;
                           carbonate petrology; metamorphic grade, facies,
                           and textures; phase equilibria and the lever
                           rule; geothermobarometry; petrographic
                           microscopy; igneous geochemistry; ophiolites;
                           granite petrogenesis; P-T-t paths; experimental
                           and field petrology)
  petrology-signature    — The Petrology Signature Database (his original
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
from entries_petrology import ENTRIES, SIG_TAIL

# ---------------------------------------------------------------- DB config

def _cfg(slug, name, tagline, record_kind, prefix, ai, role, citation, source):
    sig_line = ("Signature originals — his original Signature interpretation of petrology: "
                "clearly labeled Signature-made, never presented as authentic public record.")
    pub_line = ("Public records — real, fact-checked petrology: igneous, sedimentary, and "
                "metamorphic petrology; magma genesis and the twin engines of partial melting "
                "and fractional crystallization; Bowen's reaction series; IUGS, QAP, and TAS "
                "classification; igneous and volcanic textures; sedimentary provenance, "
                "structures, diagenesis, and carbonate petrology; metamorphic grade, facies, "
                "and textures; phase equilibria, the lever rule, and ternary diagrams; "
                "geothermobarometry; petrographic microscopy and optical properties; igneous "
                "geochemistry; ophiolites and mantle petrology; granite petrogenesis; P-T-t "
                "paths; experimental and field petrology, organized in the Signature system.")
    ladder = (" Records are ordered by the teaching ladder: Foundations (what petrology is, "
              "the rock cycle, igneous/sedimentary/metamorphic rocks, magma and lava, "
              "rock-forming minerals, intrusive vs. extrusive, igneous textures) -> "
              "Compounded (Bowen's reaction series, IUGS classification, the QAP diagram, "
              "TAS classification, magma genesis, partial melting and fractional "
              "crystallization, magma differentiation, volcanic textures, sedimentary "
              "provenance, sedimentary structures, diagenesis, carbonate petrology, "
              "metamorphic grade and index minerals, metamorphic facies, metamorphic "
              "textures) -> Advanced (binary phase diagrams, the lever rule, ternary phase "
              "diagrams, geothermobarometry, petrographic microscopy, optical properties in "
              "thin section, igneous geochemistry, ophiolites and mantle petrology, granite "
              "petrogenesis, P-T-t paths, experimental petrology, field petrology).")
    return {
        "name": name, "tagline": tagline, "record_kind": record_kind,
        "prefix": prefix, "ai": ai, "role": role,
        "hero_p": "%s — %s Every record carries the full entry: description, how it works, "
                  "key points, requirements, standards, citations, and a working demonstration "
                  "program.%s" % (tagline, sig_line if source == "signature" else pub_line, ladder),
        "sig_type": ("Signature originals organized in the Signature system"
                     if source == "signature" else
                     "Public records organized in the Signature system"),
        "search_ph": "Search Bowen, IUGS, QAP, TAS, facies, thin section, ophiolite, granite...",
        "chat_ph": "Ask about petrology...",
        "archive_blurb": ("Seeded %s petrology records, marching toward one million records. "
                          "Presented in teaching-ladder order: foundations, compounded, advanced."
                          % ("Signature-original" if source == "signature" else "public-record")),
        "schema": ("id, t, g, name, title, description, how_it_works, key_points, requirements, "
                   "standards, citations, src, ladder_rank, ladder_tier, demo"),
        "fields": "Foundations · Compounded · Advanced — each tier opens on demand and loads only what you open",
        "gen_desc": "Generate clearly-labeled structural petrology studies. Seeded archive records are the authoritative entries.",
        "greet": "I am the %s. Ask me about petrology — from the rock cycle up to P-T-t paths and experimental petrology." % ai,
        "gen_fields": ["Foundations", "Compounded", "Advanced"],
        "gen_kind": "petrology-study", "gen_demo_kind": "petrology-demo",
        "source": source,
    }

CIT_PUB = "Petrology (peer-reviewed literature and standard textbooks)."
CIT_SIG = CIT_PUB + " " + SIG_TAIL

DBCFG = {}
DBCFG["petrology"] = _cfg(
    "petrology", "The Petrology Database",
    "Real, fact-checked petrology: igneous, sedimentary, and metamorphic "
    "petrology — magma genesis, Bowen's reaction series, IUGS/QAP/TAS "
    "classification, textures and structures, provenance and diagenesis, "
    "carbonate petrology, metamorphic grade/facies/textures, phase "
    "equilibria, geothermobarometry, petrographic microscopy, igneous "
    "geochemistry, ophiolites, granite petrogenesis, P-T-t paths, and "
    "experimental and field petrology.",
    "petrology record", "JAH-PET-", "JAH Petrology Archivist",
    "petrology archivist — igneous/sedimentary/metamorphic petrology, magma genesis, "
    "Bowen's reaction series, IUGS/QAP/TAS classification, textures/structures, "
    "provenance/diagenesis/carbonates, metamorphic grade/facies/textures, phase "
    "equilibria/lever rule/ternary diagrams, geothermobarometry, petrographic microscopy, "
    "igneous geochemistry, ophiolites, granite petrogenesis, P-T-t paths, experimental "
    "and field petrology; teaching progressively along the ladder from foundations "
    "(what petrology is, rock cycle, three rock families, magma/lava, rock-forming "
    "minerals, intrusive vs extrusive, igneous textures) through compounded (Bowen, "
    "IUGS, QAP, TAS, magma genesis, partial melting/fractionation, differentiation, "
    "volcanic textures, provenance, sedimentary structures, diagenesis, carbonates, "
    "metamorphic grade, facies, textures) to advanced (binary/ternary phase diagrams, "
    "lever rule, geothermobarometry, microscopy, optical properties, geochemistry, "
    "ophiolites, granite problem, P-T-t paths, experimental and field petrology); "
    "answers from many angles — definition, example, analogy, application, history, "
    "math, how-to — using only the system's own archive data",
    CIT_PUB, "public")
DBCFG["petrology-signature"] = _cfg(
    "petrology-signature", "The Petrology Signature Database",
    "His original Signature interpretation of petrology: the full ladder from "
    "the rock cycle to P-T-t paths and experimental petrology, reframed as "
    "Signature science. Clearly labeled Signature-made, never presented as "
    "authentic public record.",
    "petrology record", "JAH-PSG-", "JAH Petrology Archivist (Signature)",
    "petrology archivist — Signature editions: his original Signature interpretation of "
    "petrology, clearly labeled Signature-made and never presented as authentic public "
    "record; teaches progressively along the ladder from foundations through compounded "
    "to advanced; answers from many angles — definition, example, analogy, application, "
    "history, math, how-to — using only the system's own archive data",
    CIT_SIG, "signature")

base.DBCFG = DBCFG

# ---------------------------------------------------------------- demos
# Every demo is real, runnable, stdlib-only Python performing the actual
# petrological calculation for its record. All are machine-executed by main().

_PREAMBLE = """import math
import re
"""

def _wrap(name, rid, group, body):
    return (base._hdr(name, rid, group) + _PREAMBLE + body.replace("NAME", json.dumps(name)))

def demo_petro_branches(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
BRANCHES = {
    "petrography": "description and classification of rocks",
    "petrogenesis": "origins of rocks",
    "experimental petrology": "lab recreation of rock-forming conditions",
    "igneous petrology": "rocks from magma",
    "sedimentary petrology": "rocks from sediment",
    "metamorphic petrology": "rocks transformed by heat and pressure",
}
def main():
    assert len(BRANCHES) == 6
    assert BRANCHES["petrogenesis"] == "origins of rocks"
    assert BRANCHES["igneous petrology"] == "rocks from magma"
    for branch, focus in BRANCHES.items():
        print("%-22s -> %s" % (branch, focus))
    print("rule: petrography describes, petrogenesis explains, experiment verifies")
    print("OK: %s mapped the branches" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_rock_cycle(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
TRANSITIONS = {
    ("magma", "cooling"): "igneous",
    ("igneous", "weathering+erosion"): "sediment",
    ("sediment", "lithification"): "sedimentary",
    ("sedimentary", "metamorphism"): "metamorphic",
    ("metamorphic", "melting"): "magma",
    ("igneous", "metamorphism"): "metamorphic",
    ("metamorphic", "weathering+erosion"): "sediment",
    ("sedimentary", "weathering+erosion"): "sediment",
}
def step(rock, process):
    return TRANSITIONS.get((rock, process))
def main():
    assert step("magma", "cooling") == "igneous"
    assert step("igneous", "weathering+erosion") == "sediment"
    assert step("sediment", "lithification") == "sedimentary"
    assert step("sedimentary", "metamorphism") == "metamorphic"
    assert step("metamorphic", "melting") == "magma"
    # shortcuts exist: igneous can metamorphose without becoming sediment
    assert step("igneous", "metamorphism") == "metamorphic"
    # impossible arrow: magma does not lithify
    assert step("magma", "lithification") is None
    # full loop returns to start
    rock = "magma"
    for proc in ("cooling", "weathering+erosion", "lithification",
                 "metamorphism", "melting"):
        rock = step(rock, proc)
    assert rock == "magma", rock
    print("loop magma->igneous->sediment->sedimentary->metamorphic->magma closes")
    print("OK: %s ran the rock cycle" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_igneous_classes(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def silica_class(sio2):
    if sio2 < 45: return "ultramafic"
    if sio2 < 52: return "mafic"
    if sio2 <= 63: return "intermediate"
    return "felsic"
def main():
    cases = [(40, "ultramafic"), (50, "mafic"), (60, "intermediate"), (72, "felsic")]
    for sio2, want in cases:
        got = silica_class(sio2)
        print("SiO2 %d%% -> %s" % (sio2, got))
        assert got == want, (sio2, got)
    print("rule: silica is the master chemical variable of igneous rocks")
    print("OK: %s classed by silica" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_sediment_classes(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def wentworth(grain_mm):
    if grain_mm > 2: return "conglomerate/breccia (gravel)"
    if grain_mm >= 0.0625: return "sandstone (sand)"
    if grain_mm >= 0.0039: return "siltstone (silt)"
    return "shale/claystone (clay)"
def main():
    cases = [(5.0, "conglomerate/breccia (gravel)"), (0.5, "sandstone (sand)"),
             (0.02, "siltstone (silt)"), (0.001, "shale/claystone (clay)")]
    for size, want in cases:
        got = wentworth(size)
        print("%.4g mm -> %s" % (size, got))
        assert got == want, (size, got)
    print("rule: grain size records transport energy (gravel=torrent, mud=still water)")
    print("OK: %s sized the sediment" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_metamorphic_agents(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def metamorphose(temp_c, directed_pressure):
    if temp_c < 200:
        return "no metamorphism (diagenesis zone)"
    if temp_c >= 700:
        return "high grade: partial melting begins (migmatite)"
    if directed_pressure:
        return "foliated metamorphic rock (slate/schist/gneiss)"
    return "non-foliated metamorphic rock (hornfels/marble/quartzite)"
def main():
    assert metamorphose(150, True) == "no metamorphism (diagenesis zone)"
    assert metamorphose(450, True) == "foliated metamorphic rock (slate/schist/gneiss)"
    assert metamorphose(450, False) == "non-foliated metamorphic rock (hornfels/marble/quartzite)"
    assert metamorphose(750, True) == "high grade: partial melting begins (migmatite)"
    print("agents: heat (T>~200C) + pressure + fluids; directed pressure -> foliation")
    print("OK: %s applied the agents" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_magma_viscosity(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def magma_profile(sio2):
    if sio2 < 52:
        return ("low viscosity", "1100-1250 C", "effusive flows and fountains")
    if sio2 <= 63:
        return ("intermediate viscosity", "900-1100 C", "mixed effusive/explosive")
    return ("high viscosity", "700-900 C", "explosive eruptions")
def main():
    assert magma_profile(50) == ("low viscosity", "1100-1250 C", "effusive flows and fountains")
    assert magma_profile(60)[0] == "intermediate viscosity"
    assert magma_profile(72) == ("high viscosity", "700-900 C", "explosive eruptions")
    for sio2 in (50, 60, 72):
        visc, temp, style = magma_profile(sio2)
        print("SiO2 %d%%: %s, %s -> %s" % (sio2, visc, temp, style))
    print("rule: silica polymerizes the melt; volatiles exsolve on ascent and drive explosions")
    print("OK: %s profiled the magmas" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_rock_formers(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
FORMERS = {
    "olivine": ["basalt", "gabbro", "peridotite"],
    "pyroxene": ["basalt", "gabbro", "pyroxenite"],
    "amphibole": ["andesite", "diorite", "amphibolite"],
    "biotite": ["granite", "granodiorite", "schist"],
    "K-feldspar": ["granite", "syenite", "rhyolite"],
    "plagioclase": ["basalt", "gabbro", "andesite", "granite"],
    "quartz": ["granite", "rhyolite", "sandstone", "quartzite"],
    "calcite": ["limestone", "marble"],
    "clay minerals": ["shale", "mudstone"],
    "iron oxides": ["banded iron formation", "laterite"],
}
def diagnose(assemblage):
    votes = {}
    for mineral in assemblage:
        for rock in FORMERS.get(mineral, []):
            votes[rock] = votes.get(rock, 0) + 1
    return sorted(votes, key=votes.get, reverse=True)
def main():
    assert len(FORMERS) == 10
    assert diagnose(["quartz", "K-feldspar", "biotite"])[0] == "granite"
    assert diagnose(["olivine", "pyroxene", "plagioclase"])[0] in ("basalt", "gabbro")
    print("assemblage quartz+K-feldspar+biotite -> %s" % diagnose(["quartz", "K-feldspar", "biotite"])[0])
    print("rule: feldspars alone build ~60% of Earth's crust")
    print("OK: %s assembled the rocks" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_cooling_grain(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def texture_for(cooling):
    return {
        "deep pluton (slow)": "phaneritic: all grains visible (granite)",
        "surface flow (fast)": "aphanitic: grains microscopic (basalt)",
        "quench (instant)": "glassy: no crystals (obsidian)",
        "two-stage": "porphyritic: phenocrysts in fine groundmass",
    }[cooling]
def main():
    assert texture_for("deep pluton (slow)").startswith("phaneritic")
    assert texture_for("surface flow (fast)").startswith("aphanitic")
    assert texture_for("quench (instant)").startswith("glassy")
    assert texture_for("two-stage").startswith("porphyritic")
    pairs = [("granite", "rhyolite"), ("diorite", "andesite"), ("gabbro", "basalt")]
    for intr, extr in pairs:
        print("%s (intrusive) <-> %s (extrusive): same chemistry, different cooling" % (intr, extr))
    print("rule: grain size is the direct readout of cooling rate")
    print("OK: %s timed the cooling" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_texture_classify(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def classify(visible_grains, phenocrysts, glassy, vesicles, fragments):
    if fragments: return "pyroclastic (explosive fragments: tuff/breccia)"
    if glassy: return "glassy (quenched melt: obsidian)"
    if vesicles: return "vesicular (frozen gas bubbles: pumice/scoria)"
    if phenocrysts: return "porphyritic (two-stage cooling)"
    if visible_grains: return "phaneritic (slow plutonic cooling: granite)"
    return "aphanitic (rapid volcanic cooling: basalt)"
def main():
    assert classify(True, False, False, False, False).startswith("phaneritic")
    assert classify(False, False, False, False, False).startswith("aphanitic")
    assert classify(False, True, False, False, False).startswith("porphyritic")
    assert classify(False, False, True, False, False).startswith("glassy")
    assert classify(False, False, False, True, False).startswith("vesicular")
    assert classify(False, False, False, False, True).startswith("pyroclastic")
    print("euhedral crystals grew early and freely; anhedral grains filled late spaces")
    print("OK: %s named the textures" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_bowen_order(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
DISCONTINUOUS = ["olivine", "pyroxene", "amphibole", "biotite"]
CONTINUOUS = ["Ca-plagioclase", "Na-plagioclase"]   # solid solution series
FINAL = ["K-feldspar", "muscovite", "quartz"]
ORDER = DISCONTINUOUS + ["plagioclase (Ca->Na)"] + FINAL
def crystallizes_before(a, b):
    seq = DISCONTINUOUS + CONTINUOUS + FINAL
    return seq.index(a) < seq.index(b)
def main():
    assert crystallizes_before("olivine", "pyroxene")
    assert crystallizes_before("pyroxene", "amphibole")
    assert crystallizes_before("amphibole", "biotite")
    assert crystallizes_before("Ca-plagioclase", "Na-plagioclase")
    assert crystallizes_before("biotite", "quartz")
    assert not crystallizes_before("quartz", "olivine")
    print("discontinuous: " + " -> ".join(DISCONTINUOUS))
    print("continuous: Ca-plagioclase -> Na-plagioclase; then " + " -> ".join(FINAL))
    print("rule: each step is a reaction of early crystals with melt (Bowen 1928)")
    print("OK: %s ordered the series" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_iugs_check(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def iugs_route(mode):
    # mode: dict of mineral volume percents
    total = sum(mode.values())
    if abs(total - 100) > 2:
        return "renormalize: mode sums to %.1f, not 100" % total
    mafic = sum(v for k, v in mode.items()
                if k in ("olivine", "pyroxene", "amphibole", "biotite", "opaques"))
    if mafic > 90:
        return "ultramafic triangle (olivine-pyroxene-hornblende)"
    if "glass" in mode and mode["glass"] > 50:
        return "glassy rock: chemical (TAS) classification"
    return "QAPF double triangle (plutonic) or TAS (volcanic)"
def main():
    granite = {"quartz": 30, "K-feldspar": 35, "plagioclase": 25,
               "biotite": 8, "opaques": 2}
    assert iugs_route(granite) == "QAPF double triangle (plutonic) or TAS (volcanic)"
    peridotite = {"olivine": 70, "pyroxene": 25, "opaques": 5}
    assert iugs_route(peridotite) == "ultramafic triangle (olivine-pyroxene-hornblende)"
    bad = {"quartz": 30, "K-feldspar": 35}
    assert iugs_route(bad).startswith("renormalize")
    print("granite mode -> %s" % iugs_route(granite))
    print("peridotite mode -> %s" % iugs_route(peridotite))
    print("rule: classify from measured mode, never from field appearance")
    print("OK: %s routed the IUGS check" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_qap_classify(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def qap_classify(Q, A, P, anorthite=None):
    tot = Q + A + P
    q, a, p = 100*Q/tot, 100*A/tot, 100*P/tot
    pap = 100*P/(A+P) if (A+P) else 0
    if q >= 20:
        if pap < 10: return "alkali-feldspar granite"
        if pap < 65: return "granite"
        if pap < 90: return "granodiorite"
        return "tonalite"
    if q >= 5:
        if pap < 35: return "quartz syenite"
        if pap < 65: return "quartz monzonite"
        return "quartz diorite"
    # Q < 5: plagioclase composition splits diorite from gabbro
    if anorthite is None:
        return "diorite/gabbro (need plagioclase An content)"
    return "gabbro" if anorthite > 50 else "diorite"
def main():
    assert qap_classify(30, 45, 25) == "granite"
    assert qap_classify(25, 10, 65) == "granodiorite"
    assert qap_classify(30, 2, 68) == "tonalite"
    assert qap_classify(28, 65, 7) == "alkali-feldspar granite"
    assert qap_classify(5, 60, 35) == "quartz monzonite"
    assert qap_classify(2, 8, 60, anorthite=30) == "diorite"
    assert qap_classify(2, 8, 60, anorthite=65) == "gabbro"
    print("Q=30 A=45 P=25 -> granite; Q=25 A=10 P=65 -> granodiorite")
    print("rule: normalize Q+A+P to 100, then read the Streckeisen field")
    print("OK: %s plotted the QAP" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_tas_classify(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def tas_classify(sio2, na2o, k2o):
    alk = na2o + k2o
    # simplified IUGS TAS: alkaline if above the dividing trend
    dividing = 5 + (sio2 - 45) * 0.15
    if alk >= dividing:
        if alk >= 12 and sio2 < 60: return "phonolite"
        if sio2 < 52: return "trachybasalt"
        if sio2 < 57: return "basaltic trachyandesite"
        if sio2 < 65: return "trachyandesite"
        return "trachyte"
    if sio2 < 45: return "picrobasalt"
    if sio2 < 52: return "basalt"
    if sio2 < 57: return "basaltic andesite"
    if sio2 < 63: return "andesite"
    if sio2 < 69: return "dacite"
    return "rhyolite"
def main():
    assert tas_classify(50, 2.0, 1.0) == "basalt"
    assert tas_classify(60, 3.5, 1.5) == "andesite"
    assert tas_classify(73, 4.0, 3.5) == "rhyolite"
    assert tas_classify(66, 4.0, 2.0) == "dacite"
    assert tas_classify(58, 6.0, 3.0) == "trachyandesite"
    assert tas_classify(55, 8.0, 4.0) == "phonolite"
    print("basalt=volcanic gabbro; andesite=volcanic diorite; rhyolite=volcanic granite")
    print("rule: analyses recalculated volatile-free before plotting")
    print("OK: %s plotted the TAS" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_melting_mechanisms(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
MECHANISMS = {
    "mid-ocean ridge": "decompression melting",
    "hotspot": "decompression melting",
    "continental rift": "decompression melting",
    "subduction zone": "flux melting (slab water)",
    "volcanic arc": "flux melting (slab water)",
    "collisional belt crust": "heat-transfer melting",
}
PRODUCTS = {
    "decompression melting": "basalts (mid-ocean ridges, ocean islands)",
    "flux melting (slab water)": "andesites and dacites (volcanic arcs)",
    "heat-transfer melting": "felsic melts / granites (continents)",
}
def main():
    assert MECHANISMS["mid-ocean ridge"] == "decompression melting"
    assert MECHANISMS["volcanic arc"] == "flux melting (slab water)"
    assert MECHANISMS["collisional belt crust"] == "heat-transfer melting"
    for setting, mech in MECHANISMS.items():
        print("%-24s -> %s -> %s" % (setting, mech, PRODUCTS[mech]))
    print("rule: solidus rises with pressure, falls with water; cross it any of 3 ways")
    print("OK: %s triggered the melting" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_batch_melting(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def batch_melt(C0, D, F):
    # C_l = C0 / (D + F*(1-D)): equilibrium (batch) melting
    return C0 / (D + F * (1 - D))
def main():
    C0 = 1.0
    F = 0.10  # 10% melting
    incompat = batch_melt(C0, D=0.01, F=F)
    compat = batch_melt(C0, D=4.0, F=F)
    print("10%% melting: incompatible (D=0.01) -> %.2fx enriched" % incompat)
    print("10%% melting: compatible   (D=4)    -> %.2fx depleted" % compat)
    assert incompat > 5, incompat       # small melts strongly enrich incompatibles
    assert compat < 1, compat           # compatibles stay in the residue
    # more melting dilutes the enrichment
    assert batch_melt(C0, 0.01, 0.30) < incompat
    print("rule: first melts take the fusible components; tiny F = huge enrichment")
    print("OK: %s melted the batch" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_rayleigh(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def rayleigh(C0, D, F):
    # C_l = C0 * F^(D-1): Rayleigh fractional crystallization
    return C0 * (F ** (D - 1))
def main():
    C0 = 1.0
    F = 0.5  # half the magma crystallized and removed
    incompat = rayleigh(C0, D=0.01, F=F)
    compat = rayleigh(C0, D=3.0, F=F)
    print("50%% crystallized: incompatible (D=0.01) -> %.2fx in residual melt" % incompat)
    print("50%% crystallized: compatible   (D=3)    -> %.2fx in residual melt" % compat)
    assert incompat > 1.5, incompat
    assert abs(compat - 0.25) < 0.01, compat
    # removing olivine+pyroxene drives residual liquid felsic (Bowen's engine)
    print("rule: early crystals removed -> residual melt evolves toward felsic")
    print("OK: %s fractionated the melt" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_vesicle_porosity(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def vesicularity(v_vesicles, v_total):
    return 100.0 * v_vesicles / v_total
def describe(pct):
    if pct > 50: return "pumice/scoria grade: so vesicular it may float"
    if pct > 15: return "highly vesicular: gas-rich eruption"
    if pct > 2: return "moderately vesicular"
    return "dense: degassed or effusive flow"
def main():
    assert abs(vesicularity(30, 100) - 30.0) < 1e-9
    assert describe(65).startswith("pumice")
    assert describe(30).startswith("highly")
    assert describe(1).startswith("dense")
    print("30 cm3 bubbles in 100 cm3 rock -> %.0f%% vesicles" % vesicularity(30, 100))
    print("stretched vesicles = melt still flowed when it froze")
    print("OK: %s measured the bubbles" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_qfl_provenance(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def qfl_provenance(Q, F, L):
    # simplified Dickinson & Suczek (1979) fields
    tot = Q + F + L
    q, f, l = 100*Q/tot, 100*F/tot, 100*L/tot
    if l >= 50: return "magmatic arc (volcanic lithics dominate)"
    if q >= 65: return "continental block / craton interior (quartz-rich, mature)"
    if f >= 25: return "recycled orogen to transitional arc"
    return "recycled orogen (mixed lithics)"
def main():
    assert qfl_provenance(80, 10, 10) == "continental block / craton interior (quartz-rich, mature)"
    assert qfl_provenance(30, 40, 30) == "recycled orogen to transitional arc"
    assert qfl_provenance(20, 25, 55) == "magmatic arc (volcanic lithics dominate)"
    print("Q=80 F=10 L=10 -> craton interior sand")
    print("Q=20 F=25 L=55 -> magmatic arc sand")
    print("rule: point-count 300-500 grains; lithic type names the source directly")
    print("OK: %s traced the provenance" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_bedform(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def ripple_diagnosis(symmetric, wavelength_cm, height_cm):
    ri = wavelength_cm / height_cm  # ripple index
    if symmetric and 5 <= ri <= 8:
        return ("wave-formed ripples", ri)
    return ("current-formed ripples", ri)
def main():
    kind, ri = ripple_diagnosis(True, 12.0, 2.0)
    assert kind == "wave-formed ripples" and abs(ri - 6.0) < 1e-9
    kind2, _ = ripple_diagnosis(False, 20.0, 1.5)
    assert kind2 == "current-formed ripples"
    print("symmetric, RI=6.0 -> wave-formed (oscillating water)")
    print("asymmetric -> current-formed; dip direction of cross-beds = paleocurrent")
    print("rule: diagnose environment from the assemblage, never one structure alone")
    print("OK: %s read the bedforms" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_compaction(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def porosity_depth(phi0, c, z_m):
    # exponential porosity loss with burial depth
    return phi0 * math.exp(-c * z_m)
def main():
    sand = porosity_depth(0.60, 0.0005, 2000.0)
    mud = porosity_depth(0.75, 0.0005, 2000.0)
    print("sand: 60%% at surface -> %.1f%% at 2 km" % (100*sand))
    print("mud:  75%% at surface -> %.1f%% at 2 km" % (100*mud))
    assert abs(sand - 0.2207) < 0.005, sand
    assert mud > sand  # muds start more porous
    assert porosity_depth(0.60, 0.0005, 0.0) == 0.60
    print("rule: quartz cement typically starts above ~80 C burial temperature")
    print("OK: %s compacted the sediment" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_dunham(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def dunham(grain_supported, mud_present, grain_pct, bound, crystalline):
    # Dunham (1962) depositional texture classification
    if crystalline: return "crystalline carbonate"
    if bound: return "boundstone (organically bound: reef)"
    if grain_supported:
        return "grainstone (no mud)" if not mud_present else "packstone (muddy)"
    return "wackestone (>10% grains)" if grain_pct > 10 else "mudstone (<10% grains)"
def main():
    assert dunham(False, True, 5, False, False) == "mudstone (<10% grains)"
    assert dunham(False, True, 30, False, False) == "wackestone (>10% grains)"
    assert dunham(True, True, 60, False, False) == "packstone (muddy)"
    assert dunham(True, False, 80, False, False) == "grainstone (no mud)"
    assert dunham(False, False, 0, True, False) == "boundstone (organically bound: reef)"
    print("mud-supported vs grain-supported = the master energy call")
    print("rule: classify depositional texture first, strip diagenesis second")
    print("OK: %s named the carbonate" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_barrovian_order(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
BARROVIAN = ["chlorite", "biotite", "garnet", "staurolite", "kyanite", "sillimanite"]
def grade_of(index_mineral):
    return BARROVIAN.index(index_mineral)  # higher = hotter
def main():
    assert grade_of("chlorite") < grade_of("biotite") < grade_of("garnet")
    assert grade_of("garnet") < grade_of("staurolite") < grade_of("kyanite")
    assert grade_of("kyanite") < grade_of("sillimanite")
    # map traverse: highest index mineral per outcrop draws the isograds
    traverse = ["biotite", "garnet", "staurolite", "kyanite"]
    assert [grade_of(m) for m in traverse] == sorted(grade_of(m) for m in traverse)
    print("Barrovian zones: " + " -> ".join(BARROVIAN))
    print("rule: read grade only in comparable protoliths (metapelites)")
    print("OK: %s zoned the belt" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_facies_lookup(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def facies(P_kbar, T_c):
    # simplified metamorphic facies P-T fields (Eskola)
    if P_kbar >= 12 and T_c < 800: return "eclogite facies (subducted slab)"
    if P_kbar >= 8 and T_c < 400: return "blueschist facies (cold subduction)"
    if T_c >= 700: return "granulite facies (hot deep crust)"
    if T_c >= 500: return "amphibolite facies (mountain root)"
    if T_c >= 300: return "greenschist facies (low grade)"
    return "zeolite / prehnite-pumpellyite facies (very low grade)"
def main():
    assert facies(6, 450) == "greenschist facies (low grade)"
    assert facies(8, 600) == "amphibolite facies (mountain root)"
    assert facies(15, 600) == "eclogite facies (subducted slab)"
    assert facies(10, 300) == "blueschist facies (cold subduction)"
    assert facies(7, 800) == "granulite facies (hot deep crust)"
    assert facies(3, 200).startswith("zeolite")
    print("glaucophane=blueschist; omphacite+garnet=eclogite; orthopyroxene=granulite")
    print("rule: a facies name is a pressure-temperature address")
    print("OK: %s located the facies" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_foliation_grade(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def foliation(grade):
    return {
        "none": "granoblastic: no foliation (marble/quartzite)",
        "low": "slaty cleavage (microscopic mica alignment)",
        "medium": "schistosity (visible aligned micas)",
        "high": "gneissic banding (segregated light/dark bands)",
        "extreme": "migmatitic (banding + partial melt)",
    }[grade]
def porphyroblast_timing(trails):
    # inclusion-trail geometry timestamps deformation
    return {
        "wrapped": "pre-tectonic (foliation wraps the crystal)",
        "spiraled": "syn-tectonic (snowball garnet: grew during shearing)",
        "straight-through": "post-tectonic (overgrows foliation undeformed)",
    }[trails]
def main():
    assert foliation("low").startswith("slaty")
    assert foliation("medium").startswith("schistosity")
    assert foliation("high").startswith("gneissic")
    assert porphyroblast_timing("spiraled").startswith("syn-tectonic")
    assert porphyroblast_timing("straight-through").startswith("post-tectonic")
    print("foliation ladder: slaty cleavage -> schistosity -> gneissic banding")
    print("OK: %s timed the deformation" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_gibbs_phase_rule(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def phase_rule(C, P, fixed_pressure=False):
    F = C - P + 2
    return F - 1 if fixed_pressure else F
def main():
    # binary eutectic: 2 components, 3 phases (2 solids + liquid)
    assert phase_rule(2, 3) == 1
    assert phase_rule(2, 3, fixed_pressure=True) == 0  # invariant at fixed P
    # single melt: 2 components, 1 phase
    assert phase_rule(2, 1) == 3
    # plagioclase loop: 2 components, 2 phases (solid+liquid)
    assert phase_rule(2, 2, fixed_pressure=True) == 1  # T varies with composition
    print("F = C - P + 2 (minus 1 more at fixed pressure)")
    print("eutectic at fixed P: F=0 -> the temperature is invariant")
    print("OK: %s counted the freedoms" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_lever_rule(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def lever(bulk, c_solid, c_liquid):
    # mass fractions from the tie-line (opposite arm / total)
    f_liq = (bulk - c_solid) / (c_liquid - c_solid)
    f_sol = (c_liquid - bulk) / (c_liquid - c_solid)
    # mass-balance verification
    assert abs(f_sol * c_solid + f_liq * c_liquid - bulk) < 1e-9
    return f_sol, f_liq
def main():
    fs, fl = lever(bulk=40.0, c_solid=80.0, c_liquid=20.0)
    print("bulk 40%% An: solid %.1f%%%%, liquid %.1f%%%%" % (100*fs, 100*fl))
    assert abs(fs - 1/3) < 1e-9 and abs(fl - 2/3) < 1e-9
    # near the liquidus almost everything is liquid
    fs2, fl2 = lever(bulk=22.0, c_solid=80.0, c_liquid=20.0)
    assert fl2 > 0.95
    print("rule: opposite lever arm over total; always verify by mass balance")
    print("OK: %s weighed the phases" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_ternary_normalize(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def normalize(a, b, c):
    tot = a + b + c
    return (100*a/tot, 100*b/tot, 100*c/tot)
def main():
    q, a, p = normalize(30, 45, 25)
    assert abs(q + a + p - 100) < 1e-9
    fo, di, qz = normalize(20, 30, 10)
    assert abs(fo - 33.333) < 0.01 and abs(di - 50.0) < 0.01
    print("Fo-Di-SiO2 (20,30,10) -> (%.1f, %.1f, %.1f)" % (fo, di, qz))
    print("rule: liquid moves directly away from the crystallizing phase")
    print("at cotectics two phases co-crystallize; liquid follows the curve downhill")
    print("OK: %s plotted the ternary" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_garnet_biotite(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def garnet_biotite_temp(Kd, P_kbar):
    # Simplified illustrative calibration after Ferry & Spear (1978):
    # T(K) = (2089 + 9.56*P) / (ln(Kd) + 0.782), Kd=(Fe/Mg)gt/(Fe/Mg)bt
    T_K = (2089 + 9.56 * P_kbar) / (math.log(Kd) + 0.782)
    return T_K - 273.15
def main():
    T = garnet_biotite_temp(Kd=5.5, P_kbar=5.0)
    print("Kd=5.5 at 5 kbar -> %.0f C" % T)
    assert 500 < T < 700, T  # amphibolite-facies range, as expected
    # hotter rocks partition Fe/Mg more evenly -> lower Kd
    T_hot = garnet_biotite_temp(Kd=3.5, P_kbar=5.0)
    assert T_hot > T
    print("rule: analyze touching rims; cross-check with an independent barometer")
    print("OK: %s read the thermometer" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_thin_section(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
STANDARD_THICKNESS_UM = 30
PPL_READS = ["relief", "color", "pleochroism", "cleavage", "habit"]
XPL_READS = ["interference colors", "extinction angle", "twinning", "optic sign"]
def routine():
    return [("PPL scan", PPL_READS), ("XPL optics", XPL_READS),
            ("synthesis", ["mineralogy", "texture", "rock name"])]
def main():
    assert STANDARD_THICKNESS_UM == 30
    assert "pleochroism" in PPL_READS
    assert "extinction angle" in XPL_READS
    for step, reads in routine():
        print("%-12s: %s" % (step, ", ".join(reads)))
    print("rule: fixed order, PPL first then XPL, so no mineral is missed")
    print("OK: %s ran the microscope routine" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_retardation(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def retardation_nm(thickness_um, birefringence):
    return thickness_um * birefringence * 1000.0
def color_order(delta_nm):
    return int(delta_nm // 550) + 1  # Michel-Levy orders, ~550 nm each
MINERALS = {"quartz": 0.009, "plagioclase": 0.010, "olivine": 0.035,
            "pyroxene": 0.025, "calcite": 0.172}
def main():
    for mineral, d in MINERALS.items():
        delta = retardation_nm(30.0, d)
        print("%-12s delta=%.0f nm -> order %d" % (mineral, delta, color_order(delta)))
    assert abs(retardation_nm(30.0, 0.009) - 270) < 1
    assert color_order(270) == 1      # quartz: first-order gray-white
    assert color_order(1050) == 2     # olivine: vivid second order
    assert color_order(5160) >= 9     # calcite: extreme, pearly high orders
    print("rule: at 30 um, interference color directly encodes birefringence")
    print("OK: %s measured the retardation" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_ree_normalize(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
# Chondrite reference values (McDonough & Sun 1995, ppm, abbreviated set)
CHONDRITE = {"La": 0.648, "Ce": 1.675, "Nd": 1.25, "Sm": 0.406, "Eu": 0.154,
             "Gd": 0.51, "Dy": 0.674, "Er": 0.438, "Yb": 0.441, "Lu": 0.0675}
def normalize(sample):
    return {el: sample[el] / CHONDRITE[el] for el in sample}
def la_yb_ratio(norm):
    return norm["La"] / norm["Yb"]
def eu_anomaly(norm):
    return norm["Eu"] / math.sqrt(norm["Sm"] * norm["Gd"])
def main():
    sample = {"La": 30.0, "Ce": 60.0, "Nd": 28.0, "Sm": 6.0, "Eu": 1.2,
              "Gd": 5.5, "Dy": 4.5, "Er": 2.2, "Yb": 2.0, "Lu": 0.30}
    n = normalize(sample)
    ratio = la_yb_ratio(n)
    eu = eu_anomaly(n)
    print("La/Yb (chondrite-normalized) = %.1f -> steep LREE-enriched pattern" % ratio)
    print("Eu/Eu* = %.2f -> negative Eu anomaly (plagioclase fractionated)" % eu)
    assert ratio > 5, ratio
    assert eu < 0.9, eu
    print("rule: isotopes don't fractionate -- any isotopic shift is source or contamination")
    print("OK: %s fingerprinted the magma" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_ophiolite_order(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
# Penrose (1972) ophiolite stratigraphy, bottom -> top
PENROSE = ["ultramafic tectonite (mantle)", "gabbro (magma chamber)",
           "sheeted dike complex", "pillow basalt", "deep-sea sediment"]
def position(unit):
    return PENROSE.index(unit)
def main():
    assert position("ultramafic tectonite (mantle)") < position("gabbro (magma chamber)")
    assert position("sheeted dike complex") < position("pillow basalt")
    assert position("pillow basalt") < position("deep-sea sediment")
    for i, unit in enumerate(PENROSE):
        print("%d. %s" % (i + 1, unit))
    print("rule: one-way chilled sheeted dikes prove seafloor spreading")
    print("OK: %s stacked the ophiolite" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_granite_types(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def asi_excess(al2o3, cao, nao2, k2o):
    # simplified alumina saturation: molar Al2O3 vs CaO+Na2O+K2O (relative units)
    return al2o3 - (cao + nao2 + k2o)
def classify_granite(minerals, asi_excess_val):
    score = {"I-type": 0, "S-type": 0, "A-type": 0, "M-type": 0}
    for m in minerals:
        if m in ("hornblende", "magnetite", "titanite"): score["I-type"] += 2
        if m in ("muscovite", "garnet", "cordierite", "ilmenite"): score["S-type"] += 2
        if m in ("arfvedsonite", "aegirine", "fluorite", "annite"): score["A-type"] += 2
        if m in ("plagiogranite",): score["M-type"] += 3
    if asi_excess_val > 0: score["S-type"] += 2
    else: score["I-type"] += 1
    return max(score, key=score.get)
def main():
    assert classify_granite(["hornblende", "magnetite"], asi_excess_val=-0.5) == "I-type"
    assert classify_granite(["muscovite", "garnet", "ilmenite"], asi_excess_val=0.8) == "S-type"
    assert classify_granite(["arfvedsonite", "fluorite"], asi_excess_val=-0.2) == "A-type"
    print("I=igneous source; S=sedimentary source; A=anorogenic; M=mantle")
    print("rule: peraluminous chemistry demands an aluminous (sedimentary) source")
    print("OK: %s typed the granite" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_ptt_interpret(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def interpret_path(shape):
    return {
        "clockwise": "collisional mountain belt (burial, heating, isothermal decompression)",
        "counterclockwise": "magmatic arc / contact setting (heating before deep burial)",
        "hairpin": "extensional collapse of overthickened crust",
    }[shape]
def main():
    assert interpret_path("clockwise").startswith("collisional")
    assert interpret_path("counterclockwise").startswith("magmatic arc")
    assert interpret_path("hairpin").startswith("extensional")
    for shape in ("clockwise", "counterclockwise", "hairpin"):
        print("%-18s -> %s" % (shape, interpret_path(shape)))
    print("rule: zoned garnet is the flight recorder; monazite/zircon pin the time")
    print("OK: %s flew the P-T-t path" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_pressure_calc(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def pressure_GPa(force_N, diameter_m):
    area = math.pi * (diameter_m / 2) ** 2
    return (force_N / area) / 1e9
def depth_km(P_Pa, rho=3300.0, g=9.81):
    return P_Pa / (rho * g) / 1000.0
def main():
    # 1/2-inch piston-cylinder: 100 kN on a 12.7 mm piston
    P = pressure_GPa(100000.0, 0.0127)
    print("100 kN on 12.7 mm piston -> %.2f GPa" % P)
    assert 0.7 < P < 0.9, P
    h = depth_km(P * 1e9)
    print("= pressure at ~%.0f km depth" % h)
    assert 20 < h < 30, h
    print("rule: pressure = force / area -- smaller anvils, higher pressure")
    print("OK: %s pressed the sample" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_strike_dip(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def dip_direction(strike_deg):
    # right-hand rule: dip direction is 90 deg clockwise from strike
    return (strike_deg + 90) % 360
def describe(strike, dip):
    dd = dip_direction(strike)
    compass = ["N", "NE", "E", "SE", "S", "SW", "W", "NW"]
    return "%03d/%02d dipping toward %s (%03d)" % (strike, dip, compass[int((dd+22.5)//45) % 8], dd)
def main():
    assert dip_direction(45) == 135
    assert dip_direction(300) == 30
    assert dip_direction(0) == 90
    print(describe(45, 30))
    print(describe(300, 60))
    print("rule: the cutter is younger -- cross-cutting gives relative age")
    print("OK: %s measured the outcrop" % NAME)
if __name__ == "__main__":
    main()
''')

DEMOS = {
    "petro_branches": demo_petro_branches, "rock_cycle": demo_rock_cycle,
    "igneous_classes": demo_igneous_classes, "sediment_classes": demo_sediment_classes,
    "metamorphic_agents": demo_metamorphic_agents,
    "magma_viscosity": demo_magma_viscosity, "rock_formers": demo_rock_formers,
    "cooling_grain": demo_cooling_grain, "texture_classify": demo_texture_classify,
    "bowen_order": demo_bowen_order, "iugs_check": demo_iugs_check,
    "qap_classify": demo_qap_classify, "tas_classify": demo_tas_classify,
    "melting_mechanisms": demo_melting_mechanisms,
    "batch_melting": demo_batch_melting, "rayleigh": demo_rayleigh,
    "vesicle_porosity": demo_vesicle_porosity,
    "qfl_provenance": demo_qfl_provenance, "bedform": demo_bedform,
    "compaction": demo_compaction, "dunham": demo_dunham,
    "barrovian_order": demo_barrovian_order, "facies_lookup": demo_facies_lookup,
    "foliation_grade": demo_foliation_grade,
    "gibbs_phase_rule": demo_gibbs_phase_rule, "lever_rule": demo_lever_rule,
    "ternary_normalize": demo_ternary_normalize,
    "garnet_biotite": demo_garnet_biotite, "thin_section": demo_thin_section,
    "retardation": demo_retardation, "ree_normalize": demo_ree_normalize,
    "ophiolite_order": demo_ophiolite_order, "granite_types": demo_granite_types,
    "ptt_interpret": demo_ptt_interpret, "pressure_calc": demo_pressure_calc,
    "strike_dip": demo_strike_dip,
}

# ---------------------------------------------------------------- records

def build_records(slug, source):
    cfg = DBCFG[slug]
    sig = source == "signature"
    # Teaching-ladder order: stable sort by ladder_rank (entries are already
    # in ladder order in entries_petrology.py).
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
    for slug in ("petrology", "petrology-signature"):
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
