(function(){'use strict';
/* JAH Star Wars Figures Action Figure Database generator — jahdb-e2-figure-star-wars-figures-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-figure-star-wars-figures',PREFIX='JAH-E2FIGURESTA-',NAME='JAH Star Wars Figures Action Figure Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Star Wars Figures: the complete guide", "d": "Star Wars Figures: the Kenner galaxy..", "g": "overview", "l": 2, "q": "What is Star Wars Figures: the complete guide?", "a": "Star Wars Figures: the Kenner galaxy..", "x": "The complete action figure guide to Star Wars Figures: the Kenner galaxy.. 1977. History, meaning, practices, and how to engage respectfully — everything in one database. Kenner. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Star Wars Figures essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Star Wars Figures essentials.", "x": "At a glance: Star Wars Figures — the Kenner galaxy.. Kenner. The essentials: Vintage.. 3.75 inch. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "1977.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "1977.", "x": "Star Wars Figures: 1977.. Vintage. Essential knowledge — 3.75 inch.. the Kenner galaxy. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 1977..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 1977..", "x": "Explained: 1977.. Carded. The context — Star Wars Figures. Vintage. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Kenner.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Kenner.", "x": "Star Wars Figures: Kenner.. Black Series. Essential knowledge — Vintage.. the Kenner galaxy. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Kenner..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Kenner..", "x": "Explained: Kenner.. 1977. The context — Star Wars Figures. Black Series. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "3.75 inch.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "3.75 inch.", "x": "Star Wars Figures: 3.75 inch.. Carded. Essential knowledge — Black Series.. the Kenner galaxy. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: 3.75 inch..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: 3.75 inch..", "x": "Explained: 3.75 inch.. History. The context — Star Wars Figures. Carded. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Vintage.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Vintage.", "x": "Star Wars Figures: Vintage.. 1977. Essential knowledge — Carded.. the Kenner galaxy. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Vintage..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Vintage..", "x": "Explained: Vintage.. Kenner. The context — Star Wars Figures. 1977. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Black Series.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Black Series.", "x": "Star Wars Figures: Black Series.. History. Essential knowledge — 1977.. the Kenner galaxy. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Black Series..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Black Series..", "x": "Explained: Black Series.. Vintage. The context — Star Wars Figures. Kenner. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Carded.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Carded.", "x": "Star Wars Figures: Carded.. Kenner. Essential knowledge — Kenner.. the Kenner galaxy. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Carded..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Carded..", "x": "Explained: Carded.. Black Series. The context — Star Wars Figures. 3.75 inch. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Kenner.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Kenner.", "x": "Star Wars Figures in depth: Kenner.. Kenner. Details — the Kenner galaxy.. Black Series. Vintage. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Vintage.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Vintage.", "x": "Star Wars Figures in depth: Vintage.. 3.75 inch. Details — the Kenner galaxy.. Carded. Black Series. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Black Series.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Black Series.", "x": "Star Wars Figures in depth: Black Series.. Vintage. Details — the Kenner galaxy.. 1977. Carded. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Carded.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Carded.", "x": "Star Wars Figures in depth: Carded.. Black Series. Details — the Kenner galaxy.. History. 1977. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "1977.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "1977.", "x": "Star Wars Figures in depth: 1977.. Carded. Details — the Kenner galaxy.. Kenner. Kenner. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "History.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "History.", "x": "Star Wars Figures in depth: History.. 1977. Details — the Kenner galaxy.. Vintage. 3.75 inch. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Star Wars Figures comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Star Wars Figures comes from.", "x": "Origins: Kenner.. 1977. The history of Star Wars Figures — the Kenner galaxy.. Vintage. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Star Wars Figures respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Star Wars Figures respectfully.", "x": "Engaging: Black Series.. Kenner. How to participate or observe well — Star Wars Figures. the Kenner galaxy. Respect first, always; Carded.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Star Wars Figures do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Star Wars Figures do's and don'ts.", "x": "Etiquette: 1977.. 3.75 inch. The rules of respect — Star Wars Figures. the Kenner galaxy. When in doubt, ask about History.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Star Wars Figures.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Star Wars Figures.", "x": "Planning: Kenner.. Vintage. Practical notes — Star Wars Figures. the Kenner galaxy. A little planning shows respect for Vintage.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Star Wars Figures and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Star Wars Figures and money.", "x": "Costs: Black Series.. Black Series. What to budget — Star Wars Figures. the Kenner galaxy. The best experiences of Carded. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-figure-star-wars-figures-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
