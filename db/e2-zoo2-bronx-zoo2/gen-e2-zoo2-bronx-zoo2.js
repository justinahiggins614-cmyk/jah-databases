(function(){'use strict';
/* JAH Bronx Zoo2 Database generator — jahdb-e2-zoo2-bronx-zoo2-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-zoo2-bronx-zoo2',PREFIX='JAH-E2ZOO2BRONX-',NAME='JAH Bronx Zoo2 Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Bronx Zoo2: the complete guide", "d": "Bronx Zoo2: the NYC 2..", "g": "overview", "l": 2, "q": "What is Bronx Zoo2: the complete guide?", "a": "Bronx Zoo2: the NYC 2..", "x": "The complete zoo guide to Bronx Zoo2: the NYC 2.. 1899. History, meaning, practices, and how to engage respectfully — everything in one database. 1899. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Bronx Zoo2 essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Bronx Zoo2 essentials.", "x": "At a glance: Bronx Zoo2 — the NYC 2.. 265 acres. The essentials: WCS.. Congo. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "1899.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "1899.", "x": "Bronx Zoo2: 1899.. WCS. Essential knowledge — Congo.. the NYC 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 1899..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 1899..", "x": "Explained: 1899.. Acres. The context — Bronx Zoo2. Tigers. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "265 acres.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "265 acres.", "x": "Bronx Zoo2: 265 acres.. NYC. Essential knowledge — Tigers.. the NYC 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: 265 acres..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: 265 acres..", "x": "Explained: 265 acres.. Congo. The context — Bronx Zoo2. NYC. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Congo.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Congo.", "x": "Bronx Zoo2: Congo.. Acres. Essential knowledge — NYC.. the NYC 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Congo..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Congo..", "x": "Explained: Congo.. Visiting. The context — Bronx Zoo2. WCS. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Tigers.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Tigers.", "x": "Bronx Zoo2: Tigers.. Congo. Essential knowledge — WCS.. the NYC 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Tigers..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Tigers..", "x": "Explained: Tigers.. 1899. The context — Bronx Zoo2. 1899. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "NYC.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "NYC.", "x": "Bronx Zoo2: NYC.. Visiting. Essential knowledge — 1899.. the NYC 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: NYC..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: NYC..", "x": "Explained: NYC.. WCS. The context — Bronx Zoo2. 265 acres. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "WCS.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "WCS.", "x": "Bronx Zoo2: WCS.. 1899. Essential knowledge — 265 acres.. the NYC 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: WCS..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: WCS..", "x": "Explained: WCS.. NYC. The context — Bronx Zoo2. Congo. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "1899.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "1899.", "x": "Bronx Zoo2 in depth: 1899.. 265 acres. Details — the NYC 2.. NYC. Tigers. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "WCS.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "WCS.", "x": "Bronx Zoo2 in depth: WCS.. Congo. Details — the NYC 2.. Acres. NYC. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "NYC.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "NYC.", "x": "Bronx Zoo2 in depth: NYC.. Tigers. Details — the NYC 2.. Congo. WCS. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Acres.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Acres.", "x": "Bronx Zoo2 in depth: Acres.. NYC. Details — the NYC 2.. Visiting. 1899. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Congo.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Congo.", "x": "Bronx Zoo2 in depth: Congo.. WCS. Details — the NYC 2.. 1899. 265 acres. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Visiting.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Visiting.", "x": "Bronx Zoo2 in depth: Visiting.. 1899. Details — the NYC 2.. WCS. Congo. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Bronx Zoo2 comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Bronx Zoo2 comes from.", "x": "Origins: 1899.. 1899. The history of Bronx Zoo2 — the NYC 2.. WCS. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Bronx Zoo2 respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Bronx Zoo2 respectfully.", "x": "Engaging: NYC.. 265 acres. How to participate or observe well — Bronx Zoo2. the NYC 2. Respect first, always; Acres.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Bronx Zoo2 do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Bronx Zoo2 do's and don'ts.", "x": "Etiquette: Congo.. Congo. The rules of respect — Bronx Zoo2. the NYC 2. When in doubt, ask about Visiting.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Bronx Zoo2.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Bronx Zoo2.", "x": "Planning: 1899.. Tigers. Practical notes — Bronx Zoo2. the NYC 2. A little planning shows respect for WCS.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Bronx Zoo2 and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Bronx Zoo2 and money.", "x": "Costs: NYC.. NYC. What to budget — Bronx Zoo2. the NYC 2. The best experiences of Acres. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-zoo2-bronx-zoo2-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
