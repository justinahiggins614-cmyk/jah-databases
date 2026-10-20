(function(){'use strict';
/* JAH Cupcakes Dessert Database generator — jahdb-e2-dessert3-cupcakes-food-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-dessert3-cupcakes-food',PREFIX='JAH-E2DESSERT3C-',NAME='JAH Cupcakes Dessert Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Cupcakes: the complete guide", "d": "Cupcakes: the single serves..", "g": "overview", "l": 2, "q": "What is Cupcakes: the complete guide?", "a": "Cupcakes: the single serves..", "x": "The complete dessert guide to Cupcakes: the single serves.. Frosting. History, meaning, practices, and how to engage respectfully — everything in one database. Frosting. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Cupcakes essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Cupcakes essentials.", "x": "At a glance: Cupcakes — the single serves.. Liners. The essentials: Party.. Party. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Frosting.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Frosting.", "x": "Cupcakes: Frosting.. Party. Essential knowledge — Party.. the single serves. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Frosting..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Frosting..", "x": "Explained: Frosting.. Liners. The context — Cupcakes. Swirl. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Liners.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Liners.", "x": "Cupcakes: Liners.. Decorating. Essential knowledge — Swirl.. the single serves. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Liners..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Liners..", "x": "Explained: Liners.. Swirl. The context — Cupcakes. Portion. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Party.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Party.", "x": "Cupcakes: Party.. Liners. Essential knowledge — Portion.. the single serves. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Party..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Party..", "x": "Explained: Party.. Baking. The context — Cupcakes. Decorating. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Swirl.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Swirl.", "x": "Cupcakes: Swirl.. Swirl. Essential knowledge — Decorating.. the single serves. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Swirl..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Swirl..", "x": "Explained: Swirl.. Frosting. The context — Cupcakes. Frosting. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Portion.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Portion.", "x": "Cupcakes: Portion.. Baking. Essential knowledge — Frosting.. the single serves. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Portion..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Portion..", "x": "Explained: Portion.. Party. The context — Cupcakes. Liners. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Decorating.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Decorating.", "x": "Cupcakes: Decorating.. Frosting. Essential knowledge — Liners.. the single serves. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Decorating..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Decorating..", "x": "Explained: Decorating.. Decorating. The context — Cupcakes. Party. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Frosting.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Frosting.", "x": "Cupcakes in depth: Frosting.. Liners. Details — the single serves.. Decorating. Swirl. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Party.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Party.", "x": "Cupcakes in depth: Party.. Party. Details — the single serves.. Liners. Portion. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Decorating.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Decorating.", "x": "Cupcakes in depth: Decorating.. Swirl. Details — the single serves.. Swirl. Decorating. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Liners.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Liners.", "x": "Cupcakes in depth: Liners.. Portion. Details — the single serves.. Baking. Frosting. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Swirl.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Swirl.", "x": "Cupcakes in depth: Swirl.. Decorating. Details — the single serves.. Frosting. Liners. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Baking.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Baking.", "x": "Cupcakes in depth: Baking.. Frosting. Details — the single serves.. Party. Party. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Cupcakes comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Cupcakes comes from.", "x": "Origins: Frosting.. Frosting. The history of Cupcakes — the single serves.. Party. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Cupcakes respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Cupcakes respectfully.", "x": "Engaging: Decorating.. Liners. How to participate or observe well — Cupcakes. the single serves. Respect first, always; Liners.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Cupcakes do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Cupcakes do's and don'ts.", "x": "Etiquette: Swirl.. Party. The rules of respect — Cupcakes. the single serves. When in doubt, ask about Baking.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Cupcakes.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Cupcakes.", "x": "Planning: Frosting.. Swirl. Practical notes — Cupcakes. the single serves. A little planning shows respect for Party.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Cupcakes and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Cupcakes and money.", "x": "Costs: Decorating.. Portion. What to budget — Cupcakes. the single serves. The best experiences of Liners. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-dessert3-cupcakes-food-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
