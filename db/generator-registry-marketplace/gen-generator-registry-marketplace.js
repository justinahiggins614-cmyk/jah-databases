// Seeded boundless generator for the Generator Registry and Marketplace
// (public edition). Deterministic: the same seed always emits the same
// record. Usage: node gen-generator-registry-marketplace.js [seed]  (prints one
// JSON record) or: node gen-generator-registry-marketplace.js --test (runTests).
// Package-only; outputs are generated, not stored files.
"use strict";
const crypto = require("crypto");

const SLUG = "generator-registry-marketplace";
const RECORD_KIND = "generator registry marketplace record";
const ID_PREFIX = "JAH-GREG-";
const AI_NAME = "JAH Generator Registry and Marketplace Librarian";
const EDITION = "public";
const CEILING = "Generator ceiling: up to 1,000,000,000 scales per file, generated on demand by the file AI \u2014 not stored files.";

const TOPICS = [
  {
    "title": "Generator Dependency Manager",
    "subject": "generator dependency manager",
    "description": "A generator dependency manager identifies the components and resources each generator requires. A generator's dependency list names every library, file, database, and tool it needs, with the version of each, and the manager checks that all of them are present before the generator runs. A generator whose dependencies are missing or changed is not run, and the missing dependency is recorded.",
    "label": "generator-dependency-manager",
    "figures": {
      "checks": 6,
      "fields": 9,
      "steps": 5,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "glossary_terms": 53,
      "sections": 16,
      "topic_index": 1
    }
  },
  {
    "title": "Build and Deployment Manager",
    "subject": "build and deployment manager",
    "description": "A build and deployment manager turns generated projects into installable and runnable products. The build step gathers the code, the parts, and the settings into a package; the deployment step places the package where it can run, with its settings in place. Each step is recorded with its date and result, and a build that fails its tests is never deployed.",
    "label": "build-deployment-manager",
    "figures": {
      "checks": 5,
      "fields": 8,
      "steps": 6,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "glossary_terms": 53,
      "sections": 16,
      "topic_index": 2
    }
  },
  {
    "title": "Automated Regression Testing",
    "subject": "automated regression testing",
    "description": "Automated regression testing ensures a repair or upgrade does not break previous functionality. A regression suite is the collection of tests that passed before the change, and it is run again after the change; a test that passed before and fails now is a regression, and the change is not accepted until the regression is fixed. The suite and its results are recorded with their dates.",
    "label": "automated-regression-testing",
    "figures": {
      "checks": 7,
      "fields": 10,
      "steps": 6,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "glossary_terms": 53,
      "sections": 16,
      "topic_index": 3
    }
  },
  {
    "title": "Software Compatibility Testing",
    "subject": "software compatibility testing",
    "description": "Software compatibility testing tests operating systems, Python versions, hardware, and dependencies. A compatibility matrix names each combination that was tested and the result for each, so a user can see whether a generator works on their system before trying it. A combination that fails is recorded with its failure, and a combination that was never tested is recorded as untested, never.",
    "label": "software-compatibility-testing",
    "figures": {
      "checks": 6,
      "fields": 9,
      "steps": 5,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "glossary_terms": 53,
      "sections": 16,
      "topic_index": 4
    }
  },
  {
    "title": "API Contract Verification",
    "subject": "API contract verification",
    "description": "API contract verification checks that documented APIs actually exist and return the expected data. An API, which stands for Application Programming Interface, is a defined way for one program to ask another for data or work, and a contract is the written promise of what it will send and return. Verification calls the API with example requests and compares the answers with the contract; a.",
    "label": "api-contract-verification",
    "figures": {
      "checks": 5,
      "fields": 8,
      "steps": 6,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "glossary_terms": 53,
      "sections": 16,
      "topic_index": 5
    }
  },
  {
    "title": "Reusable Component Library",
    "subject": "reusable component library",
    "description": "A reusable component library preserves working modules so generators do not rebuild the same functions repeatedly. Each component is stored once, with its name, its purpose, its inputs and outputs, and its tests, and generators use it by reference instead of copying it. A component is tested when it is added and re-tested when it changes, and a component that fails its tests is marked as such.",
    "label": "reusable-component-library",
    "figures": {
      "checks": 6,
      "fields": 9,
      "steps": 4,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "glossary_terms": 53,
      "sections": 16,
      "topic_index": 6
    }
  },
  {
    "title": "Generator Catalog Records",
    "subject": "generator catalog records",
    "description": "Generator catalog records are the entries of the registry: one record per generator, naming its purpose, its inputs, its outputs, its record kind, its dependencies, and its tests. A catalog record is written when a generator is listed and updated when it changes, and it is the first thing a reader sees before deciding to run a generator.",
    "label": "generator-catalog-records",
    "figures": {
      "checks": 5,
      "fields": 8,
      "steps": 5,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "glossary_terms": 53,
      "sections": 16,
      "topic_index": 7
    }
  },
  {
    "title": "Generator Inspection Reports",
    "subject": "generator inspection reports",
    "description": "Generator inspection reports are the written accounts of reading a generator before running it: its code, its dependencies, its tests, and its past runs, checked against its catalog record. Each report names the generator, the inspector, the date, and the findings, and a generator with findings that matter is not run until they are addressed.",
    "label": "generator-inspection-reports",
    "figures": {
      "checks": 6,
      "fields": 9,
      "steps": 6,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "glossary_terms": 53,
      "sections": 16,
      "topic_index": 8
    }
  }
];

const SOURCES = [
  {
    "name": "Wikipedia - Software repository",
    "url": "https://en.wikipedia.org/wiki/Software_repository",
    "establishes": "Software repository: how software and its parts are stored, listed, and fetched.",
    "retrieved": "2026-11-18",
    "resource_id": "en.wikipedia.org/wiki/Software_repository"
  },
  {
    "name": "Wikipedia - Package manager",
    "url": "https://en.wikipedia.org/wiki/Package_manager",
    "establishes": "Package manager: how software packages are installed, updated, and removed.",
    "retrieved": "2026-11-18",
    "resource_id": "en.wikipedia.org/wiki/Package_manager"
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
