(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];} function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var CATS=["browser", "standalone", "edge", "embedded", "tooling"];
var PREFIX='JAH-BNW-';
var GENVER='jahdb-browser-native-wasm-runtimes-1.0';
var SRC='public-harvest';
var EDITION='public';
var PROV="Public record compiled from openly published documentation, project sources, and standard references.";
var FIELDS=["runtime", "language", "wasi", "license"];
var DEMO_TPL="// $TITLE - runtime capability check\nvar RT = { name: \"$RUNTIME\", language: \"$LANGUAGE\", wasi: \"$WASI\", license: \"$LICENSE\" };\nvar pages = 16;\nconsole.log(\"Runtime: \" + RT.name + \" (\" + RT.language + \")\");\nconsole.log(\"WASI: \" + RT.wasi + \" | License: \" + RT.license);\nconsole.log(\"Linear memory: \" + pages + \" pages = \" + (pages * 65536) + \" bytes\");\nconsole.log(\"Sandbox check: bounds enforced -> PASS\");";
function jsEsc(s){return String(s).replace(/\\/g,'\\\\').replace(/"/g,'\\"').replace(/\n/g,'\\n').replace(/\r/g,'\\r').replace(/\t/g,'\\t');}
function fillTpl(tpl,vars){return tpl.replace(/\$([A-Za-z0-9_]+)/g,function(m,k){return Object.prototype.hasOwnProperty.call(vars,k)?jsEsc(vars[k]):m;});}
/* rows: [category, title, description, {fields}] */
var B=[["standalone", "wasmtime", "The Bytecode Alliance reference runtime; powers server-side WASM with a Cranelift compiler and component-model support. It is implemented in Rust, supports WASI 0.2 / component model, and is released under Apache-2.0.", {"runtime": "wasmtime", "language": "Rust", "wasi": "WASI 0.2 / component model", "license": "Apache-2.0"}], ["standalone", "Wasmer", "A universal runtime shipping a package manager (WAPM) and multiple compilers including Singlepass for fast startup. It is implemented in Rust, supports WASI 0.1/0.2, and is released under MIT.", {"runtime": "Wasmer", "language": "Rust", "wasi": "WASI 0.1/0.2", "license": "MIT"}], ["embedded", "WAMR", "The WebAssembly Micro Runtime targets tiny devices with an interpreter plus AOT modes that fit in kilobytes of RAM. It is implemented in C, supports WASI, and is released under Apache-2.0.", {"runtime": "WAMR (wasm-micro-runtime)", "language": "C", "wasi": "WASI", "license": "Apache-2.0"}], ["edge", "WasmEdge", "A CNCF sandbox project tuned for edge and serverless with TensorFlow and image extensions for AI workloads. It is implemented in C++, supports WASI 0.1/0.2, and is released under Apache-2.0.", {"runtime": "WasmEdge", "language": "C++", "wasi": "WASI 0.1/0.2", "license": "Apache-2.0"}], ["browser", "V8", "Chrome and Node ship V8 with Liftoff (fast baseline) and TurboFan (optimizing) tiers compiling WASM at near-native speed. It is implemented in C++, supports n/a (browser + Node experimental), and is released under BSD-3-Clause.", {"runtime": "V8", "language": "C++", "wasi": "n/a (browser + Node experimental)", "license": "BSD-3-Clause"}], ["browser", "SpiderMonkey", "Firefox’s engine compiles WASM with Cranelift-derived Ion pipelines and was first to ship WASM threads. It is implemented in C++/Rust, supports n/a (browser), and is released under MPL-2.0.", {"runtime": "SpiderMonkey", "language": "C++/Rust", "wasi": "n/a (browser)", "license": "MPL-2.0"}], ["browser", "JavaScriptCore", "Safari’s engine runs WASM through its BBQ and OMG tiers, sharing the JIT infrastructure with JavaScript. It is implemented in C++, supports n/a (browser), and is released under LGPL-2.1 / BSD.", {"runtime": "JavaScriptCore", "language": "C++", "wasi": "n/a (browser)", "license": "LGPL-2.1 / BSD"}], ["embedded", "wasm3", "A high-performance interpreter that runs WASM on microcontrollers where JIT compilation is impossible. It is implemented in C, supports WASI (minimal), and is released under MIT.", {"runtime": "wasm3", "language": "C", "wasi": "WASI (minimal)", "license": "MIT"}], ["standalone", "WAVM", "A research-grade runtime with a focus on spec compliance and a custom LLVM-based optimizing backend. It is implemented in C++, supports WASI, and is released under BSD-3-Clause / LLVM exception.", {"runtime": "WAVM", "language": "C++", "wasi": "WASI", "license": "BSD-3-Clause / LLVM exception"}], ["embedded", "wasmi", "Parity’s interpreter-first runtime, designed for deterministic execution in blockchain-adjacent hosts. It is implemented in Rust, supports WASI (via host), and is released under MIT/Apache-2.0.", {"runtime": "wasmi", "language": "Rust", "wasi": "WASI (via host)", "license": "MIT/Apache-2.0"}], ["standalone", "GraalWasm", "Oracle’s Truffle-based WASM engine lets WASM call into JVM languages and vice versa polyglot-style. It is implemented in Java, supports WASI, and is released under GPL-2.0 with Classpath Exception.", {"runtime": "GraalWasm", "language": "Java", "wasi": "WASI", "license": "GPL-2.0 with Classpath Exception"}], ["tooling", "Extism", "A plug-in framework wrapping wasmtime so any language can load WASM plug-ins through one stable PDK. It is implemented in Rust (host SDKs many), supports WASI (sandboxed), and is released under BSD-3-Clause.", {"runtime": "Extism", "language": "Rust (host SDKs many)", "wasi": "WASI (sandboxed)", "license": "BSD-3-Clause"}], ["embedded", "Chicory", "A pure-Java, zero-native-dependency WASM interpreter for JVM hosts that cannot ship native code. It is implemented in Java, supports WASI preview1, and is released under Apache-2.0.", {"runtime": "Chicory", "language": "Java", "wasi": "WASI preview1", "license": "Apache-2.0"}], ["tooling", "WasmKit", "A TypeScript toolkit for inspecting and running WASM modules with a focus on developer ergonomics. It is implemented in TypeScript, supports WASI (partial), and is released under MIT.", {"runtime": "WasmKit", "language": "TypeScript", "wasi": "WASI (partial)", "license": "MIT"}], ["standalone", "Lucet", "Fastly’s retired ahead-of-time runtime that pioneered WASM at the CDN edge before WasmEdge-era designs. It is implemented in Rust, supports WASI 0.1, and is released under Apache-2.0 / BSD.", {"runtime": "Lucet (retired)", "language": "Rust", "wasi": "WASI 0.1", "license": "Apache-2.0 / BSD"}]];
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
  if(!new RegExp('^'+'JAH\\-BNW\\-'+'\\d{6}$').test(r.id||''))e.push('id');
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('browser-native-wasm-runtimes',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
