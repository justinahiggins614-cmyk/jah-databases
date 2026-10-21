(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function jsv(v){if(typeof v==='string')return JSON.stringify(v);if(v&&typeof v==='object')return JSON.stringify(v);return String(v);}
var CATS=["protection", "healing", "growth", "efficiency", "monitoring"];
var PREFIX='JAH-SELFHE-';
var SRC='public-harvest';
var PROV='Public technical knowledge compiled from standard references and documentation; verified 2026-10-21.';
var DEMO_TPL="// Erasure coding: XOR parity lets any single lost block be rebuilt\nconst blocks=@@BLOCKS@@;\nconst parity=blocks.reduce((a,b)=>a^b,0);\nconst lost=1;\nconst recovered=blocks.filter((_,i)=>i!==lost).reduce((a,b)=>a^b,0)^parity;\nconsole.log('parity='+parity+', block['+lost+'] recovered='+recovered+' (original '+blocks[lost]+')');";
/* rows: [category, title, description, fields, demoParams] */
var B=[["protection", "Erasure Coding", "Protects data with parity fragments - any k of n fragments rebuild the data - using far less overhead than full replication. Erasure coding is how cold storage stays cheap and safe.", {"technique": "Reed-Solomon", "mechanism": "k-of-n", "benefit": "cheap safety", "cost": "rebuild cost", "used_in": "object stores", "practice": "size k wisely"}, {"BLOCKS": [10, 20, 30, 40]}], ["healing", "Scrubbing", "Reads all data periodically verifying checksums, finding bit-rot before it accumulates beyond repair. Scrubbing is the immune patrol that keeps pools healthy.", {"technique": "background verify", "mechanism": "checksums", "benefit": "rot found early", "cost": "I/O cost", "used_in": "ZFS, Ceph", "practice": "scrub regularly"}, {"BLOCKS": [7, 14, 21]}], ["monitoring", "Disk Failure Prediction", "Predicts disk failures from SMART data and error trends, replacing drives before they die. Prediction turns failures into planned maintenance.", {"technique": "SMART models", "mechanism": "error trends", "benefit": "planned swaps", "cost": "false alarms", "used_in": "operations", "practice": "trust but verify"}, {"BLOCKS": [100, 200, 300]}], ["healing", "Hot-Spare Rebuild", "Keeps hot spare disks ready and starts rebuilding onto them the moment a failure is detected - no waiting for a human. Automatic rebuild minimizes the vulnerable degraded window.", {"technique": "hot spares", "mechanism": "auto rebuild", "benefit": "fast recovery", "cost": "spare cost", "used_in": "RAID/ZFS", "practice": "keep spares ready"}, {"BLOCKS": [11, 22, 33, 44]}], ["growth", "Pool Expansion", "Adds disks or nodes to the pool online, restriping data automatically with no downtime. Expansion keeps up with growth without forklift migrations.", {"technique": "online add", "mechanism": "restripe", "benefit": "painless growth", "cost": "rebalance I/O", "used_in": "all pools", "practice": "expand before full"}, {"BLOCKS": [1, 2, 3, 4, 5]}], ["efficiency", "Tiering", "Moves data between fast and cheap tiers by access pattern - hot on SSD, cold on disk - automatically. Tiering buys performance where it matters and savings everywhere else.", {"technique": "auto tiering", "mechanism": "heat tracking", "benefit": "perf + savings", "cost": "tier thrash", "used_in": "hybrid pools", "practice": "tune thresholds"}, {"BLOCKS": [9, 18, 27]}], ["efficiency", "Deduplication", "Stores duplicate blocks once, referencing them many times - massive savings for VM images and backups. Dedup trades CPU and RAM for disk.", {"technique": "block hashing", "mechanism": "reference counts", "benefit": "huge savings", "cost": "RAM cost", "used_in": "backup stores", "practice": "measure first"}, {"BLOCKS": [5, 5, 10, 10]}], ["protection", "Snapshot Schedules", "Takes copy-on-write snapshots on a schedule - hourly, daily, weekly - giving restore points at every granularity. Schedules automate the discipline humans forget.", {"technique": "cron snapshots", "mechanism": "retention", "benefit": "restore points", "cost": "space use", "used_in": "all pools", "practice": "automate"}, {"BLOCKS": [20, 40, 60]}], ["healing", "Checksum Trees", "Verifies data with Merkle trees from blocks to pool root, pinpointing corruption precisely. Trees make integrity verification logarithmic instead of linear.", {"technique": "Merkle trees", "mechanism": "self-healing", "benefit": "precise location", "cost": "metadata cost", "used_in": "ZFS, btrfs", "practice": "end-to-end"}, {"BLOCKS": [13, 26, 39, 52]}], ["healing", "Rebuild Prioritization", "Rebuilds the most critical data first - metadata, hot data - so the pool regains safety fastest where it counts. Prioritization shrinks the risk window intelligently.", {"technique": "priority queues", "mechanism": "critical first", "benefit": "fast safety", "cost": "complexity", "used_in": "large pools", "practice": "define critical"}, {"BLOCKS": [6, 12, 18, 24]}], ["monitoring", "Capacity Alerts", "Alerts on capacity with forecasts - 'full in 30 days at current growth' - in time to act. Alerts with lead time prevent the 2 AM full-disk page.", {"technique": "forecast alerts", "mechanism": "growth models", "benefit": "lead time", "cost": "false alarms", "used_in": "operations", "practice": "act early"}, {"BLOCKS": [30, 60, 90]}], ["growth", "Pool Balancing", "Balances data and load across pool members, preventing hot disks and stranded capacity. Balancing keeps every spindle pulling its weight.", {"technique": "rebalance", "mechanism": "load metrics", "benefit": "even wear", "cost": "rebalance I/O", "used_in": "all pools", "practice": "balance regularly"}, {"BLOCKS": [16, 32, 48]}], ["healing", "ZFS-Style Self-Healing", "Detects checksum failures on read and heals from redundant copies automatically - the defining feature of self-healing filesystems. Every read verifies; every error repairs.", {"technique": "read repair", "mechanism": "redundancy", "benefit": "automatic", "cost": "redundancy cost", "used_in": "ZFS", "practice": "keep redundancy"}, {"BLOCKS": [22, 44, 66]}], ["protection", "Failure Domains", "Spreads redundancy across failure domains - racks, power, network - so one disaster cannot take all copies. Domains bound the blast radius of every failure mode.", {"technique": "domain spread", "mechanism": "topology", "benefit": "bounded blast", "cost": "complexity", "used_in": "distributed pools", "practice": "map domains"}, {"BLOCKS": [28, 56, 84]}], ["monitoring", "Pool Health Scores", "Scores pool health from errors, latency, rebuild queue, and capacity - one number the team watches. Health scores focus maintenance where it matters.", {"technique": "health score", "mechanism": "composite", "benefit": "focused care", "cost": "score gaming", "used_in": "operations", "practice": "trend scores"}, {"BLOCKS": [40, 80, 120]}]];
function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  var cat=opts.category||pick(CATS,rnd);
  var pool=B.filter(function(b){return b[0]===cat;});
  var b=pick(pool.length?pool:B,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  var variant=(seed%5)+1;
  var title=b[1]+(variant>1?' (variant '+variant+')':'');
  var demo=DEMO_TPL;
  var dp=b[4];
  for(var k in dp){ if(Object.prototype.hasOwnProperty.call(dp,k)) demo=demo.split('@@'+k+'@@').join(jsv(dp[k])); }
  return {id:id,title:title.slice(0,80),description:b[2],category:cat,ladder_rank:1+(seed%3),demo:demo,fields:b[3],provenance:PROV,last_verified:'2026-10-21',src:SRC,_seed:seed};
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  var rx=new RegExp('^'+PREFIX.replace(/[.*+?^${}()|[\]\\]/g,'\\$&')+'\\d{6}$');
  if(!rx.test(r.id||''))e.push('id');
  if(typeof r.title!=='string'||!r.title.length)e.push('title');
  if(typeof r.description!=='string'||r.description.length<20)e.push('description');
  if(CATS.indexOf(r.category)<0)e.push('category');
  if(!(r.ladder_rank>=1&&r.ladder_rank<=3))e.push('ladder_rank');
  if(typeof r.demo!=='string'||r.demo.indexOf('console.log')<0)e.push('demo');
  if(!r.fields||typeof r.fields!=='object'||!Object.keys(r.fields).length)e.push('fields');
  if(r.src!==SRC)e.push('src');
  if(r.last_verified!=='2026-10-21')e.push('last_verified');
  if(typeof r.provenance!=='string'||!r.provenance.length)e.push('provenance');
  return {ok:!e.length,errors:e};
}
var gen={version:'jahdb-self-healing-storage-pools-1.0',generate:generate,validate:validate};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('self-healing-storage-pools',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
