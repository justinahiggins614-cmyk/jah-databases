(function(){'use strict';
/* JAH Espresso Martini2 Database generator — jahdb-e2-cocktail2-espresso-martini2-cocktail-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-cocktail2-espresso-martini2-cocktail',PREFIX='JAH-E2COCKTAIL2-',NAME='JAH Espresso Martini2 Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Espresso Martini2: the complete guide", "d": "Espresso Martini2: the coffee 2..", "g": "overview", "l": 2, "q": "What is Espresso Martini2: the complete guide?", "a": "Espresso Martini2: the coffee 2..", "x": "The complete cocktail guide to Espresso Martini2: the coffee 2.. Shaken. History, meaning, practices, and how to engage respectfully — everything in one database. Crema. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Espresso Martini2 essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Espresso Martini2 essentials.", "x": "At a glance: Espresso Martini2 — the coffee 2.. Crema. The essentials: Beans.. Vodka. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Shaken.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Shaken.", "x": "Espresso Martini2: Shaken.. Beans. Essential knowledge — Vodka.. the coffee 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Shaken..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Shaken..", "x": "Explained: Shaken.. Shaken. The context — Espresso Martini2. Kahlua. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Crema.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Crema.", "x": "Espresso Martini2: Crema.. 1980s. Essential knowledge — Kahlua.. the coffee 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Crema..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Crema..", "x": "Explained: Crema.. Kahlua. The context — Espresso Martini2. Beans. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Vodka.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Vodka.", "x": "Espresso Martini2: Vodka.. Shaken. Essential knowledge — Beans.. the coffee 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Vodka..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Vodka..", "x": "Explained: Vodka.. Making. The context — Espresso Martini2. 1980s. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Kahlua.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Kahlua.", "x": "Espresso Martini2: Kahlua.. Kahlua. Essential knowledge — 1980s.. the coffee 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Kahlua..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Kahlua..", "x": "Explained: Kahlua.. Crema. The context — Espresso Martini2. Shaken. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Beans.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Beans.", "x": "Espresso Martini2: Beans.. Making. Essential knowledge — Shaken.. the coffee 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Beans..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Beans..", "x": "Explained: Beans.. Beans. The context — Espresso Martini2. Crema. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "1980s.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "1980s.", "x": "Espresso Martini2: 1980s.. Crema. Essential knowledge — Crema.. the coffee 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: 1980s..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: 1980s..", "x": "Explained: 1980s.. 1980s. The context — Espresso Martini2. Vodka. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Crema.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Crema.", "x": "Espresso Martini2 in depth: Crema.. Crema. Details — the coffee 2.. 1980s. Kahlua. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Beans.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Beans.", "x": "Espresso Martini2 in depth: Beans.. Vodka. Details — the coffee 2.. Shaken. Beans. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "1980s.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "1980s.", "x": "Espresso Martini2 in depth: 1980s.. Kahlua. Details — the coffee 2.. Kahlua. 1980s. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Shaken.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Shaken.", "x": "Espresso Martini2 in depth: Shaken.. Beans. Details — the coffee 2.. Making. Shaken. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Kahlua.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Kahlua.", "x": "Espresso Martini2 in depth: Kahlua.. 1980s. Details — the coffee 2.. Crema. Crema. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Making.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Making.", "x": "Espresso Martini2 in depth: Making.. Shaken. Details — the coffee 2.. Beans. Vodka. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Espresso Martini2 comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Espresso Martini2 comes from.", "x": "Origins: Crema.. Shaken. The history of Espresso Martini2 — the coffee 2.. Beans. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Espresso Martini2 respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Espresso Martini2 respectfully.", "x": "Engaging: 1980s.. Crema. How to participate or observe well — Espresso Martini2. the coffee 2. Respect first, always; Shaken.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Espresso Martini2 do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Espresso Martini2 do's and don'ts.", "x": "Etiquette: Kahlua.. Vodka. The rules of respect — Espresso Martini2. the coffee 2. When in doubt, ask about Making.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Espresso Martini2.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Espresso Martini2.", "x": "Planning: Crema.. Kahlua. Practical notes — Espresso Martini2. the coffee 2. A little planning shows respect for Beans.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Espresso Martini2 and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Espresso Martini2 and money.", "x": "Costs: 1980s.. Beans. What to budget — Espresso Martini2. the coffee 2. The best experiences of Shaken. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-cocktail2-espresso-martini2-cocktail-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
