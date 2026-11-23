// Seeded boundless generator for the Automated Testing Generator
// (public edition). Deterministic: the same seed always emits the same
// record. Usage: node gen-automated-testing-generator.js [seed]  (prints one
// JSON record) or: node gen-automated-testing-generator.js --test (runTests).
// Package-only; outputs are generated, not stored files.
"use strict";
const crypto = require("crypto");

const SLUG = "automated-testing-generator";
const RECORD_KIND = "automated testing generator record";
const ID_PREFIX = "JAH-ATGN-";
const AI_NAME = "JAH Automated Testing Generator Librarian";
const EDITION = "public";
const CEILING = "Generator ceiling: up to 1,000,000,000 scales per file, generated on demand by the file AI \u2014 not stored files.";

const TOPICS = [
  {
    "title": "What an Automated Testing Generator Is",
    "subject": "automated testing generator identity",
    "description": "An automated testing generator is a program that creates automated test suites: given a program or a system, it writes unit tests that check one function at a time, integration tests that check functions working together, defect tests that check known faults, and regression tests that check old faults stay fixed. Automated means the tests run by themselves, with no hand-running, and report.",
    "label": "automated-testing-generator-identity",
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
    "title": "Unit Test Generation",
    "subject": "unit test generation",
    "description": "Unit test generation is the writing of tests that check one function at a time: for each function, the generator writes cases with known inputs and known outputs, runs them, and records which passed and which failed. A unit test that passes proves its function behaves as specified for its cases, and a unit test that fails points at the exact function that is wrong. This record specifies the.",
    "label": "unit-test-generation",
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
    "title": "Integration Test Generation",
    "subject": "integration test generation",
    "description": "Integration test generation is the writing of tests that check functions working together: the generator writes cases where one function's output feeds the next function's input, runs the chain, and records whether the whole chain behaves as specified. Integration tests catch what unit tests cannot: functions that are right alone and wrong together. This record specifies the integration rules:.",
    "label": "integration-test-generation",
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
    "title": "Defect Detection Tests",
    "subject": "defect detection tests",
    "description": "Defect detection tests are the tests that prove a test suite can catch faults: the generator plants a controlled defect, which is a fault put in on purpose, runs the suite, and confirms the suite catches it. A suite that cannot catch a planted defect cannot catch a real one. This record specifies the defect rules: plant one defect at a time, run the suite, confirm the catch, repair the defect,.",
    "label": "defect-detection-tests",
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
    "title": "Regression Test Generation",
    "subject": "regression test generation",
    "description": "Regression test generation is the writing of tests that check old faults stay fixed: for each fault ever found, the generator writes a test that fails when the fault returns, and the suite runs those tests on every change. Regression tests are the memory of a program: they remember what broke, so it cannot break again silently. This record specifies the regression rules: one test per fault,.",
    "label": "regression-test-generation",
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
    "title": "Test Data Generation",
    "subject": "test data generation",
    "description": "Test data generation is the making of the inputs that tests run on: known inputs with known outputs, edge cases that sit at the boundaries, and bad inputs that must fail cleanly. Good test data covers the ordinary, the edge, and the bad, because a test that only tries ordinary inputs only proves ordinary behavior. This record specifies the test-data rules: ordinary, edge, and bad inputs in.",
    "label": "test-data-generation",
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
    "title": "Test Oracles",
    "subject": "test oracles",
    "description": "A test oracle is the source of truth a test compares against: the known output for a known input, the specification that states what a program must do, or a second program that computes the same result a different way. A test without an oracle has nothing to compare its result to, and a result with nothing to compare to is not a verdict. This record specifies the oracle rules: every test has.",
    "label": "test-oracles",
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
    "title": "Test Coverage",
    "subject": "test coverage",
    "description": "Test coverage is the measure of how much of a program the tests actually run: which functions were called, which branches were taken, and which lines were executed. Coverage is measured by running the tests with a recorder that notes what ran, and a low coverage number is a plain statement that parts of the program were never tested. This record specifies the coverage rules: coverage measured.",
    "label": "test-coverage",
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
