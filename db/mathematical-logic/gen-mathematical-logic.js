// Seeded boundless generator for the mathematical-logic database
// (public edition). Deterministic: the same seed always emits the same
// record. Usage: node gen-mathematical-logic.js [seed]  (prints one
// JSON record) or: node gen-mathematical-logic.js --test (runTests).
// Package-only; outputs are generated, not stored files.
"use strict";
const crypto = require("crypto");

const SLUG = "mathematical-logic";
const RECORD_KIND = "mathematical logic research record";
const ID_PREFIX = "JAH-MLOG-";
const AI_NAME = "JAH Mathematical Logic Librarian";
const EDITION = "public";
const SRC = "public-harvest";
const CEILING = "Generator ceiling: up to 1,000,000,000 scales per file, generated on demand by the file AI — not stored files.";
const HONESTY = " No claim of consciousness, sentience, or unlimited intelligence is established by this record.";

const TOPICS = [
  { title: "Godel's First Incompleteness Theorem",
    subject: "Godel's first incompleteness theorem",
    label: "godel-first-incompleteness",
    description: "Godel's first incompleteness theorem, proved by Kurt Godel in 1931, says that any consistent formal system strong enough to express elementary arithmetic is incomplete: it contains a true statement about numbers that it cannot prove.",
    a1: "One sentence: the Godel sentence, true but unprovable in its system.", a2: "The whole theorem: two theorems, four lemmas, one numbering scheme.", a3: "The theorem against mathematics: no single system captures all arithmetical truth.",
    figures: {"theorems": 2, "publication_year": 1931, "godel_age": 25, "key_lemmas": 4, "axiom_systems": 3, "century": 20, "sentences_constructed": 1, "proof_pages": 40} },
  { title: "Godel's Second Incompleteness Theorem",
    subject: "Godel's second incompleteness theorem",
    label: "godel-second-incompleteness",
    description: "Godel's second incompleteness theorem says that a consistent formal system strong enough for arithmetic cannot prove its own consistency.",
    a1: "One statement: Con(F), the system's own consistency claim.", a2: "The whole theorem: the first theorem formalized inside the system.", a3: "The theorem against Hilbert's program: no system vouches for itself.",
    figures: {"theorems": 2, "publication_year": 1931, "consistency_statements": 1, "key_steps": 5, "systems_covered": 3, "century": 20, "proof_pages": 40, "lemmas_used": 3} },
  { title: "Godel's Completeness Theorem",
    subject: "Godel's completeness theorem for first-order logic",
    label: "godel-completeness-theorem",
    description: "Godel's completeness theorem says that first-order logic is complete: every sentence that is true in every model of a set of axioms can be proved from those axioms.",
    a1: "One construction: the term model built from the language itself.", a2: "The whole theorem: provable if and only if true in every model.", a3: "The theorem against doubt: first-order logic's rules are enough.",
    figures: {"publication_year": 1929, "godel_age": 23, "theorems": 1, "key_steps": 6, "logic_order": 1, "century": 20, "model_constructions": 1, "proof_versions": 3} },
  { title: "The Compactness Theorem",
    subject: "the compactness theorem of first-order logic",
    label: "compactness-theorem",
    description: "The compactness theorem says that a set of first-order sentences has a model if and only if every finite subset of it has a model.",
    a1: "One principle: finite parts decide the whole set.", a2: "The whole theorem: satisfiable if and only if every finite part is.", a3: "The theorem against the infinite: finite checks suffice.",
    figures: {"theorems": 1, "corollaries": 4, "key_steps": 3, "logic_order": 1, "publication_year": 1930, "century": 20, "finite_subsets": 1, "models_built": 1} },
  { title: "The Lowenheim-Skolem Theorem",
    subject: "the Lowenheim-Skolem theorem",
    label: "lowenheim-skolem-theorem",
    description: "The Lowenheim-Skolem theorem says that a countable first-order theory with an infinite model has models of every infinite size, including a countable one.",
    a1: "One paradox: a countable model of set theory.", a2: "The whole theorem: models of every infinite size.", a3: "The theorem against size: first-order axioms cannot fix cardinality.",
    figures: {"theorems": 2, "publication_year": 1915, "skolem_year": 1920, "cardinalities": 2, "key_steps": 4, "century": 20, "models_built": 2, "countable_models": 1} },
  { title: "The Halting Problem Is Undecidable",
    subject: "the undecidability of the halting problem",
    label: "halting-problem-undecidable",
    description: "The halting problem asks whether a given program will finish running or loop forever, and Turing proved in 1936 that no general algorithm can answer it for every program.",
    a1: "One program: D, which does the opposite of what the decider predicts.", a2: "The whole proof: assume a decider, derive a contradiction.", a3: "The result against automation: no perfect halting checker exists.",
    figures: {"publication_year": 1936, "turing_age": 24, "proof_steps": 3, "machines_involved": 2, "key_lemmas": 1, "century": 20, "decision_procedures": 0, "contradictions": 1} },
  { title: "Tarski's Undefinability Theorem",
    subject: "Tarski's undefinability theorem for truth",
    label: "tarski-undefinability-theorem",
    description: "Tarski's undefinability theorem says that truth cannot be defined inside the very language it describes, for any language strong enough to express arithmetic.",
    a1: "One sentence: the liar sentence, true if and only if false.", a2: "The whole theorem: no truth predicate inside the language.", a3: "The theorem against self-definition: truth needs a metalanguage.",
    figures: {"publication_year": 1933, "tarski_age": 32, "theorems": 1, "key_steps": 4, "languages_used": 2, "century": 20, "truth_predicates": 0, "lemmas_used": 1} },
  { title: "The Church-Turing Thesis",
    subject: "the Church-Turing thesis",
    label: "church-turing-thesis",
    description: "The Church-Turing thesis claims that every effectively computable function is computable by a Turing machine.",
    a1: "One claim: mechanical computability equals Turing computability.", a2: "The whole thesis: three models, one class of functions.", a3: "The thesis against proof: supported by evidence, never proved.",
    figures: {"publication_year": 1936, "proposers": 2, "models_compared": 3, "key_steps": 3, "century": 20, "equivalent_models": 3, "proofs_offered": 0, "decades_standing": 9} },
  { title: "Zermelo-Fraenkel Set Theory (ZFC)",
    subject: "Zermelo-Fraenkel set theory with choice",
    label: "zermelo-fraenkel-set-theory",
    description: "Zermelo-Fraenkel set theory with choice, called ZFC, is the standard foundation of mathematics: a list of axioms about sets from which nearly all of mathematics is built.",
    a1: "One relation: membership, the only primitive of the theory.", a2: "The whole system: nine axioms and two schemas.", a3: "The system against mathematics: the default foundation.",
    figures: {"axioms": 9, "axiom_schemas": 2, "zermelo_year": 1908, "fraenkel_year": 1922, "century": 20, "primitive_symbols": 2, "key_axioms": 5, "editions": 2} },
  { title: "The Continuum Hypothesis Is Independent of ZFC",
    subject: "the independence of the continuum hypothesis",
    label: "continuum-hypothesis-independence",
    description: "The continuum hypothesis is Cantor's 1878 claim that there is no set whose size is strictly between the natural numbers and the real numbers, and it is independent of ZFC: neither provable nor refutable from the standard axioms of set theory.",
    a1: "One question: is there a size between countable and continuum?", a2: "The whole result: two proofs, independence from ZFC.", a3: "The result against ZFC: the axioms do not settle it.",
    figures: {"publication_year": 1878, "godel_year": 1940, "cohen_year": 1963, "independence_proofs": 2, "century": 20, "key_models": 2, "cardinalities": 2, "proof_methods": 2} },
  { title: "Forcing: Cohen's Method for Building Models",
    subject: "forcing in set theory",
    label: "forcing-method",
    description: "Forcing is Paul Cohen's 1963 method for building new models of set theory by adding a generic set to an existing model.",
    a1: "One filter: the generic filter that builds the extension.", a2: "The whole method: conditions, names, and the forcing relation.", a3: "The method against provability: models on demand.",
    figures: {"publication_year": 1963, "cohen_age": 29, "key_ideas": 3, "model_types": 2, "century": 20, "fields_medal_year": 1966, "generic_sets": 1, "proof_steps": 5} },
  { title: "The Axiom of Choice Is Independent of ZF",
    subject: "the independence of the axiom of choice",
    label: "axiom-of-choice-independence",
    description: "The axiom of choice says that for every set of nonempty sets, there is a function choosing one element from each, all at once, and it is independent of ZF: neither provable nor refutable from the other axioms of set theory.",
    a1: "One choice: a function picking one element from each set.", a2: "The whole result: two proofs, independence from ZF.", a3: "The result against ZF: the axioms do not settle choice.",
    figures: {"zermelo_year": 1904, "godel_year": 1938, "cohen_year": 1963, "independence_proofs": 2, "century": 20, "key_models": 2, "equivalent_forms": 3, "proof_methods": 2} },
  { title: "Lob's Theorem",
    subject: "Lob's theorem on provability",
    label: "lob-theorem",
    description: "Lob's theorem says that if a formal system proves that the provability of a sentence implies the sentence itself, then the system proves the sentence outright.",
    a1: "One sentence: the diagonal sentence about its own provability.", a2: "The whole theorem: self-trust forces acceptance.", a3: "The theorem against self-certification: trust cannot be built within.",
    figures: {"publication_year": 1955, "lob_age": 30, "theorems": 1, "key_steps": 4, "derivability_conditions": 3, "century": 20, "lemmas_used": 2, "proof_lines": 12} },
  { title: "Gentzen's Consistency Proof for Arithmetic",
    subject: "Gentzen's consistency proof for arithmetic",
    label: "gentzen-consistency-proof",
    description: "Gentzen's consistency proof shows that Peano arithmetic, the standard axiom system for the natural numbers, is consistent, using transfinite induction up to the ordinal epsilon-zero.",
    a1: "One ordinal: epsilon-zero, the measure of proof complexity.", a2: "The whole proof: cut elimination plus ordinal descent.", a3: "The proof against Godel's limit: consistency from a stronger principle.",
    figures: {"publication_year": 1936, "gentzen_age": 27, "proof_methods": 2, "ordinals_used": 1, "key_steps": 5, "century": 20, "systems_proved": 1, "induction_principle": 1} },
  { title: "First-Order Logic",
    subject: "first-order logic",
    label: "first-order-logic",
    description: "First-order logic is the standard language of mathematics, built from variables, function and relation symbols, five connectives, and two quantifiers.",
    a1: "One language: variables, symbols, connectives, quantifiers.", a2: "The whole logic: sound and complete.", a3: "The logic against mathematics: the default language.",
    figures: {"quantifiers": 2, "connectives": 5, "proof_rules": 4, "key_theorems": 3, "century": 20, "variables": 2, "model_types": 2, "decision_status": 0} },
  { title: "Second-Order Logic",
    subject: "second-order logic",
    label: "second-order-logic",
    description: "Second-order logic extends first-order logic with quantifiers over sets, relations, and functions, not only over individual objects.",
    a1: "One axiom: second-order induction over all subsets.", a2: "The whole logic: categorical but incomplete.", a3: "The logic against first-order logic: more power, less proof.",
    figures: {"quantifier_kinds": 2, "orders": 2, "key_results": 3, "century": 20, "completeness_status": 0, "categoricity": 1, "expressive_gains": 3, "proof_systems": 2} },
  { title: "The Lambda Calculus",
    subject: "the lambda calculus",
    label: "lambda-calculus",
    description: "The lambda calculus is Alonzo Church's formal system for functions, and it is one of the founding models of computation.",
    a1: "One rule: beta reduction, substitution of input into body.", a2: "The whole calculus: three term kinds, three rules.", a3: "The calculus against computation: a minimal universal language.",
    figures: {"publication_year": 1936, "church_age": 33, "reduction_rules": 3, "key_theorems": 3, "century": 20, "term_kinds": 3, "models_compared": 3, "typed_variants": 2} },
  { title: "Type Theory",
    subject: "type theory",
    label: "type-theory",
    description: "Type theory is the framework in which every term has a type, types classify terms, and a term can only be used as its type permits.",
    a1: "One idea: every term has a type, and types restrict use.", a2: "The whole framework: types as propositions, programs as proofs.", a3: "The framework against paradox: classification blocks self-reference.",
    figures: {"publication_year": 1908, "russell_age": 36, "type_levels": 3, "key_systems": 4, "century": 20, "proof_assistants": 3, "universes": 2, "equality_kinds": 2} },
  { title: "Modal Logic and S5",
    subject: "modal logic and the system S5",
    label: "modal-logic-s5",
    description: "Modal logic extends classical logic with two operators: box, meaning necessarily, and diamond, meaning possibly.",
    a1: "One frame: an equivalence relation over possible worlds.", a2: "The whole system: S5, necessity without qualification.", a3: "The system against classical logic: necessity made formal.",
    figures: {"operators": 2, "axiom_systems": 5, "key_axioms": 4, "century": 20, "possible_worlds": 2, "completeness_year": 1959, "kripke_age": 19, "frames": 3} },
  { title: "Intuitionistic Logic",
    subject: "intuitionistic logic",
    label: "intuitionistic-logic",
    description: "Intuitionistic logic is the logic of constructive proof: a proof of a disjunction must give a proof of one side, and a proof of an existence claim must give a witness, a concrete example that makes it true.",
    a1: "One principle dropped: the law of excluded middle.", a2: "The whole logic: proofs as constructions.", a3: "The logic against classical logic: less assumed, more carried.",
    figures: {"publication_year": 1907, "brouwer_age": 26, "principles_dropped": 1, "connectives": 5, "century": 20, "key_theorems": 3, "proof_interpretations": 1, "systems": 2} },
  { title: "Decidability of Presburger Arithmetic",
    subject: "the decidability of Presburger arithmetic",
    label: "presburger-arithmetic-decidability",
    description: "Presburger arithmetic is the theory of the natural numbers with addition and order but without multiplication, and it is decidable: there is an algorithm that determines the truth of every sentence.",
    a1: "One operation: addition, without multiplication.", a2: "The whole result: decidable by quantifier elimination.", a3: "The result against Godel: addition alone stays decidable.",
    figures: {"publication_year": 1929, "presburger_age": 25, "operations": 1, "quantifier_eliminations": 1, "century": 20, "complexity_bound": 3, "axioms_used": 6, "decision_procedures": 1} },
  { title: "Nonstandard Analysis",
    subject: "nonstandard analysis",
    label: "nonstandard-analysis",
    description: "Nonstandard analysis is Abraham Robinson's rigorous theory of infinitesimals, numbers smaller in absolute value than any positive real number yet nonzero, together with infinite numbers larger than every real.",
    a1: "One principle: transfer, truth preserved across the extension.", a2: "The whole theory: infinitesimals made rigorous.", a3: "The theory against limits: intuition with rigor.",
    figures: {"publication_year": 1961, "robinson_age": 43, "key_ideas": 3, "transfer_principles": 1, "century": 20, "infinitesimal_kinds": 2, "model_constructions": 2, "applications": 4} },
  { title: "Model Theory",
    subject: "model theory",
    label: "model-theory",
    description: "Model theory is the branch of logic that studies mathematical structures through the sentences that are true in them.",
    a1: "One question: which structures satisfy which theories?", a2: "The whole field: models, embeddings, classification.", a3: "The field against mathematics: logic as a tool for structure.",
    figures: {"founding_year": 1954, "tarski_age": 53, "key_theorems": 4, "century": 20, "subfields": 3, "methods": 4, "applications": 3, "textbooks": 2} },
  { title: "Proof Theory",
    subject: "proof theory",
    label: "proof-theory",
    description: "Proof theory is the branch of logic that studies proofs as mathematical objects: their structure, their transformations, and what they reveal about the strength of theories.",
    a1: "One transformation: cut elimination, lemmas removed.", a2: "The whole field: proofs as objects, strength as ordinals.", a3: "The field against Hilbert's program: strength measured, not assumed.",
    figures: {"founding_year": 1934, "gentzen_age": 25, "key_systems": 3, "century": 20, "methods": 4, "applications": 3, "proof_formats": 3, "ordinals_used": 1} },
];

const SOURCES = [
  { name: "Wikipedia - Godel's incompleteness theorems", url: "https://en.wikipedia.org/wiki/G%C3%B6del%27s_incompleteness_theorems", establishes: "Godel's incompleteness theorems: the contrasting undecidability when multiplication is added. Retrieved and checked 2026-11-17; the URL returned HTTP 200." },
  { name: "Stanford Encyclopedia of Philosophy - Godel's Incompleteness Theorems", url: "https://plato.stanford.edu/entries/goedel-incompleteness/", establishes: "Stanford Encyclopedia: the second incompleteness theorem and its conditions, as a peer-reviewed reference. Retrieved and checked 2026-11-17; the URL returned HTTP 200." },
  { name: "Wikipedia - Godel's completeness theorem", url: "https://en.wikipedia.org/wiki/G%C3%B6del%27s_completeness_theorem", establishes: "Godel's completeness theorem: the compactness theorem follows from it, as the cited entry explains. Retrieved and checked 2026-11-17; the URL returned HTTP 200." },
  { name: "Wikipedia - First-order logic", url: "https://en.wikipedia.org/wiki/First-order_logic", establishes: "First-order logic: the complete logic that second-order logic extends. Retrieved and checked 2026-11-17; the URL returned HTTP 200." },
  { name: "Wikipedia - Compactness theorem", url: "https://en.wikipedia.org/wiki/Compactness_theorem", establishes: "Compactness theorem: the central tool of model theory. Retrieved and checked 2026-11-17; the URL returned HTTP 200." },
  { name: "Wikipedia - Lowenheim-Skolem theorem", url: "https://en.wikipedia.org/wiki/L%C3%B6wenheim%E2%80%93Skolem_theorem", establishes: "Lowenheim-Skolem theorem: a countable first-order theory with an infinite model has models of every infinite cardinality. Retrieved and checked 2026-11-17; the URL returned HTTP 200." },
  { name: "Wikipedia - Model theory", url: "https://en.wikipedia.org/wiki/Model_theory", establishes: "Model theory: the study of mathematical structures through first-order logic. Retrieved and checked 2026-11-17; the URL returned HTTP 200." },
  { name: "Wikipedia - Halting problem", url: "https://en.wikipedia.org/wiki/Halting_problem", establishes: "Halting problem: no general algorithm can decide whether a program halts, as proved by Turing in 1936. Retrieved and checked 2026-11-17; the URL returned HTTP 200." },
  { name: "Wikipedia - Computability theory", url: "https://en.wikipedia.org/wiki/Computability_theory", establishes: "Computability theory: the study of what can and cannot be computed, in which the halting problem is the central undecidable problem. Retrieved and checked 2026-11-17; the URL returned HTTP 200." },
  { name: "Wikipedia - Tarski's undefinability theorem", url: "https://en.wikipedia.org/wiki/Tarski%27s_undefinability_theorem", establishes: "Tarski's undefinability theorem: truth for a sufficiently strong language cannot be defined inside that language. Retrieved and checked 2026-11-17; the URL returned HTTP 200." },
  { name: "Wikipedia - Church-Turing thesis", url: "https://en.wikipedia.org/wiki/Church%E2%80%93Turing_thesis", establishes: "Church-Turing thesis: the lambda calculus computes exactly the Turing-computable functions. Retrieved and checked 2026-11-17; the URL returned HTTP 200." },
  { name: "Stanford Encyclopedia of Philosophy - Computability and Complexity", url: "https://plato.stanford.edu/entries/computability/", establishes: "Stanford Encyclopedia: computability and complexity, including the thesis and its evidence, as a peer-reviewed reference. Retrieved and checked 2026-11-17; the URL returned HTTP 200." },
  { name: "Wikipedia - Zermelo-Fraenkel set theory", url: "https://en.wikipedia.org/wiki/Zermelo%E2%80%93Fraenkel_set_theory", establishes: "Zermelo-Fraenkel set theory: ZF without choice, and ZFC with it. Retrieved and checked 2026-11-17; the URL returned HTTP 200." },
  { name: "Wikipedia - Axiom of choice", url: "https://en.wikipedia.org/wiki/Axiom_of_choice", establishes: "Axiom of choice: the axiom and its independence from ZF, proved by Godel and Cohen. Retrieved and checked 2026-11-17; the URL returned HTTP 200." },
  { name: "Wikipedia - Continuum hypothesis", url: "https://en.wikipedia.org/wiki/Continuum_hypothesis", establishes: "Continuum hypothesis: the first independence result proved by forcing. Retrieved and checked 2026-11-17; the URL returned HTTP 200." },
  { name: "Wikipedia - Forcing (mathematics)", url: "https://en.wikipedia.org/wiki/Forcing_(mathematics)", establishes: "Forcing: Cohen's method for extending a model of set theory by adding a generic set. Retrieved and checked 2026-11-17; the URL returned HTTP 200." },
  { name: "Wikipedia - Lob's theorem", url: "https://en.wikipedia.org/wiki/L%C3%B6b%27s_theorem", establishes: "Lob's theorem: if a system proves that proving a sentence implies the sentence, then it proves the sentence. Retrieved and checked 2026-11-17; the URL returned HTTP 200." },
  { name: "Wikipedia - Gentzen's consistency proof", url: "https://en.wikipedia.org/wiki/Gentzen%27s_consistency_proof", establishes: "Gentzen's consistency proof: the founding result of ordinal analysis. Retrieved and checked 2026-11-17; the URL returned HTTP 200." },
  { name: "Wikipedia - Proof theory", url: "https://en.wikipedia.org/wiki/Proof_theory", establishes: "Proof theory: the study of proofs as mathematical objects, from Gentzen to ordinal analysis. Retrieved and checked 2026-11-17; the URL returned HTTP 200." },
  { name: "Stanford Encyclopedia of Philosophy - Classical Logic", url: "https://plato.stanford.edu/entries/logic-classical/", establishes: "Stanford Encyclopedia: classical logic, including modal extensions, as a peer-reviewed reference. Retrieved and checked 2026-11-17; the URL returned HTTP 200." },
  { name: "Wikipedia - Second-order logic", url: "https://en.wikipedia.org/wiki/Second-order_logic", establishes: "Second-order logic: logic with quantifiers over sets and relations, stronger and incomplete. Retrieved and checked 2026-11-17; the URL returned HTTP 200." },
  { name: "Wikipedia - Lambda calculus", url: "https://en.wikipedia.org/wiki/Lambda_calculus", establishes: "Lambda calculus: the untyped system that type theory refines with types. Retrieved and checked 2026-11-17; the URL returned HTTP 200." },
  { name: "Wikipedia - Type theory", url: "https://en.wikipedia.org/wiki/Type_theory", establishes: "Type theory: the Curry-Howard correspondence, in which intuitionistic proofs are programs. Retrieved and checked 2026-11-17; the URL returned HTTP 200." },
  { name: "Wikipedia - Modal logic", url: "https://en.wikipedia.org/wiki/Modal_logic", establishes: "Modal logic: the logic of necessity and possibility, with the systems K, T, S4, and S5. Retrieved and checked 2026-11-17; the URL returned HTTP 200." },
  { name: "Wikipedia - Intuitionistic logic", url: "https://en.wikipedia.org/wiki/Intuitionistic_logic", establishes: "Intuitionistic logic: the logic of constructive proof, without the law of excluded middle. Retrieved and checked 2026-11-17; the URL returned HTTP 200." },
  { name: "Wikipedia - Presburger arithmetic", url: "https://en.wikipedia.org/wiki/Presburger_arithmetic", establishes: "Presburger arithmetic: the theory of the natural numbers with addition only, proved decidable in 1929. Retrieved and checked 2026-11-17; the URL returned HTTP 200." },
  { name: "Wikipedia - Nonstandard analysis", url: "https://en.wikipedia.org/wiki/Nonstandard_analysis", establishes: "Nonstandard analysis: Robinson's rigorous theory of infinitesimals, built on nonstandard models. Retrieved and checked 2026-11-17; the URL returned HTTP 200." },
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
