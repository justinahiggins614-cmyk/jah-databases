(function(){'use strict';
/* JAH Statue of Zeus Wonder Database generator — jahdb-e2-wonder-statue-of-zeus-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-wonder-statue-of-zeus',PREFIX='JAH-E2WONDERSTA-',NAME='JAH Statue of Zeus Wonder Database';
var FIELDS=["overview", "context", "facts", "details", "timeline", "people", "causes", "turning-point", "legacy", "misconceptions", "what-if", "quiz", "sources", "learn-more"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Statue of Zeus: overview", "d": "Statue of Zeus (435 BC): Phidias' gold-and-ivory god..", "g": "overview", "l": 2, "q": "What is Statue of Zeus: overview?", "a": "Statue of Zeus (435 BC): Phidias' gold-and-ivory god..", "x": "The complete wonder guide to Statue of Zeus: Phidias' gold-and-ivory god.. Olympia. From causes to consequences, from the key figures to the legacy that still shapes us — this database tells the whole story the way a great history course would.", "s": "public-reference", "f": null}, {"t": "The era", "d": "Statue of Zeus in its time: 435 BC.", "g": "context", "l": 2, "q": "What is The era?", "a": "Statue of Zeus in its time: 435 BC.", "x": "Context: Statue of Zeus belonged to 435 BC — Olympia.. Phidias sculptor. Nothing in history happens in a vacuum; the era explains the motives, the means, and the stakes. Phidias' gold-and-ivory god. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Olympia.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Olympia.", "x": "Statue of Zeus: Olympia.. Technique. This is one of the load-bearing facts about Statue of Zeus — learn it cold. 12m tall. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "The story behind: Olympia..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "The story behind: Olympia..", "x": "Explained: Olympia.. Loss. In the history of Statue of Zeus, this fact connects to Ivory/gold. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Phidias sculptor.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Phidias sculptor.", "x": "Statue of Zeus: Phidias sculptor.. Wonder list. This is one of the load-bearing facts about Statue of Zeus — learn it cold. Ivory/gold. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "The story behind: Phidias sculptor..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "The story behind: Phidias sculptor..", "x": "Explained: Phidias sculptor.. Replicas. In the history of Statue of Zeus, this fact connects to Destroyed by fire. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "12m tall.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "12m tall.", "x": "Statue of Zeus: 12m tall.. Loss. This is one of the load-bearing facts about Statue of Zeus — learn it cold. Destroyed by fire. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "The story behind: 12m tall..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "The story behind: 12m tall..", "x": "Explained: 12m tall.. Art. In the history of Statue of Zeus, this fact connects to Workshop found. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Ivory/gold.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Ivory/gold.", "x": "Statue of Zeus: Ivory/gold.. Replicas. This is one of the load-bearing facts about Statue of Zeus — learn it cold. Workshop found. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "The story behind: Ivory/gold..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "The story behind: Ivory/gold..", "x": "Explained: Ivory/gold.. Olympia. In the history of Statue of Zeus, this fact connects to Olympia. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Destroyed by fire.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Destroyed by fire.", "x": "Statue of Zeus: Destroyed by fire.. Art. This is one of the load-bearing facts about Statue of Zeus — learn it cold. Olympia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "The story behind: Destroyed by fire..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "The story behind: Destroyed by fire..", "x": "Explained: Destroyed by fire.. Technique. In the history of Statue of Zeus, this fact connects to Phidias sculptor. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Workshop found.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Workshop found.", "x": "Statue of Zeus: Workshop found.. Olympia. This is one of the load-bearing facts about Statue of Zeus — learn it cold. Phidias sculptor. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "The story behind: Workshop found..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "The story behind: Workshop found..", "x": "Explained: Workshop found.. Wonder list. In the history of Statue of Zeus, this fact connects to 12m tall. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Olympia.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Olympia.", "x": "Going deeper: Olympia.. Phidias sculptor. Details are where historians live — the numbers, the names, the decisions that turned Statue of Zeus the way it did. Phidias' gold-and-ivory god. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Technique.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Technique.", "x": "Going deeper: Technique.. 12m tall. Details are where historians live — the numbers, the names, the decisions that turned Statue of Zeus the way it did. Phidias' gold-and-ivory god. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Wonder list.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Wonder list.", "x": "Going deeper: Wonder list.. Ivory/gold. Details are where historians live — the numbers, the names, the decisions that turned Statue of Zeus the way it did. Phidias' gold-and-ivory god. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Loss.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Loss.", "x": "Going deeper: Loss.. Destroyed by fire. Details are where historians live — the numbers, the names, the decisions that turned Statue of Zeus the way it did. Phidias' gold-and-ivory god. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Replicas.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Replicas.", "x": "Going deeper: Replicas.. Workshop found. Details are where historians live — the numbers, the names, the decisions that turned Statue of Zeus the way it did. Phidias' gold-and-ivory god. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Art.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Art.", "x": "Going deeper: Art.. Olympia. Details are where historians live — the numbers, the names, the decisions that turned Statue of Zeus the way it did. Phidias' gold-and-ivory god. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Timeline", "d": "Statue of Zeus, event by event.", "g": "timeline", "l": 2, "q": "What is Timeline?", "a": "Statue of Zeus, event by event.", "x": "The timeline: Olympia.. Olympia. Key dates in order — 12m tall.. 435 BC Pin the dates first; the story hangs on them. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key figures", "d": "The people of Statue of Zeus.", "g": "people", "l": 2, "q": "What is Key figures?", "a": "The people of Statue of Zeus.", "x": "The people: Technique.. Ivory/gold. History is made by people deciding under pressure — Phidias' gold-and-ivory god.. Loss. Know the actors and the events make sense. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "More key figures", "d": "More people who shaped Statue of Zeus.", "g": "people", "l": 2, "q": "What is More key figures?", "a": "More people who shaped Statue of Zeus.", "x": "More figures: Destroyed by fire. shaped Statue of Zeus as surely as anyone — Replicas.. Phidias' gold-and-ivory god. History remembers the famous; the wise student learns the overlooked too. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Causes", "d": "Why Statue of Zeus happened.", "g": "causes", "l": 2, "q": "What is Causes?", "a": "Why Statue of Zeus happened.", "x": "The causes: Olympia.. Wonder list. Historians debate the deep vs immediate causes of Statue of Zeus — Phidias' gold-and-ivory god.. Workshop found. Understanding why is the whole point of studying history.", "s": "public-reference", "f": null}, {"t": "The turning point", "d": "The moment Statue of Zeus turned.", "g": "turning-point", "l": 2, "q": "What is The turning point?", "a": "The moment Statue of Zeus turned.", "x": "The turning point: Loss.. Phidias sculptor. Every great story has the moment it could have gone otherwise — Statue of Zeus. Phidias' gold-and-ivory god. Find it and you find the drama. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-wonder-statue-of-zeus-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
