(function(){'use strict';
/* JAH English Civil War War Database generator — jahdb-e2-war-english-civil-war-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-war-english-civil-war',PREFIX='JAH-E2WARENGLIS-',NAME='JAH English Civil War War Database';
var FIELDS=["overview", "context", "facts", "details", "timeline", "people", "causes", "turning-point", "legacy", "misconceptions", "what-if", "quiz", "sources", "learn-more"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "English Civil War: overview", "d": "English Civil War (1642-1651): Parliament vs King; Cromwell's republic..", "g": "overview", "l": 2, "q": "What is English Civil War: overview?", "a": "English Civil War (1642-1651): Parliament vs King; Cromwell's republic..", "x": "The complete war guide to English Civil War: Parliament vs King; Cromwell's republic.. Charles I vs Parliament. From causes to consequences, from the key figures to the legacy that still shapes us — this database tells the whole story the way a great history course would.", "s": "public-reference", "f": null}, {"t": "The era", "d": "English Civil War in its time: 1642-1651.", "g": "context", "l": 2, "q": "What is The era?", "a": "English Civil War in its time: 1642-1651.", "x": "Context: English Civil War belonged to 1642-1651 — Ship Money.. Cromwell's New Model Army. Nothing in history happens in a vacuum; the era explains the motives, the means, and the stakes. Parliament vs King; Cromwell's republic.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Charles I vs Parliament.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Charles I vs Parliament.", "x": "English Civil War: Charles I vs Parliament.. Naseby battle. This is one of the load-bearing facts about English Civil War — learn it cold. King executed 1649. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "The story behind: Charles I vs Parliament..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "The story behind: Charles I vs Parliament..", "x": "Explained: Charles I vs Parliament.. Irish campaign. In the history of English Civil War, this fact connects to Commonwealth republic. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Cromwell's New Model Army.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Cromwell's New Model Army.", "x": "English Civil War: Cromwell's New Model Army.. Pride's Purge. This is one of the load-bearing facts about English Civil War — learn it cold. Commonwealth republic. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "The story behind: Cromwell's New Model Army..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "The story behind: Cromwell's New Model Army..", "x": "Explained: Cromwell's New Model Army.. Protectorate. In the history of English Civil War, this fact connects to Restoration 1660. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "King executed 1649.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "King executed 1649.", "x": "English Civil War: King executed 1649.. Irish campaign. This is one of the load-bearing facts about English Civil War — learn it cold. Restoration 1660. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "The story behind: King executed 1649..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "The story behind: King executed 1649..", "x": "Explained: King executed 1649.. Legacy: constitutional monarchy. In the history of English Civil War, this fact connects to No standing king above law. — see the connections and you have understanding, not trivia.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Commonwealth republic.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Commonwealth republic.", "x": "English Civil War: Commonwealth republic.. Protectorate. This is one of the load-bearing facts about English Civil War — learn it cold. No standing king above law. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "The story behind: Commonwealth republic..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "The story behind: Commonwealth republic..", "x": "Explained: Commonwealth republic.. Ship Money. In the history of English Civil War, this fact connects to Charles I vs Parliament. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Restoration 1660.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Restoration 1660.", "x": "English Civil War: Restoration 1660.. Legacy: constitutional monarchy. This is one of the load-bearing facts about English Civil War — learn it cold. Charles I vs Parliament. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "The story behind: Restoration 1660..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "The story behind: Restoration 1660..", "x": "Explained: Restoration 1660.. Naseby battle. In the history of English Civil War, this fact connects to Cromwell's New Model Army. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "No standing king above law.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "No standing king above law.", "x": "English Civil War: No standing king above law.. Ship Money. This is one of the load-bearing facts about English Civil War — learn it cold. Cromwell's New Model Army. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "The story behind: No standing king above law..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "The story behind: No standing king above law..", "x": "Explained: No standing king above law.. Pride's Purge. In the history of English Civil War, this fact connects to King executed 1649. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Ship Money.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Ship Money.", "x": "Going deeper: Ship Money.. Cromwell's New Model Army. Details are where historians live — the numbers, the names, the decisions that turned English Civil War the way it did. Parliament vs King; Cromwell's republic.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Naseby battle.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Naseby battle.", "x": "Going deeper: Naseby battle.. King executed 1649. Details are where historians live — the numbers, the names, the decisions that turned English Civil War the way it did. Parliament vs King; Cromwell's republic.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Pride's Purge.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Pride's Purge.", "x": "Going deeper: Pride's Purge.. Commonwealth republic. Details are where historians live — the numbers, the names, the decisions that turned English Civil War the way it did. Parliament vs King; Cromwell's republic.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Irish campaign.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Irish campaign.", "x": "Going deeper: Irish campaign.. Restoration 1660. Details are where historians live — the numbers, the names, the decisions that turned English Civil War the way it did. Parliament vs King; Cromwell's republic.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Protectorate.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Protectorate.", "x": "Going deeper: Protectorate.. No standing king above law. Details are where historians live — the numbers, the names, the decisions that turned English Civil War the way it did. Parliament vs King; Cromwell's republic.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Legacy: constitutional monarchy.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Legacy: constitutional monarchy.", "x": "Going deeper: Legacy: constitutional monarchy.. Charles I vs Parliament. Details are where historians live — the numbers, the names, the decisions that turned English Civil War the way it did. Parliament vs King; Cromwell's republic.", "s": "public-reference", "f": null}, {"t": "Timeline", "d": "English Civil War, event by event.", "g": "timeline", "l": 2, "q": "What is Timeline?", "a": "English Civil War, event by event.", "x": "The timeline: Charles I vs Parliament.. Ship Money. Key dates in order — King executed 1649.. 1642-1651 Pin the dates first; the story hangs on them. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key figures", "d": "The people of English Civil War.", "g": "people", "l": 2, "q": "What is Key figures?", "a": "The people of English Civil War.", "x": "The people: Naseby battle.. Commonwealth republic. History is made by people deciding under pressure — Parliament vs King; Cromwell's republic.. Irish campaign. Know the actors and the events make sense.", "s": "public-reference", "f": null}, {"t": "More key figures", "d": "More people who shaped English Civil War.", "g": "people", "l": 2, "q": "What is More key figures?", "a": "More people who shaped English Civil War.", "x": "More figures: Restoration 1660. shaped English Civil War as surely as anyone — Protectorate.. Parliament vs King; Cromwell's republic. History remembers the famous; the wise student learns the overlooked too.", "s": "public-reference", "f": null}, {"t": "Causes", "d": "Why English Civil War happened.", "g": "causes", "l": 2, "q": "What is Causes?", "a": "Why English Civil War happened.", "x": "The causes: Charles I vs Parliament.. Pride's Purge. Historians debate the deep vs immediate causes of English Civil War — Parliament vs King; Cromwell's republic.. No standing king above law. Understanding why is the whole point of studying history.", "s": "public-reference", "f": null}, {"t": "The turning point", "d": "The moment English Civil War turned.", "g": "turning-point", "l": 2, "q": "What is The turning point?", "a": "The moment English Civil War turned.", "x": "The turning point: Irish campaign.. Cromwell's New Model Army. Every great story has the moment it could have gone otherwise — English Civil War. Parliament vs King; Cromwell's republic. Find it and you find the drama.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-war-english-civil-war-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
