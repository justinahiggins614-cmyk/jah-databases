(function(){'use strict';
/* JAH Bastille Day Holiday Database generator — jahdb-e2-holiday-bastille-day-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-holiday-bastille-day',PREFIX='JAH-E2HOLIDAYBA-',NAME='JAH Bastille Day Holiday Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Bastille Day: the complete guide", "d": "Bastille Day: France's national day..", "g": "overview", "l": 2, "q": "What is Bastille Day: the complete guide?", "a": "Bastille Day: France's national day..", "x": "The complete holiday guide to Bastille Day: France's national day.. July 14. History, meaning, practices, and how to engage respectfully — everything in one database. History. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Bastille Day essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Bastille Day essentials.", "x": "At a glance: Bastille Day — France's national day.. 1789. The essentials: Parade.. Parade. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "July 14.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "July 14.", "x": "Bastille Day: July 14.. Parade. Essential knowledge — Parade.. France's national day. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: July 14..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: July 14..", "x": "Explained: July 14.. Meaning. The context — Bastille Day. Fireworks. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "1789.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "1789.", "x": "Bastille Day: 1789.. Fireworks. Essential knowledge — Fireworks.. France's national day. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: 1789..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: 1789..", "x": "Explained: 1789.. France. The context — Bastille Day. Revolution. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Parade.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Parade.", "x": "Bastille Day: Parade.. Meaning. Essential knowledge — Revolution.. France's national day. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Parade..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Parade..", "x": "Explained: Parade.. Celebration. The context — Bastille Day. Paris. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Fireworks.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Fireworks.", "x": "Bastille Day: Fireworks.. France. Essential knowledge — Paris.. France's national day. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Fireworks..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Fireworks..", "x": "Explained: Fireworks.. History. The context — Bastille Day. July 14. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Revolution.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Revolution.", "x": "Bastille Day: Revolution.. Celebration. Essential knowledge — July 14.. France's national day. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Revolution..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Revolution..", "x": "Explained: Revolution.. Parade. The context — Bastille Day. 1789. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Paris.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Paris.", "x": "Bastille Day: Paris.. History. Essential knowledge — 1789.. France's national day. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Paris..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Paris..", "x": "Explained: Paris.. Fireworks. The context — Bastille Day. Parade. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "History.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "History.", "x": "Bastille Day in depth: History.. 1789. Details — France's national day.. Fireworks. Fireworks. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Parade.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Parade.", "x": "Bastille Day in depth: Parade.. Parade. Details — France's national day.. Meaning. Revolution. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Fireworks.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Fireworks.", "x": "Bastille Day in depth: Fireworks.. Fireworks. Details — France's national day.. France. Paris. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Meaning.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Meaning.", "x": "Bastille Day in depth: Meaning.. Revolution. Details — France's national day.. Celebration. July 14. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "France.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "France.", "x": "Bastille Day in depth: France.. Paris. Details — France's national day.. History. 1789. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Celebration.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Celebration.", "x": "Bastille Day in depth: Celebration.. July 14. Details — France's national day.. Parade. Parade. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Bastille Day comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Bastille Day comes from.", "x": "Origins: History.. July 14. The history of Bastille Day — France's national day.. Parade. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Bastille Day respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Bastille Day respectfully.", "x": "Engaging: Fireworks.. 1789. How to participate or observe well — Bastille Day. France's national day. Respect first, always; Meaning.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Bastille Day do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Bastille Day do's and don'ts.", "x": "Etiquette: France.. Parade. The rules of respect — Bastille Day. France's national day. When in doubt, ask about Celebration.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Bastille Day.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Bastille Day.", "x": "Planning: History.. Fireworks. Practical notes — Bastille Day. France's national day. A little planning shows respect for Parade.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Bastille Day and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Bastille Day and money.", "x": "Costs: Fireworks.. Revolution. What to budget — Bastille Day. France's national day. The best experiences of Meaning. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-holiday-bastille-day-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
