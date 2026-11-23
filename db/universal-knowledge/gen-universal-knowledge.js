// Seeded boundless generator for the Universal Knowledge Database
// (public edition). Deterministic: the same seed always emits the same
// record. Usage: node gen-universal-knowledge.js [seed]  (prints one
// JSON record) or: node gen-universal-knowledge.js --test (runTests).
// Package-only; outputs are generated, not stored files.
"use strict";
const crypto = require("crypto");

const SLUG = "universal-knowledge";
const RECORD_KIND = "universal knowledge record";
const ID_PREFIX = "JAH-UKNW-";
const AI_NAME = "JAH Universal Knowledge Librarian";
const EDITION = "public";
const CEILING = "Generator ceiling: up to 1,000,000,000 scales per file, generated on demand by the file AI \u2014 not stored files.";

const TOPICS = [
  {
    "title": "What Universal Knowledge Is",
    "subject": "universal knowledge identity",
    "description": "Universal knowledge is general organized knowledge: facts, ideas, methods, and records gathered across all subjects into one searchable collection, so a question in any subject can start from the same place. It is not one book and not one subject; it is the shared ground that every subject database stands on, and it grows by adding complete records, each with its subject, its sources, and its.",
    "label": "universal-knowledge-identity",
    "figures": {
      "subjects": 40,
      "catalog_items": 100,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "ladder_ranks": 24,
      "glossary_terms": 27,
      "sections": 14
    }
  },
  {
    "title": "Knowledge Organization Systems",
    "subject": "knowledge organization systems",
    "description": "A knowledge organization system is the scheme that puts knowledge in order: subjects, kinds, levels, and relationships, so a record can be found again after it is filed. The systems in use include subject lists, taxonomies, which are tree-shaped classifications, thesauri, which are word lists with relationships, and ontologies, which are shared definitions of meaning. This record specifies how.",
    "label": "knowledge-organization-systems",
    "figures": {
      "schemes": 4,
      "subjects": 40,
      "levels": 3,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "glossary_terms": 27,
      "sections": 14
    }
  },
  {
    "title": "Taxonomies and Classification",
    "subject": "taxonomies and classification",
    "description": "A taxonomy is a tree-shaped classification: a broad subject at the top, narrower subjects branching below it, and each record filed under the narrowest subject that fits it. Classification is the act of filing a record in the tree, and a good taxonomy is one where a reader can guess where a record lives before searching. This record specifies the taxonomy rules for the universal knowledge.",
    "label": "taxonomies-classification",
    "figures": {
      "tree_levels": 4,
      "subjects": 40,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "glossary_terms": 27,
      "sections": 14
    }
  },
  {
    "title": "Ontologies and Shared Meaning",
    "subject": "ontologies and shared meaning",
    "description": "An ontology is a shared definition of meaning: it names the kinds of things in a subject, the relationships between them, and the rules that keep those relationships honest, so two systems that use the same ontology agree on what their words mean. Shared meaning is what lets a knowledge graph built in one place be read in another. This record specifies the ontology rules for the universal.",
    "label": "ontologies-shared-meaning",
    "figures": {
      "kinds": 12,
      "relationships": 9,
      "rules": 6,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "glossary_terms": 27,
      "sections": 14
    }
  },
  {
    "title": "Knowledge Graphs",
    "subject": "knowledge graphs",
    "description": "A knowledge graph is knowledge stored as a web of linked records: each record is a node, which is a point in the web, and each link is a named relationship between two nodes, so a reader can walk from one fact to related facts by following links. Graphs are good at answering questions that cross subjects, because the path between two facts is itself information. This record specifies the graph.",
    "label": "knowledge-graphs",
    "figures": {
      "nodes": 24,
      "links_per_node": 3,
      "paths": 18,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "glossary_terms": 27,
      "sections": 14
    }
  },
  {
    "title": "Encyclopedia Method",
    "subject": "encyclopedia method",
    "description": "The encyclopedia method is the way of writing knowledge as articles: one article per subject, each article complete on its own, each article linking to related articles, and the whole set covering a subject from its basics to its hardest parts. The method matters because an article is the unit a reader actually reads, while the database is the store the article is built from. This record.",
    "label": "encyclopedia-method",
    "figures": {
      "articles": 24,
      "facts_per_article": 8,
      "links_per_article": 4,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "glossary_terms": 27,
      "sections": 14
    }
  },
  {
    "title": "Dictionary Method",
    "subject": "dictionary method",
    "description": "The dictionary method is the way of defining terms: one entry per term, each entry giving the pronunciation, the part of speech, which is the grammatical kind of the word, and the definition in plain words, with examples of use. Definitions are the foundation of the whole network, because a term that is never defined is a term that will be misunderstood. This record specifies how the universal.",
    "label": "dictionary-method",
    "figures": {
      "entries": 24,
      "parts_of_speech": 8,
      "examples_per_entry": 2,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "glossary_terms": 27,
      "sections": 14
    }
  },
  {
    "title": "Cross-Subject Linking",
    "subject": "cross-subject linking",
    "description": "Cross-subject linking is the practice of joining records from different subjects where they genuinely touch: a mathematics record linking to the physics that uses it, a history record linking to the geography it happened in, a biology record linking to the chemistry inside it. Links are made only where the connection is real and sourced, never where it merely sounds clever. This record.",
    "label": "cross-subject-linking",
    "figures": {
      "links": 36,
      "subjects": 40,
      "bridge_subjects": 6,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "glossary_terms": 27,
      "sections": 14
    }
  }
];

const SOURCES = [
  {
    "name": "Wikipedia - Knowledge graph",
    "url": "https://en.wikipedia.org/wiki/Knowledge_graph",
    "establishes": "Knowledge graph: how knowledge is organized as linked records with named relationships.",
    "retrieved": "2026-11-17",
    "resource_id": "en.wikipedia.org/wiki/Knowledge_graph"
  },
  {
    "name": "Wikipedia - Knowledge base",
    "url": "https://en.wikipedia.org/wiki/Knowledge_base",
    "establishes": "Knowledge base: how organized knowledge is stored for retrieval and use.",
    "retrieved": "2026-11-17",
    "resource_id": "en.wikipedia.org/wiki/Knowledge_base"
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
  const label = topic.label;
  const demo = buildDemo(topic, label);
  const rec = {
    id: id,
    slug: SLUG,
    edition: EDITION,
    record_kind: RECORD_KIND,
    title: topic.title + " (Generated " + idx + ")",
    subject: topic.subject,
    status: "built",
    src: EDITION === "public" ? "public-harvest" : "signature-generated",
    ai_name: AI_NAME,
    description: topic.description + " " + "No claim of consciousness, sentience, or unlimited intelligence is established by this system; singularity and self-aware framing here is a Signature design claim only, never established fact.",
    body: "<h2>Description</h2><p>" + topic.description + "</p>",
    demo: demo.code,
    expected_output: demo.expected,
    program: "class GeneratedProgram:\n    def run(self):\n        return {\"deterministic\": True}\n",
    sources: SOURCES,
    generator: { type: "seeded boundless generator", gen_id_prefix: ID_PREFIX + "GEN-", hard_stop: 1000000000, throttle_per_call: 100, ceiling_note: CEILING },
    scales: { A1: "One record: a single entry, fully specified and checkable.", A2: "The whole type: every part of the type, specified and tested together.", A3: "The type against the network: the type feeding websites, generators, and the generator database." },
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
  t("slug form", a.slug === SLUG);
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
