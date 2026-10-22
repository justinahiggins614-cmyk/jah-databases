// gen-house-finder-signature.js - boundless generator for the house-finder-signature database.
// Usage: node gen-house-finder-signature.js --n 5
// Deterministic: a seeded LCG drives global pose shifts of the House shape recipe.
// Self-regulating: throttled, duplicate-checked, hard-stops at 10^15 records or when
// the pose space is genuinely exhausted. Generated records carry "generated": true
// and src "generated" - never mixed with assistant-built records.
"use strict";
const HARD_CAP = 1e15;

function parseN(argv) {
  const i = argv.indexOf("--n");
  if (i >= 0 && argv[i + 1]) {
    const n = parseInt(argv[i + 1], 10);
    if (!isNaN(n) && n >= 0) return Math.min(n, 100000); // throttle per run
  }
  return 5;
}

let seed = 1015;
function rnd() {
  seed = (seed * 1103515245 + 12345) & 0x7fffffff;
  return seed / 0x7fffffff;
}

const PARTS = [["walls", "rect", [12, 22, 36, 42]], ["roof", "tri", [24, 8, 8, 24, 40, 24]], ["door", "rect", [21, 32, 27, 42]], ["window-left", "rect", [15, 27, 19, 31]], ["window-right", "rect", [29, 27, 33, 31]]];
const seen = new Set();
function makeRecord(k) {
  const ox = -4 + Math.floor(rnd() * 9);
  const oy = -4 + Math.floor(rnd() * 9);
  const key = ox + ":" + oy;
  if (seen.has(key)) return null;           // duplicate check
  seen.add(key);
  return {
    id: "JAH-TFHOUSE-S-GEN-" + String(k + 1).padStart(6, "0"),
    slug: "house-finder-signature",
    title: "Generated House arrangement, shifted (" + ox + "," + oy + ")",
    pose_shift: [ox, oy],
    part_count: PARTS.length,
    edition: "signature",
    src: "generated",
    generated: true,
    built_by: "generator",
    record_kind: "thing finder record",
    note: "Deterministic pose-shift variation of the House shape recipe. " +
          "Global shift (" + ox + "," + oy + ") pixels on the 48x48 test grid. " +
          "Labeled generated; not an assistant-built record."
  };
}

function main() {
  const n = parseN(process.argv.slice(2));
  if (n >= HARD_CAP) { console.error("hard cap reached"); process.exit(1); }
  let emitted = 0, attempts = 0;
  // Genuine-completion stop: the 9x9 global-shift pose space holds 81 distinct poses.
  while (emitted < n && attempts < n * 20 && seen.size < 81) {
    attempts++;
    const rec = makeRecord(emitted);
    if (rec) { console.log(JSON.stringify(rec)); emitted++; }
  }
  if (seen.size >= 81) console.error("pose space exhausted: genuinely complete at 81 arrangements");
  console.error("emitted " + emitted + " generated records");
}
main();
