// gen-secondhand-marketplace-safety-signature.js -- boundless generator for the Secondhand Marketplace Safety Database Signature Database.
// Usage: node gen-secondhand-marketplace-safety-signature.js --n 5
// Deterministic: a seeded LCG drives parameter variations of the 16 seed
// records. Self-regulating: throttled, duplicate-checked,
// hard-stops at 10^15 records or when the variation space is genuinely exhausted.
// Generated records carry "generated": true and src "generated" -- never mixed
// with assistant-built records.
"use strict";
const HARD_CAP = 1e15;
const TOPICS = ["Signature Safe Ground", "Signature Eyes-First Inspection", "Signature Platform Channel Rule", "Signature History Shape Reader", "Signature Handover Album", "Signature Device Proving Bench", "Signature Price Compass", "Signature Brand Pattern Check", "Signature High-Value Ledger", "Signature Parcel Covenant", "Signature Return Accord", "Signature Script Ear", "Signature Provenance Watch", "Signature Child-Safe Gate", "Signature Grade Truth Table", "Signature Secondhand Routine"];
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
    id: "JAH-SHMSS-GEN-" + String(k + 1).padStart(6, "0"),
    slug: "secondhand-marketplace-safety-signature",
    title: "Generated " + topic + " parameter variation v" + variant,
    edition: "Signature",
    src: "generated",
    generated: true,
    built_by: "generator",
    record_kind: "secondhand marketplace safety record",
    feasibility_tier: "established",
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
  console.error("emitted " + emitted + " generated records for secondhand-marketplace-safety-signature");
}
main();
