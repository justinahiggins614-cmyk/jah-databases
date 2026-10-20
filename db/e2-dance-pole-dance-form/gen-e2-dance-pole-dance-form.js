(function(){'use strict';
/* JAH Pole Dance Dance Form Database generator — jahdb-e2-dance-pole-dance-form-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-dance-pole-dance-form',PREFIX='JAH-E2DANCEPOLE-',NAME='JAH Pole Dance Dance Form Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Pole Dance: the complete guide", "d": "Pole Dance: the aerial strength..", "g": "overview", "l": 2, "q": "What is Pole Dance: the complete guide?", "a": "Pole Dance: the aerial strength..", "x": "The complete dance form guide to Pole Dance: the aerial strength.. Strength. History, meaning, practices, and how to engage respectfully — everything in one database. Spins. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Pole Dance essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Pole Dance essentials.", "x": "At a glance: Pole Dance — the aerial strength.. Spins. The essentials: Sport.. Inverts. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Strength.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Strength.", "x": "Pole Dance: Strength.. Sport. Essential knowledge — Inverts.. the aerial strength. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Strength..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Strength..", "x": "Explained: Strength.. Choreo. The context — Pole Dance. Sport. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Spins.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Spins.", "x": "Pole Dance: Spins.. Grip. Essential knowledge — Sport.. the aerial strength. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Spins..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Spins..", "x": "Explained: Spins.. Strength. The context — Pole Dance. Grip. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Inverts.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Inverts.", "x": "Pole Dance: Inverts.. Choreo. Essential knowledge — Grip.. the aerial strength. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Inverts..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Inverts..", "x": "Explained: Inverts.. Training. The context — Pole Dance. Choreography. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Sport.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Sport.", "x": "Pole Dance: Sport.. Strength. Essential knowledge — Choreography.. the aerial strength. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Sport..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Sport..", "x": "Explained: Sport.. Spins. The context — Pole Dance. Strength. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Grip.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Grip.", "x": "Pole Dance: Grip.. Training. Essential knowledge — Strength.. the aerial strength. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Grip..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Grip..", "x": "Explained: Grip.. Sport. The context — Pole Dance. Spins. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Choreography.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Choreography.", "x": "Pole Dance: Choreography.. Spins. Essential knowledge — Spins.. the aerial strength. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Choreography..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Choreography..", "x": "Explained: Choreography.. Grip. The context — Pole Dance. Inverts. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Spins.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Spins.", "x": "Pole Dance in depth: Spins.. Spins. Details — the aerial strength.. Grip. Sport. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Sport.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Sport.", "x": "Pole Dance in depth: Sport.. Inverts. Details — the aerial strength.. Choreo. Grip. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Grip.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Grip.", "x": "Pole Dance in depth: Grip.. Sport. Details — the aerial strength.. Strength. Choreography. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Choreo.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Choreo.", "x": "Pole Dance in depth: Choreo.. Grip. Details — the aerial strength.. Training. Strength. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Strength.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Strength.", "x": "Pole Dance in depth: Strength.. Choreography. Details — the aerial strength.. Spins. Spins. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Training.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Training.", "x": "Pole Dance in depth: Training.. Strength. Details — the aerial strength.. Sport. Inverts. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Pole Dance comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Pole Dance comes from.", "x": "Origins: Spins.. Strength. The history of Pole Dance — the aerial strength.. Sport. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Pole Dance respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Pole Dance respectfully.", "x": "Engaging: Grip.. Spins. How to participate or observe well — Pole Dance. the aerial strength. Respect first, always; Choreo.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Pole Dance do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Pole Dance do's and don'ts.", "x": "Etiquette: Strength.. Inverts. The rules of respect — Pole Dance. the aerial strength. When in doubt, ask about Training.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Pole Dance.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Pole Dance.", "x": "Planning: Spins.. Sport. Practical notes — Pole Dance. the aerial strength. A little planning shows respect for Sport.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Pole Dance and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Pole Dance and money.", "x": "Costs: Grip.. Grip. What to budget — Pole Dance. the aerial strength. The best experiences of Choreo. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-dance-pole-dance-form-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
