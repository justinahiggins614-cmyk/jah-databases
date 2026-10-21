(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
/* CATS: ["low-rank", "quantized", "adapter", "prompt-based", "sparse", "merging"] */
var CATS=["low-rank", "quantized", "adapter", "prompt-based", "sparse", "merging"];
var PREFIX='JAH-LORA-';
var FIELDS=["params_trained", "base_compat", "memory_profile", "when_to_use"];
/* rows: [category, title, summary, details, ...fields, demoLang, demoTitle, demoProg] */
var B=[
 ["low-rank", "LoRA", "Low-Rank Adaptation: freeze the model, train small rank-decomposition matrices — the PEFT method that started it all.", "LoRA freezes pretrained weights W and learns a low-rank update ΔW = BA (B: d×r, A: r×k, r << d), added at inference with zero latency overhead (matrices can be merged). With r=8-64, trainable parameters drop to <1% while matching full fine-tuning on many tasks. Adapters are tiny, swappable, and composable — the foundation of the PEFT ecosystem (Hugging Face PEFT library).", "<1% (rank r=8-64)", "Any transformer (attention + MLP)", "Base in fp16 + tiny adapters; fits 7B on 24GB", "Default choice for efficient fine-tuning", "python", "LoRA reparameterization", "import torch\nd, r, k = 4096, 8, 4096\nW = torch.randn(d, k); A = torch.randn(r, k) * 0.01; B = torch.zeros(d, r)\nW_eff = W + (B @ A) * (16 / r)\nprint(f\"trainable {A.numel()+B.numel():,} vs full {W.numel():,} \"\n      f\"({(A.numel()+B.numel())/W.numel():.2%})\")"],
 ["quantized", "QLoRA", "LoRA on a 4-bit quantized base model: fine-tune 65B models on a single 48GB GPU.", "QLoRA combines 4-bit NormalFloat quantization of the frozen base with LoRA adapters, plus paged optimizers and double quantization. The landmark result: fine-tuning a 65B model on one 48GB GPU with quality near full fine-tuning. It democratized large-model fine-tuning overnight; bitsandbytes provides the 4-bit kernels.", "<1% adapters; base in 4-bit", "Any transformer", "65B on 48GB; 7B on ~8GB", "Big models on limited GPUs", "python", "QLoRA memory math", "params_b = 65\nprint(f\"65B: fp16 {params_b*2}GB -> NF4 {params_b*0.5:.0f}GB + adapters/optimizer\")"],
 ["low-rank", "LoHa", "Hadamard-product low-rank adaptation: more expressive updates per parameter than LoRA.", "LoHa (from the LyCORIS project) replaces LoRA's single low-rank product with the Hadamard (element-wise) product of two low-rank matrices: ΔW = (B1A1) ⊙ (B2A2). The element-wise product creates higher-rank effective updates from the same parameter budget, often beating LoRA on style/subject learning (its diffusion-model origins). Same drop-in usage as LoRA.", "~2x LoRA params, higher effective rank", "Transformers + diffusion models", "Like LoRA, slightly more", "When LoRA underfits the style/task", "python", "LoHa effective rank", "import torch\nr, d = 8, 256\nA1, B1 = torch.randn(r, d), torch.randn(d, r)\nA2, B2 = torch.randn(r, d), torch.randn(d, r)\ndW = (B1 @ A1) * (B2 @ A2)\nprint(\"effective rank:\", torch.linalg.matrix_rank(dW).item(), f\"(r={r} each)\")"],
 ["low-rank", "LoKr", "Kronecker-product adaptation: big effective updates from tiny factor matrices.", "LoKr (LyCORIS) builds ΔW as the Kronecker product of two small matrices: ΔW = B ⊗ A. The Kronecker structure yields very high-rank updates from few parameters — parameter efficiency beyond LoRA/LoHa. Best for cases needing large-capacity adaptation on a tight budget; tuning the factor shapes matters.", "Fewer than LoRA for same effective rank", "Transformers + diffusion", "Minimal", "Maximum capacity per parameter", "python", "Kronecker expansion", "import torch\nA, B = torch.randn(4, 8), torch.randn(8, 4)\ndW = torch.kron(B, A)\nprint(f\"factors {A.numel()+B.numel()} params -> {dW.numel()} update params\")"],
 ["low-rank", "AdaLoRA", "Adaptive budget allocation: give more rank to important layers, less to unimportant ones.", "AdaLoRA parameterizes updates via SVD-like decomposition and adaptively prunes singular values by importance scores during training — important layers keep high rank, unimportant ones shrink. Same total budget as LoRA, better used. Particularly effective when you do not know which layers matter for your task.", "Same budget as LoRA, adaptively allocated", "Transformers", "Like LoRA + importance overhead", "Unknown layer importance; fixed budget", "python", "Rank allocation by importance", "importance = {\"attn\": 0.9, \"mlp\": 0.5, \"embed\": 0.1}\nbudget = 64\nalloc = {k: max(2, int(budget * v / sum(importance.values()))) for k, v in importance.items()}\nprint(\"rank allocation:\", alloc)"],
 ["low-rank", "DoRA", "Weight-Decomposed Low-Rank Adaptation: separate magnitude and direction for fuller fine-tuning.", "DoRA decomposes each weight into magnitude and direction components, applying LoRA-style updates to the direction while learning magnitudes separately. This mimics full fine-tuning's learning pattern more closely than LoRA and consistently outperforms it, at modest extra cost (magnitude vector). A strong default upgrade over vanilla LoRA.", "LoRA params + magnitude vector", "Transformers", "Slightly above LoRA", "When LoRA quality is not quite enough", "python", "DoRA decomposition", "import torch\nW = torch.randn(256, 256)\nmag = W.norm(dim=1, keepdim=True)\ndirection = W / mag\nprint(\"magnitude shape:\", tuple(mag.shape), \"| direction unit-norm:\",\n      bool(torch.allclose(direction.norm(dim=1), torch.ones(256), atol=1e-5)))"],
 ["adapter", "Houlsby Adapters", "The original adapters: small bottleneck MLPs inserted between transformer layers.", "Houlsby adapters (2019) insert bottleneck feed-forward modules (down-project, nonlinearity, up-project) after attention and FFN sublayers, training only the adapters. They launched the PEFT field and remain competitive; unlike LoRA they add inference latency (extra layers), but their modularity suits multi-task setups where adapters swap per task.", "~2-4% (bottleneck size dependent)", "Transformers", "Small; adds latency at inference", "Multi-task adapter swapping", "python", "Adapter bottleneck", "import torch, torch.nn as nn\nad = nn.Sequential(nn.Linear(768, 64), nn.ReLU(), nn.Linear(64, 768))\nx = torch.randn(2, 10, 768)\nprint(\"adapter params:\", sum(p.numel() for p in ad.parameters()))"],
 ["prompt-based", "Prefix Tuning", "Learn continuous prefix vectors prepended to keys/values — the model stays frozen.", "Prefix tuning prepends learned continuous vectors to the keys and values at every layer (a reparameterized MLP generates them for stability). Only ~0.1% parameters train. It matches full fine-tuning on generation tasks with tiny storage per task — but optimization is trickier than LoRA, and it adds prefix length to every forward pass.", "~0.1% (prefix vectors)", "Transformers (esp. generation)", "Tiny; longer effective sequences", "Many tasks, tiny storage each", "python", "Prefix shapes", "layers, prefix_len, hidden = 12, 20, 768\nprint(f\"prefix params: {2*layers*prefix_len*hidden:,} \"\n      f\"({2*layers*prefix_len*hidden/110e6:.2%} of 110M)\")"]
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
var gen={version:'jahdb-lora-peft-1.0',generate:generate,validate:validate};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('lora-peft',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
