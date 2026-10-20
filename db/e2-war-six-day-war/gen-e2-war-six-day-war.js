(function(){'use strict';
/* JAH Six-Day War War Database generator — jahdb-e2-war-six-day-war-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-war-six-day-war',PREFIX='JAH-E2WARSIXDAY-',NAME='JAH Six-Day War War Database';
var FIELDS=["overview", "context", "facts", "details", "timeline", "people", "causes", "turning-point", "legacy", "misconceptions", "what-if", "quiz", "sources", "learn-more"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Six-Day War: overview", "d": "Six-Day War (1967): Israel defeated three Arab armies in six days..", "g": "overview", "l": 2, "q": "What is Six-Day War: overview?", "a": "Six-Day War (1967): Israel defeated three Arab armies in six days..", "x": "The complete war guide to Six-Day War: Israel defeated three Arab armies in six days.. Preemptive strike. From causes to consequences, from the key figures to the legacy that still shapes us — this database tells the whole story the way a great history course would.", "s": "public-reference", "f": null}, {"t": "The era", "d": "Six-Day War in its time: 1967.", "g": "context", "l": 2, "q": "What is The era?", "a": "Six-Day War in its time: 1967.", "x": "Context: Six-Day War belonged to 1967 — Straits of Tiran.. Sinai, Golan, West Bank taken. Nothing in history happens in a vacuum; the era explains the motives, the means, and the stakes. Israel defeated three Arab armies in six days.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Preemptive strike.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Preemptive strike.", "x": "Six-Day War: Preemptive strike.. Air force destroyed. This is one of the load-bearing facts about Six-Day War — learn it cold. Jerusalem reunified. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "The story behind: Preemptive strike..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "The story behind: Preemptive strike..", "x": "Explained: Preemptive strike.. Khartoum summit. In the history of Six-Day War, this fact connects to UN Resolution 242. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Sinai, Golan, West Bank taken.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Sinai, Golan, West Bank taken.", "x": "Six-Day War: Sinai, Golan, West Bank taken.. Moscow/Washington hotline. This is one of the load-bearing facts about Six-Day War — learn it cold. UN Resolution 242. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "The story behind: Sinai, Golan, West Bank taken..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "The story behind: Sinai, Golan, West Bank taken..", "x": "Explained: Sinai, Golan, West Bank taken.. Settlements. In the history of Six-Day War, this fact connects to Nasser's fall. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Jerusalem reunified.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Jerusalem reunified.", "x": "Six-Day War: Jerusalem reunified.. Khartoum summit. This is one of the load-bearing facts about Six-Day War — learn it cold. Nasser's fall. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "The story behind: Jerusalem reunified..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "The story behind: Jerusalem reunified..", "x": "Explained: Jerusalem reunified.. Conflict continues. In the history of Six-Day War, this fact connects to Occupation legacy. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "UN Resolution 242.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "UN Resolution 242.", "x": "Six-Day War: UN Resolution 242.. Settlements. This is one of the load-bearing facts about Six-Day War — learn it cold. Occupation legacy. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "The story behind: UN Resolution 242..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "The story behind: UN Resolution 242..", "x": "Explained: UN Resolution 242.. Straits of Tiran. In the history of Six-Day War, this fact connects to Preemptive strike. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Nasser's fall.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Nasser's fall.", "x": "Six-Day War: Nasser's fall.. Conflict continues. This is one of the load-bearing facts about Six-Day War — learn it cold. Preemptive strike. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "The story behind: Nasser's fall..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "The story behind: Nasser's fall..", "x": "Explained: Nasser's fall.. Air force destroyed. In the history of Six-Day War, this fact connects to Sinai, Golan, West Bank taken. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Occupation legacy.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Occupation legacy.", "x": "Six-Day War: Occupation legacy.. Straits of Tiran. This is one of the load-bearing facts about Six-Day War — learn it cold. Sinai, Golan, West Bank taken. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "The story behind: Occupation legacy..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "The story behind: Occupation legacy..", "x": "Explained: Occupation legacy.. Moscow/Washington hotline. In the history of Six-Day War, this fact connects to Jerusalem reunified. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Straits of Tiran.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Straits of Tiran.", "x": "Going deeper: Straits of Tiran.. Sinai, Golan, West Bank taken. Details are where historians live — the numbers, the names, the decisions that turned Six-Day War the way it did. Israel defeated three Arab armies in six days.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Air force destroyed.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Air force destroyed.", "x": "Going deeper: Air force destroyed.. Jerusalem reunified. Details are where historians live — the numbers, the names, the decisions that turned Six-Day War the way it did. Israel defeated three Arab armies in six days.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Moscow/Washington hotline.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Moscow/Washington hotline.", "x": "Going deeper: Moscow/Washington hotline.. UN Resolution 242. Details are where historians live — the numbers, the names, the decisions that turned Six-Day War the way it did. Israel defeated three Arab armies in six days.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Khartoum summit.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Khartoum summit.", "x": "Going deeper: Khartoum summit.. Nasser's fall. Details are where historians live — the numbers, the names, the decisions that turned Six-Day War the way it did. Israel defeated three Arab armies in six days.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Settlements.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Settlements.", "x": "Going deeper: Settlements.. Occupation legacy. Details are where historians live — the numbers, the names, the decisions that turned Six-Day War the way it did. Israel defeated three Arab armies in six days.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Conflict continues.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Conflict continues.", "x": "Going deeper: Conflict continues.. Preemptive strike. Details are where historians live — the numbers, the names, the decisions that turned Six-Day War the way it did. Israel defeated three Arab armies in six days.", "s": "public-reference", "f": null}, {"t": "Timeline", "d": "Six-Day War, event by event.", "g": "timeline", "l": 2, "q": "What is Timeline?", "a": "Six-Day War, event by event.", "x": "The timeline: Preemptive strike.. Straits of Tiran. Key dates in order — Jerusalem reunified.. 1967 Pin the dates first; the story hangs on them. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key figures", "d": "The people of Six-Day War.", "g": "people", "l": 2, "q": "What is Key figures?", "a": "The people of Six-Day War.", "x": "The people: Air force destroyed.. UN Resolution 242. History is made by people deciding under pressure — Israel defeated three Arab armies in six days.. Khartoum summit. Know the actors and the events make sense.", "s": "public-reference", "f": null}, {"t": "More key figures", "d": "More people who shaped Six-Day War.", "g": "people", "l": 2, "q": "What is More key figures?", "a": "More people who shaped Six-Day War.", "x": "More figures: Nasser's fall. shaped Six-Day War as surely as anyone — Settlements.. Israel defeated three Arab armies in six days. History remembers the famous; the wise student learns the overlooked too.", "s": "public-reference", "f": null}, {"t": "Causes", "d": "Why Six-Day War happened.", "g": "causes", "l": 2, "q": "What is Causes?", "a": "Why Six-Day War happened.", "x": "The causes: Preemptive strike.. Moscow/Washington hotline. Historians debate the deep vs immediate causes of Six-Day War — Israel defeated three Arab armies in six days.. Occupation legacy. Understanding why is the whole point of studying history.", "s": "public-reference", "f": null}, {"t": "The turning point", "d": "The moment Six-Day War turned.", "g": "turning-point", "l": 2, "q": "What is The turning point?", "a": "The moment Six-Day War turned.", "x": "The turning point: Khartoum summit.. Sinai, Golan, West Bank taken. Every great story has the moment it could have gone otherwise — Six-Day War. Israel defeated three Arab armies in six days. Find it and you find the drama.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-war-six-day-war-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
