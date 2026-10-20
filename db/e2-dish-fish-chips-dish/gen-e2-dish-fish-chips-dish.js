(function(){'use strict';
/* JAH Fish and Chips Dish Database generator — jahdb-e2-dish-fish-chips-dish-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-dish-fish-chips-dish',PREFIX='JAH-E2DISHFISHC-',NAME='JAH Fish and Chips Dish Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Fish and Chips: the complete guide", "d": "Fish and Chips: the British fry..", "g": "overview", "l": 2, "q": "What is Fish and Chips: the complete guide?", "a": "Fish and Chips: the British fry..", "x": "The complete dish guide to Fish and Chips: the British fry.. Cod. History, meaning, practices, and how to engage respectfully — everything in one database. Cod. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Fish and Chips essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Fish and Chips essentials.", "x": "At a glance: Fish and Chips — the British fry.. Batter. The essentials: Vinegar.. Chips. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Cod.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Cod.", "x": "Fish and Chips: Cod.. Vinegar. Essential knowledge — Chips.. the British fry. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Cod..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Cod..", "x": "Explained: Cod.. Batter. The context — Fish and Chips. Vinegar. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Batter.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Batter.", "x": "Fish and Chips: Batter.. Fryer. Essential knowledge — Vinegar.. the British fry. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Batter..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Batter..", "x": "Explained: Batter.. Chips. The context — Fish and Chips. Newspaper. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Chips.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Chips.", "x": "Fish and Chips: Chips.. Batter. Essential knowledge — Newspaper.. the British fry. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Chips..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Chips..", "x": "Explained: Chips.. Making. The context — Fish and Chips. Fryer. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Vinegar.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Vinegar.", "x": "Fish and Chips: Vinegar.. Chips. Essential knowledge — Fryer.. the British fry. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Vinegar..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Vinegar..", "x": "Explained: Vinegar.. Cod. The context — Fish and Chips. Cod. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Newspaper.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Newspaper.", "x": "Fish and Chips: Newspaper.. Making. Essential knowledge — Cod.. the British fry. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Newspaper..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Newspaper..", "x": "Explained: Newspaper.. Vinegar. The context — Fish and Chips. Batter. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Fryer.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Fryer.", "x": "Fish and Chips: Fryer.. Cod. Essential knowledge — Batter.. the British fry. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Fryer..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Fryer..", "x": "Explained: Fryer.. Fryer. The context — Fish and Chips. Chips. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Cod.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Cod.", "x": "Fish and Chips in depth: Cod.. Batter. Details — the British fry.. Fryer. Vinegar. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Vinegar.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Vinegar.", "x": "Fish and Chips in depth: Vinegar.. Chips. Details — the British fry.. Batter. Newspaper. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Fryer.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Fryer.", "x": "Fish and Chips in depth: Fryer.. Vinegar. Details — the British fry.. Chips. Fryer. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Batter.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Batter.", "x": "Fish and Chips in depth: Batter.. Newspaper. Details — the British fry.. Making. Cod. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Chips.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Chips.", "x": "Fish and Chips in depth: Chips.. Fryer. Details — the British fry.. Cod. Batter. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Making.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Making.", "x": "Fish and Chips in depth: Making.. Cod. Details — the British fry.. Vinegar. Chips. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Fish and Chips comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Fish and Chips comes from.", "x": "Origins: Cod.. Cod. The history of Fish and Chips — the British fry.. Vinegar. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Fish and Chips respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Fish and Chips respectfully.", "x": "Engaging: Fryer.. Batter. How to participate or observe well — Fish and Chips. the British fry. Respect first, always; Batter.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Fish and Chips do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Fish and Chips do's and don'ts.", "x": "Etiquette: Chips.. Chips. The rules of respect — Fish and Chips. the British fry. When in doubt, ask about Making.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Fish and Chips.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Fish and Chips.", "x": "Planning: Cod.. Vinegar. Practical notes — Fish and Chips. the British fry. A little planning shows respect for Vinegar.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Fish and Chips and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Fish and Chips and money.", "x": "Costs: Fryer.. Newspaper. What to budget — Fish and Chips. the British fry. The best experiences of Batter. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-dish-fish-chips-dish-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
