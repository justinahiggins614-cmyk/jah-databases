(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];} function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var CATS=["cot-methods", "search-methods", "verification", "selection", "efficiency"];
var PREFIX="JAH-ARSS-";
var FIELDS=["technique", "problem", "strategy", "evidence", "benefit", "complexity"];
var SRC="public-harvest";
var POOL=[["Chain-of-Thought Prompting", "Step-by-step reasoning in the prompt improves complex answers; the thinking is visible. Reasoning gets explicit. Answers get better.", "cot-methods", 1, "CoT", "Math", "Step-by-step", "+20% acc", "Explicit", "Low"], ["Tree of Thoughts", "Reasoning branches and backtracks like search; the tree explores. Exploration gets systematic. Solutions get found.", "search-methods", 3, "ToT", "Puzzles", "Branch+prune", "Solves hard", "Systematic", "High"], ["Self-Consistency", "Multiple reasoning paths vote; the majority wins. Voting gets wise. Answers get robust.", "cot-methods", 2, "Vote", "Any", "Majority", "+5% robust", "Wise", "Medium"], ["Verification Strategies", "A verifier checks the reasoning; wrong paths are rejected. Checking gets strict. Reasoning gets trusted.", "verification", 2, "Verifier", "Proofs", "Check", "Fewer errors", "Trusted", "Medium"], ["Program-Aided Reasoning", "The model writes code and runs it; the execution verifies. Reasoning gets executable. Answers get computed.", "cot-methods", 2, "PAL", "Math", "Code+run", "Exact", "Executable", "Medium"], ["Strategy Selection Rules", "Simple problems get CoT, hard get search; the rule is problem-driven. Selection gets principled. Compute gets budgeted.", "selection", 2, "Rules", "Any", "Match difficulty", "Efficient", "Budgeted", "Medium"], ["Least-to-Most Prompting", "Problems decompose into subproblems solved in order; the decomposition guides. Guidance gets structured. Hard gets easy.", "cot-methods", 2, "Decompose", "Complex", "Subproblems", "Solves", "Structured", "Medium"], ["ReAct (Reason+Act)", "Reasoning interleaves with tool actions; the loop grounds. Grounding gets live. Answers get verified.", "search-methods", 2, "ReAct", "QA", "Think+act", "Grounded", "Live", "Medium"], ["Reflection Strategies", "The model reflects on its reasoning and revises; the loop improves. Reflection gets productive. Answers get polished.", "verification", 2, "Reflect", "Writing", "Revise loop", "Better", "Polished", "Medium"], ["Best-of-N Sampling", "N candidates generate, the best is picked by a scorer; the picking improves. Sampling gets selective. Quality gets top.", "search-methods", 1, "Best-of-N", "Any", "Sample+pick", "Better", "Selective", "Low"], ["Process Supervision", "Each reasoning step is supervised, not just the answer; the supervision is dense. Training gets detailed. Reasoning gets shaped.", "verification", 3, "PRM", "Math", "Step rewards", "Better CoT", "Shaped", "High"], ["Reasoning Efficiency", "Shorter reasoning is cheaper; the strategy trades length for cost. Efficiency gets measured. Tokens get budgeted.", "efficiency", 1, "Budget", "Any", "Length cap", "Cheaper", "Budgeted", "Low"], ["Distilled Reasoning", "Long reasoning distills into short; the student thinks fast. Distillation gets clever. Speed gets kept.", "efficiency", 2, "Distill", "Any", "Short teach", "Fast", "Kept speed", "Medium"], ["Tool-Augmented Selection", "The strategy picks tools per subproblem; the selection is dynamic. Tools get chosen. Reasoning gets equipped.", "selection", 3, "Dynamic", "Complex", "Per-step tools", "Solves", "Equipped", "High"], ["Reasoning Benchmarks", "Strategies are benchmarked on reasoning suites; the winner is evidence. Benchmarks get fair. Strategies get ranked.", "selection", 2, "Benchmark", "Any", "Suite test", "Ranked", "Fair", "Medium"], ["Failure Mode Analysis", "Reasoning failures are categorized: the patterns guide strategy choice. Failures get studied. Choices get informed.", "selection", 1, "Analyze", "Any", "Study fails", "Patterns", "Informed", "Low"], ["Adaptive Reasoning Depth", "Depth adapts to difficulty: easy gets short, hard gets long. Adaptation gets smart. Compute gets respected.", "efficiency", 2, "Adapt depth", "Any", "Difficulty match", "Efficient", "Smart", "Medium"], ["Multi-Agent Reasoning", "Agents reason together and debate; the debate improves. Reasoning gets social. Answers get debated.", "search-methods", 3, "Debate", "Hard", "Agent debate", "Better", "Social", "High"], ["Reasoning Provenance", "Reasoning steps are recorded; the provenance is auditable. Recording gets complete. Trust gets earned.", "verification", 1, "Record", "Any", "Audit trail", "Auditable", "Earned trust", "Low"], ["Strategy Cost Modeling", "Each strategy's cost is modeled; the choice is economical. Modeling gets precise. Choices get cheap.", "efficiency", 2, "Cost model", "Any", "Economical", "Precise", "Cheap", "Medium"]];
function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  var cat=opts.category||pick(CATS,rnd);
  var sub=POOL.filter(function(p){return p[2]===cat;});
  var row=pick(sub.length?sub:POOL,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  var rec={id:id,t:row[0],g:row[2],c:0,title:row[0],description:row[1],category:row[2],ladder_rank:row[3]};
  for(var i=0;i<FIELDS.length;i++){ rec[FIELDS[i]]=row[4+i]; }
  var param=ri(rnd,2,40);
  rec.demo={language:'python',code:'scores = {\"cot\": 78, \"tot\": 85, \"verify\": 89}\nbest = max(scores, key=scores.get)\nprint(\"reasoning scores:\", scores)\nprint(\"selected:\", best)\nfor _ in range(__PARAM__):\n    pass\nprint(\"param:\", __PARAM__)\n',run:'python3'};
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
var gen={version:"jahdb-ai-reasoning-strategy-selection-1.0",generate:generate,validate:validate};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("ai-reasoning-strategy-selection",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
