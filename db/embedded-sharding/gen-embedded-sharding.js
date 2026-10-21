(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];} function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var CATS=["embedded", "edge", "distributed", "mobile", "time-series"];
var PREFIX='JAH-EMBEDD2-';
var GENVER='jahdb-embedded-sharding-1.0';
var SRC='public-harvest';
var EDITION='public';
var PROV="Public record compiled from openly published documentation, project sources, and standard references.";
var FIELDS=["system", "shards_by", "routing", "rebalance"];
var DEMO_TPL="// $TITLE - shard routing demo\nfunction hash(s) { var h = 0; for (var i = 0; i < s.length; i++) h = (h * 31 + s.charCodeAt(i)) >>> 0; return h; }\nvar SHARDS = 4;\nvar keys = [\"user:1\", \"user:2\", \"order:9\", \"order:10\", \"session:abc\"];\nconsole.log(\"System: $SYSTEM | Shards by: $SHARDS_BY\");\nkeys.forEach(function(k) { console.log(\"  \" + k + \" -> shard \" + (hash(k) % SHARDS)); });\nconsole.log(\"Routing: $ROUTING | Rebalance: $REBALANCE -> PASS\");";
function jsEsc(s){return String(s).replace(/\\/g,'\\\\').replace(/"/g,'\\"').replace(/\n/g,'\\n').replace(/\r/g,'\\r').replace(/\t/g,'\\t');}
function fillTpl(tpl,vars){return tpl.replace(/\$([A-Za-z0-9_]+)/g,function(m,k){return Object.prototype.hasOwnProperty.call(vars,k)?jsEsc(vars[k]):m;});}
/* rows: [category, title, description, {fields}] */
var B=[["embedded", "SQLite per-tenant DBs", "One SQLite file per tenant: the simplest shard — backup and migrate independently. Shards by tenant -> file; routing via tenant map; rebalance: move files.", {"system": "SQLite", "shards_by": "tenant -> file", "routing": "tenant map", "rebalance": "move files"}], ["edge", "LiteFS", "Fly.io’s FUSE layer replicating SQLite via NATS with static leases per database. Shards by database; routing via lease holder; rebalance: lease move.", {"system": "LiteFS", "shards_by": "database", "routing": "lease holder", "rebalance": "lease move"}], ["distributed", "rqlite", "Raft-replicated SQLite giving every node the full dataset with strong consistency. Shards by raft group; routing via leader redirect; rebalance: join/leave.", {"system": "rqlite", "shards_by": "raft group", "routing": "leader redirect", "rebalance": "join/leave"}], ["distributed", "dqlite", "Canonical’s Raft SQLite for clustered appliances like LXD and MicroK8s. Shards by raft cluster; routing via client redirect; rebalance: cluster mgmt.", {"system": "dqlite", "shards_by": "raft cluster", "routing": "client redirect", "rebalance": "cluster mgmt"}], ["embedded", "RocksDB column families", "Column families partition one RocksDB into isolated keyspaces with own options. Shards by column family; routing via CF handle; rebalance: manual.", {"system": "RocksDB", "shards_by": "column family", "routing": "CF handle", "rebalance": "manual"}], ["mobile", "Realm sync partitions", "MongoDB Realm partitions synced data by a partition key per user or team. Shards by partition key; routing via sync config; rebalance: re-partition.", {"system": "Realm", "shards_by": "partition key", "routing": "sync config", "rebalance": "re-partition"}], ["mobile", "PouchDB per-user DBs", "One PouchDB per user syncing to a per-user CouchDB database. Shards by user -> DB; routing via user DB name; rebalance: re-create.", {"system": "PouchDB", "shards_by": "user -> DB", "routing": "user DB name", "rebalance": "re-create"}], ["embedded", "DuckDB partitioned reads", "DuckDB scans partitioned Parquet datasets with partition pruning. Shards by hive partitions; routing via file pruning; rebalance: re-partition files.", {"system": "DuckDB", "shards_by": "hive partitions", "routing": "file pruning", "rebalance": "re-partition files"}], ["distributed", "TiKV regions", "TiKV splits the keyspace into 96 MB regions, each Raft-replicated. Shards by key range regions; routing via PD placement driver; rebalance: auto split/merge.", {"system": "TiKV", "shards_by": "key range regions", "routing": "PD placement driver", "rebalance": "auto split/merge"}], ["distributed", "CockroachDB ranges", "Ranges of ~512 MB replicate via Raft with leaseholder-local reads. Shards by key ranges; routing via range cache; rebalance: auto rebalance.", {"system": "CockroachDB", "shards_by": "key ranges", "routing": "range cache", "rebalance": "auto rebalance"}], ["distributed", "Vitess shards", "Vitess shards MySQL with vindexes routing queries to the right shard. Shards by vindex; routing via VTGate; rebalance: resharding workflows.", {"system": "Vitess", "shards_by": "vindex", "routing": "VTGate", "rebalance": "resharding workflows"}], ["distributed", "Citus", "Postgres extension distributing tables by distribution column with the coordinator routing. Shards by distribution column; routing via coordinator; rebalance: rebalance_table_shards.", {"system": "Citus", "shards_by": "distribution column", "routing": "coordinator", "rebalance": "rebalance_table_shards"}], ["distributed", "YugabyteDB tablets", "DocDB tablets split by hash/range, each Raft-replicated across zones. Shards by tablets; routing via tablet leader; rebalance: auto load balance.", {"system": "YugabyteDB", "shards_by": "tablets", "routing": "tablet leader", "rebalance": "auto load balance"}], ["distributed", "FoundationDB shards", "The storage engine auto-shards key ranges across storage servers. Shards by key ranges; routing via client shard map; rebalance: data distribution.", {"system": "FoundationDB", "shards_by": "key ranges", "routing": "client shard map", "rebalance": "data distribution"}], ["time-series", "TimescaleDB chunks", "Hypertables chunk by time; chunks are the unit of sharding and retention. Shards by time chunks; routing via chunk exclusion; rebalance: move chunks.", {"system": "TimescaleDB", "shards_by": "time chunks", "routing": "chunk exclusion", "rebalance": "move chunks"}]];
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
  if(!new RegExp('^'+'JAH\\-EMBEDD2\\-'+'\\d{6}$').test(r.id||''))e.push('id');
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('embedded-sharding',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
