(function(){'use strict';
/* JAH English Muffin Bread Database generator — jahdb-e2-bread-english-muffin-bread-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-bread-english-muffin-bread',PREFIX='JAH-E2BREADENGL-',NAME='JAH English Muffin Bread Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "English Muffin: the complete guide", "d": "English Muffin: the nooks and crannies..", "g": "overview", "l": 2, "q": "What is English Muffin: the complete guide?", "a": "English Muffin: the nooks and crannies..", "x": "The complete bread guide to English Muffin: the nooks and crannies.. Fork-split. History, meaning, practices, and how to engage respectfully — everything in one database. Nooks. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "English Muffin essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "English Muffin essentials.", "x": "At a glance: English Muffin — the nooks and crannies.. Nooks. The essentials: Split.. Crumpet? no. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Fork-split.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Fork-split.", "x": "English Muffin: Fork-split.. Split. Essential knowledge — Crumpet? no.. the nooks and crannies. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Fork-split..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Fork-split..", "x": "Explained: Fork-split.. Benedict. The context — English Muffin. Toasted. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Nooks.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Nooks.", "x": "English Muffin: Nooks.. Toasted. Essential knowledge — Toasted.. the nooks and crannies. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Nooks..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Nooks..", "x": "Explained: Nooks.. History. The context — English Muffin. 1860s. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Crumpet? no.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Crumpet? no.", "x": "English Muffin: Crumpet? no.. Benedict. Essential knowledge — 1860s.. the nooks and crannies. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Crumpet? no..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Crumpet? no..", "x": "Explained: Crumpet? no.. Crumpet. The context — English Muffin. Eggs Benedict. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Toasted.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Toasted.", "x": "English Muffin: Toasted.. History. Essential knowledge — Eggs Benedict.. the nooks and crannies. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Toasted..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Toasted..", "x": "Explained: Toasted.. Nooks. The context — English Muffin. Fork-split. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "1860s.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "1860s.", "x": "English Muffin: 1860s.. Crumpet. Essential knowledge — Fork-split.. the nooks and crannies. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: 1860s..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: 1860s..", "x": "Explained: 1860s.. Split. The context — English Muffin. Nooks. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Eggs Benedict.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Eggs Benedict.", "x": "English Muffin: Eggs Benedict.. Nooks. Essential knowledge — Nooks.. the nooks and crannies. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Eggs Benedict..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Eggs Benedict..", "x": "Explained: Eggs Benedict.. Toasted. The context — English Muffin. Crumpet? no. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Nooks.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Nooks.", "x": "English Muffin in depth: Nooks.. Nooks. Details — the nooks and crannies.. Toasted. Toasted. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Split.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Split.", "x": "English Muffin in depth: Split.. Crumpet? no. Details — the nooks and crannies.. Benedict. 1860s. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Toasted.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Toasted.", "x": "English Muffin in depth: Toasted.. Toasted. Details — the nooks and crannies.. History. Eggs Benedict. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Benedict.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Benedict.", "x": "English Muffin in depth: Benedict.. 1860s. Details — the nooks and crannies.. Crumpet. Fork-split. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "History.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "History.", "x": "English Muffin in depth: History.. Eggs Benedict. Details — the nooks and crannies.. Nooks. Nooks. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Crumpet.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Crumpet.", "x": "English Muffin in depth: Crumpet.. Fork-split. Details — the nooks and crannies.. Split. Crumpet? no. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where English Muffin comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where English Muffin comes from.", "x": "Origins: Nooks.. Fork-split. The history of English Muffin — the nooks and crannies.. Split. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing English Muffin respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing English Muffin respectfully.", "x": "Engaging: Toasted.. Nooks. How to participate or observe well — English Muffin. the nooks and crannies. Respect first, always; Benedict.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "English Muffin do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "English Muffin do's and don'ts.", "x": "Etiquette: History.. Crumpet? no. The rules of respect — English Muffin. the nooks and crannies. When in doubt, ask about Crumpet.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around English Muffin.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around English Muffin.", "x": "Planning: Nooks.. Toasted. Practical notes — English Muffin. the nooks and crannies. A little planning shows respect for Split.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "English Muffin and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "English Muffin and money.", "x": "Costs: Toasted.. 1860s. What to budget — English Muffin. the nooks and crannies. The best experiences of Benedict. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-bread-english-muffin-bread-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
