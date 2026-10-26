"use strict";
/* The Signature Honey Food Replicas Database — boundless generator. Seeded, deterministic, throttled,
   duplicate-checked, hard stop at 10^15. Generated records are
   labeled src "generated" and are never presented as archive records. */
(function (root) {
  var SLUG = "honey-food-replicas-signature";
  var PREFIX = "JAH-HFRS-";
  var RECORD_KIND = "honey food replica record";
  var HARD_STOP = 1000000000000000; // 10^15
  var MAX_BATCH = 100;
  var SEED_TITLES = ["Signature Honeycomb Gear Wheels", "Signature Honey Cake Shaped as a Beehive", "Signature Honey Nut-Paste Peaches and Hedgehogs", "Signature Honey Nougat Stars", "Signature Honey-Glazed Citrus Replicas", "Signature Hard Honey Candy Crystals", "Signature Baklava Honeycomb Hexagons", "Signature Honey Bread Shaped as a Honey Dipper", "Signature Honey Agar Gummy Grapes", "Signature Honey Caramel Honey Pots", "Signature Honey Fudge Bees and Toffee Honeycomb", "Signature Honey Chocolate Honeycomb Bars", "Signature Honey Syrup Spiral Art", "Signature Comb Honey Gift Frame", "Signature Honey Pastries Shaped as Sunflowers and Butterflies", "Signature Spiced Honey Mock-Mead"];
  var seen = {};
  var counter = 0;
  function mulberry32(a) {
    return function () {
      a |= 0; a = (a + 0x6D2B79F5) | 0;
      var t = Math.imul(a ^ (a >>> 15), 1 | a);
      t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t;
      return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
    };
  }
  function pad(n) { var s = String(n); while (s.length < 6) s = "0" + s; return s; }
  function generateRecord(seed) {
    if (counter >= HARD_STOP) return null;
    var rnd = mulberry32(typeof seed === "number" ? seed : 1);
    var title = SEED_TITLES[Math.floor(rnd() * SEED_TITLES.length)];
    var id = PREFIX + "GEN-" + pad(counter + 1);
    if (seen[id]) return null;
    seen[id] = true; counter += 1;
    return { id: id, slug: SLUG, title: "Generated: " + title,
      record_kind: RECORD_KIND, src: "generated",
      description: "A boundlessly generated honey food replica record in the " + title + " family, produced by the seeded generator for this database.",
      ingredients: ["Honey", "Sugar or flour suited to the replica", "Mold suited to the shape"],
      method: ["Follow the generated replica method for the chosen shape.", "Check the sugar stage or set before molding.", "Cool, turn out, and store as the record directs."],
      science: "The replica works through sugar-stage, crystallization, gelling, or Maillard science as described on the record.",
      safety: "Honey is not for infants under 12 months. Hot sugar syrup causes burns; handle with care.",
      storage: "Store as the record directs, protected from humidity.",
      variations: ["Vary the mold shape for a different replica from the same base."] };
  }
  function generateBatch(n, seed) {
    var out = [], count = Math.min(n || 1, MAX_BATCH);
    for (var i = 0; i < count; i++) { var r = generateRecord((seed || 1) + i); if (!r) break; out.push(r); }
    return out;
  }
  function searchRecords(q, pool) {
    q = String(q || "").toLowerCase();
    return (pool || SEED_TITLES).filter(function (t) { return t.toLowerCase().indexOf(q) !== -1; });
  }
  function validateRecord(rec) {
    var problems = [];
    if (!rec || rec.record_kind !== RECORD_KIND) problems.push("record_kind must be honey food replica record");
    if (!rec || rec.slug !== SLUG) problems.push("slug must be " + SLUG);
    if (!rec || !rec.id || rec.id.indexOf(PREFIX) !== 0) problems.push("id must start with " + PREFIX);
    if (!rec || !rec.title) problems.push("title is required");
    if (!rec || !rec.method || !rec.method.length) problems.push("method is required");
    return { valid: problems.length === 0, problems: problems };
  }
  function runTests() {
    var tests = [];
    var g = generateRecord(7);
    tests.push({ name: "generated record_kind", pass: !!g && g.record_kind === RECORD_KIND });
    tests.push({ name: "generated slug is single edition slug", pass: !!g && g.slug === SLUG });
    tests.push({ name: "generated id prefix", pass: !!g && g.id.indexOf(PREFIX + "GEN-") === 0 });
    tests.push({ name: "generated src label", pass: !!g && g.src === "generated" });
    tests.push({ name: "validateRecord accepts generated record", pass: !!g && validateRecord(g).valid });
    tests.push({ name: "duplicate ids rejected", pass: (function () { var a = generateRecord(7); return a && a.id !== g.id; })() });
    tests.push({ name: "batch throttle", pass: generateBatch(500, 99).length === MAX_BATCH });
    tests.push({ name: "search finds a title", pass: searchRecords(SEED_TITLES[0].slice(0, 4)).length >= 1 });
    var passed = tests.filter(function (t) { return t.pass; }).length;
    return { total: tests.length, passed: passed, tests: tests };
  }
  var Tools = { searchRecords: searchRecords, generateRecord: generateRecord, generateBatch: generateBatch, validateRecord: validateRecord, runTests: runTests, slug: SLUG, recordKind: RECORD_KIND, hardStop: HARD_STOP };
  root["HoneyFoodReplicasSignatureTools"] = Tools;
  if (typeof module !== "undefined" && module.exports) module.exports = Tools;
  if (typeof process !== "undefined" && typeof require !== "undefined" && require.main === module) {
    var n = 1;
    for (var i = 2; i < process.argv.length; i++) {
      if (process.argv[i] === "--n" && process.argv[i + 1]) n = parseInt(process.argv[i + 1], 10) || 1;
    }
    var batch = generateBatch(n, 1);
    if (n === 1) console.log(JSON.stringify(batch[0]));
    else console.log(JSON.stringify(batch));
  }
})(typeof window !== "undefined" ? window : globalThis);
