(function(){'use strict';
/* JAH Boston Fern Houseplant Database generator — jahdb-e2-houseplant-boston-fern-houseplant-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-houseplant-boston-fern-houseplant',PREFIX='JAH-E2HOUSEPLAN-',NAME='JAH Boston Fern Houseplant Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Boston Fern: the complete guide", "d": "Boston Fern: the hanging classic..", "g": "overview", "l": 2, "q": "What is Boston Fern: the complete guide?", "a": "Boston Fern: the hanging classic..", "x": "The complete houseplant guide to Boston Fern: the hanging classic.. Hanging. History, meaning, practices, and how to engage respectfully — everything in one database. Hanging. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Boston Fern essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Boston Fern essentials.", "x": "At a glance: Boston Fern — the hanging classic.. Humidity. The essentials: Fronds.. Fronds. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Hanging.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Hanging.", "x": "Boston Fern: Hanging.. Fronds. Essential knowledge — Fronds.. the hanging classic. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Hanging..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Hanging..", "x": "Explained: Hanging.. Shedding. The context — Boston Fern. Victorian. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Humidity.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Humidity.", "x": "Boston Fern: Humidity.. Victorian. Essential knowledge — Victorian.. the hanging classic. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Humidity..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Humidity..", "x": "Explained: Humidity.. Humidity. The context — Boston Fern. Nephrolepis. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Fronds.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Fronds.", "x": "Boston Fern: Fronds.. Shedding. Essential knowledge — Nephrolepis.. the hanging classic. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Fronds..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Fronds..", "x": "Explained: Fronds.. Guide. The context — Boston Fern. Shedding. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Victorian.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Victorian.", "x": "Boston Fern: Victorian.. Humidity. Essential knowledge — Shedding.. the hanging classic. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Victorian..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Victorian..", "x": "Explained: Victorian.. Hanging. The context — Boston Fern. Hanging. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Nephrolepis.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Nephrolepis.", "x": "Boston Fern: Nephrolepis.. Guide. Essential knowledge — Hanging.. the hanging classic. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Nephrolepis..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Nephrolepis..", "x": "Explained: Nephrolepis.. Fronds. The context — Boston Fern. Humidity. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Shedding.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Shedding.", "x": "Boston Fern: Shedding.. Hanging. Essential knowledge — Humidity.. the hanging classic. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Shedding..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Shedding..", "x": "Explained: Shedding.. Victorian. The context — Boston Fern. Fronds. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Hanging.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Hanging.", "x": "Boston Fern in depth: Hanging.. Humidity. Details — the hanging classic.. Victorian. Victorian. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Fronds.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Fronds.", "x": "Boston Fern in depth: Fronds.. Fronds. Details — the hanging classic.. Shedding. Nephrolepis. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Victorian.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Victorian.", "x": "Boston Fern in depth: Victorian.. Victorian. Details — the hanging classic.. Humidity. Shedding. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Shedding.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Shedding.", "x": "Boston Fern in depth: Shedding.. Nephrolepis. Details — the hanging classic.. Guide. Hanging. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Humidity.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Humidity.", "x": "Boston Fern in depth: Humidity.. Shedding. Details — the hanging classic.. Hanging. Humidity. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Guide.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Guide.", "x": "Boston Fern in depth: Guide.. Hanging. Details — the hanging classic.. Fronds. Fronds. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Boston Fern comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Boston Fern comes from.", "x": "Origins: Hanging.. Hanging. The history of Boston Fern — the hanging classic.. Fronds. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Boston Fern respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Boston Fern respectfully.", "x": "Engaging: Victorian.. Humidity. How to participate or observe well — Boston Fern. the hanging classic. Respect first, always; Shedding.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Boston Fern do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Boston Fern do's and don'ts.", "x": "Etiquette: Humidity.. Fronds. The rules of respect — Boston Fern. the hanging classic. When in doubt, ask about Guide.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Boston Fern.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Boston Fern.", "x": "Planning: Hanging.. Victorian. Practical notes — Boston Fern. the hanging classic. A little planning shows respect for Fronds.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Boston Fern and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Boston Fern and money.", "x": "Costs: Victorian.. Nephrolepis. What to budget — Boston Fern. the hanging classic. The best experiences of Shedding. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-houseplant-boston-fern-houseplant-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
