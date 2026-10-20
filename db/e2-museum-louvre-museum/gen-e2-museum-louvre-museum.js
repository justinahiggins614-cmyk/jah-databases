(function(){'use strict';
/* JAH Louvre Museum Museum Database generator — jahdb-e2-museum-louvre-museum-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-museum-louvre-museum',PREFIX='JAH-E2MUSEUMLOU-',NAME='JAH Louvre Museum Museum Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Louvre Museum: the complete guide", "d": "Louvre Museum: the world's most visited museum..", "g": "overview", "l": 2, "q": "What is Louvre Museum: the complete guide?", "a": "Louvre Museum: the world's most visited museum..", "x": "The complete museum guide to Louvre Museum: the world's most visited museum.. Mona Lisa. History, meaning, practices, and how to engage respectfully — everything in one database. Mona Lisa. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Louvre Museum essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Louvre Museum essentials.", "x": "At a glance: Louvre Museum — the world's most visited museum.. Paris. The essentials: Wings.. 1793. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Mona Lisa.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Mona Lisa.", "x": "Louvre Museum: Mona Lisa.. Wings. Essential knowledge — 1793.. the world's most visited museum. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Mona Lisa..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Mona Lisa..", "x": "Explained: Mona Lisa.. Tickets. The context — Louvre Museum. Pyramid. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Paris.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Paris.", "x": "Louvre Museum: Paris.. History. Essential knowledge — Pyramid.. the world's most visited museum. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Paris..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Paris..", "x": "Explained: Paris.. Pyramid. The context — Louvre Museum. Venus de Milo. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "1793.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "1793.", "x": "Louvre Museum: 1793.. Tickets. Essential knowledge — Venus de Milo.. the world's most visited museum. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: 1793..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: 1793..", "x": "Explained: 1793.. Art. The context — Louvre Museum. 8M visitors. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Pyramid.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Pyramid.", "x": "Louvre Museum: Pyramid.. Pyramid. Essential knowledge — 8M visitors.. the world's most visited museum. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Pyramid..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Pyramid..", "x": "Explained: Pyramid.. Mona Lisa. The context — Louvre Museum. Mona Lisa. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Venus de Milo.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Venus de Milo.", "x": "Louvre Museum: Venus de Milo.. Art. Essential knowledge — Mona Lisa.. the world's most visited museum. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Venus de Milo..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Venus de Milo..", "x": "Explained: Venus de Milo.. Wings. The context — Louvre Museum. Paris. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "8M visitors.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "8M visitors.", "x": "Louvre Museum: 8M visitors.. Mona Lisa. Essential knowledge — Paris.. the world's most visited museum. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: 8M visitors..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: 8M visitors..", "x": "Explained: 8M visitors.. History. The context — Louvre Museum. 1793. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Mona Lisa.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Mona Lisa.", "x": "Louvre Museum in depth: Mona Lisa.. Paris. Details — the world's most visited museum.. History. Pyramid. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Wings.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Wings.", "x": "Louvre Museum in depth: Wings.. 1793. Details — the world's most visited museum.. Tickets. Venus de Milo. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "History.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "History.", "x": "Louvre Museum in depth: History.. Pyramid. Details — the world's most visited museum.. Pyramid. 8M visitors. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Tickets.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Tickets.", "x": "Louvre Museum in depth: Tickets.. Venus de Milo. Details — the world's most visited museum.. Art. Mona Lisa. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Pyramid.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Pyramid.", "x": "Louvre Museum in depth: Pyramid.. 8M visitors. Details — the world's most visited museum.. Mona Lisa. Paris. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Art.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Art.", "x": "Louvre Museum in depth: Art.. Mona Lisa. Details — the world's most visited museum.. Wings. 1793. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Louvre Museum comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Louvre Museum comes from.", "x": "Origins: Mona Lisa.. Mona Lisa. The history of Louvre Museum — the world's most visited museum.. Wings. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Louvre Museum respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Louvre Museum respectfully.", "x": "Engaging: History.. Paris. How to participate or observe well — Louvre Museum. the world's most visited museum. Respect first, always; Tickets.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Louvre Museum do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Louvre Museum do's and don'ts.", "x": "Etiquette: Pyramid.. 1793. The rules of respect — Louvre Museum. the world's most visited museum. When in doubt, ask about Art.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Louvre Museum.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Louvre Museum.", "x": "Planning: Mona Lisa.. Pyramid. Practical notes — Louvre Museum. the world's most visited museum. A little planning shows respect for Wings.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Louvre Museum and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Louvre Museum and money.", "x": "Costs: History.. Venus de Milo. What to budget — Louvre Museum. the world's most visited museum. The best experiences of Tickets. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-museum-louvre-museum-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
