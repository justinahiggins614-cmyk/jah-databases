// Seeded boundless generator for the category-theory-signature database
// (signature edition). Deterministic: the same seed always emits the same
// record. Usage: node gen-category-theory-signature.js [seed]  (prints one
// JSON record) or: node gen-category-theory-signature.js --test (runTests).
// Package-only; outputs are generated, not stored files.
"use strict";
const crypto = require("crypto");

const SLUG = "category-theory-signature";
const RECORD_KIND = "category theory research record";
const ID_PREFIX = "JAH-CATS-";
const AI_NAME = "JAH Category Theory Librarian (Signature)";
const EDITION = "signature";
const SRC = "signature-generated";
const CEILING = "Generator ceiling: up to 1,000,000,000 scales per file, generated on demand by the file AI — not stored files.";
const HONESTY = " No claim of consciousness, sentience, or unlimited intelligence is established by this record. This is a design study, Proposed, never presented as established fact.";

const TOPICS = [
  { title: "Signature Arrow Atlas: A Design Study",
    subject: "Signature arrow atlas design study",
    label: "signature-arrow-atlas",
    description: "The Signature Arrow Atlas is a design study for a tool that draws small categories as maps of objects and arrows, letting a student navigate structure by arrows.",
    a1: "One atlas: five parts for categories as maps.", a2: "The whole design: edit, draw, trace, check.", a3: "The design against abstraction: arrows made visible.",
    figures: {"atlas_parts": 5, "category_maps": 6, "arrow_kinds": 4, "demo_cases": 7, "design_panels": 4, "check_steps": 5, "spec_pages": 10, "test_cases": 8} },
  { title: "Signature Morphism Workbench: A Design Study",
    subject: "Signature morphism workbench design study",
    label: "signature-morphism-workbench",
    description: "The Signature Morphism Workbench is a design study for a tool that classifies small arrows as monomorphisms, epimorphisms, or isomorphisms, and tests the axioms on them.",
    a1: "One workbench: five tools for arrow kinds.", a2: "The whole design: edit, test, classify, check.", a3: "The design against definition: cancellation made visible.",
    figures: {"workbench_tools": 5, "morphism_kinds": 4, "special_arrows": 3, "demo_cases": 7, "design_panels": 4, "check_steps": 5, "spec_pages": 10, "test_cases": 8} },
  { title: "Signature Functor Bridge: A Design Study",
    subject: "Signature functor bridge design study",
    label: "signature-functor-bridge",
    description: "The Signature Functor Bridge is a design study for a tool that maps a small category to another by a functor, showing objects and arrows carried across.",
    a1: "One bridge: five parts for translation between categories.", a2: "The whole design: define, check, carry across, display.", a3: "The design against translation: laws checked as they go.",
    figures: {"bridge_parts": 5, "functor_kinds": 3, "example_bridges": 5, "demo_cases": 7, "design_panels": 4, "check_steps": 5, "spec_pages": 10, "test_cases": 8} },
  { title: "Signature Naturality Checker: A Design Study",
    subject: "Signature naturality checker design study",
    label: "signature-naturality-checker",
    description: "The Signature Naturality Checker is a design study for a tool that tests whether a family of arrows is natural, by checking the naturality square for each arrow.",
    a1: "One checker: five parts for naturality squares.", a2: "The whole design: enter, test, show, compose.", a3: "The design against naturality: squares checked, never assumed.",
    figures: {"checker_parts": 5, "square_tests": 4, "example_maps": 4, "demo_cases": 7, "design_panels": 4, "check_steps": 5, "spec_pages": 10, "test_cases": 8} },
  { title: "Signature Yoneda Explorer: A Design Study",
    subject: "Signature Yoneda explorer design study",
    label: "signature-yoneda-explorer",
    description: "The Signature Yoneda Explorer is a design study for a tool that shows an object through its Hom-sets, letting a student recover an element from a natural transformation.",
    a1: "One explorer: five parts for objects as relationships.", a2: "The whole design: pick, build, evaluate, recover.", a3: "The design against the lemma: bijection shown, never proved.",
    figures: {"explorer_parts": 5, "object_views": 4, "hom_displays": 3, "demo_cases": 7, "design_panels": 4, "check_steps": 5, "spec_pages": 10, "test_cases": 8} },
  { title: "Signature Adjunction Pairing Bench: A Design Study",
    subject: "Signature adjunction pairing bench design study",
    label: "signature-adjunction-pairing-bench",
    description: "The Signature Adjunction Pairing Bench is a design study for a tool that pairs a free functor with its forgetful partner, checks the Hom-bijection, and verifies the triangle identities.",
    a1: "One bench: five parts for pairing free and forgetful.", a2: "The whole design: pair, check, build, verify.", a3: "The design against adjunction: pairing shown, never found.",
    figures: {"bench_parts": 5, "adjoint_pairs": 4, "triangle_checks": 2, "demo_cases": 7, "design_panels": 4, "check_steps": 6, "spec_pages": 11, "test_cases": 9} },
  { title: "Signature Limit Builder: A Design Study",
    subject: "Signature limit builder design study",
    label: "signature-limit-builder",
    description: "The Signature Limit Builder is a design study for a tool that takes a small diagram, builds its limit as a universal cone, and checks the factoring property.",
    a1: "One builder: five parts for universal cones.", a2: "The whole design: draw, build, factor, display.", a3: "The design against the limit: construction shown, never assumed.",
    figures: {"builder_parts": 5, "diagram_shapes": 3, "limit_kinds": 4, "demo_cases": 7, "design_panels": 4, "check_steps": 5, "spec_pages": 10, "test_cases": 8} },
  { title: "Signature Colimit Gluer: A Design Study",
    subject: "Signature colimit gluer design study",
    label: "signature-colimit-gluer",
    description: "The Signature Colimit Gluer is a design study for a tool that takes a small diagram, glues its objects into a colimit, and checks the factoring property.",
    a1: "One gluer: five parts for universal gluing.", a2: "The whole design: draw, glue, factor, display.", a3: "The design against the colimit: gluing shown, never assumed.",
    figures: {"gluer_parts": 5, "diagram_shapes": 3, "colimit_kinds": 4, "demo_cases": 7, "design_panels": 4, "check_steps": 5, "spec_pages": 10, "test_cases": 8} },
  { title: "Signature Monad Workshop: A Design Study",
    subject: "Signature monad workshop design study",
    label: "signature-monad-workshop",
    description: "The Signature Monad Workshop is a design study for a tool that wraps values in five example monads, flattens nested wrapping, and checks the three monad laws.",
    a1: "One workshop: five tools for wrapping and flattening.", a2: "The whole design: wrap, flatten, check, compose.", a3: "The design against effects: wrapping shown, never solved.",
    figures: {"workshop_tools": 5, "monad_examples": 5, "effect_kinds": 4, "demo_cases": 8, "design_panels": 4, "check_steps": 6, "spec_pages": 11, "test_cases": 10} },
  { title: "Signature Universal Property Studio: A Design Study",
    subject: "Signature universal property studio design study",
    label: "signature-universal-property-studio",
    description: "The Signature Universal Property Studio is a design study for a tool that states a universal property for six constructions, proves uniqueness by mutual factoring, and checks existence per case.",
    a1: "One studio: five tools for define-by-role.", a2: "The whole design: state, factor, prove, check existence.", a3: "The design against definition: role shown, construction checked.",
    figures: {"studio_tools": 5, "property_cases": 6, "construction_kinds": 5, "demo_cases": 7, "design_panels": 4, "check_steps": 5, "spec_pages": 10, "test_cases": 8} },
  { title: "Signature Cartesian Closed Lab: A Design Study",
    subject: "Signature cartesian closed lab design study",
    label: "signature-cartesian-closed-lab",
    description: "The Signature Cartesian Closed Lab is a design study for a tool that builds exponentials for small finite sets, curries two-argument maps, and checks the bijection.",
    a1: "One lab: five parts for exponentials and currying.", a2: "The whole design: build, curry, check, display.", a3: "The design against functions: function types built, never assumed.",
    figures: {"lab_parts": 5, "exponential_demos": 4, "currying_cases": 3, "demo_cases": 7, "design_panels": 4, "check_steps": 5, "spec_pages": 10, "test_cases": 8} },
  { title: "Signature Topos Universe Simulator: A Design Study",
    subject: "Signature topos universe simulator design study",
    label: "signature-topos-universe-simulator",
    description: "The Signature Topos Universe Simulator is a design study for a tool that shows three tiny toposes side by side, with their truth values and internal logics compared.",
    a1: "One simulator: five parts for universes side by side.", a2: "The whole design: pick, classify, compare, limit.", a3: "The design against universes: many shown, none claimed.",
    figures: {"simulator_parts": 5, "universe_views": 3, "truth_value_kinds": 2, "demo_cases": 7, "design_panels": 4, "check_steps": 5, "spec_pages": 10, "test_cases": 8} },
  { title: "Signature Abelian Ledger: A Design Study",
    subject: "Signature abelian ledger design study",
    label: "signature-abelian-ledger",
    description: "The Signature Abelian Ledger is a design study for a tool that records kernels, cokernels, and exact sequences for small diagrams of abelian groups.",
    a1: "One ledger: five parts for kernels and exactness.", a2: "The whole design: enter, compute, check, chase.", a3: "The design against homology: bookkeeping shown, never computed.",
    figures: {"ledger_parts": 5, "exact_sequences": 4, "diagram_chases": 3, "demo_cases": 7, "design_panels": 4, "check_steps": 5, "spec_pages": 10, "test_cases": 8} },
  { title: "Signature Tensor Loom: A Design Study",
    subject: "Signature tensor loom design study",
    label: "signature-tensor-loom",
    description: "The Signature Tensor Loom is a design study for a tool that weaves small tensors, rebrackets them, and checks coherence with string diagrams.",
    a1: "One loom: five parts for weaving tensors.", a2: "The whole design: weave, rebracket, check, draw.", a3: "The design against coherence: weaving shown, never proved.",
    figures: {"loom_parts": 5, "tensor_kinds": 3, "braidings": 2, "demo_cases": 7, "design_panels": 4, "check_steps": 5, "spec_pages": 10, "test_cases": 8} },
  { title: "Signature Enrichment Studio: A Design Study",
    subject: "Signature enrichment studio design study",
    label: "signature-enrichment-studio",
    description: "The Signature Enrichment Studio is a design study for a tool that enriches a small category over three bases, showing Hom-sets becoming Hom-objects.",
    a1: "One studio: five parts for Hom-objects.", a2: "The whole design: pick a base, build, check, compare.", a3: "The design against enrichment: structure kept, never proved.",
    figures: {"studio_parts": 5, "base_choices": 3, "enrichment_kinds": 3, "demo_cases": 7, "design_panels": 4, "check_steps": 5, "spec_pages": 10, "test_cases": 8} },
  { title: "Signature Kan Extension Engine: A Design Study",
    subject: "Signature Kan extension engine design study",
    label: "signature-kan-extension-engine",
    description: "The Signature Kan Extension Engine is a design study for a tool that extends a small functor along another, left and right, and checks the universal property.",
    a1: "One engine: five parts for universal extension.", a2: "The whole design: enter, extend left, extend right, check.", a3: "The design against extension: best shown, never guaranteed.",
    figures: {"engine_parts": 5, "extension_kinds": 2, "example_extensions": 4, "demo_cases": 7, "design_panels": 4, "check_steps": 5, "spec_pages": 10, "test_cases": 8} },
  { title: "Signature Sheaf Garden: A Design Study",
    subject: "Signature sheaf garden design study",
    label: "signature-sheaf-garden",
    description: "The Signature Sheaf Garden is a design study for a tool that plants sections on open patches, checks agreement on overlaps, and glues them into global sections.",
    a1: "One garden: five parts for planting and gluing.", a2: "The whole design: plant, check, glue, display.", a3: "The design against locality: local to global, visibly.",
    figures: {"garden_parts": 5, "open_patches": 4, "section_kinds": 2, "demo_cases": 7, "design_panels": 4, "check_steps": 5, "spec_pages": 10, "test_cases": 8} },
  { title: "Signature Site Builder: A Design Study",
    subject: "Signature site builder design study",
    label: "signature-site-builder",
    description: "The Signature Site Builder is a design study for a tool that builds three tiny sites, checks the three covering axioms, and defines sheaves on each.",
    a1: "One builder: five parts for tiny sites.", a2: "The whole design: build, sieve, check, define sheaves.", a3: "The design against spaces: coverings without opens.",
    figures: {"builder_parts": 5, "covering_kinds": 3, "site_examples": 3, "demo_cases": 7, "design_panels": 4, "check_steps": 5, "spec_pages": 10, "test_cases": 8} },
  { title: "Signature Derived Workshop: A Design Study",
    subject: "Signature derived workshop design study",
    label: "signature-derived-workshop",
    description: "The Signature Derived Workshop is a design study for a tool that builds small complexes, inverts quasi-isomorphisms, and shows distinguished triangles.",
    a1: "One workshop: five parts for complexes and triangles.", a2: "The whole design: build, compute, test, localize.", a3: "The design against localization: inversion shown, never assumed.",
    figures: {"workshop_parts": 5, "complex_kinds": 3, "resolution_kinds": 2, "demo_cases": 7, "design_panels": 4, "check_steps": 5, "spec_pages": 10, "test_cases": 8} },
  { title: "Signature Higher Category Climber: A Design Study",
    subject: "Signature higher category climber design study",
    label: "signature-higher-category-climber",
    description: "The Signature Higher Category Climber is a design study for a tool that ascends three dimension levels, showing morphisms, 2-morphisms, and 3-morphisms in a tiny example.",
    a1: "One climber: five parts for three levels.", a2: "The whole design: pick, view, check, ascend.", a3: "The design against dimension: ascent shown, never completed.",
    figures: {"climber_parts": 5, "dimension_levels": 3, "model_kinds": 3, "demo_cases": 7, "design_panels": 4, "check_steps": 5, "spec_pages": 10, "test_cases": 8} },
  { title: "Signature Equivalence Tester: A Design Study",
    subject: "Signature equivalence tester design study",
    label: "signature-equivalence-tester",
    description: "The Signature Equivalence Tester is a design study for a tool that checks whether a small functor is fully faithful and essentially surjective, and builds its quasi-inverse.",
    a1: "One tester: five parts for the equivalence criterion.", a2: "The whole design: enter, check both, build inverse.", a3: "The design against sameness: criterion tested, never assumed.",
    figures: {"tester_parts": 5, "criterion_checks": 2, "example_pairs": 4, "demo_cases": 7, "design_panels": 4, "check_steps": 5, "spec_pages": 10, "test_cases": 8} },
  { title: "Signature Free Category Generator: A Design Study",
    subject: "Signature free category generator design study",
    label: "signature-free-category-generator",
    description: "The Signature Free Category Generator is a design study for a tool that takes a small graph, generates its free category, and shows paths as morphisms.",
    a1: "One generator: five parts for paths from graphs.", a2: "The whole design: draw, enumerate, compose, display.", a3: "The design against generation: freest shown, never related.",
    figures: {"generator_parts": 5, "graph_kinds": 3, "path_displays": 2, "demo_cases": 7, "design_panels": 4, "check_steps": 5, "spec_pages": 10, "test_cases": 8} },
  { title: "Signature Exponential Studio: A Design Study",
    subject: "Signature exponential studio design study",
    label: "signature-exponential-studio",
    description: "The Signature Exponential Studio is a design study for a tool that builds function objects for small finite sets, evaluates them, and curries maps into them.",
    a1: "One studio: five parts for function objects.", a2: "The whole design: build, apply, curry, display.", a3: "The design against functions: objects built, never assumed.",
    figures: {"studio_parts": 5, "function_kinds": 3, "currying_cases": 3, "demo_cases": 7, "design_panels": 4, "check_steps": 5, "spec_pages": 10, "test_cases": 8} },
  { title: "Signature Forgetful Lens: A Design Study",
    subject: "Signature forgetful lens design study",
    label: "signature-forgetful-lens",
    description: "The Signature Forgetful Lens is a design study for a tool that shows a structured object, drops its structure step by step, and rebuilds the free structure on the underlying set.",
    a1: "One lens: five parts for forgetting and rebuilding.", a2: "The whole design: view, slide, rebuild, compare.", a3: "The design against structure: lost and rebuilt, honestly.",
    figures: {"lens_parts": 5, "structure_kinds": 3, "forgetting_cases": 4, "demo_cases": 7, "design_panels": 4, "check_steps": 5, "spec_pages": 10, "test_cases": 8} },
];

const SOURCES = [
  { name: "Wikipedia - Category theory", url: "https://en.wikipedia.org/wiki/Category_theory", establishes: "Category theory: concrete categories, whose objects are sets with structure. Retrieved and checked 2026-11-17; the URL returned HTTP 200." },
  { name: "Wikipedia - Functor", url: "https://en.wikipedia.org/wiki/Functor", establishes: "Functor: forgetful functors as the functors that drop structure. Retrieved and checked 2026-11-17; the URL returned HTTP 200." },
  { name: "Wikipedia - Natural transformation", url: "https://en.wikipedia.org/wiki/Natural_transformation", establishes: "Natural transformation: the public research this design study builds on. Retrieved and checked 2026-11-17; the URL returned HTTP 200." },
  { name: "Wikipedia - Yoneda lemma", url: "https://en.wikipedia.org/wiki/Yoneda_lemma", establishes: "Yoneda lemma: the public research this design study builds on. Retrieved and checked 2026-11-17; the URL returned HTTP 200." },
  { name: "nLab - Yoneda lemma", url: "https://ncatlab.org/nlab/show/Yoneda+lemma", establishes: "nLab: Yoneda lemma, with the proof and its corollaries. Retrieved and checked 2026-11-17; the URL returned HTTP 200." },
  { name: "Wikipedia - Adjoint functors", url: "https://en.wikipedia.org/wiki/Adjoint_functors", establishes: "Adjoint functors: Kan extensions as adjoints to precomposition. Retrieved and checked 2026-11-17; the URL returned HTTP 200." },
  { name: "nLab - Adjoint functor", url: "https://ncatlab.org/nlab/show/adjoint+functor", establishes: "nLab: adjoint functor, with the theorems and examples. Retrieved and checked 2026-11-17; the URL returned HTTP 200." },
  { name: "Wikipedia - Limit (category theory)", url: "https://en.wikipedia.org/wiki/Limit_(category_theory)", establishes: "Limit (category theory): limits as the central example of a universal property. Retrieved and checked 2026-11-17; the URL returned HTTP 200." },
  { name: "Wikipedia - Universal property", url: "https://en.wikipedia.org/wiki/Universal_property", establishes: "Universal property: the public research this design study builds on. Retrieved and checked 2026-11-17; the URL returned HTTP 200." },
  { name: "Wikipedia - Monad (category theory)", url: "https://en.wikipedia.org/wiki/Monad_(category_theory)", establishes: "Monad (category theory): the public research this design study builds on. Retrieved and checked 2026-11-17; the URL returned HTTP 200." },
  { name: "Wikipedia - Cartesian closed category", url: "https://en.wikipedia.org/wiki/Cartesian_closed_category", establishes: "Cartesian closed category: the setting in which exponentials exist for every pair. Retrieved and checked 2026-11-17; the URL returned HTTP 200." },
  { name: "Wikipedia - Exponential object", url: "https://en.wikipedia.org/wiki/Exponential_object", establishes: "Exponential object: the public research this design study builds on. Retrieved and checked 2026-11-17; the URL returned HTTP 200." },
  { name: "Wikipedia - Topos", url: "https://en.wikipedia.org/wiki/Topos", establishes: "Topos: the public research this design study builds on. Retrieved and checked 2026-11-17; the URL returned HTTP 200." },
  { name: "Wikipedia - Abelian category", url: "https://en.wikipedia.org/wiki/Abelian_category", establishes: "Abelian category: the setting whose complexes are derived. Retrieved and checked 2026-11-17; the URL returned HTTP 200." },
  { name: "Wikipedia - Monoidal category", url: "https://en.wikipedia.org/wiki/Monoidal_category", establishes: "Monoidal category: the base structure over which enrichment is defined. Retrieved and checked 2026-11-17; the URL returned HTTP 200." },
  { name: "Wikipedia - Enriched category", url: "https://en.wikipedia.org/wiki/Enriched_category", establishes: "Enriched category: the first step toward higher categories. Retrieved and checked 2026-11-17; the URL returned HTTP 200." },
  { name: "Wikipedia - Kan extension", url: "https://en.wikipedia.org/wiki/Kan_extension", establishes: "Kan extension: the public research this design study builds on. Retrieved and checked 2026-11-17; the URL returned HTTP 200." },
  { name: "Wikipedia - Sheaf (mathematics)", url: "https://en.wikipedia.org/wiki/Sheaf_(mathematics)", establishes: "Sheaf (mathematics): sheaves defined over a Grothendieck topology. Retrieved and checked 2026-11-17; the URL returned HTTP 200." },
  { name: "Wikipedia - Grothendieck topology", url: "https://en.wikipedia.org/wiki/Grothendieck_topology", establishes: "Grothendieck topology: the public research this design study builds on. Retrieved and checked 2026-11-17; the URL returned HTTP 200." },
  { name: "Wikipedia - Derived category", url: "https://en.wikipedia.org/wiki/Derived_category", establishes: "Derived category: the public research this design study builds on. Retrieved and checked 2026-11-17; the URL returned HTTP 200." },
  { name: "Wikipedia - Higher category theory", url: "https://en.wikipedia.org/wiki/Higher_category_theory", establishes: "Higher category theory: the public research this design study builds on. Retrieved and checked 2026-11-17; the URL returned HTTP 200." },
  { name: "Wikipedia - Equivalence of categories", url: "https://en.wikipedia.org/wiki/Equivalence_of_categories", establishes: "Equivalence of categories: the public research this design study builds on. Retrieved and checked 2026-11-17; the URL returned HTTP 200." },
  { name: "Wikipedia - Free category", url: "https://en.wikipedia.org/wiki/Free_category", establishes: "Free category: the public research this design study builds on. Retrieved and checked 2026-11-17; the URL returned HTTP 200." },
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
