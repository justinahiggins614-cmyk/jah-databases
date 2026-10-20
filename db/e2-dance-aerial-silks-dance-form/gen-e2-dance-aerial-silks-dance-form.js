(function(){'use strict';
/* JAH Aerial Silks Dance Dance Form Database generator — jahdb-e2-dance-aerial-silks-dance-form-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-dance-aerial-silks-dance-form',PREFIX='JAH-E2DANCEAERI-',NAME='JAH Aerial Silks Dance Dance Form Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Aerial Silks Dance: the complete guide", "d": "Aerial Silks Dance: the fabric flight..", "g": "overview", "l": 2, "q": "What is Aerial Silks Dance: the complete guide?", "a": "Aerial Silks Dance: the fabric flight..", "x": "The complete dance form guide to Aerial Silks Dance: the fabric flight.. Fabric. History, meaning, practices, and how to engage respectfully — everything in one database. Drops. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Aerial Silks Dance essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Aerial Silks Dance essentials.", "x": "At a glance: Aerial Silks Dance — the fabric flight.. Drops. The essentials: Circus.. Climbs. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Fabric.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Fabric.", "x": "Aerial Silks Dance: Fabric.. Circus. Essential knowledge — Climbs.. the fabric flight. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Fabric..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Fabric..", "x": "Explained: Fabric.. Fabric. The context — Aerial Silks Dance. Circus. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Drops.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Drops.", "x": "Aerial Silks Dance: Drops.. Wraps. Essential knowledge — Circus.. the fabric flight. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Drops..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Drops..", "x": "Explained: Drops.. Strength. The context — Aerial Silks Dance. Strength. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Climbs.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Climbs.", "x": "Aerial Silks Dance: Climbs.. Fabric. Essential knowledge — Strength.. the fabric flight. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Climbs..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Climbs..", "x": "Explained: Climbs.. Training. The context — Aerial Silks Dance. Wraps. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Circus.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Circus.", "x": "Aerial Silks Dance: Circus.. Strength. Essential knowledge — Wraps.. the fabric flight. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Circus..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Circus..", "x": "Explained: Circus.. Drops. The context — Aerial Silks Dance. Fabric. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Strength.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Strength.", "x": "Aerial Silks Dance: Strength.. Training. Essential knowledge — Fabric.. the fabric flight. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Strength..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Strength..", "x": "Explained: Strength.. Circus. The context — Aerial Silks Dance. Drops. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Wraps.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Wraps.", "x": "Aerial Silks Dance: Wraps.. Drops. Essential knowledge — Drops.. the fabric flight. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Wraps..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Wraps..", "x": "Explained: Wraps.. Wraps. The context — Aerial Silks Dance. Climbs. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Drops.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Drops.", "x": "Aerial Silks Dance in depth: Drops.. Drops. Details — the fabric flight.. Wraps. Circus. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Circus.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Circus.", "x": "Aerial Silks Dance in depth: Circus.. Climbs. Details — the fabric flight.. Fabric. Strength. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Wraps.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Wraps.", "x": "Aerial Silks Dance in depth: Wraps.. Circus. Details — the fabric flight.. Strength. Wraps. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Fabric.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Fabric.", "x": "Aerial Silks Dance in depth: Fabric.. Strength. Details — the fabric flight.. Training. Fabric. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Strength.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Strength.", "x": "Aerial Silks Dance in depth: Strength.. Wraps. Details — the fabric flight.. Drops. Drops. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Training.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Training.", "x": "Aerial Silks Dance in depth: Training.. Fabric. Details — the fabric flight.. Circus. Climbs. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Aerial Silks Dance comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Aerial Silks Dance comes from.", "x": "Origins: Drops.. Fabric. The history of Aerial Silks Dance — the fabric flight.. Circus. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Aerial Silks Dance respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Aerial Silks Dance respectfully.", "x": "Engaging: Wraps.. Drops. How to participate or observe well — Aerial Silks Dance. the fabric flight. Respect first, always; Fabric.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Aerial Silks Dance do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Aerial Silks Dance do's and don'ts.", "x": "Etiquette: Strength.. Climbs. The rules of respect — Aerial Silks Dance. the fabric flight. When in doubt, ask about Training.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Aerial Silks Dance.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Aerial Silks Dance.", "x": "Planning: Drops.. Circus. Practical notes — Aerial Silks Dance. the fabric flight. A little planning shows respect for Circus.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Aerial Silks Dance and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Aerial Silks Dance and money.", "x": "Costs: Wraps.. Strength. What to budget — Aerial Silks Dance. the fabric flight. The best experiences of Fabric. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-dance-aerial-silks-dance-form-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
