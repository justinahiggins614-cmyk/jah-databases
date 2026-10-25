// gen-typed-artifact-generation.js -- boundless generator for the Typed Artifact Generation Database.
// Usage: node gen-typed-artifact-generation.js --n 5
// Deterministic seeded LCG; throttled to at most 100000 records per run;
// hard-stops at 10^15 records or when the variation space is genuinely exhausted.
// Generated records carry "generated": true and src "generated".
"use strict";
const HARD_CAP = 1e15;
const TOPICS = [
  "Typed Artifact Generation Overview Note",
  "Typed Artifact Generation Core Design Note",
  "Typed Artifact Generation Architecture Note",
  "Typed Artifact Generation Demo Variation",
  "Typed Artifact Generation Edge Case Study",
  "Typed Artifact Generation Limit Study",
  "Typed Artifact Generation Safeguard Note",
  "Typed Artifact Generation Roadmap Note",
  "Typed Artifact Generation Test Case",
  "Typed Artifact Generation Validation Note",
  "Typed Artifact Generation Cross-Link Study",
  "Typed Artifact Generation Failure Mode Note",
  "Typed Artifact Generation Scaling Note",
  "Typed Artifact Generation Audit Note",
  "Typed Artifact Generation Review Checklist",
  "Typed Artifact Generation Worked Example",
  "Typed Artifact Generation Comparison Note",
  "Typed Artifact Generation Glossary Entry"
];
function parseN(argv) {
  const i = argv.indexOf("--n");
  if (i >= 0 && argv[i + 1]) {
    const n = parseInt(argv[i + 1], 10);
    if (!isNaN(n) && n >= 0) return Math.min(n, 100000);
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
  const variant = 1 + Math.floor(rnd() * 50);
  const key = topic + "#v" + variant;
  if (seen.has(key)) return null;
  seen.add(key);
  return {
    id: "JAH-G29-GEN-" + String(k + 1).padStart(6, "0"),
    slug: "typed-artifact-generation",
    title: "Generated " + topic + " parameter variation v" + variant,
    edition: "public",
    src: "generated",
    generated: true,
    built_by: "generator",
    record_kind: "capability record",
    feasibility_tier: "established",
    note: "Deterministic parameter variation (" + key + ") over the seed records. Labeled generated; not an assistant-built record."
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
  console.error("emitted " + emitted + " generated records for typed-artifact-generation");
}
main();
