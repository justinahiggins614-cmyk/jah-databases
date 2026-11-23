// Seeded boundless generator for the Website Generator
// (signature edition). Deterministic: the same seed always emits the same
// record. Usage: node gen-website-generator-signature.js [seed]  (prints one
// JSON record) or: node gen-website-generator-signature.js --test (runTests).
// Package-only; outputs are generated, not stored files.
"use strict";
const crypto = require("crypto");

const SLUG = "website-generator-signature";
const RECORD_KIND = "website generator record";
const ID_PREFIX = "JAH-WSGNS-";
const AI_NAME = "JAH Website Generator Librarian (Signature)";
const EDITION = "signature";
const CEILING = "Generator ceiling: up to 1,000,000,000 scales per file, generated on demand by the file AI \u2014 not stored files.";

const TOPICS = [
  {
    "title": "Signature Front Porch",
    "subject": "signature front porch",
    "description": "The Signature Front Porch is a design for a porch that welcomes readers into a website: a hero, a title, one status line, and a tab bar, with the big lists kept behind doors of their own. The design imagines the front door as a porch, where the welcome is simple and the furniture is inside.",
    "label": "signature-front-porch",
    "figures": {
      "front_door_parts": 4,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "glossary_terms": 27,
      "sections": 14,
      "tabs": 5,
      "hard_stop": 1000000000
    }
  },
  {
    "title": "Signature Tab Fan",
    "subject": "signature tab fan",
    "description": "The Signature Tab Fan is a design for a fan of tabs: each tab is one section, the fan opens to show them all, and the catalog tab sits at the end, always last. The design imagines tab pages as a fan, where each fold is a section and the last fold holds the archive.",
    "label": "signature-tab-fan",
    "figures": {
      "tab_rules": 3,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "glossary_terms": 27,
      "sections": 14,
      "tabs": 5,
      "hard_stop": 1000000000
    }
  },
  {
    "title": "Signature Archive Room",
    "subject": "signature archive room",
    "description": "The Signature Archive Room is a design for a room that holds the big list: a million-file catalog behind one door, grouped by letter, each letter's group closed until opened, and the AI's finest record pinned above the door with an Ask the AI box beside it. The design imagines the catalog as a room of its own, where the list cannot block the front door.",
    "label": "signature-archive-room",
    "figures": {
      "catalog_parts": 4,
      "letters": 26,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "glossary_terms": 27,
      "sections": 14,
      "hard_stop": 1000000000
    }
  },
  {
    "title": "Signature Template Loom",
    "subject": "signature template loom",
    "description": "The Signature Template Loom is a design for a loom that weaves website templates: front door, tab bar, record page, search page, and navigation are the threads, and the finished cloth is a reusable shape carrying structure only, never another site's branding. The design imagines templates as woven cloth, where the pattern can be reused and the brand can never be stolen.",
    "label": "signature-template-loom",
    "figures": {
      "template_parts": 5,
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
    "title": "Signature Signpost Road",
    "subject": "signature signpost road",
    "description": "The Signature Signpost Road is a design for a road through a website: the tab bar points to sections above, and the network navigation runs along the bottom, with the current site marked as you are here. The design imagines navigation as a road with signposts, where no page is without a way onward.",
    "label": "signature-signpost-road",
    "figures": {
      "nav_bars": 2,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "glossary_terms": 27,
      "sections": 14,
      "sites": 39,
      "hard_stop": 1000000000
    }
  },
  {
    "title": "Signature Search Well",
    "subject": "signature search well",
    "description": "The Signature Search Well is a design for a well that holds website search: the index is the water, the query is the bucket, and every bucket drawn carries full records with the matching words shown. The design imagines search as drawing water, where a search that finds nothing says so plainly instead of guessing.",
    "label": "signature-search-well",
    "figures": {
      "search_modes": 4,
      "indexed_fields": 11,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "glossary_terms": 27,
      "sections": 14,
      "hard_stop": 1000000000
    }
  },
  {
    "title": "Signature Plain Glass",
    "subject": "signature plain glass",
    "description": "The Signature Plain Glass is a design for glass that shows a website without scripts: every page readable as plain text, every list reachable by links, and no login required. The design imagines accessibility as clear glass, where the plain version shows exactly what the full version shows.",
    "label": "signature-plain-glass",
    "figures": {
      "mirror_parts": 3,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "glossary_terms": 27,
      "sections": 14,
      "formats": 4,
      "hard_stop": 1000000000
    }
  },
  {
    "title": "Signature Reading Voice",
    "subject": "signature reading voice",
    "description": "The Signature Reading Voice is a design for a voice that reads web pages aloud: one controller per page, starting one reading stops the current one, and double-tapping never stacks two readings. The design imagines read-aloud as a single voice in a quiet room, where the reader can always stop it with one button.",
    "label": "signature-reading-voice",
    "figures": {
      "controllers": 1,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "glossary_terms": 27,
      "sections": 14,
      "read_modes": 2,
      "hard_stop": 1000000000
    }
  }
];

const SOURCES = [
  {
    "name": "Wikipedia - Website",
    "url": "https://en.wikipedia.org/wiki/Website",
    "establishes": "Website: how web pages are organized into sites.",
    "retrieved": "2026-11-17",
    "resource_id": "en.wikipedia.org/wiki/Website"
  },
  {
    "name": "Wikipedia - Web development",
    "url": "https://en.wikipedia.org/wiki/Web_development",
    "establishes": "Web development: how websites are built and maintained.",
    "retrieved": "2026-11-17",
    "resource_id": "en.wikipedia.org/wiki/Web_development"
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
