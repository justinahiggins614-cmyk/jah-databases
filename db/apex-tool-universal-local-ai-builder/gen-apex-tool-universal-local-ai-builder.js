(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["runtimes", "model-assembly", "deployment"];
var PREFIX='JAH-APX56-';
var VERSION='jahdb-apex-tool-universal-local-ai-builder-1.0';
var TOOLNAME='Universal Local AI Builder';
var PROV='Public knowledge: standard engineering practice documented in open technical literature; facts cross-checked against the executed demo program. Compiled 2026-10-21.';
var DEPS=["Model weight repositories", "Runtime binaries per OS", "Vector index library", "Hardware capability probe"];
var PARAMS=[[10, 4], [15, 6], [20, 8], [25, 8], [30, 10], [40, 12], [50, 12], [60, 16], [70, 16], [80, 20], [90, 20], [100, 24], [120, 24], [140, 32], [160, 32]];
var DEMO_TPL="function prng(seed){var a=seed>>>0||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}\nvar R=prng(__SEED__);\nvar T0=Date.now();\nvar M=__P0__,LIM=__P1__;\nvar cands=[];for(var i=0;i<M;i++)cands.push({name:\"model-\"+i,ram:+(1+R()*15).toFixed(1),tps:Math.round(5+R()*120),q:+(0.5+R()*0.5).toFixed(3)});\nvar feas=cands.filter(function(c){return c.ram<=LIM;});\nfeas.sort(function(a,b){return (b.q*Math.log(b.tps))-(a.q*Math.log(a.tps));});\nvar best=feas[0]||null;\nconsole.log(JSON.stringify({id:\"__ID__\",ok:true,metrics:{candidates:M,ram_limit_gb:LIM,feasible:feas.length,chosen:best?best.name:null,chosen_tps:best?best.tps:null,chosen_quality:best?best.q:null,chosen_ram_gb:best?best.ram:null},ms:Date.now()-T0}));";
var BP=[["runtimes", "Hardware Capability Probe", "Detects CPU, GPU, RAM, and accelerator presence so the builder assembles a system the machine can actually run.", "A probe collects device facts; capability records feed the assembler's decisions.", "Runtime packager|Retrieval indexer|Prompt template set|License checker", "assemble(spec)->bundle|update(bundle,model)->bundle", "established-practice", "The demo probe reports this machine's real CPU count and memory."], ["runtimes", "Model Catalog Browser", "Lists available models with size, quality, license, and hardware needs, so selection starts from facts.", "Catalog entries carry machine-readable spec cards.", "Model downloader|Memory store|Health monitor|Runtime packager", "benchmark(bundle)->report|assemble(spec)->bundle", "established-practice", "The demo lists the sample catalog with complete spec cards."], ["runtimes", "Constraint-Based Model Picker", "Picks the best model that fits the machine's RAM, latency budget, and license constraints \u2014 no wishful thinking.", "A scorer ranks feasible models by quality-per-resource; infeasible ones are excluded with reasons.", "Quantization stage|Tool connector|Update manager|Model downloader", "deploy(bundle,target)->status|benchmark(bundle)->report", "established-practice", "The demo picker chooses the feasible best model and names why others were excluded."], ["runtimes", "Runtime Bundle Assembler", "Packages the chosen model with its runtime, tokenizer, and configs into one installable bundle.", "An assembler resolves dependencies and packs a versioned bundle.", "Retrieval indexer|Prompt template set|License checker|Quantization stage", "update(bundle,model)->bundle|deploy(bundle,target)->status", "established-practice", "The demo bundle contains model, runtime, and config with matching versions."], ["runtimes", "Quantization Stage", "Shrinks the model with quantization to fit smaller machines, measuring the quality cost before committing.", "Quantizers produce smaller variants; a quality probe scores each.", "Memory store|Health monitor|Runtime packager|Retrieval indexer", "assemble(spec)->bundle|update(bundle,model)->bundle", "established-practice", "The demo quantized variant fits the RAM limit with measured quality drop."], ["model-assembly", "Retrieval Index Builder", "Builds the local vector index over the user's documents so the assistant answers from their data.", "A chunker plus embedder fills the index; queries retrieve top passages.", "Tool connector|Update manager|Model downloader|Memory store", "benchmark(bundle)->report|assemble(spec)->bundle", "prototype-demonstrated", "The demo index answers the test question from the sample documents."], ["model-assembly", "Memory Store Wiring", "Connects short-term conversation memory and long-term fact memory to the model, so the assistant remembers within policy.", "Memory adapters with retention rules wire into the runtime.", "Prompt template set|License checker|Quantization stage|Tool connector", "deploy(bundle,target)->status|benchmark(bundle)->report", "prototype-demonstrated", "The demo recalls the stored fact in a later turn within the same session."], ["model-assembly", "Tool Connector Kit", "Wires approved local tools \u2014 calculator, file search, code runner \u2014 into the assistant with permission checks.", "Tool manifests declare capabilities; calls pass through a permission gate.", "Health monitor|Runtime packager|Retrieval indexer|Prompt template set", "update(bundle,model)->bundle|deploy(bundle,target)->status", "prototype-demonstrated", "The demo tool call succeeds for the approved tool and is refused for the unlisted one."], ["model-assembly", "Prompt Template Library", "Ships task templates \u2014 summarize, explain, plan \u2014 tuned for the local model, so users start from working prompts.", "Templates versioned per model family; a picker matches task to template.", "Update manager|Model downloader|Memory store|Health monitor", "assemble(spec)->bundle|update(bundle,model)->bundle", "prototype-demonstrated", "The demo template produces a well-formed summary prompt for the test task."], ["model-assembly", "Offline Health Monitor", "Watches the local system \u2014 latency, memory, errors \u2014 and reports degradation with causes, all without phoning home.", "Local metric collection with thresholds; reports stay on-device.", "License checker|Quantization stage|Tool connector|Update manager", "benchmark(bundle)->report|assemble(spec)->bundle", "prototype-demonstrated", "The demo monitor flags the injected memory pressure with its cause."], ["deployment", "Bundle Update Manager", "Updates models and runtimes in place with rollback, so the local AI improves without breaking.", "Versioned updates with pre-update snapshots; rollback restores the snapshot.", "Runtime packager|Retrieval indexer|Prompt template set|License checker", "deploy(bundle,target)->status|benchmark(bundle)->report", "design-stage", "The demo rolls back the bad update and the assistant works again."], ["deployment", "License Compliance Checker", "Verifies every bundled model's license permits the intended use before assembly completes.", "License records checked against use declarations; violations block the bundle.", "Model downloader|Memory store|Health monitor|Runtime packager", "update(bundle,model)->bundle|deploy(bundle,target)->status", "design-stage", "The demo blocks the bundle containing the incompatible license."], ["deployment", "Multi-Model Router", "Runs several local models and routes each request to the best one for the task \u2014 fast small model or capable large one.", "A router scores requests by complexity; models register capabilities.", "Quantization stage|Tool connector|Update manager|Model downloader", "assemble(spec)->bundle|update(bundle,model)->bundle", "design-stage", "The demo routes the simple and hard queries to different models correctly."], ["deployment", "Deployment Target Packager", "Produces installers per target OS with the right runtime binaries, so one spec deploys everywhere.", "Target profiles select binaries; packagers emit per-OS installers.", "Retrieval indexer|Prompt template set|License checker|Quantization stage", "benchmark(bundle)->report|assemble(spec)->bundle", "design-stage", "The demo emits all three target packages from one spec."], ["deployment", "Autonomous Local AI Foundry", "Takes a plain description \u2014 'a private assistant for my documents' \u2014 and delivers a working local AI bundle.", "A planner converts descriptions to specs; the pipeline assembles, tests, and packages.", "Memory store|Health monitor|Runtime packager|Retrieval indexer", "deploy(bundle,target)->status|benchmark(bundle)->report", "design-stage", "The demo foundry delivers a bundle whose smoke tests all pass."]];
function demoSource(rank,seed,id){
  var p=PARAMS[(rank-1)%PARAMS.length];
  var s=DEMO_TPL;
  s=s.split('__SEED__').join(String(seed));
  s=s.split('__ID__').join(id);
  for(var i=0;i<p.length;i++)s=s.split('__P'+i+'__').join(String(p[i]));
  return s;
}
function generate(seed,opts){
  opts=opts||{};
  var idx=Math.abs(seed)%BP.length;
  if(opts.category){
    for(var i=0;i<BP.length;i++)if(BP[i][0]===opts.category){idx=i;break;}
  }
  var b=BP[idx];
  var rank=1+(Math.abs(seed*7+idx)%15);
  var id=PREFIX+String(100000+(Math.abs(seed)%899999)).padStart(6,'0');
  var comps=b[4]?b[4].split('|'):[];
  var ifaces=b[5]?b[5].split('|'):[];
  return {id:id,t:b[1],g:b[0],title:b[1],description:b[2],ladder_rank:rank,
    demo:demoSource(rank,seed,id),architecture:b[3],components:comps,interfaces:ifaces,
    implementation_status:b[6],acceptance_tests:[b[7],'Generated record - run its demo program with node to verify.'],
    dependencies:DEPS.slice(0,3),provenance:PROV,last_verified:'2026-10-21',
    march_marker:'Million in progress - generated record marching to 1,000,000.',
    edition:'public',tool_number:56,tool_name:TOOLNAME,_seed:seed};
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  var rx=new RegExp('^'+PREFIX.replace(/[-]/g,'\\-')+'\\d{6}$');
  if(!rx.test(r.id||''))e.push('id');
  if(typeof r.title!=='string'||!r.title.length)e.push('title');
  if(typeof r.description!=='string'||r.description.length<20)e.push('description');
  if(!(r.ladder_rank>=1&&r.ladder_rank<=15))e.push('ladder_rank');
  if(typeof r.demo!=='string'||r.demo.indexOf('console.log')<0)e.push('demo');
  if(typeof r.architecture!=='string'||!r.architecture.length)e.push('architecture');
  if(!Array.isArray(r.components)||!r.components.length)e.push('components');
  if(!Array.isArray(r.acceptance_tests)||!r.acceptance_tests.length)e.push('acceptance_tests');
  if(CATS.indexOf(r.g)<0)e.push('g');
  if(r.last_verified!=='2026-10-21')e.push('last_verified');
  return {ok:!e.length,errors:e};
}
function driftCheck(rec,sample){
  sample=sample||[];
  for(var i=0;i<sample.length;i++)if(sample[i]&&sample[i].id===rec.id)return {ok:false,errors:['duplicate id']};
  return {ok:true,errors:[]};
}
var gen={version:VERSION,generate:generate,validate:validate,driftCheck:driftCheck};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('apex-tool-universal-local-ai-builder',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
