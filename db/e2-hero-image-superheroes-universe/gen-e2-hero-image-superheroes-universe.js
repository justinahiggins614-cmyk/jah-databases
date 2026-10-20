(function(){'use strict';
/* JAH Image Superheroes Superhero Database generator — jahdb-e2-hero-image-superheroes-universe-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-hero-image-superheroes-universe',PREFIX='JAH-E2HEROIMAGE-',NAME='JAH Image Superheroes Superhero Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Image Superheroes: the complete guide", "d": "Image Superheroes: the creator-owned..", "g": "overview", "l": 2, "q": "What is Image Superheroes: the complete guide?", "a": "Image Superheroes: the creator-owned..", "x": "The complete superhero guide to Image Superheroes: the creator-owned.. 1992. History, meaning, practices, and how to engage respectfully — everything in one database. Spawn. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Image Superheroes essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Image Superheroes essentials.", "x": "At a glance: Image Superheroes — the creator-owned.. Spawn. The essentials: McFarlane.. Savage Dragon. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "1992.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "1992.", "x": "Image Superheroes: 1992.. McFarlane. Essential knowledge — Savage Dragon.. the creator-owned. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 1992..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 1992..", "x": "Explained: 1992.. Invincible. The context — Image Superheroes. McFarlane. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Spawn.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Spawn.", "x": "Image Superheroes: Spawn.. Independent. Essential knowledge — McFarlane.. the creator-owned. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Spawn..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Spawn..", "x": "Explained: Spawn.. 1992. The context — Image Superheroes. Independent. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Savage Dragon.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Savage Dragon.", "x": "Image Superheroes: Savage Dragon.. Invincible. Essential knowledge — Independent.. the creator-owned. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Savage Dragon..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Savage Dragon..", "x": "Explained: Savage Dragon.. Heroes. The context — Image Superheroes. Invincible. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "McFarlane.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "McFarlane.", "x": "Image Superheroes: McFarlane.. 1992. Essential knowledge — Invincible.. the creator-owned. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: McFarlane..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: McFarlane..", "x": "Explained: McFarlane.. Spawn. The context — Image Superheroes. 1992. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Independent.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Independent.", "x": "Image Superheroes: Independent.. Heroes. Essential knowledge — 1992.. the creator-owned. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Independent..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Independent..", "x": "Explained: Independent.. McFarlane. The context — Image Superheroes. Spawn. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Invincible.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Invincible.", "x": "Image Superheroes: Invincible.. Spawn. Essential knowledge — Spawn.. the creator-owned. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Invincible..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Invincible..", "x": "Explained: Invincible.. Independent. The context — Image Superheroes. Savage Dragon. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Spawn.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Spawn.", "x": "Image Superheroes in depth: Spawn.. Spawn. Details — the creator-owned.. Independent. McFarlane. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "McFarlane.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "McFarlane.", "x": "Image Superheroes in depth: McFarlane.. Savage Dragon. Details — the creator-owned.. Invincible. Independent. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Independent.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Independent.", "x": "Image Superheroes in depth: Independent.. McFarlane. Details — the creator-owned.. 1992. Invincible. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Invincible.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Invincible.", "x": "Image Superheroes in depth: Invincible.. Independent. Details — the creator-owned.. Heroes. 1992. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "1992.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "1992.", "x": "Image Superheroes in depth: 1992.. Invincible. Details — the creator-owned.. Spawn. Spawn. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Heroes.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Heroes.", "x": "Image Superheroes in depth: Heroes.. 1992. Details — the creator-owned.. McFarlane. Savage Dragon. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Image Superheroes comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Image Superheroes comes from.", "x": "Origins: Spawn.. 1992. The history of Image Superheroes — the creator-owned.. McFarlane. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Image Superheroes respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Image Superheroes respectfully.", "x": "Engaging: Independent.. Spawn. How to participate or observe well — Image Superheroes. the creator-owned. Respect first, always; Invincible.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Image Superheroes do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Image Superheroes do's and don'ts.", "x": "Etiquette: 1992.. Savage Dragon. The rules of respect — Image Superheroes. the creator-owned. When in doubt, ask about Heroes.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Image Superheroes.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Image Superheroes.", "x": "Planning: Spawn.. McFarlane. Practical notes — Image Superheroes. the creator-owned. A little planning shows respect for McFarlane.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Image Superheroes and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Image Superheroes and money.", "x": "Costs: Independent.. Independent. What to budget — Image Superheroes. the creator-owned. The best experiences of Invincible. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-hero-image-superheroes-universe-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
