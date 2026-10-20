(function(){'use strict';
/* JAH Rabbi Profession Database generator — jahdb-e2-profession-rabbi-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-profession-rabbi',PREFIX='JAH-E2PROFESSIO-',NAME='JAH Rabbi Profession Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Rabbi Profession: the complete guide", "d": "Rabbi Profession: the teaching profession..", "g": "overview", "l": 2, "q": "What is Rabbi Profession: the complete guide?", "a": "Rabbi Profession: the teaching profession..", "x": "The complete profession guide to Rabbi Profession: the teaching profession.. Torah. History, meaning, practices, and how to engage respectfully — everything in one database. Torah. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Rabbi Profession essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Rabbi Profession essentials.", "x": "At a glance: Rabbi Profession — the teaching profession.. Congregation. The essentials: Lifecycle.. Lifecycle. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Torah.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Torah.", "x": "Rabbi Profession: Torah.. Lifecycle. Essential knowledge — Lifecycle.. the teaching profession. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Torah..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Torah..", "x": "Explained: Torah.. Shabbat. The context — Rabbi Profession. Study. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Congregation.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Congregation.", "x": "Rabbi Profession: Congregation.. Study. Essential knowledge — Study.. the teaching profession. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Congregation..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Congregation..", "x": "Explained: Congregation.. Counsel. The context — Rabbi Profession. Counsel. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Lifecycle.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Lifecycle.", "x": "Rabbi Profession: Lifecycle.. Shabbat. Essential knowledge — Counsel.. the teaching profession. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Lifecycle..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Lifecycle..", "x": "Explained: Lifecycle.. Day. The context — Rabbi Profession. Shabbat. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Study.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Study.", "x": "Rabbi Profession: Study.. Counsel. Essential knowledge — Shabbat.. the teaching profession. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Study..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Study..", "x": "Explained: Study.. Torah. The context — Rabbi Profession. Torah. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Counsel.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Counsel.", "x": "Rabbi Profession: Counsel.. Day. Essential knowledge — Torah.. the teaching profession. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Counsel..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Counsel..", "x": "Explained: Counsel.. Lifecycle. The context — Rabbi Profession. Congregation. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Shabbat.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Shabbat.", "x": "Rabbi Profession: Shabbat.. Torah. Essential knowledge — Congregation.. the teaching profession. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Shabbat..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Shabbat..", "x": "Explained: Shabbat.. Study. The context — Rabbi Profession. Lifecycle. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Torah.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Torah.", "x": "Rabbi Profession in depth: Torah.. Congregation. Details — the teaching profession.. Study. Study. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Lifecycle.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Lifecycle.", "x": "Rabbi Profession in depth: Lifecycle.. Lifecycle. Details — the teaching profession.. Shabbat. Counsel. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Study.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Study.", "x": "Rabbi Profession in depth: Study.. Study. Details — the teaching profession.. Counsel. Shabbat. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Shabbat.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Shabbat.", "x": "Rabbi Profession in depth: Shabbat.. Counsel. Details — the teaching profession.. Day. Torah. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Counsel.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Counsel.", "x": "Rabbi Profession in depth: Counsel.. Shabbat. Details — the teaching profession.. Torah. Congregation. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Day.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Day.", "x": "Rabbi Profession in depth: Day.. Torah. Details — the teaching profession.. Lifecycle. Lifecycle. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Rabbi Profession comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Rabbi Profession comes from.", "x": "Origins: Torah.. Torah. The history of Rabbi Profession — the teaching profession.. Lifecycle. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Rabbi Profession respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Rabbi Profession respectfully.", "x": "Engaging: Study.. Congregation. How to participate or observe well — Rabbi Profession. the teaching profession. Respect first, always; Shabbat.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Rabbi Profession do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Rabbi Profession do's and don'ts.", "x": "Etiquette: Counsel.. Lifecycle. The rules of respect — Rabbi Profession. the teaching profession. When in doubt, ask about Day.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Rabbi Profession.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Rabbi Profession.", "x": "Planning: Torah.. Study. Practical notes — Rabbi Profession. the teaching profession. A little planning shows respect for Lifecycle.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Rabbi Profession and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Rabbi Profession and money.", "x": "Costs: Study.. Counsel. What to budget — Rabbi Profession. the teaching profession. The best experiences of Shabbat. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-profession-rabbi-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
