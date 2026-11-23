// Seeded boundless generator for the neuromorphic-computing database
// (public edition). Deterministic: the same seed always emits the same
// record. Usage: node gen-neuromorphic-computing.js [seed]  (prints one
// JSON record) or: node gen-neuromorphic-computing.js --test (runTests).
// Package-only; outputs are generated, not stored files.
"use strict";
const crypto = require("crypto");

const SLUG = "neuromorphic-computing";
const RECORD_KIND = "neuromorphic computing record";
const ID_PREFIX = "JAH-NEUROM-";
const AI_NAME = "JAH Neuromorphic Computing Librarian";
const CEILING = "Generator ceiling: up to 1,000,000,000 scales per file, generated on demand by the file AI \u2014 not stored files.";

const TOPICS = [
  {
    "title": "Neuromorphic Computing Foundations: Brains as the Blueprint",
    "subject": "neuromorphic computing foundations",
    "description": "Neuromorphic computing is brain-inspired computing: hardware and software designed to work the way brains appear to work, with neurons that send brief pulses called spikes and synapses whose strength changes with experience.",
    "figures": {
      "neurons_brain": 86000000000,
      "synapses_brain": 100000000000000,
      "brain_power_watts": 20,
      "spike_types": 2,
      "design_principles": 5,
      "energy_gain": 100,
      "time_scales": 3
    }
  },
  {
    "title": "Spiking Neural Networks: Computing with Spikes",
    "subject": "spiking neural networks",
    "description": "A spiking neural network, usually shortened to SNN, is a neural network in which neurons communicate with brief pulses called spikes, and information is carried in the timing and rate of the spikes.",
    "figures": {
      "layers": 3,
      "neurons_per_layer": 100,
      "spike_rate_hz": 10,
      "time_steps": 100,
      "synapses": 30000,
      "encoding_schemes": 3,
      "learning_rules": 2
    }
  },
  {
    "title": "The Leaky Integrate-and-Fire Neuron: The Standard Model",
    "subject": "the leaky integrate-and-fire neuron",
    "description": "The leaky integrate-and-fire neuron, usually shortened to LIF, is the standard model of a spiking neuron: it adds up incoming spikes into a membrane voltage, leaks that voltage away over time, and fires a spike when the voltage crosses a threshold.",
    "figures": {
      "time_constant_ms": 20,
      "threshold_mv": 15,
      "reset_mv": 0,
      "refractory_ms": 2,
      "inputs": 100,
      "states": 2,
      "parameters": 4
    }
  },
  {
    "title": "Spike-Timing-Dependent Plasticity: Learning from Timing",
    "subject": "spike-timing-dependent plasticity",
    "description": "Spike-timing-dependent plasticity, usually shortened to STDP, is a learning rule: if a presynaptic spike arrives just before the postsynaptic neuron fires, the synapse strengthens, and if it arrives just after, the synapse weakens.",
    "figures": {
      "time_window_ms": 20,
      "potentiation_percent": 10,
      "depression_percent": 10,
      "synapses_updated": 1000,
      "learning_rate": 1,
      "pairings": 100,
      "stability_checks": 2
    }
  },
  {
    "title": "The Memristor as Artificial Synapse: Memory That Learns",
    "subject": "the memristor as artificial synapse",
    "description": "A memristor is a device whose resistance depends on its history: passing current one way lowers the resistance, and passing it the other way raises it, so the device remembers what happened to it.",
    "figures": {
      "resistance_states": 16,
      "switching_time_ns": 10,
      "endurance_cycles": 1000000,
      "read_voltage_v": 1,
      "write_voltage_v": 2,
      "array_size": 100,
      "retention_years": 10
    }
  },
  {
    "title": "Crossbar Arrays and In-Memory Computing: Math Where the Data Lives",
    "subject": "crossbar arrays and in-memory computing",
    "description": "A crossbar array is a grid of wires with a memory device at each crossing, and in-memory computing uses that grid to compute where the data already lives, instead of moving data to a processor.",
    "figures": {
      "array_rows": 128,
      "array_columns": 128,
      "operations_per_step": 16384,
      "precision_bits": 4,
      "energy_per_op_fj": 10,
      "devices": 16384,
      "adc_bits": 8
    }
  },
  {
    "title": "Event-Driven Sensing and the Dynamic Vision Sensor",
    "subject": "event-driven sensing and the dynamic vision sensor",
    "description": "An event-driven sensor reports only changes: instead of capturing whole frames on a clock, each pixel reports independently when its brightness changes, producing a stream of events.",
    "figures": {
      "pixels": 10000,
      "temporal_resolution_us": 1,
      "dynamic_range_db": 120,
      "power_mw": 10,
      "events_per_second": 1000000,
      "latency_us": 10,
      "sensor_types": 2
    }
  },
  {
    "title": "Intel Loihi: A Research Chip for Spiking Networks",
    "subject": "Intel Loihi",
    "description": "Intel Loihi is a neuromorphic research chip, announced in 2017, that runs spiking neural networks directly in hardware instead of simulating them on a conventional processor.",
    "figures": {
      "cores": 128,
      "neurons_per_core": 1024,
      "synapses_per_core": 1000000,
      "neurons_total": 131072,
      "learning_rules": 2,
      "process_nm": 14,
      "power_watts": 1
    }
  }
];

const SOURCES = [
  {
    "name": "Wikipedia - Neuromorphic computing",
    "url": "https://en.wikipedia.org/wiki/Neuromorphic_computing",
    "establishes": "Defines neuromorphic computing and its brain-inspired principles."
  },
  {
    "name": "Wikipedia - Spiking neural network",
    "url": "https://en.wikipedia.org/wiki/Spiking_neural_network",
    "establishes": "Defines spiking neural networks, the computing model."
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
  const label = "neuromorphic-computing-overview";
  const demo = buildDemo(topic, label);
  const rec = {
    id: id,
    slug: SLUG,
    edition: "public",
    record_kind: RECORD_KIND,
    title: topic.title + " (Generated " + idx + ")",
    subject: topic.subject,
    status: "built",
    src: "public-harvest",
    ai_name: AI_NAME,
    description: topic.description + " DARPA-grade means engineering targets modeled on public standards, never DARPA approval, certification, funding, or endorsement.",
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
  t("slug single form", a.slug === SLUG && a.slug.indexOf("-signature") === -1);
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
