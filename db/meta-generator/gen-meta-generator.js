// Seeded boundless generator for the Meta-Generator
// (public edition). Deterministic: the same seed always emits the same
// record. Usage: node gen-meta-generator.js [seed]  (prints one
// JSON record) or: node gen-meta-generator.js --test (runTests).
// Package-only; outputs are generated, not stored files.
"use strict";
const crypto = require("crypto");

const SLUG = "meta-generator";
const RECORD_KIND = "meta generator record";
const ID_PREFIX = "JAH-MTGN-";
const AI_NAME = "JAH Meta-Generator Librarian";
const EDITION = "public";
const CEILING = "Generator ceiling: up to 1,000,000,000 scales per file, generated on demand by the file AI \u2014 not stored files.";

const TOPICS = [
  {
    "title": "What a Meta-Generator Is",
    "subject": "meta-generator identity",
    "description": "A meta-generator is a program that creates other reusable generators: given the kind of generator needed, it writes the generator's contract, its seeded generation, its gates, and its tests, runs the generator, checks its output, and files it in the generator database. A meta-generator is a maker of makers, and its output is not a record but a working generator that can itself make records..",
    "label": "meta-generator-identity",
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
    "title": "Accepting a Generator Kind",
    "subject": "accepting a generator kind",
    "description": "Accepting a generator kind is the first step of the meta-generator: the kind arrives as a name and a short description, the generator checks that the kind is real and that the registry does not already hold a generator for it, and only then is the kind accepted for building. A kind that already has a working generator is linked, never rebuilt. This record specifies the acceptance rules: real.",
    "label": "accepting-generator-kind",
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
    "title": "Designing a Generator Contract",
    "subject": "designing a generator contract",
    "description": "Designing a generator contract is the writing of the agreement a generated generator makes with its users: its interface, which is the way it is called; its input specification, which says what it needs; its output format, which says what it returns; and its execution and validation procedure, which says how it runs and how it is checked. A generator without a contract cannot be used safely..",
    "label": "designing-generator-contract",
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
    "title": "Writing Seeded Generation",
    "subject": "writing seeded generation",
    "description": "Writing seeded generation is the making of the generation itself: the generated generator takes a seed, which is a starting number, and produces the same output for the same seed every time, so any output can be rebuilt exactly. Determinism is what makes generated output checkable. This record specifies the seeding rules: one seed per generation, the same seed twice giving identical output,.",
    "label": "writing-seeded-generation",
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
    "title": "Writing Generator Gates",
    "subject": "writing generator gates",
    "description": "Writing generator gates is the making of the checks a generated generator must pass: the emitted record kind must match the manifest record kind, the slug must use the single signature form, the identifier must use the database's own prefix, and the hard stop must be 1,000,000,000. Gates are written into the generated generator, so it checks itself on every run. This record specifies the gate.",
    "label": "writing-generator-gates",
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
    "title": "Writing Generator Tests",
    "subject": "writing generator tests",
    "description": "Writing generator tests is the making of the test suite for a generated generator: the same seed twice gives identical output, different seeds give different outputs, the emitted record kind matches, the slug form is single, the prefix is the database's own, and the hard stop is 1,000,000,000. Tests are written into the generated generator, so it tests itself. This record specifies the test.",
    "label": "writing-generator-tests",
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
    "title": "Running a Generated Generator",
    "subject": "running a generated generator",
    "description": "Running a generated generator is the first real run: the meta-generator feeds it a seed, watches its output, checks the output against its gates and its tests, and records the results. A generated generator that fails its first run is repaired and run again, and a generator that cannot pass is not filed. This record specifies the first-run rules: seed shown, output checked, results recorded,.",
    "label": "running-generated-generator",
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
    "title": "Validating a Generated Generator",
    "subject": "validating a generated generator",
    "description": "Validating a generated generator is the second pass, CHECK 2, that re-checks everything the first run checked, by execution: the demo runs, the program runs, the JCC code (JAH Condensed Code) round-trips, the sources return HTTP 200, and the generator passes its gates. A generated generator is only called validated when CHECK 2 passes with zero failures. This record specifies the validation.",
    "label": "validating-generated-generator",
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
