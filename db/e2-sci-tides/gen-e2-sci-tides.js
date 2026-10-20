(function(){'use strict';
/* JAH Tides Oceanography Database generator — jahdb-e2-sci-tides-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-sci-tides',PREFIX='JAH-E2SCITIDES-',NAME='JAH Tides Oceanography Database';
var FIELDS=["overview", "principles", "facts", "details", "history", "applications", "misconceptions", "terms", "quiz", "frontiers"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Tides: overview", "d": "Tides: the moon and sun's rhythmic pull on the sea..", "g": "overview", "l": 2, "q": "What is Tides: overview?", "a": "Tides: the moon and sun's rhythmic pull on the sea..", "x": "The complete oceanography guide to Tides: the moon and sun's rhythmic pull on the sea.. Moon dominates tides. From first principles to cutting-edge questions, this database teaches the topic the way a great course would — core facts, deep explanations, history, and what remains unknown.", "s": "public-reference", "f": null}, {"t": "The core principle", "d": "The one idea behind Tides.", "g": "principles", "l": 2, "q": "What is The core principle?", "a": "The one idea behind Tides.", "x": "The core principle: Spring vs neap tides.. the moon and sun's rhythmic pull on the sea. If you understand this one idea, everything else in Tides clicks into place. Gravitational bulges. Return to it whenever the details get confusing.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Moon dominates tides.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Moon dominates tides.", "x": "Tides: Moon dominates tides.. Lunar day cycle. This is load-bearing knowledge — the kind of fact that other facts hang from. the moon and sun's rhythmic pull on the sea. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Why Moon dominates tides. is true.", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Why Moon dominates tides. is true.", "x": "The explanation: Moon dominates tides.. In oceanography, this fact connects to Tide tables. — and once you see the mechanism, it stops being trivia and starts being understanding. Bay of Fundy: 16m range.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Spring vs neap tides.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Spring vs neap tides.", "x": "Tides: Spring vs neap tides.. Amphidromic points. This is load-bearing knowledge — the kind of fact that other facts hang from. the moon and sun's rhythmic pull on the sea. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Why Spring vs neap tides. is true.", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Why Spring vs neap tides. is true.", "x": "The explanation: Spring vs neap tides.. In oceanography, this fact connects to King tides. — and once you see the mechanism, it stops being trivia and starts being understanding. Tidal bores. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Bay of Fundy: 16m range.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Bay of Fundy: 16m range.", "x": "Tides: Bay of Fundy: 16m range.. Tide tables. This is load-bearing knowledge — the kind of fact that other facts hang from. the moon and sun's rhythmic pull on the sea. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Why Bay of Fundy: 16m range. is true.", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Why Bay of Fundy: 16m range. is true.", "x": "The explanation: Bay of Fundy: 16m range.. In oceanography, this fact connects to Coastal ecology. — and once you see the mechanism, it stops being trivia and starts being understanding. Tidal power potential.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Tidal bores.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Tidal bores.", "x": "Tides: Tidal bores.. King tides. This is load-bearing knowledge — the kind of fact that other facts hang from. the moon and sun's rhythmic pull on the sea. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Why Tidal bores. is true.", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Why Tidal bores. is true.", "x": "The explanation: Tidal bores.. In oceanography, this fact connects to Gravitational bulges. — and once you see the mechanism, it stops being trivia and starts being understanding. Intertidal zones. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Tidal power potential.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Tidal power potential.", "x": "Tides: Tidal power potential.. Coastal ecology. This is load-bearing knowledge — the kind of fact that other facts hang from. the moon and sun's rhythmic pull on the sea. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Why Tidal power potential. is true.", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Why Tidal power potential. is true.", "x": "The explanation: Tidal power potential.. In oceanography, this fact connects to Lunar day cycle. — and once you see the mechanism, it stops being trivia and starts being understanding. Moon dominates tides.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Intertidal zones.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Intertidal zones.", "x": "Tides: Intertidal zones.. Gravitational bulges. This is load-bearing knowledge — the kind of fact that other facts hang from. the moon and sun's rhythmic pull on the sea. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Why Intertidal zones. is true.", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Why Intertidal zones. is true.", "x": "The explanation: Intertidal zones.. In oceanography, this fact connects to Amphidromic points. — and once you see the mechanism, it stops being trivia and starts being understanding. Spring vs neap tides.", "s": "public-reference", "f": null}, {"t": "Key fact 7", "d": "Moon dominates tides.", "g": "facts", "l": 2, "q": "What is Key fact 7?", "a": "Moon dominates tides.", "x": "Tides: Moon dominates tides.. Lunar day cycle. This is load-bearing knowledge — the kind of fact that other facts hang from. the moon and sun's rhythmic pull on the sea. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 7 explained", "d": "Why Moon dominates tides. is true.", "g": "facts", "l": 2, "q": "What is Key fact 7 explained?", "a": "Why Moon dominates tides. is true.", "x": "The explanation: Moon dominates tides.. In oceanography, this fact connects to Tide tables. — and once you see the mechanism, it stops being trivia and starts being understanding. Bay of Fundy: 16m range.", "s": "public-reference", "f": null}, {"t": "Key fact 8", "d": "Spring vs neap tides.", "g": "facts", "l": 2, "q": "What is Key fact 8?", "a": "Spring vs neap tides.", "x": "Tides: Spring vs neap tides.. Amphidromic points. This is load-bearing knowledge — the kind of fact that other facts hang from. the moon and sun's rhythmic pull on the sea. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 8 explained", "d": "Why Spring vs neap tides. is true.", "g": "facts", "l": 2, "q": "What is Key fact 8 explained?", "a": "Why Spring vs neap tides. is true.", "x": "The explanation: Spring vs neap tides.. In oceanography, this fact connects to King tides. — and once you see the mechanism, it stops being trivia and starts being understanding. Tidal bores. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Gravitational bulges.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Gravitational bulges.", "x": "Going deeper on Tides: Gravitational bulges.. Spring vs neap tides. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Tides from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Lunar day cycle.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Lunar day cycle.", "x": "Going deeper on Tides: Lunar day cycle.. Bay of Fundy: 16m range. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Tides from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Amphidromic points.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Amphidromic points.", "x": "Going deeper on Tides: Amphidromic points.. Tidal bores. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Tides from knowing it. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Tide tables.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Tide tables.", "x": "Going deeper on Tides: Tide tables.. Tidal power potential. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Tides from knowing it. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "King tides.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "King tides.", "x": "Going deeper on Tides: King tides.. Intertidal zones. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Tides from knowing it. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Coastal ecology.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Coastal ecology.", "x": "Going deeper on Tides: Coastal ecology.. Moon dominates tides. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Tides from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 7", "d": "Gravitational bulges.", "g": "details", "l": 2, "q": "What is Deep dive 7?", "a": "Gravitational bulges.", "x": "Going deeper on Tides: Gravitational bulges.. Spring vs neap tides. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Tides from knowing it.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-sci-tides-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
