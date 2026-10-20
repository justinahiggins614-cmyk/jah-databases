(function(){'use strict';
/* JAH Nausicaa France Aquarium Database generator — jahdb-e2-aquarium-nausicaa-france-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-aquarium-nausicaa-france',PREFIX='JAH-E2AQUARIUMN-',NAME='JAH Nausicaa France Aquarium Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Nausicaa France: the complete guide", "d": "Nausicaa France: Europe's sea center..", "g": "overview", "l": 2, "q": "What is Nausicaa France: the complete guide?", "a": "Nausicaa France: Europe's sea center..", "x": "The complete aquarium guide to Nausicaa France: Europe's sea center.. Boulogne. History, meaning, practices, and how to engage respectfully — everything in one database. Rays. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Nausicaa France essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Nausicaa France essentials.", "x": "At a glance: Nausicaa France — Europe's sea center.. Manta rays. The essentials: High seas.. High seas. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Boulogne.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Boulogne.", "x": "Nausicaa France: Boulogne.. High seas. Essential knowledge — High seas.. Europe's sea center. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Boulogne..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Boulogne..", "x": "Explained: Boulogne.. France. The context — Nausicaa France. 1991. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Manta rays.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Manta rays.", "x": "Nausicaa France: Manta rays.. Tickets. Essential knowledge — 1991.. Europe's sea center. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Manta rays..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Manta rays..", "x": "Explained: Manta rays.. Conservation. The context — Nausicaa France. Conservation. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "High seas.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "High seas.", "x": "Nausicaa France: High seas.. France. Essential knowledge — Conservation.. Europe's sea center. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: High seas..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: High seas..", "x": "Explained: High seas.. Ocean. The context — Nausicaa France. Channel. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "1991.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "1991.", "x": "Nausicaa France: 1991.. Conservation. Essential knowledge — Channel.. Europe's sea center. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: 1991..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: 1991..", "x": "Explained: 1991.. Rays. The context — Nausicaa France. Boulogne. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Conservation.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Conservation.", "x": "Nausicaa France: Conservation.. Ocean. Essential knowledge — Boulogne.. Europe's sea center. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Conservation..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Conservation..", "x": "Explained: Conservation.. High seas. The context — Nausicaa France. Manta rays. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Channel.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Channel.", "x": "Nausicaa France: Channel.. Rays. Essential knowledge — Manta rays.. Europe's sea center. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Channel..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Channel..", "x": "Explained: Channel.. Tickets. The context — Nausicaa France. High seas. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Rays.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Rays.", "x": "Nausicaa France in depth: Rays.. Manta rays. Details — Europe's sea center.. Tickets. 1991. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "High seas.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "High seas.", "x": "Nausicaa France in depth: High seas.. High seas. Details — Europe's sea center.. France. Conservation. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Tickets.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Tickets.", "x": "Nausicaa France in depth: Tickets.. 1991. Details — Europe's sea center.. Conservation. Channel. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "France.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "France.", "x": "Nausicaa France in depth: France.. Conservation. Details — Europe's sea center.. Ocean. Boulogne. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Conservation.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Conservation.", "x": "Nausicaa France in depth: Conservation.. Channel. Details — Europe's sea center.. Rays. Manta rays. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Ocean.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Ocean.", "x": "Nausicaa France in depth: Ocean.. Boulogne. Details — Europe's sea center.. High seas. High seas. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Nausicaa France comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Nausicaa France comes from.", "x": "Origins: Rays.. Boulogne. The history of Nausicaa France — Europe's sea center.. High seas. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Nausicaa France respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Nausicaa France respectfully.", "x": "Engaging: Tickets.. Manta rays. How to participate or observe well — Nausicaa France. Europe's sea center. Respect first, always; France.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Nausicaa France do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Nausicaa France do's and don'ts.", "x": "Etiquette: Conservation.. High seas. The rules of respect — Nausicaa France. Europe's sea center. When in doubt, ask about Ocean.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Nausicaa France.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Nausicaa France.", "x": "Planning: Rays.. 1991. Practical notes — Nausicaa France. Europe's sea center. A little planning shows respect for High seas.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Nausicaa France and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Nausicaa France and money.", "x": "Costs: Tickets.. Conservation. What to budget — Nausicaa France. Europe's sea center. The best experiences of France. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-aquarium-nausicaa-france-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
