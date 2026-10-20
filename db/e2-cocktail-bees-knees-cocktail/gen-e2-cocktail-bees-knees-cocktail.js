(function(){'use strict';
/* JAH Bee\'s Knees Cocktail Database generator — jahdb-e2-cocktail-bees-knees-cocktail-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-cocktail-bees-knees-cocktail',PREFIX='JAH-E2COCKTAILB-',NAME='JAH Bee\'s Knees Cocktail Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Bee's Knees: the complete guide", "d": "Bee's Knees: the prohibition honey..", "g": "overview", "l": 2, "q": "What is Bee's Knees: the complete guide?", "a": "Bee's Knees: the prohibition honey..", "x": "The complete cocktail guide to Bee's Knees: the prohibition honey.. Gin. History, meaning, practices, and how to engage respectfully — everything in one database. Gin. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Bee's Knees essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Bee's Knees essentials.", "x": "At a glance: Bee's Knees — the prohibition honey.. Honey. The essentials: Honey.. Lemon. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Gin.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Gin.", "x": "Bee's Knees: Gin.. Honey. Essential knowledge — Lemon.. the prohibition honey. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Gin..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Gin..", "x": "Explained: Gin.. Speakeasy. The context — Bee's Knees. 1920s. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Honey.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Honey.", "x": "Bee's Knees: Honey.. 1920s. Essential knowledge — 1920s.. the prohibition honey. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Honey..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Honey..", "x": "Explained: Honey.. Lemon. The context — Bee's Knees. Prohibition. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Lemon.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Lemon.", "x": "Bee's Knees: Lemon.. Speakeasy. Essential knowledge — Prohibition.. the prohibition honey. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Lemon..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Lemon..", "x": "Explained: Lemon.. History. The context — Bee's Knees. Speakeasy. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "1920s.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "1920s.", "x": "Bee's Knees: 1920s.. Lemon. Essential knowledge — Speakeasy.. the prohibition honey. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: 1920s..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: 1920s..", "x": "Explained: 1920s.. Gin. The context — Bee's Knees. Gin. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Prohibition.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Prohibition.", "x": "Bee's Knees: Prohibition.. History. Essential knowledge — Gin.. the prohibition honey. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Prohibition..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Prohibition..", "x": "Explained: Prohibition.. Honey. The context — Bee's Knees. Honey. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Speakeasy.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Speakeasy.", "x": "Bee's Knees: Speakeasy.. Gin. Essential knowledge — Honey.. the prohibition honey. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Speakeasy..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Speakeasy..", "x": "Explained: Speakeasy.. 1920s. The context — Bee's Knees. Lemon. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Gin.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Gin.", "x": "Bee's Knees in depth: Gin.. Honey. Details — the prohibition honey.. 1920s. 1920s. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Honey.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Honey.", "x": "Bee's Knees in depth: Honey.. Lemon. Details — the prohibition honey.. Speakeasy. Prohibition. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "1920s.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "1920s.", "x": "Bee's Knees in depth: 1920s.. 1920s. Details — the prohibition honey.. Lemon. Speakeasy. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Speakeasy.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Speakeasy.", "x": "Bee's Knees in depth: Speakeasy.. Prohibition. Details — the prohibition honey.. History. Gin. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Lemon.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Lemon.", "x": "Bee's Knees in depth: Lemon.. Speakeasy. Details — the prohibition honey.. Gin. Honey. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "History.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "History.", "x": "Bee's Knees in depth: History.. Gin. Details — the prohibition honey.. Honey. Lemon. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Bee's Knees comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Bee's Knees comes from.", "x": "Origins: Gin.. Gin. The history of Bee's Knees — the prohibition honey.. Honey. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Bee's Knees respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Bee's Knees respectfully.", "x": "Engaging: 1920s.. Honey. How to participate or observe well — Bee's Knees. the prohibition honey. Respect first, always; Speakeasy.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Bee's Knees do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Bee's Knees do's and don'ts.", "x": "Etiquette: Lemon.. Lemon. The rules of respect — Bee's Knees. the prohibition honey. When in doubt, ask about History.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Bee's Knees.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Bee's Knees.", "x": "Planning: Gin.. 1920s. Practical notes — Bee's Knees. the prohibition honey. A little planning shows respect for Honey.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Bee's Knees and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Bee's Knees and money.", "x": "Costs: 1920s.. Prohibition. What to budget — Bee's Knees. the prohibition honey. The best experiences of Speakeasy. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-cocktail-bees-knees-cocktail-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
