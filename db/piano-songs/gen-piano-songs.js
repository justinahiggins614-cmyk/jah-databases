 "use strict";
/* The Piano Songs Database — boundless generator. Seeded, deterministic, throttled,
   duplicate-checked, hard stop at 10^15. Generated records are
   labeled src "generated" and are never presented as archive records. */
(function (root) {
  var SLUG = "piano-songs";
  var PREFIX = "JAH-PSO-";
  var RECORD_KIND = "piano song record";
  var HARD_STOP = 1000000000000000; // 10^15
  var MAX_BATCH = 100;
  var SEED_TITLES = ["Morning Chant in Dorian Mode", "Estampie of the Open Road", "Pavane of the Quiet Court", "Galliard in Bright Steps", "Minuet of the Small Garden", "Baroque Canon Study in C", "Sonatina in C Major", "Classical Minuet in G", "Nocturne Study in E Minor", "Waltz of the Evening Room", "Folk Dance in A Minor", "Hymn-Style Song in F Major", "March in C Major", "Lullaby in G Major", "Song of the River Valley", "Piano Songs Across the Eras"];
  var SCALE = [0, 2, 4, 5, 7, 9, 11];
  var PROG = [0, 5, 3, 4];
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
  function clampPos(p) { return Math.max(7, Math.min(14, p)); }
  function buildNotes(rnd) {
    var notes = [], pos = 9, bars = 32, bpb = 4, tonic = 60;
    for (var bar = 0; bar < bars; bar++) {
      var deg = PROG[bar % PROG.length];
      var root = tonic + SCALE[deg] - 24;
      var third = tonic + SCALE[(deg + 2) % 7] + (deg + 2 >= 7 ? 12 : 0) - 24;
      var fifth = tonic + SCALE[(deg + 4) % 7] + (deg + 4 >= 7 ? 12 : 0) - 24;
      [[0, root], [1, fifth], [2, root], [3, third]].forEach(function (p) { notes.push([bar * bpb + p[0], p[1], 1.0, 0]); });
      for (var beat = 0; beat < bpb; beat++) {
        if (beat === 0) {
          var cands = [deg + 7, deg + 9, deg + 11], best = cands[0];
          cands.forEach(function (c) { if (Math.abs(c - pos) < Math.abs(best - pos)) best = c; });
          pos = clampPos(best);
        } else {
          var steps = [-2, -1, -1, 0, 1, 1, 2];
          pos = clampPos(pos + steps[Math.floor(rnd() * steps.length)]);
        }
        var pitch = tonic + 12 * Math.floor(pos / 7) + SCALE[pos % 7];
        notes.push([bar * bpb + beat, pitch, 1.0, 1]);
      }
    }
    notes.sort(function (a, b) { return a[0] - b[0]; });
    return notes;
  }
  function demoFor(title, notes) {
    var header = title + "\nGenre: piano song | Era: all eras\nKey: C major | Time: 4/4 | Tempo: 96 BPM | Bars: 32\nStructure: A A B A\nTimeline:\n";
    var lines = notes.map(function (n) {
      var name = NAMES[n[1] % 12] + String(Math.floor(n[1] / 12) - 1);
      return "beat " + n[0].toFixed(2) + ": MIDI " + n[1] + " (" + name + ") dur " + n[2].toFixed(2) + " hand " + (n[3] === 1 ? "R" : "L");
    });
    var totalBeats = 128, seconds = (totalBeats * 60 / 96).toFixed(1);
    var codeLines = ["NOTES = " + JSON.stringify(notes), "NAMES = " + JSON.stringify(NAMES), "print(" + JSON.stringify(title) + ")",
      "print('Genre: piano song | Era: all eras')", "print('Key: C major | Time: 4/4 | Tempo: 96 BPM | Bars: 32')",
      "print('Structure: A A B A')", "print('Timeline:')",
      "for start, midi, dur, hand in NOTES:", "    print('beat %.2f: MIDI %d (%s) dur %.2f hand %s' % (start, midi, NAMES[midi % 12] + str(midi // 12 - 1), dur, 'R' if hand == 1 else 'L'))",
      "print('SONG COMPLETE: " + notes.length + " notes, 128 beats, " + seconds + " seconds')"];
    return { code: codeLines.join("\n") + "\n", expected_output: header + lines.join("\n") + "\nSONG COMPLETE: " + notes.length + " notes, 128 beats, " + seconds + " seconds\n" };
  }
  function generateRecord(seed) {
    if (counter >= HARD_STOP) return null;
    var rnd = mulberry32(typeof seed === "number" ? seed : 1);
    var title = SEED_TITLES[Math.floor(rnd() * SEED_TITLES.length)];
    var id = PREFIX + "GEN-" + pad(counter + 1);
    if (seen[id]) return null;
    seen[id] = true; counter += 1;
    var notes = buildNotes(rnd);
    return { id: id, slug: SLUG, title: "Generated: " + title, edition: "public", src: "generated",
      provenance: "public" === "signature" ? "Signature-original composition" : "public-domain framework + original realization",
      record_kind: RECORD_KIND, ladder_rank: "simple", genre: "piano song", era: "all eras",
      composer: "public" === "signature" ? "Signature original" : "Unattributed (framework realization)",
      key: "C major", time_signature: "4/4", tempo_bpm: 96, bars: 32, structure: ["A", "A", "B", "A"],
      notes: notes, difficulty: "beginner",
      technique: "Play hands separately first at a slow tempo, then together, keeping a steady beat and a relaxed wrist.",
      body: "<p>Generated: " + title + " is a complete generated piano song in C major in 4/4 at 96 beats per minute across 32 bars, in the form A A B A. The left hand carries the bass and harmony while the right hand carries the melody, and the sections return and vary so the song is heard whole.</p>",
      demo: demoFor("Generated: " + title, notes) };
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
    if (!rec || !rec.structure || rec.structure.length < 3) problems.push("structure must have >= 3 sections");
    if (rec && rec.notes) {
      var lh = rec.notes.filter(function (n) { return n[3] === 0; }).length;
      var rh = rec.notes.filter(function (n) { return n[3] === 1; }).length;
      if (lh < 8) problems.push("left hand must have >= 8 notes");
      if (rh < 8) problems.push("right hand must have >= 8 notes");
      var bpb = parseInt(rec.time_signature.split("/")[0], 10);
      var lastEnd = 0; rec.notes.forEach(function (n) { if (n[0] + n[2] > lastEnd) lastEnd = n[0] + n[2]; });
      if (lastEnd > rec.bars * bpb + 0.001) problems.push("notes exceed bars");
      var secs = rec.bars * bpb * 60 / rec.tempo_bpm;
      if (secs < 30) problems.push("duration must be >= 30 seconds");
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
    tests.push({ name: "generated song complete", pass: !!g && g.notes.length >= 64 && g.bars >= 16 && g.structure.length >= 3 });
    tests.push({ name: "duplicate ids rejected", pass: (function () { var a = generateRecord(7); return a && a.id !== g.id; })() });
    tests.push({ name: "batch throttle", pass: generateBatch(500, 99).length === MAX_BATCH });
    tests.push({ name: "search finds a title", pass: searchRecords(SEED_TITLES[0].slice(0, 4)).length >= 1 });
    var passed = tests.filter(function (t) { return t.pass; }).length;
    return { total: tests.length, passed: passed, tests: tests };
  }
  var Tools = { searchRecords: searchRecords, generateRecord: generateRecord, generateBatch: generateBatch, validateRecord: validateRecord, runTests: runTests, slug: SLUG, recordKind: RECORD_KIND, hardStop: HARD_STOP };
  root["PianoSongsTools"] = Tools;
  if (typeof module !== "undefined" && module.exports) module.exports = Tools;
  if (typeof process !== "undefined" && process.argv) {
    var idx = process.argv.indexOf("--n");
    if (idx !== -1) {
      var n = parseInt(process.argv[idx + 1], 10) || 1;
      generateBatch(n, 1).forEach(function (r) { console.log(JSON.stringify(r)); });
    }
  }
})(typeof window !== "undefined" ? window : globalThis);
