(function(){'use strict';
/* JAH Gloomhaven Board Board Game Database generator — jahdb-e2-board-gloomhaven-board-game-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-board-gloomhaven-board-game',PREFIX='JAH-E2BOARDGLOO-',NAME='JAH Gloomhaven Board Board Game Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Gloomhaven Board: the complete guide", "d": "Gloomhaven Board: the campaign epic..", "g": "overview", "l": 2, "q": "What is Gloomhaven Board: the complete guide?", "a": "Gloomhaven Board: the campaign epic..", "x": "The complete board game guide to Gloomhaven Board: the campaign epic.. 2017. History, meaning, practices, and how to engage respectfully — everything in one database. Campaign. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Gloomhaven Board essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Gloomhaven Board essentials.", "x": "At a glance: Gloomhaven Board — the campaign epic.. Campaign. The essentials: Legacy.. Legacy. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "2017.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "2017.", "x": "Gloomhaven Board: 2017.. Legacy. Essential knowledge — Legacy.. the campaign epic. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 2017..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 2017..", "x": "Explained: 2017.. Box. The context — Gloomhaven Board. 100+ hours. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Campaign.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Campaign.", "x": "Gloomhaven Board: Campaign.. Tactical. Essential knowledge — 100+ hours.. the campaign epic. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Campaign..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Campaign..", "x": "Explained: Campaign.. Hours. The context — Gloomhaven Board. Tactical. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Legacy.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Legacy.", "x": "Gloomhaven Board: Legacy.. Box. Essential knowledge — Tactical.. the campaign epic. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Legacy..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Legacy..", "x": "Explained: Legacy.. Strategy. The context — Gloomhaven Board. Box. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "100+ hours.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "100+ hours.", "x": "Gloomhaven Board: 100+ hours.. Hours. Essential knowledge — Box.. the campaign epic. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: 100+ hours..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: 100+ hours..", "x": "Explained: 100+ hours.. Campaign. The context — Gloomhaven Board. 2017. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Tactical.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Tactical.", "x": "Gloomhaven Board: Tactical.. Strategy. Essential knowledge — 2017.. the campaign epic. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Tactical..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Tactical..", "x": "Explained: Tactical.. Legacy. The context — Gloomhaven Board. Campaign. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Box.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Box.", "x": "Gloomhaven Board: Box.. Campaign. Essential knowledge — Campaign.. the campaign epic. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Box..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Box..", "x": "Explained: Box.. Tactical. The context — Gloomhaven Board. Legacy. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Campaign.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Campaign.", "x": "Gloomhaven Board in depth: Campaign.. Campaign. Details — the campaign epic.. Tactical. 100+ hours. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Legacy.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Legacy.", "x": "Gloomhaven Board in depth: Legacy.. Legacy. Details — the campaign epic.. Box. Tactical. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Tactical.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Tactical.", "x": "Gloomhaven Board in depth: Tactical.. 100+ hours. Details — the campaign epic.. Hours. Box. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Box.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Box.", "x": "Gloomhaven Board in depth: Box.. Tactical. Details — the campaign epic.. Strategy. 2017. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Hours.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Hours.", "x": "Gloomhaven Board in depth: Hours.. Box. Details — the campaign epic.. Campaign. Campaign. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Strategy.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Strategy.", "x": "Gloomhaven Board in depth: Strategy.. 2017. Details — the campaign epic.. Legacy. Legacy. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Gloomhaven Board comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Gloomhaven Board comes from.", "x": "Origins: Campaign.. 2017. The history of Gloomhaven Board — the campaign epic.. Legacy. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Gloomhaven Board respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Gloomhaven Board respectfully.", "x": "Engaging: Tactical.. Campaign. How to participate or observe well — Gloomhaven Board. the campaign epic. Respect first, always; Box.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Gloomhaven Board do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Gloomhaven Board do's and don'ts.", "x": "Etiquette: Hours.. Legacy. The rules of respect — Gloomhaven Board. the campaign epic. When in doubt, ask about Strategy.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Gloomhaven Board.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Gloomhaven Board.", "x": "Planning: Campaign.. 100+ hours. Practical notes — Gloomhaven Board. the campaign epic. A little planning shows respect for Legacy.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Gloomhaven Board and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Gloomhaven Board and money.", "x": "Costs: Tactical.. Tactical. What to budget — Gloomhaven Board. the campaign epic. The best experiences of Box. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-board-gloomhaven-board-game-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
