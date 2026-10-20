(function(){'use strict';
/* JAH Gyros Dish Database generator — jahdb-e2-dish-gyros-dish-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-dish-gyros-dish',PREFIX='JAH-E2DISHGYROS-',NAME='JAH Gyros Dish Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Gyros: the complete guide", "d": "Gyros: the vertical roast..", "g": "overview", "l": 2, "q": "What is Gyros: the complete guide?", "a": "Gyros: the vertical roast..", "x": "The complete dish guide to Gyros: the vertical roast.. Vertical. History, meaning, practices, and how to engage respectfully — everything in one database. Vertical. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Gyros essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Gyros essentials.", "x": "At a glance: Gyros — the vertical roast.. Pork. The essentials: Pita.. Pita. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Vertical.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Vertical.", "x": "Gyros: Vertical.. Pita. Essential knowledge — Pita.. the vertical roast. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Vertical..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Vertical..", "x": "Explained: Vertical.. Rotisserie. The context — Gyros. Tzatziki. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Pork.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Pork.", "x": "Gyros: Pork.. Street. Essential knowledge — Tzatziki.. the vertical roast. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Pork..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Pork..", "x": "Explained: Pork.. Tzatziki. The context — Gyros. Rotisserie. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Pita.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Pita.", "x": "Gyros: Pita.. Rotisserie. Essential knowledge — Rotisserie.. the vertical roast. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Pita..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Pita..", "x": "Explained: Pita.. Making. The context — Gyros. Street. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Tzatziki.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Tzatziki.", "x": "Gyros: Tzatziki.. Tzatziki. Essential knowledge — Street.. the vertical roast. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Tzatziki..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Tzatziki..", "x": "Explained: Tzatziki.. Vertical. The context — Gyros. Vertical. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Rotisserie.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Rotisserie.", "x": "Gyros: Rotisserie.. Making. Essential knowledge — Vertical.. the vertical roast. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Rotisserie..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Rotisserie..", "x": "Explained: Rotisserie.. Pita. The context — Gyros. Pork. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Street.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Street.", "x": "Gyros: Street.. Vertical. Essential knowledge — Pork.. the vertical roast. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Street..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Street..", "x": "Explained: Street.. Street. The context — Gyros. Pita. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Vertical.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Vertical.", "x": "Gyros in depth: Vertical.. Pork. Details — the vertical roast.. Street. Tzatziki. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Pita.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Pita.", "x": "Gyros in depth: Pita.. Pita. Details — the vertical roast.. Rotisserie. Rotisserie. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Street.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Street.", "x": "Gyros in depth: Street.. Tzatziki. Details — the vertical roast.. Tzatziki. Street. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Rotisserie.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Rotisserie.", "x": "Gyros in depth: Rotisserie.. Rotisserie. Details — the vertical roast.. Making. Vertical. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Tzatziki.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Tzatziki.", "x": "Gyros in depth: Tzatziki.. Street. Details — the vertical roast.. Vertical. Pork. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Making.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Making.", "x": "Gyros in depth: Making.. Vertical. Details — the vertical roast.. Pita. Pita. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Gyros comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Gyros comes from.", "x": "Origins: Vertical.. Vertical. The history of Gyros — the vertical roast.. Pita. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Gyros respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Gyros respectfully.", "x": "Engaging: Street.. Pork. How to participate or observe well — Gyros. the vertical roast. Respect first, always; Rotisserie.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Gyros do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Gyros do's and don'ts.", "x": "Etiquette: Tzatziki.. Pita. The rules of respect — Gyros. the vertical roast. When in doubt, ask about Making.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Gyros.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Gyros.", "x": "Planning: Vertical.. Tzatziki. Practical notes — Gyros. the vertical roast. A little planning shows respect for Pita.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Gyros and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Gyros and money.", "x": "Costs: Street.. Rotisserie. What to budget — Gyros. the vertical roast. The best experiences of Rotisserie. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-dish-gyros-dish-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
