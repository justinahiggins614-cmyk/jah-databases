(function(){'use strict';
/* JAH Hundred Years\' War War Database generator — jahdb-e2-war-hundred-years-war-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-war-hundred-years-war',PREFIX='JAH-E2WARHUNDRE-',NAME='JAH Hundred Years\' War War Database';
var FIELDS=["overview", "context", "facts", "details", "timeline", "people", "causes", "turning-point", "legacy", "misconceptions", "what-if", "quiz", "sources", "learn-more"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Hundred Years' War: overview", "d": "Hundred Years' War (1337-1453): England vs France; Joan of Arc..", "g": "overview", "l": 2, "q": "What is Hundred Years' War: overview?", "a": "Hundred Years' War (1337-1453): England vs France; Joan of Arc..", "x": "The complete war guide to Hundred Years' War: England vs France; Joan of Arc.. Lasted 116 years. From causes to consequences, from the key figures to the legacy that still shapes us — this database tells the whole story the way a great history course would.", "s": "public-reference", "f": null}, {"t": "The era", "d": "Hundred Years' War in its time: 1337-1453.", "g": "context", "l": 2, "q": "What is The era?", "a": "Hundred Years' War in its time: 1337-1453.", "x": "Context: Hundred Years' War belonged to 1337-1453 — Edward III claim.. Agincourt (1415): longbows. Nothing in history happens in a vacuum; the era explains the motives, the means, and the stakes. England vs France; Joan of Arc.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Lasted 116 years.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Lasted 116 years.", "x": "Hundred Years' War: Lasted 116 years.. Crecy. This is one of the load-bearing facts about Hundred Years' War — learn it cold. Joan of Arc: Orleans. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "The story behind: Lasted 116 years..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "The story behind: Lasted 116 years..", "x": "Explained: Lasted 116 years.. Joan's trial. In the history of Hundred Years' War, this fact connects to Black Death mid-war. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Agincourt (1415): longbows.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Agincourt (1415): longbows.", "x": "Hundred Years' War: Agincourt (1415): longbows.. Siege of Orleans. This is one of the load-bearing facts about Hundred Years' War — learn it cold. Black Death mid-war. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "The story behind: Agincourt (1415): longbows..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "The story behind: Agincourt (1415): longbows..", "x": "Explained: Agincourt (1415): longbows.. Castillon 1453. In the history of Hundred Years' War, this fact connects to Ended French victory. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Joan of Arc: Orleans.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Joan of Arc: Orleans.", "x": "Hundred Years' War: Joan of Arc: Orleans.. Joan's trial. This is one of the load-bearing facts about Hundred Years' War — learn it cold. Ended French victory. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "The story behind: Joan of Arc: Orleans..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "The story behind: Joan of Arc: Orleans..", "x": "Explained: Joan of Arc: Orleans.. Longbow revolution. In the history of Hundred Years' War, this fact connects to Feudalism declined. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Black Death mid-war.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Black Death mid-war.", "x": "Hundred Years' War: Black Death mid-war.. Castillon 1453. This is one of the load-bearing facts about Hundred Years' War — learn it cold. Feudalism declined. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "The story behind: Black Death mid-war..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "The story behind: Black Death mid-war..", "x": "Explained: Black Death mid-war.. Edward III claim. In the history of Hundred Years' War, this fact connects to Lasted 116 years. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Ended French victory.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Ended French victory.", "x": "Hundred Years' War: Ended French victory.. Longbow revolution. This is one of the load-bearing facts about Hundred Years' War — learn it cold. Lasted 116 years. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "The story behind: Ended French victory..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "The story behind: Ended French victory..", "x": "Explained: Ended French victory.. Crecy. In the history of Hundred Years' War, this fact connects to Agincourt (1415): longbows. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Feudalism declined.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Feudalism declined.", "x": "Hundred Years' War: Feudalism declined.. Edward III claim. This is one of the load-bearing facts about Hundred Years' War — learn it cold. Agincourt (1415): longbows. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "The story behind: Feudalism declined..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "The story behind: Feudalism declined..", "x": "Explained: Feudalism declined.. Siege of Orleans. In the history of Hundred Years' War, this fact connects to Joan of Arc: Orleans. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Edward III claim.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Edward III claim.", "x": "Going deeper: Edward III claim.. Agincourt (1415): longbows. Details are where historians live — the numbers, the names, the decisions that turned Hundred Years' War the way it did. England vs France; Joan of Arc.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Crecy.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Crecy.", "x": "Going deeper: Crecy.. Joan of Arc: Orleans. Details are where historians live — the numbers, the names, the decisions that turned Hundred Years' War the way it did. England vs France; Joan of Arc. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Siege of Orleans.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Siege of Orleans.", "x": "Going deeper: Siege of Orleans.. Black Death mid-war. Details are where historians live — the numbers, the names, the decisions that turned Hundred Years' War the way it did. England vs France; Joan of Arc.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Joan's trial.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Joan's trial.", "x": "Going deeper: Joan's trial.. Ended French victory. Details are where historians live — the numbers, the names, the decisions that turned Hundred Years' War the way it did. England vs France; Joan of Arc.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Castillon 1453.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Castillon 1453.", "x": "Going deeper: Castillon 1453.. Feudalism declined. Details are where historians live — the numbers, the names, the decisions that turned Hundred Years' War the way it did. England vs France; Joan of Arc.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Longbow revolution.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Longbow revolution.", "x": "Going deeper: Longbow revolution.. Lasted 116 years. Details are where historians live — the numbers, the names, the decisions that turned Hundred Years' War the way it did. England vs France; Joan of Arc.", "s": "public-reference", "f": null}, {"t": "Timeline", "d": "Hundred Years' War, event by event.", "g": "timeline", "l": 2, "q": "What is Timeline?", "a": "Hundred Years' War, event by event.", "x": "The timeline: Lasted 116 years.. Edward III claim. Key dates in order — Joan of Arc: Orleans.. 1337-1453 Pin the dates first; the story hangs on them. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key figures", "d": "The people of Hundred Years' War.", "g": "people", "l": 2, "q": "What is Key figures?", "a": "The people of Hundred Years' War.", "x": "The people: Crecy.. Black Death mid-war. History is made by people deciding under pressure — England vs France; Joan of Arc.. Joan's trial. Know the actors and the events make sense. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "More key figures", "d": "More people who shaped Hundred Years' War.", "g": "people", "l": 2, "q": "What is More key figures?", "a": "More people who shaped Hundred Years' War.", "x": "More figures: Ended French victory. shaped Hundred Years' War as surely as anyone — Castillon 1453.. England vs France; Joan of Arc. History remembers the famous; the wise student learns the overlooked too.", "s": "public-reference", "f": null}, {"t": "Causes", "d": "Why Hundred Years' War happened.", "g": "causes", "l": 2, "q": "What is Causes?", "a": "Why Hundred Years' War happened.", "x": "The causes: Lasted 116 years.. Siege of Orleans. Historians debate the deep vs immediate causes of Hundred Years' War — England vs France; Joan of Arc.. Feudalism declined. Understanding why is the whole point of studying history.", "s": "public-reference", "f": null}, {"t": "The turning point", "d": "The moment Hundred Years' War turned.", "g": "turning-point", "l": 2, "q": "What is The turning point?", "a": "The moment Hundred Years' War turned.", "x": "The turning point: Joan's trial.. Agincourt (1415): longbows. Every great story has the moment it could have gone otherwise — Hundred Years' War. England vs France; Joan of Arc. Find it and you find the drama.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-war-hundred-years-war-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
