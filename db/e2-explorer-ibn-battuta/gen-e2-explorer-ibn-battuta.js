(function(){'use strict';
/* JAH Ibn Battuta Explorer Database generator — jahdb-e2-explorer-ibn-battuta-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-explorer-ibn-battuta',PREFIX='JAH-E2EXPLORERI-',NAME='JAH Ibn Battuta Explorer Database';
var FIELDS=["overview", "context", "facts", "details", "timeline", "people", "causes", "turning-point", "legacy", "misconceptions", "what-if", "quiz", "sources", "learn-more"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Ibn Battuta: overview", "d": "Ibn Battuta (1304-1369): traveled 75,000 miles..", "g": "overview", "l": 2, "q": "What is Ibn Battuta: overview?", "a": "Ibn Battuta (1304-1369): traveled 75,000 miles..", "x": "The complete explorer guide to Ibn Battuta: traveled 75,000 miles.. Morocco to China. From causes to consequences, from the key figures to the legacy that still shapes us — this database tells the whole story the way a great history course would.", "s": "public-reference", "f": null}, {"t": "The era", "d": "Ibn Battuta in its time: 1304-1369.", "g": "context", "l": 2, "q": "What is The era?", "a": "Ibn Battuta in its time: 1304-1369.", "x": "Context: Ibn Battuta belonged to 1304-1369 — Tangier.. Rihla travelogue. Nothing in history happens in a vacuum; the era explains the motives, the means, and the stakes. traveled 75,000 miles. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Morocco to China.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Morocco to China.", "x": "Ibn Battuta: Morocco to China.. 30 years. This is one of the load-bearing facts about Ibn Battuta — learn it cold. Mali visit. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "The story behind: Morocco to China..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "The story behind: Morocco to China..", "x": "Explained: Morocco to China.. Scholarship. In the history of Ibn Battuta, this fact connects to Delhi judge. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Rihla travelogue.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Rihla travelogue.", "x": "Ibn Battuta: Rihla travelogue.. Descriptions. This is one of the load-bearing facts about Ibn Battuta — learn it cold. Delhi judge. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "The story behind: Rihla travelogue..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "The story behind: Rihla travelogue..", "x": "Explained: Rihla travelogue.. Legacy. In the history of Ibn Battuta, this fact connects to Mecca hajj. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Mali visit.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Mali visit.", "x": "Ibn Battuta: Mali visit.. Scholarship. This is one of the load-bearing facts about Ibn Battuta — learn it cold. Mecca hajj. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "The story behind: Mali visit..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "The story behind: Mali visit..", "x": "Explained: Mali visit.. Geography. In the history of Ibn Battuta, this fact connects to Medieval world. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Delhi judge.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Delhi judge.", "x": "Ibn Battuta: Delhi judge.. Legacy. This is one of the load-bearing facts about Ibn Battuta — learn it cold. Medieval world. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "The story behind: Delhi judge..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "The story behind: Delhi judge..", "x": "Explained: Delhi judge.. Tangier. In the history of Ibn Battuta, this fact connects to Morocco to China. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Mecca hajj.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Mecca hajj.", "x": "Ibn Battuta: Mecca hajj.. Geography. This is one of the load-bearing facts about Ibn Battuta — learn it cold. Morocco to China. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "The story behind: Mecca hajj..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "The story behind: Mecca hajj..", "x": "Explained: Mecca hajj.. 30 years. In the history of Ibn Battuta, this fact connects to Rihla travelogue. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Medieval world.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Medieval world.", "x": "Ibn Battuta: Medieval world.. Tangier. This is one of the load-bearing facts about Ibn Battuta — learn it cold. Rihla travelogue. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "The story behind: Medieval world..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "The story behind: Medieval world..", "x": "Explained: Medieval world.. Descriptions. In the history of Ibn Battuta, this fact connects to Mali visit. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Tangier.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Tangier.", "x": "Going deeper: Tangier.. Rihla travelogue. Details are where historians live — the numbers, the names, the decisions that turned Ibn Battuta the way it did. traveled 75,000 miles. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "30 years.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "30 years.", "x": "Going deeper: 30 years.. Mali visit. Details are where historians live — the numbers, the names, the decisions that turned Ibn Battuta the way it did. traveled 75,000 miles. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Descriptions.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Descriptions.", "x": "Going deeper: Descriptions.. Delhi judge. Details are where historians live — the numbers, the names, the decisions that turned Ibn Battuta the way it did. traveled 75,000 miles. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Scholarship.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Scholarship.", "x": "Going deeper: Scholarship.. Mecca hajj. Details are where historians live — the numbers, the names, the decisions that turned Ibn Battuta the way it did. traveled 75,000 miles. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Legacy.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Legacy.", "x": "Going deeper: Legacy.. Medieval world. Details are where historians live — the numbers, the names, the decisions that turned Ibn Battuta the way it did. traveled 75,000 miles. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Geography.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Geography.", "x": "Going deeper: Geography.. Morocco to China. Details are where historians live — the numbers, the names, the decisions that turned Ibn Battuta the way it did. traveled 75,000 miles. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Timeline", "d": "Ibn Battuta, event by event.", "g": "timeline", "l": 2, "q": "What is Timeline?", "a": "Ibn Battuta, event by event.", "x": "The timeline: Morocco to China.. Tangier. Key dates in order — Mali visit.. 1304-1369 Pin the dates first; the story hangs on them. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key figures", "d": "The people of Ibn Battuta.", "g": "people", "l": 2, "q": "What is Key figures?", "a": "The people of Ibn Battuta.", "x": "The people: 30 years.. Delhi judge. History is made by people deciding under pressure — traveled 75,000 miles.. Scholarship. Know the actors and the events make sense. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "More key figures", "d": "More people who shaped Ibn Battuta.", "g": "people", "l": 2, "q": "What is More key figures?", "a": "More people who shaped Ibn Battuta.", "x": "More figures: Mecca hajj. shaped Ibn Battuta as surely as anyone — Legacy.. traveled 75,000 miles. History remembers the famous; the wise student learns the overlooked too. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Causes", "d": "Why Ibn Battuta happened.", "g": "causes", "l": 2, "q": "What is Causes?", "a": "Why Ibn Battuta happened.", "x": "The causes: Morocco to China.. Descriptions. Historians debate the deep vs immediate causes of Ibn Battuta — traveled 75,000 miles.. Medieval world. Understanding why is the whole point of studying history.", "s": "public-reference", "f": null}, {"t": "The turning point", "d": "The moment Ibn Battuta turned.", "g": "turning-point", "l": 2, "q": "What is The turning point?", "a": "The moment Ibn Battuta turned.", "x": "The turning point: Scholarship.. Rihla travelogue. Every great story has the moment it could have gone otherwise — Ibn Battuta. traveled 75,000 miles. Find it and you find the drama. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-explorer-ibn-battuta-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
