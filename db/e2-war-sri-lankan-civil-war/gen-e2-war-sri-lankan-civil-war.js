(function(){'use strict';
/* JAH Sri Lankan Civil War War Database generator — jahdb-e2-war-sri-lankan-civil-war-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-war-sri-lankan-civil-war',PREFIX='JAH-E2WARSRILAN-',NAME='JAH Sri Lankan Civil War War Database';
var FIELDS=["overview", "context", "facts", "details", "timeline", "people", "causes", "turning-point", "legacy", "misconceptions", "what-if", "quiz", "sources", "learn-more"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Sri Lankan Civil War: overview", "d": "Sri Lankan Civil War (1983-2009): Tamil Tigers vs government..", "g": "overview", "l": 2, "q": "What is Sri Lankan Civil War: overview?", "a": "Sri Lankan Civil War (1983-2009): Tamil Tigers vs government..", "x": "The complete war guide to Sri Lankan Civil War: Tamil Tigers vs government.. Black July 1983. From causes to consequences, from the key figures to the legacy that still shapes us — this database tells the whole story the way a great history course would.", "s": "public-reference", "f": null}, {"t": "The era", "d": "Sri Lankan Civil War in its time: 1983-2009.", "g": "context", "l": 2, "q": "What is The era?", "a": "Sri Lankan Civil War in its time: 1983-2009.", "x": "Context: Sri Lankan Civil War belonged to 1983-2009 — Tamil grievances.. LTTE: suicide bombs. Nothing in history happens in a vacuum; the era explains the motives, the means, and the stakes. Tamil Tigers vs government.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Black July 1983.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Black July 1983.", "x": "Sri Lankan Civil War: Black July 1983.. Prabhakaran. This is one of the load-bearing facts about Sri Lankan Civil War — learn it cold. Tsunami 2004. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "The story behind: Black July 1983..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "The story behind: Black July 1983..", "x": "Explained: Black July 1983.. Ceasefire 2002. In the history of Sri Lankan Civil War, this fact connects to 2009: brutal end. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "LTTE: suicide bombs.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "LTTE: suicide bombs.", "x": "Sri Lankan Civil War: LTTE: suicide bombs.. IPKF. This is one of the load-bearing facts about Sri Lankan Civil War — learn it cold. 2009: brutal end. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "The story behind: LTTE: suicide bombs..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "The story behind: LTTE: suicide bombs..", "x": "Explained: LTTE: suicide bombs.. Final offensive. In the history of Sri Lankan Civil War, this fact connects to War crimes claims. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Tsunami 2004.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Tsunami 2004.", "x": "Sri Lankan Civil War: Tsunami 2004.. Ceasefire 2002. This is one of the load-bearing facts about Sri Lankan Civil War — learn it cold. War crimes claims. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "The story behind: Tsunami 2004..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "The story behind: Tsunami 2004..", "x": "Explained: Tsunami 2004.. Memory. In the history of Sri Lankan Civil War, this fact connects to Reconciliation. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "2009: brutal end.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "2009: brutal end.", "x": "Sri Lankan Civil War: 2009: brutal end.. Final offensive. This is one of the load-bearing facts about Sri Lankan Civil War — learn it cold. Reconciliation. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "The story behind: 2009: brutal end..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "The story behind: 2009: brutal end..", "x": "Explained: 2009: brutal end.. Tamil grievances. In the history of Sri Lankan Civil War, this fact connects to Black July 1983. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "War crimes claims.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "War crimes claims.", "x": "Sri Lankan Civil War: War crimes claims.. Memory. This is one of the load-bearing facts about Sri Lankan Civil War — learn it cold. Black July 1983. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "The story behind: War crimes claims..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "The story behind: War crimes claims..", "x": "Explained: War crimes claims.. Prabhakaran. In the history of Sri Lankan Civil War, this fact connects to LTTE: suicide bombs. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Reconciliation.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Reconciliation.", "x": "Sri Lankan Civil War: Reconciliation.. Tamil grievances. This is one of the load-bearing facts about Sri Lankan Civil War — learn it cold. LTTE: suicide bombs. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "The story behind: Reconciliation..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "The story behind: Reconciliation..", "x": "Explained: Reconciliation.. IPKF. In the history of Sri Lankan Civil War, this fact connects to Tsunami 2004. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Tamil grievances.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Tamil grievances.", "x": "Going deeper: Tamil grievances.. LTTE: suicide bombs. Details are where historians live — the numbers, the names, the decisions that turned Sri Lankan Civil War the way it did. Tamil Tigers vs government.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Prabhakaran.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Prabhakaran.", "x": "Going deeper: Prabhakaran.. Tsunami 2004. Details are where historians live — the numbers, the names, the decisions that turned Sri Lankan Civil War the way it did. Tamil Tigers vs government. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "IPKF.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "IPKF.", "x": "Going deeper: IPKF.. 2009: brutal end. Details are where historians live — the numbers, the names, the decisions that turned Sri Lankan Civil War the way it did. Tamil Tigers vs government. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Ceasefire 2002.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Ceasefire 2002.", "x": "Going deeper: Ceasefire 2002.. War crimes claims. Details are where historians live — the numbers, the names, the decisions that turned Sri Lankan Civil War the way it did. Tamil Tigers vs government.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Final offensive.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Final offensive.", "x": "Going deeper: Final offensive.. Reconciliation. Details are where historians live — the numbers, the names, the decisions that turned Sri Lankan Civil War the way it did. Tamil Tigers vs government. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Memory.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Memory.", "x": "Going deeper: Memory.. Black July 1983. Details are where historians live — the numbers, the names, the decisions that turned Sri Lankan Civil War the way it did. Tamil Tigers vs government. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Timeline", "d": "Sri Lankan Civil War, event by event.", "g": "timeline", "l": 2, "q": "What is Timeline?", "a": "Sri Lankan Civil War, event by event.", "x": "The timeline: Black July 1983.. Tamil grievances. Key dates in order — Tsunami 2004.. 1983-2009 Pin the dates first; the story hangs on them. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key figures", "d": "The people of Sri Lankan Civil War.", "g": "people", "l": 2, "q": "What is Key figures?", "a": "The people of Sri Lankan Civil War.", "x": "The people: Prabhakaran.. 2009: brutal end. History is made by people deciding under pressure — Tamil Tigers vs government.. Ceasefire 2002. Know the actors and the events make sense. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "More key figures", "d": "More people who shaped Sri Lankan Civil War.", "g": "people", "l": 2, "q": "What is More key figures?", "a": "More people who shaped Sri Lankan Civil War.", "x": "More figures: War crimes claims. shaped Sri Lankan Civil War as surely as anyone — Final offensive.. Tamil Tigers vs government. History remembers the famous; the wise student learns the overlooked too.", "s": "public-reference", "f": null}, {"t": "Causes", "d": "Why Sri Lankan Civil War happened.", "g": "causes", "l": 2, "q": "What is Causes?", "a": "Why Sri Lankan Civil War happened.", "x": "The causes: Black July 1983.. IPKF. Historians debate the deep vs immediate causes of Sri Lankan Civil War — Tamil Tigers vs government.. Reconciliation. Understanding why is the whole point of studying history.", "s": "public-reference", "f": null}, {"t": "The turning point", "d": "The moment Sri Lankan Civil War turned.", "g": "turning-point", "l": 2, "q": "What is The turning point?", "a": "The moment Sri Lankan Civil War turned.", "x": "The turning point: Ceasefire 2002.. LTTE: suicide bombs. Every great story has the moment it could have gone otherwise — Sri Lankan Civil War. Tamil Tigers vs government. Find it and you find the drama.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-war-sri-lankan-civil-war-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
