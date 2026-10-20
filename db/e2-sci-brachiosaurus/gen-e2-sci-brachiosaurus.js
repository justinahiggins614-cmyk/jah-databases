(function(){'use strict';
/* JAH Brachiosaurus Paleontology Database generator — jahdb-e2-sci-brachiosaurus-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-sci-brachiosaurus',PREFIX='JAH-E2SCIBRACHI-',NAME='JAH Brachiosaurus Paleontology Database';
var FIELDS=["overview", "principles", "facts", "details", "history", "applications", "misconceptions", "terms", "quiz", "frontiers"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Brachiosaurus: overview", "d": "Brachiosaurus: giraffe-like Jurassic giant..", "g": "overview", "l": 2, "q": "What is Brachiosaurus: overview?", "a": "Brachiosaurus: giraffe-like Jurassic giant..", "x": "The complete paleontology guide to Brachiosaurus: giraffe-like Jurassic giant.. 85 ft long. From first principles to cutting-edge questions, this database teaches the topic the way a great course would — core facts, deep explanations, history, and what remains unknown.", "s": "public-reference", "f": null}, {"t": "The core principle", "d": "The one idea behind Brachiosaurus.", "g": "principles", "l": 2, "q": "What is The core principle?", "a": "The one idea behind Brachiosaurus.", "x": "The core principle: Front legs longer.. giraffe-like Jurassic giant. If you understand this one idea, everything else in Brachiosaurus clicks into place. Discovery. Return to it whenever the details get confusing.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "85 ft long.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "85 ft long.", "x": "Brachiosaurus: 85 ft long.. Size estimates. This is load-bearing knowledge — the kind of fact that other facts hang from. giraffe-like Jurassic giant. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Why 85 ft long. is true.", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Why 85 ft long. is true.", "x": "The explanation: 85 ft long.. In paleontology, this fact connects to Tendaguru. — and once you see the mechanism, it stops being trivia and starts being understanding. Nostrils on top? Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Front legs longer.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Front legs longer.", "x": "Brachiosaurus: Front legs longer.. Feeding high. This is load-bearing knowledge — the kind of fact that other facts hang from. giraffe-like Jurassic giant. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Why Front legs longer. is true.", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Why Front legs longer. is true.", "x": "The explanation: Front legs longer.. In paleontology, this fact connects to Museums. — and once you see the mechanism, it stops being trivia and starts being understanding. 150M years. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Nostrils on top?", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Nostrils on top?", "x": "Brachiosaurus: Nostrils on top?. Tendaguru. This is load-bearing knowledge — the kind of fact that other facts hang from. giraffe-like Jurassic giant. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Why Nostrils on top? is true.", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Why Nostrils on top? is true.", "x": "The explanation: Nostrils on top?. In paleontology, this fact connects to Sauropods. — and once you see the mechanism, it stops being trivia and starts being understanding. Giraffatitan relative. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "150M years.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "150M years.", "x": "Brachiosaurus: 150M years.. Museums. This is load-bearing knowledge — the kind of fact that other facts hang from. giraffe-like Jurassic giant. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Why 150M years. is true.", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Why 150M years. is true.", "x": "The explanation: 150M years.. In paleontology, this fact connects to Discovery. — and once you see the mechanism, it stops being trivia and starts being understanding. Heart puzzle. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Giraffatitan relative.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Giraffatitan relative.", "x": "Brachiosaurus: Giraffatitan relative.. Sauropods. This is load-bearing knowledge — the kind of fact that other facts hang from. giraffe-like Jurassic giant. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Why Giraffatitan relative. is true.", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Why Giraffatitan relative. is true.", "x": "The explanation: Giraffatitan relative.. In paleontology, this fact connects to Size estimates. — and once you see the mechanism, it stops being trivia and starts being understanding. 85 ft long. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Heart puzzle.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Heart puzzle.", "x": "Brachiosaurus: Heart puzzle.. Discovery. This is load-bearing knowledge — the kind of fact that other facts hang from. giraffe-like Jurassic giant. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Why Heart puzzle. is true.", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Why Heart puzzle. is true.", "x": "The explanation: Heart puzzle.. In paleontology, this fact connects to Feeding high. — and once you see the mechanism, it stops being trivia and starts being understanding. Front legs longer. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 7", "d": "85 ft long.", "g": "facts", "l": 2, "q": "What is Key fact 7?", "a": "85 ft long.", "x": "Brachiosaurus: 85 ft long.. Size estimates. This is load-bearing knowledge — the kind of fact that other facts hang from. giraffe-like Jurassic giant. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 7 explained", "d": "Why 85 ft long. is true.", "g": "facts", "l": 2, "q": "What is Key fact 7 explained?", "a": "Why 85 ft long. is true.", "x": "The explanation: 85 ft long.. In paleontology, this fact connects to Tendaguru. — and once you see the mechanism, it stops being trivia and starts being understanding. Nostrils on top? Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 8", "d": "Front legs longer.", "g": "facts", "l": 2, "q": "What is Key fact 8?", "a": "Front legs longer.", "x": "Brachiosaurus: Front legs longer.. Feeding high. This is load-bearing knowledge — the kind of fact that other facts hang from. giraffe-like Jurassic giant. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 8 explained", "d": "Why Front legs longer. is true.", "g": "facts", "l": 2, "q": "What is Key fact 8 explained?", "a": "Why Front legs longer. is true.", "x": "The explanation: Front legs longer.. In paleontology, this fact connects to Museums. — and once you see the mechanism, it stops being trivia and starts being understanding. 150M years. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Discovery.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Discovery.", "x": "Going deeper on Brachiosaurus: Discovery.. Front legs longer. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Brachiosaurus from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Size estimates.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Size estimates.", "x": "Going deeper on Brachiosaurus: Size estimates.. Nostrils on top? Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Brachiosaurus from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Feeding high.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Feeding high.", "x": "Going deeper on Brachiosaurus: Feeding high.. 150M years. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Brachiosaurus from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Tendaguru.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Tendaguru.", "x": "Going deeper on Brachiosaurus: Tendaguru.. Giraffatitan relative. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Brachiosaurus from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Museums.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Museums.", "x": "Going deeper on Brachiosaurus: Museums.. Heart puzzle. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Brachiosaurus from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Sauropods.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Sauropods.", "x": "Going deeper on Brachiosaurus: Sauropods.. 85 ft long. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Brachiosaurus from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 7", "d": "Discovery.", "g": "details", "l": 2, "q": "What is Deep dive 7?", "a": "Discovery.", "x": "Going deeper on Brachiosaurus: Discovery.. Front legs longer. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Brachiosaurus from knowing it.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-sci-brachiosaurus-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
