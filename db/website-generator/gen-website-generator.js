// Seeded boundless generator for the Website Generator
// (public edition). Deterministic: the same seed always emits the same
// record. Usage: node gen-website-generator.js [seed]  (prints one
// JSON record) or: node gen-website-generator.js --test (runTests).
// Package-only; outputs are generated, not stored files.
"use strict";
const crypto = require("crypto");

const SLUG = "website-generator";
const RECORD_KIND = "website generator record";
const ID_PREFIX = "JAH-WSGN-";
const AI_NAME = "JAH Website Generator Librarian";
const EDITION = "public";
const CEILING = "Generator ceiling: up to 1,000,000,000 scales per file, generated on demand by the file AI \u2014 not stored files.";

const TOPICS = [
  {
    "title": "What a Website Generator Is",
    "subject": "website generator identity",
    "description": "A website generator is a program that creates complete websites: given a purpose and a content plan, it builds the front door, the tab pages, the catalog page, the search, the navigation, and the accessible mirror, and it checks every page by rendering it. It is a generator of whole sites, not of single pages, and it builds from structure, never by copying another site's brand names, logos,.",
    "label": "website-generator-identity",
    "figures": {
      "build_steps": 11,
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
    "title": "The Front Door",
    "subject": "the front door",
    "description": "The front door is the first page of a website: a hero image or title, one status line, and a tab bar, simple enough to read at a glance. A front door that lists a million records on its face is a door blocked by its own furniture. This record specifies the front-door rules: hero, title, one status line, tab bar, and the big lists kept behind buttons on their own pages.",
    "label": "front-door",
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
    "title": "Tab Pages",
    "subject": "tab pages",
    "description": "Tab pages are the sections of a website, each its own page under its own tab: one major section per tab, with the catalog or archive tab always last, never first. Tabs are the map of the site, and a site whose sections are all piled on one page has no map. This record specifies the tab rules: each major section its own tab page, catalog tab last, and the tab bar in calculator style, with the.",
    "label": "tab-pages",
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
    "title": "The Catalog Page",
    "subject": "the catalog page",
    "description": "The catalog page is the one page that holds the big list: a million-file collapsible A to Z catalog, reached by a front-door button, living only on its own tab page. Big lists live on their own page because a big list on the front door blocks it. This record specifies the catalog-page rules: one archive tab, collapsible per-letter groups, lazy loading, and the AI's Best of the Best pick pinned.",
    "label": "catalog-page",
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
    "title": "Website Templates",
    "subject": "website templates",
    "description": "A website template is a reusable shape for a website: the front door, the tab bar, the record page, the search page, and the navigation, laid out once so new sites can be built from it without starting over. Templates carry structure only, never another site's brand names, logos, trademarks, or copyrighted images. This record specifies the template rules: structure only, plain words, and every.",
    "label": "website-templates",
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
    "title": "Website Navigation",
    "subject": "website navigation",
    "description": "Website navigation is the set of links that lets a reader move through a site: the tab bar at the top for sections, and the network navigation at the bottom for the whole network. The network navigation sits at the bottom of every page, one instance per page, with the current site shown as you are here. This record specifies the navigation rules: tab bar for sections, bottom bar for the.",
    "label": "website-navigation",
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
    "title": "Website Search",
    "subject": "website search",
    "description": "Website search is the box that lets a reader ask a site for its records: the reader types words, the site searches its index, and the matching records are returned with the matching words shown. Search must work on the accessible mirror too, with no JavaScript required. This record specifies the search rules: every record indexed, results ranked best first, and a search that finds nothing.",
    "label": "website-search",
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
    "title": "The Accessible Mirror",
    "subject": "the accessible mirror",
    "description": "The accessible mirror is the plain version of a website that works with no JavaScript: every page readable as plain text, every list reachable by links, and no login required. Accessibility is not an extra: a page that only works with scripts running excludes readers and visiting AIs (artificial intelligences) alike. This record specifies the mirror rules: same content, same order, plain.",
    "label": "accessible-mirror",
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
