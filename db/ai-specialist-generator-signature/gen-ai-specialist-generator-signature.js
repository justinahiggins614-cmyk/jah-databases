// Seeded boundless generator for the AI Specialist Generator
// (signature edition). Deterministic: the same seed always emits the same
// record. Usage: node gen-ai-specialist-generator-signature.js [seed]  (prints one
// JSON record) or: node gen-ai-specialist-generator-signature.js --test (runTests).
// Package-only; outputs are generated, not stored files.
"use strict";
const crypto = require("crypto");

const SLUG = "ai-specialist-generator-signature";
const RECORD_KIND = "ai specialist generator record";
const ID_PREFIX = "JAH-AISGS-";
const AI_NAME = "JAH AI Specialist Generator Librarian (Signature)";
const EDITION = "signature";
const CEILING = "Generator ceiling: up to 1,000,000,000 scales per file, generated on demand by the file AI \u2014 not stored files.";

const TOPICS = [
  {
    "title": "Signature Specialist Atelier",
    "subject": "signature specialist atelier",
    "description": "The Signature Specialist Atelier is a design for a workshop where specialists are made: one bench per specialty, a knowledge base on the shelf, a rule set on the wall, and an evaluator at the door. The design imagines a specialist as a craft, where a narrow field known deeply beats a wide field known thinly.",
    "label": "signature-specialist-atelier",
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
    "title": "Signature Field Gate",
    "subject": "signature field gate",
    "description": "The Signature Field Gate is a design for a gate where specialties arrive: a name and a description are laid on the counter, the network is searched for records in the field, and the gate either opens to building or refuses for lack of records. The design imagines specialty choice as a gate, where a specialty with no records is a doctor with no books.",
    "label": "signature-field-gate",
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
    "title": "Signature Knowledge Orchard",
    "subject": "signature knowledge orchard",
    "description": "The Signature Knowledge Orchard is a design for an orchard where a specialist's knowledge grows: records are planted as trees, each one checked against its sources, and the harvest is the knowledge base. The design imagines a knowledge base as an orchard, where a tree planted without checking is a weed.",
    "label": "signature-knowledge-orchard",
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
    "title": "Signature Rule Loom",
    "subject": "signature rule loom",
    "description": "The Signature Rule Loom is a design for a loom that weaves a specialist's rules: if this is true, then that follows, with each rule named, sourced, and tested before it is woven in. The design imagines reasoning as weaving, where a rule that cannot be traced to a record is a thread with no fiber.",
    "label": "signature-rule-loom",
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
    "title": "Signature Human Voice",
    "subject": "signature human voice",
    "description": "The Signature Human Voice is a design for a voice that answers like a human: full sentences, plain words, and the records it used named in the answer, never templated blocks and never bare claims. The design imagines answering as a voice, where a form cannot be questioned and a voice can.",
    "label": "signature-human-voice",
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
    "title": "Signature Examination Hall",
    "subject": "signature examination hall",
    "description": "The Signature Examination Hall is a design for a hall where specialists are examined: questions with known answers, drawn from the specialty's records, where the specialist must answer correctly and name its records. The design imagines evaluation as an examination, where a specialist that fails is not filed until it passes.",
    "label": "signature-examination-hall",
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
    "title": "Signature Limit Fence",
    "subject": "signature limit fence",
    "description": "The Signature Limit Fence is a design for a fence around a specialist: no awareness claims, no invented records, no design presented as an achieved system, and an honest no always allowed. The design imagines honesty limits as a fence, where a specialist that climbs over it is a storyteller in a specialist's coat.",
    "label": "signature-limit-fence",
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
    "title": "Signature Errand Runners",
    "subject": "signature errand runners",
    "description": "The Signature Errand Runners are a design for runners who do a specialist's errands: one task each, such as fetching records, running tests, or drafting an answer, reporting back with results and sources. The design imagines agents as runners, where a runner that files a record on its own is a servant signing the master's name.",
    "label": "signature-errand-runners",
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
