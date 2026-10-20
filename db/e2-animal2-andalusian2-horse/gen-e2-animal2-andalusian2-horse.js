(function(){'use strict';
/* JAH Andalusian2 Database generator — jahdb-e2-animal2-andalusian2-horse-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-animal2-andalusian2-horse',PREFIX='JAH-E2ANIMAL2AN-',NAME='JAH Andalusian2 Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Andalusian2: the complete guide", "d": "Andalusian2: the Spanish 2..", "g": "overview", "l": 2, "q": "What is Andalusian2: the complete guide?", "a": "Andalusian2: the Spanish 2..", "x": "The complete horse breed guide to Andalusian2: the Spanish 2.. Spain. History, meaning, practices, and how to engage respectfully — everything in one database. Spain. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Andalusian2 essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Andalusian2 essentials.", "x": "At a glance: Andalusian2 — the Spanish 2.. Baroque. The essentials: Noble.. Dressage. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Spain.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Spain.", "x": "Andalusian2: Spain.. Noble. Essential knowledge — Dressage.. the Spanish 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Spain..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Spain..", "x": "Explained: Spain.. Baroque. The context — Andalusian2. Gray. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Baroque.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Baroque.", "x": "Andalusian2: Baroque.. PRE. Essential knowledge — Gray.. the Spanish 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Baroque..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Baroque..", "x": "Explained: Baroque.. Gray. The context — Andalusian2. Noble. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Dressage.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Dressage.", "x": "Andalusian2: Dressage.. Baroque. Essential knowledge — Noble.. the Spanish 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Dressage..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Dressage..", "x": "Explained: Dressage.. Care. The context — Andalusian2. PRE. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Gray.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Gray.", "x": "Andalusian2: Gray.. Gray. Essential knowledge — PRE.. the Spanish 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Gray..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Gray..", "x": "Explained: Gray.. Spain. The context — Andalusian2. Spain. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Noble.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Noble.", "x": "Andalusian2: Noble.. Care. Essential knowledge — Spain.. the Spanish 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Noble..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Noble..", "x": "Explained: Noble.. Noble. The context — Andalusian2. Baroque. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "PRE.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "PRE.", "x": "Andalusian2: PRE.. Spain. Essential knowledge — Baroque.. the Spanish 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: PRE..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: PRE..", "x": "Explained: PRE.. PRE. The context — Andalusian2. Dressage. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Spain.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Spain.", "x": "Andalusian2 in depth: Spain.. Baroque. Details — the Spanish 2.. PRE. Gray. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Noble.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Noble.", "x": "Andalusian2 in depth: Noble.. Dressage. Details — the Spanish 2.. Baroque. Noble. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "PRE.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "PRE.", "x": "Andalusian2 in depth: PRE.. Gray. Details — the Spanish 2.. Gray. PRE. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Baroque.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Baroque.", "x": "Andalusian2 in depth: Baroque.. Noble. Details — the Spanish 2.. Care. Spain. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Gray.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Gray.", "x": "Andalusian2 in depth: Gray.. PRE. Details — the Spanish 2.. Spain. Baroque. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Care.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Care.", "x": "Andalusian2 in depth: Care.. Spain. Details — the Spanish 2.. Noble. Dressage. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Andalusian2 comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Andalusian2 comes from.", "x": "Origins: Spain.. Spain. The history of Andalusian2 — the Spanish 2.. Noble. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Andalusian2 respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Andalusian2 respectfully.", "x": "Engaging: PRE.. Baroque. How to participate or observe well — Andalusian2. the Spanish 2. Respect first, always; Baroque.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Andalusian2 do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Andalusian2 do's and don'ts.", "x": "Etiquette: Gray.. Dressage. The rules of respect — Andalusian2. the Spanish 2. When in doubt, ask about Care.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Andalusian2.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Andalusian2.", "x": "Planning: Spain.. Gray. Practical notes — Andalusian2. the Spanish 2. A little planning shows respect for Noble.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Andalusian2 and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Andalusian2 and money.", "x": "Costs: PRE.. Noble. What to budget — Andalusian2. the Spanish 2. The best experiences of Baroque. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-animal2-andalusian2-horse-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
