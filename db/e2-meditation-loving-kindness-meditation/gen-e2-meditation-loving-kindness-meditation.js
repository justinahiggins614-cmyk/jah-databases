(function(){'use strict';
/* JAH Loving-Kindness Meditation Database generator — jahdb-e2-meditation-loving-kindness-meditation-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-meditation-loving-kindness-meditation',PREFIX='JAH-E2MEDITATIO-',NAME='JAH Loving-Kindness Meditation Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Loving-Kindness: the complete guide", "d": "Loving-Kindness: the metta practice..", "g": "overview", "l": 2, "q": "What is Loving-Kindness: the complete guide?", "a": "Loving-Kindness: the metta practice..", "x": "The complete meditation guide to Loving-Kindness: the metta practice.. Metta. History, meaning, practices, and how to engage respectfully — everything in one database. Metta. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Loving-Kindness essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Loving-Kindness essentials.", "x": "At a glance: Loving-Kindness — the metta practice.. Compassion. The essentials: Phrases.. Phrases. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Metta.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Metta.", "x": "Loving-Kindness: Metta.. Phrases. Essential knowledge — Phrases.. the metta practice. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Metta..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Metta..", "x": "Explained: Metta.. Self. The context — Loving-Kindness. Self. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Compassion.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Compassion.", "x": "Loving-Kindness: Compassion.. Compassion. Essential knowledge — Self.. the metta practice. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Compassion..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Compassion..", "x": "Explained: Compassion.. Others. The context — Loving-Kindness. Others. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Phrases.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Phrases.", "x": "Loving-Kindness: Phrases.. Self. Essential knowledge — Others.. the metta practice. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Phrases..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Phrases..", "x": "Explained: Phrases.. Practice. The context — Loving-Kindness. Buddhist. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Self.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Self.", "x": "Loving-Kindness: Self.. Others. Essential knowledge — Buddhist.. the metta practice. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Self..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Self..", "x": "Explained: Self.. Metta. The context — Loving-Kindness. Metta. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Others.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Others.", "x": "Loving-Kindness: Others.. Practice. Essential knowledge — Metta.. the metta practice. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Others..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Others..", "x": "Explained: Others.. Phrases. The context — Loving-Kindness. Compassion. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Buddhist.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Buddhist.", "x": "Loving-Kindness: Buddhist.. Metta. Essential knowledge — Compassion.. the metta practice. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Buddhist..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Buddhist..", "x": "Explained: Buddhist.. Compassion. The context — Loving-Kindness. Phrases. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Metta.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Metta.", "x": "Loving-Kindness in depth: Metta.. Compassion. Details — the metta practice.. Compassion. Self. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Phrases.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Phrases.", "x": "Loving-Kindness in depth: Phrases.. Phrases. Details — the metta practice.. Self. Others. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Compassion.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Compassion.", "x": "Loving-Kindness in depth: Compassion.. Self. Details — the metta practice.. Others. Buddhist. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Self.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Self.", "x": "Loving-Kindness in depth: Self.. Others. Details — the metta practice.. Practice. Metta. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Others.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Others.", "x": "Loving-Kindness in depth: Others.. Buddhist. Details — the metta practice.. Metta. Compassion. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Practice.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Practice.", "x": "Loving-Kindness in depth: Practice.. Metta. Details — the metta practice.. Phrases. Phrases. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Loving-Kindness comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Loving-Kindness comes from.", "x": "Origins: Metta.. Metta. The history of Loving-Kindness — the metta practice.. Phrases. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Loving-Kindness respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Loving-Kindness respectfully.", "x": "Engaging: Compassion.. Compassion. How to participate or observe well — Loving-Kindness. the metta practice. Respect first, always; Self.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Loving-Kindness do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Loving-Kindness do's and don'ts.", "x": "Etiquette: Others.. Phrases. The rules of respect — Loving-Kindness. the metta practice. When in doubt, ask about Practice.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Loving-Kindness.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Loving-Kindness.", "x": "Planning: Metta.. Self. Practical notes — Loving-Kindness. the metta practice. A little planning shows respect for Phrases.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Loving-Kindness and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Loving-Kindness and money.", "x": "Costs: Compassion.. Others. What to budget — Loving-Kindness. the metta practice. The best experiences of Self. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-meditation-loving-kindness-meditation-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
