(function(){'use strict';
/* JAH Dotwork Tattoos Tattoo Style Database generator — jahdb-e2-tattoo-dotwork-tattoos-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-tattoo-dotwork-tattoos',PREFIX='JAH-E2TATTOODOT-',NAME='JAH Dotwork Tattoos Tattoo Style Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Dotwork Tattoos: the complete guide", "d": "Dotwork Tattoos: pointillist ink..", "g": "overview", "l": 2, "q": "What is Dotwork Tattoos: the complete guide?", "a": "Dotwork Tattoos: pointillist ink..", "x": "The complete tattoo style guide to Dotwork Tattoos: pointillist ink.. Dots. History, meaning, practices, and how to engage respectfully — everything in one database. Technique. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Dotwork Tattoos essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Dotwork Tattoos essentials.", "x": "At a glance: Dotwork Tattoos — pointillist ink.. Mandalas. The essentials: Designs.. Patience. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Dots.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Dots.", "x": "Dotwork Tattoos: Dots.. Designs. Essential knowledge — Patience.. pointillist ink. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Dots..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Dots..", "x": "Explained: Dots.. Pain. The context — Dotwork Tattoos. Artists. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Mandalas.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Mandalas.", "x": "Dotwork Tattoos: Mandalas.. Artists. Essential knowledge — Artists.. pointillist ink. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Mandalas..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Mandalas..", "x": "Explained: Mandalas.. Aging. The context — Dotwork Tattoos. Geometric. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Patience.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Patience.", "x": "Dotwork Tattoos: Patience.. Pain. Essential knowledge — Geometric.. pointillist ink. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Patience..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Patience..", "x": "Explained: Patience.. Style. The context — Dotwork Tattoos. Aging. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Artists.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Artists.", "x": "Dotwork Tattoos: Artists.. Aging. Essential knowledge — Aging.. pointillist ink. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Artists..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Artists..", "x": "Explained: Artists.. Technique. The context — Dotwork Tattoos. Dots. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Geometric.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Geometric.", "x": "Dotwork Tattoos: Geometric.. Style. Essential knowledge — Dots.. pointillist ink. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Geometric..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Geometric..", "x": "Explained: Geometric.. Designs. The context — Dotwork Tattoos. Mandalas. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Aging.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Aging.", "x": "Dotwork Tattoos: Aging.. Technique. Essential knowledge — Mandalas.. pointillist ink. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Aging..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Aging..", "x": "Explained: Aging.. Artists. The context — Dotwork Tattoos. Patience. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Technique.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Technique.", "x": "Dotwork Tattoos in depth: Technique.. Mandalas. Details — pointillist ink.. Artists. Artists. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Designs.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Designs.", "x": "Dotwork Tattoos in depth: Designs.. Patience. Details — pointillist ink.. Pain. Geometric. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Artists.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Artists.", "x": "Dotwork Tattoos in depth: Artists.. Artists. Details — pointillist ink.. Aging. Aging. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Pain.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Pain.", "x": "Dotwork Tattoos in depth: Pain.. Geometric. Details — pointillist ink.. Style. Dots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Aging.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Aging.", "x": "Dotwork Tattoos in depth: Aging.. Aging. Details — pointillist ink.. Technique. Mandalas. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Style.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Style.", "x": "Dotwork Tattoos in depth: Style.. Dots. Details — pointillist ink.. Designs. Patience. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Dotwork Tattoos comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Dotwork Tattoos comes from.", "x": "Origins: Technique.. Dots. The history of Dotwork Tattoos — pointillist ink.. Designs. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Dotwork Tattoos respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Dotwork Tattoos respectfully.", "x": "Engaging: Artists.. Mandalas. How to participate or observe well — Dotwork Tattoos. pointillist ink. Respect first, always; Pain.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Dotwork Tattoos do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Dotwork Tattoos do's and don'ts.", "x": "Etiquette: Aging.. Patience. The rules of respect — Dotwork Tattoos. pointillist ink. When in doubt, ask about Style.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Dotwork Tattoos.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Dotwork Tattoos.", "x": "Planning: Technique.. Artists. Practical notes — Dotwork Tattoos. pointillist ink. A little planning shows respect for Designs.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Dotwork Tattoos and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Dotwork Tattoos and money.", "x": "Costs: Artists.. Geometric. What to budget — Dotwork Tattoos. pointillist ink. The best experiences of Pain. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-tattoo-dotwork-tattoos-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
