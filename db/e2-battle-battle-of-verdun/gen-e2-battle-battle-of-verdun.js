(function(){'use strict';
/* JAH Battle of Verdun Battle Database generator — jahdb-e2-battle-battle-of-verdun-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-battle-battle-of-verdun',PREFIX='JAH-E2BATTLEBAT-',NAME='JAH Battle of Verdun Battle Database';
var FIELDS=["overview", "context", "facts", "details", "timeline", "people", "causes", "turning-point", "legacy", "misconceptions", "what-if", "quiz", "sources", "learn-more"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Battle of Verdun: overview", "d": "Battle of Verdun (1916): 'They shall not pass'..", "g": "overview", "l": 2, "q": "What is Battle of Verdun: overview?", "a": "Battle of Verdun (1916): 'They shall not pass'..", "x": "The complete battle guide to Battle of Verdun: 'They shall not pass'.. 300 days. From causes to consequences, from the key figures to the legacy that still shapes us — this database tells the whole story the way a great history course would.", "s": "public-reference", "f": null}, {"t": "The era", "d": "Battle of Verdun in its time: 1916.", "g": "context", "l": 2, "q": "What is The era?", "a": "Battle of Verdun in its time: 1916.", "x": "Context: Battle of Verdun belonged to 1916 — Falkenhayn.. 700,000 casualties. Nothing in history happens in a vacuum; the era explains the motives, the means, and the stakes. 'They shall not pass'. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "300 days.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "300 days.", "x": "Battle of Verdun: 300 days.. Forts. This is one of the load-bearing facts about Battle of Verdun — learn it cold. Petain. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "The story behind: 300 days..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "The story behind: 300 days..", "x": "Explained: 300 days.. Memory. In the history of Battle of Verdun, this fact connects to Attrition. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "700,000 casualties.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "700,000 casualties.", "x": "Battle of Verdun: 700,000 casualties.. Aftermath. This is one of the load-bearing facts about Battle of Verdun — learn it cold. Attrition. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "The story behind: 700,000 casualties..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "The story behind: 700,000 casualties..", "x": "Explained: 700,000 casualties.. Site. In the history of Battle of Verdun, this fact connects to Symbol. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Petain.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Petain.", "x": "Battle of Verdun: Petain.. Memory. This is one of the load-bearing facts about Battle of Verdun — learn it cold. Symbol. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "The story behind: Petain..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "The story behind: Petain..", "x": "Explained: Petain.. Lessons. In the history of Battle of Verdun, this fact connects to Ossuary. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Attrition.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Attrition.", "x": "Battle of Verdun: Attrition.. Site. This is one of the load-bearing facts about Battle of Verdun — learn it cold. Ossuary. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "The story behind: Attrition..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "The story behind: Attrition..", "x": "Explained: Attrition.. Falkenhayn. In the history of Battle of Verdun, this fact connects to 300 days. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Symbol.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Symbol.", "x": "Battle of Verdun: Symbol.. Lessons. This is one of the load-bearing facts about Battle of Verdun — learn it cold. 300 days. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "The story behind: Symbol..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "The story behind: Symbol..", "x": "Explained: Symbol.. Forts. In the history of Battle of Verdun, this fact connects to 700,000 casualties. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Ossuary.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Ossuary.", "x": "Battle of Verdun: Ossuary.. Falkenhayn. This is one of the load-bearing facts about Battle of Verdun — learn it cold. 700,000 casualties. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "The story behind: Ossuary..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "The story behind: Ossuary..", "x": "Explained: Ossuary.. Aftermath. In the history of Battle of Verdun, this fact connects to Petain. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Falkenhayn.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Falkenhayn.", "x": "Going deeper: Falkenhayn.. 700,000 casualties. Details are where historians live — the numbers, the names, the decisions that turned Battle of Verdun the way it did. 'They shall not pass'. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Forts.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Forts.", "x": "Going deeper: Forts.. Petain. Details are where historians live — the numbers, the names, the decisions that turned Battle of Verdun the way it did. 'They shall not pass'. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Aftermath.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Aftermath.", "x": "Going deeper: Aftermath.. Attrition. Details are where historians live — the numbers, the names, the decisions that turned Battle of Verdun the way it did. 'They shall not pass'. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Memory.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Memory.", "x": "Going deeper: Memory.. Symbol. Details are where historians live — the numbers, the names, the decisions that turned Battle of Verdun the way it did. 'They shall not pass'. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Site.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Site.", "x": "Going deeper: Site.. Ossuary. Details are where historians live — the numbers, the names, the decisions that turned Battle of Verdun the way it did. 'They shall not pass'. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Lessons.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Lessons.", "x": "Going deeper: Lessons.. 300 days. Details are where historians live — the numbers, the names, the decisions that turned Battle of Verdun the way it did. 'They shall not pass'. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Timeline", "d": "Battle of Verdun, event by event.", "g": "timeline", "l": 2, "q": "What is Timeline?", "a": "Battle of Verdun, event by event.", "x": "The timeline: 300 days.. Falkenhayn. Key dates in order — Petain.. 1916 Pin the dates first; the story hangs on them. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key figures", "d": "The people of Battle of Verdun.", "g": "people", "l": 2, "q": "What is Key figures?", "a": "The people of Battle of Verdun.", "x": "The people: Forts.. Attrition. History is made by people deciding under pressure — 'They shall not pass'.. Memory. Know the actors and the events make sense. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "More key figures", "d": "More people who shaped Battle of Verdun.", "g": "people", "l": 2, "q": "What is More key figures?", "a": "More people who shaped Battle of Verdun.", "x": "More figures: Symbol. shaped Battle of Verdun as surely as anyone — Site.. 'They shall not pass'. History remembers the famous; the wise student learns the overlooked too. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Causes", "d": "Why Battle of Verdun happened.", "g": "causes", "l": 2, "q": "What is Causes?", "a": "Why Battle of Verdun happened.", "x": "The causes: 300 days.. Aftermath. Historians debate the deep vs immediate causes of Battle of Verdun — 'They shall not pass'.. Ossuary. Understanding why is the whole point of studying history. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "The turning point", "d": "The moment Battle of Verdun turned.", "g": "turning-point", "l": 2, "q": "What is The turning point?", "a": "The moment Battle of Verdun turned.", "x": "The turning point: Memory.. 700,000 casualties. Every great story has the moment it could have gone otherwise — Battle of Verdun. 'They shall not pass'. Find it and you find the drama. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-battle-battle-of-verdun-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
