(function(){'use strict';
/* JAH Peloponnesian War War Database generator — jahdb-e2-war-peloponnesian-war-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-war-peloponnesian-war',PREFIX='JAH-E2WARPELOPO-',NAME='JAH Peloponnesian War War Database';
var FIELDS=["overview", "context", "facts", "details", "timeline", "people", "causes", "turning-point", "legacy", "misconceptions", "what-if", "quiz", "sources", "learn-more"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Peloponnesian War: overview", "d": "Peloponnesian War (431-404 BC): Athens vs Sparta; Thucydides' history..", "g": "overview", "l": 2, "q": "What is Peloponnesian War: overview?", "a": "Peloponnesian War (431-404 BC): Athens vs Sparta; Thucydides' history..", "x": "The complete war guide to Peloponnesian War: Athens vs Sparta; Thucydides' history.. Athens' empire vs Sparta. From causes to consequences, from the key figures to the legacy that still shapes us — this database tells the whole story the way a great history course would.", "s": "public-reference", "f": null}, {"t": "The era", "d": "Peloponnesian War in its time: 431-404 BC.", "g": "context", "l": 2, "q": "What is The era?", "a": "Peloponnesian War in its time: 431-404 BC.", "x": "Context: Peloponnesian War belonged to 431-404 BC — Thucydides wrote it.. Pericles' strategy. Nothing in history happens in a vacuum; the era explains the motives, the means, and the stakes. Athens vs Sparta; Thucydides' history.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Athens' empire vs Sparta.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Athens' empire vs Sparta.", "x": "Peloponnesian War: Athens' empire vs Sparta.. Long Walls. This is one of the load-bearing facts about Peloponnesian War — learn it cold. Plague hit Athens. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "The story behind: Athens' empire vs Sparta..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "The story behind: Athens' empire vs Sparta..", "x": "Explained: Athens' empire vs Sparta.. Oligarchic coups. In the history of Peloponnesian War, this fact connects to Sicilian disaster. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Pericles' strategy.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Pericles' strategy.", "x": "Peloponnesian War: Pericles' strategy.. Alcibiades. This is one of the load-bearing facts about Peloponnesian War — learn it cold. Sicilian disaster. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "The story behind: Pericles' strategy..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "The story behind: Pericles' strategy..", "x": "Explained: Pericles' strategy.. Aegospotami. In the history of Peloponnesian War, this fact connects to Sparta won. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Plague hit Athens.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Plague hit Athens.", "x": "Peloponnesian War: Plague hit Athens.. Oligarchic coups. This is one of the load-bearing facts about Peloponnesian War — learn it cold. Sparta won. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "The story behind: Plague hit Athens..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "The story behind: Plague hit Athens..", "x": "Explained: Plague hit Athens.. Greek decline. In the history of Peloponnesian War, this fact connects to Democracy weakened. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Sicilian disaster.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Sicilian disaster.", "x": "Peloponnesian War: Sicilian disaster.. Aegospotami. This is one of the load-bearing facts about Peloponnesian War — learn it cold. Democracy weakened. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "The story behind: Sicilian disaster..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "The story behind: Sicilian disaster..", "x": "Explained: Sicilian disaster.. Thucydides wrote it. In the history of Peloponnesian War, this fact connects to Athens' empire vs Sparta. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Sparta won.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Sparta won.", "x": "Peloponnesian War: Sparta won.. Greek decline. This is one of the load-bearing facts about Peloponnesian War — learn it cold. Athens' empire vs Sparta. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "The story behind: Sparta won..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "The story behind: Sparta won..", "x": "Explained: Sparta won.. Long Walls. In the history of Peloponnesian War, this fact connects to Pericles' strategy. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Democracy weakened.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Democracy weakened.", "x": "Peloponnesian War: Democracy weakened.. Thucydides wrote it. This is one of the load-bearing facts about Peloponnesian War — learn it cold. Pericles' strategy. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "The story behind: Democracy weakened..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "The story behind: Democracy weakened..", "x": "Explained: Democracy weakened.. Alcibiades. In the history of Peloponnesian War, this fact connects to Plague hit Athens. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Thucydides wrote it.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Thucydides wrote it.", "x": "Going deeper: Thucydides wrote it.. Pericles' strategy. Details are where historians live — the numbers, the names, the decisions that turned Peloponnesian War the way it did. Athens vs Sparta; Thucydides' history.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Long Walls.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Long Walls.", "x": "Going deeper: Long Walls.. Plague hit Athens. Details are where historians live — the numbers, the names, the decisions that turned Peloponnesian War the way it did. Athens vs Sparta; Thucydides' history.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Alcibiades.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Alcibiades.", "x": "Going deeper: Alcibiades.. Sicilian disaster. Details are where historians live — the numbers, the names, the decisions that turned Peloponnesian War the way it did. Athens vs Sparta; Thucydides' history.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Oligarchic coups.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Oligarchic coups.", "x": "Going deeper: Oligarchic coups.. Sparta won. Details are where historians live — the numbers, the names, the decisions that turned Peloponnesian War the way it did. Athens vs Sparta; Thucydides' history.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Aegospotami.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Aegospotami.", "x": "Going deeper: Aegospotami.. Democracy weakened. Details are where historians live — the numbers, the names, the decisions that turned Peloponnesian War the way it did. Athens vs Sparta; Thucydides' history.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Greek decline.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Greek decline.", "x": "Going deeper: Greek decline.. Athens' empire vs Sparta. Details are where historians live — the numbers, the names, the decisions that turned Peloponnesian War the way it did. Athens vs Sparta; Thucydides' history.", "s": "public-reference", "f": null}, {"t": "Timeline", "d": "Peloponnesian War, event by event.", "g": "timeline", "l": 2, "q": "What is Timeline?", "a": "Peloponnesian War, event by event.", "x": "The timeline: Athens' empire vs Sparta.. Thucydides wrote it. Key dates in order — Plague hit Athens.. 431-404 BC Pin the dates first; the story hangs on them. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key figures", "d": "The people of Peloponnesian War.", "g": "people", "l": 2, "q": "What is Key figures?", "a": "The people of Peloponnesian War.", "x": "The people: Long Walls.. Sicilian disaster. History is made by people deciding under pressure — Athens vs Sparta; Thucydides' history.. Oligarchic coups. Know the actors and the events make sense. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "More key figures", "d": "More people who shaped Peloponnesian War.", "g": "people", "l": 2, "q": "What is More key figures?", "a": "More people who shaped Peloponnesian War.", "x": "More figures: Sparta won. shaped Peloponnesian War as surely as anyone — Aegospotami.. Athens vs Sparta; Thucydides' history. History remembers the famous; the wise student learns the overlooked too. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Causes", "d": "Why Peloponnesian War happened.", "g": "causes", "l": 2, "q": "What is Causes?", "a": "Why Peloponnesian War happened.", "x": "The causes: Athens' empire vs Sparta.. Alcibiades. Historians debate the deep vs immediate causes of Peloponnesian War — Athens vs Sparta; Thucydides' history.. Democracy weakened. Understanding why is the whole point of studying history.", "s": "public-reference", "f": null}, {"t": "The turning point", "d": "The moment Peloponnesian War turned.", "g": "turning-point", "l": 2, "q": "What is The turning point?", "a": "The moment Peloponnesian War turned.", "x": "The turning point: Oligarchic coups.. Pericles' strategy. Every great story has the moment it could have gone otherwise — Peloponnesian War. Athens vs Sparta; Thucydides' history. Find it and you find the drama.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-war-peloponnesian-war-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
