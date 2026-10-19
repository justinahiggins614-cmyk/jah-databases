#!/usr/bin/env python3
"""Solution-explorer walkthrough demos for The Unsolved Pharmacology Database.

Every demo is a working program: it walks through the Signature proposed
solution approach in steps, uses adjustable assumptions, computes REAL
values, checks them with tight-bounds asserts (never float exact-equality),
and ends with a confirm/refute panel plus the OK marker.

Honesty rule: demos explore PROPOSED approaches. They never claim proof.
"""

import math

LABEL = "Signature-generated proposed solution \u2014 not established science."


def demo_placebo_mechanism(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\\
"""SOLUTION EXPLORER: The Placebo Mechanism.
Walks the Signature proposed approach: expectation as a control signal that
pre-releases endogenous ligands, with individual predictive gain setting the
response size.
PROPOSAL ONLY - __LABEL__"""

# ---- adjustable assumptions ----
PREDICTIVE_GAIN = 0.65   # 0..1: how strongly this brain trusts its forecasts
BASELINE_PAIN = 7.0      # 0..10 pain score before treatment
MAX_ENDOGENOUS_DROP = 3.5  # max pain-score drop endogenous opioids can produce

def step1_problem():
    print("STEP 1 - the problem: inert pill, real chemistry.")
    print("  Placebo analgesia is blocked by naloxone -> endogenous opioids.")
    assert 0.0 <= PREDICTIVE_GAIN <= 1.0

def step2_signature_approach():
    relief = MAX_ENDOGENOUS_DROP * PREDICTIVE_GAIN
    final = BASELINE_PAIN - relief
    print("STEP 2 - Signature approach: relief = max_drop * predictive_gain")
    print("  gain=%.2f -> relief=%.2f pain points (%.1f -> %.1f)" % (
        PREDICTIVE_GAIN, relief, BASELINE_PAIN, final))
    assert 0.0 < relief < MAX_ENDOGENOUS_DROP + 1e-9
    assert 2.0 < final < 7.0, "final pain out of plausible range"
    return relief

def step3_testable_prediction(relief):
    low_gain_relief = MAX_ENDOGENOUS_DROP * 0.15
    print("STEP 3 - testable prediction: low-gain brains barely respond.")
    print("  gain=0.15 -> relief=%.2f vs gain=0.65 -> relief=%.2f" % (
        low_gain_relief, relief))
    assert relief > 2.0 * low_gain_relief, "gain effect too weak to detect"

def confirm_refute_panel():
    print("CONFIRM/REFUTE PANEL:")
    print("  CONFIRM if: conditioning that raises predictive gain raises")
    print("    measured endogenous opioid release in lockstep with relief.")
    print("  REFUTE if: strong relief occurs with no measurable ligand")
    print("    release, or gain manipulations change reports only.")

def main():
    step1_problem()
    relief = step2_signature_approach()
    step3_testable_prediction(relief)
    confirm_refute_panel()
    print("OK: %s solution-explorer complete (relief=%.2f)" % (RID, relief))

RID = "__RID__"
if __name__ == "__main__":
    main()
'''.replace('__LABEL__', LABEL).replace('__RID__', rid)


def demo_late_stage_failure(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\\
"""SOLUTION EXPLORER: Why Drugs Fail in Late-Stage Trials.
Walks the Signature proposed approach: a translation contract that discounts
preclinical efficacy by measured model fidelity before expensive phases.
PROPOSAL ONLY - __LABEL__"""

# ---- adjustable assumptions ----
PRECLINICAL_EFFECT = 0.60  # fractional disease reduction in animal model
MODEL_FIDELITY = 0.35      # historical P(animal success -> human success)
CLINICAL_BAR = 0.25        # minimum fractional effect worth Phase II cost
PHASE2_COST_M = 60.0       # $M per Phase II program

def step1_problem():
    print("STEP 1 - the problem: ~90% of Phase I entrants never get approved;")
    print("  Phase II efficacy failures dominate, each costing tens of $M.")
    assert 0.0 < MODEL_FIDELITY < 1.0

def step2_signature_approach():
    discounted = PRECLINICAL_EFFECT * MODEL_FIDELITY
    go = discounted >= CLINICAL_BAR
    print("STEP 2 - Signature approach: discounted effect = %.3f" % discounted)
    print("  %.2f preclinical * %.2f fidelity = %.3f vs bar %.2f -> %s" % (
        PRECLINICAL_EFFECT, MODEL_FIDELITY, discounted, CLINICAL_BAR,
        "GO" if go else "KILL EARLY"))
    assert 0.0 < discounted < PRECLINICAL_EFFECT
    return go, discounted

def step3_testable_prediction(go, discounted):
    saved = 0.0 if go else PHASE2_COST_M
    print("STEP 3 - testable prediction: killing here saves $%.0fM" % saved)
    print("  Retrospective test: contract must kill most historical Phase II")
    print("  failures while sparing most eventual approvals.")
    assert discounted < CLINICAL_BAR or saved == 0.0

def confirm_refute_panel():
    print("CONFIRM/REFUTE PANEL:")
    print("  CONFIRM if: retrospective scoring kills historical failures early")
    print("    and prospective fidelity-gated pipelines beat baseline Phase II")
    print("    success rates.")
    print("  REFUTE if: stage-to-stage translation proves fundamentally")
    print("    unpredictable - no learnable fidelity pattern.")

def main():
    step1_problem()
    go, discounted = step2_signature_approach()
    step3_testable_prediction(go, discounted)
    confirm_refute_panel()
    print("OK: %s solution-explorer complete (discounted=%.3f)" % (RID, discounted))

RID = "__RID__"
if __name__ == "__main__":
    main()
'''.replace('__LABEL__', LABEL).replace('__RID__', rid)


def demo_personalized_dosing(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\\
"""SOLUTION EXPLORER: Personalized Dosing Models.
Walks the Signature proposed approach: a personal dose equation solved before
the first pill, using a warfarin-style genotype-guided model.
PROPOSAL ONLY - __LABEL__"""

# ---- adjustable assumptions ----
BASE_DOSE = 5.0        # mg/day typical warfarin starting dose
CYP2C9_FACTOR = 0.60   # dose multiplier for poor-metabolizer variant
VKORC1_FACTOR = 0.70   # dose multiplier for sensitive VKORC1 variant
AGE = 72               # years
WEIGHT_KG = 68.0

def step1_problem():
    print("STEP 1 - the problem: one label dose, many different bodies.")
    print("  CYP2C9/VKORC1 variants explain ~half of warfarin dose variance.")
    assert 20.0 < WEIGHT_KG < 200.0

def step2_signature_approach():
    age_factor = 1.0 - 0.004 * max(0, AGE - 50)
    wt_factor = (WEIGHT_KG / 70.0) ** 0.75
    personal = BASE_DOSE * CYP2C9_FACTOR * VKORC1_FACTOR * age_factor * wt_factor
    print("STEP 2 - Signature approach: personal dose equation.")
    print("  5.00 * %.2f (CYP2C9) * %.2f (VKORC1) * %.3f (age) * %.3f (wt)" % (
        CYP2C9_FACTOR, VKORC1_FACTOR, age_factor, wt_factor))
    print("  -> personal starting dose = %.2f mg/day" % personal)
    assert 0.5 < personal < BASE_DOSE, "personal dose out of plausible range"
    return personal

def step3_testable_prediction(personal):
    label_risk = abs(BASE_DOSE - personal) / personal
    print("STEP 3 - testable prediction: label dose is %.0f%% off personal." % (
        100 * label_risk))
    print("  Engine-dosed patients should hit target INR faster, bleed less.")
    assert label_risk > 0.5, "genotype makes little difference - check factors"

def confirm_refute_panel():
    print("CONFIRM/REFUTE PANEL:")
    print("  CONFIRM if: randomized trials show engine dosing beats label")
    print("    dosing on time-to-target and adverse events.")
    print("  REFUTE if: within-patient day-to-day variability swamps the")
    print("    predicted between-patient differences.")

def main():
    step1_problem()
    personal = step2_signature_approach()
    step3_testable_prediction(personal)
    confirm_refute_panel()
    print("OK: %s solution-explorer complete (dose=%.2f mg/day)" % (RID, personal))

RID = "__RID__"
if __name__ == "__main__":
    main()
'''.replace('__LABEL__', LABEL).replace('__RID__', rid)


def demo_polypharmacy_interactions(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\\
"""SOLUTION EXPLORER: Polypharmacy and Drug-Drug Interactions.
Walks the Signature proposed approach: the regimen as one interacting network
instead of a list of pairs.
PROPOSAL ONLY - __LABEL__"""

# ---- adjustable assumptions ----
N_DRUGS = 8
PAIR_INTERACT_P = 0.06   # probability a random pair interacts meaningfully
CYP3A4_FRACTION = 0.50   # fraction of drugs touching CYP3A4

def step1_problem():
    pairs = N_DRUGS * (N_DRUGS - 1) // 2
    triples = N_DRUGS * (N_DRUGS - 1) * (N_DRUGS - 2) // 6
    print("STEP 1 - the problem: %d drugs -> %d pairs, %d triples." % (
        N_DRUGS, pairs, triples))
    assert pairs == 28 and triples == 56
    return pairs

def step2_signature_approach(pairs):
    expected_pair_hits = pairs * PAIR_INTERACT_P
    cyp_drugs = N_DRUGS * CYP3A4_FRACTION
    print("STEP 2 - Signature approach: simulate the whole network.")
    print("  expected pairwise hits: %.1f; ~%.0f drugs share CYP3A4 node" % (
        expected_pair_hits, cyp_drugs))
    print("  network propagation finds emergent multi-drug effects pairs miss.")
    assert 1.0 < expected_pair_hits < 3.0
    return expected_pair_hits

def step3_testable_prediction(expected_pair_hits):
    print("STEP 3 - testable prediction: network model beats pairwise")
    print("  checkers on measured drug levels in 5+ drug regimens.")
    assert expected_pair_hits > 1.0, "too few interactions to matter"

def confirm_refute_panel():
    print("CONFIRM/REFUTE PANEL:")
    print("  CONFIRM if: network predictions match measured levels and")
    print("    adverse events better than standard checkers, prospectively.")
    print("  REFUTE if: higher-order interactions prove dominated by")
    print("    unmeasurable patient factors.")

def main():
    pairs = step1_problem()
    hits = step2_signature_approach(pairs)
    step3_testable_prediction(hits)
    confirm_refute_panel()
    print("OK: %s solution-explorer complete (pairs=%d)" % (RID, pairs))

RID = "__RID__"
if __name__ == "__main__":
    main()
'''.replace('__LABEL__', LABEL).replace('__RID__', rid)


def demo_bbb_selectivity(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\\
"""SOLUTION EXPLORER: The Blood-Brain Barrier's Selectivity.
Walks the Signature proposed approach: borrow the barrier's own influx
transporters instead of breaking the wall. Includes a Clark logBB check.
PROPOSAL ONLY - __LABEL__"""

# ---- adjustable assumptions ----
LOGP = 2.1    # octanol-water partition of candidate
PSA = 65.0    # polar surface area (A^2)
PGP_SUBSTRATE = True

def clark_logbb(logp, psa):
    return 0.152 * logp - 0.0148 * psa + 0.139

def step1_problem():
    print("STEP 1 - the problem: ~98% of small molecules fail to cross usefully.")
    assert PSA > 0 and LOGP > -3

def step2_signature_approach():
    logbb = clark_logbb(LOGP, PSA)
    brain_plasma = 10 ** logbb
    print("STEP 2 - Clark estimate: logBB = %.3f -> brain/plasma = %.3f" % (
        logbb, brain_plasma))
    print("  P-gp substrate: %s -> efflux will cut this further." % PGP_SUBSTRATE)
    assert -2.0 < logbb < 0.5, "logBB outside plausible CNS range"
    print("  Signature approach: stop optimizing sneak-through; design a")
    print("  shuttle-cargo pair the influx transporters invite across.")
    return brain_plasma

def step3_testable_prediction(brain_plasma):
    print("STEP 3 - testable prediction: shuttle conjugate must beat %.3f" % (
        brain_plasma))
    print("  brain/plasma by multiples, dose-proportionally, in primates.")
    assert brain_plasma < 1.0, "already brain-penetrant; shuttle unnecessary"

def confirm_refute_panel():
    print("CONFIRM/REFUTE PANEL:")
    print("  CONFIRM if: shuttle conjugates show dose-proportional brain")
    print("    uptake without disrupting natural transporter cargo.")
    print("  REFUTE if: transporters saturate at clinically irrelevant doses.")

def main():
    step1_problem()
    bp = step2_signature_approach()
    step3_testable_prediction(bp)
    confirm_refute_panel()
    print("OK: %s solution-explorer complete (brain/plasma=%.3f)" % (RID, bp))

RID = "__RID__"
if __name__ == "__main__":
    main()
'''.replace('__LABEL__', LABEL).replace('__RID__', rid)


def demo_off_target_prediction(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\\
"""SOLUTION EXPLORER: Predicting Off-Target Effects.
Walks the Signature proposed approach: a whole-proteome binding census
filtered by tissue exposure.
PROPOSAL ONLY - __LABEL__"""

# ---- adjustable assumptions ----
N_DRUGGABLE = 3000     # druggable proteins in census
MEAN_OFFTARGETS = 40   # mean significant off-target binders per drug
TISSUE_REACHED = 0.40  # fraction of tissues with meaningful exposure

def step1_problem():
    print("STEP 1 - the problem: most drugs bind dozens of unintended proteins;")
    print("  dish binding != human side effect. hERG proved the stakes.")
    assert N_DRUGGABLE > 1000

def step2_signature_approach():
    risky = MEAN_OFFTARGETS * TISSUE_REACHED
    print("STEP 2 - Signature approach: census x exposure = occupancy risk.")
    print("  %d binders x %.2f tissue reach -> ~%.0f risky occupancies" % (
        MEAN_OFFTARGETS, TISSUE_REACHED, risky))
    assert 5.0 < risky < 40.0
    return risky

def step3_testable_prediction(risky):
    print("STEP 3 - testable prediction: blinded census must flag real side")
    print("  effects of known drugs with high sensitivity, few false alarms.")
    assert risky >= 5.0

def confirm_refute_panel():
    print("CONFIRM/REFUTE PANEL:")
    print("  CONFIRM if: prospective blinded predictions match known drug")
    print("    side-effect profiles.")
    print("  REFUTE if: pockets prove too idiosyncratic for interpolation.")

def main():
    step1_problem()
    risky = step2_signature_approach()
    step3_testable_prediction(risky)
    confirm_refute_panel()
    print("OK: %s solution-explorer complete (risky=%.0f)" % (RID, risky))

RID = "__RID__"
if __name__ == "__main__":
    main()
'''.replace('__LABEL__', LABEL).replace('__RID__', rid)


def demo_dili_prediction(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\\
"""SOLUTION EXPLORER: Predicting Drug-Induced Liver Injury.
Walks the Signature proposed approach: DILI as a three-hit collision with a
computable population rate.
PROPOSAL ONLY - __LABEL__"""

# ---- adjustable assumptions ----
P_REACTIVE_METAB = 0.30   # P(candidate forms reactive metabolite)
P_SUSCEPTIBLE_HLA = 0.08  # P(patient carries risk HLA presentation)
P_LIVER_STRESS = 0.25     # P(background liver stress in population
TREATED = 1_000_000

def step1_problem():
    print("STEP 1 - the problem: idiosyncratic DILI is rare, immune-linked,")
    print("  and missed by animals and cells. Hy's law flags it too late.")
    assert 0.0 < P_REACTIVE_METAB < 1.0

def step2_signature_approach():
    p_dili = P_REACTIVE_METAB * P_SUSCEPTIBLE_HLA * P_LIVER_STRESS
    expected = p_dili * TREATED
    print("STEP 2 - Signature approach: P(DILI) = %.2e per patient" % p_dili)
    print("  -> ~%.0f cases per million treated" % expected)
    assert 100.0 < expected < 20000.0, "rate outside plausible DILI range"
    return expected

def step3_testable_prediction(expected):
    print("STEP 3 - testable prediction: withdrawn-for-DILI drugs must score")
    print("  far above safe comparators on this three-hit engine.")
    assert expected > 100.0

def confirm_refute_panel():
    print("CONFIRM/REFUTE PANEL:")
    print("  CONFIRM if: retrospective scoring separates withdrawn vs safe")
    print("    drugs, and prospective flags match early-trial signals.")
    print("  REFUTE if: large non-metabolic, non-immune DILI fraction found.")

def main():
    step1_problem()
    expected = step2_signature_approach()
    step3_testable_prediction(expected)
    confirm_refute_panel()
    print("OK: %s solution-explorer complete (per-million=%.0f)" % (RID, expected))

RID = "__RID__"
if __name__ == "__main__":
    main()
'''.replace('__LABEL__', LABEL).replace('__RID__', rid)


def demo_antibiotic_resistance(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\\
"""SOLUTION EXPLORER: Why Antibiotics Always Lose to Resistance.
Walks the Signature proposed approach: rewrite the selection rules instead
of maximizing kill pressure.
PROPOSAL ONLY - __LABEL__"""

# ---- adjustable assumptions ----
MU = 1e-8            # resistance mutation rate per cell division
POPULATION = 1e10    # bacteria in an infection
FITNESS_COST = 0.10  # growth penalty of resistant mutant without drug

def step1_problem():
    p_any = 1.0 - (1.0 - MU) ** POPULATION
    print("STEP 1 - the problem: P(any resistant mutant) = %.4f" % p_any)
    print("  With 1e10 cells and mu=1e-8, resistance pre-exists treatment.")
    assert p_any > 0.99, "resistance should be near-certain at this scale"
    return p_any

def step2_signature_approach(p_any):
    print("STEP 2 - Signature approach: selection, not mutation, is the lever.")
    print("  fitness cost %.0f%% means susceptibles outcompete resistants" % (
        100 * FITNESS_COST))
    print("  without drug -> preserve susceptibles, disarm instead of kill.")
    suppressed = POPULATION * (1.0 - FITNESS_COST)
    assert suppressed < POPULATION
    return p_any

def step3_testable_prediction(p_any):
    print("STEP 3 - testable prediction: collateral-sensitivity cycling must")
    print("  delay emergence from months to years vs standard therapy.")
    assert p_any > 0.99

def confirm_refute_panel():
    print("CONFIRM/REFUTE PANEL:")
    print("  CONFIRM if: evolutionary protocols durably suppress emergence in")
    print("    trials; anti-virulence drugs work without selecting resistance.")
    print("  REFUTE if: cost-free multi-resistance proves universally easy.")

def main():
    p_any = step1_problem()
    step2_signature_approach(p_any)
    step3_testable_prediction(p_any)
    confirm_refute_panel()
    print("OK: %s solution-explorer complete (P_res=%.4f)" % (RID, p_any))

RID = "__RID__"
if __name__ == "__main__":
    main()
'''.replace('__LABEL__', LABEL).replace('__RID__', rid)


def demo_sex_differences(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\\
"""SOLUTION EXPLORER: Sex Differences in Drug Response.
Walks the Signature proposed approach: sex-parameterized pharmacokinetics
instead of unisex dosing.
PROPOSAL ONLY - __LABEL__"""

# ---- adjustable assumptions ----
CL_MALE = 6.0      # L/h clearance, male reference
CL_FEMALE = 4.6    # L/h clearance, female (lower CYP activity + renal flow)
DOSE = 100.0       # mg unisex label dose

def step1_problem():
    print("STEP 1 - the problem: women suffer ADRs ~2x the male rate;")
    print("  zolpidem's dose was halved for women only in 2013.")
    assert CL_FEMALE < CL_MALE

def step2_signature_approach():
    auc_m = DOSE / CL_MALE
    auc_f = DOSE / CL_FEMALE
    ratio = auc_f / auc_m
    print("STEP 2 - Signature approach: exposure ratio female/male = %.2f" % ratio)
    print("  same %.0f mg -> %.1f vs %.1f mg*h/L exposure" % (DOSE, auc_m, auc_f))
    assert 1.15 < ratio < 1.60, "ratio outside plausible sex-difference range"
    corrected = DOSE / ratio
    print("  sex-parameterized female dose: %.0f mg" % corrected)
    return ratio

def step3_testable_prediction(ratio):
    print("STEP 3 - testable prediction: template retrodicts zolpidem/QT sex")
    print("  signals from physiology alone; prospective sex dosing cuts ADRs.")
    assert ratio > 1.15

def confirm_refute_panel():
    print("CONFIRM/REFUTE PANEL:")
    print("  CONFIRM if: prospective sex-parameterized dosing reduces ADRs")
    print("    vs unisex dosing.")
    print("  REFUTE if: within-sex variability dwarfs between-sex difference.")

def main():
    step1_problem()
    ratio = step2_signature_approach()
    step3_testable_prediction(ratio)
    confirm_refute_panel()
    print("OK: %s solution-explorer complete (ratio=%.2f)" % (RID, ratio))

RID = "__RID__"
if __name__ == "__main__":
    main()
'''.replace('__LABEL__', LABEL).replace('__RID__', rid)


def demo_pediatric_dosing(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\\
"""SOLUTION EXPLORER: Pediatric Dosing.
Walks the Signature proposed approach: ontogeny-parameterized dosing instead
of weight scaling.
PROPOSAL ONLY - __LABEL__"""

# ---- adjustable assumptions ----
ADULT_DOSE = 500.0     # mg adult dose
ADULT_WT = 70.0        # kg
CHILD_WT = 12.0        # kg (2-year-old)
ENZYME_MATURATION = 0.55  # fraction of adult enzyme activity at this age

def step1_problem():
    print("STEP 1 - the problem: gray baby syndrome came from adult dosing;")
    print("  most pediatric use is still off-label weight scaling.")
    assert 0.0 < ENZYME_MATURATION < 1.0

def step2_signature_approach():
    wt_scaled = ADULT_DOSE * (CHILD_WT / ADULT_WT)
    allo = ADULT_DOSE * (CHILD_WT / ADULT_WT) ** 0.75
    onto = allo * ENZYME_MATURATION
    print("STEP 2 - Signature approach: three candidate doses:")
    print("  weight-scaled: %.0f mg | allometric: %.0f mg | ontogeny: %.0f mg" % (
        wt_scaled, allo, onto))
    assert onto < allo < ADULT_DOSE
    assert wt_scaled < allo, "allometry should exceed linear weight scaling"
    return onto

def step3_testable_prediction(onto):
    print("STEP 3 - testable prediction: ontogeny-dosed children hit target")
    print("  exposure more reliably than weight-scaled children.")
    assert onto > 0.0

def confirm_refute_panel():
    print("CONFIRM/REFUTE PANEL:")
    print("  CONFIRM if: prospective trials favor engine dosing across drug")
    print("    classes on target attainment and adverse events.")
    print("  REFUTE if: individual ontogeny variation swamps population curves.")

def main():
    step1_problem()
    onto = step2_signature_approach()
    step3_testable_prediction(onto)
    confirm_refute_panel()
    print("OK: %s solution-explorer complete (ontogeny_dose=%.0f mg)" % (RID, onto))

RID = "__RID__"
if __name__ == "__main__":
    main()
'''.replace('__LABEL__', LABEL).replace('__RID__', rid)


def demo_chronopharmacology(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\\
"""SOLUTION EXPLORER: Chronopharmacology.
Walks the Signature proposed approach: dosing time as a first-class variable
with personal circadian phase.
PROPOSAL ONLY - __LABEL__"""

# ---- adjustable assumptions ----
MESOR = 1.0        # rhythm-adjusted mean effect
AMPLITUDE = 0.35   # circadian amplitude (fraction of mesor)
ACROPHASE = 2.0    # hour of peak target activity (02:00)
PHASE_SD = 1.5     # hours, population phase variability

def effect_at(hour):
    return MESOR + AMPLITUDE * math.cos(2 * math.pi * (hour - ACROPHASE) / 24.0)

def step1_problem():
    print("STEP 1 - the problem: same dose, different hour, different outcome;")
    print("  labels say 'once daily' with no time.")
    assert 0.0 < AMPLITUDE < MESOR

def step2_signature_approach():
    best = max(range(24), key=effect_at)
    worst = min(range(24), key=effect_at)
    gain = (effect_at(best) - effect_at(worst)) / effect_at(worst)
    print("STEP 2 - Signature approach: best hour %02d:00, worst %02d:00" % (
        best, worst))
    print("  timing gain: %.0f%% more effect for free" % (100 * gain))
    assert 0.5 < gain < 1.5, "gain outside plausible circadian range"
    return gain

def step3_testable_prediction(gain):
    print("STEP 3 - testable prediction: phase-timed dosing beats")
    print("  clock-agnostic dosing on hard outcomes across drug classes.")
    assert gain > 0.5

def confirm_refute_panel():
    print("CONFIRM/REFUTE PANEL:")
    print("  CONFIRM if: large pragmatic trials show timed dosing wins.")
    print("  REFUTE if: real-world phases prove too unstable for fixed times.")

def main():
    step1_problem()
    gain = step2_signature_approach()
    step3_testable_prediction(gain)
    confirm_refute_panel()
    print("OK: %s solution-explorer complete (gain=%.2f)" % (RID, gain))

RID = "__RID__"
if __name__ == "__main__":
    main()
'''.replace('__LABEL__', LABEL).replace('__RID__', rid)


def demo_nocebo_effect(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\\
"""SOLUTION EXPLORER: The Nocebo Effect.
Walks the Signature proposed approach: expectation-aware framing that stays
fully honest while lowering nocebo load.
PROPOSAL ONLY - __LABEL__"""

# ---- adjustable assumptions ----
TRUE_RATE = 0.04       # true pharmacological side-effect rate
NOCEBO_GAIN_VIVID = 2.2  # symptom-report multiplier, vivid qualitative warning
NOCEBO_GAIN_CALM = 1.3   # multiplier, quantitative calm framing

def step1_problem():
    print("STEP 1 - the problem: warnings cause harm; consent requires them.")
    print("  Statin complaints track expectation, not chemistry, when blinded.")
    assert 0.0 < TRUE_RATE < 0.2

def step2_signature_approach():
    vivid = TRUE_RATE * NOCEBO_GAIN_VIVID
    calm = TRUE_RATE * NOCEBO_GAIN_CALM
    print("STEP 2 - Signature approach: same facts, different framing:")
    print("  vivid warning -> %.1f%% report; calm quantitative -> %.1f%%" % (
        100 * vivid, 100 * calm))
    assert calm < vivid
    assert 0.03 < calm < 0.08
    return vivid, calm

def step3_testable_prediction(vivid, calm):
    saved_per_1000 = (vivid - calm) * 1000
    print("STEP 3 - testable prediction: framing saves ~%.0f reports/1000" % (
        saved_per_1000))
    print("  with no loss of understanding and no missed real events.")
    assert saved_per_1000 > 20.0

def confirm_refute_panel():
    print("CONFIRM/REFUTE PANEL:")
    print("  CONFIRM if: framing trials cut reports and discontinuations with")
    print("    understanding intact.")
    print("  REFUTE if: any truthful disclosure triggers identical nocebo load.")

def main():
    step1_problem()
    vivid, calm = step2_signature_approach()
    step3_testable_prediction(vivid, calm)
    confirm_refute_panel()
    print("OK: %s solution-explorer complete (calm=%.3f)" % (RID, calm))

RID = "__RID__"
if __name__ == "__main__":
    main()
'''.replace('__LABEL__', LABEL).replace('__RID__', rid)


def demo_orphan_gpcr(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\\
"""SOLUTION EXPLORER: Deorphanizing Orphan Receptors.
Walks the Signature proposed approach: pocket-based ligand-class prediction
narrowing the metabolome haystack.
PROPOSAL ONLY - __LABEL__"""

# ---- adjustable assumptions ----
N_ORPHANS = 100
CHEMICAL_CLASSES = 6     # peptide, lipid, amine, metabolite, ion, other
HAYSTACK = 20000         # detectable metabolites/tissues-conditions

def step1_problem():
    print("STEP 1 - the problem: ~100 orphan GPCRs; a handful fall per year.")
    print("  Orexin showed one deorphanization can unlock a whole biology.")
    assert N_ORPHANS > 50

def step2_signature_approach():
    narrowed = HAYSTACK / CHEMICAL_CLASSES
    print("STEP 2 - Signature approach: pocket predicts ligand class,")
    print("  shrinking each hunt from %d to ~%d candidates." % (
        HAYSTACK, int(narrowed)))
    assert 2000 < narrowed < 5000
    return narrowed

def step3_testable_prediction(narrowed):
    print("STEP 3 - testable prediction: deorphanization rate rises and")
    print("  predicted classes match discoveries.")
    assert narrowed < HAYSTACK / 2

def confirm_refute_panel():
    print("CONFIRM/REFUTE PANEL:")
    print("  CONFIRM if: pipeline deorphanizations accelerate with class match.")
    print("  REFUTE if: most orphans prove ligand-less (constitutive).")

def main():
    step1_problem()
    narrowed = step2_signature_approach()
    step3_testable_prediction(narrowed)
    confirm_refute_panel()
    print("OK: %s solution-explorer complete (narrowed=%.0f)" % (RID, narrowed))

RID = "__RID__"
if __name__ == "__main__":
    main()
'''.replace('__LABEL__', LABEL).replace('__RID__', rid)


def demo_allosteric_design(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\\
"""SOLUTION EXPLORER: Allosteric Drug Design.
Walks the Signature proposed approach: dynamic pocket mapping with coupling
scores instead of luck.
PROPOSAL ONLY - __LABEL__"""

# ---- adjustable assumptions ----
ALPHA = 5.0        # cooperativity factor: modulator boosts affinity 5x
BASE_ACTIVITY = 0.20  # fractional target activity, disease state
DOSE_FRAC = 0.8    # fraction of max modulator occupancy at dose

def step1_problem():
    print("STEP 1 - the problem: allosteric wins (benzodiazepines, cinacalcet)")
    print("  were found, not designed; cryptic pockets hide in motion.")
    assert ALPHA > 1.0

def step2_signature_approach():
    tuned = BASE_ACTIVITY * (1 + (ALPHA - 1) * DOSE_FRAC)
    tuned = min(tuned, 1.0)
    print("STEP 2 - Signature approach: activity %.2f -> %.2f at %.0f%% occupancy" % (
        BASE_ACTIVITY, tuned, 100 * DOSE_FRAC))
    print("  ceiling effect: even at full occupancy, activity saturates <= 1.0")
    assert BASE_ACTIVITY < tuned <= 1.0
    return tuned

def step3_testable_prediction(tuned):
    print("STEP 3 - testable prediction: pipeline modulators hit predicted")
    print("  direction (potentiation vs inhibition) far above serendipity.")
    assert tuned > 0.5

def confirm_refute_panel():
    print("CONFIRM/REFUTE PANEL:")
    print("  CONFIRM if: designed modulators succeed across protein families")
    print("    with predicted direction.")
    print("  REFUTE if: transient pockets prove too fleeting for drug-like")
    print("    molecules.")

def main():
    step1_problem()
    tuned = step2_signature_approach()
    step3_testable_prediction(tuned)
    confirm_refute_panel()
    print("OK: %s solution-explorer complete (tuned=%.2f)" % (RID, tuned))

RID = "__RID__"
if __name__ == "__main__":
    main()
'''.replace('__LABEL__', LABEL).replace('__RID__', rid)


def demo_target_validation(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\\
"""SOLUTION EXPLORER: The Target Validation Crisis.
Walks the Signature proposed approach: an actuarial evidence ledger with a
genetic anchor.
PROPOSAL ONLY - __LABEL__"""

# ---- adjustable assumptions ----
P_BASE = 0.10        # base P(clinical success) per target
P_GENETIC = 0.22     # P(success) with human genetic support (~2x)
EVIDENCE_TYPES = 5

def step1_problem():
    print("STEP 1 - the problem: good drugs, wrong targets; amyloid's long")
    print("  failure taught validation can be sticky and wrong.")
    assert P_GENETIC > P_BASE

def step2_signature_approach():
    lift = P_GENETIC / P_BASE
    scored = P_BASE + (P_GENETIC - P_BASE) * 0.8  # ledger-weighted estimate
    print("STEP 2 - Signature approach: genetic anchor lifts P(success)")
    print("  %.2f -> %.2f (%.1fx); ledger score gates advancement." % (
        P_BASE, P_GENETIC, lift))
    assert 1.8 < lift < 2.6
    return lift

def step3_testable_prediction(lift):
    print("STEP 3 - testable prediction: ledger-managed portfolios beat")
    print("  historical Phase II success rates.")
    assert lift > 1.8

def confirm_refute_panel():
    print("CONFIRM/REFUTE PANEL:")
    print("  CONFIRM if: scored portfolios show higher Phase II success,")
    print("    genetic weight validated prospectively.")
    print("  REFUTE if: success proves dominated by unledgerable factors.")

def main():
    step1_problem()
    lift = step2_signature_approach()
    step3_testable_prediction(lift)
    confirm_refute_panel()
    print("OK: %s solution-explorer complete (lift=%.1fx)" % (RID, lift))

RID = "__RID__"
if __name__ == "__main__":
    main()
'''.replace('__LABEL__', LABEL).replace('__RID__', rid)


def demo_animal_model_translation(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\\
"""SOLUTION EXPLORER: Animal Model Translatability.
Walks the Signature proposed approach: fidelity-scored models gating human
trials.
PROPOSAL ONLY - __LABEL__"""

# ---- adjustable assumptions ----
FIDELITY_A = 0.45   # high-quality model historical translation rate
FIDELITY_B = 0.12   # crude model historical translation rate
N_CANDIDATES = 100

def step1_problem():
    print("STEP 1 - the problem: 1000+ stroke drugs cured mice, zero humans;")
    print("  'positive in mice' is priced as if all positives are equal.")
    assert FIDELITY_B < FIDELITY_A

def step2_signature_approach():
    pass_a = N_CANDIDATES * FIDELITY_A
    pass_b = N_CANDIDATES * FIDELITY_B
    print("STEP 2 - Signature approach: fidelity registry prices evidence.")
    print("  100 candidates: ~%.0f true translations via model A vs ~%.0f via B" % (
        pass_a, pass_b))
    assert pass_a > 3 * pass_b
    return pass_a

def step3_testable_prediction(pass_a):
    print("STEP 3 - testable prediction: fidelity-gated pipelines show higher")
    print("  Phase II success; low-fidelity models retrodict famous failures.")
    assert pass_a > 30.0

def confirm_refute_panel():
    print("CONFIRM/REFUTE PANEL:")
    print("  CONFIRM if: retrospective + prospective fidelity gating works.")
    print("  REFUTE if: translation fidelity proves essentially random.")

def main():
    step1_problem()
    pass_a = step2_signature_approach()
    step3_testable_prediction(pass_a)
    confirm_refute_panel()
    print("OK: %s solution-explorer complete (pass_a=%.0f)" % (RID, pass_a))

RID = "__RID__"
if __name__ == "__main__":
    main()
'''.replace('__LABEL__', LABEL).replace('__RID__', rid)


def demo_drug_repurposing(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\\
"""SOLUTION EXPLORER: Validating Drug Repurposing.
Walks the Signature proposed approach: a validation funnel with kill criteria
at every gate.
PROPOSAL ONLY - __LABEL__"""

# ---- adjustable assumptions ----
P_HIT = 0.20        # P(computational hit replicates in human model)
P_DOSE = 0.40       # P(effective conc. achievable at safe dose)
P_BIOMARKER = 0.50  # P(biomarker identifies responders)
P_TRIAL = 0.30      # P(passing all gates, then wins RCT)

def step1_problem():
    print("STEP 1 - the problem: sildenafil-scale wins are real but rare;")
    print("  COVID repurposing collapsed under randomized testing.")
    assert 0.0 < P_HIT < 1.0

def step2_signature_approach():
    p_funnel = P_HIT * P_DOSE * P_BIOMARKER * P_TRIAL
    print("STEP 2 - Signature approach: funnel survival = %.4f" % p_funnel)
    print("  %.2f x %.2f x %.2f x %.2f" % (P_HIT, P_DOSE, P_BIOMARKER, P_TRIAL))
    assert 0.005 < p_funnel < 0.05, "funnel rate outside plausible range"
    return p_funnel

def step3_testable_prediction(p_funnel):
    per_1000 = p_funnel * 1000
    print("STEP 3 - testable prediction: ~%.0f real wins per 1000 predictions," % per_1000)
    print("  each surviving every gate; failures published, not buried.")
    assert per_1000 > 5.0

def confirm_refute_panel():
    print("CONFIRM/REFUTE PANEL:")
    print("  CONFIRM if: funnel-validated predictions beat historical hit")
    print("    rates in RCTs.")
    print("  REFUTE if: even funnel-passers fail at historical rates.")

def main():
    step1_problem()
    p_funnel = step2_signature_approach()
    step3_testable_prediction(p_funnel)
    confirm_refute_panel()
    print("OK: %s solution-explorer complete (funnel=%.4f)" % (RID, p_funnel))

RID = "__RID__"
if __name__ == "__main__":
    main()
'''.replace('__LABEL__', LABEL).replace('__RID__', rid)


def demo_microbiome_interactions(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\\
"""SOLUTION EXPLORER: Microbiome-Drug Interactions.
Walks the Signature proposed approach: a microbial metabolic profile as a
second personal liver.
PROPOSAL ONLY - __LABEL__"""

# ---- adjustable assumptions ----
F_MICROBIAL = 0.35   # fraction of dose metabolized by gut microbes (sensitive drug)
PROFILE_ACCURACY = 0.80  # P(profile correctly predicts metabolizer status)

def step1_problem():
    print("STEP 1 - the problem: digoxin, irinotecan, levodopa all meet a")
    print("  different microbial chemical factory in every gut.")
    assert 0.0 < F_MICROBIAL < 1.0

def step2_signature_approach():
    explained = F_MICROBIAL * PROFILE_ACCURACY
    print("STEP 2 - Signature approach: functional reaction inventory, not")
    print("  species names. Explained variability: %.0f%%" % (100 * explained))
    assert 0.2 < explained < 0.4
    return explained

def step3_testable_prediction(explained):
    print("STEP 3 - testable prediction: profile-guided dosing beats standard")
    print("  dosing for microbiome-sensitive drugs.")
    assert explained > 0.2

def confirm_refute_panel():
    print("CONFIRM/REFUTE PANEL:")
    print("  CONFIRM if: prospective profile-guided trials win on exposure")
    print("    and outcomes.")
    print("  REFUTE if: profiles prove obsolete before prescriptions fill.")

def main():
    step1_problem()
    explained = step2_signature_approach()
    step3_testable_prediction(explained)
    confirm_refute_panel()
    print("OK: %s solution-explorer complete (explained=%.2f)" % (RID, explained))

RID = "__RID__"
if __name__ == "__main__":
    main()
'''.replace('__LABEL__', LABEL).replace('__RID__', rid)


def demo_biologic_immunogenicity(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\\
"""SOLUTION EXPLORER: Biologic Immunogenicity.
Walks the Signature proposed approach: a computed ADA risk score used to
engineer risk out before trials.
PROPOSAL ONLY - __LABEL__"""

# ---- adjustable assumptions ----
EPITOPE_RISK = 0.30    # P(T-cell epitopes trigger response)
AGGREGATE_RISK = 0.25  # P(aggregates trigger response)
HLA_RISK = 0.20        # P(patient HLA presents the epitopes)

def step1_problem():
    print("STEP 1 - the problem: ADAs turn miracle biologics into expensive")
    print("  placebos; even fully human antibodies provoke them.")
    assert 0.0 < EPITOPE_RISK < 1.0

def step2_signature_approach():
    p_ada = 1.0 - (1.0 - EPITOPE_RISK) * (1.0 - AGGREGATE_RISK) * (1.0 - HLA_RISK)
    print("STEP 2 - Signature approach: composite ADA risk = %.2f" % p_ada)
    deimm = p_ada * 0.35  # de-immunized redesign keeps 35% of risk
    print("  de-immunized redesign risk: %.2f" % deimm)
    assert 0.3 < p_ada < 0.7
    assert deimm < p_ada / 2
    return p_ada

def step3_testable_prediction(p_ada):
    print("STEP 3 - testable prediction: computed scores correlate with")
    print("  observed ADA rates across new biologics, prospectively.")
    assert p_ada > 0.3

def confirm_refute_panel():
    print("CONFIRM/REFUTE PANEL:")
    print("  CONFIRM if: scores predict ADA rates; redesigns lower them.")
    print("  REFUTE if: ADA formation proves dominated by stochastic factors.")

def main():
    step1_problem()
    p_ada = step2_signature_approach()
    step3_testable_prediction(p_ada)
    confirm_refute_panel()
    print("OK: %s solution-explorer complete (ada_risk=%.2f)" % (RID, p_ada))

RID = "__RID__"
if __name__ == "__main__":
    main()
'''.replace('__LABEL__', LABEL).replace('__RID__', rid)


def demo_nanomedicine_targeting(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\\
"""SOLUTION EXPLORER: Nanomedicine Targeting.
Walks the Signature proposed approach: design to measured human tumor
transport, not mouse leakiness.
PROPOSAL ONLY - __LABEL__"""

# ---- adjustable assumptions ----
EPR_MEDIAN = 0.007    # median fraction of dose reaching tumor (Wilhelm 2016)
MATCHED_BOOST = 5.0   # transport-matched design multiplier
LIVER_FRACTION = 0.60 # fraction cleared by liver regardless

def step1_problem():
    print("STEP 1 - the problem: 0.7% tumor accumulation; liver takes the rest.")
    print("  Human tumors are pressurized, not leaky like xenografts.")
    assert EPR_MEDIAN < 0.01

def step2_signature_approach():
    matched = EPR_MEDIAN * MATCHED_BOOST
    print("STEP 2 - Signature approach: 'delivery biopsy' then matched particle.")
    print("  %.2f%% -> %.2f%% tumor accumulation" % (
        100 * EPR_MEDIAN, 100 * matched))
    assert matched > 3 * EPR_MEDIAN
    assert matched < 1.0 - LIVER_FRACTION
    return matched

def step3_testable_prediction(matched):
    print("STEP 3 - testable prediction: matched particles beat free drug on")
    print("  efficacy in trials, via measured accumulation.")
    assert matched > 0.02

def confirm_refute_panel():
    print("CONFIRM/REFUTE PANEL:")
    print("  CONFIRM if: transport-matched trials show multiples of 0.7% and")
    print("    superior efficacy.")
    print("  REFUTE if: intra-tumor variability defeats all designs.")

def main():
    step1_problem()
    matched = step2_signature_approach()
    step3_testable_prediction(matched)
    confirm_refute_panel()
    print("OK: %s solution-explorer complete (matched=%.4f)" % (RID, matched))

RID = "__RID__"
if __name__ == "__main__":
    main()
'''.replace('__LABEL__', LABEL).replace('__RID__', rid)


def demo_prodrug_control(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\\
"""SOLUTION EXPLORER: Controlling Prodrug Activation.
Walks the Signature proposed approach: dual-trigger molecular logic gates.
PROPOSAL ONLY - __LABEL__"""

# ---- adjustable assumptions ----
P_TRIG1_HEALTHY = 0.30  # P(trigger 1 present in healthy tissue)
P_TRIG2_HEALTHY = 0.20  # P(trigger 2 present in healthy tissue)
P_TRIG1_DISEASE = 0.95
P_TRIG2_DISEASE = 0.90

def step1_problem():
    print("STEP 1 - the problem: clopidogrel's CYP2C19 lottery; ADC linkers")
    print("  that shed early or never release.")
    assert P_TRIG1_HEALTHY > 0.1

def step2_signature_approach():
    single = P_TRIG1_HEALTHY
    dual_healthy = P_TRIG1_HEALTHY * P_TRIG2_HEALTHY
    dual_disease = P_TRIG1_DISEASE * P_TRIG2_DISEASE
    selectivity = dual_disease / dual_healthy
    print("STEP 2 - Signature approach: two-key logic gate.")
    print("  healthy activation: %.2f -> %.3f; disease: %.2f" % (
        single, dual_healthy, dual_disease))
    print("  selectivity ratio: %.0fx" % selectivity)
    assert dual_healthy < single / 3
    assert selectivity > 10.0
    return selectivity

def step3_testable_prediction(selectivity):
    print("STEP 3 - testable prediction: dual-trigger prodrugs beat")
    print("  single-trigger analogues on target-to-healthy ratio.")
    assert selectivity > 10.0

def confirm_refute_panel():
    print("CONFIRM/REFUTE PANEL:")
    print("  CONFIRM if: dual triggers hold selectivity across patient")
    print("    enzyme variants.")
    print("  REFUTE if: disease sites never reliably co-present two triggers.")

def main():
    step1_problem()
    selectivity = step2_signature_approach()
    step3_testable_prediction(selectivity)
    confirm_refute_panel()
    print("OK: %s solution-explorer complete (selectivity=%.0fx)" % (RID, selectivity))

RID = "__RID__"
if __name__ == "__main__":
    main()
'''.replace('__LABEL__', LABEL).replace('__RID__', rid)


def demo_transporter_biology(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\\
"""SOLUTION EXPLORER: Drug Transporter Biology.
Walks the Signature proposed approach: the transporter circuit computed per
patient.
PROPOSAL ONLY - __LABEL__"""

# ---- adjustable assumptions ----
EFFLUX_RATIO = 12.0   # P-gp efflux ratio of candidate (basolateral->apical)
BRAIN_TARGET = 0.30    # desired brain/plasma ratio

def step1_problem():
    print("STEP 1 - the problem: transporters decide absorption, brain entry,")
    print("  clearance - yet most drugs lack complete profiles.")
    assert EFFLUX_RATIO > 1.0

def step2_signature_approach():
    brain_plasma = 1.0 / EFFLUX_RATIO
    inhibited = 1.0 / (EFFLUX_RATIO * 0.25)  # with P-gp inhibitor
    print("STEP 2 - Signature approach: circuit model predicts disposition.")
    print("  efflux ratio %.0f -> brain/plasma %.3f (target %.2f)" % (
        EFFLUX_RATIO, brain_plasma, BRAIN_TARGET))
    print("  with P-gp inhibited: %.3f" % inhibited)
    assert brain_plasma < BRAIN_TARGET
    assert inhibited > 3 * brain_plasma
    return brain_plasma

def step3_testable_prediction(brain_plasma):
    print("STEP 3 - testable prediction: profile-based exposure predictions")
    print("  match measured blood levels prospectively.")
    assert brain_plasma < 0.2

def confirm_refute_panel():
    print("CONFIRM/REFUTE PANEL:")
    print("  CONFIRM if: transporter profiles predict exposure and")
    print("    interactions prospectively.")
    print("  REFUTE if: in vivo regulation defeats all assay predictions.")

def main():
    step1_problem()
    bp = step2_signature_approach()
    step3_testable_prediction(bp)
    confirm_refute_panel()
    print("OK: %s solution-explorer complete (brain/plasma=%.3f)" % (RID, bp))

RID = "__RID__"
if __name__ == "__main__":
    main()
'''.replace('__LABEL__', LABEL).replace('__RID__', rid)


def demo_cancer_resistance(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\\
"""SOLUTION EXPLORER: Cancer Drug Resistance Evolution.
Walks the Signature proposed approach: manage evolution with traps and
adaptive dosing instead of maximal killing.
PROPOSAL ONLY - __LABEL__"""

# ---- adjustable assumptions ----
MUT_RATE = 1e-7        # resistance mutation per division
CELLS = 1e9            # tumor cells
FITNESS_COST_R = 0.15  # resistant clone penalty without drug

def step1_problem():
    print("STEP 1 - the problem: imatinib, EGFR inhibitors - brilliance then")
    print("  T790M. Maximal killing is maximal selection.")
    p_pre = 1.0 - (1.0 - MUT_RATE) ** CELLS
    print("  P(resistant clone pre-exists) = %.4f" % p_pre)
    assert p_pre > 0.99
    return p_pre

def step2_signature_approach(p_pre):
    print("STEP 2 - Signature approach: adaptive dosing keeps sensitives alive")
    print("  to outcompete resistants (fitness cost %.0f%%)." % (100 * FITNESS_COST_R))
    control_years = 1.2   # standard: resistance in ~1.2 years
    managed_years = 3.5   # adaptive/trap protocol projection
    gain = managed_years / control_years
    print("  time-to-resistance: %.1f -> %.1f years (%.1fx)" % (
        control_years, managed_years, gain))
    assert gain > 2.0
    return gain

def step3_testable_prediction(gain):
    print("STEP 3 - testable prediction: evolutionary protocols extend control")
    print("  by multiples, with liquid biopsy confirming predicted dynamics.")
    assert gain > 2.0

def confirm_refute_panel():
    print("CONFIRM/REFUTE PANEL:")
    print("  CONFIRM if: randomized adaptive/trap trials extend control.")
    print("  REFUTE if: tumor evolutionary creativity defeats all protocols.")

def main():
    p_pre = step1_problem()
    gain = step2_signature_approach(p_pre)
    step3_testable_prediction(gain)
    confirm_refute_panel()
    print("OK: %s solution-explorer complete (gain=%.1fx)" % (RID, gain))

RID = "__RID__"
if __name__ == "__main__":
    main()
'''.replace('__LABEL__', LABEL).replace('__RID__', rid)


def demo_cns_delivery(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\\
"""SOLUTION EXPLORER: Delivering Drugs Past the Blood-Brain Barrier.
Walks the Signature proposed approach: standardized affinity-tuned shuttle
logistics per cargo class.
PROPOSAL ONLY - __LABEL__"""

# ---- adjustable assumptions ----
KD_NM = 50.0        # shuttle-transporter dissociation constant (nM)
RECEPTOR_NM = 100.0 # effective receptor concentration at barrier
DOSE_INTERVAL_H = 168.0  # weekly dosing

def step1_problem():
    print("STEP 1 - the problem: biologics 100% excluded; intrathecal is")
    print("  invasive; every shuttle today is bespoke.")
    assert KD_NM > 0

def step2_signature_approach():
    bound = RECEPTOR_NM / (KD_NM + RECEPTOR_NM)
    print("STEP 2 - Signature approach: tuned affinity window.")
    print("  Kd=%.0f nM -> receptor occupancy %.2f (engage AND release)" % (
        KD_NM, bound))
    assert 0.3 < bound < 0.9, "affinity outside engage-release window"
    tight = 500.0 / (1.0 + 500.0)
    print("  too-tight Kd=1nM equivalent occupancy %.2f -> stuck, no release" % tight)
    return bound

def step3_testable_prediction(bound):
    print("STEP 3 - testable prediction: platform shuttles deliver multiple")
    print("  cargos to primate brain, repeat-dosed, no pathway disruption.")
    assert 0.3 < bound < 0.9

def confirm_refute_panel():
    print("CONFIRM/REFUTE PANEL:")
    print("  CONFIRM if: repeat-dose primate delivery at therapeutic levels")
    print("    with intact receptor function.")
    print("  REFUTE if: transcytosis capacity proves fundamentally too low.")

def main():
    step1_problem()
    bound = step2_signature_approach()
    step3_testable_prediction(bound)
    confirm_refute_panel()
    print("OK: %s solution-explorer complete (occupancy=%.2f)" % (RID, bound))

RID = "__RID__"
if __name__ == "__main__":
    main()
'''.replace('__LABEL__', LABEL).replace('__RID__', rid)


def demo_rational_design(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\\
"""SOLUTION EXPLORER: Why Rational Drug Design Still Falls Short.
Walks the Signature proposed approach: closed-loop calibration commons.
PROPOSAL ONLY - __LABEL__"""

# ---- adjustable assumptions ----
ERROR_START = 1.8    # kcal/mol mean affinity prediction error, uncalibrated
LEARN_RATE = 0.85    # error multiplier per doubling of calibration data
DOUBLINGS = 4

def step1_problem():
    print("STEP 1 - the problem: beautiful docked poses, failed molecules;")
    print("  serendipity still discovers most drugs.")
    assert ERROR_START > 1.0

def step2_signature_approach():
    err = ERROR_START * (LEARN_RATE ** DOUBLINGS)
    print("STEP 2 - Signature approach: every molecule calibrates the next.")
    print("  error %.2f -> %.2f kcal/mol after %d data doublings" % (
        ERROR_START, err, DOUBLINGS))
    assert err < ERROR_START * 0.6
    assert err > 0.3, "error cannot vanish - physics has floors"
    return err

def step3_testable_prediction(err):
    print("STEP 3 - testable prediction: first-synthesis success rates rise")
    print("  steadily with commons size.")
    assert err < 1.1

def confirm_refute_panel():
    print("CONFIRM/REFUTE PANEL:")
    print("  CONFIRM if: predicted-vs-measured agreement rises with data.")
    print("  REFUTE if: errors prove dominated by irreducible complexity.")

def main():
    step1_problem()
    err = step2_signature_approach()
    step3_testable_prediction(err)
    confirm_refute_panel()
    print("OK: %s solution-explorer complete (error=%.2f)" % (RID, err))

RID = "__RID__"
if __name__ == "__main__":
    main()
'''.replace('__LABEL__', LABEL).replace('__RID__', rid)


def demo_undruggable_targets(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\\
"""SOLUTION EXPLORER: The 'Undruggable' Proteome.
Walks the Signature proposed approach: systematic modality matching per
target.
PROPOSAL ONLY - __LABEL__"""

# ---- adjustable assumptions ----
MODALITIES = 5  # PROTAC, glue, covalent, RNA-targeting, allosteric
P_EACH = 0.25   # P(a given modality engages a given hard target)

def step1_problem():
    print("STEP 1 - the problem: ~85-90% of proteins lack classic pockets;")
    print("  MYC, tau, transcription factors untouchable by inhibition.")
    assert MODALITIES >= 3

def step2_signature_approach():
    p_any = 1.0 - (1.0 - P_EACH) ** MODALITIES
    print("STEP 2 - Signature approach: triage across %d modalities." % MODALITIES)
    print("  P(at least one engages) = %.2f vs inhibition-only %.2f" % (
        p_any, P_EACH))
    assert p_any > 0.7
    assert p_any > 2 * P_EACH
    return p_any

def step3_testable_prediction(p_any):
    print("STEP 3 - testable prediction: conversion rate of undruggable")
    print("  targets rises; winning modality predictable from engagement map.")
    assert p_any > 0.7

def confirm_refute_panel():
    print("CONFIRM/REFUTE PANEL:")
    print("  CONFIRM if: triage converts historically hard targets.")
    print("  REFUTE if: most hard targets resist all modalities.")

def main():
    step1_problem()
    p_any = step2_signature_approach()
    step3_testable_prediction(p_any)
    confirm_refute_panel()
    print("OK: %s solution-explorer complete (p_any=%.2f)" % (RID, p_any))

RID = "__RID__"
if __name__ == "__main__":
    main()
'''.replace('__LABEL__', LABEL).replace('__RID__', rid)


def demo_rna_delivery(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\\
"""SOLUTION EXPLORER: RNA Therapeutics Delivery.
Walks the Signature proposed approach: separate addressing from endosomal
escape; optimize each against direct measurements.
PROPOSAL ONLY - __LABEL__"""

# ---- adjustable assumptions ----
ADDRESSING = 0.40   # fraction of dose reaching target cell type
ESCAPE_NOW = 0.015  # endosomal escape today
ESCAPE_GOAL = 0.15  # engineered escape target

def step1_problem():
    print("STEP 1 - the problem: liver gets everything; escape stuck at 1-2%;")
    print("  brain, lung, muscle unreachable.")
    assert ESCAPE_NOW < 0.05

def step2_signature_approach():
    now = ADDRESSING * ESCAPE_NOW
    goal = ADDRESSING * ESCAPE_GOAL
    print("STEP 2 - Signature approach: delivery = addressing x escape.")
    print("  now: %.2f x %.3f = %.4f | goal: %.2f x %.2f = %.3f" % (
        ADDRESSING, ESCAPE_NOW, now, ADDRESSING, ESCAPE_GOAL, goal))
    assert goal > 5 * now
    return goal

def step3_testable_prediction(goal):
    print("STEP 3 - testable prediction: double-digit functional delivery in")
    print("  extrahepatic primate tissues.")
    assert goal > 0.03

def confirm_refute_panel():
    print("CONFIRM/REFUTE PANEL:")
    print("  CONFIRM if: escape metric rises 10x; extrahepatic delivery works.")
    print("  REFUTE if: escape proves fundamentally capped by cell biology.")

def main():
    step1_problem()
    goal = step2_signature_approach()
    step3_testable_prediction(goal)
    confirm_refute_panel()
    print("OK: %s solution-explorer complete (goal=%.3f)" % (RID, goal))

RID = "__RID__"
if __name__ == "__main__":
    main()
'''.replace('__LABEL__', LABEL).replace('__RID__', rid)


def demo_gene_therapy_durability(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\\
"""SOLUTION EXPLORER: Gene Therapy Delivery and Durability.
Walks the Signature proposed approach: redosable, tunable platforms instead
of one-shot AAV.
PROPOSAL ONLY - __LABEL__"""

# ---- adjustable assumptions ----
EXPRESSION_0 = 1.0    # normalized initial expression
HALF_LIFE_Y = 8.0     # expression half-life, years (one-shot)
REDOSE_BOOST = 0.9    # expression restored per redose

def step1_problem():
    print("STEP 1 - the problem: partial transduction, no redosing, fading")
    print("  expression, $2M+ per one-shot dose.")
    assert HALF_LIFE_Y > 0

def step2_signature_approach():
    y10_one = EXPRESSION_0 * 0.5 ** (10.0 / HALF_LIFE_Y)
    y10_redose = min(1.0, y10_one + REDOSE_BOOST * 0.5 ** (5.0 / HALF_LIFE_Y))
    print("STEP 2 - Signature approach: redosable platform.")
    print("  year-10 expression: one-shot %.2f vs redosed %.2f" % (
        y10_one, y10_redose))
    assert y10_redose > y10_one * 1.5
    return y10_redose

def step3_testable_prediction(y10_redose):
    print("STEP 3 - testable prediction: safe redosing restores expression;")
    print("  regulatable cassettes hold output steady for a decade.")
    assert y10_redose > 0.7

def confirm_refute_panel():
    print("CONFIRM/REFUTE PANEL:")
    print("  CONFIRM if: redosed patients regain expression; seropositives")
    print("    treatable with evasive vectors.")
    print("  REFUTE if: sterilizing immunity proves inevitable.")

def main():
    step1_problem()
    y10 = step2_signature_approach()
    step3_testable_prediction(y10)
    confirm_refute_panel()
    print("OK: %s solution-explorer complete (y10=%.2f)" % (RID, y10))

RID = "__RID__"
if __name__ == "__main__":
    main()
'''.replace('__LABEL__', LABEL).replace('__RID__', rid)


def demo_aging_therapeutics(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\\
"""SOLUTION EXPLORER: Validating Aging Therapeutics.
Walks the Signature proposed approach: biomarker-anchored composite endpoints.
PROPOSAL ONLY - __LABEL__"""

# ---- adjustable assumptions ----
EFFECT_HR = 0.85     # hazard ratio of composite endpoint on drug
N_COMPOSITE = 3000  # trial size for composite endpoint
N_LIFESPAN = 20000  # trial size if lifespan were the endpoint

def step1_problem():
    print("STEP 1 - the problem: aging isn't an indication; lifespan trials")
    print("  infeasible; biomarkers unanchored.")
    assert N_LIFESPAN > N_COMPOSITE * 3

def step2_signature_approach():
    saving = 1.0 - N_COMPOSITE / N_LIFESPAN
    print("STEP 2 - Signature approach: composite + anchored biomarker.")
    print("  trial size %d vs %d -> %.0f%% smaller, feasible" % (
        N_COMPOSITE, N_LIFESPAN, 100 * saving))
    assert saving > 0.8
    return saving

def step3_testable_prediction(saving):
    print("STEP 3 - testable prediction: a drug moves biomarkers then delays")
    print("  the composite - proving the anchor; regulators accept pathway.")
    assert EFFECT_HR < 1.0

def confirm_refute_panel():
    print("CONFIRM/REFUTE PANEL:")
    print("  CONFIRM if: anchor trial succeeds; biomarker predicts composite.")
    print("  REFUTE if: biomarkers prove epiphenomenal.")

def main():
    step1_problem()
    saving = step2_signature_approach()
    step3_testable_prediction(saving)
    confirm_refute_panel()
    print("OK: %s solution-explorer complete (saving=%.2f)" % (RID, saving))

RID = "__RID__"
if __name__ == "__main__":
    main()
'''.replace('__LABEL__', LABEL).replace('__RID__', rid)


def demo_erooms_law(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\\
"""SOLUTION EXPLORER: Eroom's Law.
Walks the Signature proposed approach: reverse the curve by making failure
cheap, fast, and decisive.
PROPOSAL ONLY - __LABEL__"""

# ---- adjustable assumptions ----
COST_1980_B = 0.06    # $B per approval, ~1980 (inflation-adjusted baseline)
DOUBLE_YEARS = 9.0   # Eroom doubling time
KILL_SHIFT = 0.40    # fraction of late failures moved early by playbook

def step1_problem():
    print("STEP 1 - the problem: cost/doubling every ~9 years for 70 years;")
    print("  $200B+/yr for ~45 approvals.")
    assert DOUBLE_YEARS > 5

def step2_signature_approach():
    years = 2026 - 1980
    cost_now = COST_1980_B * 2 ** (years / DOUBLE_YEARS)
    print("STEP 2 - Eroom projection: $%.2fB in 1980 -> $%.2fB now" % (
        COST_1980_B, cost_now))
    assert 1.0 < cost_now < 3.0, "projection should land near $1-2.6B estimates"
    late_share = 0.70  # late failures' share of cost
    cut = late_share * KILL_SHIFT
    print("  playbook: kill %.0f%% of late failures early -> cost cut ~%.0f%%" % (
        100 * KILL_SHIFT, 100 * cut))
    assert 0.2 < cut < 0.4
    return cost_now

def step3_testable_prediction(cost_now):
    print("STEP 3 - testable prediction: playbook adopters show falling")
    print("  cost-per-approval over a decade vs matched controls.")
    assert cost_now > 1.0

def confirm_refute_panel():
    print("CONFIRM/REFUTE PANEL:")
    print("  CONFIRM if: adopters bend their cost curves via earlier kills.")
    print("  REFUTE if: irreducible factors (regulation, biology) dominate.")

def main():
    step1_problem()
    cost_now = step2_signature_approach()
    step3_testable_prediction(cost_now)
    confirm_refute_panel()
    print("OK: %s solution-explorer complete (cost_now=$%.2fB)" % (RID, cost_now))

RID = "__RID__"
if __name__ == "__main__":
    main()
'''.replace('__LABEL__', LABEL).replace('__RID__', rid)


def demo_predictive_toxicology(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\\
"""SOLUTION EXPLORER: Predictive Toxicology.
Walks the Signature proposed approach: uncertainty-first prediction with
applicability-domain routing.
PROPOSAL ONLY - __LABEL__"""

# ---- adjustable assumptions ----
SENS = 0.80       # model sensitivity inside domain
SPEC = 0.85       # model specificity inside domain
PREV = 0.15       # prevalence of true toxicants in pipeline
IN_DOMAIN = 0.60  # fraction of molecules inside applicability domain

def step1_problem():
    print("STEP 1 - the problem: models interpolate, can't extrapolate;")
    print("  idiosyncratic toxicities resist all computation.")
    assert 0.0 < IN_DOMAIN < 1.0

def step2_signature_approach():
    ppv = SENS * PREV / (SENS * PREV + (1 - SPEC) * (1 - PREV))
    routed = 1.0 - IN_DOMAIN
    print("STEP 2 - Signature approach: in-domain PPV = %.2f" % ppv)
    print("  %.0f%% of molecules routed to targeted assays, not trusted blind" % (
        100 * routed))
    assert 0.4 < ppv < 0.7
    return ppv

def step3_testable_prediction(ppv):
    print("STEP 3 - testable prediction: fewer toxicology surprises for")
    print("  platform users; uncertainty scores proven calibrated.")
    assert ppv > 0.4

def confirm_refute_panel():
    print("CONFIRM/REFUTE PANEL:")
    print("  CONFIRM if: prospective surprise rate falls; calibration holds.")
    print("  REFUTE if: chemistry space proves too discontinuous to calibrate.")

def main():
    step1_problem()
    ppv = step2_signature_approach()
    step3_testable_prediction(ppv)
    confirm_refute_panel()
    print("OK: %s solution-explorer complete (ppv=%.2f)" % (RID, ppv))

RID = "__RID__"
if __name__ == "__main__":
    main()
'''.replace('__LABEL__', LABEL).replace('__RID__', rid)


def demo_pharmacogenomics_gap(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\\
"""SOLUTION EXPLORER: The Pharmacogenomics Implementation Gap.
Walks the Signature proposed approach: preemptive infrastructure - test once,
store forever, alert always.
PROPOSAL ONLY - __LABEL__"""

# ---- adjustable assumptions ----
ADR_RATE = 0.06       # actionable-ADRs per prescription opportunity
ALERT_EFFECT = 0.50   # fraction prevented when alert fires correctly
POPULATION = 100000

def step1_problem():
    print("STEP 1 - the problem: PREDICT-1 proved it in 2008; PREPARE in 2023;")
    print("  bedside still mostly ignores genetics.")
    assert 0.0 < ADR_RATE < 0.2

def step2_signature_approach():
    baseline = ADR_RATE * POPULATION
    with_infra = baseline * (1.0 - ALERT_EFFECT)
    prevented = baseline - with_infra
    nnt = POPULATION / prevented
    print("STEP 2 - Signature approach: preemptive utility.")
    print("  per 100k: %.0f ADRs -> %.0f; NNT = %.0f" % (
        baseline, with_infra, nnt))
    assert 20.0 < nnt < 60.0
    return nnt

def step3_testable_prediction(nnt):
    print("STEP 3 - testable prediction: utility systems show sustained ADR")
    print("  reductions vs matched systems, cost-effective at scale.")
    assert nnt < 60.0

def confirm_refute_panel():
    print("CONFIRM/REFUTE PANEL:")
    print("  CONFIRM if: implemented systems cut preventable ADRs durably.")
    print("  REFUTE if: alert fatigue nullifies benefit at scale.")

def main():
    step1_problem()
    nnt = step2_signature_approach()
    step3_testable_prediction(nnt)
    confirm_refute_panel()
    print("OK: %s solution-explorer complete (nnt=%.0f)" % (RID, nnt))

RID = "__RID__"
if __name__ == "__main__":
    main()
'''.replace('__LABEL__', LABEL).replace('__RID__', rid)


def demo_combination_therapy(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\\
"""SOLUTION EXPLORER: Rational Combination Therapy Design.
Walks the Signature proposed approach: set-cover over disease failure modes,
not synergy hunting.
PROPOSAL ONLY - __LABEL__"""

# ---- adjustable assumptions ----
N_ESCAPE_ROUTES = 6   # enumerable failure modes of the disease
COVER_PER_DRUG = 2.2  # mean routes blocked per drug (with overlap)
TOX_BUDGET = 3        # max drugs before toxicity overlap unacceptable

def step1_problem():
    print("STEP 1 - the problem: HAART etc. found empirically; synergy in a")
    print("  dish rarely survives the patient; search space is exponential.")
    assert N_ESCAPE_ROUTES > 3

def step2_signature_approach():
    import math as _m
    n_drugs = _m.ceil(N_ESCAPE_ROUTES / COVER_PER_DRUG)
    print("STEP 2 - Signature approach: set-cover over escape routes.")
    print("  %d routes / %.1f cover per drug -> %d drugs (budget %d)" % (
        N_ESCAPE_ROUTES, COVER_PER_DRUG, n_drugs, TOX_BUDGET))
    assert n_drugs <= TOX_BUDGET, "combination exceeds toxicity budget"
    assert n_drugs >= 2
    return n_drugs

def step3_testable_prediction(n_drugs):
    print("STEP 3 - testable prediction: coverage-designed combos beat")
    print("  empirical ones head-to-head; failures map to coverable routes.")
    assert n_drugs <= TOX_BUDGET

def confirm_refute_panel():
    print("CONFIRM/REFUTE PANEL:")
    print("  CONFIRM if: designed combinations win head-to-head trials.")
    print("  REFUTE if: escape routes prove unbounded or fully patient-specific.")

def main():
    step1_problem()
    n_drugs = step2_signature_approach()
    step3_testable_prediction(n_drugs)
    confirm_refute_panel()
    print("OK: %s solution-explorer complete (n_drugs=%d)" % (RID, n_drugs))

RID = "__RID__"
if __name__ == "__main__":
    main()
'''.replace('__LABEL__', LABEL).replace('__RID__', rid)


def demo_resistance_proof_design(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\\
"""SOLUTION EXPLORER: Designing Resistance-Proof Antibiotics.
Walks the Signature proposed approach: stacked evolutionary constraints making
resistance inaccessible, not impossible.
PROPOSAL ONLY - __LABEL__"""

# ---- adjustable assumptions ----
P_ESCAPE_EACH = 1e-6   # P(one constraint evaded per infection course)
N_CONSTRAINTS = 3      # independent stacked constraints
INFECTIONS = 1e7       # treated infections over a decade

def step1_problem():
    print("STEP 1 - the problem: every antibiotic fell; teixobactin's hype met")
    print("  lab resistance. Evolution never signs contracts.")
    assert N_CONSTRAINTS >= 2

def step2_signature_approach():
    p_joint = P_ESCAPE_EACH ** N_CONSTRAINTS
    expected = p_joint * INFECTIONS
    print("STEP 2 - Signature approach: stacked constraints multiply.")
    print("  P(joint escape) = %.1e -> expected escapes in 1e7 infections: %.2f" % (
        p_joint, expected))
    assert expected < 0.01, "escape should be inaccessible at this stacking"
    return expected

def step3_testable_prediction(expected):
    print("STEP 3 - testable prediction: red-teamed therapies show zero")
    print("  escape over billions of generations, then a clean decade.")
    assert expected < 0.01

def confirm_refute_panel():
    print("CONFIRM/REFUTE PANEL:")
    print("  CONFIRM if: extended red-teaming finds no escape; clinical")
    print("    decade stays clean.")
    print("  REFUTE if: cost-free escape around a maximal stack is demonstrated.")

def main():
    step1_problem()
    expected = step2_signature_approach()
    step3_testable_prediction(expected)
    confirm_refute_panel()
    print("OK: %s solution-explorer complete (expected=%.2f)" % (RID, expected))

RID = "__RID__"
if __name__ == "__main__":
    main()
'''.replace('__LABEL__', LABEL).replace('__RID__', rid)


DEMOS = {
 "placebo-mechanism": demo_placebo_mechanism,
 "late-stage-failure": demo_late_stage_failure,
 "personalized-dosing": demo_personalized_dosing,
 "polypharmacy-interactions": demo_polypharmacy_interactions,
 "bbb-selectivity": demo_bbb_selectivity,
 "off-target-prediction": demo_off_target_prediction,
 "dili-prediction": demo_dili_prediction,
 "antibiotic-resistance": demo_antibiotic_resistance,
 "sex-differences": demo_sex_differences,
 "pediatric-dosing": demo_pediatric_dosing,
 "chronopharmacology": demo_chronopharmacology,
 "nocebo-effect": demo_nocebo_effect,
 "orphan-gpcr": demo_orphan_gpcr,
 "allosteric-design": demo_allosteric_design,
 "target-validation": demo_target_validation,
 "animal-model-translation": demo_animal_model_translation,
 "drug-repurposing": demo_drug_repurposing,
 "microbiome-interactions": demo_microbiome_interactions,
 "biologic-immunogenicity": demo_biologic_immunogenicity,
 "nanomedicine-targeting": demo_nanomedicine_targeting,
 "prodrug-control": demo_prodrug_control,
 "transporter-biology": demo_transporter_biology,
 "cancer-resistance": demo_cancer_resistance,
 "cns-delivery": demo_cns_delivery,
 "rational-design": demo_rational_design,
 "undruggable-targets": demo_undruggable_targets,
 "rna-delivery": demo_rna_delivery,
 "gene-therapy-durability": demo_gene_therapy_durability,
 "aging-therapeutics": demo_aging_therapeutics,
 "erooms-law": demo_erooms_law,
 "predictive-toxicology": demo_predictive_toxicology,
 "pharmacogenomics-gap": demo_pharmacogenomics_gap,
 "combination-therapy": demo_combination_therapy,
 "resistance-proof-design": demo_resistance_proof_design,
}
