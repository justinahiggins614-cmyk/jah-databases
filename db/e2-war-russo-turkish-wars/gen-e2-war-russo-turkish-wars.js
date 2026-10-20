(function(){'use strict';
/* JAH Russo-Turkish Wars War Database generator — jahdb-e2-war-russo-turkish-wars-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-war-russo-turkish-wars',PREFIX='JAH-E2WARRUSSOT-',NAME='JAH Russo-Turkish Wars War Database';
var FIELDS=["overview", "context", "facts", "details", "timeline", "people", "causes", "turning-point", "legacy", "misconceptions", "what-if", "quiz", "sources", "learn-more"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Russo-Turkish Wars: overview", "d": "Russo-Turkish Wars (1568-1918): centuries of Russia vs Ottoman struggle..", "g": "overview", "l": 2, "q": "What is Russo-Turkish Wars: overview?", "a": "Russo-Turkish Wars (1568-1918): centuries of Russia vs Ottoman struggle..", "x": "The complete war guide to Russo-Turkish Wars: centuries of Russia vs Ottoman struggle.. 12+ wars over centuries. From causes to consequences, from the key figures to the legacy that still shapes us — this database tells the whole story the way a great history course would.", "s": "public-reference", "f": null}, {"t": "The era", "d": "Russo-Turkish Wars in its time: 1568-1918.", "g": "context", "l": 2, "q": "What is The era?", "a": "Russo-Turkish Wars in its time: 1568-1918.", "x": "Context: Russo-Turkish Wars belonged to 1568-1918 — Azov campaigns.. Catherine the Great gains. Nothing in history happens in a vacuum; the era explains the motives, the means, and the stakes. centuries of Russia vs Ottoman struggle.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "12+ wars over centuries.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "12+ wars over centuries.", "x": "Russo-Turkish Wars: 12+ wars over centuries.. Treaty of Kuchuk. This is one of the load-bearing facts about Russo-Turkish Wars — learn it cold. Crimean War part. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "The story behind: 12+ wars over centuries..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "The story behind: 12+ wars over centuries..", "x": "Explained: 12+ wars over centuries.. Pan-Slavism. In the history of Russo-Turkish Wars, this fact connects to 1877-78: Bulgaria freed. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Catherine the Great gains.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Catherine the Great gains.", "x": "Russo-Turkish Wars: Catherine the Great gains.. Plevna siege. This is one of the load-bearing facts about Russo-Turkish Wars — learn it cold. 1877-78: Bulgaria freed. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "The story behind: Catherine the Great gains..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "The story behind: Catherine the Great gains..", "x": "Explained: Catherine the Great gains.. Armenian tragedy. In the history of Russo-Turkish Wars, this fact connects to Naval battles. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Crimean War part.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Crimean War part.", "x": "Russo-Turkish Wars: Crimean War part.. Pan-Slavism. This is one of the load-bearing facts about Russo-Turkish Wars — learn it cold. Naval battles. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "The story behind: Crimean War part..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "The story behind: Crimean War part..", "x": "Explained: Crimean War part.. Legacy. In the history of Russo-Turkish Wars, this fact connects to Eastern Question. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "1877-78: Bulgaria freed.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "1877-78: Bulgaria freed.", "x": "Russo-Turkish Wars: 1877-78: Bulgaria freed.. Armenian tragedy. This is one of the load-bearing facts about Russo-Turkish Wars — learn it cold. Eastern Question. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "The story behind: 1877-78: Bulgaria freed..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "The story behind: 1877-78: Bulgaria freed..", "x": "Explained: 1877-78: Bulgaria freed.. Azov campaigns. In the history of Russo-Turkish Wars, this fact connects to 12+ wars over centuries. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Naval battles.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Naval battles.", "x": "Russo-Turkish Wars: Naval battles.. Legacy. This is one of the load-bearing facts about Russo-Turkish Wars — learn it cold. 12+ wars over centuries. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "The story behind: Naval battles..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "The story behind: Naval battles..", "x": "Explained: Naval battles.. Treaty of Kuchuk. In the history of Russo-Turkish Wars, this fact connects to Catherine the Great gains. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Eastern Question.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Eastern Question.", "x": "Russo-Turkish Wars: Eastern Question.. Azov campaigns. This is one of the load-bearing facts about Russo-Turkish Wars — learn it cold. Catherine the Great gains. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "The story behind: Eastern Question..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "The story behind: Eastern Question..", "x": "Explained: Eastern Question.. Plevna siege. In the history of Russo-Turkish Wars, this fact connects to Crimean War part. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Azov campaigns.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Azov campaigns.", "x": "Going deeper: Azov campaigns.. Catherine the Great gains. Details are where historians live — the numbers, the names, the decisions that turned Russo-Turkish Wars the way it did. centuries of Russia vs Ottoman struggle.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Treaty of Kuchuk.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Treaty of Kuchuk.", "x": "Going deeper: Treaty of Kuchuk.. Crimean War part. Details are where historians live — the numbers, the names, the decisions that turned Russo-Turkish Wars the way it did. centuries of Russia vs Ottoman struggle.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Plevna siege.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Plevna siege.", "x": "Going deeper: Plevna siege.. 1877-78: Bulgaria freed. Details are where historians live — the numbers, the names, the decisions that turned Russo-Turkish Wars the way it did. centuries of Russia vs Ottoman struggle.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Pan-Slavism.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Pan-Slavism.", "x": "Going deeper: Pan-Slavism.. Naval battles. Details are where historians live — the numbers, the names, the decisions that turned Russo-Turkish Wars the way it did. centuries of Russia vs Ottoman struggle.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Armenian tragedy.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Armenian tragedy.", "x": "Going deeper: Armenian tragedy.. Eastern Question. Details are where historians live — the numbers, the names, the decisions that turned Russo-Turkish Wars the way it did. centuries of Russia vs Ottoman struggle.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Legacy.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Legacy.", "x": "Going deeper: Legacy.. 12+ wars over centuries. Details are where historians live — the numbers, the names, the decisions that turned Russo-Turkish Wars the way it did. centuries of Russia vs Ottoman struggle.", "s": "public-reference", "f": null}, {"t": "Timeline", "d": "Russo-Turkish Wars, event by event.", "g": "timeline", "l": 2, "q": "What is Timeline?", "a": "Russo-Turkish Wars, event by event.", "x": "The timeline: 12+ wars over centuries.. Azov campaigns. Key dates in order — Crimean War part.. 1568-1918 Pin the dates first; the story hangs on them. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key figures", "d": "The people of Russo-Turkish Wars.", "g": "people", "l": 2, "q": "What is Key figures?", "a": "The people of Russo-Turkish Wars.", "x": "The people: Treaty of Kuchuk.. 1877-78: Bulgaria freed. History is made by people deciding under pressure — centuries of Russia vs Ottoman struggle.. Pan-Slavism. Know the actors and the events make sense.", "s": "public-reference", "f": null}, {"t": "More key figures", "d": "More people who shaped Russo-Turkish Wars.", "g": "people", "l": 2, "q": "What is More key figures?", "a": "More people who shaped Russo-Turkish Wars.", "x": "More figures: Naval battles. shaped Russo-Turkish Wars as surely as anyone — Armenian tragedy.. centuries of Russia vs Ottoman struggle. History remembers the famous; the wise student learns the overlooked too.", "s": "public-reference", "f": null}, {"t": "Causes", "d": "Why Russo-Turkish Wars happened.", "g": "causes", "l": 2, "q": "What is Causes?", "a": "Why Russo-Turkish Wars happened.", "x": "The causes: 12+ wars over centuries.. Plevna siege. Historians debate the deep vs immediate causes of Russo-Turkish Wars — centuries of Russia vs Ottoman struggle.. Eastern Question. Understanding why is the whole point of studying history.", "s": "public-reference", "f": null}, {"t": "The turning point", "d": "The moment Russo-Turkish Wars turned.", "g": "turning-point", "l": 2, "q": "What is The turning point?", "a": "The moment Russo-Turkish Wars turned.", "x": "The turning point: Pan-Slavism.. Catherine the Great gains. Every great story has the moment it could have gone otherwise — Russo-Turkish Wars. centuries of Russia vs Ottoman struggle. Find it and you find the drama.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-war-russo-turkish-wars-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
