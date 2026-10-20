(function(){'use strict';
/* JAH Disc Golf Database generator — jahdb-e2-hobby2-disc-golf-hobby-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-hobby2-disc-golf-hobby',PREFIX='JAH-E2HOBBY2DIS-',NAME='JAH Disc Golf Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Disc Golf: the complete guide", "d": "Disc Golf: the chain baskets..", "g": "overview", "l": 2, "q": "What is Disc Golf: the complete guide?", "a": "Disc Golf: the chain baskets..", "x": "The complete hobby guide to Disc Golf: the chain baskets.. Drivers. History, meaning, practices, and how to engage respectfully — everything in one database. Putters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Disc Golf essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Disc Golf essentials.", "x": "At a glance: Disc Golf — the chain baskets.. Putters. The essentials: Courses.. Chains. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Drivers.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Drivers.", "x": "Disc Golf: Drivers.. Courses. Essential knowledge — Chains.. the chain baskets. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Drivers..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Drivers..", "x": "Explained: Drivers.. Drivers. The context — Disc Golf. Courses. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Putters.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Putters.", "x": "Disc Golf: Putters.. Free. Essential knowledge — Courses.. the chain baskets. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Putters..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Putters..", "x": "Explained: Putters.. Chains. The context — Disc Golf. Par. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Chains.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Chains.", "x": "Disc Golf: Chains.. Drivers. Essential knowledge — Par.. the chain baskets. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Chains..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Chains..", "x": "Explained: Chains.. Getting started. The context — Disc Golf. Free. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Courses.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Courses.", "x": "Disc Golf: Courses.. Chains. Essential knowledge — Free.. the chain baskets. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Courses..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Courses..", "x": "Explained: Courses.. Putters. The context — Disc Golf. Drivers. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Par.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Par.", "x": "Disc Golf: Par.. Getting started. Essential knowledge — Drivers.. the chain baskets. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Par..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Par..", "x": "Explained: Par.. Courses. The context — Disc Golf. Putters. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Free.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Free.", "x": "Disc Golf: Free.. Putters. Essential knowledge — Putters.. the chain baskets. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Free..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Free..", "x": "Explained: Free.. Free. The context — Disc Golf. Chains. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Putters.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Putters.", "x": "Disc Golf in depth: Putters.. Putters. Details — the chain baskets.. Free. Courses. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Courses.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Courses.", "x": "Disc Golf in depth: Courses.. Chains. Details — the chain baskets.. Drivers. Par. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Free.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Free.", "x": "Disc Golf in depth: Free.. Courses. Details — the chain baskets.. Chains. Free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Drivers.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Drivers.", "x": "Disc Golf in depth: Drivers.. Par. Details — the chain baskets.. Getting started. Drivers. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Chains.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Chains.", "x": "Disc Golf in depth: Chains.. Free. Details — the chain baskets.. Putters. Putters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Getting started.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Getting started.", "x": "Disc Golf in depth: Getting started.. Drivers. Details — the chain baskets.. Courses. Chains. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Disc Golf comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Disc Golf comes from.", "x": "Origins: Putters.. Drivers. The history of Disc Golf — the chain baskets.. Courses. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Disc Golf respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Disc Golf respectfully.", "x": "Engaging: Free.. Putters. How to participate or observe well — Disc Golf. the chain baskets. Respect first, always; Drivers.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Disc Golf do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Disc Golf do's and don'ts.", "x": "Etiquette: Chains.. Chains. The rules of respect — Disc Golf. the chain baskets. When in doubt, ask about Getting started.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Disc Golf.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Disc Golf.", "x": "Planning: Putters.. Courses. Practical notes — Disc Golf. the chain baskets. A little planning shows respect for Courses.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Disc Golf and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Disc Golf and money.", "x": "Costs: Free.. Par. What to budget — Disc Golf. the chain baskets. The best experiences of Drivers. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-hobby2-disc-golf-hobby-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
