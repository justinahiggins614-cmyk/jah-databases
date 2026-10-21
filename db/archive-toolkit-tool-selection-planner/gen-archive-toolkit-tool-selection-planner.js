(function(){'use strict';
var PREFIX="JAH-ATK243-";
var METHODS=[["Requirement extraction", "Turn the task description into structured requirements: verbs, data types, constraints."], ["Candidate retrieval", "Pull candidate tools from the registry by capability match before scoring."], ["Multi-criteria scoring", "Score candidates on fit, cost, latency, reliability, and policy compliance with explicit weights."], ["Policy filtering", "Eliminate tools the caller's identity, region, or data classification forbids before scoring."], ["Cost estimation", "Estimate the call's cost from declared pricing and historical usage before selecting."], ["Reliability weighting", "Weight by measured success rates, down-weighting tools that fail often on this task class."], ["Explanation generation", "Produce a human-readable rationale: why this tool, what the runners-up lacked."], ["Fallback ordering", "Return a ranked list, not just the winner, so the executor can fall back gracefully."], ["Learning from outcomes", "Record which selections succeeded and adjust future scores accordingly."], ["Constraint satisfaction", "Treat hard requirements (must run offline, must be free) as filters, never as soft scores."], ["Human-in-the-loop selection", "Escalate to a human when the top candidates are close or the stakes are high."], ["Batch selection", "Select tool sets for multi-step tasks jointly, preferring combinations known to compose well."], ["Cold-start heuristics", "When no history exists, prefer simple, well-documented tools with broad capabilities."], ["Selection auditing", "Log every selection with inputs, candidates, and scores for later review."], ["A/B selection experiments", "Test new selection strategies on a traffic slice before promoting them."]];
var CATS=["planning", "tools", "selection"];
var DEMO="# Tool Selection Planner demo: requirement match -> policy filter -> scored pick.\nTOOLS={\"t-translate\":{\"verbs\":[\"translate\"],\"cost\":2,\"rel\":0.98,\"offline\":False},\n       \"t-local\":{\"verbs\":[\"translate\"],\"cost\":0,\"rel\":0.85,\"offline\":True},\n       \"t-summarize\":{\"verbs\":[\"summarize\"],\"cost\":1,\"rel\":0.97,\"offline\":True}}\ndef select(verbs,policy):\n    cands=[]\n    for name,t in TOOLS.items():\n        if not set(verbs)<=set(t[\"verbs\"]): continue\n        if policy.get(\"offline\") and not t[\"offline\"]: continue\n        score=0.6*t[\"rel\"]-0.1*t[\"cost\"]+(0.2 if t[\"offline\"] and policy.get(\"offline\") else 0)\n        cands.append((round(score,3),name))\n    return sorted(cands,reverse=True)\nprint(select([\"translate\"],{\"offline\":True}))\nprint(select([\"translate\"],{}))\n";
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function generate(seed,opts){
  opts=opts||{};var rnd=prng(seed);
  var idx=(seed-1)%METHODS.length;var m=METHODS[idx];
  var cat=opts.category||CATS[(rnd()*CATS.length)|0];
  var id=PREFIX+String(1000+((seed-1)%9000));
  var title=m[0]+' \u2014 '+"Tool Selection Planner";
  return {id:id,t:title,title:title,description:"The tool selection planner chooses the right tool for each task from the registry: it matches the task's requirements against registered capabilities, scores candidates on fit, cost, reliability, and policy, and explains its choice. Good selection is the difference between an agent that flails through five wrong tools and one that does the job in a single confident call. The planner learns from ou",
    kind:"execution tool",category:cat,ladder_rank:1+((seed-1)%3),demo:DEMO,
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
var gen={version:"jahdb-archive-toolkit-tool-selection-planner-1.0",generate:generate,validate:validate};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("archive-toolkit-tool-selection-planner",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();