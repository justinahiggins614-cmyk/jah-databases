// Seeded boundless generator for the darpa-ai-research-signature database
// (signature edition). Deterministic: the same seed always emits the same
// record. Usage: node gen-darpa-ai-research-signature.js [seed]  (prints one
// JSON record) or: node gen-darpa-ai-research-signature.js --test (runTests).
// Package-only; outputs are generated, not stored files.
"use strict";
const crypto = require("crypto");

const SLUG = "darpa-ai-research-signature";
const RECORD_KIND = "darpa ai research record";
const ID_PREFIX = "JAH-DAIRS-";
const AI_NAME = "JAH DARPA AI Research Librarian (Signature)";
const EDITION = "signature";
const SRC = "signature-generated";
const CEILING = "Generator ceiling: up to 1,000,000,000 scales per file, generated on demand by the file AI \u2014 not stored files.";

const TOPICS = [
  {
    "title": "Signature Design Study: An AI Research Workbench",
    "subject": "Artificial intelligence research overview",
    "description": "Signature design study: This record is the front door of the Artificial Intelligence Research Database. It states the mission: to help the JAH Network Master AI investigate difficult problems, develop new technologies, build prototypes, test new engineering approaches, and connect multiple advanced disciplines, with artificial intelligence research as the coordinating discipline.",
    "figures": {
      "research_areas": 12,
      "capabilities": 12,
      "evidence_rungs": 9,
      "partner_organizations": 7,
      "databases": 40,
      "websites": 30,
      "generators": 30,
      "catalog_items": 100
    },
    "label": "darpa-ai-research-overview"
  },
  {
    "title": "Signature Design Study: A Modular Learning Architecture",
    "subject": "Machine learning architectures",
    "description": "Signature design study: Machine learning is the part of artificial intelligence in which a computer system improves its performance on a task by learning from data, rather than by following only rules written by hand. This record covers the architectures, meaning the structured arrangements of parts, by which such learning systems are built: data intake, feature building, model training, evaluation, and deployment.",
    "figures": {
      "architecture_families": 6,
      "training_stages": 5,
      "evaluation_splits": 3,
      "regularization_methods": 4,
      "data_sources": 8,
      "quality_gates": 5,
      "model_versions": 12,
      "retraining_cycles": 4
    },
    "label": "machine-learning-architectures"
  },
  {
    "title": "Signature Design Study: A Layered Network Workbench",
    "subject": "Deep neural networks",
    "description": "Signature design study: A neural network is a learning system built from layers of simple computing units, where each unit takes numbers in, applies a weight, and passes a number on. Deep means many layers, so the network builds its understanding in stages: early layers find simple patterns, later layers combine them into complex ones. This record covers how such networks are designed, trained, and checked.",
    "figures": {
      "network_layers": 12,
      "hidden_units": 512,
      "training_epochs": 50,
      "batch_size": 32,
      "learning_rate_steps": 4,
      "dropout_rate_pct": 20,
      "checkpoints": 10,
      "benchmark_tasks": 6
    },
    "label": "deep-neural-networks"
  },
  {
    "title": "Signature Design Study: A Reward-Learning Sandbox",
    "subject": "Reinforcement learning",
    "description": "Signature design study: Reinforcement learning is the part of machine learning in which an agent, meaning a software system that acts, learns by trying actions and receiving rewards and penalties. A policy is the agent's rule for choosing actions. The agent's goal is to learn a policy that maximizes the total reward over time. This record covers how such learning is set up, run, and checked safely.",
    "figures": {
      "agent_policies": 5,
      "reward_signals": 4,
      "episodes": 1000,
      "state_features": 24,
      "action_choices": 8,
      "discount_steps": 10,
      "evaluation_runs": 20,
      "safety_limits": 6
    },
    "label": "reinforcement-learning"
  },
  {
    "title": "Signature Design Study: A Language Understanding Bench",
    "subject": "Natural language understanding",
    "description": "Signature design study: Natural language understanding is the part of artificial intelligence in which a machine reads human language and works out what it means: what the words refer to, what the speaker intends, and what follows from the text. Natural language means language as people actually use it, with ambiguity, idiom, and context. This record covers how understanding systems are built and judged.",
    "figures": {
      "language_tasks": 8,
      "vocabulary_size": 50000,
      "training_documents": 10000,
      "test_sentences": 2000,
      "evaluation_metrics": 5,
      "supported_languages": 12,
      "error_categories": 7,
      "review_rounds": 3
    },
    "label": "natural-language-understanding"
  },
  {
    "title": "Signature Design Study: A Vision Research Bench",
    "subject": "Computer vision research",
    "description": "Signature design study: Computer vision is the part of artificial intelligence in which a machine interprets images and video: finding objects, reading scenes, tracking motion, and estimating depth. Vision here means measurement from light, not human sight. This record covers how vision systems are built, labeled, tested, and checked for failure.",
    "figures": {
      "vision_tasks": 7,
      "image_datasets": 6,
      "test_images": 5000,
      "label_classes": 100,
      "evaluation_metrics": 4,
      "lighting_conditions": 5,
      "failure_modes": 8,
      "annotation_rounds": 3
    },
    "label": "computer-vision-research"
  },
  {
    "title": "Signature Design Study: A Reasoning Graph Workbench",
    "subject": "Knowledge representation and reasoning",
    "description": "Signature design study: Knowledge representation is the study of how to write down what is known in a form a machine can use, and reasoning is the study of how a machine draws sound conclusions from what is written down. A knowledge graph is one such form: things as nodes and relationships as links between them. This record covers how knowledge is represented, checked for consistency, and queried.",
    "figures": {
      "knowledge_domains": 9,
      "entity_types": 40,
      "relation_types": 25,
      "reasoning_rules": 120,
      "inference_tests": 60,
      "consistency_checks": 15,
      "query_patterns": 18,
      "review_rounds": 3
    },
    "label": "knowledge-representation-reasoning"
  },
  {
    "title": "Signature Design Study: An Explanation Workbench",
    "subject": "Explainable artificial intelligence",
    "description": "Signature design study: Explainable artificial intelligence, often shortened to XAI (explainable artificial intelligence), is the study of making an artificial intelligence system's decisions understandable to the people affected by them. An explanation names which inputs mattered, what rule or pattern was used, and what would have changed the decision. This record covers how explanations are built and judged.",
    "figures": {
      "explanation_methods": 8,
      "explanation_tests": 40,
      "user_studies": 6,
      "fidelity_metrics": 4,
      "decision_cases": 100,
      "review_rounds": 3,
      "stakeholder_groups": 5,
      "audit_trails": 12
    },
    "label": "explainable-ai"
  }
];

const SOURCES = [
  {
    "name": "DARPA (Defense Advanced Research Projects Agency) - research programs, technology areas, solicitations and program information",
    "url": "https://www.darpa.mil",
    "establishes": "Source for generated records in this edition."
  },
  {
    "name": "Wikipedia - Artificial intelligence",
    "url": "https://en.wikipedia.org/wiki/Artificial_intelligence",
    "establishes": "Source for generated records in this edition."
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
    src: SRC,
    ai_name: AI_NAME,
    description: topic.description + " No claim of a proven breakthrough, of flight readiness, or of deployment readiness is established by this generated record." + " DARPA-grade here means engineering targets modeled on public standards, never a claim of DARPA approval, certification, funding, or endorsement.",
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
