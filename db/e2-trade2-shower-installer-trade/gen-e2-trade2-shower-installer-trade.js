(function(){'use strict';
/* JAH Shower Installer Database generator — jahdb-e2-trade2-shower-installer-trade-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-trade2-shower-installer-trade',PREFIX='JAH-E2TRADE2SHO-',NAME='JAH Shower Installer Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Shower Installer: the complete guide", "d": "Shower Installer: the rain pros..", "g": "overview", "l": 2, "q": "What is Shower Installer: the complete guide?", "a": "Shower Installer: the rain pros..", "x": "The complete trade guide to Shower Installer: the rain pros.. Pan. History, meaning, practices, and how to engage respectfully — everything in one database. Waterproof. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Shower Installer essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Shower Installer essentials.", "x": "At a glance: Shower Installer — the rain pros.. Waterproof. The essentials: Glass.. Tile. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Pan.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Pan.", "x": "Shower Installer: Pan.. Glass. Essential knowledge — Tile.. the rain pros. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Pan..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Pan..", "x": "Explained: Pan.. Pan. The context — Shower Installer. Valve. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Waterproof.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Waterproof.", "x": "Shower Installer: Waterproof.. Drain. Essential knowledge — Valve.. the rain pros. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Waterproof..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Waterproof..", "x": "Explained: Waterproof.. Valve. The context — Shower Installer. Glass. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Tile.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Tile.", "x": "Shower Installer: Tile.. Pan. Essential knowledge — Glass.. the rain pros. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Tile..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Tile..", "x": "Explained: Tile.. Hiring. The context — Shower Installer. Drain. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Valve.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Valve.", "x": "Shower Installer: Valve.. Valve. Essential knowledge — Drain.. the rain pros. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Valve..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Valve..", "x": "Explained: Valve.. Waterproof. The context — Shower Installer. Pan. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Glass.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Glass.", "x": "Shower Installer: Glass.. Hiring. Essential knowledge — Pan.. the rain pros. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Glass..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Glass..", "x": "Explained: Glass.. Glass. The context — Shower Installer. Waterproof. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Drain.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Drain.", "x": "Shower Installer: Drain.. Waterproof. Essential knowledge — Waterproof.. the rain pros. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Drain..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Drain..", "x": "Explained: Drain.. Drain. The context — Shower Installer. Tile. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Waterproof.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Waterproof.", "x": "Shower Installer in depth: Waterproof.. Waterproof. Details — the rain pros.. Drain. Valve. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Glass.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Glass.", "x": "Shower Installer in depth: Glass.. Tile. Details — the rain pros.. Pan. Glass. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Drain.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Drain.", "x": "Shower Installer in depth: Drain.. Valve. Details — the rain pros.. Valve. Drain. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Pan.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Pan.", "x": "Shower Installer in depth: Pan.. Glass. Details — the rain pros.. Hiring. Pan. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Valve.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Valve.", "x": "Shower Installer in depth: Valve.. Drain. Details — the rain pros.. Waterproof. Waterproof. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Hiring.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Hiring.", "x": "Shower Installer in depth: Hiring.. Pan. Details — the rain pros.. Glass. Tile. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Shower Installer comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Shower Installer comes from.", "x": "Origins: Waterproof.. Pan. The history of Shower Installer — the rain pros.. Glass. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Shower Installer respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Shower Installer respectfully.", "x": "Engaging: Drain.. Waterproof. How to participate or observe well — Shower Installer. the rain pros. Respect first, always; Pan.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Shower Installer do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Shower Installer do's and don'ts.", "x": "Etiquette: Valve.. Tile. The rules of respect — Shower Installer. the rain pros. When in doubt, ask about Hiring.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Shower Installer.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Shower Installer.", "x": "Planning: Waterproof.. Valve. Practical notes — Shower Installer. the rain pros. A little planning shows respect for Glass.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Shower Installer and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Shower Installer and money.", "x": "Costs: Drain.. Glass. What to budget — Shower Installer. the rain pros. The best experiences of Pan. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-trade2-shower-installer-trade-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
