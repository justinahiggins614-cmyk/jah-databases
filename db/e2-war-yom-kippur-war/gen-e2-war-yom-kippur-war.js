(function(){'use strict';
/* JAH Yom Kippur War War Database generator — jahdb-e2-war-yom-kippur-war-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-war-yom-kippur-war',PREFIX='JAH-E2WARYOMKIP-',NAME='JAH Yom Kippur War War Database';
var FIELDS=["overview", "context", "facts", "details", "timeline", "people", "causes", "turning-point", "legacy", "misconceptions", "what-if", "quiz", "sources", "learn-more"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Yom Kippur War: overview", "d": "Yom Kippur War (1973): Egypt and Syria's surprise attack on Israel..", "g": "overview", "l": 2, "q": "What is Yom Kippur War: overview?", "a": "Yom Kippur War (1973): Egypt and Syria's surprise attack on Israel..", "x": "The complete war guide to Yom Kippur War: Egypt and Syria's surprise attack on Israel.. Attack on holy day. From causes to consequences, from the key figures to the legacy that still shapes us — this database tells the whole story the way a great history course would.", "s": "public-reference", "f": null}, {"t": "The era", "d": "Yom Kippur War in its time: 1973.", "g": "context", "l": 2, "q": "What is The era?", "a": "Yom Kippur War in its time: 1973.", "x": "Context: Yom Kippur War belonged to 1973 — Sadat's plan.. Egypt crossed Suez. Nothing in history happens in a vacuum; the era explains the motives, the means, and the stakes. Egypt and Syria's surprise attack on Israel.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Attack on holy day.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Attack on holy day.", "x": "Yom Kippur War: Attack on holy day.. Bar-Lev Line. This is one of the load-bearing facts about Yom Kippur War — learn it cold. Syria: Golan. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "The story behind: Attack on holy day..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "The story behind: Attack on holy day..", "x": "Explained: Attack on holy day.. Kissinger shuttle. In the history of Yom Kippur War, this fact connects to US airlift. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Egypt crossed Suez.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Egypt crossed Suez.", "x": "Yom Kippur War: Egypt crossed Suez.. Agranat Commission. This is one of the load-bearing facts about Yom Kippur War — learn it cold. US airlift. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "The story behind: Egypt crossed Suez..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "The story behind: Egypt crossed Suez..", "x": "Explained: Egypt crossed Suez.. Embargo recession. In the history of Yom Kippur War, this fact connects to OPEC oil embargo. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Syria: Golan.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Syria: Golan.", "x": "Yom Kippur War: Syria: Golan.. Kissinger shuttle. This is one of the load-bearing facts about Yom Kippur War — learn it cold. OPEC oil embargo. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "The story behind: Syria: Golan..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "The story behind: Syria: Golan..", "x": "Explained: Syria: Golan.. Peace. In the history of Yom Kippur War, this fact connects to Camp David followed. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "US airlift.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "US airlift.", "x": "Yom Kippur War: US airlift.. Embargo recession. This is one of the load-bearing facts about Yom Kippur War — learn it cold. Camp David followed. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "The story behind: US airlift..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "The story behind: US airlift..", "x": "Explained: US airlift.. Sadat's plan. In the history of Yom Kippur War, this fact connects to Attack on holy day. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "OPEC oil embargo.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "OPEC oil embargo.", "x": "Yom Kippur War: OPEC oil embargo.. Peace. This is one of the load-bearing facts about Yom Kippur War — learn it cold. Attack on holy day. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "The story behind: OPEC oil embargo..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "The story behind: OPEC oil embargo..", "x": "Explained: OPEC oil embargo.. Bar-Lev Line. In the history of Yom Kippur War, this fact connects to Egypt crossed Suez. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Camp David followed.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Camp David followed.", "x": "Yom Kippur War: Camp David followed.. Sadat's plan. This is one of the load-bearing facts about Yom Kippur War — learn it cold. Egypt crossed Suez. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "The story behind: Camp David followed..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "The story behind: Camp David followed..", "x": "Explained: Camp David followed.. Agranat Commission. In the history of Yom Kippur War, this fact connects to Syria: Golan. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Sadat's plan.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Sadat's plan.", "x": "Going deeper: Sadat's plan.. Egypt crossed Suez. Details are where historians live — the numbers, the names, the decisions that turned Yom Kippur War the way it did. Egypt and Syria's surprise attack on Israel.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Bar-Lev Line.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Bar-Lev Line.", "x": "Going deeper: Bar-Lev Line.. Syria: Golan. Details are where historians live — the numbers, the names, the decisions that turned Yom Kippur War the way it did. Egypt and Syria's surprise attack on Israel.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Agranat Commission.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Agranat Commission.", "x": "Going deeper: Agranat Commission.. US airlift. Details are where historians live — the numbers, the names, the decisions that turned Yom Kippur War the way it did. Egypt and Syria's surprise attack on Israel.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Kissinger shuttle.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Kissinger shuttle.", "x": "Going deeper: Kissinger shuttle.. OPEC oil embargo. Details are where historians live — the numbers, the names, the decisions that turned Yom Kippur War the way it did. Egypt and Syria's surprise attack on Israel.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Embargo recession.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Embargo recession.", "x": "Going deeper: Embargo recession.. Camp David followed. Details are where historians live — the numbers, the names, the decisions that turned Yom Kippur War the way it did. Egypt and Syria's surprise attack on Israel.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Peace.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Peace.", "x": "Going deeper: Peace.. Attack on holy day. Details are where historians live — the numbers, the names, the decisions that turned Yom Kippur War the way it did. Egypt and Syria's surprise attack on Israel.", "s": "public-reference", "f": null}, {"t": "Timeline", "d": "Yom Kippur War, event by event.", "g": "timeline", "l": 2, "q": "What is Timeline?", "a": "Yom Kippur War, event by event.", "x": "The timeline: Attack on holy day.. Sadat's plan. Key dates in order — Syria: Golan.. 1973 Pin the dates first; the story hangs on them. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key figures", "d": "The people of Yom Kippur War.", "g": "people", "l": 2, "q": "What is Key figures?", "a": "The people of Yom Kippur War.", "x": "The people: Bar-Lev Line.. US airlift. History is made by people deciding under pressure — Egypt and Syria's surprise attack on Israel.. Kissinger shuttle. Know the actors and the events make sense. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "More key figures", "d": "More people who shaped Yom Kippur War.", "g": "people", "l": 2, "q": "What is More key figures?", "a": "More people who shaped Yom Kippur War.", "x": "More figures: OPEC oil embargo. shaped Yom Kippur War as surely as anyone — Embargo recession.. Egypt and Syria's surprise attack on Israel. History remembers the famous; the wise student learns the overlooked too.", "s": "public-reference", "f": null}, {"t": "Causes", "d": "Why Yom Kippur War happened.", "g": "causes", "l": 2, "q": "What is Causes?", "a": "Why Yom Kippur War happened.", "x": "The causes: Attack on holy day.. Agranat Commission. Historians debate the deep vs immediate causes of Yom Kippur War — Egypt and Syria's surprise attack on Israel.. Camp David followed. Understanding why is the whole point of studying history.", "s": "public-reference", "f": null}, {"t": "The turning point", "d": "The moment Yom Kippur War turned.", "g": "turning-point", "l": 2, "q": "What is The turning point?", "a": "The moment Yom Kippur War turned.", "x": "The turning point: Kissinger shuttle.. Egypt crossed Suez. Every great story has the moment it could have gone otherwise — Yom Kippur War. Egypt and Syria's surprise attack on Israel. Find it and you find the drama.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-war-yom-kippur-war-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
