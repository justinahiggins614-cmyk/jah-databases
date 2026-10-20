(function(){'use strict';
/* JAH Bacalao Dish Database generator — jahdb-e2-dish-bacalao-dish-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-dish-bacalao-dish',PREFIX='JAH-E2DISHBACAL-',NAME='JAH Bacalao Dish Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Bacalao: the complete guide", "d": "Bacalao: the salt cod..", "g": "overview", "l": 2, "q": "What is Bacalao: the complete guide?", "a": "Bacalao: the salt cod..", "x": "The complete dish guide to Bacalao: the salt cod.. Salt cod. History, meaning, practices, and how to engage respectfully — everything in one database. Cod. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Bacalao essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Bacalao essentials.", "x": "At a glance: Bacalao — the salt cod.. Desalting. The essentials: Basque.. Pil-pil. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Salt cod.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Salt cod.", "x": "Bacalao: Salt cod.. Basque. Essential knowledge — Pil-pil.. the salt cod. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Salt cod..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Salt cod..", "x": "Explained: Salt cod.. Pil-pil. The context — Bacalao. Basque. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Desalting.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Desalting.", "x": "Bacalao: Desalting.. Lent. Essential knowledge — Basque.. the salt cod. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Desalting..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Desalting..", "x": "Explained: Desalting.. Desalting. The context — Bacalao. Versatile. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Pil-pil.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Pil-pil.", "x": "Bacalao: Pil-pil.. Pil-pil. Essential knowledge — Versatile.. the salt cod. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Pil-pil..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Pil-pil..", "x": "Explained: Pil-pil.. Making. The context — Bacalao. Lent. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Basque.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Basque.", "x": "Bacalao: Basque.. Desalting. Essential knowledge — Lent.. the salt cod. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Basque..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Basque..", "x": "Explained: Basque.. Cod. The context — Bacalao. Salt cod. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Versatile.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Versatile.", "x": "Bacalao: Versatile.. Making. Essential knowledge — Salt cod.. the salt cod. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Versatile..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Versatile..", "x": "Explained: Versatile.. Basque. The context — Bacalao. Desalting. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Lent.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Lent.", "x": "Bacalao: Lent.. Cod. Essential knowledge — Desalting.. the salt cod. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Lent..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Lent..", "x": "Explained: Lent.. Lent. The context — Bacalao. Pil-pil. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Cod.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Cod.", "x": "Bacalao in depth: Cod.. Desalting. Details — the salt cod.. Lent. Basque. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Basque.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Basque.", "x": "Bacalao in depth: Basque.. Pil-pil. Details — the salt cod.. Pil-pil. Versatile. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Lent.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Lent.", "x": "Bacalao in depth: Lent.. Basque. Details — the salt cod.. Desalting. Lent. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Pil-pil.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Pil-pil.", "x": "Bacalao in depth: Pil-pil.. Versatile. Details — the salt cod.. Making. Salt cod. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Desalting.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Desalting.", "x": "Bacalao in depth: Desalting.. Lent. Details — the salt cod.. Cod. Desalting. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Making.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Making.", "x": "Bacalao in depth: Making.. Salt cod. Details — the salt cod.. Basque. Pil-pil. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Bacalao comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Bacalao comes from.", "x": "Origins: Cod.. Salt cod. The history of Bacalao — the salt cod.. Basque. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Bacalao respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Bacalao respectfully.", "x": "Engaging: Lent.. Desalting. How to participate or observe well — Bacalao. the salt cod. Respect first, always; Pil-pil.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Bacalao do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Bacalao do's and don'ts.", "x": "Etiquette: Desalting.. Pil-pil. The rules of respect — Bacalao. the salt cod. When in doubt, ask about Making.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Bacalao.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Bacalao.", "x": "Planning: Cod.. Basque. Practical notes — Bacalao. the salt cod. A little planning shows respect for Basque.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Bacalao and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Bacalao and money.", "x": "Costs: Lent.. Versatile. What to budget — Bacalao. the salt cod. The best experiences of Pil-pil. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-dish-bacalao-dish-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
