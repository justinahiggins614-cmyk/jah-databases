#!/usr/bin/env python3
"""Build the Hepatology field databases for JAH Databases (field #39, taxonomy order).

Verified 2026-10-17 (see entries_hepatology.py docstring): NO database
covers hepatology as a clinical specialty (liver, biliary tract, pancreas;
viral/autoimmune hepatitis, cirrhosis, portal hypertension, NAFLD/MASLD,
alcoholic liver disease, cholestasis, liver failure, transplantation, liver
function testing). Clinical-specialty framing, liver-focused, distinct from
gastroenterology (general GI specialty).

Manifest search (2,378 databases): zero 'hepatolog*' slugs/names; no
db/hepatolog* dirs. Whole-system exact-title sweep over the manifest PLUS
all 777 shard index 't' keys: zero collisions for all 34 planned titles x2
editions (68 variants). Near-neighbors confirmed different disciplines:
'gastroenterology' covers the general GI tract (its liver/biliary/pancreas
records are survey-level and all exact-titles were avoided); 'endocrinology'
covers only the hormone system; diabetes coverage is fragmented across
general health databases. ZERO full-record discipline coverage anywhere.

So this build creates two NEW databases, 34 ladder-ordered records each:

  hepatology                 - The Hepatology Database
                               (public-harvest: real, fact-checked clinical
                               hepatology; standard references Feldman et al.
                               "Sleisenger and Fordtran's Gastrointestinal and
                               Liver Disease" 11th ed 2021; Schiff et al.
                               "Schiff's Diseases of the Liver" 12th ed 2018;
                               Jameson et al. "Harrison's Principles of
                               Internal Medicine" 21st ed 2022; AASLD practice
                               guidance: chronic hepatitis B 2018, hepatitis C
                               2018, autoimmune hepatitis 2019, primary biliary
                               cholangitis 2018, NAFLD/MASLD 2023, portal
                               hypertensive bleeding 2016, ascites/SBP/HRS
                               2021, HCC 2018; ACG drug-induced liver injury
                               2021; acute liver failure reviews; MELD and
                               Child-Pugh original papers)
  hepatology-signature       - The Hepatology Signature Database
                                  (his original Signature interpretation of
                                  the liver as the body's chemical refinery
                                  and filter works; src signature, titles
                                  suffixed " (Signature Edition)", never
                                  presented as authentic public record)

34 records each, ordered by the teaching ladder (ladder_rank 1-10,
ladder_tier foundations/compounded/advanced); the shard index is written in
ladder order so pages present simple -> compounded -> complex.

ID prefixes: JAH-HEP- (public) and JAH-HEPS- (signature), both verified free
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
from entries_hepatology import ENTRIES, SIG_TAIL

# ---------------------------------------------------------------- DB config

def _cfg(slug, name, tagline, record_kind, prefix, ai, role, citation, source):
    sig_line = ("Signature originals - his original Signature interpretation of the "
                "liver as the body's chemical refinery and filter works: the hepatocyte "
                "as the process unit, bile as the solvent line, the biliary tree as the "
                "outflow plumbing, fibrosis as scale building up in the filter, cirrhosis "
                "as the clogged refinery, transplantation as the full refinery rebuild. "
                "Clearly labeled Signature-made, never presented as authentic public record.")
    pub_line = ("Public records - real, fact-checked clinical hepatology: the full ladder from "
                "what hepatology is through liver anatomy, the biliary tree, liver physiology, "
                "bilirubin metabolism, liver function testing, and the clinical encounter, "
                "through viral hepatitis, gallstones, pancreatitis, metabolic and autoimmune "
                "liver disease, to cirrhosis, portal hypertension, liver failure, liver cancer, "
                "transplantation, and the future of the field, organized in the "
                "Signature system.")
    ladder = (" Records are ordered by the teaching ladder: Foundations (what hepatology "
              "is, liver anatomy, the biliary tree and pancreatic ducts, liver physiology, "
              "bilirubin metabolism, liver function testing, the hepatology clinical encounter) -> "
              "Compounded (acute viral hepatitis, chronic hepatitis B, gallstone disease, "
              "chronic hepatitis C, autoimmune hepatitis, alcoholic liver disease, acute "
              "pancreatitis, metabolic liver disease, drug-induced liver injury, cholestatic "
              "liver disease, chronic pancreatitis) -> Advanced (cirrhosis, portal hypertension, "
              "acute liver failure, liver biopsy and elastography, ERCP and biliary endoscopy, "
              "hepatic encephalopathy, ascites and spontaneous bacterial peritonitis, "
              "hepatorenal syndrome, the MELD and Child-Pugh scores, hepatocellular carcinoma, "
              "cholangiocarcinoma, pancreatic cancer, liver transplantation, pediatric "
              "hepatology, pregnancy and the liver, the future of hepatology).")
    return {
        "name": name, "tagline": tagline, "record_kind": record_kind,
        "prefix": prefix, "ai": ai, "role": role,
        "hero_p": "%s - %s Every record carries the full entry: description, how it works, "
                  "key points, requirements, standards, citations, and a working demonstration "
                  "program.%s" % (tagline, sig_line if source == "signature" else pub_line, ladder),
        "sig_type": ("Signature originals organized in the Signature system"
                     if source == "signature" else
                     "Public records organized in the Signature system"),
        "search_ph": "Search hepatitis, cirrhosis, jaundice, MELD, varices, HCC, transplant, PBC, PSC, MASLD, ERCP, ascites, encephalopathy...",
        "chat_ph": "Ask about hepatology...",
        "archive_blurb": ("Seeded %s hepatology records, marching toward one million records. "
                          "Presented in teaching-ladder order: foundations, compounded, advanced."
                          % ("Signature-original" if source == "signature" else "public-record")),
        "schema": ("id, t, g, name, title, description, how_it_works, key_points, requirements, "
                   "standards, citations, src, ladder_rank, ladder_tier, demo"),
        "fields": "Foundations \u00b7 Compounded \u00b7 Advanced - each tier opens on demand and loads only what you open",
        "gen_desc": "Generate clearly-labeled hepatology studies. Seeded archive records are the authoritative entries.",
        "greet": "I am the %s. Ask me about hepatology - from what it is through liver anatomy, "
        "the biliary tree, liver physiology, bilirubin metabolism, liver function testing, and "
        "the clinical encounter, through viral hepatitis, gallstones, pancreatitis, autoimmune "
        "and metabolic liver disease, to cirrhosis, portal hypertension, liver failure, liver "
        "cancer, transplantation, and the future of the field." % ai,
        "gen_fields": ["Foundations", "Compounded", "Advanced"],
        "gen_kind": "hepatology-study", "gen_demo_kind": "hepatology-demo",
        "source": source,
    }

CIT_PUB = ("Hepatology (standard references: Feldman et al. Sleisenger and Fordtran's "
           "Gastrointestinal and Liver Disease 11th ed 2021; Schiff et al. Schiff's "
           "Diseases of the Liver 12th ed 2018; Jameson et al. Harrison's Principles of "
           "Internal Medicine 21st ed 2022; AASLD hepatitis B 2018, hepatitis C 2018, "
           "autoimmune hepatitis 2019, primary biliary cholangitis 2018, NAFLD/MASLD "
           "2023, portal hypertensive bleeding 2016, ascites/SBP/HRS 2021, HCC 2018 "
           "guidance; ACG drug-induced liver injury 2021; acute liver failure reviews; "
           "MELD and Child-Pugh original papers).")
CIT_SIG = CIT_PUB + (" Signature editions are his original Signature interpretation "
                     "of the liver as the body's chemical refinery and filter works, "
                     "clearly labeled Signature-made.")

DBCFG = {}
DBCFG["hepatology"] = _cfg(
    "hepatology", "The Hepatology Database",
    "Real, fact-checked clinical hepatology: from what hepatology is through liver "
    "anatomy, the biliary tree and pancreatic ducts, liver physiology, bilirubin "
    "metabolism, liver function testing, and the clinical encounter, through acute "
    "viral hepatitis, chronic hepatitis B, gallstone disease, chronic hepatitis C, "
    "autoimmune hepatitis, alcoholic liver disease, acute pancreatitis, metabolic "
    "liver disease, drug-induced liver injury, cholestatic liver disease, and chronic "
    "pancreatitis, to cirrhosis, portal hypertension, acute liver failure, liver biopsy "
    "and elastography, ERCP and biliary endoscopy, hepatic encephalopathy, ascites and "
    "spontaneous bacterial peritonitis, hepatorenal syndrome, the MELD and Child-Pugh "
    "scores, hepatocellular carcinoma, cholangiocarcinoma, pancreatic cancer, liver "
    "transplantation, pediatric hepatology, pregnancy and the liver, and the future of "
    "hepatology - taught progressively along the ladder.",
    "hepatology record", "JAH-HEP-", "JAH Hepatology Archivist",
    "hepatology archivist - clinical hepatology: liver, biliary tract, pancreas; "
    "hepatitis, cirrhosis, portal hypertension, cholestasis, liver failure, "
    "transplantation, pancreatic disease; teaching progressively along the ladder "
    "from foundations through compounded to advanced; answers from many angles - "
    "definition, example, analogy, application, history, math, how-to - using only "
    "archive data from this system",
    CIT_PUB, "public")
DBCFG["hepatology-signature"] = _cfg(
    "hepatology-signature", "The Hepatology Signature Database",
    "His original Signature interpretation of the liver as the body's chemical "
    "refinery and filter works: the full ladder from what hepatology is through liver "
    "anatomy, the biliary tree, physiology, bilirubin, testing, and the clinical "
    "encounter, through hepatitis, gallstones, pancreatitis, and metabolic liver "
    "disease, to cirrhosis, portal hypertension, liver failure, liver cancer, "
    "transplantation, and the future of the field, reframed as Signature science. "
    "Clearly labeled Signature-made, never presented as authentic public record.",
    "hepatology record", "JAH-HEPS-", "JAH Hepatology Archivist (Signature)",
    "hepatology archivist - Signature editions: his original Signature interpretation "
    "of the liver as the bodily chemical refinery and filter works, clearly "
    "labeled Signature-made and never presented as authentic public record; teaches "
    "progressively along the ladder from foundations through compounded to advanced; "
    "answers from many angles - definition, example, analogy, application, history, "
    "math, how-to - using only archive data from this system",
    CIT_SIG, "signature")

base.DBCFG = DBCFG

# ---------------------------------------------------------------- demos
# Every demo is real, runnable, stdlib-only Python performing the actual
# hepatology computation for its record. All are machine-executed by main().

_PREAMBLE = (
"import math\n"
)

def _wrap(name, rid, group, body):
    return (base._hdr(name, rid, group) + _PREAMBLE + body.replace("NAME", json.dumps(name)))

def demo_he_what_is(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # the refinery at scale: mass share, blood-flow share, daily bile
    body_kg, liver_kg = 70.0, 1.5
    share = liver_kg / body_kg * 100.0
    cardiac = 5.0  # L/min resting cardiac output
    hepatic_flow = cardiac * 0.25  # ~25% of cardiac output
    bile_ml_day = 600.0
    bile_l_year = bile_ml_day * 365.0 / 1000.0
    print("liver mass: %.1f kg of %.0f kg = %.2f %% of body mass" % (liver_kg, body_kg, share))
    print("hepatic blood flow: 25 %% of %.1f L/min = %.2f L/min" % (cardiac, hepatic_flow))
    print("bile output: %.0f mL/day -> %.1f L/year" % (bile_ml_day, bile_l_year))
    assert 2.14 < share < 2.15
    assert 1.24 < hepatic_flow < 1.26
    assert 218.9 < bile_l_year < 219.1
    print("rule: the biggest internal organ runs the biggest chemistry")
    print("OK: %s sized the refinery" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_he_liver_anatomy(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # Couinaud segments as shares of total liver volume
    segments = {"1": 4.0, "2": 10.0, "3": 12.0, "4": 14.0,
                "5": 12.0, "6": 14.0, "7": 16.0, "8": 18.0}
    total = sum(segments.values())
    right_lobe = sum(segments[s] for s in ("5", "6", "7", "8"))
    print("Couinaud segments 1-8 sum to %.1f %%" % total)
    print("right lobe (segments 5-8): %.1f %% of liver volume" % right_lobe)
    assert 99.9 < total < 100.1
    assert 59.9 < right_lobe < 60.1
    print("rule: eight independent modules, each resectable on its own")
    print("OK: %s mapped the segments" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_he_biliary_tree(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # duct caliber: normal vs dilated; daily bile volume through the pipes
    normal_max = 6.0  # mm
    readings = [4.2, 5.8, 9.5]
    dilated = [r for r in readings if r > normal_max]
    bile_ml_day = 600.0
    per_hour = bile_ml_day / 24.0
    print("CBD readings (mm): %s; normal max %.1f" % (readings, normal_max))
    print("dilated: %s -> obstruction workup" % dilated)
    print("bile flow: %.0f mL/day = %.1f mL/hour" % (bile_ml_day, per_hour))
    assert dilated == [9.5]
    assert 24.9 < per_hour < 25.1
    print("rule: a dilated main means a blockage downstream")
    print("OK: %s read the pipe gauges" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_he_liver_physiology(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # first-pass flow: portal vein ~75%, hepatic artery ~25%
    cardiac = 5.0  # L/min
    portal = cardiac * 0.75
    arterial = cardiac * 0.25
    per_day = (portal + arterial) * 60.0 * 24.0
    print("portal vein: %.2f L/min; hepatic artery: %.2f L/min" % (portal, arterial))
    print("blood through the refinery per day: %.0f L" % per_day)
    assert 3.74 < portal < 3.76
    assert 1.24 < arterial < 1.26
    assert 7199.0 < per_day < 7201.0
    print("rule: every meal passes the gates before reaching the town")
    print("OK: %s timed the feedstock" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_he_bilirubin(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # 1 mg/dL = 17.1 micromol/L: the core conversion of the liver panel
    factor = 17.1
    normal_top = 1.2 * factor
    visible = 3.0 * factor
    print("upper limit of normal: 1.2 mg/dL = %.2f micromol/L" % normal_top)
    print("visible jaundice threshold: 3.0 mg/dL = %.2f micromol/L" % visible)
    assert 20.51 < normal_top < 20.53
    assert 51.29 < visible < 51.31
    print("rule: read the tag to find which station jammed")
    print("OK: %s converted the pigment" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_he_lft(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # R ratio = (ALT/ULN) / (ALP/ULN): >5 hepatocellular, <2 cholestatic
    alt, alt_uln = 800.0, 40.0
    alp, alp_uln = 120.0, 120.0
    r = (alt / alt_uln) / (alp / alp_uln)
    pattern = "hepatocellular" if r > 5 else ("cholestatic" if r < 2 else "mixed")
    print("ALT %.0f/%.0f, ALP %.0f/%.0f -> R = %.1f -> %s pattern"
          % (alt, alt_uln, alp, alp_uln, r, pattern))
    assert 19.9 < r < 20.1
    assert pattern == "hepatocellular"
    print("rule: read the pattern first, the numbers second")
    print("OK: %s read the gauge board" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_he_encounter(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # the fraction split: direct/total decides the workup branch
    total, direct = 10.0, 8.0
    frac = direct / total * 100.0
    branch = "cholestatic workup" if frac >= 50.0 else "hemolytic/unconjugated workup"
    print("bilirubin total %.1f, direct %.1f -> direct fraction %.1f %%"
          % (total, direct, frac))
    print("branch: %s, then ultrasound for duct dilation" % branch)
    assert 79.9 < frac < 80.1
    assert branch == "cholestatic workup"
    print("rule: fraction first, image second")
    print("OK: %s worked the jaundice case" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_he_acute_hep(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # incubation windows in days: which virus fits the exposure interval?
    windows = {"A": (15, 50), "B": (45, 160), "C": (14, 180),
               "D": (21, 90), "E": (15, 60)}
    mid = {k: (a + b) / 2.0 for k, (a, b) in windows.items()}
    print("incubation midpoints (days): " +
          ", ".join("%s=%.0f" % (k, mid[k]) for k in ("A", "B", "C", "D", "E")))
    interval = 33  # exposure to illness
    fits = [k for k, (a, b) in windows.items() if a <= interval <= b]
    print("illness %d days after exposure fits viruses: %s" % (interval, fits))
    assert 32.4 < mid["A"] < 32.6
    assert 102.4 < mid["B"] < 102.6
    assert fits == ["A", "C", "D", "E"]
    print("rule: route, incubation, serology - the field guide in three")
    print("OK: %s timed the five viruses" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_he_hbv(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # log-kill: baseline DNA to suppressed DNA on antivirals
    baseline = 1.58e8  # IU/mL
    post = 20.0
    log_base = math.log10(baseline)
    log_post = math.log10(post)
    drop = log_base - log_post
    print("HBV DNA: %.2e IU/mL = %.2f log -> %.1f IU/mL = %.2f log"
          % (baseline, log_base, post, log_post))
    print("log reduction on therapy: %.2f logs" % drop)
    assert 8.19 < log_base < 8.21
    assert 6.89 < drop < 6.91
    print("rule: suppression by logs, not eradication - cccDNA persists")
    print("OK: %s measured the log-kill" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_he_gallstones(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # cumulative stone risk from a 1%/year incidence over a decade
    annual = 0.01
    years = 10
    cum = 1.0 - (1.0 - annual) ** years
    print("annual incidence %.0f %%, %d-year cumulative risk: %.2f %%"
          % (annual * 100.0, years, cum * 100.0))
    assert 0.095 < cum < 0.097
    print("rule: silent stones are left alone; the ladder decides the rest")
    print("OK: %s weighed the odds" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_he_hcv(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # cure arithmetic: P(at least 19 of 20 cured) at 96% SVR
    p, n = 0.96, 20
    prob = sum(math.comb(n, k) * p ** k * (1 - p) ** (n - k) for k in (19, 20))
    print("per-patient SVR %.0f %% -> P(>=19/20 cured) = %.4f"
          % (p * 100.0, prob))
    assert 0.80 < prob < 0.82
    print("rule: triple blockade leaves the virus no escape")
    print("OK: %s counted the cures" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_he_aih(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # simplified IAIHG score: ANA 1:160 (2) + IgG 1.3xULN (2)
    # + typical histology (2) + viral absent (2) = 8 -> definite
    score = 2 + 2 + 2 + 2
    verdict = "definite" if score >= 7 else ("probable" if score >= 6 else "unlikely")
    print("AIH score components: 2+2+2+2 = %d -> %s AIH" % (score, verdict))
    assert score == 8
    assert verdict == "definite"
    print("rule: score it, do not guess it")
    print("OK: %s scored the case" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_he_ald(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # Maddrey discriminant function = 4.6*(PT - control) + bilirubin; >=32 severe
    pt, control, bili = 22.0, 12.0, 12.0
    df = 4.6 * (pt - control) + bili
    severe = df >= 32.0
    print("Maddrey DF = 4.6*(%.0f-%.0f) + %.0f = %.1f -> severe: %s"
          % (pt, control, bili, df, severe))
    assert 57.9 < df < 58.1
    assert severe
    print("rule: past 32, the plant is failing fast enough for steroids")
    print("OK: %s gauged the damage" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_he_acute_panc(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # diagnostic rule: lipase > 3x ULN
    lipase, uln = 900.0, 160.0
    fold = lipase / uln
    print("lipase %.0f IU/L / ULN %.0f = %.2fx upper limit" % (lipase, uln, fold))
    assert 5.62 < fold < 5.63
    assert fold > 3.0
    print("rule: three times normal means breach confirmed")
    print("OK: %s read the leak detector" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_he_masld_meta(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # FIB-4 = age*AST / (platelets * sqrt(ALT)); <1.3 low, >2.67 high
    age, ast, alt, plt = 50.0, 55.0, 60.0, 200.0
    fib4 = age * ast / (plt * math.sqrt(alt))
    band = "low" if fib4 < 1.3 else ("high" if fib4 > 2.67 else "indeterminate")
    print("FIB-4 = %.0f*%.0f/(%.0f*sqrt(%.0f)) = %.2f -> %s risk"
          % (age, ast, plt, alt, fib4, band))
    assert 1.77 < fib4 < 1.79
    assert band == "indeterminate"
    print("rule: fibrosis stage, not fat amount, predicts outcomes")
    print("OK: %s triaged the case" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_he_dili(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # Hy's law: ALT >3x + bilirubin >2x (ALP <2x) -> ~10% fatality signal
    alt_x = 450.0 / 40.0
    bili_x = 3.0 / 1.2
    alp_x = 150.0 / 120.0
    hys = alt_x > 3.0 and bili_x > 2.0 and alp_x < 2.0
    print("ALT %.2fx, bilirubin %.2fx, ALP %.2fx -> Hy's law met: %s"
          % (alt_x, bili_x, alp_x, hys))
    assert 11.24 < alt_x < 11.26
    assert hys
    print("rule: ruptured units plus failed export means one in ten")
    print("OK: %s applied Hys law" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_he_cholestatic(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # cholestatic pattern: high ALP multiple, R ratio < 2
    alp_x = 380.0 / 120.0
    alt_x = 90.0 / 40.0
    r = alt_x / alp_x
    print("ALP %.2fx ULN, R ratio = %.2f -> cholestatic pattern: %s"
          % (alp_x, r, r < 2.0))
    assert 3.16 < alp_x < 3.17
    assert 0.70 < r < 0.72
    assert r < 2.0
    print("rule: small ducts or large ducts - the pattern is shared")
    print("OK: %s read the cholestasis" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_he_chronic_panc(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # enzyme replacement: lipase units across meals and snacks
    meals = [75000, 75000, 75000]
    snacks = [25000, 25000]
    total = sum(meals + snacks)
    print("3 meals x 75k + 2 snacks x 25k = %d lipase units/day" % total)
    assert total == 275000
    print("rule: outsource digestion - dose to the meal, take during it")
    print("OK: %s dosed the enzymes" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_he_cirrhosis(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # elastography bands in kPa
    def band(kpa):
        if kpa < 7.0:
            return "normal"
        if kpa < 9.5:
            return "significant fibrosis"
        if kpa < 12.5:
            return "advanced fibrosis"
        return "cirrhosis"
    readings = [5.2, 8.8, 11.0, 16.2]
    bands = [band(r) for r in readings]
    for r, b in zip(readings, bands):
        print("  %.1f kPa -> %s" % (r, b))
    assert bands == ["normal", "significant fibrosis", "advanced fibrosis", "cirrhosis"]
    print("rule: compensated runs derated; decompensation starts the clock")
    print("OK: %s staged the scar" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_he_portal_htn(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # HVPG = wedged - free; >=10 significant, >=12 bleed territory
    wedged, free = 22.0, 8.0
    hvpg = wedged - free
    if hvpg >= 12.0:
        status = "variceal bleeding risk"
    elif hvpg >= 10.0:
        status = "clinically significant portal hypertension"
    else:
        status = "normal"
    print("HVPG = %.0f - %.0f = %.1f mmHg -> %s" % (wedged, free, hvpg, status))
    assert 13.9 < hvpg < 14.1
    assert status == "variceal bleeding risk"
    print("rule: past 12, the relief valves can blow")
    print("OK: %s read the gradient" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_he_alf(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # Kings College (acetaminophen): pH < 7.30 after resuscitation,
    # or INR > 6.5 + creatinine > 3.4 + grade 3-4 encephalopathy
    ph, inr, creat, enceph = 7.28, 7.0, 3.8, 4
    meets = (ph < 7.30) or (inr > 6.5 and creat > 3.4 and enceph >= 3)
    print("pH %.2f, INR %.1f, creatinine %.1f, encephalopathy grade %d"
          % (ph, inr, creat, enceph))
    print("Kings College criteria met: %s -> status 1A listing" % meets)
    assert meets
    print("rule: past the gauges, the only exit is a new liver")
    print("OK: %s made the listing call" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_he_biopsy(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # adequacy: >= 20 mm core with >= 11 portal tracts
    length_mm, tracts = 24.0, 13
    adequate = length_mm >= 20.0 and tracts >= 11
    print("core %.0f mm, %d portal tracts -> adequate: %s"
          % (length_mm, tracts, adequate))
    assert adequate
    print("rule: drill only when the gauges disagree")
    print("OK: %s checked the core" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_he_ercp(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # drainage arithmetic: bilirubin before and after stenting
    pre, post = 12.0, 3.0
    drop = (pre - post) / pre * 100.0
    print("bilirubin %.1f -> %.1f mg/dL after stenting: %.1f %% drop"
          % (pre, post, drop))
    assert 74.9 < drop < 75.1
    print("rule: diagnose with the camera outside; send the robot to fix")
    print("OK: %s measured the drainage" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_he_he(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # West Haven grades 0-4
    grades = {0: "inattention, sleep inversion",
              1: "trivial lack of awareness",
              2: "lethargy, asterixis",
              3: "stupor, confusion",
              4: "coma"}
    case = 2
    print("West Haven grade %d: %s" % (case, grades[case]))
    assert grades[case] == "lethargy, asterixis"
    print("rule: hunt the precipitant - the bleed, the bug, the drug")
    print("OK: %s graded the episode" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_he_ascites(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # SAAG = serum albumin - ascitic albumin; >= 1.1 = portal hypertension
    serum, ascitic = 3.2, 1.8
    saag = serum - ascitic
    cause = "portal hypertension" if saag >= 1.1 else "non-portal cause"
    print("SAAG = %.1f - %.1f = %.2f g/dL -> %s" % (serum, ascitic, saag, cause))
    assert 1.39 < saag < 1.41
    assert cause == "portal hypertension"
    print("rule: a wide gradient proves the weeping is pressure-driven")
    print("OK: %s tapped the case" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_he_hrs(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # ICA-AKI: creatinine up >= 0.3 mg/dL in 48h or >= 50% in 7 days
    base, peak = 0.9, 1.5
    rise = peak - base
    pct = rise / base * 100.0
    aki = rise >= 0.3 or pct >= 50.0
    print("creatinine %.1f -> %.1f: rise %.1f mg/dL (%.1f %%) -> AKI: %s"
          % (base, peak, rise, pct, aki))
    assert 66.6 < pct < 66.7
    assert aki
    print("rule: the kidneys are victims, not culprits - fix the pressure lie")
    print("OK: %s caught the AKI" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_he_meld(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # MELD = 3.78 ln(bili) + 11.2 ln(INR) + 9.57 ln(creat) + 6.43
    bili, inr, creat = 2.5, 1.8, 1.4
    meld = (3.78 * math.log(bili) + 11.2 * math.log(inr)
            + 9.57 * math.log(creat) + 6.43)
    print("bili %.1f, INR %.1f, creat %.1f -> MELD %.1f (rounds to %d)"
          % (bili, inr, creat, meld, round(meld)))
    assert 19.6 < meld < 19.8
    assert round(meld) == 20
    print("rule: the most failing first - no politics, just the math")
    print("OK: %s ran the triage equation" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_he_hcc(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # Milan: single <= 5 cm, or up to 3 nodules each <= 3 cm
    def milan(nodules):
        if len(nodules) == 1:
            return nodules[0] <= 5.0
        return len(nodules) <= 3 and all(n <= 3.0 for n in nodules)
    cases = [([2.8, 2.1], True), ([5.5], False), ([3.5, 2.0], False)]
    for nodules, expected in cases:
        got = milan(nodules)
        print("  nodules %s cm -> Milan: %s" % (nodules, got))
        assert got == expected
    print("rule: catch it small on surveillance, or the window closes")
    print("OK: %s applied Milan" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_he_cholangio(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # anatomic distribution: perihilar (Klatskin) is the commonest
    total, perihilar = 100, 55
    share = perihilar / total * 100.0
    print("perihilar share of %d cholangiocarcinomas: %.1f %%" % (total, share))
    assert 54.9 < share < 55.1
    print("rule: chronic irritation sands the same section for years")
    print("OK: %s mapped the ductal cancers" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_he_panc_cancer(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # resectability: no arterial involvement, venous <= 180 degrees
    def resectable(arterial, venous_deg):
        return (not arterial) and venous_deg <= 180
    cases = [(False, 90, True), (True, 0, False), (False, 270, False)]
    for art, deg, expected in cases:
        got = resectable(art, deg)
        print("  arterial=%s venous=%d deg -> resectable: %s" % (art, deg, got))
        assert got == expected
    print("rule: anatomy, not size, decides the verdict")
    print("OK: %s judged resectability" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_he_transplant(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # ABO compatibility: donor -> acceptable recipients
    compat = {"O": {"O", "A", "B", "AB"}, "A": {"A", "AB"},
              "B": {"B", "AB"}, "AB": {"AB"}}
    print("donor O -> %s" % sorted(compat["O"]))
    assert "A" in compat["O"] and "AB" in compat["A"]
    assert "A" not in compat["B"]
    assert compat["AB"] == {"AB"}
    print("rule: the queue is ordered by need, the match by blood")
    print("OK: %s matched the matrix" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_he_pediatric(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # the Kasai clock: optimal window closes at 60 days
    present_day, limit = 42, 60
    remaining = limit - present_day
    print("biliary atresia presents day %d; optimal Kasai window: %d days"
          % (present_day, limit))
    print("days remaining in the optimal window: %d" % remaining)
    assert remaining == 18
    assert remaining <= 18
    print("rule: jaundice past two weeks is never watched, it is worked up")
    print("OK: %s beat the clock" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_he_pregnancy(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # Mississippi HELLP classes by platelet count per microliter
    def hellp_class(plt):
        if plt < 50000:
            return 1
        if plt < 100000:
            return 2
        return 3
    cases = [(45000, 1), (80000, 2), (120000, 3)]
    for plt, expected in cases:
        got = hellp_class(plt)
        print("  platelets %d -> Mississippi class %d" % (plt, got))
        assert got == expected
    print("rule: a sick liver in late pregnancy is delivered, not debated")
    print("OK: %s classified HELLP" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_he_future(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\
def main():
    # demand projection: 3% annual growth on a 12,000 waitlist over 10 years
    base, rate, years = 12000.0, 0.03, 10
    proj = base * (1.0 + rate) ** years
    print("waitlist %.0f at %.0f %%/yr for %d yr -> %.0f"
          % (base, rate * 100.0, years, proj))
    assert 16126.0 < proj < 16128.0
    print("rule: the organ shortage is the engine of the engineering")
    print("OK: %s projected the demand" % NAME)
if __name__ == "__main__":
    main()
''')

DEMOS = {
    "what_is": demo_he_what_is,
    "liver_anatomy": demo_he_liver_anatomy,
    "biliary_tree": demo_he_biliary_tree,
    "liver_physiology": demo_he_liver_physiology,
    "bilirubin": demo_he_bilirubin,
    "lft": demo_he_lft,
    "encounter": demo_he_encounter,
    "acute_hep": demo_he_acute_hep,
    "hbv": demo_he_hbv,
    "gallstones": demo_he_gallstones,
    "hcv": demo_he_hcv,
    "aih": demo_he_aih,
    "ald": demo_he_ald,
    "acute_panc": demo_he_acute_panc,
    "masld_meta": demo_he_masld_meta,
    "dili": demo_he_dili,
    "cholestatic": demo_he_cholestatic,
    "chronic_panc": demo_he_chronic_panc,
    "cirrhosis": demo_he_cirrhosis,
    "portal_htn": demo_he_portal_htn,
    "alf": demo_he_alf,
    "biopsy": demo_he_biopsy,
    "ercp": demo_he_ercp,
    "he": demo_he_he,
    "ascites": demo_he_ascites,
    "hrs": demo_he_hrs,
    "meld": demo_he_meld,
    "hcc": demo_he_hcc,
    "cholangio": demo_he_cholangio,
    "panc_cancer": demo_he_panc_cancer,
    "transplant": demo_he_transplant,
    "pediatric": demo_he_pediatric,
    "pregnancy": demo_he_pregnancy,
    "future": demo_he_future,
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
    for slug in ("hepatology", "hepatology-signature"):
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
