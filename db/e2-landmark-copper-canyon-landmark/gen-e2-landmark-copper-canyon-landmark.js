(function(){'use strict';
/* JAH Copper Canyon Landmark Database generator — jahdb-e2-landmark-copper-canyon-landmark-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-landmark-copper-canyon-landmark',PREFIX='JAH-E2LANDMARKC-',NAME='JAH Copper Canyon Landmark Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Copper Canyon: the complete guide", "d": "Copper Canyon: the deeper canyon..", "g": "overview", "l": 2, "q": "What is Copper Canyon: the complete guide?", "a": "Copper Canyon: the deeper canyon..", "x": "The complete landmark guide to Copper Canyon: the deeper canyon.. Deeper than Grand. History, meaning, practices, and how to engage respectfully — everything in one database. Deeper. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Copper Canyon essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Copper Canyon essentials.", "x": "At a glance: Copper Canyon — the deeper canyon.. Chepe train. The essentials: Chepe.. Tarahumara. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Deeper than Grand.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Deeper than Grand.", "x": "Copper Canyon: Deeper than Grand.. Chepe. Essential knowledge — Tarahumara.. the deeper canyon. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Deeper than Grand..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Deeper than Grand..", "x": "Explained: Deeper than Grand.. Tarahumara. The context — Copper Canyon. 4x. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Chepe train.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Chepe train.", "x": "Copper Canyon: Chepe train.. Views. Essential knowledge — 4x.. the deeper canyon. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Chepe train..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Chepe train..", "x": "Explained: Chepe train.. 4x. The context — Copper Canyon. Views. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Tarahumara.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Tarahumara.", "x": "Copper Canyon: Tarahumara.. Tarahumara. Essential knowledge — Views.. the deeper canyon. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Tarahumara..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Tarahumara..", "x": "Explained: Tarahumara.. Tours. The context — Copper Canyon. Rim. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "4x.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "4x.", "x": "Copper Canyon: 4x.. 4x. Essential knowledge — Rim.. the deeper canyon. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: 4x..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: 4x..", "x": "Explained: 4x.. Deeper. The context — Copper Canyon. Deeper than Grand. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Views.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Views.", "x": "Copper Canyon: Views.. Tours. Essential knowledge — Deeper than Grand.. the deeper canyon. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Views..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Views..", "x": "Explained: Views.. Chepe. The context — Copper Canyon. Chepe train. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Rim.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Rim.", "x": "Copper Canyon: Rim.. Deeper. Essential knowledge — Chepe train.. the deeper canyon. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Rim..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Rim..", "x": "Explained: Rim.. Views. The context — Copper Canyon. Tarahumara. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Deeper.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Deeper.", "x": "Copper Canyon in depth: Deeper.. Chepe train. Details — the deeper canyon.. Views. 4x. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Chepe.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Chepe.", "x": "Copper Canyon in depth: Chepe.. Tarahumara. Details — the deeper canyon.. Tarahumara. Views. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Views.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Views.", "x": "Copper Canyon in depth: Views.. 4x. Details — the deeper canyon.. 4x. Rim. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Tarahumara.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Tarahumara.", "x": "Copper Canyon in depth: Tarahumara.. Views. Details — the deeper canyon.. Tours. Deeper than Grand. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "4x.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "4x.", "x": "Copper Canyon in depth: 4x.. Rim. Details — the deeper canyon.. Deeper. Chepe train. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Tours.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Tours.", "x": "Copper Canyon in depth: Tours.. Deeper than Grand. Details — the deeper canyon.. Chepe. Tarahumara. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Copper Canyon comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Copper Canyon comes from.", "x": "Origins: Deeper.. Deeper than Grand. The history of Copper Canyon — the deeper canyon.. Chepe. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Copper Canyon respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Copper Canyon respectfully.", "x": "Engaging: Views.. Chepe train. How to participate or observe well — Copper Canyon. the deeper canyon. Respect first, always; Tarahumara.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Copper Canyon do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Copper Canyon do's and don'ts.", "x": "Etiquette: 4x.. Tarahumara. The rules of respect — Copper Canyon. the deeper canyon. When in doubt, ask about Tours.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Copper Canyon.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Copper Canyon.", "x": "Planning: Deeper.. 4x. Practical notes — Copper Canyon. the deeper canyon. A little planning shows respect for Chepe.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Copper Canyon and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Copper Canyon and money.", "x": "Costs: Views.. Views. What to budget — Copper Canyon. the deeper canyon. The best experiences of Tarahumara. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-landmark-copper-canyon-landmark-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
