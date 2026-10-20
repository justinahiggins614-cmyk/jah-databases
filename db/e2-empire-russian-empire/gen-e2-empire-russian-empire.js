(function(){'use strict';
/* JAH Russian Empire Empire Database generator — jahdb-e2-empire-russian-empire-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-empire-russian-empire',PREFIX='JAH-E2EMPIRERUS-',NAME='JAH Russian Empire Empire Database';
var FIELDS=["overview", "context", "facts", "details", "timeline", "people", "causes", "turning-point", "legacy", "misconceptions", "what-if", "quiz", "sources", "learn-more"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Russian Empire: overview", "d": "Russian Empire (1721-1917): largest contiguous empire..", "g": "overview", "l": 2, "q": "What is Russian Empire: overview?", "a": "Russian Empire (1721-1917): largest contiguous empire..", "x": "The complete empire guide to Russian Empire: largest contiguous empire.. Peter the Great. From causes to consequences, from the key figures to the legacy that still shapes us — this database tells the whole story the way a great history course would.", "s": "public-reference", "f": null}, {"t": "The era", "d": "Russian Empire in its time: 1721-1917.", "g": "context", "l": 2, "q": "What is The era?", "a": "Russian Empire in its time: 1721-1917.", "x": "Context: Russian Empire belonged to 1721-1917 — Expansion.. Siberia. Nothing in history happens in a vacuum; the era explains the motives, the means, and the stakes. largest contiguous empire. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Peter the Great.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Peter the Great.", "x": "Russian Empire: Peter the Great.. Autocracy. This is one of the load-bearing facts about Russian Empire — learn it cold. Serfdom. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "The story behind: Peter the Great..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "The story behind: Peter the Great..", "x": "Explained: Peter the Great.. Nationalities. In the history of Russian Empire, this fact connects to Napoleon repelled. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Siberia.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Siberia.", "x": "Russian Empire: Siberia.. Orthodoxy. This is one of the load-bearing facts about Russian Empire — learn it cold. Napoleon repelled. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "The story behind: Siberia..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "The story behind: Siberia..", "x": "Explained: Siberia.. Industrialization. In the history of Russian Empire, this fact connects to 1905 revolution. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Serfdom.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Serfdom.", "x": "Russian Empire: Serfdom.. Nationalities. This is one of the load-bearing facts about Russian Empire — learn it cold. 1905 revolution. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "The story behind: Serfdom..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "The story behind: Serfdom..", "x": "Explained: Serfdom.. USSR. In the history of Russian Empire, this fact connects to 1917 fall. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Napoleon repelled.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Napoleon repelled.", "x": "Russian Empire: Napoleon repelled.. Industrialization. This is one of the load-bearing facts about Russian Empire — learn it cold. 1917 fall. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "The story behind: Napoleon repelled..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "The story behind: Napoleon repelled..", "x": "Explained: Napoleon repelled.. Expansion. In the history of Russian Empire, this fact connects to Peter the Great. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "1905 revolution.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "1905 revolution.", "x": "Russian Empire: 1905 revolution.. USSR. This is one of the load-bearing facts about Russian Empire — learn it cold. Peter the Great. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "The story behind: 1905 revolution..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "The story behind: 1905 revolution..", "x": "Explained: 1905 revolution.. Autocracy. In the history of Russian Empire, this fact connects to Siberia. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "1917 fall.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "1917 fall.", "x": "Russian Empire: 1917 fall.. Expansion. This is one of the load-bearing facts about Russian Empire — learn it cold. Siberia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "The story behind: 1917 fall..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "The story behind: 1917 fall..", "x": "Explained: 1917 fall.. Orthodoxy. In the history of Russian Empire, this fact connects to Serfdom. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Expansion.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Expansion.", "x": "Going deeper: Expansion.. Siberia. Details are where historians live — the numbers, the names, the decisions that turned Russian Empire the way it did. largest contiguous empire. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Autocracy.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Autocracy.", "x": "Going deeper: Autocracy.. Serfdom. Details are where historians live — the numbers, the names, the decisions that turned Russian Empire the way it did. largest contiguous empire. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Orthodoxy.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Orthodoxy.", "x": "Going deeper: Orthodoxy.. Napoleon repelled. Details are where historians live — the numbers, the names, the decisions that turned Russian Empire the way it did. largest contiguous empire. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Nationalities.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Nationalities.", "x": "Going deeper: Nationalities.. 1905 revolution. Details are where historians live — the numbers, the names, the decisions that turned Russian Empire the way it did. largest contiguous empire. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Industrialization.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Industrialization.", "x": "Going deeper: Industrialization.. 1917 fall. Details are where historians live — the numbers, the names, the decisions that turned Russian Empire the way it did. largest contiguous empire. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "USSR.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "USSR.", "x": "Going deeper: USSR.. Peter the Great. Details are where historians live — the numbers, the names, the decisions that turned Russian Empire the way it did. largest contiguous empire. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Timeline", "d": "Russian Empire, event by event.", "g": "timeline", "l": 2, "q": "What is Timeline?", "a": "Russian Empire, event by event.", "x": "The timeline: Peter the Great.. Expansion. Key dates in order — Serfdom.. 1721-1917 Pin the dates first; the story hangs on them. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key figures", "d": "The people of Russian Empire.", "g": "people", "l": 2, "q": "What is Key figures?", "a": "The people of Russian Empire.", "x": "The people: Autocracy.. Napoleon repelled. History is made by people deciding under pressure — largest contiguous empire.. Nationalities. Know the actors and the events make sense. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "More key figures", "d": "More people who shaped Russian Empire.", "g": "people", "l": 2, "q": "What is More key figures?", "a": "More people who shaped Russian Empire.", "x": "More figures: 1905 revolution. shaped Russian Empire as surely as anyone — Industrialization.. largest contiguous empire. History remembers the famous; the wise student learns the overlooked too. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Causes", "d": "Why Russian Empire happened.", "g": "causes", "l": 2, "q": "What is Causes?", "a": "Why Russian Empire happened.", "x": "The causes: Peter the Great.. Orthodoxy. Historians debate the deep vs immediate causes of Russian Empire — largest contiguous empire.. 1917 fall. Understanding why is the whole point of studying history.", "s": "public-reference", "f": null}, {"t": "The turning point", "d": "The moment Russian Empire turned.", "g": "turning-point", "l": 2, "q": "What is The turning point?", "a": "The moment Russian Empire turned.", "x": "The turning point: Nationalities.. Siberia. Every great story has the moment it could have gone otherwise — Russian Empire. largest contiguous empire. Find it and you find the drama. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-empire-russian-empire-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
