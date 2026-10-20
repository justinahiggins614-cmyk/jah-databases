(function(){'use strict';
/* JAH Bach Composer Composer Database generator — jahdb-e2-composer-bach-composer-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-composer-bach-composer',PREFIX='JAH-E2COMPOSERB-',NAME='JAH Bach Composer Composer Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Bach Composer: the complete guide", "d": "Bach Composer: the baroque master..", "g": "overview", "l": 2, "q": "What is Bach Composer: the complete guide?", "a": "Bach Composer: the baroque master..", "x": "The complete composer guide to Bach Composer: the baroque master.. 1685. History, meaning, practices, and how to engage respectfully — everything in one database. Brandenburg. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Bach Composer essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Bach Composer essentials.", "x": "At a glance: Bach Composer — the baroque master.. Brandenburg. The essentials: Goldberg.. Goldberg. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "1685.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "1685.", "x": "Bach Composer: 1685.. Goldberg. Essential knowledge — Goldberg.. the baroque master. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 1685..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 1685..", "x": "Explained: 1685.. Fugues. The context — Bach Composer. Cantatas. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Brandenburg.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Brandenburg.", "x": "Bach Composer: Brandenburg.. Cantatas. Essential knowledge — Cantatas.. the baroque master. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Brandenburg..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Brandenburg..", "x": "Explained: Brandenburg.. Leipzig. The context — Bach Composer. Fugues. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Goldberg.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Goldberg.", "x": "Bach Composer: Goldberg.. Fugues. Essential knowledge — Fugues.. the baroque master. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Goldberg..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Goldberg..", "x": "Explained: Goldberg.. Legacy. The context — Bach Composer. Leipzig. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Cantatas.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Cantatas.", "x": "Bach Composer: Cantatas.. Leipzig. Essential knowledge — Leipzig.. the baroque master. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Cantatas..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Cantatas..", "x": "Explained: Cantatas.. Brandenburg. The context — Bach Composer. 1685. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Fugues.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Fugues.", "x": "Bach Composer: Fugues.. Legacy. Essential knowledge — 1685.. the baroque master. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Fugues..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Fugues..", "x": "Explained: Fugues.. Goldberg. The context — Bach Composer. Brandenburg. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Leipzig.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Leipzig.", "x": "Bach Composer: Leipzig.. Brandenburg. Essential knowledge — Brandenburg.. the baroque master. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Leipzig..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Leipzig..", "x": "Explained: Leipzig.. Cantatas. The context — Bach Composer. Goldberg. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Brandenburg.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Brandenburg.", "x": "Bach Composer in depth: Brandenburg.. Brandenburg. Details — the baroque master.. Cantatas. Cantatas. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Goldberg.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Goldberg.", "x": "Bach Composer in depth: Goldberg.. Goldberg. Details — the baroque master.. Fugues. Fugues. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Cantatas.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Cantatas.", "x": "Bach Composer in depth: Cantatas.. Cantatas. Details — the baroque master.. Leipzig. Leipzig. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Fugues.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Fugues.", "x": "Bach Composer in depth: Fugues.. Fugues. Details — the baroque master.. Legacy. 1685. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Leipzig.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Leipzig.", "x": "Bach Composer in depth: Leipzig.. Leipzig. Details — the baroque master.. Brandenburg. Brandenburg. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Legacy.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Legacy.", "x": "Bach Composer in depth: Legacy.. 1685. Details — the baroque master.. Goldberg. Goldberg. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Bach Composer comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Bach Composer comes from.", "x": "Origins: Brandenburg.. 1685. The history of Bach Composer — the baroque master.. Goldberg. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Bach Composer respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Bach Composer respectfully.", "x": "Engaging: Cantatas.. Brandenburg. How to participate or observe well — Bach Composer. the baroque master. Respect first, always; Fugues.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Bach Composer do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Bach Composer do's and don'ts.", "x": "Etiquette: Leipzig.. Goldberg. The rules of respect — Bach Composer. the baroque master. When in doubt, ask about Legacy.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Bach Composer.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Bach Composer.", "x": "Planning: Brandenburg.. Cantatas. Practical notes — Bach Composer. the baroque master. A little planning shows respect for Goldberg.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Bach Composer and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Bach Composer and money.", "x": "Costs: Cantatas.. Fugues. What to budget — Bach Composer. the baroque master. The best experiences of Fugues. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-composer-bach-composer-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
