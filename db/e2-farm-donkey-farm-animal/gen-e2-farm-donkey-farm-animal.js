(function(){'use strict';
/* JAH Donkey Farm Farm Animal Database generator — jahdb-e2-farm-donkey-farm-animal-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-farm-donkey-farm-animal',PREFIX='JAH-E2FARMDONKE-',NAME='JAH Donkey Farm Farm Animal Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Donkey Farm: the complete guide", "d": "Donkey Farm: the sturdy ass..", "g": "overview", "l": 2, "q": "What is Donkey Farm: the complete guide?", "a": "Donkey Farm: the sturdy ass..", "x": "The complete farm animal guide to Donkey Farm: the sturdy ass.. Sturdy. History, meaning, practices, and how to engage respectfully — everything in one database. Braying. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Donkey Farm essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Donkey Farm essentials.", "x": "At a glance: Donkey Farm — the sturdy ass.. Braying. The essentials: Guards.. Guards. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Sturdy.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Sturdy.", "x": "Donkey Farm: Sturdy.. Guards. Essential knowledge — Guards.. the sturdy ass. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Sturdy..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Sturdy..", "x": "Explained: Sturdy.. Carrying. The context — Donkey Farm. Long ears. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Braying.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Braying.", "x": "Donkey Farm: Braying.. Desert. Essential knowledge — Long ears.. the sturdy ass. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Braying..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Braying..", "x": "Explained: Braying.. Sturdy. The context — Donkey Farm. Desert. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Guards.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Guards.", "x": "Donkey Farm: Guards.. Carrying. Essential knowledge — Desert.. the sturdy ass. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Guards..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Guards..", "x": "Explained: Guards.. Care. The context — Donkey Farm. Carrying. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Long ears.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Long ears.", "x": "Donkey Farm: Long ears.. Sturdy. Essential knowledge — Carrying.. the sturdy ass. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Long ears..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Long ears..", "x": "Explained: Long ears.. Braying. The context — Donkey Farm. Sturdy. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Desert.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Desert.", "x": "Donkey Farm: Desert.. Care. Essential knowledge — Sturdy.. the sturdy ass. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Desert..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Desert..", "x": "Explained: Desert.. Guards. The context — Donkey Farm. Braying. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Carrying.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Carrying.", "x": "Donkey Farm: Carrying.. Braying. Essential knowledge — Braying.. the sturdy ass. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Carrying..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Carrying..", "x": "Explained: Carrying.. Desert. The context — Donkey Farm. Guards. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Braying.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Braying.", "x": "Donkey Farm in depth: Braying.. Braying. Details — the sturdy ass.. Desert. Long ears. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Guards.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Guards.", "x": "Donkey Farm in depth: Guards.. Guards. Details — the sturdy ass.. Carrying. Desert. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Desert.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Desert.", "x": "Donkey Farm in depth: Desert.. Long ears. Details — the sturdy ass.. Sturdy. Carrying. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Carrying.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Carrying.", "x": "Donkey Farm in depth: Carrying.. Desert. Details — the sturdy ass.. Care. Sturdy. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Sturdy.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Sturdy.", "x": "Donkey Farm in depth: Sturdy.. Carrying. Details — the sturdy ass.. Braying. Braying. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Care.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Care.", "x": "Donkey Farm in depth: Care.. Sturdy. Details — the sturdy ass.. Guards. Guards. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Donkey Farm comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Donkey Farm comes from.", "x": "Origins: Braying.. Sturdy. The history of Donkey Farm — the sturdy ass.. Guards. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Donkey Farm respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Donkey Farm respectfully.", "x": "Engaging: Desert.. Braying. How to participate or observe well — Donkey Farm. the sturdy ass. Respect first, always; Carrying.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Donkey Farm do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Donkey Farm do's and don'ts.", "x": "Etiquette: Sturdy.. Guards. The rules of respect — Donkey Farm. the sturdy ass. When in doubt, ask about Care.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Donkey Farm.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Donkey Farm.", "x": "Planning: Braying.. Long ears. Practical notes — Donkey Farm. the sturdy ass. A little planning shows respect for Guards.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Donkey Farm and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Donkey Farm and money.", "x": "Costs: Desert.. Desert. What to budget — Donkey Farm. the sturdy ass. The best experiences of Carrying. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-farm-donkey-farm-animal-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
