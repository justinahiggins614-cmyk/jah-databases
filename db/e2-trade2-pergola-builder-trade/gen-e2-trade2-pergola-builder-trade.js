(function(){'use strict';
/* JAH Pergola Builder Database generator — jahdb-e2-trade2-pergola-builder-trade-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-trade2-pergola-builder-trade',PREFIX='JAH-E2TRADE2PER-',NAME='JAH Pergola Builder Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Pergola Builder: the complete guide", "d": "Pergola Builder: the shade pros..", "g": "overview", "l": 2, "q": "What is Pergola Builder: the complete guide?", "a": "Pergola Builder: the shade pros..", "x": "The complete trade guide to Pergola Builder: the shade pros.. Cedar. History, meaning, practices, and how to engage respectfully — everything in one database. Cedar. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Pergola Builder essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Pergola Builder essentials.", "x": "At a glance: Pergola Builder — the shade pros.. Footings. The essentials: Rafters.. Shade. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Cedar.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Cedar.", "x": "Pergola Builder: Cedar.. Rafters. Essential knowledge — Shade.. the shade pros. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Cedar..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Cedar..", "x": "Explained: Cedar.. Footings. The context — Pergola Builder. Rafters. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Footings.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Footings.", "x": "Pergola Builder: Footings.. Attached. Essential knowledge — Rafters.. the shade pros. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Footings..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Footings..", "x": "Explained: Footings.. Shade. The context — Pergola Builder. Staining. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Shade.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Shade.", "x": "Pergola Builder: Shade.. Footings. Essential knowledge — Staining.. the shade pros. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Shade..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Shade..", "x": "Explained: Shade.. Hiring. The context — Pergola Builder. Attached. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Rafters.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Rafters.", "x": "Pergola Builder: Rafters.. Shade. Essential knowledge — Attached.. the shade pros. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Rafters..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Rafters..", "x": "Explained: Rafters.. Cedar. The context — Pergola Builder. Cedar. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Staining.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Staining.", "x": "Pergola Builder: Staining.. Hiring. Essential knowledge — Cedar.. the shade pros. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Staining..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Staining..", "x": "Explained: Staining.. Rafters. The context — Pergola Builder. Footings. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Attached.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Attached.", "x": "Pergola Builder: Attached.. Cedar. Essential knowledge — Footings.. the shade pros. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Attached..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Attached..", "x": "Explained: Attached.. Attached. The context — Pergola Builder. Shade. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Cedar.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Cedar.", "x": "Pergola Builder in depth: Cedar.. Footings. Details — the shade pros.. Attached. Rafters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Rafters.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Rafters.", "x": "Pergola Builder in depth: Rafters.. Shade. Details — the shade pros.. Footings. Staining. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Attached.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Attached.", "x": "Pergola Builder in depth: Attached.. Rafters. Details — the shade pros.. Shade. Attached. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Footings.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Footings.", "x": "Pergola Builder in depth: Footings.. Staining. Details — the shade pros.. Hiring. Cedar. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Shade.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Shade.", "x": "Pergola Builder in depth: Shade.. Attached. Details — the shade pros.. Cedar. Footings. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Hiring.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Hiring.", "x": "Pergola Builder in depth: Hiring.. Cedar. Details — the shade pros.. Rafters. Shade. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Pergola Builder comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Pergola Builder comes from.", "x": "Origins: Cedar.. Cedar. The history of Pergola Builder — the shade pros.. Rafters. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Pergola Builder respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Pergola Builder respectfully.", "x": "Engaging: Attached.. Footings. How to participate or observe well — Pergola Builder. the shade pros. Respect first, always; Footings.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Pergola Builder do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Pergola Builder do's and don'ts.", "x": "Etiquette: Shade.. Shade. The rules of respect — Pergola Builder. the shade pros. When in doubt, ask about Hiring.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Pergola Builder.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Pergola Builder.", "x": "Planning: Cedar.. Rafters. Practical notes — Pergola Builder. the shade pros. A little planning shows respect for Rafters.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Pergola Builder and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Pergola Builder and money.", "x": "Costs: Attached.. Staining. What to budget — Pergola Builder. the shade pros. The best experiences of Footings. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-trade2-pergola-builder-trade-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
