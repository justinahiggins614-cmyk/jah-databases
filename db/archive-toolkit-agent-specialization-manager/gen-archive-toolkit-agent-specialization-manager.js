(function(){'use strict';
var PREFIX="JAH-ATK247-";
var METHODS=[["Expertise profiling", "Profile each agent's domains, tools, and languages from declared skills and measured outcomes."], ["Task requirement analysis", "Extract the expertise a task needs from its description and history of similar tasks."], ["Match scoring", "Score agent-task fit and route to the best fit above a competence threshold."], ["Competence thresholds", "Refuse to assign tasks below a minimum fit; better to queue than to botch."], ["Load-aware routing", "Balance best-fit against current load so the top expert is not drowned."], ["Mentored assignments", "Pair a developing agent with an expert on stretch tasks to grow new specialists."], ["Performance tracking", "Track per-agent, per-domain success rates as the ground truth of expertise."], ["Specialization decay", "Decay expertise scores without recent practice; skills atrophy."], ["Cross-training", "Deliberately route some tasks off-specialty to build bench depth."], ["Expert escalation", "Escalate to deeper experts when the assigned agent's confidence is low."], ["Team composition", "Assemble multi-agent teams whose combined expertise covers the whole task."], ["Expertise discovery", "Detect emerging expertise from success patterns, not just self-declared skills."], ["Fairness in routing", "Spread desirable tasks so development opportunities are not hoarded by top agents."], ["Specialization registry", "Publish who is expert at what so humans and planners can choose directly."], ["Routing audits", "Review routing decisions for bias toward familiar agents over better-fitting ones."]];
var CATS=["agents", "routing", "expertise"];
var DEMO="# Agent Specialization Manager demo: profile match scoring with load awareness.\nAGENTS={\"a1\":{\"domains\":{\"translation\":0.9,\"summarization\":0.5},\"load\":2},\n        \"a2\":{\"domains\":{\"translation\":0.6,\"summarization\":0.95},\"load\":0},\n        \"a3\":{\"domains\":{\"translation\":0.7},\"load\":5}}\ndef route(task_domain):\n    scored=[]\n    for name,a in AGENTS.items():\n        fit=a[\"domains\"].get(task_domain,0)\n        if fit<0.5: continue\n        scored.append((round(fit-0.05*a[\"load\"],3),name,fit))\n    return sorted(scored,reverse=True)\nprint(\"translation task ->\",route(\"translation\"))\nprint(\"summarization task ->\",route(\"summarization\"))\n";
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function generate(seed,opts){
  opts=opts||{};var rnd=prng(seed);
  var idx=(seed-1)%METHODS.length;var m=METHODS[idx];
  var cat=opts.category||CATS[(rnd()*CATS.length)|0];
  var id=PREFIX+String(1000+((seed-1)%9000));
  var title=m[0]+' \u2014 '+"Agent Specialization Manager";
  return {id:id,t:title,title:title,description:"The agent specialization manager makes sure the right expert gets the job: it maintains profiles of what each agent is good at \u2014 domains, tools, languages, past performance \u2014 and routes tasks accordingly. A fleet of generalists is a fleet of mediocrity; specialization routing gets expert-quality work without expert staffing on every seat. The manager also grows specialists, tracking who is becomin",
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
var gen={version:"jahdb-archive-toolkit-agent-specialization-manager-1.0",generate:generate,validate:validate};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("archive-toolkit-agent-specialization-manager",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();