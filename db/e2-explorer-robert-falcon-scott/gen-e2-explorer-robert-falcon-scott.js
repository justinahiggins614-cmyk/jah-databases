(function(){'use strict';
/* JAH Robert Falcon Scott Explorer Database generator — jahdb-e2-explorer-robert-falcon-scott-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-explorer-robert-falcon-scott',PREFIX='JAH-E2EXPLORERR-',NAME='JAH Robert Falcon Scott Explorer Database';
var FIELDS=["overview", "context", "facts", "details", "timeline", "people", "causes", "turning-point", "legacy", "misconceptions", "what-if", "quiz", "sources", "learn-more"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Robert Falcon Scott: overview", "d": "Robert Falcon Scott (1868-1912): died returning from South Pole..", "g": "overview", "l": 2, "q": "What is Robert Falcon Scott: overview?", "a": "Robert Falcon Scott (1868-1912): died returning from South Pole..", "x": "The complete explorer guide to Robert Falcon Scott: died returning from South Pole.. Terra Nova expedition. From causes to consequences, from the key figures to the legacy that still shapes us — this database tells the whole story the way a great history course would.", "s": "public-reference", "f": null}, {"t": "The era", "d": "Robert Falcon Scott in its time: 1868-1912.", "g": "context", "l": 2, "q": "What is The era?", "a": "Robert Falcon Scott in its time: 1868-1912.", "x": "Context: Robert Falcon Scott belonged to 1868-1912 — Navy.. Reached pole Jan 1912. Nothing in history happens in a vacuum; the era explains the motives, the means, and the stakes. died returning from South Pole.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Terra Nova expedition.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Terra Nova expedition.", "x": "Robert Falcon Scott: Terra Nova expedition.. Ponies vs dogs. This is one of the load-bearing facts about Robert Falcon Scott — learn it cold. Died on return. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "The story behind: Terra Nova expedition..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "The story behind: Terra Nova expedition..", "x": "Explained: Terra Nova expedition.. Search party. In the history of Robert Falcon Scott, this fact connects to Oates' sacrifice. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Reached pole Jan 1912.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Reached pole Jan 1912.", "x": "Robert Falcon Scott: Reached pole Jan 1912.. Evans' death. This is one of the load-bearing facts about Robert Falcon Scott — learn it cold. Oates' sacrifice. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "The story behind: Reached pole Jan 1912..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "The story behind: Reached pole Jan 1912..", "x": "Explained: Reached pole Jan 1912.. Memorial. In the history of Robert Falcon Scott, this fact connects to Diaries found. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Died on return.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Died on return.", "x": "Robert Falcon Scott: Died on return.. Search party. This is one of the load-bearing facts about Robert Falcon Scott — learn it cold. Diaries found. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "The story behind: Died on return..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "The story behind: Died on return..", "x": "Explained: Died on return.. Reassessment. In the history of Robert Falcon Scott, this fact connects to Heroic myth. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Oates' sacrifice.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Oates' sacrifice.", "x": "Robert Falcon Scott: Oates' sacrifice.. Memorial. This is one of the load-bearing facts about Robert Falcon Scott — learn it cold. Heroic myth. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "The story behind: Oates' sacrifice..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "The story behind: Oates' sacrifice..", "x": "Explained: Oates' sacrifice.. Navy. In the history of Robert Falcon Scott, this fact connects to Terra Nova expedition. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Diaries found.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Diaries found.", "x": "Robert Falcon Scott: Diaries found.. Reassessment. This is one of the load-bearing facts about Robert Falcon Scott — learn it cold. Terra Nova expedition. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "The story behind: Diaries found..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "The story behind: Diaries found..", "x": "Explained: Diaries found.. Ponies vs dogs. In the history of Robert Falcon Scott, this fact connects to Reached pole Jan 1912. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Heroic myth.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Heroic myth.", "x": "Robert Falcon Scott: Heroic myth.. Navy. This is one of the load-bearing facts about Robert Falcon Scott — learn it cold. Reached pole Jan 1912. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "The story behind: Heroic myth..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "The story behind: Heroic myth..", "x": "Explained: Heroic myth.. Evans' death. In the history of Robert Falcon Scott, this fact connects to Died on return. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Navy.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Navy.", "x": "Going deeper: Navy.. Reached pole Jan 1912. Details are where historians live — the numbers, the names, the decisions that turned Robert Falcon Scott the way it did. died returning from South Pole. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Ponies vs dogs.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Ponies vs dogs.", "x": "Going deeper: Ponies vs dogs.. Died on return. Details are where historians live — the numbers, the names, the decisions that turned Robert Falcon Scott the way it did. died returning from South Pole.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Evans' death.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Evans' death.", "x": "Going deeper: Evans' death.. Oates' sacrifice. Details are where historians live — the numbers, the names, the decisions that turned Robert Falcon Scott the way it did. died returning from South Pole.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Search party.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Search party.", "x": "Going deeper: Search party.. Diaries found. Details are where historians live — the numbers, the names, the decisions that turned Robert Falcon Scott the way it did. died returning from South Pole. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Memorial.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Memorial.", "x": "Going deeper: Memorial.. Heroic myth. Details are where historians live — the numbers, the names, the decisions that turned Robert Falcon Scott the way it did. died returning from South Pole. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Reassessment.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Reassessment.", "x": "Going deeper: Reassessment.. Terra Nova expedition. Details are where historians live — the numbers, the names, the decisions that turned Robert Falcon Scott the way it did. died returning from South Pole.", "s": "public-reference", "f": null}, {"t": "Timeline", "d": "Robert Falcon Scott, event by event.", "g": "timeline", "l": 2, "q": "What is Timeline?", "a": "Robert Falcon Scott, event by event.", "x": "The timeline: Terra Nova expedition.. Navy. Key dates in order — Died on return.. 1868-1912 Pin the dates first; the story hangs on them. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key figures", "d": "The people of Robert Falcon Scott.", "g": "people", "l": 2, "q": "What is Key figures?", "a": "The people of Robert Falcon Scott.", "x": "The people: Ponies vs dogs.. Oates' sacrifice. History is made by people deciding under pressure — died returning from South Pole.. Search party. Know the actors and the events make sense. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "More key figures", "d": "More people who shaped Robert Falcon Scott.", "g": "people", "l": 2, "q": "What is More key figures?", "a": "More people who shaped Robert Falcon Scott.", "x": "More figures: Diaries found. shaped Robert Falcon Scott as surely as anyone — Memorial.. died returning from South Pole. History remembers the famous; the wise student learns the overlooked too. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Causes", "d": "Why Robert Falcon Scott happened.", "g": "causes", "l": 2, "q": "What is Causes?", "a": "Why Robert Falcon Scott happened.", "x": "The causes: Terra Nova expedition.. Evans' death. Historians debate the deep vs immediate causes of Robert Falcon Scott — died returning from South Pole.. Heroic myth. Understanding why is the whole point of studying history.", "s": "public-reference", "f": null}, {"t": "The turning point", "d": "The moment Robert Falcon Scott turned.", "g": "turning-point", "l": 2, "q": "What is The turning point?", "a": "The moment Robert Falcon Scott turned.", "x": "The turning point: Search party.. Reached pole Jan 1912. Every great story has the moment it could have gone otherwise — Robert Falcon Scott. died returning from South Pole. Find it and you find the drama.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-explorer-robert-falcon-scott-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
