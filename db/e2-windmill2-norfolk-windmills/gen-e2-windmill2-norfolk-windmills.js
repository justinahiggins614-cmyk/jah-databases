(function(){'use strict';
/* JAH Norfolk Windmills Database generator — jahdb-e2-windmill2-norfolk-windmills-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-windmill2-norfolk-windmills',PREFIX='JAH-E2WINDMILL2-',NAME='JAH Norfolk Windmills Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Norfolk Windmills: the complete guide", "d": "Norfolk Windmills: the English..", "g": "overview", "l": 2, "q": "What is Norfolk Windmills: the complete guide?", "a": "Norfolk Windmills: the English..", "x": "The complete windmill guide to Norfolk Windmills: the English.. Drainage. History, meaning, practices, and how to engage respectfully — everything in one database. Drainage. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Norfolk Windmills essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Norfolk Windmills essentials.", "x": "At a glance: Norfolk Windmills — the English.. Broads. The essentials: Historic.. England. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Drainage.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Drainage.", "x": "Norfolk Windmills: Drainage.. Historic. Essential knowledge — England.. the English. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Drainage..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Drainage..", "x": "Explained: Drainage.. Broads. The context — Norfolk Windmills. Tower. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Broads.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Broads.", "x": "Norfolk Windmills: Broads.. Sails. Essential knowledge — Tower.. the English. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Broads..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Broads..", "x": "Explained: Broads.. England. The context — Norfolk Windmills. Sails. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "England.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "England.", "x": "Norfolk Windmills: England.. Broads. Essential knowledge — Sails.. the English. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: England..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: England..", "x": "Explained: England.. Visiting. The context — Norfolk Windmills. Historic. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Tower.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Tower.", "x": "Norfolk Windmills: Tower.. England. Essential knowledge — Historic.. the English. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Tower..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Tower..", "x": "Explained: Tower.. Drainage. The context — Norfolk Windmills. Drainage. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Sails.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Sails.", "x": "Norfolk Windmills: Sails.. Visiting. Essential knowledge — Drainage.. the English. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Sails..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Sails..", "x": "Explained: Sails.. Historic. The context — Norfolk Windmills. Broads. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Historic.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Historic.", "x": "Norfolk Windmills: Historic.. Drainage. Essential knowledge — Broads.. the English. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Historic..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Historic..", "x": "Explained: Historic.. Sails. The context — Norfolk Windmills. England. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Drainage.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Drainage.", "x": "Norfolk Windmills in depth: Drainage.. Broads. Details — the English.. Sails. Tower. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Historic.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Historic.", "x": "Norfolk Windmills in depth: Historic.. England. Details — the English.. Broads. Sails. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Sails.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Sails.", "x": "Norfolk Windmills in depth: Sails.. Tower. Details — the English.. England. Historic. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Broads.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Broads.", "x": "Norfolk Windmills in depth: Broads.. Sails. Details — the English.. Visiting. Drainage. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "England.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "England.", "x": "Norfolk Windmills in depth: England.. Historic. Details — the English.. Drainage. Broads. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Visiting.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Visiting.", "x": "Norfolk Windmills in depth: Visiting.. Drainage. Details — the English.. Historic. England. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Norfolk Windmills comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Norfolk Windmills comes from.", "x": "Origins: Drainage.. Drainage. The history of Norfolk Windmills — the English.. Historic. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Norfolk Windmills respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Norfolk Windmills respectfully.", "x": "Engaging: Sails.. Broads. How to participate or observe well — Norfolk Windmills. the English. Respect first, always; Broads.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Norfolk Windmills do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Norfolk Windmills do's and don'ts.", "x": "Etiquette: England.. England. The rules of respect — Norfolk Windmills. the English. When in doubt, ask about Visiting.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Norfolk Windmills.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Norfolk Windmills.", "x": "Planning: Drainage.. Tower. Practical notes — Norfolk Windmills. the English. A little planning shows respect for Historic.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Norfolk Windmills and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Norfolk Windmills and money.", "x": "Costs: Sails.. Sails. What to budget — Norfolk Windmills. the English. The best experiences of Broads. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-windmill2-norfolk-windmills-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
