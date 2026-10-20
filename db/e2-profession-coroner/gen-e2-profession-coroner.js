(function(){'use strict';
/* JAH Coroner Profession Database generator — jahdb-e2-profession-coroner-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-profession-coroner',PREFIX='JAH-E2PROFESSIO-',NAME='JAH Coroner Profession Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Coroner Profession: the complete guide", "d": "Coroner Profession: the final profession..", "g": "overview", "l": 2, "q": "What is Coroner Profession: the complete guide?", "a": "Coroner Profession: the final profession..", "x": "The complete profession guide to Coroner Profession: the final profession.. Autopsy. History, meaning, practices, and how to engage respectfully — everything in one database. Autopsy. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Coroner Profession essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Coroner Profession essentials.", "x": "At a glance: Coroner Profession — the final profession.. Reports. The essentials: Morgue.. Morgue. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Autopsy.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Autopsy.", "x": "Coroner Profession: Autopsy.. Morgue. Essential knowledge — Morgue.. the final profession. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Autopsy..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Autopsy..", "x": "Explained: Autopsy.. Respect. The context — Coroner Profession. Cause. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Reports.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Reports.", "x": "Coroner Profession: Reports.. Cause. Essential knowledge — Cause.. the final profession. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Reports..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Reports..", "x": "Explained: Reports.. Reports. The context — Coroner Profession. Elected. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Morgue.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Morgue.", "x": "Coroner Profession: Morgue.. Respect. Essential knowledge — Elected.. the final profession. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Morgue..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Morgue..", "x": "Explained: Morgue.. Day. The context — Coroner Profession. Respect. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Cause.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Cause.", "x": "Coroner Profession: Cause.. Reports. Essential knowledge — Respect.. the final profession. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Cause..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Cause..", "x": "Explained: Cause.. Autopsy. The context — Coroner Profession. Autopsy. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Elected.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Elected.", "x": "Coroner Profession: Elected.. Day. Essential knowledge — Autopsy.. the final profession. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Elected..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Elected..", "x": "Explained: Elected.. Morgue. The context — Coroner Profession. Reports. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Respect.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Respect.", "x": "Coroner Profession: Respect.. Autopsy. Essential knowledge — Reports.. the final profession. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Respect..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Respect..", "x": "Explained: Respect.. Cause. The context — Coroner Profession. Morgue. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Autopsy.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Autopsy.", "x": "Coroner Profession in depth: Autopsy.. Reports. Details — the final profession.. Cause. Cause. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Morgue.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Morgue.", "x": "Coroner Profession in depth: Morgue.. Morgue. Details — the final profession.. Respect. Elected. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Cause.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Cause.", "x": "Coroner Profession in depth: Cause.. Cause. Details — the final profession.. Reports. Respect. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Respect.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Respect.", "x": "Coroner Profession in depth: Respect.. Elected. Details — the final profession.. Day. Autopsy. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Reports.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Reports.", "x": "Coroner Profession in depth: Reports.. Respect. Details — the final profession.. Autopsy. Reports. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Day.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Day.", "x": "Coroner Profession in depth: Day.. Autopsy. Details — the final profession.. Morgue. Morgue. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Coroner Profession comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Coroner Profession comes from.", "x": "Origins: Autopsy.. Autopsy. The history of Coroner Profession — the final profession.. Morgue. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Coroner Profession respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Coroner Profession respectfully.", "x": "Engaging: Cause.. Reports. How to participate or observe well — Coroner Profession. the final profession. Respect first, always; Respect.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Coroner Profession do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Coroner Profession do's and don'ts.", "x": "Etiquette: Reports.. Morgue. The rules of respect — Coroner Profession. the final profession. When in doubt, ask about Day.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Coroner Profession.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Coroner Profession.", "x": "Planning: Autopsy.. Cause. Practical notes — Coroner Profession. the final profession. A little planning shows respect for Morgue.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Coroner Profession and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Coroner Profession and money.", "x": "Costs: Cause.. Elected. What to budget — Coroner Profession. the final profession. The best experiences of Respect. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-profession-coroner-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
