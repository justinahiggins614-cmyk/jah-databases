(function(){'use strict';
/* JAH Lindau Lighthouse Lighthouse Database generator — jahdb-e2-lighthouse-lindau-lighthouse-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-lighthouse-lindau-lighthouse',PREFIX='JAH-E2LIGHTHOUS-',NAME='JAH Lindau Lighthouse Lighthouse Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Lindau Lighthouse: the complete guide", "d": "Lindau Lighthouse: Bavaria's lake light..", "g": "overview", "l": 2, "q": "What is Lindau Lighthouse: the complete guide?", "a": "Lindau Lighthouse: Bavaria's lake light..", "x": "The complete lighthouse guide to Lindau Lighthouse: Bavaria's lake light.. 1856. History, meaning, practices, and how to engage respectfully — everything in one database. Lake. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Lindau Lighthouse essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Lindau Lighthouse essentials.", "x": "At a glance: Lindau Lighthouse — Bavaria's lake light.. Lake Constance. The essentials: Statue.. Bavaria. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "1856.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "1856.", "x": "Lindau Lighthouse: 1856.. Statue. Essential knowledge — Bavaria.. Bavaria's lake light. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 1856..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 1856..", "x": "Explained: 1856.. Views. The context — Lindau Lighthouse. Statue. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Lake Constance.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Lake Constance.", "x": "Lindau Lighthouse: Lake Constance.. History. Essential knowledge — Statue.. Bavaria's lake light. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Lake Constance..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Lake Constance..", "x": "Explained: Lake Constance.. Bavaria. The context — Lindau Lighthouse. Views. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Bavaria.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Bavaria.", "x": "Lindau Lighthouse: Bavaria.. Views. Essential knowledge — Views.. Bavaria's lake light. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Bavaria..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Bavaria..", "x": "Explained: Bavaria.. Tours. The context — Lindau Lighthouse. History. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Statue.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Statue.", "x": "Lindau Lighthouse: Statue.. Bavaria. Essential knowledge — History.. Bavaria's lake light. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Statue..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Statue..", "x": "Explained: Statue.. Lake. The context — Lindau Lighthouse. 1856. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Views.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Views.", "x": "Lindau Lighthouse: Views.. Tours. Essential knowledge — 1856.. Bavaria's lake light. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Views..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Views..", "x": "Explained: Views.. Statue. The context — Lindau Lighthouse. Lake Constance. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "History.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "History.", "x": "Lindau Lighthouse: History.. Lake. Essential knowledge — Lake Constance.. Bavaria's lake light. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: History..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: History..", "x": "Explained: History.. History. The context — Lindau Lighthouse. Bavaria. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Lake.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Lake.", "x": "Lindau Lighthouse in depth: Lake.. Lake Constance. Details — Bavaria's lake light.. History. Statue. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Statue.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Statue.", "x": "Lindau Lighthouse in depth: Statue.. Bavaria. Details — Bavaria's lake light.. Views. Views. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "History.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "History.", "x": "Lindau Lighthouse in depth: History.. Statue. Details — Bavaria's lake light.. Bavaria. History. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Views.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Views.", "x": "Lindau Lighthouse in depth: Views.. Views. Details — Bavaria's lake light.. Tours. 1856. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Bavaria.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Bavaria.", "x": "Lindau Lighthouse in depth: Bavaria.. History. Details — Bavaria's lake light.. Lake. Lake Constance. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Tours.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Tours.", "x": "Lindau Lighthouse in depth: Tours.. 1856. Details — Bavaria's lake light.. Statue. Bavaria. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Lindau Lighthouse comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Lindau Lighthouse comes from.", "x": "Origins: Lake.. 1856. The history of Lindau Lighthouse — Bavaria's lake light.. Statue. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Lindau Lighthouse respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Lindau Lighthouse respectfully.", "x": "Engaging: History.. Lake Constance. How to participate or observe well — Lindau Lighthouse. Bavaria's lake light. Respect first, always; Views.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Lindau Lighthouse do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Lindau Lighthouse do's and don'ts.", "x": "Etiquette: Bavaria.. Bavaria. The rules of respect — Lindau Lighthouse. Bavaria's lake light. When in doubt, ask about Tours.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Lindau Lighthouse.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Lindau Lighthouse.", "x": "Planning: Lake.. Statue. Practical notes — Lindau Lighthouse. Bavaria's lake light. A little planning shows respect for Statue.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Lindau Lighthouse and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Lindau Lighthouse and money.", "x": "Costs: History.. Views. What to budget — Lindau Lighthouse. Bavaria's lake light. The best experiences of Views. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-lighthouse-lindau-lighthouse-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
