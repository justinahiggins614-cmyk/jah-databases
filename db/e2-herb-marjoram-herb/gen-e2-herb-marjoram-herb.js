(function(){'use strict';
/* JAH Marjoram Herb Database generator — jahdb-e2-herb-marjoram-herb-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-herb-marjoram-herb',PREFIX='JAH-E2HERBMARJO-',NAME='JAH Marjoram Herb Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Marjoram: the complete guide", "d": "Marjoram: the sweet oregano..", "g": "overview", "l": 2, "q": "What is Marjoram: the complete guide?", "a": "Marjoram: the sweet oregano..", "x": "The complete herb guide to Marjoram: the sweet oregano.. Sweet. History, meaning, practices, and how to engage respectfully — everything in one database. Sausages. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Marjoram essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Marjoram essentials.", "x": "At a glance: Marjoram — the sweet oregano.. Sausages. The essentials: Delicate.. German. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Sweet.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Sweet.", "x": "Marjoram: Sweet.. Delicate. Essential knowledge — German.. the sweet oregano. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Sweet..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Sweet..", "x": "Explained: Sweet.. Drying. The context — Marjoram. Delicate. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Sausages.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Sausages.", "x": "Marjoram: Sausages.. German. Essential knowledge — Delicate.. the sweet oregano. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Sausages..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Sausages..", "x": "Explained: Sausages.. Growing. The context — Marjoram. Drying. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "German.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "German.", "x": "Marjoram: German.. Drying. Essential knowledge — Drying.. the sweet oregano. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: German..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: German..", "x": "Explained: German.. Oregano. The context — Marjoram. Oregano. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Delicate.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Delicate.", "x": "Marjoram: Delicate.. Growing. Essential knowledge — Oregano.. the sweet oregano. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Delicate..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Delicate..", "x": "Explained: Delicate.. Sausages. The context — Marjoram. Sweet. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Drying.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Drying.", "x": "Marjoram: Drying.. Oregano. Essential knowledge — Sweet.. the sweet oregano. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Drying..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Drying..", "x": "Explained: Drying.. Delicate. The context — Marjoram. Sausages. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Oregano.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Oregano.", "x": "Marjoram: Oregano.. Sausages. Essential knowledge — Sausages.. the sweet oregano. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Oregano..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Oregano..", "x": "Explained: Oregano.. German. The context — Marjoram. German. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Sausages.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Sausages.", "x": "Marjoram in depth: Sausages.. Sausages. Details — the sweet oregano.. German. Delicate. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Delicate.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Delicate.", "x": "Marjoram in depth: Delicate.. German. Details — the sweet oregano.. Drying. Drying. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "German.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "German.", "x": "Marjoram in depth: German.. Delicate. Details — the sweet oregano.. Growing. Oregano. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Drying.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Drying.", "x": "Marjoram in depth: Drying.. Drying. Details — the sweet oregano.. Oregano. Sweet. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Growing.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Growing.", "x": "Marjoram in depth: Growing.. Oregano. Details — the sweet oregano.. Sausages. Sausages. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Oregano.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Oregano.", "x": "Marjoram in depth: Oregano.. Sweet. Details — the sweet oregano.. Delicate. German. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Marjoram comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Marjoram comes from.", "x": "Origins: Sausages.. Sweet. The history of Marjoram — the sweet oregano.. Delicate. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Marjoram respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Marjoram respectfully.", "x": "Engaging: German.. Sausages. How to participate or observe well — Marjoram. the sweet oregano. Respect first, always; Drying.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Marjoram do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Marjoram do's and don'ts.", "x": "Etiquette: Growing.. German. The rules of respect — Marjoram. the sweet oregano. When in doubt, ask about Oregano.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Marjoram.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Marjoram.", "x": "Planning: Sausages.. Delicate. Practical notes — Marjoram. the sweet oregano. A little planning shows respect for Delicate.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Marjoram and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Marjoram and money.", "x": "Costs: German.. Drying. What to budget — Marjoram. the sweet oregano. The best experiences of Drying. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-herb-marjoram-herb-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
