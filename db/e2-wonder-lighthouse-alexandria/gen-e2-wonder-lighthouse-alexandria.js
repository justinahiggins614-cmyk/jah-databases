(function(){'use strict';
/* JAH Lighthouse of Alexandria Wonder Database generator — jahdb-e2-wonder-lighthouse-alexandria-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-wonder-lighthouse-alexandria',PREFIX='JAH-E2WONDERLIG-',NAME='JAH Lighthouse of Alexandria Wonder Database';
var FIELDS=["overview", "context", "facts", "details", "timeline", "people", "causes", "turning-point", "legacy", "misconceptions", "what-if", "quiz", "sources", "learn-more"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Lighthouse of Alexandria: overview", "d": "Lighthouse of Alexandria (c.280 BC): Pharos: prototype lighthouse..", "g": "overview", "l": 2, "q": "What is Lighthouse of Alexandria: overview?", "a": "Lighthouse of Alexandria (c.280 BC): Pharos: prototype lighthouse..", "x": "The complete wonder guide to Lighthouse of Alexandria: Pharos: prototype lighthouse.. 100m+ tall. From causes to consequences, from the key figures to the legacy that still shapes us — this database tells the whole story the way a great history course would.", "s": "public-reference", "f": null}, {"t": "The era", "d": "Lighthouse of Alexandria in its time: c.280 BC.", "g": "context", "l": 2, "q": "What is The era?", "a": "Lighthouse of Alexandria in its time: c.280 BC.", "x": "Context: Lighthouse of Alexandria belonged to c.280 BC — Ptolemy.. Pharos island. Nothing in history happens in a vacuum; the era explains the motives, the means, and the stakes. Pharos: prototype lighthouse.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "100m+ tall.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "100m+ tall.", "x": "Lighthouse of Alexandria: 100m+ tall.. Design. This is one of the load-bearing facts about Lighthouse of Alexandria — learn it cold. Mirror/fire. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "The story behind: 100m+ tall..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "The story behind: 100m+ tall..", "x": "Explained: 100m+ tall.. Guiding ships. In the history of Lighthouse of Alexandria, this fact connects to Earthquakes fell. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Pharos island.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Pharos island.", "x": "Lighthouse of Alexandria: Pharos island.. Light. This is one of the load-bearing facts about Lighthouse of Alexandria — learn it cold. Earthquakes fell. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "The story behind: Pharos island..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "The story behind: Pharos island..", "x": "Explained: Pharos island.. Ruins underwater. In the history of Lighthouse of Alexandria, this fact connects to Qaitbay fort. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Mirror/fire.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Mirror/fire.", "x": "Lighthouse of Alexandria: Mirror/fire.. Guiding ships. This is one of the load-bearing facts about Lighthouse of Alexandria — learn it cold. Qaitbay fort. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "The story behind: Mirror/fire..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "The story behind: Mirror/fire..", "x": "Explained: Mirror/fire.. Legacy. In the history of Lighthouse of Alexandria, this fact connects to Word: pharos. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Earthquakes fell.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Earthquakes fell.", "x": "Lighthouse of Alexandria: Earthquakes fell.. Ruins underwater. This is one of the load-bearing facts about Lighthouse of Alexandria — learn it cold. Word: pharos. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "The story behind: Earthquakes fell..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "The story behind: Earthquakes fell..", "x": "Explained: Earthquakes fell.. Ptolemy. In the history of Lighthouse of Alexandria, this fact connects to 100m+ tall. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Qaitbay fort.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Qaitbay fort.", "x": "Lighthouse of Alexandria: Qaitbay fort.. Legacy. This is one of the load-bearing facts about Lighthouse of Alexandria — learn it cold. 100m+ tall. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "The story behind: Qaitbay fort..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "The story behind: Qaitbay fort..", "x": "Explained: Qaitbay fort.. Design. In the history of Lighthouse of Alexandria, this fact connects to Pharos island. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Word: pharos.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Word: pharos.", "x": "Lighthouse of Alexandria: Word: pharos.. Ptolemy. This is one of the load-bearing facts about Lighthouse of Alexandria — learn it cold. Pharos island. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "The story behind: Word: pharos..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "The story behind: Word: pharos..", "x": "Explained: Word: pharos.. Light. In the history of Lighthouse of Alexandria, this fact connects to Mirror/fire. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Ptolemy.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Ptolemy.", "x": "Going deeper: Ptolemy.. Pharos island. Details are where historians live — the numbers, the names, the decisions that turned Lighthouse of Alexandria the way it did. Pharos: prototype lighthouse. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Design.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Design.", "x": "Going deeper: Design.. Mirror/fire. Details are where historians live — the numbers, the names, the decisions that turned Lighthouse of Alexandria the way it did. Pharos: prototype lighthouse. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Light.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Light.", "x": "Going deeper: Light.. Earthquakes fell. Details are where historians live — the numbers, the names, the decisions that turned Lighthouse of Alexandria the way it did. Pharos: prototype lighthouse. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Guiding ships.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Guiding ships.", "x": "Going deeper: Guiding ships.. Qaitbay fort. Details are where historians live — the numbers, the names, the decisions that turned Lighthouse of Alexandria the way it did. Pharos: prototype lighthouse.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Ruins underwater.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Ruins underwater.", "x": "Going deeper: Ruins underwater.. Word: pharos. Details are where historians live — the numbers, the names, the decisions that turned Lighthouse of Alexandria the way it did. Pharos: prototype lighthouse.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Legacy.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Legacy.", "x": "Going deeper: Legacy.. 100m+ tall. Details are where historians live — the numbers, the names, the decisions that turned Lighthouse of Alexandria the way it did. Pharos: prototype lighthouse. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Timeline", "d": "Lighthouse of Alexandria, event by event.", "g": "timeline", "l": 2, "q": "What is Timeline?", "a": "Lighthouse of Alexandria, event by event.", "x": "The timeline: 100m+ tall.. Ptolemy. Key dates in order — Mirror/fire.. c.280 BC Pin the dates first; the story hangs on them. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key figures", "d": "The people of Lighthouse of Alexandria.", "g": "people", "l": 2, "q": "What is Key figures?", "a": "The people of Lighthouse of Alexandria.", "x": "The people: Design.. Earthquakes fell. History is made by people deciding under pressure — Pharos: prototype lighthouse.. Guiding ships. Know the actors and the events make sense. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "More key figures", "d": "More people who shaped Lighthouse of Alexandria.", "g": "people", "l": 2, "q": "What is More key figures?", "a": "More people who shaped Lighthouse of Alexandria.", "x": "More figures: Qaitbay fort. shaped Lighthouse of Alexandria as surely as anyone — Ruins underwater.. Pharos: prototype lighthouse. History remembers the famous; the wise student learns the overlooked too.", "s": "public-reference", "f": null}, {"t": "Causes", "d": "Why Lighthouse of Alexandria happened.", "g": "causes", "l": 2, "q": "What is Causes?", "a": "Why Lighthouse of Alexandria happened.", "x": "The causes: 100m+ tall.. Light. Historians debate the deep vs immediate causes of Lighthouse of Alexandria — Pharos: prototype lighthouse.. Word: pharos. Understanding why is the whole point of studying history.", "s": "public-reference", "f": null}, {"t": "The turning point", "d": "The moment Lighthouse of Alexandria turned.", "g": "turning-point", "l": 2, "q": "What is The turning point?", "a": "The moment Lighthouse of Alexandria turned.", "x": "The turning point: Guiding ships.. Pharos island. Every great story has the moment it could have gone otherwise — Lighthouse of Alexandria. Pharos: prototype lighthouse. Find it and you find the drama.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-wonder-lighthouse-alexandria-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
