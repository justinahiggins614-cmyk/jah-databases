#!/usr/bin/env python3
"""Entries for The Scientific Method Basics Database (fundamentals order #9).

Verified 2026-10-17: RAW SWEEP over the full manifest (2,410 databases) PLUS
every shard index title in jah-databases-data-1 (zgrep across all
data/*/index.jsonl.gz) PLUS the main-repo data dir: zero
'scientific-method*' slugs/names; zero title collisions for any of the 68
titles (34 public + 34 ' (Signature Edition)' variants). Near-hits examined
by name/purpose/record schema/capabilities: 'components' (JAH-CPT, parts
encyclopedia), 'everything-entity' (general entity archive), 'audit-slice'
(audit tooling) - none is a first-principles teaching ladder of the
scientific method itself. Verdict: BUILD NEW.

So this build creates two NEW databases, 34 ladder-ordered records each:

  scientific-method            - The Scientific Method Basics Database
                                 (public-harvest: real, fact-checked
                                 foundational science - observation, asking
                                 testable questions, hypothesis, fair
                                 experiments, variables, collecting data,
                                 drawing conclusions, and the full ladder to
                                 peer review, case studies, and everyday
                                 application; standard references Bacon
                                 Novum Organum 1620; Newton Principia 1687;
                                 Galileo Two New Sciences 1638; Mill A System
                                 of Logic 1843; Bernard Experimental
                                 Medicine 1865; Pearson Grammar of Science
                                 1892; Fisher Design of Experiments 1935;
                                 Popper Logic of Scientific Discovery 1934;
                                 Kuhn Structure of Scientific Revolutions
                                 1962; Hill causation criteria 1965;
                                 Merton norms 1942; Belmont Report 1979;
                                 ISO 5725 accuracy/precision; and the case
                                 studies Fleming 1929, Semmelweis 1861,
                                 Michelson-Morley 1887)
  scientific-method-signature  - The Scientific Method Basics Signature
                                 Database
                                 (his original Signature Method of Inquiry:
                                 observation the covenant of attention, the
                                 question the oath of curiosity, the
                                 hypothesis the sworn prediction, the fair
                                 experiment the trial of the oath, data the
                                 testimony, and the conclusion the verdict;
                                 src signature, titles suffixed
                                 " (Signature Edition)", clearly labeled
                                 Signature-made, never presented as
                                 authentic public record)

34 records each, ordered by the teaching ladder (ladder_rank 1-10,
ladder_tier foundations/compounded/advanced); the shard index is written in
ladder order so pages present simple -> compounded -> complex.

ID prefixes: JAH-SCIM- (public) and JAH-SCIMS- (signature), verified free
in the manifest id_prefix values and in every shard index file (zero hits).

Numerical cores: all hand-computed 2026-10-17, machine-verified by the
demos (see demos_scientific_method.py). Every demo prints its real
computed values, asserts tight bounds (never float exact-equality), and
ends with the OK marker; the build machine-executes all 68 demos before
hand-off.

Screening: no hate-adjacent, profane, or inappropriate content; no
religious talk; nothing on neutralizing or defeating military or
defense-grade systems. Never the words "bat belt" anywhere. No website
references. No Facebook.
"""

SIG_TAIL = ("Signature original - his original Signature Method of Inquiry: "
            "observation the covenant of attention, the question the oath of "
            "curiosity, the hypothesis the sworn prediction, the fair "
            "experiment the trial of the oath, data the testimony, and the "
            "conclusion the verdict. Clearly labeled Signature-made, never "
            "presented as authentic public record.")

CIT_BACON = ("Bacon F. Novum Organum. London; 1620 - the inductive method: "
             "systematic observation and controlled experiment as the engine "
             "of knowledge.")
CIT_NEWTON = ("Newton I. Philosophiae Naturalis Principia Mathematica. "
              "London; 1687 - the Rules of Reasoning: nature does the same "
              "things by the same causes, and hypotheses are framed from "
              "phenomena.")
CIT_GALILEO = ("Galileo G. Discorsi e Dimostrazioni Matematiche Intorno a "
               "Due Nuove Scienze. Leiden; 1638 - measurement and experiment "
               "against received authority.")
CIT_MILL = ("Mill JS. A System of Logic, Ratiocinative and Inductive. "
            "London; 1843 - the methods of agreement, difference, residues, "
            "and concomitant variations for finding causes.")
CIT_BERNARD = ("Bernard C. An Introduction to the Study of Experimental "
               "Medicine. Paris; 1865 - the controlled experiment as the "
               "foundation of experimental science.")
CIT_PEARSON = ("Pearson K. The Grammar of Science. London; 1892 - science "
               "as the description and correlation of experience.")
CIT_FISHER = ("Fisher RA. The Design of Experiments. Edinburgh; 1935 - "
              "randomization, replication, and the null hypothesis as "
              "experimental design.")
CIT_POPPER = ("Popper K. The Logic of Scientific Discovery. Vienna; 1934 - "
              "falsifiability as the line between science and non-science.")
CIT_KUHN = ("Kuhn TS. The Structure of Scientific Revolutions. University "
            "of Chicago Press; 1962 - normal science, anomaly, and paradigm "
            "shift.")
CIT_HILL = ("Hill AB. The environment and disease: association or "
            "causation? Proceedings of the Royal Society of Medicine. "
            "1965;58(5):295-300 - the nine viewpoints for judging causation.")
CIT_MERTON = ("Merton RK. The normative structure of science. 1942 - "
              "communalism, universalism, disinterestedness, organized "
              "skepticism.")
CIT_BELMONT = ("National Commission for the Protection of Human Subjects of "
               "Biomedical and Behavioral Research. The Belmont Report. "
               "Washington; 1979 - respect for persons, beneficence, "
               "justice.")
CIT_ISO5725 = ("ISO 5725-1:2023. Accuracy (trueness and precision) of "
               "measurement methods and results - Part 1: General principles "
               "and definitions.")
CIT_FLEMING = ("Fleming A. On the antibacterial action of cultures of a "
               "penicillium. British Journal of Experimental Pathology. "
               "1929;10(3):226-236.")
CIT_SEMMELWEIS = ("Semmelweis IF. Die Aetiologie, der Begriff und die "
                  "Prophylaxis des Kindbettfiebers. Pest; 1861 - chlorine "
                  "handwashing cut Vienna maternity mortality from 18.27% "
                  "to 1.27%.")
CIT_MICHELSON = ("Michelson AA, Morley EW. On the relative motion of the "
                 "Earth and the luminiferous ether. American Journal of "
                 "Science. 1887;34(203):333-345 - expected fringe shift "
                 "about 0.4, observed below 0.01.")

ENTRIES = [
    {
        "key": "what_is",
        "name": "What Is Science",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "Science is organized curiosity: a way of learning about the "
            "world that anyone can check. Instead of deciding what is true "
            "by authority, tradition, or feeling, science tests ideas "
            "against evidence that can be observed and measured. A claim "
            "becomes scientific when there is a possible observation that "
            "could show it wrong, and when the evidence is gathered in a "
            "way others can repeat. The word covers three great territories. "
            "The natural sciences study the physical world: physics, "
            "chemistry, biology, earth science, astronomy. The formal "
            "sciences study systems of reasoning: mathematics, logic, "
            "statistics, computer science. The social sciences study people "
            "and societies: psychology, sociology, economics, "
            "anthropology. Applied science turns all of this into medicine, "
            "engineering, and technology. What unites every territory is "
            "the method: observe, question, predict, test, and revise. "
            "This record opens the whole database, because everything after "
            "it is one shelf of that method."
        ),
        "how_it_works": (
            "Science works by making thinking checkable. A person notices "
            "something, states what they expect to happen, and sets up a "
            "test where nature gets the final vote. If the test agrees "
            "with the expectation, the idea survives for now; if the test "
            "disagrees, the idea must change, no matter who proposed it. "
            "Other scientists then repeat the test independently, and only "
            "ideas that survive repeated testing become trusted. Results "
            "are published with enough detail that strangers can redo the "
            "work, which is how mistakes get caught. Over time, surviving "
            "ideas connect into theories that explain many facts at once "
            "and predict new ones. The whole machine runs on one fuel: "
            "honest reporting of what the test actually showed, including "
            "the results that did not cooperate."
        ),
        "key_points": [
            "Science is organized curiosity: ideas are tested against evidence that anyone can observe, measure, and repeat.",
            "The three territories are natural sciences, formal sciences, and social sciences, with applied science turning knowledge into medicine, engineering, and technology.",
            "A claim is scientific when a possible observation could show it wrong - testability is the entry ticket.",
            "Independent repetition is the error filter: one lab can be mistaken, but a result that every lab gets is trusted.",
            "Honest reporting of all results, including the ones that did not cooperate, is what keeps the whole system working.",
        ],
        "requirements": [
            "A phenomenon that can be observed or measured in the world, not only felt or asserted.",
            "An idea stated clearly enough that a test could confirm it or show it wrong.",
            "Evidence gathered in a documented way that others can repeat independently.",
            "Results reported fully, including failures and surprises, not only the successes.",
            "Willingness to change the idea when the evidence goes against it.",
        ],
        "standards": [
            "Claims are framed so they can be tested against observation; authority and tradition are not accepted as evidence.",
            "Measurements are reported with their methods and limits, so others can judge and repeat the work.",
            "Conclusions follow the evidence; when data and idea conflict, the idea yields.",
        ],
        "citations": [CIT_BACON, CIT_GALILEO, CIT_MERTON],
        "sig_lens": (
            "The Signature read: science is the covenant of attention - a "
            "sworn promise between the observer and the world that what is "
            "reported is what was actually seen. Where public science says "
            "testability, the Signature Method of Inquiry says the oath: "
            "no claim stands that cannot be witnessed, and no witness is "
            "trusted who reports only the flattering half of the evidence."
        ),
    },
    {
        "key": "curiosity",
        "name": "The Role of Curiosity in Discovery",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "Every scientific journey starts before any equipment is "
            "touched: with noticing something odd and refusing to let it "
            "go. Curiosity is the engine of the scientific method - the "
            "restlessness that turns a passing observation into a "
            "question, a question into a test, and a test into knowledge. "
            "Many of the great discoveries began as accidents that only "
            "mattered because a curious mind was watching. Fleming noticed "
            "mold killing bacteria on a discarded plate and investigated "
            "instead of throwing it away. Roentgen noticed a glowing "
            "screen across the room and chased the cause instead of "
            "ignoring it. The funnel of curiosity runs wide to narrow: "
            "hundreds of observations become dozens of questions, which "
            "become a handful of testable hypotheses, which become, rarely, "
            "a theory. Nothing in the funnel works without the first step, "
            "and the first step is simply paying attention on purpose. "
            "Curiosity can be trained like a muscle: the habit of asking "
            "'why is that' and 'what would happen if' about ordinary "
            "things is the daily practice of a scientist."
        ),
        "how_it_works": (
            "Curiosity works by turning surprise into a search plan. "
            "First, sustained attention catches the anomaly - the result "
            "that does not fit, the pattern that repeats, the thing that "
            "should not be there. Next, the curious mind forms questions "
            "in layers: what happened, then why did it happen, then what "
            "would happen if the conditions changed. The questions are "
            "then sorted: the ones that can be tested with available "
            "tools move forward, the rest are shelved for later. Each "
            "surviving question is sharpened until it names something "
            "measurable, and from there it enters the hypothesis stage. "
            "The discipline of curiosity is to chase the anomaly without "
            "chasing every distraction - to let the strange result set "
            "the agenda while keeping a log of what was tried. In the "
            "end, curiosity is not randomness; it is attention with a "
            "notebook."
        ),
        "key_points": [
            "Curiosity is the engine of the method: no test begins until someone notices something worth testing.",
            "Great discoveries often start as accidents that mattered only because a curious mind was paying attention.",
            "The funnel runs wide to narrow: many observations, fewer questions, a handful of hypotheses, rarely a theory.",
            "Curiosity asks in layers - what happened, why it happened, what would happen if conditions changed.",
            "Curiosity is trainable: the daily habit of asking why and what-if about ordinary things is scientific practice.",
        ],
        "requirements": [
            "Sustained, deliberate attention to the world rather than passive looking.",
            "A notebook habit: observations written down before memory reshapes them.",
            "Questions sorted into the testable-now and the shelved-for-later.",
            "Sharpening each surviving question until it names something measurable.",
            "Discipline to chase the anomaly while logging every attempt.",
        ],
        "standards": [
            "Observations are recorded as seen, before interpretation is allowed to edit them.",
            "Questions are refined until they point at measurable quantities.",
            "The search plan distinguishes the anomaly being chased from background distractions.",
        ],
        "citations": [CIT_BACON, CIT_PEARSON, CIT_FLEMING],
        "sig_lens": (
            "The Signature read: curiosity is the oath of the observer - "
            "the sworn refusal to walk past the strange thing. Public "
            "science calls it the research question; the Signature Method "
            "of Inquiry calls it the covenant of attention, and it holds "
            "that a discovery is simply an accident that met a prepared "
            "witness who wrote it down."
        ),
    },
    {
        "key": "observation",
        "name": "Observation: The Starting Point of Inquiry",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "Observation is step one of the scientific method: gathering "
            "information about the world with the senses, often extended "
            "by instruments. Good observations come in two kinds. "
            "Qualitative observations describe qualities: the leaf is "
            "green, the solution turned blue, the animal fled quickly. "
            "Quantitative observations give numbers: the leaf is 12 "
            "centimeters long, the solution reached 40 degrees, the animal "
            "ran for 9 seconds. Both kinds matter, but numbers travel "
            "better - they can be compared, graphed, and tested by "
            "others. The great rule of observation is to record what is "
            "actually there, not what you expect to see. Expectation is a "
            "filter, and filters hide surprises. That is why observers "
            "write things down immediately, measure twice, and note the "
            "conditions: the time, the place, the temperature, who was "
            "present. An observation log is the raw material of science, "
            "and every later step - questions, hypotheses, experiments - "
            "is built on its honesty."
        ),
        "how_it_works": (
            "Observation works by separating seeing from judging. The "
            "observer first decides what to watch and for how long, then "
            "records in the moment rather than from memory, because "
            "memory edits. Each entry gets the essentials: what was "
            "seen, how much, under what conditions, with what tool. "
            "Quantitative observations use instruments - rulers, scales, "
            "thermometers, timers - and the instrument reading is written "
            "exactly as shown, including the unit. When an observation "
            "repeats, the observer checks for consistency: do five "
            "readings cluster together, or do they wander? A tight cluster "
            "suggests a steady phenomenon; a wandering set suggests "
            "either a changing phenomenon or a shaky method. Patterns "
            "across many observations become the raw questions of the "
            "next step. The observer never discards the odd reading "
            "quietly - the outlier may be the discovery."
        ),
        "key_points": [
            "Observation is step one: information gathered with the senses, extended by instruments.",
            "Qualitative observations describe qualities; quantitative observations give numbers that can be compared and tested.",
            "Record what is actually there, not what you expect - expectation is a filter that hides surprises.",
            "Write it down immediately with conditions attached: time, place, tool, and circumstances.",
            "Never discard the odd reading quietly - the outlier may be the discovery.",
        ],
        "requirements": [
            "A defined target of observation: what is being watched and for how long.",
            "Recording in the moment, not reconstructed later from memory.",
            "Instruments read exactly as shown, with units written every time.",
            "Conditions logged alongside every observation: time, place, tool, circumstances.",
            "Outliers kept and flagged, never silently deleted.",
        ],
        "standards": [
            "Observations distinguish description from interpretation; the log records what happened, not what it means.",
            "Quantitative readings include units and the instrument used.",
            "Repeated observations are checked for consistency before patterns are claimed.",
        ],
        "citations": [CIT_GALILEO, CIT_BERNARD, CIT_PEARSON],
        "sig_lens": (
            "The Signature read: observation is the covenant of attention "
            "made concrete - the sworn act of witnessing without editing. "
            "Where public science logs data, the Signature Method of "
            "Inquiry keeps testimony: every entry a witnessed statement, "
            "every outlier a witness who must be heard, because the oath "
            "forbids the convenient deletion."
        ),
    },
    {
        "key": "questions",
        "name": "Asking Testable Questions",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "A scientific question is a curiosity that has been sharpened "
            "until a test can answer it. Not every question qualifies. "
            "'Why is the sky beautiful' invites poetry but no measurement; "
            "'does cloud cover change afternoon temperature' can be tested "
            "with a thermometer and a notebook. The difference is "
            "testability: a scientific question names things that can be "
            "observed or measured, and it implies a comparison. The best "
            "questions are specific - they name the who, the what, and "
            "the how-much. 'Do plants grow better with fertilizer' is a "
            "start; 'does 5 grams of nitrogen fertilizer per week increase "
            "bean stem height over 30 days' is a question an experiment "
            "can answer. Questions also need to be answerable with "
            "available tools: a question about atoms that requires a "
            "particle accelerator must wait its turn. Shaping a raw "
            "wonder into a testable question is the most creative step "
            "in the whole method, because the question decides what the "
            "experiment is allowed to discover."
        ),
        "how_it_works": (
            "Question-shaping works by running raw curiosity through a "
            "filter. First, the wonder is written down in plain words: "
            "what exactly seemed strange or interesting. Then the vague "
            "parts are replaced with measurable things: 'better' becomes "
            "'taller in centimeters', 'faster' becomes 'seconds to finish'. "
            "Next, the question is checked against three gates. The "
            "measurability gate: can the key things be observed or "
            "measured with available tools? The comparison gate: does the "
            "question compare at least two conditions, so there is "
            "something to learn? The falsifiability gate: is there a "
            "possible answer that would prove the guess wrong? Questions "
            "that pass all three move on to become hypotheses. Questions "
            "that fail a gate are not abandoned - they are rewritten. "
            "'Do fish sleep' becomes 'do goldfish show reduced movement "
            "and response during dark hours', and suddenly the test "
            "designs itself."
        ),
        "key_points": [
            "A scientific question is a curiosity sharpened until a test can answer it.",
            "Testability is the filter: the question must name things that can be observed or measured.",
            "Specific questions name the who, the what, and the how-much - vagueness kills experiments.",
            "Every good question implies a comparison between at least two conditions.",
            "Failed questions are rewritten, not abandoned - sharpening is the creative heart of the method.",
        ],
        "requirements": [
            "A plain-words statement of what seemed strange or interesting.",
            "Vague terms replaced with measurable quantities and units.",
            "A comparison built in: at least two conditions to set against each other.",
            "A possible answer that would prove the guess wrong - the falsifiability gate.",
            "Tools available to actually run the test the question implies.",
        ],
        "standards": [
            "Questions are judged by testability: measurable, comparable, falsifiable.",
            "Each question names its variables in operational terms before any experiment is designed.",
            "Questions that fail a gate are rewritten and re-gated, not quietly dropped.",
        ],
        "citations": [CIT_BACON, CIT_MILL, CIT_POPPER],
        "sig_lens": (
            "The Signature read: the question is the oath of curiosity "
            "spoken aloud - a sworn promise to pursue one specific wonder "
            "to an answer. Public science calls it the research question; "
            "the Signature Method of Inquiry calls it the naming, because "
            "a wonder given a measurable name can be hunted, and an "
            "unnamed wonder only haunts."
        ),
    },
    {
        "key": "hypothesis",
        "name": "The Hypothesis: An Educated Prediction",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "A hypothesis is an educated prediction: a clear, testable "
            "statement about what will happen under specific conditions. "
            "It is not a guess - a guess has no reason behind it, while a "
            "hypothesis is built from observations, background knowledge, "
            "and the question being asked. The classic form is the "
            "if-then statement: if bean plants get 5 grams of nitrogen "
            "fertilizer per week, then they will grow taller than plants "
            "with no fertilizer over 30 days. The if names the change "
            "being tested; the then names the expected result in "
            "measurable terms. A good hypothesis also names its "
            "conditions: the same light, the same water, the same soil, "
            "so the test is fair. And it stays falsifiable - there must "
            "be a possible result that would prove it wrong, such as the "
            "fertilized plants growing no taller at all. When the test "
            "agrees, the hypothesis survives and earns trust; when the "
            "test disagrees, the hypothesis is revised or replaced. Either "
            "outcome is progress."
        ),
        "how_it_works": (
            "A hypothesis works by putting the idea at risk. The "
            "investigator first gathers background: what is already known "
            "about this phenomenon, and what do the observations suggest. "
            "Then the prediction is written as a single clear sentence in "
            "if-then form, with the measured outcome named precisely. The "
            "test is designed so that nature can answer yes or no - "
            "ideally with numbers. When results come in, they are "
            "compared against the prediction with a pre-decided rule for "
            "what counts as support: for example, the fertilized group "
            "must average at least 2 centimeters taller. If the rule is "
            "met, the hypothesis stands - stronger, but never proven "
            "beyond all future testing. If the rule is not met, the "
            "hypothesis is modified or discarded, and the new version "
            "must explain both the old successes and the new failure. "
            "This is the mechanism by which knowledge sharpens itself: "
            "every hypothesis is a bet, and the method collects on the "
            "bets honestly."
        ),
        "key_points": [
            "A hypothesis is an educated prediction built from observation and background knowledge, not a blind guess.",
            "The if-then form names the change being tested and the expected result in measurable terms.",
            "Falsifiability is required: a possible result must exist that would prove the hypothesis wrong.",
            "A supported hypothesis survives stronger but is never proven beyond all future testing.",
            "A refuted hypothesis is revised or replaced - either outcome is progress.",
        ],
        "requirements": [
            "Background research: what is already known about the phenomenon.",
            "A single clear if-then prediction sentence naming the measured outcome.",
            "Named conditions under which the prediction should hold.",
            "A pre-decided rule for what counts as support before data is collected.",
            "A plan for what the next version of the idea must explain if this one fails.",
        ],
        "standards": [
            "Hypotheses are stated before the test is run, never invented after seeing the data.",
            "Predictions name quantities, units, and the comparison that decides support.",
            "Revised hypotheses must account for both prior successes and the new failure.",
        ],
        "citations": [CIT_BERNARD, CIT_POPPER, CIT_MILL],
        "sig_lens": (
            "The Signature read: the hypothesis is the sworn prediction - "
            "the oath staked on a named outcome. Where public science "
            "says educated guess, the Signature Method of Inquiry says "
            "covenant of the test: the investigator swears what will "
            "happen, nature swears nothing, and the verdict belongs to "
            "the numbers alone."
        ),
    },
    {
        "key": "fair_experiments",
        "name": "Fair Experiments and Controls",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "A fair experiment changes one thing at a time and keeps "
            "everything else the same, so that any difference in the "
            "result can only be blamed on the change. The group that gets "
            "the change is the experimental group; the group that does "
            "not is the control group, the baseline for comparison. "
            "Testing fertilizer on bean plants means two sets of plants: "
            "one gets fertilizer, one does not, and both get the same "
            "light, water, soil, and pot size. If the fertilized plants "
            "grow taller, the fertilizer is the reason - nothing else "
            "differs. Without a control, a taller plant proves nothing: "
            "maybe the weather changed, maybe the soil was richer. "
            "Controls come in flavors: a no-treatment control, a "
            "standard-treatment control for comparison against the usual "
            "method, and sometimes a placebo control where the subject "
            "cannot tell which group they are in. The control is the "
            "silent partner of every honest experiment, and the single "
            "biggest difference between a test and a mere demonstration."
        ),
        "how_it_works": (
            "A fair experiment works by isolation. The investigator lists "
            "every factor that could affect the outcome - light, water, "
            "temperature, soil, seed batch, pot size - and fixes all of "
            "them except the one under test. Subjects are assigned to "
            "the experimental and control groups by chance "
            "(randomization), so no hidden bias puts the strong plants "
            "in one group. Both groups are treated identically in every "
            "other respect, and measured with the same instruments by the "
            "same procedure. The result is a clean comparison: the only "
            "systematic difference between the groups is the change being "
            "tested, so any consistent difference in outcome traces back "
            "to it. If both groups change together, something else is at "
            "work - perhaps the season - and the experiment has caught a "
            "confounding factor instead of being fooled by it. Fairness "
            "is not kindness to the plants; it is ruthlessness toward "
            "alternative explanations."
        ),
        "key_points": [
            "A fair experiment changes one thing and holds everything else constant.",
            "The control group is the baseline: without it, a difference proves nothing.",
            "Random assignment keeps hidden bias from loading one group with an advantage.",
            "Both groups get identical treatment and measurement in every respect except the tested change.",
            "If both groups shift together, a confounding factor is at work - and the design has caught it.",
        ],
        "requirements": [
            "An experimental group receiving the change and a control group that does not.",
            "All other factors held constant across groups: materials, environment, procedure.",
            "Random assignment of subjects to groups.",
            "Identical measurement instruments and procedures for every group.",
            "A control type chosen for the question: no-treatment, standard-treatment, or placebo.",
        ],
        "standards": [
            "Only the tested factor differs systematically between groups.",
            "Randomization is used for group assignment, not convenience or judgment.",
            "Confounding factors are listed in advance and controlled or measured.",
        ],
        "citations": [CIT_BERNARD, CIT_FISHER, CIT_MILL],
        "sig_lens": (
            "The Signature read: the fair experiment is the trial of the "
            "oath - the sworn prediction placed in the arena with every "
            "excuse stripped away. The control is the honest witness who "
            "changes nothing, so that when the experimental group "
            "changes, the change testifies against every alternative "
            "explanation."
        ),
    },
    {
        "key": "variables",
        "name": "Independent and Dependent Variables",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "Variables are the things that can change in an experiment, "
            "and the two stars of the show are the independent and "
            "dependent variables. The independent variable is what the "
            "investigator deliberately changes - the cause being tested, "
            "such as the amount of fertilizer. The dependent variable is "
            "what is measured to see the effect - the outcome, such as "
            "plant height in centimeters. A handy memory trick: the "
            "independent variable stands alone (I change it), and the "
            "dependent variable depends on it. In the if-then "
            "hypothesis, the if holds the independent variable and the "
            "then holds the dependent one. Every experiment has exactly "
            "one independent variable if it is to stay fair; the "
            "dependent variable is measured the same way for every "
            "subject, with the same instrument, at the same times. "
            "Getting these two straight is what turns a vague activity "
            "into a real test: change this, measure that, compare."
        ),
        "how_it_works": (
            "Variables work by creating a cause-and-effect pipeline the "
            "data can travel. The investigator sets the independent "
            "variable to chosen levels - for example, 0, 2, 4, 6, and 8 "
            "grams of fertilizer - spread across the groups. The "
            "dependent variable is then measured with a fixed procedure: "
            "stem height from soil line to tip, in centimeters, on day "
            "30, with the same ruler. Plotting the dependent variable "
            "against the independent variable shows the relationship at "
            "a glance: points rising left to right suggest more fertilizer "
            "means more growth. A correlation number can summarize the "
            "strength of that trend. Because the independent variable was "
            "set by the investigator and everything else was held "
            "constant, a strong trend points at causation, not just "
            "coincidence. If the dependent variable is measured "
            "sloppily - different rulers, different days - the pipeline "
            "leaks, and no conclusion can be trusted."
        ),
        "key_points": [
            "The independent variable is what the investigator changes; the dependent variable is what gets measured.",
            "Memory trick: independent stands alone, dependent depends on it.",
            "In the if-then hypothesis, the if names the independent variable and the then names the dependent one.",
            "One experiment, one independent variable - more than one breaks fairness.",
            "The dependent variable is measured identically for every subject, every time.",
        ],
        "requirements": [
            "A named independent variable with the levels it will take.",
            "A named dependent variable with its unit and measurement procedure.",
            "The independent variable set by the investigator, not merely observed.",
            "Identical measurement of the dependent variable across all subjects and times.",
            "A plan for displaying the relationship: plot of dependent against independent.",
        ],
        "standards": [
            "Variables are defined in operational terms with units before data collection.",
            "Exactly one independent variable per fair experiment.",
            "Measurement procedures are fixed and identical for all observations.",
        ],
        "citations": [CIT_BERNARD, CIT_MILL, CIT_FISHER],
        "sig_lens": (
            "The Signature read: the independent variable is the hand "
            "that moves, the dependent variable the witness that "
            "answers. The Signature Method of Inquiry frames the pair as "
            "the oath and the testimony: the investigator swears the "
            "change, the world swears the result, and the plot is the "
            "record of both keeping their word."
        ),
    },
    {
        "key": "controlled_vars",
        "name": "Controlled Variables",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "Controlled variables are everything the investigator holds "
            "constant so the test stays fair: the light, the water, the "
            "soil, the temperature, the seed batch, the pot size. They "
            "are the silent majority of an experiment - often a dozen or "
            "more factors, each fixed at one value for every subject. "
            "The reason is simple: if the fertilized plants also got "
            "more sun, nobody can tell whether the fertilizer or the "
            "sunlight caused the extra growth. An uncontrolled factor "
            "that affects the outcome is called a confounding variable, "
            "and confounders are the number-one killer of conclusions. "
            "The discipline is to list every factor that could matter "
            "before the experiment starts, decide how each will be held "
            "steady, and write down the actual values used. Factors that "
            "cannot be held constant - like outdoor weather - are "
            "measured and reported instead, so their influence can be "
            "judged. A clean experiment is not one with no confounders; "
            "it is one where every confounder was either chained down "
            "or accounted for."
        ),
        "how_it_works": (
            "Controlled variables work by removing alternative suspects. "
            "Before the experiment, the investigator brainstorms every "
            "factor that could move the dependent variable: environment, "
            "materials, timing, handling. Each factor gets a control "
            "strategy: hold it constant (same water volume daily), "
            "standardize it (all seeds from one packet), randomize its "
            "leftovers (pots shuffled on the bench), or measure it as a "
            "backup (record daily temperature). During the run, the "
            "controls are checked - a quick daily glance confirms the "
            "lamps are all on and the watering is even. Afterward, the "
            "results are examined for confound footprints: if the "
            "control group also grew unusually fast on warm days, "
            "temperature leaked into the result and must be reported. "
            "The test of good control is the negative: when the "
            "independent variable does not change, the outcome should "
            "not change either. Holding the line on controls is "
            "unglamorous work, and it is exactly what makes the "
            "conclusion trustworthy."
        ),
        "key_points": [
            "Controlled variables are every factor held constant so the test stays fair.",
            "An uncontrolled factor that affects the outcome is a confounding variable - the top killer of conclusions.",
            "List every possible factor before starting, and give each a control strategy.",
            "Factors that cannot be controlled are measured and reported so their influence can be judged.",
            "The test of good control: when the tested change is absent, the outcome should not shift.",
        ],
        "requirements": [
            "A pre-experiment list of every factor that could affect the dependent variable.",
            "A control strategy for each factor: constant, standardized, randomized, or measured.",
            "Recorded values of the controlled conditions during the run.",
            "Checks during the experiment that controls are actually holding.",
            "A post-run review for confound footprints, reported honestly.",
        ],
        "standards": [
            "Confounding factors are identified in the design phase, not discovered in the discussion.",
            "Control conditions are documented with actual values, not assumed.",
            "Uncontrolled influences are disclosed with their measured data.",
        ],
        "citations": [CIT_BERNARD, CIT_FISHER, CIT_MILL],
        "sig_lens": (
            "The Signature read: controlled variables are the chained "
            "witnesses - every alternative explanation bound and held "
            "still while the sworn change is tested. The Signature Method "
            "of Inquiry calls an uncontrolled factor a loose suspect, "
            "and a loose suspect can overturn any verdict."
        ),
    },
]
ENTRIES.extend([
    {
        "key": "operational_defs",
        "name": "Operational Definitions",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "An operational definition turns a vague idea into a "
            "measurement recipe: it says exactly what will be observed "
            "and how. 'Plant growth' is a foggy notion; 'the change in "
            "stem height in centimeters, measured from the soil line to "
            "the tip with a ruler on day 0 and day 30' is an operational "
            "definition. Without one, two investigators can study the "
            "same thing and produce incomparable results - one measures "
            "height, the other counts leaves, and their numbers cannot "
            "meet. Operational definitions also expose hidden "
            "assumptions: defining 'learning' as 'score improvement on "
            "the same 20-question test' forces you to admit that only "
            "test learning is being measured. The recipe must be "
            "complete enough that a stranger could repeat the "
            "measurement and get the same kind of number: the "
            "instrument, the unit, the timing, the procedure. Good "
            "definitions are also honest about their limits - 'reaction "
            "time as measured by this app' is not the same as 'reaction "
            "time' in general, and saying so is a strength, not a "
            "weakness."
        ),
        "how_it_works": (
            "Operational definitions work by removing wiggle room before "
            "data collection starts. The investigator takes each key "
            "term in the hypothesis and writes the measurement recipe: "
            "what instrument, what unit, measured when, measured how, "
            "recorded where. The recipe is then trial-run on a few "
            "subjects to catch ambiguity - if two people following the "
            "recipe get different numbers, the recipe needs rewriting. "
            "Once locked, the recipe is frozen for the whole experiment: "
            "changing the definition mid-study is like moving the "
            "finish line during a race. When results are published, the "
            "operational definitions travel with them, so readers know "
            "precisely what the numbers mean and other labs can repeat "
            "the measurements exactly. This is also what makes "
            "comparisons across studies possible: when two teams define "
            "'improved' the same way, their results can be combined; "
            "when they do not, combining them is meaningless. The "
            "definition is the contract between the idea and the data."
        ),
        "key_points": [
            "An operational definition is a measurement recipe: exactly what will be observed and how.",
            "Vague terms produce incomparable results; operational terms produce repeatable ones.",
            "The recipe names the instrument, the unit, the timing, and the procedure.",
            "Trial-run the recipe first: if two people get different numbers, rewrite it.",
            "Definitions are frozen during the study and published with the results.",
        ],
        "requirements": [
            "Every key term in the hypothesis translated into an observable, measurable procedure.",
            "The instrument, unit, timing, and step-by-step procedure specified.",
            "A trial run confirming that different measurers following the recipe agree.",
            "The definition frozen before data collection begins and kept through the study.",
            "Published definitions alongside results so others can repeat the measurement.",
        ],
        "standards": [
            "Definitions are operational before any data is collected, never invented to fit results.",
            "Measurement recipes are complete enough for a stranger to reproduce the numbers.",
            "Limits of the definition are stated plainly alongside the results.",
        ],
        "citations": [CIT_BERNARD, CIT_PEARSON, CIT_FISHER],
        "sig_lens": (
            "The Signature read: the operational definition is the "
            "witness oath in written form - the sworn statement of "
            "exactly what was measured and how. The Signature Method of "
            "Inquiry holds that an idea without a measurement recipe is "
            "a rumor, and only the recipe turns the rumor into "
            "testimony."
        ),
    },
    {
        "key": "data_collection",
        "name": "Collecting and Recording Data",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "Data is the testimony of the experiment: the numbers and "
            "observations the test produces, recorded faithfully and "
            "completely. Collecting data well is mostly a matter of "
            "discipline. Decide before starting what will be recorded, "
            "how often, and in what form - a table with labeled columns "
            "beats a pile of sticky notes every time. Record in the "
            "moment: memory smooths edges and invents details, so the "
            "reading goes into the log the second it is taken. Include "
            "the units on every entry and the conditions alongside: the "
            "date, the time, the temperature, anything unusual. Collect "
            "enough data to see a pattern but not so much that quality "
            "collapses - ten careful measurements beat a hundred rushed "
            "ones. And collect it the same way every time: the same "
            "instrument, the same procedure, the same timing. "
            "Systematic collection - measuring every subject on the "
            "same schedule - prevents the quiet bias of measuring the "
            "interesting cases more often. The data table is the "
            "experiment's permanent record; everything claimed later "
            "must be traceable back to it."
        ),
        "how_it_works": (
            "Data collection works through a pre-built recording system. "
            "The investigator designs the data table first: one row per "
            "subject or observation, one column per variable, with units "
            "in the headers. A sampling plan decides which subjects get "
            "measured - for example, every 10th item off a production "
            "line, or all plants in randomly chosen pots - so the sample "
            "represents the whole fairly. During the run, readings are "
            "entered immediately, in ink or in a locked digital form, "
            "with nothing erased: corrections are made as new entries "
            "with a note, never by overwriting. Each session ends with "
            "a quick integrity check - are all rows filled, are the "
            "units consistent, do the numbers look sane. Backups are "
            "made before any analysis begins, because the raw data is "
            "irreplaceable. Only when the table is complete and checked "
            "does analysis start. This chain - plan, record, check, "
            "back up, then analyze - is what separates evidence from "
            "anecdote."
        ),
        "key_points": [
            "Data is the testimony of the experiment: recorded faithfully, completely, and in the moment.",
            "Design the data table before collecting: rows for subjects, columns for variables, units in headers.",
            "A sampling plan makes the sample represent the whole fairly instead of cherry-picking.",
            "Corrections are new entries with notes, never overwrites - the raw record is sacred.",
            "Back up the raw data before any analysis; analysis never touches the original table.",
        ],
        "requirements": [
            "A pre-designed data table with labeled columns and units.",
            "A sampling plan describing how subjects were chosen.",
            "Recording in the moment with conditions logged alongside readings.",
            "An integrity check at the end of each session: completeness, units, sanity.",
            "A backed-up, unaltered raw dataset preserved before analysis begins.",
        ],
        "standards": [
            "Raw data is recorded contemporaneously and never altered retroactively.",
            "Sampling methods are documented so representativeness can be judged.",
            "Every claimed result traces back to entries in the raw data table.",
        ],
        "citations": [CIT_BERNARD, CIT_FISHER, CIT_ISO5725],
        "sig_lens": (
            "The Signature read: data collection is the taking of "
            "testimony - each reading a sworn statement entered the "
            "moment it is spoken. The Signature Method of Inquiry "
            "forbids the altered record: a correction is new testimony, "
            "never a rewritten past, because the verdict must rest on "
            "what was actually witnessed."
        ),
    },
    {
        "key": "tables_charts",
        "name": "Tables Charts and Graphs",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "Tables, charts, and graphs are the lenses that make data "
            "visible to human eyes: a table organizes numbers so they "
            "can be found, a chart summarizes them so they can be "
            "compared, and a graph reveals patterns so they can be "
            "understood. A data table lists every observation in rows "
            "and columns with clear headers and units - the permanent "
            "record. A bar chart compares amounts across categories: "
            "the heights of the control and fertilized plant groups side "
            "by side. A line graph shows change over time: plant height "
            "climbing day by day. A scatter plot shows the relationship "
            "between two variables: fertilizer amount against final "
            "height, with each dot one plant. Choosing the right visual "
            "is a thinking skill: categories get bars, time gets lines, "
            "relationships get scatter plots, parts of a whole get pie "
            "charts. Every honest visual follows the same rules - "
            "labeled axes with units, a truthful scale, and a title "
            "that says what is shown. A graph that misleads, through a "
            "truncated axis or a cherry-picked range, is not a lens but "
            "a disguise."
        ),
        "how_it_works": (
            "Data visuals work by mapping numbers to space so patterns "
            "pop out. The investigator first picks the question the "
            "visual must answer: comparison, change over time, or "
            "relationship. Then the data is organized: raw readings go "
            "in the table, and the chart is built from checked numbers. "
            "Axes are labeled with the variable and its unit, and the "
            "scale is chosen to show the data honestly - bar charts "
            "start at zero so heights mean amounts, and line graphs "
            "show the full relevant range. The visual is then read like "
            "a witness: do the bars differ clearly, does the line trend "
            "up, do the dots form a cloud or a line. A frequency table "
            "can first compress many readings into bins - for example, "
            "how many plants fell into each 2-centimeter height range - "
            "which shows the shape of the data at a glance. The "
            "investigator checks the visual against the table to make "
            "sure nothing was distorted in translation. A good graph "
            "lets a stranger see the result in seconds; a bad one hides "
            "it on purpose or by accident."
        ),
        "key_points": [
            "Tables organize numbers so they can be found; charts compare them; graphs reveal patterns.",
            "Categories get bar charts, time gets line graphs, relationships get scatter plots.",
            "Every honest visual has labeled axes with units, a truthful scale, and a clear title.",
            "Bar charts start at zero so heights honestly represent amounts.",
            "Frequency tables compress many readings into bins, showing the shape of the data at a glance.",
        ],
        "requirements": [
            "A complete data table with headers and units as the source of every visual.",
            "The visual type matched to the question: comparison, time trend, or relationship.",
            "Axes labeled with variable names and units on every chart and graph.",
            "Truthful scales: zero-based bars, full relevant ranges, no cherry-picked windows.",
            "A cross-check that the visual faithfully represents the underlying table.",
        ],
        "standards": [
            "Visuals are built from checked data, never sketched from impressions.",
            "Scales and ranges are chosen to inform, not to exaggerate or hide.",
            "Titles state what is shown; captions state what was measured and how.",
        ],
        "citations": [CIT_PEARSON, CIT_FISHER, CIT_MILL],
        "sig_lens": (
            "The Signature read: the graph is the testimony made "
            "visible - the sworn numbers drawn so any eye can judge "
            "them. The Signature Method of Inquiry holds the "
            "dishonest scale as perjury: a truncated axis is a "
            "witness coached to lie, and the oath demands the full "
            "range be shown."
        ),
    },
    {
        "key": "conclusions",
        "name": "Drawing Conclusions",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "Drawing a conclusion is answering the original question "
            "with the evidence in hand - no more, no less. The "
            "investigator returns to the hypothesis and asks the blunt "
            "question: did the data support it, refute it, or come out "
            "unclear. Support means the results matched the prediction "
            "by the pre-decided rule; refutation means they did not; "
            "inconclusive means the test was too weak or too messy to "
            "decide. A good conclusion states the answer, cites the "
            "numbers that earned it, and admits the limits: the "
            "conditions tested, the sample size, the possible "
            "confounders. It never claims more than the data allows - "
            "'fertilizer increased bean height in this greenhouse trial' "
            "is honest; 'fertilizer makes all plants grow' is not. The "
            "conclusion also reports the surprises, because an "
            "unexpected result is often the seed of the next question. "
            "Finally, it points forward: what should be tested next, "
            "and what would strengthen or challenge this finding. A "
            "conclusion is not a victory speech; it is the verdict the "
            "evidence earned."
        ),
        "how_it_works": (
            "Conclusions work by a disciplined comparison. First, the "
            "results are summarized: the key numbers for each group, "
            "the differences, the trends - with the pre-decided support "
            "rule applied mechanically. Then the hypothesis gets its "
            "grade: supported, refuted, or inconclusive, based on that "
            "rule and nothing else. Next comes the scope check: the "
            "conclusion is fenced to what was actually tested - the "
            "subjects, the conditions, the time span. The investigator "
            "then hunts for alternative explanations: could a confounder, "
            "a measurement slip, or plain chance explain the pattern. "
            "Only explanations that survive this hunt make it into the "
            "write-up; the rest are reported as limitations. Surprises "
            "are logged as new questions rather than buried. The final "
            "statement is written in plain words a non-expert can "
            "follow, with the numbers attached as evidence. The method "
            "ends where it began - with a question - because every "
            "verdict suggests the next trial."
        ),
        "key_points": [
            "A conclusion answers the original question with the evidence in hand - no more, no less.",
            "The three verdicts are supported, refuted, or inconclusive, decided by the pre-set rule.",
            "Conclusions are fenced to what was actually tested: the subjects, conditions, and time span.",
            "Alternative explanations are hunted down; survivors are reported, the rest become limitations.",
            "Surprises are logged as new questions, and every verdict suggests the next trial.",
        ],
        "requirements": [
            "A summary of results with the key numbers for each group or condition.",
            "The pre-decided support rule applied to grade the hypothesis.",
            "A scope statement fencing the conclusion to the tested conditions.",
            "An honest hunt for alternative explanations, reported as limitations.",
            "A forward pointer: what to test next to strengthen or challenge the finding.",
        ],
        "standards": [
            "Conclusions follow the evidence; claims never exceed what the data supports.",
            "The verdict is based on the pre-registered rule, not post-hoc storytelling.",
            "Limitations and surprises are reported, not hidden.",
        ],
        "citations": [CIT_BERNARD, CIT_POPPER, CIT_MILL],
        "sig_lens": (
            "The Signature read: the conclusion is the verdict - the "
            "sworn answer the testimony earned, fenced to exactly what "
            "was witnessed. The Signature Method of Inquiry forbids the "
            "victory speech: the verdict may be supported, refuted, or "
            "unclear, and each is honorable, because the oath was to "
            "the evidence, not to the hoped-for answer."
        ),
    },
])
ENTRIES.extend([
    {
        "key": "accuracy_precision",
        "name": "Measurement Accuracy and Precision",
        "group": "Compounded",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description": (
            "Accuracy and precision are the two different ways a "
            "measurement can be right - and confusing them is one of "
            "the most common errors in science. Accuracy is closeness "
            "to the true value: an accurate scale reads 100 grams for "
            "a true 100-gram weight. Precision is consistency: a "
            "precise scale gives nearly the same reading every time, "
            "even if that reading is wrong. Picture arrows at a "
            "target: accurate and precise arrows cluster in the "
            "bullseye; precise but inaccurate arrows cluster tightly "
            "off-center; accurate but imprecise arrows scatter around "
            "the bullseye without clustering; neither accurate nor "
            "precise arrows scatter everywhere. The dangerous case is "
            "high precision with low accuracy: the tight cluster "
            "looks trustworthy while being systematically wrong - "
            "usually because the instrument needs calibration. "
            "Precision is measured by spread, such as the standard "
            "deviation of repeated readings; accuracy is measured by "
            "bias, the average distance from the true value. Good "
            "science needs both: precision you can improve by "
            "averaging, but accuracy you can only fix by finding the "
            "source of the bias."
        ),
        "how_it_works": (
            "Accuracy and precision work as a two-axis diagnosis. The "
            "investigator takes repeated measurements of a known "
            "reference - a certified weight, a standard solution, a "
            "calibrated length - and computes two numbers. The bias "
            "is the mean of the readings minus the true value: a "
            "large bias means poor accuracy, and the fix is "
            "calibration or a corrected procedure. The spread is the "
            "standard deviation of the readings: a large spread means "
            "poor precision, and the fix is steadier technique, "
            "better instruments, or more repetitions averaged "
            "together. The four outcomes each prescribe an action: "
            "accurate and precise means proceed; precise but biased "
            "means calibrate; unbiased but scattered means stabilize "
            "and repeat; both bad means fix the method before "
            "collecting real data. This check runs before the "
            "experiment, not after, because no amount of analysis "
            "can rescue measurements whose quality was never "
            "established. The standard ISO 5725 gives these ideas "
            "their formal names: trueness for the bias side, "
            "precision for the spread side, accuracy for the "
            "combination."
        ),
        "key_points": [
            "Accuracy is closeness to the true value; precision is consistency of repeated readings.",
            "High precision with low accuracy is the dangerous case: a tight cluster that is systematically wrong.",
            "Bias is measured against a known reference; spread is measured across repeats.",
            "Precision improves with averaging; accuracy improves only by finding and fixing the bias.",
            "ISO 5725 formalizes the split: trueness plus precision equals accuracy.",
        ],
        "requirements": [
            "A known reference value to test the instrument against before the experiment.",
            "Repeated readings of the reference to measure both bias and spread.",
            "A calibration step when bias is found, not a hope that it will average out.",
            "A precision target: the spread must be small enough for the question being asked.",
            "Documentation of the measurement quality check alongside the results.",
        ],
        "standards": [
            "Measurement quality is established before data collection, not inferred afterward.",
            "Bias is reported against traceable references with stated uncertainties.",
            "Precision is quantified as spread, not claimed from a single reading.",
        ],
        "citations": [CIT_ISO5725, CIT_GALILEO, CIT_BERNARD],
        "sig_lens": (
            "The Signature read: accuracy is the witness telling the "
            "truth, precision the witness telling it steadily. The "
            "Signature Method of Inquiry warns that the steady liar "
            "is the most dangerous witness of all - the tight cluster "
            "off the mark - and commands calibration as the oath of "
            "the instrument before any testimony is taken."
        ),
    },
    {
        "key": "error",
        "name": "Experimental Error",
        "group": "Compounded",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description": (
            "Experimental error is the unavoidable gap between a "
            "measurement and the true value - not a mistake, but a "
            "fact of measuring. Every instrument has limits: a ruler "
            "marked in millimeters cannot honestly report tenths of "
            "a millimeter, and every reading carries a little "
            "wobble. Errors come in two families. Systematic error "
            "pushes every reading the same direction - a scale that "
            "reads 2 grams heavy, a timer started late - and it "
            "corrupts accuracy. Random error scatters readings around "
            "the true value - hand tremor, air currents, electrical "
            "noise - and it corrupts precision. Honest science does "
            "not pretend error away; it measures it and carries it "
            "through the calculation. If length is 10.0 plus or minus "
            "0.1 centimeters and width is 5.0 plus or minus 0.1, the "
            "area is not exactly 50.0 - it is 50.0 plus or minus "
            "about 1.1, because uncertainties combine. Reporting a "
            "result without its uncertainty is like giving directions "
            "without distances: technically an answer, practically "
            "useless. The goal is never zero error - it is known "
            "error, small enough for the question at hand."
        ),
        "how_it_works": (
            "Error analysis works by tracking uncertainty from "
            "instrument to conclusion. First, each instrument's "
            "uncertainty is established: the smallest division, the "
            "calibration certificate, or the spread of repeats. "
            "Systematic errors are hunted by measuring known "
            "references - any consistent offset is corrected or at "
            "least reported. Random error is shrunk by repetition: "
            "averaging n readings cuts the random wobble by roughly "
            "the square root of n. When quantities combine in a "
            "calculation, their uncertainties combine too: for "
            "multiplication, the relative uncertainties add in "
            "quadrature - the square root of the sum of squares. The "
            "final result is reported as value plus-or-minus "
            "uncertainty, with the uncertainty rounded to one or two "
            "meaningful digits and the value rounded to match. "
            "Significant figures are the shorthand of this honesty: "
            "a calculator's ten digits are trimmed to the digits the "
            "measurement actually earned. An experiment whose "
            "uncertainty swamps its effect has not failed - it has "
            "reported that a sharper test is needed."
        ),
        "key_points": [
            "Error is the unavoidable gap between measurement and truth - not a mistake, but a fact to be measured.",
            "Systematic error biases every reading one way and corrupts accuracy; random error scatters readings and corrupts precision.",
            "Uncertainties combine through calculations: for products, relative uncertainties add in quadrature.",
            "Averaging repeated readings shrinks random error by roughly the square root of the count.",
            "Results are reported as value plus-or-minus uncertainty, with digits trimmed to what was earned.",
        ],
        "requirements": [
            "The uncertainty of every instrument established before use.",
            "Known references measured to hunt down systematic offsets.",
            "Repetition planned so random error shrinks to fit the question.",
            "Uncertainty propagated through every calculation to the final result.",
            "Final values reported with honest significant figures and stated uncertainties.",
        ],
        "standards": [
            "No result is reported without its uncertainty.",
            "Systematic errors are corrected or disclosed, never averaged away silently.",
            "Uncertainty propagation follows the standard combination rules for the operations used.",
        ],
        "citations": [CIT_ISO5725, CIT_GALILEO, CIT_PEARSON],
        "sig_lens": (
            "The Signature read: error is the honest shadow of every "
            "measurement - the sworn admission that no witness sees "
            "perfectly. The Signature Method of Inquiry counts the "
            "unstated uncertainty as a broken oath: the testimony "
            "must carry its own doubt, stated plainly, so the verdict "
            "knows exactly how much weight the evidence can bear."
        ),
    },
    {
        "key": "design",
        "name": "Forming an Experimental Design",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "Experimental design is the battle plan of the test: who "
            "gets what treatment, how many subjects, in what order, "
            "measured when. A good design is written before the first "
            "measurement, because decisions made after seeing data "
            "are corrupted by it. The core choices are the treatments "
            "(the levels of the independent variable), the control, "
            "the sample size, the assignment method, and the "
            "measurement schedule. Randomization assigns subjects to "
            "groups by chance, spreading unknown confounders evenly "
            "instead of letting them pile up in one group. "
            "Replication repeats each treatment on multiple subjects, "
            "so random wobble can be averaged out and real "
            "differences stand out. When two factors are tested at "
            "once - say fertilizer amount and watering frequency - a "
            "factorial design tries every combination, which also "
            "reveals whether the factors interact. Blocking groups "
            "subjects by a known source of variation first - such as "
            "testing each fertilizer in both sunny and shady beds - "
            "so that variation stops masquerading as treatment "
            "effect. The design is the experiment's skeleton; the "
            "data is only as strong as the bones."
        ),
        "how_it_works": (
            "Design works by deciding everything checkable in advance. "
            "The investigator writes the protocol: the treatments and "
            "their levels, the control condition, the number of "
            "subjects per group, how subjects are assigned, what is "
            "measured, when, and with what instrument. Randomization "
            "is built in - coin flips, random number tables, or "
            "shuffled assignments - so group differences start at "
            "zero. The sample size is chosen to fit the question: "
            "enough subjects that a meaningful effect would show "
            "through the noise, not so many that the study wastes "
            "resources. For multi-factor questions, the factorial "
            "layout crosses every level of each factor with every "
            "level of the others, and the run order is randomized to "
            "spread time-based drift evenly. The whole plan is "
            "reviewed for confounders one more time, then frozen: "
            "from the first measurement on, the plan is followed "
            "exactly, and any deviation is logged as a deviation. "
            "Fisher's great insight was that the design, not the "
            "data analysis, is where experiments are won or lost."
        ),
        "key_points": [
            "The design is written before the first measurement; decisions made after seeing data are corrupted by it.",
            "Randomization spreads unknown confounders evenly across groups instead of letting them pile up.",
            "Replication averages out random wobble so real differences can stand out.",
            "Factorial designs test every combination of factors and reveal interactions between them.",
            "Blocking groups subjects by known variation first, so it stops masquerading as treatment effect.",
        ],
        "requirements": [
            "A written protocol: treatments, control, sample sizes, assignment, measurements, schedule.",
            "Random assignment of subjects to treatments, documented and reproducible.",
            "Replication: multiple subjects per treatment, never a sample of one.",
            "A sample size chosen to detect a meaningful effect through the expected noise.",
            "A frozen plan: deviations during the run are logged, not hidden.",
        ],
        "standards": [
            "Designs are finalized before data collection begins.",
            "Randomization and replication are present in every comparative experiment.",
            "Multi-factor studies use factorial or blocked layouts, not one-factor-at-a-time guessing.",
        ],
        "citations": [CIT_FISHER, CIT_BERNARD, CIT_MILL],
        "sig_lens": (
            "The Signature read: the design is the sworn battle plan - "
            "the oath of the trial written before the first witness "
            "speaks. The Signature Method of Inquiry holds that a "
            "plan changed after seeing the data is a rigged trial, "
            "and commands the frozen protocol: what was sworn before "
            "the test is what the test must follow."
        ),
    },
    {
        "key": "sample_size",
        "name": "Sample Size and Statistics",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "Sample size is how many subjects get measured, and it "
            "decides whether the experiment can hear the signal "
            "through the noise. Too few subjects and a real effect "
            "drowns in random variation - the study was doomed "
            "before it began. Too many and resources are wasted "
            "chasing precision nobody needs. The mathematics is "
            "friendly: the uncertainty of an average shrinks with "
            "the square root of the sample size, so quadrupling the "
            "subjects halves the wobble. A sample must also be "
            "representative: measuring only the tallest plants tells "
            "you about tall plants, not about plants. Random "
            "sampling - every member of the population with an equal "
            "chance of being picked - is the gold standard for "
            "fairness. Statistics is the toolkit that turns samples "
            "into conclusions: means and medians summarize the "
            "center, standard deviation measures the spread, and "
            "tests like the t-test ask whether a difference between "
            "groups is bigger than chance would produce. The "
            "p-value is the most quoted and most abused member of "
            "the toolkit: it is the probability of seeing data this "
            "extreme if nothing were really happening - not the "
            "probability that the hypothesis is true."
        ),
        "how_it_works": (
            "Sample-size thinking works backward from the question. "
            "The investigator first names the smallest effect worth "
            "detecting - say, a 2-centimeter height difference - and "
            "estimates the natural variation from pilot data. The "
            "standard error of the mean, the standard deviation "
            "divided by the square root of n, predicts how tightly "
            "the average will be known: with a standard deviation of "
            "12 and 25 subjects the error is 2.4, and with 100 "
            "subjects it halves to 1.2. Subjects are then drawn by a "
            "random procedure from the full population of interest, "
            "and the plan guards against dropout and missing data. "
            "After the run, statistics summarize: the mean and "
            "spread of each group, the difference between groups, "
            "and a test of whether that difference exceeds what "
            "chance alone would produce. Confidence intervals are "
            "reported alongside p-values, because an interval says "
            "how big the effect might be, while a p-value only says "
            "whether chance is an unlikely explanation. The whole "
            "machinery serves one master: conclusions that would "
            "hold up in a bigger sample too."
        ),
        "key_points": [
            "Sample size decides whether the signal can be heard through the noise.",
            "The uncertainty of an average shrinks with the square root of n: quadruple subjects, halve the wobble.",
            "Samples must be representative; random sampling gives every member a fair chance.",
            "The p-value is the probability of such extreme data if nothing were happening - not the probability the hypothesis is true.",
            "Confidence intervals say how big an effect might be; p-values only rule chance in or out.",
        ],
        "requirements": [
            "The smallest meaningful effect named before subjects are recruited.",
            "An estimate of natural variation from pilot data or prior studies.",
            "A sample size chosen so the standard error fits the question being asked.",
            "Random sampling from the population the conclusion will speak about.",
            "Results reported with confidence intervals, not p-values alone.",
        ],
        "standards": [
            "Sample sizes are justified by the effect size and variation, not by convenience.",
            "Sampling procedures are random and documented.",
            "Statistical claims include the interval of plausible values, not just significance.",
        ],
        "citations": [CIT_FISHER, CIT_PEARSON, CIT_MILL],
        "sig_lens": (
            "The Signature read: the sample is the jury - and a jury "
            "of three cannot speak for a city. The Signature Method "
            "of Inquiry demands the jury be both large enough to be "
            "heard through the noise and fairly chosen enough to "
            "speak for all, for a verdict from a stacked jury is no "
            "verdict at all."
        ),
    },
    {
        "key": "averages_trends",
        "name": "Analyzing Data with Averages and Trends",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "Analysis turns a table of numbers into an answer, and it "
            "starts with the center and the shape. The mean - the sum "
            "divided by the count - is the workhorse average, but it "
            "is dragged around by outliers; the median, the middle "
            "value when data is ordered, resists them. The mode, the "
            "most common value, matters for categories. Spread is "
            "just as important as center: the range, the standard "
            "deviation, and the picture of the distribution tell "
            "whether the average represents the data or hides its "
            "split personality. When data arrives over time, the "
            "trend is the story: plotting day against temperature "
            "and fitting a line reveals the rate of change - the "
            "slope - such as 0.6 degrees per day of warming. A trend "
            "line is a model, and like all models it must be checked: "
            "do the points hug the line, or do they curve away at the "
            "ends. Comparing groups means comparing their centers "
            "against their spreads: a 3-centimeter difference means "
            "little if each group sprawls over 10 centimeters, and a "
            "lot if each group is tight within 1. Analysis is honest "
            "bookkeeping: describe the center, describe the spread, "
            "show the shape, then - and only then - claim the pattern."
        ),
        "how_it_works": (
            "Analysis works in layers from description to comparison. "
            "First the data is cleaned: impossible values are "
            "investigated, missing entries are counted, and nothing "
            "is silently deleted. Then the center and spread of each "
            "group are computed - mean, median, standard deviation - "
            "and the distribution is viewed, because two groups can "
            "share a mean while differing completely in shape. For "
            "time data, a line is fitted by least squares: the slope "
            "that minimizes the squared distances from the points, "
            "giving the rate of change per unit time. Group "
            "comparisons set the difference of means against the "
            "combined spread: a difference many times the standard "
            "error is a signal, a difference near it is noise. Every "
            "computed number is sanity-checked against the raw table "
            "and the graphs - if the analysis says what the eyes "
            "cannot see in the plot, something is off. The final "
            "report shows the descriptive numbers first and the "
            "inferential claims second, so readers can judge the "
            "foundation before the conclusion."
        ),
        "key_points": [
            "Describe center and spread before claiming any pattern: mean, median, mode, range, standard deviation.",
            "The mean is dragged by outliers; the median resists them - report both when they disagree.",
            "A trend line fitted by least squares gives the rate of change, but must be checked against the points.",
            "Group differences are judged against spread: a difference near the standard error is noise.",
            "Sanity-check every computed number against the raw table and the graphs.",
        ],
        "requirements": [
            "Cleaned data with impossible values investigated and missing entries counted.",
            "Center and spread computed for every group: mean, median, standard deviation.",
            "Distributions viewed, not just summarized, before conclusions are drawn.",
            "Trend fits checked against the plotted points for curvature and outliers.",
            "Descriptive numbers reported before and beneath every inferential claim.",
        ],
        "standards": [
            "Analysis never silently deletes data; exclusions are documented with reasons.",
            "Both center and spread are reported for every summarized group.",
            "Models are validated against the data they claim to describe.",
        ],
        "citations": [CIT_PEARSON, CIT_FISHER, CIT_GALILEO],
        "sig_lens": (
            "The Signature read: analysis is the weighing of "
            "testimony - the center the voice of the crowd, the "
            "spread the measure of its disagreement. The Signature "
            "Method of Inquiry forbids the lonely average: no center "
            "may testify without its spread beside it, for an average "
            "without its disagreement is a witness without "
            "cross-examination."
        ),
    },
    {
        "key": "correlation_causation",
        "name": "Correlation and Causation",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Correlation is when two things change together; causation "
            "is when one makes the other change - and the first does "
            "not prove the second. Ice cream sales and drowning "
            "deaths rise together every summer with a near-perfect "
            "correlation, yet banning ice cream would save no "
            "swimmers: the hidden third variable is hot weather, "
            "which drives both. This is the most expensive confusion "
            "in all of science, because correlated pairs are "
            "everywhere and true causes are rare. Correlation can be "
            "measured - the correlation coefficient runs from -1 to "
            "+1, with 0 meaning no linear relationship - but no "
            "number, however close to 1, can by itself prove cause. "
            "Causation needs more: the cause must come before the "
            "effect, the relationship must survive when other "
            "factors are held constant, and ideally an experiment "
            "that changes the cause changes the effect. Hill's "
            "viewpoints - strength, consistency, specificity, "
            "temporality, dose-response, plausibility, coherence, "
            "experiment, and analogy - are the classic checklist for "
            "judging when an association deserves to be called a "
            "cause. The rule to carve in memory: correlation suggests "
            "where to look; only controlled testing decides what "
            "is real."
        ),
        "how_it_works": (
            "Separating correlation from causation works by hunting "
            "the third variable. The investigator first measures the "
            "association honestly - computing the correlation and "
            "plotting the scatter to see its shape and check for "
            "outliers driving it. Then the interrogation begins: "
            "could a hidden factor cause both, could the effect "
            "cause the supposed cause in reverse, could coincidence "
            "plus a small sample be faking the pattern. The decisive "
            "move is control: hold the suspected third variable "
            "constant and see if the association survives - when "
            "temperature is fixed, the ice-cream-drowning link "
            "vanishes, exposing it as a summer artifact. The gold "
            "standard is the experiment: deliberately change the "
            "suspected cause while controlling everything else, and "
            "watch whether the effect follows. When experiments are "
            "impossible, Hill's viewpoints score the case: strong "
            "associations, consistent across studies, with the cause "
            "preceding the effect and a dose-response gradient, earn "
            "causal trust. The verdict is always provisional - new "
            "evidence can reopen any case."
        ),
        "key_points": [
            "Correlation is things changing together; causation is one making the other change - the first never proves the second.",
            "Hidden third variables manufacture most false correlations, like summer heat behind ice cream and drownings.",
            "The correlation coefficient measures strength from -1 to +1, but no value proves cause.",
            "The decisive test is control: hold the suspected third variable constant and see if the link survives.",
            "Hill's nine viewpoints score when an association deserves to be called a cause.",
        ],
        "requirements": [
            "The association measured honestly with the correlation computed and the scatter plotted.",
            "A hunt for third variables that could drive both sides of the pair.",
            "Checks for reverse causation and small-sample coincidence.",
            "Control of suspected confounders, or a direct experiment changing the supposed cause.",
            "Hill's viewpoints applied before any causal claim is published.",
        ],
        "standards": [
            "Causal language is reserved for tested relationships, not observed associations.",
            "Confounder control is demonstrated, not assumed.",
            "Causal verdicts are stated as provisional and evidence-graded.",
        ],
        "citations": [CIT_HILL, CIT_MILL, CIT_PEARSON],
        "sig_lens": (
            "The Signature read: correlation is two witnesses walking "
            "the same road - it does not prove they conspired. The "
            "Signature Method of Inquiry demands the third witness be "
            "found and questioned: the hidden season, the common "
            "driver, the quiet confounder. Only when the link "
            "survives interrogation may it testify as cause."
        ),
    },
    {
        "key": "placebo_blinding",
        "name": "The Placebo Effect and Blinding",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "The placebo effect is the mind's power to change the body "
            "when it believes it is being treated: patients given "
            "sugar pills often improve, sometimes dramatically, "
            "because expectation itself is a treatment. This makes "
            "testing medicines treacherous - a new drug must beat not "
            "just nothing, but belief. The defense is the placebo "
            "control: one group gets the real treatment, another gets "
            "an identical-looking fake, and the drug must outperform "
            "the fake to earn its claim. But there is a second trap: "
            "if patients know which group they are in, or if doctors "
            "treating them know, expectations leak into the results. "
            "Blinding seals the leak. In a single-blind trial the "
            "patient does not know; in a double-blind trial neither "
            "the patient nor the administering doctor knows - only a "
            "sealed code, broken after the data is in. Double-blind, "
            "placebo-controlled, randomized trials are the gold "
            "standard of medical evidence for exactly this reason: "
            "they strip away belief, hope, and observer bias, leaving "
            "only what the treatment itself does."
        ),
        "how_it_works": (
            "Placebo-controlled blinding works by making belief "
            "identical across groups. The trial recruits patients, "
            "then randomly assigns each to treatment or placebo - the "
            "placebo matched in appearance, taste, and ritual so no "
            "one can tell. Neither patients nor the staff measuring "
            "outcomes know who got what; the code is held by a third "
            "party until analysis is complete. Both groups are "
            "measured with the same instruments on the same "
            "schedule, so the only systematic difference is the "
            "active ingredient. The analysis compares recovery rates: "
            "if 78 of 100 treated patients recover against 52 of 100 "
            "on placebo, the treatment's real edge is the 26-point "
            "difference, not the 78 percent headline. Statistical "
            "tests then ask whether that edge exceeds chance. When "
            "the code is finally broken, any group difference can "
            "only be the treatment's doing - belief was equal, "
            "procedure was equal, only the chemistry differed. That "
            "is why regulators demand this design before approving "
            "medicines."
        ),
        "key_points": [
            "The placebo effect is real improvement from belief alone - expectation is itself a treatment.",
            "A new treatment must beat an identical-looking fake, not just nothing.",
            "Single-blind hides the group from the patient; double-blind hides it from the measurers too.",
            "The treatment's true edge is the difference over placebo, never the raw recovery rate.",
            "Double-blind, placebo-controlled, randomized trials are the gold standard of medical evidence.",
        ],
        "requirements": [
            "A placebo matched to the treatment in appearance and ritual.",
            "Random assignment of subjects to treatment and placebo groups.",
            "Blinding of subjects and of everyone measuring outcomes, with a sealed code.",
            "Identical measurement schedules and instruments across groups.",
            "Analysis of the difference over placebo before the code is broken.",
        ],
        "standards": [
            "Blinding status is reported for every trial: who knew what, and when the code was broken.",
            "Placebo characteristics are described so adequacy can be judged.",
            "Efficacy claims are stated as improvement over placebo with uncertainty.",
        ],
        "citations": [CIT_BERNARD, CIT_FISHER, CIT_BELMONT],
        "sig_lens": (
            "The Signature read: the placebo is the test of the "
            "oath against hope - belief itself put in the control "
            "group so it cannot testify for the treatment. The "
            "Signature Method of Inquiry seals every leak of "
            "expectation with blinding, for a verdict tainted by "
            "hope is testimony from a coached witness."
        ),
    },
    {
        "key": "predictions_models",
        "name": "Predictions and Models",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "A scientific model is a simplified picture of reality "
            "that can make predictions: an equation, a diagram, a "
            "computer simulation, even a physical miniature. Models "
            "are deliberately incomplete - a map that showed every "
            "blade of grass would be useless - and their power comes "
            "from keeping what matters and dropping the rest. The "
            "test of a model is prediction: it must say what will "
            "happen in situations it has not seen, and then nature "
            "grades the answer. Newton's laws predicted the return "
            "of Halley's comet; climate models predict warming from "
            "greenhouse gases; a simple linear model predicts plant "
            "height from fertilizer. Predictions are checked with "
            "residuals - the gaps between predicted and observed - "
            "and a good model's residuals are small and patternless. "
            "When predictions fail systematically, the model is "
            "revised, not the data. Models also have domains: "
            "Newton's laws predict cannonballs beautifully and atoms "
            "terribly, and knowing where a model stops working is "
            "part of knowing the model. The ladder from hypothesis "
            "to theory is paved with models that kept predicting "
            "right."
        ),
        "how_it_works": (
            "Models work by compressing reality into a calculable "
            "form and then betting on the future. The modeler "
            "chooses the essential variables and their "
            "relationships - often an equation fitted to existing "
            "data, such as height equals a base plus a rate times "
            "fertilizer. The model is then run on new conditions to "
            "generate predictions before the outcomes are known. "
            "When observations arrive, each prediction is compared "
            "to its observation, and the residuals - the misses - "
            "are examined: small random misses mean a healthy "
            "model, while a pattern in the misses means the model "
            "is missing something systematic, like curvature or an "
            "unmodeled factor. The model's error is summarized, for "
            "example as the root-mean-square of the residuals, and "
            "tracked as the model is refined. Crucially, models are "
            "tested on data they were not built from - testing on "
            "training data is grading your own homework. A model "
            "that predicts new data well earns trust; one that only "
            "describes old data is a summary, not a discovery."
        ),
        "key_points": [
            "A model is a simplified, calculable picture of reality whose test is prediction.",
            "Good models keep what matters and drop the rest; completeness is not the goal.",
            "Residuals - the gaps between predicted and observed - diagnose model health.",
            "Models must be tested on new data, never only on the data they were built from.",
            "Every model has a domain: knowing where it stops working is part of knowing it.",
        ],
        "requirements": [
            "The essential variables and their assumed relationships stated explicitly.",
            "Predictions generated for unseen conditions before outcomes are known.",
            "Residuals computed and examined for patterns, not just averaged away.",
            "Validation on independent data separate from any fitting data.",
            "The domain of applicability stated: where the model is trusted and where it is not.",
        ],
        "standards": [
            "Models are judged by prediction on new data, not fit to old data.",
            "Assumptions and simplifications are declared, not hidden.",
            "Prediction errors are reported with the same honesty as experimental errors.",
        ],
        "citations": [CIT_NEWTON, CIT_PEARSON, CIT_KUHN],
        "sig_lens": (
            "The Signature read: the model is the sworn map - a "
            "promise about territory not yet traveled. The "
            "Signature Method of Inquiry grades the map by the "
            "journey: where prediction meets observation the map "
            "holds, where residuals gather in patterns the map "
            "must be redrawn, for an oath about the future is "
            "only as good as its arrivals."
        ),
    },
    {
        "key": "falsifiability",
        "name": "Falsifiability",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Falsifiability is the line between science and "
            "non-science: a claim is scientific only if some "
            "possible observation could prove it wrong. 'All swans "
            "are white' is falsifiable - one black swan refutes it, "
            "and indeed black swans were found in Australia. 'An "
            "invisible force guides events but leaves no trace' is "
            "not falsifiable - no observation could ever contradict "
            "it, so it can never be tested. Popper's great insight "
            "was that science advances not by proving ideas true - "
            "no finite set of observations can do that - but by "
            "ruthlessly trying to prove them false and keeping the "
            "survivors. A hypothesis that survives genuine attempts "
            "at refutation earns the title 'corroborated', which is "
            "the highest honor the method bestows. This is why "
            "scientists design the strongest possible tests of "
            "their own ideas: the severe test. A claim that explains "
            "everything - that absorbs every possible outcome - "
            "explains nothing, because it risks nothing. "
            "Falsifiability does not mean false; it means honest "
            "enough to be checkable."
        ),
        "how_it_works": (
            "Falsifiability works as a gate and a discipline. At the "
            "gate, each claim is interrogated: what observation, if "
            "seen, would force us to abandon it. Claims with a "
            "clear answer pass into science; claims that can wriggle "
            "out of any result - through vague terms, moving "
            "goalposts, or untestable helpers - stay outside. As a "
            "discipline, the investigator then designs the severe "
            "test: the experiment most likely to produce the "
            "refuting observation if the idea is wrong. Auxiliary "
            "assumptions are listed in advance, so a failed "
            "prediction cannot be rescued by inventing excuses "
            "afterward. When refutation arrives, the honest "
            "response is revision or rejection - though history "
            "shows scientists rightly demand that the refuting "
            "evidence itself be solid before abandoning a "
            "well-tested idea. The scoreboard of a mature field is "
            "written in survived severe tests: each one a battle "
            "the idea won, none of them a final victory. "
            "Falsifiability keeps the whole enterprise honest by "
            "keeping every claim permanently at risk."
        ),
        "key_points": [
            "A claim is scientific only if some possible observation could prove it wrong.",
            "Science advances by surviving attempts at refutation, not by accumulating proof.",
            "The severe test - the experiment most likely to refute the idea - is the gold standard.",
            "Claims that absorb every possible outcome explain nothing because they risk nothing.",
            "Falsifiability does not mean false; it means honest enough to be checkable.",
        ],
        "requirements": [
            "For every claim, a stated observation that would force its abandonment.",
            "Auxiliary assumptions listed before testing, so failures cannot be excused afterward.",
            "Severe tests designed: genuine attempts at refutation, not victory laps.",
            "Refuting evidence held to the same solidity standard as supporting evidence.",
            "A scoreboard of survived severe tests maintained as the idea's credentials.",
        ],
        "standards": [
            "Scientific claims carry their refutation conditions openly.",
            "Post-hoc rescue hypotheses are flagged and tested separately, not smuggled in.",
            "Corroboration is reported as survival of severe tests, never as proof.",
        ],
        "citations": [CIT_POPPER, CIT_KUHN, CIT_MILL],
        "sig_lens": (
            "The Signature read: falsifiability is the oath's "
            "honor clause - the sworn statement of what would make "
            "the swearer admit defeat. The Signature Method of "
            "Inquiry holds an unruggable claim in contempt: a "
            "covenant that cannot be broken is not a covenant but "
            "a cage, and only the breakable oath can earn trust."
        ),
    },
])
ENTRIES.extend([
    {
        "key": "pitfalls",
        "name": "Data Interpretation Pitfalls",
        "group": "Compounded",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "Data interpretation is where good experiments go to be "
            "misread, and the pitfalls have names every investigator "
            "should memorize. Confirmation bias is seeing the "
            "pattern you hoped for in noise that holds no pattern. "
            "Cherry-picking is reporting the three trials that worked "
            "and burying the seven that did not. P-hacking is "
            "testing twenty comparisons and trumpeting the one that "
            "crosses the significance line by luck - with twenty "
            "tests at the five-percent level, a false alarm is "
            "expected more than sixty percent of the time. HARKing - "
            "hypothesizing after the results are known - is "
            "pretending a discovered pattern was the prediction all "
            "along. The Texas sharpshooter draws the bullseye around "
            "the bullet holes. Survivorship bias studies only the "
            "winners and forgets the graveyard of losers. Regression "
            "to the mean makes extreme first measurements drift back "
            "toward average on retest, looking like improvement. The "
            "defense against every one of these is the same boring "
            "discipline: pre-register the hypothesis and the analysis "
            "plan, report everything, and let others check the work. "
            "Pitfalls are not character flaws; they are the default "
            "settings of the human mind, and the method is the "
            "override."
        ),
        "how_it_works": (
            "Avoiding pitfalls works by removing the investigator's "
            "own cleverness from the verdict. Before data collection, "
            "the hypothesis, the sample size, the analysis method, "
            "and the rule for support are written down - "
            "pre-registered - so the analysis cannot be steered "
            "toward a pleasing result. During analysis, all "
            "comparisons actually run are reported, not just the "
            "significant ones; when many tests are run, the "
            "significance bar is raised to account for the "
            "multiplicity, because twenty tests at five percent "
            "produce a false positive most of the time. Exploratory "
            "findings are labeled as exploratory - interesting, "
            "worth following up, but not conclusions. Results are "
            "then handed to independent eyes: peer review and "
            "replication exist precisely because self-deception is "
            "invisible from the inside. The investigator also "
            "practices adversarial thinking, asking at each step "
            "'what would my sharpest critic say is wrong here' and "
            "answering honestly in the report's limitations "
            "section. These habits do not make science slow; they "
            "make it the only human enterprise with a built-in "
            "lie detector."
        ),
        "key_points": [
            "Confirmation bias, cherry-picking, p-hacking, HARKing, and survivorship bias are the classic traps.",
            "Twenty tests at the five-percent level produce a false alarm most of the time - multiplicity must be accounted for.",
            "Pre-registration locks the hypothesis and analysis plan before data can steer them.",
            "Exploratory findings are labeled as such: interesting leads, not conclusions.",
            "Adversarial self-review - arguing the critic's case - belongs in every limitations section.",
        ],
        "requirements": [
            "A pre-registered hypothesis, sample size, and analysis plan before data collection.",
            "Full reporting of all comparisons run, not only the significant ones.",
            "Multiplicity correction whenever many tests are performed.",
            "Clear labeling of exploratory versus confirmatory findings.",
            "Independent checking through peer review and replication.",
        ],
        "standards": [
            "Analysis plans are fixed before data collection and deviations are disclosed.",
            "Significance claims account for the number of tests performed.",
            "Limitations sections report the critic's case, not only the author's.",
        ],
        "citations": [CIT_FISHER, CIT_POPPER, CIT_MERTON],
        "sig_lens": (
            "The Signature read: the pitfalls are the oath-breakers "
            "within - the mind's own talent for coaching its witness. "
            "The Signature Method of Inquiry treats pre-registration "
            "as the sealed testimony: what was sworn before the "
            "data cannot be rewritten after it, and the sealed "
            "record is what keeps the swearer honest."
        ),
    },
    {
        "key": "reports",
        "name": "Writing a Scientific Report",
        "group": "Compounded",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "A scientific report is the experiment's permanent "
            "testimony: written so completely that a stranger could "
            "repeat the work and judge the conclusion. The classic "
            "structure is IMRaD - Introduction, Methods, Results, "
            "and Discussion. The Introduction states the question, "
            "the background, and the hypothesis. The Methods section "
            "is the recipe: subjects, materials, procedures, "
            "instruments, and analysis, in enough detail for "
            "replication - the most important and most "
            "under-written section. The Results section reports "
            "what was found, with tables, graphs, and numbers, and "
            "no interpretation yet. The Discussion interprets: "
            "what the results mean, how they compare with prior "
            "work, what the limitations are, and what should come "
            "next. An abstract up front summarizes the whole story "
            "in a paragraph, and references at the back credit the "
            "work built upon. The style rules are simple: past "
            "tense for what was done, precise numbers with units, "
            "no adjectives doing the work of data, and every claim "
            "traceable to the evidence. A report is not literature; "
            "it is an instruction manual for rebuilding the "
            "experiment and re-grading the verdict."
        ),
        "how_it_works": (
            "Report writing works by reconstructing the investigation "
            "for an absent reader. The investigator starts with the "
            "lab notebook and the raw data, and drafts the Methods "
            "first while the procedures are fresh - every step, "
            "every setting, every instrument model number. Results "
            "are then written from the checked analysis: the key "
            "tables and figures first, each with a caption stating "
            "what was measured and how, then the text walking the "
            "reader through them without repeating every number. "
            "The Introduction is drafted next, framing the question "
            "and stating the hypothesis exactly as it stood before "
            "the test. The Discussion is written last and hardest: "
            "the verdict on the hypothesis, the comparison with "
            "other studies, the honest limitations, the next "
            "questions. The abstract compresses all of this into "
            "one paragraph of question, method, result, and "
            "conclusion. Finally the draft is read by a colleague "
            "who was not involved - the first peer review - and "
            "every point of confusion is fixed, because confusion "
            "in the reader means incompleteness in the report."
        ),
        "key_points": [
            "IMRaD - Introduction, Methods, Results, Discussion - is the classic report structure.",
            "The Methods section is the replication recipe and the most important section.",
            "Results report findings with tables and graphs; interpretation waits for the Discussion.",
            "Every claim must be traceable to evidence; adjectives never substitute for data.",
            "A colleague's confused reading means the report is incomplete, not the reader is slow.",
        ],
        "requirements": [
            "An Introduction stating the question, background, and pre-test hypothesis.",
            "A Methods section complete enough for independent replication.",
            "A Results section with tables, figures, and numbers, free of interpretation.",
            "A Discussion with the verdict, comparisons, limitations, and next questions.",
            "An abstract and full references crediting prior work.",
        ],
        "standards": [
            "Methods are reported with instrument models, settings, and procedures in full.",
            "Results distinguish observed data from interpretation.",
            "Limitations are stated plainly; next steps follow from the findings.",
        ],
        "citations": [CIT_BERNARD, CIT_MERTON, CIT_FISHER],
        "sig_lens": (
            "The Signature read: the report is the sealed testimony "
            "delivered to the future - the complete sworn record "
            "from question to verdict. The Signature Method of "
            "Inquiry judges a report by one test: could a stranger, "
            "with this document alone, rebuild the trial and "
            "re-grade the verdict. If yes, the oath is kept."
        ),
    },
    {
        "key": "instruments",
        "name": "Scientific Instruments and Tools",
        "group": "Compounded",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "Scientific instruments are senses with superpowers: they "
            "extend observation beyond what eyes and hands can do. "
            "Thermometers read heat, balances read mass, timers read "
            "duration; microscopes open the tiny, telescopes open the "
            "distant, spectrometers open the composition of light "
            "itself. Every instrument is a bargain: it trades direct "
            "experience for reach and precision, and the price of the "
            "bargain is calibration. An uncalibrated instrument is a "
            "confident liar - precise, repeatable, and wrong - so "
            "every instrument is checked against a known reference "
            "before it testifies. Instruments also have ranges and "
            "resolutions: a kitchen scale cannot weigh a feather, and "
            "a ruler cannot measure a bacterium. Choosing the right "
            "tool means matching the instrument's range and "
            "resolution to the question, then verifying it behaves. "
            "Modern instruments often include software, which is "
            "itself an instrument needing validation: the algorithm "
            "that converts sensor readings to displayed numbers must "
            "be checked like any lens. The history of science is half "
            "the history of instruments - each new tool opened a new "
            "world to observe, and each new world demanded new "
            "questions."
        ),
        "how_it_works": (
            "Instruments work by transduction and trust. A sensor "
            "converts the phenomenon - heat, light, force, "
            "chemistry - into a readable signal, and the "
            "investigator converts the signal into a number with a "
            "known uncertainty. Trust is earned through calibration: "
            "the instrument measures certified references across "
            "its range, and any offset becomes a correction "
            "applied to all readings - for example, an offset of "
            "0.3 units found against the standard is subtracted "
            "from every measurement. The calibration is repeated "
            "on schedule, because instruments drift with time, "
            "temperature, and wear. During use, the investigator "
            "stays inside the calibrated range and honors the "
            "resolution: no reporting digits the instrument cannot "
            "resolve. Controls and blanks run alongside real "
            "samples - a blank with no sample should read zero, "
            "and if it does not, the instrument is talking about "
            "itself, not the world. When the tool, its "
            "calibration, and its limits are all documented, the "
            "numbers it produces can testify."
        ),
        "key_points": [
            "Instruments extend the senses but trade direct experience for reach - the price is calibration.",
            "An uncalibrated instrument is a confident liar: precise, repeatable, and wrong.",
            "Match the instrument's range and resolution to the question being asked.",
            "Calibration against certified references, repeated on schedule, earns the numbers their trust.",
            "Blanks and controls run alongside samples prove the instrument is measuring the world, not itself.",
        ],
        "requirements": [
            "An instrument whose range and resolution fit the quantities being measured.",
            "Calibration against certified references across the working range before use.",
            "A documented calibration schedule, because instruments drift.",
            "Blanks and controls in every measurement run.",
            "Software and algorithms in the measurement chain validated like any physical lens.",
        ],
        "standards": [
            "No measurement is reported from an uncalibrated instrument.",
            "Calibration references are traceable and their uncertainties stated.",
            "Reported digits never exceed the instrument's demonstrated resolution.",
        ],
        "citations": [CIT_GALILEO, CIT_ISO5725, CIT_BERNARD],
        "sig_lens": (
            "The Signature read: the instrument is the sworn "
            "deputy of the senses - empowered to witness what "
            "eyes cannot, and bound by calibration as its oath of "
            "office. The Signature Method of Inquiry strips the "
            "badge from any deputy never sworn against a "
            "reference: uncalibrated testimony is rumor with a "
            "digital display."
        ),
    },
    {
        "key": "repeating",
        "name": "Repeating and Reproducing Results",
        "group": "Compounded",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "A result that only happens once, for one team, might be "
            "a discovery or might be a mistake - and science has "
            "exactly one way to tell: do it again. Repetition is the "
            "same team running the same experiment again to check "
            "stability; reproduction is an independent team running "
            "it their own way to check generality. Both are "
            "non-negotiable. History is littered with exciting "
            "findings that evaporated on repeat: cold fusion in "
            "1989 entranced the world until other labs found "
            "nothing, and the 'discovery' dissolved into "
            "measurement error. Replication failures are not "
            "embarrassments to hide - they are the method working "
            "as designed, filtering error out of the record. A "
            "result that survives independent reproduction graduates "
            "from 'one lab's claim' to 'a fact about the world'. "
            "The modern reproducibility movement has made this "
            "explicit: share the data, share the code, pre-register "
            "the plan, and invite the world to check. Trust in "
            "science does not come from scientists being "
            "infallible; it comes from a system designed to catch "
            "them being fallible."
        ),
        "how_it_works": (
            "Repetition works as a two-stage filter. Stage one is "
            "internal: the original team repeats the key "
            "measurements, ideally with fresh samples and a "
            "blinded analyst, and checks that the effect reappears "
            "within the expected uncertainty - two runs giving "
            "means of 12.30 and 12.34 with a tolerance of 0.10 "
            "agree; a third run at 13.5 demands investigation. "
            "Stage two is external: independent teams, working "
            "from the published methods, attempt the result in "
            "their own labs with their own equipment. Successful "
            "reproduction across different setups proves the "
            "effect lives in nature, not in one lab's quirks. "
            "When reproduction fails, the community investigates "
            "rather than averts its eyes: was a hidden condition "
            "different, was the original a statistical fluke, was "
            "there an undisclosed flexibility in the analysis. "
            "The infrastructure of trust - open data, open code, "
            "detailed methods, pre-registration - exists to make "
            "stage two cheap and routine. A field where most "
            "results reproduce is a field whose textbooks can be "
            "believed."
        ),
        "key_points": [
            "Repetition is the same team checking stability; reproduction is independent teams checking generality.",
            "A result that survives independent reproduction graduates from claim to fact.",
            "Replication failures are the method working as designed, filtering error from the record.",
            "Cold fusion in 1989 is the cautionary tale: excitement is not evidence.",
            "Open data, open code, and pre-registration make independent checking cheap and routine.",
        ],
        "requirements": [
            "Internal repetition of key measurements with fresh samples before publication.",
            "Published methods complete enough for independent reproduction.",
            "Shared data and analysis code so others can verify every step.",
            "A tolerance defined in advance for what counts as successful repetition.",
            "Honest investigation, not defensiveness, when reproduction fails.",
        ],
        "standards": [
            "Key findings are repeated internally before they are claimed.",
            "Data and code accompany publication wherever possible.",
            "Failed reproductions are published and investigated, not suppressed.",
        ],
        "citations": [CIT_MERTON, CIT_FISHER, CIT_POPPER],
        "sig_lens": (
            "The Signature read: repetition is the recall of the "
            "witness - the same testimony given again to test its "
            "steadiness - and reproduction is the second witness, "
            "independent and uncoached. The Signature Method of "
            "Inquiry admits no verdict on a single witness: only "
            "when the testimony survives recall and the second "
            "witness agrees does the record call it fact."
        ),
    },
    {
        "key": "peer_review",
        "name": "Peer Review and Publishing",
        "group": "Compounded",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "Peer review is science's quality inspection: before a "
            "finding enters the permanent literature, independent "
            "experts examine the work for flaws. The investigator "
            "submits a manuscript to a journal; the editor sends it "
            "- usually without the author's name attached, and "
            "always without the reviewers' names revealed - to two "
            "or three specialists who probe the methods, the "
            "analysis, and the logic. Reviewers ask the hard "
            "questions: are the controls adequate, do the numbers "
            "support the claims, was prior work cited fairly, are "
            "alternative explanations addressed. The verdicts are "
            "accept, revise, or reject, and 'revise' is the most "
            "common - peer review is a negotiation toward "
            "rigor, not a coronation. The system is imperfect: "
            "reviewers are busy, biased toward the familiar, and "
            "occasionally wrong - but it remains the best filter "
            "humanity has found. Publication is what makes a result "
            "part of science at all: unpublished work cannot be "
            "checked, cited, or built upon. The published paper, "
            "with its data and methods exposed, is the unit of "
            "scientific currency - and peer review is the mint's "
            "assay office."
        ),
        "how_it_works": (
            "Peer review works as structured adversarial checking. "
            "The author prepares the manuscript to journal "
            "standards: complete methods, honest results, "
            "measured claims, full references. The editor "
            "triage-rejects work that is out of scope or clearly "
            "unsound, then assigns reviewers with no conflicts of "
            "interest. Reviewers work through a checklist: is the "
            "question clear and the hypothesis pre-stated, are the "
            "methods adequate and replicable, is the analysis "
            "correct, do the conclusions follow, is the literature "
            "fairly represented. Their reports return to the "
            "author with required and suggested changes; the "
            "author revises and answers each point, and the cycle "
            "repeats until the editor is satisfied. Rejection is "
            "normal - most papers are rejected somewhere before "
            "finding their journal - and revision almost always "
            "improves the work. After publication, review "
            "continues in public: citations, commentaries, and "
            "replication attempts keep grading the paper for "
            "years. The process assumes reviewers are expert, "
            "honest, and disinterested - which is why conflicts "
            "are disclosed and the whole exchange is documented."
        ),
        "key_points": [
            "Peer review is independent expert inspection of methods, analysis, and logic before publication.",
            "The common verdict is 'revise': review is a negotiation toward rigor, not a coronation.",
            "Reviewers check controls, numbers, claims, citations, and alternative explanations.",
            "Rejection is normal and revision almost always improves the work.",
            "Publication makes a result part of science; unpublished work cannot be checked or built upon.",
        ],
        "requirements": [
            "A manuscript with complete methods, honest results, and measured claims.",
            "Submission to a journal whose scope fits the work.",
            "Reviewers with relevant expertise and no conflicts of interest.",
            "Point-by-point responses to reviewer critiques with genuine revisions.",
            "Post-publication openness: data shared, questions answered, corrections issued when needed.",
        ],
        "standards": [
            "Methods are complete enough that reviewers can judge replicability.",
            "Claims never exceed what the reviewed evidence supports.",
            "Conflicts of interest are disclosed by authors, reviewers, and editors.",
        ],
        "citations": [CIT_MERTON, CIT_KUHN, CIT_BERNARD],
        "sig_lens": (
            "The Signature read: peer review is the council of "
            "witnesses - independent experts cross-examining the "
            "testimony before it enters the permanent record. The "
            "Signature Method of Inquiry honors the council's "
            "verdict while remembering its humanity: the assay "
            "office can err, which is why the record stays open "
            "to re-examination forever."
        ),
    },
    {
        "key": "theories",
        "name": "Scientific Theories vs Hypotheses",
        "group": "Advanced",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "In everyday speech 'theory' means a guess; in science "
            "it means the opposite - the most trusted form of "
            "knowledge there is. A hypothesis is a single testable "
            "prediction, young and at risk. A scientific theory is "
            "a broad, well-tested explanation that unifies many "
            "hypotheses and facts: germ theory, plate tectonics, "
            "evolution by natural selection, general relativity. "
            "Theories earn the title by surviving countless severe "
            "tests, predicting phenomena nobody had seen, and "
            "absorbing new evidence without breaking. They are not "
            "graduated hypotheses - a theory does not become a law, "
            "and a law does not outrank a theory. Laws describe "
            "what happens, often as equations; theories explain "
            "why it happens. Newton's law of gravitation describes "
            "the fall; Einstein's general relativity explains it as "
            "curved spacetime. Theories remain open to revision - "
            "Newton's mechanics yielded to relativity at high "
            "speeds - but revision refines rather than erases: "
            "bridges still stand on Newton. Calling evolution "
            "'just a theory' mistakes the scientific meaning for "
            "the casual one; in science, 'theory' is the highest "
            "compliment evidence can pay."
        ),
        "how_it_works": (
            "Theories work as the load-bearing structures of "
            "knowledge. A new hypothesis is tested; survivors "
            "accumulate; patterns across many surviving "
            "hypotheses suggest a deeper explanation. That "
            "explanation is proposed as a theory and must then do "
            "three jobs: explain the known facts more simply than "
            "rivals, predict new phenomena that are then "
            "confirmed, and survive attempts to break it. Germ "
            "theory, for example, unified observations about "
            "contagion, predicted that sterilization would cut "
            "infection, and survived a century of microbial "
            "challenges. Theories organize entire fields: they "
            "tell researchers which questions matter, which "
            "methods fit, and what counts as evidence - Kuhn's "
            "'normal science'. When anomalies pile up that the "
            "theory cannot absorb, a crisis brews, and "
            "occasionally a new theory replaces the old - a "
            "paradigm shift - while preserving the old theory's "
            "successes as a special case. The journey from "
            "hypothesis to theory is measured in decades and "
            "thousands of tests; there are no shortcuts."
        ),
        "key_points": [
            "In science, 'theory' is the highest compliment evidence can pay - not a synonym for guess.",
            "Hypotheses are single testable predictions; theories are broad explanations unifying many of them.",
            "Laws describe what happens; theories explain why it happens - neither outranks the other.",
            "Theories must explain, predict new phenomena, and survive attempts to break them.",
            "Revision refines theories rather than erasing them: Newton still holds bridges up.",
        ],
        "requirements": [
            "A unifying explanation covering many tested hypotheses and facts.",
            "Successful predictions of phenomena not yet observed when proposed.",
            "Survival of repeated severe tests across independent teams and decades.",
            "Simplicity relative to rivals: explaining more with fewer assumptions.",
            "Openness to revision when genuine anomalies accumulate.",
        ],
        "standards": [
            "The term 'theory' is reserved for explanations with extensive surviving test records.",
            "Theories state their domain: where they apply and where they are known to break down.",
            "Superseding theories preserve the predecessor's confirmed predictions as special cases.",
        ],
        "citations": [CIT_KUHN, CIT_POPPER, CIT_NEWTON],
        "sig_lens": (
            "The Signature read: the hypothesis is a single sworn "
            "witness; the theory is the whole courthouse - walls of "
            "survived tests, roof of unifying explanation, foundation "
            "of confirmed prediction. The Signature Method of "
            "Inquiry grants the title only after decades of "
            "cross-examination, for a courthouse is built stone by "
            "stone, and no single stone may claim to be the "
            "building."
        ),
    },
    {
        "key": "limits",
        "name": "The Limits of Science",
        "group": "Advanced",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "Science is the most powerful way of knowing ever "
            "devised, and it is not omnicompetent: knowing its "
            "limits is part of using it well. Science answers "
            "questions about the observable world - what is, what "
            "was, what will be under stated conditions. It does "
            "not answer what ought to be: no experiment can prove "
            "that kindness is better than cruelty, because values "
            "are chosen, not measured. It struggles with the "
            "singular and unrepeatable: the exact causes of one "
            "historical event can be argued but never re-tested. "
            "It is bounded by its tools: questions requiring "
            "unbuildable instruments must wait. It is bounded by "
            "ethics: experiments that would answer a question but "
            "harm people must not be run. And it is bounded by "
            "complexity: chaotic systems like weather defeat "
            "long-range prediction no matter how good the "
            "physics. None of this diminishes science - a tool "
            "with known limits is more trustworthy than one "
            "claimed to do everything. The honest scientist says "
            "'science cannot answer that' as readily as 'the data "
            "shows this', and the honest citizen asks of every "
            "claim whether it is even the kind of claim science "
            "could settle."
        ),
        "how_it_works": (
            "Working within the limits operates as a sorting "
            "discipline. Each question is classified: empirically "
            "testable now, testable in principle but not yet, or "
            "not empirically decidable at all. Testable-now "
            "questions get the full method. Testable-in-principle "
            "questions get careful theoretical work and a watch "
            "for new instruments - the Higgs boson waited "
            "decades for its collider. Non-empirical questions - "
            "moral, aesthetic, metaphysical - are handed to "
            "philosophy, law, art, and conscience, with science "
            "supplying relevant facts but not the verdict. "
            "Ethical review boards enforce the moral boundary: "
            "proposals are screened for harm to people, animals, "
            "and the environment before any test runs. "
            "Complexity limits are handled with humility: models "
            "state their horizons, forecasts carry their "
            "uncertainties, and 'we do not know yet' is a "
            "complete and honorable answer. The method's power "
            "comes from this very restraint - by refusing to "
            "overclaim, science keeps every claim it does make "
            "worth believing."
        ),
        "key_points": [
            "Science answers what is and what will be under stated conditions; it does not decree what ought to be.",
            "Values are chosen, not measured - no experiment proves kindness better than cruelty.",
            "Ethics bounds inquiry: questions answerable only by harming people must not be tested that way.",
            "Complexity bounds prediction: chaos defeats long-range forecasts regardless of good physics.",
            "A tool with known limits is more trustworthy than one claimed to do everything.",
        ],
        "requirements": [
            "Every question classified: testable now, testable in principle, or not empirically decidable.",
            "Ethical review of proposals before any test involving people, animals, or the environment.",
            "Models and forecasts carrying stated horizons and uncertainties.",
            "'We do not know yet' accepted as a complete and honorable answer.",
            "Non-empirical questions referred to their proper domains with science supplying facts, not verdicts.",
        ],
        "standards": [
            "Scientific claims are fenced to the empirically testable.",
            "Ethical boundaries are enforced before testing, not regretted after.",
            "Uncertainty and horizons are stated wherever complexity limits prediction.",
        ],
        "citations": [CIT_POPPER, CIT_KUHN, CIT_BELMONT],
        "sig_lens": (
            "The Signature read: the oath knows its own borders - "
            "the witness testifies only to what was seen, never to "
            "what should be. The Signature Method of Inquiry "
            "counts overclaiming as perjury: the method's honor "
            "rests on refusing the questions it cannot honestly "
            "answer, and that refusal is what makes its answers "
            "worth swearing by."
        ),
    },
    {
        "key": "ethics",
        "name": "Ethics in Scientific Research",
        "group": "Advanced",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "Ethics is the conscience of the method: the set of "
            "rules ensuring the pursuit of knowledge never tramples "
            "the people it claims to serve. The foundations were "
            "written in the shadow of atrocity - medical "
            "experiments without consent taught the world that "
            "curiosity without conscience is a crime. The Belmont "
            "Report names the three governing principles. Respect "
            "for persons: participants are autonomous agents who "
            "must give informed, voluntary consent and may withdraw "
            "at any time. Beneficence: maximize benefit and minimize "
            "harm, with risks honestly weighed before the first "
            "subject is enrolled. Justice: the burdens and benefits "
            "of research must be shared fairly - no exploiting "
            "vulnerable populations for the benefit of others. "
            "Beyond human subjects, ethics covers honesty in "
            "reporting, fair credit to collaborators, care for "
            "animal subjects, and responsibility for how findings "
            "might be used. Institutional review boards enforce "
            "these principles by approving, modifying, or stopping "
            "proposals. The rule is absolute: no result, however "
            "brilliant, justifies an unethical experiment."
        ),
        "how_it_works": (
            "Research ethics works through review before action. "
            "The investigator writes a protocol describing the "
            "question, the procedures, the risks, the safeguards, "
            "and the consent process - then submits it to an "
            "independent review board before recruiting anyone. "
            "The board scores the proposal against the three "
            "Belmont principles: is consent truly informed and "
            "voluntary, are risks minimized and justified by the "
            "potential benefit, are subjects chosen fairly rather "
            "than conveniently. Approval may come with conditions "
            "- extra safeguards, clearer consent forms, ongoing "
            "monitoring - and the board can halt a study that goes "
            "off-protocol. During the study, adverse events are "
            "reported, consent is treated as ongoing rather than "
            "one-time, and data is anonymized to protect privacy. "
            "Publication ethics run in parallel: authorship "
            "reflects real contribution, conflicts of interest are "
            "disclosed, and data is reported honestly. The system "
            "assumes good intentions are not enough - structure, "
            "not virtue alone, keeps research humane."
        ),
        "key_points": [
            "The Belmont principles: respect for persons, beneficence, and justice.",
            "Informed, voluntary consent is required, and participants may withdraw at any time.",
            "Risks must be minimized and honestly weighed against potential benefits before enrollment.",
            "Review boards approve, modify, or stop proposals - ethics is enforced before action, not regretted after.",
            "No result, however brilliant, justifies an unethical experiment.",
        ],
        "requirements": [
            "A written protocol with procedures, risks, safeguards, and consent process.",
            "Independent ethical review and approval before any subject is recruited.",
            "Informed consent that is voluntary, comprehensible, and ongoing.",
            "Fair subject selection: no exploiting vulnerable populations.",
            "Honest reporting, fair authorship, and disclosed conflicts in publication.",
        ],
        "standards": [
            "No human-subjects research proceeds without prior independent ethical approval.",
            "Consent is documented and revocable at any point without penalty.",
            "Adverse events are reported promptly and studies halted when safety demands it.",
        ],
        "citations": [CIT_BELMONT, CIT_MERTON, CIT_BERNARD],
        "sig_lens": (
            "The Signature read: ethics is the oath above all oaths "
            "- the sworn promise that no witness shall be harmed "
            "for the sake of testimony. The Signature Method of "
            "Inquiry holds the unethical experiment void before it "
            "begins: a verdict built on coerced or harmed witnesses "
            "is not science but extraction, and the method "
            "disowns it."
        ),
    },
])
ENTRIES.extend([
    {
        "key": "feedback_loop",
        "name": "The Feedback Loop of Inquiry",
        "group": "Advanced",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "The scientific method is not a straight line but a "
            "loop: every conclusion feeds back into new "
            "observations, new questions, and new tests. A "
            "supported hypothesis suggests sharper predictions to "
            "try next; a refuted one demands a revised idea that "
            "explains both the old wins and the new loss; a "
            "surprise spawns a question nobody had thought to ask. "
            "This is why textbooks describe the method as a cycle "
            "rather than a staircase - the end of one investigation "
            "is the beginning of several more. The loop is also "
            "how knowledge converges: each cycle shrinks the "
            "error, like a feedback controller steering toward the "
            "target. Early measurements of a constant are rough; "
            "each generation of experiments corrects the last, and "
            "the value settles. The loop operates at every scale: "
            "within one lab across months, across a field across "
            "decades, across all of science across centuries. "
            "Crucially, the loop has no finish line - theories "
            "are never declared final, only current. The method's "
            "greatest strength is that it is permanently "
            "unfinished: every answer is a better question "
            "wearing a disguise."
        ),
        "how_it_works": (
            "The feedback loop works by routing every output back "
            "to the input. After the conclusion is drawn, the "
            "investigator explicitly asks three loop questions: "
            "what new prediction does this result suggest, what "
            "did we fail to explain, and what surprised us. "
            "Supported results generate extension studies - test "
            "the effect under new conditions, push the parameters "
            "further, look for the boundary where it breaks. "
            "Refuted results generate revision studies - modify "
            "the hypothesis minimally to cover the failure, then "
            "test the new version against both old and new data. "
            "Surprises generate exploration studies - follow the "
            "anomaly with fresh eyes and a new question. Each "
            "cycle is documented so the chain of reasoning stays "
            "auditable: question to hypothesis to test to "
            "conclusion to next question. Quantitatively, the "
            "loop converges when each cycle's error is a fraction "
            "of the last - an error shrinking by forty percent "
            "per cycle falls below eight percent of its start "
            "after five rounds. The loop stops for a project when "
            "further cycles stop changing the answer; it never "
            "stops for science as a whole."
        ),
        "key_points": [
            "The method is a loop, not a line: every conclusion seeds new questions and tests.",
            "Supported results suggest extensions; refuted results demand revisions; surprises demand exploration.",
            "Each cycle shrinks the error, converging on the truth like a feedback controller on its target.",
            "The chain of cycles is documented so the reasoning stays auditable end to end.",
            "The loop has no finish line: theories are current, never final.",
        ],
        "requirements": [
            "Three loop questions asked after every conclusion: new predictions, unexplained failures, surprises.",
            "Extension studies pushing supported results into new conditions and boundaries.",
            "Revision studies testing modified hypotheses against old and new data together.",
            "Documented chains linking each cycle's question to the previous cycle's conclusion.",
            "A stopping rule for the project: cycles end when answers stop changing.",
        ],
        "standards": [
            "Follow-up studies are designed from the previous conclusion, not from convenience.",
            "Revised hypotheses must account for all prior data, not just the latest failure.",
            "Convergence is demonstrated by shrinking error across cycles, not asserted.",
        ],
        "citations": [CIT_KUHN, CIT_POPPER, CIT_BERNARD],
        "sig_lens": (
            "The Signature read: the loop is the oath renewed - "
            "each verdict sworn again under sharper questioning, "
            "each cycle a deeper covenant with the truth. The "
            "Signature Method of Inquiry never closes the case: "
            "the testimony stands, but the investigation "
            "continues, for the world keeps speaking and the "
            "oath keeps listening."
        ),
    },
    {
        "key": "penicillin",
        "name": "Case Study: The Discovery of Penicillin",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "In September 1928 Alexander Fleming returned from "
            "holiday to his laboratory at St Mary's Hospital, "
            "London, and found something odd: a mold had "
            "contaminated a petri dish of Staphylococcus bacteria, "
            "and around the mold was a clear zone where the "
            "bacteria could not grow. A tidy researcher would have "
            "thrown the spoiled plate away; Fleming, curious, "
            "investigated instead. He identified the mold as "
            "Penicillium notatum, showed its juices killed many "
            "bacteria, and published the findings in 1929 - then "
            "the discovery sat nearly idle for a decade, because "
            "purifying the active substance was brutally hard. In "
            "1940 Howard Florey, Ernst Chain, and Norman Heatley "
            "at Oxford finally purified penicillin and proved it "
            "cured bacterial infections in animals and then "
            "people; mass production followed for the Second "
            "World War, and the 1945 Nobel Prize was shared by "
            "Fleming, Florey, and Chain. The case teaches the "
            "whole method in one story: prepared observation, "
            "followed by a twelve-year gap where the science was "
            "real but the engineering was not ready, followed by "
            "teamwork that turned a curiosity into the antibiotic "
            "age. Discovery is rarely a lightning bolt; it is "
            "usually a relay race."
        ),
        "how_it_works": (
            "The penicillin story works as a method checklist in "
            "action. Observation: the clear bacteria-free zone "
            "around the mold, noticed because Fleming was in the "
            "habit of examining even spoiled plates. Question: "
            "what in the mold kills bacteria, and how broadly. "
            "Hypothesis: the mold secretes an antibacterial "
            "substance. Test: grow the mold in broth, apply the "
            "broth to many bacterial species, and measure the "
            "killing - the 1929 paper reports the effect across "
            "staphylococci, streptococci, and others. Conclusion: "
            "a real antibacterial substance exists, but purification "
            "defeats Fleming's chemistry. The loop then spans a "
            "decade: Florey's team picks up the question, "
            "hypothesizes the substance can be purified and "
            "therapeutic, tests in mice and then in patients, and "
            "concludes with cures. The timeline itself is data: "
            "1928 observation, 1940 therapeutic proof, 1945 Nobel "
            "- twelve years from seeing to curing, seventeen "
            "from seeing to the prize, averaging nearly fifteen "
            "years of relay. The lesson is structural: observation "
            "without follow-through is trivia, and follow-through "
            "without observation has nothing to follow."
        ),
        "key_points": [
            "1928: Fleming's contaminated plate showed a bacteria-free zone around Penicillium mold - and he investigated instead of discarding it.",
            "The 1929 paper documented antibacterial action across many species, but purification defeated him.",
            "1940: Florey, Chain, and Heatley purified penicillin and proved it cured infections.",
            "Twelve years from observation to cure, seventeen to the Nobel: discovery is a relay race.",
            "The case compresses the whole method: observation, question, hypothesis, test, loop, teamwork.",
        ],
        "requirements": [
            "The habit of examining anomalies, including spoiled or failed setups.",
            "Identification of the active agent behind the observed effect.",
            "Broad testing across many targets to map the effect's range.",
            "The engineering follow-through to turn an observation into a usable result.",
            "Teamwork across disciplines and decades when one lab cannot finish the relay.",
        ],
        "standards": [
            "Anomalies are investigated before being discarded.",
            "Claims of effect are tested across multiple targets, not a single convenient one.",
            "Credit follows contribution: observation, purification, and proof each earn their share.",
        ],
        "citations": [CIT_FLEMING, CIT_BERNARD, CIT_MERTON],
        "sig_lens": (
            "The Signature read: Fleming kept the covenant of "
            "attention when the easy act was the trash bin - the "
            "spoiled plate became testimony because the witness "
            "refused to look away. The Signature Method of "
            "Inquiry honors the relay: the oath passes from "
            "observer to purifier to healer, and the prize "
            "belongs to the whole chain of kept promises."
        ),
    },
    {
        "key": "semmelweis",
        "name": "Case Study: Ignaz Semmelweis and Handwashing",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "In 1847 the Vienna General Hospital had two maternity "
            "clinics with a deadly puzzle: in the First Clinic, "
            "run by doctors, nearly one mother in five died of "
            "childbed fever; in the Second Clinic, run by "
            "midwives, far fewer died. Ignaz Semmelweis, a young "
            "physician, noticed the doctors went straight from "
            "autopsies to deliveries without washing their hands. "
            "He hypothesized that 'cadaveric particles' on "
            "doctors' hands carried the fever, and ordered "
            "chlorine handwashing - mortality in the First "
            "Clinic fell from 18.27 percent in 1846 to 1.27 "
            "percent in 1848, a reduction of about 93 percent. "
            "The data was overwhelming and the medical "
            "establishment rejected him anyway: his idea "
            "insulted doctors, lacked a germ theory to explain "
            "it, and Semmelweis himself communicated it badly. "
            "He died in 1865, the same year Lister began "
            "antiseptic surgery; germ theory later vindicated "
            "him completely. The case is the method's "
            "bittersweet monument: a perfect experiment - "
            "observation, hypothesis, intervention, dramatic "
            "result - defeated for decades by pride and "
            "paradigm. Evidence alone does not persuade; "
            "evidence plus humility, communication, and time "
            "does."
        ),
        "how_it_works": (
            "Semmelweis's investigation works as a textbook "
            "controlled comparison. Observation: the mortality "
            "gap between the doctors' clinic and the midwives' "
            "clinic, plus the death of his friend Kolletschka "
            "from a scalpel cut during an autopsy - the same "
            "fever, the same particles. Hypothesis: decaying "
            "matter on hands transmits childbed fever. Test: "
            "mandatory chlorine handwashing for everyone "
            "examining mothers in the First Clinic, with the "
            "Second Clinic as the ongoing comparison. Result: "
            "mortality collapses from 18.27 percent to 1.27 "
            "percent - a relative reduction of about 93 "
            "percent, one of the largest effects ever measured "
            "in medicine. Conclusion, correctly drawn: "
            "handwashing saves mothers. The failure came "
            "after the science: the establishment demanded a "
            "mechanism he could not supply, took offense at "
            "the implication, and buried the finding until "
            "germ theory arrived. The method's lesson is "
            "twofold: run the clean comparison and get the "
            "dramatic number, then do the human work - "
            "clear writing, respectful persuasion, and "
            "allies - because data without advocacy can wait "
            "a generation to save lives."
        ),
        "key_points": [
            "1847 Vienna: doctors' clinic lost 18.27 percent of mothers; midwives' clinic lost far fewer.",
            "Semmelweis linked autopsy-to-delivery hand contact to childbed fever and mandated chlorine handwashing.",
            "Mortality fell to 1.27 percent - about a 93 percent relative reduction.",
            "The establishment rejected the finding for decades: pride, no germ theory, poor communication.",
            "Evidence alone does not persuade; evidence plus humility, communication, and allies does.",
        ],
        "requirements": [
            "A puzzling difference between comparable groups, investigated rather than accepted.",
            "A mechanistic hypothesis linking the difference to a testable cause.",
            "An intervention applied to one group with the other as ongoing comparison.",
            "Mortality or outcome data recorded before and after, with the effect quantified.",
            "Clear, respectful communication of findings to the community that must act on them.",
        ],
        "standards": [
            "Comparisons use genuinely comparable groups with measured baseline differences.",
            "Effect sizes are quantified as both absolute and relative change.",
            "Findings are communicated with the clarity and respect the stakes demand.",
        ],
        "citations": [CIT_SEMMELWEIS, CIT_BERNARD, CIT_KUHN],
        "sig_lens": (
            "The Signature read: Semmelweis swore the oath and "
            "the numbers kept it - 18.27 to 1.27, the most "
            "eloquent testimony in medical history - yet the "
            "council refused the witness. The Signature Method "
            "of Inquiry draws the hard lesson: the covenant of "
            "attention is not complete at the verdict; the "
            "witness must also make the council listen, with "
            "clarity, humility, and allies, or the truth waits "
            "a generation."
        ),
    },
    {
        "key": "michelson_morley",
        "name": "Case Study: The Michelson-Morley Experiment",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "In 1887 Albert Michelson and Edward Morley ran the "
            "most famous 'failed' experiment in history - and "
            "failure was the triumph. Physicists then believed "
            "light traveled through an invisible 'luminiferous "
            "ether', and that Earth's motion through the ether "
            "should change light's measured speed depending on "
            "direction - like a swimmer's speed differing "
            "upstream versus across the current. Their "
            "interferometer split a light beam, sent the halves "
            "along perpendicular paths, and recombined them: any "
            "ether wind would shift the interference fringes by "
            "about 0.4 of a fringe. What they found was nothing "
            "- a shift below 0.01 fringe, less than three "
            "percent of expectation, essentially zero. They had "
            "set out to measure Earth's speed through the ether "
            "and instead proved the ether was not there. The "
            "null result detonated physics: Fitzgerald and "
            "Lorentz proposed length contraction to explain it, "
            "and in 1905 Einstein's special relativity removed "
            "the ether entirely, rebuilding space and time "
            "around the constancy of light's speed. The case is "
            "the method's crown jewel: a clean, precise test "
            "that returned 'no', and the 'no' was worth more "
            "than a thousand 'yeses'."
        ),
        "how_it_works": (
            "The experiment works as the severe test perfected. "
            "Hypothesis under test: the luminiferous ether "
            "exists, and Earth's orbital motion of 30 "
            "kilometers per second through it creates an ether "
            "wind. Prediction: light traveling with versus "
            "across the wind differs in round-trip time, "
            "shifting interference fringes by about 0.4 "
            "fringe as the apparatus rotates. Design: a "
            "stone-mounted interferometer floating on mercury "
            "for vibration isolation, measurements repeated at "
            "different times of day and year to catch the wind "
            "from every angle. Result: fringe shifts below "
            "0.01 - under three percent of the predicted 0.4 "
            "- a null result reproduced in every session. "
            "Interpretation, honestly drawn: the expected "
            "effect is absent, so the ether as conceived does "
            "not exist. The feedback loop then engaged at the "
            "scale of physics itself: contraction hypotheses, "
            "then relativity, then a century of confirmations. "
            "The ratio tells the story - observed over "
            "expected below 0.03 - precision turned a "
            "non-detection into a discovery. This is "
            "falsifiability with the gloves off: the ether "
            "was scientific precisely because Michelson and "
            "Morley could kill it, and kill it they did."
        ),
        "key_points": [
            "1887: the interferometer hunted Earth's motion through the 'luminiferous ether' carrying light.",
            "Prediction: fringe shifts of about 0.4 as the apparatus rotated; observation: below 0.01.",
            "The null result - under three percent of expectation - proved the ether was not there.",
            "The 'failure' detonated physics: length contraction, then Einstein's 1905 special relativity.",
            "The most valuable experiments are the severe tests: precise enough that 'no' means something.",
        ],
        "requirements": [
            "A quantitative prediction derived from the hypothesis under test.",
            "An instrument precise enough that the predicted effect would be unmistakable.",
            "Vibration isolation and repeated sessions covering all orientations and times.",
            "Honest reporting of the null: the absent effect published, not buried.",
            "Theoretical follow-through: when the foundation cracks, rebuild rather than patch forever.",
        ],
        "standards": [
            "Severe tests state the predicted effect size before measurement.",
            "Null results are published with the same completeness as positive ones.",
            "Precision is demonstrated sufficient to have seen the effect if it existed.",
        ],
        "citations": [CIT_MICHELSON, CIT_POPPER, CIT_KUHN],
        "sig_lens": (
            "The Signature read: Michelson and Morley swore the "
            "severest oath in physics - build the instrument so "
            "fine that nature cannot mumble - and nature "
            "answered with silence. The Signature Method of "
            "Inquiry counts that silence as the purest "
            "testimony: the witness asked the hardest possible "
            "question, the answer was no, and the no rebuilt "
            "the universe."
        ),
    },
    {
        "key": "everyday",
        "name": "Scientific Method in Everyday Life",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "The scientific method is not confined to laboratories "
            "- it is the operating system of good everyday "
            "thinking, running quietly behind countless daily "
            "decisions. The cook who changes one ingredient at a "
            "time to fix a recipe is controlling variables. The "
            "commuter who tries a new route for a week and times "
            "both is running a controlled comparison. The "
            "gardener who plants the same seeds in sun and shade "
            "is testing a hypothesis about light. The "
            "troubleshooter who asks 'what changed just before it "
            "broke' is hunting the independent variable; the one "
            "who changes one setting at a time is avoiding "
            "confounders. Even the method's social tools appear: "
            "asking a friend to taste-test two versions blind is "
            "blinding, and admitting the new route is slower is "
            "honest reporting of a refuted hypothesis. Teaching "
            "children the method does not require a lab coat - "
            "it requires the habits: notice, wonder, predict, "
            "test one thing, write down what happened, and "
            "believe the result over the wish. A society that "
            "thinks this way - in kitchens, garages, offices, "
            "and voting booths - is a society running the most "
            "important experiment of all: the experiment of "
            "governing itself by evidence."
        ),
        "how_it_works": (
            "Everyday science works by shrinking the laboratory "
            "to fit the moment. Notice the problem and state it "
            "plainly: the bread is too dense, the commute is too "
            "long, the plant is wilting. Form the one-change "
            "hypothesis: if I proof the dough longer, then the "
            "loaf will rise higher. Run the fair test: bake two "
            "loaves identical except for proofing time, or drive "
            "each route on similar-traffic days and time them. "
            "Record the numbers - rise in centimeters, minutes "
            "per trip - in the moment, not from memory. Compare "
            "against the control: the usual recipe, the usual "
            "route. Draw the fenced conclusion: longer proofing "
            "helped this dough in this kitchen, not all bread "
            "everywhere. Keep what worked, discard what did not "
            "without defensiveness, and let the next question "
            "follow: now that the rise is fixed, what about the "
            "crust. The whole cycle fits on an index card and "
            "takes an afternoon - yet it contains every step the "
            "professionals use, because the method is not "
            "equipment. It is a discipline of honesty, and it "
            "runs anywhere."
        ),
        "key_points": [
            "The cook changing one ingredient, the commuter timing two routes, the gardener testing sun versus shade: all run the method.",
            "Troubleshooting is variable-hunting: 'what changed just before it broke' names the independent variable.",
            "Blind taste-tests and honest admission of slower routes are blinding and honest reporting at home.",
            "Everyday conclusions stay fenced: what worked here, this time, under these conditions.",
            "The method is not equipment but a discipline of honesty - and it runs anywhere.",
        ],
        "requirements": [
            "A plainly stated everyday problem and a one-change hypothesis.",
            "A fair comparison: the usual way as control, the new way as the test.",
            "Numbers recorded in the moment: times, measures, counts.",
            "A fenced conclusion claiming only what this test showed.",
            "No defensiveness: keep what worked, discard what did not, ask the next question.",
        ],
        "standards": [
            "One change at a time, even in the kitchen.",
            "Comparisons use matched conditions, not cherry-picked occasions.",
            "Conclusions stay local to what was tested; extrapolation is labeled as guessing.",
        ],
        "citations": [CIT_BACON, CIT_MILL, CIT_BERNARD],
        "sig_lens": (
            "The Signature read: the method needs no laboratory "
            "- the kitchen, the garage, and the commute are all "
            "fit arenas for the oath. The Signature Method of "
            "Inquiry holds that a citizen who tests one change, "
            "records the number, and believes the result over "
            "the wish is practicing the same covenant as the "
            "great laboratories, only closer to dinner."
        ),
    },
])
