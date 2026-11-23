// Seeded boundless generator for the Universal Knowledge Database
// (signature edition). Deterministic: the same seed always emits the same
// record. Usage: node gen-universal-knowledge-signature.js [seed]  (prints one
// JSON record) or: node gen-universal-knowledge-signature.js --test (runTests).
// Package-only; outputs are generated, not stored files.
"use strict";
const crypto = require("crypto");

const SLUG = "universal-knowledge-signature";
const RECORD_KIND = "universal knowledge record";
const ID_PREFIX = "JAH-UKNWS-";
const AI_NAME = "JAH Universal Knowledge Librarian (Signature)";
const EDITION = "signature";
const CEILING = "Generator ceiling: up to 1,000,000,000 scales per file, generated on demand by the file AI \u2014 not stored files.";

const TOPICS = [
  {
    "title": "Signature Knowledge Atrium",
    "subject": "signature knowledge atrium",
    "description": "The Signature Knowledge Atrium is a design for a single hall where all universal knowledge meets: a circular room with a subject for every arch, a record for every shelf, and a reading desk at the center where any record can be opened in full. The design imagines the atrium as the front door of the universal knowledge database, built to be walked through rather than searched from outside.",
    "label": "signature-knowledge-atrium",
    "figures": {
      "arches": 40,
      "shelves": 24,
      "desks": 1,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "glossary_terms": 27,
      "sections": 14
    }
  },
  {
    "title": "Signature Taxonomy Treehouse",
    "subject": "signature taxonomy treehouse",
    "description": "The Signature Taxonomy Treehouse is a design for a taxonomy that can be climbed: a tree with broad subjects as the trunk, narrower subjects as branches, and records as leaves, with a walkway at every level so a reader can climb from the general to the specific without getting lost. The design imagines classification as a place, not a list.",
    "label": "signature-taxonomy-treehouse",
    "figures": {
      "levels": 4,
      "branches": 40,
      "leaves": 24,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "glossary_terms": 27,
      "sections": 14
    }
  },
  {
    "title": "Signature Ontology Loom",
    "subject": "signature ontology loom",
    "description": "The Signature Ontology Loom is a design for weaving shared meaning: kinds are threads, relationships are the weave, and the finished cloth is an ontology that two systems can read the same way. The design imagines meaning as something made carefully on a loom, not declared in a single sentence, with every new thread defined before it is woven in.",
    "label": "signature-ontology-loom",
    "figures": {
      "threads": 12,
      "weave_rows": 9,
      "rules": 6,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "glossary_terms": 27,
      "sections": 14
    }
  },
  {
    "title": "Signature Knowledge Graph Web",
    "subject": "signature knowledge graph web",
    "description": "The Signature Knowledge Graph Web is a design for a web of linked records that can be walked: each record is a knot, each named relationship is a strand, and a reader follows strands from one fact to related facts, with every strand labeled with its reason and its source. The design imagines the graph as a web that is strung, not drawn, so it can be re-strung when knowledge changes.",
    "label": "signature-knowledge-graph-web",
    "figures": {
      "knots": 24,
      "strands_per_knot": 3,
      "paths": 18,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "glossary_terms": 27,
      "sections": 14
    }
  },
  {
    "title": "Signature Encyclopedia Workshop",
    "subject": "signature encyclopedia workshop",
    "description": "The Signature Encyclopedia Workshop is a design for a workshop where articles are built from records: one bench per subject, facts arriving as records, articles assembled on the bench, and links fitted both ways before the article leaves the shop. The design imagines article-making as bench work, with the record as the raw material and the article as the finished piece.",
    "label": "signature-encyclopedia-workshop",
    "figures": {
      "benches": 24,
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
    "title": "Signature Dictionary Press",
    "subject": "signature dictionary press",
    "description": "The Signature Dictionary Press is a design for a press that prints definitions: a term enters as a headword, its pronunciation, part of speech, and plain-words definition are set in type, an example sentence is added, and the entry is pressed onto the page. The design imagines definitions as printed things, fixed and checkable, never as passing remarks.",
    "label": "signature-dictionary-press",
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
    "title": "Signature Bridge Library",
    "subject": "signature bridge library",
    "description": "The Signature Bridge Library is a design for a library built of bridges: each bridge joins two subjects where they genuinely touch, with the reason for the bridge written on its span, and the library is the set of all such bridges. The design imagines cross-subject knowledge as a place you cross, not a list you read, so the reader feels the join.",
    "label": "signature-bridge-library",
    "figures": {
      "bridges": 36,
      "subjects": 40,
      "bridge_subjects": 6,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "glossary_terms": 27,
      "sections": 14
    }
  },
  {
    "title": "Signature Provenance Ledger",
    "subject": "signature provenance ledger",
    "description": "The Signature Provenance Ledger is a design for a ledger that records where every fact came from: each entry holds the web address, the resource identifier, and the retrieval date, and the ledger is bound so that no entry can be silently rewritten. The design imagines provenance as bookkeeping, where every fact is a coin and every coin must show where it was minted.",
    "label": "signature-provenance-ledger",
    "figures": {
      "ledger_fields": 3,
      "sources_per_record": 3,
      "records_per_edition": 24,
      "pair_records": 48,
      "glossary_terms": 27,
      "sections": 14,
      "retrieval_year": 2026,
      "retrieval_month": 11
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
