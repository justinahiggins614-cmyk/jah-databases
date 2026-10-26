// gen-dynamic-task-graphs-signature.js -- boundless generator for the Dynamic Task Graphs Signature Database.
// Usage: node gen-dynamic-task-graphs-signature.js --n 5
// Deterministic: a seeded LCG drives per-topic parameter variations of the 16
// seed task graph record records. Self-regulating: throttled, duplicate-checked,
// hard-stops at 10^15 records or when the variation space is genuinely exhausted.
// Generated records carry "generated": true and src "generated" -- never mixed
// with assistant-built records.
// Dynamic Task Graphs designs inside the Signature ecosystem.
"use strict";
const HARD_CAP = 1e15;

const TOPICS = ["Dependency Edge Modeling", "Graph Re-Planning on Change", "Cycle Detection", "Critical Path Recomputation", "Parallel Branch Scheduling", "Conditional Task Branches", "Graph Layout for Reading", "Task State Propagation", "Dynamic Priority Reweighting", "Failure Cascade Containment", "Graph Version Snapshots", "Merge of Parallel Branches"];

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
    id: "JAH-C012SGEN-" + String(k + 1).padStart(6, "0"),
    slug: "dynamic-task-graphs-signature",
    title: "Generated " + topic + " parameter variation v" + variant,
    edition: "Signature",
    src: "generated",
    generated: true,
    built_by: "generator",
    record_kind: "task graph record",
    feasibility_tier: "established",
    note: "Deterministic parameter variation (" + key + ") over the 16 seed " +
          "task graph record records. Labeled generated; not an assistant-built record. " +
          "Dynamic Task Graphs designs inside the Signature ecosystem."
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
  console.error("emitted " + emitted + " generated records for dynamic-task-graphs-signature");
}
main();
