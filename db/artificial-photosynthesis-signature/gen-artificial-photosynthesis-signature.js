// Seeded boundless generator for the Artificial Photosynthesis Database
// (signature edition). Deterministic: the same seed always emits the same
// record. Usage: node gen-artificial-photosynthesis-signature.js [seed]  (prints one
// JSON record) or: node gen-artificial-photosynthesis-signature.js --test (runTests).
// Package-only; outputs are generated, not stored files.
"use strict";
const crypto = require("crypto");

const SLUG = "artificial-photosynthesis-signature";
const RECORD_KIND = "future artificial photosynthesis record";
const ID_PREFIX = "JAH-APHOS-";
const AI_NAME = "JAH Artificial Photosynthesis Librarian (Signature)";
const EDITION = "signature";
const CEILING = "Generator ceiling: up to 1,000,000,000 scales per file, generated on demand by the file AI \u2014 not stored files.";

const TOPICS = [
  {
    "title": "Signature Sun Leaf",
    "subject": "signature sun leaf",
    "description": "The Signature Sun Leaf is a design for a leaf that makes fuel from sunlight: its light absorber is the green of the leaf, its catalysts are the veins, and its fuel drips from the stem into a jar. The design imagines the whole solar fuel system as one leaf, simple to see and simple to tend, with a field of leaves as the plant that makes fuel.",
    "label": "signature-sun-leaf",
    "figures": {
      "solar_to_fuel_efficiency_percent": 10,
      "operating_hours": 1000,
      "stability_days": 30,
      "device_area_sq_cm": 25,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "sections": 14
    }
  },
  {
    "title": "Signature Green Model",
    "subject": "signature green model",
    "description": "The Signature Green Model is a design for a glasshouse where the plant process is studied leaf by leaf: real plants grow beside artificial ones, and every trick the plant uses is written down before it is copied. The design imagines research as gardening, where the model is tended before the machine is built.",
    "label": "signature-green-model",
    "figures": {
      "solar_to_fuel_efficiency_percent": 3,
      "operating_hours": 8760,
      "stability_days": 365,
      "device_area_sq_cm": 100,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "sections": 14
    }
  },
  {
    "title": "Signature Water Splitter",
    "subject": "signature water splitter",
    "description": "The Signature Water Splitter is a design for a mill that splits water with sunlight: light falls on the wheel, the wheel turns the chemistry, and hydrogen bubbles up on one side while oxygen bubbles up on the other. The design imagines water splitting as milling, where sunlight is the stream that turns the wheel.",
    "label": "signature-water-splitter",
    "figures": {
      "solar_to_fuel_efficiency_percent": 12,
      "operating_hours": 2000,
      "stability_days": 60,
      "device_area_sq_cm": 10,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "sections": 14
    }
  },
  {
    "title": "Signature Carbon Kitchen",
    "subject": "signature carbon kitchen",
    "description": "The Signature Carbon Kitchen is a design for a kitchen where carbon dioxide is cooked into fuel: the chef is the catalyst, the recipe is the reaction, and the dish served is methanol. The design imagines carbon chemistry as cooking, where the cook must choose one dish out of many possible ones and serve it the same way every time.",
    "label": "signature-carbon-kitchen",
    "figures": {
      "solar_to_fuel_efficiency_percent": 8,
      "operating_hours": 1500,
      "stability_days": 45,
      "device_area_sq_cm": 10,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "sections": 14
    }
  },
  {
    "title": "Signature Light Catcher",
    "subject": "signature light catcher",
    "description": "The Signature Light Catcher is a design for a net that catches sunlight: fine threads of semiconductor are woven into a cloth, and every photon caught frees a charge that runs down the thread to do chemistry. The design imagines light catching as fishing, where a wider net and a finer mesh catch more of the sun.",
    "label": "signature-light-catcher",
    "figures": {
      "solar_to_fuel_efficiency_percent": 9,
      "operating_hours": 2000,
      "stability_days": 90,
      "device_area_sq_cm": 5,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "sections": 14
    }
  },
  {
    "title": "Signature Sun Cell",
    "subject": "signature sun cell",
    "description": "The Signature Sun Cell is a design for a cell like a small room: light enters through the window, which is the light absorber, and chemistry happens at the benches inside, with the liquid electrolyte as the floor. The design imagines the photoelectrochemical cell as a room where light, liquid, and chemistry must live together in balance.",
    "label": "signature-sun-cell",
    "figures": {
      "solar_to_fuel_efficiency_percent": 11,
      "operating_hours": 1800,
      "stability_days": 60,
      "device_area_sq_cm": 25,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "sections": 14
    }
  },
  {
    "title": "Signature Solar Fuel Still",
    "subject": "signature solar fuel still",
    "description": "The Signature Solar Fuel Still is a design for a still that brews fuel from sunlight the way a still brews spirit from grain: sunlight is the fire, water and carbon dioxide are the mash, and the fuel drips out slow and pure. The design imagines solar fuel making as brewing, where patience and a clean still matter more than speed.",
    "label": "signature-solar-fuel-still",
    "figures": {
      "solar_to_fuel_efficiency_percent": 10,
      "operating_hours": 2000,
      "stability_days": 90,
      "device_area_sq_cm": 25,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "sections": 14
    }
  },
  {
    "title": "Signature Oxygen Fountain",
    "subject": "signature oxygen fountain",
    "description": "The Signature Oxygen Fountain is a design for a fountain that releases oxygen: water is lifted by sunlight, the catalyst is the stone at the fountain's heart, and oxygen bubbles up like water over stone. The design imagines the hard half of water splitting as a fountain, where the stone must keep working while the water never stops.",
    "label": "signature-oxygen-fountain",
    "figures": {
      "solar_to_fuel_efficiency_percent": 7,
      "operating_hours": 1500,
      "stability_days": 60,
      "device_area_sq_cm": 5,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "sections": 14
    }
  }
];

const SOURCES = [
  {
    "name": "Wikipedia - Artificial photosynthesis",
    "url": "https://en.wikipedia.org/wiki/Artificial_photosynthesis",
    "establishes": "Artificial photosynthesis: how human-made systems copy plants to make fuels from sunlight.",
    "retrieved": "2026-11-17",
    "resource_id": "en.wikipedia.org/wiki/Artificial_photosynthesis"
  },
  {
    "name": "Wikipedia - Photosynthesis",
    "url": "https://en.wikipedia.org/wiki/Photosynthesis",
    "establishes": "Photosynthesis: how green plants turn sunlight, water, and carbon dioxide into sugars and oxygen.",
    "retrieved": "2026-11-17",
    "resource_id": "en.wikipedia.org/wiki/Photosynthesis"
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
