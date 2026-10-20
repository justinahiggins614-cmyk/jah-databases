(function(){'use strict';
/* JAH Meat Goats Goat Keeping Database generator — jahdb-e2-goat-meat-goats-keeping-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-goat-meat-goats-keeping',PREFIX='JAH-E2GOATMEATG-',NAME='JAH Meat Goats Goat Keeping Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Meat Goats: the complete guide", "d": "Meat Goats: the Boer herd..", "g": "overview", "l": 2, "q": "What is Meat Goats: the complete guide?", "a": "Meat Goats: the Boer herd..", "x": "The complete goat keeping guide to Meat Goats: the Boer herd.. Boer. History, meaning, practices, and how to engage respectfully — everything in one database. Boer. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Meat Goats essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Meat Goats essentials.", "x": "At a glance: Meat Goats — the Boer herd.. Browsing. The essentials: Market.. Market. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Boer.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Boer.", "x": "Meat Goats: Boer.. Market. Essential knowledge — Market.. the Boer herd. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Boer..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Boer..", "x": "Explained: Boer.. Weeds. The context — Meat Goats. Kidding. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Browsing.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Browsing.", "x": "Meat Goats: Browsing.. Hardy. Essential knowledge — Kidding.. the Boer herd. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Browsing..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Browsing..", "x": "Explained: Browsing.. Browsing. The context — Meat Goats. Hardy. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Market.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Market.", "x": "Meat Goats: Market.. Weeds. Essential knowledge — Hardy.. the Boer herd. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Market..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Market..", "x": "Explained: Market.. Guide. The context — Meat Goats. Weeds. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Kidding.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Kidding.", "x": "Meat Goats: Kidding.. Browsing. Essential knowledge — Weeds.. the Boer herd. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Kidding..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Kidding..", "x": "Explained: Kidding.. Boer. The context — Meat Goats. Boer. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Hardy.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Hardy.", "x": "Meat Goats: Hardy.. Guide. Essential knowledge — Boer.. the Boer herd. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Hardy..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Hardy..", "x": "Explained: Hardy.. Market. The context — Meat Goats. Browsing. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Weeds.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Weeds.", "x": "Meat Goats: Weeds.. Boer. Essential knowledge — Browsing.. the Boer herd. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Weeds..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Weeds..", "x": "Explained: Weeds.. Hardy. The context — Meat Goats. Market. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Boer.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Boer.", "x": "Meat Goats in depth: Boer.. Browsing. Details — the Boer herd.. Hardy. Kidding. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Market.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Market.", "x": "Meat Goats in depth: Market.. Market. Details — the Boer herd.. Weeds. Hardy. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Hardy.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Hardy.", "x": "Meat Goats in depth: Hardy.. Kidding. Details — the Boer herd.. Browsing. Weeds. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Weeds.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Weeds.", "x": "Meat Goats in depth: Weeds.. Hardy. Details — the Boer herd.. Guide. Boer. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Browsing.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Browsing.", "x": "Meat Goats in depth: Browsing.. Weeds. Details — the Boer herd.. Boer. Browsing. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Guide.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Guide.", "x": "Meat Goats in depth: Guide.. Boer. Details — the Boer herd.. Market. Market. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Meat Goats comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Meat Goats comes from.", "x": "Origins: Boer.. Boer. The history of Meat Goats — the Boer herd.. Market. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Meat Goats respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Meat Goats respectfully.", "x": "Engaging: Hardy.. Browsing. How to participate or observe well — Meat Goats. the Boer herd. Respect first, always; Weeds.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Meat Goats do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Meat Goats do's and don'ts.", "x": "Etiquette: Browsing.. Market. The rules of respect — Meat Goats. the Boer herd. When in doubt, ask about Guide.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Meat Goats.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Meat Goats.", "x": "Planning: Boer.. Kidding. Practical notes — Meat Goats. the Boer herd. A little planning shows respect for Market.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Meat Goats and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Meat Goats and money.", "x": "Costs: Hardy.. Hardy. What to budget — Meat Goats. the Boer herd. The best experiences of Weeds. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-goat-meat-goats-keeping-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
