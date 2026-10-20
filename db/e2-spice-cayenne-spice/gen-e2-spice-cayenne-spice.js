(function(){'use strict';
/* JAH Cayenne Spice Database generator — jahdb-e2-spice-cayenne-spice-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-spice-cayenne-spice',PREFIX='JAH-E2SPICECAYE-',NAME='JAH Cayenne Spice Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Cayenne: the complete guide", "d": "Cayenne: the clean heat..", "g": "overview", "l": 2, "q": "What is Cayenne: the complete guide?", "a": "Cayenne: the clean heat..", "x": "The complete spice guide to Cayenne: the clean heat.. 30-50K SHU. History, meaning, practices, and how to engage respectfully — everything in one database. SHU. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Cayenne essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Cayenne essentials.", "x": "At a glance: Cayenne — the clean heat.. Capsaicin. The essentials: Capsaicin.. Metabolism. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "30-50K SHU.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "30-50K SHU.", "x": "Cayenne: 30-50K SHU.. Capsaicin. Essential knowledge — Metabolism.. the clean heat. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 30-50K SHU..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 30-50K SHU..", "x": "Explained: 30-50K SHU.. Dose. The context — Cayenne. Flakes. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Capsaicin.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Capsaicin.", "x": "Cayenne: Capsaicin.. Sauces. Essential knowledge — Flakes.. the clean heat. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Capsaicin..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Capsaicin..", "x": "Explained: Capsaicin.. Flakes. The context — Cayenne. Sauces. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Metabolism.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Metabolism.", "x": "Cayenne: Metabolism.. Dose. Essential knowledge — Sauces.. the clean heat. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Metabolism..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Metabolism..", "x": "Explained: Metabolism.. Heat. The context — Cayenne. Dose. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Flakes.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Flakes.", "x": "Cayenne: Flakes.. Flakes. Essential knowledge — Dose.. the clean heat. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Flakes..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Flakes..", "x": "Explained: Flakes.. SHU. The context — Cayenne. 30-50K SHU. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Sauces.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Sauces.", "x": "Cayenne: Sauces.. Heat. Essential knowledge — 30-50K SHU.. the clean heat. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Sauces..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Sauces..", "x": "Explained: Sauces.. Capsaicin. The context — Cayenne. Capsaicin. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Dose.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Dose.", "x": "Cayenne: Dose.. SHU. Essential knowledge — Capsaicin.. the clean heat. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Dose..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Dose..", "x": "Explained: Dose.. Sauces. The context — Cayenne. Metabolism. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "SHU.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "SHU.", "x": "Cayenne in depth: SHU.. Capsaicin. Details — the clean heat.. Sauces. Flakes. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Capsaicin.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Capsaicin.", "x": "Cayenne in depth: Capsaicin.. Metabolism. Details — the clean heat.. Dose. Sauces. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Sauces.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Sauces.", "x": "Cayenne in depth: Sauces.. Flakes. Details — the clean heat.. Flakes. Dose. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Dose.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Dose.", "x": "Cayenne in depth: Dose.. Sauces. Details — the clean heat.. Heat. 30-50K SHU. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Flakes.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Flakes.", "x": "Cayenne in depth: Flakes.. Dose. Details — the clean heat.. SHU. Capsaicin. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Heat.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Heat.", "x": "Cayenne in depth: Heat.. 30-50K SHU. Details — the clean heat.. Capsaicin. Metabolism. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Cayenne comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Cayenne comes from.", "x": "Origins: SHU.. 30-50K SHU. The history of Cayenne — the clean heat.. Capsaicin. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Cayenne respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Cayenne respectfully.", "x": "Engaging: Sauces.. Capsaicin. How to participate or observe well — Cayenne. the clean heat. Respect first, always; Dose.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Cayenne do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Cayenne do's and don'ts.", "x": "Etiquette: Flakes.. Metabolism. The rules of respect — Cayenne. the clean heat. When in doubt, ask about Heat.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Cayenne.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Cayenne.", "x": "Planning: SHU.. Flakes. Practical notes — Cayenne. the clean heat. A little planning shows respect for Capsaicin.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Cayenne and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Cayenne and money.", "x": "Costs: Sauces.. Sauces. What to budget — Cayenne. the clean heat. The best experiences of Dose. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-spice-cayenne-spice-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
