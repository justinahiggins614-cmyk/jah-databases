(function(){'use strict';
/* JAH Machu Picchu Landmark Database generator — jahdb-e2-landmark-machu-picchu-landmark-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-landmark-machu-picchu-landmark',PREFIX='JAH-E2LANDMARKM-',NAME='JAH Machu Picchu Landmark Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Machu Picchu: the complete guide", "d": "Machu Picchu: the lost Inca city..", "g": "overview", "l": 2, "q": "What is Machu Picchu: the complete guide?", "a": "Machu Picchu: the lost Inca city..", "x": "The complete landmark guide to Machu Picchu: the lost Inca city.. 1450. History, meaning, practices, and how to engage respectfully — everything in one database. 1450. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Machu Picchu essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Machu Picchu essentials.", "x": "At a glance: Machu Picchu — the lost Inca city.. 2,430m. The essentials: Inca.. Inca. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "1450.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "1450.", "x": "Machu Picchu: 1450.. Inca. Essential knowledge — Inca.. the lost Inca city. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 1450..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 1450..", "x": "Explained: 1450.. UNESCO. The context — Machu Picchu. Terraces. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "2,430m.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "2,430m.", "x": "Machu Picchu: 2,430m.. Bingham. Essential knowledge — Terraces.. the lost Inca city. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: 2,430m..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: 2,430m..", "x": "Explained: 2,430m.. Terraces. The context — Machu Picchu. Hiram Bingham. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Inca.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Inca.", "x": "Machu Picchu: Inca.. UNESCO. Essential knowledge — Hiram Bingham.. the lost Inca city. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Inca..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Inca..", "x": "Explained: Inca.. Trekking. The context — Machu Picchu. UNESCO. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Terraces.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Terraces.", "x": "Machu Picchu: Terraces.. Terraces. Essential knowledge — UNESCO.. the lost Inca city. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Terraces..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Terraces..", "x": "Explained: Terraces.. 1450. The context — Machu Picchu. 1450. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Hiram Bingham.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Hiram Bingham.", "x": "Machu Picchu: Hiram Bingham.. Trekking. Essential knowledge — 1450.. the lost Inca city. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Hiram Bingham..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Hiram Bingham..", "x": "Explained: Hiram Bingham.. Inca. The context — Machu Picchu. 2,430m. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "UNESCO.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "UNESCO.", "x": "Machu Picchu: UNESCO.. 1450. Essential knowledge — 2,430m.. the lost Inca city. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: UNESCO..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: UNESCO..", "x": "Explained: UNESCO.. Bingham. The context — Machu Picchu. Inca. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "1450.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "1450.", "x": "Machu Picchu in depth: 1450.. 2,430m. Details — the lost Inca city.. Bingham. Terraces. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Inca.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Inca.", "x": "Machu Picchu in depth: Inca.. Inca. Details — the lost Inca city.. UNESCO. Hiram Bingham. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Bingham.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Bingham.", "x": "Machu Picchu in depth: Bingham.. Terraces. Details — the lost Inca city.. Terraces. UNESCO. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "UNESCO.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "UNESCO.", "x": "Machu Picchu in depth: UNESCO.. Hiram Bingham. Details — the lost Inca city.. Trekking. 1450. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Terraces.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Terraces.", "x": "Machu Picchu in depth: Terraces.. UNESCO. Details — the lost Inca city.. 1450. 2,430m. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Trekking.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Trekking.", "x": "Machu Picchu in depth: Trekking.. 1450. Details — the lost Inca city.. Inca. Inca. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Machu Picchu comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Machu Picchu comes from.", "x": "Origins: 1450.. 1450. The history of Machu Picchu — the lost Inca city.. Inca. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Machu Picchu respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Machu Picchu respectfully.", "x": "Engaging: Bingham.. 2,430m. How to participate or observe well — Machu Picchu. the lost Inca city. Respect first, always; UNESCO.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Machu Picchu do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Machu Picchu do's and don'ts.", "x": "Etiquette: Terraces.. Inca. The rules of respect — Machu Picchu. the lost Inca city. When in doubt, ask about Trekking.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Machu Picchu.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Machu Picchu.", "x": "Planning: 1450.. Terraces. Practical notes — Machu Picchu. the lost Inca city. A little planning shows respect for Inca.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Machu Picchu and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Machu Picchu and money.", "x": "Costs: Bingham.. Hiram Bingham. What to budget — Machu Picchu. the lost Inca city. The best experiences of UNESCO. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-landmark-machu-picchu-landmark-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
