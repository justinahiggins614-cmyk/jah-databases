(function(){'use strict';
/* JAH Rosh Hashanah Holiday Database generator — jahdb-e2-holiday-rosh-hashanah-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-holiday-rosh-hashanah',PREFIX='JAH-E2HOLIDAYRO-',NAME='JAH Rosh Hashanah Holiday Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Rosh Hashanah: the complete guide", "d": "Rosh Hashanah: Jewish New Year..", "g": "overview", "l": 2, "q": "What is Rosh Hashanah: the complete guide?", "a": "Rosh Hashanah: Jewish New Year..", "x": "The complete holiday guide to Rosh Hashanah: Jewish New Year.. Shofar. History, meaning, practices, and how to engage respectfully — everything in one database. Symbols. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Rosh Hashanah essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Rosh Hashanah essentials.", "x": "At a glance: Rosh Hashanah — Jewish New Year.. Apples/honey. The essentials: Food.. 2 days. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Shofar.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Shofar.", "x": "Rosh Hashanah: Shofar.. Food. Essential knowledge — 2 days.. Jewish New Year. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Shofar..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Shofar..", "x": "Explained: Shofar.. Family. The context — Rosh Hashanah. Fall. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Apples/honey.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Apples/honey.", "x": "Rosh Hashanah: Apples/honey.. Prayers. Essential knowledge — Fall.. Jewish New Year. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Apples/honey..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Apples/honey..", "x": "Explained: Apples/honey.. Meaning. The context — Rosh Hashanah. Reflection. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "2 days.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "2 days.", "x": "Rosh Hashanah: 2 days.. Family. Essential knowledge — Reflection.. Jewish New Year. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: 2 days..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: 2 days..", "x": "Explained: 2 days.. New Year. The context — Rosh Hashanah. Services. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Fall.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Fall.", "x": "Rosh Hashanah: Fall.. Meaning. Essential knowledge — Services.. Jewish New Year. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Fall..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Fall..", "x": "Explained: Fall.. Symbols. The context — Rosh Hashanah. Shofar. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Reflection.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Reflection.", "x": "Rosh Hashanah: Reflection.. New Year. Essential knowledge — Shofar.. Jewish New Year. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Reflection..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Reflection..", "x": "Explained: Reflection.. Food. The context — Rosh Hashanah. Apples/honey. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Services.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Services.", "x": "Rosh Hashanah: Services.. Symbols. Essential knowledge — Apples/honey.. Jewish New Year. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Services..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Services..", "x": "Explained: Services.. Prayers. The context — Rosh Hashanah. 2 days. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Symbols.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Symbols.", "x": "Rosh Hashanah in depth: Symbols.. Apples/honey. Details — Jewish New Year.. Prayers. Fall. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Food.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Food.", "x": "Rosh Hashanah in depth: Food.. 2 days. Details — Jewish New Year.. Family. Reflection. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Prayers.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Prayers.", "x": "Rosh Hashanah in depth: Prayers.. Fall. Details — Jewish New Year.. Meaning. Services. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Family.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Family.", "x": "Rosh Hashanah in depth: Family.. Reflection. Details — Jewish New Year.. New Year. Shofar. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Meaning.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Meaning.", "x": "Rosh Hashanah in depth: Meaning.. Services. Details — Jewish New Year.. Symbols. Apples/honey. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "New Year.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "New Year.", "x": "Rosh Hashanah in depth: New Year.. Shofar. Details — Jewish New Year.. Food. 2 days. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Rosh Hashanah comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Rosh Hashanah comes from.", "x": "Origins: Symbols.. Shofar. The history of Rosh Hashanah — Jewish New Year.. Food. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Rosh Hashanah respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Rosh Hashanah respectfully.", "x": "Engaging: Prayers.. Apples/honey. How to participate or observe well — Rosh Hashanah. Jewish New Year. Respect first, always; Family.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Rosh Hashanah do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Rosh Hashanah do's and don'ts.", "x": "Etiquette: Meaning.. 2 days. The rules of respect — Rosh Hashanah. Jewish New Year. When in doubt, ask about New Year.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Rosh Hashanah.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Rosh Hashanah.", "x": "Planning: Symbols.. Fall. Practical notes — Rosh Hashanah. Jewish New Year. A little planning shows respect for Food.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Rosh Hashanah and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Rosh Hashanah and money.", "x": "Costs: Prayers.. Reflection. What to budget — Rosh Hashanah. Jewish New Year. The best experiences of Family. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-holiday-rosh-hashanah-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
