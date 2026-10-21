(function(){'use strict';
var PREFIX="JAH-ATK207S-";
var METHODS=[["Source concentration caps", "Limit any single source to at most X% of delivered results per query, configurable per collection."], ["Source health registry", "Track per-source availability, latency, and error rates; unhealthy sources are throttled automatically."], ["Publisher bias profiles", "Record measured lean or coverage gaps per publisher so the controller can compensate explicitly."], ["Alternative-source promotion", "When the cap binds, fill freed slots with the best results from underrepresented sources."], ["Source independence scoring", "Prefer sources that do not all cite each other, measured over the citation graph."], ["Primary-source preference", "For factual claims, prefer primary sources (original data, official records) over tertiary retellings."], ["Outage failover routing", "If a dominant source goes down, reroute its slot budget to healthy alternatives without caller changes."], ["Source freshness balancing", "Do not let one fast-updating source starve slower but authoritative ones of all exposure."], ["Paywall-aware mixing", "Balance open and paywalled sources so answers remain usable for callers without subscriptions."], ["Source audit trails", "Record which sources contributed to each answer so bias can be investigated after the fact."], ["Publisher allow/block lists", "Support explicit per-application source policies layered over the automatic caps."], ["Cross-source corroboration", "Require important claims to appear in at least two independent sources before the answer states them firmly."], ["Source onboarding vetting", "New sources start with a low cap that rises as their quality and independence are measured."], ["Concentration alerts", "Alert operators when a topic's results concentrate past a threshold, even if caps are technically satisfied."], ["Per-tenant source policy", "Let different applications set different source mixes over the same underlying archive."]];
var CATS=["sources", "policy", "reliability"];
var DEMO="# Source-Diversity Controller demo: concentration caps over a source registry.\nSRCS={\"pubA\":{\"share\":0.70,\"health\":1.0},\"pubB\":{\"share\":0.15,\"health\":1.0},\n      \"pubC\":{\"share\":0.10,\"health\":0.0},\"pubD\":{\"share\":0.05,\"health\":1.0}}\nRESULTS=[(\"r%d\"%i,\"pubA\") for i in range(14)]+[(\"r%d\"%i,\"pubB\") for i in range(14,17)]+[(\"r17\",\"pubD\")]\ndef control(results,cap=0.5):\n    counts={}; out=[]\n    for rid,src in results:\n        if SRCS[src][\"health\"]<=0: continue\n        if counts.get(src,0)>=cap*len(results): continue\n        counts[src]=counts.get(src,0)+1; out.append((rid,src))\n    return out,counts\nkept,counts=control(RESULTS)\nprint(\"kept\",len(kept),\"distribution\",counts)\n";
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function generate(seed,opts){
  opts=opts||{};var rnd=prng(seed);
  var idx=(seed-1)%METHODS.length;var m=METHODS[idx];
  var cat=opts.category||CATS[(rnd()*CATS.length)|0];
  var id=PREFIX+String(1000+((seed-1)%9000));
  var title=m[0]+' \u2014 '+"Source-Diversity Controller (Signature)";
  return {id:id,t:title,title:title,description:"Signature edition. The source-diversity controller is the policy layer above diversity-aware ranking: it decides, per query, how much trust to place in each source and caps concentration before ranking begins. When one publisher dominates a topic, the controller throttles it and promotes alternatives, protecting answers from single-source bias, publisher outages, and quiet capture of the record. It keeps a live sour",
    kind:"retrieval tool",category:cat,ladder_rank:1+((seed-1)%3),demo:DEMO,
    provenance:"Signature-generated-completion",last_verified:'2026-10-21',src:"signature-generated-completion",_seed:seed};
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
  if(r.src!=="signature-generated-completion")e.push('src');
  return {ok:!e.length,errors:e};
}
var gen={version:"jahdb-archive-toolkit-source-diversity-controller-signature-1.0",generate:generate,validate:validate};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("archive-toolkit-source-diversity-controller-signature",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();