// gen-technology-signature.js -- boundless generator for the Technology Signature Database.
// Usage: node gen-technology-signature.js --n 5
// Deterministic: a seeded LCG drives design-parameter variations of Signature concepts.
// Self-regulating: throttled, duplicate-checked, hard-stops at 10^15 records or when
// the variation space is genuinely exhausted. Generated records carry "generated": true
// and src "generated" -- never mixed with assistant-built records.
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

let seed = 20261023;
function rnd() {
  seed = (seed * 1103515245 + 12345) & 0x7fffffff;
  return seed / 0x7fffffff;
}

const BASES = [
  ["Triplet Gate", "stacked-gate transistor", "subthreshold swing"],
  ["Layer Weave", "redundant-mesh interconnect", "via defect tolerance"],
  ["Mesh Ledger Web", "content-addressed web", "mirror count"],
  ["Ledger Table", "append-only versioned table", "retention window"],
  ["Split-Key Handshake", "threshold key split", "share quorum"],
  ["Tile Renderer", "tile-based graphics", "tile size"],
  ["Twin-Cylinder Reclaimer", "compound steam engine", "expansion ratio"],
  ["Sun Sandwich", "tandem photovoltaic", "top-cell bandgap"],
  ["Salt Cell", "sodium-ion battery", "cathode chemistry"],
  ["Walk-Away Core", "passive-safety reactor", "feedback coefficient"],
  ["Gust Rider", "self-pitching turbine", "pitch linkage ratio"],
  ["River Runner", "modular run-of-river hydro", "module rating"]
];

const seen = new Set();
function makeRecord(k) {
  const b = BASES[Math.floor(rnd() * BASES.length)];
  const v = 1 + Math.floor(rnd() * 999);
  const key = b[1] + "#" + v;
  if (seen.has(key)) return null;
  seen.add(key);
  return {
    id: "JAH-TECHS-GEN-" + String(k + 1).padStart(6, "0"),
    slug: "technology-signature",
    title: "Generated Signature variation: " + b[0] + " (" + b[2] + " variant " + v + ")",
    edition: "signature",
    src: "generated",
    generated: true,
    built_by: "generator",
    record_kind: "technology record",
    feasibility_tier: "signature-concept",
    mirrors: b[1],
    note: "Deterministic variation (" + key + ") of the Signature " + b[0] +
          " design family. Labeled generated; not an assistant-built record."
  };
}

function main() {
  const n = parseN(process.argv.slice(2));
  if (n >= HARD_CAP) { console.error("hard cap reached"); process.exit(1); }
  let emitted = 0, attempts = 0;
  while (emitted < n && attempts < n * 20 && seen.size < BASES.length * 999) {
    attempts++;
    const rec = makeRecord(emitted);
    if (rec) { console.log(JSON.stringify(rec)); emitted++; }
  }
  console.error("emitted " + emitted + " generated records for technology-signature");
}
main();
