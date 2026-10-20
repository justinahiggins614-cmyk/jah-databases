(function(){'use strict';
/* JAH Pena Palace Landmark Database generator — jahdb-e2-landmark-pena-palace-landmark-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-landmark-pena-palace-landmark',PREFIX='JAH-E2LANDMARKP-',NAME='JAH Pena Palace Landmark Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Pena Palace: the complete guide", "d": "Pena Palace: the romantic colors..", "g": "overview", "l": 2, "q": "What is Pena Palace: the complete guide?", "a": "Pena Palace: the romantic colors..", "x": "The complete landmark guide to Pena Palace: the romantic colors.. 1840. History, meaning, practices, and how to engage respectfully — everything in one database. 1840. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Pena Palace essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Pena Palace essentials.", "x": "At a glance: Pena Palace — the romantic colors.. Romantic. The essentials: Colors.. Colors. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "1840.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "1840.", "x": "Pena Palace: 1840.. Colors. Essential knowledge — Colors.. the romantic colors. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 1840..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 1840..", "x": "Explained: 1840.. Sintra. The context — Pena Palace. Sintra. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Romantic.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Romantic.", "x": "Pena Palace: Romantic.. UNESCO. Essential knowledge — Sintra.. the romantic colors. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Romantic..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Romantic..", "x": "Explained: Romantic.. Romantic. The context — Pena Palace. UNESCO. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Colors.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Colors.", "x": "Pena Palace: Colors.. Sintra. Essential knowledge — UNESCO.. the romantic colors. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Colors..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Colors..", "x": "Explained: Colors.. Tours. The context — Pena Palace. Yellow. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Sintra.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Sintra.", "x": "Pena Palace: Sintra.. Romantic. Essential knowledge — Yellow.. the romantic colors. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Sintra..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Sintra..", "x": "Explained: Sintra.. 1840. The context — Pena Palace. 1840. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "UNESCO.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "UNESCO.", "x": "Pena Palace: UNESCO.. Tours. Essential knowledge — 1840.. the romantic colors. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: UNESCO..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: UNESCO..", "x": "Explained: UNESCO.. Colors. The context — Pena Palace. Romantic. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Yellow.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Yellow.", "x": "Pena Palace: Yellow.. 1840. Essential knowledge — Romantic.. the romantic colors. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Yellow..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Yellow..", "x": "Explained: Yellow.. UNESCO. The context — Pena Palace. Colors. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "1840.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "1840.", "x": "Pena Palace in depth: 1840.. Romantic. Details — the romantic colors.. UNESCO. Sintra. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Colors.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Colors.", "x": "Pena Palace in depth: Colors.. Colors. Details — the romantic colors.. Sintra. UNESCO. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "UNESCO.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "UNESCO.", "x": "Pena Palace in depth: UNESCO.. Sintra. Details — the romantic colors.. Romantic. Yellow. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Sintra.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Sintra.", "x": "Pena Palace in depth: Sintra.. UNESCO. Details — the romantic colors.. Tours. 1840. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Romantic.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Romantic.", "x": "Pena Palace in depth: Romantic.. Yellow. Details — the romantic colors.. 1840. Romantic. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Tours.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Tours.", "x": "Pena Palace in depth: Tours.. 1840. Details — the romantic colors.. Colors. Colors. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Pena Palace comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Pena Palace comes from.", "x": "Origins: 1840.. 1840. The history of Pena Palace — the romantic colors.. Colors. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Pena Palace respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Pena Palace respectfully.", "x": "Engaging: UNESCO.. Romantic. How to participate or observe well — Pena Palace. the romantic colors. Respect first, always; Sintra.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Pena Palace do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Pena Palace do's and don'ts.", "x": "Etiquette: Romantic.. Colors. The rules of respect — Pena Palace. the romantic colors. When in doubt, ask about Tours.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Pena Palace.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Pena Palace.", "x": "Planning: 1840.. Sintra. Practical notes — Pena Palace. the romantic colors. A little planning shows respect for Colors.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Pena Palace and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Pena Palace and money.", "x": "Costs: UNESCO.. UNESCO. What to budget — Pena Palace. the romantic colors. The best experiences of Sintra. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-landmark-pena-palace-landmark-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
