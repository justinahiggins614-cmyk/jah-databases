// Seeded boundless generator for the darpa-semiconductor-signature database
// (signature edition). Deterministic: the same seed always emits the same
// record. Usage: node gen-darpa-semiconductor-signature.js [seed]  (prints one
// JSON record) or: node gen-darpa-semiconductor-signature.js --test (runTests).
// Package-only; outputs are generated, not stored files.
// All records are design-study: illustrative design values, never real fact.
"use strict";
const crypto = require("crypto");

const SLUG = "darpa-semiconductor-signature";
const RECORD_KIND = "darpa semiconductor record";
const ID_PREFIX = "JAH-DSEMS-";
const AI_NAME = "JAH DARPA Semiconductor Librarian (Signature)";
const CEILING = "Generator ceiling: up to 1,000,000,000 scales per file, generated on demand by the file AI \u2014 not stored files.";

const TOPICS = [
  {
    "title": "Signature FinFET Cell Library: A Design-Study Transistor Set",
    "subject": "the Signature FinFET cell library design",
    "description": "The Signature FinFET cell library is a design-study set of 24 standard cells, each built from FinFET transistors, covering logic gates, latches, and drive-strength variants.",
    "figures": {
      "cells": 24,
      "fin_counts": 4,
      "drive_strengths": 4,
      "cell_heights": 2,
      "leakage_grades": 3,
      "voltage_levels": 2,
      "characterization_corners": 5
    }
  },
  {
    "title": "Signature Gate-All-Around Test Structure: Measuring the New Transistor",
    "subject": "the Signature gate-all-around test structure design",
    "description": "The Signature gate-all-around test structure is a design-study for a test chip that measures GAA transistors, with 12 test devices covering 3 sheet counts and 3 gate lengths.",
    "figures": {
      "test_devices": 12,
      "sheet_counts": 3,
      "gate_lengths_nm": 3,
      "measurement_points": 20,
      "structures_per_die": 4,
      "pads": 16,
      "temperature_points": 3
    }
  },
  {
    "title": "Signature EUV Mask Inspection Bench: Checking the Stencil",
    "subject": "the Signature EUV mask inspection bench design",
    "description": "The Signature EUV mask inspection bench is a design-study for equipment that inspects EUV masks, the stencils that print chip patterns, for defects down to a few nanometers.",
    "figures": {
      "inspection_modes": 2,
      "defect_sizes_nm": 3,
      "scan_speed": 10,
      "repair_tools": 1,
      "mask_stages": 2,
      "review_points": 20,
      "false_alarm_rate": 1
    }
  },
  {
    "title": "Signature Chiplet Interposer: The Floor Between Chiplets",
    "subject": "the Signature chiplet interposer design",
    "description": "The Signature chiplet interposer is a design-study for the silicon floor that joins 4 chiplets inside one package, carrying 100 links between each pair of chiplets.",
    "figures": {
      "chiplets": 4,
      "routing_layers": 5,
      "links_per_pair": 100,
      "bandwidth_tbps": 10,
      "power_planes": 2,
      "test_points": 8,
      "substrate_size_mm": 50
    }
  },
  {
    "title": "Signature Three-Dimensional Stack: Four Dies, One Package",
    "subject": "the Signature three-dimensional stack design",
    "description": "The Signature three-dimensional stack is a design-study for stacking 4 dies in one package, joined by 2000 through-silicon vias and 3 bond layers.",
    "figures": {
      "dies": 4,
      "tsv_count": 2000,
      "bond_layers": 3,
      "thermal_vias": 100,
      "power_planes": 2,
      "stack_height_mm": 1,
      "test_points": 6
    }
  },
  {
    "title": "Signature Silicon Carbide Inverter: Power for an Electric Vehicle",
    "subject": "the Signature silicon carbide inverter design",
    "description": "The Signature silicon carbide inverter is a design-study for a 100 kilowatt inverter that turns a battery's direct current into the alternating current an electric-vehicle motor needs.",
    "figures": {
      "power_kw": 100,
      "switches": 6,
      "efficiency_percent": 99,
      "switching_frequency_khz": 20,
      "cooling_channels": 4,
      "voltage_v": 800,
      "temperature_c": 175
    }
  },
  {
    "title": "Signature Gallium Nitride Charger: Small Power for a Laptop",
    "subject": "the Signature gallium nitride charger design",
    "description": "The Signature gallium nitride charger is a design-study for a 65 watt laptop charger that fits in 50 cubic centimeters, using gallium nitride switches at 1 megahertz.",
    "figures": {
      "power_w": 65,
      "switching_frequency_mhz": 1,
      "outputs": 2,
      "efficiency_percent": 94,
      "volume_cm3": 50,
      "temperature_c": 80,
      "protection_features": 4
    }
  },
  {
    "title": "Signature High-Bandwidth Memory Cube: Stacked Memory, Designed",
    "subject": "the Signature high-bandwidth memory cube design",
    "description": "The Signature high-bandwidth memory cube is a design-study for a stack of 8 DRAM dies holding 16 gigabytes, with a 1024-bit interface delivering 3 terabits per second.",
    "figures": {
      "dram_dies": 8,
      "capacity_gb": 16,
      "bandwidth_tbps": 3,
      "interface_bits": 1024,
      "tsv_count": 5000,
      "power_watts": 10,
      "refresh_interval_ms": 64
    }
  }
];

const SOURCES = [
  {
    "name": "Wikipedia - FinFET",
    "url": "https://en.wikipedia.org/wiki/FinFET",
    "establishes": "Defines the FinFET transistors the library is built from."
  },
  {
    "name": "Wikipedia - Transistor",
    "url": "https://en.wikipedia.org/wiki/Transistor",
    "establishes": "Background on standard cells and logic gates."
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
  const label = "darpa-semiconductor-signature-design";
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
