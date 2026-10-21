(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];} function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var CATS=["cft", "bft", "blockchain", "systems", "theory"];
var PREFIX='JAH-DISTRI4-S-';
var GENVER='jahdb-distributed-consensus-signature-1.0';
var SRC='signature-generated-completion';
var EDITION='signature';
var PROV="Signature-original completion authored for the JAH Databases network; clearly labeled Signature, never presented as public record.";
var FIELDS=["algorithm", "tolerates", "rounds", "use"];
var DEMO_TPL="// $TITLE - leader election demo (3 nodes)\nvar nodes = [{ id: 1, term: 1 }, { id: 2, term: 1 }, { id: 3, term: 2 }];\nvar votes = {};\nnodes.forEach(function(n) { votes[n.id] = 0; });\nnodes.forEach(function(voter) {\n  var cand = nodes.reduce(function(a, b) { return (b.term > a.term || (b.term === a.term && b.id > a.id)) ? b : a; });\n  votes[cand.id]++;\n});\nvar leader = Object.keys(votes).reduce(function(a, b) { return votes[a] >= votes[b] ? a : b; });\nconsole.log(\"Algorithm: $ALGORITHM | Tolerates: $TOLERATES\");\nconsole.log(\"Votes: \" + JSON.stringify(votes));\nconsole.log(\"Leader elected: node \" + leader + \" with \" + votes[leader] + \"/3 votes -> QUORUM PASS\");";
function jsEsc(s){return String(s).replace(/\\/g,'\\\\').replace(/"/g,'\\"').replace(/\n/g,'\\n').replace(/\r/g,'\\r').replace(/\t/g,'\\t');}
function fillTpl(tpl,vars){return tpl.replace(/\$([A-Za-z0-9_]+)/g,function(m,k){return Object.prototype.hasOwnProperty.call(vars,k)?jsEsc(vars[k]):m;});}
/* rows: [category, title, description, {fields}] */
var B=[["cft", "SigRaft", "Signature-original: Raft with pre-vote and joint-consensus membership baked in. Tolerates f crash (2f+1); typical rounds: election + append. Used in: Sig clusters.", {"algorithm": "SigRaft", "tolerates": "f crash (2f+1)", "rounds": "election + append", "use": "Sig clusters"}], ["bft", "SigBFT", "Signature-original: chained BFT with threshold signatures aggregating votes. Tolerates f Byzantine (3f+1); typical rounds: 3 chained. Used in: Sig ledger.", {"algorithm": "SigBFT", "tolerates": "f Byzantine (3f+1)", "rounds": "3 chained", "use": "Sig ledger"}], ["systems", "SigMesh-Vote", "Signature-original: gossip-based membership voting for mesh clusters. Tolerates f crash; typical rounds: gossip rounds. Used in: SigMesh.", {"algorithm": "SigMesh-Vote", "tolerates": "f crash", "rounds": "gossip rounds", "use": "SigMesh"}], ["cft", "SigLease", "Signature-original: lease-based leadership with clock-bounded failover. Tolerates f crash; typical rounds: lease renew. Used in: Sig services.", {"algorithm": "SigLease", "tolerates": "f crash", "rounds": "lease renew", "use": "Sig services"}], ["bft", "SigEpoch", "Signature-original: epoch-based BFT with rotating proposers and slashing. Tolerates f Byzantine; typical rounds: epoch phases. Used in: Sig chain.", {"algorithm": "SigEpoch", "tolerates": "f Byzantine", "rounds": "epoch phases", "use": "Sig chain"}], ["systems", "SigWitness", "Signature-original: witness replicas voting without storing full data. Tolerates f crash; typical rounds: witness rounds. Used in: tie-breakers.", {"algorithm": "SigWitness", "tolerates": "f crash", "rounds": "witness rounds", "use": "tie-breakers"}], ["cft", "SigFast-Path", "Signature-original: single-round fast path when the leader is stable. Tolerates f crash; typical rounds: 1 fast / 2 slow. Used in: low-latency writes.", {"algorithm": "SigFast", "tolerates": "f crash", "rounds": "1 fast / 2 slow", "use": "low-latency writes"}], ["cft", "SigGeo", "Signature-original: geo-aware quorum placement minimizing cross-region rounds. Tolerates f crash per region; typical rounds: local + global. Used in: multi-region.", {"algorithm": "SigGeo", "tolerates": "f crash per region", "rounds": "local + global", "use": "multi-region"}], ["theory", "SigLearn", "Signature-original: learned failure detectors cutting false leader elections. Tolerates crash (adaptive); typical rounds: adaptive. Used in: all Sig consensus.", {"algorithm": "SigLearn-FD", "tolerates": "crash (adaptive)", "rounds": "adaptive", "use": "all Sig consensus"}], ["systems", "SigSnap-Log", "Signature-original: log compaction with verifiable snapshots per term. Tolerates f crash; typical rounds: snapshot rounds. Used in: Sig logs.", {"algorithm": "SigSnap-Log", "tolerates": "f crash", "rounds": "snapshot rounds", "use": "Sig logs"}], ["systems", "SigReconfig", "Signature-original: single-round reconfiguration with versioned quorums. Tolerates f crash; typical rounds: 1 round. Used in: elastic clusters.", {"algorithm": "SigReconfig", "tolerates": "f crash", "rounds": "1 round", "use": "elastic clusters"}], ["theory", "SigClock", "Signature-original: hybrid logical clocks giving total order without TrueTime hardware. Tolerates clock skew bounded; typical rounds: n/a. Used in: ordering.", {"algorithm": "SigClock", "tolerates": "clock skew bounded", "rounds": "n/a", "use": "ordering"}], ["systems", "SigAudit-Log", "Signature-original: tamper-evident replicated logs with per-entry proofs. Tolerates f crash + 1 liar; typical rounds: chained. Used in: compliance logs.", {"algorithm": "SigAudit-Log", "tolerates": "f crash + 1 liar", "rounds": "chained", "use": "compliance logs"}], ["systems", "SigEdge-Quorum", "Signature-original: edge quorums with hierarchical aggregation to the core. Tolerates f crash per tier; typical rounds: tiered. Used in: edge clusters.", {"algorithm": "SigEdge-Quorum", "tolerates": "f crash per tier", "rounds": "tiered", "use": "edge clusters"}], ["theory", "SigConsensus-One", "Signature-original: the united consensus plane — pick CFT or BFT per workload. Tolerates configurable; typical rounds: adaptive. Used in: everything.", {"algorithm": "SigConsensus-One", "tolerates": "configurable", "rounds": "adaptive", "use": "everything"}]];
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
  if(!new RegExp('^'+'JAH\\-DISTRI4\\-S\\-'+'\\d{6}$').test(r.id||''))e.push('id');
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('distributed-consensus-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
