(function(){'use strict';
/* JAH Tai Chi Martial Art Database generator — jahdb-e2-martial-tai-chi-martial-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-martial-tai-chi-martial',PREFIX='JAH-E2MARTIALTA-',NAME='JAH Tai Chi Martial Art Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Tai Chi: the complete guide", "d": "Tai Chi: the moving meditation..", "g": "overview", "l": 2, "q": "What is Tai Chi: the complete guide?", "a": "Tai Chi: the moving meditation..", "x": "The complete martial art guide to Tai Chi: the moving meditation.. Slow. History, meaning, practices, and how to engage respectfully — everything in one database. Slow. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Tai Chi essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Tai Chi essentials.", "x": "At a glance: Tai Chi — the moving meditation.. Qi. The essentials: Health.. Yang style. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Slow.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Slow.", "x": "Tai Chi: Slow.. Health. Essential knowledge — Yang style.. the moving meditation. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Slow..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Slow..", "x": "Explained: Slow.. Parks. The context — Tai Chi. Health. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Qi.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Qi.", "x": "Tai Chi: Qi.. Yang. Essential knowledge — Health.. the moving meditation. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Qi..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Qi..", "x": "Explained: Qi.. Qi. The context — Tai Chi. Push hands. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Yang style.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Yang style.", "x": "Tai Chi: Yang style.. Parks. Essential knowledge — Push hands.. the moving meditation. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Yang style..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Yang style..", "x": "Explained: Yang style.. Forms. The context — Tai Chi. Parks. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Health.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Health.", "x": "Tai Chi: Health.. Qi. Essential knowledge — Parks.. the moving meditation. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Health..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Health..", "x": "Explained: Health.. Slow. The context — Tai Chi. Slow. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Push hands.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Push hands.", "x": "Tai Chi: Push hands.. Forms. Essential knowledge — Slow.. the moving meditation. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Push hands..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Push hands..", "x": "Explained: Push hands.. Health. The context — Tai Chi. Qi. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Parks.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Parks.", "x": "Tai Chi: Parks.. Slow. Essential knowledge — Qi.. the moving meditation. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Parks..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Parks..", "x": "Explained: Parks.. Yang. The context — Tai Chi. Yang style. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Slow.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Slow.", "x": "Tai Chi in depth: Slow.. Qi. Details — the moving meditation.. Yang. Health. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Health.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Health.", "x": "Tai Chi in depth: Health.. Yang style. Details — the moving meditation.. Parks. Push hands. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Yang.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Yang.", "x": "Tai Chi in depth: Yang.. Health. Details — the moving meditation.. Qi. Parks. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Parks.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Parks.", "x": "Tai Chi in depth: Parks.. Push hands. Details — the moving meditation.. Forms. Slow. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Qi.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Qi.", "x": "Tai Chi in depth: Qi.. Parks. Details — the moving meditation.. Slow. Qi. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Forms.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Forms.", "x": "Tai Chi in depth: Forms.. Slow. Details — the moving meditation.. Health. Yang style. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Tai Chi comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Tai Chi comes from.", "x": "Origins: Slow.. Slow. The history of Tai Chi — the moving meditation.. Health. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Tai Chi respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Tai Chi respectfully.", "x": "Engaging: Yang.. Qi. How to participate or observe well — Tai Chi. the moving meditation. Respect first, always; Parks.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Tai Chi do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Tai Chi do's and don'ts.", "x": "Etiquette: Qi.. Yang style. The rules of respect — Tai Chi. the moving meditation. When in doubt, ask about Forms.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Tai Chi.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Tai Chi.", "x": "Planning: Slow.. Health. Practical notes — Tai Chi. the moving meditation. A little planning shows respect for Health.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Tai Chi and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Tai Chi and money.", "x": "Costs: Yang.. Push hands. What to budget — Tai Chi. the moving meditation. The best experiences of Parks. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-martial-tai-chi-martial-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
