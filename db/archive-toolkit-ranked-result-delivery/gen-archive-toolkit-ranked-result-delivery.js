(function(){'use strict';
var PREFIX="JAH-ATK205-";
var METHODS=[["Declared ranking criteria", "Publish the criteria and weights used for every ranking so ordering is auditable, not magic."], ["Multi-signal scoring", "Combine text relevance, freshness, authority, and usage signals into one score with explicit weights."], ["Learning-to-rank models", "Train a ranking model on judged query-result pairs and version the model with each retrain."], ["Pairwise preference labels", "Collect 'A beats B' judgments from experts and train rankers on pairs rather than absolute scores."], ["Position-bias correction", "Correct click-based training data for the fact that top results get clicked because they are on top."], ["Freshness decay", "Apply time decay to scores so breaking developments outrank stale evergreen content when recency matters."], ["Authority weighting", "Weight sources by measured reliability so well-sourced results outrank plausible-sounding unknowns."], ["Personalized re-ranking", "Adjust the base ranking with the caller's history and role without letting personalization override hard constraints."], ["Tiered ranking", "Rank in stages: cheap recall filter, mid-cost scorer, expensive re-ranker on the top K \u2014 the standard cascade."], ["Score calibration", "Calibrate scores to probabilities so 'score 0.9' means the same thing across queries and over time."], ["Ranking explanations", "Attach a per-result explanation (top contributing signals) so humans can sanity-check the order."], ["A/B ranking experiments", "Serve variant rankings to cohorts and measure engagement and task success before promoting a new ranker."], ["Fairness constraints", "Enforce exposure floors so no source class is systematically buried by the ranker."], ["Diversified re-ranking", "Apply MMR or xQuAD on top of relevance ranking so the top ten cover the question's facets."], ["Ranking audit logs", "Log every ranked response with criteria version and scores so any ordering can be replayed and defended."]];
var CATS=["ranking", "scoring", "relevance"];
var DEMO="# Ranked Result Delivery demo: declared criteria, multi-signal scoring, explanations.\nDOCS=[{\"id\":\"d1\",\"text\":\"solar sail propulsion photon pressure\",\"fresh\":2,\"auth\":0.9},\n      {\"id\":\"d2\",\"text\":\"solar panels sail boats\",\"fresh\":90,\"auth\":0.5},\n      {\"id\":\"d3\",\"text\":\"photon propulsion sails for deep space probes\",\"fresh\":10,\"auth\":0.8}]\nW={\"rel\":0.6,\"fresh\":0.2,\"auth\":0.2}\ndef rel(q,d):\n    qt=set(q.split()); dt=d[\"text\"].split()\n    return sum(dt.count(t) for t in qt)/max(1,len(dt))\ndef score(q,d):\n    r=rel(q,d); f=1.0/(1+d[\"fresh\"]/30.0); a=d[\"auth\"]\n    s=W[\"rel\"]*r+W[\"fresh\"]*f+W[\"auth\"]*a\n    return s,{\"relevance\":round(r,3),\"freshness\":round(f,3),\"authority\":a}\nq=\"solar sail propulsion\"\nfor d in sorted(DOCS,key=lambda d:-score(q,d)[0]):\n    s,exp=score(q,d); print(d[\"id\"],round(s,3),exp)\nprint(\"criteria weights:\",W)\n";
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function generate(seed,opts){
  opts=opts||{};var rnd=prng(seed);
  var idx=(seed-1)%METHODS.length;var m=METHODS[idx];
  var cat=opts.category||CATS[(rnd()*CATS.length)|0];
  var id=PREFIX+String(1000+((seed-1)%9000));
  var title=m[0]+' \u2014 '+"Ranked Result Delivery";
  return {id:id,t:title,title:title,description:"Ranked result delivery turns an unordered candidate set into a defensible ordering. Every position in the ranking is produced by declared criteria \u2014 relevance, freshness, authority, diversity \u2014 combined through a transparent scoring function, and the criteria travel with the results so consumers can audit why item three beat item four. Good ranking is what separates a search engine from a grep: it",
    kind:"retrieval tool",category:cat,ladder_rank:1+((seed-1)%3),demo:DEMO,
    provenance:"Public-harvest",last_verified:'2026-10-21',src:"public-harvest",_seed:seed};
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(typeof r.id!=='string'||r.id.indexOf(PREFIX)!==0)e.push('id');
  if(typeof r.title!=='string'||!r.title.length)e.push('title');
  if(typeof r.description!=='string'||r.description.length<100)e.push('description');
  if(CATS.indexOf(r.category)<0)e.push('category');
  if(!(r.ladder_rank>=1&&r.ladder_rank<=3))e.push('ladder_rank');
  if(typeof r.demo!=='string'||r.demo.indexOf('print(')<0)e.push('demo');
  if(r.src!=="public-harvest")e.push('src');
  return {ok:!e.length,errors:e};
}
var gen={version:"jahdb-archive-toolkit-ranked-result-delivery-1.0",generate:generate,validate:validate};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("archive-toolkit-ranked-result-delivery",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();