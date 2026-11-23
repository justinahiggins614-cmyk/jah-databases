// Seeded boundless generator for the Generator Registry and Marketplace
// (signature edition). Deterministic: the same seed always emits the same
// record. Usage: node gen-generator-registry-marketplace-signature.js [seed]  (prints one
// JSON record) or: node gen-generator-registry-marketplace-signature.js --test (runTests).
// Package-only; outputs are generated, not stored files.
"use strict";
const crypto = require("crypto");

const SLUG = "generator-registry-marketplace-signature";
const RECORD_KIND = "generator registry marketplace record";
const ID_PREFIX = "JAH-GREGS-";
const AI_NAME = "JAH Generator Registry and Marketplace Librarian (Signature)";
const EDITION = "signature";
const CEILING = "Generator ceiling: up to 1,000,000,000 scales per file, generated on demand by the file AI \u2014 not stored files.";

const TOPICS = [
  {
    "title": "The Dependency Tree — Signature Design",
    "subject": "dependency tree design",
    "description": "The Dependency Tree is a Signature-made design for the generator dependency manager, imagined as a tree where each generator is a branch and each dependency is a root. A branch cannot grow without its roots, and a root shared by many branches is a part many generators need. The design shows how dependencies could be seen: a tree where a cut root shows which branches would fall.",
    "label": "dependency-tree-design",
    "figures": {
      "checks": 3,
      "fields": 5,
      "steps": 4,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "glossary_terms": 53,
      "sections": 16,
      "topic_index": 1
    }
  },
  {
    "title": "The Build Kitchen — Signature Design",
    "subject": "build kitchen design",
    "description": "The Build Kitchen is a Signature-made design for the build and deployment manager, imagined as a kitchen where a generated project is cooked into a package. The recipe is on the wall, the ingredients are the code and parts, and the oven is the build step. A dish that fails its tasting is never served. The design shows how building could be a kitchen: recipe, ingredients, oven, and tasting.",
    "label": "build-kitchen-design",
    "figures": {
      "checks": 3,
      "fields": 5,
      "steps": 5,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "glossary_terms": 53,
      "sections": 16,
      "topic_index": 2
    }
  },
  {
    "title": "The Regression Loom — Signature Design",
    "subject": "regression loom design",
    "description": "The Regression Loom is a Signature-made design for automated regression testing, imagined as a loom where the old cloth is rewoven after every change. If the new cloth matches the old pattern, the change is safe; a thread out of place is a regression, and the loom stops until it is fixed. The design shows how regression testing could be weaving: the old pattern rewoven, thread by thread, after.",
    "label": "regression-loom-design",
    "figures": {
      "checks": 4,
      "fields": 6,
      "steps": 5,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "glossary_terms": 53,
      "sections": 16,
      "topic_index": 3
    }
  },
  {
    "title": "The Compatibility Map — Signature Design",
    "subject": "compatibility map design",
    "description": "The Compatibility Map is a Signature-made design for software compatibility testing, imagined as a map of lands: operating systems, Python versions, hardware, and dependencies. Each land is colored by whether a generator works there, fails there, or was never tried there. The design shows how compatibility could be read: a map of lands, colored by result.",
    "label": "compatibility-map-design",
    "figures": {
      "checks": 3,
      "fields": 5,
      "steps": 4,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "glossary_terms": 53,
      "sections": 16,
      "topic_index": 4
    }
  },
  {
    "title": "The Contract Seal — Signature Design",
    "subject": "contract seal design",
    "description": "The Contract Seal is a Signature-made design for API contract verification, imagined as a wax seal pressed on a contract between two programs. The seal is broken and re-pressed at every verification: if the API's answer matches the promise, the seal holds; if not, the seal cracks and the mismatch is named. The design shows how a contract could be sealed: pressed, checked, and cracked when broken.",
    "label": "contract-seal-design",
    "figures": {
      "checks": 3,
      "fields": 5,
      "steps": 5,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "glossary_terms": 53,
      "sections": 16,
      "topic_index": 5
    }
  },
  {
    "title": "The Component Shelf — Signature Design",
    "subject": "component shelf design",
    "description": "The Component Shelf is a Signature-made design for the reusable component library, imagined as a shelf of labeled jars, each holding one working module. A generator builder takes a jar from the shelf instead of making the module again, and returns it when done. The design shows how reuse could be a shelf: labeled jars, taken and returned, never rebuilt.",
    "label": "component-shelf-design",
    "figures": {
      "checks": 3,
      "fields": 5,
      "steps": 4,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "glossary_terms": 53,
      "sections": 16,
      "topic_index": 6
    }
  },
  {
    "title": "The Catalog Hall — Signature Design",
    "subject": "catalog hall design",
    "description": "The Catalog Hall is a Signature-made design for generator catalog records, imagined as a hall with one plaque per generator. Each plaque names the generator's purpose, inputs, outputs, dependencies, and tests, so a reader can choose without running anything. The design shows how a catalog could be walked: plaques in a hall, read before any run.",
    "label": "catalog-hall-design",
    "figures": {
      "checks": 3,
      "fields": 5,
      "steps": 4,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "glossary_terms": 53,
      "sections": 16,
      "topic_index": 7
    }
  },
  {
    "title": "The Inspection Lens — Signature Design",
    "subject": "inspection lens design",
    "description": "The Inspection Lens is a Signature-made design for generator inspection reports, imagined as a great lens through which a generator is read before it runs. The lens shows the code, the dependencies, the tests, and the past runs, magnified, so a hidden dependency or a missing test is seen at once. The design shows how inspection could be a lens: magnified, read, and written down before any run.",
    "label": "inspection-lens-design",
    "figures": {
      "checks": 4,
      "fields": 6,
      "steps": 5,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "glossary_terms": 53,
      "sections": 16,
      "topic_index": 8
    }
  }
];

const SOURCES = [
  {
    "name": "Wikipedia - Software repository",
    "url": "https://en.wikipedia.org/wiki/Software_repository",
    "establishes": "Software repository: how software and its parts are stored, listed, and fetched.",
    "retrieved": "2026-11-18",
    "resource_id": "en.wikipedia.org/wiki/Software_repository"
  },
  {
    "name": "Wikipedia - Package manager",
    "url": "https://en.wikipedia.org/wiki/Package_manager",
    "establishes": "Package manager: how software packages are installed, updated, and removed.",
    "retrieved": "2026-11-18",
    "resource_id": "en.wikipedia.org/wiki/Package_manager"
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
