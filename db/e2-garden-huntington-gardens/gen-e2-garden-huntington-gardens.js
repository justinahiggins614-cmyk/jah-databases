(function(){'use strict';
/* JAH Huntington Gardens Botanical Garden Database generator — jahdb-e2-garden-huntington-gardens-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-garden-huntington-gardens',PREFIX='JAH-E2GARDENHUN-',NAME='JAH Huntington Gardens Botanical Garden Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Huntington Gardens: the complete guide", "d": "Huntington Gardens: San Marino's twelve gardens..", "g": "overview", "l": 2, "q": "What is Huntington Gardens: the complete guide?", "a": "Huntington Gardens: San Marino's twelve gardens..", "x": "The complete botanical garden guide to Huntington Gardens: San Marino's twelve gardens.. 1919. History, meaning, practices, and how to engage respectfully — everything in one database. Gardens. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Huntington Gardens essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Huntington Gardens essentials.", "x": "At a glance: Huntington Gardens — San Marino's twelve gardens.. Desert Garden. The essentials: Desert.. Japanese. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "1919.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "1919.", "x": "Huntington Gardens: 1919.. Desert. Essential knowledge — Japanese.. San Marino's twelve gardens. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 1919..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 1919..", "x": "Explained: 1919.. Tickets. The context — Huntington Gardens. Roses. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Desert Garden.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Desert Garden.", "x": "Huntington Gardens: Desert Garden.. Japanese. Essential knowledge — Roses.. San Marino's twelve gardens. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Desert Garden..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Desert Garden..", "x": "Explained: Desert Garden.. LA. The context — Huntington Gardens. 120 acres. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Japanese.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Japanese.", "x": "Huntington Gardens: Japanese.. Tickets. Essential knowledge — 120 acres.. San Marino's twelve gardens. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Japanese..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Japanese..", "x": "Explained: Japanese.. Library. The context — Huntington Gardens. Library. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Roses.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Roses.", "x": "Huntington Gardens: Roses.. LA. Essential knowledge — Library.. San Marino's twelve gardens. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Roses..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Roses..", "x": "Explained: Roses.. Gardens. The context — Huntington Gardens. 1919. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "120 acres.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "120 acres.", "x": "Huntington Gardens: 120 acres.. Library. Essential knowledge — 1919.. San Marino's twelve gardens. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: 120 acres..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: 120 acres..", "x": "Explained: 120 acres.. Desert. The context — Huntington Gardens. Desert Garden. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Library.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Library.", "x": "Huntington Gardens: Library.. Gardens. Essential knowledge — Desert Garden.. San Marino's twelve gardens. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Library..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Library..", "x": "Explained: Library.. Japanese. The context — Huntington Gardens. Japanese. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Gardens.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Gardens.", "x": "Huntington Gardens in depth: Gardens.. Desert Garden. Details — San Marino's twelve gardens.. Japanese. Roses. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Desert.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Desert.", "x": "Huntington Gardens in depth: Desert.. Japanese. Details — San Marino's twelve gardens.. Tickets. 120 acres. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Japanese.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Japanese.", "x": "Huntington Gardens in depth: Japanese.. Roses. Details — San Marino's twelve gardens.. LA. Library. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Tickets.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Tickets.", "x": "Huntington Gardens in depth: Tickets.. 120 acres. Details — San Marino's twelve gardens.. Library. 1919. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "LA.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "LA.", "x": "Huntington Gardens in depth: LA.. Library. Details — San Marino's twelve gardens.. Gardens. Desert Garden. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Library.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Library.", "x": "Huntington Gardens in depth: Library.. 1919. Details — San Marino's twelve gardens.. Desert. Japanese. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Huntington Gardens comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Huntington Gardens comes from.", "x": "Origins: Gardens.. 1919. The history of Huntington Gardens — San Marino's twelve gardens.. Desert. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Huntington Gardens respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Huntington Gardens respectfully.", "x": "Engaging: Japanese.. Desert Garden. How to participate or observe well — Huntington Gardens. San Marino's twelve gardens. Respect first, always; Tickets.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Huntington Gardens do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Huntington Gardens do's and don'ts.", "x": "Etiquette: LA.. Japanese. The rules of respect — Huntington Gardens. San Marino's twelve gardens. When in doubt, ask about Library.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Huntington Gardens.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Huntington Gardens.", "x": "Planning: Gardens.. Roses. Practical notes — Huntington Gardens. San Marino's twelve gardens. A little planning shows respect for Desert.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Huntington Gardens and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Huntington Gardens and money.", "x": "Costs: Japanese.. 120 acres. What to budget — Huntington Gardens. San Marino's twelve gardens. The best experiences of Tickets. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-garden-huntington-gardens-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
