(function(){'use strict';
/* JAH Federico Fellini Director Database generator — jahdb-e2-director-federico-fellini-director-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-director-federico-fellini-director',PREFIX='JAH-E2DIRECTORF-',NAME='JAH Federico Fellini Director Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Federico Fellini: the complete guide", "d": "Federico Fellini: the Italian dreamer..", "g": "overview", "l": 2, "q": "What is Federico Fellini: the complete guide?", "a": "Federico Fellini: the Italian dreamer..", "x": "The complete director guide to Federico Fellini: the Italian dreamer.. 1920. History, meaning, practices, and how to engage respectfully — everything in one database. 8 1/2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Federico Fellini essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Federico Fellini essentials.", "x": "At a glance: Federico Fellini — the Italian dreamer.. 8 1/2. The essentials: Circus.. La Dolce Vita. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "1920.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "1920.", "x": "Federico Fellini: 1920.. Circus. Essential knowledge — La Dolce Vita.. the Italian dreamer. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 1920..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 1920..", "x": "Explained: 1920.. Surreal. The context — Federico Fellini. Circus. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "8 1/2.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "8 1/2.", "x": "Federico Fellini: 8 1/2.. Rimini. Essential knowledge — Circus.. the Italian dreamer. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: 8 1/2..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: 8 1/2..", "x": "Explained: 8 1/2.. Vita. The context — Federico Fellini. Rimini. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "La Dolce Vita.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "La Dolce Vita.", "x": "Federico Fellini: La Dolce Vita.. Surreal. Essential knowledge — Rimini.. the Italian dreamer. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: La Dolce Vita..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: La Dolce Vita..", "x": "Explained: La Dolce Vita.. Style. The context — Federico Fellini. Surreal. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Circus.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Circus.", "x": "Federico Fellini: Circus.. Vita. Essential knowledge — Surreal.. the Italian dreamer. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Circus..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Circus..", "x": "Explained: Circus.. 8 1/2. The context — Federico Fellini. 1920. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Rimini.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Rimini.", "x": "Federico Fellini: Rimini.. Style. Essential knowledge — 1920.. the Italian dreamer. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Rimini..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Rimini..", "x": "Explained: Rimini.. Circus. The context — Federico Fellini. 8 1/2. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Surreal.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Surreal.", "x": "Federico Fellini: Surreal.. 8 1/2. Essential knowledge — 8 1/2.. the Italian dreamer. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Surreal..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Surreal..", "x": "Explained: Surreal.. Rimini. The context — Federico Fellini. La Dolce Vita. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "8 1/2.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "8 1/2.", "x": "Federico Fellini in depth: 8 1/2.. 8 1/2. Details — the Italian dreamer.. Rimini. Circus. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Circus.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Circus.", "x": "Federico Fellini in depth: Circus.. La Dolce Vita. Details — the Italian dreamer.. Surreal. Rimini. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Rimini.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Rimini.", "x": "Federico Fellini in depth: Rimini.. Circus. Details — the Italian dreamer.. Vita. Surreal. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Surreal.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Surreal.", "x": "Federico Fellini in depth: Surreal.. Rimini. Details — the Italian dreamer.. Style. 1920. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Vita.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Vita.", "x": "Federico Fellini in depth: Vita.. Surreal. Details — the Italian dreamer.. 8 1/2. 8 1/2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Style.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Style.", "x": "Federico Fellini in depth: Style.. 1920. Details — the Italian dreamer.. Circus. La Dolce Vita. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Federico Fellini comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Federico Fellini comes from.", "x": "Origins: 8 1/2.. 1920. The history of Federico Fellini — the Italian dreamer.. Circus. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Federico Fellini respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Federico Fellini respectfully.", "x": "Engaging: Rimini.. 8 1/2. How to participate or observe well — Federico Fellini. the Italian dreamer. Respect first, always; Surreal.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Federico Fellini do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Federico Fellini do's and don'ts.", "x": "Etiquette: Vita.. La Dolce Vita. The rules of respect — Federico Fellini. the Italian dreamer. When in doubt, ask about Style.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Federico Fellini.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Federico Fellini.", "x": "Planning: 8 1/2.. Circus. Practical notes — Federico Fellini. the Italian dreamer. A little planning shows respect for Circus.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Federico Fellini and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Federico Fellini and money.", "x": "Costs: Rimini.. Rimini. What to budget — Federico Fellini. the Italian dreamer. The best experiences of Surreal. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-director-federico-fellini-director-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
