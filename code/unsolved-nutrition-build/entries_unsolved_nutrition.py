#!/usr/bin/env python3
"""Entries for The Unsolved Nutrition Database (unsolved-nutrition) and its
Signature half (unsolved-nutrition-signature).

34 famous unsolved problems in nutrition science, ladder-ordered by accessibility
(rank 1 = most approachable, rank 34 = most complex/compounded).
Public half: real, fact-checked problems. Signature half: the same 34
problems through the Signature lens, with Signature-generated proposed
solutions that are ALWAYS labeled as proposals, never established science.

Honesty rule (enforced in every record): never claim proof, never imply
peer acceptance, never present speculation as settled. Signature proposals
are labeled speculation for research discussion only - never dietary or
medical advice, never a recommendation; no dosages, no cure claims.
"""

LABEL = "Signature-generated proposed solution \u2014 not established science."

SIG_TAIL = ("Signature editions carry the Signature system's proposed "
            "solution approaches to famous unsolved problems. Every "
            "solution is labeled a Signature-generated proposal, never "
            "established science, never peer-accepted, never proof, never "
            "dietary or medical advice.")

STD_COMMON = [
    "Problem statements verified against the published nutrition literature; open status confirmed as of 2026.",
    "Signature solution sections are labeled proposals: they state assumptions, a reasoning path, a proposed mechanism, what would confirm or kill them, and what they do not claim.",
    "Signature proposals are labeled speculation for research discussion only - never dietary or medical advice, never a recommendation; no dosages and no cure claims appear.",
]

ENTRIES = [
# ------------------------------------------------------------------ rank 1
{
 "key": "optimal-diet",
 "name": "What Is the Optimal Human Diet?",
 "group": "Dietary Patterns",
 "ladder_rank": 1, "ladder_tier": "foundations",
 "problem": "Low-fat, low-carb, Mediterranean, plant-based - every diet has champions and trials, yet no consensus on the optimal human diet exists. Why?",
 "description": "Nutrition's central question has no answer: randomized trials of dietary patterns show modest differences, observational studies conflict, and individual responses vary enormously. The field cannot say what humans should eat - only what they shouldn't (trans fats, excess added sugar, extreme deficiency). The optimal diet may not exist as a single pattern.",
 "background": "The diet-heart hypothesis (Keys, 1950s-70s) drove low-fat guidance; the obesity epidemic drove low-carb counter-movements; PREDIMED (2013/2018) supported Mediterranean patterns. But effect sizes are small, adherence dominates outcomes, and precision-nutrition studies (ZOE PREDICT) show huge individual variation in identical meals. As of 2026 no dietary pattern has proven optimal.",
 "why_it_matters": "Diet drives the global burden of chronic disease: an evidence-based optimal diet - or proof it doesn't exist - would reshape guidelines, industry, and health.",
 "sig_pointer": "The Signature system's proposed approach treats optimal diet as an individual-matching problem, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that there is no single optimal diet: the optimum is individual, determined by genetics, microbiome, metabolism, and context - and the solvable problem is matching, not ranking diets. "
  "Assumptions: (1) individual optima differ meaningfully; (2) they are predictable from measurable biology; (3) matching beats any universal pattern. "
  "Reasoning path: a matching model explains why pattern trials show small differences - each pattern is optimal for a subset - and predicts personalized nutrition. "
  "Proposed mechanism: 'diet-matched' nutrition - predicting individual responses to dietary patterns from biology. "
  "What would confirm it: matched diets outperforming best-pattern diets in randomized trials. "
  "What would kill it: evidence that individual variation is noise, not predictable biology. "
  "What this does not claim: it does not claim any diet is optimal, offers no dietary advice, and does not constitute medical advice."),
 "sig_lens": "The Signature lens reads the diet wars as a matching problem, and asks what biology would match each person to their diet.",
 "how_it_works": "Researchers study optimal diet through pattern trials, precision-nutrition cohorts, and individual-response prediction.",
 "key_points": [
  "No dietary pattern has proven optimal in trials.",
  "Effect sizes between patterns are small.",
  "Individual responses to identical meals vary enormously.",
  "Adherence often dominates the dietary pattern itself.",
  "The optimum may be individual, not universal.",
 ],
 "requirements": [
  "Predictable individual diet-response biology.",
  "Matched diets beating best-pattern diets in trials.",
  "Proof that variation is signal, not noise.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Keys A et al. Seven Countries Study. Various; 1958-1980.",
  "Estruch R et al. PREDIMED trial. NEJM. 2013;368:1279-1290; retracted and republished 2018.",
  "Berry SE et al. ZOE PREDICT studies. Nature Medicine. 2020;26:964-973.",
  "Gardner CD et al. DIETFITS trial. JAMA. 2018;319:667-679.",
 ],
 "demo_data": {"a": ("dietary patterns with proven optimality", 0.5),
               "b": ("major dietary patterns debated (approx)", 8.0), "bounds": (0.03, 0.12),
               "step1": "eight major patterns debated, zero proven optimal - nutrition's central question unanswered",
               "confirm": "matched diets beat best-pattern diets in randomized trials",
               "refute": "individual variation proves to be noise"},
},
# ------------------------------------------------------------------ rank 2
{
 "key": "saturated-fat",
 "name": "Saturated Fat: Villain, Neutral, or Misunderstood?",
 "group": "Macronutrients",
 "ladder_rank": 2, "ladder_tier": "foundations",
 "problem": "Decades of guidance demonized saturated fat, yet recent meta-analyses find weak links to heart disease. What is saturated fat's real role?",
 "description": "Saturated fat - butter, red meat, coconut oil - was nutrition's chief villain after the diet-heart hypothesis. But meta-analyses (Siri-Tarino 2010, de Souza 2015) found no strong association with cardiovascular disease; the PURE study complicated the picture further. The field is split: replacement-nutrient effects, food-matrix effects, and LDL-subfraction debates keep the question open.",
 "background": "Keys' Seven Countries Study (1958-70s) linked saturated fat to heart disease; guidelines capped it at 10% of calories. Challenges accumulated: meta-analyses showing weak associations, the food-matrix concept (cheese versus butter), and Mendelian randomization studies. As of 2026 guidelines still limit saturated fat while the evidence base is contested.",
 "why_it_matters": "Saturated fat guidance shapes global food policy and trillions in food spending: getting it right matters enormously, and getting it wrong has already cost decades.",
 "sig_pointer": "The Signature system's proposed approach treats saturated fat as a food-matrix question, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that 'saturated fat' is the wrong unit: the health effect lives in the food matrix (cheese, yogurt, meat, oil), not the fatty-acid category - and matrix-level evidence will resolve the debate. "
  "Assumptions: (1) matrix effects are real and large; (2) they are measurable; (3) they explain the conflicting evidence. "
  "Reasoning path: a matrix model explains why dairy saturated fat looks neutral while processed-meat fat looks harmful, predicting matrix-specific guidance. "
  "Proposed mechanism: 'matrix-typed' fat guidance - recommendations by food source, not fatty-acid class. "
  "What would confirm it: matrix-specific trials showing divergent effects of equal saturated-fat doses. "
  "What would kill it: evidence that the fatty-acid category predicts outcomes regardless of source. "
  "What this does not claim: it does not claim saturated fat is safe or harmful, offers no dietary advice, and does not constitute medical advice."),
 "sig_lens": "The Signature lens reads the fat debate as miscategorized, and asks what food-level evidence would settle it.",
 "how_it_works": "Researchers study saturated fat through replacement-nutrient analyses, food-matrix trials, and LDL-subfraction research.",
 "key_points": [
  "Meta-analyses find weak saturated fat-CVD links.",
  "Guidelines still cap saturated fat at ~10% of calories.",
  "Food-matrix effects may explain conflicting evidence.",
  "Replacement nutrients change the comparison entirely.",
  "The field is split with no resolution in sight.",
 ],
 "requirements": [
  "Matrix-specific trial evidence.",
  "Proof that matrix beats fatty-acid category as predictor.",
  "Guidance reform based on food-level data.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Siri-Tarino PW et al. Meta-analysis of saturated fat and CVD. American Journal of Clinical Nutrition. 2010;91:535-546.",
  "de Souza RJ et al. Intake of saturated and trans fats and health outcomes. BMJ. 2015;351:h3978.",
  "Dehghan M et al. PURE study. Lancet. 2017;390:2050-2062.",
  "Astrup A et al. Saturated fats and health: food matrix. Various; 2019-2020.",
 ],
 "demo_data": {"a": ("decades of saturated-fat guidance (approx)", 6.0),
               "b": ("decades scale", 10.0), "bounds": (0.45, 0.75),
               "step1": "sixty years of guidance on evidence now contested - the costliest maybe-mistake in nutrition",
               "confirm": "matrix-specific trials show divergent effects of equal saturated-fat doses",
               "refute": "fatty-acid category proves predictive regardless of source"},
},
# ------------------------------------------------------------------ rank 3
{
 "key": "ultra-processed",
 "name": "Ultra-Processed Foods: What Makes Them Harmful?",
 "group": "Food Processing",
 "ladder_rank": 3, "ladder_tier": "foundations",
 "problem": "Ultra-processed foods are linked to obesity and disease - but is it the processing, the nutrients, the additives, or the eating behavior?",
 "description": "NOVA-classified ultra-processed foods (UPFs) - formulations with additives, refined ingredients - are strongly associated with obesity, diabetes, and mortality in observational studies. Hall's 2019 inpatient RCT proved UPF diets cause overeating versus unprocessed diets. But the mechanism is unknown: energy density, hyper-palatability, additives, food structure, eating rate, or gut-brain effects could each be responsible.",
 "background": "NOVA (Monteiro, 2009) defined the category; observational links accumulated through the 2010s. Hall's NIH trial (2019) provided the first causal evidence: matched nutrients, yet UPF caused +500 kcal/day overeating. Mechanistic work since has tested additives, textures, and eating rate without isolating the cause. As of 2026 the association is causal but the mechanism is not.",
 "why_it_matters": "UPFs dominate calories in rich countries: identifying the harmful mechanism would enable targeted reformulation or regulation instead of blanket avoidance.",
 "sig_pointer": "The Signature system's proposed approach decomposes ultra-processing into testable mechanisms, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that 'ultra-processed' bundles several mechanisms - eating rate, energy density, additive effects, structure loss - and each needs separate testing and separate policy. "
  "Assumptions: (1) the mechanisms are separable; (2) each contributes; (3) decomposition enables targeted action. "
  "Reasoning path: a decomposition model explains why the category is so robustly harmful and predicts mechanism-specific interventions. "
  "Proposed mechanism: 'mechanism-decomposed' UPF research - isolating eating rate, density, additives, and structure in factorial trials. "
  "What would confirm it: decomposed trials attributing the overeating effect to specific mechanisms. "
  "What would kill it: evidence that processing has a single irreducible harmful property. "
  "What this does not claim: it does not claim any mechanism is proven, offers no dietary advice, and does not constitute medical advice."),
 "sig_lens": "The Signature lens reads ultra-processing as several harms in one label, and asks what each contributes.",
 "how_it_works": "Researchers study UPFs through inpatient feeding trials, additive studies, and eating-behavior research.",
 "key_points": [
  "UPF diets cause +500 kcal/day overeating in RCT (Hall 2019).",
  "Observational links to obesity, diabetes, mortality are strong.",
  "The mechanism - processing, nutrients, additives, behavior - is unknown.",
  "NOVA defined the category in 2009.",
  "Decomposition would enable targeted policy.",
 ],
 "requirements": [
  "Factorial trials isolating each mechanism.",
  "Attribution of the overeating effect.",
  "Mechanism-targeted reformulation or regulation.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Monteiro CA et al. NOVA classification. Various; 2009-2019.",
  "Hall KD et al. Ultra-processed diets cause excess calorie intake. Cell Metabolism. 2019;30:67-77.",
  "Lane MM et al. UPF and health outcomes umbrella reviews. Various; 2021-2024.",
  "Elizabeth L et al. UPF mechanisms. Various; 2020-2023.",
 ],
 "demo_data": {"a": ("excess calories on UPF diet, kcal/day (approx)", 500.0),
               "b": ("kcal scale (thousands)", 1000.0), "bounds": (0.35, 0.65),
               "step1": "five hundred extra calories daily from processing alone - with the mechanism unknown",
               "confirm": "decomposed trials attribute the overeating to specific mechanisms",
               "refute": "processing proves to have one irreducible harmful property"},
},
# ------------------------------------------------------------------ rank 4
{
 "key": "vitamin-d",
 "name": "Vitamin D: How Much, and Does It Matter?",
 "group": "Micronutrients",
 "ladder_rank": 4, "ladder_tier": "foundations",
 "problem": "Vitamin D deficiency is linked to everything - yet supplementation trials keep failing. Does vitamin D matter beyond bones?",
 "description": "Observational studies link low vitamin D to cancer, heart disease, depression, COVID-19 severity, and mortality. But large RCTs (VITAL, D2d) show supplementation doesn't prevent these outcomes. The field is stuck: either deficiency is a marker of ill health (reverse causation, confounding), or trials dosed wrong, measured wrong, or enrolled the wrong people.",
 "background": "Vitamin D's bone role is settled; the extra-skeletal claims exploded in the 2000s-2010s. VITAL (2019, 25,000 participants) found no cancer/CVD benefit. Mendelian randomization studies largely support the null. Defenders argue trials didn't target true deficiency. As of 2026 the extra-skeletal debate is unresolved with the null leading.",
 "why_it_matters": "Billions take vitamin D supplements: resolving the question would end one of the largest uncontrolled experiments in public health.",
 "sig_pointer": "The Signature system's proposed approach tests vitamin D only in true deficiency, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that vitamin D trials failed by enrolling the sufficient: supplementation can only help the truly deficient, and trials diluted them with replete participants. "
  "Assumptions: (1) true deficiency is harmful beyond bones; (2) it is identifiable; (3) correcting it helps. "
  "Reasoning path: a deficiency-only model explains observational links and null trials, predicting positive trials in the truly deficient. "
  "Proposed mechanism: 'deficiency-targeted' vitamin D trials - enrolling only the severely deficient. "
  "What would confirm it: positive outcomes in truly deficient trial populations. "
  "What would kill it: null results even in severe deficiency. "
  "What this does not claim: it does not claim supplementation helps, offers no supplement advice, and does not constitute medical advice."),
 "sig_lens": "The Signature lens reads the null trials as diluted, and asks what deficiency-only testing would show.",
 "how_it_works": "Researchers study vitamin D through VITAL-style mega-trials, Mendelian randomization, and deficiency-targeted designs.",
 "key_points": [
  "Observational links span cancer, CVD, depression, mortality.",
  "VITAL (25,000 participants) found no cancer/CVD benefit.",
  "Mendelian randomization largely supports the null.",
  "Defenders argue trials missed true deficiency.",
  "The bone role is settled; everything else is contested.",
 ],
 "requirements": [
  "Trials restricted to true deficiency.",
  "Positive results where the model predicts them.",
  "Or acceptance of the null for extra-skeletal effects.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Manson JE et al. VITAL trial. NEJM. 2019;380:33-44.",
  "Autier P et al. Vitamin D status and ill health: systematic review. Lancet Diabetes & Endocrinology. 2014;2:76-89.",
  "Rejnmark L et al. Vitamin D Mendelian randomization. Various; 2017-2022.",
  "Scragg R et al. Vitamin D trial reviews. Various; 2018-2023.",
 ],
 "demo_data": {"a": ("VITAL participants (approx)", 25000.0),
               "b": ("participants scale (hundred-thousands)", 100000.0), "bounds": (0.15, 0.35),
               "step1": "twenty-five thousand participants, null result - the largest test of the sunshine vitamin failed",
               "confirm": "positive outcomes in truly deficient trial populations",
               "refute": "null results persist even in severe deficiency"},
},
# ------------------------------------------------------------------ rank 5
{
 "key": "fiber",
 "name": "Fiber: How Much Do We Need, and Which Kind?",
 "group": "Macronutrients",
 "ladder_rank": 5, "ladder_tier": "foundations",
 "problem": "Fiber is nutrition's most consistently beneficial nutrient - yet optimal dose, type, and mechanism remain undefined.",
 "description": "Dietary fiber - the indigestible carbohydrate fraction - is linked to lower mortality, heart disease, diabetes, and colorectal cancer in massive meta-analyses (Reynolds 2019). But which fibers (soluble, insoluble, fermentable), what dose, and through which mechanisms (microbiome, short-chain fatty acids, glycemic effects) remain open. Ancestral intakes (~100g/day) dwarf modern ones (~15g/day) without a defined target.",
 "background": "Burkitt's fiber hypothesis (1970s) launched the field; the definition and measurement of fiber evolved for decades. Reynolds' 2019 Lancet meta-analysis cemented the mortality benefit. Microbiome research reframed fiber as microbial food. But dose-response, fiber-type specificity, and individual variation are unmapped. As of 2026 guidance says 'more' without saying how much or which.",
 "why_it_matters": "Fiber is the cheapest, safest intervention in nutrition: defining the optimal fiber prescription would be public health's easiest win.",
 "sig_pointer": "The Signature system's proposed approach treats fiber as microbial nutrition to be prescribed by type, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that fiber's benefits flow through the microbiome: different fibers feed different microbes producing different metabolites, and the prescription should be fiber-type matched to the individual's microbiome. "
  "Assumptions: (1) fiber-type effects differ; (2) microbiomes differ in fiber response; (3) matching improves outcomes. "
  "Reasoning path: a microbial model explains fiber's broad benefits and predicts personalized fiber prescriptions. "
  "Proposed mechanism: 'microbiome-matched' fiber guidance - prescribing fiber types by individual microbial ecology. "
  "What would confirm it: matched fiber types outperforming generic 'more fiber' in trials. "
  "What would kill it: evidence that fiber effects are purely mechanical (bulk, glycemic) with no microbial specificity. "
  "What this does not claim: it does not claim a fiber prescription exists, offers no dietary advice, and does not constitute medical advice."),
 "sig_lens": "The Signature lens reads fiber as food for microbes, and asks which fibers feed which people.",
 "how_it_works": "Researchers study fiber through dose-response meta-analyses, microbiome feeding trials, and SCFA mechanism research.",
 "key_points": [
  "Fiber is linked to lower mortality across massive meta-analyses.",
  "Ancestral intakes (~100g) dwarf modern ones (~15g).",
  "Optimal dose and fiber type are undefined.",
  "The microbiome reframes fiber as microbial food.",
  "Guidance says 'more' without specifics.",
 ],
 "requirements": [
  "Fiber-type-specific dose-response data.",
  "Microbiome-matched prescriptions proven superior.",
  "Mechanistic proof via SCFA and microbial pathways.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Reynolds A et al. Carbohydrate quality and health. Lancet. 2019;393:434-445.",
  "Burkitt DP. Fiber hypothesis. Various; 1971-1979.",
  "Deehan EC, Walter J. Fiber and the microbiome. Various; 2016-2021.",
  "Veronese N et al. Fiber meta-analyses. Various; 2018-2022.",
 ],
 "demo_data": {"a": ("modern fiber intake, g/day (approx)", 15.0),
               "b": ("ancestral fiber intake, g/day (approx)", 100.0), "bounds": (0.1, 0.22),
               "step1": "fifteen grams against a hundred ancestral - the largest dietary deficit, the vaguest prescription",
               "confirm": "matched fiber types beat generic 'more fiber' in trials",
               "refute": "fiber effects prove purely mechanical"},
},
# ------------------------------------------------------------------ rank 6
{
 "key": "red-meat",
 "name": "Red Meat and Health: How Strong Is the Evidence?",
 "group": "Foods",
 "ladder_rank": 6, "ladder_tier": "foundations",
 "problem": "Red meat is linked to cancer and heart disease in observational studies - but the absolute risks are small and the evidence is contested. What's the truth?",
 "description": "Red and processed meat carry IARC classifications (processed meat Group 1, red meat Group 2A) and observational links to colorectal cancer and cardiovascular disease. But absolute risk increases are small, the evidence is observational and confounded (healthy-user bias), and the NutriRECS consortium (2019) controversially concluded the evidence was too weak to recommend reduction. The field remains polarized.",
 "background": "Observational links accumulated from the 1990s-2000s; IARC's 2015 classification ignited public debate. NutriRECS (2019, Annals of Internal Medicine) applied GRADE methodology and found low-certainty evidence, recommending no change - provoking outrage and debate about evidence standards. As of 2026 the polarization persists with no resolution.",
 "why_it_matters": "Red meat guidance affects global agriculture, culture, and diet: the evidence-standard debate here sets the template for all nutritional epidemiology.",
 "sig_pointer": "The Signature system's proposed approach separates processed from unprocessed and dose from pattern, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that the red-meat debate conflates distinct questions - processed versus unprocessed, dose, dietary context - and each needs separate absolute-risk answers. "
  "Assumptions: (1) the questions are separable; (2) absolute risks are the right metric; (3) separation resolves the polarization. "
  "Reasoning path: a separation model explains why both sides cite real evidence and predicts consensus on disaggregated questions. "
  "Proposed mechanism: 'disaggregated' red-meat evidence - separate verdicts for processed, unprocessed, dose levels, and contexts. "
  "What would confirm it: disaggregated analyses producing stable, agreed estimates. "
  "What would kill it: evidence that the categories can't be separated epidemiologically. "
  "What this does not claim: it does not claim red meat is safe or harmful, offers no dietary advice, and does not constitute medical advice."),
 "sig_lens": "The Signature lens reads the meat war as bundled questions, and asks what unbundling would settle.",
 "how_it_works": "Researchers study red meat through GRADE evidence reviews, absolute-risk modeling, and processed-versus-unprocessed analyses.",
 "key_points": [
  "IARC classifies processed meat Group 1, red meat Group 2A.",
  "Absolute risk increases are small.",
  "NutriRECS (2019) found low-certainty evidence, provoking outrage.",
  "Healthy-user bias confounds observational studies.",
  "The field is polarized with no resolution.",
 ],
 "requirements": [
  "Disaggregated absolute-risk estimates.",
  "Agreed evidence standards for nutrition.",
  "Separation of processed from unprocessed effects.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Bouvard V et al. IARC red/processed meat evaluation. Lancet Oncology. 2015;16:1599-1600.",
  "Johnston BC et al. NutriRECS red meat guidelines. Annals of Internal Medicine. 2019;171:756-764.",
  "Wolk A. Red meat and health meta-analyses. Various; 2017-2020.",
  "Qian F et al. Red meat and CVD. Various; 2020-2023.",
 ],
 "demo_data": {"a": ("absolute colorectal-cancer risk increase from red meat, percent (approx)", 1.0),
               "b": ("percent scale", 100.0), "bounds": (0.005, 0.02),
               "step1": "a one-percentage-point absolute risk debated as fiercely as any question in nutrition",
               "confirm": "disaggregated analyses produce stable, agreed estimates",
               "refute": "the categories prove inseparable epidemiologically"},
},
# ------------------------------------------------------------------ rank 7
{
 "key": "salt",
 "name": "Salt: How Low Should We Go?",
 "group": "Micronutrients",
 "ladder_rank": 7, "ladder_tier": "foundations",
 "problem": "Salt raises blood pressure, but aggressive reduction shows a J-curve in some studies - is there an optimal sodium intake, and does it vary by person?",
 "description": "Sodium reduction lowers blood pressure (DASH-Sodium proved it), and guidelines urge <2,300 mg/day. But observational studies (PURE) suggest very low intakes may raise cardiovascular risk - a J-curve - and the effect varies by hypertension status, age, and potassium intake. The field debates whether universal reduction or targeted reduction is right.",
 "background": "The salt-BP link was established by INTERSALT (1988) and DASH-Sodium (2001). The J-curve emerged in PURE (2014-2018) and was fiercely contested (methodological critiques of spot-urine sodium). Salt-sensitivity genetics suggests individual variation. As of 2026 guidelines push reduction while the J-curve debate simmers.",
 "why_it_matters": "Sodium policy affects every processed food: the optimal intake determines whether universal reduction helps or harms.",
 "sig_pointer": "The Signature system's proposed approach treats sodium optimum as individual, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that sodium's optimal intake is individual: salt-sensitive hypertensives benefit from reduction while others may not, and the J-curve reflects mixing these populations. "
  "Assumptions: (1) salt sensitivity varies; (2) it is measurable; (3) targeted reduction beats universal. "
  "Reasoning path: an individual-optimum model explains both DASH-Sodium and the J-curve, predicting stratified sodium guidance. "
  "Proposed mechanism: 'sensitivity-typed' sodium guidance - reduction targeted to the salt-sensitive. "
  "What would confirm it: stratified trials showing benefit only in the sensitive. "
  "What would kill it: evidence that universal reduction benefits everyone equally. "
  "What this does not claim: it does not claim any sodium level is optimal, offers no dietary advice, and does not constitute medical advice."),
 "sig_lens": "The Signature lens reads the salt debate as mixed populations, and asks what stratification would resolve it.",
 "how_it_works": "Researchers study sodium through DASH-Sodium-style trials, PURE cohort analyses, and salt-sensitivity genetics.",
 "key_points": [
  "DASH-Sodium proved reduction lowers blood pressure.",
  "PURE suggests very low intakes may raise risk (J-curve).",
  "Effects vary by hypertension status and potassium.",
  "Salt sensitivity appears partly genetic.",
  "Universal versus targeted reduction is debated.",
 ],
 "requirements": [
  "Measurable salt-sensitivity typing.",
  "Stratified trials of sodium reduction.",
  "Resolution of the J-curve with better sodium measurement.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Sacks FM et al. DASH-Sodium trial. NEJM. 2001;344:3-10.",
  "Mente A et al. PURE sodium analyses. NEJM. 2014;371:601-611; Lancet. 2018;392:496-506.",
  "Intersalt Cooperative Research Group. INTERSALT. BMJ. 1988;297:319-328.",
  "Graudal N et al. Sodium and health outcomes reviews. Various; 2014-2020.",
 ],
 "demo_data": {"a": ("guideline sodium limit, mg/day (approx)", 2300.0),
               "b": ("average intake, mg/day (approx)", 3400.0), "bounds": (0.55, 0.8),
               "step1": "guidelines say 2,300 against 3,400 consumed - with the optimal level itself disputed",
               "confirm": "stratified trials show benefit only in the salt-sensitive",
               "refute": "universal reduction proves beneficial for everyone"},
},
# ------------------------------------------------------------------ rank 8
{
 "key": "breakfast",
 "name": "Does Breakfast Matter?",
 "group": "Meal Timing",
 "ladder_rank": 8, "ladder_tier": "foundations",
 "problem": "'Breakfast is the most important meal' - but the evidence is observational, and skipping it is now a diet strategy. Does breakfast actually matter?",
 "description": "Breakfast-eating is associated with leanness and health in observational studies - but breakfast skippers differ in countless ways, and the few RCTs show little effect of assignment to eat or skip. Intermittent fasting made skipping fashionable. The field cannot say whether breakfast matters or the association is pure confounding.",
 "background": "The breakfast-health association was epidemiological conventional wisdom for decades. RCTs in the 2010s (Dhurandhar, Betts) found minimal causal effects. Chrono-nutrition research suggests timing matters but not necessarily breakfast per se. As of 2026 the most famous meal advice in nutrition rests on confounded evidence.",
 "why_it_matters": "Breakfast advice reaches every schoolchild: if it's wrong, it's the most widely repeated error in nutrition guidance.",
 "sig_pointer": "The Signature system's proposed approach treats meal timing as circadian alignment, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that breakfast's benefit is circadian alignment, not the meal: eating in sync with biological rhythms matters, and breakfast is one alignment strategy among several. "
  "Assumptions: (1) circadian alignment drives the benefit; (2) it is achievable with or without breakfast; (3) alignment is measurable. "
  "Reasoning path: an alignment model explains the observational association and null RCTs, predicting timing-based guidance. "
  "Proposed mechanism: 'circadian-aligned' eating guidance - timing meals to biological rhythms rather than mandating breakfast. "
  "What would confirm it: alignment-matched trials beating breakfast-mandate trials. "
  "What would kill it: evidence that breakfast has benefits independent of timing. "
  "What this does not claim: it does not claim breakfast is unimportant, offers no dietary advice, and does not constitute medical advice."),
 "sig_lens": "The Signature lens reads breakfast as a clock question, and asks what timing would optimize.",
 "how_it_works": "Researchers study breakfast through eating-timing RCTs, chrono-nutrition research, and confounding analyses.",
 "key_points": [
  "Breakfast-health links are observational and confounded.",
  "RCTs of assigned breakfast eating show minimal effects.",
  "Intermittent fasting made skipping a strategy.",
  "Chrono-nutrition suggests timing matters.",
  "The famous advice may be nutrition's widest-repeated error.",
 ],
 "requirements": [
  "Circadian-alignment trials versus breakfast mandates.",
  "Proof that timing, not breakfast per se, drives benefits.",
  "Individual chronotype-matched eating guidance.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Dhurandhar EJ et al. Breakfast RCTs. American Journal of Clinical Nutrition. 2014;100:507-513.",
  "Betts JA et al. Bath Breakfast Project. American Journal of Clinical Nutrition. 2014;100:539-547.",
  "Flanagan A et al. Chrono-nutrition reviews. Various; 2020-2023.",
  "Sievert K et al. Breakfast meta-analyses. Various; 2019-2021.",
 ],
 "demo_data": {"a": ("RCTs showing causal breakfast benefit (approx)", 1.0),
               "b": ("observational studies linking breakfast to health (approx)", 100.0), "bounds": (0.005, 0.02),
               "step1": "a hundred observational studies, essentially zero causal trials - the most famous advice, the thinnest proof",
               "confirm": "alignment-matched trials beat breakfast-mandate trials",
               "refute": "breakfast proves beneficial independent of timing"},
},
# ------------------------------------------------------------------ rank 9
{
 "key": "organic",
 "name": "Is Organic Food Healthier?",
 "group": "Food Systems",
 "ladder_rank": 9, "ladder_tier": "foundations",
 "problem": "Organic food commands premium prices on health claims - but is there evidence it's healthier, or is it marketing with a halo?",
 "description": "Organic foods - grown without synthetic pesticides/fertilizers - show small nutritional differences (some antioxidants, omega-3s in dairy) but no proven health benefit in human trials. Pesticide-residue exposure is lower, but whether residues at conventional levels harm health is itself unproven. The field cannot justify the health premium with evidence.",
 "background": "Nutritional comparisons (Dangour 2009, Baranski 2014) found modest differences; health-outcome studies are observational and confounded (organic buyers are healthier in every way). The pesticide-health link at dietary doses remains unproven. As of 2026 organic's health case rests on absence of evidence of harm from conventional, not evidence of benefit.",
 "why_it_matters": "Consumers spend billions on organic premiums: the evidence question determines whether that's health investment or marketing transfer.",
 "sig_pointer": "The Signature system's proposed approach tests organic's claims by mechanism, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that organic's health question decomposes: pesticide-avoidance, nutritional differences, and environmental benefits are separate claims needing separate evidence. "
  "Assumptions: (1) the claims are separable; (2) each is testable; (3) decomposition ends the halo debate. "
  "Reasoning path: a decomposition model explains why the debate never resolves - each side argues a different claim - and predicts claim-specific verdicts. "
  "Proposed mechanism: 'claim-separated' organic evidence - independent verdicts on residues, nutrition, and environment. "
  "What would confirm it: separated trials giving clear per-claim answers. "
  "What would kill it: evidence that the claims can't be separated in real diets. "
  "What this does not claim: it does not claim organic is or isn't healthier, offers no dietary advice, and does not constitute medical advice."),
 "sig_lens": "The Signature lens reads the organic debate as bundled claims, and asks what each claim's evidence shows.",
 "how_it_works": "Researchers study organic through residue biomonitoring, nutritional comparisons, and confound-controlled cohorts.",
 "key_points": [
  "Nutritional differences between organic and conventional are small.",
  "No human trial proves organic health benefits.",
  "Pesticide residues are lower; harm at conventional levels unproven.",
  "Organic buyers confound observational studies.",
  "The premium lacks an evidence-based health justification.",
 ],
 "requirements": [
  "Claim-separated trial evidence.",
  "Residue-harm assessment at dietary doses.",
  "Honest labeling of which claims have evidence.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Dangour AD et al. Nutritional quality of organic foods: systematic review. American Journal of Clinical Nutrition. 2009;90:680-685.",
  "Baranski M et al. Higher antioxidant concentrations in organic crops. British Journal of Nutrition. 2014;112:794-811.",
  "Smith-Spangler C et al. Organic foods and health: systematic review. Annals of Internal Medicine. 2012;157:348-366.",
  "Mie A et al. Pesticide residues and health. Various; 2017-2022.",
 ],
 "demo_data": {"a": ("human trials proving organic health benefit", 0.5),
               "b": ("organic price premium, percent (approx)", 50.0), "bounds": (0.005, 0.02),
               "step1": "a fifty-percent premium with zero proving trials - the halo without the evidence",
               "confirm": "separated trials give clear per-claim answers",
               "refute": "the claims prove inseparable in real diets"},
},
# ------------------------------------------------------------------ rank 10
{
 "key": "supplements",
 "name": "Do Supplements Work?",
 "group": "Micronutrients",
 "ladder_rank": 10, "ladder_tier": "foundations",
 "problem": "Half of adults take supplements, yet trials show most do nothing - why the gap between belief and evidence?",
 "description": "Multivitamins, antioxidants, and most supplements show no benefit in large RCTs (Physicians' Health Study II, SELECT) and occasional harm (beta-carotene and lung cancer, vitamin E and prostate cancer). Yet use grows. The field debates whether supplements fail because users aren't deficient, doses are wrong, or the whole paradigm - isolated nutrients versus food - is flawed.",
 "background": "Linus Pauling's vitamin C claims launched the supplement era; the antioxidant hypothesis drove massive trials. SELECT (2008-2011) and PHS II (2012) delivered nulls and harms. Defenders argue trials enrolled the replete. As of 2026 the evidence says: correct true deficiency, otherwise little benefit - but the industry thrives regardless.",
 "why_it_matters": "Supplements are a $150B+ industry built largely on unproven claims: the evidence gap is consumer protection's biggest nutrition failure.",
 "sig_pointer": "The Signature system's proposed approach treats supplements as deficiency-correction tools, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that supplements are deficiency-correction tools being sold as enhancement: they work where deficiency exists and can't work where it doesn't. "
  "Assumptions: (1) deficiencies are common enough to matter; (2) they are identifiable; (3) correction helps. "
  "Reasoning path: a deficiency model explains null trials (replete participants) and predicts targeted supplementation success. "
  "Proposed mechanism: 'deficiency-tested' supplementation - testing before supplementing, treating only real gaps. "
  "What would confirm it: deficiency-targeted trials showing clear benefits. "
  "What would kill it: evidence that even true deficiencies don't benefit from correction. "
  "What this does not claim: it does not claim supplements are useless or useful, offers no supplement advice, and does not constitute medical advice."),
 "sig_lens": "The Signature lens reads the supplement paradox as mistargeting, and asks what test-then-treat would show.",
 "how_it_works": "Researchers study supplements through mega-trials, deficiency-targeted designs, and harm surveillance.",
 "key_points": [
  "PHS II and SELECT showed nulls and occasional harms.",
  "Beta-carotene raised lung-cancer risk in smokers.",
  "Half of adults take supplements anyway.",
  "The industry is $150B+ on largely unproven claims.",
  "Deficiency correction is the evidence-based use case.",
 ],
 "requirements": [
  "Deficiency-targeted trials with clear benefits.",
  "Testing infrastructure for real gaps.",
  "Regulation matching claims to evidence.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Sesso HD et al. Physicians' Health Study II. JAMA. 2012;308:1751-1760.",
  "Lippman SM et al. SELECT trial. JAMA. 2009;301:39-51.",
  "Omenn GS et al. Beta-carotene and lung cancer (CARET). NEJM. 1996;334:1150-1155.",
  "Manson JE et al. Supplement reviews. Various; 2013-2022.",
 ],
 "demo_data": {"a": ("supplement industry, billions of dollars (approx)", 150.0),
               "b": ("billions scale", 1000.0), "bounds": (0.1, 0.22),
               "step1": "a $150 billion industry on evidence that mostly says 'no benefit' - belief versus data",
               "confirm": "deficiency-targeted trials show clear benefits",
               "refute": "even true deficiencies prove unhelped by correction"},
},
# ------------------------------------------------------------------ rank 11
{
 "key": "calories",
 "name": "Is a Calorie a Calorie?",
 "group": "Energy Balance",
 "ladder_rank": 11, "ladder_tier": "foundations",
 "problem": "Thermodynamics says a calorie is a calorie - but low-carb trials suggest metabolic advantage. Does macronutrient composition change energy expenditure?",
 "description": "The energy-balance model says weight depends on calories in versus out regardless of source. But the carbohydrate-insulin model (Ludwig, Taubes) proposes high-carb diets drive fat storage and lower expenditure; some feeding trials show higher expenditure on low-carb diets. The effect sizes are small and contested - but the question strikes at nutrition's core model.",
 "background": "The calorie model dominated for a century; Atkins' popularity forced scientific engagement. Ebbeling's feeding studies (2012, 2018) found higher expenditure on low-carb; critics cited methodological issues. Hall's metabolic-ward studies found smaller effects. As of 2026 the consensus holds - calories dominate, composition effects are small - but the debate continues.",
 "why_it_matters": "If composition meaningfully changes expenditure, weight-loss guidance transforms; if not, the calorie model stands confirmed against its strongest challenge.",
 "sig_pointer": "The Signature system's proposed approach measures the composition effect precisely enough to end the debate, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that the composition effect is real but small and individual: metabolic advantage exists, varies between people, and is dwarfed by adherence - which is why both sides see real data. "
  "Assumptions: (1) the effect is measurable; (2) it varies individually; (3) precision measurement settles the magnitude. "
  "Reasoning path: a small-and-variable model explains both camps' evidence and predicts individualized energy-balance equations. "
  "Proposed mechanism: 'precision energy-balance' - individual expenditure responses to macronutrient composition. "
  "What would confirm it: individual composition-response measures predicting weight outcomes. "
  "What would kill it: evidence of zero composition effect in definitive metabolic-ward trials. "
  "What this does not claim: it does not claim any diet's superiority, offers no dietary advice, and does not constitute medical advice."),
 "sig_lens": "The Signature lens reads the calorie war as a magnitude question, and asks what precise measurement would settle it.",
 "how_it_works": "Researchers study energy balance through metabolic-ward feeding trials, doubly-labeled water, and composition-response modeling.",
 "key_points": [
  "Thermodynamics guarantees calories matter; composition effects are the question.",
  "Feeding trials show small, contested expenditure differences.",
  "The carbohydrate-insulin model is the main challenger.",
  "Adherence likely dwarfs any metabolic advantage.",
  "The core model of nutrition is at stake.",
 ],
 "requirements": [
  "Definitive metabolic-ward effect sizes.",
  "Individual composition-response measures.",
  "Integration of composition effects into guidance.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Ebbeling CB et al. Effects of dietary composition on energy expenditure. JAMA. 2012;307:2627-2634; BMJ. 2018;363:k4583.",
  "Hall KD et al. Metabolic ward studies. Various; 2015-2021.",
  "Ludwig DS et al. Carbohydrate-insulin model. Various; 2018-2022.",
  "Taubes G. The case against sugar and the CIM debate. Various; 2016-2021.",
 ],
 "demo_data": {"a": ("expenditure difference low-carb vs low-fat, kcal/day (approx)", 150.0),
               "b": ("daily expenditure, kcal (approx)", 2500.0), "bounds": (0.03, 0.1),
               "step1": "a hundred-fifty calories of disputed advantage - the margin the whole debate hangs on",
               "confirm": "individual composition-response measures predict weight outcomes",
               "refute": "definitive trials show zero composition effect"},
},
# ------------------------------------------------------------------ rank 12
{
 "key": "nutrition-epidemiology",
 "name": "Can Nutritional Epidemiology Be Fixed?",
 "group": "Methods",
 "ladder_rank": 12, "ladder_tier": "compounded",
 "problem": "Nutrition headlines flip constantly - coffee kills, coffee cures - because food questionnaires are unreliable and confounding is rampant. Can the field's methods be salvaged?",
 "description": "Nutritional epidemiology - food-frequency questionnaires linked to disease - produces the flip-flopping headlines: methods rely on memory, confounding is extreme (healthy-user bias), and effect sizes are tiny. Critics (Ioannidis) argue most findings are false; defenders argue the methods, properly applied, work. The field's credibility is its central problem.",
 "background": "FFQs enabled the big cohorts (Nurses' Health Study and others); findings shaped guidelines for decades. Ioannidis' critiques (2010s) and the red-meat GRADE controversy (2019) brought the crisis mainstream. Biomarker-calibrated intake measures and Mendelian randomization offer partial fixes. As of 2026 the field is reforming without consensus on whether reform suffices.",
 "why_it_matters": "Most dietary guidance rests on this epidemiology: if the methods are broken, the guidance pyramid sits on sand.",
 "sig_pointer": "The Signature system's proposed approach replaces memory with measurement, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that nutritional epidemiology's flaw is measurement: self-reported intake is too noisy, and objective biomarkers of intake (metabolomics, doubly-labeled water calibration) can rebuild the field. "
  "Assumptions: (1) intake biomarkers exist for key foods; (2) they are scalable; (3) biomarker-based epidemiology replicates. "
  "Reasoning path: a measurement model explains the flip-flopping and predicts stable findings from objective measures. "
  "Proposed mechanism: 'biomarker-based' nutritional epidemiology - cohorts built on measured, not remembered, intake. "
  "What would confirm it: biomarker cohorts producing stable, replicated diet-disease links. "
  "What would kill it: evidence that even measured intake can't overcome confounding. "
  "What this does not claim: it does not claim current guidance is wrong, offers no dietary advice, and does not constitute medical advice."),
 "sig_lens": "The Signature lens reads the flip-flops as measurement noise, and asks what objective intake data would stabilize.",
 "how_it_works": "Researchers study methods through biomarker calibration, Mendelian randomization, and reporting-bias research.",
 "key_points": [
  "Food-frequency questionnaires rely on faulty memory.",
  "Healthy-user bias confounds nearly every finding.",
  "Headlines flip as noise masquerades as signal.",
  "Ioannidis and GRADE critiques brought the crisis mainstream.",
  "Biomarkers and Mendelian randomization offer partial fixes.",
 ],
 "requirements": [
  "Scalable objective intake biomarkers.",
  "Biomarker cohorts with replicated findings.",
  "Proof that measurement fixes the flip-flopping.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Ioannidis JPA. Implausible results in nutritional epidemiology. Various; 2013-2018.",
  "Archer E et al. Measurement error in nutrition. Various; 2013-2018.",
  "Prentice RL et al. Biomarker-calibrated intake. Various; 2011-2019.",
  "Johnston BC et al. NutriRECS GRADE approach. Annals of Internal Medicine. 2019;171:756-764.",
 ],
 "demo_data": {"a": ("nutrition findings replicating in biomarker studies, percent (approx)", 30.0),
               "b": ("percent scale", 100.0), "bounds": (0.2, 0.42),
               "step1": "most questionnaire findings may not survive measurement - the field's credibility gap",
               "confirm": "biomarker cohorts produce stable, replicated diet-disease links",
               "refute": "even measured intake proves unable to overcome confounding"},
},
# ------------------------------------------------------------------ rank 13
{
 "key": "protein",
 "name": "How Much Protein Do We Need?",
 "group": "Macronutrients",
 "ladder_rank": 13, "ladder_tier": "compounded",
 "problem": "Protein guidance ranges from 0.8 g/kg to bodybuilder megadoses - what does the human body actually need, and does more help or harm?",
 "description": "Protein requirements - the RDA of 0.8 g/kg/day - were set for minimum adequacy, not optimal health. Higher intakes are linked to muscle preservation in aging, satiety, and weight control; but also debated links to kidney strain, IGF-1 and longevity concerns. Athletes, the elderly, and dieters all get different advice from different authorities.",
 "background": "Nitrogen-balance studies set the RDA; the method's limitations (adaptation, short duration) were long noted. Sarcopenia research pushed higher targets for older adults (1.0-1.2 g/kg). The protein-longevity debate (Fontana, Longo) suggests moderation for lifespan. As of 2026 no consensus intake exists across life stages and goals.",
 "why_it_matters": "Protein is the most supplemented macronutrient and the center of diet debates: defining real needs would settle fitness, aging, and weight-loss guidance.",
 "sig_pointer": "The Signature system's proposed approach treats protein need as life-stage-specific, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that protein needs are life-stage-specific: growth, maintenance, aging, and illness each have different optima, and one RDA can't serve them all. "
  "Assumptions: (1) optima differ by stage and goal; (2) they are measurable; (3) stage-specific guidance beats one number. "
  "Reasoning path: a life-stage model explains the conflicting advice and predicts stage-matched recommendations. "
  "Proposed mechanism: 'stage-matched' protein guidance - different targets for young, old, athletic, and ill. "
  "What would confirm it: stage-specific trials showing divergent optima. "
  "What would kill it: evidence that one intake serves all stages equally. "
  "What this does not claim: it does not claim any protein intake is optimal, offers no dietary advice, and does not constitute medical advice."),
 "sig_lens": "The Signature lens reads the protein debate as one number for many needs, and asks what each stage requires.",
 "how_it_works": "Researchers study protein needs through nitrogen balance, muscle-protein synthesis, sarcopenia trials, and longevity research.",
 "key_points": [
  "The RDA (0.8 g/kg) was set for minimum adequacy.",
  "Older adults may need 1.0-1.2 g/kg for muscle preservation.",
  "Longevity researchers suggest moderation.",
  "Athletes, elderly, and dieters get conflicting advice.",
  "No consensus exists across life stages.",
 ],
 "requirements": [
  "Stage-specific optimal intake trials.",
  "Long-term outcome data for higher intakes.",
  "Resolution of the protein-longevity tension.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Institute of Medicine. Dietary Reference Intakes for protein. 2005.",
  "Bauer J et al. Protein for older adults (PROT-AGE). JAMDA. 2013;14:542-559.",
  "Fontana L et al. Protein and longevity. Various; 2014-2020.",
  "Phillips SM et al. Protein requirements reviews. Various; 2016-2022.",
 ],
 "demo_data": {"a": ("older-adult protein target, g/kg (approx)", 1.1),
               "b": ("RDA protein target, g/kg", 0.8), "bounds": (1.2, 1.6),
               "step1": "the elderly target exceeds the RDA by nearly half - one number can't serve all ages",
               "confirm": "stage-specific trials show divergent optima",
               "refute": "one intake proves to serve all stages equally"},
},
# ------------------------------------------------------------------ rank 14
{
 "key": "sugar",
 "name": "Sugar: Toxin, Empty Calories, or Scapegoat?",
 "group": "Macronutrients",
 "ladder_rank": 14, "ladder_tier": "compounded",
 "problem": "Sugar is blamed for obesity, diabetes, and metabolic disease - but is it uniquely toxic, or just excess calories in liquid form?",
 "description": "Added sugars - especially fructose and sugary drinks - are strongly linked to obesity, diabetes, and fatty liver. But the debate rages: is fructose metabolically unique (Lustig's 'toxin' framing), or is sugar simply the easiest overconsumed calorie? Isocaloric trials show smaller effects than hypercaloric ones, suggesting dose and context dominate.",
 "background": "Yudkin's 'Pure, White and Deadly' (1972) was dismissed; Taubes and Lustig revived the sugar case in the 2000s-2010s. Sugary-drink taxes spread globally. Isocaloric fructose trials show modest metabolic effects; hypercaloric trials show large ones. As of 2026 the consensus holds that sugary drinks are harmful, but sugar's uniqueness versus excess calories is unresolved.",
 "why_it_matters": "Sugar policy - taxes, labeling, reformulation - affects the entire food supply: the mechanism determines whether policy should target sugar specifically or calories generally.",
 "sig_pointer": "The Signature system's proposed approach separates sugar's dose, form, and context, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that sugar's harm decomposes: liquid versus solid, dose, dietary context, and fructose fraction each contribute differently - and policy should target the harmful components, not sugar as a monolith. "
  "Assumptions: (1) the components are separable; (2) liquid sugar is the worst; (3) decomposition guides better policy. "
  "Reasoning path: a decomposition model explains why sugary drinks look worst and predicts component-targeted policy. "
  "Proposed mechanism: 'component-targeted' sugar policy - taxing and labeling by harm profile, not sugar content alone. "
  "What would confirm it: component trials showing divergent harm profiles. "
  "What would kill it: evidence that all sugar is equally harmful regardless of form. "
  "What this does not claim: it does not claim sugar is safe or toxic, offers no dietary advice, and does not constitute medical advice."),
 "sig_lens": "The Signature lens reads sugar as several harms bundled, and asks which form carries each.",
 "how_it_works": "Researchers study sugar through isocaloric versus hypercaloric trials, sugary-drink epidemiology, and fructose-metabolism research.",
 "key_points": [
  "Sugary drinks are consistently linked to obesity and diabetes.",
  "Isocaloric trials show smaller effects than hypercaloric ones.",
  "Fructose's unique toxicity is debated.",
  "Sugar taxes have spread globally.",
  "Dose, form, and context may matter more than sugar per se.",
 ],
 "requirements": [
  "Component-separated harm estimates.",
  "Proof of which sugar forms drive disease.",
  "Policy matched to the actual harmful components.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Lustig RH et al. Fructose and metabolic disease. Various; 2009-2013.",
  "Malik VS et al. Sugary drinks meta-analyses. Various; 2010-2019.",
  "Stanhope KL et al. Fructose trials. Various; 2009-2015.",
  "Khan TA, Sievenpiper JL. Sugar trials and reviews. Various; 2016-2022.",
 ],
 "demo_data": {"a": ("sugar-sweetened beverage tax jurisdictions (approx)", 50.0),
               "b": ("countries (approx)", 200.0), "bounds": (0.15, 0.35),
               "step1": "a quarter of countries tax sugary drinks - policy racing ahead of the mechanism",
               "confirm": "component trials show divergent harm profiles",
               "refute": "all sugar proves equally harmful regardless of form"},
},
# ------------------------------------------------------------------ rank 15
{
 "key": "gut-microbiome-nutrition",
 "name": "The Gut Microbiome and Nutrition",
 "group": "Microbiome",
 "ladder_rank": 15, "ladder_tier": "compounded",
 "problem": "Everyone's microbiome is different and diet shapes it - but can microbiome science actually tell anyone what to eat?",
 "description": "The gut microbiome mediates diet-health links: fiber fermentation, metabolite production, immune training. Precision-nutrition studies show microbiome features predict glycemic responses. But translation is stuck: probiotics mostly don't colonize, microbiome tests give unactionable advice, and causal human evidence is thin. The hype-to-evidence ratio is nutrition's worst.",
 "background": "The Human Microbiome Project (2007-2016) mapped the ecosystem; Sonnenburg's work showed diet-driven extinction of microbes. ZOE PREDICT linked microbiome to food responses. But interventions lag: FMT works for C. difficile, not for metabolic disease; commercial tests overpromise. As of 2026 the microbiome informs nutrition research far more than nutrition practice.",
 "why_it_matters": "If the microbiome can guide diet, nutrition becomes truly personal; if not, a major research program needs redirecting.",
 "sig_pointer": "The Signature system's proposed approach treats the microbiome as a response predictor, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that the microbiome's clinical value is prediction, not treatment: microbial profiles predict who responds to which diet, even if changing the microbiome directly remains hard. "
  "Assumptions: (1) prediction is robust; (2) it beats current predictors; (3) prediction alone justifies the science. "
  "Reasoning path: a prediction-first model explains the translation gap and predicts microbiome-guided diet matching. "
  "Proposed mechanism: 'microbiome-predicted' diet assignment - using microbial profiles to match diets to people. "
  "What would confirm it: microbiome-guided diets beating standard diets in trials. "
  "What would kill it: evidence that microbiome prediction adds nothing to simpler measures. "
  "What this does not claim: it does not claim microbiome tests work today, offers no dietary advice, and does not constitute medical advice."),
 "sig_lens": "The Signature lens reads the microbiome as a predictor awaiting its trial, and asks what diet-matching would prove.",
 "how_it_works": "Researchers study the microbiome through prediction cohorts, FMT metabolic trials, and probiotic colonization research.",
 "key_points": [
  "Microbiome features predict glycemic responses to food.",
  "Probiotics mostly fail to colonize.",
  "Commercial microbiome diet tests overpromise.",
  "Causal human evidence for metabolic effects is thin.",
  "Prediction may be the real clinical value.",
 ],
 "requirements": [
  "Microbiome-guided diets proven in randomized trials.",
  "Causal evidence for microbiome-targeted interventions.",
  "Honest test labeling matching actual predictive power.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Human Microbiome Project Consortium. Nature. 2012;486:207-214.",
  "Zeevi D et al. Personalized glycemic responses. Cell. 2015;163:1079-1094.",
  "Sonnenburg ED et al. Diet-driven microbiome extinction. Various; 2014-2019.",
  "Walter J et al. Probiotic colonization reviews. Various; 2018-2022.",
 ],
 "demo_data": {"a": ("microbiome diet tests with proven clinical utility (approx)", 1.0),
               "b": ("microbiome papers published yearly (approx thousands)", 10.0), "bounds": (0.05, 0.2),
               "step1": "ten thousand papers a year, essentially zero proven tests - the hype-to-evidence gap",
               "confirm": "microbiome-guided diets beat standard diets in trials",
               "refute": "microbiome prediction proves to add nothing"},
},
# ------------------------------------------------------------------ rank 16
{
 "key": "intermittent-fasting",
 "name": "Intermittent Fasting: Mechanism or Just Calories?",
 "group": "Meal Timing",
 "ladder_rank": 16, "ladder_tier": "compounded",
 "problem": "Intermittent fasting is wildly popular - but trials suggest its benefits equal simple calorie restriction. Is there anything special about fasting?",
 "description": "Intermittent fasting (16:8, 5:2, alternate-day) promises metabolic benefits beyond weight loss: autophagy, insulin sensitivity, longevity. But calorie-matched RCTs generally show fasting equals continuous restriction for weight and metabolic outcomes. Either the magic is adherence (fasting is easier for some), or the trials miss real timing effects.",
 "background": "Animal fasting-longevity research (Mattson, Longo) drove the hype; human trials in the 2010s-2020s tested it. Trepanowski (2017) and Lowe (2020) found fasting matched or underperformed continuous restriction when calories were equated. Chrono-nutrition suggests timing windows matter. As of 2026 the consensus: fasting works, mostly via calories.",
 "why_it_matters": "Millions fast daily: knowing whether timing adds anything determines whether the practice is optimization or just palatable restriction.",
 "sig_pointer": "The Signature system's proposed approach separates fasting's timing effects from its calorie effects, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that fasting's effects decompose: calorie reduction (proven), circadian alignment (plausible), and fasting-specific biology like autophagy (unproven in humans) - and each needs separate testing. "
  "Assumptions: (1) the components are separable; (2) alignment is the most promising timing effect; (3) decomposition guides practice. "
  "Reasoning path: a decomposition model explains the null calorie-matched trials and predicts alignment-matched fasting designs. "
  "Proposed mechanism: 'component-tested' fasting research - isolating calories, timing, and fasting biology. "
  "What would confirm it: alignment-matched fasting beating calorie-matched controls. "
  "What would kill it: evidence that fasting is entirely calories with no timing component. "
  "What this does not claim: it does not claim fasting is special or ordinary, offers no dietary advice, and does not constitute medical advice."),
 "sig_lens": "The Signature lens reads fasting as bundled effects, and asks which the clock contributes.",
 "how_it_works": "Researchers study fasting through calorie-matched RCTs, chrono-nutrition trials, and autophagy biomarker research.",
 "key_points": [
  "Calorie-matched trials show fasting equals continuous restriction.",
  "Animal longevity findings drove the human hype.",
  "Autophagy benefits are unproven in humans.",
  "Circadian alignment may be the real timing effect.",
  "Adherence may explain fasting's practical success.",
 ],
 "requirements": [
  "Component-separated trial evidence.",
  "Proof of human fasting-specific biology.",
  "Alignment-optimized fasting protocols.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Trepanowski JF et al. Alternate-day fasting trial. JAMA Internal Medicine. 2017;177:930-938.",
  "Lowe DA et al. Time-restricted eating trial. JAMA Internal Medicine. 2020;180:1491-1499.",
  "Mattson MP et al. Fasting reviews. Various; 2014-2021.",
  "de Cabo R, Mattson MP. Effects of intermittent fasting. NEJM. 2019;381:2541-2551.",
 ],
 "demo_data": {"a": ("calorie-matched trials favoring fasting over restriction (approx)", 1.0),
               "b": ("calorie-matched fasting trials (approx)", 10.0), "bounds": (0.05, 0.2),
               "step1": "one in ten matched trials favors fasting - the magic mostly equals the calories",
               "confirm": "alignment-matched fasting beats calorie-matched controls",
               "refute": "fasting proves to be entirely calories"},
},
# ------------------------------------------------------------------ rank 17
{
 "key": "coffee",
 "name": "Coffee: Poison or Panacea?",
 "group": "Foods",
 "ladder_rank": 17, "ladder_tier": "compounded",
 "problem": "Coffee is linked to lower mortality in huge cohorts - yet the evidence is observational and the mechanism unclear. Should everyone drink coffee?",
 "description": "Coffee - the world's most consumed psychoactive beverage - is associated with lower all-cause mortality, diabetes, Parkinson's, and liver disease in massive cohorts. But confounding is fierce (coffee drinkers differ), the active compounds are uncertain (caffeine? chlorogenic acids? diterpenes?), and preparation methods change everything. No RCT has tested coffee and mortality.",
 "background": "Early case-control studies linked coffee to harms (confounded by smoking); modern cohorts reversed the picture. Mendelian randomization supports some benefits. The diterpene issue (unfiltered coffee raising LDL) complicates the story. As of 2026 coffee is epidemiology's favorite beverage with no causal proof.",
 "why_it_matters": "Billions drink coffee daily: establishing causality and mechanism would be the largest dietary finding in history - or the largest confounding artifact.",
 "sig_pointer": "The Signature system's proposed approach tests coffee's components separately, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that coffee's benefit decomposes by compound and preparation: the mortality signal may come from specific molecules in specific brews, not 'coffee' as a monolith. "
  "Assumptions: (1) the signal has a molecular basis; (2) preparation matters; (3) decomposition is testable. "
  "Reasoning path: a component model explains the diterpene paradox and predicts brew-specific guidance. "
  "Proposed mechanism: 'component-mapped' coffee research - identifying the beneficial molecules and optimal preparations. "
  "What would confirm it: component trials showing brew-specific effects. "
  "What would kill it: evidence that the association is pure confounding. "
  "What this does not claim: it does not claim coffee is healthy, offers no dietary advice, and does not constitute medical advice."),
 "sig_lens": "The Signature lens reads the coffee signal as molecules in brews, and asks which carry the benefit.",
 "how_it_works": "Researchers study coffee through mega-cohorts, Mendelian randomization, and compound-isolation studies.",
 "key_points": [
  "Coffee is linked to lower mortality in massive cohorts.",
  "No RCT has tested coffee and mortality.",
  "Confounding by lifestyle is fierce.",
  "Unfiltered coffee raises LDL via diterpenes.",
  "The active compounds are uncertain.",
 ],
 "requirements": [
  "Component-separated causal evidence.",
  "Brew-specific effect estimates.",
  "Or proof that the signal is confounding.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Ding M et al. Coffee and mortality meta-analyses. Various; 2014-2019.",
  "Cornelis MC et al. Coffee Mendelian randomization. Various; 2015-2020.",
  "Grosso G et al. Coffee compounds reviews. Various; 2017-2021.",
  "van Dam RM et al. Coffee and health reviews. Various; 2020-2023.",
 ],
 "demo_data": {"a": ("coffee-mortality RCTs", 0.5),
               "b": ("coffee-mortality cohort studies (approx)", 100.0), "bounds": (0.001, 0.01),
               "step1": "a hundred cohorts, zero mortality RCTs - the most studied beverage with the least causal proof",
               "confirm": "component trials show brew-specific effects",
               "refute": "the association proves to be pure confounding"},
},
# ------------------------------------------------------------------ rank 18
{
 "key": "dairy",
 "name": "Dairy: Essential, Harmful, or Neutral?",
 "group": "Foods",
 "ladder_rank": 18, "ladder_tier": "compounded",
 "problem": "Dairy guidance says three servings daily; critics call milk baby-cow food for adults. What does the evidence actually say?",
 "description": "Dairy - milk, cheese, yogurt - sits at nutrition's cultural fault line: guidelines recommend it for calcium and protein; critics cite lactose intolerance (most of humanity), saturated fat, and observational links to prostate cancer and mortality. Fermented dairy looks better than milk in studies; the food matrix complicates everything.",
 "background": "Dairy's recommended status dates to early-20th-century calcium concerns. Lactose-intolerance genetics showed most adults can't digest milk - yet guidelines persisted. Recent cohorts find fermented dairy neutral-to-beneficial; milk's effects are mixed. As of 2026 dairy is recommended on tradition and calcium, contested on everything else.",
 "why_it_matters": "Dairy is a dietary staple for billions and an environmental flashpoint: the evidence verdict shapes diets and agriculture.",
 "sig_pointer": "The Signature system's proposed approach judges dairy by product, not category, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that 'dairy' is several foods: fermented (yogurt, cheese) and unfermented milk have different biology, and guidance should split them. "
  "Assumptions: (1) fermentation changes the health profile; (2) the differences are causal; (3) split guidance is actionable. "
  "Reasoning path: a product-split model explains milk's mixed signals versus fermented dairy's consistent neutrality, predicting product-specific recommendations. "
  "Proposed mechanism: 'product-split' dairy guidance - separate verdicts for milk, yogurt, cheese, and butter. "
  "What would confirm it: product-specific trials and cohorts with stable divergent estimates. "
  "What would kill it: evidence that all dairy shares one health profile. "
  "What this does not claim: it does not claim dairy is healthy or harmful, offers no dietary advice, and does not constitute medical advice."),
 "sig_lens": "The Signature lens reads dairy as several foods in one category, and asks what each product's evidence shows.",
 "how_it_works": "Researchers study dairy through product-specific cohorts, fermentation research, and lactose-genetics studies.",
 "key_points": [
  "Guidelines recommend dairy mainly for calcium and tradition.",
  "Most of humanity is lactose intolerant as adults.",
  "Fermented dairy looks better than milk in studies.",
  "Observational links to prostate cancer are debated.",
  "The category bundles very different foods.",
 ],
 "requirements": [
  "Product-specific causal evidence.",
  "Split guidance by dairy product.",
  "Calcium-source comparisons beyond dairy.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Thorning TK et al. Dairy matrix reviews. Various; 2017-2022.",
  "Dehghan M et al. PURE dairy analyses. Lancet. 2018;392:2288-2296.",
  "Aune D et al. Dairy meta-analyses. Various; 2012-2019.",
  "Savaiano DA et al. Lactose intolerance reviews. Various; 2013-2020.",
 ],
 "demo_data": {"a": ("humans lactose intolerant as adults, percent (approx)", 65.0),
               "b": ("percent scale", 100.0), "bounds": (0.55, 0.75),
               "step1": "two-thirds of humanity can't digest milk as adults - yet guidelines recommend it daily",
               "confirm": "product-specific studies give stable divergent estimates",
               "refute": "all dairy proves to share one health profile"},
},
# ------------------------------------------------------------------ rank 19
{
 "key": "eggs",
 "name": "Eggs: How Many Are Safe?",
 "group": "Foods",
 "ladder_rank": 19, "ladder_tier": "compounded",
 "problem": "Eggs were limited, exonerated, then linked to harm again - the evidence whiplashes. What's the real story on eggs and cholesterol?",
 "description": "Eggs - dietary cholesterol's flagship - swung from restriction (300 mg/day limits) to exoneration (2015 US guidelines dropped the limit) to renewed concern (Zhong 2019 linked eggs to CVD). Dietary cholesterol raises blood cholesterol modestly; the clinical significance is debated; confounding by overall diet is fierce.",
 "background": "Cholesterol limits dated to the diet-heart era; the 2015 US Dietary Guidelines removed them citing weak evidence. Zhong's 2019 JAMA analysis re-ignited the debate with dose-response CVD links. Mendelian and feeding studies show modest LDL effects. As of 2026 eggs sit in evidence limbo.",
 "why_it_matters": "Eggs are the cheapest protein for billions: the verdict determines whether a staple food is limited or celebrated.",
 "sig_pointer": "The Signature system's proposed approach treats egg effects as individual, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that egg effects are individual: cholesterol-absorbers versus synthesizers respond differently to dietary cholesterol, and the population average hides both. "
  "Assumptions: (1) responder types exist; (2) they are identifiable; (3) typed guidance beats blanket limits. "
  "Reasoning path: a responder model explains the whiplash - different studies sample different responder mixes - and predicts personalized egg guidance. "
  "Proposed mechanism: 'responder-typed' egg guidance - identifying cholesterol responders versus non-responders. "
  "What would confirm it: responder typing predicting LDL response to eggs. "
  "What would kill it: evidence that egg effects are uniform across people. "
  "What this does not claim: it does not claim eggs are safe or harmful, offers no dietary advice, and does not constitute medical advice."),
 "sig_lens": "The Signature lens reads the egg whiplash as mixed responders, and asks what typing would sort them.",
 "how_it_works": "Researchers study eggs through feeding trials, cholesterol-absorption genetics, and dose-response cohorts.",
 "key_points": [
  "The 2015 US guidelines dropped cholesterol limits.",
  "Zhong (2019) re-linked eggs to CVD with dose-response.",
  "Dietary cholesterol modestly raises blood cholesterol.",
  "Confounding by overall diet is fierce.",
  "Individual response variation is large.",
 ],
 "requirements": [
  "Identifiable cholesterol-responder types.",
  "Responder-predicted LDL responses.",
  "Stable guidance surviving the whiplash.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Zhong VW et al. Egg consumption and CVD. JAMA. 2019;321:1081-1095.",
  "US Dietary Guidelines Advisory Committee. 2015 report (cholesterol limit removal).",
  "Rong Y et al. Egg meta-analyses. Various; 2013-2020.",
  "Blesso CN, Fernandez ML. Dietary cholesterol reviews. Various; 2018-2021.",
 ],
 "demo_data": {"a": ("egg-cholesterol guideline reversals since 1970 (approx)", 3.0),
               "b": ("guideline eras (approx)", 5.0), "bounds": (0.45, 0.75),
               "step1": "three reversals in five decades - the staple food science can't settle",
               "confirm": "responder typing predicts LDL response to eggs",
               "refute": "egg effects prove uniform across people"},
},
# ------------------------------------------------------------------ rank 20
{
 "key": "artificial-sweeteners",
 "name": "Artificial Sweeteners: Safe Substitute or Metabolic Trick?",
 "group": "Food Additives",
 "ladder_rank": 20, "ladder_tier": "compounded",
 "problem": "Diet sodas promise sweetness without calories - but observational links to obesity and diabetes, plus microbiome findings, cloud the picture. Are they safe?",
 "description": "Non-nutritive sweeteners (aspartame, sucralose, stevia) - consumed by millions - carry observational links to obesity, diabetes, and cardiovascular events, plus the famous Suez (2014) microbiome-glucose findings. But reverse causation (unhealthy people choose diet drinks) confounds everything; RCTs versus sugar show benefits; versus water show little. WHO's 2023 guidance advised against their use for weight control.",
 "background": "Sweeteners were the obvious sugar solution; observational alarms began in the 2000s-2010s. Suez's Nature paper (2014) showed saccharin altering mouse microbiomes and glucose tolerance. Human RCTs are short and mixed. WHO's 2023 systematic review found no long-term weight benefit and possible harms. As of 2026 the field is genuinely uncertain.",
 "why_it_matters": "Sweeteners are in thousands of products consumed daily: the safety verdict affects nearly every diet-conscious consumer.",
 "sig_pointer": "The Signature system's proposed approach compares sweeteners against the right counterfactual, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that the sweetener question is three questions: versus sugar (likely better), versus water (likely neutral-to-worse), and by compound (each sweetener different) - and each needs its own answer. "
  "Assumptions: (1) the counterfactual determines the verdict; (2) compounds differ; (3) separated answers end the confusion. "
  "Reasoning path: a counterfactual model explains why studies conflict - they compare against different baselines - and predicts compound-and-comparator-specific guidance. "
  "Proposed mechanism: 'comparator-specified' sweetener guidance - verdicts stated as versus-sugar, versus-water, per compound. "
  "What would confirm it: comparator-specified trials giving stable answers. "
  "What would kill it: evidence that all sweeteners share one metabolic profile. "
  "What this does not claim: it does not claim sweeteners are safe or harmful, offers no dietary advice, and does not constitute medical advice."),
 "sig_lens": "The Signature lens reads the sweetener debate as wrong comparisons, and asks what the right ones would show.",
 "how_it_works": "Researchers study sweeteners through comparator-specified RCTs, microbiome research, and WHO evidence reviews.",
 "key_points": [
  "Observational links to obesity and diabetes are confounded.",
  "Versus sugar, sweeteners look beneficial; versus water, neutral.",
  "Suez (2014) showed microbiome-mediated glucose effects in mice.",
  "WHO (2023) advised against use for weight control.",
  "Each sweetener compound may differ.",
 ],
 "requirements": [
  "Long-term comparator-specified RCTs.",
  "Compound-specific metabolic profiles.",
  "Guidance stated per comparator and compound.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Suez J et al. Artificial sweeteners induce glucose intolerance via microbiome. Nature. 2014;514:181-186.",
  "World Health Organization. Non-sugar sweeteners guideline. 2023.",
  "Rogers PJ et al. Sweetener RCT reviews. Various; 2016-2021.",
  "Debras C et al. Sweeteners and CVD (NutriNet-Sante). BMJ. 2022;378:e071204.",
 ],
 "demo_data": {"a": ("sweetener compounds needing separate verdicts (approx)", 6.0),
               "b": ("sweeteners treated as one category", 1.0), "bounds": (4.0, 9.0),
               "step1": "six-plus compounds judged as one - the category error at the debate's heart",
               "confirm": "comparator-specified trials give stable per-compound answers",
               "refute": "all sweeteners prove to share one metabolic profile"},
},
# ------------------------------------------------------------------ rank 21
{
 "key": "personalized-nutrition",
 "name": "Personalized Nutrition: Science or Startup Hype?",
 "group": "Precision Nutrition",
 "ladder_rank": 21, "ladder_tier": "compounded",
 "problem": "Startups sell DNA-based diets - but does personalized nutrition actually outperform good generic advice?",
 "description": "Personalized nutrition - diets from genetics, microbiome, continuous glucose monitors - is a booming industry. The science: Zeevi (2015) proved predictable glycemic responses; but whether personalization improves outcomes versus high-quality generic advice is unproven. The Food4Me trial (2016) found personalization added little; genetics-based diet advice has minimal evidence.",
 "background": "The Human Genome Project promised personalized everything; nutrition joined late. Zeevi's Cell paper (2015) was the proof-of-concept; ZOE commercialized it. Food4Me - the largest personalization RCT - showed small added benefit. CGM-based eating is popular without outcome proof. As of 2026 the industry outruns the evidence.",
 "why_it_matters": "If personalization works, it's the future of dietary guidance; if not, consumers are buying expensive noise.",
 "sig_pointer": "The Signature system's proposed approach tests personalization against the right control, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that personalization's test is wrong: it should be tested against the best generic advice plus attention - not against nothing - and on outcomes, not just predicted responses. "
  "Assumptions: (1) the right control is best-generic-plus-attention; (2) outcomes, not predictions, are the endpoint; (3) honest trials will show where personalization adds value. "
  "Reasoning path: a proper-control model explains Food4Me's small effects and predicts personalization winning on specific outcomes. "
  "Proposed mechanism: 'properly-controlled' personalization trials - best-generic controls, outcome endpoints. "
  "What would confirm it: personalization beating best-generic advice on hard outcomes. "
  "What would kill it: null results even against proper controls. "
  "What this does not claim: it does not claim personalization works or doesn't, offers no dietary advice, and does not constitute medical advice."),
 "sig_lens": "The Signature lens reads the personalization debate as wrong controls, and asks what honest trials would show.",
 "how_it_works": "Researchers study personalization through Food4Me-style RCTs, glycemic-prediction validation, and CGM outcome trials.",
 "key_points": [
  "Zeevi (2015) proved glycemic responses are predictable.",
  "Food4Me found personalization added little over generic advice.",
  "Genetics-based diet advice has minimal evidence.",
  "CGM-based eating lacks outcome proof.",
  "The industry outruns the evidence.",
 ],
 "requirements": [
  "Personalization beating best-generic advice on outcomes.",
  "Validated prediction-to-outcome pipelines.",
  "Honest marketing matching proven benefit.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Zeevi D et al. Personalized nutrition by prediction of glycemic responses. Cell. 2015;163:1079-1094.",
  "Celis-Morales C et al. Food4Me trial. International Journal of Epidemiology. 2016;46:578-588.",
  "Berry SE et al. ZOE PREDICT. Nature Medicine. 2020;26:964-973.",
  "Ordovas JM et al. Personalised nutrition reviews. Various; 2018-2023.",
 ],
 "demo_data": {"a": ("Food4Me added benefit of personalization, percent (approx)", 5.0),
               "b": ("percent scale", 100.0), "bounds": (0.02, 0.1),
               "step1": "the largest trial found a whisper of added benefit - the industry's evidence gap",
               "confirm": "personalization beats best-generic advice on hard outcomes",
               "refute": "null results persist even against proper controls"},
},
# ------------------------------------------------------------------ rank 22
{
 "key": "longevity-diet",
 "name": "Can Diet Extend Human Lifespan?",
 "group": "Longevity",
 "ladder_rank": 22, "ladder_tier": "compounded",
 "problem": "Calorie restriction extends life in animals - but does any diet extend human life, or just human health?",
 "description": "Calorie restriction extends lifespan in yeast, worms, flies, and monkeys (with caveats); the human evidence is limited to biomarkers and the CALERIE trial's metabolic improvements. Mediterranean patterns are linked to longevity in cohorts; protein restriction, fasting-mimicking diets, and rapamycin-adjacent nutrition are experimental. No diet has proven human lifespan extension.",
 "background": "McCay's 1935 rat experiments launched CR research; the NIA/Wisconsin monkey studies (2009-2012) showed healthspan benefits with lifespan debate. CALERIE (2018) proved feasibility and metabolic benefit in humans. Blue-Zone epidemiology suggests dietary patterns matter. As of 2026 lifespan extension by diet is proven in animals, unproven in humans.",
 "why_it_matters": "Diet is the most accessible longevity intervention: proving lifespan extension would be the most consequential nutrition finding ever.",
 "sig_pointer": "The Signature system's proposed approach treats diet-longevity as a healthspan-first question, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that diet-longevity research should target healthspan mechanisms (metabolic health, inflammation, proteostasis) rather than waiting decades for mortality data - with validated surrogate endpoints. "
  "Assumptions: (1) surrogate endpoints can be validated; (2) healthspan mechanisms drive lifespan; (3) diet modulates them. "
  "Reasoning path: a healthspan-first model makes the question answerable in years, not decades, predicting diet-healthspan trials. "
  "Proposed mechanism: 'healthspan-endpoint' diet trials - testing diets against validated aging biomarkers. "
  "What would confirm it: diets improving validated aging biomarkers in trials. "
  "What would kill it: evidence that animal CR findings don't translate to humans at all. "
  "What this does not claim: it does not claim any diet extends life, offers no dietary advice, and does not constitute medical advice."),
 "sig_lens": "The Signature lens reads the longevity question as untestable on mortality timescales, and asks what healthspan endpoints would answer it.",
 "how_it_works": "Researchers study diet and longevity through CALERIE-style trials, Blue-Zone epidemiology, and aging-biomarker research.",
 "key_points": [
  "CR extends lifespan in multiple animal species.",
  "CALERIE showed metabolic benefits in humans.",
  "No diet has proven human lifespan extension.",
  "Blue Zones suggest patterns matter.",
  "Mortality trials would take decades.",
 ],
 "requirements": [
  "Validated aging biomarkers as trial endpoints.",
  "Diets improving those biomarkers in RCTs.",
  "Translation proof from animal CR to humans.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "McCay CM et al. Calorie restriction in rats. 1935.",
  "Colman RJ et al. Wisconsin monkey CR study. Science. 2009;325:201-204.",
  "Ravussin E et al. CALERIE trial. Various; 2015-2018.",
  "Longo VD et al. Fasting-mimicking diets. Various; 2015-2021.",
 ],
 "demo_data": {"a": ("human diets proven to extend lifespan", 0.5),
               "b": ("animal species with CR lifespan extension (approx)", 5.0), "bounds": (0.05, 0.2),
               "step1": "five species proven, zero human diets - the translation gap at nutrition's grandest question",
               "confirm": "diets improve validated aging biomarkers in trials",
               "refute": "animal CR findings prove untranslatable to humans"},
},
# ------------------------------------------------------------------ rank 23
{
 "key": "food-addiction",
 "name": "Is Food Addictive?",
 "group": "Behavior",
 "ladder_rank": 23, "ladder_tier": "compounded",
 "problem": "People describe losing control over eating like addiction - but is 'food addiction' a real neurobiological entity or a metaphor?",
 "description": "The Yale Food Addiction Scale identifies 'food addiction' in a subset of people with obesity; neuroimaging shows reward-circuit responses to food cues resembling drug cues. But critics argue eating is necessary (unlike drugs), the construct medicalizes overeating, and no food meets addiction criteria pharmacologically. The concept's validity determines treatment approaches.",
 "background": "Randolph (1956) proposed food addiction; the concept revived with obesity neuroscience (Volkow, Gearhardt). YFAS (2009) operationalized it. Animal models show sugar-binge neural changes. But the DSM-5 declined the diagnosis, and critics (Hebebrand, Fletcher) argue the evidence is insufficient. As of 2026 food addiction is a research construct, not a diagnosis.",
 "why_it_matters": "If food addiction is real, obesity treatment needs addiction medicine; if not, the framing harms more than it helps.",
 "sig_pointer": "The Signature system's proposed approach tests food addiction by its treatment implications, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that food addiction's validity should be tested pragmatically: if addiction-framed treatments outperform standard obesity care in the YFAS-positive subgroup, the construct earns its keep. "
  "Assumptions: (1) the subgroup is identifiable; (2) addiction treatments transfer; (3) pragmatic testing settles validity. "
  "Reasoning path: a pragmatic model sidesteps the philosophical debate and predicts treatment-matched trials. "
  "Proposed mechanism: 'construct-tested' food-addiction care - addiction protocols for the YFAS-positive subgroup. "
  "What would confirm it: addiction-framed treatments beating standard care in the subgroup. "
  "What would kill it: null results or evidence the construct is pure metaphor. "
  "What this does not claim: it does not claim food addiction is real, offers no dietary advice, and does not constitute medical advice."),
 "sig_lens": "The Signature lens reads the addiction debate as testable by treatment, and asks what trials would settle it.",
 "how_it_works": "Researchers study food addiction through YFAS validation, cue-reactivity imaging, and addiction-protocol trials.",
 "key_points": [
  "YFAS identifies food addiction in a subset with obesity.",
  "Food cues activate reward circuits like drug cues.",
  "DSM-5 declined the diagnosis.",
  "Critics call it medicalized metaphor.",
  "Treatment implications are the pragmatic test.",
 ],
 "requirements": [
  "Addiction-protocol trials in the YFAS-positive subgroup.",
  "Proof the construct predicts treatment response.",
  "Resolution of the validity debate with data.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Gearhardt AN et al. Yale Food Addiction Scale. Appetite. 2009;52:430-436.",
  "Volkow ND et al. Food and drug reward. Various; 2008-2013.",
  "Hebebrand J et al. Critiques of food addiction. Various; 2014-2019.",
  "Fletcher PC, Kenny PJ. Food addiction: a valid concept? Neuropharmacology. 2018;131:132-138.",
 ],
 "demo_data": {"a": ("people with obesity meeting YFAS criteria, percent (approx)", 25.0),
               "b": ("percent scale", 100.0), "bounds": (0.15, 0.35),
               "step1": "a quarter of people with obesity meet addiction criteria - for a diagnosis that doesn't exist",
               "confirm": "addiction-framed treatments beat standard care in the subgroup",
               "refute": "the construct proves to be pure metaphor"},
},
# ------------------------------------------------------------------ rank 24
{
 "key": "nutrition-inequality",
 "name": "Nutrition Inequality: Why Do the Poor Eat Worse?",
 "group": "Food Systems",
 "ladder_rank": 24, "ladder_tier": "advanced",
 "problem": "Healthy diets cost more and the poor bear the disease burden - is nutrition inequality about price, access, knowledge, or something deeper?",
 "description": "Diet quality tracks income and education globally: the poor eat more ultra-processed food, less produce, and suffer more diet-related disease. Explanations compete: price (healthy food costs more per calorie), food deserts (access), time poverty, stress biology, and targeted marketing. The causal weights are unknown - and interventions (subsidies, food-desert stores) show mixed results.",
 "background": "Food-desert research (2000s-2010s) found access mattered less than expected - new supermarkets barely changed diets. Price studies show healthy diets cost ~$1.50/day more. Stress and scarcity research (Mullainathan, Shafir) suggests cognitive bandwidth effects. As of 2026 the field knows inequality exists but not its levers.",
 "why_it_matters": "Diet-related disease concentrates in the poor: finding the real levers would make nutrition policy an equity instrument.",
 "sig_pointer": "The Signature system's proposed approach tests inequality levers experimentally, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that nutrition inequality's levers are testable: price, access, time, and stress can each be experimentally manipulated to measure their causal weight. "
  "Assumptions: (1) the levers are separable; (2) experiments are feasible; (3) weights guide policy. "
  "Reasoning path: a lever-testing model explains mixed intervention results and predicts targeted equity policy. "
  "Proposed mechanism: 'lever-weighted' nutrition equity - policy matched to measured causal weights. "
  "What would confirm it: lever experiments with clear causal weights. "
  "What would kill it: evidence that inequality is irreducible to manipulable levers. "
  "What this does not claim: it does not claim any lever dominates, offers no policy prescription, and does not constitute medical advice."),
 "sig_lens": "The Signature lens reads inequality as levers awaiting measurement, and asks what experiments would weigh them.",
 "how_it_works": "Researchers study nutrition inequality through price experiments, food-access trials, and scarcity-behavior research.",
 "key_points": [
  "Diet quality tracks income globally.",
  "New supermarkets barely changed diets (access isn't the lever).",
  "Healthy diets cost ~$1.50/day more.",
  "Stress and scarcity affect food choices.",
  "The causal weights of levers are unknown.",
 ],
 "requirements": [
  "Experimental causal weights for each lever.",
  "Interventions matched to measured weights.",
  "Equity policy proven to narrow diet gaps.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Cummins S et al. Food desert interventions. Various; 2005-2014.",
  "Rao M et al. Healthy diet cost meta-analysis. BMJ Open. 2013;3:e004277.",
  "Mullainathan S, Shafir E. Scarcity. 2013.",
  "Darmon N, Drewnowski A. Nutrition inequality reviews. Various; 2015-2021.",
 ],
 "demo_data": {"a": ("healthy diet premium, dollars/day (approx)", 1.5),
               "b": ("food spending of the poor, dollars/day (approx)", 5.0), "bounds": (0.2, 0.42),
               "step1": "a $1.50 daily premium on a $5 food budget - the arithmetic of inequality",
               "confirm": "lever experiments yield clear causal weights",
               "refute": "inequality proves irreducible to manipulable levers"},
},
# ------------------------------------------------------------------ rank 25
{
 "key": "breastfeeding",
 "name": "Breastfeeding: How Much Does It Matter Long-Term?",
 "group": "Life Stages",
 "ladder_rank": 25, "ladder_tier": "advanced",
 "problem": "'Breast is best' - but sibling studies suggest many long-term benefits vanish when family is controlled. What's really causal?",
 "description": "Breastfeeding is linked to IQ, obesity, and immunity benefits in observational studies - but mothers who breastfeed differ profoundly, and sibling comparisons (Colen, 2014) found most long-term benefits disappeared within families. The field debates which benefits are causal (infection protection in infancy is solid) versus confounded.",
 "background": "The PROBIT trial (Kramer, 2001) - the only large RCT - found IQ benefits but was cluster-randomized with limitations. Sibling studies challenged the long-term claims. The microbiome and immune-programming mechanisms are plausible but unproven. As of 2026 the short-term benefits are solid; the long-term ones are contested.",
 "why_it_matters": "Breastfeeding promotion affects every new mother: honest causal accounting would replace guilt with evidence.",
 "sig_pointer": "The Signature system's proposed approach separates breastfeeding's causal benefits from confounded ones, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that breastfeeding's benefits decompose: anti-infective effects in infancy (causal), nutritional adequacy (context-dependent), and long-term programming claims (likely confounded) - each needing separate verdicts. "
  "Assumptions: (1) the benefits are separable; (2) sibling designs approximate causality; (3) decomposition ends the guilt-evidence mismatch. "
  "Reasoning path: a decomposition model explains why short-term benefits replicate and long-term ones don't, predicting honest benefit accounting. "
  "Proposed mechanism: 'benefit-separated' breastfeeding evidence - causal verdicts per claimed benefit. "
  "What would confirm it: separated analyses with stable per-benefit verdicts. "
  "What would kill it: evidence that the benefits can't be separated methodologically. "
  "What this does not claim: it does not claim breastfeeding is unimportant, offers no infant-feeding advice, and does not constitute medical advice."),
 "sig_lens": "The Signature lens reads the breastfeeding claims as bundled benefits, and asks which survive family controls.",
 "how_it_works": "Researchers study breastfeeding through sibling comparisons, PROBIT follow-ups, and microbiome mechanism research.",
 "key_points": [
  "Sibling studies erased most long-term benefit claims.",
  "PROBIT found IQ benefits with limitations.",
  "Anti-infective benefits in infancy are solid.",
  "Confounding by maternal characteristics is extreme.",
  "Promotion often outruns the causal evidence.",
 ],
 "requirements": [
  "Benefit-separated causal verdicts.",
  "Mechanistic proof for programming claims.",
  "Promotion matched to proven benefits.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Kramer MS et al. PROBIT trial. JAMA. 2001;285:413-420.",
  "Colen CG, Ramey DM. Sibling comparisons of breastfeeding effects. Social Science & Medicine. 2014;109:19-27.",
  "Victora CG et al. Breastfeeding Lancet series. 2016;387:475-490.",
  "Azad MB et al. Breastfeeding and microbiome. Various; 2018-2022.",
 ],
 "demo_data": {"a": ("long-term benefits surviving sibling controls, percent (approx)", 20.0),
               "b": ("percent scale", 100.0), "bounds": (0.1, 0.32),
               "step1": "four-fifths of long-term claims vanish within families - the confounded legacy of 'breast is best'",
               "confirm": "separated analyses give stable per-benefit verdicts",
               "refute": "the benefits prove inseparable methodologically"},
},
# ------------------------------------------------------------------ rank 26
{
 "key": "aging-nutrition",
 "name": "Nutrition for Healthy Aging",
 "group": "Life Stages",
 "ladder_rank": 26, "ladder_tier": "advanced",
 "problem": "Older adults face sarcopenia, frailty, and anorexia of aging - yet nutrition guidance for the elderly is extrapolated from the young. What should older people eat?",
 "description": "Aging changes nutrition fundamentally: muscle-protein synthesis blunts (anabolic resistance), appetite falls, absorption declines, and sarcopenia drives frailty and falls. But RDAs were set in young adults; protein targets for the elderly are debated; and the anorexia of aging has no proven nutritional treatment. Geriatric nutrition is extrapolated guesswork.",
 "background": "Anabolic resistance was characterized in the 2000s-2010s (Breen, Phillips); PROT-AGE (2013) recommended higher protein. Sarcopenia got an ICD code (2016). But trials of protein-plus-exercise in the frail show modest effects, and appetite stimulation remains elusive. As of 2026 elderly nutrition guidance rests on thin direct evidence.",
 "why_it_matters": "Populations are aging rapidly: getting elderly nutrition right would prevent frailty, falls, and institutionalization at scale.",
 "sig_pointer": "The Signature system's proposed approach builds elderly nutrition from elderly physiology, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that elderly nutrition must be built from elderly physiology: anabolic resistance, altered absorption, and appetite biology measured in the old - not extrapolated from the young. "
  "Assumptions: (1) elderly physiology differs enough to matter; (2) it is measurable; (3) elderly-specific guidance beats extrapolation. "
  "Reasoning path: a physiology-first model explains modest trial results and predicts elderly-derived recommendations. "
  "Proposed mechanism: 'elderly-derived' nutrition guidance - requirements measured in older adults. "
  "What would confirm it: elderly-measured requirements differing from extrapolated ones with better outcomes. "
  "What would kill it: evidence that young-adult requirements transfer fine. "
  "What this does not claim: it does not claim any elderly diet is optimal, offers no dietary advice, and does not constitute medical advice."),
 "sig_lens": "The Signature lens reads geriatric nutrition as extrapolated guesswork, and asks what direct measurement would prescribe.",
 "how_it_works": "Researchers study aging nutrition through anabolic-resistance research, sarcopenia trials, and elderly requirement studies.",
 "key_points": [
  "Anabolic resistance blunts muscle-protein synthesis in aging.",
  "RDAs were set in young adults.",
  "Sarcopenia drives frailty, falls, and mortality.",
  "Protein-plus-exercise trials show modest effects.",
  "The anorexia of aging has no proven treatment.",
 ],
 "requirements": [
  "Requirements measured directly in older adults.",
  "Elderly-specific guidance proven superior.",
  "Appetite and anabolic interventions that work.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Bauer J et al. PROT-AGE recommendations. JAMDA. 2013;14:542-559.",
  "Breen L, Phillips SM. Anabolic resistance. Various; 2011-2013.",
  "Cruz-Jentoft AJ et al. Sarcopenia definitions. Various; 2010-2019.",
  "Robinson SM et al. Nutrition and frailty. Various; 2018-2022.",
 ],
 "demo_data": {"a": ("nutrition trials enrolling only the elderly, percent of geriatric guidance (approx)", 20.0),
               "b": ("percent scale", 100.0), "bounds": (0.12, 0.3),
               "step1": "four-fifths of elderly guidance is extrapolated from the young - guesswork for the frail",
               "confirm": "elderly-measured requirements beat extrapolated ones on outcomes",
               "refute": "young-adult requirements prove to transfer fine"},
},
# ------------------------------------------------------------------ rank 27
{
 "key": "hydration",
 "name": "How Much Water Should We Drink?",
 "group": "Hydration",
 "ladder_rank": 27, "ladder_tier": "advanced",
 "problem": "'Eight glasses a day' has no scientific basis - yet dehydration harms and overhydration kills. What is optimal hydration?",
 "description": "The 8x8 water rule is a myth without source; thirst is a good guide for most; but the elderly have blunted thirst, athletes face hyponatremia, and chronic mild dehydration's effects are unstudied. No RCT has defined optimal water intake for health outcomes. Hydration is simultaneously over-prescribed and under-studied.",
 "background": "The 8-glasses myth was traced to a 1945 Food and Nutrition Board note (misread); Valtin's 2002 review found no evidence. Exercise-hyponatremia research (Noakes) showed overdrinking kills marathoners. As of 2026 hydration guidance is 'drink to thirst' - sensible but unproven for long-term health.",
 "why_it_matters": "Water is the most consumed 'nutrient': defining optimal intake would end the most repeated myth in nutrition.",
 "sig_pointer": "The Signature system's proposed approach treats hydration as individual and context-dependent, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that optimal hydration is individual and contextual: thirst suffices for most, but age, activity, climate, and disease create groups needing guidance - and each needs its own evidence. "
  "Assumptions: (1) needs vary meaningfully; (2) vulnerable groups are identifiable; (3) group-specific guidance beats universal rules. "
  "Reasoning path: a contextual model explains why universal rules fail and predicts group-specific hydration science. "
  "Proposed mechanism: 'context-typed' hydration guidance - different targets for elderly, athletes, and the ill. "
  "What would confirm it: group-specific trials defining optimal intakes. "
  "What would kill it: evidence that thirst suffices universally. "
  "What this does not claim: it does not claim any water intake is optimal, offers no dietary advice, and does not constitute medical advice."),
 "sig_lens": "The Signature lens reads hydration as context, not commandments, and asks what each group needs.",
 "how_it_works": "Researchers study hydration through thirst-physiology research, hyponatremia studies, and elderly hydration trials.",
 "key_points": [
  "The 8-glasses rule has no scientific source.",
  "Thirst guides most people adequately.",
  "Elderly thirst is blunted; athletes risk hyponatremia.",
  "No RCT defines optimal intake for health outcomes.",
  "Chronic mild dehydration is unstudied.",
 ],
 "requirements": [
  "Group-specific optimal intake trials.",
  "Long-term health outcomes of hydration levels.",
  "Retirement of the 8-glasses myth with evidence.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Valtin H. Drink at least eight glasses of water a day? American Journal of Physiology. 2002;283:R993-R1004.",
  "Noakes TD et al. Exercise-associated hyponatremia. Various; 2005-2015.",
  "Popkin BM et al. Water and hydration reviews. Various; 2010-2020.",
  "Perrier ET et al. Hydration biomarkers. Various; 2015-2021.",
 ],
 "demo_data": {"a": ("evidence behind the 8-glasses rule (approx)", 0.5),
               "b": ("people following it, billions (approx)", 2.0), "bounds": (0.15, 0.4),
               "step1": "two billion people follow a rule with zero evidence behind it",
               "confirm": "group-specific trials define optimal intakes",
               "refute": "thirst proves sufficient universally"},
},
# ------------------------------------------------------------------ rank 28
{
 "key": "nutrigenomics",
 "name": "Nutrigenomics: Do Genes Determine Diet Response?",
 "group": "Precision Nutrition",
 "ladder_rank": 28, "ladder_tier": "advanced",
 "problem": "Genes affect caffeine metabolism, lactose tolerance, and folate processing - but can genetics usefully guide diet, or are the effects too small?",
 "description": "Nutrigenomics - gene-diet interactions - has clear wins (CYP1A2 and caffeine, MTHFR and folate, lactase persistence) but the effect sizes for complex outcomes are tiny. Polygenic diet-response scores explain little; commercial DNA-diet tests overpromise. The field debates whether nutrigenomics will ever be clinically useful.",
 "background": "Candidate gene-diet interactions (APOE and fat, PPARG and diet) mostly failed replication. GWAS-era scores explain small variance. The clear monogenic wins remain the exception. As of 2026 nutrigenomics is a science of small effects awaiting its clinical translation.",
 "why_it_matters": "If genes meaningfully guide diet, nutrition becomes truly personal; the current evidence says mostly not - yet.",
 "sig_pointer": "The Signature system's proposed approach tests nutrigenomics by clinical utility, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that nutrigenomics' test is clinical utility: gene-guided diets must beat good generic diets on outcomes - not just show statistically significant interactions. "
  "Assumptions: (1) utility is the right bar; (2) some interactions will clear it; (3) honest testing finds them. "
  "Reasoning path: a utility model explains the hype-evidence gap and predicts gene-guided trial wins where effects are real. "
  "Proposed mechanism: 'utility-tested' nutrigenomics - gene-guided diets in outcome trials. "
  "What would confirm it: gene-guided diets beating generic diets on hard outcomes. "
  "What would kill it: persistent nulls even for the best candidate interactions. "
  "What this does not claim: it does not claim DNA diets work, offers no dietary advice, and does not constitute medical advice."),
 "sig_lens": "The Signature lens reads nutrigenomics as small effects awaiting proof, and asks what utility trials would show.",
 "how_it_works": "Researchers study nutrigenomics through gene-diet interaction GWAS, monogenic win translation, and utility trials.",
 "key_points": [
  "Clear wins exist: CYP1A2-caffeine, lactase, MTHFR-folate.",
  "Complex-outcome effects are tiny.",
  "Commercial DNA-diet tests overpromise.",
  "Candidate interactions mostly failed replication.",
  "Clinical utility is unproven.",
 ],
 "requirements": [
  "Gene-guided diets beating generic diets on outcomes.",
  "Replication of interaction effects.",
  "Honest test marketing matching proven utility.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Cornelis MC et al. CYP1A2 and caffeine. Various; 2006-2015.",
  "Ordovas JM et al. Nutrigenomics reviews. Various; 2004-2019.",
  "Qi L et al. Gene-diet interaction GWAS. Various; 2012-2020.",
  "Ferguson JF et al. Nutrigenomics utility reviews. Various; 2021-2023.",
 ],
 "demo_data": {"a": ("nutrigenomic interactions with proven clinical utility (approx)", 3.0),
               "b": ("nutrigenomic interactions marketed (approx)", 100.0), "bounds": (0.015, 0.05),
               "step1": "three proven of a hundred marketed - the utility gap in DNA diets",
               "confirm": "gene-guided diets beat generic diets on hard outcomes",
               "refute": "persistent nulls even for the best candidates"},
},
# ------------------------------------------------------------------ rank 29
{
 "key": "food-environment",
 "name": "The Food Environment: Can It Be Redesigned?",
 "group": "Food Systems",
 "ladder_rank": 29, "ladder_tier": "advanced",
 "problem": "Obesity follows food environments - but can redesigning environments (labels, taxes, placement) actually change population diets?",
 "description": "The food environment - what's available, advertised, priced, and placed - shapes diets powerfully in observational research. But interventions show modest effects: front-of-pack labels shift purchases slightly, soda taxes reduce consumption modestly, and choice-architecture nudges are small. The field debates whether environmental redesign can work at the scale of the obesity epidemic.",
 "background": "Choice architecture (Thaler, Sunstein) inspired nudge trials; labeling schemes (Nutri-Score, traffic lights) spread in Europe; soda taxes showed 10-20% consumption drops. But population obesity kept rising. As of 2026 the evidence says environments matter but redesigning them moves diets modestly.",
 "why_it_matters": "If environments can be redesigned effectively, obesity becomes a policy problem with policy solutions; if not, the focus must shift elsewhere.",
 "sig_pointer": "The Signature system's proposed approach tests environmental redesign at full policy scale, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that environmental interventions have been tested too small: labels and nudges are weak versions of the strong policies (reformulation mandates, advertising bans, price restructuring) that might actually work. "
  "Assumptions: (1) intervention strength matters; (2) strong policies are testable; (3) scale reveals true potential. "
  "Reasoning path: a strength model explains modest nudge effects and predicts strong-policy trials. "
  "Proposed mechanism: 'full-strength' environment trials - testing the strongest feasible policies. "
  "What would confirm it: strong policies producing large diet shifts. "
  "What would kill it: evidence that even strong policies barely move diets. "
  "What this does not claim: it does not claim any policy works, offers no policy prescription, and does not constitute medical advice."),
 "sig_lens": "The Signature lens reads the nudge literature as underpowered, and asks what full-strength policy would do.",
 "how_it_works": "Researchers study food environments through labeling trials, tax evaluations, and choice-architecture research.",
 "key_points": [
  "Labels shift purchases modestly.",
  "Soda taxes cut consumption 10-20%.",
  "Nudge effects are small.",
  "Population obesity kept rising regardless.",
  "Strong policies remain largely untested.",
 ],
 "requirements": [
  "Full-strength policy trials.",
  "Proof that strong redesign moves diets at scale.",
  "Or honest admission of environmental limits.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Thaler RH, Sunstein CR. Nudge. 2008.",
  "Cecchini M, Warin L. Labelling and tax reviews. Various; 2016-2021.",
  "Andreyeva T et al. Soda tax evaluations. Various; 2017-2022.",
  "Hawkes C et al. Food environment policy. Various; 2015-2020.",
 ],
 "demo_data": {"a": ("soda-tax consumption reduction, percent (approx)", 15.0),
               "b": ("percent scale", 100.0), "bounds": (0.08, 0.25),
               "step1": "the strongest tested policy moves consumption a sixth - while obesity rises regardless",
               "confirm": "strong policies produce large diet shifts",
               "refute": "even strong policies prove to barely move diets"},
},
# ------------------------------------------------------------------ rank 30
{
 "key": "sustainable-nutrition",
 "name": "Sustainable Nutrition: Feeding 10 Billion Well",
 "group": "Food Systems",
 "ladder_rank": 30, "ladder_tier": "advanced",
 "problem": "Healthy diets and sustainable diets may conflict - can the planet feed 10 billion people a healthy diet without ecological collapse?",
 "description": "The EAT-Lancet Commission (2019) proposed a planetary health diet - but critics noted affordability gaps, cultural impossibility, and nutritional adequacy concerns. Livestock's emissions, fertilizer limits, water scarcity, and food waste all constrain the solution space. No integrated model proves a healthy sustainable diet for 10 billion is achievable.",
 "background": "EAT-Lancet (2019) was the landmark attempt; critiques (Afshin, Hirvonen) showed the diet was unaffordable for 1.6 billion people. Sustainable-intensification research, alternative proteins, and waste-reduction programs each address pieces. As of 2026 the feasibility question is open with honest uncertainty.",
 "why_it_matters": "The answer determines whether humanity's food future is planned or improvised - the largest nutrition question of the century.",
 "sig_pointer": "The Signature system's proposed approach treats sustainable nutrition as a constrained optimization, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that sustainable nutrition is a constrained optimization: health, environment, affordability, and culture are simultaneous constraints, and the feasible region - if it exists - must be computed, not asserted. "
  "Assumptions: (1) the constraints are quantifiable; (2) the feasible region exists; (3) optimization finds it. "
  "Reasoning path: an optimization model replaces diet advocacy with computation, predicting feasible-region diets. "
  "Proposed mechanism: 'constraint-solved' sustainable diets - diets computed to satisfy all constraints. "
  "What would confirm it: computed diets satisfying health, environmental, and affordability constraints. "
  "What would kill it: proof that no diet satisfies all constraints simultaneously. "
  "What this does not claim: it does not claim sustainable diets exist, offers no dietary advice, and does not constitute medical advice."),
 "sig_lens": "The Signature lens reads the sustainability debate as uncomputed, and asks what optimization would find.",
 "how_it_works": "Researchers study sustainable nutrition through EAT-Lancet modeling, affordability analyses, and alternative-protein research.",
 "key_points": [
  "EAT-Lancet proposed the planetary health diet (2019).",
  "Critics showed it unaffordable for 1.6 billion people.",
  "Livestock emissions and water constrain solutions.",
  "No integrated model proves feasibility for 10 billion.",
  "The constraints may be jointly unsatisfiable.",
 ],
 "requirements": [
  "Computed diets satisfying all constraints.",
  "Affordability proof for the poorest.",
  "Or honest admission of infeasibility.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Willett W et al. EAT-Lancet Commission. Lancet. 2019;393:447-492.",
  "Hirvonen K et al. Affordability of the EAT-Lancet diet. Lancet Global Health. 2020;8:e73-e78.",
  "Springmann M et al. Sustainable diet modeling. Various; 2018-2022.",
  "Tilman D, Clark M. Food and environment. Various; 2014-2017.",
 ],
 "demo_data": {"a": ("people unable to afford the EAT-Lancet diet, billions (approx)", 1.6),
               "b": ("world population, billions (approx)", 8.0), "bounds": (0.12, 0.3),
               "step1": "a fifth of humanity can't afford the proposed sustainable diet - the feasibility gap",
               "confirm": "computed diets satisfy health, environmental, and affordability constraints",
               "refute": "no diet proves able to satisfy all constraints"},
},
# ------------------------------------------------------------------ rank 31
{
 "key": "nutrition-mental-health",
 "name": "Nutrition and Mental Health",
 "group": "Mechanisms",
 "ladder_rank": 31, "ladder_tier": "advanced",
 "problem": "Diet quality is linked to depression - but is the link causal, and can dietary change treat mental illness?",
 "description": "Observational studies link Mediterranean-style diets to lower depression risk; the SMILES trial (2017) found dietary intervention helped depression. But confounding is severe, trials are small, and the mechanisms (inflammation, microbiome, tryptophan) are unproven. Nutritional psychiatry is promising but preliminary.",
 "background": "The field emerged in the 2010s (Jacka, Sarris); SMILES was the first RCT of diet for depression. Follow-up trials (HELFIMED) were supportive but small. Mechanistic work on inflammation and the gut-brain axis is ongoing. As of 2026 nutritional psychiatry has pilot-trial evidence, not clinical-grade proof.",
 "why_it_matters": "If diet treats depression, it's the most accessible intervention in psychiatry; if the link is confounded, vulnerable patients are being misled.",
 "sig_pointer": "The Signature system's proposed approach tests diet-depression causality definitively, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that the diet-depression link needs definitive causal testing: large, long, well-controlled trials with mechanistic measures - not more observational associations. "
  "Assumptions: (1) causality is testable; (2) mechanisms are measurable; (3) definitive trials are feasible. "
  "Reasoning path: a causal-testing model explains the current stalemate and predicts mechanism-measured trials. "
  "Proposed mechanism: 'causality-proven' nutritional psychiatry - large trials with inflammation and microbiome measures. "
  "What would confirm it: large trials showing diet treats depression via measured mechanisms. "
  "What would kill it: null results in definitive trials. "
  "What this does not claim: it does not claim diet treats depression, offers no dietary advice, and does not constitute medical advice."),
 "sig_lens": "The Signature lens reads nutritional psychiatry as promising but unproven, and asks what definitive trials would show.",
 "how_it_works": "Researchers study nutrition and mental health through diet-depression RCTs, inflammation measures, and microbiome research.",
 "key_points": [
  "SMILES (2017) found dietary intervention helped depression.",
  "Trials are small and mechanisms unproven.",
  "Confounding in observational work is severe.",
  "Inflammation and microbiome are leading mechanisms.",
  "The field has pilot evidence, not clinical proof.",
 ],
 "requirements": [
  "Large definitive diet-depression trials.",
  "Measured causal mechanisms.",
  "Clinical-grade treatment protocols or honest nulls.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Jacka FN et al. SMILES trial. BMC Medicine. 2017;15:23.",
  "Sarris J et al. Nutritional psychiatry reviews. Various; 2015-2021.",
  "Lassale C et al. Diet and depression meta-analyses. Various; 2018-2021.",
  "Marx W et al. Nutritional psychiatry trials. Various; 2017-2023.",
 ],
 "demo_data": {"a": ("SMILES trial participants (approx)", 67.0),
               "b": ("participants needed for definitive proof (approx thousands)", 5.0), "bounds": (8.0, 20.0),
               "step1": "sixty-seven participants launched a field - definitive proof needs a hundred times more",
               "confirm": "large trials show diet treats depression via measured mechanisms",
               "refute": "null results in definitive trials"},
},
# ------------------------------------------------------------------ rank 32
{
 "key": "nutrient-timing",
 "name": "Nutrient Timing: Does When You Eat Protein Matter?",
 "group": "Meal Timing",
 "ladder_rank": 32, "ladder_tier": "advanced",
 "problem": "Athletes obsess over protein timing - the 'anabolic window' - but does nutrient timing actually matter beyond daily totals?",
 "description": "The anabolic window - protein within 30-60 minutes post-exercise - was sports-nutrition dogma; meta-analyses (Schoenfeld 2013) found timing mattered little once daily protein was equated. But chrono-nutrition suggests meal timing affects metabolism broadly; the field debates whether timing is marginal or meaningful.",
 "background": "The window concept drove supplement timing for decades; Schoenfeld's meta-analysis deflated it. But protein distribution across meals (even vs skewed) shows effects on muscle synthesis; pre-sleep protein has supportive data. As of 2026 the consensus: daily totals dominate, timing is second-order - but second-order isn't zero.",
 "why_it_matters": "Athletes and the elderly structure days around timing: knowing its true value optimizes effort allocation.",
 "sig_pointer": "The Signature system's proposed approach quantifies timing's true effect size, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that nutrient timing's value is quantifiable and context-dependent: small for the well-fed young, possibly meaningful for the elderly and the protein-marginal. "
  "Assumptions: (1) timing effects are real but small; (2) they vary by context; (3) quantification guides practice. "
  "Reasoning path: a quantified model explains the dogma-deflation cycle and predicts context-specific timing guidance. "
  "Proposed mechanism: 'effect-sized' timing guidance - recommendations scaled to measured timing benefits. "
  "What would confirm it: context-specific trials quantifying timing's added value. "
  "What would kill it: evidence that timing adds nothing in any context. "
  "What this does not claim: it does not claim timing matters, offers no dietary advice, and does not constitute medical advice."),
 "sig_lens": "The Signature lens reads the timing debate as unquantified, and asks what measurement would prescribe.",
 "how_it_works": "Researchers study nutrient timing through protein-distribution trials, pre-sleep protein studies, and chrono-nutrition research.",
 "key_points": [
  "The anabolic window was dogma; meta-analyses deflated it.",
  "Daily protein totals dominate timing.",
  "Protein distribution across meals shows effects.",
  "Pre-sleep protein has supportive data.",
  "Timing may matter most for the elderly and marginal.",
 ],
 "requirements": [
  "Quantified timing effect sizes by context.",
  "Context-specific timing guidance.",
  "Proof of where timing is worth the effort.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Schoenfeld BJ et al. Protein timing meta-analysis. Journal of the International Society of Sports Nutrition. 2013;10:53.",
  "Morton RW et al. Protein and muscle meta-analyses. Various; 2017-2018.",
  "Trommelen J, van Loon LJC. Pre-sleep protein. Various; 2016-2021.",
  "Flanagan A et al. Chrono-nutrition. Various; 2020-2023.",
 ],
 "demo_data": {"a": ("timing's share of protein's muscle effect, percent (approx)", 10.0),
               "b": ("percent scale", 100.0), "bounds": (0.05, 0.18),
               "step1": "a tenth of the effect from timing, nine-tenths from totals - the hierarchy the dogma inverted",
               "confirm": "context-specific trials quantify timing's added value",
               "refute": "timing proves to add nothing in any context"},
},
# ------------------------------------------------------------------ rank 33
{
 "key": "dietary-guidelines",
 "name": "Can Dietary Guidelines Be Trusted?",
 "group": "Policy",
 "ladder_rank": 33, "ladder_tier": "advanced",
 "problem": "Dietary guidelines shape school lunches and food policy - but they're built on the contested epidemiology above. Are they evidence-based?",
 "description": "National dietary guidelines (US DGA and equivalents) - the food pyramid's descendants - rest heavily on nutritional epidemiology's shaky foundations. Critics argue industry influence and weak evidence corrupt them; defenders argue they're the best synthesis available. The guidelines' credibility is nutrition's meta-problem.",
 "background": "The first US Dietary Goals (1977) were political as much as scientific; the pyramid (1992) and MyPlate (2011) followed. Industry lobbying influence is documented; the evidence reviews (NESR) are extensive but built on the methods critiqued above. As of 2026 guidelines are simultaneously the best available synthesis and genuinely contested.",
 "why_it_matters": "Guidelines shape institutional feeding for hundreds of millions: their trustworthiness is the foundation of nutrition policy.",
 "sig_pointer": "The Signature system's proposed approach grades guidelines by evidence certainty, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that guidelines should carry evidence grades: each recommendation labeled with its certainty (GRADE-style), so users know what's solid and what's provisional. "
  "Assumptions: (1) certainty is gradable; (2) graded guidelines retain authority; (3) honesty improves trust. "
  "Reasoning path: a graded model explains the trust crisis - overconfident weak recommendations - and predicts trust recovery. "
  "Proposed mechanism: 'certainty-graded' dietary guidelines - every recommendation with its evidence grade. "
  "What would confirm it: graded guidelines maintaining public trust better than ungraded ones. "
  "What would kill it: evidence that grading destroys guideline authority. "
  "What this does not claim: it does not claim guidelines are wrong, offers no dietary advice, and does not constitute medical advice."),
 "sig_lens": "The Signature lens reads the trust crisis as overconfidence, and asks what honest grading would restore.",
 "how_it_works": "Researchers study guidelines through NESR evidence reviews, influence analyses, and trust research.",
 "key_points": [
  "Guidelines rest on contested epidemiological foundations.",
  "Industry influence is documented.",
  "The 1977 goals were partly political.",
  "Defenders call them the best synthesis available.",
  "Overconfident weak recommendations erode trust.",
 ],
 "requirements": [
  "Certainty grading for every recommendation.",
  "Trust research on graded versus ungraded guidelines.",
  "Insulation of science from industry influence.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "US Dietary Guidelines Advisory Committee. Scientific reports. 2015, 2020.",
  "Teicholz N. Critiques of dietary guidelines. Various; 2014-2021.",
  "Marmot M et al. Guideline evidence reviews. Various; 2018-2022.",
  "Nestle M. Food Politics. 2002; updated 2013.",
 ],
 "demo_data": {"a": ("guideline recommendations with high-certainty evidence, percent (approx)", 20.0),
               "b": ("percent scale", 100.0), "bounds": (0.12, 0.3),
               "step1": "four-fifths of guidance rests on less than high certainty - the foundation's own audit",
               "confirm": "graded guidelines maintain public trust better",
               "refute": "grading proves to destroy guideline authority"},
},
# ------------------------------------------------------------------ rank 34
{
 "key": "nutrition-theory",
 "name": "A Unified Theory of Nutrition",
 "group": "Theory",
 "ladder_rank": 34, "ladder_tier": "advanced",
 "problem": "Physics has the Standard Model; nutrition has competing diet tribes. Can the field ever converge on a unified theoretical framework?",
 "description": "Nutrition lacks a unifying theory: energy-balance, carbohydrate-insulin, food-matrix, microbiome, circadian, and evolutionary models compete without integration. The field advances by trial-and-error rather than theory-driven prediction. Whether a unified framework is possible - or nutrition is irreducibly complex - is the discipline's deepest question.",
 "background": "Nutrition science grew from deficiency diseases (vitamins, 1900s-1940s) to chronic-disease epidemiology (1950s onward) without developing theoretical foundations. Systems biology and computational modeling offer integration tools. As of 2026 the field has data abundance and theory scarcity.",
 "why_it_matters": "A unified theory would convert nutrition from reactive epidemiology to predictive science - the transformation every mature science undergoes.",
 "sig_pointer": "The Signature system's proposed approach builds nutrition theory from mechanisms upward, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that nutrition theory must be built mechanism-up: validated causal mechanisms (energy balance, glycemic physiology, microbiome metabolism) integrated computationally, with competing models as special cases. "
  "Assumptions: (1) mechanisms are validatable; (2) integration is computable; (3) the integrated model predicts. "
  "Reasoning path: a mechanism-up model explains the tribe wars - each tribe owns one mechanism - and predicts theoretical convergence. "
  "Proposed mechanism: 'mechanism-integrated' nutrition theory - computational models unifying validated mechanisms. "
  "What would confirm it: integrated models predicting trial outcomes better than single-mechanism models. "
  "What would kill it: evidence that nutrition is irreducibly complex, defying unified theory. "
  "What this does not claim: it does not claim a unified theory exists, offers no dietary advice, and does not constitute medical advice."),
 "sig_lens": "The Signature lens reads the diet tribes as partial mechanisms, and asks what integration would predict.",
 "how_it_works": "Researchers study nutrition theory through systems biology, computational modeling, and mechanism-validation research.",
 "key_points": [
  "Nutrition has no unifying theoretical framework.",
  "Competing models (CIM, energy balance, matrix) lack integration.",
  "The field advances by trial-and-error.",
  "Systems biology offers integration tools.",
  "Theory scarcity amid data abundance defines the discipline.",
 ],
 "requirements": [
  "Validated causal mechanisms as theory building blocks.",
  "Integrated computational models.",
  "Predictions beating single-mechanism models in trials.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Mozaffarian D et al. Nutrition science needs. Various; 2018-2021.",
  "Hall KD et al. Computational nutrition models. Various; 2011-2022.",
  "Ludwig DS et al. CIM and theory debates. Various; 2018-2022.",
  "Blumberg J et al. Nutrition theory reviews. Various; 2019-2023.",
 ],
 "demo_data": {"a": ("unified nutrition theories with predictive success", 0.5),
               "b": ("competing nutrition models (approx)", 6.0), "bounds": (0.05, 0.15),
               "step1": "six competing models, zero unified theories - the discipline without a foundation",
               "confirm": "integrated models beat single-mechanism models in trials",
               "refute": "nutrition proves irreducibly complex"},
},
]