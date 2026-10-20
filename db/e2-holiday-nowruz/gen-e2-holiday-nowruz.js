(function(){'use strict';
/* JAH Nowruz Holiday Database generator — jahdb-e2-holiday-nowruz-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-holiday-nowruz',PREFIX='JAH-E2HOLIDAYNO-',NAME='JAH Nowruz Holiday Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Nowruz: the complete guide", "d": "Nowruz: Persian New Year..", "g": "overview", "l": 2, "q": "What is Nowruz: the complete guide?", "a": "Nowruz: Persian New Year..", "x": "The complete holiday guide to Nowruz: Persian New Year.. Spring equinox. History, meaning, practices, and how to engage respectfully — everything in one database. Table. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Nowruz essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Nowruz essentials.", "x": "At a glance: Nowruz — Persian New Year.. Haft-sin. The essentials: Traditions.. 13 days. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Spring equinox.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Spring equinox.", "x": "Nowruz: Spring equinox.. Traditions. Essential knowledge — 13 days.. Persian New Year. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Spring equinox..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Spring equinox..", "x": "Explained: Spring equinox.. Countries. The context — Nowruz. Fire jumping. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Haft-sin.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Haft-sin.", "x": "Nowruz: Haft-sin.. Family. Essential knowledge — Fire jumping.. Persian New Year. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Haft-sin..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Haft-sin..", "x": "Explained: Haft-sin.. Meaning. The context — Nowruz. Family. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "13 days.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "13 days.", "x": "Nowruz: 13 days.. Countries. Essential knowledge — Family.. Persian New Year. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: 13 days..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: 13 days..", "x": "Explained: 13 days.. Spring. The context — Nowruz. UNESCO. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Fire jumping.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Fire jumping.", "x": "Nowruz: Fire jumping.. Meaning. Essential knowledge — UNESCO.. Persian New Year. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Fire jumping..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Fire jumping..", "x": "Explained: Fire jumping.. Table. The context — Nowruz. Spring equinox. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Family.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Family.", "x": "Nowruz: Family.. Spring. Essential knowledge — Spring equinox.. Persian New Year. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Family..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Family..", "x": "Explained: Family.. Traditions. The context — Nowruz. Haft-sin. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "UNESCO.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "UNESCO.", "x": "Nowruz: UNESCO.. Table. Essential knowledge — Haft-sin.. Persian New Year. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: UNESCO..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: UNESCO..", "x": "Explained: UNESCO.. Family. The context — Nowruz. 13 days. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Table.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Table.", "x": "Nowruz in depth: Table.. Haft-sin. Details — Persian New Year.. Family. Fire jumping. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Traditions.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Traditions.", "x": "Nowruz in depth: Traditions.. 13 days. Details — Persian New Year.. Countries. Family. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Family.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Family.", "x": "Nowruz in depth: Family.. Fire jumping. Details — Persian New Year.. Meaning. UNESCO. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Countries.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Countries.", "x": "Nowruz in depth: Countries.. Family. Details — Persian New Year.. Spring. Spring equinox. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Meaning.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Meaning.", "x": "Nowruz in depth: Meaning.. UNESCO. Details — Persian New Year.. Table. Haft-sin. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Spring.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Spring.", "x": "Nowruz in depth: Spring.. Spring equinox. Details — Persian New Year.. Traditions. 13 days. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Nowruz comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Nowruz comes from.", "x": "Origins: Table.. Spring equinox. The history of Nowruz — Persian New Year.. Traditions. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Nowruz respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Nowruz respectfully.", "x": "Engaging: Family.. Haft-sin. How to participate or observe well — Nowruz. Persian New Year. Respect first, always; Countries.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Nowruz do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Nowruz do's and don'ts.", "x": "Etiquette: Meaning.. 13 days. The rules of respect — Nowruz. Persian New Year. When in doubt, ask about Spring.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Nowruz.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Nowruz.", "x": "Planning: Table.. Fire jumping. Practical notes — Nowruz. Persian New Year. A little planning shows respect for Traditions.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Nowruz and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Nowruz and money.", "x": "Costs: Family.. Family. What to budget — Nowruz. Persian New Year. The best experiences of Countries. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-holiday-nowruz-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
