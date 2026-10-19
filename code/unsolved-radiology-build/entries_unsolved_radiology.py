#!/usr/bin/env python3
"""Entries for The Unsolved Radiology Database (unsolved-radiology) and its
Signature half (unsolved-radiology-signature).

34 famous unsolved problems in radiology, ladder-ordered by accessibility
(rank 1 = most approachable, rank 34 = most complex/compounded).
Public half: real, fact-checked problems. Signature half: the same 34
problems through the Signature lens, with Signature-generated proposed
solutions that are ALWAYS labeled as proposals, never established science.

Honesty rule (enforced in every record): never claim proof, never imply
peer acceptance, never present speculation as settled. Signature proposals
are labeled speculation for research discussion only - never medical advice,
never a diagnostic or treatment recommendation; no cure claims.
"""

LABEL = "Signature-generated proposed solution \u2014 not established science."

SIG_TAIL = ("Signature editions carry the Signature system's proposed "
            "solution approaches to famous unsolved problems. Every "
            "solution is labeled a Signature-generated proposal, never "
            "established science, never peer-accepted, never proof, never "
            "medical advice.")

STD_COMMON = [
    "Problem statements verified against the published radiology literature; open status confirmed as of 2026.",
    "Signature solution sections are labeled proposals: they state assumptions, a reasoning path, a proposed mechanism, what would confirm or kill them, and what they do not claim.",
    "Signature proposals are labeled speculation for research discussion only - never medical advice, never a diagnostic or treatment recommendation; no cure claims appear.",
]

ENTRIES = [
# ------------------------------------------------------------------ rank 1
{
 "key": "radiation-dose",
 "name": "Low-Dose Radiation Risk: The LNT Debate",
 "group": "Radiation Safety",
 "ladder_rank": 1, "ladder_tier": "foundations",
 "problem": "Does low-dose medical radiation cause cancer? The linear no-threshold model says any dose carries risk - but the evidence at CT-level doses is fiercely contested.",
 "description": "The linear no-threshold (LNT) model - any radiation dose, however small, carries proportional cancer risk - underpins all radiation protection. But at medical-imaging doses (CT scans), epidemiology is underpowered: the projected risks are tiny, confounded, and possibly zero (hormesis proponents) or underestimated. The field cannot measure what it regulates.",
 "background": "LNT was adopted from high-dose atomic-bomb data extrapolated downward (BEIR reports). CT dose concerns exploded in the 2000s (Brenner). The Image Gently/Wisely campaigns pushed dose reduction. But direct evidence of CT-level carcinogenesis remains contested; the Australian CT cohort study suggested small risks. As of 2026 LNT rules regulation while the science at low doses is unresolved.",
 "why_it_matters": "LNT drives billions in shielding, dose-reduction technology, and scan-avoidance decisions: if low doses are harmless, the costs are wasted; if harmful, current practice needs tightening.",
 "sig_pointer": "The Signature system's proposed approach treats low-dose risk as a measurement problem, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that the LNT debate is unresolvable by epidemiology at current sample sizes: the projected effect is smaller than confounding, and only mechanistic biomarkers of radiation damage can settle it. "
  "Assumptions: (1) epidemiology is underpowered at these doses; (2) damage biomarkers exist; (3) they are scalable. "
  "Reasoning path: a measurement model explains decades of stalemate and predicts biomarker-based risk assessment. "
  "Proposed mechanism: 'biomarker-resolved' low-dose risk - measuring actual cellular damage per dose instead of extrapolating. "
  "What would confirm it: damage biomarkers showing dose-response at CT doses. "
  "What would kill it: evidence that no measurable damage occurs at these doses. "
  "What this does not claim: it does not claim low doses are safe or harmful, offers no medical advice, and does not constitute a radiation-safety recommendation."),
 "sig_lens": "The Signature lens reads the LNT stalemate as unmeasurable risk, and asks what biomarkers would measure.",
 "how_it_works": "Researchers study low-dose risk through cohort studies, BEIR modeling, and DNA-damage biomarker research.",
 "key_points": [
  "LNT is extrapolated from high-dose atomic-bomb data.",
  "CT-level epidemiology is underpowered and confounded.",
  "Image Gently/Wisely pushed dose reduction regardless.",
  "Hormesis proponents argue low doses may be harmless.",
  "Regulation outruns the evidence.",
 ],
 "requirements": [
  "Scalable biomarkers of low-dose damage.",
  "Dose-response measured, not extrapolated.",
  "Regulation matched to measured risk.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "National Research Council. BEIR VII report. 2006.",
  "Brenner DJ et al. CT radiation dose concerns. Various; 2001-2007.",
  "Mathews JD et al. Australian CT cohort study. BMJ. 2013;346:f2360.",
  "Image Gently / Image Wisely campaigns. Various; 2007 onward.",
 ],
 "demo_data": {"a": ("projected cancers per 10,000 pediatric CTs (approx)", 1.0),
               "b": ("CTs per 10,000 (scale)", 10000.0), "bounds": (0.00005, 0.0002),
               "step1": "one projected cancer per ten thousand scans - a risk too small to measure, too big to ignore",
               "confirm": "damage biomarkers show dose-response at CT doses",
               "refute": "no measurable damage proves to occur at these doses"},
},
# ------------------------------------------------------------------ rank 2
{
 "key": "incidentalomas",
 "name": "Incidentalomas: What To Do With Incidental Findings",
 "group": "Practice",
 "ladder_rank": 2, "ladder_tier": "foundations",
 "problem": "Scans find harmless-looking nodules everywhere - but which incidentalomas matter? The cascade of follow-ups harms more than it helps.",
 "description": "Incidental findings - thyroid nodules, adrenal masses, pulmonary nodules found by accident - are ubiquitous in modern imaging. Most are benign; workups cause anxiety, cost, radiation, and occasional harm. Guidelines (Fleischner for lung nodules, ACR white papers) try to standardize management, but the evidence base for most incidentaloma pathways is thin.",
 "background": "Incidentaloma prevalence rose with CT/MRI volume in the 2000s; the term itself dates to radiology's early days. Fleischner Society guidelines (2005, updated 2017) brought order to lung nodules; ACR white papers covered other organs. But overdiagnosis concerns persist: many worked-up lesions would never have harmed. As of 2026 management is guideline-driven but evidence-thin.",
 "why_it_matters": "Incidentalomas trigger millions of follow-ups yearly: better management would cut costs, anxiety, and iatrogenic harm.",
 "sig_pointer": "The Signature system's proposed approach treats incidentalomas as a risk-stratification problem, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that incidentaloma management needs individualized risk stratification: nodule characteristics plus patient context predicting which lesions warrant workup - replacing one-size-fits-all size thresholds. "
  "Assumptions: (1) risk is predictable; (2) stratification beats thresholds; (3) it is implementable. "
  "Reasoning path: a stratification model explains guideline limitations and predicts precision incidentaloma management. "
  "Proposed mechanism: 'risk-stratified' incidentaloma pathways - workup intensity matched to predicted risk. "
  "What would confirm it: stratified pathways reducing workups without missing disease. "
  "What would kill it: evidence that incidental cancers are unpredictable. "
  "What this does not claim: it does not claim any finding is benign, offers no medical advice, and does not constitute a management recommendation."),
 "sig_lens": "The Signature lens reads the incidentaloma cascade as unstratified risk, and asks what prediction would target.",
 "how_it_works": "Researchers study incidentalomas through prevalence studies, Fleischner/ACR guideline development, and overdiagnosis research.",
 "key_points": [
  "Incidental findings are ubiquitous in modern imaging.",
  "Most are benign; workups cause cost and anxiety.",
  "Fleischner and ACR guidelines standardize management.",
  "The evidence base for pathways is thin.",
  "Overdiagnosis is a real concern.",
 ],
 "requirements": [
  "Individualized risk-stratification models.",
  "Proof that stratification reduces harm.",
  "Evidence-based pathways for all common incidentalomas.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "MacMahon H et al. Fleischner Society lung nodule guidelines. Radiology. 2017;284:228-243.",
  "Berland LL et al. ACR incidental findings white papers. Various; 2010-2017.",
  "Lumbreras B et al. Incidentaloma prevalence reviews. Various; 2010-2016.",
  "O'Sullivan JW et al. Overdiagnosis in imaging. Various; 2018-2020.",
 ],
 "demo_data": {"a": ("CT scans with incidental findings, percent (approx)", 40.0),
               "b": ("percent scale", 100.0), "bounds": (0.3, 0.52),
               "step1": "two in five scans find something unexpected - mostly benign, always costly",
               "confirm": "stratified pathways reduce workups without missing disease",
               "refute": "incidental cancers prove unpredictable"},
},
# ------------------------------------------------------------------ rank 3
{
 "key": "ai-radiology",
 "name": "AI in Radiology: When Will It Be Trustworthy?",
 "group": "Artificial Intelligence",
 "ladder_rank": 3, "ladder_tier": "foundations",
 "problem": "AI matches radiologists on narrow tasks - yet deployment is slow, errors are unpredictable, and liability is unresolved. What blocks trustworthy AI?",
 "description": "Deep-learning models match or exceed radiologists on specific tasks (mammography, chest X-ray triage, stroke detection) in retrospective studies. But prospective deployment lags: distribution shift degrades performance, errors are alien (confident mistakes on obvious cases), and no framework assigns liability for AI misses. The field has impressive demos and thin clinical integration.",
 "background": "The deep-learning wave hit radiology in the mid-2010s (Esteva, Gulshan); FDA cleared dozens of AI tools. Prospective trials (McKinney mammography, 2020) showed promise; real-world studies showed degradation. As of 2026 AI assists radiologists in pockets but hasn't transformed the specialty.",
 "why_it_matters": "Radiologist shortages are global: trustworthy AI would extend expert interpretation everywhere - untrustworthy AI would systematize error at scale.",
 "sig_pointer": "The Signature system's proposed approach treats AI trust as a calibration problem, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that radiology AI needs calibrated uncertainty: models that know when they're uncertain and defer to humans - making the human-AI team the product, not the model alone. "
  "Assumptions: (1) uncertainty is calibratable; (2) deferral protocols work; (3) teams beat either alone. "
  "Reasoning path: a calibration model explains deployment failures and predicts trusted human-AI systems. "
  "Proposed mechanism: 'calibrated-deferral' AI deployment - AI handling confident cases, deferring uncertain ones. "
  "What would confirm it: calibrated teams outperforming radiologists alone in prospective trials. "
  "What would kill it: evidence that AI uncertainty can't be calibrated reliably. "
  "What this does not claim: it does not claim AI is ready, offers no medical advice, and does not constitute a deployment recommendation."),
 "sig_lens": "The Signature lens reads the AI stalemate as uncalibrated confidence, and asks what deferral would fix.",
 "how_it_works": "Researchers study radiology AI through prospective trials, distribution-shift research, and uncertainty-calibration work.",
 "key_points": [
  "AI matches radiologists on narrow retrospective tasks.",
  "Prospective performance degrades with distribution shift.",
  "AI errors are alien and unpredictable.",
  "Liability for AI misses is unresolved.",
  "Clinical integration remains thin.",
 ],
 "requirements": [
  "Calibrated uncertainty quantification.",
  "Prospective proof of human-AI team superiority.",
  "Liability frameworks for AI-assisted reads.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "McKinney SM et al. Mammography AI. Nature. 2020;577:89-94.",
  "Gulshan V et al. Diabetic retinopathy AI. JAMA. 2016;316:2402-2410.",
  "Topol EJ. AI in radiology reviews. Various; 2019-2023.",
  "FDA. Cleared radiology AI devices listings. 2018 onward.",
 ],
 "demo_data": {"a": ("FDA-cleared radiology AI tools (approx)", 200.0),
               "b": ("radiology practices using AI routinely (percent approx)", 30.0), "bounds": (4.0, 10.0),
               "step1": "two hundred cleared tools against a third of practices using them - the deployment gap",
               "confirm": "calibrated teams beat radiologists alone prospectively",
               "refute": "AI uncertainty proves uncalibratable"},
},
# ------------------------------------------------------------------ rank 4
{
 "key": "contrast-safety",
 "name": "Contrast Agent Safety: Gadolinium and Kidneys",
 "group": "Contrast Media",
 "ladder_rank": 4, "ladder_tier": "foundations",
 "problem": "Gadolinium deposits in the brain; iodinated contrast injures kidneys - how safe are contrast agents, really?",
 "description": "Gadolinium-based contrast agents (GBCAs) - essential for MRI - were found to deposit in brain tissue (Kanda, 2014), with unknown clinical significance; nephrogenic systemic fibrosis (NSF) was the earlier scare, controlled by screening. Iodinated contrast's kidney injury (contrast-induced nephropathy) is debated - recent studies suggest the risk was overstated. The field balances real diagnostic value against uncertain harms.",
 "background": "NSF (2006) led to renal screening and safer agents; gadolinium deposition (2014) triggered new concern and macrocyclic-agent shifts. Contrast-nephropathy research (McDonald, Davenport, 2010s) suggested much of the risk was confounding by the underlying illness. As of 2026 both debates are unsettled with practice erring cautious.",
 "why_it_matters": "Contrast enables millions of diagnoses yearly: overestimating harm denies needed scans; underestimating it causes injury.",
 "sig_pointer": "The Signature system's proposed approach measures contrast harms directly, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that contrast safety needs direct harm measurement: gadolinium's clinical significance tested prospectively, and kidney injury separated from underlying illness by design. "
  "Assumptions: (1) harms are measurable; (2) confounding is separable; (3) measurement settles practice. "
  "Reasoning path: a measurement model explains the persistent uncertainty and predicts evidence-based contrast protocols. "
  "Proposed mechanism: 'harm-measured' contrast practice - protocols based on measured rather than feared harms. "
  "What would confirm it: prospective studies quantifying true harm rates. "
  "What would kill it: evidence that harms are too rare or subtle to measure. "
  "What this does not claim: it does not claim contrast is safe or harmful, offers no medical advice, and does not constitute a safety recommendation."),
 "sig_lens": "The Signature lens reads the contrast debates as unmeasured harm, and asks what direct measurement would show.",
 "how_it_works": "Researchers study contrast safety through deposition studies, NSF surveillance, and nephropathy re-analyses.",
 "key_points": [
  "Gadolinium deposits in brain tissue; significance unknown.",
  "NSF was controlled by renal screening.",
  "Contrast-nephropathy risk may have been overstated.",
  "Macrocyclic agents replaced linear ones.",
  "Practice errs cautious on thin evidence.",
 ],
 "requirements": [
  "Prospective gadolinium harm quantification.",
  "Unconfounded kidney-injury estimates.",
  "Protocols matched to measured harms.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Kanda T et al. Gadolinium deposition in brain. Radiology. 2014;270:834-841.",
  "McDonald RJ et al. Contrast nephropathy re-analyses. Various; 2013-2017.",
  "Davenport MS et al. Contrast safety reviews. Various; 2015-2020.",
  "ACR. Manual on Contrast Media. Updated regularly.",
 ],
 "demo_data": {"a": ("MRI scans using gadolinium yearly, millions (approx)", 30.0),
               "b": ("millions scale", 100.0), "bounds": (0.2, 0.42),
               "step1": "thirty million gadolinium doses yearly with unknown brain significance - the scale of the uncertainty",
               "confirm": "prospective studies quantify true harm rates",
               "refute": "harms prove too rare or subtle to measure"},
},
# ------------------------------------------------------------------ rank 5
{
 "key": "mammography",
 "name": "Mammography: Screening Benefit Versus Overdiagnosis",
 "group": "Screening",
 "ladder_rank": 5, "ladder_tier": "foundations",
 "problem": "Mammography saves lives and causes overdiagnosis - what is the true balance, and who should be screened?",
 "description": "Mammographic screening reduces breast-cancer mortality (~20% relative) but causes overdiagnosis - detecting cancers that would never harm (estimates 10-30% of screen-detected). The field debates start age, interval, and whether the mortality benefit justifies the harms. Dense-breast supplemental screening adds another unresolved layer.",
 "background": "RCTs (HIP, Swedish trials) established the mortality benefit; overdiagnosis estimates came from modeling and long-term follow-up. The 2009 USPSTF controversy (start at 50 vs 40) politicized the balance. Digital breast tomosynthesis improved detection. As of 2026 guidelines vary by country with no consensus balance.",
 "why_it_matters": "Mammography screens hundreds of millions: the benefit-harm balance determines policy for half the population.",
 "sig_pointer": "The Signature system's proposed approach personalizes screening by risk, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that mammography's balance is individual: risk-stratified screening - intensity matched to personal risk - maximizing benefit while minimizing overdiagnosis. "
  "Assumptions: (1) risk is predictable; (2) stratification beats age-based rules; (3) it is implementable. "
  "Reasoning path: a stratification model explains why one-size-fits-all is contested and predicts risk-based screening. "
  "Proposed mechanism: 'risk-stratified' breast screening - personalized start age, interval, and modality. "
  "What would confirm it: stratified programs beating age-based ones on benefit-harm balance. "
  "What would kill it: evidence that risk prediction adds nothing to age. "
  "What this does not claim: it does not claim any screening schedule is correct, offers no medical advice, and does not constitute a screening recommendation."),
 "sig_lens": "The Signature lens reads the screening war as one-size-fits-all, and asks what risk stratification would settle.",
 "how_it_works": "Researchers study mammography through screening RCTs, overdiagnosis modeling, and risk-prediction research.",
 "key_points": [
  "Mammography reduces breast-cancer mortality ~20% relatively.",
  "Overdiagnosis estimates run 10-30% of screen-detected cancers.",
  "Guidelines vary by country on start age and interval.",
  "Dense breasts need supplemental screening (unresolved how).",
  "Tomosynthesis improved detection without settling the balance.",
 ],
 "requirements": [
  "Validated risk-stratification models.",
  "Stratified screening proven superior.",
  "Overdiagnosis quantified, not modeled.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Independent UK Panel on Breast Cancer Screening. Lancet. 2012;380:1778-1786.",
  "USPSTF. Breast cancer screening recommendations. Various; 2009-2024.",
  "Paci E et al. Overdiagnosis estimates. Various; 2013-2019.",
  "Skaane P et al. Tomosynthesis trials. Various; 2013-2019.",
 ],
 "demo_data": {"a": ("screen-detected cancers overdiagnosed, percent (approx)", 20.0),
               "b": ("percent scale", 100.0), "bounds": (0.12, 0.3),
               "step1": "a fifth of found cancers may never have harmed - the harm inside the benefit",
               "confirm": "stratified programs beat age-based ones on benefit-harm balance",
               "refute": "risk prediction proves to add nothing to age"},
},
# ------------------------------------------------------------------ rank 6
{
 "key": "lung-screening",
 "name": "Lung Cancer Screening: Who Benefits?",
 "group": "Screening",
 "ladder_rank": 6, "ladder_tier": "foundations",
 "problem": "Low-dose CT screening cuts lung-cancer mortality - but uptake is dismal and eligibility criteria miss many cancers. How should screening work?",
 "description": "The NLST (2011) and NELSON (2020) trials proved low-dose CT screening reduces lung-cancer mortality ~20-25% in heavy smokers. But uptake is ~5-15%, eligibility (pack-years, age) excludes many who develop cancer, and false positives burden programs. Risk-model-based eligibility (PLCOm2012) outperforms pack-year rules but isn't widely adopted.",
 "background": "NLST established efficacy; USPSTF set eligibility (2013, expanded 2021). Implementation lagged: stigma, access, and primary-care gaps. NELSON confirmed European efficacy. Risk models promised better selection. As of 2026 screening works in trials and fails in practice.",
 "why_it_matters": "Lung cancer is the top cancer killer: screening's trial efficacy is wasted by implementation failure.",
 "sig_pointer": "The Signature system's proposed approach replaces pack-years with risk models, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that lung screening eligibility should be risk-model-based: selecting by predicted risk rather than crude pack-year cutoffs - catching the missed cancers and sparing the low-risk. "
  "Assumptions: (1) risk models outperform cutoffs; (2) they are implementable; (3) uptake barriers are addressable. "
  "Reasoning path: a risk-model approach explains the eligibility gap and predicts efficient screening. "
  "Proposed mechanism: 'risk-based' lung screening - model-selected eligibility with outreach. "
  "What would confirm it: risk-based programs catching more cancers per scan. "
  "What would kill it: evidence that models don't beat cutoffs prospectively. "
  "What this does not claim: it does not claim any eligibility rule is correct, offers no medical advice, and does not constitute a screening recommendation."),
 "sig_lens": "The Signature lens reads the screening gap as crude selection, and asks what risk models would catch.",
 "how_it_works": "Researchers study lung screening through NLST/NELSON follow-ups, risk-model validation, and implementation research.",
 "key_points": [
  "NLST/NELSON proved ~20-25% mortality reduction.",
  "Uptake is only 5-15% of the eligible.",
  "Pack-year cutoffs miss many cancers.",
  "Risk models outperform cutoffs but aren't adopted.",
  "Screening works in trials, fails in practice.",
 ],
 "requirements": [
  "Prospective proof of risk-model superiority.",
  "Uptake interventions that work.",
  "Implementation matching trial efficacy.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Aberle DR et al. NLST. NEJM. 2011;365:395-409.",
  "de Koning HJ et al. NELSON trial. NEJM. 2020;382:503-513.",
  "Tammemagi MC et al. PLCOm2012 risk model. Various; 2013-2019.",
  "USPSTF. Lung cancer screening recommendations. 2021.",
 ],
 "demo_data": {"a": ("eligible smokers screened, percent (approx)", 10.0),
               "b": ("percent scale", 100.0), "bounds": (0.05, 0.18),
               "step1": "one in ten eligible gets screened - the proven lifesaver almost nobody uses",
               "confirm": "risk-based programs catch more cancers per scan",
               "refute": "models prove not to beat cutoffs prospectively"},
},
# ------------------------------------------------------------------ rank 7
{
 "key": "interobserver",
 "name": "Radiologist Disagreement: The Variability Problem",
 "group": "Practice",
 "ladder_rank": 7, "ladder_tier": "foundations",
 "problem": "Two radiologists reading the same scan often disagree - how much variability is acceptable, and what reduces it?",
 "description": "Interobserver variability - disagreement between readers - is substantial in radiology: BI-RADS assessments, lung-nodule calls, fracture detection all show meaningful discordance. Some variability is irreducible (genuine ambiguity); some reflects training, fatigue, and context. The field lacks agreed variability targets and proven reduction methods.",
 "background": "Variability was quantified across modalities in the 2000s-2010s; double-reading in mammography showed the cost of discordance. Structured reporting, second reads, and AI assistance each promise reduction. As of 2026 variability is measured but not managed: no specialty-wide standards exist.",
 "why_it_matters": "Disagreement means different patients get different care from the same scan: reducing variability is quality's low-hanging fruit.",
 "sig_pointer": "The Signature system's proposed approach treats variability as a system to be engineered, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that variability should be engineered down: measuring each reader's discordance profile, targeting the reducible portion (fatigue, context, training gaps), and accepting the irreducible. "
  "Assumptions: (1) variability decomposes into reducible and irreducible; (2) the reducible part is large; (3) feedback reduces it. "
  "Reasoning path: a decomposition model explains persistent variability and predicts engineered reduction. "
  "Proposed mechanism: 'variability-engineered' practice - discordance feedback loops for every reader. "
  "What would confirm it: feedback systems reducing discordance in trials. "
  "What would kill it: evidence that variability is mostly irreducible ambiguity. "
  "What this does not claim: it does not claim any read is correct, offers no medical advice, and does not constitute a quality recommendation."),
 "sig_lens": "The Signature lens reads disagreement as engineerable, and asks what feedback would reduce it.",
 "how_it_works": "Researchers study variability through reader studies, double-reading trials, and structured-reporting evaluations.",
 "key_points": [
  "Interobserver disagreement is substantial across modalities.",
  "Some variability is genuine ambiguity; some is reducible.",
  "Double reading catches discordance at a cost.",
  "No specialty-wide variability standards exist.",
  "Feedback loops are largely absent.",
 ],
 "requirements": [
  "Decomposed reducible versus irreducible variability.",
  "Feedback systems proven to reduce discordance.",
  "Agreed variability targets.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Elmore JG et al. Variability in mammography interpretation. Various; 2002-2015.",
  "Bankier AA et al. Reader variability reviews. Various; 2010-2018.",
  "Taylor P et al. Double reading evaluations. Various; 2005-2015.",
  "Lehman CD et al. Structured reporting. Various; 2016-2021.",
 ],
 "demo_data": {"a": ("mammography reader discordance, percent (approx)", 15.0),
               "b": ("percent scale", 100.0), "bounds": (0.08, 0.25),
               "step1": "readers disagree on one in seven mammograms - the same scan, different care",
               "confirm": "feedback systems reduce discordance in trials",
               "refute": "variability proves mostly irreducible"},
},
# ------------------------------------------------------------------ rank 8
{
 "key": "dose-optimization",
 "name": "Dose Optimization: How Low Can We Go?",
 "group": "Radiation Safety",
 "ladder_rank": 8, "ladder_tier": "foundations",
 "problem": "CT doses have fallen dramatically - but how low can dose go before diagnostic accuracy suffers? The limit is unknown.",
 "description": "CT dose-reduction technologies (iterative reconstruction, photon-counting detectors) keep lowering doses - but each reduction trades against image noise and potentially missed findings. The minimum dose for each clinical task is undefined; protocols vary wildly between institutions for identical indications.",
 "background": "ALARA guided dose practice; iterative reconstruction (2010s) cut doses substantially; photon-counting CT (2020s) promises another leap. But task-specific minimum doses were never established - the field reduced doses without defining the floor. As of 2026 identical scans use wildly different doses across hospitals.",
 "why_it_matters": "Defining minimum doses would standardize safety: patients at high-dose centers get unnecessary radiation; at ultra-low-dose centers, missed diagnoses.",
 "sig_pointer": "The Signature system's proposed approach defines task-specific minimum doses, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that minimum doses are task-specific and measurable: for each clinical question, the dose below which accuracy degrades - establishing evidence-based dose floors. "
  "Assumptions: (1) task-specific minima exist; (2) they are measurable; (3) standardization is achievable. "
  "Reasoning path: a task-specific model explains protocol variation and predicts optimized dose standards. "
  "Proposed mechanism: 'task-defined' dose floors - minimum doses per clinical indication. "
  "What would confirm it: measured minima standardizing practice without accuracy loss. "
  "What would kill it: evidence that minima vary too much between patients for standards. "
  "What this does not claim: it does not claim any dose is safe, offers no medical advice, and does not constitute a dosing recommendation."),
 "sig_lens": "The Signature lens reads dose variation as undefined floors, and asks what measurement would set them.",
 "how_it_works": "Researchers study dose optimization through phantom studies, task-based image-quality research, and protocol audits.",
 "key_points": [
  "CT doses vary wildly between institutions.",
  "Task-specific minimum doses were never established.",
  "Iterative reconstruction and photon-counting keep lowering doses.",
  "Each reduction trades against noise and missed findings.",
  "ALARA guides without defining the floor.",
 ],
 "requirements": [
  "Measured task-specific minimum doses.",
  "Standardized protocols per indication.",
  "Proof that floors don't cost accuracy.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "McCollough CH et al. CT dose reduction technologies. Various; 2009-2015.",
  "Smith-Bindman R et al. CT dose variation studies. Various; 2009-2019.",
  "Flohr T et al. Photon-counting CT. Various; 2020-2024.",
  "AAPM. Task-based image quality reports. Various.",
 ],
 "demo_data": {"a": ("dose variation between centers for identical scans, fold (approx)", 5.0),
               "b": ("fold scale", 10.0), "bounds": (0.3, 0.7),
               "step1": "five-fold dose differences for the same scan - without anyone knowing the right dose",
               "confirm": "measured minima standardize practice without accuracy loss",
               "refute": "minima prove too patient-variable for standards"},
},
# ------------------------------------------------------------------ rank 9
{
 "key": "ultrasound-operator",
 "name": "Ultrasound's Operator Dependence",
 "group": "Modalities",
 "ladder_rank": 9, "ladder_tier": "foundations",
 "problem": "Ultrasound is cheap, safe, and portable - but its accuracy depends entirely on the operator's hands. Can the dependence be engineered away?",
 "description": "Ultrasound - radiation-free, inexpensive, bedside - is the most operator-dependent modality: image quality and diagnostic accuracy vary enormously with skill. This limits its use where it's needed most (low-resource settings, point-of-care). Automated acquisition, AI guidance, and standardized protocols promise to close the gap.",
 "background": "Point-of-care ultrasound (POCUS) exploded in the 2010s; the operator-dependence problem became its binding constraint. AI-guided acquisition (Kassam, 2020s) showed novices achieving expert-quality images. As of 2026 automation is promising but not standard.",
 "why_it_matters": "De-skilled ultrasound would bring diagnostics to billions without imaging access: the operator gap is global health's imaging bottleneck.",
 "sig_pointer": "The Signature system's proposed approach automates acquisition guidance, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that AI-guided acquisition can de-skill ultrasound: real-time guidance directing probe placement until the image meets diagnostic quality - making the operator's hands assisted, not expert. "
  "Assumptions: (1) guidance algorithms generalize; (2) novices plus guidance match experts; (3) it is deployable cheaply. "
  "Reasoning path: a guidance model explains the skill gap and predicts democratized ultrasound. "
  "Proposed mechanism: 'guidance-assisted' ultrasound - AI directing every acquisition. "
  "What would confirm it: novices with guidance matching experts in trials. "
  "What would kill it: evidence that probe skill resists guidance. "
  "What this does not claim: it does not claim automated ultrasound exists, offers no medical advice, and does not constitute a device recommendation."),
 "sig_lens": "The Signature lens reads the skill gap as guidable, and asks what assistance would close it.",
 "how_it_works": "Researchers study operator dependence through POCUS training trials, AI-guidance studies, and image-quality research.",
 "key_points": [
  "Ultrasound accuracy varies enormously with operator skill.",
  "POCUS expansion made the dependence the binding constraint.",
  "AI-guided acquisition shows novice-to-expert promise.",
  "Low-resource settings need it most.",
  "Automation is promising but not standard.",
 ],
 "requirements": [
  "Guidance algorithms proven across anatomies.",
  "Novice-plus-guidance matching experts.",
  "Cheap deployable implementations.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Moore CL, Copel JA. POCUS reviews. Various; 2011-2020.",
  "Kassam N et al. AI-guided ultrasound acquisition. Various; 2020-2023.",
  "Narayanasamy S et al. Operator dependence studies. Various; 2016-2021.",
  "WHO. Ultrasound access reports. Various.",
 ],
 "demo_data": {"a": ("ultrasound accuracy gap novice vs expert, percent (approx)", 30.0),
               "b": ("percent scale", 100.0), "bounds": (0.2, 0.42),
               "step1": "novices miss nearly a third more - the skill gap blocking global access",
               "confirm": "novices with guidance match experts in trials",
               "refute": "probe skill proves resistant to guidance"},
},
# ------------------------------------------------------------------ rank 10
{
 "key": "mri-access",
 "name": "MRI Access: The World's Most Unequal Modality",
 "group": "Access",
 "ladder_rank": 10, "ladder_tier": "foundations",
 "problem": "MRI is the best diagnostic tool for countless conditions - and unavailable to most of humanity. Can low-field portable MRI close the gap?",
 "description": "MRI access is brutally unequal: high-income countries have dozens of scanners per million; low-income countries have near zero. Conventional MRI needs helium, shielding, and infrastructure. Low-field portable systems (Hyperfine, 2020s) promise bedside brain imaging at a fraction of the cost - but image quality and clinical validation are early.",
 "background": "MRI's infrastructure demands entrenched the inequality for decades. Low-field research (Sarracanie, Wald) revived in the 2010s; Hyperfine's Swoop got FDA clearance (2020). Validation studies are accumulating. As of 2026 portable MRI is proven feasible with unclear clinical scope.",
 "why_it_matters": "Closing the MRI gap would bring the best neuroimaging to billions: the most consequential equity problem in radiology.",
 "sig_pointer": "The Signature system's proposed approach defines portable MRI's clinical scope, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that portable MRI needs scope definition: identifying the clinical questions low-field answers well - rather than comparing it to high-field on high-field's terms. "
  "Assumptions: (1) a real clinical scope exists; (2) it is definable; (3) scope-matched deployment works. "
  "Reasoning path: a scope model explains slow adoption and predicts targeted deployment. "
  "Proposed mechanism: 'scope-defined' portable MRI - deployment matched to validated indications. "
  "What would confirm it: scope-matched portable MRI improving outcomes where no MRI existed. "
  "What would kill it: evidence that low-field quality is clinically insufficient. "
  "What this does not claim: it does not claim portable MRI equals high-field, offers no medical advice, and does not constitute a device recommendation."),
 "sig_lens": "The Signature lens reads the access gap as a scope question, and asks what low-field answers well.",
 "how_it_works": "Researchers study MRI access through low-field validation trials, cost-effectiveness research, and deployment studies.",
 "key_points": [
  "MRI density varies 100-fold between rich and poor countries.",
  "Conventional MRI needs helium and shielding.",
  "Portable low-field systems got FDA clearance (2020).",
  "Image quality and clinical scope are early-stage.",
  "The equity gap is radiology's largest.",
 ],
 "requirements": [
  "Validated clinical scope for low-field MRI.",
  "Outcome proof in no-MRI settings.",
  "Affordable scalable deployment.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Sarracanie M et al. Low-field MRI. Various; 2015-2020.",
  "Hyperfine. Swoop system FDA clearance. 2020.",
  "Wald LL et al. Portable MRI reviews. Various; 2020-2023.",
  "Geethanath S, Vaughan JT. Accessible MRI. Various; 2019-2022.",
 ],
 "demo_data": {"a": ("MRI scanners per million, low-income countries (approx)", 0.5),
               "b": ("MRI scanners per million, high-income (approx)", 40.0), "bounds": (0.005, 0.02),
               "step1": "eighty-fold fewer scanners where they're needed most - the steepest inequality in medicine",
               "confirm": "scope-matched portable MRI improves outcomes where no MRI existed",
               "refute": "low-field quality proves clinically insufficient"},
},
# ------------------------------------------------------------------ rank 11
{
 "key": "teleradiology",
 "name": "Teleradiology Quality at Scale",
 "group": "Practice",
 "ladder_rank": 11, "ladder_tier": "foundations",
 "problem": "Teleradiology covers night shifts worldwide - but does remote reading match on-site quality, and what gets lost?",
 "description": "Teleradiology - remote image interpretation - is now essential infrastructure: night coverage, subspecialty access, global outsourcing. But quality concerns persist: lack of clinical context, communication gaps with referrers, and the commoditization pressure of high-volume reading. The field hasn't defined quality standards for remote reads.",
 "background": "Teleradiology grew in the 2000s with PACS and broadband; night-hawk services became standard. Quality studies show comparable accuracy with context loss. Commoditization concerns (radiology as piecework) grew in the 2010s. As of 2026 teleradiology is indispensable and under-standardized.",
 "why_it_matters": "Teleradiology reads millions of studies yearly: quality standards would protect patients in the most industrialized corner of radiology.",
 "sig_pointer": "The Signature system's proposed approach defines remote-read quality standards, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that teleradiology needs context engineering: structured clinical context, referrer communication protocols, and quality metrics specific to remote reading. "
  "Assumptions: (1) context loss is the main quality gap; (2) it is engineerable; (3) standards are enforceable. "
  "Reasoning path: a context model explains quality concerns and predicts standardized remote practice. "
  "Proposed mechanism: 'context-engineered' teleradiology - mandatory context protocols and remote-specific quality metrics. "
  "What would confirm it: engineered-context remote reads matching on-site quality. "
  "What would kill it: evidence that remote reading is inherently lower quality. "
  "What this does not claim: it does not claim teleradiology is unsafe, offers no medical advice, and does not constitute a practice recommendation."),
 "sig_lens": "The Signature lens reads the quality gap as missing context, and asks what protocols would supply it.",
 "how_it_works": "Researchers study teleradiology through accuracy comparisons, context-effect studies, and commoditization analyses.",
 "key_points": [
  "Teleradiology is essential night and subspecialty infrastructure.",
  "Clinical context is often missing in remote reads.",
  "Accuracy is comparable but communication suffers.",
  "Commoditization pressures high-volume reading.",
  "No remote-specific quality standards exist.",
 ],
 "requirements": [
  "Mandatory context protocols.",
  "Remote-specific quality metrics.",
  "Proof that engineered context closes the gap.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Wachter RM. Teleradiology analyses. Various; 2006-2015.",
  "Krupinski EA et al. Teleradiology quality studies. Various; 2007-2016.",
  "Boland GW et al. Teleradiology practice reviews. Various; 2010-2018.",
  "ACR. Teleradiology practice parameters. Various.",
 ],
 "demo_data": {"a": ("studies read remotely at night, percent of US hospitals (approx)", 70.0),
               "b": ("percent scale", 100.0), "bounds": (0.55, 0.85),
               "step1": "seven in ten hospitals read nights remotely - essential infrastructure without quality standards",
               "confirm": "engineered-context remote reads match on-site quality",
               "refute": "remote reading proves inherently lower quality"},
},
# ------------------------------------------------------------------ rank 12
{
 "key": "radiology-burnout",
 "name": "Radiologist Burnout and the Reading Burden",
 "group": "Workforce",
 "ladder_rank": 12, "ladder_tier": "compounded",
 "problem": "Imaging volumes grow 5-10% yearly while radiologist numbers stagnate - how does the specialty survive its own success?",
 "description": "Radiology faces a workload crisis: CT/MRI volumes compound yearly, studies grow more complex (thinner slices, more sequences), and reimbursement pressures demand speed. Burnout rates are among medicine's highest; errors rise with fatigue and interruption. The specialty that images everything can't staff its own demand.",
 "background": "Volume growth outpaced training for two decades; the 2000s-2010s saw reading-room industrialization. Burnout studies (Harolds, 2010s) quantified the crisis. AI was promised as relief but added work (AI oversight). As of 2026 the workload curve steepens with no staffing solution.",
 "why_it_matters": "Burned-out radiologists miss findings: the workload crisis is a patient-safety crisis wearing a workforce costume.",
 "sig_pointer": "The Signature system's proposed approach treats workload as a systems-engineering problem, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that radiology workload needs systems engineering: study triage by complexity, interruption-free reading blocks, and AI that reduces rather than adds work. "
  "Assumptions: (1) workload is engineerable; (2) triage preserves safety; (3) the specialty will adopt it. "
  "Reasoning path: a systems model explains why hiring alone can't fix compounding growth and predicts engineered workflows. "
  "Proposed mechanism: 'engineered-workload' radiology - triaged, protected, AI-assisted reading. "
  "What would confirm it: engineered departments showing lower burnout with maintained accuracy. "
  "What would kill it: evidence that volume growth defeats any workflow engineering. "
  "What this does not claim: it does not claim a staffing solution exists, offers no medical advice, and does not constitute a management recommendation."),
 "sig_lens": "The Signature lens reads the crisis as unengineered work, and asks what systems would sustain it.",
 "how_it_works": "Researchers study workload through burnout surveys, interruption-error studies, and workflow trials.",
 "key_points": [
  "Imaging volumes grow 5-10% yearly; radiologist supply stagnates.",
  "Burnout rates are among medicine's highest.",
  "Errors rise with fatigue and interruption.",
  "AI oversight added work rather than relieving it.",
  "Hiring alone can't fix compounding growth.",
 ],
 "requirements": [
  "Engineered workflows proven to cut burnout.",
  "Triage systems preserving diagnostic safety.",
  "AI that verifiably reduces net work.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Harolds JA et al. Burnout in radiology. Various; 2016-2021.",
  "McDonald JS et al. Workload and error studies. Various; 2015-2020.",
  "Parikh JR et al. Radiology workforce analyses. Various; 2018-2023.",
  "Chen J et al. Interruption and diagnostic error. Various; 2019-2022.",
 ],
 "demo_data": {"a": ("annual imaging volume growth, percent (approx)", 7.0),
               "b": ("annual radiologist supply growth, percent (approx)", 2.0), "bounds": (2.5, 5.0),
               "step1": "demand grows three times faster than supply - the arithmetic of the crisis",
               "confirm": "engineered departments show lower burnout with maintained accuracy",
               "refute": "volume growth proves to defeat workflow engineering"},
},
# ------------------------------------------------------------------ rank 13
{
 "key": "pet-tracers",
 "name": "PET Tracers: Imaging Beyond FDG",
 "group": "Nuclear Medicine",
 "ladder_rank": 13, "ladder_tier": "compounded",
 "problem": "FDG-PET images glucose metabolism - but most diseases aren't glucose problems. Where are the tracers for the rest of medicine?",
 "description": "PET imaging is dominated by FDG (fluorodeoxyglucose) - a blunt glucose-metabolism marker. Disease-specific tracers exist in pockets (amyloid, tau, PSMA for prostate cancer, DOTATATE) but most pathologies lack molecular imaging. Tracer development is slow, expensive, and commercially unattractive for rare indications.",
 "background": "FDG-PET became oncology's workhorse in the 2000s; amyloid tracers (2012) enabled Alzheimer's imaging; PSMA (2020s) transformed prostate cancer. But each tracer took decades; the pipeline is thin. As of 2026 most diseases remain invisible to molecular imaging.",
 "why_it_matters": "Disease-specific tracers would make PET a precision-medicine tool: seeing the actual pathology, not its glucose shadow.",
 "sig_pointer": "The Signature system's proposed approach treats tracer development as a platform problem, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that tracer development needs platforms: modular chemistry and shared validation pipelines that make each new tracer affordable - rather than bespoke decades-long programs. "
  "Assumptions: (1) platform chemistry generalizes; (2) shared validation works; (3) economics follow. "
  "Reasoning path: a platform model explains the thin pipeline and predicts tracer proliferation. "
  "Proposed mechanism: 'platform' tracer development - modular radiochemistry with common validation. "
  "What would confirm it: platform-derived tracers reaching clinic faster and cheaper. "
  "What would kill it: evidence that each tracer is irreducibly bespoke. "
  "What this does not claim: it does not claim new tracers exist, offers no medical advice, and does not constitute a development recommendation."),
 "sig_lens": "The Signature lens reads the tracer drought as uneconomical bespoke work, and asks what platforms would change.",
 "how_it_works": "Researchers study PET tracers through radiochemistry platforms, PSMA/amyloid translation histories, and validation research.",
 "key_points": [
  "FDG dominates PET as a blunt metabolism marker.",
  "Amyloid, tau, PSMA, DOTATATE show what's possible.",
  "Each tracer took decades of bespoke development.",
  "Most diseases lack molecular imaging.",
  "Commercial incentives are weak for rare indications.",
 ],
 "requirements": [
  "Modular tracer platforms proven in practice.",
  "Faster cheaper tracer translation.",
  "Coverage of major untraced pathologies.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Gambhir SS. Molecular imaging reviews. Various; 2002-2015.",
  "Klunk WE et al. Amyloid imaging. Various; 2004-2012.",
  "Hofman MS et al. PSMA PET. Various; 2018-2021.",
  "Weber WA et al. PET tracer development. Various; 2016-2022.",
 ],
 "demo_data": {"a": ("disease-specific PET tracers in routine use (approx)", 10.0),
               "b": ("diseases needing molecular imaging (approx)", 200.0), "bounds": (0.03, 0.08),
               "step1": "ten tracers for two hundred diseases - molecular imaging's coverage gap",
               "confirm": "platform-derived tracers reach clinic faster and cheaper",
               "refute": "each tracer proves irreducibly bespoke"},
},
# ------------------------------------------------------------------ rank 14
{
 "key": "theranostics",
 "name": "Theranostics: See It, Treat It",
 "group": "Nuclear Medicine",
 "ladder_rank": 14, "ladder_tier": "compounded",
 "problem": "Theranostics pairs imaging with targeted radiotherapy - but which cancers, which targets, and how to manage the toxicities?",
 "description": "Theranostics - diagnostic tracer plus therapeutic isotope on the same target (Lutathera for neuroendocrine tumors, Pluvicto for prostate cancer) - is nuclear medicine's breakthrough. But the target list is short, resistance mechanisms are unmapped, toxicities (marrow, kidneys, salivary glands) limit dosing, and the field lacks predictive biomarkers for who benefits.",
 "background": "PRRT for neuroendocrine tumors proved the concept (NETTER-1, 2017); Pluvicto's VISION trial (2021) brought it to prostate cancer. Dosimetry - personalizing the radiation dose - remains crude. As of 2026 theranostics works brilliantly in niches with expansion blocked by target and toxicity questions.",
 "why_it_matters": "Theranostics is the closest medicine has to magic bullets: expanding it would transform oncology for target-expressing cancers.",
 "sig_pointer": "The Signature system's proposed approach treats theranostics as a dosimetry problem, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that theranostics' expansion is gated by dosimetry: personalizing the radiation dose to tumor versus organs - maximizing kill while sparing marrow and kidneys. "
  "Assumptions: (1) dosimetry predicts both efficacy and toxicity; (2) it is implementable; (3) personalized dosing expands the treatable population. "
  "Reasoning path: a dosimetry model explains current limitations and predicts precision theranostics. "
  "Proposed mechanism: 'dosimetry-driven' theranostics - every treatment planned by measured dose distribution. "
  "What would confirm it: dosimetry-planned treatments beating fixed-dose ones. "
  "What would kill it: evidence that dosimetry doesn't predict outcomes. "
  "What this does not claim: it does not claim theranostics works broadly, offers no medical advice, and does not constitute a treatment recommendation."),
 "sig_lens": "The Signature lens reads theranostics as dose-limited, and asks what personalized dosimetry would unlock.",
 "how_it_works": "Researchers study theranostics through NETTER-1/VISION follow-ups, dosimetry research, and target-discovery programs.",
 "key_points": [
  "Lutathera and Pluvicto prove the concept in niches.",
  "The target list is short.",
  "Marrow, kidney, and salivary toxicities limit dosing.",
  "Dosimetry remains crude.",
  "No predictive biomarkers for benefit exist.",
 ],
 "requirements": [
  "Personalized dosimetry proven superior.",
  "New targets with theranostic pairs.",
  "Resistance mechanisms mapped.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Strosberg J et al. NETTER-1 trial. NEJM. 2017;376:125-135.",
  "Sartor O et al. VISION trial (Pluvicto). NEJM. 2021;385:1091-1103.",
  "Bodei L et al. Theranostics reviews. Various; 2018-2023.",
  "Kratochwil C et al. Dosimetry research. Various; 2019-2023.",
 ],
 "demo_data": {"a": ("cancers with approved theranostics (approx)", 3.0),
               "b": ("cancers needing targeted therapy (approx)", 50.0), "bounds": (0.03, 0.1),
               "step1": "three cancers treated of fifty needing it - the breakthrough confined to niches",
               "confirm": "dosimetry-planned treatments beat fixed-dose ones",
               "refute": "dosimetry proves not to predict outcomes"},
},
# ------------------------------------------------------------------ rank 15
{
 "key": "radiomics",
 "name": "Radiomics: Can Images Reveal Genes?",
 "group": "Artificial Intelligence",
 "ladder_rank": 15, "ladder_tier": "compounded",
 "problem": "Radiomics extracts thousands of features from images - but do they predict biology, or just overfit noise?",
 "description": "Radiomics - high-throughput image-feature extraction - promises to predict genomics, prognosis, and treatment response from routine scans. But the field is plagued by overfitting, feature instability across scanners, and failed replications. Few radiomic signatures have validated prospectively; the signal-to-hype ratio is poor.",
 "background": "Radiomics emerged in the 2010s (Lambin, Gillies); early signatures for lung and head-neck cancer excited the field. Reproducibility studies showed scanner-dependence; the IBSI (2016) standardized features. As of 2026 radiomics is a research program with minimal clinical translation.",
 "why_it_matters": "If images truly encode biology, every scan becomes a virtual biopsy; if radiomics is overfit noise, the field needs redirecting.",
 "sig_pointer": "The Signature system's proposed approach treats radiomics as a reproducibility problem, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that radiomics needs reproducibility-first science: scanner-harmonized features, prospective validation, and biological grounding - with signatures earning clinical use only after prospective proof. "
  "Assumptions: (1) real signals exist beneath the noise; (2) harmonization preserves them; (3) prospective validation is feasible. "
  "Reasoning path: a reproducibility model explains the translation failure and predicts validated signatures. "
  "Proposed mechanism: 'reproducibility-first' radiomics - harmonized, biologically grounded, prospectively validated. "
  "What would confirm it: harmonized signatures validating prospectively. "
  "What would kill it: evidence that image features carry no stable biological signal. "
  "What this does not claim: it does not claim radiomics works, offers no medical advice, and does not constitute a diagnostic recommendation."),
 "sig_lens": "The Signature lens reads radiomics as signal buried in scanner noise, and asks what harmonization would reveal.",
 "how_it_works": "Researchers study radiomics through IBSI standardization, harmonization research, and prospective validation trials.",
 "key_points": [
  "Radiomics promises virtual biopsies from routine scans.",
  "Overfitting and scanner-dependence plague the field.",
  "Few signatures validated prospectively.",
  "IBSI standardized features but not practice.",
  "Clinical translation is minimal.",
 ],
 "requirements": [
  "Scanner-harmonized reproducible features.",
  "Prospective validation of signatures.",
  "Biological grounding of image features.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Lambin P et al. Radiomics founding papers. Various; 2012-2017.",
  "Gillies RJ et al. Radiomics and cancer. Various; 2015-2016.",
  "Zwanenburg A et al. IBSI standardization. Radiology. 2020;295:328-338.",
  "Park JE et al. Radiomics reproducibility reviews. Various; 2020-2023.",
 ],
 "demo_data": {"a": ("radiomic signatures validated prospectively (approx)", 5.0),
               "b": ("radiomic signatures published (approx)", 1000.0), "bounds": (0.002, 0.01),
               "step1": "five validated of a thousand published - the signature graveyard",
               "confirm": "harmonized signatures validate prospectively",
               "refute": "image features prove to carry no stable biological signal"},
},
# ------------------------------------------------------------------ rank 16
{
 "key": "image-reconstruction",
 "name": "Image Reconstruction: The Math Behind the Picture",
 "group": "Physics",
 "ladder_rank": 16, "ladder_tier": "compounded",
 "problem": "Every CT and MRI image is a computed reconstruction - but reconstruction algorithms keep advancing. What's the theoretical limit of image quality per dose?",
 "description": "Image reconstruction - turning raw scanner data into pictures - determines the dose-quality tradeoff: filtered back-projection, iterative reconstruction, and now deep-learning reconstruction each pushed quality higher per dose. But the theoretical limit (what's knowable from the data) is undefined, and deep-learning methods risk hallucinating plausible-but-false anatomy.",
 "background": "Iterative reconstruction (2010s) cut CT doses substantially; compressed sensing transformed MRI speed; deep-learning reconstruction (2020s) promises more. Hallucination concerns (Antun, 2020) showed networks inventing structures. As of 2026 the field advances without knowing the limit or fully controlling the artifacts.",
 "why_it_matters": "Reconstruction is the dose-quality lever: knowing the limit would define how low doses can go and which algorithms are safe.",
 "sig_pointer": "The Signature system's proposed approach bounds reconstruction by information theory, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that reconstruction limits are information-theoretic: the data contains finite information, and algorithms should be certified against hallucination by uncertainty quantification. "
  "Assumptions: (1) the limit is computable; (2) uncertainty is quantifiable; (3) certification is enforceable. "
  "Reasoning path: an information model defines the achievable and predicts hallucination-proof reconstruction. "
  "Proposed mechanism: 'uncertainty-certified' reconstruction - algorithms reporting what they know versus invent. "
  "What would confirm it: certified algorithms matching theoretical limits. "
  "What would kill it: evidence that limits are unreachable in practice. "
  "What this does not claim: it does not claim any algorithm is safe, offers no medical advice, and does not constitute a technical recommendation."),
 "sig_lens": "The Signature lens reads reconstruction as information recovery, and asks what the data actually contains.",
 "how_it_works": "Researchers study reconstruction through information-theoretic analyses, hallucination research, and algorithm comparisons.",
 "key_points": [
  "Reconstruction determines the dose-quality tradeoff.",
  "Deep-learning methods risk hallucinating anatomy.",
  "The theoretical quality-per-dose limit is undefined.",
  "Iterative and compressed-sensing methods transformed practice.",
  "Uncertainty quantification is largely absent.",
 ],
 "requirements": [
  "Computed information-theoretic limits.",
  "Hallucination-proof certified algorithms.",
  "Dose floors derived from reconstruction limits.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Antun V et al. Instabilities of deep-learning reconstruction. PNAS. 2020;117:30088-30095.",
  "Lustig M et al. Compressed sensing MRI. Various; 2007-2008.",
  "Willemink MJ et al. Iterative reconstruction reviews. Various; 2013-2019.",
  "Shan H et al. Deep-learning reconstruction reviews. Various; 2020-2023.",
 ],
 "demo_data": {"a": ("reconstruction algorithms with hallucination certification (approx)", 1.0),
               "b": ("deep-learning reconstruction methods published (approx)", 100.0), "bounds": (0.005, 0.02),
               "step1": "a hundred methods that might invent anatomy, one with certification - the safety gap",
               "confirm": "certified algorithms match theoretical limits",
               "refute": "limits prove unreachable in practice"},
},
# ------------------------------------------------------------------ rank 17
{
 "key": "functional-mri",
 "name": "fMRI's Reproducibility Problem",
 "group": "Modalities",
 "ladder_rank": 17, "ladder_tier": "compounded",
 "problem": "fMRI mapped the working brain - then the statistics collapsed. How much of brain mapping survives the reproducibility crisis?",
 "description": "Functional MRI - blood-oxygen signals as brain-activity proxies - produced decades of brain-mapping findings. Then Eklund (2016) showed common software produced 70% false-positive rates; the field's statistics were broken. Reforms (preregistration, larger samples, better methods) followed - but the old literature's validity remains uncertain.",
 "background": "fMRI's rise (1990s-2000s) was meteoric; the dead-salmon study (Bennett, 2009) first mocked the statistics. Eklund's cluster-failure paper (2016) forced reform. The field adopted fMRIPrep, larger samples, and preregistration. As of 2026 fMRI is mid-rebuild: new work is better, old findings uncertain.",
 "why_it_matters": "fMRI underpins cognitive neuroscience and presurgical mapping: its credibility determines whether brain maps guide surgery or mislead it.",
 "sig_pointer": "The Signature system's proposed approach rebuilds fMRI on validated methods, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that fMRI's rebuild needs methods triage: re-testing landmark findings with validated pipelines, retiring the unreplicable, and certifying presurgical-mapping protocols. "
  "Assumptions: (1) the valid findings are separable; (2) re-testing is feasible; (3) the field will accept triage. "
  "Reasoning path: a triage model explains the crisis and predicts a cleaned literature. "
  "Proposed mechanism: 'methods-triaged' fMRI - landmark re-testing with certified pipelines. "
  "What would confirm it: re-tested landmarks replicating with validated methods. "
  "What would kill it: evidence that most findings were statistical artifacts. "
  "What this does not claim: it does not claim any fMRI finding is valid, offers no medical advice, and does not constitute a methodological recommendation."),
 "sig_lens": "The Signature lens reads the fMRI crisis as unvalidated statistics, and asks what re-testing would salvage.",
 "how_it_works": "Researchers study fMRI reproducibility through methods reform, landmark re-testing, and presurgical-validation studies.",
 "key_points": [
  "Common fMRI software produced 70% false-positive rates (Eklund 2016).",
  "The dead-salmon study exposed the statistics early.",
  "Reforms: preregistration, larger samples, better pipelines.",
  "Old literature's validity is uncertain.",
  "Presurgical mapping needs certified reliability.",
 ],
 "requirements": [
  "Landmark findings re-tested with valid methods.",
  "Certified presurgical-mapping protocols.",
  "A cleaned, trustworthy literature.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Eklund A et al. Cluster failure in fMRI. PNAS. 2016;113:7900-7905.",
  "Bennett CM et al. Dead salmon study. 2009.",
  "Poldrack RA et al. fMRI reform. Various; 2017-2020.",
  "Nichols TE et al. Best practices in fMRI. Various; 2017-2022.",
 ],
 "demo_data": {"a": ("false-positive rate of common fMRI software, percent (approx)", 70.0),
               "b": ("percent scale", 100.0), "bounds": (0.55, 0.85),
               "step1": "seven in ten 'findings' were noise - the statistical collapse of brain mapping",
               "confirm": "re-tested landmarks replicate with validated methods",
               "refute": "most findings prove to be statistical artifacts"},
},
# ------------------------------------------------------------------ rank 18
{
 "key": "breast-density",
 "name": "Breast Density: Risk, Masking, and Notification",
 "group": "Screening",
 "ladder_rank": 18, "ladder_tier": "compounded",
 "problem": "Dense breasts raise cancer risk and hide tumors on mammograms - but what should be done about it? The answer varies by state and country.",
 "description": "Dense breast tissue - common in half of screened women - both increases cancer risk and masks tumors on mammography. Density-notification laws spread across US states; supplemental screening (ultrasound, MRI, contrast mammography) is recommended inconsistently. The evidence for which supplemental modality, for whom, is incomplete.",
 "background": "Density's dual role was established in the 2000s-2010s (Boyd, McCormack); notification laws spread from 2009; the DENSE trial (2019) showed MRI finds cancers in dense breasts. But cost-effectiveness, interval, and modality choice remain open. As of 2026 dense-breast management is legislated ahead of the evidence.",
 "why_it_matters": "Half of screened women have dense breasts: getting supplemental screening right affects hundreds of millions.",
 "sig_pointer": "The Signature system's proposed approach personalizes dense-breast screening, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that dense-breast management should be risk-personalized: density plus other risk factors determining who gets which supplemental modality - replacing blanket notification with targeted action. "
  "Assumptions: (1) combined risk predicts benefit; (2) modality choice matters; (3) personalization is implementable. "
  "Reasoning path: a personalization model explains the legislation-evidence gap and predicts effective dense-breast programs. "
  "Proposed mechanism: 'risk-personalized' dense-breast screening - modality matched to individual risk. "
  "What would confirm it: personalized programs beating blanket notification on outcomes. "
  "What would kill it: evidence that supplemental screening doesn't improve outcomes. "
  "What this does not claim: it does not claim any screening approach is correct, offers no medical advice, and does not constitute a screening recommendation."),
 "sig_lens": "The Signature lens reads density notification as legislated without targeting, and asks what personalization would direct.",
 "how_it_works": "Researchers study breast density through the DENSE trial, risk-model research, and notification-law evaluations.",
 "key_points": [
  "Half of screened women have dense breasts.",
  "Density raises risk and masks tumors.",
  "Notification laws spread ahead of the evidence.",
  "The DENSE trial showed MRI finds hidden cancers.",
  "Supplemental modality choice is unresolved.",
 ],
 "requirements": [
  "Risk-personalized supplemental screening.",
  "Modality comparisons on outcomes.",
  "Cost-effective targeted programs.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Boyd NF et al. Breast density and risk. Various; 2007-2011.",
  "Bakker MF et al. DENSE trial. NEJM. 2019;381:2091-2102.",
  "McCormack VA et al. Density meta-analyses. Various; 2006-2016.",
  "Freer PE et al. Dense-breast management reviews. Various; 2017-2022.",
 ],
 "demo_data": {"a": ("screened women with dense breasts, percent (approx)", 50.0),
               "b": ("percent scale", 100.0), "bounds": (0.4, 0.6),
               "step1": "half of screened women affected by a problem managed by inconsistent laws",
               "confirm": "personalized programs beat blanket notification on outcomes",
               "refute": "supplemental screening proves not to improve outcomes"},
},
# ------------------------------------------------------------------ rank 19
{
 "key": "pediatric-dose",
 "name": "Pediatric Dose: Children Are Not Small Adults",
 "group": "Radiation Safety",
 "ladder_rank": 19, "ladder_tier": "compounded",
 "problem": "Children are more radiosensitive and have longer to develop cancers - yet pediatric protocols are often scaled-down adult ones. What are the right doses?",
 "description": "Pediatric imaging - the most dose-sensitive population - frequently uses adult-derived protocols adjusted by weight. But children's radiosensitivity, body composition, and clinical tasks differ; size-specific dose estimates (SSDE) are underused; and the Image Gently campaign's plea for pediatric-specific protocols is incompletely implemented.",
 "background": "Pediatric radiosensitivity was long known; the Image Gently campaign (2007) pushed child-sizing. SSDE (AAPM, 2011) enabled size-specific estimates. But audits still find adult protocols used for children. As of 2026 pediatric dose optimization is advocated more than practiced.",
 "why_it_matters": "Children have the most to lose from unnecessary radiation: pediatric-specific protocols are the clearest win in dose safety.",
 "sig_pointer": "The Signature system's proposed approach mandates pediatric-specific protocol design, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that pediatric protocols must be designed from pediatric data: size-specific, task-specific, child-derived - with audits enforcing their use. "
  "Assumptions: (1) pediatric optima differ from scaled adult ones; (2) they are measurable; (3) enforcement works. "
  "Reasoning path: a pediatric-first model explains persistent over-dosing and predicts optimized child imaging. "
  "Proposed mechanism: 'pediatric-designed' protocols - built from child data, enforced by audit. "
  "What would confirm it: pediatric-designed protocols showing lower doses with maintained accuracy. "
  "What would kill it: evidence that scaled adult protocols are already optimal. "
  "What this does not claim: it does not claim any dose is safe, offers no medical advice, and does not constitute a dosing recommendation."),
 "sig_lens": "The Signature lens reads pediatric dosing as scaled-down adults, and asks what child-derived protocols would prescribe.",
 "how_it_works": "Researchers study pediatric dose through SSDE implementation, Image Gently audits, and child-specific protocol trials.",
 "key_points": [
  "Children are more radiosensitive with longer at-risk lifespans.",
  "Adult protocols are often merely weight-scaled.",
  "SSDE enables size-specific estimates but is underused.",
  "Image Gently is incompletely implemented.",
  "Audits still find adult protocols used for children.",
 ],
 "requirements": [
  "Child-derived protocol optima.",
  "Universal SSDE implementation.",
  "Audits enforcing pediatric protocols.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Image Gently campaign. 2007 onward.",
  "AAPM. Size-specific dose estimates (SSDE). Report 204. 2011.",
  "Strauss KJ et al. Pediatric dose reviews. Various; 2010-2019.",
  "Boone JM et al. Pediatric CT dose. Various; 2012-2020.",
 ],
 "demo_data": {"a": ("pediatric scans using adult-derived protocols, percent (approx)", 40.0),
               "b": ("percent scale", 100.0), "bounds": (0.28, 0.52),
               "step1": "two in five child scans use scaled adult protocols - the most radiosensitive patients, the least specific dosing",
               "confirm": "pediatric-designed protocols show lower doses with maintained accuracy",
               "refute": "scaled adult protocols prove already optimal"},
},
# ------------------------------------------------------------------ rank 20
{
 "key": "interventional",
 "name": "Interventional Radiology's Evidence Gap",
 "group": "Interventions",
 "ladder_rank": 20, "ladder_tier": "compounded",
 "problem": "Interventional radiology does remarkable minimally invasive procedures - but the RCT evidence base lags far behind the practice.",
 "description": "Interventional radiology (IR) - embolization, ablation, thrombectomy, TACE - treats disease through catheters with stunning technical success. But RCT evidence is thin: many procedures spread on technical feasibility and case series; comparative effectiveness versus surgery or medicine is often unknown. The field innovates faster than it validates.",
 "background": "IR grew from Seldinger's technique (1953) through Dotter's angioplasty (1964) to modern embolization and ablation. Technical success rates are high; but landmark RCTs are few (some stroke thrombectomy trials excepted). As of 2026 IR is a practice built on technical excellence with an evidence gap.",
 "why_it_matters": "IR procedures are done by the hundred-thousand: comparative-effectiveness evidence would ensure the right patients get the right minimally invasive option.",
 "sig_pointer": "The Signature system's proposed approach builds IR's comparative-effectiveness evidence, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that IR needs pragmatic comparative trials: procedure versus surgery versus medicine for each major indication - with the technical innovators leading the validation. "
  "Assumptions: (1) comparative trials are feasible; (2) the field will participate; (3) evidence changes practice. "
  "Reasoning path: a comparative model explains the evidence gap and predicts validated IR practice. "
  "Proposed mechanism: 'comparative-trial' IR - pragmatic RCTs for each major procedure. "
  "What would confirm it: trials defining IR's place per indication. "
  "What would kill it: evidence that technical success predicts clinical success well enough. "
  "What this does not claim: it does not claim any procedure is unproven, offers no medical advice, and does not constitute a treatment recommendation."),
 "sig_lens": "The Signature lens reads IR as innovation ahead of validation, and asks what comparative trials would establish.",
 "how_it_works": "Researchers study IR evidence through pragmatic RCTs, registry studies, and comparative-effectiveness research.",
 "key_points": [
  "IR technical success rates are high.",
  "RCT evidence is thin for most procedures.",
  "Procedures spread on feasibility and case series.",
  "Comparative effectiveness is often unknown.",
  "Stroke thrombectomy trials are the exception.",
 ],
 "requirements": [
  "Pragmatic comparative trials per indication.",
  "Registry-based outcome tracking.",
  "Evidence-matched procedure selection.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Seldinger SI. Catheter technique. 1953.",
  "Dotter CT et al. Angioplasty origins. 1964.",
  "Goyal M et al. Stroke thrombectomy trials. Various; 2015-2018.",
  "Kaufman JA et al. IR evidence reviews. Various; 2018-2023.",
 ],
 "demo_data": {"a": ("IR procedures with RCT support (approx)", 20.0),
               "b": ("major IR procedures (approx)", 100.0), "bounds": (0.12, 0.3),
               "step1": "four in five procedures lack RCT support - technical excellence without comparative proof",
               "confirm": "trials define IR's place per indication",
               "refute": "technical success proves to predict clinical success"},
},
# ------------------------------------------------------------------ rank 21
{
 "key": "quantitative-imaging",
 "name": "Quantitative Imaging Biomarkers",
 "group": "Physics",
 "ladder_rank": 21, "ladder_tier": "compounded",
 "problem": "Radiology reads images qualitatively - but quantitative biomarkers (ADC, SUV, perfusion values) could make imaging a measurement science. What's blocking them?",
 "description": "Quantitative imaging biomarkers (QIBs) - numbers extracted from images (apparent diffusion coefficients, standardized uptake values, perfusion parameters) - promise objective measurement. But standardization is poor: the same biomarker varies between scanners, vendors, and protocols. QIBA (2008) works on profiles; clinical adoption is minimal.",
 "background": "QIBs emerged with functional imaging; SUV became oncology's de facto quantitative measure despite known variability. QIBA (Quantitative Imaging Biomarkers Alliance, 2008) develops standardization profiles. But vendor cooperation is limited and clinical workflows remain qualitative. As of 2026 imaging is still mostly read, not measured.",
 "why_it_matters": "Quantitative imaging would make scans objective, comparable, and trial-ready: the transformation from art to measurement.",
 "sig_pointer": "The Signature system's proposed approach standardizes QIBs into clinical metrology, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that QIBs need metrology: traceable standards, cross-vendor calibration, and uncertainty budgets - making imaging biomarkers as reliable as lab tests. "
  "Assumptions: (1) standardization is technically achievable; (2) vendors will cooperate; (3) clinics will adopt. "
  "Reasoning path: a metrology model explains the adoption failure and predicts quantitative radiology. "
  "Proposed mechanism: 'metrology-grade' QIBs - calibrated, traceable, uncertainty-quantified biomarkers. "
  "What would confirm it: cross-vendor QIB agreement matching lab-test reliability. "
  "What would kill it: evidence that biological variability defeats standardization. "
  "What this does not claim: it does not claim any biomarker is valid, offers no medical advice, and does not constitute a technical recommendation."),
 "sig_lens": "The Signature lens reads imaging as uncalibrated measurement, and asks what metrology would standardize.",
 "how_it_works": "Researchers study QIBs through QIBA profiles, cross-vendor comparison studies, and standardization trials.",
 "key_points": [
  "QIBs promise objective imaging measurement.",
  "Scanner and vendor variation is large.",
  "QIBA develops profiles but adoption is minimal.",
  "SUV is used despite known variability.",
  "Radiology remains qualitative.",
 ],
 "requirements": [
  "Traceable cross-vendor standards.",
  "Uncertainty budgets for each biomarker.",
  "Clinical workflows built on measurement.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "QIBA (Quantitative Imaging Biomarkers Alliance). Profiles. 2008 onward.",
  "Sullivan DC et al. QIB metrology. Various; 2013-2019.",
  "Boellaard R et al. SUV standardization. Various; 2015-2020.",
  "Obuchowski NA et al. QIB statistics. Various; 2015-2021.",
 ],
 "demo_data": {"a": ("SUV variation between scanners, percent (approx)", 25.0),
               "b": ("percent scale", 100.0), "bounds": (0.15, 0.35),
               "step1": "a quarter variation in the commonest quantitative measure - uncalibrated numbers guiding cancer care",
               "confirm": "cross-vendor QIB agreement matches lab-test reliability",
               "refute": "biological variability proves to defeat standardization"},
},
# ------------------------------------------------------------------ rank 22
{
 "key": "dual-energy",
 "name": "Dual-Energy and Spectral CT: What Can It Really Do?",
 "group": "Modalities",
 "ladder_rank": 22, "ladder_tier": "compounded",
 "problem": "Spectral CT sees materials, not just densities - but its clinical applications remain narrower than the physics promises. What's the real scope?",
 "description": "Dual-energy/spectral CT - imaging at multiple X-ray energies - enables material decomposition (iodine maps, virtual non-contrast, gout crystals, kidney-stone composition). But clinical adoption is narrow: gout and stone characterization lead; most applications remain research. The physics promises more than practice delivers.",
 "background": "Dual-energy CT emerged in the 2000s (Flohr, Johnson); photon-counting detectors (2020s) promise true spectral imaging. Gout crystal detection and stone composition are validated; virtual non-contrast saves dose. But workflow integration and reimbursement lag. As of 2026 spectral CT is proven physics with a narrow clinical footprint.",
 "why_it_matters": "Spectral CT could replace multiple scans with one: defining its scope would consolidate imaging and cut dose.",
 "sig_pointer": "The Signature system's proposed approach maps spectral CT's validated scope, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that spectral CT needs scope mapping: which clinical questions it answers better than conventional CT - proven indication by indication. "
  "Assumptions: (1) the advantages are indication-specific; (2) they are provable; (3) mapping drives adoption. "
  "Reasoning path: a scope model explains narrow adoption and predicts targeted expansion. "
  "Proposed mechanism: 'scope-mapped' spectral CT - validated indications driving deployment. "
  "What would confirm it: mapped indications showing superior outcomes. "
  "What would kill it: evidence that conventional CT suffices everywhere. "
  "What this does not claim: it does not claim spectral CT is superior, offers no medical advice, and does not constitute a technology recommendation."),
 "sig_lens": "The Signature lens reads spectral CT as physics awaiting indications, and asks which questions it answers best.",
 "how_it_works": "Researchers study spectral CT through material-decomposition validation, gout/stone trials, and photon-counting research.",
 "key_points": [
  "Spectral CT enables material decomposition.",
  "Gout and kidney-stone applications are validated.",
  "Most applications remain research-stage.",
  "Photon-counting promises true spectral imaging.",
  "Workflow and reimbursement lag the physics.",
 ],
 "requirements": [
  "Indication-by-indication superiority proof.",
  "Workflow-integrated spectral protocols.",
  "Reimbursement for spectral applications.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Flohr T et al. Dual-energy CT. Various; 2006-2016.",
  "Johnson TRC et al. Clinical dual-energy applications. Various; 2007-2012.",
  "Bongartz G et al. Spectral CT reviews. Various; 2015-2020.",
  "Rajendran K et al. Photon-counting CT. Various; 2021-2024.",
 ],
 "demo_data": {"a": ("spectral CT's validated clinical indications (approx)", 5.0),
               "b": ("promised applications (approx)", 30.0), "bounds": (0.1, 0.25),
               "step1": "five delivered of thirty promised - the physics-practice gap",
               "confirm": "mapped indications show superior outcomes",
               "refute": "conventional CT proves sufficient everywhere"},
},
# ------------------------------------------------------------------ rank 23
{
 "key": "elastography",
 "name": "Elastography: Imaging Tissue Stiffness",
 "group": "Modalities",
 "ladder_rank": 23, "ladder_tier": "compounded",
 "problem": "Tissue stiffness signals disease - cancer, fibrosis, cirrhosis - but elastography's standardization and scope are incomplete. What can stiffness imaging really do?",
 "description": "Elastography - ultrasound and MR measurement of tissue stiffness - detects liver fibrosis without biopsy, characterizes breast lesions, and stages disease. But cutoffs vary between vendors, the biology of stiffness-disease links is incomplete, and the clinical scope beyond liver is still being defined.",
 "background": "Transient elastography (FibroScan, 2000s) transformed hepatology; shear-wave methods followed; MR elastography added precision. Liver applications are validated; breast, thyroid, and prostate applications are emerging. As of 2026 liver elastography is standard with other organs catching up.",
 "why_it_matters": "Stiffness imaging replaces biopsies: defining its scope would spare millions of invasive procedures.",
 "sig_pointer": "The Signature system's proposed approach standardizes elastography into a measurement science, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that elastography needs vendor-neutral standardization: calibrated stiffness scales, validated cutoffs per organ, and defined clinical scope. "
  "Assumptions: (1) stiffness is a real disease signal; (2) it is standardizable; (3) scope is definable. "
  "Reasoning path: a standardization model explains slow expansion and predicts broad adoption. "
  "Proposed mechanism: 'standardized' elastography - calibrated scales and organ-specific validated cutoffs. "
  "What would confirm it: cross-vendor cutoff agreement and expanded validated scope. "
  "What would kill it: evidence that stiffness signals are too vendor-specific to standardize. "
  "What this does not claim: it does not claim elastography replaces biopsy broadly, offers no medical advice, and does not constitute a technical recommendation."),
 "sig_lens": "The Signature lens reads elastography as signal awaiting standardization, and asks what calibration would unlock.",
 "how_it_works": "Researchers study elastography through vendor-comparison studies, cutoff-validation trials, and scope-expansion research.",
 "key_points": [
  "Elastography detects liver fibrosis without biopsy.",
  "Cutoffs vary between vendors.",
  "Liver applications are validated; other organs emerging.",
  "The stiffness-disease biology is incomplete.",
  "Standardization would enable broad adoption.",
 ],
 "requirements": [
  "Vendor-neutral calibrated stiffness scales.",
  "Organ-specific validated cutoffs.",
  "Defined clinical scope beyond liver.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Sandrin L et al. Transient elastography. Various; 2003-2011.",
  "Sigrist RMS et al. Ultrasound elastography reviews. Various; 2017-2021.",
  "Venkatesh SK et al. MR elastography. Various; 2013-2018.",
  "Ferraioli G et al. Elastography guidelines. Various; 2015-2020.",
 ],
 "demo_data": {"a": ("liver biopsies avoided by elastography, percent (approx)", 60.0),
               "b": ("percent scale", 100.0), "bounds": (0.45, 0.75),
               "step1": "three in five liver biopsies avoided - the proven win awaiting standardization elsewhere",
               "confirm": "cross-vendor cutoff agreement and expanded validated scope",
               "refute": "stiffness signals prove too vendor-specific"},
},
# ------------------------------------------------------------------ rank 24
{
 "key": "hyperpolarized-mri",
 "name": "Hyperpolarized MRI: Imaging Metabolism in Real Time",
 "group": "Modalities",
 "ladder_rank": 24, "ladder_tier": "advanced",
 "problem": "Hyperpolarized MRI watches metabolism happen live - but the technique is fiendishly complex. Can it become clinical?",
 "description": "Hyperpolarized MRI - boosting carbon-13 signals 10,000-fold to image pyruvate-to-lactate metabolism in real time - shows cancer metabolism, treatment response, and cardiac energetics directly. But it needs on-site hyperpolarizers, short-lived agents, and complex workflows. Clinical translation is slow despite stunning research results.",
 "background": "DNP hyperpolarization (Ardenkjaer-Larsen, 2003) enabled the field; first human prostate-cancer studies (Nelson, 2013) showed feasibility. Applications in cancer, heart, and kidney followed. But the infrastructure demands limit deployment to research centers. As of 2026 hyperpolarized MRI is proven science with minimal clinical footprint.",
 "why_it_matters": "Real-time metabolic imaging would transform oncology and cardiology: watching treatment work (or fail) within hours, not months.",
 "sig_pointer": "The Signature system's proposed approach simplifies hyperpolarized MRI into deployable form, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that hyperpolarized MRI needs workflow simplification: robust polarizers, longer-lived agents, and push-button protocols - making metabolic imaging deployable beyond research centers. "
  "Assumptions: (1) simplification is technically feasible; (2) clinical value justifies investment; (3) simplified systems validate. "
  "Reasoning path: a simplification model explains slow translation and predicts clinical adoption. "
  "Proposed mechanism: 'simplified' hyperpolarized MRI - deployable polarizers and agents. "
  "What would confirm it: simplified systems producing clinical-grade metabolic images. "
  "What would kill it: evidence that the physics resists simplification. "
  "What this does not claim: it does not claim hyperpolarized MRI is clinical, offers no medical advice, and does not constitute a technology recommendation."),
 "sig_lens": "The Signature lens reads the technique as brilliant but undeployable, and asks what simplification would clinicalize it.",
 "how_it_works": "Researchers study hyperpolarized MRI through polarizer engineering, agent development, and clinical-feasibility trials.",
 "key_points": [
  "Hyperpolarized MRI images metabolism in real time.",
  "Signal boosts of 10,000-fold enable carbon-13 imaging.",
  "On-site hyperpolarizers and short-lived agents limit deployment.",
  "First human studies (2013) proved feasibility.",
  "Clinical translation remains minimal.",
 ],
 "requirements": [
  "Simplified robust polarizer systems.",
  "Longer-lived hyperpolarized agents.",
  "Clinical-grade validation in deployable form.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Ardenkjaer-Larsen JH et al. DNP hyperpolarization. PNAS. 2003;100:10158-10163.",
  "Nelson SJ et al. First human hyperpolarized MRI. Science Translational Medicine. 2013;5:198ra108.",
  "Kurhanewicz J et al. Hyperpolarized MRI reviews. Various; 2011-2019.",
  "Wang ZJ et al. Clinical hyperpolarized MRI. Various; 2019-2023.",
 ],
 "demo_data": {"a": ("signal boost from hyperpolarization, fold (approx)", 10000.0),
               "b": ("fold scale (hundred-thousands)", 100000.0), "bounds": (0.05, 0.2),
               "step1": "ten-thousand-fold signal gain - yet confined to a handful of research centers",
               "confirm": "simplified systems produce clinical-grade metabolic images",
               "refute": "the physics proves resistant to simplification"},
},
# ------------------------------------------------------------------ rank 25
{
 "key": "photon-counting",
 "name": "Photon-Counting CT: The Next Revolution?",
 "group": "Modalities",
 "ladder_rank": 25, "ladder_tier": "advanced",
 "problem": "Photon-counting CT promises higher resolution at lower dose - but is it a revolution or an incremental upgrade?",
 "description": "Photon-counting CT - detectors counting individual X-ray photons by energy - offers higher spatial resolution, lower noise, spectral information, and dose reduction versus energy-integrating detectors. FDA clearance came in 2021 (Siemens Naeotom); clinical validation is accumulating. But cost, workflow, and the question of which applications truly benefit remain open.",
 "background": "Photon-counting research spanned decades (Fischer, Danielsson); the first clinical system cleared in 2021. Early studies show coronary, lung, and musculoskeletal advantages. But the installed base is tiny and comparative-effectiveness data is early. As of 2026 the technology is proven with revolution status pending.",
 "why_it_matters": "If photon-counting delivers on its promises, it resets CT's dose-quality frontier for decades; if incremental, it's an expensive upgrade.",
 "sig_pointer": "The Signature system's proposed approach tests photon-counting by clinical advantage, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that photon-counting CT needs advantage-mapping: which clinical tasks genuinely improve - proven indication by indication - rather than physics-superiority claims. "
  "Assumptions: (1) advantages are indication-specific; (2) they are provable; (3) mapping guides adoption. "
  "Reasoning path: an advantage model explains slow uptake and predicts targeted deployment. "
  "Proposed mechanism: 'advantage-mapped' photon-counting - deployment driven by proven clinical wins. "
  "What would confirm it: mapped indications showing superior outcomes. "
  "What would kill it: evidence that conventional CT matches it clinically. "
  "What this does not claim: it does not claim photon-counting is superior, offers no medical advice, and does not constitute a technology recommendation."),
 "sig_lens": "The Signature lens reads the revolution claim as unmapped, and asks which indications would prove it.",
 "how_it_works": "Researchers study photon-counting CT through comparative trials, coronary and lung validation studies, and dose comparisons.",
 "key_points": [
  "Photon-counting offers resolution, noise, spectral, and dose advantages.",
  "First clinical system cleared in 2021.",
  "Early studies show coronary and lung promise.",
  "The installed base is tiny.",
  "Comparative-effectiveness data is early.",
 ],
 "requirements": [
  "Indication-specific superiority proof.",
  "Dose-reduction validation in practice.",
  "Cost-effectiveness for adoption decisions.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Flohr T et al. Photon-counting CT. Various; 2020-2024.",
  "Rajendran K et al. Clinical photon-counting studies. Various; 2021-2023.",
  "Siemens Healthineers. Naeotom Alpha FDA clearance. 2021.",
  "Willemink MJ et al. Photon-counting reviews. Various; 2018-2023.",
 ],
 "demo_data": {"a": ("photon-counting CT systems installed worldwide (approx)", 100.0),
               "b": ("conventional CT systems (approx thousands)", 50.0), "bounds": (1.0, 3.0),
               "step1": "a hundred systems against fifty thousand - the revolution's installed base",
               "confirm": "mapped indications show superior outcomes",
               "refute": "conventional CT proves to match it clinically"},
},
# ------------------------------------------------------------------ rank 26
{
 "key": "contrast-mammography",
 "name": "Contrast-Enhanced Mammography's Place",
 "group": "Screening",
 "ladder_rank": 26, "ladder_tier": "advanced",
 "problem": "Contrast-enhanced mammography finds cancers MRI finds, cheaper and faster - but where does it fit between mammography and MRI?",
 "description": "Contrast-enhanced mammography (CEM) - iodinated contrast with dual-energy mammography - shows cancer detection approaching MRI at lower cost and better tolerance. But its place in the screening and diagnostic pathway is undefined: dense breasts? high risk? problem-solving? The evidence for each role is incomplete.",
 "background": "CEM emerged in the 2010s; studies showed MRI-comparable sensitivity for known cancers. Dense-breast and high-risk applications are being tested. But guidelines haven't positioned it, and contrast risks add complexity. As of 2026 CEM is a promising modality seeking its indication.",
 "why_it_matters": "CEM could democratize MRI-level detection: defining its place would bring high-sensitivity screening to settings without MRI.",
 "sig_pointer": "The Signature system's proposed approach positions CEM by comparative effectiveness, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that CEM needs pathway positioning: head-to-head comparisons against mammography-plus-ultrasound and MRI for each candidate indication - defining where it wins. "
  "Assumptions: (1) CEM wins specific indications; (2) comparisons are feasible; (3) positioning drives adoption. "
  "Reasoning path: a positioning model explains slow uptake and predicts defined clinical roles. "
  "Proposed mechanism: 'pathway-positioned' CEM - indications defined by comparative wins. "
  "What would confirm it: CEM winning defined indications in comparative trials. "
  "What would kill it: evidence that MRI or tomosynthesis suffices everywhere. "
  "What this does not claim: it does not claim CEM equals MRI, offers no medical advice, and does not constitute a screening recommendation."),
 "sig_lens": "The Signature lens reads CEM as a modality seeking indications, and asks which comparisons would place it.",
 "how_it_works": "Researchers study CEM through comparative-accuracy trials, dense-breast studies, and pathway analyses.",
 "key_points": [
  "CEM approaches MRI sensitivity at lower cost.",
  "Its pathway position is undefined.",
  "Dense-breast and high-risk roles are being tested.",
  "Guidelines haven't positioned it.",
  "Contrast risks add complexity.",
 ],
 "requirements": [
  "Head-to-head comparative trials per indication.",
  "Defined winning indications.",
  "Guideline positioning based on evidence.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Sorscher S et al. CEM reviews. Various; 2017-2021.",
  "Perry H et al. CEM comparative studies. Various; 2018-2022.",
  "Cozzi A et al. CEM meta-analyses. Various; 2020-2023.",
  "Fallenberg EM et al. CEM in dense breasts. Various; 2019-2022.",
 ],
 "demo_data": {"a": ("CEM sensitivity relative to MRI, percent (approx)", 95.0),
               "b": ("percent scale", 100.0), "bounds": (0.85, 1.05),
               "step1": "near-MRI sensitivity at mammography cost - the value proposition awaiting its indications",
               "confirm": "CEM wins defined indications in comparative trials",
               "refute": "MRI or tomosynthesis proves sufficient everywhere"},
},
# ------------------------------------------------------------------ rank 27
{
 "key": "whole-body-mri",
 "name": "Whole-Body MRI Screening: The Ultimate Checkup?",
 "group": "Screening",
 "ladder_rank": 27, "ladder_tier": "advanced",
 "problem": "Whole-body MRI can screen for cancer without radiation - but does finding things early in healthy people help or harm?",
 "description": "Whole-body MRI screening - offered by private clinics - finds cancers, aneurysms, and anomalies in asymptomatic people. But the benefit-harm balance is unknown: no RCT has tested it, false positives and incidentalomas are rampant, and the cancers found may include overdiagnosed ones. It's the most aggressive screening ever offered with the least evidence.",
 "background": "Whole-body MRI grew as a private-pay service in the 2010s-2020s; companies marketed it heavily. Research cohorts (German National Cohort) study it systematically. But no mortality evidence exists. As of 2026 it's a consumer product ahead of the science.",
 "why_it_matters": "Whole-body screening could be the future of early detection or the ultimate overdiagnosis machine: the evidence will decide which.",
 "sig_pointer": "The Signature system's proposed approach tests whole-body MRI like any screening, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that whole-body MRI needs screening-trial discipline: randomized evaluation of mortality benefit versus overdiagnosis harm - before it becomes standard. "
  "Assumptions: (1) trials are feasible; (2) the balance is measurable; (3) evidence will guide policy. "
  "Reasoning path: a trial-discipline model explains the current uncertainty and predicts evidence-based whole-body screening. "
  "Proposed mechanism: 'trial-validated' whole-body screening - RCT proof before widespread adoption. "
  "What would confirm it: trials showing mortality benefit exceeding harms. "
  "What would kill it: evidence of net harm from overdiagnosis. "
  "What this does not claim: it does not claim whole-body MRI helps or harms, offers no medical advice, and does not constitute a screening recommendation."),
 "sig_lens": "The Signature lens reads whole-body MRI as screening without trials, and asks what RCTs would show.",
 "how_it_works": "Researchers study whole-body MRI through research cohorts, incidentaloma tracking, and screening-trial design.",
 "key_points": [
  "Whole-body MRI finds cancers and anomalies in healthy people.",
  "No RCT has tested mortality benefit.",
  "False positives and incidentalomas are rampant.",
  "It's marketed heavily as a private-pay product.",
  "Overdiagnosis risk is the central concern.",
 ],
 "requirements": [
  "Randomized mortality trials.",
  "Overdiagnosis quantification.",
  "Benefit-harm balance established.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "German National Cohort whole-body MRI studies. Various; 2014-2022.",
  "Sohrabi S et al. Whole-body MRI reviews. Various; 2020-2023.",
  "Takahashi N et al. Whole-body screening cohorts. Various; 2018-2022.",
  "Schmidt G et al. Incidental findings in whole-body MRI. Various; 2016-2021.",
 ],
 "demo_data": {"a": ("whole-body MRI screening RCTs", 0.5),
               "b": ("private clinics offering it (approx hundreds)", 200.0), "bounds": (0.001, 0.005),
               "step1": "two hundred clinics selling what zero trials have tested - screening's evidence gap",
               "confirm": "trials show mortality benefit exceeding harms",
               "refute": "evidence shows net harm from overdiagnosis"},
},
# ------------------------------------------------------------------ rank 28
{
 "key": "radiation-therapy",
 "name": "Radiation Therapy: Precision's Limit",
 "group": "Interventions",
 "ladder_rank": 28, "ladder_tier": "advanced",
 "problem": "Radiation therapy cures cancers - but normal-tissue toxicity limits doses. What's the precision limit, and can biology widen it?",
 "description": "Radiation oncology - IMRT, SBRT, protons - delivers ever-more-precise dose distributions. But normal-tissue tolerance is the hard limit; the therapeutic ratio (tumor kill versus normal damage) improves slowly. Biological approaches (radiosensitizers, FLASH ultra-high dose rate, adaptive therapy) promise to widen it - all early-stage.",
 "background": "IMRT (2000s) and SBRT (2010s) transformed precision; protons offered Bragg-peak advantages at high cost. FLASH (2014 onward) showed normal-tissue sparing in animals with human trials early. As of 2026 physical precision is mature; biological precision is the frontier.",
 "why_it_matters": "Widening the therapeutic ratio would cure more cancers with fewer side effects: the central goal of radiation oncology.",
 "sig_pointer": "The Signature system's proposed approach treats the therapeutic ratio as biologically expandable, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that the therapeutic ratio is biologically expandable: tumor-specific radiosensitization plus normal-tissue protection - widening the gap physics alone can't. "
  "Assumptions: (1) biological widening is achievable; (2) it is targetable; (3) combinations work. "
  "Reasoning path: a biological model explains the precision plateau and predicts ratio-widening therapies. "
  "Proposed mechanism: 'ratio-widened' radiotherapy - biological sensitizers plus protectors with precise physics. "
  "What would confirm it: biological approaches improving cure rates in trials. "
  "What would kill it: evidence that the ratio is biologically fixed. "
  "What this does not claim: it does not claim any approach works, offers no medical advice, and does not constitute a treatment recommendation."),
 "sig_lens": "The Signature lens reads the precision plateau as biology's turn, and asks what would widen the ratio.",
 "how_it_works": "Researchers study the therapeutic ratio through FLASH trials, radiosensitizer research, and adaptive-therapy studies.",
 "key_points": [
  "Physical precision (IMRT, SBRT, protons) is mature.",
  "Normal-tissue tolerance is the hard limit.",
  "FLASH shows normal-tissue sparing in early research.",
  "Biological approaches are all early-stage.",
  "The therapeutic ratio improves slowly.",
 ],
 "requirements": [
  "Biological ratio-widening proven in trials.",
  "FLASH validated in humans.",
  "Tumor-specific sensitizers that work.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Favaudon V et al. FLASH radiotherapy. Science Translational Medicine. 2014;6:245ra93.",
  "Durante M et al. Charged-particle therapy reviews. Various; 2017-2021.",
  "Bentzen SM et al. Therapeutic ratio reviews. Various; 2018-2022.",
  "Vozenin MC et al. FLASH clinical translation. Various; 2019-2023.",
 ],
 "demo_data": {"a": ("radiotherapy's local control in early lung cancer, percent (approx)", 90.0),
               "b": ("percent scale", 100.0), "bounds": (0.8, 1.0),
               "step1": "nine in ten controlled where precision suffices - the remaining tenth needs biology",
               "confirm": "biological approaches improve cure rates in trials",
               "refute": "the ratio proves biologically fixed"},
},
# ------------------------------------------------------------------ rank 29
{
 "key": "imaging-biobanks",
 "name": "Imaging Biobanks: The Data Foundation",
 "group": "Data",
 "ladder_rank": 29, "ladder_tier": "advanced",
 "problem": "AI and radiomics need massive diverse imaging datasets - but biobanks are fragmented, biased, and under-shared. What would a real imaging commons look like?",
 "description": "Imaging biobanks (UK Biobank imaging, TCIA, local archives) hold millions of scans - but they're fragmented across institutions, skewed toward wealthy populations, inconsistently annotated, and hard to share (privacy, size). AI development trains on narrow data and fails broadly. The field lacks a true imaging commons.",
 "background": "UK Biobank's 100,000-scan imaging study (2014 onward) set the standard; TCIA shared cancer images. But most hospital archives are inaccessible; federated learning promises training without sharing. As of 2026 the data foundation for imaging AI is narrow and biased.",
 "why_it_matters": "Biased training data produces biased AI: the imaging commons determines whether AI helps everyone or just the well-imaged.",
 "sig_pointer": "The Signature system's proposed approach builds the imaging commons deliberately, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that the imaging commons needs deliberate construction: standardized annotation, diversity requirements, and federated infrastructure - built as shared infrastructure, not institutional accident. "
  "Assumptions: (1) coordination is achievable; (2) standards are adoptable; (3) diversity is measurable. "
  "Reasoning path: an infrastructure model explains the fragmentation and predicts a functional commons. "
  "Proposed mechanism: 'commons-built' imaging data - coordinated biobanks with diversity mandates. "
  "What would confirm it: commons-trained AI performing equitably across populations. "
  "What would kill it: evidence that institutional incentives prevent sharing. "
  "What this does not claim: it does not claim any dataset is sufficient, offers no medical advice, and does not constitute a data recommendation."),
 "sig_lens": "The Signature lens reads the data gap as unbuilt infrastructure, and asks what coordination would construct.",
 "how_it_works": "Researchers study imaging data through biobank analyses, federated-learning trials, and bias audits.",
 "key_points": [
  "Imaging biobanks are fragmented and biased.",
  "UK Biobank imaging set the standard (100,000 scans).",
  "Most hospital archives are inaccessible.",
  "AI trained on narrow data fails broadly.",
  "Federated learning promises training without sharing.",
 ],
 "requirements": [
  "Coordinated diverse imaging commons.",
  "Standardized annotation at scale.",
  "Equitable AI performance across populations.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "UK Biobank imaging study. Various; 2014-2022.",
  "Clark K et al. TCIA. Various; 2013-2020.",
  "Sheller MJ et al. Federated learning in imaging. Various; 2019-2021.",
  "Wen D et al. Imaging AI bias audits. Various; 2021-2023.",
 ],
 "demo_data": {"a": ("UK Biobank imaging participants (approx)", 100000.0),
               "b": ("hospital scans archived yearly, millions (approx)", 500.0), "bounds": (150.0, 250.0),
               "step1": "a hundred thousand shared against five hundred million locked away - the commons gap",
               "confirm": "commons-trained AI performs equitably across populations",
               "refute": "institutional incentives prove to prevent sharing"},
},
# ------------------------------------------------------------------ rank 30
{
 "key": "point-of-care",
 "name": "Point-of-Care Imaging Everywhere",
 "group": "Access",
 "ladder_rank": 30, "ladder_tier": "advanced",
 "problem": "Imaging is centralized in hospitals - but handheld ultrasound, portable X-ray, and phone-based tools could image anywhere. What blocks the decentralization?",
 "description": "Point-of-care imaging - handheld ultrasound probes, portable X-ray, smartphone attachments - can bring diagnostics to bedsides, clinics, ambulances, and villages. But quality assurance, operator training, interpretation access, and reimbursement all assume centralized radiology. The technology decentralizes; the system doesn't.",
 "background": "Handheld ultrasound (Butterfly, 2018) made probes consumer-priced; portable X-ray advanced; phone-based imaging proliferated. But most point-of-care imaging lacks radiologist oversight, quality varies, and health systems haven't integrated it. As of 2026 the tools are ready and the system isn't.",
 "why_it_matters": "Decentralized imaging would bring diagnostics to billions without radiology departments: the access transformation of the field.",
 "sig_pointer": "The Signature system's proposed approach builds the decentralized imaging system, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that point-of-care imaging needs a decentralized system: AI interpretation, remote oversight, quality assurance, and payment models designed for distributed imaging. "
  "Assumptions: (1) the components exist; (2) they integrate; (3) systems will adopt. "
  "Reasoning path: a systems model explains the tool-system gap and predicts decentralized imaging networks. "
  "Proposed mechanism: 'system-built' point-of-care imaging - integrated distributed networks. "
  "What would confirm it: decentralized networks matching centralized quality. "
  "What would kill it: evidence that quality requires centralization. "
  "What this does not claim: it does not claim decentralized imaging is ready, offers no medical advice, and does not constitute a system recommendation."),
 "sig_lens": "The Signature lens reads the decentralization gap as missing systems, and asks what integration would enable.",
 "how_it_works": "Researchers study point-of-care imaging through handheld trials, AI-interpretation studies, and integration pilots.",
 "key_points": [
  "Handheld ultrasound made probes consumer-priced.",
  "Portable X-ray and phone tools proliferated.",
  "Quality assurance assumes centralized radiology.",
  "Most point-of-care imaging lacks oversight.",
  "The tools are ready; the system isn't.",
 ],
 "requirements": [
  "Integrated decentralized imaging networks.",
  "AI interpretation matching radiologist quality.",
  "Payment models for distributed imaging.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Butterfly Network. Handheld ultrasound. 2018 onward.",
  "Nielsen K et al. Point-of-care imaging reviews. Various; 2019-2023.",
  "Baribeau Y et al. Handheld echo validation. Various; 2020-2022.",
  "Ribeiro A et al. Portable imaging in low-resource settings. Various; 2021-2023.",
 ],
 "demo_data": {"a": ("cart ultrasound cost, dollars (approx)", 50000.0),
               "b": ("handheld ultrasound probe cost, dollars (approx)", 2000.0), "bounds": (20.0, 35.0),
               "step1": "carts cost twenty-five times the handheld probe - with the system still built for the cart",
               "confirm": "decentralized networks match centralized quality",
               "refute": "quality proves to require centralization"},
},
# ------------------------------------------------------------------ rank 31
{
 "key": "molecular-imaging",
 "name": "Molecular Imaging's Full Promise",
 "group": "Nuclear Medicine",
 "ladder_rank": 31, "ladder_tier": "advanced",
 "problem": "Molecular imaging can see biology in action - but it images a handful of targets while biology has thousands. What would full coverage look like?",
 "description": "Molecular imaging - PET/SPECT tracers for specific biology - covers a tiny fraction of disease mechanisms: FDG, amyloid, PSMA, a few receptor tracers. Thousands of druggable targets, immune markers, and pathway readouts lack imaging. The gap between biology's map and imaging's map is the field's grand challenge.",
 "background": "Tracer development's economics and difficulty limit coverage; each new target needs chemistry, validation, and regulatory work. Immuno-PET (antibody tracers) expands the scope slowly. As of 2026 molecular imaging sees a few landmarks on biology's vast map.",
 "why_it_matters": "Full molecular-imaging coverage would make drug development and treatment monitoring direct: seeing the target, not inferring it.",
 "sig_pointer": "The Signature system's proposed approach systematizes target-to-tracer translation, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that target-to-tracer translation should be systematized: prioritized target lists, platform chemistry, shared validation - industrializing what is now artisanal. "
  "Assumptions: (1) systematization is feasible; (2) prioritization is possible; (3) industry will follow. "
  "Reasoning path: a systematization model explains the coverage gap and predicts broad molecular imaging. "
  "Proposed mechanism: 'industrialized' tracer translation - systematic target coverage. "
  "What would confirm it: systematic programs delivering tracers for priority targets. "
  "What would kill it: evidence that each target is irreducibly artisanal. "
  "What this does not claim: it does not claim broad coverage exists, offers no medical advice, and does not constitute a development recommendation."),
 "sig_lens": "The Signature lens reads the coverage gap as artisanal process, and asks what industrialization would deliver.",
 "how_it_works": "Researchers study molecular imaging through target-prioritization research, immuno-PET development, and translation analyses.",
 "key_points": [
  "Molecular imaging covers a handful of targets.",
  "Biology has thousands of imageable targets.",
  "Each tracer is artisanal and expensive.",
  "Immuno-PET slowly expands scope.",
  "The biology-imaging map gap is vast.",
 ],
 "requirements": [
  "Systematic target-to-tracer pipelines.",
  "Priority-target tracer delivery.",
  "Industrialized validation processes.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Gambhir SS et al. Molecular imaging roadmaps. Various; 2010-2020.",
  "van Dongen GAMS et al. Immuno-PET. Various; 2015-2021.",
  "Weber WA et al. Tracer translation reviews. Various; 2018-2023.",
  "Kraeber-Bodere F et al. Pretargeted imaging. Various; 2015-2022.",
 ],
 "demo_data": {"a": ("imaged molecular targets (approx)", 20.0),
               "b": ("druggable targets (approx)", 3000.0), "bounds": (0.004, 0.01),
               "step1": "twenty targets imaged of three thousand druggable - the map's blank spaces",
               "confirm": "systematic programs deliver tracers for priority targets",
               "refute": "each target proves irreducibly artisanal"},
},
# ------------------------------------------------------------------ rank 32
{
 "key": "imaging-genomics",
 "name": "Imaging Genomics: The Radiogenomic Map",
 "group": "Artificial Intelligence",
 "ladder_rank": 32, "ladder_tier": "advanced",
 "problem": "Can images predict a tumor's mutations? Radiogenomics says maybe - but the map from pixels to genes is mostly uncharted.",
 "description": "Radiogenomics - linking imaging features to genomic alterations - promises noninvasive mutation prediction: EGFR in lung cancer, IDH in glioma, and others show associations. But most links are weak, unvalidated, or scanner-specific. The field needs a systematic pixels-to-genes map.",
 "background": "Early radiogenomic associations (2010s) excited neuro-oncology (IDH prediction) and lung oncology (EGFR). Validation has been mixed; the TCGA-TCIA pairing enabled systematic study. As of 2026 radiogenomics has promising examples, not a map.",
 "why_it_matters": "Noninvasive mutation prediction would guide targeted therapy without biopsy: the precision-oncology shortcut.",
 "sig_pointer": "The Signature system's proposed approach builds the radiogenomic map systematically, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that radiogenomics needs systematic mapping: every common mutation tested against imaging across cancers - with prospective validation separating real links from noise. "
  "Assumptions: (1) real links exist; (2) systematic testing finds them; (3) validation is feasible. "
  "Reasoning path: a systematic model explains the example-scattered literature and predicts a usable map. "
  "Proposed mechanism: 'systematically-mapped' radiogenomics - comprehensive mutation-imaging testing. "
  "What would confirm it: validated mutation predictions guiding therapy. "
  "What would kill it: evidence that imaging-genomic links are too weak for use. "
  "What this does not claim: it does not claim any link is clinical, offers no medical advice, and does not constitute a diagnostic recommendation."),
 "sig_lens": "The Signature lens reads radiogenomics as scattered examples, and asks what systematic mapping would chart.",
 "how_it_works": "Researchers study radiogenomics through TCGA-TCIA analyses, IDH/EGFR validation studies, and systematic mapping programs.",
 "key_points": [
  "IDH and EGFR show the strongest imaging-genomic links.",
  "Most associations are weak or unvalidated.",
  "Scanner-specificity plagues the field.",
  "TCGA-TCIA pairing enabled systematic study.",
  "No comprehensive map exists.",
 ],
 "requirements": [
  "Systematic mutation-imaging testing.",
  "Prospective validation of links.",
  "Clinical-grade prediction for targetable mutations.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Aerts HJWL et al. Radiogenomics. Various; 2014-2019.",
  "Kickingereder P et al. IDH prediction. Various; 2016-2020.",
  "Rios Velazquez E et al. EGFR radiogenomics. Various; 2017-2021.",
  "Lo Gullo R et al. Radiogenomic reviews. Various; 2020-2023.",
 ],
 "demo_data": {"a": ("mutations with validated imaging prediction (approx)", 5.0),
               "b": ("actionable cancer mutations (approx)", 100.0), "bounds": (0.03, 0.08),
               "step1": "five predictable of a hundred actionable - the map's first landmarks",
               "confirm": "validated mutation predictions guide therapy",
               "refute": "imaging-genomic links prove too weak for use"},
},
# ------------------------------------------------------------------ rank 33
{
 "key": "ultrasound-therapy",
 "name": "Therapeutic Ultrasound: Sound as Treatment",
 "group": "Interventions",
 "ladder_rank": 33, "ladder_tier": "advanced",
 "problem": "Focused ultrasound can ablate tumors and open the blood-brain barrier without incisions - but where does it actually work?",
 "description": "Therapeutic ultrasound - HIFU ablation, blood-brain-barrier opening for drug delivery, neuromodulation - is incisionless treatment with striking potential. Essential tremor ablation is approved; BBB opening for Alzheimer's and brain tumors is experimental; neuromodulation is early. The field needs indication-by-indication proof.",
 "background": "HIFU fibroid treatment (2000s) proved the concept; essential-tremor thalamotomy (FDA 2016) brought it to the brain; BBB-opening trials (Lipsman, 2018 onward) target drug delivery. As of 2026 therapeutic ultrasound has approved niches and experimental frontiers.",
 "why_it_matters": "Incisionless brain treatment would transform neurology and neurosurgery: the evidence will define how far it goes.",
 "sig_pointer": "The Signature system's proposed approach proves therapeutic ultrasound indication by indication, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that therapeutic ultrasound needs indication mapping: each application (ablation, BBB opening, neuromodulation) proven separately - building the incisionless portfolio. "
  "Assumptions: (1) the physics works per indication; (2) trials are feasible; (3) mapping drives adoption. "
  "Reasoning path: an indication model explains niche status and predicts broad adoption. "
  "Proposed mechanism: 'indication-mapped' therapeutic ultrasound - proven applications portfolio. "
  "What would confirm it: mapped indications showing efficacy in trials. "
  "What would kill it: evidence that the physics limits clinical use. "
  "What this does not claim: it does not claim therapeutic ultrasound works broadly, offers no medical advice, and does not constitute a treatment recommendation."),
 "sig_lens": "The Signature lens reads the potential as unmapped, and asks which indications would prove out.",
 "how_it_works": "Researchers study therapeutic ultrasound through BBB-opening trials, ablation studies, and neuromodulation research.",
 "key_points": [
  "Essential-tremor ablation is FDA-approved.",
  "BBB opening for drug delivery is experimental.",
  "Neuromodulation is early-stage.",
  "Each application needs separate proof.",
  "Incisionless treatment is the transformative promise.",
 ],
 "requirements": [
  "Indication-by-indication trial proof.",
  "BBB-opening validated for drug delivery.",
  "A proven incisionless portfolio.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Elias WJ et al. Essential tremor HIFU. NEJM. 2016;375:730-739.",
  "Lipsman N et al. BBB opening trials. Various; 2018-2023.",
  "Tempany CMC et al. HIFU reviews. Various; 2011-2019.",
  "Blackmore J et al. Ultrasound neuromodulation. Various; 2019-2023.",
 ],
 "demo_data": {"a": ("approved therapeutic-ultrasound indications (approx)", 3.0),
               "b": ("experimental indications (approx)", 20.0), "bounds": (0.1, 0.22),
               "step1": "three approved of twenty-three explored - the incisionless frontier's early map",
               "confirm": "mapped indications show efficacy in trials",
               "refute": "the physics proves to limit clinical use"},
},
# ------------------------------------------------------------------ rank 34
{
 "key": "radiology-theory",
 "name": "A Science of Medical Imaging",
 "group": "Theory",
 "ladder_rank": 34, "ladder_tier": "advanced",
 "problem": "Radiology advances modality by modality - but is there a unified science of medical imaging, from photons to diagnosis?",
 "description": "Medical imaging lacks a unified theoretical foundation: physics, reconstruction, perception, and decision-making are separate literatures. Image perception science (Kundel, Nodine), ROC methodology, and information theory each address pieces. Whether a unified science - optimizing the entire chain from photon to diagnosis - is possible is the field's deepest question.",
 "background": "Perception science (1970s-90s) studied how radiologists see; ROC methods quantified performance; information theory was rarely applied. Each modality developed its own physics. As of 2026 the chain from photon to diagnosis is optimized piece by piece, never as a whole.",
 "why_it_matters": "A unified science would optimize imaging end-to-end: the right photons, the right reconstruction, the right reader, the right decision - as one system.",
 "sig_pointer": "The Signature system's proposed approach builds imaging science from information theory, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that medical imaging should be built on information theory: quantifying how much diagnostic information each stage preserves - and optimizing the whole chain for information per dose, per dollar, per minute. "
  "Assumptions: (1) diagnostic information is quantifiable; (2) the chain is optimizable; (3) optimization improves outcomes. "
  "Reasoning path: an information model unifies the fragmented literatures and predicts end-to-end optimized imaging. "
  "Proposed mechanism: 'information-optimized' imaging - the entire chain designed for diagnostic information efficiency. "
  "What would confirm it: optimized chains beating piecemeal ones on outcomes. "
  "What would kill it: evidence that the stages can't be jointly optimized. "
  "What this does not claim: it does not claim a unified science exists, offers no medical advice, and does not constitute a methodological recommendation."),
 "sig_lens": "The Signature lens reads imaging as an information chain, and asks what end-to-end optimization would deliver.",
 "how_it_works": "Researchers study imaging science through perception research, ROC methodology, and information-theoretic modeling.",
 "key_points": [
  "No unified theory of medical imaging exists.",
  "Perception, physics, and decision science are separate.",
  "Each modality optimizes its own piece.",
  "Information theory is rarely applied.",
  "End-to-end optimization is unattempted.",
 ],
 "requirements": [
  "Quantified diagnostic information per stage.",
  "Jointly optimized imaging chains.",
  "Outcome proof for end-to-end optimization.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Kundel HL et al. Image perception science. Various; 1978-2007.",
  "Metz CE. ROC methodology. Various; 1978-2008.",
  "Barrett HH et al. Information-theoretic imaging. Various; 2004-2015.",
  "Giger ML et al. Imaging science reviews. Various; 2018-2023.",
 ],
 "demo_data": {"a": ("imaging stages optimized jointly (approx)", 0.5),
               "b": ("imaging stages (approx)", 6.0), "bounds": (0.05, 0.15),
               "step1": "six stages, zero jointly optimized - the chain nobody designed as a whole",
               "confirm": "optimized chains beat piecemeal ones on outcomes",
               "refute": "the stages prove unable to be jointly optimized"},
},
]