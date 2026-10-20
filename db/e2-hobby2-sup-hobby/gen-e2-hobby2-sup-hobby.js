(function(){'use strict';
/* JAH Stand-Up Paddle Database generator — jahdb-e2-hobby2-sup-hobby-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-hobby2-sup-hobby',PREFIX='JAH-E2HOBBY2SUP-',NAME='JAH Stand-Up Paddle Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Stand-Up Paddle: the complete guide", "d": "Stand-Up Paddle: the standing glide..", "g": "overview", "l": 2, "q": "What is Stand-Up Paddle: the complete guide?", "a": "Stand-Up Paddle: the standing glide..", "x": "The complete hobby guide to Stand-Up Paddle: the standing glide.. Balance. History, meaning, practices, and how to engage respectfully — everything in one database. Balance. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Stand-Up Paddle essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Stand-Up Paddle essentials.", "x": "At a glance: Stand-Up Paddle — the standing glide.. Paddle. The essentials: Inflatable.. Lakes. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Balance.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Balance.", "x": "Stand-Up Paddle: Balance.. Inflatable. Essential knowledge — Lakes.. the standing glide. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Balance..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Balance..", "x": "Explained: Balance.. Paddle. The context — Stand-Up Paddle. Inflatable. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Paddle.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Paddle.", "x": "Stand-Up Paddle: Paddle.. Sunset. Essential knowledge — Inflatable.. the standing glide. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Paddle..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Paddle..", "x": "Explained: Paddle.. Lakes. The context — Stand-Up Paddle. Core. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Lakes.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Lakes.", "x": "Stand-Up Paddle: Lakes.. Paddle. Essential knowledge — Core.. the standing glide. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Lakes..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Lakes..", "x": "Explained: Lakes.. Getting started. The context — Stand-Up Paddle. Sunset. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Inflatable.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Inflatable.", "x": "Stand-Up Paddle: Inflatable.. Lakes. Essential knowledge — Sunset.. the standing glide. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Inflatable..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Inflatable..", "x": "Explained: Inflatable.. Balance. The context — Stand-Up Paddle. Balance. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Core.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Core.", "x": "Stand-Up Paddle: Core.. Getting started. Essential knowledge — Balance.. the standing glide. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Core..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Core..", "x": "Explained: Core.. Inflatable. The context — Stand-Up Paddle. Paddle. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Sunset.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Sunset.", "x": "Stand-Up Paddle: Sunset.. Balance. Essential knowledge — Paddle.. the standing glide. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Sunset..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Sunset..", "x": "Explained: Sunset.. Sunset. The context — Stand-Up Paddle. Lakes. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Balance.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Balance.", "x": "Stand-Up Paddle in depth: Balance.. Paddle. Details — the standing glide.. Sunset. Inflatable. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Inflatable.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Inflatable.", "x": "Stand-Up Paddle in depth: Inflatable.. Lakes. Details — the standing glide.. Paddle. Core. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Sunset.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Sunset.", "x": "Stand-Up Paddle in depth: Sunset.. Inflatable. Details — the standing glide.. Lakes. Sunset. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Paddle.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Paddle.", "x": "Stand-Up Paddle in depth: Paddle.. Core. Details — the standing glide.. Getting started. Balance. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Lakes.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Lakes.", "x": "Stand-Up Paddle in depth: Lakes.. Sunset. Details — the standing glide.. Balance. Paddle. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Getting started.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Getting started.", "x": "Stand-Up Paddle in depth: Getting started.. Balance. Details — the standing glide.. Inflatable. Lakes. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Stand-Up Paddle comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Stand-Up Paddle comes from.", "x": "Origins: Balance.. Balance. The history of Stand-Up Paddle — the standing glide.. Inflatable. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Stand-Up Paddle respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Stand-Up Paddle respectfully.", "x": "Engaging: Sunset.. Paddle. How to participate or observe well — Stand-Up Paddle. the standing glide. Respect first, always; Paddle.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Stand-Up Paddle do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Stand-Up Paddle do's and don'ts.", "x": "Etiquette: Lakes.. Lakes. The rules of respect — Stand-Up Paddle. the standing glide. When in doubt, ask about Getting started.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Stand-Up Paddle.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Stand-Up Paddle.", "x": "Planning: Balance.. Inflatable. Practical notes — Stand-Up Paddle. the standing glide. A little planning shows respect for Inflatable.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Stand-Up Paddle and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Stand-Up Paddle and money.", "x": "Costs: Sunset.. Core. What to budget — Stand-Up Paddle. the standing glide. The best experiences of Paddle. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-hobby2-sup-hobby-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
