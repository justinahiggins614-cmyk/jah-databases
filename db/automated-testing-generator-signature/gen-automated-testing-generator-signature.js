// Seeded boundless generator for the Automated Testing Generator
// (signature edition). Deterministic: the same seed always emits the same
// record. Usage: node gen-automated-testing-generator-signature.js [seed]  (prints one
// JSON record) or: node gen-automated-testing-generator-signature.js --test (runTests).
// Package-only; outputs are generated, not stored files.
"use strict";
const crypto = require("crypto");

const SLUG = "automated-testing-generator-signature";
const RECORD_KIND = "automated testing generator record";
const ID_PREFIX = "JAH-ATGNS-";
const AI_NAME = "JAH Automated Testing Generator Librarian (Signature)";
const EDITION = "signature";
const CEILING = "Generator ceiling: up to 1,000,000,000 scales per file, generated on demand by the file AI \u2014 not stored files.";

const TOPICS = [
  {
    "title": "Signature Test Forge",
    "subject": "signature test forge",
    "description": "The Signature Test Forge is a design for a forge where test suites are hammered out: unit tests, integration tests, defect tests, and regression tests, each one struck until it runs by itself and reports pass or fail. The design imagines testing as forging, where a suite that cannot catch a planted defect is iron never tempered.",
    "label": "signature-test-forge",
    "figures": {
      "test_kinds": 4,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "glossary_terms": 27,
      "sections": 14,
      "hard_stop": 1000000000,
      "live_records": 20
    }
  },
  {
    "title": "Signature Single Anvil",
    "subject": "signature single anvil",
    "description": "The Signature Single Anvil is a design for an anvil where one function is tested at a time: known inputs, known outputs, and a verdict for each case. The design imagines unit testing as an anvil, where a function never tested alone can only be blamed as part of a whole.",
    "label": "signature-single-anvil",
    "figures": {
      "cases_per_function": 3,
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
    "title": "Signature Chain Bench",
    "subject": "signature chain bench",
    "description": "The Signature Chain Bench is a design for a bench where functions are tested working together: one function's output feeds the next function's input, and the whole chain is run to see whether it behaves as specified. The design imagines integration testing as a bench, where functions right alone and wrong together are caught.",
    "label": "signature-chain-bench",
    "figures": {
      "chain_steps": 3,
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
    "title": "Signature Planted Thorn",
    "subject": "signature planted thorn",
    "description": "The Signature Planted Thorn is a design for a thorn planted on purpose to test a suite: the generator puts a controlled defect in, runs the suite, and confirms the suite catches it. The design imagines defect detection as a thorn, where a suite that cannot catch a planted thorn cannot catch a real one.",
    "label": "signature-planted-thorn",
    "figures": {
      "defect_steps": 5,
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
    "title": "Signature Memory Wall",
    "subject": "signature memory wall",
    "description": "The Signature Memory Wall is a design for a wall where old faults are remembered: for each fault ever found, a test is written that fails when the fault returns, and the wall is checked on every change. The design imagines regression tests as a wall of memory, where a fault fixed without a test will return.",
    "label": "signature-memory-wall",
    "figures": {
      "regression_parts": 3,
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
    "title": "Signature Test Pantry",
    "subject": "signature test pantry",
    "description": "The Signature Test Pantry is a design for a pantry where test data is kept: known inputs with known outputs, edge cases at the boundaries, and bad inputs that must fail cleanly. The design imagines test data as a pantry, where a test with no known output cannot pass or fail.",
    "label": "signature-test-pantry",
    "figures": {
      "data_kinds": 3,
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
    "title": "Signature Truth Stone",
    "subject": "signature truth stone",
    "description": "The Signature Truth Stone is a design for a stone against which test results are compared: the known output for a known input, the specification, or a second program that computes the same result a different way. The design imagines an oracle as a stone, where a test that compares a program against itself always passes and tests nothing.",
    "label": "signature-truth-stone",
    "figures": {
      "oracle_kinds": 3,
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
    "title": "Signature Coverage Net",
    "subject": "signature coverage net",
    "description": "The Signature Coverage Net is a design for a net that shows how much of a program the tests actually ran: which functions were called, which branches were taken, and which lines were executed. The design imagines coverage as a net, where a low number is a plain statement that parts of the program were never tested.",
    "label": "signature-coverage-net",
    "figures": {
      "coverage_parts": 3,
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
    "name": "Wikipedia - Software testing",
    "url": "https://en.wikipedia.org/wiki/Software_testing",
    "establishes": "Software testing: how programs are checked by running them.",
    "retrieved": "2026-11-17",
    "resource_id": "en.wikipedia.org/wiki/Software_testing"
  },
  {
    "name": "Wikipedia - Unit testing",
    "url": "https://en.wikipedia.org/wiki/Unit_testing",
    "establishes": "Unit testing: how one function at a time is checked.",
    "retrieved": "2026-11-17",
    "resource_id": "en.wikipedia.org/wiki/Unit_testing"
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
