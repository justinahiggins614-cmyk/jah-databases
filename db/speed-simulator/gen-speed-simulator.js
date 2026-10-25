// gen-speed-simulator.js -- WORKING speed simulator for the Speed Simulator Database.
// Usage:
//   node gen-speed-simulator.js --distance-km 384400
//   node gen-speed-simulator.js --distance-km 149600000 --reference "Passenger Jet"
//   node gen-speed-simulator.js --n 5   (boundless generator mode)
// Standard math only: c = 299,792,458 m/s is the absolute limit.
// Near-c rows show time dilation per special relativity, gamma = 1/sqrt(1-v^2/c^2).
// Deterministic, seeded, hard-stops at 10^15 generated records.
// Generated records carry "generated": true and src "generated".
"use strict";
const C = 299792458;
const HARD_CAP = 1e15;
const REFS = {"Walking": 1.4, "Bicycle": 5.5, "City Car": 13.9, "Highway Car": 30.0, "High-Speed Train": 83.0, "Passenger Jet": 250.0, "Supersonic Jet": 600.0, "Orbital Rocket": 7800.0, "Earth Escape Rocket": 11200.0, "Voyager Probe": 17000.0, "Light in Vacuum": 299792458.0};
function arg(name, def) { const i = process.argv.indexOf(name); return i >= 0 && process.argv[i+1] ? process.argv[i+1] : def; }
function has(name) { return process.argv.indexOf(name) >= 0; }
function fmt(sec) {
  if (sec < 0.001) return (sec*1e6).toFixed(3) + " microseconds";
  if (sec < 1) return (sec*1000).toFixed(3) + " milliseconds";
  if (sec < 60) return sec.toFixed(2) + " seconds";
  if (sec < 3600) return (sec/60).toFixed(2) + " minutes";
  if (sec < 86400) return (sec/3600).toFixed(2) + " hours";
  if (sec < 31557600) return (sec/86400).toFixed(2) + " days";
  return (sec/31557600).toFixed(2) + " years";
}
function gamma(f) { return 1 / Math.sqrt(1 - f*f); }
function table(distKm) {
  const distM = distKm * 1000;
  console.log("=== TRAVEL-TIME TABLE for " + distKm.toLocaleString("en-US") + " km ===");
  console.log("Reference | Speed (m/s) | Travel time | Notes");
  Object.keys(REFS).forEach(function(name) {
    const v = REFS[name];
    console.log(name + " | " + v.toLocaleString("en-US") + " | " + fmt(distM / v) + " | " + (v >= C ? "light speed, the limit" : "far below c; dilation negligible"));
  });
  console.log("--- Near light speed (special relativity) ---");
  [0.5, 0.9, 0.99].forEach(function(f) {
    console.log(f + "c | " + (f*C).toLocaleString("en-US") + " | stay-at-home " + fmt(distM/(f*C)) + " | traveler " + fmt(distM/(f*C)/gamma(f)) + " (gamma = " + gamma(f).toFixed(4) + ")");
  });
  console.log("Light (c) | 299,792,458 | " + fmt(distM / C) + " | light-time delay; traveler proper time 0; c is the absolute limit, never exceeded");
  const chosen = arg("--reference", "");
  if (chosen) {
    if (!REFS[chosen]) { console.error("Unknown reference. Known: " + Object.keys(REFS).join(", ")); process.exit(1); }
    console.log("CHOSEN REFERENCE: " + chosen + " -> " + fmt(distM / REFS[chosen]) + " for " + distKm.toLocaleString("en-US") + " km.");
  }
  console.log("Change --distance-km or --reference and the table rebuilds. Extrapolate: time scales linearly with distance for every row.");
}
const TOPICS = ["Reference Guide","Distance Study","Table Note","Dilation Study"];
let seed = 20261025;
function rnd() { seed = (seed * 1103515245 + 12345) & 0x7fffffff; return seed / 0x7fffffff; }
function generate() {
  const i = process.argv.indexOf("--n"); let n = 5;
  if (i >= 0 && process.argv[i+1]) { const v = parseInt(process.argv[i+1], 10); if (!isNaN(v)) n = Math.min(v, 100000); }
  const seen = new Set(); let emitted = 0, attempts = 0;
  while (emitted < n && attempts < n * 20) {
    attempts++;
    const topic = TOPICS[Math.floor(rnd() * TOPICS.length)];
    const variant = 1 + Math.floor(rnd() * 50); const key = topic + "#v" + variant;
    if (seen.has(key)) continue; seen.add(key);
    console.log(JSON.stringify({ id: "JAH-SP-GEN-" + String(emitted + 1).padStart(6, "0"), slug: "speed-simulator", title: "Generated " + topic + " parameter variation v" + variant, edition: "public", src: "generated", generated: true, built_by: "generator", record_kind: "speed simulator record", feasibility_tier: "established", note: "Deterministic parameter variation (" + key + "). Labeled generated; not an assistant-built record." }));
    emitted++;
  }
  console.error("emitted " + emitted + " generated records for " + "speed-simulator");
}
if (has("--distance-km")) table(parseFloat(arg("--distance-km", "384400")));
else if (has("--n")) generate();
else table(384400);
