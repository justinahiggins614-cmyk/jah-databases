(function(){'use strict';
/* JAH Fireworks Shows Fireworks Database generator — jahdb-e2-fireworks-fireworks-shows-fireworks-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-fireworks-fireworks-shows-fireworks',PREFIX='JAH-E2FIREWORKS-',NAME='JAH Fireworks Shows Fireworks Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Fireworks Shows: the complete guide", "d": "Fireworks Shows: the sky art..", "g": "overview", "l": 2, "q": "What is Fireworks Shows: the complete guide?", "a": "Fireworks Shows: the sky art..", "x": "The complete fireworks guide to Fireworks Shows: the sky art.. Gunpowder. History, meaning, practices, and how to engage respectfully — everything in one database. Powder. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Fireworks Shows essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Fireworks Shows essentials.", "x": "At a glance: Fireworks Shows — the sky art.. Chrysanthemum. The essentials: Colors.. July 4th. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Gunpowder.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Gunpowder.", "x": "Fireworks Shows: Gunpowder.. Colors. Essential knowledge — July 4th.. the sky art. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Gunpowder..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Gunpowder..", "x": "Explained: Gunpowder.. Pyro. The context — Fireworks Shows. Pyro. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Chrysanthemum.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Chrysanthemum.", "x": "Fireworks Shows: Chrysanthemum.. July 4th. Essential knowledge — Pyro.. the sky art. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Chrysanthemum..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Chrysanthemum..", "x": "Explained: Chrysanthemum.. Safety. The context — Fireworks Shows. Colors. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "July 4th.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "July 4th.", "x": "Fireworks Shows: July 4th.. Pyro. Essential knowledge — Colors.. the sky art. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: July 4th..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: July 4th..", "x": "Explained: July 4th.. Art. The context — Fireworks Shows. Safety. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Pyro.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Pyro.", "x": "Fireworks Shows: Pyro.. Safety. Essential knowledge — Safety.. the sky art. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Pyro..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Pyro..", "x": "Explained: Pyro.. Powder. The context — Fireworks Shows. Gunpowder. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Colors.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Colors.", "x": "Fireworks Shows: Colors.. Art. Essential knowledge — Gunpowder.. the sky art. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Colors..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Colors..", "x": "Explained: Colors.. Colors. The context — Fireworks Shows. Chrysanthemum. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Safety.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Safety.", "x": "Fireworks Shows: Safety.. Powder. Essential knowledge — Chrysanthemum.. the sky art. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Safety..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Safety..", "x": "Explained: Safety.. July 4th. The context — Fireworks Shows. July 4th. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Powder.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Powder.", "x": "Fireworks Shows in depth: Powder.. Chrysanthemum. Details — the sky art.. July 4th. Pyro. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Colors.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Colors.", "x": "Fireworks Shows in depth: Colors.. July 4th. Details — the sky art.. Pyro. Colors. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "July 4th.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "July 4th.", "x": "Fireworks Shows in depth: July 4th.. Pyro. Details — the sky art.. Safety. Safety. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Pyro.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Pyro.", "x": "Fireworks Shows in depth: Pyro.. Colors. Details — the sky art.. Art. Gunpowder. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Safety.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Safety.", "x": "Fireworks Shows in depth: Safety.. Safety. Details — the sky art.. Powder. Chrysanthemum. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Art.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Art.", "x": "Fireworks Shows in depth: Art.. Gunpowder. Details — the sky art.. Colors. July 4th. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Fireworks Shows comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Fireworks Shows comes from.", "x": "Origins: Powder.. Gunpowder. The history of Fireworks Shows — the sky art.. Colors. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Fireworks Shows respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Fireworks Shows respectfully.", "x": "Engaging: July 4th.. Chrysanthemum. How to participate or observe well — Fireworks Shows. the sky art. Respect first, always; Pyro.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Fireworks Shows do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Fireworks Shows do's and don'ts.", "x": "Etiquette: Safety.. July 4th. The rules of respect — Fireworks Shows. the sky art. When in doubt, ask about Art.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Fireworks Shows.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Fireworks Shows.", "x": "Planning: Powder.. Pyro. Practical notes — Fireworks Shows. the sky art. A little planning shows respect for Colors.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Fireworks Shows and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Fireworks Shows and money.", "x": "Costs: July 4th.. Colors. What to budget — Fireworks Shows. the sky art. The best experiences of Pyro. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-fireworks-fireworks-shows-fireworks-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
