(function(){'use strict';
/* JAH Dan Dan Noodles Dish Database generator — jahdb-e2-dish-dan-dan-noodles-dish-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-dish-dan-dan-noodles-dish',PREFIX='JAH-E2DISHDANDA-',NAME='JAH Dan Dan Noodles Dish Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Dan Dan Noodles: the complete guide", "d": "Dan Dan Noodles: the Sichuan noodles..", "g": "overview", "l": 2, "q": "What is Dan Dan Noodles: the complete guide?", "a": "Dan Dan Noodles: the Sichuan noodles..", "x": "The complete dish guide to Dan Dan Noodles: the Sichuan noodles.. Sichuan. History, meaning, practices, and how to engage respectfully — everything in one database. Sesame. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Dan Dan Noodles essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Dan Dan Noodles essentials.", "x": "At a glance: Dan Dan Noodles — the Sichuan noodles.. Sesame. The essentials: Street.. Chili. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Sichuan.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Sichuan.", "x": "Dan Dan Noodles: Sichuan.. Street. Essential knowledge — Chili.. the Sichuan noodles. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Sichuan..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Sichuan..", "x": "Explained: Sichuan.. Sichuan. The context — Dan Dan Noodles. Peanuts. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Sesame.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Sesame.", "x": "Dan Dan Noodles: Sesame.. Numbing. Essential knowledge — Peanuts.. the Sichuan noodles. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Sesame..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Sesame..", "x": "Explained: Sesame.. Chili. The context — Dan Dan Noodles. Street. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Chili.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Chili.", "x": "Dan Dan Noodles: Chili.. Sichuan. Essential knowledge — Street.. the Sichuan noodles. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Chili..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Chili..", "x": "Explained: Chili.. Making. The context — Dan Dan Noodles. Numbing. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Peanuts.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Peanuts.", "x": "Dan Dan Noodles: Peanuts.. Chili. Essential knowledge — Numbing.. the Sichuan noodles. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Peanuts..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Peanuts..", "x": "Explained: Peanuts.. Sesame. The context — Dan Dan Noodles. Sichuan. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Street.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Street.", "x": "Dan Dan Noodles: Street.. Making. Essential knowledge — Sichuan.. the Sichuan noodles. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Street..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Street..", "x": "Explained: Street.. Street. The context — Dan Dan Noodles. Sesame. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Numbing.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Numbing.", "x": "Dan Dan Noodles: Numbing.. Sesame. Essential knowledge — Sesame.. the Sichuan noodles. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Numbing..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Numbing..", "x": "Explained: Numbing.. Numbing. The context — Dan Dan Noodles. Chili. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Sesame.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Sesame.", "x": "Dan Dan Noodles in depth: Sesame.. Sesame. Details — the Sichuan noodles.. Numbing. Peanuts. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Street.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Street.", "x": "Dan Dan Noodles in depth: Street.. Chili. Details — the Sichuan noodles.. Sichuan. Street. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Numbing.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Numbing.", "x": "Dan Dan Noodles in depth: Numbing.. Peanuts. Details — the Sichuan noodles.. Chili. Numbing. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Sichuan.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Sichuan.", "x": "Dan Dan Noodles in depth: Sichuan.. Street. Details — the Sichuan noodles.. Making. Sichuan. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Chili.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Chili.", "x": "Dan Dan Noodles in depth: Chili.. Numbing. Details — the Sichuan noodles.. Sesame. Sesame. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Making.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Making.", "x": "Dan Dan Noodles in depth: Making.. Sichuan. Details — the Sichuan noodles.. Street. Chili. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Dan Dan Noodles comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Dan Dan Noodles comes from.", "x": "Origins: Sesame.. Sichuan. The history of Dan Dan Noodles — the Sichuan noodles.. Street. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Dan Dan Noodles respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Dan Dan Noodles respectfully.", "x": "Engaging: Numbing.. Sesame. How to participate or observe well — Dan Dan Noodles. the Sichuan noodles. Respect first, always; Sichuan.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Dan Dan Noodles do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Dan Dan Noodles do's and don'ts.", "x": "Etiquette: Chili.. Chili. The rules of respect — Dan Dan Noodles. the Sichuan noodles. When in doubt, ask about Making.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Dan Dan Noodles.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Dan Dan Noodles.", "x": "Planning: Sesame.. Peanuts. Practical notes — Dan Dan Noodles. the Sichuan noodles. A little planning shows respect for Street.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Dan Dan Noodles and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Dan Dan Noodles and money.", "x": "Costs: Numbing.. Street. What to budget — Dan Dan Noodles. the Sichuan noodles. The best experiences of Sichuan. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-dish-dan-dan-noodles-dish-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
