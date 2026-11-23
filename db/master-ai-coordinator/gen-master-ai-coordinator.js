// Seeded boundless generator for the Master AI Coordinator
// (public edition). Deterministic: the same seed always emits the same
// record. Usage: node gen-master-ai-coordinator.js [seed]  (prints one
// JSON record) or: node gen-master-ai-coordinator.js --test (runTests).
// Package-only; outputs are generated, not stored files.
"use strict";
const crypto = require("crypto");

const SLUG = "master-ai-coordinator";
const RECORD_KIND = "master ai coordinator record";
const ID_PREFIX = "JAH-MAIC-";
const AI_NAME = "JAH Master AI Coordinator Librarian";
const EDITION = "public";
const CEILING = "Generator ceiling: up to 1,000,000,000 scales per file, generated on demand by the file AI \u2014 not stored files.";

const TOPICS = [
  {
    "title": "AI Specialist Registry",
    "subject": "AI specialist registry",
    "description": "An AI specialist registry catalogs every AI in the network: its expertise, its instructions, its available tools, and its limitations. Each registry entry names the specialist, what it does well, what it cannot do, and how to reach it. The registry is the first place the coordinator looks when a task needs a specialist, and it is updated when a specialist is created, changed, or retired.",
    "label": "ai-specialist-registry",
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
    "title": "AI-to-AI Communication",
    "subject": "AI-to-AI communication",
    "description": "AI-to-AI communication lets specialist AIs exchange structured tasks and results. A message names the sender, the receiver, the task, and the result, and it is written in a shared format so any specialist can read any message. Messages are logged with their dates, so a task can be followed from the first request to the last result, and a message that cannot be read is recorded as such.",
    "label": "ai-to-ai-communication",
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
    "title": "Master Task Planner",
    "subject": "master task planner",
    "description": "A master task planner breaks large requests into smaller tasks and assigns them to appropriate systems. A plan names the whole request, the tasks it is broken into, the order they must run in, and the specialist assigned to each. The plan is recorded before work starts, and each task reports its result back to the plan, so the coordinator can see which tasks are done, which are running, and.",
    "label": "master-task-planner",
    "figures": {
      "checks": 7,
      "fields": 10,
      "steps": 7,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "glossary_terms": 53,
      "sections": 16,
      "topic_index": 3
    }
  },
  {
    "title": "Shared Knowledge Memory",
    "subject": "shared knowledge memory",
    "description": "Shared knowledge memory lets authorized AIs reuse validated knowledge without losing its source. Knowledge enters the memory only after it is validated: checked against its sources and recorded with its provenance. An AI that reads from the memory receives the fact and its source together, so the fact can be checked again. Knowledge that fails validation never enters the memory.",
    "label": "shared-knowledge-memory",
    "figures": {
      "checks": 5,
      "fields": 8,
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
    "title": "AI Disagreement Resolution",
    "subject": "AI disagreement resolution",
    "description": "AI disagreement resolution compares conflicting answers and requires evidence before selecting a conclusion. When two specialists answer differently, each answer is recorded with its evidence, the evidence is compared, and the conclusion is the answer whose evidence holds up. A disagreement that cannot be resolved by evidence is recorded as unresolved, with both answers kept, never decided by.",
    "label": "ai-disagreement-resolution",
    "figures": {
      "checks": 6,
      "fields": 9,
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
    "title": "AI Performance Evaluation",
    "subject": "AI performance evaluation",
    "description": "AI performance evaluation tests accuracy, reasoning, retrieval, coding, and task completion for every specialist. Each test names what it measures, the examples it uses, and the score it produced, and the results are recorded with their date so a specialist can be compared with itself over time and with others. A specialist that fails a test is recorded as failing, and the failure names the.",
    "label": "ai-performance-evaluation",
    "figures": {
      "checks": 5,
      "fields": 8,
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
    "title": "AI Capability Discovery",
    "subject": "AI capability discovery",
    "description": "AI capability discovery identifies which AI or generator can accomplish a requested task. A request names what is needed, and discovery searches the registry and the generator catalog for specialists and generators whose recorded capabilities match. The discovery is recorded with the request, the candidates found, and the one chosen, so a later reader can see why that specialist was picked.",
    "label": "ai-capability-discovery",
    "figures": {
      "checks": 4,
      "fields": 7,
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
    "title": "Task Decomposition Records",
    "subject": "task decomposition records",
    "description": "Task decomposition records are the written breakdowns of large requests into smaller tasks. Each record names the whole request, the tasks it became, the order they run in, and the specialist for each. A decomposition is checked before work starts: every task must be small enough for its assignee, and the tasks together must cover the whole request. A request that cannot be decomposed is.",
    "label": "task-decomposition-records",
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
