// Seeded boundless generator for the Meta-Generator
// (signature edition). Deterministic: the same seed always emits the same
// record. Usage: node gen-meta-generator-signature.js [seed]  (prints one
// JSON record) or: node gen-meta-generator-signature.js --test (runTests).
// Package-only; outputs are generated, not stored files.
"use strict";
const crypto = require("crypto");

const SLUG = "meta-generator-signature";
const RECORD_KIND = "meta generator record";
const ID_PREFIX = "JAH-MTGNS-";
const AI_NAME = "JAH Meta-Generator Librarian (Signature)";
const EDITION = "signature";
const CEILING = "Generator ceiling: up to 1,000,000,000 scales per file, generated on demand by the file AI \u2014 not stored files.";

const TOPICS = [
  {
    "title": "Signature Maker's Maker",
    "subject": "signature maker's maker",
    "description": "The Signature Maker's Maker is a design for a maker that makes makers: given the kind of generator needed, it writes the contract, the seeded generation, the gates, and the tests, runs the generator, checks its output, and files it. The design imagines a meta-generator as a maker of makers, where its output is not a record but a working generator.",
    "label": "signature-makers-maker",
    "figures": {
      "meta_parts": 4,
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
    "title": "Signature Kind Gate",
    "subject": "signature kind gate",
    "description": "The Signature Kind Gate is a design for a gate where generator kinds arrive: a name and a description are laid on the counter, the registry is searched for a generator that already covers the kind, and the gate either opens to building or points to what exists. The design imagines acceptance as a gate, where nothing is built twice.",
    "label": "signature-kind-gate",
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
    "title": "Signature Contract Loom",
    "subject": "signature contract loom",
    "description": "The Signature Contract Loom is a design for a loom that weaves generator contracts: interface, inputs, outputs, and validation are the threads, and the finished cloth is an agreement written in plain words. The design imagines a contract as woven cloth, where a generator without one cannot be used safely.",
    "label": "signature-contract-loom",
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
    "title": "Signature Seed Clock",
    "subject": "signature seed clock",
    "description": "The Signature Seed Clock is a design for a clock that always shows the same time for the same seed: the same starting number always produces the same output, so any output can be rebuilt exactly. The design imagines determinism as a clock, where the hands return to the same place for the same winding.",
    "label": "signature-seed-clock",
    "figures": {
      "seed_tests": 2,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "glossary_terms": 27,
      "sections": 14,
      "hard_stop": 1000000000,
      "throttle": 100
    }
  },
  {
    "title": "Signature Gate House",
    "subject": "signature gate house",
    "description": "The Signature Gate House is a design for a house where a generated generator's gates live: the record kind, the slug form, the identifier prefix, and the hard stop. The design imagines gates as a gate house, where a generator that fails its gates waits outside until it passes them.",
    "label": "signature-gate-house",
    "figures": {
      "gates": 4,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "glossary_terms": 27,
      "sections": 14,
      "hard_stop": 1000000000,
      "failures_allowed": 0
    }
  },
  {
    "title": "Signature Self Mirror",
    "subject": "signature self mirror",
    "description": "The Signature Self Mirror is a design for a mirror a generated generator holds up to itself: the same seed twice, different seeds differing, the emitted record kind matching, the slug in single signature form, the prefix right, and the hard stop at 1,000,000,000. The design imagines self-testing as a mirror, where a generator that cannot pass its own tests is not used.",
    "label": "signature-self-mirror",
    "figures": {
      "self_tests": 6,
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
    "title": "Signature First Run",
    "subject": "signature first run",
    "description": "The Signature First Run is a design for a first run that is watched: the meta-generator feeds a generated generator a seed, watches its output, checks the output against its gates and its tests, and records the results. The design imagines a first run as a maiden voyage, where a generator that fails is repaired and run again.",
    "label": "signature-first-run",
    "figures": {
      "first_run_parts": 4,
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
    "title": "Signature Second Scale",
    "subject": "signature second scale",
    "description": "The Signature Second Scale is a design for a scale that weighs a generated generator a second time: CHECK 2, the second validation pass, re-checks everything the first run checked, by execution, and the scale only balances when CHECK 2 passes with zero failures. The design imagines validation as a second weighing, where a generator marked verified because its files exist is a scale with.",
    "label": "signature-second-scale",
    "figures": {
      "validation_passes": 2,
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
    "name": "Wikipedia - Metaprogramming",
    "url": "https://en.wikipedia.org/wiki/Metaprogramming",
    "establishes": "Metaprogramming: how programs treat other programs as data.",
    "retrieved": "2026-11-17",
    "resource_id": "en.wikipedia.org/wiki/Metaprogramming"
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
