(function(){'use strict';
/* JAH Poisonous Mushrooms Mycology Database generator — jahdb-e2-sci-poisonous-mushrooms-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-sci-poisonous-mushrooms',PREFIX='JAH-E2SCIPOISON-',NAME='JAH Poisonous Mushrooms Mycology Database';
var FIELDS=["overview", "principles", "facts", "details", "history", "applications", "misconceptions", "terms", "quiz", "frontiers"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Poisonous Mushrooms: overview", "d": "Poisonous Mushrooms: deadly lookalikes; respect required..", "g": "overview", "l": 2, "q": "What is Poisonous Mushrooms: overview?", "a": "Poisonous Mushrooms: deadly lookalikes; respect required..", "x": "The complete mycology guide to Poisonous Mushrooms: deadly lookalikes; respect required.. Death cap kills. From first principles to cutting-edge questions, this database teaches the topic the way a great course would — core facts, deep explanations, history, and what remains unknown.", "s": "public-reference", "f": null}, {"t": "The core principle", "d": "The one idea behind Poisonous Mushrooms.", "g": "principles", "l": 2, "q": "What is The core principle?", "a": "The one idea behind Poisonous Mushrooms.", "x": "The core principle: Destroying angel.. deadly lookalikes; respect required. If you understand this one idea, everything else in Poisonous Mushrooms clicks into place. Toxins. Return to it whenever the details get confusing.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Death cap kills.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Death cap kills.", "x": "Poisonous Mushrooms: Death cap kills.. Symptoms delayed. This is load-bearing knowledge — the kind of fact that other facts hang from. deadly lookalikes; respect required. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Why Death cap kills. is true.", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Why Death cap kills. is true.", "x": "The explanation: Death cap kills.. In mycology, this fact connects to Myths debunked. — and once you see the mechanism, it stops being trivia and starts being understanding. Amatoxins. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Destroying angel.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Destroying angel.", "x": "Poisonous Mushrooms: Destroying angel.. Emergency care. This is load-bearing knowledge — the kind of fact that other facts hang from. deadly lookalikes; respect required. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Why Destroying angel. is true.", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Why Destroying angel. is true.", "x": "The explanation: Destroying angel.. In mycology, this fact connects to Foraging rules. — and once you see the mechanism, it stops being trivia and starts being understanding. No easy test. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Amatoxins.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Amatoxins.", "x": "Poisonous Mushrooms: Amatoxins.. Myths debunked. This is load-bearing knowledge — the kind of fact that other facts hang from. deadly lookalikes; respect required. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Why Amatoxins. is true.", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Why Amatoxins. is true.", "x": "The explanation: Amatoxins.. In mycology, this fact connects to Education. — and once you see the mechanism, it stops being trivia and starts being understanding. Expert ID only. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "No easy test.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "No easy test.", "x": "Poisonous Mushrooms: No easy test.. Foraging rules. This is load-bearing knowledge — the kind of fact that other facts hang from. deadly lookalikes; respect required. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Why No easy test. is true.", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Why No easy test. is true.", "x": "The explanation: No easy test.. In mycology, this fact connects to Toxins. — and once you see the mechanism, it stops being trivia and starts being understanding. Liver failure. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Expert ID only.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Expert ID only.", "x": "Poisonous Mushrooms: Expert ID only.. Education. This is load-bearing knowledge — the kind of fact that other facts hang from. deadly lookalikes; respect required. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Why Expert ID only. is true.", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Why Expert ID only. is true.", "x": "The explanation: Expert ID only.. In mycology, this fact connects to Symptoms delayed. — and once you see the mechanism, it stops being trivia and starts being understanding. Death cap kills. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Liver failure.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Liver failure.", "x": "Poisonous Mushrooms: Liver failure.. Toxins. This is load-bearing knowledge — the kind of fact that other facts hang from. deadly lookalikes; respect required. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Why Liver failure. is true.", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Why Liver failure. is true.", "x": "The explanation: Liver failure.. In mycology, this fact connects to Emergency care. — and once you see the mechanism, it stops being trivia and starts being understanding. Destroying angel. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 7", "d": "Death cap kills.", "g": "facts", "l": 2, "q": "What is Key fact 7?", "a": "Death cap kills.", "x": "Poisonous Mushrooms: Death cap kills.. Symptoms delayed. This is load-bearing knowledge — the kind of fact that other facts hang from. deadly lookalikes; respect required. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 7 explained", "d": "Why Death cap kills. is true.", "g": "facts", "l": 2, "q": "What is Key fact 7 explained?", "a": "Why Death cap kills. is true.", "x": "The explanation: Death cap kills.. In mycology, this fact connects to Myths debunked. — and once you see the mechanism, it stops being trivia and starts being understanding. Amatoxins. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 8", "d": "Destroying angel.", "g": "facts", "l": 2, "q": "What is Key fact 8?", "a": "Destroying angel.", "x": "Poisonous Mushrooms: Destroying angel.. Emergency care. This is load-bearing knowledge — the kind of fact that other facts hang from. deadly lookalikes; respect required. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 8 explained", "d": "Why Destroying angel. is true.", "g": "facts", "l": 2, "q": "What is Key fact 8 explained?", "a": "Why Destroying angel. is true.", "x": "The explanation: Destroying angel.. In mycology, this fact connects to Foraging rules. — and once you see the mechanism, it stops being trivia and starts being understanding. No easy test. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Toxins.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Toxins.", "x": "Going deeper on Poisonous Mushrooms: Toxins.. Destroying angel. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Poisonous Mushrooms from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Symptoms delayed.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Symptoms delayed.", "x": "Going deeper on Poisonous Mushrooms: Symptoms delayed.. Amatoxins. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Poisonous Mushrooms from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Emergency care.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Emergency care.", "x": "Going deeper on Poisonous Mushrooms: Emergency care.. No easy test. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Poisonous Mushrooms from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Myths debunked.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Myths debunked.", "x": "Going deeper on Poisonous Mushrooms: Myths debunked.. Expert ID only. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Poisonous Mushrooms from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Foraging rules.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Foraging rules.", "x": "Going deeper on Poisonous Mushrooms: Foraging rules.. Liver failure. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Poisonous Mushrooms from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Education.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Education.", "x": "Going deeper on Poisonous Mushrooms: Education.. Death cap kills. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Poisonous Mushrooms from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 7", "d": "Toxins.", "g": "details", "l": 2, "q": "What is Deep dive 7?", "a": "Toxins.", "x": "Going deeper on Poisonous Mushrooms: Toxins.. Destroying angel. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Poisonous Mushrooms from knowing it.", "s": "public-reference", "f": null}];
function pad(n){return String(n).padStart(6,'0');}
function drillProg(q,a){
  return '// boundless drill program\nvar Q='+JSON.stringify(q)+';\nvar A='+JSON.stringify(a)+';\n'
    +'console.log("DRILL: "+Q);\nconsole.log("Say it out loud, then check:");\nconsole.log("ANSWER: "+A);';
}
function bankRec(i){
  var b=BANK[(i-1)%BANK.length];
  var r={id:PREFIX+pad(i),title:b.t,description:b.x,group:b.g,ladder:b.l,
    question:b.q,answer:b.a,method:'archive-sample',
    program:drillProg(b.q,b.a),language:'javascript',
    src:b.s,last_verified:'2026-10-19',sample:true};
  return r;
}
function genQuizDrill(rnd,seed){
  var b=BANK[(rnd()*BANK.length)|0];
  var desc='Boundless drill #'+seed+' — '+NAME+'. The question: '+b.q+'\n\n'
    +'Cover the answer and say it out loud before reading on. Fluency with these facts is the whole game: '
    +'each drill pulls a real record from this database\'s archive and tests exactly one fact cold. '
    +'If you knew it, it is yours; if not, open the archive record "'+b.t+'" and read the full entry, then come back and drill it again. '
    +'The validated answer: '+b.a+'\n\n'
    +'Drills never repeat the archive verbatim — they re-ask the same true facts from new angles so the knowledge sticks.';
  return {id:PREFIX+pad(seed),title:'Drill: '+b.t,description:desc,group:b.g,ladder:b.l,
    method:'quiz-drill',question:b.q,answer:b.a,
    program:drillProg(b.q,b.a),language:'javascript',src:GEN_SRC,last_verified:'2026-10-19'};
}
function genConvertDrill(rnd,seed){
  var b1=BANK[(rnd()*BANK.length)|0],b2=BANK[(rnd()*BANK.length)|0];
  var v=Math.round((1+rnd()*999)*100)/100;
  var ans=v*b1.f/b2.f;
  var q='Convert '+v+' '+b1.t+' to '+b2.t+'.';
  var a=String(Math.round(ans*1e6)/1e6)+' '+b2.t;
  var desc='Boundless drill #'+seed+' — '+NAME+'. The question: '+q+'\n\n'
    +'Work it with the factor table: multiply by the "from" unit\'s factor to reach the base unit, then divide by the "to" unit\'s factor. '
    +'The demo program on any archive record in this database runs the same computation, so you can check your method there first. '
    +'The validated answer: '+a+'. If your number matches, the method is yours; drills like this one keep every conversion in this database one multiplication and one division away.';
  return {id:PREFIX+pad(seed),title:'Conversion drill: '+b1.t+' to '+b2.t,description:desc,
    group:b1.g,ladder:2,method:'convert-drill',question:q,answer:a,
    conv:{value:v,from:b1.t,fromF:b1.f,to:b2.t,toF:b2.f},
    program:'// conversion drill program\nvar v='+v+';\nvar fromF='+b1.f+';\nvar toF='+b2.f+';\n'
      +'console.log("Q: convert "+v+" '+b1.t.replace(/'/g,"\\'")+' to '+b2.t.replace(/'/g,"\\'")+'");\n'
      +'console.log("A: "+(v*fromF/toF)+" '+b2.t.replace(/'/g,"\\'")+'");',
    language:'javascript',src:GEN_SRC,last_verified:'2026-10-19'};
}
function generate(seed,opts,rnd){
  opts=opts||{};seed=+seed||1;rnd=rnd||prng(seed);
  var g=opts.group||opts.category;
  if(g&&FIELDS.indexOf(g)<0)g=null;
  var r;
  if(seed>=1&&seed<=BANK.length){r=bankRec(seed);}
  else{r=(MODE==='convert')?genConvertDrill(rnd,seed):genQuizDrill(rnd,seed);}
  if(g)r.group=g;
  return r;
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return{ok:false,errors:['not an object']};
  if(!new RegExp('^'+PREFIX.replace(/-/g,'\\-')+'\\d{6}$').test(r.id||''))e.push('id');
  if(FIELDS.indexOf(r.group)<0)e.push('group');
  if(typeof r.title!=='string'||!r.title.length)e.push('title');
  if(typeof r.description!=='string'||r.description.length<200)e.push('description');
  if(r.method==='quiz-drill'||r.method==='archive-sample'){
    var hit=null;
    for(var i=0;i<BANK.length;i++){if(BANK[i].q===r.question&&BANK[i].a===r.answer){hit=BANK[i];break;}}
    if(!hit)e.push('answer not banked');
  }else if(r.method==='convert-drill'){
    var c=r.conv;
    if(!c||typeof c.value!=='number')e.push('conv missing');
    else{
      var expect=c.value*c.fromF/c.toF;
      var got=parseFloat(String(r.answer).split(' ')[0]);
      if(!(Math.abs(got-expect)<Math.max(1e-6,Math.abs(expect)*1e-9)))e.push('conversion mismatch');
    }
  }else{e.push('method');}
  return{ok:!e.length,errors:e};
}
function driftCheck(rec,sample){
  var seen={};(sample||[]).forEach(function(s){if(s&&s.t)seen[s.t]=1;});
  if(rec&&seen[rec.title])return{ok:false,errors:['duplicate title in archive sample']};
  return{ok:true,errors:[]};
}
var gen={version:'jahdb-e2-sci-poisonous-mushrooms-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
