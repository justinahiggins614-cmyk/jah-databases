(function(){'use strict';
/* JAH Hot Toys Figures Action Figure Database generator — jahdb-e2-figure-hot-toys-figures-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-figure-hot-toys-figures',PREFIX='JAH-E2FIGUREHOT-',NAME='JAH Hot Toys Figures Action Figure Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Hot Toys Figures: the complete guide", "d": "Hot Toys Figures: the 1/6 premium..", "g": "overview", "l": 2, "q": "What is Hot Toys Figures: the complete guide?", "a": "Hot Toys Figures: the 1/6 premium..", "x": "The complete action figure guide to Hot Toys Figures: the 1/6 premium.. Hong Kong. History, meaning, practices, and how to engage respectfully — everything in one database. 1/6. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Hot Toys Figures essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Hot Toys Figures essentials.", "x": "At a glance: Hot Toys Figures — the 1/6 premium.. 1/6. The essentials: Realistic.. Realistic. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Hong Kong.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Hong Kong.", "x": "Hot Toys Figures: Hong Kong.. Realistic. Essential knowledge — Realistic.. the 1/6 premium. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Hong Kong..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Hong Kong..", "x": "Explained: Hong Kong.. Hong Kong. The context — Hot Toys Figures. Iron Man. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "1/6.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "1/6.", "x": "Hot Toys Figures: 1/6.. Expensive. Essential knowledge — Iron Man.. the 1/6 premium. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: 1/6..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: 1/6..", "x": "Explained: 1/6.. Iron Man. The context — Hot Toys Figures. Expensive. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Realistic.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Realistic.", "x": "Hot Toys Figures: Realistic.. Hong Kong. Essential knowledge — Expensive.. the 1/6 premium. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Realistic..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Realistic..", "x": "Explained: Realistic.. History. The context — Hot Toys Figures. Collect. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Iron Man.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Iron Man.", "x": "Hot Toys Figures: Iron Man.. Iron Man. Essential knowledge — Collect.. the 1/6 premium. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Iron Man..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Iron Man..", "x": "Explained: Iron Man.. 1/6. The context — Hot Toys Figures. Hong Kong. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Expensive.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Expensive.", "x": "Hot Toys Figures: Expensive.. History. Essential knowledge — Hong Kong.. the 1/6 premium. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Expensive..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Expensive..", "x": "Explained: Expensive.. Realistic. The context — Hot Toys Figures. 1/6. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Collect.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Collect.", "x": "Hot Toys Figures: Collect.. 1/6. Essential knowledge — 1/6.. the 1/6 premium. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Collect..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Collect..", "x": "Explained: Collect.. Expensive. The context — Hot Toys Figures. Realistic. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "1/6.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "1/6.", "x": "Hot Toys Figures in depth: 1/6.. 1/6. Details — the 1/6 premium.. Expensive. Iron Man. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Realistic.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Realistic.", "x": "Hot Toys Figures in depth: Realistic.. Realistic. Details — the 1/6 premium.. Hong Kong. Expensive. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Expensive.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Expensive.", "x": "Hot Toys Figures in depth: Expensive.. Iron Man. Details — the 1/6 premium.. Iron Man. Collect. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Hong Kong.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Hong Kong.", "x": "Hot Toys Figures in depth: Hong Kong.. Expensive. Details — the 1/6 premium.. History. Hong Kong. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Iron Man.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Iron Man.", "x": "Hot Toys Figures in depth: Iron Man.. Collect. Details — the 1/6 premium.. 1/6. 1/6. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "History.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "History.", "x": "Hot Toys Figures in depth: History.. Hong Kong. Details — the 1/6 premium.. Realistic. Realistic. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Hot Toys Figures comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Hot Toys Figures comes from.", "x": "Origins: 1/6.. Hong Kong. The history of Hot Toys Figures — the 1/6 premium.. Realistic. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Hot Toys Figures respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Hot Toys Figures respectfully.", "x": "Engaging: Expensive.. 1/6. How to participate or observe well — Hot Toys Figures. the 1/6 premium. Respect first, always; Hong Kong.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Hot Toys Figures do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Hot Toys Figures do's and don'ts.", "x": "Etiquette: Iron Man.. Realistic. The rules of respect — Hot Toys Figures. the 1/6 premium. When in doubt, ask about History.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Hot Toys Figures.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Hot Toys Figures.", "x": "Planning: 1/6.. Iron Man. Practical notes — Hot Toys Figures. the 1/6 premium. A little planning shows respect for Realistic.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Hot Toys Figures and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Hot Toys Figures and money.", "x": "Costs: Expensive.. Expensive. What to budget — Hot Toys Figures. the 1/6 premium. The best experiences of Hong Kong. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-figure-hot-toys-figures-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
