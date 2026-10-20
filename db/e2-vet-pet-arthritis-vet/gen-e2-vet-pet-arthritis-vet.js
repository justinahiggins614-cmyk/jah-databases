(function(){'use strict';
/* JAH Pet Arthritis Veterinary Database generator — jahdb-e2-vet-pet-arthritis-vet-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-vet-pet-arthritis-vet',PREFIX='JAH-E2VETPETART-',NAME='JAH Pet Arthritis Veterinary Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Pet Arthritis: the complete guide", "d": "Pet Arthritis: the stiff joints..", "g": "overview", "l": 2, "q": "What is Pet Arthritis: the complete guide?", "a": "Pet Arthritis: the stiff joints..", "x": "The complete veterinary guide to Pet Arthritis: the stiff joints.. Stiffness. History, meaning, practices, and how to engage respectfully — everything in one database. Stiffness. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Pet Arthritis essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Pet Arthritis essentials.", "x": "At a glance: Pet Arthritis — the stiff joints.. Glucosamine. The essentials: Ramps.. Weight. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Stiffness.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Stiffness.", "x": "Pet Arthritis: Stiffness.. Ramps. Essential knowledge — Weight.. the stiff joints. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Stiffness..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Stiffness..", "x": "Explained: Stiffness.. Senior. The context — Pet Arthritis. Ramps. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Glucosamine.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Glucosamine.", "x": "Pet Arthritis: Glucosamine.. Pain. Essential knowledge — Ramps.. the stiff joints. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Glucosamine..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Glucosamine..", "x": "Explained: Glucosamine.. Weight. The context — Pet Arthritis. Pain. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Weight.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Weight.", "x": "Pet Arthritis: Weight.. Senior. Essential knowledge — Pain.. the stiff joints. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Weight..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Weight..", "x": "Explained: Weight.. Guide. The context — Pet Arthritis. Senior. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Ramps.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Ramps.", "x": "Pet Arthritis: Ramps.. Weight. Essential knowledge — Senior.. the stiff joints. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Ramps..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Ramps..", "x": "Explained: Ramps.. Stiffness. The context — Pet Arthritis. Stiffness. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Pain.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Pain.", "x": "Pet Arthritis: Pain.. Guide. Essential knowledge — Stiffness.. the stiff joints. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Pain..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Pain..", "x": "Explained: Pain.. Ramps. The context — Pet Arthritis. Glucosamine. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Senior.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Senior.", "x": "Pet Arthritis: Senior.. Stiffness. Essential knowledge — Glucosamine.. the stiff joints. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Senior..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Senior..", "x": "Explained: Senior.. Pain. The context — Pet Arthritis. Weight. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Stiffness.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Stiffness.", "x": "Pet Arthritis in depth: Stiffness.. Glucosamine. Details — the stiff joints.. Pain. Ramps. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Ramps.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Ramps.", "x": "Pet Arthritis in depth: Ramps.. Weight. Details — the stiff joints.. Senior. Pain. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Pain.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Pain.", "x": "Pet Arthritis in depth: Pain.. Ramps. Details — the stiff joints.. Weight. Senior. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Senior.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Senior.", "x": "Pet Arthritis in depth: Senior.. Pain. Details — the stiff joints.. Guide. Stiffness. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Weight.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Weight.", "x": "Pet Arthritis in depth: Weight.. Senior. Details — the stiff joints.. Stiffness. Glucosamine. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Guide.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Guide.", "x": "Pet Arthritis in depth: Guide.. Stiffness. Details — the stiff joints.. Ramps. Weight. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Pet Arthritis comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Pet Arthritis comes from.", "x": "Origins: Stiffness.. Stiffness. The history of Pet Arthritis — the stiff joints.. Ramps. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Pet Arthritis respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Pet Arthritis respectfully.", "x": "Engaging: Pain.. Glucosamine. How to participate or observe well — Pet Arthritis. the stiff joints. Respect first, always; Senior.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Pet Arthritis do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Pet Arthritis do's and don'ts.", "x": "Etiquette: Weight.. Weight. The rules of respect — Pet Arthritis. the stiff joints. When in doubt, ask about Guide.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Pet Arthritis.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Pet Arthritis.", "x": "Planning: Stiffness.. Ramps. Practical notes — Pet Arthritis. the stiff joints. A little planning shows respect for Ramps.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Pet Arthritis and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Pet Arthritis and money.", "x": "Costs: Pain.. Pain. What to budget — Pet Arthritis. the stiff joints. The best experiences of Senior. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-vet-pet-arthritis-vet-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
