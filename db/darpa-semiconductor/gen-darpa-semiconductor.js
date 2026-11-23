// Seeded boundless generator for the darpa-semiconductor database
// (public edition). Deterministic: the same seed always emits the same
// record. Usage: node gen-darpa-semiconductor.js [seed]  (prints one
// JSON record) or: node gen-darpa-semiconductor.js --test (runTests).
// Package-only; outputs are generated, not stored files.
"use strict";
const crypto = require("crypto");

const SLUG = "darpa-semiconductor";
const RECORD_KIND = "darpa semiconductor record";
const ID_PREFIX = "JAH-DSEM-";
const AI_NAME = "JAH DARPA Semiconductor Librarian";
const CEILING = "Generator ceiling: up to 1,000,000,000 scales per file, generated on demand by the file AI \u2014 not stored files.";

const TOPICS = [
  {
    "title": "The Transistor and the CMOS Switch: The Unit of Computing",
    "subject": "the transistor and the CMOS switch",
    "description": "A transistor is a switch made from semiconductor material: a small voltage on its control terminal, called the gate, turns the flow of current between its other two terminals on or off.",
    "figures": {
      "transistor_types": 2,
      "terminals": 3,
      "switch_states": 2,
      "cmos_pair": 2,
      "leakage_paths": 3,
      "voltage_levels": 2,
      "switching_energy_fj": 1
    }
  },
  {
    "title": "Moore's Law and Density Scaling: More Transistors Every Generation",
    "subject": "Moore's law and density scaling",
    "description": "Moore's law is the observation, made by Gordon Moore in 1965, that the number of transistors on a chip doubles about every two years, and it has guided the semiconductor industry for more than five decades.",
    "figures": {
      "doubling_years": 2,
      "transistors_1971": 2300,
      "transistors_2023": 100000000000,
      "generations_counted": 25,
      "node_sizes_nm": 6,
      "scaling_factors": 3,
      "density_growth": 2
    }
  },
  {
    "title": "FinFET Transistors: The Fin That Saved Scaling",
    "subject": "FinFET transistors",
    "description": "A FinFET, short for fin field-effect transistor, is a transistor whose conducting channel is a thin vertical fin, with the gate wrapped around three sides of the fin instead of sitting flat on top.",
    "figures": {
      "fin_height_nm": 50,
      "fin_width_nm": 10,
      "gates_per_fin": 3,
      "fins_per_device": 4,
      "leakage_reduction": 10,
      "commercial_year": 2011,
      "gate_lengths_nm": 3
    }
  },
  {
    "title": "Gate-All-Around Transistors: The Gate That Wraps Everything",
    "subject": "gate-all-around transistors",
    "description": "A gate-all-around transistor, often shortened to GAA, wraps the gate around all four sides of the conducting channel, giving the gate complete control and cutting leakage further than a FinFET can.",
    "figures": {
      "sheets_per_device": 3,
      "sheet_thickness_nm": 5,
      "gate_sides": 4,
      "stacked_levels": 2,
      "leakage_reduction": 2,
      "commercial_year": 2022,
      "channel_widths_nm": 3
    }
  },
  {
    "title": "Extreme Ultraviolet Lithography: Printing with 13.5 Nanometer Light",
    "subject": "extreme ultraviolet lithography",
    "description": "Extreme ultraviolet lithography, usually shortened to EUV, prints chip patterns with light of 13.5 nanometer wavelength, which is short enough to draw features a few nanometers across.",
    "figures": {
      "wavelength_nm": 13,
      "mirrors": 10,
      "power_watts": 250,
      "throughput_wafers_hour": 100,
      "mask_layers": 4,
      "defect_budget": 1,
      "commercial_year": 2019
    }
  },
  {
    "title": "Deep Ultraviolet Lithography and Multi-Patterning",
    "subject": "deep ultraviolet lithography and multi-patterning",
    "description": "Deep ultraviolet lithography, usually shortened to DUV, prints chip patterns with 193 nanometer light, and it was the workhorse of chipmaking for two decades before EUV arrived.",
    "figures": {
      "wavelength_nm": 193,
      "patterning_passes": 4,
      "immersion_factor": 1,
      "overlay_nm": 3,
      "layers_multipatterned": 5,
      "cost_multiplier": 2,
      "throughput_wafers_hour": 200
    }
  },
  {
    "title": "Photolithography and the Mask: The Stencil of Chipmaking",
    "subject": "photolithography and the mask",
    "description": "Photolithography is the process of printing chip patterns with light: a photosensitive coating called resist is exposed through a mask, the exposed parts are developed away, and the remaining pattern guides etching or deposition.",
    "figures": {
      "mask_layers": 4,
      "exposure_steps": 5,
      "resist_types": 2,
      "alignment_marks": 4,
      "defect_limit": 1,
      "reticle_size_mm": 26,
      "stepper_fields": 3
    }
  },
  {
    "title": "The Wafer and the Cleanroom: Where Chips Are Born",
    "subject": "the wafer and the cleanroom",
    "description": "A wafer is a thin disc of silicon, 300 millimeters across in modern fabs, on which hundreds of chips are built at once before the wafer is cut into individual chips.",
    "figures": {
      "wafer_diameter_mm": 300,
      "chips_per_wafer": 500,
      "cleanroom_class": 1,
      "particle_limit": 1,
      "air_changes_hour": 100,
      "process_steps": 500,
      "fab_cost_billion": 10
    }
  }
];

const SOURCES = [
  {
    "name": "Wikipedia - Transistor",
    "url": "https://en.wikipedia.org/wiki/Transistor",
    "establishes": "Defines the transistor, its terminals, and CMOS pairing."
  },
  {
    "name": "Wikipedia - Moore's law",
    "url": "https://en.wikipedia.org/wiki/Moore%27s_law",
    "establishes": "Places the transistor inside the scaling story."
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
  const label = "darpa-semiconductor-overview";
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
