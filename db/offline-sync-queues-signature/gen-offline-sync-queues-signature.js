(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];} function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var CATS=["mobile", "web", "database", "messaging", "tooling"];
var PREFIX='JAH-OSQ-S-';
var GENVER='jahdb-offline-sync-queues-signature-1.0';
var SRC='signature-generated-completion';
var EDITION='signature';
var PROV="Signature-original completion authored for the JAH Databases network; clearly labeled Signature, never presented as public record.";
var FIELDS=["queue", "stores", "syncs_via", "conflict"];
var DEMO_TPL="// $TITLE - offline queue demo\nvar queue = [];\nvar online = false;\nfunction enqueue(op) { queue.push(op); console.log(\"queued offline: \" + op); }\nfunction sync() {\n  console.log(\"back online - syncing \" + queue.length + \" ops via $SYNCS_VIA\");\n  queue.forEach(function(op) { console.log(\"  applied: \" + op); });\n  queue = [];\n}\nenqueue(\"create note 1\"); enqueue(\"update note 1\");\nconsole.log(\"Queue depth while offline: \" + queue.length);\nonline = true; sync();\nconsole.log(\"Conflict strategy: $CONFLICT | Queue drained -> PASS\");";
function jsEsc(s){return String(s).replace(/\\/g,'\\\\').replace(/"/g,'\\"').replace(/\n/g,'\\n').replace(/\r/g,'\\r').replace(/\t/g,'\\t');}
function fillTpl(tpl,vars){return tpl.replace(/\$([A-Za-z0-9_]+)/g,function(m,k){return Object.prototype.hasOwnProperty.call(vars,k)?jsEsc(vars[k]):m;});}
/* rows: [category, title, description, {fields}] */
var B=[["database", "SigOutbox", "Signature-original: outbox with exactly-once relay and idempotency keys built in. Stores intents; syncs via SigRelay. Conflict strategy: idempotent merge.", {"queue": "SigOutbox", "stores": "intents", "syncs_via": "SigRelay", "conflict": "idempotent merge"}], ["mobile", "SigQueue-Mobile", "Signature-original: battery-aware sync batching by network type. Stores ops; syncs via SigSync worker. Conflict strategy: CRDT merge.", {"queue": "SigQueue-Mobile", "stores": "ops", "syncs_via": "SigSync worker", "conflict": "CRDT merge"}], ["web", "SigQueue-Web", "Signature-original: service-worker queues with background sync and periodic sync. Stores requests; syncs via SW sync. Conflict strategy: retry + merge.", {"queue": "SigQueue-Web", "stores": "requests", "syncs_via": "SW sync", "conflict": "retry + merge"}], ["messaging", "SigQueue-Mesh", "Signature-original: queues replicating across mesh peers for offline-first fleets. Stores messages; syncs via mesh gossip. Conflict strategy: causal merge.", {"queue": "SigQueue-Mesh", "stores": "messages", "syncs_via": "mesh gossip", "conflict": "causal merge"}], ["messaging", "SigQueue-IoT", "Signature-original: store-and-forward for sensors with tiny RAM footprints. Stores readings; syncs via gateway sync. Conflict strategy: time-series merge.", {"queue": "SigQueue-IoT", "stores": "readings", "syncs_via": "gateway sync", "conflict": "time-series merge"}], ["database", "SigCRDT-Log", "Signature-original: operation logs with automatic schema-aware merging. Stores ops; syncs via log exchange. Conflict strategy: CRDT.", {"queue": "SigCRDT-Log", "stores": "ops", "syncs_via": "log exchange", "conflict": "CRDT"}], ["tooling", "SigSync-Policy", "Signature-original: declarative sync policies — what syncs, when, on which network. Stores policies; syncs via policy engine. Conflict strategy: policy-defined.", {"queue": "SigSync-Policy", "stores": "policies", "syncs_via": "policy engine", "conflict": "policy-defined"}], ["tooling", "SigDedup-Queue", "Signature-original: queue dedup collapsing redundant ops before sync. Stores deduped ops; syncs via workers. Conflict strategy: collapse.", {"queue": "SigDedup", "stores": "deduped ops", "syncs_via": "workers", "conflict": "collapse"}], ["tooling", "SigPriority-Queue", "Signature-original: priority lanes syncing user-visible changes first. Stores prioritized ops; syncs via lane workers. Conflict strategy: priority merge.", {"queue": "SigPriority", "stores": "prioritized ops", "syncs_via": "lane workers", "conflict": "priority merge"}], ["messaging", "SigEncrypt-Queue", "Signature-original: end-to-end encrypted queues even the relay cannot read. Stores sealed ops; syncs via blind relay. Conflict strategy: client merge.", {"queue": "SigEncrypt", "stores": "sealed ops", "syncs_via": "blind relay", "conflict": "client merge"}], ["tooling", "SigAudit-Queue", "Signature-original: every queued op hash-chained for tamper-evident offline work. Stores chained ops; syncs via verified relay. Conflict strategy: chain verify.", {"queue": "SigAudit", "stores": "chained ops", "syncs_via": "verified relay", "conflict": "chain verify"}], ["tooling", "SigCompress-Queue", "Signature-original: delta-compressed queue payloads for metered links. Stores delta ops; syncs via SigDelta. Conflict strategy: delta merge.", {"queue": "SigCompress", "stores": "delta ops", "syncs_via": "SigDelta", "conflict": "delta merge"}], ["tooling", "SigQuota-Queue", "Signature-original: queue quotas with oldest-low-priority eviction. Stores bounded ops; syncs via workers. Conflict strategy: eviction policy.", {"queue": "SigQuota", "stores": "bounded ops", "syncs_via": "workers", "conflict": "eviction policy"}], ["tooling", "SigReplay-Queue", "Signature-original: replayable queues for debugging exactly what synced. Stores replay log; syncs via replay. Conflict strategy: deterministic.", {"queue": "SigReplay", "stores": "replay log", "syncs_via": "replay", "conflict": "deterministic"}], ["database", "SigSync-One", "Signature-original: the united sync plane — one queue abstraction for every client. Stores everything; syncs via SigSync. Conflict strategy: unified merge.", {"queue": "SigSync-One", "stores": "everything", "syncs_via": "SigSync", "conflict": "unified merge"}]];
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
  if(!new RegExp('^'+'JAH\\-OSQ\\-S\\-'+'\\d{6}$').test(r.id||''))e.push('id');
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('offline-sync-queues-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
