// Seeded boundless generator for the Programmable Materials Database
// (signature edition). Deterministic: the same seed always emits the same
// record. Usage: node gen-programmable-materials-signature.js [seed]  (prints one
// JSON record) or: node gen-programmable-materials-signature.js --test (runTests).
// Package-only; outputs are generated, not stored files.
"use strict";
const crypto = require("crypto");

const SLUG = "programmable-materials-signature";
const RECORD_KIND = "future programmable materials record";
const ID_PREFIX = "JAH-PROMATS-";
const AI_NAME = "JAH Programmable Materials Librarian (Signature)";
const EDITION = "signature";
const CEILING = "Generator ceiling: up to 1,000,000,000 scales per file, generated on demand by the file AI \u2014 not stored files.";

const TOPICS = [
  {
    "title": "A Shape-Shifting Bridge Joint",
    "subject": "shape-shifting bridge joint design",
    "description": "This design-study imagines a bridge joint built from shape-memory alloy that adjusts itself as the bridge warms and cools. In summer the joint holds the bridge deck firmly, and in winter it relaxes to let the deck shrink without cracking, and the switch is driven by temperature alone, with no motor and no controller. The design adds a sensor wire that reports the joint's shape, so engineers.",
    "label": "shape-shifting-bridge-joint",
    "figures": {
      "seasons": 2,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "glossary_terms": 50,
      "sections": 16,
      "sensors": 2
    }
  },
  {
    "title": "A Self-Fitting Splint Study",
    "subject": "self-fitting splint design",
    "description": "This design-study imagines a splint made from shape-memory polymer that softens in warm water, is shaped around a limb, and then stiffens as it cools to hold its form. The study is a design for a splint shape only: it is research, with no medical advice and no dosing information given here, and it makes no claim that the design is safe or effective for any person. The design adds a colour.",
    "label": "self-fitting-splint-study",
    "figures": {
      "shape_steps": 3,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "glossary_terms": 50,
      "sections": 16,
      "colour_states": 2
    }
  },
  {
    "title": "An Electroactive Artificial Muscle",
    "subject": "electroactive artificial muscle design",
    "description": "This design-study imagines an artificial muscle made from a stack of dielectric elastomer films, each film spreading wider when voltage is applied and relaxing when it is removed, so the stack pulls like a muscle. The muscle is soft, quiet, and light, and it is designed for a robot arm that must work beside people without the danger of a hard motor. The design adds a strain gauge, which is a.",
    "label": "electroactive-artificial-muscle",
    "figures": {
      "films": 20,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "glossary_terms": 50,
      "sections": 16,
      "sensors": 1
    }
  },
  {
    "title": "A Magnetorheological Shock Absorber",
    "subject": "magnetorheological shock absorber design",
    "description": "This design-study imagines a shock absorber filled with magnetorheological fluid, whose stiffness is set by a magnetic field that a controller adjusts a thousand times a second. On a smooth road the field is low and the ride is soft, and on a rough road the field rises and the absorber stiffens before the bump is felt. The design adds a learning controller that remembers the road and prepares.",
    "label": "magnetorheological-shock-absorber",
    "figures": {
      "adjustments_per_second": 1000,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "glossary_terms": 50,
      "sections": 16,
      "states": 2
    }
  },
  {
    "title": "A Phase-Change Cooling Wall",
    "subject": "phase-change cooling wall design",
    "description": "This design-study imagines a wall filled with phase-change wax that melts during the day, absorbing heat without warming, and freezes at night, releasing the heat back. The wall is built as panels that can be swapped out when the wax tires, and each panel carries a label stating its melting point and its cycle count, so the building keeper knows when to replace it. The design is a proposal.",
    "label": "phase-change-cooling-wall",
    "figures": {
      "panels": 12,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "glossary_terms": 50,
      "sections": 16,
      "melting_points": 1
    }
  },
  {
    "title": "A Self-Healing Phone Skin",
    "subject": "self-healing phone skin design",
    "description": "This design-study imagines a phone skin made from self-healing polymer with tiny capsules of liquid glue, so a scratch breaks a capsule, the glue fills the scratch, and the skin is smooth again by morning. The design adds a healing counter on the phone that reports how many scratches have healed and how much glue remains, so the owner knows when the skin is spent. The design is a proposal.",
    "label": "self-healing-phone-skin",
    "figures": {
      "capsules": 1000,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "glossary_terms": 50,
      "sections": 16,
      "heals": 50
    }
  },
  {
    "title": "A Sun-Tracking Window Film",
    "subject": "sun-tracking window film design",
    "description": "This design-study imagines a window film made from photo-responsive material that darkens where the sun hits it and stays clear where the sun does not, so each part of the window shades itself. The film needs no wires and no power, because sunlight itself is the trigger, and it clears again as the sun moves on. The design adds a manual override, a small voltage that clears the whole film at.",
    "label": "sun-tracking-window-film",
    "figures": {
      "zones": 9,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "glossary_terms": 50,
      "sections": 16,
      "states": 2
    }
  },
  {
    "title": "A 4D-Printed Folding Chair",
    "subject": "4d-printed folding chair design",
    "description": "This design-study imagines a chair printed flat from shape-memory polymer and hydrogel, which is a water-filled gel, that folds itself into a chair when wetted. The flat sheet ships in an envelope, and when the owner wets it, the hinges curl, the legs rise, and the seat locks into place, with no tools and no assembly. The design adds fold lines of different thicknesses, so the hinges fold in.",
    "label": "4d-printed-folding-chair",
    "figures": {
      "hinges": 8,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "glossary_terms": 50,
      "sections": 16,
      "parts": 1
    }
  }
];

const SOURCES = [
  {
    "name": "Wikipedia - Programmable matter",
    "url": "https://en.wikipedia.org/wiki/Programmable_matter",
    "establishes": "Programmable matter: matter whose properties can be changed by a signal, the goal of programmable materials research.",
    "retrieved": "2026-11-17",
    "resource_id": "en.wikipedia.org/wiki/Programmable_matter"
  },
  {
    "name": "Wikipedia - Smart material",
    "url": "https://en.wikipedia.org/wiki/Smart_material",
    "establishes": "Smart material: a material that changes its properties in response to a stimulus such as heat, light, or electricity.",
    "retrieved": "2026-11-17",
    "resource_id": "en.wikipedia.org/wiki/Smart_material"
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
