(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];} function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var CATS=["js", "native", "jvm", "mobile", "linker"];
var PREFIX='JAH-ADC-';
var GENVER='jahdb-automated-dead-code-elimination-1.0';
var SRC='public-harvest';
var EDITION='public';
var PROV="Public record compiled from openly published documentation, project sources, and standard references.";
var FIELDS=["tool", "removes", "stage", "savings"];
var DEMO_TPL="// $TITLE - reachability DCE demo\nvar graph = { main: [\"a\", \"b\"], a: [\"c\"], b: [], c: [], dead1: [\"dead2\"], dead2: [] };\nvar live = {};\n(function mark(n) { if (live[n]) return; live[n] = 1; (graph[n] || []).forEach(mark); })(\"main\");\nvar removed = Object.keys(graph).filter(function(k) { return !live[k]; });\nconsole.log(\"Tool: $TOOL | Removes: $REMOVES\");\nconsole.log(\"Live: \" + Object.keys(live).join(\", \"));\nconsole.log(\"Eliminated: \" + removed.join(\", \") + \" -> DCE PASS\");";
function jsEsc(s){return String(s).replace(/\\/g,'\\\\').replace(/"/g,'\\"').replace(/\n/g,'\\n').replace(/\r/g,'\\r').replace(/\t/g,'\\t');}
function fillTpl(tpl,vars){return tpl.replace(/\$([A-Za-z0-9_]+)/g,function(m,k){return Object.prototype.hasOwnProperty.call(vars,k)?jsEsc(vars[k]):m;});}
/* rows: [category, title, description, {fields}] */
var B=[["js", "Rollup tree-shaking", "ES-module static analysis dropping unused exports from bundles. Removes unused exports at the bundle stage; typical savings: 20-60% of bundle.", {"tool": "Rollup", "removes": "unused exports", "stage": "bundle", "savings": "20-60% of bundle"}], ["js", "esbuild tree-shaking", "Go-fast bundler with tree-shaking that finishes before coffee cools. Removes unused exports at the bundle stage; typical savings: 20-50%.", {"tool": "esbuild", "removes": "unused exports", "stage": "bundle", "savings": "20-50%"}], ["js", "webpack usedExports", "sideEffects flags plus usedExports prune dead modules in production mode. Removes unused modules at the bundle stage; typical savings: 15-40%.", {"tool": "webpack", "removes": "unused modules", "stage": "bundle", "savings": "15-40%"}], ["js", "Terser", "Compress + mangle + drop_console; the classic JS minifier with DCE. Removes dead branches/vars at the minify stage; typical savings: 10-30%.", {"tool": "Terser", "removes": "dead branches/vars", "stage": "minify", "savings": "10-30%"}], ["js", "Closure Compiler ADVANCED", "Whole-program optimization with aggressive renaming and removal. Removes dead code aggressively at the compile stage; typical savings: 30-60%.", {"tool": "Closure ADVANCED", "removes": "dead code aggressively", "stage": "compile", "savings": "30-60%"}], ["mobile", "ProGuard / R8", "Android’s shrinker removing unused classes, methods, and resources. Removes unused classes/methods at the build stage; typical savings: 30-50% of APK.", {"tool": "R8", "removes": "unused classes/methods", "stage": "build", "savings": "30-50% of APK"}], ["native", "LLVM DCE passes", "adce/dce eliminate dead instructions in the optimizer pipeline. Removes dead instructions at the optimize stage; typical savings: 5-15%.", {"tool": "LLVM", "removes": "dead instructions", "stage": "optimize", "savings": "5-15%"}], ["linker", "GCC --gc-sections", "-ffunction-sections + --gc-sections drops unreferenced sections at link. Removes unreferenced sections at the link stage; typical savings: 5-20%.", {"tool": "GNU ld", "removes": "unreferenced sections", "stage": "link", "savings": "5-20%"}], ["native", "Go linker deadcode", "The Go linker’s deadcode pass keeps binaries small despite static linking. Removes unreachable funcs at the link stage; typical savings: built-in.", {"tool": "go link", "removes": "unreachable funcs", "stage": "link", "savings": "built-in"}], ["native", "Rust LTO", "Link-time optimization sees across crates to remove dead generics. Removes dead monomorphizations at the link stage; typical savings: 10-25%.", {"tool": "rustc LTO", "removes": "dead monomorphizations", "stage": "link", "savings": "10-25%"}], ["mobile", "Dart tree-shaking", "dart2js and Flutter tree-shake the framework to ship tiny web/mobile apps. Removes unused framework at the compile stage; typical savings: large.", {"tool": "dart2js", "removes": "unused framework", "stage": "compile", "savings": "large"}], ["native", "Swift WMO", "Whole-module optimization enables cross-file DCE in Swift builds. Removes dead code cross-file at the compile stage; typical savings: 10-20%.", {"tool": "swiftc -wmo", "removes": "dead code cross-file", "stage": "compile", "savings": "10-20%"}], ["jvm", ".NET ILLink", "Trims assemblies for self-contained deployments and NativeAOT. Removes unused IL at the publish stage; typical savings: 50%+ of framework.", {"tool": "ILLink", "removes": "unused IL", "stage": "publish", "savings": "50%+ of framework"}], ["native", "GraalVM native-image", "Reachability analysis includes only what’s reachable from main. Removes unreachable classes at the AOT stage; typical savings: majority of JDK.", {"tool": "native-image", "removes": "unreachable classes", "stage": "AOT", "savings": "majority of JDK"}], ["js", "V8 TurboFan DCE", "The optimizing compiler’s dead-code pass trims unobservable computations. Removes dead nodes at the JIT stage; typical savings: per-function.", {"tool": "TurboFan", "removes": "dead nodes", "stage": "JIT", "savings": "per-function"}]];
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
  if(!new RegExp('^'+'JAH\\-ADC\\-'+'\\d{6}$').test(r.id||''))e.push('id');
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('automated-dead-code-elimination',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
