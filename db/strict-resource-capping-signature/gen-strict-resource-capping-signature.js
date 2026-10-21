(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];} function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var CATS=["cpu", "memory", "io", "process", "runtime"];
var PREFIX='JAH-STRICT2-S-';
var GENVER='jahdb-strict-resource-capping-signature-1.0';
var SRC='signature-generated-completion';
var EDITION='signature';
var PROV="Signature-original completion authored for the JAH Databases network; clearly labeled Signature, never presented as public record.";
var FIELDS=["mechanism", "limit", "unit", "usage", "limitval"];
var DEMO_TPL="// $TITLE - resource cap enforcement demo\nvar CAP = { mechanism: \"$MECHANISM\", limit: \"$LIMIT\", unit: \"$UNIT\" };\nvar usage = $USAGE, limitVal = $LIMITVAL;\nconsole.log(\"Mechanism: \" + CAP.mechanism);\nconsole.log(\"Cap: \" + limitVal + \" \" + CAP.unit + \" (\" + CAP.limit + \")\");\nconsole.log(\"Usage: \" + usage + \" \" + CAP.unit);\nconsole.log(usage > limitVal ? \"RESULT: OVER LIMIT - policy engaged\" : \"RESULT: within budget - OK\");";
function jsEsc(s){return String(s).replace(/\\/g,'\\\\').replace(/"/g,'\\"').replace(/\n/g,'\\n').replace(/\r/g,'\\r').replace(/\t/g,'\\t');}
function fillTpl(tpl,vars){return tpl.replace(/\$([A-Za-z0-9_]+)/g,function(m,k){return Object.prototype.hasOwnProperty.call(vars,k)?jsEsc(vars[k]):m;});}
/* rows: [category, title, description, {fields}] */
var B=[["cpu", "SigCap-CPU", "Signature-original: per-function CPU budgets with graceful degrade-to-queue instead of kill. It enforces 200 ms/run (ms); the demo runs a usage of 150 against the cap.", {"mechanism": "SigCap-CPU", "limit": "200 ms/run", "unit": "ms", "usage": "150", "limitval": "200"}], ["memory", "SigCap-Mem", "Signature-original: memory caps with pre-OOM callbacks letting code shed caches first. It enforces 256 MB (MB); the demo runs a usage of 180 against the cap.", {"mechanism": "SigCap-Mem", "limit": "256 MB", "unit": "MB", "usage": "180", "limitval": "256"}], ["runtime", "SigCap-Fuel", "Signature-original: instruction fuel with per-module pricing so untrusted plug-ins cost more. It enforces 500K fuel (fuel); the demo runs a usage of 300000 against the cap.", {"mechanism": "SigCap-Fuel", "limit": "500K fuel", "unit": "fuel", "usage": "300000", "limitval": "500000"}], ["io", "SigCap-Net", "Signature-original: egress byte budgets per cell with mesh-internal traffic exempt. It enforces 100 MB/day (MB); the demo runs a usage of 60 against the cap.", {"mechanism": "SigCap-Net", "limit": "100 MB/day", "unit": "MB", "usage": "60", "limitval": "100"}], ["process", "SigCap-FD", "Signature-original: file-descriptor caps with least-recently-used auto-close of idle handles. It enforces 512 fds (fds); the demo runs a usage of 300 against the cap.", {"mechanism": "SigCap-FD", "limit": "512 fds", "unit": "fds", "usage": "300", "limitval": "512"}], ["process", "SigCap-Fork", "Signature-original: process-spawn budgets stopping fork bombs while allowing workers. It enforces 32 children (children); the demo runs a usage of 12 against the cap.", {"mechanism": "SigCap-Fork", "limit": "32 children", "unit": "children", "usage": "12", "limitval": "32"}], ["cpu", "SigCap-Time", "Signature-original: wall-clock budgets with checkpoint-before-kill so work is never lost. It enforces 300 s (seconds); the demo runs a usage of 120 against the cap.", {"mechanism": "SigCap-Time", "limit": "300 s", "unit": "seconds", "usage": "120", "limitval": "300"}], ["cpu", "SigCap-GPU", "Signature-original: GPU millisecond budgets shared fairly across tenants on one card. It enforces 1000 ms/s (ms); the demo runs a usage of 600 against the cap.", {"mechanism": "SigCap-GPU", "limit": "1000 ms/s", "unit": "ms", "usage": "600", "limitval": "1000"}], ["io", "SigCap-Disk", "Signature-original: disk-write quotas with copy-on-write overflow into a spill area. It enforces 1 GB (MB); the demo runs a usage of 700 against the cap.", {"mechanism": "SigCap-Disk", "limit": "1 GB", "unit": "MB", "usage": "700", "limitval": "1024"}], ["process", "SigCap-Syscall", "Signature-original: syscall budgets per category (file, net, process) with learning mode. It enforces 20 net calls/s (calls/s); the demo runs a usage of 8 against the cap.", {"mechanism": "SigCap-Syscall", "limit": "20 net calls/s", "unit": "calls/s", "usage": "8", "limitval": "20"}], ["runtime", "SigCap-Queue", "Signature-original: queue-depth caps with backpressure signals to producers. It enforces 10000 msgs (messages); the demo runs a usage of 4000 against the cap.", {"mechanism": "SigCap-Queue", "limit": "10000 msgs", "unit": "messages", "usage": "4000", "limitval": "10000"}], ["process", "SigCap-Thread", "Signature-original: thread caps with work-stealing pools that respect the ceiling. It enforces 64 threads (threads); the demo runs a usage of 40 against the cap.", {"mechanism": "SigCap-Thread", "limit": "64 threads", "unit": "threads", "usage": "40", "limitval": "64"}], ["cpu", "SigCap-Energy", "Signature-original: joule budgets for battery devices, throttling background work first. It enforces 500 J/hr (joules); the demo runs a usage of 200 against the cap.", {"mechanism": "SigCap-Energy", "limit": "500 J/hr", "unit": "joules", "usage": "200", "limitval": "500"}], ["memory", "SigCap-Alloc", "Signature-original: allocation-rate caps smoothing spikes that fragment heaps. It enforces 50 MB/s (MB/s); the demo runs a usage of 20 against the cap.", {"mechanism": "SigCap-Alloc", "limit": "50 MB/s", "unit": "MB/s", "usage": "20", "limitval": "50"}], ["runtime", "SigCap-One", "Signature-original: the united cap policy bundling CPU, memory, I/O, and fuel in one manifest. It enforces composite (policy); the demo runs a usage of 0 against the cap.", {"mechanism": "SigCap-One", "limit": "composite", "unit": "policy", "usage": "0", "limitval": "1"}]];
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
  if(!new RegExp('^'+'JAH\\-STRICT2\\-S\\-'+'\\d{6}$').test(r.id||''))e.push('id');
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('strict-resource-capping-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
