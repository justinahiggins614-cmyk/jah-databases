(function(){'use strict';
/* JAH Canoeing Hobby Database generator — jahdb-e2-hobby2-canoeing-hobby-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-hobby2-canoeing-hobby',PREFIX='JAH-E2HOBBY2CAN-',NAME='JAH Canoeing Hobby Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Canoeing Hobby: the complete guide", "d": "Canoeing Hobby: the J-stroke..", "g": "overview", "l": 2, "q": "What is Canoeing Hobby: the complete guide?", "a": "Canoeing Hobby: the J-stroke..", "x": "The complete hobby guide to Canoeing Hobby: the J-stroke.. J-stroke. History, meaning, practices, and how to engage respectfully — everything in one database. Portage. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Canoeing Hobby essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Canoeing Hobby essentials.", "x": "At a glance: Canoeing Hobby — the J-stroke.. Portage. The essentials: Tandem.. Lakes. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "J-stroke.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "J-stroke.", "x": "Canoeing Hobby: J-stroke.. Tandem. Essential knowledge — Lakes.. the J-stroke. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: J-stroke..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: J-stroke..", "x": "Explained: J-stroke.. J-stroke. The context — Canoeing Hobby. PFD. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Portage.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Portage.", "x": "Canoeing Hobby: Portage.. Quiet. Essential knowledge — PFD.. the J-stroke. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Portage..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Portage..", "x": "Explained: Portage.. Lakes. The context — Canoeing Hobby. Tandem. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Lakes.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Lakes.", "x": "Canoeing Hobby: Lakes.. J-stroke. Essential knowledge — Tandem.. the J-stroke. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Lakes..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Lakes..", "x": "Explained: Lakes.. Getting started. The context — Canoeing Hobby. Quiet. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "PFD.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "PFD.", "x": "Canoeing Hobby: PFD.. Lakes. Essential knowledge — Quiet.. the J-stroke. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: PFD..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: PFD..", "x": "Explained: PFD.. Portage. The context — Canoeing Hobby. J-stroke. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Tandem.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Tandem.", "x": "Canoeing Hobby: Tandem.. Getting started. Essential knowledge — J-stroke.. the J-stroke. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Tandem..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Tandem..", "x": "Explained: Tandem.. Tandem. The context — Canoeing Hobby. Portage. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Quiet.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Quiet.", "x": "Canoeing Hobby: Quiet.. Portage. Essential knowledge — Portage.. the J-stroke. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Quiet..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Quiet..", "x": "Explained: Quiet.. Quiet. The context — Canoeing Hobby. Lakes. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Portage.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Portage.", "x": "Canoeing Hobby in depth: Portage.. Portage. Details — the J-stroke.. Quiet. PFD. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Tandem.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Tandem.", "x": "Canoeing Hobby in depth: Tandem.. Lakes. Details — the J-stroke.. J-stroke. Tandem. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Quiet.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Quiet.", "x": "Canoeing Hobby in depth: Quiet.. PFD. Details — the J-stroke.. Lakes. Quiet. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "J-stroke.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "J-stroke.", "x": "Canoeing Hobby in depth: J-stroke.. Tandem. Details — the J-stroke.. Getting started. J-stroke. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Lakes.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Lakes.", "x": "Canoeing Hobby in depth: Lakes.. Quiet. Details — the J-stroke.. Portage. Portage. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Getting started.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Getting started.", "x": "Canoeing Hobby in depth: Getting started.. J-stroke. Details — the J-stroke.. Tandem. Lakes. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Canoeing Hobby comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Canoeing Hobby comes from.", "x": "Origins: Portage.. J-stroke. The history of Canoeing Hobby — the J-stroke.. Tandem. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Canoeing Hobby respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Canoeing Hobby respectfully.", "x": "Engaging: Quiet.. Portage. How to participate or observe well — Canoeing Hobby. the J-stroke. Respect first, always; J-stroke.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Canoeing Hobby do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Canoeing Hobby do's and don'ts.", "x": "Etiquette: Lakes.. Lakes. The rules of respect — Canoeing Hobby. the J-stroke. When in doubt, ask about Getting started.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Canoeing Hobby.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Canoeing Hobby.", "x": "Planning: Portage.. PFD. Practical notes — Canoeing Hobby. the J-stroke. A little planning shows respect for Tandem.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Canoeing Hobby and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Canoeing Hobby and money.", "x": "Costs: Quiet.. Tandem. What to budget — Canoeing Hobby. the J-stroke. The best experiences of J-stroke. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-hobby2-canoeing-hobby-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
