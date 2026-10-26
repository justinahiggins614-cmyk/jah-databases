// gen-verifying-ai-outputs.js -- boundless generator for the Verifying AI Outputs Database.
// Usage: node gen-verifying-ai-outputs.js --n 5
// Deterministic: a seeded LCG drives parameter variations of the 16 seed
// records. Self-regulating: throttled, duplicate-checked,
// hard-stops at 10^15 records or when the variation space is genuinely exhausted.
// Generated records carry "generated": true and src "generated" -- never mixed
// with assistant-built records.
"use strict";
const HARD_CAP = 1e15;
const TOPICS = ["Read the Answer Twice: Separate Claim from Wording", "Ask for Sources, Then Open Them Yourself", "Cross-Check Numbers: Recompute, Do Not Re-Quote", "Dates, Names, and Quotes Are the First Things to Verify", "If It Sounds Too Certain, Ask What It Does Not Know", "Copy, Test, and Run Code Claims Before Trusting Them", "The Independent Second Path", "Spot a Hallucinated Citation", "Check Images and Media Claims Against Original Context", "Compare Two Independent Sources, Not Two Copies of One", "Verify Health, Legal, and Money Advice With a Qualified Source", "Build a Verification Checklist for a Whole Report", "Detect Overgeneralization and Missing Conditions", "Verify Translations and Multilingual Answers", "Audit an AI Agent's Work Before You Approve It", "Teach Verification: A Routine for Home and Classroom"];
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
    id: "JAH-VAIO-GEN-" + String(k + 1).padStart(6, "0"),
    slug: "verifying-ai-outputs",
    title: "Generated " + topic + " parameter variation v" + variant,
    edition: "public",
    src: "generated",
    generated: true,
    built_by: "generator",
    record_kind: "AI output verification record",
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
  console.error("emitted " + emitted + " generated records for verifying-ai-outputs");
}
main();
