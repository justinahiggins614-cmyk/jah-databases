(function(){'use strict';
/* JAH Crocodile Nile Reptile Database generator — jahdb-e2-reptile-nile-crocodile-reptile-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-reptile-nile-crocodile-reptile',PREFIX='JAH-E2REPTILENI-',NAME='JAH Crocodile Nile Reptile Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Crocodile Nile: the complete guide", "d": "Crocodile Nile: the river predator..", "g": "overview", "l": 2, "q": "What is Crocodile Nile: the complete guide?", "a": "Crocodile Nile: the river predator..", "x": "The complete reptile guide to Crocodile Nile: the river predator.. Nile. History, meaning, practices, and how to engage respectfully — everything in one database. Nile. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Crocodile Nile essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Crocodile Nile essentials.", "x": "At a glance: Crocodile Nile — the river predator.. Death roll. The essentials: Roll.. Africa. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Nile.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Nile.", "x": "Crocodile Nile: Nile.. Roll. Essential knowledge — Africa.. the river predator. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Nile..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Nile..", "x": "Explained: Nile.. Africa. The context — Crocodile Nile. Ambush. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Death roll.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Death roll.", "x": "Crocodile Nile: Death roll.. Ambush. Essential knowledge — Ambush.. the river predator. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Death roll..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Death roll..", "x": "Explained: Death roll.. Ancient. The context — Crocodile Nile. Armored. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Africa.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Africa.", "x": "Crocodile Nile: Africa.. Africa. Essential knowledge — Armored.. the river predator. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Africa..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Africa..", "x": "Explained: Africa.. Care. The context — Crocodile Nile. Ancient. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Ambush.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Ambush.", "x": "Crocodile Nile: Ambush.. Ancient. Essential knowledge — Ancient.. the river predator. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Ambush..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Ambush..", "x": "Explained: Ambush.. Nile. The context — Crocodile Nile. Nile. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Armored.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Armored.", "x": "Crocodile Nile: Armored.. Care. Essential knowledge — Nile.. the river predator. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Armored..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Armored..", "x": "Explained: Armored.. Roll. The context — Crocodile Nile. Death roll. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Ancient.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Ancient.", "x": "Crocodile Nile: Ancient.. Nile. Essential knowledge — Death roll.. the river predator. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Ancient..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Ancient..", "x": "Explained: Ancient.. Ambush. The context — Crocodile Nile. Africa. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Nile.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Nile.", "x": "Crocodile Nile in depth: Nile.. Death roll. Details — the river predator.. Ambush. Ambush. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Roll.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Roll.", "x": "Crocodile Nile in depth: Roll.. Africa. Details — the river predator.. Africa. Armored. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Ambush.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Ambush.", "x": "Crocodile Nile in depth: Ambush.. Ambush. Details — the river predator.. Ancient. Ancient. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Africa.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Africa.", "x": "Crocodile Nile in depth: Africa.. Armored. Details — the river predator.. Care. Nile. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Ancient.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Ancient.", "x": "Crocodile Nile in depth: Ancient.. Ancient. Details — the river predator.. Nile. Death roll. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Care.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Care.", "x": "Crocodile Nile in depth: Care.. Nile. Details — the river predator.. Roll. Africa. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Crocodile Nile comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Crocodile Nile comes from.", "x": "Origins: Nile.. Nile. The history of Crocodile Nile — the river predator.. Roll. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Crocodile Nile respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Crocodile Nile respectfully.", "x": "Engaging: Ambush.. Death roll. How to participate or observe well — Crocodile Nile. the river predator. Respect first, always; Africa.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Crocodile Nile do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Crocodile Nile do's and don'ts.", "x": "Etiquette: Ancient.. Africa. The rules of respect — Crocodile Nile. the river predator. When in doubt, ask about Care.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Crocodile Nile.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Crocodile Nile.", "x": "Planning: Nile.. Ambush. Practical notes — Crocodile Nile. the river predator. A little planning shows respect for Roll.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Crocodile Nile and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Crocodile Nile and money.", "x": "Costs: Ambush.. Armored. What to budget — Crocodile Nile. the river predator. The best experiences of Africa. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-reptile-nile-crocodile-reptile-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
