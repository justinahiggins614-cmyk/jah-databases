(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["retrieval", "reasoning", "ranking", "assignment", "verification"];
var PREFIX='JAH-UTC-S-';
var USE="Used by agent orchestrators, marketplaces, and workforce platforms to route work well.";
var FLD=[["method", "Method"], ["signal", "Signal"], ["ranking", "Ranking"]];
var DEMO="# {title} - match coverage (python3)\nmatched={d1}\nrequired={d2}\nmin_pct={d3}\npct=100.0*matched/required\nprint(\"capabilities matched: %d/%d (%.0f%%)\" % (matched, required, pct))\nprint(\"TASK COVERED\" if pct >= min_pct else \"GAPS REMAIN\")\n";
var SIG=true;
var SRC="signature-generated-completion";
var B=[["retrieval", "Capability Vector Similarity", "Embeds task needs and capability offers, matching by cosine similarity.", "Capability Vector Similarity", "embeddings", "similarity score", "8", "10", "70.0"], ["reasoning", "Skill Graph Traversal", "Walks a skill ontology from the task to capabilities that satisfy it.", "Skill Graph Traversal", "graph", "path length", "7", "10", "60.0"], ["ranking", "Ontology Subsumption", "Uses class hierarchies: a capability for a superclass satisfies subclass tasks.", "Ontology Subsumption", "taxonomy", "subsumption", "6", "8", "70.0"], ["assignment", "Embedding Retrieval", "Retrieves candidate capabilities with vector search, then reranks.", "Embedding Retrieval", "vectors", "two-stage score", "9", "10", "75.0"], ["verification", "Rule-based Filter", "Applies hard rules (certifications, regions) before any soft ranking.", "Rule-based Filter", "rules", "pass/fail", "10", "10", "100.0"], ["retrieval", "Constraint Solver", "Solves task requirements as constraints over capability attributes.", "Constraint Solver", "constraints", "feasibility", "7", "9", "70.0"], ["reasoning", "Auction Bidding", "Capabilities bid on tasks; the best value bid wins.", "Auction Bidding", "bids", "price-quality", "6", "8", "60.0"], ["ranking", "Reputation Weighting", "Weights matches by historical success rates of the capability.", "Reputation Weighting", "history", "trust score", "8", "10", "70.0"], ["assignment", "Cost-aware Ranking", "Ranks feasible matches by total cost including latency and fees.", "Cost-aware Ranking", "cost model", "total cost", "7", "10", "65.0"], ["verification", "Latency-aware Ranking", "Prefers matches that meet the task's deadline with margin.", "Latency-aware Ranking", "latency", "slack time", "8", "10", "70.0"], ["retrieval", "Provenance Filter", "Requires capabilities with auditable provenance for regulated tasks.", "Provenance Filter", "lineage", "compliance", "9", "10", "90.0"], ["reasoning", "Version Compatibility", "Checks capability versions against the task's required API surface.", "Version Compatibility", "versions", "compatible", "10", "10", "100.0"], ["ranking", "Certification Check", "Requires current certifications for safety-critical tasks.", "Certification Check", "certs", "valid certs", "8", "8", "100.0"], ["assignment", "Load-aware Assignment", "Skips overloaded capabilities even if they are the best match.", "Load-aware Assignment", "load", "headroom", "7", "10", "60.0"], ["verification", "Fairness Rotation", "Rotates among qualified capabilities to avoid winner-take-all.", "Fairness Rotation", "rotation", "fair share", "6", "9", "55.0"], ["retrieval", "Ensemble Scoring", "Combines several matchers with learned weights for robust ranking.", "Ensemble Scoring", "ensemble", "blended score", "9", "10", "75.0"], ["reasoning", "Human Confirmation Gate", "Requires human approval for high-stakes matches.", "Human Confirmation Gate", "oversight", "approved", "5", "5", "100.0"], ["ranking", "Fallback Candidate List", "Always returns ranked alternates so failure has a next option.", "Fallback Candidate List", "redundancy", "ranked list", "8", "10", "70.0"], ["assignment", "Negative Capability Exclusion", "Excludes capabilities known to fail this task class.", "Negative Capability Exclusion", "blocklist", "excluded", "4", "5", "80.0"], ["verification", "Continuous Re-matching", "Re-evaluates matches as capabilities and task state change.", "Continuous Re-matching", "streaming", "freshness", "7", "10", "65.0"]];
function buildTitle(b){ return SIG?('Signature '+b[1]):b[1]; }
function buildDesc(b){
  var d=b[2]+' Recorded facts \u2014 '+FLD[0][1]+': '+b[3]+'; '+FLD[1][1]+': '+b[4]+'; '+FLD[2][1]+': '+b[5]+'. '+USE;
  if(SIG) d='Signature-original: '+d+' Built as a Signature-authored original for the JAH network; clearly labeled Signature and never presented as a public record.';
  return d;
}
function buildDemo(b){
  return DEMO.split('{title}').join(b[1]).split('{d1}').join(b[6]).split('{d2}').join(b[7]).split('{d3}').join(b[8]);
}
function generate(seed,opts){
  opts=opts||{}; var rnd=prng(seed);
  var cat=opts.category||pick(CATS,rnd);
  var pool=B.filter(function(b){return b[0]===cat;});
  var b=pick(pool.length?pool:B,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  var title=buildTitle(b);
  var fields={}; fields[FLD[0][0]]=b[3]; fields[FLD[1][0]]=b[4]; fields[FLD[2][0]]=b[5];
  if(SIG) fields['signature_label']='Signature-authored original';
  return {id:id,title:title,description:buildDesc(b),category:cat,fields:fields,
    ladder_rank:1+(seed%3),
    demo:'# '+title+' \u2014 runnable demo (python3)\n'+buildDemo(b),
    provenance:'JAH Databases \u00b7 lane N3 build',last_verified:'2026-10-21',src:SRC,_seed:seed};
}
function driftCheck(rec,sample){
  sample=sample||[];
  for(var i=0;i<sample.length;i++){
    if(sample[i]&&sample[i].title===rec.title&&sample[i].category===rec.category)
      return {ok:false,errors:['duplicate of archive record '+sample[i].id]};
  }
  return {ok:true,errors:[]};
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  var idre=new RegExp('^'+PREFIX.replace(/[.*+?^${}()|[\]\\]/g,'\\$&')+'\\d{6}$');
  if(!idre.test(r.id||''))e.push('id');
  if(typeof r.title!=='string'||!r.title.length)e.push('title');
  if(typeof r.description!=='string'||r.description.length<40)e.push('description');
  if(CATS.indexOf(r.category)<0)e.push('category');
  if(!(r.ladder_rank>=1&&r.ladder_rank<=3))e.push('ladder_rank');
  if(typeof r.demo!=='string'||r.demo.indexOf('print(')<0)e.push('demo');
  if(['public-harvest','signature-generated-completion'].indexOf(r.src)<0)e.push('src');
  if(r.last_verified!=='2026-10-21')e.push('last_verified');
  return {ok:!e.length,errors:e};
}
var gen={version:'jahdb-universal-task-capability-matching-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('universal-task-capability-matching-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
