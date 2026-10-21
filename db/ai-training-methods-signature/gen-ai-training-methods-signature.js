(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
/* CATS: ["pretraining", "alignment", "efficiency", "data-strategy", "scaling", "regularization"] */
var CATS=["pretraining", "alignment", "efficiency", "data-strategy", "scaling", "regularization"];
var PREFIX='JAH-TRNM-S-';
var FIELDS=["method_type", "complexity", "data_needs"];
/* rows: [category, title, summary, details, ...fields, demoLang, demoTitle, demoProg] */
var B=[
 ["pretraining", "Signature Layering Pretraining", "Signature-authored pretraining schedule: capability layers added in deliberate order, each frozen before the next.", "Signature Layering Pretraining is a JAH-original schedule that trains capabilities as explicit layers: language fluency first, then factual grounding, then reasoning, then tool use — freezing earlier layers' core weights (via adapters) before adding the next. Each layer ships with its own eval gate that must pass before the next layer begins. The design trades some end-to-end optimality for interpretability and rollback: a bad layer can be retrained without touching the others. Labeled Signature throughout.", "pretraining", "high", "Tiered corpora per layer", "python", "Layer gate check", "layers = [(\"fluency\", 0.92), (\"grounding\", 0.88), (\"reasoning\", 0.81)]\ngates = {\"fluency\": 0.90, \"grounding\": 0.85, \"reasoning\": 0.80}\nfor name, score in layers:\n    print(name, \"PASS\" if score >= gates[name] else \"RETRAIN\")"],
 ["alignment", "JAH Progressive Skill Fusion", "Signature-authored method: teach skills one at a time, then fuse with pairwise skill-combination drills.", "JAH Progressive Skill Fusion is a JAH-designed fine-tuning method: each target skill (summarization, code repair, refusal handling) is first taught in isolation to a skill adapter, then adapters are fused while training on combination drills that require two or more skills at once. A skill-interference monitor rolls back fusions that degrade any single skill below its gate. Labeled Signature; an original JAH procedure.", "fine-tuning", "moderate", "Per-skill datasets + combination drills", "python", "Skill gate after fusion", "skills = {\"summarize\": 0.90, \"code_repair\": 0.87}\ngates = {\"summarize\": 0.88, \"code_repair\": 0.85}\nok = all(v >= gates[k] for k, v in skills.items())\nprint(\"fusion accepted:\" if ok else \"fusion rolled back\")"],
 ["alignment", "Signature Honesty Annealing", "Signature-authored alignment schedule: honesty pressure ramps up as capability grows.", "Signature Honesty Annealing is a JAH-original training schedule where the weight on honesty-related preference data starts low and ramps up (anneals in) as model capability grows — the insight being that honesty training is most effective once the model is capable enough to be deceptive. Early phases emphasize capability; late phases emphasize truthfulness under a fixed KL budget. Labeled Signature throughout.", "alignment", "moderate", "Honesty preference pairs + capability data", "python", "Annealing schedule", "steps = 10000\nfor s in [0, 2500, 5000, 7500, 10000]:\n    w = min(1.0, s / steps) ** 2\n    print(f\"step {s:5d}: honesty weight {w:.2f}\")"],
 ["data-strategy", "JAH Capability Ladder Curriculum", "Signature-authored curriculum: every example carries a ladder rank; training climbs the ladder.", "JAH Capability Ladder Curriculum is a JAH-designed data strategy where each training example is tagged ladder_rank 1 (foundational), 2 (compound), or 3 (complex), and the sampler's rank distribution shifts upward on a fixed schedule. Unlike ad-hoc curricula, the ladder is part of the record schema, so any dataset can declare its rungs and any trainer can climb them. Labeled Signature; an original JAH procedure.", "data scheduling", "low", "Ladder-ranked examples", "python", "Ladder sampler schedule", "import random\nrandom.seed(0)\ndef rank_dist(step, total):\n    p = step / total\n    return [max(0.05, 1-p), 0.3, min(0.9, p)]\nfor s in [0, 5000, 10000]:\n    print(s, [round(x, 2) for x in rank_dist(s, 10000)])"],
 ["efficiency", "Signature Drift-Lock Checkpointing", "Signature-authored method: lock checkpoints whose eval fingerprint matches the archive; retrain drifted ones.", "Signature Drift-Lock Checkpointing is a JAH-original training discipline: every N steps, an eval fingerprint (scores on a fixed probe set) is recorded; checkpoints whose fingerprint matches the accepted archive are 'drift-locked' and immutable, while drifted ones trigger investigation before training continues. It turns checkpointing from dumb snapshots into a quality gate. Labeled Signature throughout.", "training discipline", "low", "Fixed probe eval set", "python", "Fingerprint drift check", "probe = {\"qa\": 0.81, \"math\": 0.77}\narchive = {\"qa\": 0.81, \"math\": 0.76}\ndrift = max(abs(probe[k]-archive[k]) for k in probe)\nprint(\"drift:\", drift, \"->\", \"LOCK\" if drift < 0.02 else \"INVESTIGATE\")"],
 ["efficiency", "JAH Teacher-Student Rings", "Signature-authored distillation: concentric rings of students, each teaching the next smaller ring.", "JAH Teacher-Student Rings is a JAH-designed distillation topology: instead of one teacher-to-student jump, models form concentric rings (e.g., 70B teaches 13B teaches 7B teaches 1B), each ring distilling to the next with size-appropriate data difficulty. Smaller rings inherit reasoning traces the teacher could not fit directly into the smallest model. Labeled Signature; an original JAH procedure.", "compression", "moderate", "Distillation data per ring", "python", "Ring size plan", "rings = [70, 13, 7, 1]\nfor big, small in zip(rings, rings[1:]):\n    print(f\"{big}B -> {small}B  (compression {big/small:.1f}x)\")"],
 ["alignment", "Signature Preference Weaving", "Signature-authored method: interleave preference axes so no single axis dominates alignment.", "Signature Preference Weaving is a JAH-original alignment method that trains on helpfulness, honesty, and safety preference data in an interleaved ('woven') schedule rather than sequential phases, with per-axis loss weights rebalanced each epoch by held-out axis scores. The design prevents the classic failure where safety training erases helpfulness. Labeled Signature throughout.", "alignment", "moderate", "Preference data on 3+ axes", "python", "Axis rebalancing", "axes = {\"helpful\": 0.82, \"honest\": 0.75, \"safe\": 0.90}\nworst = min(axes, key=axes.get)\nprint(\"boosting weakest axis:\", worst)"],
 ["scaling", "JAH Sparse Expert Routing", "Signature-authored MoE routing: experts bid for tokens; underused experts get exploration bonuses.", "JAH Sparse Expert Routing is a JAH-designed MoE training method where experts 'bid' for tokens via learned scores, and an exploration bonus routes a fraction of tokens to underused experts so none atrophy. A capacity ledger tracks per-expert utilization, and experts below a floor are merged into neighbors. Labeled Signature; an original JAH procedure.", "pretraining (MoE)", "high", "Same as pretraining", "python", "Expert bidding", "import random\nrandom.seed(3)\nexperts = [{\"id\": i, \"bid\": random.random(), \"use\": random.random()}\n           for i in range(4)]\nfor e in experts:\n    e[\"score\"] = e[\"bid\"] + (0.2 if e[\"use\"] < 0.3 else 0)\nwinner = max(experts, key=lambda e: e[\"score\"])\nprint(\"token -> expert\", winner[\"id\"])"]
];
function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  var cat=opts.category||pick(CATS,rnd);
  var pool=B.filter(function(b){return b[0]===cat;});
  var b=pick(pool.length?pool:B,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  var rec={id:id,title:b[1],t:b[1],g:cat,c:1,summary:b[2],details:b[3]};
  for(var i=0;i<FIELDS.length;i++){rec[FIELDS[i]]=b[4+i];}
  var di=4+FIELDS.length;
  rec.ladder_rank=1+(seed%3);
  rec.demo={language:b[di],title:b[di+1],program:b[di+2]};
  rec.provenance="Signature Systems (JAH)";
  rec.last_verified='2026-10-20';
  rec.src="signature-generated-completion";
  rec._seed=seed;
  return rec;
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!(new RegExp('^'+PREFIX.replace(/[.*+?^${}()|[\]\\]/g,'\\$&')+'\\d{6}$')).test(r.id||''))e.push('id');
  if(typeof r.title!=='string'||!r.title.length)e.push('title');
  if(typeof r.summary!=='string'||!r.summary.length)e.push('summary');
  if(typeof r.details!=='string'||!r.details.length)e.push('details');
  if(CATS.indexOf(r.g)<0)e.push('g');
  for(var i=0;i<FIELDS.length;i++){
    var v=r[FIELDS[i]];
    if(v===undefined||v===null||(typeof v==='string'&&!v.length))e.push('field:'+FIELDS[i]);
  }
  if(!(r.ladder_rank===1||r.ladder_rank===2||r.ladder_rank===3))e.push('ladder_rank');
  var d=r.demo;
  if(!d||typeof d.language!=='string'||!d.language.length||typeof d.title!=='string'||!d.title.length||typeof d.program!=='string'||!d.program.length)e.push('demo');
  if(typeof r.provenance!=='string'||!r.provenance.length)e.push('provenance');
  if(r.last_verified!=='2026-10-20')e.push('last_verified');
  if(r.src!=="signature-generated-completion")e.push('src');
  return {ok:!e.length,errors:e};
}
var gen={version:'jahdb-ai-training-methods-signature-1.0',generate:generate,validate:validate};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('ai-training-methods-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
