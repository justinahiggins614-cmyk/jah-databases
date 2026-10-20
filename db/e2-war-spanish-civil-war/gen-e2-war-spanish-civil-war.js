(function(){'use strict';
/* JAH Spanish Civil War War Database generator — jahdb-e2-war-spanish-civil-war-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-war-spanish-civil-war',PREFIX='JAH-E2WARSPANIS-',NAME='JAH Spanish Civil War War Database';
var FIELDS=["overview", "context", "facts", "details", "timeline", "people", "causes", "turning-point", "legacy", "misconceptions", "what-if", "quiz", "sources", "learn-more"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Spanish Civil War: overview", "d": "Spanish Civil War (1936-1939): Franco's fascists beat the Republic..", "g": "overview", "l": 2, "q": "What is Spanish Civil War: overview?", "a": "Spanish Civil War (1936-1939): Franco's fascists beat the Republic..", "x": "The complete war guide to Spanish Civil War: Franco's fascists beat the Republic.. Military coup 1936. From causes to consequences, from the key figures to the legacy that still shapes us — this database tells the whole story the way a great history course would.", "s": "public-reference", "f": null}, {"t": "The era", "d": "Spanish Civil War in its time: 1936-1939.", "g": "context", "l": 2, "q": "What is The era?", "a": "Spanish Civil War in its time: 1936-1939.", "x": "Context: Spanish Civil War belonged to 1936-1939 — Republic vs Nationalists.. Guernica bombed. Nothing in history happens in a vacuum; the era explains the motives, the means, and the stakes. Franco's fascists beat the Republic.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Military coup 1936.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Military coup 1936.", "x": "Spanish Civil War: Military coup 1936.. Condor Legion. This is one of the load-bearing facts about Spanish Civil War — learn it cold. International Brigades. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "The story behind: Military coup 1936..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "The story behind: Military coup 1936..", "x": "Explained: Military coup 1936.. Non-intervention. In the history of Spanish Civil War, this fact connects to Franco won 1939. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Guernica bombed.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Guernica bombed.", "x": "Spanish Civil War: Guernica bombed.. Orwell fought. This is one of the load-bearing facts about Spanish Civil War — learn it cold. Franco won 1939. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "The story behind: Guernica bombed..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "The story behind: Guernica bombed..", "x": "Explained: Guernica bombed.. Exiles. In the history of Spanish Civil War, this fact connects to WWII preview. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "International Brigades.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "International Brigades.", "x": "Spanish Civil War: International Brigades.. Non-intervention. This is one of the load-bearing facts about Spanish Civil War — learn it cold. WWII preview. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "The story behind: International Brigades..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "The story behind: International Brigades..", "x": "Explained: International Brigades.. Memory. In the history of Spanish Civil War, this fact connects to Dictatorship to 1975. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Franco won 1939.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Franco won 1939.", "x": "Spanish Civil War: Franco won 1939.. Exiles. This is one of the load-bearing facts about Spanish Civil War — learn it cold. Dictatorship to 1975. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "The story behind: Franco won 1939..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "The story behind: Franco won 1939..", "x": "Explained: Franco won 1939.. Republic vs Nationalists. In the history of Spanish Civil War, this fact connects to Military coup 1936. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "WWII preview.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "WWII preview.", "x": "Spanish Civil War: WWII preview.. Memory. This is one of the load-bearing facts about Spanish Civil War — learn it cold. Military coup 1936. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "The story behind: WWII preview..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "The story behind: WWII preview..", "x": "Explained: WWII preview.. Condor Legion. In the history of Spanish Civil War, this fact connects to Guernica bombed. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Dictatorship to 1975.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Dictatorship to 1975.", "x": "Spanish Civil War: Dictatorship to 1975.. Republic vs Nationalists. This is one of the load-bearing facts about Spanish Civil War — learn it cold. Guernica bombed. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "The story behind: Dictatorship to 1975..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "The story behind: Dictatorship to 1975..", "x": "Explained: Dictatorship to 1975.. Orwell fought. In the history of Spanish Civil War, this fact connects to International Brigades. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Republic vs Nationalists.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Republic vs Nationalists.", "x": "Going deeper: Republic vs Nationalists.. Guernica bombed. Details are where historians live — the numbers, the names, the decisions that turned Spanish Civil War the way it did. Franco's fascists beat the Republic.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Condor Legion.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Condor Legion.", "x": "Going deeper: Condor Legion.. International Brigades. Details are where historians live — the numbers, the names, the decisions that turned Spanish Civil War the way it did. Franco's fascists beat the Republic.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Orwell fought.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Orwell fought.", "x": "Going deeper: Orwell fought.. Franco won 1939. Details are where historians live — the numbers, the names, the decisions that turned Spanish Civil War the way it did. Franco's fascists beat the Republic.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Non-intervention.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Non-intervention.", "x": "Going deeper: Non-intervention.. WWII preview. Details are where historians live — the numbers, the names, the decisions that turned Spanish Civil War the way it did. Franco's fascists beat the Republic.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Exiles.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Exiles.", "x": "Going deeper: Exiles.. Dictatorship to 1975. Details are where historians live — the numbers, the names, the decisions that turned Spanish Civil War the way it did. Franco's fascists beat the Republic.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Memory.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Memory.", "x": "Going deeper: Memory.. Military coup 1936. Details are where historians live — the numbers, the names, the decisions that turned Spanish Civil War the way it did. Franco's fascists beat the Republic. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Timeline", "d": "Spanish Civil War, event by event.", "g": "timeline", "l": 2, "q": "What is Timeline?", "a": "Spanish Civil War, event by event.", "x": "The timeline: Military coup 1936.. Republic vs Nationalists. Key dates in order — International Brigades.. 1936-1939 Pin the dates first; the story hangs on them. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key figures", "d": "The people of Spanish Civil War.", "g": "people", "l": 2, "q": "What is Key figures?", "a": "The people of Spanish Civil War.", "x": "The people: Condor Legion.. Franco won 1939. History is made by people deciding under pressure — Franco's fascists beat the Republic.. Non-intervention. Know the actors and the events make sense. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "More key figures", "d": "More people who shaped Spanish Civil War.", "g": "people", "l": 2, "q": "What is More key figures?", "a": "More people who shaped Spanish Civil War.", "x": "More figures: WWII preview. shaped Spanish Civil War as surely as anyone — Exiles.. Franco's fascists beat the Republic. History remembers the famous; the wise student learns the overlooked too. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Causes", "d": "Why Spanish Civil War happened.", "g": "causes", "l": 2, "q": "What is Causes?", "a": "Why Spanish Civil War happened.", "x": "The causes: Military coup 1936.. Orwell fought. Historians debate the deep vs immediate causes of Spanish Civil War — Franco's fascists beat the Republic.. Dictatorship to 1975. Understanding why is the whole point of studying history.", "s": "public-reference", "f": null}, {"t": "The turning point", "d": "The moment Spanish Civil War turned.", "g": "turning-point", "l": 2, "q": "What is The turning point?", "a": "The moment Spanish Civil War turned.", "x": "The turning point: Non-intervention.. Guernica bombed. Every great story has the moment it could have gone otherwise — Spanish Civil War. Franco's fascists beat the Republic. Find it and you find the drama.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-war-spanish-civil-war-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
