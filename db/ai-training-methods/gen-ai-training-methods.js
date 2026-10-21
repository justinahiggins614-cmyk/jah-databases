(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
/* CATS: ["pretraining", "alignment", "efficiency", "data-strategy", "scaling", "regularization"] */
var CATS=["pretraining", "alignment", "efficiency", "data-strategy", "scaling", "regularization"];
var PREFIX='JAH-TRNM-';
var FIELDS=["method_type", "complexity", "data_needs"];
/* rows: [category, title, summary, details, ...fields, demoLang, demoTitle, demoProg] */
var B=[
 ["pretraining", "Causal LM Pretraining", "Train a transformer to predict the next token on raw text — the foundation step behind every base LLM.", "Causal language modeling trains a decoder-only transformer on raw text with a simple objective: given all previous tokens, predict the next one, minimizing cross-entropy loss. No labels are needed, so training scales to trillions of tokens. Architecture, data mixture, and the 6*N*D FLOPs scaling relationship (Kaplan/Chinchilla) determine the outcome. The result is a base model with broad knowledge but no instruction-following behavior — that comes later with fine-tuning.", "pretraining", "very high (thousands of GPU-hours)", "Trillions of tokens of raw text", "python", "Next-token loss on toy logits", "import torch, torch.nn.functional as F\ntorch.manual_seed(0)\nlogits = torch.randn(2, 6, 1000)   # batch, seq, vocab\ntargets = torch.randint(0, 1000, (2, 6))\nloss = F.cross_entropy(logits.reshape(-1, 1000), targets.reshape(-1))\nprint(\"causal LM loss:\", round(float(loss), 3))"],
 ["alignment", "Supervised Fine-Tuning (SFT)", "Fine-tune a base model on instruction-response pairs so it follows instructions.", "SFT takes a pretrained base model and continues training on curated (instruction, response) pairs, computing loss only on the response tokens (prompt tokens are masked with -100). Typical setups use a small learning rate (1e-5 to 2e-5), a few epochs, and packing of short examples. SFT converts a base model into an assistant that follows instructions, but it only imitates the demonstration distribution — it does not learn preferences beyond the demos, which is why RLHF/DPO usually follow.", "fine-tuning", "low-moderate (single GPU to small cluster)", "10K-1M instruction pairs", "python", "Masked SFT loss (prompt masked)", "import torch, torch.nn.functional as F\nlogits = torch.randn(2, 8, 32000)\nlabels = torch.randint(0, 32000, (2, 8))\nlabels[:, :4] = -100  # mask the prompt tokens\nloss = F.cross_entropy(logits.reshape(-1, 32000), labels.reshape(-1),\n                       ignore_index=-100)\nprint(\"SFT loss:\", round(float(loss), 3))"],
 ["alignment", "RLHF with PPO", "Reinforcement learning from human feedback: train a reward model, then optimize the policy with PPO under a KL penalty.", "RLHF has three stages: (1) SFT on demonstrations, (2) train a reward model on human preference pairs (chosen vs rejected), (3) optimize the policy with PPO against the reward model, penalizing KL divergence from the SFT model to prevent reward hacking. PPO's clipped surrogate objective keeps updates stable. RLHF produced ChatGPT's helpful tone, but it is finicky — reward over-optimization and training instability are the classic failure modes.", "alignment", "high (reward model + PPO loop)", "SFT data + 10K-1M preference pairs", "python", "PPO clipped objective sketch", "import torch\nratio = torch.tensor([1.1, 0.9, 1.3])      # pi_new/pi_old\nadv = torch.tensor([0.5, -0.2, 0.8])       # advantages\neps = 0.2\nclipped = torch.clamp(ratio, 1 - eps, 1 + eps)\nloss = -torch.min(ratio * adv, clipped * adv).mean()\nprint(\"PPO loss:\", round(float(loss), 4))"],
 ["alignment", "DPO", "Direct Preference Optimization: align on preference pairs with a simple classification loss — no reward model, no PPO.", "DPO reframes RLHF as supervised learning: given a (prompt, chosen, rejected) triple, it directly increases the log-probability margin of the chosen response over the rejected one, relative to a frozen reference model. The loss is -log sigmoid(beta * margin). DPO is dramatically simpler and more stable than PPO-based RLHF and matches it on many benchmarks, though very large-scale runs sometimes still prefer online RL. Variants (IPO, KTO, ORPO) tweak the objective.", "alignment", "low (SFT-like training)", "10K-1M preference triples", "python", "DPO loss on toy log-probs", "import torch, torch.nn.functional as F\ndef dpo_loss(pi_c, pi_r, ref_c, ref_r, beta=0.1):\n    margin = (pi_c - ref_c) - (pi_r - ref_r)\n    return -F.logsigmoid(beta * margin).mean()\nl = dpo_loss(torch.tensor([-0.5]), torch.tensor([-1.2]),\n             torch.tensor([-0.6]), torch.tensor([-1.0]))\nprint(\"DPO loss:\", round(float(l), 4))"],
 ["alignment", "ORPO", "Odds-Ratio Preference Optimization: SFT and preference alignment in a single stage, no reference model.", "ORPO folds preference alignment into the SFT stage itself: the loss combines standard next-token loss on the chosen response with an odds-ratio penalty that pushes down the rejected response — all without a separate reference model. It is a one-stage, reference-free alternative to the SFT-then-DPO pipeline, attractive when you want alignment in a single training run. Trade-off: it couples imitation and preference learning, which can complicate debugging.", "alignment", "low (single-stage)", "Preference triples (chosen+rejected)", "python", "ORPO odds-ratio term sketch", "import torch, torch.nn.functional as F\nlogp_chosen, logp_rejected = torch.tensor([-0.4]), torch.tensor([-1.5])\nodds_c = torch.exp(logp_chosen) / (1 - torch.exp(logp_chosen) + 1e-9)\nodds_r = torch.exp(logp_rejected) / (1 - torch.exp(logp_rejected) + 1e-9)\nor_loss = -torch.log(torch.sigmoid(torch.log(odds_c / odds_r)))\nprint(\"odds-ratio loss:\", round(float(or_loss), 4))"],
 ["alignment", "KTO", "Kahneman-Tversky Optimization: learn from unpaired good/bad examples using prospect-theory-style loss.", "KTO drops the requirement for paired preferences: it learns from binary feedback (this response was good / bad) using a loss inspired by prospect theory — humans weigh losses more than gains, so the loss is asymmetric around a reference point. This matches real product data (thumbs up/down) far better than paired triples. KTO often matches DPO with cheaper, more abundant data.", "alignment", "low", "Binary good/bad labeled responses (unpaired OK)", "python", "KTO-style asymmetric weighting", "good = [0.8, 0.9, 0.7]   # rewards for liked responses\nbad = [0.2, 0.3]             # rewards for disliked responses\nlam_good, lam_bad = 1.0, 1.5  # losses weigh more (prospect theory)\nscore = lam_good*sum(good)/len(good) - lam_bad*(1-sum(bad)/len(bad))\nprint(\"KTO-style score:\", round(score, 3))"],
 ["efficiency", "Knowledge Distillation", "Train a small student model to mimic a large teacher's outputs or logits.", "In distillation, a large teacher model generates soft targets (logit distributions) or outputs for training inputs, and a smaller student trains to match them — often with a temperature-scaled KL divergence loss mixed with hard-label loss. The student can reach near-teacher quality at a fraction of the size (the recipe behind DistilBERT, TinyLlama-style models, and DeepSeek-R1 distills). Data can be teacher-generated, so the method also distills reasoning traces, not just labels.", "compression", "moderate (needs teacher inference)", "Inputs for the teacher to label (or teacher-generated)", "python", "Temperature-scaled distillation loss", "import torch, torch.nn.functional as F\nT = 2.0\nteacher_logits = torch.randn(4, 100)\nstudent_logits = torch.randn(4, 100)\np = F.softmax(teacher_logits / T, dim=-1)\nq = F.log_softmax(student_logits / T, dim=-1)\nloss = F.kl_div(q, p, reduction=\"batchmean\") * T * T\nprint(\"distill loss:\", round(float(loss), 3))"],
 ["data-strategy", "Curriculum Learning", "Order training examples from easy to hard so the model builds on mastered skills.", "Curriculum learning presents examples in order of increasing difficulty — short sentences before long documents, arithmetic before algebra. The classic implementation scores example difficulty (length, rarity, model loss) and schedules sampling probability over training. It can speed convergence and improve final quality, though modern LLM pretraining often uses implicit curricula (data mixture schedules) rather than explicit per-example ordering.", "data scheduling", "low-moderate", "Difficulty scores or labels per example", "python", "Difficulty-based sampler", "import random\nrandom.seed(0)\nexamples = [(f\"ex{i}\", d) for i, d in enumerate([1, 5, 2, 9, 3, 8])]\nexamples.sort(key=lambda e: e[1])          # easy first\nschedule = examples[:3] + examples          # warm up on easy, then all\nprint(\"first 5 in schedule:\", [e[0] for e in schedule[:5]])"]
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
  rec.provenance="JAH Databases generator (archive-style records)";
  rec.last_verified='2026-10-20';
  rec.src="public-harvest";
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
  if(r.src!=="public-harvest")e.push('src');
  return {ok:!e.length,errors:e};
}
var gen={version:'jahdb-ai-training-methods-1.0',generate:generate,validate:validate};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('ai-training-methods',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
