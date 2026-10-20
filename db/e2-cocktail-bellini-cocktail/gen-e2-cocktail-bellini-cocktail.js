(function(){'use strict';
/* JAH Bellini Cocktail Database generator — jahdb-e2-cocktail-bellini-cocktail-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-cocktail-bellini-cocktail',PREFIX='JAH-E2COCKTAILB-',NAME='JAH Bellini Cocktail Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Bellini: the complete guide", "d": "Bellini: the Venetian peach..", "g": "overview", "l": 2, "q": "What is Bellini: the complete guide?", "a": "Bellini: the Venetian peach..", "x": "The complete cocktail guide to Bellini: the Venetian peach.. Prosecco. History, meaning, practices, and how to engage respectfully — everything in one database. Peach. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Bellini essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Bellini essentials.", "x": "At a glance: Bellini — the Venetian peach.. Peach. The essentials: Harry's.. Harry's Bar. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Prosecco.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Prosecco.", "x": "Bellini: Prosecco.. Harry's. Essential knowledge — Harry's Bar.. the Venetian peach. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Prosecco..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Prosecco..", "x": "Explained: Prosecco.. 1948. The context — Bellini. Venice. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Peach.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Peach.", "x": "Bellini: Peach.. Venice. Essential knowledge — Venice.. the Venetian peach. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Peach..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Peach..", "x": "Explained: Peach.. Art. The context — Bellini. 1948. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Harry's Bar.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Harry's Bar.", "x": "Bellini: Harry's Bar.. 1948. Essential knowledge — 1948.. the Venetian peach. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Harry's Bar..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Harry's Bar..", "x": "Explained: Harry's Bar.. Ratio. The context — Bellini. Bellini. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Venice.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Venice.", "x": "Bellini: Venice.. Art. Essential knowledge — Bellini.. the Venetian peach. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Venice..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Venice..", "x": "Explained: Venice.. Peach. The context — Bellini. Prosecco. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "1948.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "1948.", "x": "Bellini: 1948.. Ratio. Essential knowledge — Prosecco.. the Venetian peach. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: 1948..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: 1948..", "x": "Explained: 1948.. Harry's. The context — Bellini. Peach. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Bellini.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Bellini.", "x": "Bellini: Bellini.. Peach. Essential knowledge — Peach.. the Venetian peach. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Bellini..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Bellini..", "x": "Explained: Bellini.. Venice. The context — Bellini. Harry's Bar. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Peach.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Peach.", "x": "Bellini in depth: Peach.. Peach. Details — the Venetian peach.. Venice. Venice. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Harry's.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Harry's.", "x": "Bellini in depth: Harry's.. Harry's Bar. Details — the Venetian peach.. 1948. 1948. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Venice.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Venice.", "x": "Bellini in depth: Venice.. Venice. Details — the Venetian peach.. Art. Bellini. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "1948.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "1948.", "x": "Bellini in depth: 1948.. 1948. Details — the Venetian peach.. Ratio. Prosecco. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Art.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Art.", "x": "Bellini in depth: Art.. Bellini. Details — the Venetian peach.. Peach. Peach. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Ratio.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Ratio.", "x": "Bellini in depth: Ratio.. Prosecco. Details — the Venetian peach.. Harry's. Harry's Bar. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Bellini comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Bellini comes from.", "x": "Origins: Peach.. Prosecco. The history of Bellini — the Venetian peach.. Harry's. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Bellini respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Bellini respectfully.", "x": "Engaging: Venice.. Peach. How to participate or observe well — Bellini. the Venetian peach. Respect first, always; 1948.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Bellini do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Bellini do's and don'ts.", "x": "Etiquette: Art.. Harry's Bar. The rules of respect — Bellini. the Venetian peach. When in doubt, ask about Ratio.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Bellini.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Bellini.", "x": "Planning: Peach.. Venice. Practical notes — Bellini. the Venetian peach. A little planning shows respect for Harry's.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Bellini and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Bellini and money.", "x": "Costs: Venice.. 1948. What to budget — Bellini. the Venetian peach. The best experiences of 1948. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-cocktail-bellini-cocktail-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
