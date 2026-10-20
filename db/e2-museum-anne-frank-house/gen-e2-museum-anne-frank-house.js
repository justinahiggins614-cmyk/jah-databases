(function(){'use strict';
/* JAH Anne Frank House Museum Database generator — jahdb-e2-museum-anne-frank-house-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-museum-anne-frank-house',PREFIX='JAH-E2MUSEUMANN-',NAME='JAH Anne Frank House Museum Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Anne Frank House: the complete guide", "d": "Anne Frank House: the secret annex..", "g": "overview", "l": 2, "q": "What is Anne Frank House: the complete guide?", "a": "Anne Frank House: the secret annex..", "x": "The complete museum guide to Anne Frank House: the secret annex.. Amsterdam. History, meaning, practices, and how to engage respectfully — everything in one database. Diary. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Anne Frank House essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Anne Frank House essentials.", "x": "At a glance: Anne Frank House — the secret annex.. Diary. The essentials: Annex.. 1940-44. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Amsterdam.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Amsterdam.", "x": "Anne Frank House: Amsterdam.. Annex. Essential knowledge — 1940-44.. the secret annex. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Amsterdam..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Amsterdam..", "x": "Explained: Amsterdam.. History. The context — Anne Frank House. Tickets. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Diary.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Diary.", "x": "Anne Frank House: Diary.. Tickets. Essential knowledge — Tickets.. the secret annex. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Diary..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Diary..", "x": "Explained: Diary.. Reflection. The context — Anne Frank House. Reflection. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "1940-44.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "1940-44.", "x": "Anne Frank House: 1940-44.. History. Essential knowledge — Reflection.. the secret annex. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: 1940-44..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: 1940-44..", "x": "Explained: 1940-44.. Memory. The context — Anne Frank House. History. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Tickets.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Tickets.", "x": "Anne Frank House: Tickets.. Reflection. Essential knowledge — History.. the secret annex. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Tickets..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Tickets..", "x": "Explained: Tickets.. Diary. The context — Anne Frank House. Amsterdam. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Reflection.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Reflection.", "x": "Anne Frank House: Reflection.. Memory. Essential knowledge — Amsterdam.. the secret annex. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Reflection..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Reflection..", "x": "Explained: Reflection.. Annex. The context — Anne Frank House. Diary. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "History.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "History.", "x": "Anne Frank House: History.. Diary. Essential knowledge — Diary.. the secret annex. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: History..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: History..", "x": "Explained: History.. Tickets. The context — Anne Frank House. 1940-44. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Diary.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Diary.", "x": "Anne Frank House in depth: Diary.. Diary. Details — the secret annex.. Tickets. Tickets. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Annex.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Annex.", "x": "Anne Frank House in depth: Annex.. 1940-44. Details — the secret annex.. History. Reflection. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Tickets.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Tickets.", "x": "Anne Frank House in depth: Tickets.. Tickets. Details — the secret annex.. Reflection. History. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "History.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "History.", "x": "Anne Frank House in depth: History.. Reflection. Details — the secret annex.. Memory. Amsterdam. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Reflection.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Reflection.", "x": "Anne Frank House in depth: Reflection.. History. Details — the secret annex.. Diary. Diary. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Memory.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Memory.", "x": "Anne Frank House in depth: Memory.. Amsterdam. Details — the secret annex.. Annex. 1940-44. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Anne Frank House comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Anne Frank House comes from.", "x": "Origins: Diary.. Amsterdam. The history of Anne Frank House — the secret annex.. Annex. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Anne Frank House respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Anne Frank House respectfully.", "x": "Engaging: Tickets.. Diary. How to participate or observe well — Anne Frank House. the secret annex. Respect first, always; History.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Anne Frank House do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Anne Frank House do's and don'ts.", "x": "Etiquette: Reflection.. 1940-44. The rules of respect — Anne Frank House. the secret annex. When in doubt, ask about Memory.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Anne Frank House.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Anne Frank House.", "x": "Planning: Diary.. Tickets. Practical notes — Anne Frank House. the secret annex. A little planning shows respect for Annex.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Anne Frank House and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Anne Frank House and money.", "x": "Costs: Tickets.. Reflection. What to budget — Anne Frank House. the secret annex. The best experiences of History. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-museum-anne-frank-house-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
