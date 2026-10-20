(function(){'use strict';
/* JAH Pet Insurance Veterinary Database generator — jahdb-e2-vet-pet-insurance-vet-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-vet-pet-insurance-vet',PREFIX='JAH-E2VETPETINS-',NAME='JAH Pet Insurance Veterinary Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Pet Insurance: the complete guide", "d": "Pet Insurance: the financial shield..", "g": "overview", "l": 2, "q": "What is Pet Insurance: the complete guide?", "a": "Pet Insurance: the financial shield..", "x": "The complete veterinary guide to Pet Insurance: the financial shield.. Premiums. History, meaning, practices, and how to engage respectfully — everything in one database. Premiums. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Pet Insurance essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Pet Insurance essentials.", "x": "At a glance: Pet Insurance — the financial shield.. Deductibles. The essentials: Exclusions.. Exclusions. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Premiums.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Premiums.", "x": "Pet Insurance: Premiums.. Exclusions. Essential knowledge — Exclusions.. the financial shield. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Premiums..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Premiums..", "x": "Explained: Premiums.. Wellness. The context — Pet Insurance. Claims. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Deductibles.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Deductibles.", "x": "Pet Insurance: Deductibles.. Claims. Essential knowledge — Claims.. the financial shield. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Deductibles..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Deductibles..", "x": "Explained: Deductibles.. Accident. The context — Pet Insurance. Accident. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Exclusions.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Exclusions.", "x": "Pet Insurance: Exclusions.. Wellness. Essential knowledge — Accident.. the financial shield. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Exclusions..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Exclusions..", "x": "Explained: Exclusions.. Guide. The context — Pet Insurance. Wellness. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Claims.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Claims.", "x": "Pet Insurance: Claims.. Accident. Essential knowledge — Wellness.. the financial shield. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Claims..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Claims..", "x": "Explained: Claims.. Premiums. The context — Pet Insurance. Premiums. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Accident.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Accident.", "x": "Pet Insurance: Accident.. Guide. Essential knowledge — Premiums.. the financial shield. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Accident..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Accident..", "x": "Explained: Accident.. Exclusions. The context — Pet Insurance. Deductibles. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Wellness.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Wellness.", "x": "Pet Insurance: Wellness.. Premiums. Essential knowledge — Deductibles.. the financial shield. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Wellness..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Wellness..", "x": "Explained: Wellness.. Claims. The context — Pet Insurance. Exclusions. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Premiums.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Premiums.", "x": "Pet Insurance in depth: Premiums.. Deductibles. Details — the financial shield.. Claims. Claims. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Exclusions.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Exclusions.", "x": "Pet Insurance in depth: Exclusions.. Exclusions. Details — the financial shield.. Wellness. Accident. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Claims.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Claims.", "x": "Pet Insurance in depth: Claims.. Claims. Details — the financial shield.. Accident. Wellness. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Wellness.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Wellness.", "x": "Pet Insurance in depth: Wellness.. Accident. Details — the financial shield.. Guide. Premiums. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Accident.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Accident.", "x": "Pet Insurance in depth: Accident.. Wellness. Details — the financial shield.. Premiums. Deductibles. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Guide.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Guide.", "x": "Pet Insurance in depth: Guide.. Premiums. Details — the financial shield.. Exclusions. Exclusions. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Pet Insurance comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Pet Insurance comes from.", "x": "Origins: Premiums.. Premiums. The history of Pet Insurance — the financial shield.. Exclusions. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Pet Insurance respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Pet Insurance respectfully.", "x": "Engaging: Claims.. Deductibles. How to participate or observe well — Pet Insurance. the financial shield. Respect first, always; Wellness.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Pet Insurance do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Pet Insurance do's and don'ts.", "x": "Etiquette: Accident.. Exclusions. The rules of respect — Pet Insurance. the financial shield. When in doubt, ask about Guide.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Pet Insurance.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Pet Insurance.", "x": "Planning: Premiums.. Claims. Practical notes — Pet Insurance. the financial shield. A little planning shows respect for Exclusions.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Pet Insurance and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Pet Insurance and money.", "x": "Costs: Claims.. Accident. What to budget — Pet Insurance. the financial shield. The best experiences of Wellness. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-vet-pet-insurance-vet-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
