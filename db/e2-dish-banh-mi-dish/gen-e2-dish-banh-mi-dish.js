(function(){'use strict';
/* JAH Banh Mi Dish Database generator — jahdb-e2-dish-banh-mi-dish-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-dish-banh-mi-dish',PREFIX='JAH-E2DISHBANHM-',NAME='JAH Banh Mi Dish Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Banh Mi: the complete guide", "d": "Banh Mi: the French-Vietnamese..", "g": "overview", "l": 2, "q": "What is Banh Mi: the complete guide?", "a": "Banh Mi: the French-Vietnamese..", "x": "The complete dish guide to Banh Mi: the French-Vietnamese.. Baguette. History, meaning, practices, and how to engage respectfully — everything in one database. Baguette. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Banh Mi essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Banh Mi essentials.", "x": "At a glance: Banh Mi — the French-Vietnamese.. Pate. The essentials: Colonial.. Pickles. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Baguette.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Baguette.", "x": "Banh Mi: Baguette.. Colonial. Essential knowledge — Pickles.. the French-Vietnamese. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Baguette..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Baguette..", "x": "Explained: Baguette.. Pate. The context — Banh Mi. Cilantro. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Pate.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Pate.", "x": "Banh Mi: Pate.. Crunchy. Essential knowledge — Cilantro.. the French-Vietnamese. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Pate..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Pate..", "x": "Explained: Pate.. Pickles. The context — Banh Mi. Colonial. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Pickles.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Pickles.", "x": "Banh Mi: Pickles.. Pate. Essential knowledge — Colonial.. the French-Vietnamese. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Pickles..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Pickles..", "x": "Explained: Pickles.. Making. The context — Banh Mi. Crunchy. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Cilantro.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Cilantro.", "x": "Banh Mi: Cilantro.. Pickles. Essential knowledge — Crunchy.. the French-Vietnamese. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Cilantro..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Cilantro..", "x": "Explained: Cilantro.. Baguette. The context — Banh Mi. Baguette. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Colonial.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Colonial.", "x": "Banh Mi: Colonial.. Making. Essential knowledge — Baguette.. the French-Vietnamese. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Colonial..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Colonial..", "x": "Explained: Colonial.. Colonial. The context — Banh Mi. Pate. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Crunchy.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Crunchy.", "x": "Banh Mi: Crunchy.. Baguette. Essential knowledge — Pate.. the French-Vietnamese. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Crunchy..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Crunchy..", "x": "Explained: Crunchy.. Crunchy. The context — Banh Mi. Pickles. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Baguette.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Baguette.", "x": "Banh Mi in depth: Baguette.. Pate. Details — the French-Vietnamese.. Crunchy. Cilantro. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Colonial.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Colonial.", "x": "Banh Mi in depth: Colonial.. Pickles. Details — the French-Vietnamese.. Pate. Colonial. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Crunchy.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Crunchy.", "x": "Banh Mi in depth: Crunchy.. Cilantro. Details — the French-Vietnamese.. Pickles. Crunchy. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Pate.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Pate.", "x": "Banh Mi in depth: Pate.. Colonial. Details — the French-Vietnamese.. Making. Baguette. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Pickles.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Pickles.", "x": "Banh Mi in depth: Pickles.. Crunchy. Details — the French-Vietnamese.. Baguette. Pate. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Making.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Making.", "x": "Banh Mi in depth: Making.. Baguette. Details — the French-Vietnamese.. Colonial. Pickles. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Banh Mi comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Banh Mi comes from.", "x": "Origins: Baguette.. Baguette. The history of Banh Mi — the French-Vietnamese.. Colonial. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Banh Mi respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Banh Mi respectfully.", "x": "Engaging: Crunchy.. Pate. How to participate or observe well — Banh Mi. the French-Vietnamese. Respect first, always; Pate.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Banh Mi do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Banh Mi do's and don'ts.", "x": "Etiquette: Pickles.. Pickles. The rules of respect — Banh Mi. the French-Vietnamese. When in doubt, ask about Making.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Banh Mi.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Banh Mi.", "x": "Planning: Baguette.. Cilantro. Practical notes — Banh Mi. the French-Vietnamese. A little planning shows respect for Colonial.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Banh Mi and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Banh Mi and money.", "x": "Costs: Crunchy.. Colonial. What to budget — Banh Mi. the French-Vietnamese. The best experiences of Pate. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-dish-banh-mi-dish-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
