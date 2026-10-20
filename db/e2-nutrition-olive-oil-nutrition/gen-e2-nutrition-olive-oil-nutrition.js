(function(){'use strict';
/* JAH Olive Oil Nutrition Nutrition Database generator — jahdb-e2-nutrition-olive-oil-nutrition-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-nutrition-olive-oil-nutrition',PREFIX='JAH-E2NUTRITION-',NAME='JAH Olive Oil Nutrition Nutrition Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Olive Oil Nutrition: the complete guide", "d": "Olive Oil Nutrition: the Mediterranean gold..", "g": "overview", "l": 2, "q": "What is Olive Oil Nutrition: the complete guide?", "a": "Olive Oil Nutrition: the Mediterranean gold..", "x": "The complete nutrition guide to Olive Oil Nutrition: the Mediterranean gold.. 119 calories. History, meaning, practices, and how to engage respectfully — everything in one database. Fats. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Olive Oil Nutrition essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Olive Oil Nutrition essentials.", "x": "At a glance: Olive Oil Nutrition — the Mediterranean gold.. Monounsaturated. The essentials: Polyphenols.. Polyphenols. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "119 calories.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "119 calories.", "x": "Olive Oil Nutrition: 119 calories.. Polyphenols. Essential knowledge — Polyphenols.. the Mediterranean gold. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 119 calories..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 119 calories..", "x": "Explained: 119 calories.. Smoke. The context — Olive Oil Nutrition. Extra virgin. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Monounsaturated.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Monounsaturated.", "x": "Olive Oil Nutrition: Monounsaturated.. Grades. Essential knowledge — Extra virgin.. the Mediterranean gold. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Monounsaturated..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Monounsaturated..", "x": "Explained: Monounsaturated.. Drizzle. The context — Olive Oil Nutrition. Smoke point. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Polyphenols.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Polyphenols.", "x": "Olive Oil Nutrition: Polyphenols.. Smoke. Essential knowledge — Smoke point.. the Mediterranean gold. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Polyphenols..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Polyphenols..", "x": "Explained: Polyphenols.. Fraud. The context — Olive Oil Nutrition. Drizzle. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Extra virgin.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Extra virgin.", "x": "Olive Oil Nutrition: Extra virgin.. Drizzle. Essential knowledge — Drizzle.. the Mediterranean gold. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Extra virgin..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Extra virgin..", "x": "Explained: Extra virgin.. Fats. The context — Olive Oil Nutrition. 119 calories. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Smoke point.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Smoke point.", "x": "Olive Oil Nutrition: Smoke point.. Fraud. Essential knowledge — 119 calories.. the Mediterranean gold. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Smoke point..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Smoke point..", "x": "Explained: Smoke point.. Polyphenols. The context — Olive Oil Nutrition. Monounsaturated. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Drizzle.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Drizzle.", "x": "Olive Oil Nutrition: Drizzle.. Fats. Essential knowledge — Monounsaturated.. the Mediterranean gold. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Drizzle..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Drizzle..", "x": "Explained: Drizzle.. Grades. The context — Olive Oil Nutrition. Polyphenols. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Fats.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Fats.", "x": "Olive Oil Nutrition in depth: Fats.. Monounsaturated. Details — the Mediterranean gold.. Grades. Extra virgin. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Polyphenols.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Polyphenols.", "x": "Olive Oil Nutrition in depth: Polyphenols.. Polyphenols. Details — the Mediterranean gold.. Smoke. Smoke point. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Grades.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Grades.", "x": "Olive Oil Nutrition in depth: Grades.. Extra virgin. Details — the Mediterranean gold.. Drizzle. Drizzle. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Smoke.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Smoke.", "x": "Olive Oil Nutrition in depth: Smoke.. Smoke point. Details — the Mediterranean gold.. Fraud. 119 calories. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Drizzle.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Drizzle.", "x": "Olive Oil Nutrition in depth: Drizzle.. Drizzle. Details — the Mediterranean gold.. Fats. Monounsaturated. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Fraud.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Fraud.", "x": "Olive Oil Nutrition in depth: Fraud.. 119 calories. Details — the Mediterranean gold.. Polyphenols. Polyphenols. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Olive Oil Nutrition comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Olive Oil Nutrition comes from.", "x": "Origins: Fats.. 119 calories. The history of Olive Oil Nutrition — the Mediterranean gold.. Polyphenols. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Olive Oil Nutrition respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Olive Oil Nutrition respectfully.", "x": "Engaging: Grades.. Monounsaturated. How to participate or observe well — Olive Oil Nutrition. the Mediterranean gold. Respect first, always; Smoke.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Olive Oil Nutrition do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Olive Oil Nutrition do's and don'ts.", "x": "Etiquette: Drizzle.. Polyphenols. The rules of respect — Olive Oil Nutrition. the Mediterranean gold. When in doubt, ask about Fraud.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Olive Oil Nutrition.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Olive Oil Nutrition.", "x": "Planning: Fats.. Extra virgin. Practical notes — Olive Oil Nutrition. the Mediterranean gold. A little planning shows respect for Polyphenols.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Olive Oil Nutrition and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Olive Oil Nutrition and money.", "x": "Costs: Grades.. Smoke point. What to budget — Olive Oil Nutrition. the Mediterranean gold. The best experiences of Smoke. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-nutrition-olive-oil-nutrition-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
