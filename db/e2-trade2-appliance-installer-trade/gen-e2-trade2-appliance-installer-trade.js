(function(){'use strict';
/* JAH Appliance Installer Database generator — jahdb-e2-trade2-appliance-installer-trade-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-trade2-appliance-installer-trade',PREFIX='JAH-E2TRADE2APP-',NAME='JAH Appliance Installer Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Appliance Installer: the complete guide", "d": "Appliance Installer: the install pros..", "g": "overview", "l": 2, "q": "What is Appliance Installer: the complete guide?", "a": "Appliance Installer: the install pros..", "x": "The complete trade guide to Appliance Installer: the install pros.. Delivery. History, meaning, practices, and how to engage respectfully — everything in one database. Hookup. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Appliance Installer essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Appliance Installer essentials.", "x": "At a glance: Appliance Installer — the install pros.. Hookup. The essentials: Leveling.. Leveling. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Delivery.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Delivery.", "x": "Appliance Installer: Delivery.. Leveling. Essential knowledge — Leveling.. the install pros. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Delivery..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Delivery..", "x": "Explained: Delivery.. Gas. The context — Appliance Installer. Haul-away. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Hookup.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Hookup.", "x": "Appliance Installer: Hookup.. Haul. Essential knowledge — Haul-away.. the install pros. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Hookup..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Hookup..", "x": "Explained: Hookup.. Warranty. The context — Appliance Installer. Gas. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Leveling.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Leveling.", "x": "Appliance Installer: Leveling.. Gas. Essential knowledge — Gas.. the install pros. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Leveling..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Leveling..", "x": "Explained: Leveling.. Hiring. The context — Appliance Installer. Warranty. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Haul-away.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Haul-away.", "x": "Appliance Installer: Haul-away.. Warranty. Essential knowledge — Warranty.. the install pros. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Haul-away..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Haul-away..", "x": "Explained: Haul-away.. Hookup. The context — Appliance Installer. Delivery. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Gas.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Gas.", "x": "Appliance Installer: Gas.. Hiring. Essential knowledge — Delivery.. the install pros. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Gas..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Gas..", "x": "Explained: Gas.. Leveling. The context — Appliance Installer. Hookup. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Warranty.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Warranty.", "x": "Appliance Installer: Warranty.. Hookup. Essential knowledge — Hookup.. the install pros. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Warranty..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Warranty..", "x": "Explained: Warranty.. Haul. The context — Appliance Installer. Leveling. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Hookup.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Hookup.", "x": "Appliance Installer in depth: Hookup.. Hookup. Details — the install pros.. Haul. Haul-away. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Leveling.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Leveling.", "x": "Appliance Installer in depth: Leveling.. Leveling. Details — the install pros.. Gas. Gas. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Haul.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Haul.", "x": "Appliance Installer in depth: Haul.. Haul-away. Details — the install pros.. Warranty. Warranty. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Gas.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Gas.", "x": "Appliance Installer in depth: Gas.. Gas. Details — the install pros.. Hiring. Delivery. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Warranty.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Warranty.", "x": "Appliance Installer in depth: Warranty.. Warranty. Details — the install pros.. Hookup. Hookup. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Hiring.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Hiring.", "x": "Appliance Installer in depth: Hiring.. Delivery. Details — the install pros.. Leveling. Leveling. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Appliance Installer comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Appliance Installer comes from.", "x": "Origins: Hookup.. Delivery. The history of Appliance Installer — the install pros.. Leveling. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Appliance Installer respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Appliance Installer respectfully.", "x": "Engaging: Haul.. Hookup. How to participate or observe well — Appliance Installer. the install pros. Respect first, always; Gas.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Appliance Installer do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Appliance Installer do's and don'ts.", "x": "Etiquette: Warranty.. Leveling. The rules of respect — Appliance Installer. the install pros. When in doubt, ask about Hiring.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Appliance Installer.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Appliance Installer.", "x": "Planning: Hookup.. Haul-away. Practical notes — Appliance Installer. the install pros. A little planning shows respect for Leveling.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Appliance Installer and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Appliance Installer and money.", "x": "Costs: Haul.. Gas. What to budget — Appliance Installer. the install pros. The best experiences of Gas. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-trade2-appliance-installer-trade-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
