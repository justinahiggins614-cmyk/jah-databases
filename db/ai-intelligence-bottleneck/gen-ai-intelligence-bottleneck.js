(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];} function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var CATS=["data-bottlenecks", "compute-bottlenecks", "memory-bottlenecks", "reasoning-bottlenecks", "system-bottlenecks"];
var PREFIX="JAH-AIB-";
var FIELDS=["technique", "bottleneck", "method", "measure", "benefit", "complexity"];
var SRC="public-harvest";
var POOL=[["Data Loading Bottleneck", "GPUs starve when data loading lags; the fix is parallel loaders and prefetching. Starvation gets fed. Throughput gets restored.", "data-bottlenecks", 1, "Parallel load", "Data pipeline", "Workers + prefetch", "GPU util", "Fed GPUs", "Low"], ["Compute Bottleneck Profiling", "Profiling finds the compute-bound kernels; the roofline says what's possible. Bottlenecks get profiled. Limits get known.", "compute-bottlenecks", 2, "Roofline", "Kernels", "Profile + model", "% of roof", "Known limits", "Medium"], ["Memory Bandwidth Bottleneck", "Memory-bound ops need fewer bytes, not more FLOPS: quantization and fusion help. Bytes get budgeted. Bandwidth gets respected.", "memory-bottlenecks", 2, "Byte budget", "Bandwidth", "Quant + fuse", "GB/s", "Respected", "Medium"], ["KV Cache Bottleneck", "Long contexts bottleneck on KV cache size and bandwidth; paging and compression widen it. Caches get paged. Contexts get long.", "memory-bottlenecks", 3, "Paged KV", "KV cache", "Paging", "Max tokens", "Long contexts", "High"], ["Attention Quadratic Bottleneck", "Attention's O(n²) limits sequence length; sparse and linear attention widen it. Quadratics get tamed. Sequences get long.", "compute-bottlenecks", 3, "Sparse attn", "O(n^2)", "Sparsify", "Max length", "Tamed", "High"], ["Reasoning Depth Bottleneck", "Deep reasoning needs many sequential steps; the bottleneck is latency, not FLOPS. Depth gets distilled. Thinking gets fast.", "reasoning-bottlenecks", 2, "Distill depth", "Sequential steps", "Distillation", "Steps", "Fast thinking", "Medium"], ["Communication Bottleneck", "Distributed training bottlenecks on all-reduce bandwidth; compression and overlap widen it. Networks get respected. Scaling gets linear.", "system-bottlenecks", 3, "Compress comm", "All-reduce", "Quant + overlap", "Scaling eff", "Linear scaling", "High"], ["I/O Bottleneck in Training", "Checkpointing stalls training; async checkpoints hide the I/O. Stalls get hidden. Training gets smooth.", "data-bottlenecks", 2, "Async ckpt", "Checkpoint I/O", "Background save", "Stall time", "Smooth", "Medium"], ["Token Generation Bottleneck", "Autoregressive decoding is memory-bandwidth bound; speculative decoding widens it. Bandwidth gets drafted. Generation gets fast.", "compute-bottlenecks", 3, "Spec decode", "Decode BW", "Draft+verify", "tok/s", "Fast gen", "High"], ["Embedding Table Bottleneck", "Huge embeddings bottleneck on memory; sharding and quantization widen it. Tables get sharded. Memory gets managed.", "memory-bottlenecks", 2, "Shard+quant", "Embeddings", "Distribute", "Table size", "Managed", "Medium"], ["Cold Start Bottleneck", "Model loading delays first inference; the bottleneck is I/O and init. Starts get warm. Latency gets hidden.", "system-bottlenecks", 1, "Warm pool", "Load time", "Preload", "First token", "Warm", "Low"], ["Context Window Bottleneck", "Fixed windows limit what the model sees; retrieval and summarization widen it. Windows get extended. Sight gets far.", "reasoning-bottlenecks", 2, "RAG extend", "Window", "Retrieve", "Effective ctx", "Far sight", "Medium"], ["Precision Bottleneck", "FP32 wastes bandwidth where FP16 suffices; mixed precision widens it. Precision gets fitted. Bandwidth gets doubled.", "compute-bottlenecks", 1, "Mixed precision", "Bandwidth", "FP16", "GB/s used", "Doubled", "Low"], ["Synchronization Bottleneck", "Barriers serialize distributed workers; async methods widen it. Barriers get removed. Workers get free.", "system-bottlenecks", 3, "Async SGD", "Barriers", "No sync", "Idle time", "Free workers", "High"], ["Label Bottleneck", "Human labels limit supervised learning; weak supervision and pretraining widen it. Labels get multiplied. Learning gets data.", "data-bottlenecks", 2, "Weak sup", "Labels", "Programmatic", "Label count", "Multiplied", "Medium"], ["Inference Batching Bottleneck", "One-by-one inference wastes GPUs; continuous batching widens throughput. Batching gets continuous. GPUs get fed.", "system-bottlenecks", 2, "Cont batch", "Throughput", "Batch always", "tok/s/GPU", "Fed GPUs", "Medium"], ["Gradient Bottleneck", "Huge models bottleneck on gradient communication; the fix is sharding (ZeRO). Gradients get sharded. Memory gets shared.", "memory-bottlenecks", 3, "ZeRO", "Gradients", "Shard all", "Mem/GPU", "Shared", "High"], ["Exploration Bottleneck (RL)", "RL bottlenecks on sample efficiency; the fix is better exploration and models. Samples get precious. Learning gets efficient.", "reasoning-bottlenecks", 3, "Model-based", "Samples", "Learn model", "Samples", "Precious", "High"], ["Serving Tail Bottleneck", "P99 latency bottlenecks on the slowest shard; hedging and timeouts widen it. Tails get tamed. Latency gets predictable.", "system-bottlenecks", 2, "Hedging", "Tail", "Backup requests", "p99", "Tamed", "Medium"], ["Energy Bottleneck", "Power limits throttle compute; the fix is efficiency (fewer joules per token). Joules get budgeted. Compute gets efficient.", "compute-bottlenecks", 2, "Efficiency", "Power", "Joules/token", "W", "Budgeted", "Medium"]];
function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  var cat=opts.category||pick(CATS,rnd);
  var sub=POOL.filter(function(p){return p[2]===cat;});
  var row=pick(sub.length?sub:POOL,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  var rec={id:id,t:row[0],g:row[2],c:0,title:row[0],description:row[1],category:row[2],ladder_rank:row[3]};
  for(var i=0;i<FIELDS.length;i++){ rec[FIELDS[i]]=row[4+i]; }
  var param=ri(rnd,2,40);
  rec.demo={language:'python',code:'stages = [(\"data\", 40), (\"compute\", 120), (\"memory\", 25)]\nslowest = max(stages, key=lambda x: x[1])\nprint(\"pipeline stages:\", stages)\nprint(\"bottleneck:\", slowest[0], \"(%dms)\" % slowest[1])\nprint(\"widen it first\")\nfor _ in range(__PARAM__):\n    pass\nprint(\"param:\", __PARAM__)\n',run:'python3'};
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
var gen={version:"jahdb-ai-intelligence-bottleneck-1.0",generate:generate,validate:validate};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("ai-intelligence-bottleneck",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
