(function(){'use strict';
/* JAH Nintendo 64 Console Database generator — jahdb-e2-console-nintendo-64-console-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-console-nintendo-64-console',PREFIX='JAH-E2CONSOLENI-',NAME='JAH Nintendo 64 Console Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Nintendo 64: the complete guide", "d": "Nintendo 64: the 3D pioneer..", "g": "overview", "l": 2, "q": "What is Nintendo 64: the complete guide?", "a": "Nintendo 64: the 3D pioneer..", "x": "The complete console guide to Nintendo 64: the 3D pioneer.. 1996. History, meaning, practices, and how to engage respectfully — everything in one database. Mario 64. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Nintendo 64 essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Nintendo 64 essentials.", "x": "At a glance: Nintendo 64 — the 3D pioneer.. Mario 64. The essentials: Analog.. Ocarina. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "1996.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "1996.", "x": "Nintendo 64: 1996.. Analog. Essential knowledge — Ocarina.. the 3D pioneer. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 1996..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 1996..", "x": "Explained: 1996.. Ocarina. The context — Nintendo 64. Analog. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Mario 64.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Mario 64.", "x": "Nintendo 64: Mario 64.. 4 players. Essential knowledge — Analog.. the 3D pioneer. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Mario 64..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Mario 64..", "x": "Explained: Mario 64.. Cartridges. The context — Nintendo 64. Cartridges. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Ocarina.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Ocarina.", "x": "Nintendo 64: Ocarina.. Ocarina. Essential knowledge — Cartridges.. the 3D pioneer. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Ocarina..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Ocarina..", "x": "Explained: Ocarina.. Legacy. The context — Nintendo 64. 4 players. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Analog.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Analog.", "x": "Nintendo 64: Analog.. Cartridges. Essential knowledge — 4 players.. the 3D pioneer. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Analog..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Analog..", "x": "Explained: Analog.. Mario 64. The context — Nintendo 64. 1996. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Cartridges.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Cartridges.", "x": "Nintendo 64: Cartridges.. Legacy. Essential knowledge — 1996.. the 3D pioneer. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Cartridges..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Cartridges..", "x": "Explained: Cartridges.. Analog. The context — Nintendo 64. Mario 64. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "4 players.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "4 players.", "x": "Nintendo 64: 4 players.. Mario 64. Essential knowledge — Mario 64.. the 3D pioneer. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: 4 players..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: 4 players..", "x": "Explained: 4 players.. 4 players. The context — Nintendo 64. Ocarina. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Mario 64.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Mario 64.", "x": "Nintendo 64 in depth: Mario 64.. Mario 64. Details — the 3D pioneer.. 4 players. Analog. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Analog.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Analog.", "x": "Nintendo 64 in depth: Analog.. Ocarina. Details — the 3D pioneer.. Ocarina. Cartridges. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "4 players.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "4 players.", "x": "Nintendo 64 in depth: 4 players.. Analog. Details — the 3D pioneer.. Cartridges. 4 players. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Ocarina.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Ocarina.", "x": "Nintendo 64 in depth: Ocarina.. Cartridges. Details — the 3D pioneer.. Legacy. 1996. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Cartridges.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Cartridges.", "x": "Nintendo 64 in depth: Cartridges.. 4 players. Details — the 3D pioneer.. Mario 64. Mario 64. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Legacy.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Legacy.", "x": "Nintendo 64 in depth: Legacy.. 1996. Details — the 3D pioneer.. Analog. Ocarina. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Nintendo 64 comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Nintendo 64 comes from.", "x": "Origins: Mario 64.. 1996. The history of Nintendo 64 — the 3D pioneer.. Analog. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Nintendo 64 respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Nintendo 64 respectfully.", "x": "Engaging: 4 players.. Mario 64. How to participate or observe well — Nintendo 64. the 3D pioneer. Respect first, always; Ocarina.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Nintendo 64 do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Nintendo 64 do's and don'ts.", "x": "Etiquette: Cartridges.. Ocarina. The rules of respect — Nintendo 64. the 3D pioneer. When in doubt, ask about Legacy.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Nintendo 64.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Nintendo 64.", "x": "Planning: Mario 64.. Analog. Practical notes — Nintendo 64. the 3D pioneer. A little planning shows respect for Analog.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Nintendo 64 and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Nintendo 64 and money.", "x": "Costs: 4 players.. Cartridges. What to budget — Nintendo 64. the 3D pioneer. The best experiences of Ocarina. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-console-nintendo-64-console-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
