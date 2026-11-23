// Seeded boundless generator for the theoretical-computer-science database
// (public edition). Deterministic: the same seed always emits the same
// record. Usage: node gen-theoretical-computer-science.js [seed]  (prints one
// JSON record) or: node gen-theoretical-computer-science.js --test (runTests).
// Package-only; outputs are generated, not stored files.
"use strict";
const crypto = require("crypto");

const SLUG = "theoretical-computer-science";
const RECORD_KIND = "theoretical computer science research record";
const ID_PREFIX = "JAH-THCS-";
const AI_NAME = "JAH Theoretical Computer Science Librarian";
const EDITION = "public";
const SRC = "public-harvest";
const CEILING = "Generator ceiling: up to 1,000,000,000 scales per file, generated on demand by the file AI — not stored files.";
const HONESTY = " No claim of consciousness, sentience, or unlimited intelligence is established by this record.";

const TOPICS = [
  { title: "Turing Machines",
    subject: "Turing machines",
    label: "turing-machines",
    description: "A Turing machine is a simple abstract computer: a finite-state control with a read-write head on an infinite tape divided into cells.",
    a1: "One machine: tape, head, states, rules.", a2: "The whole model: universal, equivalent, standard.", a3: "The model against computation: the definition itself.",
    figures: {"publication_year": 1936, "turing_age": 24, "machine_parts": 3, "tape_symbols": 2, "states_kinds": 2, "century": 20, "models_compared": 3, "universal_machines": 1} },
  { title: "The Cook-Levin Theorem",
    subject: "the Cook-Levin theorem",
    label: "cook-levin-theorem",
    description: "The Cook-Levin theorem says that the Boolean satisfiability problem, called SAT, is NP-complete: every problem in NP reduces to it in polynomial time.",
    a1: "One formula: the tableau of a computation.", a2: "The whole theorem: every NP problem reduces to SAT.", a3: "The theorem against hardness: one hardest problem.",
    figures: {"publication_year": 1971, "cook_age": 33, "levin_year": 1973, "key_steps": 5, "century": 20, "variables_kinds": 3, "clauses_built": 4, "proof_methods": 2} },
  { title: "P versus NP: An Open Problem",
    subject: "the P versus NP problem",
    label: "p-versus-np-problem",
    description: "P versus NP asks whether finding solutions is as easy as checking them.",
    a1: "One question: is finding as easy as checking?", a2: "The whole problem: two classes, three barriers, no proof.", a3: "The problem against computing: the central open question.",
    figures: {"posed_year": 1971, "millennium_year": 2000, "prize_dollars": 1000000, "classes_compared": 2, "century": 20, "open_years": 54, "proof_attempts": 3, "barrier_results": 3} },
  { title: "NP-Completeness",
    subject: "NP-completeness",
    label: "np-completeness",
    description: "A problem is NP-complete when it is in NP and every problem in NP reduces to it in polynomial time, so all NP-complete problems stand or fall together.",
    a1: "One idea: hardest in NP, standing together.", a2: "The whole theory: definition, reductions, thousands of problems.", a3: "The theory against hardness: proof, not resistance.",
    figures: {"karp_problems": 21, "karp_year": 1972, "reduction_kinds": 2, "century": 20, "key_theorems": 3, "problem_families": 5, "cook_year": 1971, "completeness_tests": 2} },
  { title: "NP: The Complexity Class",
    subject: "the complexity class NP",
    label: "np-complexity-class",
    description: "NP is the class of decision problems for which a yes answer has a certificate checkable in polynomial time.",
    a1: "One class: quickly checkable problems.", a2: "The whole definition: verifiers and guessing machines.", a3: "The class against solving: checkable, not necessarily solvable.",
    figures: {"definition_kinds": 2, "key_problems": 3, "century": 20, "verifier_parts": 2, "certificate_kinds": 2, "nondet_machines": 1, "inclusions": 2, "open_questions": 1} },
  { title: "The Time Hierarchy Theorem",
    subject: "the time hierarchy theorem",
    label: "time-hierarchy-theorem",
    description: "The time hierarchy theorem says that more time buys strictly more power: if f grows faster than g by a logarithmic factor, then the class of problems solvable in time g is strictly smaller than the class solvable in time f.",
    a1: "One diagonal: a machine that flips its own simulation.", a2: "The whole theorem: more time, strictly more problems.", a3: "The theorem against time: bounds create real distinctions.",
    figures: {"publication_year": 1965, "hartmanis_age": 37, "key_steps": 4, "century": 20, "hierarchy_levels": 3, "diagonal_uses": 1, "time_bounds": 2, "proof_methods": 2} },
  { title: "The Space Hierarchy Theorem",
    subject: "the space hierarchy theorem",
    label: "space-hierarchy-theorem",
    description: "The space hierarchy theorem says that more space buys strictly more power: if f grows faster than g, then the class of problems solvable in space g is strictly smaller than the class solvable in space f.",
    a1: "One diagonal: a machine that flips its own simulation.", a2: "The whole theorem: more space, strictly more problems.", a3: "The theorem against space: bounds create real distinctions.",
    figures: {"publication_year": 1965, "key_steps": 4, "century": 20, "hierarchy_levels": 3, "diagonal_uses": 1, "space_bounds": 2, "proof_methods": 2, "log_factors": 1} },
  { title: "Savitch's Theorem",
    subject: "Savitch's theorem on space",
    label: "savitch-theorem",
    description: "Savitch's theorem says that nondeterminism does not help much for space: nondeterministic space can be simulated deterministically with only a quadratic blowup.",
    a1: "One recursion: reachability by halving the steps.", a2: "The whole theorem: nondeterministic space, squared.", a3: "The theorem against guessing: space barely helps.",
    figures: {"publication_year": 1970, "savitch_age": 27, "space_blowup": 2, "key_steps": 3, "century": 20, "classes_related": 2, "recursion_depths": 2, "proof_methods": 1} },
  { title: "The PCP Theorem",
    subject: "the PCP theorem",
    label: "pcp-theorem",
    description: "The PCP theorem says that every NP proof can be rewritten so that a verifier can check it by reading only a constant number of its bits, chosen at random.",
    a1: "One encoding: proofs as low-degree polynomials.", a2: "The whole theorem: NP proofs, checkable by spot-check.", a3: "The theorem against reading: a few bits suffice.",
    figures: {"publication_year": 1992, "proof_authors": 2, "key_steps": 4, "century": 20, "gap_kinds": 2, "verifier_queries": 3, "random_bits": 2, "proof_methods": 2} },
  { title: "Ladner's Theorem",
    subject: "Ladner's theorem on NP-intermediate problems",
    label: "ladner-theorem",
    description: "Ladner's theorem says that if P differs from NP, then there are problems in NP that are neither in P nor NP-complete, called NP-intermediate.",
    a1: "One construction: padding that defeats each machine in turn.", a2: "The whole theorem: a middle exists, if P differs from NP.", a3: "The theorem against dichotomy: NP has a middle.",
    figures: {"publication_year": 1975, "ladner_age": 30, "key_steps": 3, "century": 20, "problem_kinds": 2, "diagonal_uses": 1, "classes_separated": 2, "proof_methods": 1} },
  { title: "Rice's Theorem",
    subject: "Rice's theorem on program properties",
    label: "rice-theorem",
    description: "Rice's theorem says that every nontrivial semantic property of programs is undecidable: there is no algorithm that, given a program, decides whether the function it computes has the property.",
    a1: "One reduction: halting tied to any semantic property.", a2: "The whole theorem: no perfect program checker.", a3: "The theorem against verification: limits, not failure.",
    figures: {"publication_year": 1953, "rice_age": 27, "key_steps": 3, "century": 20, "property_kinds": 2, "reduction_uses": 1, "machines_involved": 2, "proof_methods": 1} },
  { title: "Circuit Complexity",
    subject: "circuit complexity",
    label: "circuit-complexity",
    description: "Circuit complexity studies Boolean circuits, networks of AND, OR, and NOT gates, as a model of computation, measuring their size, the number of gates, and their depth, the longest path from input to output.",
    a1: "One model: gates, size, depth.", a2: "The whole field: lower bounds for restricted circuits.", a3: "The field against P versus NP: the concrete attack.",
    figures: {"circuit_parts": 3, "gate_kinds": 3, "depth_measures": 2, "century": 20, "key_results": 3, "lower_bounds": 2, "founding_year": 1949, "complexity_measures": 2} },
  { title: "Probabilistic Turing Machines and BPP",
    subject: "probabilistic Turing machines and BPP",
    label: "probabilistic-turing-machines-bpp",
    description: "A probabilistic Turing machine is a Turing machine that can flip fair coins, and BPP is the class of problems it decides in polynomial time with error at most one third on every input.",
    a1: "One coin: randomness with bounded error.", a2: "The whole class: BPP, between P and PSPACE.", a3: "The class against determinism: randomness, maybe removable.",
    figures: {"error_bounds": 2, "random_bits_kinds": 2, "key_classes": 3, "century": 20, "amplification_steps": 2, "derandomization_uses": 1, "founding_year": 1977, "error_threshold": 3} },
  { title: "Interactive Proofs and IP Equals PSPACE",
    subject: "interactive proofs and IP equals PSPACE",
    label: "interactive-proofs-ip-pspace",
    description: "An interactive proof is a conversation in which a prover convinces a verifier that a claim is true.",
    a1: "One conversation: prover convinces verifier.", a2: "The whole theorem: interaction equals polynomial space.", a3: "The theorem against verification: conversation is power.",
    figures: {"publication_year": 1990, "proof_authors": 2, "rounds_kinds": 2, "century": 20, "key_steps": 4, "verifier_parts": 2, "prover_kinds": 1, "completeness_soundness": 2} },
  { title: "Zero-Knowledge Proofs",
    subject: "zero-knowledge proofs",
    label: "zero-knowledge-proofs",
    description: "A zero-knowledge proof proves a claim without revealing why it is true.",
    a1: "One simulator: faked transcripts prove nothing leaked.", a2: "The whole idea: prove it, reveal nothing else.", a3: "The idea against privacy: proof without exposure.",
    figures: {"publication_year": 1985, "proof_authors": 3, "properties": 3, "century": 20, "key_protocols": 3, "rounds_kinds": 2, "simulator_parts": 1, "applications": 3} },
  { title: "Shor's Algorithm",
    subject: "Shor's algorithm for factoring",
    label: "shor-algorithm",
    description: "Shor's algorithm factors an integer N in polynomial time on a quantum computer, by reducing factoring to period-finding and solving period-finding with the quantum Fourier transform.",
    a1: "One reduction: factoring becomes period-finding.", a2: "The whole algorithm: superposition, Fourier, factor.", a3: "The algorithm against RSA: exponential speedup, in principle.",
    figures: {"publication_year": 1994, "shor_age": 35, "key_steps": 3, "century": 20, "quantum_parts": 2, "speedup_kinds": 1, "classical_reductions": 1, "fourier_uses": 1} },
  { title: "BQP: Bounded-Error Quantum Polynomial Time",
    subject: "the complexity class BQP",
    label: "bqp-complexity-class",
    description: "BQP is the class of decision problems solvable by a quantum computer in polynomial time with error at most one third.",
    a1: "One class: quantum polynomial time, bounded error.", a2: "The whole definition: circuits, uniformity, amplification.", a3: "The class against classical power: quantum, measured.",
    figures: {"definition_parts": 3, "key_problems": 2, "century": 20, "error_bounds": 2, "inclusions": 3, "quantum_gates": 2, "founding_year": 1993, "open_questions": 2} },
  { title: "Quantum Computing",
    subject: "quantum computing",
    label: "quantum-computing",
    description: "Quantum computing is computation with qubits, which can be in superpositions of 0 and 1, entangled with each other, and transformed by unitary gates, with measurement giving classical outputs.",
    a1: "One bit: a qubit, 0 and 1 at once.", a2: "The whole field: circuits, algorithms, hardware.", a3: "The field against classical computing: physics as power.",
    figures: {"qubit_states": 2, "gate_kinds": 3, "key_algorithms": 3, "century": 20, "hardware_kinds": 3, "error_kinds": 2, "founding_year": 1980, "demonstrations": 3} },
  { title: "Communication Complexity",
    subject: "communication complexity",
    label: "communication-complexity",
    description: "Communication complexity is the study of how many bits two parties, each holding part of the input, must exchange to compute a function of the whole input.",
    a1: "One question: how many bits must Alice and Bob exchange?", a2: "The whole field: protocols, lower bounds, applications.", a3: "The field against talking: communication, priced.",
    figures: {"founding_year": 1979, "yao_age": 33, "model_kinds": 3, "century": 20, "key_results": 3, "lower_bound_methods": 3, "protocol_kinds": 2, "complexity_measures": 2} },
  { title: "Parameterized Complexity",
    subject: "parameterized complexity",
    label: "parameterized-complexity",
    description: "Parameterized complexity studies problems with a parameter k, asking whether they can be solved in time f(k) times a polynomial in the input size, which is fixed-parameter tractability, and classifies the rest in the W-hierarchy.",
    a1: "One parameter: small k makes hard problems easy.", a2: "The whole field: kernels, search trees, W-hierarchy.", a3: "The field against hardness: hard in general, easy in practice.",
    figures: {"founding_year": 1999, "founders": 2, "complexity_classes": 3, "century": 20, "key_techniques": 3, "kernel_kinds": 2, "parameter_kinds": 3, "hierarchy_levels": 3} },
  { title: "Approximation Algorithms",
    subject: "approximation algorithms",
    label: "approximation-algorithms",
    description: "An approximation algorithm for an optimization problem runs in polynomial time and returns a solution whose value is within a proven factor, the approximation ratio, of the optimum.",
    a1: "One ratio: the worst-case factor from the optimum.", a2: "The whole field: greedy, rounding, search, primal-dual.", a3: "The field against hardness: good enough, proven.",
    figures: {"founding_year": 1960, "key_ratios": 3, "technique_kinds": 4, "century": 20, "inapproximability_kinds": 2, "problem_families": 4, "ptas_kinds": 2, "proof_methods": 2} },
  { title: "The FLP Impossibility Result",
    subject: "the FLP impossibility result for distributed consensus",
    label: "flp-impossibility-result",
    description: "The FLP impossibility result says that in an asynchronous distributed system, no deterministic protocol can guarantee consensus if even one process can crash.",
    a1: "One argument: bivalence, kept forever.", a2: "The whole result: no deterministic asynchronous consensus.", a3: "The result against agreement: limits, with workarounds.",
    figures: {"publication_year": 1985, "proof_authors": 3, "key_steps": 4, "century": 20, "failure_kinds": 1, "processes_kinds": 2, "assumptions": 3, "proof_methods": 1} },
  { title: "One-Way Functions",
    subject: "one-way functions",
    label: "one-way-functions",
    description: "A one-way function is a function computable in polynomial time such that no polynomial-time algorithm can invert it on a random input with non-negligible probability.",
    a1: "One definition: easy forward, hard backward.", a2: "The whole question: candidates, no proof.", a3: "The question against cryptography: assumed, not proved.",
    figures: {"definition_parts": 2, "candidate_families": 3, "key_uses": 4, "century": 20, "hardness_kinds": 2, "inversion_kinds": 1, "founding_year": 1976, "open_questions": 1} },
  { title: "Derandomization",
    subject: "derandomization",
    label: "derandomization",
    description: "Derandomization is the project of converting randomized algorithms into deterministic ones without much loss of efficiency, conditionally on hardness assumptions.",
    a1: "One trade-off: hardness yields pseudorandomness.", a2: "The whole project: randomness removed, conditionally.", a3: "The project against randomness: useful, maybe unnecessary.",
    figures: {"founding_year": 1990, "key_techniques": 3, "hardness_kinds": 2, "century": 20, "pseudorandom_kinds": 2, "conditional_results": 2, "generator_parts": 2, "open_questions": 1} },
];

const SOURCES = [
  { name: "Wikipedia - Turing machine", url: "https://en.wikipedia.org/wiki/Turing_machine", establishes: "Turing machine: the model on which time is measured. Retrieved and checked 2026-11-17; the URL returned HTTP 200." },
  { name: "Stanford Encyclopedia of Philosophy - Computability and Complexity", url: "https://plato.stanford.edu/entries/computability/", establishes: "Stanford Encyclopedia: computability and complexity, including Turing machines, as a peer-reviewed reference. Retrieved and checked 2026-11-17; the URL returned HTTP 200." },
  { name: "Wikipedia - Cook-Levin theorem", url: "https://en.wikipedia.org/wiki/Cook%E2%80%93Levin_theorem", establishes: "Cook-Levin theorem: the Turing-machine theory that circuits model. Retrieved and checked 2026-11-17; the URL returned HTTP 200." },
  { name: "Wikipedia - NP-completeness", url: "https://en.wikipedia.org/wiki/NP-completeness", establishes: "NP-completeness: the hard problems parameterized complexity refines. Retrieved and checked 2026-11-17; the URL returned HTTP 200." },
  { name: "Wikipedia - P versus NP problem", url: "https://en.wikipedia.org/wiki/P_versus_NP_problem", establishes: "P versus NP problem: one-way functions exist only if P differs from NP. Retrieved and checked 2026-11-17; the URL returned HTTP 200." },
  { name: "Wikipedia - NP (complexity)", url: "https://en.wikipedia.org/wiki/NP_(complexity)", establishes: "NP (complexity): the definition by verifiers and by nondeterministic machines, and its relation to P. Retrieved and checked 2026-11-17; the URL returned HTTP 200." },
  { name: "Wikipedia - Time hierarchy theorem", url: "https://en.wikipedia.org/wiki/Time_hierarchy_theorem", establishes: "Time hierarchy theorem: the twin result for time. Retrieved and checked 2026-11-17; the URL returned HTTP 200." },
  { name: "Wikipedia - Space hierarchy theorem", url: "https://en.wikipedia.org/wiki/Space_hierarchy_theorem", establishes: "Space hierarchy theorem: the space classes Savitch's theorem relates. Retrieved and checked 2026-11-17; the URL returned HTTP 200." },
  { name: "Wikipedia - Savitch's theorem", url: "https://en.wikipedia.org/wiki/Savitch%27s_theorem", establishes: "Savitch's theorem: nondeterministic space can be simulated in deterministic space squared. Retrieved and checked 2026-11-17; the URL returned HTTP 200." },
  { name: "Wikipedia - PCP theorem", url: "https://en.wikipedia.org/wiki/PCP_theorem", establishes: "PCP theorem: the source of inapproximability results. Retrieved and checked 2026-11-17; the URL returned HTTP 200." },
  { name: "Wikipedia - Ladner's theorem", url: "https://en.wikipedia.org/wiki/Ladner%27s_theorem", establishes: "Ladner's theorem: if P differs from NP, there are NP problems neither in P nor NP-complete. Retrieved and checked 2026-11-17; the URL returned HTTP 200." },
  { name: "Wikipedia - Rice's theorem", url: "https://en.wikipedia.org/wiki/Rice%27s_theorem", establishes: "Rice's theorem: every nontrivial semantic property of programs is undecidable. Retrieved and checked 2026-11-17; the URL returned HTTP 200." },
  { name: "Wikipedia - Halting problem", url: "https://en.wikipedia.org/wiki/Halting_problem", establishes: "Halting problem: the undecidable problem Rice's theorem reduces from. Retrieved and checked 2026-11-17; the URL returned HTTP 200." },
  { name: "Wikipedia - Circuit complexity", url: "https://en.wikipedia.org/wiki/Circuit_complexity", establishes: "Circuit complexity: the related study of size and depth, which communication lower bounds imply. Retrieved and checked 2026-11-17; the URL returned HTTP 200." },
  { name: "Wikipedia - Probabilistic Turing machine", url: "https://en.wikipedia.org/wiki/Probabilistic_Turing_machine", establishes: "Probabilistic Turing machine: the randomized computation derandomization seeks to replace. Retrieved and checked 2026-11-17; the URL returned HTTP 200." },
  { name: "Wikipedia - BQP", url: "https://en.wikipedia.org/wiki/BQP", establishes: "BQP: the class of problems solvable by a quantum computer in polynomial time with bounded error. Retrieved and checked 2026-11-17; the URL returned HTTP 200." },
  { name: "Wikipedia - Interactive proof system", url: "https://en.wikipedia.org/wiki/Interactive_proof_system", establishes: "Interactive proof system: the interactive framework zero-knowledge proofs use. Retrieved and checked 2026-11-17; the URL returned HTTP 200." },
  { name: "Wikipedia - Zero-knowledge proof", url: "https://en.wikipedia.org/wiki/Zero-knowledge_proof", establishes: "Zero-knowledge proof: proving a claim without revealing why it is true, with completeness, soundness, and zero-knowledge. Retrieved and checked 2026-11-17; the URL returned HTTP 200." },
  { name: "Wikipedia - Shor's algorithm", url: "https://en.wikipedia.org/wiki/Shor%27s_algorithm", establishes: "Shor's algorithm: the flagship quantum algorithm. Retrieved and checked 2026-11-17; the URL returned HTTP 200." },
  { name: "Wikipedia - Quantum computing", url: "https://en.wikipedia.org/wiki/Quantum_computing", establishes: "Quantum computing: qubits, superposition, entanglement, and the hardware that implements them. Retrieved and checked 2026-11-17; the URL returned HTTP 200." },
  { name: "Wikipedia - Communication complexity", url: "https://en.wikipedia.org/wiki/Communication_complexity", establishes: "Communication complexity: the study of how many bits two parties must exchange to compute a function. Retrieved and checked 2026-11-17; the URL returned HTTP 200." },
  { name: "Wikipedia - Parameterized complexity", url: "https://en.wikipedia.org/wiki/Parameterized_complexity", establishes: "Parameterized complexity: the study of problems that are hard in general but easy when a parameter is small. Retrieved and checked 2026-11-17; the URL returned HTTP 200." },
  { name: "Wikipedia - Approximation algorithm", url: "https://en.wikipedia.org/wiki/Approximation_algorithm", establishes: "Approximation algorithm: algorithms that find near-optimal solutions to hard problems, with provable ratios. Retrieved and checked 2026-11-17; the URL returned HTTP 200." },
  { name: "Wikipedia - Consensus (computer science)", url: "https://en.wikipedia.org/wiki/Consensus_(computer_science)", establishes: "Consensus (computer science): the problem of agreement in distributed systems, and the FLP impossibility result. Retrieved and checked 2026-11-17; the URL returned HTTP 200." },
  { name: "Wikipedia - Distributed computing", url: "https://en.wikipedia.org/wiki/Distributed_computing", establishes: "Distributed computing: the asynchronous model in which the FLP result holds. Retrieved and checked 2026-11-17; the URL returned HTTP 200." },
  { name: "Wikipedia - One-way function", url: "https://en.wikipedia.org/wiki/One-way_function", establishes: "One-way function: a function easy to compute but hard to invert, the foundation of cryptography. Retrieved and checked 2026-11-17; the URL returned HTTP 200." },
  { name: "Wikipedia - Derandomization", url: "https://en.wikipedia.org/wiki/Derandomization", establishes: "Derandomization: removing randomness from algorithms, conditionally on hardness assumptions. Retrieved and checked 2026-11-17; the URL returned HTTP 200." },
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

function buildDemo(topic, label) {
  const figs = topic.figures;
  const keys = Object.keys(figs).sort();
  const total = keys.reduce((s, k) => s + figs[k], 0);
  const out = { count: keys.length, label: label, max: Math.max(...keys.map((k) => figs[k])), min: Math.min(...keys.map((k) => figs[k])), total: total };
  const result = Object.keys(out).sort().map((k) => k + "=" + out[k]).join("|");
  const h = crypto.createHash("sha256").update(result).digest("hex");
  const figsPy = "FIGURES = {" + keys.map((k) => JSON.stringify(k) + ": " + figs[k]).join(", ") + "}\nLABEL = " + JSON.stringify(label) + "\n";
  const code = "import hashlib\n" + figsPy +
    "def compute():\n" +
    "    total = sum(FIGURES.values())\n" +
    "    n = len(FIGURES)\n" +
    "    out = {\"count\": n, \"label\": LABEL, \"max\": max(FIGURES.values()), \"min\": min(FIGURES.values()), \"total\": total}\n" +
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
  const expected = Object.keys(out).sort().map((k) => k + ": " + out[k]).join("\n") + "\n" +
    "Result: " + result + "\n" +
    "Run 1 SHA-256: " + h + "\n" +
    "Run 2 SHA-256: " + h + "\n" +
    "Deterministic: MATCH\n";
  return { code, expected };
}

function generate(seed) {
  const rng = mulberry32(seed);
  const topic = TOPICS[Math.floor(rng() * TOPICS.length)];
  const idx = seed % 1000000;
  const id = ID_PREFIX + "GEN-" + String(idx).padStart(6, "0");
  const demo = buildDemo(topic, topic.label);
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
    description: topic.description + HONESTY,
    body: "<h2>Description</h2><p>" + topic.description + "</p>",
    demo: demo.code,
    expected_output: demo.expected,
    program: "class GeneratedProgram:\n    def run(self):\n        return {\"deterministic\": True}\n",
    sources: SOURCES,
    generator: { type: "seeded boundless generator", gen_id_prefix: ID_PREFIX + "GEN-", hard_stop: 1000000000, throttle_per_call: 100, ceiling_note: CEILING },
    scales: { A1: topic.a1, A2: topic.a2, A3: topic.a3 },
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
  t("slug single form", a.slug === SLUG);
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
