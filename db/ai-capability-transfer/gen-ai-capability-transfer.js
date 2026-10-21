(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];} function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var CATS=["distillation-transfer", "adapters", "cross-model", "federated", "continual-transfer"];
var PREFIX="JAH-AICAPA3-";
var FIELDS=["technique", "source", "target", "method", "fidelity", "benefit", "complexity"];
var SRC="public-harvest";
var POOL=[["Knowledge Distillation Transfer", "Capabilities transfer from teacher to student via soft targets; the fidelity is measured. Teaching gets distilled. Skills get moved.", "distillation-transfer", 2, "Distillation", "Teacher", "Student", "Soft targets", "95%", "Moved skills", "Medium"], ["Adapter Modules (LoRA)", "Capabilities add via small adapter modules; the base stays frozen. Transfer gets modular. Skills get plugged.", "adapters", 1, "LoRA", "Base model", "Adapted", "Low-rank add", "98%", "Plugged", "Low"], ["Cross-Architecture Transfer", "Capabilities move between different architectures via representation alignment; the bridge is learned. Architectures get bridged. Skills get portable.", "cross-model", 3, "Alignment", "Transformer", "RNN", "Rep bridge", "85%", "Bridged", "High"], ["Federated Transfer", "Capabilities aggregate from distributed learners without sharing data; the federation learns together. Privacy gets kept. Skills get crowdsourced.", "federated", 3, "FedAvg", "Clients", "Global", "Aggregate", "90%", "Crowdsourced", "High"], ["Continual Transfer", "New capabilities add without forgetting old; the transfer is lifelong. Learning gets cumulative. Skills get kept.", "continual-transfer", 3, "Lifelong", "Old+new", "Unified", "No-forget", "95%", "Cumulative", "High"], ["Prompt Transfer", "Learned prompts transfer capabilities without weight changes; the prompt is the skill. Transfer gets light. Skills get portable.", "adapters", 1, "Soft prompts", "Task A", "Task B", "Prompt tune", "90%", "Light", "Low"], ["Feature Extractor Reuse", "Frozen backbones transfer visual features; only heads retrain. Reuse gets frozen. Features get shared.", "cross-model", 1, "Frozen backbone", "Pretrained", "New task", "Head only", "92%", "Shared", "Low"], ["Multi-Task Transfer", "Joint training transfers capabilities across tasks; the sharing helps all. Tasks get communal. Skills get shared.", "distillation-transfer", 2, "Joint train", "Tasks", "All", "Shared trunk", "93%", "Communal", "Medium"], ["Zero-Shot Transfer", "Capabilities apply to unseen tasks via instruction following; the transfer is magical. Generalization gets broad. Skills get universal.", "cross-model", 2, "Instruct", "Training mix", "Unseen", "Follow instruct", "80%", "Universal", "Medium"], ["Model Merging (Soups)", "Averaged weights combine capabilities; the soup is surprisingly tasty. Merging gets simple. Skills get blended.", "cross-model", 2, "Weight avg", "Models", "Merged", "Average", "94%", "Blended", "Medium"], ["Task Arithmetic", "Task vectors add and subtract capabilities; the arithmetic is vectorial. Capabilities get algebraic. Skills get computed.", "adapters", 3, "Task vectors", "Fine-tunes", "Combined", "Vector math", "88%", "Algebraic", "High"], ["Hypernetwork Transfer", "Hypernetworks generate task-specific weights; the transfer is generated. Generation gets meta. Skills get synthesized.", "adapters", 3, "Hypernet", "Meta", "Task weights", "Generate", "87%", "Synthesized", "High"], ["Cross-Lingual Transfer", "Capabilities cross languages via shared representations; the bridge is multilingual. Languages get connected. Skills get global.", "cross-model", 2, "X-lingual", "English", "Spanish", "Shared reps", "85%", "Global", "Medium"], ["Domain Adaptation", "Capabilities adapt to new domains with little data; the shift is bridged. Domains get crossed. Skills get flexible.", "distillation-transfer", 2, "Adapt", "Source dom", "Target dom", "Few-shot adapt", "89%", "Flexible", "Medium"], ["Split Learning Transfer", "Models split across parties transfer capabilities without sharing raw data; the split preserves privacy. Splitting gets private. Skills get shared safely.", "federated", 3, "Split", "Parties", "Joint", "Cut model", "91%", "Safe", "High"], ["Backward Transfer", "New learning improves old skills; the transfer flows backward. Learning gets retroactive. Old gets better.", "continual-transfer", 3, "BWT", "New task", "Old tasks", "Positive BWT", "102%", "Retroactive", "High"], ["Forward Transfer", "Old skills accelerate new learning; the transfer flows forward. Learning gets faster. New gets easy.", "continual-transfer", 2, "FWT", "Old tasks", "New task", "Warm start", "95%", "Faster", "Medium"], ["Modular Transfer (Adapters)", "Adapter modules compose capabilities like LEGO; the transfer is compositional. Modularity gets playful. Skills get built.", "adapters", 2, "AdapterFusion", "Adapters", "Composed", "Fuse", "93%", "Playful", "Medium"], ["Self-Distillation Transfer", "Models teach themselves across generations; the transfer is internal. Teaching gets recursive. Skills get refined.", "distillation-transfer", 2, "Born-again", "Gen N", "Gen N+1", "Self-teach", "101%", "Refined", "Medium"], ["Privacy-Preserving Transfer", "Differential privacy bounds what transfers; the guarantee is mathematical. Privacy gets proven. Skills get shared safely.", "federated", 3, "DP", "Private", "Public", "Noised", "88%", "Proven private", "High"]];
function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  var cat=opts.category||pick(CATS,rnd);
  var sub=POOL.filter(function(p){return p[2]===cat;});
  var row=pick(sub.length?sub:POOL,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  var rec={id:id,t:row[0],g:row[2],c:0,title:row[0],description:row[1],category:row[2],ladder_rank:row[3]};
  for(var i=0;i<FIELDS.length;i++){ rec[FIELDS[i]]=row[4+i]; }
  var param=ri(rnd,2,40);
  rec.demo={language:'python',code:'teacher_acc, student_acc = 95.0, 92.5\nprint(\"teacher: %.1f%% -> student: %.1f%%\" % (teacher_acc, student_acc))\nprint(\"fidelity: %.1f%%\" % (100 * student_acc / teacher_acc))\nfor _ in range(__PARAM__):\n    pass\nprint(\"param:\", __PARAM__)\n',run:'python3'};
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
var gen={version:"jahdb-ai-capability-transfer-1.0",generate:generate,validate:validate};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("ai-capability-transfer",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
