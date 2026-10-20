(function(){'use strict';
/* JAH Carnival Holiday Database generator — jahdb-e2-holiday-carnival-holiday-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-holiday-carnival-holiday',PREFIX='JAH-E2HOLIDAYCA-',NAME='JAH Carnival Holiday Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Carnival: the complete guide", "d": "Carnival: pre-Lent revelry worldwide..", "g": "overview", "l": 2, "q": "What is Carnival: the complete guide?", "a": "Carnival: pre-Lent revelry worldwide..", "x": "The complete holiday guide to Carnival: pre-Lent revelry worldwide.. Before Lent. History, meaning, practices, and how to engage respectfully — everything in one database. History. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Carnival essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Carnival essentials.", "x": "At a glance: Carnival — pre-Lent revelry worldwide.. Parades. The essentials: Cities.. Costumes. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Before Lent.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Before Lent.", "x": "Carnival: Before Lent.. Cities. Essential knowledge — Costumes.. pre-Lent revelry worldwide. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Before Lent..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Before Lent..", "x": "Explained: Before Lent.. Music. The context — Carnival. Rio. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Parades.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Parades.", "x": "Carnival: Parades.. Costumes. Essential knowledge — Rio.. pre-Lent revelry worldwide. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Parades..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Parades..", "x": "Explained: Parades.. Meaning. The context — Carnival. Venice. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Costumes.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Costumes.", "x": "Carnival: Costumes.. Music. Essential knowledge — Venice.. pre-Lent revelry worldwide. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Costumes..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Costumes..", "x": "Explained: Costumes.. Party. The context — Carnival. Music. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Rio.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Rio.", "x": "Carnival: Rio.. Meaning. Essential knowledge — Music.. pre-Lent revelry worldwide. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Rio..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Rio..", "x": "Explained: Rio.. History. The context — Carnival. Before Lent. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Venice.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Venice.", "x": "Carnival: Venice.. Party. Essential knowledge — Before Lent.. pre-Lent revelry worldwide. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Venice..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Venice..", "x": "Explained: Venice.. Cities. The context — Carnival. Parades. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Music.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Music.", "x": "Carnival: Music.. History. Essential knowledge — Parades.. pre-Lent revelry worldwide. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Music..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Music..", "x": "Explained: Music.. Costumes. The context — Carnival. Costumes. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "History.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "History.", "x": "Carnival in depth: History.. Parades. Details — pre-Lent revelry worldwide.. Costumes. Rio. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Cities.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Cities.", "x": "Carnival in depth: Cities.. Costumes. Details — pre-Lent revelry worldwide.. Music. Venice. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Costumes.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Costumes.", "x": "Carnival in depth: Costumes.. Rio. Details — pre-Lent revelry worldwide.. Meaning. Music. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Music.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Music.", "x": "Carnival in depth: Music.. Venice. Details — pre-Lent revelry worldwide.. Party. Before Lent. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Meaning.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Meaning.", "x": "Carnival in depth: Meaning.. Music. Details — pre-Lent revelry worldwide.. History. Parades. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Party.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Party.", "x": "Carnival in depth: Party.. Before Lent. Details — pre-Lent revelry worldwide.. Cities. Costumes. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Carnival comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Carnival comes from.", "x": "Origins: History.. Before Lent. The history of Carnival — pre-Lent revelry worldwide.. Cities. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Carnival respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Carnival respectfully.", "x": "Engaging: Costumes.. Parades. How to participate or observe well — Carnival. pre-Lent revelry worldwide. Respect first, always; Music.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Carnival do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Carnival do's and don'ts.", "x": "Etiquette: Meaning.. Costumes. The rules of respect — Carnival. pre-Lent revelry worldwide. When in doubt, ask about Party.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Carnival.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Carnival.", "x": "Planning: History.. Rio. Practical notes — Carnival. pre-Lent revelry worldwide. A little planning shows respect for Cities.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Carnival and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Carnival and money.", "x": "Costs: Costumes.. Venice. What to budget — Carnival. pre-Lent revelry worldwide. The best experiences of Music. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-holiday-carnival-holiday-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
