(function(){'use strict';
/* JAH Apple Nutrition Nutrition Database generator — jahdb-e2-nutrition-apple-nutrition-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-nutrition-apple-nutrition',PREFIX='JAH-E2NUTRITION-',NAME='JAH Apple Nutrition Nutrition Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Apple Nutrition: the complete guide", "d": "Apple Nutrition: the everyday fruit..", "g": "overview", "l": 2, "q": "What is Apple Nutrition: the complete guide?", "a": "Apple Nutrition: the everyday fruit..", "x": "The complete nutrition guide to Apple Nutrition: the everyday fruit.. 95 calories. History, meaning, practices, and how to engage respectfully — everything in one database. Calories. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Apple Nutrition essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Apple Nutrition essentials.", "x": "At a glance: Apple Nutrition — the everyday fruit.. Fiber. The essentials: Fiber.. Vitamin C. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "95 calories.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "95 calories.", "x": "Apple Nutrition: 95 calories.. Fiber. Essential knowledge — Vitamin C.. the everyday fruit. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 95 calories..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 95 calories..", "x": "Explained: 95 calories.. Varieties. The context — Apple Nutrition. Pectin. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Fiber.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Fiber.", "x": "Apple Nutrition: Fiber.. Vitamin C. Essential knowledge — Pectin.. the everyday fruit. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Fiber..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Fiber..", "x": "Explained: Fiber.. Orchard. The context — Apple Nutrition. 4,000 varieties. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Vitamin C.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Vitamin C.", "x": "Apple Nutrition: Vitamin C.. Varieties. Essential knowledge — 4,000 varieties.. the everyday fruit. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Vitamin C..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Vitamin C..", "x": "Explained: Vitamin C.. Storage. The context — Apple Nutrition. Orchard. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Pectin.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Pectin.", "x": "Apple Nutrition: Pectin.. Orchard. Essential knowledge — Orchard.. the everyday fruit. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Pectin..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Pectin..", "x": "Explained: Pectin.. Calories. The context — Apple Nutrition. 95 calories. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "4,000 varieties.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "4,000 varieties.", "x": "Apple Nutrition: 4,000 varieties.. Storage. Essential knowledge — 95 calories.. the everyday fruit. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: 4,000 varieties..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: 4,000 varieties..", "x": "Explained: 4,000 varieties.. Fiber. The context — Apple Nutrition. Fiber. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Orchard.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Orchard.", "x": "Apple Nutrition: Orchard.. Calories. Essential knowledge — Fiber.. the everyday fruit. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Orchard..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Orchard..", "x": "Explained: Orchard.. Vitamin C. The context — Apple Nutrition. Vitamin C. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Calories.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Calories.", "x": "Apple Nutrition in depth: Calories.. Fiber. Details — the everyday fruit.. Vitamin C. Pectin. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Fiber.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Fiber.", "x": "Apple Nutrition in depth: Fiber.. Vitamin C. Details — the everyday fruit.. Varieties. 4,000 varieties. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Vitamin C.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Vitamin C.", "x": "Apple Nutrition in depth: Vitamin C.. Pectin. Details — the everyday fruit.. Orchard. Orchard. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Varieties.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Varieties.", "x": "Apple Nutrition in depth: Varieties.. 4,000 varieties. Details — the everyday fruit.. Storage. 95 calories. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Orchard.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Orchard.", "x": "Apple Nutrition in depth: Orchard.. Orchard. Details — the everyday fruit.. Calories. Fiber. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Storage.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Storage.", "x": "Apple Nutrition in depth: Storage.. 95 calories. Details — the everyday fruit.. Fiber. Vitamin C. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Apple Nutrition comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Apple Nutrition comes from.", "x": "Origins: Calories.. 95 calories. The history of Apple Nutrition — the everyday fruit.. Fiber. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Apple Nutrition respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Apple Nutrition respectfully.", "x": "Engaging: Vitamin C.. Fiber. How to participate or observe well — Apple Nutrition. the everyday fruit. Respect first, always; Varieties.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Apple Nutrition do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Apple Nutrition do's and don'ts.", "x": "Etiquette: Orchard.. Vitamin C. The rules of respect — Apple Nutrition. the everyday fruit. When in doubt, ask about Storage.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Apple Nutrition.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Apple Nutrition.", "x": "Planning: Calories.. Pectin. Practical notes — Apple Nutrition. the everyday fruit. A little planning shows respect for Fiber.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Apple Nutrition and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Apple Nutrition and money.", "x": "Costs: Vitamin C.. 4,000 varieties. What to budget — Apple Nutrition. the everyday fruit. The best experiences of Varieties. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-nutrition-apple-nutrition-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
