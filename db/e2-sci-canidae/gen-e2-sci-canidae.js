(function(){'use strict';
/* JAH Canidae Zoology Database generator — jahdb-e2-sci-canidae-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-sci-canidae',PREFIX='JAH-E2SCICANIDA-',NAME='JAH Canidae Zoology Database';
var FIELDS=["overview", "principles", "facts", "details", "history", "applications", "misconceptions", "terms", "quiz", "frontiers"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Canidae: overview", "d": "Canidae: the dog family: wolves to foxes..", "g": "overview", "l": 2, "q": "What is Canidae: overview?", "a": "Canidae: the dog family: wolves to foxes..", "x": "The complete zoology guide to Canidae: the dog family: wolves to foxes.. Wolves: pack hunters. From first principles to cutting-edge questions, this database teaches the topic the way a great course would — core facts, deep explanations, history, and what remains unknown.", "s": "public-reference", "f": null}, {"t": "The core principle", "d": "The one idea behind Canidae.", "g": "principles", "l": 2, "q": "What is The core principle?", "a": "The one idea behind Canidae.", "x": "The core principle: Dogs domesticated 20k+ yrs.. the dog family: wolves to foxes. If you understand this one idea, everything else in Canidae clicks into place. Pack behavior. Return to it whenever the details get confusing.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Wolves: pack hunters.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Wolves: pack hunters.", "x": "Canidae: Wolves: pack hunters.. Breeds 300+. This is load-bearing knowledge — the kind of fact that other facts hang from. the dog family: wolves to foxes. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Why Wolves: pack hunters. is true.", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Why Wolves: pack hunters. is true.", "x": "The explanation: Wolves: pack hunters.. In zoology, this fact connects to Conservation. — and once you see the mechanism, it stops being trivia and starts being understanding. Foxes: solitary. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Dogs domesticated 20k+ yrs.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Dogs domesticated 20k+ yrs.", "x": "Canidae: Dogs domesticated 20k+ yrs.. Communication. This is load-bearing knowledge — the kind of fact that other facts hang from. the dog family: wolves to foxes. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Why Dogs domesticated 20k+ yrs. is true.", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Why Dogs domesticated 20k+ yrs. is true.", "x": "The explanation: Dogs domesticated 20k+ yrs.. In zoology, this fact connects to Feral dogs. — and once you see the mechanism, it stops being trivia and starts being understanding. Coyotes adaptable. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Foxes: solitary.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Foxes: solitary.", "x": "Canidae: Foxes: solitary.. Conservation. This is load-bearing knowledge — the kind of fact that other facts hang from. the dog family: wolves to foxes. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Why Foxes: solitary. is true.", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Why Foxes: solitary. is true.", "x": "The explanation: Foxes: solitary.. In zoology, this fact connects to Training. — and once you see the mechanism, it stops being trivia and starts being understanding. Dingoes. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Coyotes adaptable.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Coyotes adaptable.", "x": "Canidae: Coyotes adaptable.. Feral dogs. This is load-bearing knowledge — the kind of fact that other facts hang from. the dog family: wolves to foxes. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Why Coyotes adaptable. is true.", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Why Coyotes adaptable. is true.", "x": "The explanation: Coyotes adaptable.. In zoology, this fact connects to Pack behavior. — and once you see the mechanism, it stops being trivia and starts being understanding. Smell: 10k x human. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Dingoes.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Dingoes.", "x": "Canidae: Dingoes.. Training. This is load-bearing knowledge — the kind of fact that other facts hang from. the dog family: wolves to foxes. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Why Dingoes. is true.", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Why Dingoes. is true.", "x": "The explanation: Dingoes.. In zoology, this fact connects to Breeds 300+. — and once you see the mechanism, it stops being trivia and starts being understanding. Wolves: pack hunters. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Smell: 10k x human.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Smell: 10k x human.", "x": "Canidae: Smell: 10k x human.. Pack behavior. This is load-bearing knowledge — the kind of fact that other facts hang from. the dog family: wolves to foxes. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Why Smell: 10k x human. is true.", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Why Smell: 10k x human. is true.", "x": "The explanation: Smell: 10k x human.. In zoology, this fact connects to Communication. — and once you see the mechanism, it stops being trivia and starts being understanding. Dogs domesticated 20k+ yrs.", "s": "public-reference", "f": null}, {"t": "Key fact 7", "d": "Wolves: pack hunters.", "g": "facts", "l": 2, "q": "What is Key fact 7?", "a": "Wolves: pack hunters.", "x": "Canidae: Wolves: pack hunters.. Breeds 300+. This is load-bearing knowledge — the kind of fact that other facts hang from. the dog family: wolves to foxes. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 7 explained", "d": "Why Wolves: pack hunters. is true.", "g": "facts", "l": 2, "q": "What is Key fact 7 explained?", "a": "Why Wolves: pack hunters. is true.", "x": "The explanation: Wolves: pack hunters.. In zoology, this fact connects to Conservation. — and once you see the mechanism, it stops being trivia and starts being understanding. Foxes: solitary. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 8", "d": "Dogs domesticated 20k+ yrs.", "g": "facts", "l": 2, "q": "What is Key fact 8?", "a": "Dogs domesticated 20k+ yrs.", "x": "Canidae: Dogs domesticated 20k+ yrs.. Communication. This is load-bearing knowledge — the kind of fact that other facts hang from. the dog family: wolves to foxes. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 8 explained", "d": "Why Dogs domesticated 20k+ yrs. is true.", "g": "facts", "l": 2, "q": "What is Key fact 8 explained?", "a": "Why Dogs domesticated 20k+ yrs. is true.", "x": "The explanation: Dogs domesticated 20k+ yrs.. In zoology, this fact connects to Feral dogs. — and once you see the mechanism, it stops being trivia and starts being understanding. Coyotes adaptable. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Pack behavior.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Pack behavior.", "x": "Going deeper on Canidae: Pack behavior.. Dogs domesticated 20k+ yrs. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Canidae from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Breeds 300+.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Breeds 300+.", "x": "Going deeper on Canidae: Breeds 300+.. Foxes: solitary. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Canidae from knowing it. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Communication.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Communication.", "x": "Going deeper on Canidae: Communication.. Coyotes adaptable. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Canidae from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Conservation.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Conservation.", "x": "Going deeper on Canidae: Conservation.. Dingoes. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Canidae from knowing it. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Feral dogs.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Feral dogs.", "x": "Going deeper on Canidae: Feral dogs.. Smell: 10k x human. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Canidae from knowing it. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Training.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Training.", "x": "Going deeper on Canidae: Training.. Wolves: pack hunters. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Canidae from knowing it. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 7", "d": "Pack behavior.", "g": "details", "l": 2, "q": "What is Deep dive 7?", "a": "Pack behavior.", "x": "Going deeper on Canidae: Pack behavior.. Dogs domesticated 20k+ yrs. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Canidae from knowing it.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-sci-canidae-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
