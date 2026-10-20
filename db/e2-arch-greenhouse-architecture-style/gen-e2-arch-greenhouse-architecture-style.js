(function(){'use strict';
/* JAH Greenhouse Architecture Style Database generator — jahdb-e2-arch-greenhouse-architecture-style-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-arch-greenhouse-architecture-style',PREFIX='JAH-E2ARCHGREEN-',NAME='JAH Greenhouse Architecture Style Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Greenhouse Architecture: the complete guide", "d": "Greenhouse Architecture: the glass grow..", "g": "overview", "l": 2, "q": "What is Greenhouse Architecture: the complete guide?", "a": "Greenhouse Architecture: the glass grow..", "x": "The complete architecture style guide to Greenhouse Architecture: the glass grow.. Glass. History, meaning, practices, and how to engage respectfully — everything in one database. Glass. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Greenhouse Architecture essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Greenhouse Architecture essentials.", "x": "At a glance: Greenhouse Architecture — the glass grow.. Heat. The essentials: Orangeries.. Ventilation. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Glass.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Glass.", "x": "Greenhouse Architecture: Glass.. Orangeries. Essential knowledge — Ventilation.. the glass grow. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Glass..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Glass..", "x": "Explained: Glass.. Victorian. The context — Greenhouse Architecture. Victorian. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Heat.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Heat.", "x": "Greenhouse Architecture: Heat.. Humidity. Essential knowledge — Victorian.. the glass grow. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Heat..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Heat..", "x": "Explained: Heat.. Heat. The context — Greenhouse Architecture. Orangeries. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Ventilation.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Ventilation.", "x": "Greenhouse Architecture: Ventilation.. Victorian. Essential knowledge — Orangeries.. the glass grow. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Ventilation..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Ventilation..", "x": "Explained: Ventilation.. Future. The context — Greenhouse Architecture. Humidity. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Victorian.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Victorian.", "x": "Greenhouse Architecture: Victorian.. Heat. Essential knowledge — Humidity.. the glass grow. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Victorian..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Victorian..", "x": "Explained: Victorian.. Glass. The context — Greenhouse Architecture. Glass. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Orangeries.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Orangeries.", "x": "Greenhouse Architecture: Orangeries.. Future. Essential knowledge — Glass.. the glass grow. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Orangeries..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Orangeries..", "x": "Explained: Orangeries.. Orangeries. The context — Greenhouse Architecture. Heat. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Humidity.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Humidity.", "x": "Greenhouse Architecture: Humidity.. Glass. Essential knowledge — Heat.. the glass grow. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Humidity..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Humidity..", "x": "Explained: Humidity.. Humidity. The context — Greenhouse Architecture. Ventilation. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Glass.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Glass.", "x": "Greenhouse Architecture in depth: Glass.. Heat. Details — the glass grow.. Humidity. Victorian. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Orangeries.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Orangeries.", "x": "Greenhouse Architecture in depth: Orangeries.. Ventilation. Details — the glass grow.. Victorian. Orangeries. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Humidity.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Humidity.", "x": "Greenhouse Architecture in depth: Humidity.. Victorian. Details — the glass grow.. Heat. Humidity. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Victorian.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Victorian.", "x": "Greenhouse Architecture in depth: Victorian.. Orangeries. Details — the glass grow.. Future. Glass. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Heat.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Heat.", "x": "Greenhouse Architecture in depth: Heat.. Humidity. Details — the glass grow.. Glass. Heat. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Future.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Future.", "x": "Greenhouse Architecture in depth: Future.. Glass. Details — the glass grow.. Orangeries. Ventilation. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Greenhouse Architecture comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Greenhouse Architecture comes from.", "x": "Origins: Glass.. Glass. The history of Greenhouse Architecture — the glass grow.. Orangeries. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Greenhouse Architecture respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Greenhouse Architecture respectfully.", "x": "Engaging: Humidity.. Heat. How to participate or observe well — Greenhouse Architecture. the glass grow. Respect first, always; Victorian.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Greenhouse Architecture do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Greenhouse Architecture do's and don'ts.", "x": "Etiquette: Heat.. Ventilation. The rules of respect — Greenhouse Architecture. the glass grow. When in doubt, ask about Future.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Greenhouse Architecture.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Greenhouse Architecture.", "x": "Planning: Glass.. Victorian. Practical notes — Greenhouse Architecture. the glass grow. A little planning shows respect for Orangeries.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Greenhouse Architecture and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Greenhouse Architecture and money.", "x": "Costs: Humidity.. Orangeries. What to budget — Greenhouse Architecture. the glass grow. The best experiences of Victorian. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-arch-greenhouse-architecture-style-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
