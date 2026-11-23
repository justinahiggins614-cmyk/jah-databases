// Seeded boundless generator for the Universal Construction Generator
// (signature edition). Deterministic: the same seed always emits the same
// record. Usage: node gen-universal-construction-generator-signature.js [seed]  (prints one
// JSON record) or: node gen-universal-construction-generator-signature.js --test (runTests).
// Package-only; outputs are generated, not stored files.
"use strict";
const crypto = require("crypto");

const SLUG = "universal-construction-generator-signature";
const RECORD_KIND = "universal construction generator record";
const ID_PREFIX = "JAH-UCGS-";
const AI_NAME = "JAH Universal Construction Generator Librarian (Signature)";
const EDITION = "signature";
const CEILING = "Generator ceiling: up to 1,000,000,000 scales per file, generated on demand by the file AI \u2014 not stored files.";

const TOPICS = [
  {
    "title": "Signature Category Gate",
    "subject": "signature category gate",
    "description": "The Signature Category Gate is a design for a gate where new categories arrive: a name and a description are laid on the counter, the manifest is searched for existing coverage, and the gate either opens to building or points to the database that already covers it. The design imagines acceptance as a gate, where nothing is built twice.",
    "label": "signature-category-gate",
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
    "title": "Signature Definition Loom",
    "subject": "signature definition loom",
    "description": "The Signature Definition Loom is a design for a loom that weaves a category's definition: name, purpose, parts, boundaries, and non-goals are the threads, and the finished cloth is a definition in plain words. The design imagines definition as weaving, where a category defined in jargon cannot be built.",
    "label": "signature-definition-loom",
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
    "title": "Signature Search Net",
    "subject": "signature search net",
    "description": "The Signature Search Net is a design for a net that catches real resources: it is cast over the network, it pulls in actual links and full data, and every catch is tagged with its web address, its identifier, and its retrieval date. The design imagines discovery as fishing with a net, where a summary is not a catch and a bare name slips through the mesh.",
    "label": "signature-search-net",
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
    "title": "Signature Reading Room",
    "subject": "signature reading room",
    "description": "The Signature Reading Room is a design for a room where specifications are read in full: capabilities noted on one wall, limitations noted on the other, and the source of each written beside it. The design imagines reading as a room, where a specification that is skimmed is a specification misunderstood.",
    "label": "signature-reading-room",
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
    "title": "Signature Gap List",
    "subject": "signature gap list",
    "description": "The Signature Gap List is a design for a list that names what is missing: the database, the generator, the website, the tests, or the documentation that must be built, each with its reason, and no gap ever filled with a guess. The design imagines missing components as a list nailed to the wall, where a builder who cannot name what is missing builds the wrong things.",
    "label": "signature-gap-list",
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
    "title": "Signature Design Loom",
    "subject": "signature design loom",
    "description": "The Signature Design Loom is a design for a loom that weaves a new system's specification: identity, structure, retrieval, code, generator, interface, documentation, demo, tests, validation, history, provenance, and expansion are the threads, and the finished cloth is a specification long because it is complete. The design imagines design as weaving, where a missing thread leaves a hole.",
    "label": "signature-design-loom",
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
    "title": "Signature Generator Forge",
    "subject": "signature generator forge",
    "description": "The Signature Generator Forge is a design for a forge where the required generator is hammered out: contract first, seeding second, gates third, tests fourth, and no use until the generator passes its own tests. The design imagines generator-building as forging, where a generator used before it is tested builds faults at scale.",
    "label": "signature-generator-forge",
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
  },
  {
    "title": "Signature Working Bench",
    "subject": "signature working bench",
    "description": "The Signature Working Bench is a design for a bench where the tested working result is built: the generator runs, the artifact is created, its tests are run, and the result is checked by execution. The design imagines production as bench work, where a result that was never executed is a claim and a result whose tests were never run is a hope.",
    "label": "signature-working-bench",
    "figures": {
      "production_steps": 4,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "glossary_terms": 27,
      "sections": 14,
      "checks": 6,
      "failures_allowed": 0
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
