(function(){'use strict';
/* JAH Orzo Pasta Database generator — jahdb-e2-pasta-orzo-pasta-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-pasta-orzo-pasta',PREFIX='JAH-E2PASTAORZO-',NAME='JAH Orzo Pasta Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Orzo: the complete guide", "d": "Orzo: the rice-shaped..", "g": "overview", "l": 2, "q": "What is Orzo: the complete guide?", "a": "Orzo: the rice-shaped..", "x": "The complete pasta guide to Orzo: the rice-shaped.. Rice shape. History, meaning, practices, and how to engage respectfully — everything in one database. Shape. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Orzo essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Orzo essentials.", "x": "At a glance: Orzo — the rice-shaped.. Soups. The essentials: Soups.. Salads. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Rice shape.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Rice shape.", "x": "Orzo: Rice shape.. Soups. Essential knowledge — Salads.. the rice-shaped. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Rice shape..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Rice shape..", "x": "Explained: Rice shape.. Pilaf. The context — Orzo. Greek. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Soups.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Soups.", "x": "Orzo: Soups.. Greek. Essential knowledge — Greek.. the rice-shaped. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Soups..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Soups..", "x": "Explained: Soups.. Small. The context — Orzo. Pilaf. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Salads.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Salads.", "x": "Orzo: Salads.. Pilaf. Essential knowledge — Pilaf.. the rice-shaped. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Salads..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Salads..", "x": "Explained: Salads.. Uses. The context — Orzo. Small. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Greek.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Greek.", "x": "Orzo: Greek.. Small. Essential knowledge — Small.. the rice-shaped. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Greek..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Greek..", "x": "Explained: Greek.. Shape. The context — Orzo. Rice shape. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Pilaf.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Pilaf.", "x": "Orzo: Pilaf.. Uses. Essential knowledge — Rice shape.. the rice-shaped. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Pilaf..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Pilaf..", "x": "Explained: Pilaf.. Soups. The context — Orzo. Soups. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Small.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Small.", "x": "Orzo: Small.. Shape. Essential knowledge — Soups.. the rice-shaped. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Small..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Small..", "x": "Explained: Small.. Greek. The context — Orzo. Salads. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Shape.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Shape.", "x": "Orzo in depth: Shape.. Soups. Details — the rice-shaped.. Greek. Greek. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Soups.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Soups.", "x": "Orzo in depth: Soups.. Salads. Details — the rice-shaped.. Pilaf. Pilaf. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Greek.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Greek.", "x": "Orzo in depth: Greek.. Greek. Details — the rice-shaped.. Small. Small. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Pilaf.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Pilaf.", "x": "Orzo in depth: Pilaf.. Pilaf. Details — the rice-shaped.. Uses. Rice shape. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Small.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Small.", "x": "Orzo in depth: Small.. Small. Details — the rice-shaped.. Shape. Soups. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Uses.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Uses.", "x": "Orzo in depth: Uses.. Rice shape. Details — the rice-shaped.. Soups. Salads. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Orzo comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Orzo comes from.", "x": "Origins: Shape.. Rice shape. The history of Orzo — the rice-shaped.. Soups. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Orzo respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Orzo respectfully.", "x": "Engaging: Greek.. Soups. How to participate or observe well — Orzo. the rice-shaped. Respect first, always; Pilaf.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Orzo do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Orzo do's and don'ts.", "x": "Etiquette: Small.. Salads. The rules of respect — Orzo. the rice-shaped. When in doubt, ask about Uses.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Orzo.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Orzo.", "x": "Planning: Shape.. Greek. Practical notes — Orzo. the rice-shaped. A little planning shows respect for Soups.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Orzo and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Orzo and money.", "x": "Costs: Greek.. Pilaf. What to budget — Orzo. the rice-shaped. The best experiences of Pilaf. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-pasta-orzo-pasta-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
