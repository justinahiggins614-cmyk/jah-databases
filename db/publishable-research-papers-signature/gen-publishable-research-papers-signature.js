// Generator for publishable-research-papers-signature — deterministic seeded generator, version 1.0
const SLUG = "publishable-research-papers-signature";
const KIND = "publishable full work record";
const ID_PREFIX = "JAH-PFWPS-";
const GEN_VERSION = "1.0";
const HARD_STOP = 1000000000;
const MAX_BATCH = 100;
const SEED_TITLES = ["Heat Flow Through Layered Insulating Panels: A Laboratory Measurement Study", "The Speed of Sound in Air at Different Humidities: A Classroom Measurement Study", "Rust Formation on Iron in Salt Water and Fresh Water: A Thirty-Day Comparison", "Natural Indicators from Red Cabbage and Turmeric: Measuring the Acidity of Household Liquids", "How Light Colour Affects the Growth of Lettuce Seedlings Over Four Weeks", "Seed Germination at Five Soil Moisture Levels: A Controlled Study with Cress", "A Twelve-Week Walking Programme and Resting Heart Rate in Healthy Adults", "Hand-Washing Technique and Bacterial Counts: A Comparison of Three Methods", "Rainwater Acidity Near a Roadway and in a Woodland: A Six-Month Comparison", "Plastic Fragments in Stream Sediment Upstream and Downstream of a Town", "Load Testing of Small Timber Beams: Span, Depth, and Breaking Load", "A Low-Cost Solar Water Heater: Design, Construction, and Measured Performance", "Comparing Sorting Algorithms on Small Data Sets: Measured Runtimes and Operation Counts", "A Rule-Based Spam Filter: Design, Testing, and Measured Accuracy", "Estimating Pi by Random Sampling: A Monte Carlo Study with Error Analysis", "The Fibonacci Sequence in Pine Cones: A Counting Study of Twenty Cones", "The Angle of Repose of Dry Sand, Gravel, and Garden Soil: A Measurement Study", "A Year of Rainfall Records: Comparing Two Neighbouring Valleys", "Does Background Music Affect Short-Term Memory Scores? A Controlled Experiment", "Sleep Duration and Next-Day Attention in School Pupils: A Four-Week Study", "Price Changes at a Local Market Across Four Seasons: An Observation Study", "How a Small Shop's Sales Respond to Weekend Discounts: A Sixteen-Week Study", "How the Antiseptic Principle Spread: The First Ten Years of Lister's Method in Print, 1867-1877", "The Reception of the Wave Theory of Light, 1800-1850: A Study in Scientific Change"];
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
const PublishableResearchPapersSignatureTools = { generate: generate, validate: validate, generateBatch: generateBatch, search: search, runTests: runTests, SLUG: SLUG, KIND: KIND, ID_PREFIX: ID_PREFIX, GEN_VERSION: GEN_VERSION, HARD_STOP: HARD_STOP };
if (typeof window !== "undefined") {
  window.PublishableResearchPapersSignatureTools = PublishableResearchPapersSignatureTools;
  window.JAHDB = window.JAHDB || {};
  window.JAHDB[SLUG] = PublishableResearchPapersSignatureTools;
}
if (typeof module !== "undefined" && module.exports) {
  module.exports = PublishableResearchPapersSignatureTools;
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
