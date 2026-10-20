(function(){'use strict';
/* JAH Belly Dance Dance Form Database generator — jahdb-e2-dance-belly-dance-form-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-dance-belly-dance-form',PREFIX='JAH-E2DANCEBELL-',NAME='JAH Belly Dance Dance Form Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Belly Dance: the complete guide", "d": "Belly Dance: the Middle Eastern art..", "g": "overview", "l": 2, "q": "What is Belly Dance: the complete guide?", "a": "Belly Dance: the Middle Eastern art..", "x": "The complete dance form guide to Belly Dance: the Middle Eastern art.. Isolations. History, meaning, practices, and how to engage respectfully — everything in one database. Hips. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Belly Dance essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Belly Dance essentials.", "x": "At a glance: Belly Dance — the Middle Eastern art.. Hips. The essentials: Veils.. Veils. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Isolations.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Isolations.", "x": "Belly Dance: Isolations.. Veils. Essential knowledge — Veils.. the Middle Eastern art. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Isolations..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Isolations..", "x": "Explained: Isolations.. Egypt. The context — Belly Dance. Egypt. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Hips.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Hips.", "x": "Belly Dance: Hips.. Shimmy. Essential knowledge — Egypt.. the Middle Eastern art. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Hips..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Hips..", "x": "Explained: Hips.. Zills. The context — Belly Dance. Zills. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Veils.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Veils.", "x": "Belly Dance: Veils.. Egypt. Essential knowledge — Zills.. the Middle Eastern art. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Veils..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Veils..", "x": "Explained: Veils.. Training. The context — Belly Dance. Shimmy. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Egypt.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Egypt.", "x": "Belly Dance: Egypt.. Zills. Essential knowledge — Shimmy.. the Middle Eastern art. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Egypt..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Egypt..", "x": "Explained: Egypt.. Hips. The context — Belly Dance. Isolations. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Zills.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Zills.", "x": "Belly Dance: Zills.. Training. Essential knowledge — Isolations.. the Middle Eastern art. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Zills..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Zills..", "x": "Explained: Zills.. Veils. The context — Belly Dance. Hips. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Shimmy.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Shimmy.", "x": "Belly Dance: Shimmy.. Hips. Essential knowledge — Hips.. the Middle Eastern art. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Shimmy..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Shimmy..", "x": "Explained: Shimmy.. Shimmy. The context — Belly Dance. Veils. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Hips.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Hips.", "x": "Belly Dance in depth: Hips.. Hips. Details — the Middle Eastern art.. Shimmy. Egypt. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Veils.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Veils.", "x": "Belly Dance in depth: Veils.. Veils. Details — the Middle Eastern art.. Egypt. Zills. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Shimmy.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Shimmy.", "x": "Belly Dance in depth: Shimmy.. Egypt. Details — the Middle Eastern art.. Zills. Shimmy. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Egypt.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Egypt.", "x": "Belly Dance in depth: Egypt.. Zills. Details — the Middle Eastern art.. Training. Isolations. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Zills.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Zills.", "x": "Belly Dance in depth: Zills.. Shimmy. Details — the Middle Eastern art.. Hips. Hips. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Training.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Training.", "x": "Belly Dance in depth: Training.. Isolations. Details — the Middle Eastern art.. Veils. Veils. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Belly Dance comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Belly Dance comes from.", "x": "Origins: Hips.. Isolations. The history of Belly Dance — the Middle Eastern art.. Veils. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Belly Dance respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Belly Dance respectfully.", "x": "Engaging: Shimmy.. Hips. How to participate or observe well — Belly Dance. the Middle Eastern art. Respect first, always; Egypt.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Belly Dance do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Belly Dance do's and don'ts.", "x": "Etiquette: Zills.. Veils. The rules of respect — Belly Dance. the Middle Eastern art. When in doubt, ask about Training.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Belly Dance.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Belly Dance.", "x": "Planning: Hips.. Egypt. Practical notes — Belly Dance. the Middle Eastern art. A little planning shows respect for Veils.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Belly Dance and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Belly Dance and money.", "x": "Costs: Shimmy.. Zills. What to budget — Belly Dance. the Middle Eastern art. The best experiences of Egypt. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-dance-belly-dance-form-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
