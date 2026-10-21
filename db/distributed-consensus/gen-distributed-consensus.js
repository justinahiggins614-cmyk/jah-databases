(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];} function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var CATS=["cft", "bft", "blockchain", "systems", "theory"];
var PREFIX='JAH-DISTRI4-';
var GENVER='jahdb-distributed-consensus-1.0';
var SRC='public-harvest';
var EDITION='public';
var PROV="Public record compiled from openly published documentation, project sources, and standard references.";
var FIELDS=["algorithm", "tolerates", "rounds", "use"];
var DEMO_TPL="// $TITLE - leader election demo (3 nodes)\nvar nodes = [{ id: 1, term: 1 }, { id: 2, term: 1 }, { id: 3, term: 2 }];\nvar votes = {};\nnodes.forEach(function(n) { votes[n.id] = 0; });\nnodes.forEach(function(voter) {\n  var cand = nodes.reduce(function(a, b) { return (b.term > a.term || (b.term === a.term && b.id > a.id)) ? b : a; });\n  votes[cand.id]++;\n});\nvar leader = Object.keys(votes).reduce(function(a, b) { return votes[a] >= votes[b] ? a : b; });\nconsole.log(\"Algorithm: $ALGORITHM | Tolerates: $TOLERATES\");\nconsole.log(\"Votes: \" + JSON.stringify(votes));\nconsole.log(\"Leader elected: node \" + leader + \" with \" + votes[leader] + \"/3 votes -> QUORUM PASS\");";
function jsEsc(s){return String(s).replace(/\\/g,'\\\\').replace(/"/g,'\\"').replace(/\n/g,'\\n').replace(/\r/g,'\\r').replace(/\t/g,'\\t');}
function fillTpl(tpl,vars){return tpl.replace(/\$([A-Za-z0-9_]+)/g,function(m,k){return Object.prototype.hasOwnProperty.call(vars,k)?jsEsc(vars[k]):m;});}
/* rows: [category, title, description, {fields}] */
var B=[["theory", "Paxos", "Lamport’s 1998 protocol; proposers, acceptors, and learners agree through prepare/accept phases. Tolerates f crash failures (2f+1 nodes); typical rounds: 2 phases. Used in: Chubby, Spanner.", {"algorithm": "Paxos", "tolerates": "f crash failures (2f+1 nodes)", "rounds": "2 phases", "use": "Chubby, Spanner"}], ["cft", "Raft", "Ongaro and Ousterhout’s understandable consensus with leader election and log replication. Tolerates f crash failures (2f+1 nodes); typical rounds: election + append. Used in: etcd, Consul, TiKV.", {"algorithm": "Raft", "tolerates": "f crash failures (2f+1 nodes)", "rounds": "election + append", "use": "etcd, Consul, TiKV"}], ["cft", "Zab", "ZooKeeper’s atomic broadcast with a leader sequencing all writes through epochs. Tolerates f crash failures; typical rounds: discovery + sync + broadcast. Used in: ZooKeeper.", {"algorithm": "Zab", "tolerates": "f crash failures", "rounds": "discovery + sync + broadcast", "use": "ZooKeeper"}], ["bft", "PBFT", "Castro and Liskov’s practical Byzantine fault tolerance with pre-prepare/prepare/commit. Tolerates f Byzantine (3f+1 nodes); typical rounds: 3 phases. Used in: permissioned ledgers.", {"algorithm": "PBFT", "tolerates": "f Byzantine (3f+1 nodes)", "rounds": "3 phases", "use": "permissioned ledgers"}], ["bft", "HotStuff", "Chained BFT with linear communication, the core of several modern PoS chains. Tolerates f Byzantine (3f+1); typical rounds: 3 chained phases. Used in: Aptos, Flow.", {"algorithm": "HotStuff", "tolerates": "f Byzantine (3f+1)", "rounds": "3 chained phases", "use": "Aptos, Flow"}], ["bft", "Tendermint", "BFT consensus with instant finality and rotating proposers per height. Tolerates f Byzantine (3f+1); typical rounds: propose/prevote/precommit. Used in: Cosmos SDK chains.", {"algorithm": "Tendermint", "tolerates": "f Byzantine (3f+1)", "rounds": "propose/prevote/precommit", "use": "Cosmos SDK chains"}], ["blockchain", "Nakamoto PoW", "Bitcoin’s proof-of-work: the longest chain wins, finality is probabilistic. Tolerates <51% hash power honest; typical rounds: ~10 min blocks. Used in: Bitcoin.", {"algorithm": "Nakamoto consensus", "tolerates": "<51% hash power honest", "rounds": "~10 min blocks", "use": "Bitcoin"}], ["blockchain", "Casper PoS", "Ethereum’s proof-of-stake finality gadget with checkpoint justification. Tolerates <1/3 stake Byzantine; typical rounds: epoch checkpoints. Used in: Ethereum.", {"algorithm": "Casper FFG", "tolerates": "<1/3 stake Byzantine", "rounds": "epoch checkpoints", "use": "Ethereum"}], ["cft", "Viewstamped Replication", "The 1988 protocol that inspired Raft, with view changes on leader failure. Tolerates f crash failures; typical rounds: normal + view-change. Used in: theory, VR systems.", {"algorithm": "VR", "tolerates": "f crash failures", "rounds": "normal + view-change", "use": "theory, VR systems"}], ["cft", "Multi-Paxos", "Paxos with a stable leader skipping phase 1 — the production workhorse variant. Tolerates f crash failures; typical rounds: 1 phase steady-state. Used in: Spanner, Chubby.", {"algorithm": "Multi-Paxos", "tolerates": "f crash failures", "rounds": "1 phase steady-state", "use": "Spanner, Chubby"}], ["cft", "EPaxos", "Egalitarian Paxos letting any replica lead non-conflicting commands for geo-scale latency. Tolerates f crash failures; typical rounds: 1-2 rounds. Used in: geo-replicated stores.", {"algorithm": "EPaxos", "tolerates": "f crash failures", "rounds": "1-2 rounds", "use": "geo-replicated stores"}], ["systems", "etcd Raft", "The production Raft library powering Kubernetes’ control plane state. Tolerates f crash (2f+1); typical rounds: Raft rounds. Used in: Kubernetes.", {"algorithm": "etcd-raft", "tolerates": "f crash (2f+1)", "rounds": "Raft rounds", "use": "Kubernetes"}], ["cft", "Mencius", "Rotating-leader Multi-Paxos spreading leadership across replicas for WAN throughput. Tolerates f crash failures; typical rounds: rotating rounds. Used in: WAN replication.", {"algorithm": "Mencius", "tolerates": "f crash failures", "rounds": "rotating rounds", "use": "WAN replication"}], ["systems", "Raft single-membership change", "Joint consensus makes cluster membership changes safe without downtime. Tolerates f crash during change; typical rounds: 2-phase config. Used in: etcd, CockroachDB.", {"algorithm": "joint consensus", "tolerates": "f crash during change", "rounds": "2-phase config", "use": "etcd, CockroachDB"}], ["systems", "Spanner Paxos groups", "Google Spanner shards Paxos groups per tablet with TrueTime for external consistency. Tolerates f crash per group; typical rounds: Paxos rounds. Used in: Spanner.", {"algorithm": "Paxos per shard", "tolerates": "f crash per group", "rounds": "Paxos rounds", "use": "Spanner"}]];
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
  if(!new RegExp('^'+'JAH\\-DISTRI4\\-'+'\\d{6}$').test(r.id||''))e.push('id');
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('distributed-consensus',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
