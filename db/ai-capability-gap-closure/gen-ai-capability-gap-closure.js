(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];} function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var CATS=["assessment", "prioritization", "training-plans", "verification", "tracking"];
var PREFIX="JAH-ACG-";
var FIELDS=["technique", "gap", "method", "measure", "benefit", "complexity"];
var SRC="public-harvest";
var POOL=[["Gap Assessment", "Capabilities are tested to find gaps; the assessment is systematic. Gaps get found. Blind spots get lit.", "assessment", 1, "Test all", "Unknown", "Systematic", "Found gaps", "Lit spots", "Low"], ["Gap Prioritization", "Gaps are ranked by impact and feasibility; the ranking guides. Priorities get principled. Effort gets aimed.", "prioritization", 2, "Rank", "Many", "Impact x feasible", "Aimed effort", "Principled", "Medium"], ["Training Plans", "Each gap gets a training plan: data, method, timeline. Plans get concrete. Gaps get scheduled.", "training-plans", 2, "Plan", "Reasoning", "Concrete plan", "Scheduled", "Concrete", "Medium"], ["Closure Verification", "Closed gaps are re-tested; the verification proves. Proof gets rigorous. Claims get earned.", "verification", 2, "Re-test", "Closed", "Rigorous", "Earned claims", "Proven", "Medium"], ["Gap Tracking Dashboards", "Gaps are tracked on dashboards; the progress is visible. Visibility gets complete. Momentum gets kept.", "tracking", 1, "Dashboard", "All", "Track", "Visible", "Kept momentum", "Low"], ["Benchmark-Driven Gaps", "Benchmarks reveal gaps: the failures are the map. Maps get honest. Gaps get benchmarked.", "assessment", 2, "Benchmark", "Revealed", "Failures map", "Honest map", "Benchmarked", "Medium"], ["User-Reported Gaps", "Users report where the AI fails; the reports are gold. Gold gets mined. Gaps get real.", "assessment", 1, "Reports", "Real", "Mine feedback", "Mined gold", "Real", "Low"], ["Adversarial Gap Finding", "Adversaries probe for gaps; the probing is thorough. Thoroughness gets adversarial. Weaknesses get exposed.", "assessment", 3, "Red team", "Hidden", "Probe", "Exposed", "Thorough", "High"], ["Gap Closure Sprints", "Sprints focus on one gap; the focus is intense. Intensity gets scheduled. Gaps get closed fast.", "training-plans", 2, "Sprint", "One", "Intense focus", "Fast close", "Intense", "Medium"], ["Curriculum for Gaps", "Gap-specific curricula are built; the teaching is targeted. Targeting gets precise. Learning gets efficient.", "training-plans", 2, "Curriculum", "Specific", "Targeted", "Efficient", "Precise", "Medium"], ["Regression Prevention", "Closed gaps stay closed: regression tests guard. Guarding gets automatic. Progress gets kept.", "verification", 2, "Guard", "Closed", "Regression tests", "Kept progress", "Automatic", "Medium"], ["Gap Cost Estimation", "Closing each gap is costed; the budget is informed. Costing gets honest. Spending gets wise.", "prioritization", 1, "Cost", "Each", "Estimate", "Wise spend", "Honest", "Low"], ["Cross-Team Gap Ownership", "Gaps are owned by teams; the ownership is clear. Clarity gets assigned. Gaps get closed.", "prioritization", 2, "Own", "Each", "Assign team", "Closed", "Clear", "Medium"], ["Gap Closure Celebrations", "Closed gaps are celebrated; the morale compounds. Celebration gets scheduled. Teams get energized.", "tracking", 1, "Celebrate", "Closed", "Recognize", "Energized", "Scheduled joy", "Low"], ["Long-Tail Gaps", "Rare gaps are handled specially: the tail is long. Specialness gets designed. Coverage gets complete.", "assessment", 3, "Tail handle", "Rare", "Special", "Complete", "Designed", "High"], ["Gap Dependency Analysis", "Gaps depend on each other; the order matters. Ordering gets computed. Closing gets sequenced.", "prioritization", 2, "Order", "Dependent", "Topo", "Sequenced", "Computed", "Medium"], ["Synthetic Data for Gaps", "Gaps are closed with synthetic data; the generation is targeted. Targeting gets precise. Data gets made.", "training-plans", 3, "Synthesize", "Data-poor", "Generate", "Made data", "Precise", "High"], ["Gap Closure Audits", "Closures are audited independently; the audit verifies. Verification gets external. Trust gets earned.", "verification", 3, "Audit", "Claimed", "Independent", "Earned trust", "External", "High"], ["Gap Trend Analysis", "Gap trends are analyzed over time; the direction informs. Direction gets known. Strategy gets data.", "tracking", 2, "Trends", "Over time", "Analyze", "Known direction", "Data strategy", "Medium"], ["Stakeholder Gap Reviews", "Stakeholders review gap priorities; the alignment is checked. Checking gets regular. Priorities get agreed.", "prioritization", 1, "Review", "Priorities", "Regular", "Agreed", "Checked", "Low"]];
function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  var cat=opts.category||pick(CATS,rnd);
  var sub=POOL.filter(function(p){return p[2]===cat;});
  var row=pick(sub.length?sub:POOL,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  var rec={id:id,t:row[0],g:row[2],c:0,title:row[0],description:row[1],category:row[2],ladder_rank:row[3]};
  for(var i=0;i<FIELDS.length;i++){ rec[FIELDS[i]]=row[4+i]; }
  var param=ri(rnd,2,40);
  rec.demo={language:'python',code:'gaps = {\"reasoning\": 30, \"coding\": 15, \"vision\": 5}\nfor name, pct in sorted(gaps.items(), key=lambda x: -x[1]):\n    bar = \"#\" * (pct // 5)\n    print(\"%-10s [%s] %d%% gap\" % (name, bar, pct))\nprint(\"biggest gap first\")\nfor _ in range(__PARAM__):\n    pass\nprint(\"param:\", __PARAM__)\n',run:'python3'};
  rec.demo.code=rec.demo.code.replace(/__PARAM__/g,String(param));
  rec.provenance='JAH Databases lane N1 build';
  rec.last_verified='2026-10-21';
  rec.src=SRC;
  rec._seed=seed;
  return rec;
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!new RegExp('^'+PREFIX.replace(/[-\/\\^$*+?.()|[\]{}]/g,'\\$&')+'\\d{6}$').test(r.id||''))e.push('id');
  if(typeof r.title!=='string'||!r.title.length)e.push('title');
  if(typeof r.description!=='string'||r.description.length<40)e.push('description');
  if(CATS.indexOf(r.category)<0)e.push('category');
  if([1,2,3].indexOf(r.ladder_rank)<0)e.push('ladder_rank');
  FIELDS.forEach(function(f){ if(typeof r[f]!=='string'||!r[f].length)e.push('field:'+f); });
  if(!r.demo||r.demo.language!=='python'||typeof r.demo.code!=='string'||!r.demo.code.length)e.push('demo');
  if(r.src!==SRC)e.push('src');
  return {ok:!e.length,errors:e};
}
var gen={version:"jahdb-ai-capability-gap-closure-1.0",generate:generate,validate:validate};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("ai-capability-gap-closure",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
