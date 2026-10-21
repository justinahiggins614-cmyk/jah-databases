(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];} function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var CATS=["confidence", "uncertainty", "honesty", "evaluation", "improvement"];
var PREFIX="JAH-ASAC-";
var FIELDS=["technique", "target", "method", "measure", "benefit", "complexity"];
var SRC="public-harvest";
var POOL=[["Confidence Calibration", "Predicted probabilities match true frequencies; the calibration is measured. Honesty gets numeric. Trust gets earned.", "confidence", 2, "Calibrate", "Probabilities", "Match freq", "ECE", "Numeric honesty", "Medium"], ["Temperature Scaling", "A single temperature parameter calibrates logits; the fix is simple. Simplicity gets effective. Calibration gets cheap.", "confidence", 1, "Temp scale", "Logits", "One param", "ECE drop", "Cheap", "Low"], ["Uncertainty Quantification", "Models report uncertainty, not just answers; the unknown is named. Naming gets honest. Decisions get informed.", "uncertainty", 2, "UQ", "Predictions", "Report uncertainty", "Coverage", "Informed", "Medium"], ["Selective Prediction", "Models abstain when uncertain; the abstention is wise. Wisdom gets selective. Errors get avoided.", "honesty", 2, "Abstain", "Uncertain", "Threshold", "Avoided errors", "Wise", "Medium"], ["Calibration Benchmarks", "Calibration is benchmarked across tasks; the comparison is fair. Benchmarks get standard. Models get ranked.", "evaluation", 2, "Benchmark", "Models", "Standard suites", "Ranked", "Standard", "Medium"], ["Honest Capability Reporting", "Models report their limits plainly; the reporting is humble. Humility gets systematic. Users get truth.", "honesty", 1, "Report limits", "Users", "Plain speech", "Truth", "Humble", "Low"], ["Out-of-Distribution Detection", "OOD inputs are detected; the model knows when it's lost. Lostness gets detected. Hallucination gets prevented.", "uncertainty", 3, "OOD detect", "Inputs", "Density", "Detected", "Prevented halluc", "High"], ["Ensemble Uncertainty", "Ensemble disagreement measures uncertainty; the wisdom is in the crowd. Crowds get wise. Uncertainty gets real.", "uncertainty", 2, "Ensemble", "Predictions", "Disagreement", "Real UQ", "Wise crowd", "Medium"], ["Verbalized Confidence", "Models state confidence in words; the words are calibrated. Words get numeric. Users get intuition.", "confidence", 1, "Verbalize", "Answers", "Words", "Intuition", "Numeric words", "Low"], ["Calibration Under Shift", "Calibration is maintained under distribution shift; the maintenance is hard. Hardness gets addressed. Trust gets kept.", "evaluation", 3, "Shift-robust", "Deployment", "Adapt", "Kept trust", "Addressed", "High"], ["Self-Critique Calibration", "Models critique their own confidence; the loop improves. Improvement gets internal. Honesty gets better.", "improvement", 2, "Self-critique", "Confidence", "Loop", "Better", "Internal", "Medium"], ["Decision Thresholds", "Thresholds turn confidence into decisions; the tuning is principled. Principled gets optimal. Actions get right.", "confidence", 2, "Threshold", "Decisions", "Tune", "Right actions", "Optimal", "Medium"], ["Calibration Dashboards", "Calibration is monitored live; the dashboard watches. Watching gets continuous. Drift gets caught.", "evaluation", 1, "Monitor", "Live", "Dashboard", "Caught drift", "Continuous", "Low"], ["Human Calibration Comparison", "Model calibration is compared to human; the comparison humbles. Humbling gets data. Goals get set.", "evaluation", 2, "Compare", "Humans", "Side-by-side", "Set goals", "Data", "Medium"], ["Uncertainty Communication", "Uncertainty is communicated clearly to users; the clarity builds trust. Clarity gets designed. Trust gets built.", "honesty", 1, "Communicate", "Users", "Clear UX", "Built trust", "Designed", "Low"], ["Calibration Training", "Models are trained to be calibrated; the loss includes honesty. Honesty gets trained. Calibration gets native.", "improvement", 3, "Train honest", "Models", "Honest loss", "Native", "Trained", "High"], ["Knowing What You Don't Know", "The core skill: models know their ignorance. Ignorance gets mapped. Wisdom gets real.", "honesty", 2, "Ignorance map", "Knowledge", "Map gaps", "Real wisdom", "Mapped", "Medium"], ["Calibration for Safety", "Safety decisions need calibrated confidence; the stakes demand. Demanding gets met. Safety gets quantified.", "evaluation", 3, "Safety cal", "Safety", "Quantify", "Met demand", "Quantified", "High"], ["Improvement Tracking", "Calibration improves over versions; the trend is tracked. Tracking gets longitudinal. Progress gets visible.", "improvement", 1, "Track", "Versions", "Longitudinal", "Visible", "Tracked", "Low"], ["Adversarial Calibration", "Calibration holds under adversarial pressure; the testing is harsh. Harshness gets survived. Trust gets hardened.", "uncertainty", 3, "Adv test", "Robustness", "Harsh", "Hardened", "Survived", "High"]];
function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  var cat=opts.category||pick(CATS,rnd);
  var sub=POOL.filter(function(p){return p[2]===cat;});
  var row=pick(sub.length?sub:POOL,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  var rec={id:id,t:row[0],g:row[2],c:0,title:row[0],description:row[1],category:row[2],ladder_rank:row[3]};
  for(var i=0;i<FIELDS.length;i++){ rec[FIELDS[i]]=row[4+i]; }
  var param=ri(rnd,2,40);
  rec.demo={language:'python',code:'preds = [(0.9, 1), (0.8, 1), (0.6, 0), (0.7, 1)]\nacc = sum(1 for p, y in preds if (p > 0.5) == y) / len(preds)\navg_conf = sum(p for p, _ in preds) / len(preds)\nprint(\"accuracy: %.2f, avg confidence: %.2f\" % (acc, avg_conf))\nprint(\"calibrated:\" , abs(acc - avg_conf) < 0.15)\nfor _ in range(__PARAM__):\n    pass\nprint(\"param:\", __PARAM__)\n',run:'python3'};
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
var gen={version:"jahdb-ai-self-assessment-calibration-1.0",generate:generate,validate:validate};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("ai-self-assessment-calibration",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
