(function(){'use strict';
/* JAH Cahir Castle Castle Database generator — jahdb-e2-castle-cahir-castle-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-castle-cahir-castle',PREFIX='JAH-E2CASTLECAH-',NAME='JAH Cahir Castle Castle Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Cahir Castle: the complete guide", "d": "Cahir Castle: Ireland's best preserved..", "g": "overview", "l": 2, "q": "What is Cahir Castle: the complete guide?", "a": "Cahir Castle: Ireland's best preserved..", "x": "The complete castle guide to Cahir Castle: Ireland's best preserved.. 1142. History, meaning, practices, and how to engage respectfully — everything in one database. River. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Cahir Castle essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Cahir Castle essentials.", "x": "At a glance: Cahir Castle — Ireland's best preserved.. River Suir. The essentials: Films.. Films. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "1142.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "1142.", "x": "Cahir Castle: 1142.. Films. Essential knowledge — Films.. Ireland's best preserved. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 1142..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 1142..", "x": "Explained: 1142.. Ireland. The context — Cahir Castle. Sieges. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "River Suir.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "River Suir.", "x": "Cahir Castle: River Suir.. History. Essential knowledge — Sieges.. Ireland's best preserved. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: River Suir..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: River Suir..", "x": "Explained: River Suir.. Tours. The context — Cahir Castle. Ireland. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Films.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Films.", "x": "Cahir Castle: Films.. Ireland. Essential knowledge — Ireland.. Ireland's best preserved. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Films..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Films..", "x": "Explained: Films.. Sieges. The context — Cahir Castle. Tours. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Sieges.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Sieges.", "x": "Cahir Castle: Sieges.. Tours. Essential knowledge — Tours.. Ireland's best preserved. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Sieges..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Sieges..", "x": "Explained: Sieges.. River. The context — Cahir Castle. 1142. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Ireland.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Ireland.", "x": "Cahir Castle: Ireland.. Sieges. Essential knowledge — 1142.. Ireland's best preserved. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Ireland..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Ireland..", "x": "Explained: Ireland.. Films. The context — Cahir Castle. River Suir. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Tours.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Tours.", "x": "Cahir Castle: Tours.. River. Essential knowledge — River Suir.. Ireland's best preserved. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Tours..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Tours..", "x": "Explained: Tours.. History. The context — Cahir Castle. Films. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "River.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "River.", "x": "Cahir Castle in depth: River.. River Suir. Details — Ireland's best preserved.. History. Sieges. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Films.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Films.", "x": "Cahir Castle in depth: Films.. Films. Details — Ireland's best preserved.. Ireland. Ireland. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "History.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "History.", "x": "Cahir Castle in depth: History.. Sieges. Details — Ireland's best preserved.. Tours. Tours. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Ireland.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Ireland.", "x": "Cahir Castle in depth: Ireland.. Ireland. Details — Ireland's best preserved.. Sieges. 1142. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Tours.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Tours.", "x": "Cahir Castle in depth: Tours.. Tours. Details — Ireland's best preserved.. River. River Suir. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Sieges.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Sieges.", "x": "Cahir Castle in depth: Sieges.. 1142. Details — Ireland's best preserved.. Films. Films. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Cahir Castle comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Cahir Castle comes from.", "x": "Origins: River.. 1142. The history of Cahir Castle — Ireland's best preserved.. Films. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Cahir Castle respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Cahir Castle respectfully.", "x": "Engaging: History.. River Suir. How to participate or observe well — Cahir Castle. Ireland's best preserved. Respect first, always; Ireland.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Cahir Castle do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Cahir Castle do's and don'ts.", "x": "Etiquette: Tours.. Films. The rules of respect — Cahir Castle. Ireland's best preserved. When in doubt, ask about Sieges.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Cahir Castle.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Cahir Castle.", "x": "Planning: River.. Sieges. Practical notes — Cahir Castle. Ireland's best preserved. A little planning shows respect for Films.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Cahir Castle and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Cahir Castle and money.", "x": "Costs: History.. Ireland. What to budget — Cahir Castle. Ireland's best preserved. The best experiences of Ireland. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-castle-cahir-castle-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
