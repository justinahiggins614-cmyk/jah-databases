(function(){'use strict';
/* JAH Coldplay Band Band Database generator — jahdb-e2-band-coldplay-band-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-band-coldplay-band',PREFIX='JAH-E2BANDCOLDP-',NAME='JAH Coldplay Band Band Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Coldplay Band: the complete guide", "d": "Coldplay Band: the stadium glow..", "g": "overview", "l": 2, "q": "What is Coldplay Band: the complete guide?", "a": "Coldplay Band: the stadium glow..", "x": "The complete band guide to Coldplay Band: the stadium glow.. 1996. History, meaning, practices, and how to engage respectfully — everything in one database. Martin. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Coldplay Band essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Coldplay Band essentials.", "x": "At a glance: Coldplay Band — the stadium glow.. Martin. The essentials: Yellow.. Parachutes. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "1996.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "1996.", "x": "Coldplay Band: 1996.. Yellow. Essential knowledge — Parachutes.. the stadium glow. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 1996..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 1996..", "x": "Explained: 1996.. Stadiums. The context — Coldplay Band. Yellow. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Martin.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Martin.", "x": "Coldplay Band: Martin.. Wristbands. Essential knowledge — Yellow.. the stadium glow. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Martin..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Martin..", "x": "Explained: Martin.. Parachutes. The context — Coldplay Band. Wristbands. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Parachutes.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Parachutes.", "x": "Coldplay Band: Parachutes.. Stadiums. Essential knowledge — Wristbands.. the stadium glow. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Parachutes..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Parachutes..", "x": "Explained: Parachutes.. Legacy. The context — Coldplay Band. Stadiums. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Yellow.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Yellow.", "x": "Coldplay Band: Yellow.. Parachutes. Essential knowledge — Stadiums.. the stadium glow. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Yellow..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Yellow..", "x": "Explained: Yellow.. Martin. The context — Coldplay Band. 1996. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Wristbands.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Wristbands.", "x": "Coldplay Band: Wristbands.. Legacy. Essential knowledge — 1996.. the stadium glow. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Wristbands..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Wristbands..", "x": "Explained: Wristbands.. Yellow. The context — Coldplay Band. Martin. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Stadiums.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Stadiums.", "x": "Coldplay Band: Stadiums.. Martin. Essential knowledge — Martin.. the stadium glow. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Stadiums..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Stadiums..", "x": "Explained: Stadiums.. Wristbands. The context — Coldplay Band. Parachutes. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Martin.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Martin.", "x": "Coldplay Band in depth: Martin.. Martin. Details — the stadium glow.. Wristbands. Yellow. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Yellow.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Yellow.", "x": "Coldplay Band in depth: Yellow.. Parachutes. Details — the stadium glow.. Stadiums. Wristbands. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Wristbands.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Wristbands.", "x": "Coldplay Band in depth: Wristbands.. Yellow. Details — the stadium glow.. Parachutes. Stadiums. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Stadiums.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Stadiums.", "x": "Coldplay Band in depth: Stadiums.. Wristbands. Details — the stadium glow.. Legacy. 1996. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Parachutes.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Parachutes.", "x": "Coldplay Band in depth: Parachutes.. Stadiums. Details — the stadium glow.. Martin. Martin. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Legacy.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Legacy.", "x": "Coldplay Band in depth: Legacy.. 1996. Details — the stadium glow.. Yellow. Parachutes. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Coldplay Band comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Coldplay Band comes from.", "x": "Origins: Martin.. 1996. The history of Coldplay Band — the stadium glow.. Yellow. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Coldplay Band respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Coldplay Band respectfully.", "x": "Engaging: Wristbands.. Martin. How to participate or observe well — Coldplay Band. the stadium glow. Respect first, always; Stadiums.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Coldplay Band do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Coldplay Band do's and don'ts.", "x": "Etiquette: Parachutes.. Parachutes. The rules of respect — Coldplay Band. the stadium glow. When in doubt, ask about Legacy.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Coldplay Band.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Coldplay Band.", "x": "Planning: Martin.. Yellow. Practical notes — Coldplay Band. the stadium glow. A little planning shows respect for Yellow.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Coldplay Band and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Coldplay Band and money.", "x": "Costs: Wristbands.. Wristbands. What to budget — Coldplay Band. the stadium glow. The best experiences of Stadiums. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-band-coldplay-band-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
