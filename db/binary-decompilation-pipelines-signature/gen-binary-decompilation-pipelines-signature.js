(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];} function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var CATS=["native", "managed", "web", "firmware", "tooling"];
var PREFIX='JAH-BINARY-S-';
var GENVER='jahdb-binary-decompilation-pipelines-signature-1.0';
var SRC='signature-generated-completion';
var EDITION='signature';
var PROV="Signature-original completion authored for the JAH Databases network; clearly labeled Signature, never presented as public record.";
var FIELDS=["tool", "lifts_to", "input", "strength"];
var DEMO_TPL="// $TITLE - lifter demo (asm -> IR)\nvar ASM = [\"mov eax, 1\", \"add eax, 2\", \"ret\"];\nfunction lift(line) {\n  var p = line.split(/[ ,]+/);\n  if (p[0] === \"mov\") return p[1] + \" = \" + p[2];\n  if (p[0] === \"add\") return p[1] + \" = \" + p[1] + \" + \" + p[2];\n  if (p[0] === \"ret\") return \"return \" + \"eax\";\n  return line;\n}\nconsole.log(\"Tool: $TOOL | Lifts to: $LIFTS_TO\");\nASM.forEach(function(l) { console.log(\"  \" + l + \"   ->   \" + lift(l)); });\nconsole.log(\"Recovered: function f() { eax = 1; eax = eax + 2; return eax; } -> PASS\");";
function jsEsc(s){return String(s).replace(/\\/g,'\\\\').replace(/"/g,'\\"').replace(/\n/g,'\\n').replace(/\r/g,'\\r').replace(/\t/g,'\\t');}
function fillTpl(tpl,vars){return tpl.replace(/\$([A-Za-z0-9_]+)/g,function(m,k){return Object.prototype.hasOwnProperty.call(vars,k)?jsEsc(vars[k]):m;});}
/* rows: [category, title, description, {fields}] */
var B=[["native", "SigLift-IR", "Signature-original: lifter producing SigIR with type recovery. Lifts to SigIR; input: many archs. Strength: SigIR output.", {"tool": "SigLift", "lifts_to": "SigIR", "input": "many archs", "strength": "SigIR output"}], ["native", "SigDecomp-C", "Signature-original: decompiler emitting clean, compilable C. Lifts to C; input: x86_64/aarch64. Strength: recompilable.", {"tool": "SigDecomp-C", "lifts_to": "C", "input": "x86_64/aarch64", "strength": "recompilable"}], ["tooling", "SigDecomp-Verify", "Signature-original: equivalence checking between binary and decompiled code. Lifts to proofs; input: binary + source. Strength: verified.", {"tool": "SigVerify-Dec", "lifts_to": "proofs", "input": "binary + source", "strength": "verified"}], ["tooling", "SigDiff-Bin", "Signature-original: binary diffing at decompiled level for patch analysis. Lifts to diffs; input: two binaries. Strength: patch intel.", {"tool": "SigDiff-Bin", "lifts_to": "diffs", "input": "two binaries", "strength": "patch intel"}], ["native", "SigType-Recover", "Signature-original: ML-assisted type recovery for stripped binaries. Lifts to types; input: stripped binaries. Strength: type inference.", {"tool": "SigType", "lifts_to": "types", "input": "stripped binaries", "strength": "type inference"}], ["native", "SigDeobf", "Signature-original: deobfuscation passes simplifying packed/encrypted code. Lifts to clean IR; input: obfuscated. Strength: unpacking.", {"tool": "SigDeobf", "lifts_to": "clean IR", "input": "obfuscated", "strength": "unpacking"}], ["firmware", "SigFirm", "Signature-original: firmware pipeline extracting and decompiling images. Lifts to C; input: firmware images. Strength: embedded.", {"tool": "SigFirm", "lifts_to": "C", "input": "firmware images", "strength": "embedded"}], ["web", "SigWasm-Dec", "Signature-original: WASM decompiler with high-level control-flow recovery. Lifts to readable C; input: WASM. Strength: control flow.", {"tool": "SigWasm-Dec", "lifts_to": "readable C", "input": "WASM", "strength": "control flow"}], ["managed", "SigManaged", "Signature-original: managed-code decompiler for Sig bytecode. Lifts to Sig source; input: Sig bytecode. Strength: round-trip.", {"tool": "SigManaged", "lifts_to": "Sig source", "input": "Sig bytecode", "strength": "round-trip"}], ["tooling", "SigSymbol-Rebuild", "Signature-original: symbol reconstruction from debug remnants. Lifts to symbols; input: stripped. Strength: recovery.", {"tool": "SigSymbol", "lifts_to": "symbols", "input": "stripped", "strength": "recovery"}], ["tooling", "SigPatch-Gen", "Signature-original: patch generation from decompiled diffs. Lifts to patches; input: binary pair. Strength: hotfix gen.", {"tool": "SigPatch", "lifts_to": "patches", "input": "binary pair", "strength": "hotfix gen"}], ["tooling", "SigVuln-Scan", "Signature-original: vulnerability patterns matched on lifted IR. Lifts to findings; input: binaries. Strength: detection.", {"tool": "SigVuln", "lifts_to": "findings", "input": "binaries", "strength": "detection"}], ["native", "SigRecomp", "Signature-original: recompile decompiled output for another architecture. Lifts to new binary; input: decompiled C. Strength: retarget.", {"tool": "SigRecomp", "lifts_to": "new binary", "input": "decompiled C", "strength": "retarget"}], ["tooling", "SigAudit-Bin", "Signature-original: binary audit trails proving provenance of builds. Lifts to provenance; input: build outputs. Strength: supply chain.", {"tool": "SigAudit-Bin", "lifts_to": "provenance", "input": "build outputs", "strength": "supply chain"}], ["native", "SigDecomp-One", "Signature-original: the united decompilation plane — every input, one IR. Lifts to SigIR; input: everything. Strength: unified.", {"tool": "SigDecomp-One", "lifts_to": "SigIR", "input": "everything", "strength": "unified"}]];
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
  if(!new RegExp('^'+'JAH\\-BINARY\\-S\\-'+'\\d{6}$').test(r.id||''))e.push('id');
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('binary-decompilation-pipelines-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
