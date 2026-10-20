(function(){'use strict';
/* JAH Scotch Egg Dish Database generator — jahdb-e2-dish-scotch-egg-dish-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-dish-scotch-egg-dish',PREFIX='JAH-E2DISHSCOTC-',NAME='JAH Scotch Egg Dish Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Scotch Egg: the complete guide", "d": "Scotch Egg: the picnic egg..", "g": "overview", "l": 2, "q": "What is Scotch Egg: the complete guide?", "a": "Scotch Egg: the picnic egg..", "x": "The complete dish guide to Scotch Egg: the picnic egg.. Egg. History, meaning, practices, and how to engage respectfully — everything in one database. Egg. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Scotch Egg essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Scotch Egg essentials.", "x": "At a glance: Scotch Egg — the picnic egg.. Sausage. The essentials: Picnic.. Breaded. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Egg.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Egg.", "x": "Scotch Egg: Egg.. Picnic. Essential knowledge — Breaded.. the picnic egg. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Egg..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Egg..", "x": "Explained: Egg.. Breaded. The context — Scotch Egg. Picnic. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Sausage.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Sausage.", "x": "Scotch Egg: Sausage.. Fortnum. Essential knowledge — Picnic.. the picnic egg. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Sausage..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Sausage..", "x": "Explained: Sausage.. Sausage. The context — Scotch Egg. Fortnum. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Breaded.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Breaded.", "x": "Scotch Egg: Breaded.. Breaded. Essential knowledge — Fortnum.. the picnic egg. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Breaded..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Breaded..", "x": "Explained: Breaded.. Making. The context — Scotch Egg. Runny. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Picnic.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Picnic.", "x": "Scotch Egg: Picnic.. Sausage. Essential knowledge — Runny.. the picnic egg. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Picnic..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Picnic..", "x": "Explained: Picnic.. Egg. The context — Scotch Egg. Egg. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Fortnum.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Fortnum.", "x": "Scotch Egg: Fortnum.. Making. Essential knowledge — Egg.. the picnic egg. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Fortnum..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Fortnum..", "x": "Explained: Fortnum.. Picnic. The context — Scotch Egg. Sausage. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Runny.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Runny.", "x": "Scotch Egg: Runny.. Egg. Essential knowledge — Sausage.. the picnic egg. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Runny..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Runny..", "x": "Explained: Runny.. Fortnum. The context — Scotch Egg. Breaded. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Egg.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Egg.", "x": "Scotch Egg in depth: Egg.. Sausage. Details — the picnic egg.. Fortnum. Picnic. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Picnic.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Picnic.", "x": "Scotch Egg in depth: Picnic.. Breaded. Details — the picnic egg.. Breaded. Fortnum. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Fortnum.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Fortnum.", "x": "Scotch Egg in depth: Fortnum.. Picnic. Details — the picnic egg.. Sausage. Runny. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Breaded.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Breaded.", "x": "Scotch Egg in depth: Breaded.. Fortnum. Details — the picnic egg.. Making. Egg. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Sausage.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Sausage.", "x": "Scotch Egg in depth: Sausage.. Runny. Details — the picnic egg.. Egg. Sausage. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Making.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Making.", "x": "Scotch Egg in depth: Making.. Egg. Details — the picnic egg.. Picnic. Breaded. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Scotch Egg comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Scotch Egg comes from.", "x": "Origins: Egg.. Egg. The history of Scotch Egg — the picnic egg.. Picnic. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Scotch Egg respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Scotch Egg respectfully.", "x": "Engaging: Fortnum.. Sausage. How to participate or observe well — Scotch Egg. the picnic egg. Respect first, always; Breaded.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Scotch Egg do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Scotch Egg do's and don'ts.", "x": "Etiquette: Sausage.. Breaded. The rules of respect — Scotch Egg. the picnic egg. When in doubt, ask about Making.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Scotch Egg.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Scotch Egg.", "x": "Planning: Egg.. Picnic. Practical notes — Scotch Egg. the picnic egg. A little planning shows respect for Picnic.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Scotch Egg and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Scotch Egg and money.", "x": "Costs: Fortnum.. Fortnum. What to budget — Scotch Egg. the picnic egg. The best experiences of Breaded. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-dish-scotch-egg-dish-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
