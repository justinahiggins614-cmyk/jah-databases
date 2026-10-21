(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];} function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var CATS=["memory", "handles", "kernel", "language", "tooling"];
var PREFIX='JAH-RESOUR-';
var GENVER='jahdb-resource-leak-detection-1.0';
var SRC='public-harvest';
var EDITION='public';
var PROV="Public record compiled from openly published documentation, project sources, and standard references.";
var FIELDS=["tool", "finds", "how", "platform"];
var DEMO_TPL="// $TITLE - leak detection demo\nvar seen = {};\nfunction alloc(id, bytes) { seen[id] = (seen[id] || 0) + bytes; }\nfunction free(id) { delete seen[id]; }\nalloc(\"buf-a\", 1024); alloc(\"buf-b\", 2048); alloc(\"buf-c\", 512);\nfree(\"buf-b\");\nvar leaked = Object.keys(seen);\nconsole.log(\"Tool model: $TOOL\");\nconsole.log(\"Live allocations: \" + Object.keys(seen).length);\nconsole.log(leaked.length ? \"LEAK: \" + leaked.join(\", \") + \" never freed\" : \"CLEAN: no leaks\");";
function jsEsc(s){return String(s).replace(/\\/g,'\\\\').replace(/"/g,'\\"').replace(/\n/g,'\\n').replace(/\r/g,'\\r').replace(/\t/g,'\\t');}
function fillTpl(tpl,vars){return tpl.replace(/\$([A-Za-z0-9_]+)/g,function(m,k){return Object.prototype.hasOwnProperty.call(vars,k)?jsEsc(vars[k]):m;});}
/* rows: [category, title, description, {fields}] */
var B=[["memory", "Valgrind memcheck", "The classic binary-instrumentation leak checker; reports definitely/indirectly/possibly lost blocks at exit. It finds heap leaks by binary instrumentation of malloc/free. Platform: Linux.", {"tool": "Valgrind memcheck", "finds": "heap leaks", "how": "binary instrumentation of malloc/free", "platform": "Linux"}], ["memory", "LeakSanitizer", "Compile with -fsanitize=leak for near-zero-overhead leak reports at process exit. It finds heap leaks by compiler-inserted allocation tracking. Platform: Linux, macOS.", {"tool": "LeakSanitizer", "finds": "heap leaks", "how": "compiler-inserted allocation tracking", "platform": "Linux, macOS"}], ["memory", "AddressSanitizer", "Catches use-after-free and overflows at runtime, which are leaks’ close cousins. It finds memory errors by shadow-memory instrumentation. Platform: Linux, macOS, Windows.", {"tool": "AddressSanitizer", "finds": "memory errors", "how": "shadow-memory instrumentation", "platform": "Linux, macOS, Windows"}], ["language", "Go pprof heap", "net/http/pprof exposes heap profiles; go tool pprof diffs two snapshots to find growth. It finds Go heap growth by sampling heap profiler. Platform: any Go runtime.", {"tool": "go pprof", "finds": "Go heap growth", "how": "sampling heap profiler", "platform": "any Go runtime"}], ["memory", "jemalloc profiling", "MALLOC_CONF=prof:true dumps allocation sites; jeprof attributes retained bytes to call stacks. It finds native heap retention by sampling allocator profiler. Platform: Linux, macOS, BSD.", {"tool": "jemalloc", "finds": "native heap retention", "how": "sampling allocator profiler", "platform": "Linux, macOS, BSD"}], ["language", "Chrome heap snapshots", "DevTools heap snapshots with the comparison view reveal detached DOM trees and growing closures. It finds JS heap leaks by heap snapshot diffing. Platform: Chrome/Edge.", {"tool": "Chrome DevTools", "finds": "JS heap leaks", "how": "heap snapshot diffing", "platform": "Chrome/Edge"}], ["language", "VisualVM sampler", "The free JDK-bundled profiler sampling heap and threads to spot runaway object retention. It finds Java heap leaks by heap dump + sampler. Platform: any JDK.", {"tool": "VisualVM", "finds": "Java heap leaks", "how": "heap dump + sampler", "platform": "any JDK"}], ["handles", "lsof for fd leaks", "lsof -p lists a process’s open files; a count climbing forever means descriptor leaks. It finds fd leaks by inspecting open file tables. Platform: Linux, macOS, BSD.", {"tool": "lsof", "finds": "fd leaks", "how": "inspecting open file tables", "platform": "Linux, macOS, BSD"}], ["handles", "/proc fd inspection", "Counting entries in /proc/<pid>/fd over time is the zero-tool way to catch descriptor leaks. It finds fd leaks by kernel-exposed fd counts. Platform: Linux.", {"tool": "/proc filesystem", "finds": "fd leaks", "how": "kernel-exposed fd counts", "platform": "Linux"}], ["kernel", "eBPF memleak", "bpftrace’s memleak.bt traces kmalloc/kfree in the kernel to find unbalanced allocations. It finds kernel leaks by eBPF tracepoints on alloc/free. Platform: Linux 4.9+.", {"tool": "bpftrace memleak", "finds": "kernel leaks", "how": "eBPF tracepoints on alloc/free", "platform": "Linux 4.9+"}], ["language", "tracemalloc", "Python’s tracemalloc attributes every allocation to a traceback; compare snapshots to find growth. It finds Python leaks by allocation traceback tracking. Platform: any Python 3.4+.", {"tool": "tracemalloc", "finds": "Python leaks", "how": "allocation traceback tracking", "platform": "any Python 3.4+"}], ["language", "dotnet counters", "dotnet-counters watches GC heap size and gen collections live without a full profiler. It finds .NET heap growth by EventPipe runtime counters. Platform: .NET Core.", {"tool": "dotnet-counters", "finds": ".NET heap growth", "how": "EventPipe runtime counters", "platform": ".NET Core"}], ["handles", "Handle count on Windows", "Task Manager’s Handles column or handle.exe exposes GDI/USER handle leaks in Win32 apps. It finds Windows handle leaks by handle table enumeration. Platform: Windows.", {"tool": "handle.exe", "finds": "Windows handle leaks", "how": "handle table enumeration", "platform": "Windows"}], ["memory", "massif heap profiler", "Valgrind’s massif draws heap usage over time so spikes map to program phases. It finds heap usage over time by allocation-time profiling. Platform: Linux.", {"tool": "massif", "finds": "heap usage over time", "how": "allocation-time profiling", "platform": "Linux"}], ["memory", "Xcode Leaks instrument", "Instruments’ Leaks template finds malloc blocks with no reachable references in iOS/macOS apps. It finds ObjC/Swift leaks by reference-graph analysis. Platform: macOS, iOS.", {"tool": "Xcode Instruments", "finds": "ObjC/Swift leaks", "how": "reference-graph analysis", "platform": "macOS, iOS"}]];
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
  if(!new RegExp('^'+'JAH\\-RESOUR\\-'+'\\d{6}$').test(r.id||''))e.push('id');
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('resource-leak-detection',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
