#!/usr/bin/env node
// gen-cat-detection-signature.js -- boundless generator for the Cat Detection Signature Database.
// Self-regulating: duplicate-checked, hard-capped at 10^15, throttled.
// Generated output is labeled "generated" and never mixed with assistant-built records.
// Usage: node gen-cat-detection-signature.js --n 5
const CAP = 10n ** 15n;
const args = process.argv.slice(2);
let n = 5;
const ni = args.indexOf("--n");
if (ni >= 0 && args[ni + 1]) n = Math.max(0, parseInt(args[ni + 1], 10) || 0);
if (BigInt(n) > CAP) { console.error("hard cap 10^15 exceeded"); process.exit(1); }
const throttleMs = (() => { const i = args.indexOf("--throttle-ms"); return i >= 0 ? Math.max(0, parseInt(args[i+1],10)||0) : 0; })();
function mulberry32(a) { return function() { a |= 0; a = (a + 0x6D2B79F5) | 0; let t = Math.imul(a ^ (a >>> 15), 1 | a); t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t; return ((t ^ (t >>> 14)) >>> 0) / 4294967296; }; }
const rand = mulberry32(1001);
const PROBES = ["JAH ear-junction kernel", "JAH eye-pair probe", "JAH whisker-line vote", "JAH contour-closure gate", "JAH cascade composition"];
const TARGETS = ["ear tip junction", "eye pair symmetry", "muzzle contour", "tail arc"];
function pick(a) { return a[Math.floor(rand() * a.length)]; }
function kernel9() { const k = []; for (let i = 0; i < 9; i++) k.push(Math.floor(rand() * 7) - 3); return [k.slice(0,3), k.slice(3,6), k.slice(6,9)]; }
const seen = new Set();
let produced = 0, attempts = 0;
function sleep(ms) { return new Promise(r => setTimeout(r, ms)); }
(async () => {
  while (produced < n && attempts < n * 50 + 100) {
    attempts++;
    const probe = pick(PROBES), target = pick(TARGETS);
    const key = probe + "|" + target + "|" + produced;
    if (seen.has(probe + "|" + target)) continue;
    seen.add(probe + "|" + target);
    const rec = {
      id: "JAH-DET-GEN-" + String(produced + 1).padStart(6, "0"),
      slug: "cat-detection-signature",
      title: "Generated study: " + probe + " on " + target,
      edition: "signature",
      origin: "generated",
      generated: true,
      probe: probe,
      target: target,
      kernel_3x3: kernel9(),
      note: "Boundless-generator output for the Cat Detection Signature Database: a " + probe + " applied to " + target +
            ", labeled generated per the output-labeling rule; verify before treating as established."
    };
    console.log(JSON.stringify(rec));
    produced++;
    if (throttleMs > 0) await sleep(throttleMs);
  }
  if (produced < n) console.error("generator stopped early: ideas exhausted at " + produced + " (marked, not padded)");
})();
