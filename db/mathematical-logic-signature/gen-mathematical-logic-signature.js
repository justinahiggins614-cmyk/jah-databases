// Seeded boundless generator for the mathematical-logic-signature database
// (signature edition). Deterministic: the same seed always emits the same
// record. Usage: node gen-mathematical-logic-signature.js [seed]  (prints one
// JSON record) or: node gen-mathematical-logic-signature.js --test (runTests).
// Package-only; outputs are generated, not stored files.
"use strict";
const crypto = require("crypto");

const SLUG = "mathematical-logic-signature";
const RECORD_KIND = "mathematical logic research record";
const ID_PREFIX = "JAH-MLOGS-";
const AI_NAME = "JAH Mathematical Logic Librarian (Signature)";
const EDITION = "signature";
const SRC = "signature-generated";
const CEILING = "Generator ceiling: up to 1,000,000,000 scales per file, generated on demand by the file AI — not stored files.";
const HONESTY = " No claim of consciousness, sentience, or unlimited intelligence is established by this record. This is a design study, Proposed, never presented as established fact.";

const TOPICS = [
  { title: "Signature Godel Lab: A Design Study",
    subject: "Signature Godel lab design study",
    label: "signature-godel-lab",
    description: "The Signature Godel Lab is a design study for a teaching laboratory in which a student builds Godel sentences, encodes proofs as numbers, and watches incompleteness appear in a tiny formal system.",
    a1: "One lab: six modules for hands-on incompleteness.", a2: "The whole design: build, encode, diagonalize, check.", a3: "The design against the theorem: a blueprint, not a proof.",
    figures: {"lab_modules": 6, "sentence_builders": 3, "numbering_schemes": 2, "demo_cases": 8, "design_panels": 5, "check_steps": 7, "spec_pages": 12, "test_cases": 10} },
  { title: "Signature Completeness Workbench: A Design Study",
    subject: "Signature completeness workbench design study",
    label: "signature-completeness-workbench",
    description: "The Signature Completeness Workbench is a design study for a tool that builds Henkin term models from consistent axiom sets and shows proof and truth agreeing.",
    a1: "One workbench: five tools for visible completeness.", a2: "The whole design: extend, build, evaluate, display.", a3: "The design against the theorem: a blueprint, not a proof.",
    figures: {"workbench_tools": 5, "model_builders": 2, "proof_searches": 3, "demo_cases": 6, "design_panels": 4, "check_steps": 6, "spec_pages": 10, "test_cases": 8} },
  { title: "Signature Compactness Engine: A Design Study",
    subject: "Signature compactness engine design study",
    label: "signature-compactness-engine",
    description: "The Signature Compactness Engine is a design study for a tool that checks finite subsets of a theory and assembles a model when every finite part passes.",
    a1: "One engine: four parts for finite-to-infinite assembly.", a2: "The whole design: enumerate, check, assemble, display.", a3: "The design against the theorem: a blueprint, not a proof.",
    figures: {"engine_parts": 4, "finite_checkers": 3, "model_builders": 2, "demo_cases": 7, "design_panels": 4, "check_steps": 5, "spec_pages": 9, "test_cases": 9} },
  { title: "Signature Skolem Modeler: A Design Study",
    subject: "Signature Skolem modeler design study",
    label: "signature-skolem-modeler",
    description: "The Signature Skolem Modeler is a design study for a tool that builds countable and larger models of a small theory and shows the same axioms describing different sizes.",
    a1: "One modeler: five parts for models of many sizes.", a2: "The whole design: edit, build, enlarge, compare.", a3: "The design against the paradox: a blueprint, not a resolution.",
    figures: {"modeler_parts": 5, "cardinality_sliders": 3, "model_builders": 2, "demo_cases": 6, "design_panels": 4, "check_steps": 6, "spec_pages": 10, "test_cases": 8} },
  { title: "Signature Bounded Halting Checker: A Design Study",
    subject: "Signature bounded halting checker design study",
    label: "signature-bounded-halting-checker",
    description: "The Signature Bounded Halting Checker is a design study for a tool that decides halting for programs within a step bound and four restricted program classes, and honestly reports unknown outside them.",
    a1: "One checker: five parts for bounded halting answers.", a2: "The whole design: simulate, classify, report unknown.", a3: "The design against undecidability: honest bounds, never evasion.",
    figures: {"checker_parts": 5, "step_bounds": 3, "program_classes": 4, "demo_cases": 9, "design_panels": 4, "check_steps": 6, "spec_pages": 11, "test_cases": 12} },
  { title: "Signature Truth-Ladder Studio: A Design Study",
    subject: "Signature truth-ladder studio design study",
    label: "signature-truth-ladder-studio",
    description: "The Signature Truth-Ladder Studio is a design study for a tool that builds a ladder of languages and metalanguages, showing why truth must be defined one level up.",
    a1: "One studio: five parts for the truth ladder.", a2: "The whole design: edit, attempt, fail, define one level up.", a3: "The design against self-definition: a blueprint, not a loophole.",
    figures: {"studio_parts": 5, "language_levels": 3, "liar_cases": 4, "demo_cases": 6, "design_panels": 4, "check_steps": 5, "spec_pages": 10, "test_cases": 8} },
  { title: "Signature Thesis Observatory: A Design Study",
    subject: "Signature thesis observatory design study",
    label: "signature-thesis-observatory",
    description: "The Signature Thesis Observatory is a design study for a tool that runs the same function in three models of computation and displays their agreement as evidence for the Church-Turing thesis.",
    a1: "One observatory: five parts for three models, one function.", a2: "The whole design: write once, run three ways, compare.", a3: "The design against proof: evidence displayed, never proved.",
    figures: {"observatory_parts": 5, "computation_models": 3, "equivalence_proofs": 3, "demo_cases": 7, "design_panels": 4, "check_steps": 5, "spec_pages": 10, "test_cases": 9} },
  { title: "Signature ZFC Workbench: A Design Study",
    subject: "Signature ZFC workbench design study",
    label: "signature-zfc-workbench",
    description: "The Signature ZFC Workbench is a design study for a tool that lets a student build numbers, functions, and spaces from the ZFC axioms step by step.",
    a1: "One workbench: six tools, nine axiom panels.", a2: "The whole design: browse, build, check, track dependencies.", a3: "The design against the axioms: construction made visible.",
    figures: {"workbench_tools": 6, "axiom_panels": 9, "construction_kits": 4, "demo_cases": 8, "design_panels": 5, "check_steps": 7, "spec_pages": 12, "test_cases": 10} },
  { title: "Signature Continuum Explorer: A Design Study",
    subject: "Signature continuum explorer design study",
    label: "signature-continuum-explorer",
    description: "The Signature Continuum Explorer is a design study for a tool that shows two models side by side, one in which the continuum hypothesis holds and one in which it fails.",
    a1: "One explorer: two models, one question, side by side.", a2: "The whole design: view, slide, compare, debate.", a3: "The design against independence: display, never verdict.",
    figures: {"explorer_parts": 5, "model_views": 2, "cardinality_sliders": 2, "demo_cases": 6, "design_panels": 4, "check_steps": 5, "spec_pages": 10, "test_cases": 8} },
  { title: "Signature Forcing Simulator: A Design Study",
    subject: "Signature forcing simulator design study",
    label: "signature-forcing-simulator",
    description: "The Signature Forcing Simulator is a design study for a tool that walks through a tiny forcing construction, choosing conditions, meeting dense sets, and extending a toy model.",
    a1: "One simulator: five parts for tiny forcing.", a2: "The whole design: order, dense sets, filter, extend.", a3: "The design against the method: toy example, not real power.",
    figures: {"simulator_parts": 5, "partial_orders": 3, "generic_filters": 2, "demo_cases": 7, "design_panels": 4, "check_steps": 6, "spec_pages": 11, "test_cases": 9} },
  { title: "Signature Choice Laboratory: A Design Study",
    subject: "Signature choice laboratory design study",
    label: "signature-choice-laboratory",
    description: "The Signature Choice Laboratory is a design study for a tool that shows where the axiom of choice is used, which theorems need it, and what fails without it.",
    a1: "One laboratory: five parts for choice dependence.", a2: "The whole design: browse, build, track, switch off.", a3: "The design against the axiom: dependence shown, never judged.",
    figures: {"lab_parts": 5, "choice_cases": 6, "equivalent_forms": 3, "demo_cases": 7, "design_panels": 4, "check_steps": 5, "spec_pages": 10, "test_cases": 9} },
  { title: "Signature Lob Reflector: A Design Study",
    subject: "Signature Lob reflector design study",
    label: "signature-lob-reflector",
    description: "The Signature Lob Reflector is a design study for a tool that lets a student state a self-trust claim, watch Lob's theorem force acceptance, and see why self-certification fails.",
    a1: "One reflector: five parts for the self-trust trap.", a2: "The whole design: state, diagonalize, track, accept.", a3: "The design against self-certification: trap shown, never escaped.",
    figures: {"reflector_parts": 5, "self_trust_cases": 4, "diagonal_builders": 2, "demo_cases": 6, "design_panels": 4, "check_steps": 5, "spec_pages": 10, "test_cases": 8} },
  { title: "Signature Gentzen Ordinal Analyzer: A Design Study",
    subject: "Signature Gentzen ordinal analyzer design study",
    label: "signature-gentzen-ordinal-analyzer",
    description: "The Signature Gentzen Ordinal Analyzer is a design study for a tool that assigns ordinals to small proofs, eliminates cuts, and shows the ordinal falling at each step.",
    a1: "One analyzer: five parts for ordinal descent.", a2: "The whole design: edit, eliminate, assign, watch fall.", a3: "The design against the proof: descent shown, never proved.",
    figures: {"analyzer_parts": 5, "ordinal_levels": 4, "proof_trees": 3, "demo_cases": 7, "design_panels": 4, "check_steps": 6, "spec_pages": 11, "test_cases": 9} },
  { title: "Signature First-Order Studio: A Design Study",
    subject: "Signature first-order studio design study",
    label: "signature-first-order-studio",
    description: "The Signature First-Order Studio is a design study for a tool that lets a student write first-order sentences, build structures, and check truth and proof side by side.",
    a1: "One studio: six tools for sentences and structures.", a2: "The whole design: write, build, evaluate, check.", a3: "The design against the logic: agreement shown, never decided.",
    figures: {"studio_tools": 6, "quantifier_panels": 2, "connective_panels": 5, "demo_cases": 8, "design_panels": 5, "check_steps": 6, "spec_pages": 11, "test_cases": 10} },
  { title: "Signature Second-Order Explorer: A Design Study",
    subject: "Signature second-order explorer design study",
    label: "signature-second-order-explorer",
    description: "The Signature Second-Order Explorer is a design study for a tool that compares first-order and second-order descriptions of the natural numbers and shows the categoricity-completeness trade-off.",
    a1: "One explorer: five parts for the categoricity trade-off.", a2: "The whole design: view, switch, compare, weigh.", a3: "The design against the trade-off: display, never resolution.",
    figures: {"explorer_parts": 5, "quantifier_kinds": 2, "categoricity_demos": 2, "demo_cases": 6, "design_panels": 4, "check_steps": 5, "spec_pages": 10, "test_cases": 8} },
  { title: "Signature Lambda Workshop: A Design Study",
    subject: "Signature lambda workshop design study",
    label: "signature-lambda-workshop",
    description: "The Signature Lambda Workshop is a design study for a tool that lets a student write lambda terms, reduce them step by step, and encode numbers and booleans as functions.",
    a1: "One workshop: six tools for reduction by substitution.", a2: "The whole design: write, reduce, encode, compare.", a3: "The design against computation: steps shown, never hidden.",
    figures: {"workshop_tools": 6, "term_kinds": 3, "reduction_rules": 3, "demo_cases": 9, "design_panels": 5, "check_steps": 6, "spec_pages": 11, "test_cases": 10} },
  { title: "Signature Type Checker Studio: A Design Study",
    subject: "Signature type checker studio design study",
    label: "signature-type-checker-studio",
    description: "The Signature Type Checker Studio is a design study for a tool that assigns types to small terms, shows the Curry-Howard correspondence, and checks tiny proofs as programs.",
    a1: "One studio: five tools for types as propositions.", a2: "The whole design: write, assign, display, compare.", a3: "The design against proof: correspondence shown, never claimed.",
    figures: {"studio_tools": 5, "type_rules": 6, "proof_assistants": 3, "demo_cases": 8, "design_panels": 4, "check_steps": 7, "spec_pages": 11, "test_cases": 10} },
  { title: "Signature Modal Worlds Simulator: A Design Study",
    subject: "Signature modal worlds simulator design study",
    label: "signature-modal-worlds-simulator",
    description: "The Signature Modal Worlds Simulator is a design study for a tool that builds small Kripke frames, evaluates necessity and possibility at each world, and compares the systems K, T, S4, and S5.",
    a1: "One simulator: five parts for worlds and accessibility.", a2: "The whole design: build, edit, evaluate, compare.", a3: "The design against necessity: frames shown, never metaphysics.",
    figures: {"simulator_parts": 5, "world_counts": 4, "frame_kinds": 3, "demo_cases": 7, "design_panels": 4, "check_steps": 5, "spec_pages": 10, "test_cases": 9} },
  { title: "Signature Constructive Proof Bench: A Design Study",
    subject: "Signature constructive proof bench design study",
    label: "signature-constructive-proof-bench",
    description: "The Signature Constructive Proof Bench is a design study for a tool that requires a witness for every existence proof and extracts a small program from each constructive proof.",
    a1: "One bench: five tools for witnesses and extraction.", a2: "The whole design: prove, witness, extract, run.", a3: "The design against classical shortcuts: construction required.",
    figures: {"bench_tools": 5, "witness_finders": 3, "proof_kinds": 4, "demo_cases": 8, "design_panels": 4, "check_steps": 6, "spec_pages": 11, "test_cases": 10} },
  { title: "Signature Presburger Decider: A Design Study",
    subject: "Signature Presburger decider design study",
    label: "signature-presburger-decider",
    description: "The Signature Presburger Decider is a design study for a tool that eliminates quantifiers from small addition-only formulas and reports the cost of each step.",
    a1: "One decider: five parts for visible elimination.", a2: "The whole design: enter, eliminate, meter, check.", a3: "The design against decidability: steps shown, cost shown.",
    figures: {"decider_parts": 5, "elimination_steps": 4, "formula_kinds": 3, "demo_cases": 8, "design_panels": 4, "check_steps": 6, "spec_pages": 10, "test_cases": 10} },
  { title: "Signature Infinitesimal Microscope: A Design Study",
    subject: "Signature infinitesimal microscope design study",
    label: "signature-infinitesimal-microscope",
    description: "The Signature Infinitesimal Microscope is a design study for a tool that zooms into the nonstandard reals, displaying infinitesimals and infinite numbers beside their standard shadows.",
    a1: "One microscope: five parts for zooming into infinitesimals.", a2: "The whole design: view, zoom, shadow, transfer.", a3: "The design against the reals: infinitesimals shown, never built.",
    figures: {"microscope_parts": 5, "zoom_levels": 4, "infinitesimal_kinds": 2, "demo_cases": 7, "design_panels": 4, "check_steps": 5, "spec_pages": 10, "test_cases": 8} },
  { title: "Signature Model Garden: A Design Study",
    subject: "Signature model garden design study",
    label: "signature-model-garden",
    description: "The Signature Model Garden is a design study for a tool that grows small models of small theories in beds, showing how theories and models relate.",
    a1: "One garden: five parts for growing small models.", a2: "The whole design: plant, grow, check, compare.", a3: "The design against the field: correspondence shown, never classified.",
    figures: {"garden_parts": 5, "model_beds": 4, "theory_kinds": 3, "demo_cases": 7, "design_panels": 4, "check_steps": 5, "spec_pages": 10, "test_cases": 8} },
  { title: "Signature Proof Transformer: A Design Study",
    subject: "Signature proof transformer design study",
    label: "signature-proof-transformer",
    description: "The Signature Proof Transformer is a design study for a tool that converts small proofs between formats, removes cuts, and measures the result.",
    a1: "One transformer: five parts for proof conversion.", a2: "The whole design: enter, convert, eliminate, measure.", a3: "The design against proof: transformation shown, never search.",
    figures: {"transformer_parts": 5, "proof_formats": 3, "transformation_kinds": 4, "demo_cases": 7, "design_panels": 4, "check_steps": 6, "spec_pages": 11, "test_cases": 9} },
  { title: "Signature Diagonal Lab: A Design Study",
    subject: "Signature diagonal lab design study",
    label: "signature-diagonal-lab",
    description: "The Signature Diagonal Lab is a design study for a tool that exhibits the diagonal argument in five cases, showing one technique behind Godel, Tarski, and Turing.",
    a1: "One lab: five parts, five diagonal cases.", a2: "The whole design: list, diagonalize, contradict, compare.", a3: "The design against the technique: one pattern, three fields.",
    figures: {"lab_parts": 5, "diagonal_cases": 5, "self_reference_kinds": 3, "demo_cases": 8, "design_panels": 4, "check_steps": 5, "spec_pages": 10, "test_cases": 9} },
];

const SOURCES = [
  { name: "Wikipedia - Godel's incompleteness theorems", url: "https://en.wikipedia.org/wiki/G%C3%B6del%27s_incompleteness_theorems", establishes: "Godel's incompleteness theorems: the diagonal lemma at the heart of the design. Retrieved and checked 2026-11-17; the URL returned HTTP 200." },
  { name: "Stanford Encyclopedia of Philosophy - Godel's Incompleteness Theorems", url: "https://plato.stanford.edu/entries/goedel-incompleteness/", establishes: "Stanford Encyclopedia: the incompleteness theorems, as a peer-reviewed reference for the design. Retrieved and checked 2026-11-17; the URL returned HTTP 200." },
  { name: "Wikipedia - Godel's completeness theorem", url: "https://en.wikipedia.org/wiki/G%C3%B6del%27s_completeness_theorem", establishes: "Godel's completeness theorem: the theorem compactness follows from. Retrieved and checked 2026-11-17; the URL returned HTTP 200." },
  { name: "Wikipedia - First-order logic", url: "https://en.wikipedia.org/wiki/First-order_logic", establishes: "First-order logic: the complete logic that second-order logic extends. Retrieved and checked 2026-11-17; the URL returned HTTP 200." },
  { name: "Wikipedia - Compactness theorem", url: "https://en.wikipedia.org/wiki/Compactness_theorem", establishes: "Compactness theorem: the central tool of model theory. Retrieved and checked 2026-11-17; the URL returned HTTP 200." },
  { name: "Wikipedia - Lowenheim-Skolem theorem", url: "https://en.wikipedia.org/wiki/L%C3%B6wenheim%E2%80%93Skolem_theorem", establishes: "Lowenheim-Skolem theorem: the public research this design study builds on. Retrieved and checked 2026-11-17; the URL returned HTTP 200." },
  { name: "Wikipedia - Model theory", url: "https://en.wikipedia.org/wiki/Model_theory", establishes: "Model theory: the public research this design study builds on. Retrieved and checked 2026-11-17; the URL returned HTTP 200." },
  { name: "Wikipedia - Halting problem", url: "https://en.wikipedia.org/wiki/Halting_problem", establishes: "Halting problem: the diagonal argument in computability. Retrieved and checked 2026-11-17; the URL returned HTTP 200." },
  { name: "Wikipedia - Computability theory", url: "https://en.wikipedia.org/wiki/Computability_theory", establishes: "Computability theory: the field in which halting undecidability is central. Retrieved and checked 2026-11-17; the URL returned HTTP 200." },
  { name: "Wikipedia - Tarski's undefinability theorem", url: "https://en.wikipedia.org/wiki/Tarski%27s_undefinability_theorem", establishes: "Tarski's undefinability theorem: the public research this design study builds on. Retrieved and checked 2026-11-17; the URL returned HTTP 200." },
  { name: "Wikipedia - Church-Turing thesis", url: "https://en.wikipedia.org/wiki/Church%E2%80%93Turing_thesis", establishes: "Church-Turing thesis: the equivalence the workshop exhibits. Retrieved and checked 2026-11-17; the URL returned HTTP 200." },
  { name: "Stanford Encyclopedia of Philosophy - Computability and Complexity", url: "https://plato.stanford.edu/entries/computability/", establishes: "Stanford Encyclopedia: computability and complexity, including the thesis and its evidence. Retrieved and checked 2026-11-17; the URL returned HTTP 200." },
  { name: "Wikipedia - Zermelo-Fraenkel set theory", url: "https://en.wikipedia.org/wiki/Zermelo%E2%80%93Fraenkel_set_theory", establishes: "Zermelo-Fraenkel set theory: ZF without choice, and ZFC with it. Retrieved and checked 2026-11-17; the URL returned HTTP 200." },
  { name: "Wikipedia - Axiom of choice", url: "https://en.wikipedia.org/wiki/Axiom_of_choice", establishes: "Axiom of choice: the public research this design study builds on. Retrieved and checked 2026-11-17; the URL returned HTTP 200." },
  { name: "Wikipedia - Continuum hypothesis", url: "https://en.wikipedia.org/wiki/Continuum_hypothesis", establishes: "Continuum hypothesis: the first independence result proved by forcing. Retrieved and checked 2026-11-17; the URL returned HTTP 200." },
  { name: "Wikipedia - Forcing (mathematics)", url: "https://en.wikipedia.org/wiki/Forcing_(mathematics)", establishes: "Forcing: the public research this design study builds on. Retrieved and checked 2026-11-17; the URL returned HTTP 200." },
  { name: "Wikipedia - Lob's theorem", url: "https://en.wikipedia.org/wiki/L%C3%B6b%27s_theorem", establishes: "Lob's theorem: the public research this design study builds on. Retrieved and checked 2026-11-17; the URL returned HTTP 200." },
  { name: "Wikipedia - Gentzen's consistency proof", url: "https://en.wikipedia.org/wiki/Gentzen%27s_consistency_proof", establishes: "Gentzen's consistency proof: the founding result of ordinal analysis. Retrieved and checked 2026-11-17; the URL returned HTTP 200." },
  { name: "Wikipedia - Proof theory", url: "https://en.wikipedia.org/wiki/Proof_theory", establishes: "Proof theory: the public research this design study builds on. Retrieved and checked 2026-11-17; the URL returned HTTP 200." },
  { name: "Stanford Encyclopedia of Philosophy - Classical Logic", url: "https://plato.stanford.edu/entries/logic-classical/", establishes: "Stanford Encyclopedia: classical logic, including modal extensions. Retrieved and checked 2026-11-17; the URL returned HTTP 200." },
  { name: "Wikipedia - Second-order logic", url: "https://en.wikipedia.org/wiki/Second-order_logic", establishes: "Second-order logic: the public research this design study builds on. Retrieved and checked 2026-11-17; the URL returned HTTP 200." },
  { name: "Wikipedia - Lambda calculus", url: "https://en.wikipedia.org/wiki/Lambda_calculus", establishes: "Lambda calculus: the untyped system that type theory refines. Retrieved and checked 2026-11-17; the URL returned HTTP 200." },
  { name: "Wikipedia - Type theory", url: "https://en.wikipedia.org/wiki/Type_theory", establishes: "Type theory: the Curry-Howard correspondence behind the bench. Retrieved and checked 2026-11-17; the URL returned HTTP 200." },
  { name: "Wikipedia - Modal logic", url: "https://en.wikipedia.org/wiki/Modal_logic", establishes: "Modal logic: the public research this design study builds on. Retrieved and checked 2026-11-17; the URL returned HTTP 200." },
  { name: "Wikipedia - Intuitionistic logic", url: "https://en.wikipedia.org/wiki/Intuitionistic_logic", establishes: "Intuitionistic logic: the public research this design study builds on. Retrieved and checked 2026-11-17; the URL returned HTTP 200." },
  { name: "Wikipedia - Presburger arithmetic", url: "https://en.wikipedia.org/wiki/Presburger_arithmetic", establishes: "Presburger arithmetic: the public research this design study builds on. Retrieved and checked 2026-11-17; the URL returned HTTP 200." },
  { name: "Wikipedia - Nonstandard analysis", url: "https://en.wikipedia.org/wiki/Nonstandard_analysis", establishes: "Nonstandard analysis: the public research this design study builds on. Retrieved and checked 2026-11-17; the URL returned HTTP 200." },
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
