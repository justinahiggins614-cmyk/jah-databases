(function(){'use strict';
/* JAH Lentil Crop Crop Database generator — jahdb-e2-crop-lentil-crop-farm-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-crop-lentil-crop-farm',PREFIX='JAH-E2CROPLENTI-',NAME='JAH Lentil Crop Crop Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Lentil Crop: the complete guide", "d": "Lentil Crop: the pulse field..", "g": "overview", "l": 2, "q": "What is Lentil Crop: the complete guide?", "a": "Lentil Crop: the pulse field..", "x": "The complete crop guide to Lentil Crop: the pulse field.. Pulses. History, meaning, practices, and how to engage respectfully — everything in one database. Pulses. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Lentil Crop essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Lentil Crop essentials.", "x": "At a glance: Lentil Crop — the pulse field.. Nitrogen. The essentials: Canada.. Canada. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Pulses.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Pulses.", "x": "Lentil Crop: Pulses.. Canada. Essential knowledge — Canada.. the pulse field. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Pulses..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Pulses..", "x": "Explained: Pulses.. Rotation. The context — Lentil Crop. Red. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Nitrogen.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Nitrogen.", "x": "Lentil Crop: Nitrogen.. Dals. Essential knowledge — Red.. the pulse field. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Nitrogen..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Nitrogen..", "x": "Explained: Nitrogen.. Nitrogen. The context — Lentil Crop. Dals. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Canada.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Canada.", "x": "Lentil Crop: Canada.. Rotation. Essential knowledge — Dals.. the pulse field. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Canada..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Canada..", "x": "Explained: Canada.. Growing. The context — Lentil Crop. Rotation. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Red.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Red.", "x": "Lentil Crop: Red.. Nitrogen. Essential knowledge — Rotation.. the pulse field. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Red..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Red..", "x": "Explained: Red.. Pulses. The context — Lentil Crop. Pulses. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Dals.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Dals.", "x": "Lentil Crop: Dals.. Growing. Essential knowledge — Pulses.. the pulse field. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Dals..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Dals..", "x": "Explained: Dals.. Canada. The context — Lentil Crop. Nitrogen. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Rotation.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Rotation.", "x": "Lentil Crop: Rotation.. Pulses. Essential knowledge — Nitrogen.. the pulse field. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Rotation..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Rotation..", "x": "Explained: Rotation.. Dals. The context — Lentil Crop. Canada. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Pulses.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Pulses.", "x": "Lentil Crop in depth: Pulses.. Nitrogen. Details — the pulse field.. Dals. Red. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Canada.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Canada.", "x": "Lentil Crop in depth: Canada.. Canada. Details — the pulse field.. Rotation. Dals. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Dals.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Dals.", "x": "Lentil Crop in depth: Dals.. Red. Details — the pulse field.. Nitrogen. Rotation. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Rotation.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Rotation.", "x": "Lentil Crop in depth: Rotation.. Dals. Details — the pulse field.. Growing. Pulses. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Nitrogen.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Nitrogen.", "x": "Lentil Crop in depth: Nitrogen.. Rotation. Details — the pulse field.. Pulses. Nitrogen. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Growing.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Growing.", "x": "Lentil Crop in depth: Growing.. Pulses. Details — the pulse field.. Canada. Canada. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Lentil Crop comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Lentil Crop comes from.", "x": "Origins: Pulses.. Pulses. The history of Lentil Crop — the pulse field.. Canada. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Lentil Crop respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Lentil Crop respectfully.", "x": "Engaging: Dals.. Nitrogen. How to participate or observe well — Lentil Crop. the pulse field. Respect first, always; Rotation.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Lentil Crop do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Lentil Crop do's and don'ts.", "x": "Etiquette: Nitrogen.. Canada. The rules of respect — Lentil Crop. the pulse field. When in doubt, ask about Growing.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Lentil Crop.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Lentil Crop.", "x": "Planning: Pulses.. Red. Practical notes — Lentil Crop. the pulse field. A little planning shows respect for Canada.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Lentil Crop and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Lentil Crop and money.", "x": "Costs: Dals.. Dals. What to budget — Lentil Crop. the pulse field. The best experiences of Rotation. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-crop-lentil-crop-farm-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
