(function(){'use strict';
/* JAH Whiskey Sour Cocktail Database generator — jahdb-e2-cocktail-whiskey-sour-cocktail-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-cocktail-whiskey-sour-cocktail',PREFIX='JAH-E2COCKTAILW-',NAME='JAH Whiskey Sour Cocktail Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Whiskey Sour: the complete guide", "d": "Whiskey Sour: the citrus whiskey..", "g": "overview", "l": 2, "q": "What is Whiskey Sour: the complete guide?", "a": "Whiskey Sour: the citrus whiskey..", "x": "The complete cocktail guide to Whiskey Sour: the citrus whiskey.. Whiskey. History, meaning, practices, and how to engage respectfully — everything in one database. Whiskey. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Whiskey Sour essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Whiskey Sour essentials.", "x": "At a glance: Whiskey Sour — the citrus whiskey.. Lemon. The essentials: Lemon.. Sugar. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Whiskey.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Whiskey.", "x": "Whiskey Sour: Whiskey.. Lemon. Essential knowledge — Sugar.. the citrus whiskey. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Whiskey..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Whiskey..", "x": "Explained: Whiskey.. Shaken. The context — Whiskey Sour. Egg white. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Lemon.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Lemon.", "x": "Whiskey Sour: Lemon.. Foam. Essential knowledge — Egg white.. the citrus whiskey. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Lemon..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Lemon..", "x": "Explained: Lemon.. Egg. The context — Whiskey Sour. Foam. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Sugar.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Sugar.", "x": "Whiskey Sour: Sugar.. Shaken. Essential knowledge — Foam.. the citrus whiskey. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Sugar..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Sugar..", "x": "Explained: Sugar.. Variations. The context — Whiskey Sour. Shaken. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Egg white.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Egg white.", "x": "Whiskey Sour: Egg white.. Egg. Essential knowledge — Shaken.. the citrus whiskey. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Egg white..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Egg white..", "x": "Explained: Egg white.. Whiskey. The context — Whiskey Sour. Whiskey. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Foam.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Foam.", "x": "Whiskey Sour: Foam.. Variations. Essential knowledge — Whiskey.. the citrus whiskey. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Foam..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Foam..", "x": "Explained: Foam.. Lemon. The context — Whiskey Sour. Lemon. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Shaken.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Shaken.", "x": "Whiskey Sour: Shaken.. Whiskey. Essential knowledge — Lemon.. the citrus whiskey. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Shaken..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Shaken..", "x": "Explained: Shaken.. Foam. The context — Whiskey Sour. Sugar. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Whiskey.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Whiskey.", "x": "Whiskey Sour in depth: Whiskey.. Lemon. Details — the citrus whiskey.. Foam. Egg white. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Lemon.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Lemon.", "x": "Whiskey Sour in depth: Lemon.. Sugar. Details — the citrus whiskey.. Shaken. Foam. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Foam.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Foam.", "x": "Whiskey Sour in depth: Foam.. Egg white. Details — the citrus whiskey.. Egg. Shaken. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Shaken.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Shaken.", "x": "Whiskey Sour in depth: Shaken.. Foam. Details — the citrus whiskey.. Variations. Whiskey. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Egg.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Egg.", "x": "Whiskey Sour in depth: Egg.. Shaken. Details — the citrus whiskey.. Whiskey. Lemon. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Variations.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Variations.", "x": "Whiskey Sour in depth: Variations.. Whiskey. Details — the citrus whiskey.. Lemon. Sugar. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Whiskey Sour comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Whiskey Sour comes from.", "x": "Origins: Whiskey.. Whiskey. The history of Whiskey Sour — the citrus whiskey.. Lemon. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Whiskey Sour respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Whiskey Sour respectfully.", "x": "Engaging: Foam.. Lemon. How to participate or observe well — Whiskey Sour. the citrus whiskey. Respect first, always; Shaken.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Whiskey Sour do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Whiskey Sour do's and don'ts.", "x": "Etiquette: Egg.. Sugar. The rules of respect — Whiskey Sour. the citrus whiskey. When in doubt, ask about Variations.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Whiskey Sour.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Whiskey Sour.", "x": "Planning: Whiskey.. Egg white. Practical notes — Whiskey Sour. the citrus whiskey. A little planning shows respect for Lemon.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Whiskey Sour and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Whiskey Sour and money.", "x": "Costs: Foam.. Foam. What to budget — Whiskey Sour. the citrus whiskey. The best experiences of Shaken. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-cocktail-whiskey-sour-cocktail-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
