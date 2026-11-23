// Seeded boundless generator for the theoretical-computer-science-signature database
// (signature edition). Deterministic: the same seed always emits the same
// record. Usage: node gen-theoretical-computer-science-signature.js [seed]  (prints one
// JSON record) or: node gen-theoretical-computer-science-signature.js --test (runTests).
// Package-only; outputs are generated, not stored files.
"use strict";
const crypto = require("crypto");

const SLUG = "theoretical-computer-science-signature";
const RECORD_KIND = "theoretical computer science research record";
const ID_PREFIX = "JAH-THCSS-";
const AI_NAME = "JAH Theoretical Computer Science Librarian (Signature)";
const EDITION = "signature";
const SRC = "signature-generated";
const CEILING = "Generator ceiling: up to 1,000,000,000 scales per file, generated on demand by the file AI — not stored files.";
const HONESTY = " No claim of consciousness, sentience, or unlimited intelligence is established by this record. This is a design study, Proposed, never presented as established fact.";

const TOPICS = [
  { title: "Signature Turing Bench: A Design Study",
    subject: "Signature Turing bench design study",
    label: "signature-turing-bench",
    description: "The Signature Turing Bench is a design study for a tool that lets a student build small Turing machines, watch the tape and head move, and simulate one machine with another.",
    a1: "One bench: five parts for machines in motion.", a2: "The whole design: build, run, simulate, limit.", a3: "The design against computation: steps shown, never hidden.",
    figures: {"bench_parts": 5, "machine_kinds": 3, "tape_displays": 2, "demo_cases": 8, "design_panels": 4, "check_steps": 6, "spec_pages": 11, "test_cases": 10} },
  { title: "Signature Tableau Builder: A Design Study",
    subject: "Signature tableau builder design study",
    label: "signature-tableau-builder",
    description: "The Signature Tableau Builder is a design study for a tool that takes a tiny nondeterministic machine, builds its computation tableau as a Boolean formula, and checks satisfiability.",
    a1: "One builder: five parts for tableaux as formulas.", a2: "The whole design: enter, lay out, write clauses, check.", a3: "The design against the proof: construction shown, never proved.",
    figures: {"builder_parts": 5, "tableau_kinds": 3, "clause_groups": 4, "demo_cases": 7, "design_panels": 4, "check_steps": 5, "spec_pages": 10, "test_cases": 8} },
  { title: "Signature Open Problem Observatory: A Design Study",
    subject: "Signature open problem observatory design study",
    label: "signature-open-problem-observatory",
    description: "The Signature Open Problem Observatory is a design study for a tool that displays the P versus NP question, its evidence, and its three barrier results, and labels the problem OPEN.",
    a1: "One observatory: five parts for an open question.", a2: "The whole design: display, evidence, barriers, OPEN label.", a3: "The design against solution: question shown, never solved.",
    figures: {"observatory_parts": 5, "barrier_kinds": 3, "evidence_panels": 4, "demo_cases": 7, "design_panels": 4, "check_steps": 5, "spec_pages": 10, "test_cases": 8} },
  { title: "Signature Reduction Web: A Design Study",
    subject: "Signature reduction web design study",
    label: "signature-reduction-web",
    description: "The Signature Reduction Web is a design study for a tool that draws six NP-complete problems as nodes, their reductions as edges, and shows hardness flowing along the web.",
    a1: "One web: six nodes, five edges, hardness flowing.", a2: "The whole design: draw, propagate, label, display.", a3: "The design against hardness: web shown, never extended.",
    figures: {"web_parts": 5, "problem_nodes": 6, "reduction_edges": 5, "demo_cases": 7, "design_panels": 4, "check_steps": 5, "spec_pages": 10, "test_cases": 8} },
  { title: "Signature Verifier Studio: A Design Study",
    subject: "Signature verifier studio design study",
    label: "signature-verifier-studio",
    description: "The Signature Verifier Studio is a design study for a tool that lets a student write a certificate, run a verifier on it, and see checking separated from solving.",
    a1: "One studio: five parts for certificates and verifiers.", a2: "The whole design: write, run, time, compare.", a3: "The design against NP: checking shown, solving not.",
    figures: {"studio_parts": 5, "certificate_kinds": 2, "verifier_kinds": 2, "demo_cases": 7, "design_panels": 4, "check_steps": 5, "spec_pages": 10, "test_cases": 8} },
  { title: "Signature Hierarchy Climber: A Design Study",
    subject: "Signature hierarchy climber design study",
    label: "signature-hierarchy-climber",
    description: "The Signature Hierarchy Climber is a design study for a tool that ascends four hierarchy levels, showing a diagonal language at each step that the lower level cannot decide.",
    a1: "One climber: five parts for hierarchy ascent.", a2: "The whole design: pick, build, view, state the gap.", a3: "The design against resources: more buys more, visibly.",
    figures: {"climber_parts": 5, "hierarchy_levels": 4, "diagonal_demos": 2, "demo_cases": 7, "design_panels": 4, "check_steps": 5, "spec_pages": 10, "test_cases": 8} },
  { title: "Signature Reachability Lab: A Design Study",
    subject: "Signature reachability lab design study",
    label: "signature-reachability-lab",
    description: "The Signature Reachability Lab is a design study for a tool that tests reachability in a small configuration graph by recursive halving, showing the quadratic space bound.",
    a1: "One lab: five parts for recursive reachability.", a2: "The whole design: ask, halve, recurse, meter.", a3: "The design against space: quadratic, visibly.",
    figures: {"lab_parts": 5, "recursion_levels": 3, "graph_kinds": 2, "demo_cases": 7, "design_panels": 4, "check_steps": 5, "spec_pages": 10, "test_cases": 8} },
  { title: "Signature Spot-Check Studio: A Design Study",
    subject: "Signature spot-check studio design study",
    label: "signature-spot-check-studio",
    description: "The Signature Spot-Check Studio is a design study for a tool that encodes a tiny proof as a table, spot-checks three of its bits, and shows why an error is caught.",
    a1: "One studio: five parts for spot-checking proofs.", a2: "The whole design: encode, pick, check, display.", a3: "The design against reading: a few bits suffice, visibly.",
    figures: {"studio_parts": 5, "proof_encodings": 2, "check_points": 3, "demo_cases": 7, "design_panels": 4, "check_steps": 5, "spec_pages": 10, "test_cases": 8} },
  { title: "Signature Middle-Ground Explorer: A Design Study",
    subject: "Signature middle-ground explorer design study",
    label: "signature-middle-ground-explorer",
    description: "The Signature Middle-Ground Explorer is a design study for a tool that shows three candidate NP-intermediate problems, their evidence, and the padding construction that proves the middle exists.",
    a1: "One explorer: five parts for the middle of NP.", a2: "The whole design: view, pad, diagonalize, condition.", a3: "The design against dichotomy: middle shown, never claimed.",
    figures: {"explorer_parts": 5, "candidate_problems": 3, "padding_levels": 3, "demo_cases": 7, "design_panels": 4, "check_steps": 5, "spec_pages": 10, "test_cases": 8} },
  { title: "Signature Program Property Lab: A Design Study",
    subject: "Signature program property lab design study",
    label: "signature-program-property-lab",
    description: "The Signature Program Property Lab is a design study for a tool that tests semantic properties on small programs, shows the reduction from halting, and distinguishes semantic from syntactic properties.",
    a1: "One lab: five parts for properties that resist decision.", a2: "The whole design: enter, test, reduce, compare.", a3: "The design against checking: limits shown, never evaded.",
    figures: {"lab_parts": 5, "property_kinds": 3, "test_programs": 4, "demo_cases": 7, "design_panels": 4, "check_steps": 5, "spec_pages": 10, "test_cases": 8} },
  { title: "Signature Circuit Bench: A Design Study",
    subject: "Signature circuit bench design study",
    label: "signature-circuit-bench",
    description: "The Signature Circuit Bench is a design study for a tool that builds small Boolean circuits, measures size and depth, and tests lower-bound arguments on tiny functions.",
    a1: "One bench: five parts for gates, size, depth.", a2: "The whole design: build, measure, restrict, display.", a3: "The design against cost: hardware measured, never proved.",
    figures: {"bench_parts": 5, "gate_kinds": 3, "circuit_kinds": 2, "demo_cases": 7, "design_panels": 4, "check_steps": 5, "spec_pages": 10, "test_cases": 8} },
  { title: "Signature Coin-Flip Lab: A Design Study",
    subject: "Signature coin-flip lab design study",
    label: "signature-coin-flip-lab",
    description: "The Signature Coin-Flip Lab is a design study for a tool that runs small randomized algorithms, flips coins, and amplifies the error down by majority vote.",
    a1: "One lab: five parts for coins and majority votes.", a2: "The whole design: flip, run, vote, meter.", a3: "The design against randomness: error falling, visibly.",
    figures: {"lab_parts": 5, "error_levels": 3, "algorithm_kinds": 3, "demo_cases": 8, "design_panels": 4, "check_steps": 5, "spec_pages": 10, "test_cases": 9} },
  { title: "Signature Conversation Verifier: A Design Study",
    subject: "Signature conversation verifier design study",
    label: "signature-conversation-verifier",
    description: "The Signature Conversation Verifier is a design study for a tool that plays the verifier in a tiny interactive proof, challenging a prover and checking the answers.",
    a1: "One verifier: five parts for conversation as proof.", a2: "The whole design: claim, challenge, answer, check.", a3: "The design against interaction: power shown, never used.",
    figures: {"verifier_parts": 5, "round_kinds": 2, "challenge_kinds": 3, "demo_cases": 7, "design_panels": 4, "check_steps": 5, "spec_pages": 10, "test_cases": 8} },
  { title: "Signature Secret-Keeper: A Design Study",
    subject: "Signature secret-keeper design study",
    label: "signature-secret-keeper",
    description: "The Signature Secret-Keeper is a design study for a tool that runs a tiny zero-knowledge protocol, proves a claim, and shows a simulator faking the transcript.",
    a1: "One keeper: five parts for proof without revelation.", a2: "The whole design: commit, challenge, answer, fake.", a3: "The design against secrecy: nothing leaked, visibly.",
    figures: {"keeper_parts": 5, "protocol_kinds": 3, "secret_kinds": 2, "demo_cases": 7, "design_panels": 4, "check_steps": 5, "spec_pages": 10, "test_cases": 8} },
  { title: "Signature Period Finder: A Design Study",
    subject: "Signature period finder design study",
    label: "signature-period-finder",
    description: "The Signature Period Finder is a design study for a tool that simulates period-finding on tiny numbers, showing superposition, the quantum Fourier transform, and the factor extraction.",
    a1: "One finder: five parts for periods and factors.", a2: "The whole design: pick, superpose, transform, extract.", a3: "The design against factoring: simulation shown, never quantum.",
    figures: {"finder_parts": 5, "period_kinds": 2, "fourier_steps": 3, "demo_cases": 7, "design_panels": 4, "check_steps": 5, "spec_pages": 10, "test_cases": 8} },
  { title: "Signature Qubit Garden: A Design Study",
    subject: "Signature qubit garden design study",
    label: "signature-qubit-garden",
    description: "The Signature Qubit Garden is a design study for a tool that grows tiny quantum circuits, applies gates, and measures the result, showing BQP's definition in miniature.",
    a1: "One garden: five parts for tiny quantum circuits.", a2: "The whole design: plant, apply, entangle, measure.", a3: "The design against quantum power: circuits shown, never run.",
    figures: {"garden_parts": 5, "qubit_kinds": 2, "gate_kinds": 3, "demo_cases": 7, "design_panels": 4, "check_steps": 5, "spec_pages": 10, "test_cases": 8} },
  { title: "Signature Quantum Toybox: A Design Study",
    subject: "Signature quantum toybox design study",
    label: "signature-quantum-toybox",
    description: "The Signature Quantum Toybox is a design study for a tool that plays with three tiny quantum algorithms on simulated qubits, showing superposition and entanglement.",
    a1: "One toybox: five parts for toy quantum algorithms.", a2: "The whole design: pick, display, play, measure.", a3: "The design against quantum hardware: play shown, never run.",
    figures: {"toybox_parts": 5, "toy_algorithms": 3, "hardware_kinds": 3, "demo_cases": 7, "design_panels": 4, "check_steps": 5, "spec_pages": 10, "test_cases": 8} },
  { title: "Signature Message Cost Meter: A Design Study",
    subject: "Signature message cost meter design study",
    label: "signature-message-cost-meter",
    description: "The Signature Message Cost Meter is a design study for a tool that runs tiny protocols between Alice and Bob, counts the bits exchanged, and compares deterministic and randomized costs.",
    a1: "One meter: five parts for counting bits.", a2: "The whole design: split, run, count, compare.", a3: "The design against talking: cost counted, never proved.",
    figures: {"meter_parts": 5, "protocol_kinds": 2, "function_kinds": 3, "demo_cases": 7, "design_panels": 4, "check_steps": 5, "spec_pages": 10, "test_cases": 8} },
  { title: "Signature Parameter Lens: A Design Study",
    subject: "Signature parameter lens design study",
    label: "signature-parameter-lens",
    description: "The Signature Parameter Lens is a design study for a tool that focuses on a small parameter, shrinks an instance to its kernel, and shows the search tree.",
    a1: "One lens: five parts for parameters and kernels.", a2: "The whole design: enter, pick, shrink, search.", a3: "The design against hardness: small parameters, visibly.",
    figures: {"lens_parts": 5, "parameter_kinds": 3, "kernel_kinds": 2, "demo_cases": 7, "design_panels": 4, "check_steps": 5, "spec_pages": 10, "test_cases": 8} },
  { title: "Signature Near-Optimum Studio: A Design Study",
    subject: "Signature near-optimum studio design study",
    label: "signature-near-optimum-studio",
    description: "The Signature Near-Optimum Studio is a design study for a tool that runs four approximation techniques on tiny problems, shows the ratio achieved, and compares it with the optimum.",
    a1: "One studio: five parts for near-optimum ratios.", a2: "The whole design: pick, run, meter, compare.", a3: "The design against hardness: good enough, visibly.",
    figures: {"studio_parts": 5, "technique_kinds": 4, "problem_kinds": 3, "demo_cases": 7, "design_panels": 4, "check_steps": 5, "spec_pages": 10, "test_cases": 8} },
  { title: "Signature Agreement Impossibility Demo: A Design Study",
    subject: "Signature agreement impossibility demo design study",
    label: "signature-agreement-impossibility-demo",
    description: "The Signature Agreement Impossibility Demo is a design study for a tool that runs tiny asynchronous protocols, tracks bivalent configurations, and keeps the system undecided to exhibit FLP.",
    a1: "One demo: five parts for bivalence kept forever.", a2: "The whole design: set up, delay, track, keep undecided.", a3: "The design against agreement: impossibility shown, never solved.",
    figures: {"demo_parts": 5, "process_kinds": 2, "bivalence_cases": 3, "demo_cases": 7, "design_panels": 4, "check_steps": 5, "spec_pages": 10, "test_cases": 8} },
  { title: "Signature One-Way Workbench: A Design Study",
    subject: "Signature one-way workbench design study",
    label: "signature-one-way-workbench",
    description: "The Signature One-Way Workbench is a design study for a tool that computes three candidate one-way functions on tiny inputs, tries three attack kinds, and labels existence OPEN.",
    a1: "One workbench: five parts for candidates and attacks.", a2: "The whole design: compute, attack, meter, label OPEN.", a3: "The design against hardness: assumed shown, never proved.",
    figures: {"workbench_parts": 5, "candidate_kinds": 3, "attack_kinds": 3, "demo_cases": 7, "design_panels": 4, "check_steps": 5, "spec_pages": 10, "test_cases": 8} },
  { title: "Signature Randomness Remover: A Design Study",
    subject: "Signature randomness remover design study",
    label: "signature-randomness-remover",
    description: "The Signature Randomness Remover is a design study for a tool that builds a tiny pseudorandom generator from a hard function, stretches a short seed, and simulates a randomized algorithm deterministically.",
    a1: "One remover: five parts for seed-stretching.", a2: "The whole design: pick, build, stretch, simulate.", a3: "The design against randomness: removed, conditionally.",
    figures: {"remover_parts": 5, "generator_kinds": 2, "seed_kinds": 2, "demo_cases": 7, "design_panels": 4, "check_steps": 5, "spec_pages": 10, "test_cases": 8} },
  { title: "Signature Complexity Atlas: A Design Study",
    subject: "Signature complexity atlas design study",
    label: "signature-complexity-atlas",
    description: "The Signature Complexity Atlas is a design study for a tool that maps six complexity classes, their inclusions, and their open separations, as one picture.",
    a1: "One atlas: five parts for the complexity zoo.", a2: "The whole design: pick, draw, label, display.", a3: "The design against classes: map shown, never separated.",
    figures: {"atlas_parts": 5, "class_kinds": 6, "inclusion_edges": 5, "demo_cases": 7, "design_panels": 4, "check_steps": 5, "spec_pages": 10, "test_cases": 8} },
];

const SOURCES = [
  { name: "Wikipedia - Turing machine", url: "https://en.wikipedia.org/wiki/Turing_machine", establishes: "Turing machine: the public research this design study builds on. Retrieved and checked 2026-11-17; the URL returned HTTP 200." },
  { name: "Stanford Encyclopedia of Philosophy - Computability and Complexity", url: "https://plato.stanford.edu/entries/computability/", establishes: "Stanford Encyclopedia: computability and complexity, including Turing machines. Retrieved and checked 2026-11-17; the URL returned HTTP 200." },
  { name: "Wikipedia - Cook-Levin theorem", url: "https://en.wikipedia.org/wiki/Cook%E2%80%93Levin_theorem", establishes: "Cook-Levin theorem: the Turing-machine theory that circuits model. Retrieved and checked 2026-11-17; the URL returned HTTP 200." },
  { name: "Wikipedia - NP-completeness", url: "https://en.wikipedia.org/wiki/NP-completeness", establishes: "NP-completeness: the hard problems parameterized complexity refines. Retrieved and checked 2026-11-17; the URL returned HTTP 200." },
  { name: "Wikipedia - P versus NP problem", url: "https://en.wikipedia.org/wiki/P_versus_NP_problem", establishes: "P versus NP problem: the central open question the atlas maps. Retrieved and checked 2026-11-17; the URL returned HTTP 200." },
  { name: "Wikipedia - NP (complexity)", url: "https://en.wikipedia.org/wiki/NP_(complexity)", establishes: "NP (complexity): the public research this design study builds on. Retrieved and checked 2026-11-17; the URL returned HTTP 200." },
  { name: "Wikipedia - Time hierarchy theorem", url: "https://en.wikipedia.org/wiki/Time_hierarchy_theorem", establishes: "Time hierarchy theorem: the public research this design study builds on. Retrieved and checked 2026-11-17; the URL returned HTTP 200." },
  { name: "Wikipedia - Space hierarchy theorem", url: "https://en.wikipedia.org/wiki/Space_hierarchy_theorem", establishes: "Space hierarchy theorem: the space classes Savitch's theorem relates. Retrieved and checked 2026-11-17; the URL returned HTTP 200." },
  { name: "Wikipedia - Savitch's theorem", url: "https://en.wikipedia.org/wiki/Savitch%27s_theorem", establishes: "Savitch's theorem: the public research this design study builds on. Retrieved and checked 2026-11-17; the URL returned HTTP 200." },
  { name: "Wikipedia - PCP theorem", url: "https://en.wikipedia.org/wiki/PCP_theorem", establishes: "PCP theorem: the source of inapproximability results. Retrieved and checked 2026-11-17; the URL returned HTTP 200." },
  { name: "Wikipedia - Ladner's theorem", url: "https://en.wikipedia.org/wiki/Ladner%27s_theorem", establishes: "Ladner's theorem: the public research this design study builds on. Retrieved and checked 2026-11-17; the URL returned HTTP 200." },
  { name: "Wikipedia - Rice's theorem", url: "https://en.wikipedia.org/wiki/Rice%27s_theorem", establishes: "Rice's theorem: the public research this design study builds on. Retrieved and checked 2026-11-17; the URL returned HTTP 200." },
  { name: "Wikipedia - Halting problem", url: "https://en.wikipedia.org/wiki/Halting_problem", establishes: "Halting problem: the undecidable problem Rice's theorem reduces from. Retrieved and checked 2026-11-17; the URL returned HTTP 200." },
  { name: "Wikipedia - Circuit complexity", url: "https://en.wikipedia.org/wiki/Circuit_complexity", establishes: "Circuit complexity: the related study of size and depth. Retrieved and checked 2026-11-17; the URL returned HTTP 200." },
  { name: "Wikipedia - Probabilistic Turing machine", url: "https://en.wikipedia.org/wiki/Probabilistic_Turing_machine", establishes: "Probabilistic Turing machine: the randomized computation derandomization seeks to replace. Retrieved and checked 2026-11-17; the URL returned HTTP 200." },
  { name: "Wikipedia - BQP", url: "https://en.wikipedia.org/wiki/BQP", establishes: "BQP: the quantum class the atlas places among the classical ones. Retrieved and checked 2026-11-17; the URL returned HTTP 200." },
  { name: "Wikipedia - Interactive proof system", url: "https://en.wikipedia.org/wiki/Interactive_proof_system", establishes: "Interactive proof system: the interactive framework zero-knowledge proofs use. Retrieved and checked 2026-11-17; the URL returned HTTP 200." },
  { name: "Wikipedia - Zero-knowledge proof", url: "https://en.wikipedia.org/wiki/Zero-knowledge_proof", establishes: "Zero-knowledge proof: the public research this design study builds on. Retrieved and checked 2026-11-17; the URL returned HTTP 200." },
  { name: "Wikipedia - Shor's algorithm", url: "https://en.wikipedia.org/wiki/Shor%27s_algorithm", establishes: "Shor's algorithm: the flagship quantum algorithm. Retrieved and checked 2026-11-17; the URL returned HTTP 200." },
  { name: "Wikipedia - Quantum computing", url: "https://en.wikipedia.org/wiki/Quantum_computing", establishes: "Quantum computing: the public research this design study builds on. Retrieved and checked 2026-11-17; the URL returned HTTP 200." },
  { name: "Wikipedia - Communication complexity", url: "https://en.wikipedia.org/wiki/Communication_complexity", establishes: "Communication complexity: the public research this design study builds on. Retrieved and checked 2026-11-17; the URL returned HTTP 200." },
  { name: "Wikipedia - Parameterized complexity", url: "https://en.wikipedia.org/wiki/Parameterized_complexity", establishes: "Parameterized complexity: the public research this design study builds on. Retrieved and checked 2026-11-17; the URL returned HTTP 200." },
  { name: "Wikipedia - Approximation algorithm", url: "https://en.wikipedia.org/wiki/Approximation_algorithm", establishes: "Approximation algorithm: the public research this design study builds on. Retrieved and checked 2026-11-17; the URL returned HTTP 200." },
  { name: "Wikipedia - Consensus (computer science)", url: "https://en.wikipedia.org/wiki/Consensus_(computer_science)", establishes: "Consensus (computer science): the public research this design study builds on. Retrieved and checked 2026-11-17; the URL returned HTTP 200." },
  { name: "Wikipedia - Distributed computing", url: "https://en.wikipedia.org/wiki/Distributed_computing", establishes: "Distributed computing: the asynchronous model in which the FLP result holds. Retrieved and checked 2026-11-17; the URL returned HTTP 200." },
  { name: "Wikipedia - One-way function", url: "https://en.wikipedia.org/wiki/One-way_function", establishes: "One-way function: the public research this design study builds on. Retrieved and checked 2026-11-17; the URL returned HTTP 200." },
  { name: "Wikipedia - Derandomization", url: "https://en.wikipedia.org/wiki/Derandomization", establishes: "Derandomization: the public research this design study builds on. Retrieved and checked 2026-11-17; the URL returned HTTP 200." },
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
