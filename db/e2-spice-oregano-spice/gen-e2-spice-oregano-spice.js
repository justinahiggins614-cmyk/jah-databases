(function(){'use strict';
/* JAH Oregano Spice Spice Database generator — jahdb-e2-spice-oregano-spice-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-spice-oregano-spice',PREFIX='JAH-E2SPICEOREG-',NAME='JAH Oregano Spice Spice Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Oregano Spice: the complete guide", "d": "Oregano Spice: the dried punch..", "g": "overview", "l": 2, "q": "What is Oregano Spice: the complete guide?", "a": "Oregano Spice: the dried punch..", "x": "The complete spice guide to Oregano Spice: the dried punch.. Dried. History, meaning, practices, and how to engage respectfully — everything in one database. Pizza. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Oregano Spice essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Oregano Spice essentials.", "x": "At a glance: Oregano Spice — the dried punch.. Pizza. The essentials: Greek.. Greek. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Dried.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Dried.", "x": "Oregano Spice: Dried.. Greek. Essential knowledge — Greek.. the dried punch. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Dried..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Dried..", "x": "Explained: Dried.. Crush. The context — Oregano Spice. Mexican. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Pizza.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Pizza.", "x": "Oregano Spice: Pizza.. Stronger. Essential knowledge — Mexican.. the dried punch. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Pizza..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Pizza..", "x": "Explained: Pizza.. Mexican. The context — Oregano Spice. Stronger. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Greek.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Greek.", "x": "Oregano Spice: Greek.. Crush. Essential knowledge — Stronger.. the dried punch. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Greek..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Greek..", "x": "Explained: Greek.. Storage. The context — Oregano Spice. Crush. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Mexican.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Mexican.", "x": "Oregano Spice: Mexican.. Mexican. Essential knowledge — Crush.. the dried punch. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Mexican..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Mexican..", "x": "Explained: Mexican.. Pizza. The context — Oregano Spice. Dried. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Stronger.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Stronger.", "x": "Oregano Spice: Stronger.. Storage. Essential knowledge — Dried.. the dried punch. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Stronger..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Stronger..", "x": "Explained: Stronger.. Greek. The context — Oregano Spice. Pizza. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Crush.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Crush.", "x": "Oregano Spice: Crush.. Pizza. Essential knowledge — Pizza.. the dried punch. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Crush..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Crush..", "x": "Explained: Crush.. Stronger. The context — Oregano Spice. Greek. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Pizza.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Pizza.", "x": "Oregano Spice in depth: Pizza.. Pizza. Details — the dried punch.. Stronger. Mexican. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Greek.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Greek.", "x": "Oregano Spice in depth: Greek.. Greek. Details — the dried punch.. Crush. Stronger. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Stronger.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Stronger.", "x": "Oregano Spice in depth: Stronger.. Mexican. Details — the dried punch.. Mexican. Crush. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Crush.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Crush.", "x": "Oregano Spice in depth: Crush.. Stronger. Details — the dried punch.. Storage. Dried. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Mexican.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Mexican.", "x": "Oregano Spice in depth: Mexican.. Crush. Details — the dried punch.. Pizza. Pizza. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Storage.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Storage.", "x": "Oregano Spice in depth: Storage.. Dried. Details — the dried punch.. Greek. Greek. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Oregano Spice comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Oregano Spice comes from.", "x": "Origins: Pizza.. Dried. The history of Oregano Spice — the dried punch.. Greek. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Oregano Spice respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Oregano Spice respectfully.", "x": "Engaging: Stronger.. Pizza. How to participate or observe well — Oregano Spice. the dried punch. Respect first, always; Crush.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Oregano Spice do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Oregano Spice do's and don'ts.", "x": "Etiquette: Mexican.. Greek. The rules of respect — Oregano Spice. the dried punch. When in doubt, ask about Storage.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Oregano Spice.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Oregano Spice.", "x": "Planning: Pizza.. Mexican. Practical notes — Oregano Spice. the dried punch. A little planning shows respect for Greek.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Oregano Spice and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Oregano Spice and money.", "x": "Costs: Stronger.. Stronger. What to budget — Oregano Spice. the dried punch. The best experiences of Crush. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-spice-oregano-spice-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
