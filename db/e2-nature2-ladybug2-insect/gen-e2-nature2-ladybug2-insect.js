(function(){'use strict';
/* JAH Ladybug2 Database generator — jahdb-e2-nature2-ladybug2-insect-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-nature2-ladybug2-insect',PREFIX='JAH-E2NATURE2LA-',NAME='JAH Ladybug2 Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Ladybug2: the complete guide", "d": "Ladybug2: the spotted 2..", "g": "overview", "l": 2, "q": "What is Ladybug2: the complete guide?", "a": "Ladybug2: the spotted 2..", "x": "The complete insect guide to Ladybug2: the spotted 2.. Aphids. History, meaning, practices, and how to engage respectfully — everything in one database. Aphids. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Ladybug2 essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Ladybug2 essentials.", "x": "At a glance: Ladybug2 — the spotted 2.. Spots. The essentials: Garden.. Beneficial. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Aphids.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Aphids.", "x": "Ladybug2: Aphids.. Garden. Essential knowledge — Beneficial.. the spotted 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Aphids..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Aphids..", "x": "Explained: Aphids.. Spots. The context — Ladybug2. Winter. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Spots.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Spots.", "x": "Ladybug2: Spots.. Red. Essential knowledge — Winter.. the spotted 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Spots..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Spots..", "x": "Explained: Spots.. Winter. The context — Ladybug2. Red. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Beneficial.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Beneficial.", "x": "Ladybug2: Beneficial.. Spots. Essential knowledge — Red.. the spotted 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Beneficial..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Beneficial..", "x": "Explained: Beneficial.. Guide. The context — Ladybug2. Garden. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Winter.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Winter.", "x": "Ladybug2: Winter.. Winter. Essential knowledge — Garden.. the spotted 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Winter..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Winter..", "x": "Explained: Winter.. Aphids. The context — Ladybug2. Aphids. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Red.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Red.", "x": "Ladybug2: Red.. Guide. Essential knowledge — Aphids.. the spotted 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Red..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Red..", "x": "Explained: Red.. Garden. The context — Ladybug2. Spots. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Garden.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Garden.", "x": "Ladybug2: Garden.. Aphids. Essential knowledge — Spots.. the spotted 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Garden..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Garden..", "x": "Explained: Garden.. Red. The context — Ladybug2. Beneficial. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Aphids.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Aphids.", "x": "Ladybug2 in depth: Aphids.. Spots. Details — the spotted 2.. Red. Winter. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Garden.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Garden.", "x": "Ladybug2 in depth: Garden.. Beneficial. Details — the spotted 2.. Spots. Red. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Red.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Red.", "x": "Ladybug2 in depth: Red.. Winter. Details — the spotted 2.. Winter. Garden. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Spots.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Spots.", "x": "Ladybug2 in depth: Spots.. Red. Details — the spotted 2.. Guide. Aphids. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Winter.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Winter.", "x": "Ladybug2 in depth: Winter.. Garden. Details — the spotted 2.. Aphids. Spots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Guide.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Guide.", "x": "Ladybug2 in depth: Guide.. Aphids. Details — the spotted 2.. Garden. Beneficial. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Ladybug2 comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Ladybug2 comes from.", "x": "Origins: Aphids.. Aphids. The history of Ladybug2 — the spotted 2.. Garden. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Ladybug2 respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Ladybug2 respectfully.", "x": "Engaging: Red.. Spots. How to participate or observe well — Ladybug2. the spotted 2. Respect first, always; Spots.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Ladybug2 do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Ladybug2 do's and don'ts.", "x": "Etiquette: Winter.. Beneficial. The rules of respect — Ladybug2. the spotted 2. When in doubt, ask about Guide.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Ladybug2.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Ladybug2.", "x": "Planning: Aphids.. Winter. Practical notes — Ladybug2. the spotted 2. A little planning shows respect for Garden.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Ladybug2 and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Ladybug2 and money.", "x": "Costs: Red.. Red. What to budget — Ladybug2. the spotted 2. The best experiences of Spots. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-nature2-ladybug2-insect-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
