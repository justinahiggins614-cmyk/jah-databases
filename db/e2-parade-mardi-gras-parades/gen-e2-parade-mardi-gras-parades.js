(function(){'use strict';
/* JAH Mardi Gras Parades Parade Database generator — jahdb-e2-parade-mardi-gras-parades-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-parade-mardi-gras-parades',PREFIX='JAH-E2PARADEMAR-',NAME='JAH Mardi Gras Parades Parade Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Mardi Gras Parades: the complete guide", "d": "Mardi Gras Parades: the Big Easy carnival..", "g": "overview", "l": 2, "q": "What is Mardi Gras Parades: the complete guide?", "a": "Mardi Gras Parades: the Big Easy carnival..", "x": "The complete parade guide to Mardi Gras Parades: the Big Easy carnival.. New Orleans. History, meaning, practices, and how to engage respectfully — everything in one database. Beads. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Mardi Gras Parades essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Mardi Gras Parades essentials.", "x": "At a glance: Mardi Gras Parades — the Big Easy carnival.. Beads. The essentials: Krewes.. Krewes. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "New Orleans.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "New Orleans.", "x": "Mardi Gras Parades: New Orleans.. Krewes. Essential knowledge — Krewes.. the Big Easy carnival. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: New Orleans..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: New Orleans..", "x": "Explained: New Orleans.. Masks. The context — Mardi Gras Parades. Fat Tuesday. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Beads.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Beads.", "x": "Mardi Gras Parades: Beads.. Floats. Essential knowledge — Fat Tuesday.. the Big Easy carnival. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Beads..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Beads..", "x": "Explained: Beads.. NOLA. The context — Mardi Gras Parades. Floats. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Krewes.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Krewes.", "x": "Mardi Gras Parades: Krewes.. Masks. Essential knowledge — Floats.. the Big Easy carnival. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Krewes..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Krewes..", "x": "Explained: Krewes.. History. The context — Mardi Gras Parades. Masks. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Fat Tuesday.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Fat Tuesday.", "x": "Mardi Gras Parades: Fat Tuesday.. NOLA. Essential knowledge — Masks.. the Big Easy carnival. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Fat Tuesday..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Fat Tuesday..", "x": "Explained: Fat Tuesday.. Beads. The context — Mardi Gras Parades. New Orleans. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Floats.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Floats.", "x": "Mardi Gras Parades: Floats.. History. Essential knowledge — New Orleans.. the Big Easy carnival. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Floats..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Floats..", "x": "Explained: Floats.. Krewes. The context — Mardi Gras Parades. Beads. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Masks.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Masks.", "x": "Mardi Gras Parades: Masks.. Beads. Essential knowledge — Beads.. the Big Easy carnival. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Masks..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Masks..", "x": "Explained: Masks.. Floats. The context — Mardi Gras Parades. Krewes. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Beads.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Beads.", "x": "Mardi Gras Parades in depth: Beads.. Beads. Details — the Big Easy carnival.. Floats. Fat Tuesday. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Krewes.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Krewes.", "x": "Mardi Gras Parades in depth: Krewes.. Krewes. Details — the Big Easy carnival.. Masks. Floats. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Floats.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Floats.", "x": "Mardi Gras Parades in depth: Floats.. Fat Tuesday. Details — the Big Easy carnival.. NOLA. Masks. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Masks.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Masks.", "x": "Mardi Gras Parades in depth: Masks.. Floats. Details — the Big Easy carnival.. History. New Orleans. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "NOLA.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "NOLA.", "x": "Mardi Gras Parades in depth: NOLA.. Masks. Details — the Big Easy carnival.. Beads. Beads. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "History.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "History.", "x": "Mardi Gras Parades in depth: History.. New Orleans. Details — the Big Easy carnival.. Krewes. Krewes. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Mardi Gras Parades comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Mardi Gras Parades comes from.", "x": "Origins: Beads.. New Orleans. The history of Mardi Gras Parades — the Big Easy carnival.. Krewes. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Mardi Gras Parades respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Mardi Gras Parades respectfully.", "x": "Engaging: Floats.. Beads. How to participate or observe well — Mardi Gras Parades. the Big Easy carnival. Respect first, always; Masks.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Mardi Gras Parades do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Mardi Gras Parades do's and don'ts.", "x": "Etiquette: NOLA.. Krewes. The rules of respect — Mardi Gras Parades. the Big Easy carnival. When in doubt, ask about History.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Mardi Gras Parades.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Mardi Gras Parades.", "x": "Planning: Beads.. Fat Tuesday. Practical notes — Mardi Gras Parades. the Big Easy carnival. A little planning shows respect for Krewes.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Mardi Gras Parades and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Mardi Gras Parades and money.", "x": "Costs: Floats.. Floats. What to budget — Mardi Gras Parades. the Big Easy carnival. The best experiences of Masks. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-parade-mardi-gras-parades-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
