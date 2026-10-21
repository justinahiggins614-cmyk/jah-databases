(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];} function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var CATS=["text", "binary", "columnar", "schema", "streaming"];
var PREFIX='JAH-UFI-';
var GENVER='jahdb-universal-format-interchange-1.0';
var SRC='public-harvest';
var EDITION='public';
var PROV="Public record compiled from openly published documentation, project sources, and standard references.";
var FIELDS=["format", "encoding", "schema", "best_for"];
var DEMO_TPL="// $TITLE - format round-trip demo\nvar data = { name: \"sensor-1\", readings: [21.5, 22.1, 20.9] };\nvar json = JSON.stringify(data);\nvar back = JSON.parse(json);\nvar ok = back.name === data.name && back.readings.length === 3;\nconsole.log(\"Format: $FORMAT | Encoding: $ENCODING\");\nconsole.log(\"Serialized: \" + json.length + \" bytes\");\nconsole.log(\"Round-trip preserves data -> \" + (ok ? \"PASS\" : \"FAIL\"));\nconsole.log(\"Schema: $SCHEMA | Best for: $BEST_FOR\");";
function jsEsc(s){return String(s).replace(/\\/g,'\\\\').replace(/"/g,'\\"').replace(/\n/g,'\\n').replace(/\r/g,'\\r').replace(/\t/g,'\\t');}
function fillTpl(tpl,vars){return tpl.replace(/\$([A-Za-z0-9_]+)/g,function(m,k){return Object.prototype.hasOwnProperty.call(vars,k)?jsEsc(vars[k]):m;});}
/* rows: [category, title, description, {fields}] */
var B=[["text", "JSON", "The universal text interchange; every language parses it, humans can read it. Encoding: UTF-8 text; schema: optional (JSON Schema). Best for: APIs, configs.", {"format": "JSON", "encoding": "UTF-8 text", "schema": "optional (JSON Schema)", "best_for": "APIs, configs"}], ["text", "XML", "Self-describing markup with namespaces and validation via XSD; enterprise staple. Encoding: text; schema: XSD/DTD. Best for: documents, enterprise.", {"format": "XML", "encoding": "text", "schema": "XSD/DTD", "best_for": "documents, enterprise"}], ["text", "YAML", "Human-friendly superset of JSON with anchors and multi-line strings. Encoding: UTF-8 text; schema: optional. Best for: configs.", {"format": "YAML", "encoding": "UTF-8 text", "schema": "optional", "best_for": "configs"}], ["text", "TOML", "Minimal config format designed to be unambiguous and easy to parse. Encoding: UTF-8 text; schema: implicit. Best for: configs.", {"format": "TOML", "encoding": "UTF-8 text", "schema": "implicit", "best_for": "configs"}], ["binary", "Protocol Buffers", "Google’s IDL-driven binary format with field-number evolution. Encoding: binary varint; schema: required (.proto). Best for: RPC, storage.", {"format": "protobuf", "encoding": "binary varint", "schema": "required (.proto)", "best_for": "RPC, storage"}], ["binary", "Avro", "Hadoop’s row format carrying its schema in the file header. Encoding: binary; schema: embedded JSON. Best for: big data pipelines.", {"format": "Avro", "encoding": "binary", "schema": "embedded JSON", "best_for": "big data pipelines"}], ["columnar", "Parquet", "Columnar storage with dictionary/RLE encoding; the analytics standard. Encoding: columnar binary; schema: embedded. Best for: analytics, lakes.", {"format": "Parquet", "encoding": "columnar binary", "schema": "embedded", "best_for": "analytics, lakes"}], ["columnar", "Arrow", "In-memory columnar standard for zero-copy dataframe exchange. Encoding: columnar binary; schema: embedded. Best for: dataframes.", {"format": "Arrow IPC", "encoding": "columnar binary", "schema": "embedded", "best_for": "dataframes"}], ["binary", "MessagePack", "Binary JSON: smaller and faster while staying schemaless. Encoding: binary; schema: optional. Best for: caching, RPC.", {"format": "MessagePack", "encoding": "binary", "schema": "optional", "best_for": "caching, RPC"}], ["binary", "CBOR", "Concise Binary Object Representation (RFC 8949); the IETF’s binary JSON. Encoding: binary; schema: optional (CDDL). Best for: IoT, COSE.", {"format": "CBOR", "encoding": "binary", "schema": "optional (CDDL)", "best_for": "IoT, COSE"}], ["text", "CSV", "The humble comma-separated lingua franca of spreadsheets and data export. Encoding: text; schema: header row. Best for: tabular exchange.", {"format": "CSV", "encoding": "text", "schema": "header row", "best_for": "tabular exchange"}], ["binary", "HDF5", "Hierarchical scientific data with chunking, compression, and hyperslabs. Encoding: binary; schema: embedded. Best for: science data.", {"format": "HDF5", "encoding": "binary", "schema": "embedded", "best_for": "science data"}], ["columnar", "ORC", "Optimized Row Columnar from the Hive ecosystem with ACID support. Encoding: columnar binary; schema: embedded. Best for: Hive analytics.", {"format": "ORC", "encoding": "columnar binary", "schema": "embedded", "best_for": "Hive analytics"}], ["binary", "FlatBuffers", "Zero-copy access without unpacking; games and mobile favorite. Encoding: binary; schema: required (.fbs). Best for: games, mobile.", {"format": "FlatBuffers", "encoding": "binary", "schema": "required (.fbs)", "best_for": "games, mobile"}], ["binary", "Cap’n Proto", "Infinity faster claim aside, its zero-copy RPC and packing are real. Encoding: binary; schema: required. Best for: RPC, sandboxed IPC.", {"format": "Cap'n Proto", "encoding": "binary", "schema": "required", "best_for": "RPC, sandboxed IPC"}]];
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
  if(!new RegExp('^'+'JAH\\-UFI\\-'+'\\d{6}$').test(r.id||''))e.push('id');
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('universal-format-interchange',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
