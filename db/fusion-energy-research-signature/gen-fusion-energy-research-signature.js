// Seeded boundless generator for the Fusion Energy Database
// (signature edition). Deterministic: the same seed always emits the same
// record. Usage: node gen-fusion-energy-research-signature.js [seed]  (prints one
// JSON record) or: node gen-fusion-energy-research-signature.js --test (runTests).
// Package-only; outputs are generated, not stored files.
"use strict";
const crypto = require("crypto");

const SLUG = "fusion-energy-research-signature";
const RECORD_KIND = "future fusion energy research record";
const ID_PREFIX = "JAH-FERS-";
const AI_NAME = "JAH Fusion Energy Research Librarian (Signature)";
const EDITION = "signature";
const CEILING = "Generator ceiling: up to 1,000,000,000 scales per file, generated on demand by the file AI \u2014 not stored files.";

const TOPICS = [
  {
    "title": "A Tabletop Fusion Model",
    "subject": "tabletop fusion model design",
    "description": "This design-study imagines a tabletop model of fusion for teaching: a glass doughnut holding a glowing gas, with magnets around it that visitors can switch on and off to see the glow squeeze into a ring. The model shows the idea of magnetic confinement without any real plasma: the glow is a safe lamp, the magnets are small, and a dial lets the visitor raise the heat and watch the ring.",
    "label": "tabletop-fusion-model",
    "figures": {
      "magnets": 8,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "glossary_terms": 50,
      "sections": 16,
      "dials": 1
    }
  },
  {
    "title": "A D-T Fuel Capsule Design",
    "subject": "d-t fuel capsule design",
    "description": "This design-study imagines a D-T fuel capsule design: a frozen sphere of deuterium-tritium fuel, layered inside a plastic shell, with the layer thicknesses drawn to a thousandth of a millimetre. The design is a drawing and a simulation only: it studies how even the layers must be for a symmetric squeeze, and it never builds a capsule. The design adds a symmetry gauge, a simulated measure of.",
    "label": "d-t-fuel-capsule-design",
    "figures": {
      "layers": 3,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "glossary_terms": 50,
      "sections": 16,
      "tolerance_um": 1
    }
  },
  {
    "title": "A Lawson Criterion Slide Rule",
    "subject": "lawson criterion slide rule design",
    "description": "This design-study imagines a Lawson criterion slide rule: a teaching instrument with three sliding scales, one for density, one for temperature, and one for confinement time, that multiply to the triple product as the user slides them. When the product passes the threshold for the D-T reaction, which is the deuterium-tritium reaction, a lamp lights, showing the student that the three numbers.",
    "label": "lawson-criterion-slide-rule",
    "figures": {
      "scales": 3,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "glossary_terms": 50,
      "sections": 16,
      "lamps": 1
    }
  },
  {
    "title": "A Tokamak Control Room Study",
    "subject": "tokamak control room design",
    "description": "This design-study imagines a tokamak control room: a room where operators watch the plasma's shape on wall screens, read the heating power and the Q factor, which is the fusion energy gain factor, on dials, and hold a shutdown handle that ends a pulse in a second. The design gives each operator one job, one for shape, one for heating, one for fuel, and one for safety, so no person watches.",
    "label": "tokamak-control-room-study",
    "figures": {
      "operators": 4,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "glossary_terms": 50,
      "sections": 16,
      "screens": 4
    }
  },
  {
    "title": "A Stellarator Coil Workshop",
    "subject": "stellarator coil workshop design",
    "description": "This design-study imagines a stellarator coil workshop: a workshop where twisted magnetic coils are wound, measured, and fitted, with a laser scanner that checks each coil against its design to a fraction of a millimetre. The workshop keeps a coil library, where every coil's shape, measurement, and test result is filed, so a coil that fails can be traced back to its winding. The design is a.",
    "label": "stellarator-coil-workshop",
    "figures": {
      "coils": 50,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "glossary_terms": 50,
      "sections": 16,
      "scanners": 2
    }
  },
  {
    "title": "An ITER-Scale Q = 10 Demonstrator",
    "subject": "iter-scale q10 demonstrator design",
    "description": "This design-study imagines an ITER-scale Q = 10 demonstrator: a design model of a tokamak built to the ITER (International Thermonuclear Experimental Reactor) design goal, 500 MW (megawatt) of fusion power from 50 MW (megawatt) of heating power, giving Q = 10. The demonstrator is a design and a simulation only: it draws the machine, its magnets, its heating, and its blanket, and it computes.",
    "label": "iter-scale-q10-demonstrator",
    "figures": {
      "fusion_power_mw": 500,
      "heating_power_mw": 50,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "glossary_terms": 50,
      "sections": 16,
      "q_target": 10
    }
  },
  {
    "title": "A JET-Style D-T Campaign Plan",
    "subject": "jet-style d-t campaign plan design",
    "description": "This design-study imagines a JET-style D-T campaign plan: a plan for a series of experiments on a tokamak running the real D-T fuel, which is the deuterium-tritium fuel pair, written the way JET (Joint European Torus) ran its campaigns. The plan lists the pulses in order, the heating steps, the tritium accounting at each step, and the stop rules that end the campaign if the walls show damage..",
    "label": "jet-style-d-t-campaign-plan",
    "figures": {
      "pulses": 100,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "glossary_terms": 50,
      "sections": 16,
      "stop_rules": 3
    }
  },
  {
    "title": "A Laser Pellet Squeeze Simulator",
    "subject": "laser pellet squeeze simulator design",
    "description": "This design-study imagines a laser pellet squeeze simulator: a computer model that shows a D-T fuel pellet, which is a deuterium-tritium fuel pellet, being squeezed by lasers, with the squeeze shown in slow motion and the symmetry measured at every step. The simulator lets a student change the laser timing and watch the pellet squeeze evenly or lopsidedly, learning why symmetry decides.",
    "label": "laser-pellet-squeeze-simulator",
    "figures": {
      "laser_beams": 192,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "glossary_terms": 50,
      "sections": 16,
      "steps_shown": 10
    }
  }
];

const SOURCES = [
  {
    "name": "Wikipedia - Fusion power",
    "url": "https://en.wikipedia.org/wiki/Fusion_power",
    "establishes": "Fusion power: the science and engineering of producing energy from fusion reactions.",
    "retrieved": "2026-11-17",
    "resource_id": "en.wikipedia.org/wiki/Fusion_power"
  },
  {
    "name": "Wikipedia - Tokamak",
    "url": "https://en.wikipedia.org/wiki/Tokamak",
    "establishes": "Tokamak: the doughnut-shaped magnetic chamber that holds hot plasma for fusion.",
    "retrieved": "2026-11-17",
    "resource_id": "en.wikipedia.org/wiki/Tokamak"
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
    description: topic.description + " " + "No claim of consciousness, sentience, or unlimited intelligence is established by this system; future-technology framing here is a research or design claim only, never established fact.",
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
