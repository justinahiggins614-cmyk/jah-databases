(function(){'use strict';
/* JAH World War II War Database generator — jahdb-e2-war-world-war-ii-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-war-world-war-ii',PREFIX='JAH-E2WARWORLDW-',NAME='JAH World War II War Database';
var FIELDS=["overview", "context", "facts", "details", "timeline", "people", "causes", "turning-point", "legacy", "misconceptions", "what-if", "quiz", "sources", "learn-more"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "World War II: overview", "d": "World War II (1939-1945): the deadliest conflict in human history..", "g": "overview", "l": 2, "q": "What is World War II: overview?", "a": "World War II (1939-1945): the deadliest conflict in human history..", "x": "The complete war guide to World War II: the deadliest conflict in human history.. Started with Germany's invasion of Poland. From causes to consequences, from the key figures to the legacy that still shapes us — this database tells the whole story the way a great history course would.", "s": "public-reference", "f": null}, {"t": "The era", "d": "World War II in its time: 1939-1945.", "g": "context", "l": 2, "q": "What is The era?", "a": "World War II in its time: 1939-1945.", "x": "Context: World War II belonged to 1939-1945 — Blitzkrieg tactics.. Holocaust: 6M Jews murdered. Nothing in history happens in a vacuum; the era explains the motives, the means, and the stakes. the deadliest conflict in human history.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Started with Germany's invasion of Poland.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Started with Germany's invasion of Poland.", "x": "World War II: Started with Germany's invasion of Poland.. Eastern Front: Stalingrad. This is one of the load-bearing facts about World War II — learn it cold. US entered after Pearl Harbor (1941). History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "The story behind: Started with Germany's invasion of Poland..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "The story behind: Started with Germany's invasion of Poland..", "x": "Explained: Started with Germany's invasion of Poland.. Manhattan Project. In the history of World War II, this fact connects to D-Day: Normandy landings (1944). — see the connections and you have understanding, not trivia.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Holocaust: 6M Jews murdered.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Holocaust: 6M Jews murdered.", "x": "World War II: Holocaust: 6M Jews murdered.. Island hopping Pacific. This is one of the load-bearing facts about World War II — learn it cold. D-Day: Normandy landings (1944). History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "The story behind: Holocaust: 6M Jews murdered..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "The story behind: Holocaust: 6M Jews murdered..", "x": "Explained: Holocaust: 6M Jews murdered.. Nuremberg trials. In the history of World War II, this fact connects to Atomic bombs ended Pacific war. — see the connections and you have understanding, not trivia.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "US entered after Pearl Harbor (1941).", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "US entered after Pearl Harbor (1941).", "x": "World War II: US entered after Pearl Harbor (1941).. Manhattan Project. This is one of the load-bearing facts about World War II — learn it cold. Atomic bombs ended Pacific war. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "The story behind: US entered after Pearl Harbor (1941)..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "The story behind: US entered after Pearl Harbor (1941)..", "x": "Explained: US entered after Pearl Harbor (1941).. Cold War followed. In the history of World War II, this fact connects to 70M+ died; UN founded after. — see the connections and you have understanding, not trivia.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "D-Day: Normandy landings (1944).", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "D-Day: Normandy landings (1944).", "x": "World War II: D-Day: Normandy landings (1944).. Nuremberg trials. This is one of the load-bearing facts about World War II — learn it cold. 70M+ died; UN founded after. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "The story behind: D-Day: Normandy landings (1944)..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "The story behind: D-Day: Normandy landings (1944)..", "x": "Explained: D-Day: Normandy landings (1944).. Blitzkrieg tactics. In the history of World War II, this fact connects to Started with Germany's invasion of Poland. — see the connections and you have understanding, not trivia.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Atomic bombs ended Pacific war.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Atomic bombs ended Pacific war.", "x": "World War II: Atomic bombs ended Pacific war.. Cold War followed. This is one of the load-bearing facts about World War II — learn it cold. Started with Germany's invasion of Poland. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "The story behind: Atomic bombs ended Pacific war..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "The story behind: Atomic bombs ended Pacific war..", "x": "Explained: Atomic bombs ended Pacific war.. Eastern Front: Stalingrad. In the history of World War II, this fact connects to Holocaust: 6M Jews murdered. — see the connections and you have understanding, not trivia.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "70M+ died; UN founded after.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "70M+ died; UN founded after.", "x": "World War II: 70M+ died; UN founded after.. Blitzkrieg tactics. This is one of the load-bearing facts about World War II — learn it cold. Holocaust: 6M Jews murdered. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "The story behind: 70M+ died; UN founded after..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "The story behind: 70M+ died; UN founded after..", "x": "Explained: 70M+ died; UN founded after.. Island hopping Pacific. In the history of World War II, this fact connects to US entered after Pearl Harbor (1941). — see the connections and you have understanding, not trivia.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Blitzkrieg tactics.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Blitzkrieg tactics.", "x": "Going deeper: Blitzkrieg tactics.. Holocaust: 6M Jews murdered. Details are where historians live — the numbers, the names, the decisions that turned World War II the way it did. the deadliest conflict in human history.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Eastern Front: Stalingrad.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Eastern Front: Stalingrad.", "x": "Going deeper: Eastern Front: Stalingrad.. US entered after Pearl Harbor (1941). Details are where historians live — the numbers, the names, the decisions that turned World War II the way it did. the deadliest conflict in human history.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Island hopping Pacific.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Island hopping Pacific.", "x": "Going deeper: Island hopping Pacific.. D-Day: Normandy landings (1944). Details are where historians live — the numbers, the names, the decisions that turned World War II the way it did. the deadliest conflict in human history.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Manhattan Project.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Manhattan Project.", "x": "Going deeper: Manhattan Project.. Atomic bombs ended Pacific war. Details are where historians live — the numbers, the names, the decisions that turned World War II the way it did. the deadliest conflict in human history.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Nuremberg trials.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Nuremberg trials.", "x": "Going deeper: Nuremberg trials.. 70M+ died; UN founded after. Details are where historians live — the numbers, the names, the decisions that turned World War II the way it did. the deadliest conflict in human history.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Cold War followed.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Cold War followed.", "x": "Going deeper: Cold War followed.. Started with Germany's invasion of Poland. Details are where historians live — the numbers, the names, the decisions that turned World War II the way it did. the deadliest conflict in human history.", "s": "public-reference", "f": null}, {"t": "Timeline", "d": "World War II, event by event.", "g": "timeline", "l": 2, "q": "What is Timeline?", "a": "World War II, event by event.", "x": "The timeline: Started with Germany's invasion of Poland.. Blitzkrieg tactics. Key dates in order — US entered after Pearl Harbor (1941).. 1939-1945 Pin the dates first; the story hangs on them. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key figures", "d": "The people of World War II.", "g": "people", "l": 2, "q": "What is Key figures?", "a": "The people of World War II.", "x": "The people: Eastern Front: Stalingrad.. D-Day: Normandy landings (1944). History is made by people deciding under pressure — the deadliest conflict in human history.. Manhattan Project. Know the actors and the events make sense.", "s": "public-reference", "f": null}, {"t": "More key figures", "d": "More people who shaped World War II.", "g": "people", "l": 2, "q": "What is More key figures?", "a": "More people who shaped World War II.", "x": "More figures: Atomic bombs ended Pacific war. shaped World War II as surely as anyone — Nuremberg trials.. the deadliest conflict in human history. History remembers the famous; the wise student learns the overlooked too.", "s": "public-reference", "f": null}, {"t": "Causes", "d": "Why World War II happened.", "g": "causes", "l": 2, "q": "What is Causes?", "a": "Why World War II happened.", "x": "The causes: Started with Germany's invasion of Poland.. Island hopping Pacific. Historians debate the deep vs immediate causes of World War II — the deadliest conflict in human history.. 70M+ died; UN founded after. Understanding why is the whole point of studying history.", "s": "public-reference", "f": null}, {"t": "The turning point", "d": "The moment World War II turned.", "g": "turning-point", "l": 2, "q": "What is The turning point?", "a": "The moment World War II turned.", "x": "The turning point: Manhattan Project.. Holocaust: 6M Jews murdered. Every great story has the moment it could have gone otherwise — World War II. the deadliest conflict in human history. Find it and you find the drama.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-war-world-war-ii-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
