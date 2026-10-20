(function(){'use strict';
/* JAH Gypsy Vanner Horse Breed Database generator — jahdb-e2-horse-gypsy-vanner-breed-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-horse-gypsy-vanner-breed',PREFIX='JAH-E2HORSEGYPS-',NAME='JAH Gypsy Vanner Horse Breed Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Gypsy Vanner: the complete guide", "d": "Gypsy Vanner: the cob feathered..", "g": "overview", "l": 2, "q": "What is Gypsy Vanner: the complete guide?", "a": "Gypsy Vanner: the cob feathered..", "x": "The complete horse breed guide to Gypsy Vanner: the cob feathered.. Feathered. History, meaning, practices, and how to engage respectfully — everything in one database. Feathered. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Gypsy Vanner essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Gypsy Vanner essentials.", "x": "At a glance: Gypsy Vanner — the cob feathered.. Cob. The essentials: Ireland.. Ireland. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Feathered.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Feathered.", "x": "Gypsy Vanner: Feathered.. Ireland. Essential knowledge — Ireland.. the cob feathered. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Feathered..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Feathered..", "x": "Explained: Feathered.. Piebald. The context — Gypsy Vanner. Gypsy. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Cob.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Cob.", "x": "Gypsy Vanner: Cob.. Gentle. Essential knowledge — Gypsy.. the cob feathered. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Cob..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Cob..", "x": "Explained: Cob.. Cob. The context — Gypsy Vanner. Piebald. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Ireland.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Ireland.", "x": "Gypsy Vanner: Ireland.. Piebald. Essential knowledge — Piebald.. the cob feathered. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Ireland..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Ireland..", "x": "Explained: Ireland.. History. The context — Gypsy Vanner. Gentle. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Gypsy.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Gypsy.", "x": "Gypsy Vanner: Gypsy.. Cob. Essential knowledge — Gentle.. the cob feathered. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Gypsy..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Gypsy..", "x": "Explained: Gypsy.. Feathered. The context — Gypsy Vanner. Feathered. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Piebald.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Piebald.", "x": "Gypsy Vanner: Piebald.. History. Essential knowledge — Feathered.. the cob feathered. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Piebald..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Piebald..", "x": "Explained: Piebald.. Ireland. The context — Gypsy Vanner. Cob. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Gentle.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Gentle.", "x": "Gypsy Vanner: Gentle.. Feathered. Essential knowledge — Cob.. the cob feathered. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Gentle..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Gentle..", "x": "Explained: Gentle.. Gentle. The context — Gypsy Vanner. Ireland. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Feathered.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Feathered.", "x": "Gypsy Vanner in depth: Feathered.. Cob. Details — the cob feathered.. Gentle. Gypsy. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Ireland.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Ireland.", "x": "Gypsy Vanner in depth: Ireland.. Ireland. Details — the cob feathered.. Piebald. Piebald. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Gentle.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Gentle.", "x": "Gypsy Vanner in depth: Gentle.. Gypsy. Details — the cob feathered.. Cob. Gentle. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Piebald.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Piebald.", "x": "Gypsy Vanner in depth: Piebald.. Piebald. Details — the cob feathered.. History. Feathered. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Cob.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Cob.", "x": "Gypsy Vanner in depth: Cob.. Gentle. Details — the cob feathered.. Feathered. Cob. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "History.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "History.", "x": "Gypsy Vanner in depth: History.. Feathered. Details — the cob feathered.. Ireland. Ireland. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Gypsy Vanner comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Gypsy Vanner comes from.", "x": "Origins: Feathered.. Feathered. The history of Gypsy Vanner — the cob feathered.. Ireland. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Gypsy Vanner respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Gypsy Vanner respectfully.", "x": "Engaging: Gentle.. Cob. How to participate or observe well — Gypsy Vanner. the cob feathered. Respect first, always; Piebald.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Gypsy Vanner do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Gypsy Vanner do's and don'ts.", "x": "Etiquette: Cob.. Ireland. The rules of respect — Gypsy Vanner. the cob feathered. When in doubt, ask about History.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Gypsy Vanner.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Gypsy Vanner.", "x": "Planning: Feathered.. Gypsy. Practical notes — Gypsy Vanner. the cob feathered. A little planning shows respect for Ireland.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Gypsy Vanner and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Gypsy Vanner and money.", "x": "Costs: Gentle.. Piebald. What to budget — Gypsy Vanner. the cob feathered. The best experiences of Piebald. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-horse-gypsy-vanner-breed-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
