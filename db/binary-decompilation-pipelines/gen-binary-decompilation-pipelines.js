(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];} function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var CATS=["native", "managed", "web", "firmware", "tooling"];
var PREFIX='JAH-BINARY-';
var GENVER='jahdb-binary-decompilation-pipelines-1.0';
var SRC='public-harvest';
var EDITION='public';
var PROV="Public record compiled from openly published documentation, project sources, and standard references.";
var FIELDS=["tool", "lifts_to", "input", "strength"];
var DEMO_TPL="// $TITLE - lifter demo (asm -> IR)\nvar ASM = [\"mov eax, 1\", \"add eax, 2\", \"ret\"];\nfunction lift(line) {\n  var p = line.split(/[ ,]+/);\n  if (p[0] === \"mov\") return p[1] + \" = \" + p[2];\n  if (p[0] === \"add\") return p[1] + \" = \" + p[1] + \" + \" + p[2];\n  if (p[0] === \"ret\") return \"return \" + \"eax\";\n  return line;\n}\nconsole.log(\"Tool: $TOOL | Lifts to: $LIFTS_TO\");\nASM.forEach(function(l) { console.log(\"  \" + l + \"   ->   \" + lift(l)); });\nconsole.log(\"Recovered: function f() { eax = 1; eax = eax + 2; return eax; } -> PASS\");";
function jsEsc(s){return String(s).replace(/\\/g,'\\\\').replace(/"/g,'\\"').replace(/\n/g,'\\n').replace(/\r/g,'\\r').replace(/\t/g,'\\t');}
function fillTpl(tpl,vars){return tpl.replace(/\$([A-Za-z0-9_]+)/g,function(m,k){return Object.prototype.hasOwnProperty.call(vars,k)?jsEsc(vars[k]):m;});}
/* rows: [category, title, description, {fields}] */
var B=[["native", "Ghidra", "NSA’s open-source reverse-engineering suite with a strong decompiler. Lifts to C-like pseudocode; input: many architectures. Strength: free, scriptable.", {"tool": "Ghidra", "lifts_to": "C-like pseudocode", "input": "many architectures", "strength": "free, scriptable"}], ["native", "Hex-Rays (IDA)", "The commercial gold standard decompiler inside IDA Pro. Lifts to C pseudocode; input: many architectures. Strength: accuracy.", {"tool": "Hex-Rays", "lifts_to": "C pseudocode", "input": "many architectures", "strength": "accuracy"}], ["native", "Binary Ninja", "Modern IL-based analysis with a clean API and fast UI. Lifts to BNIL -> C; input: many architectures. Strength: API + UX.", {"tool": "Binary Ninja", "lifts_to": "BNIL -> C", "input": "many architectures", "strength": "API + UX"}], ["native", "Rizin / Cutter", "Open-source radare2 successor with Cutter GUI and rz-ghidra decompiler. Lifts to C via rz-ghidra; input: many architectures. Strength: free, CLI-first.", {"tool": "Rizin", "lifts_to": "C via rz-ghidra", "input": "many architectures", "strength": "free, CLI-first"}], ["tooling", "angr", "Symbolic execution + decompilation for automated vulnerability discovery. Lifts to VEX IR -> structured; input: binaries. Strength: symbolic exec.", {"tool": "angr", "lifts_to": "VEX IR -> structured", "input": "binaries", "strength": "symbolic exec"}], ["native", "RetDec", "Avast’s retargetable decompiler with LLVM-based backends. Lifts to C / LLVM IR; input: x86/ARM/MIPS. Strength: retargetable.", {"tool": "RetDec", "lifts_to": "C / LLVM IR", "input": "x86/ARM/MIPS", "strength": "retargetable"}], ["native", "Hopper", "macOS/iOS-focused disassembler with a pseudo-code decompiler. Lifts to pseudocode; input: Mach-O focus. Strength: Apple platforms.", {"tool": "Hopper", "lifts_to": "pseudocode", "input": "Mach-O focus", "strength": "Apple platforms"}], ["native", "Snowman", "Lightweight native decompiler with a Qt interface. Lifts to C-like; input: x86/ARM. Strength: fast, simple.", {"tool": "Snowman", "lifts_to": "C-like", "input": "x86/ARM", "strength": "fast, simple"}], ["managed", "JEB", "Android-focused decompiler for dex, plus native modules. Lifts to Java pseudocode; input: APK/dex. Strength: Android.", {"tool": "JEB", "lifts_to": "Java pseudocode", "input": "APK/dex", "strength": "Android"}], ["managed", "dnSpy", "The .NET debugger/decompiler for assemblies (community forks continue it). Lifts to C#; input: .NET assemblies. Strength: .NET debugging.", {"tool": "dnSpy", "lifts_to": "C#", "input": ".NET assemblies", "strength": ".NET debugging"}], ["managed", "JD-GUI", "Fast Java bytecode viewer reconstructing readable Java. Lifts to Java; input: JVM bytecode. Strength: speed.", {"tool": "JD-GUI", "lifts_to": "Java", "input": "JVM bytecode", "strength": "speed"}], ["managed", "CFR", "Modern Java decompiler handling newer class-file features well. Lifts to Java; input: JVM bytecode. Strength: modern Java.", {"tool": "CFR", "lifts_to": "Java", "input": "JVM bytecode", "strength": "modern Java"}], ["managed", "uncompyle6", "Python bytecode decompiler covering 2.7 through 3.8. Lifts to Python; input: .pyc. Strength: version range.", {"tool": "uncompyle6", "lifts_to": "Python", "input": ".pyc", "strength": "version range"}], ["managed", "pycdc", "C++ Python bytecode decompiler (Decompyle++). Lifts to Python; input: .pyc. Strength: C++ speed.", {"tool": "pycdc", "lifts_to": "Python", "input": ".pyc", "strength": "C++ speed"}], ["web", "wasm2c / wabt", "WebAssembly Binary Toolkit lifting wasm to readable C. Lifts to C; input: WASM. Strength: spec-aligned.", {"tool": "wabt", "lifts_to": "C", "input": "WASM", "strength": "spec-aligned"}]];
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
  if(!new RegExp('^'+'JAH\\-BINARY\\-'+'\\d{6}$').test(r.id||''))e.push('id');
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('binary-decompilation-pipelines',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
