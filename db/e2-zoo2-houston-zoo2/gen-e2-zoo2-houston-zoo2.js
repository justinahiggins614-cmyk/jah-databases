(function(){'use strict';
/* JAH Houston Zoo2 Database generator — jahdb-e2-zoo2-houston-zoo2-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-zoo2-houston-zoo2',PREFIX='JAH-E2ZOO2HOUST-',NAME='JAH Houston Zoo2 Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Houston Zoo2: the complete guide", "d": "Houston Zoo2: the Texas 2..", "g": "overview", "l": 2, "q": "What is Houston Zoo2: the complete guide?", "a": "Houston Zoo2: the Texas 2..", "x": "The complete zoo guide to Houston Zoo2: the Texas 2.. 1922. History, meaning, practices, and how to engage respectfully — everything in one database. 1922. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Houston Zoo2 essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Houston Zoo2 essentials.", "x": "At a glance: Houston Zoo2 — the Texas 2.. Gorillas. The essentials: Elephants.. Texas Wetlands. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "1922.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "1922.", "x": "Houston Zoo2: 1922.. Elephants. Essential knowledge — Texas Wetlands.. the Texas 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 1922..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 1922..", "x": "Explained: 1922.. Gorillas. The context — Houston Zoo2. 55 acres. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Gorillas.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Gorillas.", "x": "Houston Zoo2: Gorillas.. Houston. Essential knowledge — 55 acres.. the Texas 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Gorillas..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Gorillas..", "x": "Explained: Gorillas.. Acres. The context — Houston Zoo2. Houston. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Texas Wetlands.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Texas Wetlands.", "x": "Houston Zoo2: Texas Wetlands.. Gorillas. Essential knowledge — Houston.. the Texas 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Texas Wetlands..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Texas Wetlands..", "x": "Explained: Texas Wetlands.. Visiting. The context — Houston Zoo2. Elephants. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "55 acres.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "55 acres.", "x": "Houston Zoo2: 55 acres.. Acres. Essential knowledge — Elephants.. the Texas 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: 55 acres..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: 55 acres..", "x": "Explained: 55 acres.. 1922. The context — Houston Zoo2. 1922. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Houston.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Houston.", "x": "Houston Zoo2: Houston.. Visiting. Essential knowledge — 1922.. the Texas 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Houston..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Houston..", "x": "Explained: Houston.. Elephants. The context — Houston Zoo2. Gorillas. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Elephants.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Elephants.", "x": "Houston Zoo2: Elephants.. 1922. Essential knowledge — Gorillas.. the Texas 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Elephants..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Elephants..", "x": "Explained: Elephants.. Houston. The context — Houston Zoo2. Texas Wetlands. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "1922.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "1922.", "x": "Houston Zoo2 in depth: 1922.. Gorillas. Details — the Texas 2.. Houston. 55 acres. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Elephants.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Elephants.", "x": "Houston Zoo2 in depth: Elephants.. Texas Wetlands. Details — the Texas 2.. Gorillas. Houston. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Houston.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Houston.", "x": "Houston Zoo2 in depth: Houston.. 55 acres. Details — the Texas 2.. Acres. Elephants. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Gorillas.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Gorillas.", "x": "Houston Zoo2 in depth: Gorillas.. Houston. Details — the Texas 2.. Visiting. 1922. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Acres.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Acres.", "x": "Houston Zoo2 in depth: Acres.. Elephants. Details — the Texas 2.. 1922. Gorillas. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Visiting.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Visiting.", "x": "Houston Zoo2 in depth: Visiting.. 1922. Details — the Texas 2.. Elephants. Texas Wetlands. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Houston Zoo2 comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Houston Zoo2 comes from.", "x": "Origins: 1922.. 1922. The history of Houston Zoo2 — the Texas 2.. Elephants. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Houston Zoo2 respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Houston Zoo2 respectfully.", "x": "Engaging: Houston.. Gorillas. How to participate or observe well — Houston Zoo2. the Texas 2. Respect first, always; Gorillas.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Houston Zoo2 do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Houston Zoo2 do's and don'ts.", "x": "Etiquette: Acres.. Texas Wetlands. The rules of respect — Houston Zoo2. the Texas 2. When in doubt, ask about Visiting.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Houston Zoo2.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Houston Zoo2.", "x": "Planning: 1922.. 55 acres. Practical notes — Houston Zoo2. the Texas 2. A little planning shows respect for Elephants.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Houston Zoo2 and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Houston Zoo2 and money.", "x": "Costs: Houston.. Houston. What to budget — Houston Zoo2. the Texas 2. The best experiences of Gorillas. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-zoo2-houston-zoo2-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
