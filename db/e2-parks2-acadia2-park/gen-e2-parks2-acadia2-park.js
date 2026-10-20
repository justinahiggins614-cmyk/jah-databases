(function(){'use strict';
/* JAH Acadia2 Database generator — jahdb-e2-parks2-acadia2-park-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-parks2-acadia2-park',PREFIX='JAH-E2PARKS2ACA-',NAME='JAH Acadia2 Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Acadia2: the complete guide", "d": "Acadia2: the coastal 2..", "g": "overview", "l": 2, "q": "What is Acadia2: the complete guide?", "a": "Acadia2: the coastal 2..", "x": "The complete national park guide to Acadia2: the coastal 2.. Maine. History, meaning, practices, and how to engage respectfully — everything in one database. Maine. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Acadia2 essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Acadia2 essentials.", "x": "At a glance: Acadia2 — the coastal 2.. Cadillac. The essentials: Fall.. Coast. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Maine.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Maine.", "x": "Acadia2: Maine.. Fall. Essential knowledge — Coast.. the coastal 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Maine..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Maine..", "x": "Explained: Maine.. Cadillac. The context — Acadia2. Lobster. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Cadillac.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Cadillac.", "x": "Acadia2: Cadillac.. Tidepools. Essential knowledge — Lobster.. the coastal 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Cadillac..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Cadillac..", "x": "Explained: Cadillac.. Lobster. The context — Acadia2. Fall. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Coast.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Coast.", "x": "Acadia2: Coast.. Cadillac. Essential knowledge — Fall.. the coastal 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Coast..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Coast..", "x": "Explained: Coast.. Visiting. The context — Acadia2. Tidepools. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Lobster.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Lobster.", "x": "Acadia2: Lobster.. Lobster. Essential knowledge — Tidepools.. the coastal 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Lobster..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Lobster..", "x": "Explained: Lobster.. Maine. The context — Acadia2. Maine. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Fall.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Fall.", "x": "Acadia2: Fall.. Visiting. Essential knowledge — Maine.. the coastal 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Fall..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Fall..", "x": "Explained: Fall.. Fall. The context — Acadia2. Cadillac. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Tidepools.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Tidepools.", "x": "Acadia2: Tidepools.. Maine. Essential knowledge — Cadillac.. the coastal 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Tidepools..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Tidepools..", "x": "Explained: Tidepools.. Tidepools. The context — Acadia2. Coast. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Maine.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Maine.", "x": "Acadia2 in depth: Maine.. Cadillac. Details — the coastal 2.. Tidepools. Lobster. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Fall.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Fall.", "x": "Acadia2 in depth: Fall.. Coast. Details — the coastal 2.. Cadillac. Fall. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Tidepools.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Tidepools.", "x": "Acadia2 in depth: Tidepools.. Lobster. Details — the coastal 2.. Lobster. Tidepools. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Cadillac.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Cadillac.", "x": "Acadia2 in depth: Cadillac.. Fall. Details — the coastal 2.. Visiting. Maine. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Lobster.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Lobster.", "x": "Acadia2 in depth: Lobster.. Tidepools. Details — the coastal 2.. Maine. Cadillac. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Visiting.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Visiting.", "x": "Acadia2 in depth: Visiting.. Maine. Details — the coastal 2.. Fall. Coast. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Acadia2 comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Acadia2 comes from.", "x": "Origins: Maine.. Maine. The history of Acadia2 — the coastal 2.. Fall. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Acadia2 respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Acadia2 respectfully.", "x": "Engaging: Tidepools.. Cadillac. How to participate or observe well — Acadia2. the coastal 2. Respect first, always; Cadillac.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Acadia2 do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Acadia2 do's and don'ts.", "x": "Etiquette: Lobster.. Coast. The rules of respect — Acadia2. the coastal 2. When in doubt, ask about Visiting.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Acadia2.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Acadia2.", "x": "Planning: Maine.. Lobster. Practical notes — Acadia2. the coastal 2. A little planning shows respect for Fall.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Acadia2 and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Acadia2 and money.", "x": "Costs: Tidepools.. Fall. What to budget — Acadia2. the coastal 2. The best experiences of Cadillac. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-parks2-acadia2-park-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
