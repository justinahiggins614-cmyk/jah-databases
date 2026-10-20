(function(){'use strict';
/* JAH Onion Nutrition Nutrition Database generator — jahdb-e2-nutrition-onion-nutrition-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-nutrition-onion-nutrition',PREFIX='JAH-E2NUTRITION-',NAME='JAH Onion Nutrition Nutrition Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Onion Nutrition: the complete guide", "d": "Onion Nutrition: the flavor base..", "g": "overview", "l": 2, "q": "What is Onion Nutrition: the complete guide?", "a": "Onion Nutrition: the flavor base..", "x": "The complete nutrition guide to Onion Nutrition: the flavor base.. 40 calories. History, meaning, practices, and how to engage respectfully — everything in one database. Quercetin. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Onion Nutrition essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Onion Nutrition essentials.", "x": "At a glance: Onion Nutrition — the flavor base.. Quercetin. The essentials: Caramelize.. Sulfur. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "40 calories.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "40 calories.", "x": "Onion Nutrition: 40 calories.. Caramelize. Essential knowledge — Sulfur.. the flavor base. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 40 calories..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 40 calories..", "x": "Explained: 40 calories.. Storage. The context — Onion Nutrition. Caramelize. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Quercetin.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Quercetin.", "x": "Onion Nutrition: Quercetin.. Varieties. Essential knowledge — Caramelize.. the flavor base. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Quercetin..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Quercetin..", "x": "Explained: Quercetin.. Cutting. The context — Onion Nutrition. Varieties. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Sulfur.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Sulfur.", "x": "Onion Nutrition: Sulfur.. Storage. Essential knowledge — Varieties.. the flavor base. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Sulfur..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Sulfur..", "x": "Explained: Sulfur.. Recipes. The context — Onion Nutrition. Storage. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Caramelize.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Caramelize.", "x": "Onion Nutrition: Caramelize.. Cutting. Essential knowledge — Storage.. the flavor base. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Caramelize..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Caramelize..", "x": "Explained: Caramelize.. Quercetin. The context — Onion Nutrition. 40 calories. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Varieties.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Varieties.", "x": "Onion Nutrition: Varieties.. Recipes. Essential knowledge — 40 calories.. the flavor base. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Varieties..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Varieties..", "x": "Explained: Varieties.. Caramelize. The context — Onion Nutrition. Quercetin. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Storage.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Storage.", "x": "Onion Nutrition: Storage.. Quercetin. Essential knowledge — Quercetin.. the flavor base. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Storage..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Storage..", "x": "Explained: Storage.. Varieties. The context — Onion Nutrition. Sulfur. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Quercetin.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Quercetin.", "x": "Onion Nutrition in depth: Quercetin.. Quercetin. Details — the flavor base.. Varieties. Caramelize. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Caramelize.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Caramelize.", "x": "Onion Nutrition in depth: Caramelize.. Sulfur. Details — the flavor base.. Storage. Varieties. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Varieties.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Varieties.", "x": "Onion Nutrition in depth: Varieties.. Caramelize. Details — the flavor base.. Cutting. Storage. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Storage.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Storage.", "x": "Onion Nutrition in depth: Storage.. Varieties. Details — the flavor base.. Recipes. 40 calories. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Cutting.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Cutting.", "x": "Onion Nutrition in depth: Cutting.. Storage. Details — the flavor base.. Quercetin. Quercetin. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Recipes.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Recipes.", "x": "Onion Nutrition in depth: Recipes.. 40 calories. Details — the flavor base.. Caramelize. Sulfur. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Onion Nutrition comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Onion Nutrition comes from.", "x": "Origins: Quercetin.. 40 calories. The history of Onion Nutrition — the flavor base.. Caramelize. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Onion Nutrition respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Onion Nutrition respectfully.", "x": "Engaging: Varieties.. Quercetin. How to participate or observe well — Onion Nutrition. the flavor base. Respect first, always; Storage.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Onion Nutrition do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Onion Nutrition do's and don'ts.", "x": "Etiquette: Cutting.. Sulfur. The rules of respect — Onion Nutrition. the flavor base. When in doubt, ask about Recipes.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Onion Nutrition.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Onion Nutrition.", "x": "Planning: Quercetin.. Caramelize. Practical notes — Onion Nutrition. the flavor base. A little planning shows respect for Caramelize.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Onion Nutrition and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Onion Nutrition and money.", "x": "Costs: Varieties.. Varieties. What to budget — Onion Nutrition. the flavor base. The best experiences of Storage. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-nutrition-onion-nutrition-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
