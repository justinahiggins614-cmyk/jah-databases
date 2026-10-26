// gen-baseline-versus-enhanced-ai-comparisons.js -- boundless generator for the Baseline-versus-Enhanced AI Comparisons Database.
// Usage: node gen-baseline-versus-enhanced-ai-comparisons.js --n 5
// Deterministic: a seeded LCG drives per-topic parameter variations of the 16
// seed records. Self-regulating: throttled, duplicate-checked,
// hard-stops at 10^15 records or when the variation space is genuinely exhausted.
// Generated records carry "generated": true and src "generated" -- never mixed
// with assistant-built records.
"use strict";
const HARD_CAP = 1e15;

const TOPICS = ["Fixed Suite Retrieval Task", "Cross-Database Research Task", "Math Verification Task", "Complete File Generation Task", "Multi-Step Execution Task", "Failure Recovery Task", "Permission Enforcement Task", "Three-Arm Comparison Protocol", "Success Rate Ledger", "Error Taxonomy Log", "Time Measurement Method", "Cost Measurement Method", "Baseline Definition Record", "Retrieval Arm Definition", "Full-Stack Arm Definition", "Comparison Report Template", "Coverage Extension Note", "Variation Ledger Entry", "Parameter Sweep Record", "Template Reuse Note"];

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
    id: "JAH-C092-GEN-" + String(k + 1).padStart(6, "0"),
    slug: "baseline-versus-enhanced-ai-comparisons",
    title: "Generated " + topic + " parameter variation v" + variant,
    edition: "public",
    src: "generated",
    generated: true,
    built_by: "generator",
    record_kind: "baseline-versus-enhanced comparison record",
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
  console.error("emitted " + emitted + " generated records for baseline-versus-enhanced-ai-comparisons");
}
main();
