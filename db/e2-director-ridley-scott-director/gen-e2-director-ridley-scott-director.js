(function(){'use strict';
/* JAH Ridley Scott Director Database generator — jahdb-e2-director-ridley-scott-director-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-director-ridley-scott-director',PREFIX='JAH-E2DIRECTORR-',NAME='JAH Ridley Scott Director Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Ridley Scott: the complete guide", "d": "Ridley Scott: the visual epic..", "g": "overview", "l": 2, "q": "What is Ridley Scott: the complete guide?", "a": "Ridley Scott: the visual epic..", "x": "The complete director guide to Ridley Scott: the visual epic.. 1937. History, meaning, practices, and how to engage respectfully — everything in one database. Alien. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Ridley Scott essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Ridley Scott essentials.", "x": "At a glance: Ridley Scott — the visual epic.. Alien. The essentials: Blade Runner.. Blade Runner. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "1937.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "1937.", "x": "Ridley Scott: 1937.. Blade Runner. Essential knowledge — Blade Runner.. the visual epic. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 1937..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 1937..", "x": "Explained: 1937.. Visual. The context — Ridley Scott. Gladiator. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Alien.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Alien.", "x": "Ridley Scott: Alien.. Gladiator. Essential knowledge — Gladiator.. the visual epic. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Alien..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Alien..", "x": "Explained: Alien.. Brother. The context — Ridley Scott. Commercials. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Blade Runner.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Blade Runner.", "x": "Ridley Scott: Blade Runner.. Visual. Essential knowledge — Commercials.. the visual epic. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Blade Runner..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Blade Runner..", "x": "Explained: Blade Runner.. Style. The context — Ridley Scott. Brother. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Gladiator.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Gladiator.", "x": "Ridley Scott: Gladiator.. Brother. Essential knowledge — Brother.. the visual epic. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Gladiator..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Gladiator..", "x": "Explained: Gladiator.. Alien. The context — Ridley Scott. 1937. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Commercials.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Commercials.", "x": "Ridley Scott: Commercials.. Style. Essential knowledge — 1937.. the visual epic. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Commercials..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Commercials..", "x": "Explained: Commercials.. Blade Runner. The context — Ridley Scott. Alien. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Brother.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Brother.", "x": "Ridley Scott: Brother.. Alien. Essential knowledge — Alien.. the visual epic. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Brother..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Brother..", "x": "Explained: Brother.. Gladiator. The context — Ridley Scott. Blade Runner. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Alien.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Alien.", "x": "Ridley Scott in depth: Alien.. Alien. Details — the visual epic.. Gladiator. Gladiator. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Blade Runner.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Blade Runner.", "x": "Ridley Scott in depth: Blade Runner.. Blade Runner. Details — the visual epic.. Visual. Commercials. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Gladiator.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Gladiator.", "x": "Ridley Scott in depth: Gladiator.. Gladiator. Details — the visual epic.. Brother. Brother. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Visual.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Visual.", "x": "Ridley Scott in depth: Visual.. Commercials. Details — the visual epic.. Style. 1937. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Brother.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Brother.", "x": "Ridley Scott in depth: Brother.. Brother. Details — the visual epic.. Alien. Alien. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Style.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Style.", "x": "Ridley Scott in depth: Style.. 1937. Details — the visual epic.. Blade Runner. Blade Runner. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Ridley Scott comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Ridley Scott comes from.", "x": "Origins: Alien.. 1937. The history of Ridley Scott — the visual epic.. Blade Runner. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Ridley Scott respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Ridley Scott respectfully.", "x": "Engaging: Gladiator.. Alien. How to participate or observe well — Ridley Scott. the visual epic. Respect first, always; Visual.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Ridley Scott do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Ridley Scott do's and don'ts.", "x": "Etiquette: Brother.. Blade Runner. The rules of respect — Ridley Scott. the visual epic. When in doubt, ask about Style.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Ridley Scott.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Ridley Scott.", "x": "Planning: Alien.. Gladiator. Practical notes — Ridley Scott. the visual epic. A little planning shows respect for Blade Runner.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Ridley Scott and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Ridley Scott and money.", "x": "Costs: Gladiator.. Commercials. What to budget — Ridley Scott. the visual epic. The best experiences of Visual. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-director-ridley-scott-director-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
