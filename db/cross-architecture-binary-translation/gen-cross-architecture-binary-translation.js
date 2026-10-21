(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];} function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var CATS=["dynamic", "static", "os-layer", "hardware", "gaming"];
var PREFIX='JAH-CABT-';
var GENVER='jahdb-cross-architecture-binary-translation-1.0';
var SRC='public-harvest';
var EDITION='public';
var PROV="Public record compiled from openly published documentation, project sources, and standard references.";
var FIELDS=["translator", "from_arch", "to_arch", "method"];
var DEMO_TPL="// $TITLE - translation mapping demo\nvar MAP = { \"x86:mov\": \"arm:mov\", \"x86:add\": \"arm:add\", \"x86:jmp\": \"arm:b\" };\nfunction translate(insn) {\n  var key = \"x86:\" + insn.split(\" \")[0];\n  return (MAP[key] || \"arm:??\") + insn.slice(insn.indexOf(\" \"));\n}\nvar prog = [\"mov eax, 1\", \"add eax, 2\", \"jmp done\"];\nconsole.log(\"Translator: $TRANSLATOR | $FROM_ARCH -> $TO_ARCH\");\nprog.forEach(function(i) { console.log(\"  \" + i + \"  =>  \" + translate(i)); });\nconsole.log(\"Method: $METHOD -> PASS\");";
function jsEsc(s){return String(s).replace(/\\/g,'\\\\').replace(/"/g,'\\"').replace(/\n/g,'\\n').replace(/\r/g,'\\r').replace(/\t/g,'\\t');}
function fillTpl(tpl,vars){return tpl.replace(/\$([A-Za-z0-9_]+)/g,function(m,k){return Object.prototype.hasOwnProperty.call(vars,k)?jsEsc(vars[k]):m;});}
/* rows: [category, title, description, {fields}] */
var B=[["dynamic", "Rosetta 2", "Apple’s ahead-of-time + JIT translation running Intel apps on Apple Silicon. Translates x86_64 to aarch64 via AOT + JIT.", {"translator": "Rosetta 2", "from_arch": "x86_64", "to_arch": "aarch64", "method": "AOT + JIT"}], ["dynamic", "Rosetta 1", "The original PowerPC-to-Intel translator in early OS X. Translates PowerPC to x86 via dynamic translation.", {"translator": "Rosetta 1", "from_arch": "PowerPC", "to_arch": "x86", "method": "dynamic translation"}], ["dynamic", "QEMU user-mode", "Runs foreign-arch Linux binaries via syscall translation, a dev staple. Translates many to host via dynamic binary translation.", {"translator": "QEMU user", "from_arch": "many", "to_arch": "host", "method": "dynamic binary translation"}], ["dynamic", "box86", "Runs x86 Linux programs on ARM with wrapped native libraries for speed. Translates x86 to ARM 32-bit via dynarec + lib wrapping.", {"translator": "box86", "from_arch": "x86", "to_arch": "ARM 32-bit", "method": "dynarec + lib wrapping"}], ["dynamic", "box64", "The 64-bit sibling translating x86_64 to AArch64 on Pi and handhelds. Translates x86_64 to aarch64 via dynarec + lib wrapping.", {"translator": "box64", "from_arch": "x86_64", "to_arch": "aarch64", "method": "dynarec + lib wrapping"}], ["os-layer", "Windows on Arm emulation", "Windows 11 runs x86/x64 apps on Arm via built-in emulation. Translates x86/x64 to aarch64 via OS-integrated JIT.", {"translator": "WoA emulation", "from_arch": "x86/x64", "to_arch": "aarch64", "method": "OS-integrated JIT"}], ["os-layer", "Intel Houdini", "Android’s ARM-to-x86 translator letting ARM apps run on x86 Chromebooks. Translates ARM to x86 via dynamic translation.", {"translator": "Houdini", "from_arch": "ARM", "to_arch": "x86", "method": "dynamic translation"}], ["dynamic", "ExaGear", "Eltechs’ x86-on-ARM translator popular on Raspberry Pi before box86. Translates x86 to ARM via dynamic translation.", {"translator": "ExaGear", "from_arch": "x86", "to_arch": "ARM", "method": "dynamic translation"}], ["dynamic", "DEC FX!32", "1990s profiler-guided x86-on-Alpha translation for Windows NT. Translates x86 to Alpha via profiled translation.", {"translator": "FX!32", "from_arch": "x86", "to_arch": "Alpha", "method": "profiled translation"}], ["hardware", "Transmeta Code Morphing", "Crusoe/Efficeon CPUs translated x86 to VLIW in software. Translates x86 to VLIW via software code morphing.", {"translator": "Code Morphing", "from_arch": "x86", "to_arch": "VLIW", "method": "software code morphing"}], ["dynamic", "HP Dynamo", "The research system that pioneered dynamic optimization of running binaries. Translates PA-RISC/x86 to same (optimized) via dynamic optimization.", {"translator": "Dynamo", "from_arch": "PA-RISC/x86", "to_arch": "same (optimized)", "method": "dynamic optimization"}], ["os-layer", "IA-32 Execution Layer", "Intel’s x86 emulation layer for Itanium Windows/Linux. Translates x86 to IA-64 via OS emulation layer.", {"translator": "IA-32 EL", "from_arch": "x86", "to_arch": "IA-64", "method": "OS emulation layer"}], ["gaming", "DOSBox dynarec", "DOSBox’s dynamic core recompiles x86 on the fly for retro gaming. Translates x86 real-mode to host via dynamic recompilation.", {"translator": "DOSBox", "from_arch": "x86 real-mode", "to_arch": "host", "method": "dynamic recompilation"}], ["dynamic", "SheepShaver", "PowerPC Mac emulator with a JIT for classic Mac OS. Translates PowerPC to host via JIT emulation.", {"translator": "SheepShaver", "from_arch": "PowerPC", "to_arch": "host", "method": "JIT emulation"}], ["dynamic", "PearPC", "PowerPC emulator that once ran OS X on x86 via interpretation/JIT. Translates PowerPC to x86 via JIT emulation.", {"translator": "PearPC", "from_arch": "PowerPC", "to_arch": "x86", "method": "JIT emulation"}]];
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
  if(!new RegExp('^'+'JAH\\-CABT\\-'+'\\d{6}$').test(r.id||''))e.push('id');
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('cross-architecture-binary-translation',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
