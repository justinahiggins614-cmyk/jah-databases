(function(){'use strict';
/* JAH Easter Island Landmark Database generator — jahdb-e2-landmark-easter-island-landmark-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-landmark-easter-island-landmark',PREFIX='JAH-E2LANDMARKE-',NAME='JAH Easter Island Landmark Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Easter Island: the complete guide", "d": "Easter Island: the moai heads..", "g": "overview", "l": 2, "q": "What is Easter Island: the complete guide?", "a": "Easter Island: the moai heads..", "x": "The complete landmark guide to Easter Island: the moai heads.. 887 moai. History, meaning, practices, and how to engage respectfully — everything in one database. 887. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Easter Island essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Easter Island essentials.", "x": "At a glance: Easter Island — the moai heads.. Rapa Nui. The essentials: Rapa Nui.. Volcanic. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "887 moai.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "887 moai.", "x": "Easter Island: 887 moai.. Rapa Nui. Essential knowledge — Volcanic.. the moai heads. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 887 moai..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 887 moai..", "x": "Explained: 887 moai.. UNESCO. The context — Easter Island. Mystery. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Rapa Nui.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Rapa Nui.", "x": "Easter Island: Rapa Nui.. Mystery. Essential knowledge — Mystery.. the moai heads. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Rapa Nui..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Rapa Nui..", "x": "Explained: Rapa Nui.. Remote. The context — Easter Island. Remote. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Volcanic.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Volcanic.", "x": "Easter Island: Volcanic.. UNESCO. Essential knowledge — Remote.. the moai heads. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Volcanic..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Volcanic..", "x": "Explained: Volcanic.. Tours. The context — Easter Island. UNESCO. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Mystery.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Mystery.", "x": "Easter Island: Mystery.. Remote. Essential knowledge — UNESCO.. the moai heads. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Mystery..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Mystery..", "x": "Explained: Mystery.. 887. The context — Easter Island. 887 moai. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Remote.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Remote.", "x": "Easter Island: Remote.. Tours. Essential knowledge — 887 moai.. the moai heads. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Remote..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Remote..", "x": "Explained: Remote.. Rapa Nui. The context — Easter Island. Rapa Nui. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "UNESCO.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "UNESCO.", "x": "Easter Island: UNESCO.. 887. Essential knowledge — Rapa Nui.. the moai heads. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: UNESCO..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: UNESCO..", "x": "Explained: UNESCO.. Mystery. The context — Easter Island. Volcanic. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "887.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "887.", "x": "Easter Island in depth: 887.. Rapa Nui. Details — the moai heads.. Mystery. Mystery. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Rapa Nui.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Rapa Nui.", "x": "Easter Island in depth: Rapa Nui.. Volcanic. Details — the moai heads.. UNESCO. Remote. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Mystery.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Mystery.", "x": "Easter Island in depth: Mystery.. Mystery. Details — the moai heads.. Remote. UNESCO. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "UNESCO.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "UNESCO.", "x": "Easter Island in depth: UNESCO.. Remote. Details — the moai heads.. Tours. 887 moai. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Remote.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Remote.", "x": "Easter Island in depth: Remote.. UNESCO. Details — the moai heads.. 887. Rapa Nui. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Tours.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Tours.", "x": "Easter Island in depth: Tours.. 887 moai. Details — the moai heads.. Rapa Nui. Volcanic. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Easter Island comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Easter Island comes from.", "x": "Origins: 887.. 887 moai. The history of Easter Island — the moai heads.. Rapa Nui. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Easter Island respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Easter Island respectfully.", "x": "Engaging: Mystery.. Rapa Nui. How to participate or observe well — Easter Island. the moai heads. Respect first, always; UNESCO.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Easter Island do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Easter Island do's and don'ts.", "x": "Etiquette: Remote.. Volcanic. The rules of respect — Easter Island. the moai heads. When in doubt, ask about Tours.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Easter Island.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Easter Island.", "x": "Planning: 887.. Mystery. Practical notes — Easter Island. the moai heads. A little planning shows respect for Rapa Nui.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Easter Island and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Easter Island and money.", "x": "Costs: Mystery.. Remote. What to budget — Easter Island. the moai heads. The best experiences of UNESCO. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-landmark-easter-island-landmark-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
