// Seeded boundless generator for the Universal Database Generator
// (public edition). Deterministic: the same seed always emits the same
// record. Usage: node gen-universal-database-generator.js [seed]  (prints one
// JSON record) or: node gen-universal-database-generator.js --test (runTests).
// Package-only; outputs are generated, not stored files.
"use strict";
const crypto = require("crypto");

const SLUG = "universal-database-generator";
const RECORD_KIND = "universal database generator record";
const ID_PREFIX = "JAH-UDBG-";
const AI_NAME = "JAH Universal Database Generator Librarian";
const EDITION = "public";
const CEILING = "Generator ceiling: up to 1,000,000,000 scales per file, generated on demand by the file AI \u2014 not stored files.";

const TOPICS = [
  {
    "title": "What a Universal Database Generator Is",
    "subject": "universal database generator identity",
    "description": "A universal database generator is a program that creates new database systems: given a category, it researches what is needed, designs the specification, builds the database structure, generates the records, adds search and retrieval, writes the working code, builds the reusable generator, makes the website interface, writes the documentation, runs the demonstration, and tests the result. It.",
    "label": "universal-database-generator-identity",
    "figures": {
      "build_steps": 11,
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
    "title": "Accepting a New Category",
    "subject": "accepting a new category",
    "description": "Accepting a new category is the first step of the generator: the category arrives as a name and a short description, the generator checks that the name is plain and the description is real, and then it searches the live manifest, which is the master list of all databases, for anything that already covers it. A category that already exists is linked, never rebuilt, and a category that is.",
    "label": "accepting-new-category",
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
    "title": "Researching What Is Needed",
    "subject": "researching what is needed",
    "description": "Researching what is needed is the generator's discovery step: it retrieves the actual links and the full data behind them for existing resources, reads the relevant specifications, identifies existing capabilities and limitations, and records the source web address, the resource identifier, and the retrieval date for every resource it uses. Research follows the pull-links-and-full-data rule:.",
    "label": "researching-what-is-needed",
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
    "title": "Designing the Specification",
    "subject": "designing the specification",
    "description": "Designing the specification is the generator's planning step: from the research it writes the complete specification for the new database, with system identity, database structure, search and retrieval, working source code, reusable generator, website interface, documentation, demonstration, automated tests, validation results, version history, source provenance, and expansion instructions..",
    "label": "designing-specification",
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
    "title": "Building the Database Structure",
    "subject": "building the database structure",
    "description": "Building the database structure is the making of the record shape: the field list, the identifier prefix, the record kind, the required fields, and the rules that keep records complete. The structure is the mold every record is poured into, and a good mold makes good records easy and bad records hard. This record specifies the structure rules: every field named in plain words, required fields.",
    "label": "building-database-structure",
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
    "title": "Generating Records",
    "subject": "generating records",
    "description": "Generating records is the generator's making step: from the specification it creates complete records, each with every field filled, its own figures, its own demo, and its own sources, until the edition holds 24 records. Generation is seeded, so the same seed always produces the same records, and every generated record is checked by execution before it is filed. This record specifies the.",
    "label": "generating-records",
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
    "title": "Adding Search and Retrieval",
    "subject": "adding search and retrieval",
    "description": "Adding search and retrieval is the step that makes a generated database usable: an index over every word in every record, search by identifier, by title, by subject, and by full text, and every returned record carrying its sources and provenance. Search is built with the database, not bolted on after, because a database without search is a store with no door. This record specifies the search.",
    "label": "adding-search-retrieval",
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
    "title": "Writing the Working Code",
    "subject": "writing the working code",
    "description": "Writing the working code is the step that makes the database run: the demo that recomputes each record's figures twice, the program that wraps the same computation in a class, and the generator that creates new records on demand. The code must be real working code, not a description of code, and it must run on a plain machine with only the standard library, which is the set of tools that ships.",
    "label": "writing-working-code",
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
