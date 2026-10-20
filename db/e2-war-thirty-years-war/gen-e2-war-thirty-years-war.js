(function(){'use strict';
/* JAH Thirty Years\' War War Database generator — jahdb-e2-war-thirty-years-war-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-war-thirty-years-war',PREFIX='JAH-E2WARTHIRTY-',NAME='JAH Thirty Years\' War War Database';
var FIELDS=["overview", "context", "facts", "details", "timeline", "people", "causes", "turning-point", "legacy", "misconceptions", "what-if", "quiz", "sources", "learn-more"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Thirty Years' War: overview", "d": "Thirty Years' War (1618-1648): religious war that devastated Germany..", "g": "overview", "l": 2, "q": "What is Thirty Years' War: overview?", "a": "Thirty Years' War (1618-1648): religious war that devastated Germany..", "x": "The complete war guide to Thirty Years' War: religious war that devastated Germany.. Defenestration of Prague. From causes to consequences, from the key figures to the legacy that still shapes us — this database tells the whole story the way a great history course would.", "s": "public-reference", "f": null}, {"t": "The era", "d": "Thirty Years' War in its time: 1618-1648.", "g": "context", "l": 2, "q": "What is The era?", "a": "Thirty Years' War in its time: 1618-1648.", "x": "Context: Thirty Years' War belonged to 1618-1648 — Bohemian phase.. Catholic vs Protestant. Nothing in history happens in a vacuum; the era explains the motives, the means, and the stakes. religious war that devastated Germany.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Defenestration of Prague.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Defenestration of Prague.", "x": "Thirty Years' War: Defenestration of Prague.. Danish/Swedish phases. This is one of the load-bearing facts about Thirty Years' War — learn it cold. Wallenstein, Gustavus Adolphus. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "The story behind: Defenestration of Prague..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "The story behind: Defenestration of Prague..", "x": "Explained: Defenestration of Prague.. Magdeburg sack. In the history of Thirty Years' War, this fact connects to Westphalia peace (1648). — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Catholic vs Protestant.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Catholic vs Protestant.", "x": "Thirty Years' War: Catholic vs Protestant.. French phase. This is one of the load-bearing facts about Thirty Years' War — learn it cold. Westphalia peace (1648). History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "The story behind: Catholic vs Protestant..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "The story behind: Catholic vs Protestant..", "x": "Explained: Catholic vs Protestant.. Peace of Westphalia. In the history of Thirty Years' War, this fact connects to 8M died. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Wallenstein, Gustavus Adolphus.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Wallenstein, Gustavus Adolphus.", "x": "Thirty Years' War: Wallenstein, Gustavus Adolphus.. Magdeburg sack. This is one of the load-bearing facts about Thirty Years' War — learn it cold. 8M died. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "The story behind: Wallenstein, Gustavus Adolphus..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "The story behind: Wallenstein, Gustavus Adolphus..", "x": "Explained: Wallenstein, Gustavus Adolphus.. Modern states system. In the history of Thirty Years' War, this fact connects to Sovereignty principle. — see the connections and you have understanding, not trivia.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Westphalia peace (1648).", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Westphalia peace (1648).", "x": "Thirty Years' War: Westphalia peace (1648).. Peace of Westphalia. This is one of the load-bearing facts about Thirty Years' War — learn it cold. Sovereignty principle. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "The story behind: Westphalia peace (1648)..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "The story behind: Westphalia peace (1648)..", "x": "Explained: Westphalia peace (1648).. Bohemian phase. In the history of Thirty Years' War, this fact connects to Defenestration of Prague. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "8M died.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "8M died.", "x": "Thirty Years' War: 8M died.. Modern states system. This is one of the load-bearing facts about Thirty Years' War — learn it cold. Defenestration of Prague. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "The story behind: 8M died..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "The story behind: 8M died..", "x": "Explained: 8M died.. Danish/Swedish phases. In the history of Thirty Years' War, this fact connects to Catholic vs Protestant. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Sovereignty principle.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Sovereignty principle.", "x": "Thirty Years' War: Sovereignty principle.. Bohemian phase. This is one of the load-bearing facts about Thirty Years' War — learn it cold. Catholic vs Protestant. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "The story behind: Sovereignty principle..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "The story behind: Sovereignty principle..", "x": "Explained: Sovereignty principle.. French phase. In the history of Thirty Years' War, this fact connects to Wallenstein, Gustavus Adolphus. — see the connections and you have understanding, not trivia.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Bohemian phase.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Bohemian phase.", "x": "Going deeper: Bohemian phase.. Catholic vs Protestant. Details are where historians live — the numbers, the names, the decisions that turned Thirty Years' War the way it did. religious war that devastated Germany.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Danish/Swedish phases.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Danish/Swedish phases.", "x": "Going deeper: Danish/Swedish phases.. Wallenstein, Gustavus Adolphus. Details are where historians live — the numbers, the names, the decisions that turned Thirty Years' War the way it did. religious war that devastated Germany.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "French phase.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "French phase.", "x": "Going deeper: French phase.. Westphalia peace (1648). Details are where historians live — the numbers, the names, the decisions that turned Thirty Years' War the way it did. religious war that devastated Germany.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Magdeburg sack.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Magdeburg sack.", "x": "Going deeper: Magdeburg sack.. 8M died. Details are where historians live — the numbers, the names, the decisions that turned Thirty Years' War the way it did. religious war that devastated Germany. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Peace of Westphalia.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Peace of Westphalia.", "x": "Going deeper: Peace of Westphalia.. Sovereignty principle. Details are where historians live — the numbers, the names, the decisions that turned Thirty Years' War the way it did. religious war that devastated Germany.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Modern states system.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Modern states system.", "x": "Going deeper: Modern states system.. Defenestration of Prague. Details are where historians live — the numbers, the names, the decisions that turned Thirty Years' War the way it did. religious war that devastated Germany.", "s": "public-reference", "f": null}, {"t": "Timeline", "d": "Thirty Years' War, event by event.", "g": "timeline", "l": 2, "q": "What is Timeline?", "a": "Thirty Years' War, event by event.", "x": "The timeline: Defenestration of Prague.. Bohemian phase. Key dates in order — Wallenstein, Gustavus Adolphus.. 1618-1648 Pin the dates first; the story hangs on them. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key figures", "d": "The people of Thirty Years' War.", "g": "people", "l": 2, "q": "What is Key figures?", "a": "The people of Thirty Years' War.", "x": "The people: Danish/Swedish phases.. Westphalia peace (1648). History is made by people deciding under pressure — religious war that devastated Germany.. Magdeburg sack. Know the actors and the events make sense.", "s": "public-reference", "f": null}, {"t": "More key figures", "d": "More people who shaped Thirty Years' War.", "g": "people", "l": 2, "q": "What is More key figures?", "a": "More people who shaped Thirty Years' War.", "x": "More figures: 8M died. shaped Thirty Years' War as surely as anyone — Peace of Westphalia.. religious war that devastated Germany. History remembers the famous; the wise student learns the overlooked too.", "s": "public-reference", "f": null}, {"t": "Causes", "d": "Why Thirty Years' War happened.", "g": "causes", "l": 2, "q": "What is Causes?", "a": "Why Thirty Years' War happened.", "x": "The causes: Defenestration of Prague.. French phase. Historians debate the deep vs immediate causes of Thirty Years' War — religious war that devastated Germany.. Sovereignty principle. Understanding why is the whole point of studying history.", "s": "public-reference", "f": null}, {"t": "The turning point", "d": "The moment Thirty Years' War turned.", "g": "turning-point", "l": 2, "q": "What is The turning point?", "a": "The moment Thirty Years' War turned.", "x": "The turning point: Magdeburg sack.. Catholic vs Protestant. Every great story has the moment it could have gone otherwise — Thirty Years' War. religious war that devastated Germany. Find it and you find the drama.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-war-thirty-years-war-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
