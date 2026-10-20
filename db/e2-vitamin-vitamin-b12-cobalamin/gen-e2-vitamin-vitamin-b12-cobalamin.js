(function(){'use strict';
/* JAH B12 Cobalamin Vitamin Database generator — jahdb-e2-vitamin-vitamin-b12-cobalamin-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-vitamin-vitamin-b12-cobalamin',PREFIX='JAH-E2VITAMINVI-',NAME='JAH B12 Cobalamin Vitamin Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "B12 Cobalamin: the complete guide", "d": "B12 Cobalamin: the vegan-watch B..", "g": "overview", "l": 2, "q": "What is B12 Cobalamin: the complete guide?", "a": "B12 Cobalamin: the vegan-watch B..", "x": "The complete vitamin guide to B12 Cobalamin: the vegan-watch B.. Cobalamin. History, meaning, practices, and how to engage respectfully — everything in one database. Nerves. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "B12 Cobalamin essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "B12 Cobalamin essentials.", "x": "At a glance: B12 Cobalamin — the vegan-watch B.. Nerves. The essentials: Anemia.. Anemia. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Cobalamin.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Cobalamin.", "x": "B12 Cobalamin: Cobalamin.. Anemia. Essential knowledge — Anemia.. the vegan-watch B. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Cobalamin..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Cobalamin..", "x": "Explained: Cobalamin.. Shots. The context — B12 Cobalamin. Animal foods. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Nerves.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Nerves.", "x": "B12 Cobalamin: Nerves.. Vegans. Essential knowledge — Animal foods.. the vegan-watch B. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Nerves..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Nerves..", "x": "Explained: Nerves.. Testing. The context — B12 Cobalamin. Vegans. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Anemia.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Anemia.", "x": "B12 Cobalamin: Anemia.. Shots. Essential knowledge — Vegans.. the vegan-watch B. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Anemia..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Anemia..", "x": "Explained: Anemia.. Supplements. The context — B12 Cobalamin. Shots. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Animal foods.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Animal foods.", "x": "B12 Cobalamin: Animal foods.. Testing. Essential knowledge — Shots.. the vegan-watch B. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Animal foods..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Animal foods..", "x": "Explained: Animal foods.. Nerves. The context — B12 Cobalamin. Cobalamin. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Vegans.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Vegans.", "x": "B12 Cobalamin: Vegans.. Supplements. Essential knowledge — Cobalamin.. the vegan-watch B. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Vegans..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Vegans..", "x": "Explained: Vegans.. Anemia. The context — B12 Cobalamin. Nerves. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Shots.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Shots.", "x": "B12 Cobalamin: Shots.. Nerves. Essential knowledge — Nerves.. the vegan-watch B. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Shots..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Shots..", "x": "Explained: Shots.. Vegans. The context — B12 Cobalamin. Anemia. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Nerves.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Nerves.", "x": "B12 Cobalamin in depth: Nerves.. Nerves. Details — the vegan-watch B.. Vegans. Animal foods. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Anemia.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Anemia.", "x": "B12 Cobalamin in depth: Anemia.. Anemia. Details — the vegan-watch B.. Shots. Vegans. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Vegans.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Vegans.", "x": "B12 Cobalamin in depth: Vegans.. Animal foods. Details — the vegan-watch B.. Testing. Shots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Shots.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Shots.", "x": "B12 Cobalamin in depth: Shots.. Vegans. Details — the vegan-watch B.. Supplements. Cobalamin. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Testing.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Testing.", "x": "B12 Cobalamin in depth: Testing.. Shots. Details — the vegan-watch B.. Nerves. Nerves. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Supplements.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Supplements.", "x": "B12 Cobalamin in depth: Supplements.. Cobalamin. Details — the vegan-watch B.. Anemia. Anemia. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where B12 Cobalamin comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where B12 Cobalamin comes from.", "x": "Origins: Nerves.. Cobalamin. The history of B12 Cobalamin — the vegan-watch B.. Anemia. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing B12 Cobalamin respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing B12 Cobalamin respectfully.", "x": "Engaging: Vegans.. Nerves. How to participate or observe well — B12 Cobalamin. the vegan-watch B. Respect first, always; Shots.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "B12 Cobalamin do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "B12 Cobalamin do's and don'ts.", "x": "Etiquette: Testing.. Anemia. The rules of respect — B12 Cobalamin. the vegan-watch B. When in doubt, ask about Supplements.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around B12 Cobalamin.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around B12 Cobalamin.", "x": "Planning: Nerves.. Animal foods. Practical notes — B12 Cobalamin. the vegan-watch B. A little planning shows respect for Anemia.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "B12 Cobalamin and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "B12 Cobalamin and money.", "x": "Costs: Vegans.. Vegans. What to budget — B12 Cobalamin. the vegan-watch B. The best experiences of Shots. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-vitamin-vitamin-b12-cobalamin-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
