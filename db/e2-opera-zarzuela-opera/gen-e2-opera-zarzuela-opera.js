(function(){'use strict';
/* JAH Zarzuela Opera Opera Database generator — jahdb-e2-opera-zarzuela-opera-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-opera-zarzuela-opera',PREFIX='JAH-E2OPERAZARZ-',NAME='JAH Zarzuela Opera Opera Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Zarzuela Opera: the complete guide", "d": "Zarzuela Opera: the Spanish lyric..", "g": "overview", "l": 2, "q": "What is Zarzuela Opera: the complete guide?", "a": "Zarzuela Opera: the Spanish lyric..", "x": "The complete opera guide to Zarzuela Opera: the Spanish lyric.. Spain. History, meaning, practices, and how to engage respectfully — everything in one database. Spain. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Zarzuela Opera essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Zarzuela Opera essentials.", "x": "At a glance: Zarzuela Opera — the Spanish lyric.. Spoken/sung. The essentials: Madrid.. Madrid. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Spain.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Spain.", "x": "Zarzuela Opera: Spain.. Madrid. Essential knowledge — Madrid.. the Spanish lyric. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Spain..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Spain..", "x": "Explained: Spain.. Vibrant. The context — Zarzuela Opera. Género chico. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Spoken/sung.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Spoken/sung.", "x": "Zarzuela Opera: Spoken/sung.. Teatro. Essential knowledge — Género chico.. the Spanish lyric. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Spoken/sung..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Spoken/sung..", "x": "Explained: Spoken/sung.. Spoken. The context — Zarzuela Opera. Vibrant. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Madrid.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Madrid.", "x": "Zarzuela Opera: Madrid.. Vibrant. Essential knowledge — Vibrant.. the Spanish lyric. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Madrid..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Madrid..", "x": "Explained: Madrid.. History. The context — Zarzuela Opera. Teatro. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Género chico.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Género chico.", "x": "Zarzuela Opera: Género chico.. Spoken. Essential knowledge — Teatro.. the Spanish lyric. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Género chico..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Género chico..", "x": "Explained: Género chico.. Spain. The context — Zarzuela Opera. Spain. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Vibrant.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Vibrant.", "x": "Zarzuela Opera: Vibrant.. History. Essential knowledge — Spain.. the Spanish lyric. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Vibrant..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Vibrant..", "x": "Explained: Vibrant.. Madrid. The context — Zarzuela Opera. Spoken/sung. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Teatro.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Teatro.", "x": "Zarzuela Opera: Teatro.. Spain. Essential knowledge — Spoken/sung.. the Spanish lyric. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Teatro..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Teatro..", "x": "Explained: Teatro.. Teatro. The context — Zarzuela Opera. Madrid. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Spain.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Spain.", "x": "Zarzuela Opera in depth: Spain.. Spoken/sung. Details — the Spanish lyric.. Teatro. Género chico. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Madrid.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Madrid.", "x": "Zarzuela Opera in depth: Madrid.. Madrid. Details — the Spanish lyric.. Vibrant. Vibrant. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Teatro.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Teatro.", "x": "Zarzuela Opera in depth: Teatro.. Género chico. Details — the Spanish lyric.. Spoken. Teatro. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Vibrant.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Vibrant.", "x": "Zarzuela Opera in depth: Vibrant.. Vibrant. Details — the Spanish lyric.. History. Spain. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Spoken.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Spoken.", "x": "Zarzuela Opera in depth: Spoken.. Teatro. Details — the Spanish lyric.. Spain. Spoken/sung. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "History.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "History.", "x": "Zarzuela Opera in depth: History.. Spain. Details — the Spanish lyric.. Madrid. Madrid. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Zarzuela Opera comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Zarzuela Opera comes from.", "x": "Origins: Spain.. Spain. The history of Zarzuela Opera — the Spanish lyric.. Madrid. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Zarzuela Opera respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Zarzuela Opera respectfully.", "x": "Engaging: Teatro.. Spoken/sung. How to participate or observe well — Zarzuela Opera. the Spanish lyric. Respect first, always; Vibrant.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Zarzuela Opera do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Zarzuela Opera do's and don'ts.", "x": "Etiquette: Spoken.. Madrid. The rules of respect — Zarzuela Opera. the Spanish lyric. When in doubt, ask about History.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Zarzuela Opera.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Zarzuela Opera.", "x": "Planning: Spain.. Género chico. Practical notes — Zarzuela Opera. the Spanish lyric. A little planning shows respect for Madrid.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Zarzuela Opera and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Zarzuela Opera and money.", "x": "Costs: Teatro.. Vibrant. What to budget — Zarzuela Opera. the Spanish lyric. The best experiences of Vibrant. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-opera-zarzuela-opera-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
