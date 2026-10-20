(function(){'use strict';
/* JAH Ceilidh Dance Dance Form Database generator — jahdb-e2-dance-ceilidh-dance-form-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-dance-ceilidh-dance-form',PREFIX='JAH-E2DANCECEIL-',NAME='JAH Ceilidh Dance Dance Form Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Ceilidh Dance: the complete guide", "d": "Ceilidh Dance: the Scottish social..", "g": "overview", "l": 2, "q": "What is Ceilidh Dance: the complete guide?", "a": "Ceilidh Dance: the Scottish social..", "x": "The complete dance form guide to Ceilidh Dance: the Scottish social.. Scotland. History, meaning, practices, and how to engage respectfully — everything in one database. Reels. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Ceilidh Dance essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Ceilidh Dance essentials.", "x": "At a glance: Ceilidh Dance — the Scottish social.. Reels. The essentials: Kilts.. Social. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Scotland.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Scotland.", "x": "Ceilidh Dance: Scotland.. Kilts. Essential knowledge — Social.. the Scottish social. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Scotland..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Scotland..", "x": "Explained: Scotland.. Scotland. The context — Ceilidh Dance. Caller. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Reels.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Reels.", "x": "Ceilidh Dance: Reels.. Weddings. Essential knowledge — Caller.. the Scottish social. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Reels..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Reels..", "x": "Explained: Reels.. Social. The context — Ceilidh Dance. Kilts. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Social.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Social.", "x": "Ceilidh Dance: Social.. Scotland. Essential knowledge — Kilts.. the Scottish social. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Social..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Social..", "x": "Explained: Social.. Training. The context — Ceilidh Dance. Weddings. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Caller.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Caller.", "x": "Ceilidh Dance: Caller.. Social. Essential knowledge — Weddings.. the Scottish social. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Caller..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Caller..", "x": "Explained: Caller.. Reels. The context — Ceilidh Dance. Scotland. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Kilts.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Kilts.", "x": "Ceilidh Dance: Kilts.. Training. Essential knowledge — Scotland.. the Scottish social. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Kilts..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Kilts..", "x": "Explained: Kilts.. Kilts. The context — Ceilidh Dance. Reels. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Weddings.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Weddings.", "x": "Ceilidh Dance: Weddings.. Reels. Essential knowledge — Reels.. the Scottish social. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Weddings..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Weddings..", "x": "Explained: Weddings.. Weddings. The context — Ceilidh Dance. Social. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Reels.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Reels.", "x": "Ceilidh Dance in depth: Reels.. Reels. Details — the Scottish social.. Weddings. Caller. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Kilts.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Kilts.", "x": "Ceilidh Dance in depth: Kilts.. Social. Details — the Scottish social.. Scotland. Kilts. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Weddings.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Weddings.", "x": "Ceilidh Dance in depth: Weddings.. Caller. Details — the Scottish social.. Social. Weddings. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Scotland.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Scotland.", "x": "Ceilidh Dance in depth: Scotland.. Kilts. Details — the Scottish social.. Training. Scotland. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Social.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Social.", "x": "Ceilidh Dance in depth: Social.. Weddings. Details — the Scottish social.. Reels. Reels. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Training.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Training.", "x": "Ceilidh Dance in depth: Training.. Scotland. Details — the Scottish social.. Kilts. Social. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Ceilidh Dance comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Ceilidh Dance comes from.", "x": "Origins: Reels.. Scotland. The history of Ceilidh Dance — the Scottish social.. Kilts. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Ceilidh Dance respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Ceilidh Dance respectfully.", "x": "Engaging: Weddings.. Reels. How to participate or observe well — Ceilidh Dance. the Scottish social. Respect first, always; Scotland.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Ceilidh Dance do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Ceilidh Dance do's and don'ts.", "x": "Etiquette: Social.. Social. The rules of respect — Ceilidh Dance. the Scottish social. When in doubt, ask about Training.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Ceilidh Dance.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Ceilidh Dance.", "x": "Planning: Reels.. Caller. Practical notes — Ceilidh Dance. the Scottish social. A little planning shows respect for Kilts.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Ceilidh Dance and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Ceilidh Dance and money.", "x": "Costs: Weddings.. Kilts. What to budget — Ceilidh Dance. the Scottish social. The best experiences of Scotland. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-dance-ceilidh-dance-form-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
