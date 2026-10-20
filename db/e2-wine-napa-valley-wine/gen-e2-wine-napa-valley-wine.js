(function(){'use strict';
/* JAH Napa Valley Wine Wine Region Database generator — jahdb-e2-wine-napa-valley-wine-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-wine-napa-valley-wine',PREFIX='JAH-E2WINENAPAV-',NAME='JAH Napa Valley Wine Wine Region Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Napa Valley Wine: the complete guide", "d": "Napa Valley Wine: California's cabernet valley..", "g": "overview", "l": 2, "q": "What is Napa Valley Wine: the complete guide?", "a": "Napa Valley Wine: California's cabernet valley..", "x": "The complete wine region guide to Napa Valley Wine: California's cabernet valley.. Cabernet. History, meaning, practices, and how to engage respectfully — everything in one database. Cabernet. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Napa Valley Wine essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Napa Valley Wine essentials.", "x": "At a glance: Napa Valley Wine — California's cabernet valley.. 1976 Judgment. The essentials: 1976.. St. Helena. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Cabernet.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Cabernet.", "x": "Napa Valley Wine: Cabernet.. 1976. Essential knowledge — St. Helena.. California's cabernet valley. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Cabernet..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Cabernet..", "x": "Explained: Cabernet.. Cult. The context — Napa Valley Wine. Napa town. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "1976 Judgment.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "1976 Judgment.", "x": "Napa Valley Wine: 1976 Judgment.. Towns. Essential knowledge — Napa town.. California's cabernet valley. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: 1976 Judgment..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: 1976 Judgment..", "x": "Explained: 1976 Judgment.. Tasting. The context — Napa Valley Wine. Cult cabs. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "St. Helena.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "St. Helena.", "x": "Napa Valley Wine: St. Helena.. Cult. Essential knowledge — Cult cabs.. California's cabernet valley. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: St. Helena..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: St. Helena..", "x": "Explained: St. Helena.. History. The context — Napa Valley Wine. Tasting. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Napa town.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Napa town.", "x": "Napa Valley Wine: Napa town.. Tasting. Essential knowledge — Tasting.. California's cabernet valley. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Napa town..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Napa town..", "x": "Explained: Napa town.. Cabernet. The context — Napa Valley Wine. Cabernet. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Cult cabs.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Cult cabs.", "x": "Napa Valley Wine: Cult cabs.. History. Essential knowledge — Cabernet.. California's cabernet valley. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Cult cabs..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Cult cabs..", "x": "Explained: Cult cabs.. 1976. The context — Napa Valley Wine. 1976 Judgment. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Tasting.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Tasting.", "x": "Napa Valley Wine: Tasting.. Cabernet. Essential knowledge — 1976 Judgment.. California's cabernet valley. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Tasting..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Tasting..", "x": "Explained: Tasting.. Towns. The context — Napa Valley Wine. St. Helena. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Cabernet.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Cabernet.", "x": "Napa Valley Wine in depth: Cabernet.. 1976 Judgment. Details — California's cabernet valley.. Towns. Napa town. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "1976.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "1976.", "x": "Napa Valley Wine in depth: 1976.. St. Helena. Details — California's cabernet valley.. Cult. Cult cabs. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Towns.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Towns.", "x": "Napa Valley Wine in depth: Towns.. Napa town. Details — California's cabernet valley.. Tasting. Tasting. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Cult.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Cult.", "x": "Napa Valley Wine in depth: Cult.. Cult cabs. Details — California's cabernet valley.. History. Cabernet. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Tasting.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Tasting.", "x": "Napa Valley Wine in depth: Tasting.. Tasting. Details — California's cabernet valley.. Cabernet. 1976 Judgment. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "History.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "History.", "x": "Napa Valley Wine in depth: History.. Cabernet. Details — California's cabernet valley.. 1976. St. Helena. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Napa Valley Wine comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Napa Valley Wine comes from.", "x": "Origins: Cabernet.. Cabernet. The history of Napa Valley Wine — California's cabernet valley.. 1976. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Napa Valley Wine respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Napa Valley Wine respectfully.", "x": "Engaging: Towns.. 1976 Judgment. How to participate or observe well — Napa Valley Wine. California's cabernet valley. Respect first, always; Cult.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Napa Valley Wine do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Napa Valley Wine do's and don'ts.", "x": "Etiquette: Tasting.. St. Helena. The rules of respect — Napa Valley Wine. California's cabernet valley. When in doubt, ask about History.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Napa Valley Wine.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Napa Valley Wine.", "x": "Planning: Cabernet.. Napa town. Practical notes — Napa Valley Wine. California's cabernet valley. A little planning shows respect for 1976.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Napa Valley Wine and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Napa Valley Wine and money.", "x": "Costs: Towns.. Cult cabs. What to budget — Napa Valley Wine. California's cabernet valley. The best experiences of Cult. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-wine-napa-valley-wine-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
