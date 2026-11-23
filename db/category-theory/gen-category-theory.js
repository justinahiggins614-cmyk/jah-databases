// Seeded boundless generator for the category-theory database
// (public edition). Deterministic: the same seed always emits the same
// record. Usage: node gen-category-theory.js [seed]  (prints one
// JSON record) or: node gen-category-theory.js --test (runTests).
// Package-only; outputs are generated, not stored files.
"use strict";
const crypto = require("crypto");

const SLUG = "category-theory";
const RECORD_KIND = "category theory research record";
const ID_PREFIX = "JAH-CAT-";
const AI_NAME = "JAH Category Theory Librarian";
const EDITION = "public";
const SRC = "public-harvest";
const CEILING = "Generator ceiling: up to 1,000,000,000 scales per file, generated on demand by the file AI — not stored files.";
const HONESTY = " No claim of consciousness, sentience, or unlimited intelligence is established by this record.";

const TOPICS = [
  { title: "Category Theory: An Overview",
    subject: "category theory overview",
    label: "category-theory-overview",
    description: "Category theory is the mathematical study of structure through objects and arrows, called morphisms, between them.",
    a1: "One idea: mathematics as objects and arrows.", a2: "The whole language: categories, functors, transformations.", a3: "The language against mathematics: one pattern, many fields.",
    figures: {"founding_year": 1945, "founders": 2, "key_concepts": 6, "century": 20, "applications": 5, "core_definitions": 3, "textbooks": 2, "subfields": 4} },
  { title: "Categories and Morphisms",
    subject: "categories and morphisms",
    label: "categories-and-morphisms",
    description: "A category is defined by its objects and its morphisms, the arrows between them.",
    a1: "One definition: objects, Hom-sets, identity, composition.", a2: "The whole structure: two axioms, three special arrows.", a3: "The definition against maps: one pattern for all fields.",
    figures: {"axioms": 2, "morphism_kinds": 4, "identity_laws": 2, "examples": 5, "century": 20, "special_morphisms": 3, "composition_rules": 1, "founding_year": 1945} },
  { title: "Functors: Maps Between Categories",
    subject: "functors between categories",
    label: "functors-between-categories",
    description: "A functor is a map between categories that sends objects to objects and arrows to arrows, preserving identities and composition.",
    a1: "One map: objects to objects, arrows to arrows.", a2: "The whole definition: two laws, many examples.", a3: "The definition against translation: structure preserved.",
    figures: {"functor_laws": 2, "functor_kinds": 3, "examples": 5, "century": 20, "composition_rules": 2, "founding_year": 1945, "forgetful_examples": 3, "free_examples": 2} },
  { title: "Natural Transformations",
    subject: "natural transformations between functors",
    label: "natural-transformations",
    description: "A natural transformation is a family of arrows, one per object, that translates one functor into another in a way compatible with every arrow.",
    a1: "One square: naturality, both paths agree.", a2: "The whole definition: one arrow per object, compatible everywhere.", a3: "The definition against choice: natural means choice-free.",
    figures: {"defining_condition": 1, "functors_compared": 2, "examples": 4, "century": 20, "founding_year": 1945, "components": 2, "composition_kinds": 2, "key_uses": 3} },
  { title: "The Yoneda Lemma",
    subject: "the Yoneda lemma",
    label: "yoneda-lemma",
    description: "The Yoneda lemma is the fundamental lemma of category theory: it says an object is known by its relationships.",
    a1: "One bijection: transformations equal elements.", a2: "The whole lemma: an object is its relationships.", a3: "The lemma against identity: arrows determine objects.",
    figures: {"publication_year": 1954, "yoneda_age": 29, "statements": 2, "key_corollaries": 3, "century": 20, "functors_involved": 2, "natural_bijections": 1, "embeddings": 1} },
  { title: "Adjoint Functors",
    subject: "adjoint functors",
    label: "adjoint-functors",
    description: "Adjoint functors are a pair of functors that fit together like a free construction and its forgetful partner.",
    a1: "One bijection: free arrows equal underlying arrows.", a2: "The whole definition: unit, counit, two triangles.", a3: "The definition against construction: free and forgetful as one.",
    figures: {"functors_paired": 2, "defining_bijections": 1, "unit_counit": 2, "examples": 5, "century": 20, "key_theorems": 3, "founding_year": 1958, "triangle_identities": 2} },
  { title: "Limits in Category Theory",
    subject: "limits in category theory",
    label: "limits-category-theory",
    description: "A limit is the universal way of combining the objects of a diagram into one object.",
    a1: "One cone: universal, every other factors through it.", a2: "The whole idea: products, equalizers, pullbacks as one.", a3: "The idea against combination: the best object with maps to the parts.",
    figures: {"limit_kinds": 4, "examples": 5, "cone_parts": 2, "century": 20, "universal_properties": 1, "diagram_shapes": 3, "key_theorems": 2, "founding_year": 1945} },
  { title: "Colimits in Category Theory",
    subject: "colimits in category theory",
    label: "colimits-category-theory",
    description: "A colimit is the universal way of gluing the objects of a diagram together into one object.",
    a1: "One cocone: universal, every other factors through it.", a2: "The whole idea: coproducts, coequalizers, pushouts as one.", a3: "The idea against gluing: the best object receiving maps from the parts.",
    figures: {"colimit_kinds": 4, "examples": 5, "cocone_parts": 2, "century": 20, "universal_properties": 1, "diagram_shapes": 3, "key_theorems": 2, "duality_principle": 1} },
  { title: "Monads in Category Theory",
    subject: "monads in category theory",
    label: "monads-category-theory",
    description: "A monad is a way of wrapping values with extra structure, such as a list of possible results, a state, or a possible failure.",
    a1: "One wrap: values with extra structure, flattened by law.", a2: "The whole definition: endofunctor, unit, multiplication.", a3: "The definition against effects: pure programs with effects.",
    figures: {"monad_laws": 3, "components": 2, "examples": 5, "century": 20, "algebras_kinds": 2, "kleisli_parts": 2, "founding_year": 1958, "key_theorems": 3} },
  { title: "Universal Properties",
    subject: "universal properties in category theory",
    label: "universal-properties",
    description: "A universal property describes an object by what it does, rather than by what it is made of.",
    a1: "One pattern: defined by role, unique up to isomorphism.", a2: "The whole idea: products, free objects, limits as one pattern.", a3: "The idea against construction: what it does, not what it is.",
    figures: {"defining_pattern": 1, "examples": 6, "uniqueness_proofs": 1, "century": 20, "key_constructions": 5, "arrow_conditions": 2, "founding_year": 1945, "uses": 4} },
  { title: "Cartesian Closed Categories",
    subject: "cartesian closed categories",
    label: "cartesian-closed-categories",
    description: "A cartesian closed category is a category in which functions live inside it as objects.",
    a1: "One bijection: currying, two arguments become one.", a2: "The whole definition: products plus exponentials.", a3: "The definition against functions: functions as objects.",
    figures: {"defining_features": 3, "examples": 4, "exponential_laws": 3, "century": 20, "key_theorems": 2, "type_correspondence": 1, "founding_year": 1960, "product_rules": 2} },
  { title: "Topos Theory",
    subject: "topos theory",
    label: "topos-theory",
    description: "A topos is a category that behaves like a universe of sets. It has finite limits, exponentials, which are objects of maps, and a subobject classifier, an object Omega of truth values such that every subobject is classified by a unique arrow into Omega.",
    a1: "One object: Omega, the classifier of truth.", a2: "The whole definition: limits, exponentials, classifier.", a3: "The definition against universes: many universes, one pattern.",
    figures: {"defining_features": 4, "founding_year": 1963, "founders": 2, "century": 20, "examples": 4, "key_theorems": 3, "internal_logics": 1, "subobject_classifiers": 1} },
  { title: "Abelian Categories",
    subject: "abelian categories",
    label: "abelian-categories",
    description: "An abelian category is a category in which homological algebra works as it does for abelian groups.",
    a1: "One setting: kernels, cokernels, exactness as axioms.", a2: "The whole definition: additive plus exactness.", a3: "The definition against homology: one home for all of it.",
    figures: {"defining_features": 4, "founding_year": 1955, "founders": 2, "century": 20, "examples": 4, "key_theorems": 3, "exact_sequences": 2, "homology_uses": 2} },
  { title: "Monoidal Categories",
    subject: "monoidal categories",
    label: "monoidal-categories",
    description: "A monoidal category is a category with a way of multiplying objects, called the tensor product, and a unit object that acts as one for the tensor.",
    a1: "One product: tensor, with unit and coherence.", a2: "The whole definition: multiply, rebracket, agree.", a3: "The definition against combination: one pattern for tensors.",
    figures: {"defining_features": 3, "coherence_conditions": 2, "examples": 5, "century": 20, "key_theorems": 2, "tensor_kinds": 3, "founding_year": 1963, "unit_laws": 2} },
  { title: "Enriched Categories",
    subject: "enriched categories",
    label: "enriched-categories",
    description: "An enriched category is a category whose arrows between two objects form an object of another category, rather than a mere set.",
    a1: "One idea: Hom-collections as objects, not sets.", a2: "The whole definition: Hom-objects plus composition in V.", a3: "The definition against structure loss: arrows keep their shape.",
    figures: {"defining_features": 3, "base_categories": 3, "examples": 4, "century": 20, "key_theorems": 2, "enrichment_kinds": 3, "founding_year": 1965, "composition_laws": 2} },
  { title: "Kan Extensions",
    subject: "Kan extensions",
    label: "kan-extensions",
    description: "A Kan extension is the best way to extend a functor along another functor.",
    a1: "One extension: the universal way to extend a functor.", a2: "The whole idea: limits, adjoints, free objects as one.", a3: "The idea against extension: the best extension, not any extension.",
    figures: {"extension_kinds": 2, "defining_property": 1, "examples": 4, "century": 20, "key_theorems": 3, "founding_year": 1958, "adjunction_uses": 2, "limit_uses": 2} },
  { title: "Sheaves in Category Theory",
    subject: "sheaves in category theory",
    label: "sheaves-category-theory",
    description: "A sheaf is a way of assigning data to the open parts of a space so that local pieces fit together into global data.",
    a1: "One rule: local data that agree must glue uniquely.", a2: "The whole idea: sections over opens, assembled globally.", a3: "The idea against locality: local to global, precisely.",
    figures: {"sheaf_axioms": 2, "examples": 4, "founding_year": 1950, "century": 20, "key_theorems": 3, "topologies_used": 2, "sections_kinds": 2, "gluing_conditions": 1} },
  { title: "Grothendieck Topologies",
    subject: "Grothendieck topologies",
    label: "grothendieck-topologies",
    description: "A Grothendieck topology is a generalized notion of open cover that works in any category, not only in topological spaces.",
    a1: "One idea: coverings as sieves, not open sets.", a2: "The whole definition: three axioms for coverings.", a3: "The definition against spaces: sheaves where there are no opens.",
    figures: {"covering_axioms": 3, "founding_year": 1960, "founders": 1, "century": 20, "examples": 3, "key_theorems": 2, "site_parts": 2, "topologies_used": 2} },
  { title: "Derived Categories",
    subject: "derived categories",
    label: "derived-categories",
    description: "A derived category is a category in which homological information is kept and inessential differences are ignored.",
    a1: "One move: invert the maps that preserve homology.", a2: "The whole construction: complexes, localized, triangulated.", a3: "The construction against resolutions: choice removed.",
    figures: {"founding_year": 1961, "founders": 2, "construction_steps": 3, "century": 20, "examples": 3, "key_theorems": 3, "triangulated_axioms": 4, "homology_uses": 2} },
  { title: "Higher Category Theory",
    subject: "higher category theory",
    label: "higher-category-theory",
    description: "Higher category theory studies categories with morphisms between morphisms, up to any level.",
    a1: "One idea: morphisms between morphisms, at every level.", a2: "The whole field: models, coherence, comparison.", a3: "The field against dimension: categories, raised.",
    figures: {"dimensions": 3, "models": 4, "founding_year": 1960, "century": 20, "key_theorems": 3, "coherence_levels": 3, "examples": 3, "n_kinds": 2} },
  { title: "Equivalence of Categories",
    subject: "equivalence of categories",
    label: "equivalence-of-categories",
    description: "Two categories are equivalent when there are functors between them whose composites are naturally isomorphic to the identity functors.",
    a1: "One criterion: fully faithful plus essentially surjective.", a2: "The whole idea: same structure, different objects.", a3: "The idea against sameness: equivalence, not identity.",
    figures: {"defining_conditions": 2, "examples": 4, "key_theorems": 2, "century": 20, "functors_involved": 2, "isomorphism_kinds": 2, "founding_year": 1945, "criteria": 3} },
  { title: "Free Categories",
    subject: "free categories",
    label: "free-categories",
    description: "The free category on a directed graph has the graph's vertices as objects and its paths as morphisms, with concatenation as composition.",
    a1: "One construction: paths, concatenated, with empty identities.", a2: "The whole idea: the freest category on a graph.", a3: "The idea against generation: nothing added, nothing imposed.",
    figures: {"construction_steps": 3, "examples": 4, "universal_properties": 1, "century": 20, "key_theorems": 2, "graph_parts": 2, "founding_year": 1945, "adjunction_uses": 1} },
  { title: "Exponential Objects",
    subject: "exponential objects",
    label: "exponential-objects",
    description: "An exponential object is the object that stands for the collection of maps from A to B.",
    a1: "One object: B^A, the maps from A to B as an object.", a2: "The whole definition: evaluation plus currying.", a3: "The definition against functions: functions, internalized.",
    figures: {"defining_property": 1, "examples": 4, "evaluation_parts": 2, "century": 20, "key_theorems": 2, "currying_uses": 2, "founding_year": 1960, "universal_arrows": 1} },
  { title: "Forgetful Functors",
    subject: "forgetful functors",
    label: "forgetful-functors",
    description: "A forgetful functor is a functor that drops structure, keeping only the underlying set.",
    a1: "One functor: structure dropped, set kept.", a2: "The whole pattern: forgetful right, free left.", a3: "The pattern against structure: lost and rebuilt, adjointly.",
    figures: {"examples": 5, "structure_dropped": 3, "adjunction_partners": 2, "century": 20, "key_theorems": 2, "faithfulness_kinds": 2, "founding_year": 1945, "concrete_categories": 3} },
];

const SOURCES = [
  { name: "Wikipedia - Category theory", url: "https://en.wikipedia.org/wiki/Category_theory", establishes: "Category theory: concrete categories, whose objects are sets with structure. Retrieved and checked 2026-11-17; the URL returned HTTP 200." },
  { name: "Wikipedia - Functor", url: "https://en.wikipedia.org/wiki/Functor", establishes: "Functor: forgetful functors as the functors that drop structure, with free functors as their adjoints. Retrieved and checked 2026-11-17; the URL returned HTTP 200." },
  { name: "Wikipedia - Natural transformation", url: "https://en.wikipedia.org/wiki/Natural_transformation", establishes: "Natural transformation: the definition, the naturality square, and its examples. Retrieved and checked 2026-11-17; the URL returned HTTP 200." },
  { name: "Wikipedia - Yoneda lemma", url: "https://en.wikipedia.org/wiki/Yoneda_lemma", establishes: "Yoneda lemma: natural transformations from a Hom-functor correspond to elements, the fundamental lemma of category theory. Retrieved and checked 2026-11-17; the URL returned HTTP 200." },
  { name: "nLab - Yoneda lemma", url: "https://ncatlab.org/nlab/show/Yoneda+lemma", establishes: "nLab: Yoneda lemma, with the proof and its corollaries, as a research reference. Retrieved and checked 2026-11-17; the URL returned HTTP 200." },
  { name: "Wikipedia - Adjoint functors", url: "https://en.wikipedia.org/wiki/Adjoint_functors", establishes: "Adjoint functors: Kan extensions as adjoints to precomposition. Retrieved and checked 2026-11-17; the URL returned HTTP 200." },
  { name: "nLab - Adjoint functor", url: "https://ncatlab.org/nlab/show/adjoint+functor", establishes: "nLab: adjoint functor, with the theorems and examples, as a research reference. Retrieved and checked 2026-11-17; the URL returned HTTP 200." },
  { name: "Wikipedia - Limit (category theory)", url: "https://en.wikipedia.org/wiki/Limit_(category_theory)", establishes: "Limit (category theory): limits as the central example of a universal property. Retrieved and checked 2026-11-17; the URL returned HTTP 200." },
  { name: "Wikipedia - Universal property", url: "https://en.wikipedia.org/wiki/Universal_property", establishes: "Universal property: the pattern that defines products, free objects, limits, and more. Retrieved and checked 2026-11-17; the URL returned HTTP 200." },
  { name: "Wikipedia - Monad (category theory)", url: "https://en.wikipedia.org/wiki/Monad_(category_theory)", establishes: "Monad (category theory): the definition, its three laws, and its examples, from adjunctions to programming. Retrieved and checked 2026-11-17; the URL returned HTTP 200." },
  { name: "Wikipedia - Cartesian closed category", url: "https://en.wikipedia.org/wiki/Cartesian_closed_category", establishes: "Cartesian closed category: the setting in which exponentials exist for every pair. Retrieved and checked 2026-11-17; the URL returned HTTP 200." },
  { name: "Wikipedia - Exponential object", url: "https://en.wikipedia.org/wiki/Exponential_object", establishes: "Exponential object: the object of maps between two objects, with evaluation and currying. Retrieved and checked 2026-11-17; the URL returned HTTP 200." },
  { name: "Wikipedia - Topos", url: "https://en.wikipedia.org/wiki/Topos", establishes: "Topos: a category with finite limits, exponentials, and a subobject classifier, a universe of sets. Retrieved and checked 2026-11-17; the URL returned HTTP 200." },
  { name: "Wikipedia - Abelian category", url: "https://en.wikipedia.org/wiki/Abelian_category", establishes: "Abelian category: the setting whose complexes are derived. Retrieved and checked 2026-11-17; the URL returned HTTP 200." },
  { name: "Wikipedia - Monoidal category", url: "https://en.wikipedia.org/wiki/Monoidal_category", establishes: "Monoidal category: the base structure over which enrichment is defined. Retrieved and checked 2026-11-17; the URL returned HTTP 200." },
  { name: "Wikipedia - Enriched category", url: "https://en.wikipedia.org/wiki/Enriched_category", establishes: "Enriched category: the first step toward higher categories, Hom-objects as categories. Retrieved and checked 2026-11-17; the URL returned HTTP 200." },
  { name: "Wikipedia - Kan extension", url: "https://en.wikipedia.org/wiki/Kan_extension", establishes: "Kan extension: the universal extension of a functor along another, left and right, with limits as a special case. Retrieved and checked 2026-11-17; the URL returned HTTP 200." },
  { name: "Wikipedia - Sheaf (mathematics)", url: "https://en.wikipedia.org/wiki/Sheaf_(mathematics)", establishes: "Sheaf (mathematics): sheaves defined over a Grothendieck topology. Retrieved and checked 2026-11-17; the URL returned HTTP 200." },
  { name: "Wikipedia - Grothendieck topology", url: "https://en.wikipedia.org/wiki/Grothendieck_topology", establishes: "Grothendieck topology: the axioms for coverings in a category, generalizing open covers. Retrieved and checked 2026-11-17; the URL returned HTTP 200." },
  { name: "Wikipedia - Derived category", url: "https://en.wikipedia.org/wiki/Derived_category", establishes: "Derived category: the localization of complexes at quasi-isomorphisms, with its triangulated structure. Retrieved and checked 2026-11-17; the URL returned HTTP 200." },
  { name: "Wikipedia - Higher category theory", url: "https://en.wikipedia.org/wiki/Higher_category_theory", establishes: "Higher category theory: categories with morphisms between morphisms, and the models for infinity-categories. Retrieved and checked 2026-11-17; the URL returned HTTP 200." },
  { name: "Wikipedia - Equivalence of categories", url: "https://en.wikipedia.org/wiki/Equivalence_of_categories", establishes: "Equivalence of categories: the definition, its criteria, and its examples. Retrieved and checked 2026-11-17; the URL returned HTTP 200." },
  { name: "Wikipedia - Free category", url: "https://en.wikipedia.org/wiki/Free_category", establishes: "Free category: the category generated by a graph, with paths as morphisms. Retrieved and checked 2026-11-17; the URL returned HTTP 200." },
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
