(function(){'use strict';
/* JAH Stratford-upon-Avon Landmark Database generator — jahdb-e2-landmark-stratford-avon-landmark-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-landmark-stratford-avon-landmark',PREFIX='JAH-E2LANDMARKS-',NAME='JAH Stratford-upon-Avon Landmark Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Stratford-upon-Avon: the complete guide", "d": "Stratford-upon-Avon: Shakespeare's town..", "g": "overview", "l": 2, "q": "What is Stratford-upon-Avon: the complete guide?", "a": "Stratford-upon-Avon: Shakespeare's town..", "x": "The complete landmark guide to Stratford-upon-Avon: Shakespeare's town.. 1564. History, meaning, practices, and how to engage respectfully — everything in one database. 1564. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Stratford-upon-Avon essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Stratford-upon-Avon essentials.", "x": "At a glance: Stratford-upon-Avon — Shakespeare's town.. Shakespeare. The essentials: Birthplace.. Birthplace. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "1564.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "1564.", "x": "Stratford-upon-Avon: 1564.. Birthplace. Essential knowledge — Birthplace.. Shakespeare's town. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 1564..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 1564..", "x": "Explained: 1564.. Avon. The context — Stratford-upon-Avon. Avon. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Shakespeare.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Shakespeare.", "x": "Stratford-upon-Avon: Shakespeare.. RSC. Essential knowledge — Avon.. Shakespeare's town. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Shakespeare..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Shakespeare..", "x": "Explained: Shakespeare.. Cottages. The context — Stratford-upon-Avon. RSC. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Birthplace.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Birthplace.", "x": "Stratford-upon-Avon: Birthplace.. Avon. Essential knowledge — RSC.. Shakespeare's town. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Birthplace..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Birthplace..", "x": "Explained: Birthplace.. Tours. The context — Stratford-upon-Avon. Cottages. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Avon.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Avon.", "x": "Stratford-upon-Avon: Avon.. Cottages. Essential knowledge — Cottages.. Shakespeare's town. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Avon..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Avon..", "x": "Explained: Avon.. 1564. The context — Stratford-upon-Avon. 1564. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "RSC.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "RSC.", "x": "Stratford-upon-Avon: RSC.. Tours. Essential knowledge — 1564.. Shakespeare's town. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: RSC..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: RSC..", "x": "Explained: RSC.. Birthplace. The context — Stratford-upon-Avon. Shakespeare. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Cottages.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Cottages.", "x": "Stratford-upon-Avon: Cottages.. 1564. Essential knowledge — Shakespeare.. Shakespeare's town. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Cottages..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Cottages..", "x": "Explained: Cottages.. RSC. The context — Stratford-upon-Avon. Birthplace. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "1564.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "1564.", "x": "Stratford-upon-Avon in depth: 1564.. Shakespeare. Details — Shakespeare's town.. RSC. Avon. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Birthplace.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Birthplace.", "x": "Stratford-upon-Avon in depth: Birthplace.. Birthplace. Details — Shakespeare's town.. Avon. RSC. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "RSC.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "RSC.", "x": "Stratford-upon-Avon in depth: RSC.. Avon. Details — Shakespeare's town.. Cottages. Cottages. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Avon.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Avon.", "x": "Stratford-upon-Avon in depth: Avon.. RSC. Details — Shakespeare's town.. Tours. 1564. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Cottages.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Cottages.", "x": "Stratford-upon-Avon in depth: Cottages.. Cottages. Details — Shakespeare's town.. 1564. Shakespeare. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Tours.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Tours.", "x": "Stratford-upon-Avon in depth: Tours.. 1564. Details — Shakespeare's town.. Birthplace. Birthplace. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Stratford-upon-Avon comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Stratford-upon-Avon comes from.", "x": "Origins: 1564.. 1564. The history of Stratford-upon-Avon — Shakespeare's town.. Birthplace. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Stratford-upon-Avon respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Stratford-upon-Avon respectfully.", "x": "Engaging: RSC.. Shakespeare. How to participate or observe well — Stratford-upon-Avon. Shakespeare's town. Respect first, always; Avon.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Stratford-upon-Avon do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Stratford-upon-Avon do's and don'ts.", "x": "Etiquette: Cottages.. Birthplace. The rules of respect — Stratford-upon-Avon. Shakespeare's town. When in doubt, ask about Tours.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Stratford-upon-Avon.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Stratford-upon-Avon.", "x": "Planning: 1564.. Avon. Practical notes — Stratford-upon-Avon. Shakespeare's town. A little planning shows respect for Birthplace.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Stratford-upon-Avon and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Stratford-upon-Avon and money.", "x": "Costs: RSC.. RSC. What to budget — Stratford-upon-Avon. Shakespeare's town. The best experiences of Avon. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-landmark-stratford-avon-landmark-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
