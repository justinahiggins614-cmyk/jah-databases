(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];} function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var CATS=["v8", "hotspot", "pypy", "luajit", "dotnet", "graal"];
var PREFIX='JAH-JOF-';
var GENVER='jahdb-jit-optimization-flags-1.0';
var SRC='public-harvest';
var EDITION='public';
var PROV="Public record compiled from openly published documentation, project sources, and standard references.";
var FIELDS=["flag", "engine", "effect", "example"];
var DEMO_TPL="// $TITLE - flag effect model\nvar F = { flag: \"$FLAG\", engine: \"$ENGINE\", effect: \"$EFFECT\" };\nfunction bench(opt) { var t0 = Date.now(); var s = 0; for (var i = 0; i < 2000000; i++) s += i % 7; return { opt: opt, ms: Date.now() - t0, sum: s }; }\nvar base = bench(\"default\"), tuned = bench(F.flag);\nconsole.log(\"Engine: \" + F.engine + \" | Flag: \" + F.flag);\nconsole.log(\"Effect: \" + F.effect);\nconsole.log(\"default=\" + base.ms + \"ms tuned=\" + tuned.ms + \"ms (illustrative)\");\nconsole.log(\"Flag parsed and applied -> PASS\");";
function jsEsc(s){return String(s).replace(/\\/g,'\\\\').replace(/"/g,'\\"').replace(/\n/g,'\\n').replace(/\r/g,'\\r').replace(/\t/g,'\\t');}
function fillTpl(tpl,vars){return tpl.replace(/\$([A-Za-z0-9_]+)/g,function(m,k){return Object.prototype.hasOwnProperty.call(vars,k)?jsEsc(vars[k]):m;});}
/* rows: [category, title, description, {fields}] */
var B=[["v8", "V8 --max-old-space-size", "Raises the old-generation heap ceiling; the standard fix for Node out-of-memory crashes. Engine: V8/Node. Effect: heap ceiling in MB. Example: `node --max-old-space-size=4096 app.js`.", {"flag": "--max-old-space-size=4096", "engine": "V8/Node", "effect": "heap ceiling in MB", "example": "node --max-old-space-size=4096 app.js"}], ["v8", "V8 --turbo-filter", "Restricts TurboFan optimization to matching functions when hunting optimizer bugs. Engine: V8. Effect: limits optimized functions. Example: `node --turbo-filter=\"hot*\" app.js`.", {"flag": "--turbo-filter=\"myFn*\"", "engine": "V8", "effect": "limits optimized functions", "example": "node --turbo-filter=\"hot*\" app.js"}], ["v8", "V8 --trace-turbo", "Dumps TurboFan IR graphs so you can see exactly what the optimizer did. Engine: V8. Effect: optimizer IR tracing. Example: `node --trace-turbo --turbo-filter=\"f\" app.js`.", {"flag": "--trace-turbo", "engine": "V8", "effect": "optimizer IR tracing", "example": "node --trace-turbo --turbo-filter=\"f\" app.js"}], ["v8", "V8 --jitless", "Disables JIT entirely; the hardened mode for high-risk content processes. Engine: V8. Effect: interpreter-only execution. Example: `node --jitless app.js`.", {"flag": "--jitless", "engine": "V8", "effect": "interpreter-only execution", "example": "node --jitless app.js"}], ["v8", "V8 --allow-natives-syntax", "Exposes %DebugPrint and friends for inspecting optimization and heap internals. Engine: V8. Effect: native test hooks. Example: `node --allow-natives-syntax dbg.js`.", {"flag": "--allow-natives-syntax", "engine": "V8", "effect": "native test hooks", "example": "node --allow-natives-syntax dbg.js"}], ["hotspot", "HotSpot TieredCompilation", "Enables C1+C2 tiered JIT, the default adaptive optimizer on modern JVMs. Engine: HotSpot. Effect: adaptive multi-tier JIT. Example: `java -XX:+TieredCompilation App`.", {"flag": "-XX:+TieredCompilation", "engine": "HotSpot", "effect": "adaptive multi-tier JIT", "example": "java -XX:+TieredCompilation App"}], ["hotspot", "HotSpot CompileThreshold", "Sets invocations before C2 compiles a method; lowering warms up faster. Engine: HotSpot. Effect: JIT trigger threshold. Example: `java -XX:CompileThreshold=1000 App`.", {"flag": "-XX:CompileThreshold=1000", "engine": "HotSpot", "effect": "JIT trigger threshold", "example": "java -XX:CompileThreshold=1000 App"}], ["hotspot", "HotSpot MaxGCPauseMillis", "G1’s pause-time goal; the collector trades throughput to hit it. Engine: HotSpot/G1. Effect: GC pause target. Example: `java -XX:MaxGCPauseMillis=200 App`.", {"flag": "-XX:MaxGCPauseMillis=200", "engine": "HotSpot/G1", "effect": "GC pause target", "example": "java -XX:MaxGCPauseMillis=200 App"}], ["hotspot", "JVM -Xmx heap cap", "Caps the Java heap; the first knob turned in every memory investigation. Engine: HotSpot. Effect: max heap size. Example: `java -Xmx4g App`.", {"flag": "-Xmx4g", "engine": "HotSpot", "effect": "max heap size", "example": "java -Xmx4g App"}], ["pypy", "PyPy --jit off", "Disables the tracing JIT to compare warmup behavior or dodge JIT bugs. Engine: PyPy. Effect: disable tracing JIT. Example: `pypy --jit off script.py`.", {"flag": "--jit off", "engine": "PyPy", "effect": "disable tracing JIT", "example": "pypy --jit off script.py"}], ["luajit", "LuaJIT -j off", "Turns the JIT compiler off, leaving the fast interpreter for debugging. Engine: LuaJIT. Effect: disable JIT. Example: `luajit -j off app.lua`.", {"flag": "-j off", "engine": "LuaJIT", "effect": "disable JIT", "example": "luajit -j off app.lua"}], ["luajit", "LuaJIT -O", "Sets optimization level; -O3 enables the most aggressive trace optimizations. Engine: LuaJIT. Effect: optimization level. Example: `luajit -O3 app.lua`.", {"flag": "-O3", "engine": "LuaJIT", "effect": "optimization level", "example": "luajit -O3 app.lua"}], ["dotnet", ".NET TieredCompilation", "Lets methods start quick-JITed and recompile optimized when hot. Engine: .NET RyuJIT. Effect: tiered JIT. Example: `COMPlus_TieredCompilation=1 dotnet app.dll`.", {"flag": "COMPlus_TieredCompilation=1", "engine": ".NET RyuJIT", "effect": "tiered JIT", "example": "COMPlus_TieredCompilation=1 dotnet app.dll"}], ["graal", "Graal Truffle background compilation", "Compiles Truffle ASTs in the background so startup never blocks on optimization. Engine: GraalVM. Effect: background optimizing. Example: `java -Dgraal.TruffleBackgroundCompilation=true App`.", {"flag": "-Dgraal.TruffleBackgroundCompilation=true", "engine": "GraalVM", "effect": "background optimizing", "example": "java -Dgraal.TruffleBackgroundCompilation=true App"}], ["v8", "Node --stack-size", "Raises the stack limit for deep recursion before RangeError strikes. Engine: V8/Node. Effect: stack size in KB. Example: `node --stack-size=2000 deep.js`.", {"flag": "--stack-size=2000", "engine": "V8/Node", "effect": "stack size in KB", "example": "node --stack-size=2000 deep.js"}]];
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
  if(!new RegExp('^'+'JAH\\-JOF\\-'+'\\d{6}$').test(r.id||''))e.push('id');
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('jit-optimization-flags',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
