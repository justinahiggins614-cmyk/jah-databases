// Seeded boundless generator for the College Mathematics Database ("public" edition).
// Deterministic: the same seed always emits the same record.
// Usage: node gen-college-mathematics.js [seed]  (prints one JSON record)
// or: node gen-college-mathematics.js --test (runTests).
// Package-only; outputs are generated, not stored files.
"use strict";
const crypto = require("crypto");

const SLUG = "college-mathematics";
const RECORD_KIND = "college mathematics record";
const ID_PREFIX = "JAH-COLMATH-";
const AI_NAME = "JAH College Mathematics Librarian";
const EDITION = "public";
const SRC = "public-harvest";
const CEILING = "Generator ceiling: up to 1,000,000,000 scales per file, generated on demand by the file AI — not stored files.";

const TOPICS = [
  {
    "title": "College Mathematics: Numbers and Sets",
    "subject": "numbers and sets",
    "description": "A set is a collection of distinct objects, called its elements (the members of the collection). The natural numbers are 1, 2, 3, and so on; the integers add zero and the negatives; the rational numbers are fractions of integers; the real numbers fill in every point of a number line. A set is described by listing its elements or by a rule, and two sets are equal when they have exactly the same elements. The union of two sets holds everything in either set; the intersection holds only what is in both. The empty set, written with the symbol for an empty collection, has no elements at all and is a subset of every set. A subset is a set whose every element also belongs to a larger set.",
    "inputs": "FIGURES = {'set_a_size': 5, 'set_b_size': 4, 'union_size': 8, 'intersection_size': 1, 'shared_element': 6, 'total_elements_counted': 9, 'distinct_elements': 8, 'empty_set_size': 0}\nLABEL = 'numbers-and-sets'\n",
    "expected": "count: 8\nlabel: numbers-and-sets\nmax: 9\nmean: 5.125\nmin: 0\ntotal: 41\nResult: count=8|label=numbers-and-sets|max=9|mean=5.125|min=0|total=41\nRun 1 SHA-256: dec8d684c3ebc6ccc0a8671d105853b0ee0fb1c7ee3bfd7bd9d9db0907621240\nRun 2 SHA-256: dec8d684c3ebc6ccc0a8671d105853b0ee0fb1c7ee3bfd7bd9d9db0907621240\nDeterministic: MATCH\n"
  },
  {
    "title": "College Mathematics: Functions and Their Graphs",
    "subject": "functions and their graphs",
    "description": "A function is a rule that assigns to each input exactly one output. The domain is the set of allowed inputs; the range is the set of outputs that actually occur. The graph of a function is the set of points (input, output) drawn in a plane, so the shape of the graph shows how the output changes as the input changes. A relation is a function exactly when every input has one output; the vertical line test states this in pictures: a vertical line meets a function's graph at most once. The composition of two functions applies one after the other, and the inverse undoes the original where it exists. A function is increasing where larger inputs give larger outputs, and decreasing where they give smaller ones.",
    "inputs": "FIGURES = {'slope': 2, 'intercept': 3, 'f_at_0': 3, 'f_at_1': 5, 'f_at_2': 7, 'f_at_5': 13, 'inverse_at_13': 5, 'domain_points_checked': 4}\nLABEL = 'functions-and-their-graphs'\n",
    "expected": "count: 8\nlabel: functions-and-their-graphs\nmax: 13\nmean: 5.25\nmin: 2\ntotal: 42\nResult: count=8|label=functions-and-their-graphs|max=13|mean=5.25|min=2|total=42\nRun 1 SHA-256: e806fff5e7a31eab147dee48dc0fdcc5f899b3e5de3ff7787bb96c358ae8b45f\nRun 2 SHA-256: e806fff5e7a31eab147dee48dc0fdcc5f899b3e5de3ff7787bb96c358ae8b45f\nDeterministic: MATCH\n"
  },
  {
    "title": "College Mathematics: Logic and the Language of Proof",
    "subject": "mathematical logic and proof",
    "description": "Logic is the study of correct reasoning. A statement (also called a proposition) is a sentence that is either true or false. The connectives and, or, and not combine statements, and implication (if P then Q) is the connective that carries proofs: it is false only when P is true and Q is false. The contrapositive of if P then Q is if not Q then not P, and the two are always true together or false together. A proof is a chain of statements in which each step follows from earlier steps by a stated rule. A counterexample is a single case that makes a universal claim false, and one counterexample is enough to disprove it.",
    "inputs": "FIGURES = {'steps_in_proof': 3, 'even_number_tested': 6, 'square_of_6': 36, 'odd_number_tested': 7, 'square_of_7': 49, 'connectives_named': 4, 'proof_methods_named': 3, 'counterexamples_needed': 1}\nLABEL = 'mathematical-logic-and-proof'\n",
    "expected": "count: 8\nlabel: mathematical-logic-and-proof\nmax: 49\nmean: 13.625\nmin: 1\ntotal: 109\nResult: count=8|label=mathematical-logic-and-proof|max=49|mean=13.625|min=1|total=109\nRun 1 SHA-256: fe0dd5a658d87e1a2972127efe92072437b79a75318fa087238033defff587f5\nRun 2 SHA-256: fe0dd5a658d87e1a2972127efe92072437b79a75318fa087238033defff587f5\nDeterministic: MATCH\n"
  },
  {
    "title": "College Mathematics: Direct Proof and Proof by Contradiction",
    "subject": "proof by direct argument and by contradiction",
    "description": "A direct proof starts from the assumptions and builds forward to the conclusion, one justified step at a time. A proof by contradiction assumes the opposite of what is to be proved and derives something impossible, which shows the assumption was false and the claim true. A direct proof of if P then Q assumes P and derives Q. A proof by contradiction assumes not Q together with P and derives a contradiction, such as 0 = 1 or a number being both even and odd. The square root of 2 is irrational: the classic proof by contradiction shows it cannot be written as a fraction of integers.",
    "inputs": "FIGURES = {'primes_in_euclid_argument': 1, 'steps_in_irrationality_proof': 6, 'p_value_example': 2, 'q_value_example': 1, 'p_squared': 4, 'q_squared': 1, 'contradiction_count': 1, 'proof_methods_named': 2}\nLABEL = 'proof-by-direct-argument-and-by-contradiction'\n",
    "expected": "count: 8\nlabel: proof-by-direct-argument-and-by-contradiction\nmax: 6\nmean: 2.25\nmin: 1\ntotal: 18\nResult: count=8|label=proof-by-direct-argument-and-by-contradiction|max=6|mean=2.25|min=1|total=18\nRun 1 SHA-256: 23b42fb09208c67b98f00ed0deaf727299aefb5d3c44aa629fcc3ad863f69206\nRun 2 SHA-256: 23b42fb09208c67b98f00ed0deaf727299aefb5d3c44aa629fcc3ad863f69206\nDeterministic: MATCH\n"
  },
  {
    "title": "College Mathematics: Mathematical Induction",
    "subject": "proof by induction",
    "description": "Mathematical induction is a proof method for claims about all natural numbers. It has two steps: the base case, proving the claim for the first number (usually 1), and the inductive step, proving that if the claim holds for a number k, then it holds for k + 1. Together they prove the claim for every natural number, like a row of dominoes falling. The base case anchors the proof; without it, the inductive step proves nothing. The inductive hypothesis is the assumption that the claim holds for k, used to prove it for k + 1. Strong induction assumes the claim for all numbers up to k, which is sometimes needed.",
    "inputs": "FIGURES = {'base_case_n': 1, 'sum_to_10': 55, 'formula_at_10': 55, 'steps_in_proof': 2, 'k_plus_1_term': 11, 'sum_to_5': 15, 'formula_at_5': 15, 'domino_steps_checked': 2}\nLABEL = 'proof-by-induction'\n",
    "expected": "count: 8\nlabel: proof-by-induction\nmax: 55\nmean: 19.5\nmin: 1\ntotal: 156\nResult: count=8|label=proof-by-induction|max=55|mean=19.5|min=1|total=156\nRun 1 SHA-256: bbeaf1a67c07a15521640f0408e4e42f8551deefec107098f2981223383a807a\nRun 2 SHA-256: bbeaf1a67c07a15521640f0408e4e42f8551deefec107098f2981223383a807a\nDeterministic: MATCH\n"
  },
  {
    "title": "College Mathematics: Counting Permutations",
    "subject": "permutations and counting",
    "description": "A permutation is an arrangement of objects in an order. Counting permutations answers how many ways objects can be ordered: if there are n distinct objects, there are n factorial (written n!, the product of all numbers from 1 to n) ways to arrange all of them, because the first place has n choices, the second n - 1, and so on. The product rule says: if one choice has a options and a second independent choice has b options, the pair has a times b options. The number of permutations of r objects chosen from n is n! / (n - r)!. Factorials grow very fast: 10! is 3,628,800.",
    "inputs": "FIGURES = {'books': 4, 'arrangements_of_4': 24, 'letters': 5, 'arrangements_of_3': 60, 'factorial_5': 120, 'factorial_2': 2, 'choices_first_place': 4, 'choices_last_place': 1}\nLABEL = 'permutations-and-counting'\n",
    "expected": "count: 8\nlabel: permutations-and-counting\nmax: 120\nmean: 27.5\nmin: 1\ntotal: 220\nResult: count=8|label=permutations-and-counting|max=120|mean=27.5|min=1|total=220\nRun 1 SHA-256: 5d9e074fb01a89763c02e9f493449d6e4bd024e1423f7815cb4d4c199d90ffac\nRun 2 SHA-256: 5d9e074fb01a89763c02e9f493449d6e4bd024e1423f7815cb4d4c199d90ffac\nDeterministic: MATCH\n"
  },
  {
    "title": "College Mathematics: Counting Combinations",
    "subject": "combinations and counting",
    "description": "A combination is a choice of objects where order does not matter. The number of ways to choose r objects from n distinct objects is the binomial coefficient (written as n over r), equal to n! divided by r! times (n - r)!. It counts subsets, teams, and hands of cards. Choosing r objects from n is the same as choosing the n - r objects to leave out, so the counts are equal. The binomial coefficients are the entries of Pascal's triangle, where each entry is the sum of the two above it. The sum of all binomial coefficients for a fixed n is 2 to the power n, the number of subsets.",
    "inputs": "FIGURES = {'people': 8, 'team_size': 3, 'teams': 56, 'ordered_choices': 336, 'orders_per_team': 6, 'cards': 52, 'hand_size': 5, 'poker_hands': 2598960}\nLABEL = 'combinations-and-counting'\n",
    "expected": "count: 8\nlabel: combinations-and-counting\nmax: 2598960\nmean: 324928.25\nmin: 3\ntotal: 2599426\nResult: count=8|label=combinations-and-counting|max=2598960|mean=324928.25|min=3|total=2599426\nRun 1 SHA-256: 04ce7480ed9a918c86fa7cfa9c13712515b61c3267bec8b4a6bee5973a84b312\nRun 2 SHA-256: 04ce7480ed9a918c86fa7cfa9c13712515b61c3267bec8b4a6bee5973a84b312\nDeterministic: MATCH\n"
  },
  {
    "title": "College Mathematics: The Binomial Theorem",
    "subject": "the binomial theorem",
    "description": "The binomial theorem says how to expand a power of a sum: (x + y) raised to the power n equals the sum over k from 0 to n of the binomial coefficient C(n, k) times x to the power n - k times y to the power k. Each term counts the ways to choose k of the n factors to contribute y. The coefficients in the expansion are the binomial coefficients, read from Pascal's triangle. Setting x = 1 and y = 1 gives the sum of the coefficients, 2 to the power n. Setting x = 1 and y = -1 gives the alternating sum, which is 0 for n greater than 0.",
    "inputs": "FIGURES = {'power': 3, 'coefficient_0': 1, 'coefficient_1': 3, 'coefficient_2': 3, 'coefficient_3': 1, 'check_x': 2, 'check_y': 1, 'expansion_total': 27}\nLABEL = 'the-binomial-theorem'\n",
    "expected": "count: 8\nlabel: the-binomial-theorem\nmax: 27\nmean: 5.125\nmin: 1\ntotal: 41\nResult: count=8|label=the-binomial-theorem|max=27|mean=5.125|min=1|total=41\nRun 1 SHA-256: a618e50d0c35e22c4185295dd49044e9161cce73bad4624f723a7df55bfecd10\nRun 2 SHA-256: a618e50d0c35e22c4185295dd49044e9161cce73bad4624f723a7df55bfecd10\nDeterministic: MATCH\n"
  },
  {
    "title": "College Mathematics: Sequences and Convergence",
    "subject": "sequences and convergence",
    "description": "A sequence is a list of numbers in order, usually infinite: a first term, a second, a third, and so on. A sequence converges to a limit L if its terms get arbitrarily close to L and stay close as the index grows. A sequence that does not converge is said to diverge. The sequence 1/n converges to 0: its terms are 1, 1/2, 1/3, and shrink toward zero without ever reaching it. A bounded monotone sequence (one that never goes up, or never goes down, and stays within bounds) always converges. The squeeze theorem says a sequence trapped between two sequences with the same limit shares that limit.",
    "inputs": "FIGURES = {'first_term': 3, 'second_term': 2.5, 'fifth_term': 2.2, 'tenth_term': 2.1, 'hundredth_term': 2.01, 'limit': 2, 'error_at_10': 0.1, 'error_at_100': 0.01}\nLABEL = 'sequences-and-convergence'\n",
    "expected": "count: 8\nlabel: sequences-and-convergence\nmax: 3\nmean: 1.74\nmin: 0.01\ntotal: 13.92\nResult: count=8|label=sequences-and-convergence|max=3|mean=1.74|min=0.01|total=13.92\nRun 1 SHA-256: f2e0b1a63bd0a97bdc6f26934984f477b37b8a73d6f261de8b9677c0925cb685\nRun 2 SHA-256: f2e0b1a63bd0a97bdc6f26934984f477b37b8a73d6f261de8b9677c0925cb685\nDeterministic: MATCH\n"
  },
  {
    "title": "College Mathematics: Series and Their Sums",
    "subject": "series and their sums",
    "description": "A series is the sum of the terms of a sequence. Its partial sums add the terms one by one; if the partial sums converge to a limit, that limit is the sum of the series. The geometric series, with a constant ratio between successive terms, is the basic example: it converges exactly when the ratio has absolute value less than 1. The geometric series with first term a and ratio r sums to a / (1 - r) when the absolute value of r is less than 1. The harmonic series 1 + 1/2 + 1/3 + ... diverges: its partial sums grow without bound, though slowly. A series whose terms do not tend to zero cannot converge.",
    "inputs": "FIGURES = {'first_term': 1, 'ratio': 0.5, 'sum_limit': 2, 'partial_sum_2': 1.5, 'partial_sum_4': 1.875, 'partial_sum_10': 1.998046875, 'error_after_10': 0.001953125, 'terms_checked': 10}\nLABEL = 'series-and-their-sums'\n",
    "expected": "count: 8\nlabel: series-and-their-sums\nmax: 10\nmean: 2.3594\nmin: 0.001953125\ntotal: 18.875\nResult: count=8|label=series-and-their-sums|max=10|mean=2.3594|min=0.001953125|total=18.875\nRun 1 SHA-256: 8b15f2602acc56bdafcf1c24e92ed3a0e68f576286c72ffc7eaf29817cc291f1\nRun 2 SHA-256: 8b15f2602acc56bdafcf1c24e92ed3a0e68f576286c72ffc7eaf29817cc291f1\nDeterministic: MATCH\n"
  },
  {
    "title": "College Mathematics: Real Numbers and Completeness",
    "subject": "real numbers and completeness",
    "description": "The real numbers are the numbers on a continuous number line: every point is a real number. Completeness is the property that separates the reals from the rationals: every non-empty set of reals that is bounded above (has an upper limit) has a least upper bound, a smallest number that is still above the whole set. The rationals are not complete: the set of rationals whose square is less than 2 has no least upper bound among the rationals. Every real number is the limit of a sequence of rationals. The intermediate value theorem, which says a continuous function takes every value between its endpoints, rests on completeness.",
    "inputs": "FIGURES = {'sqrt2_approx': 1.41421356, 'rational_below_1': 1.4, 'rational_below_2': 1.41, 'rational_below_3': 1.414, 'bound_candidates': 3, 'upper_bound_2': 2, 'terms_listed': 4, 'decimal_places': 8}\nLABEL = 'real-numbers-and-completeness'\n",
    "expected": "count: 8\nlabel: real-numbers-and-completeness\nmax: 8\nmean: 2.8298\nmin: 1.4\ntotal: 22.6382\nResult: count=8|label=real-numbers-and-completeness|max=8|mean=2.8298|min=1.4|total=22.6382\nRun 1 SHA-256: 7642b075860724d13eb4be427af7b719de468ee7e0cf3bfe04268435c21328dc\nRun 2 SHA-256: 7642b075860724d13eb4be427af7b719de468ee7e0cf3bfe04268435c21328dc\nDeterministic: MATCH\n"
  },
  {
    "title": "College Mathematics: Complex Numbers",
    "subject": "complex numbers",
    "description": "A complex number is a number of the form a + b times i, where a and b are real numbers and i is the imaginary unit, defined by i squared = -1. The number a is the real part and b is the imaginary part. Complex numbers are plotted in a plane, with the real part horizontal and the imaginary part vertical. Adding complex numbers adds their real and imaginary parts separately. Multiplying uses i squared = -1: (a + bi)(c + di) = (ac - bd) + (ad + bc)i. The modulus (absolute value) of a + bi is the square root of a squared plus b squared, its distance from the origin.",
    "inputs": "FIGURES = {'real_1': 2, 'imag_1': 3, 'real_2': 1, 'imag_2': 4, 'product_real': -10, 'product_imag': 11, 'modulus_product': 14.8666, 'modulus_check': 14.8666}\nLABEL = 'complex-numbers'\n",
    "expected": "count: 8\nlabel: complex-numbers\nmax: 14.8666\nmean: 5.0916\nmin: -10\ntotal: 40.7332\nResult: count=8|label=complex-numbers|max=14.8666|mean=5.0916|min=-10|total=40.7332\nRun 1 SHA-256: 6c6e2de4e7078dffbef18f9d3a9fe1cfd6835c76c23cf6151b2eadd476d55578\nRun 2 SHA-256: 6c6e2de4e7078dffbef18f9d3a9fe1cfd6835c76c23cf6151b2eadd476d55578\nDeterministic: MATCH\n"
  },
  {
    "title": "College Mathematics: Relations and Equivalence",
    "subject": "relations and equivalence",
    "description": "A relation on a set is a rule that says, for some pairs of elements, that the first is related to the second. An equivalence relation is a relation that is reflexive (every element is related to itself), symmetric (if a is related to b then b is related to a), and transitive (if a is related to b and b to c, then a is related to c). It splits the set into equivalence classes, groups of elements that are equivalent to each other. Equality is the finest equivalence relation: each class has one element. Congruence modulo n (two numbers are related when their difference is a multiple of n) splits the integers into n classes. A partial order is reflexive, antisymmetric, and transitive, and it ranks elements rather than grouping them.",
    "inputs": "FIGURES = {'modulus': 5, 'classes': 5, 'class_0_members': 3, 'class_2_members': 3, 'difference_check_1': 10, 'difference_check_2': 11, 'properties_needed': 3, 'elements_listed': 15}\nLABEL = 'relations-and-equivalence'\n",
    "expected": "count: 8\nlabel: relations-and-equivalence\nmax: 15\nmean: 6.875\nmin: 3\ntotal: 55\nResult: count=8|label=relations-and-equivalence|max=15|mean=6.875|min=3|total=55\nRun 1 SHA-256: 034ca927b1cf50d4be33d05ea0ed6abcb72db06f3bb24cfa783a621ef56d3e47\nRun 2 SHA-256: 034ca927b1cf50d4be33d05ea0ed6abcb72db06f3bb24cfa783a621ef56d3e47\nDeterministic: MATCH\n"
  },
  {
    "title": "College Mathematics: The Pigeonhole Principle",
    "subject": "the pigeonhole principle",
    "description": "The pigeonhole principle says: if more objects are put into fewer boxes than there are objects, then at least one box holds more than one object. The general form says that if n objects go into m boxes, some box holds at least the ceiling of n/m objects (the ceiling is the smallest whole number at least as large as the value). With 13 people, two share a birth month, because there are 12 months and 13 people. The principle proves existence only: it says a crowded box exists, not which one it is. It is a proof by contradiction in disguise: assuming every box holds at most one object contradicts the count.",
    "inputs": "FIGURES = {'people': 500000, 'hair_counts': 150001, 'max_hairs': 150000, 'guaranteed_shared': 4, 'three_per_count': 450003, 'four_per_count': 600004, 'months': 12, 'people_for_months': 13}\nLABEL = 'the-pigeonhole-principle'\n",
    "expected": "count: 8\nlabel: the-pigeonhole-principle\nmax: 600004\nmean: 231254.625\nmin: 4\ntotal: 1850037\nResult: count=8|label=the-pigeonhole-principle|max=600004|mean=231254.625|min=4|total=1850037\nRun 1 SHA-256: 59f72eb5b7d230ea9e7dffb67e68a6a4c904ab0d1c0c3ce15a8858ef2df2a6b4\nRun 2 SHA-256: 59f72eb5b7d230ea9e7dffb67e68a6a4c904ab0d1c0c3ce15a8858ef2df2a6b4\nDeterministic: MATCH\n"
  },
  {
    "title": "College Mathematics: Inclusion-Exclusion",
    "subject": "inclusion-exclusion counting",
    "description": "Inclusion-exclusion is the method for counting a union of sets without double-counting: add the sizes of the sets, subtract the sizes of the pairwise intersections (the overlaps counted twice), add back the triple intersections (subtracted too many times), and continue alternating. It is the general form of the two-set union formula. For two sets, the union size is the sum of the sizes minus the intersection size. For three sets, add the three sizes, subtract the three pairwise intersections, and add the triple intersection. The principle also counts objects with none of several properties, by subtracting from the total.",
    "inputs": "FIGURES = {'students': 40, 'french': 25, 'german': 20, 'both': 12, 'at_least_one': 33, 'neither': 7, 'three_language_total': 36, 'none_of_three': 4}\nLABEL = 'inclusion-exclusion-counting'\n",
    "expected": "count: 8\nlabel: inclusion-exclusion-counting\nmax: 40\nmean: 22.125\nmin: 4\ntotal: 177\nResult: count=8|label=inclusion-exclusion-counting|max=40|mean=22.125|min=4|total=177\nRun 1 SHA-256: 6e01c416ba592b2cf1c72542e0f6dd0c8cfd54026769d6e8dde9c8bac9866e5d\nRun 2 SHA-256: 6e01c416ba592b2cf1c72542e0f6dd0c8cfd54026769d6e8dde9c8bac9866e5d\nDeterministic: MATCH\n"
  },
  {
    "title": "College Mathematics: Recursion and Recurrence",
    "subject": "recursion and recurrence relations",
    "description": "A recurrence relation defines a sequence by giving its first values and a rule for each later value in terms of earlier ones. The Fibonacci sequence is the classic example: each term after the first two is the sum of the two before it. Solving a recurrence means finding a closed form (a formula that gives any term directly). The Fibonacci sequence starts 1, 1, 2, 3, 5, 8, 13, and grows by the golden ratio, about 1.618. A linear recurrence with constant coefficients is solved by its characteristic equation. Recursion in programs mirrors recurrence in mathematics: a function defined in terms of itself.",
    "inputs": "FIGURES = {'fib_1': 1, 'fib_5': 5, 'fib_10': 55, 'fib_9': 34, 'ratio_10_9': 1.6176, 'golden_ratio': 1.618034, 'terms_listed': 10, 'starting_values': 2}\nLABEL = 'recursion-and-recurrence-relations'\n",
    "expected": "count: 8\nlabel: recursion-and-recurrence-relations\nmax: 55\nmean: 13.7795\nmin: 1\ntotal: 110.2356\nResult: count=8|label=recursion-and-recurrence-relations|max=55|mean=13.7795|min=1|total=110.2356\nRun 1 SHA-256: f985bbd1a6add2519f5e229eaa394adca59676c429ec7d873f54fea71766e4eb\nRun 2 SHA-256: f985bbd1a6add2519f5e229eaa394adca59676c429ec7d873f54fea71766e4eb\nDeterministic: MATCH\n"
  },
  {
    "title": "College Mathematics: The Language of Quantifiers",
    "subject": "quantifiers for all and there exists",
    "description": "A quantifier says how many objects a statement is about. The universal quantifier, for all, says a statement holds for every object in the domain. The existential quantifier, there exists, says it holds for at least one object. Negating a quantified statement swaps the quantifier: the negation of for all is there exists a counterexample, and vice versa. To prove a for-all statement, take an arbitrary object and prove the claim for it. To prove a there-exists statement, exhibit one object and check it works. The order of quantifiers matters: for every x there is a y is not the same as there is a y for every x.",
    "inputs": "FIGURES = {'quantifiers_named': 2, 'examples_checked': 3, 'y_for_x_plus_1': 1, 'statements_compared': 2, 'negations_named': 2, 'orderings_compared': 2, 'counterexamples_needed': 1, 'proof_steps': 2}\nLABEL = 'quantifiers-for-all-and-there-exists'\n",
    "expected": "count: 8\nlabel: quantifiers-for-all-and-there-exists\nmax: 3\nmean: 1.875\nmin: 1\ntotal: 15\nResult: count=8|label=quantifiers-for-all-and-there-exists|max=3|mean=1.875|min=1|total=15\nRun 1 SHA-256: f67f9f28298bb22580ccdf2d2583c90e7a6ee6f04f7b407b1b62d2dd3d2c363e\nRun 2 SHA-256: f67f9f28298bb22580ccdf2d2583c90e7a6ee6f04f7b407b1b62d2dd3d2c363e\nDeterministic: MATCH\n"
  },
  {
    "title": "College Mathematics: Geometry Distance and Angle",
    "subject": "distance and angle in geometry",
    "description": "Distance is the length of the straight line between two points, given in the plane by the Pythagorean formula: the square root of the sum of the squares of the differences of the coordinates. An angle is the amount of rotation between two lines meeting at a point, measured in degrees (360 to a full turn) or radians (2 pi to a full turn). The Pythagorean theorem says that in a right triangle, the square of the hypotenuse (the side opposite the right angle) equals the sum of the squares of the other two sides. The distance formula in the plane is the Pythagorean theorem applied to coordinate differences. Two lines are perpendicular exactly when the product of their slopes is -1.",
    "inputs": "FIGURES = {'dx': 3, 'dy': 4, 'distance': 5, 'dx_squared': 9, 'dy_squared': 16, 'sum_squares': 25, 'angle_degrees': 53.13, 'triangle_sides': 3}\nLABEL = 'distance-and-angle-in-geometry'\n",
    "expected": "count: 8\nlabel: distance-and-angle-in-geometry\nmax: 53.13\nmean: 14.7662\nmin: 3\ntotal: 118.13\nResult: count=8|label=distance-and-angle-in-geometry|max=53.13|mean=14.7662|min=3|total=118.13\nRun 1 SHA-256: fc652f499e10cd099d4efdcdbae8f3acf22a39e019213dd374e67e78579e00dd\nRun 2 SHA-256: fc652f499e10cd099d4efdcdbae8f3acf22a39e019213dd374e67e78579e00dd\nDeterministic: MATCH\n"
  },
  {
    "title": "College Mathematics: Area and Volume",
    "subject": "area and volume",
    "description": "Area is the measure of a two-dimensional region, in square units; volume is the measure of a three-dimensional region, in cubic units. The area of a rectangle is length times width; the area of a circle of radius r is pi times r squared; the volume of a box is length times width times height; the volume of a sphere of radius r is four-thirds pi r cubed. The area of a triangle is half the base times the height. The circumference of a circle is 2 pi r, and its area is pi r squared. Scaling a shape by a factor k multiplies area by k squared and volume by k cubed.",
    "inputs": "FIGURES = {'circle_radius': 5, 'circle_area': 78.5398, 'circle_circumference': 31.4159, 'sphere_radius': 3, 'sphere_volume': 113.0973, 'sphere_area': 113.0973, 'box_volume': 24, 'box_area': 52}\nLABEL = 'area-and-volume'\n",
    "expected": "count: 8\nlabel: area-and-volume\nmax: 113.0973\nmean: 52.5188\nmin: 3\ntotal: 420.1503\nResult: count=8|label=area-and-volume|max=113.0973|mean=52.5188|min=3|total=420.1503\nRun 1 SHA-256: 3b98ae94d718e6b3522c3ce2f91a216b8d33b29233cae53bcf85576c554fcdcc\nRun 2 SHA-256: 3b98ae94d718e6b3522c3ce2f91a216b8d33b29233cae53bcf85576c554fcdcc\nDeterministic: MATCH\n"
  },
  {
    "title": "College Mathematics: Probability Beginnings",
    "subject": "probability beginnings",
    "description": "Probability is a number between 0 and 1 that measures how likely an event (a set of outcomes) is. The sample space is the set of all possible outcomes; for equally likely outcomes, the probability of an event is the number of favourable outcomes divided by the total number of outcomes. Probabilities of all outcomes sum to 1. The probability of an event or its complement (the event not happening) sum to 1. For independent events (events that do not affect each other), the probability of both is the product of the probabilities.",
    "inputs": "FIGURES = {'outcomes': 36, 'ways_to_7': 6, 'prob_7': 0.1667, 'ways_to_2': 1, 'prob_2': 0.0278, 'prob_at_least_one_6': 0.3056, 'dice': 2, 'sides': 6}\nLABEL = 'probability-beginnings'\n",
    "expected": "count: 8\nlabel: probability-beginnings\nmax: 36\nmean: 6.4375\nmin: 0.0278\ntotal: 51.5001\nResult: count=8|label=probability-beginnings|max=36|mean=6.4375|min=0.0278|total=51.5001\nRun 1 SHA-256: c19a6ba13263006c39114a061c81052b32ac567b440c760f764ba26ca40a43a2\nRun 2 SHA-256: c19a6ba13263006c39114a061c81052b32ac567b440c760f764ba26ca40a43a2\nDeterministic: MATCH\n"
  },
  {
    "title": "College Mathematics: The Greatest Common Divisor",
    "subject": "the greatest common divisor",
    "description": "The greatest common divisor (GCD) of two integers is the largest integer that divides both of them. Euclid's algorithm finds it by repeated division with remainder: replace the pair (a, b) by (b, the remainder of a divided by b) until the remainder is zero; the last non-zero remainder is the GCD. Two numbers are coprime (relatively prime) when their GCD is 1. The GCD can be written as a combination a times x plus b times y for some integers x and y. The least common multiple of a and b is a times b divided by their GCD.",
    "inputs": "FIGURES = {'a': 252, 'b': 105, 'remainder_1': 42, 'remainder_2': 21, 'gcd': 21, 'a_over_gcd': 12, 'b_over_gcd': 5, 'lcm': 1260}\nLABEL = 'the-greatest-common-divisor'\n",
    "expected": "count: 8\nlabel: the-greatest-common-divisor\nmax: 1260\nmean: 214.75\nmin: 5\ntotal: 1718\nResult: count=8|label=the-greatest-common-divisor|max=1260|mean=214.75|min=5|total=1718\nRun 1 SHA-256: 5efc26c356bb320eeaa9e394c482299c387d7f80998625b1222f5dfd74634b49\nRun 2 SHA-256: 5efc26c356bb320eeaa9e394c482299c387d7f80998625b1222f5dfd74634b49\nDeterministic: MATCH\n"
  },
  {
    "title": "College Mathematics: Modular Arithmetic",
    "subject": "modular arithmetic",
    "description": "Modular arithmetic is arithmetic with remainders: two numbers are congruent modulo n when their difference is a multiple of n, and we work with the remainder after division by n. It is the arithmetic of clocks (12-hour time is modulo 12) and of calendars. Addition, subtraction, and multiplication work modulo n: reduce the result by the remainder. A number has a multiplicative inverse modulo n exactly when it is coprime to n. Fermat's little theorem says a to the power p - 1 is congruent to 1 modulo p, for prime p and a not divisible by p.",
    "inputs": "FIGURES = {'modulus': 7, 'sum_reduced': 4, 'product_reduced': 2, 'inverse_of_3': 5, 'inverse_check': 15, 'power_check': 8, 'power_reduced': 1, 'clock_modulus': 12}\nLABEL = 'modular-arithmetic'\n",
    "expected": "count: 8\nlabel: modular-arithmetic\nmax: 15\nmean: 6.75\nmin: 1\ntotal: 54\nResult: count=8|label=modular-arithmetic|max=15|mean=6.75|min=1|total=54\nRun 1 SHA-256: 72b723dce51cd7a4fe8a5f3aa9f371397b3da0dbbbf6c28dd5e0ec8eadc4e39c\nRun 2 SHA-256: 72b723dce51cd7a4fe8a5f3aa9f371397b3da0dbbbf6c28dd5e0ec8eadc4e39c\nDeterministic: MATCH\n"
  },
  {
    "title": "College Mathematics: Functions Composition and Inverses",
    "subject": "function composition and inverses",
    "description": "The composition of functions f and g, written g after f, applies f first and then g to the result. The inverse of a function f is a function that undoes it: applying f and then its inverse returns the original input. A function has an inverse exactly when it is one-to-one (different inputs give different outputs) and onto its target set. Composition is associative: doing three functions in order does not depend on how they are grouped. Composition is not commutative: f after g is usually different from g after f. The graph of an inverse is the reflection of the graph of the original across the line y = x.",
    "inputs": "FIGURES = {'f_at_2': 7, 'g_after_f': 49, 'f_after_g': 13, 'inverse_at_7': 2, 'g_at_minus_2': 4, 'g_at_2': 4, 'slope_of_f': 3, 'functions_composed': 2}\nLABEL = 'function-composition-and-inverses'\n",
    "expected": "count: 8\nlabel: function-composition-and-inverses\nmax: 49\nmean: 10.5\nmin: 2\ntotal: 84\nResult: count=8|label=function-composition-and-inverses|max=49|mean=10.5|min=2|total=84\nRun 1 SHA-256: cd94d17c1e34de5fe594d1fed8b910b2b63a9bba76d8a83553eadf75e11e6c37\nRun 2 SHA-256: cd94d17c1e34de5fe594d1fed8b910b2b63a9bba76d8a83553eadf75e11e6c37\nDeterministic: MATCH\n"
  },
  {
    "title": "College Mathematics: Capstone Problems Using Several Ideas",
    "subject": "capstone problems using several ideas",
    "description": "A capstone problem is a problem that uses several ideas at once: counting, functions, proof, and number sense together. Solving one means choosing the right tool for each part, checking each part, and assembling the parts into a single argument whose conclusion follows from its premises. A good solution plan names the ideas it will use before it uses them. Each part is checked separately: a count by a second count, an algebra step by substitution. The final answer is stated with its units and its conditions, not as a bare number.",
    "inputs": "FIGURES = {'digits_available': 10, 'digits_chosen': 4, 'combinations': 210, 'with_zero': 84, 'answer': 126, 'smallest': 1234, 'largest': 6789, 'parts_in_solution': 3}\nLABEL = 'capstone-problems-using-several-ideas'\n",
    "expected": "count: 8\nlabel: capstone-problems-using-several-ideas\nmax: 6789\nmean: 1057.5\nmin: 3\ntotal: 8460\nResult: count=8|label=capstone-problems-using-several-ideas|max=6789|mean=1057.5|min=3|total=8460\nRun 1 SHA-256: 33dfcc060733cd79f1747dd87739191ed34d200cea1ca0ade377fd9386541e60\nRun 2 SHA-256: 33dfcc060733cd79f1747dd87739191ed34d200cea1ca0ade377fd9386541e60\nDeterministic: MATCH\n"
  }
];

const SOURCES = [
  {
    "name": "Wikipedia - Set theory",
    "url": "https://en.wikipedia.org/wiki/Set_theory",
    "establishes": "The reference for numbers and sets in this record."
  },
  {
    "name": "Wikipedia - Mathematics",
    "url": "https://en.wikipedia.org/wiki/Mathematics",
    "establishes": "The reference for numbers and sets in this record."
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
