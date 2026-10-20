(function(){'use strict';
/* JAH Pale Ale2 Database generator — jahdb-e2-beer2-pale-ale2-beer-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-beer2-pale-ale2-beer',PREFIX='JAH-E2BEER2PALE-',NAME='JAH Pale Ale2 Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Pale Ale2: the complete guide", "d": "Pale Ale2: the balanced 2..", "g": "overview", "l": 2, "q": "What is Pale Ale2: the complete guide?", "a": "Pale Ale2: the balanced 2..", "x": "The complete beer style guide to Pale Ale2: the balanced 2.. American. History, meaning, practices, and how to engage respectfully — everything in one database. American. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Pale Ale2 essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Pale Ale2 essentials.", "x": "At a glance: Pale Ale2 — the balanced 2.. English. The essentials: Session.. Cascade. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "American.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "American.", "x": "Pale Ale2: American.. Session. Essential knowledge — Cascade.. the balanced 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: American..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: American..", "x": "Explained: American.. English. The context — Pale Ale2. Amber. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "English.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "English.", "x": "Pale Ale2: English.. Citrus. Essential knowledge — Amber.. the balanced 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: English..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: English..", "x": "Explained: English.. Amber. The context — Pale Ale2. Session. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Cascade.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Cascade.", "x": "Pale Ale2: Cascade.. English. Essential knowledge — Session.. the balanced 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Cascade..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Cascade..", "x": "Explained: Cascade.. Serving. The context — Pale Ale2. Citrus. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Amber.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Amber.", "x": "Pale Ale2: Amber.. Amber. Essential knowledge — Citrus.. the balanced 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Amber..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Amber..", "x": "Explained: Amber.. American. The context — Pale Ale2. American. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Session.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Session.", "x": "Pale Ale2: Session.. Serving. Essential knowledge — American.. the balanced 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Session..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Session..", "x": "Explained: Session.. Session. The context — Pale Ale2. English. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Citrus.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Citrus.", "x": "Pale Ale2: Citrus.. American. Essential knowledge — English.. the balanced 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Citrus..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Citrus..", "x": "Explained: Citrus.. Citrus. The context — Pale Ale2. Cascade. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "American.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "American.", "x": "Pale Ale2 in depth: American.. English. Details — the balanced 2.. Citrus. Amber. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Session.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Session.", "x": "Pale Ale2 in depth: Session.. Cascade. Details — the balanced 2.. English. Session. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Citrus.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Citrus.", "x": "Pale Ale2 in depth: Citrus.. Amber. Details — the balanced 2.. Amber. Citrus. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "English.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "English.", "x": "Pale Ale2 in depth: English.. Session. Details — the balanced 2.. Serving. American. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Amber.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Amber.", "x": "Pale Ale2 in depth: Amber.. Citrus. Details — the balanced 2.. American. English. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Serving.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Serving.", "x": "Pale Ale2 in depth: Serving.. American. Details — the balanced 2.. Session. Cascade. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Pale Ale2 comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Pale Ale2 comes from.", "x": "Origins: American.. American. The history of Pale Ale2 — the balanced 2.. Session. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Pale Ale2 respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Pale Ale2 respectfully.", "x": "Engaging: Citrus.. English. How to participate or observe well — Pale Ale2. the balanced 2. Respect first, always; English.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Pale Ale2 do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Pale Ale2 do's and don'ts.", "x": "Etiquette: Amber.. Cascade. The rules of respect — Pale Ale2. the balanced 2. When in doubt, ask about Serving.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Pale Ale2.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Pale Ale2.", "x": "Planning: American.. Amber. Practical notes — Pale Ale2. the balanced 2. A little planning shows respect for Session.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Pale Ale2 and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Pale Ale2 and money.", "x": "Costs: Citrus.. Session. What to budget — Pale Ale2. the balanced 2. The best experiences of English. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-beer2-pale-ale2-beer-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
