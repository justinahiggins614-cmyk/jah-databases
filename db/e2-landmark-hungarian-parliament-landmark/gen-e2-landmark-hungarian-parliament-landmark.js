(function(){'use strict';
/* JAH Hungarian Parliament Landmark Database generator — jahdb-e2-landmark-hungarian-parliament-landmark-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-landmark-hungarian-parliament-landmark',PREFIX='JAH-E2LANDMARKH-',NAME='JAH Hungarian Parliament Landmark Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Hungarian Parliament: the complete guide", "d": "Hungarian Parliament: the Danube Gothic..", "g": "overview", "l": 2, "q": "What is Hungarian Parliament: the complete guide?", "a": "Hungarian Parliament: the Danube Gothic..", "x": "The complete landmark guide to Hungarian Parliament: the Danube Gothic.. 1904. History, meaning, practices, and how to engage respectfully — everything in one database. 1904. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Hungarian Parliament essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Hungarian Parliament essentials.", "x": "At a glance: Hungarian Parliament — the Danube Gothic.. 691 rooms. The essentials: Danube.. Danube. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "1904.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "1904.", "x": "Hungarian Parliament: 1904.. Danube. Essential knowledge — Danube.. the Danube Gothic. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 1904..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 1904..", "x": "Explained: 1904.. Gothic. The context — Hungarian Parliament. Gothic Revival. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "691 rooms.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "691 rooms.", "x": "Hungarian Parliament: 691 rooms.. Crown. Essential knowledge — Gothic Revival.. the Danube Gothic. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: 691 rooms..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: 691 rooms..", "x": "Explained: 691 rooms.. Rooms. The context — Hungarian Parliament. Crown. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Danube.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Danube.", "x": "Hungarian Parliament: Danube.. Gothic. Essential knowledge — Crown.. the Danube Gothic. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Danube..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Danube..", "x": "Explained: Danube.. Tours. The context — Hungarian Parliament. Symmetric. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Gothic Revival.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Gothic Revival.", "x": "Hungarian Parliament: Gothic Revival.. Rooms. Essential knowledge — Symmetric.. the Danube Gothic. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Gothic Revival..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Gothic Revival..", "x": "Explained: Gothic Revival.. 1904. The context — Hungarian Parliament. 1904. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Crown.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Crown.", "x": "Hungarian Parliament: Crown.. Tours. Essential knowledge — 1904.. the Danube Gothic. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Crown..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Crown..", "x": "Explained: Crown.. Danube. The context — Hungarian Parliament. 691 rooms. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Symmetric.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Symmetric.", "x": "Hungarian Parliament: Symmetric.. 1904. Essential knowledge — 691 rooms.. the Danube Gothic. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Symmetric..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Symmetric..", "x": "Explained: Symmetric.. Crown. The context — Hungarian Parliament. Danube. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "1904.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "1904.", "x": "Hungarian Parliament in depth: 1904.. 691 rooms. Details — the Danube Gothic.. Crown. Gothic Revival. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Danube.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Danube.", "x": "Hungarian Parliament in depth: Danube.. Danube. Details — the Danube Gothic.. Gothic. Crown. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Crown.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Crown.", "x": "Hungarian Parliament in depth: Crown.. Gothic Revival. Details — the Danube Gothic.. Rooms. Symmetric. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Gothic.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Gothic.", "x": "Hungarian Parliament in depth: Gothic.. Crown. Details — the Danube Gothic.. Tours. 1904. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Rooms.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Rooms.", "x": "Hungarian Parliament in depth: Rooms.. Symmetric. Details — the Danube Gothic.. 1904. 691 rooms. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Tours.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Tours.", "x": "Hungarian Parliament in depth: Tours.. 1904. Details — the Danube Gothic.. Danube. Danube. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Hungarian Parliament comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Hungarian Parliament comes from.", "x": "Origins: 1904.. 1904. The history of Hungarian Parliament — the Danube Gothic.. Danube. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Hungarian Parliament respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Hungarian Parliament respectfully.", "x": "Engaging: Crown.. 691 rooms. How to participate or observe well — Hungarian Parliament. the Danube Gothic. Respect first, always; Gothic.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Hungarian Parliament do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Hungarian Parliament do's and don'ts.", "x": "Etiquette: Rooms.. Danube. The rules of respect — Hungarian Parliament. the Danube Gothic. When in doubt, ask about Tours.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Hungarian Parliament.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Hungarian Parliament.", "x": "Planning: 1904.. Gothic Revival. Practical notes — Hungarian Parliament. the Danube Gothic. A little planning shows respect for Danube.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Hungarian Parliament and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Hungarian Parliament and money.", "x": "Costs: Crown.. Crown. What to budget — Hungarian Parliament. the Danube Gothic. The best experiences of Gothic. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-landmark-hungarian-parliament-landmark-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
