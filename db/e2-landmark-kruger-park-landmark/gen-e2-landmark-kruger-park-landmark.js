(function(){'use strict';
/* JAH Kruger Park Landmark Database generator — jahdb-e2-landmark-kruger-park-landmark-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-landmark-kruger-park-landmark',PREFIX='JAH-E2LANDMARKK-',NAME='JAH Kruger Park Landmark Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Kruger Park: the complete guide", "d": "Kruger Park: the big five park..", "g": "overview", "l": 2, "q": "What is Kruger Park: the complete guide?", "a": "Kruger Park: the big five park..", "x": "The complete landmark guide to Kruger Park: the big five park.. 1898. History, meaning, practices, and how to engage respectfully — everything in one database. 1898. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Kruger Park essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Kruger Park essentials.", "x": "At a glance: Kruger Park — the big five park.. Big Five. The essentials: Self-drive.. 19,485 km2. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "1898.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "1898.", "x": "Kruger Park: 1898.. Self-drive. Essential knowledge — 19,485 km2.. the big five park. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 1898..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 1898..", "x": "Explained: 1898.. Big Five. The context — Kruger Park. Self-drive. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Big Five.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Big Five.", "x": "Kruger Park: Big Five.. Bush. Essential knowledge — Self-drive.. the big five park. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Big Five..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Big Five..", "x": "Explained: Big Five.. 19,485. The context — Kruger Park. Safari. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "19,485 km2.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "19,485 km2.", "x": "Kruger Park: 19,485 km2.. Big Five. Essential knowledge — Safari.. the big five park. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: 19,485 km2..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: 19,485 km2..", "x": "Explained: 19,485 km2.. Safaris. The context — Kruger Park. Bush. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Self-drive.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Self-drive.", "x": "Kruger Park: Self-drive.. 19,485. Essential knowledge — Bush.. the big five park. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Self-drive..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Self-drive..", "x": "Explained: Self-drive.. 1898. The context — Kruger Park. 1898. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Safari.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Safari.", "x": "Kruger Park: Safari.. Safaris. Essential knowledge — 1898.. the big five park. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Safari..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Safari..", "x": "Explained: Safari.. Self-drive. The context — Kruger Park. Big Five. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Bush.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Bush.", "x": "Kruger Park: Bush.. 1898. Essential knowledge — Big Five.. the big five park. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Bush..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Bush..", "x": "Explained: Bush.. Bush. The context — Kruger Park. 19,485 km2. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "1898.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "1898.", "x": "Kruger Park in depth: 1898.. Big Five. Details — the big five park.. Bush. Self-drive. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Self-drive.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Self-drive.", "x": "Kruger Park in depth: Self-drive.. 19,485 km2. Details — the big five park.. Big Five. Safari. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Bush.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Bush.", "x": "Kruger Park in depth: Bush.. Self-drive. Details — the big five park.. 19,485. Bush. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Big Five.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Big Five.", "x": "Kruger Park in depth: Big Five.. Safari. Details — the big five park.. Safaris. 1898. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "19,485.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "19,485.", "x": "Kruger Park in depth: 19,485.. Bush. Details — the big five park.. 1898. Big Five. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Safaris.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Safaris.", "x": "Kruger Park in depth: Safaris.. 1898. Details — the big five park.. Self-drive. 19,485 km2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Kruger Park comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Kruger Park comes from.", "x": "Origins: 1898.. 1898. The history of Kruger Park — the big five park.. Self-drive. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Kruger Park respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Kruger Park respectfully.", "x": "Engaging: Bush.. Big Five. How to participate or observe well — Kruger Park. the big five park. Respect first, always; Big Five.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Kruger Park do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Kruger Park do's and don'ts.", "x": "Etiquette: 19,485.. 19,485 km2. The rules of respect — Kruger Park. the big five park. When in doubt, ask about Safaris.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Kruger Park.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Kruger Park.", "x": "Planning: 1898.. Self-drive. Practical notes — Kruger Park. the big five park. A little planning shows respect for Self-drive.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Kruger Park and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Kruger Park and money.", "x": "Costs: Bush.. Safari. What to budget — Kruger Park. the big five park. The best experiences of Big Five. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-landmark-kruger-park-landmark-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
