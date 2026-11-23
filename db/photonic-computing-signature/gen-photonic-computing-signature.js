// Seeded boundless generator for the Photonic Computing Database
// (signature edition). Deterministic: the same seed always emits the same
// record. Usage: node gen-photonic-computing-signature.js [seed]  (prints one
// JSON record) or: node gen-photonic-computing-signature.js --test (runTests).
// Package-only; outputs are generated, not stored files.
"use strict";
const crypto = require("crypto");

const SLUG = "photonic-computing-signature";
const RECORD_KIND = "future photonic computing record";
const ID_PREFIX = "JAH-PHTCS-";
const AI_NAME = "JAH Photonic Computing Researcher (Signature)";
const EDITION = "signature";
const CEILING = "Generator ceiling: up to 1,000,000,000 scales per file, generated on demand by the file AI \u2014 not stored files.";

const TOPICS = [
  {
    "title": "Signature Design: Light Library",
    "subject": "signature light library",
    "description": "A Signature-made design-study for a light library: a library where every book is a beam, shelved by colour, with waveguides as aisles and interferometers as reading desks. The design imagines readers borrowing beams to calculate with, returning them unchanged, and a librarian who records which colour served which question. This is a design-study, labeled as a design and never presented as an.",
    "label": "sig-light-library",
    "figures": {
      "colours": 4,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "glossary_terms": 47,
      "sections": 16,
      "ladder_ranks": 24,
      "aisles": 4
    }
  },
  {
    "title": "Signature Design: Waveguide Garden",
    "subject": "signature waveguide garden",
    "description": "A Signature-made design-study for a waveguide garden: a garden where light travels along narrow glass paths between flower beds, each path a waveguide carrying one colour, and the gardener prunes the paths so no light leaks into the wrong bed. The design imagines the garden as the medium itself: brightness as numbers, colour as channels, and the meeting of two paths as addition. This is a.",
    "label": "sig-waveguide-garden",
    "figures": {
      "paths": 8,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "glossary_terms": 47,
      "sections": 16,
      "ladder_ranks": 24,
      "beds": 8
    }
  },
  {
    "title": "Signature Design: Silicon Orchard",
    "subject": "signature silicon orchard",
    "description": "A Signature-made design-study for a silicon orchard: an orchard where silicon trees grow light circuits in their branches, planted in rows by the same factories, called fabs, that grow electronic chips. The design imagines the orchard keeper grafting lasers from other materials onto silicon branches, because silicon does not make light easily, and testing each tree for loss before its fruit,.",
    "label": "sig-silicon-orchard",
    "figures": {
      "rows": 4,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "glossary_terms": 47,
      "sections": 16,
      "ladder_ranks": 24,
      "trees": 24
    }
  },
  {
    "title": "Signature Design: Integrated Circuit City",
    "subject": "signature integrated circuit city",
    "description": "A Signature-made design-study for an integrated circuit city: a city on one chip, with waveguides as streets, splitters as junctions, interferometers as workshops, modulators as sign painters, and detectors as town criers. The design imagines the city's rule against light leaking from one street into another, called crosstalk, and its inspectors testing every building, because one bad building.",
    "label": "sig-integrated-circuit-city",
    "figures": {
      "buildings": 100,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "glossary_terms": 47,
      "sections": 16,
      "ladder_ranks": 24,
      "streets": 20
    }
  },
  {
    "title": "Signature Design: Optical Brain Loft",
    "subject": "signature optical brain loft",
    "description": "A Signature-made design-study for an optical brain loft: a loft where a neural network, which is a computing system inspired by brains, is built from light, with interferometers as its neurons and weights, which are the numbers it has learned, hung on the walls like paintings. The design imagines training done downstairs in electronics, and the trained network run upstairs in light, fast and.",
    "label": "sig-optical-brain-loft",
    "figures": {
      "neurons": 64,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "glossary_terms": 47,
      "sections": 16,
      "ladder_ranks": 24,
      "paintings": 64
    }
  },
  {
    "title": "Signature Design: Two-Path Mill",
    "subject": "signature two-path mill",
    "description": "A Signature-made design-study for a two-path mill: a mill where light is split into two paths, one path shifted, and the two joined again, so the mill's output brightness grinds out a number. The design imagines rows of these mills, each a Mach-Zehnder interferometer, working side by side, each multiplying an input by a weight, which is a number the system has set, and their outputs gathered.",
    "label": "sig-two-path-mill",
    "figures": {
      "mills": 16,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "glossary_terms": 47,
      "sections": 16,
      "ladder_ranks": 24,
      "sacks": 4
    }
  },
  {
    "title": "Signature Design: Ring Pond",
    "subject": "signature ring pond",
    "description": "A Signature-made design-study for a ring pond: a pond with tiny rings floating on it, each ring trapping light of one colour while the rest flows past, like lily pads that catch only red petals. The design imagines the pond keeper warming a ring to shift its colour, so the ring can switch, filter, and modulate, and a thermometer at the pond's edge, because heat changes which colour each ring.",
    "label": "sig-ring-pond",
    "figures": {
      "rings": 32,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "glossary_terms": 47,
      "sections": 16,
      "ladder_ranks": 24,
      "colours": 4
    }
  },
  {
    "title": "Signature Design: Rainbow Post Office",
    "subject": "signature rainbow post office",
    "description": "A Signature-made design-study for a rainbow post office: a post office where thirty-two colours of light are sorted into thirty-two pigeonholes, each colour carrying one number down a single waveguide, and the sorters, who are filters, separate them again at the far end without mixing a single letter. The design imagines the postmaster's rule: every colour keeps its own laser and its own.",
    "label": "sig-rainbow-post-office",
    "figures": {
      "pigeonholes": 32,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "glossary_terms": 47,
      "sections": 16,
      "ladder_ranks": 24,
      "colours": 32
    }
  }
];

const SOURCES = [
  {
    "name": "Wikipedia - Optical computing",
    "url": "https://en.wikipedia.org/wiki/Optical_computing",
    "establishes": "Optical computing: computing with light instead of electricity.",
    "retrieved": "2026-11-17",
    "resource_id": "en.wikipedia.org/wiki/Optical_computing"
  },
  {
    "name": "Wikipedia - Photonic integrated circuit",
    "url": "https://en.wikipedia.org/wiki/Photonic_integrated_circuit",
    "establishes": "Photonic integrated circuit: a chip that guides and processes light.",
    "retrieved": "2026-11-17",
    "resource_id": "en.wikipedia.org/wiki/Photonic_integrated_circuit"
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
