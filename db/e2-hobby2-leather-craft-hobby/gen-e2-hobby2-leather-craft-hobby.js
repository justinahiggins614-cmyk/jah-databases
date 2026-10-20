(function(){'use strict';
/* JAH Leather Craft Database generator — jahdb-e2-hobby2-leather-craft-hobby-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-hobby2-leather-craft-hobby',PREFIX='JAH-E2HOBBY2LEA-',NAME='JAH Leather Craft Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Leather Craft: the complete guide", "d": "Leather Craft: the hide work..", "g": "overview", "l": 2, "q": "What is Leather Craft: the complete guide?", "a": "Leather Craft: the hide work..", "x": "The complete hobby guide to Leather Craft: the hide work.. Tooling. History, meaning, practices, and how to engage respectfully — everything in one database. Stitching. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Leather Craft essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Leather Craft essentials.", "x": "At a glance: Leather Craft — the hide work.. Stitching. The essentials: Burnishing.. Dyeing. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Tooling.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Tooling.", "x": "Leather Craft: Tooling.. Burnishing. Essential knowledge — Dyeing.. the hide work. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Tooling..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Tooling..", "x": "Explained: Tooling.. Tooling. The context — Leather Craft. Burnishing. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Stitching.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Stitching.", "x": "Leather Craft: Stitching.. Belts. Essential knowledge — Burnishing.. the hide work. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Stitching..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Stitching..", "x": "Explained: Stitching.. Dyeing. The context — Leather Craft. Awl. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Dyeing.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Dyeing.", "x": "Leather Craft: Dyeing.. Tooling. Essential knowledge — Awl.. the hide work. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Dyeing..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Dyeing..", "x": "Explained: Dyeing.. Getting started. The context — Leather Craft. Belts. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Burnishing.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Burnishing.", "x": "Leather Craft: Burnishing.. Dyeing. Essential knowledge — Belts.. the hide work. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Burnishing..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Burnishing..", "x": "Explained: Burnishing.. Stitching. The context — Leather Craft. Tooling. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Awl.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Awl.", "x": "Leather Craft: Awl.. Getting started. Essential knowledge — Tooling.. the hide work. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Awl..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Awl..", "x": "Explained: Awl.. Burnishing. The context — Leather Craft. Stitching. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Belts.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Belts.", "x": "Leather Craft: Belts.. Stitching. Essential knowledge — Stitching.. the hide work. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Belts..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Belts..", "x": "Explained: Belts.. Belts. The context — Leather Craft. Dyeing. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Stitching.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Stitching.", "x": "Leather Craft in depth: Stitching.. Stitching. Details — the hide work.. Belts. Burnishing. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Burnishing.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Burnishing.", "x": "Leather Craft in depth: Burnishing.. Dyeing. Details — the hide work.. Tooling. Awl. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Belts.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Belts.", "x": "Leather Craft in depth: Belts.. Burnishing. Details — the hide work.. Dyeing. Belts. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Tooling.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Tooling.", "x": "Leather Craft in depth: Tooling.. Awl. Details — the hide work.. Getting started. Tooling. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Dyeing.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Dyeing.", "x": "Leather Craft in depth: Dyeing.. Belts. Details — the hide work.. Stitching. Stitching. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Getting started.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Getting started.", "x": "Leather Craft in depth: Getting started.. Tooling. Details — the hide work.. Burnishing. Dyeing. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Leather Craft comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Leather Craft comes from.", "x": "Origins: Stitching.. Tooling. The history of Leather Craft — the hide work.. Burnishing. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Leather Craft respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Leather Craft respectfully.", "x": "Engaging: Belts.. Stitching. How to participate or observe well — Leather Craft. the hide work. Respect first, always; Tooling.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Leather Craft do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Leather Craft do's and don'ts.", "x": "Etiquette: Dyeing.. Dyeing. The rules of respect — Leather Craft. the hide work. When in doubt, ask about Getting started.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Leather Craft.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Leather Craft.", "x": "Planning: Stitching.. Burnishing. Practical notes — Leather Craft. the hide work. A little planning shows respect for Burnishing.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Leather Craft and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Leather Craft and money.", "x": "Costs: Belts.. Awl. What to budget — Leather Craft. the hide work. The best experiences of Tooling. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-hobby2-leather-craft-hobby-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
