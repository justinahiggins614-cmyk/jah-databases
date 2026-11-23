// Seeded boundless generator for the Master AI Coordinator
// (signature edition). Deterministic: the same seed always emits the same
// record. Usage: node gen-master-ai-coordinator-signature.js [seed]  (prints one
// JSON record) or: node gen-master-ai-coordinator-signature.js --test (runTests).
// Package-only; outputs are generated, not stored files.
"use strict";
const crypto = require("crypto");

const SLUG = "master-ai-coordinator-signature";
const RECORD_KIND = "master ai coordinator record";
const ID_PREFIX = "JAH-MAICS-";
const AI_NAME = "JAH Master AI Coordinator Librarian (Signature)";
const EDITION = "signature";
const CEILING = "Generator ceiling: up to 1,000,000,000 scales per file, generated on demand by the file AI \u2014 not stored files.";

const TOPICS = [
  {
    "title": "The Registry Hall — Signature Design",
    "subject": "registry hall design",
    "description": "The Registry Hall is a Signature-made design for the specialist registry, imagined as a hall with one portrait per specialist. Each portrait shows the specialist's expertise, tools, and limits, written beneath it in plain words. The design shows how a registry could be walked: portraits in a hall, each with its card below.",
    "label": "registry-hall-design",
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
    "title": "The Message Bridge — Signature Design",
    "subject": "message bridge design",
    "description": "The Message Bridge is a Signature-made design for AI-to-AI communication, imagined as a bridge between two specialists, with each message a sealed letter carried across. The letters are logged in the bridge book with their dates, so a task can be followed from the first letter to the last. The design shows how messages could be carried: sealed, logged, and read only by the specialist named on.",
    "label": "message-bridge-design",
    "figures": {
      "checks": 3,
      "fields": 5,
      "steps": 5,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "glossary_terms": 53,
      "sections": 16,
      "topic_index": 2
    }
  },
  {
    "title": "The Planner's Table — Signature Design",
    "subject": "planner's table design",
    "description": "The Planner's Table is a Signature-made design for the master task planner, imagined as a great table where a large request is laid out and cut into tasks. Each task is a piece laid in order, with a card naming its specialist, and the pieces are handed out one by one. The design shows how planning could be seen: a whole laid out, cut into pieces, handed out in order.",
    "label": "planners-table-design",
    "figures": {
      "checks": 4,
      "fields": 6,
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
    "title": "The Shared Library — Signature Design",
    "subject": "shared library design",
    "description": "The Shared Library is a Signature-made design for shared knowledge memory, imagined as a library where every book is a validated fact with its source written on the first page. An AI that reads a book takes the fact and its source together, and no book enters the library until it is checked. The design shows how shared knowledge could be kept: books with sources on the first page, checked.",
    "label": "shared-library-design",
    "figures": {
      "checks": 3,
      "fields": 5,
      "steps": 4,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "glossary_terms": 53,
      "sections": 16,
      "topic_index": 4
    }
  },
  {
    "title": "The Disagreement Court — Signature Design",
    "subject": "disagreement court design",
    "description": "The Disagreement Court is a Signature-made design for disagreement resolution, imagined as a court where two conflicting answers stand with their evidence before a judge. The judge weighs the evidence in the open, and the conclusion is the answer whose evidence holds up. A disagreement that cannot be decided is recorded with both answers kept. The design shows how a disagreement could be.",
    "label": "disagreement-court-design",
    "figures": {
      "checks": 4,
      "fields": 6,
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
    "title": "The Evaluation Arena — Signature Design",
    "subject": "evaluation arena design",
    "description": "The Evaluation Arena is a Signature-made design for performance evaluation, imagined as an arena where each specialist is tested on accuracy, reasoning, retrieval, coding, and task completion. Each test is a round with named examples and a score, and the scores are written on the arena board with their dates. The design shows how evaluation could be watched: rounds in an arena, scores on a board.",
    "label": "evaluation-arena-design",
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
    "title": "The Discovery Lantern — Signature Design",
    "subject": "discovery lantern design",
    "description": "The Discovery Lantern is a Signature-made design for capability discovery, imagined as a lantern whose light falls on the specialists that can do a requested task. A request is spoken, the lantern is raised, and the light shows the candidates, with the chosen one lit brightest. The design shows how discovery could be seen: a light that finds the right specialist for the task.",
    "label": "discovery-lantern-design",
    "figures": {
      "checks": 3,
      "fields": 5,
      "steps": 4,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "glossary_terms": 53,
      "sections": 16,
      "topic_index": 7
    }
  },
  {
    "title": "The Decomposition Loom — Signature Design",
    "subject": "decomposition loom design",
    "description": "The Decomposition Loom is a Signature-made design for task decomposition, imagined as a loom where a large request is unraveled into threads, each thread a smaller task. The threads are laid in order and handed to their specialists, and the woven result is the finished request. The design shows how decomposition could be seen: a whole unraveled into threads, then woven back into a result.",
    "label": "decomposition-loom-design",
    "figures": {
      "checks": 4,
      "fields": 6,
      "steps": 5,
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
    "name": "Wikipedia - Multi-agent system",
    "url": "https://en.wikipedia.org/wiki/Multi-agent_system",
    "establishes": "Multi-agent system: how several AI programs work together on shared tasks.",
    "retrieved": "2026-11-18",
    "resource_id": "en.wikipedia.org/wiki/Multi-agent_system"
  },
  {
    "name": "Wikipedia - Automated planning and scheduling",
    "url": "https://en.wikipedia.org/wiki/Automated_planning_and_scheduling",
    "establishes": "Automated planning and scheduling: how a large task is broken into ordered steps.",
    "retrieved": "2026-11-18",
    "resource_id": "en.wikipedia.org/wiki/Automated_planning_and_scheduling"
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
