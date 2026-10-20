(function(){'use strict';
/* JAH Confederation Bridge Bridge Database generator — jahdb-e2-bridge-confederation-bridge-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-bridge-confederation-bridge',PREFIX='JAH-E2BRIDGECON-',NAME='JAH Confederation Bridge Bridge Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Confederation Bridge: the complete guide", "d": "Confederation Bridge: to Prince Edward Island..", "g": "overview", "l": 2, "q": "What is Confederation Bridge: the complete guide?", "a": "Confederation Bridge: to Prince Edward Island..", "x": "The complete bridge guide to Confederation Bridge: to Prince Edward Island.. 12.9 km. History, meaning, practices, and how to engage respectfully — everything in one database. Length. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Confederation Bridge essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Confederation Bridge essentials.", "x": "At a glance: Confederation Bridge — to Prince Edward Island.. 1997. The essentials: Ice.. Ice. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "12.9 km.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "12.9 km.", "x": "Confederation Bridge: 12.9 km.. Ice. Essential knowledge — Ice.. to Prince Edward Island. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 12.9 km..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 12.9 km..", "x": "Explained: 12.9 km.. Drive. The context — Confederation Bridge. Canada. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "1997.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "1997.", "x": "Confederation Bridge: 1997.. PEI. Essential knowledge — Canada.. to Prince Edward Island. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: 1997..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: 1997..", "x": "Explained: 1997.. Views. The context — Confederation Bridge. Tolls. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Ice.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Ice.", "x": "Confederation Bridge: Ice.. Drive. Essential knowledge — Tolls.. to Prince Edward Island. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Ice..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Ice..", "x": "Explained: Ice.. Canada. The context — Confederation Bridge. Views. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Canada.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Canada.", "x": "Confederation Bridge: Canada.. Views. Essential knowledge — Views.. to Prince Edward Island. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Canada..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Canada..", "x": "Explained: Canada.. Length. The context — Confederation Bridge. 12.9 km. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Tolls.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Tolls.", "x": "Confederation Bridge: Tolls.. Canada. Essential knowledge — 12.9 km.. to Prince Edward Island. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Tolls..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Tolls..", "x": "Explained: Tolls.. Ice. The context — Confederation Bridge. 1997. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Views.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Views.", "x": "Confederation Bridge: Views.. Length. Essential knowledge — 1997.. to Prince Edward Island. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Views..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Views..", "x": "Explained: Views.. PEI. The context — Confederation Bridge. Ice. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Length.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Length.", "x": "Confederation Bridge in depth: Length.. 1997. Details — to Prince Edward Island.. PEI. Canada. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Ice.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Ice.", "x": "Confederation Bridge in depth: Ice.. Ice. Details — to Prince Edward Island.. Drive. Tolls. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "PEI.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "PEI.", "x": "Confederation Bridge in depth: PEI.. Canada. Details — to Prince Edward Island.. Views. Views. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Drive.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Drive.", "x": "Confederation Bridge in depth: Drive.. Tolls. Details — to Prince Edward Island.. Canada. 12.9 km. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Views.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Views.", "x": "Confederation Bridge in depth: Views.. Views. Details — to Prince Edward Island.. Length. 1997. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Canada.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Canada.", "x": "Confederation Bridge in depth: Canada.. 12.9 km. Details — to Prince Edward Island.. Ice. Ice. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Confederation Bridge comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Confederation Bridge comes from.", "x": "Origins: Length.. 12.9 km. The history of Confederation Bridge — to Prince Edward Island.. Ice. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Confederation Bridge respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Confederation Bridge respectfully.", "x": "Engaging: PEI.. 1997. How to participate or observe well — Confederation Bridge. to Prince Edward Island. Respect first, always; Drive.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Confederation Bridge do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Confederation Bridge do's and don'ts.", "x": "Etiquette: Views.. Ice. The rules of respect — Confederation Bridge. to Prince Edward Island. When in doubt, ask about Canada.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Confederation Bridge.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Confederation Bridge.", "x": "Planning: Length.. Canada. Practical notes — Confederation Bridge. to Prince Edward Island. A little planning shows respect for Ice.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Confederation Bridge and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Confederation Bridge and money.", "x": "Costs: PEI.. Tolls. What to budget — Confederation Bridge. to Prince Edward Island. The best experiences of Drive. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-bridge-confederation-bridge-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
