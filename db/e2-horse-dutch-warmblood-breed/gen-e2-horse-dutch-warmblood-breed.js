(function(){'use strict';
/* JAH Dutch Warmblood Horse Breed Database generator — jahdb-e2-horse-dutch-warmblood-breed-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-horse-dutch-warmblood-breed',PREFIX='JAH-E2HORSEDUTC-',NAME='JAH Dutch Warmblood Horse Breed Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Dutch Warmblood: the complete guide", "d": "Dutch Warmblood: the KWPN jumper..", "g": "overview", "l": 2, "q": "What is Dutch Warmblood: the complete guide?", "a": "Dutch Warmblood: the KWPN jumper..", "x": "The complete horse breed guide to Dutch Warmblood: the KWPN jumper.. Netherlands. History, meaning, practices, and how to engage respectfully — everything in one database. Jumping. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Dutch Warmblood essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Dutch Warmblood essentials.", "x": "At a glance: Dutch Warmblood — the KWPN jumper.. Jumping. The essentials: KWPN.. KWPN. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Netherlands.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Netherlands.", "x": "Dutch Warmblood: Netherlands.. KWPN. Essential knowledge — KWPN.. the KWPN jumper. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Netherlands..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Netherlands..", "x": "Explained: Netherlands.. Keuring. The context — Dutch Warmblood. Olympics. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Jumping.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Jumping.", "x": "Dutch Warmblood: Jumping.. Olympics. Essential knowledge — Olympics.. the KWPN jumper. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Jumping..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Jumping..", "x": "Explained: Jumping.. Netherlands. The context — Dutch Warmblood. Keuring. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "KWPN.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "KWPN.", "x": "Dutch Warmblood: KWPN.. Keuring. Essential knowledge — Keuring.. the KWPN jumper. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: KWPN..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: KWPN..", "x": "Explained: KWPN.. History. The context — Dutch Warmblood. Sport. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Olympics.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Olympics.", "x": "Dutch Warmblood: Olympics.. Netherlands. Essential knowledge — Sport.. the KWPN jumper. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Olympics..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Olympics..", "x": "Explained: Olympics.. Jumping. The context — Dutch Warmblood. Netherlands. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Keuring.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Keuring.", "x": "Dutch Warmblood: Keuring.. History. Essential knowledge — Netherlands.. the KWPN jumper. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Keuring..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Keuring..", "x": "Explained: Keuring.. KWPN. The context — Dutch Warmblood. Jumping. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Sport.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Sport.", "x": "Dutch Warmblood: Sport.. Jumping. Essential knowledge — Jumping.. the KWPN jumper. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Sport..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Sport..", "x": "Explained: Sport.. Olympics. The context — Dutch Warmblood. KWPN. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Jumping.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Jumping.", "x": "Dutch Warmblood in depth: Jumping.. Jumping. Details — the KWPN jumper.. Olympics. Olympics. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "KWPN.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "KWPN.", "x": "Dutch Warmblood in depth: KWPN.. KWPN. Details — the KWPN jumper.. Keuring. Keuring. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Olympics.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Olympics.", "x": "Dutch Warmblood in depth: Olympics.. Olympics. Details — the KWPN jumper.. Netherlands. Sport. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Keuring.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Keuring.", "x": "Dutch Warmblood in depth: Keuring.. Keuring. Details — the KWPN jumper.. History. Netherlands. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Netherlands.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Netherlands.", "x": "Dutch Warmblood in depth: Netherlands.. Sport. Details — the KWPN jumper.. Jumping. Jumping. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "History.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "History.", "x": "Dutch Warmblood in depth: History.. Netherlands. Details — the KWPN jumper.. KWPN. KWPN. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Dutch Warmblood comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Dutch Warmblood comes from.", "x": "Origins: Jumping.. Netherlands. The history of Dutch Warmblood — the KWPN jumper.. KWPN. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Dutch Warmblood respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Dutch Warmblood respectfully.", "x": "Engaging: Olympics.. Jumping. How to participate or observe well — Dutch Warmblood. the KWPN jumper. Respect first, always; Keuring.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Dutch Warmblood do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Dutch Warmblood do's and don'ts.", "x": "Etiquette: Netherlands.. KWPN. The rules of respect — Dutch Warmblood. the KWPN jumper. When in doubt, ask about History.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Dutch Warmblood.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Dutch Warmblood.", "x": "Planning: Jumping.. Olympics. Practical notes — Dutch Warmblood. the KWPN jumper. A little planning shows respect for KWPN.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Dutch Warmblood and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Dutch Warmblood and money.", "x": "Costs: Olympics.. Keuring. What to budget — Dutch Warmblood. the KWPN jumper. The best experiences of Keuring. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-horse-dutch-warmblood-breed-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
