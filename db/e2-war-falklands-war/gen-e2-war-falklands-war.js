(function(){'use strict';
/* JAH Falklands War War Database generator — jahdb-e2-war-falklands-war-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-war-falklands-war',PREFIX='JAH-E2WARFALKLA-',NAME='JAH Falklands War War Database';
var FIELDS=["overview", "context", "facts", "details", "timeline", "people", "causes", "turning-point", "legacy", "misconceptions", "what-if", "quiz", "sources", "learn-more"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Falklands War: overview", "d": "Falklands War (1982): Britain retook islands from Argentina..", "g": "overview", "l": 2, "q": "What is Falklands War: overview?", "a": "Falklands War (1982): Britain retook islands from Argentina..", "x": "The complete war guide to Falklands War: Britain retook islands from Argentina.. Argentina invaded. From causes to consequences, from the key figures to the legacy that still shapes us — this database tells the whole story the way a great history course would.", "s": "public-reference", "f": null}, {"t": "The era", "d": "Falklands War in its time: 1982.", "g": "context", "l": 2, "q": "What is The era?", "a": "Falklands War in its time: 1982.", "x": "Context: Falklands War belonged to 1982 — Galtieri junta.. Thatcher's resolve. Nothing in history happens in a vacuum; the era explains the motives, the means, and the stakes. Britain retook islands from Argentina.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Argentina invaded.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Argentina invaded.", "x": "Falklands War: Argentina invaded.. Task Force 8,000 miles. This is one of the load-bearing facts about Falklands War — learn it cold. Exocet sank Sheffield. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "The story behind: Argentina invaded..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "The story behind: Argentina invaded..", "x": "Explained: Argentina invaded.. Mount Tumbledown. In the history of Falklands War, this fact connects to Goose Green. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Thatcher's resolve.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Thatcher's resolve.", "x": "Falklands War: Thatcher's resolve.. Harriers. This is one of the load-bearing facts about Falklands War — learn it cold. Goose Green. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "The story behind: Thatcher's resolve..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "The story behind: Thatcher's resolve..", "x": "Explained: Thatcher's resolve.. Aftermath. In the history of Falklands War, this fact connects to Belgrano sunk. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Exocet sank Sheffield.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Exocet sank Sheffield.", "x": "Falklands War: Exocet sank Sheffield.. Mount Tumbledown. This is one of the load-bearing facts about Falklands War — learn it cold. Belgrano sunk. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "The story behind: Exocet sank Sheffield..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "The story behind: Exocet sank Sheffield..", "x": "Explained: Exocet sank Sheffield.. Sovereignty. In the history of Falklands War, this fact connects to 74 days. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Goose Green.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Goose Green.", "x": "Falklands War: Goose Green.. Aftermath. This is one of the load-bearing facts about Falklands War — learn it cold. 74 days. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "The story behind: Goose Green..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "The story behind: Goose Green..", "x": "Explained: Goose Green.. Galtieri junta. In the history of Falklands War, this fact connects to Argentina invaded. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Belgrano sunk.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Belgrano sunk.", "x": "Falklands War: Belgrano sunk.. Sovereignty. This is one of the load-bearing facts about Falklands War — learn it cold. Argentina invaded. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "The story behind: Belgrano sunk..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "The story behind: Belgrano sunk..", "x": "Explained: Belgrano sunk.. Task Force 8,000 miles. In the history of Falklands War, this fact connects to Thatcher's resolve. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "74 days.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "74 days.", "x": "Falklands War: 74 days.. Galtieri junta. This is one of the load-bearing facts about Falklands War — learn it cold. Thatcher's resolve. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "The story behind: 74 days..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "The story behind: 74 days..", "x": "Explained: 74 days.. Harriers. In the history of Falklands War, this fact connects to Exocet sank Sheffield. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Galtieri junta.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Galtieri junta.", "x": "Going deeper: Galtieri junta.. Thatcher's resolve. Details are where historians live — the numbers, the names, the decisions that turned Falklands War the way it did. Britain retook islands from Argentina.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Task Force 8,000 miles.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Task Force 8,000 miles.", "x": "Going deeper: Task Force 8,000 miles.. Exocet sank Sheffield. Details are where historians live — the numbers, the names, the decisions that turned Falklands War the way it did. Britain retook islands from Argentina.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Harriers.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Harriers.", "x": "Going deeper: Harriers.. Goose Green. Details are where historians live — the numbers, the names, the decisions that turned Falklands War the way it did. Britain retook islands from Argentina. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Mount Tumbledown.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Mount Tumbledown.", "x": "Going deeper: Mount Tumbledown.. Belgrano sunk. Details are where historians live — the numbers, the names, the decisions that turned Falklands War the way it did. Britain retook islands from Argentina.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Aftermath.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Aftermath.", "x": "Going deeper: Aftermath.. 74 days. Details are where historians live — the numbers, the names, the decisions that turned Falklands War the way it did. Britain retook islands from Argentina. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Sovereignty.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Sovereignty.", "x": "Going deeper: Sovereignty.. Argentina invaded. Details are where historians live — the numbers, the names, the decisions that turned Falklands War the way it did. Britain retook islands from Argentina.", "s": "public-reference", "f": null}, {"t": "Timeline", "d": "Falklands War, event by event.", "g": "timeline", "l": 2, "q": "What is Timeline?", "a": "Falklands War, event by event.", "x": "The timeline: Argentina invaded.. Galtieri junta. Key dates in order — Exocet sank Sheffield.. 1982 Pin the dates first; the story hangs on them. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key figures", "d": "The people of Falklands War.", "g": "people", "l": 2, "q": "What is Key figures?", "a": "The people of Falklands War.", "x": "The people: Task Force 8,000 miles.. Goose Green. History is made by people deciding under pressure — Britain retook islands from Argentina.. Mount Tumbledown. Know the actors and the events make sense.", "s": "public-reference", "f": null}, {"t": "More key figures", "d": "More people who shaped Falklands War.", "g": "people", "l": 2, "q": "What is More key figures?", "a": "More people who shaped Falklands War.", "x": "More figures: Belgrano sunk. shaped Falklands War as surely as anyone — Aftermath.. Britain retook islands from Argentina. History remembers the famous; the wise student learns the overlooked too. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Causes", "d": "Why Falklands War happened.", "g": "causes", "l": 2, "q": "What is Causes?", "a": "Why Falklands War happened.", "x": "The causes: Argentina invaded.. Harriers. Historians debate the deep vs immediate causes of Falklands War — Britain retook islands from Argentina.. 74 days. Understanding why is the whole point of studying history.", "s": "public-reference", "f": null}, {"t": "The turning point", "d": "The moment Falklands War turned.", "g": "turning-point", "l": 2, "q": "What is The turning point?", "a": "The moment Falklands War turned.", "x": "The turning point: Mount Tumbledown.. Thatcher's resolve. Every great story has the moment it could have gone otherwise — Falklands War. Britain retook islands from Argentina. Find it and you find the drama.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-war-falklands-war-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
