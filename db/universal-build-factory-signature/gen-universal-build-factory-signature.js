// Seeded boundless generator for the Universal Build Factory
// (signature edition). Deterministic: the same seed always emits the same
// record. Usage: node gen-universal-build-factory-signature.js [seed]  (prints one
// JSON record) or: node gen-universal-build-factory-signature.js --test (runTests).
// Package-only; outputs are generated, not stored files.
"use strict";
const crypto = require("crypto");

const SLUG = "universal-build-factory-signature";
const RECORD_KIND = "universal build factory record";
const ID_PREFIX = "JAH-UBFS-";
const AI_NAME = "JAH Universal Build Factory Librarian (Signature)";
const EDITION = "signature";
const CEILING = "Generator ceiling: up to 1,000,000,000 scales per file, generated on demand by the file AI \u2014 not stored files.";

const TOPICS = [
  {
    "title": "The Observatory — Signature Design",
    "subject": "observatory design",
    "description": "The Observatory is a Signature-made design for the central observability dashboard, imagined as a tower with a great window looking over the whole network. From the window, performance, errors, availability, resources, and history are all seen at once, and a failing part is a light that dims. The design shows how observability could be a tower: one window, the whole network, seen at once.",
    "label": "observatory-design",
    "figures": {
      "checks": 3,
      "fields": 5,
      "steps": 4,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "glossary_terms": 53,
      "sections": 16,
      "topic_index": 1
    }
  },
  {
    "title": "The Recovery Map — Signature Design",
    "subject": "recovery map design",
    "description": "The Recovery Map is a Signature-made design for automatic recovery and disaster planning, imagined as a map with one road home for every kind of failure. When a service fails, the map shows the road: rebuild from backup, restart the task, check the result. The design shows how recovery could be a map: roads home, drawn in advance, walked in drills.",
    "label": "recovery-map-design",
    "figures": {
      "checks": 4,
      "fields": 6,
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
    "title": "The Workload Mill — Signature Design",
    "subject": "workload mill design",
    "description": "The Workload Mill is a Signature-made design for resource and workload management, imagined as a mill where jobs are grain and resources are the grinding stones. The miller watches the grain, queues what the stones cannot grind yet, and records every grinding. The design shows how workload could be a mill: grain, stones, queues, and a miller who watches.",
    "label": "workload-mill-design",
    "figures": {
      "checks": 3,
      "fields": 5,
      "steps": 5,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "glossary_terms": 53,
      "sections": 16,
      "topic_index": 3
    }
  },
  {
    "title": "The Pipeline River — Signature Design",
    "subject": "pipeline river design",
    "description": "The Pipeline River is a Signature-made design for build pipeline records, imagined as a river with one lock per stage: gather, build, test, package, verify, deploy. Each lock is opened in turn, and the build floats through; a lock that will not open is a failed stage, and the river stops there. The design shows how a pipeline could be a river: locks in order, opened in turn.",
    "label": "pipeline-river-design",
    "figures": {
      "checks": 4,
      "fields": 6,
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
    "title": "The Assembly Bench — Signature Design",
    "subject": "assembly bench design",
    "description": "The Assembly Bench is a Signature-made design for package assembly records, imagined as a workbench where a project's parts are laid out in order and joined into a package. Each assembly is written in the bench book with its parts and its date, so the same package can be built again the same way. The design shows how assembly could be a bench: parts laid out, joined, and written down.",
    "label": "assembly-bench-design",
    "figures": {
      "checks": 3,
      "fields": 5,
      "steps": 4,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "glossary_terms": 53,
      "sections": 16,
      "topic_index": 5
    }
  },
  {
    "title": "The Executable Press — Signature Design",
    "subject": "executable press design",
    "description": "The Executable Press is a Signature-made design for executable packaging records, imagined as a press that stamps a built project into an executable file. The press is set for one target system, and each pressing is recorded with its date and its tests. The design shows how packaging could be a press: set, stamped, recorded.",
    "label": "executable-press-design",
    "figures": {
      "checks": 3,
      "fields": 5,
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
    "title": "The API Loom — Signature Design",
    "subject": "api loom design",
    "description": "The API Loom is a Signature-made design for API assembly records, imagined as a loom where an API, which stands for Application Programming Interface, is woven from its addresses. Each address is a thread, and the woven cloth is the API with its version and contract. The design shows how an API could be woven: threads of addresses, a cloth with a version.",
    "label": "api-loom-design",
    "figures": {
      "checks": 3,
      "fields": 5,
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
    "title": "The Launch Gate — Signature Design",
    "subject": "launch gate design",
    "description": "The Launch Gate is a Signature-made design for application launch records, imagined as a gate through which each built application passes when it starts. The gatekeeper writes the version, the place, the settings, and the result in the gate book, and a launch that fails is written in red. The design shows how a launch could be a gate: passed through, written down, in a book.",
    "label": "launch-gate-design",
    "figures": {
      "checks": 3,
      "fields": 5,
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
