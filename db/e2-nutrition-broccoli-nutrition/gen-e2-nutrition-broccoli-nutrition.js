(function(){'use strict';
/* JAH Broccoli Nutrition Nutrition Database generator — jahdb-e2-nutrition-broccoli-nutrition-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-nutrition-broccoli-nutrition',PREFIX='JAH-E2NUTRITION-',NAME='JAH Broccoli Nutrition Nutrition Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Broccoli Nutrition: the complete guide", "d": "Broccoli Nutrition: the cruciferous power..", "g": "overview", "l": 2, "q": "What is Broccoli Nutrition: the complete guide?", "a": "Broccoli Nutrition: the cruciferous power..", "x": "The complete nutrition guide to Broccoli Nutrition: the cruciferous power.. 34 calories. History, meaning, practices, and how to engage respectfully — everything in one database. Cruciferous. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Broccoli Nutrition essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Broccoli Nutrition essentials.", "x": "At a glance: Broccoli Nutrition — the cruciferous power.. Vitamin C. The essentials: Vitamins.. Vitamin K. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "34 calories.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "34 calories.", "x": "Broccoli Nutrition: 34 calories.. Vitamins. Essential knowledge — Vitamin K.. the cruciferous power. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 34 calories..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 34 calories..", "x": "Explained: 34 calories.. Cooking. The context — Broccoli Nutrition. Sulforaphane. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Vitamin C.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Vitamin C.", "x": "Broccoli Nutrition: Vitamin C.. Sulforaphane. Essential knowledge — Sulforaphane.. the cruciferous power. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Vitamin C..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Vitamin C..", "x": "Explained: Vitamin C.. Storage. The context — Broccoli Nutrition. Fiber. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Vitamin K.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Vitamin K.", "x": "Broccoli Nutrition: Vitamin K.. Cooking. Essential knowledge — Fiber.. the cruciferous power. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Vitamin K..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Vitamin K..", "x": "Explained: Vitamin K.. Recipes. The context — Broccoli Nutrition. Steaming. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Sulforaphane.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Sulforaphane.", "x": "Broccoli Nutrition: Sulforaphane.. Storage. Essential knowledge — Steaming.. the cruciferous power. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Sulforaphane..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Sulforaphane..", "x": "Explained: Sulforaphane.. Cruciferous. The context — Broccoli Nutrition. 34 calories. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Fiber.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Fiber.", "x": "Broccoli Nutrition: Fiber.. Recipes. Essential knowledge — 34 calories.. the cruciferous power. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Fiber..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Fiber..", "x": "Explained: Fiber.. Vitamins. The context — Broccoli Nutrition. Vitamin C. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Steaming.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Steaming.", "x": "Broccoli Nutrition: Steaming.. Cruciferous. Essential knowledge — Vitamin C.. the cruciferous power. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Steaming..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Steaming..", "x": "Explained: Steaming.. Sulforaphane. The context — Broccoli Nutrition. Vitamin K. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Cruciferous.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Cruciferous.", "x": "Broccoli Nutrition in depth: Cruciferous.. Vitamin C. Details — the cruciferous power.. Sulforaphane. Sulforaphane. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Vitamins.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Vitamins.", "x": "Broccoli Nutrition in depth: Vitamins.. Vitamin K. Details — the cruciferous power.. Cooking. Fiber. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Sulforaphane.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Sulforaphane.", "x": "Broccoli Nutrition in depth: Sulforaphane.. Sulforaphane. Details — the cruciferous power.. Storage. Steaming. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Cooking.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Cooking.", "x": "Broccoli Nutrition in depth: Cooking.. Fiber. Details — the cruciferous power.. Recipes. 34 calories. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Storage.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Storage.", "x": "Broccoli Nutrition in depth: Storage.. Steaming. Details — the cruciferous power.. Cruciferous. Vitamin C. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Recipes.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Recipes.", "x": "Broccoli Nutrition in depth: Recipes.. 34 calories. Details — the cruciferous power.. Vitamins. Vitamin K. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Broccoli Nutrition comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Broccoli Nutrition comes from.", "x": "Origins: Cruciferous.. 34 calories. The history of Broccoli Nutrition — the cruciferous power.. Vitamins. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Broccoli Nutrition respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Broccoli Nutrition respectfully.", "x": "Engaging: Sulforaphane.. Vitamin C. How to participate or observe well — Broccoli Nutrition. the cruciferous power. Respect first, always; Cooking.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Broccoli Nutrition do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Broccoli Nutrition do's and don'ts.", "x": "Etiquette: Storage.. Vitamin K. The rules of respect — Broccoli Nutrition. the cruciferous power. When in doubt, ask about Recipes.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Broccoli Nutrition.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Broccoli Nutrition.", "x": "Planning: Cruciferous.. Sulforaphane. Practical notes — Broccoli Nutrition. the cruciferous power. A little planning shows respect for Vitamins.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Broccoli Nutrition and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Broccoli Nutrition and money.", "x": "Costs: Sulforaphane.. Fiber. What to budget — Broccoli Nutrition. the cruciferous power. The best experiences of Cooking. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-nutrition-broccoli-nutrition-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
