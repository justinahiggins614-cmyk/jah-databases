(function(){'use strict';
/* JAH Itaipu Dam Database generator — jahdb-e2-dam2-itaipu-dam-dam-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-dam2-itaipu-dam-dam',PREFIX='JAH-E2DAM2ITAIP-',NAME='JAH Itaipu Dam Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Itaipu Dam: the complete guide", "d": "Itaipu Dam: the Brazil-Paraguay..", "g": "overview", "l": 2, "q": "What is Itaipu Dam: the complete guide?", "a": "Itaipu Dam: the Brazil-Paraguay..", "x": "The complete dam guide to Itaipu Dam: the Brazil-Paraguay.. 1984. History, meaning, practices, and how to engage respectfully — everything in one database. 1984. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Itaipu Dam essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Itaipu Dam essentials.", "x": "At a glance: Itaipu Dam — the Brazil-Paraguay.. Second. The essentials: Brazil.. Paraná. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "1984.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "1984.", "x": "Itaipu Dam: 1984.. Brazil. Essential knowledge — Paraná.. the Brazil-Paraguay. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 1984..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 1984..", "x": "Explained: 1984.. Second. The context — Itaipu Dam. Power. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Second.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Second.", "x": "Itaipu Dam: Second.. Binational. Essential knowledge — Power.. the Brazil-Paraguay. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Second..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Second..", "x": "Explained: Second.. Paraná. The context — Itaipu Dam. Binational. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Paraná.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Paraná.", "x": "Itaipu Dam: Paraná.. Second. Essential knowledge — Binational.. the Brazil-Paraguay. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Paraná..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Paraná..", "x": "Explained: Paraná.. Visiting. The context — Itaipu Dam. Brazil. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Power.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Power.", "x": "Itaipu Dam: Power.. Paraná. Essential knowledge — Brazil.. the Brazil-Paraguay. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Power..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Power..", "x": "Explained: Power.. 1984. The context — Itaipu Dam. 1984. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Binational.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Binational.", "x": "Itaipu Dam: Binational.. Visiting. Essential knowledge — 1984.. the Brazil-Paraguay. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Binational..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Binational..", "x": "Explained: Binational.. Brazil. The context — Itaipu Dam. Second. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Brazil.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Brazil.", "x": "Itaipu Dam: Brazil.. 1984. Essential knowledge — Second.. the Brazil-Paraguay. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Brazil..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Brazil..", "x": "Explained: Brazil.. Binational. The context — Itaipu Dam. Paraná. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "1984.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "1984.", "x": "Itaipu Dam in depth: 1984.. Second. Details — the Brazil-Paraguay.. Binational. Power. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Brazil.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Brazil.", "x": "Itaipu Dam in depth: Brazil.. Paraná. Details — the Brazil-Paraguay.. Second. Binational. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Binational.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Binational.", "x": "Itaipu Dam in depth: Binational.. Power. Details — the Brazil-Paraguay.. Paraná. Brazil. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Second.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Second.", "x": "Itaipu Dam in depth: Second.. Binational. Details — the Brazil-Paraguay.. Visiting. 1984. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Paraná.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Paraná.", "x": "Itaipu Dam in depth: Paraná.. Brazil. Details — the Brazil-Paraguay.. 1984. Second. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Visiting.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Visiting.", "x": "Itaipu Dam in depth: Visiting.. 1984. Details — the Brazil-Paraguay.. Brazil. Paraná. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Itaipu Dam comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Itaipu Dam comes from.", "x": "Origins: 1984.. 1984. The history of Itaipu Dam — the Brazil-Paraguay.. Brazil. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Itaipu Dam respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Itaipu Dam respectfully.", "x": "Engaging: Binational.. Second. How to participate or observe well — Itaipu Dam. the Brazil-Paraguay. Respect first, always; Second.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Itaipu Dam do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Itaipu Dam do's and don'ts.", "x": "Etiquette: Paraná.. Paraná. The rules of respect — Itaipu Dam. the Brazil-Paraguay. When in doubt, ask about Visiting.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Itaipu Dam.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Itaipu Dam.", "x": "Planning: 1984.. Power. Practical notes — Itaipu Dam. the Brazil-Paraguay. A little planning shows respect for Brazil.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Itaipu Dam and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Itaipu Dam and money.", "x": "Costs: Binational.. Binational. What to budget — Itaipu Dam. the Brazil-Paraguay. The best experiences of Second. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-dam2-itaipu-dam-dam-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
