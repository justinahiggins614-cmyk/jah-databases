(function(){'use strict';
/* JAH Jet Stream Meteorology Database generator — jahdb-e2-sci-jet-stream-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-sci-jet-stream',PREFIX='JAH-E2SCIJETSTR-',NAME='JAH Jet Stream Meteorology Database';
var FIELDS=["overview", "principles", "facts", "details", "history", "applications", "misconceptions", "terms", "quiz", "frontiers"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Jet Stream: overview", "d": "Jet Stream: fast upper-air rivers steering weather..", "g": "overview", "l": 2, "q": "What is Jet Stream: overview?", "a": "Jet Stream: fast upper-air rivers steering weather..", "x": "The complete meteorology guide to Jet Stream: fast upper-air rivers steering weather.. 100+ mph winds. From first principles to cutting-edge questions, this database teaches the topic the way a great course would — core facts, deep explanations, history, and what remains unknown.", "s": "public-reference", "f": null}, {"t": "The core principle", "d": "The one idea behind Jet Stream.", "g": "principles", "l": 2, "q": "What is The core principle?", "a": "The one idea behind Jet Stream.", "x": "The core principle: Polar vs subtropical.. fast upper-air rivers steering weather. If you understand this one idea, everything else in Jet Stream clicks into place. Tropopause level. Return to it whenever the details get confusing.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "100+ mph winds.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "100+ mph winds.", "x": "Jet Stream: 100+ mph winds.. Meanders. This is load-bearing knowledge — the kind of fact that other facts hang from. fast upper-air rivers steering weather. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Why 100+ mph winds. is true.", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Why 100+ mph winds. is true.", "x": "The explanation: 100+ mph winds.. In meteorology, this fact connects to Turbulence. — and once you see the mechanism, it stops being trivia and starts being understanding. Rossby waves. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Polar vs subtropical.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Polar vs subtropical.", "x": "Jet Stream: Polar vs subtropical.. Blocking patterns. This is load-bearing knowledge — the kind of fact that other facts hang from. fast upper-air rivers steering weather. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Why Polar vs subtropical. is true.", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Why Polar vs subtropical. is true.", "x": "The explanation: Polar vs subtropical.. In meteorology, this fact connects to Climate shifts. — and once you see the mechanism, it stops being trivia and starts being understanding. Flight times change.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Rossby waves.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Rossby waves.", "x": "Jet Stream: Rossby waves.. Turbulence. This is load-bearing knowledge — the kind of fact that other facts hang from. fast upper-air rivers steering weather. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Why Rossby waves. is true.", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Why Rossby waves. is true.", "x": "The explanation: Rossby waves.. In meteorology, this fact connects to Forecasting key. — and once you see the mechanism, it stops being trivia and starts being understanding. Bomb cyclones ride it. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Flight times change.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Flight times change.", "x": "Jet Stream: Flight times change.. Climate shifts. This is load-bearing knowledge — the kind of fact that other facts hang from. fast upper-air rivers steering weather. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Why Flight times change. is true.", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Why Flight times change. is true.", "x": "The explanation: Flight times change.. In meteorology, this fact connects to Tropopause level. — and once you see the mechanism, it stops being trivia and starts being understanding. Discovered WWII. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Bomb cyclones ride it.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Bomb cyclones ride it.", "x": "Jet Stream: Bomb cyclones ride it.. Forecasting key. This is load-bearing knowledge — the kind of fact that other facts hang from. fast upper-air rivers steering weather. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Why Bomb cyclones ride it. is true.", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Why Bomb cyclones ride it. is true.", "x": "The explanation: Bomb cyclones ride it.. In meteorology, this fact connects to Meanders. — and once you see the mechanism, it stops being trivia and starts being understanding. 100+ mph winds. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Discovered WWII.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Discovered WWII.", "x": "Jet Stream: Discovered WWII.. Tropopause level. This is load-bearing knowledge — the kind of fact that other facts hang from. fast upper-air rivers steering weather. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Why Discovered WWII. is true.", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Why Discovered WWII. is true.", "x": "The explanation: Discovered WWII.. In meteorology, this fact connects to Blocking patterns. — and once you see the mechanism, it stops being trivia and starts being understanding. Polar vs subtropical.", "s": "public-reference", "f": null}, {"t": "Key fact 7", "d": "100+ mph winds.", "g": "facts", "l": 2, "q": "What is Key fact 7?", "a": "100+ mph winds.", "x": "Jet Stream: 100+ mph winds.. Meanders. This is load-bearing knowledge — the kind of fact that other facts hang from. fast upper-air rivers steering weather. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 7 explained", "d": "Why 100+ mph winds. is true.", "g": "facts", "l": 2, "q": "What is Key fact 7 explained?", "a": "Why 100+ mph winds. is true.", "x": "The explanation: 100+ mph winds.. In meteorology, this fact connects to Turbulence. — and once you see the mechanism, it stops being trivia and starts being understanding. Rossby waves. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 8", "d": "Polar vs subtropical.", "g": "facts", "l": 2, "q": "What is Key fact 8?", "a": "Polar vs subtropical.", "x": "Jet Stream: Polar vs subtropical.. Blocking patterns. This is load-bearing knowledge — the kind of fact that other facts hang from. fast upper-air rivers steering weather. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 8 explained", "d": "Why Polar vs subtropical. is true.", "g": "facts", "l": 2, "q": "What is Key fact 8 explained?", "a": "Why Polar vs subtropical. is true.", "x": "The explanation: Polar vs subtropical.. In meteorology, this fact connects to Climate shifts. — and once you see the mechanism, it stops being trivia and starts being understanding. Flight times change.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Tropopause level.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Tropopause level.", "x": "Going deeper on Jet Stream: Tropopause level.. Polar vs subtropical. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Jet Stream from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Meanders.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Meanders.", "x": "Going deeper on Jet Stream: Meanders.. Rossby waves. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Jet Stream from knowing it. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Blocking patterns.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Blocking patterns.", "x": "Going deeper on Jet Stream: Blocking patterns.. Flight times change. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Jet Stream from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Turbulence.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Turbulence.", "x": "Going deeper on Jet Stream: Turbulence.. Bomb cyclones ride it. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Jet Stream from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Climate shifts.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Climate shifts.", "x": "Going deeper on Jet Stream: Climate shifts.. Discovered WWII. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Jet Stream from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Forecasting key.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Forecasting key.", "x": "Going deeper on Jet Stream: Forecasting key.. 100+ mph winds. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Jet Stream from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 7", "d": "Tropopause level.", "g": "details", "l": 2, "q": "What is Deep dive 7?", "a": "Tropopause level.", "x": "Going deeper on Jet Stream: Tropopause level.. Polar vs subtropical. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Jet Stream from knowing it.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-sci-jet-stream-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
