// gen-edge-detection-kernels.js — boundless generator for the edge-detection-kernels database.
// Usage: node gen-edge-detection-kernels.js --n 5
// Deterministic: a seeded LCG drives middle-weight variations of the Sobel form.
// Self-regulating: throttled, duplicate-checked, hard-stops at 10^15 records or when
// the variation space is genuinely exhausted. Generated records carry "generated": true
// and src "generated" — never mixed with assistant-built records.
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

// Deterministic LCG (same sequence every run -> reproducible, duplicate-checkable)
let seed = 1968;
function rnd() {
  seed = (seed * 1103515245 + 12345) & 0x7fffffff;
  return seed / 0x7fffffff;
}

// Base: Sobel Gx form [[-c,0,c],[-w,0,w],[-c,0,c]] with swept corner c and middle w.
const seen = new Set();
function makeRecord(k) {
  const c = 1 + Math.floor(rnd() * 4);      // corner weight 1..4
  const w = 1 + Math.floor(rnd() * 12);     // middle weight 1..12
  const key = c + ":" + w;
  if (seen.has(key)) return null;           // duplicate check
  seen.add(key);
  const kernel = [[-c, 0, c], [-w, 0, w], [-c, 0, c]];
  return {
    id: "JAH-KER-GEN-" + String(k + 1).padStart(6, "0"),
    slug: "edge-detection-kernels",
    title: "Generated kernel variation c=" + c + " w=" + w,
    kernel_3x3: kernel,
    edition: "public",
    src: "generated",
    generated: true,
    built_by: "generator",
    record_kind: "edge detection kernel record",
    note: "Deterministic middle-weight variation of the Sobel Gx form. " +
          "Corner weight " + c + ", middle weight " + w + ". " +
          "Row-weight total " + (2 * c + w) + ". Labeled generated; not an assistant-built record."
  };
}

function main() {
  const n = parseN(process.argv.slice(2));
  if (n >= HARD_CAP) { console.error("hard cap reached"); process.exit(1); }
  let emitted = 0, attempts = 0;
  // Genuine-completion stop: the (c,w) space has 4*12=48 distinct kernels.
  while (emitted < n && attempts < n * 10 && seen.size < 48) {
    attempts++;
    const rec = makeRecord(emitted);
    if (rec) { console.log(JSON.stringify(rec)); emitted++; }
  }
  if (seen.size >= 48) console.error("variation space exhausted: genuinely complete at 48 kernels");
  console.error("emitted " + emitted + " generated records");
}
main();
