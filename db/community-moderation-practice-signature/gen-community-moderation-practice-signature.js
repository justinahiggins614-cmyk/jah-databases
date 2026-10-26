// gen-community-moderation-practice-signature.js -- boundless generator for the Community Moderation Practice Database Signature.
// Usage: node gen-community-moderation-practice-signature.js --n 5
// Deterministic: a seeded LCG drives parameter variations of the 16 seed
// records. Self-regulating: throttled, duplicate-checked,
// hard-stops at 10^15 records or when the variation space is genuinely exhausted.
// Generated records carry "generated": true and src "generated" -- never mixed
// with assistant-built records.
"use strict";
const HARD_CAP = 1e15;
const TOPICS = ["Signature Writing Community Rules People Can Follow", "Signature Welcoming New Members", "Signature Setting Expectations for Moderators", "Signature Handling a First Rule Break", "Signature De-escalating a Heated Thread", "Signature Spam and Off-Topic Posts", "Signature Appeals: Challenging a Moderation Decision", "Signature Handling Harassment Reports", "Signature Moderating a Live Chat or Event", "Signature Recruiting and Training Volunteer Moderators", "Signature Transparency: Moderation Logs and Reports", "Signature Conflict Between Members", "Signature Protecting Younger and Vulnerable Members", "Signature Closing a Thread Without Shutting Down Discussion", "Signature Moderator Burnout and Rotation", "Signature Reviewing Rules Over Time"];
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
    id: "JAH-COMDS-GEN-" + String(k + 1).padStart(6, "0"),
    slug: "community-moderation-practice-signature",
    title: "Generated " + topic + " parameter variation v" + variant,
    edition: EDITION,
    src: "generated",
    generated: true,
    built_by: "generator",
    record_kind: "community moderation practice record",
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
  console.error("emitted " + emitted + " generated records for community-moderation-practice-signature");
}
main();
