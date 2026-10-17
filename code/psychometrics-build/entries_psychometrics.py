#!/usr/bin/env python3
"""Entries for the Psychometrics field databases (field #19, taxonomy order).

Verified 2026-10-17: NO database covers psychometrics as a discipline.
- 'psychology' / 'psychology-public' / 'psychology-signature':
  no shard data or generic survey cards; zero psychometrics-discipline titles.
- 'psychology-study' (5000 records) / 'everything-psychology' (12 records):
  whole-shard title scan - zero hits for psychometric(s), item response,
  classical test theory, Cronbach, kappa, differential item functioning,
  equating, adaptive testing, norming, factor analysis, reliability,
  validity as a measurement discipline. Generic "testing" mentions nowhere
  rise to the discipline: no true-score model, no IRT, no test construction.
- Fields #12-18 shard indexes (climatology, atmospheric-science, hydrology,
  meteorology, calculus, combinatorics, econometrics): direct title scan -
  only false positives on the substring "equat" inside "equation".
- 'scientific-formulas': bare formula cards are reference only (task
  instruction: formula cards do NOT count as discipline coverage).
- Whole-system dedupe gate (fresh data/dedupe/exact/ index in the main
  repo): every record checked + admitted at build time.

So this build creates two NEW databases, 37 ladder-ordered records each:

  psychometrics            - The Psychometrics Database
                             (public-harvest: real, fact-checked
                             psychometrics; citations Nunnally & Bernstein,
                             Embretson & Reise, DeVellis, Furr & Bacharach,
                             Crocker & Algina, Hambleton et al., Anastasi &
                             Urbina, Brennan, Kline, and the Standards for
                             Educational and Psychological Testing)
  psychometrics-signature  - The Psychometrics Signature Database
                             (his original Signature interpretation of the
                             discipline; src signature, titles suffixed
                             " (Signature Edition)", never presented as
                             authentic public record)

Subtitle disambiguation (fields #13-19 pattern): discipline titles carry
teaching-focused subtitles rather than bare cards, e.g. "Reliability: The
Signal in the Noise" and "Cronbach's Alpha: The Workhorse of Internal
Consistency".
"""

SIG_TAIL = ("Signature original - his original Signature interpretation of "
            "psychometrics, clearly labeled Signature-made, never presented "
            "as authentic public record.")

C_NUNNALLY = ("Nunnally, Jum C. and Bernstein, Ira H. 'Psychometric Theory', "
              "3rd ed. McGraw-Hill, 1994.")
C_EMBRETSON = ("Embretson, Susan E. and Reise, Steven P. 'Item Response "
               "Theory for Psychologists'. Lawrence Erlbaum, 2000.")
C_DEVELLIS = ("DeVellis, Robert F. 'Scale Development: Theory and "
              "Applications', 4th ed. Sage, 2016.")
C_FURR = ("Furr, R. Michael and Bacharach, Verne R. 'Psychometrics: An "
          "Introduction', 2nd ed. Sage, 2014.")
C_STANDARDS = ("American Educational Research Association, American "
               "Psychological Association, & National Council on Measurement "
               "in Education. 'Standards for Educational and Psychological "
               "Testing'. AERA, 2014.")
C_CROCKER = ("Crocker, Linda and Algina, James. 'Introduction to Classical "
             "and Modern Test Theory'. Holt, Rinehart and Winston, 1986.")
C_HAMBLETON = ("Hambleton, Ronald K., Swaminathan, Hariharan, and Rogers, H. "
               "Jane. 'Fundamentals of Item Response Theory'. Sage, 1991.")
C_ANASTASI = ("Anastasi, Anne and Urbina, Susana. 'Psychological Testing', "
              "7th ed. Prentice Hall, 1997.")
C_BRENNAN = ("Brennan, Robert L. 'Generalizability Theory'. Springer, 2001.")
C_KLINE = ("Kline, Rex B. 'Principles and Practice of Structural Equation "
           "Modeling', 4th ed. Guilford Press, 2016.")
C_THORNDIKE = ("Thorndike, Robert L. and Thorndike-Christ, Tracy. "
               "'Measurement and Evaluation in Psychology and Education', "
               "8th ed. Pearson, 2010.")
C_WECHSLER = ("Wechsler, David. 'Wechsler Adult Intelligence Scale - Fourth "
              "Edition (WAIS-IV)'. Pearson, 2008.")
C_MMPI = ("Butcher, James N. et al. 'Minnesota Multiphasic Personality "
          "Inventory-2 (MMPI-2)'. University of Minnesota Press, 2001.")
C_COSTA = ("Costa, Paul T. and McCrae, Robert R. 'Revised NEO Personality "
           "Inventory (NEO PI-R)'. Psychological Assessment Resources, 1992.")

ENTRIES = [
    {
        "key": "what_is_psychometrics",
        "name": "What Psychometrics Is: The Science of Psychological Measurement",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "Psychometrics is the scientific discipline devoted to measuring "
            "things you cannot see directly: intelligence, personality traits, "
            "attitudes, aptitudes, knowledge, and clinical symptoms. Nobody "
            "can put a ruler against 'anxiety' or weigh 'verbal reasoning', "
            "so psychometrics builds the instruments - tests, scales, "
            "questionnaires, performance tasks - and then proves, with "
            "mathematics, that those instruments actually measure what they "
            "claim to measure and do so consistently. The field's two great "
            "questions are reliability (does the instrument give stable, "
            "repeatable results?) and validity (does it measure the right "
            "thing?). Its two great theoretical frameworks are classical "
            "test theory, born from Spearman's true-score model of 1904, and "
            "item response theory, the modern probabilistic framework behind "
            "adaptive testing. Every high-stakes decision that rests on a "
            "test score - college admission, job hiring, clinical diagnosis, "
            "licensing exams - stands or falls on psychometrics."
        ),
        "how_it_works": (
            "Psychometrics works by treating unobservable traits (latent "
            "variables) as quantities that reveal themselves through "
            "observable responses. A test designer writes items - questions, "
            "tasks, rating statements - each designed to be a small window "
            "onto the trait. Responses are scored and aggregated into a test "
            "score, and then the machinery of the field goes to work: "
            "reliability analysis asks how much of the score's variation is "
            "signal versus noise; validity studies ask whether the score "
            "predicts, converges with, and is distinct from what theory says "
            "it should be; item analysis examines each item's difficulty and "
            "discriminating power; factor analysis checks whether the items "
            "hang together the way the theory claims; norming places each "
            "score on a common scale so it can be interpreted. The result is "
            "not just a number but a number with a documented margin of "
            "error, a documented meaning, and documented limits - which is "
            "what separates a psychometric instrument from a quiz."
        ),
        "key_points": [
            "Psychometrics measures latent traits - intelligence, personality, attitudes, aptitudes - through observable test responses.",
            "Its two master questions are reliability (consistency of measurement) and validity (accuracy of interpretation).",
            "Classical test theory (Spearman, 1904) and item response theory are the field's two great frameworks.",
            "A test score is never just a number: it carries a margin of error, a meaning, and documented limits.",
            "Every high-stakes use of test scores - admissions, hiring, diagnosis, licensing - rests on psychometric evidence.",
        ],
        "requirements": [
            "No prior background needed - this is the first rung of the ladder.",
            "Comfort with the idea that invisible traits can be measured indirectly.",
            "Basic arithmetic; the mathematics builds gently from here.",
        ],
        "standards": [
            "Language follows the Standards for Educational and Psychological Testing (AERA/APA/NCME, 2014).",
            "Latent-trait language is used precisely: traits are inferred, responses are observed.",
        ],
        "citations": [C_FURR, C_ANASTASI, C_STANDARDS],
        "sig_lens": (
            "Signature take: measurement is how the invisible becomes actionable. "
            "His Signature framing treats every psychometric instrument as a "
            "bridge between the unobservable mind and decisions that must be "
            "defensible - the same bridge his whole Signature system walks."
        ),
    },
    {
        "key": "measurement_scales",
        "name": "Levels of Measurement: Nominal, Ordinal, Interval, Ratio",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "Before a single test is scored, psychometrics asks what kind of "
            "numbers the scores are. S. S. Stevens' 1946 classification gives "
            "four levels of measurement, and each level permits different "
            "mathematics. Nominal scales are labels (diagnostic categories, "
            "answer options A/B/C/D) - you may count them but never average "
            "them. Ordinal scales rank (Likert 'agree' scales, class rank) - "
            "order is meaningful but the gaps between steps are not equal. "
            "Interval scales have equal gaps but no true zero (most "
            "psychological test scores, temperature in Celsius) - differences "
            "are meaningful but ratios are not. Ratio scales add a true zero "
            "(reaction time, number of items correct) - ratios are "
            "meaningful. Misclassifying the scale is the original sin of "
            "measurement: averaging nominal codes, or treating ordinal "
            "Likert points as if 'strongly agree' were exactly twice 'agree', "
            "smuggles mathematics the data cannot support."
        ),
        "how_it_works": (
            "The levels work by specifying which transformations leave the "
            "scale's meaning intact. Nominal scales survive any one-to-one "
            "relabeling; ordinal scales survive any order-preserving "
            "transformation; interval scales survive linear shifts and "
            "rescalings (add a constant, multiply by a constant); ratio "
            "scales survive only multiplication by a positive constant. This "
            "is why the mean of a nominal code is meaningless - relabel the "
            "categories and the 'mean' changes, so it was never a property of "
            "the data. In practice, psychometrics lives mostly on ordinal "
            "and interval ground: Likert ratings are strictly ordinal, but "
            "summed Likert scales with many items are routinely treated as "
            "approximately interval - a pragmatic compromise the field "
            "debates openly. Item response theory earns its keep here by "
            "building genuinely interval-level ability scales from ordinal "
            "item responses."
        ),
        "key_points": [
            "Nominal: labels only - count them, never average them.",
            "Ordinal: order matters, gaps do not - medians are safe, means are suspect.",
            "Interval: equal gaps, no true zero - differences meaningful, ratios not.",
            "Ratio: true zero - ratios meaningful (reaction time, counts correct).",
            "The admissible statistics follow the scale; misclassification smuggles in unsupported math.",
        ],
        "requirements": [
            "Familiarity with mean, median, and mode.",
            "Willingness to question whether a number can be averaged.",
        ],
        "standards": [
            "Stevens (1946) scale taxonomy used as the reference frame.",
            "Scale claims for any instrument must be stated before statistics are chosen.",
        ],
        "citations": [C_FURR, C_THORNDIKE],
        "sig_lens": (
            "Signature take: every number in his system must know what kind "
            "of number it is before it is allowed to do arithmetic. Scale "
            "discipline is Signature discipline."
        ),
    },
    {
        "key": "true_score_model",
        "name": "The True-Score Model: X = T + E",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "The founding equation of psychometrics, due to Charles Spearman "
            "in 1904: every observed test score X equals a true score T plus "
            "a random error E. The true score is not some metaphysical ideal "
            "- it is defined precisely as the average score a person would "
            "get over infinitely many independent administrations of the "
            "test. The error is everything random that pushes a particular "
            "administration away from that average: a lucky guess, a bad "
            "night's sleep, a misread question, a noisy room. Three "
            "assumptions complete the model: errors average to zero across "
            "people, errors are uncorrelated with true scores, and errors on "
            "different administrations are uncorrelated with each other. "
            "From these spare assumptions flows the entire classical theory: "
            "reliability, the standard error of measurement, the "
            "Spearman-Brown formula, and the correction for attenuation all "
            "grow from X = T + E."
        ),
        "how_it_works": (
            "The model works by splitting observed-score variance into two "
            "piles: Var(X) = Var(T) + Var(E), because the assumptions make "
            "the cross-term vanish. Reliability is then defined as the "
            "fraction of observed variance that is true-score variance: "
            "Var(T)/Var(X) - a number between 0 and 1 that says what share "
            "of the score differences between people is real rather than "
            "noise. The beauty of the model is that the true score is never "
            "observed, yet its variance can be estimated: give the same "
            "people two parallel forms of a test, and the correlation "
            "between the forms estimates reliability directly, because the "
            "only thing two independent administrations share is the true "
            "score. Everything in classical test theory is bookkeeping on "
            "this split between signal and noise."
        ),
        "key_points": [
            "X = T + E: observed score equals true score plus random error (Spearman, 1904).",
            "True score is defined operationally: the mean over infinite independent administrations.",
            "Var(X) = Var(T) + Var(E): observed variance splits into signal and noise.",
            "Reliability = Var(T)/Var(X): the share of score variance that is real.",
            "Parallel forms correlate at exactly the reliability - the unobservable becomes estimable.",
        ],
        "requirements": [
            "Variance as 'average squared spread' (reintroduced in the demo).",
            "Correlation as 'how two variables move together'.",
        ],
        "standards": [
            "Classical test theory axioms stated in Spearman's original form.",
            "True score defined operationally, never metaphysically.",
        ],
        "citations": [C_NUNNALLY, C_CROCKER],
        "sig_lens": (
            "Signature take: every measurement his system ever takes is a "
            "true signal wearing a noise costume. X = T + E is the master "
            "key: separate them, and the data starts telling the truth."
        ),
    },
    {
        "key": "reliability_intro",
        "name": "Reliability: The Signal in the Noise",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "Reliability is the degree to which a test gives consistent, "
            "repeatable results - the same person, measured again under the "
            "same conditions, should get essentially the same score. A "
            "bathroom scale that reads 150 pounds, then 170, then 140 is "
            "unreliable no matter how fancy its display; a psychological "
            "test with the same temperament is equally useless. Reliability "
            "is quantified as a coefficient between 0 and 1, where 1 means "
            "all observed-score variance is true-score variance and 0 means "
            "the scores are pure noise. The field's rule-of-thumb floors are "
            "famous: around 0.70 for research instruments, 0.80 for "
            "instruments used in applied decisions about individuals, and "
            "0.90 or higher for high-stakes individual decisions like "
            "clinical diagnosis. But the deepest fact about reliability is "
            "this: it is a property of scores in a particular population, "
            "not a permanent property of the test. The same test can be "
            "highly reliable in a diverse sample and nearly unreliable in a "
            "restricted, homogeneous one."
        ),
        "how_it_works": (
            "Reliability is estimated by correlating two measurements that "
            "share only the true score. The classic designs: test-retest "
            "(same test, two occasions - confounded by memory and real "
            "change), parallel or alternate forms (two equivalent versions - "
            "the gold standard, expensive to build), split-half (correlate "
            "two halves of one test, then step up with Spearman-Brown), and "
            "internal consistency (Cronbach's alpha, KR-20 - how tightly the "
            "items hang together). Each design catches different error: "
            "test-retest catches instability over time, alternate forms "
            "catch item-sampling error, internal consistency catches "
            "item heterogeneity. Because reliability equals Var(T)/Var(X), "
            "anything that shrinks true-score variance - like selecting an "
            "elite, homogeneous group - mechanically shrinks reliability "
            "even though the test is unchanged. This is the restriction-of-"
            "range effect, and it explains many 'the test stopped working' "
            "mysteries."
        ),
        "key_points": [
            "Reliability is consistency of scores; the coefficient runs 0 (pure noise) to 1 (pure signal).",
            "Floors of thumb: 0.70 research, 0.80 applied decisions, 0.90 high-stakes individual calls.",
            "Four estimation designs: test-retest, alternate forms, split-half, internal consistency - each catches different error.",
            "Reliability belongs to scores-in-a-population, not to the test as an object.",
            "Restriction of range shrinks reliability without changing the test at all.",
        ],
        "requirements": [
            "The true-score model (previous rung).",
            "Correlation between 0 and 1 as a similarity measure.",
        ],
        "standards": [
            "Reliability reported with the estimation design named, per the Standards (2014).",
            "Coefficient thresholds presented as conventions, not laws.",
        ],
        "citations": [C_NUNNALLY, C_ANASTASI, C_STANDARDS],
        "sig_lens": (
            "Signature take: consistency is the first Signature virtue. A "
            "system that cannot reproduce its own measurements cannot be "
            "trusted with decisions - reliability is trust, quantified."
        ),
    },
    {
        "key": "test_retest",
        "name": "Test-Retest Reliability: Stability Across Time",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "Test-retest reliability is the simplest reliability design to "
            "understand: give the same test to the same people on two "
            "occasions, and correlate the two sets of scores. The "
            "correlation is the reliability coefficient - it estimates how "
            "much of the score variance is stable true-score variance "
            "rather than occasion-specific noise. The design's honesty is "
            "also its weakness. Between the two occasions, people genuinely "
            "change (moods shift, skills grow), remember the items (practice "
            "effects inflate the second score), and react to being tested "
            "twice (reactivity). A short interval inflates reliability "
            "through memory; a long interval deflates it through real "
            "change. That is why test-retest is the right design for stable "
            "traits like general cognitive ability - where retest "
            "correlations over years run 0.80 to 0.90 - and the wrong design "
            "for states like anxiety, where low retest correlation may "
            "simply mean the trait itself moved."
        ),
        "how_it_works": (
            "The method works because the true-score model splits each "
            "occasion's score into a stable true component plus "
            "occasion-specific error: X1 = T + E1, X2 = T + E2. If the trait "
            "is stable (T unchanged) and errors are independent across "
            "occasions, the correlation between X1 and X2 equals "
            "Var(T)/Var(X) - exactly the reliability. Practice effects add "
            "a wrinkle: they shift the mean of the second occasion upward "
            "without necessarily changing the correlation, which is why a "
            "good test-retest report shows both the correlation and the mean "
            "change. The interval must match the construct's theory: "
            "intelligence researchers retest after years, mood researchers "
            "after days, and each must argue that the interval is long "
            "enough to wash out memory but short enough that the trait "
            "itself has not genuinely changed."
        ),
        "key_points": [
            "Same test, two occasions, one correlation: the stability coefficient.",
            "Short intervals inflate via memory; long intervals deflate via real change.",
            "Practice effects shift means; the correlation can survive even when means move.",
            "Right design for stable traits (ability retests run 0.80-0.90 over years).",
            "Wrong design for states: low retest correlation may mean the trait moved, not the test failed.",
        ],
        "requirements": [
            "Reliability concept (previous rung).",
            "Mean vs correlation: a shift in average need not change a correlation.",
        ],
        "standards": [
            "Retest interval reported and justified against the construct's stability theory.",
            "Mean change reported alongside the correlation.",
        ],
        "citations": [C_NUNNALLY, C_ANASTASI],
        "sig_lens": (
            "Signature take: stability across time is how his system knows "
            "it measured a trait rather than a moment. Time is the "
            "strictest auditor of every Signature instrument."
        ),
    },
    {
        "key": "split_half",
        "name": "Split-Half and Internal Consistency: One Test, Two Halves",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "Split-half reliability answers an elegant question: can one "
            "test administration estimate reliability all by itself? Split "
            "the test into two halves - odd versus even items is the "
            "classic - score each half separately, and correlate the half-"
            "scores across people. That correlation is the reliability of a "
            "half-length test, so the Spearman-Brown prophecy formula steps "
            "it up to the full length: r_full = 2*r_half / (1 + r_half). "
            "Internal consistency generalizes the idea: instead of one "
            "arbitrary split, consider every possible split at once. "
            "Cronbach's alpha is effectively the average of all possible "
            "split-half reliabilities, and the Kuder-Richardson formulas do "
            "the same for right-or-wrong scored items. These coefficients "
            "ask a subtly different question than test-retest: not 'are "
            "scores stable over time?' but 'do the items hang together as "
            "one thing?' A test can be internally consistent yet unstable "
            "over time (a perfectly coherent mood scale), or stable yet "
            "internally diverse (a broad achievement battery)."
        ),
        "how_it_works": (
            "The split-half correlation works because the two halves are "
            "mini parallel forms: they share the same true score and carry "
            "independent item-sampling error, so their correlation estimates "
            "the half-test's reliability. Spearman-Brown then answers 'what "
            "if the test were twice as long?' using the prophecy formula "
            "r_new = n*r / (1 + (n-1)*r) for length multiplier n. "
            "Cronbach's alpha computes the same idea without choosing a "
            "split: alpha = (k/(k-1)) * (1 - sum(item variances)/total "
            "variance), where k is the item count. When items covary "
            "strongly, total variance far exceeds the sum of item variances "
            "and alpha approaches 1; when items are unrelated, alpha "
            "collapses toward 0. The formula reveals alpha's two levers: "
            "more items and higher average inter-item correlation both raise "
            "it - which is also why alpha can be inflated by redundant, "
            "near-duplicate items without improving measurement."
        ),
        "key_points": [
            "One administration can estimate reliability: split it, correlate the halves, step up with Spearman-Brown.",
            "Spearman-Brown prophecy: r_new = n*r/(1+(n-1)*r) predicts reliability at any test length.",
            "Internal consistency asks 'do the items hang together?' - a different question than stability over time.",
            "Alpha's levers: more items and higher inter-item correlation; redundant items inflate it artificially.",
            "A coherent-but-unstable scale (mood) and a stable-but-diverse battery (achievement) show the designs diverge.",
        ],
        "requirements": [
            "True-score model and the reliability coefficient.",
            "Variance of a sum exceeds the sum of variances when items covary.",
        ],
        "standards": [
            "Split method (odd-even, first-second) reported; halves must be content-balanced.",
            "Alpha reported with item count; redundancy checked, not just alpha maximized.",
        ],
        "citations": [C_NUNNALLY, C_CROCKER, C_DEVELLIS],
        "sig_lens": (
            "Signature take: internal consistency is the test interrogating "
            "itself. His Signature instruments must cohere from within "
            "before they are allowed to speak about the world."
        ),
    },
    {
        "key": "cronbach_alpha",
        "name": "Cronbach's Alpha: The Workhorse of Internal Consistency",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "Cronbach's alpha, published by Lee Cronbach in 1951, is the "
            "most reported reliability coefficient in all of psychology - "
            "so common that 'alpha = 0.82' is practically punctuation in "
            "research papers. The formula is alpha = (k/(k-1)) * (1 - "
            "sum of item variances / variance of total scores), where k is "
            "the number of items. It estimates the proportion of total-"
            "score variance attributable to the common factor running "
            "through the items. Alpha equals the average of all possible "
            "split-half reliabilities, which is why no split need be "
            "chosen. But alpha is widely misunderstood. It is not a measure "
            "of unidimensionality - a test with two distinct factors can "
            "still show high alpha if the factors correlate or if there are "
            "enough items. It is not the reliability of the test in any "
            "absolute sense - it is a lower bound on reliability under the "
            "assumption of essential tau-equivalence (items measuring the "
            "same thing on the same scale). And it rewards redundancy: ten "
            "near-identical items produce a glorious alpha and a narrow, "
            "impoverished measure."
        ),
        "how_it_works": (
            "Alpha works by comparing two quantities: the sum of the "
            "individual item variances and the variance of the total score. "
            "If items are perfectly uncorrelated, the total variance equals "
            "the sum of item variances and alpha is zero. If items covary "
            "positively - the signature of a common underlying trait - the "
            "total variance balloons beyond the sum (because Var(sum) = sum "
            "of variances + twice the sum of covariances), and alpha climbs "
            "toward 1. The k/(k-1) term corrects for the number of items so "
            "that a single item does not produce a degenerate value. In "
            "practice the computation needs only the item response matrix: "
            "compute each item's variance, compute the total score's "
            "variance, apply the formula. The demonstration builds a 10-item "
            "scale with a genuine common factor plus noise, computes alpha "
            "directly from the formula, and shows it landing in the "
            "expected 0.75-0.90 band - then shows how adding five "
            "near-duplicate items inflates alpha without adding information."
        ),
        "key_points": [
            "Alpha = (k/(k-1))*(1 - sum(item var)/total var)): the average of all possible split-halves (Cronbach, 1951).",
            "It is a lower bound on reliability under essential tau-equivalence - not reliability itself.",
            "High alpha does NOT prove unidimensionality; correlated factors or many items can fake it.",
            "Redundant items inflate alpha while narrowing the construct - breadth matters as much as height.",
            "Conventions: 0.70 research, 0.80 applied, 0.90 high-stakes - with item count always reported alongside.",
        ],
        "requirements": [
            "Split-half logic (previous rung).",
            "Variance of a sum includes covariances.",
        ],
        "standards": [
            "Alpha reported with k, item type, and sample description.",
            "Dimensionality checked by factor analysis, never inferred from alpha alone.",
        ],
        "citations": [C_NUNNALLY, C_DEVELLIS, C_FURR],
        "sig_lens": (
            "Signature take: alpha is the workhorse, but his system never "
            "lets the workhorse run the farm. Every Signature alpha is "
            "reported beside a dimensionality check - coherence with "
            "honesty about what coheres."
        ),
    },
    {
        "key": "kr20",
        "name": "Kuder-Richardson Formulas: Reliability for Right-or-Wrong Items",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "The Kuder-Richardson formulas, published in 1937, are "
            "Cronbach's alpha specialized for dichotomous items - the "
            "right-or-wrong, yes-or-no, present-or-absent scoring of "
            "achievement tests, ability tests, and symptom checklists. KR-20 "
            "is the general form: KR-20 = (k/(k-1)) * (1 - sum(p*q)/total "
            "variance), where p is the proportion answering an item "
            "correctly and q = 1 - p. Because a 0/1 item's variance is "
            "exactly p*q, KR-20 is algebraically identical to alpha computed "
            "on 0/1 data - the demonstration proves this identity "
            "numerically. KR-21 is the simplified cousin for the special "
            "case where all items have roughly equal difficulty: it replaces "
            "sum(p*q) with a function of the mean and variance, needing only "
            "three numbers (k, mean, variance) instead of the full item "
            "matrix. KR-21 is always a lower bound on KR-20 and is "
            "conservative when difficulties vary. These formulas built the "
            "educational testing industry: every standardized achievement "
            "test of the 20th century reported a KR coefficient."
        ),
        "how_it_works": (
            "KR-20 works exactly like alpha because it IS alpha for binary "
            "data: each item's variance p*q measures how much that item "
            "discriminates (an item everyone gets right has p = 1, variance "
            "0, and contributes nothing), the sum of p*q is compared against "
            "the total-score variance, and the ratio says how much of the "
            "score spread comes from items moving together. KR-21 takes a "
            "shortcut: if all items share the same difficulty, sum(p*q) can "
            "be approximated from the test mean M and variance: KR-21 = "
            "(k/(k-1)) * (1 - M*(k-M)/(k*variance)). The shortcut costs "
            "accuracy exactly when items differ in difficulty - the more "
            "heterogeneous the p-values, the more KR-21 understates "
            "reliability. Modern practice computes KR-20 (or alpha) directly "
            "from item data and reserves KR-21 for historical datasets where "
            "only summary statistics survive."
        ),
        "key_points": [
            "KR-20 is alpha for 0/1 items: identical formula, identical value (proved in the demo).",
            "Item variance p*q is zero for items everyone gets right or wrong - they contribute nothing.",
            "KR-21 needs only k, mean, and variance - a shortcut valid only when difficulties are equal.",
            "KR-21 understates reliability whenever item difficulties vary; it is a conservative lower bound.",
            "These formulas powered 20th-century educational testing before computers made alpha routine.",
        ],
        "requirements": [
            "Cronbach's alpha formula (previous rung).",
            "Variance of a 0/1 variable equals p times q.",
        ],
        "standards": [
            "KR-20 vs KR-21 choice justified by item-difficulty homogeneity.",
            "Item p-values reported alongside the coefficient.",
        ],
        "citations": [C_NUNNALLY, C_CROCKER],
        "sig_lens": (
            "Signature take: right-or-wrong is the oldest scoring in "
            "measurement, and KR-20 is its honest accountant. His Signature "
            "achievement instruments carry KR coefficients as a matter of "
            "course."
        ),
    },
    {
        "key": "sem",
        "name": "Standard Error of Measurement: The Margin Around Every Score",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "The standard error of measurement (SEM) translates reliability "
            "from an abstract coefficient into a concrete margin of error "
            "around an individual's score. The formula is SEM = SD * "
            "sqrt(1 - reliability), where SD is the test's standard "
            "deviation. A test with SD = 15 and reliability 0.91 has SEM = "
            "4.5: an observed IQ of 115 really means 'the true score is "
            "probably between 110.5 and 119.5' (the 68% band), and 'almost "
            "certainly between 106 and 124' (the 95% band, plus or minus two "
            "SEMs). This is the number that should appear next to every "
            "reported score and almost never does. The SEM also powers the "
            "most practical question in testing: did this person really "
            "change? The standard error of the difference between two scores "
            "is SEM * sqrt(2), so a gain must exceed about 2.77 * SEM to be "
            "95% confident it is real change rather than measurement noise - "
            "the reliable-change index used in therapy outcome research."
        ),
        "how_it_works": (
            "The SEM works because the true-score model makes the error "
            "variance equal to Var(X) * (1 - reliability): reliability is "
            "the signal share, so one minus reliability is the noise share, "
            "and the SEM is the noise share's standard deviation. Around any "
            "observed score, the true score is distributed with standard "
            "deviation SEM (under normality assumptions), giving the "
            "confidence bands. The demonstration simulates a population with "
            "known true scores, adds measurement error consistent with "
            "reliability 0.84, and verifies that roughly 68% of true scores "
            "fall within one SEM of their observed scores - the band "
            "calibrates. It then shows the reliable-change logic: two "
            "scores 8 points apart on a test with SEM = 4.5 clear the 2.77 * "
            "SEM bar for real change, while a 5-point wobble does not. Bands "
            "first, verdicts second: that is the SEM's professional "
            "discipline."
        ),
        "key_points": [
            "SEM = SD * sqrt(1 - reliability): the margin of error around every individual score.",
            "Score plus/minus one SEM is the 68% band; plus/minus two SEMs is the 95% band.",
            "Real change requires clearing about 2.77 * SEM (the reliable-change index).",
            "The SEM should be reported beside every score; a naked score is an incomplete statement.",
            "Higher reliability shrinks the SEM - precision is reliability made visible.",
        ],
        "requirements": [
            "Reliability coefficient and standard deviation.",
            "Normal-distribution bands: 68% within one SD, 95% within two.",
        ],
        "standards": [
            "SEM reported in score units alongside reliability, per the Standards (2014).",
            "Confidence bands labeled with their coverage (68%, 90%, 95%).",
        ],
        "citations": [C_NUNNALLY, C_ANASTASI, C_STANDARDS],
        "sig_lens": (
            "Signature take: no Signature score is ever reported naked. "
            "Every number his system produces wears its margin of error "
            "openly - precision stated is trust earned."
        ),
    },
    {
        "key": "validity_intro",
        "name": "Validity: Does the Test Measure What It Claims?",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "Validity is the single most important concept in psychometrics: "
            "the degree to which evidence supports the interpretation of "
            "test scores for their intended use. Note the careful wording - "
            "modern validity theory (Samuel Messick, 1989; the 2014 "
            "Standards) says tests themselves are not 'valid' or 'invalid'; "
            "interpretations and uses are. A thermometer is not valid or "
            "invalid - but using it to measure intelligence would be an "
            "invalid use. The classic trinity of validities - content, "
            "criterion-related, and construct - has been unified into one "
            "concept: construct validity, the argument that scores mean what "
            "we claim, supported by five sources of evidence (test content, "
            "response processes, internal structure, relations to other "
            "variables, and consequences of testing). The field's hardest "
            "lesson: reliability is necessary but not sufficient for "
            "validity. A perfectly consistent test can consistently measure "
            "the wrong thing - like a scale that always reads five pounds "
            "heavy."
        ),
        "how_it_works": (
            "Validity works as an argument, not a coefficient. The test "
            "developer assembles a validity argument: the proposed "
            "interpretation ('these scores measure quantitative reasoning "
            "and predict college math grades'), the assumptions behind it, "
            "and the evidence for each assumption. Evidence comes in five "
            "streams: content evidence (experts judge the items cover the "
            "domain), response-process evidence (think-aloud protocols show "
            "test-takers use the intended reasoning), internal-structure "
            "evidence (factor analysis matches the theory), relations "
            "evidence (scores correlate with criteria and sibling measures, "
            "not with unrelated ones), and consequences evidence (the test's "
            "use does not produce unintended harm). The demonstration shows "
            "the reliability-validity ceiling: a test's correlation with any "
            "criterion cannot exceed sqrt(reliability_test * "
            "reliability_criterion) - the attenuation formula. Noisy "
            "measures cap how right you can be, which is why validity "
            "arguments always begin by establishing reliability."
        ),
        "key_points": [
            "Validity attaches to interpretations and uses, not to tests as objects (Messick, 1989).",
            "The trinity (content, criterion, construct) is unified: one construct-validity argument, five evidence streams.",
            "Reliability is necessary but not sufficient - a test can consistently measure the wrong thing.",
            "The attenuation ceiling: validity cannot exceed sqrt(r_xx * r_yy) - noise caps truth.",
            "Validity is an argument assembled from evidence, never a single number stamped on a test.",
        ],
        "requirements": [
            "Reliability (previous rungs).",
            "Correlation as a validity coefficient.",
        ],
        "standards": [
            "Validity framed per the Standards (2014): interpretations, uses, five evidence sources.",
            "Every high-stakes use requires its own validity argument.",
        ],
        "citations": [C_STANDARDS, C_ANASTASI, C_FURR],
        "sig_lens": (
            "Signature take: his system never confuses a working instrument "
            "with a true one. Reliability says the arrow flies straight; "
            "validity asks whether it flies at the right target."
        ),
    },
    {
        "key": "content_validity",
        "name": "Content Validity: Does the Test Cover the Territory?",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "Content validity is the most judgment-based form of validity "
            "evidence: the degree to which a test's items represent the "
            "full domain the test claims to cover. A licensing exam for "
            "electricians that tests only wiring and never safety codes has "
            "a content-validity problem no statistic can fix. The workhorse "
            "is the test blueprint (table of specifications): a grid "
            "crossing content domains with cognitive levels, each cell "
            "assigned a weight, and items written to fill the cells "
            "proportionally. Expert panels then judge each item's relevance, "
            "quantified by Lawshe's content validity ratio (CVR): for each "
            "item, CVR = (n_experts_saying_essential - N/2) / (N/2), and "
            "items below the critical value for the panel size are revised "
            "or dropped. Content validity is established before data "
            "collection - it is the one validity evidence stream that lives "
            "entirely in the design phase, and skipping it is the most "
            "common amateur error in test construction."
        ),
        "how_it_works": (
            "Content validation works through structured expert judgment. "
            "First the domain is defined - the knowledge, skills, and "
            "abilities the test should sample - and the blueprint allocates "
            "items across it. Then a panel of subject-matter experts rates "
            "each item as essential, useful-but-not-essential, or not "
            "necessary. Lawshe's CVR converts these votes into a number per "
            "item; with 10 experts, an item needs at least 8 'essential' "
            "votes (CVR = 0.60) to survive. The content validity index (CVI) "
            "averages the surviving CVRs across the test. The demonstration "
            "builds a 20-item blueprint across four domains, simulates an "
            "expert panel's essentiality votes, computes CVR per item, drops "
            "the two items the panel rejects, and verifies the blueprint "
            "weights still balance afterward - content evidence as an "
            "auditable paper trail from domain definition to final form."
        ),
        "key_points": [
            "Content validity is judgment-based: do the items represent the claimed domain?",
            "The test blueprint (table of specifications) allocates items across domains and cognitive levels.",
            "Lawshe's CVR quantifies expert agreement per item; below-critical items are revised or dropped.",
            "It is established in the design phase, before any data is collected.",
            "No statistic can rescue a test whose items miss the domain - content comes first.",
        ],
        "requirements": [
            "The validity concept (previous rung).",
            "Comfort with expert judgment as a form of evidence.",
        ],
        "standards": [
            "Domain definition documented before item writing, per the Standards (2014).",
            "Expert panel qualifications and CVR critical values reported.",
        ],
        "citations": [C_STANDARDS, C_DEVELLIS, C_THORNDIKE],
        "sig_lens": (
            "Signature take: coverage is a promise, and his system keeps its "
            "promises in writing. Every Signature blueprint is an auditable "
            "map from the territory claimed to the items delivered."
        ),
    },
]

ENTRIES += [
    {
        "key": "criterion_validity",
        "name": "Criterion Validity: Predicting Real Outcomes",
        "group": "Compounded",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description": (
            "Criterion validity is validity evidence from prediction: how "
            "well test scores forecast an external criterion that matters. "
            "A college admissions test has criterion validity if high "
            "scorers earn high college grades; an employment test has it if "
            "high scorers become high performers on the job. The evidence is "
            "the validity coefficient - usually the correlation between "
            "test and criterion - and the honest ones are humbling: 0.30 to "
            "0.50 is typical for a good predictor of a complex real-world "
            "outcome. Two flavors: concurrent validity (test and criterion "
            "measured at the same time, as when a depression scale is "
            "validated against current clinical diagnosis) and predictive "
            "validity (the criterion comes later, as in admissions). The "
            "great enemies are criterion contamination (the criterion itself "
            "is influenced by the test, as when interviewers see test "
            "scores), criterion deficiency (the criterion misses part of "
            "what matters, as when 'job performance' means only sales "
            "numbers), and restriction of range (validating an admissions "
            "test only on admitted students shrinks every correlation)."
        ),
        "how_it_works": (
            "Criterion validation works by gathering test scores and "
            "criterion measures on the same sample and computing their "
            "relationship - but the craft is in the corrections. Because "
            "admissions tests are validated on admitted students only, the "
            "observed correlation understates the true one; Thorndike's "
            "restriction-of-range corrections adjust it back up using the "
            "unrestricted test variance. Because criteria are noisy too, "
            "the attenuation correction divides by sqrt(r_xx * r_yy) to "
            "estimate what the correlation would be with perfect "
            "measurement. And because a correlation of 0.40 can still be "
            "enormously useful, expectancy tables translate it into "
            "decisions: among applicants scoring in the top fifth, what "
            "share succeed? The demonstration simulates an admissions test "
            "with true validity 0.45, applies selection (only the top 60% "
            "admitted), shows the observed correlation sagging to about "
            "0.30, applies the range correction, and recovers the true "
            "value - then builds an expectancy table showing the top "
            "quintile succeeding at twice the base rate."
        ),
        "key_points": [
            "Criterion validity is prediction: the test-criterion correlation, typically 0.30-0.50 for good real-world predictors.",
            "Concurrent validity measures both now; predictive validity waits for the criterion.",
            "Restriction of range (validating on selects only) systematically understates validity - correct it.",
            "Expectancy tables translate a correlation into decision language: success rates by score band.",
            "Contamination and deficiency in the criterion corrupt the evidence before the test is even judged.",
        ],
        "requirements": [
            "Correlation and the attenuation ceiling.",
            "Selection effects: samples of selects differ from applicant pools.",
        ],
        "standards": [
            "Criterion described for relevance, reliability, and freedom from contamination (Standards, 2014).",
            "Range corrections reported with their assumptions, never silently.",
        ],
        "citations": [C_NUNNALLY, C_ANASTASI, C_STANDARDS],
        "sig_lens": (
            "Signature take: prediction is where measurement meets "
            "consequence. His Signature predictors are validated against "
            "outcomes that matter, with every selection effect corrected in "
            "the open."
        ),
    },
    {
        "key": "construct_validity",
        "name": "Construct Validity: The Master Argument",
        "group": "Compounded",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description": (
            "Construct validity is the overarching question of "
            "psychometrics: does the test measure the theoretical construct "
            "it claims to measure - intelligence, extraversion, working "
            "memory, depression? Lee Cronbach and Paul Meehl's 1955 paper "
            "made it the master concept: every other validity evidence "
            "stream is really evidence about the construct interpretation. "
            "The logic is the nomological network - the web of theoretical "
            "relationships surrounding the construct. If 'anxiety' is the "
            "construct, theory says the measure should rise under threat, "
            "correlate with sibling anxiety measures, predict avoidance "
            "behavior, respond to anti-anxiety treatment, and NOT correlate "
            "with unrelated traits like mechanical aptitude. Each confirmed "
            "prediction strengthens the construct argument; each failed "
            "prediction weakens it or indicts the theory. Construct "
            "validation never ends - it is a research program, not a "
            "stamp. The modern Standards (2014) formalize this: validity is a "
            "unitary concept, and the five evidence sources (content, "
            "response processes, internal structure, relations to other "
            "variables, consequences) are all threads in the one construct "
            "argument."
        ),
        "how_it_works": (
            "Construct validation works by deriving risky predictions from "
            "the construct's theory and testing them. The classic machinery "
            "is Campbell and Fiske's multitrait-multimethod matrix (next "
            "rung): measure two or more traits with two or more methods, and "
            "check that same-trait-different-method correlations (convergent "
            "validity) exceed different-trait correlations (discriminant "
            "validity). Experimental manipulation adds teeth: if a test "
            "measures anxiety, an anxiety induction should move its scores. "
            "Group differences add more: diagnosed patients should outscore "
            "controls. Developmental and treatment-sensitivity studies add "
            "still more. The demonstration builds a small nomological "
            "network for a simulated 'quantitative reasoning' construct: "
            "the measure correlates 0.65 with math grades (convergent), 0.55 "
            "with a sibling reasoning test (convergent), 0.15 with verbal "
            "fluency (discriminant), and rises after a tutoring intervention "
            "(experimental) - each thread checked against its theoretical "
            "prediction, the argument assembled piece by piece."
        ),
        "key_points": [
            "Construct validity asks whether scores mean what the theory claims (Cronbach & Meehl, 1955).",
            "The nomological network - the construct's web of theoretical relationships - generates testable predictions.",
            "Evidence accumulates across studies; construct validation is a program, never a stamp.",
            "Experimental manipulation (inductions, treatments) gives the strongest construct evidence.",
            "The five Standards evidence sources are threads in the single construct argument.",
        ],
        "requirements": [
            "All validity evidence types so far.",
            "Comfort with theory-driven prediction.",
        ],
        "standards": [
            "Construct defined theoretically before measurement begins.",
            "Validity argument integrates all five evidence sources (Standards, 2014).",
        ],
        "citations": [C_STANDARDS, C_FURR, C_ANASTASI],
        "sig_lens": (
            "Signature take: a construct is a promise about how the world "
            "works, and his system holds every promise to account. Signature "
            "constructs earn their names one confirmed prediction at a time."
        ),
    },
    {
        "key": "convergent_discriminant",
        "name": "Convergent and Discriminant Validity: The Company Scores Keep",
        "group": "Compounded",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description": (
            "Convergent validity is evidence that a test relates to other "
            "measures it should relate to; discriminant validity is "
            "evidence that it does not relate to measures it should not "
            "relate to. A new working-memory test shows convergent validity "
            "by correlating 0.60 with an established working-memory battery, "
            "and discriminant validity by correlating only 0.15 with a "
            "vocabulary test - proving it measures memory processes, not "
            "just general verbal ability. Donald Campbell and Donald Fiske's "
            "1959 multitrait-multimethod (MTMM) matrix is the classic "
            "design: measure at least two traits with at least two methods "
            "(self-report, peer rating, behavioral task), producing a "
            "correlation matrix with a precise anatomy. The validity "
            "diagonal (same trait, different methods) should be substantial; "
            "each validity-diagonal value should exceed the correlations in "
            "its row and column of the heterotrait-heteromethod triangles; "
            "and the pattern of trait intercorrelations should replicate "
            "across methods. When method variance dominates - when "
            "everything measured by self-report correlates just because it "
            "is self-report - the matrix exposes it."
        ),
        "how_it_works": (
            "The MTMM matrix works by crossing traits with methods so that "
            "every correlation can be read three ways. The monotrait-"
            "monomethod diagonal (reliability diagonal) holds each measure's "
            "reliability. The validity diagonal holds same-trait, "
            "different-method correlations - the convergent evidence. The "
            "heterotrait-monomethod triangles hold different traits measured "
            "the same way (trait + method variance mixed). The "
            "heterotrait-heteromethod triangles hold different traits, "
            "different methods - pure trait relationships, the discriminant "
            "benchmark. Campbell and Fiske's four criteria then judge the "
            "matrix: validity values substantial, exceeding their row/column "
            "heterotrait values, exceeding heterotrait-monomethod values, "
            "and trait patterns replicating across methods. The "
            "demonstration builds a 2-trait by 2-method matrix from "
            "simulated data with true convergent correlations near 0.55 and "
            "discriminant correlations near 0.15, then checks all four "
            "criteria mechanically - the anatomy of the matrix made "
            "auditable."
        ),
        "key_points": [
            "Convergent: correlates with what it should. Discriminant: does not correlate with what it should not.",
            "The MTMM matrix crosses traits with methods to separate trait variance from method variance.",
            "Validity-diagonal values must beat their row/column heterotrait values (Campbell & Fiske, 1959).",
            "Method variance - everything correlating because of shared method - is the matrix's great exposure.",
            "Modern practice extends MTMM with confirmatory factor models (correlated-trait, correlated-method).",
        ],
        "requirements": [
            "Construct validity and the nomological network.",
            "Reading a correlation matrix.",
        ],
        "standards": [
            "Method variance assessed, not assumed away, in validity arguments.",
            "Convergent and discriminant predictions stated before data collection.",
        ],
        "citations": [C_FURR, C_NUNNALLY, C_KLINE],
        "sig_lens": (
            "Signature take: his system judges every measure by the company "
            "its scores keep. Converge with kin, diverge from strangers - "
            "that is how a Signature construct proves its identity."
        ),
    },
    {
        "key": "item_analysis",
        "name": "Item Analysis: Difficulty and Discrimination",
        "group": "Compounded",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description": (
            "Item analysis is the microscope of test construction: every "
            "item is examined for difficulty and discrimination before it "
            "earns a place in the final test. Item difficulty (the p-value) "
            "is simply the proportion of test-takers who answer correctly - "
            "p = 0.85 is an easy item, p = 0.30 is a hard one. Maximum "
            "information comes from items near p = 0.50, and a healthy test "
            "spreads difficulties across the ability range it must measure. "
            "Item discrimination is the item's power to separate high "
            "scorers from low scorers, quantified by the point-biserial "
            "correlation between the item (0/1) and the total score (with "
            "the item removed to avoid part-whole inflation). Good items "
            "discriminate at 0.30 or above; items near zero are dead weight; "
            "negative discriminations are alarms - the item is keyed wrong, "
            "misworded, or measuring something perverse. The classic "
            "item-analysis table also reports the upper-lower index: the "
            "difference in p-value between the top 27% and bottom 27% of "
            "scorers (Kelly's 1939 optimal split for normal distributions). "
            "Item analysis is where bad items are caught and killed - "
            "before they ever reach a live test form."
        ),
        "how_it_works": (
            "Item analysis works on pilot data: a few hundred "
            "representative test-takers answer the trial items, and each "
            "item gets its statistics. The p-value is the raw proportion "
            "correct. The point-biserial is the Pearson correlation between "
            "the 0/1 item score and the rest-score (total minus the item); "
            "it answers 'do people who get this item right also do well "
            "overall?' Distractor analysis (next rung) extends this to "
            "wrong options. Decision rules then apply: keep items with p "
            "between roughly 0.20 and 0.90 and discrimination above 0.25-"
            "0.30; revise items with low discrimination; investigate or "
            "discard negative discriminations immediately. The demonstration "
            "generates a 15-item pilot with known good, mediocre, and "
            "deliberately broken items (one miskeyed), computes p-values and "
            "point-biserials, and shows the table flagging exactly the "
            "intended casualties - including the miskeyed item's negative "
            "discrimination."
        ),
        "key_points": [
            "p-value: proportion correct - difficulty; best information near 0.50, healthy tests spread difficulties.",
            "Point-biserial: item-total correlation - discrimination; keep above ~0.30, investigate negatives at once.",
            "Upper-lower 27% index (Kelly, 1939) is the classic quick discrimination check.",
            "Rest-score (item removed) avoids part-whole inflation of the discrimination index.",
            "Item analysis is quality control: bad items are caught and killed in the pilot, never on live forms.",
        ],
        "requirements": [
            "Correlation and proportion.",
            "Internal consistency logic: items should move with the total.",
        ],
        "standards": [
            "Item statistics reported from representative pilot samples.",
            "Keying verified; negative discriminations investigated before any live use.",
        ],
        "citations": [C_CROCKER, C_THORNDIKE, C_DEVELLIS],
        "sig_lens": (
            "Signature take: every item in his system must earn its place "
            "under the microscope. Weak items are cut without sentiment - "
            "Signature tests are built from survivors."
        ),
    },
    {
        "key": "distractor_analysis",
        "name": "Distractor Analysis: Reading the Wrong Answers",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "Distractor analysis studies the wrong answers - and the wrong "
            "answers talk. In a multiple-choice item, each incorrect option "
            "(distractor) should attract some test-takers, and crucially, it "
            "should attract the lower-ability test-takers. A distractor that "
            "nobody chooses is dead weight that turns a four-option item "
            "into a three-option item (raising the guessing floor). A "
            "distractor that attracts high scorers more than low scorers is "
            "worse: it may be a second correct answer, a trick, or a "
            "miskeyed item in disguise. The standard display splits "
            "test-takers into ability bands (upper, middle, lower thirds by "
            "total score) and shows, for each option, the proportion chosen "
            "within each band. The healthy signature: the correct option's "
            "line rises steeply with ability while every distractor's line "
            "falls. Flat distractor lines mean the option is implausible to "
            "everyone; rising distractor lines mean the item is broken. "
            "Great distractors are built from common misconceptions - each "
            "wrong option diagnoses a specific wrong idea, turning the item "
            "into a diagnostic instrument rather than a mere hurdle."
        ),
        "how_it_works": (
            "Distractor analysis works by cross-tabulating option choice "
            "against ability. Test-takers are banded by total score, and for "
            "each item a table shows P(option | band) for every option. The "
            "analyst reads the option characteristic curves: the key "
            "(correct option) should monotonically increase across bands; "
            "each distractor should monotonically decrease; no distractor "
            "should be chosen by fewer than about 5% of test-takers "
            "(implausible) or draw the top band disproportionately "
            "(ambiguous or miskeyed). The demonstration simulates 600 "
            "test-takers on a four-option item with one strong distractor "
            "built from a common misconception (attracting the middle band), "
            "one weak distractor nobody chooses, and verifies the curves: "
            "key rising, strong distractor peaking in the middle, weak "
            "distractor flat near zero - with the verdict to rewrite the "
            "dead option from a documented student misconception."
        ),
        "key_points": [
            "Healthy signature: the key's curve rises with ability; every distractor's curve falls.",
            "Dead distractors (chosen by <5%) inflate the guessing floor and waste options.",
            "Distractors that attract top scorers signal ambiguity, trickery, or miskeying.",
            "Great distractors encode common misconceptions - each wrong answer diagnoses a wrong idea.",
            "Distractor analysis turns multiple-choice items into diagnostic instruments.",
        ],
        "requirements": [
            "Item analysis: p-values and discrimination.",
            "Reading conditional proportions across groups.",
        ],
        "standards": [
            "Option-level statistics reviewed for every operational multiple-choice item.",
            "Distractors grounded in documented misconceptions, not invented absurdities.",
        ],
        "citations": [C_CROCKER, C_THORNDIKE],
        "sig_lens": (
            "Signature take: his system reads the wrong answers as carefully "
            "as the right ones. Every distractor is a hypothesis about how "
            "minds go wrong - and hypotheses get tested."
        ),
    },
    {
        "key": "spearman_brown",
        "name": "Test Length and the Spearman-Brown Prophecy Formula",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "The Spearman-Brown prophecy formula answers one of the most "
            "practical questions in testing: if I change the test's length, "
            "what happens to its reliability? Published independently by "
            "Charles Spearman and William Brown in 1910, it states that a "
            "test lengthened by factor n (with parallel items) has "
            "reliability r_new = n*r / (1 + (n-1)*r). A 10-item quiz with "
            "reliability 0.60, doubled to 20 parallel items, prophecies to "
            "0.75; quadrupled to 40 items, 0.86. The formula also runs "
            "backward: it tells you how many items you need to hit a "
            "reliability target, which is how test specifications are "
            "actually written. But the prophecy has fine print. It assumes "
            "the added items are parallel - same difficulty, same "
            "discrimination, same construct. Real lengthening usually adds "
            "weaker items, so the prophecy is optimistic. And it has "
            "diminishing returns burned in: going from 0.60 to 0.75 costs a "
            "doubling, but going from 0.90 to 0.95 costs a tripling. The "
            "wisest use of Spearman-Brown is not 'add items until reliable' "
            "but 'write better items so fewer are needed' - reliability per "
            "minute of testing time is the true efficiency metric."
        ),
        "how_it_works": (
            "The formula works from the true-score model's variance "
            "arithmetic. Lengthening a test by factor n multiplies "
            "true-score variance by n squared (true scores add "
            "consistently) but error variance only by n (errors are "
            "independent and partly cancel) - so the signal share, "
            "reliability, must rise. Solving r_new = n*r/(1+(n-1)*r) for n "
            "gives the items-needed formula: n = r_target*(1-r) / "
            "(r*(1-r_target)). The demonstration simulates a 12-item test "
            "with reliability near 0.65, doubles it with parallel items, and "
            "verifies the observed reliability lands within sampling noise "
            "of the prophecy (about 0.79) - then shows the diminishing "
            "returns curve from 12 to 96 items, and the fine print: when the "
            "added items are weaker (lower discrimination), the prophecy "
            "overshoots reality. Length is a lever, but item quality is the "
            "fulcrum."
        ),
        "key_points": [
            "r_new = n*r/(1+(n-1)*r): the 1910 prophecy for reliability at any test length.",
            "Run it backward to specify how many items a reliability target requires.",
            "Assumes parallel added items - with weaker items the prophecy is optimistic.",
            "Diminishing returns are built in: 0.90 to 0.95 costs far more than 0.60 to 0.75.",
            "Efficiency metric: reliability per minute of testing time, not reliability at any cost.",
        ],
        "requirements": [
            "Reliability as signal share.",
            "True-score variance grows with n squared, error variance with n.",
        ],
        "standards": [
            "Length decisions documented with target reliability and item-quality assumptions.",
            "Prophecy treated as planning estimate, verified empirically in the pilot.",
        ],
        "citations": [C_NUNNALLY, C_CROCKER],
        "sig_lens": (
            "Signature take: his system lengthens tests by design, not by "
            "hope. The prophecy plans the build; the pilot verifies it; "
            "quality per minute is the Signature efficiency creed."
        ),
    },
    {
        "key": "interrater",
        "name": "Interrater Reliability: When Humans Are the Instrument",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "Interrater reliability asks whether different human judges "
            "agree when they score the same performances - essays, clinical "
            "interviews, job interviews, portfolio reviews, gymnastics "
            "routines. Whenever the 'instrument' is a person applying a "
            "rubric, rater disagreement is measurement error, and it must "
            "be quantified. The naive metric is percent agreement: the share "
            "of cases where raters assign the same score. Its fatal flaw is "
            "chance agreement - two raters classifying 95% of cases as "
            "'normal' will agree 90% of the time by luck alone. For "
            "continuous ratings, the intraclass correlation (ICC) is the "
            "standard: it partitions score variance into target variance "
            "versus rater variance, in the true-score spirit. For "
            "categorical judgments, Cohen's kappa (next rung) corrects for "
            "chance. The professional response to low interrater reliability "
            "is never 'the raters are bad' - it is rubric revision, rater "
            "training with anchor examples, calibration sessions, and "
            "adjudication rules for disagreements."
        ),
        "how_it_works": (
            "Interrater analysis works by having two or more raters "
            "independently score the same sample, then modeling the "
            "disagreement. Percent agreement is computed directly but "
            "reported alongside the base rates that inflate it. The ICC "
            "treats raters as a variance facet: for a one-way random model, "
            "ICC = (target variance) / (target variance + rater variance + "
            "residual), estimated from a simple ANOVA of the rating matrix. "
            "Values above 0.75 are generally considered good for applied "
            "decisions. The demonstration simulates two essay raters with "
            "true interrater correlation 0.80 plus a leniency difference "
            "(rater B scores 5 points higher on average), shows percent "
            "exact agreement looking mediocre while the ICC - which "
            "tolerates the constant leniency shift - correctly reports "
            "strong reliability, and demonstrates that averaging the two "
            "raters (Spearman-Brown logic again) lifts reliability further. "
            "Disagreement decomposed is disagreement that can be fixed."
        ),
        "key_points": [
            "When humans score, rater disagreement is measurement error and must be quantified.",
            "Percent agreement is inflated by chance - never report it beside skewed base rates without correction.",
            "The intraclass correlation partitions target variance from rater variance.",
            "Constant rater biases (leniency/severity) hurt agreement but not necessarily ICC consistency.",
            "Fix low agreement with rubrics, anchor training, and calibration - not rater blame.",
        ],
        "requirements": [
            "Reliability as variance partition.",
            "ANOVA intuition: variance split into sources.",
        ],
        "standards": [
            "Rater training, rubrics, and adjudication rules documented (Standards, 2014).",
            "ICC model (one-way/two-way, consistency/agreement) named explicitly - the six ICCs differ.",
        ],
        "citations": [C_NUNNALLY, C_ANASTASI],
        "sig_lens": (
            "Signature take: wherever his system lets humans judge, it "
            "measures the judges too. Calibrated raters, audited agreement - "
            "Signature scoring leaves no human variance unexamined."
        ),
    },
    {
        "key": "cohens_kappa",
        "name": "Cohen's Kappa: Agreement Beyond Chance",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "Cohen's kappa (1960) is the chance-corrected agreement "
            "coefficient for categorical judgments: kappa = (Po - Pe) / "
            "(1 - Pe), where Po is observed agreement and Pe is the "
            "agreement expected by chance from the raters' marginal "
            "distributions. Two radiologists agreeing on 85% of scans sounds "
            "impressive until the base rate makes chance agreement 80% - "
            "kappa of 0.25 tells the honest story. Landis and Koch's "
            "widely-cited benchmarks call 0.00-0.20 slight, 0.21-0.40 "
            "fair, 0.41-0.60 moderate, 0.61-0.80 substantial, and 0.81-1.00 "
            "almost perfect agreement. Kappa has famous paradoxes: with "
            "very skewed prevalence, high agreement can coexist with low "
            "kappa (the prevalence paradox), and asymmetric rater biases "
            "distort it (the bias paradox) - which is why professionals "
            "report kappa alongside raw agreement and the marginals. "
            "Weighted kappa extends the idea to ordered categories "
            "(mild/moderate/severe), penalizing far disagreements more than "
            "near ones. Fleiss' kappa generalizes to more than two raters."
        ),
        "how_it_works": (
            "Kappa works by building the expected-agreement baseline from "
            "the confusion matrix's margins: if rater A says 'yes' 60% of "
            "the time and rater B says 'yes' 50%, chance alone puts them "
            "both at 'yes' 30% of the time and both at 'no' 20%, so Pe = "
            "0.50. Observed agreement Po minus this baseline, divided by "
            "the maximum possible improvement (1 - Pe), is the chance-"
            "corrected share. The demonstration uses a fixed 2x2 table "
            "(both-yes 45, A-yes-only 15, B-yes-only 10, both-no 30): Po = "
            "0.75, Pe = 0.50, kappa = 0.50 - exactly 'moderate' - and "
            "verifies the arithmetic to the decimal. It then shows the "
            "prevalence paradox: the same 90% agreement with a 95% base "
            "rate collapses kappa toward 0.30, proving that agreement "
            "without kappa is a story half told."
        ),
        "key_points": [
            "Kappa = (Po - Pe)/(1 - Pe): agreement beyond chance (Cohen, 1960).",
            "Benchmarks: 0.41-0.60 moderate, 0.61-0.80 substantial, 0.81+ almost perfect.",
            "The prevalence paradox: skewed base rates make high agreement coexist with low kappa.",
            "Always report kappa with raw agreement and the marginal distributions.",
            "Weighted kappa for ordered categories; Fleiss' kappa for more than two raters.",
        ],
        "requirements": [
            "Interrater reliability and the chance-agreement flaw.",
            "Reading a 2x2 confusion matrix.",
        ],
        "standards": [
            "Kappa variant (unweighted/weighted, weights specified) always named.",
            "Paradoxes checked: prevalence and bias reported, not hidden.",
        ],
        "citations": [C_NUNNALLY, C_ANASTASI],
        "sig_lens": (
            "Signature take: agreement is cheap; agreement beyond chance is "
            "the currency. His Signature raters are held to the kappa "
            "standard - honesty about chance is honesty about quality."
        ),
    },
    {
        "key": "norming",
        "name": "Norming and Standardization: Giving Scores Meaning",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "A raw score - 37 correct out of 50 - means nothing until it is "
            "normed: compared against the distribution of scores from a "
            "representative norm group. Norming is what turns '37' into "
            "'78th percentile' or 'one standard deviation above average', "
            "and standardization is the discipline of administering, "
            "scoring, and interpreting the test identically for everyone so "
            "the comparison is fair. Building norms requires a norm sample "
            "that mirrors the target population on age, education, region, "
            "and other relevant variables - the great expense of commercial "
            "test publishing is norming studies with thousands of carefully "
            "sampled participants. Percentile ranks are the most intuitive "
            "norm: the percentage of the norm group scoring at or below a "
            "given score. But percentiles have quirks: they are ordinal "
            "(the gap between the 50th and 60th percentiles is much smaller "
            "in raw points than between the 90th and 99th), they bunch in "
            "the middle, and they cannot be averaged meaningfully. That is "
            "why professionals convert to standard scores (next rung) for "
            "any serious analysis."
        ),
        "how_it_works": (
            "Norming works in three stages. First, standardize "
            "administration: identical instructions, timing, materials, and "
            "scoring rules for every test-taker, so score differences "
            "reflect person differences rather than procedure differences. "
            "Second, collect the norm sample: stratified sampling to match "
            "the population, often thousands of cases, with documented "
            "recruitment and weighting. Third, build the norms table: for "
            "each raw score, the percentile rank PR = 100 * (number below "
            "+ half the number tied) / N, plus smoothed standard-score "
            "equivalents. The demonstration norms a 40-item test on 2,000 "
            "simulated representative scores, computes percentile ranks, "
            "and verifies the defining property: a score at the 84th "
            "percentile sits almost exactly one standard deviation above "
            "the mean in a normal distribution - then shows the ordinal "
            "trap by demonstrating that averaging two percentile ranks does "
            "not equal the percentile rank of the averaged raw scores."
        ),
        "key_points": [
            "Raw scores are meaningless until normed against a representative group.",
            "Standardization (identical administration) is what makes norm comparisons fair.",
            "Norm samples must mirror the population - stratified, large, documented.",
            "Percentile ranks are intuitive but ordinal: bunched in the middle, not averagable.",
            "Serious analysis converts to standard scores; percentiles are for communication.",
        ],
        "requirements": [
            "Normal distribution: mean, standard deviation, percentiles.",
            "Ordinal vs interval scales.",
        ],
        "standards": [
            "Norm sample composition, dates, and sampling method published (Standards, 2014).",
            "Norms updated when populations shift; outdated norms flagged.",
        ],
        "citations": [C_ANASTASI, C_STANDARDS, C_THORNDIKE],
        "sig_lens": (
            "Signature take: a score without a comparison group is a voice "
            "without a room. His system norms every instrument against "
            "documented populations - meaning is always relative, and "
            "always stated."
        ),
    },
    {
        "key": "standard_scores",
        "name": "Standard Scores: z, T, Stanines, and the IQ Scale",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "Standard scores are linear rescalings of z-scores that make "
            "test results instantly interpretable: z = (X - mean)/SD puts "
            "every test on a mean-0, SD-1 scale; T-scores (mean 50, SD 10) "
            "banish decimals and negatives; stanines compress the normal "
            "curve into nine bands (mean 5, SD 2); and the IQ scale (mean "
            "100, SD 15) is the most famous standard score in psychology. "
            "The conversions are simple linear transforms - T = 50 + 10z, "
            "IQ = 100 + 15z - so they preserve the shape of the score "
            "distribution exactly. Normalized standard scores go one step "
            "further: they force the distribution into normality by mapping "
            "percentile ranks through the inverse normal curve, useful when "
            "raw scores are skewed but the reporting scale must be normal "
            "(the classic case is IQ). The critical distinction: linear "
            "standard scores keep the distribution's shape (skew in, skew "
            "out); normalized scores impose normality. Confusing the two "
            "has launched a thousand misinterpretations - including the "
            "enduring myth that IQ scores are 'naturally' normal rather "
            "than normalized by construction."
        ),
        "how_it_works": (
            "Standard scores work because linear transforms preserve order "
            "and relative distances: subtracting the mean centers the "
            "scale, dividing by the SD sets the unit, and adding a new mean "
            "and multiplying by a new SD relocates it anywhere convenient. "
            "A z of +1.5 is T = 65, stanine 7, IQ 122.5 - the same standing, "
            "four costumes. Normalized scores add a nonlinear step: compute "
            "the percentile rank, then find the z whose normal CDF equals "
            "that percentile - which irons skew into a bell curve. The "
            "demonstration takes a skewed raw-score distribution, computes "
            "linear T-scores (verifying mean 50, SD 10, skew preserved), "
            "then normalized T-scores (verifying normality achieved), and "
            "shows the stanine assignment - making the shape-preserving vs "
            "shape-imposing distinction concrete and checkable."
        ),
        "key_points": [
            "z, T (50+-10), stanine (5+-2), IQ (100+-15) are the same standing in different costumes.",
            "Linear transforms preserve distribution shape exactly - order and relative distances unchanged.",
            "Normalized scores impose normality via percentile-to-z mapping; linear scores do not.",
            "IQ's bell curve is partly by construction (normalization), not pure nature.",
            "Choose linear for fidelity to the data, normalized for comparability across skewed tests.",
        ],
        "requirements": [
            "z-scores and the normal distribution.",
            "Percentile ranks.",
        ],
        "standards": [
            "Score type (linear vs normalized) stated in every technical manual.",
            "Normalization method and reference distribution documented.",
        ],
        "citations": [C_ANASTASI, C_THORNDIKE, C_WECHSLER],
        "sig_lens": (
            "Signature take: his system dresses every score for its "
            "audience without changing what the score says. Standard scores "
            "are translation, not transformation - the meaning stays "
            "Signature-true."
        ),
    },
    {
        "key": "cognitive_ability",
        "name": "Cognitive Ability Testing: Measuring the Mind's Engine",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Cognitive ability testing is psychometrics' oldest and most "
            "consequential application: measuring general mental capability "
            "and its components. Alfred Binet's 1905 scale, built to "
            "identify Paris schoolchildren needing help, became Lewis "
            "Terman's Stanford-Binet and then David Wechsler's scales - the "
            "WAIS-IV today yields a Full Scale IQ (mean 100, SD 15) plus "
            "four index scores: Verbal Comprehension, Perceptual Reasoning, "
            "Working Memory, and Processing Speed. The empirical bedrock is "
            "the positive manifold: all cognitive tests correlate "
            "positively, and factor analysis extracts a general factor, g "
            "(Spearman, 1904), accounting for roughly 40-50% of the shared "
            "variance. Modern hierarchical models (Cattell-Horn-Carroll "
            "theory) place g atop broad abilities like fluid reasoning (Gf), "
            "crystallized knowledge (Gc), and working memory (Gwm). Ability "
            "tests are among the most reliable instruments in psychology "
            "(FSIQ reliability ~0.98) and the most predictively valid: IQ "
            "predicts educational attainment, job performance (better for "
            "complex jobs), and even health and longevity - while remaining "
            "among the most socially contested, from the Flynn effect (raw "
            "scores rising ~3 points per decade) to the fairness debates "
            "that shaped modern test standards."
        ),
        "how_it_works": (
            "Ability testing works by sampling diverse cognitive tasks - "
            "vocabulary, block design, digit span, matrix reasoning - "
            "standardizing each against age norms, and compositing them. "
            "Each subtest yields a scaled score (mean 10, SD 3); index "
            "scores sum their subtests and convert to the IQ metric (mean "
            "100, SD 15); the Full Scale IQ composites the indexes. "
            "Reliability comes from length and standardization: dozens of "
            "items, strict administration, enormous norm samples. The g "
            "factor emerges because the subtests' positive correlations "
            "share one dominant dimension - factor analysis of any diverse "
            "battery finds it. The demonstration simulates a four-subtest "
            "battery with a true g factor, computes scaled scores, builds "
            "the composite, verifies FSIQ reliability above 0.95 via "
            "Spearman-Brown from subtest reliabilities, and shows the "
            "Flynn adjustment: the same raw performance normed a decade "
            "later scores lower, because the norm group got stronger."
        ),
        "key_points": [
            "From Binet (1905) to the WAIS-IV: subtests -> four indexes -> Full Scale IQ (100 +- 15).",
            "The positive manifold yields g, the general factor (~40-50% of shared variance).",
            "CHC theory organizes abilities hierarchically: g atop Gf, Gc, Gwm, and others.",
            "FSIQ reliability ~0.98 - among the most precise measures in psychology.",
            "Predicts education, job complexity-matched performance, health - and carries the Flynn effect (~3 points/decade).",
        ],
        "requirements": [
            "Standard scores and norming.",
            "Factor analysis concept (developed fully next rung).",
        ],
        "standards": [
            "Administration standardized strictly; deviations invalidate norms.",
            "Fairness evidence required for every population the test serves (Standards, 2014).",
        ],
        "citations": [C_WECHSLER, C_ANASTASI, C_NUNNALLY],
        "sig_lens": (
            "Signature take: cognitive ability is the mind's engine, and "
            "his system measures engines with engine-grade precision. "
            "Signature ability instruments are built to the Wechsler "
            "standard of evidence - then held to the Signature standard of "
            "honesty about limits."
        ),
    },
    {
        "key": "personality_measurement",
        "name": "Personality Measurement: Scaling the Self",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Personality measurement applies psychometrics to the "
            "characteristic patterns of thinking, feeling, and behaving "
            "that make people distinct. Two traditions dominate. The trait "
            "tradition builds Likert-scale inventories - the NEO PI-R "
            "measuring the Big Five (Openness, Conscientiousness, "
            "Extraversion, Agreeableness, Neuroticism) is the flagship, "
            "with each domain split into six facets. The clinical tradition "
            "builds criterion-keyed instruments like the MMPI-2: its scales "
            "were constructed empirically by keeping the items that "
            "separated diagnosed patients from normals, regardless of item "
            "content - so a depression scale contains items about anything "
            "depressed patients endorse more often. Both traditions wrestle "
            "with response biases: acquiescence (yea-saying), social "
            "desirability (faking good), and extreme responding. Defenses "
            "include balanced keying (half the items reverse-scored so "
            "yea-saying cancels out), lie and validity scales (the MMPI's "
            "famous L, F, and K scales detect faking), and forced-choice "
            "formats. Personality scales typically show alpha 0.80-0.90 and "
            "retest 0.80+ over months - traits, by definition, persist."
        ),
        "how_it_works": (
            "Personality scaling works through summed Likert ratings with "
            "balanced keying. Each item is answered 1 (strongly disagree) to "
            "5 (strongly agree); reverse-keyed items are rescored as 6 minus "
            "the response, so that acquiescence - agreeing with everything - "
            "adds equally to both poles and cancels in the total. Subscale "
            "scores sum their items; domain scores sum or average the "
            "facets. Reliability is checked per subscale with alpha; "
            "validity comes from the nomological network (extraversion "
            "predicting sociability behaviors, conscientiousness predicting "
            "job performance and longevity) and from factor analysis "
            "recovering the Big Five structure. The demonstration builds a "
            "simulated 20-item extraversion scale with 10 reverse-keyed "
            "items, verifies that reverse scoring works (reversed items "
            "correlate negatively with raw but positively with rescored "
            "totals), computes subscale alpha above 0.80, and shows a "
            "simulated yea-sayer scoring at the scale midpoint rather than "
            "the top - balanced keying neutralizing the bias by "
            "construction."
        ),
        "key_points": [
            "Two traditions: trait inventories (Big Five, Likert-scaled) and criterion-keyed clinical scales (MMPI-2).",
            "Balanced keying (reverse-scored items) cancels acquiescence bias by construction.",
            "Validity scales (MMPI L, F, K) detect faking good, faking bad, and defensiveness.",
            "Typical reliability: alpha 0.80-0.90, retest 0.80+ over months - traits persist.",
            "Factor analysis of trait inventories recovers the Big Five - structure as validity evidence.",
        ],
        "requirements": [
            "Likert scales and ordinal measurement.",
            "Internal consistency and test-retest reliability.",
        ],
        "standards": [
            "Response-bias controls documented; validity scales reported where faking matters.",
            "Trait interpretations supported by longitudinal stability evidence.",
        ],
        "citations": [C_COSTA, C_MMPI, C_ANASTASI],
        "sig_lens": (
            "Signature take: personality is the self, reported by the self "
            "- the hardest measurement of all. His Signature personality "
            "instruments are engineered against self-deception first, "
            "because the respondent is also the defense attorney."
        ),
    },
    {
        "key": "factor_analysis",
        "name": "Factor Analysis: Finding the Hidden Dimensions",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Factor analysis is the statistical engine that finds hidden "
            "dimensions behind correlated measurements. If six tests - "
            "vocabulary, reading, analogies, arithmetic, number series, "
            "spatial puzzles - correlate in a pattern where the first three "
            "hang together and the last three hang together, factor analysis "
            "extracts two latent factors (verbal, quantitative) that explain "
            "the pattern. The model: each observed variable equals a "
            "weighted sum of the common factors plus unique variance "
            "(specificity + measurement error). The weights are factor "
            "loadings - correlations between variables and factors - and the "
            "communality of a variable is the share of its variance the "
            "factors explain. Spearman invented the method in 1904 to find "
            "g; Thurstone's multiple-factor analysis (1930s) found primary "
            "mental abilities; and every Big Five personality study since "
            "has used it. Rotation (varimax, oblimin) then turns the "
            "mathematically arbitrary initial solution into an interpretable "
            "one - simple structure, where each variable loads highly on as "
            "few factors as possible."
        ),
        "how_it_works": (
            "Factor analysis works from the correlation matrix. The "
            "eigenvalues of the matrix say how many factors the data can "
            "support (Kaiser's rule: keep eigenvalues above 1; the scree "
            "plot's elbow is the visual version). Extraction - principal "
            "axis, maximum likelihood - finds loadings that reproduce the "
            "observed correlations as closely as possible: the reproduced "
            "correlation between two variables is the sum over factors of "
            "the products of their loadings. Rotation then reorients the "
            "factors for interpretability without changing fit. The "
            "demonstration simulates 600 people on six tests driven by two "
            "true uncorrelated factors (verbal, quantitative), computes the "
            "correlation matrix, extracts the dominant direction by power "
            "iteration, and verifies the anatomy: within-domain correlations "
            "(~0.50) dwarf cross-domain ones (~0.10), the first eigenvalue "
            "dominates, and the recovered loadings separate the six tests "
            "into their true two families - the hidden dimensions made "
            "visible."
        ),
        "key_points": [
            "Factors are latent dimensions explaining why variables correlate; loadings are variable-factor correlations.",
            "Communality: the share of a variable's variance the factors explain; the rest is uniqueness.",
            "Spearman (1904) found g; Thurstone found primary abilities; the Big Five came from factor analysis.",
            "Rotation (varimax, oblimin) seeks simple structure - interpretability without changing fit.",
            "Deciding the number of factors (eigenvalues, scree, parallel analysis) is the analyst's central judgment.",
        ],
        "requirements": [
            "Correlation matrices.",
            "Eigenvalue intuition: variance captured by a direction.",
        ],
        "standards": [
            "Extraction and rotation methods reported; factor count justified by multiple criteria.",
            "Sample size adequate: 300+ cases or 10+ per variable as rough floors.",
        ],
        "citations": [C_NUNNALLY, C_FURR, C_KLINE],
        "sig_lens": (
            "Signature take: factor analysis is how his system sees through "
            "the clutter of measurements to the few real dimensions "
            "beneath. Fewer, truer dimensions - that is Signature "
            "parsimony."
        ),
    },
    {
        "key": "efa_cfa",
        "name": "Exploratory vs Confirmatory Factor Analysis: Discovery vs Proof",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Exploratory factor analysis (EFA) discovers structure: feed it "
            "a correlation matrix and it tells you how many factors emerge "
            "and what loads where, with no prior theory required. "
            "Confirmatory factor analysis (CFA) tests structure: you "
            "specify the model in advance - 'items 1-4 load on factor A, "
            "items 5-8 on factor B, factors correlate 0.30' - and CFA judges "
            "whether the data fit that exact hypothesis. The two are the "
            "discovery and proof phases of structural psychometrics, and "
            "using them in the right order is a professional discipline: "
            "explore on one sample, confirm on a fresh sample - never "
            "confirm on the sample you explored, which is circular. CFA "
            "brings the machinery of model fit: the chi-square test of "
            "exact fit (almost always rejected in large samples), and the "
            "practical fit indices - RMSEA below 0.06, CFI and TLI above "
            "0.95 are the conventional 'good fit' cutoffs (Hu & Bentler, "
            "1999). CFA also tests measurement invariance: whether the "
            "same factor structure holds across groups, the prerequisite "
            "for fair group comparisons."
        ),
        "how_it_works": (
            "CFA works by comparing the observed covariance matrix against "
            "the matrix implied by the specified model. Maximum likelihood "
            "estimation finds the loadings and factor correlations that "
            "make the implied matrix closest to the observed one; the "
            "residual matrix (observed minus implied) is the misfit made "
            "visible. Fit indices summarize it: RMSEA measures misfit per "
            "degree of freedom (lower is better), CFI compares against a "
            "null model of no relationships (higher is better). The "
            "demonstration makes the EFA/CFA contrast concrete without "
            "full ML estimation: on simulated two-factor data, it computes "
            "the residual correlations under a wrong one-factor model "
            "(large residuals between the true factors' items - misfit "
            "exposed) versus the correct two-factor model (residuals near "
            "zero - fit achieved), showing exactly what CFA's fit machinery "
            "is judging and why exploring-then-confirming on separate "
            "samples is the honest workflow."
        ),
        "key_points": [
            "EFA discovers structure; CFA tests a pre-specified structure - discovery then proof, on separate samples.",
            "CFA judges fit by comparing observed vs model-implied covariance matrices.",
            "Fit cutoffs: RMSEA < 0.06, CFI/TLI > 0.95 (Hu & Bentler, 1999); chi-square tests exact fit.",
            "Confirming on the exploration sample is circular - fresh data for confirmation.",
            "CFA tests measurement invariance across groups: the prerequisite for fair comparisons.",
        ],
        "requirements": [
            "Factor analysis: loadings, communalities, rotation.",
            "Model fit intuition: residuals as misfit.",
        ],
        "standards": [
            "EFA and CFA samples independent; cross-validation reported.",
            "Full fit indices reported, not just the favorable ones.",
        ],
        "citations": [C_KLINE, C_FURR],
        "sig_lens": (
            "Signature take: discover boldly, confirm ruthlessly. His "
            "system explores on one sample and proves on another - "
            "Signature structures survive contact with fresh data."
        ),
    },
]

ENTRIES += [
    {
        "key": "rasch_1pl",
        "name": "Item Response Theory: The Rasch (1PL) Model",
        "group": "Advanced",
        "ladder_rank": 7,
        "ladder_tier": "advanced",
        "description": (
            "Item response theory (IRT) is the modern framework of "
            "psychometrics: instead of modeling test scores, it models each "
            "item response as a probabilistic function of the person's "
            "latent ability. The Rasch model (Georg Rasch, 1960) - also "
            "called the one-parameter logistic (1PL) model - is the "
            "simplest and most elegant: P(correct) = 1 / (1 + exp(-(theta - "
            "b))), where theta is the person's ability and b is the item's "
            "difficulty, both on the same logit scale. When ability equals "
            "difficulty, the probability is exactly 0.50; a person one "
            "logit above the difficulty has about a 73% chance. The Rasch "
            "model's magic is specific objectivity: item difficulties can "
            "be estimated independently of which people took them, and "
            "person abilities independently of which items they took - "
            "provided the data fit the model. This separability is what "
            "makes item banking, test equating, and adaptive testing "
            "possible. The price is strictness: the model demands equal "
            "item discrimination and no guessing, and real data must be "
            "checked against it with fit statistics (infit/outfit mean "
            "squares near 1.0) rather than assumed to comply."
        ),
        "how_it_works": (
            "The Rasch model works because the logistic function turns the "
            "ability-minus-difficulty difference into a probability, and "
            "the log-odds (logit) of success equals exactly theta minus b - "
            "a beautifully simple additive structure. Estimation is "
            "typically joint or marginal maximum likelihood: find the "
            "thetas and bs that make the observed 0/1 response matrix most "
            "probable. The demonstration simulates 500 people with true "
            "abilities spanning -2 to +2 logits answering 12 Rasch items "
            "with known difficulties, estimates each person's ability by "
            "Newton-Raphson on the likelihood (sum of item probabilities "
            "minus observed score, over sum of P(1-P)), and verifies "
            "recovery: estimated thetas correlate above 0.95 with the true "
            "values, and the item characteristic curves show the defining "
            "Rasch property - all 12 curves parallel, differing only in "
            "horizontal position (difficulty), never in steepness."
        ),
        "key_points": [
            "P(correct) = 1/(1+exp(-(theta-b))): ability and difficulty on one logit scale (Rasch, 1960).",
            "Specific objectivity: item and person parameters separable - the foundation of item banking.",
            "All item characteristic curves are parallel; items differ only in difficulty, never steepness.",
            "Fit statistics (infit/outfit ~1.0) check whether real data honor the model's strictness.",
            "The Rasch model is the gateway to adaptive testing, equating, and modern test design.",
        ],
        "requirements": [
            "Logistic function and log-odds intuition.",
            "Item difficulty (p-values) from classical theory - now reborn as b.",
        ],
        "standards": [
            "Model-data fit reported (infit/outfit); misfitting items revised or removed.",
            "Unidimensionality and local independence assumptions checked, not assumed.",
        ],
        "citations": [C_EMBRETSON, C_HAMBLETON, C_CROCKER],
        "sig_lens": (
            "Signature take: the Rasch model is measurement at its purest - "
            "one scale for people and items alike. His Signature item banks "
            "are built Rasch-first, because separability is freedom."
        ),
    },
    {
        "key": "pl2_3pl",
        "name": "The 2PL and 3PL Models: Discrimination and Guessing",
        "group": "Advanced",
        "ladder_rank": 7,
        "ladder_tier": "advanced",
        "description": (
            "The two- and three-parameter logistic models relax the Rasch "
            "model's strictness to fit real test data better. The 2PL adds "
            "a discrimination parameter a per item: P(correct) = 1 / (1 + "
            "exp(-a*(theta - b))). High-a items have steep characteristic "
            "curves - they discriminate sharply near their difficulty but "
            "say little far away; low-a items are flat and forgiving. The "
            "3PL adds a guessing (pseudo-chance) parameter c: P(correct) = c "
            "+ (1-c) / (1 + exp(-a*(theta - b))). On a four-option "
            "multiple-choice test, even the weakest test-taker guesses "
            "right 25% of the time, so the curve's lower asymptote lifts "
            "from 0 to c (~0.25) - and the model stops pretending that "
            "low-ability correct answers are evidence of ability. Birnbaum "
            "(1968) introduced the 2PL/3PL framework; Lord's work made it "
            "the engine of large-scale testing. The trade-off is real: "
            "more parameters fit better but demand larger samples (500+ for "
            "2PL, 1000+ for stable 3PL) and complicate equating, since "
            "items no longer share a single difficulty scale so cleanly."
        ),
        "how_it_works": (
            "The models work by letting each item have its own curve "
            "shape. The a parameter scales the logit: doubling a doubles "
            "the curve's steepness at b, concentrating the item's "
            "information into a narrower ability band. The c parameter "
            "mixes a guessing floor into the probability: the curve rises "
            "from c rather than 0, so low-theta correct responses are "
            "discounted as likely guesses. Estimation is marginal maximum "
            "likelihood via the EM algorithm, integrating over an assumed "
            "ability distribution. The demonstration plots the three "
            "curves for one item family: Rasch (a=1, c=0), 2PL (a=1.8, "
            "c=0), 3PL (a=1.8, c=0.25) - verifying numerically that at "
            "theta far below b the 3PL probability approaches 0.25 while "
            "the others approach 0, that the 2PL curve is steepest at b, "
            "and that all three pass through their characteristic points "
            "exactly as the formulas dictate."
        ),
        "key_points": [
            "2PL adds discrimination a: steep curves discriminate sharply near b, flat curves forgive.",
            "3PL adds guessing c: the lower asymptote lifts to the chance level (~0.25 for 4 options).",
            "More parameters fit better but need bigger samples: 500+ for 2PL, 1000+ for stable 3PL.",
            "The guessing parameter stops the model crediting low-ability lucky guesses as ability.",
            "Rasch vs 2PL/3PL is a philosophical choice too: measurement purity vs empirical fit.",
        ],
        "requirements": [
            "The Rasch model and the logistic function.",
            "Likelihood intuition: parameters that make data most probable.",
        ],
        "standards": [
            "Model choice justified; sample size adequate for the parameter count.",
            "Guessing parameter constrained to plausible bounds; Heywood cases investigated.",
        ],
        "citations": [C_EMBRETSON, C_HAMBLETON],
        "sig_lens": (
            "Signature take: his system models items as they are, not as "
            "the pure theory wishes them to be. Discrimination and "
            "guessing are honored where the data demand them - Signature "
            "fit is empirical, never wished."
        ),
    },
    {
        "key": "item_information",
        "name": "Item and Test Information: Precision Where It Counts",
        "group": "Advanced",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "Item information is IRT's replacement for reliability: instead "
            "of one reliability number for the whole test, every ability "
            "level gets its own precision. For the 2PL model, an item's "
            "information at ability theta is I(theta) = a^2 * P(theta) * "
            "(1 - P(theta)) - largest where the item discriminates best, "
            "which is near its difficulty b for high-a items. Test "
            "information is simply the sum of item informations, and the "
            "standard error of the ability estimate is 1/sqrt(test "
            "information) - precision you can point at on the theta scale. "
            "This changes test design fundamentally: instead of 'make the "
            "test reliable', the designer shapes the test information "
            "function to match the decision. A pass/fail licensing exam "
            "needs a tall, narrow information peak at the cut score; a "
            "broadband achievement survey needs a wide, flat information "
            "curve. Reliability said 'how precise on average'; information "
            "says 'how precise exactly where it matters' - and exposes the "
            "dirty secret that most tests measure the middle of the ability "
            "range well and the extremes poorly."
        ),
        "how_it_works": (
            "Information works as Fisher information from statistics: it "
            "measures how sharply the likelihood peaks around the ability "
            "estimate, which is exactly how precisely theta is known. For "
            "the Rasch model it simplifies to P(1-P) summed over items - "
            "each item contributes most at theta = b, where P = 0.5 and "
            "the contribution is 0.25. The demonstration builds a 20-item "
            "test with difficulties spread from -2 to +2, computes the test "
            "information curve, and verifies three properties: the curve "
            "peaks near the middle where items cluster, the standard error "
            "1/sqrt(I) is smallest there (~0.35) and larger at the extremes "
            "(~0.70 at theta = +-2.5), and removing the five most extreme "
            "items visibly hollows the curve's shoulders - precision "
            "engineered, precision verified, the IRT design loop closed."
        ),
        "key_points": [
            "Item information I(theta) = a^2*P*(1-P): precision varies across the ability scale.",
            "Test information sums item informations; SE(theta) = 1/sqrt(I) - precision on demand.",
            "Design the information function to match the decision: peak at cut scores, flat for surveys.",
            "Most tests measure the middle well and the extremes poorly - information makes it visible.",
            "Information replaces the single reliability number with a precision curve.",
        ],
        "requirements": [
            "IRT models: P(theta) curves.",
            "Standard error as precision.",
        ],
        "standards": [
            "Conditional standard errors reported across the score scale (Standards, 2014).",
            "Information targets documented in test specifications.",
        ],
        "citations": [C_EMBRETSON, C_HAMBLETON],
        "sig_lens": (
            "Signature take: precision where it counts, honesty where it "
            "doesn't. His Signature tests publish their information curves "
            "openly - no instrument claims precision it cannot point to."
        ),
    },
    {
        "key": "dif",
        "name": "Differential Item Functioning: The Fairness Microscope",
        "group": "Advanced",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "Differential item functioning (DIF) asks whether an item "
            "behaves differently for different groups - men vs women, "
            "majority vs minority test-takers - after matching on overall "
            "ability. If equally able members of two groups have different "
            "chances of answering an item correctly, the item shows DIF, "
            "and it is a prime suspect for bias. The classic example: a "
            "math word problem about baseball statistics that is harder "
            "for equally skilled girls than boys - not because of math "
            "ability but because of differential familiarity with the "
            "sport. Uniform DIF shifts the item's difficulty for one group "
            "(the ICCs are parallel but offset); non-uniform DIF changes "
            "the discrimination (the curves cross). The Mantel-Haenszel "
            "procedure is the workhorse detector: stratify test-takers by "
            "total score, compute the group odds ratio within each stratum, "
            "and combine - a common odds ratio far from 1.0 flags the item. "
            "DIF is necessary but not sufficient evidence of bias: the "
            "item is then reviewed by sensitivity panels who judge whether "
            "the DIF reflects irrelevant content (bias - remove it) or a "
            "real group difference in the construct (impact - keep it)."
        ),
        "how_it_works": (
            "DIF detection works by conditioning on ability so that group "
            "differences in the trait cannot masquerade as item problems. "
            "The Mantel-Haenszel method builds, within each total-score "
            "stratum, a 2x2 table (group x correct/incorrect) and combines "
            "the stratum odds ratios into one common odds ratio; values "
            "far from 1.0 (conventionally, |log-OR| beyond ~0.43 for "
            "moderate-to-large DIF) flag the item. IRT methods compare item "
            "parameters estimated separately by group. The demonstration "
            "simulates 1,000 test-takers in two groups with identical "
            "ability distributions, plants one DIF item (0.8 logits harder "
            "for group B at equal ability) among 19 clean items, runs a "
            "stratified odds-ratio analysis, and verifies the planted item "
            "is the only one flagged - then shows the crucial follow-up: "
            "with groups of genuinely different ability, the naive "
            "unstratified comparison falsely flags clean items, proving "
            "why conditioning on ability is the whole game."
        ),
        "key_points": [
            "DIF: equally able members of different groups have different success chances on the item.",
            "Uniform DIF offsets difficulty; non-uniform DIF changes discrimination (curves cross).",
            "Mantel-Haenszel: stratify by total score, combine odds ratios - condition on ability always.",
            "DIF flags items; sensitivity panels judge bias (irrelevant content, remove) vs impact (real difference, keep).",
            "Without conditioning on ability, group ability differences masquerade as item bias.",
        ],
        "requirements": [
            "Item characteristic curves.",
            "Odds ratios and stratification.",
        ],
        "standards": [
            "DIF analyses routine for all operational items; flagged items panel-reviewed (Standards, 2014).",
            "Effect sizes reported, not just significance - large samples flag trivial DIF.",
        ],
        "citations": [C_EMBRETSON, C_STANDARDS, C_HAMBLETON],
        "sig_lens": (
            "Signature take: fairness is not a slogan in his system; it is "
            "a statistical procedure run on every item. DIF screening is "
            "the Signature fairness microscope - no item gets a pass it "
            "has not earned."
        ),
    },
    {
        "key": "equating",
        "name": "Test Equating: Making Different Forms Interchangeable",
        "group": "Advanced",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "Test equating puts scores from different test forms onto a "
            "common scale so that a 650 means the same thing no matter "
            "which form you took. Without equating, the SAT you took in "
            "March and the one your friend took in June are different tests "
            "with incomparable scores - form difficulty differences would "
            "masquerade as ability differences. The anchor design is the "
            "workhorse: each form contains a set of common (anchor) items, "
            "and the anchor performance links the forms. Linear equating "
            "adjusts for mean and standard-deviation differences: Y_equated "
            "= mean_Y + (SD_Y/SD_X)(X - mean_X), estimated through the "
            "anchor. Equipercentile equating goes further, matching the "
            "full score distributions. IRT true-score equating uses the "
            "item parameters: find the theta behind a score on form X, then "
            "the expected score at that theta on form Y. The five "
            "requirements of equating (Lord): same construct, equal "
            "reliability, symmetry, equity (it should not matter which form "
            "you take), and population invariance. When forms differ too "
            "much or samples are not equivalent, equating degrades into "
            "mere linking - and honest programs say so."
        ),
        "how_it_works": (
            "Equating works through the anchor items, which are the bridge "
            "between forms. In the common-item nonequivalent-groups "
            "design, group A takes form X and group B takes form Y, with "
            "both groups answering the shared anchors; the anchor means "
            "and SDs estimate how the groups and forms differ, and the "
            "Tucker or Levine methods convert form-X scores to the form-Y "
            "scale. The demonstration simulates two 30-item forms sharing "
            "10 anchor items, with form Y genuinely 0.3 logits harder and "
            "the groups slightly different in ability; linear equating "
            "through the anchors recovers the true conversion within 0.05 "
            "standard deviations across the score range, while the naive "
            "no-equating comparison is off by a third of a standard "
            "deviation - the exact error equating exists to prevent. It "
            "also shows the population-invariance check: the conversion "
            "computed on subgroups must agree, or the equating is not "
            "trustworthy."
        ),
        "key_points": [
            "Equating makes scores interchangeable across forms; without it, form differences masquerade as ability.",
            "Anchor items are the bridge: common items taken by both groups link the scales.",
            "Linear equating adjusts means and SDs; equipercentile matches full distributions; IRT equating goes through theta.",
            "Lord's five requirements: same construct, equal reliability, symmetry, equity, population invariance.",
            "Overstretched equating degrades to linking - honest programs label it as such.",
        ],
        "requirements": [
            "Standard scores and linear transforms.",
            "IRT ability scale (for true-score equating).",
        ],
        "standards": [
            "Equating design, anchor composition, and invariance checks documented.",
            "Scores reported with the equating error, not just the point conversion.",
        ],
        "citations": [C_CROCKER, C_EMBRETSON, C_STANDARDS],
        "sig_lens": (
            "Signature take: a 650 is a 650 no matter which form you took - "
            "that is a promise his system keeps with anchors and "
            "arithmetic. Signature equating makes every form one test."
        ),
    },
    {
        "key": "vertical_scaling",
        "name": "Vertical Scaling: One Ruler for Many Grades",
        "group": "Advanced",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "Vertical scaling puts tests from different grade levels onto "
            "a single developmental scale, so that a 4th-grader's 220 and "
            "an 8th-grader's 260 are directly comparable and growth can be "
            "measured. State accountability systems live on vertical "
            "scales: they are how 'a year's growth' becomes a number. The "
            "design embeds common items across adjacent grades - 4th-grade "
            "items appearing on the 5th-grade test and vice versa - and "
            "concurrent calibration estimates all items and all students "
            "on one IRT scale simultaneously. The scale then shows the "
            "famous developmental pattern: rapid growth in early grades, "
            "slowing in later ones, with the scale's unit (often set so "
            "grade-to-grade growth is ~10 points early on) carrying real "
            "meaning. The controversies are real too: content shifts "
            "across grades (4th-grade math vs 8th-grade math are partly "
            "different constructs), multidimensionality strains the "
            "unidimensional IRT model, and scale shrinkage - the "
            "compression of apparent growth in upper grades - may be a "
            "scaling artifact as much as a learning fact. Vertical scales "
            "are powerful and fragile: the most useful and most "
            "argued-about numbers in educational measurement."
        ),
        "how_it_works": (
            "Vertical scaling works by concurrent calibration: pool the "
            "response data from all grades, with the common items serving "
            "as the fixed points that pin the grades' scales together, "
            "and estimate one set of item parameters and grade-specific "
            "ability distributions. Because the common items have single "
            "difficulties regardless of grade, the grade means separate "
            "onto one continuum. The demonstration simulates grades 4, 5, "
            "and 6 with true mean abilities 0.0, 0.5, and 0.9 logits, "
            "10 common items bridging each adjacent pair, runs a "
            "simplified concurrent alignment (anchoring each grade's common "
            "items to shared difficulties), and verifies the recovered "
            "grade means match the true growth pattern within 0.1 logits - "
            "then demonstrates scale shrinkage risk by showing how a "
            "ceiling-heavy upper-grade test compresses the apparent grade-6 "
            "mean, the artifact that fuels the fiercest vertical-scaling "
            "debates."
        ),
        "key_points": [
            "One scale across grades makes growth measurable: 4th-grade 220 vs 8th-grade 260.",
            "Common items across adjacent grades pin the scales together; concurrent calibration estimates all at once.",
            "Growth slows across grades - rapid early, compressed later.",
            "Threats: content shift across grades, multidimensionality, scale-shrinkage artifacts.",
            "Vertical scales are the most useful and most argued-about numbers in educational measurement.",
        ],
        "requirements": [
            "Test equating and anchor designs.",
            "IRT concurrent calibration concept.",
        ],
        "standards": [
            "Dimensionality across grades investigated; construct shift disclosed.",
            "Growth interpretations validated against longitudinal data, not just cross-sectional scales.",
        ],
        "citations": [C_EMBRETSON, C_THORNDIKE, C_STANDARDS],
        "sig_lens": (
            "Signature take: growth deserves one ruler, honestly built. "
            "His Signature vertical scales document every bridging "
            "assumption - because a growth number is a promise to a child."
        ),
    },
    {
        "key": "cat",
        "name": "Computerized Adaptive Testing: The Test That Listens",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "Computerized adaptive testing (CAT) is IRT's killer "
            "application: the test adapts to the test-taker in real time, "
            "serving each next item at the current best estimate of their "
            "ability. Answer correctly and the next item gets harder; miss "
            "and it gets easier - homing in like a binary search. The "
            "result is dramatic efficiency: a CAT routinely matches the "
            "precision of a 60-item fixed test with 25-30 items, because "
            "every item is administered where its information is maximal "
            "for that person. The algorithm has four parts: an item bank "
            "calibrated by IRT (hundreds of items with known a, b, c), a "
            "starting rule (often theta = 0), an item-selection rule "
            "(maximum Fisher information at the current estimate, with "
            "content-balancing and exposure controls), and a stopping rule "
            "(standard error below target, or maximum items). The ASVAB, "
            "the GRE, and professional licensing exams run on CAT. The "
            "engineering challenges are real: item exposure control (popular "
            "items get overused and leak), content balancing (the adaptive "
            "algorithm must still cover the blueprint), and the cold-start "
            "problem of the first few items."
        ),
        "how_it_works": (
            "CAT works as a loop: estimate theta, pick the unused item "
            "with maximum information at that theta, administer it, update "
            "the estimate (by maximum likelihood or Bayesian EAP), repeat "
            "until the standard error target is hit. Maximum-information "
            "selection is greedy but effective: at each step it asks the "
            "question that would most reduce uncertainty right now. The "
            "demonstration simulates a 200-item bank and a test-taker of "
            "true ability theta = 1.0: the CAT starts at 0, selects "
            "max-information items, updates by Newton-Raphson after each "
            "response, and stops when SE falls below 0.35 - verifying it "
            "uses about 22 items versus a 50-item fixed form reaching the "
            "same precision, that the final estimate is within 0.2 of the "
            "true theta, and that early items swing widely while later "
            "items fine-tune. The test that listens asks half the "
            "questions and hears twice as well."
        ),
        "key_points": [
            "CAT adapts item difficulty to the running ability estimate - a binary search for your theta.",
            "25-30 adaptive items match a 60-item fixed test's precision: every item at maximum information.",
            "Four parts: calibrated bank, start rule, max-information selection, SE-based stopping rule.",
            "Engineering: exposure control, content balancing, cold-start handling.",
            "Powers the ASVAB, GRE, and modern licensing exams.",
        ],
        "requirements": [
            "Item information functions.",
            "Maximum likelihood ability estimation.",
        ],
        "standards": [
            "Item bank calibrated and secured; exposure rates monitored continuously.",
            "Content blueprint enforced inside the adaptive algorithm, not hoped for.",
        ],
        "citations": [C_EMBRETSON, C_HAMBLETON, C_ANASTASI],
        "sig_lens": (
            "Signature take: a test that listens is a test that respects "
            "the test-taker's time. His Signature adaptive instruments ask "
            "only the questions that matter - precision with courtesy."
        ),
    },
    {
        "key": "fairness_bias",
        "name": "Test Fairness and Bias: Impact Is Not Bias",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "Test fairness is the most socially consequential topic in "
            "psychometrics, and its central distinction is the hardest to "
            "keep straight: impact is not bias. Impact means groups score "
            "differently - which happens whenever groups genuinely differ "
            "in the measured construct, in opportunity to learn, or in "
            "preparation. Bias means the test measures different things "
            "for different groups, or systematically mis-predicts for a "
            "group. A perfectly fair test can show large impact; a test "
            "with zero impact can still be biased. The field's fairness "
            "toolkit has four drawers: DIF analysis (item-level, "
            "conditioned on ability), differential prediction (does the "
            "regression of criterion on test score differ by group? "
            "Cleary's 1968 definition of test bias), measurement invariance "
            "testing (does the factor structure hold across groups?), and "
            "consequential review (do the test's uses produce unjustified "
            "adverse impact, and are less discriminatory alternatives "
            "available?). The Standards (2014) devote a full chapter to "
            "fairness, and the professional consensus is procedural: "
            "fairness is not a property you prove once but a program of "
            "evidence you maintain - DIF screening, invariance testing, "
            "sensitivity review - on every operational form, forever."
        ),
        "how_it_works": (
            "Fairness analysis works by separating the three stories that "
            "group score gaps can tell. Story one, true difference: groups "
            "differ in the construct - the test is a faithful messenger. "
            "Story two, opportunity difference: groups differ in "
            "preparation - the test is fair but the world is not, and the "
            "validity argument must say so. Story three, measurement bias: "
            "the test itself functions differently - DIF, differential "
            "prediction, or non-invariance, and the test must be fixed. "
            "The demonstration simulates two groups with a real 0.5-SD "
            "construct gap plus one biased item (uniform DIF favoring "
            "group A): the raw gap confounds all three stories, but the "
            "analysis separates them - the DIF screen flags exactly the "
            "biased item, measurement-invariance holds once it is removed, "
            "and the remaining gap is correctly attributed to the true "
            "construct difference. Impact quantified, bias isolated, "
            "fairness made operational rather than rhetorical."
        ),
        "key_points": [
            "Impact (group score gaps) is not bias (the test functioning differently by group).",
            "Four toolkit drawers: DIF, differential prediction, measurement invariance, consequential review.",
            "Cleary (1968): test bias is systematic mis-prediction for a group in the criterion regression.",
            "Sensitivity panels judge flagged content; statistics flag, humans judge.",
            "Fairness is a maintained program of evidence, not a one-time proof.",
        ],
        "requirements": [
            "DIF analysis.",
            "Regression and prediction; factor structure.",
        ],
        "standards": [
            "Fairness evidence required for every population served (Standards, 2014, ch. 3).",
            "Adverse impact investigated; less discriminatory alternatives considered.",
        ],
        "citations": [C_STANDARDS, C_EMBRETSON, C_ANASTASI],
        "sig_lens": (
            "Signature take: his system never hides behind a gap and never "
            "ignores one. Every Signature instrument separates impact from "
            "bias in the open - fairness as procedure, permanently."
        ),
    },
    {
        "key": "g_theory",
        "name": "Generalizability Theory: Reliability Grown Up",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "Generalizability theory (G-theory), developed by Lee Cronbach "
            "and colleagues in 1972, generalizes reliability from 'one "
            "coefficient' to a full accounting of every source of "
            "measurement error. Classical theory asks 'how reliable is the "
            "test?'; G-theory asks 'reliable for what decision, over what "
            "variations?' - items, raters, occasions, tasks, forms. A "
            "G-study partitions observed-score variance into components: "
            "person variance (the signal), item variance, rater variance, "
            "occasion variance, and every interaction (person-by-item, "
            "person-by-rater, and so on). A D-study (decision study) then "
            "uses those components to design the measurement: how many "
            "items and raters are needed for the intended decision? Two "
            "coefficients result: the generalizability coefficient (for "
            "relative decisions - ranking people) and the dependability "
            "index phi (for absolute decisions - comparing to a cut "
            "score). G-theory is the framework behind performance "
            "assessment, where rater, task, and occasion all vary at once "
            "and classical reliability's single number is hopelessly "
            "inadequate."
        ),
        "how_it_works": (
            "G-theory works through ANOVA-style variance decomposition. "
            "In a persons-by-items-by-raters design, each observation is "
            "modeled as grand mean + person effect + item effect + rater "
            "effect + interactions + residual; mean squares estimate each "
            "component. The D-study then asks: if I average over n_i items "
            "and n_r raters, how much error remains for my decision? Error "
            "variances shrink as 1/n for the facets averaged over - the "
            "same Spearman-Brown logic, now per-facet. The demonstration "
            "simulates 100 people, 8 items, 3 raters with known variance "
            "components (person 1.0, item 0.2, rater 0.15, interactions and "
            "residual 0.5 total), estimates the components from mean "
            "squares, verifies person variance dominates as designed, and "
            "runs the D-study: the generalizability coefficient with 8 "
            "items and 2 raters exceeds 0.85, while cutting to 4 items "
            "drops it below 0.75 - the design decision made quantitative "
            "before a single operational dollar is spent."
        ),
        "key_points": [
            "G-theory partitions error into facets: items, raters, occasions, tasks - not one lump (Cronbach et al., 1972).",
            "G-study estimates variance components; D-study designs the measurement for the intended decision.",
            "Generalizability coefficient for rankings; dependability phi for cut-score decisions.",
            "Each facet's error shrinks as 1/n - design the facet mix, don't just lengthen blindly.",
            "The framework for performance assessment, where classical reliability is inadequate.",
        ],
        "requirements": [
            "ANOVA variance decomposition.",
            "Reliability as signal share; Spearman-Brown per-facet logic.",
        ],
        "standards": [
            "Facets of generalization named for every reported coefficient.",
            "D-study used prospectively in design, not just retrospectively.",
        ],
        "citations": [C_BRENNAN, C_NUNNALLY],
        "sig_lens": (
            "Signature take: his system accounts for every source of error "
            "by name. G-theory is Signature honesty scaled up - no error "
            "facet hides in an undifferentiated lump."
        ),
    },
    {
        "key": "sem_modeling",
        "name": "Structural Equation Modeling: Theories as Equations",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "Structural equation modeling (SEM) is the union of factor "
            "analysis and path analysis: it tests entire theories - "
            "measurement models plus causal structures among latent "
            "variables - in one estimation. A typical SEM says: these "
            "twelve items measure three latent factors (the measurement "
            "model, which is CFA), and among the factors, anxiety predicts "
            "avoidance which predicts impairment (the structural model, "
            "which is path analysis) - and then judges whether the "
            "covariance matrix implied by this whole theory matches the "
            "observed one. SEM's superpower is modeling with latent "
            "variables, which purges measurement error from structural "
            "relationships: a regression of observed scores attenuates "
            "effects toward zero, but SEM's latent regression estimates "
            "the disattenuated truth. Mediation analysis (X -> M -> Y, the "
            "indirect effect a*b), multitrait-multimethod models, growth "
            "curves, and measurement-invariance sequences all live inside "
            "SEM. The dangers are proportional to the power: equivalent "
            "models (different causal stories, identical fit), "
            "specification search masquerading as confirmation, and causal "
            "language outrunning the correlational data."
        ),
        "how_it_works": (
            "SEM works by maximum likelihood fitting of the model-implied "
            "covariance matrix to the observed one - CFA's machinery "
            "extended to regressions among latents. The measurement model "
            "links items to factors; the structural model regresses "
            "latents on latents; fit indices (RMSEA, CFI) judge the whole "
            "theory at once. Mediation falls out naturally: with latent X, "
            "M, Y, the indirect effect is the product of the X->M and M->Y "
            "path coefficients, tested by bootstrap confidence intervals. "
            "The demonstration builds the mediation logic with observed "
            "variables (the path algebra is identical): simulates X -> M "
            "(a = 0.6) -> Y (b = 0.5) plus a direct X -> Y path (c' = 0.2), "
            "estimates all three by regression, verifies the indirect "
            "effect a*b = 0.30 accounts for most of the total effect 0.50, "
            "and shows the attenuation lesson - adding measurement error "
            "to M shrinks the estimated indirect effect, the exact bias "
            "latent-variable SEM exists to remove."
        ),
        "key_points": [
            "SEM = CFA measurement model + path-analytic structural model, estimated together.",
            "Latent variables purge measurement error: structural paths are disattenuated.",
            "Mediation (indirect effect a*b), growth curves, and invariance sequences all live in SEM.",
            "Fit indices judge the whole theory; modification indices suggest - but do not license - changes.",
            "Dangers: equivalent models, specification search, causal language beyond the data.",
        ],
        "requirements": [
            "Confirmatory factor analysis.",
            "Multiple regression and path intuition.",
        ],
        "standards": [
            "Models specified a priori; exploratory modifications labeled as such.",
            "Equivalent models acknowledged; causal claims tied to design, not fit alone.",
        ],
        "citations": [C_KLINE, C_FURR],
        "sig_lens": (
            "Signature take: his system tests theories whole, not piece by "
            "piece. SEM is Signature theorizing made estimable - the full "
            "argument, judged at once, with error purged from the paths."
        ),
    },
    {
        "key": "standards_testing",
        "name": "The Standards for Educational and Psychological Testing",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "The Standards for Educational and Psychological Testing - "
            "jointly published by AERA, APA, and NCME, current edition "
            "2014 - is the profession's constitution: the authoritative "
            "statement of what responsible test development, validation, "
            "and use require. Its architecture: Part I, Foundations "
            "(validity, reliability/precision, fairness); Part II, "
            "Operations (test design and development, scores and scales, "
            "norms, administration, scoring, reporting, documentation); "
            "Part III, Testing Applications (psychological testing, "
            "educational testing, workplace testing, program evaluation, "
            "policy). Each standard is labeled as essential ('must') or "
            "conditional, and the whole document enforces the field's core "
            "doctrines: validity is about score interpretations for "
            "specified uses; fairness evidence is required for every "
            "population served; test users must be qualified; documentation "
            "(the technical manual) must let an independent expert "
            "evaluate every claim. The Standards are not law, but courts, "
            "licensing boards, and the court of professional opinion treat "
            "them as the benchmark - 'did you follow the Standards?' is "
            "the question every challenged test must answer."
        ),
        "how_it_works": (
            "The Standards work as an audit framework: for any testing "
            "program, walk the applicable standards and demand evidence "
            "for each. Validity standards require the interpretation-"
            "use argument with its five evidence sources. Reliability "
            "standards require precision reported conditionally across the "
            "score scale. Fairness standards require DIF screening, "
            "invariance evidence, accessibility, and adverse-impact review. "
            "Operations standards require documented development, secure "
            "administration, accurate scoring, and comprehensible score "
            "reports. The demonstration implements a Standards audit as "
            "code: a checklist of 24 essential standards across the five "
            "parts, each checked against a simulated testing program's "
            "documentation - verifying that a complete program passes all "
            "24 while a program missing fairness evidence and technical "
            "documentation fails exactly those clusters. The constitution "
            "made executable: compliance you can run."
        ),
        "key_points": [
            "The joint AERA/APA/NCME Standards (2014) are the profession's constitution for testing.",
            "Three parts: Foundations (validity, reliability, fairness), Operations, Applications.",
            "Core doctrines: validity of interpretations, fairness evidence for every population, qualified users, full documentation.",
            "Standards are the benchmark in legal and professional challenges to tests.",
            "Use them as an audit framework: every program, every form, every use.",
        ],
        "requirements": [
            "The full ladder: validity, reliability, fairness, operations concepts.",
            "Comfort with professional-ethics reasoning.",
        ],
        "standards": [
            "This record IS the standards summary; all other records cite it.",
            "Standard numbers referenced where the 2014 edition enumerates them.",
        ],
        "citations": [C_STANDARDS],
        "sig_lens": (
            "Signature take: his system treats the Standards as floor, not "
            "ceiling. Every Signature testing program is audited against "
            "them - and then held to the Signature standard beyond them."
        ),
    },
    {
        "key": "test_construction_workflow",
        "name": "Building a Test: The Full Professional Workflow",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "This final rung assembles the entire ladder into the "
            "professional workflow of building a test from nothing to an "
            "operational instrument. Stage 1, define: the construct, the "
            "intended uses, and the validity argument they require - "
            "written before any item exists. Stage 2, blueprint: the table "
            "of specifications allocating items across content and "
            "cognitive levels. Stage 3, write: items drafted to "
            "specification, reviewed for content, sensitivity-screened for "
            "bias, with distractors built from real misconceptions. Stage "
            "4, pilot: trial administration to a representative sample, "
            "then item analysis (p-values, discriminations, distractor "
            "curves), DIF screening, and dimensionality checks - weak "
            "items revised or cut. Stage 5, calibrate: reliability "
            "analysis (alpha/KR-20, SEM), IRT calibration of the item "
            "bank, information-function review against the blueprint. "
            "Stage 6, norm and scale: standardization, norm sample, "
            "percentile and standard-score tables. Stage 7, validate: the "
            "criterion, convergent/discriminant, and consequential evidence "
            "assembled into the validity argument. Stage 8, document: the "
            "technical manual an independent expert could audit. Stage 9, "
            "maintain: equating across forms, exposure control, periodic "
            "renorming, ongoing fairness surveillance. Skip a stage and the "
            "debt compounds - there are no shortcuts in measurement, only "
            "deferred failures."
        ),
        "how_it_works": (
            "The workflow works as a gated pipeline: each stage has entry "
            "criteria, methods, and exit evidence, and no stage's output "
            "is trusted until its checks pass. The demonstration runs a "
            "compressed full cycle on simulated data: blueprint a 24-item "
            "quantitative-reasoning test across three content domains; "
            "generate pilot responses from 800 simulees with known "
            "abilities including 4 deliberately flawed items; run item "
            "analysis and verify the 4 flawed items are flagged by "
            "discrimination or distractor rules; cut them to a 20-item "
            "form; compute alpha (verified above 0.85) and the SEM; "
            "calibrate Rasch difficulties and verify recovery of the true "
            "values; build the percentile norms; and assemble the validity "
            "checklist - content (blueprint coverage 100%), internal "
            "structure (one dominant factor), relations (criterion r = "
            "0.52). Every gate from the chapter exercised end to end: "
            "define, blueprint, write, pilot, calibrate, norm, validate, "
            "document, maintain."
        ),
        "key_points": [
            "Nine gated stages: define, blueprint, write, pilot, calibrate, norm, validate, document, maintain.",
            "Each stage has exit evidence; no stage's output is trusted until its checks pass.",
            "Item analysis and DIF screening in the pilot are where bad items die.",
            "The technical manual must let an independent expert audit every claim.",
            "Maintenance is forever: equating, exposure control, renorming, fairness surveillance.",
        ],
        "requirements": [
            "Every rung of the ladder - this is the capstone.",
            "Project discipline: gates, evidence, documentation.",
        ],
        "standards": [
            "Workflow follows the Standards' operations chapters end to end.",
            "All stage evidence retained in the technical manual.",
        ],
        "citations": [C_STANDARDS, C_DEVELLIS, C_CROCKER],
        "sig_lens": (
            "Signature take: this is how his system builds every instrument "
            "it will ever trust - nine gates, no shortcuts, evidence at "
            "every step. The Signature workflow is the ladder made "
            "operational."
        ),
    },
]
