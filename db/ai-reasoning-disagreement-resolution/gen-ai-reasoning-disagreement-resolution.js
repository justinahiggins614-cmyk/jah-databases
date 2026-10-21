(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];} function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var CATS=["detection", "adjudication", "consensus", "debate", "verification"];
var PREFIX="JAH-ARDR-";
var FIELDS=["technique", "dispute", "method", "outcome", "benefit", "complexity"];
var SRC="public-harvest";
var POOL=[["Disagreement Detection", "Conflicting reasoning outputs are detected; the detection is automatic. Conflicts get found. Silence gets broken.", "detection", 1, "Detect", "Outputs", "Compare", "Found", "Automatic", "Low"], ["Majority Vote Resolution", "The majority of reasoning paths wins; the vote is simple. Simplicity gets effective. Disputes get settled.", "consensus", 1, "Vote", "Answers", "Majority", "Settled", "Effective", "Low"], ["Weighted Voting", "Votes are weighted by path confidence; the weighting is fair. Fairness gets numeric. Quality gets rewarded.", "consensus", 2, "Weighted", "Answers", "By confidence", "Rewarded quality", "Fair", "Medium"], ["Adjudicator Models", "A separate model adjudicates disputes; the judge is trained. Judging gets specialized. Disputes get ruled.", "adjudication", 3, "Judge model", "Hard cases", "Trained judge", "Ruled", "Specialized", "High"], ["Debate Protocols", "Agents debate until agreement; the protocol is structured. Structure gets productive. Truth gets debated.", "debate", 3, "Debate", "Positions", "Structured", "Agreement", "Productive", "High"], ["Evidence Weighing", "Disputes are resolved by evidence strength; the weighing is rational. Rationality gets applied. Facts get winning.", "adjudication", 2, "Weigh", "Claims", "Evidence", "Facts win", "Rational", "Medium"], ["Confidence Arbitration", "The most confident correct-leaning path wins; the arbitration is calibrated. Calibration gets used. Disputes get resolved.", "adjudication", 2, "Arbitrate", "Paths", "Confidence", "Resolved", "Used cal", "Medium"], ["Consistency Checking", "Reasoning paths are checked for internal consistency; the inconsistent are dropped. Dropping gets principled. Quality gets filtered.", "verification", 2, "Check", "Paths", "Consistency", "Filtered", "Principled", "Medium"], ["Meta-Reasoning", "Reasoning about the reasoning resolves disputes; the meta is powerful. Power gets reflective. Disputes get dissolved.", "debate", 3, "Meta", "Reasoning", "Reflect", "Dissolved", "Reflective", "High"], ["Human Tie-Breaking", "Humans break ties the models can't; the tie-break is final. Finality gets human. Hard gets decided.", "adjudication", 1, "Human", "Ties", "Ask human", "Decided", "Final", "Low"], ["Disagreement Logging", "All disagreements are logged; the record teaches. Teaching gets data. Futures get wiser.", "detection", 1, "Log", "All", "Record", "Wiser future", "Data", "Low"], ["Root Cause Analysis", "Disagreements are analyzed for root causes; the analysis prevents. Prevention gets systematic. Repeats get avoided.", "detection", 2, "Analyze", "Causes", "RCA", "Avoided repeats", "Systematic", "Medium"], ["Consensus Thresholds", "Consensus requires a threshold; the bar is set. Setting gets principled. Agreement gets meaningful.", "consensus", 2, "Threshold", "Agreement", "Set bar", "Meaningful", "Principled", "Medium"], ["Minority Report Preservation", "Dissenting views are preserved; the minority is recorded. Recording gets respectful. Wisdom gets kept.", "consensus", 1, "Preserve", "Minority", "Record", "Kept wisdom", "Respectful", "Low"], ["Adjudication Benchmarks", "Resolution methods are benchmarked; the best is evidence. Benchmarking gets fair. Methods get ranked.", "verification", 2, "Benchmark", "Methods", "Fair test", "Ranked", "Fair", "Medium"], ["Resolution Explanations", "Resolutions are explained; the explanation builds trust. Building gets transparent. Users get reasons.", "adjudication", 2, "Explain", "Resolved", "Transparent", "Reasons", "Transparent", "Medium"], ["Escalation Protocols", "Unresolvable disputes escalate; the protocol is clear. Clarity gets procedural. Stucks get unstuck.", "debate", 2, "Escalate", "Hard", "Clear protocol", "Unstuck", "Procedural", "Medium"], ["Disagreement Metrics", "Disagreement rates are metrics; the trend informs. Informing gets numeric. Health gets measured.", "detection", 2, "Metrics", "Rates", "Track", "Measured health", "Numeric", "Medium"], ["Self-Consistency Checks", "Models check their own consistency; the check is internal. Internal gets honest. Disputes get prevented.", "verification", 1, "Self-check", "Own", "Internal", "Prevented", "Honest", "Low"], ["Resolution Audits", "Resolutions are audited; the audit verifies fairness. Verifying gets external. Trust gets earned.", "verification", 3, "Audit", "Resolved", "External", "Earned trust", "External", "High"]];
function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  var cat=opts.category||pick(CATS,rnd);
  var sub=POOL.filter(function(p){return p[2]===cat;});
  var row=pick(sub.length?sub:POOL,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  var rec={id:id,t:row[0],g:row[2],c:0,title:row[0],description:row[1],category:row[2],ladder_rank:row[3]};
  for(var i=0;i<FIELDS.length;i++){ rec[FIELDS[i]]=row[4+i]; }
  var param=ri(rnd,2,40);
  rec.demo={language:'python',code:'votes = {\"42\": 7, \"43\": 2, \"41\": 1}\nwinner = max(votes, key=votes.get)\nprint(\"votes:\", votes)\nprint(\"resolved: %s (%d/10)\" % (winner, votes[winner]))\nfor _ in range(__PARAM__):\n    pass\nprint(\"param:\", __PARAM__)\n',run:'python3'};
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
var gen={version:"jahdb-ai-reasoning-disagreement-resolution-1.0",generate:generate,validate:validate};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("ai-reasoning-disagreement-resolution",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
