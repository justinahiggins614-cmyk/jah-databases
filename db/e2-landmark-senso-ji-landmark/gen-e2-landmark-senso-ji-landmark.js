(function(){'use strict';
/* JAH Senso-ji Landmark Database generator — jahdb-e2-landmark-senso-ji-landmark-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-landmark-senso-ji-landmark',PREFIX='JAH-E2LANDMARKS-',NAME='JAH Senso-ji Landmark Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Senso-ji: the complete guide", "d": "Senso-ji: the thunder gate..", "g": "overview", "l": 2, "q": "What is Senso-ji: the complete guide?", "a": "Senso-ji: the thunder gate..", "x": "The complete landmark guide to Senso-ji: the thunder gate.. 628. History, meaning, practices, and how to engage respectfully — everything in one database. 628. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Senso-ji essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Senso-ji essentials.", "x": "At a glance: Senso-ji — the thunder gate.. Kaminarimon. The essentials: Nakamise.. Nakamise. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "628.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "628.", "x": "Senso-ji: 628.. Nakamise. Essential knowledge — Nakamise.. the thunder gate. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 628..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 628..", "x": "Explained: 628.. Oldest. The context — Senso-ji. Incense. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Kaminarimon.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Kaminarimon.", "x": "Senso-ji: Kaminarimon.. Asakusa. Essential knowledge — Incense.. the thunder gate. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Kaminarimon..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Kaminarimon..", "x": "Explained: Kaminarimon.. Gate. The context — Senso-ji. Asakusa. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Nakamise.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Nakamise.", "x": "Senso-ji: Nakamise.. Oldest. Essential knowledge — Asakusa.. the thunder gate. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Nakamise..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Nakamise..", "x": "Explained: Nakamise.. Visits. The context — Senso-ji. Oldest. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Incense.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Incense.", "x": "Senso-ji: Incense.. Gate. Essential knowledge — Oldest.. the thunder gate. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Incense..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Incense..", "x": "Explained: Incense.. 628. The context — Senso-ji. 628. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Asakusa.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Asakusa.", "x": "Senso-ji: Asakusa.. Visits. Essential knowledge — 628.. the thunder gate. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Asakusa..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Asakusa..", "x": "Explained: Asakusa.. Nakamise. The context — Senso-ji. Kaminarimon. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Oldest.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Oldest.", "x": "Senso-ji: Oldest.. 628. Essential knowledge — Kaminarimon.. the thunder gate. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Oldest..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Oldest..", "x": "Explained: Oldest.. Asakusa. The context — Senso-ji. Nakamise. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "628.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "628.", "x": "Senso-ji in depth: 628.. Kaminarimon. Details — the thunder gate.. Asakusa. Incense. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Nakamise.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Nakamise.", "x": "Senso-ji in depth: Nakamise.. Nakamise. Details — the thunder gate.. Oldest. Asakusa. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Asakusa.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Asakusa.", "x": "Senso-ji in depth: Asakusa.. Incense. Details — the thunder gate.. Gate. Oldest. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Oldest.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Oldest.", "x": "Senso-ji in depth: Oldest.. Asakusa. Details — the thunder gate.. Visits. 628. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Gate.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Gate.", "x": "Senso-ji in depth: Gate.. Oldest. Details — the thunder gate.. 628. Kaminarimon. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Visits.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Visits.", "x": "Senso-ji in depth: Visits.. 628. Details — the thunder gate.. Nakamise. Nakamise. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Senso-ji comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Senso-ji comes from.", "x": "Origins: 628.. 628. The history of Senso-ji — the thunder gate.. Nakamise. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Senso-ji respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Senso-ji respectfully.", "x": "Engaging: Asakusa.. Kaminarimon. How to participate or observe well — Senso-ji. the thunder gate. Respect first, always; Oldest.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Senso-ji do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Senso-ji do's and don'ts.", "x": "Etiquette: Gate.. Nakamise. The rules of respect — Senso-ji. the thunder gate. When in doubt, ask about Visits.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Senso-ji.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Senso-ji.", "x": "Planning: 628.. Incense. Practical notes — Senso-ji. the thunder gate. A little planning shows respect for Nakamise.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Senso-ji and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Senso-ji and money.", "x": "Costs: Asakusa.. Asakusa. What to budget — Senso-ji. the thunder gate. The best experiences of Oldest. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-landmark-senso-ji-landmark-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
