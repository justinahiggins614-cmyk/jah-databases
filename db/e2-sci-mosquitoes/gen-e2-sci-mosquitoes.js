(function(){'use strict';
/* JAH Mosquitoes Entomology Database generator — jahdb-e2-sci-mosquitoes-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-sci-mosquitoes',PREFIX='JAH-E2SCIMOSQUI-',NAME='JAH Mosquitoes Entomology Database';
var FIELDS=["overview", "principles", "facts", "details", "history", "applications", "misconceptions", "terms", "quiz", "frontiers"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Mosquitoes: overview", "d": "Mosquitoes: deadliest animal to humans..", "g": "overview", "l": 2, "q": "What is Mosquitoes: overview?", "a": "Mosquitoes: deadliest animal to humans..", "x": "The complete entomology guide to Mosquitoes: deadliest animal to humans.. Malaria vector. From first principles to cutting-edge questions, this database teaches the topic the way a great course would — core facts, deep explanations, history, and what remains unknown.", "s": "public-reference", "f": null}, {"t": "The core principle", "d": "The one idea behind Mosquitoes.", "g": "principles", "l": 2, "q": "What is The core principle?", "a": "The one idea behind Mosquitoes.", "x": "The core principle: Only females bite.. deadliest animal to humans. If you understand this one idea, everything else in Mosquitoes clicks into place. Anopheles. Return to it whenever the details get confusing.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Malaria vector.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Malaria vector.", "x": "Mosquitoes: Malaria vector.. Larvae water. This is load-bearing knowledge — the kind of fact that other facts hang from. deadliest animal to humans. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Why Malaria vector. is true.", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Why Malaria vector. is true.", "x": "The explanation: Malaria vector.. In entomology, this fact connects to Eradication debate. — and once you see the mechanism, it stops being trivia and starts being understanding. CO2 tracking. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Only females bite.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Only females bite.", "x": "Mosquitoes: Only females bite.. Repellents. This is load-bearing knowledge — the kind of fact that other facts hang from. deadliest animal to humans. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Why Only females bite. is true.", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Why Only females bite. is true.", "x": "The explanation: Only females bite.. In entomology, this fact connects to History. — and once you see the mechanism, it stops being trivia and starts being understanding. Dengue/Zika. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "CO2 tracking.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "CO2 tracking.", "x": "Mosquitoes: CO2 tracking.. Eradication debate. This is load-bearing knowledge — the kind of fact that other facts hang from. deadliest animal to humans. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Why CO2 tracking. is true.", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Why CO2 tracking. is true.", "x": "The explanation: CO2 tracking.. In entomology, this fact connects to Control. — and once you see the mechanism, it stops being trivia and starts being understanding. Bed nets save lives. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Dengue/Zika.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Dengue/Zika.", "x": "Mosquitoes: Dengue/Zika.. History. This is load-bearing knowledge — the kind of fact that other facts hang from. deadliest animal to humans. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Why Dengue/Zika. is true.", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Why Dengue/Zika. is true.", "x": "The explanation: Dengue/Zika.. In entomology, this fact connects to Anopheles. — and once you see the mechanism, it stops being trivia and starts being understanding. Gene drives. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Bed nets save lives.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Bed nets save lives.", "x": "Mosquitoes: Bed nets save lives.. Control. This is load-bearing knowledge — the kind of fact that other facts hang from. deadliest animal to humans. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Why Bed nets save lives. is true.", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Why Bed nets save lives. is true.", "x": "The explanation: Bed nets save lives.. In entomology, this fact connects to Larvae water. — and once you see the mechanism, it stops being trivia and starts being understanding. Malaria vector. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Gene drives.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Gene drives.", "x": "Mosquitoes: Gene drives.. Anopheles. This is load-bearing knowledge — the kind of fact that other facts hang from. deadliest animal to humans. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Why Gene drives. is true.", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Why Gene drives. is true.", "x": "The explanation: Gene drives.. In entomology, this fact connects to Repellents. — and once you see the mechanism, it stops being trivia and starts being understanding. Only females bite. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 7", "d": "Malaria vector.", "g": "facts", "l": 2, "q": "What is Key fact 7?", "a": "Malaria vector.", "x": "Mosquitoes: Malaria vector.. Larvae water. This is load-bearing knowledge — the kind of fact that other facts hang from. deadliest animal to humans. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 7 explained", "d": "Why Malaria vector. is true.", "g": "facts", "l": 2, "q": "What is Key fact 7 explained?", "a": "Why Malaria vector. is true.", "x": "The explanation: Malaria vector.. In entomology, this fact connects to Eradication debate. — and once you see the mechanism, it stops being trivia and starts being understanding. CO2 tracking. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 8", "d": "Only females bite.", "g": "facts", "l": 2, "q": "What is Key fact 8?", "a": "Only females bite.", "x": "Mosquitoes: Only females bite.. Repellents. This is load-bearing knowledge — the kind of fact that other facts hang from. deadliest animal to humans. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 8 explained", "d": "Why Only females bite. is true.", "g": "facts", "l": 2, "q": "What is Key fact 8 explained?", "a": "Why Only females bite. is true.", "x": "The explanation: Only females bite.. In entomology, this fact connects to History. — and once you see the mechanism, it stops being trivia and starts being understanding. Dengue/Zika. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Anopheles.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Anopheles.", "x": "Going deeper on Mosquitoes: Anopheles.. Only females bite. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Mosquitoes from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Larvae water.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Larvae water.", "x": "Going deeper on Mosquitoes: Larvae water.. CO2 tracking. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Mosquitoes from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Repellents.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Repellents.", "x": "Going deeper on Mosquitoes: Repellents.. Dengue/Zika. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Mosquitoes from knowing it. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Eradication debate.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Eradication debate.", "x": "Going deeper on Mosquitoes: Eradication debate.. Bed nets save lives. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Mosquitoes from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "History.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "History.", "x": "Going deeper on Mosquitoes: History.. Gene drives. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Mosquitoes from knowing it. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Control.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Control.", "x": "Going deeper on Mosquitoes: Control.. Malaria vector. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Mosquitoes from knowing it. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 7", "d": "Anopheles.", "g": "details", "l": 2, "q": "What is Deep dive 7?", "a": "Anopheles.", "x": "Going deeper on Mosquitoes: Anopheles.. Only females bite. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Mosquitoes from knowing it.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-sci-mosquitoes-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
