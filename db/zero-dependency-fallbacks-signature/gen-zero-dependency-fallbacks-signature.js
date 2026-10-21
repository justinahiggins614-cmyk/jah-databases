(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];} function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var CATS=["binary", "library", "shell", "embed", "libc"];
var PREFIX='JAH-ZDF-S-';
var GENVER='jahdb-zero-dependency-fallbacks-signature-1.0';
var SRC='signature-generated-completion';
var EDITION='signature';
var PROV="Signature-original completion authored for the JAH Databases network; clearly labeled Signature, never presented as public record.";
var FIELDS=["name", "deps", "size_kb", "kind2"];
var DEMO_TPL="// $TITLE - zero-dependency audit\nvar T = { name: \"$NAME\", deps: $DEPS, size_kb: \"$SIZE_KB\" };\nconsole.log(\"Tool: \" + T.name + \" (\" + \"$KIND2\" + \")\");\nconsole.log(\"External dependencies: \" + T.deps);\nconsole.log(\"Size: ~\" + T.size_kb + \" KB\");\nconsole.log(T.deps === 0 ? \"VERDICT: zero-dependency fallback READY\" : \"VERDICT: needs vendoring\");";
function jsEsc(s){return String(s).replace(/\\/g,'\\\\').replace(/"/g,'\\"').replace(/\n/g,'\\n').replace(/\r/g,'\\r').replace(/\t/g,'\\t');}
function fillTpl(tpl,vars){return tpl.replace(/\$([A-Za-z0-9_]+)/g,function(m,k){return Object.prototype.hasOwnProperty.call(vars,k)?jsEsc(vars[k]):m;});}
/* rows: [category, title, description, {fields}] */
var B=[["binary", "SigOne-Binary", "Signature-original: one-binary packaging sealing the app, config schema, and SBOM into a signed blob. It ships with 0 external dependencies at about 5000 KB.", {"name": "SigOne-Binary", "deps": "0", "size_kb": "5000", "kind2": "binary"}], ["library", "SigLib-Amalgam", "Signature-original: amalgamated Signature libraries shipping as a single audited C file. It ships with 0 external dependencies at about 800 KB.", {"name": "SigLib-Amalgam", "deps": "0", "size_kb": "800", "kind2": "library"}], ["shell", "SigShell", "Signature-original: a fallback shell with 120 builtins so scripts run with no external tools. It ships with 0 external dependencies at about 450 KB.", {"name": "SigShell", "deps": "0", "size_kb": "450", "kind2": "shell"}], ["embed", "SigDB-Embed", "Signature-original: an embedded key-value store with zero dependencies and crash-safe writes. It ships with 0 external dependencies at about 200 KB.", {"name": "SigDB-Embed", "deps": "0", "size_kb": "200", "kind2": "embed"}], ["library", "SigNet-Tiny", "Signature-original: a dependency-free TLS 1.3 client in one header for bootstrapping. It ships with 0 external dependencies at about 350 KB.", {"name": "SigNet-Tiny", "deps": "0", "size_kb": "350", "kind2": "library"}], ["library", "SigZip", "Signature-original: a single-file compressor with a Signature container format and checksums. It ships with 0 external dependencies at about 90 KB.", {"name": "SigZip", "deps": "0", "size_kb": "90", "kind2": "library"}], ["library", "SigJSON", "Signature-original: a zero-dependency JSON parser/serializer with schema validation built in. It ships with 0 external dependencies at about 60 KB.", {"name": "SigJSON", "deps": "0", "size_kb": "60", "kind2": "library"}], ["library", "SigCrypt", "Signature-original: audited primitives (hash, AEAD, signatures) in one file, no external crypto. It ships with 0 external dependencies at about 150 KB.", {"name": "SigCrypt", "deps": "0", "size_kb": "150", "kind2": "library"}], ["library", "SigHTTP", "Signature-original: a minimal HTTP/1.1 + HTTP/2 client/server core for fallback serving. It ships with 0 external dependencies at about 180 KB.", {"name": "SigHTTP", "deps": "0", "size_kb": "180", "kind2": "library"}], ["library", "SigLog", "Signature-original: structured logging with zero deps and automatic redaction of secrets. It ships with 0 external dependencies at about 40 KB.", {"name": "SigLog", "deps": "0", "size_kb": "40", "kind2": "library"}], ["library", "SigTest", "Signature-original: a single-header test runner with property-based generation included. It ships with 0 external dependencies at about 70 KB.", {"name": "SigTest", "deps": "0", "size_kb": "70", "kind2": "library"}], ["library", "SigTime-Lib", "Signature-original: timezone-aware date handling without ICU or OS databases. It ships with 0 external dependencies at about 110 KB.", {"name": "SigTime-Lib", "deps": "0", "size_kb": "110", "kind2": "library"}], ["library", "SigMesh-Lite", "Signature-original: a dependency-free mesh networking core for fallback peer links. It ships with 0 external dependencies at about 220 KB.", {"name": "SigMesh-Lite", "deps": "0", "size_kb": "220", "kind2": "library"}], ["embed", "SigVM-Tiny", "Signature-original: a tiny WASM interpreter embedding scripting with no host dependencies. It ships with 0 external dependencies at about 280 KB.", {"name": "SigVM-Tiny", "deps": "0", "size_kb": "280", "kind2": "embed"}], ["binary", "SigKit-One", "Signature-original: the united fallback kit — shell, db, net, crypto in one signed binary. It ships with 0 external dependencies at about 3000 KB.", {"name": "SigKit-One", "deps": "0", "size_kb": "3000", "kind2": "binary"}]];
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
  if(!new RegExp('^'+'JAH\\-ZDF\\-S\\-'+'\\d{6}$').test(r.id||''))e.push('id');
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('zero-dependency-fallbacks-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
