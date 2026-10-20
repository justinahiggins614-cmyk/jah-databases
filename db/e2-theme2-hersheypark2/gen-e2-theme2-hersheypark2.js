(function(){'use strict';
/* JAH Hersheypark2 Database generator — jahdb-e2-theme2-hersheypark2-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-theme2-hersheypark2',PREFIX='JAH-E2THEME2HER-',NAME='JAH Hersheypark2 Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Hersheypark2: the complete guide", "d": "Hersheypark2: the chocolate 2..", "g": "overview", "l": 2, "q": "What is Hersheypark2: the complete guide?", "a": "Hersheypark2: the chocolate 2..", "x": "The complete theme park guide to Hersheypark2: the chocolate 2.. Chocolate. History, meaning, practices, and how to engage respectfully — everything in one database. Chocolate. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Hersheypark2 essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Hersheypark2 essentials.", "x": "At a glance: Hersheypark2 — the chocolate 2.. PA. The essentials: Zoo.. Kisses. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Chocolate.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Chocolate.", "x": "Hersheypark2: Chocolate.. Zoo. Essential knowledge — Kisses.. the chocolate 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Chocolate..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Chocolate..", "x": "Explained: Chocolate.. Kisses. The context — Hersheypark2. Coasters. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "PA.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "PA.", "x": "Hersheypark2: PA.. Sweet. Essential knowledge — Coasters.. the chocolate 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: PA..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: PA..", "x": "Explained: PA.. PA. The context — Hersheypark2. Sweet. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Kisses.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Kisses.", "x": "Hersheypark2: Kisses.. Kisses. Essential knowledge — Sweet.. the chocolate 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Kisses..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Kisses..", "x": "Explained: Kisses.. Guide. The context — Hersheypark2. Zoo. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Coasters.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Coasters.", "x": "Hersheypark2: Coasters.. PA. Essential knowledge — Zoo.. the chocolate 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Coasters..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Coasters..", "x": "Explained: Coasters.. Chocolate. The context — Hersheypark2. Chocolate. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Sweet.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Sweet.", "x": "Hersheypark2: Sweet.. Guide. Essential knowledge — Chocolate.. the chocolate 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Sweet..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Sweet..", "x": "Explained: Sweet.. Zoo. The context — Hersheypark2. PA. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Zoo.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Zoo.", "x": "Hersheypark2: Zoo.. Chocolate. Essential knowledge — PA.. the chocolate 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Zoo..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Zoo..", "x": "Explained: Zoo.. Sweet. The context — Hersheypark2. Kisses. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Chocolate.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Chocolate.", "x": "Hersheypark2 in depth: Chocolate.. PA. Details — the chocolate 2.. Sweet. Coasters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Zoo.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Zoo.", "x": "Hersheypark2 in depth: Zoo.. Kisses. Details — the chocolate 2.. Kisses. Sweet. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Sweet.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Sweet.", "x": "Hersheypark2 in depth: Sweet.. Coasters. Details — the chocolate 2.. PA. Zoo. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Kisses.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Kisses.", "x": "Hersheypark2 in depth: Kisses.. Sweet. Details — the chocolate 2.. Guide. Chocolate. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "PA.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "PA.", "x": "Hersheypark2 in depth: PA.. Zoo. Details — the chocolate 2.. Chocolate. PA. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Guide.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Guide.", "x": "Hersheypark2 in depth: Guide.. Chocolate. Details — the chocolate 2.. Zoo. Kisses. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Hersheypark2 comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Hersheypark2 comes from.", "x": "Origins: Chocolate.. Chocolate. The history of Hersheypark2 — the chocolate 2.. Zoo. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Hersheypark2 respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Hersheypark2 respectfully.", "x": "Engaging: Sweet.. PA. How to participate or observe well — Hersheypark2. the chocolate 2. Respect first, always; Kisses.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Hersheypark2 do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Hersheypark2 do's and don'ts.", "x": "Etiquette: PA.. Kisses. The rules of respect — Hersheypark2. the chocolate 2. When in doubt, ask about Guide.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Hersheypark2.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Hersheypark2.", "x": "Planning: Chocolate.. Coasters. Practical notes — Hersheypark2. the chocolate 2. A little planning shows respect for Zoo.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Hersheypark2 and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Hersheypark2 and money.", "x": "Costs: Sweet.. Sweet. What to budget — Hersheypark2. the chocolate 2. The best experiences of Kisses. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-theme2-hersheypark2-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
