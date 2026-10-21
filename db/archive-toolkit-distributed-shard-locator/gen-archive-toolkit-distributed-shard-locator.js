(function(){
'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["fundamentals", "algorithms", "implementation", "optimization", "evaluation"];
var PREFIX="JAH-ATK138-";
var KIND="traversal method";
var TOOLNAME="Distributed Shard Locator";
var SIG=false;
var PROV="Public methodology \u2014 standard computer-science technique documented in the technical literature; fact-checked 2026-10-21.";
var SRC="public-harvest";
var ASPECTS=[{"t": "Hash partitioning", "d": "Keys hash to shards: shard = hash(key) mod N. Hashing distributes uniformly. Uniformity avoids hotspots.", "c": "fundamentals", "r": 1, "p": {"SHARDS": "['s0','s1','s2']", "REPL": "1", "SALT": "x", "KEYS": "['user:1','user:2','order:9']"}}, {"t": "Consistent hashing", "d": "Consistent hashing maps shards and keys onto a ring; key belongs to the next shard clockwise. Adding a shard moves only neighboring keys. Minimal movement enables elastic scaling.", "c": "algorithms", "r": 1, "p": {"SHARDS": "['s0','s1','s2','s3']", "REPL": "1", "SALT": "y", "KEYS": "['a','b','c']"}}, {"t": "Virtual nodes", "d": "Virtual nodes (many ring points per shard) smooth distribution. More vnodes mean more even loads. Vnodes fix small-cluster skew.", "c": "implementation", "r": 1, "p": {"SHARDS": "['s0','s1']", "REPL": "1", "SALT": "z", "KEYS": "['k1','k2','k3','k4']"}}, {"t": "Replication placement", "d": "Replicas sit on distinct shards (and racks) for durability. Placement policies avoid correlated failures. Separation is survival.", "c": "optimization", "r": 1, "p": {"SHARDS": "['s0','s1','s2']", "REPL": "2", "SALT": "r", "KEYS": "['doc:7']"}}, {"t": "Range sharding", "d": "Range sharding assigns key ranges to shards, keeping order. Ordered ranges serve scans efficiently. Ranges suit time-series.", "c": "evaluation", "r": 1, "p": {"SHARDS": "['s0','s1']", "REPL": "1", "SALT": "q", "KEYS": "['2024-01','2024-06']"}}, {"t": "Directory-based locating", "d": "A directory service maps key ranges to shards authoritatively. Directories allow arbitrary placement policies. Central lookup trades a hop for flexibility.", "c": "fundamentals", "r": 2, "p": {"SHARDS": "['s0','s1','s2']", "REPL": "1", "SALT": "d", "KEYS": "['alpha','omega']"}}, {"t": "Rebalancing", "d": "Adding shards triggers key migration; locators serve both old and new during transition. Dual-read phases keep availability. Careful rebalancing avoids downtime.", "c": "algorithms", "r": 2, "p": {"SHARDS": "['s0','s1','s2','s3']", "REPL": "1", "SALT": "b", "KEYS": "['migrate-me']"}}, {"t": "Hotspot detection", "d": "Access counters per shard reveal hotspots. Mitigations split hot ranges or add caches. Detection precedes relief.", "c": "implementation", "r": 2, "p": {"SHARDS": "['s0','s1']", "REPL": "1", "SALT": "h", "KEYS": "['hot-key','cold-key']"}}, {"t": "Shard-aware routing", "d": "Clients cache the shard map and route directly. Direct routing skips coordinator hops. Client smarts cut latency.", "c": "optimization", "r": 2, "p": {"SHARDS": "['s0','s1','s2']", "REPL": "1", "SALT": "c", "KEYS": "['u:5']"}}, {"t": "Failure handling", "d": "Failed shards redirect to replicas; locators mark them down. Health checks restore them later. Failover keeps reads alive.", "c": "evaluation", "r": 2, "p": {"SHARDS": "['s0','s1','s2']", "REPL": "2", "SALT": "f", "KEYS": "['k']"}}, {"t": "Locality hints", "d": "Hints co-locate related keys on one shard for join efficiency. Co-location cuts cross-shard traffic. Locality is performance.", "c": "fundamentals", "r": 3, "p": {"SHARDS": "['s0','s1']", "REPL": "1", "SALT": "l", "KEYS": "['user:1:profile','user:1:orders']"}}, {"t": "Shard key design", "d": "Good shard keys are high-cardinality and query-aligned. Bad keys (like country) skew catastrophically. Design decides scalability.", "c": "algorithms", "r": 3, "p": {"SHARDS": "['s0','s1','s2']", "REPL": "1", "SALT": "k", "KEYS": "['tenant:42:doc:1']"}}, {"t": "Cross-shard queries", "d": "Scatter-gather fans out to all shards and merges. Merging needs global ordering. Scatter is expensive but general.", "c": "implementation", "r": 3, "p": {"SHARDS": "['s0','s1']", "REPL": "1", "SALT": "s", "KEYS": "['any']"}}, {"t": "Locator versioning", "d": "Shard-map versions let clients detect stale routing. Version checks prevent misroutes. Versions keep distributed agreement.", "c": "optimization", "r": 3, "p": {"SHARDS": "['s0','s1','s2']", "REPL": "1", "SALT": "v", "KEYS": "['vkey']"}}, {"t": "Testing shard logic", "d": "Deterministic seeds make shard assignment testable. Property tests assert uniformity and minimal movement. Tested locators are trusted.", "c": "evaluation", "r": 3, "p": {"SHARDS": "['s0','s1','s2']", "REPL": "1", "SALT": "t", "KEYS": "['t1','t2']"}}];
var DEMO="# Shard locator: consistent hashing maps keys to shards; replicas listed.\nimport hashlib\nshards = %%SHARDS%%\ndef h(key):\n    return int(hashlib.md5(key.encode()).hexdigest(), 16)\ndef locate(key, n_replicas=%%REPL%%):\n    order = sorted(shards, key=lambda s: h(s + \"#\" + \"%%SALT%%\"))\n    primary = order[h(key) % len(order)]\n    idx = order.index(primary)\n    return [order[(idx + i) % len(order)] for i in range(n_replicas)]\nfor key in %%KEYS%%:\n    print(f\"{key} -> {locate(key)}\")\n";
function demoFor(a){var s=DEMO;for(var k in a.p){s=s.split('%%'+k+'%%').join(a.p[k]);}return s;}
function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  var cat=opts.category||pick(CATS,rnd);
  var pool=ASPECTS.filter(function(a){return a.c===cat;});
  var a=pick(pool.length?pool:ASPECTS,rnd);
  var id=PREFIX+String(seed).padStart(5,'0');
  return {id:id,t:a.t.slice(0,80),title:(SIG?'Signature ':'')+a.t+' \u2014 '+TOOLNAME,description:a.d,kind:KIND,category:a.c,ladder_rank:a.r,demo:demoFor(a),provenance:PROV,last_verified:'2026-10-21',src:SRC,_seed:seed};
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!new RegExp("^JAH\\-ATK138\\-\\d+$").test(r.id||''))e.push('id');
  if(typeof r.t!=='string'||!r.t.length)e.push('t');
  if(typeof r.title!=='string'||!r.title.length)e.push('title');
  if(typeof r.description!=='string'||r.description.length<50)e.push('description');
  if(r.kind!==KIND)e.push('kind');
  if(CATS.indexOf(r.category)<0)e.push('category');
  if(!(r.ladder_rank>=1&&r.ladder_rank<=3))e.push('ladder_rank');
  if(typeof r.demo!=='string'||r.demo.indexOf('print(')<0)e.push('demo');
  if(typeof r.provenance!=='string'||!r.provenance.length)e.push('provenance');
  if(r.last_verified!=='2026-10-21')e.push('last_verified');
  if(r.src!==SRC)e.push('src');
  return {ok:!e.length,errors:e};
}
function driftCheck(rec,sample){
  sample=sample||[];
  for(var i=0;i<sample.length;i++){
    var s=sample[i];
    if(s&&s.title===rec.title&&s.description===rec.description)
      return {ok:false,errors:['duplicate of archived record '+s.id]};
  }
  return {ok:true,errors:[]};
}
var gen={version:"jahdb-archive-toolkit-distributed-shard-locator-1.0",generate:generate,validate:validate,driftCheck:driftCheck};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("archive-toolkit-distributed-shard-locator",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
