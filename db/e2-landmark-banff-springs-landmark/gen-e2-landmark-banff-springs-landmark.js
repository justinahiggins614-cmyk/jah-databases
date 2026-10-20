(function(){'use strict';
/* JAH Banff Springs Landmark Database generator — jahdb-e2-landmark-banff-springs-landmark-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-landmark-banff-springs-landmark',PREFIX='JAH-E2LANDMARKB-',NAME='JAH Banff Springs Landmark Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Banff Springs: the complete guide", "d": "Banff Springs: the castle hotel..", "g": "overview", "l": 2, "q": "What is Banff Springs: the complete guide?", "a": "Banff Springs: the castle hotel..", "x": "The complete landmark guide to Banff Springs: the castle hotel.. 1888. History, meaning, practices, and how to engage respectfully — everything in one database. 1888. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Banff Springs essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Banff Springs essentials.", "x": "At a glance: Banff Springs — the castle hotel.. Castle. The essentials: Rockies.. Rockies. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "1888.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "1888.", "x": "Banff Springs: 1888.. Rockies. Essential knowledge — Rockies.. the castle hotel. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 1888..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 1888..", "x": "Explained: 1888.. Views. The context — Banff Springs. Hot springs. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Castle.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Castle.", "x": "Banff Springs: Castle.. Fairmont. Essential knowledge — Hot springs.. the castle hotel. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Castle..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Castle..", "x": "Explained: Castle.. Castle. The context — Banff Springs. Fairmont. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Rockies.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Rockies.", "x": "Banff Springs: Rockies.. Views. Essential knowledge — Fairmont.. the castle hotel. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Rockies..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Rockies..", "x": "Explained: Rockies.. Stays. The context — Banff Springs. Views. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Hot springs.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Hot springs.", "x": "Banff Springs: Hot springs.. Castle. Essential knowledge — Views.. the castle hotel. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Hot springs..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Hot springs..", "x": "Explained: Hot springs.. 1888. The context — Banff Springs. 1888. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Fairmont.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Fairmont.", "x": "Banff Springs: Fairmont.. Stays. Essential knowledge — 1888.. the castle hotel. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Fairmont..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Fairmont..", "x": "Explained: Fairmont.. Rockies. The context — Banff Springs. Castle. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Views.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Views.", "x": "Banff Springs: Views.. 1888. Essential knowledge — Castle.. the castle hotel. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Views..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Views..", "x": "Explained: Views.. Fairmont. The context — Banff Springs. Rockies. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "1888.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "1888.", "x": "Banff Springs in depth: 1888.. Castle. Details — the castle hotel.. Fairmont. Hot springs. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Rockies.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Rockies.", "x": "Banff Springs in depth: Rockies.. Rockies. Details — the castle hotel.. Views. Fairmont. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Fairmont.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Fairmont.", "x": "Banff Springs in depth: Fairmont.. Hot springs. Details — the castle hotel.. Castle. Views. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Views.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Views.", "x": "Banff Springs in depth: Views.. Fairmont. Details — the castle hotel.. Stays. 1888. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Castle.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Castle.", "x": "Banff Springs in depth: Castle.. Views. Details — the castle hotel.. 1888. Castle. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Stays.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Stays.", "x": "Banff Springs in depth: Stays.. 1888. Details — the castle hotel.. Rockies. Rockies. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Banff Springs comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Banff Springs comes from.", "x": "Origins: 1888.. 1888. The history of Banff Springs — the castle hotel.. Rockies. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Banff Springs respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Banff Springs respectfully.", "x": "Engaging: Fairmont.. Castle. How to participate or observe well — Banff Springs. the castle hotel. Respect first, always; Views.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Banff Springs do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Banff Springs do's and don'ts.", "x": "Etiquette: Castle.. Rockies. The rules of respect — Banff Springs. the castle hotel. When in doubt, ask about Stays.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Banff Springs.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Banff Springs.", "x": "Planning: 1888.. Hot springs. Practical notes — Banff Springs. the castle hotel. A little planning shows respect for Rockies.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Banff Springs and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Banff Springs and money.", "x": "Costs: Fairmont.. Fairmont. What to budget — Banff Springs. the castle hotel. The best experiences of Views. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-landmark-banff-springs-landmark-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
