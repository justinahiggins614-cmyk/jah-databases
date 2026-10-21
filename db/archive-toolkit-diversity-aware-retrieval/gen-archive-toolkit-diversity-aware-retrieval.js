(function(){'use strict';
var PREFIX="JAH-ATK206-";
var METHODS=[["Maximal Marginal Relevance", "Greedily pick each next result to maximize relevance minus similarity to already-picked results, with a tunable lambda."], ["Subtopic coverage quotas", "Require the top K to cover at least M detected subtopics, filling gaps before adding more of the same."], ["Source-type balancing", "Cap how many results may come from one source type (blog, paper, manual) so the mix reflects the archive's breadth."], ["Viewpoint detection", "Cluster results by stance and ensure minority viewpoints appear when the question is contested."], ["Near-duplicate suppression", "Collapse result pairs above a similarity threshold before ranking so copies never occupy two slots."], ["Temporal spread", "Ensure results span the time range of the archive instead of clustering on the most recent year."], ["Geographic spread", "For location-sensitive questions, require coverage across regions rather than one country's sources."], ["Format diversity", "Mix text, tables, images, and video results when the archive holds multiple formats on the topic."], ["Author diversity", "Limit results per author so one prolific writer cannot dominate the answer set."], ["Facet-aware reranking", "Detect the question's facets (cost, safety, performance) and reserve slots for each facet's best result."], ["Novelty boosting", "Boost results containing information absent from higher-ranked results, measured by n-gram novelty."], ["Serendipity injection", "Reserve a small slot budget for high-quality tangentially related results that broaden the caller's view."], ["Diversity metrics", "Measure coverage (alpha-nDCG, ERR-IA) so diversity is a number that can be regressed, not a vibe."], ["User-controlled tradeoff", "Expose the relevance/diversity lambda to the caller so applications choose their own balance."], ["Post-hoc diversity audit", "After delivery, report the source-type and subtopic distribution so consumers can see what was covered."]];
var CATS=["ranking", "diversity", "coverage"];
var DEMO="# Diversity-Aware Retrieval demo: MMR greedy selection over toy candidates.\nimport math\nCANDS=[{\"id\":\"c1\",\"rel\":0.95,\"vec\":[1.0,0.1]},{\"id\":\"c2\",\"rel\":0.93,\"vec\":[0.95,0.12]},\n       {\"id\":\"c3\",\"rel\":0.80,\"vec\":[0.1,1.0]},{\"id\":\"c4\",\"rel\":0.75,\"vec\":[0.0,0.9]},\n       {\"id\":\"c5\",\"rel\":0.70,\"vec\":[-0.8,0.6]}]\ndef sim(a,b):\n    dot=sum(x*y for x,y in zip(a,b)); na=math.hypot(*a); nb=math.hypot(*b)\n    return dot/(na*nb)\ndef mmr(cands,k,lam=0.6):\n    sel=[]; rest=cands[:]\n    while rest and len(sel)<k:\n        best=max(rest,key=lambda c: lam*c[\"rel\"]-(1-lam)*max([sim(c[\"vec\"],s[\"vec\"]) for s in sel] or [0]))\n        sel.append(best); rest.remove(best)\n    return sel\nprint([c[\"id\"] for c in mmr(CANDS,3)])\n";
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function generate(seed,opts){
  opts=opts||{};var rnd=prng(seed);
  var idx=(seed-1)%METHODS.length;var m=METHODS[idx];
  var cat=opts.category||CATS[(rnd()*CATS.length)|0];
  var id=PREFIX+String(1000+((seed-1)%9000));
  var title=m[0]+' \u2014 '+"Diversity-Aware Retrieval";
  return {id:id,t:title,title:title,description:"Diversity-aware retrieval fights the echo problem: without it, the top results are often ten near-identical copies of the same fact from the same kind of source. The technique balances relevance against coverage \u2014 across sources, viewpoints, document types, and subtopics \u2014 so the caller sees the shape of the answer space, not just its loudest corner. Maximal Marginal Relevance and its descendants ",
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
var gen={version:"jahdb-archive-toolkit-diversity-aware-retrieval-1.0",generate:generate,validate:validate};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("archive-toolkit-diversity-aware-retrieval",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();