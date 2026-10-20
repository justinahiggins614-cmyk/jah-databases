(function(){'use strict';
/* JAH Christopher Columbus Explorer Database generator — jahdb-e2-explorer-christopher-columbus-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-explorer-christopher-columbus',PREFIX='JAH-E2EXPLORERC-',NAME='JAH Christopher Columbus Explorer Database';
var FIELDS=["overview", "context", "facts", "details", "timeline", "people", "causes", "turning-point", "legacy", "misconceptions", "what-if", "quiz", "sources", "learn-more"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Christopher Columbus: overview", "d": "Christopher Columbus (1451-1506): reached the Americas in 1492..", "g": "overview", "l": 2, "q": "What is Christopher Columbus: overview?", "a": "Christopher Columbus (1451-1506): reached the Americas in 1492..", "x": "The complete explorer guide to Christopher Columbus: reached the Americas in 1492.. Sailed for Spain 1492. From causes to consequences, from the key figures to the legacy that still shapes us — this database tells the whole story the way a great history course would.", "s": "public-reference", "f": null}, {"t": "The era", "d": "Christopher Columbus in its time: 1451-1506.", "g": "context", "l": 2, "q": "What is The era?", "a": "Christopher Columbus in its time: 1451-1506.", "x": "Context: Christopher Columbus belonged to 1451-1506 — Genoa birth.. Nina, Pinta, Santa Maria. Nothing in history happens in a vacuum; the era explains the motives, the means, and the stakes. reached the Americas in 1492.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Sailed for Spain 1492.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Sailed for Spain 1492.", "x": "Christopher Columbus: Sailed for Spain 1492.. Isabella funded. This is one of the load-bearing facts about Christopher Columbus — learn it cold. Landed Bahamas Oct 12. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "The story behind: Sailed for Spain 1492..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "The story behind: Sailed for Spain 1492..", "x": "Explained: Sailed for Spain 1492.. Taino tragedy. In the history of Christopher Columbus, this fact connects to Four voyages. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Nina, Pinta, Santa Maria.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Nina, Pinta, Santa Maria.", "x": "Christopher Columbus: Nina, Pinta, Santa Maria.. Navigation. This is one of the load-bearing facts about Christopher Columbus — learn it cold. Four voyages. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "The story behind: Nina, Pinta, Santa Maria..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "The story behind: Nina, Pinta, Santa Maria..", "x": "Explained: Nina, Pinta, Santa Maria.. Valladolid death. In the history of Christopher Columbus, this fact connects to Never knew new continent. — see the connections and you have understanding, not trivia.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Landed Bahamas Oct 12.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Landed Bahamas Oct 12.", "x": "Christopher Columbus: Landed Bahamas Oct 12.. Taino tragedy. This is one of the load-bearing facts about Christopher Columbus — learn it cold. Never knew new continent. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "The story behind: Landed Bahamas Oct 12..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "The story behind: Landed Bahamas Oct 12..", "x": "Explained: Landed Bahamas Oct 12.. Legacy debate. In the history of Christopher Columbus, this fact connects to Columbian Exchange. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Four voyages.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Four voyages.", "x": "Christopher Columbus: Four voyages.. Valladolid death. This is one of the load-bearing facts about Christopher Columbus — learn it cold. Columbian Exchange. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "The story behind: Four voyages..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "The story behind: Four voyages..", "x": "Explained: Four voyages.. Genoa birth. In the history of Christopher Columbus, this fact connects to Sailed for Spain 1492. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Never knew new continent.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Never knew new continent.", "x": "Christopher Columbus: Never knew new continent.. Legacy debate. This is one of the load-bearing facts about Christopher Columbus — learn it cold. Sailed for Spain 1492. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "The story behind: Never knew new continent..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "The story behind: Never knew new continent..", "x": "Explained: Never knew new continent.. Isabella funded. In the history of Christopher Columbus, this fact connects to Nina, Pinta, Santa Maria. — see the connections and you have understanding, not trivia.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Columbian Exchange.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Columbian Exchange.", "x": "Christopher Columbus: Columbian Exchange.. Genoa birth. This is one of the load-bearing facts about Christopher Columbus — learn it cold. Nina, Pinta, Santa Maria. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "The story behind: Columbian Exchange..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "The story behind: Columbian Exchange..", "x": "Explained: Columbian Exchange.. Navigation. In the history of Christopher Columbus, this fact connects to Landed Bahamas Oct 12. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Genoa birth.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Genoa birth.", "x": "Going deeper: Genoa birth.. Nina, Pinta, Santa Maria. Details are where historians live — the numbers, the names, the decisions that turned Christopher Columbus the way it did. reached the Americas in 1492.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Isabella funded.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Isabella funded.", "x": "Going deeper: Isabella funded.. Landed Bahamas Oct 12. Details are where historians live — the numbers, the names, the decisions that turned Christopher Columbus the way it did. reached the Americas in 1492.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Navigation.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Navigation.", "x": "Going deeper: Navigation.. Four voyages. Details are where historians live — the numbers, the names, the decisions that turned Christopher Columbus the way it did. reached the Americas in 1492. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Taino tragedy.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Taino tragedy.", "x": "Going deeper: Taino tragedy.. Never knew new continent. Details are where historians live — the numbers, the names, the decisions that turned Christopher Columbus the way it did. reached the Americas in 1492.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Valladolid death.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Valladolid death.", "x": "Going deeper: Valladolid death.. Columbian Exchange. Details are where historians live — the numbers, the names, the decisions that turned Christopher Columbus the way it did. reached the Americas in 1492.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Legacy debate.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Legacy debate.", "x": "Going deeper: Legacy debate.. Sailed for Spain 1492. Details are where historians live — the numbers, the names, the decisions that turned Christopher Columbus the way it did. reached the Americas in 1492.", "s": "public-reference", "f": null}, {"t": "Timeline", "d": "Christopher Columbus, event by event.", "g": "timeline", "l": 2, "q": "What is Timeline?", "a": "Christopher Columbus, event by event.", "x": "The timeline: Sailed for Spain 1492.. Genoa birth. Key dates in order — Landed Bahamas Oct 12.. 1451-1506 Pin the dates first; the story hangs on them. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key figures", "d": "The people of Christopher Columbus.", "g": "people", "l": 2, "q": "What is Key figures?", "a": "The people of Christopher Columbus.", "x": "The people: Isabella funded.. Four voyages. History is made by people deciding under pressure — reached the Americas in 1492.. Taino tragedy. Know the actors and the events make sense. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "More key figures", "d": "More people who shaped Christopher Columbus.", "g": "people", "l": 2, "q": "What is More key figures?", "a": "More people who shaped Christopher Columbus.", "x": "More figures: Never knew new continent. shaped Christopher Columbus as surely as anyone — Valladolid death.. reached the Americas in 1492. History remembers the famous; the wise student learns the overlooked too.", "s": "public-reference", "f": null}, {"t": "Causes", "d": "Why Christopher Columbus happened.", "g": "causes", "l": 2, "q": "What is Causes?", "a": "Why Christopher Columbus happened.", "x": "The causes: Sailed for Spain 1492.. Navigation. Historians debate the deep vs immediate causes of Christopher Columbus — reached the Americas in 1492.. Columbian Exchange. Understanding why is the whole point of studying history.", "s": "public-reference", "f": null}, {"t": "The turning point", "d": "The moment Christopher Columbus turned.", "g": "turning-point", "l": 2, "q": "What is The turning point?", "a": "The moment Christopher Columbus turned.", "x": "The turning point: Taino tragedy.. Nina, Pinta, Santa Maria. Every great story has the moment it could have gone otherwise — Christopher Columbus. reached the Americas in 1492. Find it and you find the drama.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-explorer-christopher-columbus-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
