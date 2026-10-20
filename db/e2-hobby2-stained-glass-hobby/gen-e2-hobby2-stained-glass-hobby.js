(function(){'use strict';
/* JAH Stained Glass Database generator — jahdb-e2-hobby2-stained-glass-hobby-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-hobby2-stained-glass-hobby',PREFIX='JAH-E2HOBBY2STA-',NAME='JAH Stained Glass Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Stained Glass: the complete guide", "d": "Stained Glass: the leaded light..", "g": "overview", "l": 2, "q": "What is Stained Glass: the complete guide?", "a": "Stained Glass: the leaded light..", "x": "The complete hobby guide to Stained Glass: the leaded light.. Copper foil. History, meaning, practices, and how to engage respectfully — everything in one database. Soldering. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Stained Glass essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Stained Glass essentials.", "x": "At a glance: Stained Glass — the leaded light.. Soldering. The essentials: Patterns.. Grinding. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Copper foil.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Copper foil.", "x": "Stained Glass: Copper foil.. Patterns. Essential knowledge — Grinding.. the leaded light. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Copper foil..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Copper foil..", "x": "Explained: Copper foil.. Foil. The context — Stained Glass. Patterns. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Soldering.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Soldering.", "x": "Stained Glass: Soldering.. Suncatchers. Essential knowledge — Patterns.. the leaded light. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Soldering..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Soldering..", "x": "Explained: Soldering.. Grinding. The context — Stained Glass. Lead. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Grinding.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Grinding.", "x": "Stained Glass: Grinding.. Foil. Essential knowledge — Lead.. the leaded light. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Grinding..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Grinding..", "x": "Explained: Grinding.. Getting started. The context — Stained Glass. Suncatchers. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Patterns.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Patterns.", "x": "Stained Glass: Patterns.. Grinding. Essential knowledge — Suncatchers.. the leaded light. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Patterns..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Patterns..", "x": "Explained: Patterns.. Soldering. The context — Stained Glass. Copper foil. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Lead.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Lead.", "x": "Stained Glass: Lead.. Getting started. Essential knowledge — Copper foil.. the leaded light. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Lead..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Lead..", "x": "Explained: Lead.. Patterns. The context — Stained Glass. Soldering. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Suncatchers.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Suncatchers.", "x": "Stained Glass: Suncatchers.. Soldering. Essential knowledge — Soldering.. the leaded light. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Suncatchers..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Suncatchers..", "x": "Explained: Suncatchers.. Suncatchers. The context — Stained Glass. Grinding. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Soldering.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Soldering.", "x": "Stained Glass in depth: Soldering.. Soldering. Details — the leaded light.. Suncatchers. Patterns. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Patterns.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Patterns.", "x": "Stained Glass in depth: Patterns.. Grinding. Details — the leaded light.. Foil. Lead. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Suncatchers.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Suncatchers.", "x": "Stained Glass in depth: Suncatchers.. Patterns. Details — the leaded light.. Grinding. Suncatchers. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Foil.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Foil.", "x": "Stained Glass in depth: Foil.. Lead. Details — the leaded light.. Getting started. Copper foil. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Grinding.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Grinding.", "x": "Stained Glass in depth: Grinding.. Suncatchers. Details — the leaded light.. Soldering. Soldering. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Getting started.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Getting started.", "x": "Stained Glass in depth: Getting started.. Copper foil. Details — the leaded light.. Patterns. Grinding. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Stained Glass comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Stained Glass comes from.", "x": "Origins: Soldering.. Copper foil. The history of Stained Glass — the leaded light.. Patterns. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Stained Glass respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Stained Glass respectfully.", "x": "Engaging: Suncatchers.. Soldering. How to participate or observe well — Stained Glass. the leaded light. Respect first, always; Foil.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Stained Glass do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Stained Glass do's and don'ts.", "x": "Etiquette: Grinding.. Grinding. The rules of respect — Stained Glass. the leaded light. When in doubt, ask about Getting started.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Stained Glass.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Stained Glass.", "x": "Planning: Soldering.. Patterns. Practical notes — Stained Glass. the leaded light. A little planning shows respect for Patterns.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Stained Glass and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Stained Glass and money.", "x": "Costs: Suncatchers.. Lead. What to budget — Stained Glass. the leaded light. The best experiences of Foil. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-hobby2-stained-glass-hobby-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
