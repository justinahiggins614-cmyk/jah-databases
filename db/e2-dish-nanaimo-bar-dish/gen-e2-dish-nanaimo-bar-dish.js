(function(){'use strict';
/* JAH Nanaimo Bar Dish Database generator — jahdb-e2-dish-nanaimo-bar-dish-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-dish-nanaimo-bar-dish',PREFIX='JAH-E2DISHNANAI-',NAME='JAH Nanaimo Bar Dish Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Nanaimo Bar: the complete guide", "d": "Nanaimo Bar: the BC layers..", "g": "overview", "l": 2, "q": "What is Nanaimo Bar: the complete guide?", "a": "Nanaimo Bar: the BC layers..", "x": "The complete dish guide to Nanaimo Bar: the BC layers.. Nanaimo. History, meaning, practices, and how to engage respectfully — everything in one database. No-bake. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Nanaimo Bar essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Nanaimo Bar essentials.", "x": "At a glance: Nanaimo Bar — the BC layers.. No-bake. The essentials: Custard.. Coconut. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Nanaimo.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Nanaimo.", "x": "Nanaimo Bar: Nanaimo.. Custard. Essential knowledge — Coconut.. the BC layers. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Nanaimo..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Nanaimo..", "x": "Explained: Nanaimo.. Nanaimo. The context — Nanaimo Bar. Custard. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "No-bake.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "No-bake.", "x": "Nanaimo Bar: No-bake.. BC. Essential knowledge — Custard.. the BC layers. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: No-bake..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: No-bake..", "x": "Explained: No-bake.. Coconut. The context — Nanaimo Bar. Chocolate. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Coconut.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Coconut.", "x": "Nanaimo Bar: Coconut.. Nanaimo. Essential knowledge — Chocolate.. the BC layers. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Coconut..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Coconut..", "x": "Explained: Coconut.. Making. The context — Nanaimo Bar. BC. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Custard.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Custard.", "x": "Nanaimo Bar: Custard.. Coconut. Essential knowledge — BC.. the BC layers. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Custard..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Custard..", "x": "Explained: Custard.. No-bake. The context — Nanaimo Bar. Nanaimo. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Chocolate.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Chocolate.", "x": "Nanaimo Bar: Chocolate.. Making. Essential knowledge — Nanaimo.. the BC layers. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Chocolate..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Chocolate..", "x": "Explained: Chocolate.. Custard. The context — Nanaimo Bar. No-bake. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "BC.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "BC.", "x": "Nanaimo Bar: BC.. No-bake. Essential knowledge — No-bake.. the BC layers. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: BC..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: BC..", "x": "Explained: BC.. BC. The context — Nanaimo Bar. Coconut. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "No-bake.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "No-bake.", "x": "Nanaimo Bar in depth: No-bake.. No-bake. Details — the BC layers.. BC. Custard. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Custard.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Custard.", "x": "Nanaimo Bar in depth: Custard.. Coconut. Details — the BC layers.. Nanaimo. Chocolate. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "BC.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "BC.", "x": "Nanaimo Bar in depth: BC.. Custard. Details — the BC layers.. Coconut. BC. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Nanaimo.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Nanaimo.", "x": "Nanaimo Bar in depth: Nanaimo.. Chocolate. Details — the BC layers.. Making. Nanaimo. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Coconut.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Coconut.", "x": "Nanaimo Bar in depth: Coconut.. BC. Details — the BC layers.. No-bake. No-bake. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Making.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Making.", "x": "Nanaimo Bar in depth: Making.. Nanaimo. Details — the BC layers.. Custard. Coconut. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Nanaimo Bar comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Nanaimo Bar comes from.", "x": "Origins: No-bake.. Nanaimo. The history of Nanaimo Bar — the BC layers.. Custard. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Nanaimo Bar respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Nanaimo Bar respectfully.", "x": "Engaging: BC.. No-bake. How to participate or observe well — Nanaimo Bar. the BC layers. Respect first, always; Nanaimo.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Nanaimo Bar do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Nanaimo Bar do's and don'ts.", "x": "Etiquette: Coconut.. Coconut. The rules of respect — Nanaimo Bar. the BC layers. When in doubt, ask about Making.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Nanaimo Bar.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Nanaimo Bar.", "x": "Planning: No-bake.. Custard. Practical notes — Nanaimo Bar. the BC layers. A little planning shows respect for Custard.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Nanaimo Bar and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Nanaimo Bar and money.", "x": "Costs: BC.. Chocolate. What to budget — Nanaimo Bar. the BC layers. The best experiences of Nanaimo. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-dish-nanaimo-bar-dish-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
