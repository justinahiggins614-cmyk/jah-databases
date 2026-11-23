// Seeded boundless generator for the Advanced Energy Storage Database
// (signature edition). Deterministic: the same seed always emits the same
// record. Usage: node gen-advanced-energy-storage-signature.js [seed]  (prints one
// JSON record) or: node gen-advanced-energy-storage-signature.js --test (runTests).
// Package-only; outputs are generated, not stored files.
"use strict";
const crypto = require("crypto");

const SLUG = "advanced-energy-storage-signature";
const RECORD_KIND = "future advanced energy storage record";
const ID_PREFIX = "JAH-ADESS-";
const AI_NAME = "JAH Advanced Energy Storage Librarian (Signature)";
const EDITION = "signature";
const CEILING = "Generator ceiling: up to 1,000,000,000 scales per file, generated on demand by the file AI \u2014 not stored files.";

const TOPICS = [
  {
    "title": "Signature Storage Vault",
    "subject": "signature storage vault",
    "description": "The Signature Storage Vault is a design for a single hall where all stored energy meets: a round room with a bay for every storage kind, a battery bay, an air bay, a water bay, a heat bay, and a hydrogen bay, with a reading desk at the center where any record can be opened in full. The design imagines storage as a vault to be walked through rather than a catalogue to be searched from outside.",
    "label": "signature-storage-vault",
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
    "title": "Signature Ion Garden",
    "subject": "signature ion garden",
    "description": "The Signature Ion Garden is a design for a battery grown like a garden: rows of cells planted in order, lithium rows beside sodium rows, each row tended by its own management electronics, and the gardener walks the rows reading voltages like leaves. The design imagines battery chemistry as cultivation, where the best rows are kept and the weak ones are replanted.",
    "label": "signature-ion-garden",
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
    "title": "Signature Solid-State Forge",
    "subject": "signature solid-state forge",
    "description": "The Signature Solid-State Forge is a design for a forge where solid batteries are made: solid electrolytes are pressed like metal, electrodes are fitted while still warm, and every finished battery is struck once to test its ring, like a bell. The design imagines solid-state making as smith work, where the join between materials is the craft.",
    "label": "signature-solid-state-forge",
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
    "title": "Signature Flow River",
    "subject": "signature flow river",
    "description": "The Signature Flow River is a design for a flow battery imagined as a river: two streams of liquid flow past each other, separated by a membrane like a riverbank, and the energy is carried in the water itself, so a bigger river holds more energy. The design imagines long storage as a river that can be widened by digging bigger tanks.",
    "label": "signature-flow-river",
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
    "title": "Signature Sodium Field",
    "subject": "signature sodium field",
    "description": "The Signature Sodium Field is a design for a field of salt-white batteries planted in rows, cheap and abundant, holding the grid's power where weight does not matter. The design imagines sodium-ion storage as farmland: broad, low-cost, and harvested in bulk, with lithium kept for the jobs where lightness matters most.",
    "label": "signature-sodium-field",
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
    "title": "Signature Grid Reservoir",
    "subject": "signature grid reservoir",
    "description": "The Signature Grid Reservoir is a design for a reservoir that steadies the grid: it fills when power is plentiful and empties when demand is high, and its keepers watch the frequency like a water level. The design imagines grid storage as a lake behind a dam, with sluice gates opened and closed by the hour.",
    "label": "signature-grid-reservoir",
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
    "title": "Signature Home Cellar",
    "subject": "signature home cellar",
    "description": "The Signature Home Cellar is a design for a cellar under a house where the day's sunshine is stored in jars, each jar a battery cell, to be drawn on in the evening. The design imagines home storage as a pantry: the household puts sunshine away in the day and takes it out at night, and the cellar keeps the lights on when the grid fails.",
    "label": "signature-home-cellar",
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
    "title": "Signature Fast Capacitor Tower",
    "subject": "signature fast capacitor tower",
    "description": "The Signature Fast Capacitor Tower is a design for a tower that answers in seconds: its supercapacitors catch braking energy, steady frequency dips, and bridge the gap until the batteries take over. The design imagines fast storage as a watchtower, always ready, quick to act, and never asked to hold power for long.",
    "label": "signature-fast-capacitor-tower",
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
