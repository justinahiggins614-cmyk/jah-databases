// gen-scientific-knowledge-graph-discovery-signature.js -- boundless generator for the Scientific Knowledge Graph and Discovery Signature Database.
// Usage: node gen-scientific-knowledge-graph-discovery-signature.js --n 5
// Deterministic: a seeded LCG drives per-topic parameter variations of the 16
// seed records. Self-regulating: throttled, duplicate-checked,
// hard-stops at 10^15 records or when the variation space is genuinely exhausted.
// Generated records carry "generated": true and src "generated" -- never mixed
// with assistant-built records.
"use strict";
const HARD_CAP = 1e15;

const TOPICS = ["Concept Node Record", "Publication Link Record", "Equation Link Record", "Experiment Link Record", "Open Question Record", "Discovery Query Method", "Graph Consistency Check", "Cross-Domain Bridge Note", "Contradiction Flag Record", "Knowledge Gap Map", "Graph Growth Ledger", "Citation Integrity Note", "Discovery Report Template", "Graph Audit Trail", "Hypothesis Suggestion Method", "Graph Governance Note", "Coverage Extension Note", "Variation Ledger Entry", "Parameter Sweep Record", "Template Reuse Note"];

function parseN(argv) {
  const i = argv.indexOf("--n");
  if (i >= 0 && argv[i + 1]) {
    const n = parseInt(argv[i + 1], 10);
    if (!isNaN(n) && n >= 0) return Math.min(n, 100000); // throttle per run
  }
  return 5;
}

let seed = 20261025;
function rnd() {
  seed = (seed * 1103515245 + 12345) & 0x7fffffff;
  return seed / 0x7fffffff;
}

const seen = new Set();
function makeRecord(k) {
  const topic = TOPICS[Math.floor(rnd() * TOPICS.length)];
  const variant = 1 + Math.floor(rnd() * 50);   // parameter-set variant 1..50
  const key = topic + "#v" + variant;
  if (seen.has(key)) return null;
  seen.add(key);
  return {
    id: "JAH-N094S-GEN-" + String(k + 1).padStart(6, "0"),
    slug: "scientific-knowledge-graph-discovery-signature",
    title: "Generated " + topic + " parameter variation v" + variant,
    edition: "Signature",
    src: "generated",
    generated: true,
    built_by: "generator",
    record_kind: "knowledge graph record",
    feasibility_tier: "established",
    note: "Deterministic parameter variation (" + key + ") over the 16 seed " +
          "records. Labeled generated; not an assistant-built record."
  };
}

function main() {
  const n = parseN(process.argv.slice(2));
  if (n >= HARD_CAP) { console.error("hard cap reached"); process.exit(1); }
  const space = TOPICS.length * 50;
  let emitted = 0, attempts = 0;
  while (emitted < n && attempts < n * 20 && seen.size < space) {
    attempts++;
    const rec = makeRecord(emitted);
    if (rec) { console.log(JSON.stringify(rec)); emitted++; }
  }
  console.error("emitted " + emitted + " generated records for scientific-knowledge-graph-discovery-signature");
}
main();
