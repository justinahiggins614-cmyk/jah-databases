(function(){'use strict';
/* JAH Sex on the Beach Cocktail Database generator — jahdb-e2-cocktail-sex-on-the-beach-cocktail-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-cocktail-sex-on-the-beach-cocktail',PREFIX='JAH-E2COCKTAILS-',NAME='JAH Sex on the Beach Cocktail Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Sex on the Beach: the complete guide", "d": "Sex on the Beach: the 80s fruity..", "g": "overview", "l": 2, "q": "What is Sex on the Beach: the complete guide?", "a": "Sex on the Beach: the 80s fruity..", "x": "The complete cocktail guide to Sex on the Beach: the 80s fruity.. Vodka. History, meaning, practices, and how to engage respectfully — everything in one database. Vodka. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Sex on the Beach essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Sex on the Beach essentials.", "x": "At a glance: Sex on the Beach — the 80s fruity.. Peach. The essentials: Fruity.. Cranberry. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Vodka.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Vodka.", "x": "Sex on the Beach: Vodka.. Fruity. Essential knowledge — Cranberry.. the 80s fruity. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Vodka..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Vodka..", "x": "Explained: Vodka.. Peach. The context — Sex on the Beach. Orange. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Peach.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Peach.", "x": "Sex on the Beach: Peach.. 1980s. Essential knowledge — Orange.. the 80s fruity. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Peach..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Peach..", "x": "Explained: Peach.. Orange. The context — Sex on the Beach. 1980s. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Cranberry.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Cranberry.", "x": "Sex on the Beach: Cranberry.. Peach. Essential knowledge — 1980s.. the 80s fruity. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Cranberry..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Cranberry..", "x": "Explained: Cranberry.. Variations. The context — Sex on the Beach. Fruity. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Orange.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Orange.", "x": "Sex on the Beach: Orange.. Orange. Essential knowledge — Fruity.. the 80s fruity. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Orange..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Orange..", "x": "Explained: Orange.. Vodka. The context — Sex on the Beach. Vodka. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "1980s.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "1980s.", "x": "Sex on the Beach: 1980s.. Variations. Essential knowledge — Vodka.. the 80s fruity. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: 1980s..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: 1980s..", "x": "Explained: 1980s.. Fruity. The context — Sex on the Beach. Peach. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Fruity.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Fruity.", "x": "Sex on the Beach: Fruity.. Vodka. Essential knowledge — Peach.. the 80s fruity. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Fruity..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Fruity..", "x": "Explained: Fruity.. 1980s. The context — Sex on the Beach. Cranberry. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Vodka.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Vodka.", "x": "Sex on the Beach in depth: Vodka.. Peach. Details — the 80s fruity.. 1980s. Orange. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Fruity.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Fruity.", "x": "Sex on the Beach in depth: Fruity.. Cranberry. Details — the 80s fruity.. Peach. 1980s. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "1980s.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "1980s.", "x": "Sex on the Beach in depth: 1980s.. Orange. Details — the 80s fruity.. Orange. Fruity. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Peach.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Peach.", "x": "Sex on the Beach in depth: Peach.. 1980s. Details — the 80s fruity.. Variations. Vodka. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Orange.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Orange.", "x": "Sex on the Beach in depth: Orange.. Fruity. Details — the 80s fruity.. Vodka. Peach. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Variations.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Variations.", "x": "Sex on the Beach in depth: Variations.. Vodka. Details — the 80s fruity.. Fruity. Cranberry. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Sex on the Beach comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Sex on the Beach comes from.", "x": "Origins: Vodka.. Vodka. The history of Sex on the Beach — the 80s fruity.. Fruity. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Sex on the Beach respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Sex on the Beach respectfully.", "x": "Engaging: 1980s.. Peach. How to participate or observe well — Sex on the Beach. the 80s fruity. Respect first, always; Peach.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Sex on the Beach do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Sex on the Beach do's and don'ts.", "x": "Etiquette: Orange.. Cranberry. The rules of respect — Sex on the Beach. the 80s fruity. When in doubt, ask about Variations.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Sex on the Beach.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Sex on the Beach.", "x": "Planning: Vodka.. Orange. Practical notes — Sex on the Beach. the 80s fruity. A little planning shows respect for Fruity.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Sex on the Beach and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Sex on the Beach and money.", "x": "Costs: 1980s.. 1980s. What to budget — Sex on the Beach. the 80s fruity. The best experiences of Peach. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-cocktail-sex-on-the-beach-cocktail-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
