// Seeded boundless generator for the Generator Database
// (signature edition). Deterministic: the same seed always emits the same
// record. Usage: node gen-generator-database-signature.js [seed]  (prints one
// JSON record) or: node gen-generator-database-signature.js --test (runTests).
// Package-only; outputs are generated, not stored files.
"use strict";
const crypto = require("crypto");

const SLUG = "generator-database-signature";
const RECORD_KIND = "generator database record";
const ID_PREFIX = "JAH-GNDBS-";
const AI_NAME = "JAH Generator Database Librarian (Signature)";
const EDITION = "signature";
const CEILING = "Generator ceiling: up to 1,000,000,000 scales per file, generated on demand by the file AI \u2014 not stored files.";

const TOPICS = [
  {
    "title": "Signature Registry Hall",
    "subject": "signature registry hall",
    "description": "The Signature Registry Hall is a design for a hall where every generator is filed: a shelf for each kind, a card for each generator, and the contract written on the card in plain words. The design imagines the registry as a hall, where the Master AI (artificial intelligence) can walk in and find the right generator for a job.",
    "label": "signature-registry-hall",
    "figures": {
      "registry_fields": 5,
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
    "title": "Signature Contract Scroll",
    "subject": "signature contract scroll",
    "description": "The Signature Contract Scroll is a design for a scroll that holds a generator's agreement: its interface, its inputs, its outputs, and its execution and validation procedure, all written in plain words and sealed with the date. The design imagines a contract as a scroll, where a generator without one cannot be used safely.",
    "label": "signature-contract-scroll",
    "figures": {
      "contract_parts": 4,
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
    "title": "Signature Kind Garden",
    "subject": "signature kind garden",
    "description": "The Signature Kind Garden is a design for a garden where generator kinds grow: twenty beds, one per kind, each generator planted in exactly one bed, and new kinds defined before they are planted. The design imagines kinds as garden beds, where a generator planted in two beds at once is a weed.",
    "label": "signature-kind-garden",
    "figures": {
      "kinds": 20,
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
    "title": "Signature Version Ladder",
    "subject": "signature version ladder",
    "description": "The Signature Version Ladder is a design for a ladder where generator versions climb: each rung is one dated state, with what changed and why written on it, and the old rungs kept below so work built with an old version can still be rebuilt. The design imagines versions as rungs, where a generator that changes silently has no ladder at all.",
    "label": "signature-version-ladder",
    "figures": {
      "version_fields": 3,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "glossary_terms": 27,
      "sections": 14,
      "hard_stop": 1000000000,
      "versions": 2
    }
  },
  {
    "title": "Signature Finding Hound",
    "subject": "signature finding hound",
    "description": "The Signature Finding Hound is a design for a hound that finds the right generator for a job: it sniffs the registry by kind, by output, by version, and by full text, and it returns the matching generators with their contracts in its mouth. The design imagines discovery as a hound, where searching first is the rule and building what exists is the mistake.",
    "label": "signature-finding-hound",
    "figures": {
      "search_modes": 4,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "glossary_terms": 27,
      "sections": 14,
      "hard_stop": 1000000000,
      "kinds": 20
    }
  },
  {
    "title": "Signature Trial Ground",
    "subject": "signature trial ground",
    "description": "The Signature Trial Ground is a design for a ground where generators are tried: the same seed twice, different seeds differing, the record kind matching, the slug in single signature form, the prefix right, and the hard stop at 1,000,000,000. The design imagines testing as a trial ground, where a generator that fails is not filed until it passes.",
    "label": "signature-trial-ground",
    "figures": {
      "tests_per_generator": 6,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "glossary_terms": 27,
      "sections": 14,
      "gates": 4,
      "hard_stop": 1000000000
    }
  },
  {
    "title": "Signature Result Ledger",
    "subject": "signature result ledger",
    "description": "The Signature Result Ledger is a design for a ledger that records what generators actually did: what they made, how many outputs, how long it took, which tests passed, and what failed. The design imagines results as bookkeeping, where a generator whose results are never recorded is a storyteller.",
    "label": "signature-result-ledger",
    "figures": {
      "result_fields": 4,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "glossary_terms": 27,
      "sections": 14,
      "checks": 6,
      "hard_stop": 1000000000
    }
  },
  {
    "title": "Signature Rating Balance",
    "subject": "signature rating balance",
    "description": "The Signature Rating Balance is a design for a balance that weighs generators: correctness, completeness, speed, determinism, and ease of use, each on its own pan, with every weight recorded and its reason written on the tag. The design imagines ratings as weighing, where a bare number without its weights is a cheat.",
    "label": "signature-rating-balance",
    "figures": {
      "rating_parts": 5,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "glossary_terms": 27,
      "sections": 14,
      "checks": 6,
      "hard_stop": 1000000000
    }
  }
];

const SOURCES = [
  {
    "name": "Wikipedia - Code generation",
    "url": "https://en.wikipedia.org/wiki/Code_generation",
    "establishes": "Code generation: how programs create other programs from specifications.",
    "retrieved": "2026-11-17",
    "resource_id": "en.wikipedia.org/wiki/Code_generation"
  },
  {
    "name": "Wikipedia - Database",
    "url": "https://en.wikipedia.org/wiki/Database",
    "establishes": "Database: how organized collections of records are stored and searched.",
    "retrieved": "2026-11-17",
    "resource_id": "en.wikipedia.org/wiki/Database"
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
