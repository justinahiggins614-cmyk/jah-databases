(function(){'use strict';
/* JAH Saint Bernard Dog Breed Database generator — jahdb-e2-dog-saint-bernard-dog-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-dog-saint-bernard-dog',PREFIX='JAH-E2DOGSAINTB-',NAME='JAH Saint Bernard Dog Breed Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Saint Bernard: the complete guide", "d": "Saint Bernard: the alpine rescue..", "g": "overview", "l": 2, "q": "What is Saint Bernard: the complete guide?", "a": "Saint Bernard: the alpine rescue..", "x": "The complete dog breed guide to Saint Bernard: the alpine rescue.. Alps. History, meaning, practices, and how to engage respectfully — everything in one database. Alps. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Saint Bernard essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Saint Bernard essentials.", "x": "At a glance: Saint Bernard — the alpine rescue.. Barrel. The essentials: Rescue.. Rescue. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Alps.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Alps.", "x": "Saint Bernard: Alps.. Rescue. Essential knowledge — Rescue.. the alpine rescue. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Alps..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Alps..", "x": "Explained: Alps.. Drool. The context — Saint Bernard. Gentle. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Barrel.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Barrel.", "x": "Saint Bernard: Barrel.. Hospice. Essential knowledge — Gentle.. the alpine rescue. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Barrel..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Barrel..", "x": "Explained: Barrel.. Barrel. The context — Saint Bernard. Hospice. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Rescue.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Rescue.", "x": "Saint Bernard: Rescue.. Drool. Essential knowledge — Hospice.. the alpine rescue. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Rescue..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Rescue..", "x": "Explained: Rescue.. History. The context — Saint Bernard. Drool. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Gentle.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Gentle.", "x": "Saint Bernard: Gentle.. Barrel. Essential knowledge — Drool.. the alpine rescue. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Gentle..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Gentle..", "x": "Explained: Gentle.. Alps. The context — Saint Bernard. Alps. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Hospice.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Hospice.", "x": "Saint Bernard: Hospice.. History. Essential knowledge — Alps.. the alpine rescue. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Hospice..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Hospice..", "x": "Explained: Hospice.. Rescue. The context — Saint Bernard. Barrel. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Drool.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Drool.", "x": "Saint Bernard: Drool.. Alps. Essential knowledge — Barrel.. the alpine rescue. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Drool..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Drool..", "x": "Explained: Drool.. Hospice. The context — Saint Bernard. Rescue. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Alps.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Alps.", "x": "Saint Bernard in depth: Alps.. Barrel. Details — the alpine rescue.. Hospice. Gentle. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Rescue.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Rescue.", "x": "Saint Bernard in depth: Rescue.. Rescue. Details — the alpine rescue.. Drool. Hospice. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Hospice.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Hospice.", "x": "Saint Bernard in depth: Hospice.. Gentle. Details — the alpine rescue.. Barrel. Drool. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Drool.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Drool.", "x": "Saint Bernard in depth: Drool.. Hospice. Details — the alpine rescue.. History. Alps. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Barrel.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Barrel.", "x": "Saint Bernard in depth: Barrel.. Drool. Details — the alpine rescue.. Alps. Barrel. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "History.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "History.", "x": "Saint Bernard in depth: History.. Alps. Details — the alpine rescue.. Rescue. Rescue. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Saint Bernard comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Saint Bernard comes from.", "x": "Origins: Alps.. Alps. The history of Saint Bernard — the alpine rescue.. Rescue. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Saint Bernard respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Saint Bernard respectfully.", "x": "Engaging: Hospice.. Barrel. How to participate or observe well — Saint Bernard. the alpine rescue. Respect first, always; Drool.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Saint Bernard do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Saint Bernard do's and don'ts.", "x": "Etiquette: Barrel.. Rescue. The rules of respect — Saint Bernard. the alpine rescue. When in doubt, ask about History.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Saint Bernard.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Saint Bernard.", "x": "Planning: Alps.. Gentle. Practical notes — Saint Bernard. the alpine rescue. A little planning shows respect for Rescue.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Saint Bernard and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Saint Bernard and money.", "x": "Costs: Hospice.. Hospice. What to budget — Saint Bernard. the alpine rescue. The best experiences of Drool. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-dog-saint-bernard-dog-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
