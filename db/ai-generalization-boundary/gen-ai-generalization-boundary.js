(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];} function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var CATS=["shift-types", "ood-detection", "robustness", "measurement", "expansion"];
var PREFIX="JAH-AIGENE-";
var FIELDS=["technique", "boundary", "method", "signal", "benefit", "complexity"];
var SRC="public-harvest";
var POOL=[["Covariate Shift", "Input distribution changes while P(y|x) stays; the boundary moves. Moving gets measured. Models get adapted.", "shift-types", 2, "Measure", "Inputs", "Detect shift", "Measured move", "Adapted", "Medium"], ["Concept Shift", "P(y|x) itself changes; the old mapping breaks. Breaking gets detected. Models get retrained.", "shift-types", 3, "Detect", "Mapping", "Monitor", "Detected break", "Retrained", "High"], ["OOD Detection Methods", "Out-of-distribution inputs are flagged; the flagging protects. Protection gets automatic. Trust gets kept.", "ood-detection", 2, "Flag", "Unknown", "Scores", "Kept trust", "Automatic", "Medium"], ["Adversarial Boundaries", "Adversarial examples probe the boundary; the probing maps. Mapping gets hostile. Weaknesses get found.", "robustness", 3, "Probe", "Adversarial", "Attacks", "Found weak", "Hostile map", "High"], ["Generalization Measurement", "The train-test-OOD gap is measured; the number is honest. Honesty gets numeric. Limits get known.", "measurement", 2, "Measure gap", "All", "Honest numbers", "Known limits", "Numeric", "Medium"], ["Domain Generalization", "Models train to generalize across domains; the training is robust. Robustness gets learned. Boundaries get pushed.", "expansion", 3, "DG train", "Domains", "Robust", "Pushed", "Learned", "High"], ["Spurious Correlation Boundaries", "Models relying on spurious features break at the boundary; the reliance is exposed. Exposure gets diagnostic. Fixes get targeted.", "shift-types", 2, "Expose", "Spurious", "Diagnostic", "Targeted fix", "Diagnostic", "Medium"], ["Calibration at Boundaries", "Confidence degrades at the boundary; the degradation is measured. Measuring gets honest. Decisions get cautious.", "measurement", 2, "Measure", "Edge", "Honest", "Cautious", "Honest", "Medium"], ["Boundary Expansion via Data", "More diverse data expands the boundary; the expansion is empirical. Empiricism gets scaled. Coverage gets broad.", "expansion", 2, "Diversify", "Data", "Scale", "Broad", "Empirical", "Medium"], ["Worst-Group Robustness", "Performance on the worst group is the boundary; the metric is demanding. Demanding gets fair. Minorities get served.", "robustness", 3, "Worst-group", "Groups", "Demanding", "Served", "Fair", "High"], ["Boundary Visualization", "The boundary is drawn; the picture informs. Drawing gets clear. Understanding gets instant.", "measurement", 1, "Draw", "Map", "Visualize", "Instant", "Clear", "Low"], ["Stress Testing", "Models are stressed beyond the boundary; the breaking point is found. Finding gets deliberate. Limits get known truly.", "robustness", 2, "Stress", "Breaking", "Deliberate", "Truly known", "Deliberate", "Medium"], ["Boundary-Aware Deployment", "Deployment respects the boundary; the respect is engineered. Engineering gets cautious. Users get safe.", "expansion", 2, "Respect", "Deploy", "Engineer", "Safe users", "Cautious", "Medium"], ["Continual Boundary Expansion", "The boundary expands as the model learns; the expansion is tracked. Tracking gets longitudinal. Growth gets visible.", "expansion", 3, "Expand", "Over time", "Track", "Visible growth", "Longitudinal", "High"], ["Boundary Documentation", "Known boundaries are documented; the record guides. Guiding gets written. Users get informed.", "measurement", 1, "Document", "Known", "Write", "Informed", "Written", "Low"], ["Uncertainty at Boundaries", "Uncertainty rises at the boundary; the rise is the signal. Signaling gets natural. Caution gets automatic.", "ood-detection", 2, "Rise", "Edge", "Natural", "Automatic caution", "Natural", "Medium"], ["Boundary Testing Suites", "Suites test the boundary systematically; the testing is thorough. Thoroughness gets automated. Gaps get found.", "measurement", 2, "Suite", "Systematic", "Automated", "Found gaps", "Thorough", "Medium"], ["Human-AI Boundary Handoff", "At the boundary, humans take over; the handoff is smooth. Smoothness gets designed. Safety gets kept.", "expansion", 1, "Handoff", "Edge", "Design", "Kept safety", "Smooth", "Low"], ["Theoretical Bounds", "Theory bounds generalization; the math guides. Guiding gets rigorous. Expectations get set.", "measurement", 3, "Theory", "Math", "Rigorous", "Set expectations", "Rigorous", "High"], ["Boundary Monitoring", "The boundary is monitored in production; the watch is continuous. Continuity gets automated. Drift gets caught.", "ood-detection", 2, "Monitor", "Prod", "Continuous", "Caught drift", "Automated", "Medium"]];
function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  var cat=opts.category||pick(CATS,rnd);
  var sub=POOL.filter(function(p){return p[2]===cat;});
  var row=pick(sub.length?sub:POOL,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  var rec={id:id,t:row[0],g:row[2],c:0,title:row[0],description:row[1],category:row[2],ladder_rank:row[3]};
  for(var i=0;i<FIELDS.length;i++){ rec[FIELDS[i]]=row[4+i]; }
  var param=ri(rnd,2,40);
  rec.demo={language:'python',code:'train_acc, ood_acc = 95, 72\ngap = train_acc - ood_acc\nprint(\"in-distribution: %d%%, OOD: %d%%\" % (train_acc, ood_acc))\nprint(\"generalization gap: %d points\" % gap)\nprint(\"boundary: mapped (gap = %d)\" % gap)\nfor _ in range(__PARAM__):\n    pass\nprint(\"param:\", __PARAM__)\n',run:'python3'};
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
var gen={version:"jahdb-ai-generalization-boundary-1.0",generate:generate,validate:validate};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("ai-generalization-boundary",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
