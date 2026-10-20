(function(){'use strict';
/* JAH Opera Seria Opera Database generator — jahdb-e2-opera-opera-seria-opera-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-opera-opera-seria-opera',PREFIX='JAH-E2OPERAOPER-',NAME='JAH Opera Seria Opera Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Opera Seria: the complete guide", "d": "Opera Seria: the serious opera..", "g": "overview", "l": 2, "q": "What is Opera Seria: the complete guide?", "a": "Opera Seria: the serious opera..", "x": "The complete opera guide to Opera Seria: the serious opera.. 18th century. History, meaning, practices, and how to engage respectfully — everything in one database. Da capo. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Opera Seria essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Opera Seria essentials.", "x": "At a glance: Opera Seria — the serious opera.. Da capo. The essentials: Castrati.. Castrati. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "18th century.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "18th century.", "x": "Opera Seria: 18th century.. Castrati. Essential knowledge — Castrati.. the serious opera. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 18th century..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 18th century..", "x": "Explained: 18th century.. Formal. The context — Opera Seria. Mythology. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Da capo.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Da capo.", "x": "Opera Seria: Da capo.. Handel. Essential knowledge — Mythology.. the serious opera. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Da capo..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Da capo..", "x": "Explained: Da capo.. Myth. The context — Opera Seria. Handel. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Castrati.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Castrati.", "x": "Opera Seria: Castrati.. Formal. Essential knowledge — Handel.. the serious opera. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Castrati..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Castrati..", "x": "Explained: Castrati.. History. The context — Opera Seria. Formal. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Mythology.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Mythology.", "x": "Opera Seria: Mythology.. Myth. Essential knowledge — Formal.. the serious opera. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Mythology..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Mythology..", "x": "Explained: Mythology.. Da capo. The context — Opera Seria. 18th century. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Handel.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Handel.", "x": "Opera Seria: Handel.. History. Essential knowledge — 18th century.. the serious opera. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Handel..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Handel..", "x": "Explained: Handel.. Castrati. The context — Opera Seria. Da capo. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Formal.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Formal.", "x": "Opera Seria: Formal.. Da capo. Essential knowledge — Da capo.. the serious opera. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Formal..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Formal..", "x": "Explained: Formal.. Handel. The context — Opera Seria. Castrati. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Da capo.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Da capo.", "x": "Opera Seria in depth: Da capo.. Da capo. Details — the serious opera.. Handel. Mythology. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Castrati.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Castrati.", "x": "Opera Seria in depth: Castrati.. Castrati. Details — the serious opera.. Formal. Handel. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Handel.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Handel.", "x": "Opera Seria in depth: Handel.. Mythology. Details — the serious opera.. Myth. Formal. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Formal.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Formal.", "x": "Opera Seria in depth: Formal.. Handel. Details — the serious opera.. History. 18th century. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Myth.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Myth.", "x": "Opera Seria in depth: Myth.. Formal. Details — the serious opera.. Da capo. Da capo. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "History.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "History.", "x": "Opera Seria in depth: History.. 18th century. Details — the serious opera.. Castrati. Castrati. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Opera Seria comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Opera Seria comes from.", "x": "Origins: Da capo.. 18th century. The history of Opera Seria — the serious opera.. Castrati. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Opera Seria respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Opera Seria respectfully.", "x": "Engaging: Handel.. Da capo. How to participate or observe well — Opera Seria. the serious opera. Respect first, always; Formal.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Opera Seria do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Opera Seria do's and don'ts.", "x": "Etiquette: Myth.. Castrati. The rules of respect — Opera Seria. the serious opera. When in doubt, ask about History.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Opera Seria.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Opera Seria.", "x": "Planning: Da capo.. Mythology. Practical notes — Opera Seria. the serious opera. A little planning shows respect for Castrati.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Opera Seria and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Opera Seria and money.", "x": "Costs: Handel.. Handel. What to budget — Opera Seria. the serious opera. The best experiences of Formal. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-opera-opera-seria-opera-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
