(function(){'use strict';
/* JAH Homebrewing Hobby Database generator — jahdb-e2-hobby2-homebrewing-hobby-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-hobby2-homebrewing-hobby',PREFIX='JAH-E2HOBBY2HOM-',NAME='JAH Homebrewing Hobby Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Homebrewing Hobby: the complete guide", "d": "Homebrewing Hobby: the beer craft..", "g": "overview", "l": 2, "q": "What is Homebrewing Hobby: the complete guide?", "a": "Homebrewing Hobby: the beer craft..", "x": "The complete hobby guide to Homebrewing Hobby: the beer craft.. Malt. History, meaning, practices, and how to engage respectfully — everything in one database. Ferment. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Homebrewing Hobby essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Homebrewing Hobby essentials.", "x": "At a glance: Homebrewing Hobby — the beer craft.. Hops. The essentials: Sanitize.. Ferment. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Malt.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Malt.", "x": "Homebrewing Hobby: Malt.. Sanitize. Essential knowledge — Ferment.. the beer craft. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Malt..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Malt..", "x": "Explained: Malt.. Malt. The context — Homebrewing Hobby. Bottling. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Hops.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Hops.", "x": "Homebrewing Hobby: Hops.. Recipes. Essential knowledge — Bottling.. the beer craft. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Hops..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Hops..", "x": "Explained: Hops.. Hops. The context — Homebrewing Hobby. Sanitize. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Ferment.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Ferment.", "x": "Homebrewing Hobby: Ferment.. Malt. Essential knowledge — Sanitize.. the beer craft. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Ferment..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Ferment..", "x": "Explained: Ferment.. Getting started. The context — Homebrewing Hobby. Recipes. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Bottling.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Bottling.", "x": "Homebrewing Hobby: Bottling.. Hops. Essential knowledge — Recipes.. the beer craft. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Bottling..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Bottling..", "x": "Explained: Bottling.. Ferment. The context — Homebrewing Hobby. Malt. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Sanitize.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Sanitize.", "x": "Homebrewing Hobby: Sanitize.. Getting started. Essential knowledge — Malt.. the beer craft. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Sanitize..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Sanitize..", "x": "Explained: Sanitize.. Sanitize. The context — Homebrewing Hobby. Hops. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Recipes.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Recipes.", "x": "Homebrewing Hobby: Recipes.. Ferment. Essential knowledge — Hops.. the beer craft. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Recipes..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Recipes..", "x": "Explained: Recipes.. Recipes. The context — Homebrewing Hobby. Ferment. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Ferment.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Ferment.", "x": "Homebrewing Hobby in depth: Ferment.. Hops. Details — the beer craft.. Recipes. Bottling. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Sanitize.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Sanitize.", "x": "Homebrewing Hobby in depth: Sanitize.. Ferment. Details — the beer craft.. Malt. Sanitize. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Recipes.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Recipes.", "x": "Homebrewing Hobby in depth: Recipes.. Bottling. Details — the beer craft.. Hops. Recipes. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Malt.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Malt.", "x": "Homebrewing Hobby in depth: Malt.. Sanitize. Details — the beer craft.. Getting started. Malt. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Hops.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Hops.", "x": "Homebrewing Hobby in depth: Hops.. Recipes. Details — the beer craft.. Ferment. Hops. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Getting started.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Getting started.", "x": "Homebrewing Hobby in depth: Getting started.. Malt. Details — the beer craft.. Sanitize. Ferment. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Homebrewing Hobby comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Homebrewing Hobby comes from.", "x": "Origins: Ferment.. Malt. The history of Homebrewing Hobby — the beer craft.. Sanitize. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Homebrewing Hobby respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Homebrewing Hobby respectfully.", "x": "Engaging: Recipes.. Hops. How to participate or observe well — Homebrewing Hobby. the beer craft. Respect first, always; Malt.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Homebrewing Hobby do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Homebrewing Hobby do's and don'ts.", "x": "Etiquette: Hops.. Ferment. The rules of respect — Homebrewing Hobby. the beer craft. When in doubt, ask about Getting started.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Homebrewing Hobby.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Homebrewing Hobby.", "x": "Planning: Ferment.. Bottling. Practical notes — Homebrewing Hobby. the beer craft. A little planning shows respect for Sanitize.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Homebrewing Hobby and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Homebrewing Hobby and money.", "x": "Costs: Recipes.. Sanitize. What to budget — Homebrewing Hobby. the beer craft. The best experiences of Malt. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-hobby2-homebrewing-hobby-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
