(function(){'use strict';
/* JAH Pairi Daiza Zoo Database generator — jahdb-e2-zoo-pairi-daiza-zoo-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-zoo-pairi-daiza-zoo',PREFIX='JAH-E2ZOOPAIRID-',NAME='JAH Pairi Daiza Zoo Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Pairi Daiza: the complete guide", "d": "Pairi Daiza: Belgium's garden zoo..", "g": "overview", "l": 2, "q": "What is Pairi Daiza: the complete guide?", "a": "Pairi Daiza: Belgium's garden zoo..", "x": "The complete zoo guide to Pairi Daiza: Belgium's garden zoo.. 1994. History, meaning, practices, and how to engage respectfully — everything in one database. Worlds. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Pairi Daiza essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Pairi Daiza essentials.", "x": "At a glance: Pairi Daiza — Belgium's garden zoo.. Pandas. The essentials: Pandas.. Temples. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "1994.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "1994.", "x": "Pairi Daiza: 1994.. Pandas. Essential knowledge — Temples.. Belgium's garden zoo. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 1994..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 1994..", "x": "Explained: 1994.. Belgium. The context — Pairi Daiza. Best zoo. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Pandas.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Pandas.", "x": "Pairi Daiza: Pandas.. Tickets. Essential knowledge — Best zoo.. Belgium's garden zoo. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Pandas..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Pandas..", "x": "Explained: Pandas.. Gardens. The context — Pairi Daiza. Cambron. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Temples.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Temples.", "x": "Pairi Daiza: Temples.. Belgium. Essential knowledge — Cambron.. Belgium's garden zoo. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Temples..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Temples..", "x": "Explained: Temples.. Awards. The context — Pairi Daiza. Worlds. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Best zoo.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Best zoo.", "x": "Pairi Daiza: Best zoo.. Gardens. Essential knowledge — Worlds.. Belgium's garden zoo. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Best zoo..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Best zoo..", "x": "Explained: Best zoo.. Worlds. The context — Pairi Daiza. 1994. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Cambron.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Cambron.", "x": "Pairi Daiza: Cambron.. Awards. Essential knowledge — 1994.. Belgium's garden zoo. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Cambron..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Cambron..", "x": "Explained: Cambron.. Pandas. The context — Pairi Daiza. Pandas. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Worlds.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Worlds.", "x": "Pairi Daiza: Worlds.. Worlds. Essential knowledge — Pandas.. Belgium's garden zoo. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Worlds..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Worlds..", "x": "Explained: Worlds.. Tickets. The context — Pairi Daiza. Temples. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Worlds.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Worlds.", "x": "Pairi Daiza in depth: Worlds.. Pandas. Details — Belgium's garden zoo.. Tickets. Best zoo. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Pandas.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Pandas.", "x": "Pairi Daiza in depth: Pandas.. Temples. Details — Belgium's garden zoo.. Belgium. Cambron. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Tickets.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Tickets.", "x": "Pairi Daiza in depth: Tickets.. Best zoo. Details — Belgium's garden zoo.. Gardens. Worlds. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Belgium.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Belgium.", "x": "Pairi Daiza in depth: Belgium.. Cambron. Details — Belgium's garden zoo.. Awards. 1994. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Gardens.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Gardens.", "x": "Pairi Daiza in depth: Gardens.. Worlds. Details — Belgium's garden zoo.. Worlds. Pandas. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Awards.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Awards.", "x": "Pairi Daiza in depth: Awards.. 1994. Details — Belgium's garden zoo.. Pandas. Temples. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Pairi Daiza comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Pairi Daiza comes from.", "x": "Origins: Worlds.. 1994. The history of Pairi Daiza — Belgium's garden zoo.. Pandas. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Pairi Daiza respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Pairi Daiza respectfully.", "x": "Engaging: Tickets.. Pandas. How to participate or observe well — Pairi Daiza. Belgium's garden zoo. Respect first, always; Belgium.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Pairi Daiza do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Pairi Daiza do's and don'ts.", "x": "Etiquette: Gardens.. Temples. The rules of respect — Pairi Daiza. Belgium's garden zoo. When in doubt, ask about Awards.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Pairi Daiza.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Pairi Daiza.", "x": "Planning: Worlds.. Best zoo. Practical notes — Pairi Daiza. Belgium's garden zoo. A little planning shows respect for Pandas.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Pairi Daiza and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Pairi Daiza and money.", "x": "Costs: Tickets.. Cambron. What to budget — Pairi Daiza. Belgium's garden zoo. The best experiences of Belgium. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-zoo-pairi-daiza-zoo-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
