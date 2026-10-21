(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
/* CATS: ["framework", "conversion", "quantization", "runtime", "benchmark", "deployment"] */
var CATS=["framework", "conversion", "quantization", "runtime", "benchmark", "deployment"];
var PREFIX='JAH-EDGEAI-S-';
var FIELDS=["platform", "model_format", "min_requirements", "conversion"];
/* rows: [category, title, summary, details, ...fields, demoLang, demoTitle, demoProg] */
var B=[
 ["framework", "Signature Edge Runtime", "Signature-authored runtime: one API running models on any phone's best accelerator.", "Signature Edge Runtime is a JAH-designed on-device runtime: a single API that dispatches to Neural Engine, Hexagon, GPU, or CPU per operator, with a model format converted once from PyTorch. The design includes a device-capability database so the runtime picks optimal paths per phone model. Labeled Signature throughout.", "iOS/Android (unified)", ".sigedge", "Phone with 4GB+ RAM", "Signature converter from PyTorch", "python", "Runtime dispatch", "ops = {\"linear\": \"NPU\", \"softmax\": \"GPU\", \"custom\": \"CPU\"}\nprint(\"dispatch plan:\", ops)"],
 ["conversion", "JAH Pocket LLM Packer", "Signature-authored tool: one command packs an LLM for a target phone.", "JAH Pocket LLM Packer is a JAH-designed conversion tool: input a Hugging Face model ID and target phone, and it outputs an installable pack (quantized weights, runtime config, tokenizer) sized to the device's RAM and accelerator. The design includes a fit-check that refuses impossible packs with a clear reason. Labeled Signature; an original JAH procedure.", "iOS/Android", ".sigpack", "Target phone profile", "pack(model_id, phone_model)", "python", "Fit check", "model_gb, phone_gb = 4.1, 6\nprint(\"fits:\" , model_gb < phone_gb * 0.7)"],
 ["quantization", "Signature Neural Shrinkwrap", "Signature-authored compression pipeline: prune, distill, quantize, verify — in one pass.", "Signature Neural Shrinkwrap is a JAH-designed pipeline chaining structured pruning, distillation, and quantization with a verification gate after each stage (accuracy must stay within budget). The design outputs a compression report showing what each stage cost. Labeled Signature throughout.", "All mobile", ".sigedge (compressed)", "Teacher model + calibration data", "shrinkwrap(model, budget)", "python", "Stage budget", "stages = {\"prune\": 0.5, \"distill\": 0.3, \"quantize\": 1.0}  # accuracy pts\nprint(\"total budget:\", sum(stages.values()), \"pts\")"],
 ["benchmark", "JAH On-Device Benchmark Kit", "Signature-authored kit: benchmark any model on any phone with one script.", "JAH On-Device Benchmark Kit is a JAH-designed benchmarking harness: one script measures latency, tokens/sec, peak RAM, and battery drain per model per device, uploading results to a shared leaderboard. The design standardizes the 'does it run on my phone' question. Labeled Signature; an original JAH procedure.", "iOS/Android", "Any", "Test device", "n/a", "python", "Benchmark record", "rec = {\"device\": \"pixel_8\", \"tok_s\": 14.2, \"peak_ram_gb\": 4.8}\nprint(rec)"],
 ["runtime", "Signature Thermal Governor", "Signature-authored governor: sustain AI performance by managing thermals proactively.", "Signature Thermal Governor is a JAH-designed runtime component: it monitors SoC temperature and proactively shifts work (fewer parallel requests, lower clocks, NPU preference) before throttling hits, keeping sustained throughput smooth instead of spiky. Labeled Signature throughout.", "All mobile", "n/a (runtime)", "Thermal sensors", "n/a", "python", "Governor action", "temp = 44  # C\naction = \"shift to NPU\" if temp > 42 else \"full speed\"\nprint(temp, \"C ->\", action)"],
 ["deployment", "JAH Model Slice Server", "Signature-authored delivery: stream model slices to phones on demand, cache locally.", "JAH Model Slice Server is a JAH-designed delivery system: models are sliced into downloadable chunks; phones fetch slices on demand and cache them, so apps start small and grow. The design includes delta updates (only changed slices). Labeled Signature; an original JAH procedure.", "iOS/Android", "Sliced .sigpack", "Network on first use", "slice(model, chunk_mb=50)", "python", "Slice plan", "size_mb, chunk = 4100, 50\nprint(f\"{size_mb//chunk} slices; fetch on demand\")"],
 ["deployment", "Signature Offline-First AI", "Signature-authored pattern: full features offline, cloud only as enhancement.", "Signature Offline-First AI is a JAH-designed architecture pattern: every AI feature works fully offline with the on-device model; cloud calls only enhance (never gate) the experience. The design includes a capability manifest declaring what works offline. Labeled Signature throughout.", "All mobile", ".sigedge", "On-device model", "n/a", "python", "Capability manifest", "manifest = {\"offline\": [\"chat\", \"summarize\"], \"enhanced\": [\"web_search\"]}\nprint(manifest)"],
 ["runtime", "JAH Voice-Edge Pipeline", "Signature-authored pipeline: on-device speech-to-speech with sub-second latency.", "JAH Voice-Edge Pipeline is a JAH-designed pipeline chaining on-device ASR (whisper-class), LLM, and TTS with streaming between stages — total latency under a second on flagship phones. The design specifies the streaming protocol between stages. Labeled Signature; an original JAH procedure.", "Flagship phones", ".sigedge x3", "8GB RAM device", "pack each stage", "python", "Latency budget", "budget = {\"asr\": 0.3, \"llm_first_token\": 0.4, \"tts\": 0.2}\nprint(\"total:\", sum(budget.values()), \"s\")"]
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
var gen={version:'jahdb-on-device-ai-signature-1.0',generate:generate,validate:validate};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('on-device-ai-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
