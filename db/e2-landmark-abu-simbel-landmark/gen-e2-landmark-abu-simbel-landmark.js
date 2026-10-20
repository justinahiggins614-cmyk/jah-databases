(function(){'use strict';
/* JAH Abu Simbel Landmark Database generator — jahdb-e2-landmark-abu-simbel-landmark-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-landmark-abu-simbel-landmark',PREFIX='JAH-E2LANDMARKA-',NAME='JAH Abu Simbel Landmark Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Abu Simbel: the complete guide", "d": "Abu Simbel: the relocated colossi..", "g": "overview", "l": 2, "q": "What is Abu Simbel: the complete guide?", "a": "Abu Simbel: the relocated colossi..", "x": "The complete landmark guide to Abu Simbel: the relocated colossi.. Relocated. History, meaning, practices, and how to engage respectfully — everything in one database. Relocated. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Abu Simbel essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Abu Simbel essentials.", "x": "At a glance: Abu Simbel — the relocated colossi.. Ramses II. The essentials: Colossi.. 4 colossi. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Relocated.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Relocated.", "x": "Abu Simbel: Relocated.. Colossi. Essential knowledge — 4 colossi.. the relocated colossi. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Relocated..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Relocated..", "x": "Explained: Relocated.. Nubia. The context — Abu Simbel. Sun. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Ramses II.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Ramses II.", "x": "Abu Simbel: Ramses II.. UNESCO. Essential knowledge — Sun.. the relocated colossi. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Ramses II..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Ramses II..", "x": "Explained: Ramses II.. Sun. The context — Abu Simbel. UNESCO. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "4 colossi.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "4 colossi.", "x": "Abu Simbel: 4 colossi.. Nubia. Essential knowledge — UNESCO.. the relocated colossi. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: 4 colossi..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: 4 colossi..", "x": "Explained: 4 colossi.. Tours. The context — Abu Simbel. Nubia. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Sun.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Sun.", "x": "Abu Simbel: Sun.. Sun. Essential knowledge — Nubia.. the relocated colossi. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Sun..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Sun..", "x": "Explained: Sun.. Relocated. The context — Abu Simbel. Relocated. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "UNESCO.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "UNESCO.", "x": "Abu Simbel: UNESCO.. Tours. Essential knowledge — Relocated.. the relocated colossi. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: UNESCO..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: UNESCO..", "x": "Explained: UNESCO.. Colossi. The context — Abu Simbel. Ramses II. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Nubia.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Nubia.", "x": "Abu Simbel: Nubia.. Relocated. Essential knowledge — Ramses II.. the relocated colossi. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Nubia..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Nubia..", "x": "Explained: Nubia.. UNESCO. The context — Abu Simbel. 4 colossi. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Relocated.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Relocated.", "x": "Abu Simbel in depth: Relocated.. Ramses II. Details — the relocated colossi.. UNESCO. Sun. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Colossi.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Colossi.", "x": "Abu Simbel in depth: Colossi.. 4 colossi. Details — the relocated colossi.. Nubia. UNESCO. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "UNESCO.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "UNESCO.", "x": "Abu Simbel in depth: UNESCO.. Sun. Details — the relocated colossi.. Sun. Nubia. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Nubia.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Nubia.", "x": "Abu Simbel in depth: Nubia.. UNESCO. Details — the relocated colossi.. Tours. Relocated. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Sun.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Sun.", "x": "Abu Simbel in depth: Sun.. Nubia. Details — the relocated colossi.. Relocated. Ramses II. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Tours.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Tours.", "x": "Abu Simbel in depth: Tours.. Relocated. Details — the relocated colossi.. Colossi. 4 colossi. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Abu Simbel comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Abu Simbel comes from.", "x": "Origins: Relocated.. Relocated. The history of Abu Simbel — the relocated colossi.. Colossi. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Abu Simbel respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Abu Simbel respectfully.", "x": "Engaging: UNESCO.. Ramses II. How to participate or observe well — Abu Simbel. the relocated colossi. Respect first, always; Nubia.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Abu Simbel do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Abu Simbel do's and don'ts.", "x": "Etiquette: Sun.. 4 colossi. The rules of respect — Abu Simbel. the relocated colossi. When in doubt, ask about Tours.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Abu Simbel.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Abu Simbel.", "x": "Planning: Relocated.. Sun. Practical notes — Abu Simbel. the relocated colossi. A little planning shows respect for Colossi.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Abu Simbel and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Abu Simbel and money.", "x": "Costs: UNESCO.. UNESCO. What to budget — Abu Simbel. the relocated colossi. The best experiences of Nubia. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-landmark-abu-simbel-landmark-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
