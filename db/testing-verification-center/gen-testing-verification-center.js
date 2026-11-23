// Seeded boundless generator for the testing-verification-center database
// (public edition). Deterministic: the same seed always emits the same
// record. Usage: node gen-testing-verification-center.js [seed]  (prints one
// JSON record) or: node gen-testing-verification-center.js --test (runTests).
// Package-only; outputs are generated, not stored files.
// Attribution: this system was proposed in another AI's review pasted
// 2026-11-18; source unconfirmed, NOT Manon's words.
"use strict";
const crypto = require("crypto");

const SLUG = "testing-verification-center";
const RECORD_KIND = "testing and verification center record";
const ID_PREFIX = "JAH-TVC-";
const AI_NAME = "JAH Testing and Verification Librarian";
const EDITION = "public";
const SRC = "public-harvest";
const CEILING = "Generator ceiling: up to 1,000,000,000 scales per file, generated on demand by the file AI \u2014 not stored files.";
const DISCLAIMER = " Generated content is never presented as an authentic public record; Signature records are design studies, never established fact.";

const TOPICS = [{"title": "Testing and Verification Center: Overview and Mission", "subject": "Testing and Verification Center overview", "description": "The Testing and Verification Center is the network's permanent home for checking that things work: every database, generator, website, and program passes through it before it is called finished. The center keeps one shared test method for the whole network, so a result from one database can be compared with a result from another. Nothing in the center runs a live service: it holds test specifications, test cases, test results, and evidence reports as records.", "figures": {"test_areas": 24, "evidence_rungs": 9, "test_types": 12, "report_fields": 14}, "label": "testing-verification-center-01"}, {"title": "Testing and Verification Center: Unit Testing", "subject": "Testing one small piece at a time", "description": "A unit test checks one small piece of code on its own, for example one function that adds two numbers, so a failure points at exactly one place. Unit tests run fast and run often: the usual practice is to run them on every change, before the change is accepted. A good unit test states its input, the expected output, and nothing else, so the test itself is a readable record of what the code must do.", "figures": {"example_inputs": 5, "assertions": 8, "run_seconds": 3, "failure_points": 1}, "label": "testing-verification-center-02"}, {"title": "Testing and Verification Center: Integration Testing", "subject": "Testing pieces working together", "description": "An integration test checks that two or more pieces work together, for example that a generator's output can be read back by the database that stores it. Integration failures usually come from mismatched expectations between pieces: one piece sends a date as text, the other expects a number. The center records the contract between pieces first, then tests that contract, so the test catches drift instead of discovering it by accident.", "figures": {"piece_pairs": 6, "contracts": 6, "mismatch_types": 4, "test_cases": 18}, "label": "testing-verification-center-03"}, {"title": "Testing and Verification Center: System Testing", "subject": "Testing the whole thing end to end", "description": "A system test runs the whole product the way a real user would, from the first click to the finished result, with no shortcuts. System tests catch problems that unit and integration tests cannot see, such as a page that works but takes so long that nobody waits for it. Every system test in this center names the exact starting state, the exact steps, and the exact expected ending state.", "figures": {"user_journeys": 7, "steps_per_journey": 9, "expected_states": 7, "defects_found": 3}, "label": "testing-verification-center-04"}, {"title": "Testing and Verification Center: Acceptance Testing", "subject": "Checking the work meets its order", "description": "An acceptance test answers one question: does this do what was ordered, in the words of the order, with nothing missing and nothing extra. Acceptance tests are written from the order itself, not from the code, so they cannot be bent to match whatever the code happens to do. A record passes acceptance only when every acceptance test passes and the evidence report is attached.", "figures": {"acceptance_rules": 10, "orders_checked": 4, "missing_items": 0, "extra_items": 0}, "label": "testing-verification-center-05"}, {"title": "Testing and Verification Center: Regression Testing", "subject": "Making sure a fix breaks nothing old", "description": "A regression test re-runs old tests after a change, to prove the change did not break something that used to work. The center keeps the full regression set for every database, so a repair in one place is checked against every place it could touch. A regression failure stops the change: the repair is redone until the old tests pass again.", "figures": {"old_tests_rerun": 120, "changed_files": 2, "new_failures": 0, "retries_allowed": 3}, "label": "testing-verification-center-06"}, {"title": "Testing and Verification Center: Performance and Load Testing", "subject": "Checking speed and size under pressure", "description": "A performance test measures how long a task takes and how much memory it uses, under a stated load, for example one hundred records at once. A load test raises the load step by step until something slows down or fails, and records the exact load where that happens. No performance claim in this center is accepted without the load, the machine, and the measured time written down next to it.", "figures": {"load_steps": 6, "records_per_step": 100, "max_seconds": 30, "memory_mb": 512}, "label": "testing-verification-center-07"}, {"title": "Testing and Verification Center: Compatibility Testing", "subject": "Checking the work on many systems", "description": "A compatibility test runs the same program on different operating systems, different Python versions, and different hardware, and compares results. Compatibility failures are usually small: a path written for one system that does not exist on another, or a version that changed one behaviour. The center records the exact versions tested, because untested means unknown, not working.", "figures": {"operating_systems": 3, "python_versions": 3, "hardware_types": 2, "version_pairs": 18}, "label": "testing-verification-center-08"}];

const SOURCES = [{"name": "National Institute of Standards and Technology (NIST) \u2014 software assurance and testing guidance", "url": "https://www.nist.gov/", "establishes": "Source for generated records in this edition.", "retrieved": "2026-11-18", "status": 200}, {"name": "International Software Testing Qualifications Board (ISTQB) \u2014 software testing syllabus and glossary", "url": "https://www.istqb.org/", "establishes": "Source for generated records in this edition.", "retrieved": "2026-11-18", "status": 200}, {"name": "World Wide Web Consortium (W3C) Web Accessibility Initiative (WAI)", "url": "https://www.w3.org/WAI/", "establishes": "Source for generated records in this edition.", "retrieved": "2026-11-18", "status": 200}, {"name": "International Organization for Standardization (ISO) \u2014 standards catalogue", "url": "https://www.iso.org/", "establishes": "Source for generated records in this edition.", "retrieved": "2026-11-18", "status": null}];

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
  const count = keys.length;
  const mean = (total / count).toFixed(1);
  const out = { count: count, label: label, max: Math.max(...keys.map((k) => figs[k])), mean: mean, min: Math.min(...keys.map((k) => figs[k])), total: total };
  const result = Object.keys(out).sort().map((k) => k + "=" + out[k]).join("|");
  const h = crypto.createHash("sha256").update(result).digest("hex");
  const figsPy = "FIGURES = {" + keys.map((k) => JSON.stringify(k) + ": " + figs[k]).join(", ") + "}\nLABEL = " + JSON.stringify(label) + "\n";
  const code = "import hashlib\n" + figsPy +
    "from decimal import Decimal, ROUND_HALF_UP\n" +
    "total = sum(FIGURES.values())\n" +
    "count = len(FIGURES)\n" +
    "mean = str((Decimal(total) / Decimal(count)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP))\n" +
    "mn = min(FIGURES.values())\n" +
    "mx = max(FIGURES.values())\n" +
    "print('count: %d' % count)\n" +
    "print('label: %s' % LABEL)\n" +
    "print('max: %d' % mx)\n" +
    "print('mean: %s' % mean)\n" +
    "print('min: %d' % mn)\n" +
    "print('total: %d' % total)\n" +
    "result = 'count=%d|label=%s|max=%d|mean=%s|min=%d|total=%d' % (count, LABEL, mx, mean, mn, total)\n" +
    "print('Result: %s' % result)\n" +
    "print('Run 1 SHA-256: %s' % hashlib.sha256(result.encode()).hexdigest())\n";
  const expected = Object.keys(out).sort().map((k) => k + ": " + out[k]).join("\n") + "\n" +
    "Result: " + result + "\n" +
    "Run 1 SHA-256: " + h + "\n";
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
    src: SRC,
    ai_name: AI_NAME,
    description: topic.description + " No claim of a proven breakthrough, of flight readiness, or of deployment readiness is established by this generated record." + DISCLAIMER,
    body: "<h2>Description</h2><p>" + topic.description + "</p>",
    demo: demo.code,
    expected_output: demo.expected,
    program: "class GeneratedProgram:\n    def run(self):\n        return {\"deterministic\": True}\n",
    sources: SOURCES,
    generator: { type: "seeded boundless generator", gen_id_prefix: ID_PREFIX + "GEN-", hard_stop: 1000000000, throttle_per_call: 100, ceiling_note: CEILING },
    scales: { A1: "One generated record on this topic.", A2: "The pair: generated records extend the 24 filed records.", A3: "The network: every database a knowledge source, every generator a tool." },
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
