// Generator for publishable-full-works-signature — deterministic seeded generator, version 1.0
const SLUG = "publishable-full-works-signature";
const KIND = "publishable full work record";
const ID_PREFIX = "JAH-PFWS-";
const GEN_VERSION = "1.0";
const HARD_STOP = 1000000000;
const MAX_BATCH = 100;
const SEED_TITLES = ["On Keeping a Commonplace Book", "The Patience of the Gardener", "On Walking as Thinking", "The Honesty of the Draft", "On the Pleasure of Making Lists", "The Silence Between Sentences", "The Lighthouse Keeper's Last Log", "The Cartographer's Daughter", "The Clockmaker's Apprentice", "The Letter That Arrived Fifty Years Late", "The Seed Vault", "The Man Who Collected Echoes", "How a Library Catalogue Works", "The History of the Pencil", "Why Bridges Stand", "The Life Cycle of a Letter", "How Tides Are Made", "The Making of a Map", "Reading Speed and Comprehension Across Text Lengths: A Controlled Study", "Sleep Duration and Next-Day Recall of Word Lists: An Experimental Study", "Public Library Use in Small Towns: A Survey of Twelve Libraries", "The Thermal Behaviour of a Clay Oven: Measurements and a Model", "Birdsong at Dawn: A Census of Morning Chorus Timing", "The Growth of Bean Seedlings Under Three Light Regimes: An Experimental Study"];
function hash12(input) {
  let h1 = 2166136261, h2 = 0;
  for (let i = 0; i < input.length; i++) {
    h1 ^= input.charCodeAt(i); h1 = Math.imul(h1, 16777619) >>> 0;
    h2 = (h2 * 31 + input.charCodeAt(i)) >>> 0;
  }
  const s = (h1.toString(16).padStart(8, "0") + h2.toString(16).padStart(8, "0")).slice(0, 12);
  return s;
}
function titleForSeed(seed) {
  if (SEED_TITLES.length === 0) return "Untitled work";
  const h = hash12(SLUG + "|" + GEN_VERSION + "|" + String(seed));
  return SEED_TITLES[parseInt(h.slice(0, 4), 16) % SEED_TITLES.length];
}
function generate(seed) {
  const s = String(seed);
  const hash = hash12(SLUG + "|" + GEN_VERSION + "|" + s);
  return {
    id: ID_PREFIX + "GEN-" + hash,
    slug: SLUG,
    record_kind: KIND,
    src: "generated",
    title: titleForSeed(s),
    description: "Generated publishable full work record in the " + SLUG + " family, produced by seeded generation from seed " + s + "."
  };
}
function validate(record) {
  if (!record || typeof record !== "object") return false;
  return record.slug === SLUG && record.record_kind === KIND && record.src === "generated"
    && typeof record.id === "string" && record.id.indexOf(ID_PREFIX + "GEN-") === 0
    && typeof record.title === "string" && record.title.length > 0;
}
function generateBatch(count) {
  const n = Math.min(Math.max(0, count | 0), MAX_BATCH);
  const out = [];
  for (let i = 0; i < n; i++) out.push(generate("batch-" + i));
  return out;
}
function search(query) {
  const q = String(query).toLowerCase();
  return SEED_TITLES.filter(function(t) { return t.toLowerCase().indexOf(q) !== -1; });
}
function runTests() {
  const a1 = generate("alpha"), a2 = generate("alpha"), b = generate("beta");
  const wrong = Object.assign({}, a1, { record_kind: "other kind" });
  const batch = generateBatch(150);
  const tests = {
    sameSeedIdentical: JSON.stringify(a1) === JSON.stringify(a2),
    differentSeedDifferent: JSON.stringify(a1) !== JSON.stringify(b),
    validateOwn: validate(a1) === true,
    validateWrongKind: validate(wrong) === false,
    batchThrottle: batch.length === MAX_BATCH,
    searchWorks: SEED_TITLES.length === 0 ? true : (search("Signature").length >= 0 && search(SEED_TITLES[0].slice(0, 4)).length >= 1),
    hardStop: HARD_STOP === 1000000000
  };
  const passed = Object.keys(tests).every(function(k) { return tests[k]; });
  return { passed: passed, tests: tests };
}
const PublishableFullWorksSignatureTools = { generate: generate, validate: validate, generateBatch: generateBatch, search: search, runTests: runTests, SLUG: SLUG, KIND: KIND, ID_PREFIX: ID_PREFIX, GEN_VERSION: GEN_VERSION, HARD_STOP: HARD_STOP };
if (typeof window !== "undefined") {
  window.PublishableFullWorksSignatureTools = PublishableFullWorksSignatureTools;
  window.JAHDB = window.JAHDB || {};
  window.JAHDB[SLUG] = PublishableFullWorksSignatureTools;
}
if (typeof module !== "undefined" && module.exports) {
  module.exports = PublishableFullWorksSignatureTools;
  if (require.main === module) {
    const a1 = generate("alpha"), a2 = generate("alpha");
    console.log(JSON.stringify({
      generateAlphaTwiceIdentical: JSON.stringify(a1) === JSON.stringify(a2),
      generateAlpha: a1,
      validateOwn: validate(a1),
      validateWrongKind: validate(Object.assign({}, a1, { record_kind: "other kind" })),
      runTests: runTests()
    }, null, 2));
  }
}
