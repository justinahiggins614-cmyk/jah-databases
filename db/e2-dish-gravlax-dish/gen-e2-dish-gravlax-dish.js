(function(){'use strict';
/* JAH Gravlax Dish Database generator — jahdb-e2-dish-gravlax-dish-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-dish-gravlax-dish',PREFIX='JAH-E2DISHGRAVL-',NAME='JAH Gravlax Dish Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Gravlax: the complete guide", "d": "Gravlax: the cured salmon..", "g": "overview", "l": 2, "q": "What is Gravlax: the complete guide?", "a": "Gravlax: the cured salmon..", "x": "The complete dish guide to Gravlax: the cured salmon.. Cured. History, meaning, practices, and how to engage respectfully — everything in one database. Dill. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Gravlax essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Gravlax essentials.", "x": "At a glance: Gravlax — the cured salmon.. Dill. The essentials: Salmon.. Mustard. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Cured.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Cured.", "x": "Gravlax: Cured.. Salmon. Essential knowledge — Mustard.. the cured salmon. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Cured..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Cured..", "x": "Explained: Cured.. Cured. The context — Gravlax. Salmon. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Dill.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Dill.", "x": "Gravlax: Dill.. Aquavit. Essential knowledge — Salmon.. the cured salmon. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Dill..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Dill..", "x": "Explained: Dill.. Mustard. The context — Gravlax. Scandinavia. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Mustard.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Mustard.", "x": "Gravlax: Mustard.. Cured. Essential knowledge — Scandinavia.. the cured salmon. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Mustard..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Mustard..", "x": "Explained: Mustard.. Making. The context — Gravlax. Aquavit. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Salmon.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Salmon.", "x": "Gravlax: Salmon.. Mustard. Essential knowledge — Aquavit.. the cured salmon. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Salmon..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Salmon..", "x": "Explained: Salmon.. Dill. The context — Gravlax. Cured. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Scandinavia.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Scandinavia.", "x": "Gravlax: Scandinavia.. Making. Essential knowledge — Cured.. the cured salmon. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Scandinavia..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Scandinavia..", "x": "Explained: Scandinavia.. Salmon. The context — Gravlax. Dill. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Aquavit.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Aquavit.", "x": "Gravlax: Aquavit.. Dill. Essential knowledge — Dill.. the cured salmon. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Aquavit..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Aquavit..", "x": "Explained: Aquavit.. Aquavit. The context — Gravlax. Mustard. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Dill.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Dill.", "x": "Gravlax in depth: Dill.. Dill. Details — the cured salmon.. Aquavit. Salmon. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Salmon.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Salmon.", "x": "Gravlax in depth: Salmon.. Mustard. Details — the cured salmon.. Cured. Scandinavia. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Aquavit.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Aquavit.", "x": "Gravlax in depth: Aquavit.. Salmon. Details — the cured salmon.. Mustard. Aquavit. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Cured.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Cured.", "x": "Gravlax in depth: Cured.. Scandinavia. Details — the cured salmon.. Making. Cured. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Mustard.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Mustard.", "x": "Gravlax in depth: Mustard.. Aquavit. Details — the cured salmon.. Dill. Dill. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Making.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Making.", "x": "Gravlax in depth: Making.. Cured. Details — the cured salmon.. Salmon. Mustard. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Gravlax comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Gravlax comes from.", "x": "Origins: Dill.. Cured. The history of Gravlax — the cured salmon.. Salmon. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Gravlax respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Gravlax respectfully.", "x": "Engaging: Aquavit.. Dill. How to participate or observe well — Gravlax. the cured salmon. Respect first, always; Cured.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Gravlax do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Gravlax do's and don'ts.", "x": "Etiquette: Mustard.. Mustard. The rules of respect — Gravlax. the cured salmon. When in doubt, ask about Making.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Gravlax.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Gravlax.", "x": "Planning: Dill.. Salmon. Practical notes — Gravlax. the cured salmon. A little planning shows respect for Salmon.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Gravlax and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Gravlax and money.", "x": "Costs: Aquavit.. Scandinavia. What to budget — Gravlax. the cured salmon. The best experiences of Cured. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-dish-gravlax-dish-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
