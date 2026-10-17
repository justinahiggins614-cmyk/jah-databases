#!/usr/bin/env python3
"""Build the Embryology field databases for JAH Databases (field #36, taxonomy order).

Verified 2026-10-17 (see entries_embryology.py docstring): NO database
covers embryology as a discipline (prenatal development: gametogenesis,
fertilization, cleavage, blastulation, gastrulation, neurulation,
organogenesis by system, fetal development timeline, placenta and
membranes, developmental genetics, teratology, assisted reproduction).

Manifest search (2,372 databases): zero 'embryolog*' slugs/names; no
db/embryolog* dirs. Whole-system exact-title sweep over the dedupe gate:
zero collisions for all 34 planned titles x2 editions (68 variants).
Near-neighbors confirmed different disciplines: 'anatomy' (gross adult
anatomy), 'histology' (microscopic tissues), 'cell-biology' (cell biology
as a field), 'pathology' (disease mechanisms). No pregnancy, fetus,
placenta, obstetrics, IVF, fertility, or reproduction databases exist.
ZERO full-record discipline coverage anywhere.

So this build creates two NEW databases, 34 ladder-ordered records each:

  embryology                - The Embryology Database
                               (public-harvest: real, fact-checked prenatal
                               development; standard references Sadler
                               'Langman's Medical Embryology' 15th ed 2024;
                               Moore/Persaud/Torchia 'The Developing Human'
                               11th ed 2020; Schoenwolf et al. 'Larsen's
                               Human Embryology' 6th ed 2021; Gilbert/Barresi
                               'Developmental Biology' 13th ed 2023; Carlson
                               'Human Embryology and Developmental Biology'
                               6th ed 2019; Dudek 'Embryology (BRS)' 7th ed
                               2019; O'Rahilly/Muller 'Human Embryology &
                               Teratology' 3rd ed 2001)
  embryology-signature      - The Embryology Signature Database
                               (his original Signature interpretation of
                               prenatal development as the timed construction
                               of the human body; src signature, titles
                               suffixed " (Signature Edition)", never
                               presented as authentic public record)

34 records each, ordered by the teaching ladder (ladder_rank 1-10,
ladder_tier foundations/compounded/advanced); the shard index is written in
ladder order so pages present simple -> compounded -> complex.

ID prefixes: JAH-EBR- (public) and JAH-EBS- (signature). JAH-EMB- was
unavailable (taken by the 'embeddings' database), so EMBRyology takes
JAH-EBR- and the signature edition takes JAH-EBS-.

Subtitle disambiguation (fields #13-35 pattern): specialty titles carry
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
from entries_embryology import ENTRIES, SIG_TAIL

# ---------------------------------------------------------------- DB config

def _cfg(slug, name, tagline, record_kind, prefix, ai, role, citation, source):
    sig_line = ("Signature originals - his original Signature interpretation of prenatal "
                "development as the timed construction of the human body: every stage a "
                "build phase, every organ a system coming online on schedule. Clearly "
                "labeled Signature-made, never presented as authentic public record.")
    pub_line = ("Public records - real, fact-checked embryology: what embryology is; "
                "gametogenesis; spermatogenesis; oogenesis; fertilization; cleavage; "
                "blastulation; implantation; the bilaminar disc; the trilaminar disc; "
                "extraembryonic membranes; gastrulation; neurulation; body axes; "
                "somitogenesis; folding of the embryo; the placenta; the heart; vascular "
                "development; skeletal development; muscle development; skin development; "
                "lung development; digestive system development; urinary system "
                "development; genital development; nervous system development; eye and "
                "ear development; endocrine development; developmental genetics; "
                "teratology; twinning; the fetal period; assisted reproduction, "
                "organized in the Signature system.")
    ladder = (" Records are ordered by the teaching ladder: Foundations (what embryology "
              "is, gametogenesis, spermatogenesis, oogenesis, fertilization, cleavage, "
              "blastulation, implantation, bilaminar disc, trilaminar disc, membranes) -> "
              "Compounded (gastrulation, neurulation, body axes, somitogenesis, folding, "
              "placenta, heart, vessels, skeleton, muscle, skin, lungs) -> Advanced "
              "(gut, kidneys, genital system, brain, eye and ear, endocrine glands, "
              "developmental genetics, teratology, twinning, fetal growth, assisted "
              "reproduction).")
    return {
        "name": name, "tagline": tagline, "record_kind": record_kind,
        "prefix": prefix, "ai": ai, "role": role,
        "hero_p": "%s - %s Every record carries the full entry: description, how it works, "
                  "key points, requirements, standards, citations, and a working demonstration "
                  "program.%s" % (tagline, sig_line if source == "signature" else pub_line, ladder),
        "sig_type": ("Signature originals organized in the Signature system"
                     if source == "signature" else
                     "Public records organized in the Signature system"),
        "search_ph": "Search gastrulation, neurulation, Hox genes, placenta, heart looping, somites, teratogens, twinning...",
        "chat_ph": "Ask about embryology...",
        "archive_blurb": ("Seeded %s embryology records, marching toward one million records. "
                          "Presented in teaching-ladder order: foundations, compounded, advanced."
                          % ("Signature-original" if source == "signature" else "public-record")),
        "schema": ("id, t, g, name, title, description, how_it_works, key_points, requirements, "
                   "standards, citations, src, ladder_rank, ladder_tier, demo"),
        "fields": "Foundations \u00b7 Compounded \u00b7 Advanced - each tier opens on demand and loads only what you open",
        "gen_desc": "Generate clearly-labeled embryology studies. Seeded archive records are the authoritative entries.",
        "greet": "I am the %s. Ask me about embryology - from what it is through gametogenesis, spermatogenesis, oogenesis, fertilization, cleavage, blastulation, implantation, the bilaminar and trilaminar discs, and the membranes, through gastrulation, neurulation, body axes, somitogenesis, folding, the placenta, the heart, vessels, skeleton, muscle, skin, and lungs, to the gut, kidneys, genital system, brain, eye and ear, endocrine glands, developmental genetics, teratology, twinning, the fetal timeline, and assisted reproduction." % ai,
        "gen_fields": ["Foundations", "Compounded", "Advanced"],
        "gen_kind": "embryology-study", "gen_demo_kind": "embryology-demo",
        "source": source,
    }

CIT_PUB = ("Embryology (standard references: Sadler Langman Medical Embryology "
           "15th ed 2024; Moore Persaud Torchia The Developing Human 11th ed 2020; "
           "Schoenwolf et al Larsen Human Embryology 6th ed 2021; Gilbert Barresi "
           "Developmental Biology 13th ed 2023; Carlson Human Embryology and "
           "Developmental Biology 6th ed 2019; Dudek Embryology BRS 7th ed 2019; "
           "O Rahilly Muller Human Embryology and Teratology 3rd ed 2001).")
CIT_SIG = CIT_PUB + (" Signature editions are his original Signature interpretation "
                     "of prenatal development, clearly labeled Signature-made.")

DBCFG = {}
DBCFG["embryology"] = _cfg(
    "embryology", "The Embryology Database",
    "Real, fact-checked embryology: from what embryology is through gametogenesis, "
    "spermatogenesis, oogenesis, fertilization, cleavage, blastulation, implantation, "
    "the bilaminar and trilaminar discs, and the membranes, through gastrulation, "
    "neurulation, body axes, somitogenesis, folding, the placenta, the heart, vessels, "
    "skeleton, muscle, skin, and lungs, to the gut, kidneys, genital system, brain, "
    "eye and ear, endocrine glands, developmental genetics, teratology, twinning, the "
    "fetal timeline, and assisted reproduction - taught progressively along the ladder.",
    "embryology record", "JAH-EBR-", "JAH Embryology Archivist",
    "embryology archivist - prenatal development: gametogenesis, fertilization, "
    "cleavage, blastulation, implantation, gastrulation, neurulation, body axes, "
    "organogenesis by system, placenta and membranes, developmental genetics, "
    "teratology, twinning, the fetal timeline, and assisted reproduction; teaching "
    "progressively along the ladder from foundations through compounded to advanced; "
    "answers from many angles - definition, example, analogy, application, history, "
    "math, how-to - using only archive data from this system",
    CIT_PUB, "public")
DBCFG["embryology-signature"] = _cfg(
    "embryology-signature", "The Embryology Signature Database",
    "His original Signature interpretation of prenatal development as the timed "
    "construction of the human body: the full ladder from gametes and fertilization "
    "through gastrulation, organogenesis, and fetal growth to assisted reproduction, "
    "reframed as Signature science. Clearly labeled Signature-made, never presented "
    "as authentic public record.",
    "embryology record", "JAH-EBS-", "JAH Embryology Archivist (Signature)",
    "embryology archivist - Signature editions: his original Signature interpretation "
    "of prenatal development as the timed construction of the human body, clearly "
    "labeled Signature-made and never presented as authentic public record; teaches "
    "progressively along the ladder from foundations through compounded to advanced; "
    "answers from many angles - definition, example, analogy, application, history, "
    "math, how-to - using only archive data from this system",
    CIT_SIG, "signature")

base.DBCFG = DBCFG
# ---------------------------------------------------------------- demos
# Every demo is real, runnable, stdlib-only Python performing the actual
# embryology computation for its record. All are machine-executed by main().

_PREAMBLE = (
"import math\n"
)

def _wrap(name, rid, group, body):
    return (base._hdr(name, rid, group) + _PREAMBLE + body.replace("NAME", json.dumps(name)))

def demo_eb_what_is(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # gestation calendar: 280 d gestational = 266 d fertilization age
    gest, fert = 280.0, 280.0 - 14.0
    weeks = gest/7.0
    lunar = gest/28.0
    embryonic_d = 8.0*7.0
    embryonic_share = embryonic_d/gest
    print("gestation: %.0f d = %.0f weeks = %.0f lunar months" % (gest, weeks, lunar))
    print("fertilization age: %.0f d (%.0f d younger than gestational)" % (fert, gest - fert))
    print("embryonic period: %.0f d = %.1f %% of gestation" % (embryonic_d, embryonic_share*100.0))
    assert weeks == 40.0
    assert lunar == 10.0
    assert fert == 266.0
    assert embryonic_share == 0.2
    print("rule: two clocks, never mixed - gestational for the clinic, fertilization for the biology")
    print("OK: %s ran the calendar" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_eb_gametogenesis(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # independent assortment: 2^23 gamete variants per person
    combos = 2**23
    print("chromosome pairs: 23 -> haploid number: 23")
    print("independent-assortment gamete variants: 2^23 = %d" % combos)
    print("possible child genomes from two parents: %.3e" % (combos**2))
    assert combos == 8388608
    assert combos**2 == 70368744177664
    print("rule: halve the count, shuffle the deck - every gamete is one of 8.4 million")
    print("OK: %s shuffled the deck" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_eb_spermatogenesis(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # division tree: 5 mitoses -> 32 primary spermatocytes -> x4 spermatids
    primary = 2**5
    per_founder = primary*4
    cycle_d, daily = 64.0, 100e6
    pipeline = daily*cycle_d
    print("primary spermatocytes per founder: 2^5 = %d" % primary)
    print("spermatozoa per founder: %d x 4 = %d" % (primary, per_founder))
    print("pipeline stock at %.0f-day cycle: %.3g sperm" % (cycle_d, pipeline))
    assert primary == 32
    assert per_founder == 128
    assert pipeline == 6.4e9
    print("rule: 128x per founder, 64-day takt - throughput is founders times tree over time")
    print("OK: %s ran the production line" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_eb_oogenesis(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # attrition: 7M fetal -> 2M birth -> 350K puberty -> ~450 ovulated
    fetal, birth, puberty, ovulated = 7e6, 2e6, 350e3, 450.0
    s1 = birth/fetal*100.0
    s2 = puberty/birth*100.0
    attr = (fetal - ovulated)/fetal*100.0
    print("survive to birth: %.2f %%" % s1)
    print("survive birth->puberty: %.2f %%" % s2)
    print("lifetime attrition: %.4f %%" % attr)
    print("max polar bodies per completed meiosis: 3")
    assert 28.57 < s1 < 28.58
    assert 17.49 < s2 < 17.51
    assert 99.9935 < attr < 99.9936
    print("rule: the ovary rations by attrition - audit the stock at every stage")
    print("OK: %s audited the reserve" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_eb_fertilization(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # selection: ~200 of 300M reach the ampulla; 23 + 23 = 46
    deposited, reach = 300e6, 200.0
    ratio = reach/deposited
    print("deposited: %.0f -> reach ampulla: %.0f" % (deposited, reach))
    print("pass rate: %.4g (%.6f %%)" % (ratio, ratio*100.0))
    print("chromosome restoration: 23 + 23 = %d" % (23 + 23))
    assert 6.66e-7 < ratio < 6.67e-7
    assert 23 + 23 == 46
    print("rule: two in ten million get through - then one fuses and the zona locks")
    print("OK: %s ran the selection" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_eb_cleavage(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # 4 rounds -> 16-cell morula; volume conserved, diameter shrinks by cubert(2)
    n4 = 2**4
    d0_um = 100.0
    v0 = 4.0/3.0*math.pi*(d0_um/2.0)**3
    v_cell = v0/n4
    d_cell = (6.0*v_cell/math.pi)**(1.0/3.0)
    print("morula cells after 4 rounds: %d" % n4)
    print("zygote volume: %.0f um^3 -> per blastomere: %.0f um^3" % (v0, v_cell))
    print("blastomere diameter: %.2f um" % d_cell)
    print("7 rounds -> %d cells (blastocyst order)" % 2**7)
    assert n4 == 16
    assert 523598.0 < v0 < 523600.0
    assert 39.6 < d_cell < 39.8
    assert 2**7 == 128
    print("rule: subdivide a fixed budget - no growth until the budget is spent")
    print("OK: %s split the volume" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_eb_blastulation(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # day-5 census: ~100 cells, ~1/4 ICM, ~3/4 trophectoderm
    total, icm = 100.0, 25.0
    te = total - icm
    print("blastocyst census: %.0f cells" % total)
    print("inner cell mass: %.0f (%.0f %%)" % (icm, icm/total*100.0))
    print("trophectoderm: %.0f (%.0f %%)" % (te, te/total*100.0))
    print("support-to-core ratio: %.1f : 1" % (te/icm))
    assert te == 75.0
    assert te/icm == 3.0
    print("rule: support staff outnumbers the core team 3 to 1 - life support first")
    print("OK: %s took the census" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_eb_implantation(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # hCG doubles every 48 h from ~5 mIU/mL at implantation (day 6)
    hcg0, thresh = 5.0, 25.0
    curve = [(6 + 2*i, hcg0*2**i) for i in range(5)]
    print("hCG curve (day: mIU/mL):")
    for d, h in curve:
        print("  day %2d: %6.1f %s" % (d, h, "<- detectable" if h >= thresh else ""))
    window = 24 - 20 + 1
    print("implantation window: cycle days 20-24 = %d days" % window)
    assert curve[2] == (10, 20.0)
    assert curve[3] == (12, 40.0)
    assert window == 5
    print("rule: the keep-alive signal doubles on schedule - read the curve, not the hope")
    print("OK: %s tracked the signal" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_eb_bilaminar_disc(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # week-2 disc: 0.5 mm diameter -> area
    d_mm = 0.5
    area = math.pi*(d_mm/2.0)**2
    print("disc diameter: %.1f mm -> area: %.4f mm^2" % (d_mm, area))
    print("layers: 2 (epiblast above, hypoblast below)")
    print("cavities: amniotic above, yolk sac below, chorionic outside")
    assert 0.1963 < area < 0.1964
    print("rule: the whole future body is a speck - two slabs and three cavities")
    print("OK: %s surveyed the site" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_eb_trilaminar_disc(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # streak occupies ~half the 2-mm disc at peak; 3 germ layers
    disc_mm, streak_mm = 2.0, 1.0
    share = streak_mm/disc_mm
    layers = ["ectoderm", "mesoderm", "endoderm"]
    print("streak share of disc: %.1f/%.1f mm = %.0f %%" % (streak_mm, disc_mm, share*100.0))
    print("germ layers: %d (%s)" % (len(layers), ", ".join(layers)))
    assert share == 0.5
    assert len(layers) == 3
    print("rule: three material stocks, no fourth supplier - every organ traces to week 3")
    print("OK: %s issued the materials" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_eb_membranes(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # amniotic fluid: 30 mL (wk10) -> 350 mL (wk20) -> 1000 mL (term)
    v10, v20, vterm = 30.0, 350.0, 1000.0
    rate = (v20 - v10)/((20 - 10)*7.0)
    cord_L, cord_d = 55.0, 2.0  # cm
    cord_vol = math.pi*(cord_d/2.0)**2*cord_L
    print("fluid wk10->wk20 growth: %.2f mL/day" % rate)
    print("fluid gain to term: %.0f mL" % (vterm - v10))
    print("cord volume (55 cm x 2 cm): %.1f cm^3" % cord_vol)
    print("cord vessels: 2 arteries + 1 vein")
    assert 4.57 < rate < 4.58
    assert 172.7 < cord_vol < 172.8
    print("rule: budget the fluid and the cable - both are temporary infrastructure")
    print("OK: %s plumbed the site" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_eb_gastrulation(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # streak: 1 mm peak at day 19, regressed by day 26
    peak_um, d0, d1 = 1000.0, 19.0, 26.0
    per_day = peak_um/(d1 - d0)
    per_hr = per_day/24.0
    print("streak regression: %.0f um over %.0f days" % (peak_um, d1 - d0))
    print("regression rate: %.2f um/day = %.2f um/hr" % (per_day, per_hr))
    assert 142.85 < per_day < 142.87
    assert 5.95 < per_hr < 5.96
    print("rule: the front must sweep the full length and demobilize cleanly")
    print("OK: %s ran the front" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_eb_neurulation(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # plate day 18; cranial neuropore closes day 25; caudal day 28
    total_d = 28 - 18
    window_d = 28 - 25
    ntd_per_1000 = 1.0
    with_fa = ntd_per_1000*(1.0 - 0.60)  # 60% reduction from folic acid
    print("neurulation span: day 18 -> day 28 = %d days" % total_d)
    print("closure window after cranial shut: %d days" % window_d)
    print("NTD rate: %.1f/1000 -> with folic acid: %.1f/1000" % (ntd_per_1000, with_fa))
    assert total_d == 10
    assert window_d == 3
    assert with_fa == 0.4
    print("rule: two hard close-out dates - day 25 cranial, day 28 caudal")
    print("OK: %s zipped the tube" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_eb_body_axes(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # French flag: one gradient, two thresholds -> three fates
    t1, t2 = 1.0/3.0, 2.0/3.0
    hox = [11, 10, 9, 9]
    total_hox = sum(hox)
    homeobox_aa = 180//3
    print("French-flag thresholds at %.3f and %.3f of the gradient" % (t1, t2))
    print("Hox clusters A-D: %s = %d genes" % (hox, total_hox))
    print("homeobox: 180 bp / 3 = %d amino acids" % homeobox_aa)
    assert abs(t1 - 0.3333) < 0.001
    assert total_hox == 39
    assert homeobox_aa == 60
    print("rule: position is address - one gradient, two thresholds, 39 entries of ROM")
    print("OK: %s staked the axes" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_eb_somitogenesis(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # census: 4 occipital + 8 cervical + 12 thoracic + 5 lumbar + 5 sacral + 9 coccygeal
    regions = [("occipital", 4), ("cervical", 8), ("thoracic", 12),
               ("lumbar", 5), ("sacral", 5), ("coccygeal", 9)]
    total = sum(n for _, n in regions)
    print("somite census:")
    for rname, n in regions:
        print("  %-10s %2d pairs" % (rname, n))
    print("total: %d pairs (range 42-44: %s)" % (total, 42 <= total <= 44))
    print("compartments per somite: 3 (sclerotome, myotome, dermatome)")
    assert total == 43
    assert 42 <= total <= 44
    print("rule: one tool, one rhythm - stamp the segments, then customize by address")
    print("OK: %s counted the segments" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_eb_folding(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # 4 fold events in week 4; disc 2 mm -> C-shaped cylinder, CRL ~2.5 mm
    folds = ["head fold", "tail fold", "left lateral fold", "right lateral fold"]
    crl_mm = 2.5
    print("fold events: %d (%s)" % (len(folds), ", ".join(folds)))
    print("result: flat disc -> curved cylinder, CRL ~%.1f mm" % crl_mm)
    print("captured inside: gut tube; carried ventral: umbilical cord")
    assert len(folds) == 4
    assert crl_mm == 2.5
    print("rule: four bends make the tube - check the belly seam")
    print("OK: %s folded the sheet" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_eb_placenta(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # intervillous 150 mL at 600 mL/min -> 4 turnovers/min; 12 m^2 vs disc
    iv_ml, flow = 150.0, 600.0
    turnover = flow/iv_ml
    disc_m2 = math.pi*0.10**2
    exchange_m2 = 12.0
    amp = exchange_m2/disc_m2
    print("intervillous turnover: %.0f/%.0f = %.1f x per min" % (flow, iv_ml, turnover))
    print("exchange surface: %.0f m^2 vs disc %.4f m^2 -> %.0f x folded" % (exchange_m2, disc_m2, amp))
    print("term weight: ~500 g across a ~20 cm disc")
    assert turnover == 4.0
    assert 381.0 < amp < 383.0
    print("rule: the exchanger is a folded pancake - price it by turnover")
    print("OK: %s commissioned the plant" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_eb_heart(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # rate 100 -> 170 bpm over weeks 5-9; beats across weeks 5-8 at ~135 avg
    slope = (170.0 - 100.0)/4.0
    beats = 135.0*60.0*24.0*28.0
    shunts = ["foramen ovale", "ductus arteriosus", "ductus venosus"]
    print("rate ramp: 100 -> 170 bpm = %.1f bpm/week" % slope)
    print("beats in embryonic weeks 5-8: %.3g" % beats)
    print("fetal shunts: %d (%s)" % (len(shunts), ", ".join(shunts)))
    assert slope == 17.5
    assert beats == 5443200.0
    assert len(shunts) == 3
    print("rule: commissioned before the walls exist - the pump never stops for the changeover")
    print("OK: %s timed the pump" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_eb_vascular(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # 12 dichotomous generations -> 4096 terminal branches; 6 arch pairs
    branches = 2**12
    arches = 6
    fates = {"III": "carotids", "IV-left": "aortic arch", "VI": "pulmonary + ductus arteriosus",
             "I": "regresses", "II": "regresses", "IV-right": "subclavian"}
    print("terminal branches after 12 generations: %d" % branches)
    print("aortic arch pairs installed: %d" % arches)
    for a, f in fates.items():
        print("  arch %-8s -> %s" % (a, f))
    assert branches == 4096
    assert arches == 6
    assert len(fates) == 6
    print("rule: install six, demolish selectively - the schedule is the anatomy")
    print("OK: %s plumbed the arches" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_eb_skeletal(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # ~300 bones at birth -> 206 adult; femur 75 mm -> 450 mm
    fusions = 300 - 206
    growth = 450.0/75.0
    print("birth-to-adult fusions: 300 - 206 = %d" % fusions)
    print("femur growth: 75 mm -> 450 mm = %.1f x" % growth)
    print("primary centers: diaphysis, weeks 8-12; secondary: epiphyses, postnatal")
    assert fusions == 94
    assert growth == 6.0
    print("rule: prototype in cartilage, ship in bone - swap the material, keep the geometry")
    print("OK: %s cast the skeleton" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_eb_muscle(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # 1-cm fiber, 50 um diameter; myonuclear domain ~20000 um^3
    L_um, d_um, domain = 10000.0, 50.0, 20000.0
    vol = math.pi*(d_um/2.0)**2*L_um
    nuclei = vol/domain
    print("fiber volume: %.3g um^3" % vol)
    print("myoblasts fused per cm of fiber: %.0f" % nuclei)
    print("regulators in order: MyoD -> myogenin -> MRF4")
    assert 1.963e7 < vol < 1.964e7
    assert 981.0 < nuclei < 983.0
    print("rule: each nucleus buys 20000 um^3 - the fiber keeps hiring until covered")
    print("OK: %s merged the myoblasts" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_eb_integument(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # 2 layers (wk8) -> 5 layers (wk16); periderm shed wk21; vernix from wk20
    layers_8, layers_16 = 2, 5
    added = layers_16 - layers_8
    per_week = added/8.0
    vernix_wks = 40 - 20
    print("stratification: %d -> %d layers = +%.3f layers/week" % (layers_8, layers_16, per_week))
    print("periderm shed: week 21; vernix coverage: %d weeks" % vernix_wks)
    assert added == 3
    assert per_week == 0.375
    assert vernix_wks == 20
    print("rule: temporary coating while the hull cures, then wax for the months at sea")
    print("OK: %s sealed the hull" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_eb_respiratory(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # 23 generations -> 2^23 airways; first 16 conducting; 5 stages
    airways = 2**23
    conducting = 2**16
    stages = ["embryonic", "pseudoglandular", "canalicular", "saccular", "alveolar"]
    print("terminal airways: 2^23 = %d" % airways)
    print("conducting branches: 2^16 = %d" % conducting)
    print("stages: %d; surfactant from ~week 24" % len(stages))
    assert airways == 8388608
    assert conducting == 65536
    assert len(stages) == 5
    print("rule: ducts first, anti-collapse coating second, dry run on fluid for months")
    print("OK: %s branched the tree" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_eb_digestive(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # 270-degree CCW rotation; herniation weeks 6-10; Meckel 2%
    turns = 270.0/360.0
    hernia_wks = 10 - 6
    meckel_per_1000 = 0.02*1000.0
    print("midgut rotation: 270 deg = %.2f of a full turn" % turns)
    print("herniation: weeks 6-10 = %d weeks outside" % hernia_wks)
    print("Meckel diverticulum: 2%% -> %.0f per 1000 people" % meckel_per_1000)
    assert turns == 0.75
    assert hernia_wks == 4
    assert meckel_per_1000 == 20.0
    print("rule: rotate exactly 270, close the hatch by week 10")
    print("OK: %s swung the gut" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_eb_urinary(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # 3 kidney systems; ~2M nephrons; ~1 L/day fetal urine at term
    systems = ["pronephros", "mesonephros", "metanephros"]
    nephrons = 2*1e6
    urine_ml_min = 1000.0/1440.0
    print("kidney systems attempted: %d (%s)" % (len(systems), ", ".join(systems)))
    print("nephrons shipped: %.3g" % nephrons)
    print("fetal urine at term: 1000 mL/day = %.3f mL/min" % urine_ml_min)
    assert len(systems) == 3
    assert nephrons == 2e6
    assert 0.694 < urine_ml_min < 0.695
    print("rule: three prototypes, one shipped - the last one iterates a million filters")
    print("OK: %s plumbed the kidney" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_eb_genital(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # SRY switch at week 7; ~3% cryptorchid at birth; ~75% resolve in year 1
    per_1000 = 1000.0
    crypt = per_1000*0.03
    resolve = crypt*0.75
    persist = crypt - resolve
    print("indifferent until week 7; SRY flips the switch")
    print("cryptorchid at birth: %.0f per 1000 male births" % crypt)
    print("resolve in year 1: %.1f -> persist: %.1f" % (resolve, persist))
    assert crypt == 30.0
    assert resolve == 22.5
    assert persist == 7.5
    print("rule: one bit selects the package - then ship the testes to external housing")
    print("OK: %s threw the switch" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_eb_nervous(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # 250k neurons/min peak; 16B cortical neurons -> 64000 min = 44.4 days
    rate = 250000.0
    cortical = 16e9
    minutes = cortical/rate
    days = minutes/1440.0
    print("peak production: %.0f neurons/min" % rate)
    print("16B cortical neurons need %.0f min = %.2f days of peak output" % (minutes, days))
    print("fits inside the weeks 8-16 window: %s" % (days < 63.0))
    print("brain total: ~86B neurons; cortex: 6 layers, inside-out")
    assert minutes == 64000.0
    assert 44.44 < days < 44.45
    assert days < 63.0
    print("rule: build twice what you need, then let the workload prune")
    print("OK: %s wired the cortex" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_eb_eye_ear(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # lens placode day 27 -> lens vesicle day 33; cochlea 2.5 turns = 900 deg
    induction_d = 33 - 27
    coil_deg = 2.5*360.0
    print("placode to vesicle: day 27 -> day 33 = %d days" % induction_d)
    print("cochlear coil: 2.5 turns = %.0f degrees" % coil_deg)
    print("retinal layers: 10; choroid fissure closes week 7")
    assert induction_d == 6
    assert coil_deg == 900.0
    print("rule: every part summons the next - map the dependency graph")
    print("OK: %s built the sensors" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_eb_endocrine(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # fetal adrenals ~8 g on 3.4 kg vs adult ~8 g on 70 kg -> ~20x relative
    ratio = 70.0/3.4
    glands = ["pituitary", "thyroid", "parathyroids x4", "thymus",
              "adrenals x2", "pancreatic islets", "pineal"]
    print("gland origins assembled: %d" % len(glands))
    print("fetal adrenal relative size: 70/3.4 = %.2f x adult" % ratio)
    assert len(glands) == 7
    assert 20.5 < ratio < 20.6
    print("rule: the control plane is bolted together from six different shops")
    print("OK: %s wired the controls" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_eb_dev_genetics(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # 11 + 10 + 9 + 9 = 39 Hox genes; 13 paralog groups; 180 bp = 60 aa
    clusters = [11, 10, 9, 9]
    total = sum(clusters)
    aa = 180//3
    print("Hox clusters: %s = %d genes in 4 clusters" % (clusters, total))
    print("paralog groups: 13; homeobox: %d amino acids" % aa)
    assert total == 39
    assert aa == 60
    print("rule: position is address - chromosomal order equals body order")
    print("OK: %s read the ROM" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_eb_teratology(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # thalidomide window days 20-36; 20% vs 3% background
    window_d = 36 - 20
    background, exposed = 3.0, 20.0
    rr = exposed/background
    critical_wks = 8 - 3 + 1
    print("thalidomide window: days 20-36 = %d days" % window_d)
    print("malformation: %.0f%% background -> %.0f%% exposed = RR %.2f" % (background, exposed, rr))
    print("structural critical period: weeks 3-8 = %d weeks" % critical_wks)
    assert window_d == 16
    assert 6.66 < rr < 6.67
    assert critical_wks == 6
    print("rule: same dose, different week, different outcome - timing is the master variable")
    print("OK: %s filed the incident report" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_eb_twins(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # per 1000 MZ: 275 DCDA / 700 MCDA / 20 MCMA / 5 conjoined
    table = [("DCDA (0-3d)", 275), ("MCDA (4-8d)", 700),
             ("MCMA (9-12d)", 20), ("conjoined (13+d)", 5)]
    total = sum(n for _, n in table)
    print("chorionicity per 1000 monozygotic pregnancies:")
    for label, n in table:
        print("  %-18s %3d (%.1f %%)" % (label, n, n/10.0))
    print("MZ rate: 1/250 = %.3f" % (1.0/250.0))
    assert total == 1000
    assert 1.0/250.0 == 0.004
    print("rule: fork early, separate utilities - fork late, share the plant")
    print("OK: %s split the order" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_eb_fetal_timeline(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # 300 g (wk20) -> 3400 g (term); last 12 weeks: 2400 g / 84 d
    gain_total = 3400.0/300.0
    late_gain = (3400.0 - 1000.0)/((40 - 28)*7.0)
    print("mass gain wk20->term: 300 g -> 3400 g = %.2f x" % gain_total)
    print("late gain wk28-40: 2400 g / 84 d = %.2f g/day" % late_gain)
    print("viability threshold: ~week 24 (surfactant + brainstem + skin)")
    assert 11.33 < gain_total < 11.34
    assert 28.57 < late_gain < 28.58
    print("rule: elevenfold mass gain, slowest system sets the launch window")
    print("OK: %s ran the ramp" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_eb_art(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # pipeline: 12 oocytes -> 70% fertilize -> 45% blastulate -> 1 transferred
    oocytes = 12.0
    fertilized = oocytes*0.70
    blasts = fertilized*0.45
    print("retrieved: %.0f oocytes" % oocytes)
    print("fertilized (70%%): %.1f" % fertilized)
    print("blastocysts (45%%): %.2f -> transfer 1" % blasts)
    print("surplus vitrified at >90%% survival; first IVF birth 1978")
    assert 8.399 < fertilized < 8.401
    assert 3.77 < blasts < 3.79
    print("rule: controlled inputs, measured yields - one unit per shipment")
    print("OK: %s ran the clean room" % NAME)
if __name__ == "__main__":
    main()
''')

DEMOS = {
    "what_is": demo_eb_what_is, "gametogenesis": demo_eb_gametogenesis,
    "spermatogenesis": demo_eb_spermatogenesis, "oogenesis": demo_eb_oogenesis,
    "fertilization": demo_eb_fertilization, "cleavage": demo_eb_cleavage,
    "blastulation": demo_eb_blastulation, "implantation": demo_eb_implantation,
    "bilaminar_disc": demo_eb_bilaminar_disc, "trilaminar_disc": demo_eb_trilaminar_disc,
    "membranes": demo_eb_membranes, "gastrulation": demo_eb_gastrulation,
    "neurulation": demo_eb_neurulation, "body_axes": demo_eb_body_axes,
    "somitogenesis": demo_eb_somitogenesis, "folding": demo_eb_folding,
    "placenta": demo_eb_placenta, "heart": demo_eb_heart,
    "vascular": demo_eb_vascular, "skeletal": demo_eb_skeletal,
    "muscle": demo_eb_muscle, "integument": demo_eb_integument,
    "respiratory": demo_eb_respiratory, "digestive": demo_eb_digestive,
    "urinary": demo_eb_urinary, "genital": demo_eb_genital,
    "nervous": demo_eb_nervous, "eye_ear": demo_eb_eye_ear,
    "endocrine": demo_eb_endocrine, "dev_genetics": demo_eb_dev_genetics,
    "teratology": demo_eb_teratology, "twins": demo_eb_twins,
    "fetal_timeline": demo_eb_fetal_timeline, "art": demo_eb_art,
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
    for slug in ("embryology", "embryology-signature"):
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
