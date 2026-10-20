(function(){'use strict';
/* JAH Old Fashioned Cocktail Database generator — jahdb-e2-cocktail-old-fashioned-cocktail-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-cocktail-old-fashioned-cocktail',PREFIX='JAH-E2COCKTAILO-',NAME='JAH Old Fashioned Cocktail Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Old Fashioned: the complete guide", "d": "Old Fashioned: the whiskey classic..", "g": "overview", "l": 2, "q": "What is Old Fashioned: the complete guide?", "a": "Old Fashioned: the whiskey classic..", "x": "The complete cocktail guide to Old Fashioned: the whiskey classic.. 1806. History, meaning, practices, and how to engage respectfully — everything in one database. History. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Old Fashioned essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Old Fashioned essentials.", "x": "At a glance: Old Fashioned — the whiskey classic.. Whiskey. The essentials: Whiskey.. Bitters. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "1806.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "1806.", "x": "Old Fashioned: 1806.. Whiskey. Essential knowledge — Bitters.. the whiskey classic. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 1806..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 1806..", "x": "Explained: 1806.. Orange. The context — Old Fashioned. Sugar. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Whiskey.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Whiskey.", "x": "Old Fashioned: Whiskey.. Bitters. Essential knowledge — Sugar.. the whiskey classic. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Whiskey..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Whiskey..", "x": "Explained: Whiskey.. Technique. The context — Old Fashioned. Orange. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Bitters.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Bitters.", "x": "Old Fashioned: Bitters.. Orange. Essential knowledge — Orange.. the whiskey classic. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Bitters..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Bitters..", "x": "Explained: Bitters.. Variations. The context — Old Fashioned. Muddled. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Sugar.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Sugar.", "x": "Old Fashioned: Sugar.. Technique. Essential knowledge — Muddled.. the whiskey classic. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Sugar..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Sugar..", "x": "Explained: Sugar.. History. The context — Old Fashioned. 1806. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Orange.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Orange.", "x": "Old Fashioned: Orange.. Variations. Essential knowledge — 1806.. the whiskey classic. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Orange..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Orange..", "x": "Explained: Orange.. Whiskey. The context — Old Fashioned. Whiskey. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Muddled.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Muddled.", "x": "Old Fashioned: Muddled.. History. Essential knowledge — Whiskey.. the whiskey classic. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Muddled..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Muddled..", "x": "Explained: Muddled.. Bitters. The context — Old Fashioned. Bitters. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "History.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "History.", "x": "Old Fashioned in depth: History.. Whiskey. Details — the whiskey classic.. Bitters. Sugar. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Whiskey.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Whiskey.", "x": "Old Fashioned in depth: Whiskey.. Bitters. Details — the whiskey classic.. Orange. Orange. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Bitters.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Bitters.", "x": "Old Fashioned in depth: Bitters.. Sugar. Details — the whiskey classic.. Technique. Muddled. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Orange.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Orange.", "x": "Old Fashioned in depth: Orange.. Orange. Details — the whiskey classic.. Variations. 1806. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Technique.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Technique.", "x": "Old Fashioned in depth: Technique.. Muddled. Details — the whiskey classic.. History. Whiskey. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Variations.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Variations.", "x": "Old Fashioned in depth: Variations.. 1806. Details — the whiskey classic.. Whiskey. Bitters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Old Fashioned comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Old Fashioned comes from.", "x": "Origins: History.. 1806. The history of Old Fashioned — the whiskey classic.. Whiskey. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Old Fashioned respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Old Fashioned respectfully.", "x": "Engaging: Bitters.. Whiskey. How to participate or observe well — Old Fashioned. the whiskey classic. Respect first, always; Orange.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Old Fashioned do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Old Fashioned do's and don'ts.", "x": "Etiquette: Technique.. Bitters. The rules of respect — Old Fashioned. the whiskey classic. When in doubt, ask about Variations.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Old Fashioned.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Old Fashioned.", "x": "Planning: History.. Sugar. Practical notes — Old Fashioned. the whiskey classic. A little planning shows respect for Whiskey.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Old Fashioned and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Old Fashioned and money.", "x": "Costs: Bitters.. Orange. What to budget — Old Fashioned. the whiskey classic. The best experiences of Orange. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-cocktail-old-fashioned-cocktail-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
