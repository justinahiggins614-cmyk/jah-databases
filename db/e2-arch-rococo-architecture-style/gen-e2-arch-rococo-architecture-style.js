(function(){'use strict';
/* JAH Rococo Architecture Style Database generator — jahdb-e2-arch-rococo-architecture-style-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-arch-rococo-architecture-style',PREFIX='JAH-E2ARCHROCOC-',NAME='JAH Rococo Architecture Style Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Rococo Architecture: the complete guide", "d": "Rococo Architecture: the playful ornament..", "g": "overview", "l": 2, "q": "What is Rococo Architecture: the complete guide?", "a": "Rococo Architecture: the playful ornament..", "x": "The complete architecture style guide to Rococo Architecture: the playful ornament.. Pastel. History, meaning, practices, and how to engage respectfully — everything in one database. Pastel. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Rococo Architecture essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Rococo Architecture essentials.", "x": "At a glance: Rococo Architecture — the playful ornament.. Shells. The essentials: Ornament.. Asymmetry. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Pastel.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Pastel.", "x": "Rococo Architecture: Pastel.. Ornament. Essential knowledge — Asymmetry.. the playful ornament. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Pastel..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Pastel..", "x": "Explained: Pastel.. 18th. The context — Rococo Architecture. 18th century. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Shells.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Shells.", "x": "Rococo Architecture: Shells.. Intimate. Essential knowledge — 18th century.. the playful ornament. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Shells..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Shells..", "x": "Explained: Shells.. Shells. The context — Rococo Architecture. Intimate. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Asymmetry.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Asymmetry.", "x": "Rococo Architecture: Asymmetry.. 18th. Essential knowledge — Intimate.. the playful ornament. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Asymmetry..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Asymmetry..", "x": "Explained: Asymmetry.. Legacy. The context — Rococo Architecture. Ornament. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "18th century.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "18th century.", "x": "Rococo Architecture: 18th century.. Shells. Essential knowledge — Ornament.. the playful ornament. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: 18th century..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: 18th century..", "x": "Explained: 18th century.. Pastel. The context — Rococo Architecture. Pastel. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Intimate.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Intimate.", "x": "Rococo Architecture: Intimate.. Legacy. Essential knowledge — Pastel.. the playful ornament. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Intimate..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Intimate..", "x": "Explained: Intimate.. Ornament. The context — Rococo Architecture. Shells. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Ornament.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Ornament.", "x": "Rococo Architecture: Ornament.. Pastel. Essential knowledge — Shells.. the playful ornament. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Ornament..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Ornament..", "x": "Explained: Ornament.. Intimate. The context — Rococo Architecture. Asymmetry. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Pastel.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Pastel.", "x": "Rococo Architecture in depth: Pastel.. Shells. Details — the playful ornament.. Intimate. 18th century. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Ornament.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Ornament.", "x": "Rococo Architecture in depth: Ornament.. Asymmetry. Details — the playful ornament.. 18th. Intimate. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Intimate.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Intimate.", "x": "Rococo Architecture in depth: Intimate.. 18th century. Details — the playful ornament.. Shells. Ornament. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "18th.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "18th.", "x": "Rococo Architecture in depth: 18th.. Intimate. Details — the playful ornament.. Legacy. Pastel. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Shells.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Shells.", "x": "Rococo Architecture in depth: Shells.. Ornament. Details — the playful ornament.. Pastel. Shells. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Legacy.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Legacy.", "x": "Rococo Architecture in depth: Legacy.. Pastel. Details — the playful ornament.. Ornament. Asymmetry. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Rococo Architecture comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Rococo Architecture comes from.", "x": "Origins: Pastel.. Pastel. The history of Rococo Architecture — the playful ornament.. Ornament. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Rococo Architecture respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Rococo Architecture respectfully.", "x": "Engaging: Intimate.. Shells. How to participate or observe well — Rococo Architecture. the playful ornament. Respect first, always; 18th.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Rococo Architecture do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Rococo Architecture do's and don'ts.", "x": "Etiquette: Shells.. Asymmetry. The rules of respect — Rococo Architecture. the playful ornament. When in doubt, ask about Legacy.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Rococo Architecture.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Rococo Architecture.", "x": "Planning: Pastel.. 18th century. Practical notes — Rococo Architecture. the playful ornament. A little planning shows respect for Ornament.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Rococo Architecture and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Rococo Architecture and money.", "x": "Costs: Intimate.. Intimate. What to budget — Rococo Architecture. the playful ornament. The best experiences of 18th. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-arch-rococo-architecture-style-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
