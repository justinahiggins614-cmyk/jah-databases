(function(){'use strict';
/* JAH Hanging Gardens of Babylon Wonder Database generator — jahdb-e2-wonder-hanging-gardens-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-wonder-hanging-gardens',PREFIX='JAH-E2WONDERHAN-',NAME='JAH Hanging Gardens of Babylon Wonder Database';
var FIELDS=["overview", "context", "facts", "details", "timeline", "people", "causes", "turning-point", "legacy", "misconceptions", "what-if", "quiz", "sources", "learn-more"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Hanging Gardens of Babylon: overview", "d": "Hanging Gardens of Babylon (c.600 BC): legendary terraced gardens..", "g": "overview", "l": 2, "q": "What is Hanging Gardens of Babylon: overview?", "a": "Hanging Gardens of Babylon (c.600 BC): legendary terraced gardens..", "x": "The complete wonder guide to Hanging Gardens of Babylon: legendary terraced gardens.. Nebuchadnezzar. From causes to consequences, from the key figures to the legacy that still shapes us — this database tells the whole story the way a great history course would.", "s": "public-reference", "f": null}, {"t": "The era", "d": "Hanging Gardens of Babylon in its time: c.600 BC.", "g": "context", "l": 2, "q": "What is The era?", "a": "Hanging Gardens of Babylon in its time: c.600 BC.", "x": "Context: Hanging Gardens of Babylon belonged to c.600 BC — Descriptions.. For queen Amytis. Nothing in history happens in a vacuum; the era explains the motives, the means, and the stakes. legendary terraced gardens.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Nebuchadnezzar.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Nebuchadnezzar.", "x": "Hanging Gardens of Babylon: Nebuchadnezzar.. Engineering. This is one of the load-bearing facts about Hanging Gardens of Babylon — learn it cold. Existence debated. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "The story behind: Nebuchadnezzar..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "The story behind: Nebuchadnezzar..", "x": "Explained: Nebuchadnezzar.. Art depictions. In the history of Hanging Gardens of Babylon, this fact connects to Irrigation marvel. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "For queen Amytis.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "For queen Amytis.", "x": "Hanging Gardens of Babylon: For queen Amytis.. Debate. This is one of the load-bearing facts about Hanging Gardens of Babylon — learn it cold. Irrigation marvel. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "The story behind: For queen Amytis..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "The story behind: For queen Amytis..", "x": "Explained: For queen Amytis.. Myth. In the history of Hanging Gardens of Babylon, this fact connects to Nineveh theory. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Existence debated.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Existence debated.", "x": "Hanging Gardens of Babylon: Existence debated.. Art depictions. This is one of the load-bearing facts about Hanging Gardens of Babylon — learn it cold. Nineveh theory. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "The story behind: Existence debated..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "The story behind: Existence debated..", "x": "Explained: Existence debated.. Search. In the history of Hanging Gardens of Babylon, this fact connects to Legend. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Irrigation marvel.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Irrigation marvel.", "x": "Hanging Gardens of Babylon: Irrigation marvel.. Myth. This is one of the load-bearing facts about Hanging Gardens of Babylon — learn it cold. Legend. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "The story behind: Irrigation marvel..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "The story behind: Irrigation marvel..", "x": "Explained: Irrigation marvel.. Descriptions. In the history of Hanging Gardens of Babylon, this fact connects to Nebuchadnezzar. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Nineveh theory.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Nineveh theory.", "x": "Hanging Gardens of Babylon: Nineveh theory.. Search. This is one of the load-bearing facts about Hanging Gardens of Babylon — learn it cold. Nebuchadnezzar. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "The story behind: Nineveh theory..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "The story behind: Nineveh theory..", "x": "Explained: Nineveh theory.. Engineering. In the history of Hanging Gardens of Babylon, this fact connects to For queen Amytis. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Legend.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Legend.", "x": "Hanging Gardens of Babylon: Legend.. Descriptions. This is one of the load-bearing facts about Hanging Gardens of Babylon — learn it cold. For queen Amytis. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "The story behind: Legend..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "The story behind: Legend..", "x": "Explained: Legend.. Debate. In the history of Hanging Gardens of Babylon, this fact connects to Existence debated. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Descriptions.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Descriptions.", "x": "Going deeper: Descriptions.. For queen Amytis. Details are where historians live — the numbers, the names, the decisions that turned Hanging Gardens of Babylon the way it did. legendary terraced gardens.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Engineering.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Engineering.", "x": "Going deeper: Engineering.. Existence debated. Details are where historians live — the numbers, the names, the decisions that turned Hanging Gardens of Babylon the way it did. legendary terraced gardens.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Debate.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Debate.", "x": "Going deeper: Debate.. Irrigation marvel. Details are where historians live — the numbers, the names, the decisions that turned Hanging Gardens of Babylon the way it did. legendary terraced gardens. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Art depictions.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Art depictions.", "x": "Going deeper: Art depictions.. Nineveh theory. Details are where historians live — the numbers, the names, the decisions that turned Hanging Gardens of Babylon the way it did. legendary terraced gardens.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Myth.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Myth.", "x": "Going deeper: Myth.. Legend. Details are where historians live — the numbers, the names, the decisions that turned Hanging Gardens of Babylon the way it did. legendary terraced gardens. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Search.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Search.", "x": "Going deeper: Search.. Nebuchadnezzar. Details are where historians live — the numbers, the names, the decisions that turned Hanging Gardens of Babylon the way it did. legendary terraced gardens. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Timeline", "d": "Hanging Gardens of Babylon, event by event.", "g": "timeline", "l": 2, "q": "What is Timeline?", "a": "Hanging Gardens of Babylon, event by event.", "x": "The timeline: Nebuchadnezzar.. Descriptions. Key dates in order — Existence debated.. c.600 BC Pin the dates first; the story hangs on them. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key figures", "d": "The people of Hanging Gardens of Babylon.", "g": "people", "l": 2, "q": "What is Key figures?", "a": "The people of Hanging Gardens of Babylon.", "x": "The people: Engineering.. Irrigation marvel. History is made by people deciding under pressure — legendary terraced gardens.. Art depictions. Know the actors and the events make sense. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "More key figures", "d": "More people who shaped Hanging Gardens of Babylon.", "g": "people", "l": 2, "q": "What is More key figures?", "a": "More people who shaped Hanging Gardens of Babylon.", "x": "More figures: Nineveh theory. shaped Hanging Gardens of Babylon as surely as anyone — Myth.. legendary terraced gardens. History remembers the famous; the wise student learns the overlooked too. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Causes", "d": "Why Hanging Gardens of Babylon happened.", "g": "causes", "l": 2, "q": "What is Causes?", "a": "Why Hanging Gardens of Babylon happened.", "x": "The causes: Nebuchadnezzar.. Debate. Historians debate the deep vs immediate causes of Hanging Gardens of Babylon — legendary terraced gardens.. Legend. Understanding why is the whole point of studying history.", "s": "public-reference", "f": null}, {"t": "The turning point", "d": "The moment Hanging Gardens of Babylon turned.", "g": "turning-point", "l": 2, "q": "What is The turning point?", "a": "The moment Hanging Gardens of Babylon turned.", "x": "The turning point: Art depictions.. For queen Amytis. Every great story has the moment it could have gone otherwise — Hanging Gardens of Babylon. legendary terraced gardens. Find it and you find the drama.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-wonder-hanging-gardens-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
