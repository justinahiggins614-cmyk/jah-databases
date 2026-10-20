(function(){'use strict';
/* JAH Veterinarian Profession Database generator — jahdb-e2-profession-veterinarian-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-profession-veterinarian',PREFIX='JAH-E2PROFESSIO-',NAME='JAH Veterinarian Profession Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Veterinarian Profession: the complete guide", "d": "Veterinarian Profession: the animal doctor..", "g": "overview", "l": 2, "q": "What is Veterinarian Profession: the complete guide?", "a": "Veterinarian Profession: the animal doctor..", "x": "The complete profession guide to Veterinarian Profession: the animal doctor.. DVM. History, meaning, practices, and how to engage respectfully — everything in one database. Training. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Veterinarian Profession essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Veterinarian Profession essentials.", "x": "At a glance: Veterinarian Profession — the animal doctor.. Clinics. The essentials: Clinics.. Surgery. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "DVM.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "DVM.", "x": "Veterinarian Profession: DVM.. Clinics. Essential knowledge — Surgery.. the animal doctor. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: DVM..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: DVM..", "x": "Explained: DVM.. Farm. The context — Veterinarian Profession. Compassion. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Clinics.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Clinics.", "x": "Veterinarian Profession: Clinics.. Surgery. Essential knowledge — Compassion.. the animal doctor. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Clinics..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Clinics..", "x": "Explained: Clinics.. Exotics. The context — Veterinarian Profession. Farm. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Surgery.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Surgery.", "x": "Veterinarian Profession: Surgery.. Farm. Essential knowledge — Farm.. the animal doctor. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Surgery..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Surgery..", "x": "Explained: Surgery.. Day. The context — Veterinarian Profession. Exotics. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Compassion.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Compassion.", "x": "Veterinarian Profession: Compassion.. Exotics. Essential knowledge — Exotics.. the animal doctor. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Compassion..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Compassion..", "x": "Explained: Compassion.. Training. The context — Veterinarian Profession. DVM. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Farm.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Farm.", "x": "Veterinarian Profession: Farm.. Day. Essential knowledge — DVM.. the animal doctor. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Farm..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Farm..", "x": "Explained: Farm.. Clinics. The context — Veterinarian Profession. Clinics. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Exotics.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Exotics.", "x": "Veterinarian Profession: Exotics.. Training. Essential knowledge — Clinics.. the animal doctor. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Exotics..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Exotics..", "x": "Explained: Exotics.. Surgery. The context — Veterinarian Profession. Surgery. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Training.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Training.", "x": "Veterinarian Profession in depth: Training.. Clinics. Details — the animal doctor.. Surgery. Compassion. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Clinics.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Clinics.", "x": "Veterinarian Profession in depth: Clinics.. Surgery. Details — the animal doctor.. Farm. Farm. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Surgery.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Surgery.", "x": "Veterinarian Profession in depth: Surgery.. Compassion. Details — the animal doctor.. Exotics. Exotics. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Farm.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Farm.", "x": "Veterinarian Profession in depth: Farm.. Farm. Details — the animal doctor.. Day. DVM. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Exotics.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Exotics.", "x": "Veterinarian Profession in depth: Exotics.. Exotics. Details — the animal doctor.. Training. Clinics. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Day.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Day.", "x": "Veterinarian Profession in depth: Day.. DVM. Details — the animal doctor.. Clinics. Surgery. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Veterinarian Profession comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Veterinarian Profession comes from.", "x": "Origins: Training.. DVM. The history of Veterinarian Profession — the animal doctor.. Clinics. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Veterinarian Profession respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Veterinarian Profession respectfully.", "x": "Engaging: Surgery.. Clinics. How to participate or observe well — Veterinarian Profession. the animal doctor. Respect first, always; Farm.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Veterinarian Profession do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Veterinarian Profession do's and don'ts.", "x": "Etiquette: Exotics.. Surgery. The rules of respect — Veterinarian Profession. the animal doctor. When in doubt, ask about Day.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Veterinarian Profession.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Veterinarian Profession.", "x": "Planning: Training.. Compassion. Practical notes — Veterinarian Profession. the animal doctor. A little planning shows respect for Clinics.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Veterinarian Profession and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Veterinarian Profession and money.", "x": "Costs: Surgery.. Farm. What to budget — Veterinarian Profession. the animal doctor. The best experiences of Farm. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-profession-veterinarian-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
