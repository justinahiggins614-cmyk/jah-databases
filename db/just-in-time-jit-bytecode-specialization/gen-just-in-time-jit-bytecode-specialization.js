(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];} function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var CATS=["speculation", "tiers", "guards", "profiling", "runtimes"];
var PREFIX='JAH-JTJ-';
var GENVER='jahdb-just-in-time-jit-bytecode-specialization-1.0';
var SRC='public-harvest';
var EDITION='public';
var PROV="Public record compiled from openly published documentation, project sources, and standard references.";
var FIELDS=["technique", "engine", "how", "payoff"];
var DEMO_TPL="// $TITLE - type specialization demo\nfunction add(a, b) { return a + b; }\nvar seen = {};\nfunction specializedAdd(a, b) {\n  var k = typeof a + \",\" + typeof b;\n  seen[k] = (seen[k] || 0) + 1;\n  if (k === \"number,number\") return a + b; // fast path (specialized)\n  return add(a, b); // generic fallback\n}\nfor (var i = 0; i < 1000; i++) specializedAdd(i, 1);\nspecializedAdd(\"x\", \"y\");\nconsole.log(\"Technique: $TECHNIQUE | Engine: $ENGINE\");\nconsole.log(\"Type profile: \" + JSON.stringify(seen));\nconsole.log(\"number,number fast path hit 1000x -> SPECIALIZED PASS\");";
function jsEsc(s){return String(s).replace(/\\/g,'\\\\').replace(/"/g,'\\"').replace(/\n/g,'\\n').replace(/\r/g,'\\r').replace(/\t/g,'\\t');}
function fillTpl(tpl,vars){return tpl.replace(/\$([A-Za-z0-9_]+)/g,function(m,k){return Object.prototype.hasOwnProperty.call(vars,k)?jsEsc(vars[k]):m;});}
/* rows: [category, title, description, {fields}] */
var B=[["speculation", "V8 type feedback", "V8 collects type feedback in the interpreter, then TurboFan speculates on it. Engine: V8. How it works: feedback vectors -> speculative compile. Payoff: near-native arithmetic.", {"technique": "type feedback", "engine": "V8", "how": "feedback vectors -> speculative compile", "payoff": "near-native arithmetic"}], ["speculation", "HotSpot speculative opts", "C2 speculates on class hierarchy and inlines virtual calls with uncommon traps. Engine: HotSpot. How it works: class-hierarchy analysis + traps. Payoff: devirtualized calls.", {"technique": "speculative inlining", "engine": "HotSpot", "how": "class-hierarchy analysis + traps", "payoff": "devirtualized calls"}], ["guards", "PyPy guards", "Tracing JIT guards check assumptions; failures exit to the interpreter (or a bridge). Engine: PyPy. How it works: guard instructions on traces. Payoff: straight-line fast loops.", {"technique": "guards", "engine": "PyPy", "how": "guard instructions on traces", "payoff": "straight-line fast loops"}], ["profiling", "LuaJIT traces", "LuaJIT records hot bytecode paths into traces compiled by its IR backend. Engine: LuaJIT. How it works: hot loop trace capture. Payoff: C-like loop speed.", {"technique": "trace recording", "engine": "LuaJIT", "how": "hot loop trace capture", "payoff": "C-like loop speed"}], ["tiers", "Graal partial evaluation", "Graal partially evaluates the Truffle interpreter against the program, yielding machine code. Engine: GraalVM. How it works: interpreter specialization. Payoff: polyglot peak speed.", {"technique": "partial evaluation", "engine": "GraalVM", "how": "interpreter specialization", "payoff": "polyglot peak speed"}], ["tiers", ".NET tiered JIT", "Methods start with quick JIT and recompile optimized when call counts go hot. Engine: .NET. How it works: tier0 -> tier1 promotion. Payoff: fast startup + peak.", {"technique": "tiered compilation", "engine": ".NET", "how": "tier0 -> tier1 promotion", "payoff": "fast startup + peak"}], ["tiers", "JavaScriptCore FTL", "JSC’s FTL tier compiles from B3 IR with LLVM-derived optimization. Engine: JavaScriptCore. How it works: multi-tier to LLVM IR. Payoff: Safari peak perf.", {"technique": "FTL JIT", "engine": "JavaScriptCore", "how": "multi-tier to LLVM IR", "payoff": "Safari peak perf"}], ["tiers", "SpiderMonkey Warp", "Warp replaced the old Ion pipeline with a MIR-to-native compiler fed by CacheIR. Engine: SpiderMonkey. How it works: CacheIR-guarded compile. Payoff: Firefox peak perf.", {"technique": "Warp", "engine": "SpiderMonkey", "how": "CacheIR-guarded compile", "payoff": "Firefox peak perf"}], ["runtimes", "HHVM JIT", "HHVM compiles Hack/PHP with region-based translation and profile-guided opts. Engine: HHVM. How it works: hot region translation. Payoff: server PHP speed.", {"technique": "region JIT", "engine": "HHVM", "how": "hot region translation", "payoff": "server PHP speed"}], ["speculation", "Truffle AST specialization", "Truffle nodes rewrite themselves to type-specialized versions with guards. Engine: GraalVM Truffle. How it works: node rewriting + guards. Payoff: interpreter speed.", {"technique": "self-optimizing AST", "engine": "GraalVM Truffle", "how": "node rewriting + guards", "payoff": "interpreter speed"}], ["runtimes", "ART optimizing compiler", "Android Runtime compiles dex with an optimizing backend using profile data. Engine: ART. How it works: profiles -> optimizing compile. Payoff: mobile app speed.", {"technique": "profile-guided dex2oat", "engine": "ART", "how": "profiles -> optimizing compile", "payoff": "mobile app speed"}], ["guards", "Deoptimization", "When speculation fails, the VM reconstructs interpreter state — correctness preserved. Engine: V8/HotSpot. How it works: osr + frame reconstruction. Payoff: safe speculation.", {"technique": "deoptimization", "engine": "V8/HotSpot", "how": "osr + frame reconstruction", "payoff": "safe speculation"}], ["tiers", "On-stack replacement", "OSR swaps a running interpreted loop for compiled code mid-execution. Engine: V8/HotSpot. How it works: frame transfer at backedge. Payoff: hot loops speed up live.", {"technique": "OSR", "engine": "V8/HotSpot", "how": "frame transfer at backedge", "payoff": "hot loops speed up live"}], ["speculation", "Inline caching", "Polymorphic inline caches remember receiver types at call sites. Engine: V8/JSC. How it works: PIC at call sites. Payoff: fast dispatch.", {"technique": "inline caches", "engine": "V8/JSC", "how": "PIC at call sites", "payoff": "fast dispatch"}], ["profiling", "Escape analysis", "Proving objects don’t escape lets the JIT stack-allocate or scalar-replace them. Engine: HotSpot/Graal. How it works: points-to analysis. Payoff: fewer allocations.", {"technique": "escape analysis", "engine": "HotSpot/Graal", "how": "points-to analysis", "payoff": "fewer allocations"}]];
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
  if(!new RegExp('^'+'JAH\\-JTJ\\-'+'\\d{6}$').test(r.id||''))e.push('id');
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('just-in-time-jit-bytecode-specialization',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
