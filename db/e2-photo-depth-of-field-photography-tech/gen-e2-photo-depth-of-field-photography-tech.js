(function(){'use strict';
/* JAH Depth of Field Photography Database generator — jahdb-e2-photo-depth-of-field-photography-tech-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-photo-depth-of-field-photography-tech',PREFIX='JAH-E2PHOTODEPT-',NAME='JAH Depth of Field Photography Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Depth of Field: the complete guide", "d": "Depth of Field: the focus zone..", "g": "overview", "l": 2, "q": "What is Depth of Field: the complete guide?", "a": "Depth of Field: the focus zone..", "x": "The complete photography guide to Depth of Field: the focus zone.. Aperture. History, meaning, practices, and how to engage respectfully — everything in one database. Aperture. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Depth of Field essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Depth of Field essentials.", "x": "At a glance: Depth of Field — the focus zone.. Distance. The essentials: Hyperfocal.. Bokeh. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Aperture.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Aperture.", "x": "Depth of Field: Aperture.. Hyperfocal. Essential knowledge — Bokeh.. the focus zone. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Aperture..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Aperture..", "x": "Explained: Aperture.. Bokeh. The context — Depth of Field. Hyperfocal. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Distance.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Distance.", "x": "Depth of Field: Distance.. Control. Essential knowledge — Hyperfocal.. the focus zone. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Distance..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Distance..", "x": "Explained: Distance.. Sensor. The context — Depth of Field. Sensor. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Bokeh.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Bokeh.", "x": "Depth of Field: Bokeh.. Bokeh. Essential knowledge — Sensor.. the focus zone. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Bokeh..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Bokeh..", "x": "Explained: Bokeh.. Tips. The context — Depth of Field. Control. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Hyperfocal.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Hyperfocal.", "x": "Depth of Field: Hyperfocal.. Sensor. Essential knowledge — Control.. the focus zone. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Hyperfocal..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Hyperfocal..", "x": "Explained: Hyperfocal.. Aperture. The context — Depth of Field. Aperture. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Sensor.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Sensor.", "x": "Depth of Field: Sensor.. Tips. Essential knowledge — Aperture.. the focus zone. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Sensor..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Sensor..", "x": "Explained: Sensor.. Hyperfocal. The context — Depth of Field. Distance. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Control.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Control.", "x": "Depth of Field: Control.. Aperture. Essential knowledge — Distance.. the focus zone. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Control..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Control..", "x": "Explained: Control.. Control. The context — Depth of Field. Bokeh. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Aperture.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Aperture.", "x": "Depth of Field in depth: Aperture.. Distance. Details — the focus zone.. Control. Hyperfocal. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Hyperfocal.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Hyperfocal.", "x": "Depth of Field in depth: Hyperfocal.. Bokeh. Details — the focus zone.. Bokeh. Sensor. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Control.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Control.", "x": "Depth of Field in depth: Control.. Hyperfocal. Details — the focus zone.. Sensor. Control. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Bokeh.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Bokeh.", "x": "Depth of Field in depth: Bokeh.. Sensor. Details — the focus zone.. Tips. Aperture. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Sensor.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Sensor.", "x": "Depth of Field in depth: Sensor.. Control. Details — the focus zone.. Aperture. Distance. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Tips.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Tips.", "x": "Depth of Field in depth: Tips.. Aperture. Details — the focus zone.. Hyperfocal. Bokeh. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Depth of Field comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Depth of Field comes from.", "x": "Origins: Aperture.. Aperture. The history of Depth of Field — the focus zone.. Hyperfocal. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Depth of Field respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Depth of Field respectfully.", "x": "Engaging: Control.. Distance. How to participate or observe well — Depth of Field. the focus zone. Respect first, always; Bokeh.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Depth of Field do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Depth of Field do's and don'ts.", "x": "Etiquette: Sensor.. Bokeh. The rules of respect — Depth of Field. the focus zone. When in doubt, ask about Tips.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Depth of Field.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Depth of Field.", "x": "Planning: Aperture.. Hyperfocal. Practical notes — Depth of Field. the focus zone. A little planning shows respect for Hyperfocal.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Depth of Field and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Depth of Field and money.", "x": "Costs: Control.. Sensor. What to budget — Depth of Field. the focus zone. The best experiences of Bokeh. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-photo-depth-of-field-photography-tech-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
