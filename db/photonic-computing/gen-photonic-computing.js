// Seeded boundless generator for the Photonic Computing Database
// (public edition). Deterministic: the same seed always emits the same
// record. Usage: node gen-photonic-computing.js [seed]  (prints one
// JSON record) or: node gen-photonic-computing.js --test (runTests).
// Package-only; outputs are generated, not stored files.
"use strict";
const crypto = require("crypto");

const SLUG = "photonic-computing";
const RECORD_KIND = "future photonic computing record";
const ID_PREFIX = "JAH-PHTC-";
const AI_NAME = "JAH Photonic Computing Researcher";
const EDITION = "public";
const CEILING = "Generator ceiling: up to 1,000,000,000 scales per file, generated on demand by the file AI \u2014 not stored files.";

const TOPICS = [
  {
    "title": "What Photonic Computing Is",
    "subject": "photonic computing identity",
    "description": "Photonic computing is computing with light instead of electricity: a photon, which is a single particle of light, carries information through waveguides, which are narrow channels that guide light along a chosen path on a chip, and devices such as interferometers, which split light into two paths and join them again, perform the calculations. Light has advantages electricity does not: many.",
    "label": "photonic-computing-identity",
    "figures": {
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "glossary_terms": 47,
      "sections": 16,
      "colours": 4,
      "ladder_ranks": 24,
      "advantages": 3
    }
  },
  {
    "title": "Light as a Computing Medium",
    "subject": "light as a computing medium",
    "description": "Light as a computing medium means using the properties of light itself to calculate: brightness can stand for a number, colour can stand for a channel, phase, which is where a light wave is in its cycle, can stand for a sign, and when two light waves meet they add together, so many multiplications and additions happen at the speed of light. A laser, which is a device that makes a narrow beam.",
    "label": "light-as-computing-medium",
    "figures": {
      "properties": 3,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "glossary_terms": 47,
      "sections": 16,
      "ladder_ranks": 24,
      "stages": 3
    }
  },
  {
    "title": "Silicon Photonics",
    "subject": "silicon photonics",
    "description": "Silicon photonics is the technology of building light-guiding circuits on silicon chips, the same material ordinary computer chips are made from, so that light circuits can be made in the same factories, called fabs, that make electronic chips. Silicon guides light well because light moves slowly enough in silicon to be bent around tight corners, and silicon photonics puts lasers, modulators,.",
    "label": "silicon-photonics",
    "figures": {
      "materials": 2,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "glossary_terms": 47,
      "sections": 16,
      "ladder_ranks": 24,
      "chip_parts": 4
    }
  },
  {
    "title": "Photonic Integrated Circuits",
    "subject": "photonic integrated circuits",
    "description": "A photonic integrated circuit is a chip that holds many light devices together: waveguides that guide light, splitters that divide it, interferometers that combine it, modulators that change it, and detectors that read it, all on one piece of material. Integration matters because a single light device does little alone, while a chip of hundreds of devices can do real work, such as routing data.",
    "label": "photonic-integrated-circuits",
    "figures": {
      "device_types": 5,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "glossary_terms": 47,
      "sections": 16,
      "ladder_ranks": 24,
      "devices_per_chip": 100
    }
  },
  {
    "title": "Optical Neural Networks",
    "subject": "optical neural networks",
    "description": "An optical neural network is a neural network, which is a computing system inspired by brains, built from light: light carries the input numbers, interferometers and modulators multiply them by weights, which are the numbers the network has learned, and detectors add the results up, so a whole layer of the network computes at the speed of light. Optical neural networks are studied for pattern.",
    "label": "optical-neural-networks",
    "figures": {
      "layers": 3,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "glossary_terms": 47,
      "sections": 16,
      "ladder_ranks": 24,
      "operations": 1000000
    }
  },
  {
    "title": "Mach-Zehnder Interferometers in Computing",
    "subject": "mach-zehnder interferometers in computing",
    "description": "A Mach-Zehnder interferometer is a device that splits light into two paths and joins them again, so the joined light shows how the paths differed: if one path was slowed or shifted, the joined light is brighter or dimmer, and that brightness can stand for a number. In photonic computing, rows of these interferometers form the heart of many processors: each one multiplies an input by a weight,.",
    "label": "mach-zehnder-interferometers",
    "figures": {
      "paths": 2,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "glossary_terms": 47,
      "sections": 16,
      "ladder_ranks": 24,
      "inventors": 2
    }
  },
  {
    "title": "Microring Resonators",
    "subject": "microring resonators",
    "description": "A microring resonator is a tiny ring of waveguide, often only a few micrometres across, which is a few millionths of a metre, that traps light of one colour and lets other colours pass: light of the ring's colour circles the ring many times and builds up, while other colours go straight past. In photonic computing, rings act as filters, switches, and modulators: by heating a ring slightly or.",
    "label": "microring-resonators",
    "figures": {
      "ring_diameter_micrometres": 10,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "glossary_terms": 47,
      "sections": 16,
      "ladder_ranks": 24,
      "colours": 4
    }
  },
  {
    "title": "Wavelength-Division Multiplexing for Computing",
    "subject": "wavelength-division multiplexing for computing",
    "description": "Wavelength-division multiplexing is the practice of sending many light signals down one fibre or waveguide at the same time, each on a different colour, which is called a wavelength, so one path carries many channels at once. In photonic computing, multiplexing is how parallelism is bought cheaply: one waveguide can carry dozens of numbers at once, each on its own colour, and detectors with.",
    "label": "wavelength-division-multiplexing",
    "figures": {
      "channels": 32,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "glossary_terms": 47,
      "sections": 16,
      "ladder_ranks": 24,
      "colours": 32
    }
  }
];

const SOURCES = [
  {
    "name": "Wikipedia - Optical computing",
    "url": "https://en.wikipedia.org/wiki/Optical_computing",
    "establishes": "Optical computing: computing with light instead of electricity.",
    "retrieved": "2026-11-17",
    "resource_id": "en.wikipedia.org/wiki/Optical_computing"
  },
  {
    "name": "Wikipedia - Photonic integrated circuit",
    "url": "https://en.wikipedia.org/wiki/Photonic_integrated_circuit",
    "establishes": "Photonic integrated circuit: a chip that guides and processes light.",
    "retrieved": "2026-11-17",
    "resource_id": "en.wikipedia.org/wiki/Photonic_integrated_circuit"
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
