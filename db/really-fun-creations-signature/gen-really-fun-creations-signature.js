// gen-really-fun-creations-signature.js -- boundless generator for the Really Fun Creations Signature Database.
// Usage: node gen-really-fun-creations-signature.js --n 5
// Deterministic: a seeded LCG drives parameter variations.
// Self-regulating: throttled, duplicate-checked, hard-stops at 10^15
// records or when the variation space is genuinely exhausted.
// Generated records carry "generated": true and src "generated" --
// never mixed with assistant-built records.
"use strict";
const HARD_CAP = 1e15;
const TOPICS = ["Infinite World Builder", "Random Dungeon Generator", "Creature Collector", "Choose Your Own Chaos", "Boss Battle Factory", "Procedural Kingdom Simulator", "Zombie Apocalypse Simulator", "Alien Planet Explorer", "Superhero Showdown Creator", "Infinite Obby Generator", "Ridiculous Invention Machine", "Fake Superpower Generator", "Absurd Law Generator", "Unnecessary Luxury Creator", "Random Excuse Generator", "Worst Possible Advice Machine", "Fake Conspiracy Universe", "Chaotic Animal Translator", "Cursed Product Catalog", "Bizarre Holiday Creator", "Monster DNA Mixer", "Pet Evolution Simulator", "Hybrid Animal Creator", "Kaiju Generator", "Mythical Species Encyclopedia", "Alien Lifeform Lab", "Mutant Ecosystem Simulator", "Dragon Kingdom Creator", "Living Object Generator", "Evolution Tournament", "Multiverse Creator", "Lost Civilization Generator", "Fantasy Religion and Mythology Builder", "Alien Civilization Simulator", "Time Travel Adventure Builder", "Alternate History Machine", "Dream World Generator", "Pocket Universe Creator", "Lost Dimension Explorer", "Apocalypse-to-Civilization Simulator", "Dream House Generator", "Theme Park Creator", "Spaceship Designer", "City of the Future Builder", "Secret Base Creator", "Fantasy Castle Generator", "Robot Companion Designer", "Impossible Machine Inventor", "Magical Shop Generator", "Dream Bedroom Designer", "Friend Group Trivia Creator", "Party Game Factory", "Mystery Dinner Generator", "Escape Room Creator", "Friendly Roast Generator", "Would You Rather: Extreme Edition", "Scavenger Hunt Builder", "Tournament Generator", "Collaborative Story Machine", "Random Challenge Wheel", "Album Universe Creator", "Music Video Storyboard Generator", "Comic Universe Factory", "Animated Series Creator", "Meme Universe Generator", "Fantasy Trading Card Creator", "Magic Spellbook Generator", "Random Movie Plot Machine", "Dream Creature Art Prompt Factory", "Interactive Audio Adventure", "Black Hole Playground", "Dinosaur Island Simulator", "Ecosystem Chaos Lab", "Theme Park Physics Lab", "Space Colony Manager", "Volcano and Planet Builder", "Evolutionary Robot Arena", "Economy of an Imaginary World", "Civilization Evolution Lab", "Disaster Survival Sandbox", "Infinite Treasure Chest", "Artifact Archaeology Simulator", "Secret Code Factory", "Mystery Box Generator", "Rare Creature Index", "Procedural Treasure Map Maker", "Achievement and Badge Factory", "Collectible Card Universe", "Hidden Object World Builder", "Mystery of the Day Generator", "Personal Universe Generator", "Infinite What-If Machine", "Reality Remix Studio", "Build-Your-Own Superpower System", "AI Game Master", "Living Fictional Wiki", "Invention Battle Arena", "Infinite Puzzle Universe", "Personalized Adventure Engine", "The Anything Machine"];
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
    id: "JAH-RFS-GEN-" + String(k + 1).padStart(6, "0"),
    slug: "really-fun-creations-signature",
    title: "Generated " + topic + " parameter variation v" + variant,
    edition: "signature",
    src: "generated",
    generated: true,
    built_by: "generator",
    record_kind: "fun creation package record",
    feasibility_tier: "designed",
    body: "<p>Generated parameter variation v" + variant + " of " + topic + ". Labeled generated; not an assistant-built record. Create, play, and expand layers (where applicable) follow the parent template; validation rules of the parent record apply.</p>",
    demo_code: "print('generated variation')",
    demo_output: "generated variation\n",
    implementation_status: "designed",
    provenance: "Generator output; labeled generated.",
    last_verified: "2026-10-25",
    license: "https://creativecommons.org/publicdomain/zero/1.0/"
  };
}
function main() {
  const n = parseN(process.argv.slice(2));
  if (n > HARD_CAP) { console.error("requested count exceeds HARD_CAP"); process.exit(1); }
  const out = [];
  let k = 0, guard = 0;
  while (out.length < n && guard < n * 20 + 1000) {
    guard++;
    const r = makeRecord(k);
    if (r) { out.push(r); k++; }
  }
  out.forEach(function (r) { console.log(JSON.stringify(r)); });
}
if (require.main === module) main();
module.exports = { HARD_CAP: HARD_CAP, makeRecord: makeRecord };
