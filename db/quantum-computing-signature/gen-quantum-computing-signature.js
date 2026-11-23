// Seeded boundless generator for the quantum-computing-signature database
// (signature edition). Deterministic: the same seed always emits the same
// record. Usage: node gen-quantum-computing-signature.js [seed]  (prints one
// JSON record) or: node gen-quantum-computing-signature.js --test (runTests).
// Package-only; outputs are generated, not stored files.
// All records are design-study: illustrative design values, never real fact.
"use strict";
const crypto = require("crypto");

const SLUG = "quantum-computing-signature";
const RECORD_KIND = "quantum computing exploration";
const ID_PREFIX = "JAH-QCOMPS-";
const AI_NAME = "JAH Quantum Computing Librarian (Signature)";
const CEILING = "Generator ceiling: up to 1,000,000,000 scales per file, generated on demand by the file AI \u2014 not stored files.";

const TOPICS = [
  {
    "title": "Signature Qubit Lattice Array: A Design-Study Qubit Grid",
    "subject": "the Signature qubit lattice array design",
    "description": "The Signature qubit lattice array is a design-study layout that places 64 design qubits on an 8 by 8 grid, with couplers between neighbors so that any adjacent pair can interact.",
    "figures": {
      "lattice_sites": 64,
      "qubit_rows": 8,
      "qubit_columns": 8,
      "couplers": 112,
      "control_lines": 64,
      "readout_lines": 8,
      "design_targets": 5
    }
  },
  {
    "title": "Signature Entanglement Switchboard: Routing Linked Qubits",
    "subject": "the Signature entanglement switchboard design",
    "description": "The Signature entanglement switchboard is a design-study device that routes entanglement between 8 ports, so that any two ports can share a Bell pair on demand.",
    "figures": {
      "ports": 8,
      "bell_pairs_per_port": 4,
      "switching_steps": 3,
      "routing_paths": 28,
      "fidelity_budget": 95,
      "memory_slots": 16,
      "control_channels": 8
    }
  },
  {
    "title": "Signature Surface-Code Tile: One Logical Qubit, Designed",
    "subject": "the Signature surface-code tile design",
    "description": "The Signature surface-code tile is a design-study for one logical qubit at code distance 3, using 9 data qubits and 8 measure qubits arranged on a small grid.",
    "figures": {
      "code_distance": 3,
      "data_qubits": 9,
      "measure_qubits": 8,
      "stabilizers": 8,
      "syndrome_rounds": 3,
      "tile_area": 9,
      "logical_operators": 2
    }
  },
  {
    "title": "Signature Cryogenic Control Stack: Wiring the Cold Machine",
    "subject": "the Signature cryogenic control stack design",
    "description": "The Signature cryogenic control stack is a design-study for the wiring that carries microwave control signals from room temperature down to a quantum chip at 15 millikelvin.",
    "figures": {
      "temperature_stages": 5,
      "base_temperature_mk": 15,
      "control_lines": 64,
      "attenuators_per_line": 3,
      "amplifiers": 2,
      "heat_budget_uw": 10,
      "cable_types": 3
    }
  },
  {
    "title": "Signature Photonic Interconnect: Light Between Modules",
    "subject": "the Signature photonic interconnect design",
    "description": "The Signature photonic interconnect is a design-study for linking 4 quantum modules with optical fiber, so that photons carry quantum information between modules.",
    "figures": {
      "modules": 4,
      "fibers_per_module": 8,
      "photon_rate_khz": 100,
      "loss_budget_db": 3,
      "detectors": 8,
      "wavelength_channels": 4,
      "switch_ports": 8
    }
  },
  {
    "title": "Signature Trapped-Ion Rail: Moving Ions to Compute",
    "subject": "the Signature trapped-ion rail design",
    "description": "The Signature trapped-ion rail is a design-study for a linear ion trap with 8 zones, where ions are shuttled between zones so that any pair can be brought together to interact.",
    "figures": {
      "trap_zones": 8,
      "ions_per_zone": 4,
      "total_ions": 32,
      "shuttling_steps": 6,
      "gate_zones": 2,
      "readout_zones": 1,
      "laser_beams": 4
    }
  },
  {
    "title": "Signature Superconducting Resonator Bank: Reading Many Qubits",
    "subject": "the Signature superconducting resonator bank design",
    "description": "The Signature superconducting resonator bank is a design-study for reading 8 qubits through 2 shared readout lines, with each qubit coupled to its own microwave resonator.",
    "figures": {
      "resonators": 8,
      "qubits_per_resonator": 1,
      "readout_lines": 2,
      "frequency_spacing_mhz": 100,
      "bandwidth_mhz": 800,
      "amplifiers": 2,
      "purcell_filters": 8
    }
  },
  {
    "title": "Signature Quantum Error Budget Tool: Counting Every Error",
    "subject": "the Signature quantum error budget tool design",
    "description": "The Signature quantum error budget tool is a design-study for a calculator that adds up the six error sources of a quantum computation into one total error budget.",
    "figures": {
      "error_sources": 6,
      "budget_parts": 6,
      "gate_error_ppm": 1000,
      "readout_error_percent": 1,
      "decoherence_share": 30,
      "crosstalk_share": 10,
      "total_budget_percent": 1
    }
  }
];

const SOURCES = [
  {
    "name": "Wikipedia - Quantum error correction",
    "url": "https://en.wikipedia.org/wiki/Quantum_error_correction",
    "establishes": "Surface-code geometry the lattice layout is designed to match."
  },
  {
    "name": "Wikipedia - Quantum computing",
    "url": "https://en.wikipedia.org/wiki/Quantum_computing",
    "establishes": "Public research background on qubit arrays."
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
  const label = "quantum-computing-signature-design";
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
