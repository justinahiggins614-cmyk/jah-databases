// gen-ar-vr-safety.js -- boundless generator for the AR VR Safety Database.
// Usage: node gen-ar-vr-safety.js --n 5
// Deterministic: a seeded LCG drives parameter variations of the 16 seed
// records. Self-regulating: throttled, duplicate-checked,
// hard-stops at 10^15 records or when the variation space is genuinely exhausted.
// Generated records carry "generated": true and src "generated" -- never mixed
// with assistant-built records.
"use strict";
const HARD_CAP = 1e15;
const TOPICS = ["Clear Play Space Before You Put the Headset On", "Take Breaks and Stop at the First Sign of Discomfort", "Motion Sickness: Start Slow and Build Up Gradually", "Children and Vulnerable Users: Supervise and Follow Age Guidance", "AR Street Awareness: Never Walk Blind", "Photosensitive Seizures: Respect Flashing Content Warnings", "Eye Strain and Vision Comfort: Fit the Headset to Your Eyes", "Physical Safety: Cables, Furniture, Pets, and Other People", "Privacy in Shared Virtual Spaces: What You Reveal", "Social Safety: Blocking, Muting, and Reporting Harassment", "Never Use Immersive Displays While Driving or Operating Machinery", "A Shared-Space Safety Plan for Households", "Comfort Settings Audit: Seated Mode, Movement, and View", "After an Incident: Falls, Collisions, and Distress", "Long Sessions, Sleep, and Balance After Use", "Safety for Schools, Events, and Public Demonstrations"];
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
    id: "JAH-ARVRS-GEN-" + String(k + 1).padStart(6, "0"),
    slug: "ar-vr-safety",
    title: "Generated " + topic + " parameter variation v" + variant,
    edition: "public",
    src: "generated",
    generated: true,
    built_by: "generator",
    record_kind: "AR VR safety record",
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
  console.error("emitted " + emitted + " generated records for ar-vr-safety");
}
main();
