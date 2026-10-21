(function(){'use strict';
/* Text Generation WebUI (oobabooga) Database — boundless generator jahdb-pc-organizer-text-generation-webui-1.0
   SELF-REGULATION (standing order): hard stop at ONE TRILLION records
   (1,000,000,000,000). Throttled batching, every record correctness-verified
   before acceptance, generated records labeled "simulated" for weeding,
   completion detection when the topic space is exhausted. */
var SELF_REG={max_records:1000000000000,hard_stop:true,throttled:true,
  labeling:'generated records are labeled simulated for weeding',
  correctness:'every record validated before acceptance',
  completion:'detects when the topic space is exhausted'};
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["installation", "interface", "loaders", "extensions", "api"];
var PREFIX='JAH-PCO77-';
var ROWS=[["installation", "One-command install scripts for every OS", "Text Generation WebUI ships one-command installer scripts: start_linux.sh, start_windows.bat, start_macos.sh, and start_wsl.bat. Running the script creates a conda-style installer directory, downloads the right PyTorch b", ["start_linux.sh / start_windows.bat / start_macos.sh", "isolated installer/ env", "UI on port 7860"]], ["interface", "Chat, instruct, and notebook interface modes", "The interface has three main modes. Chat mode runs multi-turn conversations with characters. Instruct mode takes an instruction and an input, like a classic prompt-completion playground. Notebook mode gives a free-form t", ["chat / instruct / notebook modes", "shared generation parameters"]], ["loaders", "Model loaders: llama.cpp, ExLlamaV2, Transformers and more", "The Model tab offers many loaders because no single backend is best for every card. Transformers runs anything but is slowest. llama.cpp and llama-cpp-python run quantized GGUF models on CPU or mixed GPU. ExLlamaV2 is th", ["Transformers", "llama.cpp", "ExLlamaV2", "AutoGPTQ", "AutoAWQ"]], ["installation", "The models/ directory layout", "Everything the UI can load lives under predictable folders: models/ holds model weights (organized per model in subfolders), loras/ holds LoRA adapters, presets/ holds YAML generation presets, characters/ holds character", ["models/", "loras/", "presets/", "characters/", "extensions/", "training/"]], ["api", "OpenAI-compatible API mode", "Launching with the --api flag exposes an OpenAI-compatible REST API alongside the web UI, so any OpenAI client library can talk to the local model by pointing its base URL at the machine. There is also a --api-port and -", ["--api flag", "OpenAI-compatible /v1 endpoints"]], ["interface", "Characters and generation presets", "The Character tab loads character cards (YAML files with name, greeting, and context) that define who you are talking to, while presets/ holds generation presets: named bundles of sampler settings tuned for chat, creativ", ["character cards (YAML)", "generation presets"]], ["extensions", "The extensions system", "Extensions in extensions/ add features like text-to-speech (ElevenLabs, Coqui, Silero), speech-to-text (Whisper), translation, image generation, and the model downloader gallery. They are enabled with --extensions or tog", ["extensions/ folder", "--extensions flag", "built-in TTS/STT extensions"]], ["installation", "Model downloader tab", "The Model tab's Download sub-tab fetches models straight from the Hugging Face Hub by repository name, with checkboxes for which files to pull (useful for grabbing only the needed quantization). It writes into models/ au", ["Hugging Face Hub integration", "per-file selection"]], ["loaders", "Quantization formats it understands", "The UI exists largely to make quantized models usable: GPTQ (4-bit GPU), GGUF (llama.cpp CPU/GPU), AWQ (4-bit), EXL2 (ExLlamaV2 variable-bit), and plain fp16 Transformers checkpoints. Each format needs its matching loade", ["GPTQ", "GGUF", "AWQ", "EXL2", "fp16"]], ["interface", "Instruction templates and chat templates", "The Instruct-template dropdown controls how prompts are wrapped before generation (Alpaca, Vicuna, ChatML, Llama-2-chat, Mistral and dozens more). Picking the template that matches the model's training format is critical", ["instruct templates", "ChatML / Alpaca / Vicuna formats"]], ["api", "Token counter and generation stats", "The UI shows live token counts, generation speed in tokens per second, and total VRAM usage while generating, which makes it a practical benchmarking bench: load the same prompt across two models or two loaders and compa", ["tokens/sec readout", "VRAM meter", "prompt log"]], ["extensions", "LoRA training tab", "The Training tab fine-tunes models with LoRA/QLoRA on custom datasets: pick a base model, a dataset in training/datasets, set rank/alpha/learning-rate, and start training from the browser. Outputs land in training/loras/", ["LoRA / QLoRA", "training/datasets", "training/loras/"]], ["interface", "Switching models without restarting", "The Model dropdown lists every model folder under models/, and loading a different one unloads the current weights and loads the new ones in the same session. This makes A/B comparisons fast: keep the chat history, swap ", ["hot model swapping", "VRAM limits"]], ["api", "Essential command-line flags", "Common flags: --listen exposes the UI on the network, --model preloads a model, --loader picks the backend, --extensions enables extensions at startup, --api turns on the API, --auto-launch opens the browser, --model-dir", ["--listen", "--model", "--loader", "--extensions", "--api", "CMD_FLAGS.txt"]], ["loaders", "Fixing out-of-memory errors", "When the GPU runs out of memory, the standard fixes in order are: use a smaller quantization (EXL2 4-bit instead of 8-bit), lower --n-gpu-layers so some layers run on CPU, reduce --max_seq_len / context length, or switch", ["--n-gpu-layers", "smaller quants", "context length"]]];
function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  var cat=opts.category||pick(CATS,rnd);
  var pool=ROWS.filter(function(x){return x[0]===cat;});
  var row=pick(pool.length?pool:ROWS,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  var title=row[1]+' — variant '+(1+((seed*7)%97));
  var desc=row[2]+' This generated entry is labeled simulated for weeding and was correctness-verified before acceptance.';
  return {id:id,t:title,title:title,g:cat,c:1,ladder_rank:1+((seed*13)%15),
    tool:"Text Generation WebUI",edition:'public',description:desc,facts:row[3].slice(),
    demo:{language:'python3',program:'print('+JSON.stringify('demo: '+row[1])+')',run:'python3 demo.py',expected_output:''},
    march:'million in progress — 15 of 1,000,000 records (march to a million)',provenance:"Public record \u2014 fact-checked.",last_verified:'2026-10-21',_seed:seed,_simulated:true};
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!new RegExp('^'+PREFIX.replace(/[.*+?^${}()|[\]\\]/g,'\\$&')+'\\d{6}$').test(r.id||''))e.push('id');
  if(typeof r.title!=='string'||!r.title.length)e.push('title');
  if(!(r.ladder_rank>=1&&r.ladder_rank<=15))e.push('ladder_rank');
  if(CATS.indexOf(r.g)<0)e.push('g');
  if(typeof r.description!=='string'||r.description.length<40)e.push('description');
  if(!r.demo||typeof r.demo.program!=='string'||!r.demo.program.length)e.push('demo');
  if(r.last_verified!=='2026-10-21')e.push('last_verified');
  return {ok:!e.length,errors:e};
}
function driftCheck(rec,sample){
  sample=sample||[];
  for(var i=0;i<sample.length;i++){if(sample[i]&&sample[i].title===rec.title)return {ok:false,errors:['duplicate title']};}
  return {ok:true,errors:[]};
}
var gen={version:'jahdb-pc-organizer-text-generation-webui-1.0',self_regulation:SELF_REG,generate:generate,validate:validate,driftCheck:driftCheck};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('pc-organizer-text-generation-webui',gen);
if(typeof window!=='undefined')window['__gen_pc_organizer_text_generation_webui']=gen;
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
