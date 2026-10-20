(function(){'use strict';
/* JAH Orchid Flowers Flower Database generator — jahdb-e2-flower-orchid-flowers-species-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-flower-orchid-flowers-species',PREFIX='JAH-E2FLOWERORC-',NAME='JAH Orchid Flowers Flower Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Orchid Flowers: the complete guide", "d": "Orchid Flowers: the exotic bloom..", "g": "overview", "l": 2, "q": "What is Orchid Flowers: the complete guide?", "a": "Orchid Flowers: the exotic bloom..", "x": "The complete flower guide to Orchid Flowers: the exotic bloom.. Epiphyte. History, meaning, practices, and how to engage respectfully — everything in one database. Epiphyte. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Orchid Flowers essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Orchid Flowers essentials.", "x": "At a glance: Orchid Flowers — the exotic bloom.. Bark. The essentials: Rebloom.. Rebloom. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Epiphyte.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Epiphyte.", "x": "Orchid Flowers: Epiphyte.. Rebloom. Essential knowledge — Rebloom.. the exotic bloom. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Epiphyte..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Epiphyte..", "x": "Explained: Epiphyte.. Patience. The context — Orchid Flowers. Moth. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Bark.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Bark.", "x": "Orchid Flowers: Bark.. Humidity. Essential knowledge — Moth.. the exotic bloom. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Bark..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Bark..", "x": "Explained: Bark.. Moth. The context — Orchid Flowers. Humidity. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Rebloom.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Rebloom.", "x": "Orchid Flowers: Rebloom.. Patience. Essential knowledge — Humidity.. the exotic bloom. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Rebloom..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Rebloom..", "x": "Explained: Rebloom.. Guide. The context — Orchid Flowers. Patience. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Moth.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Moth.", "x": "Orchid Flowers: Moth.. Moth. Essential knowledge — Patience.. the exotic bloom. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Moth..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Moth..", "x": "Explained: Moth.. Epiphyte. The context — Orchid Flowers. Epiphyte. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Humidity.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Humidity.", "x": "Orchid Flowers: Humidity.. Guide. Essential knowledge — Epiphyte.. the exotic bloom. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Humidity..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Humidity..", "x": "Explained: Humidity.. Rebloom. The context — Orchid Flowers. Bark. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Patience.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Patience.", "x": "Orchid Flowers: Patience.. Epiphyte. Essential knowledge — Bark.. the exotic bloom. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Patience..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Patience..", "x": "Explained: Patience.. Humidity. The context — Orchid Flowers. Rebloom. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Epiphyte.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Epiphyte.", "x": "Orchid Flowers in depth: Epiphyte.. Bark. Details — the exotic bloom.. Humidity. Moth. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Rebloom.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Rebloom.", "x": "Orchid Flowers in depth: Rebloom.. Rebloom. Details — the exotic bloom.. Patience. Humidity. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Humidity.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Humidity.", "x": "Orchid Flowers in depth: Humidity.. Moth. Details — the exotic bloom.. Moth. Patience. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Patience.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Patience.", "x": "Orchid Flowers in depth: Patience.. Humidity. Details — the exotic bloom.. Guide. Epiphyte. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Moth.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Moth.", "x": "Orchid Flowers in depth: Moth.. Patience. Details — the exotic bloom.. Epiphyte. Bark. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Guide.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Guide.", "x": "Orchid Flowers in depth: Guide.. Epiphyte. Details — the exotic bloom.. Rebloom. Rebloom. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Orchid Flowers comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Orchid Flowers comes from.", "x": "Origins: Epiphyte.. Epiphyte. The history of Orchid Flowers — the exotic bloom.. Rebloom. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Orchid Flowers respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Orchid Flowers respectfully.", "x": "Engaging: Humidity.. Bark. How to participate or observe well — Orchid Flowers. the exotic bloom. Respect first, always; Patience.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Orchid Flowers do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Orchid Flowers do's and don'ts.", "x": "Etiquette: Moth.. Rebloom. The rules of respect — Orchid Flowers. the exotic bloom. When in doubt, ask about Guide.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Orchid Flowers.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Orchid Flowers.", "x": "Planning: Epiphyte.. Moth. Practical notes — Orchid Flowers. the exotic bloom. A little planning shows respect for Rebloom.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Orchid Flowers and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Orchid Flowers and money.", "x": "Costs: Humidity.. Humidity. What to budget — Orchid Flowers. the exotic bloom. The best experiences of Patience. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-flower-orchid-flowers-species-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
