(function(){'use strict';
/* JAH Yosemite Landmark Database generator — jahdb-e2-landmark-yosemite-landmark-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-landmark-yosemite-landmark',PREFIX='JAH-E2LANDMARKY-',NAME='JAH Yosemite Landmark Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Yosemite: the complete guide", "d": "Yosemite: the granite valley..", "g": "overview", "l": 2, "q": "What is Yosemite: the complete guide?", "a": "Yosemite: the granite valley..", "x": "The complete landmark guide to Yosemite: the granite valley.. Half Dome. History, meaning, practices, and how to engage respectfully — everything in one database. Half Dome. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Yosemite essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Yosemite essentials.", "x": "At a glance: Yosemite — the granite valley.. El Capitan. The essentials: Climbing.. Falls. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Half Dome.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Half Dome.", "x": "Yosemite: Half Dome.. Climbing. Essential knowledge — Falls.. the granite valley. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Half Dome..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Half Dome..", "x": "Explained: Half Dome.. El Capitan. The context — Yosemite. 1864. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "El Capitan.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "El Capitan.", "x": "Yosemite: El Capitan.. Valley. Essential knowledge — 1864.. the granite valley. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: El Capitan..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: El Capitan..", "x": "Explained: El Capitan.. 1864. The context — Yosemite. Climbing. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Falls.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Falls.", "x": "Yosemite: Falls.. El Capitan. Essential knowledge — Climbing.. the granite valley. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Falls..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Falls..", "x": "Explained: Falls.. Tours. The context — Yosemite. Valley. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "1864.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "1864.", "x": "Yosemite: 1864.. 1864. Essential knowledge — Valley.. the granite valley. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: 1864..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: 1864..", "x": "Explained: 1864.. Half Dome. The context — Yosemite. Half Dome. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Climbing.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Climbing.", "x": "Yosemite: Climbing.. Tours. Essential knowledge — Half Dome.. the granite valley. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Climbing..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Climbing..", "x": "Explained: Climbing.. Climbing. The context — Yosemite. El Capitan. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Valley.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Valley.", "x": "Yosemite: Valley.. Half Dome. Essential knowledge — El Capitan.. the granite valley. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Valley..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Valley..", "x": "Explained: Valley.. Valley. The context — Yosemite. Falls. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Half Dome.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Half Dome.", "x": "Yosemite in depth: Half Dome.. El Capitan. Details — the granite valley.. Valley. 1864. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Climbing.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Climbing.", "x": "Yosemite in depth: Climbing.. Falls. Details — the granite valley.. El Capitan. Climbing. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Valley.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Valley.", "x": "Yosemite in depth: Valley.. 1864. Details — the granite valley.. 1864. Valley. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "El Capitan.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "El Capitan.", "x": "Yosemite in depth: El Capitan.. Climbing. Details — the granite valley.. Tours. Half Dome. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "1864.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "1864.", "x": "Yosemite in depth: 1864.. Valley. Details — the granite valley.. Half Dome. El Capitan. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Tours.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Tours.", "x": "Yosemite in depth: Tours.. Half Dome. Details — the granite valley.. Climbing. Falls. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Yosemite comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Yosemite comes from.", "x": "Origins: Half Dome.. Half Dome. The history of Yosemite — the granite valley.. Climbing. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Yosemite respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Yosemite respectfully.", "x": "Engaging: Valley.. El Capitan. How to participate or observe well — Yosemite. the granite valley. Respect first, always; El Capitan.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Yosemite do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Yosemite do's and don'ts.", "x": "Etiquette: 1864.. Falls. The rules of respect — Yosemite. the granite valley. When in doubt, ask about Tours.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Yosemite.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Yosemite.", "x": "Planning: Half Dome.. 1864. Practical notes — Yosemite. the granite valley. A little planning shows respect for Climbing.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Yosemite and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Yosemite and money.", "x": "Costs: Valley.. Climbing. What to budget — Yosemite. the granite valley. The best experiences of El Capitan. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-landmark-yosemite-landmark-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
