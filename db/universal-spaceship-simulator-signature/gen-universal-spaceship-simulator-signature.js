// gen-universal-spaceship-simulator-signature.js -- WORKING universal spaceship simulator for the Universal Spaceship Simulator Signature Database.
// Usage (simulator):
//   node gen-universal-spaceship-simulator-signature.js --destination Mars --speed-frac 0.1 --scale planet
//   node gen-universal-spaceship-simulator-signature.js --destination "Alpha Centauri" --speed-frac 0.9 --scale mix --advance-days 100
//   node gen-universal-spaceship-simulator-signature.js --destination Moon --speed-frac 0.01 --pause
// Usage (boundless generator): node gen-universal-spaceship-simulator-signature.js --n 5
// Standard math throughout: c = 299792458 m/s is the absolute limit.
// No faster-than-light travel is offered as working physics; any
// speculative layer is labeled Signature fiction. Deterministic, seeded,
// hard-stops at 10^15 generated records or when the variation space ends.
// Generated records carry "generated": true and src "generated".
"use strict";
const C = 299792458;
const HARD_CAP = 1e15;
const DEST = {"Signature Harbor Station": {"km": 420, "view": "Signature Harbor Station hangs in low Earth orbit as a ring of warm-lit modules: docking arms, a green growing bay glowing through its windows, and Earth turning blue and white below, the station's own lights steady against the black."}, "Signature Moon Base Meridian": {"km": 384400, "view": "Signature Moon Base Meridian sits in a grey crater plain as a cluster of low domes and buried halls: white surface suits and a small rover near an airlock, Earth small and blue overhead, and long shadows from a low Sun across the regolith."}, "Signature Mercury Watch": {"km": 91000000, "view": "Signature Mercury Watch is a shielded outpost on the night side of Mercury: dark panels facing a scorched plain, a bright Sun just below the horizon line, and instruments aimed at the terminator where day and night meet in a line of long shadows."}, "Signature Venus Cloud Deck": {"km": 41000000, "view": "Signature Venus Cloud Deck floats in the planet's upper air as a bright balloon-borne platform: cream cloud all around, the Sun a diffuse glow through the haze, and below, unseen, the hot surface that no window of the deck will ever open onto."}, "Signature Mars Redway": {"km": 78000000, "view": "Signature Mars Redway is a route station above rust-red plains: a landing field of dark pads, habitat cylinders half-buried against dust, and on the horizon the pink haze of a dust storm moving slowly across the volcanic plain."}, "Signature Jovian Relay": {"km": 628000000, "view": "Signature Jovian Relay holds station far from Jupiter's radiation belts: the banded giant fills half the viewscreen, its moons as bright points, and the relay's dish farm turned toward Earth, a thin thread of signal across the dark."}, "Signature Europa Ice Lab": {"km": 628000000, "view": "Signature Europa Ice Lab rests on pale cracked ice: a low heated shelter, a drill rig, and a sampling arm over a dark line in the ice, with Jupiter huge in the sky and the ice glowing faintly blue in the cracks."}, "Signature Ring Port": {"km": 1275000000, "view": "Signature Ring Port rides just outside Saturn's rings: the ring plane cuts the viewscreen as a brilliant line of gold and grey, Saturn's globe behind it, and small ice-tug craft moving between the port and the ring's outer edge."}, "Signature Titan Haze Station": {"km": 1275000000, "view": "Signature Titan Haze Station floats in orange haze: a warm-lit gondola platform with rain gauges for methane drizzle, the surface below hidden, and only the faintest darker patches in the haze hinting at lakes far below."}, "Signature Uranus Polar Post": {"km": 2720000000, "view": "Signature Uranus Polar Post keeps station over the planet's pale cyan pole: a quiet, nearly featureless globe below, thin rings edge-on, and a Sun so distant that the station's own lamps are the brightest local light."}, "Signature Neptune Deep Post": {"km": 4350000000, "view": "Signature Neptune Deep Post rides above deep blue cloud: white streak clouds, a dark storm oval, and a Sun reduced to a brilliant star, the post's instruments measuring winds that outrun any storm on Earth."}, "Signature Pluto Farlight": {"km": 5200000000, "view": "Signature Pluto Farlight is a small station above a mottled world: the bright heart-shaped plain below, Charon nearby, and a sky so dark and a Sun so small that the station's lights define the only warm color for millions of kilometers."}, "Signature Centauri Approach": {"km": 41300000000000, "view": "Signature Centauri Approach is a notional waypoint between two suns: a yellow star and an orange companion blazing together, a red dwarf point far off, and the long dark between the stars made visible only by the Milky Way's band."}, "Signature Sirius Beacon": {"km": 81400000000000, "view": "Signature Sirius Beacon is a marker beacon near the brightest star: fierce white-blue light, a faint white dwarf companion, and the beacon's own steady pulse, a human-made rhythm laid against a star's blaze."}, "Signature Orion Nursery": {"km": 1344000000000000, "view": "Signature Orion Nursery is a survey point inside a glowing nebula: green and pink gas folds, dark dust lanes, and four bright young stars at the center, their light still carving the cloud that made them."}, "Signature Core Crossing": {"km": 260000000000000000, "view": "Signature Core Crossing is a far waypoint toward the galactic center: a dense star field, dark dust lanes, and at the middle a point of gravity with stars whipping around it, the whole region glowing with millions of suns."}};
const SCALES = ["universe","galaxy","star system","planet","region","city","building","room","object","cell","molecule","atom"];
function arg(name, def) { const i = process.argv.indexOf(name); return i >= 0 && process.argv[i+1] ? process.argv[i+1] : def; }
function has(name) { return process.argv.indexOf(name) >= 0; }
function fmt(sec) {
  if (sec < 1) return sec.toFixed(3) + " seconds";
  if (sec < 60) return sec.toFixed(2) + " seconds";
  if (sec < 3600) return (sec/60).toFixed(2) + " minutes";
  if (sec < 86400) return (sec/3600).toFixed(2) + " hours";
  if (sec < 31557600) return (sec/86400).toFixed(2) + " days";
  return (sec/31557600).toFixed(2) + " years";
}
function gamma(f) { return 1 / Math.sqrt(1 - f*f); }
function viewFor(dest, scale) {
  const base = DEST[dest].view;
  if (scale === "mix") return "UNIVERSAL MIX: " + SCALES.map(function(s){ return "[" + s + "] " + base; }).join(" ");
  return "[" + scale + " view] " + base;
}
function simulate() {
  let dest = arg("--destination", "Mars");
  if (!DEST[dest]) {
    const low = dest.toLowerCase();
    const match = Object.keys(DEST).filter(function(k){ return k.toLowerCase().indexOf(low) >= 0 || low.indexOf(k.toLowerCase()) >= 0; });
    if (match.length === 1) dest = match[0];
    else { console.error("Unknown destination. Known: " + Object.keys(DEST).join(", ")); process.exit(1); }
  }
  let frac = parseFloat(arg("--speed-frac", "0.1"));
  if (!(frac > 0) || frac >= 1) { console.error("Speed fraction must satisfy 0 < frac < 1. Light speed c is the limit; no FTL."); process.exit(1); }
  const scale = arg("--scale", "planet");
  if (scale !== "mix" && SCALES.indexOf(scale) < 0) { console.error("Unknown scale. Scales: " + SCALES.join(", ") + ", mix"); process.exit(1); }
  const distM = DEST[dest].km * 1000;
  const lightS = distM / C;
  const travelS = distM / (frac * C);
  const g = gamma(frac);
  console.log("=== VERBAL VIEWSCREEN ===");
  console.log(viewFor(dest, scale));
  console.log("Destination: " + dest + " (" + DEST[dest].km.toLocaleString("en-US") + " km)");
  console.log("Speed: " + frac + "c (" + (frac*C).toLocaleString("en-US") + " m/s); c = 299,792,458 m/s is the limit");
  console.log("One-way light-time delay: " + fmt(lightS));
  console.log("Travel time (stay-at-home clocks): " + fmt(travelS));
  console.log("Travel time (traveler clocks, time dilation): " + fmt(travelS / g) + " (gamma = " + g.toFixed(4) + ")");
  if (has("--pause")) { console.log("TIME CONTROL: PAUSED. The ship holds position; no time advances until resumed."); return; }
  const adv = parseFloat(arg("--advance-days", "0"));
  if (has("--step")) console.log("TIME CONTROL: STEP +1 day. Elapsed: 1 day of " + fmt(travelS) + " total; progress " + (86400/travelS*100).toFixed(4) + "%.");
  else if (adv > 0) {
    const el = adv * 86400;
    if (el >= travelS) console.log("TIME CONTROL: ADVANCE " + adv + " days. ARRIVED at " + dest + ".");
    else console.log("TIME CONTROL: ADVANCE " + adv + " days. En route: " + (el/travelS*100).toFixed(2) + "% of the way to " + dest + "; " + fmt(travelS - el) + " remaining (stay-at-home clocks).");
  } else console.log("TIME CONTROL: ready. Use --advance-days N, --step, or --pause.");
  console.log("FTL: not offered as working physics. Any speculative FTL layer is labeled Signature fiction.");
}
const TOPICS = ["Destination Guide","Scale Study","Route Note","Time Control Note","Viewscreen Study"];
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
    console.log(JSON.stringify({ id: "JAH-US-GEN-" + String(emitted + 1).padStart(6, "0"), slug: "universal-spaceship-simulator-signature", title: "Generated " + topic + " parameter variation v" + variant, edition: "signature", src: "generated", generated: true, built_by: "generator", record_kind: "spaceship simulator record", feasibility_tier: "signature", note: "Deterministic parameter variation (" + key + "). Labeled generated; not an assistant-built record." }));
    emitted++;
  }
  console.error("emitted " + emitted + " generated records for " + "universal-spaceship-simulator-signature");
}
if (has("--destination") || has("--pause") || has("--step") || has("--advance-days")) simulate();
else if (has("--n")) generate();
else simulate();
