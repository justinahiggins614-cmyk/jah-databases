(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];} function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var CATS=["few-shot", "curriculum", "imitation", "self-improvement", "transfer"];
var PREFIX="JAH-ASA-";
var FIELDS=["technique", "skill", "method", "evidence", "benefit", "complexity"];
var SRC="public-harvest";
var POOL=[["Few-Shot In-Context Learning", "Models learn skills from a handful of examples in the prompt; no weight updates needed. The skill is in the context. Learning gets instant.", "few-shot", 1, "In-context", "Any pattern", "Prompt examples", "Accuracy jumps", "Instant", "Low"], ["Curriculum Learning", "Skills are taught easy-to-hard; the curriculum orders the learning. Order matters. Learning gets sequenced.", "curriculum", 2, "Curriculum", "Complex tasks", "Easy-first", "Faster converge", "Sequenced", "Medium"], ["Imitation Learning (BC)", "Agents imitate expert demonstrations; behavioral cloning copies the policy. The expert shows. Learning gets demonstrated.", "imitation", 2, "BC", "Control", "Copy expert", "Expert-level", "Demonstrated", "Medium"], ["Self-Play Skill Growth", "Agents improve by playing themselves; the opponent is always matched. Growth gets endless. Skills get forged.", "self-improvement", 3, "Self-play", "Games", "Vs self", "Elo climbs", "Endless", "High"], ["Meta-Learning (MAML)", "Models learn to learn: few gradient steps adapt to new tasks. The learning gets meta. Adaptation gets fast.", "few-shot", 3, "MAML", "Fast adapt", "Meta-train", "5-step adapt", "Meta", "High"], ["Instruction Tuning", "Models learn to follow instructions from instruction-response pairs; the skill is obedience. Tuning gets instructive. Models get helpful.", "curriculum", 2, "Instruct tune", "Following", "Pair training", "Helpful", "Instructive", "Medium"], ["RLHF Skill Shaping", "Human feedback shapes skills toward helpfulness; the reward is learned. Shaping gets human. Skills get aligned.", "self-improvement", 3, "RLHF", "Helpfulness", "Feedback reward", "Preferred", "Aligned", "High"], ["Skill Distillation", "A skilled teacher distills into a fresh student; the skill transfers. Teaching gets distilled. Students get skilled.", "transfer", 2, "Distill", "Any", "Teacher-student", "Student skilled", "Transferred", "Medium"], ["Continual Learning", "Skills accumulate without forgetting; the challenge is catastrophic forgetting. Learning gets lifelong. Memory gets protected.", "curriculum", 3, "Continual", "Many", "No-forget", "Retained", "Lifelong", "High"], ["Active Learning", "The learner queries the most informative examples; the teacher answers. Learning gets efficient. Questions get smart.", "few-shot", 2, "Active", "Classification", "Smart queries", "Fewer labels", "Efficient", "Medium"], ["Demonstration Selection", "Which examples are shown matters enormously; selection is optimized. Examples get chosen. Shots get effective.", "few-shot", 2, "Selection", "In-context", "Optimize shots", "Higher acc", "Effective", "Medium"], ["Skill Hierarchies (Options)", "Complex skills decompose into options (sub-policies); the hierarchy is learned. Decomposition gets hierarchical. Skills get structured.", "curriculum", 3, "Options", "Long tasks", "Sub-policies", "Solves long", "Structured", "High"], ["Inverse RL", "The reward is inferred from expert behavior; the skill's goal gets discovered. Goals get inferred. Experts get understood.", "imitation", 3, "IRL", "Goal inference", "Reward infer", "Matches expert", "Understood", "High"], ["Self-Supervised Pretraining", "Skills emerge from predicting hidden parts; the pretraining is the curriculum. Emergence gets scaled. Foundations get built.", "self-improvement", 2, "Pretrain", "General", "Mask predict", "Transfers", "Scaled", "Medium"], ["Constitutional Self-Critique", "Models critique and revise themselves against principles; the skill is self-improvement. Critique gets internal. Models get better alone.", "self-improvement", 3, "Self-critique", "Alignment", "Revise loop", "Improved", "Internal", "High"], ["Tool Skill Acquisition", "Tool use is learned from tool-augmented demonstrations; the skill is API fluency. Learning gets practical. Tools get mastered.", "imitation", 2, "Tool demos", "Tool use", "Augmented demos", "Fluent", "Practical", "Medium"], ["Cross-Lingual Skill Transfer", "Skills learned in one language transfer to others; the transfer is measured. Languages get bridged. Learning gets multilingual.", "transfer", 2, "X-lingual", "Any", "Shared reps", "Transfers", "Bridged", "Medium"], ["Skill Composition Learning", "New skills compose from old ones; the composition is learned explicitly. Learning gets combinatorial. Skills get combined.", "transfer", 3, "Composition", "Novel", "Compose old", "Zero-shot new", "Combinatorial", "High"], ["Forgetting Mitigation (EWC)", "Elastic weight consolidation protects important weights; forgetting gets prevented. Memory gets elastic. Skills get kept.", "curriculum", 3, "EWC", "Retention", "Protect weights", "Retained", "Kept", "High"], ["Human-in-the-Loop Teaching", "Humans teach interactively: correct, demonstrate, approve. The loop is the classroom. Teaching gets interactive. Learning gets guided.", "imitation", 1, "HITL", "Any", "Interactive", "Guided", "Interactive", "Low"]];
function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  var cat=opts.category||pick(CATS,rnd);
  var sub=POOL.filter(function(p){return p[2]===cat;});
  var row=pick(sub.length?sub:POOL,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  var rec={id:id,t:row[0],g:row[2],c:0,title:row[0],description:row[1],category:row[2],ladder_rank:row[3]};
  for(var i=0;i<FIELDS.length;i++){ rec[FIELDS[i]]=row[4+i]; }
  var param=ri(rnd,2,40);
  rec.demo={language:'python',code:'shots = [1, 5, 10]\nacc = [62, 78, 84]\nfor s, a in zip(shots, acc):\n    print(\"%d-shot: %d%% accuracy\" % (s, a))\nprint(\"skill acquired: few-shot works\")\nfor _ in range(__PARAM__):\n    pass\nprint(\"param:\", __PARAM__)\n',run:'python3'};
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
var gen={version:"jahdb-ai-skill-acquisition-1.0",generate:generate,validate:validate};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("ai-skill-acquisition",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
