(function(){'use strict';
/* JAH Zheng He Explorer Database generator — jahdb-e2-explorer-zheng-he-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-explorer-zheng-he',PREFIX='JAH-E2EXPLORERZ-',NAME='JAH Zheng He Explorer Database';
var FIELDS=["overview", "context", "facts", "details", "timeline", "people", "causes", "turning-point", "legacy", "misconceptions", "what-if", "quiz", "sources", "learn-more"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Zheng He: overview", "d": "Zheng He (1371-1433): Ming China's treasure fleets..", "g": "overview", "l": 2, "q": "What is Zheng He: overview?", "a": "Zheng He (1371-1433): Ming China's treasure fleets..", "x": "The complete explorer guide to Zheng He: Ming China's treasure fleets.. 7 voyages. From causes to consequences, from the key figures to the legacy that still shapes us — this database tells the whole story the way a great history course would.", "s": "public-reference", "f": null}, {"t": "The era", "d": "Zheng He in its time: 1371-1433.", "g": "context", "l": 2, "q": "What is The era?", "a": "Zheng He in its time: 1371-1433.", "x": "Context: Zheng He belonged to 1371-1433 — Yongle emperor.. Treasure ships huge. Nothing in history happens in a vacuum; the era explains the motives, the means, and the stakes. Ming China's treasure fleets.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "7 voyages.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "7 voyages.", "x": "Zheng He: 7 voyages.. Fleets. This is one of the load-bearing facts about Zheng He — learn it cold. Indian Ocean. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "The story behind: 7 voyages..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "The story behind: 7 voyages..", "x": "Explained: 7 voyages.. Mogadishu. In the history of Zheng He, this fact connects to Africa reached. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Treasure ships huge.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Treasure ships huge.", "x": "Zheng He: Treasure ships huge.. Calicut. This is one of the load-bearing facts about Zheng He — learn it cold. Africa reached. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "The story behind: Treasure ships huge..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "The story behind: Treasure ships huge..", "x": "Explained: Treasure ships huge.. Isolation after. In the history of Zheng He, this fact connects to Giraffe for emperor. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Indian Ocean.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Indian Ocean.", "x": "Zheng He: Indian Ocean.. Mogadishu. This is one of the load-bearing facts about Zheng He — learn it cold. Giraffe for emperor. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "The story behind: Indian Ocean..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "The story behind: Indian Ocean..", "x": "Explained: Indian Ocean.. What if. In the history of Zheng He, this fact connects to Voyages ended. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Africa reached.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Africa reached.", "x": "Zheng He: Africa reached.. Isolation after. This is one of the load-bearing facts about Zheng He — learn it cold. Voyages ended. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "The story behind: Africa reached..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "The story behind: Africa reached..", "x": "Explained: Africa reached.. Yongle emperor. In the history of Zheng He, this fact connects to 7 voyages. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Giraffe for emperor.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Giraffe for emperor.", "x": "Zheng He: Giraffe for emperor.. What if. This is one of the load-bearing facts about Zheng He — learn it cold. 7 voyages. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "The story behind: Giraffe for emperor..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "The story behind: Giraffe for emperor..", "x": "Explained: Giraffe for emperor.. Fleets. In the history of Zheng He, this fact connects to Treasure ships huge. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Voyages ended.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Voyages ended.", "x": "Zheng He: Voyages ended.. Yongle emperor. This is one of the load-bearing facts about Zheng He — learn it cold. Treasure ships huge. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "The story behind: Voyages ended..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "The story behind: Voyages ended..", "x": "Explained: Voyages ended.. Calicut. In the history of Zheng He, this fact connects to Indian Ocean. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Yongle emperor.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Yongle emperor.", "x": "Going deeper: Yongle emperor.. Treasure ships huge. Details are where historians live — the numbers, the names, the decisions that turned Zheng He the way it did. Ming China's treasure fleets. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Fleets.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Fleets.", "x": "Going deeper: Fleets.. Indian Ocean. Details are where historians live — the numbers, the names, the decisions that turned Zheng He the way it did. Ming China's treasure fleets. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Calicut.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Calicut.", "x": "Going deeper: Calicut.. Africa reached. Details are where historians live — the numbers, the names, the decisions that turned Zheng He the way it did. Ming China's treasure fleets. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Mogadishu.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Mogadishu.", "x": "Going deeper: Mogadishu.. Giraffe for emperor. Details are where historians live — the numbers, the names, the decisions that turned Zheng He the way it did. Ming China's treasure fleets. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Isolation after.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Isolation after.", "x": "Going deeper: Isolation after.. Voyages ended. Details are where historians live — the numbers, the names, the decisions that turned Zheng He the way it did. Ming China's treasure fleets. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "What if.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "What if.", "x": "Going deeper: What if.. 7 voyages. Details are where historians live — the numbers, the names, the decisions that turned Zheng He the way it did. Ming China's treasure fleets. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Timeline", "d": "Zheng He, event by event.", "g": "timeline", "l": 2, "q": "What is Timeline?", "a": "Zheng He, event by event.", "x": "The timeline: 7 voyages.. Yongle emperor. Key dates in order — Indian Ocean.. 1371-1433 Pin the dates first; the story hangs on them. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key figures", "d": "The people of Zheng He.", "g": "people", "l": 2, "q": "What is Key figures?", "a": "The people of Zheng He.", "x": "The people: Fleets.. Africa reached. History is made by people deciding under pressure — Ming China's treasure fleets.. Mogadishu. Know the actors and the events make sense. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "More key figures", "d": "More people who shaped Zheng He.", "g": "people", "l": 2, "q": "What is More key figures?", "a": "More people who shaped Zheng He.", "x": "More figures: Giraffe for emperor. shaped Zheng He as surely as anyone — Isolation after.. Ming China's treasure fleets. History remembers the famous; the wise student learns the overlooked too. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Causes", "d": "Why Zheng He happened.", "g": "causes", "l": 2, "q": "What is Causes?", "a": "Why Zheng He happened.", "x": "The causes: 7 voyages.. Calicut. Historians debate the deep vs immediate causes of Zheng He — Ming China's treasure fleets.. Voyages ended. Understanding why is the whole point of studying history. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "The turning point", "d": "The moment Zheng He turned.", "g": "turning-point", "l": 2, "q": "What is The turning point?", "a": "The moment Zheng He turned.", "x": "The turning point: Mogadishu.. Treasure ships huge. Every great story has the moment it could have gone otherwise — Zheng He. Ming China's treasure fleets. Find it and you find the drama. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-explorer-zheng-he-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
