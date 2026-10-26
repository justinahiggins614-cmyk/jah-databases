"use strict";
/* The Milk Uses Database - boundless generator. Seeded, deterministic, throttled,
   duplicate-checked, hard stop at 10^15. Generated records are
   labeled src "generated" and are never presented as archive records. */
(function (root) {
  var SLUG = "milk-uses";
  var PREFIX = "JAH-MLKU-";
  var RECORD_KIND = "milk use record";
  var HARD_STOP = 1000000000000000; // 10^15
  var MAX_BATCH = 100;
  var SEED_TITLES = ["Drinking Milk: Fresh, Flavored, and Chocolate Milk", "Milk in Baking: Breads and Cakes", "Milk Sauces and Soups: Bechamel and Chowders", "Butter and Ghee Churning", "Cream Products: Whipped, Clotted, Sour Cream, and Creme Fraiche", "Fresh Cheeses: Ricotta, Paneer, Cottage Cheese, and Mozzarella", "Aged Cheeses: Cheddar, Gouda, and Brie Styles", "Yogurt and Cultured Milk: Yogurt, Kefir, and Cultured Buttermilk", "Ice Cream and Frozen Desserts", "Puddings and Custards: Rice Pudding, Panna Cotta, Creme Brulee, and Flan", "Milk Drinks: Lattes, Milkshakes, Lassi, Honey Milk, and Chocolate Milk", "Condensed and Evaporated Milk, and Milk Powder", "Milk in Skincare: Milk Baths and Cleansers", "Casein Glue and Milk Paint: Historical Craft", "Whey Uses: Whey Drinks, Whey Ricotta, and Whey in Baking", "Milk Preservation: Pasteurization, UHT, and Fermentation Preservation"];
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
      description: "A boundlessly generated milk use record in the " + title + " family, produced by the seeded generator for this database.",
      ingredients: ["Milk suited to the use", "Supporting ingredients as the method requires"],
      method: ["Follow the generated method for this milk use.", "Keep milk foods refrigerated except while working.", "Taste, adjust, and store as the record directs."],
      safety: "Use pasteurized milk. Milk allergy and lactose notes apply.",
      storage: "Refrigerate milk foods promptly and use within the stated days.",
      variations: ["Vary the flavoring or the milk fat level for a different version."] };
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
    if (!rec || rec.record_kind !== RECORD_KIND) problems.push("record_kind must be milk use record");
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
  root["MilkUsesTools"] = Tools;
  if (typeof module !== "undefined" && module.exports) module.exports = Tools;
  if (typeof module !== "undefined" && require.main === module) {
    var argv = process.argv.slice(2);
    var n = 1;
    for (var i = 0; i < argv.length; i++) {
      if (argv[i] === "--n" && argv[i + 1]) n = parseInt(argv[i + 1], 10) || 1;
    }
    var batch = generateBatch(n, 1);
    batch.forEach(function (rec) { console.log(JSON.stringify(rec)); });
  }
})(typeof window !== "undefined" ? window : globalThis);
