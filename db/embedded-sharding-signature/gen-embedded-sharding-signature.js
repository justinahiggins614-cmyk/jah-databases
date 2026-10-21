(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];} function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var CATS=["embedded", "edge", "distributed", "mobile", "time-series"];
var PREFIX='JAH-EMBEDD2-S-';
var GENVER='jahdb-embedded-sharding-signature-1.0';
var SRC='signature-generated-completion';
var EDITION='signature';
var PROV="Signature-original completion authored for the JAH Databases network; clearly labeled Signature, never presented as public record.";
var FIELDS=["system", "shards_by", "routing", "rebalance"];
var DEMO_TPL="// $TITLE - shard routing demo\nfunction hash(s) { var h = 0; for (var i = 0; i < s.length; i++) h = (h * 31 + s.charCodeAt(i)) >>> 0; return h; }\nvar SHARDS = 4;\nvar keys = [\"user:1\", \"user:2\", \"order:9\", \"order:10\", \"session:abc\"];\nconsole.log(\"System: $SYSTEM | Shards by: $SHARDS_BY\");\nkeys.forEach(function(k) { console.log(\"  \" + k + \" -> shard \" + (hash(k) % SHARDS)); });\nconsole.log(\"Routing: $ROUTING | Rebalance: $REBALANCE -> PASS\");";
function jsEsc(s){return String(s).replace(/\\/g,'\\\\').replace(/"/g,'\\"').replace(/\n/g,'\\n').replace(/\r/g,'\\r').replace(/\t/g,'\\t');}
function fillTpl(tpl,vars){return tpl.replace(/\$([A-Za-z0-9_]+)/g,function(m,k){return Object.prototype.hasOwnProperty.call(vars,k)?jsEsc(vars[k]):m;});}
/* rows: [category, title, description, {fields}] */
var B=[["embedded", "SigShard-Hash", "Signature-original: consistent-hash sharding with virtual nodes for smooth scaling. Shards by consistent hash; routing via hash ring; rebalance: virtual node move.", {"system": "SigShard-Hash", "shards_by": "consistent hash", "routing": "hash ring", "rebalance": "virtual node move"}], ["embedded", "SigShard-Range", "Signature-original: range sharding with automatic split on size thresholds. Shards by key ranges; routing via range map; rebalance: auto split/merge.", {"system": "SigShard-Range", "shards_by": "key ranges", "routing": "range map", "rebalance": "auto split/merge"}], ["embedded", "SigShard-Tenant", "Signature-original: tenant-isolated shards with per-tenant encryption keys. Shards by tenant; routing via tenant directory; rebalance: tenant move.", {"system": "SigShard-Tenant", "shards_by": "tenant", "routing": "tenant directory", "rebalance": "tenant move"}], ["edge", "SigShard-Geo", "Signature-original: geo sharding keeping data in-region with cross-region replicas. Shards by geography; routing via geo directory; rebalance: region rebalance.", {"system": "SigShard-Geo", "shards_by": "geography", "routing": "geo directory", "rebalance": "region rebalance"}], ["time-series", "SigShard-Time", "Signature-original: time sharding with automatic rollup as chunks age. Shards by time windows; routing via time index; rebalance: rollup.", {"system": "SigShard-Time", "shards_by": "time windows", "routing": "time index", "rebalance": "rollup"}], ["edge", "SigShard-Edge", "Signature-original: edge shards syncing deltas to the core on schedule. Shards by edge site; routing via site directory; rebalance: site reassignment.", {"system": "SigShard-Edge", "shards_by": "edge site", "routing": "site directory", "rebalance": "site reassignment"}], ["distributed", "SigShard-CRDT", "Signature-original: CRDT shards merging without coordination. Shards by causal regions; routing via any replica; rebalance: merge.", {"system": "SigShard-CRDT", "shards_by": "causal regions", "routing": "any replica", "rebalance": "merge"}], ["distributed", "SigShard-Raft", "Signature-original: Raft per shard with shared witness optimization. Shards by raft groups; routing via leader cache; rebalance: joint consensus.", {"system": "SigShard-Raft", "shards_by": "raft groups", "routing": "leader cache", "rebalance": "joint consensus"}], ["embedded", "SigShard-Cache", "Signature-original: hot shards cached in memory with write-through to cold. Shards by heat; routing via heat map; rebalance: promotion.", {"system": "SigShard-Cache", "shards_by": "heat", "routing": "heat map", "rebalance": "promotion"}], ["embedded", "SigShard-Policy", "Signature-original: declarative sharding policies compiled to routing tables. Shards by policy; routing via compiled tables; rebalance: policy change.", {"system": "SigShard-Policy", "shards_by": "policy", "routing": "compiled tables", "rebalance": "policy change"}], ["distributed", "SigShard-Verify", "Signature-original: cross-shard verification with Merkle proofs per shard. Shards by any; routing via proof-carrying; rebalance: n/a.", {"system": "SigShard-Verify", "shards_by": "any", "routing": "proof-carrying", "rebalance": "n/a"}], ["distributed", "SigShard-Backup", "Signature-original: per-shard backup schedules with global restore orchestration. Shards by shard; routing via backup index; rebalance: restore planner.", {"system": "SigShard-Backup", "shards_by": "shard", "routing": "backup index", "rebalance": "restore planner"}], ["embedded", "SigShard-Quota", "Signature-original: per-shard quotas preventing noisy-neighbor overflow. Shards by tenant/shard; routing via quota guard; rebalance: quota move.", {"system": "SigShard-Quota", "shards_by": "tenant/shard", "routing": "quota guard", "rebalance": "quota move"}], ["distributed", "SigShard-Migrate", "Signature-original: online shard migration with dual-write cutover. Shards by any; routing via dual-write; rebalance: live move.", {"system": "SigShard-Migrate", "shards_by": "any", "routing": "dual-write", "rebalance": "live move"}], ["distributed", "SigShard-One", "Signature-original: the united sharding plane — one scheme language, every store. Shards by unified; routing via unified directory; rebalance: auto.", {"system": "SigShard-One", "shards_by": "unified", "routing": "unified directory", "rebalance": "auto"}]];
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
  if(!new RegExp('^'+'JAH\\-EMBEDD2\\-S\\-'+'\\d{6}$').test(r.id||''))e.push('id');
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('embedded-sharding-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
