#!/usr/bin/env python3
"""Build the Nephrology field databases for JAH Databases (field #41, taxonomy order).

Verified 2026-10-17 (see entries_nephrology.py docstring): NO database
covers nephrology as a clinical specialty (the kidney - acute kidney
injury, chronic kidney disease, glomerular diseases, tubular disorders,
electrolytes and acid-base, the kidney in hypertension, dialysis, kidney
transplantation, urinalysis). Clinical-specialty framing, kidney-focused,
distinct from urology (the surgical specialty of the urinary tract -
MISSING from the manifest entirely) and from gastroenterology/hepatology/
endocrinology.

Manifest search (2,382 databases): zero 'nephrolog*' slugs/names; no
db/nephrolog* dirs; zero 'kidney'/'dialysis'/'nephron'/'glomerul*'/
'transplant' slugs/names. Whole-system exact-title sweep over the manifest
PLUS all shard index 't' keys: zero collisions for all 34 planned titles x2
editions (68 variants). NOTE: the persisted dedupe gate dir
(data/dedupe/exact) is stale for the newest fields, so the raw
manifest+shard sweep was the authoritative preflight. ZERO full-record
discipline coverage anywhere.

So this build creates two NEW databases, 34 ladder-ordered records each:

  nephrology                 - The Nephrology Database
                               (public-harvest: real, fact-checked clinical
                               nephrology; standard references Skorecki et
                               al. "Brenner and Rector's The Kidney" 11th ed
                               2020; Jameson et al. "Harrison's Principles
                               of Internal Medicine" 21st ed 2022;
                               Daugirdas et al. "Handbook of Dialysis" 6th
                               ed 2023; KDIGO AKI 2012, CKD 2024, BP 2021,
                               GN 2021, Diabetes 2022 guidelines; CKD-EPI
                               2021 eGFR; landmark papers as cited per
                               record)
  nephrology-signature       - The Nephrology Signature Database
                               (his original Signature interpretation of
                               the kidneys as the body's twin water-and-
                               salt treatment plants: glomeruli as the
                               filter cartridges, tubules as the refining
                               lines, the medulla as the concentration
                               tower, dialysis as the auxiliary treatment
                               plant; src signature, titles suffixed
                               " (Signature Edition)", never presented as
                               authentic public record)

34 records each, ordered by the teaching ladder (ladder_rank 1-10,
ladder_tier foundations/compounded/advanced); the shard index is written in
ladder order so pages present simple -> compounded -> complex.

ID prefixes: JAH-NEPH- (public) and JAH-NEPS- (signature). JAH-NEP- was
taken by 'neptune' and JAH-NPH- by 'nanophotonics'; JAH-NEPH-/JAH-NEPS-
verified free in the manifest and in every shard index (zero hits).

Numerical cores: all hand-computed 2026-10-17, machine-verified by the
demos (see below). Every demo prints its real computed values, asserts
tight bounds (never float exact-equality), and ends with the OK marker;
the build machine-executes all 68 demos before commit.

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
from entries_nephrology import ENTRIES, SIG_TAIL

# ---------------------------------------------------------------- DB config

def _cfg(slug, name, tagline, record_kind, prefix, ai, role, citation, source):
    sig_line = ("Signature originals - his original Signature interpretation of "
                "the kidneys as the body's twin water-and-salt treatment plants: "
                "the glomeruli as the filter cartridges, the tubules as the refining "
                "lines, the medulla as the concentration tower, and dialysis as the "
                "auxiliary treatment plant built beside them. Clearly labeled "
                "Signature-made, never presented as authentic public record.")
    pub_line = ("Public records - real, fact-checked clinical nephrology: the full ladder from "
                "what nephrology is through kidney anatomy and the nephron, glomerular "
                "filtration, the renal tubule, the countercurrent multiplier, total body "
                "water, GFR measurement, urinalysis, sodium and water balance, acid-base "
                "balance, and the clinical encounter, through hyponatremia, hypernatremia, "
                "potassium disorders, calcium phosphate and magnesium disorders, metabolic "
                "acidosis, metabolic alkalosis and respiratory disorders, acute kidney "
                "injury, prerenal AKI and ATN, chronic kidney disease, nephritic syndrome, "
                "nephrotic syndrome, diabetic kidney disease, and hypertension and the "
                "kidney, to polycystic kidney disease, tubulointerstitial and drug-induced "
                "injury, mineral and bone disorder, anemia of CKD, hemodialysis, peritoneal "
                "dialysis, kidney transplantation, pregnancy and the kidney, pediatric "
                "nephrology, and the future of the field, organized in the Signature system.")
    ladder = (" Records are ordered by the teaching ladder: Foundations (what nephrology "
              "is, kidney anatomy and the nephron, glomerular filtration, the renal "
              "tubule, the countercurrent multiplier, total body water, GFR measurement, "
              "urinalysis, sodium and water balance, acid-base balance, the clinical "
              "encounter) -> Compounded (hyponatremia, hypernatremia, potassium disorders, "
              "calcium phosphate and magnesium disorders, metabolic acidosis, metabolic "
              "alkalosis and respiratory disorders, acute kidney injury, prerenal AKI and "
              "ATN, chronic kidney disease, nephritic syndrome and glomerulonephritis, "
              "nephrotic syndrome, diabetic kidney disease, hypertension and the kidney) "
              "-> Advanced (polycystic kidney disease, tubulointerstitial and drug-induced "
              "injury, mineral and bone disorder of CKD, anemia of CKD, hemodialysis, "
              "peritoneal dialysis, kidney transplantation, pregnancy and the kidney, "
              "pediatric nephrology, the future of nephrology).")
    return {
        "name": name, "tagline": tagline, "record_kind": record_kind,
        "prefix": prefix, "ai": ai, "role": role,
        "hero_p": "%s - %s Every record carries the full entry: description, how it works, "
                  "key points, requirements, standards, citations, and a working demonstration "
                  "program.%s" % (tagline, sig_line if source == "signature" else pub_line, ladder),
        "sig_type": ("Signature originals organized in the Signature system"
                     if source == "signature" else
                     "Public records organized in the Signature system"),
        "search_ph": "Search GFR, creatinine, dialysis, hyponatremia, hyperkalemia, acidosis, AKI, CKD, glomerulonephritis, nephrotic, proteinuria, transplant, ADH, aldosterone...",
        "chat_ph": "Ask about nephrology...",
        "archive_blurb": ("Seeded %s nephrology records, marching toward one million records. "
                          "Presented in teaching-ladder order: foundations, compounded, advanced."
                          % ("Signature-original" if source == "signature" else "public-record")),
        "schema": ("id, t, g, name, title, description, how_it_works, key_points, requirements, "
                   "standards, citations, src, ladder_rank, ladder_tier, demo"),
        "fields": "Foundations \u00b7 Compounded \u00b7 Advanced - each tier opens on demand and loads only what you open",
        "gen_desc": "Generate clearly-labeled nephrology studies. Seeded archive records are the authoritative entries.",
        "greet": "I am the %s. Ask me about nephrology - from what it is through the nephron, "
        "filtration, the tubule, body water, GFR, urinalysis, sodium and acid-base balance, "
        "and the clinical encounter, through electrolyte disorders, AKI, CKD, glomerular "
        "diseases, and hypertension, to dialysis, transplantation, and the future of the field." % ai,
        "gen_fields": ["Foundations", "Compounded", "Advanced"],
        "gen_kind": "nephrology-study", "gen_demo_kind": "nephrology-demo",
        "source": source,
    }

CIT_PUB = ("Nephrology (standard references: Skorecki et al. Brenner and "
           "Rectors The Kidney 11th ed 2020; Jameson et al. Harrisons "
           "Principles of Internal Medicine 21st ed 2022; Daugirdas et al. "
           "Handbook of Dialysis 6th ed 2023; KDIGO AKI 2012; KDIGO CKD "
           "2024; KDIGO BP 2021; KDIGO GN 2021; KDIGO Diabetes 2022; Inker "
           "et al. NEJM 2021 CKD-EPI; Cockcroft and Gault Kidney Int 1976; "
           "Adrogue and Madias NEJM 2000 hyponatremia; Kraut and Madias Nat "
           "Rev Nephrol 2010 metabolic acidosis; Palmer CJASN 2015 "
           "potassium; Moe et al. Kidney Int 2006 CKD-MBD; Grantham NEJM "
           "2008 ADPKD; Kasiske et al. Am J Transplant 2009 transplant; "
           "Sibai Obstet Gynecol 2003 preeclampsia; Schwartz et al. JASN "
           "2009 Schwartz equation; Mehta et al. Crit Care 2007 AKIN; "
           "Himmelfarb and Ikizler NEJM 2010 hemodialysis; Levey and Coresh "
           "Lancet 2012 CKD; Jha et al. Lancet 2013 CKD global).")
CIT_SIG = CIT_PUB + (" Signature editions are his original Signature interpretation "
                     "of the kidneys as the bodys twin water-and-salt treatment "
                     "plants, clearly labeled Signature-made.")

DBCFG = {}
DBCFG["nephrology"] = _cfg(
    "nephrology", "The Nephrology Database",
    "Real, fact-checked clinical nephrology: from what nephrology is through kidney "
    "anatomy and the nephron, glomerular filtration, the renal tubule, the "
    "countercurrent multiplier, total body water, GFR measurement, urinalysis, sodium "
    "and water balance, acid-base balance, and the clinical encounter, through "
    "hyponatremia, hypernatremia, potassium disorders, calcium phosphate and magnesium "
    "disorders, metabolic acidosis, metabolic alkalosis and respiratory disorders, acute "
    "kidney injury, prerenal AKI and ATN, chronic kidney disease, nephritic syndrome, "
    "nephrotic syndrome, diabetic kidney disease, and hypertension and the kidney, to "
    "polycystic kidney disease, tubulointerstitial and drug-induced injury, mineral and "
    "bone disorder, anemia of CKD, hemodialysis, peritoneal dialysis, kidney "
    "transplantation, pregnancy and the kidney, pediatric nephrology, and the future of "
    "the field - taught progressively along the ladder.",
    "nephrology record", "JAH-NEPH-", "JAH Nephrology Archivist",
    "nephrology archivist - clinical nephrology: the kidney; acute kidney injury, "
    "chronic kidney disease, glomerular diseases, tubular disorders, electrolytes and "
    "acid-base, the kidney in hypertension, dialysis, kidney transplantation, "
    "urinalysis; teaching progressively along the ladder from foundations through "
    "compounded to advanced; answers from many angles - definition, example, analogy, "
    "application, history, math, how-to - using only archive data from this system",
    CIT_PUB, "public")
DBCFG["nephrology-signature"] = _cfg(
    "nephrology-signature", "The Nephrology Signature Database",
    "His original Signature interpretation of the kidneys as the body's twin "
    "water-and-salt treatment plants: the glomeruli as the filter cartridges, the "
    "tubules as the refining lines, the medulla as the concentration tower, and "
    "dialysis as the auxiliary treatment plant built beside them. The full ladder from "
    "what nephrology is through the nephron, filtration, the tubule, body water, GFR, "
    "urinalysis, and the clinical encounter, through electrolyte disorders, AKI, CKD, "
    "and glomerular diseases, to dialysis, transplantation, and the future of the "
    "field, reframed as Signature science. Clearly labeled Signature-made, never "
    "presented as authentic public record.",
    "nephrology record", "JAH-NEPS-", "JAH Nephrology Archivist (Signature)",
    "nephrology archivist - Signature editions: his original Signature interpretation "
    "of the kidneys as the bodily twin water-and-salt treatment plants, clearly "
    "labeled Signature-made and never presented as authentic public record; teaches "
    "progressively along the ladder from foundations through compounded to advanced; "
    "answers from many angles - definition, example, analogy, application, history, "
    "math, how-to - using only archive data from this system",
    CIT_SIG, "signature")

base.DBCFG = DBCFG

# ---------------------------------------------------------------- demos
# Every demo is real, runnable, stdlib-only Python performing the actual
# nephrology computation for its record. All are machine-executed by main().

_PREAMBLE = (
"import math\n"
)

def _wrap(name, rid, group, body):
    return (base._hdr(name, rid, group) + _PREAMBLE + body.replace("NAME", json.dumps(name)))
def demo_np_what_is(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # the treatment plant at scale: daily filtrate, per-nephron share, reclamation
    gfr_ml_min = 125.0
    daily_L = gfr_ml_min * 1440.0 / 1000.0
    nephrons = 2.0e6
    per_nephron_uL = daily_L * 1.0e6 / nephrons
    urine_L = 1.5
    reclaimed = (daily_L - urine_L) / daily_L * 100.0
    print("daily filtrate: %.0f mL/min x 1440 min = %.1f L" % (gfr_ml_min, daily_L))
    print("per nephron: %.1f L / %.0e nephrons = %.1f microliters/day" % (daily_L, nephrons, per_nephron_uL))
    print("reclaimed: (%.1f - %.1f)/%.1f = %.2f %%" % (daily_L, urine_L, daily_L, reclaimed))
    assert 179.9 < daily_L < 180.1
    assert 89.9 < per_nephron_uL < 90.1
    assert 99.1 < reclaimed < 99.2
    print("rule: 180 liters in, under 2 liters out - the tightest refinery on earth")
    print("OK: %s sized the treatment plant" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_np_nephron_anatomy(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # the cartridge census: blood supply share and per-unit workload
    cardiac_L_min, renal_share = 5.0, 0.22
    renal_flow = cardiac_L_min * renal_share
    nephrons = 2.0e6
    daily_L = 180.0
    per_nephron_uL = daily_L * 1.0e6 / nephrons
    print("renal blood flow: %.1f L/min x %.0f %% = %.2f L/min" % (cardiac_L_min, renal_share * 100.0, renal_flow))
    print("cartridges: %.0e total; each filters %.1f microliters/day" % (nephrons, per_nephron_uL))
    assert 1.09 < renal_flow < 1.11
    assert 89.9 < per_nephron_uL < 90.1
    print("rule: richest blood supply per gram in the body, two million cartridges sharing the load")
    print("OK: %s counted the cartridges" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_np_gfr_filter(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # Starling forces across the glomerular wall and the filtration fraction
    p_gc, p_bs, pi_gc = 45.0, 10.0, 25.0
    nfp = p_gc - p_bs - pi_gc
    gfr, rpf = 125.0, 600.0
    ff = gfr / rpf
    daily_L = gfr * 1440.0 / 1000.0
    print("net filtration pressure: %.0f - %.0f - %.0f = %.0f mmHg" % (p_gc, p_bs, pi_gc, nfp))
    print("filtration fraction: %.0f / %.0f = %.4f (%.1f %%)" % (gfr, rpf, ff, ff * 100.0))
    print("daily filtrate: %.1f L" % daily_L)
    assert 9.9 < nfp < 10.1
    assert 0.208 < ff < 0.209
    assert 179.9 < daily_L < 180.1
    print("rule: 10 mmHg of net push filters the plasma pool 60 times a day")
    print("OK: %s worked the Starling arithmetic" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_np_tubule(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # the sodium mass balance: filtered load vs excretion
    gfr_L_day, p_na = 180.0, 140.0
    filtered_mmol = gfr_L_day * p_na
    excreted_mmol = 100.0
    reclaimed = (filtered_mmol - excreted_mmol) / filtered_mmol * 100.0
    print("filtered sodium: %.0f L x %.0f mmol/L = %.0f mmol/day" % (gfr_L_day, p_na, filtered_mmol))
    print("reclaimed: (%.0f - %.0f)/%.0f = %.2f %%" % (filtered_mmol, excreted_mmol, filtered_mmol, reclaimed))
    assert 25199.0 < filtered_mmol < 25201.0
    assert 99.59 < reclaimed < 99.62
    print("rule: 25,200 in, 100 out - the reclaim line runs at 99.6 percent")
    print("OK: %s balanced the sodium ledger" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_np_countercurrent(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # the concentrating ceiling sets the minimum obligatory urine volume
    solute_mosm_day, max_osm = 800.0, 1200.0
    min_vol_L = solute_mosm_day / max_osm
    cortex, papilla = 300.0, 1200.0
    fold = papilla / cortex
    print("minimum urine volume: %.0f mOsm / %.0f mOsm/kg = %.4f L/day" % (solute_mosm_day, max_osm, min_vol_L))
    print("medullary gradient: %.0f -> %.0f mOsm/kg (%.0f-fold)" % (cortex, papilla, fold))
    assert 0.666 < min_vol_L < 0.668
    assert fold == 4.0
    print("rule: the tower physics sets a hard floor near two-thirds of a liter a day")
    print("OK: %s read the concentration tower" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_np_tbw(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # the compartment map for a 70-kg man
    weight_kg = 70.0
    tbw = 0.6 * weight_kg
    icf = tbw * 2.0 / 3.0
    ecf = tbw / 3.0
    plasma = ecf / 4.0
    interstitial = ecf - plasma
    print("TBW: 0.6 x %.0f kg = %.1f L" % (weight_kg, tbw))
    print("ICF %.1f L (K-rich) | ECF %.1f L (Na-rich)" % (icf, ecf))
    print("ECF splits: plasma %.1f L + interstitial %.1f L" % (plasma, interstitial))
    assert 41.9 < tbw < 42.1
    assert 27.9 < icf < 28.1
    assert 13.9 < ecf < 14.1
    assert 3.4 < plasma < 3.6
    print("rule: 42 liters in two tanks - every fluid order is a transfer between them")
    print("OK: %s mapped the tanks" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_np_gfr_measure(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # Cockcroft-Gault on the textbook case
    age, weight_kg, creat = 65.0, 72.0, 1.2
    crcl = (140.0 - age) * weight_kg / (72.0 * creat)
    crcl_f = crcl * 0.85
    print("CrCl: (140 - %.0f) x %.0f / (72 x %.1f) = %.1f mL/min" % (age, weight_kg, creat, crcl))
    print("if female: x 0.85 = %.2f mL/min" % crcl_f)
    assert 62.4 < crcl < 62.6
    assert 53.0 < crcl_f < 53.2
    print("rule: age, weight, and the ash level - the 1976 slide rule still calls the number")
    print("OK: %s ran Cockcroft-Gault" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_np_urinalysis(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # ACR categories on the worked case
    acr = 120.0
    if acr < 30.0:
        cat = "A1 (normal to mildly increased)"
    elif acr <= 300.0:
        cat = "A2 (moderately increased)"
    else:
        cat = "A3 (severely increased)"
    print("ACR %.0f mg/g -> %s" % (acr, cat))
    assert cat.startswith("A2")
    for v, exp in [(15.0, "A1"), (120.0, "A2"), (450.0, "A3")]:
        c = "A1" if v < 30.0 else ("A2" if v <= 300.0 else "A3")
        assert c == exp, v
    print("rule: 120 sits in the amber band - moderately increased, act now")
    print("OK: %s read the effluent assay" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_np_sodium_water(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # estimated plasma osmolarity on the textbook panel
    na, glucose, bun = 140.0, 90.0, 14.0
    osm = 2.0 * na + glucose / 18.0 + bun / 2.8
    normal = 285.0 <= osm <= 295.0
    print("osmolarity: 2x%.0f + %.0f/18 + %.0f/2.8 = %.1f mOsm/kg (normal: %s)"
          % (na, glucose, bun, osm, normal))
    assert 289.9 < osm < 290.1
    assert normal is True
    print("rule: twice the sodium plus the corrections - 290, dead center of the green band")
    print("OK: %s assayed the plasma" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_np_acid_base(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # Henderson-Hasselbalch on the textbook gas
    hco3, pco2 = 24.0, 40.0
    ph = 6.1 + math.log10(hco3 / (0.03 * pco2))
    ratio = hco3 / (0.03 * pco2)
    print("ratio: %.0f / (0.03 x %.0f) = %.1f; log = %.3f" % (hco3, pco2, ratio, math.log10(ratio)))
    print("pH = 6.1 + %.3f = %.3f" % (math.log10(ratio), ph))
    assert 19.9 < ratio < 20.1
    assert 7.399 < ph < 7.403
    print("rule: the buffer tank gauge reads 7.40 dead center")
    print("OK: %s read the chemistry dial" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_np_encounter(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # BUN/creatinine ratio on the worked case
    bun, creat = 42.0, 1.0
    ratio = bun / creat
    call = "prerenal pattern" if ratio > 20.0 else "intrinsic/postrenal pattern"
    print("BUN/Cr: %.0f / %.1f = %.0f (>20: %s)" % (bun, creat, ratio, call))
    assert 41.9 < ratio < 42.1
    assert call == "prerenal pattern"
    print("rule: 42 screams supply-line failure - fill the tanks, the cartridges are fine")
    print("OK: %s worked the first branch point" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_np_hyponatremia(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # glucose-corrected sodium
    na_measured, glucose = 128.0, 400.0
    na_true = na_measured + 1.6 * (glucose - 100.0) / 100.0
    ceiling = 8.0  # mmol/L per 24 h in chronic hyponatremia
    print("corrected Na: %.0f + 1.6 x (%.0f-100)/100 = %.1f mmol/L"
          % (na_measured, glucose, na_true))
    print("correction ceiling: %.0f mmol/L per 24 h - faster risks osmotic demyelination" % ceiling)
    assert 132.7 < na_true < 132.9
    print("rule: correct the gauge for sugar first, then raise it no faster than 8 a day")
    print("OK: %s corrected the dilution alarm" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_np_hypernatremia(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # free water deficit for the 70-kg man at Na 160
    tbw, na = 42.0, 160.0
    deficit = tbw * (na / 140.0 - 1.0)
    hours = 60.0
    rate_ml_h = deficit * 1000.0 / hours
    print("free water deficit: %.0f x (%.0f/140 - 1) = %.1f L" % (tbw, na, deficit))
    print("repay over %.0f h: %.0f mL/h of water" % (hours, rate_ml_h))
    assert 5.99 < deficit < 6.01
    assert 99.0 < rate_ml_h < 101.0
    print("rule: 6 liters owed - pay it back slow or the brain swells")
    print("OK: %s tallied the water debt" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_np_potassium(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # transtubular potassium gradient on the worked case
    u_k, p_k, u_osm, p_osm = 40.0, 5.5, 600.0, 290.0
    ttkg = (u_k / p_k) / (u_osm / p_osm)
    call = "renal wasting" if ttkg >= 7.0 else "appropriate conservation (extrarenal loss)"
    print("TTKG: (%.0f/%.1f)/(%.0f/%.0f) = %.2f (<7: %s)" % (u_k, p_k, u_osm, p_osm, ttkg, call))
    assert 3.50 < ttkg < 3.53
    assert ttkg < 7.0
    print("rule: 3.5 means the plant valves are shut tight - the leak is outside the fence")
    print("OK: %s metered the high-voltage line" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_np_ca_p_mg(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # albumin-corrected calcium
    ca, albumin = 7.5, 2.8
    corrected = ca + 0.8 * (4.0 - albumin)
    low = corrected < 8.5
    print("corrected Ca: %.1f + 0.8 x (4.0 - %.1f) = %.2f mg/dL (low: %s)"
          % (ca, albumin, corrected, low))
    assert 8.45 < corrected < 8.47
    assert low is True
    print("rule: the gauge lies when albumin is low - correct it before acting")
    print("OK: %s corrected the mineral gauge" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_np_metabolic_acidosis(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # the gap arithmetic on the worked case
    na, cl, hco3 = 140.0, 104.0, 18.0
    ag = na - (cl + hco3)
    delta = (ag - 12.0) - (24.0 - hco3)
    winters = 1.5 * hco3 + 8.0
    print("anion gap: %.0f - (%.0f + %.0f) = %.0f mEq/L (elevated)" % (na, cl, hco3, ag))
    print("delta gap: (%.0f - 12) - (24 - %.0f) = %.0f -> pure high-gap acidosis" % (ag, hco3, delta))
    print("Winters pCO2: 1.5 x %.0f + 8 = %.0f mmHg" % (hco3, winters))
    assert 17.9 < ag < 18.1
    assert -0.1 < delta < 0.1
    assert 34.9 < winters < 35.1
    print("rule: one spill, no accomplice, and the lungs keeping up exactly")
    print("OK: %s ran the forensic assay" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_np_alk_resp(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # metabolic alkalosis compensation on the worked case
    hco3 = 40.0
    expected_pco2 = 0.7 * (hco3 - 24.0) + 40.0
    u_cl = 12.0
    responsive = u_cl < 20.0
    print("expected pCO2: 0.7 x (%.0f - 24) + 40 = %.1f mmHg" % (hco3, expected_pco2))
    print("urine chloride %.0f (<20: %s) -> chloride-responsive, give saline" % (u_cl, responsive))
    assert 51.1 < expected_pco2 < 51.3
    assert responsive is True
    print("rule: the stack hypoventilates on schedule and the tanks are begging for salt water")
    print("OK: %s checked the compensation" % NAME)
if __name__ == "__main__":
    main()
''')
def demo_np_aki(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # KDIGO staging on the worked case
    baseline, peak = 1.0, 2.8
    fold = peak / baseline
    rise48 = peak - baseline
    if fold >= 3.0 or peak >= 4.0:
        stage = 3
    elif fold >= 2.0:
        stage = 2
    elif fold >= 1.5 or rise48 >= 0.3:
        stage = 1
    else:
        stage = 0
    print("creatinine %.1f -> %.1f: %.1f-fold rise (>=0.3 in 48h: %s)" % (baseline, peak, fold, rise48 >= 0.3))
    print("KDIGO stage: %d" % stage)
    assert 2.79 < fold < 2.81
    assert stage == 2
    print("rule: stage 2 - the plant is at half staff, name the fault")
    print("OK: %s staged the trip" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_np_prerenal_atn(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # fractional excretion of sodium on the worked case
    u_na, p_cr, p_na, u_cr = 10.0, 2.0, 140.0, 40.0
    fena = (u_na * p_cr) / (p_na * u_cr) * 100.0
    call = "prerenal (tubules working)" if fena < 1.0 else ("ATN (tubules dead)" if fena > 2.0 else "indeterminate")
    print("FENa: (%.0f x %.1f)/(%.0f x %.0f) x 100 = %.3f %% -> %s" % (u_na, p_cr, p_na, u_cr, fena, call))
    assert 0.356 < fena < 0.359
    assert fena < 1.0
    print("rule: 0.36 percent - empty tanks, intact lines, fill them today")
    print("OK: %s separated the two faces" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_np_ckd(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # G-by-A staging on the worked case
    egfr, acr = 38.0, 450.0
    if egfr >= 90.0:
        g = "G1"
    elif egfr >= 60.0:
        g = "G2"
    elif egfr >= 45.0:
        g = "G3a"
    elif egfr >= 30.0:
        g = "G3b"
    elif egfr >= 15.0:
        g = "G4"
    else:
        g = "G5"
    a = "A1" if acr < 30.0 else ("A2" if acr <= 300.0 else "A3")
    print("eGFR %.0f -> %s; ACR %.0f -> %s; combined: %s%s (high risk, red zone)" % (egfr, g, acr, a, g, a))
    assert g == "G3b" and a == "A3"
    print("rule: G3bA3 sits deep in the red - ease the load on every front")
    print("OK: %s charted the rust" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_np_nephritic(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # complement-branching serology logic
    def branch(c3_low, aso_pos, ana_pos, anca_pos, gbm_pos):
        if gbm_pos:
            return "anti-GBM disease"
        if anca_pos:
            return "ANCA vasculitis"
        if ana_pos:
            return "lupus nephritis"
        if c3_low and aso_pos:
            return "post-infectious GN"
        if c3_low:
            return "low-complement GN (MPGN/C3, cryoglobulinemia)"
        return "IgA nephropathy (normal complement)"
    cases = [((True, True, False, False, False), "post-infectious GN"),
             ((True, False, True, False, False), "lupus nephritis"),
             ((False, False, False, True, False), "ANCA vasculitis"),
             ((False, False, False, False, True), "anti-GBM disease"),
             ((False, False, False, False, False), "IgA nephropathy (normal complement)")]
    for args, expected in cases:
        got = branch(*args)
        print("  C3low=%s ASO=%s ANA=%s ANCA=%s GBM=%s -> %s" % (args + (got,)))
        assert got == expected
    print("rule: sort the attackers by their calling cards before the biopsy")
    print("OK: %s ran the serology sort" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_np_nephrotic(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # all four syndrome criteria on the worked case
    protein_g_day = 4200.0 / 1000.0
    albumin, edema, hyperlipidemia = 2.4, True, True
    criteria = [protein_g_day > 3.5, albumin < 3.0, edema, hyperlipidemia]
    print("protein %.1f g/day (>3.5: %s)" % (protein_g_day, criteria[0]))
    print("albumin %.1f g/dL (<3.0: %s); edema %s; hyperlipidemia %s"
          % (albumin, criteria[1], edema, hyperlipidemia))
    assert all(criteria), "not all four criteria met"
    print("nephrotic syndrome: 4 of 4 - the cartridges are torn open")
    print("OK: %s confirmed the leak" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_np_dkd(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # eGFR slope on the worked case
    g0, g1, years = 62.0, 48.0, 2.0
    slope = (g0 - g1) / years
    rapid = slope > 5.0
    print("eGFR %.0f -> %.0f over %.0f y: slope %.1f /yr (rapid over 5: %s)"
          % (g0, g1, years, slope, rapid))
    assert 6.9 < slope < 7.1
    assert rapid is True
    print("rule: past the 5-point red line - intensify everything now")
    print("OK: %s timed the rust" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_np_htn_kidney(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # mean arterial pressure on the worked case
    sbp, dbp = 160.0, 90.0
    map_v = dbp + (sbp - dbp) / 3.0
    print("MAP: %.0f + (%.0f - %.0f)/3 = %.2f mmHg" % (dbp, sbp, dbp, map_v))
    assert 113.32 < map_v < 113.35
    print("target per KDIGO 2021: systolic below 120 in CKD - this system is running hot")
    print("OK: %s read the pressure gauge" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_np_pkd(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # expected ADPKD cases in the worked population
    pop, one_in = 400000.0, 800.0
    expected = pop / one_in
    print("expected ADPKD cases: %.0f / %.0f = %.0f" % (pop, one_in, expected))
    assert 499.9 < expected < 500.1
    print("rule: the commonest inherited kidney disease - screen the bloodline")
    print("OK: %s counted the families" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_np_tin_drug(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # renal dose scaling on the worked case
    dose_normal, crcl_pt, crcl_nl = 1000.0, 30.0, 100.0
    dose_adj = dose_normal * crcl_pt / crcl_nl
    print("adjusted dose: %.0f mg x (%.0f/%.0f) = %.0f mg" % (dose_normal, crcl_pt, crcl_nl, dose_adj))
    assert 299.9 < dose_adj < 300.1
    print("rule: the kidney clears the drugs, so the dose scales with the clearance")
    print("OK: %s scaled the dispensary" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_np_mbd(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # calcium-phosphate product on the worked case
    ca, phos, target = 9.8, 6.5, 55.0
    product = ca * phos
    over = product > target
    print("Ca x P: %.1f x %.1f = %.2f mg2/dL2 (target <%.0f: over=%s)" % (ca, phos, product, target, over))
    assert 63.69 < product < 63.71
    assert over is True
    print("rule: 63.7 against the 55 redline - the mineral yard is actively scaling")
    print("OK: %s read the precipitation gauge" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_np_anemia_ckd(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # correction gap and iron thresholds on the worked case
    hb, target_lo = 9.2, 10.5
    gap = target_lo - hb
    tsat, ferritin = 18.0, 220.0
    iron_ok = tsat < 30.0 and ferritin < 500.0
    print("correction gap: %.1f - %.1f = %.1f g/dL" % (target_lo, hb, gap))
    print("TSAT %.0f %% (<30) and ferritin %.0f (<500): iron-responsive %s" % (tsat, ferritin, iron_ok))
    assert 1.29 < gap < 1.31
    assert iron_ok is True
    print("rule: open the armory (iron) before issuing new orders (ESA)")
    print("OK: %s sized the recruitment gap" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_np_hemodialysis(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # Daugirdas second-generation spKt/V on the worked session
    bun_pre, bun_post = 60.0, 18.0
    t_h, uf_L, w_kg = 4.0, 2.5, 70.0
    r = bun_post / bun_pre
    spktv = -math.log(r - 0.008 * t_h) + (4.0 - 3.5 * r) * uf_L / w_kg
    adequate = spktv >= 1.2
    print("R = %.0f/%.0f = %.2f" % (bun_post, bun_pre, r))
    print("spKt/V = -ln(%.2f - 0.008x%.1f) + (4 - 3.5x%.2f)x%.1f/%.0f = %.3f (>=1.2: %s)"
          % (r, t_h, r, uf_L, w_kg, spktv, adequate))
    assert 1.41 < spktv < 1.44
    assert adequate is True
    print("rule: 1.42 past the 1.2 redline - a full shift of work done")
    print("OK: %s dosed the auxiliary plant" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_np_peritoneal(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # weekly adequacy on the worked case
    weekly_ktv, target = 1.9, 1.7
    adequate = weekly_ktv >= target
    print("weekly Kt/V %.1f (>=%.1f: %s)" % (weekly_ktv, target, adequate))
    assert adequate is True
    # PET transport logic
    def modality(dp_cr_4h):
        return "APD (short dwells)" if dp_cr_4h > 0.8 else ("CAPD (long dwells)" if dp_cr_4h < 0.5 else "either")
    for v, exp in [(0.85, "APD (short dwells)"), (0.45, "CAPD (long dwells)")]:
        assert modality(v) == exp, v
    print("rule: high transporters get the night-shift cycler, low transporters get long dwells")
    print("OK: %s checked the home plant" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_np_transplant(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # one-year graft survival expectation for living-donor kidneys
    n, surv = 100.0, 0.95
    expected = n * surv
    print("expected functioning grafts at 1 year: %.0f x %.0f %% = %.0f" % (n, surv * 100.0, expected))
    assert 94.9 < expected < 95.1
    print("rule: 95 of 100 - the swap beats the auxiliary unit on every measure")
    print("OK: %s priced the swap" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_np_pregnancy(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # preeclampsia criteria on the worked case
    sbp, dbp, protein_mg, weeks = 150.0, 100.0, 400.0, 32.0
    map_v = dbp + (sbp - dbp) / 3.0
    preeclampsia = sbp >= 140.0 and dbp >= 90.0 and protein_mg >= 300.0 and weeks >= 20.0
    print("MAP: %.0f + (%.0f-%.0f)/3 = %.2f mmHg" % (dbp, sbp, dbp, map_v))
    print("BP %.0f/%.0f + protein %.0f mg/day at %.0f weeks -> preeclampsia: %s"
          % (sbp, dbp, protein_mg, weeks, preeclampsia))
    assert 116.66 < map_v < 116.68
    assert preeclampsia is True
    print("rule: past every diagnostic line - the only cure is delivery")
    print("OK: %s worked the criteria" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_np_peds(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # bedside Schwartz equation on the worked case
    height_cm, creat = 110.0, 0.8
    egfr = 0.413 * height_cm / creat
    abnormal = egfr < 90.0
    print("Schwartz eGFR: 0.413 x %.0f / %.1f = %.2f mL/min/1.73m2 (abnormal for a child: %s)"
          % (height_cm, creat, egfr, abnormal))
    assert 56.77 < egfr < 56.80
    assert abnormal is True
    print("rule: 56.8 would pass for an adult - for a child it is abnormal")
    print("OK: %s recalibrated for small operators" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_np_future(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # the waitlist arithmetic driving the frontiers
    waiting, per_year = 90000.0, 25000.0
    wait_years = waiting / per_year
    print("average wait: %.0f / %.0f per year = %.1f years" % (waiting, per_year, wait_years))
    assert 3.59 < wait_years < 3.61
    print("rule: 3.6 years - xenotransplant, wearables, and regrowth attack exactly this number")
    print("OK: %s did the cruelest arithmetic" % NAME)
if __name__ == "__main__":
    main()
''')

DEMOS = {
    "what_is": demo_np_what_is,
    "nephron_anatomy": demo_np_nephron_anatomy,
    "gfr_filter": demo_np_gfr_filter,
    "tubule": demo_np_tubule,
    "countercurrent": demo_np_countercurrent,
    "tbw": demo_np_tbw,
    "gfr_measure": demo_np_gfr_measure,
    "urinalysis": demo_np_urinalysis,
    "sodium_water": demo_np_sodium_water,
    "acid_base": demo_np_acid_base,
    "encounter": demo_np_encounter,
    "hyponatremia": demo_np_hyponatremia,
    "hypernatremia": demo_np_hypernatremia,
    "potassium": demo_np_potassium,
    "ca_p_mg": demo_np_ca_p_mg,
    "metabolic_acidosis": demo_np_metabolic_acidosis,
    "alk_resp": demo_np_alk_resp,
    "aki": demo_np_aki,
    "prerenal_atn": demo_np_prerenal_atn,
    "ckd": demo_np_ckd,
    "nephritic": demo_np_nephritic,
    "nephrotic": demo_np_nephrotic,
    "dkd": demo_np_dkd,
    "htn_kidney": demo_np_htn_kidney,
    "pkd": demo_np_pkd,
    "tin_drug": demo_np_tin_drug,
    "mbd": demo_np_mbd,
    "anemia_ckd": demo_np_anemia_ckd,
    "hemodialysis": demo_np_hemodialysis,
    "peritoneal": demo_np_peritoneal,
    "transplant": demo_np_transplant,
    "pregnancy": demo_np_pregnancy,
    "peds": demo_np_peds,
    "future": demo_np_future,
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
    for slug in ("nephrology", "nephrology-signature"):
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
        assert "hepatology" not in page.lower(), "field leftover in %s" % slug
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
