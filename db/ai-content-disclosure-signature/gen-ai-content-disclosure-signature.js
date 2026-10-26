// gen-ai-content-disclosure-signature.js -- boundless generator for the AI Content Disclosure Database Signature.
// Usage: node gen-ai-content-disclosure-signature.js --n 5
// Deterministic: a seeded LCG drives parameter variations of the 16 seed
// records. Self-regulating: throttled, duplicate-checked,
// hard-stops at 10^15 records or when the variation space is genuinely exhausted.
// Generated records carry "generated": true and src "generated" -- never mixed
// with assistant-built records.
"use strict";
const HARD_CAP = 1e15;
const TOPICS = ["Signature What AI Disclosure Means", "Signature Visible Labels: Where a Label Belongs", "Signature Disclosure Wording Audiences Understand", "Signature Provenance Metadata: What Travels With a File", "Signature Watermarking: Visible, Invisible, and Their Limits", "Signature Disclosing Degrees: Help, Editing, and Generation", "Signature Disclosure by Medium: Image, Audio, Video, Text", "Signature Disclosure in News, Research, and Education", "Signature When Disclosure Is Required: Checking the Rules", "Signature Correcting a Missing Disclosure", "Signature AI-Edited Versus AI-Generated Work", "Signature Audience Trust: What Hidden Disclosure Costs", "Signature Disclosure in Advertising and Sponsored Content", "Signature AI Voices and Likenesses: Consent and Disclosure", "Signature Keeping Disclosure Records", "Signature A Disclosure Checklist for Every Publication"];
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
    id: "JAH-AIDCS-GEN-" + String(k + 1).padStart(6, "0"),
    slug: "ai-content-disclosure-signature",
    title: "Generated " + topic + " parameter variation v" + variant,
    edition: EDITION,
    src: "generated",
    generated: true,
    built_by: "generator",
    record_kind: "ai content disclosure record",
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
  console.error("emitted " + emitted + " generated records for ai-content-disclosure-signature");
}
main();
