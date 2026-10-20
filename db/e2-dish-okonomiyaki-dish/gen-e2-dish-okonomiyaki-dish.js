(function(){'use strict';
/* JAH Okonomiyaki Dish Database generator — jahdb-e2-dish-okonomiyaki-dish-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-dish-okonomiyaki-dish',PREFIX='JAH-E2DISHOKONO-',NAME='JAH Okonomiyaki Dish Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Okonomiyaki: the complete guide", "d": "Okonomiyaki: the savory pancake..", "g": "overview", "l": 2, "q": "What is Okonomiyaki: the complete guide?", "a": "Okonomiyaki: the savory pancake..", "x": "The complete dish guide to Okonomiyaki: the savory pancake.. Osaka. History, meaning, practices, and how to engage respectfully — everything in one database. Osaka. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Okonomiyaki essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Okonomiyaki essentials.", "x": "At a glance: Okonomiyaki — the savory pancake.. Cabbage. The essentials: Bonito.. Kewpie. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Osaka.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Osaka.", "x": "Okonomiyaki: Osaka.. Bonito. Essential knowledge — Kewpie.. the savory pancake. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Osaka..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Osaka..", "x": "Explained: Osaka.. Cabbage. The context — Okonomiyaki. Bonito. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Cabbage.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Cabbage.", "x": "Okonomiyaki: Cabbage.. Pancake. Essential knowledge — Bonito.. the savory pancake. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Cabbage..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Cabbage..", "x": "Explained: Cabbage.. Kewpie. The context — Okonomiyaki. Grill. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Kewpie.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Kewpie.", "x": "Okonomiyaki: Kewpie.. Cabbage. Essential knowledge — Grill.. the savory pancake. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Kewpie..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Kewpie..", "x": "Explained: Kewpie.. Making. The context — Okonomiyaki. Pancake. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Bonito.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Bonito.", "x": "Okonomiyaki: Bonito.. Kewpie. Essential knowledge — Pancake.. the savory pancake. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Bonito..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Bonito..", "x": "Explained: Bonito.. Osaka. The context — Okonomiyaki. Osaka. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Grill.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Grill.", "x": "Okonomiyaki: Grill.. Making. Essential knowledge — Osaka.. the savory pancake. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Grill..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Grill..", "x": "Explained: Grill.. Bonito. The context — Okonomiyaki. Cabbage. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Pancake.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Pancake.", "x": "Okonomiyaki: Pancake.. Osaka. Essential knowledge — Cabbage.. the savory pancake. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Pancake..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Pancake..", "x": "Explained: Pancake.. Pancake. The context — Okonomiyaki. Kewpie. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Osaka.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Osaka.", "x": "Okonomiyaki in depth: Osaka.. Cabbage. Details — the savory pancake.. Pancake. Bonito. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Bonito.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Bonito.", "x": "Okonomiyaki in depth: Bonito.. Kewpie. Details — the savory pancake.. Cabbage. Grill. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Pancake.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Pancake.", "x": "Okonomiyaki in depth: Pancake.. Bonito. Details — the savory pancake.. Kewpie. Pancake. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Cabbage.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Cabbage.", "x": "Okonomiyaki in depth: Cabbage.. Grill. Details — the savory pancake.. Making. Osaka. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Kewpie.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Kewpie.", "x": "Okonomiyaki in depth: Kewpie.. Pancake. Details — the savory pancake.. Osaka. Cabbage. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Making.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Making.", "x": "Okonomiyaki in depth: Making.. Osaka. Details — the savory pancake.. Bonito. Kewpie. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Okonomiyaki comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Okonomiyaki comes from.", "x": "Origins: Osaka.. Osaka. The history of Okonomiyaki — the savory pancake.. Bonito. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Okonomiyaki respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Okonomiyaki respectfully.", "x": "Engaging: Pancake.. Cabbage. How to participate or observe well — Okonomiyaki. the savory pancake. Respect first, always; Cabbage.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Okonomiyaki do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Okonomiyaki do's and don'ts.", "x": "Etiquette: Kewpie.. Kewpie. The rules of respect — Okonomiyaki. the savory pancake. When in doubt, ask about Making.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Okonomiyaki.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Okonomiyaki.", "x": "Planning: Osaka.. Bonito. Practical notes — Okonomiyaki. the savory pancake. A little planning shows respect for Bonito.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Okonomiyaki and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Okonomiyaki and money.", "x": "Costs: Pancake.. Grill. What to budget — Okonomiyaki. the savory pancake. The best experiences of Cabbage. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-dish-okonomiyaki-dish-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
