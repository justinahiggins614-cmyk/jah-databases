// Seeded boundless generator for the Quantum Information Database
// (public edition). Deterministic: the same seed always emits the same
// record. Usage: node gen-quantum-information.js [seed]  (prints one
// JSON record) or: node gen-quantum-information.js --test (runTests).
// Package-only; outputs are generated, not stored files.
"use strict";
const crypto = require("crypto");

const SLUG = "quantum-information";
const RECORD_KIND = "future quantum information record";
const ID_PREFIX = "JAH-QINF-";
const AI_NAME = "JAH Quantum Information Librarian";
const EDITION = "public";
const CEILING = "Generator ceiling: up to 1,000,000,000 scales per file, generated on demand by the file AI \u2014 not stored files.";

const TOPICS = [
  {
    "title": "What Quantum Information Is",
    "subject": "quantum information identity",
    "description": "Quantum information is information stored and processed using the rules of quantum physics, the physics of the very small. Where an ordinary computer stores bits that are zero or one, a quantum device stores qubits, which are quantum bits able to hold a blend of zero and one at once, and links them with entanglement, which joins two qubits so measuring one fixes the other. This record.",
    "label": "what-quantum-information-is",
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
    "title": "The Quantum Bit",
    "subject": "the quantum bit",
    "description": "A qubit, short for quantum bit, is the basic unit of quantum information, like a bit in an ordinary computer but able to hold a blend of zero and one at once. A qubit can be built from many physical things: a superconducting circuit cooled near absolute zero, a single trapped ion held by electric fields, or a single particle of light. This record specifies the research: what makes a good.",
    "label": "the-quantum-bit",
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
    "title": "Superposition and Measurement",
    "subject": "superposition and measurement",
    "description": "Superposition is the quantum property by which a qubit can hold a blend of zero and one at the same time until it is measured, and measurement is the act of reading a qubit, which forces its blended state to settle into a definite zero or one. The blend is where quantum power lives: a calculation can work on many blends at once. The cost is that reading the answer destroys the blend, so a.",
    "label": "superposition-and-measurement",
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
    "title": "Entanglement",
    "subject": "entanglement",
    "description": "Entanglement is the quantum property by which two qubits can be linked so that measuring one at once fixes the state of the other, however far apart they are. Entanglement is the resource that makes quantum communication and much of quantum computing possible: it lets distant devices share a state no ordinary message could carry. This record specifies the research: making entangled pairs,.",
    "label": "entanglement",
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
    "title": "Quantum Gates and Circuits",
    "subject": "quantum gates and circuits",
    "description": "A quantum gate is a basic operation that changes the state of one or more qubits, like a step in a quantum calculation, and a quantum circuit is a sequence of gates that carries out a whole calculation. Gates must be fast, accurate, and gentle: every gate adds a little error, and errors add up across a long circuit. This record specifies the research: gate designs for each qubit type, gate.",
    "label": "quantum-gates-and-circuits",
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
    "title": "Quantum Computing",
    "subject": "quantum computing",
    "description": "A quantum computer is a computer that stores and processes information in qubits and uses quantum rules such as superposition and entanglement. It does not replace ordinary computers: it excels at a few kinds of problems, such as simulating molecules, searching large spaces in a structured way, and factoring large numbers, while ordinary computers remain better at most everyday work. This.",
    "label": "quantum-computing",
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
    "title": "Quantum Error Correction",
    "subject": "quantum error correction",
    "description": "Quantum error correction is a set of methods that spread one qubit of information across many physical qubits so that errors can be found and fixed. Qubits are fragile: heat, stray fields, and imperfect gates all introduce errors, and a calculation that runs long enough will be ruined without correction. The price is steep: one protected qubit can need hundreds or thousands of physical qubits..",
    "label": "quantum-error-correction",
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
    "title": "Quantum Key Distribution",
    "subject": "quantum key distribution",
    "description": "Quantum key distribution, shortened to QKD, is a way for two parties to share a secret key using quantum physics so that anyone listening in can be detected. The key is carried on qubits, often on single particles of light, and any attempt to read them disturbs them in a way the two parties can notice. The key is then used with ordinary encryption to protect messages. This record specifies the.",
    "label": "quantum-key-distribution",
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
