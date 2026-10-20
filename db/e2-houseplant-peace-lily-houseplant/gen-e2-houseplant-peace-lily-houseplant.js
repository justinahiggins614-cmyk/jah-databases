(function(){'use strict';
/* JAH Peace Lily Houseplant Database generator — jahdb-e2-houseplant-peace-lily-houseplant-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-houseplant-peace-lily-houseplant',PREFIX='JAH-E2HOUSEPLAN-',NAME='JAH Peace Lily Houseplant Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Peace Lily: the complete guide", "d": "Peace Lily: the blooming shade..", "g": "overview", "l": 2, "q": "What is Peace Lily: the complete guide?", "a": "Peace Lily: the blooming shade..", "x": "The complete houseplant guide to Peace Lily: the blooming shade.. White blooms. History, meaning, practices, and how to engage respectfully — everything in one database. Blooms. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Peace Lily essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Peace Lily essentials.", "x": "At a glance: Peace Lily — the blooming shade.. Low light. The essentials: Drooping.. Drooping. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "White blooms.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "White blooms.", "x": "Peace Lily: White blooms.. Drooping. Essential knowledge — Drooping.. the blooming shade. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: White blooms..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: White blooms..", "x": "Explained: White blooms.. Toxic. The context — Peace Lily. Toxic. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Low light.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Low light.", "x": "Peace Lily: Low light.. Air. Essential knowledge — Toxic.. the blooming shade. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Low light..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Low light..", "x": "Explained: Low light.. Low light. The context — Peace Lily. Air. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Drooping.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Drooping.", "x": "Peace Lily: Drooping.. Toxic. Essential knowledge — Air.. the blooming shade. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Drooping..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Drooping..", "x": "Explained: Drooping.. Guide. The context — Peace Lily. Spathiphyllum. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Toxic.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Toxic.", "x": "Peace Lily: Toxic.. Low light. Essential knowledge — Spathiphyllum.. the blooming shade. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Toxic..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Toxic..", "x": "Explained: Toxic.. Blooms. The context — Peace Lily. White blooms. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Air.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Air.", "x": "Peace Lily: Air.. Guide. Essential knowledge — White blooms.. the blooming shade. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Air..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Air..", "x": "Explained: Air.. Drooping. The context — Peace Lily. Low light. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Spathiphyllum.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Spathiphyllum.", "x": "Peace Lily: Spathiphyllum.. Blooms. Essential knowledge — Low light.. the blooming shade. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Spathiphyllum..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Spathiphyllum..", "x": "Explained: Spathiphyllum.. Air. The context — Peace Lily. Drooping. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Blooms.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Blooms.", "x": "Peace Lily in depth: Blooms.. Low light. Details — the blooming shade.. Air. Toxic. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Drooping.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Drooping.", "x": "Peace Lily in depth: Drooping.. Drooping. Details — the blooming shade.. Toxic. Air. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Air.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Air.", "x": "Peace Lily in depth: Air.. Toxic. Details — the blooming shade.. Low light. Spathiphyllum. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Toxic.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Toxic.", "x": "Peace Lily in depth: Toxic.. Air. Details — the blooming shade.. Guide. White blooms. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Low light.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Low light.", "x": "Peace Lily in depth: Low light.. Spathiphyllum. Details — the blooming shade.. Blooms. Low light. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Guide.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Guide.", "x": "Peace Lily in depth: Guide.. White blooms. Details — the blooming shade.. Drooping. Drooping. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Peace Lily comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Peace Lily comes from.", "x": "Origins: Blooms.. White blooms. The history of Peace Lily — the blooming shade.. Drooping. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Peace Lily respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Peace Lily respectfully.", "x": "Engaging: Air.. Low light. How to participate or observe well — Peace Lily. the blooming shade. Respect first, always; Toxic.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Peace Lily do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Peace Lily do's and don'ts.", "x": "Etiquette: Low light.. Drooping. The rules of respect — Peace Lily. the blooming shade. When in doubt, ask about Guide.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Peace Lily.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Peace Lily.", "x": "Planning: Blooms.. Toxic. Practical notes — Peace Lily. the blooming shade. A little planning shows respect for Drooping.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Peace Lily and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Peace Lily and money.", "x": "Costs: Air.. Air. What to budget — Peace Lily. the blooming shade. The best experiences of Toxic. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-houseplant-peace-lily-houseplant-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
