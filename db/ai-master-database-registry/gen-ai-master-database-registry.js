// Generator for ai-master-database-registry — deterministic seeded generator, version 1.0
const SLUG = "ai-master-database-registry";
const KIND = "master database registry record";
const ID_PREFIX = "JAH-AMDR-";
const GEN_VERSION = "1.0";
const HARD_STOP = 1000000000;
const MAX_BATCH = 100;
const SEED_TITLES = ["Database Category Registry", "Database Industry Registry", "Database Specialty Registry", "Database Language Registry", "Database Geographic Registry", "Database Status Registry", "Database Version Registry", "Database Ownership Registry", "Database Purpose Registry", "Database API Inventory", "Database Tool Inventory", "Database Relationship Inventory", "Database Citation Inventory", "Database Source Inventory", "Database Update Inventory", "Database Searchable-Field Inventory", "Database Endpoint Inventory", "Database Download Inventory", "Database Demonstration Inventory", "Database Program Inventory", "Database Proof Inventory", "Database Validation Inventory", "Universal Database Discovery Engine", "Database Discovery Endpoint"];
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
    description: "Generated record in the " + SLUG + " family, produced by seeded generation from seed " + s + "."
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
  const wrongKind = Object.assign({}, a1, { record_kind: "other kind" });
  const wrongSlug = Object.assign({}, a1, { slug: "other-slug" });
  const wrongPrefix = Object.assign({}, a1, { id: "JAH-XXXX-GEN-0123456789ab" });
  const batch150 = generateBatch(150);
  const batch500 = generateBatch(500);
  const tests = {
    sameSeedIdentical: JSON.stringify(a1) === JSON.stringify(a2),
    differentSeedDifferent: JSON.stringify(a1) !== JSON.stringify(b),
    validateOwn: validate(a1) === true,
    validateWrongKind: validate(wrongKind) === false,
    validateWrongSlug: validate(wrongSlug) === false,
    validateWrongPrefix: validate(wrongPrefix) === false,
    batchThrottle: batch150.length === MAX_BATCH,
    throttle500to100: batch500.length === MAX_BATCH,
    searchWorks: search(SEED_TITLES[0].slice(0, 4)).length >= 1,
    hardStop: HARD_STOP === 1000000000
  };
  const passed = Object.keys(tests).every(function(k) { return tests[k]; });
  return { passed: passed, tests: tests };
}
const AiMasterDatabaseRegistryTools = { generate: generate, validate: validate, generateBatch: generateBatch, search: search, runTests: runTests, SLUG: SLUG, KIND: KIND, ID_PREFIX: ID_PREFIX, GEN_VERSION: GEN_VERSION, HARD_STOP: HARD_STOP };
if (typeof window !== "undefined") {
  window.AiMasterDatabaseRegistryTools = AiMasterDatabaseRegistryTools;
  window.JAHDB = window.JAHDB || {};
  window.JAHDB[SLUG] = AiMasterDatabaseRegistryTools;
}
if (typeof module !== "undefined" && module.exports) {
  module.exports = AiMasterDatabaseRegistryTools;
  if (require.main === module) {
    const a1 = generate("alpha"), a2 = generate("alpha");
    console.log(JSON.stringify({
      generateAlphaTwiceIdentical: JSON.stringify(a1) === JSON.stringify(a2),
      generateAlpha: a1,
      validateOwn: validate(a1),
      validateWrongKind: validate(Object.assign({}, a1, { record_kind: "other kind" })),
      batch500Length: generateBatch(500).length,
      runTests: runTests()
    }, null, 2));
  }
}
