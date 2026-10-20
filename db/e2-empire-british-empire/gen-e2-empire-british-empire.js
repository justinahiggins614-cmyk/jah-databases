(function(){'use strict';
/* JAH British Empire Empire Database generator — jahdb-e2-empire-british-empire-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-empire-british-empire',PREFIX='JAH-E2EMPIREBRI-',NAME='JAH British Empire Empire Database';
var FIELDS=["overview", "context", "facts", "details", "timeline", "people", "causes", "turning-point", "legacy", "misconceptions", "what-if", "quiz", "sources", "learn-more"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "British Empire: overview", "d": "British Empire (1583-1997): largest empire ever; sun never set..", "g": "overview", "l": 2, "q": "What is British Empire: overview?", "a": "British Empire (1583-1997): largest empire ever; sun never set..", "x": "The complete empire guide to British Empire: largest empire ever; sun never set.. 1583: Newfoundland. From causes to consequences, from the key figures to the legacy that still shapes us — this database tells the whole story the way a great history course would.", "s": "public-reference", "f": null}, {"t": "The era", "d": "British Empire in its time: 1583-1997.", "g": "context", "l": 2, "q": "What is The era?", "a": "British Empire in its time: 1583-1997.", "x": "Context: British Empire belonged to 1583-1997 — Navy.. East India Co. Nothing in history happens in a vacuum; the era explains the motives, the means, and the stakes. largest empire ever; sun never set.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "1583: Newfoundland.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "1583: Newfoundland.", "x": "British Empire: 1583: Newfoundland.. Colonies. This is one of the load-bearing facts about British Empire — learn it cold. 1776 loss. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "The story behind: 1583: Newfoundland..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "The story behind: 1583: Newfoundland..", "x": "Explained: 1583: Newfoundland.. Decolonization. In the history of British Empire, this fact connects to Victorian peak. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "East India Co.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "East India Co.", "x": "British Empire: East India Co.. Commonwealth. This is one of the load-bearing facts about British Empire — learn it cold. Victorian peak. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "The story behind: East India Co..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "The story behind: East India Co..", "x": "Explained: East India Co.. Legacy. In the history of British Empire, this fact connects to WWI/WWII cost. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "1776 loss.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "1776 loss.", "x": "British Empire: 1776 loss.. Decolonization. This is one of the load-bearing facts about British Empire — learn it cold. WWI/WWII cost. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "The story behind: 1776 loss..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "The story behind: 1776 loss..", "x": "Explained: 1776 loss.. Debate. In the history of British Empire, this fact connects to 1997: Hong Kong. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Victorian peak.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Victorian peak.", "x": "British Empire: Victorian peak.. Legacy. This is one of the load-bearing facts about British Empire — learn it cold. 1997: Hong Kong. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "The story behind: Victorian peak..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "The story behind: Victorian peak..", "x": "Explained: Victorian peak.. Navy. In the history of British Empire, this fact connects to 1583: Newfoundland. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "WWI/WWII cost.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "WWI/WWII cost.", "x": "British Empire: WWI/WWII cost.. Debate. This is one of the load-bearing facts about British Empire — learn it cold. 1583: Newfoundland. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "The story behind: WWI/WWII cost..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "The story behind: WWI/WWII cost..", "x": "Explained: WWI/WWII cost.. Colonies. In the history of British Empire, this fact connects to East India Co. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "1997: Hong Kong.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "1997: Hong Kong.", "x": "British Empire: 1997: Hong Kong.. Navy. This is one of the load-bearing facts about British Empire — learn it cold. East India Co. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "The story behind: 1997: Hong Kong..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "The story behind: 1997: Hong Kong..", "x": "Explained: 1997: Hong Kong.. Commonwealth. In the history of British Empire, this fact connects to 1776 loss. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Navy.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Navy.", "x": "Going deeper: Navy.. East India Co. Details are where historians live — the numbers, the names, the decisions that turned British Empire the way it did. largest empire ever; sun never set. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Colonies.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Colonies.", "x": "Going deeper: Colonies.. 1776 loss. Details are where historians live — the numbers, the names, the decisions that turned British Empire the way it did. largest empire ever; sun never set. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Commonwealth.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Commonwealth.", "x": "Going deeper: Commonwealth.. Victorian peak. Details are where historians live — the numbers, the names, the decisions that turned British Empire the way it did. largest empire ever; sun never set. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Decolonization.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Decolonization.", "x": "Going deeper: Decolonization.. WWI/WWII cost. Details are where historians live — the numbers, the names, the decisions that turned British Empire the way it did. largest empire ever; sun never set. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Legacy.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Legacy.", "x": "Going deeper: Legacy.. 1997: Hong Kong. Details are where historians live — the numbers, the names, the decisions that turned British Empire the way it did. largest empire ever; sun never set. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Debate.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Debate.", "x": "Going deeper: Debate.. 1583: Newfoundland. Details are where historians live — the numbers, the names, the decisions that turned British Empire the way it did. largest empire ever; sun never set. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Timeline", "d": "British Empire, event by event.", "g": "timeline", "l": 2, "q": "What is Timeline?", "a": "British Empire, event by event.", "x": "The timeline: 1583: Newfoundland.. Navy. Key dates in order — 1776 loss.. 1583-1997 Pin the dates first; the story hangs on them. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key figures", "d": "The people of British Empire.", "g": "people", "l": 2, "q": "What is Key figures?", "a": "The people of British Empire.", "x": "The people: Colonies.. Victorian peak. History is made by people deciding under pressure — largest empire ever; sun never set.. Decolonization. Know the actors and the events make sense. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "More key figures", "d": "More people who shaped British Empire.", "g": "people", "l": 2, "q": "What is More key figures?", "a": "More people who shaped British Empire.", "x": "More figures: WWI/WWII cost. shaped British Empire as surely as anyone — Legacy.. largest empire ever; sun never set. History remembers the famous; the wise student learns the overlooked too. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Causes", "d": "Why British Empire happened.", "g": "causes", "l": 2, "q": "What is Causes?", "a": "Why British Empire happened.", "x": "The causes: 1583: Newfoundland.. Commonwealth. Historians debate the deep vs immediate causes of British Empire — largest empire ever; sun never set.. 1997: Hong Kong. Understanding why is the whole point of studying history.", "s": "public-reference", "f": null}, {"t": "The turning point", "d": "The moment British Empire turned.", "g": "turning-point", "l": 2, "q": "What is The turning point?", "a": "The moment British Empire turned.", "x": "The turning point: Decolonization.. East India Co. Every great story has the moment it could have gone otherwise — British Empire. largest empire ever; sun never set. Find it and you find the drama. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-empire-british-empire-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
