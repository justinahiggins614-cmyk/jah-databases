"use strict";
/* The Milk Food Replicas Database — boundless generator. Seeded, deterministic, throttled,
   duplicate-checked, hard stop at 10^15. Generated records are
   labeled src "generated" and are never presented as archive records. */
(function (root) {
  var SLUG = "milk-food-replicas";
  var PREFIX = "JAH-MFR-";
  var RECORD_KIND = "milk food replica record";
  var HARD_STOP = 1000000000000000; // 10^15
  var MAX_BATCH = 100;
  var SEED_TITLES = ["Milk Jelly and Blancmange in Fruit Molds", "Panna Cotta Shaped as Fruit and Objects", "Milk Pudding Cups as Trompe-l'oeil Savory Dishes", "Milk Cheeses Molded as Other Foods", "Ice Cream Shaped as Fruit, Sushi and Burgers", "Milk Cakes Shaped as Foods", "Molded Milk Chocolate Objects", "Custard Tarts Shaped as Objects", "Milk Fudge and Milk Sweets Shaped as Fruit", "Frozen Yogurt Bark Shaped as Foods", "Milk Toffee and Dulce de Leche Shapes", "Milk Breads Shaped as Animals and Objects", "Butter Sculptures", "Whipped Cream Art and Cream Flowers", "Milk-Powder Confections: Milk Cake and Barfi-Style Sweets", "Milk Foam and Latte Art Designs"];
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
      description: "A boundlessly generated milk food replica record in the " + title + " family, produced by the seeded generator for this database.",
      original_food: "A milk food in the " + title + " family.",
      replica_recipe: ["Pasteurized milk", "Sugar", "Agar or starch as the setting agent, as fits the replica"],
      method: ["Prepare the milk base as the record describes.", "Shape or mold the replica while it is workable.", "Chill, freeze, or bake as the replica requires, and serve as directed."],
      science: "Milk gelling, freezing, emulsification, or foam science, as fits the replica, explains why the shape holds.",
      safety: "Use pasteurized milk, note milk allergy and lactose, and follow the record storage guidance.",
      storage: "Refrigerate, freeze, or store cool as the replica requires.", variations: ["Vary the mold shape or flavour for a new replica in the same family."] };
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
    if (!rec || rec.record_kind !== RECORD_KIND) problems.push("record_kind must be milk food replica record");
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
    tests.push({ name: "batch throttle", pass: generateBatch(500, 99).length === MAX_BATCH });
    tests.push({ name: "search finds a title", pass: searchRecords(SEED_TITLES[0].slice(0, 4)).length >= 1 });
    var passed = tests.filter(function (t) { return t.pass; }).length;
    return { total: tests.length, passed: passed, tests: tests };
  }
  var Tools = { searchRecords: searchRecords, generateRecord: generateRecord, generateBatch: generateBatch, validateRecord: validateRecord, runTests: runTests, slug: SLUG, recordKind: RECORD_KIND, hardStop: HARD_STOP };
  root["MilkFoodReplicasTools"] = Tools;
  if (typeof module !== "undefined" && module.exports) module.exports = Tools;
  if (typeof process !== "undefined" && process.argv && process.argv.indexOf("--n") !== -1) {
    var nIdx = process.argv.indexOf("--n");
    var n = parseInt(process.argv[nIdx + 1] || "1", 10) || 1;
    console.log(JSON.stringify(generateBatch(n, 1), null, 2));
  }
})(typeof window !== "undefined" ? window : globalThis);
