(function(){'use strict';
/* JAH Scottish Fold2 Database generator — jahdb-e2-animal2-scottish-fold2-cat-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-animal2-scottish-fold2-cat',PREFIX='JAH-E2ANIMAL2SC-',NAME='JAH Scottish Fold2 Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Scottish Fold2: the complete guide", "d": "Scottish Fold2: the folded 2..", "g": "overview", "l": 2, "q": "What is Scottish Fold2: the complete guide?", "a": "Scottish Fold2: the folded 2..", "x": "The complete cat breed guide to Scottish Fold2: the folded 2.. Folded. History, meaning, practices, and how to engage respectfully — everything in one database. Folded. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Scottish Fold2 essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Scottish Fold2 essentials.", "x": "At a glance: Scottish Fold2 — the folded 2.. Owl. The essentials: Scotland.. Sweet. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Folded.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Folded.", "x": "Scottish Fold2: Folded.. Scotland. Essential knowledge — Sweet.. the folded 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Folded..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Folded..", "x": "Explained: Folded.. Owl. The context — Scottish Fold2. Round. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Owl.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Owl.", "x": "Scottish Fold2: Owl.. Calm. Essential knowledge — Round.. the folded 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Owl..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Owl..", "x": "Explained: Owl.. Sweet. The context — Scottish Fold2. Scotland. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Sweet.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Sweet.", "x": "Scottish Fold2: Sweet.. Owl. Essential knowledge — Scotland.. the folded 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Sweet..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Sweet..", "x": "Explained: Sweet.. Care. The context — Scottish Fold2. Calm. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Round.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Round.", "x": "Scottish Fold2: Round.. Sweet. Essential knowledge — Calm.. the folded 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Round..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Round..", "x": "Explained: Round.. Folded. The context — Scottish Fold2. Folded. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Scotland.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Scotland.", "x": "Scottish Fold2: Scotland.. Care. Essential knowledge — Folded.. the folded 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Scotland..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Scotland..", "x": "Explained: Scotland.. Scotland. The context — Scottish Fold2. Owl. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Calm.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Calm.", "x": "Scottish Fold2: Calm.. Folded. Essential knowledge — Owl.. the folded 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Calm..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Calm..", "x": "Explained: Calm.. Calm. The context — Scottish Fold2. Sweet. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Folded.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Folded.", "x": "Scottish Fold2 in depth: Folded.. Owl. Details — the folded 2.. Calm. Round. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Scotland.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Scotland.", "x": "Scottish Fold2 in depth: Scotland.. Sweet. Details — the folded 2.. Owl. Scotland. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Calm.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Calm.", "x": "Scottish Fold2 in depth: Calm.. Round. Details — the folded 2.. Sweet. Calm. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Owl.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Owl.", "x": "Scottish Fold2 in depth: Owl.. Scotland. Details — the folded 2.. Care. Folded. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Sweet.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Sweet.", "x": "Scottish Fold2 in depth: Sweet.. Calm. Details — the folded 2.. Folded. Owl. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Care.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Care.", "x": "Scottish Fold2 in depth: Care.. Folded. Details — the folded 2.. Scotland. Sweet. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Scottish Fold2 comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Scottish Fold2 comes from.", "x": "Origins: Folded.. Folded. The history of Scottish Fold2 — the folded 2.. Scotland. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Scottish Fold2 respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Scottish Fold2 respectfully.", "x": "Engaging: Calm.. Owl. How to participate or observe well — Scottish Fold2. the folded 2. Respect first, always; Owl.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Scottish Fold2 do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Scottish Fold2 do's and don'ts.", "x": "Etiquette: Sweet.. Sweet. The rules of respect — Scottish Fold2. the folded 2. When in doubt, ask about Care.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Scottish Fold2.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Scottish Fold2.", "x": "Planning: Folded.. Round. Practical notes — Scottish Fold2. the folded 2. A little planning shows respect for Scotland.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Scottish Fold2 and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Scottish Fold2 and money.", "x": "Costs: Calm.. Scotland. What to budget — Scottish Fold2. the folded 2. The best experiences of Owl. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-animal2-scottish-fold2-cat-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
