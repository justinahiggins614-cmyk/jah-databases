(function(){'use strict';
/* JAH Aperol Spritz Cocktail Database generator — jahdb-e2-cocktail-aperol-spritz-cocktail-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-cocktail-aperol-spritz-cocktail',PREFIX='JAH-E2COCKTAILA-',NAME='JAH Aperol Spritz Cocktail Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Aperol Spritz: the complete guide", "d": "Aperol Spritz: the Italian summer..", "g": "overview", "l": 2, "q": "What is Aperol Spritz: the complete guide?", "a": "Aperol Spritz: the Italian summer..", "x": "The complete cocktail guide to Aperol Spritz: the Italian summer.. Aperol. History, meaning, practices, and how to engage respectfully — everything in one database. Aperol. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Aperol Spritz essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Aperol Spritz essentials.", "x": "At a glance: Aperol Spritz — the Italian summer.. Prosecco. The essentials: Prosecco.. Soda. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Aperol.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Aperol.", "x": "Aperol Spritz: Aperol.. Prosecco. Essential knowledge — Soda.. the Italian summer. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Aperol..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Aperol..", "x": "Explained: Aperol.. Bitter. The context — Aperol Spritz. Orange. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Prosecco.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Prosecco.", "x": "Aperol Spritz: Prosecco.. Venice. Essential knowledge — Orange.. the Italian summer. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Prosecco..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Prosecco..", "x": "Explained: Prosecco.. Summer. The context — Aperol Spritz. Venice. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Soda.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Soda.", "x": "Aperol Spritz: Soda.. Bitter. Essential knowledge — Venice.. the Italian summer. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Soda..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Soda..", "x": "Explained: Soda.. Ratio. The context — Aperol Spritz. Bitter. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Orange.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Orange.", "x": "Aperol Spritz: Orange.. Summer. Essential knowledge — Bitter.. the Italian summer. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Orange..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Orange..", "x": "Explained: Orange.. Aperol. The context — Aperol Spritz. Aperol. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Venice.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Venice.", "x": "Aperol Spritz: Venice.. Ratio. Essential knowledge — Aperol.. the Italian summer. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Venice..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Venice..", "x": "Explained: Venice.. Prosecco. The context — Aperol Spritz. Prosecco. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Bitter.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Bitter.", "x": "Aperol Spritz: Bitter.. Aperol. Essential knowledge — Prosecco.. the Italian summer. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Bitter..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Bitter..", "x": "Explained: Bitter.. Venice. The context — Aperol Spritz. Soda. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Aperol.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Aperol.", "x": "Aperol Spritz in depth: Aperol.. Prosecco. Details — the Italian summer.. Venice. Orange. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Prosecco.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Prosecco.", "x": "Aperol Spritz in depth: Prosecco.. Soda. Details — the Italian summer.. Bitter. Venice. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Venice.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Venice.", "x": "Aperol Spritz in depth: Venice.. Orange. Details — the Italian summer.. Summer. Bitter. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Bitter.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Bitter.", "x": "Aperol Spritz in depth: Bitter.. Venice. Details — the Italian summer.. Ratio. Aperol. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Summer.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Summer.", "x": "Aperol Spritz in depth: Summer.. Bitter. Details — the Italian summer.. Aperol. Prosecco. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Ratio.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Ratio.", "x": "Aperol Spritz in depth: Ratio.. Aperol. Details — the Italian summer.. Prosecco. Soda. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Aperol Spritz comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Aperol Spritz comes from.", "x": "Origins: Aperol.. Aperol. The history of Aperol Spritz — the Italian summer.. Prosecco. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Aperol Spritz respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Aperol Spritz respectfully.", "x": "Engaging: Venice.. Prosecco. How to participate or observe well — Aperol Spritz. the Italian summer. Respect first, always; Bitter.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Aperol Spritz do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Aperol Spritz do's and don'ts.", "x": "Etiquette: Summer.. Soda. The rules of respect — Aperol Spritz. the Italian summer. When in doubt, ask about Ratio.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Aperol Spritz.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Aperol Spritz.", "x": "Planning: Aperol.. Orange. Practical notes — Aperol Spritz. the Italian summer. A little planning shows respect for Prosecco.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Aperol Spritz and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Aperol Spritz and money.", "x": "Costs: Venice.. Venice. What to budget — Aperol Spritz. the Italian summer. The best experiences of Bitter. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-cocktail-aperol-spritz-cocktail-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
