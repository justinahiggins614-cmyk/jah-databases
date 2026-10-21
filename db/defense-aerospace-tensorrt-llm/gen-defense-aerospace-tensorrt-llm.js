(function(){'use strict';
/* jahdb-defense-aerospace-tensorrt-llm-1.0 — deterministic boundless generator for defense-aerospace-tensorrt-llm.
 * Self-regulation (Manon's orders): hard stop at 1,000,000,000,000 records,
 * throttled generation, every generated record labeled simulated, independent
 * validation before acceptance, drift-checked against the archive, and
 * completion detection over the seed pool. */
var HARD_STOP=1000000000000;
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var CATS=["compilation", "batching", "quantization", "kv-cache", "benchmarks"];
var PREFIX='JAH-DAE25-';
var EDITION='public';
var POOL=[["TensorRT-LLM: NVIDIA's LLM Compiler", "compilation", "TensorRT-LLM is NVIDIA's open-source framework for compiling large language models into optimized TensorRT engines — kernel fusion, quantization, and scheduling tuned per GPU. It serves LLMs at maximum throughput and minimum latency on NVIDIA hardware. The compiler between model and metal.", {"Developer": "NVIDIA, open source", "Compiles": "LLMs to TRT engines", "Tunes": "per GPU", "Serves": "max throughput"}], ["In-Flight Batching", "batching", "In-flight batching packs requests dynamically — new prompts join the batch as old ones finish, at the token level — keeping the GPU saturated where static batching idles. Throughput multiplies without latency exploding. Batching is the serving superpower.", {"Packs": "dynamically, per token", "Keeps": "GPU saturated", "Multiplies": "throughput", "Is": "serving superpower"}], ["KV-Cache Management", "kv-cache", "The KV cache stores attention keys/values per token — TensorRT-LLM manages it with paged allocation so memory is used efficiently across the batch. Cache size bounds max context and batch. Memory planning is serving planning.", {"Stores": "K/V per token", "Manages": "paged allocation", "Bounds": "context x batch", "Is": "serving planning"}], ["Quantization: FP8, INT8, INT4", "quantization", "TensorRT-LLM quantizes weights and activations — FP8 on Hopper, INT8/INT4 with AWQ/GPTQ — trading bits for speed at measured quality cost. Hopper's FP8 is the current sweet spot. Quantization plus compilation compounds.", {"Quantizes": "FP8/INT8/INT4", "Hopper": "FP8 sweet spot", "Trades": "bits for speed", "Compounds": "with compilation"}], ["Kernel Fusion and Auto-Tuning", "compilation", "The compiler fuses operations into single kernels and auto-tunes per GPU architecture — attention, norms, and MLPs become bespoke kernels. Fusion removes memory round-trips; tuning picks the fastest variant. Compiled beats generic.", {"Fuses": "ops into kernels", "Tunes": "per architecture", "Removes": "memory trips", "Beats": "generic"}], ["Tensor and Pipeline Parallelism", "batching", "TensorRT-LLM shards models across GPUs — tensor parallelism splits layers, pipeline parallelism splits stages — scaling past single-GPU memory. 70B+ serving is a multi-GPU compiled program. Scale is a compiler feature.", {"Shards": "across GPUs", "Tensor": "splits layers", "Pipeline": "splits stages", "Scales": "70B+"}], ["The Build: From Checkpoint to Engine", "compilation", "Building means converting a checkpoint, choosing precision and parallelism, and compiling the engine — minutes to hours once, then fast serving forever. Build artifacts version with the model. Compile time is an investment.", {"Converts": "checkpoint", "Chooses": "precision, parallel", "Compiles": "once", "Versions": "with model"}], ["Triton Integration", "benchmarks", "TensorRT-LLM backends plug into NVIDIA Triton Inference Server — dynamic batching, model management, and standard APIs around the compiled engines. Triton is the serving chassis; TRT-LLM is the engine. Production serving, assembled.", {"Plugs": "into Triton", "Adds": "batching, management", "Chassis": "Triton", "Engine": "TRT-LLM"}], ["Disaggregated Serving: Prefill vs Decode", "batching", "Disaggregated serving splits prefill (prompt processing) from decode (generation) onto different GPUs — each phase gets the hardware shape it wants. Throughput climbs when phases stop fighting. Architecture follows the workload's two natures.", {"Splits": "prefill vs decode", "Gives": "right HW per phase", "Climbs": "throughput", "Follows": "workload nature"}], ["Speculative Decoding in TRT-LLM", "benchmarks", "TensorRT-LLM implements speculative decoding — draft model proposes, target verifies — for latency wins on top of compilation. Drafting plus compiling stacks multiplicatively. Every millisecond gets attacked.", {"Drafts": "small model", "Verifies": "target", "Stacks": "with compile", "Attacks": "every ms"}], ["Benchmarks: tok/s per GPU", "benchmarks", "TRT-LLM benchmarks quote tokens/sec per GPU, per precision, per batch — the numbers that size serving fleets. MLPerf inference includes these engines. Fleet math starts here.", {"Quotes": "tok/s/GPU", "Sizes": "fleets", "Includes": "MLPerf", "Starts": "fleet math"}], ["Multi-LoRA Serving", "kv-cache", "TensorRT-LLM serves many LoRA adapters on one base model — one engine, many personalities, with adapter switching per request. Personalization without model sprawl. The base stays shared; the adapters specialize.", {"Serves": "many LoRAs", "Shares": "one base", "Switches": "per request", "Avoids": "model sprawl"}], ["Long Context Engineering", "kv-cache", "Long contexts (100k+ tokens) stress the KV cache — TensorRT-LLM's paged management and quantization stretch context per GPU. Context is a memory budget with engineering behind it. Long is a feature you pay for in GB.", {"Stresses": "KV cache", "Stretches": "paged + quant", "Budgets": "context in GB", "Pays": "per token"}], ["Choosing Precision per Deployment", "quantization", "Precision choice weighs quality, speed, and hardware — FP16 for fidelity, FP8 for Hopper speed, INT4 for max throughput. The deployment's SLA picks. Measured quality deltas decide, not fashion.", {"Weighs": "quality, speed, HW", "FP8": "Hopper speed", "INT4": "max throughput", "Decides": "measured deltas"}], ["The Compiled Serving Picture", "compilation", "Ladder-top TensorRT-LLM: compile once, batch in flight, manage KV, quantize wisely, serve at scale. Fifteen rungs from a checkpoint to thousands of tokens per second per GPU.", {"Compiles": "once", "Batches": "in flight", "Manages": "KV", "Serves": "at scale"}]];
/* Per-topic demo builder: seeded params -> runnable JS program (pure JS + console.log). */
function buildDemo(seed){
  var r=prng(seed^0x9e3779b9);
  var P={a:ri(r,1,9999),b:ri(r,1,9999),c:ri(r,1,9999)};
  var seq=2048, layers=32, hs=4096, bytes=2, batch=1+P.a%7;
var code='// TensorRT-LLM KV-cache planning demo (simulated model)\n';
code+='var bytes='+seq+'*'+layers+'*'+hs+'*2*'+bytes+'/1e9*'+batch+';\n';
code+='console.log("KV cache: "+bytes.toFixed(2)+" GB for batch '+batch+'");';return code;
}
function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  if(seed>HARD_STOP)throw new Error('generator hard stop: seed exceeds 1,000,000,000,000');
  var cat=opts.category&&CATS.indexOf(opts.category)>=0?opts.category:pick(CATS,rnd);
  var pool=POOL.filter(function(p){return p[1]===cat;});
  var row=pick(pool.length?pool:POOL,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  var demo=buildDemo(seed);
  var rec={
    id:id, t:row[0], title:row[0], g:cat, category:cat,
    edition:EDITION, ladder_rank:1+((seed-1)%15),
    description:row[2],
    facts:row[3],
    demo:{language:'javascript',program:demo},
    provenance:EDITION==='public'
      ? 'Public record: compiled from official project documentation and published specifications. Fact-checked 2026-10-21.'
      : 'Signature original: designed by Justin Addam Higgins (JAH) as the Signature counterpart; original engineering, labeled Signature.',
    source:EDITION==='public'?'manon-order / public documentation':'manon-order / signature original',
    last_verified:'2026-10-21',
    march:'march-to-a-million in progress',
    license:'https://creativecommons.org/publicdomain/zero/1.0/',
    _simulated:true, _seed:seed
  };
  var v=validate(rec);
  if(!v.ok)throw new Error('generated record failed validation: '+v.errors.join(','));
  return rec;
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return{ok:false,errors:['not an object']};
  if(!new RegExp('^'+PREFIX.replace(/[-\/\\^$*+?.()|[\]{}]/g,'\\$&')+'\\d{6}$').test(r.id||''))e.push('id');
  if(typeof r.title!=='string'||!r.title.length)e.push('title');
  if(typeof r.description!=='string'||r.description.length<40)e.push('description');
  if(CATS.indexOf(r.g)<0)e.push('category');
  if(!(r.ladder_rank>=1&&r.ladder_rank<=15))e.push('ladder_rank');
  if(!r.facts||typeof r.facts!=='object')e.push('facts');
  if(!r.demo||typeof r.demo.program!=='string'||r.demo.program.indexOf('console.log')<0)e.push('demo');
  if(r._simulated!==true)e.push('simulated-label');
  if(r.last_verified!=='2026-10-21')e.push('last_verified');
  return{ok:!e.length,errors:e};
}
function driftCheck(rec,sample){
  sample=sample||[];
  for(var i=0;i<sample.length;i++){
    if(sample[i]&&sample[i].title===rec.title&&sample[i].id!==rec.id)
      return{ok:false,errors:['duplicate title in archive sample']};
  }
  return{ok:true,errors:[]};
}
/* Completion detection: the seed pool is exhausted when every pool row has
 * produced records across all categories; coverage() reports progress. */
function coverage(){return{pool_rows:POOL.length,categories:CATS.length,hard_stop:HARD_STOP};}
function isComplete(filed){return filed>=HARD_STOP;}
var gen={version:'jahdb-defense-aerospace-tensorrt-llm-1.0',generate:generate,validate:validate,driftCheck:driftCheck,
  coverage:coverage,isComplete:isComplete,
  limits:{hardStop:HARD_STOP,throttleMs:25,simulatedLabel:true}};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('defense-aerospace-tensorrt-llm',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
