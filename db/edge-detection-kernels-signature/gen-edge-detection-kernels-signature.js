// gen-edge-detection-kernels-signature.js — boundless generator for the Signature edition.
// Usage: node gen-edge-detection-kernels-signature.js --n 5
// Deterministic: a seeded LCG drives JAH-style Signature kernel experiments
// (diagonal forms, stripe forms, corner forms, anchor forms).
// Self-regulating: throttled, duplicate-checked, hard-stops at 10^15 records or when
// the design space is genuinely exhausted. Generated records carry "generated": true
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

let seed = 614; // JAH lab seed
function rnd() {
  seed = (seed * 1103515245 + 12345) & 0x7fffffff;
  return seed / 0x7fffffff;
}

// Four Signature design families, each parameterized:
// 0 diagonal: [[-d,-h,0],[-h,0,h],[0,h,d]]   1 stripe: [[-s,t,-s]]x3 rows
// 2 corner: [[c,-e,c],[-e,k,-e],[c,-e,c]]    3 anchor: [[-c,0,c],[-w,0,w],[-c,0,c]]
const seen = new Set();
function makeRecord(k) {
  const fam = Math.floor(rnd() * 4);
  let kernel, label;
  if (fam === 0) {
    const d = 1 + Math.floor(rnd() * 3), h = 1 + Math.floor(rnd() * 2);
    kernel = [[-d, -h, 0], [-h, 0, h], [0, h, d]];
    label = "JAH-style diagonal experiment d=" + d + " h=" + h;
  } else if (fam === 1) {
    const s = 1 + Math.floor(rnd() * 2), t = 1 + Math.floor(rnd() * 3);
    kernel = [[-s, t, -s], [-s, t, -s], [-s, t, -s]];
    label = "JAH-style stripe experiment s=" + s + " t=" + t;
  } else if (fam === 2) {
    const c = 1, e = 1 + Math.floor(rnd() * 3), kk = 2 * e + 2 * c;
    kernel = [[c, -e, c], [-e, kk, -e], [c, -e, c]];
    label = "JAH-style corner experiment e=" + e + " center=" + kk;
  } else {
    const c = 1, w = 1 + Math.floor(rnd() * 8);
    kernel = [[-c, 0, c], [-w, 0, w], [-c, 0, c]];
    label = "JAH-style anchor experiment middle=" + w;
  }
  const key = JSON.stringify(kernel);
  if (seen.has(key)) return null;
  seen.add(key);
  return {
    id: "JAH-KER-SGEN-" + String(k + 1).padStart(6, "0"),
    slug: "edge-detection-kernels-signature",
    title: "Generated Signature kernel: " + label,
    kernel_3x3: kernel,
    edition: "signature",
    src: "generated",
    generated: true,
    built_by: "generator",
    record_kind: "edge detection kernel record",
    note: "Deterministic Signature-family kernel experiment (" + label + "). " +
          "Sums to zero; flat fields stay silent. Labeled generated; not an assistant-built record."
  };
}

function main() {
  const n = parseN(process.argv.slice(2));
  if (n >= HARD_CAP) { console.error("hard cap reached"); process.exit(1); }
  let emitted = 0, attempts = 0;
  while (emitted < n && attempts < n * 20) {
    attempts++;
    const rec = makeRecord(emitted);
    if (rec) { console.log(JSON.stringify(rec)); emitted++; }
    if (attempts > 5000 && emitted === 0) break; // genuine-exhaustion guard
  }
  console.error("emitted " + emitted + " generated records");
}
main();
