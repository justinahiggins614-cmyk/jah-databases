(function(){'use strict';
var PREFIX="JAH-ATK241-";
var METHODS=[["Capability schema", "Define a standard registration shape: verbs, inputs, outputs, preconditions, effects, cost, limits."], ["Semantic search", "Let planners find tools by describing the goal in words, matched against capability descriptions."], ["Versioned registrations", "Keep every tool version's registration so planners can pin or compare across versions."], ["Honest limit declarations", "Require declared limits (rate, size, accuracy) and verify them with benchmarks."], ["Deprecation lifecycle", "Mark tools as deprecated with sunset dates and recommended successors."], ["Access-scoped visibility", "Show each planner only the tools its identity is allowed to invoke."], ["Usage analytics", "Track which tools get selected and succeed, feeding back into ranking and registration quality."], ["Registration validation", "Test-register tools against their declared schema with synthetic calls before listing."], ["Composite capabilities", "Register tool chains as new composite capabilities with their own registrations."], ["Multi-tenant registries", "Maintain per-tenant views so different users see different tool universes."], ["Capability diffing", "Diff registrations across versions to catch silent capability changes."], ["Emergency delisting", "Delist a misbehaving tool instantly, with in-flight calls drained gracefully."], ["Registration provenance", "Record who registered each tool and what evidence backs its claims."], ["Cost-aware ranking", "Rank candidate tools by expected cost for the task, not just capability match."], ["Registry federation", "Federate registries across organizations with trust policies for foreign tools."]];
var CATS=["registry", "tools", "discovery"];
var DEMO="# Tool Capability Registry demo: register, semantic search, honest limits.\nREG={}\ndef register(name,verbs,inputs,outputs,limits):\n    REG[name]={\"verbs\":verbs,\"inputs\":inputs,\"outputs\":outputs,\"limits\":limits}\ndef find(goal_words):\n    out=[]\n    for name,r in REG.items():\n        score=sum(1 for w in goal_words if w in (\" \".join(r[\"verbs\"])+\" \"+r[\"outputs\"]).lower())\n        if score: out.append((score,name,r[\"limits\"]))\n    return sorted(out,reverse=True)\nregister(\"translator\",[\"translate\"],\"text\",\"text\",{\"max_chars\":5000})\nregister(\"summarizer\",[\"summarize\"],\"text\",\"summary\",{\"max_chars\":20000})\nprint(find([\"translate\",\"text\"]))\n";
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function generate(seed,opts){
  opts=opts||{};var rnd=prng(seed);
  var idx=(seed-1)%METHODS.length;var m=METHODS[idx];
  var cat=opts.category||CATS[(rnd()*CATS.length)|0];
  var id=PREFIX+String(1000+((seed-1)%9000));
  var title=m[0]+' \u2014 '+"Tool Capability Registry";
  return {id:id,t:title,title:title,description:"The tool capability registry is the yellow pages for the AI's toolbox: a searchable catalog describing what each available tool can do \u2014 its verbs, inputs, outputs, costs, and limits. Planners consult it instead of hardcoding tool knowledge, so adding a new tool is a registration, not a code change. Good registrations are honest about limits; a registry full of exaggeration is worse than none.",
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
var gen={version:"jahdb-archive-toolkit-tool-capability-registry-1.0",generate:generate,validate:validate};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("archive-toolkit-tool-capability-registry",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();