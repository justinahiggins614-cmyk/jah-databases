(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];} function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var CATS=["strategy-comparison", "selection-methods", "hybrid", "data-efficiency", "cost-analysis"];
var PREFIX="JAH-ALSS-";
var FIELDS=["technique", "task", "strategy", "evidence", "benefit", "complexity"];
var SRC="public-harvest";
var POOL=[["Supervised vs Self-Supervised", "The choice depends on labels: abundant labels favor supervised, scarce favor self-supervised. The decision is data-driven. Strategies get matched.", "strategy-comparison", 1, "Comparison", "Classification", "Match data", "Benchmarks", "Matched", "Low"], ["When RL Beats Supervised", "RL wins when the objective is sequential and reward-defined; supervised wins for static mappings. The boundary is clear. Choices get principled.", "strategy-comparison", 2, "Boundary", "Control", "RL", "Reward-defined", "Principled", "Medium"], ["Hybrid Strategies", "Pretrain self-supervised, fine-tune supervised, align with RL: the hybrid wins. Combination gets powerful. Strategies get stacked.", "hybrid", 2, "Stack", "LLM", "SS+Sup+RL", "Best scores", "Powerful", "Medium"], ["Data Efficiency Analysis", "Strategies are compared on data efficiency: accuracy per label. The analysis guides. Labels get budgeted.", "data-efficiency", 2, "Efficiency", "Any", "Per-label acc", "Curves", "Budgeted", "Medium"], ["Cost Analysis", "Strategies are compared on total cost: compute plus labels plus time. The analysis is honest. Choices get economical.", "cost-analysis", 1, "Costing", "Any", "Total cost", "Ledgers", "Economical", "Low"], ["Selection by Task Type", "Task taxonomies map to strategies: perception→supervised, reasoning→RL. The map guides. Selection gets taxonomic.", "selection-methods", 2, "Taxonomy", "Any", "Map", "Literature", "Taxonomic", "Medium"], ["Meta-Strategy Learning", "The strategy itself is learned from past tasks; the meta-learner recommends. Recommendation gets learned. Choices get smart.", "selection-methods", 3, "Meta-learn", "Any", "Learned", "Past tasks", "Smart", "High"], ["Curriculum Strategy Choice", "The strategy changes across training: self-supervised early, supervised late. Change gets planned. Training gets phased.", "hybrid", 2, "Phasing", "Vision", "SS->Sup", "Better", "Phased", "Medium"], ["Few-Shot Strategy", "With tiny data, few-shot and meta-learning beat full training. The strategy fits the data. Small gets smart.", "data-efficiency", 2, "Few-shot", "Rare classes", "Meta", "Wins small", "Smart small", "Medium"], ["Imitation vs RL", "Imitation wins with good demos; RL wins when exploration is needed. The choice is demo-driven. Strategies get demo-matched.", "strategy-comparison", 2, "Demo check", "Control", "Match demos", "Demos exist?", "Demo-matched", "Medium"], ["Unsupervised Discovery", "When the structure is unknown, unsupervised discovery precedes strategy choice. Discovery gets first. Structure gets found.", "selection-methods", 1, "Discover", "Unknown", "Explore first", "Clusters", "Found", "Low"], ["Strategy Benchmarks", "Strategies are benchmarked head-to-head on the same task; the winner is evidence. Benchmarks get fair. Winners get proven.", "strategy-comparison", 2, "Head-to-head", "Any", "Benchmark", "Same task", "Proven", "Medium"], ["Transfer Strategy", "Pretrained models transfer: the strategy is fine-tune, not train. Transfer gets default. Training gets cheap.", "data-efficiency", 1, "Fine-tune", "New domain", "Transfer", "Cheap wins", "Default", "Low"], ["Active Strategy Switching", "The strategy switches mid-training based on signals; the switching is adaptive. Adaptation gets live. Training gets responsive.", "hybrid", 3, "Switch", "Any", "Adaptive", "Signals", "Responsive", "High"], ["Strategy for Safety", "Safety-critical tasks need verifiable strategies: supervised with bounds. Safety gets strategy. Choices get cautious.", "selection-methods", 2, "Cautious", "Safety", "Verifiable", "Bounds", "Cautious", "Medium"], ["Compute-Optimal Strategy", "Chinchilla-style: the strategy balances parameters and data. Balance gets optimal. Compute gets respected.", "cost-analysis", 2, "Balance", "LLM", "Chinchilla", "Scaling laws", "Optimal", "Medium"], ["Strategy Documentation", "Chosen strategies are documented with reasons; the record guides future choices. Documentation gets thorough. Futures get informed.", "selection-methods", 1, "Document", "Any", "Record", "Reasons", "Informed", "Low"], ["Ensemble of Strategies", "Multiple strategies ensemble; the diversity helps. Ensembles get strategic. Robustness gets voted.", "hybrid", 2, "Ensemble", "Any", "Vote", "Better", "Voted", "Medium"], ["Strategy Failure Analysis", "Failed strategies are analyzed: the lessons are recorded. Failure gets educational. Futures get wiser.", "strategy-comparison", 1, "Analyze fail", "Any", "Learn", "Lessons", "Wiser", "Low"], ["Online Strategy Selection", "Strategies are selected online via bandits; the best emerges. Selection gets automatic. Training gets self-tuning.", "selection-methods", 3, "Bandits", "Any", "Online", "Regret bounds", "Automatic", "High"]];
function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  var cat=opts.category||pick(CATS,rnd);
  var sub=POOL.filter(function(p){return p[2]===cat;});
  var row=pick(sub.length?sub:POOL,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  var rec={id:id,t:row[0],g:row[2],c:0,title:row[0],description:row[1],category:row[2],ladder_rank:row[3]};
  for(var i=0;i<FIELDS.length;i++){ rec[FIELDS[i]]=row[4+i]; }
  var param=ri(rnd,2,40);
  rec.demo={language:'python',code:'strategies = {\"supervised\": 85, \"self-sup\": 88, \"hybrid\": 91}\nbest = max(strategies, key=strategies.get)\nprint(\"strategy scores:\", strategies)\nprint(\"selected:\", best, \"(%d%%)\" % strategies[best])\nfor _ in range(__PARAM__):\n    pass\nprint(\"param:\", __PARAM__)\n',run:'python3'};
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
var gen={version:"jahdb-ai-learning-strategy-selection-1.0",generate:generate,validate:validate};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("ai-learning-strategy-selection",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
