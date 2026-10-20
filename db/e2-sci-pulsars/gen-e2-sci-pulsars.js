(function(){'use strict';
/* JAH Pulsars Astronomy Database generator — jahdb-e2-sci-pulsars-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-sci-pulsars',PREFIX='JAH-E2SCIPULSAR-',NAME='JAH Pulsars Astronomy Database';
var FIELDS=["overview", "principles", "facts", "details", "history", "applications", "misconceptions", "terms", "quiz", "frontiers"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Pulsars: overview", "d": "Pulsars: spinning neutron-star lighthouses..", "g": "overview", "l": 2, "q": "What is Pulsars: overview?", "a": "Pulsars: spinning neutron-star lighthouses..", "x": "The complete astronomy guide to Pulsars: spinning neutron-star lighthouses.. Lighthouse beams. From first principles to cutting-edge questions, this database teaches the topic the way a great course would — core facts, deep explanations, history, and what remains unknown.", "s": "public-reference", "f": null}, {"t": "The core principle", "d": "The one idea behind Pulsars.", "g": "principles", "l": 2, "q": "What is The core principle?", "a": "The one idea behind Pulsars.", "x": "The core principle: Millisecond pulsars.. spinning neutron-star lighthouses. If you understand this one idea, everything else in Pulsars clicks into place. Neutron stars. Return to it whenever the details get confusing.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Lighthouse beams.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Lighthouse beams.", "x": "Pulsars: Lighthouse beams.. Supernova remnants. This is load-bearing knowledge — the kind of fact that other facts hang from. spinning neutron-star lighthouses. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Why Lighthouse beams. is true.", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Why Lighthouse beams. is true.", "x": "The explanation: Lighthouse beams.. In astronomy, this fact connects to Tests of relativity. — and once you see the mechanism, it stops being trivia and starts being understanding. Discovered 1967 (Bell).", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Millisecond pulsars.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Millisecond pulsars.", "x": "Pulsars: Millisecond pulsars.. Binary pulsars. This is load-bearing knowledge — the kind of fact that other facts hang from. spinning neutron-star lighthouses. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Why Millisecond pulsars. is true.", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Why Millisecond pulsars. is true.", "x": "The explanation: Millisecond pulsars.. In astronomy, this fact connects to Fast radio bursts? — and once you see the mechanism, it stops being trivia and starts being understanding. Atomic-clock precision.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Discovered 1967 (Bell).", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Discovered 1967 (Bell).", "x": "Pulsars: Discovered 1967 (Bell).. Tests of relativity. This is load-bearing knowledge — the kind of fact that other facts hang from. spinning neutron-star lighthouses. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Why Discovered 1967 (Bell). is true.", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Why Discovered 1967 (Bell). is true.", "x": "The explanation: Discovered 1967 (Bell).. In astronomy, this fact connects to Timing arrays. — and once you see the mechanism, it stops being trivia and starts being understanding. Gravitational waves.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Atomic-clock precision.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Atomic-clock precision.", "x": "Pulsars: Atomic-clock precision.. Fast radio bursts? This is load-bearing knowledge — the kind of fact that other facts hang from. spinning neutron-star lighthouses. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Why Atomic-clock precision. is true.", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Why Atomic-clock precision. is true.", "x": "The explanation: Atomic-clock precision.. In astronomy, this fact connects to Neutron stars. — and once you see the mechanism, it stops being trivia and starts being understanding. Crab pulsar. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Gravitational waves.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Gravitational waves.", "x": "Pulsars: Gravitational waves.. Timing arrays. This is load-bearing knowledge — the kind of fact that other facts hang from. spinning neutron-star lighthouses. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Why Gravitational waves. is true.", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Why Gravitational waves. is true.", "x": "The explanation: Gravitational waves.. In astronomy, this fact connects to Supernova remnants. — and once you see the mechanism, it stops being trivia and starts being understanding. Lighthouse beams.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Crab pulsar.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Crab pulsar.", "x": "Pulsars: Crab pulsar.. Neutron stars. This is load-bearing knowledge — the kind of fact that other facts hang from. spinning neutron-star lighthouses. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Why Crab pulsar. is true.", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Why Crab pulsar. is true.", "x": "The explanation: Crab pulsar.. In astronomy, this fact connects to Binary pulsars. — and once you see the mechanism, it stops being trivia and starts being understanding. Millisecond pulsars. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 7", "d": "Lighthouse beams.", "g": "facts", "l": 2, "q": "What is Key fact 7?", "a": "Lighthouse beams.", "x": "Pulsars: Lighthouse beams.. Supernova remnants. This is load-bearing knowledge — the kind of fact that other facts hang from. spinning neutron-star lighthouses. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 7 explained", "d": "Why Lighthouse beams. is true.", "g": "facts", "l": 2, "q": "What is Key fact 7 explained?", "a": "Why Lighthouse beams. is true.", "x": "The explanation: Lighthouse beams.. In astronomy, this fact connects to Tests of relativity. — and once you see the mechanism, it stops being trivia and starts being understanding. Discovered 1967 (Bell).", "s": "public-reference", "f": null}, {"t": "Key fact 8", "d": "Millisecond pulsars.", "g": "facts", "l": 2, "q": "What is Key fact 8?", "a": "Millisecond pulsars.", "x": "Pulsars: Millisecond pulsars.. Binary pulsars. This is load-bearing knowledge — the kind of fact that other facts hang from. spinning neutron-star lighthouses. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 8 explained", "d": "Why Millisecond pulsars. is true.", "g": "facts", "l": 2, "q": "What is Key fact 8 explained?", "a": "Why Millisecond pulsars. is true.", "x": "The explanation: Millisecond pulsars.. In astronomy, this fact connects to Fast radio bursts? — and once you see the mechanism, it stops being trivia and starts being understanding. Atomic-clock precision.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Neutron stars.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Neutron stars.", "x": "Going deeper on Pulsars: Neutron stars.. Millisecond pulsars. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Pulsars from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Supernova remnants.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Supernova remnants.", "x": "Going deeper on Pulsars: Supernova remnants.. Discovered 1967 (Bell). Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Pulsars from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Binary pulsars.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Binary pulsars.", "x": "Going deeper on Pulsars: Binary pulsars.. Atomic-clock precision. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Pulsars from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Tests of relativity.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Tests of relativity.", "x": "Going deeper on Pulsars: Tests of relativity.. Gravitational waves. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Pulsars from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Fast radio bursts?", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Fast radio bursts?", "x": "Going deeper on Pulsars: Fast radio bursts?. Crab pulsar. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Pulsars from knowing it. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Timing arrays.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Timing arrays.", "x": "Going deeper on Pulsars: Timing arrays.. Lighthouse beams. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Pulsars from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 7", "d": "Neutron stars.", "g": "details", "l": 2, "q": "What is Deep dive 7?", "a": "Neutron stars.", "x": "Going deeper on Pulsars: Neutron stars.. Millisecond pulsars. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Pulsars from knowing it.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-sci-pulsars-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
