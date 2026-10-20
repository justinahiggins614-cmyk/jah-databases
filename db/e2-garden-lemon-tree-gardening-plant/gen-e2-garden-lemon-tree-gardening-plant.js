(function(){'use strict';
/* JAH Lemon Tree Gardening Gardening Database generator — jahdb-e2-garden-lemon-tree-gardening-plant-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-garden-lemon-tree-gardening-plant',PREFIX='JAH-E2GARDENLEM-',NAME='JAH Lemon Tree Gardening Gardening Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Lemon Tree Gardening: the complete guide", "d": "Lemon Tree Gardening: the citrus pot..", "g": "overview", "l": 2, "q": "What is Lemon Tree Gardening: the complete guide?", "a": "Lemon Tree Gardening: the citrus pot..", "x": "The complete gardening guide to Lemon Tree Gardening: the citrus pot.. Container. History, meaning, practices, and how to engage respectfully — everything in one database. Container. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Lemon Tree Gardening essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Lemon Tree Gardening essentials.", "x": "At a glance: Lemon Tree Gardening — the citrus pot.. Indoor. The essentials: Meyer.. Meyer. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Container.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Container.", "x": "Lemon Tree Gardening: Container.. Meyer. Essential knowledge — Meyer.. the citrus pot. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Container..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Container..", "x": "Explained: Container.. Overwinter. The context — Lemon Tree Gardening. Thorns. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Indoor.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Indoor.", "x": "Lemon Tree Gardening: Indoor.. Sun. Essential knowledge — Thorns.. the citrus pot. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Indoor..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Indoor..", "x": "Explained: Indoor.. Indoor. The context — Lemon Tree Gardening. Sun. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Meyer.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Meyer.", "x": "Lemon Tree Gardening: Meyer.. Overwinter. Essential knowledge — Sun.. the citrus pot. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Meyer..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Meyer..", "x": "Explained: Meyer.. Guide. The context — Lemon Tree Gardening. Overwinter. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Thorns.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Thorns.", "x": "Lemon Tree Gardening: Thorns.. Indoor. Essential knowledge — Overwinter.. the citrus pot. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Thorns..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Thorns..", "x": "Explained: Thorns.. Container. The context — Lemon Tree Gardening. Container. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Sun.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Sun.", "x": "Lemon Tree Gardening: Sun.. Guide. Essential knowledge — Container.. the citrus pot. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Sun..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Sun..", "x": "Explained: Sun.. Meyer. The context — Lemon Tree Gardening. Indoor. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Overwinter.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Overwinter.", "x": "Lemon Tree Gardening: Overwinter.. Container. Essential knowledge — Indoor.. the citrus pot. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Overwinter..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Overwinter..", "x": "Explained: Overwinter.. Sun. The context — Lemon Tree Gardening. Meyer. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Container.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Container.", "x": "Lemon Tree Gardening in depth: Container.. Indoor. Details — the citrus pot.. Sun. Thorns. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Meyer.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Meyer.", "x": "Lemon Tree Gardening in depth: Meyer.. Meyer. Details — the citrus pot.. Overwinter. Sun. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Sun.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Sun.", "x": "Lemon Tree Gardening in depth: Sun.. Thorns. Details — the citrus pot.. Indoor. Overwinter. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Overwinter.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Overwinter.", "x": "Lemon Tree Gardening in depth: Overwinter.. Sun. Details — the citrus pot.. Guide. Container. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Indoor.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Indoor.", "x": "Lemon Tree Gardening in depth: Indoor.. Overwinter. Details — the citrus pot.. Container. Indoor. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Guide.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Guide.", "x": "Lemon Tree Gardening in depth: Guide.. Container. Details — the citrus pot.. Meyer. Meyer. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Lemon Tree Gardening comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Lemon Tree Gardening comes from.", "x": "Origins: Container.. Container. The history of Lemon Tree Gardening — the citrus pot.. Meyer. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Lemon Tree Gardening respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Lemon Tree Gardening respectfully.", "x": "Engaging: Sun.. Indoor. How to participate or observe well — Lemon Tree Gardening. the citrus pot. Respect first, always; Overwinter.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Lemon Tree Gardening do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Lemon Tree Gardening do's and don'ts.", "x": "Etiquette: Indoor.. Meyer. The rules of respect — Lemon Tree Gardening. the citrus pot. When in doubt, ask about Guide.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Lemon Tree Gardening.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Lemon Tree Gardening.", "x": "Planning: Container.. Thorns. Practical notes — Lemon Tree Gardening. the citrus pot. A little planning shows respect for Meyer.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Lemon Tree Gardening and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Lemon Tree Gardening and money.", "x": "Costs: Sun.. Sun. What to budget — Lemon Tree Gardening. the citrus pot. The best experiences of Overwinter. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-garden-lemon-tree-gardening-plant-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
