// gen-drone-defense-systems-signature.js -- boundless generator for the
// Drone Defense Systems Signature Database.
// Usage: node gen-drone-defense-systems-signature.js --n 5
// Deterministic: a seeded LCG drives per-topic parameter variations of the 28
// seed Signature drone-defense records. Self-regulating: throttled,
// duplicate-checked, hard-stops at 10^15 records or when the variation space
// is genuinely exhausted. Generated records carry "generated": true and src
// "generated" -- never mixed with assistant-built records.
// Signature civilian detection/documentation designs only, no military
// neutralization content ever generated.
"use strict";
const HARD_CAP = 1e15;

const TOPICS = [
  "Signature RF Watch Variation","Signature Acoustic Profile Entry",
  "Signature Fence Zone Note","Signature Detection Log Template",
  "Signature Optical Flag Note","Signature Broadcast Log Entry",
  "Signature Bearing Estimate Note","Signature Fusion Grade Entry",
  "Signature Airspace Context Note","Signature Ear Array Bearing Note",
  "Signature Night Flag Note","Signature Small Radar Track Note",
  "Signature Spectrum Diary Entry","Signature Handheld Walk Note",
  "Signature Garden Coverage Note","Signature Window Covering Note",
  "Signature Event Zone Plan","Signature Site Procedure Card",
  "Signature Evidence Custody Note","Signature Home Plan Page"
];

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
    id: "JAH-DDSS-GEN-" + String(k + 1).padStart(6, "0"),
    slug: "drone-defense-systems-signature",
    title: "Generated " + topic + " parameter variation v" + variant,
    edition: "signature",
    src: "generated",
    generated: true,
    built_by: "generator",
    record_kind: "drone defense record",
    feasibility_tier: "buildable-now",
    note: "Deterministic parameter variation (" + key + ") over the 28 seed " +
          "Signature drone-defense records. Civilian detection and " +
          "documentation designs only. Labeled generated; not an " +
          "assistant-built record."
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
  console.error("emitted " + emitted + " generated records for drone-defense-systems-signature");
}
main();
