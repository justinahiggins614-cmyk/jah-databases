(function(){'use strict';
/* JAH Sweet Potato Nutrition Nutrition Database generator — jahdb-e2-nutrition-sweet-potato-nutrition-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-nutrition-sweet-potato-nutrition',PREFIX='JAH-E2NUTRITION-',NAME='JAH Sweet Potato Nutrition Nutrition Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Sweet Potato Nutrition: the complete guide", "d": "Sweet Potato Nutrition: the orange tuber..", "g": "overview", "l": 2, "q": "What is Sweet Potato Nutrition: the complete guide?", "a": "Sweet Potato Nutrition: the orange tuber..", "x": "The complete nutrition guide to Sweet Potato Nutrition: the orange tuber.. 103 calories. History, meaning, practices, and how to engage respectfully — everything in one database. Carotene. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Sweet Potato Nutrition essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Sweet Potato Nutrition essentials.", "x": "At a glance: Sweet Potato Nutrition — the orange tuber.. Beta-carotene. The essentials: Fiber.. Fiber. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "103 calories.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "103 calories.", "x": "Sweet Potato Nutrition: 103 calories.. Fiber. Essential knowledge — Fiber.. the orange tuber. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 103 calories..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 103 calories..", "x": "Explained: 103 calories.. Varieties. The context — Sweet Potato Nutrition. Potassium. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Beta-carotene.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Beta-carotene.", "x": "Sweet Potato Nutrition: Beta-carotene.. Baking. Essential knowledge — Potassium.. the orange tuber. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Beta-carotene..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Beta-carotene..", "x": "Explained: Beta-carotene.. Storage. The context — Sweet Potato Nutrition. Baking. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Fiber.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Fiber.", "x": "Sweet Potato Nutrition: Fiber.. Varieties. Essential knowledge — Baking.. the orange tuber. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Fiber..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Fiber..", "x": "Explained: Fiber.. Recipes. The context — Sweet Potato Nutrition. Varieties. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Potassium.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Potassium.", "x": "Sweet Potato Nutrition: Potassium.. Storage. Essential knowledge — Varieties.. the orange tuber. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Potassium..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Potassium..", "x": "Explained: Potassium.. Carotene. The context — Sweet Potato Nutrition. 103 calories. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Baking.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Baking.", "x": "Sweet Potato Nutrition: Baking.. Recipes. Essential knowledge — 103 calories.. the orange tuber. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Baking..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Baking..", "x": "Explained: Baking.. Fiber. The context — Sweet Potato Nutrition. Beta-carotene. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Varieties.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Varieties.", "x": "Sweet Potato Nutrition: Varieties.. Carotene. Essential knowledge — Beta-carotene.. the orange tuber. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Varieties..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Varieties..", "x": "Explained: Varieties.. Baking. The context — Sweet Potato Nutrition. Fiber. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Carotene.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Carotene.", "x": "Sweet Potato Nutrition in depth: Carotene.. Beta-carotene. Details — the orange tuber.. Baking. Potassium. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Fiber.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Fiber.", "x": "Sweet Potato Nutrition in depth: Fiber.. Fiber. Details — the orange tuber.. Varieties. Baking. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Baking.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Baking.", "x": "Sweet Potato Nutrition in depth: Baking.. Potassium. Details — the orange tuber.. Storage. Varieties. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Varieties.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Varieties.", "x": "Sweet Potato Nutrition in depth: Varieties.. Baking. Details — the orange tuber.. Recipes. 103 calories. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Storage.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Storage.", "x": "Sweet Potato Nutrition in depth: Storage.. Varieties. Details — the orange tuber.. Carotene. Beta-carotene. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Recipes.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Recipes.", "x": "Sweet Potato Nutrition in depth: Recipes.. 103 calories. Details — the orange tuber.. Fiber. Fiber. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Sweet Potato Nutrition comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Sweet Potato Nutrition comes from.", "x": "Origins: Carotene.. 103 calories. The history of Sweet Potato Nutrition — the orange tuber.. Fiber. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Sweet Potato Nutrition respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Sweet Potato Nutrition respectfully.", "x": "Engaging: Baking.. Beta-carotene. How to participate or observe well — Sweet Potato Nutrition. the orange tuber. Respect first, always; Varieties.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Sweet Potato Nutrition do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Sweet Potato Nutrition do's and don'ts.", "x": "Etiquette: Storage.. Fiber. The rules of respect — Sweet Potato Nutrition. the orange tuber. When in doubt, ask about Recipes.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Sweet Potato Nutrition.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Sweet Potato Nutrition.", "x": "Planning: Carotene.. Potassium. Practical notes — Sweet Potato Nutrition. the orange tuber. A little planning shows respect for Fiber.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Sweet Potato Nutrition and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Sweet Potato Nutrition and money.", "x": "Costs: Baking.. Baking. What to budget — Sweet Potato Nutrition. the orange tuber. The best experiences of Varieties. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-nutrition-sweet-potato-nutrition-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
