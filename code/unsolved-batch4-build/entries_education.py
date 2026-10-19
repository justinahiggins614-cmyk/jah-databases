#!/usr/bin/env python3
"""Entries for the Unsolved Education databases (batch 4).

34 famous open problems in education, ladder-ordered by accessibility.
ID prefixes: JAH-USED- (public) and JAH-USEDS- (signature), verified free
in the manifest id_prefix values (exact + substring, 2026-10-18) and across
all shard index files in jah-databases-data-1.

No website references. No Facebook. No religious framing. Nothing
hate-adjacent, profane, or inappropriate.
"""

ENTRIES = [
    dict(
        key="education-01",
        name="The Transfer of Learning Problem",
        group="Learning",
        ladder_rank=1,
        ladder_tier="foundations",
        problem=("Why does learning so rarely transfer - with students "
                 "mastering skills in class that vanish in new contexts?"),
        background=("Transfer is education's holy grail and chronic "
                    "failure: Latin was defended for 'mental discipline' "
                    "without evidence; modern studies show narrow, "
                    "near transfer but little far transfer. Theories "
                    "invoke identical elements, general principles, and "
                    "mindful abstraction - but reliable far transfer "
                    "remains elusive."),
        why_it_matters=("If learning does not transfer, schooling teaches "
                        "test-passing, not thinking. The problem is "
                        "education's foundational embarrassment."),
        sig_lens=("The Signature lens treats transfer as an abstraction "
                  "ledger: the Signature approach asks what learners "
                  "carry away besides the examples."),
        sig_body=("The Signature proposal models transfer as "
                  "abstraction-plus-cuing. Assumptions: (1) learners "
                  "encode examples, not principles, by default; (2) "
                  "abstraction needs explicit comparison; (3) new "
                  "contexts need retrieval cues. Reasoning path: the "
                  "proposal predicts far transfer should follow "
                  "compare-and-contrast instruction with varied examples "
                  "- which the best studies confirm. Transfer is then "
                  "teachable but not automatic: the failure is "
                  "pedagogical, not cognitive. Limits: the model needs "
                  "better transfer measures; some domains may resist."),
        pointer=('The Signature system models transfer as teachable through comparison and varied examples - a pedagogical failure, not a cognitive one. The Signature test: transfer tracks comparison instruction. It would be refuted if no instruction produces far transfer.'),
        key_points=[
            "Far transfer is rare; near transfer is common.",
            "Latin's mental-discipline defense lacked evidence.",
            "Comparison across varied examples aids transfer.",
            "The failure may be pedagogical, not cognitive.",
        ],
        requirements=[
            "Transfer measures by distance.",
            "Instructional comparisons testing the model.",
            "An account of domain differences.",
        ],
        standards=[
            "Claims checked against the transfer literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Thorndike EL, Woodworth RS. The influence of improvement in one mental function. 1901.",
            "Gick ML, Holyoak KJ. Schema induction and analogical transfer. 1983.",
        ],
        hypotheses=[
            "Comparison-based instruction produces far transfer.",
            "Far transfer is fundamentally limited.",
            "General principles transfer; skills do not.",
            "Motivation, not cognition, is the barrier.",
        ],
        confirm="Transfer tracks comparison instruction.",
        refute="No instruction produces far transfer.",
    ),
    dict(
        key="education-02",
        name="Phonics Versus Whole Language",
        group="Learning",
        ladder_rank=2,
        ladder_tier="foundations",
        problem=("How should reading be taught - systematic phonics, whole "
                 "language immersion, or some balance - and why did the "
                 "reading wars rage so long?"),
        background=("The science is unusually clear: systematic phonics "
                    "helps beginning readers decode. Yet whole-language "
                    "approaches persisted and recur, partly from "
                    "philosophical commitments about natural learning. "
                    "The puzzle is why strong evidence moved practice so "
                    "slowly - and what the optimal balance is."),
        why_it_matters=("Reading is the gateway skill. The wars' history "
                        "shows how education handles evidence."),
        sig_lens=("The Signature lens treats the wars as an evidence ledger: "
                  "the Signature approach asks why clear findings did "
                  "not settle practice."),
        sig_body=("The Signature proposal models the wars as "
                  "philosophy-versus-evidence conflict. Assumptions: (1) "
                  "the phonics evidence is strong for decoding; (2) "
                  "whole-language commitments are philosophical; (3) "
                  "teachers follow training, not journals. Reasoning "
                  "path: the proposal shows practice follows teacher "
                  "preparation pipelines, not research - predicting "
                  "that phonics adoption tracks training reform, which "
                  "it does. The optimal balance is then phonics-first "
                  "with rich language exposure; the wars persist where "
                  "pipelines lag. Limits: the model needs better "
                  "implementation data; comprehension instruction needs "
                  "separate study."),
        pointer=('The Signature system models the wars as training-pipeline lag, with phonics-first plus rich language as the optimal balance. The Signature test: adoption tracks training reform. It would be refuted if evidence-based training fails to change practice.'),
        key_points=[
            "Systematic phonics has strong evidence for decoding.",
            "Whole-language approaches recur despite the evidence.",
            "Teacher preparation pipelines drive practice.",
            "The optimal balance question remains.",
        ],
        requirements=[
            "Implementation data on phonics adoption.",
            "An account of pipeline effects.",
            "Comprehension-instruction research.",
        ],
        standards=[
            "Claims checked against the reading-science literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "National Reading Panel. Teaching Children to Read. 2000.",
            "Castles A et al. Ending the reading wars. Psychological Science in the Public Interest; 2018.",
        ],
        hypotheses=[
            "Pipeline reform settles the wars.",
            "Philosophical commitments sustain them.",
            "The balance question needs more research.",
            "Whole language has undervalued strengths.",
        ],
        confirm="Adoption tracks training reform.",
        refute="Evidence-based training fails to change practice.",
    ),
    dict(
        key="education-03",
        name="The Testing Effect Boundaries",
        group="Learning",
        ladder_rank=3,
        ladder_tier="foundations",
        problem=("Where are the boundaries of the testing effect - the "
                 "finding that retrieval practice beats restudying?"),
        background=("The testing effect is among the most robust findings "
                    "in learning science. But its boundaries are fuzzy: "
                    "does it work for complex material, for all learners, "
                    "under high stakes? Some failures to replicate and "
                    "moderator puzzles (feedback timing, test format) "
                    "keep the effect's limits open."),
        why_it_matters=("The testing effect is the most actionable finding "
                        "in education. Its boundaries determine its use."),
        sig_lens=("The Signature lens treats the effect as a retrieval "
                  "ledger: the Signature approach asks what retrieval "
                  "does to memory that restudying does not."),
        sig_body=("The Signature proposal models the testing effect as "
                  "retrieval-strengthening with feedback gating. "
                  "Assumptions: (1) retrieval strengthens memory traces; "
                  "(2) failed retrieval without feedback harms; (3) "
                  "complex material needs scaffolded retrieval. Reasoning "
                  "path: the proposal predicts the effect should hold "
                  "wherever retrieval succeeds with feedback - "
                  "explaining the boundary puzzles as feedback and "
                  "success-rate effects. Classroom application then "
                  "needs low-stakes frequent quizzing with feedback. "
                  "Limits: the model needs better complex-material "
                  "data; individual differences need study."),
        pointer=('The Signature system models the testing effect as retrieval-strengthening gated by feedback, with boundaries at success rates. The Signature test: effects track retrieval-success rates. It would be refuted if the effect fails with feedback controlled.'),
        key_points=[
            "Retrieval practice robustly beats restudying.",
            "Feedback timing and test format moderate the effect.",
            "Complex-material boundaries are fuzzy.",
            "Some failures to replicate exist.",
        ],
        requirements=[
            "Boundary tests with complex material.",
            "Feedback-timing experiments.",
            "Individual-difference analyses.",
        ],
        standards=[
            "Claims checked against the testing-effect literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Roediger HL, Karpicke JD. Test-enhanced learning. Psychological Science; 2006.",
            "Karpicke JD, Roediger HL. The critical importance of retrieval for learning. Science; 2008.",
        ],
        hypotheses=[
            "Feedback-gated retrieval explains the boundaries.",
            "The effect is universal across materials.",
            "Complex learning needs different mechanisms.",
            "The effect is overrated for real classrooms.",
        ],
        confirm="Effects track retrieval-success rates.",
        refute="The effect fails with feedback controlled.",
    ),
    dict(
        key="education-04",
        name="Growth Mindset: The Replication Story",
        group="Learning",
        ladder_rank=4,
        ladder_tier="foundations",
        problem=("Does growth-mindset intervention work - and what does its "
                 "replication trouble teach about educational psychology?"),
        background=("Dweck's mindset theory inspired global interventions; "
                    "then came meta-analyses finding tiny effects and "
                    "replication failures. The current state: small "
                    "effects for at-risk students, near-zero for others, "
                    "with implementation quality moderating everything. "
                    "The episode became a case study in the replication "
                    "crisis."),
        why_it_matters=("Mindset was education's most popular psychology. "
                        "Its fate calibrates how the field handles "
                        "evidence."),
        sig_lens=("The Signature lens treats the episode as a heterogeneity "
                  "ledger: the Signature approach asks for whom the "
                  "intervention works."),
        sig_body=("The Signature proposal models mindset effects as "
                  "heterogeneous and context-dependent. Assumptions: (1) "
                  "beliefs about malleability matter most where "
                  "stereotype threat or fixed-mindset cultures dominate; "
                  "(2) brief interventions need supportive contexts; (3) "
                  "implementation quality varies. Reasoning path: the "
                  "proposal predicts effects should concentrate among "
                  "at-risk students in unsupportive contexts - which "
                  "matches the data. The replication 'failure' is then "
                  "a heterogeneity discovery. Limits: the model needs "
                  "better context measures; the mechanisms need "
                  "tighter testing."),
        pointer=('The Signature system models mindset effects as heterogeneous, concentrated among at-risk students in unsupportive contexts. The Signature test: effects track at-risk status and context measures. It would be refuted if no subgroup shows effects in preregistered trials.'),
        key_points=[
            "Initial findings inspired global interventions.",
            "Meta-analyses found tiny average effects.",
            "Effects concentrate among at-risk students.",
            "Implementation quality moderates everything.",
        ],
        requirements=[
            "Heterogeneity analyses by student and context.",
            "Implementation-quality measures.",
            "Mechanism tests.",
        ],
        standards=[
            "Claims checked against the mindset literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Dweck CS. Mindset. Random House; 2006.",
            "Sisk VF et al. To what extent and under which circumstances are growth mind-sets important? Psychological Science; 2018.",
        ],
        hypotheses=[
            "Heterogeneous real effects explain the pattern.",
            "The effect is essentially zero.",
            "Context determines everything.",
            "Better interventions will show larger effects.",
        ],
        confirm="Effects track at-risk status and context measures.",
        refute="No subgroup shows effects in preregistered trials.",
    ),
    dict(
        key="education-05",
        name="Bilingual Education: The Timing",
        group="Learning",
        ladder_rank=5,
        ladder_tier="foundations",
        problem=("When should bilingual education start, in which language, "
                 "and for how long - the timing questions beneath the "
                 "politics?"),
        background=("The bilingual-education wars were political; the "
                    "research questions are empirical: does initial "
                    "literacy in the home language help or delay English? "
                    "Evidence favors home-language foundations (transfer "
                    "of literacy skills), but program quality dominates "
                    "language-of-instruction effects. The optimal timing "
                    "and duration remain open."),
        why_it_matters=("Millions of children learn in a second language. "
                        "The timing decisions shape their trajectories."),
        sig_lens=("The Signature lens treats bilingual timing as a "
                  "foundation ledger: the Signature approach asks what "
                  "transfers between languages."),
        sig_body=("The Signature proposal models bilingual development "
                  "as foundation-transfer. Assumptions: (1) literacy "
                  "skills transfer across languages; (2) weak first-"
                  "language foundations undermine second-language "
                  "learning; (3) program quality dominates. Reasoning "
                  "path: the proposal predicts home-language literacy "
                  "first should outperform early immersion where home "
                  "foundations are weak - which the evidence supports. "
                  "Timing then follows the foundation, not the politics. "
                  "Limits: the model needs better program-quality "
                  "measures; the politics constrain implementation."),
        pointer=('The Signature system models bilingual timing as foundation-dependent, with home-language literacy first where foundations are weak. The Signature test: outcomes track foundation strength by language. It would be refuted if timing shows no effect with quality controlled.'),
        key_points=[
            "The wars were political; the questions are empirical.",
            "Home-language literacy foundations aid second-language learning.",
            "Program quality dominates language-of-instruction effects.",
            "Optimal timing and duration remain open.",
        ],
        requirements=[
            "Foundation measures by language.",
            "Program-quality controls.",
            "Long-term outcome tracking.",
        ],
        standards=[
            "Claims checked against the bilingual-education literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Cummins J. Language, Power and Pedagogy. Multilingual Matters; 2000.",
            "Rolstad K et al. The big picture: a meta-analysis of program effectiveness. 2005.",
        ],
        hypotheses=[
            "Foundation-transfer determines optimal timing.",
            "Early immersion is always best.",
            "Program quality swamps timing effects.",
            "The politics make evidence irrelevant.",
        ],
        confirm="Outcomes track foundation strength by language.",
        refute="Timing shows no effect with quality controlled.",
    ),
    dict(
        key="education-06",
        name="Why Class Size Effects Vary",
        group="Teaching",
        ladder_rank=6,
        ladder_tier="foundations",
        problem=("Why do class-size reductions help sometimes, barely "
                 "matter other times, and cost so much always?"),
        background=("Tennessee's STAR experiment showed real gains from "
                    "small classes, especially for disadvantaged students. "
                    "But California's reduction flopped (teacher quality "
                    "dilution), and international comparisons are mixed. "
                    "The variation - by grade, subject, student "
                    "background, and implementation - is the puzzle."),
        why_it_matters=("Class-size reduction is the most expensive popular "
                        "reform. Its true return determines budgets."),
        sig_lens=("The Signature lens treats class size as an interaction "
                  "ledger: the Signature approach asks what smaller "
                  "classes let teachers do."),
        sig_body=("The Signature proposal models class-size effects as "
                  "interaction-mediated. Assumptions: (1) smaller classes "
                  "enable more individual interaction; (2) teachers must "
                  "change practice to use it; (3) hiring surges dilute "
                  "quality. Reasoning path: the proposal predicts gains "
                  "where teachers individualize (early grades, "
                  "disadvantaged students) and nulls where they lecture "
                  "identically or quality dilutes - explaining STAR "
                  "versus California. The reform works only with "
                  "practice change and quality maintenance. Limits: the "
                  "model needs better practice measures; the cost-"
                  "effectiveness question persists."),
        pointer=('The Signature system models class-size effects as interaction-mediated, working only with practice change and quality maintenance. The Signature test: gains track individualization measures. It would be refuted if gains appear with unchanged practice.'),
        key_points=[
            "STAR showed real gains, especially for disadvantaged students.",
            "California's reduction flopped on teacher dilution.",
            "Effects vary by grade, subject, and background.",
            "The reform is extremely expensive.",
        ],
        requirements=[
            "Practice-change measures in reduced classes.",
            "Teacher-quality tracking during hiring surges.",
            "Cost-effectiveness comparisons.",
        ],
        standards=[
            "Claims checked against the class-size literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Finn JD, Achilles CM. Tennessee's class size study. 1999.",
            "Jepsen C, Rivkin S. Class size reduction and student achievement. 2009.",
        ],
        hypotheses=[
            "Interaction mediation explains the variation.",
            "Small classes always help; implementation is the issue.",
            "The effects are too small for the cost.",
            "Teacher quality dominates class size entirely.",
        ],
        confirm="Gains track individualization measures.",
        refute="Gains appear with unchanged practice.",
    ),
    dict(
        key="education-07",
        name="Teacher Value-Added: How Stable",
        group="Teaching",
        ladder_rank=7,
        ladder_tier="foundations",
        problem=("How stable and fair are teacher value-added measures - "
                 "and should they drive personnel decisions?"),
        background=("Value-added models estimate teacher effects on test "
                    "scores; they predict long-term outcomes (Chetty). But "
                    "the measures are noisy year to year, sensitive to "
                    "model choices, and may punish teachers of "
                    "disadvantaged students. Whether they are stable "
                    "enough for high-stakes use remains contested."),
        why_it_matters=("Value-added drives hiring, firing, and pay in "
                        "many systems. Its stability determines its "
                        "justice."),
        sig_lens=("The Signature lens treats value-added as a signal ledger: "
                  "the Signature approach asks how much is teacher and "
                  "how much is noise."),
        sig_body=("The Signature proposal models value-added as a noisy "
                  "signal of real effects. Assumptions: (1) teacher "
                  "effects are real (Chetty's long-term findings); (2) "
                  "year-to-year estimates contain large noise; (3) "
                  "noise shrinks with multiple years. Reasoning path: "
                  "the proposal predicts multi-year averages should be "
                  "stable enough for low-stakes use but not for firing "
                  "- which matches the evidence. The measures are then "
                  "useful diagnostics, dangerous verdicts. Limits: the "
                  "model needs better noise decomposition; the "
                  "disadvantaged-student bias needs addressing."),
        pointer=('The Signature system models value-added as a noisy signal: useful for diagnosis, dangerous for high-stakes verdicts. The Signature test: stability rises with averaging as predicted. It would be refuted if multi-year measures remain unstable.'),
        key_points=[
            "Teacher effects predict long-term student outcomes.",
            "Year-to-year estimates are noisy.",
            "Model choices affect the rankings.",
            "High-stakes use remains contested.",
        ],
        requirements=[
            "Noise decomposition by teacher and year.",
            "Long-term validation studies.",
            "Bias audits for disadvantaged classrooms.",
        ],
        standards=[
            "Claims checked against the value-added literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Chetty R et al. Measuring the impacts of teachers. American Economic Review; 2014.",
            "Rothstein J. Teacher quality in educational production. 2010.",
        ],
        hypotheses=[
            "Multi-year averages are stable enough for low-stakes use.",
            "The measures are too noisy for any personnel use.",
            "Bias against disadvantaged classrooms is fatal.",
            "Better models will stabilize the measures.",
        ],
        confirm="Stability rises with averaging as predicted.",
        refute="Multi-year measures remain unstable.",
    ),
    dict(
        key="education-08",
        name="The Two-Sigma Tutoring Problem",
        group="Teaching",
        ladder_rank=8,
        ladder_tier="foundations",
        problem=("Can the two-sigma gain of one-on-one tutoring be scaled - "
                 "or is it inherently unscalable?"),
        background=("Bloom found tutored students outperformed classroom "
                    "students by two standard deviations. Scaling attempts "
                    "- small groups, peer tutoring, AI tutors - recover "
                    "part of the gain but not all. What exactly tutoring "
                    "provides (feedback, pacing, relationship) determines "
                    "what can be scaled."),
        why_it_matters=("Two sigma is the largest effect in education. "
                        "Scaling even half of it would transform "
                        "outcomes."),
        sig_lens=("The Signature lens treats tutoring as a feedback ledger: "
                  "the Signature approach asks what the tutor does moment "
                  "to moment."),
        sig_body=("The Signature proposal models tutoring gains as "
                  "rapid-feedback loops. Assumptions: (1) tutors diagnose "
                  "and correct misconceptions instantly; (2) pacing "
                  "matches the learner; (3) the relationship sustains "
                  "effort. Reasoning path: the proposal predicts scaled "
                  "versions should recover the feedback and pacing "
                  "components but not the relationship - explaining why "
                  "small-group and AI tutoring get partway. The "
                  "scalable core is then diagnostic feedback at the "
                  "learner's pace. Limits: the model needs better "
                  "component decomposition; the relationship effect "
                  "needs measuring."),
        pointer=('The Signature system models tutoring gains as rapid-feedback loops, with the diagnostic-pacing core being the scalable part. The Signature test: scaled feedback interventions recover most of the gain. It would be refuted if no scaled version exceeds small effects.'),
        key_points=[
            "One-on-one tutoring yields two-sigma gains.",
            "Scaling attempts recover part of the gain.",
            "Feedback, pacing, and relationship are the candidate mechanisms.",
            "AI tutors are the newest scaling attempt.",
        ],
        requirements=[
            "Component decomposition of tutoring effects.",
            "Scaled-intervention trials.",
            "Relationship-effect measures.",
        ],
        standards=[
            "Claims checked against the tutoring literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Bloom BS. The 2 sigma problem. Educational Researcher; 1984.",
            "Nickow A et al. The impressive effects of tutoring. 2020.",
        ],
        hypotheses=[
            "Diagnostic feedback is the scalable core.",
            "The relationship is irreplaceable.",
            "AI tutors will close most of the gap.",
            "Two sigma is unreplicable under scrutiny.",
        ],
        confirm="Scaled feedback interventions recover most of the gain.",
        refute="No scaled version exceeds small effects.",
    ),
    dict(
        key="education-09",
        name="Direct Instruction Versus Discovery",
        group="Teaching",
        ladder_rank=9,
        ladder_tier="foundations",
        problem=("When should teachers tell and when should students "
                 "discover - and why does the debate never end?"),
        background=("Direct instruction has strong evidence for novices; "
                    "discovery learning has philosophical appeal and "
                    "some evidence for motivated, knowledgeable learners. "
                    "Kirschner, Sweller, and Clark argued against "
                    "minimal guidance; Hmelo-Silver replied the "
                    "dichotomy is false. The expertise-reversal effect - "
                    "guidance helps novices, hinders experts - may "
                    "resolve it."),
        why_it_matters=("The tell-versus-discover choice shapes every "
                        "lesson. The answer determines pedagogy's "
                        "foundation."),
        sig_lens=("The Signature lens treats the debate as an expertise "
                  "ledger: the Signature approach asks what the learner "
                  "already knows."),
        sig_body=("The Signature proposal models the optimal guidance as "
                  "expertise-dependent. Assumptions: (1) novices lack "
                  "schemas to guide discovery; (2) experts have them; "
                  "(3) guidance that helps novices bores experts. "
                  "Reasoning path: the proposal predicts direct "
                  "instruction should win for novices and discovery for "
                  "experts - the expertise-reversal effect, which the "
                  "evidence supports. The debate then persists because "
                  "each side generalizes from its expertise level. "
                  "Limits: the model needs better expertise measures; "
                  "motivational effects need integration."),
        pointer=('The Signature system models optimal guidance as expertise-dependent, with the expertise-reversal effect resolving the debate. The Signature test: guidance effects reverse with expertise. It would be refuted if one method wins regardless of expertise.'),
        key_points=[
            "Direct instruction has strong evidence for novices.",
            "Discovery appeals philosophically and for experts.",
            "The expertise-reversal effect may resolve the debate.",
            "Each side generalizes from its own expertise level.",
        ],
        requirements=[
            "Expertise measures in guidance studies.",
            "Motivational outcome integration.",
            "An account of the debate's persistence.",
        ],
        standards=[
            "Claims checked against the instruction literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Kirschner PA et al. Why minimal guidance does not work. Educational Psychologist; 2006.",
            "Kalyuga S et al. The expertise reversal effect. 2003.",
        ],
        hypotheses=[
            "Expertise-reversal resolves the debate.",
            "Direct instruction is generally superior.",
            "Discovery is generally superior with scaffolding.",
            "The dichotomy itself is false.",
        ],
        confirm="Guidance effects reverse with expertise.",
        refute="One method wins regardless of expertise.",
    ),
    dict(
        key="education-10",
        name="Homework: Does It Work",
        group="Teaching",
        ladder_rank=10,
        ladder_tier="foundations",
        problem=("Does homework improve learning - and for whom, how much, "
                 "and at what cost?"),
        background=("Meta-analyses find homework helps in secondary school "
                    "but little in elementary; the effects are modest and "
                    "inequality-amplifying (advantaged homes help more). "
                    "Some schools abolished it with little achievement "
                    "loss. Whether homework's benefits outweigh its costs "
                    "- stress, inequity, lost childhood - remains open."),
        why_it_matters=("Homework shapes family life for billions. Its true "
                        "return determines policy."),
        sig_lens=("The Signature lens treats homework as an equity ledger: "
                  "the Signature approach asks who can do it well."),
        sig_body=("The Signature proposal models homework effects as "
                  "home-resource dependent. Assumptions: (1) homework "
                  "needs quiet space, help, and materials; (2) these "
                  "vary by class; (3) practice helps those who can do "
                  "it. Reasoning path: the proposal predicts homework "
                  "should help advantaged secondary students most and "
                  "harm equity overall - which matches the evidence. "
                  "The policy implication: in-school practice over "
                  "homework, especially early. Limits: the model needs "
                  "better homework-quality data; the abolition "
                  "experiments need longer follow-up."),
        pointer=('The Signature system models homework as home-resource dependent, helping the advantaged most and widening inequity. The Signature test: effects track home-resource measures. It would be refuted if disadvantaged students benefit equally.'),
        key_points=[
            "Homework helps in secondary school, little in elementary.",
            "Effects are modest and inequality-amplifying.",
            "Some abolitions showed little achievement loss.",
            "Costs include stress and lost family time.",
        ],
        requirements=[
            "Home-resource measures in homework studies.",
            "Long-term abolition follow-ups.",
            "Homework-quality analyses.",
        ],
        standards=[
            "Claims checked against the homework literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Cooper H et al. Does homework improve academic achievement? Review of Educational Research; 2006.",
            "Kohn A. The Homework Myth. Da Capo; 2006.",
        ],
        hypotheses=[
            "Home-resource dependence explains the pattern.",
            "Homework is generally beneficial.",
            "Homework should be abolished, especially early.",
            "Quality matters more than quantity.",
        ],
        confirm="Effects track home-resource measures.",
        refute="Disadvantaged students benefit equally.",
    ),
    dict(
        key="education-11",
        name="Grades: Do They Help or Harm",
        group="Assessment",
        ladder_rank=11,
        ladder_tier="foundations",
        problem=("Do grades motivate learning or undermine it - and what "
                 "would replace them?"),
        background=("Grades provide feedback and incentives but also breed "
                    "grade-grubbing, cheating, and performance goals over "
                    "mastery. Ungrading experiments show promise but face "
                    "institutional resistance. Whether the motivational "
                    "benefits outweigh the costs remains education's most "
                    "practical open question."),
        why_it_matters=("Grades are education's currency. Their true "
                        "effects determine assessment's future."),
        sig_lens=("The Signature lens treats grades as an incentive ledger: "
                  "the Signature approach asks what behavior the currency "
                  "buys."),
        sig_body=("The Signature proposal models grades as incentives "
                  "with goal-displacement costs. Assumptions: (1) grades "
                  "motivate effort; (2) they shift goals from mastery to "
                  "performance; (3) the shift harms deep learning. "
                  "Reasoning path: the proposal predicts grades should "
                  "raise measured performance while reducing intrinsic "
                  "motivation and risk-taking - which the evidence "
                  "supports. Alternatives (narrative feedback, mastery "
                  "transcripts) then trade comparability for learning. "
                  "Limits: the model needs better long-term outcome "
                  "data; institutional needs for sorting are real."),
        pointer=('The Signature system models grades as raising measured performance while displacing mastery goals. The Signature test: motivation shifts track grading intensity. It would be refuted if graded students show equal mastery orientation.'),
        key_points=[
            "Grades motivate effort but breed strategic behavior.",
            "Performance goals displace mastery goals.",
            "Ungrading experiments show promise.",
            "Institutional sorting needs sustain grades.",
        ],
        requirements=[
            "Long-term outcome comparisons.",
            "Alternative-assessment evaluations.",
            "An account of institutional sorting needs.",
        ],
        standards=[
            "Claims checked against the assessment literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Butler R, Nisan M. Effects of no feedback, task-related comments, and grades. 1986.",
            "Blum SD. Ungrading. West Virginia University Press; 2020.",
        ],
        hypotheses=[
            "Goal displacement is the central cost.",
            "Grades are net beneficial.",
            "Alternatives outperform grades.",
            "The effects are too contextual to generalize.",
        ],
        confirm="Motivation shifts track grading intensity.",
        refute="Graded students show equal mastery orientation.",
    ),
    dict(
        key="education-12",
        name="Standardized Testing: What Does It Measure",
        group="Assessment",
        ladder_rank=12,
        ladder_tier="compounded",
        problem=("What do standardized tests actually measure - learning, "
                 "aptitude, test-taking skill, or family background?"),
        background=("Tests predict later outcomes, suggesting they measure "
                    "something real; but they correlate strongly with "
                    "parental income, and test prep raises scores without "
                    "raising learning. The construct-validity debate - "
                    "what the scores mean - underlies every testing "
                    "controversy."),
        why_it_matters=("Tests allocate opportunity: admissions, funding, "
                        "accountability. Their meaning determines their "
                        "justice."),
        sig_lens=("The Signature lens treats tests as a construct ledger: "
                  "the Signature approach asks what variance the scores "
                  "contain."),
        sig_body=("The Signature proposal models test scores as "
                  "multi-component: learned knowledge, general "
                  "cognitive skill, test-specific skill, and background "
                  "resources. Assumptions: (1) each component "
                  "contributes; (2) preparation moves the test-skill "
                  "component; (3) background moves resources. Reasoning "
                  "path: the proposal predicts scores should predict "
                  "outcomes (they capture real learning) while "
                  "correlating with income (resources) - both true. "
                  "Tests are then valid-but-contaminated measures. "
                  "Limits: the model needs component decomposition; "
                  "the fairness implications need separate analysis."),
        pointer=('The Signature system models test scores as valid-but-contaminated measures of learning, skill, and background. The Signature test: components predict differentially by outcome. It would be refuted if scores reduce to a single component.'),
        key_points=[
            "Tests predict later outcomes substantially.",
            "Scores correlate strongly with parental income.",
            "Test prep raises scores without raising learning.",
            "Construct validity underlies every controversy.",
        ],
        requirements=[
            "Component decomposition of score variance.",
            "Fairness analyses by use case.",
            "An account of preparation effects.",
        ],
        standards=[
            "Claims checked against the testing literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Sackett PR et al. High-stakes testing in employment, credentialing, and higher education. 2008.",
            "Koretz D. Measuring Up. Harvard University Press; 2008.",
        ],
        hypotheses=[
            "Multi-component models explain the pattern.",
            "Tests measure mostly background.",
            "Tests measure mostly learning.",
            "The meaning depends on the use.",
        ],
        confirm="Components predict differentially by outcome.",
        refute="Scores reduce to a single component.",
    ),
    dict(
        key="education-13",
        name="The Summer Slide",
        group="Equity",
        ladder_rank=13,
        ladder_tier="compounded",
        problem=("Do children lose learning over summer - and does the loss "
                 "explain the achievement gap?"),
        background=("Early research found summer learning loss, larger for "
                    "low-income students, explaining much of the gap. Then "
                    "came challenges: the findings may be test-artifact "
                    "(scaling, timing). Recent studies with better "
                    "measures find smaller losses. Whether summer "
                    "explains the gap or school explains it remains "
                    "contested."),
        why_it_matters=("If summer explains the gap, the fix is summer "
                        "programs; if school does, the fix is school "
                        "reform. The attribution determines billions in "
                        "spending."),
        sig_lens=("The Signature lens treats summer as a measurement "
                  "ledger: the Signature approach asks what the tests "
                  "show versus what children know."),
        sig_body=("The Signature proposal models the slide as partly "
                  "real, partly artifactual. Assumptions: (1) test "
                  "scaling affects growth estimates; (2) advantaged "
                  "children get summer enrichment; (3) both operate. "
                  "Reasoning path: the proposal predicts genuine but "
                  "smaller losses with better measures - which recent "
                  "studies confirm. Summer then contributes to the gap "
                  "without explaining it; both summer programs and "
                  "school reform are needed. Limits: the model needs "
                  "better summer-activity data; the artifact debate "
                  "continues."),
        pointer=('The Signature system models the summer slide as partly real and partly measurement artifact, contributing to but not explaining the gap. The Signature test: losses shrink with better measurement. It would be refuted if losses persist undiminished with better measures.'),
        key_points=[
            "Early research found large summer losses for low-income students.",
            "Test-artifact challenges followed.",
            "Recent better-measured studies find smaller losses.",
            "The attribution determines spending priorities.",
        ],
        requirements=[
            "Summer-activity data by background.",
            "Measurement-artifact analyses.",
            "Summer-program evaluations.",
        ],
        standards=[
            "Claims checked against the summer-learning literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Alexander KL et al. Lasting consequences of the summer learning gap. American Sociological Review; 2007.",
            "von Hippel PT, Hamrock C. Do test score gaps grow before, during, or between school years? 2019.",
        ],
        hypotheses=[
            "Partly-real-partly-artifact explains the literature.",
            "Summer fully explains the gap.",
            "School fully explains the gap.",
            "The slide is entirely artifactual.",
        ],
        confirm="Losses shrink with better measurement.",
        refute="Losses persist undiminished with better measures.",
    ),
    dict(
        key="education-14",
        name="The Achievement Gap: What Closes It",
        group="Equity",
        ladder_rank=14,
        ladder_tier="compounded",
        problem=("What actually closes achievement gaps - and why do so "
                 "many interventions fade?"),
        background=("Gaps by race and class are large and persistent. "
                    "Interventions (tutoring, charters, early childhood) "
                    "show effects that often fade after the program ends. "
                    "The fadeout puzzle - why gains do not sustain - may "
                    "be the key: later environments do not maintain "
                    "early advantages."),
        why_it_matters=("Closing gaps is education's moral center. The "
                        "fadeout puzzle determines strategy."),
        sig_lens=("The Signature lens treats gaps as an environment "
                  "ledger: the Signature approach asks what sustains "
                  "gains after programs end."),
        sig_body=("The Signature proposal models gap-closing as "
                  "environment-sustained. Assumptions: (1) interventions "
                  "build real skills; (2) later environments determine "
                  "whether skills compound; (3) disadvantaged students "
                  "face worse later environments. Reasoning path: the "
                  "proposal predicts fadeout where later schooling is "
                  "weak - which the data support - making sustained "
                  "environments, not one-shot programs, the answer. "
                  "Gap-closing then needs pipeline reform, not "
                  "interventions. Limits: the model needs better "
                  "environment measures; some programs may sustain."),
        pointer=('The Signature system models gap-closing as environment-sustained: fadeout reflects weak later schooling, not failed programs. The Signature test: fadeout tracks later-environment quality. It would be refuted if gains sustain regardless of later schooling.'),
        key_points=[
            "Gaps by race and class are large and persistent.",
            "Intervention effects often fade.",
            "Fadeout may reflect later environments.",
            "Pipeline reform may beat one-shot programs.",
        ],
        requirements=[
            "Later-environment measures in follow-ups.",
            "Sustained-intervention trials.",
            "An account of fadeout mechanisms.",
        ],
        standards=[
            "Claims checked against the gap literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Fryer RG, Levitt SD. Understanding the black-white test score gap. 2004.",
            "Bailey MJ et al. Persistence and fadeout of intervention effects. 2017.",
        ],
        hypotheses=[
            "Environment sustenance explains fadeout.",
            "Programs build the wrong skills.",
            "Fadeout is measurement artifact.",
            "Some programs do sustain; study them.",
        ],
        confirm="Fadeout tracks later-environment quality.",
        refute="Gains sustain regardless of later schooling.",
    ),
    dict(
        key="education-15",
        name="School Funding: Does Money Matter",
        group="Policy",
        ladder_rank=15,
        ladder_tier="compounded",
        problem=("Does school funding improve outcomes - settling the "
                 "decades-long money-matters debate?"),
        background=("Hanushek argued money does not matter (throwing "
                    "money at schools); Card, Krueger, and newer "
                    "court-order studies found funding increases raise "
                    "achievement and attainment. The consensus shifted: "
                    "money matters, especially for disadvantaged "
                    "students - but how it is spent matters more."),
        why_it_matters=("Funding equity lawsuits and budgets hinge on the "
                        "answer. The consensus shift reshaped policy."),
        sig_lens=("The Signature lens treats funding as a spending ledger: "
                  "the Signature approach asks what the money buys."),
        sig_body=("The Signature proposal models funding effects as "
                  "use-mediated. Assumptions: (1) money enables inputs "
                  "(teachers, programs); (2) input quality varies; (3) "
                  "disadvantaged students need more. Reasoning path: "
                  "the proposal predicts funding should help where it "
                  "buys quality inputs for needy students - matching "
                  "the court-order studies. 'Money matters' is then "
                  "true but incomplete: the spending pattern is the "
                  "mechanism. Limits: the model needs better spending "
                  "breakdowns; the political economy of allocation "
                  "needs study."),
        pointer=('The Signature system models funding effects as use-mediated: money matters where it buys quality inputs for needy students. The Signature test: effects track input-quality measures. It would be refuted if funding helps regardless of spending patterns.'),
        key_points=[
            "The consensus shifted toward money matters.",
            "Court-order studies show funding raises outcomes.",
            "Effects are largest for disadvantaged students.",
            "How money is spent matters more than how much.",
        ],
        requirements=[
            "Spending-breakdown analyses.",
            "Allocation political-economy studies.",
            "Long-term outcome tracking.",
        ],
        standards=[
            "Claims checked against the school-finance literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Jackson CK et al. The effects of school spending on educational and economic outcomes. Quarterly Journal of Economics; 2016.",
            "Hanushek EA. The economics of schooling. 1986.",
        ],
        hypotheses=[
            "Use-mediation explains the pattern.",
            "Money always matters.",
            "Money never matters; only reform does.",
            "Only targeted spending matters.",
        ],
        confirm="Effects track input-quality measures.",
        refute="Funding helps regardless of spending patterns.",
    ),
    dict(
        key="education-16",
        name="Charter Schools: Do They Work",
        group="Policy",
        ladder_rank=16,
        ladder_tier="compounded",
        problem=("Do charter schools outperform traditional public schools - "
                 "and which ones, for whom?"),
        background=("Lottery studies (Boston, New York) found large gains "
                    "from urban no-excuses charters; national studies "
                    "(CREDO) find average charters match traditional "
                    "schools, with wide variation. The heterogeneity - "
                    "some charters transform, most do not - is the real "
                    "finding."),
        why_it_matters=("Charters are education's most contested reform. "
                        "The heterogeneity determines policy."),
        sig_lens=("The Signature lens treats charters as a practice "
                  "ledger: the Signature approach asks what the "
                  "effective ones do."),
        sig_body=("The Signature proposal models charter effects as "
                  "practice-driven, not structure-driven. Assumptions: "
                  "(1) the charter label enables but does not guarantee "
                  "practices; (2) high-expectations, tutoring, and "
                  "extended time drive the gains; (3) selection "
                  "complicates comparisons. Reasoning path: the "
                  "proposal predicts lottery winners should outperform "
                  "where the charter implements proven practices - "
                  "which matches the urban no-excuses results. The "
                  "policy question is then practice replication, not "
                  "charter expansion. Limits: the model needs better "
                  "practice measures; the political debate resists "
                  "nuance."),
        pointer=('The Signature system models charter effects as practice-driven: the question is practice replication, not charter expansion. The Signature test: gains track practice measures. It would be refuted if charter status predicts gains without practices.'),
        key_points=[
            "Lottery studies found large urban charter gains.",
            "National averages show charters matching traditional schools.",
            "Heterogeneity is the real finding.",
            "Selection effects complicate comparisons.",
        ],
        requirements=[
            "Practice measures across charters.",
            "Lottery-based causal studies.",
            "Replication trials of effective practices.",
        ],
        standards=[
            "Claims checked against the charter literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Angrist JD et al. Explaining charter school effectiveness. American Economic Journal; 2013.",
            "CREDO. As a Matter of Fact: National Charter School Study III. 2023.",
        ],
        hypotheses=[
            "Practice-driven effects explain heterogeneity.",
            "Charters inherently outperform.",
            "Charters inherently underperform.",
            "Selection explains all differences.",
        ],
        confirm="Gains track practice measures.",
        refute="Charter status predicts gains without practices.",
    ),
    dict(
        key="education-17",
        name="School Choice: The Effects",
        group="Policy",
        ladder_rank=17,
        ladder_tier="compounded",
        problem=("What are the system-wide effects of school choice - "
                 "vouchers, open enrollment, and market competition?"),
        background=("Choice advocates predict competition improves all "
                    "schools; critics predict cream-skimming and "
                    "segregation. Evidence: modest test gains for "
                    "choosers, competitive effects debated, segregation "
                    "effects real in some systems. The general-"
                    "equilibrium effects - what choice does to the "
                    "whole system - remain the open question."),
        why_it_matters=("Choice is expanding rapidly. Its system effects "
                        "determine whether markets help education."),
        sig_lens=("The Signature lens treats choice as a sorting ledger: "
                  "the Signature approach asks who moves and what "
                  "remains."),
        sig_body=("The Signature proposal models choice effects as "
                  "sorting-plus-competition. Assumptions: (1) choosers "
                  "are more advantaged and informed; (2) schools respond "
                  "to competitive pressure; (3) the left-behind "
                  "concentrate disadvantage. Reasoning path: the "
                  "proposal predicts chooser gains with system-level "
                  "sorting costs - matching the evidence pattern. "
                  "Whether competition benefits outweigh sorting costs "
                  "is then the empirical question, varying by design. "
                  "Limits: the model needs better general-equilibrium "
                  "studies; design details dominate."),
        pointer=('The Signature system models choice as sorting plus competition, with net effects varying by design. The Signature test: net effects track design features. It would be refuted if choice shows uniform system effects.'),
        key_points=[
            "Choosers show modest test gains.",
            "Competitive effects on other schools are debated.",
            "Segregation effects appear in some systems.",
            "System-wide effects remain the open question.",
        ],
        requirements=[
            "General-equilibrium studies.",
            "Sorting measures by design.",
            "Long-term system outcome tracking.",
        ],
        standards=[
            "Claims checked against the school-choice literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Hoxby CM. Does competition among public schools benefit students and taxpayers? American Economic Review; 2000.",
            "Ladd HF. School vouchers: a critical view. 2002.",
        ],
        hypotheses=[
            "Sorting-plus-competition explains the pattern.",
            "Competition benefits dominate.",
            "Sorting costs dominate.",
            "Design details determine everything.",
        ],
        confirm="Net effects track design features.",
        refute="Choice shows uniform system effects.",
    ),
    dict(
        key="education-18",
        name="Teacher Pay: Does It Matter",
        group="Policy",
        ladder_rank=18,
        ladder_tier="compounded",
        problem=("Does teacher pay affect who teaches and how well students "
                 "learn - and what pay structure works?"),
        background=("Higher pay attracts stronger candidates and reduces "
                    "turnover; merit pay experiments show mixed results. "
                    "The puzzles: why pay effects on achievement are "
                    "modest given selection effects, and whether "
                    "performance pay can work without corrupting "
                    "collaboration."),
        why_it_matters=("Teacher labor markets shape the profession. Pay "
                        "policy determines who teaches."),
        sig_lens=("The Signature lens treats pay as a selection ledger: "
                  "the Signature approach asks who enters and stays."),
        sig_body=("The Signature proposal models pay effects as "
                  "selection-dominant. Assumptions: (1) pay shifts the "
                  "applicant pool; (2) retention effects compound; (3) "
                  "merit pay distorts multitask jobs. Reasoning path: "
                  "the proposal predicts base-pay increases should "
                  "improve the workforce slowly while merit pay shows "
                  "mixed results - which matches the evidence. The "
                  "mechanism is who teaches, not how hard they try. "
                  "Limits: the model needs better applicant-pool data; "
                  "the merit-pay design space needs exploration."),
        pointer=('The Signature system models pay effects as selection-dominant: base pay shapes who teaches; merit pay shows mixed results. The Signature test: workforce quality tracks base pay. It would be refuted if pay changes show no workforce effects.'),
        key_points=[
            "Higher pay attracts stronger candidates.",
            "Turnover falls with better pay.",
            "Merit pay experiments are mixed.",
            "Achievement effects of pay are modest.",
        ],
        requirements=[
            "Applicant-pool quality data.",
            "Long-term workforce composition tracking.",
            "Merit-pay design experiments.",
        ],
        standards=[
            "Claims checked against the teacher-pay literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Hendricks MD. Does it pay to pay teachers more? Economics of Education Review; 2014.",
            "Springer MG et al. Teacher pay for performance. 2010.",
        ],
        hypotheses=[
            "Selection dominance explains the pattern.",
            "Pay motivates effort directly.",
            "Merit pay can be designed to work.",
            "Working conditions matter more than pay.",
        ],
        confirm="Workforce quality tracks base pay.",
        refute="Pay changes show no workforce effects.",
    ),
    dict(
        key="education-19",
        name="The Curriculum Wars",
        group="Policy",
        ladder_rank=19,
        ladder_tier="compounded",
        problem=("What should schools teach - and who decides when the "
                 "curriculum becomes a culture war?"),
        background=("From the 1990s history standards to today's battles "
                    "over curricula, the question of what schools teach "
                    "is perennially political. The deeper puzzle: whether "
                    "curriculum content causally affects learning and "
                    "citizenship, or whether the wars are symbolic "
                    "politics over schools' expressive function."),
        why_it_matters=("Curriculum shapes what the next generation knows. "
                        "The wars determine who controls it."),
        sig_lens=("The Signature lens treats curriculum as an expressive "
                  "ledger: the Signature approach asks what the fight is "
                  "really about."),
        sig_body=("The Signature proposal models curriculum wars as "
                  "expressive politics with real pedagogical stakes. "
                  "Assumptions: (1) content choices signal values; (2) "
                  "knowledge-rich curricula aid learning; (3) the "
                  "symbolic and pedagogical mix. Reasoning path: the "
                  "proposal predicts the fiercest fights where symbolic "
                  "stakes are highest (history, literature) while "
                  "pedagogical evidence (knowledge-rich curricula help) "
                  "gets ignored - matching the pattern. Both dimensions "
                  "need addressing separately. Limits: the model needs "
                  "better curriculum-effect studies; the symbolic "
                  "dimension resists evidence."),
        pointer=('The Signature system models curriculum wars as expressive politics layered over real pedagogical stakes. The Signature test: fight intensity tracks symbolic stakes. It would be refuted if curriculum battles follow pedagogical evidence.'),
        key_points=[
            "Curriculum battles recur across decades.",
            "The fights concentrate on history and literature.",
            "Knowledge-rich curricula show learning benefits.",
            "Symbolic and pedagogical stakes mix.",
        ],
        requirements=[
            "Curriculum-effect studies by subject.",
            "An account of the symbolic dimension.",
            "Decision-process analyses.",
        ],
        standards=[
            "Claims checked against the curriculum literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Hirsch ED. Cultural Literacy. Houghton Mifflin; 1987.",
            "Nash GB et al. History on Trial. Knopf; 1997.",
        ],
        hypotheses=[
            "Expressive-plus-pedagogical models explain the wars.",
            "The wars are purely symbolic.",
            "Curriculum content strongly shapes outcomes.",
            "Pedagogy matters more than content.",
        ],
        confirm="Fight intensity tracks symbolic stakes.",
        refute="Curriculum battles follow pedagogical evidence.",
    ),
    dict(
        key="education-20",
        name="Social-Emotional Learning: The Evidence",
        group="Learning",
        ladder_rank=20,
        ladder_tier="compounded",
        problem=("Does social-emotional learning (SEL) improve outcomes - "
                 "and what exactly is it?"),
        background=("SEL programs claim academic and behavioral benefits; "
                    "meta-analyses find modest positive effects. But the "
                    "construct is fuzzy (self-awareness? grit? "
                    "mindfulness?), implementation varies wildly, and "
                    "critics see therapeutic overreach. Whether SEL is a "
                    "coherent intervention with real effects remains "
                    "open."),
        why_it_matters=("SEL is in millions of classrooms. Its coherence "
                        "determines whether the investment is sound."),
        sig_lens=("The Signature lens treats SEL as a construct ledger: "
                  "the Signature approach asks what the programs "
                  "actually do."),
        sig_body=("The Signature proposal models SEL effects as "
                  "relationship-and-routine driven. Assumptions: (1) "
                  "the 'SEL' label covers diverse practices; (2) the "
                  "effective ones build teacher-student relationships "
                  "and classroom routines; (3) the branded curricula "
                  "add little. Reasoning path: the proposal predicts "
                  "effects should track implementation of relational "
                  "practices, not curriculum fidelity - which the "
                  "evidence suggests. SEL is then a useful banner for "
                  "good teaching practices, not a distinct science. "
                  "Limits: the model needs better practice "
                  "decomposition; the therapeutic critiques need "
                  "addressing."),
        pointer=('The Signature system models SEL as a useful banner for relational teaching practices rather than a distinct science. The Signature test: effects track relational-practice measures. It would be refuted if branded curricula outperform generic good teaching.'),
        key_points=[
            "Meta-analyses find modest positive effects.",
            "The construct covers diverse practices.",
            "Implementation varies wildly.",
            "Critics allege therapeutic overreach.",
        ],
        requirements=[
            "Practice decomposition of SEL programs.",
            "Implementation-quality measures.",
            "An account of the therapeutic critiques.",
        ],
        standards=[
            "Claims checked against the SEL literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Durlak JA et al. The impact of enhancing students' social and emotional learning. Child Development; 2011.",
            "Jones SM, Doolittle EJ. Social and emotional learning. 2017.",
        ],
        hypotheses=[
            "Relational practices drive the effects.",
            "SEL is a coherent distinct intervention.",
            "The effects are placebo and reporting bias.",
            "SEL needs tighter constructs.",
        ],
        confirm="Effects track relational-practice measures.",
        refute="Branded curricula outperform generic good teaching.",
    ),
    dict(
        key="education-21",
        name="Attention Spans: Are They Shrinking",
        group="Learning",
        ladder_rank=21,
        ladder_tier="compounded",
        problem=("Are students' attention spans shrinking - and is "
                 "technology the cause?"),
        background=("The claim is ubiquitous; the evidence is thin. "
                    "Attention is task-dependent, and measures of "
                    "'span' are crude. What is real: task-switching "
                    "increased, sustained reading declined, and "
                    "classroom attention is harder to hold. Whether "
                    "capacity shrank or habits changed remains open."),
        why_it_matters=("Attention is learning's gateway. The diagnosis "
                        "determines the response."),
        sig_lens=("The Signature lens treats attention as a habit ledger: "
                  "the Signature approach asks what changed - capacity "
                  "or allocation."),
        sig_body=("The Signature proposal models the change as "
                  "allocation, not capacity. Assumptions: (1) "
                  "attentional capacity is stable; (2) habits of "
                  "switching increased; (3) environments got more "
                  "distracting. Reasoning path: the proposal predicts "
                  "students should sustain attention where motivated "
                  "and undistracted - which they do (gaming, films) - "
                  "making the problem environmental and habitual. The "
                  "fix is then environment design, not capacity "
                  "building. Limits: the model needs better attention "
                  "measures; developmental effects need study."),
        pointer=('The Signature system models attention change as allocation habits, not shrinking capacity - an environment-design problem. The Signature test: attention tracks motivation and environment. It would be refuted if capacity measures declined across cohorts.'),
        key_points=[
            "The shrinking-span claim lacks strong evidence.",
            "Task-switching increased; sustained reading declined.",
            "Students sustain attention when motivated.",
            "Capacity versus habit is the open question.",
        ],
        requirements=[
            "Attention measures by task and motivation.",
            "Developmental tracking studies.",
            "Environment-design experiments.",
        ],
        standards=[
            "Claims checked against the attention literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Mark G. Attention Span. Hanover Square; 2023.",
            "Rosen LD et al. Media-induced task-switching. 2013.",
        ],
        hypotheses=[
            "Allocation-habit change explains the pattern.",
            "Capacity genuinely shrank.",
            "Nothing changed; moral panic.",
            "Technology rebuilt attention differently.",
        ],
        confirm="Attention tracks motivation and environment.",
        refute="Capacity measures declined across cohorts.",
    ),
    dict(
        key="education-22",
        name="The Reading Wars: Settled",
        group="Learning",
        ladder_rank=22,
        ladder_tier="compounded",
        problem=("Are the reading wars actually settled - and if the "
                 "science is clear, why does practice lag?"),
        background=("This entry's companion to education-02 asks the "
                    "meta-question: given the scientific consensus on "
                    "phonics, what explains the persistent gap between "
                    "research and classrooms? Candidate explanations: "
                    "teacher preparation, philosophical resistance, "
                    "commercial curricula, and policy churn."),
        why_it_matters=("The research-practice gap is education's "
                        "systemic disease. Reading is its clearest case."),
        sig_lens=("The Signature lens treats the gap as a pipeline "
                  "ledger: the Signature approach asks where knowledge "
                  "gets lost."),
        sig_body=("The Signature proposal models the gap as a "
                  "multi-stage pipeline failure. Assumptions: (1) "
                  "research exists; (2) teacher prep filters it; (3) "
                  "curricula and policy filter further. Reasoning path: "
                  "the proposal predicts each stage should lose "
                  "fidelity - which implementation studies confirm. "
                  "Closing the gap then needs pipeline engineering "
                  "(prep reform, curriculum standards), not more "
                  "research. Limits: the model needs stage-by-stage "
                  "loss measures; philosophical resistance needs "
                  "separate treatment."),
        pointer=('The Signature system models the research-practice gap as multi-stage pipeline failure needing pipeline engineering. The Signature test: fidelity losses track pipeline stages. It would be refuted if practice follows research where communicated.'),
        key_points=[
            "The science on phonics is unusually clear.",
            "Classroom practice lags substantially.",
            "Teacher prep, curricula, and policy filter research.",
            "Each stage loses fidelity.",
        ],
        requirements=[
            "Stage-by-stage fidelity measures.",
            "Pipeline-reform evaluations.",
            "An account of philosophical resistance.",
        ],
        standards=[
            "Claims checked against the implementation literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Castles A et al. Ending the reading wars. Psychological Science in the Public Interest; 2018.",
            "Seidenberg M. Language at the Speed of Sight. Basic Books; 2017.",
        ],
        hypotheses=[
            "Pipeline failure explains the gap.",
            "The science is less settled than claimed.",
            "Teachers rationally resist oversimplified science.",
            "Commercial interests drive the gap.",
        ],
        confirm="Fidelity losses track pipeline stages.",
        refute="Practice follows research where communicated.",
    ),
    dict(
        key="education-23",
        name="Math Anxiety: Where Does It Come From",
        group="Learning",
        ladder_rank=23,
        ladder_tier="compounded",
        problem=("Where does math anxiety come from - and does it cause "
                 "poor performance or result from it?"),
        background=("Math anxiety correlates with performance and with "
                    "avoidance of math careers; it shows gender patterns. "
                    "The causal direction is debated: anxiety may consume "
                    "working memory (cause), or repeated failure may "
                    "produce anxiety (effect). Teacher anxiety transmits "
                    "to students, especially girls."),
        why_it_matters=("Math anxiety gates STEM careers. Its origins "
                        "determine interventions."),
        sig_lens=("The Signature lens treats math anxiety as a feedback "
                  "ledger: the Signature approach asks where the loop "
                  "starts."),
        sig_body=("The Signature proposal models math anxiety as a "
                  "bidirectional feedback loop. Assumptions: (1) early "
                  "difficulty seeds anxiety; (2) anxiety consumes working "
                  "memory, worsening performance; (3) transmission from "
                  "anxious teachers amplifies it. Reasoning path: the "
                  "proposal predicts interventions should work at "
                  "multiple points - reframing anxiety, building "
                  "foundations, training teachers - which they do. "
                  "Breaking the loop anywhere helps; preventing the "
                  "first turn matters most. Limits: the model needs "
                  "better longitudinal data; the gender patterns need "
                  "fuller explanation."),
        pointer=('The Signature system models math anxiety as a bidirectional feedback loop, breakable at multiple points. The Signature test: interventions work at multiple loop points. It would be refuted if only one causal direction is supported.'),
        key_points=[
            "Math anxiety correlates with performance and avoidance.",
            "Causal direction is debated.",
            "Teacher anxiety transmits to students.",
            "Gender patterns appear consistently.",
        ],
        requirements=[
            "Longitudinal causal analyses.",
            "Transmission studies.",
            "Multi-point intervention trials.",
        ],
        standards=[
            "Claims checked against the math-anxiety literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Ashcraft MH. Math anxiety. Current Directions in Psychological Science; 2002.",
            "Beilock SL et al. Female teachers' math anxiety affects girls' math achievement. PNAS; 2010.",
        ],
        hypotheses=[
            "Bidirectional feedback explains the pattern.",
            "Anxiety primarily causes poor performance.",
            "Poor performance primarily causes anxiety.",
            "Cultural stereotypes are the root.",
        ],
        confirm="Interventions work at multiple loop points.",
        refute="Only one causal direction is supported.",
    ),
    dict(
        key="education-24",
        name="The Flynn Effect in Reverse",
        group="Assessment",
        ladder_rank=24,
        ladder_tier="advanced",
        problem=("Why are IQ scores now declining in some countries - is the "
                 "Flynn effect reversing, and why?"),
        background=("IQ rose for a century (Flynn effect); since the 1990s, "
                    "several Nordic countries show declines. Candidates: "
                    "changes in schooling, media environments, nutrition "
                    "plateaus, immigration composition, or test artifacts. "
                    "Whether the reversal is real and what drives it "
                    "remains open."),
        why_it_matters=("Cognitive capital shapes economies. A genuine "
                        "reversal would be historically momentous."),
        sig_lens=("The Signature lens treats the reversal as an "
                  "environment ledger: the Signature approach asks what "
                  "changed in the cognitive environment."),
        sig_body=("The Signature proposal models the reversal as "
                  "environmental, schooling-mediated. Assumptions: (1) "
                  "the Flynn rise tracked schooling and cognitive "
                  "demand; (2) recent schooling changed (less "
                  "demanding curricula, more media); (3) composition "
                  "effects are smaller than claimed. Reasoning path: "
                  "the proposal predicts declines should track "
                  "schooling-quality measures within countries - which "
                  "early evidence supports. The reversal is then a "
                  "policy signal, not a biological fate. Limits: the "
                  "model needs better schooling measures; the "
                  "composition debate continues."),
        pointer=('The Signature system models the IQ reversal as schooling-mediated and policy-actionable, not biological fate. The Signature test: declines track schooling-quality measures. It would be refuted if declines persist with schooling controlled.'),
        key_points=[
            "IQ rose for a century, now declines in some countries.",
            "Schooling, media, and composition are candidates.",
            "The reversal's reality is debated.",
            "Policy implications are large.",
        ],
        requirements=[
            "Within-country schooling-quality tracking.",
            "Composition-effect decomposition.",
            "Test-artifact analyses.",
        ],
        standards=[
            "Claims checked against the intelligence literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Flynn JR. What Is Intelligence? Cambridge University Press; 2007.",
            "Bratsberg B, Rogeberg O. Flynn effect and its reversal. PNAS; 2018.",
        ],
        hypotheses=[
            "Schooling-mediated environmental change explains it.",
            "Composition effects dominate.",
            "It is a test artifact.",
            "Media environments are the cause.",
        ],
        confirm="Declines track schooling-quality measures.",
        refute="Declines persist with schooling controlled.",
    ),
    dict(
        key="education-25",
        name="Admissions: What Predicts Success",
        group="Assessment",
        ladder_rank=25,
        ladder_tier="advanced",
        problem=("What actually predicts college success - grades, tests, "
                 "essays, or nothing admissions measures?"),
        background=("High-school GPA predicts college GPA best; tests add "
                    "incremental validity but correlate with background. "
                    "Test-optional experiments show mixed results. The "
                    "deeper question: whether admissions predicts "
                    "learning or merely selects the already-advantaged."),
        why_it_matters=("Admissions allocate life chances. Their validity "
                        "determines their justice."),
        sig_lens=("The Signature lens treats admissions as a selection "
                  "ledger: the Signature approach asks what the "
                  "predictors measure."),
        sig_body=("The Signature proposal models admissions validity as "
                  "preparation-proxies. Assumptions: (1) GPA captures "
                  "sustained effort and preparation; (2) tests add "
                  "cognitive signal plus background; (3) essays capture "
                  "resources. Reasoning path: the proposal predicts GPA "
                  "should dominate prediction - which it does - and "
                  "that test-optional shifts weight to background-"
                  "correlated essays. Fairness then needs preparation "
                  "measures, not just achievement. Limits: the model "
                  "needs better long-term outcome data; the "
                  "test-optional experiments need longer follow-up."),
        pointer=('The Signature system models admissions predictors as preparation proxies, with GPA dominant and fairness needing preparation measures. The Signature test: prediction tracks preparation measures. It would be refuted if tests outperform preparation-based models.'),
        key_points=[
            "High-school GPA is the best predictor of college GPA.",
            "Tests add incremental validity.",
            "Test-optional experiments show mixed results.",
            "Whether admissions select or predict is the deeper question.",
        ],
        requirements=[
            "Long-term outcome prediction studies.",
            "Test-optional follow-up analyses.",
            "Preparation-versus-achievement decomposition.",
        ],
        standards=[
            "Claims checked against the admissions literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Sackett PR et al. Does socioeconomic status explain the relationship between admissions tests and post-secondary academic performance? 2009.",
            "Belasco AS et al. Test-optional admissions. 2015.",
        ],
        hypotheses=[
            "Preparation-proxy models explain predictor performance.",
            "Tests are the fairest available measure.",
            "Holistic review improves fairness.",
            "No admissions system is valid.",
        ],
        confirm="Prediction tracks preparation measures.",
        refute="Tests outperform preparation-based models.",
    ),
    dict(
        key="education-26",
        name="The Purpose of University",
        group="Policy",
        ladder_rank=26,
        ladder_tier="advanced",
        problem=("What is university for - job training, research, "
                 "citizenship, or personal transformation - and can one "
                 "institution serve all?"),
        background=("Universities promise everything: careers, knowledge, "
                    "citizenship, growth. Critics argue the missions "
                    "conflict - research versus teaching, access versus "
                    "excellence, vocational versus liberal. Whether the "
                    "multiversity is coherent or a historical accident "
                    "remains debated."),
        why_it_matters=("The purpose determines funding, curriculum, and "
                        "who belongs. The incoherence question shapes "
                        "higher education's future."),
        sig_lens=("The Signature lens treats the university as a mission "
                  "ledger: the Signature approach asks which missions "
                  "conflict and which reinforce."),
        sig_body=("The Signature proposal models the multiversity as "
                  "partially coherent. Assumptions: (1) research and "
                  "teaching can reinforce (inquiry-based learning); (2) "
                  "access and excellence conflict under scarcity; (3) "
                  "vocational and liberal aims need different "
                  "pedagogies. Reasoning path: the proposal predicts "
                  "the deepest conflicts where resources are scarcest "
                  "- which matches the pattern. The answer is then "
                  "differentiation: institutions should specialize "
                  "rather than all promising everything. Limits: the "
                  "model needs better mission-conflict measures; the "
                  "prestige economy resists differentiation."),
        pointer=('The Signature system models the multiversity as partially coherent, with differentiation as the answer. The Signature test: outcomes track mission-clarity measures. It would be refuted if multi-mission institutions outperform specialists.'),
        key_points=[
            "Universities promise multiple conflicting missions.",
            "Research versus teaching is the classic tension.",
            "Access versus excellence conflicts under scarcity.",
            "Whether the multiversity is coherent is debated.",
        ],
        requirements=[
            "Mission-conflict measures by institution.",
            "Differentiation outcome studies.",
            "An account of the prestige economy.",
        ],
        standards=[
            "Claims checked against the higher-education literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Kerr C. The Uses of the University. Harvard University Press; 1963.",
            "Labaree DF. A Perfect Mess. University of Chicago Press; 2017.",
        ],
        hypotheses=[
            "Differentiation resolves the incoherence.",
            "The multiversity is coherent as is.",
            "One mission should dominate.",
            "The conflicts are unresolvable.",
        ],
        confirm="Outcomes track mission-clarity measures.",
        refute="Multi-mission institutions outperform specialists.",
    ),
    dict(
        key="education-27",
        name="Vocational Versus Academic Tracks",
        group="Policy",
        ladder_rank=27,
        ladder_tier="advanced",
        problem=("Should systems track students into vocational versus "
                 "academic paths - and when does tracking help versus "
                 "harm?"),
        background=("Germany's dual system is admired; American tracking "
                    "is condemned for racial and class stratification. "
                    "The evidence: vocational education pays well where "
                    "labor markets value it, but early tracking "
                    "entrenches inequality. The optimal timing and "
                    "permeability remain open."),
        why_it_matters=("Tracking shapes life chances at scale. Its design "
                        "determines whether it builds skills or cements "
                        "class."),
        sig_lens=("The Signature lens treats tracking as a timing ledger: "
                  "the Signature approach asks when sorting helps and "
                  "when it harms."),
        sig_body=("The Signature proposal models tracking effects as "
                  "timing-and-permeability dependent. Assumptions: (1) "
                  "late tracking lets abilities reveal; (2) permeability "
                  "prevents dead ends; (3) labor-market linkages "
                  "determine vocational value. Reasoning path: the "
                  "proposal predicts late, permeable tracking with "
                  "employer linkages should outperform early rigid "
                  "tracking - matching the German versus American "
                  "contrast. Design, not tracking itself, is the "
                  "variable. Limits: the model needs better timing "
                  "comparisons; the stratification mechanisms need "
                  "fuller study."),
        pointer=('The Signature system models tracking as design-dependent: late, permeable, and employer-linked works; early and rigid harms. The Signature test: outcomes track timing-permeability measures. It would be refuted if tracking harms regardless of design.'),
        key_points=[
            "Germany's dual system is admired; US tracking is condemned.",
            "Vocational education pays where labor markets value it.",
            "Early tracking entrenches inequality.",
            "Timing and permeability are the open variables.",
        ],
        requirements=[
            "Timing comparisons across systems.",
            "Permeability measures and outcomes.",
            "Stratification-mechanism studies.",
        ],
        standards=[
            "Claims checked against the tracking literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Shavit Y, Muller W. From School to Work. Oxford University Press; 1998.",
            "Oakes J. Keeping Track. Yale University Press; 1985.",
        ],
        hypotheses=[
            "Timing and permeability determine effects.",
            "Tracking is inherently stratifying.",
            "Vocational education is inherently valuable.",
            "Comprehensive systems are always best.",
        ],
        confirm="Outcomes track timing-permeability measures.",
        refute="Tracking harms regardless of design.",
    ),
    dict(
        key="education-28",
        name="Education and Democracy: The Link",
        group="Theory",
        ladder_rank=28,
        ladder_tier="advanced",
        problem=("Does education cause democracy - or do democracies just "
                 "educate more?"),
        background=("The correlation is strong; the causation is debated. "
                    "Lipset proposed education as democracy's "
                    "prerequisite; Acemoglu and colleagues found the "
                    "causal effect weak once country effects are "
                    "controlled. Whether schooling builds democratic "
                    "citizens or democracies build schools remains open."),
        why_it_matters=("The answer determines whether education aid is "
                        "democracy aid - and what schools should teach."),
        sig_lens=("The Signature lens treats the link as a mechanism "
                  "ledger: the Signature approach asks what schooling "
                  "does to citizens."),
        sig_body=("The Signature proposal models the link as "
                  "content-mediated. Assumptions: (1) years of schooling "
                  "alone do little; (2) civic content and deliberative "
                  "practice matter; (3) authoritarian schooling can "
                  "anti-democratize. Reasoning path: the proposal "
                  "predicts democratic effects should track civic-"
                  "education quality, not attainment - explaining why "
                  "the attainment-democracy correlation dissolves with "
                  "controls. The link is then real but pedagogical, not "
                  "automatic. Limits: the model needs better civic-"
                  "content measures; the causal identification is hard."),
        pointer=('The Signature system models the education-democracy link as content-mediated: civic pedagogy, not attainment, builds citizens. The Signature test: democratic outcomes track civic-content measures. It would be refuted if attainment predicts democracy with content controlled.'),
        key_points=[
            "The education-democracy correlation is strong.",
            "Causal evidence is weak with country controls.",
            "Authoritarian systems also educate extensively.",
            "Civic content may be the real mechanism.",
        ],
        requirements=[
            "Civic-content measures across systems.",
            "Causal identification strategies.",
            "An account of authoritarian schooling.",
        ],
        standards=[
            "Claims checked against the political-economy literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Lipset SM. Some social requisites of democracy. 1959.",
            "Acemoglu D et al. From education to democracy? American Economic Review; 2005.",
        ],
        hypotheses=[
            "Content mediation explains the pattern.",
            "Education causes democracy directly.",
            "Democracy causes education.",
            "The correlation is spurious.",
        ],
        confirm="Democratic outcomes track civic-content measures.",
        refute="Attainment predicts democracy with content controlled.",
    ),
    dict(
        key="education-29",
        name="The Deschooling Debate",
        group="Theory",
        ladder_rank=29,
        ladder_tier="advanced",
        problem=("Would society be better without schools - Illich's "
                 "deschooling provocation, half a century on?"),
        background=("Illich argued schools monopolize learning, create "
                    "dependence, and reproduce inequality; unschooling "
                    "movements test the claim at small scale. The "
                    "evidence: unschooled children learn well with "
                    "resources but the model scales poorly to "
                    "disadvantaged contexts. Whether schooling's harms "
                    "outweigh its goods remains philosophy's question."),
        why_it_matters=("Deschooling is education's radical critique. Its "
                        "force determines reform's limits."),
        sig_lens=("The Signature lens treats deschooling as a resource "
                  "ledger: the Signature approach asks who can learn "
                  "without schools."),
        sig_body=("The Signature proposal models deschooling viability "
                  "as resource-dependent. Assumptions: (1) learning "
                  "needs resources and guidance; (2) advantaged families "
                  "supply them; (3) schools substitute for missing "
                  "family resources. Reasoning path: the proposal "
                  "predicts unschooling should work for the resourced "
                  "and fail for the deprived - which the evidence "
                  "supports. Schools are then imperfect equalizers "
                  "whose abolition would widen inequality. The "
                  "critique's force is reformist, not abolitionist. "
                  "Limits: the model needs better unschooling outcome "
                  "data; the dependence critique needs answering."),
        pointer=('The Signature system models deschooling as resource-dependent: schools are imperfect equalizers whose abolition would widen inequality. The Signature test: outcomes track family-resource measures. It would be refuted if unschooling succeeds for the deprived.'),
        key_points=[
            "Illich argued schools harm more than help.",
            "Unschooling works for resourced families.",
            "Scaling to disadvantaged contexts is unproven.",
            "Whether harms outweigh goods is philosophy's question.",
        ],
        requirements=[
            "Unschooling outcome data by background.",
            "An account of schools' equalizing function.",
            "A reformist reading of the critique.",
        ],
        standards=[
            "Claims checked against the deschooling literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Illich I. Deschooling Society. Harper; 1971.",
            "Gray P. Free to Learn. Basic Books; 2013.",
        ],
        hypotheses=[
            "Resource dependence explains unschooling outcomes.",
            "Deschooling would liberate learning generally.",
            "Schools are necessary equalizers.",
            "Hybrid models capture both insights.",
        ],
        confirm="Outcomes track family-resource measures.",
        refute="Unschooling succeeds for the deprived.",
    ),
    dict(
        key="education-30",
        name="AI Tutors: The Promise and Limits",
        group="Teaching",
        ladder_rank=30,
        ladder_tier="advanced",
        problem=("Can AI tutors deliver Bloom's two sigma at scale - and "
                 "what is lost when the tutor is a machine?"),
        background=("AI tutors promise scaled personalization: infinite "
                    "patience, instant feedback, adaptive pacing. Early "
                    "trials show real gains. But questions persist: the "
                    "relationship component, the risk of dependency, "
                    "equity of access, and whether AI tutoring teaches "
                    "thinking or answer-getting."),
        why_it_matters=("AI tutoring may be the two-sigma solution. Its "
                        "limits determine its role."),
        sig_lens=("The Signature lens treats AI tutors as a component "
                  "ledger: the Signature approach asks which tutoring "
                  "components AI supplies."),
        sig_body=("The Signature proposal models AI tutoring through the "
                  "two-sigma decomposition (see education-08). "
                  "Assumptions: (1) AI supplies feedback and pacing; "
                  "(2) it cannot supply human relationship; (3) "
                  "dependency risks are real. Reasoning path: the "
                  "proposal predicts AI tutors should recover the "
                  "feedback-pacing portion of two sigma - substantial "
                  "but partial - while needing design against "
                  "answer-getting. The role is then powerful "
                  "complement, not replacement. Limits: the model "
                  "needs long-term outcome data; the dependency "
                  "question needs study."),
        pointer=('The Signature system models AI tutors as recovering the feedback-pacing portion of two sigma - a powerful complement, not a replacement. The Signature test: gains match the feedback-pacing prediction. It would be refuted if aI tutors match full human-tutor effects.'),
        key_points=[
            "AI tutors promise scaled personalization.",
            "Early trials show real gains.",
            "The relationship component is missing.",
            "Dependency and equity questions persist.",
        ],
        requirements=[
            "Long-term outcome studies.",
            "Dependency-effect measures.",
            "Design principles against answer-getting.",
        ],
        standards=[
            "Claims checked against the AI-tutoring literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Kulik JA, Fletcher JD. Effectiveness of intelligent tutoring systems. 2016.",
            "Aleven V et al. AI in education. 2024.",
        ],
        hypotheses=[
            "Component decomposition predicts AI tutor effects.",
            "AI will match human tutors fully.",
            "Dependency will undermine the gains.",
            "Equity gaps will widen.",
        ],
        confirm="Gains match the feedback-pacing prediction.",
        refute="AI tutors match full human-tutor effects.",
    ),
    dict(
        key="education-31",
        name="The Attention Economy in Classrooms",
        group="Teaching",
        ladder_rank=31,
        ladder_tier="advanced",
        problem=("How should schools respond to the attention economy - "
                 "compete with it, ban it, or teach through it?"),
        background=("Phones in classrooms, gamified apps, algorithmic "
                    "feeds: students arrive with attention shaped by "
                    "platforms. Responses range from phone bans to "
                    "gamification. Whether schools should adapt to "
                    "platform-shaped attention or defend older norms "
                    "remains contested."),
        why_it_matters=("The attention economy shapes every student. "
                        "Schools' response determines their relevance."),
        sig_lens=("The Signature lens treats the response as a norm "
                  "ledger: the Signature approach asks which attentional "
                  "norms schools should defend."),
        sig_body=("The Signature proposal models the choice as "
                  "norm-selection. Assumptions: (1) deep learning needs "
                  "sustained attention; (2) platforms train switching; "
                  "(3) schools can train counter-habits. Reasoning path: "
                  "the proposal predicts ban-plus-training should "
                  "outperform both pure bans and gamified surrender - "
                  "because norms need both protection and rebuilding. "
                  "Schools are then attention gyms, not attention "
                  "markets. Limits: the model needs comparative trials; "
                  "the enforcement costs are real."),
        pointer=('The Signature system models schools as attention gyms: ban plus counter-habit training outperforms bans alone or gamified surrender. The Signature test: combined strategies outperform single ones. It would be refuted if bans alone achieve the full effect.'),
        key_points=[
            "Students arrive with platform-shaped attention.",
            "Responses range from bans to gamification.",
            "Deep learning needs sustained attention.",
            "Whether to adapt or defend norms is contested.",
        ],
        requirements=[
            "Comparative trials of response strategies.",
            "Counter-habit training evaluations.",
            "Enforcement-cost analyses.",
        ],
        standards=[
            "Claims checked against the attention-and-learning literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Mark G. Attention Span. Hanover Square; 2023.",
            "Haidt J. The Anxious Generation. Penguin; 2024.",
        ],
        hypotheses=[
            "Ban-plus-training is optimal.",
            "Pure bans suffice.",
            "Gamification harnesses platform attention.",
            "Schools cannot compete; adapt instead.",
        ],
        confirm="Combined strategies outperform single ones.",
        refute="Bans alone achieve the full effect.",
    ),
    dict(
        key="education-32",
        name="Credential Inflation in Education",
        group="Policy",
        ladder_rank=32,
        ladder_tier="advanced",
        problem=("Why do jobs need ever-more credentials - and is "
                 "credential inflation efficient or wasteful?"),
        background=("Jobs once done by high-school graduates now require "
                    "degrees. Signaling theory says credentials screen; "
                    "human-capital theory says they build skills. The "
                    "inflation - degrees for jobs that did not need them "
                    "- suggests screening arms races. Whether the "
                    "expansion is wasteful remains debated."),
        why_it_matters=("Credential inflation taxes workers and students. "
                        "Its efficiency determines education policy."),
        sig_lens=("The Signature lens treats credentials as a signal "
                  "ledger: the Signature approach asks what the degree "
                  "signals versus builds."),
        sig_body=("The Signature proposal models inflation as a "
                  "signaling arms race. Assumptions: (1) employers use "
                  "degrees to screen; (2) more graduates force higher "
                  "screens; (3) the skills for many jobs did not "
                  "change. Reasoning path: the proposal predicts "
                  "inflation where screening dominates skill-building - "
                  "explaining degree requirements for unchanged jobs. "
                  "The waste is then real but individually rational: "
                  "coordination, not ignorance, sustains it. Limits: "
                  "the model needs skill-change measures by "
                  "occupation; the signaling-skill mix varies."),
        pointer=('The Signature system models credential inflation as a signaling arms race - individually rational, collectively wasteful. The Signature test: requirements rise without skill changes. It would be refuted if requirements track measured skill demands.'),
        key_points=[
            "Degree requirements rose for unchanged jobs.",
            "Signaling versus human-capital theories compete.",
            "The expansion suggests screening arms races.",
            "Whether it is wasteful remains debated.",
        ],
        requirements=[
            "Skill-change measures by occupation.",
            "Signaling-skill decomposition.",
            "Coordination solutions (skills-based hiring).",
        ],
        standards=[
            "Claims checked against the labor-economics literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Spence M. Job market signaling. 1973.",
            "Caplan B. The Case Against Education. Princeton University Press; 2018.",
        ],
        hypotheses=[
            "Signaling arms races explain inflation.",
            "Degrees build needed skills.",
            "Skills-based hiring will deflate credentials.",
            "The expansion is efficient.",
        ],
        confirm="Requirements rise without skill changes.",
        refute="Requirements track measured skill demands.",
    ),
    dict(
        key="education-33",
        name="Lifelong Learning: Can Systems Adapt",
        group="Policy",
        ladder_rank=33,
        ladder_tier="advanced",
        problem=("Can education systems built for the young adapt to "
                 "lifelong learning - and what would that take?"),
        background=("Careers now span multiple skill regimes; the "
                    "front-loaded model (learn young, work old) is "
                    "obsolete. But adult retraining shows weak results, "
                    "institutions are youth-designed, and financing "
                    "models assume the front-load. Whether systems can "
                    "adapt remains the open institutional question."),
        why_it_matters=("Economic change demands reskilling at scale. The "
                        "adaptation determines who survives it."),
        sig_lens=("The Signature lens treats lifelong learning as a "
                  "design ledger: the Signature approach asks what "
                  "youth-designed institutions cannot do."),
        sig_body=("The Signature proposal models the adaptation as "
                  "institutional redesign. Assumptions: (1) adult "
                  "learners need modular, work-integrated formats; (2) "
                  "current institutions supply semester-based youth "
                  "formats; (3) financing follows the old model. "
                  "Reasoning path: the proposal predicts retraining "
                  "should fail where formats mismatch adult needs - "
                  "which the weak results confirm - and that "
                  "employer-integrated modular systems should work. "
                  "The answer is then new institutions, not reformed "
                  "old ones. Limits: the model needs better "
                  "modular-system evaluations; the financing redesign "
                  "is unsolved."),
        pointer=('The Signature system models lifelong learning as needing new institutions: modular, work-integrated, and differently financed. The Signature test: modular work-integrated systems outperform. It would be refuted if reformed traditional programs succeed equally.'),
        key_points=[
            "The front-loaded model is obsolete.",
            "Adult retraining shows weak results.",
            "Institutions are youth-designed.",
            "Financing assumes the old model.",
        ],
        requirements=[
            "Modular-system evaluations.",
            "Adult-learner format research.",
            "Financing-model innovations.",
        ],
        standards=[
            "Claims checked against the adult-education literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "OECD. Skills Outlook. 2019.",
            "McKinsey Global Institute. The future of work. 2017.",
        ],
        hypotheses=[
            "New institutions are needed, not reformed old ones.",
            "Existing institutions can adapt.",
            "Employers will lead the adaptation.",
            "Lifelong learning is overstated as a need.",
        ],
        confirm="Modular work-integrated systems outperform.",
        refute="Reformed traditional programs succeed equally.",
    ),
    dict(
        key="education-34",
        name="A Unified Theory of Learning",
        group="Theory",
        ladder_rank=34,
        ladder_tier="advanced",
        problem=("Can the sciences of learning unify - behaviorist, "
                 "cognitivist, constructivist, and sociocultural - into "
                 "one account?"),
        background=("Each tradition captures something: behaviorism the "
                    "contingencies, cognitivism the mental processes, "
                    "constructivism the active building, sociocultural "
                    "theory the social embedding. Unification attempts "
                    "remain programmatic. Whether learning's nature "
                    "permits one theory is the field's capstone "
                    "question."),
        why_it_matters=("This is learning science's capstone: the answer "
                        "determines what learning is."),
        sig_lens=("The Signature lens treats the traditions as a level "
                  "ledger: the Signature approach asks what level each "
                  "tradition owns."),
        sig_body=("The Signature proposal models unification as "
                  "level-integration. Assumptions: (1) learning spans "
                  "neural, cognitive, individual, and social levels; "
                  "(2) each tradition owns a level; (3) levels "
                  "interact. Reasoning path: the proposal assigns "
                  "behaviorism to contingencies, cognitivism to "
                  "processes, constructivism to agency, sociocultural "
                  "theory to context - with the learner's activity as "
                  "the integrator. Unity comes from the levels' "
                  "interaction, not one tradition's victory. Limits: "
                  "the integration is sketched; partisans may reject "
                  "the settlement."),
        pointer=("The Signature system assigns each tradition its level of learning, with the learner's activity as the integrator. The Signature test: integrated models predict across levels. It would be refuted if levels prove irreducible to common theory."),
        key_points=[
            "Four traditions offer incompatible images of learning.",
            "Each captures what the others miss.",
            "Unification attempts remain programmatic.",
            "Whether one theory is possible is foundational.",
        ],
        requirements=[
            "A level architecture for the traditions.",
            "An account of level interaction.",
            "Testable implications of the integration.",
        ],
        standards=[
            "Claims checked against the learning-theory literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Bruner JS. Toward a Theory of Instruction. Harvard University Press; 1966.",
            "Vygotsky LS. Mind in Society. Harvard University Press; 1978.",
        ],
        hypotheses=[
            "Level-integration unifies learning science.",
            "The traditions are incommensurable.",
            "One tradition will absorb the rest.",
            "Pluralism is permanent.",
        ],
        confirm="Integrated models predict across levels.",
        refute="Levels prove irreducible to common theory.",
    ),
]
