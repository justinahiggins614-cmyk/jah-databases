/* ✳ SIGNATURE — JAH JAH Synthetic Data generator. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed + same version always yields the same record.
   Runs in the browser (registered with JAHDB) and in node (self-test below). */
(function(){
'use strict';
var SLUG='synthetic-data', PREFIX='JAH-SYN-', VERSION='jahdb-synthetic-data-1.0';
var MARK='Signature version in the Signature system. Property of Justin Addam Higgins.';
function hashStr(s){var h=2166136261;s=String(s);for(var i=0;i<s.length;i++){h^=s.charCodeAt(i);h=Math.imul(h,16777619);}return h>>>0;}
function mulberry(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var CATS=["instruction-tuning", "pretraining", "evaluation", "code", "low-resource", "multimodal"];
var ANGLES=["recipe walkthrough", "quality gate focus", "worked example", "pitfall review", "scale notes", "evaluation of data"];
var TOPICS=[{"t": "Self-Instruct pipeline", "c": "instruction-tuning", "d": "Self-Instruct pipeline — synthetic data recipe entry.", "f": {"recipe": "Self-Instruct pipeline", "use_case": "Bootstrapping a 50k+ instruction dataset from a handful of seed tasks.", "method_steps": ["Seed with ~175 hand-written instructions.", "Prompt the model to generate new instructions from few-shot seeds.", "Generate input/output instances per instruction; filter by ROUGE-L similarity.", "Keep diverse, well-formed items; drop near-duplicates."], "quality_checks": ["Deduplicate with similarity thresholds.", "Spot-check outputs for correctness.", "Measure task diversity across the set."], "example_input": "Seed: \"Write a haiku about the sea.\"", "example_output": "New instruction: \"Write a haiku about a desert storm.\" + a valid haiku.", "pitfalls": ["Model-generated errors fossilize into the dataset.", "Diversity collapses without strict filtering."]}, "s": "online", "r": "Wang et al., Self-Instruct, 2022"}, {"t": "Evol-Instruct (complexity evolution)", "c": "instruction-tuning", "d": "Evol-Instruct (complexity evolution) — synthetic data recipe entry.", "f": {"recipe": "Evol-Instruct (complexity evolution)", "use_case": "Growing simple instructions into harder ones to train stronger reasoning.", "method_steps": ["Start from seed instructions.", "Apply evolution prompts: deepen, concretize, add constraints, complicate.", "Generate answers for evolved instructions.", "Filter for correctness and difficulty gain."], "quality_checks": ["Verify evolved answers, not just questions.", "Track difficulty distribution.", "Remove impossible or contradictory items."], "example_input": "Seed: \"Explain photosynthesis.\"", "example_output": "Evolved: \"Explain photosynthesis as a 5-step process, then contrast C3 and C4 pathways in 150 words.\" + answer.", "pitfalls": ["Evolution can produce unanswerable prompts.", "Answers may not keep up with harder questions."]}, "s": "online", "r": "Xu et al., WizardLM / Evol-Instruct, 2023"}, {"t": "Distillation from a teacher model", "c": "instruction-tuning", "d": "Distillation from a teacher model — synthetic data recipe entry.", "f": {"recipe": "Distillation from a teacher model", "use_case": "Creating a compact instruction dataset by collecting a strong model’s answers.", "method_steps": ["Curate a diverse prompt set.", "Collect teacher completions with fixed decoding settings.", "Filter refusals, truncations, and low-quality outputs.", "Fine-tune the student on the cleaned pairs."], "quality_checks": ["Check teacher outputs for hallucinations.", "Balance topics and difficulty.", "Record the teacher version and settings."], "example_input": "Prompt: \"Debug this quicksort.\"", "example_output": "Teacher’s corrected code with explanation.", "pitfalls": ["Student inherits teacher’s blind spots.", "License and terms of the teacher model apply."]}, "s": "online", "r": "Taori et al., Stanford Alpaca, 2023"}, {"t": "TinyStories-style simple-language corpus", "c": "pretraining", "d": "TinyStories-style simple-language corpus — synthetic data recipe entry.", "f": {"recipe": "TinyStories-style simple-language corpus", "use_case": "Training small models on short, simple stories to study emergence of fluent generation.", "method_steps": ["Fix a tiny vocabulary (~1500 words a child knows).", "Generate millions of short stories with a strong model.", "Grammar-check and filter.", "Train small models and probe capabilities."], "quality_checks": ["Vocabulary constraint compliance.", "Story coherence sampling.", "Grammar error rates."], "example_input": "Prompt: \"Write a story with: brave, forest, lantern.\"", "example_output": "A 150-word coherent story using only allowed words.", "pitfalls": ["Simple language limits reasoning depth.", "Stories can be formulaic."]}, "s": "online", "r": "Eldan & Li, TinyStories, 2023"}, {"t": "Rephrased web-text augmentation", "c": "pretraining", "d": "Rephrased web-text augmentation — synthetic data recipe entry.", "f": {"recipe": "Rephrased web-text augmentation", "use_case": "Multiplying pretraining tokens by paraphrasing high-quality documents.", "method_steps": ["Select high-quality source documents.", "Generate 2–3 paraphrases per document with style variation.", "Deduplicate against the original.", "Mix paraphrases with originals at a fixed ratio."], "quality_checks": ["Semantic fidelity checks.", "Near-duplicate detection.", "Perplexity sanity on held-out text."], "example_input": "Source: a science explainer paragraph.", "example_output": "Two paraphrases preserving all facts, different phrasing.", "pitfalls": ["Paraphrases can drift from facts.", "Diminishing returns past a few variants."]}, "s": "signature", "r": null}, {"t": "Synthetic eval-set generation", "c": "evaluation", "d": "Synthetic eval-set generation — synthetic data recipe entry.", "f": {"recipe": "Synthetic eval-set generation", "use_case": "Building fresh test sets that the model has never seen, to avoid contamination.", "method_steps": ["Define the capability and rubric.", "Generate items with a strong model under constraints.", "Human-review a sample for validity.", "Lock the set; never train on it."], "quality_checks": ["Human validity sampling.", "Difficulty calibration.", "Contamination screening."], "example_input": "Spec: \"2-hop factual questions with cited answers.\"", "example_output": "500 vetted questions with gold answers.", "pitfalls": ["Generator blind spots become eval blind spots.", "Leaks happen if the set is reused in training."]}, "s": "signature", "r": null}, {"t": "Execution-verified code pairs", "c": "code", "d": "Execution-verified code pairs — synthetic data recipe entry.", "f": {"recipe": "Execution-verified code pairs", "use_case": "Generating coding problems whose solutions are checked by running tests.", "method_steps": ["Generate problem statements.", "Generate candidate solutions plus unit tests.", "Execute; keep only passing pairs.", "Mutate tests to catch false positives."], "quality_checks": ["All tests must execute.", "Mutation testing on the test suite.", "Problem/solution independence review."], "example_input": "Problem: \"Return the longest palindromic substring.\"", "example_output": "Solution + 8 unit tests, all passing.", "pitfalls": ["Tests may be too weak.", "Problems can be trivially templated."]}, "s": "signature", "r": null}, {"t": "Bug-injection for repair training", "c": "code", "d": "Bug-injection for repair training — synthetic data recipe entry.", "f": {"recipe": "Bug-injection for repair training", "use_case": "Creating debugging data by injecting realistic bugs into correct code.", "method_steps": ["Collect correct programs with tests.", "Inject bug classes: off-by-one, wrong operator, missing guard.", "Record the buggy/fixed diff as the training pair.", "Verify the fixed version passes tests."], "quality_checks": ["Bug realism review.", "Diff minimality.", "Test-pass verification."], "example_input": "Correct: binary search.", "example_output": "Buggy version (off-by-one) + fixed version + explanation.", "pitfalls": ["Injected bugs may look unlike real ones.", "Over-representation of easy bugs."]}, "s": "signature", "r": null}, {"t": "Back-translation augmentation", "c": "low-resource", "d": "Back-translation augmentation — synthetic data recipe entry.", "f": {"recipe": "Back-translation augmentation", "use_case": "Growing parallel data for low-resource languages via round-trip translation.", "method_steps": ["Take monolingual target-language text.", "Translate to a high-resource language and back.", "Keep pairs with high round-trip fidelity.", "Mix with genuine parallel data."], "quality_checks": ["Round-trip fidelity scores.", "Human spot-checks.", "Language-ID verification."], "example_input": "Monolingual sentence in the target language.", "example_output": "A synthetic parallel pair for training.", "pitfalls": ["Translationese artifacts.", "Errors compound across the round trip."]}, "s": "signature", "r": null}, {"t": "Caption-then-QA synthesis", "c": "multimodal", "d": "Caption-then-QA synthesis — synthetic data recipe entry.", "f": {"recipe": "Caption-then-QA synthesis", "use_case": "Generating visual QA pairs from images using a captioning model plus an LLM.", "method_steps": ["Caption images densely.", "Generate QA pairs from captions with an LLM.", "Filter unanswerable or caption-unsupported questions.", "Human-audit a sample."], "quality_checks": ["Caption support check per QA pair.", "Answerability review.", "Visual grounding spot-checks."], "example_input": "Image + dense caption.", "example_output": "5 QA pairs with answers grounded in the caption.", "pitfalls": ["Caption errors propagate into QA.", "Questions may be answerable without the image."]}, "s": "signature", "r": null}];
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
  var errs=[],req=["id", "title", "description", "category", "recipe", "use_case", "method_steps", "quality_checks", "example_output", "source"];
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
  t('extra domain check',function(){var r=generate(9,{},null);return (r.method_steps.length>=3);});
  t('version string',function(){return GEN.version===VERSION;});
  console.log(pass+'/40 '+(fail===0?'PASS':'FAIL'));
  if(fail>0&&typeof process!=='undefined')process.exitCode=1;
}
if(typeof require!=='undefined'&&require.main===module){runTests();}
})();
