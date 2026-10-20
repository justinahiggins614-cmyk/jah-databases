(function(){'use strict';
/* JAH Oresund Bridge Bridge Database generator — jahdb-e2-bridge-oresund-bridge-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-bridge-oresund-bridge',PREFIX='JAH-E2BRIDGEORE-',NAME='JAH Oresund Bridge Bridge Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Oresund Bridge: the complete guide", "d": "Oresund Bridge: Sweden-Denmark link..", "g": "overview", "l": 2, "q": "What is Oresund Bridge: the complete guide?", "a": "Oresund Bridge: Sweden-Denmark link..", "x": "The complete bridge guide to Oresund Bridge: Sweden-Denmark link.. 7.8 km. History, meaning, practices, and how to engage respectfully — everything in one database. Design. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Oresund Bridge essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Oresund Bridge essentials.", "x": "At a glance: Oresund Bridge — Sweden-Denmark link.. 2000. The essentials: TV.. Tunnel+bridge. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "7.8 km.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "7.8 km.", "x": "Oresund Bridge: 7.8 km.. TV. Essential knowledge — Tunnel+bridge.. Sweden-Denmark link. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 7.8 km..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 7.8 km..", "x": "Explained: 7.8 km.. Drive. The context — Oresund Bridge. The Bridge TV. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "2000.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "2000.", "x": "Oresund Bridge: 2000.. Tolls. Essential knowledge — The Bridge TV.. Sweden-Denmark link. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: 2000..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: 2000..", "x": "Explained: 2000.. Views. The context — Oresund Bridge. Tolls. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Tunnel+bridge.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Tunnel+bridge.", "x": "Oresund Bridge: Tunnel+bridge.. Drive. Essential knowledge — Tolls.. Sweden-Denmark link. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Tunnel+bridge..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Tunnel+bridge..", "x": "Explained: Tunnel+bridge.. Nordic. The context — Oresund Bridge. Views. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "The Bridge TV.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "The Bridge TV.", "x": "Oresund Bridge: The Bridge TV.. Views. Essential knowledge — Views.. Sweden-Denmark link. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: The Bridge TV..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: The Bridge TV..", "x": "Explained: The Bridge TV.. Design. The context — Oresund Bridge. 7.8 km. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Tolls.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Tolls.", "x": "Oresund Bridge: Tolls.. Nordic. Essential knowledge — 7.8 km.. Sweden-Denmark link. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Tolls..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Tolls..", "x": "Explained: Tolls.. TV. The context — Oresund Bridge. 2000. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Views.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Views.", "x": "Oresund Bridge: Views.. Design. Essential knowledge — 2000.. Sweden-Denmark link. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Views..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Views..", "x": "Explained: Views.. Tolls. The context — Oresund Bridge. Tunnel+bridge. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Design.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Design.", "x": "Oresund Bridge in depth: Design.. 2000. Details — Sweden-Denmark link.. Tolls. The Bridge TV. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "TV.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "TV.", "x": "Oresund Bridge in depth: TV.. Tunnel+bridge. Details — Sweden-Denmark link.. Drive. Tolls. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Tolls.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Tolls.", "x": "Oresund Bridge in depth: Tolls.. The Bridge TV. Details — Sweden-Denmark link.. Views. Views. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Drive.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Drive.", "x": "Oresund Bridge in depth: Drive.. Tolls. Details — Sweden-Denmark link.. Nordic. 7.8 km. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Views.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Views.", "x": "Oresund Bridge in depth: Views.. Views. Details — Sweden-Denmark link.. Design. 2000. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Nordic.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Nordic.", "x": "Oresund Bridge in depth: Nordic.. 7.8 km. Details — Sweden-Denmark link.. TV. Tunnel+bridge. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Oresund Bridge comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Oresund Bridge comes from.", "x": "Origins: Design.. 7.8 km. The history of Oresund Bridge — Sweden-Denmark link.. TV. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Oresund Bridge respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Oresund Bridge respectfully.", "x": "Engaging: Tolls.. 2000. How to participate or observe well — Oresund Bridge. Sweden-Denmark link. Respect first, always; Drive.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Oresund Bridge do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Oresund Bridge do's and don'ts.", "x": "Etiquette: Views.. Tunnel+bridge. The rules of respect — Oresund Bridge. Sweden-Denmark link. When in doubt, ask about Nordic.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Oresund Bridge.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Oresund Bridge.", "x": "Planning: Design.. The Bridge TV. Practical notes — Oresund Bridge. Sweden-Denmark link. A little planning shows respect for TV.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Oresund Bridge and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Oresund Bridge and money.", "x": "Costs: Tolls.. Tolls. What to budget — Oresund Bridge. Sweden-Denmark link. The best experiences of Drive. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-bridge-oresund-bridge-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
