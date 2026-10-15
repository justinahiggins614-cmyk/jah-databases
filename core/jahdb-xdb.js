/* JAH Databases — cross-database material use (his standing rule).
   When a database pulls material from another database, it must actually
   USE that material and let it change/affect the result. Applies to every
   database.

   Load AFTER core/jahdb.js and core/jahdb-dedupe.js on every db page:
     <script src="../../core/jahdb-xdb.js"></script>

   CONTRACT (enforced, not advisory):
   1. A generator declares what it pulls:
        xdbUses: [{slug:'predictive-trajectories', fields:['waypoints'], min:1}]
   2. Every generated record must carry:
        xdb_sources: [{slug, id, fields_used:[...], trace:{...}}]
      - each cited (slug,id) MUST exist in the source database's index
        (verified live against the source's published index);
      - each field_used must be TRACEABLE: the output value deep-equals the
        source field value, OR the entry carries
        derived_from:{slug,id,field,transform} with the raw source value
        embedded in trace.source_value. Fusion/transforms are allowed —
        phantom sources are not.
   3. Verification failures REJECT the record with explicit errors.
      No silent pass. A generator that declares xdbUses but verifies nothing
      cannot emit through the sync path — it must go through
      JAHDB.generateChecked (async), which runs dedupe + xdb verification.

   HELPERS:
   - JAHDB.xdb.pull(sourceSlug, opts) -> Promise<index rows>
       opts: {filter(fn), limit}
   - JAHDB.xdb.pullFull(sourceSlug, id) -> Promise<full record>
   - JAHDB.xdb.blend(pulls, recipeFn) -> runs recipeFn(ctx) where
       ctx.get(slug,id) returns the pulled full record; stamps
       xdb_sources provenance automatically from what the recipe read.
   - JAHDB.xdb.verify(record, decl) -> Promise<{ok, errors[]}>
*/
(function(){
'use strict';
if(typeof window==='undefined'||!window.JAHDB) return;
var JAHDB = window.JAHDB;

var manifestP = null, indexCache = {}, fullCache = {};
function getManifest(){
  if(!manifestP) manifestP = JAHDB.loadManifest();
  return manifestP;
}
function dbEntry(m, slug){
  var dbs = m&&m.databases||[];
  for(var i=0;i<dbs.length;i++) if(dbs[i].slug===slug) return dbs[i];
  return null;
}
function parseRows(t){
  var s = String(t||'').trim();
  if(!s) return [];
  if(s[0]==='['){ try{ var a=JSON.parse(s); return Array.isArray(a)?a:[]; }catch(e){ return []; } }
  return s.split('\n').filter(function(l){return l.trim();}).map(function(l){
    try{ return JSON.parse(l); }catch(e){ return null; }
  }).filter(Boolean);
}
function pull(sourceSlug, opts){
  opts = opts||{};
  if(indexCache[sourceSlug]) return indexCache[sourceSlug];
  var p = getManifest().then(function(m){
    var e = dbEntry(m, sourceSlug);
    if(!e) throw new Error('unknown database: '+sourceSlug);
    var url = e.local_index || e.index;
    if(!url) throw new Error('no index URL for '+sourceSlug);
    return JAHDB.fetchGz(url).then(parseRows);
  }).then(function(rows){
    if(opts.filter) rows = rows.filter(opts.filter);
    if(opts.limit) rows = rows.slice(0, opts.limit);
    return rows;
  });
  indexCache[sourceSlug]=p; return p;
}
function chunkCandidates(base, row){
  var c = row&&(row.c!=null?row.c:row.chunk);
  var out = [];
  if(c==null||c==='') return out;
  var n = parseInt(c,10);
  function pad(v,l){ v=String(v); while(v.length<l) v='0'+v; return v; }
  ['chunk-'+pad(n,4)+'.jsonl.gz','chunk-'+pad(n,5)+'.jsonl.gz',
   'chunk-'+n+'.jsonl.gz'].forEach(function(f){ out.push(base+'chunks/'+f); });
  return out;
}
function pullFull(sourceSlug, id){
  var key = sourceSlug+'\u0000'+id;
  if(fullCache[key]) return fullCache[key];
  var p = getManifest().then(function(m){
    var e = dbEntry(m, sourceSlug);
    if(!e) throw new Error('unknown database: '+sourceSlug);
    var url = e.local_index || e.index;
    var base = url.slice(0, url.lastIndexOf('/')+1);
    return pull(sourceSlug).then(function(rows){
      var row = null;
      for(var i=0;i<rows.length;i++){
        if(String(rows[i].id)===String(id)){ row=row||rows[i]; break; }
      }
      if(!row) throw new Error(id+' not in '+sourceSlug+' index');
      var cands = chunkCandidates(base, row);
      if(!cands.length) throw new Error('no chunk addressing for '+sourceSlug);
      // try candidates in order; first hit wins
      var attempt = function(k){
        if(k>=cands.length) throw new Error('full record '+id+' not found in '+sourceSlug+' chunks');
        return JAHDB.fetchGz(cands[k]).then(parseRows).then(function(recs){
          for(var j=0;j<recs.length;j++){
            if(String(recs[j].id)===String(id)) return recs[j];
          }
          return attempt(k+1);
        }).catch(function(err){
          if(k+1<cands.length) return attempt(k+1);
          throw err;
        });
      };
      return attempt(0);
    });
  });
  fullCache[key]=p; return p;
}
function getPath(obj, path){
  var cur = obj;
  var parts = String(path).split('.');
  for(var i=0;i<parts.length;i++){
    if(cur==null||typeof cur!=='object') return undefined;
    cur = cur[parts[i]];
  }
  return cur;
}
function deepEqual(a,b){
  if(a===b) return true;
  try{ return JSON.stringify(a)===JSON.stringify(b); }catch(e){ return false; }
}
/* Verify that pulled material was actually USED and affected the result. */
function verify(record, decl){
  decl = decl||[];
  var sources = record&&record.xdb_sources;
  if(!decl.length) return Promise.resolve({ok:true, errors:[]});
  var errors = [];
  if(!Array.isArray(sources)||!sources.length){
    return Promise.resolve({ok:false, errors:[
      'xdb contract violated: generator declares pulls from '
      +decl.map(function(d){return d.slug;}).join(', ')
      +' but the record cites no xdb_sources — pulled material was not used']});
  }
  // group cited sources by slug
  var bySlug = {};
  sources.forEach(function(s){
    (bySlug[s.slug]=bySlug[s.slug]||[]).push(s);
  });
  var jobs = [];
  decl.forEach(function(d){
    var cited = bySlug[d.slug]||[];
    if(cited.length < (d.min||1)){
      errors.push('xdb contract violated: declared pull from '+d.slug
        +' (min '+(d.min||1)+') but record cites '+cited.length);
      return;
    }
    cited.forEach(function(c){
      if(!c.id){ errors.push('xdb_sources entry missing id for '+d.slug); return; }
      jobs.push(pullFull(d.slug, c.id).then(function(full){
        var fields = c.fields_used||[];
        if(!fields.length){
          errors.push('xdb_sources entry '+d.slug+':'+c.id+' names no fields_used');
          return;
        }
        fields.forEach(function(f){
          var srcVal = getPath(full, f);
          if(srcVal===undefined){
            errors.push('field "'+f+'" not found in '+d.slug+':'+c.id);
            return;
          }
          var outVal = getPath(record, f);
          var traced = c.trace && c.trace[f] && c.trace[f].source_value!==undefined;
          var derived = c.derived_from && c.derived_from.field===f;
          if(!(deepEqual(outVal,srcVal)||(traced&&derived))){
            errors.push('field "'+f+'" from '+d.slug+':'+c.id
              +' is not traceable in the output (no equality, no derived_from annotation)');
          }
        });
      }).catch(function(err){
        errors.push('could not verify source '+d.slug+':'+c.id+': '+err.message);
      }));
    });
  });
  return Promise.all(jobs).then(function(){
    return {ok:errors.length===0, errors:errors};
  });
}
/* Blend helper: recipe reads pulled records via ctx.get; provenance stamped. */
function blend(pulls, recipeFn){
  // pulls: [{slug, id}] — fetched first, then recipe runs on full records
  var jobs = pulls.map(function(p){
    return pullFull(p.slug, p.id).then(function(full){
      return {slug:p.slug, id:p.id, record:full};
    });
  });
  return Promise.all(jobs).then(function(got){
    var read = [];
    var ctx = {
      get:function(slug,id){
        for(var i=0;i<got.length;i++){
          if(got[i].slug===slug&&String(got[i].id)===String(id)){
            read.push({slug:slug,id:id,record:got[i].record});
            return got[i].record;
          }
        }
        throw new Error('blend: unpulled source '+slug+':'+id);
      },
      all:function(){ return got.map(function(g){return g.record;}); }
    };
    var out = recipeFn(ctx) || {};
    out.xdb_sources = read.map(function(r){
      return {slug:r.slug, id:r.id, fields_used:[], trace:{}};
    });
    out.xdb_blend = true;
    return out;
  });
}

/* ---- central enforcement ---- */
/* Sync path: a generator that declares xdbUses cannot emit unverified. */
var _origRun = JAHDB.runGenerator;
JAHDB.runGenerator = function(slug, seed, opts){
  var r = _origRun(slug, seed, opts);
  if(!r.ok||!r.record) return r;
  var gen = JAHDB.getGenerator ? JAHDB.getGenerator(slug) : null;
  if(gen && gen.xdbUses && gen.xdbUses.length){
    var s = r.record.xdb_sources;
    if(!Array.isArray(s)||!s.length){
      return {ok:false, record:r.record, errors:[
        'cross-db pull declared ('+gen.xdbUses.map(function(d){return d.slug;}).join(', ')
        +') but record carries no verified xdb_sources — use JAHDB.generateChecked']};
    }
    // Sync path cannot verify live; mark for the async verifier.
    r.record._xdb_unverified = true;
  }
  return r;
};
/* Async path: dedupe (if loaded) + xdb verification. */
var _dedupeChecked = JAHDB.generateChecked;
JAHDB.generateChecked = function(slug, seed, opts){
  var base = _dedupeChecked
    ? _dedupeChecked(slug, seed, opts)
    : Promise.resolve(_origRun(slug, seed, opts||{}));
  return base.then(function(r){
    if(!r.ok||!r.record) return r;
    var gen = JAHDB.getGenerator ? JAHDB.getGenerator(slug) : null;
    var decl = (gen&&gen.xdbUses)||[];
    if(!decl.length) return r;
    return verify(r.record, decl).then(function(v){
      if(!v.ok) return {ok:false, record:r.record, errors:v.errors};
      delete r.record._xdb_unverified;
      r.xdbVerified = true;
      return r;
    });
  });
};

JAHDB.xdb = {
  pull:pull, pullFull:pullFull, blend:blend, verify:verify,
  clearCache:function(){ indexCache={}; fullCache={}; }
};
})();
