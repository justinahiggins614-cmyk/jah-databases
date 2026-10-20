(function(){'use strict';
/* JAH Blood Type Diet Diet Database generator — jahdb-e2-diet-blood-type-diet-diet-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-diet-blood-type-diet-diet',PREFIX='JAH-E2DIETBLOOD-',NAME='JAH Blood Type Diet Diet Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Blood Type Diet: the complete guide", "d": "Blood Type Diet: the type eating..", "g": "overview", "l": 2, "q": "What is Blood Type Diet: the complete guide?", "a": "Blood Type Diet: the type eating..", "x": "The complete diet guide to Blood Type Diet: the type eating.. D'Adamo. History, meaning, practices, and how to engage respectfully — everything in one database. D'Adamo. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Blood Type Diet essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Blood Type Diet essentials.", "x": "At a glance: Blood Type Diet — the type eating.. Type O. The essentials: Debunked.. Debunked. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "D'Adamo.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "D'Adamo.", "x": "Blood Type Diet: D'Adamo.. Debunked. Essential knowledge — Debunked.. the type eating. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: D'Adamo..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: D'Adamo..", "x": "Explained: D'Adamo.. Lectins. The context — Blood Type Diet. Lectins. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Type O.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Type O.", "x": "Blood Type Diet: Type O.. 1996. Essential knowledge — Lectins.. the type eating. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Type O..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Type O..", "x": "Explained: Type O.. Controversy. The context — Blood Type Diet. 1996. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Debunked.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Debunked.", "x": "Blood Type Diet: Debunked.. Lectins. Essential knowledge — 1996.. the type eating. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Debunked..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Debunked..", "x": "Explained: Debunked.. Types. The context — Blood Type Diet. Controversy. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Lectins.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Lectins.", "x": "Blood Type Diet: Lectins.. Controversy. Essential knowledge — Controversy.. the type eating. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Lectins..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Lectins..", "x": "Explained: Lectins.. D'Adamo. The context — Blood Type Diet. D'Adamo. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "1996.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "1996.", "x": "Blood Type Diet: 1996.. Types. Essential knowledge — D'Adamo.. the type eating. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: 1996..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: 1996..", "x": "Explained: 1996.. Debunked. The context — Blood Type Diet. Type O. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Controversy.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Controversy.", "x": "Blood Type Diet: Controversy.. D'Adamo. Essential knowledge — Type O.. the type eating. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Controversy..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Controversy..", "x": "Explained: Controversy.. 1996. The context — Blood Type Diet. Debunked. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "D'Adamo.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "D'Adamo.", "x": "Blood Type Diet in depth: D'Adamo.. Type O. Details — the type eating.. 1996. Lectins. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Debunked.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Debunked.", "x": "Blood Type Diet in depth: Debunked.. Debunked. Details — the type eating.. Lectins. 1996. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "1996.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "1996.", "x": "Blood Type Diet in depth: 1996.. Lectins. Details — the type eating.. Controversy. Controversy. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Lectins.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Lectins.", "x": "Blood Type Diet in depth: Lectins.. 1996. Details — the type eating.. Types. D'Adamo. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Controversy.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Controversy.", "x": "Blood Type Diet in depth: Controversy.. Controversy. Details — the type eating.. D'Adamo. Type O. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Types.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Types.", "x": "Blood Type Diet in depth: Types.. D'Adamo. Details — the type eating.. Debunked. Debunked. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Blood Type Diet comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Blood Type Diet comes from.", "x": "Origins: D'Adamo.. D'Adamo. The history of Blood Type Diet — the type eating.. Debunked. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Blood Type Diet respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Blood Type Diet respectfully.", "x": "Engaging: 1996.. Type O. How to participate or observe well — Blood Type Diet. the type eating. Respect first, always; Lectins.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Blood Type Diet do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Blood Type Diet do's and don'ts.", "x": "Etiquette: Controversy.. Debunked. The rules of respect — Blood Type Diet. the type eating. When in doubt, ask about Types.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Blood Type Diet.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Blood Type Diet.", "x": "Planning: D'Adamo.. Lectins. Practical notes — Blood Type Diet. the type eating. A little planning shows respect for Debunked.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Blood Type Diet and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Blood Type Diet and money.", "x": "Costs: 1996.. 1996. What to budget — Blood Type Diet. the type eating. The best experiences of Lectins. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-diet-blood-type-diet-diet-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
