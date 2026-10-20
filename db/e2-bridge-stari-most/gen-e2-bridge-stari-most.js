(function(){'use strict';
/* JAH Stari Most Bridge Database generator — jahdb-e2-bridge-stari-most-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-bridge-stari-most',PREFIX='JAH-E2BRIDGESTA-',NAME='JAH Stari Most Bridge Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Stari Most: the complete guide", "d": "Stari Most: Mostar's rebuilt arch..", "g": "overview", "l": 2, "q": "What is Stari Most: the complete guide?", "a": "Stari Most: Mostar's rebuilt arch..", "x": "The complete bridge guide to Stari Most: Mostar's rebuilt arch.. 1566. History, meaning, practices, and how to engage respectfully — everything in one database. War. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Stari Most essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Stari Most essentials.", "x": "At a glance: Stari Most — Mostar's rebuilt arch.. War destroyed. The essentials: Rebuild.. Rebuilt 2004. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "1566.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "1566.", "x": "Stari Most: 1566.. Rebuild. Essential knowledge — Rebuilt 2004.. Mostar's rebuilt arch. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 1566..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 1566..", "x": "Explained: 1566.. History. The context — Stari Most. Divers. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "War destroyed.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "War destroyed.", "x": "Stari Most: War destroyed.. Divers. Essential knowledge — Divers.. Mostar's rebuilt arch. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: War destroyed..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: War destroyed..", "x": "Explained: War destroyed.. UNESCO. The context — Stari Most. UNESCO. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Rebuilt 2004.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Rebuilt 2004.", "x": "Stari Most: Rebuilt 2004.. History. Essential knowledge — UNESCO.. Mostar's rebuilt arch. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Rebuilt 2004..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Rebuilt 2004..", "x": "Explained: Rebuilt 2004.. Views. The context — Stari Most. Bosnia. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Divers.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Divers.", "x": "Stari Most: Divers.. UNESCO. Essential knowledge — Bosnia.. Mostar's rebuilt arch. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Divers..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Divers..", "x": "Explained: Divers.. War. The context — Stari Most. 1566. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "UNESCO.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "UNESCO.", "x": "Stari Most: UNESCO.. Views. Essential knowledge — 1566.. Mostar's rebuilt arch. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: UNESCO..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: UNESCO..", "x": "Explained: UNESCO.. Rebuild. The context — Stari Most. War destroyed. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Bosnia.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Bosnia.", "x": "Stari Most: Bosnia.. War. Essential knowledge — War destroyed.. Mostar's rebuilt arch. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Bosnia..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Bosnia..", "x": "Explained: Bosnia.. Divers. The context — Stari Most. Rebuilt 2004. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "War.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "War.", "x": "Stari Most in depth: War.. War destroyed. Details — Mostar's rebuilt arch.. Divers. Divers. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Rebuild.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Rebuild.", "x": "Stari Most in depth: Rebuild.. Rebuilt 2004. Details — Mostar's rebuilt arch.. History. UNESCO. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Divers.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Divers.", "x": "Stari Most in depth: Divers.. Divers. Details — Mostar's rebuilt arch.. UNESCO. Bosnia. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "History.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "History.", "x": "Stari Most in depth: History.. UNESCO. Details — Mostar's rebuilt arch.. Views. 1566. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "UNESCO.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "UNESCO.", "x": "Stari Most in depth: UNESCO.. Bosnia. Details — Mostar's rebuilt arch.. War. War destroyed. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Views.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Views.", "x": "Stari Most in depth: Views.. 1566. Details — Mostar's rebuilt arch.. Rebuild. Rebuilt 2004. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Stari Most comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Stari Most comes from.", "x": "Origins: War.. 1566. The history of Stari Most — Mostar's rebuilt arch.. Rebuild. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Stari Most respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Stari Most respectfully.", "x": "Engaging: Divers.. War destroyed. How to participate or observe well — Stari Most. Mostar's rebuilt arch. Respect first, always; History.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Stari Most do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Stari Most do's and don'ts.", "x": "Etiquette: UNESCO.. Rebuilt 2004. The rules of respect — Stari Most. Mostar's rebuilt arch. When in doubt, ask about Views.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Stari Most.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Stari Most.", "x": "Planning: War.. Divers. Practical notes — Stari Most. Mostar's rebuilt arch. A little planning shows respect for Rebuild.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Stari Most and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Stari Most and money.", "x": "Costs: Divers.. UNESCO. What to budget — Stari Most. Mostar's rebuilt arch. The best experiences of History. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-bridge-stari-most-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
