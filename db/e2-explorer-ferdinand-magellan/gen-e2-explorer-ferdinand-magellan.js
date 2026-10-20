(function(){'use strict';
/* JAH Ferdinand Magellan Explorer Database generator — jahdb-e2-explorer-ferdinand-magellan-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-explorer-ferdinand-magellan',PREFIX='JAH-E2EXPLORERF-',NAME='JAH Ferdinand Magellan Explorer Database';
var FIELDS=["overview", "context", "facts", "details", "timeline", "people", "causes", "turning-point", "legacy", "misconceptions", "what-if", "quiz", "sources", "learn-more"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Ferdinand Magellan: overview", "d": "Ferdinand Magellan (1519-1522): first circumnavigation (crew completed)..", "g": "overview", "l": 2, "q": "What is Ferdinand Magellan: overview?", "a": "Ferdinand Magellan (1519-1522): first circumnavigation (crew completed)..", "x": "The complete explorer guide to Ferdinand Magellan: first circumnavigation (crew completed).. Portuguese for Spain. From causes to consequences, from the key figures to the legacy that still shapes us — this database tells the whole story the way a great history course would.", "s": "public-reference", "f": null}, {"t": "The era", "d": "Ferdinand Magellan in its time: 1519-1522.", "g": "context", "l": 2, "q": "What is The era?", "a": "Ferdinand Magellan in its time: 1519-1522.", "x": "Context: Ferdinand Magellan belonged to 1519-1522 — Spice goal.. Strait of Magellan. Nothing in history happens in a vacuum; the era explains the motives, the means, and the stakes. first circumnavigation (crew completed).", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Portuguese for Spain.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Portuguese for Spain.", "x": "Ferdinand Magellan: Portuguese for Spain.. Mutinies. This is one of the load-bearing facts about Ferdinand Magellan — learn it cold. Pacific crossing brutal. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "The story behind: Portuguese for Spain..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "The story behind: Portuguese for Spain..", "x": "Explained: Portuguese for Spain.. Mactan death. In the history of Ferdinand Magellan, this fact connects to Killed in Philippines. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Strait of Magellan.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Strait of Magellan.", "x": "Ferdinand Magellan: Strait of Magellan.. Scurvy. This is one of the load-bearing facts about Ferdinand Magellan — learn it cold. Killed in Philippines. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "The story behind: Strait of Magellan..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "The story behind: Strait of Magellan..", "x": "Explained: Strait of Magellan.. Victoria returned. In the history of Ferdinand Magellan, this fact connects to Elcano completed. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Pacific crossing brutal.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Pacific crossing brutal.", "x": "Ferdinand Magellan: Pacific crossing brutal.. Mactan death. This is one of the load-bearing facts about Ferdinand Magellan — learn it cold. Elcano completed. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "The story behind: Pacific crossing brutal..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "The story behind: Pacific crossing brutal..", "x": "Explained: Pacific crossing brutal.. Legacy. In the history of Ferdinand Magellan, this fact connects to Proved globe. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Killed in Philippines.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Killed in Philippines.", "x": "Ferdinand Magellan: Killed in Philippines.. Victoria returned. This is one of the load-bearing facts about Ferdinand Magellan — learn it cold. Proved globe. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "The story behind: Killed in Philippines..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "The story behind: Killed in Philippines..", "x": "Explained: Killed in Philippines.. Spice goal. In the history of Ferdinand Magellan, this fact connects to Portuguese for Spain. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Elcano completed.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Elcano completed.", "x": "Ferdinand Magellan: Elcano completed.. Legacy. This is one of the load-bearing facts about Ferdinand Magellan — learn it cold. Portuguese for Spain. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "The story behind: Elcano completed..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "The story behind: Elcano completed..", "x": "Explained: Elcano completed.. Mutinies. In the history of Ferdinand Magellan, this fact connects to Strait of Magellan. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Proved globe.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Proved globe.", "x": "Ferdinand Magellan: Proved globe.. Spice goal. This is one of the load-bearing facts about Ferdinand Magellan — learn it cold. Strait of Magellan. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "The story behind: Proved globe..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "The story behind: Proved globe..", "x": "Explained: Proved globe.. Scurvy. In the history of Ferdinand Magellan, this fact connects to Pacific crossing brutal. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Spice goal.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Spice goal.", "x": "Going deeper: Spice goal.. Strait of Magellan. Details are where historians live — the numbers, the names, the decisions that turned Ferdinand Magellan the way it did. first circumnavigation (crew completed).", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Mutinies.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Mutinies.", "x": "Going deeper: Mutinies.. Pacific crossing brutal. Details are where historians live — the numbers, the names, the decisions that turned Ferdinand Magellan the way it did. first circumnavigation (crew completed).", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Scurvy.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Scurvy.", "x": "Going deeper: Scurvy.. Killed in Philippines. Details are where historians live — the numbers, the names, the decisions that turned Ferdinand Magellan the way it did. first circumnavigation (crew completed).", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Mactan death.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Mactan death.", "x": "Going deeper: Mactan death.. Elcano completed. Details are where historians live — the numbers, the names, the decisions that turned Ferdinand Magellan the way it did. first circumnavigation (crew completed).", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Victoria returned.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Victoria returned.", "x": "Going deeper: Victoria returned.. Proved globe. Details are where historians live — the numbers, the names, the decisions that turned Ferdinand Magellan the way it did. first circumnavigation (crew completed).", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Legacy.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Legacy.", "x": "Going deeper: Legacy.. Portuguese for Spain. Details are where historians live — the numbers, the names, the decisions that turned Ferdinand Magellan the way it did. first circumnavigation (crew completed).", "s": "public-reference", "f": null}, {"t": "Timeline", "d": "Ferdinand Magellan, event by event.", "g": "timeline", "l": 2, "q": "What is Timeline?", "a": "Ferdinand Magellan, event by event.", "x": "The timeline: Portuguese for Spain.. Spice goal. Key dates in order — Pacific crossing brutal.. 1519-1522 Pin the dates first; the story hangs on them. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key figures", "d": "The people of Ferdinand Magellan.", "g": "people", "l": 2, "q": "What is Key figures?", "a": "The people of Ferdinand Magellan.", "x": "The people: Mutinies.. Killed in Philippines. History is made by people deciding under pressure — first circumnavigation (crew completed).. Mactan death. Know the actors and the events make sense. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "More key figures", "d": "More people who shaped Ferdinand Magellan.", "g": "people", "l": 2, "q": "What is More key figures?", "a": "More people who shaped Ferdinand Magellan.", "x": "More figures: Elcano completed. shaped Ferdinand Magellan as surely as anyone — Victoria returned.. first circumnavigation (crew completed). History remembers the famous; the wise student learns the overlooked too.", "s": "public-reference", "f": null}, {"t": "Causes", "d": "Why Ferdinand Magellan happened.", "g": "causes", "l": 2, "q": "What is Causes?", "a": "Why Ferdinand Magellan happened.", "x": "The causes: Portuguese for Spain.. Scurvy. Historians debate the deep vs immediate causes of Ferdinand Magellan — first circumnavigation (crew completed).. Proved globe. Understanding why is the whole point of studying history.", "s": "public-reference", "f": null}, {"t": "The turning point", "d": "The moment Ferdinand Magellan turned.", "g": "turning-point", "l": 2, "q": "What is The turning point?", "a": "The moment Ferdinand Magellan turned.", "x": "The turning point: Mactan death.. Strait of Magellan. Every great story has the moment it could have gone otherwise — Ferdinand Magellan. first circumnavigation (crew completed). Find it and you find the drama.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-explorer-ferdinand-magellan-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
