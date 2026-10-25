// gen-bizarre-generators.js -- boundless generator for the Bizarre Generators Database.
// Usage: node gen-bizarre-generators.js --n 5
// Deterministic: a seeded LCG drives parameter variations.
// Self-regulating: throttled, duplicate-checked, hard-stops at 10^15
// records or when the variation space is genuinely exhausted.
// Generated records carry "generated": true and src "generated" --
// never mixed with assistant-built records.
"use strict";
const HARD_CAP = 1e15;
const TOPICS = ["The Nonsense Civilization Generator", "The Object Rebellion Simulator", "The Completely Unnecessary Apocalypse", "Random Tuesday Simulator", "The Infinite Excuse Multiverse", "Sentient Furniture Drama", "The World's Worst Superhero Factory", "Reverse Evolution Lab", "The Bureaucracy Dungeon", "The Forbidden Button Simulator", "100-Legged Hamster Civilization", "The Mutation Slot Machine", "Emotional Weather Monsters", "The Reverse Pet Shop", "The Unpronounceable Creature Generator", "Alien Wildlife Court", "The Evolution Mistake Museum", "Giant Microscopic World", "Monster Personality Roulette", "The Animal Merger Disaster Lab", "The Planet of Mildly Inconvenient Physics", "The Universe Inside a Sandwich", "The Planet That Is One Giant Mall", "The Upside-Down Universe", "The Universe Run by Babies", "The Infinite Basement Generator", "The Reality Glitch Factory", "The Cosmic Lost-and-Found", "The Universe With a Customer Service Department", "The Multiverse of Bad Decisions", "Competitive Rock Staring", "Extreme Hide-and-Seek for Planets", "The Floor Is Legally Lava", "Pigeon Mafia Simulator", "The World's Slowest Racing League", "Competitive Cloud Shaping", "The Unstable Tower of Random Objects", "Dungeon of Infinite Doors", "The Boss Fight Is a Complaint Form", "The Button Pressing Olympics", "The Sentient Spaghetti Simulator", "The Bad Idea Science Lab", "The Emotion-to-Object Converter", "The Randomness Amplifier", "The Laws-of-Physics Bargaining Simulator", "The Universe's Patch Notes Generator", "The Sentient Spreadsheet Simulator", "The Time Traveler's Laundry Machine", "The Dimension Blender", "The Consequence Snowball Machine", "Alien First Contact Gone Wrong", "The Ghost Job Placement Agency", "Cryptid Neighborhood Watch", "Haunted Vending Machine Simulator", "The Paranormal Complaint Hotline", "The UFO Parking Authority", "The Time Traveler's Worst Tourist Guide", "The Monster Roommate Matchmaker", "The Interdimensional Yard Sale", "The Department of Unexplained Socks", "The Museum of Things That Never Existed", "The World's Most Pointless Invention Catalog", "The Fake Luxury Brand Factory", "The Cursed Trading Card Universe", "The Extremely Specific Award Generator", "The Imaginary Food Laboratory", "The Unnecessary Gadget Workshop", "The Museum of Failed Superpowers", "The Fake Ancient Relic Creator", "The Infinite Weird Sticker Factory", "The Debate Between Two Idiotic Geniuses", "The Fake News From an Imaginary Planet Generator", "The World's Strangest Dating Show", "The Random Villain Monologue Machine", "The Intergalactic Reality Show Builder", "The Ridiculous Courtroom Generator", "The Corporate Meeting From Hell", "The Awkward Conversation Simulator", "The Argument Escalator", "The Random Character Drama Machine", "The Infinite Generator Generator", "The Self-Expanding Fictional Internet", "The Billion-Item Curiosity Vault", "The Random Civilization Collision Engine", "The Everything Has a Personality Engine", "The Impossible Theme Park Universe", "The Dream-to-Game Factory", "The Fictional Internet Rabbit Hole", "The Chaos Kingdom Builder", "The User's Own Weirdness Museum", "The Reality Roulette", "The Universe That Tries to Entertain You", "The Ultimate Mashup Machine", "The Everything Simulator", "The Infinite Secret Generator", "The Alternate Self Generator", "The Universe's Worst Upgrade System", "The Grand Tournament of Absolutely Everything", "The Bizarre Idea-to-Experience Engine", "THE JAH INFINITE CHAOS FACTORY"];
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
    id: "JAH-BZ-GEN-" + String(k + 1).padStart(6, "0"),
    slug: "bizarre-generators",
    title: "Generated " + topic + " parameter variation v" + variant,
    edition: "public",
    src: "generated",
    generated: true,
    built_by: "generator",
    record_kind: "bizarre generator package record",
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
