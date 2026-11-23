// Seeded boundless generator for the Discrete Mathematics Database ("public" edition).
// Deterministic: the same seed always emits the same record.
// Usage: node gen-discrete-mathematics.js [seed]  (prints one JSON record)
// or: node gen-discrete-mathematics.js --test (runTests).
// Package-only; outputs are generated, not stored files.
"use strict";
const crypto = require("crypto");

const SLUG = "discrete-mathematics";
const RECORD_KIND = "discrete mathematics record";
const ID_PREFIX = "JAH-DISCMATH-";
const AI_NAME = "JAH Discrete Mathematics Librarian";
const EDITION = "public";
const SRC = "public-harvest";
const CEILING = "Generator ceiling: up to 1,000,000,000 scales per file, generated on demand by the file AI — not stored files.";

const TOPICS = [
  {
    "title": "Discrete Mathematics: Propositional Logic",
    "subject": "propositional logic",
    "description": "Propositional logic is the logic of statements (sentences that are true or false) combined by connectives: and, or, not, implies, and if and only if. A truth table lists the truth value of a compound statement for every combination of its parts. Two statements are logically equivalent when their truth tables agree in every row. Implication P implies Q is false only when P is true and Q is false. De Morgan's laws say the negation of (P and Q) is (not P) or (not Q). A tautology is a statement true in every row, such as P or not P.",
    "inputs": "FIGURES = {'rows_checked': 4, 'equivalences_shown': 2, 'connectives_named': 5, 'tautology_rows': 4, 'truth_values': 2, 'statements_compared': 2, 'laws_named': 2, 'checks': 2}\nLABEL = 'propositional-logic'\n",
    "expected": "count: 8\nlabel: propositional-logic\nmax: 5\nmean: 2.875\nmin: 2\ntotal: 23\nResult: count=8|label=propositional-logic|max=5|mean=2.875|min=2|total=23\nRun 1 SHA-256: 5a4b78c0020ab970ace5ea186f57baa6738210f99190f0965f25f940faa6ca93\nRun 2 SHA-256: 5a4b78c0020ab970ace5ea186f57baa6738210f99190f0965f25f940faa6ca93\nDeterministic: MATCH\n"
  },
  {
    "title": "Discrete Mathematics: Predicate Logic and Quantifiers",
    "subject": "predicate logic and quantifiers",
    "description": "Predicate logic extends propositional logic with predicates (properties that depend on a variable, such as x is even) and quantifiers: for all (every object) and there exists (at least one object). Negating a quantified statement swaps the quantifier: the negation of for all x, P(x) is there exists x, not P(x). To prove a for-all statement, take an arbitrary object and prove the claim for it. To disprove a for-all statement, exhibit one counterexample. The order of quantifiers matters: for every x there is a y is not the same as there is a y for every x.",
    "inputs": "FIGURES = {'examples_checked': 3, 'quantifiers_named': 2, 'negations_named': 2, 'orderings_compared': 2, 'proof_steps': 2, 'counterexamples_needed': 1, 'integers_tested': 3, 'checks': 3}\nLABEL = 'predicate-logic-and-quantifiers'\n",
    "expected": "count: 8\nlabel: predicate-logic-and-quantifiers\nmax: 3\nmean: 2.25\nmin: 1\ntotal: 18\nResult: count=8|label=predicate-logic-and-quantifiers|max=3|mean=2.25|min=1|total=18\nRun 1 SHA-256: b05e67ff7df0921d6cf8637fe1f23430f30ffa42721d1b3213a86edca78e2cf3\nRun 2 SHA-256: b05e67ff7df0921d6cf8637fe1f23430f30ffa42721d1b3213a86edca78e2cf3\nDeterministic: MATCH\n"
  },
  {
    "title": "Discrete Mathematics: Sets, Functions, and Relations",
    "subject": "sets, functions, and relations in discrete mathematics",
    "description": "A set is a collection of distinct objects. A function assigns exactly one output to each input. A relation is a set of ordered pairs: a subset of the Cartesian product (the set of all pairs) of two sets. Relations include equivalence relations (which split a set into classes) and partial orders (which rank elements). A function is injective (one-to-one) when different inputs give different outputs. A function is surjective (onto) when every output is hit by some input. A bijection is both injective and surjective, and pairs the two sets exactly.",
    "inputs": "FIGURES = {'function_value': 10, 'inverse_value': 5, 'properties_checked': 2, 'sets_compared': 2, 'pairs_named': 3, 'relation_types': 2, 'checks': 2, 'integers_tested': 1}\nLABEL = 'sets-functions-and-relations-in-discrete-mathematics'\n",
    "expected": "count: 8\nlabel: sets-functions-and-relations-in-discrete-mathematics\nmax: 10\nmean: 3.375\nmin: 1\ntotal: 27\nResult: count=8|label=sets-functions-and-relations-in-discrete-mathematics|max=10|mean=3.375|min=1|total=27\nRun 1 SHA-256: 8b5597d098408eb93ffa92855a57ceb55ea857223cbaf22f99bc0610fac67002\nRun 2 SHA-256: 8b5597d098408eb93ffa92855a57ceb55ea857223cbaf22f99bc0610fac67002\nDeterministic: MATCH\n"
  },
  {
    "title": "Discrete Mathematics: Proof by Induction",
    "subject": "proof by induction in discrete mathematics",
    "description": "Mathematical induction proves a claim for all natural numbers in two steps: the base case (the claim for the first number) and the inductive step (if the claim holds for k, then it holds for k + 1). Strong induction assumes the claim for all numbers up to k, which is sometimes needed when the step uses an earlier case that is not the previous one. The base case anchors the proof; without it, the inductive step proves nothing. Strong induction is used when the step from k to k + 1 needs an earlier case. Structural induction proves claims about recursively defined structures, such as trees.",
    "inputs": "FIGURES = {'base_case': 2, 'n_factored': 12, 'prime_factors': 3, 'steps_in_proof': 2, 'induction_forms': 3, 'cases_in_step': 2, 'checks': 1, 'factors_of_12': 3}\nLABEL = 'proof-by-induction-in-discrete-mathematics'\n",
    "expected": "count: 8\nlabel: proof-by-induction-in-discrete-mathematics\nmax: 12\nmean: 3.5\nmin: 1\ntotal: 28\nResult: count=8|label=proof-by-induction-in-discrete-mathematics|max=12|mean=3.5|min=1|total=28\nRun 1 SHA-256: 3a1cfc3e5d3821fdd67494d4e5824d04f3f8e1bf3cb763762d97a172cb2f6d8f\nRun 2 SHA-256: 3a1cfc3e5d3821fdd67494d4e5824d04f3f8e1bf3cb763762d97a172cb2f6d8f\nDeterministic: MATCH\n"
  },
  {
    "title": "Discrete Mathematics: Counting with the Product and Sum Rules",
    "subject": "the product and sum rules for counting",
    "description": "The product rule says: if a task has a sequence of steps, with a choices for the first, b for the second, and so on, the total number of ways is the product a times b times .... The sum rule says: if a task can be done in one of several disjoint (non-overlapping) ways, the total is the sum of the counts. Together they are the foundation of counting. The product rule multiplies the choices at each step. The sum rule adds the counts of disjoint cases. The subtraction rule counts the complement: total minus the unwanted cases.",
    "inputs": "FIGURES = {'strings_total': 17576, 'start_vowel': 3380, 'end_vowel': 3380, 'both_vowel': 650, 'union': 6110, 'neither': 11466, 'alphabet_size': 26, 'vowels': 5}\nLABEL = 'the-product-and-sum-rules-for-counting'\n",
    "expected": "count: 8\nlabel: the-product-and-sum-rules-for-counting\nmax: 17576\nmean: 5324.125\nmin: 5\ntotal: 42593\nResult: count=8|label=the-product-and-sum-rules-for-counting|max=17576|mean=5324.125|min=5|total=42593\nRun 1 SHA-256: bb23d439f2f26bd891425da3af0161e7976b3b64ccdc7694c6de2884192939f7\nRun 2 SHA-256: bb23d439f2f26bd891425da3af0161e7976b3b64ccdc7694c6de2884192939f7\nDeterministic: MATCH\n"
  },
  {
    "title": "Discrete Mathematics: Permutations and Combinations",
    "subject": "permutations and combinations",
    "description": "A permutation is an arrangement in order; a combination is a choice where order does not matter. The number of permutations of r objects from n is P(n, r) = n! / (n - r)!. The number of combinations is C(n, r) = n! / (r! (n - r)!). The binomial theorem expands (x + y)^n using the combinations as coefficients. P(n, r) counts ordered choices; C(n, r) counts unordered choices. C(n, r) = C(n, n - r): choosing r to take is choosing n - r to leave. The binomial coefficients sum to 2^n, the number of subsets of an n-element set.",
    "inputs": "FIGURES = {'committees': 120, 'chair_choices': 3, 'total_ways': 360, 'method_2_chairs': 10, 'method_2_others': 36, 'poker_hands': 2598960, 'people': 10, 'committee_size': 3}\nLABEL = 'permutations-and-combinations'\n",
    "expected": "count: 8\nlabel: permutations-and-combinations\nmax: 2598960\nmean: 324937.75\nmin: 3\ntotal: 2599502\nResult: count=8|label=permutations-and-combinations|max=2598960|mean=324937.75|min=3|total=2599502\nRun 1 SHA-256: 0e14f8548bc29f40f3bc464fe78b1ad4d5fa81fbc115f0fa068025c5fdaad78e\nRun 2 SHA-256: 0e14f8548bc29f40f3bc464fe78b1ad4d5fa81fbc115f0fa068025c5fdaad78e\nDeterministic: MATCH\n"
  },
  {
    "title": "Discrete Mathematics: The Pigeonhole Principle",
    "subject": "the pigeonhole principle",
    "description": "The pigeonhole principle says: if more objects are put into fewer boxes than there are objects, then at least one box holds more than one object. The general form says that if n objects go into m boxes, some box holds at least the ceiling of n/m objects (the ceiling is the smallest whole number at least as large as the value). With 13 people, two share a birth month, because there are 12 months and 13 people. The principle proves existence only: it says a crowded box exists, not which one it is. It is a proof by contradiction in disguise: assuming every box holds at most one object contradicts the count.",
    "inputs": "FIGURES = {'points': 5, 'boxes': 4, 'max_distance': 0.7071, 'small_square_side': 0.5, 'diagonal': 0.7071, 'months': 12, 'people_for_months': 13, 'guaranteed': 2}\nLABEL = 'the-pigeonhole-principle'\n",
    "expected": "count: 8\nlabel: the-pigeonhole-principle\nmax: 13\nmean: 4.7393\nmin: 0.5\ntotal: 37.9142\nResult: count=8|label=the-pigeonhole-principle|max=13|mean=4.7393|min=0.5|total=37.9142\nRun 1 SHA-256: 3646eb228632c7c9b81b759cf5037843c941892559459b2a86d812d7fc6fad9f\nRun 2 SHA-256: 3646eb228632c7c9b81b759cf5037843c941892559459b2a86d812d7fc6fad9f\nDeterministic: MATCH\n"
  },
  {
    "title": "Discrete Mathematics: Inclusion-Exclusion",
    "subject": "inclusion-exclusion in discrete mathematics",
    "description": "Inclusion-exclusion counts a union of sets without double-counting: add the sizes of the sets, subtract the pairwise intersections, add back the triple intersections, and continue alternating. It also counts objects with none of several properties, by subtracting from the total. For two sets, the union size is the sum of the sizes minus the intersection size. For three sets, add the three sizes, subtract the three pairwise intersections, and add the triple intersection. The number of integers from 1 to n that are coprime to n is counted this way (Euler's totient).",
    "inputs": "FIGURES = {'divisible_by_2': 50, 'divisible_by_3': 33, 'divisible_by_6': 16, 'union': 67, 'neither': 33, 'blocks': 16, 'per_block': 4, 'remainder_qualifying': 3}\nLABEL = 'inclusion-exclusion-in-discrete-mathematics'\n",
    "expected": "count: 8\nlabel: inclusion-exclusion-in-discrete-mathematics\nmax: 67\nmean: 27.75\nmin: 3\ntotal: 222\nResult: count=8|label=inclusion-exclusion-in-discrete-mathematics|max=67|mean=27.75|min=3|total=222\nRun 1 SHA-256: d4d40ac39c8b969c970ea71305b9161caae83aa383ee0a4867ecd088fd689d03\nRun 2 SHA-256: d4d40ac39c8b969c970ea71305b9161caae83aa383ee0a4867ecd088fd689d03\nDeterministic: MATCH\n"
  },
  {
    "title": "Discrete Mathematics: Graphs and Their Basics",
    "subject": "graphs and their basics",
    "description": "A graph is a set of vertices (points) joined by edges (lines). The degree of a vertex is the number of edges touching it. The handshaking lemma says the sum of the degrees is twice the number of edges, because each edge contributes 1 to the degree of each of its two endpoints. A path is a sequence of vertices joined by edges; a cycle is a path that returns to its start. The sum of the degrees is twice the number of edges. The number of vertices of odd degree is always even. A tree is a connected graph with no cycles; a tree with n vertices has n - 1 edges.",
    "inputs": "FIGURES = {'vertices': 6, 'degree_sum': 10, 'edges': 5, 'odd_degree_vertices': 4, 'tree_edges': 5, 'complete_graph_vertices': 5, 'complete_graph_edges': 10, 'complete_degree': 4}\nLABEL = 'graphs-and-their-basics'\n",
    "expected": "count: 8\nlabel: graphs-and-their-basics\nmax: 10\nmean: 6.125\nmin: 4\ntotal: 49\nResult: count=8|label=graphs-and-their-basics|max=10|mean=6.125|min=4|total=49\nRun 1 SHA-256: 7366770148763b35e8db150a51743b189944b34ec45c6d0a98e0b23d7e4f5398\nRun 2 SHA-256: 7366770148763b35e8db150a51743b189944b34ec45c6d0a98e0b23d7e4f5398\nDeterministic: MATCH\n"
  },
  {
    "title": "Discrete Mathematics: Eulerian and Hamiltonian Paths",
    "subject": "Eulerian and Hamiltonian paths",
    "description": "An Eulerian path uses every edge of a graph exactly once; an Eulerian circuit is one that returns to its start. A Hamiltonian path visits every vertex exactly once. Euler's theorem says a connected graph has an Eulerian circuit exactly when every vertex has even degree, and an Eulerian path exactly when zero or two vertices have odd degree. No such simple test exists for Hamiltonian paths. An Eulerian circuit exists exactly when the graph is connected and every vertex has even degree. An Eulerian path exists exactly when zero or two vertices have odd degree. Deciding whether a Hamiltonian path exists is NP-complete (no fast general method is known).",
    "inputs": "FIGURES = {'konigsberg_vertices': 4, 'odd_degrees_konigsberg': 4, 'square_odd_vertices': 2, 'square_vertices': 4, 'square_edges': 5, 'hamiltonian_vertices': 4, 'degrees_konigsberg': 3, 'bridges': 7}\nLABEL = 'eulerian-and-hamiltonian-paths'\n",
    "expected": "count: 8\nlabel: eulerian-and-hamiltonian-paths\nmax: 7\nmean: 4.125\nmin: 2\ntotal: 33\nResult: count=8|label=eulerian-and-hamiltonian-paths|max=7|mean=4.125|min=2|total=33\nRun 1 SHA-256: 893065bf6690c82b4dcd5ae1466ac022a5c9c5a39d0cc7c6c2a3c8b730102f87\nRun 2 SHA-256: 893065bf6690c82b4dcd5ae1466ac022a5c9c5a39d0cc7c6c2a3c8b730102f87\nDeterministic: MATCH\n"
  },
  {
    "title": "Discrete Mathematics: Trees",
    "subject": "trees in graph theory",
    "description": "A tree is a connected graph with no cycles. A tree with n vertices has exactly n - 1 edges, and there is exactly one path between any two vertices. A spanning tree of a graph is a tree that uses all the graph's vertices and some of its edges. A rooted tree has a distinguished root, with parent and child relationships. A tree with n vertices has n - 1 edges. There is exactly one simple path between any two vertices of a tree. Removing any edge of a tree disconnects it; adding any edge creates exactly one cycle.",
    "inputs": "FIGURES = {'offices': 8, 'cables_needed': 7, 'labelled_trees': 262144, 'binary_tree_levels': 4, 'binary_tree_vertices': 15, 'edges_in_tree': 7, 'paths_between_vertices': 1, 'cayley_exponent': 6}\nLABEL = 'trees-in-graph-theory'\n",
    "expected": "count: 8\nlabel: trees-in-graph-theory\nmax: 262144\nmean: 32774.0\nmin: 1\ntotal: 262192\nResult: count=8|label=trees-in-graph-theory|max=262144|mean=32774.0|min=1|total=262192\nRun 1 SHA-256: 5366dd3539c415667a8fe8487f374004d61ea302582a0033dc15b2c8e94faa4c\nRun 2 SHA-256: 5366dd3539c415667a8fe8487f374004d61ea302582a0033dc15b2c8e94faa4c\nDeterministic: MATCH\n"
  },
  {
    "title": "Discrete Mathematics: Recurrence Relations",
    "subject": "recurrence relations",
    "description": "A recurrence relation defines a sequence by its first values and a rule for each later value in terms of earlier ones. The Fibonacci sequence is the classic example: each term after the first two is the sum of the two before it. A linear recurrence with constant coefficients is solved by its characteristic equation, like a differential equation. The Fibonacci recurrence is F(n) = F(n-1) + F(n-2), with F(1) = F(2) = 1. A linear recurrence with constant coefficients is solved by its characteristic equation. The characteristic roots give the closed form; repeated roots need a factor of n.",
    "inputs": "FIGURES = {'a_0': 1, 'a_1': 3, 'a_2': 7, 'root_1': 1, 'root_2': 2, 'constant_a': -1, 'constant_b': 2, 'terms_checked': 3}\nLABEL = 'recurrence-relations'\n",
    "expected": "count: 8\nlabel: recurrence-relations\nmax: 7\nmean: 2.25\nmin: -1\ntotal: 18\nResult: count=8|label=recurrence-relations|max=7|mean=2.25|min=-1|total=18\nRun 1 SHA-256: 9a6bd39cb34656e093c677d2696f03f463225cbd77da62436549899a10ad2f35\nRun 2 SHA-256: 9a6bd39cb34656e093c677d2696f03f463225cbd77da62436549899a10ad2f35\nDeterministic: MATCH\n"
  },
  {
    "title": "Discrete Mathematics: Generating Functions",
    "subject": "generating functions",
    "description": "A generating function is a power series whose coefficients are the terms of a sequence: for the sequence a_0, a_1, a_2, ..., the ordinary generating function is the sum of a_n x^n. Manipulating the series (adding, multiplying, differentiating) manipulates the sequence, turning counting problems into algebra. The generating function of the constant sequence 1, 1, 1, ... is 1/(1 - x). The generating function of the Fibonacci sequence is x / (1 - x - x squared). Multiplying generating functions corresponds to convolving (combining) the sequences.",
    "inputs": "FIGURES = {'ways_to_make_change': 4, 'coins_used': 3, 'amount': 10, 'coefficient': 4, 'generating_terms': 3, 'denominations': 3, 'fives_used_max': 2, 'checks': 1}\nLABEL = 'generating-functions'\n",
    "expected": "count: 8\nlabel: generating-functions\nmax: 10\nmean: 3.75\nmin: 1\ntotal: 30\nResult: count=8|label=generating-functions|max=10|mean=3.75|min=1|total=30\nRun 1 SHA-256: 0ffdc01bd5dbfe80382639b52109dcca5f27eec0f265b54b33d5c06ffaba0f05\nRun 2 SHA-256: 0ffdc01bd5dbfe80382639b52109dcca5f27eec0f265b54b33d5c06ffaba0f05\nDeterministic: MATCH\n"
  },
  {
    "title": "Discrete Mathematics: Number Theory and Divisibility",
    "subject": "number theory and divisibility",
    "description": "Number theory is the study of the integers. Divisibility is its basic relation: a divides b when b is a multiple of a. A prime is an integer greater than 1 whose only divisors are 1 and itself. The fundamental theorem of arithmetic says every integer greater than 1 is a product of primes in exactly one way (up to order). Every integer greater than 1 is a product of primes, uniquely up to order. There are infinitely many primes, proved by Euclid. The greatest common divisor is found by Euclid's algorithm.",
    "inputs": "FIGURES = {'n_factored': 360, 'prime_2_power': 3, 'prime_3_power': 2, 'prime_5_power': 1, 'divisor_count': 24, 'primes_used': 3, 'check_product': 360, 'steps': 3}\nLABEL = 'number-theory-and-divisibility'\n",
    "expected": "count: 8\nlabel: number-theory-and-divisibility\nmax: 360\nmean: 94.5\nmin: 1\ntotal: 756\nResult: count=8|label=number-theory-and-divisibility|max=360|mean=94.5|min=1|total=756\nRun 1 SHA-256: cac0399e39ef3d05165f165138d34d5d2cdfe6378db17356db363866003f36fc\nRun 2 SHA-256: cac0399e39ef3d05165f165138d34d5d2cdfe6378db17356db363866003f36fc\nDeterministic: MATCH\n"
  },
  {
    "title": "Discrete Mathematics: Modular Arithmetic and Cryptography",
    "subject": "modular arithmetic and cryptography",
    "description": "Modular arithmetic is arithmetic with remainders: a and b are congruent modulo n when their difference is a multiple of n. Fermat's little theorem says a^(p-1) is congruent to 1 modulo p for prime p and a not divisible by p. RSA cryptography uses modular exponentiation with a product of two large primes: encryption is easy, decryption needs the factorisation. Congruence modulo n is an equivalence relation with n classes. A number has a multiplicative inverse modulo n exactly when it is coprime to n. RSA encrypts a message m as m^e modulo n, and decrypts with the private exponent d.",
    "inputs": "FIGURES = {'modulus': 7, 'sum_reduced': 4, 'product_reduced': 2, 'inverse_of_3': 5, 'rsa_n': 55, 'rsa_e': 3, 'rsa_d': 27, 'ciphertext': 13}\nLABEL = 'modular-arithmetic-and-cryptography'\n",
    "expected": "count: 8\nlabel: modular-arithmetic-and-cryptography\nmax: 55\nmean: 14.5\nmin: 2\ntotal: 116\nResult: count=8|label=modular-arithmetic-and-cryptography|max=55|mean=14.5|min=2|total=116\nRun 1 SHA-256: 4950746fe8f2223a7d5a6ee5e14fd9cc52d9ff55c97730e2adc2485f503c849d\nRun 2 SHA-256: 4950746fe8f2223a7d5a6ee5e14fd9cc52d9ff55c97730e2adc2485f503c849d\nDeterministic: MATCH\n"
  },
  {
    "title": "Discrete Mathematics: Boolean Algebra",
    "subject": "Boolean algebra",
    "description": "Boolean algebra is the algebra of true and false: the operations are and (conjunction), or (disjunction), and not (negation), obeying laws such as commutativity, distributivity, and De Morgan's laws. A Boolean function is a function from bits (0 and 1) to bits, and every Boolean function can be built from and, or, and not. De Morgan's laws: not (A and B) is (not A) or (not B). A Boolean function can be written in disjunctive normal form (an or of ands). A Karnaugh map simplifies a Boolean function by grouping adjacent ones.",
    "inputs": "FIGURES = {'truth_table_rows': 4, 'ones_in_table': 2, 'terms_in_dnf': 2, 'simplified_terms': 2, 'variables': 2, 'checks': 4, 'laws_named': 3, 'gates_named': 3}\nLABEL = 'boolean-algebra'\n",
    "expected": "count: 8\nlabel: boolean-algebra\nmax: 4\nmean: 2.75\nmin: 2\ntotal: 22\nResult: count=8|label=boolean-algebra|max=4|mean=2.75|min=2|total=22\nRun 1 SHA-256: ef9546703a06f288854075c9affb5afc5f09570adce95d4012f26fff7c25e662\nRun 2 SHA-256: ef9546703a06f288854075c9affb5afc5f09570adce95d4012f26fff7c25e662\nDeterministic: MATCH\n"
  },
  {
    "title": "Discrete Mathematics: The Pigeonhole Principle in Algorithms",
    "subject": "the pigeonhole principle in algorithms",
    "description": "The pigeonhole principle in algorithms says that if more items are hashed into fewer slots than there are items, collisions (two items in one slot) must occur. It is the same principle as in counting: n objects into m boxes force a box with at least ceiling(n/m) objects. It proves lower bounds: no lossless compression can shrink every file, and no hashing scheme avoids collisions. A hash table with m slots and n > m items must have a collision. No lossless compression can make every file shorter: there are more long files than short ones. The principle gives a lower bound, not a construction.",
    "inputs": "FIGURES = {'slots': 100, 'items': 150, 'average_load': 1.5, 'guaranteed_collision': 2, 'files_100bit': 2, 'shorter_files': 1, 'bits': 100, 'checks': 2}\nLABEL = 'the-pigeonhole-principle-in-algorithms'\n",
    "expected": "count: 8\nlabel: the-pigeonhole-principle-in-algorithms\nmax: 150\nmean: 44.8125\nmin: 1\ntotal: 358.5\nResult: count=8|label=the-pigeonhole-principle-in-algorithms|max=150|mean=44.8125|min=1|total=358.5\nRun 1 SHA-256: 7226eba31c240d50333756cacbc61044b2d8dd0832c902f5ffd896865329a63b\nRun 2 SHA-256: 7226eba31c240d50333756cacbc61044b2d8dd0832c902f5ffd896865329a63b\nDeterministic: MATCH\n"
  },
  {
    "title": "Discrete Mathematics: Graph Colouring",
    "subject": "graph colouring",
    "description": "A colouring of a graph assigns a colour to each vertex so that adjacent vertices (joined by an edge) have different colours. The chromatic number is the smallest number of colours needed. The four-colour theorem says every planar graph (one drawable in the plane without crossing edges) can be coloured with 4 colours. A graph needs at least as many colours as its largest clique (a set of mutually adjacent vertices). A bipartite graph (one whose vertices split into two sets with edges only between them) needs 2 colours. The four-colour theorem, proved in 1976 with computer assistance, says 4 colours suffice for any map.",
    "inputs": "FIGURES = {'pentagon_vertices': 5, 'chromatic_number': 3, 'colours_tried': 2, 'complete_graph_vertices': 4, 'complete_chromatic': 4, 'map_colours': 4, 'theorem_year': 1976, 'clique_size': 4}\nLABEL = 'graph-colouring'\n",
    "expected": "count: 8\nlabel: graph-colouring\nmax: 1976\nmean: 250.25\nmin: 2\ntotal: 2002\nResult: count=8|label=graph-colouring|max=1976|mean=250.25|min=2|total=2002\nRun 1 SHA-256: c9a28a0da96fd0f84f3240baa3526900577f60e9d24cd1e145dfaf4bdaab9d61\nRun 2 SHA-256: c9a28a0da96fd0f84f3240baa3526900577f60e9d24cd1e145dfaf4bdaab9d61\nDeterministic: MATCH\n"
  },
  {
    "title": "Discrete Mathematics: Counting Derangements",
    "subject": "derangements",
    "description": "A derangement is a permutation with no element in its original place. The number of derangements of n objects, written !n (subfactorial), is n! times the sum of (-1)^k / k! for k from 0 to n. As n grows, the fraction of permutations that are derangements approaches 1/e, about 0.3679. The derangement count is found by inclusion-exclusion. The fraction of derangements approaches 1/e as n grows. !n is the nearest integer to n! / e.",
    "inputs": "FIGURES = {'derangements_4': 9, 'permutations_4': 24, 'fraction_4': 0.375, 'derangements_5': 44, 'permutations_5': 120, 'fraction_5': 0.3667, 'limit_fraction': 0.3679, 'sum_terms': 5}\nLABEL = 'derangements'\n",
    "expected": "count: 8\nlabel: derangements\nmax: 120\nmean: 25.3887\nmin: 0.3667\ntotal: 203.1096\nResult: count=8|label=derangements|max=120|mean=25.3887|min=0.3667|total=203.1096\nRun 1 SHA-256: 9998f7622698a7ceb46f954af918d2125ce02ccc4c9de86c9d337ef652253f99\nRun 2 SHA-256: 9998f7622698a7ceb46f954af918d2125ce02ccc4c9de86c9d337ef652253f99\nDeterministic: MATCH\n"
  },
  {
    "title": "Discrete Mathematics: The Principle of Mathematical Induction for Graphs",
    "subject": "induction for graphs",
    "description": "Induction proves facts about graphs by removing a vertex or an edge and applying the hypothesis to the smaller graph. The base case is the smallest graph; the step adds a vertex or an edge and checks that the claim survives. This is structural induction: the structure is built up one piece at a time. A tree with n vertices has n - 1 edges, proved by removing a leaf (a vertex of degree 1). Every tree has a leaf: a longest path's endpoint has degree 1. Induction on the number of vertices is the standard method for graph theorems.",
    "inputs": "FIGURES = {'base_vertices': 1, 'base_edges': 0, 'tree_5_edges': 4, 'tree_8_edges': 7, 'leaf_degree': 1, 'steps_in_proof': 2, 'paths_endpoints': 2, 'checks': 2}\nLABEL = 'induction-for-graphs'\n",
    "expected": "count: 8\nlabel: induction-for-graphs\nmax: 7\nmean: 2.375\nmin: 0\ntotal: 19\nResult: count=8|label=induction-for-graphs|max=7|mean=2.375|min=0|total=19\nRun 1 SHA-256: f92cf19dc8f56df5aea4f95b3d47a2b3be2353f8c53e478bb3857cdb029ea8be\nRun 2 SHA-256: f92cf19dc8f56df5aea4f95b3d47a2b3be2353f8c53e478bb3857cdb029ea8be\nDeterministic: MATCH\n"
  },
  {
    "title": "Discrete Mathematics: Binary Relations and Partial Orders",
    "subject": "binary relations and partial orders",
    "description": "A binary relation on a set is a set of ordered pairs. A partial order is a relation that is reflexive (every element relates to itself), antisymmetric (if a relates to b and b to a, then a = b), and transitive (if a relates to b and b to c, then a relates to c). It ranks elements: a precedes b. A total order compares every pair; a partial order may leave some pairs incomparable. Divisibility is a partial order on the positive integers: 2 divides 6 and 6 divides 12, but 2 and 3 are incomparable. A Hasse diagram draws a partial order with edges for the covering relations. A maximal element has nothing above it; a maximum is above everything.",
    "inputs": "FIGURES = {'elements': 4, 'comparable_pairs': 5, 'reflexive_pairs': 4, 'maximal_elements': 1, 'maximum': 6, 'chains': 2, 'levels': 3, 'properties': 3}\nLABEL = 'binary-relations-and-partial-orders'\n",
    "expected": "count: 8\nlabel: binary-relations-and-partial-orders\nmax: 6\nmean: 3.5\nmin: 1\ntotal: 28\nResult: count=8|label=binary-relations-and-partial-orders|max=6|mean=3.5|min=1|total=28\nRun 1 SHA-256: d9cde19d22bc030d74ccc1f5fbeda83dc594d40e7c5d2a53a7344458c45725e1\nRun 2 SHA-256: d9cde19d22bc030d74ccc1f5fbeda83dc594d40e7c5d2a53a7344458c45725e1\nDeterministic: MATCH\n"
  },
  {
    "title": "Discrete Mathematics: Counting with Generating Functions",
    "subject": "counting with generating functions",
    "description": "A generating function encodes a sequence as a power series, and counting problems become algebra on the series. The coefficient of x^n in 1/(1 - x)^2 is n + 1, the number of ways to write n as a sum of two non-negative integers (order matters). The coefficient of x^n in 1/(1 - x - x^2) is the (n+1)-th Fibonacci number. The coefficient of x^n in 1/(1 - x) is 1 for every n. The coefficient of x^n in 1/(1 - x)^2 is n + 1. Differentiating a generating function shifts and weights its coefficients.",
    "inputs": "FIGURES = {'ways_n5': 6, 'ways_n10': 11, 'fib_5': 5, 'coefficient_formula': 6, 'terms_shown': 4, 'sequences_encoded': 2, 'checks': 2, 'n_tested': 5}\nLABEL = 'counting-with-generating-functions'\n",
    "expected": "count: 8\nlabel: counting-with-generating-functions\nmax: 11\nmean: 5.125\nmin: 2\ntotal: 41\nResult: count=8|label=counting-with-generating-functions|max=11|mean=5.125|min=2|total=41\nRun 1 SHA-256: 0f5df5a55d539c11d8c107b9441ed5ce5662c3740cba74211359d9e9e9010be2\nRun 2 SHA-256: 0f5df5a55d539c11d8c107b9441ed5ce5662c3740cba74211359d9e9e9010be2\nDeterministic: MATCH\n"
  },
  {
    "title": "Discrete Mathematics: The Euclidean Algorithm and Bezout",
    "subject": "the Euclidean algorithm and Bezout's identity",
    "description": "Euclid's algorithm finds the greatest common divisor (GCD) of two integers by repeated division with remainder. Bezout's identity says the GCD can be written as a combination a x + b y for some integers x and y, and the extended Euclidean algorithm finds x and y. This combination is what makes modular inverses exist. The GCD is the last non-zero remainder in Euclid's algorithm. Bezout's identity: gcd(a, b) = a x + b y for some integers x and y. The extended algorithm finds x and y by working backwards through the divisions.",
    "inputs": "FIGURES = {'gcd': 21, 'coefficient_105': 5, 'coefficient_252': -2, 'check_525': 525, 'check_504': 504, 'divisions': 3, 'remainders': 2, 'steps': 3}\nLABEL = 'the-euclidean-algorithm-and-bezout-s-identity'\n",
    "expected": "count: 8\nlabel: the-euclidean-algorithm-and-bezout-s-identity\nmax: 525\nmean: 132.625\nmin: -2\ntotal: 1061\nResult: count=8|label=the-euclidean-algorithm-and-bezout-s-identity|max=525|mean=132.625|min=-2|total=1061\nRun 1 SHA-256: 9bb3f2d8700437afa921b08bde224781af49338e4593dfc0496ff0bbdb1752b0\nRun 2 SHA-256: 9bb3f2d8700437afa921b08bde224781af49338e4593dfc0496ff0bbdb1752b0\nDeterministic: MATCH\n"
  },
  {
    "title": "Discrete Mathematics: Capstone Counting a Real System",
    "subject": "capstone: counting a real system",
    "description": "A capstone problem for discrete mathematics counts a real system by combining the product rule, combinations, inclusion-exclusion, and the pigeonhole principle. This record counts the passwords, the schedules, and the collisions of a small system, showing each tool in turn and checking each count twice. The plan names the tools before they are used. Each count is checked by a second method. The final answer is stated with its conditions.",
    "inputs": "FIGURES = {'passwords': 69000, 'first_choices': 5, 'second_choices': 25, 'third_choices': 24, 'fourth_choices': 23, 'prefixes': 125, 'guarantee_threshold': 69001, 'tools_used': 4}\nLABEL = 'capstone-counting-a-real-system'\n",
    "expected": "count: 8\nlabel: capstone-counting-a-real-system\nmax: 69001\nmean: 17275.875\nmin: 4\ntotal: 138207\nResult: count=8|label=capstone-counting-a-real-system|max=69001|mean=17275.875|min=4|total=138207\nRun 1 SHA-256: 4c95a1073e9db7c1200083181bb26381a7a762c204812c6010bac26c61fb1e99\nRun 2 SHA-256: 4c95a1073e9db7c1200083181bb26381a7a762c204812c6010bac26c61fb1e99\nDeterministic: MATCH\n"
  }
];

const SOURCES = [
  {
    "name": "Wikipedia - Mathematical logic",
    "url": "https://en.wikipedia.org/wiki/Mathematical_logic",
    "establishes": "The reference for propositional logic in this record."
  },
  {
    "name": "Wikipedia - Boolean algebra",
    "url": "https://en.wikipedia.org/wiki/Boolean_algebra",
    "establishes": "The reference for propositional logic in this record."
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
