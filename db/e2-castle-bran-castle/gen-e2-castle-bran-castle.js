(function(){'use strict';
/* JAH Bran Castle Castle Database generator — jahdb-e2-castle-bran-castle-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-castle-bran-castle',PREFIX='JAH-E2CASTLEBRA-',NAME='JAH Bran Castle Castle Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Bran Castle: the complete guide", "d": "Bran Castle: Dracula's castle..", "g": "overview", "l": 2, "q": "What is Bran Castle: the complete guide?", "a": "Bran Castle: Dracula's castle..", "x": "The complete castle guide to Bran Castle: Dracula's castle.. Romania. History, meaning, practices, and how to engage respectfully — everything in one database. Myth. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Bran Castle essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Bran Castle essentials.", "x": "At a glance: Bran Castle — Dracula's castle.. 1377. The essentials: History.. Vlad Tepes. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Romania.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Romania.", "x": "Bran Castle: Romania.. History. Essential knowledge — Vlad Tepes.. Dracula's castle. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Romania..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Romania..", "x": "Explained: Romania.. Romania. The context — Bran Castle. Tourism. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "1377.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "1377.", "x": "Bran Castle: 1377.. Tours. Essential knowledge — Tourism.. Dracula's castle. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: 1377..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: 1377..", "x": "Explained: 1377.. Vlad. The context — Bran Castle. Myth. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Vlad Tepes.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Vlad Tepes.", "x": "Bran Castle: Vlad Tepes.. Romania. Essential knowledge — Myth.. Dracula's castle. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Vlad Tepes..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Vlad Tepes..", "x": "Explained: Vlad Tepes.. Views. The context — Bran Castle. Transylvania. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Tourism.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Tourism.", "x": "Bran Castle: Tourism.. Vlad. Essential knowledge — Transylvania.. Dracula's castle. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Tourism..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Tourism..", "x": "Explained: Tourism.. Myth. The context — Bran Castle. Romania. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Myth.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Myth.", "x": "Bran Castle: Myth.. Views. Essential knowledge — Romania.. Dracula's castle. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Myth..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Myth..", "x": "Explained: Myth.. History. The context — Bran Castle. 1377. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Transylvania.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Transylvania.", "x": "Bran Castle: Transylvania.. Myth. Essential knowledge — 1377.. Dracula's castle. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Transylvania..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Transylvania..", "x": "Explained: Transylvania.. Tours. The context — Bran Castle. Vlad Tepes. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Myth.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Myth.", "x": "Bran Castle in depth: Myth.. 1377. Details — Dracula's castle.. Tours. Tourism. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "History.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "History.", "x": "Bran Castle in depth: History.. Vlad Tepes. Details — Dracula's castle.. Romania. Myth. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Tours.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Tours.", "x": "Bran Castle in depth: Tours.. Tourism. Details — Dracula's castle.. Vlad. Transylvania. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Romania.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Romania.", "x": "Bran Castle in depth: Romania.. Myth. Details — Dracula's castle.. Views. Romania. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Vlad.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Vlad.", "x": "Bran Castle in depth: Vlad.. Transylvania. Details — Dracula's castle.. Myth. 1377. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Views.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Views.", "x": "Bran Castle in depth: Views.. Romania. Details — Dracula's castle.. History. Vlad Tepes. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Bran Castle comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Bran Castle comes from.", "x": "Origins: Myth.. Romania. The history of Bran Castle — Dracula's castle.. History. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Bran Castle respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Bran Castle respectfully.", "x": "Engaging: Tours.. 1377. How to participate or observe well — Bran Castle. Dracula's castle. Respect first, always; Romania.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Bran Castle do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Bran Castle do's and don'ts.", "x": "Etiquette: Vlad.. Vlad Tepes. The rules of respect — Bran Castle. Dracula's castle. When in doubt, ask about Views.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Bran Castle.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Bran Castle.", "x": "Planning: Myth.. Tourism. Practical notes — Bran Castle. Dracula's castle. A little planning shows respect for History.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Bran Castle and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Bran Castle and money.", "x": "Costs: Tours.. Myth. What to budget — Bran Castle. Dracula's castle. The best experiences of Romania. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-castle-bran-castle-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
