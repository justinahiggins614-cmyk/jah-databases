(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];} function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var CATS=["memory", "handles", "kernel", "language", "tooling"];
var PREFIX='JAH-RESOUR-S-';
var GENVER='jahdb-resource-leak-detection-signature-1.0';
var SRC='signature-generated-completion';
var EDITION='signature';
var PROV="Signature-original completion authored for the JAH Databases network; clearly labeled Signature, never presented as public record.";
var FIELDS=["tool", "finds", "how", "platform"];
var DEMO_TPL="// $TITLE - leak detection demo\nvar seen = {};\nfunction alloc(id, bytes) { seen[id] = (seen[id] || 0) + bytes; }\nfunction free(id) { delete seen[id]; }\nalloc(\"buf-a\", 1024); alloc(\"buf-b\", 2048); alloc(\"buf-c\", 512);\nfree(\"buf-b\");\nvar leaked = Object.keys(seen);\nconsole.log(\"Tool model: $TOOL\");\nconsole.log(\"Live allocations: \" + Object.keys(seen).length);\nconsole.log(leaked.length ? \"LEAK: \" + leaked.join(\", \") + \" never freed\" : \"CLEAN: no leaks\");";
function jsEsc(s){return String(s).replace(/\\/g,'\\\\').replace(/"/g,'\\"').replace(/\n/g,'\\n').replace(/\r/g,'\\r').replace(/\t/g,'\\t');}
function fillTpl(tpl,vars){return tpl.replace(/\$([A-Za-z0-9_]+)/g,function(m,k){return Object.prototype.hasOwnProperty.call(vars,k)?jsEsc(vars[k]):m;});}
/* rows: [category, title, description, {fields}] */
var B=[["memory", "SigTrace-Alloc", "Signature-original: allocation tracing with per-type budgets that alarm before the OOM killer acts. It finds heap leaks by budgeted allocation tracing. Platform: Signature runtime.", {"tool": "sigtrace", "finds": "heap leaks", "how": "budgeted allocation tracing", "platform": "Signature runtime"}], ["memory", "SigDiff-Heap", "Signature-original: heap snapshot diffing built into the runtime, no external profiler needed. It finds retained objects by snapshot differencing. Platform: Signature runtime.", {"tool": "sigdiff-heap", "finds": "retained objects", "how": "snapshot differencing", "platform": "Signature runtime"}], ["handles", "SigWatch-FD", "Signature-original: descriptor watchers auto-closing handles idle past a policy threshold. It finds fd leaks by idle-handle reclamation. Platform: Signature runtime.", {"tool": "sigwatch-fd", "finds": "fd leaks", "how": "idle-handle reclamation", "platform": "Signature runtime"}], ["language", "SigGuard-GC", "Signature-original: GC pressure guards shedding caches when heap growth exceeds slope limits. It finds GC pressure by growth-slope monitoring. Platform: Signature runtime.", {"tool": "sigguard-gc", "finds": "GC pressure", "how": "growth-slope monitoring", "platform": "Signature runtime"}], ["kernel", "SigProbe-Kernel", "Signature-original: kernel allocation probes with per-module leak attribution. It finds kernel leaks by module-attributed tracing. Platform: SigCell hosts.", {"tool": "sigprobe", "finds": "kernel leaks", "how": "module-attributed tracing", "platform": "SigCell hosts"}], ["language", "SigScan-Refs", "Signature-original: reference-cycle scanning for runtimes without cycle collectors. It finds reference cycles by cycle detection passes. Platform: Signature runtime.", {"tool": "sigscan", "finds": "reference cycles", "how": "cycle detection passes", "platform": "Signature runtime"}], ["handles", "SigMeter-Thread", "Signature-original: thread-leak metering counting spawned vs joined threads per service. It finds thread leaks by spawn/join accounting. Platform: Signature runtime.", {"tool": "sigmeter", "finds": "thread leaks", "how": "spawn/join accounting", "platform": "Signature runtime"}], ["handles", "SigAudit-Socket", "Signature-original: socket auditing flagging connections open past their TTL. It finds socket leaks by TTL-based auditing. Platform: Signature runtime.", {"tool": "sigaudit", "finds": "socket leaks", "how": "TTL-based auditing", "platform": "Signature runtime"}], ["memory", "SigMap-GPU", "Signature-original: GPU memory mapping tracking allocations across CUDA-like APIs. It finds GPU leaks by API-interposition tracking. Platform: SigGPU hosts.", {"tool": "sigmap-gpu", "finds": "GPU leaks", "how": "API-interposition tracking", "platform": "SigGPU hosts"}], ["memory", "SigCheck-Mmap", "Signature-original: mmap/munmap balance checking for native extensions. It finds mapping leaks by map/unmap pairing. Platform: Signature runtime.", {"tool": "sigcheck-mmap", "finds": "mapping leaks", "how": "map/unmap pairing", "platform": "Signature runtime"}], ["tooling", "SigProfile-Cont", "Signature-original: continuous leak profiling with weekly regression reports per service. It finds regressions by continuous sampling. Platform: Signature fleet.", {"tool": "sigprofile", "finds": "regressions", "how": "continuous sampling", "platform": "Signature fleet"}], ["handles", "SigKill-Zombie", "Signature-original: zombie-process reaping with parent notification chains. It finds zombie processes by reaper daemons. Platform: SigCell hosts.", {"tool": "sigkill-z", "finds": "zombie processes", "how": "reaper daemons", "platform": "SigCell hosts"}], ["language", "SigTrace-Async", "Signature-original: async-resource tracing matching timers and promises to their creators. It finds async leaks by async-context tracking. Platform: Signature runtime.", {"tool": "sigtrace-async", "finds": "async leaks", "how": "async-context tracking", "platform": "Signature runtime"}], ["memory", "SigBudget-Quota", "Signature-original: quota budgets that fail fast with the leaking call stack attached. It finds quota breaches by budget enforcement. Platform: Signature runtime.", {"tool": "sigbudget", "finds": "quota breaches", "how": "budget enforcement", "platform": "Signature runtime"}], ["tooling", "SigOne-Leak", "Signature-original: the united leak plane correlating heap, fd, and handle data per service. It finds all leak classes by correlated telemetry. Platform: Signature fleet.", {"tool": "sigone-leak", "finds": "all leak classes", "how": "correlated telemetry", "platform": "Signature fleet"}]];
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
  if(!new RegExp('^'+'JAH\\-RESOUR\\-S\\-'+'\\d{6}$').test(r.id||''))e.push('id');
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('resource-leak-detection-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
