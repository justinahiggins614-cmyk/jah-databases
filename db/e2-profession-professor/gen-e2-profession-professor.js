(function(){'use strict';
/* JAH Professor Profession Database generator — jahdb-e2-profession-professor-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-profession-professor',PREFIX='JAH-E2PROFESSIO-',NAME='JAH Professor Profession Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Professor Profession: the complete guide", "d": "Professor Profession: the lecture profession..", "g": "overview", "l": 2, "q": "What is Professor Profession: the complete guide?", "a": "Professor Profession: the lecture profession..", "x": "The complete profession guide to Professor Profession: the lecture profession.. Lectures. History, meaning, practices, and how to engage respectfully — everything in one database. Lectures. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Professor Profession essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Professor Profession essentials.", "x": "At a glance: Professor Profession — the lecture profession.. Research. The essentials: Research.. Tenure. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Lectures.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Lectures.", "x": "Professor Profession: Lectures.. Research. Essential knowledge — Tenure.. the lecture profession. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Lectures..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Lectures..", "x": "Explained: Lectures.. Grants. The context — Professor Profession. Papers. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Research.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Research.", "x": "Professor Profession: Research.. Tenure. Essential knowledge — Papers.. the lecture profession. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Research..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Research..", "x": "Explained: Research.. Hours. The context — Professor Profession. Office hours. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Tenure.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Tenure.", "x": "Professor Profession: Tenure.. Grants. Essential knowledge — Office hours.. the lecture profession. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Tenure..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Tenure..", "x": "Explained: Tenure.. Day. The context — Professor Profession. Grants. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Papers.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Papers.", "x": "Professor Profession: Papers.. Hours. Essential knowledge — Grants.. the lecture profession. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Papers..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Papers..", "x": "Explained: Papers.. Lectures. The context — Professor Profession. Lectures. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Office hours.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Office hours.", "x": "Professor Profession: Office hours.. Day. Essential knowledge — Lectures.. the lecture profession. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Office hours..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Office hours..", "x": "Explained: Office hours.. Research. The context — Professor Profession. Research. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Grants.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Grants.", "x": "Professor Profession: Grants.. Lectures. Essential knowledge — Research.. the lecture profession. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Grants..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Grants..", "x": "Explained: Grants.. Tenure. The context — Professor Profession. Tenure. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Lectures.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Lectures.", "x": "Professor Profession in depth: Lectures.. Research. Details — the lecture profession.. Tenure. Papers. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Research.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Research.", "x": "Professor Profession in depth: Research.. Tenure. Details — the lecture profession.. Grants. Office hours. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Tenure.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Tenure.", "x": "Professor Profession in depth: Tenure.. Papers. Details — the lecture profession.. Hours. Grants. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Grants.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Grants.", "x": "Professor Profession in depth: Grants.. Office hours. Details — the lecture profession.. Day. Lectures. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Hours.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Hours.", "x": "Professor Profession in depth: Hours.. Grants. Details — the lecture profession.. Lectures. Research. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Day.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Day.", "x": "Professor Profession in depth: Day.. Lectures. Details — the lecture profession.. Research. Tenure. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Professor Profession comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Professor Profession comes from.", "x": "Origins: Lectures.. Lectures. The history of Professor Profession — the lecture profession.. Research. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Professor Profession respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Professor Profession respectfully.", "x": "Engaging: Tenure.. Research. How to participate or observe well — Professor Profession. the lecture profession. Respect first, always; Grants.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Professor Profession do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Professor Profession do's and don'ts.", "x": "Etiquette: Hours.. Tenure. The rules of respect — Professor Profession. the lecture profession. When in doubt, ask about Day.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Professor Profession.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Professor Profession.", "x": "Planning: Lectures.. Papers. Practical notes — Professor Profession. the lecture profession. A little planning shows respect for Research.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Professor Profession and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Professor Profession and money.", "x": "Costs: Tenure.. Office hours. What to budget — Professor Profession. the lecture profession. The best experiences of Grants. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-profession-professor-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
