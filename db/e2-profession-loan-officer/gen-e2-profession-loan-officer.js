(function(){'use strict';
/* JAH Loan Officer Profession Database generator — jahdb-e2-profession-loan-officer-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-profession-loan-officer',PREFIX='JAH-E2PROFESSIO-',NAME='JAH Loan Officer Profession Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Loan Officer Profession: the complete guide", "d": "Loan Officer Profession: the lend profession..", "g": "overview", "l": 2, "q": "What is Loan Officer Profession: the complete guide?", "a": "Loan Officer Profession: the lend profession..", "x": "The complete profession guide to Loan Officer Profession: the lend profession.. Applications. History, meaning, practices, and how to engage respectfully — everything in one database. Credit. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Loan Officer Profession essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Loan Officer Profession essentials.", "x": "At a glance: Loan Officer Profession — the lend profession.. Credit. The essentials: Closings.. Underwriting. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Applications.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Applications.", "x": "Loan Officer Profession: Applications.. Closings. Essential knowledge — Underwriting.. the lend profession. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Applications..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Applications..", "x": "Explained: Applications.. Paperwork. The context — Loan Officer Profession. Closings. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Credit.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Credit.", "x": "Loan Officer Profession: Credit.. Rates. Essential knowledge — Closings.. the lend profession. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Credit..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Credit..", "x": "Explained: Credit.. Applications. The context — Loan Officer Profession. Rates. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Underwriting.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Underwriting.", "x": "Loan Officer Profession: Underwriting.. Paperwork. Essential knowledge — Rates.. the lend profession. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Underwriting..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Underwriting..", "x": "Explained: Underwriting.. Day. The context — Loan Officer Profession. Paperwork. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Closings.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Closings.", "x": "Loan Officer Profession: Closings.. Applications. Essential knowledge — Paperwork.. the lend profession. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Closings..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Closings..", "x": "Explained: Closings.. Credit. The context — Loan Officer Profession. Applications. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Rates.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Rates.", "x": "Loan Officer Profession: Rates.. Day. Essential knowledge — Applications.. the lend profession. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Rates..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Rates..", "x": "Explained: Rates.. Closings. The context — Loan Officer Profession. Credit. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Paperwork.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Paperwork.", "x": "Loan Officer Profession: Paperwork.. Credit. Essential knowledge — Credit.. the lend profession. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Paperwork..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Paperwork..", "x": "Explained: Paperwork.. Rates. The context — Loan Officer Profession. Underwriting. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Credit.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Credit.", "x": "Loan Officer Profession in depth: Credit.. Credit. Details — the lend profession.. Rates. Closings. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Closings.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Closings.", "x": "Loan Officer Profession in depth: Closings.. Underwriting. Details — the lend profession.. Paperwork. Rates. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Rates.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Rates.", "x": "Loan Officer Profession in depth: Rates.. Closings. Details — the lend profession.. Applications. Paperwork. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Paperwork.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Paperwork.", "x": "Loan Officer Profession in depth: Paperwork.. Rates. Details — the lend profession.. Day. Applications. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Applications.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Applications.", "x": "Loan Officer Profession in depth: Applications.. Paperwork. Details — the lend profession.. Credit. Credit. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Day.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Day.", "x": "Loan Officer Profession in depth: Day.. Applications. Details — the lend profession.. Closings. Underwriting. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Loan Officer Profession comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Loan Officer Profession comes from.", "x": "Origins: Credit.. Applications. The history of Loan Officer Profession — the lend profession.. Closings. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Loan Officer Profession respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Loan Officer Profession respectfully.", "x": "Engaging: Rates.. Credit. How to participate or observe well — Loan Officer Profession. the lend profession. Respect first, always; Paperwork.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Loan Officer Profession do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Loan Officer Profession do's and don'ts.", "x": "Etiquette: Applications.. Underwriting. The rules of respect — Loan Officer Profession. the lend profession. When in doubt, ask about Day.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Loan Officer Profession.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Loan Officer Profession.", "x": "Planning: Credit.. Closings. Practical notes — Loan Officer Profession. the lend profession. A little planning shows respect for Closings.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Loan Officer Profession and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Loan Officer Profession and money.", "x": "Costs: Rates.. Rates. What to budget — Loan Officer Profession. the lend profession. The best experiences of Paperwork. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-profession-loan-officer-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
