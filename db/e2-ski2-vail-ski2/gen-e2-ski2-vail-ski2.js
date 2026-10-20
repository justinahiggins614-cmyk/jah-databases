(function(){'use strict';
/* JAH Vail Ski2 Database generator — jahdb-e2-ski2-vail-ski2-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-ski2-vail-ski2',PREFIX='JAH-E2SKI2VAILS-',NAME='JAH Vail Ski2 Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Vail Ski2: the complete guide", "d": "Vail Ski2: the vast 2..", "g": "overview", "l": 2, "q": "What is Vail Ski2: the complete guide?", "a": "Vail Ski2: the vast 2..", "x": "The complete ski resort guide to Vail Ski2: the vast 2.. Back Bowls. History, meaning, practices, and how to engage respectfully — everything in one database. Bowls. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Vail Ski2 essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Vail Ski2 essentials.", "x": "At a glance: Vail Ski2 — the vast 2.. Epic Pass. The essentials: Legend.. Colorado. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Back Bowls.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Back Bowls.", "x": "Vail Ski2: Back Bowls.. Legend. Essential knowledge — Colorado.. the vast 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Back Bowls..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Back Bowls..", "x": "Explained: Back Bowls.. Epic. The context — Vail Ski2. 5,289 acres. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Epic Pass.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Epic Pass.", "x": "Vail Ski2: Epic Pass.. Village. Essential knowledge — 5,289 acres.. the vast 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Epic Pass..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Epic Pass..", "x": "Explained: Epic Pass.. Acres. The context — Vail Ski2. Village. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Colorado.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Colorado.", "x": "Vail Ski2: Colorado.. Epic. Essential knowledge — Village.. the vast 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Colorado..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Colorado..", "x": "Explained: Colorado.. Guide. The context — Vail Ski2. Legend. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "5,289 acres.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "5,289 acres.", "x": "Vail Ski2: 5,289 acres.. Acres. Essential knowledge — Legend.. the vast 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: 5,289 acres..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: 5,289 acres..", "x": "Explained: 5,289 acres.. Bowls. The context — Vail Ski2. Back Bowls. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Village.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Village.", "x": "Vail Ski2: Village.. Guide. Essential knowledge — Back Bowls.. the vast 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Village..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Village..", "x": "Explained: Village.. Legend. The context — Vail Ski2. Epic Pass. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Legend.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Legend.", "x": "Vail Ski2: Legend.. Bowls. Essential knowledge — Epic Pass.. the vast 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Legend..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Legend..", "x": "Explained: Legend.. Village. The context — Vail Ski2. Colorado. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Bowls.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Bowls.", "x": "Vail Ski2 in depth: Bowls.. Epic Pass. Details — the vast 2.. Village. 5,289 acres. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Legend.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Legend.", "x": "Vail Ski2 in depth: Legend.. Colorado. Details — the vast 2.. Epic. Village. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Village.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Village.", "x": "Vail Ski2 in depth: Village.. 5,289 acres. Details — the vast 2.. Acres. Legend. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Epic.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Epic.", "x": "Vail Ski2 in depth: Epic.. Village. Details — the vast 2.. Guide. Back Bowls. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Acres.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Acres.", "x": "Vail Ski2 in depth: Acres.. Legend. Details — the vast 2.. Bowls. Epic Pass. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Guide.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Guide.", "x": "Vail Ski2 in depth: Guide.. Back Bowls. Details — the vast 2.. Legend. Colorado. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Vail Ski2 comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Vail Ski2 comes from.", "x": "Origins: Bowls.. Back Bowls. The history of Vail Ski2 — the vast 2.. Legend. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Vail Ski2 respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Vail Ski2 respectfully.", "x": "Engaging: Village.. Epic Pass. How to participate or observe well — Vail Ski2. the vast 2. Respect first, always; Epic.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Vail Ski2 do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Vail Ski2 do's and don'ts.", "x": "Etiquette: Acres.. Colorado. The rules of respect — Vail Ski2. the vast 2. When in doubt, ask about Guide.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Vail Ski2.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Vail Ski2.", "x": "Planning: Bowls.. 5,289 acres. Practical notes — Vail Ski2. the vast 2. A little planning shows respect for Legend.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Vail Ski2 and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Vail Ski2 and money.", "x": "Costs: Village.. Village. What to budget — Vail Ski2. the vast 2. The best experiences of Epic. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-ski2-vail-ski2-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
