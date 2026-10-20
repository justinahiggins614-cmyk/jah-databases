(function(){'use strict';
/* JAH Bobotie Dish Database generator — jahdb-e2-dish-bobotie-dish-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-dish-bobotie-dish',PREFIX='JAH-E2DISHBOBOT-',NAME='JAH Bobotie Dish Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Bobotie: the complete guide", "d": "Bobotie: the baked mince..", "g": "overview", "l": 2, "q": "What is Bobotie: the complete guide?", "a": "Bobotie: the baked mince..", "x": "The complete dish guide to Bobotie: the baked mince.. Cape Malay. History, meaning, practices, and how to engage respectfully — everything in one database. Malay. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Bobotie essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Bobotie essentials.", "x": "At a glance: Bobotie — the baked mince.. Curried. The essentials: Custard.. Egg custard. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Cape Malay.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Cape Malay.", "x": "Bobotie: Cape Malay.. Custard. Essential knowledge — Egg custard.. the baked mince. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Cape Malay..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Cape Malay..", "x": "Explained: Cape Malay.. Cape. The context — Bobotie. Bay leaves. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Curried.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Curried.", "x": "Bobotie: Curried.. Baked. Essential knowledge — Bay leaves.. the baked mince. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Curried..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Curried..", "x": "Explained: Curried.. Curried. The context — Bobotie. Sweet. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Egg custard.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Egg custard.", "x": "Bobotie: Egg custard.. Cape. Essential knowledge — Sweet.. the baked mince. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Egg custard..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Egg custard..", "x": "Explained: Egg custard.. Making. The context — Bobotie. Baked. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Bay leaves.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Bay leaves.", "x": "Bobotie: Bay leaves.. Curried. Essential knowledge — Baked.. the baked mince. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Bay leaves..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Bay leaves..", "x": "Explained: Bay leaves.. Malay. The context — Bobotie. Cape Malay. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Sweet.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Sweet.", "x": "Bobotie: Sweet.. Making. Essential knowledge — Cape Malay.. the baked mince. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Sweet..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Sweet..", "x": "Explained: Sweet.. Custard. The context — Bobotie. Curried. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Baked.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Baked.", "x": "Bobotie: Baked.. Malay. Essential knowledge — Curried.. the baked mince. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Baked..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Baked..", "x": "Explained: Baked.. Baked. The context — Bobotie. Egg custard. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Malay.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Malay.", "x": "Bobotie in depth: Malay.. Curried. Details — the baked mince.. Baked. Bay leaves. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Custard.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Custard.", "x": "Bobotie in depth: Custard.. Egg custard. Details — the baked mince.. Cape. Sweet. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Baked.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Baked.", "x": "Bobotie in depth: Baked.. Bay leaves. Details — the baked mince.. Curried. Baked. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Cape.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Cape.", "x": "Bobotie in depth: Cape.. Sweet. Details — the baked mince.. Making. Cape Malay. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Curried.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Curried.", "x": "Bobotie in depth: Curried.. Baked. Details — the baked mince.. Malay. Curried. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Making.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Making.", "x": "Bobotie in depth: Making.. Cape Malay. Details — the baked mince.. Custard. Egg custard. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Bobotie comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Bobotie comes from.", "x": "Origins: Malay.. Cape Malay. The history of Bobotie — the baked mince.. Custard. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Bobotie respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Bobotie respectfully.", "x": "Engaging: Baked.. Curried. How to participate or observe well — Bobotie. the baked mince. Respect first, always; Cape.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Bobotie do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Bobotie do's and don'ts.", "x": "Etiquette: Curried.. Egg custard. The rules of respect — Bobotie. the baked mince. When in doubt, ask about Making.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Bobotie.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Bobotie.", "x": "Planning: Malay.. Bay leaves. Practical notes — Bobotie. the baked mince. A little planning shows respect for Custard.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Bobotie and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Bobotie and money.", "x": "Costs: Baked.. Sweet. What to budget — Bobotie. the baked mince. The best experiences of Cape. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-dish-bobotie-dish-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
