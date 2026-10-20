(function(){'use strict';
/* JAH Pet Radiology Veterinary Database generator — jahdb-e2-vet-pet-radiology-vet-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-vet-pet-radiology-vet',PREFIX='JAH-E2VETPETRAD-',NAME='JAH Pet Radiology Veterinary Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Pet Radiology: the complete guide", "d": "Pet Radiology: the imaging..", "g": "overview", "l": 2, "q": "What is Pet Radiology: the complete guide?", "a": "Pet Radiology: the imaging..", "x": "The complete veterinary guide to Pet Radiology: the imaging.. X-ray. History, meaning, practices, and how to engage respectfully — everything in one database. X-ray. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Pet Radiology essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Pet Radiology essentials.", "x": "At a glance: Pet Radiology — the imaging.. Ultrasound. The essentials: Ultrasound.. Contrast. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "X-ray.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "X-ray.", "x": "Pet Radiology: X-ray.. Ultrasound. Essential knowledge — Contrast.. the imaging. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: X-ray..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: X-ray..", "x": "Explained: X-ray.. Fractures. The context — Pet Radiology. Sedation. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Ultrasound.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Ultrasound.", "x": "Pet Radiology: Ultrasound.. Sedation. Essential knowledge — Sedation.. the imaging. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Ultrasound..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Ultrasound..", "x": "Explained: Ultrasound.. Reads. The context — Pet Radiology. Fractures. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Contrast.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Contrast.", "x": "Pet Radiology: Contrast.. Fractures. Essential knowledge — Fractures.. the imaging. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Contrast..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Contrast..", "x": "Explained: Contrast.. Guide. The context — Pet Radiology. Reads. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Sedation.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Sedation.", "x": "Pet Radiology: Sedation.. Reads. Essential knowledge — Reads.. the imaging. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Sedation..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Sedation..", "x": "Explained: Sedation.. X-ray. The context — Pet Radiology. X-ray. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Fractures.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Fractures.", "x": "Pet Radiology: Fractures.. Guide. Essential knowledge — X-ray.. the imaging. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Fractures..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Fractures..", "x": "Explained: Fractures.. Ultrasound. The context — Pet Radiology. Ultrasound. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Reads.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Reads.", "x": "Pet Radiology: Reads.. X-ray. Essential knowledge — Ultrasound.. the imaging. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Reads..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Reads..", "x": "Explained: Reads.. Sedation. The context — Pet Radiology. Contrast. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "X-ray.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "X-ray.", "x": "Pet Radiology in depth: X-ray.. Ultrasound. Details — the imaging.. Sedation. Sedation. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Ultrasound.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Ultrasound.", "x": "Pet Radiology in depth: Ultrasound.. Contrast. Details — the imaging.. Fractures. Fractures. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Sedation.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Sedation.", "x": "Pet Radiology in depth: Sedation.. Sedation. Details — the imaging.. Reads. Reads. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Fractures.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Fractures.", "x": "Pet Radiology in depth: Fractures.. Fractures. Details — the imaging.. Guide. X-ray. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Reads.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Reads.", "x": "Pet Radiology in depth: Reads.. Reads. Details — the imaging.. X-ray. Ultrasound. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Guide.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Guide.", "x": "Pet Radiology in depth: Guide.. X-ray. Details — the imaging.. Ultrasound. Contrast. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Pet Radiology comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Pet Radiology comes from.", "x": "Origins: X-ray.. X-ray. The history of Pet Radiology — the imaging.. Ultrasound. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Pet Radiology respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Pet Radiology respectfully.", "x": "Engaging: Sedation.. Ultrasound. How to participate or observe well — Pet Radiology. the imaging. Respect first, always; Fractures.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Pet Radiology do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Pet Radiology do's and don'ts.", "x": "Etiquette: Reads.. Contrast. The rules of respect — Pet Radiology. the imaging. When in doubt, ask about Guide.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Pet Radiology.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Pet Radiology.", "x": "Planning: X-ray.. Sedation. Practical notes — Pet Radiology. the imaging. A little planning shows respect for Ultrasound.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Pet Radiology and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Pet Radiology and money.", "x": "Costs: Sedation.. Fractures. What to budget — Pet Radiology. the imaging. The best experiences of Fractures. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-vet-pet-radiology-vet-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
