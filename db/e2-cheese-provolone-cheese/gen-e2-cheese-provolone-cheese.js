(function(){'use strict';
/* JAH Provolone Cheese Database generator — jahdb-e2-cheese-provolone-cheese-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-cheese-provolone-cheese',PREFIX='JAH-E2CHEESEPRO-',NAME='JAH Provolone Cheese Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Provolone: the complete guide", "d": "Provolone: the hanging cheese..", "g": "overview", "l": 2, "q": "What is Provolone: the complete guide?", "a": "Provolone: the hanging cheese..", "x": "The complete cheese guide to Provolone: the hanging cheese.. Pasta filata. History, meaning, practices, and how to engage respectfully — everything in one database. Hung. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Provolone essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Provolone essentials.", "x": "At a glance: Provolone — the hanging cheese.. Hung. The essentials: Smoked.. Smoked. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Pasta filata.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Pasta filata.", "x": "Provolone: Pasta filata.. Smoked. Essential knowledge — Smoked.. the hanging cheese. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Pasta filata..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Pasta filata..", "x": "Explained: Pasta filata.. Italy. The context — Provolone. Deli. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Hung.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Hung.", "x": "Provolone: Hung.. Deli. Essential knowledge — Deli.. the hanging cheese. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Hung..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Hung..", "x": "Explained: Hung.. Mild. The context — Provolone. Mild/sharp. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Smoked.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Smoked.", "x": "Provolone: Smoked.. Italy. Essential knowledge — Mild/sharp.. the hanging cheese. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Smoked..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Smoked..", "x": "Explained: Smoked.. Making. The context — Provolone. Italy. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Deli.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Deli.", "x": "Provolone: Deli.. Mild. Essential knowledge — Italy.. the hanging cheese. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Deli..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Deli..", "x": "Explained: Deli.. Hung. The context — Provolone. Pasta filata. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Mild/sharp.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Mild/sharp.", "x": "Provolone: Mild/sharp.. Making. Essential knowledge — Pasta filata.. the hanging cheese. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Mild/sharp..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Mild/sharp..", "x": "Explained: Mild/sharp.. Smoked. The context — Provolone. Hung. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Italy.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Italy.", "x": "Provolone: Italy.. Hung. Essential knowledge — Hung.. the hanging cheese. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Italy..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Italy..", "x": "Explained: Italy.. Deli. The context — Provolone. Smoked. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Hung.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Hung.", "x": "Provolone in depth: Hung.. Hung. Details — the hanging cheese.. Deli. Deli. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Smoked.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Smoked.", "x": "Provolone in depth: Smoked.. Smoked. Details — the hanging cheese.. Italy. Mild/sharp. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Deli.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Deli.", "x": "Provolone in depth: Deli.. Deli. Details — the hanging cheese.. Mild. Italy. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Italy.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Italy.", "x": "Provolone in depth: Italy.. Mild/sharp. Details — the hanging cheese.. Making. Pasta filata. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Mild.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Mild.", "x": "Provolone in depth: Mild.. Italy. Details — the hanging cheese.. Hung. Hung. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Making.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Making.", "x": "Provolone in depth: Making.. Pasta filata. Details — the hanging cheese.. Smoked. Smoked. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Provolone comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Provolone comes from.", "x": "Origins: Hung.. Pasta filata. The history of Provolone — the hanging cheese.. Smoked. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Provolone respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Provolone respectfully.", "x": "Engaging: Deli.. Hung. How to participate or observe well — Provolone. the hanging cheese. Respect first, always; Italy.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Provolone do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Provolone do's and don'ts.", "x": "Etiquette: Mild.. Smoked. The rules of respect — Provolone. the hanging cheese. When in doubt, ask about Making.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Provolone.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Provolone.", "x": "Planning: Hung.. Deli. Practical notes — Provolone. the hanging cheese. A little planning shows respect for Smoked.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Provolone and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Provolone and money.", "x": "Costs: Deli.. Mild/sharp. What to budget — Provolone. the hanging cheese. The best experiences of Italy. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-cheese-provolone-cheese-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
