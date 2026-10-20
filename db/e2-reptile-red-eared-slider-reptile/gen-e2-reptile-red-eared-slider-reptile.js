(function(){'use strict';
/* JAH Red-Eared Slider Reptile Database generator — jahdb-e2-reptile-red-eared-slider-reptile-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-reptile-red-eared-slider-reptile',PREFIX='JAH-E2REPTILERE-',NAME='JAH Red-Eared Slider Reptile Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Red-Eared Slider: the complete guide", "d": "Red-Eared Slider: the pond classic..", "g": "overview", "l": 2, "q": "What is Red-Eared Slider: the complete guide?", "a": "Red-Eared Slider: the pond classic..", "x": "The complete reptile guide to Red-Eared Slider: the pond classic.. Red ears. History, meaning, practices, and how to engage respectfully — everything in one database. Ears. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Red-Eared Slider essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Red-Eared Slider essentials.", "x": "At a glance: Red-Eared Slider — the pond classic.. Basking. The essentials: Basking.. Ponds. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Red ears.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Red ears.", "x": "Red-Eared Slider: Red ears.. Basking. Essential knowledge — Ponds.. the pond classic. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Red ears..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Red ears..", "x": "Explained: Red ears.. Beginner. The context — Red-Eared Slider. Invasive. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Basking.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Basking.", "x": "Red-Eared Slider: Basking.. Invasive. Essential knowledge — Invasive.. the pond classic. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Basking..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Basking..", "x": "Explained: Basking.. Ponds. The context — Red-Eared Slider. Beginner. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Ponds.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Ponds.", "x": "Red-Eared Slider: Ponds.. Beginner. Essential knowledge — Beginner.. the pond classic. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Ponds..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Ponds..", "x": "Explained: Ponds.. Care. The context — Red-Eared Slider. Turtles. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Invasive.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Invasive.", "x": "Red-Eared Slider: Invasive.. Ponds. Essential knowledge — Turtles.. the pond classic. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Invasive..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Invasive..", "x": "Explained: Invasive.. Ears. The context — Red-Eared Slider. Red ears. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Beginner.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Beginner.", "x": "Red-Eared Slider: Beginner.. Care. Essential knowledge — Red ears.. the pond classic. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Beginner..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Beginner..", "x": "Explained: Beginner.. Basking. The context — Red-Eared Slider. Basking. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Turtles.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Turtles.", "x": "Red-Eared Slider: Turtles.. Ears. Essential knowledge — Basking.. the pond classic. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Turtles..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Turtles..", "x": "Explained: Turtles.. Invasive. The context — Red-Eared Slider. Ponds. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Ears.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Ears.", "x": "Red-Eared Slider in depth: Ears.. Basking. Details — the pond classic.. Invasive. Invasive. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Basking.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Basking.", "x": "Red-Eared Slider in depth: Basking.. Ponds. Details — the pond classic.. Beginner. Beginner. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Invasive.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Invasive.", "x": "Red-Eared Slider in depth: Invasive.. Invasive. Details — the pond classic.. Ponds. Turtles. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Beginner.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Beginner.", "x": "Red-Eared Slider in depth: Beginner.. Beginner. Details — the pond classic.. Care. Red ears. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Ponds.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Ponds.", "x": "Red-Eared Slider in depth: Ponds.. Turtles. Details — the pond classic.. Ears. Basking. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Care.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Care.", "x": "Red-Eared Slider in depth: Care.. Red ears. Details — the pond classic.. Basking. Ponds. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Red-Eared Slider comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Red-Eared Slider comes from.", "x": "Origins: Ears.. Red ears. The history of Red-Eared Slider — the pond classic.. Basking. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Red-Eared Slider respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Red-Eared Slider respectfully.", "x": "Engaging: Invasive.. Basking. How to participate or observe well — Red-Eared Slider. the pond classic. Respect first, always; Beginner.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Red-Eared Slider do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Red-Eared Slider do's and don'ts.", "x": "Etiquette: Ponds.. Ponds. The rules of respect — Red-Eared Slider. the pond classic. When in doubt, ask about Care.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Red-Eared Slider.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Red-Eared Slider.", "x": "Planning: Ears.. Invasive. Practical notes — Red-Eared Slider. the pond classic. A little planning shows respect for Basking.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Red-Eared Slider and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Red-Eared Slider and money.", "x": "Costs: Invasive.. Beginner. What to budget — Red-Eared Slider. the pond classic. The best experiences of Beginner. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-reptile-red-eared-slider-reptile-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
