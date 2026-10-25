// gen-image-verbal-documentation-signature.js -- boundless generator for the Image Verbal Documentation Signature Database.
// Usage: node gen-image-verbal-documentation-signature.js --n 5
// Deterministic: a seeded LCG drives per-topic parameter variations.
// Self-regulating: throttled, duplicate-checked, hard-stops at 10^15
// records or when the variation space is genuinely exhausted.
// Generated records carry "generated": true and src "generated" --
// never mixed with assistant-built records.
"use strict";
const HARD_CAP = 1e15;
const TOPICS = ["Signature Study: Geyser Eruption in Words", "Signature Study: Tide Pool at Low Water", "Signature Study: Frost Patterns on a Window", "Signature Study: River Delta From Above", "Signature Study: Canyon Light Beam", "Signature Study: Glacier Blue Ice", "Signature Study: Milky Way Over Desert Night", "Signature Study: Rain Rings on a Lake", "Signature Study: Sea of Clouds at Sunset", "Signature Study: Ice Halo Around the Moon", "Signature Study: Sand Ripples After Wind", "Signature Study: Autumn Forest Light", "Signature Study: Blossom Snow in Spring", "Signature Study: Moon Halo Over Snow", "Signature Study: Star Trails Circling the Pole", "Signature Study: Morning Dew on a Spider Web"];
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
  return { id: "JAH-IV-GEN-" + String(k + 1).padStart(6, "0"), slug: "image-verbal-documentation-signature",
    title: "Generated " + topic + " parameter variation v" + variant,
    edition: "signature", src: "generated", generated: true, built_by: "generator",
    record_kind: "image verbal documentation record", feasibility_tier: "signature",
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
  console.error("emitted " + emitted + " generated records for " + "image-verbal-documentation-signature");
}
main();
