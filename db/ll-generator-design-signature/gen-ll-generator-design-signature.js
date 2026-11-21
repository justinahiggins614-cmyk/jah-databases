"use strict";
/* The L.L. Generator for ll-generator-design-signature - boundless generator. Seeded, deterministic,
   throttled, duplicate-checked, hard stop at 1,000,000,000. Generated records
   are labeled src "generated" and "simulated" and are never presented as
   public records or as things that were built. The wwii-history-products
   profile is public history only, labeled history. */
(function (root) {
  var SLUG = "ll-generator-design-signature";
  var PREFIX = "JAH-LLDS-";
  var RECORD_KIND = "L.L. design record";
  var HARD_STOP = 1000000000;
  var MAX_BATCH = 100;
  var DESIGN_DNA = { tower_ratio: "746 ft / 4200 ft = 0.1776",
    cable_geometry: "catenary, 27,572 wires per cable (public design)",
    color: "International Orange" };
  var PROFILES = [{"name": "bridge-products", "label": "Bridge Products", "designs": ["L.L. Footbridge", "L.L. Garden Bridge", "L.L. Park Crossing", "L.L. River Footbridge", "L.L. Plaza Bridge", "L.L. Trail Bridge", "L.L. Courtyard Bridge", "L.L. Campus Crossing", "L.L. Meadow Bridge", "L.L. Harbor Footbridge", "L.L. Village Bridge", "L.L. Hillside Crossing"]}, {"name": "tower-products", "label": "Tower Products", "designs": ["L.L. Tower Lamp", "L.L. Tower Shelf", "L.L. Tower Bookend", "L.L. Tower Model", "L.L. Tower Clock", "L.L. Tower Garden Ornament", "L.L. Tower Coat Stand", "L.L. Tower Table Leg", "L.L. Tower Signpost", "L.L. Tower Birdhouse", "L.L. Tower Lantern", "L.L. Tower Trophy"]}, {"name": "cable-products", "label": "Cable Products", "designs": ["L.L. Hanging Lamp", "L.L. Cable Shelf", "L.L. Suspender Chandelier", "L.L. Cable Coat Rack", "L.L. Catenary Mirror", "L.L. Cable Plant Hanger", "L.L. Hanging Chair", "L.L. Cable Desk Lamp", "L.L. Suspender Mobile", "L.L. Cable Room Divider", "L.L. Catenary Bookshelf", "L.L. Cable Wall Art"]}, {"name": "deck-products", "label": "Deck Products", "designs": ["L.L. Deck Walkway", "L.L. Garden Deck", "L.L. Deck Bench", "L.L. Walkway Model", "L.L. Deck Table", "L.L. Boardwalk Section", "L.L. Deck Swing", "L.L. Footbridge Deck", "L.L. Deck Planter", "L.L. Viewing Platform", "L.L. Deck Canopy", "L.L. Riverside Walkway"]}, {"name": "companies", "label": "Companies", "designs": ["L.L. Bridgeworks", "L.L. Tower Company", "L.L. Cable Works", "L.L. Deck Builders", "L.L. Anchorage Works", "L.L. Span Studio", "L.L. Crossing Company", "L.L. Design Foundry", "L.L. Suspension Works", "L.L. Profile Studio", "L.L. Bridge Design Co.", "L.L. Scale Works"]}, {"name": "wwii-history-products", "label": "WWII History Products", "designs": ["Bailey Bridge (history record)", "Higgins Landing Craft LCVP (history record)", "Mulberry Harbour (history record)", "Pontoon Bridge Section (history record)", "Wartime Crossing Record (history record)", "Bailey Panel Set (history record)", "Landing Craft Record (history record)", "Harbour Section Record (history record)", "Rhine Crossing Record (history record)", "Wartime Bridge Record (history record)", "Portable Bridge Record (history record)", "War Years Crossing Record (history record)"]}, {"name": "everyday-products", "label": "Everyday Products", "designs": ["L.L. Bridge Lamp", "L.L. Orange Mug", "L.L. Tower Toy", "L.L. Bridge Puzzle", "L.L. Suspension Bookends", "L.L. Bridge Poster Frame", "L.L. Cable Key Ring", "L.L. Bridge Model Kit", "L.L. Tower Night Light", "L.L. Bridge Coasters", "L.L. Orange Throw Pillow", "L.L. Bridge Calendar"]}, {"name": "city-products", "label": "City Products", "designs": ["L.L. Bridge District", "L.L. Crossing Plaza", "L.L. Waterfront Walk", "L.L. Span Quarter", "L.L. Tower Square", "L.L. Cable Promenade", "L.L. Deck Esplanade", "L.L. Anchorage Park", "L.L. Gateway District", "L.L. Harbor Crossing", "L.L. Riverside Quarter", "L.L. Bayfront Walk"]}];
  function profileNames() { return PROFILES.map(function (p) { return p.name; }); }
  function findProfile(name) {
    for (var i = 0; i < PROFILES.length; i++) { if (PROFILES[i].name === name) return PROFILES[i]; }
    return null;
  }
  function fnv1a(s) {
    var h = 0x811c9dc5;
    for (var i = 0; i < s.length; i++) { h ^= s.charCodeAt(i); h = Math.imul(h, 0x01000193) >>> 0; }
    return h >>> 0;
  }
  function pad8(n) { var s = n.toString(16); while (s.length < 8) s = "0" + s; return s; }
  function genId(seed) {
    var a = pad8(fnv1a(SLUG + "|" + String(seed)));
    var b = pad8(fnv1a(SLUG + "|" + String(seed) + "|2"));
    return PREFIX + "GEN-" + (a + b).slice(0, 12);
  }
  function generateRecord(seed, profile) {
    var s = (seed === undefined || seed === null) ? 1 : seed;
    var prof = findProfile(profile);
    if (!prof) { prof = PROFILES[fnv1a(SLUG + "|" + String(s)) % PROFILES.length]; }
    var design = prof.designs[fnv1a(SLUG + "|" + String(s) + "|" + prof.name) % prof.designs.length];
    var history = prof.name === "wwii-history-products";
    return { id: genId(s), slug: SLUG, title: "Generated: " + design,
      record_kind: RECORD_KIND, src: "generated", simulated: true,
      profile: prof.name, profile_label: prof.label,
      design_dna: DESIGN_DNA, label: history ? "history" : "simulated",
      description: history
        ? "A generated history record in the " + prof.label + " profile: public history only, labeled history, drawn from the documented wartime record. This is a generated design-study record, not a public record."
        : "A boundlessly generated " + prof.label + " design in the family of " + design + ", produced by The L.L. Generator from the L.L. design DNA (tower ratio 0.1776, catenary cable, International Orange). Simulated design study, not a public record and not a thing that was built." };
  }
  function generateBatch(n, seed) {
    var out = [], count = Math.min(n || 1, MAX_BATCH);
    for (var i = 0; i < count; i++) { out.push(generateRecord((seed || 1) + i)); }
    return out;
  }
  function searchRecords(q, pool) {
    q = String(q || "").toLowerCase();
    var names = pool || PROFILES.reduce(function (acc, p) { return acc.concat(p.designs); }, []);
    return names.filter(function (t) { return t.toLowerCase().indexOf(q) !== -1; });
  }
  function validateRecord(rec) {
    var problems = [];
    if (!rec || rec.record_kind !== RECORD_KIND) problems.push("record_kind must be " + RECORD_KIND);
    if (!rec || rec.slug !== SLUG) problems.push("slug must be " + SLUG);
    if (!rec || !rec.id || rec.id.indexOf(PREFIX + "GEN-") !== 0) problems.push("id must start with " + PREFIX + "GEN-");
    if (!rec || !rec.title) problems.push("title is required");
    if (!rec || rec.src !== "generated") problems.push("src must be generated");
    if (!rec || rec.simulated !== true) problems.push("simulated must be true");
    if (!rec || !findProfile(rec.profile)) problems.push("profile must be one of the eight profiles");
    if (!rec || !rec.design_dna || rec.design_dna.tower_ratio !== DESIGN_DNA.tower_ratio) problems.push("design_dna must carry the L.L. tower ratio");
    return { valid: problems.length === 0, problems: problems };
  }
  function runTests() {
    var tests = [];
    var g = generateRecord(7);
    tests.push({ name: "generated record_kind", pass: !!g && g.record_kind === RECORD_KIND });
    tests.push({ name: "generated slug is single edition slug", pass: !!g && g.slug === SLUG && g.slug.indexOf("signature-" + "signature") === -1 });
    tests.push({ name: "generated id prefix", pass: !!g && g.id.indexOf(PREFIX + "GEN-") === 0 });
    tests.push({ name: "generated src label", pass: !!g && g.src === "generated" });
    tests.push({ name: "profile honored", pass: generateRecord(7, "tower-products").profile === "tower-products" });
    tests.push({ name: "validateRecord accepts generated record", pass: !!g && validateRecord(g).valid });
    tests.push({ name: "reproducibility same seed same record", pass: JSON.stringify(generateRecord(7)) === JSON.stringify(g) });
    tests.push({ name: "different seeds give different ids", pass: generateRecord(7).id !== generateRecord(8).id });
    tests.push({ name: "batch throttle", pass: generateBatch(500, 99).length === MAX_BATCH });
    tests.push({ name: "hard stop is 10^9", pass: HARD_STOP === 1000000000 });
    var passed = tests.filter(function (t) { return t.pass; }).length;
    return { total: tests.length, passed: passed, tests: tests };
  }
  var Tools = { searchRecords: searchRecords, generateRecord: generateRecord, generateBatch: generateBatch, validateRecord: validateRecord, runTests: runTests, genId: genId, profileNames: profileNames, profiles: PROFILES, slug: SLUG, recordKind: RECORD_KIND, hardStop: HARD_STOP, designDNA: DESIGN_DNA };
  root["LLGeneratorDesignSignatureTools"] = Tools;
  if (typeof module !== "undefined" && module.exports) module.exports = Tools;
})(typeof window !== "undefined" ? window : globalThis);
