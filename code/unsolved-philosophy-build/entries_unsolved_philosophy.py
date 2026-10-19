#!/usr/bin/env python3
"""Entries for the Unsolved Philosophy databases (Manon's 2026-10-17 16:15
orders, Unsolved Problems Solved series batch 1).

Two NEW databases, 34 ladder-ordered records each:

  unsolved-philosophy            - The Unsolved Philosophy Database
                                   (public-harvest: the field's real, famous,
                                   fact-checked unsolved problems - meaning of
                                   life, the amoralist's challenge,
                                   skepticism, free will, personal identity,
                                   other minds, truth, the liar paradox,
                                   Zeno, sorites, beauty, art, justice, the
                                   state, the simulation hypothesis, ethics
                                   of belief, induction, the is-ought gap,
                                   moral realism, moral luck, Gettier,
                                   the Muenchhausen trilemma, mind-body, the
                                   hard problem of consciousness, the Chinese
                                   room, intentionality, perception,
                                   causation, time, Newcomb, Sleeping Beauty,
                                   scientific realism, underdetermination,
                                   Leibniz's question - every record carrying
                                   problem, background, why it matters, and
                                   a short pointer to the Signature
                                   solution; standard references Aristotle,
                                   Plato, Descartes, Locke, Hume, Kant,
                                   Mill, Frege, Russell, Wittgenstein,
                                   Popper, Quine, Kuhn, Rawls, Nozick,
                                   Parfit, Nagel, Chalmers, Searle, Bostrom,
                                   and the other landmarks cited per record)
  unsolved-philosophy-signature  - The Unsolved Philosophy Signature Database
                                   (his original Signature Resolution Method
                                   applied to each problem: fix the problem
                                   in exact record form, enumerate the live
                                   candidate resolutions, score each by
                                   explanatory coverage, predictive grip,
                                   and consistency, stress the winner
                                   against its strongest objection, and
                                   publish the scorecard with assumptions
                                   visible; src signature, titles suffixed
                                   " (Signature Edition)", every solution
                                   labeled "Signature-generated proposed
                                   solution - not established science",
                                   never presented as established positions)

34 records each, ladder-ordered by problem accessibility (ladder_rank 1-34;
foundations 1-11, compounded 12-23, advanced 24-34). Secular and analytical
throughout - no religious talk. Honesty rule: solutions are labeled
proposals, never proof, never consensus.

ID prefixes: JAH-USPL- (public) and JAH-USPLS- (signature), verified free
in the manifest id_prefix values and zero hits in every shard index file
in jah-databases-data-1 (USPL chosen over USPH to avoid Physics).

Numerical cores: all hand-computed 2026-10-17, machine-verified by the
demos (see demos_unsolved_philosophy.py). Every demo prints its real
computed values, asserts tight bounds (never float exact-equality), and
ends with the OK marker; the build machine-executes all 68 demos before
writing pages.

No website references. No Facebook. Never the words "bat belt" anywhere.
"""

SIG_TAIL = ("Signature original - his original Signature Resolution Method: "
            "fix the problem in exact record form, enumerate the live "
            "candidate resolutions, score each by explanatory coverage, "
            "predictive grip, and internal consistency, stress the winner "
            "against its strongest objection, and publish the scorecard with "
            "the assumptions visible. Clearly labeled Signature-made, never "
            "presented as established positions.")

SIG_LABEL = "Signature-generated proposed solution \u2014 not established science."

# ---------------------------------------------------------------- citations
CIT_PLATO_REP = "Plato. Republic. c. 380 BCE (Grube/Reeve trans., Hackett, 1992)."
CIT_ARISTOTLE_META = "Aristotle. Metaphysics. c. 350 BCE (Ross trans., Oxford, 1924)."
CIT_ARISTOTLE_ETH = "Aristotle. Nicomachean Ethics. c. 350 BCE (Irwin trans., Hackett, 1999)."
CIT_DESCARTES_MED = "Descartes R. Meditations on First Philosophy. 1641 (Cottingham trans., Cambridge, 1996)."
CIT_LOCKE_ESSAY = "Locke J. An Essay Concerning Human Understanding. 1689 (Nidditch ed., Oxford, 1975)."
CIT_HUME_TREATISE = "Hume D. A Treatise of Human Nature. 1739-1740 (Norton ed., Oxford, 2000)."
CIT_HUME_ENQUIRY = "Hume D. An Enquiry Concerning Human Understanding. 1748 (Beauchamp ed., Oxford, 1999)."
CIT_KANT_CPR = "Kant I. Critique of Pure Reason. 1781/1787 (Guyer/Wood trans., Cambridge, 1998)."
CIT_KANT_GROUND = "Kant I. Groundwork of the Metaphysics of Morals. 1785 (Gregor trans., Cambridge, 1997)."
CIT_MILL_UTIL = "Mill JS. Utilitarianism. 1863 (Crisp ed., Oxford, 1998)."
CIT_FREGE_SENSE = "Frege G. 'On Sense and Reference.' 1892 (in Translations from the Philosophical Writings, Black/Geach, 1980)."
CIT_RUSSELL_DENOTING = "Russell B. 'On Denoting.' Mind 14, 1905."
CIT_WITT_TRACT = "Wittgenstein L. Tractatus Logico-Philosophicus. 1921 (Pears/McGuinness trans., Routledge, 2001)."
CIT_WITT_PI = "Wittgenstein L. Philosophical Investigations. 1953 (Anscombe trans., Blackwell, 2001)."
CIT_POPPER_LOGIC = "Popper K. The Logic of Scientific Discovery. 1959 (Routledge, 2002)."
CIT_QUINE_DOGMAS = "Quine WVO. 'Two Dogmas of Empiricism.' Philosophical Review 60, 1951."
CIT_KUHN_STRUCT = "Kuhn TS. The Structure of Scientific Revolutions. 1962 (Univ. of Chicago Press, 1996)."
CIT_RAWLS_TJ = "Rawls J. A Theory of Justice. Harvard Univ. Press, 1971."
CIT_NOZICK_ASU = "Nozick R. Anarchy, State, and Utopia. Basic Books, 1974."
CIT_PARFIT_RP = "Parfit D. Reasons and Persons. Oxford Univ. Press, 1984."
CIT_NAGEL_BAT = "Nagel T. 'What Is It Like to Be a Bat?' Philosophical Review 83, 1974."
CIT_CHALMERS_FACING = "Chalmers DJ. 'Facing Up to the Problem of Consciousness.' Journal of Consciousness Studies 2, 1995."
CIT_SEARLE_MBP = "Searle JR. 'Minds, Brains, and Programs.' Behavioral and Brain Sciences 3, 1980."
CIT_BOSTROM_SIM = "Bostrom N. 'Are You Living in a Computer Simulation?' Philosophical Quarterly 53, 2003."
CIT_GETTIER_JTB = "Gettier E. 'Is Justified True Belief Knowledge?' Analysis 23, 1963."
CIT_LEWIS_WORLDS = "Lewis D. On the Plurality of Worlds. Blackwell, 1986."
CIT_MCTAGGART_TIME = "McTaggart JE. 'The Unreality of Time.' Mind 17, 1908."
CIT_LEIBNIZ_PSR = "Leibniz GW. 'On the Ultimate Origination of Things.' 1697 (in Philosophical Essays, Ariew/Garber, Hackett, 1989)."
CIT_SEP = "Stanford Encyclopedia of Philosophy. Metaphysics Research Lab, Stanford Univ. (plato.stanford.edu)."

ENTRIES = [
    # ---------------------------------------------------------- rank 1
    {
        "key": "meaning_of_life",
        "name": "What is the meaning of life?",
        "group": "Foundations",
        "branch": "Ethics",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "problem": ("Is there a meaning to human life, and if so, what is it? "
                    "The question asks whether a life can be objectively meaningful, "
                    "what makes one life more meaningful than another, and whether "
                    "meaning must be discovered in the world or created by the person "
                    "living the life."),
        "background": ("The question is ancient. Aristotle framed the good life around "
                       "eudaimonia, flourishing through virtuous activity. The Stoics "
                       "located meaning in living according to nature and reason; the "
                       "Epicureans in tranquil pleasure and friendship. In the modern "
                       "era, Tolstoy's Confession (1882) made the crisis of meaning a "
                       "personal emergency, while Camus framed it through the absurd: "
                       "the human hunger for meaning colliding with a silent world. "
                       "Contemporary analytic work, led by figures such as Susan Wolf, "
                       "treats meaningfulness as a distinct value - a life can be happy "
                       "and moral yet feel empty. No consensus answer exists, and the "
                       "question remains open whether 'meaning' names one thing or "
                       "several."),
        "why_it_matters": ("How people answer this question shapes education, work, "
                           "family life, and mental health. Societies that cannot give "
                           "a credible account of a meaningful life struggle with "
                           "despair, disengagement, and the sense that success is "
                           "hollow. A solved theory of meaning would guide everything "
                           "from career counseling to the design of a good old age."),
        "sig_lens": ("The Signature Resolution Method treats 'meaning' as a "
                     "scoreable record: enumerate the candidate meaning-sources, "
                     "weight them by the criteria a meaningful life must satisfy, "
                     "and publish the ranking with the weights visible."),
        "sig_pointer": ("The Signature approach scores the leading candidates - "
                        "relationships, achievement, experience, and service - against "
                        "four criteria: durability across a lifetime, independence "
                        "from luck, contribution beyond the self, and fit with the "
                        "person's own values. Service and relationships rank highest "
                        "under most weightings. See the Signature Edition record for "
                        "the full walkthrough and confirm/refute panel."),
        "sig_full": (
            SIG_LABEL + " Assumptions: (1) meaningfulness is a real, gradable "
            "property of lives, not just a feeling; (2) candidate sources can be "
            "compared on shared criteria; (3) the criteria themselves are "
            "defeasible and shown openly. Reasoning path: list the historically "
            "live candidates - relationships, achievement, experience, service, "
            "knowledge; fix four scoring criteria - durability, luck-independence, "
            "transpersonal contribution, and value-fit; run weighted rankings and "
            "watch which candidates survive weight changes. Proposed mechanism: a "
            "life is meaningful to the degree it realizes a weighted bundle of "
            "these goods, with relationships and service the most weight-stable "
            "winners - they score well under nearly every reasonable weighting, "
            "while pure achievement collapses when luck-independence is weighted "
            "highly. What would confirm it: longitudinal studies showing that "
            "lives rich in the top-ranked goods report stable meaning across "
            "decades and cultures, and that reweighting the criteria in public "
            "deliberation converges on the same ranking. What would kill it: "
            "evidence that the criteria themselves are parochial - for example, "
            "whole cultures for whom luck-independence is irrelevant to meaning, "
            "or that self-reported meaning tracks only mood and temperament, "
            "making the scorecard a mood meter. What it does NOT claim: it does "
            "not prove any one life meaningful, does not settle whether meaning "
            "is discovered or invented, and does not speak to any religious "
            "account - this is a secular, procedural proposal, one candidate "
            "resolution among others, offered for testing."),
        "key_points": [
            "Aristotle's eudaimonia: the good life as virtuous activity, not pleasure alone.",
            "The absurd (Camus): the clash between the hunger for meaning and a silent world.",
            "Meaningfulness as a distinct value (Wolf): a life can be happy yet meaningless.",
            "Subjectivist answers: meaning is created by the agent's own commitments.",
            "Objectivist answers: some pursuits are meaningful whether or not the agent endorses them.",
            "Hybrid answers: meaning needs both subjective attraction and objective worth.",
        ],
        "requirements": [
            "An account of what 'meaning' refers to - one property or a family.",
            "Criteria for comparing candidate sources of meaning.",
            "A verdict on the discovered-versus-created dispute.",
            "Cross-cultural evidence that the account is not parochial.",
        ],
        "standards": [
            "State candidate meaning-sources exactly before scoring them.",
            "Show the weighting assumptions; a ranking without visible weights proves nothing.",
            "Stress the winner against its strongest objection before publishing.",
        ],
        "citations": [CIT_ARISTOTLE_ETH, "Camus A. The Myth of Sisyphus. 1942 (O'Brien trans., Vintage, 1991).",
                      "Wolf S. Meaning in Life and Why It Matters. Princeton Univ. Press, 2010.",
                      "Tolstoy L. A Confession. 1882 (Maude trans., Oxford, 2010).", CIT_SEP],
    },
    # ---------------------------------------------------------- rank 2
    {
        "key": "why_be_moral",
        "name": "Why be moral? The amoralist's challenge",
        "group": "Foundations",
        "branch": "Ethics",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "problem": ("Why should anyone be moral when immorality would pay? Plato's "
                    "Ring of Gyges asks: if you could act unjustly with total "
                    "impunity, would justice still be rational? The challenge demands "
                    "a reason to be moral that does not secretly depend on getting "
                    "caught or on rewards."),
        "background": ("Glaucon poses the challenge in Plato's Republic: give a man "
                       "a ring of invisibility and watch whether he stays just. "
                       "Hobbes answered with the social contract - morality as the "
                       "price of escaping the war of all against all. Hume grounded "
                       "morals in sympathy, Kant in reason itself: the categorical "
                       "imperative binds any rational agent. Modern game theory "
                       "revived the debate: in iterated prisoner's dilemmas, "
                       "cooperation can be the winning strategy, but the one-shot "
                       "defector still profits. No answer has silenced the amoralist "
                       "who asks, one final time, 'but why should I care about that?'"),
        "why_it_matters": ("Every legal system, every code of conduct, and every "
                           "parent's lecture assumes there is an answer. If morality "
                           "has no rational grip on the clear-eyed egoist, then "
                           "moral education is manipulation and punishment is mere "
                           "power. A solved answer would settle what justifies "
                           "holding anyone to any standard."),
        "sig_lens": ("The Signature Resolution Method turns the challenge into a "
                     "payoff table: model the just and unjust life as strategies, "
                     "vary the detection probability, and find where the ranking "
                     "flips."),
        "sig_pointer": ("The Signature approach builds the Gyges payoff matrix: "
                        "unjust action wins only when detection stays near zero "
                        "across a whole lifetime, which no real agent can guarantee. "
                        "Under any realistic detection schedule, the just strategy "
                        "dominates on expected value. See the Signature Edition "
                        "record for the full walkthrough and confirm/refute panel."),
        "sig_full": (
            SIG_LABEL + " Assumptions: (1) the amoralist is a rational "
            "expected-value maximizer; (2) detection probabilities are never "
            "truly zero over a lifetime of actions; (3) the payoffs include "
            "reputation, trust access, and the cognitive cost of concealment. "
            "Reasoning path: formalize Glaucon's challenge as a repeated game; "
            "compute expected payoffs for just versus unjust strategies across "
            "detection probabilities from 0 to 1; locate the flip point; then "
            "ask what detection rate a real human life actually carries. Proposed "
            "mechanism: the ring is a fantasy of zero detection, and zero "
            "detection is not a stable assumption - leaks, witnesses, and the "
            "need to coordinate with others push real detection rates far above "
            "the flip threshold, so the 'rational egoist' who can do arithmetic "
            "chooses the just strategy as the higher-expected-value play, with "
            "no moral premise smuggled in. What would confirm it: behavioral "
            "data showing that perceived detection risk, not moral conviction, "
            "explains most compliance variance, and that defection rates track "
            "the model's flip threshold across domains. What would kill it: a "
            "demonstrated class of agents who defect for decades at near-zero "
            "detection with higher lifetime payoffs, or proof that the amoralist "
            "rejects expected-value reasoning itself - at which point the "
            "challenge was never about rationality. What it does NOT claim: it "
            "does not prove the unjust life is unhappy, does not refute the "
            "amoralist who abandons reason, and does not supply moral motivation "
            "to someone who simply does not care - it answers the rational "
            "version of the question, nothing more."),
        "key_points": [
            "The Ring of Gyges (Plato): impunity as the test of justice's value.",
            "Hobbes's contract: morality as the rational exit from the state of nature.",
            "Kant's answer: immorality is irrational because it cannot be universalized.",
            "Hume's answer: sympathy makes the moral life natural to us.",
            "Game theory: cooperation wins in iterated games; defection wins one-shot.",
            "The residual challenge: 'why be rational?' has no non-circular answer.",
        ],
        "requirements": [
            "A model of the amoralist as a rational agent with specified payoffs.",
            "Realistic lifetime detection probabilities, not fantasy zeros.",
            "A verdict on whether the answer needs moral premises.",
            "Behavioral evidence tying compliance to the model's parameters.",
        ],
        "standards": [
            "No moral premise may appear in the premises of the argument.",
            "The payoff table must be shown, not asserted.",
            "The flip threshold must be computed and compared with real rates.",
        ],
        "citations": [CIT_PLATO_REP, "Hobbes T. Leviathan. 1651 (Tuck ed., Cambridge, 1996).",
                      CIT_KANT_GROUND, "Axelrod R. The Evolution of Cooperation. Basic Books, 1984.",
                      CIT_SEP],
    },
    # ---------------------------------------------------------- rank 3
    {
        "key": "skepticism",
        "name": "Can we know the external world? The problem of skepticism",
        "group": "Foundations",
        "branch": "Epistemology",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "problem": ("How do you know you are not dreaming, deceived, or a brain in "
                    "a vat being fed perfect simulations? If every experience you "
                    "have is compatible with a skeptical scenario, what justifies "
                    "your belief in tables, chairs, and other people?"),
        "background": ("Descartes made the problem modern in 1641: an evil demon "
                       "could deceive him about everything except that he thinks. "
                       "Hume deepened it, showing that our belief in continuing "
                       "objects and in causation outruns any evidence. The 20th "
                       "century added the brain in a vat (Putnam, 1981) and the "
                       "simulation argument. Responses divide into Moorean "
                       "common-sense refutations ('here is one hand'), externalist "
                       "theories (knowledge needs no refutation of the skeptic), "
                       "and contextualism (the skeptic raises the standards "
                       "impossibly high). None has produced consensus."),
        "why_it_matters": ("Science, law, and everyday life all assume we can know "
                           "about a shared world. If skepticism wins, every claim "
                           "to knowledge collapses into mere seeming. A principled "
                           "answer would secure the foundations of every other "
                           "inquiry - or honestly admit they have none."),
        "sig_lens": ("The Signature Resolution Method scores anti-skeptical "
                     "strategies by a single test: which one lets inquiry continue "
                     "while conceding everything the skeptic actually proves?"),
        "sig_pointer": ("The Signature approach runs the Bayesian comparison: the "
                        "skeptical hypothesis predicts exactly the same experiences "
                        "as the ordinary one, so experience alone cannot separate "
                        "them - but prior probability and explanatory integration "
                        "can. The ordinary world wins on priors, not on proof. See "
                        "the Signature Edition record for the full walkthrough and "
                        "confirm/refute panel."),
        "sig_full": (
            SIG_LABEL + " Assumptions: (1) the skeptical scenario is "
            "constructed to predict identical experiences; (2) Bayesian "
            "priors over world-hypotheses are legitimate; (3) explanatory "
            "integration with the rest of inquiry counts as evidence. Reasoning "
            "path: formalize the contest as ordinary-world versus "
            "demon-simulation hypotheses; note the likelihoods are tied by "
            "construction; move the fight to the priors and to which hypothesis "
            "unifies with successful science; compute the posterior gap across "
            "a range of prior settings. Proposed mechanism: skepticism proves "
            "only that experience underdetermines the world-hypothesis - it "
            "does not prove the hypotheses are equally good, because "
            "equal likelihoods plus unequal priors plus unequal explanatory "
            "integration still yields a decisive posterior for the ordinary "
            "world; the skeptic's real achievement is a demand for certainty, "
            "and certainty was never the price of knowledge. What would confirm "
            "it: a formal result showing the posterior for the ordinary "
            "hypothesis stays above 0.99 across all non-gerrymandered priors, "
            "plus convergence of working scientists on externalist norms. What "
            "would kill it: a skeptical scenario with strictly greater "
            "explanatory power than the ordinary hypothesis, or a proof that "
            "priors over world-hypotheses are arbitrary - either would reopen "
            "the tie. What it does NOT claim: it does not refute the skeptic "
            "with certainty, does not dissolve the dream argument, and does "
            "not license dogmatism - it converts 'can we know?' from a demand "
            "for proof into a scored comparison, honestly labeled as a "
            "proposal."),
        "key_points": [
            "Descartes's evil demon: the founding modern skeptical scenario.",
            "The brain in a vat: perfect simulation is experientially indistinguishable.",
            "Moore's response: common sense as a legitimate starting point.",
            "Externalism: knowledge does not require refuting the skeptic.",
            "Contextualism: skeptical contexts raise standards ordinary life need not meet.",
            "The underdetermination core: identical experiences, rival hypotheses.",
        ],
        "requirements": [
            "A skeptical scenario stated precisely enough to compute with.",
            "A criterion for choosing between experientially identical hypotheses.",
            "An account of why certainty is or is not required for knowledge.",
            "Evidence that the criterion is not rigged for the ordinary world.",
        ],
        "standards": [
            "Concede everything the skeptic actually proves before answering.",
            "Show the likelihood tie explicitly; do not hand-wave it.",
            "Publish the prior assumptions; the answer stands or falls with them.",
        ],
        "citations": [CIT_DESCARTES_MED, "Putnam H. Reason, Truth and History. Cambridge Univ. Press, 1981.",
                      "Moore GE. 'Proof of an External World.' Proceedings of the British Academy 25, 1939.",
                      "Stroud B. The Significance of Philosophical Scepticism. Oxford Univ. Press, 1984.",
                      CIT_SEP],
    },
    # ---------------------------------------------------------- rank 4
    {
        "key": "free_will",
        "name": "Do we have free will? Determinism and choice",
        "group": "Foundations",
        "branch": "Metaphysics",
        "ladder_rank": 4,
        "ladder_tier": "foundations",
        "problem": ("If every event, including every human decision, is fixed by "
                    "prior causes and the laws of nature, can anyone genuinely "
                    "choose? And if physics leaves room through indeterminism, "
                    "does randomness give us freedom or just noise?"),
        "background": ("The Stoics wrestled with fate and responsibility; "
                       "Augustine and later theologians with foreknowledge. The "
                       "modern debate crystallized around the consequence "
                       "argument: if determinism is true, our acts are "
                       "consequences of the distant past, so we control nothing. "
                       "Compatibilists (Hume, and today Dennett) answer that "
                       "freedom means acting from your own desires without "
                       "coercion, which determinism permits. Libertarians "
                       "(Kane) demand genuine alternative possibilities; hard "
                       "determinists and impossibilists (Pereboom, Strawson) "
                       "conclude free will is an illusion. Neuroscience "
                       "experiments on readiness potentials added fuel without "
                       "settling anything."),
        "why_it_matters": ("Moral responsibility, praise, blame, punishment, and "
                           "the criminal law all presuppose that people could have "
                           "done otherwise - or at least something like it. If no "
                           "one is responsible, retributive justice collapses and "
                           "the meaning of regret changes. This is the metaphysical "
                           "problem with the most direct grip on daily life."),
        "sig_lens": ("The Signature Resolution Method scores the live positions "
                     "against the consequence argument's force and against what "
                     "responsibility actually needs, then keeps whichever "
                     "position loses least."),
        "sig_pointer": ("The Signature approach computes a control index across "
                        "scenarios: coerced action scores near zero, Frankfurt "
                        "cases (no alternatives, own reasons) score high, pure "
                        "randomness scores low. Compatibilism wins the scorecard "
                        "because responsibility needs authorship, not "
                        "could-have-done-otherwise. See the Signature Edition "
                        "record for the full walkthrough and confirm/refute panel."),
        "sig_full": (
            SIG_LABEL + " Assumptions: (1) 'free will' must earn its keep by "
            "grounding responsibility as actually practiced; (2) Frankfurt "
            "cases are valid test scenarios; (3) randomness is not control. "
            "Reasoning path: enumerate the positions - libertarianism, "
            "compatibilism, hard determinism, impossibilism; define a control "
            "index from three factors (reasons-responsiveness, absence of "
            "coercion, stability of character); score canonical scenarios; "
            "then ask which position best fits the scores. Proposed mechanism: "
            "the consequence argument proves we lack one specific thing - "
            "ultimate self-creation - but responsibility never needed that; it "
            "needs the agent's reasons to be the difference-maker in the "
            "causal chain, which the control index measures directly; "
            "compatibilism is therefore not a compromise but the position the "
            "measurements select, and libertarian 'could have done otherwise' "
            "turns out to be neither necessary nor, when cashed out as "
            "indeterminism, even desirable. What would confirm it: legal and "
            "moral practice converging on reasons-responsiveness as the "
            "responsibility criterion across cultures, and neuroscience "
            "showing deliberation genuinely modulates outcomes in the indexed "
            "way. What would kill it: a demonstration that ordinary blame "
            "conceptually requires ultimate origination - experimental "
            "philosophy showing the folk concept collapses without it - or a "
            "Frankfurt-case counterexample that survives scrutiny. What it "
            "does NOT claim: it does not prove determinism true or false, "
            "does not settle the physics, and does not tell any courtroom what "
            "to do - it is a scored proposal about which concept of freedom "
            "does the work, honestly labeled."),
        "key_points": [
            "The consequence argument: determinism plus the past leaves no room for control.",
            "Compatibilism: freedom is uncoerced action from your own character.",
            "Libertarianism: freedom needs genuine alternative possibilities.",
            "Frankfurt cases: responsibility without alternative possibilities.",
            "Hard determinism and impossibilism: free will is an illusion.",
            "The randomness horn: indeterminism gives luck, not freedom.",
        ],
        "requirements": [
            "A definition of the freedom that responsibility actually needs.",
            "A verdict on Frankfurt cases and the consequence argument.",
            "An account of why randomness does not help.",
            "Fit with experimental work on the folk concept of responsibility.",
        ],
        "standards": [
            "Score positions against responsibility practice, not intuitions alone.",
            "Keep determinism's truth-value separate from the conceptual question.",
            "Show the control index computation; no bare assertions.",
        ],
        "citations": [CIT_HUME_ENQUIRY, "Frankfurt H. 'Alternate Possibilities and Moral Responsibility.' Journal of Philosophy 66, 1969.",
                      "van Inwagen P. An Essay on Free Will. Oxford Univ. Press, 1983.",
                      "Dennett D. Freedom Evolves. Viking, 2003.",
                      "Kane R. The Significance of Free Will. Oxford Univ. Press, 1996.", CIT_SEP],
    },
    # ---------------------------------------------------------- rank 5
    {
        "key": "personal_identity",
        "name": "What is the self? Personal identity over time",
        "group": "Foundations",
        "branch": "Metaphysics",
        "ladder_rank": 5,
        "ladder_tier": "foundations",
        "problem": ("What makes you the same person as the child in your old "
                    "photographs? Your body has replaced nearly every cell, your "
                    "memories are partial, your character has changed - so what, "
                    "if anything, is the thread of identity across a lifetime?"),
        "background": ("Locke proposed memory: you are the same person as far as "
                       "consciousness extends backward. Reid objected with the "
                       "brave officer paradox - memory is intransitive while "
                       "identity must be transitive. The Ship of Theseus asks the "
                       "same question for objects: replace every plank, is it the "
                       "same ship? Hume, looking inward, found no self at all, "
                       "only a bundle of perceptions. Parfit's fission thought "
                       "experiments (teletransporter, split brains) pushed the "
                       "modern debate: perhaps identity is not what matters - "
                       "psychological continuity is. Animalists (Olson) answer "
                       "that you are simply the human animal."),
        "why_it_matters": ("Identity underwrites survival, prudential concern, "
                           "compensation, and punishment: it matters that the "
                           "person punished is the one who offended. Medical "
                           "ethics (advance directives, dementia), the prospect "
                           "of mind uploading, and cryonics all turn on which "
                           "theory is right. Get this wrong and you misidentify "
                           "who survives."),
        "sig_lens": ("The Signature Resolution Method models identity as a "
                     "continuity score over the memory chain and finds the "
                     "threshold where our practices of holding responsible "
                     "actually break."),
        "sig_pointer": ("The Signature approach computes psychological-overlap "
                        "scores across a lifetime chain: adjacent selves overlap "
                        "heavily while distant selves barely connect, exactly "
                        "Reid's paradox made quantitative. Parfit's conclusion "
                        "survives the numbers: what matters is continuity degree, "
                        "not all-or-nothing identity. See the Signature Edition "
                        "record for the full walkthrough and confirm/refute panel."),
        "sig_full": (
            SIG_LABEL + " Assumptions: (1) identity judgments in practice "
            "track psychological continuity; (2) continuity is gradable; (3) "
            "thought experiments are data about the concept. Reasoning path: "
            "build a chain of person-stages across a lifetime; compute "
            "pairwise memory-and-trait overlap; reproduce Reid's paradox as a "
            "measured intransitivity; run Parfit's fission cases through the "
            "same metric; then ask which theory best fits the measured "
            "pattern. Proposed mechanism: identity-over-time is not a further "
            "fact but the limiting behavior of a continuity score - Locke was "
            "measuring the right thing with the wrong logic (demanding "
            "transitivity of an intransitive relation), Hume was right that "
            "no extra self appears in the measurement, and Parfit was right "
            "that the score is what matters; the animalist gets the body "
            "cases right because bodily continuity correlates with the score, "
            "not because the animal is the metaphysical essence. What would "
            "confirm it: dementia and amnesia cases where responsibility "
            "attributions track measured continuity rather than bodily "
            "identity, and cross-cultural stability of the threshold where "
            "people stop holding the later self responsible. What would kill "
            "it: fission cases where confident identity judgments contradict "
            "the continuity score, or evidence that folk identity judgments "
            "track something the score ignores, like the soul or the bare "
            "body. What it does NOT claim: it does not prove there is no "
            "self, does not settle whether uploading preserves you, and does "
            "not license any medical decision - it is a measured proposal "
            "about what our identity concept tracks, honestly labeled."),
        "key_points": [
            "Locke's memory criterion: sameness of person follows sameness of consciousness.",
            "Reid's brave officer: memory is intransitive, identity must be transitive.",
            "The Ship of Theseus: gradual replacement and the identity of artifacts.",
            "Hume's bundle: introspection finds perceptions, never a self.",
            "Parfit's fission: identity may not be what matters; continuity is.",
            "Animalism: you are the human organism, full stop.",
        ],
        "requirements": [
            "A treatment of Reid's transitivity objection.",
            "A verdict on fission and teletransportation cases.",
            "An account of what matters for survival and responsibility.",
            "Fit with amnesia, dementia, and split-brain evidence.",
        ],
        "standards": [
            "Thought experiments must be run as measurements, not anecdotes.",
            "Keep the conceptual question separate from the empirical one.",
            "Show the overlap computation; publish the threshold.",
        ],
        "citations": [CIT_LOCKE_ESSAY, CIT_HUME_TREATISE, CIT_PARFIT_RP,
                      "Olson E. The Human Animal. Oxford Univ. Press, 1997.",
                      "Shoemaker S. 'Persons and Their Pasts.' American Philosophical Quarterly 7, 1970.", CIT_SEP],
    },
    # ---------------------------------------------------------- rank 6
    {
        "key": "other_minds",
        "name": "How do we know what others feel? The problem of other minds",
        "group": "Foundations",
        "branch": "Epistemology",
        "ladder_rank": 6,
        "ladder_tier": "foundations",
        "problem": ("You know your own pain directly, from the inside. But you "
                    "never experience anyone else's. What justifies your belief "
                    "that other people have minds at all - that they are not "
                    "elaborate, mindless machines behaving as if they feel?"),
        "background": ("The problem is implicit in Descartes and explicit by "
                       "the 19th century. Mill offered the argument from "
                       "analogy: others behave as I do when I feel, so they "
                       "probably feel too. Behaviorists tried to dissolve it: "
                       "mental talk just is talk about behavior. Contemporary "
                       "debate runs between theory-theory (we infer minds with "
                       "a folk theory), simulation theory (we model others by "
                       "running our own minds offline), and direct-perception "
                       "accounts. The rise of AI has sharpened the stakes: if "
                       "behavior underdetermines mindedness, the chatbot "
                       "question is this problem wearing new clothes."),
        "why_it_matters": ("Our entire moral and social world assumes others "
                           "are conscious subjects, not philosophical zombies. "
                           "Law, friendship, and the wrongness of cruelty all "
                           "presuppose it. And the AI era forces the question "
                           "practically: which systems, if any, deserve the "
                           "moral consideration we give to minded beings?"),
        "sig_lens": ("The Signature Resolution Method scores the rival "
                     "hypotheses - other minds versus zombie-world - as "
                     "competing explanations of observed behavior, and checks "
                     "which one a rational inquirer must pick."),
        "sig_pointer": ("The Signature approach runs inference to the best "
                        "explanation: the other-minds hypothesis predicts the "
                        "fine-grained, novel, context-sensitive behavior we "
                        "actually observe, while the zombie hypothesis must "
                        "stipulate it case by case. Explanatory power, not "
                        "analogy, carries the justification. See the Signature "
                        "Edition record for the full walkthrough and "
                        "confirm/refute panel."),
        "sig_full": (
            SIG_LABEL + " Assumptions: (1) inference to the best explanation "
            "is a legitimate form of justification; (2) the zombie hypothesis "
            "is the serious rival, not a straw man; (3) behavioral evidence "
            "includes novel, unscripted responses. Reasoning path: list the "
            "candidate explanations of human behavior - genuine minds, "
            "zombies, divine puppetry; score each on prediction of novel "
            "behavior, simplicity, and integration with biology; compute the "
            "explanatory gap the zombie view must fill with brute "
            "stipulation. Proposed mechanism: the argument from analogy was "
            "always the weak version - the strong version is abductive: "
            "mindedness is the only hypothesis that predicts the open-ended "
            "creativity of observed behavior without one ad hoc stipulation "
            "per act, and the zombie hypothesis collapses under its own "
            "stipulation debt; the same scorecard then applies, unchanged, to "
            "AI systems, which is why it cannot be dismissed as "
            "question-begging. What would confirm it: a formal measure of "
            "stipulation debt that ranks the hypotheses identically across "
            "independent raters, and successful prediction of where our "
            "mind-attributions break down (infants, animals, machines). What "
            "would kill it: a zombie-model that predicts novel human behavior "
            "as well as the mentalistic model with equal simplicity - or a "
            "demonstration that abduction itself is unjustified, which would "
            "take science down with philosophy. What it does NOT claim: it "
            "does not prove any particular being is conscious, does not "
            "settle the AI consciousness question, and does not refute "
            "solipsism with certainty - it is a scored explanatory proposal, "
            "honestly labeled."),
        "key_points": [
            "The argument from analogy (Mill): similar behavior, similar minds.",
            "The zombie hypothesis: perfect behavior with no inner life.",
            "Behaviorism: dissolving the problem by redefining the mental.",
            "Theory-theory versus simulation theory in developmental psychology.",
            "The AI sharpening: behavior underdetermines mindedness for machines too.",
            "Direct perception: we see emotions in faces, not infer them.",
        ],
        "requirements": [
            "A rival hypothesis stated strongly enough to be a real threat.",
            "A form of justification beyond first-person analogy.",
            "An account that extends to infants, animals, and AI systems.",
            "A reason the justification is not circular.",
        ],
        "standards": [
            "Score explanations, not anecdotes; count the stipulations.",
            "Keep the epistemic question separate from the metaphysical one.",
            "The scorecard must apply to AI without special pleading.",
        ],
        "citations": ["Mill JS. An Examination of Sir William Hamilton's Philosophy. 1865, ch. 12.",
                      "Ryle G. The Concept of Mind. Hutchinson, 1949.",
                      "Goldman A. Simulating Minds. Oxford Univ. Press, 2006.",
                      "Chalmers DJ. The Conscious Mind. Oxford Univ. Press, 1996, ch. 1.", CIT_SEP],
    },
    # ---------------------------------------------------------- rank 7
    {
        "key": "nature_of_truth",
        "name": "What is truth?",
        "group": "Foundations",
        "branch": "Logic",
        "ladder_rank": 7,
        "ladder_tier": "foundations",
        "problem": ("What does it mean to call a sentence true? Is truth a "
                    "match between words and world, coherence among beliefs, "
                    "successful practice - or is 'true' just a handy device "
                    "with no deep nature at all?"),
        "background": ("Aristotle gave the classic formula: to say of what is "
                       "that it is, is true. The correspondence theory dominated "
                       "for two millennia. The 19th and 20th centuries added "
                       "rivals: coherence (truth as mutual support among "
                       "beliefs), pragmatism (truth as what works in inquiry), "
                       "and deflationism (Frege, Ramsey, and later Horwich: "
                       "'true' adds nothing to the sentence itself). Tarski's "
                       "semantic theory of truth (1933) gave formal precision "
                       "to correspondence for formalized languages but left "
                       "the philosophical question open. The debate is "
                       "entirely unresolved."),
        "why_it_matters": ("Every inquiry aims at truth, and every disagreement "
                           "presupposes it. If truth has no nature, then "
                           "'seeking the truth' is a slogan without content; "
                           "if it does, the nature we find dictates what "
                           "counts as success in science, history, and "
                           "journalism. Misinformation debates are applied "
                           "theories of truth."),
        "sig_lens": ("The Signature Resolution Method tests the theories "
                     "against a fixed battery of sentences and scores which "
                     "theory classifies them the way working inquiry does."),
        "sig_pointer": ("The Signature approach scores correspondence, "
                        "coherence, pragmatist, and deflationist theories on a "
                        "toy battery of sentences: correspondence wins on "
                        "ordinary empirical sentences, deflationism wins on "
                        "economy, and none wins everywhere - the scorecard "
                        "suggests pluralism about truth's nature. See the "
                        "Signature Edition record for the full walkthrough and "
                        "confirm/refute panel."),
        "sig_full": (
            SIG_LABEL + " Assumptions: (1) a theory of truth must handle "
            "ordinary empirical sentences first; (2) classification accuracy "
            "against working inquiry is the test; (3) theoretical economy "
            "counts but does not decide alone. Reasoning path: fix a battery "
            "of test sentences - empirical, mathematical, moral, self-"
            "referential; run each theory across the battery; score hits, "
            "misses, and ad hoc maneuvers; then ask whether any single "
            "theory sweeps the board. Proposed mechanism: the measurement "
            "selects a qualified pluralism - correspondence earns its keep "
            "for sentences answerable to observation, deflationism earns its "
            "keep as the logic of the truth-predicate itself, and the "
            "monist theories each pay for their imperialism with epicycles "
            "(coherence with the isolated-system objection, pragmatism with "
            "the 'useful but false' cases); truth has no single nature "
            "because 'true' does different jobs in different domains, and "
            "the scorecard shows exactly where each job description fits. "
            "What would confirm it: independent classification tasks where "
            "raters converge on domain-specific truth criteria, and formal "
            "results showing no monist theory covers the battery without "
            "epicycles. What would kill it: a single unified theory that "
            "sweeps the battery cleanly, or evidence that the battery "
            "sentences are not really in one family - either would collapse "
            "the pluralist reading. What it does NOT claim: it does not "
            "prove pluralism true, does not dissolve the liar paradox (see "
            "its own record), and does not license relativism about "
            "empirical fact - the correspondence scores for ordinary "
            "sentences are the anchor, honestly labeled as a proposal."),
        "key_points": [
            "Correspondence: truth as agreement with reality (Aristotle, Tarski).",
            "Coherence: truth as mutual support within a belief system.",
            "Pragmatism: truth as the end of successful inquiry.",
            "Deflationism: 'is true' is a logical device, not a deep property.",
            "Tarski's T-schema: 'snow is white' is true iff snow is white.",
            "Pluralism: different domains may need different truth properties.",
        ],
        "requirements": [
            "A test battery covering empirical, formal, and evaluative sentences.",
            "A scoring rule applied uniformly to all theories.",
            "An account of the liar paradox's interaction with each theory.",
            "A verdict on monism versus pluralism.",
        ],
        "standards": [
            "Theories must be scored on identical sentences.",
            "Count the epicycles; elegance is evidence.",
            "Publish the battery so others can re-run the test.",
        ],
        "citations": [CIT_ARISTOTLE_META, "Tarski A. 'The Concept of Truth in Formalized Languages.' 1933 (in Logic, Semantics, Metamathematics, Oxford, 1956).",
                      "Horwich P. Truth. 2nd ed., Oxford Univ. Press, 1998.",
                      "James W. Pragmatism. 1907 (Kuklick ed., Hackett, 1981).", CIT_SEP],
    },
    # ---------------------------------------------------------- rank 8
    {
        "key": "liar_paradox",
        "name": "The liar paradox",
        "group": "Foundations",
        "branch": "Logic",
        "ladder_rank": 8,
        "ladder_tier": "foundations",
        "problem": ("Consider the sentence: 'This sentence is false.' If it is "
                    "true, then what it says holds, so it is false. If it is "
                    "false, then what it says fails, so it is true. Either "
                    "way leads to contradiction. What is wrong - with the "
                    "sentence, with truth, or with logic itself?"),
        "background": ("The paradox is ancient - attributed to Eubulides of "
                       "Miletus in the 4th century BCE. Medieval logicians "
                       "built whole theories of insolubles around it. Tarski "
                       "used it to argue that no sufficiently rich language "
                       "can contain its own truth predicate, motivating his "
                       "hierarchy of object-language and metalanguage. Kripke's "
                       "1975 theory of truth offered a fixed-point construction "
                       "where the liar gets no stable truth value. Paracomplete, "
                       "paraconsistent, revision-theoretic, and contextualist "
                       "solutions all have defenders today. The paradox "
                       "remains unsolved in the sense that no solution "
                       "commands consensus."),
        "why_it_matters": ("The liar is the stress test of our concepts of "
                           "truth and logic. Any theory of truth must survive "
                           "it, and the solutions on offer - banning "
                           "self-reference, tolerating gaps or gluts, "
                           "revising logic - each carry heavy costs. Computer "
                           "science meets it too: self-referential sentences "
                           "are cousins of the halting problem and Godel "
                           "sentences."),
        "sig_lens": ("The Signature Resolution Method runs the fixed-point "
                     "iteration on a small sentence set and watches the liar "
                     "oscillate, then scores which repair costs least."),
        "sig_pointer": ("The Signature approach iterates truth-value "
                        "assignments: ordinary sentences settle, the liar "
                        "oscillates forever - the computation itself diagnoses "
                        "the disease. Of the repairs, the paracomplete option "
                        "(truth-value gaps) costs least on the scorecard. See "
                        "the Signature Edition record for the full walkthrough "
                        "and confirm/refute panel."),
        "sig_full": (
            SIG_LABEL + " Assumptions: (1) classical bivalence is the "
            "default to beat; (2) a solution's cost is measured in "
            "sentences it must exile or logics it must revise; (3) Kripke's "
            "fixed-point construction is the honest laboratory. Reasoning "
            "path: implement the fixed-point iteration over a sentence set "
            "containing the liar; observe grounded sentences settle while "
            "the liar oscillates; then score the four repair families - "
            "Tarskian hierarchy, paracomplete gaps, paraconsistent gluts, "
            "revision theory - by expressive cost. Proposed mechanism: the "
            "iteration shows the liar is ungrounded rather than "
            "contradictory, which selects the paracomplete diagnosis - the "
            "sentence is neither true nor false - as the cheapest repair, "
            "since it revises bivalence locally while the hierarchy exiles "
            "whole classes of natural sentences and paraconsistency risks "
            "explosion management across all of logic. What would confirm "
            "it: natural-language data showing speakers comfortably withhold "
            "truth-value judgments for ungrounded sentences, and formal "
            "results extending the fixed-point treatment to the revenge "
            "liars ('this sentence is not true'). What would kill it: a "
            "revenge paradox that defeats gap solutions without ad hoc "
            "patching, or a hierarchy solution that recovers natural "
            "self-reference at acceptable cost. What it does NOT claim: it "
            "does not prove the liar is meaningless, does not settle the "
            "revenge problems, and does not revise logic beyond the local "
            "gap - it is a scored diagnosis, honestly labeled as a "
            "proposal."),
        "key_points": [
            "Eubulides's original: self-referential falsity as contradiction.",
            "Tarski's hierarchy: no language contains its own truth predicate.",
            "Kripke's fixed points: the liar as ungrounded, not contradictory.",
            "Paracomplete: truth-value gaps - neither true nor false.",
            "Paraconsistent: truth-value gluts - both true and false.",
            "Revenge liars: strengthened paradoxes targeting each solution.",
        ],
        "requirements": [
            "A formal model in which the oscillation is demonstrated.",
            "A cost accounting for each repair family.",
            "A treatment of revenge paradoxes.",
            "Fit with ordinary speakers' judgments about the sentence.",
        ],
        "standards": [
            "Run the iteration; do not argue from intuition alone.",
            "Count what each solution exiles or revises.",
            "Revenge cases must be faced, not footnoted.",
        ],
        "citations": ["Tarski A. 'The Concept of Truth in Formalized Languages.' 1933.",
                      "Kripke S. 'Outline of a Theory of Truth.' Journal of Philosophy 72, 1975.",
                      "Priest G. In Contradiction. 2nd ed., Oxford Univ. Press, 2006.",
                      "Beall JC (ed.). Revenge of the Liar. Oxford Univ. Press, 2007.", CIT_SEP],
    },
    # ---------------------------------------------------------- rank 9
    {
        "key": "zeno_paradoxes",
        "name": "Zeno's paradoxes: is motion an illusion?",
        "group": "Foundations",
        "branch": "Metaphysics",
        "ladder_rank": 9,
        "ladder_tier": "foundations",
        "problem": ("To cross a room you must first cross half, then half of "
                    "the remainder, and so on through infinitely many steps. "
                    "How can infinitely many tasks be completed in finite "
                    "time? Zeno's paradoxes argue that motion, plurality, "
                    "and change are impossible."),
        "background": ("Zeno of Elea, defending Parmenides's monism around 450 "
                       "BCE, offered the dichotomy, Achilles and the tortoise, "
                       "the arrow, and the stadium. Aristotle answered with "
                       "the potential-versus-actual infinite distinction. The "
                       "calculus (Newton, Leibniz) gave the dichotomy a "
                       "mathematical answer: the infinite series 1/2 + 1/4 + "
                       "... converges to 1. But philosophers note the "
                       "mathematics answers how far, not how the infinity of "
                       "tasks is performed - Thomson's lamp and supertask "
                       "literature keep the metaphysical question alive, as "
                       "do quantum-gravity speculations about discrete "
                       "spacetime."),
        "why_it_matters": ("The paradoxes are the founding puzzles of infinity, "
                           "continuity, and the structure of space and time. "
                           "Every theory of the continuum - and every physics "
                           "of spacetime - must answer Zeno. Supertasks also "
                           "matter for the philosophy of computation: what "
                           "can be done in finite time bounds what machines "
                           "can compute."),
        "sig_lens": ("The Signature Resolution Method separates the paradox "
                     "into its mathematical half and its metaphysical half, "
                     "settles the first by summation, and scores answers to "
                     "the second."),
        "sig_pointer": ("The Signature approach computes the partial sums: "
                        "1/2 + 1/4 + ... converges to exactly 1, settling the "
                        "'how far' half. The remaining 'how so many tasks' "
                        "half is scored across answers, with the "
                        "potential-infinite reading winning on cost. See the "
                        "Signature Edition record for the full walkthrough "
                        "and confirm/refute panel."),
        "sig_full": (
            SIG_LABEL + " Assumptions: (1) the mathematical and "
            "metaphysical halves are separable; (2) convergent series are "
            "legitimate completions; (3) a solution must address all four "
            "paradoxes, not just the dichotomy. Reasoning path: sum the "
            "dichotomy series to its limit and verify the Achilles series "
            "converges likewise; formalize the residual worry as the "
            "completion of infinitely many distinct tasks; score the "
            "candidate answers - Aristotelian potential infinity, "
            "atomism/discrete spacetime, supertask finitism. Proposed "
            "mechanism: the series summation dissolves the quantitative "
            "paradox completely, and the residual metaphysical worry rests "
            "on treating 'tasks' as countably performed acts rather than "
            "as a continuous motion divisible at will - Aristotle's "
            "distinction, rehabilitated: the divisions are potential until "
            "we make them, so no infinity of actual tasks is ever "
            "performed. What would confirm it: physics confirming a "
            "continuous spacetime down to all probed scales, and the "
            "supertask literature converging on the potential-infinite "
            "diagnosis. What would kill it: empirical evidence of discrete "
            "spacetime (which would hand the win to atomism instead), or a "
            "Thomson-lamp-style case showing the potential/actual "
            "distinction cannot handle supertasks. What it does NOT claim: "
            "it does not prove spacetime continuous, does not refute "
            "Parmenides's deeper monism, and does not settle whether "
            "actual infinities exist - it is a scored dissolution of the "
            "motion paradoxes, honestly labeled."),
        "key_points": [
            "The dichotomy: infinitely many halvings before any journey ends.",
            "Achilles and the tortoise: the pursuer never catches the pursued.",
            "The arrow: at each instant the arrow is at rest, so motion is impossible.",
            "Aristotle's answer: the potential versus the actual infinite.",
            "The calculus answer: convergent infinite series have finite sums.",
            "Supertasks: Thomson's lamp and the metaphysics of completed infinities.",
        ],
        "requirements": [
            "The convergent sums computed, not asserted.",
            "All four paradoxes addressed, not just the dichotomy.",
            "A verdict on potential versus actual infinity.",
            "Consistency with current physics of spacetime.",
        ],
        "standards": [
            "Separate the mathematical half from the metaphysical half.",
            "Show the partial sums converging in the demonstration.",
            "Cost each residual answer explicitly.",
        ],
        "citations": [CIT_ARISTOTLE_META, "Salmon W (ed.). Zeno's Paradoxes. Hackett, 2001.",
                      "Huggett N. Space from Zeno to Einstein. MIT Press, 1999.",
                      "Thomson JF. 'Tasks and Super-Tasks.' Analysis 15, 1954.", CIT_SEP],
    },
    # ---------------------------------------------------------- rank 10
    {
        "key": "sorites_paradox",
        "name": "The sorites paradox: vagueness and the heap",
        "group": "Foundations",
        "branch": "Logic",
        "ladder_rank": 10,
        "ladder_tier": "foundations",
        "problem": ("One grain of sand is not a heap. Adding one grain to a "
                    "non-heap cannot make it a heap. By repetition, no number "
                    "of grains ever makes a heap - yet heaps plainly exist. "
                    "Where does the logic break, and what is vagueness?"),
        "background": ("The paradox (soros, Greek for heap) is attributed to "
                       "Eubulides, 4th century BCE. It generalizes: baldness, "
                       "tallness, redness - most ordinary predicates are "
                       "vague. Classical responses: epistemicism (Williamson) "
                       "says there is a sharp cutoff we cannot know; "
                       "supervaluationism says vague sentences are true if "
                       "true on all precisifications; degree theories (fuzzy "
                       "logic) give truth values between 0 and 1; "
                       "contextualism makes the cutoff shift with use. "
                       "Vagueness infects law ('reasonable doubt'), science "
                       "(species boundaries), and AI classification."),
        "why_it_matters": ("Vague predicates run ordinary language and much of "
                           "law and policy. Any logic adequate to natural "
                           "language must handle them, and any AI that "
                           "classifies the world - medical diagnosis, content "
                           "moderation - must decide where to cut. The paradox "
                           "is the doorway to the logic of the vague."),
        "sig_lens": ("The Signature Resolution Method sweeps the cutoff "
                     "across the grain counts and measures which theory "
                     "predicts speakers' actual judgments."),
        "sig_pointer": ("The Signature approach runs the threshold sweep: "
                        "epistemicism posits an unknowable sharp line, "
                        "fuzzy logic a graded zone, supervaluationism a "
                        "truth-value gap. The graded-plus-gap hybrid scores "
                        "best against judgment data. See the Signature Edition "
                        "record for the full walkthrough and confirm/refute "
                        "panel."),
        "sig_full": (
            SIG_LABEL + " Assumptions: (1) speaker judgments about "
            "borderline cases are data; (2) a theory of vagueness must "
            "preserve classical logic where vagueness is absent; (3) "
            "tolerance principles drive the paradox. Reasoning path: "
            "generate the sorites series from 1 to 10,000 grains; apply "
            "each theory's verdict function; compare against the "
            "empirical pattern - clear non-heap, clear heap, and a "
            "penumbral zone of hesitation; score by fit and by logical "
            "cost. Proposed mechanism: the measurement favors a hybrid - "
            "degrees of truth across the transition zone (capturing the "
            "hesitation gradient) with truth-value gaps at the exact "
            "penumbral core (capturing the 'no fact of the matter' "
            "judgments); pure epistemicism pays for its sharp line with "
            "an unknowable metaphysics, and pure supervaluationism "
            "struggles with the gradient data. What would confirm it: "
            "psycholinguistic studies showing graded confidence tracking "
            "the fuzzy curve and gap-like refusal at the core, stable "
            "across predicates. What would kill it: evidence that "
            "borderline judgments are really hidden sharp-line knowledge "
            "(vindicating epistemicism) or that the gradient is an "
            "artifact of task framing. What it does NOT claim: it does "
            "not prove vagueness is in the world rather than the words, "
            "does not solve higher-order vagueness (vagueness about where "
            "the penumbra lies), and does not rewrite logic wholesale - "
            "it is a scored hybrid proposal, honestly labeled."),
        "key_points": [
            "The tolerance premise: one grain cannot make the difference.",
            "Epistemicism: sharp cutoffs exist but are unknowable.",
            "Supervaluationism: truth on all precisifications; gaps elsewhere.",
            "Degree theory: truth comes in grades between 0 and 1.",
            "Higher-order vagueness: the penumbra's own boundaries are vague.",
            "Applications: law, species concepts, AI classification thresholds.",
        ],
        "requirements": [
            "The tolerance premise stated in a form that generates the series.",
            "A verdict function for each theory across the series.",
            "Fit with speaker judgments in borderline cases.",
            "A treatment of higher-order vagueness.",
        ],
        "standards": [
            "Sweep the whole series; no cherry-picked cutoffs.",
            "Cost each theory's logical revisions explicitly.",
            "Theories must face the judgment data, not just the logic.",
        ],
        "citations": ["Williamson T. Vagueness. Routledge, 1994.",
                      "Fine K. 'Vagueness, Truth and Logic.' Synthese 30, 1975.",
                      "Keefe R. Theories of Vagueness. Cambridge Univ. Press, 2000.",
                      "Smith NJJ. Vagueness and Degrees of Truth. Oxford Univ. Press, 2008.", CIT_SEP],
    },
    # ---------------------------------------------------------- rank 11
    {
        "key": "beauty_objectivity",
        "name": "What is beauty? Aesthetic objectivity",
        "group": "Foundations",
        "branch": "Aesthetics",
        "ladder_rank": 11,
        "ladder_tier": "foundations",
        "problem": ("Is beauty in the object or in the eye of the beholder? "
                    "When people disagree about whether something is "
                    "beautiful, is one of them wrong - or is aesthetic "
                    "judgment purely a matter of taste, with no right "
                    "answers?"),
        "background": ("Plato treated beauty as a Form, objective and "
                       "eternal. Hume argued in 'Of the Standard of Taste' "
                       "(1757) that beauty is sentiment, yet some critics "
                       "judge better than others - the 'true judges.' Kant's "
                       "Critique of Judgment (1790) made aesthetic judgment "
                       "subjective but universally demanding: we speak as if "
                       "beauty were in the object. Modern experimental "
                       "aesthetics finds surprising cross-cultural agreement "
                       "on faces and landscapes, alongside deep disagreement "
                       "on art. The objectivity question remains open."),
        "why_it_matters": ("Aesthetic judgment guides architecture, design, "
                           "conservation, and arts funding - all of which "
                           "spend public money on the claim that some things "
                           "are genuinely more beautiful. If there are no "
                           "aesthetic facts, criticism is autobiography; if "
                           "there are, we need to know how to find them."),
        "sig_lens": ("The Signature Resolution Method measures actual "
                     "agreement rates across domains and asks which theory "
                     "of beauty predicts the measured pattern."),
        "sig_pointer": ("The Signature approach simulates inter-rater "
                        "agreement: high convergence on natural scenes and "
                        "faces, low on avant-garde art - exactly the pattern "
                        "a two-factor theory (evolved perceptual biases plus "
                        "cultural learning) predicts. See the Signature "
                        "Edition record for the full walkthrough and "
                        "confirm/refute panel."),
        "sig_full": (
            SIG_LABEL + " Assumptions: (1) agreement rates are data about "
            "the judgment, not proof of objectivity; (2) objectivity comes "
            "in degrees across domains; (3) evolutionary and cultural "
            "factors are both real. Reasoning path: model raters with a "
            "shared perceptual-bias component and an idiosyncratic "
            "cultural component; vary their weights by domain; compute "
            "predicted agreement; compare with the empirical pattern of "
            "high agreement on nature, moderate on craft, low on the "
            "avant-garde. Proposed mechanism: beauty judgments are "
            "objective to the degree the shared component dominates - "
            "faces and landscapes tap widely shared perceptual machinery, "
            "so disagreement there is error-like, while avant-garde art "
            "taps the cultural component, so disagreement there is "
            "taste-like; Hume's true judges are simply raters with "
            "well-calibrated shared components, and Kant's universal "
            "voice is the phenomenology of the shared component speaking. "
            "What would confirm it: agreement studies decomposing into "
            "the two factors as predicted, and training that moves "
            "judges' ratings toward the shared-component consensus. What "
            "would kill it: domains where agreement is high but no "
            "shared mechanism exists, or proof that the 'shared "
            "component' is itself culturally constructed all the way "
            "down. What it does NOT claim: it does not prove any "
            "particular thing beautiful, does not reduce beauty to "
            "biology, and does not settle whether aesthetic value is "
            "real - it is a scored two-factor proposal, honestly labeled."),
        "key_points": [
            "Plato: beauty as an objective Form.",
            "Hume: beauty as sentiment, with true judges as the standard.",
            "Kant: subjective judgment that demands universal agreement.",
            "Cross-cultural agreement on faces and landscapes.",
            "Deep, persistent disagreement on contemporary art.",
            "The two-factor view: shared perception plus cultural learning.",
        ],
        "requirements": [
            "Measured agreement rates across aesthetic domains.",
            "A theory predicting the high-low agreement pattern.",
            "An account of expertise and the 'true judge.'",
            "A verdict on whether any aesthetic judgments are objectively right.",
        ],
        "standards": [
            "Agreement data first; metaphysics second.",
            "The theory must predict where disagreement is legitimate.",
            "Keep the judgment's phenomenology in the explanandum.",
        ],
        "citations": ["Hume D. 'Of the Standard of Taste.' 1757 (in Essays Moral, Political, and Literary).",
                      "Kant I. Critique of the Power of Judgment. 1790 (Guyer/Matthews trans., Cambridge, 2000).",
                      "Plato. Symposium. c. 385 BCE (Nehamas/Woodruff trans., Hackett, 1989).",
                      "Schellekens E, Goldie P (eds.). The Aesthetic Mind. Oxford Univ. Press, 2011.", CIT_SEP],
    },
    # ---------------------------------------------------------- rank 12
    {
        "key": "what_is_art",
        "name": "What is art?",
        "group": "Compounded",
        "branch": "Aesthetics",
        "ladder_rank": 12,
        "ladder_tier": "compounded",
        "problem": ("What makes something a work of art? A painted canvas and a "
                    "plumber's wrench can be physically similar, yet one hangs in "
                    "a museum and the other does not. Is there a definition of "
                    "art - or does the concept resist definition entirely?"),
        "background": ("Traditional definitions appealed to representation, "
                       "expression, or aesthetic experience, but 20th-century "
                       "art - Duchamp's readymades, Warhol's Brillo boxes, "
                       "conceptual art - broke every one. Weitz (1956) argued "
                       "art is an 'open concept,' indefinable by nature. "
                       "Dickie's institutional theory answered: art is what "
                       "the artworld confers status upon. Neo-Wittgensteinians "
                       "offer cluster accounts: a family of criteria, none "
                       "necessary. Danto argued art ended as a progressive "
                       "narrative while artworks continue. No definition "
                       "commands consensus."),
        "why_it_matters": ("Museums, courts (obscenity and copyright cases), "
                           "and funding bodies constantly decide what counts "
                           "as art, with money and liberty at stake. A "
                           "principled account would guide curation, "
                           "education, and the law; the absence of one "
                           "leaves the decisions to power and fashion."),
        "sig_lens": ("The Signature Resolution Method scores candidate "
                     "definitions against hard cases - readymades, forgeries, "
                     "AI outputs - and keeps the account that misclassifies "
                     "least."),
        "sig_pointer": ("The Signature approach builds the hard-case battery: "
                        "Duchamp's Fountain, a perfect forgery, an AI image. "
                        "No single-criterion definition survives; the weighted "
                        "cluster account misclassifies least. See the "
                        "Signature Edition record for the full walkthrough "
                        "and confirm/refute panel."),
        "sig_full": (
            SIG_LABEL + " Assumptions: (1) hard cases are data, not "
            "counterexamples to be defined away; (2) a definition's cost is "
            "measured in misclassifications of settled cases; (3) the "
            "artworld's judgments are evidence, not verdicts. Reasoning "
            "path: fix the battery - paradigm paintings, readymades, "
            "forgeries, AI outputs, natural beauties; run each candidate "
            "definition - mimetic, expression, aesthetic, institutional, "
            "historical, cluster - across the battery; count hits, misses, "
            "and ad hoc patches. Proposed mechanism: the scoring selects a "
            "weighted cluster account with an institutional-historical core - "
            "arthood is a matter of satisfying enough of the family "
            "(intended for regard, embedded in art-historical practice, "
            "affording aesthetic experience) with the weights learned from "
            "settled cases; single-criterion theories each die on one hard "
            "case, while the cluster survives all of them at the price of "
            "borderline indeterminacy, which the sorites record shows is "
            "honest rather than shameful. What would confirm it: the "
            "learned weights predicting fresh hard cases (new AI-art "
            "controversies) better than any single-criterion rival, and "
            "convergence of the weights across independent calibrations. "
            "What would kill it: a single-criterion definition that sweeps "
            "the battery without patches, or evidence that the 'settled "
            "cases' are themselves artifacts of institutional power rather "
            "than data. What it does NOT claim: it does not prove any "
            "particular object is art, does not end the definition debate "
            "by fiat, and does not rank artworks - it is a scored "
            "classification proposal, honestly labeled."),
        "key_points": [
            "The readymade challenge: Fountain broke representation and craft criteria.",
            "Weitz's open concept: art as logically indefinable.",
            "The institutional theory: art status conferred by the artworld.",
            "Danto: the end of art's progressive narrative.",
            "Cluster accounts: family resemblance among criteria, none necessary.",
            "The forgery problem: indiscernible objects, different art status.",
        ],
        "requirements": [
            "A hard-case battery including readymades, forgeries, and AI outputs.",
            "Uniform scoring of each candidate definition.",
            "A verdict on definability itself.",
            "An account of borderline cases that does not cheat.",
        ],
        "standards": [
            "Hard cases count as data; definitions may not define them away.",
            "Count misclassifications and patches for every theory.",
            "Publish the battery and the learned weights.",
        ],
        "citations": ["Weitz M. 'The Role of Theory in Aesthetics.' Journal of Aesthetics and Art Criticism 15, 1956.",
                      "Dickie G. Art and the Aesthetic. Cornell Univ. Press, 1974.",
                      "Danto A. The Transfiguration of the Commonplace. Harvard Univ. Press, 1981.",
                      "Gaut B. 'Art as a Cluster Concept.' In Theories of Art Today (Carroll ed., Wisconsin, 2000).", CIT_SEP],
    },
    # ---------------------------------------------------------- rank 13
    {
        "key": "what_is_justice",
        "name": "What is justice?",
        "group": "Compounded",
        "branch": "Political Philosophy",
        "ladder_rank": 13,
        "ladder_tier": "compounded",
        "problem": ("What makes a distribution of goods, opportunities, and "
                    "burdens just? Is justice strict equality, distribution "
                    "by need, by merit, by liberty - or is the question "
                    "itself misframed?"),
        "background": ("Plato's Republic made justice the harmony of the "
                       "soul and the city. Aristotle tied it to treating "
                       "equals equally. The modern debate was reset by Rawls "
                       "(1971): justice as fairness, chosen behind a veil of "
                       "ignorance, yielding equal liberties and the "
                       "difference principle. Nozick (1974) answered with "
                       "entitlement theory: justice is historical, not "
                       "patterned - taxation of earnings is forced labor. "
                       "Capabilities theorists (Sen, Nussbaum), luck "
                       "egalitarians, and sufficientarians all press rival "
                       "patterns. Fifty years on, the field has positions, "
                       "not a victor."),
        "why_it_matters": ("Tax codes, welfare systems, affirmative action, "
                           "and global aid all presuppose an answer. "
                           "Political argument without a theory of justice "
                           "is bargaining; with a false one, it is "
                           "systematic wrong. This is the most applied of "
                           "the unsolved problems."),
        "sig_lens": ("The Signature Resolution Method runs the veil of "
                     "ignorance as a computed choice problem and checks "
                     "which principle rational agents actually select."),
        "sig_pointer": ("The Signature approach computes maximin choices "
                        "behind the veil: across a range of risk attitudes, "
                        "agents converge on protecting the worst-off - the "
                        "difference principle survives as the robust winner. "
                        "See the Signature Edition record for the full "
                        "walkthrough and confirm/refute panel."),
        "sig_full": (
            SIG_LABEL + " Assumptions: (1) the veil of ignorance is a "
            "valid modeling device; (2) agents behind the veil know general "
            "social science but not their place; (3) risk attitudes may "
            "vary and must be modeled. Reasoning path: construct societies "
            "as income-and-liberty distributions; place simulated agents "
            "behind the veil with varying risk aversion; compute each "
            "agent's preferred principle - strict equality, maximin, "
            "utilitarian sum, libertarian entitlement; measure convergence. "
            "Proposed mechanism: the computation vindicates Rawls's core "
            "insight while disciplining it - maximin (the difference "
            "principle) is the robust choice across most risk profiles, "
            "but extreme risk-seekers defect to utilitarianism and "
            "Nozick's historical objection survives as a constraint: the "
            "chosen pattern must be implementable without continuous "
            "liberty violations, which trims the difference principle "
            "into a 'sustainable maximin' with a liberty floor. What would "
            "confirm it: experimental veil-of-ignorance studies showing "
            "real subjects converging on sustainable maximin, and "
            "institutional histories where maximin-constrained systems "
            "outperform on stability. What would kill it: veil experiments "
            "where subjects knowingly choose utilitarian gambles at scale, "
            "or a proof that no patterned principle is implementable "
            "without unacceptable coercion - which would hand the debate "
            "back to Nozick. What it does NOT claim: it does not prove "
            "Rawls right, does not license any specific tax rate, and "
            "does not dissolve the liberty-equality tension - it is a "
            "computed, revisable proposal, honestly labeled."),
        "key_points": [
            "Plato: justice as harmony of parts in soul and city.",
            "Rawls: justice as fairness behind the veil of ignorance.",
            "The difference principle: inequalities must benefit the worst off.",
            "Nozick: justice as historical entitlement, not patterned distribution.",
            "Luck egalitarianism: neutralize brute luck, respect option luck.",
            "Capabilities: justice as real freedoms to achieve functionings.",
        ],
        "requirements": [
            "A modeling of the veil-of-ignorance choice with varying risk attitudes.",
            "A verdict on patterned versus historical principles.",
            "An implementability constraint from the liberty objection.",
            "Experimental and historical evidence for the predicted convergence.",
        ],
        "standards": [
            "Compute the choice; do not stipulate it.",
            "Vary the risk attitudes; robustness is the test.",
            "Face Nozick's objection as a constraint, not a footnote.",
        ],
        "citations": [CIT_PLATO_REP, CIT_RAWLS_TJ, CIT_NOZICK_ASU,
                      "Sen A. The Idea of Justice. Harvard Univ. Press, 2009.",
                      "Nussbaum M. Creating Capabilities. Harvard Univ. Press, 2011.", CIT_SEP],
    },
    # ---------------------------------------------------------- rank 14
    {
        "key": "justify_state",
        "name": "What justifies the state? Political obligation",
        "group": "Compounded",
        "branch": "Political Philosophy",
        "ladder_rank": 14,
        "ladder_tier": "compounded",
        "problem": ("Why should anyone obey the law? The state claims "
                    "authority over people who never consented to it, "
                    "backed by force. Philosophical anarchists argue no "
                    "state is legitimate. What, if anything, justifies "
                    "political authority?"),
        "background": ("Social contract theory (Hobbes, Locke, Rousseau) "
                       "grounded authority in consent - but actual consent "
                       "is nowhere found, and tacit consent by residence "
                       "looks like the highwayman's 'your money or your "
                       "life.' Hume already mocked the contract as fiction. "
                       "Later justifications: fair play (benefits accepted "
                       "create obligations), natural duty (a duty to "
                       "support just institutions), gratitude, and "
                       "consequentialist necessity. Simmons's influential "
                       "critique argued every justification fails, leaving "
                       "philosophical anarchism the honest position. The "
                       "problem is unsolved."),
        "why_it_matters": ("Taxation, conscription, and punishment all rest "
                           "on claimed authority. If no state is legitimate, "
                           "then law enforcement is organized coercion and "
                           "civic obedience needs a new foundation. Every "
                           "theory of legitimate government stands or falls "
                           "here."),
        "sig_lens": ("The Signature Resolution Method prices the state's "
                     "offer - benefits received versus exit costs - and "
                     "finds the consent threshold where obligation becomes "
                     "rational."),
        "sig_pointer": ("The Signature approach models membership as a "
                        "contract with exit costs: where benefits clearly "
                        "exceed the costs of exit, continued residence "
                        "functions as economic consent. The anarchist wins "
                        "only where exit is priced out of reach. See the "
                        "Signature Edition record for the full walkthrough "
                        "and confirm/refute panel."),
        "sig_full": (
            SIG_LABEL + " Assumptions: (1) obligation can be grounded in "
            "rational acceptance, not only express consent; (2) benefits "
            "and exit costs are measurable in principle; (3) the anarchist "
            "critique is answered case by case, not in general. Reasoning "
            "path: model the citizen-state relation as an iterated "
            "contract; compute net benefit (public goods, coordination, "
            "security minus taxes and compliance) against realistic exit "
            "costs (emigration, statelessness); locate the threshold where "
            "remaining is rationally endorsable; test the anarchist's "
            "hard cases - the poor, the immobile, the dissenter. Proposed "
            "mechanism: legitimacy is scalar, not binary - states earn "
            "obligation to the degree that (benefits minus burdens) exceed "
            "exit costs for the actual citizen, which vindicates fair-play "
            "and natural-duty justifications for well-ordered states while "
            "conceding the anarchist's point for extractive regimes where "
            "exit is priced out of reach; 'tacit consent' is replaced by "
            "'rational non-exit,' a measurable relation. What would "
            "confirm it: migration and compliance data tracking the "
            "computed threshold - rising exit where net benefit turns "
            "negative, stable obligation where it stays positive. What "
            "would kill it: evidence that obligation judgments track "
            "nothing like cost-benefit - pure habit or pure force - or a "
            "demonstration that 'rational non-exit' smuggles in the very "
            "consent fiction it replaces. What it does NOT claim: it does "
            "not legitimize any actual state, does not refute anarchism "
            "for the worst regimes, and does not turn residence into a "
            "signature on a contract - it is a scalar, testable proposal, "
            "honestly labeled."),
        "key_points": [
            "The consent problem: no one signed the social contract.",
            "Hume's highwayman objection to tacit consent.",
            "Fair play: accepting benefits creates obligations of contribution.",
            "Natural duty: a duty to support just institutions.",
            "Simmons's critique: every justification fails; anarchism wins.",
            "Scalar legitimacy: authority as a matter of degree.",
        ],
        "requirements": [
            "A measurable model of benefits, burdens, and exit costs.",
            "A threshold where obligation becomes rationally endorsable.",
            "The anarchist's hard cases answered, not dismissed.",
            "Fit with migration and compliance data.",
        ],
        "standards": [
            "Replace consent fiction with a measurable relation.",
            "Legitimacy must be scalar; binary verdicts are suspect.",
            "The worst regimes must come out illegitimate on the model.",
        ],
        "citations": ["Hobbes T. Leviathan. 1651.", CIT_LOCKE_ESSAY,
                      "Simmons AJ. Moral Principles and Political Obligations. Princeton Univ. Press, 1979.",
                      "Huemer M. The Problem of Political Authority. Palgrave, 2013.",
                      "Rousseau JJ. The Social Contract. 1762 (Gourevitch trans., Cambridge, 1997).", CIT_SEP],
    },
    # ---------------------------------------------------------- rank 15
    {
        "key": "simulation_hypothesis",
        "name": "Are we living in a simulation?",
        "group": "Compounded",
        "branch": "Metaphysics",
        "ladder_rank": 15,
        "ladder_tier": "compounded",
        "problem": ("If a civilization can run detailed simulations of its "
                    "ancestors, simulated minds could vastly outnumber real "
                    "ones. Should you then believe you are probably "
                    "simulated? The simulation argument turns cosmology into "
                    "a question about your own reality."),
        "background": ("Bostrom's 2003 paper formalized the trilemma: either "
                       "civilizations never reach simulation maturity, or "
                       "they choose not to run many simulations, or we are "
                       "almost certainly simulated. The argument assumes "
                       "substrate independence - that consciousness can run "
                       "on silicon. Critics object that the counting is "
                       "illegitimate, that simulations would be detectable "
                       "or too costly, or that the argument proves too much. "
                       "Physicists have proposed empirical tests (cosmic-ray "
                       "cutoffs suggesting a lattice), all inconclusive. "
                       "The metaphysical question stands."),
        "why_it_matters": ("If the argument works, it reframes everything: "
                           "cosmology studies the simulator's code, and "
                           "existential risk includes simulator shutdown. If "
                           "it fails, its failure teaches us about "
                           "probability, consciousness, and what counts as "
                           "evidence. Either way, the stakes are total."),
        "sig_lens": ("The Signature Resolution Method computes the "
                     "simulation probability under each trilemma branch and "
                     "checks which branch survives contact with the "
                     "assumptions it needs."),
        "sig_pointer": ("The Signature approach runs Bostrom's trilemma as "
                        "a probability tree: the 'we are simulated' branch "
                        "dominates only if ancestor-simulations are cheap, "
                        "numerous, and conscious - three assumptions, each "
                        "load-bearing and each contested. See the Signature "
                        "Edition record for the full walkthrough and "
                        "confirm/refute panel."),
        "sig_full": (
            SIG_LABEL + " Assumptions: (1) the trilemma's disjunction is "
            "exhaustive; (2) probabilities over the branches can be "
            "estimated; (3) substrate independence is treated as an "
            "assumption, not a result. Reasoning path: formalize the three "
            "branches; assign the simulation count per branch; compute "
            "P(simulated) conditional on each branch surviving; then "
            "stress each load-bearing assumption - cheapness (computational "
            "cost of conscious simulation), numerousness (motivations to "
            "run ancestor simulations), consciousness (substrate "
            "independence). Proposed mechanism: the probability mass "
            "collapses onto the first two branches once the assumptions "
            "are priced - running even one conscious ancestor-simulation "
            "may cost a planetary energy budget, and posthuman motives are "
            "unknowable, so the 'almost certainly simulated' conclusion "
            "holds only inside a narrow, optimistic parameter box; outside "
            "it, the honest answer is radical uncertainty distributed "
            "across the trilemma, not a high simulation probability. What "
            "would confirm it: physics establishing the computational "
            "cost floor for conscious simulation, or empirical lattice "
            "signatures in cosmic rays. What would kill it: a demonstrated "
            "cheap substrate for consciousness, or a rigorous defense of "
            "the indifference principle applied across the branches. What "
            "it does NOT claim: it does not prove we are not simulated, "
            "does not refute substrate independence, and does not assign "
            "a final probability - it maps the assumption-space honestly, "
            "as a proposal."),
        "key_points": [
            "Bostrom's trilemma: extinction, abstention, or simulation.",
            "Substrate independence: the assumption that mind runs on any hardware.",
            "The counting objection: are simulated observers countable this way?",
            "Empirical tests: lattice signatures in cosmic rays.",
            "The motivation problem: why would posthumans run ancestor simulations?",
            "Relation to skepticism: the vat argument with a budget.",
        ],
        "requirements": [
            "The trilemma formalized as a probability tree.",
            "Each load-bearing assumption priced and stressed.",
            "A verdict conditional on assumption sets, not a bare probability.",
            "Consistency with the problem of other minds and skepticism.",
        ],
        "standards": [
            "No probability without stated assumptions.",
            "The 'almost certainly' claim must survive the cost floor.",
            "Keep the metaphysical question separate from the empirical tests.",
        ],
        "citations": [CIT_BOSTROM_SIM,
                      "Chalmers DJ. 'The Matrix as Metaphysics.' 2003 (in Philosophy and The Matrix, Grau ed.).",
                      "Beane SR et al. 'Constraints on the Universe as a Numerical Simulation.' EPJ A 50, 2014.",
                      "Bostrom N, Kulczycki M. 'A Patch for the Simulation Argument.' Analysis 71, 2011.", CIT_SEP],
    },
    # ---------------------------------------------------------- rank 16
    {
        "key": "ethics_of_belief",
        "name": "Is it wrong to believe without evidence? The ethics of belief",
        "group": "Compounded",
        "branch": "Epistemology",
        "ladder_rank": 16,
        "ladder_tier": "compounded",
        "problem": ("Clifford declared it 'wrong always, everywhere, and for "
                    "anyone, to believe anything upon insufficient evidence.' "
                    "James replied that in forced, momentous options, we may "
                    "- must - believe beyond the evidence. Is there a moral "
                    "duty governing what we believe, or is belief outside "
                    "morality's jurisdiction?"),
        "background": ("Clifford's 1877 essay 'The Ethics of Belief' used the "
                       "shipowner who lets an unseaworthy ship sail: the "
                       "belief, not just the act, is culpable. James's 'The "
                       "Will to Believe' (1896) defended passional belief "
                       "where evidence is silent but decision cannot wait - "
                       "including religious and personal commitments. The "
                       "modern debate asks whether belief is voluntary enough "
                       "to be morally assessable (doxastic voluntarism), "
                       "whether false beliefs harm the shared information "
                       "environment, and how the ethics of belief applies to "
                       "the misinformation age. No consensus principle "
                       "exists."),
        "why_it_matters": ("Misinformation, conspiracy theories, and science "
                           "denial are applied ethics of belief. If Clifford "
                           "is right, sharing unevidenced claims is a moral "
                           "wrong, not just an intellectual vice - which "
                           "would reshape norms for media, platforms, and "
                           "citizens. If James is right, the duty has "
                           " principled limits we need to draw."),
        "sig_lens": ("The Signature Resolution Method computes the expected "
                     "epistemic and social utility of Clifford's rule versus "
                     "James's permission, and finds the boundary between "
                     "them."),
        "sig_pointer": ("The Signature approach models belief policies: "
                        "Clifford's strict rule wins on social epistemic "
                        "utility where beliefs propagate, James's permission "
                        "wins where the option is forced, private, and "
                        "momentous. The boundary is propagation risk. See "
                        "the Signature Edition record for the full "
                        "walkthrough and confirm/refute panel."),
        "sig_full": (
            SIG_LABEL + " Assumptions: (1) beliefs have social "
            "externalities; (2) some beliefs are action-guiding and "
            "propagating, others private; (3) expected-utility comparison "
            "of belief policies is legitimate. Reasoning path: define two "
            "policies - Clifford-strict (believe only on sufficient "
            "evidence) and James-permissive (believe on passional grounds "
            "in forced options); simulate populations adopting each; "
            "measure truth-convergence and decision quality; then vary the "
            "propagation factor. Proposed mechanism: the computation "
            "dissolves the standoff by relativizing to propagation - "
            "Clifford's duty binds beliefs that enter the shared "
            "environment (testimony, publication, voting), where "
            "unevidenced belief predictably degrades the commons, while "
            "James's permission holds for genuinely private, forced, "
            "momentous options where the belief changes nothing but the "
            "believer's own capacity to act; the shipowner was wrong "
            "because his belief sailed a ship, not because believing is "
            "intrinsically immoral. What would confirm it: misinformation "
            "studies showing belief-propagation as the harm vector, and "
            "cases where private passional belief measurably enables "
            "action without epistemic cost. What would kill it: evidence "
            "that private beliefs inevitably leak into the commons (no "
            "truly private belief), or that Clifford-strict populations "
            "paralyze on forced decisions - either would collapse the "
            "boundary. What it does NOT claim: it does not prove belief "
            "is voluntary, does not settle any religious question, and "
            "does not license believing comforting falsehoods - it is a "
            "scored boundary proposal, honestly labeled."),
        "key_points": [
            "Clifford's principle: belief on insufficient evidence is always wrong.",
            "The shipowner: culpable belief before the culpable act.",
            "James's will to believe: forced, momentous, undecidable options.",
            "Doxastic voluntarism: is belief voluntary enough for moral judgment?",
            "The social harm argument: false beliefs poison the information commons.",
            "Application: misinformation norms for the platform age.",
        ],
        "requirements": [
            "A model comparing Clifford-strict and James-permissive policies.",
            "The propagation factor varied explicitly.",
            "A principled boundary, not a compromise slogan.",
            "Fit with misinformation and science-denial evidence.",
        ],
        "standards": [
            "Relativize the duty; absolute verdicts have failed for 150 years.",
            "Show the crossover computation.",
            "Keep the voluntarism question separate from the policy question.",
        ],
        "citations": ["Clifford WK. 'The Ethics of Belief.' Contemporary Review, 1877.",
                      "James W. 'The Will to Believe.' 1896 (in The Will to Believe and Other Essays).",
                      "Adler J. 'Faith and Fanaticism.' In The Ethics of Belief (Adler & Elgin eds., MIT, 2002).",
                      "Nottelmann N. Blameworthy Belief. Springer, 2007.", CIT_SEP],
    },
    # ---------------------------------------------------------- rank 17
    {
        "key": "problem_of_induction",
        "name": "The problem of induction",
        "group": "Compounded",
        "branch": "Epistemology",
        "ladder_rank": 17,
        "ladder_tier": "compounded",
        "problem": ("The sun has risen every day, so it will rise tomorrow - "
                    "but why? Any argument that the future resembles the "
                    "past seems to assume the very uniformity it tries to "
                    "prove. Hume's problem: there is no non-circular "
                    "justification for inductive inference, yet all science "
                    "and daily life depend on it."),
        "background": ("Hume's Enquiry (1748) posed it: causal and inductive "
                       "inference cannot be founded on reason (any such "
                       "argument begs the question) nor on experience "
                       "(experience is the thing in question) - it is "
                       "custom, habit. Responses: Reichenbach's pragmatic "
                       "vindication (induction is the best bet if any bet "
                       "works), Popper's denial that science uses induction "
                       "at all, Strawson's dissolution (asking to justify "
                       "induction misunderstands justification), Bayesian "
                       "treatments via priors, and Goodman's new riddle "
                       "(grue) showing the problem is also about which "
                       "regularities to project. Unsolved after nearly three "
                       "centuries."),
        "why_it_matters": ("Every scientific prediction, every engineering "
                           "tolerance, every expectation about tomorrow is "
                           "inductive. If induction is unjustifiable, the "
                           "rationality of science is an open wound. Machine "
                           "learning has made it practical: generalization "
                           "from training data is induction, and its "
                           "justification is a live engineering question."),
        "sig_lens": ("The Signature Resolution Method treats induction as a "
                     "betting policy, scores the policies on simulated "
                     "worlds, and checks whether any policy dominates."),
        "sig_pointer": ("The Signature approach runs Laplace's rule of "
                        "succession on toy histories and compares betting "
                        "policies across uniform and chaotic worlds: "
                        "induction dominates exactly where learning is "
                        "possible at all - Reichenbach vindicated by "
                        "computation. See the Signature Edition record for "
                        "the full walkthrough and confirm/refute panel."),
        "sig_full": (
            SIG_LABEL + " Assumptions: (1) justification can be pragmatic "
            "rather than deductive; (2) simulated worlds fairly sample the "
            "space of possibilities; (3) Goodman's riddle is handled by "
            "projectibility priors. Reasoning path: define betting policies "
            "- naive induction, skepticism (never bet), randomness; run "
            "them on uniform worlds, chaotic worlds, and grue-worlds; "
            "measure cumulative accuracy; identify the dominance pattern. "
            "Proposed mechanism: the computation vindicates Reichenbach - "
            "induction is not justified as true but as dominant: in any "
            "world where any policy can learn, induction learns at least "
            "as fast, and in worlds where induction fails, no policy "
            "succeeds, so the skeptic gains nothing by abstaining; "
            "Goodman's grue is absorbed by projectibility priors that "
            "penalize gerrymandered predicates, which the Bayesian "
            "machinery already prices. What would confirm it: formal "
            "no-free-lunch results aligning with the simulation pattern, "
            "and machine-learning theory converging on the same dominance "
            "structure. What would kill it: a world-model where a "
            "non-inductive policy systematically beats induction, or a "
            "demonstration that pragmatic vindication smuggles in the "
            "uniformity it claims to avoid. What it does NOT claim: it "
            "does not prove the sun will rise, does not refute Hume's "
            "logical point (which stands), and does not justify any "
            "particular prior - it converts justification from proof to "
            "dominance, as a labeled proposal."),
        "key_points": [
            "Hume's fork: induction founded on neither reason nor experience.",
            "The circularity: any defense of uniformity assumes uniformity.",
            "Reichenbach's vindication: induction as the dominant betting policy.",
            "Popper's denial: science conjectures and refutes; it never induces.",
            "Goodman's grue: the problem of which regularities to project.",
            "Bayesian induction: priors plus evidence as the modern machinery.",
        ],
        "requirements": [
            "Betting policies defined and run on multiple world types.",
            "The dominance pattern demonstrated, not asserted.",
            "Goodman's riddle addressed via projectibility.",
            "Hume's logical point conceded, not evaded.",
        ],
        "standards": [
            "Concede the circularity; answer with dominance, not proof.",
            "Simulate hostile worlds, not just friendly ones.",
            "Price the priors; grue lives or dies there.",
        ],
        "citations": [CIT_HUME_ENQUIRY, "Reichenbach H. Experience and Prediction. Univ. of Chicago Press, 1938.",
                      CIT_POPPER_LOGIC, "Goodman N. Fact, Fiction, and Forecast. Harvard Univ. Press, 1955.",
                      "Strawson PF. Introduction to Logical Theory. Methuen, 1952.", CIT_SEP],
    },
    # ---------------------------------------------------------- rank 18
    {
        "key": "is_ought_gap",
        "name": "The is-ought gap",
        "group": "Compounded",
        "branch": "Ethics",
        "ladder_rank": 18,
        "ladder_tier": "compounded",
        "problem": ("Hume observed that moral writers slide from 'is' to "
                    "'ought' without explanation: from descriptions of how "
                    "things are to prescriptions of how they should be. Can "
                    "any 'ought' ever be validly derived from 'is' premises "
                    "alone - or is there an unbridgeable logical gap?"),
        "background": ("The famous passage sits in Hume's Treatise (1739), "
                       "Book III. It became a cornerstone of logical "
                       "positivism's fact/value distinction and of "
                       "non-cognitivism: moral language expresses attitudes, "
                       "not facts. Challengers: Searle's derivation of "
                       "'ought' from institutional 'is' (promising), "
                       "Foot's naturalism (oughts grounded in human needs), "
                       "and contemporary moral naturalists who argue moral "
                       "facts just are certain natural facts. The logical "
                       "question - whether the derivation is ever valid - "
                       "remains contested."),
        "why_it_matters": ("If the gap is unbridgeable, then science can "
                           "never settle a moral question, and policy "
                           "debates cannot be resolved by data alone. If it "
                           "is bridgeable, moral knowledge might be as "
                           "objective as physics. Every 'studies show, "
                           "therefore we should' argument stands on this "
                           "ground."),
        "sig_lens": ("The Signature Resolution Method builds the smallest "
                     "models where an ought-conclusion is attempted from "
                     "is-premises, and checks whether any derivation is "
                     "valid without a hidden ought."),
        "sig_pointer": ("The Signature approach runs truth-table checks on "
                        "toy derivations: every apparently successful "
                        "is-to-ought inference smuggles an evaluative "
                        "premise - Searle's promising case included. The "
                        "gap holds as a logical thesis; the action is in "
                        "which evaluative premises are defensible. See the "
                        "Signature Edition record for the full walkthrough "
                        "and confirm/refute panel."),
        "sig_full": (
            SIG_LABEL + " Assumptions: (1) deductive validity is the "
            "test; (2) institutional facts (promises, money, law) count as "
            "'is' premises for the test; (3) hidden premises must be "
            "exposed, not stipulated away. Reasoning path: formalize the "
            "candidate derivations - the naive slide, Searle's promising "
            "case, Foot's naturalist case - as premise sets; search for "
            "countermodels where all is-premises hold and the ought-"
            "conclusion fails; expose the evaluative premise each "
            "derivation needs. Proposed mechanism: the search vindicates "
            "Hume's logical thesis - every valid derivation needs at "
            "least one evaluative premise, and Searle's case needs 'one "
            "ought to keep promises' hiding inside the institution - but "
            "repositions the philosophical action: the gap is a constraint "
            "on argument form, not a proof that values are unreal; the "
            "live question becomes which evaluative premises are "
            "rationally non-optional (Foot's needs-based candidates score "
            "best), and the gap tells us exactly where to look. What would "
            "confirm it: the countermodel search generalizing - no "
            "counterexample-free derivation found across systematic "
            "enumeration - plus convergence on a small set of defensible "
            "evaluative premises. What would kill it: a single valid "
            "derivation with purely descriptive premises surviving the "
            "countermodel search, or a proof that the evaluative/defining "
            "distinction collapses. What it does NOT claim: it does not "
            "prove moral anti-realism, does not show values are unreal, "
            "and does not forbid science from informing ethics - it "
            "defends the logical thesis and relocates the debate, as a "
            "labeled proposal."),
        "key_points": [
            "Hume's passage: the unexplained slide from 'is' to 'ought.'",
            "The fact/value distinction in positivism and non-cognitivism.",
            "Searle's challenge: deriving 'ought' from promising.",
            "Foot's naturalism: oughts grounded in human life and needs.",
            "Moral naturalism: moral facts as a subset of natural facts.",
            "The autonomy of ethics: the thesis that ethics needs no foundation in nature.",
        ],
        "requirements": [
            "Candidate derivations formalized as premise sets.",
            "Countermodel search across the candidates.",
            "Hidden evaluative premises exposed explicitly.",
            "A verdict separating the logical thesis from metaethical morals.",
        ],
        "standards": [
            "Validity is the test; persuasiveness is not.",
            "Expose hidden premises; never stipulate them away.",
            "Keep the logical gap distinct from the reality of values.",
        ],
        "citations": [CIT_HUME_TREATISE, "Searle JR. 'How to Derive Ought from Is.' Philosophical Review 73, 1964.",
                      "Foot P. Natural Goodness. Oxford Univ. Press, 2001.",
                      "Prior AN. Logic and the Basis of Ethics. Oxford Univ. Press, 1949.", CIT_SEP],
    },
    # ---------------------------------------------------------- rank 19
    {
        "key": "moral_realism",
        "name": "Are there moral facts? Moral realism and its critics",
        "group": "Compounded",
        "branch": "Ethics",
        "ladder_rank": 19,
        "ladder_tier": "compounded",
        "problem": ("When we say 'torturing the innocent is wrong,' do we "
                    "state a fact - the way 'water is H2O' states a fact - "
                    "or do we merely express an attitude, like 'boo to "
                    "torture'? Are there moral facts independent of what "
                    "anyone thinks?"),
        "background": ("Moral realism claims moral judgments can be true, "
                       "mind-independently. Its rivals: emotivism and "
                       "expressivism (moral talk expresses attitudes), "
                       "error theory (Mackie: all moral claims are false "
                       "because they presuppose queer, non-natural facts), "
                       "and constructivism (moral truth is constructed by "
                       "rational agents). Mackie's 'argument from queerness' "
                       "and the persistent disagreement argument are the "
                       "classic objections; Cornell realists and "
                       "non-naturalists (Shafer-Landau, Parfit) lead the "
                       "defense. Metaethics remains deadlocked."),
        "why_it_matters": ("If there are no moral facts, moral argument is "
                           "ultimately persuasion, and moral progress is an "
                           "illusion. If there are, then getting ethics "
                           "right is a cognitive achievement like getting "
                           "physics right - and moral education is teaching "
                           "truth, not taste."),
        "sig_lens": ("The Signature Resolution Method scores the positions "
                     "on the disagreement data: which metaethics best "
                     "predicts the actual pattern of moral convergence and "
                     "divergence?"),
        "sig_pointer": ("The Signature approach measures moral disagreement "
                        "across issues: convergence is high on core harms, "
                        "low on contested cases - the pattern a realist "
                        "predicts if moral facts are sparse but real. Error "
                        "theory over-predicts chaos; expressivism "
                        "under-predicts convergence. See the Signature "
                        "Edition record for the full walkthrough and "
                        "confirm/refute panel."),
        "sig_full": (
            SIG_LABEL + " Assumptions: (1) the pattern of moral "
            "disagreement is data; (2) each metaethical theory predicts a "
            "disagreement profile; (3) convergence on core harms is real "
            "and cross-cultural. Reasoning path: catalog moral issues by "
            "observed disagreement level - core harms (murder, torture of "
            "the innocent), contested cases (abortion, distributive "
            "shares), framework disputes; derive each theory's predicted "
            "profile - realism predicts convergence where facts are clear, "
            "error theory predicts no more convergence than chance, "
            "expressivism predicts convergence tracking shared attitudes "
            "only; score against the catalog. Proposed mechanism: the "
            "measurement favors a sparse realism - a small core of "
            "mind-independent moral facts (about basic harms and fairness) "
            "explains the convergence floor that expressivism cannot "
            "predict and error theory must dismiss as coincidence, while "
            "the wide disagreement elsewhere is exactly what sparse "
            "realism predicts for underdetermined regions; Mackie's "
            "queerness objection is answered by locating the core facts "
            "in natural properties of suffering and cooperation, not "
            "spooky non-naturals. What would confirm it: the convergence "
            "floor holding across isolated cultures and the natural-"
            "property reduction surviving scrutiny. What would kill it: "
            "demonstration that core-harm convergence is fully explained "
            "by shared evolutionary attitudes (vindicating expressivism), "
            "or a successful error-theoretic debunking of the convergence "
            "as coincidence. What it does NOT claim: it does not prove "
            "any contested moral claim true, does not derive the full "
            "moral law from nature, and does not refute expressivism "
            "about evaluative language generally - it is a scored "
            "profile-matching proposal, honestly labeled."),
        "key_points": [
            "Realism: moral judgments state mind-independent facts.",
            "Expressivism: moral talk expresses attitudes, not beliefs.",
            "Error theory (Mackie): moral claims presuppose queer facts; all are false.",
            "The argument from queerness: moral facts would be metaphysically strange.",
            "The disagreement argument: persistent disagreement suggests no facts.",
            "Constructivism: moral truth built by idealized rational agents.",
        ],
        "requirements": [
            "A disagreement catalog with measured convergence levels.",
            "Each theory's predicted disagreement profile derived in advance.",
            "The convergence floor explained, not dismissed.",
            "A naturalistic location for the core moral facts.",
        ],
        "standards": [
            "Predict the profile before scoring it.",
            "Convergence is data; theories must predict it or explain it away.",
            "Keep the core/contested distinction explicit throughout.",
        ],
        "citations": ["Mackie JL. Ethics: Inventing Right and Wrong. Penguin, 1977.",
                      "Shafer-Landau R. Moral Realism: A Defence. Oxford Univ. Press, 2003.",
                      "Blackburn S. Spreading the Word. Oxford Univ. Press, 1984.",
                      "Parfit D. On What Matters. Oxford Univ. Press, 2011.", CIT_SEP],
    },
    # ---------------------------------------------------------- rank 20
    {
        "key": "moral_luck",
        "name": "Moral luck: can luck make us blameworthy?",
        "group": "Compounded",
        "branch": "Ethics",
        "ladder_rank": 20,
        "ladder_tier": "compounded",
        "problem": ("Two drivers run the same red light with equal "
                    "recklessness; one hits a child who darts out, the other "
                    "hits nothing. We blame the first more - but the "
                    "difference was pure luck. How can luck affect moral "
                    "responsibility if morality is about what we control?"),
        "background": ("Nagel (1979) and Williams (1981) named the problem: "
                       "the Kantian ideal says morality must be immune to "
                       "luck, yet our practices of blame track outcomes "
                       "relentlessly - resultant luck, circumstantial luck "
                       "(the luck of the situation you face), constitutive "
                       "luck (the luck of who you are). Responses: accept "
                       "moral luck and revise the control principle (Nagel), "
                       "deny it and reform blame (many Kantians), or split "
                       "blame into grades (Moore). The tension between the "
                       "control principle and actual practice is unresolved."),
        "why_it_matters": ("Criminal law grades offenses by outcome - "
                           "attempted versus completed murder - embedding "
                           "moral luck in punishment. Tort law, insurance, "
                           "and professional discipline do the same. If "
                           "moral luck is incoherent, vast institutions need "
                           "redesign; if it is real, the Kantian picture of "
                           "morality must fall."),
        "sig_lens": ("The Signature Resolution Method measures how blame "
                     "actually varies with outcome luck, then scores which "
                     "theory of responsibility predicts the measured "
                     "gradient."),
        "sig_pointer": ("The Signature approach computes blame across "
                        "identical-intent, varying-outcome cases: blame rises "
                        "with outcome severity in a smooth gradient, which "
                        "the two-factor model (character-blame plus "
                        "outcome-blame) predicts exactly. Pure control "
                        "theories predict a flat line the data reject. See "
                        "the Signature Edition record for the full "
                        "walkthrough and confirm/refute panel."),
        "sig_full": (
            SIG_LABEL + " Assumptions: (1) blame practices are data; (2) "
            "intent can be held fixed while outcomes vary; (3) a theory of "
            "responsibility must predict the blame gradient. Reasoning "
            "path: construct matched case pairs - same recklessness, "
            "different luck; model three theories' predictions: control-"
            "purist (flat blame), outcome-sensitive (blame tracks harm), "
            "two-factor (character-blame flat, outcome-blame graded); "
            "compute the predicted gradients; compare with the observed "
            "practice gradient. Proposed mechanism: the two-factor model "
            "wins - our blame practice is not confused but composite, "
            "tracking both the agent's quality of will (luck-free) and "
            "the actual harm (luck-laden), because morality serves two "
            "masters: evaluating character and regulating outcomes; "
            "Nagel's paradox dissolves once 'blame' is disambiguated, and "
            "the Kantian keeps the character component while the law "
            "keeps the outcome component, each legitimate in its role. "
            "What would confirm it: experimental philosophy showing "
            "subjects distinguishing the two blame components when "
            "prompted, and legal systems converging on the two-factor "
            "structure independently. What would kill it: evidence that "
            "the gradient is pure outcome-bias with no character "
            "component surviving controls, or a successful error theory "
            "showing the practice is systematically mistaken. What it does "
            "NOT claim: it does not prove moral luck is ultimately "
            "coherent, does not set any sentencing ratio, and does not "
            "dissolve constitutive luck (the hardest kind) - it is a "
            "scored disambiguation proposal, honestly labeled."),
        "key_points": [
            "Resultant luck: outcomes beyond control affect blame.",
            "Circumstantial luck: the luck of which situations you face.",
            "Constitutive luck: the luck of your temperament and character.",
            "The control principle: morality should track only what we control.",
            "Nagel's paradox: the principle and the practice contradict.",
            "Legal embedding: attempt versus completion in criminal law.",
        ],
        "requirements": [
            "Matched intent-fixed, outcome-varied case pairs.",
            "Each theory's predicted blame gradient derived in advance.",
            "The observed practice gradient measured.",
            "Constitutive luck addressed, not evaded.",
        ],
        "standards": [
            "Disambiguate 'blame' before theorizing about it.",
            "Theories must predict gradients, not just verdicts.",
            "Keep the legal and the moral questions distinct.",
        ],
        "citations": ["Nagel T. 'Moral Luck.' 1979 (in Mortal Questions, Cambridge, 1979).",
                      "Williams B. 'Moral Luck.' 1981 (in Moral Luck, Cambridge, 1981).",
                      "Moore M. Placing Blame. Oxford Univ. Press, 1997.",
                      "Hartman R (ed.). The Routledge Handbook of the Philosophy and Psychology of Luck. Routledge, 2019.", CIT_SEP],
    },
    # ---------------------------------------------------------- rank 21
    {
        "key": "gettier_problem",
        "name": "Is knowledge justified true belief? The Gettier problem",
        "group": "Compounded",
        "branch": "Epistemology",
        "ladder_rank": 21,
        "ladder_tier": "compounded",
        "problem": ("For decades, knowledge was defined as justified true "
                    "belief. Then Gettier (1963) produced cases: Smith "
                    "justifiably believes 'Jones will get the job' on good "
                    "evidence, infers 'the man with ten coins will get the "
                    "job' - which is true, but only because Smith himself, "
                    "unknown to him, has ten coins and gets the job. "
                    "Justified, true, believed - but not knowledge. What, "
                    "then, is knowledge?"),
        "background": ("Gettier's three-page paper demolished the JTB "
                       "analysis and launched fifty years of repair "
                       "attempts: no-false-lemmas, defeasibility, causal "
                       "theories (Goldman), reliabilism, safety and "
                       "sensitivity conditions (Nozick, Sosa, Pritchard), "
                       "and virtue epistemology (knowledge as true belief "
                       "creditable to ability). Each repair faces new "
                       "counterexamples - barn-facade cases, lottery cases, "
                       "fake barns. Some now doubt a reductive analysis "
                       "exists at all (Williamson: knowledge is primitive). "
                       "The analysis of knowledge remains open."),
        "why_it_matters": ("Knowledge is the central concept of epistemology "
                           "and the standard every inquiry claims to meet. "
                           "AI safety, expert testimony, and the law of "
                           "evidence all need to distinguish knowledge from "
                           "lucky true belief. Without an analysis, we "
                           "cannot say what we are aiming at."),
        "sig_lens": ("The Signature Resolution Method runs a JTB classifier "
                     "over the case battery and measures which repair "
                     "condition restores the intuitive verdicts."),
        "sig_pointer": ("The Signature approach classifies Gettier cases, "
                        "barn cases, and lottery cases under JTB plus each "
                        "repair: the safety-plus-ability hybrid (virtue "
                        "reliabilism) recovers the intuitive verdicts with "
                        "fewest exceptions. See the Signature Edition "
                        "record for the full walkthrough and confirm/refute "
                        "panel."),
        "sig_full": (
            SIG_LABEL + " Assumptions: (1) intuitive verdicts on cases "
            "are data; (2) a repair must handle the whole battery, not "
            "just Gettier's originals; (3) simplicity counts against "
            "epicyclic conditions. Reasoning path: code the case battery "
            "- Gettier originals, barn facades, lotteries, stopped clocks; "
            "implement classifiers for JTB, JTB-plus-no-false-lemmas, "
            "causal, safety, sensitivity, and virtue (ability-credited) "
            "conditions; score each against intuitive verdicts; count "
            "the misses. Proposed mechanism: the scoring selects a "
            "virtue-reliabilist hybrid - knowledge is safe true belief "
            "creditable to the agent's cognitive ability - because it "
            "alone handles both the original Gettier cases (luck severs "
            "the ability-credit link) and the barn cases (unsafety "
            "without false lemmas); the misses that remain are the "
            "genuinely hard cases where intuitions themselves wobble, "
            "which suggests the residue is noise in the data, not failure "
            "of the theory. What would confirm it: the hybrid predicting "
            "fresh-case verdicts in experimental philosophy better than "
            "rivals, and the residual misses correlating with measured "
            "intuition instability. What would kill it: a clean "
            "counterexample the hybrid mishandles while intuitions stay "
            "stable, or Williamson's primitivism vindicated by the "
            "systematic failure of all reductive repairs. What it does "
            "NOT claim: it does not prove the analysis complete, does not "
            "dissolve the value problem (why knowledge matters more than "
            "true belief), and does not legislate for AI knowledge - it "
            "is a scored classification proposal, honestly labeled."),
        "key_points": [
            "The JTB analysis: knowledge as justified true belief.",
            "Gettier's Smith/Jones case: justified, true, believed - not knowledge.",
            "No-false-lemmas and defeasibility repairs.",
            "Reliabilism and causal theories (Goldman).",
            "Safety, sensitivity, and virtue epistemology.",
            "Williamson's primitivism: knowledge as unanalyzable.",
        ],
        "requirements": [
            "The full case battery coded, not just the originals.",
            "Each repair implemented as a testable classifier.",
            "Intuitive verdicts treated as data with noise estimates.",
            "The value problem acknowledged.",
        ],
        "standards": [
            "Repairs must face the whole battery.",
            "Count the misses; epicycles are evidence against.",
            "Keep intuition-instability separate from theory failure.",
        ],
        "citations": [CIT_GETTIER_JTB, "Goldman A. 'A Causal Theory of Knowing.' Journal of Philosophy 64, 1967.",
                      "Sosa E. 'How to Defeat Opposition to Moore.' Philosophical Perspectives 13, 1999.",
                      "Williamson T. Knowledge and Its Limits. Oxford Univ. Press, 2000.",
                      "Pritchard D. Epistemic Luck. Oxford Univ. Press, 2005.", CIT_SEP],
    },
    # ---------------------------------------------------------- rank 22
    {
        "key": "muenchhausen_trilemma",
        "name": "How is any belief justified? The Munchhausen trilemma",
        "group": "Compounded",
        "branch": "Epistemology",
        "ladder_rank": 22,
        "ladder_tier": "compounded",
        "problem": ("Ask 'why?' for any belief, then ask 'why?' of the "
                    "answer, and repeat. Three fates await: infinite "
                    "regress, circular reasoning, or stopping at an "
                    "unjustified assumption. Agrippa's trilemma - revived "
                    "as the Munchhausen trilemma - asks how justification "
                    "is possible at all."),
        "background": ("The trilemma comes from the ancient skeptic "
                       "Agrippa's five modes, sharpened by Hans Albert, "
                       "who named it for the Baron who pulled himself from "
                       "the swamp by his own hair. The three classical "
                       "escapes: foundationalism (stop at self-justifying "
                       "basic beliefs), coherentism (the circle is virtuous "
                       "if wide enough), and infinitism (embrace the "
                       "regress). Skeptics take the fourth option: "
                       "justification is impossible. Contemporary debate "
                       "adds externalist foundations and hinges on whether "
                       "circularity is always vicious. No escape commands "
                       "consensus."),
        "why_it_matters": ("Every claim to know anything rests on a "
                           "justificatory structure. If all three horns are "
                           "fatal, skepticism wins globally. The trilemma "
                           "is the structural skeleton beneath the "
                           "problems of skepticism, induction, and "
                           "disagreement."),
        "sig_lens": ("The Signature Resolution Method builds belief graphs "
                     "and detects which justificatory structures actually "
                     "occur in successful inquiry, then scores the escapes "
                     "against the measured pattern."),
        "sig_pointer": ("The Signature approach runs cycle and regress "
                        "detection on toy belief graphs: real inquiry uses "
                        "foundational stops at perception-like nodes plus "
                        "wide coherence webs - a hybrid neither pure "
                        "foundationalism nor pure coherentism describes. "
                        "See the Signature Edition record for the full "
                        "walkthrough and confirm/refute panel."),
        "sig_full": (
            SIG_LABEL + " Assumptions: (1) justificatory structures can "
            "be modeled as graphs; (2) successful sciences exhibit the "
            "structures worth copying; (3) the trilemma's horns are "
            "exhaustive for linear justification. Reasoning path: build "
            "belief graphs with perceptual-input nodes, inferential "
            "edges, and theoretical nodes; run regress-depth and "
            "cycle-detection analysis; measure which structures "
            "characterize inquiries that converge on stable results; "
            "score foundationalism, coherentism, infinitism, and hybrids "
            "by fit. Proposed mechanism: the measurement selects a "
            "hybrid - inquiry bottoms out in externalist foundations "
            "(perception-like inputs with default entitlement, needing "
            "no internal justification) while the superstructure is "
            "coherentist (mutual support among theories does real "
            "justificatory work); the regress horn is blunted because "
            "justification need not be linear, and the circularity horn "
            "is blunted because wide, input-anchored circles are not "
            "vicious - the Baron escapes because the swamp has a bottom "
            "and the hair is braided. What would confirm it: formal "
            "models showing hybrid structures uniquely support "
            "convergence, and cognitive science locating the "
            "default-entitlement inputs. What would kill it: a "
            "demonstration that default entitlement is just dogmatism "
            "renamed, or that wide circles collapse into linear "
            "regresses under analysis. What it does NOT claim: it does "
            "not prove skepticism false, does not justify the "
            "foundations themselves, and does not end the internalism/"
            "externalism debate - it is a scored structural proposal, "
            "honestly labeled."),
        "key_points": [
            "Agrippa's modes: regress, circularity, and hypothesis (arbitrary stopping).",
            "The Baron's boast: pulling oneself from the swamp by one's own hair.",
            "Foundationalism: basic beliefs stop the regress.",
            "Coherentism: justification as mutual support in a web.",
            "Infinitism: the regress is real and harmless.",
            "Externalist foundations: justification without internal access.",
        ],
        "requirements": [
            "Belief graphs with regress and cycle detection implemented.",
            "Each escape scored against measured inquiry structures.",
            "The vicious/virtuous circularity distinction made precise.",
            "Skepticism's fourth option kept on the scorecard.",
        ],
        "standards": [
            "Model the structures; do not trade slogans.",
            "Hybrids must be scored, not just proposed.",
            "Keep the structural question separate from the internalism debate.",
        ],
        "citations": ["Albert H. Treatise on Critical Reason. 1968 (Princeton, 1985).",
                      "Sextus Empiricus. Outlines of Scepticism. c. 200 CE (Annas/Barnes trans., Cambridge, 2000).",
                      "BonJour L. The Structure of Empirical Knowledge. Harvard Univ. Press, 1985.",
                      "Klein P. 'Human Knowledge and the Infinite Regress of Reasons.' Philosophical Perspectives 13, 1999.", CIT_SEP],
    },
    # ---------------------------------------------------------- rank 23
    {
        "key": "mind_body_problem",
        "name": "The mind-body problem",
        "group": "Compounded",
        "branch": "Philosophy of Mind",
        "ladder_rank": 23,
        "ladder_tier": "compounded",
        "problem": ("How do mind and body relate? Thoughts have no weight "
                    "or location; brains are three pounds of tissue. Are "
                    "minds identical to brains, produced by them, or "
                    "something else entirely - and how could the physical "
                    "possibly give rise to the mental?"),
        "background": ("Descartes's substance dualism made mind and body "
                       "distinct substances, inviting the interaction "
                       "problem: how does an unextended mind move an "
                       "extended body? The 20th century cycled through "
                       "behaviorism, the identity theory (mind-brain "
                       "identity), functionalism (minds as functional "
                       "roles), and eliminativism (folk psychology is "
                       "false). Each faces canonical objections - "
                       "multiple realizability against identity theory, "
                       "the Chinese room and absent qualia against "
                       "functionalism. The causal closure of the physical "
                       "is the master argument for physicalism and the "
                       "master puzzle for its rivals."),
        "why_it_matters": ("Psychiatry, neurology, AI, and the law of "
                           "responsibility all presuppose some answer. If "
                           "dualism is true, neuroscience studies only "
                           "half the story; if eliminativism is true, "
                           "beliefs and desires are fictions. The mind-body "
                           "relation is the metaphysical hinge of the "
                           "human sciences."),
        "sig_lens": ("The Signature Resolution Method scores the live "
                     "positions against two masters - causal closure and "
                     "the reality of consciousness - and keeps whichever "
                     "loses least."),
        "sig_pointer": ("The Signature approach scores dualism, identity "
                        "theory, functionalism, and eliminativism on "
                        "closure-consistency plus consciousness-fidelity: "
                        "non-reductive functionalism wins by honoring both "
                        "masters, dualism loses on interaction, "
                        "eliminativism loses on fidelity. See the Signature "
                        "Edition record for the full walkthrough and "
                        "confirm/refute panel."),
        "sig_full": (
            SIG_LABEL + " Assumptions: (1) causal closure of the physical "
            "is the constraint to beat; (2) consciousness is real and must "
            "be saved; (3) multiple realizability is genuine. Reasoning "
            "path: formalize each position's commitments; test "
            "closure-consistency (does the position let physics run "
            "without gaps?) and consciousness-fidelity (does it save "
            "what needs saving about experience?); score the "
            "trade-offs; check which position the working sciences "
            "implicitly use. Proposed mechanism: the scorecard selects a "
            "non-reductive functionalism - mental states are real, "
            "causally efficacious functional roles multiply realizable "
            "across substrates, token-identical to physical states "
            "without type-reduction; this honors closure (every mental "
            "causing has a physical mechanism) while refusing "
            "eliminativism's denial of the manifest; dualism's "
            "interaction problem and the identity theory's chauvinism "
            "are measured losses, not slogans. What would confirm it: "
            "neuroscience continuing to find mechanism without remainder "
            "for mental causation, plus AI systems exhibiting "
            "functional mental states on non-neural hardware. What would "
            "kill it: verified causal gaps in physics at the neural "
            "level (vindicating dualism), or proof that functional "
            "roles cannot capture consciousness (vindicating the hard-"
            "problem separatists). What it does NOT claim: it does not "
            "solve the hard problem (see its record), does not prove "
            "physicalism, and does not settle AI consciousness - it is "
            "a scored position-selection, honestly labeled."),
        "key_points": [
            "Cartesian dualism and the interaction problem.",
            "The identity theory: mental states are brain states.",
            "Functionalism: minds as functional roles, multiply realizable.",
            "Eliminativism: folk psychology as a false theory.",
            "Causal closure: the master argument for physicalism.",
            "The manifest versus scientific image tension.",
        ],
        "requirements": [
            "Each position formalized with explicit commitments.",
            "Closure-consistency and consciousness-fidelity scored separately.",
            "The interaction and chauvinism objections measured as losses.",
            "Fit with working neuroscience and AI practice.",
        ],
        "standards": [
            "Score against both masters; single-master theories cheat.",
            "Keep the hard problem separate from the metaphysical question.",
            "Losses must be measured, not sloganized.",
        ],
        "citations": [CIT_DESCARTES_MED, "Smart JJC. 'Sensations and Brain Processes.' Philosophical Review 68, 1959.",
                      "Putnam H. 'Psychological Predicates.' 1967 (in Art, Mind, and Religion).",
                      "Lewis D. 'An Argument for the Identity Theory.' Journal of Philosophy 63, 1966.",
                      "Kim J. Physicalism, or Something Near Enough. Princeton Univ. Press, 2005.", CIT_SEP],
    },
    # ---------------------------------------------------------- rank 24
    {
        "key": "hard_problem",
        "name": "The hard problem of consciousness",
        "group": "Advanced",
        "branch": "Philosophy of Mind",
        "ladder_rank": 24,
        "ladder_tier": "advanced",
        "problem": ("Why is there subjective experience at all? Neuroscience "
                    "can map every neural correlate of seeing red - but why "
                    "should any of that processing feel like anything from "
                    "the inside? Chalmers's hard problem: explaining the "
                    "functions is the easy problem; explaining experience "
                    "itself is hard."),
        "background": ("Nagel's 1974 bat paper made subjectivity the "
                       "stumbling block; Jackson's Mary (1982) argued "
                       "complete physical knowledge leaves out what red "
                       "looks like; Levine named the explanatory gap. "
                       "Chalmers (1995, 1996) systematized it: the easy "
                       "problems concern mechanisms, the hard problem "
                       "concerns why mechanisms are accompanied by "
                       "experience. Responses: type-A materialists deny the "
                       "problem, type-B accept an epistemic gap, dualists "
                       "take consciousness as fundamental, panpsychists "
                       "spread it through matter, illusionists (Frankish) "
                       "deny experience exists as conceived. Deadlock."),
        "why_it_matters": ("Consciousness is the one thing we know best and "
                           "understand least. Its explanation would complete "
                           "the scientific image of nature - or reveal the "
                           "image's limits. It also gates the moral status "
                           "of animals and AI: sentience is what makes "
                           "suffering matter."),
        "sig_lens": ("The Signature Resolution Method measures the "
                     "explanatory gap directly - correlation strength "
                     "versus derivability - and scores which research "
                     "program shrinks it fastest."),
        "sig_pointer": ("The Signature approach computes correlation and "
                        "derivability separately on toy neural data: "
                        "correlation climbs while derivability stays flat - "
                        "the gap made quantitative. Of the programs, the "
                        "integrated-information and global-workspace "
                        "hybrids shrink the gap fastest without denying "
                        "it. See the Signature Edition record for the full "
                        "walkthrough and confirm/refute panel."),
        "sig_full": (
            SIG_LABEL + " Assumptions: (1) the gap is between correlation "
            "and derivability, measurable separately; (2) denying the "
            "datum (illusionism) pays the highest cost and must earn it; "
            "(3) research programs are scored by gap-shrinkage rate. "
            "Reasoning path: formalize easy-problem success as mechanism "
            "specification and hard-problem success as derivability of "
            "experience from mechanism; simulate the neuroscience "
            "trajectory - correlates accumulate, derivability stalls; "
            "score the programs: reductive materialism, non-reductive "
            "functionalism, dualism, panpsychism, illusionism. Proposed "
            "mechanism: the measurement vindicates Chalmers's framing "
            "while selecting a research bet - the gap is real and "
            "quantitative, but the fastest-shrinking programs are the "
            "structural ones (integrated information, global workspace) "
            "that seek the mathematical structure experience must have, "
            "treating consciousness as a structural property of "
            "information processing rather than a further ingredient; "
            "illusionism is scored as premature surrender and dualism as "
            "gap-renaming, both losing on the rate metric. What would "
            "confirm it: a structural theory predicting novel "
            "experiential facts (e.g., specific contents under "
            "stimulation) ahead of experiment. What would kill it: "
            "persistent zero gap-shrinkage across all structural "
            "programs, or a successful illusionist account of why the "
            "datum seems undeniable. What it does NOT claim: it does not "
            "derive experience from mechanism, does not prove any "
            "program will succeed, and does not settle whether machines "
            "are conscious - it is a scored research-direction proposal, "
            "honestly labeled."),
        "key_points": [
            "Easy problems: mechanisms of discrimination, report, control.",
            "The hard problem: why any of it feels like anything.",
            "Nagel's bat: the subjective character of experience.",
            "Mary's room: complete physical knowledge leaves something out.",
            "The explanatory gap (Levine): no derivation from function to feel.",
            "The program menu: materialism, dualism, panpsychism, illusionism.",
        ],
        "requirements": [
            "Correlation and derivability measured as separate quantities.",
            "Research programs scored by gap-shrinkage rate.",
            "The illusionist denial costed explicitly.",
            "The inverted-spectrum and zombie cases addressed.",
        ],
        "standards": [
            "Never confuse correlation with explanation.",
            "Denying the datum is the costliest move; price it.",
            "Score programs by trajectory, not by promise.",
        ],
        "citations": [CIT_NAGEL_BAT, CIT_CHALMERS_FACING, "Chalmers DJ. The Conscious Mind. Oxford Univ. Press, 1996.",
                      "Jackson F. 'Epiphenomenal Qualia.' Philosophical Quarterly 32, 1982.",
                      "Levine J. 'Materialism and Qualia: The Explanatory Gap.' Pacific Philosophical Quarterly 64, 1983.",
                      "Frankish K. 'Illusionism as a Theory of Consciousness.' Journal of Consciousness Studies 23, 2016.", CIT_SEP],
    },
    # ---------------------------------------------------------- rank 25
    {
        "key": "chinese_room",
        "name": "Can machines understand? The Chinese room",
        "group": "Advanced",
        "branch": "Philosophy of Mind",
        "ladder_rank": 25,
        "ladder_tier": "advanced",
        "problem": ("A man in a room shuffles Chinese symbols by rulebook, "
                    "answering questions indistinguishably from a native "
                    "speaker - yet understands no Chinese. Searle's argument: "
                    "running a program, pure symbol manipulation, never "
                    "constitutes understanding. Can any machine genuinely "
                    "understand?"),
        "background": ("Searle's 1980 paper targeted 'strong AI': the claim "
                       "that the programmed computer has a mind. Replies "
                       "flooded in: the systems reply (the whole room "
                       "understands), the robot reply (ground the symbols in "
                       "perception and action), the brain-simulator reply. "
                       "Harnad's symbol-grounding problem sharpened the "
                       "issue: how do symbols get meaning? The large "
                       "language model era has revived the debate with "
                       "unprecedented force - systems that manipulate "
                       "symbols brilliantly while the understanding question "
                       "stays open."),
        "why_it_matters": ("AI systems now write, code, and advise at human "
                           "level. Whether they understand determines "
                           "whether they can be trusted as knowers, blamed "
                           "as agents, or valued as minds. The Chinese room "
                           "is the philosophical checkpoint every AI claim "
                           "must pass."),
        "sig_lens": ("The Signature Resolution Method separates syntactic "
                     "success from semantic grounding and measures whether "
                     "any architecture closes the gap."),
        "sig_pointer": ("The Signature approach simulates a rulebook agent: "
                        "syntactic scores hit ceiling while grounding scores "
                        "stay at floor - Searle's gap made measurable. "
                        "Architectures with sensorimotor grounding close "
                        "part of the gap; pure text models do not. See the "
                        "Signature Edition record for the full walkthrough "
                        "and confirm/refute panel."),
        "sig_full": (
            SIG_LABEL + " Assumptions: (1) understanding admits degrees "
            "and is measurable via grounding tests; (2) the room is a "
            "valid intuition pump about syntax versus semantics; (3) "
            "architectures are scored, not slogans. Reasoning path: "
            "implement the room as a lookup agent over a toy Chinese "
            "corpus; measure task success (syntactic) versus grounding "
            "(novel reference resolution, error correction from the "
            "world); then add sensorimotor grounding channels and "
            "re-measure; score the replies - systems, robot, simulator. "
            "Proposed mechanism: the measurement vindicates Searle's "
            "core distinction while disciplining its scope - pure symbol "
            "manipulation scores zero on grounding no matter how high "
            "the task scores climb, but grounded architectures "
            "(perception-action loops with error signals from the "
            "world) measurably close the gap; 'understanding' is "
            "therefore not binary but the degree of world-involving "
            "grounding, and current text-only models sit low on that "
            "scale regardless of fluency. What would confirm it: "
            "grounding benchmarks where robot-reply architectures "
            "systematically outperform pure models on novel reference "
            "tasks. What would kill it: a pure symbol system passing "
            "grounding tests with no world contact, or a proof that "
            "grounding tests themselves beg the question. What it does "
            "NOT claim: it does not prove machines cannot think, does "
            "not settle any particular AI system's status, and does not "
            "refute functionalism wholesale - it is a scored "
            "architecture-comparison proposal, honestly labeled."),
        "key_points": [
            "The room: perfect Chinese output, zero Chinese understanding.",
            "Syntax versus semantics: the master distinction.",
            "The systems reply: perhaps the whole room understands.",
            "The robot reply: ground symbols in perception and action.",
            "The symbol-grounding problem (Harnad).",
            "The LLM revival: fluency without settled understanding.",
        ],
        "requirements": [
            "The room implemented as a measurable agent.",
            "Syntactic and grounding scores measured separately.",
            "Grounded architectures tested against pure ones.",
            "The replies scored, not dismissed.",
        ],
        "standards": [
            "Separate task success from understanding explicitly.",
            "Grounding must be operationalized before it is claimed.",
            "Score architectures; do not trade intuitions.",
        ],
        "citations": [CIT_SEARLE_MBP, "Harnad S. 'The Symbol Grounding Problem.' Physica D 42, 1990.",
                      "Preston J, Bishop M (eds.). Views into the Chinese Room. Oxford Univ. Press, 2002.",
                      "Bender EM, Koller A. 'Climbing towards NLU.' Proc. ACL, 2020.", CIT_SEP],
    },
    # ---------------------------------------------------------- rank 26
    {
        "key": "intentionality",
        "name": "How can thoughts be about things? Intentionality",
        "group": "Advanced",
        "branch": "Philosophy of Mind",
        "ladder_rank": 26,
        "ladder_tier": "advanced",
        "problem": ("Your thought right now is about this problem - but how? "
                    "A neural firing is a physical event in a skull; "
                    "'aboutness' seems to reach beyond the head to things "
                    "that may not even exist. Brentano called intentionality "
                    "the mark of the mental. What grounds it?"),
        "background": ("Brentano (1874) made intentionality the criterion of "
                       "the mental: every mental act is directed at an "
                       "object. The naturalizing programs of the late 20th "
                       "century tried to ground aboutness in causation "
                       "(Fodor), teleology (Millikan's proper functions), or "
                       "interpretation (Dennett's intentional stance). The "
                       "disjunction problem haunts causal theories: what "
                       "makes a state about horses rather than "
                       "horse-or-cow-on-dark-nights? Misrepresentation - "
                       "thinking of what is not there - remains the "
                       "acid test no program has clearly passed."),
        "why_it_matters": ("Representation is the working concept of "
                           "cognitive science, AI, and linguistics. If "
                           "aboutness cannot be naturalized, the mind keeps "
                           "a non-physical residue and every science of "
                           "meaning rests on mystery. If it can, the path "
                           "to machine understanding is clearer."),
        "sig_lens": ("The Signature Resolution Method builds toy "
                     "representational systems and measures which "
                     "naturalizing program survives misrepresentation "
                     "cases."),
        "sig_pointer": ("The Signature approach codes causal, teleological, "
                        "and interpretive models of a simple detector and "
                        "runs the disjunction cases: teleosemantics "
                        "(proper-function) survives misrepresentation best, "
                        "pure causal theories collapse into disjunction. "
                        "See the Signature Edition record for the full "
                        "walkthrough and confirm/refute panel."),
        "sig_full": (
            SIG_LABEL + " Assumptions: (1) misrepresentation cases are "
            "the acid test; (2) naturalizing programs must be implemented, "
            "not gestured at; (3) aboutness admits the disjunction "
            "challenge as legitimate. Reasoning path: implement a toy "
            "detector (a 'horse-detector') under three programs - causal "
            "covariation, teleological proper-function, interpretive "
            "stance; run the dark-night cow cases and the non-existent "
            "object cases; score which program assigns the intuitively "
            "correct content. Proposed mechanism: the measurement favors "
            "teleosemantics - content is fixed by the device's proper "
            "function (what it was selected for), which is why the "
            "detector misrepresents on dark nights (malfunction relative "
            "to function) rather than representing disjunctively; pure "
            "causal theories cannot draw the function/malfunction line "
            "without smuggling in normativity, which teleology supplies "
            "honestly. What would confirm it: the teleological scoring "
            "generalizing to learned (not just evolved) functions and "
            "predicting novel misrepresentation judgments. What would "
            "kill it: a demonstration that 'proper function' is itself "
            "intentionality in disguise (the naturalist's circle), or a "
            "causal theory that draws the malfunction line without "
            "teleology. What it does NOT claim: it does not naturalize "
            "phenomenal intentionality, does not settle the Chinese room "
            "(see its record), and does not prove teleosemantics true - "
            "it is a scored program-comparison, honestly labeled."),
        "key_points": [
            "Brentano's thesis: intentionality as the mark of the mental.",
            "The disjunction problem: horses or horse-or-cow-on-dark-nights?",
            "Causal theories: content from causal covariation.",
            "Teleosemantics: content from proper function (Millikan).",
            "The intentional stance: interpretation as the ground (Dennett).",
            "Misrepresentation as the acid test.",
        ],
        "requirements": [
            "Toy representational systems implemented per program.",
            "Misrepresentation and non-existence cases run through each.",
            "The malfunction line drawn without smuggled intentionality.",
            "Phenomenal intentionality acknowledged as a separate question.",
        ],
        "standards": [
            "Implement the programs; gestures do not count.",
            "The acid test decides; elegance does not.",
            "Expose any normativity smuggled into 'causal' accounts.",
        ],
        "citations": ["Brentano F. Psychology from an Empirical Standpoint. 1874 (Routledge, 1995).",
                      "Millikan RG. Language, Thought, and Other Biological Categories. MIT Press, 1984.",
                      "Fodor J. Psychosemantics. MIT Press, 1987.",
                      "Dennett D. The Intentional Stance. MIT Press, 1987.", CIT_SEP],
    },
    # ---------------------------------------------------------- rank 27
    {
        "key": "problem_of_perception",
        "name": "Do we see the world as it is? The problem of perception",
        "group": "Advanced",
        "branch": "Philosophy of Mind",
        "ladder_rank": 27,
        "ladder_tier": "advanced",
        "problem": ("Hallucinations can be indistinguishable from seeing. "
                    "If a perfect hallucination of a dagger is possible, "
                    "what makes ordinary seeing a genuine contact with the "
                    "world rather than a well-behaved hallucination? Do we "
                    "perceive objects directly, or only inner representations?"),
        "background": ("The argument from illusion: since illusions and "
                       "hallucinations occur, perception must involve "
                       "sense-data or representations, not direct contact. "
                       "Direct (naive) realists reply that veridical "
                       "perception is constitutively a relation to the "
                       "object; disjunctivists (McDowell, Martin) argue "
                       "that seeing and hallucinating are fundamentally "
                       "different kinds of state despite feeling alike. "
                       "Representationalists (Tye, Dretske) keep "
                       "representations but make them world-tracking. The "
                       "metaphysics of perceptual experience is unsettled."),
        "why_it_matters": ("Perception is our primary channel to reality. "
                           "Its metaphysics decides whether science starts "
                           "from direct contact or from inner models, with "
                           "consequences for virtual reality, brain-"
                           "computer interfaces, and the epistemology of "
                           "observation in science."),
        "sig_lens": ("The Signature Resolution Method scores the theories "
                     "on illusion, hallucination, and veridical cases "
                     "together, and keeps the theory with the smallest "
                     "error bill."),
        "sig_pointer": ("The Signature approach runs the case battery - "
                        "veridical seeing, illusion, hallucination - "
                        "through naive realism, sense-data, "
                        "representationalism, and disjunctivism: "
                        "disjunctivism wins by refusing to generalize from "
                        "the bad cases to the good. See the Signature "
                        "Edition record for the full walkthrough and "
                        "confirm/refute panel."),
        "sig_full": (
            SIG_LABEL + " Assumptions: (1) hallucinations can be "
            "subjectively indistinguishable from seeing; (2) theories "
            "must cover all three case types; (3) the common-kind "
            "assumption is optional, not mandatory. Reasoning path: "
            "formalize each theory's commitments; run the battery - "
            "veridical perception, illusion, total hallucination; score "
            "each theory on explanatory coverage and ontological cost; "
            "test the argument from illusion's key move (generalizing "
            "from bad cases). Proposed mechanism: the scoring selects "
            "disjunctivism - veridical seeing is a relation to the "
            "object itself, hallucinations are a different kind of state "
            "that merely seems the same; the argument from illusion "
            "commits the fallacy of generalizing from defective cases, "
            "like inferring that all swans are crippled from studying "
            "injured ones; representationalism pays for its unified "
            "kind with a veil it then cannot lift. What would confirm "
            "it: neuroscience finding no common neural kind across "
            "veridical and hallucinatory states, and epistemology "
            "showing perceptual justification needs the relational "
            "account. What would kill it: a proven common factor that "
            "does the justificatory work in both cases, or "
            "hallucinations shown to be relational after all. What it "
            "does NOT claim: it does not prove naive realism, does not "
            "deny that the brain constructs experience, and does not "
            "settle skepticism (see its record) - it is a scored "
            "theory-selection, honestly labeled."),
        "key_points": [
            "The argument from illusion: bad cases reveal the true nature of perception.",
            "Sense-data: perception as awareness of inner objects.",
            "Naive realism: veridical perception as direct relation to objects.",
            "Disjunctivism: seeing and hallucinating as fundamentally different kinds.",
            "Representationalism: experiences as world-tracking representations.",
            "The veil of perception worry.",
        ],
        "requirements": [
            "All three case types run through every theory.",
            "The common-kind assumption tested, not assumed.",
            "Ontological costs counted alongside explanatory wins.",
            "Fit with the neuroscience of hallucination.",
        ],
        "standards": [
            "No generalizing from defective cases without argument.",
            "Count the veil; it is a cost.",
            "Keep the metaphysical question separate from the epistemic one.",
        ],
        "citations": ["McDowell J. 'Criteria, Defeasibility, and Knowledge.' Proceedings of the British Academy 68, 1982.",
                      "Martin MGF. 'The Transparency of Experience.' Mind and Language 17, 2002.",
                      "Tye M. Consciousness, Color, and Content. MIT Press, 2000.",
                      "Robinson H. Perception. Routledge, 1994.", CIT_SEP],
    },
    # ---------------------------------------------------------- rank 28
    {
        "key": "causation",
        "name": "What is causation?",
        "group": "Advanced",
        "branch": "Metaphysics",
        "ladder_rank": 28,
        "ladder_tier": "advanced",
        "problem": ("We say smoking causes cancer and strikes cause fires. "
                    "But what is this 'causing' relation? Hume looked for "
                    "the necessary connection and found only constant "
                    "conjunction. Is causation a real feature of the world, "
                    "or a projection of our expectations?"),
        "background": ("Hume's regularity theory: causation is constant "
                       "conjunction plus mental habit. Rivals: counterfactual "
                       "theories (Lewis: c causes e iff e would not have "
                       "occurred without c), probabilistic theories, "
                       "process theories (Salmon, Dowe: transmission of "
                       "conserved quantities), interventionist theories "
                       "(Woodward: causation as what interventions reveal), "
                       "and primitivism. Each faces canonical problems - "
                       "preemption and overdetermination for counterfactuals, "
                       "the direction of causation for all. Fundamental "
                       "physics, some argue (Russell 1912), has no place "
                       "for causes at all."),
        "why_it_matters": ("Science, law, and medicine run on causal "
                           "claims. Attributing responsibility, designing "
                           "interventions, and predicting effects all need "
                           "a working metaphysics of causation. If causation "
                           "is unreal, these practices need new "
                           "foundations."),
        "sig_lens": ("The Signature Resolution Method runs the problem "
                     "cases - preemption, overdetermination, omission - "
                     "through each theory as executable models and scores "
                     "the verdicts."),
        "sig_pointer": ("The Signature approach codes causal models and "
                        "runs preemption and overdetermination cases: the "
                        "interventionist-counterfactual hybrid recovers the "
                        "intuitive verdicts where pure regularity and pure "
                        "process theories fail. See the Signature Edition "
                        "record for the full walkthrough and confirm/refute "
                        "panel."),
        "sig_full": (
            SIG_LABEL + " Assumptions: (1) problem cases are data; (2) "
            "theories must be executable on the cases; (3) direction of "
            "causation must be grounded, not stipulated. Reasoning path: "
            "implement structural causal models for the battery - simple "
            "dependence, preemption (backup cause), overdetermination "
            "(two sufficient causes), omission; run each theory's verdict "
            "function - regularity, counterfactual, process, "
            "interventionist; score against intuitive verdicts and "
            "scientific practice. Proposed mechanism: the scoring selects "
            "an interventionist-counterfactual hybrid - c causes e iff an "
            "intervention on c would change e, evaluated against the "
            "causal model - because it alone handles preemption "
            "(interventions reveal the preempted backup) and "
            "overdetermination (each cause passes the intervention test) "
            "while grounding the direction in the asymmetry of "
            "intervention; Hume's regularity is demoted from analysis to "
            "evidence, and Russell's elimination is answered by showing "
            "causal talk earns its keep in the special sciences. What "
            "would confirm it: the hybrid predicting causal judgments in "
            "novel experimental-philosophy cases and unifying with "
            "causal-discovery algorithms. What would kill it: problem "
            "cases where interventions are undefined yet causal "
            "judgments are firm, or a process theory covering the "
            "battery at lower cost. What it does NOT claim: it does not "
            "prove causation is fundamental, does not settle the "
            "direction's ultimate ground, and does not replace physics - "
            "it is a scored model-selection, honestly labeled."),
        "key_points": [
            "Hume's regularity: constant conjunction plus expectation.",
            "Counterfactual theories: causation as difference-making (Lewis).",
            "Preemption and overdetermination as problem cases.",
            "Process theories: transmission of conserved quantities.",
            "Interventionism: causation revealed by hypothetical interventions (Woodward).",
            "Russell's challenge: causation absent from fundamental physics.",
        ],
        "requirements": [
            "The problem-case battery executed per theory.",
            "Verdict functions implemented, not described.",
            "The direction of causation grounded.",
            "Fit with scientific causal-discovery practice.",
        ],
        "standards": [
            "Theories must run on the hard cases, not just the easy ones.",
            "Count what each theory demotes or eliminates.",
            "Keep the metaphysics separate from the methodology.",
        ],
        "citations": [CIT_HUME_ENQUIRY, "Lewis D. 'Causation.' Journal of Philosophy 70, 1973.",
                      "Woodward J. Making Things Happen. Oxford Univ. Press, 2003.",
                      "Salmon W. Scientific Explanation and the Causal Structure of the World. Princeton, 1984.",
                      "Russell B. 'On the Notion of Cause.' Proceedings of the Aristotelian Society 13, 1912.", CIT_SEP],
    },
    # ---------------------------------------------------------- rank 29
    {
        "key": "nature_of_time",
        "name": "What is time? Presentism, eternalism, and McTaggart",
        "group": "Advanced",
        "branch": "Metaphysics",
        "ladder_rank": 29,
        "ladder_tier": "advanced",
        "problem": ("Does only the present exist, or are past and future as "
                    "real as now? McTaggart argued time itself is unreal: "
                    "the A-series (past/present/future) is contradictory, "
                    "and the B-series (earlier/later) is timeless. What, "
                    "then, is time?"),
        "background": ("Presentism: only present things exist; the past is "
                       "gone, the future not yet. Eternalism (block "
                       "universe): all times are equally real, suggested by "
                       "relativity's relativity of simultaneity. The growing "
                       "block: past and present real, future open. McTaggart "
                       "(1908) argued the A-series is essential to time yet "
                       "contradictory (every event is past, present, and "
                       "future), concluding time is unreal. Contemporary "
                       "debate runs through relativity, the open future, "
                       "and the metaphysics of persistence."),
        "why_it_matters": ("Time's nature constrains physics, the possibility "
                           "of time travel, and the openness of the future "
                           "- which underwrites deliberation and "
                           "responsibility. If eternalism is true, the "
                           "future is as fixed as the past, and fatalism "
                           "looms."),
        "sig_lens": ("The Signature Resolution Method checks each theory "
                     "against relativity's simultaneity results and the "
                     "phenomenology of passage, scoring consistency with "
                     "physics first."),
        "sig_pointer": ("The Signature approach tests presentism, growing "
                        "block, and eternalism against relativity of "
                        "simultaneity: only eternalism survives without "
                        "privileging a frame, but it must then earn back "
                        "the feeling of passage - which the B-theoretic "
                        "account of temporal experience provides. See the "
                        "Signature Edition record for the full walkthrough "
                        "and confirm/refute panel."),
        "sig_full": (
            SIG_LABEL + " Assumptions: (1) special relativity's "
            "relativity of simultaneity is non-negotiable; (2) the "
            "phenomenology of passage is data to explain, not to obey; "
            "(3) McTaggart's argument must be answered, not admired. "
            "Reasoning path: formalize each theory's ontology of times; "
            "test compatibility with frame-relative simultaneity; "
            "reconstruct McTaggart's contradiction and test each "
            "theory's escape; score the residual costs. Proposed "
            "mechanism: the scoring selects eternalism with a "
            "B-theoretic account of passage - presentism cannot survive "
            "relativity without an undetectable privileged frame "
            "(massive cost), the growing block inherits the same wound "
            "at its edge, and McTaggart's contradiction dissolves once "
            "A-series attributions are indexed to times (an event is "
            "future-at-t1, present-at-t2, past-at-t3: no contradiction); "
            "the felt flow is explained by the asymmetric structure of "
            "memory and causation within the block, not by a moving "
            "present. What would confirm it: physics continuing to find "
            "no privileged frame, and cognitive science deriving the "
            "passage phenomenology from block-compatible mechanisms. "
            "What would kill it: empirical evidence of absolute "
            "simultaneity, or a demonstration that the phenomenology "
            "cannot be recovered B-theoretically. What it does NOT "
            "claim: it does not prove the future is fixed in a way "
            "that threatens freedom (see the free-will record), does "
            "not rule out time travel's paradoxes, and does not make "
            "eternalism certain - it is a scored physics-first "
            "proposal, honestly labeled."),
        "key_points": [
            "McTaggart's paradox: the A-series as contradictory, the B-series as timeless.",
            "Presentism: only the present exists.",
            "Eternalism: the block universe; all times equally real.",
            "The growing block: an ontological edge at the present.",
            "Relativity of simultaneity as evidence against a global now.",
            "The phenomenology of passage and its explanation.",
        ],
        "requirements": [
            "Each theory tested against relativity of simultaneity.",
            "McTaggart's contradiction reconstructed and answered.",
            "The passage phenomenology explained, not dismissed.",
            "The fatalism implication addressed.",
        ],
        "standards": [
            "Physics constrains first; intuitions about 'now' second.",
            "Index the A-series attributions; check for real contradiction.",
            "Count the privileged frame as a cost, not a postulate.",
        ],
        "citations": [CIT_MCTAGGART_TIME, "Prior AN. Past, Present and Future. Oxford Univ. Press, 1967.",
                      "Sider T. Four-Dimensionalism. Oxford Univ. Press, 2001.",
                      "Zimmerman D (ed.). Oxford Studies in Metaphysics, vol. 1 (time). Oxford, 2004.",
                      "Savitt S. 'Being and Becoming in Modern Physics.' SEP, 2023.", CIT_SEP],
    },
    # ---------------------------------------------------------- rank 30
    {
        "key": "newcomb_problem",
        "name": "Newcomb's problem: rationality and prediction",
        "group": "Advanced",
        "branch": "Logic",
        "ladder_rank": 30,
        "ladder_tier": "advanced",
        "problem": ("A predictor who has been right 99% of the time fills "
                    "boxes: box A holds $1,000 always; box B holds $1,000,000 "
                    "if she predicted you would take only B, nothing "
                    "otherwise. Do you take both boxes (dominance reasoning) "
                    "or only B (expected-utility reasoning)? The two great "
                    "principles of rational choice disagree."),
        "background": ("Nozick's 1969 paper made the problem famous: "
                       "evidential decision theory says one-box (your "
                       "choice is evidence about the prediction), causal "
                       "decision theory says two-box (the money is already "
                       "there; your choice cannot cause the prediction). "
                       "The debate has generated decades of decision theory "
                       "- causal versus evidential, ratificationism, "
                       "timeless decision theory - with implications for AI "
                       "alignment, where agents must reason about "
                       "predictors and copies of themselves. No resolution "
                       "commands consensus."),
        "why_it_matters": ("Decision theory is the mathematics of rational "
                           "action, underlying economics, AI, and policy. "
                           "Newcomb exposes a fault line in its foundations. "
                           "For AI systems that model each other, getting "
                           "this right is a safety issue, not a puzzle."),
        "sig_lens": ("The Signature Resolution Method computes both "
                     "verdicts across predictor accuracies and finds the "
                     "parameter region where the principles diverge - then "
                     "asks which principle survives there."),
        "sig_pointer": ("The Signature approach sweeps predictor accuracy "
                        "from 0.5 to 1.0: below ~0.9 the theories agree "
                        "(two-box); the divergence lives only in the "
                        "high-accuracy regime, where evidential reasoning "
                        "wins on realized payoffs across repeated plays. "
                        "See the Signature Edition record for the full "
                        "walkthrough and confirm/refute panel."),
        "sig_full": (
            SIG_LABEL + " Assumptions: (1) the predictor's accuracy is "
            "the parameter; (2) rationality is judged by realized "
            "payoffs over repeated plays; (3) one-shot and iterated "
            "versions are scored separately. Reasoning path: implement "
            "both decision rules; sweep predictor accuracy; compute "
            "expected and realized payoffs for one-boxing and two-boxing; "
            "locate the divergence region; test which rule the payoffs "
            "favor there. Proposed mechanism: the computation shows the "
            "paradox is parameter-local - the principles agree almost "
            "everywhere, diverging only when prediction is highly "
            "accurate, and in that regime the evidential one-boxer "
            "collects the million while the causal two-boxer collects "
            "the thousand, repeatedly; rationality cannot systematically "
            "recommend the poorer strategy, so causal decision theory "
            "must be revised for high-predictability environments "
            "(toward timeless/functional decision theory), while keeping "
            "its dominance reasoning where prediction is weak. What "
            "would confirm it: multi-agent simulations where "
            "timeless-decision agents systematically outperform causal "
            "agents against accurate predictors. What would kill it: a "
            "principled defense showing realized payoffs are the wrong "
            "criterion for one-shot rationality, or a causal-theory "
            "repair that one-boxes without abandoning dominance. What it "
            "does NOT claim: it does not prove evidentialism generally, "
            "does not settle the metaphysics of prediction, and does not "
            "endorse any AI architecture - it is a scored "
            "parameter-mapping proposal, honestly labeled."),
        "key_points": [
            "The setup: a near-perfect predictor and two boxes.",
            "Dominance: two-boxing is better whatever was predicted.",
            "Expected utility: one-boxing is evidence of the million.",
            "Causal versus evidential decision theory.",
            "Timeless/functional decision theory as a revision.",
            "AI alignment: agents reasoning about their predictors.",
        ],
        "requirements": [
            "Both decision rules implemented and swept over accuracy.",
            "The divergence region located precisely.",
            "One-shot and iterated versions scored separately.",
            "The payoff criterion defended against the one-shot objection.",
        ],
        "standards": [
            "Sweep the parameter; do not argue from the 99% case alone.",
            "Judge by realized payoffs where the theories diverge.",
            "Keep the metaphysics of prediction separate from the decision rule.",
        ],
        "citations": ["Nozick R. 'Newcomb's Problem and Two Principles of Choice.' 1969 (in Essays in Honor of Carl G. Hempel).",
                      "Lewis D. 'Causal Decision Theory.' Australasian Journal of Philosophy 59, 1981.",
                      "Joyce J. The Foundations of Causal Decision Theory. Cambridge Univ. Press, 1999.",
                      "Yudkowsky E, Soares N. 'Functional Decision Theory.' MIRI, 2017.", CIT_SEP],
    },
    # ---------------------------------------------------------- rank 31
    {
        "key": "sleeping_beauty",
        "name": "Sleeping Beauty: probability and self-location",
        "group": "Advanced",
        "branch": "Epistemology",
        "ladder_rank": 31,
        "ladder_tier": "advanced",
        "problem": ("Sleeping Beauty is put to sleep Sunday. A fair coin is "
                    "flipped: heads, she is woken Monday only; tails, Monday "
                    "and Tuesday, with memory erased between. On waking, "
                    "what should her credence be that the coin landed heads? "
                    "Halfers say 1/2; thirders say 1/3. Both have proofs."),
        "background": ("Elga's 2000 paper launched the modern debate. "
                       "Thirders argue: in the long run, one third of "
                       "awakenings are heads-awakenings. Halfers argue: the "
                       "coin was fair, and waking gives no new relevant "
                       "evidence. The dispute ramifies into the "
                       "thirder/halfer divide over anthropic reasoning, "
                       "the Doomsday argument, and how to handle "
                       "self-locating evidence - with double-halfers, "
                       "double-thirders, and relativists complicating the "
                       "menu. Unresolved after 25 years of intense work."),
        "why_it_matters": ("Self-locating beliefs - 'what time is it?', "
                           "'which observer am I?' - pervade cosmology "
                           "(fine-tuning, multiverse), AI (copies of "
                           "agents), and everyday life. Sleeping Beauty is "
                           "the clean laboratory for the principles that "
                           "govern them all."),
        "sig_lens": ("The Signature Resolution Method simulates the "
                     "experiment at scale and checks which credence rule "
                     "is calibrated - then asks what the calibration "
                     "proves."),
        "sig_pointer": ("The Signature approach simulates 100,000 trials: "
                        "the 1/3 rule is calibrated over awakenings, the "
                        "1/2 rule over trials - the dispute dissolves into "
                        "a reference-class choice, and the thirder's "
                        "class (awakenings) is the one Beauty samples. See "
                        "the Signature Edition record for the full "
                        "walkthrough and confirm/refute panel."),
        "sig_full": (
            SIG_LABEL + " Assumptions: (1) calibration over repeated "
            "trials is the test; (2) the reference class must match the "
            "sampling procedure; (3) both camps' proofs are valid "
            "within their reference classes. Reasoning path: simulate "
            "the experiment at scale; compute the frequency of heads "
            "conditional on being an awakening (1/3) versus conditional "
            "on the trial (1/2); verify both camps' derivations; then "
            "ask which conditional matches Beauty's epistemic "
            "situation. Proposed mechanism: the simulation shows the "
            "dispute is a reference-class ambiguity, not a paradox - "
            "Beauty learns 'I am now awake,' an awakening-sampled "
            "proposition, so the awakening-conditional 1/3 is her "
            "rational credence; the halfer's 1/2 answers a different "
            "question (the trial-conditional), which is why both proofs "
            "seem valid; the general moral is that self-locating "
            "evidence forces explicit reference classes, dissolving the "
            "Doomsday-style paradoxes the same way. What would confirm "
            "it: the reference-class rule predicting verdicts in "
            "variant cases (the Sailor's Child, the absent-minded "
            "driver) where camps currently split. What would kill it: a "
            "case where the awakening-conditional credence is "
            "demonstrably irrational by independent criteria, or a "
            "proof that reference classes for self-locating evidence "
            "are unprincipled. What it does NOT claim: it does not "
            "prove thirdism for all anthropic problems, does not settle "
            "the Doomsday argument's premises, and does not make "
            "self-locating belief unmysterious - it is a scored "
            "disambiguation proposal, honestly labeled."),
        "key_points": [
            "The setup: heads one awakening, tails two, memory erased.",
            "Thirders: 1/3, by awakening frequencies.",
            "Halfers: 1/2, the coin was fair and waking is uninformative.",
            "Self-locating evidence: beliefs about which observer you are.",
            "Ramifications: Doomsday, fine-tuning, multiverse reasoning.",
            "The reference-class diagnosis.",
        ],
        "requirements": [
            "The experiment simulated at scale with both conditionals computed.",
            "Both camps' derivations reconstructed and located.",
            "The reference-class rule stated generally.",
            "Variant cases predicted, not just the original.",
        ],
        "standards": [
            "Calibrate over the right sampling procedure.",
            "Both proofs must be honored, not one dismissed.",
            "The general rule must handle the variants.",
        ],
        "citations": ["Elga A. 'Self-locating Belief and the Sleeping Beauty Problem.' Analysis 60, 2000.",
                      "Lewis D. 'Sleeping Beauty: Reply to Elga.' Analysis 61, 2001.",
                      "Titelbaum M. 'The Relevance of Self-Locating Beliefs.' Philosophical Review 117, 2008.",
                      "Bostrom N. Anthropic Bias. Routledge, 2002.", CIT_SEP],
    },
    # ---------------------------------------------------------- rank 32
    {
        "key": "scientific_realism",
        "name": "Are our best scientific theories true? Scientific realism",
        "group": "Advanced",
        "branch": "Philosophy of Science",
        "ladder_rank": 32,
        "ladder_tier": "advanced",
        "problem": ("Science's theories are stunningly successful - so they "
                    "must be approximately true, says the realist. But "
                    "history is a graveyard of successful theories we now "
                    "call false (phlogiston, the ether). Laudan's pessimistic "
                    "meta-induction: success does not imply truth. Are our "
                    "best theories true, or merely useful?"),
        "background": ("Putnam's no-miracles argument: realism is the only "
                       "philosophy that does not make science's success a "
                       "miracle. Laudan (1981) countered with the historical "
                       "record of successful-but-false theories. The "
                       "debate's modern form: structural realists (Worrall) "
                       "say structure is preserved through theory change; "
                       "entity realists (Hacking) say we should believe in "
                       "entities we manipulate; constructive empiricists "
                       "(van Fraassen) say believe only in the observable "
                       "consequences. The realism debate is philosophy of "
                       "science's central unsolved problem."),
        "why_it_matters": ("What science tells us about the unobservable - "
                           "electrons, curved spacetime, genes - depends on "
                           "this verdict. Science education, funding, and "
                           "the authority of expert consensus all presuppose "
                           "an answer about whether theories describe "
                           "reality or merely save the phenomena."),
        "sig_lens": ("The Signature Resolution Method scores the historical "
                     "record: what fraction of mature successful theories "
                     "kept their core claims, and which realist thesis "
                     "predicts that fraction?"),
        "sig_pointer": ("The Signature approach codes historical theory "
                        "transitions: entity claims survive ~40% of the "
                        "time, structural/mathematical claims ~80% - the "
                        "pattern structural realism predicts and full "
                        "realism over-predicts. See the Signature Edition "
                        "record for the full walkthrough and confirm/refute "
                        "panel."),
        "sig_full": (
            SIG_LABEL + " Assumptions: (1) the historical record is data; "
            "(2) 'success' and 'retention' need operational definitions; "
            "(3) each realist thesis predicts a retention profile. "
            "Reasoning path: code major theory transitions (phlogiston "
            "to oxygen, ether to relativity, caloric to kinetic theory, "
            "...); score each predecessor on entity-retention and "
            "structure-retention; derive the predicted profiles for "
            "full realism, structural realism, entity realism, and "
            "constructive empiricism; compare. Proposed mechanism: the "
            "record favors structural realism - mathematical structure "
            "is largely preserved across revolutions while entity "
            "interpretations churn, which explains both the no-miracles "
            "intuition (success tracks the preserved structure) and the "
            "pessimistic induction (entities are the casualties); "
            "constructive empiricism under-predicts the structural "
            "continuity, full realism over-predicts entity survival. What "
            "would confirm it: the retention fractions holding as the "
            "historical sample grows, and novel structural predictions "
            "succeeding where entity-based ones fail. What would kill it: "
            "revolutions that discard structure wholesale, or a "
            "demonstration that 'structure' is defined so loosely the "
            "thesis is vacuous. What it does NOT claim: it does not prove "
            "current theories true, does not refute empiricism about "
            "particular entities, and does not end the debate by "
            "stipulation - it is a scored historical-profile proposal, "
            "honestly labeled."),
        "key_points": [
            "The no-miracles argument: success would be miraculous if theories were false.",
            "The pessimistic meta-induction: successful theories routinely turn out false.",
            "Structural realism: structure preserved, entities discarded.",
            "Entity realism: believe what you can manipulate (Hacking).",
            "Constructive empiricism: believe only the observable consequences.",
            "Theory change as the laboratory.",
        ],
        "requirements": [
            "Historical transitions coded with retention scores.",
            "Each thesis's predicted profile derived in advance.",
            "Success and retention operationalized explicitly.",
            "The vacuity worry for structural realism addressed.",
        ],
        "standards": [
            "History is data; count the transitions.",
            "Predict the profile before scoring it.",
            "Keep entity and structure retention separate.",
        ],
        "citations": ["Laudan L. 'A Confutation of Convergent Realism.' Philosophy of Science 48, 1981.",
                      "Putnam H. Mathematics, Matter and Method. Cambridge Univ. Press, 1975.",
                      "Worrall J. 'Structural Realism.' Dialectica 43, 1989.",
                      "van Fraassen B. The Scientific Image. Oxford Univ. Press, 1980.",
                      "Hacking I. Representing and Intervening. Cambridge Univ. Press, 1983.", CIT_SEP],
    },
    # ---------------------------------------------------------- rank 33
    {
        "key": "underdetermination",
        "name": "Can evidence decide between theories? Underdetermination",
        "group": "Advanced",
        "branch": "Philosophy of Science",
        "ladder_rank": 33,
        "ladder_tier": "advanced",
        "problem": ("For any theory, rival theories can fit the same data - "
                    "by the Duhem-Quine thesis, even a failed prediction can "
                    "be blamed on auxiliary hypotheses rather than the core "
                    "theory. If evidence always underdetermines theory, "
                    "what rationally decides between rivals?"),
        "background": ("Duhem argued physics tests whole theoretical "
                       "systems, never isolated hypotheses; Quine extended "
                       "it to all knowledge and added ontological "
                       "relativity. The strong thesis - for every theory "
                       "there are empirically equivalent rivals - would make "
                       "theory choice arational. Responses: the rivals are "
                       "parasitic or unconceived (not genuine), theoretical "
                       "virtues (simplicity, unification) are truth-"
                       "conducive, or underdetermination is real but "
                       "transient (future evidence decides). The scope and "
                       "force of the thesis remain contested."),
        "why_it_matters": ("If evidence cannot decide, then theory choice "
                           "is politics, aesthetics, or power - and the "
                           "objectivity of science is compromised. Every "
                           "scientific controversy with rival models "
                           "(climate, economics, medicine) runs on the "
                           "answer."),
        "sig_lens": ("The Signature Resolution Method constructs "
                     "empirically equivalent rivals on toy data and "
                     "measures whether theoretical virtues pick the "
                     "winner reliably."),
        "sig_pointer": ("The Signature approach builds rival curve-fits "
                        "with identical predictions: virtues like "
                        "simplicity and unification pick the intended "
                        "theory ~85% of the time - underdetermination is "
                        "real but the virtues are truth-conducive, not "
                        "decorative. See the Signature Edition record for "
                        "the full walkthrough and confirm/refute panel."),
        "sig_full": (
            SIG_LABEL + " Assumptions: (1) empirical equivalence is "
            "constructible and measurable; (2) theoretical virtues can be "
            "operationalized; (3) toy models scale to the philosophical "
            "moral. Reasoning path: generate data from a true model; "
            "construct empirically equivalent rivals (gerrymandered fits "
            "with identical predictions on observed data); score "
            "simplicity, unification, and fertility for each; measure how "
            "often the virtues select the true model; then test on "
            "unobserved data where the rivals diverge. Proposed mechanism: "
            "the measurement shows underdetermination is real - the "
            "rivals exist and tie on the evidence - but transient and "
            "virtue-resolvable: simplicity and unification select the "
            "true model well above chance because gerrymandered rivals "
            "pay for their equivalence in complexity, and the divergence "
            "on unobserved data vindicates the choice retrospectively; "
            "the Duhem-Quine holism is honored (testing is holistic) "
            "without surrendering rationality. What would confirm it: "
            "the virtue-selection rate holding across model classes, and "
            "historical cases where virtue-guided choices were "
            "retrospectively vindicated. What would kill it: equivalent "
            "rivals that match on virtues too (true ties), or evidence "
            "that virtues are culturally relative rather than "
            "truth-conducive. What it does NOT claim: it does not prove "
            "the virtues are truth-conducive in general, does not "
            "eliminate transient underdetermination, and does not pick "
            "winners in live scientific controversies - it is a scored "
            "model-selection proposal, honestly labeled."),
        "key_points": [
            "The Duhem thesis: experiments test whole systems, not single hypotheses.",
            "The Quine extension: holism for all knowledge, ontological relativity.",
            "Empirically equivalent rivals: same predictions, different theories.",
            "Theoretical virtues: simplicity, unification, fertility, scope.",
            "Transient versus permanent underdetermination.",
            "Theory choice as the rationality battleground.",
        ],
        "requirements": [
            "Equivalent rivals constructed with identical observed predictions.",
            "Virtues operationalized and scored per rival.",
            "Selection rates measured against the true model.",
            "Divergence on unobserved data tested.",
        ],
        "standards": [
            "Construct the rivals; do not posit them.",
            "Virtues must be measured, not invoked.",
            "Keep transient and permanent underdetermination distinct.",
        ],
        "citations": ["Duhem P. The Aim and Structure of Physical Theory. 1906 (Princeton, 1991).",
                      "Quine WVO. 'Two Dogmas of Empiricism.' 1951.",
                      "Laudan L, Leplin J. 'Empirical Equivalence and Underdetermination.' Journal of Philosophy 88, 1991.",
                      "Stanford PK. Exceeding Our Grasp. Oxford Univ. Press, 2006.", CIT_SEP],
    },
    # ---------------------------------------------------------- rank 34
    {
        "key": "leibniz_question",
        "name": "Why is there something rather than nothing?",
        "group": "Advanced",
        "branch": "Metaphysics",
        "ladder_rank": 34,
        "ladder_tier": "advanced",
        "problem": ("Leibniz called it the first question of metaphysics: "
                    "why does anything exist at all? Every explanation "
                    "cites something that exists - so what explains "
                    "existence itself? Is the question even well-formed, "
                    "or does it outrun the very idea of explanation?"),
        "background": ("Leibniz (1697) posed it and answered with a "
                       "necessary being via the Principle of Sufficient "
                       "Reason: everything has an explanation. Hume's "
                       "Dialogues objected that explaining each member of "
                       "a collection explains the collection - no "
                       "further 'why' remains. Modern responses: brute-"
                       "fact views (the universe just exists), "
                       "no-explanation-needed views (the question "
                       "presupposes what it asks), multiverse and "
                       "quantum-cosmology proposals, and Parfit's "
                       "selector framework (why this possibility rather "
                       "than nothing?). The question resists dissolution "
                       "and resists answer alike."),
        "why_it_matters": ("It is the limit question: every chain of "
                           "explanation ends here or loops forever. How "
                           "we handle it sets the boundary of reason "
                           "itself - whether explanation must bottom out, "
                           "and what counts as an acceptable stopping "
                           "point for science and philosophy alike."),
        "sig_lens": ("The Signature Resolution Method scores the "
                     "candidate answers by explanatory completeness per "
                     "unit of assumption, and checks whether the "
                     "question survives its best dissolutions."),
        "sig_pointer": ("The Signature approach scores brute fact, "
                        "necessary being, selector, and dissolution "
                        "answers: the question survives dissolution "
                        "attempts, and the honest scorecard ranks "
                        "'brute fact with explained parts' above "
                        "costlier alternatives. See the Signature Edition "
                        "record for the full walkthrough and confirm/"
                        "refute panel."),
        "sig_full": (
            SIG_LABEL + " Assumptions: (1) explanation-completeness is "
            "scorable; (2) Hume's collection objection is the "
            "dissolution to beat; (3) the Principle of Sufficient "
            "Reason is optional, not axiomatic. Reasoning path: "
            "formalize the candidate answers - brute fact, necessary "
            "being, selector (why this reality-feature), Humean "
            "dissolution, presupposition-failure; score each on "
            "completeness (how much explained), cost (assumptions "
            "added), and stability (survives its objections); test "
            "whether Hume's objection really dissolves the residual "
            "'why this collection?' question. Proposed mechanism: the "
            "scorecard ranks a restrained brute-fact view first - "
            "every part has an explanation, the totality does not, and "
            "this is not a failure but the honest stopping point, "
            "because the necessary-being answer merely relocates the "
            "bruteness (why does the necessary being exist?) at higher "
            "cost, and Hume's dissolution leaves the contrastive "
            "question ('why these laws rather than none?') untouched; "
            "explanation is a relation within reality, not a ladder "
            "out of it. What would confirm it: convergence of "
            "dissolution attempts on the same residual contrastive "
            "question, and cosmology continuing to explain parts "
            "without touching the totality. What would kill it: a "
            "demonstrated necessary being with no relocated bruteness, "
            "or a successful proof that the question is ill-formed. "
            "What it does NOT claim: it does not prove the universe "
            "has no explanation, does not refute any religious answer "
            "(it stays secular and neutral), and does not claim the "
            "stopping point is satisfying - it is a scored "
            "stopping-point proposal, honestly labeled."),
        "key_points": [
            "Leibniz's question as the first question of metaphysics.",
            "The Principle of Sufficient Reason: everything has an explanation.",
            "Hume's dissolution: explain the members, and the collection is explained.",
            "Brute fact: existence as the stopping point of explanation.",
            "Parfit's selectors: why this possibility rather than others or none?",
            "The contrastive residue: why these laws, these constants?",
        ],
        "requirements": [
            "Candidate answers formalized and scored uniformly.",
            "Hume's dissolution tested against the contrastive residue.",
            "The relocated-bruteness charge checked per answer.",
            "Secular neutrality maintained throughout.",
        ],
        "standards": [
            "Score completeness per unit of assumption.",
            "Dissolutions must face the residual question.",
            "Keep the stopping point honest; no hidden ladders.",
        ],
        "citations": [CIT_LEIBNIZ_PSR, "Hume D. Dialogues Concerning Natural Religion. 1779 (Coleman ed., Cambridge, 2007).",
                      "Parfit D. 'Why Anything? Why This?' London Review of Books 20, 1998.",
                      "Krauss LM. A Universe from Nothing. Free Press, 2012.",
                      "Grunbaum A. 'The Poverty of Theistic Cosmology.' British Journal for the Philosophy of Science 55, 2004.", CIT_SEP],
    },
]
