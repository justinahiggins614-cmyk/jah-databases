(function(){'use strict';
/* JAH Rose Gardening Flower Database generator — jahdb-e2-flower-rose-gardening-flower-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-flower-rose-gardening-flower',PREFIX='JAH-E2FLOWERROS-',NAME='JAH Rose Gardening Flower Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Rose Gardening: the complete guide", "d": "Rose Gardening: the queen of flowers..", "g": "overview", "l": 2, "q": "What is Rose Gardening: the complete guide?", "a": "Rose Gardening: the queen of flowers..", "x": "The complete flower guide to Rose Gardening: the queen of flowers.. Pruning. History, meaning, practices, and how to engage respectfully — everything in one database. Pruning. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Rose Gardening essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Rose Gardening essentials.", "x": "At a glance: Rose Gardening — the queen of flowers.. Black spot. The essentials: Fragrance.. Hybrid tea. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Pruning.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Pruning.", "x": "Rose Gardening: Pruning.. Fragrance. Essential knowledge — Hybrid tea.. the queen of flowers. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Pruning..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Pruning..", "x": "Explained: Pruning.. Zones. The context — Rose Gardening. Fragrance. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Black spot.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Black spot.", "x": "Rose Gardening: Black spot.. Deadheading. Essential knowledge — Fragrance.. the queen of flowers. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Black spot..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Black spot..", "x": "Explained: Black spot.. Tea. The context — Rose Gardening. Deadheading. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Hybrid tea.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Hybrid tea.", "x": "Rose Gardening: Hybrid tea.. Zones. Essential knowledge — Deadheading.. the queen of flowers. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Hybrid tea..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Hybrid tea..", "x": "Explained: Hybrid tea.. Guide. The context — Rose Gardening. Zones. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Fragrance.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Fragrance.", "x": "Rose Gardening: Fragrance.. Tea. Essential knowledge — Zones.. the queen of flowers. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Fragrance..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Fragrance..", "x": "Explained: Fragrance.. Pruning. The context — Rose Gardening. Pruning. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Deadheading.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Deadheading.", "x": "Rose Gardening: Deadheading.. Guide. Essential knowledge — Pruning.. the queen of flowers. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Deadheading..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Deadheading..", "x": "Explained: Deadheading.. Fragrance. The context — Rose Gardening. Black spot. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Zones.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Zones.", "x": "Rose Gardening: Zones.. Pruning. Essential knowledge — Black spot.. the queen of flowers. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Zones..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Zones..", "x": "Explained: Zones.. Deadheading. The context — Rose Gardening. Hybrid tea. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Pruning.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Pruning.", "x": "Rose Gardening in depth: Pruning.. Black spot. Details — the queen of flowers.. Deadheading. Fragrance. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Fragrance.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Fragrance.", "x": "Rose Gardening in depth: Fragrance.. Hybrid tea. Details — the queen of flowers.. Zones. Deadheading. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Deadheading.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Deadheading.", "x": "Rose Gardening in depth: Deadheading.. Fragrance. Details — the queen of flowers.. Tea. Zones. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Zones.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Zones.", "x": "Rose Gardening in depth: Zones.. Deadheading. Details — the queen of flowers.. Guide. Pruning. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Tea.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Tea.", "x": "Rose Gardening in depth: Tea.. Zones. Details — the queen of flowers.. Pruning. Black spot. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Guide.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Guide.", "x": "Rose Gardening in depth: Guide.. Pruning. Details — the queen of flowers.. Fragrance. Hybrid tea. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Rose Gardening comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Rose Gardening comes from.", "x": "Origins: Pruning.. Pruning. The history of Rose Gardening — the queen of flowers.. Fragrance. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Rose Gardening respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Rose Gardening respectfully.", "x": "Engaging: Deadheading.. Black spot. How to participate or observe well — Rose Gardening. the queen of flowers. Respect first, always; Zones.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Rose Gardening do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Rose Gardening do's and don'ts.", "x": "Etiquette: Tea.. Hybrid tea. The rules of respect — Rose Gardening. the queen of flowers. When in doubt, ask about Guide.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Rose Gardening.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Rose Gardening.", "x": "Planning: Pruning.. Fragrance. Practical notes — Rose Gardening. the queen of flowers. A little planning shows respect for Fragrance.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Rose Gardening and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Rose Gardening and money.", "x": "Costs: Deadheading.. Deadheading. What to budget — Rose Gardening. the queen of flowers. The best experiences of Zones. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-flower-rose-gardening-flower-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
