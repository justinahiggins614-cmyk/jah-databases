#!/usr/bin/env python3
"""Entries for The Unsolved Psychiatry Database (unsolved-psychiatry) and its
Signature half (unsolved-psychiatry-signature).

34 famous unsolved problems in psychiatry, ladder-ordered by accessibility
(rank 1 = most approachable, rank 34 = most complex/compounded).
Public half: real, fact-checked problems. Signature half: the same 34
problems through the Signature lens, with Signature-generated proposed
solutions that are ALWAYS labeled as proposals, never established science.

Honesty rule (enforced in every record): never claim proof, never imply
peer acceptance, never present speculation as settled. Signature proposals
are labeled speculation for research discussion only - never medical advice,
never a treatment recommendation, no dosages, no cure claims. Nothing here
encourages self-harm; crisis resources belong with real providers, not records.
"""

LABEL = "Signature-generated proposed solution \u2014 not established science."

SIG_TAIL = ("Signature editions carry the Signature system's proposed "
            "solution approaches to famous unsolved problems. Every "
            "solution is labeled a Signature-generated proposal, never "
            "established science, never peer-accepted, never proof, never "
            "medical advice.")

STD_COMMON = [
    "Problem statements verified against the published psychiatric literature; open status confirmed as of 2026.",
    "Signature solution sections are labeled proposals: they state assumptions, a reasoning path, a proposed mechanism, what would confirm or kill them, and what they do not claim.",
    "Signature proposals are labeled speculation for research discussion only - never medical advice, never a treatment recommendation; no dosages and no cure claims appear.",
]

ENTRIES = [
# ------------------------------------------------------------------ rank 1
{
 "key": "no-biomarker",
 "name": "No Objective Test: The Biomarker Gap",
 "group": "Diagnostics",
 "ladder_rank": 1, "ladder_tier": "foundations",
 "problem": "There is no blood test, brain scan, or lab marker for any major psychiatric disorder - why is diagnosis still entirely clinical?",
 "description": "Every major psychiatric diagnosis - schizophrenia, bipolar disorder, major depression - is made by clinical interview and symptom checklists. No biomarker (blood, genetic, imaging) has the sensitivity and specificity for clinical diagnosis, despite decades of searching. This is unique among major medical specialties and a root cause of psychiatry's other unsolved problems.",
 "background": "The DSM-III (1980) made diagnoses reliable (clinicians agree) but not valid (matching biology). The NIMH's RDoC (2010) tried to rebuild from circuits and genes. Thousands of biomarker studies followed - inflammatory markers, BDNF, imaging signatures, polygenic scores - but none crossed into clinical use. As of 2026, diagnosis remains symptom-based, and every treatment trial enrolls biologically heterogeneous patients.",
 "why_it_matters": "Without biomarkers, psychiatry cannot do precision medicine: trials fail on heterogeneous patients, and treatment remains trial-and-error. A real biomarker would reorganize the entire field.",
 "sig_pointer": "The Signature system's proposed approach treats the biomarker gap as a heterogeneity problem, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that biomarker searches fail because DSM categories are biologically heterogeneous: the signal is real but diluted across different biologies wearing one label. "
  "Assumptions: (1) real biologic subtypes exist within diagnoses; (2) current categories mix them; (3) markers will appear once patients are re-sorted. "
  "Reasoning path: a heterogeneity model explains why findings replicate poorly - each study samples a different subtype mix - and predicts that subtyping first will reveal markers. "
  "Proposed mechanism: 'subtype-first' biomarker discovery - stratifying patients by trajectory and treatment response before searching for markers. "
  "What would confirm it: markers discovered in stratified cohorts validating in new samples. "
  "What would kill it: evidence that psychiatric disorders have no stable biologic subtypes, only dimensions. "
  "What this does not claim: it does not claim a biomarker exists, offers no diagnostic advice, and does not constitute medical advice."),
 "sig_lens": "The Signature lens reads the missing biomarker as hidden by mixed biology, and asks what subtyping would reveal.",
 "how_it_works": "Researchers study the biomarker gap through large cohort studies, machine-learning on multimodal data, and RDoC-framework investigations.",
 "key_points": [
  "No biomarker exists for any major psychiatric diagnosis.",
  "DSM-III made diagnoses reliable but not biologically valid.",
  "NIMH's RDoC (2010) attempted a biology-based rebuild.",
  "Thousands of candidate markers failed to reach clinical use.",
  "Heterogeneity within diagnoses dilutes every signal.",
 ],
 "requirements": [
  "Biologically grounded patient subtyping.",
  "Markers validated in independent cohorts.",
  "Clinical-grade sensitivity and specificity.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "American Psychiatric Association. Diagnostic and Statistical Manual of Mental Disorders, 5th ed. 2013.",
  "Insel T et al. Research Domain Criteria (RDoC). American Journal of Psychiatry. 2010;167(7):748-751.",
  "Kapur S et al. Why has it taken so long for biological psychiatry to develop clinical tests. Molecular Psychiatry. 2012;17:1174-1179.",
  "Stephan KE et al. Charting the landscape of priority problems in psychiatry. Lancet Psychiatry. 2016;3(1):e1.",
 ],
 "demo_data": {"a": ("biomarkers in clinical use for major psychiatric diagnoses", 0.5),
               "b": ("major psychiatric diagnoses", 10.0), "bounds": (0.02, 0.1),
               "step1": "essentially zero of ten major diagnoses has a clinical biomarker - a gap unique in medicine",
               "confirm": "markers found in stratified cohorts validate independently",
               "refute": "disorders prove to have no stable biologic subtypes"},
},
# ------------------------------------------------------------------ rank 2
{
 "key": "dsm-validity",
 "name": "Are Psychiatric Diagnoses Real?",
 "group": "Nosology",
 "ladder_rank": 2, "ladder_tier": "foundations",
 "problem": "Do schizophrenia, bipolar disorder, and depression carve nature at its joints - or are they useful fictions awaiting replacement?",
 "description": "Psychiatric nosology - the DSM/ICD categories - is under sustained attack: massive comorbidity (most patients meet multiple diagnoses), shared genetics across 'distinct' disorders, and symptom dimensions that cut across categories. Critics argue the categories are reified checklists; defenders argue they remain clinically indispensable. The field cannot agree on what its objects of study are.",
 "background": "Kendell's validation criteria (1970s) and Robins & Guze (1970) set the program; DSM-III/IV/V implemented it. But genetic studies (PGC) found shared risk across schizophrenia, bipolar, depression; HiTOP and RDoC proposed dimensional alternatives. The debate - categories versus dimensions - is psychiatry's oldest unresolved argument. As of 2026 the DSM-5-TR still rules clinically while research moves dimensional.",
 "why_it_matters": "If the categories are wrong, every trial, gene study, and treatment guideline built on them is misaimed. Nosology is the foundation everything else stands on.",
 "sig_pointer": "The Signature system's proposed approach treats diagnoses as provisional clusters, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that psychiatric categories are provisional clusters - real patterns with fuzzy boundaries - and the field needs both: categories for clinical action, dimensions for research. "
  "Assumptions: (1) symptom clusters reflect real regularities; (2) boundaries are genuinely fuzzy; (3) a dual system is workable. "
  "Reasoning path: a dual model explains both clinical utility and research failure, predicting that dimensional research will gradually re-carve categories. "
  "Proposed mechanism: 'dual nosology' - clinical categories retained for care, dimensional biology driving research, with formal translation rules between them. "
  "What would confirm it: dimensional findings progressively redefining categories with better treatment prediction. "
  "What would kill it: evidence that categories are entirely arbitrary, or that dimensions never yield clinical traction. "
  "What this does not claim: it does not claim any category is invalid, offers no diagnostic advice, and does not constitute medical advice."),
 "sig_lens": "The Signature lens reads the diagnosis debate as a both-and problem, and asks what dual system would serve care and science together.",
 "how_it_works": "Researchers study nosology through genetic correlations, HiTOP dimensional modeling, and treatment-prediction comparisons.",
 "key_points": [
  "Comorbidity is the rule; 'pure' diagnoses are rare.",
  "Genetics is shared across supposedly distinct disorders.",
  "HiTOP and RDoC propose dimensional alternatives.",
  "DSM-5-TR still rules clinical practice.",
  "The categories-versus-dimensions debate is decades old.",
 ],
 "requirements": [
  "Dimensional models with clinical utility.",
  "Translation rules between research and clinical systems.",
  "Treatment prediction beating current categories.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Robins E, Guze SB. Establishment of diagnostic validity. American Journal of Psychiatry. 1970;126:983-987.",
  "Kotov R et al. The Hierarchical Taxonomy of Psychopathology (HiTOP). Journal of Abnormal Psychology. 2017;126(4):454-477.",
  "Cross-Disorder Group of the Psychiatric Genomics Consortium. Genetic relationship between five psychiatric disorders. Lancet. 2013;382:998-1008.",
  "Kendler KS. The nature of psychiatric disorders. World Psychiatry. 2016;15:5-12.",
 ],
 "demo_data": {"a": ("psychiatric patients meeting criteria for multiple diagnoses, percent (approx)", 50.0),
               "b": ("percent scale", 100.0), "bounds": (0.35, 0.65),
               "step1": "half of patients meet multiple diagnoses - the categories overlap more than they separate",
               "confirm": "dimensional findings progressively redefine categories with better treatment prediction",
               "refute": "dimensions prove to yield no clinical traction"},
},
# ------------------------------------------------------------------ rank 3
{
 "key": "antidepressant-delay",
 "name": "Why Do Antidepressants Take Weeks?",
 "group": "Treatment",
 "ladder_rank": 3, "ladder_tier": "foundations",
 "problem": "SSRIs raise serotonin within hours but lift depression in weeks - what happens in the gap, and why?",
 "description": "Serotonin reuptake blockade is immediate; mood improvement takes 2-6 weeks. The delay implies the therapeutic mechanism is downstream - neuroplasticity, BDNF, hippocampal neurogenesis, network remodeling - but the actual chain of events remains unproven. The delay costs lives: the highest suicide risk often sits in the treatment-initiation window.",
 "background": "The delay was noted with the first antidepressants (1950s-60s); the monoamine hypothesis couldn't explain it. Neuroplasticity theories (Duman, 1990s-2000s) proposed BDNF and neurogenesis; ketamine's rapid action (2000s-2010s) proved fast relief is possible, sharpening the question. As of 2026 the delay's mechanism is still inferred, not demonstrated.",
 "why_it_matters": "Understanding the delay would reveal the true therapeutic mechanism - and point to genuinely rapid treatments for the highest-risk window.",
 "sig_pointer": "The Signature system's proposed approach treats the delay as network remodeling time, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that the antidepressant delay is network-remodeling time: serotonin is the trigger, and the therapy is the slow rewiring it initiates. "
  "Assumptions: (1) the delay reflects plasticity processes; (2) these are measurable; (3) accelerating them is safe. "
  "Reasoning path: a remodeling model explains both the delay and ketamine's speed (different plasticity route), predicting that plasticity measures will track response. "
  "Proposed mechanism: 'remodeling-tracked' treatment - plasticity biomarkers guiding when the drug has done its slow work. "
  "What would confirm it: plasticity measures predicting response timing in patients. "
  "What would kill it: evidence that the delay is pharmacokinetic or unrelated to plasticity. "
  "What this does not claim: it does not claim the mechanism is known, offers no treatment advice, and does not constitute medical advice."),
 "sig_lens": "The Signature lens reads the weeks-long wait as slow rewiring, and asks what would track the remodeling.",
 "how_it_works": "Researchers study the delay through plasticity biomarkers, neurogenesis models, and rapid-acting comparator drugs like ketamine.",
 "key_points": [
  "Serotonin rises in hours; mood lifts in weeks.",
  "The delay implies downstream plasticity mechanisms.",
  "BDNF and neurogenesis are leading but unproven candidates.",
  "Ketamine proves rapid relief is biologically possible.",
  "The initiation window carries elevated risk.",
 ],
 "requirements": [
  "Plasticity measures tracking response in patients.",
  "Proof of the causal chain from drug to remodeling to mood.",
  "Rapid treatments safe for the high-risk window.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Duman RS et al. Neuronal plasticity and survival in mood disorders. Biological Psychiatry. 2000;48:732-739.",
  "Harmer CJ et al. How do antidepressants work? British Journal of Psychiatry. 2009;195:102-108.",
  "Zarate CA et al. Ketamine and rapid antidepressant action. Various; 2006-2019.",
  "Castren E, Hen R. Neuronal plasticity and antidepressants. Nature Reviews Neuroscience. 2013;14:101-111.",
 ],
 "demo_data": {"a": ("hours to antidepressant response (approx)", 672.0),
               "b": ("hours to serotonin rise (approx)", 6.0), "bounds": (80.0, 160.0),
               "step1": "672 hours of waiting for 6 hours of chemistry - the gap is the unsolved mechanism",
               "confirm": "plasticity measures predict response timing in patients",
               "refute": "the delay proves pharmacokinetic, not plasticity-based"},
},
# ------------------------------------------------------------------ rank 4
{
 "key": "schizophrenia-cause",
 "name": "What Causes Schizophrenia?",
 "group": "Etiology",
 "ladder_rank": 4, "ladder_tier": "foundations",
 "problem": "Schizophrenia affects ~1% of people worldwide, yet its cause remains unknown - genes, dopamine, development, or all three?",
 "description": "Schizophrenia - psychosis, disorganization, negative and cognitive symptoms - has ~80% heritability but no single gene; dopamine explains psychosis partially; neurodevelopmental hits (prenatal infection, obstetric complications, cannabis, urban upbringing) add risk. No unified causal model exists: the field holds fragments - dopamine, glutamate, neurodevelopment, immune - without integration.",
 "background": "Kraepelin's dementia praecox (1899) and Bleuler's schizophrenia (1911) defined it; the dopamine hypothesis (1960s-70s) explained antipsychotics' action. Twin studies established heritability; GWAS (PGC) found 100+ small-effect loci. The neurodevelopmental hypothesis (Weinberger, Murray) reframed it as a developmental disorder. As of 2026 the fragments remain unintegrated.",
 "why_it_matters": "Schizophrenia is among the most disabling human diseases: a causal model would enable prevention and treatments for the currently untreatable symptoms.",
 "sig_pointer": "The Signature system's proposed approach treats schizophrenia as a developmental cascade, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that schizophrenia is a developmental cascade: genetic vulnerability plus prenatal and adolescent hits converge on circuit maturation, and psychosis is the late visible stage. "
  "Assumptions: (1) the cascade has identifiable stages; (2) stages are measurable prospectively; (3) early stages are modifiable. "
  "Reasoning path: a cascade model integrates the fragments - genes set vulnerability, development delivers hits, dopamine is downstream - and predicts stage-specific interventions. "
  "Proposed mechanism: 'cascade-staged' prevention - identifying the developmental stages and intervening at each. "
  "What would confirm it: prospective cohorts showing the staged sequence predicting onset. "
  "What would kill it: evidence that the fragments are independent diseases, not one cascade. "
  "What this does not claim: it does not claim the cause is known, offers no prevention advice, and does not constitute medical advice."),
 "sig_lens": "The Signature lens reads schizophrenia as a cascade with stages, and asks what each stage would need.",
 "how_it_works": "Researchers study causation through prospective birth cohorts, GWAS, prodrome studies, and developmental neuroimaging.",
 "key_points": [
  "Schizophrenia affects ~1% of the population with ~80% heritability.",
  "100+ small-effect genetic loci found; no single gene.",
  "Dopamine explains psychosis only partially.",
  "Neurodevelopmental hits add risk without a unified model.",
  "The field holds fragments, not an integrated cause.",
 ],
 "requirements": [
  "Prospective staging of the developmental cascade.",
  "Integration of genetic, immune, and circuit findings.",
  "Stage-specific prevention proven in trials.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Weinberger DR. Implications of normal brain development for the pathogenesis of schizophrenia. Archives of General Psychiatry. 1987;44:660-669.",
  "Schizophrenia Working Group of the PGC. Biological insights from 108 schizophrenia-associated loci. Nature. 2014;511:421-427.",
  "Murray RM et al. The neurodevelopmental hypothesis. Various; 1992-2017.",
  "Howes OD, Kapur S. The dopamine hypothesis of schizophrenia: version III. Schizophrenia Bulletin. 2009;35:549-562.",
 ],
 "demo_data": {"a": ("schizophrenia heritability, percent (approx)", 80.0),
               "b": ("percent scale", 100.0), "bounds": (0.65, 0.95),
               "step1": "four-fifths heritable yet no gene found - the most genetic disease without a genetic cause",
               "confirm": "prospective cohorts show the staged sequence predicting onset",
               "refute": "the fragments prove to be independent diseases"},
},
# ------------------------------------------------------------------ rank 5
{
 "key": "depression-cause",
 "name": "What Causes Depression?",
 "group": "Etiology",
 "ladder_rank": 5, "ladder_tier": "foundations",
 "problem": "Depression is the leading cause of disability worldwide - yet the serotonin story collapsed and no replacement cause has emerged.",
 "description": "Major depression's etiology is famously unresolved: the serotonin-deficiency hypothesis - never strongly evidenced - was effectively retired by umbrella reviews (Moncrieff 2022). Candidates crowd the field: inflammation, HPA-axis dysregulation, circadian disruption, gut-brain, network dysfunction, stress sensitization, genetics. None explains the whole syndrome; the field lacks a causal core.",
 "background": "The monoamine hypothesis (1960s) organized research for decades despite thin evidence. Stress-diathesis models, learned helplessness, and cognitive theories offered psychology. The 2000s added inflammation (Dantzer) and neuroplasticity. Moncrieff's 2022 umbrella review forced the reckoning: no consistent serotonin-depression link. As of 2026 depression has risk factors, not a cause.",
 "why_it_matters": "Depression disables more people than any other condition: without a causal core, treatment development wanders and prevention is impossible.",
 "sig_pointer": "The Signature system's proposed approach treats depression as multiple causal routes to one syndrome, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that depression is a final common syndrome: multiple distinct causal routes - inflammatory, circadian, stress-sensitized, network - converge on one clinical picture. "
  "Assumptions: (1) distinct routes exist; (2) they are distinguishable; (3) route determines treatment. "
  "Reasoning path: a routes model explains why no single cause emerged and why treatments work partially - each treats one route - predicting route-matched therapy. "
  "Proposed mechanism: 'route-mapped' depression care - identifying each patient's causal route and matching treatment to it. "
  "What would confirm it: route-matched treatments outperforming one-size-fits-all in trials. "
  "What would kill it: evidence that depression is one causal process after all, or that routes can't be distinguished. "
  "What this does not claim: it does not claim the causes are known, offers no treatment advice, and does not constitute medical advice."),
 "sig_lens": "The Signature lens reads depression as several roads to one place, and asks what map would sort the travelers.",
 "how_it_works": "Researchers study depression's causes through inflammation trials, circadian research, stress biology, and network neuroscience.",
 "key_points": [
  "Depression is the leading cause of disability worldwide.",
  "The serotonin-deficiency story was retired by umbrella review (2022).",
  "Candidates: inflammation, HPA axis, circadian, gut-brain, networks.",
  "The field has risk factors, not a causal core.",
  "Treatments work partially - consistent with multiple routes.",
 ],
 "requirements": [
  "Distinguishable causal routes with markers.",
  "Route-matched treatments proven superior.",
  "A causal core or a validated multi-route model.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Moncrieff J et al. The serotonin theory of depression: a systematic umbrella review. Molecular Psychiatry. 2022;28:3243-3256.",
  "Dantzer R et al. Inflammation and depression. Various; 2008-2020.",
  "Otte C et al. Major depressive disorder. Nature Reviews Disease Primers. 2016;2:16065.",
  "Malhi GS, Mann JJ. Depression. Lancet. 2018;392:2299-2312.",
 ],
 "demo_data": {"a": ("people disabled by depression, millions (approx)", 280.0),
               "b": ("millions scale", 1000.0), "bounds": (0.2, 0.4),
               "step1": "hundreds of millions disabled by a disease with no agreed cause",
               "confirm": "route-matched treatments beat one-size-fits-all in trials",
               "refute": "depression proves to be one causal process after all"},
},
# ------------------------------------------------------------------ rank 6
{
 "key": "bipolar-cause",
 "name": "What Causes Bipolar Disorder?",
 "group": "Etiology",
 "ladder_rank": 6, "ladder_tier": "foundations",
 "problem": "Bipolar disorder swings between mania and depression - what drives the oscillation, and why lithium stabilizes it is still mysterious.",
 "description": "Bipolar disorder's mood oscillation has no agreed mechanism: circadian-clock genes, ion-channel dysfunction, mitochondrial hypotheses, and kindling models all have partial support. Lithium - the most effective mood stabilizer - works through mechanisms (GSK-3, inositol, neuroprotection) still debated after 70 years of use. The field treats the swings without understanding the pendulum.",
 "background": "Kraepelin's manic-depressive insanity (1899) defined the course; Cade's lithium discovery (1949) preceded any theory. Circadian theories (Wehr, Goodwin) linked mood to biological rhythms; the kindling model (Post) proposed episode sensitization. GWAS found overlapping genetics with schizophrenia. As of 2026 lithium's mechanism and the oscillation's cause remain open.",
 "why_it_matters": "Bipolar disorder carries the highest suicide risk of mood disorders and resists treatment: understanding the oscillator would enable real mood stabilization.",
 "sig_pointer": "The Signature system's proposed approach treats bipolarity as a broken biological clock network, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that bipolar oscillation is a coupled-oscillator failure: circadian and cellular clocks that should stabilize each other instead drive the mood swings. "
  "Assumptions: (1) mood tracks clock-network state; (2) the network is measurable; (3) stabilizing clocks stabilizes mood. "
  "Reasoning path: a clock model explains circadian triggers, lithium's clock effects, and episode rhythmicity, predicting clock-targeted stabilization. "
  "Proposed mechanism: 'clock-stabilized' bipolar care - measuring and entraining the patient's oscillator network. "
  "What would confirm it: clock measures predicting episodes and clock interventions preventing them. "
  "What would kill it: evidence that oscillation is unrelated to biological clocks. "
  "What this does not claim: it does not claim the mechanism is known, offers no treatment advice, and does not constitute medical advice."),
 "sig_lens": "The Signature lens reads the mood swings as clocks gone wrong, and asks what would re-entrain them.",
 "how_it_works": "Researchers study bipolar causation through circadian genetics, lithium-mechanism research, and longitudinal mood-clock monitoring.",
 "key_points": [
  "No agreed mechanism for mood oscillation exists.",
  "Lithium works after 70 years with debated mechanisms.",
  "Circadian genes and ion channels are leading candidates.",
  "The kindling model proposes episode sensitization.",
  "Genetics overlaps heavily with schizophrenia.",
 ],
 "requirements": [
  "Clock-network measures predicting episodes.",
  "Lithium's mechanism resolved.",
  "Clock-targeted stabilization proven in trials.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Cade JFJ. Lithium salts in the treatment of psychotic excitement. Medical Journal of Australia. 1949;2:349-352.",
  "Goodwin FK, Jamison KR. Manic-Depressive Illness. Oxford University Press; 2007.",
  "McCarthy MJ, Welsh DK. Cellular circadian clocks in bipolar disorder. Various; 2012-2020.",
  "Stahl SM et al. Bipolar disorder mechanisms. Various; 2015-2022.",
 ],
 "demo_data": {"a": ("years lithium used with debated mechanism (approx)", 75.0),
               "b": ("years scale", 100.0), "bounds": (0.6, 0.9),
               "step1": "seventy-five years of lithium without an agreed mechanism - psychiatry's most useful mystery",
               "confirm": "clock measures predict episodes and clock interventions prevent them",
               "refute": "oscillation proves unrelated to biological clocks"},
},
# ------------------------------------------------------------------ rank 7
{
 "key": "placebo",
 "name": "The Placebo Effect in Psychiatry",
 "group": "Treatment",
 "ladder_rank": 7, "ladder_tier": "foundations",
 "problem": "Placebo response in depression trials keeps rising - is it expectation, natural course, or proof the drugs barely work?",
 "description": "Antidepressant trials show large and growing placebo responses - often 30-40% - shrinking drug-placebo differences. The field cannot separate true placebo effect (expectation-driven improvement) from natural course, regression to the mean, and trial artifacts. The rising placebo response threatens the entire drug-development pipeline: new drugs can't beat a rising bar.",
 "background": "Placebo responses were noted in early trials; the increase was quantified in the 2000s-2010s (Walsh, Kirsch). Explanations compete: better trial conduct, milder enrolled patients, expectancy effects, marketing. Kirsch's analyses argued drug effects are small relative to placebo. As of 2026 the field still can't decompose the placebo response or stop its rise.",
 "why_it_matters": "If the drug effect is mostly placebo, the pharmacology era rests on sand; if placebo is a real neurobiological effect, it should be harnessed, not controlled away.",
 "sig_pointer": "The Signature system's proposed approach decomposes the placebo response into parts, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that the 'placebo response' is several effects bundled: true expectancy neurobiology, natural course, and trial artifacts - and each needs different handling. "
  "Assumptions: (1) the components are separable; (2) expectancy is neurobiological; (3) trial designs can isolate components. "
  "Reasoning path: a decomposition model explains the rising response (changing trial populations) and predicts designs that isolate true drug effects. "
  "Proposed mechanism: 'decomposed' trial designs - separating expectancy, course, and artifact before measuring drug effects. "
  "What would confirm it: decomposed designs showing stable drug effects across eras. "
  "What would kill it: evidence that the response is entirely artifact, or that components can't be separated. "
  "What this does not claim: it does not claim drugs don't work, offers no treatment advice, and does not constitute medical advice."),
 "sig_lens": "The Signature lens reads the placebo response as several effects in one coat, and asks what unbundling would reveal.",
 "how_it_works": "Researchers study placebo through expectancy neuroimaging, trial-design methodology, and meta-analytic decomposition.",
 "key_points": [
  "Placebo response in depression trials reaches 30-40%.",
  "The response has risen over decades, shrinking drug-placebo gaps.",
  "Expectancy, natural course, and artifacts are confounded.",
  "The rise threatens new drug development.",
  "Decomposition would rescue trial science.",
 ],
 "requirements": [
  "Separated measures of expectancy, course, and artifact.",
  "Trial designs with stable drug-effect estimates.",
  "Harnessing of true expectancy effects therapeutically.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Kirsch I et al. Initial severity and antidepressant benefits. PLoS Medicine. 2008;5(2):e45.",
  "Walsh BT et al. Placebo response in studies of major depression. JAMA. 2002;287:1840-1847.",
  "Benedetti F. Placebo Effects. Oxford University Press; 2014.",
  "Rutherford BR, Roose SP. A model of placebo response in antidepressant trials. American Journal of Psychiatry. 2013;170:723-733.",
 ],
 "demo_data": {"a": ("placebo response in depression trials, percent (approx)", 35.0),
               "b": ("percent scale", 100.0), "bounds": (0.25, 0.45),
               "step1": "a third of patients improve on sugar pills - the effect trials can't explain or escape",
               "confirm": "decomposed designs show stable drug effects across eras",
               "refute": "the response proves entirely artifactual"},
},
# ------------------------------------------------------------------ rank 8
{
 "key": "negative-symptoms",
 "name": "Treating Schizophrenia's Negative Symptoms",
 "group": "Treatment",
 "ladder_rank": 8, "ladder_tier": "foundations",
 "problem": "Antipsychotics quiet hallucinations but leave apathy, flat affect, and social withdrawal untouched - why is there no treatment for negative symptoms?",
 "description": "Negative symptoms - avolition, anhedonia, flat affect, alogia - drive schizophrenia's disability more than psychosis does, yet no drug treats them. Antipsychotics (dopamine blockade) target positive symptoms; glutamate, inflammation, and cognitive-enhancement approaches have all failed in trials. The neurobiology of diminished motivation is barely mapped.",
 "background": "The positive/negative distinction (Crow, Andreasen, 1980s) framed the problem; second-generation antipsychotics promised broader efficacy and delivered mostly metabolic side effects. Glutamatergic trials (glycine, D-serine, bitopertin) failed; anti-inflammatory add-ons disappointed. As of 2026 negative symptoms remain psychiatry's most treatment-resistant target.",
 "why_it_matters": "Negative symptoms determine whether patients work, connect, and live independently: treating them would change schizophrenia's prognosis more than any antipsychotic advance.",
 "sig_pointer": "The Signature system's proposed approach treats negative symptoms as a motivation-circuit problem, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that negative symptoms are a reward-circuit disorder distinct from psychosis: dopamine blockade treats the wrong circuit, and motivation needs its own pharmacology. "
  "Assumptions: (1) motivation circuits are separable from psychosis circuits; (2) they are druggable; (3) current drugs miss them. "
  "Reasoning path: a circuit-separation model explains why antipsychotics fail negatives and predicts motivation-targeted drugs. "
  "Proposed mechanism: 'motivation-targeted' pharmacology - drugs acting on reward and effort circuits rather than psychosis circuits. "
  "What would confirm it: motivation-circuit drugs improving negatives in trials. "
  "What would kill it: evidence that negatives are irreversible deficit states, not circuit disorders. "
  "What this does not claim: it does not claim a treatment exists, offers no treatment advice, and does not constitute medical advice."),
 "sig_lens": "The Signature lens reads the apathy as a circuit problem, not a psychosis leftover, and asks what would rewire motivation.",
 "how_it_works": "Researchers study negative symptoms through reward-circuit imaging, glutamate and inflammation trials, and effort-based behavioral measures.",
 "key_points": [
  "Negative symptoms drive disability more than psychosis.",
  "No drug is approved for primary negative symptoms.",
  "Glutamate and anti-inflammatory trials failed.",
  "The motivation neurobiology is barely mapped.",
  "Second-generation antipsychotics didn't solve it.",
 ],
 "requirements": [
  "Mapped motivation-circuit pathology in schizophrenia.",
  "Drugs targeting reward/effort circuits.",
  "Trial success where all previous approaches failed.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Crow TJ. Molecular pathology of schizophrenia. British Medical Journal. 1980;280:66-68.",
  "Andreasen NC. Negative symptoms in schizophrenia. Archives of General Psychiatry. 1982;39:784-788.",
  "Kirkpatrick B et al. The NIMH-MATRICS consensus on negative symptoms. Schizophrenia Bulletin. 2006;32:214-219.",
  "Remington G et al. Treating negative symptoms. Various; 2016-2022.",
 ],
 "demo_data": {"a": ("drugs approved for primary negative symptoms", 0.5),
               "b": ("drugs approved for psychosis (approx)", 20.0), "bounds": (0.01, 0.05),
               "step1": "twenty drugs for hallucinations, essentially none for apathy - the untreated half of schizophrenia",
               "confirm": "motivation-circuit drugs improve negatives in trials",
               "refute": "negatives prove to be irreversible deficit states"},
},
# ------------------------------------------------------------------ rank 9
{
 "key": "cognition-schizophrenia",
 "name": "Cognitive Impairment in Schizophrenia",
 "group": "Treatment",
 "ladder_rank": 9, "ladder_tier": "foundations",
 "problem": "Cognitive deficits - memory, attention, executive function - are schizophrenia's core disability, yet no treatment improves them. Why?",
 "description": "Cognitive impairment in schizophrenia precedes psychosis, predicts functional outcome better than any symptom, and resists every treatment: antipsychotics don't help, cognitive enhancers failed in trials (MATRICS), and remediation training shows modest transfer. The neural basis - prefrontal dysconnectivity, GABAergic deficits, neurodevelopmental lesions - is described but not druggable.",
 "background": "Kraepelin named it dementia praecox for the cognitive decline; the MATRICS initiative (2000s) organized the search for pro-cognitive drugs. Trial after trial failed (alpha-7 nicotinic, 5-HT, glutamate). Cognitive remediation helps modestly. As of 2026 cognition remains the untreatable core of schizophrenia.",
 "why_it_matters": "Cognition determines employment, independence, and quality of life: a pro-cognitive treatment would do more for patients than any antipsychotic.",
 "sig_pointer": "The Signature system's proposed approach treats cognitive impairment as a developmental circuit lesion, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that cognitive impairment is a developmental circuit lesion - miswired prefrontal networks from aberrant maturation - and adult pharmacology can't rewire development. "
  "Assumptions: (1) the lesion is developmental; (2) adult drugs can't reverse miswiring; (3) plasticity-based retraining can partially compensate. "
  "Reasoning path: a developmental-lesion model explains universal drug failure and predicts that early intervention plus plasticity training is the path. "
  "Proposed mechanism: 'rewiring-focused' cognition care - intensive plasticity-based remediation during developmental windows. "
  "What would confirm it: early plasticity interventions showing durable cognitive gains. "
  "What would kill it: evidence that the lesion is degenerative and progressive, not developmental. "
  "What this does not claim: it does not claim a treatment exists, offers no treatment advice, and does not constitute medical advice."),
 "sig_lens": "The Signature lens reads the cognitive deficit as miswiring, not chemistry, and asks what would rewire it.",
 "how_it_works": "Researchers study cognitive impairment through prefrontal imaging, MATRICS trial programs, and remediation research.",
 "key_points": [
  "Cognitive deficits precede psychosis and predict outcome.",
  "No drug improves cognition in schizophrenia.",
  "The MATRICS pro-cognitive drug program failed.",
  "Remediation training shows modest transfer.",
  "The basis is developmental miswiring, not adult chemistry.",
 ],
 "requirements": [
  "Proof of the developmental-lesion model.",
  "Plasticity interventions with durable gains.",
  "Early-intervention windows identified.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Green MF. What are the functional consequences of neurocognitive deficits in schizophrenia? American Journal of Psychiatry. 1996;153:321-330.",
  "Keefe RSE et al. MATRICS and pro-cognitive drug development. Various; 2004-2013.",
  "Barch DM, Ceaser A. Cognition in schizophrenia. Annual Review of Clinical Psychology. 2012;8:321-348.",
  "Wykes T et al. Cognitive remediation meta-analyses. Various; 2011-2021.",
 ],
 "demo_data": {"a": ("pro-cognitive drugs approved for schizophrenia", 0.5),
               "b": ("failed pro-cognitive trial programs (approx)", 15.0), "bounds": (0.01, 0.06),
               "step1": "fifteen failed drug programs, zero approvals - the untreatable core of the disease",
               "confirm": "early plasticity interventions show durable cognitive gains",
               "refute": "the lesion proves degenerative rather than developmental"},
},
# ------------------------------------------------------------------ rank 10
{
 "key": "treatment-resistant-depression",
 "name": "Treatment-Resistant Depression",
 "group": "Treatment",
 "ladder_rank": 10, "ladder_tier": "foundations",
 "problem": "A third of depressed patients fail multiple treatments - what makes depression resistant, and what breaks the resistance?",
 "description": "Treatment-resistant depression (TRD) - failure of two or more adequate antidepressant trials - affects roughly a third of depressed patients. Options (augmentation, ECT, ketamine, TMS, psychedelics) help some; many remain ill for years. Whether resistance is a distinct biology or the severe end of a spectrum is unknown - and nothing predicts which patient will resist.",
 "background": "STAR*D (2006) quantified the problem: remission falls with each failed trial. TRD definitions standardized around two failures. Ketamine (2000s-2010s) and esketamine (2019) offered rapid options; psychedelics show promise. But prediction remains absent and mechanisms of resistance unmapped. As of 2026 TRD is defined by failure, not biology.",
 "why_it_matters": "TRD concentrates depression's suffering, disability, and suicide risk: understanding resistance would rescue the patients current medicine abandons.",
 "sig_pointer": "The Signature system's proposed approach treats resistance as a distinct biology, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that treatment resistance is a distinct biology - not just severe depression - with its own mechanisms (glutamate, inflammation, network rigidity) that standard drugs don't touch. "
  "Assumptions: (1) TRD biology differs qualitatively; (2) it is measurable; (3) matching mechanism to biology breaks resistance. "
  "Reasoning path: a distinct-biology model explains why more of the same fails and predicts mechanism-matched rescue therapies. "
  "Proposed mechanism: 'resistance-typed' treatment - identifying the resistance mechanism and matching the intervention to it. "
  "What would confirm it: resistance typing predicting which rescue therapy works. "
  "What would kill it: evidence that TRD is merely severe depression on a continuum. "
  "What this does not claim: it does not claim a cure exists, offers no treatment advice, and does not constitute medical advice."),
 "sig_lens": "The Signature lens reads resistance as a different disease hiding in the same diagnosis, and asks what typing would expose it.",
 "how_it_works": "Researchers study TRD through STAR*D-style sequencing trials, ketamine and psychedelic research, and resistance-biomarker searches.",
 "key_points": [
  "Roughly a third of depressed patients fail multiple treatments.",
  "STAR*D showed remission falls with each failed trial.",
  "TRD is defined by failure, not by biology.",
  "Ketamine and psychedelics offer partial rescue options.",
  "Nothing predicts who will resist.",
 ],
 "requirements": [
  "Biological typing of resistance mechanisms.",
  "Proof that typing predicts rescue-therapy response.",
  "Rescue options for all resistance types.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Rush AJ et al. STAR*D outcomes. American Journal of Psychiatry. 2006;163:1905-1917.",
  "Conway CR et al. Treatment-resistant depression definitions. Various; 2017-2021.",
  "Zarate CA et al. Ketamine for TRD. Various; 2006-2019.",
  "McIntyre RS et al. TRD mechanisms and management. Various; 2014-2023.",
 ],
 "demo_data": {"a": ("depressed patients failing multiple treatments, percent (approx)", 30.0),
               "b": ("percent scale", 100.0), "bounds": (0.2, 0.4),
               "step1": "a third of patients fail treatment after treatment - defined by failure, not biology",
               "confirm": "resistance typing predicts which rescue therapy works",
               "refute": "TRD proves to be merely severe depression on a continuum"},
},
# ------------------------------------------------------------------ rank 11
{
 "key": "ect-mechanism",
 "name": "How Does ECT Work?",
 "group": "Treatment",
 "ladder_rank": 11, "ladder_tier": "foundations",
 "problem": "ECT is psychiatry's most effective treatment - and nobody knows how it works. Why does inducing a seizure cure depression?",
 "description": "Electroconvulsive therapy - brief electrically induced seizure under anesthesia - has the highest response rates in severe depression (~70-90%), yet its mechanism is unknown: neurogenesis, neuroplasticity, network reset, neurotransmitter changes, and neuroendocrine effects are all proposed, none proven. The mystery sustains stigma and blocks improvement of the technique.",
 "background": "ECT was introduced by Cerletti and Bini (1938); its efficacy was established while theories lagged. Modern ECT is safe and refined (brief pulse, unilateral), but the mechanism question persisted through every era. Ketamine's discovery renewed interest in 'reset' mechanisms. As of 2026 the most effective treatment in psychiatry remains mechanistically unexplained.",
 "why_it_matters": "Understanding ECT would allow designing its benefits without seizures, anesthesia, or stigma - potentially the most important therapeutic advance in psychiatry.",
 "sig_pointer": "The Signature system's proposed approach treats ECT as a network-reset event, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that ECT is a network reset: the seizure forces a pathological brain network out of its attractor state, and the therapeutic work is the network's reorganization afterward. "
  "Assumptions: (1) depression involves attractor states; (2) seizures disrupt them; (3) the reset can be achieved more selectively. "
  "Reasoning path: a reset model explains high efficacy across diagnoses and predicts that targeted network disruption will match ECT. "
  "Proposed mechanism: 'reset without seizure' - focal network-disruption techniques achieving ECT's reorganization selectively. "
  "What would confirm it: network measures showing attractor escape predicting ECT response. "
  "What would kill it: evidence that the mechanism is purely neurochemical, not network-level. "
  "What this does not claim: it does not claim the mechanism is known, offers no treatment advice, and does not constitute medical advice."),
 "sig_lens": "The Signature lens reads the seizure as a reboot, and asks what targeted reboot would keep the benefits.",
 "how_it_works": "Researchers study ECT through neuroimaging of network changes, seizure-parameter trials, and neuroplasticity measures.",
 "key_points": [
  "ECT has the highest response rates in severe depression (~70-90%).",
  "Its mechanism is unknown after 85+ years.",
  "Candidates: neurogenesis, plasticity, network reset, endocrine.",
  "Modern ECT is safe but stigmatized.",
  "Understanding it could yield seizure-free equivalents.",
 ],
 "requirements": [
  "Network-level proof of the reset mechanism.",
  "Response prediction from pre-treatment networks.",
  "Focal techniques matching ECT's efficacy.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Cerletti U, Bini L. Un nuovo metodo di shockterapia. Bollettino Accademia Medica Roma. 1938;64:136-138.",
  "UK ECT Review Group. Efficacy and safety of ECT. Lancet. 2003;361:799-808.",
  "Lisanby SH. Electroconvulsive therapy for depression. NEJM. 2007;357:1939-1945.",
  "Bolwig TG. How does ECT work? Theories. Various; 2011-2014.",
 ],
 "demo_data": {"a": ("ECT response rate in severe depression, percent (approx)", 80.0),
               "b": ("percent scale", 100.0), "bounds": (0.65, 0.95),
               "step1": "four in five respond to a treatment nobody understands - efficacy without mechanism",
               "confirm": "network measures show attractor escape predicting ECT response",
               "refute": "the mechanism proves purely neurochemical, not network-level"},
},
# ------------------------------------------------------------------ rank 12
{
 "key": "suicide-neurobiology",
 "name": "The Neurobiology of Suicide",
 "group": "Etiology",
 "ladder_rank": 12, "ladder_tier": "compounded",
 "problem": "Suicide kills 700,000+ people yearly, yet its neurobiology is barely mapped - what drives the transition from despair to action?",
 "description": "Suicide's neurobiology is among psychiatry's least developed areas: serotonin findings are inconsistent, the transition from ideation to action is unmapped, and known risk factors (depression, impulsivity, access to means) predict poorly at the individual level. The field cannot distinguish who will act from who will only suffer - the central unsolved prediction problem in all of medicine.",
 "background": "Serotonin-suicide links (Asberg, 1970s-80s) launched the biology; the ideation-to-action framework (Klonsky, 2010s) clarified that different factors govern thinking versus acting. Means restriction proved the most effective prevention - an environmental, not biological, intervention. As of 2026 no biological marker predicts the transition to action.",
 "why_it_matters": "Suicide is a leading cause of death in young people: mapping the ideation-to-action transition would enable prevention at the critical moment.",
 "sig_pointer": "The Signature system's proposed approach separates ideation biology from action biology, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that suicidal ideation and suicidal action have different biologies: ideation is the mood disorder's product, action is an impulsivity-plus-opportunity event. "
  "Assumptions: (1) the two are biologically separable; (2) action has its own markers; (3) the transition has warning signals. "
  "Reasoning path: a two-biology model explains why depression treatment doesn't reliably prevent suicide and predicts action-specific prevention. "
  "Proposed mechanism: 'transition-focused' prevention - detecting the ideation-to-action shift and intervening at the transition. "
  "What would confirm it: distinct markers for ideation versus action validated prospectively. "
  "What would kill it: evidence that action is purely situational with no biology. "
  "What this does not claim: it does not claim prediction is possible today, offers no prevention advice beyond established means-restriction, and does not constitute medical advice. Anyone in crisis should contact local emergency services or a crisis line."),
 "sig_lens": "The Signature lens reads suicide as two problems - the despair and the act - and asks what biology separates them.",
 "how_it_works": "Researchers study suicide neurobiology through postmortem studies, the ideation-to-action framework, and means-restriction epidemiology.",
 "key_points": [
  "700,000+ suicide deaths yearly worldwide.",
  "Serotonin findings are inconsistent.",
  "Ideation and action appear to have different drivers.",
  "Individual-level prediction remains poor.",
  "Means restriction is the most proven prevention.",
 ],
 "requirements": [
  "Biology of the ideation-to-action transition.",
  "Markers distinguishing who will act.",
  "Transition-targeted prevention proven effective.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Asberg M et al. Serotonin and suicide. Various; 1976-1986.",
  "Klonsky ED, May AM. The three-step theory of suicide. International Journal of Cognitive Therapy. 2015;8:114-129.",
  "World Health Organization. Suicide worldwide estimates. 2021.",
  "Turecki G et al. Suicide neurobiology. Nature Reviews Neuroscience. 2019;20:628-641.",
 ],
 "demo_data": {"a": ("annual suicide deaths worldwide, thousands (approx)", 700.0),
               "b": ("thousands scale", 1000.0), "bounds": (0.55, 0.85),
               "step1": "hundreds of thousands die yearly from a transition science cannot predict",
               "confirm": "distinct markers for ideation versus action validate prospectively",
               "refute": "action proves purely situational with no biology"},
},
# ------------------------------------------------------------------ rank 13
{
 "key": "addiction-mechanism",
 "name": "The Mechanism of Addiction",
 "group": "Addiction",
 "ladder_rank": 13, "ladder_tier": "compounded",
 "problem": "Addiction hijacks the brain's reward system - but why do some users become addicted while others don't, and what would truly break the cycle?",
 "description": "Addiction - compulsive drug use despite harm - involves dopamine reward circuits, habit systems, stress pathways, and prefrontal control loss. Yet vulnerability varies enormously: most users don't become addicted. Genetics explains part; trauma, environment, and psychiatric comorbidity explain more; but the transition from use to compulsion has no agreed mechanism, and no treatment reliably restores control.",
 "background": "The dopamine-reward model (Wise, Koob) organized the field; the opponent-process and allostasis theories (Koob, Le Moal) described the cycle. Genetics found modest heritability; the ACE studies linked trauma to addiction. Medications (methadone, buprenorphine, naltrexone) manage opioids and alcohol partially; stimulant addiction has no approved medication. As of 2026 the use-to-compulsion transition remains unmapped.",
 "why_it_matters": "Addiction kills hundreds of thousands yearly and devastates families: understanding the compulsion transition would enable prevention and real cures.",
 "sig_pointer": "The Signature system's proposed approach treats addiction as a control-circuit failure, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that addiction is a prefrontal control-circuit failure: the reward system learns normally, but the braking system - prefrontal regulation of habit circuits - fails to develop or is damaged. "
  "Assumptions: (1) control circuits are separable from reward circuits; (2) their failure is measurable; (3) strengthening them restores control. "
  "Reasoning path: a control-failure model explains why knowledge of harm doesn't stop use and predicts control-restoring interventions. "
  "Proposed mechanism: 'control-restored' addiction care - interventions strengthening prefrontal regulation of habit circuits. "
  "What would confirm it: control measures predicting recovery and control-targeted interventions improving outcomes. "
  "What would kill it: evidence that compulsion is purely reward-driven with control intact. "
  "What this does not claim: it does not claim a cure exists, offers no treatment advice, and does not constitute medical advice."),
 "sig_lens": "The Signature lens reads addiction as brakes failing, not the engine overpowering, and asks what would restore the brakes.",
 "how_it_works": "Researchers study addiction through reward-circuit imaging, vulnerability genetics, trauma epidemiology, and control-circuit interventions.",
 "key_points": [
  "Most drug users don't become addicted; vulnerability varies enormously.",
  "Dopamine models explain reward but not the compulsion transition.",
  "Trauma and comorbidity are major risk factors.",
  "Stimulant addiction has no approved medication.",
  "The use-to-compulsion mechanism is unmapped.",
 ],
 "requirements": [
  "Mapped control-circuit pathology in addiction.",
  "Vulnerability markers predicting the transition.",
  "Control-restoring interventions proven effective.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Koob GF, Le Moal M. Drug addiction and allostasis. Various; 1997-2008.",
  "Wise RA. Dopamine and addiction. Various; 1980-2004.",
  "Volkow ND et al. Addiction circuitry. Various; 2003-2016.",
  "Felitti VJ et al. ACE study and addiction risk. American Journal of Preventive Medicine. 1998;14:245-258.",
 ],
 "demo_data": {"a": ("drug users who become addicted, percent (approx)", 15.0),
               "b": ("percent scale", 100.0), "bounds": (0.08, 0.25),
               "step1": "a minority of users become addicted - the vulnerability gap science can't explain",
               "confirm": "control measures predict recovery and control-targeted interventions improve outcomes",
               "refute": "compulsion proves purely reward-driven with control intact"},
},
# ------------------------------------------------------------------ rank 14
{
 "key": "ptsd-memory",
 "name": "PTSD and Traumatic Memory",
 "group": "Trauma",
 "ladder_rank": 14, "ladder_tier": "compounded",
 "problem": "Traumatic memories refuse to fade like normal memories - what makes them indelible, and what would let them be reconsolidated?",
 "description": "PTSD - intrusive re-experiencing, avoidance, hyperarousal after trauma - reflects memory gone wrong: the traumatic memory is vivid, fragmented, and unextinguished. Fear-conditioning models explain part; but why some trauma survivors develop PTSD while most don't, and why extinction learning fails in PTSD, remain unsolved. Reconsolidation-based treatments (propranolol, novel approaches) show promise without a proven mechanism.",
 "background": "Fear-conditioning models (LeDoux, Davis) provided the biology; the amygdala-hippocampus-prefrontal circuit became the canonical model. Twin studies showed vulnerability is partly heritable. Reconsolidation research (Nader, 2000) offered a mechanism for memory updating; clinical translation has been slow and contested. As of 2026 PTSD treatment (trauma-focused therapy, SSRIs) helps many but not all.",
 "why_it_matters": "PTSD affects millions - veterans, assault survivors, disaster victims: understanding traumatic memory would unlock treatments that actually erase the disorder rather than manage it.",
 "sig_pointer": "The Signature system's proposed approach treats PTSD as a reconsolidation failure, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that PTSD is a reconsolidation failure: normal memories update when retrieved, but traumatic memories retrieve without updating - the update gate is stuck. "
  "Assumptions: (1) reconsolidation is the normal update mechanism; (2) trauma locks it; (3) unlocking it permits cure. "
  "Reasoning path: a reconsolidation model explains intrusive vividness and predicts that update-gate interventions will work. "
  "Proposed mechanism: 'reconsolidation-unlocked' PTSD treatment - retrieving the memory while the update gate is pharmacologically opened. "
  "What would confirm it: reconsolidation-based treatments showing durable PTSD remission in trials. "
  "What would kill it: evidence that traumatic memories are consolidated differently and can't be updated. "
  "What this does not claim: it does not claim a cure exists, offers no treatment advice, and does not constitute medical advice."),
 "sig_lens": "The Signature lens reads the haunting memory as a file that won't save over, and asks what would unlock the update.",
 "how_it_works": "Researchers study PTSD memory through fear-conditioning models, reconsolidation research, and trauma-focused treatment trials.",
 "key_points": [
  "Traumatic memories are vivid, fragmented, and resist extinction.",
  "Most trauma survivors don't develop PTSD; vulnerability is unexplained.",
  "The amygdala-hippocampus-prefrontal model is canonical but incomplete.",
  "Reconsolidation offers a mechanism without proven clinical translation.",
  "Current treatments help many but not all.",
 ],
 "requirements": [
  "Proof of the reconsolidation-failure model in humans.",
  "Update-gate interventions with durable remission.",
  "Vulnerability markers predicting who develops PTSD.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Nader K et al. Fear memories require protein synthesis for reconsolidation. Nature. 2000;406:722-726.",
  "LeDoux JE. Emotion circuits in the brain. Annual Review of Neuroscience. 2000;23:155-184.",
  "Pitman RK et al. PTSD biology and treatment. Various; 2002-2012.",
  "Koenen KC et al. PTSD genetics and epidemiology. Various; 2003-2017.",
 ],
 "demo_data": {"a": ("trauma survivors developing PTSD, percent (approx)", 10.0),
               "b": ("percent scale", 100.0), "bounds": (0.05, 0.2),
               "step1": "one in ten trauma survivors develops PTSD - the vulnerability difference without an explanation",
               "confirm": "reconsolidation-based treatments show durable remission in trials",
               "refute": "traumatic memories prove consolidated in an un-updatable form"},
},
# ------------------------------------------------------------------ rank 15
{
 "key": "autism-etiology",
 "name": "The Causes of Autism",
 "group": "Neurodevelopment",
 "ladder_rank": 15, "ladder_tier": "compounded",
 "problem": "Autism prevalence keeps rising and its causes remain fragmented - hundreds of genes, environmental hints, no unified etiology. What actually causes autism?",
 "description": "Autism spectrum disorder - social-communication differences and restricted/repetitive behaviors - has ~80% heritability with hundreds of implicated genes, each explaining a tiny fraction. Environmental factors (parental age, prenatal exposures) add modest risk. No unified causal model connects genes to the autistic brain; the 'spectrum' may be many conditions.",
 "background": "Kanner (1943) and Asperger (1944) described it; the refrigerator-mother theory was debunked by twin studies establishing heritability. Genomics (2000s-2010s) found hundreds of risk genes (CHD8, SHANK3, etc.) and copy-number variants. The female-protective effect and the broad-spectrum concept complicated the picture. As of 2026 autism has risk architecture, not etiology.",
 "why_it_matters": "Autism affects 1-2% of children: etiology would enable early identification, targeted supports, and understanding of the autistic brain.",
 "sig_pointer": "The Signature system's proposed approach treats autism as convergent developmental pathways, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that autism is convergent pathways: hundreds of genetic and environmental hits funnel through a few developmental processes (synaptic pruning, excitatory-inhibitory balance) to produce the spectrum. "
  "Assumptions: (1) convergence points exist; (2) they are measurable early; (3) they are modifiable. "
  "Reasoning path: a convergence model explains genetic heterogeneity with phenotypic similarity and predicts pathway-targeted early intervention. "
  "Proposed mechanism: 'pathway-targeted' early support - identifying each child's convergent pathway and supporting development through it. "
  "What would confirm it: pathway measures predicting developmental trajectories and guiding effective support. "
  "What would kill it: evidence that no convergence exists - each genetic cause producing its own unrelated condition. "
  "What this does not claim: it does not claim autism needs curing, takes no position on neurodiversity debates, offers no treatment advice, and does not constitute medical advice."),
 "sig_lens": "The Signature lens reads the spectrum as many roads converging, and asks where they meet.",
 "how_it_works": "Researchers study autism etiology through genomics, prospective infant-sibling studies, and developmental neuroscience.",
 "key_points": [
  "Autism has ~80% heritability with hundreds of implicated genes.",
  "Each gene explains a tiny fraction of cases.",
  "Environmental factors add modest risk.",
  "No unified model connects genes to the autistic brain.",
  "The spectrum may be many conditions.",
 ],
 "requirements": [
  "Identified convergence pathways.",
  "Early pathway measures predicting trajectories.",
  "Pathway-matched supports proven effective.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Kanner L. Autistic disturbances of affective contact. Nervous Child. 1943;2:217-250.",
  "Tick B et al. Heritability of autism spectrum disorders. JAMA. 2016;315:194-195.",
  "De Rubeis S et al. Synaptic, transcriptional and chromatin genes in autism. Nature. 2014;515:209-215.",
  "Lord C et al. Autism spectrum disorder. Lancet. 2018;392:508-520.",
 ],
 "demo_data": {"a": ("autism risk genes implicated (approx)", 500.0),
               "b": ("genes scale (thousands)", 1000.0), "bounds": (0.35, 0.65),
               "step1": "hundreds of genes implicated, each explaining a sliver - heterogeneity without a unifying cause",
               "confirm": "pathway measures predict trajectories and guide effective support",
               "refute": "no convergence proves to exist between genetic causes"},
},
# ------------------------------------------------------------------ rank 16
{
 "key": "eating-disorders",
 "name": "The Biology of Eating Disorders",
 "group": "Etiology",
 "ladder_rank": 16, "ladder_tier": "compounded",
 "problem": "Anorexia has the highest mortality of any psychiatric disorder, yet its biology is barely understood - what drives the relentless drive for thinness?",
 "description": "Anorexia nervosa - self-starvation with distorted body image - kills more patients than any other psychiatric illness (medical complications, suicide). Its biology is obscure: reward-circuit abnormalities, serotonin and dopamine findings, gut-brain signals, and genetic risk all appear, but no causal model exists. Treatment (refeeding, therapy) has high relapse; no drug is approved.",
 "background": "Anorexia was medicalized in the 19th century (Gull, Lasegue); the cultural explanation dominated the late 20th century. Biology emerged in the 2000s-2010s: GWAS found metabolic as well as psychiatric genetics (Watson 2019), implicating metabolism itself. But the drive mechanism - why starvation feels right - remains unmapped. As of 2026 no medication treats anorexia's core.",
 "why_it_matters": "Anorexia kills the young and resists treatment: understanding its biology would convert the deadliest psychiatric disorder into a treatable one.",
 "sig_pointer": "The Signature system's proposed approach treats anorexia as a reward-circuit inversion, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that anorexia is a reward-circuit inversion: starvation and thinness activate reward pathways that food activates in others - the drive is neurobiological, not vanity. "
  "Assumptions: (1) the inversion is measurable; (2) it precedes the disorder; (3) it is modifiable. "
  "Reasoning path: an inversion model explains why willpower-based treatment fails and predicts reward-retargeting interventions. "
  "Proposed mechanism: 'reward-retargeted' anorexia care - interventions normalizing the inverted reward response. "
  "What would confirm it: reward measures predicting onset and retargeting improving outcomes. "
  "What would kill it: evidence that the reward findings are consequences of starvation, not causes. "
  "What this does not claim: it does not claim a treatment exists, offers no treatment advice, and does not constitute medical advice."),
 "sig_lens": "The Signature lens reads the starvation drive as reward gone inverted, and asks what would flip it back.",
 "how_it_works": "Researchers study eating-disorder biology through reward imaging, metabolic genetics, and refeeding-outcome research.",
 "key_points": [
  "Anorexia has the highest mortality of any psychiatric disorder.",
  "GWAS implicates metabolic as well as psychiatric genetics.",
  "No drug is approved for anorexia's core symptoms.",
  "Relapse rates after treatment are high.",
  "The drive mechanism remains unmapped.",
 ],
 "requirements": [
  "Proof of the reward-inversion model.",
  "Pre-illness markers of the inversion.",
  "Reward-retargeting interventions proven effective.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Gull WW. Anorexia nervosa. Transactions of the Clinical Society of London. 1874;7:22-28.",
  "Watson HJ et al. Genome-wide association study of anorexia nervosa. Nature Genetics. 2019;51:1207-1214.",
  "Kaye WH et al. Neurobiology of anorexia. Various; 2005-2013.",
  "Arcelus J et al. Mortality rates in eating disorders. Archives of General Psychiatry. 2011;68:724-731.",
 ],
 "demo_data": {"a": ("anorexia mortality, standardized ratio (approx)", 6.0),
               "b": ("general population ratio", 1.0), "bounds": (4.0, 9.0),
               "step1": "six times the expected death rate - the deadliest psychiatric disorder, biologically unexplained",
               "confirm": "reward measures predict onset and retargeting improves outcomes",
               "refute": "reward findings prove to be consequences of starvation"},
},
# ------------------------------------------------------------------ rank 17
{
 "key": "personality-disorders",
 "name": "The Origins of Personality Disorders",
 "group": "Etiology",
 "ladder_rank": 17, "ladder_tier": "compounded",
 "problem": "Borderline personality disorder devastates lives through unstable relationships and self-harm - but what creates a disordered personality?",
 "description": "Personality disorders - enduring maladaptive patterns (borderline, antisocial, narcissistic, and others) - have the murkiest etiology in psychiatry: genetics, childhood adversity, attachment, and neurobiology all contribute, but no model explains how a personality becomes disordered. Borderline PD is the most studied and most treatable (DBT helps); the others barely have evidence-based treatments.",
 "background": "Personality disorders entered the DSM in 1980; borderline PD's trauma links (Herman, Linehan) shaped treatment. DBT (Linehan, 1990s) proved a personality pattern could be treated. Genetics shows moderate heritability; neuroimaging finds emotion-circuit abnormalities. But the developmental mechanism - how adversity becomes personality - remains undescribed. As of 2026 etiology is a list of risk factors, not a model.",
 "why_it_matters": "Personality disorders cause immense suffering and have almost no pharmacological treatments: a developmental model would enable prevention and new therapies.",
 "sig_pointer": "The Signature system's proposed approach treats personality disorders as developmental emotion-regulation trajectories, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that personality disorders are emotion-regulation developmental trajectories: early adversity plus vulnerability canalize development into stable maladaptive patterns. "
  "Assumptions: (1) trajectories are identifiable prospectively; (2) canalization points exist; (3) early redirection works. "
  "Reasoning path: a trajectory model explains the adversity link and DBT's success (it re-trains regulation), predicting early-intervention prevention. "
  "Proposed mechanism: 'trajectory-redirected' prevention - identifying at-risk developmental paths and redirecting them early. "
  "What would confirm it: prospective trajectories predicting adult personality pathology and redirection preventing it. "
  "What would kill it: evidence that personality pathology emerges without developmental precursors. "
  "What this does not claim: it does not claim prevention exists, offers no treatment advice, and does not constitute medical advice."),
 "sig_lens": "The Signature lens reads the disordered personality as development canalized wrong, and asks where the channel could be redirected.",
 "how_it_works": "Researchers study personality-disorder origins through longitudinal developmental cohorts, adversity research, and DBT mechanism studies.",
 "key_points": [
  "Personality disorders have the murkiest etiology in psychiatry.",
  "Borderline PD is the most studied and most treatable (DBT).",
  "Genetics, adversity, and attachment all contribute.",
  "Almost no pharmacological treatments exist.",
  "How adversity becomes personality is undescribed.",
 ],
 "requirements": [
  "Prospective developmental trajectories.",
  "Identified canalization points.",
  "Early redirection proven preventive.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Linehan MM. Cognitive-Behavioral Treatment of Borderline Personality Disorder. Guilford; 1993.",
  "Herman JL. Trauma and Recovery. Basic Books; 1992.",
  "Distel MA et al. Heritability of borderline personality. Various; 2008-2010.",
  "Gunderson JG. Borderline personality disorder. NEJM. 2011;364:2037-2042.",
 ],
 "demo_data": {"a": ("personality disorders with proven pharmacological treatment", 0.5),
               "b": ("personality disorder categories (approx)", 10.0), "bounds": (0.02, 0.1),
               "step1": "ten categories, essentially zero proven drugs - the least treatable corner of psychiatry",
               "confirm": "prospective trajectories predict pathology and redirection prevents it",
               "refute": "personality pathology proves to emerge without developmental precursors"},
},
# ------------------------------------------------------------------ rank 18
{
 "key": "neuroinflammation",
 "name": "Neuroinflammation in Mental Illness",
 "group": "Mechanisms",
 "ladder_rank": 18, "ladder_tier": "compounded",
 "problem": "Inflammation is elevated in depression and schizophrenia - but is it cause, consequence, or coincidence?",
 "description": "Meta-analyses consistently show elevated inflammatory markers (CRP, IL-6, TNF-alpha) in depression and schizophrenia; microglial activation appears in imaging; anti-inflammatory add-ons show small benefits. But causality is unproven: inflammation could drive illness, result from stress and lifestyle, or mark a subtype. The field oscillates between excitement and skepticism.",
 "background": "The cytokine hypothesis of depression (Smith 1991, Dantzer 2000s) launched the field; interferon-alpha's depressive side effects provided a human model. Schizophrenia's immune links (prenatal infection, MHC genetics) converged. Anti-inflammatory trials (minocycline, celecoxib) showed modest signals. As of 2026 inflammation is a replicated correlate without proven causality.",
 "why_it_matters": "If inflammation causes a subtype of mental illness, anti-inflammatory treatments would be the first mechanistically new psychiatric drugs in decades.",
 "sig_pointer": "The Signature system's proposed approach treats inflammation as a subtype marker, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that inflammation defines a subtype: a fraction of depression and schizophrenia is inflammatory in origin, and anti-inflammatories work only there. "
  "Assumptions: (1) the inflammatory subtype is real and stable; (2) it is identifiable by markers; (3) subtype-matched treatment works. "
  "Reasoning path: a subtype model explains small average trial effects (dilution by non-inflammatory patients) and predicts stratified-trial success. "
  "Proposed mechanism: 'inflammation-stratified' treatment - identifying inflammatory-subtype patients and treating the inflammation. "
  "What would confirm it: stratified trials showing large effects in the inflammatory subgroup. "
  "What would kill it: evidence that inflammation is purely consequential in all patients. "
  "What this does not claim: it does not claim anti-inflammatories treat mental illness, offers no treatment advice, and does not constitute medical advice."),
 "sig_lens": "The Signature lens reads the inflammation signal as a subtype hiding in averages, and asks what stratification would reveal.",
 "how_it_works": "Researchers study neuroinflammation through cytokine meta-analyses, microglial imaging, and stratified anti-inflammatory trials.",
 "key_points": [
  "Inflammatory markers are consistently elevated in depression and schizophrenia.",
  "Microglial activation appears in brain imaging.",
  "Anti-inflammatory add-ons show small average benefits.",
  "Causality versus consequence is unproven.",
  "The field oscillates between excitement and skepticism.",
 ],
 "requirements": [
  "A stable, identifiable inflammatory subtype.",
  "Stratified trials with large subgroup effects.",
  "Causal proof, not just correlation.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Dantzer R et al. From inflammation to sickness and depression. Nature Reviews Neuroscience. 2008;9:46-56.",
  "Miller AH, Raison CL. The role of inflammation in depression. Nature Reviews Immunology. 2016;16:22-34.",
  "Mondelli V et al. Inflammation in schizophrenia. Various; 2010-2017.",
  "Kappelmann N et al. Anti-inflammatory treatment meta-analyses. Various; 2018-2021.",
 ],
 "demo_data": {"a": ("depressed patients with elevated CRP, percent (approx)", 30.0),
               "b": ("percent scale", 100.0), "bounds": (0.2, 0.45),
               "step1": "a third of depressed patients show inflammation - a subtype or a side effect, nobody knows",
               "confirm": "stratified trials show large effects in the inflammatory subgroup",
               "refute": "inflammation proves purely consequential in all patients"},
},
# ------------------------------------------------------------------ rank 19
{
 "key": "gut-brain",
 "name": "The Gut-Brain Axis in Psychiatry",
 "group": "Mechanisms",
 "ladder_rank": 19, "ladder_tier": "compounded",
 "problem": "Gut microbes affect mood and behavior in animals - but does the human gut microbiome cause psychiatric illness, or just reflect it?",
 "description": "The gut-brain axis - microbial metabolites, vagus nerve, immune signaling - modulates behavior in rodents: germ-free mice show altered anxiety, and fecal transplants transfer behavioral traits. Human studies find microbiome differences in depression and autism, but causality is unproven: diet, drugs, and lifestyle confound everything. Probiotic psychiatry ('psychobiotics') is marketed ahead of evidence.",
 "background": "The field exploded in the 2010s (Cryan, Dinan); rodent transplant experiments were striking. Human association studies followed but couldn't establish direction. The first small human FMT-for-depression trials are underway. As of 2026 the gut-brain axis is a proven animal phenomenon and an unproven human therapy.",
 "why_it_matters": "If gut microbes causally drive mood, dietary and microbial interventions would be the most accessible psychiatric treatments ever - but hype currently outruns evidence.",
 "sig_pointer": "The Signature system's proposed approach tests causality through the metabolite, not the microbe, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that the gut-brain signal is carried by specific metabolites (short-chain fatty acids, tryptophan metabolites), and the therapeutic unit is the molecule, not the microbiome. "
  "Assumptions: (1) causal metabolites exist; (2) they reach the brain; (3) they are administrable. "
  "Reasoning path: a metabolite model explains rodent findings and predicts metabolite-based interventions. "
  "Proposed mechanism: 'metabolite-targeted' gut-brain therapy - identifying and delivering the causal microbial molecules. "
  "What would confirm it: metabolite interventions improving mood in controlled trials. "
  "What would kill it: evidence that human effects are entirely confounded, with no causal microbial signal. "
  "What this does not claim: it does not claim probiotics treat mental illness, offers no treatment advice, and does not constitute medical advice."),
 "sig_lens": "The Signature lens reads the gut signal as molecules, not microbes, and asks which molecules carry the message.",
 "how_it_works": "Researchers study the gut-brain axis through metabolomics, FMT trials, and confound-controlled human cohorts.",
 "key_points": [
  "Rodent transplants transfer behavioral traits convincingly.",
  "Human studies show associations, not causation.",
  "Diet, drugs, and lifestyle confound human research.",
  "'Psychobiotics' are marketed ahead of evidence.",
  "Metabolites may be the real therapeutic unit.",
 ],
 "requirements": [
  "Causal human evidence, not just association.",
  "Identified causal metabolites.",
  "Metabolite interventions proven in trials.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Cryan JF, Dinan TG. Mind-altering microorganisms. Nature Reviews Neuroscience. 2012;13:701-712.",
  "Zheng P et al. Gut microbiome remodeling in depression. Molecular Psychiatry. 2016;21:786-796.",
  "Kelly JR et al. Transferring depression via microbiota. Journal of Psychiatric Research. 2016;82:109-118.",
  "Bastiaanssen TFS et al. Gut-brain axis reviews. Various; 2019-2024.",
 ],
 "demo_data": {"a": ("human RCTs proving microbiome causation of psychiatric illness", 0.5),
               "b": ("rodent studies showing behavioral transfer (approx)", 100.0), "bounds": (0.001, 0.01),
               "step1": "a hundred rodent studies, essentially zero causal human trials - the translation gap is total",
               "confirm": "metabolite interventions improve mood in controlled trials",
               "refute": "human effects prove entirely confounded"},
},
# ------------------------------------------------------------------ rank 20
{
 "key": "missing-heritability",
 "name": "Missing Heritability in Psychiatry",
 "group": "Genetics",
 "ladder_rank": 20, "ladder_tier": "compounded",
 "problem": "Psychiatric disorders are highly heritable, yet known genetic variants explain only a fraction - where is the missing heritability?",
 "description": "Twin studies put schizophrenia and bipolar heritability near 80%; GWAS loci explain perhaps 10-25% of variance. The gap - missing heritability - may hide in rare variants, structural variation, gene-environment interaction, epigenetics, or overestimated twin heritability. Each explanation has partial support; none closes the gap.",
 "background": "The missing-heritability problem was named in 2009 (Maher) across genetics; psychiatry is its most extreme case. Whole-exome studies found rare variants (SETD1A and others) with larger effects. Polygenic scores predict modestly. As of 2026 the gap persists: most genetic risk remains unmapped.",
 "why_it_matters": "Finding the missing heritability would reveal the actual genetic architecture - and with it, the biology the common variants only hint at.",
 "sig_pointer": "The Signature system's proposed approach looks for heritability in interactions, not just variants, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that missing heritability hides in gene-environment interaction: genetic risk that only expresses under specific environmental conditions, invisible to main-effect GWAS. "
  "Assumptions: (1) GxE effects are large; (2) environments are measurable; (3) interaction-aware designs find them. "
  "Reasoning path: an interaction model explains why heritability is high but variants are weak, predicting GxE-aware mapping success. "
  "Proposed mechanism: 'interaction-mapped' genetics - GWAS designs incorporating measured environments. "
  "What would confirm it: GxE loci explaining substantial heritability in replication. "
  "What would kill it: evidence that twin heritability was simply overestimated, with no hidden architecture. "
  "What this does not claim: it does not claim the heritability is found, offers no genetic counseling, and does not constitute medical advice."),
 "sig_lens": "The Signature lens reads the missing heritability as hiding in interactions, and asks what environments would reveal it.",
 "how_it_works": "Researchers study missing heritability through rare-variant sequencing, GxE designs, and heritability-methodology research.",
 "key_points": [
  "Twin heritability near 80%; GWAS explains 10-25%.",
  "Rare variants (SETD1A etc.) have larger effects but are rare.",
  "Gene-environment interaction is the leading hiding place.",
  "Polygenic scores predict only modestly.",
  "The gap is psychiatry's most extreme in genetics.",
 ],
 "requirements": [
  "GxE loci with replicated large effects.",
  "Measured environments at GWAS scale.",
  "Heritability accounting that closes the gap.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Maher B. Personal genomes: the case of the missing heritability. Nature. 2008;456:18-21.",
  "Sullivan PF et al. Psychiatric genomics. Various; 2012-2022.",
  "Singh T et al. Rare variants in schizophrenia (SCHEMA). Nature. 2022;604:509-516.",
  "Border R et al. Heritability estimation debates. Various; 2019-2022.",
 ],
 "demo_data": {"a": ("heritability explained by known variants, percent (approx)", 20.0),
               "b": ("twin-study heritability, percent (approx)", 80.0), "bounds": (0.15, 0.35),
               "step1": "a fifth explained of four-fifths heritable - three-quarters of the genetics is missing",
               "confirm": "GxE loci explain substantial heritability in replication",
               "refute": "twin heritability proves overestimated with no hidden architecture"},
},
# ------------------------------------------------------------------ rank 21
{
 "key": "psychedelic-mechanism",
 "name": "How Do Psychedelics Work?",
 "group": "Treatment",
 "ladder_rank": 21, "ladder_tier": "compounded",
 "problem": "Psilocybin and MDMA show remarkable therapeutic promise - but is the healing in the molecule, the mystical experience, or the therapy around it?",
 "description": "Psychedelics (psilocybin for depression, MDMA for PTSD) show large effect sizes in trials, with benefits persisting months after dosing. The mechanism is contested: 5-HT2A-driven plasticity, the subjective 'mystical experience,' network disintegration-reintegration, and the psychotherapeutic container all claim credit. Whether the trip is necessary - or a side effect - determines the entire drug-development path.",
 "background": "The first psychedelic era (1950s-60s) ended with prohibition; the renaissance began with Griffiths (2006) and Carhart-Harris imaging. MDMA for PTSD (MAPS trials) and psilocybin for depression showed striking results. Non-hallucinogenic analogs are in development to test whether the experience is required. As of 2026 the mechanism question is the field's central fork.",
 "why_it_matters": "The answer determines whether the future is guided psychedelic therapy or a daily non-tripping pill - two completely different medicines and industries.",
 "sig_pointer": "The Signature system's proposed approach separates the plasticity from the experience, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that psychedelic healing is plasticity plus meaning: the molecule opens a plasticity window, and the experience (or therapy) determines what rewires during it. "
  "Assumptions: (1) the plasticity window is real and measurable; (2) content during the window shapes outcome; (3) the two are separable. "
  "Reasoning path: a window-plus-content model explains both rapid biological effects and the experience-outcome correlation, predicting optimized combinations. "
  "Proposed mechanism: 'window-optimized' psychedelic care - maximizing plasticity while structuring the therapeutic content. "
  "What would confirm it: non-hallucinogenic analogs tested against full psychedelics with content controlled. "
  "What would kill it: evidence that the molecule alone (or the experience alone) fully explains outcomes. "
  "What this does not claim: it does not claim psychedelics are proven treatments, offers no treatment advice, and does not constitute medical advice."),
 "sig_lens": "The Signature lens reads the trip as a window, not the therapy itself, and asks what should happen inside the window.",
 "how_it_works": "Researchers study psychedelic mechanisms through 5-HT2A imaging, non-hallucinogenic analog trials, and experience-outcome analyses.",
 "key_points": [
  "Effect sizes are large with months-long persistence.",
  "The mechanism is the field's central fork in the road.",
  "5-HT2A plasticity, mystical experience, and therapy all claim credit.",
  "Non-hallucinogenic analogs test whether the trip is needed.",
  "The answer shapes two completely different futures.",
 ],
 "requirements": [
  "Separated measures of plasticity, experience, and therapy effects.",
  "Analog-versus-classic controlled comparisons.",
  "Optimized window-plus-content protocols.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Griffiths RR et al. Psilocybin and mystical experience. Psychopharmacology. 2006;187:268-283.",
  "Carhart-Harris RL et al. Neural correlates of the psychedelic state. PNAS. 2012;109:2138-2143.",
  "Mitchell JM et al. MDMA for PTSD (MAPS trials). Nature Medicine. 2021;27:1025-1033.",
  "Vargas MV et al. Non-hallucinogenic psychedelic analogs. Various; 2021-2023.",
 ],
 "demo_data": {"a": ("months of benefit after psychedelic dosing (approx)", 6.0),
               "b": ("months scale", 12.0), "bounds": (0.3, 0.7),
               "step1": "half a year of benefit from one or two doses - with the mechanism still contested",
               "confirm": "analog-versus-classic trials separate plasticity from experience effects",
               "refute": "the molecule alone proves to fully explain outcomes"},
},
# ------------------------------------------------------------------ rank 22
{
 "key": "adhd-neurobiology",
 "name": "The Neurobiology of ADHD",
 "group": "Neurodevelopment",
 "ladder_rank": 22, "ladder_tier": "compounded",
 "problem": "ADHD is among the most treatable psychiatric disorders - yet what it fundamentally is remains disputed. A dopamine deficit? A developmental delay? A different cognitive style?",
 "description": "ADHD - inattention, hyperactivity, impulsivity - responds well to stimulants, but its nature is contested: dopamine/norepinephrine deficit models, developmental-delay models (brain maturation lagging ~3 years), reward-timing models, and neurodiversity framings all compete. Adult ADHD's validity was long denied; its persistence and impairment are now established but its adult neurobiology is thin.",
 "background": "Stimulant treatment (Bradley, 1937) preceded theory by decades. Brain imaging (Castellanos, Shaw) showed developmental delay and circuit differences. Genetics found modest heritability with many small loci. The neurodiversity movement reframed ADHD as difference, not deficit. As of 2026 treatment works while theory fragments.",
 "why_it_matters": "ADHD affects millions of children and adults: understanding its nature would improve treatment matching and settle harmful debates about validity.",
 "sig_pointer": "The Signature system's proposed approach treats ADHD as a timing disorder, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that ADHD is fundamentally a timing disorder: reward, attention, and control circuits operate on mismatched timescales, and stimulants resynchronize them. "
  "Assumptions: (1) circuit timing is measurable; (2) mismatch predicts symptoms; (3) resynchronization is the drug mechanism. "
  "Reasoning path: a timing model integrates delay, reward, and dopamine findings, predicting timing-based diagnosis and treatment. "
  "Proposed mechanism: 'timing-matched' ADHD care - measuring circuit timescales and matching interventions to the mismatch. "
  "What would confirm it: timing measures predicting diagnosis and treatment response. "
  "What would kill it: evidence that timing differences are consequences, not causes. "
  "What this does not claim: it does not claim ADHD's nature is settled, offers no treatment advice, and does not constitute medical advice."),
 "sig_lens": "The Signature lens reads ADHD as clocks out of sync, and asks what resynchronization would look like.",
 "how_it_works": "Researchers study ADHD through developmental imaging, reward-timing experiments, and stimulant-mechanism research.",
 "key_points": [
  "Stimulants work well; theory remains fragmented.",
  "Brain maturation lags ~3 years in ADHD (Shaw).",
  "Reward-timing and dopamine models compete.",
  "Adult ADHD is now established but thinly studied.",
  "Neurodiversity framings challenge deficit models.",
 ],
 "requirements": [
  "Measurable circuit-timing differences.",
  "Timing-based diagnosis and treatment matching.",
  "Resolution of the deficit-versus-difference debate with data.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Bradley C. The behavior of children receiving benzedrine. American Journal of Psychiatry. 1937;94:577-585.",
  "Shaw P et al. Attention-deficit/hyperactivity disorder and delayed cortical maturation. PNAS. 2007;104:19649-19654.",
  "Faraone SV et al. ADHD genetics and neurobiology. Various; 2005-2021.",
  "Sonuga-Barke EJS et al. Timing models of ADHD. Various; 2010-2020.",
 ],
 "demo_data": {"a": ("cortical maturation delay in ADHD, years (approx)", 3.0),
               "b": ("childhood years scale", 12.0), "bounds": (0.15, 0.35),
               "step1": "three years of maturational lag - the most concrete finding in a contested disorder",
               "confirm": "timing measures predict diagnosis and treatment response",
               "refute": "timing differences prove to be consequences, not causes"},
},
# ------------------------------------------------------------------ rank 23
{
 "key": "ocd-circuits",
 "name": "OCD Circuit Mechanisms",
 "group": "Mechanisms",
 "ladder_rank": 23, "ladder_tier": "compounded",
 "problem": "OCD's cortico-striatal circuits are the best-mapped in psychiatry - yet deep understanding hasn't produced better treatments. Why?",
 "description": "OCD - intrusive obsessions and compulsive rituals - has the clearest circuit model in psychiatry (cortico-striato-thalamo-cortical loops), successful circuit interventions (DBS, capsulotomy for severe cases), and effective therapy (exposure and response prevention). Yet SSRIs help partially, the circuit model's therapeutic yield has plateaued, and the obsession's origin - why these thoughts, this person - is unknown.",
 "background": "The CSTC model (Baxter, 1990s) organized OCD biology; neuroimaging confirmed hyperactive loops. DBS for severe OCD (1999 onward) proved circuit intervention works. ERP remains the best treatment. But the model hasn't generated new drugs, and the content question - why contamination, why symmetry - is untouched by circuits. As of 2026 OCD is the best-mapped disorder that mapping hasn't cured.",
 "why_it_matters": "OCD is the proof-of-concept for circuit psychiatry: if the best-mapped disorder can't be cured by mapping, the whole circuit program needs rethinking.",
 "sig_pointer": "The Signature system's proposed approach treats OCD as a stuck error-signal, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that OCD is a stuck error-signal: the brain's 'something is wrong' detector fires without resolution, and compulsions are attempts to clear an unclearable signal. "
  "Assumptions: (1) the error signal is identifiable; (2) its stuckness is measurable; (3) unstickable. "
  "Reasoning path: an error-signal model explains the content (threat themes trigger the detector) and predicts signal-targeted interventions. "
  "Proposed mechanism: 'signal-reset' OCD treatment - interventions that clear the stuck error signal rather than suppressing the loop. "
  "What would confirm it: error-signal measures predicting OCD severity and reset interventions working. "
  "What would kill it: evidence that the loops are structurally fixed, not functionally stuck. "
  "What this does not claim: it does not claim a cure exists, offers no treatment advice, and does not constitute medical advice."),
 "sig_lens": "The Signature lens reads the compulsion as a signal that won't clear, and asks what would reset it.",
 "how_it_works": "Researchers study OCD circuits through CSTC imaging, DBS trials, and ERP mechanism research.",
 "key_points": [
  "OCD has psychiatry's clearest circuit model (CSTC loops).",
  "DBS proves circuit intervention can work in severe cases.",
  "ERP remains the most effective treatment.",
  "The model hasn't generated new drugs.",
  "Why these obsessions in this person is unknown.",
 ],
 "requirements": [
  "Identifiable error-signal pathology.",
  "Signal-reset interventions proven effective.",
  "An account of obsession content, not just circuits.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Baxter LR et al. CSTC model of OCD. Various; 1987-1996.",
  "Greenberg BD et al. DBS for OCD. Various; 1999-2010.",
  "Abramowitz JS et al. ERP mechanisms. Various; 2005-2019.",
  "Stein DJ et al. OCD neurobiology. Various; 2019-2023.",
 ],
 "demo_data": {"a": ("OCD patients helped by first-line treatments, percent (approx)", 60.0),
               "b": ("percent scale", 100.0), "bounds": (0.45, 0.75),
               "step1": "the best-mapped disorder still leaves two in five without adequate help",
               "confirm": "error-signal measures predict severity and reset interventions work",
               "refute": "the loops prove structurally fixed, not functionally stuck"},
},
# ------------------------------------------------------------------ rank 24
{
 "key": "lithium-mechanism",
 "name": "How Does Lithium Work?",
 "group": "Mechanisms",
 "ladder_rank": 24, "ladder_tier": "advanced",
 "problem": "Lithium prevents suicide and stabilizes mood better than any alternative - after 75 years, its mechanism is still debated. How can the best drug be the least understood?",
 "description": "Lithium - the lightest metal, a simple ion - is uniquely effective in bipolar disorder: it prevents both poles and distinctively reduces suicide. Proposed mechanisms crowd the field: inositol depletion, GSK-3beta inhibition, neuroprotection, circadian-clock effects, BDNF. None fully explains its clinical profile; the field prescribes a mystery.",
 "background": "Cade (1949) discovered it; the inositol-depletion hypothesis (Berridge, 1980s) and GSK-3 inhibition (Klein, 1990s-2000s) became leading theories. Lithium's anti-suicidal effect - unique among mood stabilizers - resists all mechanistic accounts. As of 2026 lithium remains the most effective and least understood psychiatric drug.",
 "why_it_matters": "Understanding lithium would enable designing its benefits without its toxicity and monitoring burden - and reveal what mood stabilization fundamentally is.",
 "sig_pointer": "The Signature system's proposed approach treats lithium as a multi-target network stabilizer, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that lithium works precisely because it is multi-target: mood stability is a network property, and only a drug hitting several network nodes (inositol, GSK-3, clocks) can stabilize it. "
  "Assumptions: (1) stability is a network property; (2) lithium's targets are network nodes; (3) the combination is the mechanism. "
  "Reasoning path: a network-stabilizer model explains why single-target drugs fail at mood stabilization and predicts multi-node drug design. "
  "Proposed mechanism: 'network-designed' mood stabilizers - drugs hitting lithium's node combination without its toxicity. "
  "What would confirm it: node-combination drugs matching lithium's profile in trials. "
  "What would kill it: evidence that one target fully explains lithium's effects. "
  "What this does not claim: it does not claim the mechanism is known, offers no treatment advice, and does not constitute medical advice."),
 "sig_lens": "The Signature lens reads lithium as a network drug, not a molecule with a target, and asks which node combination is the medicine.",
 "how_it_works": "Researchers study lithium through GSK-3 and inositol research, circadian studies, and anti-suicidal effect investigations.",
 "key_points": [
  "Lithium uniquely prevents suicide among mood stabilizers.",
  "Inositol depletion and GSK-3 inhibition lead the theories.",
  "No single mechanism explains its full clinical profile.",
  "It is the most effective and least understood psychiatric drug.",
  "Understanding it could yield safer replacements.",
 ],
 "requirements": [
  "Proof of the multi-node network model.",
  "Node-combination drugs matching lithium's efficacy.",
  "An account of the anti-suicidal effect specifically.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Cade JFJ. Lithium salts in the treatment of psychotic excitement. Medical Journal of Australia. 1949;2:349-352.",
  "Berridge MJ et al. Inositol depletion hypothesis. Various; 1982-1989.",
  "Klein PS, Melton DA. GSK-3 inhibition by lithium. PNAS. 1996;93:8455-8459.",
  "Cipriani A et al. Lithium and suicide prevention meta-analyses. Various; 2005-2013.",
 ],
 "demo_data": {"a": ("lithium's suicide-risk reduction, percent (approx)", 60.0),
               "b": ("percent scale", 100.0), "bounds": (0.45, 0.75),
               "step1": "three-fifths fewer suicides on a drug whose mechanism is still debated",
               "confirm": "node-combination drugs match lithium's profile in trials",
               "refute": "one target proves to fully explain lithium's effects"},
},
# ------------------------------------------------------------------ rank 25
{
 "key": "antipsychotic-limits",
 "name": "Why Do Antipsychotics Stop at Psychosis?",
 "group": "Treatment",
 "ladder_rank": 25, "ladder_tier": "advanced",
 "problem": "Every antipsychotic ever made blocks dopamine - 70 years without a non-dopamine mechanism reaching patients. Why is the pipeline frozen on one target?",
 "description": "All approved antipsychotics - from chlorpromazine (1952) to the newest - act primarily via dopamine D2 blockade. Glutamate, trace-amine, and muscarinic approaches (KarXT/xanomeline-trospium, approved 2024, is the first real departure) took decades. The dopamine monopoly reflects both the hypothesis's grip and the difficulty of proving efficacy for novel mechanisms.",
 "background": "Chlorpromazine's antipsychotic effect (Delay, Deniker, 1952) preceded the dopamine hypothesis; every subsequent drug followed the D2 template. Clozapine (superior efficacy, agranulocytosis risk) hinted at broader mechanisms. Glutamate hypotheses (Olney, Coyle) motivated decades of failed trials. KarXT's 2024 approval - muscarinic agonism - broke the monopoly. As of 2026 the pipeline is finally diversifying.",
 "why_it_matters": "Dopamine blockade treats psychosis but causes major side effects and misses negatives and cognition: new mechanisms are the only path to better schizophrenia treatment.",
 "sig_pointer": "The Signature system's proposed approach treats the dopamine monopoly as a trial-design artifact, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that the dopamine monopoly is partly a trial-design artifact: trials optimized to detect D2-like effects select D2-like drugs, and novel mechanisms need novel trial designs. "
  "Assumptions: (1) trial designs bias mechanism selection; (2) novel mechanisms need different endpoints; (3) redesigned trials will find them. "
  "Reasoning path: a design-bias model explains decades of glutamate failures and KarXT's success, predicting mechanism-matched trial designs. "
  "Proposed mechanism: 'mechanism-matched' antipsychotic trials - endpoints and populations fitted to each candidate's biology. "
  "What would confirm it: novel-mechanism drugs succeeding in matched designs after failing in standard ones. "
  "What would kill it: evidence that dopamine is simply the only druggable psychosis target. "
  "What this does not claim: it does not claim new drugs exist beyond approved ones, offers no treatment advice, and does not constitute medical advice."),
 "sig_lens": "The Signature lens reads the frozen pipeline as a measurement problem, and asks what trials would unfreeze it.",
 "how_it_works": "Researchers study antipsychotic limits through glutamate and muscarinic trials, trial-methodology research, and clozapine-mechanism studies.",
 "key_points": [
  "Every antipsychotic until 2024 blocked dopamine D2.",
  "KarXT (2024) broke the monopoly via muscarinic agonism.",
  "Glutamate approaches failed for decades in standard trials.",
  "Clozapine's superior efficacy hints at broader mechanisms.",
  "Trial designs may select for D2-like effects.",
 ],
 "requirements": [
  "Mechanism-matched trial designs proven to work.",
  "Novel-mechanism drugs for negatives and cognition.",
  "An account of clozapine's unique efficacy.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Delay J, Deniker P. Chlorpromazine in psychiatry. Various; 1952-1955.",
  "Kane J et al. Clozapine for treatment-resistant schizophrenia. Archives of General Psychiatry. 1988;45:789-796.",
  "Olney JW et al. Glutamate hypotheses. Various; 1995-1999.",
  "Kaul I et al. KarXT (xanomeline-trospium) trials. Various; 2021-2024.",
 ],
 "demo_data": {"a": ("years of dopamine-only antipsychotics (approx)", 70.0),
               "b": ("years scale", 100.0), "bounds": (0.55, 0.85),
               "step1": "seven decades on one receptor - the longest drug-target monopoly in medicine",
               "confirm": "novel-mechanism drugs succeed in mechanism-matched designs",
               "refute": "dopamine proves to be the only druggable psychosis target"},
},
# ------------------------------------------------------------------ rank 26
{
 "key": "prodrome-prediction",
 "name": "Predicting Psychosis Before It Strikes",
 "group": "Prevention",
 "ladder_rank": 26, "ladder_tier": "advanced",
 "problem": "The psychosis prodrome offers a window for prevention - but most 'high-risk' youth never convert, and we can't tell who will. Can the transition be predicted?",
 "description": "Clinical high-risk (CHR) criteria identify youth with ~20-35% psychosis conversion over 2-3 years - meaning most never convert. Prediction models (NAPLS risk calculator) improve odds modestly. The false-positive problem blocks preventive intervention: treating all CHR youth would medicate many who'd never become ill. The biology of the conversion moment is unknown.",
 "background": "Prodrome research (McGorry, Yung, 1990s-2000s) defined CHR; NAPLS validated risk calculators. Omega-3 and CBT prevention trials showed modest signals. But conversion prediction plateaued: clinical plus biomarker models barely beat clinical alone. As of 2026 the field can enrich risk but not predict conversion.",
 "why_it_matters": "Preventing psychosis would avert schizophrenia's devastation: the prodrome is the only window, and prediction is its key.",
 "sig_pointer": "The Signature system's proposed approach detects the conversion as a dynamical transition, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that psychosis conversion is a dynamical-systems transition - a tipping point with early-warning signals (critical slowing down) detectable before it happens. "
  "Assumptions: (1) conversion is a tipping point; (2) early-warning signals exist in symptoms and physiology; (3) they are detectable in time. "
  "Reasoning path: a tipping-point model explains sudden onset and predicts that intensive longitudinal monitoring will catch the transition. "
  "Proposed mechanism: 'early-warning' prodrome monitoring - high-frequency symptom and physiologic tracking detecting critical slowing. "
  "What would confirm it: early-warning signals prospectively predicting conversion. "
  "What would kill it: evidence that conversion is gradual with no tipping point. "
  "What this does not claim: it does not claim prediction works today, offers no clinical advice, and does not constitute medical advice."),
 "sig_lens": "The Signature lens reads the psychosis onset as a tipping point, and asks what signals precede the fall.",
 "how_it_works": "Researchers study prodrome prediction through NAPLS cohorts, risk calculators, and dynamical-systems modeling.",
 "key_points": [
  "CHR criteria yield 20-35% conversion; most never convert.",
  "The false-positive problem blocks preventive treatment.",
  "Risk calculators improve odds only modestly.",
  "Biomarkers barely beat clinical prediction.",
  "The conversion moment's biology is unknown.",
 ],
 "requirements": [
  "Early-warning signals validated prospectively.",
  "Prediction accurate enough for preventive intervention.",
  "Preventive treatments proven in high-risk youth.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "McGorry PD et al. Early intervention in psychosis. Various; 1996-2010.",
  "Cannon TD et al. NAPLS risk calculator. American Journal of Psychiatry. 2016;173:980-988.",
  "Fusar-Poli P et al. CHR meta-analyses. Various; 2012-2020.",
  "Nelson B et al. Dynamical models of psychosis onset. Various; 2017-2022.",
 ],
 "demo_data": {"a": ("CHR youth converting to psychosis, percent (approx)", 25.0),
               "b": ("percent scale", 100.0), "bounds": (0.15, 0.4),
               "step1": "three-quarters of 'high-risk' youth never convert - prediction too weak to act on",
               "confirm": "early-warning signals prospectively predict conversion",
               "refute": "conversion proves gradual with no tipping point"},
},
# ------------------------------------------------------------------ rank 27
{
 "key": "comorbidity",
 "name": "Why Does Everything Co-occur?",
 "group": "Nosology",
 "ladder_rank": 27, "ladder_tier": "advanced",
 "problem": "Depression with anxiety, ADHD with autism, schizophrenia with substance use - comorbidity is the rule. Is it shared biology, or are the categories just wrong?",
 "description": "Psychiatric comorbidity - meeting criteria for multiple disorders - is so common it challenges the category system: depression-anxiety co-occur in half of cases; ADHD-autism overlap substantially; psychosis and substance use travel together. Explanations compete: shared genetics, common risk factors, causal chains (one disorder causing another), and diagnostic artifacts (overlapping criteria).",
 "background": "Comorbidity was quantified in the ECA and NCS surveys (1980s-90s); the PGC's cross-disorder genetics (2013) proved shared biology. Causal modeling (Mendelian randomization) began disentangling directions. The p-factor (Caspi, 2014) proposed a general psychopathology dimension underlying all comorbidity. As of 2026 the field holds shared biology plus artifacts without a unified account.",
 "why_it_matters": "Comorbidity determines real-world treatment: single-disorder guidelines fail comorbid patients, who are the majority. Understanding it would reorganize care.",
 "sig_pointer": "The Signature system's proposed approach treats comorbidity as network structure, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that comorbidity is network structure: symptoms cause symptoms across diagnostic boundaries, and the network - not shared genes alone - explains co-occurrence patterns. "
  "Assumptions: (1) symptom networks are real and causal; (2) bridge symptoms connect disorders; (3) targeting bridges treats comorbidity. "
  "Reasoning path: a network model explains specific comorbidity patterns and predicts that bridge-symptom interventions will outperform single-disorder treatment. "
  "Proposed mechanism: 'bridge-targeted' comorbidity care - treating the symptoms that connect disorders. "
  "What would confirm it: bridge interventions outperforming single-disorder protocols in comorbid patients. "
  "What would kill it: evidence that comorbidity is entirely genetic overlap with no symptom-level causation. "
  "What this does not claim: it does not claim the categories are wrong, offers no treatment advice, and does not constitute medical advice."),
 "sig_lens": "The Signature lens reads comorbidity as bridges between symptom islands, and asks which bridges carry the traffic.",
 "how_it_works": "Researchers study comorbidity through network analysis, cross-disorder genetics, and the p-factor literature.",
 "key_points": [
  "Comorbidity is the rule across all psychiatric diagnoses.",
  "Cross-disorder genetics proves shared biology.",
  "The p-factor proposes a general psychopathology dimension.",
  "Single-disorder guidelines fail comorbid majorities.",
  "Symptom networks may explain specific patterns.",
 ],
 "requirements": [
  "Causal bridge symptoms identified.",
  "Bridge-targeted treatments proven superior.",
  "A unified account of shared biology and networks.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Kessler RC et al. NCS comorbidity findings. Archives of General Psychiatry. 1994;51:8-19.",
  "Caspi A et al. The p factor. Clinical Psychological Science. 2014;2:119-137.",
  "Borsboom D, Cramer AOJ. Network theory of mental disorders. Annual Review of Clinical Psychology. 2013;9:91-121.",
  "Cross-Disorder Group of the PGC. Genetic relationship between five psychiatric disorders. Lancet. 2013;382:998-1008.",
 ],
 "demo_data": {"a": ("depressed patients with comorbid anxiety, percent (approx)", 50.0),
               "b": ("percent scale", 100.0), "bounds": (0.35, 0.65),
               "step1": "half of depressed patients also meet anxiety criteria - the 'pure' patient is the exception",
               "confirm": "bridge interventions beat single-disorder protocols in comorbid patients",
               "refute": "comorbidity proves entirely genetic overlap"},
},
# ------------------------------------------------------------------ rank 28
{
 "key": "precision-psychiatry",
 "name": "Precision Psychiatry: Matching Treatment to Patient",
 "group": "Treatment",
 "ladder_rank": 28, "ladder_tier": "advanced",
 "problem": "Psychiatry prescribes by trial and error - can treatment ever be matched to the patient's biology on the first try?",
 "description": "Precision psychiatry - the right treatment for the right patient first time - remains aspirational: pharmacogenetic tests (CYP2D6, etc.) guide dosing modestly; no test predicts which antidepressant or antipsychotic will work. Trials (GUIDED) showed small benefits. The biology needed for matching - the subtypes, the markers - doesn't exist yet.",
 "background": "Pharmacogenetics entered psychiatry in the 2000s (CYP testing); commercial combinatorial tests followed with contested evidence. The GUIDED trial (2019) showed modest benefit. Biomarker-guided trials (EMBARC) are underway. As of 2026 precision psychiatry is a promise with pilot data, not a practice.",
 "why_it_matters": "Trial-and-error prescribing wastes months of suffering per patient: precision matching would be the single biggest quality-of-life advance in psychiatric care.",
 "sig_pointer": "The Signature system's proposed approach builds precision from treatment-response biology, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that precision psychiatry must start from response biology: instead of matching drugs to diagnoses, match them to the mechanisms that determine individual response. "
  "Assumptions: (1) response mechanisms are identifiable; (2) they vary between patients; (3) they are measurable pre-treatment. "
  "Reasoning path: a response-biology model explains why diagnosis-based matching fails and predicts mechanism-based matching success. "
  "Proposed mechanism: 'response-typed' prescribing - pre-treatment mechanism measures guiding first-line choice. "
  "What would confirm it: response-typed prescribing beating trial-and-error in randomized trials. "
  "What would kill it: evidence that response is too stochastic for pre-treatment prediction. "
  "What this does not claim: it does not claim precision tests work today, offers no prescribing advice, and does not constitute medical advice."),
 "sig_lens": "The Signature lens reads trial-and-error as a matching problem, and asks what biology would match correctly.",
 "how_it_works": "Researchers study precision psychiatry through pharmacogenetic trials, EMBARC biomarker research, and response-prediction modeling.",
 "key_points": [
  "No test predicts which antidepressant will work for a patient.",
  "Pharmacogenetic tests guide dosing, not drug choice.",
  "The GUIDED trial showed only modest benefit.",
  "Response biology - not diagnosis - may be the matching key.",
  "Precision psychiatry remains a promise with pilot data.",
 ],
 "requirements": [
  "Pre-treatment response predictors with clinical accuracy.",
  "Randomized proof that typed prescribing beats trial-and-error.",
  "Response biology mapped for major drug classes.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Greden JF et al. GUIDED trial. Journal of Psychiatric Research. 2019;111:59-67.",
  "Trivedi MH et al. EMBARC biomarker study. Various; 2016-2020.",
  "Zeier Z et al. Pharmacogenetics in psychiatry. Various; 2018-2022.",
  "Perlis RH. Precision psychiatry reviews. Various; 2016-2021.",
 ],
 "demo_data": {"a": ("first antidepressant trials achieving remission, percent (approx)", 35.0),
               "b": ("percent scale", 100.0), "bounds": (0.25, 0.45),
               "step1": "two-thirds of first prescriptions fail - the cost of trial-and-error psychiatry",
               "confirm": "response-typed prescribing beats trial-and-error in randomized trials",
               "refute": "response proves too stochastic for pre-treatment prediction"},
},
# ------------------------------------------------------------------ rank 29
{
 "key": "replication-crisis",
 "name": "Psychiatry's Replication Crisis",
 "group": "Methods",
 "ladder_rank": 29, "ladder_tier": "advanced",
 "problem": "Landmark findings in psychiatry - from candidate genes to brain-scan signatures - keep failing to replicate. How much of the literature is real?",
 "description": "Psychiatry's replication crisis is severe: candidate-gene associations (the 1990s-2000s literature) almost entirely failed; structural-imaging findings replicate poorly; even some treatment effects shrink in replications. Causes include small samples, publication bias, flexible analyses, and the heterogeneity problem. The field is rebuilding on preregistration and large consortia - but the old literature's wreckage remains.",
 "background": "Candidate-gene failures (2000s-2010s) were the first collapse; the ENIGMA consortium (2009 onward) brought large-scale imaging; preregistration and registered reports spread in the 2010s. GWAS succeeded precisely because it adopted rigorous standards early. As of 2026 psychiatry is mid-rebuild: new standards, old uncertainty.",
 "why_it_matters": "Clinical practice and drug development rest on the literature: if the foundations are unreliable, everything built on them - including current treatments - needs re-examination.",
 "sig_pointer": "The Signature system's proposed approach treats replication as a heterogeneity artifact, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that many replication failures are heterogeneity artifacts: the original finding was real in a subtype, and 'failures' sampled different subtype mixes. "
  "Assumptions: (1) subtype structure explains failures; (2) it is discoverable; (3) subtype-aware replication succeeds. "
  "Reasoning path: a heterogeneity model rescues real findings from the wreckage and predicts subtype-stratified replication. "
  "Proposed mechanism: 'subtype-aware' replication science - re-testing findings within biologically defined subgroups. "
  "What would confirm it: failed findings replicating within subtypes. "
  "What would kill it: evidence that the failures were pure false positives with no subtype structure. "
  "What this does not claim: it does not claim any failed finding is real, offers no clinical advice, and does not constitute medical advice."),
 "sig_lens": "The Signature lens reads the replication wreckage as mixed subtypes, and asks what stratified re-testing would salvage.",
 "how_it_works": "Researchers study replication through consortium science, preregistration, and heterogeneity-aware re-analysis.",
 "key_points": [
  "Candidate-gene literature almost entirely failed replication.",
  "Imaging findings replicate poorly across studies.",
  "Causes: small samples, bias, flexible analyses, heterogeneity.",
  "ENIGMA and preregistration are rebuilding standards.",
  "Some 'failures' may be real subtype effects.",
 ],
 "requirements": [
  "Subtype-aware replication successes.",
  "Field-wide preregistration and large samples.",
  "A cleaned literature clinicians can trust.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Ioannidis JPA. Why most published research findings are false. PLoS Medicine. 2005;2(8):e124.",
  "Border R et al. No support for candidate-gene hypotheses. American Journal of Psychiatry. 2019;176:376-387.",
  "Thompson PM et al. ENIGMA consortium. Various; 2009-2020.",
  "Nosek BA et al. Preregistration and reproducibility. Various; 2015-2018.",
 ],
 "demo_data": {"a": ("candidate-gene associations replicating (approx)", 2.0),
               "b": ("candidate-gene associations published (approx)", 100.0), "bounds": (0.005, 0.05),
               "step1": "two in a hundred candidate-gene findings replicated - the most complete literature collapse in medicine",
               "confirm": "failed findings replicate within biologically defined subtypes",
               "refute": "the failures prove to be pure false positives"},
},
# ------------------------------------------------------------------ rank 30
{
 "key": "mind-brain",
 "name": "The Mind-Brain Problem in Psychiatry",
 "group": "Philosophy",
 "ladder_rank": 30, "ladder_tier": "advanced",
 "problem": "Psychiatry treats the mind by changing the brain - but how do subjective experience and neural activity relate? The field works atop philosophy's hardest problem.",
 "description": "The mind-brain problem - how subjective experience arises from neural activity - is philosophy's hard problem (Chalmers) and psychiatry's unspoken foundation: every treatment assumes changing the brain changes the mind, but the relationship is unmapped. Psychotherapy changes the brain without drugs; drugs change experience without insight. The field has no account of how its two treatment modalities connect.",
 "background": "Dualism (Descartes) gave way to identity theory, functionalism, and eliminativism without resolution. Psychiatry pragmatically ignored the problem: the biopsychosocial model (Engel, 1977) asserted integration without mechanism. Neuroscience mapped correlates of consciousness (Crick, Koch) without explaining experience. As of 2026 psychiatry works brilliantly and blindly atop the mystery.",
 "why_it_matters": "A real account of mind-brain relations would unify psychiatry's split treatments - therapy and pharmacology - and ground the field's deepest assumptions.",
 "sig_pointer": "The Signature system's proposed approach treats mind and brain as two descriptions of one system, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that mind and brain are two measurement scales of one dynamical system: psychological and neural descriptions constrain each other, and treatment works by moving the system, describable at either scale. "
  "Assumptions: (1) the system is genuinely one; (2) cross-scale constraints are lawful; (3) they are discoverable. "
  "Reasoning path: a one-system model explains why both therapy and drugs work and predicts cross-scale treatment principles. "
  "Proposed mechanism: 'cross-scale' psychiatry - treatment principles stated at both scales with translation rules. "
  "What would confirm it: lawful mind-brain correspondences predicting treatment response across scales. "
  "What would kill it: evidence that the scales are incommensurable - no lawful translation exists. "
  "What this does not claim: it does not claim the hard problem is solved, offers no clinical advice, and does not constitute medical advice."),
 "sig_lens": "The Signature lens reads mind and brain as one system in two languages, and asks for the translation dictionary.",
 "how_it_works": "Researchers study mind-brain relations through consciousness neuroscience, therapy-neuroimaging, and computational psychiatry.",
 "key_points": [
  "The hard problem of consciousness is unsolved.",
  "Psychiatry assumes brain change alters mind without mapping how.",
  "Therapy changes the brain; drugs change experience.",
  "The biopsychosocial model asserts integration without mechanism.",
  "The field works effectively atop the mystery.",
 ],
 "requirements": [
  "Lawful cross-scale correspondences.",
  "Translation rules between psychological and neural descriptions.",
  "Treatment principles valid at both scales.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Chalmers DJ. Facing up to the problem of consciousness. Journal of Consciousness Studies. 1995;2:200-219.",
  "Engel GL. The biopsychosocial model. Science. 1977;196:129-136.",
  "Crick F, Koch C. Consciousness neuroscience. Various; 1990-2003.",
  "Montague PR et al. Computational psychiatry. Various; 2012-2020.",
 ],
 "demo_data": {"a": ("treatment modalities needing a mind-brain account", 2.0),
               "b": ("modalities with one (approx)", 0.5), "bounds": (2.5, 6.0),
               "step1": "two great treatments, zero accounts of how they connect - the foundation nobody mapped",
               "confirm": "lawful mind-brain correspondences predict treatment response",
               "refute": "the scales prove incommensurable"},
},
# ------------------------------------------------------------------ rank 31
{
 "key": "childhood-trauma",
 "name": "How Childhood Trauma Becomes Adult Illness",
 "group": "Development",
 "ladder_rank": 31, "ladder_tier": "advanced",
 "problem": "Childhood adversity massively raises adult psychiatric risk - but the biological embedding mechanism, the how, is still missing.",
 "description": "The ACE studies showed dose-response links between childhood trauma and adult depression, suicide, addiction, and psychosis. But the embedding mechanism - how early experience becomes lasting biology - is unproven: HPA-axis programming, epigenetic changes, immune priming, and brain-development alterations all have partial evidence. Without the mechanism, prevention is generic and treatment can't target the embedding.",
 "background": "The ACE study (Felitti, 1998) quantified the link; Meaney's rat work showed epigenetic programming of stress responses. Human epigenetic studies (McGowan, 2009) found glucocorticoid-receptor methylation in suicide victims with abuse histories. But human causal proof remains elusive and effect sizes are small. As of 2026 the field has correlation at scale and mechanism in fragments.",
 "why_it_matters": "Childhood trauma is the largest preventable driver of adult mental illness: understanding embedding would enable targeted prevention and reversal.",
 "sig_pointer": "The Signature system's proposed approach treats embedding as multi-system programming, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that trauma embedding is multi-system programming: stress, immune, and epigenetic systems are jointly calibrated by early experience, and no single-system account will suffice. "
  "Assumptions: (1) the systems interact; (2) joint calibration is measurable; (3) recalibration is possible. "
  "Reasoning path: a multi-system model explains partial single-system findings and predicts integrated embedding measures. "
  "Proposed mechanism: 'embedding-mapped' prevention - measuring the joint calibration and recalibrating it early. "
  "What would confirm it: integrated measures predicting adult illness and recalibration preventing it. "
  "What would kill it: evidence that the link is entirely genetic confounding with no embedding. "
  "What this does not claim: it does not claim embedding is reversible today, offers no clinical advice, and does not constitute medical advice."),
 "sig_lens": "The Signature lens reads the traumatized child as multi-system programmed, and asks what recalibration would restore.",
 "how_it_works": "Researchers study trauma embedding through ACE cohorts, epigenetic studies, and developmental programming models.",
 "key_points": [
  "ACE studies show dose-response links to adult illness.",
  "Epigenetic programming is proven in animals, unproven in humans.",
  "HPA-axis, immune, and brain changes all appear partially.",
  "No integrated embedding mechanism exists.",
  "Prevention remains generic without the mechanism.",
 ],
 "requirements": [
  "Integrated multi-system embedding measures.",
  "Causal human proof of the embedding mechanism.",
  "Recalibration interventions proven preventive.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Felitti VJ et al. ACE study. American Journal of Preventive Medicine. 1998;14:245-258.",
  "McGowan PO et al. Epigenetic regulation of the glucocorticoid receptor in suicide victims. Nature Neuroscience. 2009;12:342-348.",
  "Meaney MJ et al. Epigenetic programming of stress responses. Various; 2001-2010.",
  "Teicher MH et al. Childhood trauma and brain development. Various; 2003-2016.",
 ],
 "demo_data": {"a": ("adults with 4+ ACEs developing depression, percent (approx)", 25.0),
               "b": ("percent scale", 100.0), "bounds": (0.15, 0.35),
               "step1": "a quarter of heavily traumatized children develop depression - the dose-response without a mechanism",
               "confirm": "integrated measures predict adult illness and recalibration prevents it",
               "refute": "the link proves entirely genetic confounding"},
},
# ------------------------------------------------------------------ rank 32
{
 "key": "dissociation",
 "name": "Dissociation and Consciousness Fragmentation",
 "group": "Mechanisms",
 "ladder_rank": 32, "ladder_tier": "advanced",
 "problem": "Dissociative disorders - including dissociative identity disorder - fragment consciousness itself. What is dissociation neurobiologically, and is DID real?",
 "description": "Dissociation - detachment from experience, identity fragmentation - spans everyday absorption to dissociative identity disorder (DID), psychiatry's most contested diagnosis. Neurobiological research is thin: altered corticolimbic connectivity appears, but the mechanism of identity fragmentation is unmapped. The field is split between trauma-model and sociocognitive-model camps, with the diagnosis's validity still debated.",
 "background": "DID (formerly multiple personality) entered DSM-III (1980); the trauma model (Putnam) and sociocognitive model (Spanos, Lilienfeld) have debated for decades. Neuroimaging (Reinders, 2000s-2010s) found distinct brain states between identities, supporting validity. But mechanism remains unknown and the debate unresolved. As of 2026 dissociation is the least biologically mapped major phenomenon in psychiatry.",
 "why_it_matters": "Dissociation affects trauma survivors profoundly and challenges theories of selfhood: understanding it would illuminate consciousness and validate suffering patients.",
 "sig_pointer": "The Signature system's proposed approach treats dissociation as a compartmentalization mechanism, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that dissociation is a compartmentalization mechanism: under overwhelming threat, the brain partitions experience into non-communicating modules - adaptive in the moment, pathological when the partitions persist. "
  "Assumptions: (1) compartmentalization is a real neural process; (2) it is measurable; (3) reintegration is achievable. "
  "Reasoning path: a compartment model explains both adaptive dissociation and DID, predicting integration-targeted treatment. "
  "Proposed mechanism: 'partition-mapped' dissociation care - identifying the compartments and their triggers, then reintegrating. "
  "What would confirm it: compartment measures predicting symptoms and integration improving outcomes. "
  "What would kill it: evidence that DID is entirely sociocognitive with no neural compartmentalization. "
  "What this does not claim: it does not claim DID's validity is settled, offers no clinical advice, and does not constitute medical advice."),
 "sig_lens": "The Signature lens reads the fragmented self as partitioned, not broken, and asks what would reintegrate the partitions.",
 "how_it_works": "Researchers study dissociation through identity-state neuroimaging, trauma-model versus sociocognitive debates, and integration therapy research.",
 "key_points": [
  "Dissociation spans absorption to identity fragmentation.",
  "DID is psychiatry's most contested diagnosis.",
  "Distinct brain states between identities support validity.",
  "The fragmentation mechanism is unmapped.",
  "Trauma-model and sociocognitive camps remain split.",
 ],
 "requirements": [
  "Measurable compartmentalization processes.",
  "Resolution of the validity debate with data.",
  "Integration-targeted treatments proven effective.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Putnam FW. Dissociation as trauma response. Various; 1989-1997.",
  "Reinders AATS et al. Identity-state neuroimaging in DID. Various; 2003-2014.",
  "Lilienfeld SO et al. Sociocognitive model critiques. Various; 1999-2019.",
  "Spiegel D et al. Dissociation reviews. Various; 2011-2018.",
 ],
 "demo_data": {"a": ("decades of the DID validity debate (approx)", 4.0),
               "b": ("decades scale", 10.0), "bounds": (0.25, 0.55),
               "step1": "forty years of debate over whether the diagnosis is real - with the mechanism still unmapped",
               "confirm": "compartment measures predict symptoms and integration improves outcomes",
               "refute": "DID proves entirely sociocognitive"},
},
# ------------------------------------------------------------------ rank 33
{
 "key": "anxiety-circuits",
 "name": "Anxiety Disorder Circuit Mechanisms",
 "group": "Mechanisms",
 "ladder_rank": 33, "ladder_tier": "advanced",
 "problem": "Anxiety disorders are the commonest psychiatric illnesses - yet fear-circuit models haven't yielded new treatments in decades. What is anxiety, really?",
 "description": "Anxiety disorders - generalized anxiety, panic, phobias, social anxiety - affect ~300 million people. Fear-circuit models (amygdala-prefrontal) are well-mapped but therapeutically sterile: SSRIs and CBT are decades old, benzodiazepines are effective but addictive, and no mechanistically new anxiolytic has succeeded. The field treats the commonest disorders with the oldest tools.",
 "background": "Fear conditioning (LeDoux) provided the canonical circuit; SSRIs' anxiolytic action was discovered serendipitously. CBT/exposure works well but access is limited. Novel mechanisms (CRF antagonists, glutamate modulators) failed in trials. As of 2026 anxiety treatment is effective but stagnant: old drugs, old therapy, no new biology translated.",
 "why_it_matters": "Anxiety disables more people than any other psychiatric category: new mechanisms would help hundreds of millions stuck with partial relief or addictive drugs.",
 "sig_pointer": "The Signature system's proposed approach treats anxiety as a threat-prediction disorder, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that anxiety is a threat-prediction disorder: the brain's threat-forecasting system is miscalibrated, predicting danger where none exists - and treatment must recalibrate the forecaster, not suppress the fear. "
  "Assumptions: (1) threat prediction is a distinct computable process; (2) its miscalibration is measurable; (3) recalibration is achievable. "
  "Reasoning path: a prediction model explains why exposure works (it retrains the forecaster) and predicts forecaster-targeted drugs. "
  "Proposed mechanism: 'forecaster-recalibrated' anxiety care - interventions retraining threat prediction specifically. "
  "What would confirm it: threat-prediction measures guiding treatment and novel recalibrating drugs working. "
  "What would kill it: evidence that anxiety is purely amygdala hyperactivity with no prediction component. "
  "What this does not claim: it does not claim new treatments exist, offers no treatment advice, and does not constitute medical advice."),
 "sig_lens": "The Signature lens reads anxiety as a forecaster gone wrong, and asks what would recalibrate the predictions.",
 "how_it_works": "Researchers study anxiety circuits through threat-prediction modeling, exposure-mechanism research, and novel anxiolytic trials.",
 "key_points": [
  "Anxiety disorders affect ~300 million people.",
  "Fear circuits are well-mapped but therapeutically sterile.",
  "SSRIs and CBT are decades old; benzodiazepines are addictive.",
  "No mechanistically new anxiolytic has succeeded.",
  "Threat prediction may be the missing computational level.",
 ],
 "requirements": [
  "Measurable threat-prediction miscalibration.",
  "Forecaster-targeted drugs proven effective.",
  "An account of why circuit maps didn't yield drugs.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "LeDoux JE. The Emotional Brain. Simon & Schuster; 1996.",
  "Baxter AJ et al. Global prevalence of anxiety disorders. Psychological Medicine. 2013;43:897-910.",
  "Grupe DW, Nitschke JB. Uncertainty and anxiety. Nature Reviews Neuroscience. 2013;14:488-501.",
  "Craske MG et al. Exposure therapy mechanisms. Various; 2008-2022.",
 ],
 "demo_data": {"a": ("people with anxiety disorders, millions (approx)", 300.0),
               "b": ("millions scale", 1000.0), "bounds": (0.2, 0.4),
               "step1": "three hundred million anxious on the oldest tools in psychiatry - the commonest illness, the stalest treatments",
               "confirm": "threat-prediction measures guide treatment and recalibrating drugs work",
               "refute": "anxiety proves to be pure amygdala hyperactivity"},
},
# ------------------------------------------------------------------ rank 34
{
 "key": "consciousness-psychiatry",
 "name": "Consciousness Itself: Psychiatry's Final Frontier",
 "group": "Philosophy",
 "ladder_rank": 34, "ladder_tier": "advanced",
 "problem": "Every psychiatric symptom is a disturbance of consciousness - yet psychiatry has no theory of consciousness. Can the field that treats experience explain it?",
 "description": "Psychosis alters reality-experience; depression alters time, self, and world-experience; dissociation fragments it; mania expands it. Every psychiatric disorder is, at bottom, a disorder of consciousness - yet psychiatry borrows its consciousness theories from philosophy and neuroscience without contributing its own. The clinical phenomenology of disturbed experience is the richest consciousness data in existence, and it sits largely untheorized.",
 "background": "Phenomenological psychiatry (Jaspers, 1913; Sass, Parnas) preserved the tradition of careful experience-description. Consciousness science (Crick, Koch, Dehaene, Tononi) developed theories - global workspace, integrated information - without psychiatric input. The two literatures barely meet. As of 2026 psychiatry treats consciousness disorders without a consciousness theory.",
 "why_it_matters": "A psychiatric theory of consciousness would unify the field's fragmented disorders as disturbances of one thing - and give consciousness science its most important dataset.",
 "sig_pointer": "The Signature system's proposed approach builds consciousness theory from psychiatric phenomenology, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that psychiatric phenomenology is consciousness theory's missing dataset: the systematic ways experience breaks down reveal the structure of experience itself. "
  "Assumptions: (1) breakdown patterns reveal normal structure; (2) phenomenology is systematizable; (3) the structure yields theory. "
  "Reasoning path: a breakdown-reveals-structure model turns every disorder into a consciousness experiment, predicting a unified theory. "
  "Proposed mechanism: 'phenomenology-first' consciousness science - building theory from the systematic description of disturbed experience. "
  "What would confirm it: phenomenological patterns predicting neural and computational findings. "
  "What would kill it: evidence that phenomenology is too unreliable for theory-building. "
  "What this does not claim: it does not claim consciousness is explained, offers no clinical advice, and does not constitute medical advice."),
 "sig_lens": "The Signature lens reads every symptom as consciousness disturbed, and asks what the disturbances reveal about consciousness itself.",
 "how_it_works": "Researchers study consciousness and psychiatry through phenomenological psychopathology, consciousness-science theories, and computational modeling.",
 "key_points": [
  "Every psychiatric disorder is a disorder of experience.",
  "Psychiatry has no theory of consciousness of its own.",
  "Phenomenological psychiatry preserved experience-description.",
  "Consciousness theories developed without psychiatric input.",
  "Breakdown patterns may reveal experience's structure.",
 ],
 "requirements": [
  "Systematized phenomenology of disturbed experience.",
  "Theory predicting neural and computational findings.",
  "Unification of disorders as consciousness disturbances.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Jaspers K. General Psychopathology. 1913; English ed. 1963.",
  "Sass LA, Parnas J. Phenomenological psychiatry. Various; 2003-2017.",
  "Tononi G et al. Integrated information theory. Various; 2004-2016.",
  "Dehaene S et al. Global workspace theory. Various; 1998-2017.",
 ],
 "demo_data": {"a": ("psychiatric disorders that are consciousness disturbances (approx)", 15.0),
               "b": ("major psychiatric disorders (approx)", 15.0), "bounds": (0.9, 1.1),
               "step1": "every major disorder disturbs experience - yet the field has no theory of the thing it treats",
               "confirm": "phenomenological patterns predict neural and computational findings",
               "refute": "phenomenology proves too unreliable for theory-building"},
},
]
