// Seeded boundless generator for the Universal Database Generator
// (signature edition). Deterministic: the same seed always emits the same
// record. Usage: node gen-universal-database-generator-signature.js [seed]  (prints one
// JSON record) or: node gen-universal-database-generator-signature.js --test (runTests).
// Package-only; outputs are generated, not stored files.
"use strict";
const crypto = require("crypto");

const SLUG = "universal-database-generator-signature";
const RECORD_KIND = "universal database generator record";
const ID_PREFIX = "JAH-UDBGS-";
const AI_NAME = "JAH Universal Database Generator Librarian (Signature)";
const EDITION = "signature";
const CEILING = "Generator ceiling: up to 1,000,000,000 scales per file, generated on demand by the file AI \u2014 not stored files.";

const TOPICS = [
  {
    "title": "Signature Category Gate",
    "subject": "signature category gate",
    "description": "The Signature Category Gate is a design for a gate where new categories arrive: a name and a description are laid on the counter, the manifest is searched for existing coverage, and the gate either opens to building or points to the database that already covers it. The design imagines acceptance as a gate, where nothing is built twice.",
    "label": "signature-category-gate",
    "figures": {
      "acceptance_steps": 4,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "glossary_terms": 27,
      "sections": 14,
      "manifest_entries": 63047,
      "hard_stop": 1000000000
    }
  },
  {
    "title": "Signature Research Net",
    "subject": "signature research net",
    "description": "The Signature Research Net is a design for a net that catches real resources: it is cast over the network, it pulls in actual links and full data, and every catch is tagged with its web address, its identifier, and its retrieval date. The design imagines research as fishing with a net, where a summary is not a catch and a bare name slips through the mesh.",
    "label": "signature-research-net",
    "figures": {
      "research_steps": 7,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "glossary_terms": 27,
      "sections": 14,
      "hard_stop": 1000000000,
      "throttle": 100
    }
  },
  {
    "title": "Signature Spec Loom",
    "subject": "signature spec loom",
    "description": "The Signature Spec Loom is a design for a loom that weaves complete specifications: identity, structure, retrieval, code, generator, interface, documentation, demo, tests, validation, history, provenance, and expansion are the threads, and the finished cloth is a specification long because it is complete, never padded. The design imagines specification as weaving, where a missing thread leaves.",
    "label": "signature-spec-loom",
    "figures": {
      "spec_sections": 14,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "glossary_terms": 27,
      "hard_stop": 1000000000,
      "throttle": 100,
      "build_steps": 11
    }
  },
  {
    "title": "Signature Mold Shop",
    "subject": "signature mold shop",
    "description": "The Signature Mold Shop is a design for a shop where record shapes are cast: the field list is the mold, the identifier prefix is the stamp, and every record poured into the mold comes out in the same shape. The design imagines structure as casting, where a good mold makes good records easy.",
    "label": "signature-mold-shop",
    "figures": {
      "shape_fields": 24,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "glossary_terms": 27,
      "sections": 14,
      "hard_stop": 1000000000
    }
  },
  {
    "title": "Signature Record Kiln",
    "subject": "signature record kiln",
    "description": "The Signature Record Kiln is a design for a kiln that fires generated records: each record enters with every field filled, is fired by execution, and comes out checked, with its demo run, its program run, and its sources dated. The design imagines generation as firing clay, where a cracked record is caught before it leaves the kiln.",
    "label": "signature-record-kiln",
    "figures": {
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "glossary_terms": 27,
      "sections": 14,
      "hard_stop": 1000000000,
      "throttle": 100,
      "checks": 6
    }
  },
  {
    "title": "Signature Search Well",
    "subject": "signature search well",
    "description": "The Signature Search Well is a design for a well that holds search: the index is the water, the bucket is the query, and every bucket drawn carries full records with their sources attached. The design imagines retrieval as drawing water, where the well is dug with the database, not after it.",
    "label": "signature-search-well",
    "figures": {
      "search_modes": 4,
      "indexed_fields": 11,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "glossary_terms": 27,
      "sections": 14,
      "hard_stop": 1000000000
    }
  },
  {
    "title": "Signature Code Forge",
    "subject": "signature code forge",
    "description": "The Signature Code Forge is a design for a forge where working code is hammered out: demos, programs, and generators are heated in the standard library and struck until they run, with every expected output captured from a real run. The design imagines code as forged iron, where a piece that has never been struck is not yet a tool.",
    "label": "signature-code-forge",
    "figures": {
      "code_parts": 3,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "glossary_terms": 27,
      "sections": 14,
      "hard_stop": 1000000000,
      "checks": 6
    }
  },
  {
    "title": "Signature Generator Cradle",
    "subject": "signature generator cradle",
    "description": "The Signature Generator Cradle is a design for a cradle that rocks new generators to life: each generator is laid in seeded, gated, and throttled, and it is rocked until its own tests pass. The design imagines a reusable generator as a child, where the cradle holds it until it can stand on its own.",
    "label": "signature-generator-cradle",
    "figures": {
      "hard_stop": 1000000000,
      "throttle": 100,
      "gates": 4,
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
    "name": "Wikipedia - Database",
    "url": "https://en.wikipedia.org/wiki/Database",
    "establishes": "Database: how organized collections of records are stored and searched.",
    "retrieved": "2026-11-17",
    "resource_id": "en.wikipedia.org/wiki/Database"
  },
  {
    "name": "Wikipedia - Code generation",
    "url": "https://en.wikipedia.org/wiki/Code_generation",
    "establishes": "Code generation: how programs create other programs from specifications.",
    "retrieved": "2026-11-17",
    "resource_id": "en.wikipedia.org/wiki/Code_generation"
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
