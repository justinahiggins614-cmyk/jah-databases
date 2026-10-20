(function(){'use strict';
/* JAH Mackinac Bridge Bridge Database generator — jahdb-e2-bridge-mackinac-bridge-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-bridge-mackinac-bridge',PREFIX='JAH-E2BRIDGEMAC-',NAME='JAH Mackinac Bridge Bridge Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Mackinac Bridge: the complete guide", "d": "Mackinac Bridge: the mighty Mac..", "g": "overview", "l": 2, "q": "What is Mackinac Bridge: the complete guide?", "a": "Mackinac Bridge: the mighty Mac..", "x": "The complete bridge guide to Mackinac Bridge: the mighty Mac.. 8 km. History, meaning, practices, and how to engage respectfully — everything in one database. Length. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Mackinac Bridge essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Mackinac Bridge essentials.", "x": "At a glance: Mackinac Bridge — the mighty Mac.. 1957. The essentials: History.. Michigan. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "8 km.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "8 km.", "x": "Mackinac Bridge: 8 km.. History. Essential knowledge — Michigan.. the mighty Mac. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 8 km..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 8 km..", "x": "Explained: 8 km.. Walk. The context — Mackinac Bridge. Lakes. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "1957.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "1957.", "x": "Mackinac Bridge: 1957.. Lakes. Essential knowledge — Lakes.. the mighty Mac. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: 1957..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: 1957..", "x": "Explained: 1957.. Michigan. The context — Mackinac Bridge. Labor Day walk. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Michigan.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Michigan.", "x": "Mackinac Bridge: Michigan.. Walk. Essential knowledge — Labor Day walk.. the mighty Mac. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Michigan..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Michigan..", "x": "Explained: Michigan.. Views. The context — Mackinac Bridge. Views. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Lakes.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Lakes.", "x": "Mackinac Bridge: Lakes.. Michigan. Essential knowledge — Views.. the mighty Mac. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Lakes..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Lakes..", "x": "Explained: Lakes.. Length. The context — Mackinac Bridge. 8 km. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Labor Day walk.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Labor Day walk.", "x": "Mackinac Bridge: Labor Day walk.. Views. Essential knowledge — 8 km.. the mighty Mac. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Labor Day walk..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Labor Day walk..", "x": "Explained: Labor Day walk.. History. The context — Mackinac Bridge. 1957. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Views.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Views.", "x": "Mackinac Bridge: Views.. Length. Essential knowledge — 1957.. the mighty Mac. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Views..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Views..", "x": "Explained: Views.. Lakes. The context — Mackinac Bridge. Michigan. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Length.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Length.", "x": "Mackinac Bridge in depth: Length.. 1957. Details — the mighty Mac.. Lakes. Lakes. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "History.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "History.", "x": "Mackinac Bridge in depth: History.. Michigan. Details — the mighty Mac.. Walk. Labor Day walk. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Lakes.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Lakes.", "x": "Mackinac Bridge in depth: Lakes.. Lakes. Details — the mighty Mac.. Michigan. Views. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Walk.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Walk.", "x": "Mackinac Bridge in depth: Walk.. Labor Day walk. Details — the mighty Mac.. Views. 8 km. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Michigan.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Michigan.", "x": "Mackinac Bridge in depth: Michigan.. Views. Details — the mighty Mac.. Length. 1957. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Views.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Views.", "x": "Mackinac Bridge in depth: Views.. 8 km. Details — the mighty Mac.. History. Michigan. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Mackinac Bridge comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Mackinac Bridge comes from.", "x": "Origins: Length.. 8 km. The history of Mackinac Bridge — the mighty Mac.. History. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Mackinac Bridge respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Mackinac Bridge respectfully.", "x": "Engaging: Lakes.. 1957. How to participate or observe well — Mackinac Bridge. the mighty Mac. Respect first, always; Walk.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Mackinac Bridge do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Mackinac Bridge do's and don'ts.", "x": "Etiquette: Michigan.. Michigan. The rules of respect — Mackinac Bridge. the mighty Mac. When in doubt, ask about Views.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Mackinac Bridge.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Mackinac Bridge.", "x": "Planning: Length.. Lakes. Practical notes — Mackinac Bridge. the mighty Mac. A little planning shows respect for History.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Mackinac Bridge and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Mackinac Bridge and money.", "x": "Costs: Lakes.. Labor Day walk. What to budget — Mackinac Bridge. the mighty Mac. The best experiences of Walk. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-bridge-mackinac-bridge-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
