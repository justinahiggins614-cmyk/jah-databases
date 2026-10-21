(function(){'use strict';
var PREFIX="JAH-ATK245-";
var METHODS=[["Rule-based branching", "Express next-step rules as readable conditions on the previous step's structured output."], ["Decision tables", "Capture complex routing in decision tables reviewers can audit without reading code."], ["Confidence-gated routes", "Route low-confidence results to verification and high-confidence ones straight through."], ["Error-class routing", "Map each error class to its own recovery route instead of one generic catch-all."], ["Loop constructs", "Support bounded retry loops with exit conditions and loop-carried state."], ["Parallel fan-out/fan-in", "Branch into parallel routes on a condition and join them with a defined merge policy."], ["Default routes", "Define explicit default routes so no outcome falls through silently."], ["Route testing", "Test every branch with synthetic step outputs to prove the router covers its space."], ["Execution tracing", "Record the exact path taken through the router for every run."], ["Rule versioning", "Version routing rules with the workflow so old runs remain replayable."], ["Human decision nodes", "Route genuinely ambiguous decisions to a human with the evidence summarized."], ["Cost-aware routing", "Prefer cheaper routes when outcomes are equivalent, and document the tradeoff."], ["Time-based routing", "Route differently by time of day, deadlines, or SLA pressure."], ["Learning routers", "Tune routing thresholds from historical outcomes while keeping rules readable."], ["Router composition", "Nest routers inside routers for hierarchical decision-making."]];
var CATS=["workflows", "routing", "decisions"];
var DEMO="# Conditional Workflow Router demo: outcome-driven branching with tracing.\ndef router(result):\n    trace=[]\n    if result[\"ok\"]:\n        trace.append(\"success\")\n        route=\"store\" if result[\"confidence\"]>0.8 else \"verify-then-store\"\n    elif result[\"error\"]==\"timeout\":\n        route=\"retry-with-backoff\"; trace.append(\"error:timeout\")\n    else:\n        route=\"escalate\"; trace.append(\"error:\"+result[\"error\"])\n    trace.append(\"route:\"+route); return route,trace\nfor r in [{\"ok\":True,\"confidence\":0.95},{\"ok\":True,\"confidence\":0.4},\n          {\"ok\":False,\"error\":\"timeout\"},{\"ok\":False,\"error\":\"auth\"}]:\n    print(router(r))\n";
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function generate(seed,opts){
  opts=opts||{};var rnd=prng(seed);
  var idx=(seed-1)%METHODS.length;var m=METHODS[idx];
  var cat=opts.category||CATS[(rnd()*CATS.length)|0];
  var id=PREFIX+String(1000+((seed-1)%9000));
  var title=m[0]+' \u2014 '+"Conditional Workflow Router";
  return {id:id,t:title,title:title,description:"The conditional workflow router makes pipelines smart: instead of a fixed chain, each step's outcome decides what runs next \u2014 success goes one way, a particular error goes another, a low-confidence result triggers verification. It is the difference between a script and a strategy. The router's rules are explicit, testable, and logged, so a workflow's path through the decision tree can be replayed ",
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
var gen={version:"jahdb-archive-toolkit-conditional-workflow-router-1.0",generate:generate,validate:validate};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("archive-toolkit-conditional-workflow-router",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();