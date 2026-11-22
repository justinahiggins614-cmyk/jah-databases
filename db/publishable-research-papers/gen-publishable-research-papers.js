// Generator for publishable-research-papers — deterministic seeded generator, version 1.0
const SLUG = "publishable-research-papers";
const KIND = "publishable full work record";
const ID_PREFIX = "JAH-PFWP-";
const GEN_VERSION = "1.0";
const HARD_STOP = 1000000000;
const MAX_BATCH = 100;
const SEED_TITLES = ["On a Heuristic Point of View about the Creation and Conversion of Light", "Geometry and Experience", "The Development of Our Views on the Composition and Essence of Radiation", "On the Electric and Magnetic Effects produced by the Motion of Electrified Bodies", "A Revision of the Fundamental Laws of Matter and Energy", "On the Relative Motion of the Earth and the Luminiferous Ether", "A New System of Alternating Current Motors and Transformers", "On the Antiseptic Principle of the Practice of Surgery", "A Biographical Sketch of an Infant", "Composite Portraits", "Psychometric Facts", "Health and Sex in Higher Education", "The Chaos in Moral Training", "The Scientific Basis of Morals", "On the Causes Which Operate to Create Scientific Men", "Aims and Instruments of Scientific Thought I", "The Economic Theory of Woman's Dress", "The Investigation of the San Francisco Earthquake", "Are Animals Automatons?", "What are Species?", "The Equation of State for a Monatomic Gas (Eight Lectures, Lecture IV)", "Heat Radiation. Electrodynamic Theory (Lecture V)", "General Dynamics. Principle of Least Action (Lecture VII)", "On the Tendency of Varieties to Depart Indefinitely from the Original Type"];
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
    searchWorks: search("Signature").length >= 0 && search(SEED_TITLES[0].slice(0, 4)).length >= 1,
    hardStop: HARD_STOP === 1000000000
  };
  const passed = Object.keys(tests).every(function(k) { return tests[k]; });
  return { passed: passed, tests: tests };
}
const PublishableResearchPapersTools = { generate: generate, validate: validate, generateBatch: generateBatch, search: search, runTests: runTests, SLUG: SLUG, KIND: KIND, ID_PREFIX: ID_PREFIX, GEN_VERSION: GEN_VERSION, HARD_STOP: HARD_STOP };
if (typeof window !== "undefined") {
  window.PublishableResearchPapersTools = PublishableResearchPapersTools;
  window.JAHDB = window.JAHDB || {};
  window.JAHDB[SLUG] = PublishableResearchPapersTools;
}
if (typeof module !== "undefined" && module.exports) {
  module.exports = PublishableResearchPapersTools;
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
