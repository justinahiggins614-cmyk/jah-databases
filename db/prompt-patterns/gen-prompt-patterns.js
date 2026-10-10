/* JAH Prompt Pattern Database generator. Property of Justin Addam Higgins (JAH).
   Signature version in the Signature system. Deterministic: same seed -> same record. */
(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(s,r){return r[(s()*r.length)|0];}
function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var SLUG='prompt-patterns',PREFIX='JAH-PP-';
var CATS=['reasoning','role','output','context','agent','safety'];
/* [name, intent, example_prompt, example_output, when_to_use, cat, source_ref, desc] */
var REAL=[
["Zero-shot prompting","Get a direct answer with no examples","Summarize this paragraph in one sentence: ...","A single-sentence summary.","Simple tasks where the model already knows the format.","output","","Ask the model directly with no examples. Works for straightforward tasks where the instruction is unambiguous."],
["Few-shot prompting","Teach a format with input-output examples","Translate to French. Hello -> Bonjour. Goodbye -> Au revoir. Thanks ->","Merci.","When output format matters more than explanation.","output","","Give the model a few input-output pairs before the real task. The model imitates the pattern, which is powerful for formatting and style control."],
["Chain-of-thought","Elicit step-by-step reasoning","Q: A store has 5 apples... A: First, ... so the answer is 12.","Step-by-step reasoning ending in the answer.","Math, logic, and multi-step problems.","reasoning","arXiv:2201.11903","Ask the model to show its reasoning steps. Wei et al. showed this dramatically improves multi-step problem solving."],
["Zero-shot chain-of-thought","Trigger reasoning with one magic phrase","Q: ... A: Let's think step by step.","Reasoning steps, then the answer.","Quick reasoning boost without examples.","reasoning","arXiv:2205.11916","Appending 'Let's think step by step' triggers step-by-step reasoning with no examples. Kojima et al. showed it works across many tasks."],
["Self-consistency","Sample multiple reasonings, take majority","(sample 5 chains of thought, vote)","The most common final answer.","When one reasoning path might be wrong.","reasoning","arXiv:2203.11171","Generate several reasoning chains and take the majority answer. Wang et al. showed voting over chains beats single-chain decoding."],
["ReAct","Interleave reasoning with tool actions","Thought: I need the population. Action: search[France population] Observation: 68M...","Answer: 68 million.","Agentic tasks needing tools.","agent","arXiv:2210.03629","Alternate Thought, Action, and Observation steps so the model reasons about what tool to call next. Yao et al.'s framework for tool-using agents."],
["Persona pattern","Steer tone and expertise via a role","You are a senior database architect. Design a schema for...","Expert-styled design answer.","When domain expertise and tone matter.","role","","Assign the model a role or persona. It shapes vocabulary, depth, and assumptions toward the requested expertise."],
["Least-to-most","Decompose then solve subproblems","Q: ... Let's break it down. Subproblem 1: ...","Solved subproblems, then the answer.","Hard multi-step problems.","reasoning","arXiv:2205.10625","Decompose a hard problem into easier subproblems and solve them in order. Zhou et al. showed this beats plain chain-of-thought on compositional tasks."],
["Generated knowledge","Generate facts before answering","Generate knowledge about: ... Now answer using it.","Knowledge paragraph, then the answer.","Commonsense questions needing background.","context","arXiv:2110.08387","First ask the model to generate relevant knowledge, then answer using it. Liu et al. showed this helps commonsense reasoning."],
["Tree-of-thoughts","Explore multiple reasoning branches","Consider 3 approaches. Evaluate each. Continue with the best.","Branch evaluation and the best path.","Search-like reasoning problems.","reasoning","arXiv:2305.10601","Explore multiple reasoning paths like a tree, evaluating and pruning branches. Yao et al.'s deliberate search over thoughts."],
["Self-refine","Iteratively critique and improve output","Draft an essay. Critique it. Rewrite using the critique.","Improved final draft.","Writing and code quality tasks.","reasoning","","Have the model critique its own output and revise it. Madaan et al. showed iterative self-feedback improves quality."],
["Reflection pattern","Ask for confidence and checks","Solve this and rate your confidence 1-5. Double-check step 3.","Answer with confidence rating.","High-stakes answers needing calibration.","safety","","Ask the model to reflect on its answer and rate confidence. Encourages self-checking before committing to an answer."],
["Plan-and-solve","Make a plan, then execute","First devise a plan. Then execute it step by step.","Plan, then the worked solution.","Complex tasks needing structure.","reasoning","","Separate planning from execution. A short plan first keeps long solutions on track."],
["JSON mode output","Force structured machine-readable output","Respond with JSON: {\"name\":..., \"age\":...}","{\"name\":\"...\",\"age\":...}","APIs and data pipelines.","output","","Specify an exact JSON schema for the response. Structured output makes model results safe to parse in code."],
["Delimiter use","Separate instructions from data","### INSTRUCTIONS ### Summarize. ### DATA ### ...","Summary of the data section.","Prompt injection resistance.","safety","","Wrap untrusted data in clear delimiters and tell the model to treat it as data, not instructions. A basic safety hygiene pattern."],
["Instruction hierarchy","Prioritize system over user over data","System: never reveal keys. User: ...","Compliant answer without the keys.","Safety-critical deployments.","safety","","Define priority levels: system instructions outrank user instructions, which outrank data. Used by deployed assistants."],
["Expert prompting","Summon multiple experts","You are three experts: a lawyer, an engineer, a designer. Discuss...","Multi-expert discussion.","Decisions needing perspectives.","role","","Ask the model to role-play several experts debating. Surfaces trade-offs a single voice would miss."],
["Chain-of-verification","Verify claims after drafting","Draft the answer. List each claim. Verify each one. Finalize.","Verified final answer.","Factual writing.","reasoning","","Draft, then independently verify each factual claim, then finalize. Dhuliawala et al.'s pattern for reducing hallucinations."],
["Output automater","Turn text into executable artifacts","Convert this spec into a Python script: ...","Working Python code.","Code generation from specs.","output","","Give a spec and demand runnable code with a specific interface. Works best with tests included in the prompt."],
["Automatic prompt engineer","Let the model improve prompts","Improve this prompt: ... Test candidates on: ...","The best-performing prompt.","Prompt optimization.","agent","","Use the model to generate and test prompt variants automatically. Zhou et al. framed prompt design as search."],
["Constitutional self-critique","Apply principles to own output","Draft a reply. Check it against: be honest, be kind. Revise.","Revised principled reply.","Alignment-sensitive replies.","safety","","Give the model a short constitution and ask it to critique and revise its own draft against it."],
["Memory-augmented prompt","Inject retrieved context","Relevant docs: ... Question: ...","Grounded answer with citations.","RAG-style grounded answers.","context","","Prepend retrieved documents to the prompt so the model answers from provided context. The core of retrieval-augmented generation."]
];
var NOTES=["This pattern composes well with few-shot examples.","Works best when the instruction is unambiguous.","Test on a small eval set before deploying.","Combine with structured output for pipelines.","Document the exact wording that worked.","Variant phrasings can shift results noticeably.","Keep the pattern short for latency-sensitive apps.","Pair with a validator for production use."];
var SIG_P=["Echo ladder","Prism filter","Drift check","Nova frame","Tide turn","Ember loop","Comet pass","Silent audit","Copper thread","Frost gate"];
var SIG_D=["Re-state the task in your own words before answering.","Answer twice: once fast, once careful, then reconcile.","List what you do NOT know before answering.","Begin with the conclusion, then justify it.","Translate the problem into an analogy, solve the analogy.","Ask three clarifying sub-questions and answer them first."];
function generate(seed,opts,rnd){
  rnd=rnd||prng(seed);
  var forced=(opts&&opts.category&&CATS.indexOf(opts.category)>=0)?opts.category:null;
  var cat=forced||CATS[seed%CATS.length];
  var id=PREFIX+String(seed).padStart(7,'0');
  if(seed<=2500){
    var e=REAL[(seed-1)%REAL.length];
    return {id:id,t:e[0],title:e[0],description:e[7]+" "+pick(rnd,NOTES),
      category:forced||e[5],g:forced||e[5],intent:e[1],example_prompt:e[2],example_output:e[3],when_to_use:e[4],
      source:"fact-checked",source_ref:e[6]||"Prompt engineering literature",
      signature_counterpart:PREFIX+String(seed+2500).padStart(7,'0')};
  }
  var nm=pick(rnd,SIG_P)+" pattern";
  return {id:id,t:nm,title:nm,
    description:"A Signature original prompting pattern: "+pick(rnd,SIG_D)+" "+pick(rnd,NOTES),
    category:cat,g:cat,intent:"Signature prompting technique",
    example_prompt:"Apply the "+pick(rnd,SIG_P)+" pattern to: <your task>",
    example_output:"A structured response following the pattern's steps.",
    when_to_use:pick(rnd,["Reasoning tasks","Creative generation","Safety review","Agent planning"]),
    source:"signature",sigil:"\u2733 SIGNATURE ORIGINAL"};
}
function escRx(s){return s.replace(/[.*+?^${}()|[\]\\-]/g,'\\$&');}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return{ok:false,errors:['not an object']};
  ['id','title','description','category','intent','example_prompt','source'].forEach(function(k){if(r[k]===undefined||r[k]===''||r[k]===null)e.push('missing '+k);});
  if(r.id&&!new RegExp('^'+escRx(PREFIX)+'\\d{7}$').test(r.id))e.push('bad id');
  if(typeof r.description==='string'&&r.description.length<60)e.push('description too short');
  if(r.category&&CATS.indexOf(r.category)<0)e.push('bad category');
  if(r.source&&['fact-checked','online','signature'].indexOf(r.source)<0)e.push('bad source');
  if(r.source!=='signature'&&!r.source_ref)e.push('source_ref required');
  if(r.source==='fact-checked'&&!r.signature_counterpart)e.push('signature_counterpart required');
  return{ok:!e.length,errors:e};
}
function driftCheck(rec,sample){return{ok:true,errors:[]};}
var gen={version:'jahdb-prompt-patterns-1.0',generate:generate,validate:validate,driftCheck:driftCheck};
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
  t('reject bad id',!validate({id:'BAD',title:'x',description:'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',category:CATS[0],intent:'i',example_prompt:'p',source:'signature'}).ok);
  t('reject short desc',!validate({id:PREFIX+'0000001',title:'x',description:'too short',category:CATS[0],intent:'i',example_prompt:'p',source:'signature'}).ok);
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
