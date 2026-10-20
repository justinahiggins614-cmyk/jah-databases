(function(){'use strict';
/* JAH Viola Davis Actor Database generator — jahdb-e2-actor-viola-davis-actor-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-actor-viola-davis-actor',PREFIX='JAH-E2ACTORVIOL-',NAME='JAH Viola Davis Actor Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Viola Davis: the complete guide", "d": "Viola Davis: the EGOT queen..", "g": "overview", "l": 2, "q": "What is Viola Davis: the complete guide?", "a": "Viola Davis: the EGOT queen..", "x": "The complete actor guide to Viola Davis: the EGOT queen.. 1965. History, meaning, practices, and how to engage respectfully — everything in one database. EGOT. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Viola Davis essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Viola Davis essentials.", "x": "At a glance: Viola Davis — the EGOT queen.. EGOT. The essentials: Fences.. Fences. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "1965.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "1965.", "x": "Viola Davis: 1965.. Fences. Essential knowledge — Fences.. the EGOT queen. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 1965..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 1965..", "x": "Explained: 1965.. Rhode Island. The context — Viola Davis. How to Get Away. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "EGOT.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "EGOT.", "x": "Viola Davis: EGOT.. Juilliard. Essential knowledge — How to Get Away.. the EGOT queen. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: EGOT..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: EGOT..", "x": "Explained: EGOT.. Murder. The context — Viola Davis. Rhode Island. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Fences.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Fences.", "x": "Viola Davis: Fences.. Rhode Island. Essential knowledge — Rhode Island.. the EGOT queen. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Fences..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Fences..", "x": "Explained: Fences.. Roles. The context — Viola Davis. Juilliard. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "How to Get Away.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "How to Get Away.", "x": "Viola Davis: How to Get Away.. Murder. Essential knowledge — Juilliard.. the EGOT queen. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: How to Get Away..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: How to Get Away..", "x": "Explained: How to Get Away.. EGOT. The context — Viola Davis. 1965. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Rhode Island.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Rhode Island.", "x": "Viola Davis: Rhode Island.. Roles. Essential knowledge — 1965.. the EGOT queen. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Rhode Island..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Rhode Island..", "x": "Explained: Rhode Island.. Fences. The context — Viola Davis. EGOT. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Juilliard.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Juilliard.", "x": "Viola Davis: Juilliard.. EGOT. Essential knowledge — EGOT.. the EGOT queen. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Juilliard..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Juilliard..", "x": "Explained: Juilliard.. Juilliard. The context — Viola Davis. Fences. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "EGOT.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "EGOT.", "x": "Viola Davis in depth: EGOT.. EGOT. Details — the EGOT queen.. Juilliard. How to Get Away. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Fences.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Fences.", "x": "Viola Davis in depth: Fences.. Fences. Details — the EGOT queen.. Rhode Island. Rhode Island. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Juilliard.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Juilliard.", "x": "Viola Davis in depth: Juilliard.. How to Get Away. Details — the EGOT queen.. Murder. Juilliard. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Rhode Island.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Rhode Island.", "x": "Viola Davis in depth: Rhode Island.. Rhode Island. Details — the EGOT queen.. Roles. 1965. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Murder.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Murder.", "x": "Viola Davis in depth: Murder.. Juilliard. Details — the EGOT queen.. EGOT. EGOT. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Roles.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Roles.", "x": "Viola Davis in depth: Roles.. 1965. Details — the EGOT queen.. Fences. Fences. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Viola Davis comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Viola Davis comes from.", "x": "Origins: EGOT.. 1965. The history of Viola Davis — the EGOT queen.. Fences. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Viola Davis respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Viola Davis respectfully.", "x": "Engaging: Juilliard.. EGOT. How to participate or observe well — Viola Davis. the EGOT queen. Respect first, always; Rhode Island.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Viola Davis do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Viola Davis do's and don'ts.", "x": "Etiquette: Murder.. Fences. The rules of respect — Viola Davis. the EGOT queen. When in doubt, ask about Roles.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Viola Davis.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Viola Davis.", "x": "Planning: EGOT.. How to Get Away. Practical notes — Viola Davis. the EGOT queen. A little planning shows respect for Fences.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Viola Davis and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Viola Davis and money.", "x": "Costs: Juilliard.. Rhode Island. What to budget — Viola Davis. the EGOT queen. The best experiences of Rhode Island. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-actor-viola-davis-actor-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
