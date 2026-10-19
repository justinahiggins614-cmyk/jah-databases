#!/usr/bin/env python3
"""Demo programs for the Unsolved Medicine Database pair (Manon's 16:15
orders, Unsolved Problems Solved series, batch 1 - medicine).

Every demo is a SOLUTION-EXPLORER WALKTHROUGH: it walks the user through the
Signature solution approach step by step, states its adjustable assumptions
up front, computes real values from them, and ends with explicit CONFIRM
(what evidence would confirm the approach) and REFUTE (what would kill it)
panels. All are real, runnable, stdlib-only Python, machine-executed by
build.py: each prints its real computed values, asserts tight bounds (never
float exact-equality), and ends with the OK marker.

HONESTY: every walkthrough frames the approach as an exploratory research
direction - never medical advice, never a treatment claim, never presented
as established science.
"""

_PREAMBLE = "import math\n"


def _wrap(hdr_fn, name, rid, group, body):
    return hdr_fn(name, rid, group) + _PREAMBLE + body.replace(
        "NAME", __import__("json").dumps(name))


def demo_usme_common_cold(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    print("SOLUTION EXPLORER: conserved-target cold vaccine")
    print("Approach: stop aiming at 160 variable coats; aim at the inner")
    print("machinery (VP4/inner VP1) every rhinovirus must keep.")
    print("This is an exploratory research direction, not medical advice.")
    # adjustable assumptions
    n_serotypes = 160
    conserved_fraction = 0.92      # fraction of serotypes carrying the target
    take_rate = 0.70              # fraction of vaccinees mounting response
    expected_covered = n_serotypes * conserved_fraction * take_rate
    print("assumptions: serotypes=%d conserved=%.2f take=%.2f" % (
        n_serotypes, conserved_fraction, take_rate))
    print("expected serotypes covered per vaccinee: %.2f" % expected_covered)
    assert 102.9 < expected_covered < 103.1
    # vs the old strategy: one serotype per vaccine
    old_covered = 1.0 * take_rate
    improvement = expected_covered / old_covered
    print("improvement over single-serotype vaccine: %.1fx" % improvement)
    assert 146.9 < improvement < 147.3
    print("STEP 1: map conserved inner-shell regions across all serotypes")
    print("STEP 2: display them on a nasal-delivered immunogen")
    print("STEP 3: measure airway (not just blood) immunity in humans")
    print("CONFIRM: vaccinated volunteers resist challenge from MANY")
    print("  serotypes, with nasal IgA against the conserved target.")
    print("REFUTE: conserved regions prove non-immunogenic in the human")
    print("  nose, or protection fails against natural infection.")
    print("OK: %s explored the conserved target" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_usme_flu_remade(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    print("SOLUTION EXPLORER: why the yearly flu vaccine expires")
    print("Approach: quantify drift so the universal-vaccine target (the")
    print("conserved HA stem) can be judged against the moving head.")
    print("This is an exploratory research direction, not medical advice.")
    # adjustable assumptions: drift as a per-season escape probability
    p_escape = 0.35      # chance last year's immunity is evaded this year
    years = 5
    p_still_protected = (1.0 - p_escape) ** years
    print("assumptions: yearly escape probability=%.2f horizon=%d years" % (
        p_escape, years))
    print("protection surviving %d years of drift: %.4f" % (years, p_still_protected))
    assert 0.1160 < p_still_protected < 0.1161
    # universal candidate: stem changes far slower
    p_stem_escape = 0.03
    p_stem_survives = (1.0 - p_stem_escape) ** years
    print("stem-target protection surviving %d years: %.4f" % (years, p_stem_survives))
    assert 0.8586 < p_stem_survives < 0.8588
    gain = p_stem_survives / p_still_protected
    print("durability gain of stem targeting: %.2fx" % gain)
    assert 7.39 < gain < 7.41
    print("STEP 1: quantify head-drift escape from surveillance data")
    print("STEP 2: elicit stem antibodies and measure their breadth")
    print("STEP 3: test multi-season protection in humans")
    print("CONFIRM: stem-vaccinated cohorts show protection across drifted")
    print("  seasons and against shifted strains.")
    print("REFUTE: immunodominance keeps pulling responses to the head, or")
    print("  stem antibodies fail to prevent human infection.")
    print("OK: %s explored the drift math" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_usme_placebo(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    print("SOLUTION EXPLORER: mapping the placebo pharmacy")
    print("Approach: decompose placebo analgesia into measurable")
    print("neurochemical parts, starting from the naloxone experiment.")
    print("This is an exploratory research direction, not medical advice.")
    # adjustable assumptions from the literature pattern
    total_effect = 0.50        # standardized placebo analgesia effect
    opioid_share = 0.60        # fraction blocked by naloxone
    opioid_part = total_effect * opioid_share
    non_opioid = total_effect - opioid_part
    print("assumptions: total effect=%.2f opioid share=%.2f" % (
        total_effect, opioid_share))
    print("opioid-carried relief: %.3f" % opioid_part)
    print("non-opioid remainder (cannabinoid, dopamine, expectancy): %.3f" % non_opioid)
    assert 0.2999 < opioid_part < 0.3001
    assert 0.1999 < non_opioid < 0.2001
    # if the pharmacy could be deliberately engaged at 80% efficiency
    deliberate = total_effect * 0.80
    print("deliberate engagement at 80%% efficiency: %.3f effect" % deliberate)
    assert 0.3999 < deliberate < 0.4001
    print("STEP 1: separate opioid vs non-opioid parts per condition")
    print("STEP 2: trace expectation circuits to each chemical system")
    print("STEP 3: test ethical expectancy-boosting alongside real drugs")
    print("CONFIRM: distinct neurochemical signatures per condition, and")
    print("  expectancy protocols boost drug effects dose-sparingly.")
    print("REFUTE: the effect collapses to reporting bias once objective")
    print("  biomarkers are required, in condition after condition.")
    print("OK: %s explored the inner pharmacy" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_usme_allergy_misfire(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    print("SOLUTION EXPLORER: reissuing the immune system's orders")
    print("Approach: model tolerance as a learned classifier and ask what")
    print("retraining schedule rewrites a misclassification.")
    print("This is an exploratory research direction, not medical advice.")
    # adjustable assumptions: oral immunotherapy dose-escalation model
    steps = 12
    p_step_success = 0.88     # per-step tolerance gain probability
    p_desensitized = p_step_success ** steps
    print("assumptions: escalation steps=%d per-step success=%.2f" % (
        steps, p_step_success))
    print("probability of completing desensitization: %.4f" % p_desensitized)
    assert 0.21566 < p_desensitized < 0.21568
    # sustained unresponsiveness is rarer than desensitization
    p_sustained_given_desens = 0.35
    p_cured = p_desensitized * p_sustained_given_desens
    print("probability of durable, treatment-free tolerance: %.4f" % p_cured)
    assert 0.07547 < p_cured < 0.07550
    print("STEP 1: find the misclassification moment in early life")
    print("STEP 2: test retraining schedules that maximize durable tolerance")
    print("STEP 3: validate with treatment-free follow-up, not on-drug scores")
    print("CONFIRM: retrained patients stay tolerant years off therapy with")
    print("  regulatory T cell signatures to prove the mechanism.")
    print("REFUTE: tolerance always decays after therapy stops - the")
    print("  classifier reverts, and no schedule changes that.")
    print("OK: %s explored the tolerance rewrite" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_usme_chronic_pain(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    print("SOLUTION EXPLORER: finding the pain volume knob")
    print("Approach: model chronic pain as signal times pathological gain,")
    print("then hunt the gain's molecular identity (glia, descending control).")
    print("This is an exploratory research direction, not medical advice.")
    # adjustable assumptions: allodynia implies a gain factor
    normal_touch_signal = 1.0
    reported_pain = 6.5          # on a 0-10 scale for light touch
    gain = reported_pain / normal_touch_signal
    print("assumptions: touch signal=%.1f reported pain=%.1f" % (
        normal_touch_signal, reported_pain))
    print("implied central gain: %.2fx" % gain)
    assert 6.49 < gain < 6.51
    # a therapy that halves the gain
    treated_gain = gain * 0.5
    treated_pain = normal_touch_signal * treated_gain
    print("pain after halving the gain: %.2f" % treated_pain)
    assert 3.24 < treated_pain < 3.26
    # vs opioids which scale the signal, not the gain
    opioid_signal_cut = 0.30
    opioid_pain = normal_touch_signal * (1 - opioid_signal_cut) * gain
    print("pain after opioid signal cut: %.2f (gain untouched)" % opioid_pain)
    assert 4.54 < opioid_pain < 4.56
    print("STEP 1: measure the gain objectively (quantitative sensory testing)")
    print("STEP 2: identify the gain's drivers - glial activation markers")
    print("STEP 3: test gain-resetting vs signal-muffling in trials")
    print("CONFIRM: a gain biomarker predicts who suffers chronic pain, and")
    print("  gain-targeted therapy normalizes it with function restored.")
    print("REFUTE: no objective gain measure separates patients from")
    print("  controls - the knob cannot be found because it is not there.")
    print("OK: %s explored the volume knob" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_usme_migraine(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    print("SOLUTION EXPLORER: the primed brain and the last straw")
    print("Approach: model migraine as a threshold process - priming raises")
    print("baseline excitability until an ordinary trigger crosses the line.")
    print("This is an exploratory research direction, not medical advice.")
    # adjustable assumptions
    baseline = 0.45        # resting excitability (arbitrary units)
    priming = 0.40         # accumulated priming before an attack window
    trigger = 0.25         # a trigger that is harmless on ordinary days
    threshold = 1.00
    total = baseline + priming + trigger
    print("assumptions: baseline=%.2f priming=%.2f trigger=%.2f threshold=%.2f" % (
        baseline, priming, trigger, threshold))
    print("ordinary day: %.2f (no attack)" % (baseline + trigger))
    print("primed day: %.2f -> ATTACK" % total)
    assert 0.69 < (baseline + trigger) < 0.71
    assert 1.09 < total < 1.11
    # prevention by lowering priming 50%
    prevented = baseline + priming * 0.5 + trigger
    print("with priming halved: %.2f (no attack)" % prevented)
    assert 0.89 < prevented < 0.91
    print("STEP 1: find the priming signal - hypothalamic/brainstem markers")
    print("STEP 2: build a pre-attack predictor from physiology")
    print("STEP 3: test priming-lowering prevention vs trigger avoidance")
    print("CONFIRM: a priming biomarker forecasts attacks days ahead, and")
    print("  lowering it prevents attacks better than dodging triggers.")
    print("REFUTE: no pre-attack signal exists - attacks are random")
    print("  threshold crossings with no measurable priming phase.")
    print("OK: %s explored the priming threshold" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_usme_sleep_biology(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    print("SOLUTION EXPLORER: pricing the night shift")
    print("Approach: quantify what each sleep job costs to skip, starting")
    print("with glymphatic waste clearance as a measurable example.")
    print("This is an exploratory research direction, not medical advice.")
    # adjustable assumptions: clearance modeled as exponential decay
    halflife_sleep = 4.0    # hours to halve brain waste during sleep
    halflife_wake = 12.0    # hours during wakefulness
    k_sleep = math.log(2) / halflife_sleep
    k_wake = math.log(2) / halflife_wake
    print("assumptions: waste half-life sleep=%.1fh wake=%.1fh" % (
        halflife_sleep, halflife_wake))
    print("clearance rate sleep: %.4f /h, wake: %.4f /h" % (k_sleep, k_wake))
    assert 0.1732 < k_sleep < 0.1734
    assert 0.0577 < k_wake < 0.0579
    # waste remaining after an 8h night vs 8h of forced wakefulness
    waste_after_sleep = math.exp(-k_sleep * 8.0)
    waste_after_wake = math.exp(-k_wake * 8.0)
    print("waste left after 8h asleep: %.3f; after 8h awake: %.3f" % (
        waste_after_sleep, waste_after_wake))
    assert 0.2499 < waste_after_sleep < 0.2501
    assert 0.6299 < waste_after_wake < 0.6301
    print("STEP 1: measure each sleep job's dose-response separately")
    print("STEP 2: test whether any job can be done awake (the hard test)")
    print("STEP 3: assemble the minimal theory: which jobs REQUIRE sleep")
    print("CONFIRM: specific harms trace to specific lost stages, and no")
    print("  waking intervention replaces a stage's function.")
    print("REFUTE: all sleep functions prove replaceable awake - sleep is")
    print("  then a habit of evolution, not a necessity.")
    print("OK: %s explored the night shift ledger" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_usme_obesity_setpoint(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    print("SOLUTION EXPLORER: reprogramming the defended weight")
    print("Approach: model the thermostat, then ask what moves the setting")
    print("instead of overriding it with lifelong drugs.")
    print("This is an exploratory research direction, not medical advice.")
    # adjustable assumptions: metabolic adaptation after weight loss
    setpoint = 100.0       # kg defended weight
    lost = 12.0            # kg lost by dieting
    adaptation = 0.35      # fraction of loss the body fights via slowdown+hunger
    defended_regain = lost * adaptation
    print("assumptions: setpoint=%.0fkg lost=%.0fkg adaptation=%.2f" % (
        setpoint, lost, adaptation))
    print("expected regain pressure: %.2f kg" % defended_regain)
    assert 4.19 < defended_regain < 4.21
    # GLP-1 overrides the thermostat while dosed
    override = 0.85        # fraction of adaptation suppressed on drug
    on_drug_regain = defended_regain * (1 - override)
    print("regain pressure on drug: %.3f kg" % on_drug_regain)
    assert 0.629 < on_drug_regain < 0.631
    # true set-point reset would zero the adaptation
    print("regain pressure after true reset: 0.00 kg")
    print("STEP 1: locate the defended number in hypothalamic circuitry")
    print("STEP 2: find what writes it - developmental and environmental inputs")
    print("STEP 3: test reset strategies with off-treatment follow-up")
    print("CONFIRM: weight stays off years after treatment ends, with the")
    print("  defended weight measurably re-encoded.")
    print("REFUTE: every intervention's effect vanishes off treatment - the")
    print("  setting is written in indelible ink.")
    print("OK: %s explored the thermostat" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_usme_vaccine_durability(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    print("SOLUTION EXPLORER: the librarian's decision rule")
    print("Approach: compare antibody decay curves of durable vs fading")
    print("vaccines to extract the signature of lifelong memory.")
    print("This is an exploratory research direction, not medical advice.")
    # adjustable assumptions: exponential antibody decay
    hl_measles = 200.0 * 365.0   # effectively lifelong (days)
    hl_pertussis = 1.1 * 365.0   # ~1.1 years (days)
    def remaining(hl, days):
        return 0.5 ** (days / hl)
    y5 = 5 * 365.0
    r_measles = remaining(hl_measles, y5)
    r_pertussis = remaining(hl_pertussis, y5)
    print("assumptions: measles Ab half-life=%.0f days, pertussis=%.0f days" % (
        hl_measles, hl_pertussis))
    print("antibody remaining at 5 years: measles=%.4f pertussis=%.4f" % (
        r_measles, r_pertussis))
    assert 0.98281 < r_measles < 0.98284
    assert 0.04281 < r_pertussis < 0.04284
    ratio = r_measles / r_pertussis
    print("durability ratio at 5 years: %.1fx" % ratio)
    assert 22.9 < ratio < 23.1
    print("STEP 1: compare germinal-center reactions of durable vs fading vaccines")
    print("STEP 2: extract the early signature that predicts longevity")
    print("STEP 3: engineer adjuvants/doses to reproduce the durable signature")
    print("CONFIRM: an early immune signature predicts multi-year protection,")
    print("  and engineered vaccines bearing it last.")
    print("REFUTE: no early measurement predicts durability - longevity is")
    print("  discovered only by waiting, forever.")
    print("OK: %s explored the durability signature" % NAME)
if __name__ == "__main__":
    main()
''')


DEMOS = {
    "common_cold": demo_usme_common_cold,
    "flu_remade": demo_usme_flu_remade,
    "placebo": demo_usme_placebo,
    "allergy_misfire": demo_usme_allergy_misfire,
    "chronic_pain": demo_usme_chronic_pain,
    "migraine": demo_usme_migraine,
    "sleep_biology": demo_usme_sleep_biology,
    "obesity_setpoint": demo_usme_obesity_setpoint,
    "vaccine_durability": demo_usme_vaccine_durability,
}


def demo_usme_sepsis(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    print("SOLUTION EXPLORER: staging the storm before drugging it")
    print("Approach: model sepsis as two opposite immune states and compute")
    print("the cost of treating the wrong state - the staging argument.")
    print("This is an exploratory research direction, not medical advice.")
    # adjustable assumptions
    p_hyper = 0.55         # fraction of patients in hyper-inflammatory state
    p_hypo = 1.0 - p_hyper
    benefit_right = 0.12   # absolute mortality reduction when matched
    harm_wrong = 0.08      # absolute mortality increase when mismatched
    # blind one-size treatment: half the patients get the wrong drug
    blind = p_hyper * benefit_right - p_hypo * harm_wrong
    staged = p_hyper * benefit_right + p_hypo * benefit_right
    print("assumptions: hyper fraction=%.2f benefit=%.2f harm=%.2f" % (
        p_hyper, benefit_right, harm_wrong))
    print("blind treatment net effect: %+.4f" % blind)
    print("staged treatment net effect: %+.4f" % staged)
    assert 0.0299 < blind < 0.0301
    assert 0.1199 < staged < 0.1201
    gain = staged / blind
    print("staging multiplies benefit: %.2fx" % gain)
    assert 3.99 < gain < 4.01
    print("STEP 1: validate a rapid immune-state blood signature")
    print("STEP 2: run state-stratified trials - the trials history skipped")
    print("STEP 3: match drug to state at the bedside in hours")
    print("CONFIRM: staged patients survive more; the signature predicts")
    print("  who is inflamed vs paralyzed before treatment.")
    print("REFUTE: states prove unmeasurable in time, or matched therapy")
    print("  shows no advantage over supportive care.")
    print("OK: %s explored the staging argument" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_usme_long_covid(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    print("SOLUTION EXPLORER: one umbrella, several diseases")
    print("Approach: model post-viral illness as a mixture of mechanisms")
    print("and compute why single treatments keep failing.")
    print("This is an exploratory research direction, not medical advice.")
    # adjustable assumptions: 4 mechanisms, one treatment hits one
    mechanisms = ["viral persistence", "autoimmunity", "microclots",
                  "autonomic injury"]
    shares = [0.30, 0.25, 0.20, 0.25]
    p_hit = 0.60           # treatment efficacy within its mechanism
    overall = sum(s * p_hit if m == "microclots" else 0.0
                  for m, s in zip(mechanisms, shares))
    print("assumptions: mechanisms=%s" % (", ".join(mechanisms)))
    print("a microclot-targeted drug's trial-wide response: %.3f" % overall)
    assert 0.1199 < overall < 0.1201
    # stratified: treat only the matching subgroup
    stratified = p_hit
    print("same drug in its matched subgroup: %.2f" % stratified)
    assert 0.599 < stratified < 0.601
    lift = stratified / overall
    print("stratification lift: %.2fx" % lift)
    assert 4.99 < lift < 5.01
    print("STEP 1: phenotype patients deeply - find the real subgroups")
    print("STEP 2: assign each subgroup its mechanism with biomarkers")
    print("STEP 3: run subgroup-matched trials, not umbrella trials")
    print("CONFIRM: subgroup-matched treatments restore function where")
    print("  umbrella trials showed nothing.")
    print("REFUTE: no stable subgroups exist - every patient is a unique")
    print("  mixture no stratification can capture.")
    print("OK: %s explored the mixture model" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_usme_antibiotic_resistance(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    print("SOLUTION EXPLORER: outrunning evolution")
    print("Approach: model resistance as logistic spread and compare")
    print("kill-everything drugs vs disarm-without-killing strategies.")
    print("This is an exploratory research direction, not medical advice.")
    # adjustable assumptions: logistic growth of resistant fraction
    r0 = 0.02             # current resistant fraction
    growth = 0.45         # per-year logistic growth rate under selection
    def resistant(t):
        return 1.0 / (1.0 + ((1 - r0) / r0) * math.exp(-growth * t))
    r5 = resistant(5.0)
    print("assumptions: initial=%.2f growth=%.2f/yr" % (r0, growth))
    print("resistant fraction in 5 years: %.4f" % r5)
    assert 0.16221 < r5 < 0.16223
    # anti-virulence: lower selection pressure -> slower growth
    growth_av = 0.10
    def resistant_av(t):
        return 1.0 / (1.0 + ((1 - r0) / r0) * math.exp(-growth_av * t))
    r5_av = resistant_av(5.0)
    print("with disarm-not-kill strategy: %.4f" % r5_av)
    assert 0.0325 < r5_av < 0.0327
    print("STEP 1: measure selection pressure per strategy, not just cure rate")
    print("STEP 2: pair new drugs with rapid diagnostics from day one")
    print("STEP 3: fix the economics - reward availability, not volume")
    print("CONFIRM: low-pressure strategies show flat resistance curves over")
    print("  years where kill-drugs climb logistically.")
    print("REFUTE: bacteria evolve around disarming as fast as killing -")
    print("  selection finds a way regardless.")
    print("OK: %s explored the resistance race" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_usme_autoimmune_triggers(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    print("SOLUTION EXPLORER: catching the truce breaking")
    print("Approach: Bayesian update on the Epstein-Barr/MS link - how")
    print("strong must trigger evidence be to justify prevention trials.")
    print("This is an exploratory research direction, not medical advice.")
    # adjustable assumptions: prior and evidence strength
    prior = 0.02          # prior probability EBV is causal for MS
    likelihood_ratio = 32.0   # 32-fold MS risk increase after EBV (study scale)
    prior_odds = prior / (1 - prior)
    post_odds = prior_odds * likelihood_ratio
    posterior = post_odds / (1 + post_odds)
    print("assumptions: prior=%.2f likelihood ratio=%.1f" % (prior, likelihood_ratio))
    print("posterior probability EBV is causal: %.4f" % posterior)
    assert 0.3950 < posterior < 0.3952
    # expected value of an EBV vaccine that prevents fraction f of MS
    f_prevented = 0.80
    ms_cases_per_100k = 100.0
    prevented = ms_cases_per_100k * posterior * f_prevented
    print("expected MS cases prevented per 100k vaccinated: %.2f" % prevented)
    assert 31.60 < prevented < 31.62
    print("STEP 1: nail the mechanism - how EBV breaks tolerance")
    print("STEP 2: test EBV vaccines with MS prevention as endpoint")
    print("STEP 3: generalize the trigger-hunt to lupus, RA, T1D")
    print("CONFIRM: EBV-naive cohorts show near-zero MS; vaccinees show")
    print("  reduced MS decades later.")
    print("REFUTE: EBV proves necessary but the true trigger is a co-factor")
    print("  EBV merely enables - prevention fails.")
    print("OK: %s explored the trigger math" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_usme_t1d_prevention(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    print("SOLUTION EXPLORER: the prevention window")
    print("Approach: model beta-cell decline from antibody appearance to")
    print("symptoms, and size the window where stopping the attack works.")
    print("This is an exploratory research direction, not medical advice.")
    # adjustable assumptions: exponential beta-cell decline
    years_to_symptoms = 4.0
    remaining_at_diagnosis = 0.15   # fraction of beta cells left
    k = -math.log(remaining_at_diagnosis) / years_to_symptoms
    print("assumptions: %.1f years antibody-to-symptom, %.0f%% cells at diagnosis" % (
        years_to_symptoms, remaining_at_diagnosis * 100))
    print("decline rate: %.4f per year" % k)
    assert 0.4742 < k < 0.4744
    # intervene at year 1: cells remaining
    cells_at_1 = math.exp(-k * 1.0)
    print("cells remaining if caught at year 1: %.3f" % cells_at_1)
    assert 0.6222 < cells_at_1 < 0.6224
    # teplizumab-style delay: shift the curve by 2.5 years
    delay = 2.5
    effective_years = years_to_symptoms + delay
    print("symptom onset delayed to year: %.1f" % effective_years)
    assert 6.49 < effective_years < 6.51
    print("STEP 1: screen antibody-positive children into the window")
    print("STEP 2: test tolerance-inducing (not just delaying) therapies")
    print("STEP 3: prove permanent drug-free halt, not postponement")
    print("CONFIRM: treated at-risk children never progress, with beta-cell")
    print("  function preserved years off therapy.")
    print("REFUTE: the attack always resumes after therapy - delay is the")
    print("  ceiling, and tolerance cannot be taught.")
    print("OK: %s explored the prevention window" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_usme_microbiome_map(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    print("SOLUTION EXPLORER: from census to causation")
    print("Approach: compute what it costs - in samples and precision - to")
    print("prove one strain causes one disease effect.")
    print("This is an exploratory research direction, not medical advice.")
    # adjustable assumptions: power calculation sketch for strain effect
    effect = 0.30          # standardized effect of the strain
    noise = 1.0            # background variation
    # samples per group for 80% power at p<0.05 (two-sample, approx)
    n = int(math.ceil(2 * ((1.96 + 0.84) ** 2) * (noise / effect) ** 2))
    print("assumptions: strain effect=%.2f background noise=%.1f" % (effect, noise))
    print("samples per group needed: %d" % n)
    assert 173 < n < 177
    # genus-level blur dilutes the effect 3x
    effect_blur = effect / 3.0
    n_blur = int(math.ceil(2 * ((1.96 + 0.84) ** 2) * (noise / effect_blur) ** 2))
    print("at genus-level blur: %d per group (%.1fx more)" % (n_blur, n_blur / n))
    assert 8.9 < n_blur / n < 9.1
    print("STEP 1: measure at strain level with functional readouts")
    print("STEP 2: test causation in defined-consortium experiments")
    print("STEP 3: confirm in humans with interventional trials")
    print("CONFIRM: defined microbial changes produce defined disease")
    print("  changes in randomized human trials.")
    print("REFUTE: every association dissolves under intervention - the")
    print("  microbiome is scenery, not machinery.")
    print("OK: %s explored the causation ladder" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_usme_depression_biology(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    print("SOLUTION EXPLORER: matching patient to mechanism")
    print("Approach: model depression as subtypes and compute the prize for")
    print("treating the subtype instead of the syndrome.")
    print("This is an exploratory research direction, not medical advice.")
    # adjustable assumptions: 3 subtypes, one drug per subtype
    subtypes = ["inflammatory", "plasticity-loss", "circadian"]
    shares = [0.30, 0.45, 0.25]
    p_match = 0.65         # response when drug matches subtype
    p_mismatch = 0.25      # response when it does not
    # current: everyone gets the same first drug (matches 1/3 of subtypes)
    current = shares[0] * p_match + (shares[1] + shares[2]) * p_mismatch
    matched = sum(s * p_match for s in shares)
    print("assumptions: subtypes=%s response matched=%.2f mismatched=%.2f" % (
        subtypes, p_match, p_mismatch))
    print("one-size response rate: %.4f" % current)
    print("subtype-matched response rate: %.4f" % matched)
    assert 0.3699 < current < 0.3701
    assert 0.6499 < matched < 0.6501
    lift = matched / current
    print("matching lift: %.2fx" % lift)
    assert 1.75 < lift < 1.77
    print("STEP 1: define subtypes with biomarkers that predict response")
    print("STEP 2: validate prospectively - predict BEFORE treating")
    print("STEP 3: develop one mechanism-matched therapy per subtype")
    print("CONFIRM: biomarker-matched patients respond at far higher rates,")
    print("  and the resistant third shrinks.")
    print("REFUTE: subtypes prove unstable - patients slide between them,")
    print("  and matching adds nothing over trial and error.")
    print("OK: %s explored the subtype match" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_usme_schizophrenia(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    print("SOLUTION EXPLORER: the over-pruned city")
    print("Approach: quantify adolescent pruning and ask how much excess")
    print("explains the break - the C4 complement lead.")
    print("This is an exploratory research direction, not medical advice.")
    # adjustable assumptions: normal vs excess pruning in adolescence
    normal_prune = 0.30     # fraction of synapses pruned normally
    excess = 0.12          # additional pruning in high-risk trajectory
    total_prune = normal_prune + excess
    connectivity = 1.0 - total_prune
    normal_connectivity = 1.0 - normal_prune
    print("assumptions: normal pruning=%.0f%% excess=%.0f%%" % (
        normal_prune * 100, excess * 100))
    print("connectivity: normal=%.2f high-risk=%.2f" % (
        normal_connectivity, connectivity))
    assert 0.699 < normal_connectivity < 0.701
    assert 0.579 < connectivity < 0.581
    deficit = (normal_connectivity - connectivity) / normal_connectivity
    print("relative connectivity deficit: %.4f" % deficit)
    assert 0.1713 < deficit < 0.1715
    # rescue: halving the excess
    rescued = 1.0 - (normal_prune + excess * 0.5)
    print("connectivity if excess halved: %.3f" % rescued)
    assert 0.639 < rescued < 0.641
    print("STEP 1: measure pruning longitudinally in high-risk youth")
    print("STEP 2: test whether C4/complement blockade normalizes it")
    print("STEP 3: prove prevention - fewer conversions to psychosis")
    print("CONFIRM: excessive pruning precedes onset, and normalizing it")
    print("  prevents psychosis in high-risk cohorts.")
    print("REFUTE: pruning is normal in future patients - the C4 signal is")
    print("  correlation without a causal role.")
    print("OK: %s explored the pruning ledger" % NAME)
if __name__ == "__main__":
    main()
''')


DEMOS.update({
    "sepsis": demo_usme_sepsis,
    "long_covid": demo_usme_long_covid,
    "antibiotic_resistance": demo_usme_antibiotic_resistance,
    "autoimmune_triggers": demo_usme_autoimmune_triggers,
    "t1d_prevention": demo_usme_t1d_prevention,
    "microbiome_map": demo_usme_microbiome_map,
    "depression_biology": demo_usme_depression_biology,
    "schizophrenia": demo_usme_schizophrenia,
})


def demo_usme_hiv_cure(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    print("SOLUTION EXPLORER: emptying the sleeper cells")
    print("Approach: model latent reservoir decay and ask what it takes to")
    print("reach zero - shock-and-kill vs block-and-lock.")
    print("This is an exploratory research direction, not medical advice.")
    # adjustable assumptions: reservoir half-life on therapy ~44 months
    halflife_months = 44.0
    reservoir_0 = 1e6        # latently infected cells
    k = math.log(2) / halflife_months
    years = 30.0
    remaining = reservoir_0 * math.exp(-k * years * 12.0)
    print("assumptions: reservoir=%g cells half-life=%.0f months" % (
        reservoir_0, halflife_months))
    print("cells remaining after %.0f years of therapy: %.1f" % (years, remaining))
    assert 3443.6 < remaining < 3443.8
    # years to reach <1 cell at natural decay
    t_zero = math.log(reservoir_0) / k * (1.0 / 12.0)
    print("years to natural eradication: %.1f (longer than a life)" % t_zero)
    assert 73.0 < t_zero < 73.2
    # shock-and-kill that multiplies clearance 20x
    k2 = k * 20.0
    t_shock = math.log(reservoir_0) / k2 * (1.0 / 12.0)
    print("years with 20x clearance: %.2f" % t_shock)
    assert 3.64 < t_shock < 3.66
    print("STEP 1: measure the intact (not defective) reservoir precisely")
    print("STEP 2: test clearance multipliers in humans safely")
    print("STEP 3: prove years of drug-free remission, tissue by tissue")
    print("CONFIRM: reservoir shrinks toward zero with ultrasensitive")
    print("  assays, and remission holds years off drugs.")
    print("REFUTE: the reservoir proves unshrinkable - every wake attempt")
    print("  reseeds it, and silence is the ceiling.")
    print("OK: %s explored the reservoir math" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_usme_drug_resistant_tb(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    print("SOLUTION EXPLORER: starving the fortress")
    print("Approach: model how treatment length breeds resistance, and what")
    print("a sterilizing short course would be worth.")
    print("This is an exploratory research direction, not medical advice.")
    # adjustable assumptions: incomplete-course probability grows with duration
    months = 6.0
    p_incomplete_per_month = 0.06
    p_incomplete = 1.0 - (1.0 - p_incomplete_per_month) ** months
    p_resistance_given_incomplete = 0.15
    p_resistance = p_incomplete * p_resistance_given_incomplete
    print("assumptions: %.0f-month course, %.0f%% monthly dropout risk" % (
        months, p_incomplete_per_month * 100))
    print("incomplete-course probability: %.4f" % p_incomplete)
    print("resistance-generation probability: %.4f" % p_resistance)
    assert 0.31012 < p_incomplete < 0.31015
    assert 0.04651 < p_resistance < 0.04653
    # a 1-month sterilizing course
    p_incomplete_short = 1.0 - (1.0 - p_incomplete_per_month) ** 1.0
    p_res_short = p_incomplete_short * p_resistance_given_incomplete
    print("with a 1-month sterilizing course: %.4f" % p_res_short)
    assert 0.00899 < p_res_short < 0.00901
    cut = p_resistance / p_res_short
    print("resistance-generation cut: %.2fx" % cut)
    assert 5.15 < cut < 5.17
    print("STEP 1: find drugs that kill dormant, non-replicating bacteria")
    print("STEP 2: prove sterilization in months, not half-years")
    print("STEP 3: deploy in resistance-proof combinations from day one")
    print("CONFIRM: short courses sterilize with relapse rates matching")
    print("  long courses, and resistance curves flatten.")
    print("REFUTE: dormancy proves undruggable - every short course")
    print("  relapses, and length is irreducible.")
    print("OK: %s explored the fortress math" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_usme_universal_flu_vaccine(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    print("SOLUTION EXPLORER: retraining the student's attention")
    print("Approach: model immunodominance as a competition between head")
    print("and stem responses, and compute the refocusing needed.")
    print("This is an exploratory research direction, not medical advice.")
    # adjustable assumptions: antibody response split head vs stem
    head_share = 0.90       # immunodominance: 90% of response hits the head
    stem_share = 1.0 - head_share
    head_durability = 1.0   # one season
    stem_durability = 8.0   # seasons
    effective = head_share * head_durability + stem_share * stem_durability
    print("assumptions: head share=%.2f stem share=%.2f" % (head_share, stem_share))
    print("effective protection (season-equivalents): %.2f" % effective)
    assert 1.69 < effective < 1.71
    # refocused: 70% of response to the stem
    stem_share2 = 0.70
    head_share2 = 1.0 - stem_share2
    effective2 = head_share2 * head_durability + stem_share2 * stem_durability
    print("refocused protection: %.2f season-equivalents" % effective2)
    assert 5.89 < effective2 < 5.91
    print("STEP 1: build immunogens that hide the head and show the stem")
    print("STEP 2: prove refocused responses in humans, durably")
    print("STEP 3: demonstrate multi-season, mismatched-strain protection")
    print("CONFIRM: refocused vaccinees carry stem antibodies for years")
    print("  and resist drifted and shifted strains.")
    print("REFUTE: the immune system always reverts to the head -")
    print("  immunodominance is unteachable.")
    print("OK: %s explored the refocusing math" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_usme_malaria_durability(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    print("SOLUTION EXPLORER: making protection outlast the season")
    print("Approach: model efficacy waning and compute the booster burden")
    print("vs a durable multi-stage design.")
    print("This is an exploratory research direction, not medical advice.")
    # adjustable assumptions: exponential efficacy waning
    eff_0 = 0.55           # initial efficacy
    halflife = 1.2         # years
    def eff(t):
        return eff_0 * 0.5 ** (t / halflife)
    e1, e3 = eff(1.0), eff(3.0)
    print("assumptions: initial efficacy=%.2f waning half-life=%.1f yr" % (
        eff_0, halflife))
    print("efficacy at 1 yr: %.4f; at 3 yr: %.4f" % (e1, e3))
    assert 0.30866 < e1 < 0.30869
    assert 0.0972 < e3 < 0.0974
    # durable design: half-life 6 years
    halflife2 = 6.0
    def eff2(t):
        return eff_0 * 0.5 ** (t / halflife2)
    e3b = eff2(3.0)
    print("durable-design efficacy at 3 yr: %.4f" % e3b)
    assert 0.3888 < e3b < 0.3890
    gain = e3b / e3
    print("3-year protection gain: %.2fx" % gain)
    assert 3.99 < gain < 4.01
    print("STEP 1: find why natural immunity takes years - copy its lessons")
    print("STEP 2: test multi-stage combinations for additive protection")
    print("STEP 3: prove multi-year efficacy in endemic field trials")
    print("CONFIRM: protection holds across transmission seasons without")
    print("  yearly boosting, against field strains.")
    print("REFUTE: the parasite's evasion always wins - every design wanes")
    print("  on the same curve, and only perpetual boosting works.")
    print("OK: %s explored the waning curve" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_usme_pancreatic_early(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    print("SOLUTION EXPLORER: finding a whisper in a crowd")
    print("Approach: the screening math - why a rare cancer demands a")
    print("near-perfect test, and what 'near-perfect' means numerically.")
    print("This is an exploratory research direction, not medical advice.")
    # adjustable assumptions
    prevalence = 0.00013    # ~13 per 100,000 per year
    sensitivity = 0.85
    specificity = 0.99
    # positive predictive value via Bayes
    ppv = (sensitivity * prevalence) / (
        sensitivity * prevalence + (1 - specificity) * (1 - prevalence))
    print("assumptions: prevalence=%.5f sens=%.2f spec=%.2f" % (
        prevalence, sensitivity, specificity))
    print("positive predictive value: %.4f (%.2f%%)" % (ppv, ppv * 100))
    assert 0.0109 < ppv < 0.0111
    # what specificity is needed for PPV = 25%?
    target_ppv = 0.25
    # solve: spec = 1 - sens*prev*(1-ppv)/(ppv*(1-prev))
    spec_needed = 1 - sensitivity * prevalence * (1 - target_ppv) / (
        target_ppv * (1 - prevalence))
    print("specificity needed for 25%% PPV: %.5f" % spec_needed)
    assert 0.99966 < spec_needed < 0.99968
    print("STEP 1: find tumor-shed signals (methylation, DNA, proteins)")
    print("STEP 2: build panels reaching five-nines specificity")
    print("STEP 3: prove mortality reduction in prospective trials")
    print("CONFIRM: a blood test finds stage I cancers with PPV high")
    print("  enough for population screening, cutting mortality.")
    print("REFUTE: tiny tumors shed nothing detectable - the signal is")
    print("  below physics, and screening stays impossible.")
    print("OK: %s explored the screening math" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_usme_glioblastoma_bbb(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    print("SOLUTION EXPLORER: speaking the gatehouse password")
    print("Approach: quantify the delivery gap the barrier creates, then")
    print("model what temporary opening buys.")
    print("This is an exploratory research direction, not medical advice.")
    # adjustable assumptions
    dose = 100.0            # arbitrary dose units
    frac_crosses = 0.02     # 2% crosses the intact barrier
    delivered = dose * frac_crosses
    needed = 10.0           # therapeutic level at the tumor edge
    print("assumptions: dose=%.0f units, barrier passage=%.0f%%, need=%.0f" % (
        dose, frac_crosses * 100, needed))
    print("delivered to tumor edge: %.2f (need %.0f)" % (delivered, needed))
    assert 1.99 < delivered < 2.01
    # focused ultrasound opens the barrier 8x locally
    opened = 8.0
    delivered_open = dose * frac_crosses * opened
    print("delivered with temporary opening: %.1f" % delivered_open)
    assert 15.9 < delivered_open < 16.1
    margin = delivered_open / needed
    print("therapeutic margin: %.2fx" % margin)
    assert 1.59 < margin < 1.61
    print("STEP 1: prove opening is reversible and safe, repeatedly")
    print("STEP 2: deliver proven drugs through the opened window")
    print("STEP 3: extend survival with cognition preserved")
    print("CONFIRM: opened-barrier delivery extends survival with")
    print("  imaging proof the drug arrived at the infiltrating edge.")
    print("REFUTE: opening harms more than delivery helps - edema,")
    print("  bleeding, or tumor seeding through the breach.")
    print("OK: %s explored the gatehouse math" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_usme_alzheimer(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    print("SOLUTION EXPLORER: the failing city, whole-system view")
    print("Approach: model Alzheimer as combined failure - amyloid, tau,")
    print("microglia, vascular - and compute the multi-lever prize.")
    print("This is an exploratory research direction, not medical advice.")
    # adjustable assumptions: each lever slows decline by a fraction
    levers = {"anti-amyloid": 0.27, "anti-tau": 0.20,
              "microglia-calming": 0.15, "vascular": 0.12}
    # combined slowing if effects multiply (independent mechanisms)
    remaining = 1.0
    for name_l, frac in levers.items():
        remaining *= (1.0 - frac)
    combined = 1.0 - remaining
    print("assumptions: lever slowdowns=%s" % levers)
    print("single best lever: %.0f%% slowing" % (max(levers.values()) * 100))
    print("combined (independent) slowing: %.4f" % combined)
    assert 0.2699 < max(levers.values()) < 0.2701
    assert 0.56315 < combined < 0.56318
    gain = combined / max(levers.values())
    print("multi-lever gain over best single: %.2fx" % gain)
    assert 2.084 < gain < 2.087
    print("STEP 1: order the failures - which lever is upstream")
    print("STEP 2: test combinations, not monotherapies")
    print("STEP 3: intervene in preclinical carriers (APOE4) early")
    print("CONFIRM: combination therapy halts decline where single levers")
    print("  merely slow it, with biomarkers agreeing.")
    print("REFUTE: levers prove redundant or antagonistic - the city fails")
    print("  as one, and no combination beats the best single drug.")
    print("OK: %s explored the multi-lever math" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_usme_parkinson_halt(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    print("SOLUTION EXPLORER: stopping the dying, not masking it")
    print("Approach: model dopamine-neuron loss and size the prodromal")
    print("window where halting still matters.")
    print("This is an exploratory research direction, not medical advice.")
    # adjustable assumptions: exponential neuron loss, symptoms at 70% lost
    lost_at_diagnosis = 0.70
    years_prodromal = 8.0     # years of silent loss before diagnosis
    k = -math.log(1 - lost_at_diagnosis) / years_prodromal
    print("assumptions: %.0f%% lost at diagnosis after %.0f silent years" % (
        lost_at_diagnosis * 100, years_prodromal))
    print("loss rate: %.4f per year" % k)
    assert 0.1504 < k < 0.1506
    # intervene at year 4 of the silent phase: loss so far
    lost_at_4 = 1 - math.exp(-k * 4.0)
    print("loss if caught at silent year 4: %.4f" % lost_at_4)
    assert 0.45226 < lost_at_4 < 0.45229
    # a halting drug that cuts the rate 60%, started at year 4
    k2 = k * 0.40
    lost_at_12 = 1 - math.exp(-k * 4.0) * math.exp(-k2 * 8.0)
    print("loss at year 12 with halting drug from year 4: %.4f" % lost_at_12)
    assert 0.66160 < lost_at_12 < 0.66163
    print("  (vs %.2f without it - still above the symptom line, barely)" % (
        1 - math.exp(-k * 12.0)))
    print("STEP 1: detect prodromal Parkinson (smell loss, RBD, DAT scan)")
    print("STEP 2: test halting drugs in prodromal cohorts")
    print("STEP 3: prove slowed decline over years, not biomarker wiggles")
    print("CONFIRM: prodromal treatment delays or prevents the symptom")
    print("  threshold, with neuron-loss biomarkers agreeing.")
    print("REFUTE: loss proves unstoppable once seeded - every candidate")
    print("  fails the delayed-start test.")
    print("OK: %s explored the halting window" % NAME)
if __name__ == "__main__":
    main()
''')


DEMOS.update({
    "hiv_cure": demo_usme_hiv_cure,
    "drug_resistant_tb": demo_usme_drug_resistant_tb,
    "universal_flu_vaccine": demo_usme_universal_flu_vaccine,
    "malaria_durability": demo_usme_malaria_durability,
    "pancreatic_early": demo_usme_pancreatic_early,
    "glioblastoma_bbb": demo_usme_glioblastoma_bbb,
    "alzheimer": demo_usme_alzheimer,
    "parkinson_halt": demo_usme_parkinson_halt,
})


def demo_usme_als_cure(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    print("SOLUTION EXPLORER: unjamming the motor neuron")
    print("Approach: model misfolded-protein load vs clearance and ask what")
    print("tips the neuron from coping to collapse.")
    print("This is an exploratory research direction, not medical advice.")
    # adjustable assumptions: production vs clearance of toxic protein
    production = 1.00
    clearance = 0.92        # slightly behind production
    load = 0.0
    years = 3.0
    dt = 0.01
    steps_n = int(round(years / dt))
    for _ in range(steps_n):
        load += (production - clearance) * dt
    print("assumptions: production=%.2f clearance=%.2f over %.1f years" % (
        production, clearance, years))
    print("accumulated toxic load: %.4f" % load)
    assert 0.2399 < load < 0.2401
    # a therapy boosting clearance 15%
    clearance2 = clearance * 1.15
    load2 = 0.0
    for _ in range(steps_n):
        load2 += (production - clearance2) * dt
    print("load with 15%% clearance boost: %.4f" % load2)
    assert -0.1741 < load2 < -0.1739
    print("  (negative = net clearance: the jam reverses)")
    print("STEP 1: find the sporadic trigger - what starts the jam")
    print("STEP 2: explain motor-neuron selectivity - why these cells")
    print("STEP 3: test clearance-boosting in sporadic models and patients")
    print("CONFIRM: clearance therapies halt neurofilament rise and")
    print("  functional decline in sporadic ALS.")
    print("REFUTE: the jam is downstream - clearing protein changes")
    print("  nothing because the dying started elsewhere.")
    print("OK: %s explored the protein ledger" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_usme_metastasis(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    print("SOLUTION EXPLORER: intercepting the invasion dispatches")
    print("Approach: model metastasis as a chain of steps and compute the")
    print("value of breaking any single link.")
    print("This is an exploratory research direction, not medical advice.")
    # adjustable assumptions: per-step success probabilities
    steps = {"escape": 0.40, "survive circulation": 0.10,
             "exit vessel": 0.30, "colonize": 0.05, "awaken": 0.50}
    p_meta = 1.0
    for s, p in steps.items():
        p_meta *= p
    print("assumptions: step probabilities=%s" % steps)
    print("per-cell metastasis probability: %.6f" % p_meta)
    assert 0.000299 < p_meta < 0.000301
    # block the awakening step 90%
    steps2 = dict(steps)
    steps2["awaken"] = steps["awaken"] * 0.10
    p_meta2 = 1.0
    for p in steps2.values():
        p_meta2 *= p
    print("with awakening blocked 90%%: %.7f" % p_meta2)
    assert 0.0000299 < p_meta2 < 0.0000301
    cut = p_meta / p_meta2
    print("metastasis cut: %.1fx" % cut)
    assert 9.9 < cut < 10.1
    print("STEP 1: find the wake signal for dormant micrometastases")
    print("STEP 2: drug the pre-metastatic niche before seeds arrive")
    print("STEP 3: prove metastasis-free survival improves in trials")
    print("CONFIRM: dormancy-targeted therapy cuts distant recurrence")
    print("  without needing to kill every disseminated cell.")
    print("REFUTE: blocking one step reroutes the invasion - the chain")
    print("  has alternate paths science has not mapped.")
    print("OK: %s explored the invasion chain" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_usme_cancer_immune_evasion(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    print("SOLUTION EXPLORER: defeating a redundant deception")
    print("Approach: model evasion tricks as redundant layers and compute")
    print("why single-trick drugs select for the next trick.")
    print("This is an exploratory research direction, not medical advice.")
    # adjustable assumptions: 4 evasion layers, drug defeats one
    layers = 4
    p_layer_beats_drug = 0.70   # chance the tumor leans on another layer
    p_escape_single = p_layer_beats_drug
    # combination defeating all 4 (independent for the model)
    p_escape_combo = p_layer_beats_drug ** layers
    print("assumptions: evasion layers=%d, per-layer escape=%.2f" % (
        layers, p_layer_beats_drug))
    print("tumor escape vs single-trick drug: %.2f" % p_escape_single)
    print("tumor escape vs 4-layer combination: %.4f" % p_escape_combo)
    assert 0.699 < p_escape_single < 0.701
    assert 0.2400 < p_escape_combo < 0.2402
    control_single = 1 - p_escape_single
    control_combo = 1 - p_escape_combo
    print("disease control: single=%.2f combo=%.4f" % (control_single, control_combo))
    assert 0.299 < control_single < 0.301
    assert 0.7598 < control_combo < 0.7600
    print("STEP 1: profile each tumor's full evasion stack, cell by cell")
    print("STEP 2: match combinations to stacks, not single biomarkers")
    print("STEP 3: prove durable control in 'cold' tumors")
    print("CONFIRM: stack-matched combinations control cold tumors where")
    print("  single checkpoint drugs failed.")
    print("REFUTE: the stack is effectively infinite - every combination")
    print("  reveals another layer, without end.")
    print("OK: %s explored the deception stack" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_usme_spinal_cord(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    print("SOLUTION EXPLORER: splicing the cut wire")
    print("Approach: model axon regrowth as rate vs distance vs inhibition,")
    print("and compute what combined therapy must achieve.")
    print("This is an exploratory research direction, not medical advice.")
    # adjustable assumptions
    growth_rate = 1.0       # mm/day when uninhibited
    inhibition = 0.95       # scar inhibition fraction
    effective_rate = growth_rate * (1 - inhibition)
    lesion_mm = 10.0
    days_blocked = lesion_mm / effective_rate
    print("assumptions: growth=%.1f mm/day inhibition=%.0f%% lesion=%.0f mm" % (
        growth_rate, inhibition * 100, lesion_mm))
    print("effective regrowth: %.3f mm/day -> crossing takes %.0f days" % (
        effective_rate, days_blocked))
    assert 0.0499 < effective_rate < 0.0501
    assert 199.9 < days_blocked < 200.1
    # combined therapy: inhibition cut to 30%, growth program doubled
    inhibition2 = 0.30
    growth2 = 2.0
    effective2 = growth2 * (1 - inhibition2)
    days2 = lesion_mm / effective2
    print("combined therapy: %.2f mm/day -> crossing takes %.2f days" % (
        effective2, days2))
    assert 1.399 < effective2 < 1.401
    assert 7.13 < days2 < 7.15
    print("STEP 1: neutralize scar inhibitors without removing protection")
    print("STEP 2: switch on the neuron's intrinsic growth program")
    print("STEP 3: prove axons cross, synapse correctly, and restore function")
    print("CONFIRM: tract tracing shows axons crossing the lesion and")
    print("  voluntary function returning in humans.")
    print("REFUTE: regrown axons wander - growth without guidance is noise,")
    print("  and no guidance cue restores ordered connections.")
    print("OK: %s explored the splice math" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_usme_organ_regeneration(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    print("SOLUTION EXPLORER: waking the sleeping blueprint")
    print("Approach: model blastema regrowth as controlled cell divisions")
    print("and bound the cancer risk of reopening growth.")
    print("This is an exploratory research direction, not medical advice.")
    # adjustable assumptions: regrowing 1 cm^3 of tissue
    target_cells = 1e9
    start_cells = 1e4
    divisions = math.log2(target_cells / start_cells)
    print("assumptions: target=%g cells from %g blastema cells" % (
        target_cells, start_cells))
    print("divisions required: %.2f" % divisions)
    assert 16.60 < divisions < 16.62
    # at one division per day
    days = divisions / 1.0
    print("time at 1 division/day: %.1f days" % days)
    assert 16.60 < days < 16.62
    # cancer risk bound: per-division mutation escape probability
    p_escape = 1e-7
    p_any = 1 - (1 - p_escape) ** target_cells
    print("uncontrolled-escape probability without an off-switch: %.4f" % p_any)
    assert 0.9999 < p_any <= 1.0
    print("  -> the off-switch is not optional; it is the therapy")
    print("STEP 1: map the blastema program gene by gene")
    print("STEP 2: build the off-switch FIRST - growth with a brake")
    print("STEP 3: prove patterned, innervated regrowth in mammals")
    print("CONFIRM: mammalian digits/organs regrow patterned and functional")
    print("  with zero tumors on long follow-up.")
    print("REFUTE: mammalian cells cannot be coaxed into blastema - the")
    print("  program is locked beyond any safe key.")
    print("OK: %s explored the regrowth ledger" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_usme_transplant_tolerance(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    print("SOLUTION EXPLORER: drafting the organ's peace treaty")
    print("Approach: compare lifelong suppression vs tolerance induction as")
    print("expected healthy years - the treaty's value.")
    print("This is an exploratory research direction, not medical advice.")
    # adjustable assumptions
    years_graft = 15.0
    qaly_suppressed = 0.75    # quality weight on immunosuppression
    qaly_tolerant = 0.95
    p_tolerance_success = 0.55
    expected_suppressed = years_graft * qaly_suppressed
    expected_tolerance = (p_tolerance_success * years_graft * qaly_tolerant +
                          (1 - p_tolerance_success) * years_graft * qaly_suppressed)
    print("assumptions: graft years=%.0f, tolerance success=%.0f%%" % (
        years_graft, p_tolerance_success * 100))
    print("expected healthy years, suppression: %.3f" % expected_suppressed)
    print("expected healthy years, tolerance attempt: %.3f" % expected_tolerance)
    assert 11.249 < expected_suppressed < 11.251
    assert 12.899 < expected_tolerance < 12.901
    gain = expected_tolerance - expected_suppressed
    print("expected gain: %.3f healthy years" % gain)
    assert 1.649 < gain < 1.651
    print("STEP 1: copy pregnancy's regulatory playbook molecule by molecule")
    print("STEP 2: lighten chimerism conditioning to routine safety")
    print("STEP 3: prove durable drug-free graft survival at scale")
    print("CONFIRM: routine protocols yield drug-free tolerance with")
    print("  protocol biopsies clean for years.")
    print("REFUTE: tolerance always proves partial - drugs can be lowered")
    print("  but never stopped, in any scalable protocol.")
    print("OK: %s explored the treaty math" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_usme_anesthesia_mechanism(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    print("SOLUTION EXPLORER: tracing the off-switch current")
    print("Approach: model consciousness as integrated information flow and")
    print("compute what anesthetics do to the network's integration.")
    print("This is an exploratory research direction, not medical advice.")
    # adjustable assumptions: toy network integration measure
    n_regions = 8
    p_connected_awake = 0.85
    p_connected_asleep = 0.25
    # integration ~ connected pairs
    pairs = n_regions * (n_regions - 1) / 2.0
    integ_awake = pairs * p_connected_awake
    integ_asleep = pairs * p_connected_asleep
    print("assumptions: %d regions, connection p awake=%.2f asleep=%.2f" % (
        n_regions, p_connected_awake, p_connected_asleep))
    print("integration awake: %.2f, anesthetized: %.2f" % (integ_awake, integ_asleep))
    assert 23.79 < integ_awake < 23.81
    assert 6.99 < integ_asleep < 7.01
    drop = 1 - integ_asleep / integ_awake
    print("integration drop: %.4f" % drop)
    assert 0.7057 < drop < 0.7059
    # reversibility: connections restore
    print("connections restored on emergence: %.2f (reversibility = the phenomenon)" % integ_awake)
    print("STEP 1: record the awake->anesthetized transition at high resolution")
    print("STEP 2: test which network property predicts the loss of experience")
    print("STEP 3: build drugs that target components independently")
    print("CONFIRM: a network measure predicts loss and return of")
    print("  consciousness across drugs, sleep, and coma.")
    print("REFUTE: no network measure tracks experience - molecular")
    print("  effects never assemble into an explanation of the off-switch.")
    print("OK: %s explored the off-switch current" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_usme_aging_biology(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    print("SOLUTION EXPLORER: reading the smudged catalog")
    print("Approach: model aging as information loss vs damage, using the")
    print("reprogramming result as the discriminator.")
    print("This is an exploratory research direction, not medical advice.")
    # adjustable assumptions: two models of an age-related deficit
    deficit = 1.00
    # damage model: reprogramming cannot fix broken parts -> no rejuvenation
    # information model: resetting annotations restores function
    info_fraction = 0.60     # fraction of deficit that is information loss
    damage_fraction = 1.0 - info_fraction
    rejuvenation = deficit * info_fraction  # what reprogramming recovers
    residual = deficit * damage_fraction
    print("assumptions: information-loss fraction=%.2f" % info_fraction)
    print("deficit recovered by reprogramming: %.2f" % rejuvenation)
    print("residual (true damage): %.2f" % residual)
    assert 0.599 < rejuvenation < 0.601
    assert 0.399 < residual < 0.401
    # epigenetic clock: biological age reversal in the mouse experiments scale
    age_months = 24.0
    reversal_fraction = 0.30
    reversed_age = age_months * (1 - reversal_fraction)
    print("24-month-old mouse, 30%% clock reversal -> %.1f months" % reversed_age)
    assert 16.79 < reversed_age < 16.81
    print("STEP 1: separate information loss from damage, tissue by tissue")
    print("STEP 2: prove clock reversal predicts real function and lifespan")
    print("STEP 3: test partial reprogramming in humans with tumor watch")
    print("CONFIRM: clock reversal tracks with restored function and")
    print("  longer healthspan, without raised cancer rates.")
    print("REFUTE: reprogramming rejuvenates clocks but not bodies - the")
    print("  annotations were never the cause.")
    print("OK: %s explored the catalog math" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_usme_full_regeneration(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    print("SOLUTION EXPLORER: raising the cathedral again")
    print("Approach: the summit problem - combine every hard lesson (tolerance,")
    print("patterning, plumbing, growth control) and price the integration.")
    print("This is an exploratory research direction, not medical advice.")
    # adjustable assumptions: success requires ALL subsystems
    subsystems = {"patterning": 0.70, "vascularization": 0.65,
                  "innervation": 0.55, "immune acceptance": 0.60,
                  "growth control": 0.75}
    p_all = 1.0
    for s, p in subsystems.items():
        p_all *= p
    print("assumptions: subsystem readiness=%s" % subsystems)
    print("joint success probability: %.5f" % p_all)
    assert 0.11260 < p_all < 0.11263
    # improve the weakest link (innervation) to 0.80
    subsystems2 = dict(subsystems)
    subsystems2["innervation"] = 0.80
    p_all2 = 1.0
    for p in subsystems2.values():
        p_all2 *= p
    print("with innervation raised to 0.80: %.5f" % p_all2)
    assert 0.16379 < p_all2 < 0.16381
    weakest = min(subsystems, key=subsystems.get)
    print("weakest link today: %s" % weakest)
    assert weakest == "innervation"
    print("STEP 1: master each subsystem to reliability separately")
    print("STEP 2: integrate in small organs first (bladder, trachea)")
    print("STEP 3: scale to complex organs, then limbs")
    print("CONFIRM: a patient-derived complex organ functions for years -")
    print("  perfused, innervated, accepted, and size-stable.")
    print("REFUTE: integration proves multiplicative in the bad way - each")
    print("  added subsystem collapses the others, without limit.")
    print("OK: %s explored the summit math" % NAME)
if __name__ == "__main__":
    main()
''')


DEMOS.update({
    "als_cure": demo_usme_als_cure,
    "metastasis": demo_usme_metastasis,
    "cancer_immune_evasion": demo_usme_cancer_immune_evasion,
    "spinal_cord": demo_usme_spinal_cord,
    "organ_regeneration": demo_usme_organ_regeneration,
    "transplant_tolerance": demo_usme_transplant_tolerance,
    "anesthesia_mechanism": demo_usme_anesthesia_mechanism,
    "aging_biology": demo_usme_aging_biology,
    "full_regeneration": demo_usme_full_regeneration,
})
