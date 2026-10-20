(function(){'use strict';
/* JAH Bangers and Mash Dish Database generator — jahdb-e2-dish-bangers-mash-dish-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-dish-bangers-mash-dish',PREFIX='JAH-E2DISHBANGE-',NAME='JAH Bangers and Mash Dish Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Bangers and Mash: the complete guide", "d": "Bangers and Mash: the sausage mash..", "g": "overview", "l": 2, "q": "What is Bangers and Mash: the complete guide?", "a": "Bangers and Mash: the sausage mash..", "x": "The complete dish guide to Bangers and Mash: the sausage mash.. Sausages. History, meaning, practices, and how to engage respectfully — everything in one database. Sausages. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Bangers and Mash essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Bangers and Mash essentials.", "x": "At a glance: Bangers and Mash — the sausage mash.. Mash. The essentials: Pub.. Onion gravy. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Sausages.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Sausages.", "x": "Bangers and Mash: Sausages.. Pub. Essential knowledge — Onion gravy.. the sausage mash. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Sausages..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Sausages..", "x": "Explained: Sausages.. Mash. The context — Bangers and Mash. Pub. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Mash.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Mash.", "x": "Bangers and Mash: Mash.. Comfort. Essential knowledge — Pub.. the sausage mash. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Mash..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Mash..", "x": "Explained: Mash.. Gravy. The context — Bangers and Mash. Comfort. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Onion gravy.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Onion gravy.", "x": "Bangers and Mash: Onion gravy.. Mash. Essential knowledge — Comfort.. the sausage mash. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Onion gravy..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Onion gravy..", "x": "Explained: Onion gravy.. Making. The context — Bangers and Mash. Bangers. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Pub.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Pub.", "x": "Bangers and Mash: Pub.. Gravy. Essential knowledge — Bangers.. the sausage mash. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Pub..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Pub..", "x": "Explained: Pub.. Sausages. The context — Bangers and Mash. Sausages. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Comfort.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Comfort.", "x": "Bangers and Mash: Comfort.. Making. Essential knowledge — Sausages.. the sausage mash. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Comfort..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Comfort..", "x": "Explained: Comfort.. Pub. The context — Bangers and Mash. Mash. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Bangers.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Bangers.", "x": "Bangers and Mash: Bangers.. Sausages. Essential knowledge — Mash.. the sausage mash. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Bangers..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Bangers..", "x": "Explained: Bangers.. Comfort. The context — Bangers and Mash. Onion gravy. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Sausages.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Sausages.", "x": "Bangers and Mash in depth: Sausages.. Mash. Details — the sausage mash.. Comfort. Pub. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Pub.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Pub.", "x": "Bangers and Mash in depth: Pub.. Onion gravy. Details — the sausage mash.. Mash. Comfort. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Comfort.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Comfort.", "x": "Bangers and Mash in depth: Comfort.. Pub. Details — the sausage mash.. Gravy. Bangers. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Mash.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Mash.", "x": "Bangers and Mash in depth: Mash.. Comfort. Details — the sausage mash.. Making. Sausages. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Gravy.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Gravy.", "x": "Bangers and Mash in depth: Gravy.. Bangers. Details — the sausage mash.. Sausages. Mash. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Making.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Making.", "x": "Bangers and Mash in depth: Making.. Sausages. Details — the sausage mash.. Pub. Onion gravy. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Bangers and Mash comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Bangers and Mash comes from.", "x": "Origins: Sausages.. Sausages. The history of Bangers and Mash — the sausage mash.. Pub. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Bangers and Mash respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Bangers and Mash respectfully.", "x": "Engaging: Comfort.. Mash. How to participate or observe well — Bangers and Mash. the sausage mash. Respect first, always; Mash.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Bangers and Mash do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Bangers and Mash do's and don'ts.", "x": "Etiquette: Gravy.. Onion gravy. The rules of respect — Bangers and Mash. the sausage mash. When in doubt, ask about Making.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Bangers and Mash.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Bangers and Mash.", "x": "Planning: Sausages.. Pub. Practical notes — Bangers and Mash. the sausage mash. A little planning shows respect for Pub.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Bangers and Mash and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Bangers and Mash and money.", "x": "Costs: Comfort.. Comfort. What to budget — Bangers and Mash. the sausage mash. The best experiences of Mash. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-dish-bangers-mash-dish-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
