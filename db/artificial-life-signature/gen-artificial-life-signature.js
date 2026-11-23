// Seeded boundless generator for the Artificial Life Database
// (signature edition). Deterministic: the same seed always emits the same
// record. Usage: node gen-artificial-life-signature.js [seed]  (prints one
// JSON record) or: node gen-artificial-life-signature.js --test (runTests).
// Package-only; outputs are generated, not stored files.
"use strict";
const crypto = require("crypto");

const SLUG = "artificial-life-signature";
const RECORD_KIND = "future artificial life record";
const ID_PREFIX = "JAH-ALIFES-";
const AI_NAME = "JAH Artificial Life Librarian (Signature)";
const EDITION = "signature";
const CEILING = "Generator ceiling: up to 1,000,000,000 scales per file, generated on demand by the file AI \u2014 not stored files.";

const TOPICS = [
  {
    "title": "A Digital Tide-Pool Organism",
    "subject": "digital tide-pool organism design",
    "description": "This design-study imagines a digital organism that lives in a simulated tide pool, a shallow world that fills and drains on a regular cycle. The organism is a string of instructions that copies itself when the pool is full and rests when the pool drains, so its life follows the rhythm of its world. When the pool drains, organisms that stored extra copies survive, and organisms that spent.",
    "label": "digital-tide-pool-organism",
    "figures": {
      "species": 2,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "glossary_terms": 50,
      "sections": 16,
      "cycle_hours": 6
    }
  },
  {
    "title": "A Self-Replicating Garden Program",
    "subject": "self-replicating garden design",
    "description": "This design-study imagines a garden program in which self-replicating code grows like plants in beds, tended by a gardener program that waters the strong and weeds the broken. Each plant is a program that copies itself into neighbouring soil, which is free memory, and mutations change its colour, which marks its family, and its growth rate. The gardener does not design the plants: it only.",
    "label": "self-replicating-garden",
    "figures": {
      "beds": 8,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "glossary_terms": 50,
      "sections": 16,
      "families": 5
    }
  },
  {
    "title": "A Tierra-Style Evolution Chamber",
    "subject": "tierra-style evolution chamber design",
    "description": "This design-study imagines a modern Tierra-style evolution chamber with a glass wall: the memory world is shown live, parasites glow one colour and hosts another, and the audience watches ecological roles appear. The chamber keeps Tierra's rules, programs competing for computer time and memory, copying with mutation, and adds full ancestry recording so any organism's whole line can be.",
    "label": "tierra-style-chamber",
    "figures": {
      "climates": 4,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "glossary_terms": 50,
      "sections": 16,
      "generations": 5000
    }
  },
  {
    "title": "An Avida-Style Fitness Landscape",
    "subject": "avida-style fitness landscape design",
    "description": "This design-study imagines an Avida-style fitness landscape as a walkable terrain, where height means success and digital organisms climb it by evolving new logic tasks. Each hill is a task, each valley is a failed strategy, and the population spreads across the terrain as it learns. The design adds bridges: when two populations meet on a ridge, they can exchange code, which models how real.",
    "label": "avida-style-landscape",
    "figures": {
      "hills": 9,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "glossary_terms": 50,
      "sections": 16,
      "bridges": 3
    }
  },
  {
    "title": "A Game-of-Life City Simulator",
    "subject": "game-of-life city design",
    "description": "This design-study imagines a city simulator built on the Game of Life, where each cell is a city block and the three rules decide whether blocks live, die, or are born. Live blocks with two or three live neighbours stay alive, overcrowded blocks die, and empty blocks with exactly three live neighbours are built. Gliders become delivery routes crawling across the city, and glider guns become.",
    "label": "game-of-life-city",
    "figures": {
      "districts": 6,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "glossary_terms": 50,
      "sections": 16,
      "rules": 3
    }
  },
  {
    "title": "A Cellular Automaton Weather World",
    "subject": "cellular automaton weather design",
    "description": "This design-study imagines a weather world built as a cellular automaton, where each cell holds temperature, moisture, and wind, and local rules move heat and water across the grid. Warm cells rise, moist cells gather into clouds, and clouds release rain when they grow heavy, so storms form, travel, and fade without any central weather controller. The design adds seasons: the sun's angle.",
    "label": "cellular-automaton-weather",
    "figures": {
      "cell_values": 3,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "glossary_terms": 50,
      "sections": 16,
      "seasons": 4
    }
  },
  {
    "title": "A Self-Repairing Code Colony",
    "subject": "self-repairing code colony design",
    "description": "This design-study imagines a colony of self-replicating programs that also repair each other: when one program is damaged by a copying error, a neighbour donates a clean copy of the damaged part. The colony keeps a library of spare parts, which are clean copies of each instruction block, and repair crews, which are small programs that patrol the memory looking for damage. The design tests how.",
    "label": "self-repairing-code-colony",
    "figures": {
      "repair_crews": 6,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "glossary_terms": 50,
      "sections": 16,
      "spare_parts": 32
    }
  },
  {
    "title": "An Artificial Chemistry Kitchen",
    "subject": "artificial chemistry kitchen design",
    "description": "This design-study imagines an artificial chemistry kitchen, a visual laboratory where molecules are ingredients, reactions are recipes, and the cook is a program that stirs the pot at random. Visitors add ingredients, watch cycles form that keep themselves going, and save any cycle that lasts a thousand steps as a recipe card. The kitchen keeps a cookbook of every cycle ever found, with the.",
    "label": "artificial-chemistry-kitchen",
    "figures": {
      "ingredients": 20,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "glossary_terms": 50,
      "sections": 16,
      "recipe_cards": 50
    }
  }
];

const SOURCES = [
  {
    "name": "Wikipedia - Artificial life",
    "url": "https://en.wikipedia.org/wiki/Artificial_life",
    "establishes": "Artificial life: the study of life-like behaviour in systems built by people, in software, in hardware, or in laboratory chemistry.",
    "retrieved": "2026-11-17",
    "resource_id": "en.wikipedia.org/wiki/Artificial_life"
  },
  {
    "name": "Wikipedia - Digital organism",
    "url": "https://en.wikipedia.org/wiki/Digital_organism",
    "establishes": "Digital organism: a self-replicating program that lives, competes, and evolves inside a computer.",
    "retrieved": "2026-11-17",
    "resource_id": "en.wikipedia.org/wiki/Digital_organism"
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
