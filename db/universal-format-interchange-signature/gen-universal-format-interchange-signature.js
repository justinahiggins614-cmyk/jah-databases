(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];} function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var CATS=["text", "binary", "columnar", "schema", "streaming"];
var PREFIX='JAH-UFI-S-';
var GENVER='jahdb-universal-format-interchange-signature-1.0';
var SRC='signature-generated-completion';
var EDITION='signature';
var PROV="Signature-original completion authored for the JAH Databases network; clearly labeled Signature, never presented as public record.";
var FIELDS=["format", "encoding", "schema", "best_for"];
var DEMO_TPL="// $TITLE - format round-trip demo\nvar data = { name: \"sensor-1\", readings: [21.5, 22.1, 20.9] };\nvar json = JSON.stringify(data);\nvar back = JSON.parse(json);\nvar ok = back.name === data.name && back.readings.length === 3;\nconsole.log(\"Format: $FORMAT | Encoding: $ENCODING\");\nconsole.log(\"Serialized: \" + json.length + \" bytes\");\nconsole.log(\"Round-trip preserves data -> \" + (ok ? \"PASS\" : \"FAIL\"));\nconsole.log(\"Schema: $SCHEMA | Best for: $BEST_FOR\");";
function jsEsc(s){return String(s).replace(/\\/g,'\\\\').replace(/"/g,'\\"').replace(/\n/g,'\\n').replace(/\r/g,'\\r').replace(/\t/g,'\\t');}
function fillTpl(tpl,vars){return tpl.replace(/\$([A-Za-z0-9_]+)/g,function(m,k){return Object.prototype.hasOwnProperty.call(vars,k)?jsEsc(vars[k]):m;});}
/* rows: [category, title, description, {fields}] */
var B=[["text", "SigJSON+", "Signature-original: JSON with comments, trailing commas, and schema hints tolerated. Encoding: UTF-8 text; schema: optional inline. Best for: Sig configs.", {"format": "SigJSON+", "encoding": "UTF-8 text", "schema": "optional inline", "best_for": "Sig configs"}], ["binary", "SigBin", "Signature-original: self-describing binary with embedded schema hashes. Encoding: binary; schema: embedded hash. Best for: Sig RPC.", {"format": "SigBin", "encoding": "binary", "schema": "embedded hash", "best_for": "Sig RPC"}], ["columnar", "SigCol", "Signature-original: columnar format with adaptive encoding per column. Encoding: columnar binary; schema: embedded. Best for: Sig analytics.", {"format": "SigCol", "encoding": "columnar binary", "schema": "embedded", "best_for": "Sig analytics"}], ["streaming", "SigStream", "Signature-original: streaming records with per-record checksums and resume. Encoding: framed binary; schema: per-stream. Best for: Sig pipelines.", {"format": "SigStream", "encoding": "framed binary", "schema": "per-stream", "best_for": "Sig pipelines"}], ["text", "SigDoc", "Signature-original: document format unifying JSON/YAML/TOML with lossless conversion. Encoding: UTF-8 text; schema: optional. Best for: Sig documents.", {"format": "SigDoc", "encoding": "UTF-8 text", "schema": "optional", "best_for": "Sig documents"}], ["columnar", "SigTable", "Signature-original: tabular format with statistics sketches per row group. Encoding: columnar; schema: embedded. Best for: Sig tables.", {"format": "SigTable", "encoding": "columnar", "schema": "embedded", "best_for": "Sig tables"}], ["binary", "SigGraph", "Signature-original: graph serialization with CSR layout for zero-copy traversal. Encoding: binary CSR; schema: embedded. Best for: Sig graphs.", {"format": "SigGraph", "encoding": "binary CSR", "schema": "embedded", "best_for": "Sig graphs"}], ["binary", "SigTensor", "Signature-original: tensor format with quantization metadata and sharding. Encoding: binary; schema: embedded. Best for: Sig AI models.", {"format": "SigTensor", "encoding": "binary", "schema": "embedded", "best_for": "Sig AI models"}], ["streaming", "SigEvent", "Signature-original: event envelopes with causal headers for distributed tracing. Encoding: binary/text; schema: envelope. Best for: Sig events.", {"format": "SigEvent", "encoding": "binary/text", "schema": "envelope", "best_for": "Sig events"}], ["text", "SigConfig", "Signature-original: config format with includes, overlays, and secret references. Encoding: UTF-8 text; schema: validated. Best for: Sig configs.", {"format": "SigConfig", "encoding": "UTF-8 text", "schema": "validated", "best_for": "Sig configs"}], ["streaming", "SigLog", "Signature-original: JSONL logs with indexed fields for instant querying. Encoding: JSONL; schema: field index. Best for: Sig logs.", {"format": "SigLog", "encoding": "JSONL", "schema": "field index", "best_for": "Sig logs"}], ["binary", "SigMesh-Packet", "Signature-original: mesh packet format with routing headers and e2e encryption. Encoding: binary; schema: fixed. Best for: Sig mesh.", {"format": "SigMesh-Packet", "encoding": "binary", "schema": "fixed", "best_for": "Sig mesh"}], ["binary", "SigArchive", "Signature-original: archive format with global dedup across all stored files. Encoding: binary; schema: manifest. Best for: Sig archives.", {"format": "SigArchive", "encoding": "binary", "schema": "manifest", "best_for": "Sig archives"}], ["binary", "SigDelta-Fmt", "Signature-original: delta-friendly format where small edits produce small diffs. Encoding: binary; schema: embedded. Best for: versioned data.", {"format": "SigDelta-Fmt", "encoding": "binary", "schema": "embedded", "best_for": "versioned data"}], ["binary", "SigFormat-One", "Signature-original: the united interchange — one container negotiating text/binary/columnar. Encoding: negotiated; schema: embedded. Best for: everything.", {"format": "SigFormat-One", "encoding": "negotiated", "schema": "embedded", "best_for": "everything"}]];
function demoFor(title,id,f){
  var vars={TITLE:title,ID:id};
  for(var k in f){ if(Object.prototype.hasOwnProperty.call(f,k)) vars[k.toUpperCase()]=f[k]; }
  return fillTpl(DEMO_TPL,vars);
}
function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  var cat=opts.category||pick(CATS,rnd);
  var pool=B.filter(function(b){return b[0]===cat;});
  var b=pick(pool.length?pool:B,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  var fields={}; for(var k in b[3]){fields[k]=b[3][k];}
  return {id:id,t:b[1],title:b[1],g:cat,c:1,category:cat,description:b[2],fields:fields,ladder_rank:1+(seed%3),demo:demoFor(b[1],id,fields),provenance:PROV,src:SRC,last_verified:'2026-10-21',edition:EDITION,_seed:seed};
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!new RegExp('^'+'JAH\\-UFI\\-S\\-'+'\\d{6}$').test(r.id||''))e.push('id');
  if(typeof r.title!=='string'||!r.title.length)e.push('title');
  if(r.t!==r.title)e.push('t');
  if(typeof r.description!=='string'||r.description.length<40)e.push('description');
  if(CATS.indexOf(r.category)<0)e.push('category');
  if(r.g!==r.category)e.push('g');
  if(!r.fields||typeof r.fields!=='object')e.push('fields');
  else{FIELDS.forEach(function(k){if(typeof r.fields[k]!=='string'||!r.fields[k].length)e.push('fields.'+k);});}
  if(!(r.ladder_rank>=1&&r.ladder_rank<=3))e.push('ladder_rank');
  if(typeof r.demo!=='string'||r.demo.indexOf('console.log')<0)e.push('demo');
  if(r.src!==SRC)e.push('src');
  if(r.edition!==EDITION)e.push('edition');
  if(r.last_verified!=='2026-10-21')e.push('last_verified');
  if(typeof r.provenance!=='string'||!r.provenance.length)e.push('provenance');
  return {ok:!e.length,errors:e};
}
var gen={version:GENVER,generate:generate,validate:validate};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('universal-format-interchange-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
