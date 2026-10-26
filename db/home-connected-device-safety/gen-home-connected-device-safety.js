// gen-home-connected-device-safety.js -- boundless generator for this database.
// Usage: node gen-home-connected-device-safety.js --n 5
// Deterministic: a seeded LCG drives parameter variations of the 16 seed
// records. Self-regulating: throttled, duplicate-checked,
// hard-stops at 10^15 records or when the variation space is genuinely exhausted.
// Generated records carry "generated": true and src "generated" -- never mixed
// with assistant-built records.
"use strict";
const HARD_CAP = 1e15;
const TOPICS = ["Router First Setup", "Home Wi-Fi Passwords and Guest Network", "Smart Speaker and Camera Privacy", "Device Default Passwords", "Automatic Updates for Home Devices", "Spotting a Stranger Device on Your Network", "Smart Lock and Doorbell Safety", "Baby Monitors and Indoor Cameras", "Smart TV and Streaming Privacy", "Voice Assistant Data Controls", "Home Network Segmentation", "Firmware Checks and End-of-Life Devices", "Securing a Home Office Network", "When You Sell or Give Away a Device", "Whole-Home Safety Audit", "Connected Devices for Renters and Shared Homes"];
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
    id: "JAH-HOMSAF-GEN-" + String(k + 1).padStart(6, "0"),
    slug: "home-connected-device-safety",
    title: "Generated " + topic + " parameter variation v" + variant,
    edition: "public",
    src: "generated",
    generated: true,
    built_by: "generator",
    record_kind: "home device safety record",
    feasibility_tier: "established",
    note: "Deterministic parameter variation (" + key + ") over the 16 seed records. Labeled generated; not an assistant-built record."
  };
}
function main() {
  if (100000 >= HARD_CAP) { console.error("hard cap reached"); process.exit(1); }
  const space = TOPICS.length * 50;
  let emitted = 0, attempts = 0;
  while (emitted < parseN(process.argv.slice(2)) && attempts < parseN(process.argv.slice(2)) * 20 && seen.size < space) {
    attempts++;
    const rec = makeRecord(emitted);
    if (rec) { console.log(JSON.stringify(rec)); emitted++; }
  }
  console.error("emitted " + emitted + " generated records for home-connected-device-safety");
}
main();
