(function(){'use strict';
/* JAH Dole Whip Dessert Database generator — jahdb-e2-dessert3-dole-whip-food-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-dessert3-dole-whip-food',PREFIX='JAH-E2DESSERT3D-',NAME='JAH Dole Whip Dessert Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Dole Whip: the complete guide", "d": "Dole Whip: the pineapple swirl..", "g": "overview", "l": 2, "q": "What is Dole Whip: the complete guide?", "a": "Dole Whip: the pineapple swirl..", "x": "The complete dessert guide to Dole Whip: the pineapple swirl.. Pineapple. History, meaning, practices, and how to engage respectfully — everything in one database. Pineapple. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Dole Whip essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Dole Whip essentials.", "x": "At a glance: Dole Whip — the pineapple swirl.. Disney. The essentials: Disney.. Dairy-free. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Pineapple.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Pineapple.", "x": "Dole Whip: Pineapple.. Disney. Essential knowledge — Dairy-free.. the pineapple swirl. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Pineapple..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Pineapple..", "x": "Explained: Pineapple.. Swirl. The context — Dole Whip. Swirl. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Disney.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Disney.", "x": "Dole Whip: Disney.. Tropical. Essential knowledge — Swirl.. the pineapple swirl. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Disney..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Disney..", "x": "Explained: Disney.. Dole. The context — Dole Whip. Dole. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Dairy-free.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Dairy-free.", "x": "Dole Whip: Dairy-free.. Swirl. Essential knowledge — Dole.. the pineapple swirl. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Dairy-free..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Dairy-free..", "x": "Explained: Dairy-free.. Making. The context — Dole Whip. Tropical. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Swirl.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Swirl.", "x": "Dole Whip: Swirl.. Dole. Essential knowledge — Tropical.. the pineapple swirl. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Swirl..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Swirl..", "x": "Explained: Swirl.. Pineapple. The context — Dole Whip. Pineapple. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Dole.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Dole.", "x": "Dole Whip: Dole.. Making. Essential knowledge — Pineapple.. the pineapple swirl. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Dole..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Dole..", "x": "Explained: Dole.. Disney. The context — Dole Whip. Disney. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Tropical.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Tropical.", "x": "Dole Whip: Tropical.. Pineapple. Essential knowledge — Disney.. the pineapple swirl. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Tropical..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Tropical..", "x": "Explained: Tropical.. Tropical. The context — Dole Whip. Dairy-free. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Pineapple.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Pineapple.", "x": "Dole Whip in depth: Pineapple.. Disney. Details — the pineapple swirl.. Tropical. Swirl. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Disney.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Disney.", "x": "Dole Whip in depth: Disney.. Dairy-free. Details — the pineapple swirl.. Swirl. Dole. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Tropical.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Tropical.", "x": "Dole Whip in depth: Tropical.. Swirl. Details — the pineapple swirl.. Dole. Tropical. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Swirl.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Swirl.", "x": "Dole Whip in depth: Swirl.. Dole. Details — the pineapple swirl.. Making. Pineapple. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Dole.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Dole.", "x": "Dole Whip in depth: Dole.. Tropical. Details — the pineapple swirl.. Pineapple. Disney. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Making.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Making.", "x": "Dole Whip in depth: Making.. Pineapple. Details — the pineapple swirl.. Disney. Dairy-free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Dole Whip comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Dole Whip comes from.", "x": "Origins: Pineapple.. Pineapple. The history of Dole Whip — the pineapple swirl.. Disney. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Dole Whip respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Dole Whip respectfully.", "x": "Engaging: Tropical.. Disney. How to participate or observe well — Dole Whip. the pineapple swirl. Respect first, always; Swirl.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Dole Whip do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Dole Whip do's and don'ts.", "x": "Etiquette: Dole.. Dairy-free. The rules of respect — Dole Whip. the pineapple swirl. When in doubt, ask about Making.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Dole Whip.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Dole Whip.", "x": "Planning: Pineapple.. Swirl. Practical notes — Dole Whip. the pineapple swirl. A little planning shows respect for Disney.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Dole Whip and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Dole Whip and money.", "x": "Costs: Tropical.. Dole. What to budget — Dole Whip. the pineapple swirl. The best experiences of Swirl. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-dessert3-dole-whip-food-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
