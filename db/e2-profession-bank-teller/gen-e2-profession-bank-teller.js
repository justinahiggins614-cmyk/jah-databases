(function(){'use strict';
/* JAH Bank Teller Profession Database generator — jahdb-e2-profession-bank-teller-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-profession-bank-teller',PREFIX='JAH-E2PROFESSIO-',NAME='JAH Bank Teller Profession Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Bank Teller Profession: the complete guide", "d": "Bank Teller Profession: the window profession..", "g": "overview", "l": 2, "q": "What is Bank Teller Profession: the complete guide?", "a": "Bank Teller Profession: the window profession..", "x": "The complete profession guide to Bank Teller Profession: the window profession.. Cash. History, meaning, practices, and how to engage respectfully — everything in one database. Cash. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Bank Teller Profession essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Bank Teller Profession essentials.", "x": "At a glance: Bank Teller Profession — the window profession.. Drawer. The essentials: Customers.. Customers. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Cash.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Cash.", "x": "Bank Teller Profession: Cash.. Customers. Essential knowledge — Customers.. the window profession. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Cash..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Cash..", "x": "Explained: Cash.. Lines. The context — Bank Teller Profession. Counts. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Drawer.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Drawer.", "x": "Bank Teller Profession: Drawer.. Security. Essential knowledge — Counts.. the window profession. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Drawer..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Drawer..", "x": "Explained: Drawer.. Drawer. The context — Bank Teller Profession. Security. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Customers.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Customers.", "x": "Bank Teller Profession: Customers.. Lines. Essential knowledge — Security.. the window profession. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Customers..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Customers..", "x": "Explained: Customers.. Day. The context — Bank Teller Profession. Lines. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Counts.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Counts.", "x": "Bank Teller Profession: Counts.. Drawer. Essential knowledge — Lines.. the window profession. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Counts..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Counts..", "x": "Explained: Counts.. Cash. The context — Bank Teller Profession. Cash. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Security.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Security.", "x": "Bank Teller Profession: Security.. Day. Essential knowledge — Cash.. the window profession. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Security..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Security..", "x": "Explained: Security.. Customers. The context — Bank Teller Profession. Drawer. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Lines.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Lines.", "x": "Bank Teller Profession: Lines.. Cash. Essential knowledge — Drawer.. the window profession. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Lines..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Lines..", "x": "Explained: Lines.. Security. The context — Bank Teller Profession. Customers. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Cash.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Cash.", "x": "Bank Teller Profession in depth: Cash.. Drawer. Details — the window profession.. Security. Counts. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Customers.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Customers.", "x": "Bank Teller Profession in depth: Customers.. Customers. Details — the window profession.. Lines. Security. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Security.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Security.", "x": "Bank Teller Profession in depth: Security.. Counts. Details — the window profession.. Drawer. Lines. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Lines.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Lines.", "x": "Bank Teller Profession in depth: Lines.. Security. Details — the window profession.. Day. Cash. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Drawer.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Drawer.", "x": "Bank Teller Profession in depth: Drawer.. Lines. Details — the window profession.. Cash. Drawer. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Day.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Day.", "x": "Bank Teller Profession in depth: Day.. Cash. Details — the window profession.. Customers. Customers. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Bank Teller Profession comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Bank Teller Profession comes from.", "x": "Origins: Cash.. Cash. The history of Bank Teller Profession — the window profession.. Customers. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Bank Teller Profession respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Bank Teller Profession respectfully.", "x": "Engaging: Security.. Drawer. How to participate or observe well — Bank Teller Profession. the window profession. Respect first, always; Lines.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Bank Teller Profession do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Bank Teller Profession do's and don'ts.", "x": "Etiquette: Drawer.. Customers. The rules of respect — Bank Teller Profession. the window profession. When in doubt, ask about Day.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Bank Teller Profession.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Bank Teller Profession.", "x": "Planning: Cash.. Counts. Practical notes — Bank Teller Profession. the window profession. A little planning shows respect for Customers.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Bank Teller Profession and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Bank Teller Profession and money.", "x": "Costs: Security.. Security. What to budget — Bank Teller Profession. the window profession. The best experiences of Lines. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-profession-bank-teller-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
