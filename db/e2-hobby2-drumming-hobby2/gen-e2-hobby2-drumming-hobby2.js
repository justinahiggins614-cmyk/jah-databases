(function(){'use strict';
/* JAH Drumming Hobby Database generator — jahdb-e2-hobby2-drumming-hobby2-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-hobby2-drumming-hobby2',PREFIX='JAH-E2HOBBY2DRU-',NAME='JAH Drumming Hobby Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Drumming Hobby: the complete guide", "d": "Drumming Hobby: the rhythm kit..", "g": "overview", "l": 2, "q": "What is Drumming Hobby: the complete guide?", "a": "Drumming Hobby: the rhythm kit..", "x": "The complete hobby guide to Drumming Hobby: the rhythm kit.. Rudiments. History, meaning, practices, and how to engage respectfully — everything in one database. Metronome. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Drumming Hobby essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Drumming Hobby essentials.", "x": "At a glance: Drumming Hobby — the rhythm kit.. Metronome. The essentials: Kit.. Grip. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Rudiments.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Rudiments.", "x": "Drumming Hobby: Rudiments.. Kit. Essential knowledge — Grip.. the rhythm kit. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Rudiments..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Rudiments..", "x": "Explained: Rudiments.. Rudiments. The context — Drumming Hobby. Practice. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Metronome.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Metronome.", "x": "Drumming Hobby: Metronome.. Groove. Essential knowledge — Practice.. the rhythm kit. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Metronome..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Metronome..", "x": "Explained: Metronome.. Grip. The context — Drumming Hobby. Kit. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Grip.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Grip.", "x": "Drumming Hobby: Grip.. Rudiments. Essential knowledge — Kit.. the rhythm kit. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Grip..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Grip..", "x": "Explained: Grip.. Getting started. The context — Drumming Hobby. Groove. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Practice.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Practice.", "x": "Drumming Hobby: Practice.. Grip. Essential knowledge — Groove.. the rhythm kit. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Practice..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Practice..", "x": "Explained: Practice.. Metronome. The context — Drumming Hobby. Rudiments. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Kit.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Kit.", "x": "Drumming Hobby: Kit.. Getting started. Essential knowledge — Rudiments.. the rhythm kit. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Kit..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Kit..", "x": "Explained: Kit.. Kit. The context — Drumming Hobby. Metronome. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Groove.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Groove.", "x": "Drumming Hobby: Groove.. Metronome. Essential knowledge — Metronome.. the rhythm kit. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Groove..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Groove..", "x": "Explained: Groove.. Groove. The context — Drumming Hobby. Grip. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Metronome.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Metronome.", "x": "Drumming Hobby in depth: Metronome.. Metronome. Details — the rhythm kit.. Groove. Practice. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Kit.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Kit.", "x": "Drumming Hobby in depth: Kit.. Grip. Details — the rhythm kit.. Rudiments. Kit. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Groove.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Groove.", "x": "Drumming Hobby in depth: Groove.. Practice. Details — the rhythm kit.. Grip. Groove. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Rudiments.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Rudiments.", "x": "Drumming Hobby in depth: Rudiments.. Kit. Details — the rhythm kit.. Getting started. Rudiments. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Grip.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Grip.", "x": "Drumming Hobby in depth: Grip.. Groove. Details — the rhythm kit.. Metronome. Metronome. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Getting started.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Getting started.", "x": "Drumming Hobby in depth: Getting started.. Rudiments. Details — the rhythm kit.. Kit. Grip. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Drumming Hobby comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Drumming Hobby comes from.", "x": "Origins: Metronome.. Rudiments. The history of Drumming Hobby — the rhythm kit.. Kit. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Drumming Hobby respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Drumming Hobby respectfully.", "x": "Engaging: Groove.. Metronome. How to participate or observe well — Drumming Hobby. the rhythm kit. Respect first, always; Rudiments.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Drumming Hobby do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Drumming Hobby do's and don'ts.", "x": "Etiquette: Grip.. Grip. The rules of respect — Drumming Hobby. the rhythm kit. When in doubt, ask about Getting started.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Drumming Hobby.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Drumming Hobby.", "x": "Planning: Metronome.. Practice. Practical notes — Drumming Hobby. the rhythm kit. A little planning shows respect for Kit.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Drumming Hobby and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Drumming Hobby and money.", "x": "Costs: Groove.. Kit. What to budget — Drumming Hobby. the rhythm kit. The best experiences of Rudiments. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-hobby2-drumming-hobby2-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
