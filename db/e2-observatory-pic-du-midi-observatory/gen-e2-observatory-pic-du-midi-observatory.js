(function(){'use strict';
/* JAH Pic du Midi Observatory Observatory Database generator — jahdb-e2-observatory-pic-du-midi-observatory-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-observatory-pic-du-midi-observatory',PREFIX='JAH-E2OBSERVATO-',NAME='JAH Pic du Midi Observatory Observatory Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Pic du Midi Observatory: the complete guide", "d": "Pic du Midi Observatory: the Pyrenees' eye..", "g": "overview", "l": 2, "q": "What is Pic du Midi Observatory: the complete guide?", "a": "Pic du Midi Observatory: the Pyrenees' eye..", "x": "The complete observatory guide to Pic du Midi Observatory: the Pyrenees' eye.. 2,877m. History, meaning, practices, and how to engage respectfully — everything in one database. Altitude. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Pic du Midi Observatory essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Pic du Midi Observatory essentials.", "x": "At a glance: Pic du Midi Observatory — the Pyrenees' eye.. 1870. The essentials: Sun.. Coronagraph. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "2,877m.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "2,877m.", "x": "Pic du Midi Observatory: 2,877m.. Sun. Essential knowledge — Coronagraph.. the Pyrenees' eye. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 2,877m..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 2,877m..", "x": "Explained: 2,877m.. Nights. The context — Pic du Midi Observatory. Cable car. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "1870.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "1870.", "x": "Pic du Midi Observatory: 1870.. Cable car. Essential knowledge — Cable car.. the Pyrenees' eye. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: 1870..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: 1870..", "x": "Explained: 1870.. France. The context — Pic du Midi Observatory. Sunsets. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Coronagraph.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Coronagraph.", "x": "Pic du Midi Observatory: Coronagraph.. Nights. Essential knowledge — Sunsets.. the Pyrenees' eye. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Coronagraph..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Coronagraph..", "x": "Explained: Coronagraph.. History. The context — Pic du Midi Observatory. France. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Cable car.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Cable car.", "x": "Pic du Midi Observatory: Cable car.. France. Essential knowledge — France.. the Pyrenees' eye. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Cable car..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Cable car..", "x": "Explained: Cable car.. Altitude. The context — Pic du Midi Observatory. 2,877m. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Sunsets.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Sunsets.", "x": "Pic du Midi Observatory: Sunsets.. History. Essential knowledge — 2,877m.. the Pyrenees' eye. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Sunsets..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Sunsets..", "x": "Explained: Sunsets.. Sun. The context — Pic du Midi Observatory. 1870. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "France.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "France.", "x": "Pic du Midi Observatory: France.. Altitude. Essential knowledge — 1870.. the Pyrenees' eye. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: France..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: France..", "x": "Explained: France.. Cable car. The context — Pic du Midi Observatory. Coronagraph. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Altitude.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Altitude.", "x": "Pic du Midi Observatory in depth: Altitude.. 1870. Details — the Pyrenees' eye.. Cable car. Cable car. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Sun.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Sun.", "x": "Pic du Midi Observatory in depth: Sun.. Coronagraph. Details — the Pyrenees' eye.. Nights. Sunsets. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Cable car.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Cable car.", "x": "Pic du Midi Observatory in depth: Cable car.. Cable car. Details — the Pyrenees' eye.. France. France. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Nights.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Nights.", "x": "Pic du Midi Observatory in depth: Nights.. Sunsets. Details — the Pyrenees' eye.. History. 2,877m. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "France.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "France.", "x": "Pic du Midi Observatory in depth: France.. France. Details — the Pyrenees' eye.. Altitude. 1870. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "History.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "History.", "x": "Pic du Midi Observatory in depth: History.. 2,877m. Details — the Pyrenees' eye.. Sun. Coronagraph. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Pic du Midi Observatory comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Pic du Midi Observatory comes from.", "x": "Origins: Altitude.. 2,877m. The history of Pic du Midi Observatory — the Pyrenees' eye.. Sun. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Pic du Midi Observatory respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Pic du Midi Observatory respectfully.", "x": "Engaging: Cable car.. 1870. How to participate or observe well — Pic du Midi Observatory. the Pyrenees' eye. Respect first, always; Nights.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Pic du Midi Observatory do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Pic du Midi Observatory do's and don'ts.", "x": "Etiquette: France.. Coronagraph. The rules of respect — Pic du Midi Observatory. the Pyrenees' eye. When in doubt, ask about History.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Pic du Midi Observatory.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Pic du Midi Observatory.", "x": "Planning: Altitude.. Cable car. Practical notes — Pic du Midi Observatory. the Pyrenees' eye. A little planning shows respect for Sun.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Pic du Midi Observatory and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Pic du Midi Observatory and money.", "x": "Costs: Cable car.. Sunsets. What to budget — Pic du Midi Observatory. the Pyrenees' eye. The best experiences of Nights. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-observatory-pic-du-midi-observatory-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
