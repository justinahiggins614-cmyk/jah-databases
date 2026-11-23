// Seeded boundless generator for the The Signature College Mathematics Database ("signature" edition).
// Deterministic: the same seed always emits the same record.
// Usage: node gen-college-mathematics-signature.js [seed]  (prints one JSON record)
// or: node gen-college-mathematics-signature.js --test (runTests).
// Package-only; outputs are generated, not stored files.
"use strict";
const crypto = require("crypto");

const SLUG = "college-mathematics-signature";
const RECORD_KIND = "college mathematics record";
const ID_PREFIX = "JAH-COLMATHS-";
const AI_NAME = "JAH College Mathematics Librarian (Signature)";
const EDITION = "signature";
const SRC = "signature-generated";
const CEILING = "Generator ceiling: up to 1,000,000,000 scales per file, generated on demand by the file AI — not stored files.";

const TOPICS = [
  {
    "title": "Signature Design: The Proof Studio",
    "subject": "a Signature proof studio design",
    "description": "The Proof Studio is a Signature-made design for teaching proof: a workshop where a learner builds a proof step by step, each step naming its justification, with the machine checking that every step follows from earlier ones. A proof is a chain of statements in which each step follows by a stated rule; the studio makes the chain visible and checkable. The studio presents a claim, the allowed starting points, and a palette of proof moves. Each step records its justification, so a reader can audit the whole chain. A finished proof is exported as a readable document with its step count and its checks.",
    "inputs": "FIGURES = {'steps_in_guided_proof': 3, 'checks_performed': 5, 'n_tested': 5, 'sum_of_odds': 25, 'n_squared': 25, 'proof_moves_offered': 6, 'exports_supported': 2, 'design_version': 1}\nLABEL = 'a-signature-proof-studio-design'\n",
    "expected": "count: 8\nlabel: a-signature-proof-studio-design\nmax: 25\nmean: 9.0\nmin: 1\ntotal: 72\nResult: count=8|label=a-signature-proof-studio-design|max=25|mean=9.0|min=1|total=72\nRun 1 SHA-256: 5a60a0376b291445774f58daeebcec548b44d5e74fb54dddc9b1ddc09aad7802\nRun 2 SHA-256: 5a60a0376b291445774f58daeebcec548b44d5e74fb54dddc9b1ddc09aad7802\nDeterministic: MATCH\n"
  },
  {
    "title": "Signature Design: The Counting Workshop",
    "subject": "a Signature counting workshop design",
    "description": "The Counting Workshop is a Signature-made design for teaching counting: a bench where a learner builds arrangements and choices from physical tokens, watches the product rule multiply the choices, and checks a count by a second method. A permutation is an arrangement in order; a combination is a choice where order does not matter. The workshop gives tokens, boxes, and a counter that tracks the choices made. Each count is checked by a second method, such as counting the complement. The workshop exports a counting argument as a readable solution.",
    "inputs": "FIGURES = {'tokens': 4, 'arrangements': 24, 'combinations_of_2': 6, 'orders_per_pair': 2, 'checks_passed': 2, 'places': 4, 'choices_first': 4, 'design_version': 1}\nLABEL = 'a-signature-counting-workshop-design'\n",
    "expected": "count: 8\nlabel: a-signature-counting-workshop-design\nmax: 24\nmean: 5.875\nmin: 1\ntotal: 47\nResult: count=8|label=a-signature-counting-workshop-design|max=24|mean=5.875|min=1|total=47\nRun 1 SHA-256: 7bea391ffccd4f9271b839fa3a81f7204fd2ac4ab70e1bda6581f044560cfc05\nRun 2 SHA-256: 7bea391ffccd4f9271b839fa3a81f7204fd2ac4ab70e1bda6581f044560cfc05\nDeterministic: MATCH\n"
  },
  {
    "title": "Signature Design: The Function Laboratory",
    "subject": "a Signature function laboratory design",
    "description": "The Function Laboratory is a Signature-made design for exploring functions: a bench where a learner enters a rule, sees its graph drawn, traces inputs to outputs, and composes functions to see the composition drawn as a new graph. A function is a rule assigning exactly one output to each input. The laboratory draws the graph of any entered rule over a chosen domain. Tracing shows the input-output pair at each point of the graph. Composing two functions draws the composed graph and shows the intermediate value.",
    "inputs": "FIGURES = {'functions_entered': 2, 'points_traced': 4, 'composition_value_at_3': 10, 'composition_value_at_2': 5, 'composition_value_at_1': 2, 'composition_value_at_0': 1, 'graphs_drawn': 3, 'design_version': 1}\nLABEL = 'a-signature-function-laboratory-design'\n",
    "expected": "count: 8\nlabel: a-signature-function-laboratory-design\nmax: 10\nmean: 3.5\nmin: 1\ntotal: 28\nResult: count=8|label=a-signature-function-laboratory-design|max=10|mean=3.5|min=1|total=28\nRun 1 SHA-256: 86c988a7e4ef95894c47ebf0d8e47b19b3dc2ed136391bacb4f835bfca500133\nRun 2 SHA-256: 86c988a7e4ef95894c47ebf0d8e47b19b3dc2ed136391bacb4f835bfca500133\nDeterministic: MATCH\n"
  },
  {
    "title": "Signature Design: The Set Builder",
    "subject": "a Signature set builder design",
    "description": "The Set Builder is a Signature-made design for teaching sets: a tool where a learner defines sets by listing or by rule, and the tool draws unions, intersections, and complements as shaded regions, with counts shown for each region. A set is a collection of distinct objects. The builder accepts sets by listing or by a rule, such as even numbers below 20. Union, intersection, difference, and complement are drawn as shaded regions. Each region shows its count, and the counts are checked against the inclusion-exclusion formula.",
    "inputs": "FIGURES = {'set_a_size': 5, 'set_b_size': 3, 'union_size': 7, 'intersection_size': 1, 'difference_size': 4, 'regions_drawn': 4, 'checks_passed': 2, 'design_version': 1}\nLABEL = 'a-signature-set-builder-design'\n",
    "expected": "count: 8\nlabel: a-signature-set-builder-design\nmax: 7\nmean: 3.375\nmin: 1\ntotal: 27\nResult: count=8|label=a-signature-set-builder-design|max=7|mean=3.375|min=1|total=27\nRun 1 SHA-256: a60d7e6c8bdc5750fb5d51be80d7d9bd91ee82233fb9148d5f95f40567620d7a\nRun 2 SHA-256: a60d7e6c8bdc5750fb5d51be80d7d9bd91ee82233fb9148d5f95f40567620d7a\nDeterministic: MATCH\n"
  },
  {
    "title": "Signature Design: The Domino Proof",
    "subject": "a Signature domino proof design",
    "description": "The Domino Proof is a Signature-made design for teaching mathematical induction: a ladder of rungs, one per natural number, where proving the base case lights the first rung and proving the inductive step lights the next rung from any lit rung. Induction proves a claim for all natural numbers from a base case and an inductive step. Each rung is one natural number, with the claim stated for that number. Lighting the first rung is the base case; the step rule lights the next rung from any lit one. The ladder shows the first 10 rungs lit and states the general argument for all rungs.",
    "inputs": "FIGURES = {'rungs_lit': 10, 'proof_parts': 2, 'sum_to_10': 55, 'formula_at_10': 55, 'sum_to_3': 6, 'formula_at_3': 6, 'base_case': 1, 'design_version': 1}\nLABEL = 'a-signature-domino-proof-design'\n",
    "expected": "count: 8\nlabel: a-signature-domino-proof-design\nmax: 55\nmean: 17.0\nmin: 1\ntotal: 136\nResult: count=8|label=a-signature-domino-proof-design|max=55|mean=17.0|min=1|total=136\nRun 1 SHA-256: 7112a6d281ccbebcc834fea1b984d74ffeb292c0351033dadf93217313d1e08b\nRun 2 SHA-256: 7112a6d281ccbebcc834fea1b984d74ffeb292c0351033dadf93217313d1e08b\nDeterministic: MATCH\n"
  },
  {
    "title": "Signature Design: The Number Line Atlas",
    "subject": "a Signature number line atlas design",
    "description": "The Number Line Atlas is a Signature-made design for teaching number systems: a zoomable number line showing the natural numbers, integers, rationals, and reals, with irrational numbers marked as points that no fraction reaches. The real numbers fill the whole line; the rationals leave gaps. Zooming shows integers, then fractions between them, then the gaps where irrationals sit. The square root of 2 is marked at about 1.41421356, between the rationals 1.414 and 1.415. Completeness is shown as the claim that every point on the line is a real number.",
    "inputs": "FIGURES = {'number_systems': 4, 'zoom_levels': 3, 'sqrt2_marked': 1.41421356, 'pi_marked': 3.14159265, 'rationals_shown': 2, 'points_marked': 6, 'decimal_places': 8, 'design_version': 1}\nLABEL = 'a-signature-number-line-atlas-design'\n",
    "expected": "count: 8\nlabel: a-signature-number-line-atlas-design\nmax: 8\nmean: 3.5695\nmin: 1\ntotal: 28.5558\nResult: count=8|label=a-signature-number-line-atlas-design|max=8|mean=3.5695|min=1|total=28.5558\nRun 1 SHA-256: bbe5c3bd41efffd227c55400731e4cf4472d13106ad19d31223ecc5fbd8f45eb\nRun 2 SHA-256: bbe5c3bd41efffd227c55400731e4cf4472d13106ad19d31223ecc5fbd8f45eb\nDeterministic: MATCH\n"
  },
  {
    "title": "Signature Design: The Logic Table Builder",
    "subject": "a Signature logic table builder design",
    "description": "The Logic Table Builder is a Signature-made design for teaching logic: a tool where a learner enters a statement built from and, or, not, and implication, and the tool builds its truth table, showing the truth value for every combination of its parts. A statement is a sentence that is either true or false. The builder accepts statements with up to 3 parts and fills all 8 rows of the table. Equivalent statements are flagged when their columns match in every row. The contrapositive is generated automatically and shown to match the original.",
    "inputs": "FIGURES = {'rows_checked': 4, 'parts': 2, 'equivalences_found': 1, 'rows_for_3_parts': 8, 'rows_for_10_parts': 1024, 'cap_parts': 5, 'connectives_supported': 4, 'design_version': 1}\nLABEL = 'a-signature-logic-table-builder-design'\n",
    "expected": "count: 8\nlabel: a-signature-logic-table-builder-design\nmax: 1024\nmean: 131.125\nmin: 1\ntotal: 1049\nResult: count=8|label=a-signature-logic-table-builder-design|max=1024|mean=131.125|min=1|total=1049\nRun 1 SHA-256: dfdc50c8cc5d0b53d5d9a1249a3d233849b2c8fba1b3a8b7f1abed78e3952556\nRun 2 SHA-256: dfdc50c8cc5d0b53d5d9a1249a3d233849b2c8fba1b3a8b7f1abed78e3952556\nDeterministic: MATCH\n"
  },
  {
    "title": "Signature Design: The Sequence Explorer",
    "subject": "a Signature sequence explorer design",
    "description": "The Sequence Explorer is a Signature-made design for teaching sequences: a tool where a learner enters a formula for the n-th term, sees the first terms listed and plotted, and watches the terms approach a limit or diverge. A sequence converges when its terms get arbitrarily close to a limit and stay close. The explorer lists the first 20 terms and plots them against their index. A limit guess is tested by showing the error at terms 10, 100, and 1000. Divergent sequences are flagged when the terms do not settle.",
    "inputs": "FIGURES = {'terms_listed': 20, 'error_at_10': 0.1, 'error_at_100': 0.01, 'error_at_1000': 0.001, 'limit_confirmed': 0, 'checks': 3, 'first_term': 1, 'fifth_term': 0.2}\nLABEL = 'a-signature-sequence-explorer-design'\n",
    "expected": "count: 8\nlabel: a-signature-sequence-explorer-design\nmax: 20\nmean: 3.0389\nmin: 0\ntotal: 24.311\nResult: count=8|label=a-signature-sequence-explorer-design|max=20|mean=3.0389|min=0|total=24.311\nRun 1 SHA-256: 7520259be0c36e10f056dac0b0db2dcbdb2a9d6a5ab50e140bd9bb47c7a40617\nRun 2 SHA-256: 7520259be0c36e10f056dac0b0db2dcbdb2a9d6a5ab50e140bd9bb47c7a40617\nDeterministic: MATCH\n"
  },
  {
    "title": "Signature Design: The Complex Plane Studio",
    "subject": "a Signature complex plane studio design",
    "description": "The Complex Plane Studio is a Signature-made design for teaching complex numbers: a plane where a learner places a complex number a + b times i as a point, sees its modulus (its distance from the origin) and its argument (its angle), and multiplies numbers by rotating and scaling. The imaginary unit i satisfies i squared = -1. Placing a point shows its real part, imaginary part, modulus, and argument. Multiplying by i rotates a point by 90 degrees around the origin. Multiplying two numbers multiplies their moduli and adds their arguments.",
    "inputs": "FIGURES = {'points_placed': 3, 'modulus_1_plus_i': 1.4142, 'argument_degrees': 45, 'rotation_degrees': 90, 'product_modulus': 2, 'product_argument': 90, 'multiplications': 2, 'design_version': 1}\nLABEL = 'a-signature-complex-plane-studio-design'\n",
    "expected": "count: 8\nlabel: a-signature-complex-plane-studio-design\nmax: 90\nmean: 29.3018\nmin: 1\ntotal: 234.4142\nResult: count=8|label=a-signature-complex-plane-studio-design|max=90|mean=29.3018|min=1|total=234.4142\nRun 1 SHA-256: 17f2b8086f100c523540bbfb7957fa570aef39c189ac5c7305482b10ca1f8b60\nRun 2 SHA-256: 17f2b8086f100c523540bbfb7957fa570aef39c189ac5c7305482b10ca1f8b60\nDeterministic: MATCH\n"
  },
  {
    "title": "Signature Design: The Equivalence Class Sorter",
    "subject": "a Signature equivalence class sorter design",
    "description": "The Equivalence Class Sorter is a Signature-made design for teaching equivalence relations: a tool where a learner drops objects into classes, and the tool checks the three properties (reflexive, symmetric, transitive) and reports whether the sorting is a true equivalence. An equivalence relation splits a set into classes of equivalent elements. The sorter accepts a rule and a set of objects, and builds the classes. Each of the three properties is checked and reported separately. A failed property is shown with the pair of objects that breaks it.",
    "inputs": "FIGURES = {'numbers_sorted': 12, 'classes_built': 4, 'members_per_class': 3, 'properties_checked': 3, 'tests_run': 3, 'failures_shown': 1, 'modulus': 4, 'design_version': 1}\nLABEL = 'a-signature-equivalence-class-sorter-design'\n",
    "expected": "count: 8\nlabel: a-signature-equivalence-class-sorter-design\nmax: 12\nmean: 3.875\nmin: 1\ntotal: 31\nResult: count=8|label=a-signature-equivalence-class-sorter-design|max=12|mean=3.875|min=1|total=31\nRun 1 SHA-256: 840cf9ecf6f151cf3be8d79ec0950ec3301ba3cf14aa0826b17d7e3ef2a832a3\nRun 2 SHA-256: 840cf9ecf6f151cf3be8d79ec0950ec3301ba3cf14aa0826b17d7e3ef2a832a3\nDeterministic: MATCH\n"
  },
  {
    "title": "Signature Design: The Pigeonhole Boxes",
    "subject": "a Signature pigeonhole boxes design",
    "description": "The Pigeonhole Boxes is a Signature-made design for teaching the pigeonhole principle: a bench with boxes and objects where a learner places objects and watches the fullest box fill. The principle says that if more objects go into fewer boxes, some box holds more than one. The bench shows boxes, objects, and the count in each box as objects are placed. The guaranteed minimum in the fullest box is computed as the ceiling of objects over boxes. A counterexample attempt is blocked: the bench shows why no placement avoids the guarantee.",
    "inputs": "FIGURES = {'objects_1': 13, 'boxes_1': 12, 'guaranteed_1': 2, 'objects_2': 25, 'boxes_2': 7, 'guaranteed_2': 4, 'placements_shown': 2, 'design_version': 1}\nLABEL = 'a-signature-pigeonhole-boxes-design'\n",
    "expected": "count: 8\nlabel: a-signature-pigeonhole-boxes-design\nmax: 25\nmean: 8.25\nmin: 1\ntotal: 66\nResult: count=8|label=a-signature-pigeonhole-boxes-design|max=25|mean=8.25|min=1|total=66\nRun 1 SHA-256: 74a018c1e092877bebf336528e66928a5feb4a699a3ef804a10a4f61d2b77d5e\nRun 2 SHA-256: 74a018c1e092877bebf336528e66928a5feb4a699a3ef804a10a4f61d2b77d5e\nDeterministic: MATCH\n"
  },
  {
    "title": "Signature Design: The Overlap Counter",
    "subject": "a Signature overlap counter design",
    "description": "The Overlap Counter is a Signature-made design for teaching inclusion-exclusion: a Venn diagram tool where a learner toggles sets and watches the counter add, subtract, and add back the overlaps to give the exact union size. Inclusion-exclusion counts a union by alternating adding and subtracting intersections. Toggling a set updates the union count and shows each correction step. Each region of the diagram shows its count, and the sum of the regions equals the union. The tool checks the result against a direct count of the elements.",
    "inputs": "FIGURES = {'set_a': 10, 'set_b': 8, 'set_c': 6, 'pairwise_sum': 9, 'triple': 1, 'union': 16, 'regions': 7, 'counts_agreeing': 2}\nLABEL = 'a-signature-overlap-counter-design'\n",
    "expected": "count: 8\nlabel: a-signature-overlap-counter-design\nmax: 16\nmean: 7.375\nmin: 1\ntotal: 59\nResult: count=8|label=a-signature-overlap-counter-design|max=16|mean=7.375|min=1|total=59\nRun 1 SHA-256: ab867dee992379ad8076635ae6185ab469778581d845353c3eadeab9468f7f7e\nRun 2 SHA-256: ab867dee992379ad8076635ae6185ab469778581d845353c3eadeab9468f7f7e\nDeterministic: MATCH\n"
  },
  {
    "title": "Signature Design: The Fibonacci Garden",
    "subject": "a Signature Fibonacci garden design",
    "description": "The Fibonacci Garden is a Signature-made design for teaching recurrence: a garden where each new plant count is the sum of the two previous counts, growing the Fibonacci sequence visibly. A recurrence defines a sequence by its first values and a rule for later values in terms of earlier ones. Each generation is planted from the two before it, and the counts are shown. The ratio of successive counts is plotted and shown approaching about 1.618. The closed form is displayed alongside the recurrence for comparison.",
    "inputs": "FIGURES = {'generations': 10, 'fib_10': 55, 'fib_9': 34, 'ratio_10': 1.6176, 'ratio_8': 1.6154, 'golden_ratio': 1.618034, 'starting_values': 2, 'design_version': 1}\nLABEL = 'a-signature-fibonacci-garden-design'\n",
    "expected": "count: 8\nlabel: a-signature-fibonacci-garden-design\nmax: 55\nmean: 13.3564\nmin: 1\ntotal: 106.851\nResult: count=8|label=a-signature-fibonacci-garden-design|max=55|mean=13.3564|min=1|total=106.851\nRun 1 SHA-256: 50364fab23e66c3a9d75891394a2e41c147964f719384e18a158f6693fb181f2\nRun 2 SHA-256: 50364fab23e66c3a9d75891394a2e41c147964f719384e18a158f6693fb181f2\nDeterministic: MATCH\n"
  },
  {
    "title": "Signature Design: The For-All Game",
    "subject": "a Signature for-all game design",
    "description": "The For-All Game is a Signature-made design for teaching quantifiers: a game where a learner must prove a for-all statement by a general argument, prove a there-exists statement by exhibiting one example, and disprove a for-all statement by finding one counterexample. For all and there exists are the two quantifiers. Each round presents a quantified statement over a small domain. The player chooses a strategy: general argument, exhibit an example, or find a counterexample. The game scores the strategy, not just the answer, and explains a wrong choice.",
    "inputs": "FIGURES = {'rounds': 10, 'forall_rounds': 4, 'exists_rounds': 3, 'disproof_rounds': 3, 'hints_used': 2, 'strategies_corrected': 1, 'points_per_round': 10, 'design_version': 1}\nLABEL = 'a-signature-for-all-game-design'\n",
    "expected": "count: 8\nlabel: a-signature-for-all-game-design\nmax: 10\nmean: 4.25\nmin: 1\ntotal: 34\nResult: count=8|label=a-signature-for-all-game-design|max=10|mean=4.25|min=1|total=34\nRun 1 SHA-256: 56525681a73cbbb20c39d4c9f969efd7895fb37ad8c6ec98073bec1e17b72f0c\nRun 2 SHA-256: 56525681a73cbbb20c39d4c9f969efd7895fb37ad8c6ec98073bec1e17b72f0c\nDeterministic: MATCH\n"
  },
  {
    "title": "Signature Design: The Geometry Workbench",
    "subject": "a Signature geometry workbench design",
    "description": "The Geometry Workbench is a Signature-made design for teaching distance, angle, area, and volume: a bench where a learner places points, draws shapes, and reads off distances, angles, areas, and volumes computed from the coordinates. Distance in the plane follows the Pythagorean theorem. Placing two points shows their distance by the Pythagorean formula. Drawing a polygon shows its area, computed by the shoelace method (a sum over its vertices). A 3D mode shows boxes and spheres with their volumes.",
    "inputs": "FIGURES = {'points_placed': 3, 'distances_shown': 3, 'hypotenuse': 5, 'triangle_area': 6, 'box_volume': 24, 'box_sides': 3, 'angles_shown': 1, 'design_version': 1}\nLABEL = 'a-signature-geometry-workbench-design'\n",
    "expected": "count: 8\nlabel: a-signature-geometry-workbench-design\nmax: 24\nmean: 5.75\nmin: 1\ntotal: 46\nResult: count=8|label=a-signature-geometry-workbench-design|max=24|mean=5.75|min=1|total=46\nRun 1 SHA-256: 63077b57f23eda386cbf0844e5b49d35fa7a1c3086524587aacdbfec75af23c5\nRun 2 SHA-256: 63077b57f23eda386cbf0844e5b49d35fa7a1c3086524587aacdbfec75af23c5\nDeterministic: MATCH\n"
  },
  {
    "title": "Signature Design: The Probability Table",
    "subject": "a Signature probability table design",
    "description": "The Probability Table is a Signature-made design for teaching probability: a table of all equally likely outcomes where a learner highlights an event and reads its probability as favourable outcomes over total outcomes. Probability is a number between 0 and 1 measuring likelihood. The table lists all outcomes of a small experiment, such as two dice. Highlighting an event counts its outcomes and shows the probability as a fraction and a decimal. Independent events are shown as a product of probabilities.",
    "inputs": "FIGURES = {'outcomes': 36, 'ways_to_7': 6, 'prob_7': 0.1667, 'doubles': 6, 'at_least_one_6': 11, 'prob_6': 0.3056, 'events_highlighted': 3, 'design_version': 1}\nLABEL = 'a-signature-probability-table-design'\n",
    "expected": "count: 8\nlabel: a-signature-probability-table-design\nmax: 36\nmean: 7.934\nmin: 0.1667\ntotal: 63.4723\nResult: count=8|label=a-signature-probability-table-design|max=36|mean=7.934|min=0.1667|total=63.4723\nRun 1 SHA-256: 3f233604e6137cccee6b13c65d9be3c925a99e1c3f088a9711f55398392b46bb\nRun 2 SHA-256: 3f233604e6137cccee6b13c65d9be3c925a99e1c3f088a9711f55398392b46bb\nDeterministic: MATCH\n"
  },
  {
    "title": "Signature Design: The Euclid Machine",
    "subject": "a Signature Euclid machine design",
    "description": "The Euclid Machine is a Signature-made design for teaching the greatest common divisor: a machine where a learner enters two numbers and watches Euclid's algorithm divide with remainder until the remainder is zero. The greatest common divisor (GCD) is the largest integer dividing both numbers. Each step shows the division, the quotient, and the remainder. The last non-zero remainder is highlighted as the GCD. The machine also shows the combination of the two numbers that equals the GCD.",
    "inputs": "FIGURES = {'steps_test_1': 3, 'gcd_1': 21, 'steps_test_2': 3, 'gcd_2': 6, 'numbers_entered': 4, 'divisions_shown': 6, 'remainders_shown': 6, 'design_version': 1}\nLABEL = 'a-signature-euclid-machine-design'\n",
    "expected": "count: 8\nlabel: a-signature-euclid-machine-design\nmax: 21\nmean: 6.25\nmin: 1\ntotal: 50\nResult: count=8|label=a-signature-euclid-machine-design|max=21|mean=6.25|min=1|total=50\nRun 1 SHA-256: fbca4c32ea9847103c8059c74b3d033a0e2e41771fc10d6bf8ceb520659a33c8\nRun 2 SHA-256: fbca4c32ea9847103c8059c74b3d033a0e2e41771fc10d6bf8ceb520659a33c8\nDeterministic: MATCH\n"
  },
  {
    "title": "Signature Design: The Clock Arithmetic Dial",
    "subject": "a Signature clock arithmetic dial design",
    "description": "The Clock Arithmetic Dial is a Signature-made design for teaching modular arithmetic: a clock face with n hours where a learner adds and multiplies by moving the hand, and the hand's final position is the result modulo n. Modular arithmetic is arithmetic with remainders. The dial has n positions, and adding moves the hand forward that many steps, wrapping around. Multiplying is repeated adding, shown as repeated jumps. The inverse of a number is the jump that returns the hand to 1.",
    "inputs": "FIGURES = {'dial_hours': 7, 'sum_result': 4, 'product_result': 2, 'inverse_of_3': 5, 'inverse_check': 15, 'operations_shown': 3, 'turns_for_product': 4, 'design_version': 1}\nLABEL = 'a-signature-clock-arithmetic-dial-design'\n",
    "expected": "count: 8\nlabel: a-signature-clock-arithmetic-dial-design\nmax: 15\nmean: 5.125\nmin: 1\ntotal: 41\nResult: count=8|label=a-signature-clock-arithmetic-dial-design|max=15|mean=5.125|min=1|total=41\nRun 1 SHA-256: ea9b9ef67b24d56bbd1ac18380d358a3f2322bb9cf33beb25beb9d1866536ee8\nRun 2 SHA-256: ea9b9ef67b24d56bbd1ac18380d358a3f2322bb9cf33beb25beb9d1866536ee8\nDeterministic: MATCH\n"
  },
  {
    "title": "Signature Design: The Composition Pipeline",
    "subject": "a Signature composition pipeline design",
    "description": "The Composition Pipeline is a Signature-made design for teaching function composition: a pipeline of stages where a learner feeds a value in one end, watches it change at each stage, and reads the final output. Composition applies one function after another. Each stage is a function with its rule shown and its input and output displayed. Reordering the stages shows that composition is generally not commutative. An inverse stage undoes the stage before it, and the pipeline shows the round trip.",
    "inputs": "FIGURES = {'stages': 2, 'output_order_1': 49, 'output_order_2': 13, 'input': 2, 'after_stage_1': 7, 'after_stage_2': 49, 'round_trip_back': 2, 'design_version': 1}\nLABEL = 'a-signature-composition-pipeline-design'\n",
    "expected": "count: 8\nlabel: a-signature-composition-pipeline-design\nmax: 49\nmean: 15.625\nmin: 1\ntotal: 125\nResult: count=8|label=a-signature-composition-pipeline-design|max=49|mean=15.625|min=1|total=125\nRun 1 SHA-256: 9fcf8e3d4d621579e185d7738a34c08a076f09f5d2c5eff4416033b5ef84fd01\nRun 2 SHA-256: 9fcf8e3d4d621579e185d7738a34c08a076f09f5d2c5eff4416033b5ef84fd01\nDeterministic: MATCH\n"
  },
  {
    "title": "Signature Design: The Capstone Challenge Board",
    "subject": "a Signature capstone challenge board design",
    "description": "The Capstone Challenge Board is a Signature-made design for teaching combined problem solving: a board of challenges, each needing several ideas, where a learner plans the tools, solves each part, and assembles the parts into one argument. A capstone problem uses several ideas at once. Each challenge names the ideas it needs before the learner starts. Each part is solved and checked separately, then assembled. The board scores the plan, the checks, and the assembly, not just the final answer.",
    "inputs": "FIGURES = {'parts': 3, 'checks_passed': 3, 'combinations': 210, 'excluded': 84, 'answer': 126, 'challenges_on_board': 12, 'ideas_named': 4, 'design_version': 1}\nLABEL = 'a-signature-capstone-challenge-board-design'\n",
    "expected": "count: 8\nlabel: a-signature-capstone-challenge-board-design\nmax: 210\nmean: 55.375\nmin: 1\ntotal: 443\nResult: count=8|label=a-signature-capstone-challenge-board-design|max=210|mean=55.375|min=1|total=443\nRun 1 SHA-256: e8ca8bf0c5f844f08de44de5f2434773698d4f8aac434838237cba71c433a232\nRun 2 SHA-256: e8ca8bf0c5f844f08de44de5f2434773698d4f8aac434838237cba71c433a232\nDeterministic: MATCH\n"
  },
  {
    "title": "Signature Design: The Definition Dictionary",
    "subject": "a Signature definition dictionary design",
    "description": "The Definition Dictionary is a Signature-made design for teaching precise language: a dictionary where every term in the subject is defined in plain words, with an example and a non-example, and where a learner is quizzed by being shown a use and asked whether it matches the definition. A definition states exactly what a term means. Each entry gives the term, its plain-words definition, one example, and one non-example. The quiz shows a use and asks whether it matches, with the definition shown on demand. Terms are linked: each definition names the earlier terms it uses.",
    "inputs": "FIGURES = {'entries': 24, 'quiz_items': 8, 'matching_uses': 5, 'non_matching_uses': 3, 'score': 7, 'examples_per_entry': 1, 'non_examples_per_entry': 1, 'design_version': 1}\nLABEL = 'a-signature-definition-dictionary-design'\n",
    "expected": "count: 8\nlabel: a-signature-definition-dictionary-design\nmax: 24\nmean: 6.25\nmin: 1\ntotal: 50\nResult: count=8|label=a-signature-definition-dictionary-design|max=24|mean=6.25|min=1|total=50\nRun 1 SHA-256: a23e73aceca479e2012683e0ecaa8280c7a150300502cd6b9b588d3aa60cca18\nRun 2 SHA-256: a23e73aceca479e2012683e0ecaa8280c7a150300502cd6b9b588d3aa60cca18\nDeterministic: MATCH\n"
  },
  {
    "title": "Signature Design: The Estimation Bench",
    "subject": "a Signature estimation bench design",
    "description": "The Estimation Bench is a Signature-made design for teaching checking by estimation: a bench where a learner guesses an answer's size before computing, then compares the computed answer with the guess and explains any mismatch. Estimation is judging the size of an answer before computing it exactly. Each problem asks for an estimate first, then the exact computation. The bench shows the estimate, the exact answer, and the ratio between them. A mismatch above a factor of 2 is flagged and the learner must find the error.",
    "inputs": "FIGURES = {'problems': 3, 'estimate_1': 1000, 'exact_1': 912, 'ratio_1': 0.912, 'estimate_2': 100, 'exact_2': 100, 'factorial_7': 5040, 'flags': 0}\nLABEL = 'a-signature-estimation-bench-design'\n",
    "expected": "count: 8\nlabel: a-signature-estimation-bench-design\nmax: 5040\nmean: 894.489\nmin: 0\ntotal: 7155.912\nResult: count=8|label=a-signature-estimation-bench-design|max=5040|mean=894.489|min=0|total=7155.912\nRun 1 SHA-256: ab3bb82da72470b3a07343f516d5e9e64d3077f0d7bf26040bbf0be5ed0ad634\nRun 2 SHA-256: ab3bb82da72470b3a07343f516d5e9e64d3077f0d7bf26040bbf0be5ed0ad634\nDeterministic: MATCH\n"
  },
  {
    "title": "Signature Design: The Proof Review Circle",
    "subject": "a Signature proof review circle design",
    "description": "The Proof Review Circle is a Signature-made design for teaching proof review: a circle of learners where each proof is read by another learner, who must name the step they find hardest to follow and the step they find most elegant, before the proof is accepted. A proof is a chain of justified steps. Each proof is submitted with its steps and justifications listed. A reviewer must name one hard step and one elegant step, with reasons. A proof is accepted only after two reviews and a revision.",
    "inputs": "FIGURES = {'steps_submitted': 3, 'steps_revised': 4, 'reviewers': 2, 'revisions': 1, 'hard_steps_named': 1, 'elegant_steps_named': 1, 'proofs_reviewed': 6, 'design_version': 1}\nLABEL = 'a-signature-proof-review-circle-design'\n",
    "expected": "count: 8\nlabel: a-signature-proof-review-circle-design\nmax: 6\nmean: 2.375\nmin: 1\ntotal: 19\nResult: count=8|label=a-signature-proof-review-circle-design|max=6|mean=2.375|min=1|total=19\nRun 1 SHA-256: d3005cd29fe8322e9b0053cf5197a471a8d6733ab1d041693acee21a3e9d8056\nRun 2 SHA-256: d3005cd29fe8322e9b0053cf5197a471a8d6733ab1d041693acee21a3e9d8056\nDeterministic: MATCH\n"
  },
  {
    "title": "Signature Design: The Word Problem Translator",
    "subject": "a Signature word problem translator design",
    "description": "The Word Problem Translator is a Signature-made design for teaching translation between words and symbols: a tool where a learner reads a word problem, underlines the quantities, names the unknowns, writes the equation, solves it, and translates the answer back into words. Translation is the skill of turning a story into mathematics and back. Each problem is solved in 5 stages: quantities, unknowns, equation, solution, translation back. The tool checks each stage before the next opens. The final answer is stated as a sentence with its units.",
    "inputs": "FIGURES = {'stages': 5, 'quantities': 2, 'unknowns': 2, 'equations': 2, 'solution_x': 19, 'solution_y': 11, 'sum_check': 30, 'difference_check': 8}\nLABEL = 'a-signature-word-problem-translator-design'\n",
    "expected": "count: 8\nlabel: a-signature-word-problem-translator-design\nmax: 30\nmean: 9.875\nmin: 2\ntotal: 79\nResult: count=8|label=a-signature-word-problem-translator-design|max=30|mean=9.875|min=2|total=79\nRun 1 SHA-256: ad425e5efb2090c80cf16268bfcfc45671cb6da8c7867d8f7ff903ff531b81f8\nRun 2 SHA-256: ad425e5efb2090c80cf16268bfcfc45671cb6da8c7867d8f7ff903ff531b81f8\nDeterministic: MATCH\n"
  }
];

const SOURCES = [
  {
    "name": "Wikipedia - Mathematical proof",
    "url": "https://en.wikipedia.org/wiki/Mathematical_proof",
    "establishes": "The reference for a Signature proof studio design in this record."
  },
  {
    "name": "Wikipedia - Proof by induction",
    "url": "https://en.wikipedia.org/wiki/Proof_by_induction",
    "establishes": "The reference for a Signature proof studio design in this record."
  }
];

function mulberry32(seed) {
  let a = seed >>> 0;
  return function () {
    a |= 0; a = (a + 0x6D2B79F5) | 0;
    let t = Math.imul(a ^ (a >>> 15), 1 | a);
    t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t;
    return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
  };
}

function canonical(obj) {
  if (obj === null || typeof obj !== "object") return JSON.stringify(obj);
  if (Array.isArray(obj)) return "[" + obj.map(canonical).join(",") + "]";
  const keys = Object.keys(obj).sort();
  return "{" + keys.map((k) => JSON.stringify(k) + ":" + canonical(obj[k])).join(",") + "}";
}

function buildDemo(topic) {
  const code = "import hashlib\n" + topic.inputs +
    "def compute():\n" +
    "    total = sum(FIGURES.values())\n" +
    "    n = len(FIGURES)\n" +
    "    mean = round(total / n, 4) if n else 0\n" +
    "    out = {\"count\": n, \"label\": LABEL, \"max\": max(FIGURES.values()), " +
    "\"mean\": mean, \"min\": min(FIGURES.values()), \"total\": round(total, 4)}\n" +
    "    return out\n" +
    "outputs = compute()\n" +
    "result = \"|\".join(f\"{k}={v}\" for k, v in sorted(outputs.items()))\n" +
    "h1 = hashlib.sha256(result.encode()).hexdigest()\n" +
    "outputs2 = compute()\n" +
    "result2 = \"|\".join(f\"{k}={v}\" for k, v in sorted(outputs2.items()))\n" +
    "h2 = hashlib.sha256(result2.encode()).hexdigest()\n" +
    "for k, v in sorted(outputs.items()):\n" +
    "    print(f\"{k}: {v}\")\n" +
    "print(f\"Result: {result}\")\n" +
    "print(f\"Run 1 SHA-256: {h1}\")\n" +
    "print(f\"Run 2 SHA-256: {h2}\")\n" +
    "print(f\"Deterministic: {'MATCH' if h1 == h2 else 'MISMATCH'}\")\n";
  return { code: code, expected: topic.expected };
}

function generate(seed) {
  const rng = mulberry32(seed);
  const topic = TOPICS[Math.floor(rng() * TOPICS.length)];
  const idx = seed % 1000000;
  const id = ID_PREFIX + "GEN-" + String(idx).padStart(6, "0");
  const demo = buildDemo(topic);
  const rec = {
    id: id,
    slug: SLUG,
    edition: EDITION,
    record_kind: RECORD_KIND,
    title: topic.title + " (Generated " + idx + ")",
    subject: topic.subject,
    status: "built",
    src: SRC,
    ai_name: AI_NAME,
    description: topic.description + (EDITION === "signature"
      ? " Design-study: this is a Signature-made design, labelled design-study throughout, never presented as established fact or as an authentic public record."
      : " Established college-level knowledge, checked against its cited sources."),
    body: "<h2>Description</h2><p>" + topic.description + "</p>",
    demo: demo.code,
    expected_output: demo.expected,
    program: "class GeneratedProgram:\n    def run(self):\n        return {\"deterministic\": True}\n",
    sources: SOURCES,
    generator: { type: "seeded boundless generator", gen_id_prefix: ID_PREFIX + "GEN-", hard_stop: 1000000000, throttle_per_call: 100, ceiling_note: CEILING },
    scales: { A1: "One generated record: the same shape as the filed records, with its own figures.", A2: "The whole edition: every generated record joins the 24 filed records.", A3: "The subject against the whole network: every college subject linked, every record searchable." },
  };
  const slim = {};
  for (const k of Object.keys(rec)) slim[k] = rec[k];
  rec.jcc_key = "k=" + crypto.createHash("sha256").update(canonical(slim)).digest("hex").slice(0, 8);
  rec.jcc_code = "JAHDB/" + SLUG + "#" + id;
  return rec;
}

function runTests() {
  let passed = 0, failed = 0;
  function t(name, ok) { if (ok) { passed++; } else { failed++; console.log("FAIL: " + name); } }
  const a = generate(42), b = generate(42);
  t("same seed twice identical", JSON.stringify(a) === JSON.stringify(b));
  t("record_kind", a.record_kind === RECORD_KIND);
  t("slug", a.slug === SLUG);
  t("slug signature form", EDITION === "signature" ? (a.slug.split("-signature").length - 1) === 1 : a.slug.indexOf("-signature") === -1);
  t("id prefix own family", a.id.indexOf(ID_PREFIX) === 0);
  t("generator hard_stop 1e9", a.generator.hard_stop === 1000000000);
  t("generator gen prefix own family", a.generator.gen_id_prefix === ID_PREFIX + "GEN-");
  t("jcc_code form", a.jcc_code === "JAHDB/" + SLUG + "#" + a.id);
  const slim = {}; for (const k of Object.keys(a)) { if (k !== "jcc_code" && k !== "jcc_key") slim[k] = a[k]; }
  t("jcc_key round-trip", a.jcc_key === "k=" + crypto.createHash("sha256").update(canonical(slim)).digest("hex").slice(0, 8));
  t("different seeds differ", JSON.stringify(generate(42)) !== JSON.stringify(generate(43)));
  t("19 keys", Object.keys(a).length === 19);
  console.log("Tests: " + passed + " passed, " + failed + " failed");
  return failed === 0;
}

if (require.main === module) {
  const arg = process.argv[2];
  if (arg === "--test") {
    process.exit(runTests() ? 0 : 1);
  }
  const seed = arg === undefined ? 1 : parseInt(arg, 10);
  if (!Number.isFinite(seed)) { console.error("seed must be an integer"); process.exit(2); }
  console.log(JSON.stringify(generate(seed)));
}
module.exports = { generate, runTests };
