(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];} function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var CATS=["cpu", "memory", "io", "process", "runtime"];
var PREFIX='JAH-STRICT2-';
var GENVER='jahdb-strict-resource-capping-1.0';
var SRC='public-harvest';
var EDITION='public';
var PROV="Public record compiled from openly published documentation, project sources, and standard references.";
var FIELDS=["mechanism", "limit", "unit", "usage", "limitval"];
var DEMO_TPL="// $TITLE - resource cap enforcement demo\nvar CAP = { mechanism: \"$MECHANISM\", limit: \"$LIMIT\", unit: \"$UNIT\" };\nvar usage = $USAGE, limitVal = $LIMITVAL;\nconsole.log(\"Mechanism: \" + CAP.mechanism);\nconsole.log(\"Cap: \" + limitVal + \" \" + CAP.unit + \" (\" + CAP.limit + \")\");\nconsole.log(\"Usage: \" + usage + \" \" + CAP.unit);\nconsole.log(usage > limitVal ? \"RESULT: OVER LIMIT - policy engaged\" : \"RESULT: within budget - OK\");";
function jsEsc(s){return String(s).replace(/\\/g,'\\\\').replace(/"/g,'\\"').replace(/\n/g,'\\n').replace(/\r/g,'\\r').replace(/\t/g,'\\t');}
function fillTpl(tpl,vars){return tpl.replace(/\$([A-Za-z0-9_]+)/g,function(m,k){return Object.prototype.hasOwnProperty.call(vars,k)?jsEsc(vars[k]):m;});}
/* rows: [category, title, description, {fields}] */
var B=[["cpu", "cgroups v2 cpu.max", "The unified hierarchy’s cpu.max takes quota and period in microseconds, the standard way to pin containers. It enforces 100000 100000 (1 CPU) (quota/period); the demo runs a usage of 85000 against the cap.", {"mechanism": "cgroups v2 cpu.max", "limit": "100000 100000 (1 CPU)", "unit": "quota/period", "usage": "85000", "limitval": "100000"}], ["memory", "systemd MemoryMax", "systemd translates MemoryMax into the cgroup memory.max knob per service with clean OOM accounting. It enforces 512M (MB); the demo runs a usage of 420 against the cap.", {"mechanism": "systemd MemoryMax", "limit": "512M", "unit": "MB", "usage": "420", "limitval": "512"}], ["memory", "Docker --memory", "Docker’s --memory flag sets the container cgroup limit; --memory-swap extends it to swap. It enforces 1g (MB); the demo runs a usage of 900 against the cap.", {"mechanism": "docker --memory", "limit": "1g", "unit": "MB", "usage": "900", "limitval": "1024"}], ["cpu", "Kubernetes limits", "Pod resource limits are enforced by the kubelet via cgroups; exceeding memory triggers OOMKill. It enforces 256Mi (MiB); the demo runs a usage of 200 against the cap.", {"mechanism": "kubernetes limits.memory", "limit": "256Mi", "unit": "MiB", "usage": "200", "limitval": "256"}], ["memory", "ulimit -v virtual memory", "The classic per-process address-space cap; exceeding it makes malloc fail instead of growing. It enforces 1048576 KB (KB); the demo runs a usage of 800000 against the cap.", {"mechanism": "ulimit -v", "limit": "1048576 KB", "unit": "KB", "usage": "800000", "limitval": "1048576"}], ["cpu", "setrlimit RLIMIT_CPU", "RLIMIT_CPU sends SIGXCPU then SIGKILL when a process burns its CPU budget — the original time cap. It enforces 60 seconds (seconds); the demo runs a usage of 45 against the cap.", {"mechanism": "setrlimit RLIMIT_CPU", "limit": "60 seconds", "unit": "seconds", "usage": "45", "limitval": "60"}], ["process", "seccomp-bpf syscall filter", "seccomp-bpf caps which syscalls a process may invoke, shrinking the kernel attack surface. It enforces 44 syscalls allowed (syscalls); the demo runs a usage of 30 against the cap.", {"mechanism": "seccomp-bpf", "limit": "44 syscalls allowed", "unit": "syscalls", "usage": "30", "limitval": "44"}], ["runtime", "wasmtime fuel metering", "Fuel counts down per executed instruction; when it hits zero the WASM instance traps deterministically. It enforces 1M fuel units (fuel); the demo runs a usage of 750000 against the cap.", {"mechanism": "wasmtime fuel", "limit": "1M fuel units", "unit": "fuel", "usage": "750000", "limitval": "1000000"}], ["memory", "V8 --max-old-space-size", "Caps the old-generation heap in megabytes; Node’s default is ~2 GB on 64-bit. It enforces 2048 MB (MB); the demo runs a usage of 1500 against the cap.", {"mechanism": "v8 --max-old-space-size", "limit": "2048 MB", "unit": "MB", "usage": "1500", "limitval": "2048"}], ["memory", "JVM -Xmx", "-Xmx sets the maximum Java heap; allocation beyond it throws OutOfMemoryError instead of paging. It enforces 4g (MB); the demo runs a usage of 3000 against the cap.", {"mechanism": "jvm -Xmx", "limit": "4g", "unit": "MB", "usage": "3000", "limitval": "4096"}], ["process", "Erlang +P max processes", "+P caps the BEAM process count so a fork-bomb-style bug cannot exhaust the VM. It enforces 1M processes (processes); the demo runs a usage of 120000 against the cap.", {"mechanism": "erlang +P", "limit": "1M processes", "unit": "processes", "usage": "120000", "limitval": "1000000"}], ["cpu", "Cloudflare Workers CPU time", "Workers get ~10-50 ms CPU per request on the free tier; overruns throw, they never queue. It enforces 50 ms (ms); the demo runs a usage of 32 against the cap.", {"mechanism": "workers cpu time", "limit": "50 ms", "unit": "ms", "usage": "32", "limitval": "50"}], ["process", "prlimit at runtime", "prlimit adjusts another running process’s rlimits without restart — caps applied live. It enforces nofile 1024 (fds); the demo runs a usage of 800 against the cap.", {"mechanism": "prlimit", "limit": "nofile 1024", "unit": "fds", "usage": "800", "limitval": "1024"}], ["cpu", "systemd CPUQuota", "CPUQuota=50% pins a service to half a core across the whole machine, enforced by the scheduler. It enforces 50% (percent); the demo runs a usage of 40 against the cap.", {"mechanism": "systemd CPUQuota", "limit": "50%", "unit": "percent", "usage": "40", "limitval": "50"}], ["io", "cgroup io.max", "io.max throttles block-device bandwidth per cgroup with rbps/wbps/riops/wiops keys. It enforces 10 MB/s (MB/s); the demo runs a usage of 7 against the cap.", {"mechanism": "cgroup io.max", "limit": "10 MB/s", "unit": "MB/s", "usage": "7", "limitval": "10"}]];
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
  if(!new RegExp('^'+'JAH\\-STRICT2\\-'+'\\d{6}$').test(r.id||''))e.push('id');
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('strict-resource-capping',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
