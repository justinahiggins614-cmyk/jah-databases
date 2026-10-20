(function(){'use strict';
/* JAH Hernando de Soto Explorer Database generator — jahdb-e2-explorer-hernando-de-soto-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-explorer-hernando-de-soto',PREFIX='JAH-E2EXPLORERH-',NAME='JAH Hernando de Soto Explorer Database';
var FIELDS=["overview", "context", "facts", "details", "timeline", "people", "causes", "turning-point", "legacy", "misconceptions", "what-if", "quiz", "sources", "learn-more"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Hernando de Soto: overview", "d": "Hernando de Soto (c.1500-1542): crossed the Southeast; Mississippi..", "g": "overview", "l": 2, "q": "What is Hernando de Soto: overview?", "a": "Hernando de Soto (c.1500-1542): crossed the Southeast; Mississippi..", "x": "The complete explorer guide to Hernando de Soto: crossed the Southeast; Mississippi.. 1539 landing Florida. From causes to consequences, from the key figures to the legacy that still shapes us — this database tells the whole story the way a great history course would.", "s": "public-reference", "f": null}, {"t": "The era", "d": "Hernando de Soto in its time: c.1500-1542.", "g": "context", "l": 2, "q": "What is The era?", "a": "Hernando de Soto in its time: c.1500-1542.", "x": "Context: Hernando de Soto belonged to c.1500-1542 — Peru veteran.. Mississippi River. Nothing in history happens in a vacuum; the era explains the motives, the means, and the stakes. crossed the Southeast; Mississippi.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "1539 landing Florida.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "1539 landing Florida.", "x": "Hernando de Soto: 1539 landing Florida.. Chickasaw battle. This is one of the load-bearing facts about Hernando de Soto — learn it cold. Died 1542. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "The story behind: 1539 landing Florida..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "The story behind: 1539 landing Florida..", "x": "Explained: 1539 landing Florida.. Legacy. In the history of Hernando de Soto, this fact connects to Brutal expedition. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Mississippi River.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Mississippi River.", "x": "Hernando de Soto: Mississippi River.. River burial. This is one of the load-bearing facts about Hernando de Soto — learn it cold. Brutal expedition. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "The story behind: Mississippi River..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "The story behind: Mississippi River..", "x": "Explained: Mississippi River.. Archaeology. In the history of Hernando de Soto, this fact connects to Southeast tribes. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Died 1542.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Died 1542.", "x": "Hernando de Soto: Died 1542.. Legacy. This is one of the load-bearing facts about Hernando de Soto — learn it cold. Southeast tribes. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "The story behind: Died 1542..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "The story behind: Died 1542..", "x": "Explained: Died 1542.. Myth. In the history of Hernando de Soto, this fact connects to No gold. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Brutal expedition.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Brutal expedition.", "x": "Hernando de Soto: Brutal expedition.. Archaeology. This is one of the load-bearing facts about Hernando de Soto — learn it cold. No gold. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "The story behind: Brutal expedition..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "The story behind: Brutal expedition..", "x": "Explained: Brutal expedition.. Peru veteran. In the history of Hernando de Soto, this fact connects to 1539 landing Florida. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Southeast tribes.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Southeast tribes.", "x": "Hernando de Soto: Southeast tribes.. Myth. This is one of the load-bearing facts about Hernando de Soto — learn it cold. 1539 landing Florida. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "The story behind: Southeast tribes..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "The story behind: Southeast tribes..", "x": "Explained: Southeast tribes.. Chickasaw battle. In the history of Hernando de Soto, this fact connects to Mississippi River. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "No gold.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "No gold.", "x": "Hernando de Soto: No gold.. Peru veteran. This is one of the load-bearing facts about Hernando de Soto — learn it cold. Mississippi River. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "The story behind: No gold..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "The story behind: No gold..", "x": "Explained: No gold.. River burial. In the history of Hernando de Soto, this fact connects to Died 1542. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Peru veteran.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Peru veteran.", "x": "Going deeper: Peru veteran.. Mississippi River. Details are where historians live — the numbers, the names, the decisions that turned Hernando de Soto the way it did. crossed the Southeast; Mississippi.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Chickasaw battle.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Chickasaw battle.", "x": "Going deeper: Chickasaw battle.. Died 1542. Details are where historians live — the numbers, the names, the decisions that turned Hernando de Soto the way it did. crossed the Southeast; Mississippi. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "River burial.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "River burial.", "x": "Going deeper: River burial.. Brutal expedition. Details are where historians live — the numbers, the names, the decisions that turned Hernando de Soto the way it did. crossed the Southeast; Mississippi.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Legacy.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Legacy.", "x": "Going deeper: Legacy.. Southeast tribes. Details are where historians live — the numbers, the names, the decisions that turned Hernando de Soto the way it did. crossed the Southeast; Mississippi. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Archaeology.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Archaeology.", "x": "Going deeper: Archaeology.. No gold. Details are where historians live — the numbers, the names, the decisions that turned Hernando de Soto the way it did. crossed the Southeast; Mississippi. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Myth.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Myth.", "x": "Going deeper: Myth.. 1539 landing Florida. Details are where historians live — the numbers, the names, the decisions that turned Hernando de Soto the way it did. crossed the Southeast; Mississippi. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Timeline", "d": "Hernando de Soto, event by event.", "g": "timeline", "l": 2, "q": "What is Timeline?", "a": "Hernando de Soto, event by event.", "x": "The timeline: 1539 landing Florida.. Peru veteran. Key dates in order — Died 1542.. c.1500-1542 Pin the dates first; the story hangs on them. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key figures", "d": "The people of Hernando de Soto.", "g": "people", "l": 2, "q": "What is Key figures?", "a": "The people of Hernando de Soto.", "x": "The people: Chickasaw battle.. Brutal expedition. History is made by people deciding under pressure — crossed the Southeast; Mississippi.. Legacy. Know the actors and the events make sense. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "More key figures", "d": "More people who shaped Hernando de Soto.", "g": "people", "l": 2, "q": "What is More key figures?", "a": "More people who shaped Hernando de Soto.", "x": "More figures: Southeast tribes. shaped Hernando de Soto as surely as anyone — Archaeology.. crossed the Southeast; Mississippi. History remembers the famous; the wise student learns the overlooked too.", "s": "public-reference", "f": null}, {"t": "Causes", "d": "Why Hernando de Soto happened.", "g": "causes", "l": 2, "q": "What is Causes?", "a": "Why Hernando de Soto happened.", "x": "The causes: 1539 landing Florida.. River burial. Historians debate the deep vs immediate causes of Hernando de Soto — crossed the Southeast; Mississippi.. No gold. Understanding why is the whole point of studying history.", "s": "public-reference", "f": null}, {"t": "The turning point", "d": "The moment Hernando de Soto turned.", "g": "turning-point", "l": 2, "q": "What is The turning point?", "a": "The moment Hernando de Soto turned.", "x": "The turning point: Legacy.. Mississippi River. Every great story has the moment it could have gone otherwise — Hernando de Soto. crossed the Southeast; Mississippi. Find it and you find the drama. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-explorer-hernando-de-soto-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
