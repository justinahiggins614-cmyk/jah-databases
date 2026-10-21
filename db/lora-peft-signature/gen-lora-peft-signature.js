(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
/* CATS: ["low-rank", "quantized", "adapter", "prompt-based", "sparse", "merging"] */
var CATS=["low-rank", "quantized", "adapter", "prompt-based", "sparse", "merging"];
var PREFIX='JAH-LORA-S-';
var FIELDS=["params_trained", "base_compat", "memory_profile", "when_to_use"];
/* rows: [category, title, summary, details, ...fields, demoLang, demoTitle, demoProg] */
var B=[
 ["low-rank", "JAH SlimTune", "Signature-authored PEFT: rank-adaptive LoRA with per-layer rank chosen by sensitivity scan.", "JAH SlimTune is a JAH-designed low-rank method: a quick sensitivity scan assigns each layer its rank (sensitive layers get more), then training proceeds like LoRA with per-layer ranks. The design automates what AdaLoRA does dynamically, upfront and deterministically. Labeled Signature; an original JAH procedure.", "<1% (adaptive ranks)", "Any transformer", "LoRA-level", "Default Signature efficient tune", "python", "Sensitivity scan", "sens = {\"l0\": 0.2, \"l12\": 0.9, \"l23\": 0.7}\nranks = {k: 4 if v < 0.4 else 16 if v < 0.8 else 32 for k, v in sens.items()}\nprint(ranks)"],
 ["low-rank", "Signature RankWeaver", "Signature-authored PEFT: weave two LoRAs (content + style) with learned mixing.", "Signature RankWeaver is a JAH-designed method training two LoRA pairs — one for content/task, one for style/tone — with a learned per-layer mixing coefficient. The design disentangles what the model does from how it sounds. Labeled Signature throughout.", "2x LoRA", "Transformers", "2x LoRA adapters", "Separate content and style control", "python", "Weave mixing", "content_w, style_w = 0.7, 0.3\nprint(f\"layer output = {content_w}*content + {style_w}*style\")"],
 ["quantized", "JAH QuantTune", "Signature-authored PEFT: QLoRA with Signature mixed-precision base and adaptive rank.", "JAH QuantTune is a JAH-designed quantized tuning method: the base uses mixed bit-widths from the Signature sensitivity profile, and adapters use adaptive ranks — QLoRA upgraded with Signature components. The design targets 70B tunes on 24GB GPUs. Labeled Signature; an original JAH procedure.", "<1% adapters; mixed-precision base", "Transformers", "70B on 24GB (target)", "Big models, small GPUs", "python", "Memory target", "print(\"70B mixed-precision base ~35GB -> fits 2x24GB with adapters\")"],
 ["adapter", "Signature AdapterMesh", "Signature-authored PEFT: a mesh of tiny adapters routed per token.", "Signature AdapterMesh is a JAH-designed method: instead of one adapter, a mesh of tiny adapters with a learned router picks adapters per token — like MoE but for PEFT. The design gives multi-skill models without multi-model cost. Labeled Signature throughout.", "Mesh of tiny adapters (~2%)", "Transformers", "Small; router overhead", "Multi-skill single model", "python", "Mesh routing", "import random\nrandom.seed(0)\nadapters = [\"code\", \"math\", \"chat\"]\nprint(\"token ->\", random.choice(adapters))"],
 ["prompt-based", "JAH PromptSeed Tuning", "Signature-authored PEFT: initialize soft prompts from task descriptions, then tune.", "JAH PromptSeed Tuning is a JAH-designed prompt method: soft prompts are initialized from the embedding of a natural-language task description (not random), then fine-tuned — converging faster and higher than random-init prompt tuning. Labeled Signature; an original JAH procedure.", "<0.01%", "Transformers", "Negligible", "Fast prompt-based adaptation", "python", "Seed from description", "desc = \"summarize news articles\"\nprint(\"init soft prompt from embedding of:\", desc[:20], \"...\")"],
 ["sparse", "Signature SparseTune", "Signature-authored PEFT: tune only the weights the task actually moves.", "Signature SparseTune is a JAH-designed method: a probe run identifies the top-k% most-changed weights, then real training updates only those (sparse mask), with periodic re-probing. The design gets full-tuning quality at PEFT cost by following the task's own gradient signal. Labeled Signature throughout.", "Top-k% mask (e.g., 1%)", "Transformers", "Mask + sparse updates", "Task-localized adaptation", "python", "Mask from probe", "import torch\ngrad = torch.randn(10000)\nk = int(0.01 * grad.numel())\nmask = torch.zeros_like(grad, dtype=torch.bool)\nmask[torch.topk(grad.abs(), k).indices] = True\nprint(\"tuning\", mask.sum().item(), \"weights\")"],
 ["sparse", "JAH GradientLite", "Signature-authored optimizer: GaLore-style projection with Signature subspace schedule.", "JAH GradientLite is a JAH-designed memory-efficient optimizer: gradients project to a low-rank subspace on a Signature schedule (subspace refreshes when the projection error exceeds a band), training full parameters at near-PEFT memory. Labeled Signature; an original JAH procedure.", "100% (projected optimizer)", "Transformers", "Near-PEFT", "Full-param training, tight memory", "python", "Subspace refresh check", "proj_err, band = 0.08, 0.05\nprint(\"refresh subspace:\" , proj_err > band)"],
 ["merging", "Signature MergeForge", "Signature-authored merging: forge task adapters into one with conflict resolution.", "Signature MergeForge is a JAH-designed adapter-merging method: task adapters are merged with sign-conflict resolution (TIES-style) plus a validation-weighted blend, producing one multi-task adapter. The design includes a merge report showing per-task retention. Labeled Signature throughout.", "n/a (post-training)", "Same-base adapters", "None extra", "Unite specialist adapters", "python", "Merge report", "retention = {\"qa\": 0.98, \"code\": 0.95, \"chat\": 0.99}\nprint(\"retention:\", retention)"]
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
var gen={version:'jahdb-lora-peft-signature-1.0',generate:generate,validate:validate};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('lora-peft-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
