(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];} function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var CATS=["browser", "standalone", "edge", "embedded", "tooling"];
var PREFIX='JAH-BNW-S-';
var GENVER='jahdb-browser-native-wasm-runtimes-signature-1.0';
var SRC='signature-generated-completion';
var EDITION='signature';
var PROV="Signature-original completion authored for the JAH Databases network; clearly labeled Signature, never presented as public record.";
var FIELDS=["runtime", "language", "wasi", "license"];
var DEMO_TPL="// $TITLE - runtime capability check\nvar RT = { name: \"$RUNTIME\", language: \"$LANGUAGE\", wasi: \"$WASI\", license: \"$LICENSE\" };\nvar pages = 16;\nconsole.log(\"Runtime: \" + RT.name + \" (\" + RT.language + \")\");\nconsole.log(\"WASI: \" + RT.wasi + \" | License: \" + RT.license);\nconsole.log(\"Linear memory: \" + pages + \" pages = \" + (pages * 65536) + \" bytes\");\nconsole.log(\"Sandbox check: bounds enforced -> PASS\");";
function jsEsc(s){return String(s).replace(/\\/g,'\\\\').replace(/"/g,'\\"').replace(/\n/g,'\\n').replace(/\r/g,'\\r').replace(/\t/g,'\\t');}
function fillTpl(tpl,vars){return tpl.replace(/\$([A-Za-z0-9_]+)/g,function(m,k){return Object.prototype.hasOwnProperty.call(vars,k)?jsEsc(vars[k]):m;});}
/* rows: [category, title, description, {fields}] */
var B=[["embedded", "SigVM-Nano", "Signature-original: a WASM interpreter designed to cold-boot in under 2 ms on microcontrollers with 64 KB RAM. It is implemented in C, supports SigWASI-tiny, and is released under Signature.", {"runtime": "SigVM-Nano", "language": "C", "wasi": "SigWASI-tiny", "license": "Signature"}], ["edge", "SigVM-Edge", "Signature-original: an edge runtime with built-in request metering and per-request fuel caps for multi-tenant hosts. It is implemented in Rust, supports WASI 0.2, and is released under Signature.", {"runtime": "SigVM-Edge", "language": "Rust", "wasi": "WASI 0.2", "license": "Signature"}], ["browser", "SigVM-Browser", "Signature-original: a browser-embeddable runtime exposing WASM modules as DOM-addressable components. It is implemented in TypeScript/C++, supports browser-bindings, and is released under Signature.", {"runtime": "SigVM-Browser", "language": "TypeScript/C++", "wasi": "browser-bindings", "license": "Signature"}], ["standalone", "SigVM-Fleet", "Signature-original: a fleet runtime that live-migrates running WASM instances between hosts with CRIU-style freeze. It is implemented in Rust, supports WASI 0.2, and is released under Signature.", {"runtime": "SigVM-Fleet", "language": "Rust", "wasi": "WASI 0.2", "license": "Signature"}], ["tooling", "SigVM-Deterministic", "Signature-original: a deterministic replay runtime recording every host call for exact re-execution of WASM runs. It is implemented in Rust, supports WASI-recorded, and is released under Signature.", {"runtime": "SigVM-Deterministic", "language": "Rust", "wasi": "WASI-recorded", "license": "Signature"}], ["tooling", "SigVM-Synth", "Signature-original: a synthesis runtime that generates WASM modules from high-level specs for testing harnesses. It is implemented in Python/Rust, supports WASI, and is released under Signature.", {"runtime": "SigVM-Synth", "language": "Python/Rust", "wasi": "WASI", "license": "Signature"}], ["standalone", "SigVM-Guard", "Signature-original: a hardening runtime inserting canaries and control-flow checks into WASM at load time. It is implemented in C++, supports WASI 0.2, and is released under Signature.", {"runtime": "SigVM-Guard", "language": "C++", "wasi": "WASI 0.2", "license": "Signature"}], ["edge", "SigVM-Mesh", "Signature-original: a mesh runtime where WASM modules address each other over the Signature peer mesh directly. It is implemented in Rust, supports SigMesh-WASI, and is released under Signature.", {"runtime": "SigVM-Mesh", "language": "Rust", "wasi": "SigMesh-WASI", "license": "Signature"}], ["tooling", "SigVM-Trace", "Signature-original: a tracing runtime emitting per-instruction cost profiles to tune hot loops. It is implemented in Rust, supports WASI, and is released under Signature.", {"runtime": "SigVM-Trace", "language": "Rust", "wasi": "WASI", "license": "Signature"}], ["embedded", "SigVM-Fuse", "Signature-original: a fused runtime merging interpreter and AOT tiers so cold code interprets and hot code compiles. It is implemented in C, supports SigWASI-tiny, and is released under Signature.", {"runtime": "SigVM-Fuse", "language": "C", "wasi": "SigWASI-tiny", "license": "Signature"}], ["standalone", "SigVM-Vault", "Signature-original: a confidential runtime sealing module memory with hardware enclaves where available. It is implemented in Rust, supports WASI 0.2, and is released under Signature.", {"runtime": "SigVM-Vault", "language": "Rust", "wasi": "WASI 0.2", "license": "Signature"}], ["edge", "SigVM-Stream", "Signature-original: a streaming runtime compiling WASM while bytes still arrive, cutting time-to-first-run. It is implemented in Rust, supports WASI 0.2, and is released under Signature.", {"runtime": "SigVM-Stream", "language": "Rust", "wasi": "WASI 0.2", "license": "Signature"}], ["tooling", "SigVM-Verify", "Signature-original: a verification runtime proving memory-safety properties of modules before execution. It is implemented in OCaml/Rust, supports WASI, and is released under Signature.", {"runtime": "SigVM-Verify", "language": "OCaml/Rust", "wasi": "WASI", "license": "Signature"}], ["embedded", "SigVM-Offline", "Signature-original: an offline-first runtime queuing host calls and replaying them when connectivity returns. It is implemented in C, supports SigWASI-tiny, and is released under Signature.", {"runtime": "SigVM-Offline", "language": "C", "wasi": "SigWASI-tiny", "license": "Signature"}], ["standalone", "SigVM-One", "Signature-original: the united master runtime combining Nano, Edge, Fleet, and Guard tiers behind one API. It is implemented in Rust/C, supports WASI 0.2 + SigWASI, and is released under Signature.", {"runtime": "SigVM-One", "language": "Rust/C", "wasi": "WASI 0.2 + SigWASI", "license": "Signature"}]];
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
  if(!new RegExp('^'+'JAH\\-BNW\\-S\\-'+'\\d{6}$').test(r.id||''))e.push('id');
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('browser-native-wasm-runtimes-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
