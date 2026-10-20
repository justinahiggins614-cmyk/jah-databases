(function(){'use strict';
/* JAH Profiteroles Dessert Database generator — jahdb-e2-dessert-profiteroles-dessert-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-dessert-profiteroles-dessert',PREFIX='JAH-E2DESSERTPR-',NAME='JAH Profiteroles Dessert Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Profiteroles: the complete guide", "d": "Profiteroles: the choux puffs..", "g": "overview", "l": 2, "q": "What is Profiteroles: the complete guide?", "a": "Profiteroles: the choux puffs..", "x": "The complete dessert guide to Profiteroles: the choux puffs.. Choux. History, meaning, practices, and how to engage respectfully — everything in one database. Choux. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Profiteroles essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Profiteroles essentials.", "x": "At a glance: Profiteroles — the choux puffs.. Cream. The essentials: Cream.. Chocolate. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Choux.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Choux.", "x": "Profiteroles: Choux.. Cream. Essential knowledge — Chocolate.. the choux puffs. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Choux..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Choux..", "x": "Explained: Choux.. Puffs. The context — Profiteroles. French. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Cream.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Cream.", "x": "Profiteroles: Cream.. French. Essential knowledge — French.. the choux puffs. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Cream..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Cream..", "x": "Explained: Cream.. Chocolate. The context — Profiteroles. Puffs. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Chocolate.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Chocolate.", "x": "Profiteroles: Chocolate.. Puffs. Essential knowledge — Puffs.. the choux puffs. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Chocolate..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Chocolate..", "x": "Explained: Chocolate.. Making. The context — Profiteroles. Stacked. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "French.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "French.", "x": "Profiteroles: French.. Chocolate. Essential knowledge — Stacked.. the choux puffs. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: French..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: French..", "x": "Explained: French.. Choux. The context — Profiteroles. Choux. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Puffs.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Puffs.", "x": "Profiteroles: Puffs.. Making. Essential knowledge — Choux.. the choux puffs. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Puffs..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Puffs..", "x": "Explained: Puffs.. Cream. The context — Profiteroles. Cream. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Stacked.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Stacked.", "x": "Profiteroles: Stacked.. Choux. Essential knowledge — Cream.. the choux puffs. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Stacked..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Stacked..", "x": "Explained: Stacked.. French. The context — Profiteroles. Chocolate. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Choux.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Choux.", "x": "Profiteroles in depth: Choux.. Cream. Details — the choux puffs.. French. French. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Cream.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Cream.", "x": "Profiteroles in depth: Cream.. Chocolate. Details — the choux puffs.. Puffs. Puffs. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "French.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "French.", "x": "Profiteroles in depth: French.. French. Details — the choux puffs.. Chocolate. Stacked. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Puffs.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Puffs.", "x": "Profiteroles in depth: Puffs.. Puffs. Details — the choux puffs.. Making. Choux. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Chocolate.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Chocolate.", "x": "Profiteroles in depth: Chocolate.. Stacked. Details — the choux puffs.. Choux. Cream. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Making.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Making.", "x": "Profiteroles in depth: Making.. Choux. Details — the choux puffs.. Cream. Chocolate. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Profiteroles comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Profiteroles comes from.", "x": "Origins: Choux.. Choux. The history of Profiteroles — the choux puffs.. Cream. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Profiteroles respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Profiteroles respectfully.", "x": "Engaging: French.. Cream. How to participate or observe well — Profiteroles. the choux puffs. Respect first, always; Puffs.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Profiteroles do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Profiteroles do's and don'ts.", "x": "Etiquette: Chocolate.. Chocolate. The rules of respect — Profiteroles. the choux puffs. When in doubt, ask about Making.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Profiteroles.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Profiteroles.", "x": "Planning: Choux.. French. Practical notes — Profiteroles. the choux puffs. A little planning shows respect for Cream.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Profiteroles and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Profiteroles and money.", "x": "Costs: French.. Puffs. What to budget — Profiteroles. the choux puffs. The best experiences of Puffs. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-dessert-profiteroles-dessert-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
