(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];} function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var CATS=["mobile", "web", "database", "messaging", "tooling"];
var PREFIX='JAH-OSQ-';
var GENVER='jahdb-offline-sync-queues-1.0';
var SRC='public-harvest';
var EDITION='public';
var PROV="Public record compiled from openly published documentation, project sources, and standard references.";
var FIELDS=["queue", "stores", "syncs_via", "conflict"];
var DEMO_TPL="// $TITLE - offline queue demo\nvar queue = [];\nvar online = false;\nfunction enqueue(op) { queue.push(op); console.log(\"queued offline: \" + op); }\nfunction sync() {\n  console.log(\"back online - syncing \" + queue.length + \" ops via $SYNCS_VIA\");\n  queue.forEach(function(op) { console.log(\"  applied: \" + op); });\n  queue = [];\n}\nenqueue(\"create note 1\"); enqueue(\"update note 1\");\nconsole.log(\"Queue depth while offline: \" + queue.length);\nonline = true; sync();\nconsole.log(\"Conflict strategy: $CONFLICT | Queue drained -> PASS\");";
function jsEsc(s){return String(s).replace(/\\/g,'\\\\').replace(/"/g,'\\"').replace(/\n/g,'\\n').replace(/\r/g,'\\r').replace(/\t/g,'\\t');}
function fillTpl(tpl,vars){return tpl.replace(/\$([A-Za-z0-9_]+)/g,function(m,k){return Object.prototype.hasOwnProperty.call(vars,k)?jsEsc(vars[k]):m;});}
/* rows: [category, title, description, {fields}] */
var B=[["database", "Outbox pattern", "Write intents to a local outbox table; a relay publishes them when connectivity returns. Stores pending intents; syncs via relay publisher. Conflict strategy: server wins / merge.", {"queue": "DB outbox table", "stores": "pending intents", "syncs_via": "relay publisher", "conflict": "server wins / merge"}], ["mobile", "SQLite queue", "A local SQLite table as the durable queue — crash-safe and queryable. Stores queued ops; syncs via sync worker. Conflict strategy: last-write-wins + vector clocks.", {"queue": "SQLite", "stores": "queued ops", "syncs_via": "sync worker", "conflict": "last-write-wins + vector clocks"}], ["mobile", "Android WorkManager", "Defers background sync until constraints (network, charging) are met. Stores work requests; syncs via constraint-aware worker. Conflict strategy: app-defined.", {"queue": "WorkManager", "stores": "work requests", "syncs_via": "constraint-aware worker", "conflict": "app-defined"}], ["web", "Background Sync API", "Service workers retry failed fetches when the browser regains connectivity. Stores failed requests; syncs via sync event. Conflict strategy: retry with backoff.", {"queue": "service worker", "stores": "failed requests", "syncs_via": "sync event", "conflict": "retry with backoff"}], ["database", "Kafka outbox", "Debezium tails the outbox table into Kafka for exactly-once downstream delivery. Stores change events; syncs via Debezium CDC. Conflict strategy: idempotent consumers.", {"queue": "Kafka topic", "stores": "change events", "syncs_via": "Debezium CDC", "conflict": "idempotent consumers"}], ["messaging", "MQTT persistent sessions", "MQTT brokers queue QoS1/2 messages for disconnected clients by session. Stores inflight messages; syncs via session resume. Conflict strategy: broker redelivery.", {"queue": "broker session", "stores": "inflight messages", "syncs_via": "session resume", "conflict": "broker redelivery"}], ["database", "PouchDB/CouchDB sync", "Bidirectional replication with MVCC revisions resolving most conflicts automatically. Stores local docs; syncs via _replicate. Conflict strategy: revision tree merge.", {"queue": "PouchDB", "stores": "local docs", "syncs_via": "_replicate", "conflict": "revision tree merge"}], ["database", "Firebase offline", "Firestore caches writes locally and syncs with latency compensation. Stores pending writes; syncs via SDK sync. Conflict strategy: last-write-wins.", {"queue": "Firestore cache", "stores": "pending writes", "syncs_via": "SDK sync", "conflict": "last-write-wins"}], ["mobile", "WatermelonDB sync", "Pull/push sync with per-table timestamps for React Native offline apps. Stores dirty records; syncs via synchronize(). Conflict strategy: server timestamp wins.", {"queue": "WatermelonDB", "stores": "dirty records", "syncs_via": "synchronize()", "conflict": "server timestamp wins"}], ["database", "CRDT op logs", "Operation logs merge commutatively — conflicts are mathematically impossible. Stores operations; syncs via log exchange. Conflict strategy: CRDT merge.", {"queue": "op log", "stores": "operations", "syncs_via": "log exchange", "conflict": "CRDT merge"}], ["messaging", "MSMQ", "Microsoft’s durable message queuing with transactional exactly-once delivery. Stores messages; syncs via queue manager. Conflict strategy: transactional.", {"queue": "MSMQ", "stores": "messages", "syncs_via": "queue manager", "conflict": "transactional"}], ["messaging", "RabbitMQ durable queues", "Durable queues + persistent messages survive broker restarts. Stores persistent msgs; syncs via AMQP consumers. Conflict strategy: redelivery + ack.", {"queue": "RabbitMQ", "stores": "persistent msgs", "syncs_via": "AMQP consumers", "conflict": "redelivery + ack"}], ["tooling", "Sidekiq retries", "Failed jobs retry with exponential backoff into a dead queue after 25 tries. Stores jobs; syncs via workers. Conflict strategy: at-least-once.", {"queue": "Redis (Sidekiq)", "stores": "jobs", "syncs_via": "workers", "conflict": "at-least-once"}], ["tooling", "BullMQ", "Redis-based Node queues with delayed, repeated, and prioritized jobs. Stores jobs; syncs via workers. Conflict strategy: at-least-once + dedupe.", {"queue": "Redis (BullMQ)", "stores": "jobs", "syncs_via": "workers", "conflict": "at-least-once + dedupe"}], ["messaging", "NATS JetStream", "Persistent streams with consumer ack semantics for edge-to-cloud sync. Stores streams; syncs via consumers. Conflict strategy: ack-based redelivery.", {"queue": "JetStream", "stores": "streams", "syncs_via": "consumers", "conflict": "ack-based redelivery"}]];
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
  if(!new RegExp('^'+'JAH\\-OSQ\\-'+'\\d{6}$').test(r.id||''))e.push('id');
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('offline-sync-queues',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
