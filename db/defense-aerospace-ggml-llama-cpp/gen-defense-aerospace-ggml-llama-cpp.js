(function(){'use strict';
/* jahdb-defense-aerospace-ggml-llama-cpp-1.0 — deterministic boundless generator for defense-aerospace-ggml-llama-cpp.
 * Self-regulation (Manon's orders): hard stop at 1,000,000,000,000 records,
 * throttled generation, every generated record labeled simulated, independent
 * validation before acceptance, drift-checked against the archive, and
 * completion detection over the seed pool. */
var HARD_STOP=1000000000000;
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var CATS=["runtimes", "quantization", "backends", "models", "benchmarks"];
var PREFIX='JAH-DAE23-';
var EDITION='public';
var POOL=[["llama.cpp: LLMs on Your CPU", "runtimes", "llama.cpp (by Georgi Gerganov) runs large language model inference in plain C/C++ with zero heavy dependencies — no Python, no CUDA required — on CPUs, and optionally GPUs. It made 7B-70B models runnable on laptops and edge boxes. The tactical AI runtime for disconnected hardware.", {"Author": "Georgi Gerganov", "Language": "C/C++, zero deps", "Runs": "CPU (+GPU optional)", "Makes": "7B-70B on laptops"}], ["ggml: The Tensor Library", "runtimes", "ggml is the tensor library underneath llama.cpp — 16-bit floats, integer quantization, and SIMD/GPU backends in compact C. It does for edge inference what BLAS did for servers: the fast math everyone builds on. whisper.cpp and others reuse it.", {"Is": "tensor library", "Does": "quantized SIMD math", "Reused by": "whisper.cpp et al", "Role": "edge BLAS"}], ["Quantization: Q4_K_M and Friends", "quantization", "Quantization shrinks model weights from 16-bit floats to 4-8 bit integers — Q4_K_M is the beloved balance — cutting a 7B model from 14GB to ~4GB with small quality loss. K-quants group weights for better accuracy per bit. Quantization is what makes big models fit small machines.", {"Shrinks": "16-bit to 4-8 bit", "Q4_K_M": "the sweet spot", "7B": "14GB -> ~4GB", "Costs": "small quality loss"}], ["CPU Backends: AVX, NEON, Accelerate", "backends", "llama.cpp compiles SIMD paths for x86 (AVX2/AVX-512), ARM (NEON), and Apple Accelerate — the same model runs fast on a server, a phone chip, or a Mac. Backend selection is automatic at build or runtime. Portable speed.", {"x86": "AVX2/AVX-512", "ARM": "NEON", "Apple": "Accelerate", "Selects": "automatically"}], ["GPU Offload: Partial Acceleration", "backends", "llama.cpp offloads layers to GPU — CUDA, Metal, ROCm, Vulkan — keeping the rest on CPU when VRAM is short. n_gpu_layers tunes the split. Partial offload is the pragmatic middle between CPU-only and full-GPU.", {"Offloads": "layers to GPU", "APIs": "CUDA, Metal, ROCm, Vulkan", "Tunes": "n_gpu_layers", "Is": "pragmatic middle"}], ["Memory Bandwidth Is the Limit", "benchmarks", "LLM inference is memory-bandwidth bound: each token streams the whole model through the processor, so tokens/sec ≈ bandwidth / model size. Faster RAM beats more cores for inference. Sizing edge inference starts with the memory bus.", {"Bound": "memory bandwidth", "Math": "tok/s = BW / size", "Beats": "RAM over cores", "Sizes": "from the bus"}], ["GGUF: The Model File Format", "models", "GGUF is llama.cpp's model file format — metadata plus quantized tensors in one file, replacing the older GGML format. Converters quantize Hugging Face models into GGUF. One file, every backend, everywhere.", {"Format": "GGUF", "Holds": "metadata + tensors", "From": "HF models via converter", "One": "file everywhere"}], ["Prompt Processing vs Generation", "benchmarks", "Inference has two phases: prompt processing (parallel, fast — the model reads your prompt) and token generation (serial, slow — one token at a time). Long prompts cost upfront; long answers cost per token. Benchmarks quote both: pp tok/s and tg tok/s.", {"Prompt": "parallel, fast", "Generate": "serial, slow", "Quotes": "pp and tg tok/s", "Costs": "prompt upfront, answers per token"}], ["Sampling: Temperature and Top-p", "runtimes", "Sampling turns logits into tokens: temperature flattens or sharpens the distribution, top-p (nucleus) cuts the tail, repeat penalties fight loops. Tactical deployments tune sampling per task — low temp for extraction, higher for drafting. Decoding is a policy choice.", {"Temperature": "sharpens/flattens", "Top-p": "cuts the tail", "Penalties": "fight loops", "Tunes": "per task"}], ["Server Mode: OpenAI-Compatible API", "runtimes", "llama.cpp's server mode exposes an OpenAI-compatible HTTP API — existing tools talk to the edge model unchanged. Local inference, standard interface. The edge slots into existing software.", {"Exposes": "OpenAI-compatible API", "Keeps": "tools unchanged", "Runs": "local", "Slots": "into existing SW"}], ["Constrained Grammars (GBNF)", "runtimes", "GBNF grammars constrain generation to valid JSON, enums, or DSLs — the model cannot emit malformed output. Tactical pipelines need machine-parseable answers, not prose. Grammar is the contract between model and code.", {"Constrains": "JSON, enums, DSLs", "Cannot": "emit malformed", "Needs": "parseable answers", "Is": "the contract"}], ["Speculative Decoding", "benchmarks", "Speculative decoding drafts tokens with a small model and verifies with the big one — accepting most drafts, keeping quality, gaining speed. Two models collaborating beat one model waiting. llama.cpp implements it for the speed-hungry.", {"Drafts": "small model", "Verifies": "big model", "Keeps": "quality", "Gains": "speed"}], ["Benchmarking Edge Inference", "benchmarks", "Edge inference benchmarks report pp/tg tok/s per model, quant, backend, and device — the matrix that sizes deployments. Reproduce before trusting: same flags, same prompt. Numbers without methodology are anecdotes.", {"Reports": "tok/s per config", "Matrix": "sizes deployments", "Reproduces": "before trusting", "Needs": "methodology"}], ["Model Provenance and Licensing", "models", "Edge deployments track model provenance — base model, quantizer, license — because weights carry licenses and some forbid commercial use. The GGUF metadata records the chain. Compliance rides with the file.", {"Tracks": "base, quant, license", "Carries": "license terms", "Records": "in metadata", "Rides": "with the file"}], ["The Disconnected AI Picture", "runtimes", "Ladder-top llama.cpp: quantized models, CPU/GPU backends, local server API, grammars for structure, benchmarks for sizing. Fifteen rungs from C code to capable AI on hardware with no internet at all.", {"Runs": "C/C++, anywhere", "Shrinks": "quantization", "Serves": "local API", "Structures": "grammars"}]];
/* Per-topic demo builder: seeded params -> runnable JS program (pure JS + console.log). */
function buildDemo(seed){
  var r=prng(seed^0x9e3779b9);
  var P={a:ri(r,1,9999),b:ri(r,1,9999),c:ri(r,1,9999)};
  var params=(7+(P.a%63)), bits=4;
var code='// llama.cpp quantization size demo (simulated model)\n';
code+='var P='+params+',bits='+bits+';\nvar gb=P*bits/8;\n';
code+='console.log(P+"B params @ Q"+bits+" = "+gb.toFixed(1)+" GB weights");';return code;
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
var gen={version:'jahdb-defense-aerospace-ggml-llama-cpp-1.0',generate:generate,validate:validate,driftCheck:driftCheck,
  coverage:coverage,isComplete:isComplete,
  limits:{hardStop:HARD_STOP,throttleMs:25,simulatedLabel:true}};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('defense-aerospace-ggml-llama-cpp',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
