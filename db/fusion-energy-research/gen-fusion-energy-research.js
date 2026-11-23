// Seeded boundless generator for the Fusion Energy Database
// (public edition). Deterministic: the same seed always emits the same
// record. Usage: node gen-fusion-energy-research.js [seed]  (prints one
// JSON record) or: node gen-fusion-energy-research.js --test (runTests).
// Package-only; outputs are generated, not stored files.
"use strict";
const crypto = require("crypto");

const SLUG = "fusion-energy-research";
const RECORD_KIND = "future fusion energy research record";
const ID_PREFIX = "JAH-FER-";
const AI_NAME = "JAH Fusion Energy Research Librarian";
const EDITION = "public";
const CEILING = "Generator ceiling: up to 1,000,000,000 scales per file, generated on demand by the file AI \u2014 not stored files.";

const TOPICS = [
  {
    "title": "What Fusion Energy Research Is",
    "subject": "fusion energy research identity",
    "description": "Fusion energy research is the science and engineering of producing energy from fusion, which is the joining of light atomic nuclei to form a heavier nucleus, releasing energy, the process that powers the Sun. The research goal is to hold a hot fuel, called plasma, which is a hot gas of charged particles, hot enough and dense enough and long enough that fusion reactions release more energy than.",
    "label": "what-fusion-energy-research-is",
    "figures": {
      "paths": 2,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "glossary_terms": 50,
      "sections": 16,
      "research_parts": 10
    }
  },
  {
    "title": "The Deuterium-Tritium Reaction",
    "subject": "deuterium-tritium reaction",
    "description": "The deuterium-tritium reaction, shortened to D-T, is the fusion reaction every major experiment aims for, because it is the easiest fusion reaction to start. Deuterium is a heavy form of hydrogen, with one proton and one neutron, and tritium is a heavy form of hydrogen, with one proton and two neutrons. When a deuterium nucleus and a tritium nucleus join, they form a helium nucleus and a.",
    "label": "deuterium-tritium-reaction",
    "figures": {
      "fuels": 2,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "glossary_terms": 50,
      "sections": 16,
      "temperature_million_k": 150
    }
  },
  {
    "title": "The Lawson Criterion",
    "subject": "lawson criterion",
    "description": "The Lawson criterion is the condition of temperature, density, and time that fusion must meet, named after the physicist John Lawson, who stated it in 1957. It says that the product of the plasma's density, which is how many fuel particles crowd each volume, and its confinement time, which is how long the heat stays trapped, must pass a threshold that rises with temperature, before the fusion.",
    "label": "lawson-criterion",
    "figures": {
      "factors": 3,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "glossary_terms": 50,
      "sections": 16,
      "year_stated": 1957
    }
  },
  {
    "title": "Tokamaks",
    "subject": "tokamaks",
    "description": "A tokamak is a doughnut-shaped chamber that holds hot plasma in place with magnetic fields so fusion can happen inside it, and it is the leading design for magnetic confinement fusion. The name comes from Russian words for a toroidal chamber with magnetic coils. The plasma runs as a ring inside the doughnut, held away from the walls by magnetic fields, and heated until it is hot enough to.",
    "label": "tokamaks",
    "figures": {
      "chambers": 1,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "glossary_terms": 50,
      "sections": 16,
      "major_machines": 2
    }
  },
  {
    "title": "Stellarators",
    "subject": "stellarators",
    "description": "A stellarator is a twisted chamber that holds hot plasma in place with magnetic fields, like a tokamak but with a more complex twisted shape, and it is the tokamak's great rival. Where a tokamak drives a current through the plasma to shape its field, a stellarator shapes its field entirely with twisted magnetic coils outside the plasma, so it needs no plasma current and can run steadily.",
    "label": "stellarators",
    "figures": {
      "coil_shapes": 3,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "glossary_terms": 50,
      "sections": 16,
      "major_machines": 1
    }
  },
  {
    "title": "ITER",
    "subject": "iter",
    "description": "ITER, which stands for International Thermonuclear Experimental Reactor, is the large international fusion experiment being built in France, and it is the largest fusion experiment ever attempted. ITER is a tokamak, a doughnut-shaped chamber that holds hot plasma with magnetic fields, built by seven members, the European Union, China, India, Japan, Korea, Russia, and the United States, at a.",
    "label": "iter",
    "figures": {
      "members": 7,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "glossary_terms": 50,
      "sections": 16,
      "q_target": 10
    }
  },
  {
    "title": "JET",
    "subject": "jet",
    "description": "JET, which stands for Joint European Torus, is the European fusion experiment in England, and it was the world's largest tokamak for decades. JET is a tokamak, a doughnut-shaped chamber that holds hot plasma with magnetic fields, and it is the only machine so far to have run on the real D-T fuel, which is the deuterium-tritium fuel pair, at large scale. In its final campaigns it set records.",
    "label": "jet",
    "figures": {
      "campaigns": 3,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "glossary_terms": 50,
      "sections": 16,
      "fuel_kinds": 2
    }
  },
  {
    "title": "Inertial Confinement Fusion",
    "subject": "inertial confinement fusion",
    "description": "Inertial confinement fusion is fusion by squeezing a fuel pellet with lasers or beams, so fast that fusion happens before the pellet flies apart. The pellet is a tiny frozen sphere of D-T fuel, which is the deuterium-tritium fuel pair, and the lasers strike it from all sides, ablating, which means blowing off, its outer layer, so the recoil crushes the inside to enormous density and.",
    "label": "inertial-confinement-fusion",
    "figures": {
      "lasers": 192,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "glossary_terms": 50,
      "sections": 16,
      "squeeze_time_ns": 1
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
