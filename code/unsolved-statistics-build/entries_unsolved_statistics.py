#!/usr/bin/env python3
"""Entries for the Unsolved Statistics databases (Manon's 16:15 orders, batch 1).

34 famous open problems in statistics, ladder-ordered by accessibility
(rank 1 = most approachable, rank 34 = most complex). Public half carries
the real fact-checked problem record plus a short pointer to the Signature
approach; Signature half carries the full Signature-generated proposed
solution, always labeled and never presented as established science.

ID prefixes: JAH-USST- (public) and JAH-USSTS- (signature), verified free
(zero hits in the manifest id_prefix values and zero hits across all shard
index files in jah-databases-data-1, 2026-10-17).

Numerical cores: all hand-computed 2026-10-17, machine-verified by the
demos (see demos_unsolved_statistics.py). Every demo prints its real
computed values, asserts tight bounds (never float exact-equality), and
ends with the OK marker; the build machine-executes all 68 demos.

Honesty rule: the signature_solution opens with the exact label
"Signature-generated proposed solution — not established science" and
never claims proof, peer acceptance, or settled status.

No website references. No Facebook. No religious talk. Nothing
hate-adjacent, profane, or inappropriate.
"""

SIG_TAIL = ("Signature original - his original Signature solution method: every "
            "unsolved problem approached as a covenant between the known and the "
            "unknown, the proposed path walked step by step with its assumptions "
            "declared, its confirm and refute conditions stated, and its limits "
            "honestly marked. Clearly labeled Signature-made, never presented as "
            "established science or authentic public record.")

CIT_HUME = ("Hume D. An Enquiry Concerning Human Understanding. London; 1748.")
CIT_GOODMAN = ("Goodman N. Fact, Fiction, and Forecast. Harvard University Press; 1955.")
CIT_HACKING = ("Hacking I. An Introduction to Probability and Inductive Logic. "
               "Cambridge University Press; 2001.")
CIT_GILLIES = ("Gillies D. Philosophical Theories of Probability. Routledge; 2000.")
CIT_KOLMOGOROV = ("Kolmogorov AN. Foundations of the Theory of Probability. 1933.")
CIT_NEYMAN = ("Neyman J. Outline of a theory of statistical estimation based on the classical "
              "theory of probability. Philosophical Transactions of the Royal Society; 1937.")
CIT_MOREY = ("Morey RD, Hoekstra R, Rouder JN, Lee MD, Wagenmakers EJ. The fallacy of placing "
             "confidence in confidence intervals. Psychonomic Bulletin and Review; 2016.")
CIT_OSC = ("Open Science Collaboration. Estimating the reproducibility of psychological science. "
           "Science; 2015.")
CIT_IOANNIDIS = ("Ioannidis JPA. Why most published research findings are false. "
                 "PLoS Medicine; 2005.")
CIT_ASA16 = ("Wasserstein RL, Lazar NA. The ASA Statement on p-Values: Context, Process, and "
             "Purpose. The American Statistician; 2016.")
CIT_ASA19 = ("Wasserstein RL, Schirm AL, Lazar NA. Moving to a World Beyond p < 0.05. "
             "The American Statistician; 2019.")
CIT_SIMMONS = ("Simmons JP, Nelson LD, Simonsohn U. False-positive psychology: undisclosed "
               "flexibility in data collection and analysis allows presenting anything as "
               "significant. Psychological Science; 2011.")
CIT_FISHER = ("Fisher RA. Statistical Methods for Research Workers. Oliver and Boyd; 1925.")
CIT_BH = ("Benjamini Y, Hochberg Y. Controlling the false discovery rate: a practical and "
          "powerful approach to multiple testing. Journal of the Royal Statistical Society B; 1995.")
CIT_BIRNBAUM = ("Birnbaum A. On the foundations of statistical inference. Journal of the "
                "American Statistical Association; 1962.")
CIT_ARMITAGE = ("Armitage P, McPherson CK, Rowe BC. Repeated significance tests on accumulating "
                "data. Journal of the Royal Statistical Society A; 1969.")
CIT_AKAIKE = ("Akaike H. A new look at the statistical model identification. IEEE Transactions "
              "on Automatic Control; 1974.")
CIT_SCHWARZ = ("Schwarz G. Estimating the dimension of a model. Annals of Statistics; 1978.")
CIT_YANG = ("Yang Y. Can the strengths of AIC and BIC be shared? A conflict between model "
            "identification and regression estimation. Biometrika; 2005.")
CIT_HUBER = ("Huber PJ. The behavior of maximum likelihood estimates under nonstandard "
             "conditions. Proceedings of the Fifth Berkeley Symposium; 1967.")
CIT_WHITE = ("White H. Maximum likelihood estimation of misspecified models. "
             "Econometrica; 1982.")
CIT_BERK = ("Berk R, Brown L, Buja A, Zhang K, Zhao L. Valid post-selection inference. "
            "Annals of Statistics; 2013.")
CIT_LEE = ("Lee JD, Sun DL, Sun Y, Taylor JE. Exact post-selection inference, with application "
           "to the lasso. Annals of Statistics; 2016.")
CIT_BRT = ("Bickel PJ, Ritov Y, Tsybakov AB. Simultaneous analysis of Lasso and Dantzig "
           "selector. Annals of Statistics; 2009.")
CIT_ZZ = ("Zhang CH, Zhang SS. Confidence intervals for low dimensional parameters in high "
          "dimensional linear models. Journal of the Royal Statistical Society B; 2014.")
CIT_ANDREWS = ("Andrews DWK. Inconsistency of the bootstrap when a parameter is on the boundary "
               "of the parameter space. Econometrica; 2000.")
CIT_BF = ("Bickel PJ, Freedman DA. Some asymptotic theory for the bootstrap. Annals of "
          "Statistics; 1981.")
CIT_EFRON = ("Efron B. Bootstrap methods: another look at the jackknife. Annals of "
             "Statistics; 1979.")
CIT_PEARL = ("Pearl J. Causality: Models, Reasoning, and Inference. 2nd ed. Cambridge "
             "University Press; 2009.")
CIT_RUBIN74 = ("Rubin DB. Estimating causal effects of treatments in randomized and "
               "nonrandomized studies. Journal of Educational Psychology; 1974.")
CIT_ROSENBAUM = ("Rosenbaum PR. Observational Studies. 2nd ed. Springer; 2002.")
CIT_CHICKERING = ("Chickering DM. Learning Bayesian networks is NP-hard. Proceedings of "
                  "AAAI; 1996.")
CIT_SPIRTES = ("Spirtes P, Glymour C, Scheines R. Causation, Prediction, and Search. "
               "2nd ed. MIT Press; 2000.")
CIT_PB = ("Pearl J, Bareinboim E. Transportability of causal and statistical relations: a "
          "formal approach. Proceedings of AAAI; 2011.")
CIT_HH = ("Hudgens MG, Halloran ME. Toward causal inference with interference. Journal of "
          "the American Statistical Association; 2008.")
CIT_RUBIN76 = ("Rubin DB. Inference and missing data. Biometrika; 1976.")
CIT_VOVK = ("Vovk V, Gammerman A, Shafer G. Algorithmic Learning in a Random World. "
            "Springer; 2005.")
CIT_BARBER = ("Barber RF, Candes EJ, Ramdas A, Tibshirani RJ. The limits of distribution-free "
              "conditional predictive inference. Information and Inference; 2021.")
CIT_DWORK15 = ("Dwork C, Feldman V, Hardt M, Pitassi T, Reingold O, Roth A. The reusable "
               "holdout: preserving validity in adaptive data analysis. Science; 2015.")
CIT_DWORKROTH = ("Dwork C, Roth A. The Algorithmic Foundations of Differential Privacy. "
                 "Foundations and Trends in Theoretical Computer Science; 2014.")
CIT_BERNARDO = ("Bernardo JM. Reference posterior distributions for Bayesian inference. "
                "Journal of the Royal Statistical Society B; 1979.")
CIT_GRUENWALD = ("Gruenwald P, de Heide R, Koolen W. Safe testing. Journal of the Royal "
                 "Statistical Society B; 2024.")
CIT_BISSIRI = ("Bissiri PG, Holmes CC, Walker SG. A general framework for updating belief: "
                "Bayesian and otherwise. Journal of the Royal Statistical Society B; 2016.")
CIT_GINENICKL = ("Gine E, Nickl R. Mathematical Foundations of Infinite-Dimensional "
                 "Statistical Models. Cambridge University Press; 2016.")
CIT_PETERS = ("Peters O. The ergodicity problem in economics. Nature Physics; 2019.")
CIT_WALLEY = ("Walley P. Statistical Reasoning with Imprecise Probabilities. Chapman and "
              "Hall; 1991.")
CIT_XIESINGH = ("Xie M, Singh K. Confidence distribution, the frequentist distribution "
                "estimator of a parameter: a review. International Statistical Review; 2013.")
CIT_TIBSHIRANI = ("Tibshirani R. Regression shrinkage and selection via the lasso. Journal of "
                  "the Royal Statistical Society B; 1996.")
CIT_BLUME = ("Blume JD, DAgostino McGowan L, Dupont WD, Greevy RA. Second-generation "
             "p-values. The American Statistician; 2018.")

LABEL = "Signature-generated proposed solution \u2014 not established science."

ENTRIES = [
    {
        "key": "induction",
        "name": "The Problem of Induction in Statistics",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "problem": ("Every statistical inference extrapolates from observed data to unobserved "
                    "cases: from a sample to a population, from the past to the future. David Hume "
                    "showed there is no non-circular logical justification for assuming the future "
                    "will resemble the past. The problem is open: what, if anything, warrants "
                    "inductive statistical inference?"),
        "background": ("Hume posed the problem in 1739 in A Treatise of Human Nature and sharpened it "
                       "in the 1748 Enquiry: no deductive argument proves nature is uniform, and any "
                       "inductive defense of induction begs the question. Every confidence interval, "
                       "posterior, and prediction interval silently assumes the data-generating process "
                       "stays put. Reichenbach offered a pragmatic vindication: if any method works, "
                       "induction works. Popper tried to sidestep induction with falsification, but "
                       "statistical practice still bets on the future resembling the past. Modern "
                       "responses include Bayesian coherence arguments and formal learning theory, yet "
                       "none has produced a justification all parties accept, and working statisticians "
                       "simply assume stability while knowing the assumption is the load-bearing wall."),
        "why_it_matters": ("If induction has no foundation, then every generalization from data rests on "
                           "an article of faith, and understanding the gap tells us where statistical "
                           "claims are fragile. Regime change, distribution shift, and black-swan events "
                           "are exactly the places the unjustified assumption bites. A real answer would "
                           "tell us which extrapolations are licensed and which are wishful thinking."),
        "pointer": ("The Signature system proposes a labeled approach to this open problem - see the "
                    "companion Signature Edition record for the full step-by-step walkthrough. The "
                    "problem itself remains open in established science; no solution is claimed."),
        "sig_lens": ("The Signature lens reads induction as a covenant problem: the data promise that "
                     "tomorrow behaves like today, and the Signature approach makes that promise "
                     "checkable by turning stability itself into a monitored, testable claim instead of "
                     "a silent background assumption."),
        "sig_solution": (
            LABEL + " Approach S-01: monitored-stability induction. "
            "Assumptions: (A1) the data-generating process is piecewise stable with detectable change "
            "points rather than adversarially shifting at every step; (A2) a stability monitor - a "
            "sequential test for distribution change - runs alongside every inference; (A3) inferences "
            "are issued with an explicit stability certificate whose strength decays as the monitor "
            "accumulates evidence of drift. "
            "Reasoning path: (S1) replace the silent uniformity assumption with an explicit, testable "
            "stability hypothesis; (S2) attach to every estimate a sequential change-detection monitor "
            "with anytime-valid guarantees; (S3) when the monitor fires, the inference is withdrawn or "
            "re-based instead of silently extrapolating; (S4) grade every historical success of induction "
            "by the monitor record, building an empirical track record of when stability held. "
            "Proposed mechanism: induction becomes a standing bet with a tripwire - the method does not "
            "justify uniformity, it watches for its failure and stops betting when the tripwire trips. "
            "What would confirm it: monitored procedures that detect real regime changes faster than "
            "unmonitored ones while rarely crying wolf, across many domains. What would kill it: proof "
            "that change points are undetectable before they corrupt inference, or monitors that fire "
            "constantly and make every inference useless. "
            "What it does NOT claim: a logical justification of induction, an answer to Hume, or peer "
            "acceptance. Hume stands undefeated; this is a proposed engineering discipline for living "
            "with his result, honestly labeled."),
        "key_points": [
            "Hume 1739/1748: no non-circular justification for assuming the future resembles the past.",
            "All statistical generalization - samples to populations, past to future - assumes uniformity of nature.",
            "Reichenbach pragmatic vindication and Popper falsificationism never closed the logical gap.",
            "This walkthrough simulates a regime change and shows past data going blind at the change point.",
            "Distribution shift and black swans are where the unjustified assumption does its damage.",
        ],
        "requirements": [
            "Any claimed solution must answer Hume without circular appeal to past success of induction.",
            "A practical proposal must say exactly which extrapolations it licenses and which it refuses.",
            "Change-detection machinery must be validated on real regime changes, not toy simulations.",
            "Philosophical acceptance requires surviving scrutiny from Bayesians, frequentists, and skeptics alike.",
        ],
        "standards": [
            "Hume D. An Enquiry Concerning Human Understanding; 1748.",
            "Standard: a proposed justification must not assume in its premises what induction is meant to prove.",
            "Standard: practical methods must state their stability assumptions explicitly and monitor them.",
        ],
        "citations": [CIT_HUME, CIT_GOODMAN, CIT_HACKING],
    },
    {
        "key": "prob_interpretations",
        "name": "Interpretations of Probability",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "problem": ("Kolmogorov 1933 axioms tell us how probabilities compute, not what they mean. "
                    "Is a probability a long-run frequency, a degree of belief, a physical propensity, "
                    "or a logical relation? After a century of debate there is still no consensus, and "
                    "the choice changes what statistical statements are even allowed to say."),
        "background": ("The classical interpretation of Laplace gave way to frequentism in Venn, von "
                       "Mises, and Reichenbach: probability as limiting relative frequency in a repeatable "
                       "collective. Ramsey, de Finetti, and Savage countered with subjective Bayesianism: "
                       "probability as coherent degree of belief, updated by Bayes rule. Popper proposed "
                       "propensities as physical dispositions of experimental setups; Keynes and Carnap "
                       "defended logical probability as partial entailment. Each interpretation struggles "
                       "somewhere: frequentism with single cases, subjectivism with objectivity, propensity "
                       "with Humphreys paradox, logical probability with a workable confirmation theory. "
                       "Working statisticians mostly compute first and interpret later, which is why two "
                       "analysts can agree on every number and disagree on what any of them mean."),
        "why_it_matters": ("The interpretation decides which questions are meaningful: a frequentist cannot "
                           "say the probability this hypothesis is true is 0.9, a subjectivist cannot point "
                           "to a physical frequency. Courts, medicine, and policy all consume single-case "
                           "probabilities that frequentism officially cannot supply. Settling the meaning "
                           "would settle what statistics is allowed to promise."),
        "pointer": ("The Signature system proposes a labeled approach to this open problem - see the "
                    "companion Signature Edition record for the full step-by-step walkthrough. The "
                    "problem itself remains open in established science; no solution is claimed."),
        "sig_lens": ("The Signature lens reads the interpretation debate as a translation problem: every "
                     "camp computes nearly the same numbers on real data, so the Signature approach builds "
                     "an explicit translation table between interpretations and marks exactly where the "
                     "translations break down."),
        "sig_solution": (
            LABEL + " Approach S-02: interpretation-translation discipline. "
            "Assumptions: (A1) on real data, frequentist, Bayesian, and propensity computations usually "
            "agree numerically to within modeling noise; (A2) the disagreements live in the semantics "
            "attached to the numbers, not the numbers; (A3) each interpretation can be formalized as a "
            "mapping from the same evidence to statements with explicit truth conditions. "
            "Reasoning path: (S1) for a given analysis, compute the frequentist estimate, the Bayesian "
            "posterior, and the propensity reading side by side; (S2) write the translation table: what "
            "each camp may and may not assert from the same numbers; (S3) flag the exact claims where "
            "translations fail, such as single-case probability under strict frequentism; (S4) let the "
            "decision context choose the interpretation whose licensed claims match the question asked. "
            "Proposed mechanism: stop asking which interpretation is true and start requiring every "
            "analysis to carry its interpretation license - the list of claims its numbers are allowed "
            "to support. "
            "What would confirm it: decision-makers making fewer interpretation errors when analyses ship "
            "with explicit licenses. What would kill it: cases where the camps compute irreconcilably "
            "different numbers from the same evidence, breaking the translation premise. "
            "What it does NOT claim: a true interpretation of probability, a philosophical consensus, or "
            "peer acceptance. The century-old debate stays open; this is a proposed working discipline, "
            "honestly labeled."),
        "key_points": [
            "Kolmogorov 1933 axiomatized the mathematics of probability, not its meaning.",
            "Rival camps: frequentist, subjective Bayesian, propensity, logical - none commands consensus.",
            "Single-case probabilities embarrass strict frequentism; objectivity embarrasses subjectivism.",
            "This walkthrough computes frequentist and Bayesian answers on the same coin data: the numbers agree, the licenses differ.",
            "The interpretation you choose decides which sentences you are allowed to utter.",
        ],
        "requirements": [
            "Any claimed resolution must handle single-case probability, the hardest test case.",
            "It must explain why the camps agree numerically so often despite disagreeing semantically.",
            "It must survive Humphreys paradox and the reference-class problem, not dodge them.",
            "Philosophical acceptance requires engaging a century of literature, not redefining terms.",
        ],
        "standards": [
            "Kolmogorov AN. Foundations of the Theory of Probability; 1933.",
            "Standard: interpretations are judged by the claims they license, tested on single cases.",
            "Standard: numerical agreement across camps on real data is the datum any theory must explain.",
        ],
        "citations": [CIT_KOLMOGOROV, CIT_HACKING, CIT_GILLIES],
    },
    {
        "key": "confidence_meaning",
        "name": "What a 95 Percent Confidence Interval Really Means",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "problem": ("A 95 percent confidence interval is routinely read as there being a 95 percent "
                    "chance the true parameter lies inside it. That reading is wrong under the "
                    "frequentist definition Neyman gave in 1937, yet the misreading persists in "
                    "textbooks, papers, and software output. The open problem: what should a "
                    "confidence interval mean, and how should uncertainty be communicated so people "
                    "stop misunderstanding it?"),
        "background": ("Neyman 1937 defined the confidence interval as a procedure: in repeated use, "
                       "95 percent of the intervals constructed will cover the true fixed parameter. "
                       "Any single realized interval either covers it or does not; no probability "
                       "attaches. Fisher objected that scientists want to say something about this "
                       "interval, not about long-run procedure behavior, and the fiducial argument he "
                       "offered instead never won consensus. Morey and colleagues in 2016 documented "
                       "that even researchers endorse the fallacious reading. Bayesian credible "
                       "intervals give the reading people want but require a prior. Confidence "
                       "distributions and generalized fiducial inference try to rebuild the bridge, "
                       "but no proposal has displaced the misunderstood standard."),
        "why_it_matters": ("Confidence intervals are the most consumed uncertainty statement in "
                           "science, medicine, and policy. If the consumers systematically misread the "
                           "product, decisions rest on a fiction. A correct, teachable meaning for "
                           "interval estimates would repair one of the most widespread quantitative "
                           "misunderstandings in public life."),
        "pointer": ("The Signature system proposes a labeled approach to this open problem - see the "
                    "companion Signature Edition record for the full step-by-step walkthrough. The "
                    "problem itself remains open in established science; no solution is claimed."),
        "sig_lens": ("The Signature lens reads the confidence-interval mess as a labeling failure: the "
                     "procedure ships without its meaning attached, so users invent one. The Signature "
                     "approach attaches an explicit meaning label to every interval and refuses to "
                     "report intervals whose meaning the audience cannot state back."),
        "sig_solution": (
            LABEL + " Approach S-03: meaning-labeled intervals. "
            "Assumptions: (A1) the misreading is caused by missing semantics, not by user innumeracy; "
            "(A2) every interval method can be shipped with a one-sentence license stating exactly what "
            "its 95 percent refers to; (A3) audiences can learn the licensed reading when it is stated "
            "plainly and tested. "
            "Reasoning path: (S1) define three labeled products: the procedure interval (Neyman: 95 "
            "percent of such intervals cover), the belief interval (Bayesian: 95 percent posterior "
            "probability inside, prior declared), and the bet interval (what odds the analyst will "
            "actually lay); (S2) require software and papers to print the label with the numbers; "
            "(S3) run comprehension trials: readers must paraphrase the meaning correctly before the "
            "interval counts as communicated; (S4) track misreading rates by label over time. "
            "Proposed mechanism: a labeling standard plus comprehension testing, modeled on nutrition "
            "labels - the numbers stay, but the meaning becomes impossible to miss. "
            "What would confirm it: measured drops in the fallacious 95-percent-chance reading where "
            "labels are used. What would kill it: evidence that users misread even perfectly labeled "
            "intervals, implying the concept itself resists the desired reading. "
            "What it does NOT claim: a new definition of confidence, a philosophical resolution, or "
            "peer acceptance. Neyman stands as defined; this is a proposed communication discipline, "
            "honestly labeled."),
        "key_points": [
            "Neyman 1937: a 95 percent CI is a procedure that covers the true parameter in 95 percent of repetitions.",
            "The realized interval either covers the parameter or does not; no 95 percent attaches to it.",
            "Morey et al. 2016 documented the fallacious reading even among researchers.",
            "This walkthrough simulates 2000 intervals: coverage lands near 95 percent while any single interval is cover-or-not.",
            "Bayesian credible intervals give the wanted reading but demand a prior.",
        ],
        "requirements": [
            "Any proposal must keep the frequentist coverage guarantee intact while fixing the reading.",
            "Comprehension must be measured in trials, not asserted by experts.",
            "Software output is the main battlefield: labels must appear where numbers appear.",
            "The fix must work for non-statisticians, the actual consumers of intervals.",
        ],
        "standards": [
            "Neyman J. Outline of a theory of statistical estimation; 1937.",
            "Standard: the licensed meaning must be statable in one sentence and testable by paraphrase.",
            "Standard: interval methods are judged by both coverage and communicated meaning.",
        ],
        "citations": [CIT_NEYMAN, CIT_MOREY, CIT_XIESINGH],
    },
    {
        "key": "replication",
        "name": "The Replication Crisis in Statistics",
        "group": "Foundations",
        "ladder_rank": 4,
        "ladder_tier": "foundations",
        "problem": ("Large replication projects found that a large fraction of published findings do "
                    "not replicate: the Open Science Collaboration 2015 effort reproduced only about "
                    "36 to 39 percent of 100 psychology studies. Researcher degrees of freedom, "
                    "p-hacking, and publication bias mean the published literature is a selected "
                    "sample. The open problem: which statistical methods actually guarantee "
                    "replicable findings, and can the crisis be fixed methodologically at all?"),
        "background": ("Ioannidis argued in 2005 that most published findings are false under plausible "
                       "assumptions about bias and low prior odds. Simmons, Nelson, and Simonsohn showed "
                       "in 2011 that undisclosed flexibility in analysis lets researchers present anything "
                       "as significant. The Open Science Collaboration 2015 replication of 100 studies "
                       "put numbers on the damage: replication effect sizes averaged about half the "
                       "originals. The American Statistical Association responded in 2016 with its "
                       "statement on p-values, and in 2019 an editorial urged moving beyond p less than "
                       "0.05. Pre-registration and registered reports attack the flexibility; larger "
                       "samples and replication itself attack the noise. But no purely statistical fix "
                       "commands agreement, because the crisis is partly about incentives, and methods "
                       "cannot fix incentives alone."),
        "why_it_matters": ("Science is the input to medicine, policy, and technology. If the input is "
                           "unreliable, everything downstream inherits the unreliability. A methodological "
                           "fix that made findings actually replicate would be worth more than any single "
                           "discovery, because it would repair the discovery pipeline itself."),
        "pointer": ("The Signature system proposes a labeled approach to this open problem - see the "
                    "companion Signature Edition record for the full step-by-step walkthrough. The "
                    "problem itself remains open in established science; no solution is claimed."),
        "sig_lens": ("The Signature lens reads the replication crisis as a selection problem: the "
                     "literature is not a record of experiments, it is a record of experiments that "
                     "passed a filter. The Signature approach models the filter explicitly and "
                     "discounts every claim by the selection pressure that produced it."),
        "sig_solution": (
            LABEL + " Approach S-04: selection-discounted inference. "
            "Assumptions: (A1) published results are a selected sample, selected largely on "
            "statistical significance; (A2) the selection mechanism can be estimated from the "
            "literature itself via funnel asymmetry and p-curve shapes; (A3) a finding discounted "
            "for its estimated selection pressure is closer to the replicable truth. "
            "Reasoning path: (S1) for a literature, estimate the selection function from the joint "
            "distribution of effect sizes and standard errors; (S2) compute selection-adjusted effect "
            "estimates and intervals for each claim; (S3) validate the discounts prospectively: do "
            "discounted estimates predict actual replication outcomes better than raw ones; (S4) publish "
            "the discount alongside the claim so consumers see the replicability-graded version. "
            "Proposed mechanism: a selection model fitted to each literature, producing discounted "
            "estimates that forecast replication success. "
            "What would confirm it: discounted estimates systematically predicting replication outcomes "
            "across fields in preregistered tests. What would kill it: selection mechanisms too "
            "heterogeneous to estimate, or discounts that add noise without improving forecasts. "
            "What it does NOT claim: a cure for bad incentives, a replacement for actual replication, "
            "or peer acceptance. Selection modeling is hard and contested; this is a proposed path, "
            "honestly labeled."),
        "key_points": [
            "Open Science Collaboration 2015: only about 36 to 39 percent of 100 studies replicated.",
            "Ioannidis 2005: under plausible bias, most published findings are false.",
            "Simmons et al. 2011: undisclosed analytic flexibility can make anything significant.",
            "This walkthrough simulates p-hacked publication: published effects inflate, then shrink on replication.",
            "Pre-registration attacks flexibility; no purely statistical fix is agreed.",
        ],
        "requirements": [
            "Any fix must be validated against actual replication outcomes, not simulations alone.",
            "Selection models must be shown robust to misspecification of the selection mechanism.",
            "The proposal must separate the statistical problem from the incentive problem honestly.",
            "Adoption requires journals and funders, not just methods papers.",
        ],
        "standards": [
            "Open Science Collaboration. Estimating the reproducibility of psychological science; 2015.",
            "Standard: replicability claims are tested by preregistered replication, the ground truth.",
            "Standard: methods must report performance under selection, not just under random sampling.",
        ],
        "citations": [CIT_OSC, CIT_IOANNIDIS, CIT_SIMMONS, CIT_ASA16],
    },
    {
        "key": "pvalues",
        "name": "P-Values and the Search for a Replacement",
        "group": "Foundations",
        "ladder_rank": 5,
        "ladder_tier": "foundations",
        "problem": ("The p-value is the most used and most misused number in science. The American "
                    "Statistical Association 2016 statement listed six principles constraining its "
                    "proper use, and a 2019 editorial urged moving beyond p less than 0.05 entirely. "
                    "Yet no replacement - not Bayes factors, not e-values, not second-generation "
                    "p-values - has been adopted. The open problem: what should replace or repair the "
                    "p-value as the workhorse of applied inference?"),
        "background": ("Fisher 1925 popularized the p-value as a measure of evidence against a null; "
                       "Neyman and Pearson rebuilt it as a decision rule with error rates. Decades of "
                       "misuse followed: p-hacking, publication bias, the conflation of statistical and "
                       "practical significance. The ASA 2016 statement, authored by Wasserstein and "
                       "Lazar, laid down six principles, including that p-values do not measure the "
                       "probability the hypothesis is true. The 2019 special issue editorial went further, "
                       "recommending researchers stop using the term statistically significant. Proposed "
                       "successors each have costs: Bayes factors need priors, e-values need new habits, "
                       "second-generation p-values need an indifference zone scientists must specify. The "
                       "field agrees the status quo is broken and cannot agree on the fix."),
        "why_it_matters": ("Millions of scientific conclusions hinge on this one number. A better "
                           "workhorse - one that measures evidence honestly and resists gaming - would "
                           "upgrade every field that runs experiments. The choice of successor will shape "
                           "what counts as a discovery for a generation."),
        "pointer": ("The Signature system proposes a labeled approach to this open problem - see the "
                    "companion Signature Edition record for the full step-by-step walkthrough. The "
                    "problem itself remains open in established science; no solution is claimed."),
        "sig_lens": ("The Signature lens reads the p-value wars as a missing-specification problem: the "
                     "number is asked to do jobs it was never specified for. The Signature approach "
                     "splits the jobs - evidence measurement, error control, decision support - and "
                     "assigns each its own honestly labeled instrument."),
        "sig_solution": (
            LABEL + " Approach S-05: job-separated evidence instruments. "
            "Assumptions: (A1) no single number can serve evidence measurement, error control, and "
            "decision-making simultaneously without misuse; (A2) e-values can carry the "
            "anytime-valid evidence job; (A3) calibrated effect sizes with uncertainty carry the "
            "practical-significance job. "
            "Reasoning path: (S1) retire the p-value from evidence duty and keep it only where "
            "Neyman-Pearson error control is genuinely wanted; (S2) report e-values for evidence, "
            "with their betting interpretation made explicit; (S3) report effect sizes with "
            "compatibility intervals for practical importance; (S4) run head-to-head trials: do "
            "analysts using the separated instruments make fewer false discovery claims and better "
            "calibrated decisions. "
            "Proposed mechanism: a three-instrument reporting standard replacing the single p-value "
            "with labeled, job-specific numbers. "
            "What would confirm it: adoption trials showing fewer irreproducible claims and better "
            "calibration than p-value practice. What would kill it: analysts gaming the new "
            "instruments just as effectively, proving the problem is incentives all the way down. "
            "What it does NOT claim: that e-values or any successor are proven superior, that the "
            "field will adopt them, or peer acceptance. This is a proposed reporting discipline, "
            "honestly labeled."),
        "key_points": [
            "ASA 2016: six principles; p-values do not give the probability the hypothesis is true.",
            "2019 ASA editorial: retire the phrase statistically significant.",
            "Under the null, p-values are uniform - this walkthrough verifies the uniformity directly.",
            "Candidates to succeed it: Bayes factors, e-values, second-generation p-values; none adopted.",
            "The field agrees the status quo is broken and cannot agree on the fix.",
        ],
        "requirements": [
            "Any successor must be validated in real analyst behavior, not just theory.",
            "It must resist gaming at least as well as the p-value does, preferably better.",
            "It must be teachable to working scientists within existing training.",
            "Its operating characteristics under realistic misuse must be measured, not assumed.",
        ],
        "standards": [
            "Wasserstein RL, Lazar NA. The ASA Statement on p-Values; 2016.",
            "Standard: evidence measures are judged by calibration under both honest and adversarial use.",
            "Standard: proposals must state which job - evidence, error control, decision - each number serves.",
        ],
        "citations": [CIT_ASA16, CIT_ASA19, CIT_FISHER, CIT_GRUENWALD, CIT_BLUME],
    },
    {
        "key": "multiple_testing",
        "name": "Multiple Testing and the Multiplicity Burden",
        "group": "Foundations",
        "ladder_rank": 6,
        "ladder_tier": "foundations",
        "problem": ("Test enough hypotheses and some will look significant by chance alone. "
                    "Controlling the resulting flood of false positives without drowning real "
                    "discoveries is the multiplicity problem. Bonferroni is safe but powerless, "
                    "false discovery rate methods are powerful but rest on dependence assumptions, "
                    "and choosing the right error rate for the job remains an open judgment with "
                    "no universal answer."),
        "background": ("The problem is ancient in statistics but exploded with genomics, neuroimaging, "
                       "and large-scale A/B testing, where thousands or millions of tests run at once. "
                       "Bonferroni correction controls the family-wise error rate but becomes brutally "
                       "conservative as the number of tests grows. Benjamini and Hochberg 1995 "
                       "introduced the false discovery rate, controlling the expected fraction of false "
                       "findings among rejections - a breakthrough that powers modern high-throughput "
                       "science. But FDR procedures assume independence or specific dependence "
                       "structures, adaptive variants behave subtly, and the deeper question persists: "
                       "which error rate should a given investigation control, and who decides? Selective "
                       "inference and post-selection methods extend the battlefield, but the choice of "
                       "the right multiplicity adjustment for novel settings is still expert judgment, "
                       "not settled science."),
        "why_it_matters": ("Every genome-wide association study, every brain scan, every tech company "
                           "experimentation platform lives or dies by multiplicity control. Too strict and "
                           "real discoveries die unpublished; too loose and the literature fills with "
                           "noise. Getting the tradeoff right is worth billions in research efficiency."),
        "pointer": ("The Signature system proposes a labeled approach to this open problem - see the "
                    "companion Signature Edition record for the full step-by-step walkthrough. The "
                    "problem itself remains open in established science; no solution is claimed."),
        "sig_lens": ("The Signature lens reads multiplicity as a budget problem: the analyst has a "
                     "fixed allowance of false claims to spend across an investigation. The Signature "
                     "approach makes the budget explicit, spends it where discoveries matter most, and "
                     "reports the remaining balance."),
        "sig_solution": (
            LABEL + " Approach S-06: explicit error budgeting. "
            "Assumptions: (A1) every investigation can state its tolerable false-claim budget up front; "
            "(A2) hypotheses can be ranked by scientific importance before seeing the data; (A3) "
            "weighted and hierarchical procedures can spend the budget unevenly without breaking "
            "guarantees. "
            "Reasoning path: (S1) require a preregistered error budget: which rate, at what level, "
            "and why that rate fits the decision; (S2) use weighted FDR and hierarchical testing to "
            "spend power on important hypotheses; (S3) report the realized false-discovery proportion "
            "estimate alongside rejections so consumers see what was spent; (S4) audit: in replication "
            "follow-ups, check whether budgeted procedures delivered their promised rates. "
            "Proposed mechanism: multiplicity control as accountable budgeting rather than ritual "
            "correction, with the budget declared before data collection. "
            "What would confirm it: budgeted procedures hitting their stated rates in replication audits "
            "while finding more true effects than one-size-fits-all corrections. What would kill it: "
            "budgets chosen post hoc to justify whatever was found, recreating p-hacking with extra "
            "steps. "
            "What it does NOT claim: a universally correct error rate, a proof of optimality, or peer "
            "acceptance. The choice of rate stays a judgment call; this is a proposed discipline for "
            "making it accountably, honestly labeled."),
        "key_points": [
            "Testing many hypotheses guarantees some chance findings; uncorrected testing floods the literature.",
            "Bonferroni controls family-wise error but sacrifices power as tests multiply.",
            "Benjamini-Hochberg 1995 FDR: control the expected fraction of false rejections - the modern workhorse.",
            "This walkthrough runs 2000 null tests: raw testing rejects about 100, Bonferroni about 0, BH a controlled few.",
            "Which error rate to control, and at what level, remains expert judgment.",
        ],
        "requirements": [
            "Any proposal must state the error rate, level, and justification before data collection.",
            "Procedures must be validated under realistic dependence, not just independence.",
            "The method must report realized error estimates, not just nominal guarantees.",
            "Replication audits must confirm promised rates in practice.",
        ],
        "standards": [
            "Benjamini Y, Hochberg Y. Controlling the false discovery rate; 1995.",
            "Standard: multiplicity methods are judged by realized error rates under realistic dependence.",
            "Standard: the chosen error rate must be justified by the decision the tests inform.",
        ],
        "citations": [CIT_BH, CIT_ASA16],
    },
    {
        "key": "optional_stopping",
        "name": "Optional Stopping and Data Peeking",
        "group": "Foundations",
        "ladder_rank": 7,
        "ladder_tier": "foundations",
        "problem": ("If you peek at accumulating data and stop the moment results look significant, "
                    "your false positive rate balloons far above the nominal level - Armitage, "
                    "McPherson, and Rowe showed this in 1969. Yet the likelihood principle says the "
                    "stopping rule should be irrelevant to the evidence. The open problem: how should "
                    "inference handle data-dependent stopping, and can the frequentist and "
                    "likelihood perspectives ever be reconciled?"),
        "background": ("Sequential analysis began as a wartime necessity, with Wald developing the "
                       "sequential probability ratio test. Armitage and colleagues then demonstrated "
                       "the cost of naive peeking: repeated significance testing on accumulating data "
                       "inflates the Type I error dramatically. Group-sequential methods answered with "
                       "alpha-spending functions that ration the error budget across looks. But the "
                       "philosophical tension never resolved: the likelihood of the observed data is "
                       "identical whether you planned to stop or peeked, so likelihood-based and "
                       "Bayesian inference ignore the stopping rule while frequentist inference depends "
                       "on it. Modern anytime-valid inference with e-values and test martingales offers "
                       "a frequentist way to peek safely, but the foundations question - whose answer "
                       "is right - remains open."),
        "why_it_matters": ("Everyone peeks: clinical trials have interim analyses, tech companies watch "
                           "dashboards, scientists check results early. If peeking invalidates the "
                           "statistics, most applied inference is broken; if it does not, much "
                           "frequentist machinery is needlessly rigid. The answer decides how the "
                           "world is allowed to learn from streaming data."),
        "pointer": ("The Signature system proposes a labeled approach to this open problem - see the "
                    "companion Signature Edition record for the full step-by-step walkthrough. The "
                    "problem itself remains open in established science; no solution is claimed."),
        "sig_lens": ("The Signature lens reads peeking as a contract problem: the analyst and the "
                     "audience need a stopping contract both can verify. The Signature approach "
                     "replaces the unobservable intention to stop with an observable, "
                     "anytime-valid evidence process anyone can audit."),
        "sig_solution": (
            LABEL + " Approach S-07: auditable anytime evidence. "
            "Assumptions: (A1) analysts will peek regardless of what theory says, so the method must "
            "survive peeking; (A2) e-values and test martingales give valid inference at arbitrary "
            "data-dependent stopping times; (A3) an evidence process logged immutably lets anyone "
            "verify the stopping contract after the fact. "
            "Reasoning path: (S1) replace fixed-sample p-values with e-value processes that stay valid "
            "under any stopping rule; (S2) log every interim look in a tamper-evident record so the "
            "actual stopping behavior is observable; (S3) report the stopped e-value with its "
            "anytime-valid guarantee instead of a peeking-corrupted p-value; (S4) compare decisions "
            "made under anytime rules against fixed-sample rules on historical trial data. "
            "Proposed mechanism: peeking made safe by construction through anytime-valid instruments "
            "plus an audit trail of looks. "
            "What would confirm it: trials run under anytime rules reaching correct conclusions as "
            "often as fixed designs while stopping earlier on average. What would kill it: e-value "
            "procedures proving too conservative for practical use, or analysts refusing the audit "
            "trail. "
            "What it does NOT claim: a resolution of the stopping-rule philosophical debate, a proof "
            "that peeking is always fine, or peer acceptance. This is a proposed engineering answer, "
            "honestly labeled."),
        "key_points": [
            "Armitage et al. 1969: repeated testing on accumulating data inflates Type I error far above nominal.",
            "The likelihood of the data is the same whether you planned the sample size or peeked - the core tension.",
            "Group-sequential methods ration the error budget across interim looks.",
            "This walkthrough simulates peeking: fixed-sample rejection stays near 5 percent, peeking inflates it sharply.",
            "Anytime-valid e-values aim to make peeking safe by construction.",
        ],
        "requirements": [
            "Any proposal must keep false positive rates at nominal levels under arbitrary peeking.",
            "The stopping behavior must be observable or the guarantee must not need it.",
            "Efficiency loss versus fixed-sample designs must be measured and acceptable.",
            "The philosophical disagreement must be acknowledged, not defined away.",
        ],
        "standards": [
            "Armitage P, McPherson CK, Rowe BC. Repeated significance tests on accumulating data; 1969.",
            "Standard: peeking-robust methods are validated by simulation under adversarial stopping rules.",
            "Standard: the stopping contract must be auditable by a third party.",
        ],
        "citations": [CIT_ARMITAGE, CIT_BIRNBAUM, CIT_GRUENWALD],
    },
    {
        "key": "likelihood_principle",
        "name": "The Likelihood Principle Versus Frequentist Practice",
        "group": "Foundations",
        "ladder_rank": 8,
        "ladder_tier": "foundations",
        "problem": ("Birnbaum proved in 1962 that two accepted principles - sufficiency and "
                    "conditionality - jointly imply the likelihood principle: all the evidence in "
                    "data is contained in the likelihood function, and experiments with proportional "
                    "likelihoods carry identical evidence. Yet standard frequentist tools violate it "
                    "daily. The open problem: is the likelihood principle true, and if so, what "
                    "becomes of p-values and confidence intervals?"),
        "background": ("Birnbaum 1962 derived the likelihood principle from the sufficiency principle "
                       "and the conditionality principle, both widely accepted, creating a paradox: "
                       "accept the premises and you must accept that stopping rules, sample spaces, "
                       "and unobserved outcomes are evidentially irrelevant. But frequentist p-values "
                       "and confidence intervals depend on all three. The binomial versus negative "
                       "binomial example is the classic exhibit: same data, proportional likelihoods, "
                       "different p-values. Bayesians embraced the principle; frequentists largely "
                       "rejected the conclusion while struggling to locate the flaw in the proof. "
                       "Decades of debate followed - Mayo, Evans, and others disputed the derivation - "
                       "but no refutation has won consensus, and the principle remains the sharpest "
                       "wedge between the schools of inference."),
        "why_it_matters": ("If the likelihood principle is correct, then a large share of standard "
                           "statistical practice conditions on things that did not happen and should be "
                           "abandoned. If it is wrong, then Bayesian and likelihood methods rest on a "
                           "false foundation. There is no middle position that has satisfied both "
                           "camps, and the working statistician deserves to know which foundation is "
                           "sound."),
        "pointer": ("The Signature system proposes a labeled approach to this open problem - see the "
                    "companion Signature Edition record for the full step-by-step walkthrough. The "
                    "problem itself remains open in established science; no solution is claimed."),
        "sig_lens": ("The Signature lens reads the likelihood-principle standoff as an unstated "
                     "question problem: the camps answer different questions - what does this data say, "
                     "versus how does this procedure behave. The Signature approach forces every "
                     "analysis to print its question before its answer."),
        "sig_solution": (
            LABEL + " Approach S-08: question-first reporting. "
            "Assumptions: (A1) the dispute persists because evidence questions and procedure questions "
            "are conflated in single-number reporting; (A2) both questions are legitimate and each has "
            "a correct instrument; (A3) analysts can be trained to separate them. "
            "Reasoning path: (S1) require every analysis to declare whether it answers an evidence "
            "question (what do these data say) or a procedure question (how does this rule behave); "
            "(S2) answer evidence questions with likelihood-respecting instruments and procedure "
            "questions with calibrated frequentist instruments, each labeled; (S3) exhibit the "
            "binomial versus negative binomial case side by side so the difference is visible; "
            "(S4) survey whether question-first reporting reduces cross-camp miscommunication. "
            "Proposed mechanism: a reporting standard that ends the conflation by making the question "
            "explicit, letting each school be right about its own question. "
            "What would confirm it: analysts and readers reliably distinguishing the two questions and "
            "choosing fitting instruments. What would kill it: proof that the two questions cannot be "
            "separated in practice, or that one camp rejects the legitimacy of the other question. "
            "What it does NOT claim: a proof or refutation of the likelihood principle, a philosophical "
            "victory for either side, or peer acceptance. Birnbaum paradox stands; this is a proposed "
            "truce with labels, honestly labeled."),
        "key_points": [
            "Birnbaum 1962: sufficiency plus conditionality implies the likelihood principle.",
            "The principle says experiments with proportional likelihoods carry identical evidence.",
            "Binomial versus negative binomial: same data and likelihood, different p-values - the classic exhibit.",
            "This walkthrough computes both likelihoods and both p-values to show the split concretely.",
            "No refutation of the derivation has won consensus; the wedge between schools persists.",
        ],
        "requirements": [
            "Any claimed resolution must address Birnbaum proof directly, not wave at it.",
            "It must say which of sufficiency, conditionality, or the derivation fails, if any.",
            "Practical guidance must follow: what should analysts actually compute.",
            "Both camps must recognize their question in the settlement.",
        ],
        "standards": [
            "Birnbaum A. On the foundations of statistical inference; 1962.",
            "Standard: resolutions are judged against the binomial versus negative binomial exhibit.",
            "Standard: evidence claims and procedure claims must be labeled as such.",
        ],
        "citations": [CIT_BIRNBAUM, CIT_HACKING],
    },
    {
        "key": "model_selection",
        "name": "AIC Versus BIC: No Universal Model Selection Winner",
        "group": "Foundations",
        "ladder_rank": 9,
        "ladder_tier": "foundations",
        "problem": ("Akaike 1974 AIC aims at predictive accuracy; Schwarz 1978 BIC aims at finding the "
                    "true model and is consistent. Yang proved in 2005 that no criterion can be both "
                    "consistent and minimax-rate optimal for prediction. The open problem: since no "
                    "single criterion does everything, what principled rule tells an analyst which "
                    "criterion to use - or is model selection inherently a judgment call?"),
        "background": ("Model selection is unavoidable: every analysis chooses variables, functional "
                       "forms, and complexity. Akaike derived AIC as an asymptotically unbiased estimate "
                       "of predictive risk, penalizing each parameter by 2. Schwarz derived BIC from a "
                       "Bayesian approximation, penalizing by log n per parameter, and it consistently "
                       "selects the true model when one exists. Practitioners split: prediction tasks "
                       "favor AIC-like criteria, scientific explanation favors BIC-like ones. Yang 2005 "
                       "proved the split is fundamental - consistency and minimax-rate optimal prediction "
                       "cannot be shared by one criterion. Cross-validation, focused information criteria, "
                       "and post-selection inference each address pieces, but the master question - which "
                       "criterion, when, and why - has no universally accepted answer."),
        "why_it_matters": ("Every fitted model in science, industry, and government passed through a "
                           "selection step. The choice of criterion changes which variables are declared "
                           "important, which effects are published, and which policies are justified. A "
                           "principled selection rule would remove one of the largest unacknowledged "
                           "researcher degrees of freedom."),
        "pointer": ("The Signature system proposes a labeled approach to this open problem - see the "
                    "companion Signature Edition record for the full step-by-step walkthrough. The "
                    "problem itself remains open in established science; no solution is claimed."),
        "sig_lens": ("The Signature lens reads AIC versus BIC as a goal-confusion problem: the analyst "
                     "has not said whether the model is for predicting or for explaining. The Signature "
                     "approach forces the goal into the open and lets the goal choose the criterion, "
                     "with the tradeoff priced explicitly."),
        "sig_solution": (
            LABEL + " Approach S-09: goal-declared selection. "
            "Assumptions: (A1) every modeling task has a primary goal on the prediction-explanation "
            "spectrum and the analyst can state it; (A2) Yang impossibility means the goal genuinely "
            "matters - there is no goal-free best criterion; (A3) stating the goal before selection "
            "removes the largest hidden degree of freedom. "
            "Reasoning path: (S1) require a goal declaration with every model selection: predict, "
            "explain, or a stated mixture; (S2) map goals to criteria by proven properties - AIC-family "
            "for prediction, BIC-family for identification - and publish the mapping; (S3) report the "
            "criterion the goal did not choose as a sensitivity check; (S4) audit published selections "
            "for goal-criterion mismatch. "
            "Proposed mechanism: a goal-declaration standard that turns criterion choice from a hidden "
            "lever into an accountable, auditable decision. "
            "What would confirm it: fewer contradictory model choices across analysts given the same "
            "data and goal. What would kill it: goals too vague to map to criteria, or analysts "
            "declaring goals post hoc to justify preferred models. "
            "What it does NOT claim: a universal criterion, a refutation of Yang impossibility, or peer "
            "acceptance. The impossibility stands; this is a proposed discipline for choosing honestly, "
            "honestly labeled."),
        "key_points": [
            "AIC (1974): penalize 2 per parameter, targets predictive accuracy.",
            "BIC (1978): penalize log n per parameter, consistent for the true model.",
            "Yang 2005: no criterion is both consistent and minimax-rate optimal - the split is fundamental.",
            "This walkthrough simulates both: BIC finds the true model, AIC predicts better - neither does both.",
            "Which criterion to use, when, and why has no universally accepted answer.",
        ],
        "requirements": [
            "Any proposal must respect Yang impossibility - no goal-free universal criterion exists.",
            "The goal-to-criterion mapping must rest on proven properties, not folklore.",
            "Sensitivity to the unchosen criterion must be reported.",
            "Adoption needs journal and software defaults, not just papers.",
        ],
        "standards": [
            "Akaike H. A new look at the statistical model identification; 1974.",
            "Schwarz G. Estimating the dimension of a model; 1978.",
            "Standard: selection criteria are judged against the declared goal, prediction or identification.",
        ],
        "citations": [CIT_AKAIKE, CIT_SCHWARZ, CIT_YANG],
    },
    {
        "key": "reference_class",
        "name": "The Reference Class Problem",
        "group": "Foundations",
        "ladder_rank": 10,
        "ladder_tier": "foundations",
        "problem": ("To say a 60-year-old smoker has a 12 percent chance of heart disease, you must "
                    "pick a reference class: 60-year-olds, smokers, 60-year-old smokers, people with "
                    "his exact profile. Each class gives a different probability, and narrower is not "
                    "always better. Reichenbach and von Mises posed the problem a century ago; no "
                    "principled rule for choosing the reference class has won acceptance."),
        "background": ("Frequentist probability attaches to collectives, not individuals, so any "
                       "single-case probability must borrow a class the individual belongs to. But "
                       "every individual belongs to many classes - age, sex, habits, genetics, zip code "
                       "- and the classes give different rates. Reichenbach proposed the narrowest "
                       "class with reliable statistics, but narrow classes have tiny samples and their "
                       "own selection biases. The problem infects medicine, insurance, and law: a risk "
                       "score is only as meaningful as its reference class, and the choice of class is "
                       "rarely defended. Machine learning inherits it silently - a model prediction is a "
                       "reference-class probability where the class is whatever the training data "
                       "resembled. A century on, the choice remains convention and convenience."),
        "why_it_matters": ("Risk scores drive medical treatment, insurance pricing, parole decisions, "
                           "and hiring tools. If the reference class is arbitrary, the score is "
                           "arbitrary in exactly the measure that matters. A principled rule would turn "
                           "risk assessment from alchemy into science."),
        "pointer": ("The Signature system proposes a labeled approach to this open problem - see the "
                    "companion Signature Edition record for the full step-by-step walkthrough. The "
                    "problem itself remains open in established science; no solution is claimed."),
        "sig_lens": ("The Signature lens reads the reference class as a hidden parameter of every risk "
                     "statement. The Signature approach promotes it to a reported parameter: every "
                     "probability ships with its class, plus the range across neighboring classes, so "
                     "the arbitrariness becomes visible and bounded."),
        "sig_solution": (
            LABEL + " Approach S-10: class-labeled probabilities. "
            "Assumptions: (A1) the reference class is a genuine parameter of the probability claim and "
            "can be reported; (A2) probabilities across a ladder of nested classes usually vary "
            "smoothly enough that the range is informative; (A3) decision-makers prefer an honest "
            "range over a false point. "
            "Reasoning path: (S1) require every single-case probability to name its reference class; "
            "(S2) compute the probability across a ladder of nested classes from broad to narrow and "
            "report the range; (S3) where the range is wide, flag the claim as class-sensitive and "
            "demand more data before acting; (S4) validate that class-labeled reporting reduces "
            "overconfident decisions in trials. "
            "Proposed mechanism: a reporting standard that makes the reference class explicit and "
            "bounds the arbitrariness with a class ladder. "
            "What would confirm it: decisions improving when ranges replace points in high-stakes "
            "risk scoring. What would kill it: class ladders so unstable that ranges are uselessly "
            "wide everywhere, or users ignoring the labels. "
            "What it does NOT claim: a rule for the one true reference class, a philosophical "
            "solution, or peer acceptance. The problem stays open; this is a proposed honesty "
            "discipline, honestly labeled."),
        "key_points": [
            "Single-case probabilities need a reference class; individuals belong to many classes.",
            "Different classes give different probabilities - the choice moves the number.",
            "Reichenbach narrowest-reliable-class rule never won consensus; narrow means noisy.",
            "This walkthrough computes the same risk under three nested classes: the number moves each time.",
            "Machine learning predictions are reference-class probabilities with the class left implicit.",
        ],
        "requirements": [
            "Any proposal must handle the narrow-class noise problem, not just the broad-class vagueness.",
            "The class ladder must be computable from available data.",
            "Decision trials must show the labels change behavior, not just decorate reports.",
            "Legal and medical contexts need the rule stated plainly enough for non-statisticians.",
        ],
        "standards": [
            "Reichenbach H. The Theory of Probability; 1949.",
            "Standard: single-case probabilities must name the class or be marked class-unspecified.",
            "Standard: class sensitivity is measured by the range across nested classes.",
        ],
        "citations": [CIT_GILLIES, CIT_HACKING],
    },
    {
        "key": "prior_elicitation",
        "name": "The Problem of Priors: Elicitation and Sensitivity",
        "group": "Foundations",
        "ladder_rank": 11,
        "ladder_tier": "foundations",
        "problem": ("Bayesian inference needs a prior, and the posterior can depend on it more than on "
                    "the data. Eliciting honest priors from experts is notoriously hard, priors are "
                    "often chosen for convenience, and sensitivity analyses can show conclusions "
                    "reversing under reasonable alternative priors. The open problem: how should priors "
                    "be chosen, justified, and stress-tested so Bayesian conclusions are trustworthy?"),
        "background": ("Since Ramsey, de Finetti, and Savage, Bayesians have held that priors represent "
                       "beliefs and coherence governs updating. In practice, priors are often default "
                       "choices - conjugate, flat, or weakly informative - selected for computation, not "
                       "belief. Elicitation research shows experts are overconfident and inconsistent, "
                       "and that small elicitation differences can move posteriors substantially. "
                       "Objective Bayes offers reference priors as defaults, but their objectivity is "
                       "contested. Robust Bayesian analysis reports ranges over prior classes instead of "
                       "points, which is honest but often too wide to act on. The working compromise - "
                       "weakly informative priors plus a sensitivity paragraph - is convention, not a "
                       "solved methodology."),
        "why_it_matters": ("Bayesian methods now run clinical trials, A/B tests, and AI systems. If "
                           "conclusions hinge on an unjustified prior, the objectivity Bayesian methods "
                           "promise is an illusion. A trustworthy prior methodology would let decision "
                           "makers know exactly how much of a conclusion came from data and how much "
                           "from assumption."),
        "pointer": ("The Signature system proposes a labeled approach to this open problem - see the "
                    "companion Signature Edition record for the full step-by-step walkthrough. The "
                    "problem itself remains open in established science; no solution is claimed."),
        "sig_lens": ("The Signature lens reads the prior as a budget of assumption the analysis spends. "
                     "The Signature approach requires the budget to be declared, priced in posterior "
                     "movement, and stress-tested against adversarially reasonable alternatives before "
                     "any conclusion ships."),
        "sig_solution": (
            LABEL + " Approach S-11: prior budgeting with adversarial audit. "
            "Assumptions: (A1) every prior encodes assumptions whose influence can be measured by "
            "sensitivity; (A2) a class of reasonable alternative priors can be constructed from the "
            "elicitation record; (A3) conclusions stable across the class deserve more trust than "
            "fragile ones. "
            "Reasoning path: (S1) elicit priors with a structured protocol that records uncertainty "
            "about the elicitation itself; (S2) compute the posterior across the reasonable-prior "
            "class and report the range, not just the default-prior point; (S3) run an adversarial "
            "audit: the most hostile reasonable prior gets its say in the report; (S4) grade "
            "conclusions by stability - publish the fragility index alongside the posterior. "
            "Proposed mechanism: priors as declared assumption budgets with mandatory adversarial "
            "sensitivity auditing. "
            "What would confirm it: audited analyses replicating better and surviving criticism more "
            "often than unaudited ones. What would kill it: reasonable-prior classes too wide to ever "
            "permit conclusions, or elicitation too unreliable to build the class. "
            "What it does NOT claim: a true prior, a proof that elicitation works, or peer acceptance. "
            "The prior problem stays open; this is a proposed accountability discipline, honestly "
            "labeled."),
        "key_points": [
            "Posteriors can move more with the prior than with the data - this walkthrough shows the swing directly.",
            "Expert elicitation is unreliable: overconfidence and inconsistency are well documented.",
            "Default priors are chosen for computation, not belief; their objectivity is contested.",
            "Robust Bayes reports ranges over prior classes - honest, but often too wide to act on.",
            "The standard compromise of weakly informative priors plus a sensitivity paragraph is convention, not solution.",
        ],
        "requirements": [
            "Elicitation protocols must be validated against expert calibration data.",
            "The reasonable-prior class must be constructible without circularity.",
            "Stability grading must be shown to predict real-world robustness.",
            "The audit must be cheap enough for routine analyses.",
        ],
        "standards": [
            "Savage LJ. The Foundations of Statistics; 1954.",
            "Standard: Bayesian reports must separate what the data said from what the prior assumed.",
            "Standard: sensitivity ranges are reported, not buried in appendices.",
        ],
        "citations": [CIT_HACKING, CIT_BERNARDO],
    },
    {
        "key": "grue",
        "name": "Goodman New Riddle: Projectibility",
        "group": "Foundations",
        "ladder_rank": 12,
        "ladder_tier": "foundations",
        "problem": ("Define grue as green if observed before some future time t, blue afterwards. "
                    "Every green emerald ever seen confirms both all emeralds are green and all "
                    "emeralds are grue, yet the two predict opposite colors after t. Goodman 1955 "
                    "showed that past fit cannot pick the projectible hypothesis. The open problem: "
                    "what makes a pattern projectible, and can statistics formalize it?"),
        "background": ("Hume asked why we project the past into the future; Goodman asked which "
                       "patterns we project. Grue is the perfect trap: it fits all evidence exactly as "
                       "well as green, so no evidence-based rule stated purely in terms of fit can "
                       "prefer green. Goodman answer was entrenchment: green is projectible because the "
                       "predicate has a history of successful use in our language. Bayesians reply with "
                       "simplicity priors; formal learning theorists with Occam bounds; machine learning "
                       "with inductive bias. But every formal proposal either smuggles in projectibility "
                       "through the choice of hypothesis class or faces grue-like counterexamples in a "
                       "richer language. Feature engineering in statistics and machine learning is "
                       "applied projectibility judgment, and it remains judgment, not theorem."),
        "why_it_matters": ("Every predictive model bets that its features are projectible - that the "
                           "patterns it found will hold. Grue shows that fit alone can never justify "
                           "the bet. Understanding projectibility is understanding when prediction is "
                           "licensed, which is the central question of applied statistics and machine "
                           "learning."),
        "pointer": ("The Signature system proposes a labeled approach to this open problem - see the "
                    "companion Signature Edition record for the full step-by-step walkthrough. The "
                    "problem itself remains open in established science; no solution is claimed."),
        "sig_lens": ("The Signature lens reads grue as a feature-audit problem: the danger is not in "
                     "the fitting but in the predicates. The Signature approach audits every feature "
                     "for projectibility - causal grounding, stability across regimes, resistance to "
                     "grue-style redescription - before the model is allowed to bet on it."),
        "sig_solution": (
            LABEL + " Approach S-12: projectibility auditing for features. "
            "Assumptions: (A1) projectibility is a property of predicates that can be probed, even if "
            "not defined formally; (A2) causally grounded and regime-stable features resist "
            "grue-style redescription better than gerrymandered ones; (A3) an audit trail of feature "
            "provenance is feasible in applied work. "
            "Reasoning path: (S1) require every predictive feature to carry provenance: why this "
            "predicate, what mechanism grounds it; (S2) run grue stress tests - redescribe features in "
            "time-indexed or disjunctive forms and check whether the model survives; (S3) score "
            "features on regime stability using historical regime changes; (S4) refuse to deploy "
            "models whose predictive power concentrates in unaudited features. "
            "Proposed mechanism: a feature projectibility audit that treats predicates as guilty until "
            "proven projectible. "
            "What would confirm it: audited models surviving regime changes better than unaudited ones "
            "in prospective tests. What would kill it: grue-style redescriptions defeating every "
            "audit, proving projectibility unformalizable in practice. "
            "What it does NOT claim: a formal solution to Goodman riddle, a definition of "
            "projectibility, or peer acceptance. The riddle stands; this is a proposed engineering "
            "discipline, honestly labeled."),
        "key_points": [
            "Goodman 1955: grue fits all past evidence exactly as well as green but predicts the opposite future.",
            "No purely fit-based rule can prefer the projectible hypothesis - that is the riddle.",
            "Entrenchment, simplicity priors, and inductive bias are the main replies; all are contested.",
            "This walkthrough shows both hypotheses fitting past data perfectly and diverging after time t.",
            "Feature engineering is applied projectibility judgment, still judgment rather than theorem.",
        ],
        "requirements": [
            "Any proposal must survive grue-style redescription, not just toy examples.",
            "The audit must be applicable to real feature pipelines.",
            "Regime-stability scoring needs historical regime changes to validate against.",
            "The approach must acknowledge it formalizes heuristics, not the riddle itself.",
        ],
        "standards": [
            "Goodman N. Fact, Fiction, and Forecast; 1955.",
            "Standard: projectibility claims are tested by grue-style redescription stress tests.",
            "Standard: features ship with provenance or are marked unaudited.",
        ],
        "citations": [CIT_GOODMAN, CIT_HUME],
    },
    {
        "key": "misspecification",
        "name": "Optimal Inference Under Model Misspecification",
        "group": "Compounded",
        "ladder_rank": 13,
        "ladder_tier": "compounded",
        "problem": ("All models are wrong, yet inference theory mostly assumes the model is right. "
                    "Huber 1967 and White 1982 gave us sandwich covariances and quasi-likelihood for "
                    "coping, but there is no unified theory of OPTIMAL inference under "
                    "misspecification: which estimator to use, what target it estimates, and what "
                    "efficiency even means when the model is false remain open questions."),
        "background": ("Box aphorism that all models are wrong but some are useful is the working "
                       "creed, and Huber 1967 made it rigorous: maximum likelihood under misspecification "
                       "converges to the parameter minimizing Kullback-Leibler divergence, with a "
                       "sandwich covariance replacing the naive one. White 1982 built the full "
                       "quasi-maximum-likelihood theory. But optimality theory - Cramer-Rao bounds, "
                       "efficient estimators, optimal tests - is developed almost entirely under correct "
                       "specification. Under misspecification, even the target is unclear: the "
                       "pseudo-true value, the best linear approximation, or a projection the scientist "
                       "actually wants. Model-robust standard errors are standard in econometrics, yet "
                       "choosing among robust estimators, and knowing what is lost by robustness, has no "
                       "complete theory."),
        "why_it_matters": ("Every real analysis is misspecified - wrong functional form, wrong "
                           "distributional assumptions, omitted variables. A theory of optimal inference "
                           "for the world as it is, rather than the world as models pretend, would "
                           "upgrade essentially all applied statistics. Until then, robustness is craft, "
                           "not science."),
        "pointer": ("The Signature system proposes a labeled approach to this open problem - see the "
                    "companion Signature Edition record for the full step-by-step walkthrough. The "
                    "problem itself remains open in established science; no solution is claimed."),
        "sig_lens": ("The Signature lens reads misspecification as a target problem first and an "
                     "estimator problem second: you cannot be optimal until you say optimal for what. "
                     "The Signature approach forces the target to be declared - the projection the "
                     "scientist actually wants - then builds the estimator to hit that target "
                     "robustly."),
        "sig_solution": (
            LABEL + " Approach S-13: target-declared robust inference. "
            "Assumptions: (A1) the scientifically relevant target can be stated as a functional of the "
            "true distribution, not of a false model; (A2) influence-function machinery can build "
            "estimators for such targets with known robustness properties; (A3) the degree of "
            "misspecification can be bounded or at least probed empirically. "
            "Reasoning path: (S1) replace model parameters with target functionals declared in plain "
            "language; (S2) construct estimators via influence functions with bounded influence and "
            "document the breakdown behavior; (S3) report a misspecification diagnostic - how far the "
            "working model is from the data - alongside every estimate; (S4) validate on real "
            "misspecified problems where the target functional is known by design. "
            "Proposed mechanism: inference organized around declared targets with robustness priced "
            "explicitly, instead of around models everyone knows are false. "
            "What would confirm it: target-declared procedures beating model-based ones on real "
            "misspecified tasks in preregistered comparisons. What would kill it: targets too vague "
            "to formalize in practice, or robustness costs too large to bear. "
            "What it does NOT claim: a general optimality theory under misspecification, a replacement "
            "for modeling care, or peer acceptance. The unified theory stays open; this is a proposed "
            "discipline, honestly labeled."),
        "key_points": [
            "Huber 1967: under misspecification, MLE converges to the KL-minimizing pseudo-true value.",
            "White 1982: full quasi-MLE theory with sandwich covariances.",
            "This walkthrough simulates heteroskedastic regression: naive standard errors undercover, sandwich covers.",
            "Optimality theory under misspecification barely exists - even the target is disputed.",
            "Robustness today is craft: sandwich errors are standard but estimator choice is ad hoc.",
        ],
        "requirements": [
            "Any proposal must define the target independently of the false model.",
            "Robustness properties must be stated as theorems or measured empirically, not assumed.",
            "The cost of robustness in efficiency must be quantified.",
            "Validation needs real misspecified problems with known targets.",
        ],
        "standards": [
            "Huber PJ. The behavior of maximum likelihood estimates under nonstandard conditions; 1967.",
            "White H. Maximum likelihood estimation of misspecified models; 1982.",
            "Standard: robust procedures report both the target functional and the misspecification diagnostic.",
        ],
        "citations": [CIT_HUBER, CIT_WHITE],
    },
    {
        "key": "post_selection",
        "name": "Post-Selection Inference",
        "group": "Compounded",
        "ladder_rank": 14,
        "ladder_tier": "compounded",
        "problem": ("Analysts use data to select a model - stepwise regression, the lasso, thresholding "
                    "- then report p-values and intervals as if the model were fixed in advance. It was "
                    "not, and the naive intervals undercover badly. Berk and colleagues 2013 and Lee "
                    "and colleagues 2016 built exact conditional methods for selected models, but valid "
                    "post-selection inference in general, powerful, and usable form remains open."),
        "background": ("Selection bias after data snooping is old - it is the winner curse formalized. "
                       "Classical theory conditions on nothing selected, so it cannot handle selection. "
                       "Berk, Brown, Buja, Zhang, and Zhao 2013 gave PoSI: intervals valid over all "
                       "possible selected submodels, at the price of width. Lee, Sun, Sun, and Taylor "
                       "2016 gave exact conditional inference for the lasso: condition on the selection "
                       "event and get exact p-values, at the price of conditioning away power and "
                       "handling only specific selectors. The field has since grown - selective inference "
                       "for many procedures - but gaps remain: uniformity over selection rules, "
                       "nonparametric settings, and methods scientists will actually use instead of the "
                       "naive intervals they currently publish."),
        "why_it_matters": ("Nearly every published regression selected its variables somehow, and nearly "
                           "every published interval ignores the selection. The published uncertainty "
                           "statements of applied science are therefore systematically overconfident. "
                           "Fixing post-selection inference would repair the credibility of the most "
                           "common analysis in science."),
        "pointer": ("The Signature system proposes a labeled approach to this open problem - see the "
                    "companion Signature Edition record for the full step-by-step walkthrough. The "
                    "problem itself remains open in established science; no solution is claimed."),
        "sig_lens": ("The Signature lens reads post-selection as a honesty-about-search problem: the "
                     "reported uncertainty must price the search that found the model. The Signature "
                     "approach logs the selection path automatically and attaches the selection-adjusted "
                     "uncertainty to every reported result."),
        "sig_solution": (
            LABEL + " Approach S-14: search-logged selective reporting. "
            "Assumptions: (A1) selection procedures can be logged completely by software; (A2) "
            "conditional-on-selection inference is computable for logged procedures or conservatively "
            "bounded; (A3) analysts will accept wider honest intervals over narrow dishonest ones if "
            "journals require it. "
            "Reasoning path: (S1) instrument analysis software to log every selection decision in a "
            "machine-readable search record; (S2) compute selection-adjusted intervals by conditioning "
            "on the logged selection event, falling back to PoSI-style universal bounds when exact "
            "conditioning is infeasible; (S3) print naive and adjusted intervals side by side so the "
            "cost of selection is visible; (S4) audit published work: how often do adjusted intervals "
            "change conclusions. "
            "Proposed mechanism: selection logging plus automatic selective inference, making honest "
            "post-selection uncertainty the default output. "
            "What would confirm it: adjusted intervals achieving nominal coverage in real analysis "
            "pipelines while remaining usable. What would kill it: selection events too complex to "
            "condition on, or adjustments so wide that nothing is ever significant. "
            "What it does NOT claim: a general powerful selective inference theory, a solution for "
            "informal human selection, or peer acceptance. The theory stays open; this is a proposed "
            "engineering discipline, honestly labeled."),
        "key_points": [
            "Selecting a model with data then ignoring the selection invalidates classical intervals.",
            "Berk et al. 2013 PoSI: intervals valid over all submodels, at the price of width.",
            "Lee et al. 2016: exact conditional inference for the lasso by conditioning on selection.",
            "This walkthrough simulates selection among 20 null predictors: naive p-values inflate badly.",
            "General, powerful, usable selective inference remains an open research frontier.",
        ],
        "requirements": [
            "Adjusted intervals must achieve nominal coverage under realistic selection pipelines.",
            "The method must handle the selectors analysts actually use, not just the lasso.",
            "Power loss versus the naive (invalid) procedure must be measured and acceptable.",
            "Informal human selection - the analyst eyeballing results - must be addressed, not ignored.",
        ],
        "standards": [
            "Berk R et al. Valid post-selection inference; 2013.",
            "Lee JD et al. Exact post-selection inference, with application to the lasso; 2016.",
            "Standard: reported uncertainty must price the search that produced the model.",
        ],
        "citations": [CIT_BERK, CIT_LEE],
    },
    {
        "key": "high_dim",
        "name": "High-Dimensional p Much Greater Than n Guarantees",
        "group": "Compounded",
        "ladder_rank": 15,
        "ladder_tier": "compounded",
        "problem": ("Modern data have more variables than observations: genomics, imaging, text. The "
                    "lasso and its cousins estimate well under sparsity, with sharp theory from "
                    "Bickel, Ritov, and Tsybakov 2009. But valid inference - confidence intervals, "
                    "p-values - in p much greater than n rests on unverifiable assumptions like "
                    "restricted eigenvalues, and model-free finite-sample guarantees remain largely "
                    "open."),
        "background": ("Tibshirani 1996 lasso made high-dimensional estimation practical via l1 "
                       "penalization. The theory followed: oracle inequalities and minimax rates under "
                       "sparsity and design conditions such as restricted eigenvalues or compatibility "
                       "(Bickel, Ritov, Tsybakov 2009). Estimation was the solved half. Inference - "
                       "honest uncertainty for selected or low-dimensional parameters - proved harder: "
                       "the debiased lasso of Zhang and Zhang 2014 and van de Geer and colleagues 2014 "
                       "gives asymptotically valid intervals, but under assumptions no one can verify "
                       "on real data. Uniform inference, assumption-lean guarantees, and finite-sample "
                       "(not asymptotic) validity in high dimensions are the open frontier, and the gap "
                       "between what the theory assumes and what data provide has never been closed."),
        "why_it_matters": ("High-dimensional data are the data of modern biology, medicine, and AI. If "
                           "inference in p greater than n cannot be made honest without unverifiable "
                           "assumptions, then the uncertainty statements on the most important modern "
                           "datasets are built on hope. Closing the gap would put high-dimensional "
                           "science on solid ground."),
        "pointer": ("The Signature system proposes a labeled approach to this open problem - see the "
                    "companion Signature Edition record for the full step-by-step walkthrough. The "
                    "problem itself remains open in established science; no solution is claimed."),
        "sig_lens": ("The Signature lens reads high-dimensional inference as an assumption-pricing "
                     "problem: the guarantees are only as good as the unverifiable conditions behind "
                     "them. The Signature approach prices every assumption with a sensitivity audit and "
                     "reports assumption-lean bounds alongside the sharp ones."),
        "sig_solution": (
            LABEL + " Approach S-15: assumption-priced high-dimensional inference. "
            "Assumptions: (A1) sharp high-dimensional guarantees need strong design conditions; "
            "(A2) assumption-lean but wider guarantees exist via sample splitting and conformal-style "
            "arguments; (A3) reporting both lets consumers see what the assumptions buy. "
            "Reasoning path: (S1) compute the sharp debiased-lasso interval under standard assumptions "
            "and an assumption-lean interval via sample splitting; (S2) run assumption diagnostics - "
            "stability of selection across splits, design-condition proxies - and report them; "
            "(S3) where diagnostics fail, the lean interval becomes the headline; (S4) benchmark on "
            "real high-dimensional datasets with known ground truth from follow-up experiments. "
            "Proposed mechanism: dual reporting - sharp under assumptions, lean without - with "
            "diagnostics deciding which headline the analysis earns. "
            "What would confirm it: dual-reported analyses showing better real-world coverage than "
            "sharp-only reporting. What would kill it: lean intervals too wide for any use, or "
            "diagnostics with no power to detect assumption failure. "
            "What it does NOT claim: assumption-free high-dimensional inference, a proof of new "
            "guarantees, or peer acceptance. The frontier stays open; this is a proposed honesty "
            "discipline, honestly labeled."),
        "key_points": [
            "Tibshirani 1996 lasso: l1 penalization makes p greater than n estimation practical.",
            "Bickel, Ritov, Tsybakov 2009: sharp oracle inequalities under restricted eigenvalues.",
            "Debiased lasso (Zhang and Zhang 2014) gives intervals, but under unverifiable assumptions.",
            "This walkthrough fits a lasso by coordinate descent in p greater than n and measures recovery.",
            "Model-free finite-sample inference guarantees in high dimensions remain largely open.",
        ],
        "requirements": [
            "Any proposal must state its design assumptions and provide diagnostics for them.",
            "Coverage must be demonstrated empirically, not just asymptotically.",
            "The method must scale to real p much greater than n problems.",
            "Assumption-lean fallbacks must be usable, not vacuous.",
        ],
        "standards": [
            "Bickel PJ, Ritov Y, Tsybakov AB. Simultaneous analysis of Lasso and Dantzig selector; 2009.",
            "Zhang CH, Zhang SS. Confidence intervals for low dimensional parameters; 2014.",
            "Standard: high-dimensional intervals report their assumptions and diagnostics, not just numbers.",
        ],
        "citations": [CIT_TIBSHIRANI, CIT_BRT, CIT_ZZ],
    },
    {
        "key": "bootstrap_fail",
        "name": "Where the Bootstrap Breaks",
        "group": "Compounded",
        "ladder_rank": 16,
        "ladder_tier": "compounded",
        "problem": ("Efron 1979 bootstrap is the most trusted resampling tool in statistics, but it "
                    "fails silently in important cases: parameters on the boundary of the parameter "
                    "space (Andrews 2000), superefficient and shrinkage estimators like the lasso "
                    "(Bickel and Freedman 1981), and extremes. The open problem: a complete, usable "
                    "characterization of when the bootstrap can be trusted and what to use when it "
                    "cannot."),
        "background": ("The bootstrap approximates sampling distributions by resampling the data, and "
                       "for smooth functionals of means it works beautifully with deep theory behind "
                       "it. The failures were found early: Bickel and Freedman 1981 showed inconsistency "
                       "for estimators with nonstandard asymptotics, and Andrews 2000 showed the "
                       "bootstrap fails when the true parameter sits on the boundary, because resampling "
                       "cannot mimic the constrained geometry. Fixes exist - the m-out-of-n bootstrap, "
                       "subsampling - but they trade efficiency for validity and need tuning. "
                       "Practitioners bootstrap boundary and shrinkage problems daily without knowing "
                       "the theory voids the warranty, and no complete map of the safe territory exists."),
        "why_it_matters": ("The bootstrap is the default uncertainty engine across science and "
                           "industry. Silent failures mean published intervals that do not cover at "
                           "their stated rates, with no warning light. A complete trust map would tell "
                           "every analyst when resampling is safe and what to reach for instead."),
        "pointer": ("The Signature system proposes a labeled approach to this open problem - see the "
                    "companion Signature Edition record for the full step-by-step walkthrough. The "
                    "problem itself remains open in established science; no solution is claimed."),
        "sig_lens": ("The Signature lens reads bootstrap failure as a missing warning-light problem: "
                     "the method gives no signal when its warranty is void. The Signature approach "
                     "builds a pre-flight diagnostic that probes the failure modes before any "
                     "resampling begins."),
        "sig_solution": (
            LABEL + " Approach S-16: bootstrap pre-flight diagnostics. "
            "Assumptions: (A1) the known failure modes - boundary parameters, nonstandard asymptotics, "
            "heavy tails, extremes - are detectable from the data and estimator; (A2) a diagnostic "
            "suite can flag them with acceptable error rates; (A3) valid fallbacks exist for flagged "
            "cases. "
            "Reasoning path: (S1) build a diagnostic battery: boundary proximity tests, smoothness "
            "probes of the estimator, tail-index estimates; (S2) run it before bootstrapping and grade "
            "the problem green, amber, or red; (S3) route amber and red cases to subsampling, m-out-of-n, "
            "or analytic alternatives automatically; (S4) validate the router on the known failure "
            "catalog plus real datasets. "
            "Proposed mechanism: a pre-flight check that voids the bootstrap warranty explicitly when "
            "the theory does, with automatic fallback routing. "
            "What would confirm it: the router catching the classic failures and achieving nominal "
            "coverage where naive bootstrap fails. What would kill it: failure modes too subtle for "
            "diagnostics, or fallbacks too weak to matter. "
            "What it does NOT claim: a complete characterization of bootstrap consistency, new theory, "
            "or peer acceptance. The map stays incomplete; this is a proposed safety system, honestly "
            "labeled."),
        "key_points": [
            "Efron 1979 bootstrap: resample the data to approximate sampling distributions.",
            "Bickel and Freedman 1981: inconsistent for estimators with nonstandard asymptotics.",
            "Andrews 2000: fails when the parameter is on the boundary of the parameter space.",
            "This walkthrough bootstraps a uniform maximum: coverage falls well short of nominal.",
            "No complete, usable map of safe versus unsafe bootstrap territory exists.",
        ],
        "requirements": [
            "Diagnostics must detect the known failure modes with measured error rates.",
            "Fallbacks must achieve nominal coverage where the bootstrap fails.",
            "The suite must run fast enough for routine use.",
            "Validation must cover the full known failure catalog.",
        ],
        "standards": [
            "Efron B. Bootstrap methods: another look at the jackknife; 1979.",
            "Andrews DWK. Inconsistency of the bootstrap on the boundary; 2000.",
            "Standard: resampling reports must state the diagnostic grade, not just the interval.",
        ],
        "citations": [CIT_EFRON, CIT_BF, CIT_ANDREWS],
    },
    {
        "key": "causal_obs",
        "name": "Causal Inference from Observational Data",
        "group": "Compounded",
        "ladder_rank": 17,
        "ladder_tier": "compounded",
        "problem": ("Randomized experiments identify causes; observational data usually do not, "
                    "because of unmeasured confounding. Pearl do-calculus 2009 is complete for "
                    "identification given a known causal graph, and potential-outcomes methods handle "
                    "measured confounding - but the graph is rarely known and unmeasured confounding "
                    "is untestable. The open problem: what licenses causal claims from observational "
                    "data, and how should the untestable assumptions be handled?"),
        "background": ("Causality formalized along two tracks: Rubin 1974 potential outcomes, where "
                       "causal effects are contrasts between treated and untreated potential states, "
                       "and Pearl 2009 structural causal models with DAGs and the do-operator. Given a "
                       "correct graph, do-calculus decides identifiability completely. The catch is "
                       "epistemic: graphs encode exactly the untestable assumptions - which variables "
                       "confound, which are colliders - that the data cannot verify. Sensitivity "
                       "analysis in the Rosenbaum tradition asks how much hidden bias would overturn a "
                       "conclusion, which is honest but often inconclusive. Natural experiments, "
                       "instrumental variables, and difference-in-differences each buy identification "
                       "with their own untestable assumptions. The field has superb machinery for "
                       "reasoning given assumptions and no consensus on which assumptions observational "
                       "studies may claim."),
        "why_it_matters": ("Most questions that matter - does this drug work, does this policy help, "
                           "does this exposure harm - cannot be randomized, or cannot be randomized "
                           "ethically. If observational causal inference cannot be put on solid ground, "
                           "evidence-based medicine and policy rest on hope; if it can, the payoff is "
                           "enormous."),
        "pointer": ("The Signature system proposes a labeled approach to this open problem - see the "
                    "companion Signature Edition record for the full step-by-step walkthrough. The "
                    "problem itself remains open in established science; no solution is claimed."),
        "sig_lens": ("The Signature lens reads observational causality as an assumption-ledger problem: "
                     "every causal claim spends untestable assumptions, and the spending is currently "
                     "off the books. The Signature approach puts every assumption on a public ledger "
                     "with its price in conclusion-fragility."),
        "sig_solution": (
            LABEL + " Approach S-17: assumption-ledger causal reporting. "
            "Assumptions: (A1) every observational causal analysis can enumerate its identifying "
            "assumptions explicitly; (A2) sensitivity analysis can price each assumption in terms of "
            "how much violation overturns the conclusion; (A3) graded conclusions - robust, fragile, "
            "speculative - are more useful than binary causal claims. "
            "Reasoning path: (S1) require a causal graph or equivalent assumption set drawn before "
            "estimation; (S2) compute the estimate plus a full sensitivity frontier: the set of hidden-"
            "bias magnitudes compatible with each conclusion; (S3) grade the claim by its distance to "
            "the overturn boundary; (S4) validate grading against cases where later experiments "
            "revealed the truth. "
            "Proposed mechanism: causal conclusions shipped with an assumption ledger and a fragility "
            "grade, replacing binary causal claims with priced ones. "
            "What would confirm it: fragility grades predicting which observational claims later "
            "experiments overturn. What would kill it: sensitivity frontiers too wide to grade "
            "anything, or ledgers too complex for applied researchers. "
            "What it does NOT claim: a way to test the untestable, identification without assumptions, "
            "or peer acceptance. The epistemic gap stays open; this is a proposed accounting "
            "discipline, honestly labeled."),
        "key_points": [
            "Rubin 1974 potential outcomes and Pearl 2009 DAGs are the two formal frameworks.",
            "Do-calculus is complete for identification given the true graph - but the graph is the assumption.",
            "Unmeasured confounding is untestable from observational data alone.",
            "This walkthrough simulates hidden confounding: naive regression is badly biased, sensitivity analysis maps the fragility.",
            "No consensus exists on which untestable assumptions observational studies may claim.",
        ],
        "requirements": [
            "Assumption sets must be enumerated before estimation, not rationalized after.",
            "Sensitivity frontiers must be computed, not gestured at.",
            "Grading must be validated against later experimental truth.",
            "The ledger must be usable by applied researchers, not only methodologists.",
        ],
        "standards": [
            "Pearl J. Causality: Models, Reasoning, and Inference; 2009.",
            "Rubin DB. Estimating causal effects of treatments; 1974.",
            "Standard: causal claims report their assumption ledger and fragility grade.",
        ],
        "citations": [CIT_PEARL, CIT_RUBIN74, CIT_ROSENBAUM],
    },
    {
        "key": "causal_discovery",
        "name": "Causal Discovery: Learning Cause from Correlation",
        "group": "Compounded",
        "ladder_rank": 18,
        "ladder_tier": "compounded",
        "problem": ("Can observational data reveal the causal graph itself? Algorithms like PC and FCI "
                    "try, but graphs in the same Markov equivalence class imply identical conditional "
                    "independencies and are indistinguishable from observational data alone. Learning "
                    "Bayesian networks is NP-hard (Chickering 1996). The open problem: how far can "
                    "causal discovery go, and what extra assumptions or data buy the rest?"),
        "background": ("Spirtes, Glymour, and Scheines built the constraint-based program: under the "
                       "causal Markov and faithfulness assumptions, conditional independence tests "
                       "reveal the graph up to Markov equivalence. Score-based methods search the "
                       "superexponential graph space, and Chickering 1996 proved the hardness is "
                       "fundamental. Extensions handle latent variables (FCI), cycles, and "
                       "non-Gaussianity (LiNGAM exploits non-Gaussian structure to orient edges). But "
                       "faithfulness is untestable and often violated, finite-sample tests err, and "
                       "equivalence classes leave edge directions unresolved. Practitioners want "
                       "discovery; theory offers partial identification plus strong assumptions, and the "
                       "distance between the two is the open problem."),
        "why_it_matters": ("If discovery worked, science could mine its vast observational archives for "
                           "causal structure instead of running one expensive experiment per question. "
                           "Genomics, economics, and climate science all sit on data that might contain "
                           "causal answers - if the extraction problem can be solved honestly."),
        "pointer": ("The Signature system proposes a labeled approach to this open problem - see the "
                    "companion Signature Edition record for the full step-by-step walkthrough. The "
                    "problem itself remains open in established science; no solution is claimed."),
        "sig_lens": ("The Signature lens reads discovery as a partial-knowledge problem: the honest "
                     "output is not a graph but the set of graphs the data cannot rule out. The "
                     "Signature approach reports the equivalence class with orientation confidence "
                     "scores, and prices every oriented edge by the assumption that oriented it."),
        "sig_solution": (
            LABEL + " Approach S-18: equivalence-class reporting with orientation pricing. "
            "Assumptions: (A1) constraint-based discovery reliably recovers the Markov equivalence "
            "class under faithfulness; (A2) each oriented edge can be traced to the specific "
            "assumption or test that oriented it; (A3) consumers prefer honest partial graphs over "
            "confident wrong ones. "
            "Reasoning path: (S1) run discovery and report the full equivalence class, not a single "
            "chosen DAG; (S2) attach to each oriented edge its provenance: which test, which "
            "assumption, what p-value; (S3) stress-test orientations by perturbing tests and checking "
            "stability; (S4) benchmark orientation accuracy on real systems with experimentally known "
            "graphs. "
            "Proposed mechanism: discovery output as a priced equivalence class, where every causal "
            "arrow carries its evidence receipt. "
            "What would confirm it: priced orientations proving more reliable than single-DAG outputs "
            "on benchmark systems. What would kill it: equivalence classes so large or orientations "
            "so unstable that the output is useless in practice. "
            "What it does NOT claim: a way past Markov equivalence from observational data alone, new "
            "hardness results, or peer acceptance. The identifiability wall stands; this is a proposed "
            "honesty discipline, honestly labeled."),
        "key_points": [
            "Spirtes, Glymour, Scheines: constraint-based discovery under Markov and faithfulness assumptions.",
            "Markov equivalence classes are indistinguishable from observational data alone.",
            "Chickering 1996: learning Bayesian networks is NP-hard - the hardness is fundamental.",
            "This walkthrough builds two DAGs with identical observational distributions: the data cannot tell them apart.",
            "Faithfulness is untestable and often violated; finite-sample tests err.",
        ],
        "requirements": [
            "Discovery output must include the full equivalence class, not a silently chosen DAG.",
            "Every oriented edge needs its provenance and stability score.",
            "Benchmarks need real systems with experimentally known graphs.",
            "The method must say what extra data would resolve the remaining orientations.",
        ],
        "standards": [
            "Spirtes P, Glymour C, Scheines R. Causation, Prediction, and Search; 2000.",
            "Chickering DM. Learning Bayesian networks is NP-hard; 1996.",
            "Standard: discovery reports the class and prices each orientation.",
        ],
        "citations": [CIT_SPIRTES, CIT_CHICKERING, CIT_PEARL],
    },
    {
        "key": "transportability",
        "name": "Transportability and External Validity",
        "group": "Compounded",
        "ladder_rank": 19,
        "ladder_tier": "compounded",
        "problem": ("A randomized trial proves a treatment works in its study population. Will it work "
                    "in yours? Populations differ in effect modifiers, and naive transport of the "
                    "average effect can be badly wrong. Pearl and Bareinboim 2011 gave a formal "
                    "transportability theory using selection diagrams, but general necessary and "
                    "sufficient conditions for transporting causal effects remain incomplete - the "
                    "open problem of external validity."),
        "background": ("Internal validity - did the study get its own answer right - has a mature "
                       "theory. External validity - does the answer travel - was long treated as "
                       "informal judgment about similarity. Pearl and Bareinboim 2011 formalized it: "
                       "given a selection diagram marking where populations differ, do-calculus "
                       "derives transport formulas that reweight the experimental result for the target "
                       "population. The machinery is elegant but demanding: it needs the selection "
                       "diagram, which encodes exactly the knowledge of how populations differ that "
                       "practitioners usually lack. Meta-analysis, generalizability weighting, and "
                       "effect-modifier transport each handle pieces. But a complete, usable account of "
                       "when effects transport - and what to do when the diagram is unknown - remains "
                       "open, even as medicine and policy constantly transport effects across "
                       "populations."),
        "why_it_matters": ("Every clinical guideline, every policy pilot, every A/B test transports an "
                           "effect from a study population to a decision population. Wrong transport "
                           "means treatments that fail in the real world and policies that backfire. A "
                           "complete transport theory would tell decision makers exactly what must be "
                           "measured to carry an effect safely across populations."),
        "pointer": ("The Signature system proposes a labeled approach to this open problem - see the "
                    "companion Signature Edition record for the full step-by-step walkthrough. The "
                    "problem itself remains open in established science; no solution is claimed."),
        "sig_lens": ("The Signature lens reads transport as a difference-ledger problem: the question "
                     "is never are populations similar but where exactly they differ. The Signature "
                     "approach builds the difference ledger explicitly and transports only through "
                     "measured differences, marking the rest as untransportable."),
        "sig_solution": (
            LABEL + " Approach S-19: difference-ledger transport. "
            "Assumptions: (A1) population differences relevant to the effect can be enumerated as "
            "candidate effect modifiers; (A2) the modifiers distributions are measurable in the "
            "target population; (A3) unmeasured modifiers make transport speculative, and the "
            "speculation must be labeled. "
            "Reasoning path: (S1) build the difference ledger: every known way the target population "
            "differs from the study population, with effect-modifier status assessed; (S2) transport "
            "through measured modifiers with reweighting, reporting the transported estimate; "
            "(S3) run sensitivity analysis over unmeasured modifiers to bound the transported effect; "
            "(S4) validate against cases where effects were transported and later measured in the "
            "target. "
            "Proposed mechanism: transport as explicit reweighting through a published difference "
            "ledger, with unmeasured differences priced by sensitivity bounds. "
            "What would confirm it: ledger-based transports predicting target-population effects better "
            "than naive transports in prospective tests. What would kill it: effect modifiers too "
            "numerous or unmeasurable to ledger, making every transport speculative. "
            "What it does NOT claim: a complete transportability theory, identification without "
            "difference knowledge, or peer acceptance. The theory stays incomplete; this is a proposed "
            "accounting discipline, honestly labeled."),
        "key_points": [
            "Internal validity has a mature theory; external validity was long informal judgment.",
            "Pearl and Bareinboim 2011: transportability via selection diagrams and do-calculus.",
            "The selection diagram encodes exactly the population-difference knowledge practitioners lack.",
            "This walkthrough transports an effect across populations with shifted modifiers: naive transport is biased, reweighted transport recovers.",
            "General necessary and sufficient transport conditions remain incomplete.",
        ],
        "requirements": [
            "The difference ledger must be built before transport, not after failure.",
            "Transported estimates need sensitivity bounds for unmeasured modifiers.",
            "Validation needs transported effects later measured in target populations.",
            "The method must say when transport should be refused.",
        ],
        "standards": [
            "Pearl J, Bareinboim E. Transportability of causal and statistical relations; 2011.",
            "Standard: transported effects report the difference ledger and sensitivity bounds.",
            "Standard: untransportable effects are labeled as such, not transported silently.",
        ],
        "citations": [CIT_PB, CIT_PEARL],
    },
    {
        "key": "interference",
        "name": "Causal Inference Under Interference",
        "group": "Compounded",
        "ladder_rank": 20,
        "ladder_tier": "compounded",
        "problem": ("Standard causal inference assumes SUTVA: one unit treatment does not affect "
                    "another unit outcome. Vaccines, social networks, and markets violate it "
                    "routinely - treating your neighbors changes your outcome. Hudgens and Halloran "
                    "2008 built foundations for causal effects under interference, but general "
                    "identification, efficient estimation, and design for network and spillover "
                    "settings remain wide open."),
        "background": ("Rubin potential-outcomes framework bakes in the stable unit treatment value "
                       "assumption: no interference between units and no hidden treatment versions. "
                       "Where interference is the phenomenon - herd immunity, peer effects, "
                       "marketplace spillovers - SUTVA is not an approximation but a falsehood. "
                       "Hudgens and Halloran 2008 defined direct, indirect, total, and overall effects "
                       "under interference within groups and gave randomization-based inference. Since "
                       "then the literature has grown: partial interference, network interference, "
                       "spatial spillovers. But each setting needs its own interference structure "
                       "assumed known, estimands proliferate, and general results - what is "
                       "identifiable under arbitrary interference, how to design experiments for it - "
                       "are missing. Most applied work still assumes SUTVA and hopes."),
        "why_it_matters": ("Vaccination policy, social programs, online platforms, and economic "
                           "interventions all operate through interference - the spillover IS the "
                           "effect of interest. Without a general interference theory, the most "
                           "consequential causal questions are answered with methods that assume the "
                           "phenomenon away."),
        "pointer": ("The Signature system proposes a labeled approach to this open problem - see the "
                    "companion Signature Edition record for the full step-by-step walkthrough. The "
                    "problem itself remains open in established science; no solution is claimed."),
        "sig_lens": ("The Signature lens reads interference as an exposure-mapping problem: the "
                     "treatment is not binary but a whole exposure pattern. The Signature approach "
                     "makes the exposure mapping explicit, estimates effects as functions of exposure, "
                     "and refuses SUTVA estimates where interference is detected."),
        "sig_solution": (
            LABEL + " Approach S-20: exposure-mapped interference analysis. "
            "Assumptions: (A1) interference travels through measurable channels - networks, groups, "
            "geography - that can be mapped; (A2) potential outcomes depend on a low-dimensional "
            "exposure summary, not the full treatment vector; (A3) interference can be detected from "
            "pilot or observational data before the main analysis. "
            "Reasoning path: (S1) map the interference channels and test for interference presence; "
            "(S2) define exposure mappings - e.g., own treatment plus fraction of treated neighbors - "
            "and state them explicitly; (S3) estimate direct and spillover effects as functions of "
            "exposure using design-based methods; (S4) validate on systems where interference was "
            "later measured directly. "
            "Proposed mechanism: interference analysis organized around explicit exposure mappings "
            "with SUTVA estimates flagged as invalid where interference is found. "
            "What would confirm it: exposure-mapped estimates matching directly measured spillovers "
            "better than SUTVA estimates. What would kill it: exposure depending on the full network "
            "in ways no low-dimensional mapping captures. "
            "What it does NOT claim: a general interference identification theory, a universal "
            "exposure mapping, or peer acceptance. The general theory stays open; this is a proposed "
            "mapping discipline, honestly labeled."),
        "key_points": [
            "SUTVA assumes no interference between units; vaccines, networks, and markets violate it.",
            "Hudgens and Halloran 2008: direct, indirect, total, and overall effects under interference.",
            "Each interference setting needs its own structure assumed known; no general theory exists.",
            "This walkthrough simulates spillover: the SUTVA estimator is biased, exposure-mapped estimation recovers the effects.",
            "Most applied work still assumes SUTVA and hopes.",
        ],
        "requirements": [
            "Interference channels must be mapped and tested, not assumed away.",
            "Exposure mappings must be stated explicitly before estimation.",
            "Estimands must match the decision: direct, spillover, and total effects reported separately.",
            "Validation needs systems with directly measured spillovers.",
        ],
        "standards": [
            "Hudgens MG, Halloran ME. Toward causal inference with interference; 2008.",
            "Standard: analyses report interference diagnostics and the assumed exposure mapping.",
            "Standard: SUTVA estimates are flagged invalid where interference is detected.",
        ],
        "citations": [CIT_HH, CIT_RUBIN74],
    },
    {
        "key": "publication_bias",
        "name": "Meta-Analysis Under Publication Bias",
        "group": "Compounded",
        "ladder_rank": 21,
        "ladder_tier": "compounded",
        "problem": ("Published studies are a selected sample: significant results get published, null "
                    "results sleep in file drawers. Meta-analyses that pool the published literature "
                    "therefore inflate effects. Trim-and-fill, selection models, and p-curve methods "
                    "try to correct the bias, but no debiasing method is a gold standard - the open "
                    "problem of honest evidence synthesis."),
        "background": ("Meta-analysis pools studies to estimate an effect, and under unbiased "
                       "publication it is close to the best evidence synthesis available. But "
                       "publication selects on significance, so the pool is enriched for inflated "
                       "effects - the funnel plot asymmetry that Egger and colleagues taught the field "
                       "to inspect. Corrections abound: trim-and-fill imputes missing studies, "
                       "selection models estimate the publication process jointly with the effect, "
                       "p-curve and p-uniform use only the significant p-values distribution. Each "
                       "works under assumptions about the selection mechanism that are themselves "
                       "untestable, and they famously disagree with each other. Registered reports and "
                       "pre-registration attack the source, but the vast published archive is already "
                       "selected, and synthesizing it honestly remains unsolved."),
        "why_it_matters": ("Clinical guidelines, policy reviews, and scientific consensus statements are "
                           "built on meta-analyses. If synthesis cannot correct publication bias "
                           "reliably, the evidence base of medicine and policy is systematically "
                           "optimistic. Honest synthesis would recalibrate what we think we know."),
        "pointer": ("The Signature system proposes a labeled approach to this open problem - see the "
                    "companion Signature Edition record for the full step-by-step walkthrough. The "
                    "problem itself remains open in established science; no solution is claimed."),
        "sig_lens": ("The Signature lens reads meta-analysis as a missing-data problem where the "
                     "missingness mechanism is the publication process itself. The Signature approach "
                     "fits the selection mechanism and the effect jointly, reports a family of "
                     "debiasing methods instead of one, and grades the synthesis by their agreement."),
        "sig_solution": (
            LABEL + " Approach S-21: ensemble debiasing with agreement grading. "
            "Assumptions: (A1) different debiasing methods fail in different ways, so their consensus "
            "is more trustworthy than any single method; (A2) the selection mechanism leaves "
            "detectable traces in funnel asymmetry and p-value distributions; (A3) syntheses must "
            "report what the unselected literature would need to look like to overturn them. "
            "Reasoning path: (S1) run a family of debiasing methods - selection models, p-curve, "
            "p-uniform, trim-and-fill - on the same literature; (S2) report the full range of "
            "adjusted estimates, not a chosen one; (S3) grade the synthesis by method agreement: "
            "tight agreement earns trust, wide disagreement earns a fragility flag; (S4) validate "
            "grades against literatures later completed by registered replications. "
            "Proposed mechanism: evidence synthesis as a debiasing ensemble with agreement grading, "
            "replacing single-method meta-analysis. "
            "What would confirm it: agreement grades predicting which meta-analytic conclusions "
            "survive unbiased replication. What would kill it: methods disagreeing everywhere, "
            "making every synthesis ungradeable. "
            "What it does NOT claim: a gold-standard debiasing method, recovery of the true effect "
            "from selected data, or peer acceptance. Honest synthesis stays open; this is a proposed "
            "ensemble discipline, honestly labeled."),
        "key_points": [
            "Publication selects significant results; meta-analyses of the published pool inflate effects.",
            "Funnel-plot asymmetry is the visible trace of the selection process.",
            "Trim-and-fill, selection models, p-curve, p-uniform: each corrects under untestable assumptions.",
            "This walkthrough simulates selective publication: the naive meta-mean inflates, debiasing methods disagree.",
            "No debiasing method is a gold standard.",
        ],
        "requirements": [
            "Syntheses must run multiple debiasing methods, not a chosen favorite.",
            "Method disagreement must be reported as fragility, not averaged away silently.",
            "Grades must be validated against later unbiased replication evidence.",
            "The synthesis must state what missing evidence would overturn it.",
        ],
        "standards": [
            "Egger M et al. Bias in meta-analysis detected by a simple graphical test; 1997.",
            "Standard: meta-analyses report a debiasing ensemble and an agreement grade.",
            "Standard: single-method syntheses are marked selection-uncorrected.",
        ],
        "citations": [CIT_IOANNIDIS, CIT_OSC],
    },
    {
        "key": "missing_data",
        "name": "Missing Data and Nonignorable Nonresponse",
        "group": "Compounded",
        "ladder_rank": 22,
        "ladder_tier": "compounded",
        "problem": ("Rubin 1976 classified missingness into MCAR, MAR, and MNAR. Under MAR, principled "
                    "methods like multiple imputation work; under MNAR - where missingness depends on "
                    "the missing values themselves - the observed data cannot identify the mechanism. "
                    "The open problem: credible inference under nonignorable nonresponse without "
                    "strong untestable assumptions."),
        "background": ("Missing data are everywhere: survey nonresponse, dropout in trials, sensor "
                       "gaps. Rubin 1976 gave the field its language: missing completely at random, "
                       "missing at random (missingness depends only on observed data), and missing not "
                       "at random, where it depends on what is missing - the classic example being "
                       "income nonresponse by high earners. Under MAR, likelihood and multiple "
                       "imputation are principled and standard. Under MNAR, identification fails "
                       "without extra assumptions: the data cannot distinguish a high-mean population "
                       "with random nonresponse from a low-mean one with selective nonresponse. "
                       "Pattern-mixture and selection models parameterize the untestable, and "
                       "sensitivity analyses map assumption to conclusion, but the core gap - "
                       "assumption-free credible inference under MNAR - is a theorem-shaped hole: it "
                       "cannot be filled, only honestly bounded."),
        "why_it_matters": ("Surveys, trials, and administrative data all suffer nonresponse, and the "
                           "nonresponse is usually related to what is missing - the sickest drop out, "
                           "the richest do not answer. If MNAR cannot be handled credibly, then "
                           "headline statistics from every survey rest on untestable assumptions nobody "
                           "states."),
        "pointer": ("The Signature system proposes a labeled approach to this open problem - see the "
                    "companion Signature Edition record for the full step-by-step walkthrough. The "
                    "problem itself remains open in established science; no solution is claimed."),
        "sig_lens": ("The Signature lens reads MNAR as a bounds problem, not an estimation problem: "
                     "the data identify a range, and any point inside is assumption. The Signature "
                     "approach computes the identified bounds honestly, prices every point estimate by "
                     "the assumption that selects it, and refuses to report precision the data do not "
                     "contain."),
        "sig_solution": (
            LABEL + " Approach S-22: identified-bounds reporting for MNAR. "
            "Assumptions: (A1) under MNAR the observed data identify bounds, not points, and the "
            "bounds are computable; (A2) subject-matter knowledge can sometimes narrow bounds "
            "credibly; (A3) decision-makers prefer honest wide bounds over precise fiction. "
            "Reasoning path: (S1) diagnose the missingness mechanism with all available evidence, "
            "stating the MNAR risk explicitly; (S2) compute nonparametric identified bounds for the "
            "target quantity; (S3) show how each candidate assumption - each selection model - picks "
            "a point inside the bounds, pricing the assumption; (S4) report the bounds as the headline "
            "with assumption-priced points as sensitivity analysis. "
            "Proposed mechanism: MNAR inference as bounds-first reporting, where precision beyond the "
            "bounds must be purchased with stated, priced assumptions. "
            "What would confirm it: bounds-based reports proving better calibrated than "
            "assumption-point reports in follow-up complete-data studies. What would kill it: bounds "
            "too wide for any decision use, forcing analysts back to hidden assumptions. "
            "What it does NOT claim: identification under MNAR, assumption-free inference, or peer "
            "acceptance. The hole stays a hole; this is a proposed honesty discipline, honestly "
            "labeled."),
        "key_points": [
            "Rubin 1976: MCAR, MAR, MNAR - the classification that organizes the field.",
            "Under MAR, multiple imputation is principled; under MNAR, the mechanism is unidentifiable.",
            "The data cannot distinguish high-mean random nonresponse from low-mean selective nonresponse.",
            "This walkthrough simulates MNAR income nonresponse: complete-case analysis is badly biased.",
            "Assumption-free credible MNAR inference is a theorem-shaped hole: it cannot be filled, only bounded.",
        ],
        "requirements": [
            "MNAR risk must be diagnosed and stated, not assumed away.",
            "Identified bounds must be computed nonparametrically where possible.",
            "Every point estimate inside the bounds must name and price its assumption.",
            "Bounds must be validated against later complete-data follow-ups.",
        ],
        "standards": [
            "Rubin DB. Inference and missing data; 1976.",
            "Standard: MNAR analyses headline identified bounds, not assumption-selected points.",
            "Standard: precision beyond the bounds requires stated, priced assumptions.",
        ],
        "citations": [CIT_RUBIN76],
    },
    {
        "key": "conformal",
        "name": "Conformal Prediction: Validity Versus Efficiency",
        "group": "Compounded",
        "ladder_rank": 23,
        "ladder_tier": "compounded",
        "problem": ("Vovk, Gammerman, and Shafer 2005 gave prediction a remarkable gift: conformal "
                    "prediction delivers finite-sample coverage guarantees with no distributional "
                    "assumptions. But validity is not efficiency - intervals can be valid and uselessly "
                    "wide. The open problem: how efficient can distribution-free prediction be, and "
                    "what is the optimal tradeoff between guaranteed coverage and sharp intervals?"),
        "background": ("Classical prediction intervals assume a model; when the model is wrong, "
                       "coverage fails. Conformal prediction changed the game: using only "
                       "exchangeability of the data, split-conformal and full-conformal methods produce "
                       "prediction sets with exact finite-sample marginal coverage. The guarantee is "
                       "real and assumption-free, which is why industry adopted it for ML uncertainty "
                       "quantification. But marginal coverage averages over the whole population - the "
                       "intervals can systematically undercover important subgroups, and conditional "
                       "coverage given the features is impossible in general (Barber and colleagues "
                       "2021). Efficiency - making the valid sets as small as possible - depends on the "
                       "underlying predictor and conformity score, and the optimal choice is open. The "
                       "field has validity solved and efficiency unsolved."),
        "why_it_matters": ("Machine learning systems need uncertainty they can stand behind: medical "
                           "diagnosis, autonomous driving, financial risk. Conformal prediction is the "
                           "closest thing to guaranteed uncertainty quantification in existence. Making "
                           "it efficient would give every ML deployment trustworthy, tight uncertainty "
                           "bounds."),
        "pointer": ("The Signature system proposes a labeled approach to this open problem - see the "
                    "companion Signature Edition record for the full step-by-step walkthrough. The "
                    "problem itself remains open in established science; no solution is claimed."),
        "sig_lens": ("The Signature lens reads conformal prediction as a solved-validity, open-"
                     "efficiency problem: the guarantee is banked, and the remaining work is making "
                     "the guaranteed sets small. The Signature approach treats efficiency as a "
                     "measurable engineering target with the validity guarantee held fixed."),
        "sig_solution": (
            LABEL + " Approach S-23: validity-fixed efficiency engineering. "
            "Assumptions: (A1) the marginal coverage guarantee must never be traded away for "
            "sharpness; (A2) conformity scores and underlying predictors can be optimized for "
            "efficiency while preserving validity; (A3) efficiency is measurable as mean set size at "
            "fixed coverage. "
            "Reasoning path: (S1) fix the coverage level and the validity proof as non-negotiable; "
            "(S2) optimize the conformity score - normalized, locally adaptive, quantile-based - for "
            "mean interval width on held-out data; (S3) report the efficiency frontier: width versus "
            "coverage across methods on benchmark tasks; (S4) probe subgroup coverage and flag where "
            "marginal validity hides conditional failure. "
            "Proposed mechanism: conformal prediction as an engineering discipline with validity "
            "locked and efficiency maximized, plus subgroup-coverage auditing. "
            "What would confirm it: optimized conformal variants delivering substantially tighter "
            "intervals at the same guaranteed coverage across benchmarks. What would kill it: "
            "efficiency gains proving illusory - merely shifting width between subgroups - or "
            "validity breaking under optimization pressure. "
            "What it does NOT claim: optimal efficiency theory, conditional coverage, or peer "
            "acceptance. The efficiency optimum stays open; this is a proposed engineering "
            "discipline, honestly labeled."),
        "key_points": [
            "Vovk, Gammerman, Shafer 2005: conformal prediction with finite-sample coverage, no distributional assumptions.",
            "The guarantee needs only exchangeability - the reason industry adopted it for ML uncertainty.",
            "Marginal coverage can hide subgroup undercoverage; conditional coverage is impossible in general.",
            "This walkthrough runs split-conformal regression: empirical coverage hits the nominal level.",
            "Validity is solved; efficiency - how small the valid sets can be - is the open problem.",
        ],
        "requirements": [
            "The coverage guarantee must be preserved exactly under any efficiency optimization.",
            "Efficiency must be measured as mean set size at fixed coverage on held-out data.",
            "Subgroup coverage must be audited wherever decisions affect subgroups differently.",
            "Benchmarks must cover real ML tasks, not just synthetic regressions.",
        ],
        "standards": [
            "Vovk V, Gammerman A, Shafer G. Algorithmic Learning in a Random World; 2005.",
            "Standard: conformal reports state coverage level, method, and mean set size together.",
            "Standard: subgroup coverage audits accompany any deployment claim.",
        ],
        "citations": [CIT_VOVK, CIT_BARBER],
    },
    {
        "key": "adaptive_analysis",
        "name": "Adaptive Data Analysis and the Reusable Holdout",
        "group": "Compounded",
        "ladder_rank": 24,
        "ladder_tier": "compounded",
        "problem": ("Analysts reuse the same holdout set adaptively: try a model, check the holdout, "
                    "tweak, repeat. Each adaptive query leaks information, and the holdout quietly "
                    "becomes training data - the Freedman paradox formalized. Dwork and colleagues "
                    "2015 used differential privacy to build a reusable holdout with provable "
                    "guarantees, but the optimal theory of adaptive data analysis - how many adaptive "
                    "queries a dataset can really support - remains open."),
        "background": ("Classical theory assumes the analysis is fixed before seeing the data; real "
                       "analysis is a conversation with the data. Freedman showed that screening "
                       "variables on the same data used for fitting produces spurious significance - "
                       "the paradox that launched a literature. The modern formulation: an analyst "
                       "makes adaptive queries, each depending on previous answers, and classical "
                       "guarantees degrade with adaptivity. Dwork, Feldman, Hardt, Pitassi, Reingold, "
                       "and Roth 2015 connected adaptivity to differential privacy: a mechanism that "
                       "answers queries privately generalizes, giving the reusable holdout - a test set "
                       "that survives adaptive reuse with provable bounds. Follow-up work tightened "
                       "bounds via max-information and monitor arguments, but the bounds are often "
                       "loose, the practical query budgets unclear, and the gap between theory and the "
                       "analyst actual practice remains wide."),
        "why_it_matters": ("Every data science workflow is adaptive: notebooks, dashboards, and leaderboards "
                           "all reuse data. If adaptivity silently invalidates results, then the standard "
                           "modern workflow is broken by default. A tight theory would tell practitioners "
                           "exactly how much adaptivity their data budget allows."),
        "pointer": ("The Signature system proposes a labeled approach to this open problem - see the "
                    "companion Signature Edition record for the full step-by-step walkthrough. The "
                    "problem itself remains open in established science; no solution is claimed."),
        "sig_lens": ("The Signature lens reads adaptivity as a spending problem: each adaptive query "
                     "spends some of the dataset information budget. The Signature approach gives "
                     "every analysis an explicit adaptivity budget, meters the spending, and refuses "
                     "further queries when the budget is exhausted."),
        "sig_solution": (
            LABEL + " Approach S-24: adaptivity budgeting with metering. "
            "Assumptions: (A1) adaptive queries can be logged and their information cost bounded via "
            "max-information or privacy-based arguments; (A2) analysts accept a finite query budget "
            "if the accounting is transparent; (A3) fresh data can replenish the budget. "
            "Reasoning path: (S1) log every adaptive query against the holdout in an analysis "
            "notebook; (S2) meter the cumulative adaptivity cost with the tightest available bounds; "
            "(S3) when the budget is exhausted, require fresh validation data before further claims; "
            "(S4) calibrate budgets empirically: how much adaptivity do real workflows actually use. "
            "Proposed mechanism: adaptive data analysis with an explicit, metered information budget "
            "per dataset. "
            "What would confirm it: budgeted workflows maintaining validity where unbudgeted ones "
            "overfit, in controlled comparisons. What would kill it: bounds too loose to give usable "
            "budgets, or analysts routing around the meter. "
            "What it does NOT claim: optimal adaptive query bounds, a tight general theory, or peer "
            "acceptance. The optimal theory stays open; this is a proposed accounting discipline, "
            "honestly labeled."),
        "key_points": [
            "Adaptive reuse of a holdout leaks information; the holdout quietly becomes training data.",
            "Freedman paradox: screening and fitting on the same data manufactures significance.",
            "Dwork et al. 2015: the reusable holdout via differential privacy, with provable guarantees.",
            "This walkthrough adaptively picks the best of 50 noise features: holdout accuracy inflates versus fresh data.",
            "Optimal bounds on how many adaptive queries data can support remain open.",
        ],
        "requirements": [
            "Query budgets must rest on the tightest available bounds, stated explicitly.",
            "The meter must capture real analyst behavior, including informal peeking.",
            "Budget exhaustion must trigger a fresh-data requirement, not a warning easily dismissed.",
            "Empirical calibration needs measurements of real workflow adaptivity.",
        ],
        "standards": [
            "Dwork C et al. The reusable holdout: preserving validity in adaptive data analysis; 2015.",
            "Standard: adaptive analyses report their query count and remaining budget.",
            "Standard: validity claims under adaptivity cite the bound used, not folklore.",
        ],
        "citations": [CIT_DWORK15, CIT_DWORKROTH],
    },
    {
        "key": "privacy_utility",
        "name": "Differential Privacy and the Utility Frontier",
        "group": "Compounded",
        "ladder_rank": 25,
        "ladder_tier": "compounded",
        "problem": ("Differential privacy gives a rigorous promise: one person data barely changes the "
                    "output. But privacy costs accuracy, and the exact shape of the privacy-utility "
                    "frontier - how much statistical utility must be sacrificed for a given privacy "
                    "level, and which estimators sit on the frontier - is unknown for most realistic "
                    "problems. The open problem: optimal private inference."),
        "background": ("Dwork and colleagues introduced differential privacy in 2006, and Dwork and Roth "
                       "2014 systematized it: the Laplace and Gaussian mechanisms, composition theorems "
                       "that bound privacy loss across analyses, and the exponential mechanism for "
                       "general selection. The framework is the gold standard for formal privacy, "
                       "deployed in the US Census and by major technology companies. But utility theory "
                       "lags: minimax rates under privacy constraints are known only for basic problems "
                       "- means, histograms, simple regression - and even there the optimal mechanisms "
                       "are recent and delicate. For complex models, adaptive analyses, and the "
                       "high-dimensional settings where privacy matters most, the frontier is unmapped. "
                       "Practitioners choose epsilon by convention, and nobody knows how much utility "
                       "they are leaving on the table."),
        "why_it_matters": ("Privacy-preserving data analysis is becoming legally and ethically "
                           "mandatory, from censuses to medical research to AI training. If we do not "
                           "know the frontier, we either overpay in accuracy - wasting data - or "
                           "underpay in privacy - wasting trust. Mapping the frontier tells society the "
                           "true price of privacy."),
        "pointer": ("The Signature system proposes a labeled approach to this open problem - see the "
                    "companion Signature Edition record for the full step-by-step walkthrough. The "
                    "problem itself remains open in established science; no solution is claimed."),
        "sig_lens": ("The Signature lens reads privacy-utility as a frontier-mapping problem: every "
                     "analysis should know where it sits relative to the best achievable. The Signature "
                     "approach requires the frontier to be measured on each problem and every deployed "
                     "mechanism to report its distance from it."),
        "sig_solution": (
            LABEL + " Approach S-25: frontier-measured private estimation. "
            "Assumptions: (A1) for a given problem the privacy-utility frontier can be bounded - lower "
            "bounds from minimax theory, upper bounds from candidate mechanisms; (A2) practitioners "
            "will pay for measured optimality; (A3) epsilon choices can be made by cost-benefit, not "
            "convention, once the frontier is visible. "
            "Reasoning path: (S1) for the estimation task, compute privacy-constrained lower bounds "
            "and the best known mechanism upper bound; (S2) deploy mechanisms with a reported "
            "frontier gap: how far from optimal this analysis sits; (S3) choose epsilon by explicit "
            "cost-benefit on the measured frontier; (S4) publish frontier measurements so the map "
            "grows with each deployment. "
            "Proposed mechanism: private estimation with mandatory frontier measurement and gap "
            "reporting. "
            "What would confirm it: measured frontiers guiding epsilon choices that dominate "
            "conventional ones on utility at equal privacy. What would kill it: frontiers too hard "
            "to bound for realistic problems, leaving gaps unmeasurable. "
            "What it does NOT claim: optimal private estimators in general, a mapped frontier, or peer "
            "acceptance. The frontier stays largely unmapped; this is a proposed measurement "
            "discipline, honestly labeled."),
        "key_points": [
            "Differential privacy: one person data barely changes the output - the rigorous privacy promise.",
            "Dwork and Roth 2014 systematized mechanisms, composition, and the foundations.",
            "Privacy costs accuracy; the exact frontier shape is unknown for most realistic problems.",
            "This walkthrough measures the Laplace-mechanism tradeoff: error falls as epsilon rises, exactly as theory predicts.",
            "Epsilon is usually chosen by convention; the utility left on the table is unknown.",
        ],
        "requirements": [
            "Frontier bounds must be computed per problem, not borrowed from toy settings.",
            "Deployed mechanisms must report their gap from the best known bound.",
            "Epsilon choices need cost-benefit justification on the measured frontier.",
            "Composition across full analysis pipelines must be accounted, not just single queries.",
        ],
        "standards": [
            "Dwork C, Roth A. The Algorithmic Foundations of Differential Privacy; 2014.",
            "Standard: private analyses report epsilon, mechanism, and frontier gap.",
            "Standard: privacy accounting covers the whole pipeline via composition.",
        ],
        "citations": [CIT_DWORKROTH, CIT_DWORK15],
    },
    {
        "key": "objective_bayes",
        "name": "Objective Bayes and Reference Priors",
        "group": "Compounded",
        "ladder_rank": 26,
        "ladder_tier": "compounded",
        "problem": ("Subjective priors embarrass Bayesians who want objectivity; flat priors are not "
                    "transformation-invariant and can behave badly. Jeffreys priors and Bernardo 1979 "
                    "reference priors aim at priors that let the data speak, with probability-matching "
                    "properties linking them to frequentist coverage. But whether objective Bayes is "
                    "coherent, truly objective, or the right default remains an open foundational "
                    "dispute."),
        "background": ("Jeffreys built priors from the Fisher information, gaining invariance under "
                       "reparameterization. Bernardo 1979 formalized reference priors as maximizing the "
                       "missing information - the prior that lets the data dominate asymptotically. "
                       "Probability-matching priors go further, calibrating Bayesian credible sets to "
                       "frequentist coverage to higher order. These are the workhorses of applied "
                       "Bayesian analysis, the defaults in software. Yet critics note the reference "
                       "prior depends on the parameter of interest and the model - hardly objective - "
                       "and that the whole program concedes the subjectivist premise it claims to "
                       "escape. The dispute matters because default priors decide the conclusions of "
                       "thousands of analyses whose users never chose a prior at all."),
        "why_it_matters": ("Default priors are the priors most analyses actually use. If objective "
                           "Bayes is sound, applied Bayesian inference has a principled default; if not, "
                           "the field leans on a philosophical fiction. Settling it decides what "
                           "Bayesian software should ship as the default."),
        "pointer": ("The Signature system proposes a labeled approach to this open problem - see the "
                    "companion Signature Edition record for the full step-by-step walkthrough. The "
                    "problem itself remains open in established science; no solution is claimed."),
        "sig_lens": ("The Signature lens reads objective Bayes as a default-warranty problem: the "
                     "software ships a prior the user never chose, so the prior needs a warranty. The "
                     "Signature approach tests the warranty empirically - calibration, matching, "
                     "robustness - and prints the results with the analysis."),
        "sig_solution": (
            LABEL + " Approach S-26: warranted-default priors. "
            "Assumptions: (A1) default priors can be graded by empirical performance: calibration of "
            "credible sets, probability matching, robustness across models; (A2) no default is "
            "universally best, so the warranty is conditional on problem class; (A3) users benefit "
            "from seeing the grade. "
            "Reasoning path: (S1) for each problem class, benchmark candidate defaults - Jeffreys, "
            "reference, weakly informative - on calibration and matching; (S2) ship the winner per "
            "class with its measured warranty: coverage accuracy, sensitivity range; (S3) where no "
            "default earns a warranty, require explicit prior choice; (S4) re-benchmark as theory "
            "and practice evolve. "
            "Proposed mechanism: default priors as warranted products with measured performance, "
            "replacing philosophical claims of objectivity with empirical grades. "
            "What would confirm it: warranted defaults delivering better-calibrated applied analyses "
            "than unwarranted ones. What would kill it: performance too problem-dependent for any "
            "default to warrant, or grades that mislead users into false confidence. "
            "What it does NOT claim: that objective priors are truly objective, a philosophical "
            "victory, or peer acceptance. The dispute stays open; this is a proposed empirical "
            "warranty discipline, honestly labeled."),
        "key_points": [
            "Jeffreys priors: built from Fisher information, invariant under reparameterization.",
            "Bernardo 1979 reference priors: maximize missing information, let the data dominate.",
            "Probability-matching priors calibrate Bayesian credible sets to frequentist coverage.",
            "This walkthrough tests Jeffreys Beta(0.5, 0.5) intervals: coverage lands near nominal across the parameter range.",
            "Whether objective Bayes is coherent or truly objective remains disputed.",
        ],
        "requirements": [
            "Default priors must be graded by measured calibration, not philosophical argument.",
            "Warranties must be conditional on problem class.",
            "Where no default is warranted, explicit prior choice must be required.",
            "Benchmarks must be re-run as methods evolve.",
        ],
        "standards": [
            "Bernardo JM. Reference posterior distributions for Bayesian inference; 1979.",
            "Standard: default priors ship with measured calibration warranties.",
            "Standard: unwarranted defaults are labeled as conventional, not objective.",
        ],
        "citations": [CIT_BERNARDO],
    },
    {
        "key": "evidence_foundations",
        "name": "Foundations of Statistical Evidence",
        "group": "Advanced",
        "ladder_rank": 27,
        "ladder_tier": "advanced",
        "problem": ("What is statistical evidence, and how is it measured? P-values, likelihood "
                    "ratios, Bayes factors, and e-values can disagree about the strength of the same "
                    "data - one calling it strong evidence, another weak. Safe testing with e-values "
                    "(Gruenwald, de Heide, Koolen 2024) offers anytime-valid evidence measurement, but "
                    "no unified account of evidence that all camps accept exists. The open problem: a "
                    "foundation for what counts as evidence."),
        "background": ("Fisher treated the p-value as evidence against the null; Neyman and Pearson "
                       "rebuilt testing as decision with error rates, explicitly not evidence. "
                       "Likelihoodists measure evidence in likelihood ratios; Bayesians in Bayes "
                       "factors, the ratio of marginal likelihoods. Each scale has pathologies: "
                       "p-values exaggerate, Bayes factors depend on priors, likelihood ratios ignore "
                       "stopping. E-values - nonnegative random variables with expectation at most one "
                       "under the null - give evidence a betting interpretation with anytime validity, "
                       "and safe testing builds a full theory on them. Yet the camps still talk past "
                       "each other: the same dataset can be strong evidence on one scale and weak on "
                       "another, and there is no accepted exchange rate between the currencies of "
                       "evidence."),
        "why_it_matters": ("Every scientific claim is a claim about evidence. Without a shared "
                           "foundation, fields cannot compare findings, combine studies, or even agree "
                           "on what was learned. A unified account of evidence would be the common "
                           "currency of science."),
        "pointer": ("The Signature system proposes a labeled approach to this open problem - see the "
                    "companion Signature Edition record for the full step-by-step walkthrough. The "
                    "problem itself remains open in established science; no solution is claimed."),
        "sig_lens": ("The Signature lens reads the evidence dispute as a missing-exchange-rate "
                     "problem: the currencies exist but cannot be converted. The Signature approach "
                     "builds the conversion table empirically - how p-values, Bayes factors, and "
                     "e-values map to each other and to real-world calibration - and requires multi-"
                     "currency reporting until one currency wins."),
        "sig_solution": (
            LABEL + " Approach S-27: multi-currency evidence reporting. "
            "Assumptions: (A1) no evidence scale will win by argument alone; adoption follows "
            "demonstrated calibration; (A2) the scales can be empirically calibrated against each "
            "other and against real outcomes; (A3) multi-currency reporting disciplines claims better "
            "than single-currency advocacy. "
            "Reasoning path: (S1) report p-value, Bayes factor, and e-value side by side for every "
            "major claim; (S2) build empirical conversion tables on benchmark problems with known "
            "truth; (S3) track which currency best predicts replication across fields; (S4) let the "
            "winning currency emerge from the track record, not from debate. "
            "Proposed mechanism: evidence as a multi-currency system with empirical exchange rates, "
            "replacing advocacy with measurement. "
            "What would confirm it: one currency systematically out-predicting the others on "
            "replication benchmarks. What would kill it: currencies disagreeing irreconcilably with "
            "no empirical way to choose, or all of them miscalibrated. "
            "What it does NOT claim: a true measure of evidence, a philosophical unification, or peer "
            "acceptance. The foundation stays open; this is a proposed measurement discipline, "
            "honestly labeled."),
        "key_points": [
            "P-values, likelihood ratios, Bayes factors, e-values: four currencies of evidence that can disagree.",
            "Fisher evidence versus Neyman-Pearson decision: the original split, never healed.",
            "Safe testing (Gruenwald, de Heide, Koolen 2024): e-values with anytime-valid guarantees.",
            "This walkthrough computes all three on the same data: the verdicts differ in strength.",
            "No accepted exchange rate exists between the currencies of evidence.",
        ],
        "requirements": [
            "Evidence scales must be compared on empirical calibration, not philosophical appeal.",
            "Conversion tables need benchmark problems with known ground truth.",
            "The track record must be replication prediction, the hardest test.",
            "Multi-currency reporting must be the norm until a winner emerges.",
        ],
        "standards": [
            "Gruenwald P, de Heide R, Koolen W. Safe testing; 2024.",
            "Standard: evidence claims report multiple scales until one is empirically vindicated.",
            "Standard: currencies are judged by replication prediction, not by tradition.",
        ],
        "citations": [CIT_GRUENWALD, CIT_ASA16, CIT_FISHER],
    },
    {
        "key": "generalized_bayes",
        "name": "Generalized Bayesian Inference Under Misspecification",
        "group": "Advanced",
        "ladder_rank": 28,
        "ladder_tier": "advanced",
        "problem": ("Standard Bayesian updating can be overconfident and miscalibrated when the model "
                    "is misspecified - the posterior concentrates, but on the wrong thing, with "
                    "false precision. Generalized Bayesian inference tempers the likelihood with a "
                    "learning rate, but choosing the rate is itself an open problem (Bissiri, Holmes, "
                    "Walker 2016; Gruenwald and van Ommen 2017 SafeBayes). The open problem: a "
                    "principled, automatic generalized Bayes for the misspecified world."),
        "background": ("Bayes rule is optimal when the model contains the truth; under "
                       "misspecification it minimizes a KL divergence but with credible sets that can "
                       "undercover badly - the posterior is sure and wrong. Bissiri, Holmes, and Walker "
                       "2016 generalized updating to arbitrary loss functions with a learning rate "
                       "controlling how aggressively the data move beliefs. Gruenwald and van Ommen "
                       "2017 SafeBayes chose the rate to optimize predictive performance, fixing the "
                       "hypercompression phenomenon where standard Bayes predicts worse than tempered "
                       "versions. But learning-rate selection remains heuristic: cross-validated, "
                       "SafeBayes-optimized, or set by theory that assumes what it needs. A fully "
                       "principled, automatic, calibrated generalized Bayes does not yet exist, even "
                       "though every real application is misspecified."),
        "why_it_matters": ("Bayesian methods are deployed on misspecified models everywhere - every "
                           "neural network posterior, every applied hierarchical model. If the updating "
                           "rule itself miscalibrates under misspecification, the uncertainty "
                           "statements of modern AI and applied Bayes are systematically overconfident. "
                           "A principled generalized Bayes would fix the update rule for the real "
                           "world."),
        "pointer": ("The Signature system proposes a labeled approach to this open problem - see the "
                    "companion Signature Edition record for the full step-by-step walkthrough. The "
                    "problem itself remains open in established science; no solution is claimed."),
        "sig_lens": ("The Signature lens reads tempering as a humility dial: standard Bayes is "
                     "maximum arrogance about the model, and the learning rate dials it down. The "
                     "Signature approach makes the dial data-driven, calibrates it on held-out "
                     "performance, and reports the chosen humility with every posterior."),
        "sig_solution": (
            LABEL + " Approach S-28: calibrated humility dialing. "
            "Assumptions: (A1) the learning rate can be selected by held-out predictive performance "
            "without circularity; (A2) tempered posteriors with well-chosen rates are better "
            "calibrated than standard ones under misspecification; (A3) reporting the rate makes "
            "the humility auditable. "
            "Reasoning path: (S1) fit the standard posterior and a ladder of tempered posteriors; "
            "(S2) select the learning rate by SafeBayes-style predictive criteria on held-out data; "
            "(S3) validate calibration - do tempered credible sets cover at nominal rates on real "
            "misspecified problems; (S4) report the rate, the calibration check, and the standard "
            "posterior as a sensitivity anchor. "
            "Proposed mechanism: generalized Bayes with a data-driven, calibrated, reported learning "
            "rate. "
            "What would confirm it: tempered posteriors systematically better calibrated than "
            "standard ones across misspecified benchmarks. What would kill it: rate selection "
            "proving unstable or circular, or tempering destroying the coherence properties that "
            "make Bayes attractive. "
            "What it does NOT claim: a principled automatic generalized Bayes, optimal rates, or peer "
            "acceptance. The problem stays open; this is a proposed calibration discipline, honestly "
            "labeled."),
        "key_points": [
            "Under misspecification, standard Bayes can be sure and wrong: tight posteriors, bad coverage.",
            "Bissiri, Holmes, Walker 2016: generalized updating with a learning rate for arbitrary losses.",
            "Gruenwald and van Ommen 2017 SafeBayes: choose the rate for predictive performance.",
            "This walkthrough fits a normal model to heavy-tailed data: standard credible sets undercover, tempered ones recover.",
            "Principled automatic learning-rate selection remains open.",
        ],
        "requirements": [
            "Rate selection must avoid circularity - it cannot assume the model it tempers.",
            "Calibration must be measured on real misspecified problems, not just theory.",
            "The coherence cost of tempering must be stated honestly.",
            "The standard posterior stays as a sensitivity anchor.",
        ],
        "standards": [
            "Bissiri PG, Holmes CC, Walker SG. A general framework for updating belief; 2016.",
            "Standard: tempered posteriors report the rate, its selection criterion, and a calibration check.",
            "Standard: humility is measured by held-out predictive performance.",
        ],
        "citations": [CIT_BISSIRI, CIT_GRUENWALD],
    },
    {
        "key": "uniform_bands",
        "name": "Honest Uniform Inference for Complex Estimators",
        "group": "Advanced",
        "ladder_rank": 29,
        "ladder_tier": "advanced",
        "problem": ("Pointwise confidence intervals cover at each point separately; a claim about a "
                    "whole function - a dose-response curve, a regression surface - needs uniform "
                    "coverage over all points simultaneously. Honest uniform bands exist for classical "
                    "smooth estimators, but Low impossibility results show adaptation and honesty "
                    "conflict over large function classes, and for modern machine-learning-based "
                    "estimators the theory is fragmentary. The open problem: honest uncertainty for "
                    "complex function estimates."),
        "background": ("Uniform confidence bands guarantee coverage of the entire unknown function "
                       "with stated probability - far stronger than pointwise intervals, which invite "
                       "cherry-picking of significant regions. Classical theory (Bickel and Rosenblatt, "
                       "Gine and Nickl) constructs honest bands for smooth function classes. But Low "
                       "1997 proved a fundamental limit: fully adaptive honest bands are impossible "
                       "over rich classes - you cannot have both optimal width and guaranteed coverage "
                       "without knowing the smoothness. Modern estimators - random forests, neural "
                       "nets, debiased ML - need uniform inference for their outputs, and the theory "
                       "for honest bands around them is incomplete. Practitioners plot pointwise "
                       "intervals and interpret them uniformly, which is exactly the error the theory "
                       "warns against."),
        "why_it_matters": ("Dose-response curves, heterogeneous treatment effects, and ML prediction "
                           "surfaces are functions, and decisions are made from their shapes - where "
                           "the curve rises, where it crosses zero. Pointwise intervals systematically "
                           "overstate confidence in shapes. Honest uniform bands would let science trust "
                           "what curves say."),
        "pointer": ("The Signature system proposes a labeled approach to this open problem - see the "
                    "companion Signature Edition record for the full step-by-step walkthrough. The "
                    "problem itself remains open in established science; no solution is claimed."),
        "sig_lens": ("The Signature lens reads uniform inference as a shape-warranty problem: the "
                     "analyst wants to warrant the shape, but only pointwise parts are warranted. The "
                     "Signature approach computes the honest uniform band wherever theory allows, "
                     "marks where Low impossibility bites, and refuses shape claims beyond the "
                     "warranty."),
        "sig_solution": (
            LABEL + " Approach S-29: warranted-shape reporting. "
            "Assumptions: (A1) honest uniform bands are computable for the estimator classes where "
            "theory exists; (A2) Low-type impossibility zones can be detected and marked; (A3) "
            "analysts will respect marked zones if the marking is automatic. "
            "Reasoning path: (S1) compute uniform bands by the sharpest honest method available for "
            "the estimator; (S2) run an impossibility audit: where does adaptation-with-honesty fail "
            "for this problem, and mark those regions; (S3) report shape claims - monotonicity, "
            "thresholds, peaks - only inside warranted zones; (S4) validate band coverage on "
            "simulated and real function-estimation benchmarks. "
            "Proposed mechanism: function estimates shipped with honest uniform bands and explicit "
            "impossibility markings, replacing pointwise plots interpreted uniformly. "
            "What would confirm it: warranted-shape reports avoiding the false shape discoveries that "
            "pointwise practice produces. What would kill it: impossibility zones covering everything "
            "of interest, leaving nothing warrantable. "
            "What it does NOT claim: a way around Low impossibility, honest adaptive bands in "
            "general, or peer acceptance. The impossibility stands; this is a proposed warranty "
            "discipline, honestly labeled."),
        "key_points": [
            "Pointwise intervals cover per point; uniform bands cover the whole function at once.",
            "Interpreting pointwise intervals as shape claims is the standard error.",
            "Low 1997: adaptive honest bands are impossible over rich classes - adaptation and honesty conflict.",
            "This walkthrough builds a uniform band for a CDF via DKW: whole-curve coverage holds.",
            "Honest uniform theory for ML-based estimators is fragmentary.",
        ],
        "requirements": [
            "Bands must be honest: uniform coverage proved or empirically validated.",
            "Impossibility zones must be marked, not silently crossed.",
            "Shape claims need warrant checks before publication.",
            "Validation needs function-estimation benchmarks with known truth.",
        ],
        "standards": [
            "Gine E, Nickl R. Mathematical Foundations of Infinite-Dimensional Statistical Models; 2016.",
            "Standard: function estimates report uniform bands or are marked pointwise-only.",
            "Standard: shape claims outside warranted zones are flagged unwarranted.",
        ],
        "citations": [CIT_GINENICKL],
    },
    {
        "key": "conditional_coverage",
        "name": "The Conditional Coverage Impossibility",
        "group": "Advanced",
        "ladder_rank": 30,
        "ladder_tier": "advanced",
        "problem": ("Conformal prediction guarantees marginal coverage: 90 percent of prediction "
                    "intervals cover, averaged over the population. But decision-makers need "
                    "conditional coverage: 90 percent coverage for people like this patient, this "
                    "applicant. Barber and colleagues 2021 proved exact conditional coverage is "
                    "impossible distribution-free. The open problem: what are the best achievable "
                    "relaxations, and which should practice adopt?"),
        "background": ("Marginal validity averages over regions where the predictor is accurate and "
                       "regions where it is not - the guarantee can hold overall while failing every "
                       "subgroup a decision-maker cares about. This is not a small blemish: in "
                       "heteroskedastic problems the intervals systematically undercover hard cases "
                       "and overcover easy ones. Barber, Candes, Ramdas, and Tibshirani 2021 proved "
                       "the impossibility is fundamental: no distribution-free method achieves "
                       "nontrivial conditional coverage. The field responded with relaxations: "
                       "group-conditional conformal (Mondrian), localized conformal weighting, "
                       "conditional calibration diagnostics. Each buys some conditionality at some "
                       "cost, and the map of what is achievable - the optimal relaxations - is still "
                       "being drawn."),
        "why_it_matters": ("Fairness and safety live in the conditional: a medical interval that "
                           "covers 90 percent overall but 70 percent for elderly patients is a "
                           "malfunction, not a success. Until conditional coverage is understood, "
                           "prediction intervals cannot be trusted where they matter most."),
        "pointer": ("The Signature system proposes a labeled approach to this open problem - see the "
                    "companion Signature Edition record for the full step-by-step walkthrough. The "
                    "problem itself remains open in established science; no solution is claimed."),
        "sig_lens": ("The Signature lens reads conditional coverage as a guarantee-grading problem: "
                     "marginal validity is grade C, and every deployment should know its grade. The "
                     "Signature approach audits conditional coverage across a battery of subgroups and "
                     "refuses deployment where the grades fail."),
        "sig_solution": (
            LABEL + " Approach S-30: coverage-grade auditing. "
            "Assumptions: (A1) conditional coverage can be audited on held-out data across many "
            "subgroups even though it cannot be guaranteed; (A2) the worst-subgroup shortfall is the "
            "right deployment metric; (A3) relaxations like group-conditional conformal improve the "
            "worst case measurably. "
            "Reasoning path: (S1) build prediction intervals by the best available method; (S2) audit "
            "coverage across a battery of subgroups, reporting the worst shortfall; (S3) apply "
            "relaxations - group-conditional, localized - and re-audit; (S4) set a deployment gate: "
            "no deployment where the worst audited subgroup falls below a stated floor. "
            "Proposed mechanism: prediction intervals shipped with a conditional-coverage audit and a "
            "deployment gate on the worst subgroup. "
            "What would confirm it: gated deployments showing fewer subgroup failures in production. "
            "What would kill it: audits too noisy to gate on, or relaxations that merely move "
            "undercoverage between subgroups. "
            "What it does NOT claim: a way around the impossibility theorem, conditional guarantees, "
            "or peer acceptance. The impossibility stands; this is a proposed auditing discipline, "
            "honestly labeled."),
        "key_points": [
            "Marginal coverage averages over easy and hard cases; subgroups can fail badly.",
            "Barber et al. 2021: exact distribution-free conditional coverage is impossible.",
            "This walkthrough builds heteroskedastic conformal intervals: marginal coverage holds while a subgroup undercovers.",
            "Relaxations exist: group-conditional, localized, and diagnostic approaches.",
            "The map of optimal achievable relaxations is still being drawn.",
        ],
        "requirements": [
            "Audits must cover subgroups decision-makers actually care about.",
            "The worst-subgroup shortfall is the headline metric, not the average.",
            "Relaxations must be compared on the audit battery, not on theory alone.",
            "Deployment gates need stated floors, not vague caution.",
        ],
        "standards": [
            "Barber RF et al. The limits of distribution-free conditional predictive inference; 2021.",
            "Standard: prediction intervals report subgroup coverage audits with the worst shortfall.",
            "Standard: impossibility is cited wherever conditional claims are refused.",
        ],
        "citations": [CIT_BARBER, CIT_VOVK],
    },
    {
        "key": "ergodicity",
        "name": "Ergodicity: Time Averages Versus Ensemble Averages",
        "group": "Advanced",
        "ladder_rank": 31,
        "ladder_tier": "advanced",
        "problem": ("Statistics optimizes expected values - ensemble averages over hypothetical "
                    "parallel worlds. But an individual lives one trajectory through time, and for "
                    "multiplicative dynamics the time average and the ensemble average disagree "
                    "violently. Peters 2019 argued economics chose the wrong average; the dispute "
                    "spills into statistics whenever expectations guide decisions for individuals. "
                    "The open problem: which average should statistics target?"),
        "background": ("The St. Petersburg paradox already showed expected value can mislead: infinite "
                       "expectation, yet no sane person pays much to play. Expected utility theory "
                       "patched it with concave utility, but Peters 2019 reopened the wound: for "
                       "multiplicative gambles, the ensemble-average growth rate is positive while "
                       "almost every individual trajectory decays to zero - the time average, what "
                       "anyone actually experiences, differs from the expectation. Ergodicity economics "
                       "proposes optimizing time-average growth instead. Statisticians object that "
                       "expectation remains the right target for repeatable decisions and risk pooling, "
                       "and that the dispute dissolves once the decision problem is stated precisely. "
                       "But applied statistics constantly prescribes expectation-optimal choices to "
                       "individuals facing multiplicative risk - investing, business bets, medical "
                       "gambles - where the ergodicity critique bites hardest, and no consensus "
                       "prescription exists."),
        "why_it_matters": ("If statistics targets the wrong average, its prescriptions can be optimal "
                           "on paper and ruinous in life - the classic multiplicative gamble enriches "
                           "the ensemble while bankrupting nearly every player. Getting the target "
                           "right changes advice on investing, insurance, and every risky decision an "
                           "individual faces once."),
        "pointer": ("The Signature system proposes a labeled approach to this open problem - see the "
                    "companion Signature Edition record for the full step-by-step walkthrough. The "
                    "problem itself remains open in established science; no solution is claimed."),
        "sig_lens": ("The Signature lens reads ergodicity as a whose-average problem: the analysis "
                     "must say whose experience it optimizes. The Signature approach computes both "
                     "averages for every risky prescription and flags every case where they disagree, "
                     "forcing the choice into the open."),
        "sig_solution": (
            LABEL + " Approach S-31: dual-average prescription auditing. "
            "Assumptions: (A1) for the decision at hand both the ensemble average and the time "
            "average (or its finite-horizon version) are computable; (A2) disagreement between them "
            "is the signal that the prescription needs scrutiny; (A3) stating whose average is "
            "optimized prevents the silent substitution. "
            "Reasoning path: (S1) for every expectation-based prescription, compute the "
            "time-average counterpart; (S2) flag disagreements - cases where the ensemble says go "
            "and the time average says stop; (S3) resolve flagged cases by stating the decision "
            "problem precisely: one-shot or repeated, pooled or individual risk; (S4) track real "
            "outcomes of flagged prescriptions to learn which average predicted lived experience. "
            "Proposed mechanism: risky prescriptions shipped with both averages and a disagreement "
            "flag, replacing silent ensemble optimization. "
            "What would confirm it: flagged prescriptions proving worse for individuals than "
            "unflagged ones in outcome tracking. What would kill it: the dispute dissolving in "
            "practice because decision problems are always stated precisely enough. "
            "What it does NOT claim: that time averages are always right, a refutation of expected "
            "utility, or peer acceptance. The dispute stays open; this is a proposed auditing "
            "discipline, honestly labeled."),
        "key_points": [
            "Ensemble average: mean over hypothetical parallel worlds. Time average: what one trajectory experiences.",
            "For multiplicative gambles they disagree: positive ensemble growth, almost-sure individual decay.",
            "Peters 2019: economics may have chosen the wrong average; ergodicity economics proposes time averages.",
            "This walkthrough simulates the classic gamble: the mean trajectory soars while the median collapses.",
            "No consensus prescription exists for which average statistics should target.",
        ],
        "requirements": [
            "Both averages must be computed for prescriptions involving multiplicative risk.",
            "Disagreements must trigger explicit decision-problem specification.",
            "Outcome tracking must compare flagged versus unflagged prescriptions.",
            "The analysis must state whose average is optimized: the individual or the ensemble.",
        ],
        "standards": [
            "Peters O. The ergodicity problem in economics; 2019.",
            "Standard: risky prescriptions report both averages and any disagreement flag.",
            "Standard: one-shot versus repeated framing must be stated, not assumed.",
        ],
        "citations": [CIT_PETERS],
    },
    {
        "key": "imprecise_prob",
        "name": "Imprecise Probabilities and Rival Foundations",
        "group": "Advanced",
        "ladder_rank": 32,
        "ladder_tier": "advanced",
        "problem": ("Kolmogorov axioms demand precise probabilities, but real uncertainty is often "
                    "imprecise: we know the bias is between 0.3 and 0.7, not that it is 0.5. Walley "
                    "1991 built statistical reasoning on lower and upper previsions; Dempster-Shafer "
                    "theory offers belief functions. The open problem: does precise probability "
                    "suffice, or do the foundations need imprecision - and if so, which rival "
                    "foundation is right?"),
        "background": ("The Bayesian response to ignorance is a prior: pick a distribution and update. "
                       "Critics reply that picking 0.5 when you know only the interval [0.3, 0.7] "
                       "manufactures information - precision without evidence. Walley 1991 "
                       "formalized imprecise probability via coherent lower previsions, generalizing "
                       "both Bayesian and frequentist ideas while representing ignorance honestly as "
                       "intervals. Dempster-Shafer theory, robust Bayes with prior classes, and "
                       "info-gap theory offer neighboring formalisms. Defenders of precision counter "
                       "that hierarchical Bayes already models uncertainty about parameters, and that "
                       "imprecision just pushes the precision up a level. The mathematics of each "
                       "rival is developed; what is missing is agreement on whether precise "
                       "probability is adequate and, if not, which imprecise foundation to adopt."),
        "why_it_matters": ("Expert elicitation, climate projections, and AI safety all face deep "
                           "uncertainty that resists precise quantification. If precise probability "
                           "forces false precision, decisions inherit invented numbers; if imprecision "
                           "is unnecessary, its intervals waste information. The foundation decides "
                           "how honestly uncertainty can be expressed."),
        "pointer": ("The Signature system proposes a labeled approach to this open problem - see the "
                    "companion Signature Edition record for the full step-by-step walkthrough. The "
                    "problem itself remains open in established science; no solution is claimed."),
        "sig_lens": ("The Signature lens reads imprecision as an honesty instrument: where knowledge "
                     "is genuinely interval-valued, the analysis should say so. The Signature approach "
                     "runs precise and imprecise analyses side by side and measures what the precision "
                     "costs in calibration."),
        "sig_solution": (
            LABEL + " Approach S-32: precision-cost measurement. "
            "Assumptions: (A1) precise and imprecise analyses can be run on the same problems; "
            "(A2) false precision has measurable costs in calibration and decision quality; (A3) "
            "the comparison can be made without settling the foundations. "
            "Reasoning path: (S1) for problems with genuinely interval-valued knowledge, compute the "
            "precise-Bayesian answer and the imprecise-probability bounds; (S2) measure the precision "
            "cost: where the precise answer is overconfident relative to later outcomes; (S3) "
            "catalog the problem types where imprecision changes decisions; (S4) let the measured "
            "costs, not philosophy, guide which foundation each problem class uses. "
            "Proposed mechanism: foundations chosen per problem class by measured precision cost, "
            "replacing the one-foundation-fits-all presumption. "
            "What would confirm it: problem classes where imprecise analyses are systematically better "
            "calibrated, justifying the foundation switch there. What would kill it: precise methods "
            "matching imprecise calibration everywhere, making imprecision pure overhead. "
            "What it does NOT claim: that Kolmogorov axioms are wrong, a winning rival foundation, or "
            "peer acceptance. The foundations dispute stays open; this is a proposed measurement "
            "discipline, honestly labeled."),
        "key_points": [
            "Precise probability can manufacture information: 0.5 pretends knowledge of [0.3, 0.7].",
            "Walley 1991: coherent lower and upper previsions as an imprecise foundation.",
            "Dempster-Shafer, robust Bayes, info-gap: neighboring formalisms for deep uncertainty.",
            "This walkthrough computes interval probabilities for an unknown-bias coin: honest ranges versus pretended points.",
            "No agreement on whether precision suffices or which rival to adopt.",
        ],
        "requirements": [
            "Comparisons must run precise and imprecise methods on identical problems.",
            "Precision cost must be measured in calibration against outcomes.",
            "Foundation choice per problem class needs the measured evidence, not advocacy.",
            "The analysis must handle the regress: uncertainty about the intervals themselves.",
        ],
        "standards": [
            "Walley P. Statistical Reasoning with Imprecise Probabilities; 1991.",
            "Standard: interval-valued knowledge is reported as intervals until precision is earned.",
            "Standard: foundation choice is justified by measured cost, not by tradition.",
        ],
        "citations": [CIT_WALLEY, CIT_GILLIES],
    },
    {
        "key": "anytime_inference",
        "name": "Anytime-Valid Inference for Arbitrary Models",
        "group": "Advanced",
        "ladder_rank": 33,
        "ladder_tier": "advanced",
        "problem": ("Classical inference is valid at a fixed, pre-chosen sample size; peeking breaks "
                    "it. Anytime-valid inference - e-values, test martingales, confidence sequences - "
                    "stays valid at arbitrary data-dependent stopping times. The theory works "
                    "beautifully for simple hypotheses, but extending anytime validity to arbitrary "
                    "models and parameters with good efficiency remains an open frontier."),
        "background": ("The peeking problem is old; the anytime solution is new. Robbins and Darling "
                       "built confidence sequences in the 1960s, but the modern revival came through "
                       "test martingales and e-values: wealth processes from betting against the null "
                       "that stay valid no matter when you stop looking. Ville inequality replaces the "
                       "fixed-sample union bound. The framework now covers means, quantiles, regression "
                       "coefficients, and more, with software appearing. But gaps remain: composite "
                       "nonparametric hypotheses, efficient anytime estimation (not just testing), "
                       "optimal betting strategies for complex models, and the practical question of "
                       "how much efficiency anytime validity costs versus fixed-sample methods. The "
                       "vision - all inference anytime-valid by default - is stated; the complete "
                       "theory is not."),
        "why_it_matters": ("Science runs on streaming data: trials with interim looks, dashboards, "
                           "continuous experimentation. If all inference were anytime-valid by default, "
                           "the peeking problem would dissolve and interim decisions would be safe. The "
                           "prize is a statistics that works the way the world actually collects data."),
        "pointer": ("The Signature system proposes a labeled approach to this open problem - see the "
                    "companion Signature Edition record for the full step-by-step walkthrough. The "
                    "problem itself remains open in established science; no solution is claimed."),
        "sig_lens": ("The Signature lens reads anytime validity as the natural contract for a "
                     "streaming world: the guarantee should hold whenever you ask, not only when you "
                     "promised to ask. The Signature approach builds every sequential analysis on "
                     "anytime instruments and prices the efficiency cost openly."),
        "sig_solution": (
            LABEL + " Approach S-33: anytime-by-default sequential analysis. "
            "Assumptions: (A1) e-value and martingale instruments exist or can be constructed for the "
            "parameters of interest; (A2) the efficiency cost of anytime validity is measurable and "
            "usually modest; (A3) analysts will adopt anytime methods if software makes them as easy "
            "as fixed-sample ones. "
            "Reasoning path: (S1) replace fixed-sample tests and intervals in sequential settings "
            "with e-value and confidence-sequence counterparts; (S2) measure the efficiency cost "
            "against fixed-sample methods on benchmark problems; (S3) extend the instrument library "
            "to the models practitioners actually fit; (S4) run adoption trials: do analysts reach "
            "correct conclusions faster and more safely. "
            "Proposed mechanism: sequential analysis rebuilt on anytime-valid instruments with openly "
            "priced efficiency costs. "
            "What would confirm it: anytime analyses matching fixed-sample correctness while "
            "permitting safe early stopping. What would kill it: efficiency costs too large for "
            "practical use, or models that resist anytime instrumentation. "
            "What it does NOT claim: a complete anytime theory for arbitrary models, optimal betting "
            "strategies in general, or peer acceptance. The frontier stays open; this is a proposed "
            "rebuilding discipline, honestly labeled."),
        "key_points": [
            "Classical inference is valid at a fixed sample size; peeking breaks it.",
            "E-values and test martingales stay valid at arbitrary stopping times via Ville inequality.",
            "Confidence sequences are intervals valid at all times simultaneously.",
            "This walkthrough runs an e-value test stopped at a random time: validity holds anyway.",
            "Extension to arbitrary models with good efficiency is the open frontier.",
        ],
        "requirements": [
            "Anytime instruments must be constructed for the models practitioners fit.",
            "Efficiency costs versus fixed-sample methods must be measured openly.",
            "Software must make anytime methods as easy as classical ones.",
            "Adoption trials must show faster, safer conclusions.",
        ],
        "standards": [
            "Gruenwald P, de Heide R, Koolen W. Safe testing; 2024.",
            "Standard: sequential analyses use anytime-valid instruments by default.",
            "Standard: efficiency costs are priced, not hidden.",
        ],
        "citations": [CIT_GRUENWALD, CIT_ARMITAGE],
    },
    {
        "key": "unification",
        "name": "The Unification Problem: One Framework for All Inference",
        "group": "Advanced",
        "ladder_rank": 34,
        "ladder_tier": "advanced",
        "problem": ("Frequentist, Bayesian, and fiducial inference give different answers to what an "
                    "uncertainty statement means, and the schools have fought for a century. "
                    "Confidence distributions (Xie and Singh 2013) and generalized fiducial inference "
                    "try to bridge them: a distribution on the parameter space with frequentist "
                    "validity that often matches Bayesian posteriors. The open problem: a single "
                    "accepted framework unifying the schools - or proof that none exists."),
        "background": ("Fisher fiducial argument tried to get posterior-like statements without "
                       "priors and collapsed under paradoxes. Neyman confidence intervals kept "
                       "frequentist validity but lost the distributional statement. Confidence "
                       "distributions revive the distribution-on-parameter idea with rigorous "
                       "frequentist definitions: a sample-dependent distribution whose quantiles are "
                       "confidence intervals at all levels (Xie and Singh 2013 review). Generalized "
                       "fiducial inference (Hannig and colleagues) gives a modern fiducial recipe with "
                       "asymptotic validity. In many standard problems the confidence distribution, "
                       "the fiducial distribution, and the Bayesian posterior with flat prior coincide "
                       "numerically - a striking convergence. But the interpretations still differ, "
                       "counterexamples separate the frameworks, and no unification commands assent. "
                       "The deepest open question in statistical foundations may be whether the "
                       "schools describe one thing or three."),
        "why_it_matters": ("A century of foundational warfare has real costs: confused teaching, "
                           "incompatible software defaults, and practitioners who pick a school by "
                           "tribe rather than fit. A true unification would end the war and give "
                           "statistics a single coherent story about uncertainty. Proof of impossibility "
                           "would be almost as valuable: it would license pluralism honestly."),
        "pointer": ("The Signature system proposes a labeled approach to this open problem - see the "
                    "companion Signature Edition record for the full step-by-step walkthrough. The "
                    "problem itself remains open in established science; no solution is claimed."),
        "sig_lens": ("The Signature lens reads unification as a convergence-accounting problem: the "
                     "frameworks already agree numerically on wide territory, and the honest work is "
                     "mapping exactly where they agree, where they diverge, and what each divergence "
                     "costs. The Signature approach builds the agreement map and treats it as the "
                     "proto-unification."),
        "sig_solution": (
            LABEL + " Approach S-34: agreement-map proto-unification. "
            "Assumptions: (A1) the frameworks numerical agreement on standard problems is extensive "
            "enough to map; (A2) divergences cluster at identifiable features - priors, stopping "
            "rules, parameterizations; (A3) an explicit agreement map is useful even without a "
            "unified theory. "
            "Reasoning path: (S1) compute confidence, fiducial, and Bayesian answers across a "
            "benchmark of problems and map where they coincide; (S2) characterize each divergence by "
            "its cause: which assumption drives it; (S3) test whether divergences matter for "
            "decisions or are philosophical only; (S4) publish the map as the working proto-"
            "unification, updated as theory advances. "
            "Proposed mechanism: unification pursued as explicit agreement mapping rather than "
            "philosophical victory, with divergences priced by decision impact. "
            "What would confirm it: the map showing agreement almost everywhere that matters, "
            "deflating the war; or sharp decision-relevant divergences, licensing honest pluralism. "
            "What would kill it: agreement too fragile to map, or camps rejecting the map exercise. "
            "What it does NOT claim: a unified framework, an impossibility proof, or peer acceptance. "
            "The deepest open question in statistical foundations stays open; this is a proposed "
            "mapping discipline, honestly labeled."),
        "key_points": [
            "Fisher fiducial argument collapsed; Neyman kept validity but lost the parameter distribution.",
            "Confidence distributions (Xie and Singh 2013): frequentist distributions on the parameter space.",
            "Generalized fiducial inference gives a modern fiducial recipe with asymptotic validity.",
            "This walkthrough computes all three for a normal mean: the answers coincide - the striking convergence.",
            "No unification commands assent; the schools may describe one thing or three.",
        ],
        "requirements": [
            "The agreement map must cover benchmark problems across the frameworks.",
            "Each divergence needs its cause identified: prior, stopping rule, or parameterization.",
            "Decision relevance of divergences must be tested, not assumed.",
            "The map must be maintained as theory advances.",
        ],
        "standards": [
            "Xie M, Singh K. Confidence distribution: a review; 2013.",
            "Standard: framework comparisons report the agreement map, not tribal verdicts.",
            "Standard: divergences are priced by decision impact.",
        ],
        "citations": [CIT_XIESINGH, CIT_NEYMAN],
    },
];
