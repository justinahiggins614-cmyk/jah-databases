(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];} function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var CATS=["c", "rust", "jvm", "browser", "post-link"];
var PREFIX='JAH-PGO-';
var GENVER='jahdb-profile-guided-optimization-pgo-1.0';
var SRC='public-harvest';
var EDITION='public';
var PROV="Public record compiled from openly published documentation, project sources, and standard references.";
var FIELDS=["technique", "toolchain", "workflow", "gain"];
var DEMO_TPL="// $TITLE - profile-guided decision demo\nvar profile = { \"hot:render\": 9500, \"cold:init\": 12, \"warm:parse\": 800 };\nfunction decide(fn) {\n  var hits = profile[fn] || 0;\n  if (hits > 5000) return \"compile -O3 + inline aggressively\";\n  if (hits > 100) return \"compile -O2\";\n  return \"compile -Os (cold)\";\n}\nconsole.log(\"Technique: $TECHNIQUE | Toolchain: $TOOLCHAIN\");\nObject.keys(profile).forEach(function(f) { console.log(\"  \" + f + \" (\" + profile[f] + \" hits) -> \" + decide(f)); });\nconsole.log(\"Hot path gets max optimization -> PASS\");";
function jsEsc(s){return String(s).replace(/\\/g,'\\\\').replace(/"/g,'\\"').replace(/\n/g,'\\n').replace(/\r/g,'\\r').replace(/\t/g,'\\t');}
function fillTpl(tpl,vars){return tpl.replace(/\$([A-Za-z0-9_]+)/g,function(m,k){return Object.prototype.hasOwnProperty.call(vars,k)?jsEsc(vars[k]):m;});}
/* rows: [category, title, description, {fields}] */
var B=[["c", "GCC -fprofile-generate/use", "Two-phase: instrument, run workload, recompile with profiles. Toolchain: GCC. Workflow: -fprofile-generate run, -fprofile-use build. Typical gain: 10-20%.", {"technique": "instrumented PGO", "toolchain": "GCC", "workflow": "-fprofile-generate run, -fprofile-use build", "gain": "10-20%"}], ["c", "LLVM PGO", "Clang’s -fprofile-instr-generate/use with llvm-profdata merging. Toolchain: Clang/LLVM. Workflow: instr-generate, merge, use. Typical gain: 10-25%.", {"technique": "instrumented PGO", "toolchain": "Clang/LLVM", "workflow": "instr-generate, merge, use", "gain": "10-25%"}], ["c", "MSVC /LTCG:PGO", "Profile-guided optimization for Windows with pgomgr/pgoauto workflows. Toolchain: MSVC. Workflow: instrument, train, optimize. Typical gain: 10-15%.", {"technique": "PGO", "toolchain": "MSVC", "workflow": "instrument, train, optimize", "gain": "10-15%"}], ["c", "Go PGO (1.20+)", "Go builds consume pprof CPU profiles via -pgo=auto for devirtualization. Toolchain: Go. Workflow: -pgo=auto with default.pgo. Typical gain: 2-7%.", {"technique": "profile-guided", "toolchain": "Go", "workflow": "-pgo=auto with default.pgo", "gain": "2-7%"}], ["rust", "Rust PGO", "rustc -Cprofile-generate/use with LLVM profile data. Toolchain: rustc. Workflow: build, train, rebuild. Typical gain: 10-20%.", {"technique": "LLVM PGO", "toolchain": "rustc", "workflow": "build, train, rebuild", "gain": "10-20%"}], ["browser", "V8 type feedback PGO", "Runtime type profiles drive TurboFan speculation — PGO by design. Toolchain: V8. Workflow: automatic. Typical gain: built-in.", {"technique": "feedback PGO", "toolchain": "V8", "workflow": "automatic", "gain": "built-in"}], ["jvm", "HotSpot tiered PGO", "Interpreter profiles feed C2; always-on PGO in the JVM. Toolchain: HotSpot. Workflow: automatic. Typical gain: built-in.", {"technique": "tiered PGO", "toolchain": "HotSpot", "workflow": "automatic", "gain": "built-in"}], ["browser", "Chrome PGO builds", "Official Chrome builds train on benchmarks for layout/JS hot paths. Toolchain: Clang. Workflow: train on workloads. Typical gain: ~10% startup.", {"technique": "instrumented PGO", "toolchain": "Clang", "workflow": "train on workloads", "gain": "~10% startup"}], ["browser", "Firefox PGO", "Firefox’s build trains PGO+LTO on Talos workloads. Toolchain: Clang/Rust. Workflow: profiled build. Typical gain: 10%+.", {"technique": "PGO+LTO", "toolchain": "Clang/Rust", "workflow": "profiled build", "gain": "10%+"}], ["jvm", ".NET dynamic PGO", "RyuJIT consumes runtime profiles for devirtualization and inlining. Toolchain: .NET. Workflow: DOTNET_TieredPGO=1. Typical gain: 5-15%.", {"technique": "dynamic PGO", "toolchain": ".NET", "workflow": "DOTNET_TieredPGO=1", "gain": "5-15%"}], ["c", "Python PGO builds", "CPython’s --with-pgo trains the interpreter on the test suite. Toolchain: GCC/Clang. Workflow: make profile-opt. Typical gain: 10-20%.", {"technique": "build-time PGO", "toolchain": "GCC/Clang", "workflow": "make profile-opt", "gain": "10-20%"}], ["post-link", "BOLT post-link", "Facebook’s Binary Optimization and Layout Tool reorders code post-link. Toolchain: BOLT. Workflow: perf sample, bolt binary. Typical gain: 5-15%.", {"technique": "post-link PGO", "toolchain": "BOLT", "workflow": "perf sample, bolt binary", "gain": "5-15%"}], ["c", "AutoFDO", "Sample-based PGO from perf data without instrumentation builds. Toolchain: GCC/LLVM. Workflow: perf record, create_gcov, build. Typical gain: 5-15%.", {"technique": "sample PGO", "toolchain": "GCC/LLVM", "workflow": "perf record, create_gcov, build", "gain": "5-15%"}], ["post-link", "Propeller", "Google’s post-link optimizer with basic-block sections. Toolchain: Clang/LLD. Workflow: perf + propeller. Typical gain: 5-10%.", {"technique": "post-link", "toolchain": "Clang/LLD", "workflow": "perf + propeller", "gain": "5-10%"}], ["c", "CSS PGO (ThinLTO)", "ThinLTO + PGO combos in Chromium’s official builds. Toolchain: Clang. Workflow: combined. Typical gain: 15%+.", {"technique": "PGO+LTO", "toolchain": "Clang", "workflow": "combined", "gain": "15%+"}]];
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
  if(!new RegExp('^'+'JAH\\-PGO\\-'+'\\d{6}$').test(r.id||''))e.push('id');
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('profile-guided-optimization-pgo',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
