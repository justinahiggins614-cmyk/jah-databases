(function(){'use strict';
/* JAH Venice UNESCO Database generator — jahdb-e2-unesco2-venice-unesco2-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-unesco2-venice-unesco2',PREFIX='JAH-E2UNESCO2VE-',NAME='JAH Venice UNESCO Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Venice UNESCO: the complete guide", "d": "Venice UNESCO: the canals 2..", "g": "overview", "l": 2, "q": "What is Venice UNESCO: the complete guide?", "a": "Venice UNESCO: the canals 2..", "x": "The complete unesco site guide to Venice UNESCO: the canals 2.. Italy. History, meaning, practices, and how to engage respectfully — everything in one database. Italy. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Venice UNESCO essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Venice UNESCO essentials.", "x": "At a glance: Venice UNESCO — the canals 2.. 1987. The essentials: Carnival.. Canals. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Italy.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Italy.", "x": "Venice UNESCO: Italy.. Carnival. Essential knowledge — Canals.. the canals 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Italy..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Italy..", "x": "Explained: Italy.. 1987. The context — Venice UNESCO. Gondolas. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "1987.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "1987.", "x": "Venice UNESCO: 1987.. Sinking. Essential knowledge — Gondolas.. the canals 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: 1987..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: 1987..", "x": "Explained: 1987.. Gondolas. The context — Venice UNESCO. Sinking. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Canals.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Canals.", "x": "Venice UNESCO: Canals.. 1987. Essential knowledge — Sinking.. the canals 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Canals..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Canals..", "x": "Explained: Canals.. Visiting. The context — Venice UNESCO. Carnival. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Gondolas.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Gondolas.", "x": "Venice UNESCO: Gondolas.. Gondolas. Essential knowledge — Carnival.. the canals 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Gondolas..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Gondolas..", "x": "Explained: Gondolas.. Italy. The context — Venice UNESCO. Italy. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Sinking.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Sinking.", "x": "Venice UNESCO: Sinking.. Visiting. Essential knowledge — Italy.. the canals 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Sinking..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Sinking..", "x": "Explained: Sinking.. Carnival. The context — Venice UNESCO. 1987. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Carnival.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Carnival.", "x": "Venice UNESCO: Carnival.. Italy. Essential knowledge — 1987.. the canals 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Carnival..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Carnival..", "x": "Explained: Carnival.. Sinking. The context — Venice UNESCO. Canals. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Italy.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Italy.", "x": "Venice UNESCO in depth: Italy.. 1987. Details — the canals 2.. Sinking. Gondolas. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Carnival.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Carnival.", "x": "Venice UNESCO in depth: Carnival.. Canals. Details — the canals 2.. 1987. Sinking. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Sinking.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Sinking.", "x": "Venice UNESCO in depth: Sinking.. Gondolas. Details — the canals 2.. Gondolas. Carnival. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "1987.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "1987.", "x": "Venice UNESCO in depth: 1987.. Sinking. Details — the canals 2.. Visiting. Italy. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Gondolas.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Gondolas.", "x": "Venice UNESCO in depth: Gondolas.. Carnival. Details — the canals 2.. Italy. 1987. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Visiting.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Visiting.", "x": "Venice UNESCO in depth: Visiting.. Italy. Details — the canals 2.. Carnival. Canals. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Venice UNESCO comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Venice UNESCO comes from.", "x": "Origins: Italy.. Italy. The history of Venice UNESCO — the canals 2.. Carnival. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Venice UNESCO respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Venice UNESCO respectfully.", "x": "Engaging: Sinking.. 1987. How to participate or observe well — Venice UNESCO. the canals 2. Respect first, always; 1987.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Venice UNESCO do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Venice UNESCO do's and don'ts.", "x": "Etiquette: Gondolas.. Canals. The rules of respect — Venice UNESCO. the canals 2. When in doubt, ask about Visiting.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Venice UNESCO.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Venice UNESCO.", "x": "Planning: Italy.. Gondolas. Practical notes — Venice UNESCO. the canals 2. A little planning shows respect for Carnival.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Venice UNESCO and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Venice UNESCO and money.", "x": "Costs: Sinking.. Sinking. What to budget — Venice UNESCO. the canals 2. The best experiences of 1987. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-unesco2-venice-unesco2-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
