// Seeded boundless generator for the Universal Construction Generator
// (public edition). Deterministic: the same seed always emits the same
// record. Usage: node gen-universal-construction-generator.js [seed]  (prints one
// JSON record) or: node gen-universal-construction-generator.js --test (runTests).
// Package-only; outputs are generated, not stored files.
"use strict";
const crypto = require("crypto");

const SLUG = "universal-construction-generator";
const RECORD_KIND = "universal construction generator record";
const ID_PREFIX = "JAH-UCG-";
const AI_NAME = "JAH Universal Construction Generator Librarian";
const EDITION = "public";
const CEILING = "Generator ceiling: up to 1,000,000,000 scales per file, generated on demand by the file AI \u2014 not stored files.";

const TOPICS = [
  {
    "title": "What a Universal Construction Generator Is",
    "subject": "universal construction generator identity",
    "description": "A universal construction generator is a program that designs and builds new categories of systems: given a new construction category, it researches what is needed, finds relevant JAH resources, builds the required generator, produces a tested working result, and registers it for future use. It is universal because it is not tied to any one category, and it is the ultimate priority of the.",
    "label": "universal-construction-generator-identity",
    "figures": {
      "constructor_parts": 4,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "glossary_terms": 27,
      "sections": 14,
      "hard_stop": 1000000000,
      "live_records": 300
    }
  },
  {
    "title": "Accepting a New Category",
    "subject": "accepting a new category",
    "description": "Accepting a new category is the first step of the constructor: the category arrives as a name and a short description, the constructor checks that the name is plain and the description is real, and then it searches the live manifest, which is the master list of all databases, for anything that already covers it. A category that already exists is linked, never rebuilt, and a category that is.",
    "label": "accepting-new-category",
    "figures": {
      "acceptance_steps": 4,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "glossary_terms": 27,
      "sections": 14,
      "manifest_entries": 63047,
      "hard_stop": 1000000000
    }
  },
  {
    "title": "Defining the Category",
    "subject": "defining the category",
    "description": "Defining the category is the writing of what the new category is: its name, its purpose, its parts, its boundaries, and what it is not. A category defined in plain words can be built, and a category defined in jargon cannot, because the builders cannot tell where it starts or ends. This record specifies the definition rules: name, purpose, parts, boundaries, and non-goals, all in plain words,.",
    "label": "defining-category",
    "figures": {
      "definition_parts": 5,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "glossary_terms": 27,
      "sections": 14,
      "hard_stop": 1000000000,
      "catalog_items": 100
    }
  },
  {
    "title": "Searching the Network",
    "subject": "searching the network",
    "description": "Searching the network is the constructor's discovery step: it searches the JAH Network for existing databases, files, generators, specifications, websites, demonstrations, and working implementations that touch the new category, and it retrieves the actual contents of what it finds. Search follows the discover-before-building rule, and it follows the pull-links-and-full-data rule: the complete.",
    "label": "searching-network",
    "figures": {
      "search_steps": 7,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "glossary_terms": 27,
      "sections": 14,
      "hard_stop": 1000000000,
      "manifest_entries": 63047
    }
  },
  {
    "title": "Reading Relevant Specifications",
    "subject": "reading relevant specifications",
    "description": "Reading relevant specifications is the study of what the search found: the constructor reads the specifications and associated resources, identifies existing capabilities and limitations, and records the source web address and resource identifiers. Reading is not skimming: a specification that is skimmed is a specification misunderstood, and a misunderstood specification is built wrong. This.",
    "label": "reading-relevant-specifications",
    "figures": {
      "reading_parts": 4,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "glossary_terms": 27,
      "sections": 14,
      "hard_stop": 1000000000,
      "checks": 6
    }
  },
  {
    "title": "Identifying Missing Components",
    "subject": "identifying missing components",
    "description": "Identifying missing components is the listing of what the new category needs that does not yet exist: the database, the generator, the website, the tests, or the documentation that must be built. The list is honest: it names what is missing, it does not hide gaps, and it never fills a gap with a guess. This record specifies the missing-component rules: list every gap, give each gap a reason,.",
    "label": "identifying-missing-components",
    "figures": {
      "gap_fields": 3,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "glossary_terms": 27,
      "sections": 14,
      "hard_stop": 1000000000,
      "checks": 6
    }
  },
  {
    "title": "Designing the New System",
    "subject": "designing the new system",
    "description": "Designing the new system is the writing of its complete specification: system identity, database structure, search and retrieval, working source code, reusable generator, website interface, documentation, demonstration, automated tests, validation results, version history, source provenance, and expansion instructions. The specification is long because it is complete, never padded, and a short.",
    "label": "designing-new-system",
    "figures": {
      "spec_sections": 14,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "glossary_terms": 27,
      "hard_stop": 1000000000,
      "throttle": 100,
      "catalog_items": 100
    }
  },
  {
    "title": "Building the Required Generator",
    "subject": "building the required generator",
    "description": "Building the required generator is the making of the generator the new category needs: its contract, its seeded generation, its gates, and its tests, written by the constructor, run once, checked, and filed. The generator is the tool that will build the category's records, so it must be right before it is used. This record specifies the generator-building rules: contract first, seeding second,.",
    "label": "building-required-generator",
    "figures": {
      "generator_parts": 4,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "glossary_terms": 27,
      "sections": 14,
      "gates": 4,
      "hard_stop": 1000000000
    }
  }
];

const SOURCES = [
  {
    "name": "Wikipedia - Systems engineering",
    "url": "https://en.wikipedia.org/wiki/Systems_engineering",
    "establishes": "Systems engineering: how large systems are specified, built, and checked.",
    "retrieved": "2026-11-17",
    "resource_id": "en.wikipedia.org/wiki/Systems_engineering"
  },
  {
    "name": "Wikipedia - Code generation",
    "url": "https://en.wikipedia.org/wiki/Code_generation",
    "establishes": "Code generation: how programs create other programs from specifications.",
    "retrieved": "2026-11-17",
    "resource_id": "en.wikipedia.org/wiki/Code_generation"
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
