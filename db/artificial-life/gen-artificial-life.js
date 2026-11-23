// Seeded boundless generator for the Artificial Life Database
// (public edition). Deterministic: the same seed always emits the same
// record. Usage: node gen-artificial-life.js [seed]  (prints one
// JSON record) or: node gen-artificial-life.js --test (runTests).
// Package-only; outputs are generated, not stored files.
"use strict";
const crypto = require("crypto");

const SLUG = "artificial-life";
const RECORD_KIND = "future artificial life record";
const ID_PREFIX = "JAH-ALIFE-";
const AI_NAME = "JAH Artificial Life Librarian";
const EDITION = "public";
const CEILING = "Generator ceiling: up to 1,000,000,000 scales per file, generated on demand by the file AI \u2014 not stored files.";

const TOPICS = [
  {
    "title": "What Artificial Life Is",
    "subject": "artificial life identity",
    "description": "Artificial life is the study of life-like behaviour in systems built by people, in software, in hardware, or in laboratory chemistry, rather than life that evolved in nature. A life-like system is one that shows some of the patterns of living things: it keeps itself going, it makes copies of itself, it changes over time, and it adapts to its surroundings. Artificial life research asks which of.",
    "label": "what-artificial-life-is",
    "figures": {
      "branches": 3,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "glossary_terms": 50,
      "sections": 16,
      "research_parts": 10
    }
  },
  {
    "title": "Digital Organisms",
    "subject": "digital organisms",
    "description": "A digital organism is a self-replicating program that lives, competes, and evolves inside a computer, like a living thing in a digital world. The organism is a string of instructions that copies itself into computer memory, and copies sometimes carry small changes, which are called mutations, meaning small random changes in the instructions. Organisms compete for the two resources of their.",
    "label": "digital-organisms",
    "figures": {
      "resources": 2,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "glossary_terms": 50,
      "sections": 16,
      "generations": 1000
    }
  },
  {
    "title": "Tierra and Early Digital Evolution",
    "subject": "tierra digital evolution",
    "description": "Tierra is the early digital evolution system in which programs competed for computer time and memory, built by Thomas Ray and first described in the early 1990s. In Tierra, small programs lived in a shared block of memory, copied themselves, and sometimes made copying mistakes that created new variants. Shorter programs that copied faster spread, and over time the population produced.",
    "label": "tierra-digital-evolution",
    "figures": {
      "instruction_count": 32,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "glossary_terms": 50,
      "sections": 16,
      "decade": 1990
    }
  },
  {
    "title": "Avida and Digital Evolution Research",
    "subject": "avida digital evolution",
    "description": "Avida is the digital evolution research platform in which programs evolve to perform logic tasks, developed from Tierra's ideas by researchers at Michigan State University and the California Institute of Technology. In Avida, digital organisms live in separate cells, copy themselves with mutations, and can earn extra computer time by performing logic operations such as AND, OR, and NOT, which.",
    "label": "avida-digital-evolution",
    "figures": {
      "logic_tasks": 9,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "glossary_terms": 50,
      "sections": 16,
      "generations": 10000
    }
  },
  {
    "title": "Conway's Game of Life",
    "subject": "game of life",
    "description": "Conway's Game of Life is the cellular automaton in which simple rules produce complex patterns, invented by the mathematician John Horton Conway in 1970. The game runs on a grid of cells, each cell either alive or dead, and each step applies three rules: a live cell with two or three live neighbours stays alive, a live cell with any other number of neighbours dies, and a dead cell with exactly.",
    "label": "game-of-life",
    "figures": {
      "rules": 3,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "glossary_terms": 50,
      "sections": 16,
      "year": 1970
    }
  },
  {
    "title": "Cellular Automata",
    "subject": "cellular automata",
    "description": "A cellular automaton is a grid of cells that change by simple local rules, step by step, and can produce complex patterns from those rules. Each cell holds a state, such as alive or dead, or a colour, and at each step every cell looks at its neighbours and updates its own state by a fixed rule. The rules are local, meaning each cell only sees its neighbours, and uniform, meaning the same rule.",
    "label": "cellular-automata",
    "figures": {
      "behaviour_kinds": 4,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "glossary_terms": 50,
      "sections": 16,
      "dimensions": 2
    }
  },
  {
    "title": "Self-Replication in Software",
    "subject": "self-replication in software",
    "description": "Self-replication in software is the ability of a program to make a copy of itself, and it is the foundation of digital artificial life, because without copying there is no population and no evolution. A self-replicating program reads its own instructions, writes them into a new place in memory, and starts the copy running, so one program becomes two, and two become four. Copying is never.",
    "label": "self-replication-software",
    "figures": {
      "copies_per_generation": 2,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "glossary_terms": 50,
      "sections": 16,
      "minimum_parts": 4
    }
  },
  {
    "title": "Artificial Chemistries",
    "subject": "artificial chemistries",
    "description": "An artificial chemistry is a simulated chemistry in which molecules react by rules and new forms appear, built to study how chemistry can organize itself without a living cell to guide it. In an artificial chemistry, the molecules are strings of symbols, the reactions are rules that rewrite those strings, and the container is a shared space where molecules meet at random. From those parts come.",
    "label": "artificial-chemistries",
    "figures": {
      "reaction_rules": 12,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "glossary_terms": 50,
      "sections": 16,
      "molecule_kinds": 20
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
