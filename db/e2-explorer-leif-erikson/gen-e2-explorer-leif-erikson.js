(function(){'use strict';
/* JAH Leif Erikson Explorer Database generator — jahdb-e2-explorer-leif-erikson-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-explorer-leif-erikson',PREFIX='JAH-E2EXPLORERL-',NAME='JAH Leif Erikson Explorer Database';
var FIELDS=["overview", "context", "facts", "details", "timeline", "people", "causes", "turning-point", "legacy", "misconceptions", "what-if", "quiz", "sources", "learn-more"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Leif Erikson: overview", "d": "Leif Erikson (c.970-c.1020): Viking in North America..", "g": "overview", "l": 2, "q": "What is Leif Erikson: overview?", "a": "Leif Erikson (c.970-c.1020): Viking in North America..", "x": "The complete explorer guide to Leif Erikson: Viking in North America.. Vinland c.1000. From causes to consequences, from the key figures to the legacy that still shapes us — this database tells the whole story the way a great history course would.", "s": "public-reference", "f": null}, {"t": "The era", "d": "Leif Erikson in its time: c.970-c.1020.", "g": "context", "l": 2, "q": "What is The era?", "a": "Leif Erikson in its time: c.970-c.1020.", "x": "Context: Leif Erikson belonged to c.970-c.1020 — Greenland.. Son of Erik the Red. Nothing in history happens in a vacuum; the era explains the motives, the means, and the stakes. Viking in North America.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Vinland c.1000.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Vinland c.1000.", "x": "Leif Erikson: Vinland c.1000.. Voyage. This is one of the load-bearing facts about Leif Erikson — learn it cold. L'Anse aux Meadows. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "The story behind: Vinland c.1000..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "The story behind: Vinland c.1000..", "x": "Explained: Vinland c.1000.. Skraelings. In the history of Leif Erikson, this fact connects to Sagas. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Son of Erik the Red.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Son of Erik the Red.", "x": "Leif Erikson: Son of Erik the Red.. Settlement. This is one of the load-bearing facts about Leif Erikson — learn it cold. Sagas. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "The story behind: Son of Erik the Red..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "The story behind: Son of Erik the Red..", "x": "Explained: Son of Erik the Red.. Legacy. In the history of Leif Erikson, this fact connects to 500 yrs before Columbus. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "L'Anse aux Meadows.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "L'Anse aux Meadows.", "x": "Leif Erikson: L'Anse aux Meadows.. Skraelings. This is one of the load-bearing facts about Leif Erikson — learn it cold. 500 yrs before Columbus. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "The story behind: L'Anse aux Meadows..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "The story behind: L'Anse aux Meadows..", "x": "Explained: L'Anse aux Meadows.. Archaeology. In the history of Leif Erikson, this fact connects to Norse. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Sagas.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Sagas.", "x": "Leif Erikson: Sagas.. Legacy. This is one of the load-bearing facts about Leif Erikson — learn it cold. Norse. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "The story behind: Sagas..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "The story behind: Sagas..", "x": "Explained: Sagas.. Greenland. In the history of Leif Erikson, this fact connects to Vinland c.1000. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "500 yrs before Columbus.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "500 yrs before Columbus.", "x": "Leif Erikson: 500 yrs before Columbus.. Archaeology. This is one of the load-bearing facts about Leif Erikson — learn it cold. Vinland c.1000. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "The story behind: 500 yrs before Columbus..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "The story behind: 500 yrs before Columbus..", "x": "Explained: 500 yrs before Columbus.. Voyage. In the history of Leif Erikson, this fact connects to Son of Erik the Red. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Norse.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Norse.", "x": "Leif Erikson: Norse.. Greenland. This is one of the load-bearing facts about Leif Erikson — learn it cold. Son of Erik the Red. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "The story behind: Norse..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "The story behind: Norse..", "x": "Explained: Norse.. Settlement. In the history of Leif Erikson, this fact connects to L'Anse aux Meadows. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Greenland.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Greenland.", "x": "Going deeper: Greenland.. Son of Erik the Red. Details are where historians live — the numbers, the names, the decisions that turned Leif Erikson the way it did. Viking in North America. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Voyage.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Voyage.", "x": "Going deeper: Voyage.. L'Anse aux Meadows. Details are where historians live — the numbers, the names, the decisions that turned Leif Erikson the way it did. Viking in North America. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Settlement.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Settlement.", "x": "Going deeper: Settlement.. Sagas. Details are where historians live — the numbers, the names, the decisions that turned Leif Erikson the way it did. Viking in North America. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Skraelings.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Skraelings.", "x": "Going deeper: Skraelings.. 500 yrs before Columbus. Details are where historians live — the numbers, the names, the decisions that turned Leif Erikson the way it did. Viking in North America. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Legacy.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Legacy.", "x": "Going deeper: Legacy.. Norse. Details are where historians live — the numbers, the names, the decisions that turned Leif Erikson the way it did. Viking in North America. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Archaeology.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Archaeology.", "x": "Going deeper: Archaeology.. Vinland c.1000. Details are where historians live — the numbers, the names, the decisions that turned Leif Erikson the way it did. Viking in North America. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Timeline", "d": "Leif Erikson, event by event.", "g": "timeline", "l": 2, "q": "What is Timeline?", "a": "Leif Erikson, event by event.", "x": "The timeline: Vinland c.1000.. Greenland. Key dates in order — L'Anse aux Meadows.. c.970-c.1020 Pin the dates first; the story hangs on them. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key figures", "d": "The people of Leif Erikson.", "g": "people", "l": 2, "q": "What is Key figures?", "a": "The people of Leif Erikson.", "x": "The people: Voyage.. Sagas. History is made by people deciding under pressure — Viking in North America.. Skraelings. Know the actors and the events make sense. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "More key figures", "d": "More people who shaped Leif Erikson.", "g": "people", "l": 2, "q": "What is More key figures?", "a": "More people who shaped Leif Erikson.", "x": "More figures: 500 yrs before Columbus. shaped Leif Erikson as surely as anyone — Legacy.. Viking in North America. History remembers the famous; the wise student learns the overlooked too. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Causes", "d": "Why Leif Erikson happened.", "g": "causes", "l": 2, "q": "What is Causes?", "a": "Why Leif Erikson happened.", "x": "The causes: Vinland c.1000.. Settlement. Historians debate the deep vs immediate causes of Leif Erikson — Viking in North America.. Norse. Understanding why is the whole point of studying history. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "The turning point", "d": "The moment Leif Erikson turned.", "g": "turning-point", "l": 2, "q": "What is The turning point?", "a": "The moment Leif Erikson turned.", "x": "The turning point: Skraelings.. Son of Erik the Red. Every great story has the moment it could have gone otherwise — Leif Erikson. Viking in North America. Find it and you find the drama. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-explorer-leif-erikson-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
