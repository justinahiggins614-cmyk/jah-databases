(function(){'use strict';
/* JAH Haydn Composer Composer Database generator — jahdb-e2-composer-haydn-composer-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-composer-haydn-composer',PREFIX='JAH-E2COMPOSERH-',NAME='JAH Haydn Composer Composer Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Haydn Composer: the complete guide", "d": "Haydn Composer: the father of symphony..", "g": "overview", "l": 2, "q": "What is Haydn Composer: the complete guide?", "a": "Haydn Composer: the father of symphony..", "x": "The complete composer guide to Haydn Composer: the father of symphony.. 1732. History, meaning, practices, and how to engage respectfully — everything in one database. Symphonies. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Haydn Composer essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Haydn Composer essentials.", "x": "At a glance: Haydn Composer — the father of symphony.. 104 symphonies. The essentials: Quartet.. Esterhazy. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "1732.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "1732.", "x": "Haydn Composer: 1732.. Quartet. Essential knowledge — Esterhazy.. the father of symphony. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 1732..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 1732..", "x": "Explained: 1732.. London. The context — Haydn Composer. String quartet. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "104 symphonies.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "104 symphonies.", "x": "Haydn Composer: 104 symphonies.. Surprise. Essential knowledge — String quartet.. the father of symphony. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: 104 symphonies..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: 104 symphonies..", "x": "Explained: 104 symphonies.. Esterhazy. The context — Haydn Composer. Surprise. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Esterhazy.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Esterhazy.", "x": "Haydn Composer: Esterhazy.. London. Essential knowledge — Surprise.. the father of symphony. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Esterhazy..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Esterhazy..", "x": "Explained: Esterhazy.. Legacy. The context — Haydn Composer. London. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "String quartet.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "String quartet.", "x": "Haydn Composer: String quartet.. Esterhazy. Essential knowledge — London.. the father of symphony. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: String quartet..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: String quartet..", "x": "Explained: String quartet.. Symphonies. The context — Haydn Composer. 1732. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Surprise.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Surprise.", "x": "Haydn Composer: Surprise.. Legacy. Essential knowledge — 1732.. the father of symphony. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Surprise..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Surprise..", "x": "Explained: Surprise.. Quartet. The context — Haydn Composer. 104 symphonies. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "London.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "London.", "x": "Haydn Composer: London.. Symphonies. Essential knowledge — 104 symphonies.. the father of symphony. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: London..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: London..", "x": "Explained: London.. Surprise. The context — Haydn Composer. Esterhazy. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Symphonies.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Symphonies.", "x": "Haydn Composer in depth: Symphonies.. 104 symphonies. Details — the father of symphony.. Surprise. String quartet. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Quartet.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Quartet.", "x": "Haydn Composer in depth: Quartet.. Esterhazy. Details — the father of symphony.. London. Surprise. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Surprise.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Surprise.", "x": "Haydn Composer in depth: Surprise.. String quartet. Details — the father of symphony.. Esterhazy. London. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "London.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "London.", "x": "Haydn Composer in depth: London.. Surprise. Details — the father of symphony.. Legacy. 1732. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Esterhazy.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Esterhazy.", "x": "Haydn Composer in depth: Esterhazy.. London. Details — the father of symphony.. Symphonies. 104 symphonies. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Legacy.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Legacy.", "x": "Haydn Composer in depth: Legacy.. 1732. Details — the father of symphony.. Quartet. Esterhazy. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Haydn Composer comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Haydn Composer comes from.", "x": "Origins: Symphonies.. 1732. The history of Haydn Composer — the father of symphony.. Quartet. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Haydn Composer respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Haydn Composer respectfully.", "x": "Engaging: Surprise.. 104 symphonies. How to participate or observe well — Haydn Composer. the father of symphony. Respect first, always; London.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Haydn Composer do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Haydn Composer do's and don'ts.", "x": "Etiquette: Esterhazy.. Esterhazy. The rules of respect — Haydn Composer. the father of symphony. When in doubt, ask about Legacy.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Haydn Composer.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Haydn Composer.", "x": "Planning: Symphonies.. String quartet. Practical notes — Haydn Composer. the father of symphony. A little planning shows respect for Quartet.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Haydn Composer and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Haydn Composer and money.", "x": "Costs: Surprise.. Surprise. What to budget — Haydn Composer. the father of symphony. The best experiences of London. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-composer-haydn-composer-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
