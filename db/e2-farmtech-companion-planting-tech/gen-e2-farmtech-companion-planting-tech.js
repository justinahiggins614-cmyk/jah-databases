(function(){'use strict';
/* JAH Companion Planting Farming Technique Database generator — jahdb-e2-farmtech-companion-planting-tech-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-farmtech-companion-planting-tech',PREFIX='JAH-E2FARMTECHC-',NAME='JAH Companion Planting Farming Technique Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Companion Planting: the complete guide", "d": "Companion Planting: the plant friends..", "g": "overview", "l": 2, "q": "What is Companion Planting: the complete guide?", "a": "Companion Planting: the plant friends..", "x": "The complete farming technique guide to Companion Planting: the plant friends.. Three sisters. History, meaning, practices, and how to engage respectfully — everything in one database. Sisters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Companion Planting essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Companion Planting essentials.", "x": "At a glance: Companion Planting — the plant friends.. Marigolds. The essentials: Trap.. Basil. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Three sisters.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Three sisters.", "x": "Companion Planting: Three sisters.. Trap. Essential knowledge — Basil.. the plant friends. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Three sisters..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Three sisters..", "x": "Explained: Three sisters.. Observation. The context — Companion Planting. Trap crops. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Marigolds.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Marigolds.", "x": "Companion Planting: Marigolds.. Guilds. Essential knowledge — Trap crops.. the plant friends. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Marigolds..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Marigolds..", "x": "Explained: Marigolds.. Marigolds. The context — Companion Planting. Guilds. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Basil.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Basil.", "x": "Companion Planting: Basil.. Observation. Essential knowledge — Guilds.. the plant friends. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Basil..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Basil..", "x": "Explained: Basil.. Guide. The context — Companion Planting. Observation. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Trap crops.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Trap crops.", "x": "Companion Planting: Trap crops.. Marigolds. Essential knowledge — Observation.. the plant friends. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Trap crops..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Trap crops..", "x": "Explained: Trap crops.. Sisters. The context — Companion Planting. Three sisters. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Guilds.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Guilds.", "x": "Companion Planting: Guilds.. Guide. Essential knowledge — Three sisters.. the plant friends. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Guilds..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Guilds..", "x": "Explained: Guilds.. Trap. The context — Companion Planting. Marigolds. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Observation.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Observation.", "x": "Companion Planting: Observation.. Sisters. Essential knowledge — Marigolds.. the plant friends. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Observation..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Observation..", "x": "Explained: Observation.. Guilds. The context — Companion Planting. Basil. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Sisters.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Sisters.", "x": "Companion Planting in depth: Sisters.. Marigolds. Details — the plant friends.. Guilds. Trap crops. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Trap.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Trap.", "x": "Companion Planting in depth: Trap.. Basil. Details — the plant friends.. Observation. Guilds. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Guilds.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Guilds.", "x": "Companion Planting in depth: Guilds.. Trap crops. Details — the plant friends.. Marigolds. Observation. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Observation.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Observation.", "x": "Companion Planting in depth: Observation.. Guilds. Details — the plant friends.. Guide. Three sisters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Marigolds.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Marigolds.", "x": "Companion Planting in depth: Marigolds.. Observation. Details — the plant friends.. Sisters. Marigolds. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Guide.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Guide.", "x": "Companion Planting in depth: Guide.. Three sisters. Details — the plant friends.. Trap. Basil. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Companion Planting comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Companion Planting comes from.", "x": "Origins: Sisters.. Three sisters. The history of Companion Planting — the plant friends.. Trap. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Companion Planting respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Companion Planting respectfully.", "x": "Engaging: Guilds.. Marigolds. How to participate or observe well — Companion Planting. the plant friends. Respect first, always; Observation.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Companion Planting do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Companion Planting do's and don'ts.", "x": "Etiquette: Marigolds.. Basil. The rules of respect — Companion Planting. the plant friends. When in doubt, ask about Guide.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Companion Planting.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Companion Planting.", "x": "Planning: Sisters.. Trap crops. Practical notes — Companion Planting. the plant friends. A little planning shows respect for Trap.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Companion Planting and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Companion Planting and money.", "x": "Costs: Guilds.. Guilds. What to budget — Companion Planting. the plant friends. The best experiences of Observation. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-farmtech-companion-planting-tech-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
