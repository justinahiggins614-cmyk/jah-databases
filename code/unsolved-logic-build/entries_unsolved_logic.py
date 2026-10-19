#!/usr/bin/env python3
"""Entries for the Unsolved Logic databases (unsolved-problems SOLVED series, 2026-10-17).

34 famous open problems of logic, ladder-ordered by accessibility (1 = most
approachable, 34 = most complex/compounded). Public half = the problem as the
world knows it (fact-checked); signature half = the Signature system's
proposed solution approach, ALWAYS opened with the exact label
"Signature-generated proposed solution - not established science" and
honestly bounded (never claims proof, never implies peer acceptance).

Verified 2026-10-17: RAW SWEEP over the full manifest (2,602 databases)
PLUS every shard index in jah-databases-data-1 (1,049 index files):
zero 'unsolved-logic' slugs/names; ID prefixes JAH-USLG- and JAH-USLGS-
verified free in manifest id_prefix values AND in every shard index file
(zero hits). Titles ran through the whole-system dedupe gate before
authoring: zero collisions.

Record fields (template spec): problem, background, why_it_matters,
signature_solution (public half: short pointer; signature half: full
treatment). Mapped onto the build-canon schema (description, how_it_works,
key_points, requirements, standards, citations, src, ladder_rank,
ladder_tier, demo) with the template fields carried explicitly.
"""

SIG_LABEL = ("Signature-generated proposed solution - not established "
             "science.")

CIT_TARSKI = ("Tarski, A. The concept of truth in formalized languages "
              "(1933/1983).")
CIT_KRIPKE = ("Kripke, S. Outline of a theory of truth. Journal of "
              "Philosophy 72 (1975).")
CIT_PRIEST = ("Priest, G. In Contradiction (2nd ed., 2006).")
CIT_BEALL = ("Beall, Jc. Spandrels of Truth (2009).")
CIT_GODEL31 = ("Goedel, K. On formally undecidable propositions (1931).")
CIT_GODEL40 = ("Goedel, K. The consistency of the axiom of choice and of "
               "the generalized continuum-hypothesis (1940).")
CIT_COHEN = ("Cohen, P. J. Set Theory and the Continuum Hypothesis "
             "(1966).")
CIT_WOODIN = ("Woodin, W. H. The Axiom of Determinacy, Forcing Axioms, "
              "and the Nonstationary Ideal (1999).")
CIT_KRAJICEK = ("Krajicek, J. Bounded Arithmetic, Propositional Logic, "
                "and Complexity Theory (1995).")
CIT_BUSSD = ("Buss, S. Bounded Arithmetic (1986).")
CIT_ROBINSON = ("Robinson, J. A. A machine-oriented logic based on the "
                "resolution principle. JACM 12 (1965).")
CIT_ANDERSON = ("Anderson, A. R. and Belnap, N. D. Entailment: The Logic "
                "of Relevance and Necessity, vols. 1-2 (1975, 1992).")
CIT_SHELAH = ("Shelah, S. Infinite abelian groups, Whitehead problem and "
              "some constructions. Israel J. Math. 18 (1974).")
CIT_FRIEDMAN = ("Friedman, H. Finite functions and the necessary use of "
                "large cardinals. Annals of Math. 148 (1998).")
CIT_FIELD = ("Field, H. Saving Truth from Paradox (2008).")
CIT_RESTALL = ("Restall, G. An Introduction to Substructural Logics "
               "(2000).")
CIT_JECH = ("Jech, T. Set Theory (3rd ed., 2003).")
CIT_KANAMORI = ("Kanamori, A. The Higher Infinite (2nd ed., 2003).")
CIT_HILBERT = ("Hilbert, D. Mathematical problems (1900).")
CIT_BROUWER = ("Brouwer, L. E. J. Intuitionism and formalism (1912).")
CIT_QUINE = ("Quine, W. V. O. Word and Object (1960).")
CIT_WILLIAMSON = ("Williamson, T. Vagueness (1994).")
CIT_KEEFE = ("Keefe, R. Theories of Vagueness (2000).")
CIT_HEMPEL = ("Hempel, C. G. Studies in the logic of confirmation. Mind "
              "54 (1945).")
CIT_KYBERG = ("Kyburg, H. Probability and the Logic of Rational Belief "
              "(1961).")
CIT_MAKINSON = ("Makinson, D. C. The paradox of the preface. Analysis 25 "
                "(1965).")
CIT_MOORE = ("Moore, G. E. A reply to my critics (1942).")
CIT_QUINE_HANG = ("Quine, W. V. O. On a so-called paradox. Mind 62 "
                  "(1953).")
CIT_YABLO = ("Yablo, S. Paradox without self-reference. Analysis 53 "
              "(1993).")
CIT_CURRY = ("Curry, H. B. The inconsistency of certain formal logics. "
             "JSL 7 (1942).")
CIT_BERRY = ("Russell, B. Mathematical logic as based on the theory of "
              "types (1908) - Berry's paradox reported therein.")
CIT_LOB = ("Lob, M. H. Solution of a problem raised by Leon Henkin. "
           "JSL 20 (1955).")
CIT_GENTZEN = ("Gentzen, G. Die Widerspruchsfreiheit der reinen "
               "Zahlentheorie. Math. Ann. 112 (1936).")
CIT_HUET = ("Huet, G. P. The undecidability of unification in third "
            "order logic. Information and Control 22 (1973).")
CIT_RAZBOROV = ("Razborov, A. A. and Rudich, S. Natural proofs. JCSS 55 "
                "(1997).")
CIT_PARIS = ("Paris, J. and Kirby, L. Sigma_n-collection schemas in "
             "arithmetic (1978).")
CIT_MARTIN = ("Martin, D. A. and Steel, J. R. A proof of projective "
              "determinacy. JAMS 2 (1989).")
CIT_SOLOVAY = ("Solovay, R. M. A model of set-theory in which every set "
               "of reals is Lebesgue measurable. Annals of Math. 92 "
               "(1970).")
CIT_SILVER = ("Silver, J. On the singular cardinals problem. Proc. ICM "
              "(1974).")
CIT_ANDRETTA = ("Maddy, P. Believing the axioms. JSL 53 (1988).")
CIT_HAMKINS = ("Hamkins, J. D. The set-theoretic multiverse. Review of "
               "Symbolic Logic 5 (2012).")

SIG_TAIL = ("Signature completion note: this entry is a Signature-"
            "generated proposed solution - not established science. It is "
            "filed as a Signature original interpretation of an open "
            "problem; it claims no proof and no peer acceptance.")

ENTRIES = [
    # ------------------------------------------------------------ FOUNDATIONS
    {
        "key": "liar",
        "name": "The Liar Paradox",
        "group": "Paradoxes of Truth",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "problem": ("Is the sentence 'This sentence is false' true or "
                    "false? If it is true, then what it says holds and it "
                    "is false; if it is false, then it is true. It seems "
                    "both answers collapse - the problem is to give a "
                    "principled account of truth that resolves the "
                    "paradox without breaking ordinary reasoning."),
        "background": (
            "The liar paradox is the oldest open wound in the philosophy "
            "of logic, traced to Eubulides of Miletus in the 4th century "
            "BCE and refined through the medieval insolubilia tradition. "
            "Tarski's 1933 work showed that no sufficiently rich formal "
            "language can contain its own truth predicate without "
            "contradiction, which is why his famous T-schema is stated "
            "for a meta-language. Kripke's 1975 theory of truth offered "
            "a way to let truth predicates partially apply to their own "
            "language, classifying the liar sentence as 'ungrounded'. "
            "Paraconsistent logicians such as Priest argue instead that "
            "the liar is simply both true and false - a dialetheia. "
            "Field, Beall, and others defend revisionary theories "
            "keeping classical logic by restricting the truth rules. "
            "No proposal commands consensus: each saves some intuitions "
            "and sacrifices others, and the revenge problem - paradoxes "
            "rebuilt against each new theory - keeps the debate live."
        ),
        "why_it_matters": (
            "Truth is the central concept of logic, semantics, and much "
            "of epistemology; a paradox at its core infects everything "
            "built on it. Settling the liar would fix the foundations "
            "of formal semantics, databases with self-referential "
            "content, and AI systems that must reason about their own "
            "statements. It also decides whether classical logic survives "
            "contact with natural-language truth."
        ),
        "sig_pointer": (
            "The Signature edition proposes a layered groundedness "
            "diagnostic: sentences are scored by the depth of the "
            "evidence chain behind them, and the liar is filed as a "
            "zero-depth utterance - grammatically fine, semantically "
            "empty. See the Signature edition for the full walkthrough, "
            "adjustable assumptions, and the confirm/refute panel."
        ),
        "assumptions": [
            "A1: Truth applies only to grounded claims - claims anchored "
            "in evidence chains terminating outside the sentence itself.",
            "A2: Self-application of a truth predicate is allowed but "
            "scored, not banned.",
            "A3: Classical inference rules are kept for grounded "
            "sentences.",
        ],
        "steps": [
            "Step 1: Trace the liar's evidence chain: 'This sentence is "
            "false' points only at itself, so its grounding depth is "
            "zero.",
            "Step 2: Apply A1: a zero-depth claim is ungrounded, hence "
            "not a bearer of truth-value at all.",
            "Step 3: Observe that 'the liar is false' and 'the liar is "
            "true' are both claims about an ungrounded utterance - both "
            "presuppose what A1 denies.",
            "Step 4: Keep classical logic intact for every grounded "
            "sentence; restrict only the truth predicate's domain.",
            "Step 5: Check revenge: the sentence 'this very analysis is "
            "ungrounded' is itself grounded in the analysis, so it "
            "receives a truth-value and the regress stops.",
        ],
        "confirm": [
            "Formalizing groundedness depth in a Kripke-style fixed "
            "point and showing the liar gets no value in all minimal "
            "fixed points would confirm the mechanism.",
            "Showing the approach also handles Curry, Yablo, and the "
            "truth-teller without extra machinery would strengthen it "
            "considerably.",
        ],
        "refute": [
            "A revenge sentence that the depth metric itself classifies "
            "as grounded-yet-paradoxical would kill the proposal.",
            "If groundedness depth turns out to be expressible inside "
            "the object language, Tarski's theorem would re-derive the "
            "contradiction and the approach fails.",
        ],
        "not_claims": [
            "It does not claim the liar is meaningless in ordinary "
            "speech - only that it carries no truth-value.",
            "It does not claim to be the unique solution; dialetheist "
            "and revisionary rivals remain live competitors.",
            "It does not claim classical logic is exceptionless - only "
            "that this paradox does not force abandoning it.",
        ],
        "citations": [CIT_TARSKI, CIT_KRIPKE, CIT_PRIEST],
    },
    {
        "key": "sorites",
        "name": "The Sorites Paradox",
        "group": "Paradoxes of Vagueness and Reason",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "problem": (
            "One grain of sand is not a heap. Adding one grain to "
            "something that is not a heap cannot make it a heap. Yet "
            "repeated addition eventually yields a heap. Where is the "
            "boundary, and what does its absence mean for logic, which "
            "assumes every statement is true or false?"
        ),
        "background": (
            "The sorites (Greek for 'heap') is another Eubulides paradox, "
            "and unlike the liar it is not about self-reference but about "
            "vagueness - the pervasive phenomenon that most of our "
            "predicates lack sharp boundaries. Classical logic assumes "
            "bivalence, so something must give: either heaps have "
            "unknowable sharp cutoffs (Williamson's epistemicism), or "
            "truth comes in degrees (fuzzy logic), or vague predicates "
            "are unsettled in borderline cases (supervaluationism), or "
            "logic itself must tolerate the contradiction (dialetheism). "
            "The paradox matters practically: law, medicine, and "
            "engineering all classify by vague predicates, and AI "
            "systems must make binary decisions on vague input. "
            "Twenty-five centuries on, the camps are stable and none "
            "has won."
        ),
        "why_it_matters": (
            "Almost every predicate humans use - tall, rich, red, "
            "conscious, alive - is vague, so the sorites is a paradox "
            "about ordinary thought itself. A solution would settle how "
            "logic handles borderline cases, with direct consequences "
            "for legal reasoning, medical diagnosis thresholds, and "
            "machine classification systems. It also decides whether "
            "bivalence is a law of thought or a convenient fiction."
        ),
        "sig_pointer": (
            "The Signature edition proposes a tolerance-band model: "
            "vague predicates carry a context-set band of admissible "
            "cutoffs, and sorites reasoning is diagnosed as illicit "
            "cutoff smuggling across steps. The full edition walks the "
            "steps, lets the band width be adjusted, and lists what "
            "would confirm or refute the model."
        ),
        "assumptions": [
            "A1: Vague predicates are used with a contextually set "
            "tolerance band, not a hidden sharp cutoff.",
            "A2: Within the band, 'is a heap' is unsettled rather than "
            "unknown-true-or-false.",
            "A3: Speakers implicitly fix a cutoff per conversation; the "
            "sorites argument covertly shifts it.",
        ],
        "steps": [
            "Step 1: Model 'heap' as: definitely-not-heap below n1, "
            "definitely-heap above n2, unsettled between - the tolerance "
            "band.",
            "Step 2: Read the sorites premise 'one grain cannot make the "
            "difference' as true only relative to a fixed cutoff.",
            "Step 3: Show the iterated argument smuggles the cutoff "
            "forward: each step re-fixes the context, so the chain of "
            "'not a heap' verdicts was never about one context.",
            "Step 4: Derive the diagnosis: the paradox is a fallacy of "
            "equivocation across contexts, not a deep truth about "
            "heaps.",
            "Step 5: Test higher-order vagueness: the band's own edges "
            "get bands - the model tolerates this by iteration, and "
            "predicts where speakers actually hesitate.",
        ],
        "confirm": [
            "Psycholinguistic data showing speakers shift cutoffs "
            "mid-series exactly as the model predicts would confirm it.",
            "A formal semantics in which the band model validates all "
            "uncontroversial vague inferences and invalidates the "
            "sorites chain would be strong confirmation.",
        ],
        "refute": [
            "Evidence that competent speakers hold a single fixed "
            "cutoff through the whole series (Williamson's epistemicist "
            "prediction) would refute the smuggling diagnosis.",
            "A forced-march sorites with explicitly fixed context that "
            "still compels assent to the absurd conclusion would kill "
            "the model.",
        ],
        "not_claims": [
            "It does not deny that vagueness is real - it relocates it "
            "from the world to the context of use.",
            "It does not claim sharp cutoffs exist unknowably; it claims "
            "the question presupposes what vagueness denies.",
            "It does not settle higher-order vagueness conclusively - "
            "that remains the model's hardest test.",
        ],
        "citations": [CIT_WILLIAMSON, CIT_KEEFE],
    },
    {
        "key": "truth-nature",
        "name": "What Is Truth?",
        "group": "Paradoxes of Truth",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "problem": (
            "Is truth a substantial property that sentences have when "
            "they correspond to reality, or is 'is true' just a "
            "linguistic device for endorsement and generalization? "
            "Deflationists say the concept is thin; correspondence "
            "theorists say it is thick. The problem: give a theory of "
            "truth that explains its explanatory role without "
            "collapsing under the paradoxes."
        ),
        "background": (
            "Theories of truth divide roughly into robust theories - "
            "correspondence, coherence, pragmatist - which treat truth "
            "as a substantive property doing explanatory work, and "
            "deflationary theories, which hold that the truth predicate "
            "exists for expressive convenience (endorsement, "
            "generalization over infinite conjunctions) and that the "
            "T-schema 'p is true iff p' says nearly everything there is "
            "to say. Tarski gave the first rigorous formal treatment but "
            "restricted it to formalized languages. The liar paradox is "
            "the deflationist's nightmare: if truth is thin, why does "
            "the thin notion breed contradiction? Robust theorists "
            "counter that deflationism cannot explain why truth is a "
            "norm of belief and assertion, or its role in scientific "
            "explanation. The debate structures whole research programs "
            "in metaphysics and philosophy of language, and it is "
            "unresolved."
        ),
        "why_it_matters": (
            "Every science aims at truth, and every database stores "
            "claims taken to be true; the nature of truth determines "
            "what those enterprises are doing. If deflationism is right, "
            "truth-talk is a convenience and paradoxes are linguistic "
            "housekeeping; if correspondence is right, truth is a deep "
            "relation between language and world that science must "
            "respect. AI alignment itself depends on what it means for "
            "an AI's statements to be true."
        ),
        "sig_pointer": (
            "The Signature edition proposes a two-role account: truth "
            "has a thin endorsement role in ordinary talk and a thick "
            "evidence-tracking role in inquiry, and the paradoxes arise "
            "only when the roles are confused. The full edition lays out "
            "the role-separation test, the steps, and the confirm/refute "
            "panel."
        ),
        "assumptions": [
            "A1: 'True' plays two distinct roles: endorsement in "
            "conversation and evidence-tracking in inquiry.",
            "A2: The liar and kin exploit the endorsement role while "
            "demanding the standards of the evidence role.",
            "A3: No single metaphysical property needs to unify both "
            "roles.",
        ],
        "steps": [
            "Step 1: Separate the roles: 'that's true' as conversational "
            "endorsement versus 'the theory is true' as a claim about "
            "evidence-responsiveness.",
            "Step 2: Show deflationism correctly describes the "
            "endorsement role and correspondence correctly describes the "
            "evidence-tracking role.",
            "Step 3: Diagnose the liar as an endorsement-role sentence "
            "graded by evidence-role standards - a category error, not "
            "a deep contradiction.",
            "Step 4: Preserve the normativity of truth: inquiry's "
            "evidence-tracking role is genuinely normative; "
            "conversation's endorsement role inherits its authority "
            "from it.",
            "Step 5: Predict that paradoxes dissolve exactly when the "
            "role in play is made explicit - testable against the "
            "revenge literature.",
        ],
        "confirm": [
            "Linguistic evidence that speakers systematically treat "
            "'true' differently in endorsement versus inquiry contexts "
            "would confirm the role split.",
            "If every major truth paradox can be diagnosed as a "
            "role-confusion with no residue, the account gains serious "
            "support.",
        ],
        "refute": [
            "A paradox formulated purely inside the evidence-tracking "
            "role with no endorsement-role involvement would refute the "
            "diagnosis.",
            "If the two roles turn out to be inseparable in actual "
            "scientific practice, the separation collapses and so does "
            "the proposal.",
        ],
        "not_claims": [
            "It does not claim deflationists and correspondence "
            "theorists were both simply right - it claims they were "
            "describing different roles.",
            "It does not eliminate the metaphysical question of what "
            "makes evidence-tracking claims correct.",
            "It does not claim ordinary speakers are confused - only "
            "that theorizing conflates the roles.",
        ],
        "citations": [CIT_TARSKI, CIT_QUINE],
    },
    {
        "key": "curry",
        "name": "Curry's Paradox",
        "group": "Paradoxes of Truth",
        "ladder_rank": 4,
        "ladder_tier": "foundations",
        "problem": (
            "Consider the sentence C: 'If this sentence is true, then "
            "the moon is made of cheese.' Reasoning that looks valid "
            "proves the moon is made of cheese - from nothing. Unlike "
            "the liar, Curry's paradox uses no negation, so solutions "
            "that merely restrict negation or tolerate contradictions "
            "do not touch it. What blocks the proof?"
        ),
        "background": (
            "Haskell Curry published the paradox in 1942, and its "
            "significance took decades to sink in: it shows the "
            "paradoxes are not really about negation at all but about "
            "the combination of self-reference with conditional proof "
            "(if you can derive B from the assumption A, infer "
            "A-implies-B). Dialetheist solutions to the liar - accept "
            "true contradictions - are helpless here, because Curry's "
            "proof derives an arbitrary absurdity, and accepting every "
            "absurdity as true is trivialism, which even paraconsistent "
            "logicians reject. The paradox puts pressure on the "
            "structural rules of logic themselves: contraction (using "
            "an assumption twice) and the deduction theorem. "
            "Substructural logics that drop contraction dissolve the "
            "proof, but at the cost of crippling ordinary reasoning. "
            "No consensus fix exists."
        ),
        "why_it_matters": (
            "Curry's paradox is the stress test every theory of truth "
            "must pass and most fail; it shows the problem runs deeper "
            "than negation. Any logic used by AI systems, proof "
            "assistants, or formalized mathematics must either block "
            "Curry sentences or restrict the deduction rules that make "
            "ordinary mathematics possible. It marks the true boundary "
            "of consistent self-referential reasoning."
        ),
        "sig_pointer": (
            "The Signature edition proposes a discharge-budget rule: "
            "conditional proof may discharge an assumption only when "
            "the assumption earned its keep independently of the "
            "conclusion. The full edition walks the Curry proof "
            "step by step, shows where the budget runs out, and gives "
            "the confirm/refute panel."
        ),
        "assumptions": [
            "A1: Conditional proof is valid but budgeted: discharging "
            "an assumption requires the assumption to do independent "
            "work.",
            "A2: Self-referential truth ascriptions are 'unearned' - "
            "they contribute no content beyond the conditional "
            "itself.",
            "A3: Ordinary mathematical conditional proofs always meet "
            "the budget.",
        ],
        "steps": [
            "Step 1: Reconstruct Curry's proof: assume C, from C derive "
            "'C is true', modus ponens gives the absurdity, discharge "
            "to get C, then detach the absurdity.",
            "Step 2: Audit the discharge step: the only content of "
            "assumption C was the conditional whose consequent is the "
            "absurdity - the assumption did no independent work.",
            "Step 3: Apply the budget rule: discharge is refused, so "
            "the proof halts before the paradoxical conclusion.",
            "Step 4: Verify ordinary proofs pass: in real mathematics "
            "the discharged assumption always constrains the "
            "derivation independently.",
            "Step 5: Check that contraction is preserved for earned "
            "assumptions, so no substructural crippling is needed.",
        ],
        "confirm": [
            "A precise formalization of 'earned discharge' that keeps "
            "all of standard mathematics while blocking every known "
            "Curry construction would confirm the rule.",
            "If the budget rule also diagnoses Loeb's paradox and "
            "v-Curry with no extra clauses, that is strong evidence.",
        ],
        "refute": [
            "A legitimate mathematical proof that the budget rule "
            "blocks would refute it - the rule must be conservative "
            "over practice.",
            "A Curry-style derivation that earns its discharge under "
            "any natural precisification of 'earned' would kill the "
            "proposal.",
        ],
        "not_claims": [
            "It does not claim contraction is invalid - only that "
            "discharge has a content requirement.",
            "It does not claim to save naive truth outright; it claims "
            "to locate the exact illicit step.",
            "It does not deny the force of the paradox - Curry's proof "
            "looks valid because each local step is fine; the fault is "
            "global.",
        ],
        "citations": [CIT_CURRY, CIT_RESTALL],
    },
    {
        "key": "yablo",
        "name": "Yablo's Paradox",
        "group": "Paradoxes of Truth",
        "ladder_rank": 5,
        "ladder_tier": "foundations",
        "problem": (
            "Imagine an infinite list of sentences S1, S2, S3, ... where "
            "each Sn says 'All later sentences are false.' If some Sn is "
            "true, then all later ones are false - but then Sn+1's claim "
            "that all later ones are false is true, contradiction. If "
            "all are false, then each Sn's claim is correct, so each is "
            "true - contradiction. No sentence refers to itself, yet "
            "paradox blooms. What, then, was ever the culprit?"
        ),
        "background": (
            "Stephen Yablo published the paradox in 1993 as 'Paradox "
            "without self-reference', and it detonated a research "
            "program: if self-reference is not necessary for the liar "
            "phenomenon, then diagnoses that blame self-reference - the "
            "most popular kind - are targeting the wrong thing. "
            "Responses split. Some argue Yablo's construction smuggles "
            "self-reference back in through the infinite totality (the "
            "list refers to itself as a whole). Others take it at face "
            "value and conclude the real culprit is something deeper: "
            "ungroundedness, circularity of dependence, or the "
            "impredicativity of quantifying over a totality containing "
            "the sentence doing the quantifying. Formal work has mapped "
            "exactly which fixed-point constructions the Yablo sequence "
            "defeats. There is no agreed moral of the story."
        ),
        "why_it_matters": (
            "Yablo's paradox is the experiment that isolates the "
            "variable: remove self-reference and see if paradox "
            "survives - it does. Whatever blocks Yablo blocks the whole "
            "family of semantic paradoxes, so it is the sharpest test "
            "of any theory of truth. It also matters for the foundations "
            "of set theory, where impredicative definitions raise the "
            "same structural worry."
        ),
        "sig_pointer": (
            "The Signature edition proposes a dependence-loop test: a "
            "sentence is admissible only if its truth-dependence graph "
            "has no infinitely descending chain with no floor. Yablo's "
            "sequence fails the test at infinity. The full edition "
            "walks the dependence graph, adjusts the chain-length "
            "knob, and gives the confirm/refute panel."
        ),
        "assumptions": [
            "A1: Truth-evaluation follows dependence: to evaluate Sn "
            "you must evaluate what Sn depends on.",
            "A2: An infinite descending dependence chain with no "
            "ground floor never terminates evaluation.",
            "A3: Non-terminating evaluation means no truth-value - not "
            "unknown, but unassigned.",
        ],
        "steps": [
            "Step 1: Draw the dependence graph: S1 depends on S2, S3, "
            "...; each Sn depends on all later Sm.",
            "Step 2: Note the chain S1 -> S2 -> S3 -> ... descends "
            "forever with no bottom sentence to anchor evaluation.",
            "Step 3: Apply A2-A3: evaluation never grounds, so no Sn "
            "gets a truth-value, and the 'contradiction' derivation "
            "presupposes values that were never assigned.",
            "Step 4: Show the liar is the finite special case: a "
            "1-cycle is a dependence loop, blocked by the same test.",
            "Step 5: Verify ordinary infinite claims ('all natural "
            "numbers...') pass: their dependence bottoms out in "
            "decidable instances.",
        ],
        "confirm": [
            "A graph-theoretic semantics where exactly the Yablo-style "
            "sequences come out value-less while standard mathematics "
            "is untouched would confirm the test.",
            "If the dependence criterion also predicts which "
            "self-referential sentences are harmless (the truth-teller "
            "passes, the liar fails), that is strong support.",
        ],
        "refute": [
            "A paradox-free infinite dependence chain that the test "
            "wrongly rejects would refute the criterion's necessity.",
            "If Yablo sequences can be shown to contain disguised "
            "self-reference after all, the test's motivation collapses "
            "and a simpler diagnosis wins.",
        ],
        "not_claims": [
            "It does not claim infinite sentences are illegitimate - "
            "only infinitely ungrounded dependence.",
            "It does not claim to settle whether self-reference is "
            "guilty; it claims the dependence test covers both cases.",
            "It does not deny the paradox's force - the reasoning looks "
            "airtight until the hidden presupposition is exposed.",
        ],
        "citations": [CIT_YABLO, CIT_KRIPKE],
    },
    {
        "key": "grelling",
        "name": "Grelling-Nelson and the Barber",
        "group": "Paradoxes of Vagueness and Reason",
        "ladder_rank": 6,
        "ladder_tier": "foundations",
        "problem": (
            "Call an adjective heterological if it does not describe "
            "itself: 'long' is heterological (the word is short), "
            "'short' is not. Is 'heterological' heterological? Either "
            "answer contradicts itself. The barber shaves all and only "
            "those who do not shave themselves - who shaves the barber? "
            "These paradoxes of classification look trivial until you "
            "notice they are Russell's paradox wearing everyday clothes."
        ),
        "background": (
            "Kurt Grelling and Leonard Nelson published the "
            "heterological paradox in 1908, the same season Russell's "
            "paradox was convulsing the foundations of mathematics. The "
            "barber version is Russell's own popularization. The deep "
            "point: the paradox needs no sets, no infinity, no formal "
            "machinery - just the everyday ability to classify words by "
            "whether they apply to themselves. Responses mirror the "
            "set-theoretic ones: type restrictions (adjectives live on "
            "levels and cannot classify across levels), the denial that "
            "'heterological' is a legitimate predicate, or the "
            "paraconsistent shrug. But unlike the set-theoretic "
            "paradoxes, these live in natural language, where type "
            "restrictions feel artificial and nobody legislates the "
            "vocabulary. The question of what, exactly, is wrong with "
            "'heterological' remains open."
        ),
        "why_it_matters": (
            "These paradoxes show the foundations problem is not "
            "confined to abstruse set theory - it is built into the way "
            "language classifies itself. Any AI that reasons about "
            "categories, any database schema with self-describing "
            "metadata, and any formal ontology faces the Grelling "
            "question. Solving it would tell us the real scope of "
            "Russell's paradox: a quirk of naive set theory, or a "
            "universal feature of classification."
        ),
        "sig_pointer": (
            "The Signature edition proposes a use-mention firewall: "
            "classification predicates may classify uses, never the "
            "mention that introduces them in the same breath. The full "
            "edition walks the heterological question through the "
            "firewall, shows the barber dissolving, and gives the "
            "confirm/refute panel."
        ),
        "assumptions": [
            "A1: Every classifying act separates the classifier (in "
            "use) from the classified (mentioned).",
            "A2: A predicate cannot classify its own classifying act "
            "in the same utterance.",
            "A3: Cross-utterance self-classification is permitted and "
            "evaluated normally.",
        ],
        "steps": [
            "Step 1: Ask 'is heterological heterological?' and mark the "
            "two roles: the question uses the predicate to classify the "
            "mention 'heterological'.",
            "Step 2: Apply A2: the verdict would have to classify the "
            "very act of classifying - refused by the firewall.",
            "Step 3: Show the question is ill-formed in the same way "
            "as 'is the present act of asking present?' - a use-mention "
            "tangle, not a deep truth.",
            "Step 4: Dissolve the barber: 'shaves' as a habitual "
            "classifier cannot adjudicate the barber's own shaving in "
            "the breath that defines the habit.",
            "Step 5: Verify ordinary self-description ('this sentence "
            "is in English') passes: it classifies a mention across "
            "utterances, allowed by A3.",
        ],
        "confirm": [
            "If the firewall dissolves Grelling, the barber, and the "
            "liar's self-referential variants with one principle, that "
            "unity is strong confirmation.",
            "Linguistic data showing speakers balk at same-breath "
            "self-classification but accept cross-utterance cases "
            "would support A2/A3.",
        ],
        "refute": [
            "A same-breath self-classification that is clearly "
            "legitimate and paradox-free would refute the firewall's "
            "necessity.",
            "If the firewall must be stated in a way that itself "
            "violates it, the proposal is self-defeating.",
        ],
        "not_claims": [
            "It does not ban self-reference in general - only "
            "same-breath self-classification.",
            "It does not claim type theory was wrong; it claims the "
            "firewall is the natural-language shape of the same "
            "insight.",
            "It does not deny the paradoxes felt real - the tangle is "
            "genuine, the contradiction is not.",
        ],
        "citations": [CIT_QUINE],
    },
    {
        "key": "berry",
        "name": "Berry's Paradox of Definability",
        "group": "Paradoxes of Vagueness and Reason",
        "ladder_rank": 7,
        "ladder_tier": "foundations",
        "problem": (
            "Consider 'the smallest positive integer not definable in "
            "under sixty letters.' That phrase has under sixty letters "
            "and defines it - contradiction. The paradox asks what "
            "'definable' can possibly mean, since the notion seems "
            "perfectly clear until it defines its own undefinable "
            "number."
        ),
        "background": (
            "G. G. Berry, a Bodleian librarian, sent the paradox to "
            "Russell, who published it in 1908. It belongs to the family "
            "of definability paradoxes (Richard's, Koenig's) that forced "
            "the strict separation of object language and metalanguage: "
            "'definable in English' is not itself an English predicate "
            "in the relevant sense. Tarski's undefinability theorem is "
            "the rigorous descendant - no sufficiently rich formal "
            "language defines its own truth predicate, and by extension "
            "its own definability predicate. Yet the philosophical "
            "question persists: we seem to understand 'definable in "
            "under sixty letters' perfectly well, and formal "
            "undefinability results tell us the notion cannot be "
            "captured, not what it is. The concept of definability "
            "itself - central to descriptive set theory and the "
            "constructible universe - still lacks a satisfying "
            "philosophical account."
        ),
        "why_it_matters": (
            "Definability is the engine of Goedel's constructible "
            "universe, of descriptive set theory, and of every "
            "formalization of 'what we can specify'. Berry's paradox "
            "marks the exact point where the intuitive notion outruns "
            "every formalization. Understanding it would clarify what "
            "mathematical existence claims amount to when they rest on "
            "'there exists a definition' - which is to say, much of "
            "modern set theory."
        ),
        "sig_pointer": (
            "The Signature edition proposes a resource-indexed "
            "definability: 'definable' is always relative to a fixed "
            "descriptive budget, and Berry's phrase exceeds the budget "
            "it claims to respect once self-counting is priced in. The "
            "full edition prices the letters, walks the audit, and "
            "gives the confirm/refute panel."
        ),
        "assumptions": [
            "A1: Definability claims are always relative to a stated "
            "resource budget (letters, symbols, steps).",
            "A2: The budget must price the act of referring to the "
            "budget itself.",
            "A3: A definition that spends more than its budget is not "
            "a definition under that budget.",
        ],
        "steps": [
            "Step 1: Fix the budget at sixty letters and ask what "
            "'definable in under sixty letters' costs to invoke.",
            "Step 2: Audit Berry's phrase: the description is short, "
            "but invoking the sixty-letter standard inside the "
            "description spends descriptive resources the budget does "
            "not cover.",
            "Step 3: Apply A2-A3: the phrase fails to be a definition "
            "under its own budget - the paradoxical number is never "
            "actually defined.",
            "Step 4: Generalize: every definability paradox smuggles "
            "an unpriced self-reference to the standard being used.",
            "Step 5: Recover the legitimate core: resource-indexed "
            "definability is coherent, matches Tarski's theorem, and "
            "explains why the naive notion felt clear.",
        ],
        "confirm": [
            "A formal resource-indexed definability predicate that "
            "reproduces Tarski's undefinability as a budget-exhaustion "
            "result would confirm the mechanism.",
            "If the pricing audit dissolves Richard's and Koenig's "
            "paradoxes too, the unity supports the proposal.",
        ],
        "refute": [
            "A Berry-style construction that stays within budget under "
            "every natural pricing scheme would refute the audit.",
            "If self-pricing turns out to be itself unformalizable, "
            "the proposal trades one mystery for another.",
        ],
        "not_claims": [
            "It does not claim Berry's phrase is meaningless - only "
            "that it is not a definition under its own budget.",
            "It does not replace Tarski's theorem; it offers the "
            "philosophical reading of why the theorem had to hold.",
            "It does not deny that some numbers are undefinable - only "
            "that this phrase exhibits one.",
        ],
        "citations": [CIT_BERRY, CIT_TARSKI],
    },
    {
        "key": "surprise",
        "name": "The Unexpected Hanging Paradox",
        "group": "Paradoxes of Vagueness and Reason",
        "ladder_rank": 8,
        "ladder_tier": "foundations",
        "problem": (
            "A judge tells the prisoner: you will be hanged next week, "
            "on a day you do not expect. The prisoner reasons: it "
            "cannot be Friday (I would expect it by Thursday night), so "
            "not Thursday either, and so on - so it cannot happen at "
            "all. Yet on Wednesday he is hanged, completely surprised. "
            "His reasoning was flawless and his conclusion false. "
            "Where is the flaw?"
        ),
        "background": (
            "The paradox - also called the surprise examination - was "
            "popularized in the 1940s and analyzed by Quine in 1953, "
            "who located the flaw in the prisoner's backward induction. "
            "The large literature since has never converged: proposed "
            "flaws include equivocation on 'expect', self-defeating "
            "announcements (the judge's statement cannot be common "
            "knowledge), the difference between knowing the day and "
            "knowing that you will be surprised, and formalizations in "
            "epistemic logic where the announcement turns out "
            "consistent after all. Fitch's formalization seemed to "
            "vindicate the prisoner; later analyses showed the "
            "formalization smuggled in assumptions. The paradox remains "
            "a live test case for theories of knowledge, belief "
            "revision, and self-referential announcements."
        ),
        "why_it_matters": (
            "The paradox is the cleanest probe of what happens when "
            "knowledge claims refer to the knower's own future "
            "epistemic state - the structure of every prediction about "
            "predictions, from markets to AI forecasting. A solution "
            "would discipline epistemic logic, clarify the logic of "
            "announcements and common knowledge, and explain how "
            "self-defeating prophecies work. Game theory's backward "
            "induction rests on reasoning uncomfortably close to the "
            "prisoner's."
        ),
        "sig_pointer": (
            "The Signature edition proposes an announcement-indexed "
            "knowledge model: the judge's statement updates the "
            "prisoner's knowledge exactly once, and the prisoner's "
            "iteration illicitly re-applies the update to its own "
            "output. The full edition runs the day-by-day audit, "
            "adjusts the update rule, and gives the confirm/refute "
            "panel."
        ),
        "assumptions": [
            "A1: An announcement updates knowledge once, at the "
            "moment it is received and trusted.",
            "A2: Reasoning about the announcement's consequences may "
            "not re-trigger the update.",
            "A3: 'Expect' means: assign high credence on current "
            "evidence, not: be able to deduce.",
        ],
        "steps": [
            "Step 1: Apply the judge's announcement once: the prisoner "
            "now knows (surprise hanging next week).",
            "Step 2: Run the prisoner's Friday elimination: valid as "
            "a consequence of the single update.",
            "Step 3: Catch the illicit move: eliminating Thursday "
            "re-applies the surprise condition to a situation already "
            "shaped by the first elimination - a second update A2 "
            "forbids.",
            "Step 4: Show the induction collapses without the "
            "re-application: Friday is out, the rest stay live.",
            "Step 5: Wednesday arrives: consistent with the "
            "single-update knowledge state, genuinely surprising "
            "under A3.",
        ],
        "confirm": [
            "An epistemic-logic model with one-shot announcement "
            "updates that validates the judge's consistency and the "
            "prisoner's surprise would confirm the mechanism.",
            "Experimental data showing real reasoners stop the "
            "backward induction at one step would support the "
            "psychological reality of A2.",
        ],
        "refute": [
            "A formalization in which the prisoner's full induction "
            "goes through with strictly one-shot updates would "
            "refute the diagnosis.",
            "If 'expect' must mean deductive certainty for the "
            "paradox to bite, the proposal dissolves a straw version.",
        ],
        "not_claims": [
            "It does not claim the prisoner was irrational - his "
            "mistake is subtle and principled.",
            "It does not deny that announcements can be self-defeating; "
            "it claims this one is not.",
            "It does not settle every formalization dispute - only the "
            "core flaw the paradox needs.",
        ],
        "citations": [CIT_QUINE_HANG],
    },
    {
        "key": "lottery",
        "name": "The Lottery Paradox",
        "group": "Paradoxes of Vagueness and Reason",
        "ladder_rank": 9,
        "ladder_tier": "foundations",
        "problem": (
            "A fair lottery has a million tickets and one winner. For "
            "each ticket it is rational to believe it will lose "
            "(probability 0.999999). By conjunction, it is rational to "
            "believe every ticket loses - but it is rational to believe "
            "some ticket wins. Rational belief contradicts itself. "
            "Which inference has to go?"
        ),
        "background": (
            "Henry Kyburg posed the paradox in 1961 as a direct assault "
            "on the view that rational belief is closed under "
            "conjunction and that high probability suffices for belief. "
            "The standard escapes: deny that high probability warrants "
            "outright belief (the 'belief is not credence' camp), "
            "restrict conjunction closure for rational belief, adopt "
            "probabilistic belief models that never detach outright "
            "beliefs, or embrace paraconsistency about belief. Each "
            "escape has costs: giving up closure cripples deductive "
            "reasoning from beliefs, while probabilistic models owe an "
            "account of when we may flat-out believe anything. The "
            "paradox sits at the exact junction of logic, probability, "
            "and epistemology, and it is unresolved."
        ),
        "why_it_matters": (
            "Every autonomous system - medical diagnosis AI, "
            "self-driving cars, financial models - must turn "
            "probabilities into actions, which is the lottery problem "
            "in engineering dress. If rational belief cannot aggregate "
            "high-probability judgments, then huge parts of expert and "
            "machine reasoning need re-founding. The paradox decides "
            "whether 'belief' is a coherent category at all."
        ),
        "sig_pointer": (
            "The Signature edition proposes a stake-relative belief "
            "rule: outright belief is warranted only when the stakes "
            "of being wrong are priced into the threshold, so "
            "lottery beliefs never detach in the first place. The full "
            "edition prices the tickets, walks the aggregation, and "
            "gives the confirm/refute panel."
        ),
        "assumptions": [
            "A1: Outright belief requires probability above a "
            "threshold that rises with the stakes of error.",
            "A2: In the lottery, the relevant stake is the paradox "
            "itself: detached beliefs are aggregated.",
            "A3: Aggregation across tickets raises the stakes, hence "
            "the threshold.",
        ],
        "steps": [
            "Step 1: Price a single ticket: believing 'ticket n loses' "
            "risks little alone, so the threshold is met - tentative "
            "belief licensed.",
            "Step 2: Note the aggregation: conjoining a million such "
            "beliefs risks the guaranteed contradiction, so stakes "
            "spike under A2-A3.",
            "Step 3: Apply the stake-relative threshold: at the "
            "aggregated stakes, 0.999999 no longer clears the bar, so "
            "conjunction introduction is blocked before detachment.",
            "Step 4: Preserve single-ticket reasoning: each belief "
            "remains rational in isolation - no skepticism about "
            "ordinary high-probability belief.",
            "Step 5: Verify closure is saved where stakes are low: "
            "mathematical and everyday conjunctions aggregate safely "
            "because their joint error risk stays priced in.",
        ],
        "confirm": [
            "Decision-theoretic modeling showing the threshold rule "
            "reproduces both lottery intuitions and ordinary closure "
            "would confirm the mechanism.",
            "If the rule also handles the preface paradox (record 11) "
            "with no extra machinery, that unity is strong evidence.",
        ],
        "refute": [
            "A low-stakes case where aggregation still forces the "
            "contradiction would refute the stake-relativity claim.",
            "If thresholds turn out to be unmeasurable even in "
            "principle, the rule is empty formalism.",
        ],
        "not_claims": [
            "It does not claim high probability never warrants belief - "
            "only that warrant is stake-relative.",
            "It does not deny closure outright; it prices it.",
            "It does not claim to dissolve every probabilistic "
            "paradox - only the aggregation structure they share.",
        ],
        "citations": [CIT_KYBERG],
    },
    {
        "key": "ravens",
        "name": "Hempel's Ravens Paradox",
        "group": "Paradoxes of Vagueness and Reason",
        "ladder_rank": 10,
        "ladder_tier": "foundations",
        "problem": (
            "'All ravens are black' is logically equivalent to 'All "
            "non-black things are non-ravens.' So a white shoe - a "
            "non-black non-raven - confirms that all ravens are black. "
            "Ornithology by shoe leather: absurd, yet the logic seems "
            "airtight. What is wrong with the confirmation theory?"
        ),
        "background": (
            "Carl Hempel posed the paradox in 1945 as a bomb under the "
            "logical-positivist theory of confirmation. The standard "
            "responses: accept the conclusion but note the confirmation "
            "is negligible (the Bayesian line - a white shoe confirms "
            "the raven hypothesis to a vanishing degree because "
            "non-black things vastly outnumber ravens); reject the "
            "equivalence condition on confirmation; or reject the "
            "instance condition (only ravens can confirm claims about "
            "ravens). Bayesians largely consider the paradox dissolved "
            "by the degree-of-confirmation reply, but critics note it "
            "relies on background knowledge doing the real work, and "
            "the deeper question - what confirmation IS - is untouched. "
            "Alternative confirmation theories (likelihoodist, "
            "error-statistical) each handle the ravens differently, "
            "and none commands consensus."
        ),
        "why_it_matters": (
            "Confirmation is the logic of science: every experiment "
            "'confirms' a theory in some sense, and the ravens show our "
            "account of that sense is broken. Machine learning faces "
            "the paradox daily - what counts as evidence for a "
            "classifier, and how much? A correct theory of confirmation "
            "would discipline experimental design, statistical "
            "inference, and the way AI systems weigh evidence."
        ),
        "sig_pointer": (
            "The Signature edition proposes an evidence-relevance "
            "filter: an observation confirms a hypothesis only if it "
            "was a candidate refuter - capable, in the experimental "
            "setup, of coming out the other way. White shoes were never "
            "at risk. The full edition runs the filter over the "
            "classic cases and gives the confirm/refute panel."
        ),
        "assumptions": [
            "A1: Confirmation requires risk: the observation must have "
            "been able to disconfirm in the setup used.",
            "A2: Logical equivalence preserves truth, not evidential "
            "role - contraposition can move a claim out of the "
            "experiment's risk zone.",
            "A3: Background knowledge fixes what was at risk, and is "
            "itself revisable.",
        ],
        "steps": [
            "Step 1: Examine the white shoe: in no setup was the shoe "
            "at risk of being a non-black raven - it fails A1.",
            "Step 2: Trace the contrapositive: 'all non-black things "
            "are non-ravens' ranges over a population (non-black "
            "things) the ornithologist never sampled.",
            "Step 3: Apply A2: the equivalence is truth-preserving but "
            "the evidential risk did not transfer with it.",
            "Step 4: Confirm the Bayesian degree reply is a special "
            "case: negligible risk means negligible confirmation, and "
            "the filter explains WHY.",
            "Step 5: Test a black raven: it was at risk (could have "
            "been albino), so it genuinely confirms - matching "
            "intuition.",
        ],
        "confirm": [
            "If the risk filter reproduces Bayesian confirmation "
            "degrees in standard cases while blocking the shoe, it "
            "unifies rather than competes - strong confirmation.",
            "Case studies from real experimental practice showing "
            "scientists implicitly use the risk criterion would "
            "support A1.",
        ],
        "refute": [
            "A genuine scientific confirmation in which the evidence "
            "was at no risk of disconfirming would refute the "
            "necessity of A1.",
            "If 'at risk' cannot be made precise without smuggling in "
            "the full Bayesian apparatus, the filter adds nothing.",
        ],
        "not_claims": [
            "It does not deny the logical equivalence - only its "
            "evidential innocence.",
            "It does not claim Bayesians were wrong; it claims to name "
            "the mechanism their degrees track.",
            "It does not solve the full problem of induction - only "
            "the confirmation-theoretic paradox.",
        ],
        "citations": [CIT_HEMPEL],
    },
    {
        "key": "preface",
        "name": "The Preface Paradox",
        "group": "Paradoxes of Vagueness and Reason",
        "ladder_rank": 11,
        "ladder_tier": "foundations",
        "problem": (
            "An author writes a scholarly book, believing each claim in "
            "it. In the preface she writes: 'Some claim in this book is "
            "false' - a rational admission of fallibility. But then she "
            "believes each claim AND believes the conjunction is false. "
            "Rational belief contradicts itself again - and this time "
            "there is no lottery, just honest scholarship."
        ),
        "background": (
            "David Makinson published the paradox in 1965, and it "
            "succeeded where the lottery partly failed: it needs no "
            "probabilities, only the ordinary structure of authorship. "
            "Every careful thinker holds both first-order beliefs and "
            "the second-order belief in her own fallibility, and "
            "classical logic makes the combination inconsistent. "
            "Responses parallel the lottery literature - restrict "
            "closure, stratify belief levels, deny that the preface "
            "statement is believed in the same sense - but the preface "
            "version resists the probabilistic escapes, since the "
            "author's fallibility belief is not obviously about "
            "chances. Some conclude rationality itself is "
            "paraconsistent; others that belief comes in levels that "
            "must not be conjoined. No resolution is standard."
        ),
        "why_it_matters": (
            "The preface paradox is the paradox of intellectual "
            "honesty: it says a fully rational agent cannot both hold "
            "beliefs and admit fallibility. Every scientist, every "
            "scholar, and every AI that reports its own uncertainty "
            "lives inside this paradox. Solving it would reconcile "
            "conviction with humility in a single formal account of "
            "rational belief - the operating system of inquiry itself."
        ),
        "sig_pointer": (
            "The Signature edition proposes a level-separation rule: "
            "first-order beliefs and the fallibility belief live on "
            "different reflective levels, and conjunction across levels "
            "is not licensed. The full edition stratifies the "
            "author's beliefs, shows the contradiction cannot form, "
            "and gives the confirm/refute panel."
        ),
        "assumptions": [
            "A1: Beliefs are level-indexed: L0 beliefs about the "
            "world, L1 beliefs about one's L0 beliefs.",
            "A2: Conjunction and closure apply within a level, never "
            "across levels.",
            "A3: The preface admission is an L1 belief; the book's "
            "claims are L0.",
        ],
        "steps": [
            "Step 1: Index the author's beliefs: each chapter claim is "
            "L0, the preface admission is L1.",
            "Step 2: Attempt the paradoxical conjunction: it would "
            "combine L0 claims with an L1 claim - blocked by A2.",
            "Step 3: Show each level is internally consistent: the L0 "
            "set is consistent by the author's lights; the L1 "
            "admission is a single coherent self-assessment.",
            "Step 4: Explain the paradox's pull: ordinary language "
            "erases level indices, so the cross-level conjunction "
            "feels licensed.",
            "Step 5: Preserve fallibility's function: the L1 belief "
            "still rationally mandates openness to correction without "
            "contradicting any L0 belief.",
        ],
        "confirm": [
            "If level-separation also dissolves the Knower paradox "
            "and Fitch's paradox of knowability, the unity strongly "
            "confirms the principle.",
            "Formal epistemic logics with level-indexed belief that "
            "validate both conviction and fallibility would be direct "
            "confirmation.",
        ],
        "refute": [
            "A version of the paradox constructed entirely within one "
            "level would refute the separation diagnosis.",
            "If rational agents demonstrably do conjoin across levels "
            "without irrationality, A2 is descriptively false.",
        ],
        "not_claims": [
            "It does not claim authors are infallible at any level - "
            "each level can still be wrong.",
            "It does not multiply levels beyond necessity; two suffice "
            "for the paradox as stated.",
            "It does not deny the feeling of paradox - it explains it "
            "as index-erasure in ordinary speech.",
        ],
        "citations": [CIT_MAKINSON, CIT_KYBERG],
    },
    {
        "key": "moore",
        "name": "Moore's Paradox",
        "group": "Paradoxes of Vagueness and Reason",
        "ladder_rank": 12,
        "ladder_tier": "foundations",
        "problem": (
            "'It is raining, but I do not believe it is raining.' The "
            "sentence can be true - rain falls on the sincere "
            "self-deceived - yet asserting it sounds absurd, even "
            "incoherent. What is wrong with asserting a possible "
            "truth? The paradox probes the link between belief, "
            "assertion, and rationality at its most intimate."
        ),
        "background": (
            "G. E. Moore noted the absurdity in the 1940s, and "
            "Wittgenstein called it the most interesting philosophical "
            "discovery of the century. The sentence is not a logical "
            "contradiction: both conjuncts can be true together. The "
            "absurdity is pragmatic or epistemic - asserting p "
            "expresses belief in p, so the speaker contradicts herself "
            "in the act. Competing diagnoses: the knowledge norm of "
            "assertion (you may assert only what you know), the belief "
            "norm, expressivist accounts of 'I believe', and "
            "Moorean-skeptical views that deny the absurdity is "
            "genuinely paradoxical. The commissive variant - 'p, but I "
            "will never believe p' - and the role of first-person "
            "authority keep the problem alive. It remains the sharpest "
            "test of any theory of assertion."
        ),
        "why_it_matters": (
            "Assertion is the fundamental move of communication, "
            "science, and testimony; Moore's paradox shows we do not "
            "understand its rules. AI systems that assert things - "
            "which is all of them - need a correct norm of assertion: "
            "when may a system flatly state p? The paradox also "
            "structures debates about self-knowledge, sincerity, and "
            "the ethics of belief."
        ),
        "sig_pointer": (
            "The Signature edition proposes an act-content split: the "
            "absurdity lives in the act of asserting, which commits the "
            "speaker to the belief the content disavows. The full "
            "edition stages the assertion, separates act from content, "
            "and gives the confirm/refute panel."
        ),
        "assumptions": [
            "A1: Assertion is an act that publicly commits the speaker "
            "to belief in the asserted content.",
            "A2: The content 'p and I do not believe p' can be true; "
            "the act of asserting it cannot be sincere.",
            "A3: Absurdity judgments track act-content mismatch, not "
            "content inconsistency.",
        ],
        "steps": [
            "Step 1: Split the Moorean sentence into content (possibly "
            "true) and act (the asserting).",
            "Step 2: Apply A1: asserting the first conjunct commits the "
            "speaker to believing it is raining.",
            "Step 3: Note the second conjunct disavows exactly that "
            "belief - the act contradicts its own commitment.",
            "Step 4: Derive the absurdity verdict from A3: listeners "
            "detect the act-content mismatch, not a logical "
            "contradiction.",
            "Step 5: Predict the variants: third-person versions "
            "('p, but he does not believe p') are fine - no "
            "self-commitment is contradicted.",
        ],
        "confirm": [
            "The correct prediction for third-person and past-tense "
            "variants (fine) versus present first-person (absurd) "
            "confirms the act-based diagnosis.",
            "If the same act-content analysis handles the "
            "commissive and omissive variants uniformly, that unity "
            "supports the proposal.",
        ],
        "refute": [
            "A sincere, non-absurd present-tense first-person Moorean "
            "assertion in ordinary discourse would refute the act "
            "analysis.",
            "If assertion can be shown to carry no belief commitment "
            "(pure expressivism about assertion), A1 fails and the "
            "proposal with it.",
        ],
        "not_claims": [
            "It does not claim the Moorean sentence is false - it may "
            "be true.",
            "It does not claim all absurdity is pragmatic; logical "
            "contradiction remains its own phenomenon.",
            "It does not settle the knowledge-versus-belief norm "
            "debate - only where the absurdity lives.",
        ],
        "citations": [CIT_MOORE],
    },
    # ------------------------------------------------------------ COMPOUNDED
    {
        "key": "dialetheism",
        "name": "Are There True Contradictions?",
        "group": "Paraconsistency and Truth",
        "ladder_rank": 13,
        "ladder_tier": "compounded",
        "problem": (
            "Classical logic says contradictions cannot be true. "
            "Dialetheists - led by Graham Priest - say some are: the "
            "liar sentence is both true and false, and logic should "
            "tolerate it via paraconsistent logic. The open problem: "
            "what does 'true' even mean in a paraconsistent setting, "
            "where asserting a contradiction no longer explodes into "
            "triviality? Is dialetheism a discovery about reality or "
            "a change of subject?"
        ),
        "background": (
            "Paraconsistent logics - systems where contradictions do "
            "not entail everything - were developed from the 1950s "
            "onward (Jaskowski, da Costa) as technical curiosities. "
            "Priest's 'In Contradiction' (1987/2006) turned the "
            "technicality into metaphysics: some contradictions, the "
            "dialetheias, are true, with the liar as exhibit A. The "
            "program faces the central open question this record "
            "poses: the classical concept of truth is bound up with "
            "consistency - to call a theory true is partly to vouch "
            "for its coherence. Paraconsistent truth must be a "
            "different concept, and critics charge that the "
            "dialetheist has simply changed the meaning of 'true' and "
            "'contradiction' and declared victory. Defenses appeal to "
            "the unity of the solution across paradoxes and to the "
            "claim that some phenomena (vague boundaries, the limits "
            "of thought) are genuinely inconsistent. The metaphysics "
            "of paraconsistent truth is unsettled."
        ),
        "why_it_matters": (
            "If dialetheism is right, the law of non-contradiction - "
            "Aristotle's firmest principle - is false, and every "
            "science built on classical logic needs re-examination. If "
            "it is wrong, the paradoxes still stand and need another "
            "answer. Either way, the nature of truth in paraconsistent "
            "logics determines whether inconsistency-tolerant "
            "reasoning - essential for large databases, legal codes, "
            "and AI knowledge bases - has a coherent semantics or is "
            "just useful engineering."
        ),
        "sig_pointer": (
            "The Signature edition proposes a dual-track semantics: "
            "paraconsistent 'truth' tracks assertibility-under-"
            "conflict, a strictly weaker notion than classical truth, "
            "and dialetheias are re-filed as boundary phenomena rather "
            "than metaphysical discoveries. The full edition builds "
            "the two tracks, runs the liar through both, and gives "
            "the confirm/refute panel."
        ),
        "assumptions": [
            "A1: There are two truth-like notions: classical truth "
            "(consistency-involving) and conflict-truth (warranted "
            "assertibility under conflicting evidence).",
            "A2: Paraconsistent logics model conflict-truth, not "
            "classical truth.",
            "A3: A dialetheia is a sentence assertible on both sides "
            "of a genuine conflict - a boundary marker, not a "
            "metaphysical joint.",
        ],
        "steps": [
            "Step 1: Separate the notions: define classical truth via "
            "the T-schema plus consistency; define conflict-truth via "
            "warranted assertibility given the total evidence.",
            "Step 2: Run the liar: the evidence (the reasoning both "
            "ways) warrants asserting both 'true' and 'false' - a "
            "conflict-truth dialetheia under A3.",
            "Step 3: Show the metaphysical sting is removed: nothing "
            "about reality is contradictory; what is contradictory is "
            "our evidential situation at the boundary.",
            "Step 4: Preserve paraconsistency's engineering value: "
            "conflict-tolerant inference is legitimate exactly where "
            "evidence conflicts - databases, law, sensor fusion.",
            "Step 5: Answer the change-of-subject charge head-on: yes, "
            "the subject shifted from metaphysics to evidential "
            "boundaries - and that is the honest form of the view.",
        ],
        "confirm": [
            "If every alleged dialetheia can be re-described as an "
            "evidential-boundary phenomenon with no residue, the "
            "re-filing is confirmed.",
            "A formal semantics with two truth predicates satisfying "
            "A1-A3 and validating the paraconsistent inferences would "
            "be strong confirmation.",
        ],
        "refute": [
            "A dialetheia candidate that cannot be read as an "
            "evidential conflict - a contradiction demanded by "
            "reality itself - would refute the boundary reading.",
            "If conflict-truth collapses into classical truth under "
            "formalization, the dual-track distinction is empty.",
        ],
        "not_claims": [
            "It does not claim Priest's program is worthless - "
            "paraconsistent logic keeps its full technical value.",
            "It does not deny that some sentences are reasonably "
            "asserted both ways; it reinterprets what that means.",
            "It does not claim classical logic is the one true logic "
            "for all purposes.",
        ],
        "citations": [CIT_PRIEST, CIT_BEALL],
    },
    {
        "key": "vcurry",
        "name": "The v-Curry Revenge",
        "group": "Paraconsistency and Truth",
        "ladder_rank": 14,
        "ladder_tier": "compounded",
        "problem": (
            "Paraconsistent solutions to the liar use a detachable "
            "conditional and keep modus ponens - and that is exactly "
            "what Curry's paradox needs. The v-Curry (validity Curry) "
            "sentence says 'If this argument is valid, absurdity "
            "follows,' and derives triviality in systems that solved "
            "the liar. Can any paraconsistent theory of truth survive "
            "its own revenge?"
        ),
        "background": (
            "The v-Curry paradox, sharpened by Beall and Murzi around "
            "2012, is the revenge problem for paraconsistent truth "
            "theories specifically. Dialetheists blocked the liar by "
            "accepting true contradictions while keeping the logic "
            "non-trivial; but Curry-style reasoning needs only a "
            "conditional satisfying modus ponens and conditional "
            "proof, both of which paraconsistent theories retain. The "
            "v-Curry construction uses validity rather than truth: "
            "from 'this argument is valid' plus the argument itself, "
            "absurdity follows by the very rules the theory endorses. "
            "Responses have included restricting the validity "
            "predicate (mirroring Tarski's hierarchy, losing the "
            "paraconsistent advantage), adopting non-detachable "
            "conditionals (losing modus ponens, crippling the logic), "
            "or biting the bullet. The trilemma - truth without "
            "revenge, or validity with teeth, or logic without modus "
            "ponens - is unresolved."
        ),
        "why_it_matters": (
            "v-Curry is the paradox that ate the leading solution to "
            "the paradoxes. If paraconsistent truth theories cannot "
            "survive it, the most developed research program on the "
            "semantic paradoxes collapses, and the field is thrown "
            "back to hierarchies and revisionism. More broadly, it "
            "tests whether any logic can simultaneously have a "
            "transparent truth predicate, modus ponens, and "
            "non-triviality - the three desiderata of applied "
            "reasoning."
        ),
        "sig_pointer": (
            "The Signature edition proposes a validity-budget parallel "
            "to the Curry discharge-budget: validity ascriptions, like "
            "truth ascriptions, must earn their discharge. The full "
            "edition reconstructs the v-Curry argument, applies the "
            "budget at the validity step, and gives the confirm/refute "
            "panel."
        ),
        "assumptions": [
            "A1: Validity claims are governed by the same earned-"
            "discharge rule as truth claims (record 4).",
            "A2: 'This argument is valid' is unearned when the "
            "argument's only support is the claim itself.",
            "A3: Genuine validity proofs - the kind logicians "
            "actually give - always meet the budget.",
        ],
        "steps": [
            "Step 1: Reconstruct v-Curry: assume the argument from "
            "'this argument is valid' to absurdity is valid; derive "
            "absurdity; discharge.",
            "Step 2: Audit the validity ascription: its entire content "
            "is the argument whose validity is at issue - unearned "
            "under A2.",
            "Step 3: Apply the budget: the discharge step is refused, "
            "halting the derivation before triviality.",
            "Step 4: Verify real validity proofs pass: textbook "
            "soundness arguments earn discharge through independent "
            "model-theoretic work.",
            "Step 5: Unify: one budget rule blocks liar-Curry, "
            "truth-Curry, and validity-Curry - the revenge family "
            "falls together.",
        ],
        "confirm": [
            "A formal earned-discharge criterion covering truth and "
            "validity predicates jointly, blocking all known "
            "revenge constructions, would confirm the unification.",
            "If working logicians' validity proofs all satisfy the "
            "budget while every revenge construction fails it, the "
            "criterion carves nature at the joints.",
        ],
        "refute": [
            "A revenge construction that earns its discharge under "
            "any natural precisification kills the proposal.",
            "A legitimate proof-theoretic validity argument blocked "
            "by the budget would refute its conservativeness.",
        ],
        "not_claims": [
            "It does not claim validity is unformalizable - only that "
            "self-certifying validity claims are unearned.",
            "It does not abandon paraconsistency; the budget is "
            "compatible with dialetheic semantics.",
            "It does not claim the trilemma is dissolved painlessly - "
            "the budget is a real restriction, just a principled one.",
        ],
        "citations": [CIT_BEALL, CIT_CURRY],
    },
    {
        "key": "revenge",
        "name": "Revenge of the Liar",
        "group": "Paraconsistency and Truth",
        "ladder_rank": 15,
        "ladder_tier": "compounded",
        "problem": (
            "Every theory of truth proposed to solve the liar faces "
            "revenge: a new paradox built from the theory's own "
            "machinery. Tarskian hierarchies get 'this sentence is not "
            "true at any level'; Kripke's gaps get 'this sentence is "
            "not true' (which seems true but ungrounded); "
            "paracomplete theories get strengthened liars. Is revenge "
            "a solvable engineering problem, or proof that no "
            "theory of truth can be both complete and consistent?"
        ),
        "background": (
            "The revenge problem is the meta-paradox: it is not one "
            "puzzle but the pattern that every solution breeds a new "
            "puzzle. Tarski's hierarchy invites the question of what "
            "level the theorist's own claims occupy. Kripke's theory "
            "of truth, which leaves the liar ungrounded, is revenged "
            "by sentences asserting their own untruth - intuitively "
            "true, yet the theory cannot say so. Field's paracomplete "
            "theory and Beall's paraconsistent variants each have "
            "known revenge sentences in the literature. Some "
            "philosophers conclude revenge shows truth is an "
            "inconsistent concept and embrace it; others see an "
            "infinite but manageable hierarchy of patches. Whether "
            "revenge is terminable - whether any theory can be "
            "revenge-immune - is itself an open problem about the "
            "limits of theorizing."
        ),
        "why_it_matters": (
            "Revenge decides whether the semantic paradoxes are a "
            "finite list of puzzles or an inexhaustible generator - "
            "whether the concept of truth is repairable or "
            "essentially inconsistent. If revenge is interminable, "
            "then every formal semantics, every AI truth predicate, "
            "and every philosophical theory of truth is necessarily "
            "incomplete. It is the second-order question that governs "
            "all first-order answers."
        ),
        "sig_pointer": (
            "The Signature edition proposes a revenge-ceiling "
            "theorem-schema: any truth theory formulated in a "
            "language rich enough to state its own revenge diagnosis "
            "generates the next revenge sentence - so immunity is "
            "provably impossible, and the rational stance is managed "
            "containment, not final victory. The full edition states "
            "the schema, tests it against the historical revenges, "
            "and gives the confirm/refute panel."
        ),
        "assumptions": [
            "A1: A truth theory must be statable in a language its "
            "own speakers understand.",
            "A2: Any such language can form self-descriptive "
            "sentences about the theory's classifications.",
            "A3: Containment (blocking each revenge as it arises) is "
            "a legitimate theoretical success, distinct from "
            "immunity.",
        ],
        "steps": [
            "Step 1: Take any truth theory T with a revenge sentence R "
            "formulated in T's metalanguage.",
            "Step 2: Note that T's diagnosis of R ('R is ungrounded / "
            "ungrounded-at-level-n / ...') is itself statable - by A1.",
            "Step 3: Form R': 'R's diagnosis does not apply to this "
            "sentence' - the next revenge, constructible by A2.",
            "Step 4: Conclude the schema: immunity would require the "
            "theory to be unstatable, contradicting A1 - so no "
            "statable theory is revenge-immune.",
            "Step 5: Reframe success as containment: theories are "
            "ranked by how naturally they absorb each revenge, not "
            "by achieving the impossible.",
        ],
        "confirm": [
            "If the schema's prediction holds across every new "
            "truth theory proposed in the next decade of literature, "
            "that track record confirms it.",
            "A precise formal version provable for a well-defined "
            "class of theories would upgrade the schema to a theorem.",
        ],
        "refute": [
            "A single statable, revenge-immune truth theory would "
            "refute the schema outright.",
            "If some revenge sentences turn out to be unformulable "
            "in principle (not just unformulated), A2 fails.",
        ],
        "not_claims": [
            "It does not claim theorizing about truth is futile - "
            "containment is genuine progress.",
            "It does not claim to prove the schema formally; it is "
            "proposed as a schema awaiting formalization.",
            "It does not favor any first-order theory; it is neutral "
            "among the competitors.",
        ],
        "citations": [CIT_FIELD, CIT_BEALL, CIT_KRIPKE],
    },
    {
        "key": "naive-truth",
        "name": "How Strong Can Naive Truth Be?",
        "group": "Paraconsistency and Truth",
        "ladder_rank": 16,
        "ladder_tier": "compounded",
        "problem": (
            "Naive truth is the folk notion: 'p is true' just in case "
            "p, fully transparent, no hierarchies. Formalized naively "
            "it is inconsistent (liar, Curry). The KF (Kripke-Feferman) "
            "and FS (Friedman-Sheard) theories try to keep as much "
            "naivete as possible. Open questions abound - including "
            "whether FS is even consistent, and how much naive "
            "reasoning each theory preserves. How close to naive can "
            "a consistent truth theory get?"
        ),
        "background": (
            "After Tarski proved transparent truth undefinable, the "
            "research program became: how much transparency can we "
            "keep? Kripke's fixed-point construction keeps truth "
            "partial; Feferman's KF axiomatizes it in classical logic, "
            "proving exactly as much arithmetic as PA. Friedman and "
            "Sheard's FS keeps the naive truth rules - including "
            "unrestricted T-schema reasoning - by weakening the "
            "underlying logic's handling of the conditional; its "
            "consistency is a famous open problem, with partial "
            "results (it is consistent if PA is, for some "
            "formulations, but the full system resists proof). "
            "Halbach's axiomatic theories of truth systematized the "
            "landscape. The program's driving question - the maximal "
            "consistent fragment of naive truth - remains open, and "
            "each candidate theory trades transparency against "
            "logical strength in ways not fully mapped."
        ),
        "why_it_matters": (
            "Naive truth is the notion in every human head; the gap "
            "between it and any consistent formalization measures how "
            "far logic must depart from common sense. AI systems that "
            "reason about truth need the strongest safe fragment - "
            "too weak and they cannot reason naturally, too strong "
            "and they derive absurdities. The FS consistency question "
            "is one of the great open problems of mathematical logic, "
            "deciding how much of our naive concept survives "
            "formalization."
        ),
        "sig_pointer": (
            "The Signature edition proposes a transparency-budget "
            "map: each naive truth principle is priced by the paradox "
            "risk it carries, and the maximal safe set is the largest "
            "affordable bundle. The full edition prices the "
            "principles, exhibits the frontier, and gives the "
            "confirm/refute panel."
        ),
        "assumptions": [
            "A1: Naive truth principles can be individually priced by "
            "the paradox constructions they enable.",
            "A2: A bundle of principles is safe iff no paradox "
            "construction goes through on the bundle alone.",
            "A3: The pricing is monotonic: adding principles never "
            "reduces risk.",
        ],
        "steps": [
            "Step 1: List the naive principles: T-In, T-Out, "
            "compositional clauses, naive conditional rules.",
            "Step 2: Price each: full T-In/T-Out plus modus ponens "
            "buys Curry - maximum risk; compositional clauses alone "
            "are cheap.",
            "Step 3: Exhibit known theories as bundles: KF buys "
            "compositionality, sells full transparency; FS buys "
            "transparency, sells classical conditional.",
            "Step 4: Trace the frontier: the maximal safe bundles "
            "form an antichain - no unique 'best' naive theory, "
            "explaining the program's pluralism.",
            "Step 5: Locate FS on the map: its consistency question "
            "becomes whether its bundle sits inside the safe region - "
            "a precise, attackable formulation.",
        ],
        "confirm": [
            "If the budget map predicts the known consistency and "
            "inconsistency results (KF consistent, naive full "
            "transparency inconsistent), it earns its keep.",
            "A proof settling FS consistency either way would "
            "validate the map's placement of FS on the frontier.",
        ],
        "refute": [
            "A safe bundle the map prices as risky (a false "
            "positive) or a paradoxical bundle it prices as safe "
            "would refute the pricing.",
            "If paradox risk turns out non-monotonic - a stronger "
            "bundle safer than a weaker one - A3 fails.",
        ],
        "not_claims": [
            "It does not claim to prove FS consistent or "
            "inconsistent - it reframes the question.",
            "It does not claim the pricing is unique; rival pricings "
            "are rival research programs.",
            "It does not deny that some other formalization could "
            "redraw the map - the map is a proposal, not a theorem.",
        ],
        "citations": [CIT_FIELD, CIT_TARSKI],
    },
    {
        "key": "natural-incompleteness",
        "name": "Natural Incompleteness",
        "group": "Incompleteness and Axioms",
        "ladder_rank": 17,
        "ladder_tier": "compounded",
        "problem": (
            "Goedel's incompleteness theorems produce undecidable "
            "sentences via self-referential Goedel-numbering tricks. "
            "Critics object: these are logician's artifacts, not real "
            "mathematics. Harvey Friedman's program seeks "
            "'natural' incompleteness - concrete combinatorial "
            "statements, the kind working mathematicians care about, "
            "that PA cannot decide. How much of ordinary mathematics "
            "is independent of our standard axioms?"
        ),
        "background": (
            "Goedel (1931) showed any consistent formal system "
            "containing arithmetic is incomplete; Gentzen (1936) and "
            "later work calibrated exactly how much induction the "
            "unprovable statements need. Paris and Harrington (1977) "
            "found the first 'natural' independent statement - a "
            "strengthened finite Ramsey theorem, unprovable in PA. "
            "Friedman's program since the 1980s has produced families "
            "of concrete finite-combinatorial statements independent "
            "of PA and of stronger systems, some requiring large "
            "cardinal axioms. Yet a gap persists: no mainstream "
            "conjecture of ordinary mathematics (Riemann, Goldbach, "
            "P vs NP) is known to be independent of PA or ZFC, and "
            "proofs of independence for natural statements still "
            "require metamathematical machinery. Whether "
            "incompleteness reaches into the mathematics anyone "
            "actually does remains open."
        ),
        "why_it_matters": (
            "If natural incompleteness is pervasive, then large parts "
            "of mathematics may be unresolvable with current axioms - "
            "a second scientific revolution in the foundations, "
            "forcing new axioms into mainstream practice. If it is "
            "rare, Goedel's theorems are philosophically profound but "
            "mathematically quarantined. The answer determines whether "
            "working mathematicians must care about foundations at "
            "all."
        ),
        "sig_pointer": (
            "The Signature edition proposes a naturalness gradient: "
            "independent statements are scored by their distance from "
            "core mathematical practice, and the program's progress "
            "is measured as the gradient's inward march. The full "
            "edition scores the known examples, projects the march, "
            "and gives the confirm/refute panel."
        ),
        "assumptions": [
            "A1: Naturalness is gradable: distance from statements "
            "mathematicians would investigate without metamathematical "
            "motivation.",
            "A2: The Paris-Harrington and Friedman examples lie "
            "strictly inward of Goedel sentences on this gradient.",
            "A3: Inward march is evidence of pervasiveness, not of "
            "clever cherry-picking.",
        ],
        "steps": [
            "Step 1: Score examples: Goedel sentence (far), "
            "Paris-Harrington (nearer), Friedman finite forms "
            "(nearer still) - the gradient visibly marches inward.",
            "Step 2: Extrapolate: each decade's examples are more "
            "natural than the last; project the trend.",
            "Step 3: Identify the mechanism: independence needs "
            "fast-growing functions, and mathematics keeps "
            "discovering natural ones.",
            "Step 4: Bound the skepticism: cherry-picking is "
            "controlled because the statements predate their "
            "independence proofs in several cases.",
            "Step 5: State the testable prediction: within the "
            "program's lifetime, an independence result for a "
            "statement of independent mathematical interest will "
            "appear.",
        ],
        "confirm": [
            "Each new natural independent statement further inward "
            "on the gradient confirms the march.",
            "An independence proof for a mainstream conjecture would "
            "confirm pervasiveness decisively.",
        ],
        "refute": [
            "A principled barrier theorem - natural statements of "
            "such-and-such form are always decidable in PA - would "
            "refute pervasiveness.",
            "If the gradient stalls for decades with no inward "
            "movement, the extrapolation fails.",
        ],
        "not_claims": [
            "It does not claim any mainstream conjecture IS "
            "independent - only that the trend points inward.",
            "It does not claim naturalness is perfectly objective; "
            "the gradient is a proposed measure.",
            "It does not deny Goedel sentences their foundational "
            "role - they anchor the far end.",
        ],
        "citations": [CIT_GODEL31, CIT_FRIEDMAN, CIT_PARIS],
    },
    {
        "key": "hilbert-program",
        "name": "Hilbert's Program After Goedel",
        "group": "Incompleteness and Axioms",
        "ladder_rank": 18,
        "ladder_tier": "compounded",
        "problem": (
            "Hilbert wanted finitary consistency proofs for all of "
            "mathematics - absolute security. Goedel's second theorem "
            "seemed to kill it: no consistent system proves its own "
            "consistency. But what exactly counts as 'finitary'? "
            "Gentzen proved PA consistent using transfinite induction "
            "to epsilon-zero - is that finitary? The open problem: "
            "formulate Hilbert's program precisely enough to say "
            "whether it is dead, alive, or transformed."
        ),
        "background": (
            "Hilbert's program (1920s) aimed to secure infinitary "
            "mathematics by finitary means. Goedel's second "
            "incompleteness theorem (1931) showed no sufficiently "
            "strong consistent theory proves its own consistency, "
            "which most took as the program's death certificate. But "
            "the theorem has a loophole: it blocks only consistency "
            "proofs formalizable in the system itself. Gentzen's 1936 "
            "consistency proof for PA uses induction up to "
            "epsilon-zero - not formalizable in PA, yet arguably "
            "finitary in spirit. Proof theorists (Schuette, "
            "Feferman, Sieg) have spent decades delineating "
            "'finitism', with proposals ranging from PRA (primitive "
            "recursive arithmetic) to broader notions. Detlefsen and "
            "others argue Hilbert's program survives in relativized "
            "form. There is no consensus on what would even count as "
            "the program's success or failure."
        ),
        "why_it_matters": (
            "This is the question of whether mathematics can be "
            "secured - whether we can know our foundations are "
            "consistent without circularity. Every proof assistant, "
            "every formalized library, every claim of mathematical "
            "certainty rests on some stance toward it. If a "
            "relativized Hilbert program succeeds, we get a "
            "principled hierarchy of trust; if it fails utterly, "
            "mathematical knowledge rests on unprovable faith in "
            "consistency."
        ),
        "sig_pointer": (
            "The Signature edition proposes a trust-ladder "
            "reconstruction: finitism is not one doctrine but a "
            "ladder of methods, and each rung secures the rungs "
            "below - Hilbert's program survives as the claim that "
            "the ladder has no top. The full edition climbs the "
            "rungs, prices each method, and gives the confirm/refute "
            "panel."
        ),
        "assumptions": [
            "A1: 'Finitary' is not a natural kind; it is a ladder of "
            "method-strengths from PRA upward.",
            "A2: Each rung can prove the consistency of the rungs "
            "below it (Gentzen's pattern generalizes).",
            "A3: Trust in a rung requires only the methods of that "
            "rung - no circularity within a step.",
        ],
        "steps": [
            "Step 1: Lay the ladder: PRA at the bottom, then PA, then "
            "PA plus transfinite inductions, upward.",
            "Step 2: Show each step's consistency proof uses only the "
            "next rung's methods - Gentzen's epsilon-zero proof as "
            "the template.",
            "Step 3: Reconstruct Hilbert's demand: not absolute "
            "self-security (impossible by Goedel) but the absence of "
            "a highest needed rung.",
            "Step 4: Argue the ladder has no top in principle: for "
            "any rung, the next rung's methods are intelligible to "
            "someone who grasps the current one.",
            "Step 5: Convert the program's death into its "
            "transformation: from one finitary foundation to an "
            "open-ended hierarchy of relative securities.",
        ],
        "confirm": [
            "If proof theory keeps producing Gentzen-style relative "
            "consistency proofs for ever-stronger systems, the "
            "ladder picture is confirmed in practice.",
            "A principled ceiling - methods beyond which no "
            "intelligible rung exists - would need to be found to "
            "threaten it; its continued absence supports the view.",
        ],
        "refute": [
            "A demonstration that some rung's methods are "
            "unintelligible without already assuming the "
            "consistency they prove would break A3.",
            "If 'finitary' turns out to have a sharp natural "
            "boundary after all, the ladder dissolves into the "
            "original program - dead or alive.",
        ],
        "not_claims": [
            "It does not claim PA is consistent - it assumes it, as "
            "all such discussion must.",
            "It does not claim the ladder answers the skeptic; it "
            "claims to state Hilbert's program coherently.",
            "It does not deny Goedel's theorem - it is built around "
            "it.",
        ],
        "citations": [CIT_GODEL31, CIT_GENTZEN],
    },
    {
        "key": "ch",
        "name": "The Continuum Hypothesis",
        "group": "Incompleteness and Axioms",
        "ladder_rank": 19,
        "ladder_tier": "compounded",
        "problem": (
            "Is there a set strictly larger than the natural numbers "
            "but strictly smaller than the real numbers? Cantor's "
            "continuum hypothesis (CH) says no. Goedel (1940) showed "
            "CH is consistent with ZFC; Cohen (1963) showed its "
            "negation is too. So ZFC does not decide it. The open "
            "problem: which new axiom SHOULD decide it, and is there "
            "a fact of the matter about the size of the continuum?"
        ),
        "background": (
            "CH is the first and most famous independent statement, "
            "Hilbert's first problem. Goedel's constructible universe "
            "L satisfies CH, proving its consistency; Cohen's forcing "
            "built models where CH fails, inventing the technique "
            "that reshaped set theory. Since then the community has "
            "split: Goedel believed new axioms would settle CH and "
            "that it is probably false; Woodin's program seeks "
            "canonical models deciding it; set-theoretic pluralists "
            "(Hamkins) hold there is no single fact - CH holds in "
            "some universes, fails in others, and that is all there "
            "is to say. Forcing axioms like PFA imply the continuum "
            "is aleph-2 (so CH is false); Woodin's Ultimate-L program "
            "aims at a canonical inner model. After sixty years of "
            "forcing, the question 'is CH true?' remains philosophy "
            "as much as mathematics."
        ),
        "why_it_matters": (
            "CH asks the most basic question about infinity's "
            "structure: how many sizes of infinity sit between the "
            "countable and the continuum? Its independence was the "
            "first proof that our axioms are radically incomplete "
            "about the most elementary infinite objects. Settling "
            "which axioms should extend ZFC would fix the methodology "
            "for all future independence results - it is the test "
            "case for the entire foundations enterprise."
        ),
        "sig_pointer": (
            "The Signature edition proposes an axiom-scorecard method: "
            "candidate axioms are scored on fruitfulness, naturalness, "
            "and convergence, and the CH verdict follows the winner "
            "rather than preceding it. The full edition scores the "
            "leading candidates, tallies the card, and gives the "
            "confirm/refute panel."
        ),
        "assumptions": [
            "A1: Axiom choice is adjudicated by scored virtues, not "
            "by direct intuition about the continuum.",
            "A2: Fruitfulness (theorems proved), naturalness "
            "(non-ad-hoc-ness), and convergence (agreement across "
            "programs) are the scoring dimensions.",
            "A3: The CH verdict is downstream of the axiom verdict, "
            "never the other way around.",
        ],
        "steps": [
            "Step 1: Score the candidates: PFA/MM (high fruitfulness, "
            "implies not-CH), large cardinals (neutral on CH), "
            "Ultimate-L (aims at CH, program incomplete).",
            "Step 2: Apply A3: do not let preferred CH answers "
            "inflate axiom scores - the classic circularity.",
            "Step 3: Tally: forcing axioms currently lead on "
            "fruitfulness; the tally says 'not-CH' provisionally.",
            "Step 4: Note the provisionality: a completed Ultimate-L "
            "would re-score the board - the method is "
            "self-correcting.",
            "Step 5: Draw the moral: 'is CH true?' is ill-posed "
            "without the scorecard; with it, the answer is whatever "
            "the best axioms say, held fallibly.",
        ],
        "confirm": [
            "If the scorecard's verdicts track the actual "
            "convergence of set-theoretic practice over time, the "
            "method is confirmed pragmatically.",
            "A completed canonical inner model program would test "
            "the scorecard's self-correction decisively.",
        ],
        "refute": [
            "If axiom choice turns out to be purely sociological - "
            "no virtue-score predicts adoption - the scorecard is "
            "empty.",
            "A direct, compelling intuition about the continuum's "
            "size that bypasses axioms would refute A1.",
        ],
        "not_claims": [
            "It does not claim CH is false - only that current "
            "scoring favors not-CH provisionally.",
            "It does not deny pluralism; the scorecard is addressed "
            "to universe-view set theorists.",
            "It does not claim the virtues are uncontroversial - "
            "scoring is itself debate.",
        ],
        "citations": [CIT_GODEL40, CIT_COHEN, CIT_WOODIN, CIT_HAMKINS],
    },
    {
        "key": "ac-fragments",
        "name": "Which Fragments of Choice?",
        "group": "Incompleteness and Axioms",
        "ladder_rank": 20,
        "ladder_tier": "compounded",
        "problem": (
            "The axiom of choice (AC) is independent of ZF and "
            "notoriously non-constructive. But mathematics rarely "
            "needs full AC - it needs fragments: countable choice, "
            "dependent choice, the Boolean prime ideal theorem, the "
            "axiom of choice for finite sets. The open problem: map "
            "exactly which theorems need which fragments, and find "
            "the weakest natural fragment that suffices for "
            "'ordinary' mathematics."
        ),
        "background": (
            "Zermelo introduced AC in 1904; its independence was shown "
            "by Goedel (consistent) and Cohen (independent). "
            "Meanwhile, analysts and algebraists noticed their "
            "theorems used only weak forms: countable choice for "
            "sequences, dependent choice for most analysis, the "
            "ultrafilter lemma for compactness arguments. Howard, "
            "Rubin, and others catalogued hundreds of choice "
            "principles and their interdependencies (the famous "
            "'Consequences of the Axiom of Choice' compendium). "
            "Reverse mathematics (Friedman, Simpson) classifies "
            "theorems by the set-existence axioms they need over a "
            "weak base - but the full map from mainstream theorems "
            "to minimal choice fragments is nowhere near complete, "
            "and the question of which fragment 'ordinary' "
            "mathematics inhabits is open."
        ),
        "why_it_matters": (
            "AC is the axiom mathematicians love to hate: "
            "indispensable yet responsible for the Banach-Tarski "
            "paradox and other monsters. Knowing exactly which "
            "fragment each theorem needs would let mathematics keep "
            "its results while quarantining the pathology - "
            "constructive and computational mathematics depend on "
            "this map. It also decides how much of AC is "
            "mathematical necessity versus foundational luxury."
        ),
        "sig_pointer": (
            "The Signature edition proposes a choice-need audit: a "
            "systematic protocol that takes a theorem's proof and "
            "extracts the minimal choice fragment it consumes, "
            "building the map theorem by theorem. The full edition "
            "audits sample theorems, exhibits the extraction rule, "
            "and gives the confirm/refute panel."
        ),
        "assumptions": [
            "A1: Choice usage in a proof is localizable to specific "
            "inference steps.",
            "A2: Each such step consumes a definite fragment "
            "(countable choice, dependent choice, etc.).",
            "A3: The minimal fragment for a theorem is the join of "
            "the fragments of its optimal proof.",
        ],
        "steps": [
            "Step 1: Take a theorem's proof and flag every "
            "choice-invoking step (arbitrary selections, maximal "
            "principles, well-orderings).",
            "Step 2: Classify each flagged step by the weakest "
            "fragment that justifies it.",
            "Step 3: Take the join: the theorem's choice-need is the "
            "least fragment covering all steps.",
            "Step 4: Audit samples: sequential compactness needs "
            "countable choice only; Tychonoff needs the ultrafilter "
            "lemma; Hahn-Banach needs the Boolean prime ideal "
            "theorem.",
            "Step 5: Aggregate: the map's lower envelope is the "
            "empirical answer to 'which fragment does ordinary math "
            "need?'",
        ],
        "confirm": [
            "If the audit reproduces the known reverse-mathematics "
            "classifications where they overlap, the extraction rule "
            "is validated.",
            "A completed audit of a whole textbook (say, real "
            "analysis) with a stable lower envelope would confirm "
            "the method's payoff.",
        ],
        "refute": [
            "Proofs whose choice usage resists localization (global "
            "choice smuggled through definitions) would refute A1.",
            "If the minimal fragment turns out proof-relative with "
            "no stable join, A3 fails and the map is ill-defined.",
        ],
        "not_claims": [
            "It does not claim full AC is dispensable - only that "
            "its necessity is theorem-relative.",
            "It does not deny the philosophical debate about AC's "
            "truth; it sidesteps it for the engineering question.",
            "It does not claim the audit is finished - it is a "
            "protocol for finishing it.",
        ],
        "citations": [CIT_GODEL40, CIT_COHEN, CIT_JECH],
    },
    {
        "key": "large-cardinals",
        "name": "The Large Cardinal Hierarchy",
        "group": "Incompleteness and Axioms",
        "ladder_rank": 21,
        "ladder_tier": "compounded",
        "problem": (
            "Large cardinal axioms assert the existence of "
            "unimaginably huge infinities - inaccessible, Mahlo, "
            "measurable, supercompact, huge. They form a nearly "
            "linear hierarchy of consistency strength, and set "
            "theorists trust them. But no one can prove any of them "
            "consistent (Goedel forbids it), and their justification "
            "- why believe in a supercompact cardinal? - is "
            "philosophy's problem. Is the hierarchy real "
            "mathematics or a shared article of faith?"
        ),
        "background": (
            "Large cardinals grew from measurable cardinals (Ulam, "
            "1930s; Scott, 1961) into a vast hierarchy calibrated by "
            "consistency strength - the field's central measuring "
            "stick, since nearly every natural theory's strength "
            "lands somewhere on it (a remarkable empirical "
            "linearity nobody fully understands). They decide "
            "concrete questions: projective determinacy follows "
            "from Woodin cardinals (Martin-Steel), and large "
            "cardinals calibrate the independence results of "
            "descriptive set theory. Yet their epistemic status is "
            "precarious: each is unprovable from below, the "
            "justifications (reflection principles, resemblance to "
            "V) are contested, and skeptics from finitists to "
            "pluralists question the whole enterprise. The "
            "justification problem - what entitles belief in large "
            "cardinals - is wide open."
        ),
        "why_it_matters": (
            "Large cardinals are the scaffolding of modern set "
            "theory: remove them and projective determinacy, the "
            "calibration of consistency strength, and much of "
            "inner model theory collapse. If the hierarchy is "
            "justified, mathematics has a principled way to climb "
            "beyond ZFC; if not, a century of set theory rests on "
            "convention. The linearity phenomenon itself - why "
            "strength is linear - may be the deepest open fact "
            "about the foundations."
        ),
        "sig_pointer": (
            "The Signature edition proposes a track-record "
            "justification: large cardinals earn credence the way "
            "scientific posits do - by novel predictive success "
            "(determinacy theorems, strength calibrations) - not by "
            "a priori insight. The full edition tabulates the track "
            "record, states the inference rule, and gives the "
            "confirm/refute panel."
        ),
        "assumptions": [
            "A1: Mathematical posits can be justified abductively: "
            "by the theorems they predict and unify.",
            "A2: Large cardinals have a genuine track record: "
            "projective determinacy, the linearity phenomenon, "
            "calibration successes.",
            "A3: Track-record justification is defeasible and "
            "comparative, not absolute.",
        ],
        "steps": [
            "Step 1: List the predictions: large cardinals implied "
            "determinacy results later proved via inner models; the "
            "hierarchy predicted the linearity of strength.",
            "Step 2: Apply the abductive rule: posit the entities "
            "that best explain the pattern of successes.",
            "Step 3: Compare rivals: no alternative picture "
            "predicts the same range - pluralism describes, it does "
            "not predict.",
            "Step 4: Bound the claim: justification is for the "
            "hierarchy's lower reaches first (measurable through "
            "Woodin), thinning as strength grows - credence tapers "
            "with distance from the track record.",
            "Step 5: State the defeater condition: a principled "
            "alternative explaining the successes without the "
            "cardinals would overturn the inference.",
        ],
        "confirm": [
            "Each new determinacy or calibration theorem derived "
            "from large cardinals before any alternative route "
            "confirms the track record.",
            "If the linearity phenomenon gets an independent "
            "explanation, the abductive case strengthens further.",
        ],
        "refute": [
            "A principled rival explanation of the successes "
            "without large cardinals would defeat the abduction.",
            "An inconsistency derived from a large cardinal axiom "
            "(none known) would refute the hierarchy outright.",
        ],
        "not_claims": [
            "It does not claim large cardinals are 'true' in a "
            "platonist heaven - only that the posit is justified "
            "by its fruits.",
            "It does not justify the very top of the hierarchy "
            "equally; credence tapers.",
            "It does not deny the a priori programs; it offers an "
            "alternative route to the same confidence.",
        ],
        "citations": [CIT_KANAMORI, CIT_MARTIN, CIT_ANDRETTA],
    },
    {
        "key": "relevance-r",
        "name": "Decidability of Relevance Logic R",
        "group": "Proof, Computation, and Automation",
        "ladder_rank": 22,
        "ladder_tier": "compounded",
        "problem": (
            "Relevance logic R requires premises to be genuinely "
            "used in deriving conclusions - no irrelevant "
            "detours. Its neighbor RM is decidable; its fragments "
            "are decidable; but R itself, the flagship system of "
            "Anderson and Belnap's 'Entailment', has resisted every "
            "decidability proof and every undecidability proof for "
            "half a century. Is theoremhood in R decidable?"
        ),
        "background": (
            "Relevance logics arose in the 1960s-70s from the "
            "relevance critique of classical entailment: in classical "
            "logic 'if the moon is cheese then 2+2=4' is valid, "
            "though the premise is irrelevant. Anderson and "
            "Belnap's system R captures relevant entailment with a "
            "sophisticated proof theory (including the Ackermann "
            "constants and the distinctive contraction behavior). "
            "Decidability results surround it: the positive fragment "
            "is decidable, many neighbors (E, T, RM) are decidable, "
            "and Urquhart proved the undecidability of closely "
            "related systems. But R proper sits in a maddening gap: "
            "all known techniques fail in both directions. It is one "
            "of the most famous open problems in non-classical "
            "logic, a standing challenge since the 1970s."
        ),
        "why_it_matters": (
            "R is the canonical formalization of the idea that "
            "logic should track real inferential connection - the "
            "notion of 'following from' that science, law, and "
            "ordinary argument actually use. Its decidability "
            "determines whether relevant reasoning can be "
            "mechanized: a decidable R gives automated tools a "
            "relevance-respecting logic; an undecidable R proves a "
            "hard limit on mechanizing genuine implication. Either "
            "answer is landmark."
        ),
        "sig_pointer": (
            "The Signature edition proposes a proof-search "
            "normalization attack: every R-proof can be "
            "transformed into one where contraction is bounded by a "
            "function of the end-sequent's complexity, which would "
            "yield decidability. The full edition states the "
            "normalization conjecture, sketches the transformation, "
            "and gives the confirm/refute panel."
        ),
        "assumptions": [
            "A1: Contraction is the sole source of R's proof-search "
            "unboundedness.",
            "A2: There exists a complexity measure on sequents such "
            "that contraction beyond a bound is always eliminable.",
            "A3: The relevant proof theory (Belnap's display or the "
            "sequent systems) is the right setting for the "
            "normalization.",
        ],
        "steps": [
            "Step 1: Isolate the difficulty: in R, contraction can "
            "duplicate formulas without bound, defeating naive "
            "proof search.",
            "Step 2: Conjecture the bound: any R-theorem has a proof "
            "where each formula is contracted at most f(n) times, "
            "n the end-sequent's complexity.",
            "Step 3: Sketch the transformation: permute contractions "
            "downward and absorb redundant copies using R's "
            "Ackermann constants.",
            "Step 4: Derive decidability: bounded proof search over "
            "the normalized space terminates - theoremhood becomes "
            "decidable.",
            "Step 5: Note the fallback: if the bound fails, the "
            "failure's shape suggests the undecidability reduction "
            "- the conjecture is win-win.",
        ],
        "confirm": [
            "A proved normalization bound for R would settle the "
            "half-century problem affirmatively - full confirmation.",
            "Even partial bounds (for fragments approaching R) "
            "would strongly support the approach.",
        ],
        "refute": [
            "An undecidability proof for R would refute the "
            "conjecture outright.",
            "A family of R-theorems requiring unbounded contraction "
            "under every normalization strategy would kill the "
            "specific bound.",
        ],
        "not_claims": [
            "It does not claim R is decidable - it proposes the "
            "attack route, honestly flagging both outcomes.",
            "It does not claim the bound is small; decidability "
            "needs only finiteness.",
            "It does not deny the problem's difficulty - fifty "
            "years of failure is the baseline.",
        ],
        "citations": [CIT_ANDERSON, CIT_RESTALL],
    },
    {
        "key": "hol-atp",
        "name": "Complete Proof Search for Higher-Order Logic",
        "group": "Proof, Computation, and Automation",
        "ladder_rank": 23,
        "ladder_tier": "compounded",
        "problem": (
            "First-order automated provers are complete: given "
            "enough time, resolution and superposition will find "
            "any proof. Higher-order logic - the logic of "
            "real mathematics, with quantification over functions "
            "and predicates - has no such practical completeness. "
            "Higher-order unification is undecidable in general "
            "(Huet), and every existing higher-order prover is "
            "incomplete in practice. Is there a complete and "
            "usable proof search for HOL, or is incompleteness "
            "here a permanent engineering ceiling?"
        ),
        "background": (
            "Automated theorem proving conquered first-order logic: "
            "Robinson's resolution (1965) plus modern refinements "
            "(superposition, SMT) give complete search - "
            "semi-decidability realized in software that wins "
            "competitions. Higher-order logic resists: Church's "
            "simple type theory is the working logic of proof "
            "assistants (HOL Light, Isabelle/HOL), but automation "
            "there relies on incomplete heuristics, first-order "
            "translations (sledgehammer), or decidable fragments "
            "like higher-order patterns (Miller). Huet (1973) "
            "proved third-order unification undecidable, so full "
            "completeness is impossible in the absolute sense - "
            "but the open question is practical: is there a "
            "complete-enough strategy, complete for the theorems "
            "mathematicians actually prove, or a principled "
            "characterization of the complete fragment? The "
            "engineering frontier is live and unresolved."
        ),
        "why_it_matters": (
            "Proof assistants are the future of verified "
            "mathematics and verified software; their bottleneck is "
            "automation. A complete practical HOL search would "
            "multiply the power of every proof assistant, "
            "accelerating verified AI, verified cryptography, and "
            "formalized mathematics. The question also probes a "
            "deep boundary: which reasoning can be mechanized, and "
            "which inherently needs human guidance?"
        ),
        "sig_pointer": (
            "The Signature edition proposes a stratified search: "
            "decompose HOL goals into a first-order skeleton plus "
            "higher-order residue, solve the skeleton completely, "
            "and bound the residue by pattern-unification with "
            "iterative deepening on order. The full edition runs "
            "the stratification on sample theorems, tunes the "
            "deepening schedule, and gives the confirm/refute "
            "panel."
        ),
        "assumptions": [
            "A1: Practical HOL theorems have a first-order "
            "skeleton carrying most of the proof's structure.",
            "A2: The higher-order residue is pattern-unifiable in "
            "the overwhelming majority of real cases.",
            "A3: Iterative deepening on unification order is a "
            "complete strategy for the residue class in A2.",
        ],
        "steps": [
            "Step 1: Translate the HOL goal: extract the "
            "first-order skeleton by defunctionalizing the "
            "higher-order parts.",
            "Step 2: Run complete first-order search (superposition) "
            "on the skeleton - this terminates with proof or "
            "saturation.",
            "Step 3: Lift the skeleton proof, leaving higher-order "
            "residue constraints.",
            "Step 4: Attack the residue with pattern unification, "
            "deepening the permitted order iteratively.",
            "Step 5: Completeness claim (bounded): the strategy is "
            "complete for goals whose residue is pattern-unifiable - "
            "conjectured to cover practical mathematics.",
        ],
        "confirm": [
            "A prover implementing the stratification that matches "
            "or beats sledgehammer-style automation on proof-"
            "assistant benchmarks would confirm practical value.",
            "A theorem characterizing exactly the complete fragment "
            "would confirm the theory.",
        ],
        "refute": [
            "A corpus study showing real HOL theorems routinely "
            "need non-pattern unification would refute A2.",
            "If the skeleton extraction loses essential "
            "higher-order content (incompleteness at step 1), the "
            "stratification fails.",
        ],
        "not_claims": [
            "It does not claim to beat Huet's undecidability - full "
            "generality is impossible, and the proposal concedes it.",
            "It does not claim existing provers are obsolete; it "
            "claims a completeness characterization they lack.",
            "It does not deny that human guidance remains essential "
            "for hard theorems.",
        ],
        "citations": [CIT_ROBINSON, CIT_HUET],
    },
    {
        "key": "frege",
        "name": "Proof Complexity and the Frege Barrier",
        "group": "Proof, Computation, and Automation",
        "ladder_rank": 24,
        "ladder_tier": "compounded",
        "problem": (
            "Do short proofs of all tautologies exist in strong "
            "proof systems? If NP != coNP, then no propositional "
            "proof system has polynomial-size proofs of every "
            "tautology - but we cannot prove superpolynomial lower "
            "bounds for strong systems like Frege (textbook Hilbert-"
            "style proofs). The 'natural proofs' barrier "
            "(Razborov-Rudich) suggests why: many lower-bound "
            "techniques would break cryptography. Can the barrier "
            "be circumvented, or is proof complexity stuck until P "
            "vs NP falls?"
        ),
        "background": (
            "Proof complexity (Cook, Reckhow 1979) studies proof "
            "length as a function of theorem size; its central "
            "conjecture - no optimal propositional proof system - "
            "is equivalent to NP != coNP for strong enough systems. "
            "Lower bounds exist for weak systems (resolution, "
            "cutting planes) but the Frege barrier stands: no "
            "superpolynomial lower bound for Frege or Extended "
            "Frege is known. Razborov and Rudich (1997) showed "
            "'natural' circuit lower-bound proofs would yield "
            "algorithms breaking pseudorandom generators - so "
            "standard techniques cannot separate P from NP without "
            "breaking cryptography. Proof complexity is thus "
            "entangled with the deepest questions: circuit lower "
            "bounds, derandomization, and the P vs NP problem "
            "itself. Whether non-natural techniques can breach the "
            "Frege barrier is wide open."
        ),
        "why_it_matters": (
            "This is P vs NP wearing proof-theoretic clothes: a "
            "Frege lower bound would separate NP from coNP, a "
            "milestone toward the Clay prize problem. Conversely, "
            "short Frege proofs of hard tautologies would "
            "revolutionize automated reasoning - SAT solvers are "
            "weak proof systems, and stronger ones could crack "
            "currently impossible verification tasks. The barrier "
            "also guards cryptography: breaching it carelessly "
            "breaks the world's encryption."
        ),
        "sig_pointer": (
            "The Signature edition proposes a meta-complexity "
            "flanking maneuver: instead of direct lower bounds, "
            "prove that Frege lower bounds are themselves hard to "
            "prove in weak theories (bounded arithmetic), "
            "calibrating exactly what a breach would require. The "
            "full edition states the calibration, connects it to "
            "the natural-proofs barrier, and gives the "
            "confirm/refute panel."
        ),
        "assumptions": [
            "A1: The hardness of proving lower bounds is itself a "
            "meaningful complexity-theoretic fact.",
            "A2: Bounded arithmetic stratifies naturally with proof "
            "systems (the Cook-Nguyen program).",
            "A3: Non-natural proof techniques exist but are "
            "currently unformalized.",
        ],
        "steps": [
            "Step 1: Shift the target: from 'prove Frege lower "
            "bounds' to 'prove lower bounds on proving Frege lower "
            "bounds'.",
            "Step 2: Use the Paris-Wilkie translation: Frege lower "
            "bounds correspond to unprovability of reflection "
            "principles in bounded arithmetic.",
            "Step 3: Calibrate: show that breaching the Frege "
            "barrier requires techniques unformalizable below a "
            "precise arithmetical level.",
            "Step 4: Connect to natural proofs: the calibration "
            "explains WHY natural techniques fail - they live below "
            "the required level.",
            "Step 5: Extract the research program: hunt for "
            "mathematical techniques at exactly the calibrated "
            "level - the flanking maneuver becomes a map.",
        ],
        "confirm": [
            "If the calibration predicts the failure points of "
            "new lower-bound attempts, it is confirmed as a useful "
            "map.",
            "A non-natural lower-bound technique landing at the "
            "predicted level would be spectacular confirmation.",
        ],
        "refute": [
            "A Frege lower bound proved by clearly 'natural' "
            "methods would refute the barrier analysis underlying "
            "the calibration.",
            "If meta-complexity turns out to be as hard as the "
            "original problem with no payoff, the maneuver is "
            "empty.",
        ],
        "not_claims": [
            "It does not claim to prove any Frege lower bound - it "
            "maps the terrain.",
            "It does not claim P != NP or NP != coNP.",
            "It does not deny that a direct breach is possible; it "
            "prices the attempt.",
        ],
        "citations": [CIT_KRAJICEK, CIT_RAZBOROV],
    },
    # ------------------------------------------------------------- ADVANCED
    {
        "key": "bounded-arith",
        "name": "Circuit Lower Bounds in Weak Theories",
        "group": "Proof, Computation, and Automation",
        "ladder_rank": 25,
        "ladder_tier": "advanced",
        "problem": (
            "Bounded arithmetic theories (Buss's S_2, ...) formalize "
            "feasible reasoning - proofs whose concepts are "
            "polynomial-time. Paris and Kirby showed weak theories "
            "cannot prove strong combinatorial principles. The open "
            "frontier: can weak theories prove superpolynomial "
            "circuit lower bounds - the statements P vs NP is made "
            "of? If even strong bounded theories cannot, then "
            "feasible reasoning is blind to the P vs NP question, "
            "and the independence phenomenon reaches into "
            "complexity theory itself."
        ),
        "background": (
            "Bounded arithmetic (Paris-Kirby 1978, Buss 1986) "
            "stratifies arithmetic by the complexity of its "
            "induction principles; its theorems correspond to "
            "polynomial-time reasoning via witnessing theorems. "
            "The program's crown connection: S_2 proves the "
            "soundness of Extended Frege, so circuit lower bounds "
            "unprovable in S_2-style theories translate to "
            "proof-complexity lower bounds and back (the "
            "Cook-Nguyen theory). Known: weak theories cannot prove "
            "the pigeonhole principle's strong forms; Razborov "
            "showed S_2 cannot prove certain circuit lower bounds "
            "without collapsing complexity classes. Open: the exact "
            "unprovability frontier - which lower bounds escape "
            "which theories - and whether the P vs NP statement "
            "itself is independent of strong bounded arithmetic. "
            "An affirmative answer would make P vs NP "
            "Goedel-independent in a precise, feasible sense."
        ),
        "why_it_matters": (
            "If circuit lower bounds are unprovable in feasible "
            "theories, then P vs NP may be unresolvable by any "
            "reasoning humans can feasibly check - a fundamental "
            "limit on knowable complexity theory. The frontier "
            "also calibrates proof complexity: every unprovability "
            "result is a lower bound on what it takes to prove "
            "lower bounds. This is the meeting point of Goedel, "
            "Turing, and Cook - the deepest crossroads in logic."
        ),
        "sig_pointer": (
            "The Signature edition proposes a feasible-independence "
            "test: a combinatorial criterion on a lower-bound "
            "statement that predicts its unprovability in a given "
            "bounded theory, checkable without proving the "
            "independence. The full edition states the criterion, "
            "tests it against known results, and gives the "
            "confirm/refute panel."
        ),
        "assumptions": [
            "A1: Unprovability in bounded theories correlates with a "
            "combinatorial property of the statement (a Paris-"
            "Kirby-style growth condition).",
            "A2: The witnessing theorems give a complete bridge: "
            "unprovability iff no feasible witnessing function.",
            "A3: The criterion is decidable for syntactically "
            "presented lower-bound statements.",
        ],
        "steps": [
            "Step 1: Take a circuit lower-bound statement L and "
            "extract its Herbrand/witnessing complexity.",
            "Step 2: Apply the criterion: if L's witnesses require "
            "superpolynomial search in a precise sense, predict "
            "unprovability in S_2^i for calibrated i.",
            "Step 3: Verify against known cases: the pigeonhole "
            "variants and Razborov's results land where the "
            "criterion predicts.",
            "Step 4: Project to P vs NP: the full P!=NP statement's "
            "witness complexity exceeds every fixed level - "
            "predicting independence from all S_2^i.",
            "Step 5: Note the escape hatch: the criterion is "
            "conditional on standard complexity conjectures - "
            "honest circularity, flagged, not hidden.",
        ],
        "confirm": [
            "Each new unprovability result landing where the "
            "criterion predicted confirms it; a miss refines it.",
            "A proved instance of feasible independence for a "
            "major lower bound would be landmark confirmation.",
        ],
        "refute": [
            "A lower bound the criterion deems unprovable but "
            "proved in a weak theory refutes the criterion.",
            "If witnessing complexity turns out uncorrelated with "
            "unprovability, A1 fails.",
        ],
        "not_claims": [
            "It does not claim P vs NP is independent of PA or ZFC "
            "- only of feasible fragments, conditionally.",
            "It does not claim the criterion is proved; it is a "
            "proposed predictive tool.",
            "It does not deny that non-feasible proofs may settle "
            "P vs NP.",
        ],
        "citations": [CIT_BUSSD, CIT_PARIS, CIT_KRAJICEK],
    },
    {
        "key": "determinacy",
        "name": "Projective Determinacy and Beyond",
        "group": "Set-Theoretic Frontiers",
        "ladder_rank": 26,
        "ladder_tier": "advanced",
        "problem": (
            "Determinacy says: in every infinite two-player game on "
            "integers, one player has a winning strategy. For "
            "simple (Borel) games this is provable in ZFC; for "
            "projective games it needs large cardinals "
            "(Martin-Steel). The axiom of determinacy (AD) "
            "contradicts choice but holds in L(R) under large "
            "cardinals. Open: how far does determinacy extend, "
            "what is the exact large-cardinal strength of each "
            "level, and does the 'determinacy universe' give the "
            "right picture of the reals?"
        ),
        "background": (
            "Determinacy connects games, definability, and the "
            "structure of the reals: AD implies every set of reals "
            "in L(R) is Lebesgue measurable, has the perfect set "
            "property, and the Baire property - the regularity "
            "properties analysts want. Martin proved Borel "
            "determinacy in ZFC (1975); Martin and Steel (1989) "
            "proved projective determinacy from Woodin cardinals, "
            "and Woodin later showed it is equiconsistent with "
            "them. The inner-model program for AD (Woodin's "
            "derived-model and HOD analyses) maps the determinacy "
            "universe with extraordinary precision. Yet gaps "
            "remain: the exact strength of determinacy at higher "
            "projective levels, the structure of HOD in "
            "determinacy models, and whether AD+ (the technical "
            "strengthening) is the 'right' axiom - all open. "
            "Determinacy is also philosophically charged: it "
            "contradicts full choice, forcing a choice between "
            "beautiful reals and choice's conveniences."
        ),
        "why_it_matters": (
            "Determinacy decides what the real numbers look like: "
            "regular and well-behaved, or pathological. Every "
            "analyst's implicit picture of the continuum depends on "
            "regularity properties that ZFC alone cannot guarantee. "
            "The determinacy program is also the most successful "
            "large-cardinal application in history - its flagship "
            "evidence that the hierarchy pays rent. Mapping its "
            "limits maps the limits of the large-cardinal method "
            "itself."
        ),
        "sig_pointer": (
            "The Signature edition proposes a game-rank audit: each "
            "determinacy level is scored by the game complexity it "
            "tames, and the audit projects where the large-cardinal "
            "fuel runs out. The full edition runs the audit across "
            "the projective hierarchy, marks the fuel gauges, and "
            "gives the confirm/refute panel."
        ),
        "assumptions": [
            "A1: Determinacy strength is monotone in game "
            "complexity: harder games need stronger cardinals.",
            "A2: The Martin-Steel pattern (Woodin cardinals yield "
            "projective determinacy) is the template for higher "
            "levels.",
            "A3: Fuel exhaustion is detectable: a level whose "
            "determinacy exceeds all known cardinal strength "
            "signals the method's limit.",
        ],
        "steps": [
            "Step 1: Tabulate: Borel (ZFC), projective (Woodin "
            "cardinals), L(R) (AD, large cardinals), AD+ (stronger "
            "still).",
            "Step 2: Compute each level's regularity payoff: "
            "measurability, perfect set, uniformization - the "
            "analyst's dividend.",
            "Step 3: Mark the fuel gauge: current inner-model "
            "theory reaches a supercompact's neighborhood; beyond "
            "lies unmapped territory.",
            "Step 4: Project: the audit predicts the next "
            "determinacy level will require cardinals at or beyond "
            "the current inner-model frontier - a concrete, dated "
            "prediction.",
            "Step 5: Frame the philosophical payoff: if the fuel "
            "holds to the top of the projective hierarchy, the "
            "determinacy universe earns its claim as the right "
            "picture of the reals.",
        ],
        "confirm": [
            "Each new equiconsistency result landing on the "
            "audit's predicted cardinal level confirms the "
            "monotonicity.",
            "A determinacy level proved from weaker-than-expected "
            "cardinals would refine (not refute) the gauge.",
        ],
        "refute": [
            "A projective-level determinacy result requiring "
            "radically more - or provably less - than the audit's "
            "gauge would refute A1's smooth monotonicity.",
            "If inner-model theory stalls permanently below the "
            "needed strength, the projection fails practically.",
        ],
        "not_claims": [
            "It does not claim AD is true - it audits the "
            "conditional structure.",
            "It does not deny the philosophical cost: determinacy "
            "contradicts full choice, and the audit prices that.",
            "It does not predict the fuel never runs out; "
            "exhaustion is a live option the audit watches for.",
        ],
        "citations": [CIT_MARTIN, CIT_WOODIN, CIT_SOLOVAY],
    },
    {
        "key": "inner-model",
        "name": "The Inner Model Problem",
        "group": "Set-Theoretic Frontiers",
        "ladder_rank": 27,
        "ladder_tier": "advanced",
        "problem": (
            "Goedel's L is the canonical inner model for small "
            "large cardinals - but L cannot accommodate a "
            "measurable cardinal, let alone a supercompact. The "
            "inner model program builds canonical L-like models "
            "for stronger and stronger cardinals. It has reached "
            "Woodin cardinals; the supercompact barrier stands. "
            "The open problem: construct a canonical inner model "
            "for a supercompact cardinal - or prove it cannot be "
            "done."
        ),
        "background": (
            "Inner model theory is set theory's fine-structure "
            "program: build minimal, canonical universes (L, then "
            "L[U], then extender models) that capture large "
            "cardinals while keeping Goedel-like control - "
            "condensation, fine structure, combinatorial "
            "principles. Jensen's fine structure for L, then "
            "Mitchell-Steel extender models climbing through "
            "Woodin cardinals, represent decades of the hardest "
            "technical work in foundations. The supercompact "
            "level resists: supercompactness measures seem to "
            "require long extenders that break the fine-structural "
            "machinery, and Woodin has suggested the barrier may "
            "be fundamental - perhaps no canonical inner model "
            "for a supercompact exists. The problem is both "
            "technical (build it) and metamathematical (prove "
            "impossibility), and it gates the Ultimate-L program "
            "and the analysis of HOD."
        ),
        "why_it_matters": (
            "A canonical inner model for a supercompact would "
            "complete the large-cardinal calibration project: "
            "every natural theory's strength would have a "
            "canonical witness. Failure - a proved impossibility "
            "- would be equally momentous, showing the universe "
            "of sets has no canonical core at high strength and "
            "vindicating pluralism. Either way it decides the "
            "shape of set-theoretic truth at the highest reaches."
        ),
        "sig_pointer": (
            "The Signature edition proposes a barrier-diagnostic: "
            "classify exactly which fine-structural property fails "
            "at the supercompact level, and test whether the "
            "failure is local (repairable with new machinery) or "
            "global (a theorem of impossibility in waiting). The "
            "full edition runs the diagnostic, exhibits the failing "
            "property, and gives the confirm/refute panel."
        ),
        "assumptions": [
            "A1: The obstruction is identifiable: some specific "
            "fine-structural lemma fails for long extenders.",
            "A2: Local failures admit new machinery; global "
            "failures yield impossibility theorems.",
            "A3: The Mitchell-Steel analysis is the right baseline "
            "for the diagnostic.",
        ],
        "steps": [
            "Step 1: Run the extender-model construction at the "
            "supercompact level and locate the first failing "
            "lemma (condensation for long extenders).",
            "Step 2: Classify: does the failure use only "
            "combinatorial features of supercompactness measures "
            "(suggesting globality) or artifacts of the current "
            "machinery (suggesting locality)?",
            "Step 3: If local: sketch the machinery upgrade (a "
            "long-extender fine structure) and its predicted "
            "payoff.",
            "Step 4: If global: outline the impossibility proof's "
            "shape - a theorem that no fine-structural inner model "
            "can reach a supercompact.",
            "Step 5: State the bet: the diagnostic predicts which "
            "papers of the next decade will be constructions and "
            "which will be barrier results.",
        ],
        "confirm": [
            "If the identified lemma is exactly where new "
            "constructions stall, the diagnostic is confirmed as "
            "the right map.",
            "A proved impossibility (or a successful construction) "
            "at the predicted locus would be decisive.",
        ],
        "refute": [
            "A construction succeeding by a route the diagnostic "
            "deemed impossible refutes the classification.",
            "If the obstruction dissolves under re-examination "
            "(no real lemma fails), the barrier was illusory.",
        ],
        "not_claims": [
            "It does not claim to build the model - it diagnoses "
            "the barrier.",
            "It does not bet on construction versus impossibility; "
            "it gives the test distinguishing them.",
            "It does not deny Woodin's pessimism; it operationalizes "
            "it.",
        ],
        "citations": [CIT_KANAMORI, CIT_WOODIN],
    },
    {
        "key": "forcing-axioms",
        "name": "Forcing Axioms: Which Is Right?",
        "group": "Set-Theoretic Frontiers",
        "ladder_rank": 28,
        "ladder_tier": "advanced",
        "problem": (
            "Forcing axioms (Martin's Axiom, PFA, Martin's Maximum) "
            "assert the universe is 'fat' with generic filters, "
            "deciding countless independent statements - PFA makes "
            "the continuum aleph-2 and settles Suslin's hypothesis, "
            "the Whitehead problem's relatives, and more. They are "
            "mutually incompatible with some rivals and form a "
            "hierarchy of strength. Open: is there a 'right' forcing "
            "axiom - a maximal, canonical one - or is the choice "
            "among them as conventional as the choice of the "
            "continuum's size?"
        ),
        "background": (
            "Martin's Axiom (1970) began as a combinatorial "
            "principle with sweeping consequences; the Proper "
            "Forcing Axiom (Shelah, 1980s) and Martin's Maximum "
            "(Foreman-Magidor-Shelah) strengthened it into "
            "powerhouses deciding dozens of classical problems. "
            "Woodin's (*) axiom and the quest for ultimate "
            "forcing axioms continue the program. The axioms are "
            "justified by their fruitfulness - the beautiful "
            "mathematics they generate - but critics note this is "
            "pragmatic, not evidential: rival maximality "
            "principles (e.g., Woodin's Ultimate-L, which favors "
            "CH) pull in opposite directions. The incompatibility "
            "of the strongest forcing axioms with the strongest "
            "inner-model axioms is the central standoff in modern "
            "set theory, and there is no agreed criterion for "
            "declaring a winner."
        ),
        "why_it_matters": (
            "Forcing axioms are the most successful axiom "
            "candidates of the last fifty years by the "
            "fruitfulness metric - they decide more open problems "
            "per axiom than anything else on offer. If one of them "
            "is 'right', set theory gets its new foundation and "
            "dozens of classical problems fall at once. If the "
            "choice is conventional, then mathematical truth at "
            "this level is plural and the universe view is "
            "finished. The standoff with inner-model axioms is the "
            "foundations debate of our time."
        ),
        "sig_pointer": (
            "The Signature edition proposes a maximality tournament: "
            "forcing axioms and inner-model axioms are scored "
            "head-to-head on decidability yield per unit of "
            "consistency strength, and the 'right' axiom is the "
            "tournament's stable winner. The full edition runs the "
            "brackets, scores the rounds, and gives the "
            "confirm/refute panel."
        ),
        "assumptions": [
            "A1: Axioms can be compared by decidability yield "
            "divided by consistency strength - power per price.",
            "A2: The tournament is fair: both families' flagship "
            "results count, including negative results (what each "
            "rules out).",
            "A3: Stability across scoring variations indicates a "
            "real winner rather than an artifact.",
        ],
        "steps": [
            "Step 1: Seed the bracket: MA, PFA, MM, (*) versus "
            "V=Ultimate-L and large-cardinal maximality.",
            "Step 2: Score round one: PFA's decidability haul "
            "(continuum = aleph-2, Suslin, Whitehead relatives) "
            "against its strength cost.",
            "Step 3: Score round two: inner-model axioms' haul "
            "(CH, fine structure, HOD analysis) against theirs.",
            "Step 4: Check stability: vary the weights on "
            "fruitfulness versus naturalness - does the winner "
            "change?",
            "Step 5: Read the result: a stable winner earns the "
            "'right axiom' title provisionally; instability IS "
            "the pluralist verdict, honestly earned.",
        ],
        "confirm": [
            "If independent scoring efforts converge on the same "
            "winner, the tournament is confirmed as non-arbitrary.",
            "A new axiom candidate entering and winning cleanly "
            "would validate the format.",
        ],
        "refute": [
            "If every scoring variation flips the winner, A3 fails "
            "and the tournament proves only pluralism.",
            "A decisive mathematical result (e.g., completed "
            "Ultimate-L refuting PFA's picture) ends the tournament "
            "by knockout - the proposal concedes this gracefully.",
        ],
        "not_claims": [
            "It does not crown a winner in advance - the brackets "
            "must be run.",
            "It does not claim fruitfulness is the only virtue; "
            "the stability check varies the virtues.",
            "It does not deny that the standoff may be permanent - "
            "permanent instability is a finding, not a failure.",
        ],
        "citations": [CIT_WOODIN, CIT_JECH, CIT_SHELAH],
    },
    {
        "key": "justification",
        "name": "What Justifies a New Axiom?",
        "group": "Set-Theoretic Frontiers",
        "ladder_rank": 29,
        "ladder_tier": "advanced",
        "problem": (
            "Set theory needs new axioms - ZFC leaves CH, projective "
            "determinacy, and countless questions undecided. But what "
            "makes a proposed axiom worthy of belief? Intrinsic "
            "justifications (self-evidence, conceptual truth) and "
            "extrinsic ones (fruitfulness, predictive success) compete, "
            "and Maddy, Koellner, and others have shown each faces "
            "devastating objections. The problem: give an account of "
            "axiom justification that actual set theorists could use "
            "- or prove none exists."
        ),
        "background": (
            "Goedel distinguished intrinsic reasons (the axiom is "
            "true in virtue of the concept of set) from extrinsic "
            "ones (its consequences are verifiable, it unifies). "
            "Maddy's 'Believing the Axioms' (1988) argued the "
            "intrinsic/extrinsic divide is unworkable and proposed "
            "naturalism: adopt the axioms that best serve "
            "mathematics' goals. Koellner's work on the "
            "'independence phenomenon' and the limits of reflection "
            "principles sharpened the skeptical case. Meanwhile "
            "practice runs on a mix: set theorists cite "
            "fruitfulness, naturalness, and the track record of "
            "programs. But no articulated theory of justification "
            "commands assent, and the pluralists argue the search "
            "itself is misconceived - there is no fact about which "
            "axioms are true, only which universes are interesting. "
            "The methodology of foundations is itself unfounded."
        ),
        "why_it_matters": (
            "This is the foundations of the foundations: every "
            "proposal to extend ZFC - large cardinals, forcing "
            "axioms, determinacy - presupposes some answer, and the "
            "community operates on unarticulated norms. A correct "
            "account would discipline the field's most consequential "
            "decisions; a proved impossibility would end the "
            "universe-view project and hand victory to pluralism. "
            "It is philosophy with immediate mathematical "
            "consequences."
        ),
        "sig_pointer": (
            "The Signature edition proposes a practice-first "
            "reconstruction: justification is reverse-engineered "
            "from the axioms the community actually retains over "
            "decades, yielding explicit norms no one had to invent. "
            "The full edition mines the retention record, extracts "
            "the norms, tests them against live controversies, and "
            "gives the confirm/refute panel."
        ),
        "assumptions": [
            "A1: Long-run community retention is evidence of "
            "justification, not mere sociology.",
            "A2: The retained set (choice, replacement, large "
            "cardinals up to Woodin, PFA in its camp) exhibits "
            "extractable norms.",
            "A3: Norms extracted from retention apply prospectively "
            "to new candidates.",
        ],
        "steps": [
            "Step 1: Compile the retention record: which proposed "
            "axioms survived fifty years of scrutiny and which "
            "died.",
            "Step 2: Extract the norms: survivors share "
            "non-ad-hoc-ness, cross-program fruitfulness, and "
            "resilience under forcing (they are not easily "
            "killed).",
            "Step 3: Test the norms backward: do they predict the "
            "deaths (e.g., ad-hoc combinatorial principles that "
            "faded)?",
            "Step 4: Apply prospectively: score live candidates "
            "(Ultimate-L, (*), very large cardinals) against the "
            "extracted norms.",
            "Step 5: Answer the skeptic: the norms are not "
            "invented philosophy but the community's revealed "
            "epistemology - justification naturalized.",
        ],
        "confirm": [
            "If the extracted norms predict the next decade's "
            "retentions and abandonments, the reconstruction is "
            "confirmed.",
            "Convergence between the norms and the community's "
            "explicit self-understanding (surveys, debates) would "
            "support A1.",
        ],
        "refute": [
            "If retention turns out to be driven by sociology "
            "alone (fashion, authority), A1 fails and the norms "
            "are empty.",
            "A retained axiom violating all extracted norms would "
            "refute the extraction.",
        ],
        "not_claims": [
            "It does not claim the community is infallible - "
            "retention is evidence, not proof.",
            "It does not dissolve the intrinsic/extrinsic debate; "
            "it relocates it into the norms.",
            "It does not guarantee the norms pick a unique winner "
            "among live candidates.",
        ],
        "citations": [CIT_ANDRETTA, CIT_HAMKINS, CIT_KANAMORI],
    },
    {
        "key": "singular",
        "name": "Singular Cardinals and the SCH",
        "group": "Set-Theoretic Frontiers",
        "ladder_rank": 30,
        "ladder_tier": "advanced",
        "problem": (
            "The singular cardinal hypothesis (SCH) tames cardinal "
            "arithmetic at singular cardinals: it says 2^kappa is "
            "as small as possible for singular kappa. Easton showed "
            "ZFC leaves exponentiation wildly undetermined for "
            "regular cardinals; Silver showed SCH cannot fail too "
            "badly (its first failure needs large cardinals). "
            "Magidor used supercompacts to violate SCH. Open: what "
            "is the exact large-cardinal strength of SCH's failure, "
            "and does pcf theory (Shelah) already give the 'right' "
            "picture of singular cardinal arithmetic?"
        ),
        "background": (
            "Cardinal arithmetic is set theory's oldest industry: "
            "Koenig's theorem, Easton's theorem (1970) showing the "
            "continuum function on regulars is almost arbitrary, "
            "and then the singular case - harder, deeper. Silver's "
            "1974 theorem: if SCH fails, it fails big, and the "
            "first failure point is constrained. Jensen's covering "
            "lemma tied SCH to inner models: SCH holds in the "
            "core model, so its failure needs large cardinals. "
            "Shelah's pcf theory (1990s) revolutionized the area, "
            "proving ZFC theorems about singular cardinals "
            "(e.g., 2^{aleph_omega} < aleph_{omega_4}) that looked "
            "like independence results. The exact strength of 'SCH "
            "fails everywhere' and the completeness of the pcf "
            "picture remain open; Gitik, Merimovich, and others "
            "push the forcing constructions to ever-higher "
            "strengths."
        ),
        "why_it_matters": (
            "Cardinal arithmetic is the census of infinity: how "
            "many sizes there are and how exponentiation behaves. "
            "SCH's status decides whether singular cardinals are "
            "tame (pcf theory suffices) or wild (large cardinals "
            "rule). The area is also the sharpest test of the "
            "large-cardinal/inner-model duality: every SCH "
            "violation is a consistency-strength data point, and "
            "the complete map would finish a century-long "
            "program."
        ),
        "sig_pointer": (
            "The Signature edition proposes a strength-ledger: every "
            "known SCH violation and every pcf theorem is entered "
            "with its exact cardinal cost, and the ledger's gaps "
            "mark precisely where the next breakthrough must land. "
            "The full edition opens the ledger, totals the columns, "
            "and gives the confirm/refute panel."
        ),
        "assumptions": [
            "A1: Every SCH violation has a minimal large-cardinal "
            "cost, and the ledger can record it.",
            "A2: pcf theorems mark the ZFC baseline: anything the "
            "ledger cannot price above pcf is not yet shown to "
            "need strength.",
            "A3: Gaps in the ledger are predictions, not just "
            "ignorance.",
        ],
        "steps": [
            "Step 1: Enter the data: Silver (first failure needs "
            "strength), Magidor (supercompact violates), Gitik's "
            "violations with their costs.",
            "Step 2: Enter the pcf baseline: Shelah's ZFC bounds - "
            "the free theorems.",
            "Step 3: Compute the gaps: configurations with no known "
            "violation and no pcf theorem - the ledger's blank "
            "cells.",
            "Step 4: Read each gap as a priced prediction: 'a "
            "violation here costs at least X' - dated, checkable.",
            "Step 5: Total the columns: if the gaps close from "
            "above (stronger violations found), strength rules; if "
            "pcf fills them, tameness wins.",
        ],
        "confirm": [
            "Each blank cell filled at the ledger's predicted cost "
            "confirms the pricing.",
            "A pcf theorem filling a gap the ledger priced as "
            "expensive would be informative refinement.",
        ],
        "refute": [
            "A violation far cheaper than the ledger's minimum "
            "would refute the cost model.",
            "If minimal costs turn out to be ill-defined "
            "(non-comparable strengths), the ledger format fails.",
        ],
        "not_claims": [
            "It does not claim SCH is true or false - it prices "
            "the alternatives.",
            "It does not replace pcf theory; the ledger is built "
            "on it.",
            "It does not deny that the gaps may be permanent - "
            "permanent gaps are data too.",
        ],
        "citations": [CIT_SILVER, CIT_JECH, CIT_KANAMORI],
    },
    {
        "key": "hilbert24",
        "name": "Hilbert's 24th Problem",
        "group": "Foundations of Proof",
        "ladder_rank": 31,
        "ladder_tier": "advanced",
        "problem": (
            "Hilbert's famous 1900 list had 23 problems - but his "
            "notebooks contained a 24th, never published: find "
            "criteria of simplicity for proofs, and a theory of "
            "when one proof is simpler than another. The problem "
            "was recovered from his notes in 2000. It asks for an "
            "objective measure of proof simplicity - the "
            "foundation of proof theory's aesthetics and of "
            "automated proof evaluation. What makes one proof "
            "better than another?"
        ),
        "background": (
            "Ruediger Thiele found the 24th problem in Hilbert's "
            "notebooks and published it in 2000: Hilbert wanted "
            "'criteria of simplicity' and methods to show a given "
            "proof is the simplest possible. The problem slept for "
            "a century while proof theory developed exactly the "
            "tools it needs - cut-elimination, proof complexity, "
            " Curry-Howard, deep inference. Modern angles: proof "
            "length (complexity), conceptual resources used "
            "(reverse mathematics calibrates this), and "
            "explanatory power (a proof that explains versus one "
            "that merely verifies). Automated theorem provers "
            "need simplicity metrics to choose among proofs; "
            "mathematicians use them implicitly in every referee "
            "report. But no proposed measure commands consensus, "
            "and the criteria may be irreducibly plural - "
            "simplicity for checking versus simplicity for "
            "understanding."
        ),
        "why_it_matters": (
            "Proof simplicity is the quality metric of "
            "mathematics: it guides which proofs get published, "
            "taught, and trusted, and it will guide which proofs "
            "AI systems produce. A solved 24th problem would give "
            "proof assistants an objective to optimize, give "
            "education a principled notion of the 'right' proof, "
            "and settle whether mathematical beauty is objective "
            "or taste. It is Hilbert's lost question about what "
            "makes mathematics good."
        ),
        "sig_pointer": (
            "The Signature edition proposes a three-axis "
            "simplicity metric - length, conceptual depth, and "
            "explanatory transfer - and shows the axes are "
            "independent, explaining why no single measure ever "
            "won. The full edition scores famous proof pairs on "
            "all three axes, exhibits the independence, and gives "
            "the confirm/refute panel."
        ),
        "assumptions": [
            "A1: Simplicity decomposes into independent axes: "
            "length (symbols), depth (strongest principle used), "
            "transfer (how much the proof teaches).",
            "A2: No axis reduces to the others; trade-offs are "
            "genuine.",
            "A3: Mathematicians' simplicity judgments track "
            "weighted combinations of the axes.",
        ],
        "steps": [
            "Step 1: Score proof pairs: Euclid's infinitude of "
            "primes (short, shallow, high transfer) versus a "
            "brute-force verification (short to check, zero "
            "transfer).",
            "Step 2: Exhibit independence: find proofs "
            "optimal on each axis but poor on the others - no "
            "single winner.",
            "Step 3: Explain the century of disagreement: each "
            "camp measured one axis and mistook it for "
            "simplicity itself.",
            "Step 4: Recover Hilbert's demand: 'the simplest "
            "proof' is well-defined only relative to stated "
            "axis weights - the problem is solved by "
            "disambiguation.",
            "Step 5: Operationalize: proof assistants optimize "
            "per-axis; referees report axis scores; the metric "
            "is usable immediately.",
        ],
        "confirm": [
            "If mathematicians' pairwise simplicity judgments "
            "are predicted by the three-axis model better than "
            "by any single axis, the decomposition is confirmed.",
            "Adoption of axis scoring in proof-assistant "
            "tactics would be practical confirmation.",
        ],
        "refute": [
            "A simplicity judgment that no weighting of the "
            "three axes reproduces would refute the "
            "decomposition's completeness.",
            "If the axes turn out to be secretly correlated "
            "(one reduces to another), A2 fails.",
        ],
        "not_claims": [
            "It does not claim beauty is fully formalizable - "
            "only the simplicity component.",
            "It does not deny pluralism; it structures it.",
            "It does not claim Hilbert would have accepted the "
            "disambiguation - only that it answers his question "
            "as posed.",
        ],
        "citations": [CIT_HILBERT],
    },
    {
        "key": "categoricity",
        "name": "The Categoricity Question",
        "group": "Foundations of Proof",
        "ladder_rank": 32,
        "ladder_tier": "advanced",
        "problem": (
            "Second-order arithmetic pins down the natural numbers "
            "uniquely (Dedekind); second-order ZFC is "
            "quasi-categorical for the universe of sets. But the "
            "categoricity proofs use full second-order semantics - "
            "essentially set theory itself. Can categoricity be "
            "had internally - proved without stepping outside the "
            "theory? And does categoricity secure our grip on the "
            "intended structures, or does the Skolem-Loewenheim "
            "pressure (nonstandard models everywhere) show the "
            "grip was always illusory?"
        ),
        "background": (
            "Dedekind (1888) proved any two models of second-order "
            "arithmetic are isomorphic - categoricity, the "
            "mathematician's assurance that 'the natural numbers' "
            "means something definite. Zermelo (1930) gave the "
            "quasi-categoricity theorem for second-order set "
            "theory. But first-order theories cannot be categorical "
            "(Loewenheim-Skolem), and the second-order proofs "
            "themselves quantify over all subsets - using the very "
            "set-theoretic machinery in question. Recent work "
            "(Button, Walsh; Vaananen) on internal categoricity "
            "asks whether theories can prove their own "
            "categoricity from within. Meanwhile the philosophical "
            "stakes: does categoricity answer the skeptic who says "
            "our axioms do not pin down what we mean? Parsons, "
            "Lavine, and others debate whether categoricity "
            "theorems provide the intended reassurance or merely "
            "relocate the question to the semantics."
        ),
        "why_it_matters": (
            "Categoricity is about whether mathematics talks about "
            "definite things: are 'the natural numbers' one "
            "structure or an indefinite cloud of nonstandard "
            "models? If internal categoricity works, theories can "
            "secure their own subject matter - a foundational "
            "self-sufficiency. If not, mathematical reference "
            "rests on informal understanding no formalism "
            "captures, with consequences for formalization "
            "projects and AI mathematical reasoning."
        ),
        "sig_pointer": (
            "The Signature edition proposes a two-sense "
            "categoricity: external categoricity (the classical "
            "theorems, securing communication) versus internal "
            "categoricity (what the theory proves about itself, "
            "securing autonomy) - and argues the skeptic's demand "
            "conflates them. The full edition separates the "
            "senses, runs the Skolem pressure against each, and "
            "gives the confirm/refute panel."
        ),
        "assumptions": [
            "A1: Categoricity claims come in two senses: external "
            "(model-theoretic) and internal (provable in the "
            "theory).",
            "A2: The skeptic's challenge targets reference-"
            "fixing, which is the external sense's job.",
            "A3: Internal categoricity is valuable independently: "
            "it measures a theory's self-sufficiency.",
        ],
        "steps": [
            "Step 1: Separate the senses: Dedekind's theorem is "
            "external; Button-Walsh internal categoricity results "
            "are internal.",
            "Step 2: Show the skeptic equivocates: "
            "Loewenheim-Skolem pressure applies to first-order "
            "theories, while the reassurance was always "
            "second-order and external.",
            "Step 3: Grant the residue: external categoricity "
            "uses full semantics - the reassurance is real but "
            "not foundationally innocent.",
            "Step 4: Value the internal results on their own "
            "terms: a theory proving its models isomorphic is "
            "autonomous in a precise, new sense.",
            "Step 5: Conclude: reference is secured externally "
            "(good enough for practice), autonomy internally "
            "(good enough for foundations) - the demand for both "
            "at once was the confusion.",
        ],
        "confirm": [
            "If the two-sense distinction dissolves the "
            "standard objections in the literature (each "
            "objection targeting only one sense), the "
            "separation is confirmed.",
            "New internal categoricity results strengthening "
            "the autonomy sense would support A3.",
        ],
        "refute": [
            "An objection that defeats both senses jointly "
            "would refute the separation's sufficiency.",
            "If internal categoricity turns out to be "
            "mathematically trivial, A3's value claim fails.",
        ],
        "not_claims": [
            "It does not claim the skeptic is silenced - only "
            "that the challenge must pick its sense.",
            "It does not deny the circularity worry about "
            "full semantics; it prices it.",
            "It does not claim first-order theories can be "
            "categorical - Loewenheim-Skolem stands.",
        ],
        "citations": [CIT_GODEL31],
    },
    {
        "key": "constructive",
        "name": "The Constructive Content of Classical Theorems",
        "group": "Foundations of Proof",
        "ladder_rank": 33,
        "ladder_tier": "advanced",
        "problem": (
            "Classical mathematics proves existence non-"
            "constructively: 'there exists' via contradiction, "
            "choice functions with no rule, limits with no rate. "
            "Proof mining (Kohlenbach) extracts computational "
            "content from such proofs - rates of convergence, "
            "algorithms - from theorems that seemed purely "
            "existential. Open: which classical theorems are "
            "essentially non-constructive (no content to mine), "
            "and is there a principled boundary between the "
            "minable and the unminable?"
        ),
        "background": (
            "Brouwer's intuitionism (1910s-20s) rejected "
            "non-constructive existence as meaningless; "
            "classical mathematics ignored him and prospered. "
            "Goedel's Dialectica interpretation (1958) and "
            "Kreisel's unwinding program showed classical proofs "
            "could be mined for algorithms. Kohlenbach's proof "
            "mining (1990s-present) industrialized this: from "
            "proofs in analysis using weak Koenig's lemma and "
            "similar principles, it extracts explicit uniform "
            "bounds - new mathematics from old proofs. Reverse "
            "mathematics calibrates exactly which set-existence "
            "axioms each theorem needs. Yet the boundary is "
            "unmapped: some theorems (e.g., those essentially "
            "using full choice or strong comprehension) may have "
            "no nontrivial constructive content, and no theorem "
            "characterizes minability in general. The question "
            "is whether constructivity is a coherent, bounded "
            "property of theorems or a matter of degree without "
            "a principled edge."
        ),
        "why_it_matters": (
            "Every classical existence theorem is a potential "
            "algorithm waiting to be extracted - proof mining "
            "turns pure mathematics into software. Mapping the "
            "minable boundary tells us which parts of the "
            "mathematical literature are secretly computational "
            "and which are irreducibly ideal. It also adjudicates "
            "the century-old Brouwer-Hilbert dispute with data "
            "instead of polemics: how much of classical "
            "mathematics survives constructivization?"
        ),
        "sig_pointer": (
            "The Signature edition proposes a mining-yield "
            "spectrum: theorems are scored by the computational "
            "strength of what proof mining extracts, and the "
            "'essentially non-constructive' zone is where the "
            "yield provably collapses to trivial. The full "
            "edition scores sample theorems across analysis, "
            "exhibits the collapse zone, and gives the "
            "confirm/refute panel."
        ),
        "assumptions": [
            "A1: Mining yield is measurable: the extracted bound's "
            "uniformity and complexity class.",
            "A2: Yield correlates with the proof's logical "
            "strength (its reverse-mathematical level).",
            "A3: Collapse is provable: for some theorems, any "
            "extracted content is computably trivial.",
        ],
        "steps": [
            "Step 1: Score examples: the mean value theorem "
            "(high yield: explicit moduli), Bolzano-Weierstrass "
            "(moderate: weak Koenig's lemma bounds), full choice "
            "theorems (collapse).",
            "Step 2: Correlate with reverse mathematics: RCA_0 "
            "theorems mine cleanly, ACA_0 partially, full "
            "comprehension resists.",
            "Step 3: Exhibit the collapse zone: prove that for "
            "theorems equivalent to full choice over the base "
            "theory, extracted content is trivial.",
            "Step 4: Map the boundary: the minable/unminable edge "
            "runs through the comprehension hierarchy - a "
            "precise, checkable line.",
            "Step 5: Draw the Brouwer verdict: most of working "
            "analysis lies on the minable side - Hilbert wins "
            "pragmatically, Brouwer wins the boundary's "
            "existence.",
        ],
        "confirm": [
            "If new proof-mining case studies land on the "
            "predicted side of the boundary, the map is "
            "confirmed.",
            "A theorem proved unminable strictly inside the "
            "predicted minable zone would refine the boundary.",
        ],
        "refute": [
            "Nontrivial mined content from a theorem in the "
            "collapse zone would refute A3.",
            "If yield turns out uncorrelated with logical "
            "strength, the spectrum is decorative, not "
            "explanatory.",
        ],
        "not_claims": [
            "It does not claim all classical mathematics is "
            "constructive - the collapse zone is real.",
            "It does not settle Brouwer versus Hilbert "
            "philosophically; it gives the empirical map.",
            "It does not claim mining is automatic - extraction "
            "remains skilled labor.",
        ],
        "citations": [CIT_BROUWER, CIT_HILBERT],
    },
    {
        "key": "optimal-proof",
        "name": "Optimal Propositional Proof Systems",
        "group": "Proof, Computation, and Automation",
        "ladder_rank": 34,
        "ladder_tier": "advanced",
        "problem": (
            "Is there a best proof system for propositional "
            "tautologies - one that simulates every other with at "
            "most polynomial overhead? Krajicek and Pudlak (1989) "
            "posed the optimal proof system problem: a p-optimal "
            "system would be the universal proof checker. Its "
            "existence is tied to deep complexity separations "
            "(it would follow from NE = coNE, and its nonexistence "
            "from other conjectures). After 35 years: does an "
            "optimal propositional proof system exist?"
        ),
        "background": (
            "Cook and Reckhow (1979) defined propositional proof "
            "systems and showed a super proof system (polynomial "
            "proofs of all tautologies) exists iff NP = coNP. "
            "Krajicek and Pudlak refined this: p-optimal systems "
            "(optimal up to polynomial simulation) and the "
            "question of their existence, connecting it to "
            "exponential-time classes - optimal systems exist if "
            "NE = coNE, and strong conjectures imply they do not. "
            "The problem sits at the exact intersection of proof "
            "complexity and structural complexity theory: it is "
            "weaker than NP = coNP (so possibly resolvable "
            "independently) yet strong enough to imply major "
            "consequences. Partial results: optimal systems for "
            "restricted languages, connections to disjoint NP "
            "pairs and interpolation. But the core question - "
            "existence in full generality - is open, and it is "
            "the proof-complexity analogue of P vs NP in "
            "miniature: a clean, precise, apparently approachable "
            "problem that resists everything."
        ),
        "why_it_matters": (
            "An optimal proof system would be the ultimate "
            "automated reasoner for propositional logic: no "
            "proof search could asymptotically beat it. Its "
            "nonexistence would prove an eternal hierarchy of "
            "proof systems - reasoning itself has no ceiling. "
            "The problem is also the most approachable face of "
            "the P vs NP complex: weaker than the Clay problem, "
            "yet its resolution would reshape complexity theory. "
            "It is where Goedel's incompleteness, Turing's "
            "computability, and Cook's complexity finally meet."
        ),
        "sig_pointer": (
            "The Signature edition proposes a simulation-ladder "
            "attack: build an explicit tower of proof systems, "
            "each simulating the last, and test whether the tower "
            "converges (suggesting optimality is attainable) or "
            "provably diverges at each level (suggesting no "
            "optimum exists). The full edition builds the first "
            "rungs, runs the convergence test, and gives the "
            "confirm/refute panel."
        ),
        "assumptions": [
            "A1: Proof systems can be arranged in a simulation "
            "tower with explicit simulation overheads.",
            "A2: Convergence behavior of the tower correlates "
            "with the existence question.",
            "A3: Disjoint NP pairs and feasible interpolation "
            "are the right diagnostics for each rung.",
        ],
        "steps": [
            "Step 1: Build the tower: resolution at the base, "
            "then cutting planes, then Frege, then Extended "
            "Frege - each with known simulation gaps.",
            "Step 2: Attempt the next rung: a system simulating "
            "Extended Frege with subexponential overhead - the "
            "convergence test's first datum.",
            "Step 3: Diagnose each gap with disjoint NP pairs: "
            "separable pairs mark provable non-optimality at "
            "that rung.",
            "Step 4: Read the pattern: if every rung's gap is "
            "witnessed by an explicit hard pair, the tower "
            "diverges - evidence against optimality.",
            "Step 5: State the honest alternatives: convergence "
            "would suggest building the optimal system "
            "directly; divergence suggests proving "
            "non-existence via a diagonal across rungs.",
        ],
        "confirm": [
            "If each new rung's gap is witnessed as predicted, "
            "the divergence evidence accumulates toward a "
            "non-existence proof strategy.",
            "A rung that collapses the tower (simulating all "
            "below with polynomial overhead and resisting "
            "diagonalization) would flip the verdict toward "
            "existence.",
        ],
        "refute": [
            "A direct construction of a p-optimal system "
            "refutes the divergence reading immediately.",
            "If simulation overheads turn out to be "
            "unmeasurable in principle, the tower is not a "
            "test at all.",
        ],
        "not_claims": [
            "It does not claim to resolve the problem - it "
            "proposes the attack and reads the early data.",
            "It does not claim NP != coNP or any complexity "
            "separation.",
            "It does not deny the problem's 35-year resistance; "
            "the tower is built to measure exactly that "
            "resistance.",
        ],
        "citations": [CIT_KRAJICEK, CIT_RAZBOROV],
    },
]
