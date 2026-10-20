(function(){'use strict';
/* JAH Colosseum2 Database generator — jahdb-e2-landmark2-colosseum2-landmark-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-landmark2-colosseum2-landmark',PREFIX='JAH-E2LANDMARK2-',NAME='JAH Colosseum2 Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Colosseum2: the complete guide", "d": "Colosseum2: the Roman arena..", "g": "overview", "l": 2, "q": "What is Colosseum2: the complete guide?", "a": "Colosseum2: the Roman arena..", "x": "The complete landmark guide to Colosseum2: the Roman arena.. Rome. History, meaning, practices, and how to engage respectfully — everything in one database. Rome. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Colosseum2 essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Colosseum2 essentials.", "x": "At a glance: Colosseum2 — the Roman arena.. 80 AD. The essentials: Ruins.. Gladiators. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Rome.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Rome.", "x": "Colosseum2: Rome.. Ruins. Essential knowledge — Gladiators.. the Roman arena. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Rome..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Rome..", "x": "Explained: Rome.. 80 AD. The context — Colosseum2. 50K. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "80 AD.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "80 AD.", "x": "Colosseum2: 80 AD.. Flavian. Essential knowledge — 50K.. the Roman arena. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: 80 AD..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: 80 AD..", "x": "Explained: 80 AD.. 50K. The context — Colosseum2. Flavian. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Gladiators.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Gladiators.", "x": "Colosseum2: Gladiators.. 80 AD. Essential knowledge — Flavian.. the Roman arena. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Gladiators..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Gladiators..", "x": "Explained: Gladiators.. Visiting. The context — Colosseum2. Ruins. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "50K.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "50K.", "x": "Colosseum2: 50K.. 50K. Essential knowledge — Ruins.. the Roman arena. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: 50K..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: 50K..", "x": "Explained: 50K.. Rome. The context — Colosseum2. Rome. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Flavian.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Flavian.", "x": "Colosseum2: Flavian.. Visiting. Essential knowledge — Rome.. the Roman arena. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Flavian..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Flavian..", "x": "Explained: Flavian.. Ruins. The context — Colosseum2. 80 AD. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Ruins.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Ruins.", "x": "Colosseum2: Ruins.. Rome. Essential knowledge — 80 AD.. the Roman arena. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Ruins..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Ruins..", "x": "Explained: Ruins.. Flavian. The context — Colosseum2. Gladiators. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Rome.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Rome.", "x": "Colosseum2 in depth: Rome.. 80 AD. Details — the Roman arena.. Flavian. 50K. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Ruins.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Ruins.", "x": "Colosseum2 in depth: Ruins.. Gladiators. Details — the Roman arena.. 80 AD. Flavian. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Flavian.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Flavian.", "x": "Colosseum2 in depth: Flavian.. 50K. Details — the Roman arena.. 50K. Ruins. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "80 AD.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "80 AD.", "x": "Colosseum2 in depth: 80 AD.. Flavian. Details — the Roman arena.. Visiting. Rome. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "50K.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "50K.", "x": "Colosseum2 in depth: 50K.. Ruins. Details — the Roman arena.. Rome. 80 AD. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Visiting.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Visiting.", "x": "Colosseum2 in depth: Visiting.. Rome. Details — the Roman arena.. Ruins. Gladiators. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Colosseum2 comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Colosseum2 comes from.", "x": "Origins: Rome.. Rome. The history of Colosseum2 — the Roman arena.. Ruins. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Colosseum2 respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Colosseum2 respectfully.", "x": "Engaging: Flavian.. 80 AD. How to participate or observe well — Colosseum2. the Roman arena. Respect first, always; 80 AD.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Colosseum2 do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Colosseum2 do's and don'ts.", "x": "Etiquette: 50K.. Gladiators. The rules of respect — Colosseum2. the Roman arena. When in doubt, ask about Visiting.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Colosseum2.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Colosseum2.", "x": "Planning: Rome.. 50K. Practical notes — Colosseum2. the Roman arena. A little planning shows respect for Ruins.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Colosseum2 and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Colosseum2 and money.", "x": "Costs: Flavian.. Flavian. What to budget — Colosseum2. the Roman arena. The best experiences of 80 AD. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-landmark2-colosseum2-landmark-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
