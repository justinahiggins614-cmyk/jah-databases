/* Group B build harness: builds 10,000 records, tests the generator 40/40,
   writes index.jsonl.gz + 100 chunk files, then verifies everything.
   Usage: node data/<slug>/build.js   (slug taken from the directory name) */
var fs = require('fs'), path = require('path'), zlib = require('zlib');
var dir = __dirname;
var slug = path.basename(dir);
var gen = require(path.join(dir, '..', '..', 'db', slug, 'gen-' + slug + '.js'));
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var N = 10000, PER = 100, NCHUNK = 100;
var REQ = ['id','title','category','record_kind','summary','details','provenance','source'];

/* ---------- 1. harness: 40/40 (fields present, deterministic, valid) ---------- */
var pass = 0, fails = [];
for (var s = 1; s <= 40; s++) {
  var r1 = gen.generate(s, {}, prng(s));
  var r2 = gen.generate(s, {}, prng(s));
  var v = gen.validate(r1);
  var det = JSON.stringify(r1) === JSON.stringify(r2);
  var hasAll = REQ.every(function(k){ return r1[k] !== undefined && r1[k] !== null && r1[k] !== ''; });
  var provOk = (r1.provenance === 'sourced' || r1.provenance === 'signature');
  /* explicit-category path must also validate for a spread of seeds */
  var cats = gen.categories || [];
  var expOk = true;
  for (var ci = 0; ci < cats.length; ci++) {
    var rx = gen.generate(3 + ci * 977, {category: cats[ci]}, prng(3 + ci * 977));
    var vx = gen.validate(rx);
    if (!vx.ok) { expOk = false; fails.push('explicit cat '+cats[ci]+': '+vx.errors.join(',')); break; }
  }
  if (v.ok && det && hasAll && provOk && expOk) pass++;
  else fails.push('seed '+s+': valid='+v.ok+' det='+det+' fields='+hasAll+' prov='+provOk+' errs='+v.errors.join(','));
}
console.log('[' + slug + '] harness: ' + pass + '/40 pass');
if (fails.length) { console.log('FAILURES:\n' + fails.slice(0,10).join('\n')); process.exit(1); }

/* ---------- 2. build ---------- */
var chunksDir = path.join(dir, 'chunks');
fs.mkdirSync(chunksDir, {recursive: true});
var idxLines = [];
var catCount = {}, provCount = {};
for (var chunk = 1; chunk <= NCHUNK; chunk++) {
  var recs = [];
  for (var i = 1; i <= PER; i++) {
    var seed = (chunk - 1) * PER + i;
    var r = gen.generate(seed, {}, prng(seed));
    var vv = gen.validate(r);
    if (!vv.ok) { console.error('INVALID seed ' + seed + ': ' + vv.errors.join(',')); process.exit(1); }
    recs.push(r);
    idxLines.push(JSON.stringify({id: r.id, t: r.title, c: chunk, g: r.category}));
    catCount[r.category] = (catCount[r.category] || 0) + 1;
    provCount[r.provenance] = (provCount[r.provenance] || 0) + 1;
  }
  var cf = path.join(chunksDir, 'chunk-' + String(chunk).padStart(4, '0') + '.jsonl.gz');
  fs.writeFileSync(cf, zlib.gzipSync(recs.map(function(r){ return JSON.stringify(r); }).join('\n')));
}
fs.writeFileSync(path.join(dir, 'index.jsonl.gz'), zlib.gzipSync(idxLines.join('\n')));
console.log('[' + slug + '] wrote index (' + idxLines.length + ' lines) + ' + NCHUNK + ' chunks');
console.log('[' + slug + '] categories: ' + JSON.stringify(catCount));
console.log('[' + slug + '] provenance: ' + JSON.stringify(provCount));

/* ---------- 3. verify ---------- */
var ok = true;
var idxRaw = zlib.gunzipSync(fs.readFileSync(path.join(dir, 'index.jsonl.gz'))).toString().split('\n').filter(Boolean);
if (idxRaw.length !== N) { console.log('INDEX LINE COUNT WRONG: ' + idxRaw.length); ok = false; }
var idxIds = {}, idxCats = {};
idxRaw.forEach(function(l){
  var o;
  try { o = JSON.parse(l); } catch (e) { console.log('INDEX PARSE FAIL'); ok = false; return; }
  if (!o.id || o.t === undefined || !o.c || !o.g) { console.log('INDEX FIELD MISSING', l.slice(0,80)); ok = false; }
  idxIds[o.id] = o.c; idxCats[o.id] = o.g;
});
var nChunkIds = 0;
for (var ch = 1; ch <= NCHUNK; ch++) {
  var cf2 = path.join(chunksDir, 'chunk-' + String(ch).padStart(4, '0') + '.jsonl.gz');
  var lines = zlib.gunzipSync(fs.readFileSync(cf2)).toString().split('\n').filter(Boolean);
  if (lines.length !== PER) { console.log('CHUNK ' + ch + ' HAS ' + lines.length); ok = false; }
  lines.forEach(function(l){
    var o;
    try { o = JSON.parse(l); } catch (e) { console.log('CHUNK PARSE FAIL', ch); ok = false; return; }
    nChunkIds++;
    if (idxIds[o.id] !== ch) { console.log('ID/CHUNK MISMATCH', o.id, 'idx says', idxIds[o.id], 'found in', ch); ok = false; }
    if (idxCats[o.id] !== o.category) { console.log('CATEGORY MISMATCH', o.id); ok = false; }
    var vvv = gen.validate(o);
    if (!vvv.ok) { console.log('STORED RECORD INVALID', o.id, vvv.errors.join(',')); ok = false; }
  });
}
if (Object.keys(idxIds).length !== N) { console.log('INDEX ID UNIQUENESS: ' + Object.keys(idxIds).length); ok = false; }
if (nChunkIds !== N) { console.log('CHUNK ID COUNT: ' + nChunkIds); ok = false; }
console.log('[' + slug + '] verify: ' + (ok ? 'ALL CHECKS PASSED' : 'FAILURES FOUND'));
if (!ok) process.exit(1);
