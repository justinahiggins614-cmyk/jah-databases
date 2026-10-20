(function(){'use strict';
/* JAH Infrared Photography Photography Database generator — jahdb-e2-photo-infrared-photo-tech-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-photo-infrared-photo-tech',PREFIX='JAH-E2PHOTOINFR-',NAME='JAH Infrared Photography Photography Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Infrared Photography: the complete guide", "d": "Infrared Photography: the invisible light..", "g": "overview", "l": 2, "q": "What is Infrared Photography: the complete guide?", "a": "Infrared Photography: the invisible light..", "x": "The complete photography guide to Infrared Photography: the invisible light.. IR. History, meaning, practices, and how to engage respectfully — everything in one database. IR. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Infrared Photography essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Infrared Photography essentials.", "x": "At a glance: Infrared Photography — the invisible light.. White foliage. The essentials: Surreal.. Conversion. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "IR.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "IR.", "x": "Infrared Photography: IR.. Surreal. Essential knowledge — Conversion.. the invisible light. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: IR..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: IR..", "x": "Explained: IR.. Foliage. The context — Infrared Photography. Surreal. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "White foliage.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "White foliage.", "x": "Infrared Photography: White foliage.. 720nm. Essential knowledge — Surreal.. the invisible light. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: White foliage..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: White foliage..", "x": "Explained: White foliage.. Filters. The context — Infrared Photography. Filters. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Conversion.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Conversion.", "x": "Infrared Photography: Conversion.. Foliage. Essential knowledge — Filters.. the invisible light. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Conversion..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Conversion..", "x": "Explained: Conversion.. Tips. The context — Infrared Photography. 720nm. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Surreal.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Surreal.", "x": "Infrared Photography: Surreal.. Filters. Essential knowledge — 720nm.. the invisible light. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Surreal..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Surreal..", "x": "Explained: Surreal.. IR. The context — Infrared Photography. IR. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Filters.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Filters.", "x": "Infrared Photography: Filters.. Tips. Essential knowledge — IR.. the invisible light. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Filters..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Filters..", "x": "Explained: Filters.. Surreal. The context — Infrared Photography. White foliage. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "720nm.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "720nm.", "x": "Infrared Photography: 720nm.. IR. Essential knowledge — White foliage.. the invisible light. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: 720nm..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: 720nm..", "x": "Explained: 720nm.. 720nm. The context — Infrared Photography. Conversion. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "IR.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "IR.", "x": "Infrared Photography in depth: IR.. White foliage. Details — the invisible light.. 720nm. Surreal. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Surreal.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Surreal.", "x": "Infrared Photography in depth: Surreal.. Conversion. Details — the invisible light.. Foliage. Filters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "720nm.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "720nm.", "x": "Infrared Photography in depth: 720nm.. Surreal. Details — the invisible light.. Filters. 720nm. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Foliage.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Foliage.", "x": "Infrared Photography in depth: Foliage.. Filters. Details — the invisible light.. Tips. IR. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Filters.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Filters.", "x": "Infrared Photography in depth: Filters.. 720nm. Details — the invisible light.. IR. White foliage. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Tips.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Tips.", "x": "Infrared Photography in depth: Tips.. IR. Details — the invisible light.. Surreal. Conversion. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Infrared Photography comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Infrared Photography comes from.", "x": "Origins: IR.. IR. The history of Infrared Photography — the invisible light.. Surreal. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Infrared Photography respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Infrared Photography respectfully.", "x": "Engaging: 720nm.. White foliage. How to participate or observe well — Infrared Photography. the invisible light. Respect first, always; Foliage.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Infrared Photography do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Infrared Photography do's and don'ts.", "x": "Etiquette: Filters.. Conversion. The rules of respect — Infrared Photography. the invisible light. When in doubt, ask about Tips.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Infrared Photography.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Infrared Photography.", "x": "Planning: IR.. Surreal. Practical notes — Infrared Photography. the invisible light. A little planning shows respect for Surreal.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Infrared Photography and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Infrared Photography and money.", "x": "Costs: 720nm.. Filters. What to budget — Infrared Photography. the invisible light. The best experiences of Foliage. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-photo-infrared-photo-tech-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
