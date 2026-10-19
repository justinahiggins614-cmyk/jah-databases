#!/usr/bin/env python3
"""Entries for The Unsolved Data Science Database (unsolved-data-science) and
its Signature half (unsolved-data-science-signature).

34 famous unsolved problems in data science, ladder-ordered by accessibility
(rank 1 = most approachable, rank 34 = most complex/compounded).
Public half: real, fact-checked problems. Signature half: the same 34 problems
through the Signature lens, with Signature-generated proposed solutions that
are ALWAYS labeled as proposals, never established science.

ID prefixes JAH-USDS- / JAH-USDSS- verified free: zero hits in manifest
id_prefix values (exact + substring, both directions, all manifest prefixes).

Honesty rule: every sig_solution opens with the exact label
"Signature-generated proposed solution \u2014 not established science.";
never claims proof, never implies peer acceptance, never presents speculation
as settled.
"""

LABEL = "Signature-generated proposed solution \u2014 not established science."

FIELD = {
 "tag": "data-science",
 "disp": "data science",
 "name": "The Unsolved Data Science Database",
 "sig_name": "The Unsolved Data Science Signature Database",
 "prefix": "JAH-USDS-",
 "sig_prefix": "JAH-USDSS-",
 "ai": "JAH Unsolved Data Science Archivist",
 "tagline": ("Thirty-four famous open problems in data science, from reproducibility and causation "
             "to scaling laws and a unified theory: real, fact-checked, each with its full story and "
             "a clearly labeled Signature proposed solution."),
 "sig_tagline": ("His original Signature solution method applied to all 34 great open problems of data "
                 "science: Signature-generated proposed solutions with assumptions declared, confirm and "
                 "refute conditions stated, and limits honestly marked. Clearly labeled Signature-made, "
                 "never established science."),
 "pub_line": ("Public records - 34 famous open problems in data science, real and fact-checked: the "
              "reproducibility crisis, causation from observation, missing data, the curse of "
              "dimensionality, overfitting, class imbalance, data leakage, label noise, concept drift, "
              "interpretability, and the fairness impossibility - every record carrying the problem "
              "statement, background, why it matters, key points, requirements, standards, citations, "
              "and a working solution-explorer demonstration, organized in the Signature system."),
 "sig_line": ("Signature originals - his original Signature solution method: the same 34 famous unsolved "
              "data science problems approached as a covenant between the known and the unknown, each "
              "carrying the full Signature-generated proposed solution with its assumptions declared, "
              "its confirm and refute conditions stated, and its limits honestly marked. Clearly labeled "
              "Signature-made, never presented as established science or authentic public record."),
 "ladder_text": (" Records are ordered by the teaching ladder: Foundations (reproducibility, causation, "
                 "missing data, dimensionality, overfitting, imbalance, leakage, label noise, drift, "
                 "interpretability, fairness) -> Compounded (privacy against utility, out-of-distribution "
                 "generalization, adversarial robustness, calibration, feature engineering, small data, "
                 "time series causality, recommender loops, graph expressivity, synthetic data, federated "
                 "non-IID data, benchmark saturation) -> Advanced (overparameterized generalization, "
                 "scaling laws, compute-versus-statistics tradeoffs, optimal transport, the manifold "
                 "hypothesis, meta-learning theory, streaming bounds, anomaly guarantees, data valuation, "
                 "metric geometry, the unified theory)."),
 "search_ph": ("Search reproducibility, causation, fairness, privacy, adversarial examples, scaling laws, "
               "double descent, federated learning, interpretability, concept drift..."),
 "chat_ph": "Ask about the great open problems of data science...",
 "greet_pub": ("I am the JAH Unsolved Data Science Archivist. Ask me about the great open problems of data "
               "science - from reproducibility, causation, and fairness through privacy, robustness, and "
               "federated learning, to scaling laws, double descent, and the dream of a unified theory."),
 "greet_sig": ("I am the JAH Unsolved Data Science Archivist (Signature). Ask me about the Signature "
               "proposed solutions to the great open problems of data science - every approach labeled as "
               "a proposal, never established science."),
 "role_pub": ("unsolved data science archivist - the great open problems of data science, from the "
              "reproducibility crisis, causation, and fairness through privacy, robustness, and federated "
              "learning, to scaling laws, double descent, and the unified theory; teaches progressively "
              "along the ladder from foundations through compounded to advanced; answers from many angles "
              "- definition, example, analogy, application, history, math - using only archive data from "
              "this system"),
 "role_sig": ("unsolved data science archivist - Signature editions: his original Signature solution "
              "method applied to the 34 great open problems of data science, each carrying the full "
              "Signature-generated proposed solution, clearly labeled Signature-made and never presented "
              "as established science; teaches progressively along the ladder from foundations through "
              "compounded to advanced; answers from many angles - definition, example, analogy, "
              "application, history, math - using only archive data from this system"),
 "gen_desc": "Generate clearly-labeled unsolved data science studies. Seeded archive records are the authoritative entries.",
 "standards": [
  "Problem statements verified against the published literature; open status confirmed as of 2026.",
  "Quantitative claims cross-checked against standard references (James et al., An Introduction to Statistical Learning; Goodfellow, Bengio and Courville, Deep Learning, MIT Press 2016).",
  "Signature solution sections are labeled proposals: they state assumptions, a reasoning path, a proposed mechanism, what would confirm or kill them, and what they do not claim.",
 ],
 "sig_tail": ("Signature editions carry the Signature system's proposed solution approaches to famous "
              "unsolved problems. Every solution is labeled a Signature-generated proposal, never "
              "established science, never peer-accepted, never proof."),
}

ENTRIES = [
# ------------------------------------------------------------------ rank 1
{
 "key": "ds-reproducibility",
 "name": "The Reproducibility Problem in Data Science",
 "group": "Machine Learning",
 "ladder_rank": 1, "ladder_tier": "foundations",
 "problem": "Why do so many published data science findings fail to reproduce, and how can an analysis be designed so its conclusions survive independent re-execution on new data?",
 "background": "John Ioannidis argued in 2005 that most published research findings are false, and large replication efforts since have confirmed the worry: the Open Science Collaboration (2015) reproduced only about 36 percent of 100 psychology studies, and similar shortfalls appear across the empirical sciences. In data science the failure modes have names: p-hacking, the garden of forking paths (Gelman and Loken, 2013), researcher degrees of freedom, and silent multiple testing across model variants. A pipeline that tries hundreds of feature sets and reports the best is performing an uncorrected search, and its reported accuracy is an optimistic fiction. Preregistration, held-out test sets, and registered reports help, but most industrial modeling has no preregistration at all, and leakage between train and test remains endemic.",
 "why_it_matters": "Every decision built on a non-reproducible model is built on sand: medical triage tools, hiring screens, credit models, and scientific claims all inherit the fragility. Until reproducibility is engineered into the workflow rather than hoped for after it, the field cannot tell which of its victories are real.",
 "sig_lens": "The Signature lens reads reproducibility as a ledger problem: every fork in the analysis path is a debit against the claim, and the books must balance before the result ships.",
 "sig_solution": LABEL + " Assumptions: (1) every analytic choice (imputation, feature, split, metric) is a degree of freedom that must be logged; (2) the reported performance is a random variable over the choice path, not a point. Reasoning path: attach a tamper-evident ledger to the pipeline that records each fork, then report the full distribution of outcomes across the fork tree instead of the best leaf. Proposed mechanism: a fork-ledger protocol where the final claim carries its fork count, the variance across forks, and a preregistered primary path; claims whose fork-variance exceeds a declared bound are automatically downgraded to exploratory. Confirm: ledger-audited pipelines show smaller train-to-deployment gaps than unaudited ones. Kill: analysts game the ledger by hiding forks off-book. Does NOT claim: an end to false findings - it prices the forking, it does not forbid it.",
 "pointer": "The Signature system's proposed approach treats every analytic fork as a ledger debit and reports the distribution across the fork tree; the companion Signature Edition record lays out the fork-ledger protocol in full.",
 "key_points": [
  "Replication efforts routinely reproduce far fewer than half of published empirical findings.",
  "Unreported multiple testing across model variants silently inflates reported accuracy.",
  "Preregistration and held-out evaluation help but are rare in industrial practice.",
  "The garden of forking paths means even honest analysts overfit by choosing among analyses.",
 ],
 "requirements": [
  "A logged record of analytic choices from raw data to reported metric.",
  "A held-out evaluation set never used for any selection decision.",
  "Reporting of the full outcome distribution, not the best observed run.",
 ],
 "citations": [
  "Ioannidis JPA (2005) Why most published research findings are false. PLoS Medicine 2(8): e124.",
  "Gelman A, Loken E (2013) The garden of forking paths. Unpublished manuscript, Columbia University.",
 ],
 "demo": {"probs": [0.5, 0.25, 0.125, 0.125], "qpert": [0.4, 0.3, 0.2, 0.1]},
},
# ------------------------------------------------------------------ rank 2
{
 "key": "ds-causation",
 "name": "Causation Against Correlation in Observational Data",
 "group": "Statistics",
 "ladder_rank": 2, "ladder_tier": "foundations",
 "problem": "Given only observational data, when can a data scientist legitimately claim that changing X will change Y, rather than merely that X and Y move together?",
 "background": "Correlation is cheap and causation is expensive: this asymmetry has organized statistics for a century. The Neyman-Rubin potential-outcomes framework (Rubin, 1974) and Pearl causal graphs with do-calculus (Pearl, 2000) give formal languages for the question, but both demand assumptions - unconfoundedness, ignorability, correct graph structure - that observational data alone cannot verify. Randomized trials remain the gold standard, yet most data science runs on logs, not experiments: click streams, medical records, economic panels. Methods like propensity scores, instrumental variables, and difference-in-differences each buy causal conclusions at the price of an untestable assumption, and practitioners routinely forget the price was paid.",
 "why_it_matters": "Policy, medicine, and product decisions need causal answers: will this treatment help, will this price change revenue, will this intervention reduce harm. A correlational model confidently recommending the wrong lever is worse than no model at all, because it wears the authority of data.",
 "sig_lens": "The Signature lens reads causation as a licensing problem: every causal claim ships with an explicit license listing the assumptions that authorize it, and the license is part of the deliverable.",
 "sig_solution": LABEL + " Assumptions: (1) no observational method yields assumption-free causal claims; (2) decision-makers misread unlicensed causal language as licensed. Reasoning path: require every causal statement to carry a machine-readable assumption license (identification strategy, sensitivity bounds, falsification tests attempted), and grade the license, not just the estimate. Proposed mechanism: an assumption-ledger pipeline that computes how badly each assumption must fail to overturn the conclusion (Rosenbaum-style sensitivity bounds as standard output) and refuses to print causal verbs when the bounds are wide. Confirm: licensed causal reports lead to fewer reversed decisions than unlicensed ones. Kill: users ignore the license and read the headline anyway. Does NOT claim: a way to get causation without assumptions - the license prices the assumptions, it does not remove them.",
 "pointer": "The Signature system's proposed approach licenses every causal claim with its assumption list and sensitivity bounds; the companion Signature Edition record specifies the assumption-ledger protocol.",
 "key_points": [
  "Potential-outcomes and causal-graph frameworks formalize the question but need untestable assumptions.",
  "Randomized trials are the gold standard; most data science runs on observational logs.",
  "Propensity scores, instruments, and diff-in-diff each purchase causality with one key assumption.",
  "Sensitivity analysis can bound how wrong the assumptions must be to overturn a result.",
 ],
 "requirements": [
  "An explicit identification strategy stated before estimation.",
  "Sensitivity bounds showing how fragile the conclusion is to assumption failure.",
  "Falsification tests (placebos, negative controls) reported alongside the estimate.",
 ],
 "citations": [
  "Pearl J (2000) Causality: Models, Reasoning, and Inference. Cambridge University Press.",
  "Rubin DB (1974) Estimating causal effects of treatments in randomized and nonrandomized studies. Journal of Educational Psychology 66(5): 688-701.",
 ],
 "demo": {"probs": [0.6, 0.2, 0.1, 0.1], "qpert": [0.5, 0.25, 0.15, 0.1]},
},
# ------------------------------------------------------------------ rank 3
{
 "key": "ds-missing-data",
 "name": "The Missing Data Mechanism Problem",
 "group": "Statistics",
 "ladder_rank": 3, "ladder_tier": "foundations",
 "problem": "When values are missing from a dataset, under what conditions can analysis proceed as if the missingness does not matter, and what must be done when it does matter?",
 "background": "Donald Rubin classified missingness in 1976 into MCAR (missing completely at random), MAR (missing at random, explainable by observed variables), and MNAR (missing not at random, depending on the missing values themselves). Standard tools - multiple imputation (Rubin, 1987), EM, inverse-probability weighting - are valid under MAR but can be badly biased under MNAR, and the data cannot tell you which regime you are in: the distinction is about the unobserved. Survey nonresponse, sensor dropout, and churned users are routinely MNAR - the people who leave are different in ways the remaining data cannot show. Sensitivity analysis for MNAR exists but is rarely run, so most pipelines silently assume MAR and hope.",
 "why_it_matters": "Missingness is not a cleaning step; it is a modeling decision that can reverse conclusions. Medical registries, economic surveys, and user analytics all lose the very cases that would change the answer, and assuming the loss is random manufactures false confidence.",
 "sig_lens": "The Signature lens reads missing data as an absence with a shape: the pattern of what is missing is itself data, and the analysis must model the hole, not just fill it.",
 "sig_solution": LABEL + " Assumptions: (1) the missingness mechanism is never verifiable from the observed data; (2) analysts default to MAR by convenience, not evidence. Reasoning path: make the missingness pattern a first-class modeled object - estimate the response model alongside the outcome model, and report conclusions as a function over plausible MNAR departures. Proposed mechanism: a missingness-shape audit that fits the response model, stress-tests conclusions across a declared family of MNAR departures, and prints the tipping point where the conclusion flips. Confirm: audits catch sign-flipping MNAR sensitivity in real datasets where MAR analysis looked safe. Kill: the declared MNAR family misses the true mechanism and the tipping point misleads. Does NOT claim: identification of the true mechanism - it maps the fragility, it does not resolve it.",
 "pointer": "The Signature system's proposed approach models the missingness pattern itself and reports conclusions with their MNAR tipping points; the companion Signature Edition record details the missingness-shape audit.",
 "key_points": [
  "Rubin taxonomy (MCAR, MAR, MNAR) governs which methods are valid; the data cannot identify the regime.",
  "Multiple imputation and weighting are valid under MAR, biased under MNAR.",
  "Nonresponse and dropout are routinely MNAR in practice.",
  "MNAR sensitivity analysis exists but is seldom performed.",
 ],
 "requirements": [
  "A stated missingness assumption with justification, not a default.",
  "Diagnostics of the missingness pattern before any imputation.",
  "Sensitivity analysis across plausible MNAR departures for key conclusions.",
 ],
 "citations": [
  "Rubin DB (1976) Inference and missing data. Biometrika 63(3): 581-592.",
  "Little RJ, Rubin DB (2019) Statistical Analysis with Missing Data, 3rd ed. Wiley.",
 ],
 "demo": {"probs": [0.7, 0.15, 0.1, 0.05], "qpert": [0.6, 0.2, 0.12, 0.08]},
},
# ------------------------------------------------------------------ rank 4
{
 "key": "ds-curse-dimensionality",
 "name": "The Curse of Dimensionality in Practice",
 "group": "Machine Learning",
 "ladder_rank": 4, "ladder_tier": "foundations",
 "problem": "Why do learning methods that work beautifully in low dimensions collapse as the number of features grows, and what principled escapes exist?",
 "background": "Richard Bellman named the curse in 1957: in high dimensions, volume concentrates in shells, distances lose contrast, and data becomes exponentially sparse - covering a unit cube in 10 dimensions at the density of 100 points per dimension-side needs 10^20 points. Nearest neighbors stop meaning anything because all pairwise distances converge; grid-based methods die outright. The practical escapes are all bets on structure: sparsity (L1 methods, Tibshirani 1996), low-dimensional manifolds, smoothness, or learned representations. Deep learning's success is arguably one giant bet that real data lives near low-dimensional manifolds - a bet that works remarkably often and is still unproven in general.",
 "why_it_matters": "Genomics, text, images, and sensor fusion all live in thousands of dimensions. Every practitioner either beats the curse with a structural assumption or is beaten by it silently, with models that fit training data and know nothing.",
 "sig_lens": "The Signature lens reads dimensionality as a budget: each dimension spends sample, and the ledger must show what structural assumption repays the spend.",
 "sig_solution": LABEL + " Assumptions: (1) no method beats the curse without a structural bet; (2) the bet is usually implicit and unpriced. Reasoning path: force the structural assumption into the open as a declared, testable claim (intrinsic dimension estimate, sparsity level, smoothness class), then monitor whether incoming data keeps paying for it. Proposed mechanism: a dimension-budget ledger that estimates intrinsic dimension (e.g., nearest-neighbor scaling), declares the assumption funding the model, and raises an alarm when new data violates it. Confirm: ledger-monitored models degrade gracefully with warnings instead of silently. Kill: intrinsic-dimension estimates are too noisy to be actionable. Does NOT claim: a universal cure for high dimensions - it prices the bet, it does not remove the risk.",
 "pointer": "The Signature system's proposed approach keeps a dimension-budget ledger that declares and monitors the structural bet funding the model; the companion Signature Edition record specifies the ledger protocol.",
 "key_points": [
  "Volume concentrates and distances lose contrast as dimensions grow; data becomes exponentially sparse.",
  "Nearest-neighbor and grid methods degrade first and hardest.",
  "All escapes (sparsity, manifolds, smoothness) are bets on hidden structure.",
  "Deep learning is one large, largely successful, still-unproven manifold bet.",
 ],
 "requirements": [
  "An estimate of intrinsic dimension before choosing the method.",
  "A declared structural assumption (sparsity, manifold, smoothness).",
  "Monitoring that incoming data continues to satisfy the assumption.",
 ],
 "citations": [
  "Bellman RE (1957) Dynamic Programming. Princeton University Press.",
  "Tibshirani R (1996) Regression shrinkage and selection via the lasso. JRSS-B 58(1): 267-288.",
 ],
 "demo": {"probs": [0.4, 0.3, 0.2, 0.1], "qpert": [0.35, 0.3, 0.2, 0.15]},
},
# ------------------------------------------------------------------ rank 5
{
 "key": "ds-overfitting",
 "name": "Overfitting Against Generalization",
 "group": "Machine Learning",
 "ladder_rank": 5, "ladder_tier": "foundations",
 "problem": "How can a practitioner know, before deployment, whether a model has learned the signal or merely memorized the noise in its training data?",
 "background": "The bias-variance tradeoff (Geman, Bienenstock and Doursat, 1992) frames the classic answer: complex models fit training data tightly but vary wildly across samples. Cross-validation, regularization, and held-out testing are the standard defenses, yet each has holes - cross-validation can leak through preprocessing, regularization strength is itself tuned on data, and held-out sets get reused until they are effectively training data. The modern shock is that massively overparameterized networks generalize anyway (Zhang et al., 2017, showed they can memorize random labels yet still generalize on real ones), which broke the classical story without replacing it. Practitioners are left with rituals that mostly work and a theory that no longer explains why.",
 "why_it_matters": "A memorized model is a confident liar: perfect on the data it saw, arbitrary on the data it will meet. Hiring, lending, and diagnostic models that overfit do not just fail - they fail with high reported accuracy right up until deployment.",
 "sig_lens": "The Signature lens reads overfitting as unpriced flexibility: every parameter is a loan against future data, and the ledger must show the collateral.",
 "sig_solution": LABEL + " Assumptions: (1) classical capacity measures no longer predict deep-network generalization; (2) what matters is the effective flexibility actually used, not the parameter count. Reasoning path: measure used flexibility directly (sensitivity of predictions to training perturbations, sharpness of minima) and report a generalization margin alongside accuracy. Proposed mechanism: a flexibility ledger that computes perturbation-sensitivity scores on the trained model and refuses to certify deployment when the margin is thin, regardless of test accuracy. Confirm: ledger-flagged models fail deployment more often than ledger-cleared ones. Kill: sensitivity scores prove as gameable as accuracy. Does NOT claim: a new generalization theory - it measures the risk, it does not explain it.",
 "pointer": "The Signature system's proposed approach ledgers the flexibility a model actually used and certifies deployment on the margin, not the accuracy; the companion Signature Edition record details the flexibility ledger.",
 "key_points": [
  "Classical bias-variance theory no longer predicts deep-network behavior.",
  "Networks can memorize random labels yet generalize on structured data.",
  "Cross-validation and regularization help but are themselves tunable and leakable.",
  "Held-out sets degrade into training data through repeated reuse.",
 ],
 "requirements": [
  "A truly held-out evaluation set, used once, for the final verdict.",
  "Regularization and selection decisions logged, not silently tuned.",
  "A measured generalization margin, not just a point accuracy.",
 ],
 "citations": [
  "Geman S, Bienenstock E, Doursat R (1992) Neural networks and the bias/variance dilemma. Neural Computation 4(1): 1-58.",
  "Zhang C et al. (2017) Understanding deep learning requires rethinking generalization. ICLR.",
 ],
 "demo": {"probs": [0.55, 0.2, 0.15, 0.1], "qpert": [0.45, 0.25, 0.18, 0.12]},
},
# ------------------------------------------------------------------ rank 6
{
 "key": "ds-class-imbalance",
 "name": "The Class Imbalance Problem",
 "group": "Machine Learning",
 "ladder_rank": 6, "ladder_tier": "foundations",
 "problem": "How should a classifier be trained and evaluated when the event of interest - fraud, disease, failure - is thousands of times rarer than the background?",
 "background": "Accuracy is a lie under imbalance: a fraud detector that always says legitimate scores 99.9 percent on a 0.1 percent fraud rate while catching nothing. The field answers with resampling (SMOTE, Chawla et al., 2002), cost-sensitive learning, threshold tuning, and better metrics (precision-recall curves, PR-AUC), but each fix has a failure mode - SMOTE synthesizes noise, cost matrices are guesses, and threshold choice smuggles the business decision into the modeling step. Worse, the rare class is often the one with the least reliable labels and the most distribution shift, so the hardest cases get the weakest data. Evaluation remains genuinely unsolved: with 50 positives, confidence intervals on recall are wide enough to hide total failure.",
 "why_it_matters": "The rare events are the important ones: fraud, cancer, network intrusion, equipment failure. A model optimized for the majority class is optimized to ignore exactly what it was built to catch.",
 "sig_lens": "The Signature lens reads imbalance as a majority tax: the majority class taxes every decision, and the ledger must show the tax rate explicitly.",
 "sig_solution": LABEL + " Assumptions: (1) the business cost matrix is the real objective and is usually unstated; (2) with few positives, uncertainty dominates any point metric. Reasoning path: force the cost matrix into the open before training, optimize expected cost directly, and report full uncertainty bands on minority-class metrics. Proposed mechanism: a cost-ledger protocol where stakeholders sign the cost matrix first, the model optimizes it, and every reported recall comes with an exact binomial confidence band - deployment requires the lower band, not the point estimate, to clear the bar. Confirm: cost-ledgered models meet their business targets more often. Kill: stakeholders cannot or will not state costs honestly. Does NOT claim: a fix for having too few positives - it prices the uncertainty, it does not create data.",
 "pointer": "The Signature system's proposed approach signs the cost matrix first and deploys on the lower confidence band; the companion Signature Edition record specifies the cost-ledger protocol.",
 "key_points": [
  "Accuracy is meaningless under severe imbalance; precision-recall metrics are the honest currency.",
  "Resampling and cost weighting help but inject their own artifacts and guesses.",
  "The rare class usually has the noisiest labels and the most shift.",
  "With dozens of positives, recall estimates carry enormous uncertainty.",
 ],
 "requirements": [
  "A stakeholder-signed cost matrix before any modeling.",
  "Precision-recall evaluation with exact confidence bands on minority metrics.",
  "Deployment gated on the lower confidence band, not the point estimate.",
 ],
 "citations": [
  "Chawla NV et al. (2002) SMOTE: synthetic minority over-sampling technique. JAIR 16: 321-357.",
  "He H, Garcia EA (2009) Learning from imbalanced data. IEEE TKDE 21(9): 1263-1284.",
 ],
 "demo": {"probs": [0.9, 0.06, 0.03, 0.01], "qpert": [0.85, 0.08, 0.05, 0.02]},
},
# ------------------------------------------------------------------ rank 7
{
 "key": "ds-data-leakage",
 "name": "The Data Leakage Problem",
 "group": "Data Engineering",
 "ladder_rank": 7, "ladder_tier": "foundations",
 "problem": "How can a modeling pipeline guarantee that information from the future - or from the test set - never contaminates training, when leakage hides in preprocessing, joins, and time?",
 "background": "Leakage is the silent killer of honest evaluation: a feature computed with knowledge of the target, a train-test split that ignores time, an imputation fit on the full dataset, a patient appearing in both train and test. Kaufman et al. (2012) surveyed leakage as a central failure mode, and practitioners keep rediscovering it - most famously when models that looked brilliant in development collapse on deployment because a timestamp or an ID carried the answer. Temporal leakage is the hardest: any split that lets the model train on Tuesday to predict Monday is fiction. Detection is genuinely hard because leakage often lives in pipeline code, not in the model, and the inflated metrics look like success.",
 "why_it_matters": "Leakage does not degrade a model gracefully - it manufactures a fantasy of performance that evaporates on contact with reality. Every leaked pipeline ships false confidence to decision-makers.",
 "sig_lens": "The Signature lens reads leakage as time travel: any information crossing from the future side of a boundary to the past side is contraband, and the pipeline needs customs.",
 "sig_solution": LABEL + " Assumptions: (1) leakage hides in pipeline code, not model code; (2) inflated metrics are indistinguishable from genuine success without provenance. Reasoning path: make every data artifact carry a time-and-source passport, and enforce boundary customs that block any feature whose provenance postdates the prediction point. Proposed mechanism: a provenance-passport system where each column records its earliest legitimate availability time, plus an automated customs check that fails the build if any training feature postdates the label time. Confirm: passported pipelines show smaller development-to-deployment gaps. Kill: provenance metadata is wrong or incomplete and customs waves contraband through. Does NOT claim: detection of all leakage - it catches provenance violations, not subtle semantic leaks.",
 "pointer": "The Signature system's proposed approach passports every feature with its availability time and enforces boundary customs; the companion Signature Edition record specifies the passport protocol.",
 "key_points": [
  "Leakage hides in preprocessing, joins, IDs, and timestamps - rarely in the model itself.",
  "Temporal leakage (training on the future) is the most common and most damaging form.",
  "Leaked metrics look like success, so the failure is discovered at deployment.",
  "Group and time-aware splitting is necessary but not sufficient.",
 ],
 "requirements": [
  "Time-and-source provenance on every feature used in training.",
  "Splits that respect time and entity grouping, verified not assumed.",
  "An automated customs check blocking features that postdate the prediction point.",
 ],
 "citations": [
  "Kaufman S et al. (2012) Leakage in data mining: formulation, detection, and avoidance. ACM TKDD 6(4).",
 ],
 "demo": {"probs": [0.65, 0.2, 0.1, 0.05], "qpert": [0.55, 0.25, 0.12, 0.08]},
},
# ------------------------------------------------------------------ rank 8
{
 "key": "ds-label-noise",
 "name": "The Label Noise Problem",
 "group": "Machine Learning",
 "ladder_rank": 8, "ladder_tier": "foundations",
 "problem": "When training labels come from crowds, heuristics, or tired experts, how can a model learn the truth when a substantial fraction of its supervision is wrong?",
 "background": "Real labels are noisy: crowd workers disagree, weak-supervision heuristics misfire, experts err under load. Frenay and Verleysen (2014) surveyed the damage - noise rates of 10 to 40 percent are common in practice, and deep networks memorize noise as readily as signal. The field has countermeasures: noise-robust losses, sample reweighting, confident learning (Northcutt et al., 2021) to prune mislabeled points, and noise-rate estimation. But the core difficulty is identifiability: without clean anchor data, systematic label bias (one class mislabeled more than another) is indistinguishable from a true pattern, and no clever loss can recover what the supervision never contained.",
 "why_it_matters": "Supervision is the fuel of machine learning, and contaminated fuel poisons everything downstream. Medical, legal, and safety models trained on noisy labels inherit the noise as confident error.",
 "sig_lens": "The Signature lens reads labels as testimony: every label is a witness statement with a credibility score, and the court must weigh witnesses, not just count them.",
 "sig_solution": LABEL + " Assumptions: (1) label noise is structured, not uniform - some sources err systematically; (2) a small clean anchor set is worth more than a large noisy one. Reasoning path: score every label source for credibility on anchor data, then train with credibility-weighted supervision and report the effective clean-sample size. Proposed mechanism: a witness-credibility ledger that estimates per-source noise matrices on anchors, reweights training accordingly, and prints the credibility-adjusted sample size alongside accuracy - deployment requires the adjusted size, not the raw count, to be adequate. Confirm: credibility-weighted models beat unweighted ones on clean held-out tests. Kill: no anchor data exists and the credibility scores are circular. Does NOT claim: recovery of truth from pure noise - it weighs testimony, it does not manufacture witnesses.",
 "pointer": "The Signature system's proposed approach scores every label source like a witness and trains on credibility-weighted supervision; the companion Signature Edition record specifies the witness-credibility ledger.",
 "key_points": [
  "Real-world label noise of 10 to 40 percent is common; networks memorize it.",
  "Noise-robust losses and confident learning help with random noise.",
  "Systematic (class-dependent) label bias is unidentifiable without clean anchors.",
  "A small clean anchor set outweighs a large noisy one.",
 ],
 "requirements": [
  "A clean anchor set for calibrating label-source credibility.",
  "Per-source noise estimates, not a single global noise rate.",
  "Reporting of the credibility-adjusted effective sample size.",
 ],
 "citations": [
  "Frenay B, Verleysen M (2014) Classification in the presence of label noise: a survey. IEEE TNNLS 25(5).",
  "Northcutt CG et al. (2021) Confident learning. JAIR 70: 1373-1411.",
 ],
 "demo": {"probs": [0.5, 0.3, 0.12, 0.08], "qpert": [0.42, 0.3, 0.16, 0.12]},
},
# ------------------------------------------------------------------ rank 9
{
 "key": "ds-concept-drift",
 "name": "The Concept Drift Problem",
 "group": "Machine Learning",
 "ladder_rank": 9, "ladder_tier": "foundations",
 "problem": "When the world changes under a deployed model - new fraud tactics, shifting language, evolving disease - how can the system detect the drift and adapt before the damage compounds?",
 "background": "Stationarity is the founding fiction of most modeling: the future will resemble the past. Reality drifts - suddenly (a pandemic rewrites demand), gradually (language evolves), or recurrently (seasonality). Gama et al. (2014) surveyed drift detection: statistical monitors (DDM, ADWIN), distribution tests, and performance trackers. But detection is only half the problem; adaptation is the hard half. Retraining on recent data chases noise, forgetting old regimes destroys hard-won knowledge (catastrophic forgetting), and ground-truth labels for the new regime arrive late or never. Most deployed models have no drift monitor at all - they fail silently until a human notices the business metric moved.",
 "why_it_matters": "A model is a snapshot of a world that no longer exists the moment it deploys. Without drift handling, every production model has an unmarked expiration date, and the failures arrive as surprises.",
 "sig_lens": "The Signature lens reads drift as weather: the model needs a barometer, not just a thermometer - a standing instrument that watches the sky, not the wreckage.",
 "sig_solution": LABEL + " Assumptions: (1) drift is inevitable and mostly unlabeled at onset; (2) retraining blindly on recent data amplifies noise. Reasoning path: run a standing drift barometer (feature-distribution monitors plus a small labeled probe set) and adapt by regime - blend, don't replace. Proposed mechanism: a barometer protocol with three adaptation gears (recalibrate thresholds, reweight recent data, full retrain) selected by drift type and magnitude, with rollback to the previous regime model when the new regime proves transient. Confirm: barometer-equipped deployments recover faster from real drift events. Kill: drift arrives faster than the probe labels, and the barometer lags reality. Does NOT claim: prediction of unprecedented regime breaks - it shortens the reaction time, it does not see the future.",
 "pointer": "The Signature system's proposed approach runs a standing drift barometer with geared adaptation and rollback; the companion Signature Edition record specifies the barometer protocol.",
 "key_points": [
  "Stationarity fails in production: fraud, language, and demand all drift.",
  "Drift detectors exist (ADWIN, DDM) but adaptation, not detection, is the hard half.",
  "Blind retraining chases noise; full retraining forgets old regimes.",
  "Most deployed models have no drift monitor and fail silently.",
 ],
 "requirements": [
  "A standing drift monitor on features and (probed) labels, not just business metrics.",
  "Geared adaptation: recalibrate, reweight, or retrain based on drift type.",
  "Rollback capability when a new regime proves transient.",
 ],
 "citations": [
  "Gama J et al. (2014) A survey on concept drift adaptation. ACM Computing Surveys 46(4).",
 ],
 "demo": {"probs": [0.45, 0.25, 0.2, 0.1], "qpert": [0.38, 0.27, 0.2, 0.15]},
},
# ----------------------------------------------------------------- rank 10
{
 "key": "ds-interpretability",
 "name": "The Interpretability Gap in Machine Learning",
 "group": "Machine Learning",
 "ladder_rank": 10, "ladder_tier": "foundations",
 "problem": "When a model denies a loan, flags a tumor, or recommends a sentence, what counts as an adequate explanation - and can current explanation methods actually provide it?",
 "background": "High-stakes decisions demand explanations, but the explanation toolkit is shaky. Post-hoc methods (LIME, SHAP, saliency maps) approximate black boxes locally, yet Adebayo et al. (2018) showed saliency maps can be insensitive to both model and data - pretty pictures with no fidelity guarantee. Cynthia Rudin (2019) argued the field should stop explaining black boxes and build interpretable models instead, at least where stakes are high. The deeper problem is philosophical: there is no agreed definition of what an explanation is - a causal story, a contrastive counterfactual, a global rule set - so methods optimize different, sometimes incompatible, targets. Regulators increasingly demand explanations the science cannot yet certify.",
 "why_it_matters": "Unexplainable models in high-stakes roles are unaccountable power: no appeal, no audit, no learning from mistakes. And explanations that mislead are worse than silence, because they manufacture false understanding.",
 "sig_lens": "The Signature lens reads explanation as a contract: the explainer warrants specific claims about the model, and the warranty must be testable, not decorative.",
 "sig_solution": LABEL + " Assumptions: (1) no single explanation type serves all stakeholders; (2) unfaithful explanations are actively harmful. Reasoning path: replace decorative explanations with warranted ones - each explanation ships with a fidelity test the user can run, and the explanation type is matched to the decision at stake. Proposed mechanism: an explanation-warranty protocol that requires every deployed explanation to pass a fidelity battery (remove-and-retest, counterfactual consistency) and to state its scope (local vs global, which features it covers); high-stakes decisions default to inherently interpretable models. Confirm: warranted explanations reduce user over-reliance errors in trials. Kill: fidelity tests prove too weak to catch misleading explanations. Does NOT claim: a definition of explanation everyone accepts - it warrants claims, it does not settle philosophy.",
 "pointer": "The Signature system's proposed approach warranties every explanation with runnable fidelity tests; the companion Signature Edition record specifies the explanation-warranty protocol.",
 "key_points": [
  "Post-hoc explanations lack fidelity guarantees; saliency maps can be meaningless.",
  "There is no agreed definition of what counts as an explanation.",
  "High-stakes settings may require inherently interpretable models instead.",
  "Misleading explanations cause harmful over-reliance.",
 ],
 "requirements": [
  "A fidelity battery (remove-and-retest, counterfactual checks) for every explanation method.",
  "Scope statements: what the explanation does and does not cover.",
  "Inherently interpretable models as the default for high-stakes decisions.",
 ],
 "citations": [
  "Rudin C (2019) Stop explaining black box machine learning models for high stakes decisions. Nature Machine Intelligence 1: 206-215.",
  "Adebayo J et al. (2018) Sanity checks for saliency maps. NeurIPS.",
 ],
 "demo": {"probs": [0.52, 0.24, 0.14, 0.1], "qpert": [0.44, 0.26, 0.17, 0.13]},
},
# ----------------------------------------------------------------- rank 11
{
 "key": "ds-fairness-impossibility",
 "name": "The Fairness Impossibility in Automated Decisions",
 "group": "Statistics",
 "ladder_rank": 11, "ladder_tier": "foundations",
 "problem": "Can an automated decision system be fair to all groups at once, or do the leading mathematical definitions of fairness contradict each other?",
 "background": "The field converged on several fairness definitions - demographic parity, equalized odds, calibration across groups - and then Kleinberg, Mullainathan and Raghavan (2016) and Chouldechova (2017) proved they cannot all hold simultaneously except in degenerate cases: when base rates differ across groups, a calibrated classifier cannot equalize both false-positive and false-negative rates. This is not a bug to fix but a theorem to live with. The practical fallout is a forced choice of which unfairness to tolerate, usually made implicitly by engineers rather than explicitly by stakeholders. Meanwhile the deeper critiques note that mathematical fairness metrics can legitimize unjust systems by optimizing the metric while leaving the underlying power relations untouched.",
 "why_it_matters": "Automated decisions allocate loans, jobs, bail, and medical care. Pretending all fairness notions are compatible lets vendors claim fairness while choosing, silently, which groups bear the errors.",
 "sig_lens": "The Signature lens reads fairness as a declared tradeoff: the impossibility theorem forces a choice, and the choice must be signed in public, not buried in code.",
 "sig_solution": LABEL + " Assumptions: (1) the impossibility results are theorems, not obstacles; (2) the fairness choice is a values decision, not a technical one. Reasoning path: move the choice out of the code and into a signed fairness charter - stakeholders pick which metric is primary, the system optimizes it, and the sacrificed metrics are reported honestly. Proposed mechanism: a fairness-charter protocol requiring a public, signed statement of the chosen fairness definition, the measured values of all major definitions, and the groups bearing the residual unfairness - reviewed on a schedule, not once. Confirm: chartered systems face fewer post-deployment fairness surprises. Kill: stakeholders sign charters they do not understand, or charters become liability shields. Does NOT claim: a way to satisfy all fairness definitions - the theorem stands; it forces the choice into the light.",
 "pointer": "The Signature system's proposed approach charters the fairness tradeoff explicitly with stakeholder signatures; the companion Signature Edition record specifies the fairness-charter protocol.",
 "key_points": [
  "Leading fairness definitions are provably incompatible when base rates differ.",
  "The incompatibility is a theorem, not an engineering gap.",
  "The choice of which unfairness to tolerate is currently made implicitly.",
  "Metrics alone can legitimize unjust systems without changing outcomes.",
 ],
 "requirements": [
  "A signed fairness charter naming the primary definition and the sacrificed ones.",
  "Measurement of all major fairness definitions, not just the chosen one.",
  "Scheduled review of the charter as populations and base rates shift.",
 ],
 "citations": [
  "Kleinberg J, Mullainathan S, Raghavan M (2016) Inherent trade-offs in the fair determination of risk scores. ITCS.",
  "Chouldechova A (2017) Fair prediction with disparate impact. Big Data 5(2): 153-163.",
 ],
 "demo": {"probs": [0.48, 0.26, 0.16, 0.1], "qpert": [0.4, 0.28, 0.18, 0.14]},
},
# ----------------------------------------------------------------- rank 12
{
 "key": "ds-privacy-utility",
 "name": "The Privacy Against Utility Tradeoff",
 "group": "Statistics",
 "ladder_rank": 12, "ladder_tier": "compounded",
 "problem": "How much useful signal must be destroyed to guarantee that no individual in a dataset can be re-identified, and who gets to set the price?",
 "background": "Differential privacy (Dwork, 2006) gave the first rigorous answer: add calibrated noise so any single person's presence barely changes the output, with a privacy budget epsilon quantifying the guarantee. The US Census Bureau's adoption of differential privacy for the 2020 census made the tradeoff concrete and controversial - small-area statistics degraded visibly, and demographers protested. The core tension is fundamental, not implementational: privacy and utility are conjugate quantities, and the optimal frontier is unknown for most real workloads. Worse, epsilon values in deployment (often 1 to 10) provide weak guarantees that few users understand, and composition of many queries burns the budget fast.",
 "why_it_matters": "Every data release is a bet about re-identification: medical records, census data, location traces. Under-protect and people are exposed; over-protect and the data becomes useless for the research that justified collecting it.",
 "sig_lens": "The Signature lens reads privacy as a budget with a public ledger: every query spends, the balance is visible, and the spending policy is signed before the first query.",
 "sig_solution": LABEL + " Assumptions: (1) privacy and utility are genuinely conjugate - no free lunch; (2) epsilon numbers are meaningless to the people whose privacy is at stake. Reasoning path: translate the budget into plain-language risk statements and let data stewards allocate it across queries like money, with the ledger public. Proposed mechanism: a privacy-budget ledger that converts each epsilon spend into a stated re-identification risk bound, requires steward sign-off per allocation, and publishes the remaining budget; utility loss is measured per query so the price is visible. Confirm: ledgered deployments match their stated risk bounds in audit. Kill: the risk translation misleads and stewards misallocate. Does NOT claim: a way around the tradeoff - it makes the price legible, it does not lower it.",
 "pointer": "The Signature system's proposed approach ledgers the privacy budget in plain-language risk terms; the companion Signature Edition record specifies the budget-ledger protocol.",
 "key_points": [
  "Differential privacy quantifies the guarantee with epsilon, but deployed epsilons are often weak.",
  "The 2020 census deployment showed the utility cost is real and politically charged.",
  "Query composition burns the privacy budget faster than intuition suggests.",
  "The optimal privacy-utility frontier is unknown for most workloads.",
 ],
 "requirements": [
  "A declared privacy budget with per-query accounting.",
  "Plain-language risk translations of epsilon spends.",
  "Measured utility loss per query so the price is visible.",
 ],
 "citations": [
  "Dwork C (2006) Differential privacy. ICALP.",
  "Abowd JM (2018) The US Census Bureau adopts differential privacy. KDD.",
 ],
 "demo": {"probs": [0.6, 0.18, 0.12, 0.1], "qpert": [0.5, 0.22, 0.15, 0.13]},
},
# ----------------------------------------------------------------- rank 13
{
 "key": "ds-ood-generalization",
 "name": "The Out of Distribution Generalization Problem",
 "group": "Machine Learning",
 "ladder_rank": 13, "ladder_tier": "compounded",
 "problem": "Why do models that ace their test sets collapse on slightly different data, and what would it take to learn the stable structure instead of the spurious correlations?",
 "background": "The i.i.d. assumption - train and test drawn from the same distribution - fails everywhere interesting: new hospitals, new cameras, new slang, new fraud. Models latch onto spurious correlations (backgrounds, textures, demographic proxies) because empirical risk minimization rewards any predictive shortcut. The subfield of OOD generalization (Arjovsky et al., invariant risk minimization, 2019) tries to learn features stable across environments, but Gulrajani and Lopez-Paz (2021) showed that with careful tuning, plain ERM matches fancy methods on the standard benchmarks - suggesting the benchmarks, not the methods, are the problem. Genuinely new environments remain the graveyard of deployed models.",
 "why_it_matters": "Deployment IS out-of-distribution: the lab never matches the field. A model that cannot survive distribution shift is a demo, not a tool.",
 "sig_lens": "The Signature lens reads OOD failure as shortcut addiction: the model must be weaned off spurious features by training it where the shortcuts break.",
 "sig_solution": LABEL + " Assumptions: (1) ERM will exploit any stable-looking shortcut; (2) environments where shortcuts break are the only honest teachers. Reasoning path: curate training environments specifically to break known shortcuts, then certify the model on environments held out from training entirely. Proposed mechanism: a shortcut-breaking curriculum that mines the training data for spurious features (via environment splits), retrains with those shortcuts neutralized, and reports an OOD certificate: performance on environments the model never saw. Confirm: certified models degrade less on genuinely new deployments. Kill: unknown shortcuts survive the mining and the certificate is hollow. Does NOT claim: immunity to unprecedented shifts - it hardens against known shortcut families.",
 "pointer": "The Signature system's proposed approach trains on shortcut-breaking environments and issues OOD certificates; the companion Signature Edition record details the curriculum protocol.",
 "key_points": [
  "ERM rewards spurious correlations that break under distribution shift.",
  "Invariant-risk methods have not beaten well-tuned ERM on standard benchmarks.",
  "Benchmarks may be too easy; genuinely new environments still kill models.",
  "Deployment is inherently out-of-distribution.",
 ],
 "requirements": [
  "Training environments that break suspected shortcuts.",
  "Certification on environments fully held out from training.",
  "Shortcut mining to discover the spurious features the model uses.",
 ],
 "citations": [
  "Arjovsky M et al. (2019) Invariant risk minimization. arXiv:1907.02893.",
  "Gulrajani I, Lopez-Paz D (2021) In search of lost domain generalization. ICLR.",
 ],
 "demo": {"probs": [0.42, 0.28, 0.18, 0.12], "qpert": [0.36, 0.28, 0.2, 0.16]},
},
# ----------------------------------------------------------------- rank 14
{
 "key": "ds-adversarial-robustness",
 "name": "Adversarial Examples and Model Robustness",
 "group": "Machine Learning",
 "ladder_rank": 14, "ladder_tier": "compounded",
 "problem": "Why can imperceptible perturbations flip a neural network's prediction, and can models be made robust without surrendering their accuracy?",
 "background": "Szegedy et al. (2013) found that tiny, human-invisible perturbations reliably flip deep network predictions; Goodfellow et al. (2014) tied the phenomenon to linearity in high dimensions. A decade later the problem persists: adversarial training (Madry et al., 2018) buys robustness at a steep price in clean accuracy and compute, certified defenses cover only small perturbation radii, and attackers keep adapting. The accuracy-robustness tradeoff appears fundamental for current architectures - Tsipras et al. (2019) argue robust and accurate features genuinely conflict. Physical-world attacks (stickers on stop signs, adversarial glasses) move the threat from pixels to streets.",
 "why_it_matters": "Brittle models in vision, speech, and control are attack surfaces: a sticker that turns a stop sign into a speed limit sign is not an academic curiosity when cars drive themselves.",
 "sig_lens": "The Signature lens reads adversarial fragility as unguarded borders: the decision boundary lies too close to the data, and the fix is a demilitarized zone, not thicker walls.",
 "sig_solution": LABEL + " Assumptions: (1) the accuracy-robustness tradeoff is real for current architectures; (2) certification, not just empirical defense, is what safety needs. Reasoning path: enforce a margin - a demilitarized zone around training data inside which the prediction cannot change - and certify the radius rather than hoping attacks fail. Proposed mechanism: a margin-enforcement protocol that trains with certified-radius objectives, reports the certified radius per prediction at inference time, and abstains when the radius is too small for the stakes. Confirm: margin-certified models resist adaptive attacks within their radius. Kill: certified radii prove too small for real threat models. Does NOT claim: robustness to all attacks - it certifies a radius, it does not end the arms race.",
 "pointer": "The Signature system's proposed approach enforces certified prediction margins and abstains outside them; the companion Signature Edition record specifies the margin protocol.",
 "key_points": [
  "Imperceptible perturbations reliably flip network predictions.",
  "Adversarial training trades substantial clean accuracy for robustness.",
  "Certified defenses cover only small perturbation radii.",
  "Physical-world attacks bring the threat to safety-critical systems.",
 ],
 "requirements": [
  "Training objectives that maximize the certified radius, not just empirical defense.",
  "Per-prediction certified radii reported at inference time.",
  "Abstention when the certified radius is too small for the stakes.",
 ],
 "citations": [
  "Szegedy C et al. (2013) Intriguing properties of neural networks. ICLR.",
  "Madry A et al. (2018) Towards deep learning models resistant to adversarial attacks. ICLR.",
 ],
 "demo": {"probs": [0.58, 0.2, 0.12, 0.1], "qpert": [0.48, 0.24, 0.15, 0.13]},
},
# ----------------------------------------------------------------- rank 15
{
 "key": "ds-calibration",
 "name": "The Uncertainty Calibration Problem",
 "group": "Machine Learning",
 "ladder_rank": 15, "ladder_tier": "compounded",
 "problem": "When a model says it is 90 percent confident, how can we know it is right 90 percent of the time - and why are modern networks systematically overconfident?",
 "background": "Guo et al. (2017) showed that modern deep networks are poorly calibrated: their confidence far exceeds their accuracy, a regression from earlier, simpler models. Temperature scaling and other post-hoc fixes recalibrate on held-out data, but calibration shatters under distribution shift - exactly when it matters most. The deeper issue is that softmax outputs are not probabilities in any decision-theoretic sense; they are scores wearing probability costumes. Bayesian neural networks, ensembles, and conformal prediction (Vovk et al., 2005) offer principled uncertainty, each with costs: compute, complexity, or assumptions. Safety-critical deployment needs calibrated uncertainty; the field ships overconfidence instead.",
 "why_it_matters": "Decisions need uncertainty, not just predictions: a doctor needs to know when the model is guessing. Overconfident models do not just err - they err while discouraging the human oversight that would catch them.",
 "sig_lens": "The Signature lens reads calibration as honesty accounting: confidence is a currency, and the model must be audited like a bank - reserves must match liabilities.",
 "sig_solution": LABEL + " Assumptions: (1) softmax scores are not probabilities; (2) calibration measured in-distribution tells little about deployment. Reasoning path: attach an independent uncertainty auditor that recalibrates continuously on recent outcomes and reports calibration drift as a first-class metric. Proposed mechanism: a calibration-audit protocol that bins recent predictions by stated confidence, compares against realized accuracy, and forces the model to abstain or defer when the audit shows systematic overconfidence in the current regime. Confirm: audited deployments show fewer high-confidence errors. Kill: the audit lags fast regime changes and certifies stale calibration. Does NOT claim: true Bayesian uncertainty - it audits the honesty of the stated confidence.",
 "pointer": "The Signature system's proposed approach audits calibration continuously and forces abstention on overconfidence; the companion Signature Edition record specifies the calibration-audit protocol.",
 "key_points": [
  "Modern networks are systematically overconfident; calibration has regressed with depth.",
  "Post-hoc fixes like temperature scaling break under distribution shift.",
  "Softmax outputs are scores, not decision-theoretic probabilities.",
  "Principled alternatives (Bayesian, ensembles, conformal) each carry real costs.",
 ],
 "requirements": [
  "Continuous calibration auditing on recent deployment outcomes.",
  "Abstention or deferral when the audit shows overconfidence.",
  "Uncertainty reports that survive distribution shift, not just in-distribution tests.",
 ],
 "citations": [
  "Guo C et al. (2017) On calibration of modern neural networks. ICML.",
  "Vovk V, Gammerman A, Shafer G (2005) Algorithmic Learning in a Random World. Springer.",
 ],
 "demo": {"probs": [0.5, 0.22, 0.16, 0.12], "qpert": [0.43, 0.24, 0.18, 0.15]},
},
# ----------------------------------------------------------------- rank 16
{
 "key": "ds-auto-feature",
 "name": "The Automated Feature Engineering Problem",
 "group": "Data Engineering",
 "ladder_rank": 16, "ladder_tier": "compounded",
 "problem": "Can the craft of turning raw data into predictive features be automated without losing the domain knowledge that makes features meaningful?",
 "background": "Feature engineering was the dark art of the 2000s and 2010s: the winning Kaggle solutions were won on features, not models. Automated tools (Deep Feature Synthesis, Kanter and Veeramachaneni, 2015; AutoML feature pipelines) now generate thousands of candidate features by composing primitives, and deep learning internalized the whole step by learning representations end to end. Yet automation has not replaced the craft: generated features are often uninterpretable, leak-prone, and computationally explosive, and the domain-informed feature - the ratio a clinician knows matters - still beats brute-force synthesis. The open question is whether automation can discover semantically meaningful features or only statistically convenient ones.",
 "why_it_matters": "Features are where domain knowledge enters the model. Automating them badly severs that link; automating them well would democratize modeling for everyone without a domain expert on call.",
 "sig_lens": "The Signature lens reads features as translations: raw data speaks one language, the model another, and a good feature is a faithful translation, not a convenient fiction.",
 "sig_solution": LABEL + " Assumptions: (1) brute-force synthesis finds statistical convenience, not meaning; (2) domain experts remain the bottleneck. Reasoning path: make automated synthesis propose and domain knowledge dispose - generate broadly, then filter through interpretability and stability screens before any feature ships. Proposed mechanism: a translation-verdict protocol where synthesized features must pass three gates (stable across time splits, interpretable in domain terms, non-redundant) before entering the model, with rejected features logged as evidence of what the data does not support. Confirm: gated synthesis matches expert features on benchmarks with less expert time. Kill: the gates reject genuinely useful but uninterpretable features and performance suffers. Does NOT claim: discovery of deep domain truths - it industrializes the craft without replacing the craftsman.",
 "pointer": "The Signature system's proposed approach gates synthesized features on stability, interpretability, and non-redundancy; the companion Signature Edition record specifies the translation-verdict protocol.",
 "key_points": [
  "Classical ML was won on features; deep learning internalized feature learning.",
  "Automated synthesis generates thousands of candidates but many are leaky or meaningless.",
  "Domain-informed features still beat brute-force synthesis in practice.",
  "The open question is semantic discovery versus statistical convenience.",
 ],
 "requirements": [
  "Stability screening of synthesized features across time splits.",
  "Interpretability review in domain terms before features ship.",
  "Logging of rejected features as negative evidence.",
 ],
 "citations": [
  "Kanter JM, Veeramachaneni K (2015) Deep feature synthesis. IEEE DSAA.",
 ],
 "demo": {"probs": [0.46, 0.26, 0.16, 0.12], "qpert": [0.39, 0.27, 0.18, 0.16]},
},
# ----------------------------------------------------------------- rank 17
{
 "key": "ds-small-data",
 "name": "The Small Data Problem in Deep Learning",
 "group": "Machine Learning",
 "ladder_rank": 17, "ladder_tier": "compounded",
 "problem": "How can deep learning work when there are only hundreds of examples - rare diseases, low-resource languages, novel materials - instead of millions?",
 "background": "Deep learning's victories are victories of scale: ImageNet's millions of images, web-scale text. But most real problems are small-data problems - a rare disease with 200 cases, a factory with 50 failure logs, a language with no web corpus. The standard escapes are transfer learning, few-shot meta-learning (Finn et al., MAML, 2017), data augmentation, and synthetic data, yet each has limits: transfer helps only when the source resembles the target, few-shot methods shine on benchmarks but wobble in the wild, and augmentation cannot invent information the data lacks. The fundamental question - how much can be learned from how little, and when - has no general answer.",
 "why_it_matters": "The long tail of important problems is small-data by nature. A learning paradigm that only works at web scale abandons medicine's rare cases, science's novel phenomena, and every community too small to generate big data.",
 "sig_lens": "The Signature lens reads small data as precious testimony: with few witnesses, each one must be heard fully, and the uncertainty must be reported at full volume.",
 "sig_solution": LABEL + " Assumptions: (1) small data cannot support the same claims as big data; (2) prior knowledge is the only honest supplement. Reasoning path: quantify exactly what the small sample licenses via exact (non-asymptotic) inference, import prior knowledge explicitly as priors or constraints, and report the wide bands without shame. Proposed mechanism: a small-data charter that requires exact finite-sample uncertainty quantification, explicit prior declarations, and a stated minimum-detectable-effect before modeling begins - claims beyond the charter are forbidden. Confirm: chartered small-data studies replicate better than unchartered ones. Kill: priors smuggle in the answer and the charter becomes theater. Does NOT claim: learning from nothing - it rightsizes the claims to the evidence.",
 "pointer": "The Signature system's proposed approach charters small-data studies with exact uncertainty and explicit priors; the companion Signature Edition record specifies the small-data charter.",
 "key_points": [
  "Deep learning's wins are wins of scale; most real problems are small-data.",
  "Transfer and few-shot learning help only when source resembles target.",
  "Augmentation cannot invent information the data lacks.",
  "No general theory says how much can be learned from how little.",
 ],
 "requirements": [
  "Exact finite-sample uncertainty quantification, not asymptotic approximations.",
  "Explicit prior declarations with their influence measured.",
  "A stated minimum detectable effect before modeling begins.",
 ],
 "citations": [
  "Finn C, Abbeel P, Levine S (2017) Model-agnostic meta-learning. ICML.",
 ],
 "demo": {"probs": [0.54, 0.2, 0.14, 0.12], "qpert": [0.46, 0.23, 0.16, 0.15]},
},
# ----------------------------------------------------------------- rank 18
{
 "key": "ds-time-causality",
 "name": "The Time Series Causality Problem",
 "group": "Statistics",
 "ladder_rank": 18, "ladder_tier": "compounded",
 "problem": "When one time series reliably precedes another, when does that precedence license a causal claim - and when is it just Granger causality, prediction without causation?",
 "background": "Clive Granger (1969) defined a pragmatic test: X Granger-causes Y if past X improves forecasts of Y beyond past Y alone. Economists and neuroscientists use it constantly - and constantly overclaim, because Granger causality is predictability, not causation: a barometer Granger-causes rain in the statistical sense. True causal inference in time series needs interventions or strong structural models (structural VARs, dynamic causal modeling), and the confounders are often unmeasured common drivers with their own dynamics. With high-frequency data the problems multiply: temporal aggregation, lead-lag estimation, and nonstationarity can manufacture or mask causal signatures at will.",
 "why_it_matters": "Policy and trading and medicine all ask time-series causal questions: will raising rates cool inflation, does this neural region drive that one. Mistaking precedence for causation turns the arrow of time into an arrow of error.",
 "sig_lens": "The Signature lens reads temporal precedence as a witness that must be cross-examined: prediction is testimony, and testimony needs corroboration before it becomes verdict.",
 "sig_solution": LABEL + " Assumptions: (1) Granger causality is prediction, and prediction is not causation; (2) unmeasured common drivers are the rule, not the exception. Reasoning path: require every temporal causal claim to survive a corroboration battery - intervention evidence where available, mechanism plausibility, and sensitivity to unmeasured confounding - before the causal verb is licensed. Proposed mechanism: a temporal-verdict protocol that grades time-series causal claims on a scale from precedes through predicts to causes, each grade requiring strictly stronger evidence, with the grade printed on every chart. Confirm: graded claims reverse less often than ungraded ones. Kill: the grades become fine print nobody reads. Does NOT claim: a test that converts precedence into causation - it labels the distance between them.",
 "pointer": "The Signature system's proposed approach grades temporal causal claims from precedes to causes with escalating evidence; the companion Signature Edition record specifies the temporal-verdict protocol.",
 "key_points": [
  "Granger causality measures predictive precedence, not causation.",
  "Unmeasured common drivers with their own dynamics are the standard confounder.",
  "Temporal aggregation and nonstationarity can manufacture causal signatures.",
  "Structural models buy causality with strong, often unverifiable assumptions.",
 ],
 "requirements": [
  "A graded claim scale (precedes, predicts, causes) with evidence thresholds.",
  "Corroboration battery: interventions, mechanisms, confounding sensitivity.",
  "The grade printed on every chart and headline, not buried in methods.",
 ],
 "citations": [
  "Granger CWJ (1969) Investigating causal relations by econometric models and cross-spectral methods. Econometrica 37(3): 424-438.",
 ],
 "demo": {"probs": [0.44, 0.28, 0.16, 0.12], "qpert": [0.37, 0.28, 0.19, 0.16]},
},
# ----------------------------------------------------------------- rank 19
{
 "key": "ds-recommender-loops",
 "name": "The Recommender Feedback Loop Problem",
 "group": "Machine Learning",
 "ladder_rank": 19, "ladder_tier": "compounded",
 "problem": "When a recommender system shapes the very behavior it learns from, how can it tell whether its predictions are accurate or merely self-fulfilling?",
 "background": "Recommenders create the data they train on: shown items get clicks, clicked items look relevant, relevance justifies showing them again. This feedback loop amplifies popularity bias, collapses diversity, and can radicalize or bore users into degenerate equilibria - the filter-bubble debate is one facet. Researchers have named the pathologies (exposure bias, position bias, feedback loops; Chaney et al., 2018) and proposed correctives: randomization, exploration, counterfactual evaluation, diversity objectives. But exploration costs engagement today for knowledge tomorrow, and no platform willingly pays that bill at scale. The measurement problem is fundamental: the counterfactual - what the user would have liked unshown - is never observed.",
 "why_it_matters": "Recommenders mediate what billions read, watch, and buy. A loop that mistakes its own influence for user preference does not serve users - it farms them, and calls the harvest engagement.",
 "sig_lens": "The Signature lens reads the feedback loop as a hall of mirrors: the system must break the glass periodically with randomized exposure, or it will mistake its reflection for the world.",
 "sig_solution": LABEL + " Assumptions: (1) the counterfactual of unshown items is never observed; (2) pure exploitation converges to degenerate equilibria. Reasoning path: budget a fixed exploration share that cannot be optimized away, measure with counterfactual estimators, and report loop-health metrics alongside engagement. Proposed mechanism: a mirror-breaking protocol mandating a randomized exploration budget, inverse-propensity-weighted evaluation of what was learned, and quarterly loop-health audits (diversity, novelty, user-control metrics) with the power to override engagement KPIs. Confirm: audited systems sustain diversity without engagement collapse. Kill: exploration budgets get quietly reallocated to exploitation. Does NOT claim: knowledge of true user preferences - it keeps the system honest about its own influence.",
 "pointer": "The Signature system's proposed approach budgets exploration, evaluates counterfactually, and audits loop health; the companion Signature Edition record specifies the mirror-breaking protocol.",
 "key_points": [
  "Recommenders train on behavior they themselves shaped - a fundamental confounding.",
  "Feedback loops amplify popularity bias and collapse diversity.",
  "Exploration costs present engagement for future knowledge; platforms underinvest.",
  "The counterfactual of unshown items is never observed.",
 ],
 "requirements": [
  "A protected randomized exploration budget.",
  "Counterfactual (propensity-weighted) evaluation of recommendations.",
  "Loop-health audits with authority over engagement KPIs.",
 ],
 "citations": [
  "Chaney AJB et al. (2018) How algorithmic confounding in recommendation systems increases homogeneity and decreases utility. RecSys.",
 ],
 "demo": {"probs": [0.62, 0.18, 0.12, 0.08], "qpert": [0.52, 0.22, 0.14, 0.12]},
},
# ----------------------------------------------------------------- rank 20
{
 "key": "ds-graph-expressivity",
 "name": "The Graph Learning Expressivity Limit",
 "group": "Machine Learning",
 "ladder_rank": 20, "ladder_tier": "compounded",
 "problem": "What structural patterns can graph neural networks fundamentally not distinguish, and does that limit matter for real molecular, social, and knowledge graphs?",
 "background": "Message-passing graph neural networks are bounded by the Weisfeiler-Lehman isomorphism test: Xu et al. (2019) proved standard GNNs cannot distinguish graphs that 1-WL cannot, which includes many regular structures. The field responded with higher-order GNNs, subgraph methods, and positional encodings that climb the WL hierarchy at steep computational cost. The open question is practical, not just theoretical: do real tasks need beyond-WL expressivity, or do the standard architectures already capture what molecules and social networks require? Evidence is mixed - expressive models win on synthetic benchmarks designed to need them and often tie on real ones, suggesting the benchmarks, again, may be the problem.",
 "why_it_matters": "Molecules, proteins, power grids, and fraud rings are graphs. If the workhorse architectures are blind to structures that matter, entire application areas rest on a representational ceiling nobody can see through.",
 "sig_lens": "The Signature lens reads expressivity as eyesight: the question is not how powerful the model could be, but which structures the task actually requires it to see.",
 "sig_solution": LABEL + " Assumptions: (1) the WL bound is a theorem about standard message passing; (2) practical need for beyond-WL power is task-dependent and unmeasured. Reasoning path: test whether the task needs the eyesight before buying stronger glasses - probe datasets with WL-failing pairs and escalate architecture only where probes show blindness. Proposed mechanism: an eyesight-probe protocol that constructs task-relevant WL-indistinguishable pairs, measures whether the current model treats them differently when the labels demand it, and upgrades to higher-order methods only on probe failure. Confirm: probe-guided upgrades beat blanket expressive architectures on cost-adjusted performance. Kill: real tasks need expressivity the probes cannot construct. Does NOT claim: a free climb up the WL hierarchy - expressivity is priced in compute.",
 "pointer": "The Signature system's proposed approach probes task-relevant WL blindness before buying expressivity; the companion Signature Edition record specifies the eyesight-probe protocol.",
 "key_points": [
  "Standard message-passing GNNs are bounded by the 1-Weisfeiler-Lehman test.",
  "Higher-order methods climb the hierarchy at steep computational cost.",
  "Whether real tasks need beyond-WL power remains empirically open.",
  "Synthetic benchmarks may overstate the practical need.",
 ],
 "requirements": [
  "Task-relevant WL-indistinguishable probe pairs.",
  "Measurement of whether label-relevant distinctions survive the WL bound.",
  "Cost-accounted escalation to higher-order methods only on probe failure.",
 ],
 "citations": [
  "Xu K et al. (2019) How powerful are graph neural networks? ICLR.",
 ],
 "demo": {"probs": [0.4, 0.3, 0.18, 0.12], "qpert": [0.34, 0.3, 0.2, 0.16]},
},
# ----------------------------------------------------------------- rank 21
{
 "key": "ds-synthetic-data",
 "name": "The Synthetic Data Fidelity Problem",
 "group": "Data Engineering",
 "ladder_rank": 21, "ladder_tier": "compounded",
 "problem": "When real data cannot be shared - privacy, scarcity, cost - how can we verify that synthetic data preserves what matters without leaking what must stay hidden?",
 "background": "Generative models now synthesize tabular data, images, and text well enough to train on, and privacy law increasingly pushes organizations toward synthetic substitutes. But fidelity is multi-dimensional: marginal distributions, joint dependencies, rare subgroups, and downstream task performance can each pass or fail independently. Worse, the failure modes are adversarial to naive checks - a generator can match every marginal while destroying the joint structure, or memorize training records (Carlini et al. showed extraction attacks against large generators). The privacy-fidelity frontier is genuinely unmapped: too faithful and the synthetic data leaks; too private and it teaches the wrong lessons.",
 "why_it_matters": "Synthetic data is becoming the legal workaround for data sharing in medicine, finance, and government. If its fidelity cannot be certified, every downstream model trains on a plausible fiction - and if its privacy cannot be certified, the workaround is a breach.",
 "sig_lens": "The Signature lens reads synthetic data as a forgery that must pass two authentications: faithful enough to teach from, and private enough to share.",
 "sig_solution": LABEL + " Assumptions: (1) fidelity is multi-dimensional and partial failure is the norm; (2) memorization is a privacy failure, not a fidelity success. Reasoning path: certify synthetic data on a battery - distributional, relational, subgroup, and downstream-task fidelity plus extraction-resistance - and ship the certificate with the data. Proposed mechanism: a dual-authentication protocol requiring passing scores on all four fidelity dimensions and on membership-inference resistance before synthetic data may substitute for real data in any regulated use. Confirm: certified synthetic data trains models that transfer to real data within tolerance. Kill: the battery misses a fidelity dimension that matters downstream. Does NOT claim: a universal synthetic substitute - the certificate is per-use-case.",
 "pointer": "The Signature system's proposed approach dual-authenticates synthetic data on fidelity and privacy batteries; the companion Signature Edition record specifies the authentication protocol.",
 "key_points": [
  "Fidelity spans marginals, joints, subgroups, and downstream tasks - each can fail alone.",
  "Generators can memorize training records, turning synthesis into leakage.",
  "The privacy-fidelity frontier is unmapped for most data types.",
  "Naive checks (matching marginals) miss joint-structure destruction.",
 ],
 "requirements": [
  "A four-dimension fidelity battery with per-dimension passing scores.",
  "Membership-inference and extraction resistance testing.",
  "Per-use-case certificates, not blanket synthetic approval.",
 ],
 "citations": [
  "Carlini N et al. (2021) Extracting training data from large language models. USENIX Security.",
 ],
 "demo": {"probs": [0.56, 0.2, 0.14, 0.1], "qpert": [0.47, 0.24, 0.16, 0.13]},
},
# ----------------------------------------------------------------- rank 22
{
 "key": "ds-federated-noniid",
 "name": "The Federated Learning Non-IID Problem",
 "group": "Machine Learning",
 "ladder_rank": 22, "ladder_tier": "compounded",
 "problem": "When data lives on millions of devices that cannot share it, how can a global model learn from clients whose data distributions wildly disagree?",
 "background": "Federated learning (McMahan et al., 2017) trains across decentralized devices without centralizing data - the privacy-preserving dream behind phone keyboards and medical consortia. The nightmare is statistical heterogeneity: each client's data is non-IID, drawn from its own skewed distribution, so local updates pull the global model in incompatible directions (client drift). FedAvg converges under IID assumptions; under real heterogeneity it can diverge or crawl. Fixes - proximal terms (FedProx), variance reduction (SCAFFOLD), personalization layers - help, but the fundamental tension remains: one global model cannot fit a thousand different worlds, and personalization fragments the very collaboration federated learning promises.",
 "why_it_matters": "The most sensitive data - medical, personal, industrial - cannot be centralized. If federated learning only works when clients agree, it fails exactly where privacy matters most.",
 "sig_lens": "The Signature lens reads federation as a parliament: clients are constituencies with divergent interests, and the protocol must represent them, not average them into mush.",
 "sig_solution": LABEL + " Assumptions: (1) client distributions genuinely disagree; (2) one global model cannot fit all worlds. Reasoning path: stop forcing consensus - learn a shared representation plus client-specific heads, and report per-client performance, not just the global average. Proposed mechanism: a parliamentary protocol with a shared backbone, personalized heads, and a representation-quality audit; the global objective explicitly trades off shared knowledge against client fit, and no client ships a model worse than its local-only baseline. Confirm: parliamentary models beat both pure-global and pure-local on held-out clients. Kill: personalization fragments into a thousand local models and the federation adds nothing. Does NOT claim: a free lunch on heterogeneity - it represents the disagreement instead of averaging it away.",
 "pointer": "The Signature system's proposed approach federates as a parliament with shared backbone and personal heads; the companion Signature Edition record specifies the parliamentary protocol.",
 "key_points": [
  "Non-IID client data causes client drift that breaks FedAvg convergence.",
  "Statistical heterogeneity is the norm in privacy-sensitive deployments.",
  "Proximal and variance-reduction fixes help but do not resolve the tension.",
  "One global model cannot fit fundamentally different client worlds.",
 ],
 "requirements": [
  "Per-client performance reporting, not just global averages.",
  "A no-harm guarantee: no client does worse than its local-only model.",
  "Explicit tradeoff accounting between shared and personalized components.",
 ],
 "citations": [
  "McMahan B et al. (2017) Communication-efficient learning of deep networks from decentralized data. AISTATS.",
 ],
 "demo": {"probs": [0.38, 0.3, 0.2, 0.12], "qpert": [0.33, 0.29, 0.21, 0.17]},
},
# ----------------------------------------------------------------- rank 23
{
 "key": "ds-benchmark-saturation",
 "name": "The Benchmark Saturation Problem",
 "group": "Data Engineering",
 "ladder_rank": 23, "ladder_tier": "compounded",
 "problem": "When models saturate every benchmark, how can the field tell whether capabilities are genuinely advancing or the tests have just been memorized and gamed?",
 "background": "Benchmarks drive the field - ImageNet, GLUE, SuperGLUE - and benchmarks die: models hit the ceiling, then the ceiling turns out to have been the test set leaking into training. Recht et al. (2019) showed ImageNet models generalize to a fresh test set with a consistent accuracy drop, implying years of tuning to the specific test distribution. Contamination is now endemic at web scale: test items appear in pretraining corpora, and decontamination is an arms race the test-makers are losing. Goodhart's law rules: when the benchmark becomes the target, it ceases to be a good measure. The field has no agreed replacement - live leaderboards, private held-outs, and human evaluation each have their own failure modes.",
 "why_it_matters": "If the scoreboard is broken, the race is theater: billions in compute chase leaderboard positions that may measure memorization, not capability. Decisions about what AI can do rest on numbers nobody fully trusts.",
 "sig_lens": "The Signature lens reads benchmarks as exams that must be proctored: a test the student has seen is not a test, and the proctoring must be continuous, not ceremonial.",
 "sig_solution": LABEL + " Assumptions: (1) any static public benchmark will be contaminated; (2) capability claims need adversarial, not cooperative, measurement. Reasoning path: replace static leaderboards with living evaluation - private held-outs, time-gated releases, and human-judged open tasks - and report contamination audits alongside scores. Proposed mechanism: a proctored-evaluation protocol requiring contamination screening (n-gram and embedding overlap against training corpora), private test refresh on a schedule, and a published audit trail; scores without audits are marked provisional. Confirm: proctored scores predict real-task performance better than leaderboard scores. Kill: even private tests leak through API probing and human memory. Does NOT claim: an ungameable benchmark - it makes the gaming visible and priced.",
 "pointer": "The Signature system's proposed approach proctors evaluation with contamination audits and living tests; the companion Signature Edition record specifies the proctoring protocol.",
 "key_points": [
  "Saturated benchmarks often measure test-set tuning, not capability gains.",
  "Web-scale pretraining contaminates public test sets routinely.",
  "Goodhart's law: targeted metrics stop measuring what they were meant to.",
  "No replacement (live boards, private tests, human eval) is failure-free.",
 ],
 "requirements": [
  "Contamination screening against training corpora for every reported score.",
  "Private, refreshed test sets on a published schedule.",
  "Audit trails marking unaudited scores as provisional.",
 ],
 "citations": [
  "Recht B et al. (2019) Do ImageNet classifiers generalize to ImageNet? ICML.",
 ],
 "demo": {"probs": [0.5, 0.24, 0.14, 0.12], "qpert": [0.42, 0.26, 0.17, 0.15]},
},
# ----------------------------------------------------------------- rank 24
{
 "key": "ds-double-descent",
 "name": "Why Overparameterized Models Generalize",
 "group": "Machine Learning",
 "ladder_rank": 24, "ladder_tier": "advanced",
 "problem": "Classical theory says models with more parameters than data points should memorize and fail - so why do the biggest neural networks generalize best?",
 "background": "The classical U-curve (test error falls then rises with capacity) broke around 2019: Belkin et al. documented double descent, where error falls, rises near the interpolation threshold, then falls again as parameters grow far beyond data points. Zhang et al. (2017) had already shown networks fit random labels yet generalize on real data. Candidate explanations abound - implicit regularization of gradient descent, benign overfitting (Bartlett et al., 2020), the neural tangent kernel regime - but none commands consensus, and each explains some phenomena while failing others. Practitioners now routinely train models with billions of parameters on millions of examples, operating entirely beyond the theory that is supposed to govern them.",
 "why_it_matters": "The central empirical fact of modern AI - scale works - has no agreed theoretical explanation. Without one, the field cannot predict when scaling stops working, which is the most expensive question in computing.",
 "sig_lens": "The Signature lens reads double descent as a phase transition: the model changes kind at the interpolation threshold, and the theory must describe the new phase, not the old one.",
 "sig_solution": LABEL + " Assumptions: (1) classical capacity theory describes the wrong phase; (2) the truth involves the interaction of architecture, optimizer, and data structure. Reasoning path: characterize the post-interpolation phase directly - measure the effective complexity actually used (not parameter count) and map where the second descent begins across architectures. Proposed mechanism: a phase-mapping protocol that empirically charts the interpolation threshold and second-descent region for each architecture family, then restricts deployment claims to the mapped region; unmapped scale-ups are labeled experimental. Confirm: phase-mapped scaling predictions beat naive extrapolation on new architectures. Kill: the phase structure proves architecture-specific to the point of useless generality. Does NOT claim: a proof of why scale works - it maps the territory, it does not explain the geology.",
 "pointer": "The Signature system's proposed approach maps the double-descent phase structure per architecture family; the companion Signature Edition record specifies the phase-mapping protocol.",
 "key_points": [
  "Double descent violates the classical U-curve of test error versus capacity.",
  "Networks memorize random labels yet generalize on structured data.",
  "Candidate theories (implicit regularization, benign overfitting, NTK) each explain only part.",
  "Practice operates billions of parameters beyond any agreed theory.",
 ],
 "requirements": [
  "Empirical mapping of the interpolation threshold per architecture.",
  "Measurement of effective used complexity, not raw parameter counts.",
  "Experimental labeling for scale-ups outside mapped regions.",
 ],
 "citations": [
  "Belkin M et al. (2019) Reconciling modern machine-learning practice and the classical bias-variance trade-off. PNAS 116(32).",
  "Bartlett PL et al. (2020) Benign overfitting in linear regression. PNAS 117(48).",
 ],
 "demo": {"probs": [0.36, 0.28, 0.2, 0.16], "qpert": [0.31, 0.28, 0.22, 0.19]},
},
# ----------------------------------------------------------------- rank 25
{
 "key": "ds-scaling-laws",
 "name": "The Scaling Laws Theoretical Basis",
 "group": "Machine Learning",
 "ladder_rank": 25, "ladder_tier": "advanced",
 "problem": "Model performance follows eerily smooth power laws in parameters, data, and compute - but why these exponents, and where do the laws break?",
 "background": "Kaplan et al. (2020) found that language-model loss scales as a power law in model size, dataset size, and compute, with smooth predictable curves that let labs budget hundred-million-dollar training runs. Hoffmann et al. (2022, Chinchilla) refined the compute-optimal tradeoffs and showed many models were undertrained. Yet the laws are empirical, not derived: no theory predicts the exponents from first principles, and the breaks are poorly understood - emergent capabilities appear discontinuously, downstream task performance does not follow loss smoothly, and the laws say nothing about data quality. The field plans its future on curves it cannot derive and whose failure modes it cannot foresee.",
 "why_it_matters": "Scaling laws are the central planning instrument of the AI industry: they decide billion-dollar compute budgets. An empirical law with unknown breaking points is a load-bearing guess.",
 "sig_lens": "The Signature lens reads scaling laws as weather charts: useful for sailing, dangerous for navigation - the wise captain watches for the storm the chart cannot show.",
 "sig_solution": LABEL + " Assumptions: (1) the power laws are real but underived; (2) the breaks matter more than the trends. Reasoning path: hunt the breaks deliberately - stress-test scaling predictions at the edges (data quality cliffs, capability discontinuities) and attach break-risk to every extrapolation. Proposed mechanism: a break-hunting protocol that requires scaling-based plans to state their extrapolation distance, to test predictions on held-out scale points before committing budgets, and to carry explicit break-risk reserves. Confirm: break-hunted plans hit their targets more reliably. Kill: breaks prove unpredictable in principle and the reserves are theater. Does NOT claim: a derivation of the exponents - it navigates by the chart while watching the sky.",
 "pointer": "The Signature system's proposed approach hunts scaling-law breaks and budgets break-risk reserves; the companion Signature Edition record specifies the break-hunting protocol.",
 "key_points": [
  "Loss follows power laws in parameters, data, and compute with smooth curves.",
  "Chinchilla showed many models were undertrained for their compute.",
  "No theory derives the exponents; emergent capabilities break smoothness.",
  "Downstream task performance does not track loss predictably.",
 ],
 "requirements": [
  "Stated extrapolation distance for every scaling-based plan.",
  "Held-out scale-point tests before budget commitment.",
  "Explicit break-risk reserves in compute planning.",
 ],
 "citations": [
  "Kaplan J et al. (2020) Scaling laws for neural language models. arXiv:2001.08361.",
  "Hoffmann J et al. (2022) Training compute-optimal large language models. arXiv:2203.15556.",
 ],
 "demo": {"probs": [0.52, 0.22, 0.14, 0.12], "qpert": [0.44, 0.24, 0.17, 0.15]},
},
# ----------------------------------------------------------------- rank 26
{
 "key": "ds-compute-statistics",
 "name": "The Computational Against Statistical Tradeoff",
 "group": "Statistics",
 "ladder_rank": 26, "ladder_tier": "advanced",
 "problem": "Some problems are statistically solvable but computationally intractable - where exactly is the frontier, and how should practitioners navigate it?",
 "background": "Statistics traditionally asked what is learnable with infinite computation; computer science asks what is learnable efficiently. The intersection has gaps: sparse PCA is statistically possible at one signal strength but no known polynomial algorithm succeeds until a higher one (Berthet and Rigollet, 2013) - a computational-statistical gap. Planted clique, sparse regression, and tensor problems show similar gaps, often tied to average-case hardness conjectures. For practitioners the question is brutally concrete: given a budget of compute and data, which problems are worth attempting? The theory offers phase diagrams for toy models; the messy middle of real problems has no map.",
 "why_it_matters": "Every modeling project spends two currencies - data and compute - and the exchange rate between them is unknown. Projects fail when they buy data for a problem that needed compute, or compute for one that needed data.",
 "sig_lens": "The Signature lens reads the gap as a strait between two shores: the map must mark where the ferries stop running, so travelers do not sail into the fog expecting a bridge.",
 "sig_solution": LABEL + " Assumptions: (1) computational-statistical gaps are real and widespread; (2) practitioners currently navigate without a map. Reasoning path: build an empirical frontier atlas - for each problem family, chart the observed boundary between feasible and infeasible across compute and data budgets. Proposed mechanism: a frontier-atlas protocol that records, per problem family, the compute-data combinations that succeeded or failed in practice, publishes the observed frontier, and flags projects planned inside the infeasible region before money is spent. Confirm: atlas-guided project selection wastes less compute on infeasible regimes. Kill: real problems prove too heterogeneous for family-level frontiers. Does NOT claim: proofs of the gaps - it charts the observed strait, it does not explain the currents.",
 "pointer": "The Signature system's proposed approach charts empirical compute-data feasibility frontiers per problem family; the companion Signature Edition record specifies the atlas protocol.",
 "key_points": [
  "Sparse PCA and planted clique show gaps between statistical and computational feasibility.",
  "Gaps are tied to average-case hardness conjectures, not proven separations.",
  "Practitioners trade data against compute with no map of the exchange rate.",
  "Theory covers toy models; real problems sit in the unmapped middle.",
 ],
 "requirements": [
  "Per-family records of compute-data combinations tried, with outcomes.",
  "Published observed frontiers, updated as evidence accumulates.",
  "Pre-spend feasibility flags for projects inside infeasible regions.",
 ],
 "citations": [
  "Berthet Q, Rigollet P (2013) Optimal detection of sparse principal components in high dimension. Annals of Statistics 41(4).",
 ],
 "demo": {"probs": [0.48, 0.24, 0.16, 0.12], "qpert": [0.4, 0.26, 0.18, 0.16]},
},
# ----------------------------------------------------------------- rank 27
{
 "key": "ds-optimal-transport",
 "name": "The Optimal Transport Curse in High Dimensions",
 "group": "Statistics",
 "ladder_rank": 27, "ladder_tier": "advanced",
 "problem": "Optimal transport gives the mathematically right way to compare distributions - so why does estimating it from samples collapse in high dimensions?",
 "background": "The Wasserstein distance is the principled metric between probability distributions, powering applications from generative modeling to domain adaptation. But its sample complexity is cursed: estimating it in d dimensions needs roughly n^{-1/d} samples (Fournier and Guillin, 2015) - exponentially many as dimension grows. Entropic regularization (Cuturi, 2013, Sinkhorn) buys computation at the price of blurring the metric, and sliced or low-dimensional variants buy tractability at the price of the very geometry that made transport attractive. Practitioners use Wasserstein-flavored objectives everywhere while the quantity they approximate degrades silently with dimension.",
 "why_it_matters": "Generative models, domain adaptation, and distributional robustness all lean on transport geometry. If the estimated distances are noise in high dimensions, the objectives optimize a mirage.",
 "sig_lens": "The Signature lens reads the curse as a toll road: the geometry is worth the price only where the toll is affordable, and the ledger must show the toll paid.",
 "sig_solution": LABEL + " Assumptions: (1) the n^{-1/d} rate is a theorem, not a challenge; (2) regularized variants change the question being answered. Reasoning path: measure the estimation error of the transport quantity actually used, and report it alongside the objective value - optimize the estimate, not the fantasy. Proposed mechanism: a toll-ledger protocol that computes sample-complexity bounds for the transport variant in use, requires the estimated error bars on reported distances, and switches to low-dimensional projections only with the projection loss quantified. Confirm: toll-ledgered objectives correlate better with downstream performance. Kill: the error bars prove too wide to be actionable and get ignored. Does NOT claim: a cure for the curse - it prices the toll, it does not pave the road.",
 "pointer": "The Signature system's proposed approach ledgers the estimation toll on every transport computation; the companion Signature Edition record specifies the toll-ledger protocol.",
 "key_points": [
  "Wasserstein estimation needs exponentially many samples as dimension grows.",
  "Entropic regularization buys speed by blurring the metric itself.",
  "Sliced variants sacrifice the geometry that motivated transport.",
  "Practitioners optimize transport objectives whose estimates are noise.",
 ],
 "requirements": [
  "Sample-complexity bounds computed for the transport variant in use.",
  "Error bars on every reported transport distance.",
  "Quantified projection loss when low-dimensional variants are used.",
 ],
 "citations": [
  "Cuturi M (2013) Sinkhorn distances: lightspeed computation of optimal transport. NeurIPS.",
  "Fournier N, Guillin A (2015) On the rate of convergence in Wasserstein distance. PTRF 162.",
 ],
 "demo": {"probs": [0.34, 0.3, 0.2, 0.16], "qpert": [0.3, 0.28, 0.22, 0.2]},
},
# ----------------------------------------------------------------- rank 28
{
 "key": "ds-manifold-hypothesis",
 "name": "The Manifold Hypothesis Validation Problem",
 "group": "Machine Learning",
 "ladder_rank": 28, "ladder_tier": "advanced",
 "problem": "Deep learning assumes real data concentrates near low-dimensional manifolds - but how would we know if the hypothesis is false, and what breaks if it is?",
 "background": "The manifold hypothesis - that high-dimensional data like images lies near a low-dimensional manifold - is the unspoken foundation of representation learning. Intrinsic-dimension estimators (nearest-neighbor scaling, TwoNN) suggest image datasets have intrinsic dimensions in the tens, far below pixel counts, which comforts practitioners. But the estimates are fragile, the hypothesis is rarely tested as a hypothesis, and counterexamples lurk: adversarial examples may live off the manifold, and some data types (text, graphs) fit the manifold picture awkwardly. If the hypothesis fails for a domain, the entire representation-learning playbook - autoencoders, contrastive learning, diffusion models - rests on a false premise there.",
 "why_it_matters": "Trillions of parameters are trained on the assumption that data has low-dimensional structure. An untested foundation is a structural risk to the whole enterprise.",
 "sig_lens": "The Signature lens reads the hypothesis as a load-bearing wall: before building more floors, test whether the wall is actually holding weight.",
 "sig_solution": LABEL + " Assumptions: (1) the hypothesis is currently an article of faith, not a tested claim; (2) different domains may differ. Reasoning path: turn the hypothesis into a falsifiable claim per domain - predict specific geometric signatures (scaling laws of neighbor distances, off-manifold behavior) and test them. Proposed mechanism: a foundation-test protocol that estimates intrinsic dimension with multiple independent estimators, checks their agreement, and probes off-manifold behavior with adversarial and synthetic probes; domains failing the tests get non-manifold methods. Confirm: tested domains show better method selection and fewer surprises. Kill: the estimators disagree too wildly to support any verdict. Does NOT claim: a proof of the hypothesis anywhere - it makes the faith measurable.",
 "pointer": "The Signature system's proposed approach tests the manifold hypothesis per domain with independent estimators; the companion Signature Edition record specifies the foundation-test protocol.",
 "key_points": [
  "The manifold hypothesis underwrites representation learning but is rarely tested.",
  "Intrinsic-dimension estimates suggest low dimension but are fragile.",
  "Adversarial examples may exploit off-manifold directions.",
  "Text and graphs fit the manifold picture less cleanly than images.",
 ],
 "requirements": [
  "Multiple independent intrinsic-dimension estimators with agreement checks.",
  "Off-manifold probes (adversarial, synthetic) per domain.",
  "Non-manifold method alternatives for domains that fail the tests.",
 ],
 "citations": [
  "Fefferman C et al. (2016) Testing the manifold hypothesis. JAMS 29(4).",
 ],
 "demo": {"probs": [0.44, 0.26, 0.18, 0.12], "qpert": [0.37, 0.27, 0.2, 0.16]},
},
# ----------------------------------------------------------------- rank 29
{
 "key": "ds-metalearning-theory",
 "name": "The AutoML Meta Learning Theory Problem",
 "group": "Machine Learning",
 "ladder_rank": 29, "ladder_tier": "advanced",
 "problem": "Meta-learning promises to learn how to learn - but when does experience on past tasks actually help on new ones, and when is it just expensive overfitting to the task distribution?",
 "background": "Meta-learning (learning to learn) trains across tasks so new tasks need few examples - MAML, prototypical networks, and neural architecture search all ride this promise, and AutoML industrializes it. But the theory is thin: generalization bounds across tasks need assumptions about task relatedness that are rarely stated, let alone verified. Negative transfer - where meta-training hurts the new task - is common and poorly predicted. NAS famously found architectures no better than random search under fair evaluation (Li and Talwalkar, 2020). The field automates the search while the question of when the search is worth running remains unanswered.",
 "why_it_matters": "AutoML sells automation of the modeler's judgment. If meta-learning only helps when tasks are already similar - the case needing it least - the automation is a very expensive way to rediscover the obvious.",
 "sig_lens": "The Signature lens reads meta-learning as apprenticeship: the apprentice learns only if the master tasks resemble the journeyman work, and the resemblance must be measured, not assumed.",
 "sig_solution": LABEL + " Assumptions: (1) task relatedness is the load-bearing assumption and is usually unstated; (2) negative transfer is underreported. Reasoning path: measure task relatedness explicitly before meta-training, and license few-shot claims only where the measurement supports them. Proposed mechanism: an apprenticeship protocol that computes task-similarity diagnostics on the meta-training set, predicts transfer benefit per new task, and requires the prediction to clear a bar before meta-learned priors may be used - with negative-transfer monitoring in production. Confirm: protocol-guided meta-learning beats blind meta-learning on cost-adjusted performance. Kill: relatedness proves unmeasurable in practice and the diagnostics are noise. Does NOT claim: a theory of when learning-to-learn works - it measures the apprenticeship fit.",
 "pointer": "The Signature system's proposed approach measures task relatedness before licensing meta-learned priors; the companion Signature Edition record specifies the apprenticeship protocol.",
 "key_points": [
  "Meta-learning theory needs task-relatedness assumptions that go unstated.",
  "Negative transfer is common and poorly predicted.",
  "NAS has matched random search under fair evaluation.",
  "The value case for meta-learning remains theoretically unmapped.",
 ],
 "requirements": [
  "Task-similarity diagnostics on every meta-training set.",
  "Per-task transfer-benefit predictions with a clearance bar.",
  "Negative-transfer monitoring in production.",
 ],
 "citations": [
  "Finn C et al. (2017) Model-agnostic meta-learning. ICML.",
  "Li L, Talwalkar A (2020) Random search and reproducibility for neural architecture search. UAI.",
 ],
 "demo": {"probs": [0.5, 0.22, 0.16, 0.12], "qpert": [0.42, 0.25, 0.18, 0.15]},
},
# ----------------------------------------------------------------- rank 30
{
 "key": "ds-streaming-bounds",
 "name": "The Streaming Memory Lower Bound Problem",
 "group": "Data Engineering",
 "ladder_rank": 30, "ladder_tier": "advanced",
 "problem": "When data arrives as an endless stream that cannot be stored, what can and cannot be computed in one pass with limited memory - and are the limits fundamental or just undiscovered algorithms?",
 "background": "Streaming algorithms process massive flows in sublinear memory: counting distinct elements (Flajolet-Martin, HyperLogLog), frequency moments, quantiles. The theory is rich with lower bounds - Alon, Matias and Szegedy (1999) proved linear memory is needed for exact frequency moments, forcing approximation. But the map has blank regions: optimal tradeoffs for many problems are unknown, multi-pass versus one-pass gaps are uncharted, and the adversarial-robustness of streaming sketches (an adaptive adversary observing outputs) was only recently formalized. Practitioners pick sketches by folklore; the theory cannot yet tell them what is impossible versus merely unknown.",
 "why_it_matters": "Network monitoring, ad-tech, and sensor networks all run on streams too big to store. Choosing a sketch without knowing the lower bounds is gambling memory against accuracy blind.",
 "sig_lens": "The Signature lens reads streaming as triage under fire: with memory for a thimble and a river incoming, the protocol must decide what is worth keeping before the water arrives.",
 "sig_solution": LABEL + " Assumptions: (1) lower bounds are the honest map of the impossible; (2) practitioners choose sketches by folklore. Reasoning path: compile the known lower bounds into a decision atlas per problem, and require sketch selection to cite the bound it operates under. Proposed mechanism: a triage-atlas protocol that documents, for each streaming task, the best known lower bound, the best known algorithm, and the gap between them - flagged as open or closed - so engineers choose sketches against the frontier, not folklore. Confirm: atlas-guided selection reduces memory waste on solved problems. Kill: the atlas goes stale as theory advances and misleads. Does NOT claim: new lower bounds - it organizes the known frontier for engineers.",
 "pointer": "The Signature system's proposed approach compiles streaming lower bounds into an engineer-facing decision atlas; the companion Signature Edition record specifies the triage-atlas protocol.",
 "key_points": [
  "Exact frequency moments need linear memory - approximation is forced, not optional.",
  "Optimal memory-accuracy tradeoffs are unknown for many streaming problems.",
  "Adversarial robustness of sketches was only recently formalized.",
  "Sketch selection in practice runs on folklore, not frontier knowledge.",
 ],
 "requirements": [
  "Per-task documentation of the best known lower bound and best known algorithm.",
  "Open-versus-closed gap flags on every bound.",
  "Sketch selection citing the bound it operates under.",
 ],
 "citations": [
  "Alon N, Matias Y, Szegedy M (1999) The space complexity of approximating the frequency moments. JCSS 58(1).",
 ],
 "demo": {"probs": [0.42, 0.28, 0.18, 0.12], "qpert": [0.36, 0.28, 0.2, 0.16]},
},
# ----------------------------------------------------------------- rank 31
{
 "key": "ds-anomaly-guarantees",
 "name": "The Anomaly Detection Guarantee Problem",
 "group": "Machine Learning",
 "ladder_rank": 31, "ladder_tier": "advanced",
 "problem": "Anomaly detection hunts the unknown unknowns - but without labeled anomalies, what can any method actually guarantee about what it will catch?",
 "background": "Fraud, intrusion, and failure detection all face the same void: anomalies are rare, diverse, and unlabeled by definition - if you could label them reliably, you would just classify. The field offers one-class SVMs, isolation forests, autoencoder reconstruction, and deep variants, each with implicit assumptions about what normal looks like. The guarantees are nearly nonexistent: without assumptions on the anomaly distribution, no method can promise detection rates, and the assumptions that would license guarantees (known anomaly families) contradict the premise of hunting unknowns. Evaluation is circular - benchmarks inject synthetic anomalies that match somebody's method. Practitioners tune thresholds on vibes.",
 "why_it_matters": "Security and safety depend on catching what has never been seen. A detector with no guarantees is a scarecrow: it may work, and nobody can say why or when it stops.",
 "sig_lens": "The Signature lens reads anomaly detection as a watchtower: the watchman cannot promise to see every intruder, but must report exactly which approaches are visible from the tower.",
 "sig_solution": LABEL + " Assumptions: (1) guarantee-free detection is the honest baseline; (2) every method sees some anomaly families and is blind to others. Reasoning path: characterize each detector's visibility - which anomaly families it provably or empirically catches - and report coverage, not just precision on synthetic benchmarks. Proposed mechanism: a watchtower protocol that stress-tests detectors against a battery of anomaly families (point, contextual, collective, adversarial), publishes the visibility map, and requires deployment to state which families are covered and which are blind spots. Confirm: visibility-mapped deployments catch more real incidents. Kill: real anomalies fall outside every battery family and the map is decorative. Does NOT claim: detection of true unknown unknowns - it maps the visible approaches.",
 "pointer": "The Signature system's proposed approach publishes each detector's anomaly-family visibility map; the companion Signature Edition record specifies the watchtower protocol.",
 "key_points": [
  "Anomalies are unlabeled by definition; supervised guarantees are unavailable.",
  "Every method assumes a shape of normal and is blind outside it.",
  "Benchmarks with synthetic anomalies are circular.",
  "Thresholds are tuned without principled guidance.",
 ],
 "requirements": [
  "Stress batteries across anomaly families (point, contextual, collective, adversarial).",
  "Published visibility maps per detector.",
  "Deployment statements of covered families and known blind spots.",
 ],
 "citations": [
  "Chandola V, Banerjee A, Kumar V (2009) Anomaly detection: a survey. ACM Computing Surveys 41(3).",
 ],
 "demo": {"probs": [0.58, 0.2, 0.12, 0.1], "qpert": [0.49, 0.23, 0.15, 0.13]},
},
# ----------------------------------------------------------------- rank 32
{
 "key": "ds-data-valuation",
 "name": "The Data Valuation Problem",
 "group": "Statistics",
 "ladder_rank": 32, "ladder_tier": "advanced",
 "problem": "When a model is trained on data from many sources, how much is each source's data actually worth - and can the value be computed fairly?",
 "background": "Data has value but no price tag: the Shapley value from cooperative game theory offers the principled attribution - each point's marginal contribution averaged over all subsets - and Ghorbani and Zou (2019, Data Shapley) brought it to ML. The catch is computation: exact Shapley needs exponentially many retrainings, and approximations (TMC-Shapley, KNN-Shapley) trade accuracy for feasibility with poorly understood error. Deeper problems persist: value depends on the model and task, not just the data; correlated sources split credit arbitrarily; and strategic data providers can game the valuation. Data markets and federated compensation schemes need these numbers, but the numbers remain approximate, manipulable, and model-dependent.",
 "why_it_matters": "Compensation, data markets, and cleaning priorities all need data prices. Without fair valuation, contributors are underpaid, markets misallocate, and the most valuable data - the rare, hard cases - goes unrewarded.",
 "sig_lens": "The Signature lens reads data value as wages: every contributor deserves paystub accounting - what their data earned, computed transparently, auditable line by line.",
 "sig_solution": LABEL + " Assumptions: (1) exact Shapley is intractable; approximations carry unquantified error; (2) value is model- and task-relative, not intrinsic. Reasoning path: standardize approximate valuation with error bars and make the attribution auditable - every data paycheck shows its computation. Proposed mechanism: a paystub protocol requiring valuation reports to state the approximation method, its error bounds, the model and task the value is relative to, and a dispute procedure for contributors; payments clear only on audited paystubs. Confirm: audited valuations correlate with held-out marginal value better than unaudited ones. Kill: approximation error dominates and paystubs mislead. Does NOT claim: the true intrinsic value of data - it standardizes the accounting.",
 "pointer": "The Signature system's proposed approach issues auditable data-valuation paystubs with error bounds; the companion Signature Edition record specifies the paystub protocol.",
 "key_points": [
  "Shapley values give the principled attribution but need exponential computation.",
  "Approximations trade accuracy for feasibility with poorly understood error.",
  "Value is relative to model and task, not an intrinsic property of data.",
  "Correlated sources and strategic providers complicate fair attribution.",
 ],
 "requirements": [
  "Valuation reports stating method, error bounds, and the model/task context.",
  "Auditable computation trails per valuation.",
  "Dispute procedures for contributing sources.",
 ],
 "citations": [
  "Ghorbani A, Zou J (2019) Data Shapley: equitable valuation of data. ICML.",
 ],
 "demo": {"probs": [0.46, 0.26, 0.16, 0.12], "qpert": [0.39, 0.27, 0.18, 0.16]},
},
# ----------------------------------------------------------------- rank 33
{
 "key": "ds-metric-geometry",
 "name": "The Metric Learning Geometry Problem",
 "group": "Machine Learning",
 "ladder_rank": 33, "ladder_tier": "advanced",
 "problem": "What is the right notion of distance for a given task - and can it be learned from data without collapsing into trivial or overfit geometries?",
 "background": "Nearest neighbors, clustering, and retrieval all depend on the metric, and the wrong metric makes similar things distant: Euclidean distance on raw pixels is famously meaningless. Metric learning (Weinberger and Saul, LMNN, 2009; deep variants like triplet and contrastive losses) learns embeddings where task-similar points are near. But learned metrics overfit their training pairs, collapse dimensions silently, and transfer poorly; the geometry that serves one task distorts another. The fundamental question - what geometric structure the data actually has versus what the loss imposes - is unanswered. Practitioners tune embedding dimensions and margins by validation, which measures the symptom, not the geometry.",
 "why_it_matters": "Search, recommendation, and face recognition are metric systems: their entire behavior is the geometry. A collapsed or overfit metric does not degrade gracefully - it reorganizes the world wrongly and confidently.",
 "sig_lens": "The Signature lens reads metrics as maps: a good map preserves the territory's real distances, and the cartographer must survey before drawing.",
 "sig_solution": LABEL + " Assumptions: (1) the loss imposes geometry as much as it discovers it; (2) collapsed dimensions are silent failures. Reasoning path: survey the learned geometry directly - measure effective rank, neighborhood preservation, and cross-task transfer - and certify metrics on the survey, not the loss. Proposed mechanism: a cartography protocol that audits every learned metric for dimensional collapse, neighborhood fidelity on held-out pairs, and transfer to adjacent tasks, with collapse alarms that block deployment. Confirm: surveyed metrics transfer better and collapse less in production. Kill: the survey metrics themselves overfit and certify bad geometries. Does NOT claim: discovery of the data's true geometry - it audits the map against the territory.",
 "pointer": "The Signature system's proposed approach surveys learned metrics for collapse and fidelity before deployment; the companion Signature Edition record specifies the cartography protocol.",
 "key_points": [
  "Euclidean distance on raw features is often meaningless for the task.",
  "Learned metrics overfit training pairs and collapse dimensions silently.",
  "Task-serving geometry may distort other tasks sharing the embedding.",
  "Validation measures symptoms; the geometry itself goes unaudited.",
 ],
 "requirements": [
  "Effective-rank and collapse audits on every learned metric.",
  "Neighborhood-fidelity measurement on held-out pairs.",
  "Cross-task transfer checks before shared embeddings ship.",
 ],
 "citations": [
  "Weinberger KQ, Saul LK (2009) Distance metric learning for large margin nearest neighbor classification. JMLR 10: 207-244.",
 ],
 "demo": {"probs": [0.4, 0.3, 0.18, 0.12], "qpert": [0.34, 0.3, 0.2, 0.16]},
},
# ----------------------------------------------------------------- rank 34
{
 "key": "ds-unified-theory",
 "name": "The Unified Theory of Data Science Problem",
 "group": "Statistics",
 "ladder_rank": 34, "ladder_tier": "advanced",
 "problem": "Is there a single theoretical framework that unifies statistical inference, machine learning, and causal reasoning - or are they permanently separate disciplines sharing only tools?",
 "background": "Data science lives in three houses: statistics (inference under uncertainty), machine learning (prediction at scale), and causal inference (interventions and mechanisms) - with information theory, optimization, and computation as shared utilities. Breiman's two cultures (2001) diagnosed the statistics-ML split; the causality community maintains its own separate foundations. Attempts at unification - statistical learning theory, PAC-Bayes, decision-theoretic frameworks - cover prediction and inference but leave causation as an add-on. A true unification would derive when prediction suffices, when inference is needed, and when only causal knowledge will do, from common principles. No such framework exists, and it is unclear whether the divisions reflect deep mathematical necessity or historical accident.",
 "why_it_matters": "A fractured field gives fractured answers: prediction tools misapplied to causal questions, inference rituals misapplied to prediction. Unification would tell practitioners which house to enter for which question - the most practical theory imaginable.",
 "sig_lens": "The Signature lens reads the three houses as one building with three doors: the unification is not a new theory but a map showing which door each question enters through.",
 "sig_solution": LABEL + " Assumptions: (1) the divisions may reflect deep necessity, not just history; (2) practitioners need guidance, not philosophy. Reasoning path: build the map first - a decision framework that routes each question type (predict, infer, intervene) to the right formalism with its assumptions priced - and let the map reveal where the formalisms truly connect. Proposed mechanism: a three-doors protocol that classifies every data science question by its decision target, routes it to the appropriate framework with assumption licenses attached, and maintains a living atlas of the boundary cases where frameworks overlap or conflict. Confirm: routed projects choose appropriate methods more reliably. Kill: the boundaries prove illusory and the map misroutes. Does NOT claim: a single mathematical unification - it maps the building while theorists debate the architecture.",
 "pointer": "The Signature system's proposed approach maps every question to its proper framework with priced assumptions; the companion Signature Edition record specifies the three-doors protocol.",
 "key_points": [
  "Statistics, machine learning, and causal inference maintain separate foundations.",
  "Breiman two cultures diagnosed the split; unification attempts remain partial.",
  "Causation resists absorption into prediction-or-inference frameworks.",
  "Practitioners misapply tools across the divides constantly.",
 ],
 "requirements": [
  "Question classification by decision target (predict, infer, intervene).",
  "Assumption licenses attached at every framework routing.",
  "A living atlas of boundary cases where frameworks overlap or conflict.",
 ],
 "citations": [
  "Breiman L (2001) Statistical modeling: the two cultures. Statistical Science 16(3): 199-231.",
 ],
 "demo": {"probs": [0.5, 0.25, 0.15, 0.1], "qpert": [0.42, 0.26, 0.18, 0.14]},
},
]
