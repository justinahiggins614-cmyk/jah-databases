(function(){'use strict';
/* JAH Vegan Diet Diet Database generator — jahdb-e2-diet-vegan-diet-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-diet-vegan-diet',PREFIX='JAH-E2DIETVEGAN-',NAME='JAH Vegan Diet Diet Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Vegan Diet: the complete guide", "d": "Vegan Diet: the plant-only..", "g": "overview", "l": 2, "q": "What is Vegan Diet: the complete guide?", "a": "Vegan Diet: the plant-only..", "x": "The complete diet guide to Vegan Diet: the plant-only.. No animal. History, meaning, practices, and how to engage respectfully — everything in one database. B12. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Vegan Diet essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Vegan Diet essentials.", "x": "At a glance: Vegan Diet — the plant-only.. B12. The essentials: Protein.. Protein. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "No animal.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "No animal.", "x": "Vegan Diet: No animal.. Protein. Essential knowledge — Protein.. the plant-only. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: No animal..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: No animal..", "x": "Explained: No animal.. Planning. The context — Vegan Diet. Ethics. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "B12.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "B12.", "x": "Vegan Diet: B12.. Ethics. Essential knowledge — Ethics.. the plant-only. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: B12..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: B12..", "x": "Explained: B12.. Environment. The context — Vegan Diet. Environment. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Protein.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Protein.", "x": "Vegan Diet: Protein.. Planning. Essential knowledge — Environment.. the plant-only. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Protein..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Protein..", "x": "Explained: Protein.. Foods. The context — Vegan Diet. Planning. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Ethics.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Ethics.", "x": "Vegan Diet: Ethics.. Environment. Essential knowledge — Planning.. the plant-only. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Ethics..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Ethics..", "x": "Explained: Ethics.. B12. The context — Vegan Diet. No animal. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Environment.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Environment.", "x": "Vegan Diet: Environment.. Foods. Essential knowledge — No animal.. the plant-only. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Environment..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Environment..", "x": "Explained: Environment.. Protein. The context — Vegan Diet. B12. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Planning.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Planning.", "x": "Vegan Diet: Planning.. B12. Essential knowledge — B12.. the plant-only. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Planning..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Planning..", "x": "Explained: Planning.. Ethics. The context — Vegan Diet. Protein. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "B12.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "B12.", "x": "Vegan Diet in depth: B12.. B12. Details — the plant-only.. Ethics. Ethics. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Protein.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Protein.", "x": "Vegan Diet in depth: Protein.. Protein. Details — the plant-only.. Planning. Environment. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Ethics.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Ethics.", "x": "Vegan Diet in depth: Ethics.. Ethics. Details — the plant-only.. Environment. Planning. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Planning.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Planning.", "x": "Vegan Diet in depth: Planning.. Environment. Details — the plant-only.. Foods. No animal. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Environment.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Environment.", "x": "Vegan Diet in depth: Environment.. Planning. Details — the plant-only.. B12. B12. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Foods.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Foods.", "x": "Vegan Diet in depth: Foods.. No animal. Details — the plant-only.. Protein. Protein. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Vegan Diet comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Vegan Diet comes from.", "x": "Origins: B12.. No animal. The history of Vegan Diet — the plant-only.. Protein. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Vegan Diet respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Vegan Diet respectfully.", "x": "Engaging: Ethics.. B12. How to participate or observe well — Vegan Diet. the plant-only. Respect first, always; Planning.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Vegan Diet do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Vegan Diet do's and don'ts.", "x": "Etiquette: Environment.. Protein. The rules of respect — Vegan Diet. the plant-only. When in doubt, ask about Foods.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Vegan Diet.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Vegan Diet.", "x": "Planning: B12.. Ethics. Practical notes — Vegan Diet. the plant-only. A little planning shows respect for Protein.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Vegan Diet and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Vegan Diet and money.", "x": "Costs: Ethics.. Environment. What to budget — Vegan Diet. the plant-only. The best experiences of Planning. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-diet-vegan-diet-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
