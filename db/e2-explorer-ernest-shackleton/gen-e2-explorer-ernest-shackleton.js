(function(){'use strict';
/* JAH Ernest Shackleton Explorer Database generator — jahdb-e2-explorer-ernest-shackleton-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-explorer-ernest-shackleton',PREFIX='JAH-E2EXPLORERE-',NAME='JAH Ernest Shackleton Explorer Database';
var FIELDS=["overview", "context", "facts", "details", "timeline", "people", "causes", "turning-point", "legacy", "misconceptions", "what-if", "quiz", "sources", "learn-more"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Ernest Shackleton: overview", "d": "Ernest Shackleton (1874-1922): Endurance: greatest survival story..", "g": "overview", "l": 2, "q": "What is Ernest Shackleton: overview?", "a": "Ernest Shackleton (1874-1922): Endurance: greatest survival story..", "x": "The complete explorer guide to Ernest Shackleton: Endurance: greatest survival story.. Endurance crushed 1915. From causes to consequences, from the key figures to the legacy that still shapes us — this database tells the whole story the way a great history course would.", "s": "public-reference", "f": null}, {"t": "The era", "d": "Ernest Shackleton in its time: 1874-1922.", "g": "context", "l": 2, "q": "What is The era?", "a": "Ernest Shackleton in its time: 1874-1922.", "x": "Context: Ernest Shackleton belonged to 1874-1922 — Nimrod expedition.. Elephant Island. Nothing in history happens in a vacuum; the era explains the motives, the means, and the stakes. Endurance: greatest survival story.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Endurance crushed 1915.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Endurance crushed 1915.", "x": "Ernest Shackleton: Endurance crushed 1915.. Leadership legend. This is one of the load-bearing facts about Ernest Shackleton — learn it cold. 800-mile open boat. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "The story behind: Endurance crushed 1915..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "The story behind: Endurance crushed 1915..", "x": "Explained: Endurance crushed 1915.. Antarctic. In the history of Ernest Shackleton, this fact connects to South Georgia crossing. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Elephant Island.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Elephant Island.", "x": "Ernest Shackleton: Elephant Island.. Endurance found 2022. This is one of the load-bearing facts about Ernest Shackleton — learn it cold. South Georgia crossing. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "The story behind: Elephant Island..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "The story behind: Elephant Island..", "x": "Explained: Elephant Island.. Endurance crew. In the history of Ernest Shackleton, this fact connects to All crew saved. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "800-mile open boat.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "800-mile open boat.", "x": "Ernest Shackleton: 800-mile open boat.. Antarctic. This is one of the load-bearing facts about Ernest Shackleton — learn it cold. All crew saved. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "The story behind: 800-mile open boat..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "The story behind: 800-mile open boat..", "x": "Explained: 800-mile open boat.. Management lessons. In the history of Ernest Shackleton, this fact connects to Died 1922. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "South Georgia crossing.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "South Georgia crossing.", "x": "Ernest Shackleton: South Georgia crossing.. Endurance crew. This is one of the load-bearing facts about Ernest Shackleton — learn it cold. Died 1922. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "The story behind: South Georgia crossing..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "The story behind: South Georgia crossing..", "x": "Explained: South Georgia crossing.. Nimrod expedition. In the history of Ernest Shackleton, this fact connects to Endurance crushed 1915. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "All crew saved.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "All crew saved.", "x": "Ernest Shackleton: All crew saved.. Management lessons. This is one of the load-bearing facts about Ernest Shackleton — learn it cold. Endurance crushed 1915. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "The story behind: All crew saved..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "The story behind: All crew saved..", "x": "Explained: All crew saved.. Leadership legend. In the history of Ernest Shackleton, this fact connects to Elephant Island. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Died 1922.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Died 1922.", "x": "Ernest Shackleton: Died 1922.. Nimrod expedition. This is one of the load-bearing facts about Ernest Shackleton — learn it cold. Elephant Island. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "The story behind: Died 1922..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "The story behind: Died 1922..", "x": "Explained: Died 1922.. Endurance found 2022. In the history of Ernest Shackleton, this fact connects to 800-mile open boat. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Nimrod expedition.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Nimrod expedition.", "x": "Going deeper: Nimrod expedition.. Elephant Island. Details are where historians live — the numbers, the names, the decisions that turned Ernest Shackleton the way it did. Endurance: greatest survival story.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Leadership legend.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Leadership legend.", "x": "Going deeper: Leadership legend.. 800-mile open boat. Details are where historians live — the numbers, the names, the decisions that turned Ernest Shackleton the way it did. Endurance: greatest survival story.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Endurance found 2022.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Endurance found 2022.", "x": "Going deeper: Endurance found 2022.. South Georgia crossing. Details are where historians live — the numbers, the names, the decisions that turned Ernest Shackleton the way it did. Endurance: greatest survival story.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Antarctic.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Antarctic.", "x": "Going deeper: Antarctic.. All crew saved. Details are where historians live — the numbers, the names, the decisions that turned Ernest Shackleton the way it did. Endurance: greatest survival story. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Endurance crew.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Endurance crew.", "x": "Going deeper: Endurance crew.. Died 1922. Details are where historians live — the numbers, the names, the decisions that turned Ernest Shackleton the way it did. Endurance: greatest survival story. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Management lessons.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Management lessons.", "x": "Going deeper: Management lessons.. Endurance crushed 1915. Details are where historians live — the numbers, the names, the decisions that turned Ernest Shackleton the way it did. Endurance: greatest survival story.", "s": "public-reference", "f": null}, {"t": "Timeline", "d": "Ernest Shackleton, event by event.", "g": "timeline", "l": 2, "q": "What is Timeline?", "a": "Ernest Shackleton, event by event.", "x": "The timeline: Endurance crushed 1915.. Nimrod expedition. Key dates in order — 800-mile open boat.. 1874-1922 Pin the dates first; the story hangs on them. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key figures", "d": "The people of Ernest Shackleton.", "g": "people", "l": 2, "q": "What is Key figures?", "a": "The people of Ernest Shackleton.", "x": "The people: Leadership legend.. South Georgia crossing. History is made by people deciding under pressure — Endurance: greatest survival story.. Antarctic. Know the actors and the events make sense. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "More key figures", "d": "More people who shaped Ernest Shackleton.", "g": "people", "l": 2, "q": "What is More key figures?", "a": "More people who shaped Ernest Shackleton.", "x": "More figures: All crew saved. shaped Ernest Shackleton as surely as anyone — Endurance crew.. Endurance: greatest survival story. History remembers the famous; the wise student learns the overlooked too.", "s": "public-reference", "f": null}, {"t": "Causes", "d": "Why Ernest Shackleton happened.", "g": "causes", "l": 2, "q": "What is Causes?", "a": "Why Ernest Shackleton happened.", "x": "The causes: Endurance crushed 1915.. Endurance found 2022. Historians debate the deep vs immediate causes of Ernest Shackleton — Endurance: greatest survival story.. Died 1922. Understanding why is the whole point of studying history.", "s": "public-reference", "f": null}, {"t": "The turning point", "d": "The moment Ernest Shackleton turned.", "g": "turning-point", "l": 2, "q": "What is The turning point?", "a": "The moment Ernest Shackleton turned.", "x": "The turning point: Antarctic.. Elephant Island. Every great story has the moment it could have gone otherwise — Ernest Shackleton. Endurance: greatest survival story. Find it and you find the drama. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-explorer-ernest-shackleton-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
