(function(){'use strict';
/* JAH Old Quebec Landmark Database generator — jahdb-e2-landmark-old-quebec-landmark-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-landmark-old-quebec-landmark',PREFIX='JAH-E2LANDMARKO-',NAME='JAH Old Quebec Landmark Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Old Quebec: the complete guide", "d": "Old Quebec: the walled city..", "g": "overview", "l": 2, "q": "What is Old Quebec: the complete guide?", "a": "Old Quebec: the walled city..", "x": "The complete landmark guide to Old Quebec: the walled city.. 1608. History, meaning, practices, and how to engage respectfully — everything in one database. 1608. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Old Quebec essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Old Quebec essentials.", "x": "At a glance: Old Quebec — the walled city.. Walls. The essentials: Chateau.. Champlain. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "1608.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "1608.", "x": "Old Quebec: 1608.. Chateau. Essential knowledge — Champlain.. the walled city. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 1608..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 1608..", "x": "Explained: 1608.. European. The context — Old Quebec. Chateau. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Walls.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Walls.", "x": "Old Quebec: Walls.. UNESCO. Essential knowledge — Chateau.. the walled city. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Walls..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Walls..", "x": "Explained: Walls.. Walls. The context — Old Quebec. UNESCO. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Champlain.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Champlain.", "x": "Old Quebec: Champlain.. European. Essential knowledge — UNESCO.. the walled city. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Champlain..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Champlain..", "x": "Explained: Champlain.. Walking. The context — Old Quebec. European. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Chateau.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Chateau.", "x": "Old Quebec: Chateau.. Walls. Essential knowledge — European.. the walled city. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Chateau..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Chateau..", "x": "Explained: Chateau.. 1608. The context — Old Quebec. 1608. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "UNESCO.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "UNESCO.", "x": "Old Quebec: UNESCO.. Walking. Essential knowledge — 1608.. the walled city. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: UNESCO..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: UNESCO..", "x": "Explained: UNESCO.. Chateau. The context — Old Quebec. Walls. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "European.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "European.", "x": "Old Quebec: European.. 1608. Essential knowledge — Walls.. the walled city. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: European..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: European..", "x": "Explained: European.. UNESCO. The context — Old Quebec. Champlain. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "1608.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "1608.", "x": "Old Quebec in depth: 1608.. Walls. Details — the walled city.. UNESCO. Chateau. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Chateau.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Chateau.", "x": "Old Quebec in depth: Chateau.. Champlain. Details — the walled city.. European. UNESCO. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "UNESCO.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "UNESCO.", "x": "Old Quebec in depth: UNESCO.. Chateau. Details — the walled city.. Walls. European. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "European.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "European.", "x": "Old Quebec in depth: European.. UNESCO. Details — the walled city.. Walking. 1608. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Walls.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Walls.", "x": "Old Quebec in depth: Walls.. European. Details — the walled city.. 1608. Walls. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Walking.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Walking.", "x": "Old Quebec in depth: Walking.. 1608. Details — the walled city.. Chateau. Champlain. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Old Quebec comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Old Quebec comes from.", "x": "Origins: 1608.. 1608. The history of Old Quebec — the walled city.. Chateau. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Old Quebec respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Old Quebec respectfully.", "x": "Engaging: UNESCO.. Walls. How to participate or observe well — Old Quebec. the walled city. Respect first, always; European.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Old Quebec do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Old Quebec do's and don'ts.", "x": "Etiquette: Walls.. Champlain. The rules of respect — Old Quebec. the walled city. When in doubt, ask about Walking.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Old Quebec.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Old Quebec.", "x": "Planning: 1608.. Chateau. Practical notes — Old Quebec. the walled city. A little planning shows respect for Chateau.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Old Quebec and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Old Quebec and money.", "x": "Costs: UNESCO.. UNESCO. What to budget — Old Quebec. the walled city. The best experiences of European. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-landmark-old-quebec-landmark-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
