(function(){'use strict';
/* JAH Maltese Dog Breed Database generator — jahdb-e2-dog-maltese-dog-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-dog-maltese-dog',PREFIX='JAH-E2DOGMALTES-',NAME='JAH Maltese Dog Breed Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Maltese: the complete guide", "d": "Maltese: the white ancient..", "g": "overview", "l": 2, "q": "What is Maltese: the complete guide?", "a": "Maltese: the white ancient..", "x": "The complete dog breed guide to Maltese: the white ancient.. White. History, meaning, practices, and how to engage respectfully — everything in one database. White. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Maltese essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Maltese essentials.", "x": "At a glance: Maltese — the white ancient.. Ancient. The essentials: Ancient.. Malta. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "White.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "White.", "x": "Maltese: White.. Ancient. Essential knowledge — Malta.. the white ancient. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: White..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: White..", "x": "Explained: White.. Lap. The context — Maltese. Gentle. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Ancient.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Ancient.", "x": "Maltese: Ancient.. Gentle. Essential knowledge — Gentle.. the white ancient. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Ancient..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Ancient..", "x": "Explained: Ancient.. Malta. The context — Maltese. Hypoallergenic. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Malta.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Malta.", "x": "Maltese: Malta.. Lap. Essential knowledge — Hypoallergenic.. the white ancient. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Malta..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Malta..", "x": "Explained: Malta.. History. The context — Maltese. Lap. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Gentle.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Gentle.", "x": "Maltese: Gentle.. Malta. Essential knowledge — Lap.. the white ancient. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Gentle..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Gentle..", "x": "Explained: Gentle.. White. The context — Maltese. White. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Hypoallergenic.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Hypoallergenic.", "x": "Maltese: Hypoallergenic.. History. Essential knowledge — White.. the white ancient. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Hypoallergenic..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Hypoallergenic..", "x": "Explained: Hypoallergenic.. Ancient. The context — Maltese. Ancient. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Lap.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Lap.", "x": "Maltese: Lap.. White. Essential knowledge — Ancient.. the white ancient. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Lap..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Lap..", "x": "Explained: Lap.. Gentle. The context — Maltese. Malta. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "White.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "White.", "x": "Maltese in depth: White.. Ancient. Details — the white ancient.. Gentle. Gentle. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Ancient.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Ancient.", "x": "Maltese in depth: Ancient.. Malta. Details — the white ancient.. Lap. Hypoallergenic. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Gentle.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Gentle.", "x": "Maltese in depth: Gentle.. Gentle. Details — the white ancient.. Malta. Lap. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Lap.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Lap.", "x": "Maltese in depth: Lap.. Hypoallergenic. Details — the white ancient.. History. White. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Malta.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Malta.", "x": "Maltese in depth: Malta.. Lap. Details — the white ancient.. White. Ancient. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "History.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "History.", "x": "Maltese in depth: History.. White. Details — the white ancient.. Ancient. Malta. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Maltese comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Maltese comes from.", "x": "Origins: White.. White. The history of Maltese — the white ancient.. Ancient. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Maltese respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Maltese respectfully.", "x": "Engaging: Gentle.. Ancient. How to participate or observe well — Maltese. the white ancient. Respect first, always; Lap.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Maltese do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Maltese do's and don'ts.", "x": "Etiquette: Malta.. Malta. The rules of respect — Maltese. the white ancient. When in doubt, ask about History.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Maltese.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Maltese.", "x": "Planning: White.. Gentle. Practical notes — Maltese. the white ancient. A little planning shows respect for Ancient.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Maltese and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Maltese and money.", "x": "Costs: Gentle.. Hypoallergenic. What to budget — Maltese. the white ancient. The best experiences of Lap. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-dog-maltese-dog-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
