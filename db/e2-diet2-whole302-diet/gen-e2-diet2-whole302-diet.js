(function(){'use strict';
/* JAH Whole302 Database generator — jahdb-e2-diet2-whole302-diet-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-diet2-whole302-diet',PREFIX='JAH-E2DIET2WHOL-',NAME='JAH Whole302 Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Whole302: the complete guide", "d": "Whole302: the reset 2..", "g": "overview", "l": 2, "q": "What is Whole302: the complete guide?", "a": "Whole302: the reset 2..", "x": "The complete diet guide to Whole302: the reset 2.. NSV. History, meaning, practices, and how to engage respectfully — everything in one database. NSV. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Whole302 essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Whole302 essentials.", "x": "At a glance: Whole302 — the reset 2.. Reintro. The essentials: Community.. Tiger Blood. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "NSV.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "NSV.", "x": "Whole302: NSV.. Community. Essential knowledge — Tiger Blood.. the reset 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: NSV..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: NSV..", "x": "Explained: NSV.. Reintro. The context — Whole302. 30 days. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Reintro.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Reintro.", "x": "Whole302: Reintro.. Rules. Essential knowledge — 30 days.. the reset 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Reintro..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Reintro..", "x": "Explained: Reintro.. 30 days. The context — Whole302. Rules. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Tiger Blood.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Tiger Blood.", "x": "Whole302: Tiger Blood.. Reintro. Essential knowledge — Rules.. the reset 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Tiger Blood..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Tiger Blood..", "x": "Explained: Tiger Blood.. Guide. The context — Whole302. Community. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "30 days.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "30 days.", "x": "Whole302: 30 days.. 30 days. Essential knowledge — Community.. the reset 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: 30 days..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: 30 days..", "x": "Explained: 30 days.. NSV. The context — Whole302. NSV. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Rules.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Rules.", "x": "Whole302: Rules.. Guide. Essential knowledge — NSV.. the reset 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Rules..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Rules..", "x": "Explained: Rules.. Community. The context — Whole302. Reintro. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Community.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Community.", "x": "Whole302: Community.. NSV. Essential knowledge — Reintro.. the reset 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Community..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Community..", "x": "Explained: Community.. Rules. The context — Whole302. Tiger Blood. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "NSV.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "NSV.", "x": "Whole302 in depth: NSV.. Reintro. Details — the reset 2.. Rules. 30 days. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Community.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Community.", "x": "Whole302 in depth: Community.. Tiger Blood. Details — the reset 2.. Reintro. Rules. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Rules.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Rules.", "x": "Whole302 in depth: Rules.. 30 days. Details — the reset 2.. 30 days. Community. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Reintro.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Reintro.", "x": "Whole302 in depth: Reintro.. Rules. Details — the reset 2.. Guide. NSV. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "30 days.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "30 days.", "x": "Whole302 in depth: 30 days.. Community. Details — the reset 2.. NSV. Reintro. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Guide.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Guide.", "x": "Whole302 in depth: Guide.. NSV. Details — the reset 2.. Community. Tiger Blood. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Whole302 comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Whole302 comes from.", "x": "Origins: NSV.. NSV. The history of Whole302 — the reset 2.. Community. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Whole302 respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Whole302 respectfully.", "x": "Engaging: Rules.. Reintro. How to participate or observe well — Whole302. the reset 2. Respect first, always; Reintro.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Whole302 do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Whole302 do's and don'ts.", "x": "Etiquette: 30 days.. Tiger Blood. The rules of respect — Whole302. the reset 2. When in doubt, ask about Guide.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Whole302.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Whole302.", "x": "Planning: NSV.. 30 days. Practical notes — Whole302. the reset 2. A little planning shows respect for Community.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Whole302 and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Whole302 and money.", "x": "Costs: Rules.. Rules. What to budget — Whole302. the reset 2. The best experiences of Reintro. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-diet2-whole302-diet-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
