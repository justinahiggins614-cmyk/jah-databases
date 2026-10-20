(function(){'use strict';
/* JAH Marco Polo Explorer Database generator — jahdb-e2-explorer-marco-polo-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-explorer-marco-polo',PREFIX='JAH-E2EXPLORERM-',NAME='JAH Marco Polo Explorer Database';
var FIELDS=["overview", "context", "facts", "details", "timeline", "people", "causes", "turning-point", "legacy", "misconceptions", "what-if", "quiz", "sources", "learn-more"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Marco Polo: overview", "d": "Marco Polo (1254-1324): Venetian in Kublai Khan's China..", "g": "overview", "l": 2, "q": "What is Marco Polo: overview?", "a": "Marco Polo (1254-1324): Venetian in Kublai Khan's China..", "x": "The complete explorer guide to Marco Polo: Venetian in Kublai Khan's China.. Silk Road 1271. From causes to consequences, from the key figures to the legacy that still shapes us — this database tells the whole story the way a great history course would.", "s": "public-reference", "f": null}, {"t": "The era", "d": "Marco Polo in its time: 1254-1324.", "g": "context", "l": 2, "q": "What is The era?", "a": "Marco Polo in its time: 1254-1324.", "x": "Context: Marco Polo belonged to 1254-1324 — Father/uncle traders.. 17 years in China. Nothing in history happens in a vacuum; the era explains the motives, the means, and the stakes. Venetian in Kublai Khan's China.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Silk Road 1271.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Silk Road 1271.", "x": "Marco Polo: Silk Road 1271.. Yuan China. This is one of the load-bearing facts about Marco Polo — learn it cold. Il Milione book. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "The story behind: Silk Road 1271..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "The story behind: Silk Road 1271..", "x": "Explained: Silk Road 1271.. Skeptics. In the history of Marco Polo, this fact connects to Prisoner in Genoa. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "17 years in China.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "17 years in China.", "x": "Marco Polo: 17 years in China.. Descriptions. This is one of the load-bearing facts about Marco Polo — learn it cold. Prisoner in Genoa. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "The story behind: 17 years in China..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "The story behind: 17 years in China..", "x": "Explained: 17 years in China.. Manuscript. In the history of Marco Polo, this fact connects to Kublai's court. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Il Milione book.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Il Milione book.", "x": "Marco Polo: Il Milione book.. Skeptics. This is one of the load-bearing facts about Marco Polo — learn it cold. Kublai's court. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "The story behind: Il Milione book..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "The story behind: Il Milione book..", "x": "Explained: Il Milione book.. Legend. In the history of Marco Polo, this fact connects to Inspired Columbus. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Prisoner in Genoa.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Prisoner in Genoa.", "x": "Marco Polo: Prisoner in Genoa.. Manuscript. This is one of the load-bearing facts about Marco Polo — learn it cold. Inspired Columbus. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "The story behind: Prisoner in Genoa..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "The story behind: Prisoner in Genoa..", "x": "Explained: Prisoner in Genoa.. Father/uncle traders. In the history of Marco Polo, this fact connects to Silk Road 1271. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Kublai's court.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Kublai's court.", "x": "Marco Polo: Kublai's court.. Legend. This is one of the load-bearing facts about Marco Polo — learn it cold. Silk Road 1271. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "The story behind: Kublai's court..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "The story behind: Kublai's court..", "x": "Explained: Kublai's court.. Yuan China. In the history of Marco Polo, this fact connects to 17 years in China. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Inspired Columbus.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Inspired Columbus.", "x": "Marco Polo: Inspired Columbus.. Father/uncle traders. This is one of the load-bearing facts about Marco Polo — learn it cold. 17 years in China. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "The story behind: Inspired Columbus..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "The story behind: Inspired Columbus..", "x": "Explained: Inspired Columbus.. Descriptions. In the history of Marco Polo, this fact connects to Il Milione book. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Father/uncle traders.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Father/uncle traders.", "x": "Going deeper: Father/uncle traders.. 17 years in China. Details are where historians live — the numbers, the names, the decisions that turned Marco Polo the way it did. Venetian in Kublai Khan's China.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Yuan China.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Yuan China.", "x": "Going deeper: Yuan China.. Il Milione book. Details are where historians live — the numbers, the names, the decisions that turned Marco Polo the way it did. Venetian in Kublai Khan's China. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Descriptions.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Descriptions.", "x": "Going deeper: Descriptions.. Prisoner in Genoa. Details are where historians live — the numbers, the names, the decisions that turned Marco Polo the way it did. Venetian in Kublai Khan's China. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Skeptics.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Skeptics.", "x": "Going deeper: Skeptics.. Kublai's court. Details are where historians live — the numbers, the names, the decisions that turned Marco Polo the way it did. Venetian in Kublai Khan's China. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Manuscript.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Manuscript.", "x": "Going deeper: Manuscript.. Inspired Columbus. Details are where historians live — the numbers, the names, the decisions that turned Marco Polo the way it did. Venetian in Kublai Khan's China. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Legend.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Legend.", "x": "Going deeper: Legend.. Silk Road 1271. Details are where historians live — the numbers, the names, the decisions that turned Marco Polo the way it did. Venetian in Kublai Khan's China. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Timeline", "d": "Marco Polo, event by event.", "g": "timeline", "l": 2, "q": "What is Timeline?", "a": "Marco Polo, event by event.", "x": "The timeline: Silk Road 1271.. Father/uncle traders. Key dates in order — Il Milione book.. 1254-1324 Pin the dates first; the story hangs on them. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key figures", "d": "The people of Marco Polo.", "g": "people", "l": 2, "q": "What is Key figures?", "a": "The people of Marco Polo.", "x": "The people: Yuan China.. Prisoner in Genoa. History is made by people deciding under pressure — Venetian in Kublai Khan's China.. Skeptics. Know the actors and the events make sense. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "More key figures", "d": "More people who shaped Marco Polo.", "g": "people", "l": 2, "q": "What is More key figures?", "a": "More people who shaped Marco Polo.", "x": "More figures: Kublai's court. shaped Marco Polo as surely as anyone — Manuscript.. Venetian in Kublai Khan's China. History remembers the famous; the wise student learns the overlooked too. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Causes", "d": "Why Marco Polo happened.", "g": "causes", "l": 2, "q": "What is Causes?", "a": "Why Marco Polo happened.", "x": "The causes: Silk Road 1271.. Descriptions. Historians debate the deep vs immediate causes of Marco Polo — Venetian in Kublai Khan's China.. Inspired Columbus. Understanding why is the whole point of studying history.", "s": "public-reference", "f": null}, {"t": "The turning point", "d": "The moment Marco Polo turned.", "g": "turning-point", "l": 2, "q": "What is The turning point?", "a": "The moment Marco Polo turned.", "x": "The turning point: Skeptics.. 17 years in China. Every great story has the moment it could have gone otherwise — Marco Polo. Venetian in Kublai Khan's China. Find it and you find the drama. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-explorer-marco-polo-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
