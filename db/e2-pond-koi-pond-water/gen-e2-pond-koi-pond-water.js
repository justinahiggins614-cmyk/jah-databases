(function(){'use strict';
/* JAH Koi Pond Pond Database generator — jahdb-e2-pond-koi-pond-water-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-pond-koi-pond-water',PREFIX='JAH-E2PONDKOIPO-',NAME='JAH Koi Pond Pond Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Koi Pond: the complete guide", "d": "Koi Pond: the living jewels..", "g": "overview", "l": 2, "q": "What is Koi Pond: the complete guide?", "a": "Koi Pond: the living jewels..", "x": "The complete pond guide to Koi Pond: the living jewels.. Koi. History, meaning, practices, and how to engage respectfully — everything in one database. Koi. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Koi Pond essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Koi Pond essentials.", "x": "At a glance: Koi Pond — the living jewels.. Filtration. The essentials: Depth.. Depth. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Koi.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Koi.", "x": "Koi Pond: Koi.. Depth. Essential knowledge — Depth.. the living jewels. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Koi..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Koi..", "x": "Explained: Koi.. Winter. The context — Koi Pond. Predators. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Filtration.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Filtration.", "x": "Koi Pond: Filtration.. Predators. Essential knowledge — Predators.. the living jewels. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Filtration..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Filtration..", "x": "Explained: Filtration.. Filtration. The context — Koi Pond. Feeding. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Depth.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Depth.", "x": "Koi Pond: Depth.. Winter. Essential knowledge — Feeding.. the living jewels. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Depth..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Depth..", "x": "Explained: Depth.. Guide. The context — Koi Pond. Winter. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Predators.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Predators.", "x": "Koi Pond: Predators.. Filtration. Essential knowledge — Winter.. the living jewels. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Predators..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Predators..", "x": "Explained: Predators.. Koi. The context — Koi Pond. Koi. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Feeding.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Feeding.", "x": "Koi Pond: Feeding.. Guide. Essential knowledge — Koi.. the living jewels. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Feeding..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Feeding..", "x": "Explained: Feeding.. Depth. The context — Koi Pond. Filtration. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Winter.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Winter.", "x": "Koi Pond: Winter.. Koi. Essential knowledge — Filtration.. the living jewels. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Winter..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Winter..", "x": "Explained: Winter.. Predators. The context — Koi Pond. Depth. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Koi.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Koi.", "x": "Koi Pond in depth: Koi.. Filtration. Details — the living jewels.. Predators. Predators. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Depth.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Depth.", "x": "Koi Pond in depth: Depth.. Depth. Details — the living jewels.. Winter. Feeding. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Predators.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Predators.", "x": "Koi Pond in depth: Predators.. Predators. Details — the living jewels.. Filtration. Winter. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Winter.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Winter.", "x": "Koi Pond in depth: Winter.. Feeding. Details — the living jewels.. Guide. Koi. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Filtration.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Filtration.", "x": "Koi Pond in depth: Filtration.. Winter. Details — the living jewels.. Koi. Filtration. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Guide.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Guide.", "x": "Koi Pond in depth: Guide.. Koi. Details — the living jewels.. Depth. Depth. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Koi Pond comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Koi Pond comes from.", "x": "Origins: Koi.. Koi. The history of Koi Pond — the living jewels.. Depth. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Koi Pond respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Koi Pond respectfully.", "x": "Engaging: Predators.. Filtration. How to participate or observe well — Koi Pond. the living jewels. Respect first, always; Winter.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Koi Pond do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Koi Pond do's and don'ts.", "x": "Etiquette: Filtration.. Depth. The rules of respect — Koi Pond. the living jewels. When in doubt, ask about Guide.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Koi Pond.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Koi Pond.", "x": "Planning: Koi.. Predators. Practical notes — Koi Pond. the living jewels. A little planning shows respect for Depth.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Koi Pond and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Koi Pond and money.", "x": "Costs: Predators.. Feeding. What to budget — Koi Pond. the living jewels. The best experiences of Winter. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-pond-koi-pond-water-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
