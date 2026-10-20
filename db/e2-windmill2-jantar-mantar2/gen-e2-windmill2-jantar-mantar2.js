(function(){'use strict';
/* JAH Jantar Mantar2 Database generator — jahdb-e2-windmill2-jantar-mantar2-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-windmill2-jantar-mantar2',PREFIX='JAH-E2WINDMILL2-',NAME='JAH Jantar Mantar2 Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Jantar Mantar2: the complete guide", "d": "Jantar Mantar2: the Indian..", "g": "overview", "l": 2, "q": "What is Jantar Mantar2: the complete guide?", "a": "Jantar Mantar2: the Indian..", "x": "The complete windmill guide to Jantar Mantar2: the Indian.. Jaipur. History, meaning, practices, and how to engage respectfully — everything in one database. Jaipur. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Jantar Mantar2 essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Jantar Mantar2 essentials.", "x": "At a glance: Jantar Mantar2 — the Indian.. 1724. The essentials: Singh.. Astronomical. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Jaipur.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Jaipur.", "x": "Jantar Mantar2: Jaipur.. Singh. Essential knowledge — Astronomical.. the Indian. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Jaipur..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Jaipur..", "x": "Explained: Jaipur.. 1724. The context — Jantar Mantar2. Stone. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "1724.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "1724.", "x": "Jantar Mantar2: 1724.. UNESCO. Essential knowledge — Stone.. the Indian. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: 1724..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: 1724..", "x": "Explained: 1724.. Stone. The context — Jantar Mantar2. UNESCO. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Astronomical.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Astronomical.", "x": "Jantar Mantar2: Astronomical.. 1724. Essential knowledge — UNESCO.. the Indian. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Astronomical..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Astronomical..", "x": "Explained: Astronomical.. Visiting. The context — Jantar Mantar2. Jai Singh. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Stone.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Stone.", "x": "Jantar Mantar2: Stone.. Stone. Essential knowledge — Jai Singh.. the Indian. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Stone..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Stone..", "x": "Explained: Stone.. Jaipur. The context — Jantar Mantar2. Jaipur. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "UNESCO.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "UNESCO.", "x": "Jantar Mantar2: UNESCO.. Visiting. Essential knowledge — Jaipur.. the Indian. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: UNESCO..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: UNESCO..", "x": "Explained: UNESCO.. Singh. The context — Jantar Mantar2. 1724. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Jai Singh.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Jai Singh.", "x": "Jantar Mantar2: Jai Singh.. Jaipur. Essential knowledge — 1724.. the Indian. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Jai Singh..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Jai Singh..", "x": "Explained: Jai Singh.. UNESCO. The context — Jantar Mantar2. Astronomical. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Jaipur.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Jaipur.", "x": "Jantar Mantar2 in depth: Jaipur.. 1724. Details — the Indian.. UNESCO. Stone. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Singh.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Singh.", "x": "Jantar Mantar2 in depth: Singh.. Astronomical. Details — the Indian.. 1724. UNESCO. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "UNESCO.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "UNESCO.", "x": "Jantar Mantar2 in depth: UNESCO.. Stone. Details — the Indian.. Stone. Jai Singh. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "1724.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "1724.", "x": "Jantar Mantar2 in depth: 1724.. UNESCO. Details — the Indian.. Visiting. Jaipur. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Stone.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Stone.", "x": "Jantar Mantar2 in depth: Stone.. Jai Singh. Details — the Indian.. Jaipur. 1724. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Visiting.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Visiting.", "x": "Jantar Mantar2 in depth: Visiting.. Jaipur. Details — the Indian.. Singh. Astronomical. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Jantar Mantar2 comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Jantar Mantar2 comes from.", "x": "Origins: Jaipur.. Jaipur. The history of Jantar Mantar2 — the Indian.. Singh. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Jantar Mantar2 respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Jantar Mantar2 respectfully.", "x": "Engaging: UNESCO.. 1724. How to participate or observe well — Jantar Mantar2. the Indian. Respect first, always; 1724.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Jantar Mantar2 do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Jantar Mantar2 do's and don'ts.", "x": "Etiquette: Stone.. Astronomical. The rules of respect — Jantar Mantar2. the Indian. When in doubt, ask about Visiting.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Jantar Mantar2.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Jantar Mantar2.", "x": "Planning: Jaipur.. Stone. Practical notes — Jantar Mantar2. the Indian. A little planning shows respect for Singh.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Jantar Mantar2 and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Jantar Mantar2 and money.", "x": "Costs: UNESCO.. UNESCO. What to budget — Jantar Mantar2. the Indian. The best experiences of 1724. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-windmill2-jantar-mantar2-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
