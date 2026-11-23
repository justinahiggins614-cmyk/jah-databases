// Seeded boundless generator for the Database Explorer
// (signature edition). Deterministic: the same seed always emits the same
// record. Usage: node gen-database-explorer-signature.js [seed]  (prints one
// JSON record) or: node gen-database-explorer-signature.js --test (runTests).
// Package-only; outputs are generated, not stored files.
"use strict";
const crypto = require("crypto");

const SLUG = "database-explorer-signature";
const RECORD_KIND = "database explorer record";
const ID_PREFIX = "JAH-DBEXS-";
const AI_NAME = "JAH Database Explorer Librarian (Signature)";
const EDITION = "signature";
const CEILING = "Generator ceiling: up to 1,000,000,000 scales per file, generated on demand by the file AI \u2014 not stored files.";

const TOPICS = [
  {
    "title": "Signature Explorer Compass",
    "subject": "signature explorer compass",
    "description": "The Signature Explorer Compass is a design for a compass that points through databases: the needle swings to the database the reader needs, the dial shows the record count, and the case holds the way back. The design imagines browsing as navigation, where the reader always knows where they are and where the needle points.",
    "label": "signature-explorer-compass",
    "figures": {
      "databases": 63047,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "glossary_terms": 27,
      "sections": 14,
      "browse_modes": 4,
      "search_modes": 4
    }
  },
  {
    "title": "Signature Letter Staircase",
    "subject": "signature letter staircase",
    "description": "The Signature Letter Staircase is a design for a staircase with twenty-six steps, one for each letter, where each step opens to the records that start with that letter, and only the step the reader stands on is open. The design imagines A to Z browsing as climbing, one letter at a time.",
    "label": "signature-letter-staircase",
    "figures": {
      "letters": 26,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "glossary_terms": 27,
      "sections": 14,
      "browse_modes": 4
    }
  },
  {
    "title": "Signature Subject Map",
    "subject": "signature subject map",
    "description": "The Signature Subject Map is a design for a map of subjects: each subject is a region, its size shows its record count, and shared records are bridges between regions. The design imagines subject browsing as travel, where the reader can see the whole country before choosing a road.",
    "label": "signature-subject-map",
    "figures": {
      "subjects": 40,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "glossary_terms": 27,
      "sections": 14,
      "browse_modes": 4
    }
  },
  {
    "title": "Signature Search Lantern",
    "subject": "signature search lantern",
    "description": "The Signature Search Lantern is a design for a lantern that lights up matching words: the reader types words, the lantern shines on the records that hold them, and the matching words glow in context so the reader can see why each record matched. The design imagines search as light, where the best matches shine brightest.",
    "label": "signature-search-lantern",
    "figures": {
      "indexed_fields": 11,
      "search_modes": 4,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "glossary_terms": 27,
      "sections": 14
    }
  },
  {
    "title": "Signature Filter Sieve",
    "subject": "signature filter sieve",
    "description": "The Signature Filter Sieve is a design for a sieve that narrows results: records pour in at the top, the mesh holds back what does not match, and the count of what passed and what was held back is written on the rim. The design imagines filtering as sifting, where the sieve never hides how much it held back.",
    "label": "signature-filter-sieve",
    "figures": {
      "facets": 4,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "glossary_terms": 27,
      "sections": 14,
      "search_modes": 4
    }
  },
  {
    "title": "Signature Record Window",
    "subject": "signature record window",
    "description": "The Signature Record Window is a design for a window that opens onto one record in full: the glass is the page, the frame is the fixed section order, and the sill holds the sources with their addresses and dates. The design imagines the full record view as a window, where one click opens it and the whole record can be seen through it.",
    "label": "signature-record-window",
    "figures": {
      "sections": 14,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "glossary_terms": 27,
      "fields": 24,
      "browse_modes": 4
    }
  },
  {
    "title": "Signature Card Table",
    "subject": "signature card table",
    "description": "The Signature Card Table is a design for a table where browse cards are laid out: each card holds an image, a title, and a description, and one tap on a card opens the full record it stands for. The design imagines browsing as a card game, where every card is honest about the record it holds.",
    "label": "signature-card-table",
    "figures": {
      "card_parts": 3,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "glossary_terms": 27,
      "sections": 14,
      "browse_modes": 4
    }
  },
  {
    "title": "Signature Question Bell",
    "subject": "signature question bell",
    "description": "The Signature Question Bell is a design for a bell a reader rings with a question: the ring carries the question to the database AI (artificial intelligence), which answers in natural sentences from the database's own records and names the records it used. The design imagines asking as ringing a bell, where the answer always arrives with its sources.",
    "label": "signature-question-bell",
    "figures": {
      "answer_parts": 3,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "glossary_terms": 27,
      "sections": 14,
      "search_modes": 4
    }
  }
];

const SOURCES = [
  {
    "name": "Wikipedia - Database",
    "url": "https://en.wikipedia.org/wiki/Database",
    "establishes": "Database: how organized collections of records are stored and searched.",
    "retrieved": "2026-11-17",
    "resource_id": "en.wikipedia.org/wiki/Database"
  },
  {
    "name": "Wikipedia - Information retrieval",
    "url": "https://en.wikipedia.org/wiki/Information_retrieval",
    "establishes": "Information retrieval: how the right records are found among many.",
    "retrieved": "2026-11-17",
    "resource_id": "en.wikipedia.org/wiki/Information_retrieval"
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
