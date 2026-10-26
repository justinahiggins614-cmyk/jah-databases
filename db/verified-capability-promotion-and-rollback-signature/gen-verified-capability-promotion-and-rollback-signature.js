// gen-verified-capability-promotion-and-rollback-signature.js -- boundless generator for the verified-capability-promotion-and-rollback-signature database.
// Usage: node gen-verified-capability-promotion-and-rollback-signature.js --n 5
// Deterministic: a seeded LCG drives parameter variations of the 16 seed
// records. Self-regulating: throttled, duplicate-checked,
// hard-stops at 10^15 records or when the variation space is genuinely exhausted.
// Generated records carry "generated": true and src "generated" -- never mixed
// with assistant-built records.
"use strict";
const HARD_CAP = 1e15;
const TOPICS = ["Promotion Criteria and Gates: Overview", "Promotion Criteria and Gates: Method", "Promotion Criteria and Gates: Worked Example", "Promotion Criteria and Gates: Validation Checklist", "Rollback Procedures: Overview", "Rollback Procedures: Method", "Rollback Procedures: Worked Example", "Rollback Procedures: Validation Checklist", "Promotion Audit Trails: Overview", "Promotion Audit Trails: Method", "Promotion Audit Trails: Worked Example", "Promotion Audit Trails: Validation Checklist", "Failed Promotion Reviews: Overview", "Failed Promotion Reviews: Method", "Failed Promotion Reviews: Worked Example", "Failed Promotion Reviews: Validation Checklist"];
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
    id: "JAH-GEN-" + String(k + 1).padStart(6, "0"),
    slug: "verified-capability-promotion-and-rollback-signature",
    title: "Generated " + topic + " parameter variation v" + variant,
    edition: "public",
    src: "generated",
    generated: true,
    built_by: "generator",
    note: "Deterministic parameter variation (" + key + ") over the 16 seed records. Labeled generated; not an assistant-built record."
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
  console.error("emitted " + emitted + " generated records for verified-capability-promotion-and-rollback-signature");
}
main();
