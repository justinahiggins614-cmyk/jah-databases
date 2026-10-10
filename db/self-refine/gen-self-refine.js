/* ✳ SIGNATURE — JAH JAH Self-Refine generator. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed + same version always yields the same record.
   Runs in the browser (registered with JAHDB) and in node (self-test below). */
(function(){
'use strict';
var SLUG='self-refine', PREFIX='JAH-SR-', VERSION='jahdb-self-refine-1.0';
var MARK='Signature version in the Signature system. Property of Justin Addam Higgins.';
function hashStr(s){var h=2166136261;s=String(s);for(var i=0;i<s.length;i++){h^=s.charCodeAt(i);h=Math.imul(h,16777619);}return h>>>0;}
function mulberry(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var CATS=["writing", "code", "math", "summarization", "translation", "reasoning"];
var ANGLES=["rubric focus", "critique depth", "single-iteration sprint", "multi-iteration polish", "flaw taxonomy", "score delta study"];
var TOPICS=[{"t": "Write a one-paragraph product description for a sola", "c": "writing", "d": "Write a one-paragraph product description for a sola — self-refine iteration entry.", "f": {"task": "Write a one-paragraph product description for a solar lantern.", "initial_output": "This lantern is good. It has light and solar power. Buy it now for camping.", "identified_flaw": "vague and salesy with no specifics", "critique": ["No concrete specifications (lumens, battery life, weight).", "Hype language (\"Buy it now\") with no evidence.", "No mention of who it is for or when it helps."], "refined_output": "The Solbeam lantern delivers 400 lumens for up to 12 hours on a full solar charge, weighs 320 g, and recharges in 6 hours of sunlight — a dependable light for campers and emergency kits.", "iterations": 2, "score_before": 5.2, "score_after": 8.6, "rubric": "Clarity, specificity, audience fit"}, "s": "signature", "r": null}, {"t": "Draft a polite decline to a meeting invitation.", "c": "writing", "d": "Draft a polite decline to a meeting invitation. — self-refine iteration entry.", "f": {"task": "Draft a polite decline to a meeting invitation.", "initial_output": "No, I cannot come to the meeting. I am busy.", "identified_flaw": "blunt and gives no alternative", "critique": ["Tone is abrupt for professional mail.", "No reason or goodwill is offered.", "No alternative time is proposed."], "refined_output": "Thanks for the invitation — I can’t make Thursday’s meeting due to a conflict, but I’d welcome the notes afterward and can join the follow-up next week if that helps.", "iterations": 2, "score_before": 5.2, "score_after": 8.6, "rubric": "Tone, completeness, professionalism"}, "s": "signature", "r": null}, {"t": "Write a Python function that returns the factorial o", "c": "code", "d": "Write a Python function that returns the factorial o — self-refine iteration entry.", "f": {"task": "Write a Python function that returns the factorial of n.", "initial_output": "def fact(n):\n    r=1\n    for i in range(n): r*=i\n    return r", "identified_flaw": "off-by-one: multiplies by 0", "critique": ["range(n) includes 0, so the result is always 0.", "No handling of negative input.", "No docstring."], "refined_output": "def fact(n):\n    \"\"\"Return n! for non-negative integer n.\"\"\"\n    if n < 0: raise ValueError(\"n must be >= 0\")\n    r = 1\n    for i in range(1, n+1): r *= i\n    return r", "iterations": 2, "score_before": 5.2, "score_after": 8.6, "rubric": "Correctness, edge cases, documentation"}, "s": "signature", "r": null}, {"t": "Write a function that checks whether a string is a p", "c": "code", "d": "Write a function that checks whether a string is a p — self-refine iteration entry.", "f": {"task": "Write a function that checks whether a string is a palindrome.", "initial_output": "def ispal(s): return s == s[::-1]", "identified_flaw": "fails on case and punctuation", "critique": ["\"Racecar\" and \"A man, a plan\" are misjudged.", "No normalization of case or non-letters.", "No docstring or examples."], "refined_output": "def ispal(s):\n    \"\"\"True if s reads the same forward and backward, ignoring case and non-letters.\"\"\"\n    t = \"\".join(c.lower() for c in s if c.isalnum())\n    return t == t[::-1]", "iterations": 2, "score_before": 5.2, "score_after": 8.6, "rubric": "Correctness, robustness, documentation"}, "s": "signature", "r": null}, {"t": "Solve: a store sells 4 apples for $2. How much do 10", "c": "math", "d": "Solve: a store sells 4 apples for $2. How much do 10 — self-refine iteration entry.", "f": {"task": "Solve: a store sells 4 apples for $2. How much do 10 apples cost?", "initial_output": "10 apples cost $4 because 4 is half of 10 roughly.", "identified_flaw": "wrong proportion logic", "critique": ["\"Roughly half\" is not a valid proportion step.", "Unit price ($0.50/apple) was never computed.", "Arithmetic is guessed, not derived."], "refined_output": "Unit price: $2 ÷ 4 = $0.50 per apple. For 10 apples: 10 × $0.50 = $5.00.", "iterations": 2, "score_before": 5.2, "score_after": 8.6, "rubric": "Correct setup, arithmetic, units"}, "s": "signature", "r": null}, {"t": "What is 15% of 240?", "c": "math", "d": "What is 15% of 240? — self-refine iteration entry.", "f": {"task": "What is 15% of 240?", "initial_output": "15% of 240 is 30.", "identified_flaw": "arithmetic error (should be 36)", "critique": ["10% of 240 is 24 and 5% is 12, so 15% is 36, not 30.", "No decomposition shown.", "Answer stated without verification."], "refined_output": "10% of 240 = 24; 5% of 240 = 12; 15% = 24 + 12 = 36.", "iterations": 2, "score_before": 5.2, "score_after": 8.6, "rubric": "Correct method, arithmetic, verification"}, "s": "signature", "r": null}, {"t": "Summarize in one sentence: \"The committee met Tuesda", "c": "summarization", "d": "Summarize in one sentence: \"The committee met Tuesda — self-refine iteration entry.", "f": {"task": "Summarize in one sentence: \"The committee met Tuesday, reviewed three budget proposals, and approved the parks proposal with a 6-2 vote.\"", "initial_output": "People met and did stuff about money.", "identified_flaw": "loses all key facts", "critique": ["Drops the day, the count of proposals, and the vote.", "\"Stuff about money\" is not a summary.", "No outcome stated."], "refined_output": "On Tuesday the committee reviewed three budget proposals and approved the parks proposal 6–2.", "iterations": 2, "score_before": 5.2, "score_after": 8.6, "rubric": "Factual completeness, concision"}, "s": "signature", "r": null}, {"t": "Summarize in one sentence: \"After a two-hour outage,", "c": "summarization", "d": "Summarize in one sentence: \"After a two-hour outage, — self-refine iteration entry.", "f": {"task": "Summarize in one sentence: \"After a two-hour outage, the grid operator restored power to 40,000 homes by 6 pm and blamed a failed transformer.\"", "initial_output": "Power went out somewhere.", "identified_flaw": "missing who, scale, cause, resolution", "critique": ["Omits the operator, 40,000 homes, the 6 pm restoration, and the cause.", "Too vague to be useful.", "No time bounds."], "refined_output": "A failed transformer cut power for two hours; the operator restored 40,000 homes by 6 pm.", "iterations": 2, "score_before": 5.2, "score_after": 8.6, "rubric": "Who/what/when/why coverage"}, "s": "signature", "r": null}, {"t": "Translate to Spanish: \"The library opens at nine.\"", "c": "translation", "d": "Translate to Spanish: \"The library opens at nine.\" — self-refine iteration entry.", "f": {"task": "Translate to Spanish: \"The library opens at nine.\"", "initial_output": "La biblioteca abre a las nueve en punto de la mañana todos los días.", "identified_flaw": "adds information not in the source", "critique": ["\"Todos los días\" (every day) was invented.", "Faithful translation must not add facts.", "Keep it literal and short."], "refined_output": "La biblioteca abre a las nueve.", "iterations": 2, "score_before": 5.2, "score_after": 8.6, "rubric": "Faithfulness, no additions"}, "s": "signature", "r": null}, {"t": "Translate to French: \"She reads every evening.\"", "c": "translation", "d": "Translate to French: \"She reads every evening.\" — self-refine iteration entry.", "f": {"task": "Translate to French: \"She reads every evening.\"", "initial_output": "Elle lit chaque soirée avec un livre intéressant.", "identified_flaw": "adds \"with an interesting book\"", "critique": ["The source says nothing about a book.", "Added detail breaks faithfulness.", "Tense and agreement are otherwise fine."], "refined_output": "Elle lit tous les soirs.", "iterations": 2, "score_before": 5.2, "score_after": 8.6, "rubric": "Faithfulness, natural phrasing"}, "s": "signature", "r": null}, {"t": "Explain why ice floats on water.", "c": "reasoning", "d": "Explain why ice floats on water. — self-refine iteration entry.", "f": {"task": "Explain why ice floats on water.", "initial_output": "Ice is lighter so it floats.", "identified_flaw": "true but shallow; misses the mechanism", "critique": ["\"Lighter\" is vague — less dense is the precise claim.", "No mention of hydrogen bonding / crystal structure.", "Does not generalize to why most solids sink."], "refined_output": "Ice floats because its hydrogen-bonded crystal lattice holds molecules farther apart than in liquid water, making ice about 9% less dense than the water it displaces.", "iterations": 2, "score_before": 5.2, "score_after": 8.6, "rubric": "Mechanism, precision, completeness"}, "s": "signature", "r": null}, {"t": "Why is the sky blue?", "c": "reasoning", "d": "Why is the sky blue? — self-refine iteration entry.", "f": {"task": "Why is the sky blue?", "initial_output": "Because the sky is blue colored.", "identified_flaw": "circular, explains nothing", "critique": ["Restates the observation as the cause.", "No mention of Rayleigh scattering.", "Does not explain sunsets turning red."], "refined_output": "Sunlight’s short blue wavelengths scatter off air molecules (Rayleigh scattering) far more than red ones, so blue reaches our eyes from all directions.", "iterations": 2, "score_before": 5.2, "score_after": 8.6, "rubric": "Causal mechanism, predictive power"}, "s": "signature", "r": null}];
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
  var errs=[],req=["id", "title", "description", "category", "task", "initial_output", "critique", "refined_output", "source"];
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
  t('extra domain check',function(){var r=generate(9,{},null);return (r.critique.length>=2);});
  t('version string',function(){return GEN.version===VERSION;});
  console.log(pass+'/40 '+(fail===0?'PASS':'FAIL'));
  if(fail>0&&typeof process!=='undefined')process.exitCode=1;
}
if(typeof require!=='undefined'&&require.main===module){runTests();}
})();
