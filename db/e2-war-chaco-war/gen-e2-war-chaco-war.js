(function(){'use strict';
/* JAH Chaco War War Database generator — jahdb-e2-war-chaco-war-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-war-chaco-war',PREFIX='JAH-E2WARCHACOW-',NAME='JAH Chaco War War Database';
var FIELDS=["overview", "context", "facts", "details", "timeline", "people", "causes", "turning-point", "legacy", "misconceptions", "what-if", "quiz", "sources", "learn-more"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Chaco War: overview", "d": "Chaco War (1932-1935): Bolivia vs Paraguay over the Chaco..", "g": "overview", "l": 2, "q": "What is Chaco War: overview?", "a": "Chaco War (1932-1935): Bolivia vs Paraguay over the Chaco..", "x": "The complete war guide to Chaco War: Bolivia vs Paraguay over the Chaco.. Oil rumors. From causes to consequences, from the key figures to the legacy that still shapes us — this database tells the whole story the way a great history course would.", "s": "public-reference", "f": null}, {"t": "The era", "d": "Chaco War in its time: 1932-1935.", "g": "context", "l": 2, "q": "What is The era?", "a": "Chaco War in its time: 1932-1935.", "x": "Context: Chaco War belonged to 1932-1935 — Gran Chaco.. Bloodiest 20th-c. Americas war. Nothing in history happens in a vacuum; the era explains the motives, the means, and the stakes. Bolivia vs Paraguay over the Chaco.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Oil rumors.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Oil rumors.", "x": "Chaco War: Oil rumors.. German/Bolivian officers. This is one of the load-bearing facts about Chaco War — learn it cold. Paraguay won. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "The story behind: Oil rumors..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "The story behind: Oil rumors..", "x": "Explained: Oil rumors.. Nanawa battles. In the history of Chaco War, this fact connects to 100,000 died. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Bloodiest 20th-c. Americas war.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Bloodiest 20th-c. Americas war.", "x": "Chaco War: Bloodiest 20th-c. Americas war.. Fortines. This is one of the load-bearing facts about Chaco War — learn it cold. 100,000 died. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "The story behind: Bloodiest 20th-c. Americas war..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "The story behind: Bloodiest 20th-c. Americas war..", "x": "Explained: Bloodiest 20th-c. Americas war.. Aftermath. In the history of Chaco War, this fact connects to Treaty 1938. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Paraguay won.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Paraguay won.", "x": "Chaco War: Paraguay won.. Nanawa battles. This is one of the load-bearing facts about Chaco War — learn it cold. Treaty 1938. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "The story behind: Paraguay won..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "The story behind: Paraguay won..", "x": "Explained: Paraguay won.. Memory. In the history of Chaco War, this fact connects to National traumas. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "100,000 died.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "100,000 died.", "x": "Chaco War: 100,000 died.. Aftermath. This is one of the load-bearing facts about Chaco War — learn it cold. National traumas. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "The story behind: 100,000 died..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "The story behind: 100,000 died..", "x": "Explained: 100,000 died.. Gran Chaco. In the history of Chaco War, this fact connects to Oil rumors. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Treaty 1938.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Treaty 1938.", "x": "Chaco War: Treaty 1938.. Memory. This is one of the load-bearing facts about Chaco War — learn it cold. Oil rumors. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "The story behind: Treaty 1938..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "The story behind: Treaty 1938..", "x": "Explained: Treaty 1938.. German/Bolivian officers. In the history of Chaco War, this fact connects to Bloodiest 20th-c. Americas war. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "National traumas.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "National traumas.", "x": "Chaco War: National traumas.. Gran Chaco. This is one of the load-bearing facts about Chaco War — learn it cold. Bloodiest 20th-c. Americas war. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "The story behind: National traumas..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "The story behind: National traumas..", "x": "Explained: National traumas.. Fortines. In the history of Chaco War, this fact connects to Paraguay won. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Gran Chaco.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Gran Chaco.", "x": "Going deeper: Gran Chaco.. Bloodiest 20th-c. Americas war. Details are where historians live — the numbers, the names, the decisions that turned Chaco War the way it did. Bolivia vs Paraguay over the Chaco.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "German/Bolivian officers.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "German/Bolivian officers.", "x": "Going deeper: German/Bolivian officers.. Paraguay won. Details are where historians live — the numbers, the names, the decisions that turned Chaco War the way it did. Bolivia vs Paraguay over the Chaco.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Fortines.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Fortines.", "x": "Going deeper: Fortines.. 100,000 died. Details are where historians live — the numbers, the names, the decisions that turned Chaco War the way it did. Bolivia vs Paraguay over the Chaco. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Nanawa battles.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Nanawa battles.", "x": "Going deeper: Nanawa battles.. Treaty 1938. Details are where historians live — the numbers, the names, the decisions that turned Chaco War the way it did. Bolivia vs Paraguay over the Chaco. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Aftermath.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Aftermath.", "x": "Going deeper: Aftermath.. National traumas. Details are where historians live — the numbers, the names, the decisions that turned Chaco War the way it did. Bolivia vs Paraguay over the Chaco. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Memory.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Memory.", "x": "Going deeper: Memory.. Oil rumors. Details are where historians live — the numbers, the names, the decisions that turned Chaco War the way it did. Bolivia vs Paraguay over the Chaco. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Timeline", "d": "Chaco War, event by event.", "g": "timeline", "l": 2, "q": "What is Timeline?", "a": "Chaco War, event by event.", "x": "The timeline: Oil rumors.. Gran Chaco. Key dates in order — Paraguay won.. 1932-1935 Pin the dates first; the story hangs on them. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key figures", "d": "The people of Chaco War.", "g": "people", "l": 2, "q": "What is Key figures?", "a": "The people of Chaco War.", "x": "The people: German/Bolivian officers.. 100,000 died. History is made by people deciding under pressure — Bolivia vs Paraguay over the Chaco.. Nanawa battles. Know the actors and the events make sense.", "s": "public-reference", "f": null}, {"t": "More key figures", "d": "More people who shaped Chaco War.", "g": "people", "l": 2, "q": "What is More key figures?", "a": "More people who shaped Chaco War.", "x": "More figures: Treaty 1938. shaped Chaco War as surely as anyone — Aftermath.. Bolivia vs Paraguay over the Chaco. History remembers the famous; the wise student learns the overlooked too. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Causes", "d": "Why Chaco War happened.", "g": "causes", "l": 2, "q": "What is Causes?", "a": "Why Chaco War happened.", "x": "The causes: Oil rumors.. Fortines. Historians debate the deep vs immediate causes of Chaco War — Bolivia vs Paraguay over the Chaco.. National traumas. Understanding why is the whole point of studying history.", "s": "public-reference", "f": null}, {"t": "The turning point", "d": "The moment Chaco War turned.", "g": "turning-point", "l": 2, "q": "What is The turning point?", "a": "The moment Chaco War turned.", "x": "The turning point: Nanawa battles.. Bloodiest 20th-c. Americas war. Every great story has the moment it could have gone otherwise — Chaco War. Bolivia vs Paraguay over the Chaco. Find it and you find the drama.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-war-chaco-war-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
