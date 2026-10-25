// gen-design-briefs-client-requirements-signature.js -- boundless generator for the Design Briefs and Client Requirements Database (Signature Edition).
// Usage: node gen-design-briefs-client-requirements-signature.js --n 5
// Deterministic: a seeded LCG drives per-topic parameter variations.
// Self-regulating: throttled, duplicate-checked, hard-stops at 10^15
// records or when the variation space is genuinely exhausted.
// Generated records carry "generated": true and src "generated" --
// never mixed with assistant-built records.
"use strict";
const HARD_CAP = 1e15;
const TOPICS = ["Client Needs Interview", "Budget Framework", "Room List and Schedule", "Style and Character Preferences", "Site Constraints Register", "Project Goals and Priorities", "Approval Gates", "Decision History Log", "Brief Change Control", "Brief to Design Handover"];
function parseN(argv) {
  const i = argv.indexOf("--n");
  if (i >= 0 && argv[i + 1]) {
    const n = parseInt(argv[i + 1], 10);
    if (!isNaN(n) && n >= 0) return Math.min(n, 100000);
  }
  return 5;
}
let seed = 20261035;
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
    id: "JAH-AR10-S-GEN-" + String(k + 1).padStart(6, "0"),
    slug: "design-briefs-client-requirements-signature",
    title: "Generated " + topic + " parameter variation v" + variant,
    edition: "signature",
    src: "generated",
    generated: true,
    built_by: "generator",
    record_kind: "design brief record",
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
  console.error("emitted " + emitted + " generated records for design-briefs-client-requirements-signature");
}
main();
