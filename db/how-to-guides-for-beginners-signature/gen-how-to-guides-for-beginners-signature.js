// gen-how-to-guides-for-beginners-signature.js -- boundless generator for the How-To Guides for Beginners Signature Database.
// Usage: node gen-how-to-guides-for-beginners-signature.js --n 5
// Deterministic: a seeded LCG drives parameter variations of the 16 seed
// records. Self-regulating: throttled, duplicate-checked,
// hard-stops at 10^15 records or when the variation space is genuinely exhausted.
// Generated records carry "generated": true and src "generated" -- never mixed
// with assistant-built records.
"use strict";
const HARD_CAP = 1e15;
const TOPICS = ["Signature Egg Method: Boil and Peel Clean", "Signature Jar Release: Open a Stuck Lid", "Signature Sheet Fold: The Flat Fitted Sheet", "Signature Residue Lift: Remove Sticker Glue", "Signature Envelope Address: Written Right", "Signature Avocado Ripening: Bag and Wait", "Signature Lens Wash: Glasses Without Scratches", "Signature Picture Hang: Level and Secure", "Signature Hinge Quiet: Squeak Removal", "Signature Screw Rescue: The Stripped Head", "Signature Microwave Steam-Clean", "Signature Knife Edge: Whetstone Sharpening", "Signature Watch Cell: Battery Swap", "Signature Fire Response: PASS by Heart", "Signature Paper Flight: Fold and Tune", "Signature Kerb Park: Parallel, First Try"];
function parseN(argv) {
  const i = argv.indexOf("--n");
  if (i >= 0 && argv[i + 1]) {
    const n = parseInt(argv[i + 1], 10);
    if (!isNaN(n) && n >= 0) return Math.min(n, 100000);
  }
  return 5;
}
let seed = 20261026;
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
    id: "JAH-HTGS-GEN-" + String(k + 1).padStart(6, "0"),
    slug: "how-to-guides-for-beginners-signature",
    title: "Generated " + topic + " parameter variation v" + variant,
    edition: "Signature",
    src: "generated",
    generated: true,
    built_by: "generator",
    record_kind: "how-to guide record",
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
  console.error("emitted " + emitted + " generated records for how-to-guides-for-beginners-signature");
}
main();
