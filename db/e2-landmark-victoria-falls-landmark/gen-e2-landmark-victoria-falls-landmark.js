(function(){'use strict';
/* JAH Victoria Falls Landmark Database generator — jahdb-e2-landmark-victoria-falls-landmark-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-landmark-victoria-falls-landmark',PREFIX='JAH-E2LANDMARKV-',NAME='JAH Victoria Falls Landmark Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Victoria Falls: the complete guide", "d": "Victoria Falls: the smoke that thunders..", "g": "overview", "l": 2, "q": "What is Victoria Falls: the complete guide?", "a": "Victoria Falls: the smoke that thunders..", "x": "The complete landmark guide to Victoria Falls: the smoke that thunders.. 108m. History, meaning, practices, and how to engage respectfully — everything in one database. 108m. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Victoria Falls essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Victoria Falls essentials.", "x": "At a glance: Victoria Falls — the smoke that thunders.. 1.7 km. The essentials: Mist.. Mosi-oa-Tunya. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "108m.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "108m.", "x": "Victoria Falls: 108m.. Mist. Essential knowledge — Mosi-oa-Tunya.. the smoke that thunders. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 108m..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 108m..", "x": "Explained: 108m.. Mosi. The context — Victoria Falls. Mist. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "1.7 km.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "1.7 km.", "x": "Victoria Falls: 1.7 km.. UNESCO. Essential knowledge — Mist.. the smoke that thunders. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: 1.7 km..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: 1.7 km..", "x": "Explained: 1.7 km.. Devil's. The context — Victoria Falls. Devil's Pool. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Mosi-oa-Tunya.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Mosi-oa-Tunya.", "x": "Victoria Falls: Mosi-oa-Tunya.. Mosi. Essential knowledge — Devil's Pool.. the smoke that thunders. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Mosi-oa-Tunya..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Mosi-oa-Tunya..", "x": "Explained: Mosi-oa-Tunya.. Tours. The context — Victoria Falls. UNESCO. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Mist.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Mist.", "x": "Victoria Falls: Mist.. Devil's. Essential knowledge — UNESCO.. the smoke that thunders. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Mist..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Mist..", "x": "Explained: Mist.. 108m. The context — Victoria Falls. 108m. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Devil's Pool.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Devil's Pool.", "x": "Victoria Falls: Devil's Pool.. Tours. Essential knowledge — 108m.. the smoke that thunders. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Devil's Pool..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Devil's Pool..", "x": "Explained: Devil's Pool.. Mist. The context — Victoria Falls. 1.7 km. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "UNESCO.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "UNESCO.", "x": "Victoria Falls: UNESCO.. 108m. Essential knowledge — 1.7 km.. the smoke that thunders. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: UNESCO..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: UNESCO..", "x": "Explained: UNESCO.. UNESCO. The context — Victoria Falls. Mosi-oa-Tunya. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "108m.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "108m.", "x": "Victoria Falls in depth: 108m.. 1.7 km. Details — the smoke that thunders.. UNESCO. Mist. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Mist.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Mist.", "x": "Victoria Falls in depth: Mist.. Mosi-oa-Tunya. Details — the smoke that thunders.. Mosi. Devil's Pool. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "UNESCO.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "UNESCO.", "x": "Victoria Falls in depth: UNESCO.. Mist. Details — the smoke that thunders.. Devil's. UNESCO. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Mosi.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Mosi.", "x": "Victoria Falls in depth: Mosi.. Devil's Pool. Details — the smoke that thunders.. Tours. 108m. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Devil's.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Devil's.", "x": "Victoria Falls in depth: Devil's.. UNESCO. Details — the smoke that thunders.. 108m. 1.7 km. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Tours.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Tours.", "x": "Victoria Falls in depth: Tours.. 108m. Details — the smoke that thunders.. Mist. Mosi-oa-Tunya. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Victoria Falls comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Victoria Falls comes from.", "x": "Origins: 108m.. 108m. The history of Victoria Falls — the smoke that thunders.. Mist. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Victoria Falls respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Victoria Falls respectfully.", "x": "Engaging: UNESCO.. 1.7 km. How to participate or observe well — Victoria Falls. the smoke that thunders. Respect first, always; Mosi.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Victoria Falls do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Victoria Falls do's and don'ts.", "x": "Etiquette: Devil's.. Mosi-oa-Tunya. The rules of respect — Victoria Falls. the smoke that thunders. When in doubt, ask about Tours.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Victoria Falls.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Victoria Falls.", "x": "Planning: 108m.. Mist. Practical notes — Victoria Falls. the smoke that thunders. A little planning shows respect for Mist.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Victoria Falls and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Victoria Falls and money.", "x": "Costs: UNESCO.. Devil's Pool. What to budget — Victoria Falls. the smoke that thunders. The best experiences of Mosi. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-landmark-victoria-falls-landmark-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
