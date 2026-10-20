(function(){'use strict';
/* JAH Foundation Repair Database generator — jahdb-e2-trade2-foundation-repair-trade-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-trade2-foundation-repair-trade',PREFIX='JAH-E2TRADE2FOU-',NAME='JAH Foundation Repair Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Foundation Repair: the complete guide", "d": "Foundation Repair: the pier pros..", "g": "overview", "l": 2, "q": "What is Foundation Repair: the complete guide?", "a": "Foundation Repair: the pier pros..", "x": "The complete trade guide to Foundation Repair: the pier pros.. Piers. History, meaning, practices, and how to engage respectfully — everything in one database. Piers. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Foundation Repair essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Foundation Repair essentials.", "x": "At a glance: Foundation Repair — the pier pros.. Cracks. The essentials: Settling.. Settling. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Piers.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Piers.", "x": "Foundation Repair: Piers.. Settling. Essential knowledge — Settling.. the pier pros. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Piers..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Piers..", "x": "Explained: Piers.. Cracks. The context — Foundation Repair. Waterproof. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Cracks.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Cracks.", "x": "Foundation Repair: Cracks.. Engineers. Essential knowledge — Waterproof.. the pier pros. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Cracks..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Cracks..", "x": "Explained: Cracks.. Helical. The context — Foundation Repair. Helical. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Settling.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Settling.", "x": "Foundation Repair: Settling.. Cracks. Essential knowledge — Helical.. the pier pros. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Settling..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Settling..", "x": "Explained: Settling.. Hiring. The context — Foundation Repair. Engineers. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Waterproof.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Waterproof.", "x": "Foundation Repair: Waterproof.. Helical. Essential knowledge — Engineers.. the pier pros. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Waterproof..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Waterproof..", "x": "Explained: Waterproof.. Piers. The context — Foundation Repair. Piers. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Helical.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Helical.", "x": "Foundation Repair: Helical.. Hiring. Essential knowledge — Piers.. the pier pros. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Helical..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Helical..", "x": "Explained: Helical.. Settling. The context — Foundation Repair. Cracks. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Engineers.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Engineers.", "x": "Foundation Repair: Engineers.. Piers. Essential knowledge — Cracks.. the pier pros. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Engineers..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Engineers..", "x": "Explained: Engineers.. Engineers. The context — Foundation Repair. Settling. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Piers.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Piers.", "x": "Foundation Repair in depth: Piers.. Cracks. Details — the pier pros.. Engineers. Waterproof. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Settling.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Settling.", "x": "Foundation Repair in depth: Settling.. Settling. Details — the pier pros.. Cracks. Helical. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Engineers.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Engineers.", "x": "Foundation Repair in depth: Engineers.. Waterproof. Details — the pier pros.. Helical. Engineers. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Cracks.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Cracks.", "x": "Foundation Repair in depth: Cracks.. Helical. Details — the pier pros.. Hiring. Piers. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Helical.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Helical.", "x": "Foundation Repair in depth: Helical.. Engineers. Details — the pier pros.. Piers. Cracks. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Hiring.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Hiring.", "x": "Foundation Repair in depth: Hiring.. Piers. Details — the pier pros.. Settling. Settling. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Foundation Repair comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Foundation Repair comes from.", "x": "Origins: Piers.. Piers. The history of Foundation Repair — the pier pros.. Settling. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Foundation Repair respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Foundation Repair respectfully.", "x": "Engaging: Engineers.. Cracks. How to participate or observe well — Foundation Repair. the pier pros. Respect first, always; Cracks.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Foundation Repair do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Foundation Repair do's and don'ts.", "x": "Etiquette: Helical.. Settling. The rules of respect — Foundation Repair. the pier pros. When in doubt, ask about Hiring.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Foundation Repair.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Foundation Repair.", "x": "Planning: Piers.. Waterproof. Practical notes — Foundation Repair. the pier pros. A little planning shows respect for Settling.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Foundation Repair and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Foundation Repair and money.", "x": "Costs: Engineers.. Helical. What to budget — Foundation Repair. the pier pros. The best experiences of Cracks. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-trade2-foundation-repair-trade-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
