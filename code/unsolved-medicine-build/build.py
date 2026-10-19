#!/usr/bin/env python3
"""Build the Unsolved Medicine Database pair (Manon's 16:15 orders,
Unsolved Problems Solved series, batch 1 - medicine).

The halves are two views of the SAME 34 famous unsolved medicine problems:
  unsolved-medicine              - The Unsolved Medicine Database
                                   (public-harvest: real, fact-checked
                                   problems - the cold, flu drift, placebo,
                                   allergy, chronic pain, migraine, sleep,
                                   obesity, vaccine durability, sepsis,
                                   long COVID, resistance, autoimmunity,
                                   diabetes, microbiome, depression,
                                   schizophrenia, HIV, TB, universal flu,
                                   malaria, pancreatic detection,
                                   glioblastoma, Alzheimer, Parkinson, ALS,
                                   metastasis, immune evasion, spinal cord,
                                   regeneration, transplant tolerance,
                                   anesthesia, aging, full regeneration)
  unsolved-medicine-signature    - The Unsolved Medicine Signature Database
                                   (same 34 problems through the Signature
                                   lens, titles suffixed " (Signature
                                   Edition)", src signature, full proposed-
                                   solution treatments; clearly labeled
                                   Signature-made)

ID prefixes: JAH-USME- (public) and JAH-USMES- (signature), verified free
2026-10-17 in manifest id_prefix values (zero hits) and in all 874 shard
data directories of jah-databases-data-1 (zero hits).

Every record: problem + background + why_it_matters + signature_solution.
signature_solution OPENS WITH THE EXACT LABEL "Signature-generated proposed
solution - not established science." Public half carries a short pointer;
signature half carries the full treatment. HONESTY RULE: never claim proof,
never imply peer acceptance, never present speculation as settled. Proposed
solutions are exploratory research directions - NEVER medical advice or
treatment claims. Nothing hate-adjacent, profane, or inappropriate; no
religious talk.

34 records each, ladder-ordered 1-34 (simple -> compounded -> complex);
the shard index is written in ladder order.

Dedupe: gate.check() on all 68 titles vs the whole system before authoring:
zero collisions, zero refusals.

68 demos machine-executed (solution-explorer walkthroughs with
confirm/refute panels), ALL OK: real computed values, tight-bounds asserts,
never float exact-equality; entry text cross-checked vs demo outputs.

NOTE (concurrency): this builder NEVER touches data/manifest.json,
api.json, index.html, README.md, or docs/AI_ACCESS.md, and never commits
or pushes. A merger handles registration and restamping.

Never the words "bat belt" anywhere. No website references. No Facebook.
"""
import importlib.util
import json
import os
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
from entries_unsolved_medicine import ENTRIES, SIG_TAIL, LABEL
from demos_unsolved_medicine import DEMOS

# ------------------------------------------------------------------ solutions
# Full Signature proposed-solution treatments (signature half). Each lays out
# assumptions, reasoning path, proposed mechanism, what would confirm or kill
# it, and what it does NOT claim. Exploratory research directions only.

SOLUTIONS = {
"common_cold": (
    "ASSUMPTIONS: (1) rhinovirus serotypes share conserved inner-shell "
    "machinery they cannot mutate away without breaking replication; (2) "
    "nasal mucosal immunity can be trained independently of blood immunity. "
    "REASONING PATH: serotype-chasing failed for 70 years, so invert the "
    "target - vaccinate against what the virus cannot change. PROPOSED "
    "MECHANISM: a nasal immunogen displaying conserved VP4/inner-VP1 "
    "epitopes plus a mucosal adjuvant, building resident airway IgA and "
    "tissue-resident memory T cells at the site of infection. CONFIRM: "
    "multi-serotype challenge protection in humans with nasal antibody "
    "correlates. KILL: conserved epitopes prove non-immunogenic in human "
    "noses, or protection fails against natural colds. DOES NOT CLAIM: a "
    "cure for colds, safety in children, or applicability to non-rhinovirus "
    "colds."
),
"flu_remade": (
    "ASSUMPTIONS: (1) the HA stem is conserved because it performs the "
    "membrane-fusion job no mutation can redesign cheaply; (2) "
    "immunodominance is a trainable habit, not a fixed law. REASONING PATH: "
    "stop forecasting the head; teach the immune system to ignore the head "
    "and study the stem via sequential chimeric-HA immunization. PROPOSED "
    "MECHANISM: prime-boost series where each dose keeps the stem constant "
    "but swaps the head, so only stem-directed memory is recalled and "
    "amplified. CONFIRM: multi-season human protection against drifted and "
    "shifted strains with stem-antibody correlates. KILL: responses always "
    "revert to head-dominance, or stem antibodies fail to prevent "
    "infection. DOES NOT CLAIM: an existing vaccine, pandemic readiness "
    "today, or protection against non-influenza viruses."
),
"placebo": (
    "ASSUMPTIONS: (1) placebo biology decomposes into separable "
    "neurochemical modules (opioid, cannabinoid, dopamine, expectancy "
    "circuits); (2) these modules can be engaged deliberately without "
    "deception. REASONING PATH: the naloxone experiment proved one module "
    "is real chemistry - map the rest the same way, then prescribe the "
    "context, not the lie. PROPOSED MECHANISM: open-label expectancy "
    "protocols - honest conditioning rituals paired with real drugs - that "
    "amplify endogenous systems and allow dose-sparing, measured against "
    "objective biomarkers. CONFIRM: expectancy protocols produce "
    "biomarker-verified effects and reduce required drug doses in "
    "randomized trials. KILL: effects collapse to reporting bias wherever "
    "objective measures are required. DOES NOT CLAIM: that belief cures "
    "disease, or that any condition should be treated with placebo alone."
),
"allergy_misfire": (
    "ASSUMPTIONS: (1) early-life immune calibration is a learnable "
    "classifier with a critical window; (2) misclassification is "
    "reversible because immunotherapy proves retraining works. REASONING "
    "PATH: find the training data the modern infant is missing, then "
    "supply it deliberately rather than by accident of lifestyle. PROPOSED "
    "MECHANISM: defined early-life microbial and dietary exposures that "
    "teach regulatory T cells the food-vs-foe boundary, validated by "
    "prospective tolerance outcomes. CONFIRM: intervention cohorts show "
    "durable, treatment-free tolerance with regulatory immune signatures. "
    "KILL: no exposure pattern predicts or prevents allergy prospectively. "
    "DOES NOT CLAIM: a proven prevention regimen, or that any family "
    "should change infant care on this basis."
),
"chronic_pain": (
    "ASSUMPTIONS: (1) chronic pain equals peripheral signal times a "
    "pathological central gain; (2) the gain has a measurable molecular "
    "identity, likely glial-driven. REASONING PATH: opioids fail because "
    "they scale the signal while the gain stays cranked - find the knob "
    "and turn it, instead of muffling the speaker. PROPOSED MECHANISM: "
    "quantitative sensory testing plus glial-activation biomarkers to stage "
    "the gain, then gain-targeted interventions (glial modulators, "
    "descending-control restoration) tested against gain normalization, "
    "not just pain scores. CONFIRM: a gain biomarker predicts chronicity "
    "and normalizes as function returns. KILL: no objective gain measure "
    "separates patients from controls. DOES NOT CLAIM: an available "
    "treatment, or that any patient's pain is imaginary."
),
"migraine": (
    "ASSUMPTIONS: (1) attacks are threshold crossings of a primed brain, "
    "not reactions to triggers; (2) priming has a measurable prodromal "
    "physiology. REASONING PATH: triggers are inconsistent because they "
    "are the last straw - find the straw pile (priming) and forecast the "
    "collapse. PROPOSED MECHANISM: hypothalamic/brainstem priming markers "
    "tracked longitudinally to build individual pre-attack predictors, then "
    "priming-lowering prevention timed to the forecast window. CONFIRM: "
    "priming biomarkers forecast attacks days ahead and timed prevention "
    "beats trigger avoidance. KILL: no pre-attack signal exists; attacks "
    "are random crossings. DOES NOT CLAIM: a known priming marker today, "
    "or advice to abandon current preventives."
),
"sleep_biology": (
    "ASSUMPTIONS: (1) each sleep stage performs at least one job that "
    "cannot be done awake; (2) the jobs are separable by selective "
    "stage deprivation. REASONING PATH: catalog functions is done - now "
    "run the subtraction experiments that prove necessity, stage by "
    "stage. PROPOSED MECHANISM: targeted stage-suppression studies mapping "
    "each stage to its non-substitutable function, converging on the "
    "minimal theory of why unconsciousness is required. CONFIRM: specific "
    "harms trace to specific lost stages with no waking substitute. KILL: "
    "every function proves replaceable awake. DOES NOT CLAIM: that less "
    "sleep is safe, or any method to reduce sleep need."
),
"obesity_setpoint": (
    "ASSUMPTIONS: (1) the defended weight is encoded in specific "
    "hypothalamic circuitry; (2) the encoding is plastic because the "
    "environment moved it upward within decades. REASONING PATH: drugs "
    "override the thermostat; find the thermostat's wiring and the signal "
    "that writes the setting. PROPOSED MECHANISM: map the set-point "
    "circuit, identify the developmental/environmental inputs that ratchet "
    "it, and test reset strategies with off-treatment weight defense as "
    "the endpoint. CONFIRM: weight stays off years after treatment ends "
    "with the defended weight measurably re-encoded. KILL: the setting "
    "proves indelible - every effect vanishes off treatment. DOES NOT "
    "CLAIM: a reset method today, or that willpower is the problem."
),
"vaccine_durability": (
    "ASSUMPTIONS: (1) germinal-center quality determines plasma-cell "
    "longevity; (2) the durable-vs-fading vaccine pair (measles vs "
    "pertussis) contains the contrast that reveals the rule. REASONING "
    "PATH: compare the two side by side until the early signature of "
    "lifelong memory appears, then engineer it deliberately. PROPOSED "
    "MECHANISM: adjuvants and schedules tuned to reproduce the durable "
    "germinal-center signature, validated by prospective multi-year "
    "protection. CONFIRM: an early signature predicts years of "
    "protection and engineered vaccines bearing it last. KILL: durability "
    "is unpredictable by any early measure. DOES NOT CLAIM: a universal "
    "durability formula today, or that boosters are unnecessary now."
),
"sepsis": (
    "ASSUMPTIONS: (1) sepsis is several opposite immune states, not one "
    "disease; (2) the state is readable from blood within hours. "
    "REASONING PATH: one-size trials failed because they averaged help "
    "for one state with harm for another - stratify first, then treat. "
    "PROPOSED MECHANISM: rapid transcriptomic/protein immune staging at "
    "the bedside, with state-matched immunomodulation (calm the storm or "
    "wake the paralyzed immune system, per the reading). CONFIRM: staged "
    "patients survive more than supportively-managed controls. KILL: "
    "states prove unmeasurable in time or matched therapy adds nothing. "
    "DOES NOT CLAIM: an available staging test or drug today."
),
"long_covid": (
    "ASSUMPTIONS: (1) post-viral illness is a mixture of distinct "
    "mechanisms under one umbrella; (2) each mechanism has a biomarker "
    "signature. REASONING PATH: stop running umbrella trials; split the "
    "mixture, match treatment to mechanism, and the 'failures' become "
    "successes in the right subgroup. PROPOSED MECHANISM: deep "
    "phenotyping (immune, clotting, autonomic, exercise physiology) to "
    "assign each patient a mechanism, then subgroup-matched trials. "
    "CONFIRM: matched treatments restore function where umbrella trials "
    "showed nothing. KILL: no stable subgroups exist. DOES NOT CLAIM: a "
    "known cure, or that any specific therapy works."
),
"antibiotic_resistance": (
    "ASSUMPTIONS: (1) resistance is selection pressure made visible; (2) "
    "strategies that disarm without killing impose far less pressure. "
    "REASONING PATH: the kill-everything paradigm breeds what it fights - "
    "shift the unit of selection by removing the kill incentive. PROPOSED "
    "MECHANISM: anti-virulence drugs, engineered phages, and resistance-"
    "gene-targeting constructs deployed with minute-scale diagnostics and "
    "availability-based economics. CONFIRM: low-pressure strategies show "
    "flat resistance curves over years. KILL: bacteria evolve around "
    "disarming as fast as killing. DOES NOT CLAIM: an available "
    "replacement for antibiotics today."
),
"autoimmune_triggers": (
    "ASSUMPTIONS: (1) most autoimmune disease begins with a specific "
    "tolerance break, often infection-shaped; (2) the break leaves a "
    "detectable preclinical signature. REASONING PATH: the EBV-MS link is "
    "the strongest lead the field has ever had - generalize the "
    "trigger-hunt it exemplifies. PROPOSED MECHANISM: prospective "
    "trigger-mapping cohorts plus antigen-specific tolerance therapies "
    "that retrain against the culprit self-protein without global "
    "suppression. CONFIRM: trigger removal/prevention cuts disease "
    "incidence; tolerance therapy yields drug-free remission. KILL: "
    "triggers prove untraceable and tolerance unteachable. DOES NOT "
    "CLAIM: a known prevention for any autoimmune disease today."
),
"t1d_prevention": (
    "ASSUMPTIONS: (1) the autoimmune attack has a years-long visible "
    "preclinical phase; (2) tolerance can be taught because the immune "
    "system learned it once. REASONING PATH: screening opened a window "
    "that never existed - use it for tolerance induction, not just delay. "
    "PROPOSED MECHANISM: antibody-stage screening of at-risk children, "
    "then antigen-specific tolerance therapy (beta-cell antigens plus "
    "regulatory-T support) with permanent drug-free non-progression as "
    "the bar. CONFIRM: treated children never progress, beta-cell "
    "function preserved years off therapy. KILL: the attack always "
    "resumes; delay is the ceiling. DOES NOT CLAIM: an available "
    "prevention, or that families should seek unproven therapy."
),
"microbiome_map": (
    "ASSUMPTIONS: (1) microbial effects on disease are real but strain- "
    "specific and metabolite-mediated; (2) causation requires "
    "interventional proof. REASONING PATH: climb from census to function "
    "to causation - measure what microbes DO (metabolites), then change "
    "it deliberately. PROPOSED MECHANISM: strain-level functional mapping "
    "followed by defined-consortium interventions in randomized human "
    "trials, with durable ecosystem remodeling as the bar. CONFIRM: "
    "defined microbial changes produce defined disease changes in "
    "humans. KILL: every association dissolves under intervention. DOES "
    "NOT CLAIM: that any probiotic treats disease, or a usable map today."
),
"depression_biology": (
    "ASSUMPTIONS: (1) depression is several diseases sharing a final "
    "pathway; (2) subtypes have predictive biomarkers. REASONING PATH: "
    "the SSRI era proved one-size treatment leaves a third behind - match "
    "mechanism to patient the way oncology matches drug to tumor. "
    "PROPOSED MECHANISM: biomarker-defined subtypes (inflammatory, "
    "plasticity-loss, circadian) with one mechanism-matched therapy each, "
    "validated by prospective prediction of response. CONFIRM: matched "
    "patients respond at far higher rates and the resistant third "
    "shrinks. KILL: subtypes prove unstable and matching adds nothing. "
    "DOES NOT CLAIM: validated subtypes today, or that anyone should stop "
    "current treatment."
),
"schizophrenia": (
    "ASSUMPTIONS: (1) excessive adolescent synaptic pruning is causal, not "
    "correlated; (2) pruning is measurable before onset in high-risk "
    "youth. REASONING PATH: the C4 discovery gave the first gene-to-brain "
    "bridge - test whether normalizing pruning prevents psychosis. "
    "PROPOSED MECHANISM: longitudinal pruning imaging in high-risk "
    "cohorts, then complement-pathway modulation timed to the adolescent "
    "pruning window, with conversion-to-psychosis as the endpoint. "
    "CONFIRM: excessive pruning precedes onset and normalizing it prevents "
    "psychosis. KILL: pruning is normal in future patients. DOES NOT "
    "CLAIM: a preventive treatment today, or that pruning explains all "
    "cases."
),
"hiv_cure": (
    "ASSUMPTIONS: (1) the intact latent reservoir is finite and "
    "measurable; (2) clearance can be multiplied without reseeding. "
    "REASONING PATH: natural decay would take a lifetime - so multiply "
    "clearance (shock-and-kill) or make dormancy permanent (block-and-"
    "lock), and measure the intact reservoir, not defective fossils. "
    "PROPOSED MECHANISM: latency reversal paired with engineered immune "
    "clearance, or permanent epigenetic silencing, proven by years of "
    "drug-free remission with tissue-level reservoir assays. CONFIRM: "
    "reservoir shrinks toward zero and remission holds years off drugs. "
    "KILL: the reservoir proves unshrinkable in every tissue including "
    "the brain. DOES NOT CLAIM: a cure today, or that anyone should stop "
    "antiretrovirals."
),
"drug_resistant_tb": (
    "ASSUMPTIONS: (1) treatment length is the resistance engine - "
    "incomplete long courses select survivors; (2) dormant bacteria are "
    "druggable if targeted directly. REASONING PATH: shrink the course by "
    "killing what current drugs miss (the dormant), and the resistance "
    "treadmill slows. PROPOSED MECHANISM: dormancy-targeted drug "
    "combinations plus host-directed granuloma therapy, aiming at "
    "sterilizing courses of weeks, deployed in resistance-proof "
    "combinations from day one. CONFIRM: short courses sterilize with "
    "low relapse and flattening resistance curves. KILL: dormancy proves "
    "undruggable. DOES NOT CLAIM: a short cure today."
),
"universal_flu_vaccine": (
    "ASSUMPTIONS: (1) immunodominance is retrainable; (2) stem antibodies "
    "can prevent human infection, not just bind in a dish. REASONING "
    "PATH: sequential chimeric-HA immunization keeps the stem constant "
    "while swapping the head, forcing memory to the conserved target. "
    "PROPOSED MECHANISM: prime-boost series with stem-constant, head-"
    "swapped immunogens (protein, nanoparticle, or mRNA), validated by "
    "multi-season mismatched-strain protection in humans. CONFIRM: "
    "refocused vaccinees resist drifted and shifted strains for years. "
    "KILL: responses always revert to head-dominance. DOES NOT CLAIM: an "
    "available universal vaccine."
),
"malaria_durability": (
    "ASSUMPTIONS: (1) natural immunity's slowness is a clue, not just a "
    "fact - the parasite teaches badly, and vaccinology must teach "
    "better; (2) multi-stage targeting adds protection. REASONING PATH: "
    "copy what years of natural exposure eventually learn, and deliver "
    "it in a schedule. PROPOSED MECHANISM: multi-stage vaccines "
    "(sporozoite plus blood-stage) with durability-engineered adjuvants, "
    "or long-acting monoclonal antibodies, proven by multi-year field "
    "efficacy. CONFIRM: protection holds across transmission seasons "
    "without yearly boosting. KILL: every design wanes on the same curve. "
    "DOES NOT CLAIM: a durable vaccine today."
),
"pancreatic_early": (
    "ASSUMPTIONS: (1) even tiny pancreatic tumors shed detectable "
    "molecules (methylated DNA, proteins, exosomes); (2) five-nines "
    "specificity is achievable with multi-marker panels. REASONING PATH: "
    "the math demands near-perfect specificity for a rare cancer - so "
    "build the panel that reaches it, then prove mortality falls. "
    "PROPOSED MECHANISM: blood-based multi-analyte panels (methylation "
    "plus protein) validated prospectively, with AI-enriched high-risk "
    "targeting to raise pre-test probability. CONFIRM: stage I detection "
    "with screening-grade PPV and reduced mortality in trials. KILL: tiny "
    "tumors shed nothing detectable. DOES NOT CLAIM: an available "
    "screening test."
),
"glioblastoma_bbb": (
    "ASSUMPTIONS: (1) the barrier can be opened reversibly and repeatedly "
    "without harm; (2) the infiltrating edge, not the core, is the "
    "therapeutic target. REASONING PATH: focused ultrasound proved the "
    "wall can be cracked - now deliver proven drugs through the crack on "
    "a schedule, and pair delivery with immune activation. PROPOSED "
    "MECHANISM: image-guided barrier opening synchronized with "
    "chemotherapy/antibody dosing, plus microenvironment-reprogramming "
    "agents, with overall survival and cognition as endpoints. CONFIRM: "
    "extended survival with drug-arrival imaging proof. KILL: opening "
    "harms more than delivery helps. DOES NOT CLAIM: an available therapy."
),
"alzheimer": (
    "ASSUMPTIONS: (1) Alzheimer is multi-factorial - amyloid, tau, "
    "microglia, vascular, metabolic; (2) the factors interact, so "
    "combinations beat monotherapies. REASONING PATH: the single-cause "
    "era failed expensively - order the failures causally and attack "
    "them together, early, in preclinical carriers. PROPOSED MECHANISM: "
    "combination prevention trials in APOE4 carriers (amyloid clearance "
    "plus tau plus microglial modulation plus vascular care) with "
    "clinical-decline endpoints. CONFIRM: combinations halt decline "
    "where single levers merely slow it. KILL: levers prove redundant or "
    "antagonistic. DOES NOT CLAIM: a cure or a recommended prevention "
    "regimen today."
),
"parkinson_halt": (
    "ASSUMPTIONS: (1) alpha-synuclein spread drives progression; (2) a "
    "prodromal window exists where most neurons still live. REASONING "
    "PATH: by tremor onset the battle is mostly lost - detect the silent "
    "phase (smell loss, RBD, DAT imaging) and intervene there. PROPOSED "
    "MECHANISM: prodromal cohorts treated with spread-blocking "
    "(anti-synuclein) plus resilience-boosting (lysosomal/mitochondrial) "
    "therapy, proven by delayed-start designs showing true slowing. "
    "CONFIRM: prodromal treatment delays or prevents the symptom "
    "threshold. KILL: loss proves unstoppable once seeded. DOES NOT "
    "CLAIM: a halting therapy today."
),
"als_cure": (
    "ASSUMPTIONS: (1) sporadic ALS shares the protein-homeostasis failure "
    "seen in genetic forms; (2) motor-neuron selectivity has a discoverable "
    "reason (length, workload, transport). REASONING PATH: tofersen proved "
    "the genetic slice is druggable - generalize from protein load vs "
    "clearance to the sporadic majority. PROPOSED MECHANISM: clearance-"
    "boosting and transport-restoring therapies guided by neurofilament "
    "monitoring, enrolled early, with functional halt as the bar. "
    "CONFIRM: clearance therapies halt neurofilament rise and functional "
    "decline in sporadic ALS. KILL: the jam is downstream of the true "
    "cause. DOES NOT CLAIM: a treatment for sporadic ALS today."
),
"metastasis": (
    "ASSUMPTIONS: (1) metastasis is a chain of druggable steps; (2) "
    "dormancy has a wake signal that can be found. REASONING PATH: no "
    "drug prevents spread because all drugs target growing cells - target "
    "the sleeping ones and the dispatches instead. PROPOSED MECHANISM: "
    "dormancy-locking or wake-and-kill strategies plus pre-metastatic-"
    "niche disruption, proven by metastasis-free survival in trials. "
    "CONFIRM: dormancy-targeted therapy cuts distant recurrence. KILL: "
    "the chain has unmappable alternate paths. DOES NOT CLAIM: an "
    "available anti-metastatic drug."
),
"cancer_immune_evasion": (
    "ASSUMPTIONS: (1) evasion is layered and redundant but finite; (2) "
    "each tumor's evasion stack is profileable. REASONING PATH: single-"
    "trick drugs select for the next trick - match the full stack with a "
    "combination, the way infections are treated. PROPOSED MECHANISM: "
    "single-cell tumor-immune profiling to read each patient's stack, "
    "then stack-matched combinations (checkpoint plus microenvironment "
    "plus engineered cells), proven in immunologically cold tumors. "
    "CONFIRM: stack-matched combinations control cold tumors. KILL: the "
    "stack is effectively infinite. DOES NOT CLAIM: an available "
    "combination today."
),
"spinal_cord": (
    "ASSUMPTIONS: (1) the regrowth blockade is reversible - rat studies "
    "prove the principle; (2) growth without guidance is noise, so "
    "guidance cues must be supplied. REASONING PATH: combine all three - "
    "silence the scar's stop signals, switch on the neuron's growth "
    "program, bridge with cells or scaffolds - plus stimulation to wake "
    "surviving circuits. PROPOSED MECHANISM: triple therapy (scar "
    "neutralization plus intrinsic growth activation plus bridging) with "
    "tract-tracing proof of correct reconnection and voluntary function "
    "as the bar. CONFIRM: human axons cross the lesion and function "
    "returns. KILL: regrown axons cannot be guided to correct targets. "
    "DOES NOT CLAIM: an available reconnection therapy."
),
"organ_regeneration": (
    "ASSUMPTIONS: (1) the blastema program sleeps in the mammalian "
    "genome; (2) growth can be switched off as reliably as on. "
    "REASONING PATH: the off-switch is the therapy - uncontrolled growth "
    "is cancer, so build the brake before the accelerator. PROPOSED "
    "MECHANISM: transient reprogramming plus Hippo/YAP modulation with a "
    "built-in growth-arrest switch, immune modulation toward blastema "
    "rather than scar, proven by patterned functional regrowth with "
    "long-term tumor surveillance. CONFIRM: patterned, innervated "
    "mammalian regrowth with zero tumors. KILL: the program is locked "
    "beyond any safe key. DOES NOT CLAIM: a regrown organ today."
),
"transplant_tolerance": (
    "ASSUMPTIONS: (1) pregnancy proves durable tolerance of half-foreign "
    "tissue is biologically possible; (2) mixed chimerism's harshness "
    "can be lightened. REASONING PATH: copy the mother's regulatory "
    "playbook instead of suppressing the whole army. PROPOSED MECHANISM: "
    "light-conditioning chimerism plus regulatory T cell therapy, with "
    "donor-specific unresponsiveness and intact third-party immunity as "
    "proof, scaled to routine safety. CONFIRM: routine drug-free graft "
    "survival for years. KILL: tolerance always proves partial. DOES NOT "
    "CLAIM: a routine protocol today, or that anyone should stop "
    "immunosuppression."
),
"anesthesia_mechanism": (
    "ASSUMPTIONS: (1) consciousness corresponds to a measurable network "
    "property (integration of information flow); (2) anesthetics disrupt "
    "that property specifically. REASONING PATH: compare awake, dreaming, "
    "anesthetized, and comatose brains at high resolution until the "
    "property that vanishes with experience is found. PROPOSED MECHANISM: "
    "pre-registered tests of competing network theories against the "
    "anesthesia transition, converging on component-specific drugs "
    "(unconsciousness, amnesia, immobility independently). CONFIRM: a "
    "network measure predicts loss and return of consciousness across "
    "drugs, sleep, and coma. KILL: no network measure tracks experience. "
    "DOES NOT CLAIM: a solved theory of consciousness."
),
"aging_biology": (
    "ASSUMPTIONS: (1) a substantial fraction of aging is information loss "
    "(epigenetic disorganization), not just damage; (2) clocks that "
    "measure it can serve as trial endpoints once validated. REASONING "
    "PATH: the reprogramming result discriminates the theories - use it "
    "to separate reversible information loss from true damage, tissue by "
    "tissue. PROPOSED MECHANISM: partial reprogramming and senolytics "
    "tested against validated clock-plus-function endpoints, with "
    "cancer surveillance as a co-primary, aiming at healthspan. CONFIRM: "
    "clock reversal tracks with restored function and longer healthspan "
    "without raised cancer rates. KILL: reprogramming rejuvenates clocks "
    "but not bodies. DOES NOT CLAIM: a proven human anti-aging therapy."
),
"full_regeneration": (
    "ASSUMPTIONS: (1) every subsystem (patterning, vessels, nerves, "
    "tolerance, growth control) is independently solvable; (2) the joint "
    "probability is the product - so the weakest link dominates. "
    "REASONING PATH: attack the weakest link first (innervation and "
    "vascularization), integrate in small organs, then scale. PROPOSED "
    "MECHANISM: staged integration - scaffold reseeding plus bioprinted "
    "vasculature plus tolerance induction plus growth-arrest switches - "
    "proven by a patient-derived complex organ functioning for years. "
    "CONFIRM: perfused, innervated, accepted, size-stable organs in "
    "patients. KILL: integration collapses multiplicatively without "
    "limit. DOES NOT CLAIM: a whole engineered organ today."
),
}

POINTER = (" The full Signature proposed-solution treatment for this problem "
           "is laid out step by step in the companion Signature half of this "
           "database (same problem, \"Signature Edition\" title): assumptions, "
           "reasoning path, proposed mechanism, what evidence would confirm "
           "or kill it, and what it does not claim. It is an exploratory "
           "research direction - never medical advice, never established "
           "science.")

# ---------------------------------------------------------------- DB config

def _cfg(slug, name, tagline, record_kind, prefix, ai, role, citation, source):
    sig_line = ("Signature originals - the same 34 famous unsolved medicine "
                "problems read through the Signature lens, each carrying the "
                "full Signature proposed-solution treatment: assumptions, "
                "reasoning path, proposed mechanism, confirm-or-kill "
                "evidence, and honest limits. Clearly labeled "
                "Signature-made, never presented as established science, "
                "never medical advice.")
    pub_line = ("Public records - 34 real, fact-checked unsolved medicine "
                "problems: the problem as the world knows it, its history "
                "and current state, why solving it matters, and a pointer "
                "to the Signature proposed-solution treatment in the "
                "companion Signature half. Organized in the Signature "
                "system.")
    ladder = (" Records are ordered by the teaching ladder, simple to "
              "compounded to complex: Foundations (the common cold, yearly "
              "flu vaccines, the placebo effect, allergy, chronic pain, "
              "migraine, sleep, obesity, vaccine durability, sepsis, long "
              "COVID, antibiotic resistance) -> Compounded (autoimmune "
              "triggers, type 1 diabetes, the microbiome map, depression, "
              "schizophrenia, HIV cure, drug-resistant TB, universal flu "
              "vaccine, malaria durability, pancreatic early detection, "
              "glioblastoma) -> Advanced (Alzheimer, Parkinson, ALS, "
              "metastasis, immune evasion, spinal cord repair, organ "
              "regeneration, transplant tolerance, anesthesia mechanism, "
              "the biology of aging, full regeneration).")
    return {
        "name": name, "tagline": tagline, "record_kind": record_kind,
        "prefix": prefix, "ai": ai, "role": role,
        "hero_p": "%s - %s Every record carries the full entry: the problem, its background, why it matters, key points, what a solution must satisfy, standards, citations, a Signature-lens reading, the proposed-solution treatment, and a working solution-explorer demonstration program.%s" % (tagline, sig_line if source == "signature" else pub_line, ladder),
        "sig_type": ("Signature originals organized in the Signature system"
                     if source == "signature" else
                     "Public records organized in the Signature system"),
        "search_ph": "Search Alzheimer, cancer, vaccines, antibiotics, pain, sleep, immunity, diabetes, depression, aging, regeneration, anesthesia...",
        "chat_ph": "Ask about unsolved medicine...",
        "archive_blurb": ("Seeded %s unsolved-medicine problem records, marching toward one million records. "
                          "Presented in teaching-ladder order: foundations, compounded, advanced."
                          % ("Signature-original" if source == "signature" else "public-record")),
        "schema": ("id, t, g, name, title, description, how_it_works, key_points, requirements, "
                   "standards, citations, solution, src, ladder_rank, ladder_tier, demo"),
        "fields": "Foundations \u00b7 Compounded \u00b7 Advanced - each tier opens on demand and loads only what you open",
        "gen_desc": "Generate clearly-labeled unsolved-medicine studies. Seeded archive records are the authoritative entries.",
        "greet": "I am the %s. Ask me about the great unsolved problems of medicine - from the common cold, flu vaccines, placebo, allergy, chronic pain, migraine, sleep, obesity, vaccine durability, sepsis, long COVID, and antibiotic resistance, through autoimmune triggers, diabetes, the microbiome, depression, schizophrenia, HIV, tuberculosis, universal vaccines, malaria, early cancer detection, and glioblastoma, to Alzheimer, Parkinson, ALS, metastasis, immune evasion, spinal cord repair, regeneration, transplant tolerance, anesthesia, aging, and full organ regrowth. I answer honestly: the problems are open, and the Signature approaches are proposed paths, labeled as such." % ai,
        "gen_fields": ["Foundations", "Compounded", "Advanced"],
        "gen_kind": "unsolved-medicine-study", "gen_demo_kind": "unsolved-medicine-demo",
        "source": source,
    }

CIT_PUB = ("Unsolved problems of medicine (standard references: Harrison's "
           "Principles of Internal Medicine; Robbins and Cotran Pathologic "
           "Basis of Disease; Janeway's Immunobiology; Guyton and Hall "
           "Textbook of Medical Physiology; Kandel et al. Principles of "
           "Neural Science; New England Journal of Medicine; Nature; The "
           "Lancet; World Health Organization fact sheets; Centers for "
           "Disease Control and Prevention surveillance reports; National "
           "Institutes of Health research programs; Alzheimer's Association "
           "Facts and Figures). Problem statements are fact-checked "
           "against these sources; proposed solutions are Signature work.")
CIT_SIG = CIT_PUB + (" Signature editions are his original Signature Lens "
                     "readings with Signature-generated proposed solutions - "
                     "exploratory research directions, never medical advice, "
                     "never established science, clearly labeled "
                     "Signature-made.")

DBCFG = {}
DBCFG["unsolved-medicine"] = _cfg(
    "unsolved-medicine", "The Unsolved Medicine Database",
    "Thirty-four of the most famous unsolved problems in medicine - real, "
    "fact-checked, and honestly open: from the common cold and the placebo "
    "effect through cancer, Alzheimer, and antibiotic resistance to aging "
    "itself - each with its history, its current state, why solving it "
    "matters, and a pointer to the Signature proposed-solution treatment.",
    "unsolved problem record", "JAH-USME-", "JAH Unsolved Medicine Archivist",
    "unsolved medicine archivist - the great open problems of medicine, "
    "taught progressively along the ladder from foundations through "
    "compounded to advanced; answers honestly from many angles - "
    "definition, example, analogy, application, history, math - using only "
    "archive data from this system; never presents proposed solutions as "
    "established science or medical advice",
    CIT_PUB, "public")
DBCFG["unsolved-medicine-signature"] = _cfg(
    "unsolved-medicine-signature", "The Unsolved Medicine Signature Database",
    "The same 34 famous unsolved medicine problems through the Signature "
    "lens: each problem reframed as Signature science and each carrying "
    "the full Signature proposed-solution treatment - assumptions, "
    "reasoning path, proposed mechanism, confirm-or-kill evidence, and "
    "honest limits. Clearly labeled Signature-made, never established "
    "science, never medical advice.",
    "unsolved problem record", "JAH-USMES-", "JAH Unsolved Medicine Archivist (Signature)",
    "unsolved medicine archivist - Signature editions: the same 34 open "
    "problems read through the Signature lens with full proposed-solution "
    "treatments, clearly labeled Signature-made and never presented as "
    "established science or medical advice; teaches progressively along "
    "the ladder from foundations through compounded to advanced; answers "
    "from many angles - definition, example, analogy, application, "
    "history, math - using only archive data from this system",
    CIT_SIG, "signature")

base.DBCFG = DBCFG

assert set(DEMOS) == {e["key"] for e in ENTRIES}, "demo map misses entries"
assert set(SOLUTIONS) == {e["key"] for e in ENTRIES}, "solution map misses entries"


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
            solution = LABEL + " " + SOLUTIONS[e["key"]]
        else:
            description = e["description"]
            how = e["how_it_works"]
            citations = list(e["citations"])
            solution = LABEL + POINTER
        rec = {
            "id": rid, "t": title, "g": e["group"], "name": name, "title": title,
            "description": description,
            "how_it_works": how,
            "key_points": list(e["key_points"]),
            "requirements": list(e["requirements"]),
            "standards": list(e["standards"]),
            "citations": citations,
            "solution": solution,
            "src": "signature" if sig else "public-harvest",
            "ladder_rank": e["ladder_rank"],
            "ladder_tier": e["ladder_tier"],
        }
        demo_fn = DEMOS[e["key"]]
        program = demo_fn(base._hdr, name if not sig else title, rid, e["group"],
                          e["key_points"], "; ".join(e["requirements"]))
        rec["demo"] = {"kind": "python", "language": "python",
                       "program": program,
                       "note": "Solution-explorer walkthrough: working demonstration program (real, runnable Python) with confirm/refute panels."}
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
    for slug in ("unsolved-medicine", "unsolved-medicine-signature"):
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
                      "solution", "src", "ladder_rank", "ladder_tier", "demo"):
                assert k in r, "missing %s in %s" % (k, r["id"])
            prog = r["demo"].get("program")
            assert prog and len(r["description"]) > 200, "stub in %s" % r["id"]
            assert 1 <= r["ladder_rank"] <= 34, "ladder_rank out of range in %s" % r["id"]
            assert r["ladder_tier"] in ("foundations", "compounded", "advanced"), \
                "bad ladder_tier in %s" % r["id"]
            assert r["solution"].startswith(LABEL), "solution label missing in %s" % r["id"]
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
        assert "universal build" not in page.lower(), "field leftover in %s" % slug
        assert "universal-build" not in page, "slug leftover in %s" % slug
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
        assert "universal build" not in gen_js.lower(), "field leftover in gen js %s" % slug
        with open(os.path.join(ddir, "gen-%s.js" % slug), "w", encoding="utf-8") as f:
            f.write(gen_js)
        print("page:  db/%s/index.html + gen-%s.js [%s]" % (slug, slug, ", ".join(notes)), flush=True)

    # NOTE: manifest.json / api.json / index.html / README / docs are owned by
    # the merger. This builder registers nothing and commits nothing.
    print("manifest + api.json: SKIPPED (merger-owned).")
    print("NEXT: merger verifies, registers, restamps, commits.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
