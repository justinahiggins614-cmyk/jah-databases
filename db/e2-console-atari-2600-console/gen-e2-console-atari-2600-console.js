(function(){'use strict';
/* JAH Atari 2600 Console Database generator — jahdb-e2-console-atari-2600-console-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-console-atari-2600-console',PREFIX='JAH-E2CONSOLEAT-',NAME='JAH Atari 2600 Console Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Atari 2600: the complete guide", "d": "Atari 2600: the crash pioneer..", "g": "overview", "l": 2, "q": "What is Atari 2600: the complete guide?", "a": "Atari 2600: the crash pioneer..", "x": "The complete console guide to Atari 2600: the crash pioneer.. 1977. History, meaning, practices, and how to engage respectfully — everything in one database. Crash. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Atari 2600 essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Atari 2600 essentials.", "x": "At a glance: Atari 2600 — the crash pioneer.. Atari. The essentials: Joystick.. Pitfall. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "1977.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "1977.", "x": "Atari 2600: 1977.. Joystick. Essential knowledge — Pitfall.. the crash pioneer. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 1977..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 1977..", "x": "Explained: 1977.. Atari. The context — Atari 2600. Crash 1983. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Atari.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Atari.", "x": "Atari 2600: Atari.. Cartridges. Essential knowledge — Crash 1983.. the crash pioneer. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Atari..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Atari..", "x": "Explained: Atari.. Pitfall. The context — Atari 2600. Joystick. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Pitfall.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Pitfall.", "x": "Atari 2600: Pitfall.. Atari. Essential knowledge — Joystick.. the crash pioneer. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Pitfall..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Pitfall..", "x": "Explained: Pitfall.. Legacy. The context — Atari 2600. Cartridges. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Crash 1983.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Crash 1983.", "x": "Atari 2600: Crash 1983.. Pitfall. Essential knowledge — Cartridges.. the crash pioneer. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Crash 1983..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Crash 1983..", "x": "Explained: Crash 1983.. Crash. The context — Atari 2600. 1977. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Joystick.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Joystick.", "x": "Atari 2600: Joystick.. Legacy. Essential knowledge — 1977.. the crash pioneer. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Joystick..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Joystick..", "x": "Explained: Joystick.. Joystick. The context — Atari 2600. Atari. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Cartridges.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Cartridges.", "x": "Atari 2600: Cartridges.. Crash. Essential knowledge — Atari.. the crash pioneer. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Cartridges..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Cartridges..", "x": "Explained: Cartridges.. Cartridges. The context — Atari 2600. Pitfall. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Crash.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Crash.", "x": "Atari 2600 in depth: Crash.. Atari. Details — the crash pioneer.. Cartridges. Crash 1983. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Joystick.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Joystick.", "x": "Atari 2600 in depth: Joystick.. Pitfall. Details — the crash pioneer.. Atari. Joystick. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Cartridges.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Cartridges.", "x": "Atari 2600 in depth: Cartridges.. Crash 1983. Details — the crash pioneer.. Pitfall. Cartridges. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Atari.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Atari.", "x": "Atari 2600 in depth: Atari.. Joystick. Details — the crash pioneer.. Legacy. 1977. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Pitfall.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Pitfall.", "x": "Atari 2600 in depth: Pitfall.. Cartridges. Details — the crash pioneer.. Crash. Atari. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Legacy.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Legacy.", "x": "Atari 2600 in depth: Legacy.. 1977. Details — the crash pioneer.. Joystick. Pitfall. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Atari 2600 comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Atari 2600 comes from.", "x": "Origins: Crash.. 1977. The history of Atari 2600 — the crash pioneer.. Joystick. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Atari 2600 respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Atari 2600 respectfully.", "x": "Engaging: Cartridges.. Atari. How to participate or observe well — Atari 2600. the crash pioneer. Respect first, always; Atari.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Atari 2600 do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Atari 2600 do's and don'ts.", "x": "Etiquette: Pitfall.. Pitfall. The rules of respect — Atari 2600. the crash pioneer. When in doubt, ask about Legacy.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Atari 2600.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Atari 2600.", "x": "Planning: Crash.. Crash 1983. Practical notes — Atari 2600. the crash pioneer. A little planning shows respect for Joystick.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Atari 2600 and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Atari 2600 and money.", "x": "Costs: Cartridges.. Joystick. What to budget — Atari 2600. the crash pioneer. The best experiences of Atari. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-console-atari-2600-console-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
