(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];} function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var CATS=["cdn", "client", "server", "dns", "degraded"];
var PREFIX='JAH-ISF-S-';
var GENVER='jahdb-instant-static-fallbacks-signature-1.0';
var SRC='signature-generated-completion';
var EDITION='signature';
var PROV="Signature-original completion authored for the JAH Databases network; clearly labeled Signature, never presented as public record.";
var FIELDS=["pattern", "triggers", "serves", "example"];
var DEMO_TPL="// $TITLE - fallback chain demo\nvar chain = [\n  { name: \"live backend\", ok: false },\n  { name: \"$PATTERN\", ok: true }\n];\nvar served = null;\nfor (var i = 0; i < chain.length; i++) { if (chain[i].ok) { served = chain[i].name; break; } }\nconsole.log(\"Pattern: $PATTERN | Serves: $SERVES\");\nconsole.log(\"Backend down -> fallback engaged: \" + served);\nconsole.log(served ? \"RESULT: user still gets a page -> PASS\" : \"RESULT: outage\");";
function jsEsc(s){return String(s).replace(/\\/g,'\\\\').replace(/"/g,'\\"').replace(/\n/g,'\\n').replace(/\r/g,'\\r').replace(/\t/g,'\\t');}
function fillTpl(tpl,vars){return tpl.replace(/\$([A-Za-z0-9_]+)/g,function(m,k){return Object.prototype.hasOwnProperty.call(vars,k)?jsEsc(vars[k]):m;});}
/* rows: [category, title, description, {fields}] */
var B=[["cdn", "SigFall-Stale", "Signature-original: edge nodes serve cryptographically timestamped stale copies with age headers. Triggers when origin failure; serves signed stale copy. Example: sigedge serve --stale-signed.", {"pattern": "SigFall-Stale", "triggers": "origin failure", "serves": "signed stale copy", "example": "sigedge serve --stale-signed"}], ["client", "SigFall-Shell", "Signature-original: app shells with embedded last-known data for zero-network starts. Triggers when offline; serves shell + data. Example: sigpwa shell --embed-data.", {"pattern": "SigFall-Shell", "triggers": "offline", "serves": "shell + data", "example": "sigpwa shell --embed-data"}], ["cdn", "SigFall-Mesh", "Signature-original: fall back to peer mesh copies when the origin and CDN both fail. Triggers when origin + CDN down; serves mesh copy. Example: sigmesh fetch <url>.", {"pattern": "SigFall-Mesh", "triggers": "origin + CDN down", "serves": "mesh copy", "example": "sigmesh fetch <url>"}], ["degraded", "SigFall-ReadOnly", "Signature-original: automatic read-only promotion with write-intent queuing. Triggers when primary write path down; serves reads + queued writes. Example: sigdb degrade --readonly.", {"pattern": "SigFall-ReadOnly", "triggers": "primary write path down", "serves": "reads + queued writes", "example": "sigdb degrade --readonly"}], ["server", "SigFall-Snap", "Signature-original: per-minute snapshots promotable to live in one command. Triggers when bad deploy; serves last snapshot. Example: sigfall promote --last-good.", {"pattern": "SigFall-Snap", "triggers": "bad deploy", "serves": "last snapshot", "example": "sigfall promote --last-good"}], ["dns", "SigFall-DNS", "Signature-original: mesh-aware DNS failing over in under 5 seconds with signed records. Triggers when region failure; serves healthy region. Example: sigdns failover --auto.", {"pattern": "SigFall-DNS", "triggers": "region failure", "serves": "healthy region", "example": "sigdns failover --auto"}], ["degraded", "SigFall-Queue", "Signature-original: every write path gets a durable local queue by default. Triggers when backend down; serves durable queue. Example: sigqueue spill --auto.", {"pattern": "SigFall-Queue", "triggers": "backend down", "serves": "durable queue", "example": "sigqueue spill --auto"}], ["server", "SigFall-Static", "Signature-original: continuous static rendering so a static copy always exists. Triggers when dynamic failure; serves static render. Example: sigrender --continuous.", {"pattern": "SigFall-Static", "triggers": "dynamic failure", "serves": "static render", "example": "sigrender --continuous"}], ["client", "SigFall-Image", "Signature-original: responsive image fallbacks generated at build for every asset. Triggers when asset 404; serves generated placeholder. Example: sigimg fallback --all.", {"pattern": "SigFall-Image", "triggers": "asset 404", "serves": "generated placeholder", "example": "sigimg fallback --all"}], ["degraded", "SigFall-Flags", "Signature-original: flag system with automatic rollback on error-budget burn. Triggers when error budget burn; serves previous flag state. Example: sigflag auto-rollback.", {"pattern": "SigFall-Flags", "triggers": "error budget burn", "serves": "previous flag state", "example": "sigflag auto-rollback"}], ["server", "SigFall-Maint", "Signature-original: maintenance pages with live status and queue-position for users. Triggers when planned work; serves status page. Example: sigmaint on --eta 30m.", {"pattern": "SigFall-Maint", "triggers": "planned work", "serves": "status page", "example": "sigmaint on --eta 30m"}], ["cdn", "SigFall-API", "Signature-original: API gateways serving versioned snapshots with deprecation headers. Triggers when upstream stall; serves versioned snapshot. Example: sigapi snapshot --serve.", {"pattern": "SigFall-API", "triggers": "upstream stall", "serves": "versioned snapshot", "example": "sigapi snapshot --serve"}], ["degraded", "SigFall-DB", "Signature-original: replica promotion with zero-downtime cutover and lag guards. Triggers when primary failure; serves promoted replica. Example: sigdb promote --lag-max 5s.", {"pattern": "SigFall-DB", "triggers": "primary failure", "serves": "promoted replica", "example": "sigdb promote --lag-max 5s"}], ["server", "SigFall-Cell", "Signature-original: failed cells replaced from frozen images in under a second. Triggers when cell crash; serves fresh cell. Example: sigcell replace --from-freeze.", {"pattern": "SigFall-Cell", "triggers": "cell crash", "serves": "fresh cell", "example": "sigcell replace --from-freeze"}], ["cdn", "SigFall-One", "Signature-original: the united fallback plane — every layer degrades gracefully as one system. Triggers when any failure; serves graceful degradation. Example: sigfall status.", {"pattern": "SigFall-One", "triggers": "any failure", "serves": "graceful degradation", "example": "sigfall status"}]];
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
  if(!new RegExp('^'+'JAH\\-ISF\\-S\\-'+'\\d{6}$').test(r.id||''))e.push('id');
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('instant-static-fallbacks-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
