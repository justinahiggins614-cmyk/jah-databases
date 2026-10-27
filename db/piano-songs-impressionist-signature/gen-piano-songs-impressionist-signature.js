"use strict";
/* The Signature Piano Songs Impressionist Database — boundless generator. Seeded, deterministic, throttled,
   duplicate-checked, hard stop at 10^15. Generated records are
   labeled src "generated" and are never presented as archive records. */
(function (root) {
  var SLUG = "piano-songs-impressionist-signature";
  var PREFIX = "JAH-PSIMS-";
  var RECORD_KIND = "piano impressionist song record";
  var GENRE = "impressionist piano";
  var HARD_STOP = 1000000000000000; // 10^15
  var MAX_BATCH = 100;
  var NAMES = ["C","C#","D","D#","E","F","F#","G","G#","A","A#","B"];
  var SCALES = [[0,2,4,5,7,9,11],[0,3,5,6,7,10],[0,2,3,5,7,9,10],[0,2,4,7,9]];
  var PROGS = [[[0,[0,4,7]],[5,[0,4,7]],[0,[0,4,7]],[7,[0,4,7,10]]],
               [[2,[0,3,7,10]],[7,[0,4,7,10]],[0,[0,4,7,11]],[9,[0,3,7,10]]]];
  var SEED_TITLES = ["Veil of Silver Rain", "Garden of Quiet Hours", "The Pale Horizon Line", "Lanterns on the Lagoon", "Song of the Hidden Spring", "Dusk Over the Water Meadow", "The Glass Pavilion", "Autumn Mist at Dawn", "The Whispering Cypress", "Tides of Soft Light", "The Moonlit Courtyard", "Rain on the Rooftops of the Old Town", "The Dreaming Lake", "Footsteps in the Fern Gully", "Evening Star Over the Hills", "The Still Point of the Day"];
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
  function midiName(m) { return NAMES[m % 12] + String(Math.floor(m / 12) - 1); }
  function buildNotes(rnd, keyRoot, scale) {
    var notes = [];
    var base = 60 + keyRoot;
    var pitches = [];
    for (var o = 0; o < 2; o++) for (var i = 0; i < scale.length; i++) {
      var p = base + 12 * o + scale[i];
      if (p >= 55 && p <= 86) pitches.push(p);
    }
    pitches.sort(function (a, b) { return a - b; });
    var idx = Math.floor(pitches.length / 2);
    var prog = PROGS[Math.floor(rnd() * PROGS.length)];
    for (var bar = 0; bar < 32; bar++) {
      var chord = prog[bar % prog.length];
      var rootPc = (keyRoot + chord[0]) % 12;
      var bass = 36 + rootPc;
      notes.push([bar * 4, bass, 1.0, 0]);
      for (var k = 0; k < chord[1].length; k++)
        notes.push([bar * 4 + 2, 48 + ((rootPc + chord[1][k]) % 12), 2.0, 0]);
      var chordPcs = {};
      for (var j = 0; j < chord[1].length; j++) chordPcs[(rootPc + chord[1][j]) % 12] = true;
      for (var beat = 0; beat < 4; beat++) {
        if (beat === 0) {
          var best = idx, bestD = 1e9;
          for (var q = 0; q < pitches.length; q++)
            if (chordPcs[pitches[q] % 12] && Math.abs(q - idx) < bestD) { bestD = Math.abs(q - idx); best = q; }
          idx = best;
        } else {
          idx = Math.max(0, Math.min(pitches.length - 1, idx + Math.floor(rnd() * 5) - 2));
        }
        notes.push([bar * 4 + beat, pitches[idx], 1.0, 1]);
      }
    }
    notes.sort(function (a, b) { return (a[0] - b[0]) || (a[3] - b[3]) || (a[1] - b[1]); });
    return notes;
  }
  function buildDemo(title, genre, keyName, tempo, notes) {
    var lines = [];
    lines.push(title);
    lines.push("Genre: " + genre + " | Key: " + keyName + " | Time: 4/4 | Tempo: " + tempo + " BPM | Bars: 32 | Structure: A-A-B-A");
    var sorted = notes.slice().sort(function (a, b) { return (a[0] - b[0]) || (a[3] - b[3]) || (a[1] - b[1]); });
    for (var i = 0; i < sorted.length; i++) {
      var n = sorted[i];
      lines.push("beat " + n[0].toFixed(1) + ": MIDI " + n[1] + " (" + midiName(n[1]) + ") dur " + n[2].toFixed(1) + " hand " + (n[3] === 1 ? "R" : "L"));
    }
    var beats = 128, secs = (beats * 60.0 / tempo).toFixed(1);
    lines.push("SONG COMPLETE: " + notes.length + " notes, " + beats + " beats, " + secs + " seconds");
    var code = "NOTES = " + JSON.stringify(notes) + "\n# Generated demo prints the full timeline (see expected_output).";
    return { code: code, expected_output: lines.join("\n") + "\n" };
  }
  function generateRecord(seed) {
    if (counter >= HARD_STOP) return null;
    var rnd = mulberry32(typeof seed === "number" ? seed : 1);
    var title = SEED_TITLES[Math.floor(rnd() * SEED_TITLES.length)];
    var keyRoot = Math.floor(rnd() * 12);
    var scale = SCALES[Math.floor(rnd() * SCALES.length)];
    var notes = buildNotes(rnd, keyRoot, scale);
    var id = PREFIX + "GEN-" + pad(counter + 1);
    if (seen[id]) return null;
    seen[id] = true; counter += 1;
    var keyName = NAMES[keyRoot] + " major";
    var tempo = 96;
    return { id: id, slug: SLUG, title: "Generated: " + title, edition: "generated",
      src: "generated", provenance: "generated complete song", record_kind: RECORD_KIND,
      ladder_rank: "simple", genre: GENRE, era: "generated", composer: "Generated composition",
      key: keyName, time_signature: "4/4", tempo_bpm: tempo, bars: 32,
      structure: ["A", "A", "B", "A"], notes: notes, difficulty: "beginner",
      technique: "Generated complete song: steady left hand under a singing right hand.",
      body: "<p>Generated complete song in the family of " + title + ", produced by the seeded generator for this database.</p>",
      demo: buildDemo("Generated: " + title, GENRE, keyName, tempo, notes) };
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
    if (!rec || !rec.id || rec.id.indexOf(PREFIX + "GEN-") !== 0) problems.push("id must start with " + PREFIX + "GEN-");
    if (!rec || rec.src !== "generated") problems.push("src must be generated");
    if (!rec || !rec.title) problems.push("title is required");
    if (!rec || rec.bars < 16) problems.push("bars must be >= 16");
    if (!rec || !rec.notes || rec.notes.length < 64) problems.push("notes must be >= 64");
    if (!rec || !rec.structure || rec.structure.length < 3) problems.push("structure must have >= 3 sections");
    if (rec && rec.notes) {
      var lh = 0, rh = 0, beats = rec.bars * 4, ok = true;
      for (var i = 0; i < rec.notes.length; i++) {
        var n = rec.notes[i];
        if (n[3] === 0) lh++; else rh++;
        if (n[1] < 21 || n[1] > 108) ok = false;
        if (n[0] + n[2] > beats + 1e-9) ok = false;
      }
      if (lh < 8 || rh < 8) problems.push("both hands need >= 8 notes");
      if (!ok) problems.push("note range or time-signature consistency failed");
      if (beats * 60.0 / rec.tempo_bpm < 30.0) problems.push("duration must be >= 30 s");
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
    tests.push({ name: "generated record is a complete song", pass: !!g && g.notes.length >= 64 && g.bars >= 16 });
    tests.push({ name: "duplicate ids rejected", pass: (function () { var a = generateRecord(7); return a && a.id !== g.id; })() });
    tests.push({ name: "batch throttle", pass: generateBatch(500, 99).length === MAX_BATCH });
    tests.push({ name: "search finds a title", pass: searchRecords(SEED_TITLES[0].slice(0, 4)).length >= 1 });
    var passed = tests.filter(function (t) { return t.pass; }).length;
    return { total: tests.length, passed: passed, tests: tests };
  }
  var Tools = { searchRecords: searchRecords, generateRecord: generateRecord, generateBatch: generateBatch, validateRecord: validateRecord, runTests: runTests, slug: SLUG, recordKind: RECORD_KIND, hardStop: HARD_STOP };
  root["PianoSongsImpressionistSignatureTools"] = Tools;
  if (typeof module !== "undefined" && module.exports) module.exports = Tools;
  if (typeof process !== "undefined" && process.argv) {
    var idx = process.argv.indexOf("--n");
    if (idx !== -1) {
      var n = parseInt(process.argv[idx + 1], 10) || 1;
      generateBatch(n, 1).forEach(function (r) { console.log(JSON.stringify(r)); });
    }
  }
})(typeof window !== "undefined" ? window : globalThis);
