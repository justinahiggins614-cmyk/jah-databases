(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];} function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var CATS=["llvm", "jvm", "js", "wasm", "mobile"];
var PREFIX='JAH-BYTECO-';
var GENVER='jahdb-bytecode-optimization-passes-1.0';
var SRC='public-harvest';
var EDITION='public';
var PROV="Public record compiled from openly published documentation, project sources, and standard references.";
var FIELDS=["pass", "runs_on", "does", "order"];
var DEMO_TPL="// $TITLE - optimization pass demo (constant folding)\nfunction fold(node) {\n  if (node.op === \"add\" && typeof node.l === \"number\" && typeof node.r === \"number\")\n    return { op: \"const\", v: node.l + node.r };\n  return node;\n}\nvar before = { op: \"add\", l: 20, r: 22 };\nvar after = fold(before);\nconsole.log(\"Pass: $PASS | Runs on: $RUNS_ON\");\nconsole.log(\"Before: \" + JSON.stringify(before));\nconsole.log(\"After:  \" + JSON.stringify(after));\nconsole.log(\"Constant folded at compile time -> PASS\");";
function jsEsc(s){return String(s).replace(/\\/g,'\\\\').replace(/"/g,'\\"').replace(/\n/g,'\\n').replace(/\r/g,'\\r').replace(/\t/g,'\\t');}
function fillTpl(tpl,vars){return tpl.replace(/\$([A-Za-z0-9_]+)/g,function(m,k){return Object.prototype.hasOwnProperty.call(vars,k)?jsEsc(vars[k]):m;});}
/* rows: [category, title, description, {fields}] */
var B=[["llvm", "LLVM instcombine", "Combines redundant instructions into simpler forms — the peephole workhorse. Runs on LLVM IR; it folds instruction patterns. Pipeline order: early, repeated.", {"pass": "instcombine", "runs_on": "LLVM IR", "does": "folds instruction patterns", "order": "early, repeated"}], ["llvm", "LLVM GVN", "Global value numbering eliminates redundant computations across blocks. Runs on LLVM IR; it removes redundant loads/computes. Pipeline order: mid pipeline.", {"pass": "gvn", "runs_on": "LLVM IR", "does": "removes redundant loads/computes", "order": "mid pipeline"}], ["llvm", "LLVM LICM", "Hoists loop-invariant code out of loops. Runs on LLVM IR; it hoists invariants. Pipeline order: after loop opts.", {"pass": "licm", "runs_on": "LLVM IR", "does": "hoists invariants", "order": "after loop opts"}], ["llvm", "LLVM SROA", "Scalar replacement of aggregates breaks structs into SSA values. Runs on LLVM IR; it promotes allocas. Pipeline order: early.", {"pass": "sroa", "runs_on": "LLVM IR", "does": "promotes allocas", "order": "early"}], ["llvm", "LLVM loop unrolling", "Unrolls loops with known trip counts to expose ILP. Runs on LLVM IR; it unrolls loops. Pipeline order: late loop opts.", {"pass": "loop-unroll", "runs_on": "LLVM IR", "does": "unrolls loops", "order": "late loop opts"}], ["llvm", "LLVM inlining", "Inlines callees using cost models and profiles. Runs on LLVM IR; it inlines functions. Pipeline order: early + CGSCC.", {"pass": "inline", "runs_on": "LLVM IR", "does": "inlines functions", "order": "early + CGSCC"}], ["jvm", "CPython peephole", "The classic bytecode peepholer folding constants in code objects. Runs on CPython bytecode; it constant folds. Pipeline order: compile time.", {"pass": "peephole", "runs_on": "CPython bytecode", "does": "constant folds", "order": "compile time"}], ["js", "V8 TurboFan typed lowering", "Lowers simplified operators to machine ops using type feedback. Runs on TurboFan IR; it type-based lowering. Pipeline order: mid TurboFan.", {"pass": "typed-lowering", "runs_on": "TurboFan IR", "does": "type-based lowering", "order": "mid TurboFan"}], ["mobile", "ART dex2oat", "Android’s AOT compiler optimizing dex with an SSA backend. Runs on dex bytecode; it AOT optimize. Pipeline order: install time.", {"pass": "dex2oat", "runs_on": "dex bytecode", "does": "AOT optimize", "order": "install time"}], ["wasm", "Binaryen precompute", "Evaluates constant expressions at compile time in WASM. Runs on WASM; it constant propagation. Pipeline order: wasm-opt.", {"pass": "precompute", "runs_on": "WASM", "does": "constant propagation", "order": "wasm-opt"}], ["wasm", "Binaryen dead-code-elim", "Removes unreachable WASM functions and code. Runs on WASM; it removes dead code. Pipeline order: wasm-opt.", {"pass": "dead-code-elimination", "runs_on": "WASM", "does": "removes dead code", "order": "wasm-opt"}], ["jvm", ".NET RyuJIT morph", "RyuJIT’s morph phase simplifies IR before lowering. Runs on .NET IR; it IR simplification. Pipeline order: early JIT.", {"pass": "morph", "runs_on": ".NET IR", "does": "IR simplification", "order": "early JIT"}], ["jvm", "JVM C2 ideal graph opts", "C2’s ideal-graph optimizations: IGVN, loop opts, macro expansion. Runs on HotSpot ideal graph; it global opts. Pipeline order: C2 pipeline.", {"pass": "C2 ideal opts", "runs_on": "HotSpot ideal graph", "does": "global opts", "order": "C2 pipeline"}], ["js", "LuaJIT IR opts", "LuaJIT’s trace IR passes: CSE, DCE, alias analysis on traces. Runs on LuaJIT IR; it trace optimization. Pipeline order: per trace.", {"pass": "trace IR opts", "runs_on": "LuaJIT IR", "does": "trace optimization", "order": "per trace"}], ["mobile", "Dalvik dex optimizer", "The old Dalvik verifier/optimizer quickening bytecodes at install. Runs on dex; it bytecode quickening. Pipeline order: install.", {"pass": "dexopt", "runs_on": "dex", "does": "bytecode quickening", "order": "install"}]];
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
  if(!new RegExp('^'+'JAH\\-BYTECO\\-'+'\\d{6}$').test(r.id||''))e.push('id');
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('bytecode-optimization-passes',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
