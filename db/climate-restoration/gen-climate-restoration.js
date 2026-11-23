// Seeded boundless generator for the Climate Restoration Research Database
// (public edition). Deterministic: the same seed always emits the same
// record. Usage: node gen-climate-restoration.js [seed]  (prints one
// JSON record) or: node gen-climate-restoration.js --test (runTests).
// Package-only; outputs are generated, not stored files.
"use strict";
const crypto = require("crypto");

const SLUG = "climate-restoration";
const RECORD_KIND = "future climate restoration research record";
const ID_PREFIX = "JAH-CLRE-";
const AI_NAME = "JAH Climate Restoration Researcher";
const EDITION = "public";
const CEILING = "Generator ceiling: up to 1,000,000,000 scales per file, generated on demand by the file AI \u2014 not stored files.";

const TOPICS = [
  {
    "title": "What Climate Restoration Research Is",
    "subject": "climate restoration research identity",
    "description": "Climate restoration research is the study of how the climate system might be helped to recover: removing carbon dioxide, which is the gas that warms the planet, from the air and storing it; restoring forests, wetlands, and soils that store carbon; and studying large-scale interventions, called geoengineering, which is large-scale research into changing the climate system on purpose. The field.",
    "label": "climate-restoration-identity",
    "figures": {
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "glossary_terms": 47,
      "sections": 16,
      "research_areas": 3,
      "ladder_ranks": 24,
      "paris_year": 2015
    }
  },
  {
    "title": "Carbon Dioxide Removal Overview",
    "subject": "carbon dioxide removal overview",
    "description": "Carbon dioxide removal, shortened to CDR (Carbon Dioxide Removal), is the family of methods that take carbon dioxide out of the air and store it somewhere it stays put: in trees and soils, in rocks, in the deep ocean, or underground in old gas fields. Removal is different from cutting emissions: cutting emissions stops new gas going up, while removal takes old gas down, and the climate needs.",
    "label": "carbon-dioxide-removal-overview",
    "figures": {
      "removal_methods": 6,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "glossary_terms": 47,
      "sections": 16,
      "ladder_ranks": 24,
      "storage_places": 4
    }
  },
  {
    "title": "Direct Air Capture",
    "subject": "direct air capture",
    "description": "Direct air capture, shortened to DAC (Direct Air Capture), is the use of machines to pull carbon dioxide straight out of the open air: large fans blow air over filters or liquids that catch the gas, the filters are then heated or treated to release the gas in pure form, and the pure gas is stored underground or used in products. DAC (Direct Air Capture) works anywhere, because air is.",
    "label": "direct-air-capture",
    "figures": {
      "carbon_per_10000_air": 4,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "glossary_terms": 47,
      "sections": 16,
      "ladder_ranks": 24,
      "capture_steps": 3
    }
  },
  {
    "title": "Enhanced Rock Weathering",
    "subject": "enhanced rock weathering",
    "description": "Enhanced rock weathering is the speeding up of a natural process: rain slowly dissolves certain rocks, and the dissolved minerals capture carbon dioxide from the air and carry it to the sea, where it is stored as bicarbonate, which is a dissolved form of carbon. Spreading crushed basalt, a dark volcanic rock, on fields speeds the process up, and the rock also gives minerals to the soil, but.",
    "label": "enhanced-rock-weathering",
    "figures": {
      "rock_types": 2,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "glossary_terms": 47,
      "sections": 16,
      "ladder_ranks": 24,
      "capture_years": 5
    }
  },
  {
    "title": "Ocean Alkalinity Enhancement",
    "subject": "ocean alkalinity enhancement",
    "description": "Ocean alkalinity enhancement is the study of adding alkaline materials, such as crushed limestone or olivine, to seawater so the ocean can hold more carbon dioxide: alkalinity is the measure of how much a liquid such as seawater can absorb acid without changing, and raising it lets the ocean draw more carbon dioxide from the air and store it as bicarbonate, which is a dissolved form of carbon..",
    "label": "ocean-alkalinity-enhancement",
    "figures": {
      "alkaline_materials": 2,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "glossary_terms": 47,
      "sections": 16,
      "ladder_ranks": 24,
      "ocean_stores": 1
    }
  },
  {
    "title": "Reforestation and Afforestation",
    "subject": "reforestation and afforestation",
    "description": "Reforestation is planting forests again where they were lost, and afforestation is planting forests where there were none before, and both store carbon dioxide in trees, roots, and soil as the forest grows. Forests are the most proven form of carbon dioxide removal, with centuries of knowledge about how trees grow, but they are slow, they need land and water, they can burn and release their.",
    "label": "reforestation-afforestation",
    "figures": {
      "forest_types": 2,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "glossary_terms": 47,
      "sections": 16,
      "ladder_ranks": 24,
      "growth_years": 20
    }
  },
  {
    "title": "Soil Carbon Restoration",
    "subject": "soil carbon restoration",
    "description": "Soil carbon restoration is the work of increasing the carbon stored in soil, which already holds more carbon than the air and all plants together: soil carbon grows when plants are grown and their roots and fallen leaves feed the soil, and it falls when soil is ploughed, overgrazed, or left bare. Practices studied include cover crops, which are plants grown to protect soil between harvests,.",
    "label": "soil-carbon-restoration",
    "figures": {
      "practices": 4,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "glossary_terms": 47,
      "sections": 16,
      "ladder_ranks": 24,
      "carbon_pools": 2
    }
  },
  {
    "title": "Wetland and Peatland Restoration",
    "subject": "wetland and peatland restoration",
    "description": "Wetland and peatland restoration is the work of bringing back marshes, swamps, and peat bogs, which are waterlogged lands where dead plants pile up as peat, a dark spongy material that stores carbon for thousands of years because the water keeps it from rotting. Drained peatlands release their stored carbon as they dry, so rewetting them, which means letting water back in, stops the release.",
    "label": "wetland-peatland-restoration",
    "figures": {
      "wetland_types": 2,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "glossary_terms": 47,
      "sections": 16,
      "ladder_ranks": 24,
      "storage_years": 1000
    }
  }
];

const SOURCES = [
  {
    "name": "Wikipedia - Carbon dioxide removal",
    "url": "https://en.wikipedia.org/wiki/Carbon_dioxide_removal",
    "establishes": "Carbon dioxide removal: taking carbon dioxide out of the air and storing it.",
    "retrieved": "2026-11-17",
    "resource_id": "en.wikipedia.org/wiki/Carbon_dioxide_removal"
  },
  {
    "name": "Wikipedia - Climate change mitigation",
    "url": "https://en.wikipedia.org/wiki/Climate_change_mitigation",
    "establishes": "Climate change mitigation: reducing emissions and removing carbon dioxide to limit warming.",
    "retrieved": "2026-11-17",
    "resource_id": "en.wikipedia.org/wiki/Climate_change_mitigation"
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
