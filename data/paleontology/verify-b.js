/* Group B final verification: syntax, no-website-refs, fetch paths, data integrity */
var fs = require('fs'), path = require('path'), zlib = require('zlib');
var cp = require('child_process');
var base = '/home/hatch/workspace/jah-databases-new18';
var slugs = ['paleontology','sociology','parenting','pets','photography','publishing'];
var failures = [];
function fail(m){ failures.push(m); console.log('FAIL: ' + m); }

/* 1. node --check every JS file we wrote */
slugs.forEach(function(slug){
  ['db/'+slug+'/gen-'+slug+'.js', 'data/'+slug+'/build.js'].forEach(function(f){
    var r = cp.spawnSync('node', ['--check', path.join(base, f)]);
    if (r.status !== 0) fail('syntax ' + f + ': ' + r.stderr.toString().slice(0,200));
  });
  /* extract inline page script and syntax-check it */
  var html = fs.readFileSync(path.join(base, 'db/'+slug+'/index.html'), 'utf8');
  var m = html.match(/<script>\n\(function\(\)\{[\s\S]*?<\/script>/);
  if (!m) { fail('no inline script found in ' + slug); return; }
  var js = m[0].replace(/^<script>/,'').replace(/<\/script>$/,'');
  var tmp = '/tmp/verify-inline-' + slug + '.js';
  fs.writeFileSync(tmp, js);
  var r2 = cp.spawnSync('node', ['--check', tmp]);
  if (r2.status !== 0) fail('inline JS syntax ' + slug + ': ' + r2.stderr.toString().slice(0,300));
});

/* 2. zero website references in pages */
var badRe = /website|https?:\/\/|www\.|[a-z0-9]\.com\b|\.org\b|\.net\b|\.io\b/i;
slugs.forEach(function(slug){
  var html = fs.readFileSync(path.join(base, 'db/'+slug+'/index.html'), 'utf8');
  var lines = html.split('\n');
  lines.forEach(function(line, i){
    if (line.indexOf('application/ld+json') >= 0) return; /* template-parity schema.org JSON-LD only */
    if (badRe.test(line)) fail('website-ref in ' + slug + ' line ' + (i+1) + ': ' + line.trim().slice(0,100));
  });
});
/* also check gen files for website refs */
slugs.forEach(function(slug){
  var js = fs.readFileSync(path.join(base, 'db/'+slug+'/gen-'+slug+'.js'), 'utf8');
  if (badRe.test(js)) fail('website-ref in gen-' + slug + '.js');
});

/* 3. every fetch path in pages resolves to a real file */
slugs.forEach(function(slug){
  var pageDir = path.join(base, 'db', slug);
  var html = fs.readFileSync(path.join(pageDir, 'index.html'), 'utf8');
  var need = [
    '../../core/jahdb.js', '../../core/standard-1.0.js', '../../core/guide-conv.js', '../../core/apex-2.0.js',
    'gen-'+slug+'.js',
    '../../data/'+slug+'/index.jsonl.gz',
    '../../data/manifest.json'
  ];
  need.forEach(function(rel){
    var abs = path.resolve(pageDir, rel);
    if (!fs.existsSync(abs)) fail('missing fetch target for ' + slug + ': ' + rel);
  });
  for (var c = 1; c <= 100; c++) {
    var cf = path.join(base, 'data', slug, 'chunks', 'chunk-' + String(c).padStart(4,'0') + '.jsonl.gz');
    if (!fs.existsSync(cf)) { fail('missing chunk ' + slug + ' ' + c); break; }
  }
});

/* 4. data integrity re-verified from disk (independent of build.js) */
slugs.forEach(function(slug){
  var dir = path.join(base, 'data', slug);
  var idx = zlib.gunzipSync(fs.readFileSync(path.join(dir, 'index.jsonl.gz'))).toString().split('\n').filter(Boolean);
  if (idx.length !== 10000) fail(slug + ' index lines = ' + idx.length);
  var ids = {}, nChunk = 0, cats = {};
  idx.forEach(function(l){
    var o = JSON.parse(l);
    if (!o.id || o.t === undefined || !o.c || !o.g) fail(slug + ' index field missing');
    ids[o.id] = o.c; cats[o.g] = (cats[o.g]||0)+1;
  });
  for (var c = 1; c <= 100; c++) {
    var lines = zlib.gunzipSync(fs.readFileSync(path.join(dir, 'chunks', 'chunk-' + String(c).padStart(4,'0') + '.jsonl.gz'))).toString().split('\n').filter(Boolean);
    if (lines.length !== 100) fail(slug + ' chunk ' + c + ' lines = ' + lines.length);
    lines.forEach(function(l){
      var o = JSON.parse(l); nChunk++;
      if (ids[o.id] !== c) fail(slug + ' id/chunk mismatch ' + o.id);
      if (cats[o.category] === undefined) fail(slug + ' chunk category not in index: ' + o.category);
      if (typeof o.summary !== 'string' || o.summary.length < 80) fail(slug + ' short summary ' + o.id);
      if (o.provenance !== 'sourced' && o.provenance !== 'signature') fail(slug + ' bad provenance ' + o.id);
    });
  }
  if (Object.keys(ids).length !== 10000) fail(slug + ' index unique ids = ' + Object.keys(ids).length);
  if (nChunk !== 10000) fail(slug + ' chunk total = ' + nChunk);
  console.log(slug + ': index=10000 chunks=100x100 cats=' + Object.keys(cats).length);
});

console.log(failures.length ? ('\n' + failures.length + ' FAILURES') : '\nALL VERIFICATIONS PASSED');
process.exit(failures.length ? 1 : 0);
