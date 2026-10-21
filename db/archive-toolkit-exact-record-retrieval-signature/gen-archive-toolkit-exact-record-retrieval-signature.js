(function(){'use strict';
var PREFIX="JAH-ATK201S-";
var METHODS=[["Canonical key resolution", "Map aliases, legacy IDs, and human-readable names to one canonical record key before any fetch, so duplicate identities never split an archive."], ["Primary index lookup", "Hold a primary B-tree or hash index over the canonical key space; a point lookup returns the record location in logarithmic or constant time."], ["Tombstone-aware existence check", "Consult a deletion log before reading storage so removed records report 'gone' instead of silently returning stale bytes."], ["Byte-faithful read path", "Read the record body straight from the content-addressed store and stream it to the caller with no reformatting, truncation, or summarization."], ["Checksum-on-read", "Recompute the stored checksum on every exact read and reject the read if a single byte differs, catching bit-rot at the moment of use."], ["Alias disambiguation", "When several aliases collide, require an explicit disambiguation token rather than guessing which record the caller meant."], ["Version-pinned retrieval", "Accept a version stamp alongside the key so callers can reproduce exactly the bytes a citation pointed at, even after later edits."], ["Snapshot-scoped retrieval", "Scope the lookup to a named archive snapshot so the returned record matches the archive state as of a known instant."], ["Read-path authorization", "Enforce per-record access policy on the exact-read path so private records are never exposed through identifier guessing."], ["Negative caching", "Cache 'not found' results briefly so repeated lookups of missing keys do not hammer the index or storage layer."], ["Key normalization", "Lowercase, trim, and canonicalize keys at ingestion and at query time so the same record is reachable through every spelling variant."], ["Multi-key batch fetch", "Accept a list of keys and return a map key to record, preserving order and reporting per-key misses instead of failing the whole batch."], ["Replica-local reads", "Serve exact reads from the nearest healthy replica, falling back across replicas only when the checksum check fails."], ["Read audit trail", "Log every exact read with key, version, timestamp, and caller identity so citations can be audited years later."], ["Summary-substitution guard", "Reject any code path that would hand back a summary where an exact record was requested, failing loudly instead of silently degrading."]];
var CATS=["keys", "storage", "verification"];
var DEMO="# Exact Record Retrieval demo: canonical-key index, tombstone check, byte-faithful read.\nimport hashlib\nSTORE={\"rec-001\":b\"Title: Solar Sail Propulsion\\nStatus: public draft\\n\",\"rec-002\":b\"Title: Tidal Array Maintenance\\nStatus: public draft\\n\"}\nCHECKS={k:hashlib.sha256(v).hexdigest() for k,v in STORE.items()}\nTOMBSTONES={\"rec-009\"}\nALIASES={\"old-id-1\":\"rec-001\",\"TIDAL\":\"rec-002\"}\ndef canonical(key):\n    key=key.strip().lower()\n    key=ALIASES.get(key,ALIASES.get(key.upper(),key))\n    return key\ndef exact_read(key,version=None):\n    k=canonical(key)\n    if k in TOMBSTONES: return {\"ok\":False,\"reason\":\"tombstoned\"}\n    if k not in STORE: return {\"ok\":False,\"reason\":\"not found\"}\n    body=STORE[k]\n    if hashlib.sha256(body).hexdigest()!=CHECKS[k]: return {\"ok\":False,\"reason\":\"checksum mismatch\"}\n    return {\"ok\":True,\"key\":k,\"bytes\":len(body),\"body\":body.decode()}\nfor q in [\"rec-001\",\"OLD-ID-1\",\" rec-002 \",\"rec-009\",\"rec-404\"]:\n    r=exact_read(q); print(q,\"->\",r[\"ok\"],r.get(\"key\",r.get(\"reason\")))\n";
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function generate(seed,opts){
  opts=opts||{};var rnd=prng(seed);
  var idx=(seed-1)%METHODS.length;var m=METHODS[idx];
  var cat=opts.category||CATS[(rnd()*CATS.length)|0];
  var id=PREFIX+String(1000+((seed-1)%9000));
  var title=m[0]+' \u2014 '+"Exact Record Retrieval (Signature)";
  return {id:id,t:title,title:title,description:"Signature edition. Exact record retrieval is the discipline of returning precisely the record a caller asked for \u2014 by primary key, canonical identifier, or stable locator \u2014 and refusing to substitute a summary, a near-match, or a regenerated approximation. In near-boundless archives, summaries drift from sources; the exact-record contract keeps citations grounded, reproducible, and legally defensible. The technique ",
    kind:"retrieval tool",category:cat,ladder_rank:1+((seed-1)%3),demo:DEMO,
    provenance:"Signature-generated-completion",last_verified:'2026-10-21',src:"signature-generated-completion",_seed:seed};
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(typeof r.id!=='string'||r.id.indexOf(PREFIX)!==0)e.push('id');
  if(typeof r.title!=='string'||!r.title.length)e.push('title');
  if(typeof r.description!=='string'||r.description.length<100)e.push('description');
  if(CATS.indexOf(r.category)<0)e.push('category');
  if(!(r.ladder_rank>=1&&r.ladder_rank<=3))e.push('ladder_rank');
  if(typeof r.demo!=='string'||r.demo.indexOf('print(')<0)e.push('demo');
  if(r.src!=="signature-generated-completion")e.push('src');
  return {ok:!e.length,errors:e};
}
var gen={version:"jahdb-archive-toolkit-exact-record-retrieval-signature-1.0",generate:generate,validate:validate};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("archive-toolkit-exact-record-retrieval-signature",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();