// Seeded boundless generator for the neuromorphic-computing-signature database
// (signature edition). Deterministic: the same seed always emits the same
// record. Usage: node gen-neuromorphic-computing-signature.js [seed]  (prints one
// JSON record) or: node gen-neuromorphic-computing-signature.js --test (runTests).
// Package-only; outputs are generated, not stored files.
// All records are design-study: illustrative design values, never real fact.
"use strict";
const crypto = require("crypto");

const SLUG = "neuromorphic-computing-signature";
const RECORD_KIND = "neuromorphic computing record";
const ID_PREFIX = "JAH-NEUROMS-";
const AI_NAME = "JAH Neuromorphic Computing Librarian (Signature)";
const CEILING = "Generator ceiling: up to 1,000,000,000 scales per file, generated on demand by the file AI \u2014 not stored files.";

const TOPICS = [
  {
    "title": "Signature Spiking Neuron Cell: One Neuron, Designed",
    "subject": "the Signature spiking neuron cell design",
    "description": "The Signature spiking neuron cell is a design-study for one leaky integrate-and-fire neuron built from 20 transistors and a 100 femtofarad capacitor.",
    "figures": {
      "transistors": 20,
      "capacitor_ff": 100,
      "time_constant_ms": 20,
      "threshold_mv": 15,
      "power_nw": 10,
      "inputs": 100,
      "refractory_ms": 2
    }
  },
  {
    "title": "Signature Memristor Crossbar: A Grid That Multiplies",
    "subject": "the Signature memristor crossbar design",
    "description": "The Signature memristor crossbar is a design-study for a 64 by 64 grid of memristors that performs a matrix-vector multiplication in one step.",
    "figures": {
      "rows": 64,
      "columns": 64,
      "devices": 4096,
      "precision_bits": 4,
      "adc_bits": 8,
      "operations_per_step": 4096,
      "energy_per_op_fj": 10
    }
  },
  {
    "title": "Signature Event Camera Front End: Seeing Only Change",
    "subject": "the Signature event camera front end design",
    "description": "The Signature event camera front end is a design-study for a 10,000-pixel event camera that reports only brightness changes, with 1 microsecond temporal resolution.",
    "figures": {
      "pixels": 10000,
      "temporal_resolution_us": 1,
      "dynamic_range_db": 120,
      "power_mw": 10,
      "readout_channels": 4,
      "latency_us": 10,
      "polarities": 2
    }
  },
  {
    "title": "Signature Plasticity Engine: Learning on the Chip",
    "subject": "the Signature plasticity engine design",
    "description": "The Signature plasticity engine is a design-study for on-chip learning: it updates 10,000 synapses in parallel at 100 hertz, using 3 learning rules.",
    "figures": {
      "synapses": 10000,
      "learning_rules": 3,
      "update_rate_hz": 100,
      "time_window_ms": 20,
      "weight_bits": 8,
      "parallel_updates": 1000,
      "power_mw": 5
    }
  },
  {
    "title": "Signature Dendrite Array: Branches That Compute",
    "subject": "the Signature dendrite array design",
    "description": "The Signature dendrite array is a design-study for 64 neurons, each with 8 dendritic branches divided into 4 compartments, so that inputs are combined nonlinearly before they reach the cell body.",
    "figures": {
      "neurons": 64,
      "branches_per_neuron": 8,
      "compartments": 4,
      "inputs_per_branch": 16,
      "nonlinearities": 2,
      "integration_zones": 3,
      "power_mw": 20
    }
  },
  {
    "title": "Signature Reservoir Core: A Fixed Pool, A Trained Readout",
    "subject": "the Signature reservoir core design",
    "description": "The Signature reservoir core is a design-study for a fixed, randomly connected network of 100 nodes with a trained readout of 100 weights.",
    "figures": {
      "reservoir_nodes": 100,
      "readout_weights": 100,
      "input_dimensions": 5,
      "spectral_radius": 1,
      "memory_steps": 10,
      "training_samples": 1000,
      "nonlinearities": 2
    }
  },
  {
    "title": "Signature Olfactory Chip: Smelling with a Sensor Array",
    "subject": "the Signature olfactory chip design",
    "description": "The Signature olfactory chip is a design-study for a 64-sensor array of 3 types feeding a spiking network that classifies 10 odors with 90 percent accuracy.",
    "figures": {
      "sensors": 64,
      "sensor_types": 3,
      "odors": 10,
      "accuracy_percent": 90,
      "response_time_ms": 100,
      "drift_compensation": 2,
      "calibration_steps": 3
    }
  },
  {
    "title": "Signature Motor Control Loop: Spikes That Move a Robot",
    "subject": "the Signature motor control loop design",
    "description": "The Signature motor control loop is a design-study for a spiking controller that drives 6 robot joints at 100 hertz with about 10 milliseconds of latency.",
    "figures": {
      "joints": 6,
      "control_rate_hz": 100,
      "latency_ms": 10,
      "sensors": 4,
      "adaptation_rate": 5,
      "tasks": 3,
      "power_mw": 100
    }
  }
];

const SOURCES = [
  {
    "name": "Wikipedia - Leaky integrate-and-fire",
    "url": "https://en.wikipedia.org/wiki/Leaky_integrate-and-fire",
    "establishes": "Defines the leaky integrate-and-fire neuron the cell implements."
  },
  {
    "name": "Wikipedia - Spiking neural network",
    "url": "https://en.wikipedia.org/wiki/Spiking_neural_network",
    "establishes": "Defines the spiking networks the cell belongs to."
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
  const label = "neuromorphic-computing-signature-design";
  const demo = buildDemo(topic, label);
  const rec = {
    id: id,
    slug: SLUG,
    edition: "signature",
    record_kind: RECORD_KIND,
    title: topic.title + " (Generated " + idx + ")",
    subject: topic.subject,
    status: "built",
    src: "signature-generated",
    ai_name: AI_NAME,
    description: topic.description + " Design-study: illustrative design values, never real fact. DARPA-grade means engineering targets modeled on public standards, never DARPA approval, certification, funding, or endorsement.",
    body: "<h2>Description</h2><p>" + topic.description + "</p>",
    demo: demo.code,
    expected_output: demo.expected,
    program: "class GeneratedProgram:\n    def run(self):\n        return {\"deterministic\": True}\n",
    sources: SOURCES,
    generator: { type: "seeded boundless generator", gen_id_prefix: ID_PREFIX + "GEN-", hard_stop: 1000000000, throttle_per_call: 100, ceiling_note: CEILING },
    scales: { A1: "One request: " + topic.subject + " specified in full.", A2: "The whole pair: public research records beside Signature design-study designs.", A3: "The network: every database a knowledge source, every generator a tool." },
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
  t("slug single -signature form", a.slug === SLUG && (a.slug.match(/-signature/g) || []).length === 1);
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
