(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];} function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var CATS=["tracing", "binary", "kernel", "debug", "profiling"];
var PREFIX='JAH-DYNAMI-';
var GENVER='jahdb-dynamic-instrumentation-1.0';
var SRC='public-harvest';
var EDITION='public';
var PROV="Public record compiled from openly published documentation, project sources, and standard references.";
var FIELDS=["tool", "observes", "method", "platform"];
var DEMO_TPL="// $TITLE - probe demo (function interposition model)\nvar calls = [];\nfunction probe(name, fn) {\n  return function() {\n    var t0 = Date.now();\n    var r = fn.apply(null, arguments);\n    calls.push({ name: name, ms: Date.now() - t0 });\n    return r;\n  };\n}\nvar work = probe(\"work\", function(n) { var s = 0; for (var i = 0; i < n; i++) s += i; return s; });\nconsole.log(\"Tool model: $TOOL | Observes: $OBSERVES\");\nconsole.log(\"work(100000) = \" + work(100000));\nconsole.log(\"Probe record: \" + JSON.stringify(calls[0]));";
function jsEsc(s){return String(s).replace(/\\/g,'\\\\').replace(/"/g,'\\"').replace(/\n/g,'\\n').replace(/\r/g,'\\r').replace(/\t/g,'\\t');}
function fillTpl(tpl,vars){return tpl.replace(/\$([A-Za-z0-9_]+)/g,function(m,k){return Object.prototype.hasOwnProperty.call(vars,k)?jsEsc(vars[k]):m;});}
/* rows: [category, title, description, {fields}] */
var B=[["tracing", "strace", "Traces every syscall a process makes; -f follows forks and -c summarizes counts. It observes syscalls via ptrace syscall interception. Platform: Linux.", {"tool": "strace", "observes": "syscalls", "method": "ptrace syscall interception", "platform": "Linux"}], ["tracing", "ltrace", "Like strace but for library calls, showing arguments to libc and shared-library functions. It observes library calls via breakpoint PLT interception. Platform: Linux.", {"tool": "ltrace", "observes": "library calls", "method": "breakpoint PLT interception", "platform": "Linux"}], ["kernel", "eBPF / bpftrace", "Run sandboxed programs in the kernel to trace syscalls, network, and disks with near-zero overhead. It observes kernel + user events via eBPF programs on tracepoints. Platform: Linux 4.9+.", {"tool": "bpftrace", "observes": "kernel + user events", "method": "eBPF programs on tracepoints", "platform": "Linux 4.9+"}], ["binary", "Frida", "Inject JavaScript into running processes to hook functions on desktop and mobile without source. It observes function calls via dynamic code injection. Platform: Linux/macOS/Windows/Android/iOS.", {"tool": "Frida", "observes": "function calls", "method": "dynamic code injection", "platform": "Linux/macOS/Windows/Android/iOS"}], ["binary", "DynamoRIO", "A runtime code-manipulation system powering tools like Dr. Memory with basic-block granularity. It observes instruction execution via dynamic binary translation. Platform: Linux, Windows.", {"tool": "DynamoRIO", "observes": "instruction execution", "method": "dynamic binary translation", "platform": "Linux, Windows"}], ["binary", "Intel Pin", "Pin instruments binaries at instruction level; the classic platform for custom analysis tools. It observes instructions via JIT-based instrumentation. Platform: Linux, Windows, macOS.", {"tool": "Intel Pin", "observes": "instructions", "method": "JIT-based instrumentation", "platform": "Linux, Windows, macOS"}], ["kernel", "DTrace", "Sun’s dynamic tracing with the D language; probes fire on function entry, syscalls, and more. It observes kernel + app probes via in-kernel D-script probes. Platform: Solaris, macOS, BSD.", {"tool": "DTrace", "observes": "kernel + app probes", "method": "in-kernel D-script probes", "platform": "Solaris, macOS, BSD"}], ["kernel", "SystemTap", "Red Hat’s kernel instrumentation compiling scripts to kernel modules for deep tracing. It observes kernel events via kprobes/uprobes scripts. Platform: Linux.", {"tool": "SystemTap", "observes": "kernel events", "method": "kprobes/uprobes scripts", "platform": "Linux"}], ["debug", "gdb breakpoints", "The debugger’s breakpoints, watchpoints, and catchpoints are instrumentation for humans. It observes program state via ptrace breakpoints. Platform: Linux, macOS, BSD.", {"tool": "GDB", "observes": "program state", "method": "ptrace breakpoints", "platform": "Linux, macOS, BSD"}], ["debug", "rr reversible debugging", "rr records execution deterministically so you can replay backwards — time-travel instrumentation. It observes full execution via deterministic record/replay. Platform: Linux x86_64.", {"tool": "rr", "observes": "full execution", "method": "deterministic record/replay", "platform": "Linux x86_64"}], ["profiling", "perf", "Linux perf samples CPU, cache, and tracepoints with hardware counters at negligible overhead. It observes CPU + hardware events via PMU sampling. Platform: Linux.", {"tool": "perf", "observes": "CPU + hardware events", "method": "PMU sampling", "platform": "Linux"}], ["profiling", "Intel VTune", "VTune’s hotspots and microarchitecture analysis find pipeline stalls in optimized code. It observes microarchitecture via PMU + instrumentation. Platform: Linux, Windows.", {"tool": "VTune", "observes": "microarchitecture", "method": "PMU + instrumentation", "platform": "Linux, Windows"}], ["binary", "Valgrind", "Memcheck, Helgrind, and cachegrind all ride Valgrind’s IR-based binary instrumentation. It observes memory + threads via IR translation. Platform: Linux.", {"tool": "Valgrind", "observes": "memory + threads", "method": "IR translation", "platform": "Linux"}], ["debug", "ptrace", "The raw Linux API behind strace and gdb: PTRACE_SYSCALL, PEEKDATA, and friends. It observes process internals via kernel process-tracing API. Platform: Linux, BSD.", {"tool": "ptrace", "observes": "process internals", "method": "kernel process-tracing API", "platform": "Linux, BSD"}], ["kernel", "uprobe", "User-space static/dynamic probes letting eBPF attach to any userspace function entry. It observes userspace functions via eBPF uprobe attachment. Platform: Linux.", {"tool": "uprobe", "observes": "userspace functions", "method": "eBPF uprobe attachment", "platform": "Linux"}]];
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
  if(!new RegExp('^'+'JAH\\-DYNAMI\\-'+'\\d{6}$').test(r.id||''))e.push('id');
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('dynamic-instrumentation',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
