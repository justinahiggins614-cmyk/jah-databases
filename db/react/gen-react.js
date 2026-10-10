/* ✳ SIGNATURE — JAH JAH ReAct generator. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed + same version always yields the same record.
   Runs in the browser (registered with JAHDB) and in node (self-test below). */
(function(){
'use strict';
var SLUG='react', PREFIX='JAH-REACT-', VERSION='jahdb-react-1.0';
var MARK='Signature version in the Signature system. Property of Justin Addam Higgins.';
function hashStr(s){var h=2166136261;s=String(s);for(var i=0;i<s.length;i++){h^=s.charCodeAt(i);h=Math.imul(h,16777619);}return h>>>0;}
function mulberry(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var CATS=["question-answering", "research", "math-solving", "code-debugging", "planning", "web-navigation"];
var ANGLES=["tool-selection focus", "error recovery", "multi-hop trace", "minimal-step trace", "observation quality", "final-answer check"];
var TOPICS=[{"t": "", "c": "question-answering", "d": "", "f": {}, "s": "signature", "r": null}, {"t": "", "c": "research", "d": "", "f": {}, "s": "signature", "r": null}, {"t": "", "c": "math-solving", "d": "", "f": {}, "s": "signature", "r": null}, {"t": "", "c": "code-debugging", "d": "", "f": {}, "s": "signature", "r": null}, {"t": "", "c": "planning", "d": "", "f": {}, "s": "signature", "r": null}, {"t": "", "c": "web-navigation", "d": "", "f": {}, "s": "signature", "r": null}];
function pickR(rnd,a){return a[(rnd()*a.length)|0];}
function makeId(seed){var n=(typeof seed==='number'?seed:hashStr(String(seed)));return PREFIX+String((n%1000000)+1).padStart(7,'0');}
var R_TASKS=[
 {c:'question-answering',tpl:'Answer this multi-hop question: {q}',tools:['Search','Lookup']},
 {c:'research',tpl:'Compare {x} and {y} for training a chat model, then recommend one.',tools:['Search','Fetch']},
 {c:'math-solving',tpl:'Compute {e} and show the value.',tools:['Calculator']},
 {c:'code-debugging',tpl:'Diagnose and fix this bug: {bug}',tools:['ReadFile','RunCode']},
 {c:'planning',tpl:'Plan a {n}-day {theme} itinerary with a daily budget of ${b}.',tools:['Search','Calendar']},
 {c:'web-navigation',tpl:'Find the official documentation for {x} and report its main sections.',tools:['Search','Click','Scroll']}];
var R_Q=[['Who directed the film that won Best Picture at the 2020 Academy Awards?','Bong Joon-ho','Parasite won Best Picture at the 2020 ceremony; directed by Bong Joon-ho.'],['What is the capital of Australia?','Canberra','Search results confirm Canberra is the capital of Australia.'],['How many moons does Mars have?','2','Mars has two small moons: Phobos and Deimos.']];
var R_M=[['(12 + 8) * 7 - 40','100'],['3**4 + 2**5','113'],['144 / 12 + 7 * 3','33']];
var R_B=[['def add(a, b): return a - b','It subtracts instead of adding; change - to +.'],['if x = 5: print("five")','Assignment used instead of comparison; use ==.']];
var R_X=['RLHF','DPO','chain-of-thought prompting','retrieval-augmented generation','constitutional AI'];
function fill(tpl,rnd,extra){var m={x:pickR(rnd,R_X),y:pickR(rnd,R_X),n:String(3+((rnd()*5)|0)),theme:pickR(rnd,['museum','hiking','food','history']),b:pickR(rnd,['80','120','200'])};
  for(var k in (extra||{}))m[k]=extra[k];
  return tpl.replace(/\{(\w+)\}/g,function(mm,k){return m[k]!==undefined?m[k]:mm;});}
function compose(seed,rnd,T,cat){
  var A=pickR(rnd,ANGLES);
  var pool=R_TASKS.filter(function(t){return !((T&&T.c)||cat)||t.c===((T&&T.c)||cat);});
  if(!pool.length)pool=R_TASKS;
  var tk=pickR(rnd,pool),task,traj,final;
  if(tk.c==='question-answering'){var q=pickR(rnd,R_Q);task=fill(tk.tpl,rnd,{q:q[0]});final=q[1];
    traj=[{thought:'I need to answer: "'+q[0]+'". Let me search.',action:'Search['+q[0].slice(0,50)+']',observation:'Results point to the relevant facts.'},{thought:'I will look up the specific detail.',action:'Lookup['+q[0].slice(0,35)+']',observation:q[2]},{thought:'I can now answer directly.',action:'Finish['+final+']',observation:'Answer recorded.'}];}
  else if(tk.c==='math-solving'){var mm=pickR(rnd,R_M);task=fill(tk.tpl,rnd,{e:mm[0]});final=mm[1];
    traj=[{thought:'I need to compute '+mm[0]+'.',action:'Calculator['+mm[0]+']',observation:'The tool returns '+mm[1]+'.'},{thought:'Value confirmed.',action:'Finish['+mm[1]+']',observation:'Answer recorded.'}];}
  else if(tk.c==='code-debugging'){var bg=pickR(rnd,R_B);task=fill(tk.tpl,rnd,{bug:bg[0]});final=bg[1];
    traj=[{thought:'I will read the buggy code first.',action:'ReadFile[buggy_module.py]',observation:'The suspect code is confirmed.'},{thought:'Diagnosis: '+bg[1],action:'RunCode[verify_fix.py]',observation:'All checks pass after the fix.'},{thought:'Fix verified.',action:'Finish[fixed]',observation:'Answer recorded.'}];}
  else{task=fill(tk.tpl,rnd);final='Completed: '+task;
    traj=[{thought:'Task: "'+task.slice(0,55)+'". I will gather information.',action:tk.tools[0]+'['+task.slice(0,45)+']',observation:'Relevant material retrieved.'},{thought:'Now specifics with '+tk.tools[tk.tools.length-1]+'.',action:tk.tools[tk.tools.length-1]+'[details]',observation:'Details retrieved.'},{thought:'I have enough to finish.',action:'Finish[composed answer]',observation:'Answer recorded.'}];}
  return {title:tk.c.replace(/-/g,' ')+' trace \u2014 '+A,
    description:'A '+tk.c+' ReAct trajectory ('+traj.length+' tool rounds, '+A+').',
    category:tk.c,task:task,tools:tk.tools,trajectory:traj,rounds:traj.length,final_answer:final,focus:A};
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
  var errs=[],req=["id", "title", "description", "category", "task", "tools", "trajectory", "final_answer", "source"];
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
  t('extra domain check',function(){var r=generate(9,{},null);return (r.trajectory.length>=2);});
  t('version string',function(){return GEN.version===VERSION;});
  console.log(pass+'/40 '+(fail===0?'PASS':'FAIL'));
  if(fail>0&&typeof process!=='undefined')process.exitCode=1;
}
if(typeof require!=='undefined'&&require.main===module){runTests();}
})();
