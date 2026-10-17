#!/usr/bin/env python3
"""Build the Endocrinology field databases for JAH Databases (field #37, taxonomy order).

Verified 2026-10-17 (see entries_endocrinology.py docstring): NO database
covers endocrinology as a clinical specialty (hypothalamic-pituitary axes,
thyroid, adrenal, pancreatic/diabetes, calcium-PTH-vitamin D, reproductive
endocrinology, neuroendocrinology, endocrine tumors, hormone assays and
dynamic testing).

Manifest search (2,374 databases): zero 'endocrinolog*' slugs/names; no
db/endocrinolog* dirs. Whole-system exact-title sweep over the dedupe gate:
zero collisions for all 34 planned titles x2 editions (68 variants).
Near-neighbors confirmed different disciplines: 'biochemistry' (molecular
mechanisms), 'physiology' (general body function), 'embryology' (has only
an 'endocrine development' organogenesis record), diabetes coverage is
fragmented across general health databases. ZERO full-record discipline
coverage anywhere.

So this build creates two NEW databases, 34 ladder-ordered records each:

  endocrinology              - The Endocrinology Database
                               (public-harvest: real, fact-checked clinical
                               endocrinology; standard references Melmed et al.
                               'Williams Textbook of Endocrinology' 15th ed
                               2024; Gardner/Shoback "Greenspan's Basic &
                               Clinical Endocrinology" 11th ed 2022; Jameson et
                               al. "Harrison's Principles of Internal Medicine"
                               21st ed 2022; ADA Standards of Care in Diabetes
                               2024; ATA hyperthyroidism and thyroid nodule
                               guidelines)
  endocrinology-signature    - The Endocrinology Signature Database
                               (his original Signature interpretation of the
                               hormone system as the body's chemical command
                               network; src signature, titles suffixed
                               " (Signature Edition)", never presented as
                               authentic public record)

34 records each, ordered by the teaching ladder (ladder_rank 1-10,
ladder_tier foundations/compounded/advanced); the shard index is written in
ladder order so pages present simple -> compounded -> complex.

ID prefixes: JAH-ENR- (public) and JAH-ENS- (signature). JAH-END- was
unavailable (taken by an earlier database), so endocrinology takes JAH-ENR-
and the signature edition takes JAH-ENS-; both verified free in the manifest
and in every shard index.

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
from entries_endocrinology import ENTRIES, SIG_TAIL

# ---------------------------------------------------------------- DB config

def _cfg(slug, name, tagline, record_kind, prefix, ai, role, citation, source):
    sig_line = ("Signature originals - his original Signature interpretation of the hormone system as the "
                "chemical command network of the body: every axis a control loop, every gland a "
                "transmitter, every hormone a signed message. Clearly "
                "labeled Signature-made, never presented as authentic public record.")
    pub_line = ("Public records - real, fact-checked clinical endocrinology: the full ladder from "
                "what endocrinology is through the axes, glands, feedback loops, and disorders, "
                "organized in the Signature system.")
    ladder = (" Records are ordered by the teaching ladder: Foundations (what endocrinology "
              "is, the endocrine system, hormone classes, receptors, the hypothalamus, the pituitary, "
              "negative feedback, hormone synthesis and secretion, hormone assays, half-lives) -> "
              "Compounded (growth hormone axis, thyroid axis, thyroid disorders, adrenal cortex, "
              "adrenal medulla, cortisol disorders, glucose control, diabetes) -> Advanced (calcium "
              "homeostasis, male and female reproductive endocrinology, posterior pituitary, "
              "neuroendocrinology, endocrine tumors, PCOS, thyroid nodules and cancer, pituitary "
              "tumors, dynamic testing, congenital adrenal hyperplasia, obesity and metabolic "
              "syndrome, therapeutic hormones, pediatric endocrinology, endocrine emergencies, "
              "the future of hormone medicine).")
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
        "chat_ph": "Ask about endocrinology...",
        "archive_blurb": ("Seeded %s endocrinology records, marching toward one million records. "
                          "Presented in teaching-ladder order: foundations, compounded, advanced."
                          % ("Signature-original" if source == "signature" else "public-record")),
        "schema": ("id, t, g, name, title, description, how_it_works, key_points, requirements, "
                   "standards, citations, src, ladder_rank, ladder_tier, demo"),
        "fields": "Foundations \u00b7 Compounded \u00b7 Advanced - each tier opens on demand and loads only what you open",
        "gen_desc": "Generate clearly-labeled endocrinology studies. Seeded archive records are the authoritative entries.",
        "greet": "I am the %s. Ask me about endocrinology - from what it is through the endocrine "
        "system, hormone classes, receptors, the hypothalamus, the pituitary, negative feedback, "
        "hormone synthesis and testing, through the growth hormone and thyroid axes, the adrenals, "
        "glucose control and diabetes, to calcium, reproductive endocrinology, neuroendocrinology, "
        "endocrine tumors, and hormone therapy." % ai,
        "gen_fields": ["Foundations", "Compounded", "Advanced"],
        "gen_kind": "endocrinology-study", "gen_demo_kind": "endocrinology-demo",
        "source": source,
    }

CIT_PUB = ("Endocrinology (standard references: Melmed et al. Williams Textbook of "
           "Endocrinology 15th ed 2024; Gardner/Shoback Greenspan's Basic & Clinical "
           "Endocrinology 11th ed 2022; Jameson et al. Harrison's Principles of Internal "
           "Medicine 21st ed 2022; American Diabetes Association Standards of Care in "
           "Diabetes 2024; Ross et al. 2016 ATA Hyperthyroidism Guidelines; Haugen et al. "
           "2015 ATA Thyroid Nodule/DTC Guidelines).")
CIT_SIG = CIT_PUB + (" Signature editions are his original Signature interpretation "
                     "of the hormone system as the body's chemical command network, "
                     "clearly labeled Signature-made.")

DBCFG = {}
DBCFG["endocrinology"] = _cfg(
    "endocrinology", "The Endocrinology Database",
    "Real, fact-checked clinical endocrinology: from what endocrinology is through "
    "the endocrine system, hormone classes, receptors, the hypothalamus, the pituitary, "
    "negative feedback, hormone synthesis and secretion, hormone assays, and half-lives, "
    "through the growth hormone axis, the thyroid axis, thyroid disorders, the adrenal "
    "cortex and medulla, cortisol disorders, glucose control, and diabetes, to calcium "
    "homeostasis, male and female reproductive endocrinology, the posterior pituitary, "
    "neuroendocrinology, endocrine tumors, PCOS, thyroid nodules and cancer, pituitary "
    "tumors, dynamic testing, congenital adrenal hyperplasia, obesity and metabolic "
    "syndrome, therapeutic hormones, pediatric endocrinology, endocrine emergencies, "
    "and the future of hormone medicine - taught progressively along the ladder.",
    "endocrinology record", "JAH-ENR-", "JAH Endocrinology Archivist",
    "endocrinology archivist - clinical endocrinology: hypothalamic-pituitary axes, "
    "thyroid, adrenal, pancreatic and diabetes, calcium-PTH-vitamin D, reproductive "
    "endocrinology, neuroendocrinology, endocrine tumors, hormone assays and dynamic "
    "testing; teaching progressively along the ladder from foundations through "
    "compounded to advanced; answers from many angles - definition, example, analogy, "
    "application, history, math, how-to - using only archive data from this system",
    CIT_PUB, "public")
DBCFG["endocrinology-signature"] = _cfg(
    "endocrinology-signature", "The Endocrinology Signature Database",
    "His original Signature interpretation of the hormone system as the chemical "
    "command network of the body: the full ladder from what endocrinology is through "
    "the axes, glands, feedback loops, and disorders to therapeutic hormones and the "
    "future of hormone medicine, reframed as Signature science. Clearly labeled "
    "Signature-made, never presented as authentic public record.",
    "endocrinology record", "JAH-ENS-", "JAH Endocrinology Archivist (Signature)",
    "endocrinology archivist - Signature editions: his original Signature "
    "interpretation of the hormone system as the chemical command network of the body, "
    "clearly labeled Signature-made and never presented as authentic public record; "
    "teaches progressively along the ladder from foundations through compounded to "
    "advanced; answers from many angles - definition, example, analogy, application, "
    "history, math, how-to - using only archive data from this system",
    CIT_SIG, "signature")

base.DBCFG = DBCFG

# ---------------------------------------------------------------- demos
# Every demo is real, runnable, stdlib-only Python performing the actual
# endocrinology computation for its record. All are machine-executed by main().

_PREAMBLE = (
"import math\n"
)

def _wrap(name, rid, group, body):
    return (base._hdr(name, rid, group) + _PREAMBLE + body.replace("NAME", json.dumps(name)))

def demo_en_what_is(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def main():
    # receptor occupancy: fraction = [H] / (Kd + [H]); Kd = 1.0 nM
    kd = 1.0
    def occ(h):
        return h/(kd + h)
    o_half, o_10x = occ(1.0), occ(10.0)
    # doubling near Kd vs far above saturation
    d_near = occ(1.0) - occ(0.5)
    d_far = occ(200.0) - occ(100.0)
    print("Kd = %.1f nM" % kd)
    print("occupancy at [H]=Kd: %.3f; at 10x Kd: %.4f" % (o_half, o_10x))
    print("doubling 0.5->1.0 nM gains %.4f occupancy" % d_near)
    print("doubling 100->200 nM gains %.6f occupancy" % d_far)
    assert 0.499 < o_half < 0.501
    assert 0.9090 < o_10x < 0.9091
    assert 0.1666 < d_near < 0.1667
    assert 0.00492 < d_far < 0.00493
    print("rule: near the Kd the signal doubles with the dose; at saturation the dose is noise")
    print("OK: %s read the binding curve" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_en_endocrine_system(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def main():
    # disturbance rejection: 10x open-loop disturbance held to 1.5x closed-loop
    open_loop, closed_loop = 10.0, 1.5
    effectiveness = (open_loop - closed_loop)/(open_loop - 1.0)
    axes = ["HPA (stress)", "HPT (thyroid)", "HPG (reproduction)", "GH (growth)", "prolactin (lactation)"]
    print("classic hypothalamic-pituitary axes: %d" % len(axes))
    for a in axes:
        print("  " + a)
    print("open-loop disturbance: %.1fx -> closed-loop: %.1fx" % (open_loop, closed_loop))
    print("feedback disturbance rejection: %.2f %%" % (effectiveness*100.0))
    assert len(axes) == 5
    assert 0.9444 < effectiveness < 0.9445
    print("rule: feedback does not prevent the push - it erases most of it")
    print("OK: %s closed the loop" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_en_hormone_classes(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def main():
    # insulin: 1 IU = 0.0347 mg; MW 5808 Da -> moles per IU
    iu_mg = 0.0347
    mw = 5808.0
    nmol_per_iu = (iu_mg*1e-3)/mw*1e9
    # half-life span: T4 7 days vs insulin ~5 minutes
    t4_min = 7.0*24.0*60.0
    span = t4_min/5.0
    print("1 IU insulin = %.4f mg = %.3f nmol" % (iu_mg, nmol_per_iu))
    print("T4 half-life: %.0f min vs insulin: 5 min -> %.0fx span" % (t4_min, span))
    assert 5.97 < nmol_per_iu < 5.98
    assert span == 2016.0
    print("rule: chemistry picks the postal class - telegrams or sealed orders")
    print("OK: %s weighed the families" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_en_receptors(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def main():
    # cascade gain: 1 ligand -> 10 G-proteins -> 100 cAMP each -> 1000 targets each
    g_proteins, camp_each, targets_each = 10, 100, 1000
    gain = 1*g_proteins*camp_each*targets_each
    # same ligand, different readers: epinephrine via beta-1 vs alpha-1
    readers = {"beta-1 (heart)": "faster, stronger beat", "alpha-1 (skin vessels)": "constriction",
               "beta-2 (airways)": "dilation"}
    print("cascade gain: 1 x %d x %d x %d = %d" % (g_proteins, camp_each, targets_each, gain))
    for r, e in readers.items():
        print("  epinephrine via %-20s -> %s" % (r, e))
    assert gain == 1000000
    assert len(readers) == 3
    print("rule: the broadcast is public; the meaning is in the installed reader")
    print("OK: %s mapped the readers" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_en_hypothalamus(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def main():
    # GnRH pulse arithmetic: pulses per day at normal / fast / slow cadence
    for label, minutes in (("normal", 90.0), ("fast (PCOS-like)", 60.0), ("slow (stress-like)", 180.0)):
        print("%-18s pulse every %3.0f min -> %.0f pulses/day" % (label, minutes, 24.0*60.0/minutes))
    signals = ["TRH", "CRH", "GnRH", "GHRH", "somatostatin", "dopamine"]
    print("hypothalamic regulators: %d (%s)" % (len(signals), ", ".join(signals)))
    assert 24.0*60.0/90.0 == 16.0
    assert 24.0*60.0/60.0 == 24.0
    assert 24.0*60.0/180.0 == 8.0
    assert len(signals) == 6
    print("rule: the message is in the rhythm - same molecule, different tempo, different order")
    print("OK: %s timed the pulses" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_en_pituitary(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def main():
    # anterior pituitary cell census (percent of cells)
    tribes = [("somatotrophs (GH)", 50.0), ("lactotrophs (prolactin)", 20.0),
              ("corticotrophs (ACTH)", 15.0), ("gonadotrophs (LH/FSH)", 10.0),
              ("thyrotrophs (TSH)", 5.0)]
    total = sum(p for _, p in tribes)
    hormones = ["GH", "prolactin", "ACTH", "TSH", "LH", "FSH"]
    print("anterior pituitary cell census:")
    for tname, p in tribes:
        print("  %-24s %4.1f %%" % (tname, p))
    print("census total: %.0f %%; anterior hormones: %d; gland size ~1 cm" % (total, len(hormones)))
    assert total == 100.0
    assert len(hormones) == 6
    print("rule: half the staff works the growth desk - the biggest department falls first")
    print("OK: %s took the census" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_en_negative_feedback(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def main():
    # log-linear TSH-T4: 2x free T4 -> ~100x fall in TSH
    t4_a, tsh_a = 1.2, 2.5
    tsh_b = tsh_a/100.0
    print("free T4 %.1f ng/dL -> TSH %.1f mIU/L" % (t4_a, tsh_a))
    print("free T4 %.1f ng/dL (2x) -> TSH %.4f mIU/L (~100x down)" % (2.0*t4_a, tsh_b))
    # discrete controller converging on set point
    h, target, k = 2.0, 1.0, 0.3
    for _ in range(20):
        h = h + k*(target - h)
    print("controller after 20 steps: %.6f (target %.1f)" % (h, target))
    assert 0.0249 < tsh_b < 0.0251
    assert 1.0007 < h < 1.0009
    print("rule: watch the thermostat wire, not the furnace - the control signal shouts first")
    print("OK: %s ran the thermostat" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_en_synthesis_secretion(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def main():
    # proinsulin cleavage accounting: 86 = insulin(21+30) + C-peptide(31) + cleavage sites
    pro, a_chain, b_chain, cpep = 86, 21, 30, 31
    insulin = a_chain + b_chain
    sites = pro - insulin - cpep
    # thyroid warehouse: ~100-day supply at 100 mcg T4/day
    days, daily_ug = 100.0, 100.0
    pool_ug = days*daily_ug
    print("proinsulin %d aa = insulin %d + C-peptide %d + cleavage sites %d" % (pro, insulin, cpep, sites))
    print("thyroid pool: %.0f days x %.0f mcg/day = %.0f mcg = %.1f mg" % (days, daily_ug, pool_ug, pool_ug/1000.0))
    assert sites == 4
    assert insulin == 51
    assert pool_ug == 10000.0
    print("rule: peptides are kitted in stages, steroids are built to order, thyroid keeps a warehouse")
    print("OK: %s audited the factory" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_en_assays(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def main():
    # predictive value: sens 99%, spec 98%, prevalence 5%
    sens, spec, prev = 0.99, 0.98, 0.05
    ppv = (sens*prev)/(sens*prev + (1.0 - spec)*(1.0 - prev))
    print("sensitivity %.0f %%, specificity %.0f %%, prevalence %.0f %%" % (sens*100, spec*100, prev*100))
    print("positive predictive value: %.2f %%" % (ppv*100.0))
    print("reference range = central 95%%: 2.5%% of healthy people fall outside by definition" % ())
    assert 0.7226 < ppv < 0.7227
    print("rule: a positive is a rumor until Bayes confirms it - prevalence sets the meaning")
    print("OK: %s interrogated the assay" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_en_half_lives(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def main():
    # stopping levothyroxine: 21 days = 3 T4 half-lives -> 1/8 remains
    t4_left = 0.5**3
    # stopping insulin drip: 30 min = 6 half-lives -> under 2% remains
    ins_left = 0.5**6
    # five-half-life rule: steady state fraction
    steady = 1.0 - 0.5**5
    t4_recheck_days = 5.0*7.0
    print("T4 remaining after 21 days off: %.3f" % t4_left)
    print("insulin remaining 30 min after drip stops: %.4f" % ins_left)
    print("steady-state fraction after 5 half-lives: %.4f" % steady)
    print("levothyroxine recheck no sooner than %.0f days" % t4_recheck_days)
    assert 0.124 < t4_left < 0.126
    assert 0.0156 < ins_left < 0.0157
    assert 0.9687 < steady < 0.9688
    assert t4_recheck_days == 35.0
    print("rule: five half-lives to steady state - the clock sets every recheck")
    print("OK: %s ran the clocks" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_en_gh_axis(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def main():
    # growth arithmetic: prepubertal 5.5 cm/yr; pubertal peak 10 cm/yr for 2 years
    pre, peak, peak_years = 5.5, 10.0, 2.0
    pubertal_gain = peak*peak_years
    # acromegaly: GH fails to suppress below 1 ng/mL on glucose load
    nadir_cutoff = 1.0
    print("prepubertal velocity: %.1f cm/yr" % pre)
    print("pubertal peak: %.0f cm/yr x %.0f yr = %.0f cm gain" % (peak, peak_years, pubertal_gain))
    print("acromegaly OGTT nadir cutoff: %.0f ng/mL" % nadir_cutoff)
    assert pubertal_gain == 20.0
    assert nadir_cutoff == 1.0
    print("rule: the foreman's report (IGF-1) and the earned-value curve (velocity) - audit output, not orders")
    print("OK: %s measured the build" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_en_thyroid_axis(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def main():
    # daily budget: T4 100 mcg secreted; T3 30 mcg total = 6 direct + 24 converted (80%)
    t4 = 100.0
    t3_total, t3_direct = 30.0, 6.0
    t3_converted = t3_total - t3_direct
    conv_share = t3_converted/t3_total
    # T3 ~4x potency of T4: total in T3-equivalents
    t3_eq = t4/4.0 + t3_total
    print("T4 secreted: %.0f mcg/day" % t4)
    print("T3: %.0f direct + %.0f converted = %.0f mcg/day (%.0f %% converted)" % (t3_direct, t3_converted, t3_total, conv_share*100.0))
    print("circulating pool in T3-equivalents: %.0f mcg/day" % t3_eq)
    assert conv_share == 0.8
    assert t3_eq == 55.0
    print("rule: ship the reserve currency in bulk, mint the spending currency locally")
    print("OK: %s balanced the mint" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_en_thyroid_disorders(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def main():
    # levothyroxine: 1.6 mcg/kg/day for a 70-kg adult
    dose = 70.0*1.6
    print("levothyroxine dose: 70 kg x 1.6 mcg/kg/day = %.0f mcg/day" % dose)
    print("TSH bands: subclinical hypo 4.5-10, overt hypo >10 mIU/L; overt hyper <0.1")
    print("recheck no sooner than ~6 weeks after a dose change (five T4 half-lives)")
    assert 111.9 < dose < 112.1
    print("rule: brownout or surge - the thermostat wire tells you which, and the dose follows body mass")
    print("OK: %s dosed the grid" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_en_adrenal_cortex(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def main():
    # cortisol: ~9 mg/m2/day x 1.73 m2 BSA
    daily = 1.73*9.0
    zones = [("glomerulosa", "aldosterone (salt)"), ("fasciculata", "cortisol (stress)"),
             ("reticularis", "DHEA/androgens")]
    # circadian amplitude: ~20 mcg/dL at 8 AM vs ~5 at midnight
    amplitude = 20.0/5.0
    print("cortisol production: 1.73 m2 x 9 mg/m2/day = %.2f mg/day" % daily)
    for z, p in zones:
        print("  zona %-12s -> %s" % (z, p))
    print("circadian amplitude: 20/5 = %.0fx" % amplitude)
    assert 15.56 < daily < 15.58
    assert amplitude == 4.0
    assert len(zones) == 3
    print("rule: two control rooms, one feedstock - headquarters blackout idles only the crisis desk")
    print("OK: %s toured the refinery" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_en_adrenal_medulla(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def main():
    # hemodynamics of the surge: HR x stroke volume
    co_rest = 70.0*70.0/1000.0
    co_stress = 150.0*110.0/1000.0
    ratio = co_stress/co_rest
    print("resting cardiac output: 70 bpm x 70 mL = %.1f L/min" % co_rest)
    print("emergency cardiac output: 150 bpm x 110 mL = %.1f L/min" % co_stress)
    print("surge multiplier: %.3fx; medullary E:NE split 80:20" % ratio)
    assert 3.367 < ratio < 3.368
    print("rule: the panic button needs no committee - nerve in, broadcast out, self-destruct in 2 minutes")
    print("OK: %s hit the panic button" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_en_cortisol_disorders(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def main():
    # unit conversion: 1 mcg/dL cortisol = 27.6 nmol/L; pass mark 18 mcg/dL
    nmol = 18.0*27.6
    # dexamethasone suppression: 15 -> 1.2 mcg/dL
    baseline, post = 15.0, 1.2
    suppression = (baseline - post)/baseline*100.0
    print("cosyntropin pass mark: 18 mcg/dL = %.1f nmol/L (~500)" % nmol)
    print("DST: %.1f -> %.1f mcg/dL = %.1f %% suppression (cutoff <1.8)" % (baseline, post, suppression))
    assert 496.7 < nmol < 496.9
    assert 91.99 < suppression < 92.01
    print("rule: phish the axis with a forged stand-down, drill it with a fake alarm - failures confess")
    print("OK: %s penetration-tested the axis" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_en_glucose_control(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def main():
    # HOMA-IR = (FPG mmol/L x FPI microU/mL) / 22.5
    homa = (5.5*10.0)/22.5
    print("fasting glucose 5.5 mmol/L, fasting insulin 10 microU/mL")
    print("HOMA-IR = 5.5 x 10 / 22.5 = %.4f (normal <~2)" % homa)
    print("fed state: insulin:glucagon high (store); fasted: low (mobilize)")
    assert 2.444 < homa < 2.445
    print("rule: the ratio is the instruction - not either hormone alone")
    print("OK: %s balanced the ledger" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_en_diabetes(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def main():
    # eAG = 28.7 x A1C - 46.7
    def eag(a1c):
        return 28.7*a1c - 46.7
    for a in (6.5, 7.0, 9.0):
        print("A1C %.1f %% -> eAG %.1f mg/dL" % (a, eag(a)))
    gap = eag(9.0) - eag(7.0)
    print("per A1C point: %.1f mg/dL; 9.0 -> 7.0 erases %.1f mg/dL" % (28.7, gap))
    assert 154.1 < eag(7.0) < 154.3
    assert 139.8 < eag(6.5) < 139.9
    assert 57.3 < gap < 57.5
    print("rule: the quarterly audit cannot be faked the morning of the inspection")
    print("OK: %s ran the audit" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_en_calcium(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def main():
    # albumin correction: corrected = measured + 0.8 x (4.0 - albumin)
    measured, albumin = 8.0, 3.0
    corrected = measured + 0.8*(4.0 - albumin)
    print("measured Ca %.1f mg/dL, albumin %.1f g/dL -> corrected %.1f mg/dL" % (measured, albumin, corrected))
    print("reference 8.5-10.5 mg/dL; PTH answers a calcium fall within minutes")
    assert 8.79 < corrected < 8.81
    print("rule: keep two columns in the ledger - calcium and phosphate move together")
    print("OK: %s balanced the treasury" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_en_male_repro(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def main():
    # spermatogenesis pipeline: 150M/day x 64 days in flight
    daily, transit = 150e6, 64.0
    in_flight = daily*transit
    print("daily output: %.0f million sperm/day" % (daily/1e6))
    print("in-flight inventory: %.0fM x %.0f d = %.2e sperm" % (daily/1e6, transit, in_flight))
    print("testosterone 5-7 mg/day; ~2%% free; primary failure = low T + high LH/FSH")
    assert 9.59e9 < in_flight < 9.61e9
    print("rule: two plants under one roof, each with its own report card - and a 64-day conveyor")
    print("OK: %s walked the plant" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_en_female_repro(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def main():
    # fertile window: 5 days sperm survival + ovulation day
    window = 5 + 1
    follicular, luteal = 14, 14
    cycle = follicular + luteal
    print("cycle: %d d follicular + ovulation + %d d luteal = %d d" % (follicular, luteal, cycle))
    print("fertile window: 5 d sperm survival + ovulation day = %d d" % window)
    print("ovulation confirmed by luteal progesterone >3 ng/mL")
    assert window == 6
    assert cycle == 28
    print("rule: a monthly build-and-test with a sign-flipping trigger and a fixed two-week acceptance test")
    print("OK: %s ran the program" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_en_posterior_pituitary(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def main():
    # controller gain: 10% ADH rise per 1% osmolarity rise
    gain, osm_rise = 10.0, 2.0
    adh_rise = gain*osm_rise
    print("controller gain: %.0f %% ADH per 1 %% osmolarity" % gain)
    print("+%.0f %% osmolarity -> +%.0f %% ADH" % (osm_rise, adh_rise))
    print("urine concentration range: 50 to 1200 mOsm/kg; deprivation pass mark >800")
    assert adh_rise == 20.0
    print("rule: the tightest loop in the building - dehydration compounds, so the gain is high")
    print("OK: %s tuned the valve" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_en_neuroendocrinology(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def main():
    # cortisol circadian amplitude: ~20 mcg/dL at 8 AM vs ~5 at midnight
    amplitude = 20.0/5.0
    print("cortisol: 8 AM ~20 mcg/dL, midnight ~5 mcg/dL -> %.0fx amplitude" % amplitude)
    print("melatonin: dim-light onset ~21:00, peak 02:00-04:00, gated by darkness")
    assert amplitude == 4.0
    print("rule: the broadcast time signal and the scheduled shift change - chronobiology is dosing")
    print("OK: %s read the clock" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_en_endocrine_tumors(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def main():
    # pheochromocytoma 10% rule: P(all three) = 0.1^3
    p_all_three = 0.1**3
    # MEN1: 200 carriers x 95% hyperparathyroidism penetrance by 50
    men1_cases = 200.0*0.95
    print("pheo 10%% rule compound: 0.1^3 = %.4f (%.2f %%)" % (p_all_three, p_all_three*100.0))
    print("MEN1: 200 carriers x 95%% -> %.0f with hyperparathyroidism by 50" % men1_cases)
    assert 0.00099 < p_all_three < 0.00101
    assert men1_cases == 190.0
    print("rule: find the rogue station by its transmissions, not by sweeping the terrain")
    print("OK: %s ran counter-intelligence" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_en_pcos(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def main():
    # Rotterdam phenotypes: C(3,2) + C(3,3) = 3 + 1
    import math
    def c(n, k):
        return math.factorial(n)//(math.factorial(k)*math.factorial(n - k))
    phenotypes = c(3, 2) + c(3, 3)
    lo, hi = 1000.0*0.08, 1000.0*0.13
    print("Rotterdam 2-of-3: C(3,2)+C(3,3) = %d phenotypes" % phenotypes)
    print("prevalence 8-13%% -> %.0f to %.0f per 1000 women" % (lo, hi))
    assert phenotypes == 4
    assert lo == 80.0 and hi == 130.0
    print("rule: one hijacker, four crime scenes - the combinatorics map the intrusion")
    print("OK: %s profiled the phenotypes" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_en_thyroid_nodules(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def main():
    # Bethesda II risk ~2%: expected cancers in 100 biopsied nodules
    expected = 100.0*0.02
    risks = {"I": 10, "II": 2, "III": 15, "IV": 25, "V": 70, "VI": 97}
    print("Bethesda malignancy risks (%%): " + ", ".join("%s~%d" % (k, v) for k, v in risks.items()))
    print("100 Bethesda-II nodules x 2%% -> %.1f expected cancers (watch, do not cut)" % expected)
    assert 1.99 < expected < 2.01
    assert len(risks) == 6
    print("rule: the funnel spends the scalpel only on the statistically guilty")
    print("OK: %s worked the funnel" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_en_pituitary_tumors(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def main():
    # volume ratio: 12-mm vs 8-mm adenoma (spheres): (6/4)^3
    ratio = (6.0/4.0)**3
    print("12-mm adenoma vs 8-mm: volume ratio (6/4)^3 = %.3f" % ratio)
    print("micro <10 mm, macro >=10 mm; prolactinoma ~40%% of adenomas; cabergoline ~90%% effective")
    assert 3.374 < ratio < 3.376
    print("rule: millimeters matter under the optic chiasm - volume grows with the cube")
    print("OK: %s measured the rack" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_en_dynamic_testing(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def main():
    # DST suppression: 15 -> 1.2 mcg/dL
    suppression = (15.0 - 1.2)/15.0*100.0
    # cosyntropin pass mark in nmol/L
    nmol = 18.0*27.6
    print("DST suppression: (15-1.2)/15 = %.1f %% (fail line: <1.8 mcg/dL)" % suppression)
    print("cosyntropin pass: 18 mcg/dL = %.1f nmol/L" % nmol)
    assert 91.99 < suppression < 92.01
    assert 496.7 < nmol < 496.9
    print("rule: phish with a forged stand-down, drill with a fake alarm - the numbers draw the line")
    print("OK: %s red-teamed the axis" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_en_cah(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def main():
    # classic 21-hydroxylase deficiency: 1 in 15,000 births; ~75% salt-wasting
    births = 300000.0
    cases = births/15000.0
    salt_wasters = cases*0.75
    print("%.0f births / 15000 -> %.0f classic cases" % (births, cases))
    print("salt-wasting share: %.0f x 75%% = %.0f newborns at crisis risk" % (cases, salt_wasters))
    assert cases == 20.0
    assert salt_wasters == 15.0
    print("rule: one broken machine re-routes the whole factory - screen the stockpile marker")
    print("OK: %s traced the block" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_en_obesity(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def main():
    # metabolic syndrome: C(5,3)+C(5,4)+C(5,5) qualifying patterns
    import math
    def c(n, k):
        return math.factorial(n)//(math.factorial(k)*math.factorial(n - k))
    patterns = c(5, 3) + c(5, 4) + c(5, 5)
    # STEP-1: 110-kg patient x 14.9% loss
    final_wt = 110.0*(1.0 - 0.149)
    print("metabolic syndrome qualifying patterns: 10+5+1 = %d" % patterns)
    print("110 kg x 14.9%% (STEP-1 semaglutide) -> %.2f kg" % final_wt)
    assert patterns == 16
    assert 93.60 < final_wt < 93.62
    print("rule: the firmware was written during famines - the override code forges 'enough'")
    print("OK: %s weighed the economics" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_en_hormone_therapy(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def main():
    # Pearl index: pregnancies per 100 woman-years
    typical = 1000.0*7.0/100.0
    perfect = 1000.0*0.3/100.0
    print("combined pill typical use (7/100 WY): 1000 woman-years -> %.0f pregnancies" % typical)
    print("combined pill perfect use (0.3/100 WY): 1000 woman-years -> %.0f pregnancies" % perfect)
    assert typical == 70.0
    assert perfect == 3.0
    print("rule: one pill, three independent mechanisms - denial of service on the ovulation trigger")
    print("OK: %s counted the ledger" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_en_pediatric(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def main():
    # mid-parental height: father 175, mother 162
    boy = (175.0 + 162.0 + 13.0)/2.0
    girl = (175.0 + 162.0 - 13.0)/2.0
    print("father 175 cm, mother 162 cm")
    print("predicted son: (175+162+13)/2 = %.1f cm" % boy)
    print("predicted daughter: (175+162-13)/2 = %.1f cm" % girl)
    print("red flag: growth velocity <4 cm/yr in mid-childhood")
    assert boy == 175.0
    assert girl == 162.0
    print("rule: the chart is the vital sign, velocity its slope, bone age the auditor's clock")
    print("OK: %s projected the build" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_en_emergencies(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def main():
    # DKA fluids: 15-20 mL/kg first hour for 70 kg
    lo, hi = 70.0*15.0, 70.0*20.0
    # anion gap: Na 140 - (Cl 100 + HCO3 15)
    ag = 140.0 - (100.0 + 15.0)
    print("DKA fluids first hour: 70 kg -> %.0f-%.0f mL" % (lo, hi))
    print("anion gap: 140-(100+15) = %.0f (normal 8-12)" % ag)
    print("thyroid storm: Burch-Wartofsky >=45 highly suggestive; adrenal crisis: hydrocortisone 100 mg IV now")
    assert lo == 1050.0 and hi == 1400.0
    assert ag == 25.0
    print("rule: fluids before insulin, beta-blocker before thionamide before iodine - order is the therapy")
    print("OK: %s ran the runbook" % NAME)
if __name__ == "__main__":
    main()
''')

def demo_en_future(name, rid, group, points, req):
    return _wrap(name, rid, group, '''\\
def main():
    # SURMOUNT-1: tirzepatide 15 mg, -20.9% at 72 weeks, 110-kg patient
    loss = 110.0*0.209
    final = 110.0 - loss
    # STEP-1: semaglutide 2.4 mg, -14.9% at 68 weeks
    final_sema = 110.0*(1.0 - 0.149)
    print("tirzepatide: 110 kg - %.2f kg = %.2f kg" % (loss, final))
    print("semaglutide: 110 kg -> %.2f kg" % final_sema)
    print("teplizumab: delays stage-3 type 1 diabetes ~2 years in high-risk relatives")
    assert 86.99 < final < 87.03
    assert 93.60 < final_sema < 93.62
    print("rule: from spare parts to systems engineering - the messages were always code")
    print("OK: %s compiled the future" % NAME)
if __name__ == "__main__":
    main()
''')

DEMOS = {
    "what_is": demo_en_what_is,
    "endocrine_system": demo_en_endocrine_system,
    "hormone_classes": demo_en_hormone_classes,
    "receptors": demo_en_receptors,
    "hypothalamus": demo_en_hypothalamus,
    "pituitary": demo_en_pituitary,
    "negative_feedback": demo_en_negative_feedback,
    "synthesis_secretion": demo_en_synthesis_secretion,
    "assays": demo_en_assays,
    "half_lives": demo_en_half_lives,
    "gh_axis": demo_en_gh_axis,
    "thyroid_axis": demo_en_thyroid_axis,
    "thyroid_disorders": demo_en_thyroid_disorders,
    "adrenal_cortex": demo_en_adrenal_cortex,
    "adrenal_medulla": demo_en_adrenal_medulla,
    "cortisol_disorders": demo_en_cortisol_disorders,
    "glucose_control": demo_en_glucose_control,
    "diabetes": demo_en_diabetes,
    "calcium": demo_en_calcium,
    "male_repro": demo_en_male_repro,
    "female_repro": demo_en_female_repro,
    "posterior_pituitary": demo_en_posterior_pituitary,
    "neuroendocrinology": demo_en_neuroendocrinology,
    "endocrine_tumors": demo_en_endocrine_tumors,
    "pcos": demo_en_pcos,
    "thyroid_nodules": demo_en_thyroid_nodules,
    "pituitary_tumors": demo_en_pituitary_tumors,
    "dynamic_testing": demo_en_dynamic_testing,
    "cah": demo_en_cah,
    "obesity": demo_en_obesity,
    "hormone_therapy": demo_en_hormone_therapy,
    "pediatric": demo_en_pediatric,
    "emergencies": demo_en_emergencies,
    "future": demo_en_future,
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
    for slug in ("endocrinology", "endocrinology-signature"):
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
