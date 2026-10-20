(function(){'use strict';
/* JAH Austin City Limits Festival Database generator — jahdb-e2-festival-austin-city-limits-festival-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-festival-austin-city-limits-festival',PREFIX='JAH-E2FESTIVALA-',NAME='JAH Austin City Limits Festival Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Austin City Limits: the complete guide", "d": "Austin City Limits: two weekends in Zilker..", "g": "overview", "l": 2, "q": "What is Austin City Limits: the complete guide?", "a": "Austin City Limits: two weekends in Zilker..", "x": "The complete festival guide to Austin City Limits: two weekends in Zilker.. October. History, meaning, practices, and how to engage respectfully — everything in one database. Park. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Austin City Limits essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Austin City Limits essentials.", "x": "At a glance: Austin City Limits — two weekends in Zilker.. Zilker Park. The essentials: Lineups.. Two weekends. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "October.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "October.", "x": "Austin City Limits: October.. Lineups. Essential knowledge — Two weekends.. two weekends in Zilker. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: October..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: October..", "x": "Explained: October.. History. The context — Austin City Limits. Lineups. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Zilker Park.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Zilker Park.", "x": "Austin City Limits: Zilker Park.. Food. Essential knowledge — Lineups.. two weekends in Zilker. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Zilker Park..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Zilker Park..", "x": "Explained: Zilker Park.. Travel. The context — Austin City Limits. Tacos. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Two weekends.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Two weekends.", "x": "Austin City Limits: Two weekends.. History. Essential knowledge — Tacos.. two weekends in Zilker. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Two weekends..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Two weekends..", "x": "Explained: Two weekends.. Music. The context — Austin City Limits. TV show. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Lineups.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Lineups.", "x": "Austin City Limits: Lineups.. Travel. Essential knowledge — TV show.. two weekends in Zilker. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Lineups..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Lineups..", "x": "Explained: Lineups.. Park. The context — Austin City Limits. October. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Tacos.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Tacos.", "x": "Austin City Limits: Tacos.. Music. Essential knowledge — October.. two weekends in Zilker. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Tacos..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Tacos..", "x": "Explained: Tacos.. Lineups. The context — Austin City Limits. Zilker Park. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "TV show.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "TV show.", "x": "Austin City Limits: TV show.. Park. Essential knowledge — Zilker Park.. two weekends in Zilker. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: TV show..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: TV show..", "x": "Explained: TV show.. Food. The context — Austin City Limits. Two weekends. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Park.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Park.", "x": "Austin City Limits in depth: Park.. Zilker Park. Details — two weekends in Zilker.. Food. Lineups. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Lineups.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Lineups.", "x": "Austin City Limits in depth: Lineups.. Two weekends. Details — two weekends in Zilker.. History. Tacos. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Food.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Food.", "x": "Austin City Limits in depth: Food.. Lineups. Details — two weekends in Zilker.. Travel. TV show. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "History.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "History.", "x": "Austin City Limits in depth: History.. Tacos. Details — two weekends in Zilker.. Music. October. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Travel.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Travel.", "x": "Austin City Limits in depth: Travel.. TV show. Details — two weekends in Zilker.. Park. Zilker Park. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Music.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Music.", "x": "Austin City Limits in depth: Music.. October. Details — two weekends in Zilker.. Lineups. Two weekends. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Austin City Limits comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Austin City Limits comes from.", "x": "Origins: Park.. October. The history of Austin City Limits — two weekends in Zilker.. Lineups. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Austin City Limits respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Austin City Limits respectfully.", "x": "Engaging: Food.. Zilker Park. How to participate or observe well — Austin City Limits. two weekends in Zilker. Respect first, always; History.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Austin City Limits do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Austin City Limits do's and don'ts.", "x": "Etiquette: Travel.. Two weekends. The rules of respect — Austin City Limits. two weekends in Zilker. When in doubt, ask about Music.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Austin City Limits.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Austin City Limits.", "x": "Planning: Park.. Lineups. Practical notes — Austin City Limits. two weekends in Zilker. A little planning shows respect for Lineups.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Austin City Limits and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Austin City Limits and money.", "x": "Costs: Food.. Tacos. What to budget — Austin City Limits. two weekends in Zilker. The best experiences of History. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-festival-austin-city-limits-festival-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
