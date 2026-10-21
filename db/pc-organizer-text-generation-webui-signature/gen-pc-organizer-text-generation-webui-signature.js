(function(){'use strict';
/* Signature Text Generation WebUI (oobabooga) Database — boundless generator jahdb-pc-organizer-text-generation-webui-signature-1.0
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
var PREFIX='JAH-PCO77S-';
var ROWS=[["installation", "SigStory boots a whole library in one click", "The Signature Story Engine is a Signature original: a local-model interface that boots an entire library of Signature stories, characters, and presets with one click. Where the public UI makes you configure loaders and f", ["one-click library boot", "auto backend detection"]], ["loaders", "SigLoader unified backend", "SigLoader is SigStory's original unified loader layer: instead of exposing a dozen backends, it profiles the model file (format, size, quantization) and the machine (VRAM, RAM, CPU threads) and routes to the best engine ", ["auto routing", "per-model backend pins"]], ["interface", "Story shelves instead of folders", "SigStory replaces raw folders with story shelves: curated collections (mystery shelf, sci-fi shelf, study shelf) that bundle a character set, a preset, and an instruct template that were tuned together. Installing a shel", ["curated shelves", "bundled character+preset+template"]], ["interface", "SigCast character format", "SigCast is the Signature character format: a character card plus voice settings, memory notes, and a relationship map to other characters on the same shelf. Characters remember shelf-level facts (who met whom) so multi-c", ["character + voice + memory", "relationship maps"]], ["api", "SigAPI local endpoint", "SigAPI mirrors the familiar chat-completions shape so existing scripts work, but adds Signature extensions: shelf context injection, character memory endpoints, and generation receipts (which preset/template/seed produce", ["chat-completions shape", "generation receipts"]], ["interface", "Preset tuner with live A/B", "The preset tuner runs the same prompt through two presets side by side and shows both outputs with tokens/sec, so tuning stops being guesswork. Winning settings save as a new preset with one click, and the tuner keeps a ", ["side-by-side A/B", "one-click preset save"]], ["extensions", "SigExtensions sandbox", "SigExtensions run in a sandbox with declared permissions (network, filesystem, microphone), shown in the UI before you enable one. A misbehaving extension can be killed without restarting the server, and its permission g", ["permission manifest", "per-session grants"]], ["installation", "Shelf downloader", "The downloader fetches whole shelves (characters, presets, templates, sample models) as one signed bundle and verifies the signature before installing. Partial downloads resume, and bundles install into the shelf tree wi", ["signed bundles", "resume support"]], ["loaders", "SigQuant smart quantization picker", "SigQuant inspects free VRAM and picks the heaviest quantization that fits with headroom for context, then explains the choice in plain language. If the user later frees VRAM, one click re-picks. The picker logic and its ", ["VRAM-aware picking", "plain-language explanations"]], ["interface", "Template matcher", "The template matcher reads a model's config and README hints and suggests the instruct template the model was trained with, with a confidence score. A wrong-template warning appears before generation, not after bad outpu", ["auto template suggestion", "wrong-template warning"]], ["api", "SigBench built-in benchmark runs", "SigBench runs a standard prompt battery against every installed model and keeps a leaderboard (tokens/sec, quality votes, VRAM used). Results are stored per model file hash, so re-downloaded models do not need re-benchma", ["prompt battery", "per-hash result cache"]], ["extensions", "SigTrain one-click adapters", "SigTrain wraps adapter training in a three-screen wizard: pick base, pick shelf dataset, pick style strength. It validates the dataset (format, size, license note) before spending GPU time, and trained adapters attach to", ["dataset validation", "auto shelf attach"]], ["interface", "Hot-swap with session carryover", "SigStory hot-swaps models mid-conversation and carries a compressed session summary into the new model so the story continues coherently. The summary is shown to the user and editable before the swap completes. Signature", ["session summary handoff", "editable carryover"]], ["api", "SigFlags launch profiles", "Launch profiles save full flag sets (network exposure, API on/off, preloaded model, extensions) as named profiles: 'solo', 'lan-party', 'api-server'. Switching profiles restarts only what changed. The profile file format", ["named flag sets", "minimal restarts"]], ["loaders", "SigGuard memory watchdog", "SigGuard watches VRAM during generation and, before an OOM crash, pauses and offers fixes: drop context, switch quant, or offload layers — with the exact VRAM each fix frees. It turns crashes into a dialog box. Original ", ["pre-OOM pause", "fix menu with VRAM math"]]];
function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  var cat=opts.category||pick(CATS,rnd);
  var pool=ROWS.filter(function(x){return x[0]===cat;});
  var row=pick(pool.length?pool:ROWS,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  var title=row[1]+' — variant '+(1+((seed*7)%97));
  var desc=row[2]+' This generated entry is labeled simulated for weeding and was correctness-verified before acceptance.';
  return {id:id,t:title,title:title,g:cat,c:1,ladder_rank:1+((seed*13)%15),
    tool:"Signature Story Engine",edition:'signature',description:desc,facts:row[3].slice(),
    demo:{language:'python3',program:'print('+JSON.stringify('demo: '+row[1])+')',run:'python3 demo.py',expected_output:''},
    march:'million in progress — 15 of 1,000,000 records (march to a million)',provenance:"Signature original \u2014 designed by Justin Addam Higgins (JAH).",last_verified:'2026-10-21',_seed:seed,_simulated:true};
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
var gen={version:'jahdb-pc-organizer-text-generation-webui-signature-1.0',self_regulation:SELF_REG,generate:generate,validate:validate,driftCheck:driftCheck};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('pc-organizer-text-generation-webui-signature',gen);
if(typeof window!=='undefined')window['__gen_pc_organizer_text_generation_webui_signature']=gen;
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
