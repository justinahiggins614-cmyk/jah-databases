(function(){'use strict';
var PREFIX="JAH-ATK202-";
var METHODS=[["Projection pushdown", "Push the field list into the storage engine so unrequested columns are never read from disk, not merely dropped before serialization."], ["Declared field schema", "Publish a schema of every field with type and sensitivity so callers request by name and validators can reject unknown fields."], ["Nested path selection", "Support dotted paths like author.name so callers can reach into nested structures without fetching the whole subtree."], ["Field-level access control", "Deny or mask fields the caller is not authorized for, returning an explicit marker rather than silently omitting them."], ["Default minimal projection", "When no fields are named, return only the identity fields (id, title) so accidental full-record fetches do not happen."], ["Wildcard with exclusions", "Allow '*' minus named fields for 'everything except internals', implemented as schema minus exclusion list."], ["Computed field injection", "Evaluate small server-side expressions (counts, hashes) as virtual fields so callers avoid a second round trip."], ["Array slicing projection", "Support field[0:10] style slices so huge arrays return a window instead of millions of elements."], ["Projection-aware caching", "Key the cache by (record id, sorted field list) so a narrow projection never poisons a later full fetch and vice versa."], ["Cost estimation", "Estimate bytes per field from statistics and warn callers when a projection exceeds a budget, offering pagination."], ["Schema-versioned fields", "Tag fields with the schema version that introduced them so older clients get predictable shapes."], ["Binary field skipping", "Never deserialize binary blobs unless the blob field itself is requested; read only the offset table."], ["Join projection", "Resolve referenced record fields (author->name) in one projection instead of forcing N+1 fetches."], ["Field deprecation markers", "Flag retired fields in the schema so migrations happen before removal, never by surprise."], ["Projection diffing", "Compare the requested projection against the last one to power change-only updates for long-lived clients."]];
var CATS=["projection", "storage", "performance"];
var DEMO="# Selective Field Retrieval demo: push-down projection with access control.\nRECORDS={\"r1\":{\"id\":\"r1\",\"title\":\"Solar Sails\",\"body\":\"x\"*5000,\"secret\":\"classified\",\"author\":{\"name\":\"J. Doe\",\"email\":\"j@x.io\"},\"tags\":[\"a\",\"b\",\"c\",\"d\"]}}\nSCHEMA={\"id\":\"str\",\"title\":\"str\",\"body\":\"str\",\"secret\":\"str\",\"author.name\":\"str\",\"author.email\":\"str\",\"tags\":\"list\"}\nDENIED={\"secret\"}\ndef project(rec_id,fields):\n    rec=RECORDS[rec_id]; out={}\n    for f in fields:\n        if f in DENIED: out[f]=\"<redacted: not authorized>\"; continue\n        if f not in SCHEMA: raise ValueError(\"unknown field: \"+f)\n        if f==\"*\": out.update({k:v for k,v in rec.items() if k not in DENIED}); continue\n        val=rec\n        for part in f.split(\".\"): val=val[part]\n        out[f]=val\n    return out\nprint(project(\"r1\",[\"id\",\"title\",\"author.name\"]))\nprint(project(\"r1\",[\"secret\",\"tags\"]))\n";
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function generate(seed,opts){
  opts=opts||{};var rnd=prng(seed);
  var idx=(seed-1)%METHODS.length;var m=METHODS[idx];
  var cat=opts.category||CATS[(rnd()*CATS.length)|0];
  var id=PREFIX+String(1000+((seed-1)%9000));
  var title=m[0]+' \u2014 '+"Selective Field Retrieval";
  return {id:id,t:title,title:title,description:"Selective field retrieval answers a projection, not a whole record: the caller names the fields it needs and the store returns just those, skipping the rest. Over a near-boundless archive this cuts transferred bytes by orders of magnitude, speeds up mobile clients, and reduces exposure of fields the caller never asked for. The technique combines a declared field schema, push-down projection at the",
    kind:"retrieval tool",category:cat,ladder_rank:1+((seed-1)%3),demo:DEMO,
    provenance:"Public-harvest",last_verified:'2026-10-21',src:"public-harvest",_seed:seed};
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
  if(r.src!=="public-harvest")e.push('src');
  return {ok:!e.length,errors:e};
}
var gen={version:"jahdb-archive-toolkit-selective-field-retrieval-1.0",generate:generate,validate:validate};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("archive-toolkit-selective-field-retrieval",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();