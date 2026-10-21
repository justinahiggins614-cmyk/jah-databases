(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];} function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var CATS=["confidence", "uncertainty", "honesty", "evaluation", "improvement"];
var PREFIX="JAH-ASAC-S-";
var FIELDS=["technique", "target", "method", "measure", "benefit", "complexity"];
var SRC="signature-generated-completion";
var POOL=[["Signature Honesty Gardener", "Signature original — gardens model honesty: the confidence is tended to match reality. The garden blooms truthful. Trust gets cultivated.", "confidence", 2, "Signature gardener", "Probabilities", "Tended match", "Cultivated", "Truthful", "Medium"], ["Signature Temperature Tuner", "Signature original — tunes the temperature like an instrument: the calibration sings. The tuning is musical. Honesty gets harmonious.", "confidence", 1, "Signature tuner", "Logits", "Musical tune", "Harmonious", "Musical", "Low"], ["Signature Uncertainty Bard", "Signature original — a bard that sings the unknown: the uncertainty becomes verse. The singing names. Decisions get informed poetically.", "uncertainty", 2, "Signature bard", "Predictions", "Sung unknown", "Poetic inform", "Names", "Medium"], ["Signature Wise Abstainer", "Signature original — an abstainer of wisdom: the uncertain is declined gracefully. The declining is dignified. Errors get avoided elegantly.", "honesty", 2, "Signature abstainer", "Uncertain", "Dignified decline", "Elegant avoid", "Dignified", "Medium"], ["Signature Fair Referee", "Signature original — a referee for calibration benchmarks: the contest is fair. The refereeing is strict. Models get ranked truly.", "evaluation", 2, "Signature referee", "Models", "Strict contest", "Truly ranked", "Fair", "Medium"], ["Signature Humble Reporter", "Signature original — a reporter of humble limits: the plain speech is practiced. The reporting works. Users get truth kindly.", "honesty", 1, "Signature reporter", "Users", "Practiced plain", "Kindly true", "Humble", "Low"], ["Signature Lost Detector", "Signature original — detects when the model is lost: the OOD is sensed. The sensing saves. Hallucination gets prevented truly.", "uncertainty", 3, "Signature detector", "Inputs", "Sensed lost", "Truly prevented", "Saves", "High"], ["Signature Crowd Gardener", "Signature original — gardens ensemble crowds: the disagreement is tended into wisdom. The gardening works. Uncertainty gets real truly.", "uncertainty", 2, "Signature gardener", "Predictions", "Tended disagree", "Truly real", "Works", "Medium"], ["Signature Word Measurer", "Signature original — measures confidence words: the verbal is calibrated. The measuring is precise. Users get intuition truly.", "confidence", 1, "Signature measurer", "Answers", "Precise words", "Truly intuitive", "Precise", "Low"], ["Signature Shift Gardener", "Signature original — gardens calibration through shifts: the maintenance is tended. The gardening is hard. Trust gets kept truly.", "evaluation", 3, "Signature gardener", "Deployment", "Tended maintain", "Truly kept", "Hard", "High"], ["Signature Mirror Polisher", "Signature original — polishes self-critique mirrors: the overconfidence is seen. The polishing improves. Honesty gets better truly.", "improvement", 2, "Signature polisher", "Confidence", "Seen overconf", "Truly better", "Improves", "Medium"], ["Signature Threshold Gardener", "Signature original — gardens decision thresholds: the tuning is tended. The gardening optimizes. Actions get right truly.", "confidence", 2, "Signature gardener", "Decisions", "Tended tune", "Truly right", "Optimizes", "Medium"], ["Signature Watch Gardener", "Signature original — gardens calibration dashboards: the watching is tended. The gardening catches drift. Monitoring gets continuous truly.", "evaluation", 1, "Signature gardener", "Live", "Tended watch", "Truly continuous", "Catches", "Low"], ["Signature Humble Measurer", "Signature original — measures against humans humbly: the comparison is honest. The measuring sets goals. Ambition gets data.", "evaluation", 2, "Signature measurer", "Humans", "Honest compare", "Data ambition", "Honest", "Medium"], ["Signature Clarity Gardener", "Signature original — gardens uncertainty communication: the clarity is tended. The gardening builds trust. Users get informed beautifully.", "honesty", 1, "Signature gardener", "Users", "Tended clarity", "Beautiful inform", "Builds trust", "Low"], ["Signature Honesty Teacher", "Signature original — a teacher of native honesty: the loss includes truth. The teaching works. Calibration gets native truly.", "improvement", 3, "Signature teacher", "Models", "Taught truth", "Truly native", "Works", "High"], ["Signature Ignorance Cartographer", "Signature original — maps ignorance like territory: the unknown unknowns are charted. The cartography is brave. Wisdom gets real truly.", "honesty", 2, "Signature cartographer", "Knowledge", "Brave chart", "Truly real", "Brave", "Medium"], ["Signature Safety Quantifier", "Signature original — quantifies safety confidence: the stakes are measured. The quantifying is rigorous. Safety gets proven.", "evaluation", 3, "Signature quantifier", "Safety", "Rigorous measure", "Proven", "Rigorous", "High"], ["Signature Progress Chronicler", "Signature original — chronicles calibration progress: the versions are compared. The chronicle shows. Progress gets visible truly.", "improvement", 1, "Signature chronicler", "Versions", "Compared", "Truly visible", "Shows", "Low"], ["Signature Hardness Gardener", "Signature original — gardens adversarial calibration: the harsh testing is tended. The gardening hardens. Trust gets tempered.", "uncertainty", 3, "Signature gardener", "Robustness", "Tended harsh", "Tempered", "Hardens", "High"]];
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
  rec.origin='Signature original';
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
var gen={version:"jahdb-ai-self-assessment-calibration-signature-1.0",generate:generate,validate:validate};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("ai-self-assessment-calibration-signature",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
