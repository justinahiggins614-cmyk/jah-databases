"use strict";
/* The Piano Songs Romantic Database — boundless generator. Seeded, deterministic, throttled,
   duplicate-checked, hard stop at 10^15. Every generated record is ONE
   COMPLETE SONG (32 bars, both hands, full note data) and is labeled
   src "generated", never presented as an archive record. */
(function (root) {
  var SLUG = "piano-songs-romantic";
  var PREFIX = "JAH-PSRM-";
  var RECORD_KIND = "piano romantic song record";
  var GENRE = "romantic";
  var ERA = "Romantic era (1820-1910)";
  var AI_NAME = "JAH Romantic Piano Guide";
  var HARD_STOP = 1000000000000000; // 10^15
  var MAX_BATCH = 100;
  var MAJ = [0, 2, 4, 5, 7, 9, 11];
  var MIN = [0, 2, 3, 5, 7, 8, 10];
  var PROGS = [[0, 4, 5, 3, 0, 4, 5, 4], [5, 3, 0, 4, 5, 3, 4, 4], [0, 3, 5, 4, 0, 3, 4, 4], [0, 4, 0, 5, 3, 4, 5, 4]];
  var SECTIONS = ["Opening", "Development", "Return", "Closing"];
  var SEED_TITLES = ["Nocturne in E-flat Major", "Waltz in A Minor", "Character Piece: Longing in D Major", "Lied-Style Song in G Major", "Etude-Style Study in C Minor", "Nocturne in B-flat Major", "Waltz in C Major", "Character Piece: Evening Calm in F Major", "Lied-Style Song in D Minor", "Etude-Style Study in A Minor", "Nocturne in F Minor", "Waltz in G Major", "Character Piece: First Snow in E Major", "Lied-Style Song in A Major", "Etude-Style Study in E Minor", "Waltz in D-flat Major"];
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
  function buildNotes(rnd, tonic, minor) {
    var iv = minor ? MIN : MAJ;
    var ext = iv.concat(iv.map(function (x) { return x + 12; }));
    var rhBase = 60 + tonic; if (rhBase > 66) rhBase -= 12;
    var lhBase = 36 + tonic; if (lhBase > 41) lhBase -= 12;
    var notes = [], pos = 4;
    for (var sec = 0; sec < 4; sec++) {
      var prog = PROGS[sec];
      for (var bar = 0; bar < 8; bar++) {
        var deg = prog[bar], b0 = (sec * 8 + bar) * 4;
        for (var beat = 0; beat < 4; beat++) {
          if (beat === 0) {
            var tones = [deg, deg + 2, deg + 4], best = tones[0], bd = 99;
            tones.forEach(function (t) { [0, 7].forEach(function (o) {
              var c = t + o; if (c >= 0 && c <= 13 && Math.abs(c - pos) < bd) { bd = Math.abs(c - pos); best = c; }
            }); });
            pos = best;
          } else {
            pos = Math.max(0, Math.min(13, pos + [-2, -1, -1, 0, 1, 1, 2][Math.floor(rnd() * 7)]));
          }
          notes.push([b0 + beat, rhBase + ext[pos], 1.0, 1]);
        }
        var root = lhBase + iv[deg];
        var third = lhBase + iv[(deg + 2) % 7] + (deg + 2 >= 7 ? 12 : 0);
        var fifth = lhBase + iv[(deg + 4) % 7] + (deg + 4 >= 7 ? 12 : 0);
        if (GENRE === "classical") {
          [root, fifth, third, fifth].forEach(function (m, k) { notes.push([b0 + k * 0.5, m, 0.5, 0]); });
        } else if (GENRE === "romantic") {
          [root, third, fifth, root + 12].forEach(function (m, k) { notes.push([b0 + k, m, 1.0, 0]); });
        } else {
          notes.push([b0, root, 1.0, 0]); notes.push([b0 + 2, fifth, 1.0, 0]);
        }
      }
    }
    notes.sort(function (a, b) { return (a[0] - b[0]) || (a[3] - b[3]) || (a[1] - b[1]); });
    return notes;
  }
  function generateRecord(seed) {
    if (counter >= HARD_STOP) return null;
    var rnd = mulberry32(typeof seed === "number" ? seed : 1);
    var tonic = Math.floor(rnd() * 12);
    var minor = rnd() < 0.4;
    var title = SEED_TITLES[Math.floor(rnd() * SEED_TITLES.length)];
    var id = PREFIX + "GEN-" + pad(counter + 1);
    if (seen[id]) return null;
    seen[id] = true; counter += 1;
    var notes = buildNotes(rnd, tonic, minor);
    return { id: id, slug: SLUG, title: "Generated: " + title, record_kind: RECORD_KIND,
      src: "generated", genre: GENRE, era: ERA, key: "Generated key", time_signature: "4/4",
      tempo_bpm: 100, bars: 32, structure: SECTIONS.slice(), notes: notes,
      difficulty: "intermediate", composer: "Generated composition",
      provenance: "Generated complete song",
      body: "A boundlessly generated complete " + GENRE + " piano song in the family of " + title + ", produced by the seeded generator for this database. It is a full 32-bar song with complete note data for both hands." };
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
    if (!rec || rec.record_kind !== RECORD_KIND) problems.push("record_kind must be " + RECORD_KIND);
    if (!rec || rec.slug !== SLUG) problems.push("slug must be " + SLUG);
    if (!rec || !rec.id || rec.id.indexOf(PREFIX) !== 0) problems.push("id must start with " + PREFIX);
    if (!rec || !rec.title) problems.push("title is required");
    if (!rec || rec.bars < 16) problems.push("bars must be >= 16");
    if (!rec || !rec.notes || rec.notes.length < 64) problems.push("notes must be >= 64");
    if (!rec || (rec.structure || []).length < 3) problems.push("structure must have >= 3 sections");
    if (rec && rec.notes) {
      var lh = 0, rh = 0, last = 0, poly = {};
      rec.notes.forEach(function (n) {
        if (n[3] === 0) lh++; else rh++;
        if (n[1] < 21 || n[1] > 108) problems.push("midi out of range");
        if (Math.abs(n[0] * 4 - Math.round(n[0] * 4)) > 0.001) problems.push("beat grid must be 0.25 steps");
        if (n[0] + n[2] > last) last = n[0] + n[2];
        poly[n[0]] = (poly[n[0]] || 0) + 1;
      });
      if (lh < 8 || rh < 8) problems.push("both hands need >= 8 notes");
      if (last > rec.bars * 4) problems.push("notes exceed bars");
      Object.keys(poly).forEach(function (k) { if (poly[k] > 10) problems.push("polyphony exceeds 10"); });
    }
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
    tests.push({ name: "generated song is complete (bars/notes/sections)", pass: !!g && g.bars >= 16 && g.notes.length >= 64 && g.structure.length >= 3 });
    tests.push({ name: "duplicate ids rejected", pass: (function () { var a = generateRecord(7); return a && a.id !== g.id; })() });
    tests.push({ name: "batch throttle", pass: generateBatch(500, 99).length === MAX_BATCH });
    tests.push({ name: "search finds a title", pass: searchRecords(SEED_TITLES[0].slice(0, 4)).length >= 1 });
    var passed = tests.filter(function (t) { return t.pass; }).length;
    return { total: tests.length, passed: passed, tests: tests };
  }
  var Tools = { searchRecords: searchRecords, generateRecord: generateRecord, generateBatch: generateBatch, validateRecord: validateRecord, runTests: runTests, slug: SLUG, recordKind: RECORD_KIND, hardStop: HARD_STOP };
  root["PianoSongsRomanticTools"] = Tools;
  if (typeof module !== "undefined" && module.exports) module.exports = Tools;
  if (typeof process !== "undefined" && process.argv) {
    var idx = process.argv.indexOf("--n");
    if (idx !== -1) {
      var n = parseInt(process.argv[idx + 1], 10) || 1;
      generateBatch(n, 1).forEach(function (r) { console.log(JSON.stringify(r)); });
    }
  }
})(typeof window !== "undefined" ? window : globalThis);
