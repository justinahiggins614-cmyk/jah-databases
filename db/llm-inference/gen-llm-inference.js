(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
/* CATS: ["memory", "scheduling", "parallelism", "decoding", "quantization", "serving-engine"] */
var CATS=["memory", "scheduling", "parallelism", "decoding", "quantization", "serving-engine"];
var PREFIX='JAH-INFER-';
var FIELDS=["technique_type", "benefit", "engines", "complexity"];
/* rows: [category, title, summary, details, ...fields, demoLang, demoTitle, demoProg] */
var B=[
 ["memory", "KV Cache", "Store keys and values from processed tokens so each new token costs O(1) instead of recomputation.", "During generation, the transformer recomputes attention over all previous tokens unless their key/value projections are cached. The KV cache stores K and V per layer per token, turning each decode step into a cheap append-and-attend. Cache size grows linearly with sequence length and batch size — for a 70B model at 32K context it can exceed tens of GB — which is why PagedAttention, quantization, and prefix caching exist. Every serving engine implements it; it is the single most important inference optimization.", "memory optimization", "Turns O(n^2) per-token recompute into O(1) appends", ["vLLM", "TGI", "TensorRT-LLM", "SGLang"], "low (built into engines)", "python", "KV cache size math", "layers, hidden, kv_ratio = 32, 4096, 0.25  # GQA\nbytes_per_token = 2 * layers * hidden * kv_ratio * 2  # K+V, fp16\nfor seq, batch in [(4096, 1), (32768, 8)]:\n    gb = bytes_per_token * seq * batch / 1e9\n    print(f\"seq={seq} batch={batch}: {gb:.1f} GB KV cache\")"],
 ["scheduling", "Continuous Batching", "Batch at the iteration level, not the request level — fill every freed slot the moment it opens.", "Static batching waits for the longest sequence in a batch to finish, wasting GPU on finished requests. Continuous (iteration-level) batching, pioneered by ORCA and popularized by vLLM, inserts new requests into the batch as soon as any slot frees — at each decode iteration. Combined with chunked prefill, it keeps the GPU saturated under bursty traffic and typically multiplies throughput 5-20x over naive batching.", "scheduling", "5-20x throughput via slot-level packing", ["vLLM", "TGI", "SGLang", "TensorRT-LLM"], "moderate (engine feature)", "python", "Static vs continuous batching", "reqs = [10, 50, 30, 20]  # output lengths\nstatic = max(reqs) * len(reqs)\ncont = sum(reqs)\nprint(f\"static token-slots: {static}, continuous: {cont} \"\n      f\"({static/cont:.1f}x waste)\")"],
 ["memory", "PagedAttention", "Manage KV cache in fixed-size blocks like OS virtual memory — kill fragmentation.", "KV caches for variable-length sequences fragment GPU memory badly. PagedAttention (vLLM) splits the cache into fixed blocks allocated on demand and mapped through a block table, like virtual memory pages. Fragmentation drops to near zero, memory sharing across beam-search candidates becomes trivial, and larger batches fit. It is the memory manager inside vLLM and the reason vLLM serves so many concurrent requests.", "memory management", "Near-zero fragmentation; bigger batches", ["vLLM", "SGLang"], "moderate (engine feature)", "python", "Fragmentation without paging", "import random\nrandom.seed(0)\nmem, blocks = 100, []\nfor _ in range(20):\n    need = random.randint(3, 12)\n    blocks.append(need)\nused = sum(blocks)\nprint(f\"requested {used}/100 but worst-fit leaves gaps; \"\n      f\"paged: waste < 1 block per sequence\")"],
 ["decoding", "Speculative Decoding", "Draft tokens with a small model, verify with the big one — same output, much faster.", "Speculative decoding uses a cheap draft model (or the base model's own heads, as in Medusa/EAGLE) to propose K tokens, then the large model verifies them in one forward pass, accepting the matching prefix. Because verification is parallel, accepted tokens cost a fraction of sequential decoding. Typical speedups are 2-3x with identical outputs (it is lossless — the target model's distribution is preserved). Draft quality determines the win.", "decoding algorithm", "2-3x faster, mathematically lossless", ["vLLM", "TGI", "TensorRT-LLM", "SGLang"], "moderate", "python", "Expected speedup from acceptance rate", "draft_cost, verify_cost = 0.15, 1.0  # relative to one target step\nfor accept in [0.5, 0.7, 0.85]:\n    k = 4\n    expected_tokens = sum(accept**i for i in range(k)) + accept**k\n    speedup = expected_tokens / (draft_cost * k + verify_cost)\n    print(f\"accept={accept}: {speedup:.2f}x\")"],
 ["parallelism", "Tensor Parallelism", "Shard each layer's matrices across GPUs so big models fit and run fast.", "Tensor (model) parallelism splits individual layers — typically attention heads and MLP shards — across GPUs within a node, with all-reduce/all-gather at layer boundaries over NVLink. It is how 70B+ models fit across multiple GPUs with low latency: each GPU holds 1/N of the weights. Megatron-LM's column/row-parallel linear layers are the canonical implementation; serving engines configure TP degree to match the NVLink domain (usually 8).", "parallelism", "Fit large models; low-latency sharding", ["vLLM", "TensorRT-LLM", "TGI"], "moderate (config)", "python", "TP memory per GPU", "params_b, tp = 70, 8\nprint(f\"70B fp16 = 140 GB -> {140/tp:.1f} GB/GPU at TP={tp} (+KV cache)\")"],
 ["parallelism", "Pipeline Parallelism", "Put different layers on different GPUs — simple, but mind the pipeline bubbles.", "Pipeline parallelism assigns contiguous layer ranges to each GPU; micro-batches flow through the stages. It needs no fast interconnect between stages (activations only cross stage boundaries), so it suits multi-node serving, but pipeline bubbles idle GPUs when micro-batch counts are low. For inference it is usually combined with tensor parallelism: TP within fast nodes, PP across slower links.", "parallelism", "Scale across nodes without fast fabric", ["vLLM", "TensorRT-LLM", "DeepSpeed-Inference"], "moderate", "python", "Pipeline bubble fraction", "stages, microbatches = 4, 8\nbubble = (stages - 1) / (microbatches + stages - 1)\nprint(f\"bubble idle: {bubble:.1%} (more microbatches -> smaller)\")"],
 ["quantization", "AWQ Quantization", "Activation-aware 4-bit weight quantization — near-FP16 quality, ~4x smaller weights.", "AWQ (Activation-aware Weight Quantization) observes that a few salient weight channels matter far more; it scales those channels up before quantizing weights to INT4, protecting them from quantization error. The result: 4-bit weights with minimal perplexity loss, no retraining, and fast INT4 kernels. It is a top choice for serving 70B-class models on limited GPUs.", "quantization", "~4x smaller weights, minimal quality loss", ["vLLM", "TGI", "TensorRT-LLM", "llama.cpp"], "low (one-time quant)", "python", "Weight memory: fp16 vs INT4", "params = 70e9\nfor name, b in [(\"fp16\", 2), (\"int4\", 0.5)]:\n    print(f\"{name}: {params*b/1e9:.0f} GB weights\")"],
 ["quantization", "GPTQ Quantization", "Layer-wise 4-bit quantization using approximate second-order information.", "GPTQ quantizes weights layer by layer, using inverse-Hessian information to choose rounding that minimizes layer-output error, processing columns in order with error compensation. One-shot (no retraining), fast to apply, and supported everywhere — GPTQ was the first widely used 4-bit format for LLM serving and remains a baseline every new quant method is compared against.", "quantization", "One-shot 4-bit with strong quality", ["vLLM", "TGI", "llama.cpp", "ExLlamaV2"], "low (one-time quant)", "python", "Quantization error sketch", "import torch\nw = torch.randn(1000)\nq = (torch.round(w * 8) / 8)  # fake 4-bit-ish\nprint(\"mse:\", round(float(((w - q)**2).mean()), 5))"]
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
var gen={version:'jahdb-llm-inference-1.0',generate:generate,validate:validate};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('llm-inference',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
