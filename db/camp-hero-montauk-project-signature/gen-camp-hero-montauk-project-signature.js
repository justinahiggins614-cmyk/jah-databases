// gen-camp-hero-montauk-project-signature.js -- boundless generator for the Camp Hero and the Montauk Project Database — Signature Edition.
// Usage: node gen-camp-hero-montauk-project-signature.js --n 5
// Deterministic seeded variations of the 16 seed records. Self-regulating:
// throttled, duplicate-checked, hard-stops at 10^15 records or when the
// variation space is genuinely exhausted. Generated records carry
// "generated": true and src "generated" -- never mixed with built records.
"use strict";
const HARD_CAP = 1e15;
const TOPICS = ["Signature Camp Hero Station Redesign", "Signature Long-Range Watch Panel", "Signature Station-to-Park Conversion Kit", "Signature Lighthouse Keeper's Log", "Signature Legend-Checking Worksheet", "Signature Magnetic Signature Reducer", "Signature Book-Series Growth Map", "Signature Program Separation Chart", "Signature Fiction-Inspiration Tracker", "Signature Beach Find Identifier", "Signature Warning Network Model", "Signature Source Criticism Ladder", "Signature Park Visit Planner", "Signature Claim Table Builder", "Signature Harbor Year Planner", "Signature Layered Interpretation Sign"];
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
  return { id: "JAH-CHMPS-GEN-" + String(k + 1).padStart(6, "0"), slug: "camp-hero-montauk-project-signature",
    title: "Generated " + topic + " parameter variation v" + variant,
    edition: "signature", src: "generated", generated: true, built_by: "generator",
    record_kind: "camp hero record", feasibility_tier: "established",
    note: "Deterministic parameter variation (" + key + ") over the 16 seed records. Labeled generated; not a built record." };
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
  console.error("emitted " + emitted + " generated records for camp-hero-montauk-project-signature");
}
main();
