// Seeded boundless generator for the Software Code Database
// (signature edition). Deterministic: the same seed always emits the same
// record. Usage: node gen-software-code-signature.js [seed]  (prints one
// JSON record) or: node gen-software-code-signature.js --test (runTests).
// Package-only; outputs are generated, not stored files.
"use strict";
const crypto = require("crypto");

const SLUG = "software-code-signature";
const RECORD_KIND = "software code record";
const ID_PREFIX = "JAH-SFCDS-";
const AI_NAME = "JAH Software Code Librarian (Signature)";
const EDITION = "signature";
const CEILING = "Generator ceiling: up to 1,000,000,000 scales per file, generated on demand by the file AI \u2014 not stored files.";

const TOPICS = [
  {
    "title": "Signature Code Library",
    "subject": "signature code library",
    "description": "The Signature Code Library is a design for a library where reusable programs live: each program on its shelf with its purpose, its inputs, its outputs, its tests, and its license note, so a builder can take a program and use it without rewriting it. The design imagines code as books, where every book on the shelf must open and read.",
    "label": "signature-code-library",
    "figures": {
      "library_parts": 4,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "glossary_terms": 27,
      "sections": 14,
      "hard_stop": 1000000000,
      "languages": 3
    }
  },
  {
    "title": "Signature Reuse Workshop",
    "subject": "signature reuse workshop",
    "description": "The Signature Reuse Workshop is a design for a workshop where programs are made reusable: arguments in, results out, errors clear, and tests included, so a program written once can be used a hundred times. The design imagines reuse as workshop craft, where a tool made once and used a hundred times is a hundred tools never made.",
    "label": "signature-reuse-workshop",
    "figures": {
      "reuse_parts": 4,
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
    "title": "Signature Shelf Rows",
    "subject": "signature shelf rows",
    "description": "The Signature Shelf Rows are a design for rows of shelves where libraries live: string tools in one row, file tools in another, math tools in a third, so a builder who needs a tool knows which row to walk down. The design imagines libraries as shelf rows, where a builder searches by purpose and never by author.",
    "label": "signature-shelf-rows",
    "figures": {
      "libraries": 6,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "glossary_terms": 27,
      "sections": 14,
      "hard_stop": 1000000000,
      "programs": 24
    }
  },
  {
    "title": "Signature Module Chest",
    "subject": "signature module chest",
    "description": "The Signature Module Chest is a design for a chest where modules are kept: one file per drawer, one job per function, and every function named in plain words. The design imagines modules as drawers, where a drawer that holds everything holds nothing findable.",
    "label": "signature-module-chest",
    "figures": {
      "module_rules": 3,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "glossary_terms": 27,
      "sections": 14,
      "hard_stop": 1000000000,
      "functions": 8
    }
  },
  {
    "title": "Signature Object Garden",
    "subject": "signature object garden",
    "description": "The Signature Object Garden is a design for a garden where classes grow: a class is a seed, an object is the plant that grows from it, and each plant holds its own data and its own methods. The design imagines classes as seeds, where a record class grows records and a generator class grows generators.",
    "label": "signature-object-garden",
    "figures": {
      "class_parts": 4,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "glossary_terms": 27,
      "sections": 14,
      "hard_stop": 1000000000,
      "methods": 3
    }
  },
  {
    "title": "Signature Interface Door",
    "subject": "signature interface door",
    "description": "The Signature Interface Door is a design for a door between programs: an API (Application Programming Interface) with a small set of calls, named in plain words, documented, and versioned, so programs that knock on it are not broken when the room behind it changes. The design imagines an interface as a door, where a door that changes shape without warning traps everyone who uses it.",
    "label": "signature-interface-door",
    "figures": {
      "interface_parts": 4,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "glossary_terms": 27,
      "sections": 14,
      "hard_stop": 1000000000,
      "versions": 2
    }
  },
  {
    "title": "Signature Manual Press",
    "subject": "signature manual press",
    "description": "The Signature Manual Press is a design for a press that prints code documentation: the purpose of each module, the job of each function, the meaning of each argument, and a worked example, all in plain words with every term defined. The design imagines documentation as printing, where a machine without instructions cannot be used.",
    "label": "signature-manual-press",
    "figures": {
      "doc_parts": 4,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "glossary_terms": 27,
      "sections": 14,
      "examples": 1,
      "hard_stop": 1000000000
    }
  },
  {
    "title": "Signature Test Bench",
    "subject": "signature test bench",
    "description": "The Signature Test Bench is a design for a bench where code is tested: unit tests that check one function at a time, integration tests that check functions working together, and the demo that recomputes the figures twice. The design imagines testing as bench work, where a program that fails its tests is not filed until it passes.",
    "label": "signature-test-bench",
    "figures": {
      "test_kinds": 3,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "glossary_terms": 27,
      "sections": 14,
      "checks": 6,
      "hard_stop": 1000000000
    }
  }
];

const SOURCES = [
  {
    "name": "Wikipedia - Python (programming language)",
    "url": "https://en.wikipedia.org/wiki/Python_(programming_language)",
    "establishes": "Python (programming language): the language used for working programs in this network.",
    "retrieved": "2026-11-17",
    "resource_id": "en.wikipedia.org/wiki/Python_(programming_language)"
  },
  {
    "name": "Wikipedia - Software development",
    "url": "https://en.wikipedia.org/wiki/Software_development",
    "establishes": "Software development: how programs are built, tested, and maintained.",
    "retrieved": "2026-11-17",
    "resource_id": "en.wikipedia.org/wiki/Software_development"
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
