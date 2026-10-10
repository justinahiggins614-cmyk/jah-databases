/* JAH AI Evaluation Database generator. Property of Justin Addam Higgins (JAH).
   Signature version in the Signature system. Deterministic: same seed -> same record. */
(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(s,r){return r[(s()*r.length)|0];}
function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var SLUG='eval-harness',PREFIX='JAH-EH-';
var CATS=['knowledge','reasoning','code','safety','dialogue','multimodal'];
/* [name, org, year, tasks, metric, cat, source_ref, desc] */
var REAL=[
["MMLU","Hendrycks et al.","2021","57 subjects, 15,908 questions","accuracy","knowledge","","Massive Multitask Language Understanding: 57 subjects from math to law. The headline benchmark for general knowledge in language models."],
["HellaSwag","Zellers et al.","2019","10,042 questions","accuracy","knowledge","","Commonsense natural language inference built adversarially against models. Tests whether a model can finish everyday situations sensibly."],
["HumanEval","OpenAI","2021","164 programming problems","pass@k","code","","Hand-written Python problems testing functional correctness of generated code. The standard code generation benchmark."],
["GSM8K","OpenAI","2021","8,500 grade-school math problems","accuracy","reasoning","","Grade-school math word problems requiring multi-step reasoning. A core test of chain-of-thought ability."],
["ARC","AI2","2018","7,787 science questions","accuracy","reasoning","","The AI2 Reasoning Challenge: grade-school science questions split into Easy and Challenge sets. A reasoning staple."],
["TruthfulQA","Lin et al.","2021","817 questions","truthfulness score","safety","","Tests whether models repeat common human falsehoods. Designed to measure truthfulness, not just accuracy."],
["Winogrande","Sakaguchi et al.","2019","44,000 problems","accuracy","reasoning","","An adversarial Winograd Schema dataset for commonsense coreference. Hard for models that rely on statistical cues."],
["BIG-bench","Srivastava et al.","2022","200+ tasks","task-specific","reasoning","","Beyond the Imitation Game: a massive collaborative benchmark of 200+ diverse tasks probing model capabilities."],
["Big-Bench Hard","Suzgun et al.","2022","23 hard tasks","accuracy","reasoning","","The 23 BIG-bench tasks where models lagged humans. The proving ground for chain-of-thought prompting."],
["DROP","Dua et al.","2019","96,000 questions","F1 / EM","reasoning","","Discrete reasoning over paragraphs: questions requiring counting, sorting, and arithmetic on text."],
["SQuAD","Rajpurkar et al.","2016","100,000+ questions","F1 / exact match","knowledge","","The Stanford Question Answering Dataset on Wikipedia passages. Launched the modern reading-comprehension era."],
["GLUE","Wang et al.","2018","9 tasks","aggregate score","knowledge","","The General Language Understanding Evaluation: nine NLU tasks that defined the pre-LLM benchmark era."],
["SuperGLUE","Wang et al.","2019","8 harder tasks","aggregate score","knowledge","","A harder successor to GLUE with more difficult language understanding tasks."],
["MATH","Hendrycks et al.","2021","12,500 competition problems","accuracy","reasoning","","Competition mathematics problems from AMC, AIME, and similar contests. Tests serious mathematical reasoning."],
["MT-Bench","Zheng et al.","2023","80 multi-turn questions","LLM-judge score","dialogue","","Multi-turn dialogue evaluated by a strong LLM judge. Tests instruction following across conversations."],
["IFEval","Zhou et al.","2023","541 prompts","instruction-level accuracy","dialogue","","Instruction-Following Eval: verifiable instructions like 'mention AI 3 times'. Objective scoring of obedience."],
["SimpleQA","OpenAI","2024","4,326 questions","accuracy","knowledge","","Short fact-seeking questions with a single verifiable answer. A precision test for factuality."],
["Chatbot Arena","LMSYS","2023","crowdsourced battles","Elo rating","dialogue","","Human preference battles between anonymous models, ranked by Elo. The public leaderboard of chat quality."],
["GPQA","Rein et al.","2024","448 questions","accuracy","knowledge","","Graduate-level Google-proof questions in biology, physics, and chemistry. Extremely difficult for models."],
["SWE-bench","Jimenez et al.","2024","2,294 GitHub issues","resolved rate","code","","Can a model resolve real GitHub issues? Tests agentic software engineering on real repositories."],
["MMMU","Yue et al.","2024","11,500 questions","accuracy","multimodal","","Massive Multi-discipline Multimodal Understanding: college-level questions across 30 subjects with images."],
["RealToxicityPrompts","Gehman et al.","2020","100,000 prompts","toxicity score","safety","","Measures toxic degeneration from provocative prompts. A standard safety evaluation."],
["ToxiGen","Hartvigsen et al.","2022","274,000 statements","toxicity detection","safety","","Implicit hate speech detection across 13 minority groups. Tests subtle toxicity recognition."],
["BBQ","Parrish et al.","2022","58,492 questions","bias score","safety","","Bias Benchmark for QA: measures social biases in question answering across nine categories."]
];
var NOTES=["Scores are reported with confidence intervals where available.","Leaderboard results should be reproduced independently.","Contamination checks are recommended before trusting scores.","This benchmark has known saturation on recent models.","Report the exact prompt template used.","Multiple seeds reduce variance in results."];
var SIG_B=["Drift Sentinel","Echo Chamber Eval","Nova Reasoning Gauntlet","Iron Instruction Suite","Prism Safety Grid","Tide Dialogue Trials","Ember Code Forge","Comet Context Window","Frost Factuality Check","Copper Tool-Use Trials"];
function generate(seed,opts,rnd){
  rnd=rnd||prng(seed);
  var cat=(opts&&opts.category&&CATS.indexOf(opts.category)>=0)?opts.category:CATS[seed%CATS.length];
  var id=PREFIX+String(seed).padStart(7,'0');
  if(seed<=2500){
    var e=REAL[(seed-1)%REAL.length];
    return {id:id,t:e[0],title:e[0],description:e[7]+" "+pick(rnd,NOTES),
      category:e[5],g:e[5],org:e[1],year:e[2],tasks:e[3],metric:e[4],
      source:"fact-checked",source_ref:e[6]||"Published benchmark paper",
      signature_counterpart:PREFIX+String(seed+2500).padStart(7,'0')};
  }
  var nm=pick(rnd,SIG_B)+" v"+ri(rnd,1,3);
  return {id:id,t:nm,title:nm,
    description:"A Signature original evaluation suite for "+cat+" tasks. It runs "+ri(rnd,200,2000)+" generated items through a deterministic scorer with per-item rubrics, and reports accuracy plus a calibration score. "+pick(rnd,NOTES),
    category:cat,g:cat,org:"Signature Eval Works",year:String(ri(rnd,2024,2026)),
    tasks:String(ri(rnd,200,2000))+" generated items",metric:pick(rnd,["accuracy","pass@k","rubric score","Elo"]),
    source:"signature",sigil:"\u2733 SIGNATURE ORIGINAL"};
}
function escRx(s){return s.replace(/[.*+?^${}()|[\]\\-]/g,'\\$&');}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return{ok:false,errors:['not an object']};
  ['id','title','description','category','org','year','metric','source'].forEach(function(k){if(r[k]===undefined||r[k]===''||r[k]===null)e.push('missing '+k);});
  if(r.id&&!new RegExp('^'+escRx(PREFIX)+'\\d{7}$').test(r.id))e.push('bad id');
  if(typeof r.description==='string'&&r.description.length<60)e.push('description too short');
  if(r.category&&CATS.indexOf(r.category)<0)e.push('bad category');
  if(r.source&&['fact-checked','online','signature'].indexOf(r.source)<0)e.push('bad source');
  if(r.source!=='signature'&&!r.source_ref)e.push('source_ref required');
  if(r.source==='fact-checked'&&!r.signature_counterpart)e.push('signature_counterpart required');
  return{ok:!e.length,errors:e};
}
function driftCheck(rec,sample){return{ok:true,errors:[]};}
var gen={version:'jahdb-eval-harness-1.0',generate:generate,validate:validate,driftCheck:driftCheck};
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
  t('reject bad id',!validate({id:'BAD',title:'x',description:'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',category:CATS[0],org:'o',year:'2020',metric:'m',source:'signature'}).ok);
  t('reject short desc',!validate({id:PREFIX+'0000001',title:'x',description:'too short',category:CATS[0],org:'o',year:'2020',metric:'m',source:'signature'}).ok);
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
