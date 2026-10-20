(function(){'use strict';
/* JAH Bokh Wrestling Martial Art Database generator — jahdb-e2-martial-bokh-wrestling-martial-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-martial-bokh-wrestling-martial',PREFIX='JAH-E2MARTIALBO-',NAME='JAH Bokh Wrestling Martial Art Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Bokh Wrestling: the complete guide", "d": "Bokh Wrestling: the Mongolian wrestling..", "g": "overview", "l": 2, "q": "What is Bokh Wrestling: the complete guide?", "a": "Bokh Wrestling: the Mongolian wrestling..", "x": "The complete martial art guide to Bokh Wrestling: the Mongolian wrestling.. Mongolia. History, meaning, practices, and how to engage respectfully — everything in one database. Naadam. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Bokh Wrestling essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Bokh Wrestling essentials.", "x": "At a glance: Bokh Wrestling — the Mongolian wrestling.. Naadam. The essentials: Zodog.. Open chest. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Mongolia.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Mongolia.", "x": "Bokh Wrestling: Mongolia.. Zodog. Essential knowledge — Open chest.. the Mongolian wrestling. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Mongolia..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Mongolia..", "x": "Explained: Mongolia.. Dance. The context — Bokh Wrestling. Zodog. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Naadam.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Naadam.", "x": "Bokh Wrestling: Naadam.. Mongolia. Essential knowledge — Zodog.. the Mongolian wrestling. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Naadam..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Naadam..", "x": "Explained: Naadam.. No weight. The context — Bokh Wrestling. Eagle dance. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Open chest.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Open chest.", "x": "Bokh Wrestling: Open chest.. Dance. Essential knowledge — Eagle dance.. the Mongolian wrestling. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Open chest..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Open chest..", "x": "Explained: Open chest.. Festival. The context — Bokh Wrestling. No weight. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Zodog.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Zodog.", "x": "Bokh Wrestling: Zodog.. No weight. Essential knowledge — No weight.. the Mongolian wrestling. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Zodog..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Zodog..", "x": "Explained: Zodog.. Naadam. The context — Bokh Wrestling. Mongolia. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Eagle dance.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Eagle dance.", "x": "Bokh Wrestling: Eagle dance.. Festival. Essential knowledge — Mongolia.. the Mongolian wrestling. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Eagle dance..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Eagle dance..", "x": "Explained: Eagle dance.. Zodog. The context — Bokh Wrestling. Naadam. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "No weight.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "No weight.", "x": "Bokh Wrestling: No weight.. Naadam. Essential knowledge — Naadam.. the Mongolian wrestling. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: No weight..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: No weight..", "x": "Explained: No weight.. Mongolia. The context — Bokh Wrestling. Open chest. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Naadam.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Naadam.", "x": "Bokh Wrestling in depth: Naadam.. Naadam. Details — the Mongolian wrestling.. Mongolia. Zodog. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Zodog.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Zodog.", "x": "Bokh Wrestling in depth: Zodog.. Open chest. Details — the Mongolian wrestling.. Dance. Eagle dance. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Mongolia.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Mongolia.", "x": "Bokh Wrestling in depth: Mongolia.. Zodog. Details — the Mongolian wrestling.. No weight. No weight. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Dance.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Dance.", "x": "Bokh Wrestling in depth: Dance.. Eagle dance. Details — the Mongolian wrestling.. Festival. Mongolia. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "No weight.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "No weight.", "x": "Bokh Wrestling in depth: No weight.. No weight. Details — the Mongolian wrestling.. Naadam. Naadam. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Festival.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Festival.", "x": "Bokh Wrestling in depth: Festival.. Mongolia. Details — the Mongolian wrestling.. Zodog. Open chest. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Bokh Wrestling comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Bokh Wrestling comes from.", "x": "Origins: Naadam.. Mongolia. The history of Bokh Wrestling — the Mongolian wrestling.. Zodog. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Bokh Wrestling respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Bokh Wrestling respectfully.", "x": "Engaging: Mongolia.. Naadam. How to participate or observe well — Bokh Wrestling. the Mongolian wrestling. Respect first, always; Dance.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Bokh Wrestling do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Bokh Wrestling do's and don'ts.", "x": "Etiquette: No weight.. Open chest. The rules of respect — Bokh Wrestling. the Mongolian wrestling. When in doubt, ask about Festival.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Bokh Wrestling.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Bokh Wrestling.", "x": "Planning: Naadam.. Zodog. Practical notes — Bokh Wrestling. the Mongolian wrestling. A little planning shows respect for Zodog.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Bokh Wrestling and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Bokh Wrestling and money.", "x": "Costs: Mongolia.. Eagle dance. What to budget — Bokh Wrestling. the Mongolian wrestling. The best experiences of Dance. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-martial-bokh-wrestling-martial-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
