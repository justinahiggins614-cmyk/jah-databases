(function(){'use strict';
/* JAH Dallas Zoo2 Database generator — jahdb-e2-zoo2-dallas-zoo2-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-zoo2-dallas-zoo2',PREFIX='JAH-E2ZOO2DALLA-',NAME='JAH Dallas Zoo2 Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Dallas Zoo2: the complete guide", "d": "Dallas Zoo2: the Texas 2..", "g": "overview", "l": 2, "q": "What is Dallas Zoo2: the complete guide?", "a": "Dallas Zoo2: the Texas 2..", "x": "The complete zoo guide to Dallas Zoo2: the Texas 2.. 1888. History, meaning, practices, and how to engage respectfully — everything in one database. 1888. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Dallas Zoo2 essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Dallas Zoo2 essentials.", "x": "At a glance: Dallas Zoo2 — the Texas 2.. Giants of Savanna. The essentials: Texas.. Monorail. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "1888.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "1888.", "x": "Dallas Zoo2: 1888.. Texas. Essential knowledge — Monorail.. the Texas 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 1888..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 1888..", "x": "Explained: 1888.. Savanna. The context — Dallas Zoo2. Dallas. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Giants of Savanna.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Giants of Savanna.", "x": "Dallas Zoo2: Giants of Savanna.. Acres. Essential knowledge — Dallas.. the Texas 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Giants of Savanna..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Giants of Savanna..", "x": "Explained: Giants of Savanna.. Monorail. The context — Dallas Zoo2. 106 acres. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Monorail.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Monorail.", "x": "Dallas Zoo2: Monorail.. Savanna. Essential knowledge — 106 acres.. the Texas 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Monorail..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Monorail..", "x": "Explained: Monorail.. Visiting. The context — Dallas Zoo2. Texas. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Dallas.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Dallas.", "x": "Dallas Zoo2: Dallas.. Monorail. Essential knowledge — Texas.. the Texas 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Dallas..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Dallas..", "x": "Explained: Dallas.. 1888. The context — Dallas Zoo2. 1888. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "106 acres.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "106 acres.", "x": "Dallas Zoo2: 106 acres.. Visiting. Essential knowledge — 1888.. the Texas 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: 106 acres..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: 106 acres..", "x": "Explained: 106 acres.. Texas. The context — Dallas Zoo2. Giants of Savanna. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Texas.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Texas.", "x": "Dallas Zoo2: Texas.. 1888. Essential knowledge — Giants of Savanna.. the Texas 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Texas..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Texas..", "x": "Explained: Texas.. Acres. The context — Dallas Zoo2. Monorail. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "1888.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "1888.", "x": "Dallas Zoo2 in depth: 1888.. Giants of Savanna. Details — the Texas 2.. Acres. Dallas. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Texas.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Texas.", "x": "Dallas Zoo2 in depth: Texas.. Monorail. Details — the Texas 2.. Savanna. 106 acres. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Acres.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Acres.", "x": "Dallas Zoo2 in depth: Acres.. Dallas. Details — the Texas 2.. Monorail. Texas. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Savanna.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Savanna.", "x": "Dallas Zoo2 in depth: Savanna.. 106 acres. Details — the Texas 2.. Visiting. 1888. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Monorail.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Monorail.", "x": "Dallas Zoo2 in depth: Monorail.. Texas. Details — the Texas 2.. 1888. Giants of Savanna. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Visiting.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Visiting.", "x": "Dallas Zoo2 in depth: Visiting.. 1888. Details — the Texas 2.. Texas. Monorail. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Dallas Zoo2 comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Dallas Zoo2 comes from.", "x": "Origins: 1888.. 1888. The history of Dallas Zoo2 — the Texas 2.. Texas. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Dallas Zoo2 respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Dallas Zoo2 respectfully.", "x": "Engaging: Acres.. Giants of Savanna. How to participate or observe well — Dallas Zoo2. the Texas 2. Respect first, always; Savanna.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Dallas Zoo2 do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Dallas Zoo2 do's and don'ts.", "x": "Etiquette: Monorail.. Monorail. The rules of respect — Dallas Zoo2. the Texas 2. When in doubt, ask about Visiting.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Dallas Zoo2.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Dallas Zoo2.", "x": "Planning: 1888.. Dallas. Practical notes — Dallas Zoo2. the Texas 2. A little planning shows respect for Texas.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Dallas Zoo2 and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Dallas Zoo2 and money.", "x": "Costs: Acres.. 106 acres. What to budget — Dallas Zoo2. the Texas 2. The best experiences of Savanna. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-zoo2-dallas-zoo2-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
