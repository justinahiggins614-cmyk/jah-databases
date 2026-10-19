#!/usr/bin/env python3
"""Build the Pharmaceutical Manufacturing and Quality pair (gap-audit part 2).

Verified 2026-10-17: NO database covers pharmaceutical manufacturing quality
(production controls, batch records, stability, GMP quality systems). Manifest
keyword search (pharmaceutical, GMP, batch record): zero hits. Nearest:
'unsolved-pharmacology-build' is a build dir for pharmacology unsolved problems
(different discipline: drug science vs manufacturing quality). ZERO full-record
coverage of pharma manufacturing quality.

Two NEW databases, 34 ladder-ordered records each:
  pharmaceutical-manufacturing-quality            (public-harvest)
  pharmaceutical-manufacturing-quality-signature  (signature)

Never any website references. No Facebook.
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, "/home/hatch/workspace/jah-databases/code/gapaudit-p2")
import driver
from entries_pharma_quality import ENTRIES

RK = "pharmaceutical quality record"
CIT_PUB = ("Pharmaceutical manufacturing quality (standard references: FDA 21 CFR Part 211 "
           "'Current Good Manufacturing Practice for Finished Pharmaceuticals'; EU Guidelines "
           "to Good Manufacturing Practice; ICH Q1A stability testing; ICH Q2 analytical "
           "validation; ICH Q8 pharmaceutical development; ICH Q9 quality risk management; "
           "ICH Q10 pharmaceutical quality system; United States Pharmacopeia (USP)).")
CIT_SIG = CIT_PUB + " Signature editions are his original Signature treatment of pharma quality."
STANDARDS = ["Quality practice per FDA 21 CFR 211 / ICH Q-series as cited",
             "Teaching-ladder order: foundations, compounded, advanced"]

cfg_pub, cfg_sig = driver.pair_cfgs(
    slug_base="pharmaceutical-manufacturing-quality", name_base="Pharmaceutical Manufacturing and Quality",
    tagline=("Production controls, batch records, stability, and quality systems (GMP): how "
             "medicines are made identically safe every time - from raw materials and batch "
             "records through validation, OOS investigations, and CAPA to sterile manufacture "
             "and inspection readiness, taught progressively along the ladder."),
    record_kind=RK, prefix_pub="JAH-PMQ-", prefix_sig="JAH-PMQS-",
    ai_base="JAH Pharma Quality Archivist",
    role_pub=("pharmaceutical quality archivist - GMP production controls, batch records, "
              "validation, stability, OOS, CAPA, sterile manufacture; teaching progressively "
              "along the ladder from foundations through compounded to advanced; answers from "
              "many angles - definition, example, procedure, math, standards - using only the "
              "system's own archive data"),
    role_sig=("pharmaceutical quality archivist - Signature editions: his original Signature "
              "treatment of pharmaceutical quality, clearly labeled Signature-made and never "
              "presented as authentic public record; teaches progressively along the ladder; "
              "answers from many angles using only the system's own archive data"),
    search_ph="Search GMP, batch record, validation, stability, OOS, CAPA, Cpk...",
    chat_ph="Ask about pharmaceutical quality...",
    archive_topic="pharmaceutical-quality records",
    gen_kind="pharma-quality",
    standards=STANDARDS, cit_pub=CIT_PUB, cit_sig=CIT_SIG,
    hero_pub=("Public records - real, fact-checked pharmaceutical quality: what GMP is, batch "
              "records, identity/strength/quality/purity, raw materials, weighing, formulas, "
              "in-process controls, contamination control, cleaning, personnel, facilities, "
              "documentation, IQ/OQ/PQ, cleaning validation, method validation, stability, "
              "accelerated stability, specifications, OOS investigations, deviations, CAPA, "
              "change control, sampling, environmental monitoring, ICH Q10, process "
              "capability, continued verification, sterile manufacture, containment, data "
              "integrity, batch release, stability-indicating methods, extractables, and "
              "inspection readiness - organized in the Signature system. Every record carries "
              "the full entry: description, how it works, key points, requirements, "
              "standards, citations, and a working demonstration program. Records are ordered "
              "by the teaching ladder: Foundations -> Compounded -> Advanced."),
    hero_sig=("Signature originals - his original Signature treatment of pharmaceutical "
              "manufacturing quality: the full ladder from GMP basics through validation and "
              "stability to sterile manufacture and inspection readiness, reframed as "
              "Signature science. Clearly labeled Signature-made, never presented as "
              "authentic public record. Every record carries the full entry: description, "
              "how it works, key points, requirements, standards, citations, and a working "
              "demonstration program."))

DEMOS = {}


def _reg(key):
    def deco(fn):
        DEMOS[key] = fn
        return fn
    return deco


import json as _json


@_reg("pm_yield")
def d_yield(name, rid, group):
    return driver.demo_hdr(name, rid, group) + '''\
def main():
    # batch yield: actual vs theoretical, with acceptance limits
    theoretical_kg = 100.0
    actual_kg = 97.4
    yield_pct = actual_kg / theoretical_kg * 100.0
    lo, hi = 95.0, 105.0
    print("theoretical %.1f kg, actual %.1f kg -> yield %.1f%%" % (theoretical_kg, actual_kg, yield_pct))
    print("limits %.0f-%.0f%% -> %s" % (lo, hi, "PASS" if lo <= yield_pct <= hi else "FAIL"))
    assert abs(yield_pct - 97.4) < 1e-9
    assert lo <= yield_pct <= hi
    print("OK: %s computed batch yield against limits" % ''' + _json.dumps(name) + ''')
if __name__ == "__main__":
    main()
'''


@_reg("pm_arrhenius")
def d_arrhenius(name, rid, group):
    return driver.demo_hdr(name, rid, group) + '''\
import math
def main():
    # Arrhenius: accelerated 40 C degradation rate -> predicted 25 C shelf life
    # k = A exp(-Ea/RT); ratio k40/k25 from activation energy
    Ea = 80000.0   # J/mol
    R = 8.314
    T_acc = 40.0 + 273.15
    T_rt = 25.0 + 273.15
    ratio = math.exp(-Ea / R * (1.0 / T_acc - 1.0 / T_rt))
    # 6 months at 40 C with 2% degradation -> equivalent real-time months
    months_acc = 6.0
    equiv_months = months_acc * ratio
    print("acceleration factor 40C/25C: %.1fx" % ratio)
    print("6 months accelerated ~= %.1f months real-time" % equiv_months)
    assert 3.0 < ratio < 6.0, ratio
    assert equiv_months > 20.0
    print("OK: %s extrapolated shelf life with Arrhenius kinetics" % ''' + _json.dumps(name) + ''')
if __name__ == "__main__":
    main()
'''


@_reg("pm_cpk")
def d_cpk(name, rid, group):
    return driver.demo_hdr(name, rid, group) + '''\
import statistics
def main():
    # process capability: tablet weights, spec 500 +/- 15 mg
    weights = [501.2, 499.8, 500.5, 502.1, 498.9, 500.3, 501.0, 499.5,
               500.8, 501.5, 499.2, 500.0, 500.6, 499.7, 501.1, 500.4]
    usl, lsl = 515.0, 485.0
    mu = statistics.mean(weights)
    sd = statistics.stdev(weights)
    cpk = min(usl - mu, mu - lsl) / (3.0 * sd)
    print("n=%d mean=%.2f sd=%.3f Cpk=%.2f" % (len(weights), mu, sd, cpk))
    print("Cpk >= 1.33 required -> %s" % ("CAPABLE" if cpk >= 1.33 else "NOT CAPABLE"))
    assert cpk >= 1.33, cpk
    print("OK: %s demonstrated process capability Cpk" % ''' + _json.dumps(name) + ''')
if __name__ == "__main__":
    main()
'''


@_reg("pm_oos")
def d_oos(name, rid, group):
    return driver.demo_hdr(name, rid, group) + '''\
def main():
    # OOS investigation phases (FDA guidance): Phase I lab, Phase II full
    phases = [
        ("Phase Ia", "analyst interview, obvious lab error check"),
        ("Phase Ib", "retest by second analyst if no assignable cause"),
        ("Phase II", "full investigation: manufacturing review, CAPA"),
        ("Phase III", "batch disposition decision with QA"),
    ]
    for ph, desc in phases:
        print("  %-10s %s" % (ph, desc))
    assert [p for p, _ in phases] == ["Phase Ia", "Phase Ib", "Phase II", "Phase III"]
    print("rule: never retest into compliance - every result stands in the record")
    print("OK: %s walked the OOS investigation phases" % ''' + _json.dumps(name) + ''')
if __name__ == "__main__":
    main()
'''


@_reg("pm_sampling")
def d_sampling(name, rid, group):
    return driver.demo_hdr(name, rid, group) + '''\
import math
def main():
    # sampling: how many containers to sample from N (sqrt(N)+1 rule of thumb)
    for N in (100, 400, 1000):
        n = int(math.sqrt(N)) + 1
        print("  lot of %4d containers -> sample %d" % (N, n))
    assert int(math.sqrt(400)) + 1 == 21
    # acceptance sampling: n=20, accept on 0 defectives
    print("acceptance: n=20, c=0 - one defective fails the lot")
    print("OK: %s sized sampling plans for incoming lots" % ''' + _json.dumps(name) + ''')
if __name__ == "__main__":
    main()
'''


@_reg("pm_cleaning")
def d_cleaning(name, rid, group):
    return driver.demo_hdr(name, rid, group) + '''\
def main():
    # MACO: maximum allowable carryover of previous product into next
    # MACO = (therapeutic dose x batch size) / (safety factor x daily dose)
    dose_prev_mg = 10.0        # min therapeutic dose of previous product
    batch_next_kg = 200.0
    safety = 1000.0
    daily_dose_next_mg = 500.0
    maco_mg = dose_prev_mg * (batch_next_kg * 1e6) / (safety * daily_dose_next_mg)
    print("MACO = %.1f mg in next %g kg batch" % (maco_mg, batch_next_kg))
    limit_ppm = maco_mg / (batch_next_kg * 1e6) * 1e6
    print("surface limit equivalent: %.2f ppm" % limit_ppm)
    assert abs(maco_mg - 4000.0) < 1e-9
    print("OK: %s computed a cleaning validation MACO limit" % ''' + _json.dumps(name) + ''')
if __name__ == "__main__":
    main()
'''


@_reg("pm_env")
def d_env(name, rid, group):
    return driver.demo_hdr(name, rid, group) + '''\
import statistics
def main():
    # environmental monitoring: viable air counts, alert/action trending
    counts = [2, 1, 3, 2, 5, 1, 4, 8, 3, 2, 6, 12]  # CFU per sample, monthly
    alert, action = 10, 25
    mu = statistics.mean(counts)
    print("12-month mean %.1f CFU; alert=%d action=%d" % (mu, alert, action))
    over_alert = [c for c in counts if c >= alert]
    over_action = [c for c in counts if c >= action]
    print("alert excursions: %d  action excursions: %d" % (len(over_alert), len(over_action)))
    assert len(over_alert) == 1 and len(over_action) == 0
    # adverse trend: 3 consecutive increases
    trend = any(counts[i] < counts[i+1] < counts[i+2] for i in range(len(counts)-2))
    print("adverse trend detected: %s" % trend)
    print("OK: %s trended environmental monitoring data" % ''' + _json.dumps(name) + ''')
if __name__ == "__main__":
    main()
'''


@_reg("pm_capa")
def d_capa(name, rid, group):
    return driver.demo_hdr(name, rid, group) + '''\
def main():
    # CAPA record lifecycle with effectiveness check
    capa = {"id": "CAPA-2026-014", "source": "deviation DEV-088",
            "root_cause": "weighing procedure ambiguity",
            "actions": ["revise SOP-114", "retrain 12 operators"],
            "effectiveness": "zero repeats in 3 lots post-implementation"}
    stages = ["open", "investigate", "plan", "implement", "effectiveness-check", "close"]
    for i, s in enumerate(stages, 1):
        print("  %d. %s" % (i, s))
    assert capa["effectiveness"].startswith("zero repeats")
    assert len(stages) == 6
    print("CAPA %s closed only after effectiveness proven" % capa["id"])
    print("OK: %s tracked a CAPA to effectiveness-verified closure" % ''' + _json.dumps(name) + ''')
if __name__ == "__main__":
    main()
'''


@_reg("pm_stability")
def d_stability(name, rid, group):
    return driver.demo_hdr(name, rid, group) + '''\
def main():
    # stability trending: assay % over 24 months, spec 95.0-105.0
    months = [0, 3, 6, 9, 12, 18, 24]
    assay = [100.2, 99.8, 99.5, 99.1, 98.8, 98.3, 97.9]
    n = len(months)
    mx, my = sum(months) / n, sum(assay) / n
    slope = sum((x - mx) * (y - my) for x, y in zip(months, assay)) / sum((x - mx) ** 2 for x in months)
    intercept = my - slope * mx
    # extrapolate: when does assay hit 95.0?
    t_95 = (95.0 - intercept) / slope
    print("degradation slope %.3f %%/month; projected 95.0%% at %.1f months" % (slope, t_95))
    assert slope < 0
    assert t_95 > 36.0, t_95
    print("OK: %s trended stability data to a shelf-life projection" % ''' + _json.dumps(name) + ''')
if __name__ == "__main__":
    main()
'''


@_reg("pm_batchrecord")
def d_batchrecord(name, rid, group):
    return driver.demo_hdr(name, rid, group) + '''\
def main():
    # batch record review checklist: every critical element verified
    checklist = [
        ("formula", "quantities match master formula"),
        ("weighing", "second-person verification recorded"),
        ("equipment", "clean/qualified status documented"),
        ("in-process", "all IPC results within limits"),
        ("deviations", "all investigated and closed"),
        ("yield", "within registered limits"),
        ("signatures", "production + QA review complete"),
    ]
    for item, criterion in checklist:
        print("  [x] %-12s %s" % (item, criterion))
    assert len(checklist) == 7
    print("batch released only when every box is honestly checked")
    print("OK: %s executed a batch record review checklist" % ''' + _json.dumps(name) + ''')
if __name__ == "__main__":
    main()
'''


def main():
    return driver.run_pair(HERE, cfg_pub, cfg_sig, ENTRIES, DEMOS)


if __name__ == "__main__":
    sys.exit(0 if main() else 1)
