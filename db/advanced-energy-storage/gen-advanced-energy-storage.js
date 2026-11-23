// Seeded boundless generator for the Advanced Energy Storage Database
// (public edition). Deterministic: the same seed always emits the same
// record. Usage: node gen-advanced-energy-storage.js [seed]  (prints one
// JSON record) or: node gen-advanced-energy-storage.js --test (runTests).
// Package-only; outputs are generated, not stored files.
"use strict";
const crypto = require("crypto");

const SLUG = "advanced-energy-storage";
const RECORD_KIND = "future advanced energy storage record";
const ID_PREFIX = "JAH-ADES-";
const AI_NAME = "JAH Advanced Energy Storage Librarian";
const EDITION = "public";
const CEILING = "Generator ceiling: up to 1,000,000,000 scales per file, generated on demand by the file AI \u2014 not stored files.";

const TOPICS = [
  {
    "title": "What Advanced Energy Storage Is",
    "subject": "advanced energy storage identity",
    "description": "Advanced energy storage is the set of technologies that hold energy made at one time so it can be used at a later time, going beyond the batteries in everyday use today. It covers batteries with new chemistries, storage that holds energy as moving air, as water held high, as heat, or as hydrogen gas, and the systems that manage all of them. Storage matters because sunlight and wind come and.",
    "label": "what-advanced-energy-storage-is",
    "figures": {
      "energy_density_wh_per_kg": 250,
      "round_trip_efficiency_percent": 90,
      "cycle_life": 5000,
      "lifetime_years": 15,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "sections": 14
    }
  },
  {
    "title": "Lithium-Ion Batteries at Scale",
    "subject": "lithium-ion batteries at scale",
    "description": "A lithium-ion battery is a rechargeable battery that moves lithium ions, which are charged lithium atoms, through its electrolyte to store and release energy. At small scale it powers phones and laptop computers; at large scale, thousands of cells are joined into packs that store power for homes, for vehicles, and for the grid. This record specifies how lithium-ion storage scales up: cell.",
    "label": "lithium-ion-batteries-at-scale",
    "figures": {
      "energy_density_wh_per_kg": 260,
      "round_trip_efficiency_percent": 92,
      "cycle_life": 4000,
      "lifetime_years": 12,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "sections": 14
    }
  },
  {
    "title": "Solid-State Batteries",
    "subject": "solid-state batteries",
    "description": "A solid-state battery is a battery whose electrolyte is a solid material instead of a liquid. A solid electrolyte can make the battery safer, because there is no flammable liquid to leak, and it can allow a denser anode, which is the part where current flows out, so the battery holds more energy for its size. The research problem is the boundary where the solid meets the electrodes: the.",
    "label": "solid-state-batteries",
    "figures": {
      "energy_density_wh_per_kg": 400,
      "round_trip_efficiency_percent": 90,
      "cycle_life": 3000,
      "lifetime_years": 10,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "sections": 14
    }
  },
  {
    "title": "Flow Batteries for Long Storage",
    "subject": "flow batteries for long storage",
    "description": "A flow battery is a battery that stores its energy in liquid chemicals held in tanks, and pumps those liquids past electrodes to charge and discharge. Its power depends on the size of the electrodes, and its capacity depends on the size of the tanks, so the two can be sized separately — a useful property when storage must last many hours. This record specifies flow battery research: the.",
    "label": "flow-batteries-for-long-storage",
    "figures": {
      "energy_density_wh_per_kg": 40,
      "round_trip_efficiency_percent": 75,
      "cycle_life": 10000,
      "lifetime_years": 20,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "sections": 14
    }
  },
  {
    "title": "Sodium-Ion Batteries",
    "subject": "sodium-ion batteries",
    "description": "A sodium-ion battery is a rechargeable battery that moves sodium ions, which are charged sodium atoms, instead of lithium ions. Sodium is abundant and cheap, found in ordinary salt, so sodium-ion batteries could lower the cost of storage where weight matters less than price, such as grid storage and home storage. The research question is how close sodium-ion performance can come to.",
    "label": "sodium-ion-batteries",
    "figures": {
      "energy_density_wh_per_kg": 160,
      "round_trip_efficiency_percent": 85,
      "cycle_life": 4000,
      "lifetime_years": 12,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "sections": 14
    }
  },
  {
    "title": "Grid Energy Storage",
    "subject": "grid energy storage",
    "description": "Grid energy storage is storage connected to the grid, which is the network of wires, power stations, and substations that carries electricity. It steadies the grid by absorbing power when supply is high and releasing it when demand is high, by holding frequency steady, and by keeping power on through short outages. This record specifies grid storage research: sizing, siting, control, response.",
    "label": "grid-energy-storage",
    "figures": {
      "energy_density_wh_per_kg": 200,
      "round_trip_efficiency_percent": 88,
      "cycle_life": 6000,
      "lifetime_years": 15,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "sections": 14
    }
  },
  {
    "title": "Home Battery Systems",
    "subject": "home battery systems",
    "description": "A home battery system is a battery pack installed in a home, usually beside rooftop solar panels, that stores sunshine made in the day for use in the evening. It can keep lights on through an outage, cut the home's peak demand from the grid, and let the household use more of its own solar power instead of sending it away. This record specifies home storage research: sizing for a household,.",
    "label": "home-battery-systems",
    "figures": {
      "energy_density_wh_per_kg": 180,
      "round_trip_efficiency_percent": 90,
      "cycle_life": 6000,
      "lifetime_years": 10,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "sections": 14
    }
  },
  {
    "title": "Supercapacitors and Fast Storage",
    "subject": "supercapacitors and fast storage",
    "description": "A supercapacitor is a storage device that holds electric charge directly on surfaces, charging and discharging very fast but holding less energy than a battery of the same size. Fast storage matters where power is needed in seconds — to catch a braking vehicle, to steady a grid frequency dip, or to bridge the gap until a battery takes over. This record specifies fast storage research:.",
    "label": "supercapacitors-and-fast-storage",
    "figures": {
      "energy_density_wh_per_kg": 10,
      "round_trip_efficiency_percent": 95,
      "cycle_life": 1000000,
      "lifetime_years": 20,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "sections": 14
    }
  }
];

const SOURCES = [
  {
    "name": "Wikipedia - Energy storage",
    "url": "https://en.wikipedia.org/wiki/Energy_storage",
    "establishes": "Energy storage: how energy is stored in different forms and returned when needed.",
    "retrieved": "2026-11-17",
    "resource_id": "en.wikipedia.org/wiki/Energy_storage"
  },
  {
    "name": "Wikipedia - Lithium-ion battery",
    "url": "https://en.wikipedia.org/wiki/Lithium-ion_battery",
    "establishes": "Lithium-ion battery: how the most widely used rechargeable battery chemistry works.",
    "retrieved": "2026-11-17",
    "resource_id": "en.wikipedia.org/wiki/Lithium-ion_battery"
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
