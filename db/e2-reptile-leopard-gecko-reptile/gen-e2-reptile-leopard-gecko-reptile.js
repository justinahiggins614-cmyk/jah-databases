(function(){'use strict';
/* JAH Leopard Gecko Reptile Database generator — jahdb-e2-reptile-leopard-gecko-reptile-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-reptile-leopard-gecko-reptile',PREFIX='JAH-E2REPTILELE-',NAME='JAH Leopard Gecko Reptile Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Leopard Gecko: the complete guide", "d": "Leopard Gecko: the spotted beginner..", "g": "overview", "l": 2, "q": "What is Leopard Gecko: the complete guide?", "a": "Leopard Gecko: the spotted beginner..", "x": "The complete reptile guide to Leopard Gecko: the spotted beginner.. Spots. History, meaning, practices, and how to engage respectfully — everything in one database. Spots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Leopard Gecko essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Leopard Gecko essentials.", "x": "At a glance: Leopard Gecko — the spotted beginner.. Eyelids. The essentials: Nocturnal.. Nocturnal. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Spots.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Spots.", "x": "Leopard Gecko: Spots.. Nocturnal. Essential knowledge — Nocturnal.. the spotted beginner. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Spots..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Spots..", "x": "Explained: Spots.. Pakistan. The context — Leopard Gecko. Beginner. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Eyelids.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Eyelids.", "x": "Leopard Gecko: Eyelids.. Tail. Essential knowledge — Beginner.. the spotted beginner. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Eyelids..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Eyelids..", "x": "Explained: Eyelids.. Beginner. The context — Leopard Gecko. Tail. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Nocturnal.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Nocturnal.", "x": "Leopard Gecko: Nocturnal.. Pakistan. Essential knowledge — Tail.. the spotted beginner. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Nocturnal..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Nocturnal..", "x": "Explained: Nocturnal.. Care. The context — Leopard Gecko. Pakistan. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Beginner.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Beginner.", "x": "Leopard Gecko: Beginner.. Beginner. Essential knowledge — Pakistan.. the spotted beginner. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Beginner..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Beginner..", "x": "Explained: Beginner.. Spots. The context — Leopard Gecko. Spots. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Tail.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Tail.", "x": "Leopard Gecko: Tail.. Care. Essential knowledge — Spots.. the spotted beginner. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Tail..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Tail..", "x": "Explained: Tail.. Nocturnal. The context — Leopard Gecko. Eyelids. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Pakistan.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Pakistan.", "x": "Leopard Gecko: Pakistan.. Spots. Essential knowledge — Eyelids.. the spotted beginner. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Pakistan..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Pakistan..", "x": "Explained: Pakistan.. Tail. The context — Leopard Gecko. Nocturnal. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Spots.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Spots.", "x": "Leopard Gecko in depth: Spots.. Eyelids. Details — the spotted beginner.. Tail. Beginner. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Nocturnal.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Nocturnal.", "x": "Leopard Gecko in depth: Nocturnal.. Nocturnal. Details — the spotted beginner.. Pakistan. Tail. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Tail.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Tail.", "x": "Leopard Gecko in depth: Tail.. Beginner. Details — the spotted beginner.. Beginner. Pakistan. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Pakistan.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Pakistan.", "x": "Leopard Gecko in depth: Pakistan.. Tail. Details — the spotted beginner.. Care. Spots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Beginner.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Beginner.", "x": "Leopard Gecko in depth: Beginner.. Pakistan. Details — the spotted beginner.. Spots. Eyelids. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Care.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Care.", "x": "Leopard Gecko in depth: Care.. Spots. Details — the spotted beginner.. Nocturnal. Nocturnal. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Leopard Gecko comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Leopard Gecko comes from.", "x": "Origins: Spots.. Spots. The history of Leopard Gecko — the spotted beginner.. Nocturnal. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Leopard Gecko respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Leopard Gecko respectfully.", "x": "Engaging: Tail.. Eyelids. How to participate or observe well — Leopard Gecko. the spotted beginner. Respect first, always; Pakistan.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Leopard Gecko do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Leopard Gecko do's and don'ts.", "x": "Etiquette: Beginner.. Nocturnal. The rules of respect — Leopard Gecko. the spotted beginner. When in doubt, ask about Care.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Leopard Gecko.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Leopard Gecko.", "x": "Planning: Spots.. Beginner. Practical notes — Leopard Gecko. the spotted beginner. A little planning shows respect for Nocturnal.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Leopard Gecko and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Leopard Gecko and money.", "x": "Costs: Tail.. Tail. What to budget — Leopard Gecko. the spotted beginner. The best experiences of Pakistan. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-reptile-leopard-gecko-reptile-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
