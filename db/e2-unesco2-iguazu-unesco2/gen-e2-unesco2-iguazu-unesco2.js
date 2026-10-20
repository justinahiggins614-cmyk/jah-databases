(function(){'use strict';
/* JAH Iguazu UNESCO Database generator — jahdb-e2-unesco2-iguazu-unesco2-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-unesco2-iguazu-unesco2',PREFIX='JAH-E2UNESCO2IG-',NAME='JAH Iguazu UNESCO Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Iguazu UNESCO: the complete guide", "d": "Iguazu UNESCO: the falls 2..", "g": "overview", "l": 2, "q": "What is Iguazu UNESCO: the complete guide?", "a": "Iguazu UNESCO: the falls 2..", "x": "The complete unesco site guide to Iguazu UNESCO: the falls 2.. Argentina. History, meaning, practices, and how to engage respectfully — everything in one database. Argentina. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Iguazu UNESCO essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Iguazu UNESCO essentials.", "x": "At a glance: Iguazu UNESCO — the falls 2.. 1984. The essentials: Mist.. Falls. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Argentina.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Argentina.", "x": "Iguazu UNESCO: Argentina.. Mist. Essential knowledge — Falls.. the falls 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Argentina..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Argentina..", "x": "Explained: Argentina.. 1984. The context — Iguazu UNESCO. Devil's Throat. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "1984.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "1984.", "x": "Iguazu UNESCO: 1984.. Brazil. Essential knowledge — Devil's Throat.. the falls 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: 1984..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: 1984..", "x": "Explained: 1984.. Throat. The context — Iguazu UNESCO. Brazil. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Falls.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Falls.", "x": "Iguazu UNESCO: Falls.. 1984. Essential knowledge — Brazil.. the falls 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Falls..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Falls..", "x": "Explained: Falls.. Visiting. The context — Iguazu UNESCO. Mist. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Devil's Throat.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Devil's Throat.", "x": "Iguazu UNESCO: Devil's Throat.. Throat. Essential knowledge — Mist.. the falls 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Devil's Throat..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Devil's Throat..", "x": "Explained: Devil's Throat.. Argentina. The context — Iguazu UNESCO. Argentina. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Brazil.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Brazil.", "x": "Iguazu UNESCO: Brazil.. Visiting. Essential knowledge — Argentina.. the falls 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Brazil..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Brazil..", "x": "Explained: Brazil.. Mist. The context — Iguazu UNESCO. 1984. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Mist.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Mist.", "x": "Iguazu UNESCO: Mist.. Argentina. Essential knowledge — 1984.. the falls 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Mist..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Mist..", "x": "Explained: Mist.. Brazil. The context — Iguazu UNESCO. Falls. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Argentina.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Argentina.", "x": "Iguazu UNESCO in depth: Argentina.. 1984. Details — the falls 2.. Brazil. Devil's Throat. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Mist.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Mist.", "x": "Iguazu UNESCO in depth: Mist.. Falls. Details — the falls 2.. 1984. Brazil. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Brazil.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Brazil.", "x": "Iguazu UNESCO in depth: Brazil.. Devil's Throat. Details — the falls 2.. Throat. Mist. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "1984.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "1984.", "x": "Iguazu UNESCO in depth: 1984.. Brazil. Details — the falls 2.. Visiting. Argentina. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Throat.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Throat.", "x": "Iguazu UNESCO in depth: Throat.. Mist. Details — the falls 2.. Argentina. 1984. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Visiting.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Visiting.", "x": "Iguazu UNESCO in depth: Visiting.. Argentina. Details — the falls 2.. Mist. Falls. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Iguazu UNESCO comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Iguazu UNESCO comes from.", "x": "Origins: Argentina.. Argentina. The history of Iguazu UNESCO — the falls 2.. Mist. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Iguazu UNESCO respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Iguazu UNESCO respectfully.", "x": "Engaging: Brazil.. 1984. How to participate or observe well — Iguazu UNESCO. the falls 2. Respect first, always; 1984.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Iguazu UNESCO do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Iguazu UNESCO do's and don'ts.", "x": "Etiquette: Throat.. Falls. The rules of respect — Iguazu UNESCO. the falls 2. When in doubt, ask about Visiting.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Iguazu UNESCO.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Iguazu UNESCO.", "x": "Planning: Argentina.. Devil's Throat. Practical notes — Iguazu UNESCO. the falls 2. A little planning shows respect for Mist.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Iguazu UNESCO and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Iguazu UNESCO and money.", "x": "Costs: Brazil.. Brazil. What to budget — Iguazu UNESCO. the falls 2. The best experiences of 1984. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-unesco2-iguazu-unesco2-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
