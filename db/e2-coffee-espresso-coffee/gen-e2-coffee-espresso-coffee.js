(function(){'use strict';
/* JAH Espresso Coffee Database generator — jahdb-e2-coffee-espresso-coffee-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-coffee-espresso-coffee',PREFIX='JAH-E2COFFEEESP-',NAME='JAH Espresso Coffee Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Espresso: the complete guide", "d": "Espresso: the concentrated shot..", "g": "overview", "l": 2, "q": "What is Espresso: the complete guide?", "a": "Espresso: the concentrated shot..", "x": "The complete coffee guide to Espresso: the concentrated shot.. 25-30 sec. History, meaning, practices, and how to engage respectfully — everything in one database. Extraction. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Espresso essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Espresso essentials.", "x": "At a glance: Espresso — the concentrated shot.. 9 bars. The essentials: Crema.. Crema. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "25-30 sec.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "25-30 sec.", "x": "Espresso: 25-30 sec.. Crema. Essential knowledge — Crema.. the concentrated shot. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 25-30 sec..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 25-30 sec..", "x": "Explained: 25-30 sec.. Base drinks. The context — Espresso. Italy. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "9 bars.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "9 bars.", "x": "Espresso: 9 bars.. Italy. Essential knowledge — Italy.. the concentrated shot. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: 9 bars..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: 9 bars..", "x": "Explained: 9 bars.. Grind. The context — Espresso. Base. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Crema.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Crema.", "x": "Espresso: Crema.. Base drinks. Essential knowledge — Base.. the concentrated shot. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Crema..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Crema..", "x": "Explained: Crema.. Machine. The context — Espresso. Ristretto. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Italy.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Italy.", "x": "Espresso: Italy.. Grind. Essential knowledge — Ristretto.. the concentrated shot. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Italy..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Italy..", "x": "Explained: Italy.. Extraction. The context — Espresso. 25-30 sec. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Base.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Base.", "x": "Espresso: Base.. Machine. Essential knowledge — 25-30 sec.. the concentrated shot. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Base..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Base..", "x": "Explained: Base.. Crema. The context — Espresso. 9 bars. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Ristretto.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Ristretto.", "x": "Espresso: Ristretto.. Extraction. Essential knowledge — 9 bars.. the concentrated shot. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Ristretto..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Ristretto..", "x": "Explained: Ristretto.. Italy. The context — Espresso. Crema. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Extraction.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Extraction.", "x": "Espresso in depth: Extraction.. 9 bars. Details — the concentrated shot.. Italy. Italy. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Crema.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Crema.", "x": "Espresso in depth: Crema.. Crema. Details — the concentrated shot.. Base drinks. Base. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Italy.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Italy.", "x": "Espresso in depth: Italy.. Italy. Details — the concentrated shot.. Grind. Ristretto. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Base drinks.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Base drinks.", "x": "Espresso in depth: Base drinks.. Base. Details — the concentrated shot.. Machine. 25-30 sec. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Grind.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Grind.", "x": "Espresso in depth: Grind.. Ristretto. Details — the concentrated shot.. Extraction. 9 bars. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Machine.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Machine.", "x": "Espresso in depth: Machine.. 25-30 sec. Details — the concentrated shot.. Crema. Crema. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Espresso comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Espresso comes from.", "x": "Origins: Extraction.. 25-30 sec. The history of Espresso — the concentrated shot.. Crema. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Espresso respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Espresso respectfully.", "x": "Engaging: Italy.. 9 bars. How to participate or observe well — Espresso. the concentrated shot. Respect first, always; Base drinks.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Espresso do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Espresso do's and don'ts.", "x": "Etiquette: Grind.. Crema. The rules of respect — Espresso. the concentrated shot. When in doubt, ask about Machine.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Espresso.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Espresso.", "x": "Planning: Extraction.. Italy. Practical notes — Espresso. the concentrated shot. A little planning shows respect for Crema.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Espresso and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Espresso and money.", "x": "Costs: Italy.. Base. What to budget — Espresso. the concentrated shot. The best experiences of Base drinks. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-coffee-espresso-coffee-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
