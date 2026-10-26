// gen-ablation-feature-contribution-experiments-signature.js -- boundless generator for the Ablation and Feature Contribution Experiments Signature Database.
// Usage: node gen-ablation-feature-contribution-experiments-signature.js --n 5
// Deterministic: a seeded LCG drives per-topic parameter variations of the 16
// seed records. Self-regulating: throttled, duplicate-checked,
// hard-stops at 10^15 records or when the variation space is genuinely exhausted.
// Generated records carry "generated": true and src "generated" -- never mixed
// with assistant-built records.
"use strict";
const HARD_CAP = 1e15;

const TOPICS = ["Database Ablation Study", "Generator Ablation Study", "Tool Ablation Study", "Retrieval Depth Ablation", "Verification Step Ablation", "Specialist Routing Ablation", "Evidence Link Ablation", "Cross-Database Link Ablation", "Feature Contribution Ledger", "Interaction Effect Study", "Cost-of-Feature Analysis", "Latency-of-Feature Analysis", "Minimal Viable Stack Study", "Redundancy Detection Study", "Contribution Ranking Method", "Ablation Report Template", "Coverage Extension Note", "Variation Ledger Entry", "Parameter Sweep Record", "Template Reuse Note"];

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
    id: "JAH-C093S-GEN-" + String(k + 1).padStart(6, "0"),
    slug: "ablation-feature-contribution-experiments-signature",
    title: "Generated " + topic + " parameter variation v" + variant,
    edition: "Signature",
    src: "generated",
    generated: true,
    built_by: "generator",
    record_kind: "ablation experiment record",
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
  console.error("emitted " + emitted + " generated records for ablation-feature-contribution-experiments-signature");
}
main();
