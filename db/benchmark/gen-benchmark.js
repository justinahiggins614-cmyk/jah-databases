/* ✳ SIGNATURE — JAH JAH Benchmark generator. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed + same version always yields the same record.
   Runs in the browser (registered with JAHDB) and in node (self-test below). */
(function(){
'use strict';
var SLUG='benchmark', PREFIX='JAH-BENCH-', VERSION='jahdb-benchmark-1.0';
var MARK='Signature version in the Signature system. Property of Justin Addam Higgins.';
function hashStr(s){var h=2166136261;s=String(s);for(var i=0;i<s.length;i++){h^=s.charCodeAt(i);h=Math.imul(h,16777619);}return h>>>0;}
function mulberry(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var CATS=["language", "reasoning", "code", "math", "multimodal", "safety"];
var ANGLES=["metric deep dive", "dataset construction", "example walkthrough", "results analysis", "usage guide", "history and versions"];
var TOPICS=[{"t": "MMLU", "c": "language", "d": "MMLU — benchmark suite entry.", "f": {"benchmark": "MMLU (Massive Multitask Language Understanding)", "what_it_measures": "Broad knowledge and reasoning across 57 subjects, from elementary math to professional law.", "metrics": ["accuracy (exact match)", "per-subject accuracy", "average across subjects"], "dataset_size": "15,908 test questions across 57 subjects", "example_item": "Subject: high-school physics. Q: \"A ball is thrown upward at 20 m/s…\" A/B/C/D.", "notable_result": "Strong models now exceed 85% average; early baselines sat near 30–40%.", "evaluation_tip": "Report per-subject scores, not just the average — averages hide weak spots."}, "s": "online", "r": "Hendrycks et al., Measuring Massive Multitask Language Understanding, 2020"}, {"t": "HellaSwag", "c": "language", "d": "HellaSwag — benchmark suite entry.", "f": {"benchmark": "HellaSwag", "what_it_measures": "Commonsense natural-language inference: choose the most plausible continuation of a situation.", "metrics": ["accuracy", "normalized accuracy (length-corrected)"], "dataset_size": "~70,000 multiple-choice questions (10k test)", "example_item": "Context: \"A woman is chopping vegetables…\" Pick the sensible next sentence.", "notable_result": "Human performance ~95%; models climbed from ~40% to 85%+ over five years.", "evaluation_tip": "Use the normalized metric; raw accuracy favors short answers."}, "s": "online", "r": "Zellers et al., HellaSwag, 2019"}, {"t": "BIG-bench Hard", "c": "reasoning", "d": "BIG-bench Hard — benchmark suite entry.", "f": {"benchmark": "BIG-bench Hard (BBH)", "what_it_measures": "The 23 hardest BIG-bench tasks, testing multi-step reasoning with chain-of-thought prompting.", "metrics": ["exact-match accuracy", "multiple-choice grade"], "dataset_size": "23 tasks, ~6,500 examples", "example_item": "Task: \"boolean expressions\" — evaluate nested logical statements.", "notable_result": "Chain-of-thought prompting roughly doubled scores over direct answering on many tasks.", "evaluation_tip": "Always report both direct and chain-of-thought numbers."}, "s": "online", "r": "Suzgun et al., Challenging BIG-Bench Tasks (BBH), 2022"}, {"t": "ARC", "c": "reasoning", "d": "ARC — benchmark suite entry.", "f": {"benchmark": "ARC (AI2 Reasoning Challenge)", "what_it_measures": "Grade-school science questions requiring reasoning beyond retrieval.", "metrics": ["accuracy (Challenge set)", "accuracy (Easy set)"], "dataset_size": "~7,800 questions (Challenge: ~2,600)", "example_item": "\"Which property of water allows it to stick to itself?\" (cohesion)", "notable_result": "The Challenge set long separated strong from weak models.", "evaluation_tip": "Split Challenge vs. Easy when reporting."}, "s": "online", "r": "Clark et al., Think You Have Solved Question Answering? (ARC), 2018"}, {"t": "HumanEval", "c": "code", "d": "HumanEval — benchmark suite entry.", "f": {"benchmark": "HumanEval", "what_it_measures": "Functional correctness of Python code from docstrings: 164 hand-written problems.", "metrics": ["pass@1", "pass@10", "pass@100"], "dataset_size": "164 problems", "example_item": "def add(a, b): \"Add two numbers.\" — model writes the body; hidden tests grade it.", "notable_result": "pass@1 rose from ~30% (2021 models) to 85%+ with modern systems.", "evaluation_tip": "pass@1 with temperature 0 is the standard headline number."}, "s": "online", "r": "Chen et al., Evaluating Large Language Models Trained on Code (HumanEval), 2021"}, {"t": "SWE-bench", "c": "code", "d": "SWE-bench — benchmark suite entry.", "f": {"benchmark": "SWE-bench", "what_it_measures": "Resolving real GitHub issues in Python repositories, graded by the repo’s own tests.", "metrics": ["resolved rate (% of issues fixed)", "pass-to-pass / fail-to-pass tests"], "dataset_size": "~2,300 real issues (Verified: 500)", "example_item": "Issue: \"DataFrame.merge raises on overlapping columns\" + repo + failing test.", "notable_result": "Top agents now resolve 50%+ of the Verified set.", "evaluation_tip": "Use the Verified split for clean comparisons."}, "s": "online", "r": "Jimenez et al., SWE-bench, 2023"}, {"t": "GSM8K", "c": "math", "d": "GSM8K — benchmark suite entry.", "f": {"benchmark": "GSM8K", "what_it_measures": "Grade-school math word problems requiring 2–8 steps of arithmetic reasoning.", "metrics": ["exact-match accuracy (final number)"], "dataset_size": "8,500 problems (7.5k train / 1k test)", "example_item": "\"Janet has 3 apples and buys 2 more bags of 4… How many apples?\"", "notable_result": "Chain-of-thought lifted scores from ~20% to 80%+ across model generations.", "evaluation_tip": "Grade the final number only; reasoning format varies."}, "s": "online", "r": "Cobbe et al., Training Verifiers to Solve Math Word Problems (GSM8K), 2021"}, {"t": "MATH", "c": "math", "d": "MATH — benchmark suite entry.", "f": {"benchmark": "MATH", "what_it_measures": "Competition mathematics (AMC/AIME level) across 7 subjects and 5 difficulty levels.", "metrics": ["exact-match accuracy", "accuracy by difficulty level"], "dataset_size": "12,500 problems", "example_item": "Algebra: solve a system with a clever substitution.", "notable_result": "Even strong models score well under 60% without tool use.", "evaluation_tip": "Report by difficulty level; level-5 items separate the best."}, "s": "online", "r": "Hendrycks et al., Measuring Mathematical Problem Solving (MATH), 2021"}, {"t": "VQA v2", "c": "multimodal", "d": "VQA v2 — benchmark suite entry.", "f": {"benchmark": "VQA v2", "what_it_measures": "Open-ended visual question answering on real images.", "metrics": ["VQA accuracy (consensus-weighted)"], "dataset_size": "~1.1M questions over ~200k images", "example_item": "Image of a street scene; Q: \"What color is the bus?\"", "notable_result": "Balanced pairs force models to look at the image, not guess from language.", "evaluation_tip": "Use the consensus-weighted accuracy, not plain exact match."}, "s": "online", "r": "Goyal et al., Making the V in VQA Matter (VQA v2), 2017"}, {"t": "MMMU", "c": "multimodal", "d": "MMMU — benchmark suite entry.", "f": {"benchmark": "MMMU", "what_it_measures": "Expert-level multimodal questions across 30 subjects requiring college knowledge.", "metrics": ["accuracy"], "dataset_size": "~11,500 questions, 30 subjects", "example_item": "A chemistry diagram question needing to read structures and recall reactions.", "notable_result": "Frontier models score ~60–70%; earlier models near 30%.", "evaluation_tip": "Needs genuine domain knowledge, not just vision."}, "s": "online", "r": "Yue et al., MMMU, 2023"}, {"t": "ToxiGen", "c": "safety", "d": "ToxiGen — benchmark suite entry.", "f": {"benchmark": "ToxiGen (implicit hate detection)", "what_it_measures": "Detecting implicit hate speech that keyword filters miss.", "metrics": ["accuracy", "false-positive rate on benign mentions"], "dataset_size": "~274k machine-generated statements (v2)", "example_item": "A subtly demeaning statement about a group with no slurs.", "notable_result": "Tests whether detectors catch implication, not just profanity.", "evaluation_tip": "Track false positives: over-blocking is a failure mode."}, "s": "online", "r": "Hartvigsen et al., ToxiGen, 2022"}, {"t": "RealToxicityPrompts", "c": "safety", "d": "RealToxicityPrompts — benchmark suite entry.", "f": {"benchmark": "RealToxicityPrompts", "what_it_measures": "Measuring toxic degeneration: how often innocuous prompts lead to toxic continuations.", "metrics": ["toxicity probability", "expected maximum toxicity"], "dataset_size": "100k prompts", "example_item": "Prompt: a neutral sentence fragment; measure toxicity over 25 continuations.", "notable_result": "Baseline for every detoxification method since 2020.", "evaluation_tip": "Report both probability and expected-maximum metrics."}, "s": "online", "r": "Gehman et al., RealToxicityPrompts, 2020"}];
function pickR(rnd,a){return a[(rnd()*a.length)|0];}
function makeId(seed){var n=(typeof seed==='number'?seed:hashStr(String(seed)));return PREFIX+String((n%1000000)+1).padStart(7,'0');}
function compose(seed,rnd,T,cat){
  var A=pickR(rnd,ANGLES);
  var rec={focus:A};
  for(var k in T.f){rec[k]=T.f[k];}
  return rec;
}
function generate(seed,opts,rnd){
  var r=rnd||mulberry(typeof seed==='number'?seed:hashStr(String(seed)));
  var cat=opts&&opts.category,pool=TOPICS;
  if(cat){var f=TOPICS.filter(function(t){return t.c===cat;});if(f.length)pool=f;}
  var T=pickR(r,pool);
  var rec=compose(seed,r,T,cat);
  if(!rec.id)rec.id=makeId(seed);
  if(!rec.title)rec.title=T.t;
  if(!rec.description)rec.description=T.d;
  if(!rec.category)rec.category=T.c;
  if(!rec.source)rec.source=T.s||'signature';
  if(T.r&&!rec.source_ref)rec.source_ref=T.r;
  rec.signature_mark=MARK;
  return rec;
}
function validate(rec){
  var errs=[],req=["id", "title", "description", "category", "benchmark", "what_it_measures", "metrics", "dataset_size", "example_item", "source"];
  if(!rec||typeof rec!=='object')return{ok:false,errors:['not an object']};
  req.forEach(function(k){if(rec[k]===undefined||rec[k]===null||rec[k]==='')errs.push('missing '+k);});
  if(rec.id&&!/^[A-Z0-9]+(-[A-Z0-9]+)*-[0-9]{7}$/.test(rec.id))errs.push('bad id format');
  if(rec.source&&['online','signature','fact-checked'].indexOf(rec.source)<0)errs.push('bad source');
  return{ok:errs.length===0,errors:errs};
}
function driftCheck(rec,sample){
  var key;try{key=JSON.stringify(rec);}catch(e){return{ok:false,errors:['unstringifiable']};}
  sample=sample||[];
  for(var i=0;i<sample.length;i++){try{if(JSON.stringify(sample[i])===key)return{ok:false,errors:['exact duplicate of archive record']};}catch(e){}}
  return{ok:true,errors:[]};
}
var GEN={version:VERSION,generate:generate,validate:validate,driftCheck:driftCheck};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator){try{JAHDB.registerGenerator(SLUG,GEN);}catch(e){}}
if(typeof module!=='undefined'){module.exports=GEN;}
function runTests(){
  var pass=0,fail=0;
  function t(name,fn){try{if(fn()){pass++;}else{fail++;console.log('FAIL: '+name);}}catch(e){fail++;console.log('FAIL: '+name+' threw '+e.message);}}
  var i;
  for(i=1;i<=10;i++){(function(s){t('gen+validate seed '+s,function(){return validate(generate(s,{},null)).ok;});})(i);}
  for(i=11;i<=20;i++){(function(s){t('determinism seed '+s,function(){return JSON.stringify(generate(s,{},null))===JSON.stringify(generate(s,{},null));});})(i);}
  for(i=0;i<CATS.length;i++){(function(c){t('category filter '+c,function(){var r=generate(7,{category:c},null);return r.category===c&&validate(r).ok;});})(CATS[i]);}
  t('id format',function(){return /^[A-Z0-9]+(-[A-Z0-9]+)*-[0-9]{7}$/.test(generate(42,{},null).id);});
  t('title non-empty',function(){return String(generate(5,{},null).title).length>3;});
  t('description non-empty',function(){return String(generate(5,{},null).description).length>10;});
  t('source valid',function(){return['online','signature','fact-checked'].indexOf(generate(5,{},null).source)>=0;});
  t('signature mark',function(){return String(generate(5,{},null).signature_mark).indexOf('Signature')>=0;});
  t('reject empty',function(){return !validate({}).ok;});
  t('reject missing title',function(){var r=generate(3,{},null);delete r.title;return !validate(r).ok;});
  t('reject bad id',function(){var r=generate(3,{},null);r.id='nope';return !validate(r).ok;});
  t('driftCheck novel ok',function(){return driftCheck(generate(999,{},null),[]).ok;});
  t('driftCheck dupe caught',function(){var r=generate(999,{},null);return !driftCheck(r,[JSON.parse(JSON.stringify(r))]).ok;});
  t('distinct seeds distinct ids',function(){return generate(1001,{},null).id!==generate(1002,{},null).id;});
  t('json round-trip',function(){var r=generate(77,{},null);return JSON.parse(JSON.stringify(r)).id===r.id;});
  t('extra domain check',function(){var r=generate(9,{},null);return (r.metrics.length>=1);});
  t('version string',function(){return GEN.version===VERSION;});
  console.log(pass+'/40 '+(fail===0?'PASS':'FAIL'));
  if(fail>0&&typeof process!=='undefined')process.exitCode=1;
}
if(typeof require!=='undefined'&&require.main===module){runTests();}
})();
