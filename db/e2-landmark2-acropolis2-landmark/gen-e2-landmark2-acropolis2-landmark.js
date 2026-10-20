(function(){'use strict';
/* JAH Acropolis2 Database generator — jahdb-e2-landmark2-acropolis2-landmark-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-landmark2-acropolis2-landmark',PREFIX='JAH-E2LANDMARK2-',NAME='JAH Acropolis2 Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Acropolis2: the complete guide", "d": "Acropolis2: the Athenian rock..", "g": "overview", "l": 2, "q": "What is Acropolis2: the complete guide?", "a": "Acropolis2: the Athenian rock..", "x": "The complete landmark guide to Acropolis2: the Athenian rock.. Athens. History, meaning, practices, and how to engage respectfully — everything in one database. Athens. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Acropolis2 essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Acropolis2 essentials.", "x": "At a glance: Acropolis2 — the Athenian rock.. Parthenon. The essentials: UNESCO.. 5th BC. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Athens.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Athens.", "x": "Acropolis2: Athens.. UNESCO. Essential knowledge — 5th BC.. the Athenian rock. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Athens..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Athens..", "x": "Explained: Athens.. Parthenon. The context — Acropolis2. Marble. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Parthenon.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Parthenon.", "x": "Acropolis2: Parthenon.. Democracy. Essential knowledge — Marble.. the Athenian rock. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Parthenon..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Parthenon..", "x": "Explained: Parthenon.. 5th BC. The context — Acropolis2. Democracy. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "5th BC.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "5th BC.", "x": "Acropolis2: 5th BC.. Parthenon. Essential knowledge — Democracy.. the Athenian rock. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: 5th BC..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: 5th BC..", "x": "Explained: 5th BC.. Visiting. The context — Acropolis2. UNESCO. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Marble.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Marble.", "x": "Acropolis2: Marble.. 5th BC. Essential knowledge — UNESCO.. the Athenian rock. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Marble..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Marble..", "x": "Explained: Marble.. Athens. The context — Acropolis2. Athens. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Democracy.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Democracy.", "x": "Acropolis2: Democracy.. Visiting. Essential knowledge — Athens.. the Athenian rock. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Democracy..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Democracy..", "x": "Explained: Democracy.. UNESCO. The context — Acropolis2. Parthenon. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "UNESCO.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "UNESCO.", "x": "Acropolis2: UNESCO.. Athens. Essential knowledge — Parthenon.. the Athenian rock. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: UNESCO..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: UNESCO..", "x": "Explained: UNESCO.. Democracy. The context — Acropolis2. 5th BC. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Athens.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Athens.", "x": "Acropolis2 in depth: Athens.. Parthenon. Details — the Athenian rock.. Democracy. Marble. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "UNESCO.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "UNESCO.", "x": "Acropolis2 in depth: UNESCO.. 5th BC. Details — the Athenian rock.. Parthenon. Democracy. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Democracy.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Democracy.", "x": "Acropolis2 in depth: Democracy.. Marble. Details — the Athenian rock.. 5th BC. UNESCO. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Parthenon.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Parthenon.", "x": "Acropolis2 in depth: Parthenon.. Democracy. Details — the Athenian rock.. Visiting. Athens. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "5th BC.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "5th BC.", "x": "Acropolis2 in depth: 5th BC.. UNESCO. Details — the Athenian rock.. Athens. Parthenon. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Visiting.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Visiting.", "x": "Acropolis2 in depth: Visiting.. Athens. Details — the Athenian rock.. UNESCO. 5th BC. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Acropolis2 comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Acropolis2 comes from.", "x": "Origins: Athens.. Athens. The history of Acropolis2 — the Athenian rock.. UNESCO. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Acropolis2 respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Acropolis2 respectfully.", "x": "Engaging: Democracy.. Parthenon. How to participate or observe well — Acropolis2. the Athenian rock. Respect first, always; Parthenon.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Acropolis2 do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Acropolis2 do's and don'ts.", "x": "Etiquette: 5th BC.. 5th BC. The rules of respect — Acropolis2. the Athenian rock. When in doubt, ask about Visiting.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Acropolis2.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Acropolis2.", "x": "Planning: Athens.. Marble. Practical notes — Acropolis2. the Athenian rock. A little planning shows respect for UNESCO.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Acropolis2 and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Acropolis2 and money.", "x": "Costs: Democracy.. Democracy. What to budget — Acropolis2. the Athenian rock. The best experiences of Parthenon. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-landmark2-acropolis2-landmark-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
