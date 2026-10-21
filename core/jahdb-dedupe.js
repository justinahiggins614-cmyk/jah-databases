/* JAH Databases — whole-system duplicate check (his standing rule).
   Every generator must check the WHOLE system before generating.
   No time limit; correctness first.

   Load AFTER core/jahdb.js on every db page:
     <script src="../../core/jahdb-dedupe.js"></script>

   What it does:
   1. Wraps JAHDB.runGenerator with an EXACT same-database title check
      (synchronous, zero network — the page already holds archiveIdx).
      Intra-database duplicates are rejected on the spot.
   2. Provides JAHDB.generateChecked(slug, seed, opts) — async. Generates,
      then checks the whole system: same-db exact set + the global dedupe
      index (bloom shards, then exact shard on a bloom hit). On a duplicate
      it reseeds and retries (up to 200 attempts); if it cannot produce a
      unique title it FAILS HONESTLY instead of emitting a duplicate.
      If the global index is unreachable, uniqueness cannot be established
      and generation FAILS CLOSED — it refuses to emit the record unchecked
      rather than treating "unknown" as "not a duplicate".
   3. JAHDB.dedupe.checkTitle(title) -> Promise<{dupe, hits, checked}> for
      direct use.

   Dedupe index layout (built by code/build_global_dedupe.py, published
   under the data-1 shard):
     data/dedupe/bloom/<xx>.json.gz  — per-hash-prefix Bloom filter
     data/dedupe/exact/<xx>.json.gz  — per-hash-prefix exact map
     data/dedupe/manifest.json       — build metadata
   <xx> = first byte of the 64-bit FNV-1a hash of the normalized title.

   Normalization + hashing MUST match code/build_global_dedupe.py exactly:
   NFKD -> strip combining marks -> lowercase -> keep [a-z0-9] ->
   collapse whitespace -> trim -> UTF-16 code units -> FNV-1a 64.
   Self-test vector: FNV-1a64("foobar") = 85944171f73967e8.
*/
(function(){
'use strict';
if(typeof window==='undefined'||!window.JAHDB) return;
var JAHDB = window.JAHDB;

var DEDUPE_BASE = 'https://justinahiggins614-cmyk.github.io/jah-databases-data-1/data/dedupe/';
var MAX_TRIES = 200;

/* ---------- normalization + hashing (mirror of build_global_dedupe.py) ---------- */
function normTitle(t){
  var s = String(t==null?'':t);
  try{ s = s.normalize('NFKD').replace(/[\u0300-\u036f]/g,''); }
  catch(e){}
  s = s.toLowerCase().replace(/[^a-z0-9]+/g,' ').replace(/\s+/g,' ').trim();
  return s;
}
function fnv1a64hex(s){
  var h = 0xcbf29ce484222325n, p = 0x100000001b3n, mask = 0xffffffffffffffffn;
  for(var i=0;i<s.length;i++){ h ^= BigInt(s.charCodeAt(i)); h = (h*p)&mask; }
  return h.toString(16).padStart(16,'0');
}
function hashTitle(t){ return fnv1a64hex(normTitle(t)); }
function shardOf(hashHex){ return hashHex.slice(0,2); }

/* ---------- same-database exact set (built from the page's archiveIdx) ---------- */
var sameDbTitles = null;   // Set of normalized titles, or null if not indexed
var sameDbSlug = null;
function indexSameDb(rows, slug){
  sameDbTitles = new Set();
  (rows||[]).forEach(function(r){
    var t = r&&(r.t||r.title||r.name);
    if(t) sameDbTitles.add(normTitle(t));
  });
  sameDbSlug = slug||null;
}
function sameDbHas(title){ return !!(sameDbTitles && sameDbTitles.has(normTitle(title))); }

/* ---------- global index fetch (bloom, then exact on hit) ---------- */
var bloomCache = {}, exactCache = {};
function fetchGzJson(url){
  return JAHDB.fetchGz(url).then(function(t){ return JSON.parse(t); });
}
function getBloom(xx){
  if(bloomCache[xx]) return bloomCache[xx];
  var p = fetchGzJson(DEDUPE_BASE+'bloom/'+xx+'.json.gz').catch(function(){ return null; });
  bloomCache[xx]=p; return p;
}
function getExact(xx){
  if(exactCache[xx]) return exactCache[xx];
  var p = fetchGzJson(DEDUPE_BASE+'exact/'+xx+'.json.gz').catch(function(){ return null; });
  exactCache[xx]=p; return p;
}
/* Bloom check, mirroring build_global_dedupe.py: k indices via double hashing. */
function bloomHas(bloom, hashHex){
  if(!bloom||!bloom.bits) return false;
  var h1 = BigInt('0x'+hashHex), mask = 0xffffffffffffffffn;
  var h2 = (h1 ^ 0x9e3779b97f4a7c15n) & mask;
  var m = bloom.m, k = bloom.k;
  if(!bloom._bytes){
    var bin = atob(bloom.bits), arr = new Uint8Array(bin.length);
    for(var j=0;j<bin.length;j++) arr[j]=bin.charCodeAt(j);
    bloom._bytes = arr;
  }
  var bytes = bloom._bytes;
  var bigM = BigInt(m);
  for(var i=0;i<k;i++){
    // NOTE: modulo in BigInt first — Number() of a 64-bit value loses
    // precision, which would address the wrong bits. Must mirror
    // build_global_dedupe.py exactly.
    var idx = Number(((h1 + BigInt(i)*h2) & mask) % bigM);
    if(!(bytes[idx>>3] & (1<<(idx&7)))) return false;
  }
  return true;
}
function checkTitle(title){
  var h = hashTitle(title), xx = shardOf(h);
  return getBloom(xx).then(function(bloom){
    /* FAIL CLOSED: if the global index cannot be fetched, uniqueness cannot
       be established — report dupe:null/checked:'failed', never dupe:false.
       Callers (generateChecked) must refuse to file unchecked records. */
    if(!bloom) return {dupe:null, hits:null, checked:'failed', error:'global dedupe bloom shard "'+xx+'" could not be fetched — uniqueness unverifiable'};
    if(!bloomHas(bloom,h)) return {dupe:false, hits:null, checked:'bloom'};
    return getExact(xx).then(function(exact){
      if(!exact||!exact.m) return {dupe:true, hits:null, checked:'bloom-only'};
      var hits = exact.m[h]||[];
      return {dupe:hits.length>0, hits:hits, checked:'exact'};
    });
  });
}

/* ---------- central enforcement: wrap runGenerator (same-db exact) ----------
   Batch-uniqueness: a title that passes is ADMITTED to the session set, so a
   later record in the same generation batch cannot repeat it (previously only
   generateChecked admitted, leaving the sync path batch-blind). The check is
   slug-aware: it only applies when the set belongs to the slug being
   generated, so cross-slug harnesses never false-reject. */
var origRunGenerator = JAHDB.runGenerator;
function titleOf(rec){ return rec&&(rec.title||rec.t||rec.name||''); }
JAHDB.runGenerator = function(slug, seed, opts){
  var r = origRunGenerator(slug, seed, opts);
  if(r.ok && r.record && sameDbTitles && (!sameDbSlug || sameDbSlug === slug)){
    var t = titleOf(r.record);
    if(t){
      if(sameDbHas(t)){
        return {ok:false, errors:['duplicate title already in this database archive: "'+t+'"'], record:r.record};
      }
      try{ sameDbTitles.add(normTitle(t)); }catch(e){}
    }
  }
  return r;
};

/* ---------- async whole-system checked generation ---------- */
function sleep(ms){ return new Promise(function(res){ setTimeout(res, ms); }); }
JAHDB.generateChecked = function(slug, seed, opts){
  opts = opts||{};
  var attempt = 0, s = seed;
  function attemptOnce(){
    attempt++;
    var r = JAHDB.runGenerator(slug, s, opts); // includes same-db exact check
    if(!r.ok){
      // A same-db duplicate rejection from the wrapper: reseed and retry.
      if(attempt<MAX_TRIES && /duplicate title already in this database/.test((r.errors||[]).join(' '))){
        s = (typeof s==='number')? s+1 : s+'#'+attempt;
        return sleep(0).then(attemptOnce);
      }
      return Promise.resolve(r);
    }
    var t = titleOf(r.record);
    if(!t) return Promise.resolve(r);
    return checkTitle(t).then(function(chk){
      /* FAIL CLOSED: when the global index is unreachable, uniqueness cannot
         be established — refuse to emit the record rather than filing it
         unchecked (the old code treated this as "not a duplicate"). */
      if(chk.checked === 'failed'){
        return {ok:false, errors:['whole-system duplicate check FAILED for "'+t+'" — uniqueness cannot be established ('+(chk.error||'dedupe index unreachable')+'). Refusing to generate unchecked.'], record:r.record};
      }
      if(chk.dupe){
        if(attempt<MAX_TRIES){
          s = (typeof s==='number')? s+1 : s+'#'+attempt;
          return sleep(0).then(attemptOnce);
        }
        var where = (chk.hits||[]).map(function(h){return h[0]+':'+h[1];}).join(', ');
        return {ok:false, errors:['whole-system duplicate: "'+t+'" already exists'
          +(where?' in '+where:'')+'. Could not produce a unique title in '+MAX_TRIES
          +' attempts — the system already covers this. Try different options.'],
          record:r.record};
      }
      // New title: admit it to the same-db set so a batch can't dupe itself.
      if(sameDbTitles) sameDbTitles.add(normTitle(t));
      r.dedupeChecked = chk.checked;
      return r;
    });
  }
  return attemptOnce();
};

JAHDB.dedupe = {
  normTitle:normTitle, hashTitle:hashTitle, shardOf:shardOf,
  indexSameDb:indexSameDb, sameDbHas:sameDbHas,
  checkTitle:checkTitle, warmShard:function(xx){ getBloom(xx); },
  MAX_TRIES:MAX_TRIES,
  selfTest:function(){
    return fnv1a64hex('foobar')==='85944171f73967e8'
        && normTitle('  Hello, World!  ')==='hello world';
  }
};
})();
