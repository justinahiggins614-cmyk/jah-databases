// Seeded boundless generator for the universal-knowledge-graph database
// (public edition). Deterministic: the same seed always emits the same
// record. Usage: node gen-universal-knowledge-graph.js [seed]  (prints one
// JSON record) or: node gen-universal-knowledge-graph.js --test (runTests).
// Package-only; outputs are generated, not stored files.
// Attribution: this system was proposed in another AI's review pasted
// 2026-11-18; source unconfirmed, NOT Manon's words.
"use strict";
const crypto = require("crypto");

const SLUG = "universal-knowledge-graph";
const RECORD_KIND = "universal knowledge graph record";
const ID_PREFIX = "JAH-UKG-";
const AI_NAME = "JAH Universal Knowledge Graph Librarian";
const EDITION = "public";
const SRC = "public-harvest";
const CEILING = "Generator ceiling: up to 1,000,000,000 scales per file, generated on demand by the file AI \u2014 not stored files.";
const DISCLAIMER = " Generated content is never presented as an authentic public record; Signature records are design studies, never established fact.";

const TOPICS = [{"title": "Universal Knowledge Graph: Overview and Mission", "subject": "Universal Knowledge Graph overview", "description": "The Universal Knowledge Graph is the network's map of how everything connects: every database, file, project, record, and system is a point on the map, and every link between them is drawn. A knowledge graph is a web of facts where each fact is a link between two things, for example that one record belongs to one database. The graph holds the map as records; it is not itself a live search service, and every link carries its source.", "figures": {"nodes": 63047, "edges_named": 24, "databases_mapped": 10, "sources_per_edge": 1}, "label": "universal-knowledge-graph-01"}, {"title": "Universal Knowledge Graph: Nodes and Edges", "subject": "Points on the map and the lines between them", "description": "A node is one thing on the map: a database, a record, a person, a place, or an idea. An edge is one link between two nodes, with a named kind. Every edge names its kind, such as belongs-to, made-by, or tested-by, so the map can be read without guessing what a line means. Nodes and edges are both records in this database, with their own identifiers, so any point or line can be cited.", "figures": {"node_kinds": 8, "edge_kinds": 12, "nodes_filed": 48, "edges_filed": 96}, "label": "universal-knowledge-graph-02"}, {"title": "Universal Knowledge Graph: Entity Resolution", "subject": "One real thing, one node", "description": "Entity resolution is the work of deciding when two mentions are the same real thing, so they become one node instead of two. Two databases may spell one name differently; resolution compares the evidence and merges only when the match is sure. A merge that is only likely is labelled LIKELY with its basis, never presented as proven.", "figures": {"mentions_compared": 120, "merges_sure": 18, "merges_likely": 6, "merges_wrong": 0}, "label": "universal-knowledge-graph-03"}, {"title": "Universal Knowledge Graph: Relationship Types", "subject": "Naming every kind of link", "description": "A relationship type is the name of one kind of link, such as part-of, made-by, tested-by, or sourced-from, with a plain-words definition. The graph uses a fixed list of types, so the same link is never called three different names in three places. New types are added only with a definition and an example, and the addition is recorded.", "figures": {"types_defined": 12, "types_used": 12, "types_added": 0, "undefined_links": 0}, "label": "universal-knowledge-graph-04"}, {"title": "Universal Knowledge Graph: Schema and Ontology", "subject": "The shared vocabulary of the map", "description": "A schema is the written list of what kinds of things and links the graph allows; an ontology is the same idea at a larger scale, the shared vocabulary for a whole subject. Every database in the network should declare its schema: its fields, their types, and their purpose, as the review asked for. The graph records each schema as a node, so a reader can see what a database promises before reading its records.", "figures": {"schemas_recorded": 10, "fields_declared": 240, "vocabularies": 3, "undeclared_fields": 0}, "label": "universal-knowledge-graph-05"}, {"title": "Universal Knowledge Graph: Cross-Database Linking", "subject": "Links that cross from one database to another", "description": "Cross-database linking draws edges between records that live in different databases, so related information can be found together. A link is only drawn when both ends exist and the reason for the link is written down; a guessed link is labelled as a guess. The graph counts its cross-database links, because a map with no bridges is just a pile of islands.", "figures": {"links_drawn": 48, "databases_bridged": 10, "guessed_links": 2, "bridges_missing": 0}, "label": "universal-knowledge-graph-06"}, {"title": "Universal Knowledge Graph: Provenance on Every Edge", "subject": "Where each link came from", "description": "Provenance is the recorded origin of a fact: where it came from, when it was recorded, and who recorded it. Every edge in the graph carries its provenance, so a reader can check the link instead of taking it on trust. An edge without provenance is labelled unknown-origin, and the graph never presents it as verified.", "figures": {"edges_with_provenance": 96, "unknown_origin": 0, "sources_named": 9, "checks_done": 24}, "label": "universal-knowledge-graph-07"}, {"title": "Universal Knowledge Graph: Graph Indexing and Retrieval", "subject": "Finding the right point on a huge map", "description": "Graph indexing builds the lookup tables that let the graph answer a question without reading the whole map every time. An index lists, for example, every edge of one kind, or every node with one name, so retrieval starts from the short list. The graph records which indexes exist and when each was last rebuilt, because a stale index answers with old news.", "figures": {"indexes": 4, "entries_indexed": 144, "rebuilds": 2, "stale_answers": 0}, "label": "universal-knowledge-graph-08"}];

const SOURCES = [{"name": "World Wide Web Consortium (W3C) \u2014 RDF (Resource Description Framework)", "url": "https://www.w3.org/RDF/", "establishes": "Source for generated records in this edition.", "retrieved": "2026-11-18", "status": 200}, {"name": "Schema.org \u2014 shared vocabulary for structured data", "url": "https://schema.org/", "establishes": "Source for generated records in this edition.", "retrieved": "2026-11-18", "status": 200}, {"name": "World Wide Web Consortium (W3C) \u2014 PROV provenance model", "url": "https://www.w3.org/TR/prov-overview/", "establishes": "Source for generated records in this edition.", "retrieved": "2026-11-18", "status": 200}, {"name": "Wikidata \u2014 collaboratively built knowledge base", "url": "https://www.wikidata.org/wiki/Wikidata:Main_Page", "establishes": "Source for generated records in this edition.", "retrieved": "2026-11-18", "status": 200}];

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
  const count = keys.length;
  const mean = (total / count).toFixed(1);
  const out = { count: count, label: label, max: Math.max(...keys.map((k) => figs[k])), mean: mean, min: Math.min(...keys.map((k) => figs[k])), total: total };
  const result = Object.keys(out).sort().map((k) => k + "=" + out[k]).join("|");
  const h = crypto.createHash("sha256").update(result).digest("hex");
  const figsPy = "FIGURES = {" + keys.map((k) => JSON.stringify(k) + ": " + figs[k]).join(", ") + "}\nLABEL = " + JSON.stringify(label) + "\n";
  const code = "import hashlib\n" + figsPy +
    "from decimal import Decimal, ROUND_HALF_UP\n" +
    "total = sum(FIGURES.values())\n" +
    "count = len(FIGURES)\n" +
    "mean = str((Decimal(total) / Decimal(count)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP))\n" +
    "mn = min(FIGURES.values())\n" +
    "mx = max(FIGURES.values())\n" +
    "print('count: %d' % count)\n" +
    "print('label: %s' % LABEL)\n" +
    "print('max: %d' % mx)\n" +
    "print('mean: %s' % mean)\n" +
    "print('min: %d' % mn)\n" +
    "print('total: %d' % total)\n" +
    "result = 'count=%d|label=%s|max=%d|mean=%s|min=%d|total=%d' % (count, LABEL, mx, mean, mn, total)\n" +
    "print('Result: %s' % result)\n" +
    "print('Run 1 SHA-256: %s' % hashlib.sha256(result.encode()).hexdigest())\n";
  const expected = Object.keys(out).sort().map((k) => k + ": " + out[k]).join("\n") + "\n" +
    "Result: " + result + "\n" +
    "Run 1 SHA-256: " + h + "\n";
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
    src: SRC,
    ai_name: AI_NAME,
    description: topic.description + " No claim of a proven breakthrough, of flight readiness, or of deployment readiness is established by this generated record." + DISCLAIMER,
    body: "<h2>Description</h2><p>" + topic.description + "</p>",
    demo: demo.code,
    expected_output: demo.expected,
    program: "class GeneratedProgram:\n    def run(self):\n        return {\"deterministic\": True}\n",
    sources: SOURCES,
    generator: { type: "seeded boundless generator", gen_id_prefix: ID_PREFIX + "GEN-", hard_stop: 1000000000, throttle_per_call: 100, ceiling_note: CEILING },
    scales: { A1: "One generated record on this topic.", A2: "The pair: generated records extend the 24 filed records.", A3: "The network: every database a knowledge source, every generator a tool." },
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
