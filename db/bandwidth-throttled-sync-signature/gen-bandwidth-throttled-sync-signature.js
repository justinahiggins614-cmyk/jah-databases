(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];} function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var CATS=["cli", "network", "cloud", "p2p", "qos"];
var PREFIX='JAH-BANDWI-S-';
var GENVER='jahdb-bandwidth-throttled-sync-signature-1.0';
var SRC='signature-generated-completion';
var EDITION='signature';
var PROV="Signature-original completion authored for the JAH Databases network; clearly labeled Signature, never presented as public record.";
var FIELDS=["tool", "caps_at", "mechanism", "use"];
var DEMO_TPL="// $TITLE - token bucket throttle demo\nfunction Bucket(rate, cap) { this.rate = rate; this.cap = cap; this.tokens = cap; this.last = Date.now(); }\nBucket.prototype.take = function(n) {\n  var now = Date.now(), el = (now - this.last) / 1000;\n  this.tokens = Math.min(this.cap, this.tokens + el * this.rate); this.last = now;\n  if (this.tokens >= n) { this.tokens -= n; return true; } return false;\n};\nvar b = new Bucket(1000, 1000); // 1000 KB/s\nvar sent = 0, chunks = [400, 400, 400, 400];\nchunks.forEach(function(c) { if (b.take(c)) sent += c; });\nconsole.log(\"Tool: $TOOL | Mechanism: $MECHANISM\");\nconsole.log(\"Requested 1600 KB, bucket allowed: \" + sent + \" KB\");\nconsole.log(\"Throttle enforced -> PASS\");";
function jsEsc(s){return String(s).replace(/\\/g,'\\\\').replace(/"/g,'\\"').replace(/\n/g,'\\n').replace(/\r/g,'\\r').replace(/\t/g,'\\t');}
function fillTpl(tpl,vars){return tpl.replace(/\$([A-Za-z0-9_]+)/g,function(m,k){return Object.prototype.hasOwnProperty.call(vars,k)?jsEsc(vars[k]):m;});}
/* rows: [category, title, description, {fields}] */
var B=[["network", "SigThrottle-Token", "Signature-original: distributed token buckets shared across mesh peers. Caps at global bucket via distributed tokens. Used for: mesh sync.", {"tool": "SigThrottle", "caps_at": "global bucket", "mechanism": "distributed tokens", "use": "mesh sync"}], ["network", "SigThrottle-AI", "Signature-original: ML-predicted congestion throttling before links saturate. Caps at predicted cap via congestion prediction. Used for: smart sync.", {"tool": "SigThrottle-AI", "caps_at": "predicted cap", "mechanism": "congestion prediction", "use": "smart sync"}], ["cloud", "SigThrottle-PerUser", "Signature-original: per-user fair-share buckets on shared sync infrastructure. Caps at per-user rate via fair queueing. Used for: multi-tenant sync.", {"tool": "SigThrottle-User", "caps_at": "per-user rate", "mechanism": "fair queueing", "use": "multi-tenant sync"}], ["cli", "SigThrottle-Schedule", "Signature-original: time-of-day sync schedules with bandwidth calendars. Caps at calendar rates via scheduled pacing. Used for: off-peak sync.", {"tool": "SigThrottle-Sched", "caps_at": "calendar rates", "mechanism": "scheduled pacing", "use": "off-peak sync"}], ["qos", "SigThrottle-Priority", "Signature-original: priority lanes — interactive traffic always beats bulk. Caps at lane weights via weighted fair queue. Used for: mixed traffic.", {"tool": "SigThrottle-Prio", "caps_at": "lane weights", "mechanism": "weighted fair queue", "use": "mixed traffic"}], ["network", "SigThrottle-Adapt", "Signature-original: adaptive throttling probing available bandwidth continuously. Caps at probed cap via bandwidth probing. Used for: variable links.", {"tool": "SigThrottle-Adapt", "caps_at": "probed cap", "mechanism": "bandwidth probing", "use": "variable links"}], ["network", "SigThrottle-Metered", "Signature-original: metered-link mode minimizing bytes on cellular/satellite. Caps at byte budget via budget pacing. Used for: metered links.", {"tool": "SigThrottle-Metered", "caps_at": "byte budget", "mechanism": "budget pacing", "use": "metered links"}], ["network", "SigThrottle-Burst", "Signature-original: burst allowances for interactive spikes within average caps. Caps at avg + burst via token bucket+. Used for: bursty sync.", {"tool": "SigThrottle-Burst", "caps_at": "avg + burst", "mechanism": "token bucket+", "use": "bursty sync"}], ["cloud", "SigThrottle-Group", "Signature-original: group budgets shared across a team’s devices. Caps at group pool via shared bucket. Used for: team sync.", {"tool": "SigThrottle-Group", "caps_at": "group pool", "mechanism": "shared bucket", "use": "team sync"}], ["network", "SigThrottle-Edge", "Signature-original: edge-aware throttling preferring LAN peers over WAN. Caps at LAN-preferring via peer selection. Used for: edge sync.", {"tool": "SigThrottle-Edge", "caps_at": "LAN-preferring", "mechanism": "peer selection", "use": "edge sync"}], ["cli", "SigThrottle-Night", "Signature-original: night-window full-speed sync with daytime politeness. Caps at windowed via time windows. Used for: backup windows.", {"tool": "SigThrottle-Night", "caps_at": "windowed", "mechanism": "time windows", "use": "backup windows"}], ["cloud", "SigThrottle-Cost", "Signature-original: cost-aware throttling staying under egress spend budgets. Caps at spend cap via cost pacing. Used for: cloud egress.", {"tool": "SigThrottle-Cost", "caps_at": "spend cap", "mechanism": "cost pacing", "use": "cloud egress"}], ["qos", "SigThrottle-Fair", "Signature-original: max-min fair sharing across concurrent sync jobs. Caps at fair share via max-min fairness. Used for: job fleets.", {"tool": "SigThrottle-Fair", "caps_at": "fair share", "mechanism": "max-min fairness", "use": "job fleets"}], ["tooling", "SigThrottle-Audit", "Signature-original: throttle decision logs explaining every slowdown. Caps at logged via decision log. Used for: debugging.", {"tool": "SigThrottle-Audit", "caps_at": "logged", "mechanism": "decision log", "use": "debugging"}], ["network", "SigThrottle-One", "Signature-original: the united throttle plane — one policy for every sync path. Caps at unified via unified buckets. Used for: everything.", {"tool": "SigThrottle-One", "caps_at": "unified", "mechanism": "unified buckets", "use": "everything"}]];
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
  if(!new RegExp('^'+'JAH\\-BANDWI\\-S\\-'+'\\d{6}$').test(r.id||''))e.push('id');
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('bandwidth-throttled-sync-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
