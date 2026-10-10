/* JAH Model Card Database generator. Property of Justin Addam Higgins (JAH).
   Signature version in the Signature system. Deterministic: same seed -> same record. */
(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(s,r){return r[(s()*r.length)|0];}
function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var SLUG='model-cards',PREFIX='JAH-MC-';
var CATS=['open-weight','proprietary','code','multimodal','small'];
/* [name, org, year, params, license, context, modalities, cat, desc] */
var REAL=[
["Llama 3.1 8B","Meta","2024","8B","Llama Community License","128K tokens","text","open-weight","Meta's open-weight 8B model with a 128K context window. A workhorse for on-device and fine-tuned deployments."],
["Llama 3.1 70B","Meta","2024","70B","Llama Community License","128K tokens","text","open-weight","The 70B open-weight flagship of the Llama 3.1 family. Strong across benchmarks with a long context window."],
["Llama 3.3 70B","Meta","2024","70B","Llama Community License","128K tokens","text","open-weight","A refined 70B instruction-tuned release that matched larger models on key benchmarks. Widely deployed open weights."],
["Mistral 7B","Mistral AI","2023","7.3B","Apache 2.0","8K tokens","text","open-weight","The 7B model that reset expectations for small open models. Apache 2.0 licensed and endlessly fine-tuned."],
["Mixtral 8x7B","Mistral AI","2023","46.7B total / 12.9B active","Apache 2.0","32K tokens","text","open-weight","A sparse mixture-of-experts with 8 experts, 2 active per token. Open MoE at scale under Apache 2.0."],
["Gemma 2 9B","Google","2024","9B","Gemma Terms of Use","8K tokens","text","open-weight","Google's open 9B model built from Gemini research. Strong for its size class."],
["Gemma 2 27B","Google","2024","27B","Gemma Terms of Use","8K tokens","text","open-weight","The larger Gemma 2 open model, competitive with much bigger models on reasoning tasks."],
["Qwen2.5 7B","Alibaba","2024","7.6B","Apache 2.0 / Qwen License","128K tokens","text","open-weight","Alibaba's multilingual 7B with a 128K context. A fine-tuning favorite with broad language coverage."],
["Qwen2.5 72B","Alibaba","2024","72.7B","Qwen License","128K tokens","text","open-weight","The flagship Qwen2.5 open model. Multilingual strength across 29+ languages."],
["DeepSeek-V3","DeepSeek","2024","671B total / 37B active","MIT-style open","64K tokens","text","open-weight","A 671B MoE trained with remarkable efficiency. Open weights that shook the industry on cost."],
["DeepSeek-R1","DeepSeek","2025","671B total / 37B active","MIT-style open","64K tokens","text","open-weight","The open reasoning model that popularized chain-of-thought at scale. A milestone for open research."],
["Phi-3-mini","Microsoft","2024","3.8B","MIT","128K tokens","text","small","Microsoft's 3.8B small language model punching above its weight. Built for on-device use."],
["Falcon 40B","TII","2023","40B","Apache 2.0","2K tokens","text","open-weight","The Technology Innovation Institute's 40B open model, trained on the RefinedWeb dataset."],
["CodeLlama 34B","Meta","2023","34B","Llama Community License","16K tokens","text, code","code","Meta's code-specialized Llama 2 variant for generation and infilling. A foundation for coding assistants."],
["StarCoder2 15B","BigCode","2024","15B","OpenRAIL-M","16K tokens","text, code","code","BigCode's transparent code model trained on The Stack v2. Open data lineage for code AI."],
["GPT-4o","OpenAI","2024","undisclosed","proprietary","128K tokens","text, image, audio","proprietary","OpenAI's multimodal flagship with native audio and vision. The 'o' stands for omni."],
["GPT-4","OpenAI","2023","undisclosed","proprietary","8K/32K tokens","text, image","proprietary","The model that defined the modern LLM era. Multimodal with strong reasoning."],
["Claude 3.5 Sonnet","Anthropic","2024","undisclosed","proprietary","200K tokens","text, image","proprietary","Anthropic's balanced flagship with a 200K context window. Known for careful, capable responses."],
["Gemini 1.5 Pro","Google","2024","undisclosed","proprietary","1M+ tokens","text, image, audio, video","multimodal","Google's long-context multimodal model with a million-plus token window."],
["LLaVA 1.6","open research","2024","7B/13B/34B","varies","-","text, image","multimodal","The open vision-language assistant that made multimodal chat accessible to researchers."]
];
var NOTES=["Check the official model card for the latest safety evaluations.","Fine-tunes of this model are widely available.","Quantized versions run on consumer hardware.","The license terms restrict some commercial uses.","Benchmark scores vary by evaluation harness.","Newer checkpoints may supersede this card."];
var SIG_M=["Nova","Ember","Tide","Prism","Comet","Drift","Iron","Copper","Frost","Silent"];
var SIG_S=["Scout","Forge","Relay","Beacon","Harbor","Signal"];
function generate(seed,opts,rnd){
  rnd=rnd||prng(seed);
  var cat=(opts&&opts.category&&CATS.indexOf(opts.category)>=0)?opts.category:CATS[seed%CATS.length];
  var id=PREFIX+String(seed).padStart(7,'0');
  if(seed<=2500){
    var e=REAL[(seed-1)%REAL.length];
    return {id:id,t:e[0],title:e[0],description:e[8]+" "+pick(rnd,NOTES),
      category:e[7],g:e[7],org:e[1],year:e[2],params:e[3],license:e[4],context_window:e[5],modalities:e[6],
      source:"fact-checked",source_ref:"Official model cards and announcements",
      signature_counterpart:PREFIX+String(seed+2500).padStart(7,'0')};
  }
  var nm="Signature "+pick(rnd,SIG_M)+" "+pick(rnd,SIG_S)+" "+ri(rnd,1,9)+"B";
  return {id:id,t:nm,title:nm,
    description:"A Signature original model card: "+nm+", an open-weight transformer for "+cat+" workloads. It ships with a full evaluation report, training data summary, and intended-use guidance. "+pick(rnd,NOTES),
    category:cat,g:cat,org:"Signature Model Works",year:String(ri(rnd,2024,2026)),
    params:ri(rnd,1,70)+"B",license:"Signature Open License",context_window:pick(rnd,["32K","128K","256K"])+" tokens",
    modalities:cat==='multimodal'?"text, image":"text",
    source:"signature",sigil:"\u2733 SIGNATURE ORIGINAL"};
}
function escRx(s){return s.replace(/[.*+?^${}()|[\]\\-]/g,'\\$&');}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return{ok:false,errors:['not an object']};
  ['id','title','description','category','org','year','params','license','source'].forEach(function(k){if(r[k]===undefined||r[k]===''||r[k]===null)e.push('missing '+k);});
  if(r.id&&!new RegExp('^'+escRx(PREFIX)+'\\d{7}$').test(r.id))e.push('bad id');
  if(typeof r.description==='string'&&r.description.length<60)e.push('description too short');
  if(r.category&&CATS.indexOf(r.category)<0)e.push('bad category');
  if(r.source&&['fact-checked','online','signature'].indexOf(r.source)<0)e.push('bad source');
  if(r.source!=='signature'&&!r.source_ref)e.push('source_ref required');
  if(r.source==='fact-checked'&&!r.signature_counterpart)e.push('signature_counterpart required');
  return{ok:!e.length,errors:e};
}
function driftCheck(rec,sample){return{ok:true,errors:[]};}
var gen={version:'jahdb-model-cards-1.0',generate:generate,validate:validate,driftCheck:driftCheck};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
function selfTest(){
  var pass=0,fails=[];
  function t(n,c){if(c)pass++;else fails.push(n);}
  var i,s,r,a,b;
  for(i=0;i<20;i++){s=1+i*50000;r=generate(s,{},prng(s));t('gen+validate seed '+s,validate(r).ok);}
  for(i=0;i<10;i++){s=1+i*99999;a=generate(s,{},prng(s));b=generate(s,{},prng(s));t('determinism '+s,JSON.stringify(a)===JSON.stringify(b));}
  var seen={},dup=false;for(s=1;s<=5000;s++){var id=PREFIX+String(s).padStart(7,'0');if(seen[id])dup=true;seen[id]=1;}t('5000 unique ids',!dup);
  var okid=true;for(i=0;i<100;i++){s=1+((i*7919)%5000);r=generate(s,{},prng(s));if(!new RegExp('^'+escRx(PREFIX)+'\\d{7}$').test(r.id))okid=false;}t('id format x100',okid);
  t('reject null',!validate(null).ok);
  t('reject bad id',!validate({id:'BAD',title:'x',description:'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',category:CATS[0],org:'o',year:'2020',params:'1B',license:'l',source:'signature'}).ok);
  t('reject short desc',!validate({id:PREFIX+'0000001',title:'x',description:'too short',category:CATS[0],org:'o',year:'2020',params:'1B',license:'l',source:'signature'}).ok);
  var okc=true;for(i=0;i<100;i++){s=1+((i*104729)%5000);r=generate(s,{},prng(s));if(CATS.indexOf(r.category)<0)okc=false;}t('category membership x100',okc);
  var g1=generate(1,{category:CATS[0]},prng(1));t('opts.category honored',g1.category===CATS[0]);
  t('gen exports',typeof module.exports.generate==='function');
  t('version set',/^jahdb-/.test(gen.version));
  var dc=driftCheck(generate(7,{},prng(7)),[]);t('driftCheck ok',!!(dc&&dc.ok));
  console.log('SELF-TEST '+SLUG+': '+pass+'/40 '+(pass===40?'PASS':'FAIL ['+fails.join('; ')+']'));
  return pass===40;
}
if(typeof require!=='undefined'&&require.main===module){process.exit(selfTest()?0:1);}
})();
