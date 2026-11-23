// Seeded boundless generator for the Quantum Information Database
// (signature edition). Deterministic: the same seed always emits the same
// record. Usage: node gen-quantum-information-signature.js [seed]  (prints one
// JSON record) or: node gen-quantum-information-signature.js --test (runTests).
// Package-only; outputs are generated, not stored files.
"use strict";
const crypto = require("crypto");

const SLUG = "quantum-information-signature";
const RECORD_KIND = "future quantum information record";
const ID_PREFIX = "JAH-QINFS-";
const AI_NAME = "JAH Quantum Information Librarian (Signature)";
const EDITION = "signature";
const CEILING = "Generator ceiling: up to 1,000,000,000 scales per file, generated on demand by the file AI \u2014 not stored files.";

const TOPICS = [
  {
    "title": "Signature Qubit Room",
    "subject": "signature qubit room",
    "description": "The Signature Qubit Room is a design for a room where one qubit lives: the room is cold and quiet, the qubit is a coin spinning on a table that is both heads and tails until someone looks, and the reader must enter softly or the coin falls. The design imagines quantum information as a room to be entered quietly, not a machine to be shouted at.",
    "label": "signature-qubit-room",
    "figures": {
      "qubits": 50,
      "gate_fidelity_per_thousand": 999,
      "coherence_ms": 100,
      "error_rate_per_thousand": 1,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "sections": 14
    }
  },
  {
    "title": "Signature Bit Cradle",
    "subject": "signature bit cradle",
    "description": "The Signature Bit Cradle is a design for a cradle that rocks a qubit gently: superconducting circuits are the wood, the cold is the blanket, and the cradle rocks the qubit's blend without waking it into a plain zero or one. The design imagines qubit care as nursing, where gentleness is the engineering.",
    "label": "signature-bit-cradle",
    "figures": {
      "qubits": 100,
      "gate_fidelity_per_thousand": 999,
      "coherence_ms": 150,
      "error_rate_per_thousand": 1,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "sections": 14
    }
  },
  {
    "title": "Signature Superposition Bridge",
    "subject": "signature superposition bridge",
    "description": "The Signature Superposition Bridge is a design for a bridge that stands in two places at once: the qubit walks the bridge as a blend of both paths, and only when it reaches the far side does it choose one. The design imagines superposition as a bridge that is both roads until it is crossed.",
    "label": "signature-superposition-bridge",
    "figures": {
      "qubits": 50,
      "gate_fidelity_per_thousand": 998,
      "coherence_ms": 120,
      "error_rate_per_thousand": 2,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "sections": 14
    }
  },
  {
    "title": "Signature Entanglement Loom",
    "subject": "signature entanglement loom",
    "description": "The Signature Entanglement Loom is a design for a loom that weaves two qubits into one cloth: the threads are the qubits, the weave is the entanglement, and pulling one thread moves the other however far the cloth stretches. The design imagines entanglement as weaving, where the cloth is one thing even when its ends are far apart.",
    "label": "signature-entanglement-loom",
    "figures": {
      "qubits": 2,
      "gate_fidelity_per_thousand": 999,
      "coherence_ms": 100,
      "error_rate_per_thousand": 1,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "sections": 14
    }
  },
  {
    "title": "Signature Gate Workshop",
    "subject": "signature gate workshop",
    "description": "The Signature Gate Workshop is a design for a workshop where quantum gates are made: each gate is a tool that turns a qubit a precise amount, and the tools are laid out in order so a circuit can be built step by step. The design imagines gates as tools on a bench, where a tool that is a hair off ruins the work.",
    "label": "signature-gate-workshop",
    "figures": {
      "qubits": 100,
      "gate_fidelity_per_thousand": 999,
      "coherence_ms": 50,
      "error_rate_per_thousand": 1,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "sections": 14
    }
  },
  {
    "title": "Signature Computing Hall",
    "subject": "signature computing hall",
    "description": "The Signature Computing Hall is a design for a hall where quantum computers work: rows of cold cabinets hum quietly, each holding qubits that calculate in blends, while ordinary computers stand at the door doing the everyday work. The design imagines quantum computing as a specialist hall beside an ordinary office, each doing what it does best.",
    "label": "signature-computing-hall",
    "figures": {
      "qubits": 1000,
      "gate_fidelity_per_thousand": 999,
      "coherence_ms": 100,
      "error_rate_per_thousand": 1,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "sections": 14
    }
  },
  {
    "title": "Signature Error Shield",
    "subject": "signature error shield",
    "description": "The Signature Error Shield is a design for a shield woven from many qubits: one protected qubit hides behind hundreds of physical ones, and when an error strikes, the shield's pattern shows where it landed so it can be mended. The design imagines error correction as a shield wall, where many stand to guard one.",
    "label": "signature-error-shield",
    "figures": {
      "qubits": 1000,
      "gate_fidelity_per_thousand": 999,
      "coherence_ms": 100,
      "error_rate_per_thousand": 1,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "sections": 14
    }
  },
  {
    "title": "Signature Key Courier",
    "subject": "signature key courier",
    "description": "The Signature Key Courier is a design for a courier who carries secret keys on single particles of light: the courier walks a road of fibre, and if anyone stops the courier to read the message, the disturbance shows in the courier's step. The design imagines key distribution as a trusted messenger whose every stumble proves an ambush.",
    "label": "signature-key-courier",
    "figures": {
      "qubits": 2,
      "gate_fidelity_per_thousand": 999,
      "coherence_ms": 100,
      "error_rate_per_thousand": 1,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "sections": 14
    }
  }
];

const SOURCES = [
  {
    "name": "Wikipedia - Quantum information",
    "url": "https://en.wikipedia.org/wiki/Quantum_information",
    "establishes": "Quantum information: how information is stored and processed using quantum physics.",
    "retrieved": "2026-11-17",
    "resource_id": "en.wikipedia.org/wiki/Quantum_information"
  },
  {
    "name": "Wikipedia - Quantum computing",
    "url": "https://en.wikipedia.org/wiki/Quantum_computing",
    "establishes": "Quantum computing: how computers that use qubits work.",
    "retrieved": "2026-11-17",
    "resource_id": "en.wikipedia.org/wiki/Quantum_computing"
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
