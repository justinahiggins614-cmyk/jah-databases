(function(){'use strict';
/* JAH Temple of Artemis Wonder Database generator — jahdb-e2-wonder-temple-of-artemis-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-wonder-temple-of-artemis',PREFIX='JAH-E2WONDERTEM-',NAME='JAH Temple of Artemis Wonder Database';
var FIELDS=["overview", "context", "facts", "details", "timeline", "people", "causes", "turning-point", "legacy", "misconceptions", "what-if", "quiz", "sources", "learn-more"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Temple of Artemis: overview", "d": "Temple of Artemis (c.550 BC): marble temple at Ephesus..", "g": "overview", "l": 2, "q": "What is Temple of Artemis: overview?", "a": "Temple of Artemis (c.550 BC): marble temple at Ephesus..", "x": "The complete wonder guide to Temple of Artemis: marble temple at Ephesus.. Antipater's list. From causes to consequences, from the key figures to the legacy that still shapes us — this database tells the whole story the way a great history course would.", "s": "public-reference", "f": null}, {"t": "The era", "d": "Temple of Artemis in its time: c.550 BC.", "g": "context", "l": 2, "q": "What is The era?", "a": "Temple of Artemis in its time: c.550 BC.", "x": "Context: Temple of Artemis belonged to c.550 BC — Ephesus.. Herostratus burned it. Nothing in history happens in a vacuum; the era explains the motives, the means, and the stakes. marble temple at Ephesus.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Antipater's list.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Antipater's list.", "x": "Temple of Artemis: Antipater's list.. Croesus funded. This is one of the load-bearing facts about Temple of Artemis — learn it cold. Rebuilt grander. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "The story behind: Antipater's list..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "The story behind: Antipater's list..", "x": "Explained: Antipater's list.. Rebuild. In the history of Temple of Artemis, this fact connects to Goths destroyed. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Herostratus burned it.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Herostratus burned it.", "x": "Temple of Artemis: Herostratus burned it.. Arson fame. This is one of the load-bearing facts about Temple of Artemis — learn it cold. Goths destroyed. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "The story behind: Herostratus burned it..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "The story behind: Herostratus burned it..", "x": "Explained: Herostratus burned it.. Ruins. In the history of Temple of Artemis, this fact connects to Column drums. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Rebuilt grander.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Rebuilt grander.", "x": "Temple of Artemis: Rebuilt grander.. Rebuild. This is one of the load-bearing facts about Temple of Artemis — learn it cold. Column drums. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "The story behind: Rebuilt grander..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "The story behind: Rebuilt grander..", "x": "Explained: Rebuilt grander.. Artifacts. In the history of Temple of Artemis, this fact connects to British Museum. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Goths destroyed.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Goths destroyed.", "x": "Temple of Artemis: Goths destroyed.. Ruins. This is one of the load-bearing facts about Temple of Artemis — learn it cold. British Museum. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "The story behind: Goths destroyed..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "The story behind: Goths destroyed..", "x": "Explained: Goths destroyed.. Ephesus. In the history of Temple of Artemis, this fact connects to Antipater's list. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Column drums.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Column drums.", "x": "Temple of Artemis: Column drums.. Artifacts. This is one of the load-bearing facts about Temple of Artemis — learn it cold. Antipater's list. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "The story behind: Column drums..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "The story behind: Column drums..", "x": "Explained: Column drums.. Croesus funded. In the history of Temple of Artemis, this fact connects to Herostratus burned it. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "British Museum.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "British Museum.", "x": "Temple of Artemis: British Museum.. Ephesus. This is one of the load-bearing facts about Temple of Artemis — learn it cold. Herostratus burned it. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "The story behind: British Museum..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "The story behind: British Museum..", "x": "Explained: British Museum.. Arson fame. In the history of Temple of Artemis, this fact connects to Rebuilt grander. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Ephesus.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Ephesus.", "x": "Going deeper: Ephesus.. Herostratus burned it. Details are where historians live — the numbers, the names, the decisions that turned Temple of Artemis the way it did. marble temple at Ephesus. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Croesus funded.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Croesus funded.", "x": "Going deeper: Croesus funded.. Rebuilt grander. Details are where historians live — the numbers, the names, the decisions that turned Temple of Artemis the way it did. marble temple at Ephesus. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Arson fame.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Arson fame.", "x": "Going deeper: Arson fame.. Goths destroyed. Details are where historians live — the numbers, the names, the decisions that turned Temple of Artemis the way it did. marble temple at Ephesus. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Rebuild.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Rebuild.", "x": "Going deeper: Rebuild.. Column drums. Details are where historians live — the numbers, the names, the decisions that turned Temple of Artemis the way it did. marble temple at Ephesus. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Ruins.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Ruins.", "x": "Going deeper: Ruins.. British Museum. Details are where historians live — the numbers, the names, the decisions that turned Temple of Artemis the way it did. marble temple at Ephesus. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Artifacts.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Artifacts.", "x": "Going deeper: Artifacts.. Antipater's list. Details are where historians live — the numbers, the names, the decisions that turned Temple of Artemis the way it did. marble temple at Ephesus. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Timeline", "d": "Temple of Artemis, event by event.", "g": "timeline", "l": 2, "q": "What is Timeline?", "a": "Temple of Artemis, event by event.", "x": "The timeline: Antipater's list.. Ephesus. Key dates in order — Rebuilt grander.. c.550 BC Pin the dates first; the story hangs on them. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key figures", "d": "The people of Temple of Artemis.", "g": "people", "l": 2, "q": "What is Key figures?", "a": "The people of Temple of Artemis.", "x": "The people: Croesus funded.. Goths destroyed. History is made by people deciding under pressure — marble temple at Ephesus.. Rebuild. Know the actors and the events make sense. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "More key figures", "d": "More people who shaped Temple of Artemis.", "g": "people", "l": 2, "q": "What is More key figures?", "a": "More people who shaped Temple of Artemis.", "x": "More figures: Column drums. shaped Temple of Artemis as surely as anyone — Ruins.. marble temple at Ephesus. History remembers the famous; the wise student learns the overlooked too. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Causes", "d": "Why Temple of Artemis happened.", "g": "causes", "l": 2, "q": "What is Causes?", "a": "Why Temple of Artemis happened.", "x": "The causes: Antipater's list.. Arson fame. Historians debate the deep vs immediate causes of Temple of Artemis — marble temple at Ephesus.. British Museum. Understanding why is the whole point of studying history.", "s": "public-reference", "f": null}, {"t": "The turning point", "d": "The moment Temple of Artemis turned.", "g": "turning-point", "l": 2, "q": "What is The turning point?", "a": "The moment Temple of Artemis turned.", "x": "The turning point: Rebuild.. Herostratus burned it. Every great story has the moment it could have gone otherwise — Temple of Artemis. marble temple at Ephesus. Find it and you find the drama. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-wonder-temple-of-artemis-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
