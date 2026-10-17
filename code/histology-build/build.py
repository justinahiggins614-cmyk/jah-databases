#!/usr/bin/env python3
"""Build the Histology field databases for JAH Databases (field #35, taxonomy order).

Verified 2026-10-17 (see entries_histology.py docstring): NO database
covers histology as a discipline (microscopic study of tissues: the four
basic tissue types, cell biology foundations, microscopy and staining,
tissue processing, organ/system histology, histopathology basics,
artifacts).

Manifest search (2,370 databases): zero 'histol*' slugs/names.
Whole-system exact-title sweep over all 769 shard indexes: zero
collisions for all 34 planned titles. Near-neighbors confirmed different
disciplines: 'anatomy' (gross anatomy), 'cell-biology' (cell biology as a
field), 'cytology' (single-cell diagnostics), 'pathology' (disease
mechanisms). ZERO full-record discipline coverage anywhere.

So this build creates two NEW databases, 34 ladder-ordered records each:

  histology                 - The Histology Database
                               (public-harvest: real, fact-checked
                               histology; standard references Ross &
                               Pawlina 'Histology: A Text and Atlas'
                               8th ed 2019; Mescher 'Junqueira's Basic
                               Histology' 16th ed 2021; Gartner & Hiatt
                               'Color Textbook of Histology';
                               Eroschenko 'diFiore's Atlas of Histology';
                               Young/O'Dowd/Woodford 'Wheater's Functional
                               Histology'; Kierszenbaum & Tres 'Histology
                               and Cell Biology'; Bancroft & Gamble
                               'Theory and Practice of Histological
                               Techniques'; Kiernan 'Histological and
                               Histochemical Methods')
  histology-signature       - The Histology Signature Database
                               (his original Signature interpretation of
                               histology as the microscopic reading of
                               the body; src signature, titles suffixed
                               " (Signature Edition)", never presented as
                               authentic public record)

34 records each, ordered by the teaching ladder (ladder_rank 1-10,
ladder_tier foundations/compounded/advanced); the shard index is written in
ladder order so pages present simple -> compounded -> complex.

Subtitle disambiguation (fields #13-34 pattern): specialty titles carry
teaching-focused subtitles rather than bare cards.

Numerical cores: all hand-computed 2026-10-17, machine-verified by the
demos (see below). Every demo prints its real computed values, asserts
tight bounds, and ends with the OK marker; the build machine-executes all
68 demos before commit.

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
sys.path.insert(0, os.path.join(REPO, "code"))
from dedupe_gate import DedupeGate
base.GATE = DedupeGate(os.path.join(REPO, "data", "dedupe", "exact"))

sys.path.insert(0, HERE)
from entries_histology import ENTRIES, SIG_TAIL

# ---------------------------------------------------------------- DB config

def _cfg(slug, name, tagline, record_kind, prefix, ai, role, citation, source):
    sig_line = ("Signature originals - his original Signature interpretation of histology "
                "as the microscopic reading of the body: clearly labeled Signature-made, "
                "never presented as authentic public record.")
    pub_line = ("Public records - real, fact-checked histology: what histology is; cells "
                "and ultrastructure; the four basic tissue types; epithelial tissue and "
                "glands; connective tissue; muscle tissue; nervous tissue; membranes; "
                "fixation; embedding and sectioning; H and E staining; special stains; "
                "immunohistochemistry; microscopy; cell junctions and the basement membrane; "
                "blood; hemopoiesis; skin; the digestive tract; liver and pancreas; the "
                "respiratory tract; the urinary system; the cardiovascular system; lymphoid "
                "tissue; endocrine glands; bone; the male reproductive system; the female "
                "reproductive system; the central nervous system; the eye; histopathology; "
                "artifacts; histomorphometry; digital histology, organized in the Signature system.")
    ladder = (" Records are ordered by the teaching ladder: Foundations (what histology is, "
              "cells, the four basic tissue types, epithelium, connective tissue, muscle, "
              "nervous tissue, membranes, fixation, sectioning, H and E, special stains) -> "
              "Compounded (immunohistochemistry, microscopy, junctions, blood, hemopoiesis, "
              "skin, digestive tract, liver and pancreas, respiratory tract, urinary system, "
              "cardiovascular system, lymphoid tissue) -> Advanced (endocrine glands, bone, "
              "male and female reproductive systems, central nervous system, eye, "
              "histopathology, artifacts, histomorphometry, digital histology).")
    return {
        "name": name, "tagline": tagline, "record_kind": record_kind,
        "prefix": prefix, "ai": ai, "role": role,
        "hero_p": "%s - %s Every record carries the full entry: description, how it works, "
                  "key points, requirements, standards, citations, and a working demonstration "
                  "program.%s" % (tagline, sig_line if source == "signature" else pub_line, ladder),
        "sig_type": ("Signature originals organized in the Signature system"
                     if source == "signature" else
                     "Public records organized in the Signature system"),
        "search_ph": "Search epithelium, H&E, immunohistochemistry, nephrons, alveoli, osteons, retinal layers...",
        "chat_ph": "Ask about histology...",
        "archive_blurb": ("Seeded %s histology records, marching toward one million records. "
                          "Presented in teaching-ladder order: foundations, compounded, advanced."
                          % ("Signature-original" if source == "signature" else "public-record")),
        "schema": ("id, t, g, name, title, description, how_it_works, key_points, requirements, "
                   "standards, citations, src, ladder_rank, ladder_tier, demo"),
        "fields": "Foundations \u00b7 Compounded \u00b7 Advanced - each tier opens on demand and loads only what you open",
        "gen_desc": "Generate clearly-labeled histology studies. Seeded archive records are the authoritative entries.",
        "greet": "I am the %s. Ask me about histology - from what it is through cells, the four basic tissue types, epithelium, connective tissue, muscle, nervous tissue, membranes, fixation, sectioning, H and E staining, and special stains, through immunohistochemistry, microscopy, cell junctions, blood, hemopoiesis, skin, the digestive tract, liver and pancreas, the respiratory tract, the urinary system, the cardiovascular system, and lymphoid tissue, to endocrine glands, bone, the male and female reproductive systems, the central nervous system, the eye, histopathology, artifacts, histomorphometry, and digital histology." % ai,
        "gen_fields": ["Foundations", "Compounded", "Advanced"],
        "gen_kind": "histology-study", "gen_demo_kind": "histology-demo",
        "source": source,
    }

CIT_PUB = ("Histology (standard references: Ross and Pawlina Histology: A Text and Atlas "
           "8th ed 2019; Mescher Junqueira Basic Histology 16th ed 2021; Gartner and Hiatt "
           "Color Textbook of Histology; Eroschenko diFiore Atlas of Histology; "
           "Young Woodford Wheater Functional Histology; Kierszenbaum and Tres "
           "Histology and Cell Biology; Bancroft and Gamble Theory and Practice of "
           "Histological Techniques; Kiernan Histological and Histochemical Methods).")
CIT_SIG = CIT_PUB + (" Signature editions are his original Signature interpretation of "
                     "histology, clearly labeled Signature-made.")

DBCFG = {}
DBCFG["histology"] = _cfg(
    "histology", "The Histology Database",
    "Real, fact-checked histology: from what histology is through cells, the four basic "
    "tissue types, epithelium, connective tissue, muscle, nervous tissue, membranes, "
    "fixation, sectioning, H&E, and special stains, through immunohistochemistry, "
    "microscopy, junctions, blood, hemopoiesis, skin, the digestive tract, liver and "
    "pancreas, the respiratory tract, the urinary system, the cardiovascular system, and "
    "lymphoid tissue, to endocrine glands, bone, the male and female reproductive systems, "
    "the central nervous system, the eye, histopathology, artifacts, histomorphometry, and "
    "digital histology - taught progressively along the ladder.",
    "histology record", "JAH-HIS-", "JAH Histology Archivist",
    "histology archivist - microscopic study of tissues: the four basic tissue types, "
    "cell biology foundations, fixation, embedding, sectioning, H&E and special stains, "
    "immunohistochemistry, microscopy, and organ and system histology from skin, gut, "
    "liver, lung, kidney, vessels, and lymphoid tissue through endocrine glands, bone, "
    "reproductive systems, the central nervous system, and the eye, to histopathology, "
    "artifacts, histomorphometry, and digital imaging; teaching progressively along the "
    "ladder from foundations through compounded to advanced; answers from many angles - "
    "definition, example, analogy, application, history, math, how-to - using only "
    "archive data from this system",
    CIT_PUB, "public")
DBCFG["histology-signature"] = _cfg(
    "histology-signature", "The Histology Signature Database",
    "His original Signature interpretation of histology as the microscopic reading of "
    "the body: the full ladder from tissues and staining through organ histology to "
    "measurement and digital imaging, reframed as Signature science. Clearly labeled "
    "Signature-made, never presented as authentic public record.",
    "histology record", "JAH-HTS-", "JAH Histology Archivist (Signature)",
    "histology archivist - Signature editions: his original Signature interpretation "
    "of histology as the microscopic reading of the body, clearly labeled "
    "Signature-made and never presented as authentic public record; teaches "
    "progressively along the ladder from foundations through compounded to advanced; "
    "answers from many angles - definition, example, analogy, application, history, "
    "math, how-to - using only archive data from this system",
    CIT_SIG, "signature")

base.DBCFG = DBCFG
# ---------------------------------------------------------------- demos
# Every demo is real, runnable, stdlib-only Python performing the actual
# histology computation for its record. All are machine-executed by main().

_PREAMBLE = (
"import math\n"
)

def _wrap(name, rid, group, body):
    return (base._hdr(name, rid, group) + _PREAMBLE + body.replace("NAME", json.dumps(name)))

def demo_hs_what_is(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # Rayleigh resolution of the light microscope: d = 0.61*lam/NA
    lam, NA = 550e-9, 1.4
    d = 0.61*lam/NA
    d_um = d*1e6
    useful = 1000.0*NA          # useful magnification ceiling
    apparent_mm = 10.0*useful/1000.0  # a 10-um cell at the ceiling
    print("light resolution (550 nm, NA 1.4): %.4f um" % d_um)
    print("useful magnification ceiling: %.0fx" % useful)
    print("a 10-um cell at the ceiling appears %.1f mm across" % apparent_mm)
    assert 0.239 < d_um < 0.240
    assert useful == 1400.0
    assert apparent_mm == 14.0
    print("rule: resolution is diffraction, not magnification - price the NA first")
    print("OK: %s resolved the limit" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_hs_cells(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # surface-to-volume ratio of spherical cells: S/V = 6/d
    sv10 = 6.0/10e-6/1e6   # per um
    sv20 = 6.0/20e-6/1e6
    per_cm3 = (1e-2/10e-6)**3  # cells at 10 um per side in 1 cm^3
    print("S/V at 10 um: %.2f um^-1" % sv10)
    print("S/V at 20 um: %.2f um^-1" % sv20)
    print("exchange surface per volume ratio (10 vs 20 um): %.1f" % (sv10/sv20))
    print("cells per cubic centimeter at 10 um: %.3g" % per_cm3)
    assert 0.599 < sv10 < 0.601
    assert 0.299 < sv20 < 0.301
    assert sv10/sv20 == 2.0
    assert 9.99e8 < per_cm3 < 1.001e9
    print("rule: small cells exchange faster - size is a design parameter")
    print("OK: %s priced the exchange" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_hs_four_tissues(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # epithelial classifier: (layers, shape) -> classical type
    table = {
        ("simple", "squamous"): "simple squamous epithelium",
        ("simple", "cuboidal"): "simple cuboidal epithelium",
        ("simple", "columnar"): "simple columnar epithelium",
        ("stratified", "squamous"): "stratified squamous epithelium",
        ("stratified", "cuboidal"): "stratified cuboidal epithelium",
        ("stratified", "columnar"): "stratified columnar epithelium",
        ("pseudostratified", "columnar"): "pseudostratified ciliated columnar epithelium",
        ("transitional", ""): "transitional epithelium (urothelium)",
    }
    print("classical epithelial types classified: %d" % len(table))
    for k in sorted(table):
        print("  %-28s -> %s" % (str(k), table[k]))
    bad = table.get(("simple", "transitional"))
    print("impossible combo (simple, transitional): %s" % bad)
    assert len(table) == 8
    assert bad is None
    assert table[("stratified", "squamous")] == "stratified squamous epithelium"
    print("rule: layers first, then shape - the code never changes")
    print("OK: %s ran the decision tree" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_hs_epithelium(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # exocrine gland classification matrix: 7 classical combinations
    glands = [
        ("simple tubular", "intestinal crypts"),
        ("simple branched tubular", "gastric glands"),
        ("simple acinar", "sebaceous (holocrine)"),
        ("simple branched acinar", "prostate"),
        ("compound tubular", "Brunner glands"),
        ("compound acinar", "pancreas exocrine"),
        ("compound tubuloacinar", "salivary glands"),
    ]
    print("classical exocrine gland combinations: %d" % len(glands))
    for g, ex in glands:
        print("  %-26s e.g. %s" % (g, ex))
    modes = {"merocrine": "salivary (exocytosis)",
             "apocrine": "mammary (apical budding)",
             "holocrine": "sebaceous (whole cell)"}
    print("secretion modes: %d" % len(modes))
    assert len(glands) == 7
    assert len(modes) == 3
    assert glands[0][0] == "simple tubular"
    assert glands[6][0] == "compound tubuloacinar"
    print("rule: ducts x secretory units - every gland files somewhere")
    print("OK: %s classified the glands" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_hs_connective(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # collagen fibril packing in tendon: 70% area fraction, 100-nm fibrils
    d = 100e-9
    fibril_area = math.pi*(d/2.0)**2
    per_mm2 = 0.70*1e-6/fibril_area
    print("fibril cross-section: %.3e m^2" % fibril_area)
    print("fibrils per mm^2 of tendon at 70%% packing: %.3e" % per_mm2)
    assert 7.85e-15 < fibril_area < 7.86e-15
    assert 8.91e7 < per_mm2 < 8.92e7
    print("rule: tendon is a cable - count the fibrils and the strength follows")
    print("OK: %s packed the tendon" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_hs_muscle(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # sarcomere series summation: 2.2 um rest -> 1.6 um contracted
    shorten = (2.2 - 1.6)/2.2*100.0
    n_series = int(0.10/2.2e-6)
    excursion_cm = n_series*0.6e-6*100.0
    print("shortening per sarcomere: %.2f %%" % shorten)
    print("sarcomeres in series along 10 cm: %d" % n_series)
    print("total excursion: %.2f cm" % excursion_cm)
    assert 27.27 < shorten < 27.28
    assert n_series == 45454
    assert 2.72 < excursion_cm < 2.73
    print("rule: small motors in series make large movements")
    print("OK: %s summed the sarcomeres" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_hs_nervous(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # conduction velocity: myelinated v=6*d (m/s per um); unmyelinated v=1.7*sqrt(d)
    v_myel = 6.0*10.0
    t_myel_ms = 1.0/v_myel*1000.0
    v_un = 1.7*math.sqrt(1.0)
    t_un_ms = 1.0/v_un*1000.0
    print("myelinated 10 um: %.0f m/s -> 1 m in %.2f ms" % (v_myel, t_myel_ms))
    print("unmyelinated 1 um: %.1f m/s -> 1 m in %.0f ms" % (v_un, t_un_ms))
    print("myelin speed advantage: %.1fx" % (t_un_ms/t_myel_ms))
    assert v_myel == 60.0
    assert 16.66 < t_myel_ms < 16.67
    assert 588.2 < t_un_ms < 588.3
    print("rule: myelin is bandwidth - the signal jumps, it does not crawl")
    print("OK: %s timed the impulse" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_hs_membranes(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # membrane areas in m^2, each as a multiple of skin area
    skin, alveolar, intestinal, peritoneum = 1.8, 70.0, 30.0, 1.7
    for label, a in (("alveolar", alveolar), ("intestinal", intestinal),
                     ("peritoneum", peritoneum)):
        print("%-11s %5.1f m^2 = %.2f x skin" % (label, a, a/skin))
    assert 38.88 < alveolar/skin < 38.90
    assert 16.66 < intestinal/skin < 16.68
    assert 0.944 < peritoneum/skin < 0.945
    print("rule: exchange membranes dwarf armor - area is budgeted to work")
    print("OK: %s measured the membranes" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_hs_fixation(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # 10:1 fixative rule for 1 cm^3 tissue; penetration 1 mm/hr
    fix_ml = 1.0*10.0  # 1 cm^3 tissue -> mL fixative
    t_center_hr = 5.0/1.0  # 10-mm block, fixed from both faces
    depth_24h = 1.0*24.0
    print("fixative for 1 cm^3 tissue: %.0f mL" % fix_ml)
    print("time to fix the center of a 10-mm block: %.0f hr" % t_center_hr)
    print("penetration in 24 hr: %.0f mm" % depth_24h)
    assert fix_ml == 10.0
    assert t_center_hr == 5.0
    assert depth_24h == 24.0
    print("rule: thin pieces, big volumes, honest hours - fixation is diffusion")
    print("OK: %s timed the fixative" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_hs_sectioning(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # serial sections: 4-mm block at 5 um; ribbon length at 20 mm/section
    n = int(4000.0/5.0)
    ribbon_m = n*20.0/1000.0
    n_frozen = int(4000.0/10.0)
    print("sections from a 4-mm block at 5 um: %d" % n)
    print("ribbon length at 20 mm per section: %.0f m" % ribbon_m)
    print("same block at 10 um frozen: %d sections" % n_frozen)
    assert n == 800
    assert ribbon_m == 16.0
    assert n_frozen == 400
    print("rule: one block can hold a whole organ in series - plan the orientation")
    print("OK: %s cut the ribbon" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_hs_he_stain(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # Beer-Lambert: T = 10^-OD; nucleus OD 0.8, cytoplasm OD 0.5
    t_nuc = 10.0**(-0.8)
    t_cyt = 10.0**(-0.5)
    contrast = t_cyt/t_nuc
    print("nuclear transmittance: %.1f %%" % (t_nuc*100.0))
    print("cytoplasm transmittance: %.1f %%" % (t_cyt*100.0))
    print("pink-blue contrast ratio: %.2f:1" % contrast)
    assert 0.158 < t_nuc < 0.159
    assert 0.316 < t_cyt < 0.317
    assert 1.99 < contrast < 2.01
    print("rule: contrast is quantitative - the eye reads the ratio")
    print("OK: %s read pink and blue" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_hs_special_stains(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # pH arithmetic of special-stain baths: Henderson-Hasselbalch
    h_trichrome = 10.0**(-2.5)          # [H+] at pH 2.5
    ph_11 = 4.76 + math.log10(1.0/1.0)  # 1:1 acetate buffer = pKa
    ratio_55 = 10.0**(5.5 - 4.76)       # base/acid ratio for pH 5.5
    print("[H+] in trichrome bath (pH 2.5): %.2e M" % h_trichrome)
    print("pH of 1:1 acetate buffer: %.2f" % ph_11)
    print("base:acid ratio for pH 5.5 acetate: %.2f" % ratio_55)
    assert 3.16e-3 < h_trichrome < 3.17e-3
    assert ph_11 == 4.76
    assert 5.49 < ratio_55 < 5.50
    print("rule: stain baths are pH instruments - meter them, do not guess")
    print("OK: %s metered the baths" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_hs_ihc(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # antibody dilution bench arithmetic
    stock_ugml = 1000.0
    working = stock_ugml/200.0
    vol_ul = 10.0/200.0*1000.0
    series = [stock_ugml/(100.0*2**i) for i in range(8)]
    print("working concentration at 1:200: %.1f ug/mL" % working)
    print("stock needed for 10 mL: %.0f uL" % vol_ul)
    print("8-well 2-fold series from 1:100 (ug/mL):")
    print("  " + ", ".join("%.4g" % c for c in series))
    assert working == 5.0
    assert vol_ul == 50.0
    assert abs(series[-1] - 0.078125) < 1e-9
    assert abs(series[0] - 10.0) < 1e-9
    print("rule: dilution is arithmetic - pipette the math, not the hope")
    print("OK: %s diluted the antibody" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_hs_microscopy(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # microscopist's table: magnifications, field, depth of field, e- wavelength
    mags = [o*10 for o in (4, 10, 20, 40, 100)]
    field_40x_mm = 22.0/40.0
    dof_um = 550e-9/(2.0*0.65**2)*1e6
    h, m, e, V, c = 6.626e-34, 9.109e-31, 1.602e-19, 1e5, 2.998e8
    lam = h/math.sqrt(2*m*e*V*(1 + e*V/(2*m*c**2)))
    lam_pm = lam*1e12
    print("total magnifications: %s" % mags)
    print("field at 40x (FN 22): %.2f mm" % field_40x_mm)
    print("depth of field at NA 0.65: %.3f um" % dof_um)
    print("electron wavelength at 100 kV: %.2f pm" % lam_pm)
    assert mags == [40, 100, 200, 400, 1000]
    assert field_40x_mm == 0.55
    assert 0.650 < dof_um < 0.652
    assert 3.69 < lam_pm < 3.71
    print("rule: know the field, the depth, and the wavelength - then choose the mode")
    print("OK: %s calibrated the optics" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_hs_junctions(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # transepithelial resistance -> paracellular conductance
    ter_leaky, ter_tight = 100.0, 10000.0  # ohm.cm^2
    g_leaky = 1.0/ter_leaky*1000.0         # mS/cm^2
    g_tight = 1.0/ter_tight*1000.0
    print("leaky epithelium:  TER %6.0f -> %.1f mS/cm^2" % (ter_leaky, g_leaky))
    print("tight epithelium:  TER %6.0f -> %.2f mS/cm^2" % (ter_tight, g_tight))
    print("paracellular flux ratio: %.0f:1" % (g_leaky/g_tight))
    assert g_leaky == 10.0
    assert g_tight == 0.1
    assert g_leaky/g_tight == 100.0
    print("rule: the seal has a rating - claudins set it, TER measures it")
    print("OK: %s rated the barrier" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_hs_blood(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # absolute differential from 7,000 WBC/uL; hematocrit from RBC x MCV
    wbc = 7000.0
    diff = {"neutrophils": 0.60, "lymphocytes": 0.30, "monocytes": 0.06,
            "eosinophils": 0.03, "basophils": 0.01}
    print("absolute differential at %.0f WBC/uL:" % wbc)
    for k, p in diff.items():
        print("  %-12s %4.0f /uL" % (k, wbc*p))
    hct = 5.0e6*90e-15/1e-6*100.0  # RBC/uL x MCV(L) / uL volume -> percent
    print("hematocrit from 5.0e6 RBC x 90 fL MCV: %.0f %%" % hct)
    assert wbc*diff["neutrophils"] == 4200.0
    assert wbc*diff["lymphocytes"] == 2100.0
    assert wbc*diff["basophils"] == 70.0
    assert hct == 45.0
    print("rule: percentages without totals are decoration - report absolutes")
    print("OK: %s counted the blood" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_hs_hemopoiesis(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # marrow throughput: 2e11 RBC/day, 1e11 platelets/day
    rbc_s = 2e11/86400.0
    plt_s = 1e11/86400.0
    print("red cells manufactured: %.0f per day = %.3g per second" % (2e11, rbc_s))
    print("platelets manufactured: %.0f per day = %.3g per second" % (1e11, plt_s))
    assert 2.314e6 < rbc_s < 2.315e6
    assert 1.157e6 < plt_s < 1.158e6
    print("rule: marrow is a factory - read the M:E ratio as its balance sheet")
    print("OK: %s ran the production line" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_hs_skin(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # epidermal conveyor: 28-day transit over ~15 cell layers
    layers, transit = 15.0, 28.0
    per_day = layers/transit
    corneum_turnover_d = 14.0
    print("epidermal layers replaced per day: %.3f" % per_day)
    print("stratum corneum turnover: every %.0f days" % corneum_turnover_d)
    assert 0.535 < per_day < 0.537
    assert layers/per_day == transit
    print("rule: skin is a conveyor - time the belt, then read the strata")
    print("OK: %s timed the conveyor" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_hs_gi_tract(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # absorptive amplification: plicae x villi x microvilli
    amp = 3.0*10.0*20.0
    smooth = math.pi*0.025*6.0
    functional = smooth*amp
    print("amplification factor: 3 x 10 x 20 = %.0f" % amp)
    print("smooth-tube area (6 m x 2.5 cm): %.3f m^2" % smooth)
    print("functional absorptive area: %.0f m^2" % functional)
    assert amp == 600.0
    assert 0.471 < smooth < 0.472
    assert 282.0 < functional < 284.0
    print("rule: the gut is a fractal - multiply the stages, price the area")
    print("OK: %s unfolded the gut" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_hs_liver_pancreas(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # classic lobule census: 1-mm hexagon, 20-um hepatocytes, 2-mm long
    r = 0.5  # mm
    area = (3.0*math.sqrt(3.0)/2.0)*r**2
    per_section = area/(0.02**2)
    total = per_section*(2.0/0.02)
    print("lobule cross-section: %.4f mm^2" % area)
    print("hepatocytes per section: %.0f" % per_section)
    print("hepatocytes per 2-mm lobule: %.0f" % total)
    assert 0.649 < area < 0.650
    assert 1623.0 < per_section < 1625.0
    assert 162000.0 < total < 163000.0
    print("rule: the lobule is a process unit - census it, then trace the flows")
    print("OK: %s counted the lobule" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_hs_respiratory(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # alveolar census: 70 m^2 over 480M alveoli
    per_m2 = 70.0/480e6
    per_mm2 = per_m2*1e6
    d_mm = math.sqrt(per_mm2/math.pi)
    branches = 2**23
    print("surface per alveolus: %.4f mm^2" % per_mm2)
    print("equivalent sphere diameter: %.3f mm" % d_mm)
    print("terminal branches after 23 generations: %d" % branches)
    assert 0.1458 < per_mm2 < 0.1459
    assert 0.215 < d_mm < 0.216
    assert branches == 8388608
    print("rule: 480 million parallel exchangers - the lung is a numbers game")
    print("OK: %s counted the alveoli" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_hs_urinary(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # GFR 125 mL/min -> L/day -> single-nephron GFR over 2M nephrons
    gfr_day_L = 125.0*1440.0/1000.0
    sngfr_nL_min = 125.0/2e6*1e6
    print("filtered per day: %.0f L" % gfr_day_L)
    print("single-nephron GFR: %.1f nL/min" % sngfr_nL_min)
    assert gfr_day_L == 180.0
    assert sngfr_nL_min == 62.5
    print("rule: the organ divides into nephrons - price each one")
    print("OK: %s filtered the numbers" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_hs_cardiovascular(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # cardiac output = HR x SV; circulation time = volume / output
    co_L_min = 70.0*70.0/1000.0
    circuit_s = 5.0/co_L_min*60.0
    print("cardiac output: 70 bpm x 70 mL = %.1f L/min" % co_L_min)
    print("one full circulation of 5 L: %.0f s" % circuit_s)
    assert co_L_min == 4.9
    assert 61.0 < circuit_s < 61.3
    print("rule: the pump closes the loop - output over volume is the tempo")
    print("OK: %s timed the circulation" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_hs_lymphoid(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # thoracic duct throughput shared over ~600 nodes
    per_day_mL = 100.0*24.0
    per_node_mL = per_day_mL/600.0
    print("thoracic duct return: %.0f mL/hr -> %.1f L/day" % (100.0, per_day_mL/1000.0))
    print("lymph filtered per node per day: %.1f mL" % per_node_mL)
    assert per_day_mL == 2400.0
    assert per_node_mL == 4.0
    print("rule: 600 screening stations share the flow - price each station")
    print("OK: %s metered the lymph" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_hs_endocrine(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # negative-feedback loop: TSH = 10/(1+T4/4); dT4 = (2*TSH - 0.5*T4)*dt
    t4, dt = 1.0, 0.1
    for _ in range(2000):
        tsh = 10.0/(1.0 + t4/4.0)
        t4 += (2.0*tsh - 0.5*t4)*dt
    analytic = (-0.5 + math.sqrt(0.25 + 10.0))/0.25
    print("simulated steady-state T4: %.4f" % t4)
    print("analytic steady state:      %.4f" % analytic)
    assert abs(t4 - analytic) < 0.05
    assert 10.80 < analytic < 10.81
    print("rule: the loop holds itself - feedback is the controller")
    print("OK: %s closed the loop" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_hs_bone(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # osteon lamellae: 200-um osteon, 50-um canal, 5-um lamellae
    wall = (200.0 - 50.0)/2.0
    lamellae = wall/5.0
    turnover_yr = 100.0/10.0
    print("osteon wall thickness: %.0f um" % wall)
    print("concentric lamellae: %.0f" % lamellae)
    print("skeleton turnover at 10%%/yr: every %.0f years" % turnover_yr)
    assert wall == 75.0
    assert lamellae == 15.0
    assert turnover_yr == 10.0
    print("rule: count the lamellae, budget the remodeling - bone is maintained, not made once")
    print("OK: %s cored the osteon" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_hs_male_repro(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # sperm production: 100M/day continuous
    per_s = 100e6/86400.0
    per_74d = 100e6*74.0
    print("sperm per second: %.1f" % per_s)
    print("sperm per 74-day pipeline: %.3g" % per_74d)
    assert 1157.4 < per_s < 1157.5
    assert per_74d == 7.4e9
    print("rule: the pipeline never stops - 74 days in, a thousand per second out")
    print("OK: %s ran the pipeline" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_hs_female_repro(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # ovarian attrition: 1.5M follicles at birth, ~400 ovulated
    atresia_pct = (1.5e6 - 400.0)/1.5e6*100.0
    print("follicles at birth: 1500000; ever ovulated: ~400")
    print("lost to atresia: %.3f %%" % atresia_pct)
    assert 99.973 < atresia_pct < 99.974
    print("rule: the ovary rations by attrition - count the stock, count the issues")
    print("OK: %s audited the inventory" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_hs_cns(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # cortical layer budget: 2.5 mm over 6 layers; cell census
    per_layer_mm = 2.5/6.0
    print("cortical thickness per layer: %.3f mm" % per_layer_mm)
    print("neurons: 86B total, 16B cortical; glia ~85B")
    assert 0.416 < per_layer_mm < 0.418
    assert 16.0/86.0 < 0.19
    print("rule: the cortex is six laminates - budget each, count the nodes")
    print("OK: %s mapped the cortex" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_hs_eye(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # photoreceptor census; foveal cones from density x area
    ratio = 120.0/6.0
    foveal = math.pi*0.75**2*200000.0
    print("rod:cone ratio: %.0f:1" % ratio)
    print("foveal cones (1.5-mm fovea at 200k/mm^2): %.0f" % foveal)
    assert ratio == 20.0
    assert 353429.0 < foveal < 353430.0
    print("rule: the sensor array has a spec sheet - read it layer by layer")
    print("OK: %s counted the pixels" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_hs_histopathology(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # grading metrics: mitoses per 10 HPF (2 mm^2); Ki-67 index
    mit_per_mm2 = 25.0/2.0
    ki67 = 300.0/1000.0*100.0
    print("mitotic density: 25 per 10 HPF -> %.1f /mm^2" % mit_per_mm2)
    print("Ki-67 proliferation index: 300/1000 -> %.0f %%" % ki67)
    assert mit_per_mm2 == 12.5
    assert ki67 == 30.0
    print("rule: grade with numbers - the diagnosis signs in counts")
    print("OK: %s graded the tumor" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_hs_artifacts(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # shrinkage and compression corrections
    slide_mm = 10.0*(1.0 - 0.13)
    effective_um = 5.0*(1.0 - 0.10)
    restored_mm = slide_mm/0.87
    print("10 mm fresh at 13%% shrinkage: %.1f mm on slide" % slide_mm)
    print("5-um section at 10%% compression: %.1f um effective" % effective_um)
    print("margin restored to fresh dimension: %.1f mm" % restored_mm)
    assert slide_mm == 8.7
    assert effective_um == 4.5
    assert abs(restored_mm - 10.0) < 1e-9
    print("rule: correct every dimension - the slide shrank, the truth did not")
    print("OK: %s subtracted the artifacts" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_hs_histomorphometry(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # point counting: 23 hits on 100 points -> volume fraction + binomial SE
    vf = 23.0/100.0
    se = math.sqrt(vf*(1.0 - vf)/100.0)
    print("volume fraction: %.2f" % vf)
    print("standard error: %.4f" % se)
    print("report: %.2f +/- %.3f" % (vf, se))
    assert vf == 0.23
    assert 0.0420 < se < 0.0422
    print("rule: Delesse never lies - but always report the error bar")
    print("OK: %s counted the points" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_hs_digital(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # whole-slide storage budget: 15x15 mm at 0.25 um/px
    px_side = 15e-3/0.25e-6
    px_total = px_side**2
    raw_GB = px_total*3.0/1e9
    stored_MB = raw_GB/30.0*1000.0
    print("pixels per side: %.0f" % px_side)
    print("total pixels: %.2e" % px_total)
    print("raw size: %.1f GB -> stored (~30:1): %.0f MB" % (raw_GB, stored_MB))
    assert px_side == 60000.0
    assert px_total == 3.6e9
    assert 10.79 < raw_GB < 10.81
    assert 359.0 < stored_MB < 361.0
    print("rule: budget the pixels before buying the scanner")
    print("OK: %s budgeted the slide" % NAME)
if __name__ == "__main__":
    main()
''')

DEMOS = {
    "what_is": demo_hs_what_is, "cells": demo_hs_cells,
    "four_tissues": demo_hs_four_tissues, "epithelium": demo_hs_epithelium,
    "connective": demo_hs_connective, "muscle": demo_hs_muscle,
    "nervous": demo_hs_nervous, "membranes": demo_hs_membranes,
    "fixation": demo_hs_fixation, "sectioning": demo_hs_sectioning,
    "he_stain": demo_hs_he_stain, "special_stains": demo_hs_special_stains,
    "ihc": demo_hs_ihc, "microscopy": demo_hs_microscopy,
    "junctions": demo_hs_junctions, "blood": demo_hs_blood,
    "hemopoiesis": demo_hs_hemopoiesis, "skin": demo_hs_skin,
    "gi_tract": demo_hs_gi_tract, "liver_pancreas": demo_hs_liver_pancreas,
    "respiratory": demo_hs_respiratory, "urinary": demo_hs_urinary,
    "cardiovascular": demo_hs_cardiovascular, "lymphoid": demo_hs_lymphoid,
    "endocrine": demo_hs_endocrine, "bone": demo_hs_bone,
    "male_repro": demo_hs_male_repro, "female_repro": demo_hs_female_repro,
    "cns": demo_hs_cns, "eye": demo_hs_eye,
    "histopathology": demo_hs_histopathology, "artifacts": demo_hs_artifacts,
    "histomorphometry": demo_hs_histomorphometry, "digital": demo_hs_digital,
}
assert set(DEMOS) == {e["key"] for e in ENTRIES}, "demo map misses entries"


def build_records(slug, source):
    cfg = DBCFG[slug]
    sig = source == "signature"
    ordered = sorted(enumerate(ENTRIES), key=lambda p: (p[1]["ladder_rank"], p[0]))
    recs = []
    for _, e in ordered:
        name = e["name"]
        title = name + " (Signature Edition)" if sig else name
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
    for slug in ("histology", "histology-signature"):
        source = "signature" if slug.endswith("-signature") else "public"
        built[slug] = build_records(slug, source)

    total = 0
    for slug, recs in built.items():
        cfg = DBCFG[slug]
        ids = [r["id"] for r in recs]
        assert len(ids) == len(set(ids)), "dup ids in %s" % slug
        assert all(i.startswith(cfg["prefix"]) for i in ids), "prefix drift in %s" % slug
        assert len(recs) == 34, "expected 34 records in %s, got %d" % (slug, len(recs))
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
