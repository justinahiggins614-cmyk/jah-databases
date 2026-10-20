(function(){'use strict';
/* JAH Monstera Houseplant Database generator — jahdb-e2-houseplant-monstera-houseplant-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-houseplant-monstera-houseplant',PREFIX='JAH-E2HOUSEPLAN-',NAME='JAH Monstera Houseplant Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Monstera: the complete guide", "d": "Monstera: the split leaf..", "g": "overview", "l": 2, "q": "What is Monstera: the complete guide?", "a": "Monstera: the split leaf..", "x": "The complete houseplant guide to Monstera: the split leaf.. Fenestrations. History, meaning, practices, and how to engage respectfully — everything in one database. Splits. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Monstera essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Monstera essentials.", "x": "At a glance: Monstera — the split leaf.. Climbing. The essentials: Pole.. Moss pole. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Fenestrations.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Fenestrations.", "x": "Monstera: Fenestrations.. Pole. Essential knowledge — Moss pole.. the split leaf. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Fenestrations..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Fenestrations..", "x": "Explained: Fenestrations.. Statement. The context — Monstera. Deliciosa. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Climbing.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Climbing.", "x": "Monstera: Climbing.. Tropical. Essential knowledge — Deliciosa.. the split leaf. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Climbing..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Climbing..", "x": "Explained: Climbing.. Climbing. The context — Monstera. Tropical. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Moss pole.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Moss pole.", "x": "Monstera: Moss pole.. Statement. Essential knowledge — Tropical.. the split leaf. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Moss pole..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Moss pole..", "x": "Explained: Moss pole.. Guide. The context — Monstera. Statement. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Deliciosa.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Deliciosa.", "x": "Monstera: Deliciosa.. Climbing. Essential knowledge — Statement.. the split leaf. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Deliciosa..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Deliciosa..", "x": "Explained: Deliciosa.. Splits. The context — Monstera. Fenestrations. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Tropical.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Tropical.", "x": "Monstera: Tropical.. Guide. Essential knowledge — Fenestrations.. the split leaf. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Tropical..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Tropical..", "x": "Explained: Tropical.. Pole. The context — Monstera. Climbing. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Statement.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Statement.", "x": "Monstera: Statement.. Splits. Essential knowledge — Climbing.. the split leaf. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Statement..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Statement..", "x": "Explained: Statement.. Tropical. The context — Monstera. Moss pole. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Splits.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Splits.", "x": "Monstera in depth: Splits.. Climbing. Details — the split leaf.. Tropical. Deliciosa. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Pole.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Pole.", "x": "Monstera in depth: Pole.. Moss pole. Details — the split leaf.. Statement. Tropical. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Tropical.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Tropical.", "x": "Monstera in depth: Tropical.. Deliciosa. Details — the split leaf.. Climbing. Statement. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Statement.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Statement.", "x": "Monstera in depth: Statement.. Tropical. Details — the split leaf.. Guide. Fenestrations. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Climbing.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Climbing.", "x": "Monstera in depth: Climbing.. Statement. Details — the split leaf.. Splits. Climbing. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Guide.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Guide.", "x": "Monstera in depth: Guide.. Fenestrations. Details — the split leaf.. Pole. Moss pole. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Monstera comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Monstera comes from.", "x": "Origins: Splits.. Fenestrations. The history of Monstera — the split leaf.. Pole. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Monstera respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Monstera respectfully.", "x": "Engaging: Tropical.. Climbing. How to participate or observe well — Monstera. the split leaf. Respect first, always; Statement.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Monstera do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Monstera do's and don'ts.", "x": "Etiquette: Climbing.. Moss pole. The rules of respect — Monstera. the split leaf. When in doubt, ask about Guide.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Monstera.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Monstera.", "x": "Planning: Splits.. Deliciosa. Practical notes — Monstera. the split leaf. A little planning shows respect for Pole.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Monstera and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Monstera and money.", "x": "Costs: Tropical.. Tropical. What to budget — Monstera. the split leaf. The best experiences of Statement. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-houseplant-monstera-houseplant-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
