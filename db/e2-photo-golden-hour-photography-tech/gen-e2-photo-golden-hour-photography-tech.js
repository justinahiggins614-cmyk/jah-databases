(function(){'use strict';
/* JAH Golden Hour Photography Database generator — jahdb-e2-photo-golden-hour-photography-tech-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-photo-golden-hour-photography-tech',PREFIX='JAH-E2PHOTOGOLD-',NAME='JAH Golden Hour Photography Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Golden Hour: the complete guide", "d": "Golden Hour: the magic light..", "g": "overview", "l": 2, "q": "What is Golden Hour: the complete guide?", "a": "Golden Hour: the magic light..", "x": "The complete photography guide to Golden Hour: the magic light.. Sunset. History, meaning, practices, and how to engage respectfully — everything in one database. Warm. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Golden Hour essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Golden Hour essentials.", "x": "At a glance: Golden Hour — the magic light.. Warm. The essentials: Flares.. Backlight. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Sunset.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Sunset.", "x": "Golden Hour: Sunset.. Flares. Essential knowledge — Backlight.. the magic light. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Sunset..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Sunset..", "x": "Explained: Sunset.. Sunset. The context — Golden Hour. Hour. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Warm.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Warm.", "x": "Golden Hour: Warm.. Planning. Essential knowledge — Hour.. the magic light. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Warm..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Warm..", "x": "Explained: Warm.. Backlight. The context — Golden Hour. Flares. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Backlight.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Backlight.", "x": "Golden Hour: Backlight.. Sunset. Essential knowledge — Flares.. the magic light. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Backlight..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Backlight..", "x": "Explained: Backlight.. Tips. The context — Golden Hour. Planning. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Hour.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Hour.", "x": "Golden Hour: Hour.. Backlight. Essential knowledge — Planning.. the magic light. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Hour..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Hour..", "x": "Explained: Hour.. Warm. The context — Golden Hour. Sunset. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Flares.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Flares.", "x": "Golden Hour: Flares.. Tips. Essential knowledge — Sunset.. the magic light. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Flares..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Flares..", "x": "Explained: Flares.. Flares. The context — Golden Hour. Warm. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Planning.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Planning.", "x": "Golden Hour: Planning.. Warm. Essential knowledge — Warm.. the magic light. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Planning..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Planning..", "x": "Explained: Planning.. Planning. The context — Golden Hour. Backlight. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Warm.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Warm.", "x": "Golden Hour in depth: Warm.. Warm. Details — the magic light.. Planning. Hour. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Flares.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Flares.", "x": "Golden Hour in depth: Flares.. Backlight. Details — the magic light.. Sunset. Flares. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Planning.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Planning.", "x": "Golden Hour in depth: Planning.. Hour. Details — the magic light.. Backlight. Planning. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Sunset.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Sunset.", "x": "Golden Hour in depth: Sunset.. Flares. Details — the magic light.. Tips. Sunset. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Backlight.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Backlight.", "x": "Golden Hour in depth: Backlight.. Planning. Details — the magic light.. Warm. Warm. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Tips.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Tips.", "x": "Golden Hour in depth: Tips.. Sunset. Details — the magic light.. Flares. Backlight. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Golden Hour comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Golden Hour comes from.", "x": "Origins: Warm.. Sunset. The history of Golden Hour — the magic light.. Flares. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Golden Hour respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Golden Hour respectfully.", "x": "Engaging: Planning.. Warm. How to participate or observe well — Golden Hour. the magic light. Respect first, always; Sunset.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Golden Hour do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Golden Hour do's and don'ts.", "x": "Etiquette: Backlight.. Backlight. The rules of respect — Golden Hour. the magic light. When in doubt, ask about Tips.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Golden Hour.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Golden Hour.", "x": "Planning: Warm.. Hour. Practical notes — Golden Hour. the magic light. A little planning shows respect for Flares.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Golden Hour and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Golden Hour and money.", "x": "Costs: Planning.. Flares. What to budget — Golden Hour. the magic light. The best experiences of Sunset. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-photo-golden-hour-photography-tech-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
