#!/usr/bin/env python3
"""Build the Gastroenterology field databases for JAH Databases (field #38, taxonomy order).

Verified 2026-10-17 (see entries_gastroenterology.py docstring): NO database
covers gastroenterology as a clinical specialty (esophagus, stomach,
small/large intestine, liver/biliary, pancreas; GERD, ulcers, IBD, IBS,
celiac, GI bleeding, liver disease, pancreatitis, GI cancers, endoscopy
concepts, gut microbiome clinical aspects). Clinical-specialty framing,
distinct from anatomy/histology.

Manifest search (2,376 databases): zero 'gastroenterolog*' slugs/names; no
db/gastroenterolog* dirs. Whole-system exact-title sweep over the manifest
PLUS every shard index 't' key: zero collisions for all 34 planned titles
x2 editions (68 variants). Near-neighbors confirmed different disciplines:
'hepatology' is MISSING (n=558, not yet built), 'endocrinology' covers the
hormone system (pancreatic endocrine function only), diabetes coverage is
fragmented across general health databases, 'nutrition' databases cover food
science not the clinical GI specialty. ZERO full-record discipline coverage
anywhere.

So this build creates two NEW databases, 34 ladder-ordered records each:

  gastroenterology              - The Gastroenterology Database
                                  (public-harvest: real, fact-checked clinical
                                  gastroenterology; standard references
                                  Feldman et al. "Sleisenger and Fordtran's
                                  Gastrointestinal and Liver Disease" 11th ed
                                  2021; Podolsky et al. "Yamada's Textbook of
                                  Gastroenterology" 7th ed 2022; Jameson et
                                  al. "Harrison's Principles of Internal
                                  Medicine" 21st ed 2022; ACG/AGA/AASLD
                                  clinical guidelines)
  gastroenterology-signature    - The Gastroenterology Signature Database
                                  (his original Signature interpretation of
                                  the digestive system as the body's intake,
                                  refining, and logistics works; src
                                  signature, titles suffixed
                                  " (Signature Edition)", never presented as
                                  authentic public record)

34 records each, ordered by the teaching ladder (ladder_rank 1-10,
ladder_tier foundations/compounded/advanced); the shard index is written in
ladder order so pages present simple -> compounded -> complex.

ID prefixes: JAH-GAS- (public) and JAH-GASS- (signature), both verified free
in the manifest and in every shard index (zero hits).

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
from entries_gastroenterology import ENTRIES, SIG_TAIL

# ---------------------------------------------------------------- DB config

def _cfg(slug, name, tagline, record_kind, prefix, ai, role, citation, source):
    sig_line = ("Signature originals - his original Signature interpretation of the digestive "
                "system as the body's intake, refining, and logistics works: the gut as the "
                "receiving dock, enzymes as the processing crews, the liver as the refinery, "
                "the microbiome as the resident workforce. Clearly "
                "labeled Signature-made, never presented as authentic public record.")
    pub_line = ("Public records - real, fact-checked clinical gastroenterology: the full ladder from "
                "what gastroenterology is through the tract, the chemistry, the wall, the liver, "
                "the pancreas, and the microbiome to the great GI diseases, organized in the "
                "Signature system.")
    ladder = (" Records are ordered by the teaching ladder: Foundations (what gastroenterology "
              "is, the digestive tract, digestion chemistry, the gut wall, the liver and biliary "
              "system, the pancreas, the gut microbiome, the clinical encounter) -> "
              "Compounded (GERD, functional dyspepsia, peptic ulcer disease and H. pylori, upper "
              "GI bleeding, celiac disease and malabsorption, irritable bowel syndrome, motility "
              "disorders, Crohn's disease, ulcerative colitis, lower GI bleeding and diverticular "
              "disease, colorectal polyps and screening) -> Advanced (endoscopy and colonoscopy, "
              "endoscopic therapy, acute pancreatitis, gallstone disease, biliary obstruction and "
              "jaundice, chronic liver disease and cirrhosis, viral hepatitis, fatty liver disease, "
              "upper GI cancers, colorectal cancer, pancreatic and liver cancers, GI emergencies, "
              "nutritional support, pediatric gastroenterology, the future of the field).")
    return {
        "name": name, "tagline": tagline, "record_kind": record_kind,
        "prefix": prefix, "ai": ai, "role": role,
        "hero_p": "%s - %s Every record carries the full entry: description, how it works, "
                  "key points, requirements, standards, citations, and a working demonstration "
                  "program.%s" % (tagline, sig_line if source == "signature" else pub_line, ladder),
        "sig_type": ("Signature originals organized in the Signature system"
                     if source == "signature" else
                     "Public records organized in the Signature system"),
        "search_ph": "Search GERD, ulcers, IBD, Crohn's, colitis, cirrhosis, hepatitis, endoscopy, polyps, pancreatitis, microbiome, jaundice...",
        "chat_ph": "Ask about gastroenterology...",
        "archive_blurb": ("Seeded %s gastroenterology records, marching toward one million records. "
                          "Presented in teaching-ladder order: foundations, compounded, advanced."
                          % ("Signature-original" if source == "signature" else "public-record")),
        "schema": ("id, t, g, name, title, description, how_it_works, key_points, requirements, "
                   "standards, citations, src, ladder_rank, ladder_tier, demo"),
        "fields": "Foundations \u00b7 Compounded \u00b7 Advanced - each tier opens on demand and loads only what you open",
        "gen_desc": "Generate clearly-labeled gastroenterology studies. Seeded archive records are the authoritative entries.",
        "greet": "I am the %s. Ask me about gastroenterology - from what it is through the digestive "
        "tract, digestion chemistry, the gut wall, the liver and biliary system, the pancreas, the "
        "gut microbiome, and the clinical encounter, through GERD, ulcers, IBD, IBS, celiac disease, "
        "GI bleeding, and polyps, to endoscopy, pancreatitis, liver disease, GI cancers, and the "
        "future of the field." % ai,
        "gen_fields": ["Foundations", "Compounded", "Advanced"],
        "gen_kind": "gastroenterology-study", "gen_demo_kind": "gastroenterology-demo",
        "source": source,
    }

CIT_PUB = ("Gastroenterology (standard references: Feldman et al. Sleisenger and Fordtran's "
           "Gastrointestinal and Liver Disease 11th ed 2021; Podolsky et al. Yamada's Textbook "
           "of Gastroenterology 7th ed 2022; Jameson et al. Harrison's Principles of Internal "
           "Medicine 21st ed 2022; ACG GERD, H. pylori, ulcerative colitis, and Crohn's disease "
           "guidelines; U.S. Multi-Society Task Force colorectal cancer screening "
           "recommendations; AASLD hepatitis B guidance).")
CIT_SIG = CIT_PUB + (" Signature editions are his original Signature interpretation "
                     "of the digestive system as the body's intake, refining, and logistics "
                     "works, clearly labeled Signature-made.")

DBCFG = {}
DBCFG["gastroenterology"] = _cfg(
    "gastroenterology", "The Gastroenterology Database",
    "Real, fact-checked clinical gastroenterology: from what gastroenterology is through "
    "the digestive tract, digestion chemistry, the gut wall, the liver and biliary system, "
    "the pancreas, the gut microbiome, and the clinical encounter, through GERD, functional "
    "dyspepsia, peptic ulcer disease and H. pylori, upper GI bleeding, celiac disease and "
    "malabsorption, irritable bowel syndrome, motility disorders, Crohn's disease, ulcerative "
    "colitis, lower GI bleeding and diverticular disease, and colorectal polyps and screening, "
    "to endoscopy and colonoscopy, endoscopic therapy, acute pancreatitis, gallstone disease, "
    "biliary obstruction and jaundice, chronic liver disease and cirrhosis, viral hepatitis, "
    "fatty liver disease, upper GI cancers, colorectal cancer, pancreatic and liver cancers, "
    "GI emergencies, nutritional support, pediatric gastroenterology, and the future of the "
    "field - taught progressively along the ladder.",
    "gastroenterology record", "JAH-GAS-", "JAH Gastroenterology Archivist",
    "gastroenterology archivist - clinical gastroenterology: esophagus, stomach, intestines, "
    "liver, biliary, pancreas; GERD, ulcers, IBD, IBS, celiac, GI bleeding, liver disease, "
    "pancreatitis, GI cancers, endoscopy, microbiome; teaching progressively along the ladder "
    "from foundations through compounded to advanced; answers from many angles - definition, "
    "example, analogy, application, history, math, how-to - using only archive data from this system",
    CIT_PUB, "public")
DBCFG["gastroenterology-signature"] = _cfg(
    "gastroenterology-signature", "The Gastroenterology Signature Database",
    "His original Signature interpretation of the digestive system as the body's intake, "
    "refining, and logistics works: the full ladder from what gastroenterology is through "
    "the tract, the chemistry, the wall, the liver, the pancreas, and the microbiome to the "
    "great GI diseases and the future of the field, reframed as Signature science. Clearly "
    "labeled Signature-made, never presented as authentic public record.",
    "gastroenterology record", "JAH-GASS-", "JAH Gastroenterology Archivist (Signature)",
    "gastroenterology archivist - Signature editions: his original Signature interpretation "
    "of the digestive system as the bodily intake, refining, and logistics works, clearly "
    "labeled Signature-made and never presented as authentic public record; teaches "
    "progressively along the ladder from foundations through compounded to advanced; answers "
    "from many angles - definition, example, analogy, application, history, math, how-to - "
    "using only archive data from this system",
    CIT_SIG, "signature")

base.DBCFG = DBCFG

# ---------------------------------------------------------------- demos
# Every demo is real, runnable, stdlib-only Python performing the actual
# gastroenterology computation for its record. All are machine-executed by main().

_PREAMBLE = (
"import math\n"
)

def _wrap(name, rid, group, body):
    return (base._hdr(name, rid, group) + _PREAMBLE + body.replace("NAME", json.dumps(name)))

def demo_ga_what_is(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def main():
    # the eight-meter line: segment lengths in cm
    segments = [("esophagus", 25), ("stomach", 25), ("small intestine", 600), ("large intestine", 150)]
    total_cm = sum(s for _, s in segments)
    # surface amplification: small intestine ~250 m^2 vs skin ~1.7 m^2
    ratio = 250.0/1.7
    print("digestive tract segments:")
    for sname, s in segments:
        print("  %-16s %3d cm" % (sname, s))
    print("total line: %d cm = %.1f m" % (total_cm, total_cm/100.0))
    print("small-intestine surface ~250 m^2 vs skin ~1.7 m^2 -> %.2fx amplification" % ratio)
    assert total_cm == 800
    assert 147.0 < ratio < 147.1
    print("rule: length sets the route, surface sets the throughput")
    print("OK: %s walked the line" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_ga_tract(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def main():
    # nominal station times in hours
    stomach, small_bowel, colon = 3.0, 4.0, 33.0
    total = stomach + small_bowel + colon
    colon_share = colon/total*100.0
    print("station times: stomach %.0f h, small bowel %.0f h, colon %.0f h" % (stomach, small_bowel, colon))
    print("whole-gut transit: %.0f + %.0f + %.0f = %.0f h" % (stomach, small_bowel, colon, total))
    print("colon share: %.0f/%.0f = %.1f %%" % (colon, total, colon_share))
    assert total == 40.0
    assert 82.4 < colon_share < 82.6
    print("rule: the slowest station sets the symptom - read transit from the bottom up")
    print("OK: %s timed the conveyor" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_ga_chemistry(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def main():
    # pH 1.5 -> [H+] = 10^-1.5 M, in millimolar
    h_mm = 10.0**(-1.5)*1000.0
    acid_meq = 200.0
    bicarb_meq = 150.0
    print("gastric pH 1.5 -> [H+] = 10^-1.5 M = %.2f mM" % h_mm)
    print("daily gastric acid: ~%.0f mEq; pancreatic bicarbonate answer: ~%.0f mEq" % (acid_meq, bicarb_meq))
    print("net luminal acid after neutralization: ~%.0f mEq (absorbed/buffered downstream)" % (acid_meq - bicarb_meq))
    assert 31.6 < h_mm < 31.7
    assert acid_meq - bicarb_meq == 50.0
    print("rule: run hot, then neutralize - the line is an acid bath with a fire crew downstream")
    print("OK: %s balanced the pours" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_ga_gut_wall(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def main():
    layers = ["mucosa", "submucosa", "muscularis propria", "serosa/adventitia"]
    # esophageal wave: 25 cm at 3 cm/s
    wave_s = 25.0/3.0
    print("gut wall layers (inside out): %d" % len(layers))
    for i, lname in enumerate(layers, 1):
        print("  %d. %s" % (i, lname))
    print("esophageal wave: 25 cm / 3 cm/s = %.2f s per swallow" % wave_s)
    assert len(layers) == 4
    assert 8.33 < wave_s < 8.34
    print("rule: contract behind, relax ahead - wave speed times length sets clearing time")
    print("OK: %s ran the wave" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_ga_liver(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def main():
    # hepatic blood flow split: portal 75%, arterial 25% of 1.5 L/min
    total_flow = 1.5
    portal = total_flow*0.75
    arterial = total_flow*0.25
    cardiac = 5.0
    share = total_flow/cardiac*100.0
    recycles = 8
    print("hepatic flow: %.2f L/min = portal %.3f + arterial %.3f" % (total_flow, portal, arterial))
    print("share of %.1f L/min cardiac output: %.0f %%" % (cardiac, share))
    print("bile-salt pool recycling: ~%d turns/day" % recycles)
    assert portal == 1.125 and arterial == 0.375
    assert share == 30.0
    print("rule: a third of the blood visits the refinery every minute - first pass is the inspection")
    print("OK: %s toured the refinery" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_ga_pancreas(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def main():
    # weight-based total daily insulin: 0.6 U/kg/day
    wt = 70.0
    tdd = wt*0.6
    basal_day = tdd*0.5
    basal_hr = basal_day/24.0
    print("weight %.0f kg x 0.6 U/kg/day = %.0f U total daily" % (wt, tdd))
    print("basal half: %.0f U/day = %.3f U/hour; bolus half: %.0f U/day" % (basal_day, basal_hr, tdd - basal_day))
    assert tdd == 42.0
    assert basal_day == 21.0
    assert 0.874 < basal_hr < 0.876
    print("rule: the ratio is the instruction - store when fed, mobilize when fasted")
    print("OK: %s dosed the control room" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_ga_microbiome(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def main():
    # Sender/Fuchs/Milo 2016: ~38T bacteria vs ~30T human cells
    cell_ratio = 38.0/30.0
    gene_leverage = 3.0e6/2.0e4
    fmt_cures = 100*0.90
    print("bacteria 38T / human cells 30T = %.4f : 1 (near parity)" % cell_ratio)
    print("microbial genes 3M / human genes 20K = %.0fx metabolic leverage" % gene_leverage)
    print("FMT for recurrent C. difficile: 100 patients x 90%% -> %.0f cures" % fmt_cures)
    assert 1.266 < cell_ratio < 1.268
    assert gene_leverage == 150.0
    assert fmt_cures == 90.0
    print("rule: the workforce you did not hire does the shifts you cannot staff")
    print("OK: %s took the census" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_ga_encounter(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def main():
    # Bayes: sens 90%, spec 85%, prevalence 10%
    sens, spec, prev = 0.90, 0.85, 0.10
    tp = sens*prev
    fp = (1.0 - spec)*(1.0 - prev)
    ppv = tp/(tp + fp)
    print("sensitivity %.0f %%, specificity %.0f %%, prevalence %.0f %%" % (sens*100, spec*100, prev*100))
    print("true positives %.3f, false positives %.3f" % (tp, fp))
    print("positive predictive value: %.3f / %.3f = %.1f %%" % (tp, tp + fp, ppv*100.0))
    assert 0.399 < ppv < 0.401
    print("rule: prevalence sets the meaning - test the story, not the symptom")
    print("OK: %s read the odds" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_ga_gerd(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def main():
    # acid exposure time: 90 min of the 1440-min day
    aet = 90.0/1440.0*100.0
    print("acid exposure: 90 min / 1440 min = %.2f %%" % aet)
    print("Lyon lines: <4%% normal, 4-6%% inconclusive, >6%% abnormal")
    verdict = "ABNORMAL - GERD" if aet > 6.0 else "not abnormal"
    print("verdict: %s" % verdict)
    assert 6.24 < aet < 6.26
    assert aet > 6.0
    print("rule: the check valve failed - pressure gradient always wins an open gate")
    print("OK: %s timed the reflux" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_ga_dyspepsia(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def main():
    # 4 cardinal symptoms -> C(4,2) two-symptom patterns
    def c(n, k):
        return math.factorial(n)//(math.factorial(k)*math.factorial(n - k))
    patterns = c(4, 2)
    symptoms = ["fullness", "early satiety", "epigastric pain", "burning"]
    print("cardinal symptoms: %s" % ", ".join(symptoms))
    print("two-symptom patterns: C(4,2) = %d" % patterns)
    assert patterns == 6
    print("rule: six presentations, one name - the sensors misreport, the pipes are fine")
    print("OK: %s mapped the patterns" % NAME)
if __name__ == "__main__":
    main()
''')
def demo_ga_ulcer(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def main():
    # 1000 people, 44% H. pylori prevalence, 85% eradication
    infected = 1000.0*0.44
    cured = infected*0.85
    salvage = infected - cured
    print("1000 people x 44%% -> %.0f infected" % infected)
    print("eradication 85%%: %.0f x 0.85 = %.0f cured, %.0f need salvage" % (infected, cured, salvage))
    assert infected == 440.0
    assert cured == 374.0
    assert salvage == 66.0
    print("rule: evict the saboteurs, recoat the wall, hold the acid back while it cures")
    print("OK: %s cleared the infection" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_ga_ugib(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def main():
    # 1 unit PRBC ~= +1 g/dL hemoglobin; restrictive threshold <7 g/dL
    hb_now, hb_target = 6.0, 9.0
    units = hb_target - hb_now
    threshold = 7.0
    print("hemoglobin %.0f g/dL -> target %.0f g/dL: %.0f units PRBC" % (hb_now, hb_target, units))
    print("transfuse below %.0f g/dL (restrictive); scope within 24 hours" % threshold)
    assert units == 3.0
    assert hb_now < threshold
    print("rule: restore line pressure first, then send the camera crew to clamp the leak")
    print("OK: %s ran the runbook" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_ga_celiac(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def main():
    # screening 10,000 at 1% prevalence; tTG-IgA 95% sens / 95% spec
    pop, prev = 10000.0, 0.01
    cases = pop*prev
    tp = cases*0.95
    fp = (pop - cases)*0.05
    ppv = tp/(tp + fp)*100.0
    print("10000 screened x 1%% -> %.0f true cases" % cases)
    print("true positives %.0f, false positives %.0f" % (tp, fp))
    print("positive predictive value: 95/590 = %.2f %% - biopsy confirms" % ppv)
    assert tp == 95.0
    assert fp == 495.0
    assert 16.10 < ppv < 16.11
    print("rule: most screening positives are false - confirm the demolition order with tissue")
    print("OK: %s read the screening table" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_ga_ibs(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def main():
    # Rome IV: pain >=1 day/week x 12 weeks = 12 pain days minimum
    pain_days = 12*1
    subtypes = ["IBS-D", "IBS-C", "IBS-M", "IBS-U"]
    bristol = 7
    print("Rome IV pain threshold: 12 weeks x 1 day/week = %d pain days minimum" % pain_days)
    print("subtypes from %d Bristol stool types: %s" % (bristol, ", ".join(subtypes)))
    assert pain_days == 12
    assert len(subtypes) == 4
    print("rule: recalibrate sensors and software - the machinery is sound")
    print("OK: %s subtyped the loop" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_ga_motility(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def main():
    # scintigraphy: >10% retained at 4 h = gastroparesis; patient retains 25%
    cutoff, retained = 10.0, 25.0
    multiple = retained/cutoff
    print("cutoff: %.0f %% retained at 4 h; patient: %.0f %%" % (cutoff, retained))
    print("delay multiple: %.0f/%.0f = %.1fx the diagnostic line" % (retained, cutoff, multiple))
    assert multiple == 2.5
    print("achalasia pattern: non-relaxing sphincter + aperistalsis on manometry")
    print("rule: push a weak pump harder; cut open a gate that will not obey")
    print("OK: %s tested the pumps" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_ga_crohn(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def main():
    # Montreal: 3 ages x 3 locations x 3 behaviors
    phenotypes = 3*3*3
    hb_cutoff = 5
    print("Montreal axes: 3 ages x 3 locations x 3 behaviors = %d phenotypes" % phenotypes)
    print("Harvey-Bradshaw remission: under %d" % hb_cutoff)
    assert phenotypes == 27
    print("rule: a wall-deep siege - seal the tunnels, resect the ruins, intercept the messengers")
    print("OK: %s classified the siege" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_ga_uc(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def main():
    # Mayo: 4 components x 0-3 = 0-12; example 2+2+1+1
    mayo = 2 + 2 + 1 + 1
    extents = ["E1 proctitis", "E2 left-sided", "E3 extensive"]
    print("Mayo score: 2+2+1+1 = %d / 12 -> moderate disease" % mayo)
    print("extent grades: %s" % ", ".join(extents))
    assert mayo == 6
    assert len(extents) == 3
    print("rule: a surface fire in the last warehouse - demolishing the building ends it")
    print("OK: %s scored the fire" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_ga_lgib(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def main():
    # 1000 eighty-year-olds: >50% diverticulosis, 4% of those bleed
    cohort = 1000.0
    divert = cohort*0.50
    bleeders = divert*0.04
    print("1000 octogenarians x >50%% -> %.0f with diverticulosis" % divert)
    print("bleed rate 4%%: %.0f x 0.04 = %.0f expected bleeders" % (divert, bleeders))
    assert divert == 500.0
    assert bleeders == 20.0
    print("rule: age writes the odds, pressure writes the blisters")
    print("OK: %s counted the cohort" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_ga_polyps(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def main():
    # FIT: 74% cancer sensitivity on 100 cancers; size cutoff 1 cm
    detected = 100.0*0.74
    missed = 100.0 - detected
    cutoff_cm = 1.0
    print("FIT on 100 cancers: %.0f detected, %.0f missed - repeat annually" % (detected, missed))
    print("size triage: >=%.0f cm = advanced adenoma until proven otherwise" % cutoff_cm)
    assert detected == 74.0
    assert missed == 26.0
    print("rule: the sweep passes on a shorter cycle than the fault needs to mature")
    print("OK: %s worked the interception" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_ga_endoscopy(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def main():
    # ADR 30% on 200 screening exams; withdrawal >=6 min; ADR floor 25%
    exams, adr = 200.0, 0.30
    yield_n = exams*adr
    print("200 exams x 30%% ADR = %.0f patients with adenomas found and removed" % yield_n)
    print("quality floors: ADR >=25%%, withdrawal >=6 min")
    assert yield_n == 60.0
    print("rule: an inspection that misses the faults is worse than none - publish the batting average")
    print("OK: %s audited the inspector" % NAME)
if __name__ == "__main__":
    main()
''')
def demo_ga_endo_therapy(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def main():
    # ERCP: 92% cannulation on 100 attempts; banding 2-4 sessions
    successes = 100.0*0.92
    print("ERCP: 100 attempts x 92%% -> %.0f successful duct accesses" % successes)
    print("variceal banding: eradication in 2-4 sessions")
    assert successes == 92.0
    print("rule: bring the operating room to the lesion - diagnosis and treatment in one insertion")
    print("OK: %s worked the tools" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_ga_pancreatitis(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def main():
    # fluids: 300 mL/h x 12 h; lipase >3x ULN; Ranson >=3 of 11 = severe
    fluids_ml = 300.0*12.0
    print("aggressive fluids: 300 mL/h x 12 h = %.0f mL" % fluids_ml)
    print("diagnostic line: lipase >3x upper limit of normal (2 of 3 criteria)")
    print("Ranson: >=3 of 11 criteria = severe")
    assert fluids_ml == 3600.0
    print("rule: flood the building, let it burn out, remove what jammed the dock")
    print("OK: %s fought the fire" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_ga_gallstones(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def main():
    # 100 Western stone patients: 80% cholesterol; HIDA EF cutoff 35%
    chol = 100.0*0.80
    ef, cutoff = 40.0, 35.0
    print("100 stone patients x 80%% -> %.0f cholesterol stones" % chol)
    print("HIDA ejection fraction %.0f %% vs cutoff %.0f %% -> %s" % (ef, cutoff, "normal" if ef >= cutoff else "dyskinesia"))
    assert chol == 80.0
    assert ef >= cutoff
    print("rule: the sump is expendable, the main drain is not")
    print("OK: %s assayed the sump" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_ga_biliary(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def main():
    # total 5.2, direct 4.1 mg/dL; conversion x17.1
    total, direct = 5.2, 4.1
    direct_share = direct/total*100.0
    umol = 3.0*17.1
    print("bilirubin: total %.1f, direct %.1f mg/dL -> direct share %.2f %%" % (total, direct, direct_share))
    print("pattern: %s" % ("cholestatic/obstructive" if direct_share > 50.0 else "pre-hepatic"))
    print("3 mg/dL x 17.1 = %.1f micromol/L" % umol)
    assert 78.84 < direct_share < 78.86
    assert 51.29 < umol < 51.31
    print("rule: the fraction locates the dam - read which side you stand on")
    print("OK: %s sounded the river" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_ga_cirrhosis(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def main():
    # Child-Pugh: 2+2+1+2+1; classes A 5-6, B 7-9, C 10-15
    score = 2 + 2 + 1 + 2 + 1
    if score <= 6:
        cls = "A"
    elif score <= 9:
        cls = "B"
    else:
        cls = "C"
    print("Child-Pugh: 2+2+1+2+1 = %d -> class %s (A 5-6, B 7-9, C 10-15)" % (score, cls))
    assert score == 8
    assert cls == "B"
    print("rule: manage the failures while the replacement plant is commissioned")
    print("OK: %s graded the refinery" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_ga_hepatitis(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def main():
    # 3 binary serology markers -> 8 patterns; 8 log10 IU/mL; 95% HCV cure
    patterns = 2**3
    viral_load = 10**8
    cures = 100.0*0.95
    print("serology: 3 markers -> 2^3 = %d patterns" % patterns)
    print("8 log10 IU/mL = %d IU/mL" % viral_load)
    print("HCV direct-acting antivirals: 100 treated x 95%% -> %.0f cures" % cures)
    assert patterns == 8
    assert viral_load == 100000000
    assert cures == 95.0
    print("rule: eviction record runs from total victory (C) to permanent containment (B)")
    print("OK: %s read the tenancy" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_ga_nafld(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def main():
    # FIB-4 = (age x AST) / (platelets x sqrt(ALT)); cutoffs 1.3 / 2.67
    age, ast, alt, plt = 55.0, 45.0, 60.0, 200.0
    fib4 = (age*ast)/(plt*math.sqrt(alt))
    print("FIB-4 = (%.0f x %.0f) / (%.0f x sqrt(%.0f)) = %.0f / %.1f = %.3f" % (age, ast, plt, alt, age*ast, plt*math.sqrt(alt), fib4))
    print("cutoffs: <1.3 rules out, >2.67 rules in -> indeterminate, elastography decides")
    assert 1.596 < fib4 < 1.599
    assert 1.3 < fib4 < 2.67
    print("rule: read the corrosion from the control room without opening a tank")
    print("OK: %s ran the gauge" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_ga_cancer_upper(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def main():
    # tumor volume scales with diameter^3: 2 cm -> 4 cm
    multiple = (4.0/2.0)**3
    print("tumor 2 cm -> 4 cm: volume multiple (4/2)^3 = %.0fx" % multiple)
    print("TNM: wall depth (T), nodes (N), metastases (M) - M1 ends curative intent")
    assert multiple == 8.0
    print("rule: the cube law is why the inspection schedule cannot slip")
    print("OK: %s measured the mass" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_ga_cancer_crc(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def main():
    # stage I ~90% vs stage IV ~14% five-year survival; FIT 74% on 100 cancers
    gap = 90.0 - 14.0
    detected = 100.0*0.74
    print("stage I ~90%% vs stage IV ~14%%: %.0f-point survival gap" % gap)
    print("FIT on 100 cancers: %.0f detected" % detected)
    assert gap == 76.0
    assert detected == 74.0
    print("rule: the 76-point gap is the screening program's report card")
    print("OK: %s ran the staging" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_ga_cancer_pancliver(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def main():
    # HCC surveillance: 100 cirrhotics x 2 scans/year; Milan: <5 cm single or 3x<3 cm
    scans = 100*2
    print("surveillance load: 100 cirrhotics x 2/year = %d scans" % scans)
    print("Milan criteria: single lesion <5 cm, or up to 3 lesions each <3 cm")
    assert scans == 200
    print("rule: patrol the timber on schedule - anatomy decides detectability")
    print("OK: %s walked the patrol" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_ga_emergencies(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def main():
    # lactate 5 -> 3 mmol/L clearance; thresholds >2 concerning, >4 severe
    clearance = (5.0 - 3.0)/5.0*100.0
    print("lactate 5 -> 3 mmol/L: (5-3)/5 = %.0f %% clearance - resuscitation working" % clearance)
    print("thresholds: >2 mmol/L concerning, >4 severe")
    print("patterns: perforation = rigidity; obstruction = obstipation; ischemia = pain-exam mismatch")
    assert clearance == 40.0
    print("rule: exam plus lactate decide faster than scans - delay kills bowel")
    print("OK: %s triaged the alarms" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_ga_nutrition(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def main():
    # Mifflin-St Jeor (men): 10w + 6.25h - 5a + 5; protein 1.5 g/kg
    w, h, a = 70.0, 175.0, 40.0
    bmr = 10.0*w + 6.25*h - 5.0*a + 5.0
    protein = w*1.5
    print("BMR: 10x%.0f + 6.25x%.0f - 5x%.0f + 5 = %.2f kcal/day" % (w, h, a, bmr))
    print("protein: %.0f kg x 1.5 g/kg = %.0f g/day" % (w, protein))
    assert 1598.7 < bmr < 1598.8
    assert protein == 105.0
    print("rule: fuel from the spec plate, never guessed - and the starved punish enthusiasm")
    print("OK: %s wrote the fueling order" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_ga_pediatric(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def main():
    # per 5000 births: Hirschsprung 1/5000; pyloric stenosis 2/1000
    births = 5000.0
    hirsch = births/5000.0
    pyloric = births*0.002
    print("5000 births: Hirschsprung 5000/5000 = %.0f expected case" % hirsch)
    print("5000 births: pyloric stenosis 5000 x 0.002 = %.0f expected cases" % pyloric)
    assert hirsch == 1.0
    assert pyloric == 10.0
    print("rule: vomiting workup runs pylorus-first - an order of magnitude more common")
    print("OK: %s ran the shakedown" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_ga_future(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def main():
    # CADe: 25% ADR x 1.5 lift; FMT 90 vs vancomycin 30 per 100
    adr_assisted = 25.0*1.5
    gap = 90.0 - 30.0
    print("CADe: 25%% ADR x 1.5 = %.1f %% assisted ADR" % adr_assisted)
    print("recurrent C. difficile: FMT 90 vs vancomycin 30 per 100 -> %.0f-patient gap" % gap)
    assert adr_assisted == 37.5
    assert gap == 60.0
    print("rule: see every fault, miss nothing, manage the ecosystem deliberately")
    print("OK: %s compiled the future" % NAME)
if __name__ == "__main__":
    main()
''')

DEMOS = {
    "what_is": demo_ga_what_is,
    "tract": demo_ga_tract,
    "chemistry": demo_ga_chemistry,
    "gut_wall": demo_ga_gut_wall,
    "liver": demo_ga_liver,
    "pancreas": demo_ga_pancreas,
    "microbiome": demo_ga_microbiome,
    "encounter": demo_ga_encounter,
    "gerd": demo_ga_gerd,
    "dyspepsia": demo_ga_dyspepsia,
    "ulcer": demo_ga_ulcer,
    "ugib": demo_ga_ugib,
    "celiac": demo_ga_celiac,
    "ibs": demo_ga_ibs,
    "motility": demo_ga_motility,
    "crohn": demo_ga_crohn,
    "uc": demo_ga_uc,
    "lgib": demo_ga_lgib,
    "polyps": demo_ga_polyps,
    "endoscopy": demo_ga_endoscopy,
    "endo_therapy": demo_ga_endo_therapy,
    "pancreatitis": demo_ga_pancreatitis,
    "gallstones": demo_ga_gallstones,
    "biliary": demo_ga_biliary,
    "cirrhosis": demo_ga_cirrhosis,
    "hepatitis": demo_ga_hepatitis,
    "nafld": demo_ga_nafld,
    "cancer_upper": demo_ga_cancer_upper,
    "cancer_crc": demo_ga_cancer_crc,
    "cancer_pancliver": demo_ga_cancer_pancliver,
    "emergencies": demo_ga_emergencies,
    "nutrition": demo_ga_nutrition,
    "pediatric": demo_ga_pediatric,
    "future": demo_ga_future,
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
    for slug in ("gastroenterology", "gastroenterology-signature"):
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
