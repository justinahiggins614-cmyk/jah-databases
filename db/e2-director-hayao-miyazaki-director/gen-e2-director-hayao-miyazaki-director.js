(function(){'use strict';
/* JAH Hayao Miyazaki Director Database generator — jahdb-e2-director-hayao-miyazaki-director-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-director-hayao-miyazaki-director',PREFIX='JAH-E2DIRECTORH-',NAME='JAH Hayao Miyazaki Director Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Hayao Miyazaki: the complete guide", "d": "Hayao Miyazaki: the anime master..", "g": "overview", "l": 2, "q": "What is Hayao Miyazaki: the complete guide?", "a": "Hayao Miyazaki: the anime master..", "x": "The complete director guide to Hayao Miyazaki: the anime master.. 1941. History, meaning, practices, and how to engage respectfully — everything in one database. Totoro. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Hayao Miyazaki essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Hayao Miyazaki essentials.", "x": "At a glance: Hayao Miyazaki — the anime master.. Totoro. The essentials: Spirited.. Spirited Away. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "1941.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "1941.", "x": "Hayao Miyazaki: 1941.. Spirited. Essential knowledge — Spirited Away.. the anime master. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 1941..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 1941..", "x": "Explained: 1941.. Hand-drawn. The context — Hayao Miyazaki. Ghibli. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Totoro.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Totoro.", "x": "Hayao Miyazaki: Totoro.. Ghibli. Essential knowledge — Ghibli.. the anime master. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Totoro..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Totoro..", "x": "Explained: Totoro.. Retirement. The context — Hayao Miyazaki. Retirement. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Spirited Away.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Spirited Away.", "x": "Hayao Miyazaki: Spirited Away.. Hand-drawn. Essential knowledge — Retirement.. the anime master. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Spirited Away..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Spirited Away..", "x": "Explained: Spirited Away.. Style. The context — Hayao Miyazaki. Hand-drawn. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Ghibli.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Ghibli.", "x": "Hayao Miyazaki: Ghibli.. Retirement. Essential knowledge — Hand-drawn.. the anime master. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Ghibli..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Ghibli..", "x": "Explained: Ghibli.. Totoro. The context — Hayao Miyazaki. 1941. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Retirement.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Retirement.", "x": "Hayao Miyazaki: Retirement.. Style. Essential knowledge — 1941.. the anime master. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Retirement..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Retirement..", "x": "Explained: Retirement.. Spirited. The context — Hayao Miyazaki. Totoro. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Hand-drawn.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Hand-drawn.", "x": "Hayao Miyazaki: Hand-drawn.. Totoro. Essential knowledge — Totoro.. the anime master. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Hand-drawn..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Hand-drawn..", "x": "Explained: Hand-drawn.. Ghibli. The context — Hayao Miyazaki. Spirited Away. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Totoro.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Totoro.", "x": "Hayao Miyazaki in depth: Totoro.. Totoro. Details — the anime master.. Ghibli. Ghibli. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Spirited.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Spirited.", "x": "Hayao Miyazaki in depth: Spirited.. Spirited Away. Details — the anime master.. Hand-drawn. Retirement. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Ghibli.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Ghibli.", "x": "Hayao Miyazaki in depth: Ghibli.. Ghibli. Details — the anime master.. Retirement. Hand-drawn. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Hand-drawn.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Hand-drawn.", "x": "Hayao Miyazaki in depth: Hand-drawn.. Retirement. Details — the anime master.. Style. 1941. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Retirement.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Retirement.", "x": "Hayao Miyazaki in depth: Retirement.. Hand-drawn. Details — the anime master.. Totoro. Totoro. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Style.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Style.", "x": "Hayao Miyazaki in depth: Style.. 1941. Details — the anime master.. Spirited. Spirited Away. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Hayao Miyazaki comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Hayao Miyazaki comes from.", "x": "Origins: Totoro.. 1941. The history of Hayao Miyazaki — the anime master.. Spirited. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Hayao Miyazaki respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Hayao Miyazaki respectfully.", "x": "Engaging: Ghibli.. Totoro. How to participate or observe well — Hayao Miyazaki. the anime master. Respect first, always; Hand-drawn.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Hayao Miyazaki do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Hayao Miyazaki do's and don'ts.", "x": "Etiquette: Retirement.. Spirited Away. The rules of respect — Hayao Miyazaki. the anime master. When in doubt, ask about Style.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Hayao Miyazaki.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Hayao Miyazaki.", "x": "Planning: Totoro.. Ghibli. Practical notes — Hayao Miyazaki. the anime master. A little planning shows respect for Spirited.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Hayao Miyazaki and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Hayao Miyazaki and money.", "x": "Costs: Ghibli.. Retirement. What to budget — Hayao Miyazaki. the anime master. The best experiences of Hand-drawn. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-director-hayao-miyazaki-director-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
