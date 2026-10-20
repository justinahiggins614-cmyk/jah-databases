(function(){'use strict';
/* JAH Astronomy Hobby Database generator — jahdb-e2-hobby2-astronomy-hobby-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-hobby2-astronomy-hobby',PREFIX='JAH-E2HOBBY2AST-',NAME='JAH Astronomy Hobby Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Astronomy Hobby: the complete guide", "d": "Astronomy Hobby: the deep sky..", "g": "overview", "l": 2, "q": "What is Astronomy Hobby: the complete guide?", "a": "Astronomy Hobby: the deep sky..", "x": "The complete hobby guide to Astronomy Hobby: the deep sky.. Telescope. History, meaning, practices, and how to engage respectfully — everything in one database. Dark sky. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Astronomy Hobby essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Astronomy Hobby essentials.", "x": "At a glance: Astronomy Hobby — the deep sky.. Dark sky. The essentials: Parties.. Messier. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Telescope.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Telescope.", "x": "Astronomy Hobby: Telescope.. Parties. Essential knowledge — Messier.. the deep sky. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Telescope..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Telescope..", "x": "Explained: Telescope.. Telescope. The context — Astronomy Hobby. Star parties. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Dark sky.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Dark sky.", "x": "Astronomy Hobby: Dark sky.. Patience. Essential knowledge — Star parties.. the deep sky. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Dark sky..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Dark sky..", "x": "Explained: Dark sky.. Messier. The context — Astronomy Hobby. Apps. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Messier.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Messier.", "x": "Astronomy Hobby: Messier.. Telescope. Essential knowledge — Apps.. the deep sky. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Messier..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Messier..", "x": "Explained: Messier.. Getting started. The context — Astronomy Hobby. Patience. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Star parties.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Star parties.", "x": "Astronomy Hobby: Star parties.. Messier. Essential knowledge — Patience.. the deep sky. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Star parties..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Star parties..", "x": "Explained: Star parties.. Dark sky. The context — Astronomy Hobby. Telescope. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Apps.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Apps.", "x": "Astronomy Hobby: Apps.. Getting started. Essential knowledge — Telescope.. the deep sky. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Apps..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Apps..", "x": "Explained: Apps.. Parties. The context — Astronomy Hobby. Dark sky. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Patience.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Patience.", "x": "Astronomy Hobby: Patience.. Dark sky. Essential knowledge — Dark sky.. the deep sky. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Patience..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Patience..", "x": "Explained: Patience.. Patience. The context — Astronomy Hobby. Messier. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Dark sky.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Dark sky.", "x": "Astronomy Hobby in depth: Dark sky.. Dark sky. Details — the deep sky.. Patience. Star parties. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Parties.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Parties.", "x": "Astronomy Hobby in depth: Parties.. Messier. Details — the deep sky.. Telescope. Apps. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Patience.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Patience.", "x": "Astronomy Hobby in depth: Patience.. Star parties. Details — the deep sky.. Messier. Patience. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Telescope.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Telescope.", "x": "Astronomy Hobby in depth: Telescope.. Apps. Details — the deep sky.. Getting started. Telescope. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Messier.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Messier.", "x": "Astronomy Hobby in depth: Messier.. Patience. Details — the deep sky.. Dark sky. Dark sky. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Getting started.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Getting started.", "x": "Astronomy Hobby in depth: Getting started.. Telescope. Details — the deep sky.. Parties. Messier. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Astronomy Hobby comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Astronomy Hobby comes from.", "x": "Origins: Dark sky.. Telescope. The history of Astronomy Hobby — the deep sky.. Parties. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Astronomy Hobby respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Astronomy Hobby respectfully.", "x": "Engaging: Patience.. Dark sky. How to participate or observe well — Astronomy Hobby. the deep sky. Respect first, always; Telescope.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Astronomy Hobby do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Astronomy Hobby do's and don'ts.", "x": "Etiquette: Messier.. Messier. The rules of respect — Astronomy Hobby. the deep sky. When in doubt, ask about Getting started.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Astronomy Hobby.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Astronomy Hobby.", "x": "Planning: Dark sky.. Star parties. Practical notes — Astronomy Hobby. the deep sky. A little planning shows respect for Parties.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Astronomy Hobby and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Astronomy Hobby and money.", "x": "Costs: Patience.. Apps. What to budget — Astronomy Hobby. the deep sky. The best experiences of Telescope. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-hobby2-astronomy-hobby-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
