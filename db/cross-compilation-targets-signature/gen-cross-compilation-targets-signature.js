(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];} function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var CATS=["linux", "windows", "macos", "mobile", "wasm", "embedded"];
var PREFIX='JAH-CCT-S-';
var GENVER='jahdb-cross-compilation-targets-signature-1.0';
var SRC='signature-generated-completion';
var EDITION='signature';
var PROV="Signature-original completion authored for the JAH Databases network; clearly labeled Signature, never presented as public record.";
var FIELDS=["triple", "toolchain", "os", "arch", "use"];
var DEMO_TPL="// $TITLE - target triple parser\nvar triple = \"$TRIPLE\";\nvar parts = triple.split(\"-\");\nconsole.log(\"Triple: \" + triple);\nconsole.log(\"Arch: \" + parts[0]);\nconsole.log(\"Vendor: \" + (parts[1] || \"?\"));\nconsole.log(\"OS/ABI: \" + parts.slice(2).join(\"-\"));\nconsole.log(\"Toolchain: $TOOLCHAIN | Use: $USE\");";
function jsEsc(s){return String(s).replace(/\\/g,'\\\\').replace(/"/g,'\\"').replace(/\n/g,'\\n').replace(/\r/g,'\\r').replace(/\t/g,'\\t');}
function fillTpl(tpl,vars){return tpl.replace(/\$([A-Za-z0-9_]+)/g,function(m,k){return Object.prototype.hasOwnProperty.call(vars,k)?jsEsc(vars[k]):m;});}
/* rows: [category, title, description, {fields}] */
var B=[["embedded", "SigCell microVM target", "Signature-original: a freestanding target emitting SigCell microVM images directly. Toolchain: sigc; OS: SigCell; architecture: multi. Typical use: microVM functions.", {"triple": "sigcell-unknown-sigcell", "toolchain": "sigc", "os": "SigCell", "arch": "multi", "use": "microVM functions"}], ["wasm", "SigWASM tiny", "Signature-original: wasm32 with the SigWASI-tiny interface for 64 KB devices. Toolchain: sigc; OS: SigWASI-tiny; architecture: wasm32. Typical use: microcontroller WASM.", {"triple": "wasm32-unknown-sigwasi-tiny", "toolchain": "sigc", "os": "SigWASI-tiny", "arch": "wasm32", "use": "microcontroller WASM"}], ["embedded", "SigMesh node", "Signature-original: firmware target with the mesh stack linked in at boot. Toolchain: sigc; OS: none; architecture: multi. Typical use: mesh devices.", {"triple": "sigmesh-unknown-none", "toolchain": "sigc", "os": "none", "arch": "multi", "use": "mesh devices"}], ["linux", "SigEnclave SGX", "Signature-original: enclave target with attestation intrinsics in the standard library. Toolchain: sigc; OS: SigEnclave; architecture: x86_64. Typical use: confidential compute.", {"triple": "x86_64-unknown-sigenclave", "toolchain": "sigc", "os": "SigEnclave", "arch": "x86_64", "use": "confidential compute"}], ["mobile", "SigPhone ARM64", "Signature-original: hardened Android target with memory-tagging enabled by default. Toolchain: sigc/ndk; OS: Android; architecture: aarch64. Typical use: hardened mobile.", {"triple": "aarch64-sigphone-android", "toolchain": "sigc/ndk", "os": "Android", "arch": "aarch64", "use": "hardened mobile"}], ["macos", "SigDesk universal", "Signature-original: one artifact running on macOS, Windows, and Linux via the Sig runtime. Toolchain: sigc; OS: SigDesk; architecture: multi. Typical use: portable desktop.", {"triple": "universal-unknown-sigdesk", "toolchain": "sigc", "os": "SigDesk", "arch": "multi", "use": "portable desktop"}], ["embedded", "SigBoot UEFI", "Signature-original: UEFI application target for pre-OS Signature tooling. Toolchain: sigc; OS: UEFI; architecture: x86_64. Typical use: boot tooling.", {"triple": "x86_64-unknown-sigboot", "toolchain": "sigc", "os": "UEFI", "arch": "x86_64", "use": "boot tooling"}], ["linux", "SigGPU kernels", "Signature-original: GPU kernel target with portable IR across vendors. Toolchain: sigc; OS: none; architecture: siggpu. Typical use: portable GPU code.", {"triple": "siggpu-unknown-sigir", "toolchain": "sigc", "os": "none", "arch": "siggpu", "use": "portable GPU code"}], ["wasm", "SigWasm-GC", "Signature-original: WASM with GC proposal enabled for managed-language compilation. Toolchain: sigc; OS: SigWASI; architecture: wasm32. Typical use: managed WASM.", {"triple": "wasm32-unknown-sigwasi-gc", "toolchain": "sigc", "os": "SigWASI", "arch": "wasm32", "use": "managed WASM"}], ["embedded", "SigRT real-time", "Signature-original: real-time target with worst-case execution analysis built into builds. Toolchain: sigc; OS: SigRT; architecture: armv7. Typical use: real-time control.", {"triple": "armv7-unknown-sigrt", "toolchain": "sigc", "os": "SigRT", "arch": "armv7", "use": "real-time control"}], ["embedded", "SigSat space", "Signature-original: radiation-tolerant target with triple-voted critical sections. Toolchain: sigc; OS: none; architecture: riscv64. Typical use: space systems.", {"triple": "riscv64-unknown-sigsat", "toolchain": "sigc", "os": "none", "arch": "riscv64", "use": "space systems"}], ["wasm", "SigBrowser component", "Signature-original: browser component target exposing DOM bindings as WIT interfaces. Toolchain: sigc; OS: browser; architecture: wasm32. Typical use: browser components.", {"triple": "wasm32-unknown-sigdom", "toolchain": "sigc", "os": "browser", "arch": "wasm32", "use": "browser components"}], ["wasm", "SigEdge function", "Signature-original: edge-function target with cold-start budgets enforced at compile time. Toolchain: sigc; OS: SigEdge; architecture: wasm32. Typical use: edge functions.", {"triple": "wasm32-unknown-sigedge", "toolchain": "sigc", "os": "SigEdge", "arch": "wasm32", "use": "edge functions"}], ["linux", "SigAI accelerator", "Signature-original: NPU target with quantized operator fusion in the backend. Toolchain: sigc; OS: Linux; architecture: aarch64. Typical use: on-device AI.", {"triple": "aarch64-unknown-signpu", "toolchain": "sigc", "os": "Linux", "arch": "aarch64", "use": "on-device AI"}], ["wasm", "SigOne universal", "Signature-original: the united target — one build fanning out to every Sig platform. Toolchain: sigc; OS: SigOne; architecture: multi. Typical use: write once, run anywhere.", {"triple": "universal-unknown-sigone", "toolchain": "sigc", "os": "SigOne", "arch": "multi", "use": "write once, run anywhere"}]];
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
  if(!new RegExp('^'+'JAH\\-CCT\\-S\\-'+'\\d{6}$').test(r.id||''))e.push('id');
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('cross-compilation-targets-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
