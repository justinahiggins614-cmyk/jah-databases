// Seeded boundless generator for the AI Specialist Generator
// (public edition). Deterministic: the same seed always emits the same
// record. Usage: node gen-ai-specialist-generator.js [seed]  (prints one
// JSON record) or: node gen-ai-specialist-generator.js --test (runTests).
// Package-only; outputs are generated, not stored files.
"use strict";
const crypto = require("crypto");

const SLUG = "ai-specialist-generator";
const RECORD_KIND = "ai specialist generator record";
const ID_PREFIX = "JAH-AISG-";
const AI_NAME = "JAH AI Specialist Generator Librarian";
const EDITION = "public";
const CEILING = "Generator ceiling: up to 1,000,000,000 scales per file, generated on demand by the file AI \u2014 not stored files.";

const TOPICS = [
  {
    "title": "What an AI Specialist Generator Is",
    "subject": "ai specialist generator identity",
    "description": "An AI specialist generator is a program that creates specialist AI (artificial intelligence) systems: given a specialty, such as mathematics, medicine, law, or engineering, it builds a system that knows that specialty, reasons over its records, answers questions in it, and checks its own answers against its tests. A specialist is narrow on purpose: it knows one field deeply instead of all.",
    "label": "ai-specialist-generator-identity",
    "figures": {
      "generator_parts": 4,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "glossary_terms": 27,
      "sections": 14,
      "hard_stop": 1000000000,
      "specialties": 12
    }
  },
  {
    "title": "Choosing a Specialty",
    "subject": "choosing a specialty",
    "description": "Choosing a specialty is the first step of the generator: the specialty arrives as a name and a short description, the generator checks that the specialty is real and that the network holds records for it, and only then is the specialty accepted for building. A specialty with no records is a specialist with nothing to know, and a specialist with nothing to know invents. This record specifies.",
    "label": "choosing-specialty",
    "figures": {
      "specialty_steps": 4,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "glossary_terms": 27,
      "sections": 14,
      "hard_stop": 1000000000,
      "specialties": 12
    }
  },
  {
    "title": "Building the Knowledge Base",
    "subject": "building the knowledge base",
    "description": "Building the knowledge base is the gathering of the specialty's records: the generator retrieves the actual links and the full data behind them from the network's databases, checks each record against its sources, and files the checked records as the specialist's knowledge. The knowledge base is built from the network's own records, never from invented knowledge, and every record in it carries.",
    "label": "building-knowledge-base",
    "figures": {
      "kb_steps": 4,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "glossary_terms": 27,
      "sections": 14,
      "hard_stop": 1000000000,
      "specialties": 12
    }
  },
  {
    "title": "Writing the Rule Set",
    "subject": "writing the rule set",
    "description": "A rule set is the specialist's reasoning written as rules: if this is true, then that follows, with each rule named, sourced, and tested. Rules are how a specialist reasons instead of guessing, and a rule that cannot be traced to a record is a guess wearing a rule's clothes. This record specifies the rule rules: every rule named, every rule sourced, every rule tested, and no rule ever filed.",
    "label": "writing-rule-set",
    "figures": {
      "rule_parts": 3,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "glossary_terms": 27,
      "sections": 14,
      "hard_stop": 1000000000,
      "specialties": 12
    }
  },
  {
    "title": "Answering in Natural Sentences",
    "subject": "answering in natural sentences",
    "description": "Answering in natural sentences is the rule that a specialist talks like a human: full sentences, plain words, and the records it used named in the answer, never templated blocks and never bare claims. A specialist that answers in blocks sounds like a form, and a form cannot be questioned. This record specifies the answer rules: natural sentences, records named, and an honest no when the.",
    "label": "answering-natural-sentences",
    "figures": {
      "answer_parts": 3,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "glossary_terms": 27,
      "sections": 14,
      "hard_stop": 1000000000,
      "specialties": 12
    }
  },
  {
    "title": "Evaluating a Specialist",
    "subject": "evaluating a specialist",
    "description": "Evaluating a specialist is the testing of its answers against its specialty's tests: questions with known answers, drawn from the specialty's records, where the specialist must answer correctly and name its records. A specialist that fails its evaluation is not filed until it passes. This record specifies the evaluation rules: known-answer questions, records named, and zero failures allowed on.",
    "label": "evaluating-specialist",
    "figures": {
      "evaluation_parts": 4,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "glossary_terms": 27,
      "sections": 14,
      "checks": 6,
      "hard_stop": 1000000000
    }
  },
  {
    "title": "Specialist Honesty Limits",
    "subject": "specialist honesty limits",
    "description": "Honesty limits are the lines a specialist never crosses: it never claims to be aware, sentient, or unlimited in intelligence; it never presents a design as an achieved system; it never invents a record; and it says plainly when it does not know. The limits are part of the specialist, not an afterthought, and they are stated in every record the specialist's generator files. This record.",
    "label": "specialist-honesty-limits",
    "figures": {
      "limit_rules": 4,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "glossary_terms": 27,
      "sections": 14,
      "hard_stop": 1000000000,
      "specialties": 12
    }
  },
  {
    "title": "Specialist Agents",
    "subject": "specialist agents",
    "description": "A specialist agent is a task-oriented agent that works for a specialist: it carries out one task, such as fetching records, running tests, or drafting an answer, and it reports back with its results and its sources. Agents do the specialist's errands, and the specialist does the reasoning. This record specifies the agent rules: one task per agent, results reported with sources, and no agent.",
    "label": "specialist-agents",
    "figures": {
      "agent_parts": 3,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "glossary_terms": 27,
      "sections": 14,
      "hard_stop": 1000000000,
      "specialties": 12
    }
  }
];

const SOURCES = [
  {
    "name": "Wikipedia - Expert system",
    "url": "https://en.wikipedia.org/wiki/Expert_system",
    "establishes": "Expert system: how specialist knowledge is captured as rules a program can use.",
    "retrieved": "2026-11-17",
    "resource_id": "en.wikipedia.org/wiki/Expert_system"
  },
  {
    "name": "Wikipedia - Artificial general intelligence",
    "url": "https://en.wikipedia.org/wiki/Artificial_general_intelligence",
    "establishes": "Artificial general intelligence: the background concept for specialist AI systems.",
    "retrieved": "2026-11-17",
    "resource_id": "en.wikipedia.org/wiki/Artificial_general_intelligence"
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
