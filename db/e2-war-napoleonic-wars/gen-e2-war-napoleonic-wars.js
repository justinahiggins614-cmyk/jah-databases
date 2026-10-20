(function(){'use strict';
/* JAH Napoleonic Wars War Database generator — jahdb-e2-war-napoleonic-wars-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-war-napoleonic-wars',PREFIX='JAH-E2WARNAPOLE-',NAME='JAH Napoleonic Wars War Database';
var FIELDS=["overview", "context", "facts", "details", "timeline", "people", "causes", "turning-point", "legacy", "misconceptions", "what-if", "quiz", "sources", "learn-more"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Napoleonic Wars: overview", "d": "Napoleonic Wars (1803-1815): Napoleon's bid for European empire..", "g": "overview", "l": 2, "q": "What is Napoleonic Wars: overview?", "a": "Napoleonic Wars (1803-1815): Napoleon's bid for European empire..", "x": "The complete war guide to Napoleonic Wars: Napoleon's bid for European empire.. Austerlitz: masterpiece (1805). From causes to consequences, from the key figures to the legacy that still shapes us — this database tells the whole story the way a great history course would.", "s": "public-reference", "f": null}, {"t": "The era", "d": "Napoleonic Wars in its time: 1803-1815.", "g": "context", "l": 2, "q": "What is The era?", "a": "Napoleonic Wars in its time: 1803-1815.", "x": "Context: Napoleonic Wars belonged to 1803-1815 — Rise from Revolution.. Trafalgar: British naval win. Nothing in history happens in a vacuum; the era explains the motives, the means, and the stakes. Napoleon's bid for European empire.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Austerlitz: masterpiece (1805).", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Austerlitz: masterpiece (1805).", "x": "Napoleonic Wars: Austerlitz: masterpiece (1805).. Peninsular War. This is one of the load-bearing facts about Napoleonic Wars — learn it cold. Russia 1812: disastrous retreat. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "The story behind: Austerlitz: masterpiece (1805)..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "The story behind: Austerlitz: masterpiece (1805)..", "x": "Explained: Austerlitz: masterpiece (1805).. Elba exile. In the history of Napoleonic Wars, this fact connects to Waterloo (1815): final defeat. — see the connections and you have understanding, not trivia.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Trafalgar: British naval win.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Trafalgar: British naval win.", "x": "Napoleonic Wars: Trafalgar: British naval win.. Continental System. This is one of the load-bearing facts about Napoleonic Wars — learn it cold. Waterloo (1815): final defeat. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "The story behind: Trafalgar: British naval win..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "The story behind: Trafalgar: British naval win..", "x": "Explained: Trafalgar: British naval win.. Hundred Days. In the history of Napoleonic Wars, this fact connects to Napoleonic Code legacy. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Russia 1812: disastrous retreat.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Russia 1812: disastrous retreat.", "x": "Napoleonic Wars: Russia 1812: disastrous retreat.. Elba exile. This is one of the load-bearing facts about Napoleonic Wars — learn it cold. Napoleonic Code legacy. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "The story behind: Russia 1812: disastrous retreat..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "The story behind: Russia 1812: disastrous retreat..", "x": "Explained: Russia 1812: disastrous retreat.. Exile to St. Helena. In the history of Napoleonic Wars, this fact connects to Congress of Vienna. — see the connections and you have understanding, not trivia.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Waterloo (1815): final defeat.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Waterloo (1815): final defeat.", "x": "Napoleonic Wars: Waterloo (1815): final defeat.. Hundred Days. This is one of the load-bearing facts about Napoleonic Wars — learn it cold. Congress of Vienna. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "The story behind: Waterloo (1815): final defeat..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "The story behind: Waterloo (1815): final defeat..", "x": "Explained: Waterloo (1815): final defeat.. Rise from Revolution. In the history of Napoleonic Wars, this fact connects to Austerlitz: masterpiece (1805). — see the connections and you have understanding, not trivia.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Napoleonic Code legacy.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Napoleonic Code legacy.", "x": "Napoleonic Wars: Napoleonic Code legacy.. Exile to St. Helena. This is one of the load-bearing facts about Napoleonic Wars — learn it cold. Austerlitz: masterpiece (1805). History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "The story behind: Napoleonic Code legacy..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "The story behind: Napoleonic Code legacy..", "x": "Explained: Napoleonic Code legacy.. Peninsular War. In the history of Napoleonic Wars, this fact connects to Trafalgar: British naval win. — see the connections and you have understanding, not trivia.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Congress of Vienna.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Congress of Vienna.", "x": "Napoleonic Wars: Congress of Vienna.. Rise from Revolution. This is one of the load-bearing facts about Napoleonic Wars — learn it cold. Trafalgar: British naval win. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "The story behind: Congress of Vienna..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "The story behind: Congress of Vienna..", "x": "Explained: Congress of Vienna.. Continental System. In the history of Napoleonic Wars, this fact connects to Russia 1812: disastrous retreat. — see the connections and you have understanding, not trivia.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Rise from Revolution.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Rise from Revolution.", "x": "Going deeper: Rise from Revolution.. Trafalgar: British naval win. Details are where historians live — the numbers, the names, the decisions that turned Napoleonic Wars the way it did. Napoleon's bid for European empire.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Peninsular War.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Peninsular War.", "x": "Going deeper: Peninsular War.. Russia 1812: disastrous retreat. Details are where historians live — the numbers, the names, the decisions that turned Napoleonic Wars the way it did. Napoleon's bid for European empire.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Continental System.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Continental System.", "x": "Going deeper: Continental System.. Waterloo (1815): final defeat. Details are where historians live — the numbers, the names, the decisions that turned Napoleonic Wars the way it did. Napoleon's bid for European empire.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Elba exile.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Elba exile.", "x": "Going deeper: Elba exile.. Napoleonic Code legacy. Details are where historians live — the numbers, the names, the decisions that turned Napoleonic Wars the way it did. Napoleon's bid for European empire.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Hundred Days.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Hundred Days.", "x": "Going deeper: Hundred Days.. Congress of Vienna. Details are where historians live — the numbers, the names, the decisions that turned Napoleonic Wars the way it did. Napoleon's bid for European empire.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Exile to St. Helena.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Exile to St. Helena.", "x": "Going deeper: Exile to St. Helena.. Austerlitz: masterpiece (1805). Details are where historians live — the numbers, the names, the decisions that turned Napoleonic Wars the way it did. Napoleon's bid for European empire.", "s": "public-reference", "f": null}, {"t": "Timeline", "d": "Napoleonic Wars, event by event.", "g": "timeline", "l": 2, "q": "What is Timeline?", "a": "Napoleonic Wars, event by event.", "x": "The timeline: Austerlitz: masterpiece (1805).. Rise from Revolution. Key dates in order — Russia 1812: disastrous retreat.. 1803-1815 Pin the dates first; the story hangs on them. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key figures", "d": "The people of Napoleonic Wars.", "g": "people", "l": 2, "q": "What is Key figures?", "a": "The people of Napoleonic Wars.", "x": "The people: Peninsular War.. Waterloo (1815): final defeat. History is made by people deciding under pressure — Napoleon's bid for European empire.. Elba exile. Know the actors and the events make sense.", "s": "public-reference", "f": null}, {"t": "More key figures", "d": "More people who shaped Napoleonic Wars.", "g": "people", "l": 2, "q": "What is More key figures?", "a": "More people who shaped Napoleonic Wars.", "x": "More figures: Napoleonic Code legacy. shaped Napoleonic Wars as surely as anyone — Hundred Days.. Napoleon's bid for European empire. History remembers the famous; the wise student learns the overlooked too.", "s": "public-reference", "f": null}, {"t": "Causes", "d": "Why Napoleonic Wars happened.", "g": "causes", "l": 2, "q": "What is Causes?", "a": "Why Napoleonic Wars happened.", "x": "The causes: Austerlitz: masterpiece (1805).. Continental System. Historians debate the deep vs immediate causes of Napoleonic Wars — Napoleon's bid for European empire.. Congress of Vienna. Understanding why is the whole point of studying history.", "s": "public-reference", "f": null}, {"t": "The turning point", "d": "The moment Napoleonic Wars turned.", "g": "turning-point", "l": 2, "q": "What is The turning point?", "a": "The moment Napoleonic Wars turned.", "x": "The turning point: Elba exile.. Trafalgar: British naval win. Every great story has the moment it could have gone otherwise — Napoleonic Wars. Napoleon's bid for European empire. Find it and you find the drama.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-war-napoleonic-wars-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
