// gen-universal-spaceship-simulator.js -- WORKING universal spaceship simulator for the Universal Spaceship Simulator Database.
// Usage (simulator):
//   node gen-universal-spaceship-simulator.js --destination Mars --speed-frac 0.1 --scale planet
//   node gen-universal-spaceship-simulator.js --destination "Alpha Centauri" --speed-frac 0.9 --scale mix --advance-days 100
//   node gen-universal-spaceship-simulator.js --destination Moon --speed-frac 0.01 --pause
// Usage (boundless generator): node gen-universal-spaceship-simulator.js --n 5
// Standard math throughout: c = 299792458 m/s is the absolute limit.
// No faster-than-light travel is offered as working physics; any
// speculative layer is labeled Signature fiction. Deterministic, seeded,
// hard-stops at 10^15 generated records or when the variation space ends.
// Generated records carry "generated": true and src "generated".
"use strict";
const C = 299792458;
const HARD_CAP = 1e15;
const DEST = {"Earth Orbit": {"km": 420, "view": "Low orbit above Earth: a blue marble fills the lower viewscreen, white cloud swirls over ocean and continent, the black of space above cut by a thin glowing blue line of atmosphere, and the Sun, when it rises over the limb, flares hard and white with no air to soften it."}, "The Moon": {"km": 384400, "view": "The Moon fills the viewscreen as a grey, cratered world: bright rayed craters near the center, dark smooth maria like old seas, mountains casting long shadows at the terminator, and Earth hanging small and blue in the black sky above the airless ground."}, "Mercury": {"km": 91000000, "view": "Mercury is a scorched, cratered ball close to the Sun: grey-brown plains pocked with craters, long cliff scarps crossing the surface, and a Sun that looks nearly three times wider than from Earth, glaring over a landscape with almost no atmosphere to hold heat or soften light."}, "Venus": {"km": 41000000, "view": "Venus hides under unbroken cream-yellow cloud: the viewscreen shows no surface at all, only swirling cloud tops in pale gold, while below them, known from radar and not from sight, lies a hot, high-pressure world of volcanic plains that no window will ever show directly."}, "Mars": {"km": 78000000, "view": "Mars is a rust-red world of contrasts: dark volcanic plains, the pale pink of dust storms at the limb, white polar caps, and the great canyon Valles Marineris as a dark scar across the disk, with two tiny moons too small to show as more than points."}, "Jupiter": {"km": 628000000, "view": "Jupiter dominates the viewscreen as a banded giant: cream, rust, and brown belts streaming around the planet, the Great Red Spot as a pale oval storm larger than Earth, and the four bright Galilean moons strung like beads near the limb."}, "Europa": {"km": 628000000, "view": "Europa is a bright ice ball crossed by brown cracks: the viewscreen shows a smooth, pale surface with long dark lineae like cracks in an eggshell, almost no craters, and Jupiter looming huge in the black sky behind it, the ice lit by reflected giant-planet light."}, "Saturn": {"km": 1275000000, "view": "Saturn's rings steal the viewscreen: a thin, brilliant ellipse of ice particles, banded in shades of gold and grey, with the pale gold globe of Saturn itself behind it, its belts softer than Jupiter's, and small shepherd moons dotting the ring plane."}, "Titan": {"km": 1275000000, "view": "Titan is an orange world under haze: the viewscreen shows a featureless orange globe, its surface hidden by thick nitrogen haze, with only a darker patch here and there hinting at the methane lakes and dunes that radar and landers have mapped beneath the veil."}, "Uranus": {"km": 2720000000, "view": "Uranus is a pale cyan-green globe, almost featureless: the viewscreen shows a smooth, quiet planet with only a faint polar hood and a thin dark ring system edge-on, a world tipped on its side so its poles, not its equator, face the Sun in turn."}, "Neptune": {"km": 4350000000, "view": "Neptune is a deep blue world with white streaks: the viewscreen shows dark blue bands, bright white methane clouds scudding across the disk, and a single dark storm oval, all lit by a Sun that is now only a bright star, not a disk of warmth."}, "Pluto": {"km": 5200000000, "view": "Pluto is a small, mottled world of pale plains and dark red-brown terrain: the viewscreen shows a heart-shaped bright plain of nitrogen ice against darker highlands, with its large moon Charon hanging nearby, grey and cratered, in a sky black as pitch."}, "Alpha Centauri": {"km": 41300000000000, "view": "Alpha Centauri is a double sun: two stars, one yellow like the Sun and one orange, blaze close together in the viewscreen, with the faint red dwarf Proxima a distant point, and any planets here are too small to show, known only from wobbles and dips in starlight."}, "Sirius": {"km": 81400000000000, "view": "Sirius is the brightest star of Earth's sky, seen close as a fierce white-blue point with a small white dwarf companion: the viewscreen shows no planets, only the blaze of the main star and the faint companion, with the Milky Way's band behind them."}, "Orion Nebula": {"km": 1344000000000000, "view": "The Orion Nebula is a glowing cloud of gas and newborn stars: the viewscreen shows green and pink folds of gas, dark dust lanes cutting across them, and at the center the four bright Trapezium stars, their light carving a cavity in the cloud around them."}, "Galactic Center": {"km": 260000000000000000, "view": "The galactic center is a crowded blaze: the viewscreen shows a dense star field, dark dust lanes, and at the very middle a point of gravity around which stars whip in tight, fast orbits, the whole region glowing with the combined light of millions of stars."}};
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
    console.log(JSON.stringify({ id: "JAH-US-GEN-" + String(emitted + 1).padStart(6, "0"), slug: "universal-spaceship-simulator", title: "Generated " + topic + " parameter variation v" + variant, edition: "public", src: "generated", generated: true, built_by: "generator", record_kind: "spaceship simulator record", feasibility_tier: "established", note: "Deterministic parameter variation (" + key + "). Labeled generated; not an assistant-built record." }));
    emitted++;
  }
  console.error("emitted " + emitted + " generated records for " + "universal-spaceship-simulator");
}
if (has("--destination") || has("--pause") || has("--step") || has("--advance-days")) simulate();
else if (has("--n")) generate();
else simulate();
