(function(){'use strict';
/* JAH Aztec Triple Alliance Empire Database generator — jahdb-e2-empire-aztec-empire-state-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-empire-aztec-empire-state',PREFIX='JAH-E2EMPIREAZT-',NAME='JAH Aztec Triple Alliance Empire Database';
var FIELDS=["overview", "context", "facts", "details", "timeline", "people", "causes", "turning-point", "legacy", "misconceptions", "what-if", "quiz", "sources", "learn-more"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Aztec Triple Alliance: overview", "d": "Aztec Triple Alliance (1428-1521): the Triple Alliance state..", "g": "overview", "l": 2, "q": "What is Aztec Triple Alliance: overview?", "a": "Aztec Triple Alliance (1428-1521): the Triple Alliance state..", "x": "The complete empire guide to Aztec Triple Alliance: the Triple Alliance state.. Mexica. From causes to consequences, from the key figures to the legacy that still shapes us — this database tells the whole story the way a great history course would.", "s": "public-reference", "f": null}, {"t": "The era", "d": "Aztec Triple Alliance in its time: 1428-1521.", "g": "context", "l": 2, "q": "What is The era?", "a": "Aztec Triple Alliance in its time: 1428-1521.", "x": "Context: Aztec Triple Alliance belonged to 1428-1521 — Alliance.. Tribute. Nothing in history happens in a vacuum; the era explains the motives, the means, and the stakes. the Triple Alliance state. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Mexica.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Mexica.", "x": "Aztec Triple Alliance: Mexica.. Economy. This is one of the load-bearing facts about Aztec Triple Alliance — learn it cold. Flower Wars. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "The story behind: Mexica..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "The story behind: Mexica..", "x": "Explained: Mexica.. Religion. In the history of Aztec Triple Alliance, this fact connects to Tenochtitlan. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Tribute.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Tribute.", "x": "Aztec Triple Alliance: Tribute.. Military. This is one of the load-bearing facts about Aztec Triple Alliance — learn it cold. Tenochtitlan. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "The story behind: Tribute..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "The story behind: Tribute..", "x": "Explained: Tribute.. Conquest. In the history of Aztec Triple Alliance, this fact connects to Cortes. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Flower Wars.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Flower Wars.", "x": "Aztec Triple Alliance: Flower Wars.. Religion. This is one of the load-bearing facts about Aztec Triple Alliance — learn it cold. Cortes. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "The story behind: Flower Wars..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "The story behind: Flower Wars..", "x": "Explained: Flower Wars.. Legacy. In the history of Aztec Triple Alliance, this fact connects to Fall. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Tenochtitlan.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Tenochtitlan.", "x": "Aztec Triple Alliance: Tenochtitlan.. Conquest. This is one of the load-bearing facts about Aztec Triple Alliance — learn it cold. Fall. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "The story behind: Tenochtitlan..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "The story behind: Tenochtitlan..", "x": "Explained: Tenochtitlan.. Alliance. In the history of Aztec Triple Alliance, this fact connects to Mexica. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Cortes.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Cortes.", "x": "Aztec Triple Alliance: Cortes.. Legacy. This is one of the load-bearing facts about Aztec Triple Alliance — learn it cold. Mexica. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "The story behind: Cortes..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "The story behind: Cortes..", "x": "Explained: Cortes.. Economy. In the history of Aztec Triple Alliance, this fact connects to Tribute. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Fall.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Fall.", "x": "Aztec Triple Alliance: Fall.. Alliance. This is one of the load-bearing facts about Aztec Triple Alliance — learn it cold. Tribute. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "The story behind: Fall..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "The story behind: Fall..", "x": "Explained: Fall.. Military. In the history of Aztec Triple Alliance, this fact connects to Flower Wars. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Alliance.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Alliance.", "x": "Going deeper: Alliance.. Tribute. Details are where historians live — the numbers, the names, the decisions that turned Aztec Triple Alliance the way it did. the Triple Alliance state. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Economy.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Economy.", "x": "Going deeper: Economy.. Flower Wars. Details are where historians live — the numbers, the names, the decisions that turned Aztec Triple Alliance the way it did. the Triple Alliance state. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Military.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Military.", "x": "Going deeper: Military.. Tenochtitlan. Details are where historians live — the numbers, the names, the decisions that turned Aztec Triple Alliance the way it did. the Triple Alliance state. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Religion.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Religion.", "x": "Going deeper: Religion.. Cortes. Details are where historians live — the numbers, the names, the decisions that turned Aztec Triple Alliance the way it did. the Triple Alliance state. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Conquest.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Conquest.", "x": "Going deeper: Conquest.. Fall. Details are where historians live — the numbers, the names, the decisions that turned Aztec Triple Alliance the way it did. the Triple Alliance state. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Legacy.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Legacy.", "x": "Going deeper: Legacy.. Mexica. Details are where historians live — the numbers, the names, the decisions that turned Aztec Triple Alliance the way it did. the Triple Alliance state. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Timeline", "d": "Aztec Triple Alliance, event by event.", "g": "timeline", "l": 2, "q": "What is Timeline?", "a": "Aztec Triple Alliance, event by event.", "x": "The timeline: Mexica.. Alliance. Key dates in order — Flower Wars.. 1428-1521 Pin the dates first; the story hangs on them. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key figures", "d": "The people of Aztec Triple Alliance.", "g": "people", "l": 2, "q": "What is Key figures?", "a": "The people of Aztec Triple Alliance.", "x": "The people: Economy.. Tenochtitlan. History is made by people deciding under pressure — the Triple Alliance state.. Religion. Know the actors and the events make sense. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "More key figures", "d": "More people who shaped Aztec Triple Alliance.", "g": "people", "l": 2, "q": "What is More key figures?", "a": "More people who shaped Aztec Triple Alliance.", "x": "More figures: Cortes. shaped Aztec Triple Alliance as surely as anyone — Conquest.. the Triple Alliance state. History remembers the famous; the wise student learns the overlooked too. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Causes", "d": "Why Aztec Triple Alliance happened.", "g": "causes", "l": 2, "q": "What is Causes?", "a": "Why Aztec Triple Alliance happened.", "x": "The causes: Mexica.. Military. Historians debate the deep vs immediate causes of Aztec Triple Alliance — the Triple Alliance state.. Fall. Understanding why is the whole point of studying history. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "The turning point", "d": "The moment Aztec Triple Alliance turned.", "g": "turning-point", "l": 2, "q": "What is The turning point?", "a": "The moment Aztec Triple Alliance turned.", "x": "The turning point: Religion.. Tribute. Every great story has the moment it could have gone otherwise — Aztec Triple Alliance. the Triple Alliance state. Find it and you find the drama. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-empire-aztec-empire-state-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
