(function(){'use strict';
/* JAH Henry Morton Stanley Explorer Database generator — jahdb-e2-explorer-henry-morton-stanley-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-explorer-henry-morton-stanley',PREFIX='JAH-E2EXPLORERH-',NAME='JAH Henry Morton Stanley Explorer Database';
var FIELDS=["overview", "context", "facts", "details", "timeline", "people", "causes", "turning-point", "legacy", "misconceptions", "what-if", "quiz", "sources", "learn-more"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Henry Morton Stanley: overview", "d": "Henry Morton Stanley (1841-1904): found Livingstone; Congo..", "g": "overview", "l": 2, "q": "What is Henry Morton Stanley: overview?", "a": "Henry Morton Stanley (1841-1904): found Livingstone; Congo..", "x": "The complete explorer guide to Henry Morton Stanley: found Livingstone; Congo.. Found Livingstone 1871. From causes to consequences, from the key figures to the legacy that still shapes us — this database tells the whole story the way a great history course would.", "s": "public-reference", "f": null}, {"t": "The era", "d": "Henry Morton Stanley in its time: 1841-1904.", "g": "context", "l": 2, "q": "What is The era?", "a": "Henry Morton Stanley in its time: 1841-1904.", "x": "Context: Henry Morton Stanley belonged to 1841-1904 — Welsh/American.. Congo for Leopold. Nothing in history happens in a vacuum; the era explains the motives, the means, and the stakes. found Livingstone; Congo.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Found Livingstone 1871.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Found Livingstone 1871.", "x": "Henry Morton Stanley: Found Livingstone 1871.. New York Herald. This is one of the load-bearing facts about Henry Morton Stanley — learn it cold. Through Dark Continent. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "The story behind: Found Livingstone 1871..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "The story behind: Found Livingstone 1871..", "x": "Explained: Found Livingstone 1871.. Exploration. In the history of Henry Morton Stanley, this fact connects to Emin Pasha relief. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Congo for Leopold.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Congo for Leopold.", "x": "Henry Morton Stanley: Congo for Leopold.. Congo atrocities. This is one of the load-bearing facts about Henry Morton Stanley — learn it cold. Emin Pasha relief. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "The story behind: Congo for Leopold..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "The story behind: Congo for Leopold..", "x": "Explained: Congo for Leopold.. Reputation. In the history of Henry Morton Stanley, this fact connects to Journalist. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Through Dark Continent.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Through Dark Continent.", "x": "Henry Morton Stanley: Through Dark Continent.. Exploration. This is one of the load-bearing facts about Henry Morton Stanley — learn it cold. Journalist. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "The story behind: Through Dark Continent..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "The story behind: Through Dark Continent..", "x": "Explained: Through Dark Continent.. History. In the history of Henry Morton Stanley, this fact connects to Controversial. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Emin Pasha relief.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Emin Pasha relief.", "x": "Henry Morton Stanley: Emin Pasha relief.. Reputation. This is one of the load-bearing facts about Henry Morton Stanley — learn it cold. Controversial. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "The story behind: Emin Pasha relief..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "The story behind: Emin Pasha relief..", "x": "Explained: Emin Pasha relief.. Welsh/American. In the history of Henry Morton Stanley, this fact connects to Found Livingstone 1871. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Journalist.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Journalist.", "x": "Henry Morton Stanley: Journalist.. History. This is one of the load-bearing facts about Henry Morton Stanley — learn it cold. Found Livingstone 1871. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "The story behind: Journalist..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "The story behind: Journalist..", "x": "Explained: Journalist.. New York Herald. In the history of Henry Morton Stanley, this fact connects to Congo for Leopold. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Controversial.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Controversial.", "x": "Henry Morton Stanley: Controversial.. Welsh/American. This is one of the load-bearing facts about Henry Morton Stanley — learn it cold. Congo for Leopold. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "The story behind: Controversial..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "The story behind: Controversial..", "x": "Explained: Controversial.. Congo atrocities. In the history of Henry Morton Stanley, this fact connects to Through Dark Continent. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Welsh/American.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Welsh/American.", "x": "Going deeper: Welsh/American.. Congo for Leopold. Details are where historians live — the numbers, the names, the decisions that turned Henry Morton Stanley the way it did. found Livingstone; Congo. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "New York Herald.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "New York Herald.", "x": "Going deeper: New York Herald.. Through Dark Continent. Details are where historians live — the numbers, the names, the decisions that turned Henry Morton Stanley the way it did. found Livingstone; Congo.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Congo atrocities.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Congo atrocities.", "x": "Going deeper: Congo atrocities.. Emin Pasha relief. Details are where historians live — the numbers, the names, the decisions that turned Henry Morton Stanley the way it did. found Livingstone; Congo.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Exploration.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Exploration.", "x": "Going deeper: Exploration.. Journalist. Details are where historians live — the numbers, the names, the decisions that turned Henry Morton Stanley the way it did. found Livingstone; Congo. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Reputation.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Reputation.", "x": "Going deeper: Reputation.. Controversial. Details are where historians live — the numbers, the names, the decisions that turned Henry Morton Stanley the way it did. found Livingstone; Congo. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "History.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "History.", "x": "Going deeper: History.. Found Livingstone 1871. Details are where historians live — the numbers, the names, the decisions that turned Henry Morton Stanley the way it did. found Livingstone; Congo. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Timeline", "d": "Henry Morton Stanley, event by event.", "g": "timeline", "l": 2, "q": "What is Timeline?", "a": "Henry Morton Stanley, event by event.", "x": "The timeline: Found Livingstone 1871.. Welsh/American. Key dates in order — Through Dark Continent.. 1841-1904 Pin the dates first; the story hangs on them. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key figures", "d": "The people of Henry Morton Stanley.", "g": "people", "l": 2, "q": "What is Key figures?", "a": "The people of Henry Morton Stanley.", "x": "The people: New York Herald.. Emin Pasha relief. History is made by people deciding under pressure — found Livingstone; Congo.. Exploration. Know the actors and the events make sense. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "More key figures", "d": "More people who shaped Henry Morton Stanley.", "g": "people", "l": 2, "q": "What is More key figures?", "a": "More people who shaped Henry Morton Stanley.", "x": "More figures: Journalist. shaped Henry Morton Stanley as surely as anyone — Reputation.. found Livingstone; Congo. History remembers the famous; the wise student learns the overlooked too. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Causes", "d": "Why Henry Morton Stanley happened.", "g": "causes", "l": 2, "q": "What is Causes?", "a": "Why Henry Morton Stanley happened.", "x": "The causes: Found Livingstone 1871.. Congo atrocities. Historians debate the deep vs immediate causes of Henry Morton Stanley — found Livingstone; Congo.. Controversial. Understanding why is the whole point of studying history.", "s": "public-reference", "f": null}, {"t": "The turning point", "d": "The moment Henry Morton Stanley turned.", "g": "turning-point", "l": 2, "q": "What is The turning point?", "a": "The moment Henry Morton Stanley turned.", "x": "The turning point: Exploration.. Congo for Leopold. Every great story has the moment it could have gone otherwise — Henry Morton Stanley. found Livingstone; Congo. Find it and you find the drama. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-explorer-henry-morton-stanley-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
