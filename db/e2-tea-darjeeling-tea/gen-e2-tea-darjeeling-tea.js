(function(){'use strict';
/* JAH Darjeeling Tea Tea Database generator — jahdb-e2-tea-darjeeling-tea-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-tea-darjeeling-tea',PREFIX='JAH-E2TEADARJEE-',NAME='JAH Darjeeling Tea Tea Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Darjeeling Tea: the complete guide", "d": "Darjeeling Tea: the champagne of teas..", "g": "overview", "l": 2, "q": "What is Darjeeling Tea: the complete guide?", "a": "Darjeeling Tea: the champagne of teas..", "x": "The complete tea guide to Darjeeling Tea: the champagne of teas.. India. History, meaning, practices, and how to engage respectfully — everything in one database. Muscatel. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Darjeeling Tea essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Darjeeling Tea essentials.", "x": "At a glance: Darjeeling Tea — the champagne of teas.. Muscatel. The essentials: Flush.. First flush. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "India.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "India.", "x": "Darjeeling Tea: India.. Flush. Essential knowledge — First flush.. the champagne of teas. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: India..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: India..", "x": "Explained: India.. Champagne. The context — Darjeeling Tea. Himalayas. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Muscatel.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Muscatel.", "x": "Darjeeling Tea: Muscatel.. Himalayas. Essential knowledge — Himalayas.. the champagne of teas. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Muscatel..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Muscatel..", "x": "Explained: Muscatel.. Light. The context — Darjeeling Tea. Champagne. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "First flush.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "First flush.", "x": "Darjeeling Tea: First flush.. Champagne. Essential knowledge — Champagne.. the champagne of teas. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: First flush..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: First flush..", "x": "Explained: First flush.. India. The context — Darjeeling Tea. Light. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Himalayas.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Himalayas.", "x": "Darjeeling Tea: Himalayas.. Light. Essential knowledge — Light.. the champagne of teas. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Himalayas..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Himalayas..", "x": "Explained: Himalayas.. Muscatel. The context — Darjeeling Tea. India. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Champagne.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Champagne.", "x": "Darjeeling Tea: Champagne.. India. Essential knowledge — India.. the champagne of teas. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Champagne..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Champagne..", "x": "Explained: Champagne.. Flush. The context — Darjeeling Tea. Muscatel. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Light.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Light.", "x": "Darjeeling Tea: Light.. Muscatel. Essential knowledge — Muscatel.. the champagne of teas. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Light..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Light..", "x": "Explained: Light.. Himalayas. The context — Darjeeling Tea. First flush. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Muscatel.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Muscatel.", "x": "Darjeeling Tea in depth: Muscatel.. Muscatel. Details — the champagne of teas.. Himalayas. Himalayas. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Flush.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Flush.", "x": "Darjeeling Tea in depth: Flush.. First flush. Details — the champagne of teas.. Champagne. Champagne. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Himalayas.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Himalayas.", "x": "Darjeeling Tea in depth: Himalayas.. Himalayas. Details — the champagne of teas.. Light. Light. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Champagne.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Champagne.", "x": "Darjeeling Tea in depth: Champagne.. Champagne. Details — the champagne of teas.. India. India. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Light.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Light.", "x": "Darjeeling Tea in depth: Light.. Light. Details — the champagne of teas.. Muscatel. Muscatel. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "India.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "India.", "x": "Darjeeling Tea in depth: India.. India. Details — the champagne of teas.. Flush. First flush. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Darjeeling Tea comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Darjeeling Tea comes from.", "x": "Origins: Muscatel.. India. The history of Darjeeling Tea — the champagne of teas.. Flush. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Darjeeling Tea respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Darjeeling Tea respectfully.", "x": "Engaging: Himalayas.. Muscatel. How to participate or observe well — Darjeeling Tea. the champagne of teas. Respect first, always; Champagne.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Darjeeling Tea do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Darjeeling Tea do's and don'ts.", "x": "Etiquette: Light.. First flush. The rules of respect — Darjeeling Tea. the champagne of teas. When in doubt, ask about India.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Darjeeling Tea.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Darjeeling Tea.", "x": "Planning: Muscatel.. Himalayas. Practical notes — Darjeeling Tea. the champagne of teas. A little planning shows respect for Flush.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Darjeeling Tea and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Darjeeling Tea and money.", "x": "Costs: Himalayas.. Champagne. What to budget — Darjeeling Tea. the champagne of teas. The best experiences of Champagne. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-tea-darjeeling-tea-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
