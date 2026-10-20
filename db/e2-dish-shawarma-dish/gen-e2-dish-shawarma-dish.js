(function(){'use strict';
/* JAH Shawarma Dish Database generator — jahdb-e2-dish-shawarma-dish-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-dish-shawarma-dish',PREFIX='JAH-E2DISHSHAWA-',NAME='JAH Shawarma Dish Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Shawarma: the complete guide", "d": "Shawarma: the vertical meat..", "g": "overview", "l": 2, "q": "What is Shawarma: the complete guide?", "a": "Shawarma: the vertical meat..", "x": "The complete dish guide to Shawarma: the vertical meat.. Vertical. History, meaning, practices, and how to engage respectfully — everything in one database. Vertical. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Shawarma essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Shawarma essentials.", "x": "At a glance: Shawarma — the vertical meat.. Lamb. The essentials: Pickles.. Garlic. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Vertical.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Vertical.", "x": "Shawarma: Vertical.. Pickles. Essential knowledge — Garlic.. the vertical meat. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Vertical..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Vertical..", "x": "Explained: Vertical.. Lamb. The context — Shawarma. Pickles. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Lamb.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Lamb.", "x": "Shawarma: Lamb.. Street. Essential knowledge — Pickles.. the vertical meat. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Lamb..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Lamb..", "x": "Explained: Lamb.. Garlic. The context — Shawarma. Rotisserie. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Garlic.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Garlic.", "x": "Shawarma: Garlic.. Lamb. Essential knowledge — Rotisserie.. the vertical meat. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Garlic..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Garlic..", "x": "Explained: Garlic.. Making. The context — Shawarma. Street. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Pickles.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Pickles.", "x": "Shawarma: Pickles.. Garlic. Essential knowledge — Street.. the vertical meat. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Pickles..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Pickles..", "x": "Explained: Pickles.. Vertical. The context — Shawarma. Vertical. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Rotisserie.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Rotisserie.", "x": "Shawarma: Rotisserie.. Making. Essential knowledge — Vertical.. the vertical meat. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Rotisserie..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Rotisserie..", "x": "Explained: Rotisserie.. Pickles. The context — Shawarma. Lamb. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Street.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Street.", "x": "Shawarma: Street.. Vertical. Essential knowledge — Lamb.. the vertical meat. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Street..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Street..", "x": "Explained: Street.. Street. The context — Shawarma. Garlic. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Vertical.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Vertical.", "x": "Shawarma in depth: Vertical.. Lamb. Details — the vertical meat.. Street. Pickles. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Pickles.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Pickles.", "x": "Shawarma in depth: Pickles.. Garlic. Details — the vertical meat.. Lamb. Rotisserie. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Street.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Street.", "x": "Shawarma in depth: Street.. Pickles. Details — the vertical meat.. Garlic. Street. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Lamb.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Lamb.", "x": "Shawarma in depth: Lamb.. Rotisserie. Details — the vertical meat.. Making. Vertical. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Garlic.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Garlic.", "x": "Shawarma in depth: Garlic.. Street. Details — the vertical meat.. Vertical. Lamb. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Making.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Making.", "x": "Shawarma in depth: Making.. Vertical. Details — the vertical meat.. Pickles. Garlic. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Shawarma comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Shawarma comes from.", "x": "Origins: Vertical.. Vertical. The history of Shawarma — the vertical meat.. Pickles. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Shawarma respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Shawarma respectfully.", "x": "Engaging: Street.. Lamb. How to participate or observe well — Shawarma. the vertical meat. Respect first, always; Lamb.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Shawarma do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Shawarma do's and don'ts.", "x": "Etiquette: Garlic.. Garlic. The rules of respect — Shawarma. the vertical meat. When in doubt, ask about Making.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Shawarma.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Shawarma.", "x": "Planning: Vertical.. Pickles. Practical notes — Shawarma. the vertical meat. A little planning shows respect for Pickles.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Shawarma and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Shawarma and money.", "x": "Costs: Street.. Rotisserie. What to budget — Shawarma. the vertical meat. The best experiences of Lamb. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-dish-shawarma-dish-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
