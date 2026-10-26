// gen-camp-hero-montauk-project.js -- boundless generator for the Camp Hero and the Montauk Project Database.
// Usage: node gen-camp-hero-montauk-project.js --n 5
// Deterministic seeded variations of the 16 seed records. Self-regulating:
// throttled, duplicate-checked, hard-stops at 10^15 records or when the
// variation space is genuinely exhausted. Generated records carry
// "generated": true and src "generated" -- never mixed with built records.
"use strict";
const HARD_CAP = 1e15;
const TOPICS = ["Camp Hero Air Force Station: A Cold War Radar Post", "The AN/FPS-35 Radar Tower at Montauk", "From Station to State Park: Closure and Public Use", "Montauk Point and the Lighthouse: The Older Landmark", "The Philadelphia Experiment Legend", "Project Rainbow: The Documented Naval Program", "The Montauk Project Books: How the Story Grew", "MK Ultra: The Documented Program, Kept Separate", "Camp Hero in Popular Culture: The Stranger Things Connection", "The Montauk Monster and Local Lore", "Radar and Cold War Early Warning", "How Legends Grow: Oral History Versus Documented Record", "Visiting Camp Hero State Park Today", "Claim by Claim: Checking Montauk Stories Against Evidence", "Montauk's Fishing and Maritime History", "Preserving Cold War Sites: Heritage Interpretation"];
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
  return { id: "JAH-CHMP-GEN-" + String(k + 1).padStart(6, "0"), slug: "camp-hero-montauk-project",
    title: "Generated " + topic + " parameter variation v" + variant,
    edition: "public", src: "generated", generated: true, built_by: "generator",
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
  console.error("emitted " + emitted + " generated records for camp-hero-montauk-project");
}
main();
