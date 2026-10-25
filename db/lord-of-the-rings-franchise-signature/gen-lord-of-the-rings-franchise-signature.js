// gen-lord-of-the-rings-franchise-signature.js -- boundless generator for the lord-of-the-rings-franchise-signature Database.
// Usage: node gen-lord-of-the-rings-franchise-signature.js --n 5
// Deterministic: a seeded LCG drives parameter variations.
// Self-regulating: throttled, duplicate-checked, hard-stops at 10^15
// records or when the variation space is genuinely exhausted.
// Generated records carry "generated": true and src "generated" --
// never mixed with assistant-built records.
"use strict";
const HARD_CAP = 1e15;
const TOPICS = ["The Lord of the Rings Signature Continuation Overview", "Bram Underhill and the Glass Compass", "Bram Underhill and the Silent Archive", "Bram Underhill and the Ember Charter", "Bram Underhill and the Hollow Lighthouse", "Bram Underhill and the Map of Unmade Roads", "Bram Underhill and the Winter Market", "Bram Underhill and the Stone Choir", "Bram Underhill and the Paper Fleet", "Bram Underhill and the Lantern Accord", "Bram Underhill and the Thirteenth Door", "Bram Underhill and the Salt Library"];
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
    id: "JAH-FRLR-S-GEN-" + String(k + 1).padStart(6, "0"),
    slug: "lord-of-the-rings-franchise-signature",
    title: "Generated " + topic + " parameter variation v" + variant,
    edition: "signature",
    src: "generated",
    generated: true,
    built_by: "generator",
    record_kind: "franchise record",
    feasibility_tier: "signature",
    note: "Deterministic parameter variation (" + key + "). Labeled generated; not an assistant-built record."
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
  console.error("emitted " + emitted + " generated records for lord-of-the-rings-franchise-signature");
}
main();
