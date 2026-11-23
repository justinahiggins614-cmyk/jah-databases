// Seeded boundless generator for the Climate Restoration Research Database
// (signature edition). Deterministic: the same seed always emits the same
// record. Usage: node gen-climate-restoration-signature.js [seed]  (prints one
// JSON record) or: node gen-climate-restoration-signature.js --test (runTests).
// Package-only; outputs are generated, not stored files.
"use strict";
const crypto = require("crypto");

const SLUG = "climate-restoration-signature";
const RECORD_KIND = "future climate restoration research record";
const ID_PREFIX = "JAH-CLRES-";
const AI_NAME = "JAH Climate Restoration Researcher (Signature)";
const EDITION = "signature";
const CEILING = "Generator ceiling: up to 1,000,000,000 scales per file, generated on demand by the file AI \u2014 not stored files.";

const TOPICS = [
  {
    "title": "Signature Design: Climate Library",
    "subject": "signature climate library",
    "description": "A Signature-made design-study for a climate library: a library where every book is a restoration method, shelved by where its carbon is stored, in trees, in soil, in rocks, in the deep ocean, or underground, with the research-only rule written over the door. The design imagines the librarian stamping each book with its maturity label, T2, which means Hypothetical, a reasoned guess, not yet.",
    "label": "sig-climate-library",
    "figures": {
      "shelves": 5,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "glossary_terms": 47,
      "sections": 16,
      "ladder_ranks": 24,
      "books": 24
    }
  },
  {
    "title": "Signature Design: Removal Ledger",
    "subject": "signature removal ledger",
    "description": "A Signature-made design-study for a removal ledger: a great book where every tonne of carbon dioxide removed is written down once, with its baseline, which is the measurement of what would have happened without the project, its buffer, which is extra stored carbon set aside in case some is lost, and its auditor, an independent checker, beside it. The design imagines the ledger's rule in red.",
    "label": "sig-removal-ledger",
    "figures": {
      "entries": 24,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "glossary_terms": 47,
      "sections": 16,
      "ladder_ranks": 24,
      "rules": 3
    }
  },
  {
    "title": "Signature Design: Air Capture Mill",
    "subject": "signature air capture mill",
    "description": "A Signature-made design-study for an air capture mill: a mill with great fans blowing open air over filters that catch carbon dioxide, then heated to release the gas in pure form for storage underground. The design imagines the miller counting the energy per tonne and writing the cost on the mill wall, because the air holds only about four molecules of carbon dioxide in every ten thousand, and.",
    "label": "sig-air-capture-mill",
    "figures": {
      "fans": 4,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "glossary_terms": 47,
      "sections": 16,
      "ladder_ranks": 24,
      "carbon_per_10000_air": 4
    }
  },
  {
    "title": "Signature Design: Basalt Field",
    "subject": "signature basalt field",
    "description": "A Signature-made design-study for a basalt field: a field where crushed basalt, a dark volcanic rock, is spread to speed the natural weathering that captures carbon dioxide and carries it to the sea as bicarbonate, which is a dissolved form of carbon. The design imagines the field measured over five years, with soil and water tested each season, and the quarry that supplied the rock marked on.",
    "label": "sig-basalt-field",
    "figures": {
      "seasons": 4,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "glossary_terms": 47,
      "sections": 16,
      "ladder_ranks": 24,
      "capture_years": 5
    }
  },
  {
    "title": "Signature Design: Alkalinity Harbour",
    "subject": "signature alkalinity harbour",
    "description": "A Signature-made design-study for an alkalinity harbour: a harbour where alkaline materials are added to seawater in small measured amounts, so the ocean can hold more carbon dioxide, with watchers in boats testing the water and the plankton, which are tiny organisms drifting in the sea, every day. The design imagines the harbour's rule: no large addition before years of small trials, and.",
    "label": "sig-alkalinity-harbour",
    "figures": {
      "watchers": 4,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "glossary_terms": 47,
      "sections": 16,
      "ladder_ranks": 24,
      "materials": 2
    }
  },
  {
    "title": "Signature Design: Forest Nursery",
    "subject": "signature forest nursery",
    "description": "A Signature-made design-study for a forest nursery: a nursery where mixed native trees are grown for planting, with the right trees matched to the right places, local people as the planters, and a twenty-year growth chart on the nursery wall. The design imagines the nursery refusing single-species plantations, because a forest of one species stores carbon for a while and then fails, while a.",
    "label": "sig-forest-nursery",
    "figures": {
      "tree_mixes": 6,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "glossary_terms": 47,
      "sections": 16,
      "ladder_ranks": 24,
      "growth_years": 20
    }
  },
  {
    "title": "Signature Design: Soil Kitchen",
    "subject": "signature soil kitchen",
    "description": "A Signature-made design-study for a soil kitchen: a kitchen where compost, which is rotted plant and food matter, cover crops, which are plants grown to protect soil between harvests, and careful grazing are cooked into recipes for soil carbon, with each recipe tested on a field and its carbon measured yearly. The design imagines the kitchen's rule: no recipe is served until its carbon is.",
    "label": "sig-soil-kitchen",
    "figures": {
      "recipes": 4,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "glossary_terms": 47,
      "sections": 16,
      "ladder_ranks": 24,
      "fields": 4
    }
  },
  {
    "title": "Signature Design: Peat Bog Rewetting Crew",
    "subject": "signature peat bog rewetting crew",
    "description": "A Signature-made design-study for a peat bog rewetting crew: a crew that lets water back into drained peat bogs, blocking the ditches that dried them, so the bogs stop releasing carbon and begin storing it again, while watching wildlife return and floods slow. The design imagines the crew's logbook with water levels, carbon release, and wildlife counts, kept yearly, and a rule that no bog is.",
    "label": "sig-peat-bog-crew",
    "figures": {
      "crew_members": 6,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "glossary_terms": 47,
      "sections": 16,
      "ladder_ranks": 24,
      "bogs": 3
    }
  }
];

const SOURCES = [
  {
    "name": "Wikipedia - Carbon dioxide removal",
    "url": "https://en.wikipedia.org/wiki/Carbon_dioxide_removal",
    "establishes": "Carbon dioxide removal: taking carbon dioxide out of the air and storing it.",
    "retrieved": "2026-11-17",
    "resource_id": "en.wikipedia.org/wiki/Carbon_dioxide_removal"
  },
  {
    "name": "Wikipedia - Climate change mitigation",
    "url": "https://en.wikipedia.org/wiki/Climate_change_mitigation",
    "establishes": "Climate change mitigation: reducing emissions and removing carbon dioxide to limit warming.",
    "retrieved": "2026-11-17",
    "resource_id": "en.wikipedia.org/wiki/Climate_change_mitigation"
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
