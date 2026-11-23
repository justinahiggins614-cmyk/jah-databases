// Seeded boundless generator for the Universal Build Factory
// (public edition). Deterministic: the same seed always emits the same
// record. Usage: node gen-universal-build-factory.js [seed]  (prints one
// JSON record) or: node gen-universal-build-factory.js --test (runTests).
// Package-only; outputs are generated, not stored files.
"use strict";
const crypto = require("crypto");

const SLUG = "universal-build-factory";
const RECORD_KIND = "universal build factory record";
const ID_PREFIX = "JAH-UBF-";
const AI_NAME = "JAH Universal Build Factory Librarian";
const EDITION = "public";
const CEILING = "Generator ceiling: up to 1,000,000,000 scales per file, generated on demand by the file AI \u2014 not stored files.";

const TOPICS = [
  {
    "title": "Central Observability Dashboard",
    "subject": "central observability dashboard",
    "description": "A central observability dashboard tracks performance, errors, availability, resource use, and execution history for the whole network in one view. The dashboard shows what is running, what has failed, how much each part is using, and what happened over time, so a problem can be seen before it is felt. The dashboard is itself recorded: what it shows, where its numbers come from, and when it was.",
    "label": "central-observability-dashboard",
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
    "title": "Automatic Recovery and Disaster Planning",
    "subject": "automatic recovery and disaster planning",
    "description": "Automatic recovery and disaster planning detects failures, restores services, and recovers interrupted tasks. A failure is detected by a watch, the affected service is rebuilt from its backup or its recipe, and an interrupted task is restarted from its last recorded step. The plan for each kind of disaster is written in advance, tested by drills, and recorded with its date and result.",
    "label": "automatic-recovery-disaster-planning",
    "figures": {
      "checks": 7,
      "fields": 10,
      "steps": 7,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "glossary_terms": 53,
      "sections": 16,
      "topic_index": 2
    }
  },
  {
    "title": "Resource and Workload Management",
    "subject": "resource and workload management",
    "description": "Resource and workload management coordinates CPU, memory, storage, network access, queues, and concurrent jobs. The manager watches how much each job needs and how much is free, queues jobs when the system is full, and schedules them when room opens. Every allocation is recorded with its job, its amount, and its time, so a job that used too much can be found and its limits set.",
    "label": "resource-workload-management",
    "figures": {
      "checks": 5,
      "fields": 8,
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
    "title": "Build Pipeline Records",
    "subject": "build pipeline records",
    "description": "Build pipeline records are the written accounts of each build pipeline: its stages, their order, and what each stage does. A pipeline gathers the code, builds it, tests it, packages it, verifies it, and deploys it, in order, and each stage records its date and result. A pipeline that stops at a failed stage is recorded as stopped, with the stage named.",
    "label": "build-pipeline-records",
    "figures": {
      "checks": 6,
      "fields": 9,
      "steps": 6,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "glossary_terms": 53,
      "sections": 16,
      "topic_index": 4
    }
  },
  {
    "title": "Package Assembly Records",
    "subject": "package assembly records",
    "description": "Package assembly records are the dated accounts of gathering a project's parts into a package: which files, which components, which settings, and in what order. Each record names the project, the parts assembled, and the package produced, so the same package can be assembled again the same way. A package that fails its assembly checks is recorded as failing, with the check that caught it.",
    "label": "package-assembly-records",
    "figures": {
      "checks": 5,
      "fields": 8,
      "steps": 5,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "glossary_terms": 53,
      "sections": 16,
      "topic_index": 5
    }
  },
  {
    "title": "Executable Packaging Records",
    "subject": "executable packaging records",
    "description": "Executable packaging records are the dated accounts of turning a built project into an executable file: the program, its settings, its libraries, and the system it runs on. Each record names the executable, the system it was built for, the tests it passed, and the date it was packaged. An executable that fails its tests is never packaged.",
    "label": "executable-packaging-records",
    "figures": {
      "checks": 6,
      "fields": 9,
      "steps": 5,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "glossary_terms": 53,
      "sections": 16,
      "topic_index": 6
    }
  },
  {
    "title": "API Assembly Records",
    "subject": "API assembly records",
    "description": "API assembly records are the dated accounts of building an API, which stands for Application Programming Interface: the addresses it offers, the data it returns, the contract it keeps, and the tests it passed. Each record names the API, its version, its addresses, and the date it was assembled, so a program that uses it can check the version it was built against.",
    "label": "api-assembly-records",
    "figures": {
      "checks": 5,
      "fields": 8,
      "steps": 6,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "glossary_terms": 53,
      "sections": 16,
      "topic_index": 7
    }
  },
  {
    "title": "Application Launch Records",
    "subject": "application launch records",
    "description": "Application launch records are the dated accounts of starting a built application: which version was started, where it runs, what settings it used, and whether it started cleanly. Each launch is recorded with its date and result, and a launch that fails is recorded with its failure, so a bad version can be stopped before it reaches users.",
    "label": "application-launch-records",
    "figures": {
      "checks": 4,
      "fields": 7,
      "steps": 4,
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
    "name": "Wikipedia - Build automation",
    "url": "https://en.wikipedia.org/wiki/Build_automation",
    "establishes": "Build automation: how the steps of building software are run by a program instead of by hand.",
    "retrieved": "2026-11-18",
    "resource_id": "en.wikipedia.org/wiki/Build_automation"
  },
  {
    "name": "Wikipedia - Continuous integration",
    "url": "https://en.wikipedia.org/wiki/Continuous_integration",
    "establishes": "Continuous integration: how changes are built and tested together, often, so faults are found early.",
    "retrieved": "2026-11-18",
    "resource_id": "en.wikipedia.org/wiki/Continuous_integration"
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
