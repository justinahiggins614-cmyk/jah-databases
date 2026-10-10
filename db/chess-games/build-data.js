/* Build data/<slug>/ for the JAH Theater Database: 10,000 full records.
   Usage: node build-data.js [--test]   (--test runs the 40/40 harness only) */
'use strict';
var fs = require('fs'), zlib = require('zlib'), path = require('path');
var GEN = require('./gen-chess-games.js');
var SLUG = GEN.slug, PREFIX = GEN.prefix;
var N = 10000, PER = 100, NCHUNKS = N / PER;

function prng(seed) { var a = (seed >>> 0) || 1; return function () { a |= 0; a = (a + 0x6D2B79F5) | 0; var t = Math.imul(a ^ (a >>> 15), 1 | a); t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t; return ((t ^ (t >>> 14)) >>> 0) / 4294967296; }; }
function deepEqual(a, b) { return JSON.stringify(a) === JSON.stringify(b); }
function chunkName(c) { return 'chunk-' + String(c).padStart(4, '0') + '.jsonl.gz'; }

function harnessTest() {
  var pass = 0, fail = 0, fails = [];
  var seeds = [];
  for (var i = 1; i <= 40; i++) seeds.push(i);
  seeds.forEach(function (seed) {
    var rnd = prng(seed), rec, ok = true, errs = [];
    try { rec = GEN.generate(seed, {}, rnd); } catch (e) { ok = false; errs.push('threw: ' + e.message); }
    if (ok) {
      var v = GEN.validate(rec);
      if (!v.ok) { ok = false; errs = errs.concat(v.errors); }
      // determinism: same seed twice -> identical
      var rec2 = GEN.generate(seed, {}, prng(seed));
      var a = JSON.parse(JSON.stringify(rec)), b = JSON.parse(JSON.stringify(rec2));
      if (!deepEqual(a, b)) { ok = false; errs.push('not deterministic'); }
      // all required fields present and non-empty
      ['id', 'title', 'category', 'record_kind', 'origin', 'summary', 'details', 'sections', 'record_text', 'source_note'].forEach(function (k) {
        if (rec[k] === undefined || rec[k] === null || rec[k] === '') { ok = false; errs.push('empty field ' + k); }
      });
      if (!new RegExp('^' + PREFIX.replace(/-/g, '\\-') + '\\d{7}$').test(rec.id)) { ok = false; errs.push('id format'); }
      if (GEN.categories.indexOf(rec.category) < 0) { ok = false; errs.push('category'); }
    }
    if (ok) pass++; else { fail++; fails.push({ seed: seed, errors: errs }); }
  });
  console.log('HARNESS ' + SLUG + ': ' + pass + '/40 passed' + (fail ? ' FAILS: ' + JSON.stringify(fails).slice(0, 500) : ''));
  return fail === 0;
}

if (process.argv.indexOf('--test') >= 0) { process.exit(harnessTest() ? 0 : 1); }

if (!harnessTest()) { console.error('harness failed; aborting build'); process.exit(1); }

var dataDir = path.join(__dirname, '..', '..', 'data', SLUG);
var chunkDir = path.join(dataDir, 'chunks');
fs.mkdirSync(chunkDir, { recursive: true });

var indexLines = [], chunkBuf = [], chunkNo = 1, catCounts = {}, originCounts = {};
for (var seed = 1; seed <= N; seed++) {
  var rec = GEN.generate(seed, {}, prng(seed));
  var v = GEN.validate(rec);
  if (!v.ok) { console.error('validate failed at seed ' + seed + ': ' + v.errors.join('; ')); process.exit(1); }
  rec._gen_version = GEN.version;
  chunkNo = Math.ceil(seed / PER);
  indexLines.push(JSON.stringify({ id: rec.id, t: rec.title, c: chunkNo, g: rec.category }));
  chunkBuf.push(JSON.stringify(rec));
  catCounts[rec.category] = (catCounts[rec.category] || 0) + 1;
  originCounts[rec.origin] = (originCounts[rec.origin] || 0) + 1;
  if (seed % PER === 0) {
    fs.writeFileSync(path.join(chunkDir, chunkName(chunkNo)), zlib.gzipSync(chunkBuf.join('\n') + '\n'));
    chunkBuf = [];
  }
}
fs.writeFileSync(path.join(dataDir, 'index.jsonl.gz'), zlib.gzipSync(indexLines.join('\n') + '\n'));
console.log('BUILT ' + SLUG + ': ' + indexLines.length + ' index lines, ' + NCHUNKS + ' chunks');
console.log('categories: ' + JSON.stringify(catCounts));
console.log('origins: ' + JSON.stringify(originCounts));

// verify: gunzip+parse all records; chunk<->index ID sets agree
var idxIds = new Set(), chunkIds = new Set();
zlib.gunzipSync(fs.readFileSync(path.join(dataDir, 'index.jsonl.gz'))).toString().split('\n').forEach(function (l) {
  if (l.trim()) idxIds.add(JSON.parse(l).id);
});
for (var c = 1; c <= NCHUNKS; c++) {
  zlib.gunzipSync(fs.readFileSync(path.join(chunkDir, chunkName(c)))).toString().split('\n').forEach(function (l) {
    if (l.trim()) { var r = JSON.parse(l); chunkIds.add(r.id); var vv = GEN.validate(r); if (!vv.ok) { console.error('chunk record invalid ' + r.id); process.exit(1); } }
  });
}
var onlyIdx = [...idxIds].filter(function (x) { return !chunkIds.has(x); });
var onlyChunk = [...chunkIds].filter(function (x) { return !idxIds.has(x); });
console.log('index ids: ' + idxIds.size + ', chunk ids: ' + chunkIds.size + ', mismatch: ' + (onlyIdx.length + onlyChunk.length));
if (idxIds.size !== N || chunkIds.size !== N || onlyIdx.length || onlyChunk.length) { console.error('ID SET MISMATCH'); process.exit(1); }
console.log('VERIFY OK ' + SLUG);
