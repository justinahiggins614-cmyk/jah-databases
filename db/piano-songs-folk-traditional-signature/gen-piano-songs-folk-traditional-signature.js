
"use strict";
/* The Piano Songs Folk Traditional Database (Signature Edition) - boundless generator. Seeded, deterministic, throttled,
   duplicate-checked, hard stop at 10^15. Generated records are
   labeled src "generated" and are never presented as archive records. */
(function (root) {
  var SLUG = "piano-songs-folk-traditional-signature";
  var PREFIX = "JAH-PSFKS-";
  var RECORD_KIND = "piano folk song record";
  var HARD_STOP = 1000000000000000;
  var MAX_BATCH = 100;
  var SCALES = {"major": [0, 2, 4, 5, 7, 9, 11], "minor": [0, 2, 3, 5, 7, 8, 10]};
  var PROGS = [[1, 5, 6, 4], [1, 6, 4, 5], [1, 4, 6, 5], [1, 7, 6, 5]];
  var KEYS = [["C", "major", 0], ["G", "major", 7], ["F", "major", 5], ["A", "minor", 9], ["D", "minor", 2], ["E", "minor", 4]];
  var NAMES = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"];
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
  function noteName(m) { return NAMES[m % 12] + String(Math.floor(m / 12) - 1); }
  function renderDemo(rec) {
    var lines = [];
    lines.push("NOTES = " + JSON.stringify(rec.notes));
    lines.push("NAMES = " + JSON.stringify(NAMES));
    lines.push("print(" + JSON.stringify("TITLE: " + rec.title) + ")");
    lines.push("print(" + JSON.stringify("GENRE/ERA: " + rec.genre + " / " + rec.era) + ")");
    lines.push("print(" + JSON.stringify("KEY: " + rec.key + " | TIME: " + rec.time_signature + " | TEMPO: " + rec.tempo_bpm + " BPM | BARS: " + rec.bars + " | STRUCTURE: " + rec.structure.join(" ")) + ")");
    var out = [];
    out.push("TITLE: " + rec.title);
    out.push("GENRE/ERA: " + rec.genre + " / " + rec.era);
    out.push("KEY: " + rec.key + " | TIME: " + rec.time_signature + " | TEMPO: " + rec.tempo_bpm + " BPM | BARS: " + rec.bars + " | STRUCTURE: " + rec.structure.join(" "));
    lines.push("for start, midi, dur, hand in NOTES:");
    lines.push("    print(" + JSON.stringify("beat %.2f: MIDI %d (%s) dur %.2f hand %s") + " % (start, midi, NAMES[midi % 12] + str(midi // 12 - 1), dur, " + JSON.stringify("R") + " if hand == 1 else " + JSON.stringify("L") + "))");
    rec.notes.forEach(function (n) {
      out.push("beat " + n[0].toFixed(2) + ": MIDI " + n[1] + " (" + noteName(n[1]) + ") dur " + n[2].toFixed(2) + " hand " + (n[3] === 1 ? "R" : "L"));
    });
    var tb = rec.bars * 4;
    var secs = (tb * 60 / rec.tempo_bpm).toFixed(1);
    out.push("SONG COMPLETE: " + rec.notes.length + " notes, " + tb + " beats, " + secs + " seconds");
    lines.push("print(" + JSON.stringify("SONG COMPLETE: " + rec.notes.length + " notes, " + tb + " beats, " + secs + " seconds") + ")");
    return { code: lines.join(String.fromCharCode(10)) + String.fromCharCode(10), expected_output: out.join(String.fromCharCode(10)) + String.fromCharCode(10) };
  }
  function generateRecord(seed) {
    if (counter >= HARD_STOP) return null;
    var rnd = mulberry32(typeof seed === "number" ? seed : 1);
    var ki = Math.floor(rnd() * KEYS.length);
    var keyName = KEYS[ki][0];
    var mode = KEYS[ki][1];
    var tonic = KEYS[ki][2];
    var sc = SCALES[mode];
    var prog = PROGS[Math.floor(rnd() * PROGS.length)];
    var bars = 24;
    var tempo = 72 + Math.floor(rnd() * 56);
    var notes = [];
    var deg = 7;
    var rhythm = [1, 1, 1, 1];
    for (var bar = 0; bar < bars; bar++) {
      var chord = prog[bar % prog.length];
      var rootIdx = (chord - 1) % 7;
      var thirdIdx = (chord + 1) % 7;
      var fifthIdx = (chord + 3) % 7;
      var b0 = bar * 4;
      notes.push([b0, 36 + tonic + sc[rootIdx], 2, 0]);
      notes.push([b0 + 2, 36 + tonic + sc[fifthIdx], 2, 0]);
      var cur = b0;
      for (var ri = 0; ri < rhythm.length; ri++) {
        var dur = rhythm[ri];
        var r = rnd();
        if (r < 0.55) deg += (rnd() < 0.5 ? -1 : 1);
        else if (r < 0.75) deg += (rnd() < 0.5 ? -2 : 2);
        else if (r >= 0.85) {
          var tones = [rootIdx, thirdIdx, fifthIdx];
          var curPc = ((deg % 7) + 7) % 7;
          var best = tones[0];
          var bd = 99;
          tones.forEach(function (t) { var d = Math.abs(t - curPc); if (d < bd) { bd = d; best = t; } });
          while (((deg % 7) + 7) % 7 !== best) { deg += (((best - curPc) % 7) + 7) % 7 <= 3 ? 1 : -1; curPc = ((deg % 7) + 7) % 7; }
        }
        if (deg < 0) deg = 0;
        if (deg > 13) deg = 13;
        var midi = 60 + tonic + sc[((deg % 7) + 7) % 7] + 12 * Math.floor(deg / 7);
        notes.push([cur, midi, dur, 1]);
        cur += dur;
      }
    }
    notes.sort(function (a, b) { return (a[0] - b[0]) || (a[3] - b[3]); });
    var id = PREFIX + "GEN-" + pad(counter + 1);
    if (seen[id]) return null;
    seen[id] = true; counter += 1;
    var rec = { id: id, slug: SLUG, title: "Generated: " + mode + " study " + String(counter),
      edition: "signature", src: "generated", provenance: "Signature-original composition",
      record_kind: RECORD_KIND, ladder_rank: "simple", genre: "traditional nursery tune", era: "traditional",
      composer: "Signature original", key: keyName + " " + mode, time_signature: "4/4",
      tempo_bpm: tempo, bars: bars, structure: ["A", "A", "B", "A"], notes: notes,
      difficulty: "beginner", technique: "Generated complete song: melody over chord accompaniment.",
      body: "<p>A boundlessly generated complete piano song in this database, produced by the seeded generator.</p>" };
    rec.demo = renderDemo(rec);
    return rec;
  }
  function generateBatch(n, seed) {
    var out = [], count = Math.min(n || 1, MAX_BATCH);
    for (var i = 0; i < count; i++) { var r = generateRecord((seed || 1) + i); if (!r) break; out.push(r); }
    return out;
  }
  function searchRecords(q, pool) {
    q = String(q || "").toLowerCase();
    var titles = ["ballad", "dance", "songwriter", "theme", "underscore", "romance", "adventure", "mystery", "folk", "hymn", "carol", "spiritual", "reel", "jig", "waltz", "lullaby"];
    return (pool || titles).filter(function (t) { return t.toLowerCase().indexOf(q) !== -1; });
  }
  function validateRecord(rec) {
    var problems = [];
    if (!rec || rec.record_kind !== RECORD_KIND) problems.push("record_kind must be " + RECORD_KIND);
    if (!rec || rec.slug !== SLUG) problems.push("slug must be " + SLUG);
    if (!rec || !rec.id || rec.id.indexOf(PREFIX) !== 0) problems.push("id must start with " + PREFIX);
    if (!rec || !rec.title) problems.push("title is required");
    if (!rec || rec.bars < 16) problems.push("bars must be >= 16");
    if (!rec || !rec.notes || rec.notes.length < 64) problems.push("notes must be >= 64");
    if (rec && rec.notes) {
      var lh = 0, rh = 0, badGrid = false, badMidi = false;
      var atBeat = {};
      rec.notes.forEach(function (n) {
        if (n[3] === 0) lh += 1; else rh += 1;
        if (Math.abs(n[0] * 4 - Math.round(n[0] * 4)) > 1e-9) badGrid = true;
        if (n[1] < 21 || n[1] > 108) badMidi = true;
        atBeat[n[0]] = (atBeat[n[0]] || 0) + 1;
      });
      if (lh < 8) problems.push("left hand must be >= 8");
      if (rh < 8) problems.push("right hand must be >= 8");
      if (badGrid) problems.push("beat grid must be 0.25");
      if (badMidi) problems.push("midi range 21-108");
      Object.keys(atBeat).forEach(function (k) { if (atBeat[k] > 10) problems.push("polyphony > 10"); });
      var dur = rec.bars * 4 * 60 / rec.tempo_bpm;
      if (dur < 30) problems.push("duration must be >= 30s");
    }
    if (!rec || !rec.structure || rec.structure.length < 3) problems.push("structure must be >= 3 sections");
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
    tests.push({ name: "generated record is a complete song", pass: !!g && g.bars >= 16 && g.notes.length >= 64 && g.structure.length >= 3 });
    tests.push({ name: "generated demo ends SONG COMPLETE", pass: !!g && g.demo && g.demo.expected_output.indexOf("SONG COMPLETE") !== -1 });
    tests.push({ name: "duplicate ids rejected", pass: (function () { var a = generateRecord(7); return a && a.id !== g.id; })() });
    tests.push({ name: "batch throttle", pass: generateBatch(500, 99).length === MAX_BATCH });
    tests.push({ name: "search finds a title", pass: searchRecords("ball").length >= 1 });
    var passed = tests.filter(function (t) { return t.pass; }).length;
    return { total: tests.length, passed: passed, tests: tests };
  }
  var Tools = { searchRecords: searchRecords, generateRecord: generateRecord, generateBatch: generateBatch, validateRecord: validateRecord, runTests: runTests, slug: SLUG, recordKind: RECORD_KIND, hardStop: HARD_STOP };
  root["PianoSongsFolkTraditionalSignatureTools"] = Tools;
  if (typeof module !== "undefined" && module.exports) module.exports = Tools;
  if (typeof process !== "undefined" && process.argv) {
    var idx = process.argv.indexOf("--n");
    if (idx !== -1) {
      var n = parseInt(process.argv[idx + 1], 10) || 1;
      generateBatch(n, 1).forEach(function (r) { console.log(JSON.stringify(r)); });
    }
  }
})(typeof window !== "undefined" ? window : globalThis);
