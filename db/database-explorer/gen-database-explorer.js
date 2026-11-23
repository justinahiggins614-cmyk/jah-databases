// Seeded boundless generator for the Database Explorer
// (public edition). Deterministic: the same seed always emits the same
// record. Usage: node gen-database-explorer.js [seed]  (prints one
// JSON record) or: node gen-database-explorer.js --test (runTests).
// Package-only; outputs are generated, not stored files.
"use strict";
const crypto = require("crypto");

const SLUG = "database-explorer";
const RECORD_KIND = "database explorer record";
const ID_PREFIX = "JAH-DBEX-";
const AI_NAME = "JAH Database Explorer Librarian";
const EDITION = "public";
const CEILING = "Generator ceiling: up to 1,000,000,000 scales per file, generated on demand by the file AI \u2014 not stored files.";

const TOPICS = [
  {
    "title": "What a Database Explorer Is",
    "subject": "database explorer identity",
    "description": "A database explorer is a website for browsing and searching databases: it shows what databases exist, lets a reader open one, search inside it, filter its records, and open any record in full. It is the front door of a database, and a database without an explorer is a store with no door: the records are inside, but a reader cannot reach them. This record specifies the explorer for the whole.",
    "label": "database-explorer-identity",
    "figures": {
      "browse_modes": 4,
      "search_modes": 4,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "glossary_terms": 27,
      "sections": 14
    }
  },
  {
    "title": "Browsing by Letter",
    "subject": "browsing by letter",
    "description": "Browsing by letter is the A to Z way through a database: the records are grouped under their first letters, each letter's group starts closed, and only the opened letter's records are shown, so a list of a million records never floods the page. Collapsible means a group can be opened and closed, and lazy loading means records are built only when their letter is opened. This record specifies.",
    "label": "browsing-by-letter",
    "figures": {
      "letters": 26,
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
    "title": "Browsing by Subject",
    "subject": "browsing by subject",
    "description": "Browsing by subject is the way through a database by what records are about: subjects are listed with their record counts, each subject opens to its records, and records that belong to more than one subject appear under each with a note that they are shared. Subject browsing serves the reader who knows what they want to learn but not what it is called. This record specifies the.",
    "label": "browsing-by-subject",
    "figures": {
      "subjects": 40,
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
    "title": "Full-Text Search",
    "subject": "full-text search",
    "description": "Full-text search is search over every word in every record: the reader types words, the explorer looks them up in its index, and the matching records are returned with the matching words shown in context. The index is the word list that maps each word to its records, built once and updated when records change. This record specifies the search rules: every prose field indexed, results ranked.",
    "label": "full-text-search",
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
    "title": "Filters and Facets",
    "subject": "filters and facets",
    "description": "A filter is a narrowing rule, such as only records from one subject or one year, and a facet is one named way of narrowing, such as subject, kind, or date. Filters let a reader cut a thousand matches down to the ten that matter, but a filter that hides its effect misleads: the explorer must always show how many records matched before and after filtering. This record specifies the filter rules:.",
    "label": "filters-facets",
    "figures": {
      "facets": 4,
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
    "title": "The Full Record View",
    "subject": "full record view",
    "description": "The full record view is the page that shows one record completely: every field, every figure, the demo, the program, the sources with their web addresses and retrieval dates, the network links, and the generator block. One click from a browse card or a search result must reach it, and it must never show a summary in place of the record. This record specifies the full-view rules: all fields.",
    "label": "full-record-view",
    "figures": {
      "sections": 14,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "glossary_terms": 27,
      "fields": 24,
      "browse_modes": 4,
      "search_modes": 4
    }
  },
  {
    "title": "Browse Cards",
    "subject": "browse cards",
    "description": "A browse card is the small preview that stands for a record in a list: an image where one exists, the title, and a short description, with one click opening the full record. Cards must be honest previews: the title is the record's real title, the description is the record's real description, and a card never promises content the record does not hold. This record specifies the card rules: image.",
    "label": "browse-cards",
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
    "title": "The Ask the AI Box",
    "subject": "ask the ai box",
    "description": "The Ask the AI box is the question box on the explorer: a reader types a question in plain words, and the database AI (artificial intelligence) answers from the database's own records, naming the records it used. The AI must answer conversationally, in natural sentences, and must say plainly when the database does not hold the answer, instead of inventing one. This record specifies the Ask box.",
    "label": "ask-the-ai-box",
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
