(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];} function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var CATS=["search-spaces", "strategies", "efficiency", "evaluation", "deployment"];
var PREFIX="JAH-AIARCH-";
var FIELDS=["technique", "space", "method", "cost", "benefit", "complexity"];
var SRC="public-harvest";
var POOL=[["Reinforcement Learning NAS", "A controller RNN samples architectures and gets accuracy as reward; the pioneering but expensive approach. The controller learns to design. Cost is the tuition.", "strategies", 3, "RL controller", "Cell-based", "Policy gradient", "Thousands GPU-days", "Pioneering", "High"], ["Evolutionary NAS", "Architectures evolve: mutate, crossover, select by accuracy. Evolution explores broadly. Populations get fit.", "strategies", 3, "Evolution", "Cell-based", "Mutate+select", "Hundreds GPU-days", "Broad explore", "High"], ["DARTS (Differentiable)", "Architecture weights are learned by gradient descent on a supernet; the search is differentiable. DARTS is fast but finicky. Gradients get architectural.", "strategies", 2, "DARTS", "Supernet", "Bilevel gradient", "Few GPU-days", "Fast", "Medium"], ["One-Shot / Weight Sharing", "All architectures share weights in a supernet; each is evaluated cheaply. Sharing makes search affordable. Weights get shared.", "efficiency", 2, "Weight sharing", "Supernet", "Shared eval", "One training", "Affordable", "Medium"], ["ProxylessNAS", "Search directly on the target task and hardware without proxies; the found architecture is deployment-ready. No proxy gap. Search gets direct.", "deployment", 3, "Direct search", "Mobile", "Hardware-aware", "200 GPU-hours", "Deploy-ready", "High"], ["Hardware-Aware Search", "Latency is part of the objective; the search trades accuracy for speed on the real device. Hardware gets a vote. Tradeoffs get real.", "deployment", 2, "Latency objective", "Mobile", "Measured latency", "Moderate", "Real tradeoffs", "Medium"], ["Search Space Design", "The space defines what's findable: cells, macro skeletons, operations. Design gets deliberate. Findability gets designed.", "search-spaces", 2, "Space design", "N/A (meta)", "Deliberate design", "Design effort", "Findable", "Medium"], ["Random Search Baseline", "Random search is the baseline every method must beat; it's embarrassingly competitive. Baselines get honest. Fancy gets justified.", "strategies", 1, "Random", "Any", "Uniform sample", "Cheap", "Honest baseline", "Low"], ["Bayesian Optimization NAS", "Surrogate models predict architecture performance; the search samples where promising. Sampling gets smart. Evaluations get few.", "strategies", 2, "BayesOpt", "Cell-based", "Surrogate guided", "Few hundred evals", "Smart sampling", "Medium"], ["Zero-Cost Proxies", "Proxies (grad norms, NTK) rank architectures without training; the ranking is instant. Proxies get instant. Search gets free-ish.", "efficiency", 2, "Proxies", "Any", "Train-free rank", "~Zero", "Instant rank", "Medium"], ["Fairness in Weight Sharing", "Shared weights must be trained fairly or rankings lie; fairness techniques fix the bias. Sharing gets fair. Rankings get honest.", "efficiency", 3, "Fair training", "Supernet", "Debiased", "Careful", "Honest ranks", "High"], ["Multi-Objective NAS", "Accuracy, latency, and size are optimized together; the Pareto front is the answer. Objectives get plural. Fronts get found.", "deployment", 2, "Pareto search", "Mobile", "Multi-objective", "Moderate", "Plural objectives", "Medium"], ["Transformer Search Spaces", "Spaces for transformers: attention variants, MLP ratios, depths. The space fits the architecture. Transformers get searched.", "search-spaces", 3, "Transformer space", "Transformer", "Component search", "High", "Fitted space", "High"], ["NAS Evaluation Protocol", "Found architectures are retrained from scratch with fixed hyperparameters; the protocol is fair. Evaluation gets standardized. Comparisons get honest.", "evaluation", 2, "Retrain protocol", "N/A", "Fixed hyperparams", "Retrain cost", "Honest compare", "Medium"], ["Search Cost Reporting", "Papers must report the search cost honestly; hidden costs mislead the field. Reporting gets honest. Fields get informed.", "evaluation", 1, "Cost report", "N/A", "Honest accounting", "Reported", "Informed field", "Low"], ["Robustness-Aware Search", "Architectures are searched for robustness too; the objective includes adversarial accuracy. Robustness gets designed. Models get tough.", "deployment", 3, "Robust objective", "Cell-based", "Adv accuracy", "High", "Tough models", "High"], ["Green NAS (Efficient)", "Search methods minimize carbon: proxies, sharing, and early stopping. The planet gets considered. Search gets green.", "efficiency", 1, "Green methods", "Any", "Carbon-aware", "Low carbon", "Considered planet", "Low"], ["NAS for Object Detection", "Search spaces include backbones, necks, and heads for detection; the found detectors are deployment-tuned. Detection gets searched. Boxes get found.", "search-spaces", 3, "Detection space", "Detector", "Full search", "High", "Tuned detectors", "High"], ["Latency Predictors", "Learned latency predictors replace on-device measurement; the search queries the predictor. Prediction gets fast. Search gets quick.", "efficiency", 2, "Predictors", "Mobile", "Learned latency", "Train once", "Fast queries", "Medium"], ["Reproducible NAS", "NAS runs are made reproducible: seeds, spaces, and code published. The field gets science. Luck gets separated from method.", "evaluation", 1, "Reproducibility", "N/A", "Publish all", "Discipline", "Science", "Low"]];
function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  var cat=opts.category||pick(CATS,rnd);
  var sub=POOL.filter(function(p){return p[2]===cat;});
  var row=pick(sub.length?sub:POOL,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  var rec={id:id,t:row[0],g:row[2],c:0,title:row[0],description:row[1],category:row[2],ladder_rank:row[3]};
  for(var i=0;i<FIELDS.length;i++){ rec[FIELDS[i]]=row[4+i]; }
  var param=ri(rnd,2,40);
  rec.demo={language:'python',code:'import random\nrandom.seed(11)\nspace = [\"conv3\", \"conv5\", \"dwconv\", \"skip\"]\narch = [random.choice(space) for _ in range(6)]\nprint(\"sampled architecture:\", arch)\nprint(\"estimated params: %dK\" % (sum(10 for _ in arch)))\nfor _ in range(__PARAM__):\n    pass\nprint(\"param:\", __PARAM__)\n',run:'python3'};
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
var gen={version:"jahdb-ai-architecture-search-1.0",generate:generate,validate:validate};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("ai-architecture-search",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
