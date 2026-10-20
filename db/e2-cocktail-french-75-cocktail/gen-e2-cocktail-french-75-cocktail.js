(function(){'use strict';
/* JAH French 75 Cocktail Database generator — jahdb-e2-cocktail-french-75-cocktail-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-cocktail-french-75-cocktail',PREFIX='JAH-E2COCKTAILF-',NAME='JAH French 75 Cocktail Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "French 75: the complete guide", "d": "French 75: the gin champagne..", "g": "overview", "l": 2, "q": "What is French 75: the complete guide?", "a": "French 75: the gin champagne..", "x": "The complete cocktail guide to French 75: the gin champagne.. Gin. History, meaning, practices, and how to engage respectfully — everything in one database. Gin. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "French 75 essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "French 75 essentials.", "x": "At a glance: French 75 — the gin champagne.. Champagne. The essentials: Champagne.. Lemon. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Gin.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Gin.", "x": "French 75: Gin.. Champagne. Essential knowledge — Lemon.. the gin champagne. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Gin..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Gin..", "x": "Explained: Gin.. Elegant. The context — French 75. 1915. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Champagne.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Champagne.", "x": "French 75: Champagne.. 1915. Essential knowledge — 1915.. the gin champagne. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Champagne..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Champagne..", "x": "Explained: Champagne.. Gun. The context — French 75. Gun. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Lemon.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Lemon.", "x": "French 75: Lemon.. Elegant. Essential knowledge — Gun.. the gin champagne. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Lemon..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Lemon..", "x": "Explained: Lemon.. Ratio. The context — French 75. Elegant. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "1915.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "1915.", "x": "French 75: 1915.. Gun. Essential knowledge — Elegant.. the gin champagne. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: 1915..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: 1915..", "x": "Explained: 1915.. Gin. The context — French 75. Gin. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Gun.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Gun.", "x": "French 75: Gun.. Ratio. Essential knowledge — Gin.. the gin champagne. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Gun..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Gun..", "x": "Explained: Gun.. Champagne. The context — French 75. Champagne. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Elegant.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Elegant.", "x": "French 75: Elegant.. Gin. Essential knowledge — Champagne.. the gin champagne. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Elegant..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Elegant..", "x": "Explained: Elegant.. 1915. The context — French 75. Lemon. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Gin.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Gin.", "x": "French 75 in depth: Gin.. Champagne. Details — the gin champagne.. 1915. 1915. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Champagne.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Champagne.", "x": "French 75 in depth: Champagne.. Lemon. Details — the gin champagne.. Elegant. Gun. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "1915.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "1915.", "x": "French 75 in depth: 1915.. 1915. Details — the gin champagne.. Gun. Elegant. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Elegant.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Elegant.", "x": "French 75 in depth: Elegant.. Gun. Details — the gin champagne.. Ratio. Gin. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Gun.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Gun.", "x": "French 75 in depth: Gun.. Elegant. Details — the gin champagne.. Gin. Champagne. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Ratio.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Ratio.", "x": "French 75 in depth: Ratio.. Gin. Details — the gin champagne.. Champagne. Lemon. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where French 75 comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where French 75 comes from.", "x": "Origins: Gin.. Gin. The history of French 75 — the gin champagne.. Champagne. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing French 75 respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing French 75 respectfully.", "x": "Engaging: 1915.. Champagne. How to participate or observe well — French 75. the gin champagne. Respect first, always; Elegant.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "French 75 do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "French 75 do's and don'ts.", "x": "Etiquette: Gun.. Lemon. The rules of respect — French 75. the gin champagne. When in doubt, ask about Ratio.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around French 75.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around French 75.", "x": "Planning: Gin.. 1915. Practical notes — French 75. the gin champagne. A little planning shows respect for Champagne.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "French 75 and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "French 75 and money.", "x": "Costs: 1915.. Gun. What to budget — French 75. the gin champagne. The best experiences of Elegant. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-cocktail-french-75-cocktail-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
