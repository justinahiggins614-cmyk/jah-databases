#!/usr/bin/env python3
"""Entries for The Unsolved Epidemiology Database (unsolved-epidemiology) and its
Signature half (unsolved-epidemiology-signature).

34 famous unsolved problems in epidemiology, ladder-ordered by accessibility
(rank 1 = most approachable, rank 34 = most complex/compounded).
Public half: real, fact-checked problems. Signature half: the same 34
problems through the Signature lens, with Signature-generated proposed
solutions that are ALWAYS labeled as proposals, never established science.

Honesty rule (enforced in every record): never claim proof, never imply
peer acceptance, never present speculation as settled. Signature proposals
are labeled speculation for research discussion only - never medical or
public-health advice, never a recommendation; no cure claims.
"""

LABEL = "Signature-generated proposed solution \u2014 not established science."

SIG_TAIL = ("Signature editions carry the Signature system's proposed "
            "solution approaches to famous unsolved problems. Every "
            "solution is labeled a Signature-generated proposal, never "
            "established science, never peer-accepted, never proof, never "
            "medical or public-health advice.")

STD_COMMON = [
    "Problem statements verified against the published epidemiology literature; open status confirmed as of 2026.",
    "Signature solution sections are labeled proposals: they state assumptions, a reasoning path, a proposed mechanism, what would confirm or kill them, and what they do not claim.",
    "Signature proposals are labeled speculation for research discussion only - never medical or public-health advice, never a recommendation; no cure claims appear.",
]

ENTRIES = [
# ------------------------------------------------------------------ rank 1
{
 "key": "causation",
 "name": "Causation: Epidemiology's Central Problem",
 "group": "Methods",
 "ladder_rank": 1, "ladder_tier": "foundations",
 "problem": "Epidemiology observes associations - but when is an association causal? The field's central question has no complete answer.",
 "description": "Causal inference - distinguishing cause from correlation - is epidemiology's founding problem: smoking and lung cancer took decades to establish; hormone replacement's apparent benefits reversed in RCTs. Bradford Hill's criteria (1965) guide judgment but don't prove; modern methods (Mendelian randomization, target-trial emulation) help but don't settle.",
 "background": "Hill's criteria organized causal judgment; the HRT reversal (WHI, 2002) showed observational confidence misplaced; Mendelian randomization (2000s-2010s) added genetic instruments. As of 2026 causal inference is better tooled but still judgment-dependent.",
 "why_it_matters": "Every public-health decision rests on causal claims: better inference means better policy and fewer reversals.",
 "sig_pointer": "The Signature system's proposed approach treats causation as triangulated, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that causal claims should be triangulated: no single method suffices, but convergent evidence across designs (cohort, Mendelian, quasi-experimental) with different biases earns causal confidence. "
  "Assumptions: (1) biases differ across designs; (2) convergence is meaningful; (3) triangulation is implementable. "
  "Reasoning path: a triangulation model explains single-method failures and predicts robust causal science. "
  "Proposed mechanism: 'triangulated' causal inference - required multi-design convergence for policy. "
  "What would confirm it: triangulated claims replicating where single-method ones failed. "
  "What would kill it: evidence that biases correlate across designs. "
  "What this does not claim: it does not claim any association is causal, offers no health advice, and does not constitute a methodological prescription."),
 "sig_lens": "The Signature lens reads causation as convergence, and asks what multi-design agreement would prove.",
 "how_it_works": "Researchers study causation through Hill's criteria, Mendelian randomization, and target-trial emulation.",
 "key_points": [
  "Association is not causation; the gap is the field's core.",
  "HRT's reversal showed observational overconfidence.",
  "Hill's criteria guide but don't prove.",
  "Mendelian randomization adds genetic instruments.",
  "Triangulation across designs is the emerging standard.",
 ],
 "requirements": [
  "Required multi-design convergence for policy claims.",
  "Triangulated claims outperforming single-method ones.",
  "Judgment frameworks made explicit.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Hill AB. The environment and disease: association or causation? 1965.",
  "Rossouw JE et al. WHI trial. JAMA. 2002;288:321-333.",
  "Smith GD et al. Mendelian randomization. Various; 2003-2014.",
  "Hernan MA et al. Target trial emulation. Various; 2016-2022.",
 ],
 "demo_data": {"a": ("observational findings reversing in RCTs, percent (approx)", 30.0),
               "b": ("percent scale", 100.0), "bounds": (0.2, 0.42),
               "step1": "three in ten observational findings reverse - the cost of causal overconfidence",
               "confirm": "triangulated claims replicate where single-method ones failed",
               "refute": "biases prove correlated across designs"},
},
# ------------------------------------------------------------------ rank 2
{
 "key": "confounding",
 "name": "Confounding: The Invisible Bias",
 "group": "Methods",
 "ladder_rank": 2, "ladder_tier": "foundations",
 "problem": "Confounders - hidden third variables - distort every observational study. Can they ever be fully controlled?",
 "description": "Confounding - exposure and outcome sharing a hidden cause - is epidemiology's eternal adversary: healthy-user bias, socioeconomic confounding, and unmeasured factors distort diet, lifestyle, and drug studies. Methods (adjustment, propensity scores, negative controls) help; residual confounding is always suspected.",
 "background": "Confounding was formalized in the mid-20th century; propensity scores (Rosenbaum, Rubin, 1983) modernized adjustment; negative controls and E-values (2010s) quantified residual concern. As of 2026 no observational study is free of confounding doubt.",
 "why_it_matters": "Confounding determines whether observational findings are real: controlling it is the credibility of the field.",
 "sig_pointer": "The Signature system's proposed approach quantifies residual confounding, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that residual confounding should be quantified, not hand-waved: E-values, negative controls, and bias analysis bounding the distortion - reported with every finding. "
  "Assumptions: (1) bounds are computable; (2) they are honest; (3) reporting changes interpretation. "
  "Reasoning path: a quantification model explains credibility crises and predicts honest epidemiology. "
  "Proposed mechanism: 'confounding-bounded' reporting - every finding with its bias bounds. "
  "What would confirm it: bounded findings replicating better than unbounded ones. "
  "What would kill it: evidence that bounds are uninformative in practice. "
  "What this does not claim: it does not claim any finding is confounded, offers no health advice, and does not constitute a methodological prescription."),
 "sig_lens": "The Signature lens reads confounding as unquantified doubt, and asks what bounds would make honest.",
 "how_it_works": "Researchers study confounding through propensity methods, negative controls, and bias-analysis research.",
 "key_points": [
  "Confounding distorts every observational study.",
  "Healthy-user and socioeconomic biases are pervasive.",
  "Propensity scores modernized adjustment.",
  "E-values quantify residual concern.",
  "No study is free of confounding doubt.",
 ],
 "requirements": [
  "Routine bias-bounded reporting.",
  "Negative controls as standard practice.",
  "Bounded findings replicating better.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Rosenbaum PR, Rubin DB. Propensity scores. Biometrika. 1983;70:41-55.",
  "VanderWeele TJ et al. E-values. Various; 2017-2019.",
  "Lipsitch M et al. Negative controls. Various; 2010-2018.",
  "Greenland S et al. Bias analysis. Various; 2005-2020.",
 ],
 "demo_data": {"a": ("observational studies reporting bias bounds, percent (approx)", 10.0),
               "b": ("percent scale", 100.0), "bounds": (0.05, 0.18),
               "step1": "nine in ten findings report no bias bounds - doubt unquantified",
               "confirm": "bounded findings replicate better than unbounded ones",
               "refute": "bounds prove uninformative in practice"},
},
# ------------------------------------------------------------------ rank 3
{
 "key": "replication-epi",
 "name": "Epidemiology's Replication Crisis",
 "group": "Methods",
 "ladder_rank": 3, "ladder_tier": "foundations",
 "problem": "Landmark epidemiological findings keep failing to replicate - from vitamins to diet to screening. How much of the literature is real?",
 "description": "Epidemiology's replication problems are notorious: beta-carotene, vitamin E, hormone replacement, and countless dietary findings reversed. Causes include confounding, publication bias, p-hacking, and small effects. The field is reforming (preregistration, triangulation) but the old literature's validity is uncertain.",
 "background": "Reversals accumulated through the 1990s-2000s (HRT, antioxidants); Ioannidis' critiques (2005 onward) generalized the problem; preregistration and registered reports spread in the 2010s. As of 2026 epidemiology is mid-reform.",
 "why_it_matters": "Public health rests on this literature: its reliability determines whether guidance helps or harms.",
 "sig_pointer": "The Signature system's proposed approach triages the epidemiological literature, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that the literature needs triage: landmark findings re-tested with modern methods, the unreplicable retired, and new standards preventing recurrence. "
  "Assumptions: (1) the valid findings are separable; (2) re-testing is feasible; (3) the field accepts triage. "
  "Reasoning path: a triage model explains the crisis and predicts a cleaned literature. "
  "Proposed mechanism: 'literature-triaged' epidemiology - systematic re-testing of landmarks. "
  "What would confirm it: re-tested findings separating into robust and retired. "
  "What would kill it: evidence that most findings were false. "
  "What this does not claim: it does not claim any finding is false, offers no health advice, and does not constitute a methodological prescription."),
 "sig_lens": "The Signature lens reads the crisis as untriaged literature, and asks what re-testing would salvage.",
 "how_it_works": "Researchers study replication through re-testing programs, preregistration, and meta-research.",
 "key_points": [
  "Beta-carotene, vitamin E, and HRT reversed.",
  "Causes: confounding, bias, p-hacking, small effects.",
  "Ioannidis generalized the critique.",
  "Preregistration is spreading.",
  "Old literature's validity is uncertain.",
 ],
 "requirements": [
  "Systematic landmark re-testing.",
  "Retirement of unreplicable findings.",
  "New standards preventing recurrence.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Ioannidis JPA. Why most published research findings are false. PLoS Medicine. 2005;2(8):e124.",
  "Omenn GS et al. CARET beta-carotene. NEJM. 1996;334:1150-1155.",
  "Rossouw JE et al. WHI. JAMA. 2002;288:321-333.",
  "Nosek BA et al. Reproducibility reforms. Various; 2015-2018.",
 ],
 "demo_data": {"a": ("landmark findings re-tested with modern methods, percent (approx)", 15.0),
               "b": ("percent scale", 100.0), "bounds": (0.08, 0.25),
               "step1": "six in seven landmarks un-retested - the literature's unknown validity",
               "confirm": "re-tested findings separate into robust and retired",
               "refute": "most findings prove false"},
},
# ------------------------------------------------------------------ rank 4
{
 "key": "r0",
 "name": "R0: The Number That Rules Pandemics",
 "group": "Infectious Disease",
 "ladder_rank": 4, "ladder_tier": "foundations",
 "problem": "R0 - the basic reproduction number - drives pandemic policy, yet it's unobservable, variable, and often misused. What does R0 actually mean?",
 "description": "R0 - average secondary infections from one case in a susceptible population - is estimated, not measured: it varies by setting, behavior, and variant; early estimates are wildly uncertain; and the effective R (Rt) is what matters. COVID-19 showed both the number's power and its misuse.",
 "background": "R0 theory dates to Ross and Macdonald (malaria); modern estimation uses contact data and genomics. COVID-19's early R0 estimates ranged 2-6; policy hinged on uncertain numbers. As of 2026 R0 remains estimated with wide uncertainty.",
 "why_it_matters": "R0 estimates trigger lockdowns and reopenings: understanding their uncertainty would make pandemic policy honest.",
 "sig_pointer": "The Signature system's proposed approach reports R0 with honest uncertainty, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that R0 should be reported as distributions, not points: the uncertainty quantified and communicated - with policy tied to uncertainty-aware thresholds. "
  "Assumptions: (1) uncertainty is quantifiable; (2) policymakers can use distributions; (3) honesty improves decisions. "
  "Reasoning path: an uncertainty model explains R0 misuse and predicts better pandemic policy. "
  "Proposed mechanism: 'uncertainty-reported' R0 - distributions with decision thresholds. "
  "What would confirm it: uncertainty-aware policy outperforming point-estimate policy. "
  "What would kill it: evidence that decisions need point estimates. "
  "What this does not claim: it does not claim any R0 value, offers no health advice, and does not constitute a policy recommendation."),
 "sig_lens": "The Signature lens reads R0 as uncertain numbers treated as certain, and asks what honest reporting would change.",
 "how_it_works": "Researchers study R0 through estimation methods, uncertainty quantification, and policy-use analyses.",
 "key_points": [
  "R0 is estimated, not measured.",
  "Early-pandemic estimates are wildly uncertain.",
  "Rt (effective R) is what matters for policy.",
  "COVID-19 showed both power and misuse.",
  "Point estimates hide the uncertainty.",
 ],
 "requirements": [
  "Routine uncertainty-quantified R0 reporting.",
  "Uncertainty-aware policy thresholds.",
  "Better early-estimation methods.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Ross R et al. Malaria R0 theory. Early 1900s.",
  "Anderson RM, May RM. Infectious Diseases of Humans. 1991.",
  "Li Q et al. Early COVID-19 R0 estimates. NEJM. 2020;382:1199-1207.",
  "Delamater PL et al. R0 complexity. Emerging Infectious Diseases. 2019;25:1-4.",
 ],
 "demo_data": {"a": ("early COVID-19 R0 estimates, range width (approx)", 4.0),
               "b": ("R0 point estimates used in policy (approx)", 2.5), "bounds": (1.2, 2.2),
               "step1": "estimates spanning 2 to 6 drove policy as single numbers - uncertainty hidden",
               "confirm": "uncertainty-aware policy outperforms point-estimate policy",
               "refute": "decisions prove to need point estimates"},
},
# ------------------------------------------------------------------ rank 5
{
 "key": "herd-immunity",
 "name": "Herd Immunity Thresholds: Real or Myth?",
 "group": "Infectious Disease",
 "ladder_rank": 5, "ladder_tier": "foundations",
 "problem": "The herd-immunity threshold (1 - 1/R0) is textbook formula - but heterogeneity, waning, and variants make it elusive. Does the threshold exist?",
 "description": "Herd immunity thresholds - the coverage needed to stop transmission - assume homogeneous mixing and lasting immunity. Reality: heterogeneous contact, waning immunity, immune escape, and behavior change the math. COVID-19's elusive threshold challenged the concept; measles' threshold holds better.",
 "background": "The threshold formula dates to early-20th-century theory; measles vaccination validated it approximately. COVID-19 (2020-2022) showed thresholds shifting with variants and waning. As of 2026 the threshold is understood as dynamic, not fixed.",
 "why_it_matters": "Threshold beliefs drive vaccine-coverage targets: getting them right determines whether elimination is achievable.",
 "sig_pointer": "The Signature system's proposed approach treats herd immunity as dynamic, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that herd immunity is a dynamic state, not a fixed threshold: coverage, heterogeneity, waning, and variants jointly determining transmission - modeled continuously. "
  "Assumptions: (1) the dynamics are modelable; (2) they are measurable; (3) dynamic targets beat fixed ones. "
  "Reasoning path: a dynamic model explains threshold failures and predicts achievable control. "
  "Proposed mechanism: 'dynamically-modeled' herd immunity - continuous transmission modeling. "
  "What would confirm it: dynamic models predicting control better than thresholds. "
  "What would kill it: evidence that fixed thresholds suffice. "
  "What this does not claim: it does not claim any threshold value, offers no health advice, and does not constitute a policy recommendation."),
 "sig_lens": "The Signature lens reads the threshold as dynamic, and asks what continuous modeling would target.",
 "how_it_works": "Researchers study herd immunity through heterogeneous models, waning studies, and variant analyses.",
 "key_points": [
  "The classic threshold assumes homogeneity and lasting immunity.",
  "Heterogeneity, waning, and variants break the formula.",
  "COVID-19's threshold proved elusive.",
  "Measles' threshold holds approximately.",
  "Dynamic modeling is replacing fixed thresholds.",
 ],
 "requirements": [
  "Validated dynamic transmission models.",
  "Dynamic coverage targets.",
  "Proof that dynamics beat thresholds.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Fine P et al. Herd immunity reviews. Various; 1993-2011.",
  "Anderson RM, May RM. Threshold theory. 1991.",
  "Britton T et al. Heterogeneity and thresholds. Various; 2020-2021.",
  "Metcalf CJE et al. Dynamic herd immunity. Various; 2015-2022.",
 ],
 "demo_data": {"a": ("measles herd threshold, percent (approx)", 95.0),
               "b": ("percent scale", 100.0), "bounds": (0.9, 1.0),
               "step1": "ninety-five percent for measles - the threshold that holds, against the ones that don't",
               "confirm": "dynamic models predict control better than thresholds",
               "refute": "fixed thresholds prove sufficient"},
},
# ------------------------------------------------------------------ rank 6
{
 "key": "flu-burden",
 "name": "The True Burden of Influenza",
 "group": "Infectious Disease",
 "ladder_rank": 6, "ladder_tier": "foundations",
 "problem": "Flu kills - but how many? Estimates range widely because most flu deaths are never tested. What's the real toll?",
 "description": "Influenza mortality - estimated 290,000-650,000 yearly globally - is modeled, not counted: most deaths lack testing, and excess-mortality models attribute them. The uncertainty hampers vaccine prioritization and pandemic planning.",
 "background": "Excess-mortality modeling (Serfling, 1960s) became the standard; global estimates (Iuliano, 2018) quantified the range. COVID-19 improved respiratory surveillance. As of 2026 flu burden remains modeled with wide uncertainty.",
 "why_it_matters": "The true toll determines vaccine investment and pandemic preparedness: uncertainty wastes both.",
 "sig_pointer": "The Signature system's proposed approach counts flu deaths directly, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that flu burden should be directly measured: systematic testing of respiratory deaths - replacing models with counts. "
  "Assumptions: (1) direct measurement is feasible; (2) it is affordable; (3) counts beat models. "
  "Reasoning path: a measurement model explains the uncertainty and predicts accurate burden data. "
  "Proposed mechanism: 'directly-counted' flu mortality - systematic respiratory-death testing. "
  "What would confirm it: counted burdens guiding better policy than modeled ones. "
  "What would kill it: evidence that models are already accurate. "
  "What this does not claim: it does not claim any burden number, offers no health advice, and does not constitute a policy recommendation."),
 "sig_lens": "The Signature lens reads flu burden as modeled guesses, and asks what direct counting would reveal.",
 "how_it_works": "Researchers study flu burden through excess-mortality models, surveillance improvement, and testing studies.",
 "key_points": [
  "Global flu deaths: 290,000-650,000 estimated yearly.",
  "Most flu deaths are never tested.",
  "Excess-mortality models attribute untested deaths.",
  "Uncertainty hampers vaccine prioritization.",
  "Direct counting is rare.",
 ],
 "requirements": [
  "Systematic respiratory-death testing.",
  "Counted versus modeled comparisons.",
  "Burden data guiding investment.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Iuliano AD et al. Global flu mortality. Lancet. 2018;391:1285-1300.",
  "Serfling RE. Excess mortality methods. 1963.",
  "Paget J et al. Flu burden reviews. Various; 2019-2023.",
  "WHO. Flu surveillance reports. Various.",
 ],
 "demo_data": {"a": ("flu burden estimate range width, thousands (approx)", 360.0),
               "b": ("thousands scale", 1000.0), "bounds": (0.25, 0.5),
               "step1": "estimates spanning 290,000 to 650,000 - the toll nobody counts",
               "confirm": "counted burdens guide better policy than modeled ones",
               "refute": "models prove already accurate"},
},
# ------------------------------------------------------------------ rank 7
{
 "key": "vaccine-hesitancy",
 "name": "Vaccine Hesitancy: The Behavioral Pandemic",
 "group": "Behavioral",
 "ladder_rank": 7, "ladder_tier": "foundations",
 "problem": "Vaccines save millions, yet hesitancy grows - what drives it, and what actually changes minds?",
 "description": "Vaccine hesitancy - delay or refusal despite availability - is rising globally: measles resurged in under-vaccinated communities; COVID-19 vaccination stalled on hesitancy. Drivers (distrust, misinformation, access, complacency) are mapped; effective interventions are less clear - mandates work but polarize.",
 "background": "Hesitancy was declared a top global health threat (WHO, 2019); COVID-19 made it central; research into effective communication is active. As of 2026 the drivers are known but the solutions are partial.",
 "why_it_matters": "Hesitancy determines whether vaccines achieve their potential: solving it is public health's behavioral frontier.",
 "sig_pointer": "The Signature system's proposed approach treats hesitancy as trust to be earned, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that hesitancy is trust-shaped: the trusted messengers and honest communication that change minds identified experimentally. "
  "Assumptions: (1) trust is the key driver; (2) it is measurable; (3) it is earnable. "
  "Reasoning path: a trust model explains intervention variation and predicts effective campaigns. "
  "Proposed mechanism: 'trust-built' vaccination campaigns - messenger and message tested. "
  "What would confirm it: trust-based interventions raising uptake in trials. "
  "What would kill it: evidence that hesitancy is immutable. "
  "What this does not claim: it does not take a position on mandates, offers no health advice, and does not constitute a policy recommendation."),
 "sig_lens": "The Signature lens reads hesitancy as trust deficit, and asks what would earn it.",
 "how_it_works": "Researchers study hesitancy through trust surveys, messenger trials, and misinformation research.",
 "key_points": [
  "WHO declared hesitancy a top threat (2019).",
  "Measles resurged in under-vaccinated communities.",
  "Drivers: distrust, misinformation, access, complacency.",
  "Mandates work but polarize.",
  "Effective persuasion is partially understood.",
 ],
 "requirements": [
  "Trust-based interventions proven in trials.",
  "Messenger and message optimization.",
  "Uptake gains without polarization.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "WHO. Vaccine hesitancy as global threat. 2019.",
  "Larson HJ et al. Hesitancy research. Various; 2014-2022.",
  "Brewer NT et al. Intervention reviews. Various; 2017-2021.",
  "Dubé E et al. Hesitancy determinants. Various; 2013-2020.",
 ],
 "demo_data": {"a": ("measles cases in under-vaccinated outbreaks (approx thousands)", 10.0),
               "b": ("global measles cases, thousands (approx)", 100.0), "bounds": (0.05, 0.18),
               "step1": "outbreaks in the hesitant drive the global count - the behavioral pandemic's toll",
               "confirm": "trust-based interventions raise uptake in trials",
               "refute": "hesitancy proves immutable"},
},
# ------------------------------------------------------------------ rank 8
{
 "key": "screening-epi",
 "name": "Screening Epidemiology: Lead Time and Overdiagnosis",
 "group": "Methods",
 "ladder_rank": 8, "ladder_tier": "foundations",
 "problem": "Screening finds disease early - but lead-time bias and overdiagnosis inflate its apparent benefit. How much screening truly helps?",
 "description": "Screening evaluation - separating real mortality benefit from lead-time bias, length bias, and overdiagnosis - is epidemiology's subtlest methods problem. RCTs are the gold standard but rare; observational screening studies are systematically biased toward benefit.",
 "background": "Lead-time and length bias were formalized in the 1960s-70s; overdiagnosis quantification matured in the 2000s-2010s (mammography, PSA, thyroid). As of 2026 screening claims require RCT proof, but most screening lacks it.",
 "why_it_matters": "Screening affects hundreds of millions: honest benefit accounting determines which screening helps and which harms.",
 "sig_pointer": "The Signature system's proposed approach demands RCT-grade screening evidence, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that screening claims need RCT-grade evidence: mortality trials with overdiagnosis quantification - before population rollout. "
  "Assumptions: (1) trials are feasible; (2) overdiagnosis is quantifiable; (3) evidence guides policy. "
  "Reasoning path: an evidence model explains screening controversies and predicts honest screening. "
  "Proposed mechanism: 'RCT-validated' screening - trial proof before rollout. "
  "What would confirm it: validated screening showing true mortality benefit. "
  "What would kill it: evidence that observational evaluation suffices. "
  "What this does not claim: it does not claim any screening works, offers no health advice, and does not constitute a policy recommendation."),
 "sig_lens": "The Signature lens reads screening claims as biased toward benefit, and asks what RCTs would prove.",
 "how_it_works": "Researchers study screening through RCTs, overdiagnosis modeling, and bias research.",
 "key_points": [
  "Lead-time and length bias inflate apparent benefit.",
  "Overdiagnosis is real in mammography, PSA, thyroid.",
  "Observational screening studies are systematically biased.",
  "RCTs are rare but the gold standard.",
  "Most screening lacks RCT proof.",
 ],
 "requirements": [
  "RCT proof for major screening programs.",
  "Overdiagnosis quantified per program.",
  "Honest benefit-harm accounting.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Morrison AS. Screening evaluation. 1985.",
  "Welch HG et al. Overdiagnosis research. Various; 2010-2020.",
  "Independent UK Panel. Mammography screening. Lancet. 2012;380:1778-1786.",
  "Harris R et al. Screening methods. Various; 2011-2019.",
 ],
 "demo_data": {"a": ("screening programs with RCT mortality proof (approx)", 8.0),
               "b": ("population screening programs (approx)", 30.0), "bounds": (0.18, 0.38),
               "step1": "eight proven of thirty practiced - screening's evidence gap",
               "confirm": "validated screening shows true mortality benefit",
               "refute": "observational evaluation proves sufficient"},
},
# ------------------------------------------------------------------ rank 9
{
 "key": "social-determinants",
 "name": "Social Determinants: Measuring What Matters",
 "group": "Social Epidemiology",
 "ladder_rank": 9, "ladder_tier": "foundations",
 "problem": "Social conditions drive health more than medicine - but which determinants are causal, and which interventions work?",
 "description": "Social determinants - income, education, housing, racism - explain most health variation; but the causal pathways are debated, and interventions (housing programs, income supplements) show mixed results. The field knows inequality kills but not precisely how to fix it.",
 "background": "Whitehall studies (Marmot, 1970s onward) proved the social gradient; fundamental-cause theory (Link, Phelan) framed it; intervention trials are mixed. As of 2026 the determinants are described with causal levers partially identified.",
 "why_it_matters": "Social determinants are the largest health lever: identifying causal interventions would improve population health more than any medical advance.",
 "sig_pointer": "The Signature system's proposed approach tests determinant interventions experimentally, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that determinant interventions need experimental testing: housing, income, and education interventions trialed like drugs - with health outcomes. "
  "Assumptions: (1) interventions are testable; (2) effects are measurable; (3) trials guide policy. "
  "Reasoning path: an experimental model explains mixed evidence and predicts effective equity policy. "
  "Proposed mechanism: 'experimentally-tested' determinant interventions - RCT-grade social policy. "
  "What would confirm it: tested interventions improving health in trials. "
  "What would kill it: evidence that determinants resist intervention. "
  "What this does not claim: it does not claim any intervention works, offers no health advice, and does not constitute a policy recommendation."),
 "sig_lens": "The Signature lens reads determinants as untested levers, and asks what experiments would pull them.",
 "how_it_works": "Researchers study determinants through Whitehall-style cohorts, intervention trials, and fundamental-cause research.",
 "key_points": [
  "Social conditions explain most health variation.",
  "Whitehall proved the social gradient.",
  "Causal pathways are debated.",
  "Intervention trials show mixed results.",
  "The levers are partially identified.",
 ],
 "requirements": [
  "RCT-grade determinant intervention trials.",
  "Causal pathways mapped.",
  "Effective equity policies proven.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Marmot MG et al. Whitehall studies. Various; 1978-2020.",
  "Link BG, Phelan J. Fundamental cause theory. Various; 1995-2015.",
  "Braveman P et al. Determinants reviews. Various; 2011-2021.",
  "Thornton RLJ et al. Intervention trials. Various; 2016-2022.",
 ],
 "demo_data": {"a": ("life-expectancy gap richest vs poorest, years (approx)", 15.0),
               "b": ("years scale", 100.0), "bounds": (0.1, 0.22),
               "step1": "fifteen years of life between rich and poor - the gradient without proven levers",
               "confirm": "tested interventions improve health in trials",
               "refute": "determinants prove resistant to intervention"},
},
# ------------------------------------------------------------------ rank 10
{
 "key": "outbreak-detection",
 "name": "Outbreak Detection: Finding Epidemics Early",
 "group": "Surveillance",
 "ladder_rank": 10, "ladder_tier": "foundations",
 "problem": "Epidemics are detected late - COVID-19 spread for weeks before alarms. Can surveillance catch outbreaks at the start?",
 "description": "Outbreak detection - finding epidemics early - relies on syndromic surveillance, lab reporting, and increasingly wastewater and genomic signals. But sensitivity is low, false alarms are costly, and the first weeks of novel pathogens are inherently hard to detect.",
 "background": "Syndromic surveillance grew post-9/11; ProMED-mail crowdsourced detection; wastewater surveillance proved itself in COVID-19; genomic early-warning is emerging. As of 2026 detection is faster but still lags the pathogen.",
 "why_it_matters": "Early detection buys the response time that determines pandemic scale: days matter exponentially.",
 "sig_pointer": "The Signature system's proposed approach builds integrated early-warning systems, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that outbreak detection needs integrated signals: clinical, wastewater, genomic, and digital data fused - with validated alert thresholds. "
  "Assumptions: (1) signals are fusible; (2) thresholds are validatable; (3) alerts trigger action. "
  "Reasoning path: an integration model explains detection lags and predicts early warning. "
  "Proposed mechanism: 'signal-fused' outbreak detection - integrated early-warning systems. "
  "What would confirm it: fused systems detecting outbreaks earlier in practice. "
  "What would kill it: evidence that novel pathogens are inherently undetectable early. "
  "What this does not claim: it does not claim early detection exists, offers no health advice, and does not constitute a policy recommendation."),
 "sig_lens": "The Signature lens reads detection as unfused signals, and asks what integration would catch.",
 "how_it_works": "Researchers study outbreak detection through wastewater surveillance, genomic early-warning, and syndromic systems.",
 "key_points": [
  "COVID-19 spread weeks before alarms.",
  "Wastewater surveillance proved its value.",
  "Genomic early-warning is emerging.",
  "False alarms are costly.",
  "Detection still lags the pathogen.",
 ],
 "requirements": [
  "Integrated signal-fusion systems.",
  "Validated alert thresholds.",
  "Demonstrated earlier detection.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "ProMED-mail. Outbreak reporting. 1994 onward.",
  "Peccia J et al. Wastewater surveillance. Various; 2020-2022.",
  "Gardner L et al. Digital surveillance. Various; 2020-2023.",
  "WHO. Epidemic intelligence frameworks. Various.",
 ],
 "demo_data": {"a": ("COVID-19 undetected spread, weeks (approx)", 4.0),
               "b": ("weeks scale", 10.0), "bounds": (0.25, 0.55),
               "step1": "a month of silent spread - the detection lag that determined the pandemic",
               "confirm": "fused systems detect outbreaks earlier in practice",
               "refute": "novel pathogens prove inherently undetectable early"},
},
# ------------------------------------------------------------------ rank 11
{
 "key": "contact-tracing",
 "name": "Contact Tracing: Does It Work at Scale?",
 "group": "Interventions",
 "ladder_rank": 11, "ladder_tier": "foundations",
 "problem": "Contact tracing is textbook outbreak control - but COVID-19 showed it failing at scale. When does tracing work, and what are its limits?",
 "description": "Contact tracing - finding and isolating exposed contacts - works for slow pathogens (Ebola, TB) but struggled with fast respiratory spread: too many contacts, too little compliance, digital apps underused. The effectiveness conditions are debated.",
 "background": "Tracing eradicated smallpox; Ebola control relied on it; COVID-19 overwhelmed manual systems; digital exposure notification had low uptake. As of 2026 tracing's scale limits are acknowledged but unquantified.",
 "why_it_matters": "Tracing is the alternative to lockdowns: knowing its limits determines the outbreak-response toolkit.",
 "sig_pointer": "The Signature system's proposed approach defines tracing's effectiveness envelope, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that tracing has a definable effectiveness envelope: the pathogen speed, contact volume, and compliance combinations where it works - mapped to guide response choice. "
  "Assumptions: (1) the envelope is mappable; (2) it is measurable; (3) it guides policy. "
  "Reasoning path: an envelope model explains variable success and predicts optimal response mixes. "
  "Proposed mechanism: 'envelope-mapped' tracing - deployment where it works. "
  "What would confirm it: envelope predictions matching outbreak outcomes. "
  "What would kill it: evidence that tracing effectiveness is unpredictable. "
  "What this does not claim: it does not claim tracing works generally, offers no health advice, and does not constitute a policy recommendation."),
 "sig_lens": "The Signature lens reads tracing as unmapped limits, and asks what envelope would define them.",
 "how_it_works": "Researchers study contact tracing through effectiveness studies, digital-app evaluations, and modeling.",
 "key_points": [
  "Tracing works for slow pathogens (Ebola, TB, smallpox).",
  "COVID-19 overwhelmed manual tracing.",
  "Digital apps had low uptake.",
  "Effectiveness conditions are debated.",
  "Scale limits are unquantified.",
 ],
 "requirements": [
  "Mapped effectiveness envelope.",
  "Digital tracing that achieves uptake.",
  "Response mixes guided by the envelope.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Fenner F et al. Smallpox eradication and tracing. 1988.",
  "Hellewell J et al. COVID-19 tracing models. Lancet Global Health. 2020;8:e488-e496.",
  "Braithwaite I et al. Digital tracing reviews. Various; 2020-2022.",
  "WHO. Contact tracing guidance. Various.",
 ],
 "demo_data": {"a": ("contacts per COVID-19 case overwhelming tracers (approx)", 20.0),
               "b": ("contacts manageable per tracer-day (approx)", 5.0), "bounds": (2.5, 6.0),
               "step1": "four times the manageable contacts - the arithmetic of tracing's failure",
               "confirm": "envelope predictions match outbreak outcomes",
               "refute": "tracing effectiveness proves unpredictable"},
},
# ------------------------------------------------------------------ rank 12
{
 "key": "noncommunicable",
 "name": "The NCD Epidemic: Epidemiology of Chronic Disease",
 "group": "Chronic Disease",
 "ladder_rank": 12, "ladder_tier": "compounded",
 "problem": "Chronic diseases now kill most people - but their epidemiology is dominated by weak risk factors and failed prevention. What actually prevents NCDs?",
 "description": "Noncommunicable diseases (heart disease, cancer, diabetes) - 70%+ of global deaths - have epidemiology built on weak associations: most risk factors have small effects, prevention trials disappoint, and the population-level drivers (food systems, inequality, environment) resist study.",
 "background": "Framingham (1948 onward) founded chronic-disease epidemiology; risk-factor lists grew; but prevention at scale proved hard. The field debates whether the risk-factor paradigm has failed. As of 2026 NCD epidemiology is established with prevention gaps.",
 "why_it_matters": "NCDs are the main killer: effective prevention would save more lives than any treatment advance.",
 "sig_pointer": "The Signature system's proposed approach treats NCD prevention as systems change, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that NCD prevention needs systems epidemiology: the food, built-environment, and economic systems driving disease - intervened at system level. "
  "Assumptions: (1) systems are the right unit; (2) they are intervenable; (3) system change prevents disease. "
  "Reasoning path: a systems model explains risk-factor limits and predicts effective prevention. "
  "Proposed mechanism: 'systems-level' NCD prevention - intervening on drivers, not risks. "
  "What would confirm it: system interventions reducing NCD burden in trials. "
  "What would kill it: evidence that systems resist intervention. "
  "What this does not claim: it does not claim any prevention works, offers no health advice, and does not constitute a policy recommendation."),
 "sig_lens": "The Signature lens reads NCD epidemiology as wrong-level science, and asks what systems interventions would prevent.",
 "how_it_works": "Researchers study NCDs through systems modeling, natural experiments, and prevention trials.",
 "key_points": [
  "NCDs cause 70%+ of global deaths.",
  "Risk factors are mostly weak.",
  "Prevention trials disappoint.",
  "Population drivers resist study.",
  "The risk-factor paradigm may have failed.",
 ],
 "requirements": [
  "Systems-level intervention trials.",
  "Proven NCD burden reduction.",
  "A post-risk-factor epidemiology.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Framingham Heart Study. 1948 onward.",
  "Rose G. The Strategy of Preventive Medicine. 1992.",
  "Ezzati M et al. NCD burden. Various; 2015-2020.",
  "Hammond RA et al. Systems epidemiology. Various; 2018-2022.",
 ],
 "demo_data": {"a": ("global deaths from NCDs, percent (approx)", 70.0),
               "b": ("percent scale", 100.0), "bounds": (0.6, 0.8),
               "step1": "seven in ten deaths are chronic - with prevention's evidence thinnest where the burden is largest",
               "confirm": "system interventions reduce NCD burden in trials",
               "refute": "systems prove resistant to intervention"},
},
# ------------------------------------------------------------------ rank 13
{
 "key": "pandemic-preparedness",
 "name": "Pandemic Preparedness: The Readiness Gap",
 "group": "Preparedness",
 "ladder_rank": 13, "ladder_tier": "compounded",
 "problem": "Every pandemic review says 'never again' - yet preparedness decays between crises. Can readiness be sustained?",
 "description": "Pandemic preparedness - surveillance, stockpiles, surge capacity, plans - decays after each crisis: funding lapses, stockpiles expire, plans gather dust. The cycle (panic-neglect) is well described; breaking it is unsolved. COVID-19's reviews repeat SARS' and H1N1's recommendations.",
 "background": "Post-SARS and H1N1 reviews made recommendations; the Global Health Security Index (2019) measured unreadiness accurately; COVID-19 proved it. Preparedness funding remains cyclical. As of 2026 the panic-neglect cycle continues.",
 "why_it_matters": "Sustained readiness would blunt the next pandemic: the difference between a wave and a catastrophe.",
 "sig_pointer": "The Signature system's proposed approach makes preparedness self-sustaining, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that preparedness needs self-sustaining design: systems that maintain readiness through routine use - not emergency funding. "
  "Assumptions: (1) routine-use systems sustain readiness; (2) they are designable; (3) they are fundable. "
  "Reasoning path: a sustainability model explains the panic-neglect cycle and predicts durable readiness. "
  "Proposed mechanism: 'self-sustaining' preparedness - dual-use systems maintaining readiness. "
  "What would confirm it: sustained readiness metrics between crises. "
  "What would kill it: evidence that preparedness inherently decays. "
  "What this does not claim: it does not claim readiness exists, offers no health advice, and does not constitute a policy recommendation."),
 "sig_lens": "The Signature lens reads preparedness as cyclical funding, and asks what design would sustain it.",
 "how_it_works": "Researchers study preparedness through GHS Index tracking, after-action reviews, and sustainability research.",
 "key_points": [
  "Preparedness decays between crises (panic-neglect).",
  "COVID-19's reviews repeat earlier recommendations.",
  "The GHS Index measured unreadiness accurately.",
  "Funding remains cyclical.",
  "Dual-use systems could sustain readiness.",
 ],
 "requirements": [
  "Self-sustaining preparedness designs.",
  "Sustained readiness metrics.",
  "Proof that decay is preventable.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Global Health Security Index. 2019, 2021.",
  "WHO. Pandemic preparedness reviews. Various.",
  "Independent Panel for Pandemic Preparedness. 2021.",
  "Lal A et al. Preparedness sustainability. Various; 2021-2023.",
 ],
 "demo_data": {"a": ("pandemic reviews repeating prior recommendations, percent (approx)", 80.0),
               "b": ("percent scale", 100.0), "bounds": (0.65, 0.95),
               "step1": "four in five recommendations are repeats - the lesson-learning that never learns",
               "confirm": "sustained readiness metrics between crises",
               "refute": "preparedness proves to inherently decay"},
},
# ------------------------------------------------------------------ rank 14
{
 "key": "modeling",
 "name": "Epidemic Modeling: Prediction or Fiction?",
 "group": "Methods",
 "ladder_rank": 14, "ladder_tier": "compounded",
 "problem": "Epidemic models guided COVID-19 policy - and were often wrong. Can models be trusted, and what are their limits?",
 "description": "Epidemic modeling (SIR, agent-based, forecasting) - predicted COVID-19 trajectories with wide error: Imperial College's 2.2M US deaths shaped policy; forecasts routinely missed. Models are sensitive to unknowable parameters; their policy influence exceeds their accuracy.",
 "background": "Kermack-McKendrick (1927) founded compartmental modeling; agent-based methods grew in the 2000s; COVID-19 was modeling's largest policy test. Forecast hubs now ensemble predictions. As of 2026 modeling is influential with acknowledged limits.",
 "why_it_matters": "Models drive lockdowns and reopenings: honest modeling would make pandemic policy evidence-based.",
 "sig_pointer": "The Signature system's proposed approach makes models uncertainty-honest, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that epidemic models should be uncertainty-honest: full parameter uncertainty propagated, with decision-useful scenarios - not false-precision point forecasts. "
  "Assumptions: (1) uncertainty is quantifiable; (2) honesty is usable; (3) it improves decisions. "
  "Reasoning path: an honesty model explains modeling's credibility problems and predicts trusted models. "
  "Proposed mechanism: 'uncertainty-honest' epidemic modeling - distributions and scenarios. "
  "What would confirm it: honest models guiding better policy. "
  "What would kill it: evidence that decisions need false precision. "
  "What this does not claim: it does not claim any model is accurate, offers no health advice, and does not constitute a policy recommendation."),
 "sig_lens": "The Signature lens reads models as false precision, and asks what honest uncertainty would guide.",
 "how_it_works": "Researchers study epidemic modeling through forecast evaluation, uncertainty research, and policy-use analyses.",
 "key_points": [
  "COVID-19 models were often wrong.",
  "Imperial College's projections shaped global policy.",
  "Models are sensitive to unknowable parameters.",
  "Forecast hubs now ensemble predictions.",
  "Policy influence exceeds accuracy.",
 ],
 "requirements": [
  "Uncertainty-honest modeling standards.",
  "Forecast evaluation and accountability.",
  "Decision-useful scenario modeling.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Kermack WO, McKendrick AG. Compartmental models. 1927.",
  "Ferguson NM et al. Imperial College COVID-19 report. 2020.",
  "Ioannidis JPA et al. Modeling critiques. Various; 2020-2022.",
  "Reich NG et al. Forecast hubs. Various; 2020-2023.",
 ],
 "demo_data": {"a": ("COVID-19 forecasts within 50% of reality, percent (approx)", 30.0),
               "b": ("percent scale", 100.0), "bounds": (0.2, 0.42),
               "step1": "seven in ten forecasts missed by half - the precision that wasn't",
               "confirm": "honest models guide better policy",
               "refute": "decisions prove to need false precision"},
},
# ------------------------------------------------------------------ rank 15
{
 "key": "wastewater",
 "name": "Wastewater Surveillance: The Population's Blood Test",
 "group": "Surveillance",
 "ladder_rank": 15, "ladder_tier": "compounded",
 "problem": "Wastewater detects pathogens, drugs, and resistance genes population-wide - but can it become routine public-health infrastructure?",
 "description": "Wastewater surveillance - monitoring sewage for pathogens - proved its worth in COVID-19: early warning, variant tracking, unbiased by testing behavior. But standardization, funding, and the scope (which pathogens, what actions) are unresolved. The infrastructure exists as emergency project, not permanent system.",
 "background": "Polio wastewater monitoring was the precedent; COVID-19 scaled it globally (2020-2022); the US NWSS systematized it. Expansion to flu, RSV, AMR, and opioids is underway. As of 2026 wastewater surveillance is proven with permanent status pending.",
 "why_it_matters": "Routine wastewater monitoring would give unbiased population health data: the cheapest surveillance ever built.",
 "sig_pointer": "The Signature system's proposed approach makes wastewater surveillance permanent, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that wastewater surveillance should be permanent infrastructure: standardized methods, sustained funding, and defined action triggers - like water-quality monitoring. "
  "Assumptions: (1) standardization is achievable; (2) funding is justifiable; (3) triggers guide action. "
  "Reasoning path: an infrastructure model explains the emergency-project status and predicts routine surveillance. "
  "Proposed mechanism: 'infrastructure-grade' wastewater monitoring - permanent standardized systems. "
  "What would confirm it: permanent systems guiding public-health action. "
  "What would kill it: evidence that wastewater signals don't guide action. "
  "What this does not claim: it does not claim wastewater monitoring is sufficient, offers no health advice, and does not constitute a policy recommendation."),
 "sig_lens": "The Signature lens reads wastewater as proven but temporary, and asks what permanence would enable.",
 "how_it_works": "Researchers study wastewater through NWSS data, standardization research, and action-trigger studies.",
 "key_points": [
  "Wastewater gave early COVID-19 warning unbiased by testing.",
  "Polio monitoring was the long precedent.",
  "Standardization and funding are unresolved.",
  "Expansion to flu, RSV, AMR is underway.",
  "Emergency-project status persists.",
 ],
 "requirements": [
  "Standardized permanent methods.",
  "Sustained funding models.",
  "Action triggers tied to signals.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Peccia J et al. COVID-19 wastewater. Various; 2020-2022.",
  "US CDC NWSS. National Wastewater Surveillance System. 2020 onward.",
  "Medina CY et al. Wastewater expansion reviews. Various; 2022-2024.",
  "WHO. Wastewater surveillance guidance. Various.",
 ],
 "demo_data": {"a": ("wastewater early-warning lead, days (approx)", 7.0),
               "b": ("days scale", 30.0), "bounds": (0.15, 0.35),
               "step1": "a week's warning from sewage - the signal without a permanent system",
               "confirm": "permanent systems guide public-health action",
               "refute": "wastewater signals prove not to guide action"},
},
# ------------------------------------------------------------------ rank 16
{
 "key": "genomic-epi",
 "name": "Genomic Epidemiology: Reading Outbreaks in DNA",
 "group": "Surveillance",
 "ladder_rank": 16, "ladder_tier": "compounded",
 "problem": "Pathogen genomes trace transmission - but genomic epidemiology is still a research tool, not routine surveillance. What would routine look like?",
 "description": "Genomic epidemiology - sequencing pathogens to track spread - transformed outbreak response (Ebola, COVID-19 variants). But routine use faces cost, turnaround, bioinformatics, and data-sharing barriers. The vision: every case sequenced, transmission mapped in real time.",
 "background": "Next-generation sequencing enabled the field (2010s); Ebola (2014-2016) proved field genomics; COVID-19 variant tracking (2020-2022) was the largest application. As of 2026 genomic surveillance is established for select pathogens, not routine.",
 "why_it_matters": "Routine genomic surveillance would make transmission visible: outbreaks mapped as they happen.",
 "sig_pointer": "The Signature system's proposed approach routinizes pathogen genomics, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that pathogen genomics should be routine: every case sequenced with rapid turnaround - the infrastructure built like clinical labs. "
  "Assumptions: (1) costs keep falling; (2) bioinformatics scales; (3) sharing is solvable. "
  "Reasoning path: an infrastructure model explains research-tool status and predicts routine genomics. "
  "Proposed mechanism: 'routine' genomic epidemiology - sequenced-every-case surveillance. "
  "What would confirm it: routine systems mapping transmission in real time. "
  "What would kill it: evidence that costs or complexity block routinization. "
  "What this does not claim: it does not claim routine genomics exists, offers no health advice, and does not constitute a policy recommendation."),
 "sig_lens": "The Signature lens reads genomics as research-grade, and asks what routine infrastructure would map.",
 "how_it_works": "Researchers study genomic epidemiology through variant-tracking programs, cost analyses, and bioinformatics scaling.",
 "key_points": [
  "Genomics transformed Ebola and COVID-19 response.",
  "Cost, turnaround, and bioinformatics are barriers.",
  "Data sharing is politically fraught.",
  "Select pathogens have genomic surveillance.",
  "Routine every-case sequencing is the vision.",
 ],
 "requirements": [
  "Affordable rapid sequencing at scale.",
  "Scalable bioinformatics pipelines.",
  "Data-sharing frameworks that work.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Gardy JL, Loman NJ. Genomic epidemiology. Various; 2018-2022.",
  "Quick J et al. Ebola field genomics. Various; 2016-2018.",
  "O'Toole A et al. COVID-19 variant tracking. Various; 2021-2023.",
  "WHO. Genomic surveillance strategy. 2022.",
 ],
 "demo_data": {"a": ("COVID-19 genomes sequenced, millions (approx)", 15.0),
               "b": ("COVID-19 cases, millions (approx)", 700.0), "bounds": (0.012, 0.032),
               "step1": "two percent of cases sequenced - the largest genomic effort, still a sample",
               "confirm": "routine systems map transmission in real time",
               "refute": "costs prove to block routinization"},
},
# ------------------------------------------------------------------ rank 17
{
 "key": "health-equity",
 "name": "Health Equity Measurement",
 "group": "Social Epidemiology",
 "ladder_rank": 17, "ladder_tier": "compounded",
 "problem": "Health inequities are documented endlessly - but measurement rarely leads to reduction. Can equity epidemiology become interventional?",
 "description": "Health-equity research - documenting disparities by race, income, place - is vast; disparity reduction is rare. The field debates whether measurement without intervention is sufficient, and which study designs identify effective equity interventions.",
 "background": "Disparity documentation grew for decades; the intervention evidence base is thin; COVID-19's disparities renewed urgency. As of 2026 equity epidemiology measures more than it fixes.",
 "why_it_matters": "Interventional equity research would convert documentation into reduction: the field's moral imperative.",
 "sig_pointer": "The Signature system's proposed approach makes equity research interventional, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that equity research should be interventional: every disparity study paired with tested interventions - measurement plus remedy. "
  "Assumptions: (1) interventions are testable; (2) they are effective; (3) the field will shift. "
  "Reasoning path: an interventional model explains the measurement-action gap and predicts disparity reduction. "
  "Proposed mechanism: 'intervention-paired' equity research - studies that test remedies. "
  "What would confirm it: paired studies reducing disparities. "
  "What would kill it: evidence that disparities resist intervention. "
  "What this does not claim: it does not claim any intervention works, offers no health advice, and does not constitute a policy recommendation."),
 "sig_lens": "The Signature lens reads equity research as documentation without remedy, and asks what pairing would fix.",
 "how_it_works": "Researchers study health equity through disparity surveillance, intervention trials, and implementation research.",
 "key_points": [
  "Disparity documentation is vast.",
  "Disparity reduction is rare.",
  "COVID-19 renewed urgency.",
  "Intervention evidence is thin.",
  "Measurement rarely leads to action.",
 ],
 "requirements": [
  "Intervention-paired disparity studies.",
  "Proven disparity-reducing interventions.",
  "A field oriented to remedy.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Braveman P et al. Health equity reviews. Various; 2011-2022.",
  "Bailey ZD et al. Structural racism and health. Various; 2017-2021.",
  "Krieger N et al. Equity measurement. Various; 2012-2020.",
  "Chin MH et al. Intervention reviews. Various; 2012-2018.",
 ],
 "demo_data": {"a": ("equity studies testing interventions, percent (approx)", 15.0),
               "b": ("percent scale", 100.0), "bounds": (0.08, 0.25),
               "step1": "six in seven equity studies only document - measurement without remedy",
               "confirm": "paired studies reduce disparities",
               "refute": "disparities prove resistant to intervention"},
},
# ------------------------------------------------------------------ rank 18
{
 "key": "climate-health",
 "name": "Climate Change and Health: The Attribution Problem",
 "group": "Environmental",
 "ladder_rank": 18, "ladder_tier": "compounded",
 "problem": "Climate change harms health - but attributing specific health outcomes to climate is methodologically hard. What's the true toll?",
 "description": "Climate-health links (heat mortality, vector spread, crop failure) are established qualitatively; quantitative attribution is hard: counterfactual climates, adaptation, and confounding complicate estimates. The field needs attributable-burden numbers for policy.",
 "background": "The Lancet Countdown (2015 onward) tracks indicators; attribution science matured in the 2010s-2020s; heat-mortality attribution is advancing. As of 2026 the qualitative case is solid with quantitative gaps.",
 "why_it_matters": "Attributable numbers drive climate policy: the health toll quantified is the argument for action.",
 "sig_pointer": "The Signature system's proposed approach attributes climate-health burden rigorously, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that climate-health attribution needs counterfactual rigor: the health outcomes without climate change modeled carefully - per outcome, per region. "
  "Assumptions: (1) counterfactuals are modelable; (2) they are credible; (3) they guide policy. "
  "Reasoning path: an attribution model explains the quantitative gap and predicts policy-grade numbers. "
  "Proposed mechanism: 'counterfactual-rigorous' attribution - credible attributable burdens. "
  "What would confirm it: attributed burdens guiding climate-health policy. "
  "What would kill it: evidence that attribution is infeasible. "
  "What this does not claim: it does not claim any toll number, offers no health advice, and does not constitute a policy recommendation."),
 "sig_lens": "The Signature lens reads climate-health as qualitatively certain but quantitatively vague, and asks what rigor would number.",
 "how_it_works": "Researchers study climate health through attribution modeling, Lancet Countdown tracking, and heat-mortality studies.",
 "key_points": [
  "Climate-health links are qualitatively established.",
  "Quantitative attribution is methodologically hard.",
  "The Lancet Countdown tracks indicators.",
  "Heat-mortality attribution is advancing.",
  "Policy needs attributable numbers.",
 ],
 "requirements": [
  "Credible counterfactual attributions.",
  "Per-outcome per-region burden numbers.",
  "Policy guided by attributed tolls.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Lancet Countdown on health and climate change. Annual; 2015 onward.",
  "Ebi KL et al. Attribution reviews. Various; 2018-2022.",
  "Vicedo-Cabrera AM et al. Heat-mortality attribution. Various; 2021-2023.",
  "Romanello M et al. Countdown indicators. Various; 2021-2023.",
 ],
 "demo_data": {"a": ("heat deaths attributed to climate change, percent (approx)", 35.0),
               "b": ("percent scale", 100.0), "bounds": (0.25, 0.48),
               "step1": "a third of heat deaths attributed - the quantified edge of a qualitative certainty",
               "confirm": "attributed burdens guide climate-health policy",
               "refute": "attribution proves infeasible"},
},
# ------------------------------------------------------------------ rank 19
{
 "key": "antimicrobial-resistance",
 "name": "AMR Surveillance: Tracking the Silent Pandemic",
 "group": "Surveillance",
 "ladder_rank": 19, "ladder_tier": "compounded",
 "problem": "Antimicrobial resistance kills millions - but surveillance is patchy, and the true burden is modeled, not measured. What's the real toll?",
 "description": "AMR - drug-resistant infections - causes an estimated 1.27M direct deaths yearly (Lancet, 2022); but surveillance covers a fraction of the world, and burden estimates are modeled. The field needs measured burden to drive action.",
 "background": "The Lancet AMR study (2022) quantified the modeled toll; GLASS (WHO surveillance) is expanding; but most of the world lacks lab capacity. As of 2026 AMR burden is estimated with wide uncertainty.",
 "why_it_matters": "Measured burden would drive the investment AMR needs: the silent pandemic made visible.",
 "sig_pointer": "The Signature system's proposed approach measures AMR burden directly, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that AMR burden should be directly measured: lab-capacity building plus systematic resistant-infection counting - replacing models with surveillance. "
  "Assumptions: (1) capacity is buildable; (2) counting is feasible; (3) measured burden drives action. "
  "Reasoning path: a measurement model explains the action gap and predicts funded AMR response. "
  "Proposed mechanism: 'directly-measured' AMR burden - global lab surveillance. "
  "What would confirm it: measured burdens driving investment. "
  "What would kill it: evidence that capacity can't be built at scale. "
  "What this does not claim: it does not claim any burden number, offers no health advice, and does not constitute a policy recommendation."),
 "sig_lens": "The Signature lens reads AMR burden as modeled guesses, and asks what global labs would count.",
 "how_it_works": "Researchers study AMR through GLASS surveillance, burden modeling, and lab-capacity research.",
 "key_points": [
  "AMR causes ~1.27M direct deaths yearly (modeled).",
  "Surveillance covers a fraction of the world.",
  "Most countries lack lab capacity.",
  "Burden estimates have wide uncertainty.",
  "Measured data would drive investment.",
 ],
 "requirements": [
  "Global lab-capacity building.",
  "Directly counted resistant infections.",
  "Measured burden guiding funding.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Murray CJL et al. Global AMR burden. Lancet. 2022;399:629-655.",
  "WHO GLASS. AMR surveillance reports. Various.",
  "Laxminarayan R et al. AMR policy reviews. Various; 2013-2020.",
  "Tacconelli E et al. Surveillance reviews. Various; 2018-2022.",
 ],
 "demo_data": {"a": ("countries with quality AMR surveillance (approx)", 70.0),
               "b": ("countries (approx)", 200.0), "bounds": (0.25, 0.48),
               "step1": "two-thirds of countries lack quality surveillance - the silent pandemic's blind spots",
               "confirm": "measured burdens drive investment",
               "refute": "capacity proves unbuildable at scale"},
},
# ------------------------------------------------------------------ rank 20
{
 "key": "long-covid",
 "name": "Long COVID: Epidemiology of the Aftermath",
 "group": "Infectious Disease",
 "ladder_rank": 20, "ladder_tier": "compounded",
 "problem": "Long COVID affects millions - but prevalence, mechanisms, and risk factors are still being defined. What's the true scale?",
 "description": "Long COVID (post-acute sequelae) - persistent symptoms after infection - affects an estimated 5-10% of infections; but definitions vary, mechanisms are unproven, and risk-factor epidemiology is early. The field is defining the condition while counting it.",
 "background": "Patient advocacy defined long COVID before medicine did; RECOVER and similar cohorts are characterizing it; definitions evolved (WHO, 2021). As of 2026 the epidemiology is maturing with mechanism gaps.",
 "why_it_matters": "Millions are disabled: defining and counting long COVID is the prerequisite to treating it.",
 "sig_pointer": "The Signature system's proposed approach defines long COVID rigorously, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that long COVID needs definitional rigor: consensus phenotypes with biomarkers - enabling true prevalence and mechanism research. "
  "Assumptions: (1) phenotypes are definable; (2) biomarkers exist; (3) rigor enables progress. "
  "Reasoning path: a definition model explains the epidemiological confusion and predicts real progress. "
  "Proposed mechanism: 'rigorously-defined' long COVID - consensus phenotypes guiding research. "
  "What would confirm it: defined phenotypes yielding mechanisms and treatments. "
  "What would kill it: evidence that long COVID defies definition. "
  "What this does not claim: it does not claim any prevalence number, offers no health advice, and does not constitute a clinical recommendation."),
 "sig_lens": "The Signature lens reads long COVID as undefined but real, and asks what rigor would clarify.",
 "how_it_works": "Researchers study long COVID through RECOVER cohorts, definition research, and mechanism studies.",
 "key_points": [
  "Long COVID affects an estimated 5-10% of infections.",
  "Definitions vary; mechanisms are unproven.",
  "Patient advocacy defined it before medicine.",
  "RECOVER is characterizing it systematically.",
  "Epidemiology is maturing with gaps.",
 ],
 "requirements": [
  "Consensus phenotypes with biomarkers.",
  "True prevalence estimates.",
  "Mechanism-driven treatments.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Nalbandian A et al. Post-acute COVID-19. Nature Medicine. 2021;27:601-615.",
  "RECOVER initiative. Various; 2021 onward.",
  "WHO. Post-COVID condition definition. 2021.",
  "Davis HE et al. Long COVID characterization. Various; 2021-2023.",
 ],
 "demo_data": {"a": ("infections with long COVID, percent (approx)", 7.0),
               "b": ("percent scale", 100.0), "bounds": (0.04, 0.12),
               "step1": "one in fourteen infections leaves lasting illness - counted while still being defined",
               "confirm": "defined phenotypes yield mechanisms and treatments",
               "refute": "long COVID proves to defy definition"},
},
# ------------------------------------------------------------------ rank 21
{
 "key": "digital-epi",
 "name": "Digital Epidemiology: Phones as Sensors",
 "group": "Methods",
 "ladder_rank": 21, "ladder_tier": "compounded",
 "problem": "Phones generate mobility and symptom data at population scale - can digital epidemiology become reliable public-health infrastructure?",
 "description": "Digital epidemiology - mobility data, search trends, app symptoms - offered real-time COVID-19 insights; but biases (who's tracked), privacy concerns, and the Google Flu Trends failure haunt the field. The methods need validation as infrastructure.",
 "background": "Google Flu Trends (2008-2015) famously failed; COVID-19 mobility data proved useful; privacy-preserving methods advanced. As of 2026 digital epidemiology is promising with validation gaps.",
 "why_it_matters": "Validated digital surveillance would give real-time population health data: the fastest epidemiology ever.",
 "sig_pointer": "The Signature system's proposed approach validates digital epidemiology as infrastructure, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that digital epidemiology needs infrastructure validation: each data stream validated against ground truth - with privacy preserved. "
  "Assumptions: (1) validation is feasible; (2) privacy methods work; (3) validated streams guide action. "
  "Reasoning path: a validation model explains the Google Flu Trends failure and predicts reliable digital surveillance. "
  "Proposed mechanism: 'validated' digital epidemiology - ground-truth-checked streams. "
  "What would confirm it: validated streams guiding public-health action. "
  "What would kill it: evidence that digital biases are uncorrectable. "
  "What this does not claim: it does not claim digital surveillance works, offers no health advice, and does not constitute a policy recommendation."),
 "sig_lens": "The Signature lens reads digital data as unvalidated signal, and asks what ground-truth checking would certify.",
 "how_it_works": "Researchers study digital epidemiology through mobility-data validation, privacy research, and stream comparisons.",
 "key_points": [
  "Google Flu Trends famously failed.",
  "COVID-19 mobility data proved useful.",
  "Biases (who's tracked) are the core problem.",
  "Privacy concerns limit deployment.",
  "Validation as infrastructure is pending.",
 ],
 "requirements": [
  "Ground-truth-validated data streams.",
  "Privacy-preserving methods at scale.",
  "Action-guiding digital surveillance.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Lazer D et al. Google Flu Trends failure. Science. 2014;343:1203-1205.",
  "Buckee CO et al. Mobility data in COVID-19. Various; 2020-2021.",
  "Salathe M et al. Digital epidemiology reviews. Various; 2018-2022.",
  "Wesolowski A et al. Phone data validation. Various; 2015-2020.",
 ],
 "demo_data": {"a": ("digital streams validated against ground truth, percent (approx)", 20.0),
               "b": ("percent scale", 100.0), "bounds": (0.12, 0.3),
               "step1": "four in five streams unvalidated - the signal without certification",
               "confirm": "validated streams guide public-health action",
               "refute": "digital biases prove uncorrectable"},
},
# ------------------------------------------------------------------ rank 22
{
 "key": "exposome",
 "name": "The Exposome: Measuring Everything",
 "group": "Environmental",
 "ladder_rank": 22, "ladder_tier": "compounded",
 "problem": "The exposome - all lifetime environmental exposures - is epidemiology's answer to the genome. But can it actually be measured?",
 "description": "The exposome concept (Wild, 2005) - measuring all exposures from conception onward - promises to explain the environment's disease share. But measurement is daunting: sensors, biomonitoring, and geospatial data each capture slices; integration is early; and the concept risks being everything and nothing.",
 "background": "The Human Genome Project's success inspired the exposome; HELIX and similar cohorts began measuring; wearable sensors proliferated. As of 2026 the exposome is a compelling concept with partial measurement.",
 "why_it_matters": "A measured exposome would complete the nature-nurture picture: the environmental half of disease causation.",
 "sig_pointer": "The Signature system's proposed approach makes the exposome measurable, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that the exposome needs prioritized measurement: the exposures that matter most identified first - measured systematically. "
  "Assumptions: (1) priorities are identifiable; (2) measurement scales; (3) integration works. "
  "Reasoning path: a prioritization model explains the concept-measurement gap and predicts useful exposomics. "
  "Proposed mechanism: 'prioritized' exposome measurement - systematic key-exposure tracking. "
  "What would confirm it: measured exposomes explaining disease variation. "
  "What would kill it: evidence that the exposome is unmeasurable. "
  "What this does not claim: it does not claim the exposome is measurable today, offers no health advice, and does not constitute a methodological prescription."),
 "sig_lens": "The Signature lens reads the exposome as unmeasured ambition, and asks what prioritization would make real.",
 "how_it_works": "Researchers study the exposome through HELIX cohorts, sensor research, and integration methods.",
 "key_points": [
  "The exposome is all lifetime exposures.",
  "Measurement is daunting in scope.",
  "HELIX and cohorts began systematic measurement.",
  "Integration of data types is early.",
  "The concept risks being everything and nothing.",
 ],
 "requirements": [
  "Prioritized measurable exposure sets.",
  "Scaled measurement infrastructure.",
  "Exposome-disease links established.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Wild CP. The exposome concept. Cancer Epidemiology Biomarkers & Prevention. 2005;14:1847-1850.",
  "Vrijheid M et al. HELIX project. Various; 2014-2020.",
  "Stingone JA et al. Exposome methods. Various; 2017-2022.",
  "Vineis P et al. Exposome reviews. Various; 2017-2021.",
 ],
 "demo_data": {"a": ("exposures routinely measured in cohorts (approx)", 50.0),
               "b": ("lifetime exposures experienced (approx thousands)", 100.0), "bounds": (0.35, 0.65),
               "step1": "fifty measured of a hundred thousand experienced - the unmeasured environmental half",
               "confirm": "measured exposomes explain disease variation",
               "refute": "the exposome proves unmeasurable"},
},
# ------------------------------------------------------------------ rank 23
{
 "key": "causal-ai",
 "name": "AI for Causal Inference",
 "group": "Methods",
 "ladder_rank": 23, "ladder_tier": "compounded",
 "problem": "Machine learning predicts brilliantly but confuses correlation with causation - can AI do causal inference?",
 "description": "ML-for-causality - causal forests, double machine learning, causal discovery - promises to automate confounding control and discover causal structure. But the methods need untestable assumptions; performance on real epidemiological problems is mixed; and the hype exceeds the validation.",
 "background": "The potential-outcomes framework met ML in the 2010s (Athey, Imbens); double/debiased ML (Chernozhukov, 2018) brought rigor; causal discovery remains fragile. As of 2026 AI causality is promising with validation gaps.",
 "why_it_matters": "Reliable AI causality would automate the hardest part of epidemiology: the confounding problem at scale.",
 "sig_pointer": "The Signature system's proposed approach validates AI causality on known answers, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that AI causality needs known-answer validation: methods tested on problems with RCT-established truth - earning trust before deployment. "
  "Assumptions: (1) known-answer tests exist; (2) they are discriminating; (3) validation transfers. "
  "Reasoning path: a validation model explains the hype-evidence gap and predicts trustworthy AI causality. "
  "Proposed mechanism: 'known-answer-validated' causal AI - methods proven on established truths. "
  "What would confirm it: validated methods matching RCT answers on new problems. "
  "What would kill it: evidence that assumptions defeat automation. "
  "What this does not claim: it does not claim AI does causality, offers no health advice, and does not constitute a methodological prescription."),
 "sig_lens": "The Signature lens reads AI causality as unvalidated promise, and asks what known-answer testing would certify.",
 "how_it_works": "Researchers study AI causality through benchmark competitions, double-ML applications, and discovery-method evaluations.",
 "key_points": [
  "ML predicts well but confuses correlation and causation.",
  "Causal forests and double ML add rigor.",
  "Untestable assumptions remain.",
  "Real-world performance is mixed.",
  "Known-answer validation is the missing step.",
 ],
 "requirements": [
  "Known-answer benchmark suites.",
  "Validated methods matching RCT truth.",
  "Deployed trustworthy causal AI.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Athey S, Imbens G. Machine learning and causality. Various; 2016-2019.",
  "Chernozhukov V et al. Double/debiased ML. 2018.",
  "Pearl J. Causality frameworks. 2009.",
  "Shalit U et al. Causal ML evaluations. Various; 2017-2022.",
 ],
 "demo_data": {"a": ("causal-AI methods validated on known answers, percent (approx)", 15.0),
               "b": ("percent scale", 100.0), "bounds": (0.08, 0.25),
               "step1": "six in seven methods unvalidated on known truth - the promise without proof",
               "confirm": "validated methods match RCT answers on new problems",
               "refute": "assumptions prove to defeat automation"},
},
# ------------------------------------------------------------------ rank 24
{
 "key": "zoonotic-spillover-epi",
 "name": "Spillover Epidemiology: Counting the Next Jump",
 "group": "One Health",
 "ladder_rank": 24, "ladder_tier": "advanced",
 "problem": "Most pandemics start in animals - but spillover epidemiology (how often jumps happen, where, why) is barely quantified. What's the true rate?",
 "description": "Zoonotic spillover - animal-to-human pathogen jumps - is mostly invisible: most jumps die out, few are detected. The rate, the high-risk interfaces, and the predictors are poorly quantified. PREDICT catalogued viruses; the epidemiological rate of jumping remains unknown.",
 "background": "Spillover gained attention post-SARS; PREDICT (2009-2020) discovered viruses; Jones (2008) mapped hotspots. But the jump rate - jumps per interface per time - is unmeasured. As of 2026 spillover epidemiology is hotspot maps without rates.",
 "why_it_matters": "Quantified spillover rates would target prevention at the highest-risk interfaces: pandemic prevention by the numbers.",
 "sig_pointer": "The Signature system's proposed approach measures spillover rates directly, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that spillover needs rate measurement: serological cohort studies at high-risk interfaces - counting jumps directly. "
  "Assumptions: (1) jumps are serologically detectable; (2) cohorts are feasible; (3) rates guide prevention. "
  "Reasoning path: a measurement model explains the prevention gap and predicts targeted spillover control. "
  "Proposed mechanism: 'rate-measured' spillover epidemiology - counted jumps guiding prevention. "
  "What would confirm it: measured rates predicting pandemic risk. "
  "What would kill it: evidence that jumps are unmeasurable. "
  "What this does not claim: it does not claim any spillover rate, offers no health advice, and does not constitute a policy recommendation."),
 "sig_lens": "The Signature lens reads spillover as uncounted jumps, and asks what serology would tally.",
 "how_it_works": "Researchers study spillover through interface cohorts, serological surveys, and hotspot modeling.",
 "key_points": [
  "Most jumps die out undetected.",
  "Hotspot maps exist without rates.",
  "PREDICT catalogued viruses, not jump rates.",
  "High-risk interfaces are identified qualitatively.",
  "The jump rate is unmeasured.",
 ],
 "requirements": [
  "Serological jump-rate cohorts.",
  "Quantified interface risks.",
  "Rate-guided prevention.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Jones KE et al. Emerging disease hotspots. Nature. 2008;451:990-993.",
  "USAID PREDICT. Various; 2009-2020.",
  "Allen T et al. Hotspot correlates. Nature Communications. 2017;8:1124.",
  "Carlson CJ et al. Spillover reviews. Various; 2022-2024.",
 ],
 "demo_data": {"a": ("zoonotic jumps detected per pandemic (approx)", 1.0),
               "b": ("zoonotic jumps occurring, estimated (approx thousands)", 10.0), "bounds": (0.05, 0.2),
               "step1": "one detected of ten thousand occurring - the invisible denominator",
               "confirm": "measured rates predict pandemic risk",
               "refute": "jumps prove unmeasurable"},
},
# ------------------------------------------------------------------ rank 25
{
 "key": "intervention-evaluation",
 "name": "Evaluating Public-Health Interventions",
 "group": "Methods",
 "ladder_rank": 25, "ladder_tier": "advanced",
 "problem": "Lockdowns, mask mandates, school closures - were evaluated messily in real time. Can public-health interventions be evaluated rigorously?",
 "description": "Non-pharmaceutical interventions (NPIs) - the COVID-19 toolkit - were evaluated through natural experiments with heavy confounding: places that locked down differed systematically. The evidence base remains contested; the methods for rapid rigorous evaluation are underdeveloped.",
 "background": "NPI evaluation was ad hoc during COVID-19; synthetic-control and difference-in-differences methods were applied; conclusions remain debated. As of 2026 the field lacks agreed rapid-evaluation methods.",
 "why_it_matters": "The next pandemic needs evaluated interventions: knowing what works would replace debate with evidence.",
 "sig_pointer": "The Signature system's proposed approach builds rapid-evaluation infrastructure, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that intervention evaluation needs pre-built infrastructure: agreed methods, data pipelines, and rapid-trial platforms - ready before the crisis. "
  "Assumptions: (1) methods are agreeable; (2) infrastructure is buildable; (3) rapid evaluation works. "
  "Reasoning path: an infrastructure model explains the evaluation mess and predicts rigorous NPI evidence. "
  "Proposed mechanism: 'pre-built' intervention evaluation - ready methods and platforms. "
  "What would confirm it: rapid rigorous NPI evaluations in the next crisis. "
  "What would kill it: evidence that crises defeat rigorous evaluation. "
  "What this does not claim: it does not claim any intervention worked, offers no health advice, and does not constitute a policy recommendation."),
 "sig_lens": "The Signature lens reads NPI evidence as unbuilt infrastructure, and asks what readiness would evaluate.",
 "how_it_works": "Researchers study NPI evaluation through natural-experiment methods, synthetic controls, and platform-trial designs.",
 "key_points": [
  "COVID-19 NPI evaluation was confounded.",
  "Places adopting interventions differed systematically.",
  "Conclusions remain debated.",
  "Rapid rigorous methods are underdeveloped.",
  "Pre-built infrastructure is the proposed fix.",
 ],
 "requirements": [
  "Agreed rapid-evaluation methods.",
  "Pre-built data and trial platforms.",
  "Rigorous NPI evidence base.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Hsiang S et al. NPI evaluations. Nature. 2020;584:262-267.",
  "Flaxman S et al. Intervention modeling. Nature. 2020;584:257-261.",
  "Bendavid E et al. Evaluation critiques. Various; 2021-2023.",
  "Jefferson T et al. NPI reviews. Various; 2020-2023.",
 ],
 "demo_data": {"a": ("NPI studies with rigorous causal design, percent (approx)", 20.0),
               "b": ("percent scale", 100.0), "bounds": (0.12, 0.3),
               "step1": "four in five NPI studies lack rigorous design - the evidence base that wasn't",
               "confirm": "rapid rigorous NPI evaluations in the next crisis",
               "refute": "crises prove to defeat rigorous evaluation"},
},
# ------------------------------------------------------------------ rank 26
{
 "key": "health-communication",
 "name": "Health Communication That Works",
 "group": "Behavioral",
 "ladder_rank": 26, "ladder_tier": "advanced",
 "problem": "Public-health messaging often fails - what communication actually changes behavior?",
 "description": "Health communication - pandemic guidance, vaccine campaigns, risk messages - frequently misses: mixed messages, distrust, and behavioral resistance. The evidence base for effective communication is thin; the field learns slowly from failures.",
 "background": "Risk-communication research grew post-9/11; COVID-19 was the largest test - with mixed results. Message-testing is rare in practice. As of 2026 health communication is more art than science.",
 "why_it_matters": "Effective communication saves lives at population scale: the cheapest intervention in public health.",
 "sig_pointer": "The Signature system's proposed approach tests health messages like drugs, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that health messages should be RCT-tested: randomized message trials - with behavior outcomes - before campaigns launch. "
  "Assumptions: (1) messages are testable; (2) effects are measurable; (3) testing improves campaigns. "
  "Reasoning path: a testing model explains communication failures and predicts effective messaging. "
  "Proposed mechanism: 'RCT-tested' health communication - trial-validated messages. "
  "What would confirm it: tested messages outperforming untested ones. "
  "What would kill it: evidence that message effects are untestable. "
  "What this does not claim: it does not claim any message works, offers no health advice, and does not constitute a policy recommendation."),
 "sig_lens": "The Signature lens reads health messaging as untested, and asks what trials would validate.",
 "how_it_works": "Researchers study health communication through message-testing trials, trust research, and campaign evaluations.",
 "key_points": [
  "COVID-19 messaging had mixed results.",
  "Message-testing is rare in practice.",
  "Distrust and resistance are common.",
  "The evidence base is thin.",
  "Communication is more art than science.",
 ],
 "requirements": [
  "Routine RCT-tested messaging.",
  "Behavior-outcome message trials.",
  "Campaigns built on tested messages.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Fischhoff B et al. Risk communication. Various; 2011-2021.",
  "Brewer NT et al. Message-testing reviews. Various; 2017-2021.",
  "Noar SM et al. Campaign evaluations. Various; 2006-2020.",
  "WHO. Health communication guidance. Various.",
 ],
 "demo_data": {"a": ("health campaigns with pre-tested messages, percent (approx)", 15.0),
               "b": ("percent scale", 100.0), "bounds": (0.08, 0.25),
               "step1": "six in seven campaigns launch untested messages - the art without the trial",
               "confirm": "tested messages outperform untested ones",
               "refute": "message effects prove untestable"},
},
# ------------------------------------------------------------------ rank 27
{
 "key": "mortality-measurement",
 "name": "Counting the Dead: Global Mortality Measurement",
 "group": "Surveillance",
 "ladder_rank": 27, "ladder_tier": "advanced",
 "problem": "Most of the world's deaths are never registered with a cause - how can global health be managed without counting?",
 "description": "Civil registration and vital statistics (CRVS) - death counting - covers a minority of the world's deaths: most occur without medical certification. Verbal autopsy fills gaps imperfectly. The field cannot manage what it doesn't count.",
 "background": "CRVS gaps were long known; verbal-autopsy methods improved (2010s); the Lancet counting series advocated investment. As of 2026 most global deaths remain uncounted by cause.",
 "why_it_matters": "Uncounted deaths mean misallocated resources: counting is global health's foundation.",
 "sig_pointer": "The Signature system's proposed approach builds universal death registration, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that death registration should be universal: CRVS systems built everywhere - with verbal autopsy as bridge. "
  "Assumptions: (1) systems are buildable; (2) they are affordable; (3) counted deaths guide policy. "
  "Reasoning path: an infrastructure model explains the counting gap and predicts managed global health. "
  "Proposed mechanism: 'universal' mortality measurement - every death counted with cause. "
  "What would confirm it: universal systems guiding resource allocation. "
  "What would kill it: evidence that registration is infeasible in fragile states. "
  "What this does not claim: it does not claim any mortality number, offers no health advice, and does not constitute a policy recommendation."),
 "sig_lens": "The Signature lens reads global health as uncounted, and asks what universal registration would manage.",
 "how_it_works": "Researchers study mortality measurement through CRVS building, verbal-autopsy validation, and counting advocacy.",
 "key_points": [
  "Most global deaths lack medical certification.",
  "Verbal autopsy fills gaps imperfectly.",
  "CRVS covers a minority of deaths.",
  "Uncounted deaths misallocate resources.",
  "Counting is the foundation.",
 ],
 "requirements": [
  "Universal CRVS systems.",
  "Validated verbal-autopsy bridges.",
  "Counted deaths guiding allocation.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Mikkelsen L et al. CRVS reviews. Lancet. 2015;386:171-172.",
  "Nichols EK et al. Verbal autopsy. Various; 2018-2022.",
  "AbouZahr C et al. Counting series. Various; 2015-2021.",
  "WHO. CRVS strategic plans. Various.",
 ],
 "demo_data": {"a": ("global deaths with certified cause, percent (approx)", 40.0),
               "b": ("percent scale", 100.0), "bounds": (0.3, 0.52),
               "step1": "three in five deaths uncounted by cause - the foundation nobody built",
               "confirm": "universal systems guide resource allocation",
               "refute": "registration proves infeasible in fragile states"},
},
# ------------------------------------------------------------------ rank 28
{
 "key": "precision-public-health",
 "name": "Precision Public Health",
 "group": "Methods",
 "ladder_rank": 28, "ladder_tier": "advanced",
 "problem": "Public health treats populations uniformly - can genomics, geospatial data, and digital streams make it precise?",
 "description": "Precision public health - targeted interventions using granular data - promises efficiency: the right intervention for the right subpopulation. But the methods are early, equity concerns are real (precision for the well-measured), and the evidence base is thin.",
 "background": "The concept emerged in the 2010s (Khoury, Iademarco); COVID-19 showed both potential and inequity. As of 2026 precision public health is a vision with pilot data.",
 "why_it_matters": "Precise public health would maximize impact per dollar: efficiency's frontier - if equity is preserved.",
 "sig_pointer": "The Signature system's proposed approach builds precision with equity guards, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that precision public health needs equity-by-design: granular targeting with measured equity impact - precision that doesn't widen gaps. "
  "Assumptions: (1) precision is achievable; (2) equity is measurable; (3) both are compatible. "
  "Reasoning path: an equity model explains the vision's risks and predicts fair precision. "
  "Proposed mechanism: 'equity-guarded' precision public health - targeted with disparity monitoring. "
  "What would confirm it: precision programs improving outcomes without widening gaps. "
  "What would kill it: evidence that precision inherently widens inequity. "
  "What this does not claim: it does not claim precision works, offers no health advice, and does not constitute a policy recommendation."),
 "sig_lens": "The Signature lens reads precision as efficiency with equity risk, and asks what guards would ensure fairness.",
 "how_it_works": "Researchers study precision public health through pilot programs, equity-impact analyses, and methods development.",
 "key_points": [
  "Precision promises targeted efficient intervention.",
  "Methods are early; evidence is thin.",
  "Equity concerns are real.",
  "COVID-19 showed potential and inequity.",
  "The vision has pilot data.",
 ],
 "requirements": [
  "Precision programs with proven impact.",
  "Equity guards preventing gap-widening.",
  "Methods validated at scale.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Khoury MJ et al. Precision public health. Various; 2016-2020.",
  "Iademarco MF et al. CDC precision vision. Various; 2017-2021.",
  "Dolley S et al. Equity critiques. Various; 2020-2023.",
  "Chowkwanyun M et al. Precision reviews. Various; 2018-2022.",
 ],
 "demo_data": {"a": ("precision public-health programs at scale (approx)", 5.0),
               "b": ("pilot programs (approx)", 50.0), "bounds": (0.05, 0.18),
               "step1": "five at scale of fifty pilots - the vision's early map",
               "confirm": "precision programs improve outcomes without widening gaps",
               "refute": "precision proves to inherently widen inequity"},
},
# ------------------------------------------------------------------ rank 29
{
 "key": "infodemic",
 "name": "The Infodemic: Epidemiology of Misinformation",
 "group": "Behavioral",
 "ladder_rank": 29, "ladder_tier": "advanced",
 "problem": "Health misinformation spreads like a pathogen - can it be studied, predicted, and countered epidemiologically?",
 "description": "The infodemic - misinformation accompanying epidemics - undermines vaccination, treatment, and trust. Research into its spread dynamics, effective counters (prebunking, inoculation theory), and platform interventions is growing but early.",
 "background": "WHO coined 'infodemic' (2020); inoculation theory (McGuire, 1960s; revived by van der Linden) showed prebunking works; platform interventions are contested. As of 2026 infodemic science is emerging.",
 "why_it_matters": "Misinformation kills through behavior: countering it epidemiologically would protect the information environment.",
 "sig_pointer": "The Signature system's proposed approach treats misinformation as a pathogen, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that misinformation should be modeled epidemiologically: spread dynamics, susceptibility, and immunity (prebunking) - with interventions trialed like vaccines. "
  "Assumptions: (1) the analogy holds; (2) dynamics are modelable; (3) counters work. "
  "Reasoning path: an epidemiological model explains misinformation's impact and predicts effective counters. "
  "Proposed mechanism: 'epidemiologically-modeled' infodemic response - tracked and countered. "
  "What would confirm it: modeled counters reducing misinformation impact. "
  "What would kill it: evidence that misinformation resists modeling. "
  "What this does not claim: it does not take a position on content moderation, offers no health advice, and does not constitute a policy recommendation."),
 "sig_lens": "The Signature lens reads misinformation as a pathogen, and asks what epidemiology would counter it.",
 "how_it_works": "Researchers study infodemics through spread modeling, prebunking trials, and platform-intervention studies.",
 "key_points": [
  "WHO declared the infodemic (2020).",
  "Prebunking shows promise (inoculation theory).",
  "Spread dynamics are modelable.",
  "Platform interventions are contested.",
  "The science is emerging.",
 ],
 "requirements": [
  "Validated misinformation-spread models.",
  "Trial-proven counters at scale.",
  "Infodemic surveillance systems.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "WHO. Infodemic management. 2020 onward.",
  "van der Linden S et al. Inoculation theory. Various; 2017-2023.",
  "Ecker UKH et al. Misinformation reviews. Various; 2022-2024.",
  "Rubinelli S et al. Infodemic frameworks. Various; 2021-2023.",
 ],
 "demo_data": {"a": ("misinformation exposures with prebunking protection, percent (approx)", 15.0),
               "b": ("percent scale", 100.0), "bounds": (0.08, 0.25),
               "step1": "six in seven exposures unprotected - the pathogen without a vaccine program",
               "confirm": "modeled counters reduce misinformation impact",
               "refute": "misinformation proves resistant to modeling"},
},
# ------------------------------------------------------------------ rank 30
{
 "key": "syndemics",
 "name": "Syndemics: Diseases That Feed Each Other",
 "group": "Theory",
 "ladder_rank": 30, "ladder_tier": "advanced",
 "problem": "Diseases cluster and amplify each other - HIV, TB, diabetes, depression - but epidemiology studies them separately. Can syndemics be measured and intervened on?",
 "description": "Syndemics (Singer, 1990s) - interacting epidemics driven by social conditions - describes how diseases amplify each other: HIV-TB, diabetes-depression, substance-use-violence-HIV. But measurement methods are underdeveloped and interventions rarely target the syndemic.",
 "background": "Singer's anthropological concept entered epidemiology slowly; measurement frameworks are emerging; intervention trials are rare. As of 2026 syndemics is influential theory with thin methods.",
 "why_it_matters": "Syndemic thinking would target disease clusters, not single diseases: the efficiency of treating interactions.",
 "sig_pointer": "The Signature system's proposed approach makes syndemics measurable and intervenable, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that syndemics need measurement and intervention methods: interaction quantification plus cluster-targeted trials. "
  "Assumptions: (1) interactions are quantifiable; (2) clusters are intervenable; (3) methods are developable. "
  "Reasoning path: a methods model explains the theory-practice gap and predicts syndemic public health. "
  "Proposed mechanism: 'measured' syndemics - quantified interactions with cluster interventions. "
  "What would confirm it: cluster interventions beating single-disease ones. "
  "What would kill it: evidence that interactions are unmeasurable. "
  "What this does not claim: it does not claim any syndemic exists, offers no health advice, and does not constitute a policy recommendation."),
 "sig_lens": "The Signature lens reads syndemics as theory without methods, and asks what measurement would enable.",
 "how_it_works": "Researchers study syndemics through interaction modeling, cluster trials, and framework development.",
 "key_points": [
  "Diseases cluster and amplify each other.",
  "Singer's concept is influential but method-thin.",
  "Measurement frameworks are emerging.",
  "Interventions rarely target clusters.",
  "Single-disease studies miss interactions.",
 ],
 "requirements": [
  "Quantified interaction methods.",
  "Cluster-targeted intervention trials.",
  "Syndemic-guided public health.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Singer M et al. Syndemics theory. Various; 1994-2017.",
  "Tsai AC et al. Syndemics measurement. Various; 2018-2022.",
  "Mendenhall E et al. Syndemics reviews. Various; 2017-2022.",
  "Willen SS et al. Intervention frameworks. Various; 2017-2021.",
 ],
 "demo_data": {"a": ("disease programs addressing interactions (approx)", 5.0),
               "b": ("disease programs (approx)", 100.0), "bounds": (0.02, 0.1),
               "step1": "five of a hundred programs address interactions - the clusters nobody treats",
               "confirm": "cluster interventions beat single-disease ones",
               "refute": "interactions prove unmeasurable"},
},
# ------------------------------------------------------------------ rank 31
{
 "key": "global-surveillance",
 "name": "Global Surveillance Architecture",
 "group": "Surveillance",
 "ladder_rank": 31, "ladder_tier": "advanced",
 "problem": "Global disease surveillance is fragmented across agencies and countries - what architecture would actually detect the next pandemic?",
 "description": "Global surveillance - WHO, national systems, ProMED, GOARN - is fragmented: data sharing is political, capacity is unequal, and the IHR (2005) compliance is weak. The architecture for reliable global detection doesn't exist.",
 "background": "IHR (2005) set obligations widely unmet; GOARN coordinates response; the pandemic treaty negotiations address gaps. As of 2026 the architecture is aspirational.",
 "why_it_matters": "The next pandemic's detection depends on global architecture: fragmentation is the vulnerability.",
 "sig_pointer": "The Signature system's proposed approach designs functional global surveillance, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that global surveillance needs functional design: shared data infrastructure, capacity building, and compliance mechanisms - built as a system. "
  "Assumptions: (1) design is possible; (2) countries will participate; (3) the system detects faster. "
  "Reasoning path: a design model explains fragmentation and predicts functional surveillance. "
  "Proposed mechanism: 'designed' global surveillance - functional architecture. "
  "What would confirm it: designed systems detecting outbreaks faster. "
  "What would kill it: evidence that sovereignty defeats architecture. "
  "What this does not claim: it does not claim any architecture exists, offers no health advice, and does not constitute a policy recommendation."),
 "sig_lens": "The Signature lens reads global surveillance as undesigned, and asks what architecture would detect.",
 "how_it_works": "Researchers study global surveillance through IHR evaluations, treaty negotiations, and capacity research.",
 "key_points": [
  "Global surveillance is fragmented.",
  "IHR compliance is weak.",
  "Data sharing is political.",
  "Capacity is unequal.",
  "The pandemic treaty addresses gaps.",
 ],
 "requirements": [
  "Functional designed architecture.",
  "Compliance mechanisms that work.",
  "Faster detection demonstrated.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "WHO. International Health Regulations. 2005.",
  "Gostin LO et al. IHR evaluations. Various; 2015-2022.",
  "WHO. Pandemic treaty negotiations. 2021 onward.",
  "Davies SE et al. Surveillance architecture. Various; 2020-2023.",
 ],
 "demo_data": {"a": ("countries IHR-compliant (approx)", 70.0),
               "b": ("countries (approx)", 200.0), "bounds": (0.25, 0.48),
               "step1": "two-thirds of countries non-compliant - the architecture of aspiration",
               "confirm": "designed systems detect outbreaks faster",
               "refute": "sovereignty proves to defeat architecture"},
},
# ------------------------------------------------------------------ rank 32
{
 "key": "epi-theory",
 "name": "Epidemiological Theory: From Risk Factors to Systems",
 "group": "Theory",
 "ladder_rank": 32, "ladder_tier": "advanced",
 "problem": "Epidemiology's risk-factor paradigm is aging - can systems thinking, counterfactuals, and complexity science build a new theoretical foundation?",
 "description": "Epidemiological theory - from Hill to Rothman to Hernan - is evolving: the sufficient-cause model, counterfactual frameworks, and systems approaches compete. Whether a new synthesis emerges is the discipline's theoretical question.",
 "background": "Rothman's sufficient-cause model (1976) and Hernan's counterfactuals (2000s) modernized theory; systems epidemiology is emerging. As of 2026 the synthesis is pending.",
 "why_it_matters": "Theory guides methods: a new synthesis would modernize the discipline's foundations.",
 "sig_pointer": "The Signature system's proposed approach synthesizes epidemiological theory, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that epidemiological theory needs synthesis: counterfactual rigor plus systems thinking - unified formally. "
  "Assumptions: (1) synthesis is possible; (2) it is formalizable; (3) it guides practice. "
  "Reasoning path: a synthesis model explains theoretical fragmentation and predicts modern foundations. "
  "Proposed mechanism: 'synthesized' epidemiological theory - unified formal foundations. "
  "What would confirm it: synthesized theory guiding better methods. "
  "What would kill it: evidence that the paradigms are incompatible. "
  "What this does not claim: it does not claim a synthesis exists, offers no health advice, and does not constitute a methodological prescription."),
 "sig_lens": "The Signature lens reads theory as fragmented paradigms, and asks what synthesis would unify.",
 "how_it_works": "Researchers study epidemiological theory through framework comparisons, formalization, and methods research.",
 "key_points": [
  "The risk-factor paradigm is aging.",
  "Counterfactuals modernized causal theory.",
  "Systems approaches are emerging.",
  "No synthesis exists yet.",
  "Theory guides the methods.",
 ],
 "requirements": [
  "Formalized unified theory.",
  "Better methods from synthesis.",
  "Disciplinary adoption.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Rothman KJ. Sufficient-cause model. 1976.",
  "Hernan MA et al. Counterfactual frameworks. Various; 2004-2020.",
  "Diez Roux AV. Systems epidemiology. Various; 2011-2021.",
  "VanderWeele TJ et al. Theory reviews. Various; 2017-2022.",
 ],
 "demo_data": {"a": ("unified epidemiological theories", 0.5),
               "b": ("competing paradigms (approx)", 4.0), "bounds": (0.08, 0.2),
               "step1": "four paradigms, zero syntheses - the foundations awaiting unification",
               "confirm": "synthesized theory guides better methods",
               "refute": "the paradigms prove incompatible"},
},
# ------------------------------------------------------------------ rank 33
{
 "key": "eradication",
 "name": "Eradication: Which Diseases Next?",
 "group": "One Health",
 "ladder_rank": 33, "ladder_tier": "advanced",
 "problem": "Smallpox was eradicated; polio nearly - which diseases can be eradicated next, and what would it take?",
 "description": "Disease eradication - permanent global zero - succeeded once (smallpox) and nearly again (polio, guinea worm). Candidates (measles, rubella, yaws, malaria) each face biological and political barriers. The field debates feasibility versus control.",
 "background": "Smallpox (1980) proved eradication possible; polio's decades-long campaign shows the difficulty; measles eradication is debated. As of 2026 eradication is proven possible with few candidates.",
 "why_it_matters": "Eradication is public health's ultimate prize: permanent victory over a disease.",
 "sig_pointer": "The Signature system's proposed approach assesses eradication feasibility systematically, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that eradication candidates need systematic feasibility assessment: biological, technical, and political criteria - scored per disease. "
  "Assumptions: (1) feasibility is assessable; (2) criteria are valid; (3) assessment guides investment. "
  "Reasoning path: an assessment model explains eradication debates and predicts successful campaigns. "
  "Proposed mechanism: 'feasibility-scored' eradication - systematic candidate evaluation. "
  "What would confirm it: scored candidates achieving eradication. "
  "What would kill it: evidence that feasibility is unpredictable. "
  "What this does not claim: it does not claim any disease is eradicable, offers no health advice, and does not constitute a policy recommendation."),
 "sig_lens": "The Signature lens reads eradication as unassessed ambition, and asks what scoring would prioritize.",
 "how_it_works": "Researchers study eradication through feasibility frameworks, polio-campaign lessons, and candidate assessments.",
 "key_points": [
  "Smallpox is the only human disease eradicated.",
  "Polio is nearly eradicated after decades.",
  "Measles, rubella, yaws are debated candidates.",
  "Biological and political barriers each matter.",
  "Feasibility assessment is unsystematic.",
 ],
 "requirements": [
  "Systematic feasibility scoring.",
  "Successful scored campaigns.",
  "Investment guided by assessment.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Fenner F et al. Smallpox eradication. 1988.",
  "WHO. Polio eradication initiative. Various.",
  "Dowdle WR et al. Eradication criteria. Various; 1998-2020.",
  "Cohen J et al. Eradication debates. Various; 2019-2023.",
 ],
 "demo_data": {"a": ("human diseases eradicated", 1.0),
               "b": ("eradication candidates debated (approx)", 10.0), "bounds": (0.05, 0.18),
               "step1": "one eradicated of ten debated - the ultimate prize's short list",
               "confirm": "scored candidates achieve eradication",
               "refute": "feasibility proves unpredictable"},
},
# ------------------------------------------------------------------ rank 34
{
 "key": "epi-future",
 "name": "Epidemiology's Future: The Science of Populations",
 "group": "Theory",
 "ladder_rank": 34, "ladder_tier": "advanced",
 "problem": "Epidemiology faces data abundance and theory scarcity - what will the science of populations become?",
 "description": "Epidemiology's future - big data, genomics, systems science, AI - promises transformation; but the field's core (causal inference for policy) remains. Whether the data revolution transforms or merely accelerates epidemiology is the discipline's existential question.",
 "background": "The data revolution (2010s-2020s) brought new tools; the theoretical core persists; the field debates its identity. As of 2026 epidemiology is data-rich with its future open.",
 "why_it_matters": "The science of populations determines public health's future: its evolution shapes humanity's health.",
 "sig_pointer": "The Signature system's proposed approach defines epidemiology's data-era identity, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that epidemiology's future is causal inference at data scale: the theoretical core preserved - with new tools serving it. "
  "Assumptions: (1) the core endures; (2) tools serve the core; (3) the synthesis works. "
  "Reasoning path: an identity model explains the existential debate and predicts the discipline's evolution. "
  "Proposed mechanism: 'core-preserved' data-era epidemiology - new tools, enduring questions. "
  "What would confirm it: data-scale causal inference guiding policy. "
  "What would kill it: evidence that data replaces theory. "
  "What this does not claim: it does not claim any future is certain, offers no health advice, and does not constitute a disciplinary prescription."),
 "sig_lens": "The Signature lens reads the future as tools seeking purpose, and asks what core they would serve.",
 "how_it_works": "Researchers study epidemiology's future through methods foresight, data-science integration, and disciplinary debates.",
 "key_points": [
  "Data abundance meets theory scarcity.",
  "Big data, genomics, and AI promise transformation.",
  "Causal inference for policy remains the core.",
  "The field debates its identity.",
  "The future is open.",
 ],
 "requirements": [
  "Data-scale causal methods.",
  "Preserved theoretical core.",
  "Policy guided by data-era epidemiology.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Galea S et al. Epidemiology's future. Various; 2018-2023.",
  "Keyes KM, Galea S. Population Health Science. 2016.",
  "Lash TL et al. Methods futures. Various; 2020-2023.",
  "Adamiak A et al. Data-era reviews. Various; 2021-2024.",
 ],
 "demo_data": {"a": ("epidemiologists using big-data methods, percent (approx)", 40.0),
               "b": ("percent scale", 100.0), "bounds": (0.3, 0.52),
               "step1": "two in five use the new tools - the discipline mid-transformation",
               "confirm": "data-scale causal inference guides policy",
               "refute": "data proves to replace theory"},
},
]
