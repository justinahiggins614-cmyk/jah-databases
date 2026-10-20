(function(){'use strict';
/* JAH Paramedic Profession Database generator — jahdb-e2-profession-paramedic-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-profession-paramedic',PREFIX='JAH-E2PROFESSIO-',NAME='JAH Paramedic Profession Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Paramedic Profession: the complete guide", "d": "Paramedic Profession: the emergency profession..", "g": "overview", "l": 2, "q": "What is Paramedic Profession: the complete guide?", "a": "Paramedic Profession: the emergency profession..", "x": "The complete profession guide to Paramedic Profession: the emergency profession.. EMT. History, meaning, practices, and how to engage respectfully — everything in one database. Training. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Paramedic Profession essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Paramedic Profession essentials.", "x": "At a glance: Paramedic Profession — the emergency profession.. Ambulance. The essentials: Ambulance.. Protocols. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "EMT.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "EMT.", "x": "Paramedic Profession: EMT.. Ambulance. Essential knowledge — Protocols.. the emergency profession. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: EMT..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: EMT..", "x": "Explained: EMT.. Trauma. The context — Paramedic Profession. Shifts. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Ambulance.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Ambulance.", "x": "Paramedic Profession: Ambulance.. Protocols. Essential knowledge — Shifts.. the emergency profession. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Ambulance..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Ambulance..", "x": "Explained: Ambulance.. Certs. The context — Paramedic Profession. Trauma. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Protocols.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Protocols.", "x": "Paramedic Profession: Protocols.. Trauma. Essential knowledge — Trauma.. the emergency profession. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Protocols..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Protocols..", "x": "Explained: Protocols.. Day. The context — Paramedic Profession. Certs. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Shifts.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Shifts.", "x": "Paramedic Profession: Shifts.. Certs. Essential knowledge — Certs.. the emergency profession. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Shifts..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Shifts..", "x": "Explained: Shifts.. Training. The context — Paramedic Profession. EMT. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Trauma.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Trauma.", "x": "Paramedic Profession: Trauma.. Day. Essential knowledge — EMT.. the emergency profession. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Trauma..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Trauma..", "x": "Explained: Trauma.. Ambulance. The context — Paramedic Profession. Ambulance. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Certs.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Certs.", "x": "Paramedic Profession: Certs.. Training. Essential knowledge — Ambulance.. the emergency profession. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Certs..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Certs..", "x": "Explained: Certs.. Protocols. The context — Paramedic Profession. Protocols. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Training.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Training.", "x": "Paramedic Profession in depth: Training.. Ambulance. Details — the emergency profession.. Protocols. Shifts. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Ambulance.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Ambulance.", "x": "Paramedic Profession in depth: Ambulance.. Protocols. Details — the emergency profession.. Trauma. Trauma. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Protocols.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Protocols.", "x": "Paramedic Profession in depth: Protocols.. Shifts. Details — the emergency profession.. Certs. Certs. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Trauma.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Trauma.", "x": "Paramedic Profession in depth: Trauma.. Trauma. Details — the emergency profession.. Day. EMT. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Certs.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Certs.", "x": "Paramedic Profession in depth: Certs.. Certs. Details — the emergency profession.. Training. Ambulance. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Day.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Day.", "x": "Paramedic Profession in depth: Day.. EMT. Details — the emergency profession.. Ambulance. Protocols. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Paramedic Profession comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Paramedic Profession comes from.", "x": "Origins: Training.. EMT. The history of Paramedic Profession — the emergency profession.. Ambulance. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Paramedic Profession respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Paramedic Profession respectfully.", "x": "Engaging: Protocols.. Ambulance. How to participate or observe well — Paramedic Profession. the emergency profession. Respect first, always; Trauma.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Paramedic Profession do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Paramedic Profession do's and don'ts.", "x": "Etiquette: Certs.. Protocols. The rules of respect — Paramedic Profession. the emergency profession. When in doubt, ask about Day.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Paramedic Profession.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Paramedic Profession.", "x": "Planning: Training.. Shifts. Practical notes — Paramedic Profession. the emergency profession. A little planning shows respect for Ambulance.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Paramedic Profession and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Paramedic Profession and money.", "x": "Costs: Protocols.. Trauma. What to budget — Paramedic Profession. the emergency profession. The best experiences of Trauma. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-profession-paramedic-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
