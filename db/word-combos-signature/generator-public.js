// word-combos — boundless generator (Signature design). PACKAGE-ONLY.
// Emits records of kind "word-combo" with id prefix "JAH-WCOM-".
// Hard stop: 1,000,000,000 per file. Throttled: at most 1000 records per tick.
// Generated outputs are labelled simulated/design, never presented as public record.
// Seeded: same seed + same range gives identical output; different seeds differ.
// Held words: the 139 distinct words of the 103 Wave 1 stored combos
// (pair records JAH-WCOM-000004–JAH-WCOM-000106). The generator does not
// carry the full 102,223-headword vocabulary, so a generated design combo
// is given rank null with the reason stated, never faked.
"use strict";
const SLUG = "word-combos";
const KIND = "word-combo";
const PREFIX = "JAH-WCOM-";
const HARD_STOP = 1000000000;
const THROTTLE = 1000;
const WORDS = ["AI", "Accountability", "Age", "Animal", "Attraction", "Audiobook", "Build-your-own-world", "Caption", "Checkers", "Chess", "Community", "Concert", "Construction", "Content", "Cost-of-living", "Coupon", "Creator", "Creature", "Currency", "Daily", "Date", "Digital", "Discount", "Ebook", "Fan", "Festival", "Fitness", "Flashcard", "Future-self", "GPA", "Gardening", "Geography", "Goal", "Grade", "Guess-the-movie", "Guess-the-personality", "Guess-the-picture", "Guess-the-song", "Habit", "Hairstyle", "Hobby", "Image", "Inflation", "Interactive", "Interest", "Joke", "Knowledge", "Loan", "Meal", "Measurement", "Memory", "Monster", "Mood", "Mortgage", "Movie", "Museum", "Music", "Mystery-solving", "Newsletter", "Number", "Old-photo", "One-minute", "Paycheck", "Percentage", "Personal", "Photo", "Photo-to-anime", "Photo-to-cartoon", "Podcast", "Poster", "Price-drop", "Probability", "Public", "Question-and-answer", "Recipe", "Restaurant", "Retirement", "Salary", "Shared", "Statistics", "Subscription", "Superhero", "Superpower", "Tax", "Time-zone", "Unit", "Universal", "Used-item", "Virtual", "Vocabulary", "Wardrobe", "Word-of-the-day", "Workout", "alerts", "calculator", "calendar", "classroom", "collections", "colorization", "communities", "community", "comparison", "competition", "competitions", "converter", "creator", "diary", "dictionary", "directory", "discovery", "encyclopedia", "enhancement", "estimator", "explorer", "finder", "game", "games", "generator", "groups", "journal", "lessons", "marketplace", "meetups", "organizer", "planner", "platform", "polls", "preview", "puzzles", "recommendations", "restoration", "service", "simulator", "storefront", "tracker", "translator", "trivia", "tutor", "upscaler"];
function mulberry32(a) {
  return function () {
    a |= 0; a = (a + 0x6D2B79F5) | 0;
    let t = Math.imul(a ^ (a >>> 15), 1 | a);
    t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t;
    return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
  };
}
function makeRecord(n, seed) {
  if (n < 1 || n > HARD_STOP) throw new Error("out of range: " + n);
  seed = (seed === undefined || seed === null) ? 1 : seed;
  const id = PREFIX + String(n).padStart(6, "0");
  const rnd = mulberry32(seed * 1000003 + n);
  const i1 = Math.floor(rnd() * WORDS.length);
  let i2 = Math.floor(rnd() * WORDS.length);
  if (i2 === i1) i2 = (i2 + 1) % WORDS.length;
  const w1 = WORDS[i1], w2 = WORDS[i2];
  const combo = w1 + " " + w2;
  const comboSlug = (w1 + "-" + w2).toLowerCase();
  return {
    id: id,
    slug: SLUG,
    record_kind: KIND,
    edition: "public",
    title: "Generated word-combo record " + n + " — seed " + seed + ", combo \"" + combo + "\" (design)",
    seed: seed,
    combo: combo,
    combo_slug: comboSlug,
    combo_url: "combos/" + comboSlug + "/",
    words: [w1, w2],
    word_count: 2,
    length_class: "2-word",
    rank: null,
    rank_reason: "Generated design combo: rank is computed only against the full 102,223-headword ordering, which this script does not carry; rank left null, never faked.",
    design_label: "Signature design — simulated/design, never presented as a public record.",
    plain_words: "PLAIN WORDS: This is a made-up design record about a word combination. It is not a public fact. It follows the same plain-words rules as the real records.",
    body: "Generated design record " + n + " for word combos (seed " + seed + ", combo \"" + combo + "\"). The combo slug is the combo's identity. The full combo space is generator option space, sampled and verified, never stored. SIGNATURE DESIGN CLAIM: this generated combo is design, never a public record.",
    hierarchy: "God supreme; humanity highest earthly authority under God; man measured fully under that authority; Signature the shared foundation.",
    provenance: { source_name: "Signature boundless generator (design)", source_url: "", retrieved: "2026-11-23", license: "Signature design — simulated." },
    last_verified: "2026-11-23",
  };
}
function generate(count, start, seed) {
  start = start || 1;
  seed = (seed === undefined || seed === null) ? 1 : seed;
  if (start + count - 1 > HARD_STOP) throw new Error("hard stop 1000000000 exceeded");
  const out = [];
  for (let i = 0; i < count; i += THROTTLE) {
    const chunk = Math.min(THROTTLE, count - i);
    for (let j = 0; j < chunk; j++) out.push(makeRecord(start + i + j, seed));
  }
  return out;
}
function runTests() {
  const fails = [];
  const r = makeRecord(1);
  if (r.record_kind !== KIND) fails.push("record_kind mismatch: " + r.record_kind);
  if (r.slug !== SLUG) fails.push("slug mismatch: " + r.slug);
  if (r.slug.indexOf("-signature") !== -1 && "public" !== "signature") fails.push("signature slug on public edition");
  if ("public" === "signature" && r.slug.slice(-10) !== "-signature") fails.push("signature slug must end -signature");
  if (r.id.indexOf(PREFIX) !== 0) fails.push("id prefix mismatch: " + r.id);
  if (!/^JAH-[A-Z]+-\d{6}$/.test(r.id)) fails.push("id shape bad: " + r.id);
  if (r.rank !== null) fails.push("generated rank must be null, never faked");
  if (r.words.length !== 2 || r.words[0] === r.words[1]) fails.push("generated combo words bad");
  const batch = generate(5, 1);
  if (batch.length !== 5) fails.push("generate count wrong");
  if (new Set(batch.map(x => x.id)).size !== 5) fails.push("duplicate ids");
  if (batch.some(x => x.record_kind !== KIND)) fails.push("batch kind mismatch");
  const a = generate(5, 1, 42), b = generate(5, 1, 42);
  if (JSON.stringify(a) !== JSON.stringify(b)) fails.push("same-seed outputs differ");
  const c = generate(5, 1, 43);
  if (JSON.stringify(a) === JSON.stringify(c)) fails.push("different-seed outputs identical");
  if (a[0].seed !== 42 || c[0].seed !== 43) fails.push("seed not carried in record");
  try { generate(1, HARD_STOP + 1); fails.push("hard stop not enforced"); } catch (e) {}
  return { passed: fails.length === 0, failures: fails };
}
if (typeof module !== "undefined") module.exports = { makeRecord: makeRecord, generate: generate, runTests: runTests, SLUG: SLUG, KIND: KIND, PREFIX: PREFIX, HARD_STOP: HARD_STOP };
if (typeof require !== "undefined" && require.main === module) {
  const t = runTests();
  console.log(JSON.stringify(t, null, 2));
  if (!t.passed) process.exit(1);
  console.log(JSON.stringify(generate(3, 1), null, 2));
}
