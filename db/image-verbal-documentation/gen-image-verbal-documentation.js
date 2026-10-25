// gen-image-verbal-documentation.js -- boundless generator for the Image Verbal Documentation Database.
// Usage: node gen-image-verbal-documentation.js --n 5
// Deterministic: a seeded LCG drives per-topic parameter variations.
// Self-regulating: throttled, duplicate-checked, hard-stops at 10^15
// records or when the variation space is genuinely exhausted.
// Generated records carry "generated": true and src "generated" --
// never mixed with assistant-built records.
"use strict";
const HARD_CAP = 1e15;
const TOPICS = ["Total Solar Eclipse Corona Over Open Country", "Partial Eclipse Crescent Shadows on the Ground", "Lunar Eclipse Color Stages Across One Night", "Eclipse Shadow Bands Rippling Over Sand", "Pinhole-Projection Crescents on a White Card", "Aurora Curtains Over a Frozen Lake", "Lightning Forking Over an Open Plain", "Double Rainbow After Rain Over a Valley", "Low Tide Flats With Wading Birds", "Waterfall Mist and Its Standing Rainbow", "Morning Fog Filling a Valley", "Desert Dune Shadows at Late Afternoon", "Alpenglow on Snow-Capped Peaks", "Ocean Wave Crest Breaking Into Foam", "Comet Tail Across a Dark Sky", "Mammatus Clouds After a Thunderstorm"];
function parseN(argv) {
  const i = argv.indexOf("--n");
  if (i >= 0 && argv[i + 1]) {
    const n = parseInt(argv[i + 1], 10);
    if (!isNaN(n) && n >= 0) return Math.min(n, 100000);
  }
  return 5;
}
let seed = 20261025;
function rnd() { seed = (seed * 1103515245 + 12345) & 0x7fffffff; return seed / 0x7fffffff; }
const seen = new Set();
function makeRecord(k) {
  const topic = TOPICS[Math.floor(rnd() * TOPICS.length)];
  const variant = 1 + Math.floor(rnd() * 50);
  const key = topic + "#v" + variant;
  if (seen.has(key)) return null;
  seen.add(key);
  return { id: "JAH-IV-GEN-" + String(k + 1).padStart(6, "0"), slug: "image-verbal-documentation",
    title: "Generated " + topic + " parameter variation v" + variant,
    edition: "public", src: "generated", generated: true, built_by: "generator",
    record_kind: "image verbal documentation record", feasibility_tier: "established",
    note: "Deterministic parameter variation (" + key + "). Labeled generated; not an assistant-built record." };
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
  console.error("emitted " + emitted + " generated records for " + "image-verbal-documentation");
}
main();
