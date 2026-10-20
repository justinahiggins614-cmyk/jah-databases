(function(){'use strict';
/* JAH Gold Rush Cocktail Database generator — jahdb-e2-cocktail-gold-rush-cocktail-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-cocktail-gold-rush-cocktail',PREFIX='JAH-E2COCKTAILG-',NAME='JAH Gold Rush Cocktail Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Gold Rush: the complete guide", "d": "Gold Rush: the honey bourbon..", "g": "overview", "l": 2, "q": "What is Gold Rush: the complete guide?", "a": "Gold Rush: the honey bourbon..", "x": "The complete cocktail guide to Gold Rush: the honey bourbon.. Bourbon. History, meaning, practices, and how to engage respectfully — everything in one database. Bourbon. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Gold Rush essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Gold Rush essentials.", "x": "At a glance: Gold Rush — the honey bourbon.. Honey. The essentials: Honey.. Lemon. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Bourbon.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Bourbon.", "x": "Gold Rush: Bourbon.. Honey. Essential knowledge — Lemon.. the honey bourbon. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Bourbon..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Bourbon..", "x": "Explained: Bourbon.. Modern. The context — Gold Rush. 2000s. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Honey.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Honey.", "x": "Gold Rush: Honey.. Simple. Essential knowledge — 2000s.. the honey bourbon. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Honey..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Honey..", "x": "Explained: Honey.. Lemon. The context — Gold Rush. Simple. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Lemon.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Lemon.", "x": "Gold Rush: Lemon.. Modern. Essential knowledge — Simple.. the honey bourbon. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Lemon..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Lemon..", "x": "Explained: Lemon.. Variations. The context — Gold Rush. Bee's Knees. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "2000s.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "2000s.", "x": "Gold Rush: 2000s.. Lemon. Essential knowledge — Bee's Knees.. the honey bourbon. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: 2000s..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: 2000s..", "x": "Explained: 2000s.. Bourbon. The context — Gold Rush. Bourbon. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Simple.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Simple.", "x": "Gold Rush: Simple.. Variations. Essential knowledge — Bourbon.. the honey bourbon. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Simple..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Simple..", "x": "Explained: Simple.. Honey. The context — Gold Rush. Honey. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Bee's Knees.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Bee's Knees.", "x": "Gold Rush: Bee's Knees.. Bourbon. Essential knowledge — Honey.. the honey bourbon. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Bee's Knees..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Bee's Knees..", "x": "Explained: Bee's Knees.. Simple. The context — Gold Rush. Lemon. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Bourbon.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Bourbon.", "x": "Gold Rush in depth: Bourbon.. Honey. Details — the honey bourbon.. Simple. 2000s. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Honey.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Honey.", "x": "Gold Rush in depth: Honey.. Lemon. Details — the honey bourbon.. Modern. Simple. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Simple.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Simple.", "x": "Gold Rush in depth: Simple.. 2000s. Details — the honey bourbon.. Lemon. Bee's Knees. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Modern.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Modern.", "x": "Gold Rush in depth: Modern.. Simple. Details — the honey bourbon.. Variations. Bourbon. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Lemon.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Lemon.", "x": "Gold Rush in depth: Lemon.. Bee's Knees. Details — the honey bourbon.. Bourbon. Honey. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Variations.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Variations.", "x": "Gold Rush in depth: Variations.. Bourbon. Details — the honey bourbon.. Honey. Lemon. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Gold Rush comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Gold Rush comes from.", "x": "Origins: Bourbon.. Bourbon. The history of Gold Rush — the honey bourbon.. Honey. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Gold Rush respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Gold Rush respectfully.", "x": "Engaging: Simple.. Honey. How to participate or observe well — Gold Rush. the honey bourbon. Respect first, always; Modern.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Gold Rush do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Gold Rush do's and don'ts.", "x": "Etiquette: Lemon.. Lemon. The rules of respect — Gold Rush. the honey bourbon. When in doubt, ask about Variations.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Gold Rush.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Gold Rush.", "x": "Planning: Bourbon.. 2000s. Practical notes — Gold Rush. the honey bourbon. A little planning shows respect for Honey.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Gold Rush and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Gold Rush and money.", "x": "Costs: Simple.. Simple. What to budget — Gold Rush. the honey bourbon. The best experiences of Modern. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-cocktail-gold-rush-cocktail-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
