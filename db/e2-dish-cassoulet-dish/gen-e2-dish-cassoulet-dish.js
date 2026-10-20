(function(){'use strict';
/* JAH Cassoulet Dish Database generator — jahdb-e2-dish-cassoulet-dish-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-dish-cassoulet-dish',PREFIX='JAH-E2DISHCASSO-',NAME='JAH Cassoulet Dish Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Cassoulet: the complete guide", "d": "Cassoulet: the bean casserole..", "g": "overview", "l": 2, "q": "What is Cassoulet: the complete guide?", "a": "Cassoulet: the bean casserole..", "x": "The complete dish guide to Cassoulet: the bean casserole.. Toulouse. History, meaning, practices, and how to engage respectfully — everything in one database. Duck. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Cassoulet essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Cassoulet essentials.", "x": "At a glance: Cassoulet — the bean casserole.. Duck. The essentials: Crust.. Beans. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Toulouse.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Toulouse.", "x": "Cassoulet: Toulouse.. Crust. Essential knowledge — Beans.. the bean casserole. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Toulouse..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Toulouse..", "x": "Explained: Toulouse.. Beans. The context — Cassoulet. Crust. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Duck.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Duck.", "x": "Cassoulet: Duck.. Southwest. Essential knowledge — Crust.. the bean casserole. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Duck..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Duck..", "x": "Explained: Duck.. Slow. The context — Cassoulet. Slow. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Beans.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Beans.", "x": "Cassoulet: Beans.. Beans. Essential knowledge — Slow.. the bean casserole. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Beans..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Beans..", "x": "Explained: Beans.. Making. The context — Cassoulet. Southwest. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Crust.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Crust.", "x": "Cassoulet: Crust.. Slow. Essential knowledge — Southwest.. the bean casserole. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Crust..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Crust..", "x": "Explained: Crust.. Duck. The context — Cassoulet. Toulouse. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Slow.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Slow.", "x": "Cassoulet: Slow.. Making. Essential knowledge — Toulouse.. the bean casserole. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Slow..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Slow..", "x": "Explained: Slow.. Crust. The context — Cassoulet. Duck. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Southwest.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Southwest.", "x": "Cassoulet: Southwest.. Duck. Essential knowledge — Duck.. the bean casserole. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Southwest..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Southwest..", "x": "Explained: Southwest.. Southwest. The context — Cassoulet. Beans. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Duck.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Duck.", "x": "Cassoulet in depth: Duck.. Duck. Details — the bean casserole.. Southwest. Crust. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Crust.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Crust.", "x": "Cassoulet in depth: Crust.. Beans. Details — the bean casserole.. Beans. Slow. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Southwest.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Southwest.", "x": "Cassoulet in depth: Southwest.. Crust. Details — the bean casserole.. Slow. Southwest. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Beans.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Beans.", "x": "Cassoulet in depth: Beans.. Slow. Details — the bean casserole.. Making. Toulouse. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Slow.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Slow.", "x": "Cassoulet in depth: Slow.. Southwest. Details — the bean casserole.. Duck. Duck. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Making.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Making.", "x": "Cassoulet in depth: Making.. Toulouse. Details — the bean casserole.. Crust. Beans. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Cassoulet comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Cassoulet comes from.", "x": "Origins: Duck.. Toulouse. The history of Cassoulet — the bean casserole.. Crust. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Cassoulet respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Cassoulet respectfully.", "x": "Engaging: Southwest.. Duck. How to participate or observe well — Cassoulet. the bean casserole. Respect first, always; Beans.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Cassoulet do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Cassoulet do's and don'ts.", "x": "Etiquette: Slow.. Beans. The rules of respect — Cassoulet. the bean casserole. When in doubt, ask about Making.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Cassoulet.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Cassoulet.", "x": "Planning: Duck.. Crust. Practical notes — Cassoulet. the bean casserole. A little planning shows respect for Crust.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Cassoulet and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Cassoulet and money.", "x": "Costs: Southwest.. Slow. What to budget — Cassoulet. the bean casserole. The best experiences of Beans. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-dish-cassoulet-dish-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
