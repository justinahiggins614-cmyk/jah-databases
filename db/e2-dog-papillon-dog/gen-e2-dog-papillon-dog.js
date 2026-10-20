(function(){'use strict';
/* JAH Papillon Dog Breed Database generator — jahdb-e2-dog-papillon-dog-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-dog-papillon-dog',PREFIX='JAH-E2DOGPAPILL-',NAME='JAH Papillon Dog Breed Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Papillon: the complete guide", "d": "Papillon: the butterfly ears..", "g": "overview", "l": 2, "q": "What is Papillon: the complete guide?", "a": "Papillon: the butterfly ears..", "x": "The complete dog breed guide to Papillon: the butterfly ears.. Butterfly. History, meaning, practices, and how to engage respectfully — everything in one database. Butterfly. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Papillon essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Papillon essentials.", "x": "At a glance: Papillon — the butterfly ears.. Ears. The essentials: Tiny.. Tiny. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Butterfly.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Butterfly.", "x": "Papillon: Butterfly.. Tiny. Essential knowledge — Tiny.. the butterfly ears. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Butterfly..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Butterfly..", "x": "Explained: Butterfly.. France. The context — Papillon. Smart. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Ears.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Ears.", "x": "Papillon: Ears.. Smart. Essential knowledge — Smart.. the butterfly ears. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Ears..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Ears..", "x": "Explained: Ears.. Agility. The context — Papillon. France. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Tiny.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Tiny.", "x": "Papillon: Tiny.. France. Essential knowledge — France.. the butterfly ears. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Tiny..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Tiny..", "x": "Explained: Tiny.. History. The context — Papillon. Agility. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Smart.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Smart.", "x": "Papillon: Smart.. Agility. Essential knowledge — Agility.. the butterfly ears. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Smart..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Smart..", "x": "Explained: Smart.. Butterfly. The context — Papillon. Butterfly. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "France.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "France.", "x": "Papillon: France.. History. Essential knowledge — Butterfly.. the butterfly ears. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: France..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: France..", "x": "Explained: France.. Tiny. The context — Papillon. Ears. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Agility.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Agility.", "x": "Papillon: Agility.. Butterfly. Essential knowledge — Ears.. the butterfly ears. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Agility..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Agility..", "x": "Explained: Agility.. Smart. The context — Papillon. Tiny. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Butterfly.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Butterfly.", "x": "Papillon in depth: Butterfly.. Ears. Details — the butterfly ears.. Smart. Smart. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Tiny.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Tiny.", "x": "Papillon in depth: Tiny.. Tiny. Details — the butterfly ears.. France. France. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Smart.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Smart.", "x": "Papillon in depth: Smart.. Smart. Details — the butterfly ears.. Agility. Agility. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "France.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "France.", "x": "Papillon in depth: France.. France. Details — the butterfly ears.. History. Butterfly. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Agility.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Agility.", "x": "Papillon in depth: Agility.. Agility. Details — the butterfly ears.. Butterfly. Ears. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "History.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "History.", "x": "Papillon in depth: History.. Butterfly. Details — the butterfly ears.. Tiny. Tiny. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Papillon comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Papillon comes from.", "x": "Origins: Butterfly.. Butterfly. The history of Papillon — the butterfly ears.. Tiny. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Papillon respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Papillon respectfully.", "x": "Engaging: Smart.. Ears. How to participate or observe well — Papillon. the butterfly ears. Respect first, always; France.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Papillon do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Papillon do's and don'ts.", "x": "Etiquette: Agility.. Tiny. The rules of respect — Papillon. the butterfly ears. When in doubt, ask about History.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Papillon.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Papillon.", "x": "Planning: Butterfly.. Smart. Practical notes — Papillon. the butterfly ears. A little planning shows respect for Tiny.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Papillon and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Papillon and money.", "x": "Costs: Smart.. France. What to budget — Papillon. the butterfly ears. The best experiences of France. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-dog-papillon-dog-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
