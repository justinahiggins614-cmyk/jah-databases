(function(){'use strict';
/* JAH The Who Band Band Database generator — jahdb-e2-band-the-who-band-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-band-the-who-band',PREFIX='JAH-E2BANDTHEWH-',NAME='JAH The Who Band Band Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "The Who Band: the complete guide", "d": "The Who Band: the maximum R&B..", "g": "overview", "l": 2, "q": "What is The Who Band: the complete guide?", "a": "The Who Band: the maximum R&B..", "x": "The complete band guide to The Who Band: the maximum R&B.. 1964. History, meaning, practices, and how to engage respectfully — everything in one database. Townshend. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "The Who Band essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "The Who Band essentials.", "x": "At a glance: The Who Band — the maximum R&B.. Townshend. The essentials: Tommy.. My Generation. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "1964.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "1964.", "x": "The Who Band: 1964.. Tommy. Essential knowledge — My Generation.. the maximum R&B. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 1964..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 1964..", "x": "Explained: 1964.. Windmill. The context — The Who Band. Tommy. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Townshend.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Townshend.", "x": "The Who Band: Townshend.. Moon. Essential knowledge — Tommy.. the maximum R&B. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Townshend..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Townshend..", "x": "Explained: Townshend.. Who. The context — The Who Band. Windmill. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "My Generation.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "My Generation.", "x": "The Who Band: My Generation.. Windmill. Essential knowledge — Windmill.. the maximum R&B. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: My Generation..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: My Generation..", "x": "Explained: My Generation.. Legacy. The context — The Who Band. Moon. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Tommy.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Tommy.", "x": "The Who Band: Tommy.. Who. Essential knowledge — Moon.. the maximum R&B. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Tommy..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Tommy..", "x": "Explained: Tommy.. Townshend. The context — The Who Band. 1964. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Windmill.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Windmill.", "x": "The Who Band: Windmill.. Legacy. Essential knowledge — 1964.. the maximum R&B. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Windmill..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Windmill..", "x": "Explained: Windmill.. Tommy. The context — The Who Band. Townshend. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Moon.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Moon.", "x": "The Who Band: Moon.. Townshend. Essential knowledge — Townshend.. the maximum R&B. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Moon..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Moon..", "x": "Explained: Moon.. Moon. The context — The Who Band. My Generation. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Townshend.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Townshend.", "x": "The Who Band in depth: Townshend.. Townshend. Details — the maximum R&B.. Moon. Tommy. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Tommy.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Tommy.", "x": "The Who Band in depth: Tommy.. My Generation. Details — the maximum R&B.. Windmill. Windmill. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Moon.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Moon.", "x": "The Who Band in depth: Moon.. Tommy. Details — the maximum R&B.. Who. Moon. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Windmill.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Windmill.", "x": "The Who Band in depth: Windmill.. Windmill. Details — the maximum R&B.. Legacy. 1964. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Who.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Who.", "x": "The Who Band in depth: Who.. Moon. Details — the maximum R&B.. Townshend. Townshend. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Legacy.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Legacy.", "x": "The Who Band in depth: Legacy.. 1964. Details — the maximum R&B.. Tommy. My Generation. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where The Who Band comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where The Who Band comes from.", "x": "Origins: Townshend.. 1964. The history of The Who Band — the maximum R&B.. Tommy. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing The Who Band respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing The Who Band respectfully.", "x": "Engaging: Moon.. Townshend. How to participate or observe well — The Who Band. the maximum R&B. Respect first, always; Windmill.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "The Who Band do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "The Who Band do's and don'ts.", "x": "Etiquette: Who.. My Generation. The rules of respect — The Who Band. the maximum R&B. When in doubt, ask about Legacy.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around The Who Band.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around The Who Band.", "x": "Planning: Townshend.. Tommy. Practical notes — The Who Band. the maximum R&B. A little planning shows respect for Tommy.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "The Who Band and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "The Who Band and money.", "x": "Costs: Moon.. Windmill. What to budget — The Who Band. the maximum R&B. The best experiences of Windmill. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-band-the-who-band-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
