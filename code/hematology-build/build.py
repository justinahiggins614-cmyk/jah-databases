#!/usr/bin/env python3
"""Build the Hematology field databases for JAH Databases (field #40, taxonomy order).

Verified 2026-10-17 (see entries_hematology.py docstring): NO database
covers hematology as a clinical specialty (blood and blood-forming organs;
anemias, hemoglobinopathies, leukemias, lymphomas, myeloma, bleeding and
clotting disorders, transfusion medicine, bone marrow, CBC interpretation,
the coagulation cascade). Clinical-specialty framing, blood-focused,
distinct from oncology (general cancer) and immunology (the immune system).

Manifest search (2,380 databases): zero 'hematolog*' slugs/names; no
db/hematolog* dirs. Whole-system exact-title sweep over the manifest PLUS
all 779 shard index 't' keys (1,130,197 rows): zero collisions for all 34
planned titles x2 editions (68 variants). Near-neighbors confirmed
different disciplines: 'medical-diagnostics-study' holds only formulaic
"Signature Study of Hematology testing: ..." study-format records (study
methodology, not the clinical specialty); 'oncology' covers general
cancer; 'immunology' covers the immune system. ZERO full-record discipline
coverage anywhere.

So this build creates two NEW databases, 34 ladder-ordered records each:

  hematology                 - The Hematology Database
                               (public-harvest: real, fact-checked clinical
                               hematology; standard references Kaushansky et
                               al. "Williams Hematology" 10th ed 2021;
                               Hoffman et al. "Hematology: Basic Principles
                               and Practice" 8th ed 2023; Hoffbrand and Moss
                               "Hoffbrand's Essential Haematology" 8th ed
                               2019; Jameson et al. "Harrison's Principles
                               of Internal Medicine" 21st ed 2022; ASH, WFH,
                               ELN, IMWG, ESMO, AABB, CHEST guidelines and
                               landmark papers as cited per record)
  hematology-signature       - The Hematology Signature Database
                               (his original Signature interpretation of
                               blood as the body's freight and supply line:
                               red cells as the oxygen freight fleet, white
                               cells as the patrol fleet, platelets as the
                               rapid-repair crews, plasma as the river they
                               sail, the marrow as the shipyard; src
                               signature, titles suffixed
                               " (Signature Edition)", never presented as
                               authentic public record)

34 records each, ordered by the teaching ladder (ladder_rank 1-10,
ladder_tier foundations/compounded/advanced); the shard index is written in
ladder order so pages present simple -> compounded -> complex.

ID prefixes: JAH-HEM- (public) and JAH-HEMS- (signature), both verified free
in the manifest and in every shard index (zero hits).

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
from entries_hematology import ENTRIES, SIG_TAIL

# ---------------------------------------------------------------- DB config

def _cfg(slug, name, tagline, record_kind, prefix, ai, role, citation, source):
    sig_line = ("Signature originals - his original Signature interpretation of "
                "blood as the body's freight and supply line: red cells as the "
                "oxygen freight fleet, white cells as the patrol fleet, platelets "
                "as the rapid-repair crews, plasma as the river they sail, and "
                "the marrow as the shipyard that builds them all. Clearly labeled "
                "Signature-made, never presented as authentic public record.")
    pub_line = ("Public records - real, fact-checked clinical hematology: the full ladder from "
                "what hematology is through blood composition and hematopoiesis, the CBC, "
                "hemoglobin physiology, the bone marrow, iron B12 and folate supply lines, "
                "white cells and the differential, and the clinical encounter, through "
                "iron deficiency, B12 and folate deficiency, anemia of inflammation, "
                "hemolytic anemia, thalassemia, sickle cell disease, aplastic anemia, "
                "myelodysplastic syndromes, ITP, the coagulation cascade, hemophilia "
                "and von Willebrand disease, and venous thromboembolism, to acute and "
                "chronic leukemia, lymphoma, multiple myeloma, myeloproliferative "
                "neoplasms, DIC, transfusion medicine, transfusion reactions, stem cell "
                "transplantation, antithrombotic therapy, antiphospholipid syndrome and "
                "HIT, pediatric hematology, pregnancy and blood, and the future of the "
                "field, organized in the Signature system.")
    ladder = (" Records are ordered by the teaching ladder: Foundations (what hematology "
              "is, blood composition and hematopoiesis, the CBC, hemoglobin and red cell "
              "physiology, the bone marrow, iron B12 and folate supply lines, white "
              "blood cells and the differential, the clinical encounter) -> "
              "Compounded (iron deficiency anemia, B12 and folate deficiency, anemia of "
              "inflammation, hemolytic anemia, thalassemia, sickle cell disease, "
              "aplastic anemia, myelodysplastic syndromes, immune thrombocytopenia, "
              "the coagulation cascade, hemophilia and von Willebrand disease, venous "
              "thromboembolism and thrombophilia) -> Advanced (acute leukemia, chronic "
              "leukemias, lymphoma, multiple myeloma, myeloproliferative neoplasms, "
              "DIC, transfusion medicine, transfusion reactions, stem cell "
              "transplantation, anticoagulant and antiplatelet therapy, "
              "antiphospholipid syndrome and heparin-induced thrombocytopenia, "
              "pediatric hematology, pregnancy and blood, the future of hematology).")
    return {
        "name": name, "tagline": tagline, "record_kind": record_kind,
        "prefix": prefix, "ai": ai, "role": role,
        "hero_p": "%s - %s Every record carries the full entry: description, how it works, "
                  "key points, requirements, standards, citations, and a working demonstration "
                  "program.%s" % (tagline, sig_line if source == "signature" else pub_line, ladder),
        "sig_type": ("Signature originals organized in the Signature system"
                     if source == "signature" else
                     "Public records organized in the Signature system"),
        "search_ph": "Search anemia, sickle cell, leukemia, lymphoma, myeloma, ITP, hemophilia, DIC, transfusion, CBC, MCV, INR, marrow, platelets, clotting...",
        "chat_ph": "Ask about hematology...",
        "archive_blurb": ("Seeded %s hematology records, marching toward one million records. "
                          "Presented in teaching-ladder order: foundations, compounded, advanced."
                          % ("Signature-original" if source == "signature" else "public-record")),
        "schema": ("id, t, g, name, title, description, how_it_works, key_points, requirements, "
                   "standards, citations, src, ladder_rank, ladder_tier, demo"),
        "fields": "Foundations \u00b7 Compounded \u00b7 Advanced - each tier opens on demand and loads only what you open",
        "gen_desc": "Generate clearly-labeled hematology studies. Seeded archive records are the authoritative entries.",
        "greet": "I am the %s. Ask me about hematology - from what it is through blood composition, "
        "the CBC, hemoglobin, the marrow, and the clinical encounter, through anemias, clotting "
        "disorders, and transfusion medicine, to leukemias, lymphomas, myeloma, stem cell "
        "transplantation, and the future of the field." % ai,
        "gen_fields": ["Foundations", "Compounded", "Advanced"],
        "gen_kind": "hematology-study", "gen_demo_kind": "hematology-demo",
        "source": source,
    }

CIT_PUB = ("Hematology (standard references: Kaushansky et al. Williams Hematology "
           "10th ed 2021; Hoffman et al. Hematology: Basic Principles and Practice "
           "8th ed 2023; Hoffbrand and Moss Hoffbrands Essential Haematology 8th ed "
           "2019; Jameson et al. Harrisons Principles of Internal Medicine 21st ed "
           "2022; Camaschella Blood 2019 iron deficiency; Green Blood 2017 B12 "
           "deficiency; Weiss et al. Blood 2019 anemia of inflammation; Piel et al. "
           "NEJM 2017 sickle cell disease; Taher et al. Lancet 2018 thalassaemia; "
           "Killick et al. Br J Haematol 2016 aplastic anaemia; Greenberg et al. "
           "Blood 2012 IPSS-R; Neunert et al. ASH 2019 ITP; Srivastava et al. WFH "
           "2020 hemophilia; James et al. ASH ISTH NHF WFH 2021 VWD; Stevens et al. "
           "CHEST 2021 VTE; Dohner et al. ELN 2022 AML; Hochhaus et al. ELN 2020 "
           "CML; Hallek et al. iwCLL 2018; Rajkumar et al. IMWG 2014 myeloma; "
           "Eichenauer et al. ESMO 2018 Hodgkin lymphoma; Tefferi and Barbui Am J "
           "Hematol 2020 MPN; Levi et al. Br J Haematol 2009 DIC; Carson et al. "
           "JAMA 2023 AABB transfusion; Majhail et al. 2015 transplant indications; "
           "Cuker et al. ASH 2018 HIT; Maude et al. NEJM 2018 CAR-T).")
CIT_SIG = CIT_PUB + (" Signature editions are his original Signature interpretation "
                     "of blood as the body's freight and supply line, clearly labeled "
                     "Signature-made.")

DBCFG = {}
DBCFG["hematology"] = _cfg(
    "hematology", "The Hematology Database",
    "Real, fact-checked clinical hematology: from what hematology is through blood "
    "composition and hematopoiesis, the CBC, hemoglobin physiology, the bone marrow, "
    "iron B12 and folate supply lines, white cells and the differential, and the "
    "clinical encounter, through iron deficiency, B12 and folate deficiency, anemia "
    "of inflammation, hemolytic anemia, thalassemia, sickle cell disease, aplastic "
    "anemia, myelodysplastic syndromes, immune thrombocytopenia, the coagulation "
    "cascade, hemophilia and von Willebrand disease, and venous thromboembolism, to "
    "acute and chronic leukemia, lymphoma, multiple myeloma, myeloproliferative "
    "neoplasms, DIC, transfusion medicine, transfusion reactions, stem cell "
    "transplantation, antithrombotic therapy, antiphospholipid syndrome and HIT, "
    "pediatric hematology, pregnancy and blood, and the future of the field - taught "
    "progressively along the ladder.",
    "hematology record", "JAH-HEM-", "JAH Hematology Archivist",
    "hematology archivist - clinical hematology: blood and blood-forming organs; "
    "anemias, hemoglobinopathies, leukemias, lymphomas, myeloma, bleeding and "
    "clotting disorders, transfusion medicine, marrow failure; teaching "
    "progressively along the ladder from foundations through compounded to "
    "advanced; answers from many angles - definition, example, analogy, "
    "application, history, math, how-to - using only archive data from this system",
    CIT_PUB, "public")
DBCFG["hematology-signature"] = _cfg(
    "hematology-signature", "The Hematology Signature Database",
    "His original Signature interpretation of blood as the body's freight and supply "
    "line: red cells as the oxygen freight fleet, white cells as the patrol fleet, "
    "platelets as the rapid-repair crews, plasma as the river they sail, and the "
    "marrow as the shipyard that builds them all. The full ladder from what "
    "hematology is through blood composition, the CBC, hemoglobin, the marrow, and "
    "the clinical encounter, through anemias, clotting disorders, and transfusion "
    "medicine, to leukemias, lymphomas, myeloma, stem cell transplantation, and the "
    "future of the field, reframed as Signature science. Clearly labeled "
    "Signature-made, never presented as authentic public record.",
    "hematology record", "JAH-HEMS-", "JAH Hematology Archivist (Signature)",
    "hematology archivist - Signature editions: his original Signature interpretation "
    "of blood as the bodily freight and supply line, clearly labeled "
    "Signature-made and never presented as authentic public record; teaches "
    "progressively along the ladder from foundations through compounded to advanced; "
    "answers from many angles - definition, example, analogy, application, history, "
    "math, how-to - using only archive data from this system",
    CIT_SIG, "signature")

base.DBCFG = DBCFG

# ---------------------------------------------------------------- demos
# Every demo is real, runnable, stdlib-only Python performing the actual
# hematology computation for its record. All are machine-executed by main().

_PREAMBLE = (
"import math\n"
)

def _wrap(name, rid, group, body):
    return (base._hdr(name, rid, group) + _PREAMBLE + body.replace("NAME", json.dumps(name)))

def demo_hm_what_is(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # the fleet at scale: blood volume, total red cells, daily production
    body_kg = 70.0
    bv_L = body_kg * 70.0 / 1000.0  # ~70 mL per kg
    rbc_per_uL = 5.0e6
    total_rbc = rbc_per_uL * bv_L * 1.0e6  # uL per liter
    daily_prod = 2.0e11
    print("blood volume: %.1f mL/kg x %.0f kg = %.2f L" % (70.0, body_kg, bv_L))
    print("total red cells: %.1e/uL x %.2f L = %.2e cells" % (rbc_per_uL, bv_L, total_rbc))
    print("marrow daily output: %.1e new red cells per day" % daily_prod)
    assert 4.85 < bv_L < 4.95
    assert 2.4e13 < total_rbc < 2.5e13
    print("rule: a 120-day lifespan demands a 200-billion-a-day shipyard")
    print("OK: %s counted the fleet" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_hm_blood_composition(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # steady state: circulating pool = daily production x lifespan
    rbc_pool = 2.0e11 * 120.0
    plt_pool = 1.0e11 * 10.0
    bv_uL = 4.9e6  # 4.9 L in microliters
    plt_conc = plt_pool / bv_uL
    print("red cell pool: 2.0e11/day x 120 d = %.2e cells" % rbc_pool)
    print("platelet pool: 1.0e11/day x 10 d = %.2e platelets" % plt_pool)
    print("platelet concentration: %.0f per microliter" % plt_conc)
    assert 2.39e13 < rbc_pool < 2.41e13
    assert 150000.0 < plt_conc < 400000.0
    print("rule: production x lifespan = the circulating pool, inside the normal band")
    print("OK: %s balanced the production line" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_hm_cbc(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # the four-gauge read on a sample panel
    hb, mcv, wbc, plt = 9.8, 72.0, 6500.0, 180000.0
    anemia = hb < 12.0
    if mcv < 80.0:
        bucket = "microcytic"
    elif mcv <= 100.0:
        bucket = "normocytic"
    else:
        bucket = "macrocytic"
    wbc_ok = 4000.0 <= wbc <= 11000.0
    plt_ok = 150000.0 <= plt <= 400000.0
    print("hemoglobin %.1f -> anemia: %s" % (hb, anemia))
    print("MCV %.0f -> %s" % (mcv, bucket))
    print("WBC %.0f in range: %s; platelets %.0f in range: %s" % (wbc, wbc_ok, plt, plt_ok))
    assert anemia is True
    assert bucket == "microcytic"
    assert wbc_ok and plt_ok
    print("read: microcytic anemia - check iron studies next")
    print("OK: %s read the four gauges" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_hm_hemoglobin_rbc(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # arterial oxygen content: 1.34 x Hb x saturation (+ dissolved)
    hufner, hb, sao2 = 1.34, 15.0, 0.98
    cao2 = hufner * hb * sao2 + 0.003 * 100.0
    cardiac_dL_min = 50.0  # 5.0 L/min
    do2 = cao2 * cardiac_dL_min
    print("CaO2: 1.34 x %.1f x %.2f + dissolved = %.2f mL/dL" % (hb, sao2, cao2))
    print("oxygen transport: %.2f mL/dL x %.0f dL/min = %.0f mL/min" % (cao2, cardiac_dL_min, do2))
    assert 19.6 < cao2 < 20.1
    assert 990.0 < do2 < 1010.0
    print("rule: hemoglobin is the freight capacity; saturation is how full the holds are")
    print("OK: %s loaded the oxygen freight" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_hm_marrow(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # the 100-minus-age rule for marrow cellularity
    for age, expected in [(20, 80), (40, 60), (60, 40), (80, 20)]:
        cell = 100 - age
        print("  age %d -> cellularity about %d %%" % (age, cell))
        assert cell == expected
    print("rule: the shipyard slowly fills with fat as the years pass")
    print("OK: %s inspected the shipyard" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_hm_iron_b12_folate(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # the iron inventory: a 500 mL donation vs daily absorption
    donation_mg = 500.0 * 0.5  # ~0.5 mg iron per mL of blood
    absorb_per_day = 1.5
    days = donation_mg / absorb_per_day
    b12_store_ug, b12_need_ug = 3000.0, 2.4
    b12_years = (b12_store_ug / b12_need_ug) / 365.0
    print("donation removes %.0f mg iron; at %.1f mg/day -> %.1f days to replace"
          % (donation_mg, absorb_per_day, days))
    print("B12 warehouse: %.0f ug / %.1f ug/day = %.2f years of stock"
          % (b12_store_ug, b12_need_ug, b12_years))
    assert 166.0 < days < 168.0
    assert 3.4 < b12_years < 3.5
    print("rule: iron is just-in-time, B12 is deep warehouse stock, folate is fresh produce")
    print("OK: %s audited the supply lines" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_hm_wbc_diff(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # absolute neutrophil count and its grades
    wbc, segs, bands = 2500.0, 0.30, 0.05
    anc = wbc * (segs + bands)
    if anc < 500.0:
        grade = "severe"
    elif anc < 1000.0:
        grade = "moderate"
    elif anc < 1500.0:
        grade = "mild"
    else:
        grade = "normal"
    print("ANC: %.0f x (%.0f %% + %.0f %%) = %.0f per microliter -> %s neutropenia"
          % (wbc, segs * 100.0, bands * 100.0, anc, grade))
    assert 870.0 < anc < 880.0
    assert grade == "moderate"
    print("rule: the ANC is the fleet readiness score - one number, and the harbor knows")
    print("OK: %s mustered the patrol fleet" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_hm_encounter(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # Mentzer index: MCV / red cell count; under 13 favors thalassemia trait
    def mentzer(mcv, rbc):
        return mcv / rbc
    cases = [((68.0, 5.9), "thalassemia pattern"), ((70.0, 3.8), "iron deficiency pattern")]
    for (mcv, rbc), expected in cases:
        m = mentzer(mcv, rbc)
        call = "thalassemia pattern" if m < 13.0 else "iron deficiency pattern"
        print("  MCV %.0f / RBC %.1f = %.2f -> %s" % (mcv, rbc, m, call))
        assert call == expected
    print("rule: bedside arithmetic separates the two look-alike small-cell anemias")
    print("OK: %s worked the Mentzer index" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_hm_iron_def(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # transferrin saturation = serum iron / TIBC; under 16 % is deficient
    iron, tibc, ferritin = 28.0, 460.0, 8.0
    tsat = iron / tibc * 100.0
    deficient = tsat < 16.0 and ferritin < 15.0
    print("TSAT: %.0f / %.0f x 100 = %.2f %% (deficient under 16 %%)" % (iron, tibc, tsat))
    print("ferritin %.0f ng/mL (deficient under 15) -> iron deficiency: %s" % (ferritin, deficient))
    assert 6.0 < tsat < 6.2
    assert deficient is True
    print("rule: restock the steel AND find the leak")
    print("OK: %s staged the iron deficiency" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_hm_b12_folate_def(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # megaloblastic triage: high MCV + low B12 = B12 deficiency
    mcv, b12, folate = 112.0, 140.0, 8.0
    macro = mcv > 100.0
    b12_low = b12 < 200.0
    folate_ok = folate >= 3.0
    if macro and b12_low:
        call = "B12-deficiency megaloblastic anemia"
    elif macro and not folate_ok:
        call = "folate-deficiency megaloblastic anemia"
    else:
        call = "not megaloblastic"
    print("MCV %.0f (macro: %s), B12 %.0f (low: %s), folate %.1f (ok: %s)"
          % (mcv, macro, b12, b12_low, folate, folate_ok))
    print("call: %s" % call)
    assert call == "B12-deficiency megaloblastic anemia"
    print("rule: replace B12 first and urgently - the nerves cannot wait")
    print("OK: %s triaged the megaloblasts" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_hm_acd(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # the trap pattern: low iron + low TSAT like deficiency, but ferritin high, TIBC low
    ferritin, tsat, tibc = 380.0, 11.0, 220.0
    trap = ferritin > 200.0 and tsat < 16.0 and tibc < 250.0
    true_def = ferritin < 15.0 and tsat < 16.0
    call = "anemia of inflammation (trap pattern)" if trap else ("true iron deficiency" if true_def else "unclear")
    print("ferritin %.0f, TSAT %.0f %%, TIBC %.0f -> %s" % (ferritin, tsat, tibc, call))
    assert trap is True
    assert call == "anemia of inflammation (trap pattern)"
    print("rule: full warehouse + starving assembly line = the siege, not the shortage")
    print("OK: %s read the trap pattern" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_hm_hemolysis(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # corrected reticulocyte count: retic % x (patient Hct / 45); over 2 % = marrow answering
    retic_pct, hct = 8.0, 27.0
    corr = retic_pct * (hct / 45.0)
    answering = corr > 2.0
    print("corrected retic: %.1f %% x (%.0f / 45) = %.2f %% (answering over 2 %%)"
          % (retic_pct, hct, corr))
    assert 4.7 < corr < 4.9
    assert answering is True
    print("call: marrow answering -> destruction (hemolysis), not production failure")
    print("OK: %s measured the overtime report" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_hm_thalassemia(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # beta trait pattern: HbA2 over 3.5 %, low MCV, high red count, Mentzer under 13
    hba2, mcv, rbc = 5.8, 66.0, 6.1
    mentzer = mcv / rbc
    trait = hba2 > 3.5 and mentzer < 13.0 and rbc > 5.0
    print("HbA2 %.1f %% (>3.5), MCV %.0f, RBC %.1f, Mentzer %.2f (<13)"
          % (hba2, mcv, rbc, mentzer))
    assert 10.8 < mentzer < 10.9
    assert trait is True
    print("call: beta thalassemia trait - no iron, counsel the family")
    print("OK: %s read the trait pattern" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_hm_sickle(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # epidemiology: 1 in 365 Black births in the US carries sickle cell disease
    births = 36500.0
    expected = births / 365.0
    print("expected cases in %.0f Black births at 1 in 365: %.1f" % (births, expected))
    assert 99.9 < expected < 100.1
    print("rule: one letter of DNA, and the cargo crystallizes when the air thins")
    print("OK: %s counted the newborns" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_hm_aplastic(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # Camitta: cellularity under 25 % + two of ANC<500, plt<20000, retic<20000
    cellularity, anc, plt = 15.0, 320.0, 14000.0
    criteria = sum([anc < 500.0, plt < 20000.0, True])  # retic low in this case
    severe = cellularity < 25.0 and criteria >= 2
    grade = "severe aplastic anemia" if severe else "non-severe"
    print("cellularity %.0f %%, ANC %.0f, platelets %.0f -> %s" % (cellularity, anc, plt, grade))
    assert severe is True
    print("rule: the empty marrow with pancytopenia is failure - transplant or immunosuppression, urgently")
    print("OK: %s graded the shutdown" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_hm_mds(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # IPSS-R: blasts 7 % -> 2, poor cytogenetics -> 3, Hb 8.5 -> 1, ANC 0.6 -> 0.5, plt 65k -> 0.5
    score = 2.0 + 3.0 + 1.0 + 0.5 + 0.5
    risk = "very high" if score > 6.0 else ("high" if score > 4.5 else "lower")
    print("IPSS-R: 2.0 + 3.0 + 1.0 + 0.5 + 0.5 = %.1f -> %s risk" % (score, risk))
    assert 6.9 < score < 7.1
    assert risk == "very high"
    print("rule: full factory, empty shelves - evaluate for transplant now")
    print("OK: %s scored the takeover" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_hm_itp(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # treatment threshold: under 30,000 or bleeding
    def decide(plt, bleeding):
        if plt < 30000.0 or bleeding:
            return "treat"
        return "observe"
    cases = [((18000.0, False), "treat"), ((75000.0, False), "observe"), ((45000.0, True), "treat")]
    for (plt, bleeding), expected in cases:
        got = decide(plt, bleeding)
        print("  platelets %.0f, bleeding %s -> %s" % (plt, bleeding, got))
        assert got == expected
    print("rule: outbuild the bounty hunters, or disarm them")
    print("OK: %s worked the threshold" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_hm_coag_cascade(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # INR = (patient PT / mean normal PT) ^ ISI
    pt, mnpt, isi = 19.2, 12.0, 1.1
    inr = (pt / mnpt) ** isi
    print("INR: (%.1f / %.1f) ^ %.1f = %.3f" % (pt, mnpt, isi, inr))
    assert 1.67 < inr < 1.69
    print("mixing-study rule: corrects with normal plasma -> factor missing; "
          "no correction -> inhibitor present")
    print("OK: %s standardized the weld gauge" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_hm_hemophilia_vwd(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # severity bands: under 1 % severe, 1-5 moderate, 5-40 mild; VWF activity under 30 abnormal
    def hemo_grade(f):
        if f < 1.0:
            return "severe"
        if f < 5.0:
            return "moderate"
        return "mild"
    fviii, vwf_act = 0.4, 28.0
    g = hemo_grade(fviii)
    vwd = vwf_act < 30.0
    print("factor VIII %.1f %% -> %s hemophilia A" % (fviii, g))
    print("VWF activity %.0f %% (<30) -> von Willebrand disease: %s" % (vwf_act, vwd))
    assert g == "severe"
    assert vwd is True
    print("rule: the missing foreman bleeds deep; the faulty glue bleeds mucosal")
    print("OK: %s graded the missing links" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_hm_vte(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # Wells DVT score: 2 or more means DVT likely
    pts = {"active cancer": 1, "entire leg swollen": 1, "calf >3 cm": 1,
           "pitting edema": 1, "previous DVT": 1, "alternative diagnosis": 0}
    score = sum(pts.values())
    likely = score >= 2
    for k, v in pts.items():
        print("  %s: +%d" % (k, v))
    print("Wells total: %d -> DVT likely: %s" % (score, likely))
    assert score == 5
    assert likely is True
    print("rule: score first, then D-dimer or ultrasound - never the reverse")
    print("OK: %s ran the Wells arithmetic" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_hm_acute_leuk(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # 20 % or more blasts defines acute leukemia
    wbc, blast_pct = 42000.0, 55.0
    blasts_abs = wbc * blast_pct / 100.0
    acute = blast_pct >= 20.0
    print("blasts: %.0f x %.0f %% = %.0f per microliter; >=20 %%: %s"
          % (wbc, blast_pct, blasts_abs, acute))
    assert 23000.0 < blasts_abs < 23200.0
    assert acute is True
    print("rule: the mutiny threshold is 20 % - workup and treatment as an emergency")
    print("OK: %s counted the mutineers" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_hm_chronic_leuk(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # lymphocyte doubling time: dt x ln2 / ln(N2/N1); under 12 months = active CLL
    n1, n2, dt = 25000.0, 50000.0, 9.0
    ldt = dt * math.log(2.0) / math.log(n2 / n1)
    active = ldt < 12.0
    print("LDT: %.0f mo x ln2 / ln(%.0f/%.0f) = %.2f months (<12: %s)"
          % (dt, n2, n1, ldt, active))
    assert 8.9 < ldt < 9.1
    assert active is True
    print("rule: the hoard's speedometer decides - under 12 months, treatment indicated")
    print("OK: %s timed the hoard" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_hm_lymphoma(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # Ann Arbor: regions + diaphragm side + B symptoms
    def stage(regions, both_sides, disseminated, b_symptoms):
        if disseminated:
            s = "IV"
        elif both_sides:
            s = "III"
        elif regions >= 2:
            s = "II"
        else:
            s = "I"
        return s + ("B" if b_symptoms else "A")
    cases = [((2, False, False, True), "IIB"), ((1, False, False, False), "IA"),
             ((3, True, False, False), "IIIA")]
    for (r, bs, d, sym), expected in cases:
        got = stage(r, bs, d, sym)
        print("  regions %d, both sides %s, disseminated %s, B %s -> stage %s"
              % (r, bs, d, sym, got))
        assert got == expected
    print("rule: map the rebellion's territory - biopsy with immunophenotyping first, always")
    print("OK: %s staged the rebellion" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_hm_myeloma(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # CRAB: Ca>11.5, creatinine>2, Hb<10, bone lesions
    ca, creat, hb, lesions, m_spike = 11.8, 2.3, 9.2, True, 3.2
    crab = sum([ca > 11.5, creat > 2.0, hb < 10.0, lesions])
    active = crab >= 1 and m_spike >= 3.0
    print("CRAB: Ca %.1f, creatinine %.1f, Hb %.1f, lesions %s -> %d of 4"
          % (ca, creat, hb, lesions, crab))
    print("M-spike %.1f g/dL -> active myeloma: %s" % (m_spike, active))
    assert crab == 4
    assert active is True
    print("rule: four checkboxes turn suspicion into a treatment order")
    print("OK: %s ran the damage audit" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_hm_mpn(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # phlebotomy arithmetic: remove enough whole blood to take Hct from 57 % to 45 %
    bv, h0, ht = 5.0, 0.57, 0.45
    excess_rbc = bv * (h0 - ht)
    vol = excess_rbc / h0
    print("excess red cell volume: %.1f L x (%.2f - %.2f) = %.2f L" % (bv, h0, ht, excess_rbc))
    print("whole blood to remove at Hct %.0f %%: %.3f L" % (h0 * 100.0, vol))
    assert 1.05 < vol < 1.06
    print("rule: the release valve opens until the hematocrit reads under 45 %")
    print("OK: %s worked the release valve" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_hm_dic(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # ISTH DIC score: 5 or more means overt DIC
    plt_pts = 2      # platelets 38k < 50k
    ddimer_pts = 3   # strongly elevated
    pt_pts = 2       # PT prolonged 7 s (>= 6)
    fib_pts = 1      # fibrinogen 85 < 100
    total = plt_pts + ddimer_pts + pt_pts + fib_pts
    overt = total >= 5
    print("ISTH: platelets %d + D-dimer %d + PT %d + fibrinogen %d = %d (>=5: %s)"
          % (plt_pts, ddimer_pts, pt_pts, fib_pts, total, overt))
    assert total == 8
    assert overt is True
    print("rule: stop the panic (treat the trigger), then refill the shelves")
    print("OK: %s audited the empty accounts" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_hm_transfusion(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # ABO red-cell compatibility: donor antigens vs recipient antibodies
    compat = {"O": ["O", "A", "B", "AB"], "A": ["A", "AB"],
              "B": ["B", "AB"], "AB": ["AB"]}
    cases = [(("O", "A"), True), (("A", "O"), False), (("B", "AB"), True),
             (("AB", "O"), False), (("O", "AB"), True), (("A", "AB"), True)]
    for (donor, recip), expected in cases:
        got = recip in compat[donor]
        print("  donor %s -> recipient %s: compatible %s" % (donor, recip, got))
        assert got == expected
    print("rule: fly the wrong flag and the shore batteries open fire - O is the plain flag")
    print("OK: %s checked the recognition signals" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_hm_transfusion_reactions(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # reaction triage: timing + signature
    def triage(when, signs):
        if when == "during" and "flank pain" in signs and "red urine" in signs:
            return "acute hemolytic"
        if when == "within 6h" and "breathless" in signs:
            if "overload" in signs:
                return "TACO"
            return "TRALI"
        if signs == ["hives"]:
            return "allergic"
        if "fever" in signs:
            return "febrile non-hemolytic"
        return "unclear"
    cases = [(("during", ["flank pain", "red urine"]), "acute hemolytic"),
             (("within 6h", ["breathless"]), "TRALI"),
             (("during", ["hives"]), "allergic")]
    for (when, signs), expected in cases:
        got = triage(when, signs)
        print("  %s %s -> %s" % (when, signs, got))
        assert got == expected
    print("rule: stop the unit first with any concerning symptom, assess second")
    print("OK: %s ran the reaction triage" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_hm_hsct(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # CD34 dose target: 2 million or more per kilogram
    weight_kg, per_kg = 75.0, 2.0e6
    dose = weight_kg * per_kg
    ok = dose >= 2.0e6 * weight_kg
    print("CD34 dose: %.0f kg x %.1e/kg = %.2e cells (target met: %s)"
          % (weight_kg, per_kg, dose, ok))
    assert 1.49e8 < dose < 1.51e8
    assert ok is True
    print("rule: demolish, re-crew, engraft at 2 to 3 weeks")
    print("OK: %s counted the new workforce" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_hm_anticoag(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # warfarin control: INR 2.0-3.0 therapeutic; time in range from readings
    inr_now = 1.4
    state = "subtherapeutic" if inr_now < 2.0 else ("supratherapeutic" if inr_now > 3.0 else "therapeutic")
    readings = [2.4, 2.8, 1.9, 2.2, 3.4, 2.6, 1.4, 2.9, 2.1, 2.5]
    in_range = sum(1 for x in readings if 2.0 <= x <= 3.0)
    ttr = in_range / len(readings) * 100.0
    print("INR now %.1f -> %s (window 2.0-3.0): increase the dose" % (inr_now, state))
    print("time in range: %d of %d readings = %.0f %%" % (in_range, len(readings), ttr))
    assert state == "subtherapeutic"
    assert 69.0 < ttr < 71.0
    print("rule: name the reversal plan before the first dose")
    print("OK: %s audited the traffic control" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_hm_aps_hit(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # 4Ts: platelet fall (2) + timing day 5-10 (2) + thrombosis (1) + no other cause (2)
    t1, t2, t3, t4 = 2, 2, 1, 2
    total = t1 + t2 + t3 + t4
    prob = "high" if total >= 6 else ("intermediate" if total >= 4 else "low")
    print("4Ts: %d + %d + %d + %d = %d -> %s probability" % (t1, t2, t3, t4, total, prob))
    assert total == 7
    assert prob == "high"
    print("rule: a forged order is countermanded instantly - stop all heparin")
    print("OK: %s scored the inside job" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_hm_pediatric(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # the 2-month physiologic nadir: 9 to 11 g/dL is normal there
    hb, age_months = 9.8, 2.0
    lo, hi = 9.0, 11.0
    normal = lo <= hb <= hi
    print("age %.0f months, Hb %.1f g/dL; nadir range %.0f-%.0f -> physiologic: %s"
          % (age_months, hb, lo, hi, normal))
    assert normal is True
    print("rule: read the child on the child's curve, not the adult's")
    print("OK: %s checked the commissioning curve" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_hm_pregnancy(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # third-trimester threshold 10.5 g/dL separates dilution from true anemia
    hb, weeks, threshold = 10.8, 30.0, 10.5
    anemic = hb < threshold
    print("week %.0f, Hb %.1f g/dL vs threshold %.1f -> anemic: %s"
          % (weeks, hb, threshold, anemic))
    assert anemic is False
    print("rule: the planned flood thins every gauge by design - threshold first, worry second")
    print("OK: %s read the flood gauge" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_hm_future(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # landmark numbers: CAR-T 81 % remissions; gene therapy 32 of 35 transfusion-free
    car_t = 81.0 / 100.0 * 100.0
    gene = 32.0 / 35.0 * 100.0
    print("CAR-T remissions: 81 of 100 = %.0f %%" % car_t)
    print("gene therapy transfusion-free: 32 of 35 = %.2f %%" % gene)
    assert 80.9 < car_t < 81.1
    assert 91.0 < gene < 92.0
    print("rule: draw it, engineer it, return it - the accessible tissue leads")
    print("OK: %s ran the landmark numbers" % NAME)
if __name__ == "__main__":
    main()
''')

DEMOS = {
    "what_is": demo_hm_what_is,
    "blood_composition": demo_hm_blood_composition,
    "cbc": demo_hm_cbc,
    "hemoglobin_rbc": demo_hm_hemoglobin_rbc,
    "marrow": demo_hm_marrow,
    "iron_b12_folate": demo_hm_iron_b12_folate,
    "wbc_diff": demo_hm_wbc_diff,
    "encounter": demo_hm_encounter,
    "iron_def": demo_hm_iron_def,
    "b12_folate_def": demo_hm_b12_folate_def,
    "acd": demo_hm_acd,
    "hemolysis": demo_hm_hemolysis,
    "thalassemia": demo_hm_thalassemia,
    "sickle": demo_hm_sickle,
    "aplastic": demo_hm_aplastic,
    "mds": demo_hm_mds,
    "itp": demo_hm_itp,
    "coag_cascade": demo_hm_coag_cascade,
    "hemophilia_vwd": demo_hm_hemophilia_vwd,
    "vte": demo_hm_vte,
    "acute_leuk": demo_hm_acute_leuk,
    "chronic_leuk": demo_hm_chronic_leuk,
    "lymphoma": demo_hm_lymphoma,
    "myeloma": demo_hm_myeloma,
    "mpn": demo_hm_mpn,
    "dic": demo_hm_dic,
    "transfusion": demo_hm_transfusion,
    "transfusion_reactions": demo_hm_transfusion_reactions,
    "hsct": demo_hm_hsct,
    "anticoag": demo_hm_anticoag,
    "aps_hit": demo_hm_aps_hit,
    "pediatric": demo_hm_pediatric,
    "pregnancy": demo_hm_pregnancy,
    "future": demo_hm_future,
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
    for slug in ("hematology", "hematology-signature"):
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
