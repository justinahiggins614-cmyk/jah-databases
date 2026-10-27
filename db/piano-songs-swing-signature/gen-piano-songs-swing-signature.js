"use strict";
/* The Piano Songs Swing Database Signature — boundless generator. Seeded, deterministic, throttled,
   duplicate-checked, hard stop at 10^15. Generated records are
   labeled src "generated" and are never presented as archive records.
   Every generated record is a COMPLETE song: bars >= 16, notes >= 64,
   both hands >= 8, polyphony <= 10, midi 21-108. */
(function (root) {
  var SLUG = "piano-songs-swing-signature";
  var PREFIX = "JAH-PSSWS-";
  var RECORD_KIND = "piano swing song record";
  var GENRE = "piano swing";
  var ERA = "1930s to 1940s, swing era";
  var SCALE = [0, 2, 4, 5, 7, 9, 11];
  var CYCLE = [[2, [0, 3, 7, 10]], [7, [0, 4, 7, 10]], [0, [0, 4, 7, 11]], [0, [0, 4, 7, 11]], [9, [0, 3, 7, 10]], [2, [0, 3, 7, 10]], [7, [0, 4, 7, 10]], [0, [0, 4, 7, 11]]];
  var LHSTYLE = "stride";
  var HARD_STOP = 1000000000000000; // 10^15
  var MAX_BATCH = 100;
  var SEED_TITLES = ["Signature Easy Swing", "Signature Avenue Stroll", "Signature Gentle Stride", "Signature Afternoon Swing", "Signature Soft Shoe Study", "Signature Midtown Walk", "Signature Stride Showcase", "Signature Jump Swing", "Signature Big-Band Study", "Signature Swing Ballad", "Signature Sixteen-Bar Swing", "Signature Fast Stride", "Signature Late Night Ballad", "Signature Double-Time Swing", "Signature Grand Swing Study", "Signature Swing Finale"];
  var NAMES = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"];
  var KEYS = ["Bb major", "C major", "D major", "Eb major", "F major", "G major"];
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
  function fmt(v) { return v.toFixed(1); }
  function noteName(m) { return NAMES[m % 12] + (Math.floor(m / 12) - 1); }
  function demoFor(rec) {
    var lines = [];
    lines.push(rec.title);
    lines.push("Genre: " + rec.genre + " | Era: " + rec.era + " | Key: " + rec.key + " | Time: " + rec.time_signature + " | Tempo: " + rec.tempo_bpm + " BPM | Bars: " + rec.bars + " | Structure: " + rec.structure.join(" "));
    rec.notes.forEach(function (n) {
      lines.push("beat " + fmt(n[0]) + ": MIDI " + n[1] + " (" + noteName(n[1]) + ") dur " + fmt(n[2]) + " hand " + (n[3] === 1 ? "R" : "L"));
    });
    var beats = rec.bars * 4;
    lines.push("SONG COMPLETE: " + rec.notes.length + " notes, " + beats + " beats, " + (beats * 60 / rec.tempo_bpm).toFixed(1) + " seconds");
    var code = "BARS = " + rec.bars + "\nTEMPO = " + rec.tempo_bpm + "\nNOTES = " + JSON.stringify(rec.notes) + "\nNAMES = [\"C\", \"C#\", \"D\", \"D#\", \"E\", \"F\", \"F#\", \"G\", \"G#\", \"A\", \"A#\", \"B\"]\nprint(" + JSON.stringify(rec.title) + ")\nprint(" + JSON.stringify("Genre: " + rec.genre + " | Era: " + rec.era + " | Key: " + rec.key + " | Time: " + rec.time_signature + " | Tempo: " + rec.tempo_bpm + " BPM | Bars: " + rec.bars + " | Structure: " + rec.structure.join(" ")) + ")\nfor start, midi, dur, hand in NOTES:\n    name = NAMES[midi % 12] + str(midi // 12 - 1)\n    print(\"beat %.1f: MIDI %d (%s) dur %.1f hand %s\" % (start, midi, name, dur, \"R\" if hand == 1 else \"L\"))\nprint(\"SONG COMPLETE: %d notes, %d beats, %.1f seconds\" % (len(NOTES), BARS * 4, BARS * 4 * 60.0 / TEMPO))\n";
    return { code: code, expected_output: lines.join("\n") + "\n" };
  }
  function generateRecord(seed) {
    if (counter >= HARD_STOP) return null;
    var rnd = mulberry32(typeof seed === "number" ? seed : 1);
    var ti = Math.floor(rnd() * SEED_TITLES.length);
    var title = SEED_TITLES[ti];
    var key = KEYS[Math.floor(rnd() * KEYS.length)];
    var pcMap = { "C": 0, "D": 2, "E": 4, "F": 5, "G": 7, "A": 9, "Bb": 10, "Eb": 3 };
    var pc = pcMap[key.split(" ")[0]];
    var center = 60 + pc, lhBase = 36 + pc;
    var pitches = [];
    for (var m = center - 5; m < center + 18; m++) {
      if (SCALE.indexOf(((m - pc) % 12 + 12) % 12) !== -1) pitches.push(m);
    }
    var bars = 32, tempo = 108, level = "simple";
    if (ti >= 11) level = "complex"; else if (ti >= 6) level = "compounded";
    var pattern = level === "simple" ? [[0, 1], [1, 1], [2, 1], [3, 1]]
      : [[0, 1], [1, 1], [2, 0.5], [2.5, 0.5], [3, 0.5], [3.5, 0.5]];
    var idx = Math.floor(pitches.length / 2);
    var notes = [];
    for (var bar = 0; bar < bars; bar++) {
      var chord = CYCLE[bar % CYCLE.length];
      var root = lhBase + chord[0], tones = chord[1];
      var b0 = bar * 4;
      if (LHSTYLE === "stride") {
        notes.push([b0, root, 1, 0]); notes.push([b0 + 2, root + tones[1], 1, 0]); notes.push([b0 + 2, root + tones[3], 1, 0]);
      } else if (LHSTYLE === "boogie") {
        notes.push([b0, root, 0.5, 0]); notes.push([b0 + 1, root + 7, 0.5, 0]); notes.push([b0 + 2, root + 12, 0.5, 0]); notes.push([b0 + 3, root + 7, 0.5, 0]);
      } else if (LHSTYLE === "slow") {
        notes.push([b0, root, 2, 0]); notes.push([b0 + 2, root + 7, 2, 0]);
      } else {
        notes.push([b0, root, 1, 0]); notes.push([b0 + 2, root + 7, 1, 0]);
      }
      for (var p = 0; p < pattern.length; p++) {
        idx += Math.floor(rnd() * 5) - 2;
        if (rnd() < 0.12) idx += rnd() < 0.5 ? -4 : 4;
        if (idx < 0) idx = 0; if (idx > pitches.length - 1) idx = pitches.length - 1;
        var mel = pitches[idx];
        notes.push([b0 + pattern[p][0], mel, pattern[p][1], 1]);
        if (level === "complex" && pattern[p][0] === 0 && idx + 2 < pitches.length)
          notes.push([b0, pitches[idx + 2], pattern[p][1], 1]);
      }
    }
    notes.sort(function (a, b) { return (a[0] - b[0]) || (a[3] - b[3]) || (a[1] - b[1]); });
    var id = PREFIX + "GEN-" + pad(counter + 1);
    if (seen[id]) return null;
    seen[id] = true; counter += 1;
    var rec = { id: id, slug: SLUG, title: "Generated: " + title,
      edition: "signature", src: "generated",
      provenance: "signature" === "signature" ? "Signature-original composition" : "original genre study",
      record_kind: RECORD_KIND, ladder_rank: level, genre: GENRE, era: ERA,
      composer: "signature" === "signature" ? "Signature original" : "Original genre study",
      key: key, time_signature: "4/4", tempo_bpm: tempo, bars: bars,
      structure: ["Intro", "A", "B", "A"], notes: notes,
      difficulty: level === "simple" ? "beginner" : (level === "compounded" ? "intermediate" : "advanced"),
      technique: "Play the accompaniment steadily under a stepwise melody, keeping the beat even.",
      body: "<p>A complete generated " + GENRE + " piano song in " + key + ", generated by the seeded generator for this database.</p>" };
    rec.demo = demoFor(rec);
    return rec;
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
    if (!rec || rec.src !== "generated") problems.push("src must be generated");
    if (!rec || rec.bars < 16) problems.push("bars must be >= 16");
    if (!rec || !rec.notes || rec.notes.length < 64) problems.push("notes must be >= 64");
    if (rec && rec.notes) {
      var lh = 0, rh = 0, ok = true;
      rec.notes.forEach(function (n) { if (n[3] === 0) lh++; else rh++; if (n[1] < 21 || n[1] > 108) ok = false; });
      if (lh < 8 || rh < 8) problems.push("both hands need >= 8 notes");
      if (!ok) problems.push("midi out of range");
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
    tests.push({ name: "generated song is complete", pass: !!g && g.bars >= 16 && g.notes.length >= 64 });
    tests.push({ name: "duplicate ids rejected", pass: (function () { var a = generateRecord(7); return a && a.id !== g.id; })() });
    tests.push({ name: "batch throttle", pass: generateBatch(500, 99).length === MAX_BATCH });
    tests.push({ name: "search finds a title", pass: searchRecords(SEED_TITLES[0].slice(0, 4)).length >= 1 });
    tests.push({ name: "hard stop is 10^15", pass: HARD_STOP === 1000000000000000 });
    var passed = tests.filter(function (t) { return t.pass; }).length;
    return { total: tests.length, passed: passed, tests: tests };
  }
  var Tools = { searchRecords: searchRecords, generateRecord: generateRecord, generateBatch: generateBatch, validateRecord: validateRecord, runTests: runTests, slug: SLUG, recordKind: RECORD_KIND, hardStop: HARD_STOP };
  root["PianoSongsSwingSignatureTools"] = Tools;
  if (typeof module !== "undefined" && module.exports) module.exports = Tools;
  if (typeof process !== "undefined" && process.argv) {
    var idx = process.argv.indexOf("--n");
    if (idx !== -1) {
      var n = parseInt(process.argv[idx + 1], 10) || 1;
      generateBatch(n, 1).forEach(function (r) { console.log(JSON.stringify(r)); });
    }
  }
})(typeof window !== "undefined" ? window : globalThis);
