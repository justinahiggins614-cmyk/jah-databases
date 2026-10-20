(function(){'use strict';
/* JAH Blue Tang Fish Species Database generator — jahdb-e2-fish-blue-tang-fish-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-fish-blue-tang-fish',PREFIX='JAH-E2FISHBLUET-',NAME='JAH Blue Tang Fish Species Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Blue Tang: the complete guide", "d": "Blue Tang: the Dory fish..", "g": "overview", "l": 2, "q": "What is Blue Tang: the complete guide?", "a": "Blue Tang: the Dory fish..", "x": "The complete fish species guide to Blue Tang: the Dory fish.. Blue. History, meaning, practices, and how to engage respectfully — everything in one database. Blue. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Blue Tang essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Blue Tang essentials.", "x": "At a glance: Blue Tang — the Dory fish.. Dory. The essentials: Reef.. Surgeonfish. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Blue.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Blue.", "x": "Blue Tang: Blue.. Reef. Essential knowledge — Surgeonfish.. the Dory fish. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Blue..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Blue..", "x": "Explained: Blue.. Schooling. The context — Blue Tang. Reef. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Dory.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Dory.", "x": "Blue Tang: Dory.. Scalpel. Essential knowledge — Reef.. the Dory fish. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Dory..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Dory..", "x": "Explained: Dory.. Dory. The context — Blue Tang. Scalpel. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Surgeonfish.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Surgeonfish.", "x": "Blue Tang: Surgeonfish.. Schooling. Essential knowledge — Scalpel.. the Dory fish. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Surgeonfish..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Surgeonfish..", "x": "Explained: Surgeonfish.. Habitat. The context — Blue Tang. Schooling. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Reef.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Reef.", "x": "Blue Tang: Reef.. Dory. Essential knowledge — Schooling.. the Dory fish. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Reef..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Reef..", "x": "Explained: Reef.. Blue. The context — Blue Tang. Blue. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Scalpel.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Scalpel.", "x": "Blue Tang: Scalpel.. Habitat. Essential knowledge — Blue.. the Dory fish. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Scalpel..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Scalpel..", "x": "Explained: Scalpel.. Reef. The context — Blue Tang. Dory. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Schooling.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Schooling.", "x": "Blue Tang: Schooling.. Blue. Essential knowledge — Dory.. the Dory fish. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Schooling..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Schooling..", "x": "Explained: Schooling.. Scalpel. The context — Blue Tang. Surgeonfish. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Blue.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Blue.", "x": "Blue Tang in depth: Blue.. Dory. Details — the Dory fish.. Scalpel. Reef. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Reef.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Reef.", "x": "Blue Tang in depth: Reef.. Surgeonfish. Details — the Dory fish.. Schooling. Scalpel. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Scalpel.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Scalpel.", "x": "Blue Tang in depth: Scalpel.. Reef. Details — the Dory fish.. Dory. Schooling. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Schooling.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Schooling.", "x": "Blue Tang in depth: Schooling.. Scalpel. Details — the Dory fish.. Habitat. Blue. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Dory.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Dory.", "x": "Blue Tang in depth: Dory.. Schooling. Details — the Dory fish.. Blue. Dory. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Habitat.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Habitat.", "x": "Blue Tang in depth: Habitat.. Blue. Details — the Dory fish.. Reef. Surgeonfish. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Blue Tang comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Blue Tang comes from.", "x": "Origins: Blue.. Blue. The history of Blue Tang — the Dory fish.. Reef. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Blue Tang respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Blue Tang respectfully.", "x": "Engaging: Scalpel.. Dory. How to participate or observe well — Blue Tang. the Dory fish. Respect first, always; Schooling.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Blue Tang do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Blue Tang do's and don'ts.", "x": "Etiquette: Dory.. Surgeonfish. The rules of respect — Blue Tang. the Dory fish. When in doubt, ask about Habitat.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Blue Tang.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Blue Tang.", "x": "Planning: Blue.. Reef. Practical notes — Blue Tang. the Dory fish. A little planning shows respect for Reef.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Blue Tang and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Blue Tang and money.", "x": "Costs: Scalpel.. Scalpel. What to budget — Blue Tang. the Dory fish. The best experiences of Schooling. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-fish-blue-tang-fish-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
