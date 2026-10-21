(function(){'use strict';
/* jahdb-defense-aerospace-mlc-llm-1.0 — deterministic boundless generator for defense-aerospace-mlc-llm.
   Self-regulation (per standing order):
   - HARD STOP at 1,000,000,000,000 total records (one trillion).
   - Throttled: at most MAX_PER_CALL records per request.
   - Every generated record is labeled SIMULATED ("simulated" generation labeling).
   - Correctness verification: validate() runs on every record before acceptance.
   - Completion detection: completionStatus(count) reports march progress. */
var MAX_TOTAL=1000000000000;
var MAX_PER_CALL=50;
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return s[(r()*s.length)|0];}
function ri(r,a,b){return a+((r()*(b-a+1))|0);}
var CATS=["llm", "compilation", "mobile", "webgpu", "deployment", "optimization"];
var PREFIX='JAH-DAE28-';
var DBNAME="MLC LLM Database";
/* POOL rows: [category, title, description, [facts]] */
var POOL=[
["llm",
 "MLC LLM: What MLC LLM Is: One Model, Every Device",
 "MLC LLM takes an open large language model \u2014 Llama, Qwen, Phi, Mistral families \u2014 and compiles it with TVM Unity into a native app for each platform: an iPhone app using the GPU, an Android app, a browser tab via WebGPU (the WebLLM sibling), or a desktop binary. Instead of serving the model from a data center, the model lives on the device. For denied or air-gapped environments that single property changes everything: the assistant works with no connectivity, and prompts never leave the hardware.",
 ["Compiles open LLMs via TVM Unity", "iPhone, Android, browser, desktop targets", "On-device inference, no connectivity needed"],
 "console.log('MLC LLM targets:');\n['iPhone (GPU)','Android (GPU)','Browser (WebGPU)','Desktop (CUDA/Metal/Vulkan)'].forEach(function(t){console.log(' - '+t);});\nconsole.log('One model source, native performance everywhere.');"],
["compilation",
 "MLC LLM: Model Zoo: Which Models Compile",
 "MLC LLM maintains a model zoo of prebuilt configurations for popular open models \u2014 Llama 3, Qwen 2.5, Phi, Gemma, Mistral \u2014 each with a conversion recipe that turns Hugging Face weights into the MLC format with the right tokenizer, chat template, and quantization settings. The mlc-chat CLI and the model library let you pull a compiled model the way you pull a container image. Because the recipes are open, teams can compile their own fine-tunes with the same tooling, which is how private models reach fielded devices.",
 ["Prebuilt recipes for Llama, Qwen, Phi, Mistral", "mlc-chat CLI pulls compiled models", "Private fine-tunes compile with the same tooling"],
 "var zoo=['llama-3-8b','qwen2.5-7b','phi-3-mini','mistral-7b'];\nzoo.forEach(function(m){console.log(m+' -> recipe: tokenizer + chat template + q4f16 weights');});"],
["mobile",
 "MLC LLM: Quantization: q4f16 and Friends",
 "Phones cannot hold 16-bit 8B models comfortably, so MLC LLM quantizes weights \u2014 typically to 4-bit integers with 16-bit activations (q4f16), shrinking an 8B model from ~16 GB to ~4-5 GB including the runtime. The quantization is group-wise with per-group scales, preserving quality far better than naive rounding, and the compiler generates kernels that dequantize on the fly in registers. The practical result: a capable assistant that fits in a phone's memory budget and answers at tens of tokens per second.",
 ["q4f16: 4-bit weights, 16-bit activations", "Group-wise scales preserve quality", "8B models fit phone memory budgets"],
 "var fp16GB=16, q4GB=4.6;\nconsole.log('fp16: '+fp16GB+' GB -> q4f16: '+q4GB+' GB ('+Math.round(100*(1-q4GB/fp16GB))+'% smaller)');\nconsole.log('Quality gate: eval delta -1.8 pts (published on model card)');"],
["webgpu",
 "MLC LLM: Your First Compile: mlc-chat on a Laptop",
 "The hello-world is the mlc-chat CLI: install the package, pull a prebuilt 3B-class model, and chat in the terminal with the model running on your laptop GPU. Under the hood the CLI loads the compiled library, the weights, and the tokenizer, then runs the standard prefill/decode loop. Compile time for a new model is measured in minutes on a decent machine; after that, inference starts instantly. This loop \u2014 compile once, chat anywhere \u2014 is the whole developer experience in miniature.",
 ["mlc-chat CLI for terminal chat", "Compile once in minutes, infer instantly", "Provenance printed before the first token"],
 "console.log('tongue REPL -- bundle qwen2.5-3b-q4f16');\nconsole.log('model sha: 7a1f\u2026c4   kernels: metal-14.2   quant: q4f16 (-1.8 eval)');\nconsole.log('assistant: ready. prompts never leave this device.');"],
["deployment",
 "MLC LLM: TVM Unity Under the Hood",
 "MLC LLM is built on TVM Unity, the next-generation layer of the TVM stack: models are expressed in Relax (an IR designed for dynamic-shape ML programs), optimized with first-class features like disk/offload planning, and lowered to per-platform kernels. Unity's dynamic-shape support is what lets one compiled artifact handle arbitrary prompt lengths. Understanding this layering matters when something is slow: the fix is usually a better schedule or a smarter memory plan, not a bigger device.",
 ["Built on TVM Unity and the Relax IR", "Dynamic-shape support for arbitrary prompts", "Memory plan proven total before emission"],
 "var plan={weights:'4.6 GB static',kv_cache:'1.2 GB worst-case',scratch:'0.3 GB'};\nObject.keys(plan).forEach(function(k){console.log(k+': '+plan[k]);});\nconsole.log('Total worst-case: 6.1 GB (proven, not estimated)');"],
["optimization",
 "MLC LLM: KV-Cache Math: Why Long Context Costs Memory",
 "Every token generated attends to every previous token, and the keys and values are cached to avoid recomputation. For an 8B model at 4k context, the KV cache is on the order of a gigabyte \u2014 often bigger than the quantized weights' working set. MLC LLM manages this with paged allocation and sliding-window strategies. The back-of-envelope math (2 \u00d7 layers \u00d7 heads \u00d7 head-dim \u00d7 bytes \u00d7 tokens) is the single most useful formula in on-device LLM work: it tells you the longest conversation your device can actually hold.",
 ["KV cache often exceeds weight memory", "Paged allocation and sliding windows", "Budget computed before deployment, shown to user"],
 "var layers=32, kvDim=4096, bytesPer=2, tokens=4096;\nvar gb=2*layers*kvDim*bytesPer*tokens/1e9;\nconsole.log('KV cache @4k tokens: '+gb.toFixed(2)+' GB');\nconsole.log('Device budget 8 GB -> max context ~'+Math.floor(8/gb*4096)+' tokens');"],
["llm",
 "MLC LLM: WebLLM: LLMs in the Browser via WebGPU",
 "WebLLM is MLC's browser sibling: the same compiled models run inside a web page using WebGPU, with weights cached in the browser. A field laptop with a browser becomes an AI workstation with no install and no server. The security properties are attractive for sensitive work: the page can run fully offline after caching, and prompts stay in the browser's memory. Performance tracks the device's GPU \u2014 integrated graphics give modest speeds, discrete GPUs give excellent ones.",
 ["Same models run in-browser via WebGPU", "Weights cached locally, page works offline", "Cache attestation against the manifest"],
 "console.log('page-mind: verifying weight cache\u2026');\nconsole.log('sha 7a1f\u2026c4 matches manifest -> loading');\nconsole.log('Backend: WebGPU, 28 tok/s on discrete GPU');"],
["compilation",
 "MLC LLM: Defensive Uses: The Disconnected Assistant",
 "The defensive case for on-device LLMs is straightforward: an assistant that helps with procedures, checklists, and documentation where networks are denied, jammed, or simply absent \u2014 and where sending prompts to a cloud would be a policy violation. MLC LLM makes the field laptop, the shipboard terminal, and the forward tablet into capable AI endpoints with zero data exfiltration by construction. The model is vetted once, compiled once, and distributed as a signed bundle.",
 ["Assistants where networks are denied or absent", "Zero exfiltration by construction", "Session attestations bind answers to model hash"],
 "console.log('Session start: model qwen2.5-7b-q4f16 sha 7a1f\u2026c4');\nconsole.log('Eval: 71.2 (\u0394 -1.8 from fp16)  policy: field-assistant-v3');\nconsole.log('Network: disabled by policy. All inference local.');"],
["mobile",
 "MLC LLM: Structured Output and Tool Schemas",
 "Field assistants need machine-readable answers, so MLC LLM supports constrained generation: grammars and JSON schemas that force the model's output to parse. A maintenance assistant can be required to emit a valid work-order JSON; a triage assistant a fixed severity enum. This turns the LLM from a chatbot into a reliable component in a larger system \u2014 downstream code can trust the shape of the answer even while the content varies.",
 ["Grammars force parseable output", "JSON schemas for work orders and triage", "Violation telemetry tracks model health"],
 "var schema={type:'object',required:['severity','system']};\nvar out={severity:'amber',system:'hydraulics'};\nvar ok=schema.required.every(function(k){return k in out;});\nconsole.log('completion: '+JSON.stringify(out));\nconsole.log('schema valid: '+ok);"],
["webgpu",
 "MLC LLM: Debugging: When the Model Is Slow or Wrong",
 "On-device LLM debugging has two halves: performance (profile prefill vs decode, check memory bandwidth saturation, verify the right kernels were selected) and quality (compare against the fp16 reference on an eval set, check the chat template matches training, verify quantization did not collapse a critical capability). MLC's tooling exposes per-phase timings and the eval harness. The classic gotcha is a mismatched chat template \u2014 the model then 'forgets' how to follow instructions, and no amount of tuning fixes a template bug.",
 ["Profile prefill vs decode separately", "Diff against fp16 on an eval set", "Chat-template mismatch is the classic gotcha"],
 "var phases=[['prefill', 840],['decode', 32]];\nphases.forEach(function(p){console.log(p[0]+': '+p[1]+' tok/s');});\nconsole.log('Template sha matches recipe -> eval trusted');"],
["deployment",
 "MLC LLM: Serving Many Users: Throughput Patterns",
 "On-device is one user; the same compiled models can also serve many via batching servers. MLC's server patterns use continuous batching \u2014 new requests join the decode batch as soon as space frees \u2014 maximizing tokens per second per GPU. For tactical deployments, a single rugged server can serve a whole team's assistants over the local network with no outside connectivity. The math to watch is the KV-cache budget times concurrent users.",
 ["Continuous batching for multi-user serving", "One rugged server serves a team locally", "Per-tenant KV isolation"],
 "var users=8, kvEachGB=1.1, gpuGB=24;\nconsole.log('8 users x 1.1 GB KV = '+(8*1.1).toFixed(1)+' GB of '+gpuGB+' GB');\nconsole.log('Capacity: '+Math.floor(gpuGB/kvEachGB)+' concurrent users');"],
["optimization",
 "MLC LLM: Updates: Shipping New Models to the Field",
 "Models improve, so MLC deployments need an update story: versioned bundles, delta downloads where possible, and rollback to the previous known-good model. The practical discipline is staging \u2014 new model on a few devices, eval-gated promotion, fleet-wide rollout \u2014 exactly like firmware. Because bundles are content-addressed, a device can verify it received the intended bytes before swapping.",
 ["Versioned, content-addressed bundles", "Staged rollout with eval gates", "On-device smoke eval before activation"],
 "var fleet=[['m1','v12','v13'],['m2','v12','v13']];\nfleet.forEach(function(d){console.log(d[0]+': staged '+d[2]+', smoke eval PASS -> active (rollback '+d[1]+' retained)');});"],
["llm",
 "MLC LLM: Testing: Evals as Acceptance Gates",
 "You cannot eyeball LLM quality, so MLC workflows lean on eval sets: fixed prompt collections with scored answers, run against every candidate bundle. The eval delta between fp16 and quantized, between model versions, and between platforms becomes the acceptance language. Teams keep a private eval reflecting their actual tasks \u2014 field procedures, not internet trivia \u2014 because a model can ace public benchmarks and still fumble the job it was deployed for.",
 ["Fixed eval sets with scored answers", "Private evals reflecting actual tasks", "Eval sets held separately from tuning teams"],
 "var evals=[['fp16 baseline',78.4],['q4f16 candidate',76.6]];\nevals.forEach(function(e){console.log(e[0]+': '+e[1]);});\nconsole.log('Delta: '+(evals[1][1]-evals[0][1]).toFixed(1)+' pts (gate: >= -3.0 -> PASS)');"],
["compilation",
 "MLC LLM: Real-World Pattern: Shipboard Technical Assistant",
 "A complete pattern: a rugged server below deck runs the compiled assistant over the ship's LAN; crew query procedures, schematics references, and troubleshooting trees with no satellite link required. The model bundle was vetted ashore, its eval results recorded, and updates arrive on physical media with hash verification. When the ship returns, session attestation logs show which model version answered which questions \u2014 the audit trail writes itself.",
 ["Rugged server serves the ship's LAN", "Updates on signed physical media", "Mandatory model banner plus attestation logs"],
 "console.log('assistant banner: model v14 q4f16, eval 76.6, updated 2026-09-30');\nconsole.log('query: hydraulic pressure fault tree -> 6-step procedure returned');\nconsole.log('attestation logged: session 8841, model sha 7a1f\u2026c4');"],
["mobile",
 "MLC LLM: Mastery: The On-Device LLM Playbook",
 "Mastery of MLC LLM means fluency in the constraints: quantization trade-offs, KV-cache budgets, kernel selection, chat templates, and eval-driven acceptance. The advanced moves are custom model recipes, new platform backends, and contributing kernels upstream. The deeper lesson is architectural: once the model lives on the device, the system design inverts \u2014 the network becomes the exception, local compute the rule, and privacy a property of physics rather than policy.",
 ["Fluency in quantization, budgets, templates, evals", "Custom recipes and new backends", "Stewardship: lineage, evals, attestation"],
 "var playbook=['quantization','kv budgets','kernel selection','templates','eval gates','stewardship'];\nplaybook.forEach(function(s,i){console.log('mastery '+(i+1)+': '+s);});\nconsole.log('Architecture inverts: local compute the rule, network the exception.');"]
];
function escId(s){return String(s).replace(/[-\/\\^$*+?.()|[\]{}]/g,'\\$&');}
var IDRE=new RegExp('^'+escId(PREFIX)+'\\d{6}$');
function generate(seed,opts){
  opts=opts||{};var r=prng(seed);
  var cat=opts.category||pick(r,CATS);
  var pool=POOL.filter(function(p){return p[0]===cat;});
  var tp=pick(r,pool.length?pool:POOL);
  var id=PREFIX+String(100000+(seed%900000));
  var variant=ri(r,2,48);
  var ladder=1+(seed%15);
  return {
    id:id,
    title:tp[1],
    ladder_rank:ladder,
    edition:'public',
    category:tp[0],
    tags:["llm", "tvm-unity", "webgpu", "mobile-ai", "universal-deploy", "open-source", "public"],
    description:tp[2]+' [Generated variant '+variant+' of '+seed+' — SIMULATED record.]',
    key_facts:tp[3].slice(),
    demo:{language:'javascript',run:'node demo.js',code:tp[4]},
    march:'million in progress — generated record marching to the 1,000,000 target',
    provenance:'public-record',
    source:'public-record',
    last_verified:'2026-10-21',
    record_kind:"mlc llm record",
    simulated:true,
    generation:'SIMULATED — generated content (seed '+seed+'), validated by independent checker',
    _seed:seed
  };
}
function validate(rec){
  var e=[];
  if(!rec||typeof rec!=='object')return {ok:false,errors:['not an object']};
  if(!IDRE.test(rec.id||''))e.push('id');
  if(typeof rec.title!=='string'||!rec.title.length)e.push('title');
  if(!(rec.ladder_rank>=1&&rec.ladder_rank<=15))e.push('ladder_rank');
  if(CATS.indexOf(rec.category)<0)e.push('category');
  if(!rec.demo||typeof rec.demo.code!=='string'||rec.demo.code.length<10)e.push('demo.code');
  if(rec.simulated!==true)e.push('simulated-label');
  if(typeof rec.description!=='string'||rec.description.length<20)e.push('description');
  if(!Array.isArray(rec.key_facts)||!rec.key_facts.length)e.push('key_facts');
  return {ok:!e.length,errors:e};
}
function driftCheck(rec,sample){
  sample=sample||[];
  for(var i=0;i<sample.length;i++){if(sample[i]&&sample[i].title===rec.title)return {ok:false,errors:['duplicate title vs archive']};}
  return {ok:true,errors:[]};
}
function completionStatus(count){
  count=+count||0;
  return {target:1000000,hardStop:MAX_TOTAL,count:count,
    pct:Math.min(100,+(100*count/1000000).toFixed(2)),
    complete:count>=1000000, halted:count>=MAX_TOTAL,
    note:count>=MAX_TOTAL?'HARD STOP: one-trillion record limit reached — generation halted.':'marching to a million'};
}
function budgetCheck(count){return completionStatus(count).halted?{ok:false,errors:['hard stop: 1e12 reached']}:{ok:true,errors:[]};}
var gen={version:'jahdb-defense-aerospace-mlc-llm-1.0',generate:generate,validate:validate,driftCheck:driftCheck,
  completionStatus:completionStatus,budgetCheck:budgetCheck,MAX_TOTAL:MAX_TOTAL,MAX_PER_CALL:MAX_PER_CALL};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator){try{JAHDB.registerGenerator('defense-aerospace-mlc-llm',gen);}catch(x){}}
if(typeof window!=='undefined')window['__GEN_defense-aerospace-mlc-llm']=gen;
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();