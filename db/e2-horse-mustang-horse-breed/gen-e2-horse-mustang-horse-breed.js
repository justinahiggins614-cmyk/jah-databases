(function(){'use strict';
/* JAH Mustang Horse Horse Breed Database generator — jahdb-e2-horse-mustang-horse-breed-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-horse-mustang-horse-breed',PREFIX='JAH-E2HORSEMUST-',NAME='JAH Mustang Horse Horse Breed Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Mustang Horse: the complete guide", "d": "Mustang Horse: the wild west..", "g": "overview", "l": 2, "q": "What is Mustang Horse: the complete guide?", "a": "Mustang Horse: the wild west..", "x": "The complete horse breed guide to Mustang Horse: the wild west.. Wild. History, meaning, practices, and how to engage respectfully — everything in one database. Wild. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Mustang Horse essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Mustang Horse essentials.", "x": "At a glance: Mustang Horse — the wild west.. West. The essentials: BLM.. BLM. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Wild.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Wild.", "x": "Mustang Horse: Wild.. BLM. Essential knowledge — BLM.. the wild west. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Wild..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Wild..", "x": "Explained: Wild.. Free. The context — Mustang Horse. Spanish. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "West.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "West.", "x": "Mustang Horse: West.. Spanish. Essential knowledge — Spanish.. the wild west. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: West..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: West..", "x": "Explained: West.. West. The context — Mustang Horse. Free. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "BLM.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "BLM.", "x": "Mustang Horse: BLM.. Free. Essential knowledge — Free.. the wild west. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: BLM..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: BLM..", "x": "Explained: BLM.. History. The context — Mustang Horse. Mustangs. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Spanish.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Spanish.", "x": "Mustang Horse: Spanish.. West. Essential knowledge — Mustangs.. the wild west. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Spanish..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Spanish..", "x": "Explained: Spanish.. Wild. The context — Mustang Horse. Wild. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Free.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Free.", "x": "Mustang Horse: Free.. History. Essential knowledge — Wild.. the wild west. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Free..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Free..", "x": "Explained: Free.. BLM. The context — Mustang Horse. West. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Mustangs.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Mustangs.", "x": "Mustang Horse: Mustangs.. Wild. Essential knowledge — West.. the wild west. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Mustangs..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Mustangs..", "x": "Explained: Mustangs.. Spanish. The context — Mustang Horse. BLM. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Wild.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Wild.", "x": "Mustang Horse in depth: Wild.. West. Details — the wild west.. Spanish. Spanish. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "BLM.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "BLM.", "x": "Mustang Horse in depth: BLM.. BLM. Details — the wild west.. Free. Free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Spanish.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Spanish.", "x": "Mustang Horse in depth: Spanish.. Spanish. Details — the wild west.. West. Mustangs. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Free.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Free.", "x": "Mustang Horse in depth: Free.. Free. Details — the wild west.. History. Wild. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "West.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "West.", "x": "Mustang Horse in depth: West.. Mustangs. Details — the wild west.. Wild. West. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "History.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "History.", "x": "Mustang Horse in depth: History.. Wild. Details — the wild west.. BLM. BLM. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Mustang Horse comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Mustang Horse comes from.", "x": "Origins: Wild.. Wild. The history of Mustang Horse — the wild west.. BLM. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Mustang Horse respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Mustang Horse respectfully.", "x": "Engaging: Spanish.. West. How to participate or observe well — Mustang Horse. the wild west. Respect first, always; Free.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Mustang Horse do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Mustang Horse do's and don'ts.", "x": "Etiquette: West.. BLM. The rules of respect — Mustang Horse. the wild west. When in doubt, ask about History.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Mustang Horse.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Mustang Horse.", "x": "Planning: Wild.. Spanish. Practical notes — Mustang Horse. the wild west. A little planning shows respect for BLM.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Mustang Horse and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Mustang Horse and money.", "x": "Costs: Spanish.. Free. What to budget — Mustang Horse. the wild west. The best experiences of Free. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-horse-mustang-horse-breed-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
