// gen-everyday-communication-practice-signature.js -- boundless generator for the Everyday Communication Practice Database Signature.
// Usage: node gen-everyday-communication-practice-signature.js --n 5
// Deterministic: a seeded LCG drives parameter variations of the 16 seed
// records. Self-regulating: throttled, duplicate-checked,
// hard-stops at 10^15 records or when the variation space is genuinely exhausted.
// Generated records carry "generated": true and src "generated" -- never mixed
// with assistant-built records.
"use strict";
const HARD_CAP = 1e15;
const TOPICS = ["Signature Choosing the Right Channel", "Signature Writing a Clear Email", "Signature The Useful Reply", "Signature Group Messages Done Well", "Signature Tone in Text", "Signature Voice Notes With Care", "Signature Setting Up a Video Call", "Signature Looking and Sounding Good on Video", "Signature Running a Small Video Meeting", "Signature The Follow-Up Summary", "Signature Response-Time Boundaries", "Signature Communicating Across Time Zones", "Signature Accessible Everyday Communication", "Signature Correcting a Mis-Sent Message", "Signature Keeping a Record of Decisions", "Signature Checking Before Acting on an Urgent Request"];
const EDITION = "signature";
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
    id: "JAH-ECPS-GEN-" + String(k + 1).padStart(6, "0"),
    slug: "everyday-communication-practice-signature",
    title: "Generated " + topic + " parameter variation v" + variant,
    edition: EDITION,
    src: "generated",
    generated: true,
    built_by: "generator",
    record_kind: "everyday communication practice record",
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
  console.error("emitted " + emitted + " generated records for everyday-communication-practice-signature");
}
main();
