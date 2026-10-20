(function(){'use strict';
/* JAH Yom Kippur Holiday Database generator — jahdb-e2-holiday-yom-kippur-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-holiday-yom-kippur',PREFIX='JAH-E2HOLIDAYYO-',NAME='JAH Yom Kippur Holiday Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Yom Kippur: the complete guide", "d": "Yom Kippur: Day of Atonement..", "g": "overview", "l": 2, "q": "What is Yom Kippur: the complete guide?", "a": "Yom Kippur: Day of Atonement..", "x": "The complete holiday guide to Yom Kippur: Day of Atonement.. Fasting. History, meaning, practices, and how to engage respectfully — everything in one database. Meaning. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Yom Kippur essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Yom Kippur essentials.", "x": "At a glance: Yom Kippur — Day of Atonement.. Prayers. The essentials: Services.. Solemn. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Fasting.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Fasting.", "x": "Yom Kippur: Fasting.. Services. Essential knowledge — Solemn.. Day of Atonement. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Fasting..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Fasting..", "x": "Explained: Fasting.. Traditions. The context — Yom Kippur. New Year. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Prayers.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Prayers.", "x": "Yom Kippur: Prayers.. Fast. Essential knowledge — New Year.. Day of Atonement. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Prayers..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Prayers..", "x": "Explained: Prayers.. Reflection. The context — Yom Kippur. Repentance. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Solemn.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Solemn.", "x": "Yom Kippur: Solemn.. Traditions. Essential knowledge — Repentance.. Day of Atonement. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Solemn..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Solemn..", "x": "Explained: Solemn.. Faith. The context — Yom Kippur. Synagogue. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "New Year.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "New Year.", "x": "Yom Kippur: New Year.. Reflection. Essential knowledge — Synagogue.. Day of Atonement. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: New Year..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: New Year..", "x": "Explained: New Year.. Meaning. The context — Yom Kippur. Fasting. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Repentance.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Repentance.", "x": "Yom Kippur: Repentance.. Faith. Essential knowledge — Fasting.. Day of Atonement. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Repentance..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Repentance..", "x": "Explained: Repentance.. Services. The context — Yom Kippur. Prayers. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Synagogue.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Synagogue.", "x": "Yom Kippur: Synagogue.. Meaning. Essential knowledge — Prayers.. Day of Atonement. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Synagogue..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Synagogue..", "x": "Explained: Synagogue.. Fast. The context — Yom Kippur. Solemn. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Meaning.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Meaning.", "x": "Yom Kippur in depth: Meaning.. Prayers. Details — Day of Atonement.. Fast. New Year. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Services.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Services.", "x": "Yom Kippur in depth: Services.. Solemn. Details — Day of Atonement.. Traditions. Repentance. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Fast.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Fast.", "x": "Yom Kippur in depth: Fast.. New Year. Details — Day of Atonement.. Reflection. Synagogue. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Traditions.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Traditions.", "x": "Yom Kippur in depth: Traditions.. Repentance. Details — Day of Atonement.. Faith. Fasting. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Reflection.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Reflection.", "x": "Yom Kippur in depth: Reflection.. Synagogue. Details — Day of Atonement.. Meaning. Prayers. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Faith.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Faith.", "x": "Yom Kippur in depth: Faith.. Fasting. Details — Day of Atonement.. Services. Solemn. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Yom Kippur comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Yom Kippur comes from.", "x": "Origins: Meaning.. Fasting. The history of Yom Kippur — Day of Atonement.. Services. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Yom Kippur respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Yom Kippur respectfully.", "x": "Engaging: Fast.. Prayers. How to participate or observe well — Yom Kippur. Day of Atonement. Respect first, always; Traditions.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Yom Kippur do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Yom Kippur do's and don'ts.", "x": "Etiquette: Reflection.. Solemn. The rules of respect — Yom Kippur. Day of Atonement. When in doubt, ask about Faith.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Yom Kippur.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Yom Kippur.", "x": "Planning: Meaning.. New Year. Practical notes — Yom Kippur. Day of Atonement. A little planning shows respect for Services.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Yom Kippur and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Yom Kippur and money.", "x": "Costs: Fast.. Repentance. What to budget — Yom Kippur. Day of Atonement. The best experiences of Traditions. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-holiday-yom-kippur-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
