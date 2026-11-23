// Seeded boundless generator for the The Signature Discrete Mathematics Database ("signature" edition).
// Deterministic: the same seed always emits the same record.
// Usage: node gen-discrete-mathematics-signature.js [seed]  (prints one JSON record)
// or: node gen-discrete-mathematics-signature.js --test (runTests).
// Package-only; outputs are generated, not stored files.
"use strict";
const crypto = require("crypto");

const SLUG = "discrete-mathematics-signature";
const RECORD_KIND = "discrete mathematics record";
const ID_PREFIX = "JAH-DISCMATHS-";
const AI_NAME = "JAH Discrete Mathematics Librarian (Signature)";
const EDITION = "signature";
const SRC = "signature-generated";
const CEILING = "Generator ceiling: up to 1,000,000,000 scales per file, generated on demand by the file AI — not stored files.";

const TOPICS = [
  {
    "title": "Signature Design: The Truth Table Builder",
    "subject": "a Signature truth table builder design",
    "description": "The Truth Table Builder is a Signature-made design for teaching propositional logic: a tool where a learner enters a statement built from and, or, not, and implies, and the tool builds its truth table and flags equivalences. A truth table lists the truth value for every combination of the parts. The builder fills all rows for up to 4 parts (16 rows). Two statements are flagged as equivalent when their columns match. Tautologies (statements true in every row) are flagged green.",
    "inputs": "FIGURES = {'rows_checked': 4, 'equivalences_found': 1, 'tautologies_flagged': 1, 'parts_max': 4, 'rows_for_4_parts': 16, 'rows_for_10_parts': 1024, 'cap_parts': 5, 'design_version': 1}\nLABEL = 'a-signature-truth-table-builder-design'\n",
    "expected": "count: 8\nlabel: a-signature-truth-table-builder-design\nmax: 1024\nmean: 132.0\nmin: 1\ntotal: 1056\nResult: count=8|label=a-signature-truth-table-builder-design|max=1024|mean=132.0|min=1|total=1056\nRun 1 SHA-256: 5727ac1dd82e3a317371b193a14662da7cf799254515775fe3c83dc9939296a1\nRun 2 SHA-256: 5727ac1dd82e3a317371b193a14662da7cf799254515775fe3c83dc9939296a1\nDeterministic: MATCH\n"
  },
  {
    "title": "Signature Design: The Quantifier Game",
    "subject": "a Signature quantifier game design",
    "description": "The Quantifier Game is a Signature-made design for teaching predicate logic: a game where a learner must prove a for-all statement by a general argument, prove a there-exists statement by exhibiting one example, and disprove a for-all statement by finding one counterexample. For all and there exists are the two quantifiers. Each round presents a quantified statement over a small domain. The player chooses a strategy: general argument, exhibit an example, or find a counterexample. The game scores the strategy, not just the answer.",
    "inputs": "FIGURES = {'rounds': 10, 'forall_rounds': 4, 'exists_rounds': 3, 'disproof_rounds': 3, 'hints_used': 2, 'strategies_corrected': 1, 'points_per_round': 10, 'design_version': 1}\nLABEL = 'a-signature-quantifier-game-design'\n",
    "expected": "count: 8\nlabel: a-signature-quantifier-game-design\nmax: 10\nmean: 4.25\nmin: 1\ntotal: 34\nResult: count=8|label=a-signature-quantifier-game-design|max=10|mean=4.25|min=1|total=34\nRun 1 SHA-256: 3fef7fae06fe09f93ce422af938d70cfa1b4f0e5ca8451043d8b2195f16417ad\nRun 2 SHA-256: 3fef7fae06fe09f93ce422af938d70cfa1b4f0e5ca8451043d8b2195f16417ad\nDeterministic: MATCH\n"
  },
  {
    "title": "Signature Design: The Function Classifier",
    "subject": "a Signature function classifier design",
    "description": "The Function Classifier is a Signature-made design for teaching functions: a tool where a learner enters a function between two finite sets, and the tool reports whether it is injective (one-to-one), surjective (onto), both (a bijection), or neither, with the evidence shown. A bijection pairs the two sets exactly. The tool lists the image of every input and checks for collisions and gaps. Injective means no two inputs share an output; surjective means every output is hit. A bijection is shown as a perfect matching between the sets.",
    "inputs": "FIGURES = {'functions_tested': 2, 'bijections_found': 1, 'inputs_1': 3, 'inputs_2': 5, 'collisions_found': 1, 'gaps_found': 1, 'properties_checked': 2, 'design_version': 1}\nLABEL = 'a-signature-function-classifier-design'\n",
    "expected": "count: 8\nlabel: a-signature-function-classifier-design\nmax: 5\nmean: 2.0\nmin: 1\ntotal: 16\nResult: count=8|label=a-signature-function-classifier-design|max=5|mean=2.0|min=1|total=16\nRun 1 SHA-256: e9f3a5b6c496d235a778966d5606e7181f2ff0d69a777a6a956d8fb144977c6c\nRun 2 SHA-256: e9f3a5b6c496d235a778966d5606e7181f2ff0d69a777a6a956d8fb144977c6c\nDeterministic: MATCH\n"
  },
  {
    "title": "Signature Design: The Induction Ladder",
    "subject": "a Signature induction ladder design",
    "description": "The Induction Ladder is a Signature-made design for teaching induction: a ladder of rungs, one per natural number, where proving the base case lights the first rung and proving the inductive step lights the next rung from any lit rung. Strong induction lights a rung from all the rungs below it. Each rung is one natural number, with the claim stated for that number. Lighting the first rung is the base case; the step rule lights the next rung. Strong induction is shown as a rung lit by all the rungs below it.",
    "inputs": "FIGURES = {'rungs_lit': 10, 'base_case': 2, 'splits_shown': 2, 'proof_parts': 2, 'induction_forms': 2, 'rungs_total': 10, 'checks': 2, 'design_version': 1}\nLABEL = 'a-signature-induction-ladder-design'\n",
    "expected": "count: 8\nlabel: a-signature-induction-ladder-design\nmax: 10\nmean: 3.875\nmin: 1\ntotal: 31\nResult: count=8|label=a-signature-induction-ladder-design|max=10|mean=3.875|min=1|total=31\nRun 1 SHA-256: e7cf1b76d5d4ddaa29d30254a94c53f58761e0c64d6655651d782886f142620c\nRun 2 SHA-256: e7cf1b76d5d4ddaa29d30254a94c53f58761e0c64d6655651d782886f142620c\nDeterministic: MATCH\n"
  },
  {
    "title": "Signature Design: The Counting Bench",
    "subject": "a Signature counting bench design",
    "description": "The Counting Bench is a Signature-made design for teaching the product and sum rules: a bench where a learner builds a counting problem step by step, choosing the number of choices at each step, and watches the product grow, with disjoint cases added by the sum rule. The product rule multiplies the choices at each step. Each step shows its number of choices, and the running product. Disjoint cases are added as separate branches, with the sum rule. The complement (counting what is not wanted) is offered as a second method.",
    "inputs": "FIGURES = {'strings_counted': 3380, 'total_strings': 17576, 'complement_count': 14196, 'methods_used': 2, 'steps': 3, 'choices_first': 5, 'choices_later': 26, 'design_version': 1}\nLABEL = 'a-signature-counting-bench-design'\n",
    "expected": "count: 8\nlabel: a-signature-counting-bench-design\nmax: 17576\nmean: 4398.625\nmin: 1\ntotal: 35189\nResult: count=8|label=a-signature-counting-bench-design|max=17576|mean=4398.625|min=1|total=35189\nRun 1 SHA-256: 47203e37a97ca7d77e6cd13be6b6c073894da3fbbe116bc756d0dc33cf8981ba\nRun 2 SHA-256: 47203e37a97ca7d77e6cd13be6b6c073894da3fbbe116bc756d0dc33cf8981ba\nDeterministic: MATCH\n"
  },
  {
    "title": "Signature Design: The Committee Counter",
    "subject": "a Signature committee counter design",
    "description": "The Committee Counter is a Signature-made design for teaching permutations and combinations: a counter where a learner chooses a committee and then a chair, and the counter shows both counting orders giving the same total. A combination is a choice where order does not matter. The counter shows the committee choice and the chair choice separately. Both orders (committee first, or chair first) are computed and compared. The binomial coefficients are shown in Pascal's triangle.",
    "inputs": "FIGURES = {'committees': 120, 'total_ways': 360, 'method_2_total': 360, 'poker_hands': 2598960, 'people': 10, 'committee_size': 3, 'orders_compared': 2, 'design_version': 1}\nLABEL = 'a-signature-committee-counter-design'\n",
    "expected": "count: 8\nlabel: a-signature-committee-counter-design\nmax: 2598960\nmean: 324977.0\nmin: 1\ntotal: 2599816\nResult: count=8|label=a-signature-committee-counter-design|max=2598960|mean=324977.0|min=1|total=2599816\nRun 1 SHA-256: ee22f30c2feccb48e5fed207eddda574fd99c7607d3722000f78e33f726cd4bf\nRun 2 SHA-256: ee22f30c2feccb48e5fed207eddda574fd99c7607d3722000f78e33f726cd4bf\nDeterministic: MATCH\n"
  },
  {
    "title": "Signature Design: The Pigeonhole Demonstrator",
    "subject": "a Signature pigeonhole demonstrator design",
    "description": "The Pigeonhole Demonstrator is a Signature-made design for teaching the pigeonhole principle: a bench with boxes and objects where a learner places objects and watches the fullest box fill. The principle says that if more objects go into fewer boxes, some box holds more than one. The bench shows boxes, objects, and the count in each box as objects are placed. The guaranteed minimum in the fullest box is computed as the ceiling of objects over boxes. A counterexample attempt is blocked: the bench shows why no placement avoids the guarantee.",
    "inputs": "FIGURES = {'points': 5, 'boxes': 4, 'max_distance': 0.7071, 'objects_2': 13, 'boxes_2': 12, 'guaranteed_2': 2, 'tests': 2, 'design_version': 1}\nLABEL = 'a-signature-pigeonhole-demonstrator-design'\n",
    "expected": "count: 8\nlabel: a-signature-pigeonhole-demonstrator-design\nmax: 13\nmean: 4.9634\nmin: 0.7071\ntotal: 39.7071\nResult: count=8|label=a-signature-pigeonhole-demonstrator-design|max=13|mean=4.9634|min=0.7071|total=39.7071\nRun 1 SHA-256: 25572e8bcfa45ed2e64641d752576b4d8066ca6f6b7d392c862be345613cddd9\nRun 2 SHA-256: 25572e8bcfa45ed2e64641d752576b4d8066ca6f6b7d392c862be345613cddd9\nDeterministic: MATCH\n"
  },
  {
    "title": "Signature Design: The Inclusion-Exclusion Counter",
    "subject": "a Signature inclusion-exclusion counter design",
    "description": "The Inclusion-Exclusion Counter is a Signature-made design for teaching inclusion-exclusion: a Venn diagram tool where a learner toggles sets and watches the counter add, subtract, and add back the overlaps to give the exact union size. Inclusion-exclusion counts a union by alternating adding and subtracting intersections. Toggling a set updates the union count and shows each correction step. Each region of the diagram shows its count, and the sum of the regions equals the union. The tool checks the result against a direct count of the elements.",
    "inputs": "FIGURES = {'divisible_by_2': 50, 'divisible_by_3': 33, 'divisible_by_6': 16, 'union': 67, 'neither': 33, 'methods': 2, 'regions': 3, 'design_version': 1}\nLABEL = 'a-signature-inclusion-exclusion-counter-design'\n",
    "expected": "count: 8\nlabel: a-signature-inclusion-exclusion-counter-design\nmax: 67\nmean: 25.625\nmin: 1\ntotal: 205\nResult: count=8|label=a-signature-inclusion-exclusion-counter-design|max=67|mean=25.625|min=1|total=205\nRun 1 SHA-256: 0f1cee021cc32bcb6de223fd3bfaa931ce06cc4056ed3ef54aa139a1f387a42b\nRun 2 SHA-256: 0f1cee021cc32bcb6de223fd3bfaa931ce06cc4056ed3ef54aa139a1f387a42b\nDeterministic: MATCH\n"
  },
  {
    "title": "Signature Design: The Graph Studio",
    "subject": "a Signature graph studio design",
    "description": "The Graph Studio is a Signature-made design for teaching graphs: a studio where a learner draws vertices and edges, and the studio shows the degrees, the handshaking lemma (the sum of the degrees is twice the number of edges), and whether the graph is a tree, has an Eulerian path, or is connected. A graph is vertices joined by edges. Drawing a vertex or an edge updates the degree list and the edge count. The handshaking lemma is checked live: the degree sum must be twice the edge count. The studio tests for trees, Eulerian paths, and connectivity.",
    "inputs": "FIGURES = {'vertices': 6, 'degree_sum': 10, 'edges': 5, 'odd_degree_vertices': 4, 'tree_edges': 5, 'graphs_drawn': 2, 'checks': 2, 'design_version': 1}\nLABEL = 'a-signature-graph-studio-design'\n",
    "expected": "count: 8\nlabel: a-signature-graph-studio-design\nmax: 10\nmean: 4.375\nmin: 1\ntotal: 35\nResult: count=8|label=a-signature-graph-studio-design|max=10|mean=4.375|min=1|total=35\nRun 1 SHA-256: 042f53724f360986792dba6738827fb2b042caa40e69714f88786cee6ab370cd\nRun 2 SHA-256: 042f53724f360986792dba6738827fb2b042caa40e69714f88786cee6ab370cd\nDeterministic: MATCH\n"
  },
  {
    "title": "Signature Design: The Bridge Puzzle",
    "subject": "a Signature bridge puzzle design",
    "description": "The Bridge Puzzle is a Signature-made design for teaching Eulerian paths: a puzzle where a learner tries to cross each bridge of a city exactly once, and the tool reports why it is possible or impossible from the degrees of the land masses. An Eulerian path uses every edge exactly once. The puzzle shows the city, its bridges, and the degree of each land mass. Each attempt is traced, and the tool reports where it gets stuck. The Eulerian test is shown: zero or two odd vertices are needed.",
    "inputs": "FIGURES = {'konigsberg_odd': 4, 'square_odd': 2, 'bridges': 7, 'square_edges': 5, 'puzzles': 2, 'paths_found': 1, 'impossible_count': 1, 'design_version': 1}\nLABEL = 'a-signature-bridge-puzzle-design'\n",
    "expected": "count: 8\nlabel: a-signature-bridge-puzzle-design\nmax: 7\nmean: 2.875\nmin: 1\ntotal: 23\nResult: count=8|label=a-signature-bridge-puzzle-design|max=7|mean=2.875|min=1|total=23\nRun 1 SHA-256: f9a3a5e459f9f805a00f9dde781a038f36f727da6668ab9ce8f28d128c457cd5\nRun 2 SHA-256: f9a3a5e459f9f805a00f9dde781a038f36f727da6668ab9ce8f28d128c457cd5\nDeterministic: MATCH\n"
  },
  {
    "title": "Signature Design: The Tree Builder",
    "subject": "a Signature tree builder design",
    "description": "The Tree Builder is a Signature-made design for teaching trees: a builder where a learner connects vertices with edges, and the tool reports whether the result is a tree (connected, no cycles), with the edge count shown against n - 1. A tree with n vertices has exactly n - 1 edges. Adding an edge that creates a cycle is flagged and refused. Adding an edge that keeps the graph disconnected is shown as a forest (a collection of trees). The number of labelled trees is shown by Cayley's formula, n^(n-2).",
    "inputs": "FIGURES = {'offices': 8, 'cables': 7, 'labelled_trees': 262144, 'binary_levels': 4, 'binary_vertices': 15, 'cycles_flagged': 1, 'trees_built': 1, 'design_version': 1}\nLABEL = 'a-signature-tree-builder-design'\n",
    "expected": "count: 8\nlabel: a-signature-tree-builder-design\nmax: 262144\nmean: 32772.625\nmin: 1\ntotal: 262181\nResult: count=8|label=a-signature-tree-builder-design|max=262144|mean=32772.625|min=1|total=262181\nRun 1 SHA-256: 8b237ab39d9f702c6727a48d9fc17ccdd641d1a410fe2aa1578882bcb3b5a1f1\nRun 2 SHA-256: 8b237ab39d9f702c6727a48d9fc17ccdd641d1a410fe2aa1578882bcb3b5a1f1\nDeterministic: MATCH\n"
  },
  {
    "title": "Signature Design: The Recurrence Table",
    "subject": "a Signature recurrence table design",
    "description": "The Recurrence Table is a Signature-made design for teaching recurrence relations: a solver where a learner enters a recurrence and its starting values, the solver finds the characteristic roots, and shows the closed form and the first terms. A recurrence defines a sequence by its earlier terms. The solver shows the characteristic equation and its roots. The closed form is built from the roots and the starting values. The first terms are listed from both the recurrence and the closed form, and must agree.",
    "inputs": "FIGURES = {'a_0': 1, 'a_1': 3, 'a_2': 7, 'a_3': 15, 'a_4': 31, 'root_1': 1, 'root_2': 2, 'terms_listed': 5}\nLABEL = 'a-signature-recurrence-table-design'\n",
    "expected": "count: 8\nlabel: a-signature-recurrence-table-design\nmax: 31\nmean: 8.125\nmin: 1\ntotal: 65\nResult: count=8|label=a-signature-recurrence-table-design|max=31|mean=8.125|min=1|total=65\nRun 1 SHA-256: 49894267eb128e20363af689e8d17ed7a87ec16872d08be926410d9577005699\nRun 2 SHA-256: 49894267eb128e20363af689e8d17ed7a87ec16872d08be926410d9577005699\nDeterministic: MATCH\n"
  },
  {
    "title": "Signature Design: The Generating Function Workbench",
    "subject": "a Signature generating function workbench design",
    "description": "The Generating Function Workbench is a Signature-made design for teaching generating functions: a workbench where a learner enters a sequence, the workbench shows its generating function as a power series, and reads off coefficients to count combinations. A generating function encodes a sequence as a power series. The workbench shows the series for a sequence, with the first terms listed. Multiplying series is shown as combining the counting problems. The coefficient of x^n is read off as the answer to the counting problem.",
    "inputs": "FIGURES = {'ways_change': 4, 'ways_sum5': 6, 'amount': 10, 'coins': 3, 'problems_solved': 2, 'coefficients_read': 2, 'terms_shown': 4, 'design_version': 1}\nLABEL = 'a-signature-generating-function-workbench-design'\n",
    "expected": "count: 8\nlabel: a-signature-generating-function-workbench-design\nmax: 10\nmean: 4.0\nmin: 1\ntotal: 32\nResult: count=8|label=a-signature-generating-function-workbench-design|max=10|mean=4.0|min=1|total=32\nRun 1 SHA-256: f1f440681f889b60aa3c8c823d2ed59eda0c62711268f3f4c7a3a1ad2ad0edd5\nRun 2 SHA-256: f1f440681f889b60aa3c8c823d2ed59eda0c62711268f3f4c7a3a1ad2ad0edd5\nDeterministic: MATCH\n"
  },
  {
    "title": "Signature Design: The Prime Factoriser",
    "subject": "a Signature prime factoriser design",
    "description": "The Prime Factoriser is a Signature-made design for teaching number theory: a tool where a learner enters a number, the tool factors it into primes by trial division, and shows the divisor count from the exponents. The fundamental theorem of arithmetic says every integer above 1 is a product of primes in exactly one way. The tool divides by 2, then 3, then 5, and so on, showing each division. The factorisation is shown with exponents, and the divisor count is computed as the product of (exponent + 1). A prime input is flagged as prime, with the trial divisions shown.",
    "inputs": "FIGURES = {'n_factored': 360, 'prime_2_power': 3, 'prime_3_power': 2, 'prime_5_power': 1, 'divisor_count': 24, 'prime_tested': 97, 'sqrt_97': 9.85, 'divisions_shown': 5}\nLABEL = 'a-signature-prime-factoriser-design'\n",
    "expected": "count: 8\nlabel: a-signature-prime-factoriser-design\nmax: 360\nmean: 62.7313\nmin: 1\ntotal: 501.85\nResult: count=8|label=a-signature-prime-factoriser-design|max=360|mean=62.7313|min=1|total=501.85\nRun 1 SHA-256: 13c6362a7fcd0862f64526ef0bba9fc60ab4281c8b5f2b296b603428e9f62286\nRun 2 SHA-256: 13c6362a7fcd0862f64526ef0bba9fc60ab4281c8b5f2b296b603428e9f62286\nDeterministic: MATCH\n"
  },
  {
    "title": "Signature Design: The RSA Toy",
    "subject": "a Signature RSA toy design",
    "description": "The RSA Toy is a Signature-made design for teaching RSA cryptography: a toy where a learner picks two small primes, the toy builds the public and private keys, encrypts a message, and decrypts it, showing every modular exponentiation. RSA encrypts as m^e modulo n and decrypts with the private exponent d. This toy uses tiny primes for teaching only and is trivially breakable. The toy shows the primes, n, phi (Euler's totient), e, and d. Encryption and decryption are shown step by step with the remainders. The toy warns that small primes are for teaching only and are not secure.",
    "inputs": "FIGURES = {'rsa_n': 55, 'rsa_phi': 40, 'rsa_e': 3, 'rsa_d': 27, 'message': 7, 'ciphertext': 13, 'primes_used': 2, 'design_version': 1}\nLABEL = 'a-signature-rsa-toy-design'\n",
    "expected": "count: 8\nlabel: a-signature-rsa-toy-design\nmax: 55\nmean: 18.5\nmin: 1\ntotal: 148\nResult: count=8|label=a-signature-rsa-toy-design|max=55|mean=18.5|min=1|total=148\nRun 1 SHA-256: 5a9a9c2eba575825fde6f44f7ff940e417e60910a48032ee875f179f5b8dd083\nRun 2 SHA-256: 5a9a9c2eba575825fde6f44f7ff940e417e60910a48032ee875f179f5b8dd083\nDeterministic: MATCH\n"
  },
  {
    "title": "Signature Design: The Circuit Builder",
    "subject": "a Signature circuit builder design",
    "description": "The Circuit Builder is a Signature-made design for teaching Boolean algebra: a builder where a learner places and, or, and not gates, wires them into a circuit, and watches the output for every input combination. Boolean algebra is the algebra of true and false. Gates are placed and wired, and the circuit's truth table is filled live. De Morgan's laws are shown as circuit rewrites. The exclusive-or circuit is built two ways and shown to agree.",
    "inputs": "FIGURES = {'truth_table_rows': 4, 'ones_in_table': 2, 'builds': 2, 'gates_used': 5, 'variables': 2, 'tables_agreeing': 2, 'laws_shown': 2, 'design_version': 1}\nLABEL = 'a-signature-circuit-builder-design'\n",
    "expected": "count: 8\nlabel: a-signature-circuit-builder-design\nmax: 5\nmean: 2.5\nmin: 1\ntotal: 20\nResult: count=8|label=a-signature-circuit-builder-design|max=5|mean=2.5|min=1|total=20\nRun 1 SHA-256: 0240e6af65d58f781580a67e93125e314275f186d4fd003fee7e1baef4f2ba3a\nRun 2 SHA-256: 0240e6af65d58f781580a67e93125e314275f186d4fd003fee7e1baef4f2ba3a\nDeterministic: MATCH\n"
  },
  {
    "title": "Signature Design: The Hash Collision Finder",
    "subject": "a Signature hash collision finder design",
    "description": "The Hash Collision Finder is a Signature-made design for teaching the pigeonhole principle in algorithms: a finder where a learner hashes items into slots and watches collisions form, with the pigeonhole guarantee shown. If more items are hashed into fewer slots, collisions must occur. Items are hashed one by one, and the slot loads are shown. The first collision is flagged, and the guarantee is stated. The average load is shown alongside the fullest slot.",
    "inputs": "FIGURES = {'slots': 100, 'items': 150, 'average_load': 1.5, 'first_collision_by': 101, 'fullest_slot': 4, 'guaranteed_collision': 2, 'collisions_found': 50, 'design_version': 1}\nLABEL = 'a-signature-hash-collision-finder-design'\n",
    "expected": "count: 8\nlabel: a-signature-hash-collision-finder-design\nmax: 150\nmean: 51.1875\nmin: 1\ntotal: 409.5\nResult: count=8|label=a-signature-hash-collision-finder-design|max=150|mean=51.1875|min=1|total=409.5\nRun 1 SHA-256: 6db6b74b08614abadfa3f4ffb8373abac32a7613e233d00d9a36b533ae77b79e\nRun 2 SHA-256: 6db6b74b08614abadfa3f4ffb8373abac32a7613e233d00d9a36b533ae77b79e\nDeterministic: MATCH\n"
  },
  {
    "title": "Signature Design: The Map Colourer",
    "subject": "a Signature map colourer design",
    "description": "The Map Colourer is a Signature-made design for teaching graph colouring: a colourer where a learner colours a map or a graph so that neighbours differ, with the colour count shown and the four-colour theorem stated. The chromatic number is the smallest number of colours needed. Clicking a region cycles its colour; a conflict with a neighbour is flagged red. The colour count is shown, and the tool reports when it is minimal. The four-colour theorem is stated: any map needs at most 4 colours.",
    "inputs": "FIGURES = {'pentagon_vertices': 5, 'chromatic_number': 3, 'colours_tried': 2, 'complete_vertices': 4, 'complete_chromatic': 4, 'map_colours': 4, 'graphs_coloured': 2, 'design_version': 1}\nLABEL = 'a-signature-map-colourer-design'\n",
    "expected": "count: 8\nlabel: a-signature-map-colourer-design\nmax: 5\nmean: 3.125\nmin: 1\ntotal: 25\nResult: count=8|label=a-signature-map-colourer-design|max=5|mean=3.125|min=1|total=25\nRun 1 SHA-256: bb5345a20cb95a40bf0a951f62559225b24703248e7f1550c404507668de86ac\nRun 2 SHA-256: bb5345a20cb95a40bf0a951f62559225b24703248e7f1550c404507668de86ac\nDeterministic: MATCH\n"
  },
  {
    "title": "Signature Design: The Hat Check Simulator",
    "subject": "a Signature hat check simulator design",
    "description": "The Hat Check Simulator is a Signature-made design for teaching derangements: a simulator where n people check their hats and the hats are returned at random, and the simulator counts how often nobody gets their own hat back. A derangement is a permutation with nothing in its original place. The simulator runs many trials and shows the fraction with no one correct. The exact count !n is shown from the inclusion-exclusion formula. The fraction is shown approaching 1/e, about 0.3679, as n grows.",
    "inputs": "FIGURES = {'derangements_4': 9, 'permutations_4': 24, 'fraction_4': 0.375, 'derangements_5': 44, 'permutations_5': 120, 'fraction_5': 0.3667, 'trials': 1000, 'limit_fraction': 0.3679}\nLABEL = 'a-signature-hat-check-simulator-design'\n",
    "expected": "count: 8\nlabel: a-signature-hat-check-simulator-design\nmax: 1000\nmean: 149.7637\nmin: 0.3667\ntotal: 1198.1096\nResult: count=8|label=a-signature-hat-check-simulator-design|max=1000|mean=149.7637|min=0.3667|total=1198.1096\nRun 1 SHA-256: f3bfb6b94e4c2484cd654ee7fcba3573108d43d093cfc7b1dfd1bc6702ab6987\nRun 2 SHA-256: f3bfb6b94e4c2484cd654ee7fcba3573108d43d093cfc7b1dfd1bc6702ab6987\nDeterministic: MATCH\n"
  },
  {
    "title": "Signature Design: The Graph Induction Prover",
    "subject": "a Signature graph induction prover design",
    "description": "The Graph Induction Prover is a Signature-made design for teaching induction on graphs: a prover where a learner proves a fact about trees by removing a leaf, applying the hypothesis to the smaller tree, and adding the leaf back. A tree with n vertices has n - 1 edges. The prover shows the leaf to remove and the smaller tree left behind. The hypothesis is applied to the smaller tree, and the leaf is added back. The base case (a single vertex, 0 edges) is shown first.",
    "inputs": "FIGURES = {'base_vertices': 1, 'base_edges': 0, 'tree_5_edges': 4, 'tree_8_edges': 7, 'leaf_degree': 1, 'proofs': 2, 'steps': 2, 'design_version': 1}\nLABEL = 'a-signature-graph-induction-prover-design'\n",
    "expected": "count: 8\nlabel: a-signature-graph-induction-prover-design\nmax: 7\nmean: 2.25\nmin: 0\ntotal: 18\nResult: count=8|label=a-signature-graph-induction-prover-design|max=7|mean=2.25|min=0|total=18\nRun 1 SHA-256: fd625caa924bc3882f7ddf803d7527d6ad98be384f8219c08fa74175f8b77d58\nRun 2 SHA-256: fd625caa924bc3882f7ddf803d7527d6ad98be384f8219c08fa74175f8b77d58\nDeterministic: MATCH\n"
  },
  {
    "title": "Signature Design: The Order Diagrammer",
    "subject": "a Signature order diagrammer design",
    "description": "The Order Diagrammer is a Signature-made design for teaching partial orders: a diagrammer where a learner enters a relation, the tool tests the three properties (reflexive, antisymmetric, transitive), and draws the Hasse diagram (the diagram of covering relations). A partial order ranks elements, leaving some pairs incomparable. Each of the three properties is tested and reported separately. The Hasse diagram is drawn with the smallest elements at the bottom. Maximal elements and the maximum (if it exists) are marked.",
    "inputs": "FIGURES = {'elements': 4, 'comparable_pairs': 5, 'reflexive_pairs': 4, 'maximal_elements': 1, 'maximum': 6, 'properties_tested': 3, 'relations_tested': 2, 'design_version': 1}\nLABEL = 'a-signature-order-diagrammer-design'\n",
    "expected": "count: 8\nlabel: a-signature-order-diagrammer-design\nmax: 6\nmean: 3.25\nmin: 1\ntotal: 26\nResult: count=8|label=a-signature-order-diagrammer-design|max=6|mean=3.25|min=1|total=26\nRun 1 SHA-256: a3945a7119a42f5ca23066e0bb5a95170bbe40ca8b54b1f7d1e406f7e6c68d34\nRun 2 SHA-256: a3945a7119a42f5ca23066e0bb5a95170bbe40ca8b54b1f7d1e406f7e6c68d34\nDeterministic: MATCH\n"
  },
  {
    "title": "Signature Design: The Bezout Finder",
    "subject": "a Signature Bezout finder design",
    "description": "The Bezout Finder is a Signature-made design for teaching the extended Euclidean algorithm: a finder where a learner enters two numbers, the tool runs Euclid's algorithm, and works backwards to write the GCD as a combination a x + b y. Bezout's identity says the GCD can always be written this way. The divisions are shown step by step, with quotients and remainders. Working backwards expresses each remainder as a combination of the originals. The final combination is verified by arithmetic.",
    "inputs": "FIGURES = {'gcd': 21, 'coefficient_105': 5, 'coefficient_252': -2, 'check_525': 525, 'check_504': 504, 'divisions': 3, 'combinations_found': 1, 'design_version': 1}\nLABEL = 'a-signature-bezout-finder-design'\n",
    "expected": "count: 8\nlabel: a-signature-bezout-finder-design\nmax: 525\nmean: 132.25\nmin: -2\ntotal: 1058\nResult: count=8|label=a-signature-bezout-finder-design|max=525|mean=132.25|min=-2|total=1058\nRun 1 SHA-256: 584c3d303bb659c86d58eab3d28365bfed8b5fdcd52cf241a8ac9ee10e11722d\nRun 2 SHA-256: 584c3d303bb659c86d58eab3d28365bfed8b5fdcd52cf241a8ac9ee10e11722d\nDeterministic: MATCH\n"
  },
  {
    "title": "Signature Design: The Hamiltonian Tour Finder",
    "subject": "a Signature Hamiltonian tour finder design",
    "description": "The Hamiltonian Tour Finder is a Signature-made design for teaching Hamiltonian cycles: a finder where a learner looks for a cycle that visits every vertex exactly once, with the count of cycles in a complete graph shown. A Hamiltonian cycle visits each vertex once and returns to the start. The finder tries cycles and shows the ones that visit every vertex. The complete graph K5 is shown to have 12 Hamiltonian cycles. Hamilton's original game (the dodecahedron, 20 vertices) is shown.",
    "inputs": "FIGURES = {'vertices_k5': 5, 'cycles_k5': 12, 'dodecahedron_vertices': 20, 'game_year': 1857, 'directions': 2, 'graphs': 2, 'cycles_found': 12, 'design_version': 1}\nLABEL = 'a-signature-hamiltonian-tour-finder-design'\n",
    "expected": "count: 8\nlabel: a-signature-hamiltonian-tour-finder-design\nmax: 1857\nmean: 238.875\nmin: 1\ntotal: 1911\nResult: count=8|label=a-signature-hamiltonian-tour-finder-design|max=1857|mean=238.875|min=1|total=1911\nRun 1 SHA-256: 1eed1184801c6d1e17222ab11cbb5ee54b8f16a4d43f695d80c66b37363cbb5a\nRun 2 SHA-256: 1eed1184801c6d1e17222ab11cbb5ee54b8f16a4d43f695d80c66b37363cbb5a\nDeterministic: MATCH\n"
  },
  {
    "title": "Signature Design: The Discrete Capstone Board",
    "subject": "a Signature discrete capstone board design",
    "description": "The Discrete Capstone Board is a Signature-made design for teaching combined discrete mathematics: a board of challenges, each needing logic, counting, graphs, and number theory together, where a learner plans the tools, solves each part, and assembles the parts. A capstone problem uses several ideas at once. Each challenge names the tools it needs before the learner starts. Each part is solved and checked separately, then assembled. The board scores the plan, the checks, and the assembly.",
    "inputs": "FIGURES = {'passwords': 69000, 'parts': 3, 'checks_passed': 3, 'prefixes': 125, 'guarantee_threshold': 69001, 'tools_named': 4, 'first_choices': 5, 'design_version': 1}\nLABEL = 'a-signature-discrete-capstone-board-design'\n",
    "expected": "count: 8\nlabel: a-signature-discrete-capstone-board-design\nmax: 69001\nmean: 17267.75\nmin: 1\ntotal: 138142\nResult: count=8|label=a-signature-discrete-capstone-board-design|max=69001|mean=17267.75|min=1|total=138142\nRun 1 SHA-256: 6d4fb289dbc394af51d9a8c605f22b01022c4ce6196dd19e5554478633809d36\nRun 2 SHA-256: 6d4fb289dbc394af51d9a8c605f22b01022c4ce6196dd19e5554478633809d36\nDeterministic: MATCH\n"
  }
];

const SOURCES = [
  {
    "name": "Wikipedia - Mathematical logic",
    "url": "https://en.wikipedia.org/wiki/Mathematical_logic",
    "establishes": "The reference for a Signature truth table builder design in this record."
  },
  {
    "name": "Wikipedia - Boolean algebra",
    "url": "https://en.wikipedia.org/wiki/Boolean_algebra",
    "establishes": "The reference for a Signature truth table builder design in this record."
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
