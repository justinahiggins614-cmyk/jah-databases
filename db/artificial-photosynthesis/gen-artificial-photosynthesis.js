// Seeded boundless generator for the Artificial Photosynthesis Database
// (public edition). Deterministic: the same seed always emits the same
// record. Usage: node gen-artificial-photosynthesis.js [seed]  (prints one
// JSON record) or: node gen-artificial-photosynthesis.js --test (runTests).
// Package-only; outputs are generated, not stored files.
"use strict";
const crypto = require("crypto");

const SLUG = "artificial-photosynthesis";
const RECORD_KIND = "future artificial photosynthesis record";
const ID_PREFIX = "JAH-APHO-";
const AI_NAME = "JAH Artificial Photosynthesis Librarian";
const EDITION = "public";
const CEILING = "Generator ceiling: up to 1,000,000,000 scales per file, generated on demand by the file AI \u2014 not stored files.";

const TOPICS = [
  {
    "title": "What Artificial Photosynthesis Is",
    "subject": "artificial photosynthesis identity",
    "description": "Artificial photosynthesis is a human-made system that copies the plant process, using sunlight to split water or to turn carbon dioxide into a fuel. A plant uses sunlight, water, and carbon dioxide to make sugars and oxygen; an artificial system uses sunlight, water, and carbon dioxide to make hydrogen or a carbon-based fuel that can be stored and used later. The work is experimental: devices.",
    "label": "what-artificial-photosynthesis-is",
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
    "title": "Natural Photosynthesis as the Model",
    "subject": "natural photosynthesis as the model",
    "description": "Natural photosynthesis is the process green plants use to turn sunlight, water, and carbon dioxide into sugars and oxygen, and it is the model every artificial system copies. Plants split water to release oxygen, move electrons through a chain of proteins, and use that energy to fix carbon dioxide into sugars. The plant's tricks worth copying are its use of abundant materials, its repair of.",
    "label": "natural-photosynthesis-as-the-model",
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
    "title": "Water Splitting for Hydrogen",
    "subject": "water splitting for hydrogen",
    "description": "Water splitting is the chemical change that breaks water into hydrogen and oxygen using energy, here energy from sunlight. Hydrogen is the lightest chemical element, a gas that can be burned or used in a fuel cell to release energy, leaving water behind. A water-splitting device must do two hard jobs at once: catch sunlight efficiently, and drive the chemistry fast enough to matter, without.",
    "label": "water-splitting-for-hydrogen",
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
    "title": "Carbon Dioxide Reduction to Fuels",
    "subject": "carbon dioxide reduction to fuels",
    "description": "Carbon dioxide reduction is the chemical change that turns carbon dioxide, the gas in the air made when fuels burn, into a fuel such as carbon monoxide, methanol, or methane, using energy from sunlight. It is harder than water splitting, because the reaction has many possible products and the device must choose the wanted one. This record specifies the research: catalysts that select one.",
    "label": "carbon-dioxide-reduction-to-fuels",
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
    "title": "Photocatalysts and Light Absorbers",
    "subject": "photocatalysts and light absorbers",
    "description": "A photocatalyst is a material that speeds up a chemical change when light falls on it, without being used up itself, and a light absorber is the part of a device that catches sunlight and turns it into electric charges that can do chemical work. The two are often the same material doing both jobs. The research problem is finding materials that absorb enough sunlight, last in water and light,.",
    "label": "photocatalysts-and-light-absorbers",
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
    "title": "Photoelectrochemical Cells",
    "subject": "photoelectrochemical cells",
    "description": "A photoelectrochemical cell is a device that uses light falling on a material in a liquid to drive a chemical change, such as splitting water. The cell holds the light absorber in an electrolyte, which is the liquid that lets charged particles move, and wires carry the charges to where the chemistry happens. Its design must balance light catching, charge movement, and chemical speed, all in.",
    "label": "photoelectrochemical-cells",
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
    "title": "Solar Fuels",
    "subject": "solar fuels",
    "description": "A solar fuel is a fuel made using sunlight, such as hydrogen made by splitting water with sunlight, that can be stored and used later. Solar fuels are valuable because fuels can be stored for months, moved by pipe or ship, and used in engines and furnaces that electricity cannot easily serve. This record specifies the research: which fuels to make, how to measure the sunlight-to-fuel.",
    "label": "solar-fuels",
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
    "title": "Catalysts for Oxygen Production",
    "subject": "catalysts for oxygen production",
    "description": "Catalysts for oxygen production are the materials that speed up the half of water splitting that releases oxygen, which is the harder half of the reaction because it must move four electrons and four protons at once. Plants use a cluster of manganese and calcium atoms for this job, and researchers copy that cluster and invent new ones from abundant metals. This record specifies the research:.",
    "label": "catalysts-for-oxygen-production",
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
