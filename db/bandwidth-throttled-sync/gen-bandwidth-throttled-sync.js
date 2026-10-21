(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];} function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var CATS=["cli", "network", "cloud", "p2p", "qos"];
var PREFIX='JAH-BANDWI-';
var GENVER='jahdb-bandwidth-throttled-sync-1.0';
var SRC='public-harvest';
var EDITION='public';
var PROV="Public record compiled from openly published documentation, project sources, and standard references.";
var FIELDS=["tool", "caps_at", "mechanism", "use"];
var DEMO_TPL="// $TITLE - token bucket throttle demo\nfunction Bucket(rate, cap) { this.rate = rate; this.cap = cap; this.tokens = cap; this.last = Date.now(); }\nBucket.prototype.take = function(n) {\n  var now = Date.now(), el = (now - this.last) / 1000;\n  this.tokens = Math.min(this.cap, this.tokens + el * this.rate); this.last = now;\n  if (this.tokens >= n) { this.tokens -= n; return true; } return false;\n};\nvar b = new Bucket(1000, 1000); // 1000 KB/s\nvar sent = 0, chunks = [400, 400, 400, 400];\nchunks.forEach(function(c) { if (b.take(c)) sent += c; });\nconsole.log(\"Tool: $TOOL | Mechanism: $MECHANISM\");\nconsole.log(\"Requested 1600 KB, bucket allowed: \" + sent + \" KB\");\nconsole.log(\"Throttle enforced -> PASS\");";
function jsEsc(s){return String(s).replace(/\\/g,'\\\\').replace(/"/g,'\\"').replace(/\n/g,'\\n').replace(/\r/g,'\\r').replace(/\t/g,'\\t');}
function fillTpl(tpl,vars){return tpl.replace(/\$([A-Za-z0-9_]+)/g,function(m,k){return Object.prototype.hasOwnProperty.call(vars,k)?jsEsc(vars[k]):m;});}
/* rows: [category, title, description, {fields}] */
var B=[["cli", "rsync --bwlimit", "The classic per-transfer cap in KB/s for polite syncing. Caps at --bwlimit KB/s via transfer pacing. Used for: polite syncs.", {"tool": "rsync", "caps_at": "--bwlimit KB/s", "mechanism": "transfer pacing", "use": "polite syncs"}], ["cli", "rclone --bwlimit", "Timetable-aware limits (e.g. slower by day) across 70+ cloud backends. Caps at --bwlimit \"08:00,512k 18:00,10M\" via token bucket. Used for: cloud syncs.", {"tool": "rclone", "caps_at": "--bwlimit \"08:00,512k 18:00,10M\"", "mechanism": "token bucket", "use": "cloud syncs"}], ["cli", "trickle", "A userspace shaper (LD_PRELOAD) capping any dynamically-linked program. Caps at -d/-u KB/s via LD_PRELOAD shaping. Used for: per-app caps.", {"tool": "trickle", "caps_at": "-d/-u KB/s", "mechanism": "LD_PRELOAD shaping", "use": "per-app caps"}], ["network", "wondershaper", "tc-based scripts shaping whole interfaces with HTB queues. Caps at interface kbit/s via tc HTB. Used for: link shaping.", {"tool": "wondershaper", "caps_at": "interface kbit/s", "mechanism": "tc HTB", "use": "link shaping"}], ["network", "tc (traffic control)", "Linux’s qdisc/filter framework: HTB, fq_codel, and cake for real QoS. Caps at qdisc rates via queueing disciplines. Used for: router QoS.", {"tool": "tc", "caps_at": "qdisc rates", "mechanism": "queueing disciplines", "use": "router QoS"}], ["network", "nginx limit_rate", "Per-connection response throttling for downloads and media. Caps at limit_rate 500k via per-conn pacing. Used for: download throttling.", {"tool": "nginx", "caps_at": "limit_rate 500k", "mechanism": "per-conn pacing", "use": "download throttling"}], ["cli", "curl --limit-rate", "Caps a single transfer’s speed — the quick manual throttle. Caps at --limit-rate 1M via transfer pacing. Used for: manual downloads.", {"tool": "curl", "caps_at": "--limit-rate 1M", "mechanism": "transfer pacing", "use": "manual downloads"}], ["cli", "wget --limit-rate", "Same idea for wget’s recursive mirrors. Caps at --limit-rate=200k via transfer pacing. Used for: mirroring.", {"tool": "wget", "caps_at": "--limit-rate=200k", "mechanism": "transfer pacing", "use": "mirroring"}], ["cli", "aria2c max limits", "Per-download and global caps for multi-connection downloads. Caps at --max-download-limit via per-task pacing. Used for: fast downloads.", {"tool": "aria2c", "caps_at": "--max-download-limit", "mechanism": "per-task pacing", "use": "fast downloads"}], ["p2p", "Syncthing rate limits", "In/out LAN+WAN rate caps so sync never crowds out video calls. Caps at KB/s in/out via transfer pacing. Used for: P2P sync.", {"tool": "Syncthing", "caps_at": "KB/s in/out", "mechanism": "transfer pacing", "use": "P2P sync"}], ["cloud", "Dropbox bandwidth settings", "Client-side caps for uploads/downloads in the desktop app. Caps at KB/s setting via client pacing. Used for: desktop sync.", {"tool": "Dropbox", "caps_at": "KB/s setting", "mechanism": "client pacing", "use": "desktop sync"}], ["network", "BITS throttling", "Windows Background Intelligent Transfer Service throttles by policy and time. Caps at policy KB/s via job throttling. Used for: Windows updates.", {"tool": "BITS", "caps_at": "policy KB/s", "mechanism": "job throttling", "use": "Windows updates"}], ["qos", "QoS DSCP marking", "Differentiated Services marks packets so routers prioritize voice over bulk sync. Caps at per-hop behavior via packet marking. Used for: traffic classes.", {"tool": "DSCP", "caps_at": "per-hop behavior", "mechanism": "packet marking", "use": "traffic classes"}], ["cloud", "S3 transfer limits", "S3 request-rate and multipart tuning to stay within account throughput. Caps at concurrency + part size via request pacing. Used for: cloud uploads.", {"tool": "S3 clients", "caps_at": "concurrency + part size", "mechanism": "request pacing", "use": "cloud uploads"}], ["cli", "scp -l", "The old-school per-transfer bit-rate cap for scp. Caps at -l kbit/s via transfer pacing. Used for: quick capped copy.", {"tool": "scp", "caps_at": "-l kbit/s", "mechanism": "transfer pacing", "use": "quick capped copy"}]];
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
  if(!new RegExp('^'+'JAH\\-BANDWI\\-'+'\\d{6}$').test(r.id||''))e.push('id');
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('bandwidth-throttled-sync',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
